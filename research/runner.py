"""Readable, ordinary-Python orchestration for the iterative research loop."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Protocol

from research.config import MAX_RESEARCH_ITERATIONS
from research.models import FinalReport, IterationAnalysis, ResearchIteration, ResearchState, Source

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
    ) -> None:
        self.search_client = search_client
        self.analyzer = analyzer
        self.report_generator = report_generator
        self.max_iterations = max_iterations

    def run(self, question: str) -> ResearchResult:
        question = question.strip()
        if not question:
            raise ValueError("Research question must not be empty")

        state = ResearchState(question=question)
        query = question
        executed_queries: set[str] = set()
        seen_urls: set[str] = set()

        logger.info("Research question:\n%s", question)
        for iteration_number in range(1, self.max_iterations + 1):
            logger.info("Iteration %d/%d", iteration_number, self.max_iterations)
            logger.info("Searching:\n%s", query)
            executed_queries.add(normalize_query(query))

            retrieved = self.search_client.search(query)
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
            logger.info("Analyzing evidence...")
            analysis = self.analyzer.analyze(state, new_sources)
            validate_analysis_source_references(analysis, state)
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
                break

            if iteration_number == self.max_iterations:
                state.stop_reason = "max_iterations"
                break

            next_query = analysis.next_search_query
            # The Pydantic model guarantees this is non-empty when continuing.
            assert next_query is not None
            if normalize_query(next_query) in executed_queries:
                state.stop_reason = "duplicate_query"
                break

            logger.info("Next search:\n%s", next_query)
            query = next_query

        if state.stop_reason is None:
            state.stop_reason = "max_iterations"

        logger.info("Research stopped: %s", state.stop_reason)
        final_report = self.report_generator.generate(state)
        return ResearchResult(state=state, report=final_report)
