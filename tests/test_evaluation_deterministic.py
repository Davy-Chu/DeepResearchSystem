from __future__ import annotations

from collections.abc import Callable

import pytest

from evaluation.deterministic import DeterministicEvaluator
from evaluation.models import EvaluationInput


def failed_names(evaluation_input: EvaluationInput) -> set[str]:
    result = DeterministicEvaluator().evaluate(evaluation_input)
    return {item.check_name for item in result.checks if not item.passed}


def test_valid_run_passes(evaluation_input: EvaluationInput) -> None:
    result = DeterministicEvaluator().evaluate(evaluation_input)
    assert result.all_passed
    assert result.failed_count == 0
    assert result.passed_count == len(result.checks)


@pytest.mark.parametrize(
    ("mutate", "expected_check"),
    [
        (lambda item: setattr(item, "question", ""), "question_exists"),
        (lambda item: setattr(item, "report", None), "report_exists"),
        (lambda item: setattr(item.report.findings[0], "claim", ""), "F1_claim_exists"),
        (
            lambda item: setattr(item.report.findings[0], "confidence", None),
            "F1_confidence_exists",
        ),
        (
            lambda item: setattr(item.report.findings[0], "confidence", "CERTAIN"),
            "F1_confidence_valid",
        ),
        (
            lambda item: setattr(item.report.findings[0].evidence[0], "source_ids", ["S9"]),
            "F1_evidence_1_source_ids_valid",
        ),
        (
            lambda item: item.sources.append(item.sources[0].model_copy()),
            "source_ids_unique",
        ),
        (lambda item: setattr(item.sources[0], "url", ""), "source_S1_url_exists"),
        (
            lambda item: setattr(item.sources[0], "content", ""),
            "source_S1_content_exists",
        ),
        (
            lambda item: setattr(item.report.findings[0].evidence[0], "source_ids", []),
            "F1_evidence_1_source_ids_exist",
        ),
        (
            lambda item: setattr(item.report.findings[0], "evidence", []),
            "F1_evidence_exists",
        ),
    ],
)
def test_invalid_run_reports_specific_failure(
    evaluation_input: EvaluationInput,
    mutate: Callable[[EvaluationInput], None],
    expected_check: str,
) -> None:
    mutate(evaluation_input)
    assert expected_check in failed_names(evaluation_input)
