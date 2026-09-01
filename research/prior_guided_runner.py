"""Coverage-aware V0 runner whose planning metadata is never research evidence."""

from __future__ import annotations

import logging
from time import perf_counter
from typing import Protocol

from research.config import MAX_RESEARCH_ITERATIONS
from research.models import (
    FinalReport,
    IterationAnalysis,
    PriorGuidedIterationAnalysis,
    PriorKnowledgeResearchPlan,
    ResearchDimension,
    ResearchDimensionImportance,
    ResearchDimensionStatus,
    ResearchDimensionStatusChange,
    ResearchIteration,
    ResearchState,
    Source,
)
from research.prior_guided_analyzer import validate_dimension_updates
from research.prior_guided_logger import PriorGuidedResearchLogger
from research.runner import (
    Reporter,
    ResearchResult,
    Searcher,
    normalize_query,
    validate_analysis_source_references,
)
from research.versions import PRIOR_GUIDED_SYSTEM_VERSION

logger = logging.getLogger(__name__)


class Planner(Protocol):
    def plan(self, question: str) -> PriorKnowledgeResearchPlan: ...


class PriorGuidedAnalyzer(Protocol):
    def analyze(
        self, state: ResearchState, new_sources: list[Source]
    ) -> PriorGuidedIterationAnalysis: ...


class PriorGuidedResearchRunner:
    def __init__(
        self,
        search_client: Searcher,
        planner: Planner,
        analyzer: PriorGuidedAnalyzer,
        report_generator: Reporter,
        max_iterations: int = MAX_RESEARCH_ITERATIONS,
        research_logger: PriorGuidedResearchLogger | None = None,
    ) -> None:
        self.search_client = search_client
        self.planner = planner
        self.analyzer = analyzer
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
            system_version=PRIOR_GUIDED_SYSTEM_VERSION,
        )
        self.last_state = state
        run_start = perf_counter()
        if self.research_logger:
            self.research_logger.start_run()
            self.research_logger.record_planning_attempt()

        planning_start = perf_counter()
        try:
            plan = self.planner.plan(question)
        except Exception as exc:
            self._record_failure("OpenAI Prior-Knowledge Planning", exc, run_start)
            raise
        state.prior_knowledge_plan = plan
        if self.research_logger:
            self.research_logger.record_plan(plan, perf_counter() - planning_start)

        logger.info("Research question:\n%s", question)
        logger.info("Prior-knowledge coverage plan created with %d dimensions.", len(plan.dimensions))
        query = question
        query_reason = "This is the user's original research question."
        query_target_dimension_id: str | None = None
        executed_queries: set[str] = set()
        seen_urls: set[str] = set()

        for iteration_number in range(1, self.max_iterations + 1):
            state.current_iteration = iteration_number
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
                    iteration_number,
                    query,
                    query_reason,
                    len(retrieved),
                    new_sources,
                    search_duration,
                )

            logger.info("Analyzing evidence against the coverage map...")
            analysis_start = perf_counter()
            try:
                analysis = self.analyzer.analyze(state, new_sources)
                validate_dimension_updates(analysis, plan)
                validate_grounded_prior_analysis(analysis, state)
                changes = apply_dimension_status_updates(plan, analysis)
            except Exception as exc:
                self._record_failure(
                    f"OpenAI Evidence Analysis — Iteration {iteration_number}",
                    exc,
                    run_start,
                )
                raise
            analysis_duration = perf_counter() - analysis_start
            base_analysis = to_iteration_analysis(analysis)
            if self.research_logger:
                self.research_logger.record_analysis(
                    iteration_number, base_analysis, analysis_duration
                )
            state.iterations.append(
                ResearchIteration(
                    iteration_number=iteration_number,
                    search_query=query,
                    source_ids=[source.id for source in new_sources],
                    analysis=base_analysis,
                    search_target_dimension_id=query_target_dimension_id,
                    dimension_status_changes=changes,
                    blocking_conflict=analysis.blocking_conflict,
                )
            )

            unresolved_core = state.unresolved_core_dimensions()
            logger.info(
                "Unresolved CORE dimensions: %s",
                ", ".join(item.id for item in unresolved_core) or "None",
            )

            if iteration_number == self.max_iterations:
                self._stop(
                    state,
                    iteration_number,
                    analysis.research_reason,
                    "max_iterations",
                    changes,
                )
                break

            if (
                not unresolved_core
                and not analysis.blocking_conflict
                and not analysis.needs_more_research
            ):
                self._stop(
                    state,
                    iteration_number,
                    analysis.research_reason,
                    "coverage_sufficient",
                    changes,
                )
                break

            next_target = select_next_dimension(plan, analysis.target_dimension_id)
            must_continue = bool(unresolved_core) or analysis.blocking_conflict
            next_query = choose_next_query(
                analysis,
                next_target,
                executed_queries,
                must_continue=must_continue,
                conflict_fallback_query=(
                    f"{question} conflicting evidence independent comparison"
                    if analysis.blocking_conflict
                    else None
                ),
            )
            if next_query is None:
                stop_reason = "no_search_results" if not new_sources else "duplicate_query"
                self._stop(
                    state,
                    iteration_number,
                    analysis.research_reason,
                    stop_reason,
                    changes,
                )
                break

            if next_target is not None:
                next_target.search_attempts += 1
            decision_reason = analysis.research_reason
            if not analysis.needs_more_research and unresolved_core:
                decision_reason = (
                    "Coverage policy requires continuation because unresolved CORE "
                    "dimensions remain: "
                    + ", ".join(item.id for item in unresolved_core)
                    + ". Analyzer assessment: "
                    + analysis.research_reason
                )
            if self.research_logger:
                self.research_logger.record_decision(
                    iteration_number,
                    continue_research=True,
                    reason=decision_reason,
                    next_search_query=next_query,
                )
                self.research_logger.record_coverage_snapshot(
                    iteration_number,
                    plan.dimensions,
                    changes,
                    next_target.id if next_target is not None else None,
                    decision_reason,
                )
            query = next_query
            query_reason = decision_reason
            query_target_dimension_id = (
                next_target.id if next_target is not None else None
            )

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
                state,
                final_report,
                report_duration,
                perf_counter() - run_start,
            )
        return ResearchResult(state=state, report=final_report)

    def _stop(
        self,
        state: ResearchState,
        iteration_number: int,
        reason: str,
        stop_reason: str,
        changes: list[ResearchDimensionStatusChange],
    ) -> None:
        state.stop_reason = stop_reason
        if self.research_logger:
            self.research_logger.record_decision(
                iteration_number,
                continue_research=False,
                reason=reason,
                stop_reason=stop_reason,
            )
            assert state.prior_knowledge_plan is not None
            self.research_logger.record_coverage_snapshot(
                iteration_number,
                state.prior_knowledge_plan.dimensions,
                changes,
                None,
                reason,
            )

    def _record_failure(
        self, stage: str, error: BaseException, run_start: float
    ) -> None:
        if self.research_logger:
            self.research_logger.record_failure(
                stage, error, perf_counter() - run_start
            )

    def search_provider_name(self) -> str:
        return self.research_logger.search_provider if self.research_logger else "Web"


def to_iteration_analysis(analysis: PriorGuidedIterationAnalysis) -> IterationAnalysis:
    return IterationAnalysis(
        findings=analysis.findings,
        conflicts=analysis.conflicts,
        unresolved_questions=analysis.unresolved_questions,
        needs_more_research=analysis.needs_more_research,
        research_reason=analysis.research_reason,
        next_search_query=analysis.next_search_query,
    )


def validate_grounded_prior_analysis(
    analysis: PriorGuidedIterationAnalysis, state: ResearchState
) -> None:
    validate_analysis_source_references(analysis, state)
    for number, finding in enumerate(analysis.findings, start=1):
        if not finding.evidence:
            raise ValueError(
                f"Prior-guided finding {number} has no retrieved evidence"
            )
        for evidence_number, evidence in enumerate(finding.evidence, start=1):
            if not evidence.source_ids:
                raise ValueError(
                    f"Prior-guided finding {number}, evidence item {evidence_number} "
                    "has no retrieved source IDs"
                )


def apply_dimension_status_updates(
    plan: PriorKnowledgeResearchPlan,
    analysis: PriorGuidedIterationAnalysis,
) -> list[ResearchDimensionStatusChange]:
    validate_dimension_updates(analysis, plan)
    changes: list[ResearchDimensionStatusChange] = []
    for update in analysis.dimension_status_updates:
        dimension = plan.get_dimension(update.dimension_id)
        assert dimension is not None
        previous = dimension.status
        dimension.status = update.status
        dimension.status_reason = update.status_reason
        if previous != dimension.status:
            changes.append(
                ResearchDimensionStatusChange(
                    dimension_id=dimension.id,
                    previous_status=previous,
                    current_status=dimension.status,
                    status_reason=dimension.status_reason,
                )
            )
    return changes


def dimension_priority(dimension: ResearchDimension) -> int | None:
    if (
        dimension.importance == ResearchDimensionImportance.CORE
        and dimension.status == ResearchDimensionStatus.UNRESEARCHED
    ):
        return 0
    if (
        dimension.importance == ResearchDimensionImportance.CORE
        and dimension.status == ResearchDimensionStatus.PARTIAL
    ):
        return 1
    if (
        dimension.importance == ResearchDimensionImportance.SECONDARY
        and dimension.status == ResearchDimensionStatus.UNRESEARCHED
    ):
        return 2
    if (
        dimension.importance == ResearchDimensionImportance.SECONDARY
        and dimension.status == ResearchDimensionStatus.PARTIAL
    ):
        return 3
    return None


def select_next_dimension(
    plan: PriorKnowledgeResearchPlan,
    proposed_id: str | None,
) -> ResearchDimension | None:
    candidates = [
        item for item in plan.dimensions if dimension_priority(item) is not None
    ]
    if not candidates:
        return None
    best_priority = min(dimension_priority(item) for item in candidates)
    preferred = [
        item for item in candidates if dimension_priority(item) == best_priority
    ]
    proposed = plan.get_dimension(proposed_id) if proposed_id else None
    if proposed in preferred:
        return proposed
    return min(preferred, key=lambda item: (item.search_attempts, item.id))


def build_dimension_query(dimension: ResearchDimension) -> str:
    query = f"{dimension.research_question} {dimension.evidence_needed}"
    return " ".join(query.split())[:399].rstrip()


def choose_next_query(
    analysis: PriorGuidedIterationAnalysis,
    target: ResearchDimension | None,
    executed_queries: set[str],
    *,
    must_continue: bool,
    conflict_fallback_query: str | None = None,
) -> str | None:
    proposed = analysis.next_search_query if analysis.needs_more_research else None
    proposed_matches_target = (
        target is None or analysis.target_dimension_id == target.id
    )
    if (
        proposed
        and proposed_matches_target
        and normalize_query(proposed) not in executed_queries
    ):
        return proposed
    if target is not None and (must_continue or analysis.needs_more_research):
        fallback = build_dimension_query(target)
        if fallback and normalize_query(fallback) not in executed_queries:
            return fallback
    if must_continue and conflict_fallback_query:
        fallback = " ".join(conflict_fallback_query.split())[:399].rstrip()
        if fallback and normalize_query(fallback) not in executed_queries:
            return fallback
    return None
