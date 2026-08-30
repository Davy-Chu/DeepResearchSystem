from collections.abc import Iterable

import pytest

from research.models import FinalReport, IterationAnalysis, ResearchState, Source
from research.research_logger import ResearchLogger
from research.runner import ResearchRunner


def source(url: str, title: str = "Source") -> Source:
    return Source(id="", title=title, url=url, content="Relevant evidence", score=0.8)


def analysis(more: bool, next_query: str | None = None) -> IterationAnalysis:
    return IterationAnalysis(
        findings=[],
        conflicts=[],
        unresolved_questions=[] if not more else ["A gap remains"],
        needs_more_research=more,
        research_reason="More evidence is needed." if more else "Evidence is sufficient.",
        next_search_query=next_query,
    )


class FakeSearch:
    def __init__(self, results: Iterable[list[Source]]) -> None:
        self.results = iter(results)
        self.queries: list[str] = []

    def search(self, query: str) -> list[Source]:
        self.queries.append(query)
        return next(self.results)


class FakeAnalyzer:
    def __init__(self, analyses: Iterable[IterationAnalysis]) -> None:
        self.analyses = iter(analyses)
        self.calls = 0

    def analyze(self, state: ResearchState, new_sources: list[Source]) -> IterationAnalysis:
        self.calls += 1
        return next(self.analyses)


class FailingAnalyzer:
    def analyze(self, state: ResearchState, new_sources: list[Source]) -> IterationAnalysis:
        raise RuntimeError("analysis unavailable")


class FakeReporter:
    def generate(self, state: ResearchState) -> FinalReport:
        return FinalReport(
            question=state.question,
            summary="Test summary.",
            findings=[],
            conflicts_and_uncertainties=[],
            remaining_gaps=state.all_unresolved_questions(),
            conclusion="Test conclusion.",
        )


def run_with(search: FakeSearch, analyzer: FakeAnalyzer):
    return ResearchRunner(search, analyzer, FakeReporter()).run("Original question")


def test_runner_stops_when_evidence_is_sufficient() -> None:
    search = FakeSearch([[source("https://example.com/1")]])
    result = run_with(search, FakeAnalyzer([analysis(False)]))
    assert search.queries == ["Original question"]
    assert result.state.stop_reason == "sufficient_evidence"


def test_runner_performs_another_iteration() -> None:
    search = FakeSearch(
        [[source("https://example.com/1")], [source("https://example.com/2")]]
    )
    analyzer = FakeAnalyzer([analysis(True, "focused gap query"), analysis(False)])
    result = run_with(search, analyzer)
    assert search.queries == ["Original question", "focused gap query"]
    assert len(result.state.iterations) == 2


def test_maximum_iteration_guard() -> None:
    search = FakeSearch(
        [
            [source("https://example.com/1")],
            [source("https://example.com/2")],
            [source("https://example.com/3")],
        ]
    )
    analyzer = FakeAnalyzer(
        [
            analysis(True, "query two"),
            analysis(True, "query three"),
            analysis(True, "query four"),
        ]
    )
    result = run_with(search, analyzer)
    assert len(search.queries) == 3
    assert result.state.stop_reason == "max_iterations"


def test_duplicate_query_guard_normalizes_case_and_whitespace() -> None:
    search = FakeSearch([[source("https://example.com/1")]])
    analyzer = FakeAnalyzer([analysis(True, "  ORIGINAL   QUESTION  ")])
    result = run_with(search, analyzer)
    assert len(search.queries) == 1
    assert result.state.stop_reason == "duplicate_query"


def test_source_deduplication_by_url() -> None:
    search = FakeSearch(
        [
            [source("https://example.com/same")],
            [source("https://example.com/same"), source("https://example.com/new")],
        ]
    )
    analyzer = FakeAnalyzer([analysis(True, "second query"), analysis(False)])
    result = run_with(search, analyzer)
    assert [item.id for item in result.state.sources] == ["S1", "S2"]
    assert [item.url for item in result.state.sources] == [
        "https://example.com/same",
        "https://example.com/new",
    ]
    assert result.state.iterations[1].source_ids == ["S2"]


def test_no_results_stops_honestly_when_analyzer_has_no_next_query() -> None:
    search = FakeSearch([[]])
    result = run_with(search, FakeAnalyzer([analysis(False)]))
    assert result.state.stop_reason == "no_search_results"


def test_runner_populates_human_readable_logger_without_changing_flow() -> None:
    search = FakeSearch(
        [[source("https://example.com/1")], [source("https://example.com/2")]]
    )
    analyzer = FakeAnalyzer([analysis(True, "focused gap query"), analysis(False)])
    research_log = ResearchLogger("Original question", "test-model", 3)

    result = ResearchRunner(
        search,
        analyzer,
        FakeReporter(),
        research_logger=research_log,
    ).run("Original question")

    assert result.state.stop_reason == "sufficient_evidence"
    assert research_log.status == "Completed"
    assert len(research_log.iterations) == 2
    assert research_log.iterations[0].query_reason == (
        "This is the user's original research question."
    )
    assert research_log.iterations[1].query_reason == "More evidence is needed."
    assert research_log.iterations[0].continue_research is True
    assert research_log.iterations[1].continue_research is False


def test_runner_records_partial_log_state_when_analysis_fails() -> None:
    research_log = ResearchLogger("Original question", "test-model", 3)
    runner = ResearchRunner(
        FakeSearch([[source("https://example.com/1")]]),
        FailingAnalyzer(),
        FakeReporter(),
        research_logger=research_log,
    )

    with pytest.raises(RuntimeError, match="analysis unavailable"):
        runner.run("Original question")

    assert research_log.status == "Failed"
    assert research_log.failure_stage == "OpenAI Evidence Analysis — Iteration 1"
    assert len(research_log.iterations) == 1
    assert "Analysis did not complete" in research_log.render_markdown()
