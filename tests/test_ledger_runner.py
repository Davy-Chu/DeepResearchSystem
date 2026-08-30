from __future__ import annotations

import json
from collections.abc import Iterable
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace

from evaluation.evaluator import load_evaluation_input
from research.ledger_logger import LedgerResearchLogger
from research.ledger_runner import LedgerResearchRunner
from research.models import (
    ClaimStatus,
    ClaimUpdate,
    Confidence,
    Conflict,
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
    ResearchDecision,
    ResearchState,
    Source,
)
from research.report import FinalReportGenerator, save_research_outputs


def source(url_suffix: str) -> Source:
    return Source(
        id="",
        title=f"Source {url_suffix}",
        url=f"https://example.com/{url_suffix}",
        content=f"Exact saved evidence for {url_suffix}.",
    )


def evidence(source_id: str, relation_type: EvidenceRelationType) -> EvidenceRelation:
    return EvidenceRelation(
        source_id=source_id,
        relation=relation_type,
        summary=f"{source_id} provides {relation_type.value.lower()} evidence.",
        strength=EvidenceStrength.DIRECT,
    )


class FakeSearch:
    def __init__(self, results: Iterable[list[Source]]) -> None:
        self.results = iter(results)
        self.queries: list[str] = []

    def search(self, query: str) -> list[Source]:
        self.queries.append(query)
        return next(self.results)


class FakeProcessor:
    def __init__(self) -> None:
        self.states_seen: list[ResearchState] = []

    def process(
        self, state: ResearchState, new_sources: list[Source]
    ) -> EvidenceProcessingResult:
        self.states_seen.append(state.model_copy(deep=True))
        if state.current_iteration == 1:
            return EvidenceProcessingResult(
                new_claims=[
                    NewClaim(
                        claim="Claim one.",
                        supporting_evidence=[
                            evidence("S1", EvidenceRelationType.SUPPORTS)
                        ],
                        confidence=Confidence.MEDIUM,
                        confidence_reason="One direct source.",
                        status=ClaimStatus.WEAK,
                    ),
                    NewClaim(
                        claim="Claim two.",
                        supporting_evidence=[
                            evidence("S2", EvidenceRelationType.SUPPORTS)
                        ],
                        confidence=Confidence.MEDIUM,
                        confidence_reason="One direct source.",
                        status=ClaimStatus.WEAK,
                    ),
                ],
                new_gaps=[
                    NewGap(
                        description="Gap one needs targeted evidence.",
                        importance=GapImportance.HIGH,
                    )
                ],
            )
        assert state.evidence_ledger.get_claim("C1") is not None
        assert state.evidence_ledger.get_claim("C2") is not None
        assert state.open_gaps()[0].id == "G1"
        return EvidenceProcessingResult(
            claim_updates=[
                ClaimUpdate(
                    existing_claim_id="C1",
                    new_supporting_evidence=[
                        evidence("S3", EvidenceRelationType.SUPPORTS)
                    ],
                    updated_confidence=Confidence.HIGH,
                    updated_confidence_reason="Two direct sources agree.",
                    updated_status=ClaimStatus.SUPPORTED,
                ),
                ClaimUpdate(
                    existing_claim_id="C2",
                    new_contradicting_evidence=[
                        evidence("S4", EvidenceRelationType.CONTRADICTS)
                    ],
                    updated_confidence=Confidence.MEDIUM,
                    updated_confidence_reason="Direct sources disagree.",
                    updated_status=ClaimStatus.CONFLICTING,
                ),
            ],
            resolved_gap_ids=["G1"],
        )


class FakeDecisionMaker:
    def __init__(self) -> None:
        self.states_seen: list[ResearchState] = []

    def decide(self, state: ResearchState) -> ResearchDecision:
        self.states_seen.append(state.model_copy(deep=True))
        assert len(state.evidence_ledger.claims) == 2
        assert [gap.id for gap in state.open_gaps()] == ["G1"]
        return ResearchDecision(
            needs_more_research=True,
            reason="G1 is central and remains open.",
            target_type=DecisionTargetType.GAP,
            target_id="G1",
            next_search_query="targeted evidence for gap one",
        )


class LedgerBackedReporter:
    def generate(self, state: ResearchState) -> FinalReport:
        c1 = state.evidence_ledger.get_claim("C1")
        c2 = state.evidence_ledger.get_claim("C2")
        assert c1 is not None and c2 is not None
        assert c1.status == ClaimStatus.SUPPORTED
        assert c2.status == ClaimStatus.CONFLICTING
        assert state.open_gaps() == []
        return FinalReport(
            question=state.question,
            summary="The ledger contains one supported and one conflicting claim.",
            findings=[
                Finding(
                    claim=c1.claim,
                    evidence=[
                        EvidenceItem(summary=item.summary, source_ids=[item.source_id])
                        for item in c1.supporting_evidence
                    ],
                    confidence=c1.confidence,
                    confidence_reason=c1.confidence_reason,
                ),
                Finding(
                    claim=c2.claim,
                    evidence=[
                        EvidenceItem(summary=item.summary, source_ids=[item.source_id])
                        for item in c2.supporting_evidence
                    ],
                    confidence=c2.confidence,
                    confidence_reason=c2.confidence_reason,
                ),
            ],
            conflicts_and_uncertainties=[
                Conflict(
                    description="Claim two has meaningful contradictory evidence.",
                    source_ids=["S2", "S4"],
                )
            ],
            remaining_gaps=[],
            conclusion="Claim one is supported; claim two remains conflicting.",
        )


def test_two_iteration_ledger_flow_persists_state_log_trace_and_evaluator_input() -> None:
    search = FakeSearch(
        [
            [source("one"), source("two")],
            [source("three"), source("four"), source("five")],
        ]
    )
    processor = FakeProcessor()
    decision_maker = FakeDecisionMaker()
    logger = LedgerResearchLogger("Synthetic question", "test-model", 2)
    runner = LedgerResearchRunner(
        search,
        processor,
        decision_maker,
        LedgerBackedReporter(),
        max_iterations=2,
        research_logger=logger,
    )

    result = runner.run("Synthetic question")

    c1 = result.state.evidence_ledger.get_claim("C1")
    c2 = result.state.evidence_ledger.get_claim("C2")
    assert c1 is not None and c2 is not None
    assert [item.source_id for item in c1.supporting_evidence] == ["S1", "S3"]
    assert c1.confidence == Confidence.HIGH
    assert c1.status == ClaimStatus.SUPPORTED
    assert [item.source_id for item in c2.supporting_evidence] == ["S2"]
    assert [item.source_id for item in c2.contradicting_evidence] == ["S4"]
    assert c2.status == ClaimStatus.CONFLICTING
    assert result.state.research_gaps[0].status.value == "RESOLVED"
    assert result.state.stop_reason == "max_iterations"
    assert search.queries == ["Synthetic question", "targeted evidence for gap one"]
    assert len(decision_maker.states_seen) == 1
    assert len(processor.states_seen[1].evidence_ledger.claims) == 2

    log_text = logger.render_markdown()
    assert "New Claim C1" in log_text
    assert "Updated Claim C1" in log_text
    assert "WEAK → SUPPORTED" in log_text
    assert "WEAK → CONFLICTING" in log_text
    assert "New Gap G1" in log_text
    assert "Resolved Gap G1" in log_text
    assert "GAP G1" in log_text
    assert "Open Gaps: 0" in log_text

    with TemporaryDirectory(dir=Path.cwd()) as temporary_directory:
        run_directory = Path(temporary_directory) / "ledger-run"
        report_path, trace_path = save_research_outputs(
            result.state,
            result.report,
            "test-model",
            output_dir=run_directory,
            max_iterations=2,
        )
        logger.save(run_directory)
        trace = json.loads(trace_path.read_text(encoding="utf-8"))
        evaluation_input = load_evaluation_input(run_directory)

        assert report_path.exists()
        assert trace["system_version"] == "evidence-ledger-v1"
        assert trace["evidence_ledger"]["claims"][0]["id"] == "C1"
        assert trace["iterations"][1]["ledger_updates"]["claim_changes"][0][
            "previous_status"
        ] == "WEAK"
        assert trace["iterations"][0]["research_decision"]["target_id"] == "G1"
        assert trace["research_gaps"][0]["status"] == "RESOLVED"
        assert evaluation_input.report is not None
        assert len(evaluation_input.report.findings) == 2
        assert len(evaluation_input.sources) == 5


def test_final_report_generator_uses_ledger_claim_ids_and_translates_output() -> None:
    state = ResearchState(
        question="Question",
        system_version="evidence-ledger-v1",
        sources=[
            Source(
                id="S1",
                title="Source",
                url="https://example.com/source",
                content="Raw source content must not enter the report prompt.",
            )
        ],
    )
    from research.evidence_processor import apply_evidence_processing_result

    apply_evidence_processing_result(
        state,
        EvidenceProcessingResult(
            new_claims=[
                NewClaim(
                    claim="Claim one.",
                    supporting_evidence=[
                        evidence("S1", EvidenceRelationType.SUPPORTS)
                    ],
                    confidence=Confidence.MEDIUM,
                    confidence_reason="One direct source.",
                    status=ClaimStatus.WEAK,
                )
            ]
        ),
        1,
    )
    parsed = LedgerFinalReport(
        question="Question",
        summary="Ledger summary.",
        findings=[
            LedgerReportFinding(
                ledger_claim_ids=["C1"],
                claim="Claim one.",
                evidence=[EvidenceItem(summary="S1 supports it.", source_ids=["S1"])],
                confidence=Confidence.MEDIUM,
                confidence_reason="One direct source.",
            )
        ],
        conflicts_and_uncertainties=[],
        remaining_gaps=[],
        conclusion="Ledger conclusion.",
    )
    calls: list[dict[str, object]] = []

    class Responses:
        def parse(self, **kwargs: object) -> SimpleNamespace:
            calls.append(kwargs)
            return SimpleNamespace(output_parsed=parsed)

    generator = FinalReportGenerator(
        "unused", "test-model", client=SimpleNamespace(responses=Responses())
    )
    report = generator.generate(state)

    assert report.findings[0].claim == "Claim one."
    assert report.findings[0].evidence[0].source_ids == ["S1"]
    assert calls[0]["text_format"] is LedgerFinalReport
    prompt = str(calls[0]["input"])
    assert "C1" in prompt
    assert "Raw source content must not enter the report prompt." not in prompt
