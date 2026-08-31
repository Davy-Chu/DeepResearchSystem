from __future__ import annotations

import pytest
from pydantic import ValidationError

from evaluation.v1.models import (
    CitationSupportJudgment,
    CitationSupportStatus,
    RequirementEvaluation,
    Rubric,
    RubricRequirement,
)
from evaluation.v1.scoring import (
    citation_quality,
    citation_support_score,
    overall_score,
    weighted_comprehensiveness,
)


def requirement(identifier: str, importance: int) -> RubricRequirement:
    return RubricRequirement(
        id=identifier,
        category="evidence",
        requirement=f"Requirement {identifier}",
        description="Independently judgeable research obligation.",
        importance=importance,
        evidence_expected=True,
    )


def judgment(identifier: str, coverage: float, depth: float) -> RequirementEvaluation:
    return RequirementEvaluation(
        requirement_id=identifier,
        coverage=coverage,
        depth=depth,
        candidate_evidence=["Candidate passage"] if coverage or depth else [],
        missing=["Missing detail"] if coverage < 1 or depth < 1 else [],
        rationale="Auditable score.",
    )


def test_rubric_rejects_duplicate_ids_invalid_importance_and_non_atomic_scores() -> None:
    with pytest.raises(ValidationError, match="less than or equal to 3"):
        requirement("R1", 4)
    with pytest.raises(ValidationError, match="unique"):
        Rubric(
            rubric_version="1.0",
            fixture_id="fixture",
            requirements=[requirement("R1", 3), requirement("R1", 2)],
        )
    with pytest.raises(ValidationError, match="0, .25"):
        judgment("R1", 0.6, 0.5)


def test_weighted_comprehensiveness_and_formulas() -> None:
    rubric = [requirement("R1", 3), requirement("R2", 1)]
    coverage, depth, score = weighted_comprehensiveness(
        rubric,
        [judgment("R1", 1.0, 0.75), judgment("R2", 0.0, 0.0)],
    )
    assert coverage == pytest.approx(0.75)
    assert depth == pytest.approx(0.5625)
    assert score == pytest.approx(0.69375)
    citations = citation_quality(1.0, 0.5, 0.75)
    assert citations == pytest.approx(0.65)
    assert overall_score(score, citations, 0.9) == pytest.approx(70.125)


def test_not_evaluable_support_is_excluded_from_denominator() -> None:
    judgments = [
        CitationSupportJudgment(
            finding_id="F1",
            claim="Claim 1",
            citation_ids=["S1"],
            status=CitationSupportStatus.SUPPORTED,
            rationale="Supported.",
            supporting_text="Evidence.",
        ),
        CitationSupportJudgment(
            finding_id="F2",
            claim="Claim 2",
            citation_ids=["S2"],
            status=CitationSupportStatus.NOT_EVALUABLE,
            rationale="Missing snapshot.",
            supporting_text="",
        ),
        CitationSupportJudgment(
            finding_id="F3",
            claim="Claim 3",
            citation_ids=["S3"],
            status=CitationSupportStatus.PARTIALLY_SUPPORTED,
            rationale="Partial.",
            supporting_text="Narrow support.",
        ),
    ]
    assert citation_support_score(judgments) == pytest.approx(0.75)
    judgments[0].status = CitationSupportStatus.UNSUPPORTED
    assert citation_support_score(judgments) == pytest.approx(0.25)
    assert citation_quality(1.0, None, 1.0) is None
    assert overall_score(None, 1.0, 1.0) is None


def test_synthetic_report_ordering_guards_against_excessive_generosity() -> None:
    rubric = [requirement(f"R{number}", 3 if number < 3 else 2) for number in range(1, 5)]
    levels = {
        "empty": (0.0, 0.0),
        "shallow": (0.25, 0.25),
        "partial": (0.5, 0.5),
        "comprehensive": (1.0, 1.0),
    }
    scores = {
        label: weighted_comprehensiveness(
            rubric,
            [judgment(item.id, values[0], values[1]) for item in rubric],
        )[2]
        for label, values in levels.items()
    }
    assert scores["comprehensive"] > scores["partial"] > scores["shallow"] > scores["empty"]
