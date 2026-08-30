"""Explicit orchestration for evidence-ledger-v1 research."""

from __future__ import annotations

import logging
from time import perf_counter
from typing import Protocol

from research.config import MAX_RESEARCH_ITERATIONS
from research.decision import validate_decision_target
from research.evidence_processor import apply_evidence_processing_result
from research.ledger_logger import LedgerResearchLogger
from research.models import (
    EvidenceProcessingResult,
    FinalReport,
    LedgerResearchIteration,
    ResearchDecision,
    ResearchState,
    Source,
)
from research.runner import ResearchResult, normalize_query

logger = logging.getLogger(__name__)


class Searcher(Protocol):
    def search(self, query: str) -> list[Source]: ...


class Processor(Protocol):
    def process(
        self, state: ResearchState, new_sources: list[Source]
    ) -> EvidenceProcessingResult: ...


class DecisionMaker(Protocol):
    def decide(self, state: ResearchState) -> ResearchDecision: ...


class Reporter(Protocol):
    def generate(self, state: ResearchState) -> FinalReport: ...


class LedgerResearchRunner:
    def __init__(
        self,
        search_client: Searcher,
        evidence_processor: Processor,
        decision_maker: DecisionMaker,
        report_generator: Reporter,
        max_iterations: int = MAX_RESEARCH_ITERATIONS,
        research_logger: LedgerResearchLogger | None = None,
    ) -> None:
        self.search_client = search_client
        self.evidence_processor = evidence_processor
        self.decision_maker = decision_maker
        self.report_generator = report_generator
        self.max_iterations = max_iterations
        self.research_logger = research_logger
        self.last_state: ResearchState | None = None

    def run(self, question: str) -> ResearchResult:
        question = question.strip()
        if not question:
            raise ValueError("Research question must not be empty")
        state = ResearchState(
            question=question,
            max_iterations=self.max_iterations,
            system_version="evidence-ledger-v1",
        )
        self.last_state = state
        query = question
        query_reason = "This is the user's original research question."
        executed_queries: set[str] = set()
        seen_urls: set[str] = set()
        run_start = perf_counter()
        if self.research_logger:
            self.research_logger.start_run()

        logger.info("Research question:\n%s", question)
        for iteration_number in range(1, self.max_iterations + 1):
            state.current_iteration = iteration_number
            logger.info("Iteration %d/%d", iteration_number, self.max_iterations)
            logger.info("Searching:\n%s", query)
            executed_queries.add(normalize_query(query))

            search_start = perf_counter()
            try:
                retrieved = self.search_client.search(query)
            except Exception as error:
                self._record_failure(
                    f"{self.search_provider_name()} Search — Iteration {iteration_number}",
                    error,
                    run_start,
                )
                raise
            search_duration = perf_counter() - search_start
            logger.info("Retrieved %d results.", len(retrieved))

            new_sources: list[Source] = []
            for candidate in retrieved:
                url_key = candidate.url.strip()
                if not url_key or url_key in seen_urls:
                    continue
                seen_urls.add(url_key)
                permanent = candidate.model_copy(
                    update={"id": f"S{len(state.sources) + 1}"}
                )
                state.sources.append(permanent)
                new_sources.append(permanent)
            logger.info("Added %d new sources.", len(new_sources))
            if self.research_logger:
                self.research_logger.record_search(
                    iteration_number,
                    query,
                    query_reason,
                    len(retrieved),
                    new_sources,
                    search_duration,
                )

            logger.info("Processing evidence into the ledger...")
            processing_start = perf_counter()
            try:
                processing_result = self.evidence_processor.process(state, new_sources)
                ledger_updates = apply_evidence_processing_result(
                    state, processing_result, iteration_number
                )
            except Exception as error:
                self._record_failure(
                    f"OpenAI Evidence Processing — Iteration {iteration_number}",
                    error,
                    run_start,
                )
                raise
            processing_duration = perf_counter() - processing_start
            ledger_iteration = LedgerResearchIteration(
                iteration_number=iteration_number,
                search_query=query,
                source_ids=[source.id for source in new_sources],
                processing_result=processing_result,
                ledger_updates=ledger_updates,
            )
            state.ledger_iterations.append(ledger_iteration)
            if self.research_logger:
                self.research_logger.record_processing(
                    iteration_number,
                    processing_result,
                    ledger_updates,
                    state,
                    processing_duration,
                )

            if iteration_number == self.max_iterations:
                decision = ResearchDecision(
                    needs_more_research=False,
                    reason="The maximum research iteration budget was reached.",
                )
                ledger_iteration.decision = decision
                state.stop_reason = "max_iterations"
                self._record_decision(
                    iteration_number,
                    decision,
                    duration=0.0,
                    model_call=False,
                    stop_reason=state.stop_reason,
                )
                break

            logger.info("Deciding the next research action...")
            decision_start = perf_counter()
            try:
                decision = self.decision_maker.decide(state)
                validate_decision_target(decision, state)
            except Exception as error:
                self._record_failure(
                    f"OpenAI Research Decision — Iteration {iteration_number}",
                    error,
                    run_start,
                )
                raise
            decision_duration = perf_counter() - decision_start
            ledger_iteration.decision = decision
            logger.info(
                "More research needed: %s",
                "Yes" if decision.needs_more_research else "No",
            )
            logger.info("Reason:\n%s", decision.reason)

            if not decision.needs_more_research:
                state.stop_reason = (
                    "no_search_results" if not new_sources else "sufficient_evidence"
                )
                self._record_decision(
                    iteration_number,
                    decision,
                    decision_duration,
                    model_call=True,
                    stop_reason=state.stop_reason,
                )
                break

            next_query = decision.next_search_query
            assert next_query is not None
            if normalize_query(next_query) in executed_queries:
                state.stop_reason = "duplicate_query"
                stop_decision = decision.model_copy(
                    update={
                        "needs_more_research": False,
                        "reason": (
                            "The proposed next query duplicated a query already executed. "
                            + decision.reason
                        ),
                        "target_type": None,
                        "target_id": None,
                        "next_search_query": None,
                    }
                )
                ledger_iteration.decision = stop_decision
                self._record_decision(
                    iteration_number,
                    stop_decision,
                    decision_duration,
                    model_call=True,
                    stop_reason=state.stop_reason,
                )
                break

            self._record_decision(
                iteration_number,
                decision,
                decision_duration,
                model_call=True,
            )
            logger.info("Next search:\n%s", next_query)
            query = next_query
            query_reason = decision.reason

        if state.stop_reason is None:
            state.stop_reason = "max_iterations"

        logger.info("Research stopped: %s", state.stop_reason)
        report_start = perf_counter()
        try:
            final_report = self.report_generator.generate(state)
        except Exception as error:
            self._record_failure("OpenAI Ledger Report Generation", error, run_start)
            raise
        report_duration = perf_counter() - report_start
        if self.research_logger:
            self.research_logger.finish_run(
                state,
                final_report,
                report_duration,
                perf_counter() - run_start,
            )
        return ResearchResult(state=state, report=final_report)

    def _record_decision(
        self,
        iteration_number: int,
        decision: ResearchDecision,
        duration: float,
        model_call: bool,
        stop_reason: str | None = None,
    ) -> None:
        if self.research_logger:
            self.research_logger.record_decision(
                iteration_number,
                decision,
                duration,
                model_call,
                stop_reason,
            )

    def _record_failure(
        self, stage: str, error: BaseException, run_start: float
    ) -> None:
        if self.research_logger:
            self.research_logger.record_failure(
                stage=stage,
                error=error,
                total_runtime=perf_counter() - run_start,
            )

    def search_provider_name(self) -> str:
        return self.research_logger.search_provider if self.research_logger else "Web"
