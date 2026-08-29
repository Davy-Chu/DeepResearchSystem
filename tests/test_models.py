import pytest
from pydantic import ValidationError

from research.models import Confidence, EvidenceItem, Finding, IterationAnalysis


def test_valid_finding_is_accepted() -> None:
    finding = Finding(
        claim="The intervention improved the measured outcome.",
        evidence=[EvidenceItem(summary="A controlled comparison reported an improvement.", source_ids=["S1"])],
        confidence=Confidence.MEDIUM,
        confidence_reason="The result is direct but comes from one source.",
    )
    assert finding.confidence is Confidence.MEDIUM


def test_invalid_confidence_is_rejected() -> None:
    with pytest.raises(ValidationError):
        Finding(
            claim="A claim",
            evidence=[],
            confidence="87%",  # type: ignore[arg-type]
            confidence_reason="Invalid numerical confidence.",
        )


def test_next_query_is_required_when_more_research_is_needed() -> None:
    with pytest.raises(ValidationError, match="next_search_query"):
        IterationAnalysis(
            findings=[],
            conflicts=[],
            unresolved_questions=["What remains unknown?"],
            needs_more_research=True,
            research_reason="A material gap remains.",
            next_search_query=None,
        )
