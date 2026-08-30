from __future__ import annotations

from types import SimpleNamespace

import pytest

from evaluation.citations import CitationEvaluator
from evaluation.models import CitationLLMJudgment, SourceSupportJudgment, SupportLabel
from research.models import Confidence, EvidenceItem, Finding, Source


class FakeResponses:
    def __init__(self, outputs: list[CitationLLMJudgment]) -> None:
        self.outputs = outputs
        self.calls: list[dict[str, object]] = []

    def parse(self, **kwargs: object) -> SimpleNamespace:
        self.calls.append(kwargs)
        return SimpleNamespace(output_parsed=self.outputs.pop(0))


def finding(claim: str, source_ids: list[str]) -> Finding:
    evidence = (
        [EvidenceItem(summary="Saved evidence summary.", source_ids=source_ids)]
        if source_ids
        else []
    )
    return Finding(
        claim=claim,
        evidence=evidence,
        confidence=Confidence.MEDIUM,
        confidence_reason="Test confidence.",
    )


def judgment(
    finding_id: str, source_ids: list[str], label: SupportLabel
) -> CitationLLMJudgment:
    return CitationLLMJudgment(
        finding_id=finding_id,
        source_judgments=[
            SourceSupportJudgment(
                finding_id=finding_id,
                source_id=source_id,
                support_label=label,
                reason="The saved text determines this label.",
            )
            for source_id in source_ids
        ],
        combined_support=label,
        combined_reason="The combined saved evidence determines this label.",
    )


def test_citation_labels_joint_support_and_metrics(evaluation_input) -> None:
    assert evaluation_input.report is not None
    evaluation_input.sources = [
        Source(
            id=f"S{number}",
            title=f"Source {number}",
            url=f"https://example.com/{number}",
            content=f"Exact saved source content {number}.",
        )
        for number in range(1, 5)
    ]
    evaluation_input.report.findings = [
        finding("Two sources jointly support this claim.", ["S1", "S4"]),
        finding("This claim is broader than its evidence.", ["S2"]),
        finding("This claim is not supported.", ["S3"]),
        finding("This claim is contradicted.", ["S4"]),
        finding("This factual claim has no citation.", []),
    ]
    outputs = [
        judgment("F1", ["S1", "S4"], SupportLabel.FULLY_SUPPORTED),
        judgment("F2", ["S2"], SupportLabel.PARTIALLY_SUPPORTED),
        judgment("F3", ["S3"], SupportLabel.UNSUPPORTED),
        judgment("F4", ["S4"], SupportLabel.CONTRADICTED),
    ]
    responses = FakeResponses(outputs)
    evaluator = CitationEvaluator("unused", "test-model", client=SimpleNamespace(responses=responses))

    result = evaluator.evaluate(evaluation_input)

    assert result.evaluated_findings == 5
    assert result.findings_with_evidence == 4
    assert result.findings_without_evidence == 1
    assert result.citation_completeness_rate == pytest.approx(0.8)
    assert result.citation_support_rate == pytest.approx(0.3)
    assert result.fully_supported_count == 1
    assert result.partially_supported_count == 1
    assert result.unsupported_count == 2
    assert result.contradicted_count == 1
    assert len(result.findings[0].source_judgments) == 2
    assert len(responses.calls) == 4
    first_prompt = str(responses.calls[0]["input"])
    assert "Exact saved source content 1." in first_prompt
    assert "Exact saved source content 4." in first_prompt
    assert "Exact saved source content 2." not in first_prompt
