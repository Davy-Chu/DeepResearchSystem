from __future__ import annotations

from types import SimpleNamespace

import pytest

from research.decision import ResearchDecisionMaker, validate_decision_target
from research.evidence_processor import EvidenceProcessor, apply_evidence_processing_result
from research.models import (
    ClaimStatus,
    ClaimUpdate,
    Confidence,
    DecisionTargetType,
    EvidenceProcessingResult,
    EvidenceRelation,
    EvidenceRelationType,
    EvidenceStrength,
    GapImportance,
    GapStatus,
    NewClaim,
    NewGap,
    ResearchDecision,
    ResearchGap,
    ResearchState,
    Source,
)


def relation(
    source_id: str,
    relation_type: EvidenceRelationType = EvidenceRelationType.SUPPORTS,
    summary: str = "Relevant evidence.",
) -> EvidenceRelation:
    return EvidenceRelation(
        source_id=source_id,
        relation=relation_type,
        summary=summary,
        strength=EvidenceStrength.DIRECT,
    )


def source(source_id: str) -> Source:
    return Source(
        id=source_id,
        title=f"Source {source_id}",
        url=f"https://example.com/{source_id}",
        content=f"Exact saved content for {source_id}.",
    )


def new_claim(source_id: str = "S1") -> NewClaim:
    return NewClaim(
        claim="A persistent ledger claim.",
        supporting_evidence=[relation(source_id)],
        confidence=Confidence.MEDIUM,
        confidence_reason="One direct source supports it.",
        status=ClaimStatus.WEAK,
    )


def test_new_claim_and_gap_receive_stable_ids() -> None:
    state = ResearchState(question="Question", sources=[source("S1")])
    result = EvidenceProcessingResult(
        new_claims=[new_claim()],
        new_gaps=[
            NewGap(
                description="An important gap remains.",
                importance=GapImportance.HIGH,
            )
        ],
    )

    updates = apply_evidence_processing_result(state, result, 1)

    assert state.evidence_ledger.claims[0].id == "C1"
    assert state.research_gaps[0].id == "G1"
    assert state.research_gaps[0].status == GapStatus.OPEN
    assert updates.claim_changes[0].claim_id == "C1"
    assert updates.gap_changes[0].gap_id == "G1"


def test_claim_update_deduplicates_evidence_and_changes_status_and_confidence() -> None:
    state = ResearchState(question="Question", sources=[source("S1"), source("S2")])
    apply_evidence_processing_result(
        state, EvidenceProcessingResult(new_claims=[new_claim()]), 1
    )
    result = EvidenceProcessingResult(
        claim_updates=[
            ClaimUpdate(
                existing_claim_id="C1",
                new_supporting_evidence=[
                    relation("S1", summary="Updated summary from the same source."),
                    relation("S2", summary="Independent supporting evidence."),
                ],
                updated_confidence=Confidence.HIGH,
                updated_confidence_reason="Two direct sources now agree.",
                updated_status=ClaimStatus.SUPPORTED,
            )
        ]
    )

    updates = apply_evidence_processing_result(state, result, 2)
    claim = state.evidence_ledger.get_claim("C1")

    assert claim is not None
    assert [item.source_id for item in claim.supporting_evidence] == ["S1", "S2"]
    assert claim.supporting_evidence[0].summary == "Updated summary from the same source."
    assert claim.confidence == Confidence.HIGH
    assert claim.status == ClaimStatus.SUPPORTED
    assert claim.first_seen_iteration == 1
    assert claim.last_updated_iteration == 2
    assert updates.claim_changes[0].previous_confidence == Confidence.MEDIUM
    assert updates.claim_changes[0].previous_status == ClaimStatus.WEAK


def test_contradictory_evidence_is_separate_and_creates_conflict_transition() -> None:
    state = ResearchState(question="Question", sources=[source("S1"), source("S2")])
    apply_evidence_processing_result(
        state, EvidenceProcessingResult(new_claims=[new_claim()]), 1
    )
    apply_evidence_processing_result(
        state,
        EvidenceProcessingResult(
            claim_updates=[
                ClaimUpdate(
                    existing_claim_id="C1",
                    new_contradicting_evidence=[
                        relation("S2", EvidenceRelationType.CONTRADICTS)
                    ],
                    updated_confidence=Confidence.MEDIUM,
                    updated_confidence_reason="Direct sources disagree.",
                    updated_status=ClaimStatus.CONFLICTING,
                )
            ]
        ),
        2,
    )

    claim = state.evidence_ledger.get_claim("C1")
    assert claim is not None
    assert [item.source_id for item in claim.supporting_evidence] == ["S1"]
    assert [item.source_id for item in claim.contradicting_evidence] == ["S2"]
    assert state.conflicting_claims() == [claim]


def test_gap_can_be_resolved_in_a_later_iteration() -> None:
    state = ResearchState(
        question="Question",
        research_gaps=[
            ResearchGap(
                id="G1",
                description="Open gap",
                importance=GapImportance.HIGH,
                created_iteration=1,
            )
        ],
    )
    apply_evidence_processing_result(
        state, EvidenceProcessingResult(resolved_gap_ids=["G1"]), 2
    )
    assert state.research_gaps[0].status == GapStatus.RESOLVED
    assert state.research_gaps[0].resolved_iteration == 2
    assert state.open_gaps() == []


def test_unknown_source_rejects_update_without_mutating_state() -> None:
    state = ResearchState(question="Question", sources=[source("S1")])
    result = EvidenceProcessingResult(new_claims=[new_claim("S999")])
    with pytest.raises(ValueError, match="unknown source ID: S999"):
        apply_evidence_processing_result(state, result, 1)
    assert state.evidence_ledger.claims == []


def test_update_to_nonexistent_claim_is_rejected() -> None:
    state = ResearchState(question="Question", sources=[source("S1")])
    result = EvidenceProcessingResult(
        claim_updates=[
            ClaimUpdate(
                existing_claim_id="C99",
                updated_confidence=Confidence.LOW,
                updated_confidence_reason="Missing claim.",
                updated_status=ClaimStatus.INSUFFICIENT_EVIDENCE,
            )
        ]
    )
    with pytest.raises(ValueError, match="nonexistent claim: C99"):
        apply_evidence_processing_result(state, result, 1)


def test_resolution_of_nonexistent_gap_is_rejected() -> None:
    state = ResearchState(question="Question")
    with pytest.raises(ValueError, match="nonexistent gap ID.*G99"):
        apply_evidence_processing_result(
            state,
            EvidenceProcessingResult(resolved_gap_ids=["G99"]),
            1,
        )


def test_continue_decision_requires_next_query() -> None:
    with pytest.raises(ValueError, match="next_search_query"):
        ResearchDecision(
            needs_more_research=True,
            reason="More evidence is needed.",
            target_type=DecisionTargetType.GENERAL,
        )


def test_decision_target_must_exist_and_processor_prompt_uses_ledger() -> None:
    state = ResearchState(question="Question", sources=[source("S1")])
    apply_evidence_processing_result(
        state, EvidenceProcessingResult(new_claims=[new_claim()]), 1
    )
    invalid = ResearchDecision(
        needs_more_research=True,
        reason="Investigate missing claim.",
        target_type=DecisionTargetType.CLAIM,
        target_id="C99",
        next_search_query="missing claim evidence",
    )
    with pytest.raises(ValueError, match="nonexistent claim"):
        validate_decision_target(invalid, state)

    processing = EvidenceProcessingResult()
    calls: list[dict[str, object]] = []

    class Responses:
        def parse(self, **kwargs: object) -> SimpleNamespace:
            calls.append(kwargs)
            return SimpleNamespace(output_parsed=processing)

    processor = EvidenceProcessor(
        "unused", "test-model", client=SimpleNamespace(responses=Responses())
    )
    processor.process(state, [state.sources[0]])
    prompt = str(calls[0]["input"])
    assert "current_evidence_ledger" in prompt
    assert "allowed_existing_claim_ids" in prompt
    assert "allowed_subquestion_ids" in prompt
    assert "C1" in prompt
    assert "Exact saved content for S1." in prompt
    assert calls[0]["reasoning"] == {"effort": "low"}


def test_decision_prompt_uses_state_without_raw_source_content() -> None:
    state = ResearchState(question="Question", sources=[source("S1")])
    apply_evidence_processing_result(
        state, EvidenceProcessingResult(new_claims=[new_claim()]), 1
    )
    decision = ResearchDecision(
        needs_more_research=True,
        reason="C1 is central and weak.",
        target_type=DecisionTargetType.CLAIM,
        target_id="C1",
        next_search_query="independent evidence for claim",
    )
    calls: list[dict[str, object]] = []

    class Responses:
        def parse(self, **kwargs: object) -> SimpleNamespace:
            calls.append(kwargs)
            return SimpleNamespace(output_parsed=decision)

    maker = ResearchDecisionMaker(
        "unused", "test-model", client=SimpleNamespace(responses=Responses())
    )
    assert maker.decide(state) == decision
    prompt = str(calls[0]["input"])
    assert "C1" in prompt
    assert "remaining_search_budget" in prompt
    assert "Exact saved content for S1." not in prompt
