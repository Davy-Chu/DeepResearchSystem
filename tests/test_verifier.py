from __future__ import annotations

import json
from types import SimpleNamespace

import pytest

from research.evidence_processor import apply_evidence_processing_result
from research.decomposer import refresh_subquestion_statuses
from research.ledger_logger import LedgerResearchLogger
from research.ledger_runner import LedgerResearchRunner
from research.models import (
    ClaimStatus,
    ClaimUpdate,
    ClaimVerificationResult,
    Confidence,
    CounterSearchStatus,
    DecisionOrigin,
    DecisionTargetType,
    EvidenceItem,
    EvidenceProcessingResult,
    EvidenceRelation,
    EvidenceRelationType,
    EvidenceStrength,
    FinalReport,
    Finding,
    LedgerFinalReport,
    LedgerReportFinding,
    NewClaim,
    ResearchDecision,
    ResearchPlan,
    ResearchState,
    SearchPurpose,
    Source,
    SubQuestion,
    SubQuestionImportance,
    SubQuestionStatus,
    VerificationPhase,
    VerificationVerdict,
)
from research.report import (
    build_incomplete_report,
    build_trace,
    validate_ledger_report,
)
from research.verifier import (
    IndependentClaimVerifier,
    apply_verification_result,
    build_neutral_evidence_pool,
    select_claim_for_verification,
    validate_verification_result,
)


def research_plan() -> ResearchPlan:
    return ResearchPlan(
        subquestions=[
            SubQuestion(
                id="SQ1",
                question="Does X improve reasoning?",
                importance=SubQuestionImportance.CORE,
                success_criteria="Establish measured gains and their scope.",
            ),
            SubQuestion(
                id="SQ2",
                question="When does X fail?",
                importance=SubQuestionImportance.CORE,
                success_criteria="Identify limitations and negative results.",
            ),
            SubQuestion(
                id="SQ3",
                question="What background is useful?",
                importance=SubQuestionImportance.SECONDARY,
                success_criteria="Provide nonessential context.",
            ),
        ]
    )


def source(source_id: str, content: str | None = None) -> Source:
    return Source(
        id=source_id,
        title=f"Source {source_id}",
        url=f"https://example.com/{source_id}",
        content=content or f"Exact neutral content for {source_id}.",
    )


def relation(
    source_id: str,
    relation_type: EvidenceRelationType = EvidenceRelationType.SUPPORTS,
) -> EvidenceRelation:
    return EvidenceRelation(
        source_id=source_id,
        relation=relation_type,
        summary=f"Researcher summary for {source_id}.",
        strength=EvidenceStrength.DIRECT,
    )


def add_claim(
    state: ResearchState,
    text: str,
    source_id: str,
    confidence: Confidence = Confidence.HIGH,
    subquestion_id: str = "SQ1",
    iteration: int = 1,
) -> None:
    apply_evidence_processing_result(
        state,
        EvidenceProcessingResult(
            new_claims=[
                NewClaim(
                    claim=text,
                    supporting_evidence=[relation(source_id)],
                    confidence=confidence,
                    confidence_reason="SECRET CONFIDENCE REASON",
                    status=ClaimStatus.SUPPORTED,
                    related_subquestion_ids=[subquestion_id],
                )
            ]
        ),
        iteration,
    )


def result(
    claim_id: str,
    verdict: VerificationVerdict = VerificationVerdict.VERIFIED,
    *,
    counter: bool = False,
    query: str | None = None,
    text: str | None = None,
    confidence: Confidence = Confidence.MEDIUM,
    status: ClaimStatus = ClaimStatus.SUPPORTED,
) -> ClaimVerificationResult:
    return ClaimVerificationResult(
        claim_id=claim_id,
        verdict=verdict,
        reason="Independent evidence judgment.",
        missing_assumptions=["Generalization is not established."],
        source_quality_concerns=["The evidence pool is limited."],
        counter_search_needed=counter,
        counter_search_query=query,
        recommended_claim_text=text,
        recommended_confidence=confidence,
        recommended_status=status,
    )


def test_verifier_payload_enforces_information_boundary_and_neutral_pool() -> None:
    state = ResearchState(
        question="Original question",
        research_plan=research_plan(),
        sources=[
            source("S1", "Distinct supporting source content."),
            source("S2", "Distinct contradicting source content."),
            source("S3", "Unrelated other-claim content."),
        ],
    )
    add_claim(state, "Distinct candidate claim.", "S1")
    claim = state.evidence_ledger.get_claim("C1")
    assert claim is not None
    claim.contradicting_evidence = [
        relation("S2", EvidenceRelationType.CONTRADICTS)
    ]
    add_claim(state, "Unrelated claim.", "S3", subquestion_id="SQ2")
    calls: list[dict[str, object]] = []

    class Responses:
        def parse(self, **kwargs: object) -> SimpleNamespace:
            calls.append(kwargs)
            return SimpleNamespace(output_parsed=result("C1"))

    verifier = IndependentClaimVerifier(
        "unused", "verifier-model", client=SimpleNamespace(responses=Responses())
    )
    verifier.verify(state, claim, VerificationPhase.INITIAL, True)
    payload = json.loads(calls[0]["input"][1]["content"])  # type: ignore[index]

    assert payload["candidate_claim"] == {
        "id": "C1",
        "text": "Distinct candidate claim.",
    }
    assert payload["related_subquestions"][0]["success_criteria"]
    assert [item["source_id"] for item in payload["evidence_sources"]] == [
        "S1",
        "S2",
    ]
    serialized = json.dumps(payload)
    assert "Distinct supporting source content." in serialized
    assert "Distinct contradicting source content." in serialized
    assert "Unrelated other-claim content." not in serialized
    assert "SECRET CONFIDENCE REASON" not in serialized
    assert "confidence" not in payload["candidate_claim"]
    assert "status" not in payload["candidate_claim"]
    assert "relation" not in payload["evidence_sources"][0]
    assert calls[0]["reasoning"] == {"effort": "low"}


def test_neutral_pool_fails_when_attached_source_snapshot_is_missing() -> None:
    state = ResearchState(
        question="Question", research_plan=research_plan(), sources=[source("S1")]
    )
    add_claim(state, "Claim", "S1")
    claim = state.evidence_ledger.get_claim("C1")
    assert claim is not None
    claim.contradicting_evidence = [
        relation("S99", EvidenceRelationType.CONTRADICTS)
    ]
    with pytest.raises(ValueError, match="without saved content.*S99"):
        build_neutral_evidence_pool(state, claim)


def test_claim_selection_is_deterministic_and_rechecks_only_new_versions() -> None:
    state = ResearchState(
        question="Question",
        research_plan=research_plan(),
        sources=[source("S1"), source("S2"), source("S3")],
    )
    add_claim(state, "High core", "S1", Confidence.HIGH, "SQ1")
    add_claim(state, "Medium core", "S2", Confidence.MEDIUM, "SQ2")
    add_claim(state, "High secondary", "S3", Confidence.HIGH, "SQ3")
    assert select_claim_for_verification(state).id == "C1"  # type: ignore[union-attr]

    apply_verification_result(
        state,
        result("C1", confidence=Confidence.HIGH),
        1,
        VerificationPhase.INITIAL,
    )
    assert select_claim_for_verification(state).id == "C2"  # type: ignore[union-attr]
    state.evidence_ledger.get_claim("C1").last_updated_iteration = 2  # type: ignore[union-attr]
    assert select_claim_for_verification(state).id == "C1"  # type: ignore[union-attr]


def test_qualification_reconciles_atomically_without_changing_evidence() -> None:
    state = ResearchState(
        question="Question", research_plan=research_plan(), sources=[source("S1")]
    )
    add_claim(state, "Method A always improves performance.", "S1")
    claim = state.evidence_ledger.get_claim("C1")
    assert claim is not None
    supporting_before = claim.supporting_evidence.copy()
    record = apply_verification_result(
        state,
        result(
            "C1",
            VerificationVerdict.NEEDS_QUALIFICATION,
            text=(
                "Method A improves performance in several tested settings, "
                "but results vary by task."
            ),
        ),
        1,
        VerificationPhase.INITIAL,
    )
    assert claim.claim.endswith("results vary by task.")
    assert claim.confidence == Confidence.MEDIUM
    assert claim.status == ClaimStatus.SUPPORTED
    assert claim.supporting_evidence == supporting_before
    assert claim.contradicting_evidence == []
    assert record.previous_claim_text == "Method A always improves performance."
    assert record.reconciliation_applied is True


@pytest.mark.parametrize(
    ("verdict", "status", "subquestion_status"),
    [
        (
            VerificationVerdict.CONTRADICTED,
            ClaimStatus.CONFLICTING,
            SubQuestionStatus.CONFLICTING,
        ),
        (
            VerificationVerdict.INSUFFICIENT_EVIDENCE,
            ClaimStatus.INSUFFICIENT_EVIDENCE,
            SubQuestionStatus.PARTIAL,
        ),
    ],
)
def test_conservative_verdicts_update_status_without_inverting_claim(
    verdict: VerificationVerdict,
    status: ClaimStatus,
    subquestion_status: SubQuestionStatus,
) -> None:
    state = ResearchState(
        question="Question", research_plan=research_plan(), sources=[source("S1")]
    )
    add_claim(state, "X improves performance.", "S1")
    refresh_subquestion_statuses(state)
    assert state.get_subquestion("SQ1").status == SubQuestionStatus.SUFFICIENT  # type: ignore[union-attr]
    apply_verification_result(
        state,
        result("C1", verdict, status=status, confidence=Confidence.LOW),
        1,
        VerificationPhase.INITIAL,
    )
    claim = state.evidence_ledger.get_claim("C1")
    assert claim is not None
    assert claim.claim == "X improves performance."
    assert claim.status == status
    refresh_subquestion_statuses(state)
    assert state.get_subquestion("SQ1").status == subquestion_status  # type: ignore[union-attr]


def test_invalid_verifier_result_does_not_partially_mutate_claim() -> None:
    state = ResearchState(
        question="Question", research_plan=research_plan(), sources=[source("S1")]
    )
    add_claim(state, "Original canonical wording.", "S1")
    claim = state.evidence_ledger.get_claim("C1")
    assert claim is not None
    before = claim.model_copy(deep=True)

    with pytest.raises(ValueError, match="expected C1"):
        validate_verification_result(
            state,
            claim,
            result("C2"),
            VerificationPhase.INITIAL,
            ["S1"],
        )

    assert claim == before
    assert state.claim_verifications == []


def test_ledger_report_rejects_superseded_preverification_wording() -> None:
    state = ResearchState(
        question="Question", research_plan=research_plan(), sources=[source("S1")]
    )
    old_wording = "Method A always improves performance."
    new_wording = "Method A improves some tested settings, with variable results."
    add_claim(state, old_wording, "S1")
    apply_verification_result(
        state,
        result(
            "C1",
            VerificationVerdict.NEEDS_QUALIFICATION,
            text=new_wording,
        ),
        1,
        VerificationPhase.INITIAL,
    )
    report = LedgerFinalReport(
        question=state.question,
        summary="Summary.",
        findings=[
            LedgerReportFinding(
                claim=old_wording,
                evidence=[EvidenceItem(summary="Evidence.", source_ids=["S1"])],
                confidence=Confidence.MEDIUM,
                confidence_reason="Qualified by independent verification.",
                ledger_claim_ids=["C1"],
                subquestion_ids=["SQ1"],
            )
        ],
        acknowledged_unresolved_subquestion_ids=["SQ2"],
        conclusion="Conclusion.",
    )

    with pytest.raises(ValueError, match="superseded"):
        validate_ledger_report(report, state)

    validate_ledger_report(
        report.model_copy(
            update={
                "findings": [report.findings[0].model_copy(update={"claim": new_wording})]
            }
        ),
        state,
    )


def test_post_countersearch_cannot_request_another_search() -> None:
    state = ResearchState(
        question="Question", research_plan=research_plan(), sources=[source("S1")]
    )
    add_claim(state, "Claim", "S1")
    claim = state.evidence_ledger.get_claim("C1")
    assert claim is not None
    invalid = result("C1", counter=True, query="another counter search")
    with pytest.raises(ValueError, match="cannot request another"):
        validate_verification_result(
            state,
            claim,
            invalid,
            VerificationPhase.POST_COUNTERSEARCH,
            ["S1"],
        )


class FakeDecomposer:
    def decompose(self, question: str) -> ResearchPlan:
        return research_plan()


class FakeSearcher:
    def __init__(self) -> None:
        self.queries: list[str] = []

    def search(self, query: str) -> list[Source]:
        self.queries.append(query)
        number = len(self.queries)
        return [source("", f"Retrieved content {number}.").model_copy(
            update={"url": f"https://example.com/run-{number}"}
        )]


class IntegrationProcessor:
    def process(
        self, state: ResearchState, new_sources: list[Source]
    ) -> EvidenceProcessingResult:
        source_id = new_sources[0].id
        if state.current_iteration == 1:
            return EvidenceProcessingResult(
                new_claims=[
                    NewClaim(
                        claim="Technique X reliably improves reasoning.",
                        supporting_evidence=[relation(source_id)],
                        confidence=Confidence.HIGH,
                        confidence_reason="Initial evidence.",
                        status=ClaimStatus.SUPPORTED,
                        related_subquestion_ids=["SQ1"],
                    )
                ]
            )
        if state.current_iteration == 2:
            return EvidenceProcessingResult(
                claim_updates=[
                    ClaimUpdate(
                        existing_claim_id="C1",
                        new_contradicting_evidence=[
                            relation(source_id, EvidenceRelationType.CONTRADICTS)
                        ],
                        updated_confidence=Confidence.MEDIUM,
                        updated_confidence_reason="Counterevidence conflicts.",
                        updated_status=ClaimStatus.CONFLICTING,
                    )
                ]
            )
        return EvidenceProcessingResult(
            new_claims=[
                NewClaim(
                    claim="Technique X has documented limitations.",
                    supporting_evidence=[relation(source_id)],
                    confidence=Confidence.HIGH,
                    confidence_reason="Direct limitations evidence.",
                    status=ClaimStatus.SUPPORTED,
                    related_subquestion_ids=["SQ2"],
                )
            ]
        )


class IntegrationVerifier:
    def __init__(self) -> None:
        self.calls: list[tuple[str, VerificationPhase, bool]] = []

    def verify(
        self,
        state: ResearchState,
        claim: object,
        phase: VerificationPhase,
        counter_search_allowed: bool,
    ) -> ClaimVerificationResult:
        claim_id = claim.id  # type: ignore[attr-defined]
        self.calls.append((claim_id, phase, counter_search_allowed))
        if len(self.calls) == 1:
            return result(
                "C1",
                VerificationVerdict.NEEDS_QUALIFICATION,
                counter=True,
                query="technique X failure replication no improvement limitations",
                text="Technique X improves some tested reasoning settings.",
            )
        if len(self.calls) == 2:
            return result(
                "C1",
                VerificationVerdict.NEEDS_QUALIFICATION,
                text=(
                    "Technique X improves reasoning in some tested settings, "
                    "but gains are inconsistent across tasks."
                ),
            )
        return result("C2", confidence=Confidence.HIGH)


class OneDecision:
    calls = 0

    def decide(self, state: ResearchState) -> ResearchDecision:
        self.calls += 1
        return ResearchDecision(
            needs_more_research=True,
            reason="Research the remaining limitations subquestion.",
            target_type=DecisionTargetType.SUBQUESTION,
            target_id="SQ2",
            next_search_query="technique X limitations boundary conditions",
        )


class CanonicalReporter:
    def generate(self, state: ResearchState) -> FinalReport:
        c1 = state.evidence_ledger.get_claim("C1")
        c2 = state.evidence_ledger.get_claim("C2")
        assert c1 is not None and c2 is not None
        return FinalReport(
            question=state.question,
            summary="Verified canonical state.",
            findings=[
                Finding(
                    claim=c1.claim,
                    evidence=[EvidenceItem(summary="Evidence.", source_ids=["S1"])],
                    confidence=c1.confidence,
                    confidence_reason=c1.confidence_reason,
                ),
                Finding(
                    claim=c2.claim,
                    evidence=[EvidenceItem(summary="Evidence.", source_ids=["S3"])],
                    confidence=c2.confidence,
                    confidence_reason=c2.confidence_reason,
                ),
            ],
            conclusion="Conclusion.",
        )


def test_three_search_verified_integration_countersearches_and_reconciles() -> None:
    searcher = FakeSearcher()
    verifier = IntegrationVerifier()
    decision = OneDecision()
    run_logger = LedgerResearchLogger(
        "Does technique X reliably improve model reasoning, and what are its limitations?",
        "researcher-model",
        3,
        system_version="evidence-ledger-decomposer-verifier-v1",
        verifier_model="verifier-model",
    )
    result_state = LedgerResearchRunner(
        searcher,
        IntegrationProcessor(),
        decision,
        CanonicalReporter(),
        max_iterations=3,
        research_logger=run_logger,
        question_decomposer=FakeDecomposer(),
        claim_verifier=verifier,
    ).run(
        "Does technique X reliably improve model reasoning, and what are its limitations?"
    ).state

    assert searcher.queries == [
        result_state.question,
        "technique X failure replication no improvement limitations",
        "technique X limitations boundary conditions",
    ]
    assert [item.search_purpose for item in result_state.ledger_iterations] == [
        SearchPurpose.GENERAL,
        SearchPurpose.COUNTERSEARCH,
        SearchPurpose.SUBQUESTION,
    ]
    assert [item.search_target_id for item in result_state.ledger_iterations] == [
        None,
        "C1",
        "SQ2",
    ]
    assert verifier.calls == [
        ("C1", VerificationPhase.INITIAL, True),
        ("C1", VerificationPhase.POST_COUNTERSEARCH, False),
        ("C2", VerificationPhase.INITIAL, False),
    ]
    assert len(result_state.claim_verifications) == 3
    assert result_state.claim_verifications[0].counter_search_status == CounterSearchStatus.EXECUTED
    assert result_state.claim_verifications[0].counter_search_source_ids == ["S2"]
    assert result_state.claim_verifications[1].reconciliation_applied is True
    assert result_state.evidence_ledger.get_claim("C1").claim.endswith(  # type: ignore[union-attr]
        "gains are inconsistent across tasks."
    )
    assert result_state.stop_reason == "max_iterations"
    assert result_state.ledger_iterations[0].decision.decision_origin == (  # type: ignore[union-attr]
        DecisionOrigin.VERIFIER_COUNTERSEARCH
    )
    assert result_state.ledger_iterations[2].decision.decision_origin == (  # type: ignore[union-attr]
        DecisionOrigin.BUDGET_STOP
    )
    log = run_logger.render_markdown()
    assert "Independent Verification" in log
    assert "V1 — Claim C1" in log
    assert "COUNTERSEARCH" in log
    assert "Confidence:" in log
    assert "Counter-search evidence:** S2" in log
    assert "# Verifier Diagnostics" in log
    assert "Counter-searches executed: 1" in log
    assert "Searches allocated to counter-search: 1" in log
    trace = build_trace(result_state, "researcher-model", 3)
    assert trace["system_version"] == "evidence-ledger-decomposer-verifier-v1"
    assert trace["iterations"][1]["search_purpose"] == "COUNTERSEARCH"
    assert trace["iterations"][0]["research_decision"]["decision_origin"] == (
        "VERIFIER_COUNTERSEARCH"
    )
    assert len(trace["claim_verifications"]) == 3


class StaticProcessor:
    def process(
        self, state: ResearchState, new_sources: list[Source]
    ) -> EvidenceProcessingResult:
        if state.evidence_ledger.claims:
            return EvidenceProcessingResult()
        return EvidenceProcessingResult(
            new_claims=[
                NewClaim(
                    claim="Supported core claim.",
                    supporting_evidence=[relation(new_sources[0].id)],
                    confidence=Confidence.HIGH,
                    confidence_reason="Direct.",
                    status=ClaimStatus.SUPPORTED,
                    related_subquestion_ids=["SQ1"],
                )
            ]
        )


class StaticVerifier:
    def __init__(self, query: str) -> None:
        self.query = query

    def verify(self, state: ResearchState, claim: object, phase: VerificationPhase, counter_search_allowed: bool) -> ClaimVerificationResult:
        return result("C1", counter=True, query=self.query)


class StopDecision:
    def __init__(self, query: str | None = None) -> None:
        self.query = query

    def decide(self, state: ResearchState) -> ResearchDecision:
        if self.query:
            return ResearchDecision(
                needs_more_research=True,
                reason="Use ordinary research budget.",
                target_type=DecisionTargetType.SUBQUESTION,
                target_id="SQ2",
                next_search_query=self.query,
            )
        return ResearchDecision(needs_more_research=False, reason="Stop.")


def test_duplicate_countersearch_does_not_stop_normal_controller() -> None:
    question = "Original question"
    searcher = FakeSearcher()
    state = LedgerResearchRunner(
        searcher,
        StaticProcessor(),
        StopDecision("ordinary follow-up"),
        CanonicalReporterForOneClaim(),
        max_iterations=2,
        question_decomposer=FakeDecomposer(),
        claim_verifier=StaticVerifier(question),
    ).run(question).state
    assert searcher.queries == [question, "ordinary follow-up"]
    assert state.claim_verifications[0].counter_search_status == (
        CounterSearchStatus.BLOCKED_DUPLICATE
    )
    assert state.stop_reason == "max_iterations"


class CanonicalReporterForOneClaim:
    def generate(self, state: ResearchState) -> FinalReport:
        claim = state.evidence_ledger.get_claim("C1")
        assert claim is not None
        return FinalReport(
            question=state.question,
            summary="Summary.",
            findings=[
                Finding(
                    claim=claim.claim,
                    evidence=[EvidenceItem(summary="Evidence.", source_ids=["S1"])],
                    confidence=claim.confidence,
                    confidence_reason=claim.confidence_reason,
                )
            ],
            conclusion="Conclusion.",
        )


def test_final_iteration_blocks_countersearch_and_incomplete_report_discloses_it() -> None:
    state = LedgerResearchRunner(
        FakeSearcher(),
        StaticProcessor(),
        StopDecision(),
        CanonicalReporterForOneClaim(),
        max_iterations=1,
        question_decomposer=FakeDecomposer(),
        claim_verifier=StaticVerifier("counter evidence query"),
    ).run("Question").state
    assert len(state.ledger_iterations) == 1
    assert state.claim_verifications[0].counter_search_status == (
        CounterSearchStatus.BLOCKED_BUDGET
    )
    assert state.stop_reason == "max_iterations"
    incomplete = build_incomplete_report(state, "test")
    assert any(
        "Independent verification of C1" in gap
        and "BLOCKED_BUDGET" in gap
        for gap in incomplete.remaining_gaps
    )
