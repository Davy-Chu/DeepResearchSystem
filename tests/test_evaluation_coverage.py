from __future__ import annotations

from types import SimpleNamespace

import pytest

from evaluation.coverage import CoverageEvaluator, calculate_coverage_rates
from evaluation.models import (
    AspectExtraction,
    AspectImportance,
    AspectJudgment,
    CoverageJudgments,
    CoverageStatus,
    EvaluationAspect,
    EvaluationInput,
    StageStatus,
)


class FakeResponses:
    def __init__(self, outputs: list[object]) -> None:
        self.outputs = outputs
        self.calls: list[dict[str, object]] = []

    def parse(self, **kwargs: object) -> SimpleNamespace:
        self.calls.append(kwargs)
        return SimpleNamespace(output_parsed=self.outputs.pop(0))


def test_coverage_labels_and_rates(evaluation_input: EvaluationInput) -> None:
    aspects = [
        EvaluationAspect(id="A1", description="Benefits", importance=AspectImportance.CORE),
        EvaluationAspect(id="A2", description="Risks", importance=AspectImportance.CORE),
        EvaluationAspect(id="A3", description="Adoption", importance=AspectImportance.SECONDARY),
    ]
    judgments = [
        AspectJudgment(
            aspect_id="A1",
            status=CoverageStatus.COVERED,
            reason="Substantive discussion.",
            report_evidence="Benefits section.",
        ),
        AspectJudgment(
            aspect_id="A2",
            status=CoverageStatus.PARTIALLY_COVERED,
            reason="Only one risk.",
            report_evidence="Risk sentence.",
        ),
        AspectJudgment(
            aspect_id="A3",
            status=CoverageStatus.NOT_COVERED,
            reason="Absent.",
            report_evidence="No report evidence.",
        ),
    ]
    responses = FakeResponses([AspectExtraction(aspects=aspects), CoverageJudgments(judgments=judgments)])
    evaluator = CoverageEvaluator("unused", "test-model", client=SimpleNamespace(responses=responses))

    result = evaluator.evaluate(evaluation_input)

    assert result.status == StageStatus.COMPLETED
    assert result.core_coverage_rate == pytest.approx(0.75)
    assert result.overall_coverage_rate == pytest.approx(0.5)
    assert len(responses.calls) == 2
    assert all(call["reasoning"] == {"effort": "low"} for call in responses.calls)


def test_coverage_calculation_rejects_missing_aspect_judgment() -> None:
    aspects = [EvaluationAspect(id="A1", description="One", importance=AspectImportance.CORE)]
    with pytest.raises(ValueError, match="exactly one"):
        calculate_coverage_rates(aspects, [])
