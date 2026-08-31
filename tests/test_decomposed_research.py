from __future__ import annotations

import json
from types import SimpleNamespace

import pytest
from pydantic import ValidationError

from research.decomposer import QuestionDecomposer, refresh_subquestion_statuses
from research.evidence_processor import apply_evidence_processing_result
from research.ledger_logger import LedgerResearchLogger
from research.ledger_runner import LedgerResearchRunner
from research.models import (
    ClaimStatus,
    ClaimUpdate,
    Confidence,
    DecisionTargetType,
    EvidenceItem,
    EvidenceProcessingResult,
    EvidenceRelation,
    EvidenceRelationType,
    EvidenceStrength,
    FinalReport,
    Finding,
    GapImportance,
    LedgerFinalReport,
    LedgerReportFinding,
    NewClaim,
    NewGap,
    QuestionDecomposition,
    ResearchDecision,
    ResearchPlan,
    ResearchState,
    Source,
    SubQuestion,
    SubQuestionImportance,
    SubQuestionProposal,
    SubQuestionStatus,
)
from research.report import build_trace, validate_ledger_report
from research.subquestion_decision import (
    SubquestionResearchDecisionMaker,
    validate_subquestion_decision_target,
)


def plan() -> ResearchPlan:
    return ResearchPlan(
        subquestions=[
            SubQuestion(
                id="SQ1",
                question="What does the strongest evidence show?",
                importance=SubQuestionImportance.CORE,
                success_criteria="Find direct evidence.",
            ),
            SubQuestion(
                id="SQ2",
                question="What explains disagreement?",
                importance=SubQuestionImportance.CORE,
                success_criteria="Compare conflicting studies.",
            ),
            SubQuestion(
                id="SQ3",
                question="What secondary context matters?",
                importance=SubQuestionImportance.SECONDARY,
                success_criteria="Identify useful context.",
            ),
        ],
        synthesis_requirements=["Compare the evidence types."],
        output_requirements=["Include a concise table."],
    )


def source(source_id: str = "S1") -> Source:
    return Source(
        id=source_id,
        title=source_id,
        url=f"https://example.com/{source_id}",
        content=f"raw-{source_id}",
    )


def relation(source_id: str = "S1") -> EvidenceRelation:
    return EvidenceRelation(
        source_id=source_id,
        relation=EvidenceRelationType.SUPPORTS,
        summary="Direct evidence.",
        strength=EvidenceStrength.DIRECT,
    )


def claim(status: ClaimStatus, subquestion_id: str = "SQ1") -> NewClaim:
    return NewClaim(
        claim="Evidence-backed claim.",
        supporting_evidence=[relation()],
        confidence=Confidence.HIGH,
        confidence_reason="Direct evidence is available.",
        status=status,
        related_subquestion_ids=[subquestion_id],
    )


def test_decomposer_uses_only_original_question_and_assigns_stable_ids() -> None:
    parsed = QuestionDecomposition(
        subquestions=[
            SubQuestionProposal(
                question="First?",
                importance=SubQuestionImportance.CORE,
                success_criteria="Criterion one.",
            ),
            SubQuestionProposal(
                question="Second?",
                importance=SubQuestionImportance.SECONDARY,
                success_criteria="Criterion two.",
            ),
        ],
        synthesis_requirements=["Synthesize."],
        output_requirements=["Use a table."],
    )
    calls: list[dict[str, object]] = []

    class Responses:
        def parse(self, **kwargs: object) -> SimpleNamespace:
            calls.append(kwargs)
            return SimpleNamespace(output_parsed=parsed)

    decomposer = QuestionDecomposer(
        "unused", "test-model", client=SimpleNamespace(responses=Responses())
    )
    result = decomposer.decompose("  Original question?  ")

    assert [item.id for item in result.subquestions] == ["SQ1", "SQ2"]
    assert calls[0]["reasoning"] == {"effort": "low"}
    assert calls[0]["text_format"] is QuestionDecomposition
    assert calls[0]["input"][1]["content"] == "Original question?"  # type: ignore[index]


def test_failed_decomposition_is_counted_as_an_openai_call() -> None:
    logger = LedgerResearchLogger(
        "Question",
        "test-model",
        3,
        system_version="evidence-ledger-decomposer-v1",
    )
    logger.start_run()
    logger.record_decomposition_attempt()
    logger.record_failure("OpenAI Question Decomposition", RuntimeError("failed"))
    rendered = logger.render_markdown()
    assert "**OpenAI Calls:** 1" in rendered
    assert "| Question Decomposition | 1 |" in rendered


def test_decomposition_rejects_too_few_too_many_and_duplicate_questions() -> None:
    proposal = SubQuestionProposal(
        question="Only?",
        importance=SubQuestionImportance.CORE,
        success_criteria="Answer it.",
    )
    with pytest.raises(ValidationError):
        QuestionDecomposition(subquestions=[proposal])
    with pytest.raises(ValidationError):
        QuestionDecomposition(subquestions=[proposal] * 7)
    with pytest.raises(ValidationError, match="unique"):
        QuestionDecomposition(subquestions=[proposal, proposal])


def test_state_helpers_and_atomic_subquestion_validation() -> None:
    state = ResearchState(question="Question", research_plan=plan(), sources=[source()])
    invalid = EvidenceProcessingResult(
        new_claims=[claim(ClaimStatus.SUPPORTED)],
        new_gaps=[
            NewGap(
                description="Invalid association.",
                importance=GapImportance.HIGH,
                related_subquestion_ids=["SQ99"],
            )
        ],
    )
    with pytest.raises(ValueError, match="unknown subquestion.*SQ99"):
        apply_evidence_processing_result(state, invalid, 1)
    assert state.evidence_ledger.claims == []
    assert state.research_gaps == []

    apply_evidence_processing_result(
        state,
        EvidenceProcessingResult(new_claims=[claim(ClaimStatus.SUPPORTED)]),
        1,
    )
    assert [item.id for item in state.core_subquestions()] == ["SQ1", "SQ2"]
    assert [item.id for item in state.claims_for("SQ1")] == ["C1"]
    assert state.gaps_for("SQ1") == []


def test_claim_update_unions_subquestion_associations() -> None:
    state = ResearchState(question="Question", research_plan=plan(), sources=[source()])
    apply_evidence_processing_result(
        state,
        EvidenceProcessingResult(new_claims=[claim(ClaimStatus.WEAK)]),
        1,
    )
    apply_evidence_processing_result(
        state,
        EvidenceProcessingResult(
            claim_updates=[
                ClaimUpdate(
                    existing_claim_id="C1",
                    updated_confidence=Confidence.HIGH,
                    updated_confidence_reason="Now supported.",
                    updated_status=ClaimStatus.SUPPORTED,
                    related_subquestion_ids=["SQ2", "SQ1"],
                )
            ]
        ),
        2,
    )
    assert state.evidence_ledger.claims[0].related_subquestion_ids == ["SQ1", "SQ2"]


@pytest.mark.parametrize(
    ("claim_status", "gap_importance", "expected"),
    [
        (ClaimStatus.CONFLICTING, None, SubQuestionStatus.CONFLICTING),
        (ClaimStatus.WEAK, None, SubQuestionStatus.PARTIAL),
        (ClaimStatus.SUPPORTED, GapImportance.HIGH, SubQuestionStatus.PARTIAL),
        (ClaimStatus.SUPPORTED, GapImportance.LOW, SubQuestionStatus.SUFFICIENT),
        (ClaimStatus.SUPPORTED, None, SubQuestionStatus.SUFFICIENT),
    ],
)
def test_deterministic_status_rules(
    claim_status: ClaimStatus,
    gap_importance: GapImportance | None,
    expected: SubQuestionStatus,
) -> None:
    state = ResearchState(question="Question", research_plan=plan(), sources=[source()])
    gaps = (
        [
            NewGap(
                description="A linked gap.",
                importance=gap_importance,
                related_subquestion_ids=["SQ1"],
            )
        ]
        if gap_importance is not None
        else []
    )
    apply_evidence_processing_result(
        state,
        EvidenceProcessingResult(new_claims=[claim(claim_status)], new_gaps=gaps),
        1,
    )
    refresh_subquestion_statuses(state)
    assert state.get_subquestion("SQ1").status == expected  # type: ignore[union-attr]
    assert state.get_subquestion("SQ2").status == SubQuestionStatus.UNRESEARCHED  # type: ignore[union-attr]
    assert "%" not in state.get_subquestion("SQ1").status_reason  # type: ignore[union-attr]


def test_status_transitions_partial_to_sufficient_to_conflicting() -> None:
    state = ResearchState(
        question="Question", research_plan=plan(), sources=[source(), source("S2")]
    )
    apply_evidence_processing_result(
        state,
        EvidenceProcessingResult(
            new_claims=[claim(ClaimStatus.WEAK)],
            new_gaps=[
                NewGap(
                    description="Important gap.",
                    importance=GapImportance.HIGH,
                    related_subquestion_ids=["SQ1"],
                )
            ],
        ),
        1,
    )
    assert refresh_subquestion_statuses(state)[0].current_status == SubQuestionStatus.PARTIAL

    apply_evidence_processing_result(
        state,
        EvidenceProcessingResult(
            claim_updates=[
                ClaimUpdate(
                    existing_claim_id="C1",
                    updated_confidence=Confidence.HIGH,
                    updated_confidence_reason="The evidence now supports the claim.",
                    updated_status=ClaimStatus.SUPPORTED,
                )
            ],
            resolved_gap_ids=["G1"],
        ),
        2,
    )
    assert refresh_subquestion_statuses(state)[0].current_status == SubQuestionStatus.SUFFICIENT

    apply_evidence_processing_result(
        state,
        EvidenceProcessingResult(
            claim_updates=[
                ClaimUpdate(
                    existing_claim_id="C1",
                    new_contradicting_evidence=[
                        EvidenceRelation(
                            source_id="S2",
                            relation=EvidenceRelationType.CONTRADICTS,
                            summary="Direct contradictory evidence.",
                            strength=EvidenceStrength.DIRECT,
                        )
                    ],
                    updated_confidence=Confidence.MEDIUM,
                    updated_confidence_reason="Direct evidence now conflicts.",
                    updated_status=ClaimStatus.CONFLICTING,
                )
            ]
        ),
        3,
    )
    assert (
        refresh_subquestion_statuses(state)[0].current_status
        == SubQuestionStatus.CONFLICTING
    )


def test_subquestion_decision_payload_excludes_raw_sources_and_validates_target() -> None:
    state = ResearchState(
        question="Question", research_plan=plan(), sources=[source()], current_iteration=1
    )
    decision = ResearchDecision(
        needs_more_research=True,
        reason="The core question is unresolved.",
        target_type=DecisionTargetType.SUBQUESTION,
        target_id="SQ1",
        next_search_query="focused evidence",
    )
    calls: list[dict[str, object]] = []

    class Responses:
        def parse(self, **kwargs: object) -> SimpleNamespace:
            calls.append(kwargs)
            return SimpleNamespace(output_parsed=decision)

    maker = SubquestionResearchDecisionMaker(
        "unused", "test-model", client=SimpleNamespace(responses=Responses())
    )
    assert maker.decide(state) == decision
    prompt = json.dumps(calls[0]["input"])
    assert "success_criteria" in prompt
    assert "search_attempts" in prompt
    assert "raw-S1" not in prompt

    missing = decision.model_copy(update={"target_id": "SQ99"})
    with pytest.raises(ValueError, match="nonexistent subquestion"):
        validate_subquestion_decision_target(missing, state)


def test_sufficient_target_is_rejected_while_core_remains_unresolved() -> None:
    state = ResearchState(question="Question", research_plan=plan())
    state.get_subquestion("SQ3").status = SubQuestionStatus.SUFFICIENT  # type: ignore[union-attr]
    decision = ResearchDecision(
        needs_more_research=True,
        reason="Target secondary context.",
        target_type=DecisionTargetType.SUBQUESTION,
        target_id="SQ3",
        next_search_query="secondary context",
    )
    with pytest.raises(ValueError, match="sufficient subquestion"):
        validate_subquestion_decision_target(decision, state)


def test_decomposed_report_must_cover_or_acknowledge_every_core_subquestion() -> None:
    state = ResearchState(question="Question", research_plan=plan(), sources=[source()])
    apply_evidence_processing_result(
        state,
        EvidenceProcessingResult(new_claims=[claim(ClaimStatus.SUPPORTED)]),
        1,
    )
    refresh_subquestion_statuses(state)
    finding = LedgerReportFinding(
        ledger_claim_ids=["C1"],
        subquestion_ids=["SQ1"],
        claim="Evidence-backed claim.",
        evidence=[EvidenceItem(summary="Direct evidence.", source_ids=["S1"])],
        confidence=Confidence.HIGH,
        confidence_reason="Direct.",
    )
    omitted = LedgerFinalReport(
        question="Question",
        summary="Summary.",
        findings=[finding],
        conclusion="Conclusion.",
    )
    with pytest.raises(ValueError, match="SQ2"):
        validate_ledger_report(omitted, state)

    complete = omitted.model_copy(
        update={"acknowledged_unresolved_subquestion_ids": ["SQ2"]}
    )
    validate_ledger_report(complete, state)


def test_three_iteration_runner_keeps_first_query_and_tracks_targeted_attempts() -> None:
    research_plan = plan()

    class Decomposer:
        calls = 0

        def decompose(self, question: str) -> ResearchPlan:
            self.calls += 1
            return research_plan.model_copy(deep=True)

    class Searcher:
        queries: list[str] = []

        def search(self, query: str) -> list[Source]:
            self.queries.append(query)
            number = len(self.queries)
            return [source(f"incoming-{number}")]

    class Processor:
        attempts_seen: list[tuple[int, int, int | None]] = []

        def process(
            self, state: ResearchState, new_sources: list[Source]
        ) -> EvidenceProcessingResult:
            sq1 = state.get_subquestion("SQ1")
            assert sq1 is not None
            self.attempts_seen.append(
                (state.current_iteration, sq1.search_attempts, sq1.last_targeted_iteration)
            )
            return EvidenceProcessingResult(
                new_claims=[
                    NewClaim(
                        claim=f"Claim {state.current_iteration}",
                        supporting_evidence=[relation(new_sources[0].id)],
                        confidence=Confidence.HIGH,
                        confidence_reason="Direct.",
                        status=(
                            ClaimStatus.WEAK
                            if state.current_iteration == 1
                            else ClaimStatus.SUPPORTED
                        ),
                        related_subquestion_ids=[
                            "SQ1" if state.current_iteration < 3 else "SQ2"
                        ],
                    )
                ]
            )

    class Decisions:
        calls = 0

        def decide(self, state: ResearchState) -> ResearchDecision:
            self.calls += 1
            return ResearchDecision(
                needs_more_research=True,
                reason="Target unresolved core evidence.",
                target_type=DecisionTargetType.SUBQUESTION,
                target_id="SQ1" if self.calls == 1 else "SQ2",
                next_search_query=f"target query {self.calls}",
            )

    class Reporter:
        def generate(self, state: ResearchState) -> FinalReport:
            return FinalReport(
                question=state.question,
                summary="Summary.",
                findings=[
                    Finding(
                        claim="Claim 1",
                        evidence=[EvidenceItem(summary="Direct.", source_ids=["S1"])],
                        confidence=Confidence.HIGH,
                        confidence_reason="Direct.",
                    )
                ],
                conclusion="Conclusion.",
            )

    decomposer = Decomposer()
    searcher = Searcher()
    processor = Processor()
    decisions = Decisions()
    logger = LedgerResearchLogger(
        "Original exact question?",
        "test-model",
        3,
        system_version="evidence-ledger-decomposer-v1",
    )
    result = LedgerResearchRunner(
        searcher,
        processor,
        decisions,
        Reporter(),
        max_iterations=3,
        research_logger=logger,
        question_decomposer=decomposer,
    ).run("Original exact question?")

    assert decomposer.calls == 1
    assert searcher.queries == [
        "Original exact question?",
        "target query 1",
        "target query 2",
    ]
    assert processor.attempts_seen == [(1, 0, None), (2, 1, 2), (3, 1, 2)]
    assert result.state.get_subquestion("SQ1").search_attempts == 1  # type: ignore[union-attr]
    assert result.state.get_subquestion("SQ2").search_attempts == 1  # type: ignore[union-attr]
    assert result.state.get_subquestion("SQ2").last_targeted_iteration == 3  # type: ignore[union-attr]
    assert result.state.stop_reason == "max_iterations"
    log = logger.render_markdown()
    assert "# Research Plan" in log
    assert "Subquestion Progress" in log
    assert "SUBQUESTION SQ1" in log
    trace = build_trace(result.state, "test-model", 3, result.report)
    assert trace["research_plan"]["subquestions"][0]["id"] == "SQ1"
    assert "subquestion_status_changes" in trace["iterations"][0]
