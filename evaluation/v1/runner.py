"""Evaluator-v1 orchestration over normalized saved-run input."""

from __future__ import annotations

from datetime import datetime, timezone

from evaluation.v1.citations import CitationEvaluator
from evaluation.v1.comprehensiveness import ComprehensivenessEvaluator
from evaluation.v1.config import prompt_versions, scoring_weights
from evaluation.v1.deterministic import DeterministicEvaluator
from evaluation.v1.models import (
    CheckStatus,
    CitationRequirement,
    CitationSupportStatus,
    ComponentStatus,
    EvaluationInput,
    EvaluationResult,
    EvaluatorMetadata,
    FrozenFixture,
    UsageMetadata,
)
from evaluation.v1.openai_utils import UsageTracker
from evaluation.v1.scoring import overall_score


class EvaluatorRunner:
    def __init__(
        self,
        evaluator_model: str,
        comprehensiveness_evaluator: ComprehensivenessEvaluator,
        citation_evaluator: CitationEvaluator,
        deterministic_evaluator: DeterministicEvaluator | None = None,
        usage: UsageTracker | None = None,
    ) -> None:
        self.evaluator_model = evaluator_model
        self.comprehensiveness_evaluator = comprehensiveness_evaluator
        self.citation_evaluator = citation_evaluator
        self.deterministic_evaluator = deterministic_evaluator or DeterministicEvaluator()
        self.usage = usage or comprehensiveness_evaluator.usage

    def evaluate(
        self, item: EvaluationInput, fixture: FrozenFixture | None
    ) -> EvaluationResult:
        deterministic = self.deterministic_evaluator.evaluate(item)
        comprehensiveness = self.comprehensiveness_evaluator.evaluate(item, fixture)
        citations = self.citation_evaluator.evaluate(item)
        aggregate = overall_score(
            comprehensiveness.score,
            citations.score,
            deterministic.score,
        )

        support_fraction = (
            citations.evaluable_support_claims / citations.total_support_claims
            if citations.total_support_claims
            else (1.0 if citations.support is not None else 0.0)
        )
        completeness_parts = [
            1.0 if comprehensiveness.status == ComponentStatus.COMPLETED else 0.0,
            1.0 if citations.validity is not None else 0.0,
            support_fraction,
            1.0 if citations.completeness is not None else 0.0,
            1.0 if deterministic.score is not None else 0.0,
        ]
        evaluation_completeness = sum(completeness_parts) / len(completeness_parts)
        weaknesses = _main_weaknesses(
            item,
            fixture,
            comprehensiveness,
            citations,
            deterministic,
        )
        return EvaluationResult(
            question=item.question,
            system_version=item.system_version,
            overall_score=aggregate,
            evaluation_completeness=evaluation_completeness,
            comprehensiveness=comprehensiveness,
            citations=citations,
            deterministic_integrity=deterministic,
            main_weaknesses=weaknesses,
            metadata=EvaluatorMetadata(
                fixture_id=fixture.metadata.fixture_id if fixture else None,
                fixture_version=fixture.metadata.fixture_version if fixture else None,
                rubric_hash=fixture.metadata.rubric_sha256 if fixture else None,
                candidate_report_hash=item.candidate_report_sha256,
                evaluator_model=self.evaluator_model,
                scoring_weights=scoring_weights(),
                prompt_versions=prompt_versions(),
                evaluated_at=datetime.now(timezone.utc).isoformat(),
                usage=UsageMetadata(
                    llm_calls=self.usage.llm_calls,
                    input_tokens=(self.usage.input_tokens if self.usage.usage_available else None),
                    output_tokens=(self.usage.output_tokens if self.usage.usage_available else None),
                    estimated_cost=None,
                ),
            ),
        )


def _main_weaknesses(item, fixture, comprehensiveness, citations, deterministic) -> list[str]:
    weaknesses: list[str] = []
    if fixture is None:
        weaknesses.append("No exact frozen fixture matched; reference comprehensiveness is unavailable.")
    else:
        requirement_map = {entry.id: entry for entry in fixture.rubric.requirements}
        weakest = sorted(
            (
                judgment
                for judgment in comprehensiveness.requirements
                if judgment.coverage < 0.75 or judgment.depth < 0.75
            ),
            key=lambda judgment: (
                -requirement_map[judgment.requirement_id].importance,
                judgment.coverage + judgment.depth,
            ),
        )
        for judgment in weakest[:3]:
            requirement = requirement_map[judgment.requirement_id]
            weaknesses.append(f"{requirement.id}: {requirement.requirement}")
    weak_citations = [
        judgment
        for judgment in citations.support_judgments
        if judgment.status
        in {
            CitationSupportStatus.PARTIALLY_SUPPORTED,
            CitationSupportStatus.UNSUPPORTED,
            CitationSupportStatus.CONTRADICTED,
        }
    ]
    if weak_citations:
        weaknesses.append(
            f"{len(weak_citations)} cited finding(s) were not fully supported by saved evidence."
        )
    missing_citations = [
        claim
        for claim in citations.completeness_claims
        if claim.classification == CitationRequirement.CITATION_REQUIRED
        and not claim.has_appropriate_citation
    ]
    if missing_citations:
        weaknesses.append(
            f"{len(missing_citations)} citation-required claim(s) lacked an appropriate citation."
        )
    if deterministic.failed_count:
        weaknesses.append(f"{deterministic.failed_count} deterministic integrity check(s) failed.")
    return weaknesses[:5]
