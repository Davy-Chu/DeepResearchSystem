"""Typed schemas for frozen fixtures and evaluator-v1 results."""

from __future__ import annotations

from enum import Enum
from pathlib import Path

from pydantic import Field, model_validator

from research.models import FinalReport, Source, StrictModel

from evaluation.v1.config import EVALUATOR_SCHEMA_VERSION, EVALUATOR_VERSION


class ComponentStatus(str, Enum):
    COMPLETED = "COMPLETED"
    NOT_EVALUABLE = "NOT_EVALUABLE"


class CheckStatus(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    NOT_EVALUABLE = "NOT_EVALUABLE"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class CitationSupportStatus(str, Enum):
    SUPPORTED = "SUPPORTED"
    PARTIALLY_SUPPORTED = "PARTIALLY_SUPPORTED"
    UNSUPPORTED = "UNSUPPORTED"
    CONTRADICTED = "CONTRADICTED"
    NOT_EVALUABLE = "NOT_EVALUABLE"


class CitationRequirement(str, Enum):
    CITATION_REQUIRED = "CITATION_REQUIRED"
    CITATION_OPTIONAL = "CITATION_OPTIONAL"
    NO_CITATION_REQUIRED = "NO_CITATION_REQUIRED"


class RubricRequirement(StrictModel):
    id: str
    category: str
    requirement: str
    description: str
    importance: int = Field(ge=1, le=3)
    evidence_expected: bool

    @model_validator(mode="after")
    def validate_requirement(self) -> "RubricRequirement":
        self.id = self.id.strip()
        self.category = self.category.strip()
        self.requirement = self.requirement.strip()
        self.description = self.description.strip()
        if not self.id.startswith("R") or not self.id[1:].isdigit():
            raise ValueError("Rubric requirement IDs must use R1, R2, ...")
        if not self.category or not self.requirement or not self.description:
            raise ValueError("Rubric requirements cannot contain empty text fields")
        return self


class Rubric(StrictModel):
    rubric_version: str
    fixture_id: str
    requirements: list[RubricRequirement] = Field(min_length=1)

    @model_validator(mode="after")
    def validate_rubric(self) -> "Rubric":
        ids = [item.id for item in self.requirements]
        if len(ids) != len(set(ids)):
            raise ValueError("Rubric requirement IDs must be unique")
        expected = [f"R{number}" for number in range(1, len(ids) + 1)]
        if ids != expected:
            raise ValueError("Rubric requirement IDs must be sequential starting at R1")
        if not self.fixture_id.strip():
            raise ValueError("Rubric fixture_id must not be empty")
        return self


class RubricDraft(StrictModel):
    requirements: list[RubricRequirement] = Field(min_length=5, max_length=10)

    @model_validator(mode="after")
    def validate_ids(self) -> "RubricDraft":
        ids = [item.id for item in self.requirements]
        if ids != [f"R{number}" for number in range(1, len(ids) + 1)]:
            raise ValueError("Draft requirement IDs must be unique and sequential from R1")
        return self


class FixtureMetadata(StrictModel):
    fixture_id: str
    fixture_version: str
    question_sha256: str
    reference_report_sha256: str
    rubric_sha256: str
    created_at: str
    status: str
    builder_model: str
    prompt_versions: dict[str, str]


class FrozenFixture(StrictModel):
    directory: Path
    question: str
    reference_report: str
    rubric: Rubric
    metadata: FixtureMetadata


class EvaluationInput(StrictModel):
    run_directory: Path
    question: str
    report_markdown: str
    report: FinalReport | None = None
    sources: list[Source] = Field(default_factory=list)
    system_version: str | None = None
    benchmark_fixture_id: str | None = None
    evidence_ledger: dict | None = None
    trace_metadata: dict = Field(default_factory=dict)
    candidate_report_sha256: str

    @property
    def structured_claim_evidence_available(self) -> bool:
        return bool(self.evidence_ledger and self.evidence_ledger.get("claims"))


class RequirementEvaluation(StrictModel):
    requirement_id: str
    coverage: float = Field(ge=0.0, le=1.0)
    depth: float = Field(ge=0.0, le=1.0)
    candidate_evidence: list[str] = Field(default_factory=list)
    missing: list[str] = Field(default_factory=list)
    rationale: str

    @model_validator(mode="after")
    def enforce_quarter_steps(self) -> "RequirementEvaluation":
        allowed = {0.0, 0.25, 0.5, 0.75, 1.0}
        if self.coverage not in allowed or self.depth not in allowed:
            raise ValueError("Coverage and depth must use 0, .25, .5, .75, or 1")
        if (self.coverage > 0 or self.depth > 0) and not self.candidate_evidence:
            raise ValueError("Every nonzero score requires candidate evidence")
        if (self.coverage < 1 or self.depth < 1) and not self.missing:
            raise ValueError("Every score below 1 requires a missing-item explanation")
        return self


class NovelValue(StrictModel):
    present: bool
    findings: list[str] = Field(default_factory=list)


class ComprehensivenessJudgment(StrictModel):
    requirements: list[RequirementEvaluation]
    novel_value: NovelValue


class ComprehensivenessResult(StrictModel):
    status: ComponentStatus
    score: float | None = Field(default=None, ge=0.0, le=1.0)
    coverage: float | None = Field(default=None, ge=0.0, le=1.0)
    depth: float | None = Field(default=None, ge=0.0, le=1.0)
    requirements: list[RequirementEvaluation] = Field(default_factory=list)
    novel_value: NovelValue = Field(default_factory=lambda: NovelValue(present=False))
    error: str | None = None


class CitationReferenceCheck(StrictModel):
    finding_id: str
    source_id: str
    status: CheckStatus
    reason: str


class CitationSupportJudgment(StrictModel):
    finding_id: str
    claim: str
    citation_ids: list[str]
    status: CitationSupportStatus
    rationale: str
    supporting_text: str


class CitationCompletenessClaim(StrictModel):
    claim_id: str
    claim: str
    classification: CitationRequirement
    has_appropriate_citation: bool
    citation_ids: list[str] = Field(default_factory=list)
    rationale: str


class CitationCompletenessJudgment(StrictModel):
    claims: list[CitationCompletenessClaim]

    @model_validator(mode="after")
    def validate_claim_ids(self) -> "CitationCompletenessJudgment":
        ids = [item.claim_id for item in self.claims]
        if len(ids) != len(set(ids)) or any(
            not identifier.startswith("Q") or not identifier[1:].isdigit()
            for identifier in ids
        ):
            raise ValueError("Completeness claim IDs must be unique Q<number> identifiers")
        return self


class CitationQualityResult(StrictModel):
    status: ComponentStatus
    score: float | None = Field(default=None, ge=0.0, le=1.0)
    validity: float | None = Field(default=None, ge=0.0, le=1.0)
    support: float | None = Field(default=None, ge=0.0, le=1.0)
    completeness: float | None = Field(default=None, ge=0.0, le=1.0)
    reference_checks: list[CitationReferenceCheck] = Field(default_factory=list)
    support_judgments: list[CitationSupportJudgment] = Field(default_factory=list)
    completeness_claims: list[CitationCompletenessClaim] = Field(default_factory=list)
    evaluable_support_claims: int = 0
    total_support_claims: int = 0
    error: str | None = None


class DeterministicCheck(StrictModel):
    check_name: str
    status: CheckStatus
    details: str | None = None


class DeterministicIntegrityResult(StrictModel):
    score: float | None = Field(default=None, ge=0.0, le=1.0)
    checks: list[DeterministicCheck]
    passed_count: int
    failed_count: int
    not_evaluable_count: int
    structured_claim_evidence_available: bool


class UsageMetadata(StrictModel):
    llm_calls: int = 0
    input_tokens: int | None = None
    output_tokens: int | None = None
    estimated_cost: float | None = None


class EvaluatorMetadata(StrictModel):
    evaluator_version: str = EVALUATOR_SCHEMA_VERSION
    fixture_id: str | None = None
    fixture_version: str | None = None
    rubric_hash: str | None = None
    candidate_report_hash: str
    evaluator_model: str
    scoring_weights: dict[str, float]
    prompt_versions: dict[str, str]
    evaluated_at: str
    usage: UsageMetadata


class EvaluationResult(StrictModel):
    evaluation_name: str = EVALUATOR_VERSION
    question: str
    system_version: str | None = None
    overall_score: float | None = Field(default=None, ge=0.0, le=100.0)
    evaluation_completeness: float = Field(ge=0.0, le=1.0)
    comprehensiveness: ComprehensivenessResult
    citations: CitationQualityResult
    deterministic_integrity: DeterministicIntegrityResult
    main_weaknesses: list[str] = Field(default_factory=list)
    metadata: EvaluatorMetadata
