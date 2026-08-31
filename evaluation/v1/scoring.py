"""Pure scoring functions for evaluator-v1."""

from __future__ import annotations

from evaluation.v1.config import (
    CITATION_COMPLETENESS_WEIGHT,
    CITATION_SUPPORT_WEIGHT,
    CITATION_VALIDITY_WEIGHT,
    CITATION_WEIGHT,
    COMPREHENSIVENESS_WEIGHT,
    COVERAGE_WEIGHT,
    DEPTH_WEIGHT,
    DETERMINISTIC_WEIGHT,
)
from evaluation.v1.models import (
    CitationSupportJudgment,
    CitationSupportStatus,
    RequirementEvaluation,
    RubricRequirement,
)


def weighted_comprehensiveness(
    rubric: list[RubricRequirement], judgments: list[RequirementEvaluation]
) -> tuple[float, float, float]:
    if not rubric:
        raise ValueError("Cannot score an empty rubric")
    by_id = {item.requirement_id: item for item in judgments}
    expected_ids = {item.id for item in rubric}
    if len(by_id) != len(judgments) or set(by_id) != expected_ids:
        raise ValueError("Comprehensiveness judgments must match every rubric requirement")
    denominator = sum(item.importance for item in rubric)
    coverage = sum(by_id[item.id].coverage * item.importance for item in rubric) / denominator
    depth = sum(by_id[item.id].depth * item.importance for item in rubric) / denominator
    return coverage, depth, COVERAGE_WEIGHT * coverage + DEPTH_WEIGHT * depth


def citation_support_score(judgments: list[CitationSupportJudgment]) -> float | None:
    scores = {
        CitationSupportStatus.SUPPORTED: 1.0,
        CitationSupportStatus.PARTIALLY_SUPPORTED: 0.5,
        CitationSupportStatus.UNSUPPORTED: 0.0,
        CitationSupportStatus.CONTRADICTED: 0.0,
    }
    evaluable = [item for item in judgments if item.status in scores]
    if not evaluable:
        return None
    return sum(scores[item.status] for item in evaluable) / len(evaluable)


def citation_quality(
    validity: float | None, support: float | None, completeness: float | None
) -> float | None:
    if validity is None or support is None or completeness is None:
        return None
    return (
        CITATION_VALIDITY_WEIGHT * validity
        + CITATION_SUPPORT_WEIGHT * support
        + CITATION_COMPLETENESS_WEIGHT * completeness
    )


def overall_score(
    comprehensiveness: float | None,
    citations: float | None,
    deterministic: float | None,
) -> float | None:
    if comprehensiveness is None or citations is None or deterministic is None:
        return None
    return 100 * (
        COMPREHENSIVENESS_WEIGHT * comprehensiveness
        + CITATION_WEIGHT * citations
        + DETERMINISTIC_WEIGHT * deterministic
    )
