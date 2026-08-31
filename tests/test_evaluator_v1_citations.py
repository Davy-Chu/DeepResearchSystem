from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

import pytest

from evaluation.v1.citations import CitationEvaluator
from evaluation.v1.models import (
    CheckStatus,
    CitationCompletenessClaim,
    CitationCompletenessJudgment,
    CitationRequirement,
    CitationSupportJudgment,
    CitationSupportStatus,
    EvaluationInput,
)
from research.models import Confidence, EvidenceItem, FinalReport, Finding, Source


class FakeResponses:
    def __init__(self, outputs: list[object | Exception]) -> None:
        self.outputs = list(outputs)
        self.calls = []

    def parse(self, **kwargs):
        self.calls.append(kwargs)
        output = self.outputs.pop(0)
        if isinstance(output, Exception):
            raise output
        return SimpleNamespace(output_parsed=output, usage=None)


def input_with_sources(sources: list[Source], citation_id: str = "S1") -> EvaluationInput:
    question = "Benchmark question"
    report = FinalReport(
        question=question,
        summary="Summary",
        findings=[
            Finding(
                claim="A substantive factual claim.",
                evidence=[EvidenceItem(summary="Evidence", source_ids=[citation_id])],
                confidence=Confidence.MEDIUM,
                confidence_reason="Saved evidence.",
            )
        ],
        conclusion="Conclusion",
    )
    return EvaluationInput(
        run_directory=Path.cwd(),
        question=question,
        report_markdown="# Report\n\nA substantive factual claim. [S1]",
        report=report,
        sources=sources,
        candidate_report_sha256="a" * 64,
    )


def completeness(has_citation: bool = True) -> CitationCompletenessJudgment:
    return CitationCompletenessJudgment(
        claims=[
            CitationCompletenessClaim(
                claim_id="Q1",
                claim="A substantive factual claim.",
                classification=CitationRequirement.CITATION_REQUIRED,
                has_appropriate_citation=has_citation,
                citation_ids=["S1"] if has_citation else [],
                rationale="Citation is required.",
            )
        ]
    )


def test_citation_validity_support_and_completeness_are_separate() -> None:
    source = Source(id="S1", title="Study", url="https://example.com", content="Direct support.")
    support = CitationSupportJudgment(
        finding_id="F1",
        claim="A substantive factual claim.",
        citation_ids=["S1"],
        status=CitationSupportStatus.PARTIALLY_SUPPORTED,
        rationale="Only a narrower claim is supported.",
        supporting_text="Direct support.",
    )
    fake = FakeResponses([completeness(False), support])
    result = CitationEvaluator(
        "unused", "test-model", client=SimpleNamespace(responses=fake)
    ).evaluate(input_with_sources([source]))
    assert result.validity == 1.0
    assert result.support == 0.5
    assert result.completeness == 0.0
    assert result.score == pytest.approx(0.425)


def test_unknown_source_fails_validity_and_missing_content_is_not_evaluable() -> None:
    unknown = CitationEvaluator(
        "unused",
        "test-model",
        client=SimpleNamespace(responses=FakeResponses([completeness()])),
    ).evaluate(input_with_sources([], "S99"))
    assert unknown.reference_checks[0].status == CheckStatus.FAIL
    assert unknown.validity == 0.0
    assert unknown.support_judgments[0].status == CitationSupportStatus.NOT_EVALUABLE

    empty_source = Source(id="S1", title="Study", url="https://example.com", content="")
    missing = CitationEvaluator(
        "unused",
        "test-model",
        client=SimpleNamespace(responses=FakeResponses([completeness()])),
    ).evaluate(input_with_sources([empty_source]))
    assert missing.validity == 1.0
    assert missing.support is None
    assert missing.support_judgments[0].status == CitationSupportStatus.NOT_EVALUABLE


def test_invalid_output_retries_once_then_marks_only_component_not_evaluable() -> None:
    source = Source(id="S1", title="Study", url="https://example.com", content="Support")
    fake = FakeResponses(
        [completeness(), RuntimeError("bad output"), RuntimeError("still bad")]
    )
    result = CitationEvaluator(
        "unused", "test-model", client=SimpleNamespace(responses=fake)
    ).evaluate(input_with_sources([source]))
    assert len(fake.calls) == 3
    assert result.support is None
    assert result.completeness == 1.0
    assert result.error and "F1" in result.error


def test_legacy_markdown_citations_can_be_evaluated_without_structured_findings() -> None:
    source = Source(id="S1", title="Study", url="https://example.com", content="Direct support")
    item = EvaluationInput(
        run_directory=Path.cwd(),
        question="Legacy question",
        report_markdown="# Report\n\nA legacy factual claim. [S1]",
        report=None,
        sources=[source],
        candidate_report_sha256="b" * 64,
    )
    complete = CitationCompletenessJudgment(
        claims=[
            CitationCompletenessClaim(
                claim_id="Q1",
                claim="A legacy factual claim.",
                classification=CitationRequirement.CITATION_REQUIRED,
                has_appropriate_citation=True,
                citation_ids=["S1"],
                rationale="Nearby citation.",
            )
        ]
    )
    support = CitationSupportJudgment(
        finding_id="Q1",
        claim="A legacy factual claim.",
        citation_ids=["S1"],
        status=CitationSupportStatus.SUPPORTED,
        rationale="Direct support.",
        supporting_text="Direct support",
    )
    result = CitationEvaluator(
        "unused",
        "test-model",
        client=SimpleNamespace(responses=FakeResponses([complete, support])),
    ).evaluate(item)
    assert result.validity == 1.0
    assert result.support == 1.0
    assert result.completeness == 1.0
