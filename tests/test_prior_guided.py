from __future__ import annotations

import json
from collections.abc import Iterable
from types import SimpleNamespace

import pytest

from main import build_parser as build_main_parser
from research.models import (
    Confidence,
    EvidenceItem,
    FinalReport,
    Finding,
    PriorGuidedIterationAnalysis,
    PriorKnowledgePlanProposal,
    PriorKnowledgeResearchPlan,
    ResearchDimension,
    ResearchDimensionImportance,
    ResearchDimensionProposal,
    ResearchDimensionStatus,
    ResearchDimensionStatusUpdate,
    ResearchState,
    Source,
)
from research.prior_guided_logger import PriorGuidedResearchLogger
from research.prior_guided_analyzer import validate_dimension_updates
from research.prior_guided_runner import (
    PriorGuidedResearchRunner,
    select_next_dimension,
    validate_grounded_prior_analysis,
)
from research.prior_knowledge_planner import PriorKnowledgeResearchPlanner
from research.report import _prior_guided_report_payload, build_trace, validate_source_references
from research.versions import (
    CANONICAL_SYSTEM_VERSIONS,
    EXPERIMENTAL_SYSTEM_VERSIONS,
    PRIOR_GUIDED_SYSTEM_VERSION,
)
from scripts.run_fixture_suite import (
    MAX_RESEARCH_OPENAI_CALLS,
    MAX_TAVILY_CALLS,
    build_parser as build_suite_parser,
)


def plan() -> PriorKnowledgeResearchPlan:
    return PriorKnowledgeResearchPlan(
        dimensions=[
            ResearchDimension(
                id="D1",
                title="First core dimension",
                research_question="What evidence addresses the first core dimension?",
                why_it_matters="It is necessary to answer the question.",
                evidence_needed="Direct independent evidence.",
                importance=ResearchDimensionImportance.CORE,
            ),
            ResearchDimension(
                id="D2",
                title="Second core dimension",
                research_question="What evidence addresses the second core dimension?",
                why_it_matters="It prevents a one-sided answer.",
                evidence_needed="Comparative empirical evidence.",
                importance=ResearchDimensionImportance.CORE,
            ),
            ResearchDimension(
                id="D3",
                title="Secondary context",
                research_question="What secondary context is useful?",
                why_it_matters="It adds context.",
                evidence_needed="Relevant contextual evidence.",
                importance=ResearchDimensionImportance.SECONDARY,
            ),
            ResearchDimension(
                id="D4",
                title="Limitations",
                research_question="What limitations should be investigated?",
                why_it_matters="It bounds the conclusion.",
                evidence_needed="Evidence about limitations.",
                importance=ResearchDimensionImportance.SECONDARY,
            ),
        ],
        synthesis_requirements=["Compare the core dimensions."],
    )


def proposal() -> PriorKnowledgePlanProposal:
    return PriorKnowledgePlanProposal(
        dimensions=[
            ResearchDimensionProposal(
                title=item.title,
                research_question=item.research_question,
                why_it_matters=item.why_it_matters,
                evidence_needed=item.evidence_needed,
                importance=item.importance,
            )
            for item in plan().dimensions
        ],
        synthesis_requirements=["Compare the core dimensions."],
    )


def updates(
    d1: ResearchDimensionStatus,
    d2: ResearchDimensionStatus,
    d3: ResearchDimensionStatus = ResearchDimensionStatus.SUFFICIENT,
    d4: ResearchDimensionStatus = ResearchDimensionStatus.SUFFICIENT,
) -> list[ResearchDimensionStatusUpdate]:
    statuses = (d1, d2, d3, d4)
    return [
        ResearchDimensionStatusUpdate(
            dimension_id=f"D{index}",
            status=status,
            status_reason="Status is based only on retrieved evidence.",
        )
        for index, status in enumerate(statuses, start=1)
    ]


def analysis(
    dimension_updates: list[ResearchDimensionStatusUpdate],
    *,
    more: bool = False,
    query: str | None = None,
    target: str | None = None,
    findings: list[Finding] | None = None,
    blocking_conflict: bool = False,
) -> PriorGuidedIterationAnalysis:
    return PriorGuidedIterationAnalysis(
        findings=findings or [],
        conflicts=[],
        unresolved_questions=[],
        needs_more_research=more,
        research_reason="Evidence-only assessment.",
        next_search_query=query,
        dimension_status_updates=dimension_updates,
        target_dimension_id=target,
        blocking_conflict=blocking_conflict,
    )


def source(number: int) -> Source:
    return Source(
        id="",
        title=f"Source {number}",
        url=f"https://example.com/{number}",
        content="Retrieved external evidence.",
    )


class FakePlanner:
    def __init__(self, value: PriorKnowledgeResearchPlan) -> None:
        self.value = value
        self.calls: list[str] = []

    def plan(self, question: str) -> PriorKnowledgeResearchPlan:
        self.calls.append(question)
        return self.value


class FakeSearch:
    def __init__(self, results: Iterable[list[Source]]) -> None:
        self.results = iter(results)
        self.queries: list[str] = []

    def search(self, query: str) -> list[Source]:
        self.queries.append(query)
        return next(self.results)


class FakeAnalyzer:
    def __init__(self, values: Iterable[PriorGuidedIterationAnalysis]) -> None:
        self.values = iter(values)
        self.calls = 0

    def analyze(
        self, state: ResearchState, new_sources: list[Source]
    ) -> PriorGuidedIterationAnalysis:
        self.calls += 1
        return next(self.values)


class FakeReporter:
    def generate(self, state: ResearchState) -> FinalReport:
        return FinalReport(
            question=state.question,
            summary="Evidence-only summary.",
            findings=[],
            conflicts_and_uncertainties=[],
            remaining_gaps=state.all_unresolved_questions(),
            conclusion="Evidence-only conclusion.",
        )


def run(
    analyses: list[PriorGuidedIterationAnalysis],
    *,
    max_iterations: int = 10,
    logger: PriorGuidedResearchLogger | None = None,
):
    search = FakeSearch([[source(index)] for index in range(1, len(analyses) + 1)])
    planner = FakePlanner(plan())
    result = PriorGuidedResearchRunner(
        search,
        planner,
        FakeAnalyzer(analyses),
        FakeReporter(),
        max_iterations=max_iterations,
        research_logger=logger,
    ).run("Original question")
    return result, search, planner


def test_planner_receives_only_question_and_has_no_answer_or_evidence_fields() -> None:
    calls: list[dict[str, object]] = []

    class Responses:
        def parse(self, **kwargs: object) -> SimpleNamespace:
            calls.append(kwargs)
            return SimpleNamespace(output_parsed=proposal())

    planner = PriorKnowledgeResearchPlanner(
        "unused", "test-model", client=SimpleNamespace(responses=Responses())
    )
    result = planner.plan("  Original question only  ")

    assert len(calls) == 1
    assert calls[0]["reasoning"] == {"effort": "low"}
    assert calls[0]["text_format"] is PriorKnowledgePlanProposal
    assert calls[0]["input"][1]["content"] == "Original question only"  # type: ignore[index]
    assert [item.id for item in result.dimensions] == ["D1", "D2", "D3", "D4"]
    schema_fields = set(PriorKnowledgePlanProposal.model_json_schema()["properties"])
    assert schema_fields == {"dimensions", "synthesis_requirements"}
    dimension_fields = set(ResearchDimensionProposal.model_json_schema()["properties"])
    assert not dimension_fields & {
        "evidence",
        "source_ids",
        "confidence",
        "answer",
        "claims",
        "final_report",
    }


def test_first_search_is_original_question_and_planning_adds_no_tavily_call() -> None:
    result, search, planner = run(
        [
            analysis(
                updates(
                    ResearchDimensionStatus.SUFFICIENT,
                    ResearchDimensionStatus.SUFFICIENT,
                )
            )
        ]
    )
    assert planner.calls == ["Original question"]
    assert search.queries == ["Original question"]
    assert result.state.stop_reason == "coverage_sufficient"


def test_unresearched_core_dimension_forces_continuation() -> None:
    result, search, _ = run(
        [
            analysis(
                updates(
                    ResearchDimensionStatus.SUFFICIENT,
                    ResearchDimensionStatus.UNRESEARCHED,
                )
            ),
            analysis(
                updates(
                    ResearchDimensionStatus.SUFFICIENT,
                    ResearchDimensionStatus.SUFFICIENT,
                )
            ),
        ],
        max_iterations=3,
    )
    assert len(search.queries) == 2
    assert "second core dimension" in search.queries[1].lower()
    assert result.state.stop_reason == "coverage_sufficient"
    assert result.state.prior_knowledge_plan is not None
    assert result.state.prior_knowledge_plan.get_dimension("D2").search_attempts == 1  # type: ignore[union-attr]


def test_secondary_gap_does_not_block_early_stop() -> None:
    result, search, _ = run(
        [
            analysis(
                updates(
                    ResearchDimensionStatus.SUFFICIENT,
                    ResearchDimensionStatus.SUFFICIENT,
                    ResearchDimensionStatus.PARTIAL,
                )
            )
        ]
    )
    assert len(search.queries) == 1
    assert result.state.stop_reason == "coverage_sufficient"


def test_blocking_conflict_forces_continuation_after_core_coverage() -> None:
    sufficient = updates(
        ResearchDimensionStatus.SUFFICIENT,
        ResearchDimensionStatus.SUFFICIENT,
    )
    result, search, _ = run(
        [
            analysis(sufficient, blocking_conflict=True),
            analysis(sufficient),
        ],
        max_iterations=3,
    )
    assert len(search.queries) == 2
    assert "conflicting evidence" in search.queries[1]
    assert result.state.stop_reason == "coverage_sufficient"


def test_search_targeting_prefers_unresearched_core_over_partial_core() -> None:
    value = plan()
    value.get_dimension("D1").status = ResearchDimensionStatus.PARTIAL  # type: ignore[union-attr]
    value.get_dimension("D2").status = ResearchDimensionStatus.UNRESEARCHED  # type: ignore[union-attr]
    assert select_next_dimension(value, "D1").id == "D2"  # type: ignore[union-attr]


def test_model_cannot_omit_or_fabricate_dimension_ids() -> None:
    incomplete = analysis(
        updates(
            ResearchDimensionStatus.SUFFICIENT,
            ResearchDimensionStatus.SUFFICIENT,
        )[:-1]
    )
    with pytest.raises(ValueError, match="must cover the plan"):
        validate_dimension_updates(incomplete, plan())


def test_planning_does_not_increase_tavily_budget() -> None:
    unresolved = updates(
        ResearchDimensionStatus.UNRESEARCHED,
        ResearchDimensionStatus.UNRESEARCHED,
        ResearchDimensionStatus.UNRESEARCHED,
        ResearchDimensionStatus.UNRESEARCHED,
    )
    result, search, planner = run(
        [analysis(unresolved), analysis(unresolved), analysis(unresolved)],
        max_iterations=3,
    )
    assert len(planner.calls) == 1
    assert len(search.queries) == 3
    assert result.state.stop_reason == "max_iterations"


def test_planner_text_cannot_be_an_uncited_evidence_finding() -> None:
    unsupported = Finding(
        claim="Fact X is true.",
        evidence=[],
        confidence=Confidence.HIGH,
        confidence_reason="It appeared in planning metadata.",
    )
    state = ResearchState(
        question="Question",
        prior_knowledge_plan=plan(),
        system_version=PRIOR_GUIDED_SYSTEM_VERSION,
    )
    with pytest.raises(ValueError, match="no retrieved evidence"):
        validate_grounded_prior_analysis(
            analysis(
                updates(
                    ResearchDimensionStatus.UNRESEARCHED,
                    ResearchDimensionStatus.UNRESEARCHED,
                ),
                findings=[unsupported],
            ),
            state,
        )

    invalid_report = FinalReport(
        question="Question",
        summary="Unsupported.",
        findings=[unsupported],
        conflicts_and_uncertainties=[],
        remaining_gaps=[],
        conclusion="Unsupported.",
    )
    with pytest.raises(ValueError, match="has no evidence items"):
        validate_source_references(invalid_report, state)


def test_report_payload_excludes_prior_plan_from_factual_state() -> None:
    value = plan()
    value.dimensions[0].why_it_matters = "UNIQUE PRIOR PLANNING PHRASE"
    state = ResearchState(
        question="Question",
        prior_knowledge_plan=value,
        system_version=PRIOR_GUIDED_SYSTEM_VERSION,
    )
    payload = json.dumps(_prior_guided_report_payload(state))
    assert "UNIQUE PRIOR PLANNING PHRASE" not in payload
    assert "prior_knowledge_plan" not in payload


def test_trace_and_log_keep_planning_separate_and_record_diagnostics() -> None:
    logger = PriorGuidedResearchLogger("Original question", "test-model", 3)
    result, _, _ = run(
        [
            analysis(
                updates(
                    ResearchDimensionStatus.SUFFICIENT,
                    ResearchDimensionStatus.SUFFICIENT,
                )
            )
        ],
        max_iterations=3,
        logger=logger,
    )
    trace = build_trace(result.state, "test-model", 3, result.report)
    assert trace["system_version"] == PRIOR_GUIDED_SYSTEM_VERSION
    assert trace["prior_knowledge_plan"]["dimensions"][0]["id"] == "D1"
    assert trace["evidence_ledger"] == {"claims": []}
    assert trace["coverage_diagnostics"] == {
        "core_dimensions": 2,
        "core_sufficient": 2,
        "core_partial": 0,
        "core_unresearched": 0,
    }
    rendered = logger.render_markdown()
    assert "## Prior-Knowledge Coverage Plan" in rendered
    assert "## Coverage Map After Iteration 1" in rendered
    assert "Planner output is planning metadata, not evidence." in rendered
    assert "**OpenAI Calls:** 3" in rendered


def test_mode_is_experimental_and_fixture_suite_has_matching_budgets() -> None:
    assert build_main_parser().parse_args(
        ["Question", "--mode", "prior-guided"]
    ).mode == "prior-guided"
    assert build_suite_parser().parse_args(
        ["prior-guided", "--dry-run"]
    ).architecture == "prior-guided"
    assert PRIOR_GUIDED_SYSTEM_VERSION in EXPERIMENTAL_SYSTEM_VERSIONS
    assert PRIOR_GUIDED_SYSTEM_VERSION not in CANONICAL_SYSTEM_VERSIONS
    assert MAX_TAVILY_CALLS["prior-guided"] == MAX_TAVILY_CALLS["baseline"] == 10
    assert MAX_RESEARCH_OPENAI_CALLS["prior-guided"] == 12
