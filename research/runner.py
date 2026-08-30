"""Readable, ordinary-Python orchestration for the iterative research loop."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from time import perf_counter
from typing import Protocol

from research.config import MAX_RESEARCH_ITERATIONS
from research.models import FinalReport, IterationAnalysis, ResearchIteration, ResearchState, Source
from research.research_logger import ResearchLogger

logger = logging.getLogger(__name__)


class Searcher(Protocol):
    def search(self, query: str) -> list[Source]: ...


class Analyzer(Protocol):
    def analyze(self, state: ResearchState, new_sources: list[Source]) -> IterationAnalysis: ...


class Reporter(Protocol):
    def generate(self, state: ResearchState) -> FinalReport: ...


@dataclass(frozen=True)
class ResearchResult:
    state: ResearchState
    report: FinalReport


def normalize_query(query: str) -> str:
    return " ".join(query.lower().split())


def validate_analysis_source_references(
    analysis: IterationAnalysis, state: ResearchState
) -> None:
    """Reject model-created citations that do not exist in the run state."""
    valid_ids = {source.id for source in state.sources}
    cited_ids = {
        source_id
        for finding in analysis.findings
        for evidence in finding.evidence
        for source_id in evidence.source_ids
    }
    cited_ids.update(
        source_id for conflict in analysis.conflicts for source_id in conflict.source_ids
    )
    invalid_ids = sorted(cited_ids - valid_ids)
    if invalid_ids:
        raise ValueError(
            "Iteration analysis cites unknown source ID(s): " + ", ".join(invalid_ids)
        )


class ResearchRunner:
    def __init__(
        self,
        search_client: Searcher,
        analyzer: Analyzer,
        report_generator: Reporter,
        max_iterations: int = MAX_RESEARCH_ITERATIONS,
        research_logger: ResearchLogger | None = None,
    ) -> None:
        self.search_client = search_client
        self.analyzer = analyzer
        self.report_generator = report_generator
        self.max_iterations = max_iterations
        self.research_logger = research_logger
        self.last_state: ResearchState | None = None

    def run(self, question: str) -> ResearchResult:
        question = question.strip()
        if not question:
            raise ValueError("Research question must not be empty")

        state = ResearchState(question=question)
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
            logger.info("Iteration %d/%d", iteration_number, self.max_iterations)
            logger.info("Searching:\n%s", query)
            executed_queries.add(normalize_query(query))

            search_start = perf_counter()
            try:
                retrieved = self.search_client.search(query)
            except Exception as exc:
                self._record_failure(
                    f"{self.search_provider_name()} Search — Iteration {iteration_number}",
                    exc,
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
                permanent = candidate.model_copy(update={"id": f"S{len(state.sources) + 1}"})
                state.sources.append(permanent)
                new_sources.append(permanent)

            logger.info("Added %d new sources.", len(new_sources))
            if self.research_logger:
                self.research_logger.record_search(
                    iteration_number=iteration_number,
                    search_query=query,
                    query_reason=query_reason,
                    results_returned=len(retrieved),
                    new_sources=new_sources,
                    duration=search_duration,
                )

            logger.info("Analyzing evidence...")
            analysis_start = perf_counter()
            try:
                analysis = self.analyzer.analyze(state, new_sources)
                validate_analysis_source_references(analysis, state)
            except Exception as exc:
                self._record_failure(
                    f"OpenAI Evidence Analysis — Iteration {iteration_number}",
                    exc,
                    run_start,
                )
                raise
            analysis_duration = perf_counter() - analysis_start
            if self.research_logger:
                self.research_logger.record_analysis(
                    iteration_number, analysis, analysis_duration
                )
            state.iterations.append(
                ResearchIteration(
                    iteration_number=iteration_number,
                    search_query=query,
                    source_ids=[source.id for source in new_sources],
                    analysis=analysis,
                )
            )

            logger.info(
                "More research needed: %s", "Yes" if analysis.needs_more_research else "No"
            )
            logger.info("Reason:\n%s", analysis.research_reason)

            if not analysis.needs_more_research:
                state.stop_reason = "no_search_results" if not new_sources else "sufficient_evidence"
                self._record_decision(iteration_number, analysis, state.stop_reason)
                break

            if iteration_number == self.max_iterations:
                state.stop_reason = "max_iterations"
                self._record_decision(iteration_number, analysis, state.stop_reason)
                break

            next_query = analysis.next_search_query
            # The Pydantic model guarantees this is non-empty when continuing.
            assert next_query is not None
            if normalize_query(next_query) in executed_queries:
                state.stop_reason = "duplicate_query"
                self._record_decision(iteration_number, analysis, state.stop_reason)
                break

            if self.research_logger:
                self.research_logger.record_decision(
                    iteration_number=iteration_number,
                    continue_research=True,
                    reason=analysis.research_reason,
                    next_search_query=next_query,
                )
            logger.info("Next search:\n%s", next_query)
            query = next_query
            query_reason = analysis.research_reason

        if state.stop_reason is None:
            state.stop_reason = "max_iterations"

        logger.info("Research stopped: %s", state.stop_reason)
        report_start = perf_counter()
        try:
            final_report = self.report_generator.generate(state)
        except Exception as exc:
            self._record_failure("OpenAI Report Generation", exc, run_start)
            raise
        report_duration = perf_counter() - report_start
        if self.research_logger:
            self.research_logger.finish_run(
                state=state,
                report=final_report,
                report_duration=report_duration,
                total_runtime=perf_counter() - run_start,
            )
        return ResearchResult(state=state, report=final_report)

    def _record_decision(
        self,
        iteration_number: int,
        analysis: IterationAnalysis,
        stop_reason: str,
    ) -> None:
        if self.research_logger:
            self.research_logger.record_decision(
                iteration_number=iteration_number,
                continue_research=False,
                reason=analysis.research_reason,
                stop_reason=stop_reason,
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
        if self.research_logger:
            return self.research_logger.search_provider
        return "Web"
