from __future__ import annotations

import pytest

from evaluation.models import EvaluationInput
from research.models import Confidence, EvidenceItem, FinalReport, Finding, Source


@pytest.fixture
def evaluation_input() -> EvaluationInput:
    return EvaluationInput(
        question="What are the benefits and risks of synthetic data?",
        report_markdown="# Research Report\n\nBenefits and risks are discussed.",
        report=FinalReport(
            question="What are the benefits and risks of synthetic data?",
            summary="The report summarizes benefits and risks.",
            findings=[
                Finding(
                    claim="Synthetic data can improve data availability.",
                    evidence=[
                        EvidenceItem(
                            summary="The study reports improved availability.",
                            source_ids=["S1"],
                        )
                    ],
                    confidence=Confidence.HIGH,
                    confidence_reason="Direct saved evidence.",
                )
            ],
            conflicts_and_uncertainties=[],
            remaining_gaps=["Generalization remains uncertain."],
            conclusion="Benefits exist, with important limitations.",
        ),
        sources=[
            Source(
                id="S1",
                title="Saved study",
                url="https://example.com/study",
                content="The study says synthetic data improved data availability.",
                score=0.9,
            )
        ],
    )
