"""Typed inputs and outputs for evaluator-v0."""

from __future__ import annotations

from enum import Enum

from pydantic import Field

from research.models import FinalReport, Source, StrictModel

EVALUATION_VERSION = "evaluator-v0"


class StageStatus(str, Enum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class AspectImportance(str, Enum):
    CORE = "CORE"
    SECONDARY = "SECONDARY"


class CoverageStatus(str, Enum):
    COVERED = "COVERED"
    PARTIALLY_COVERED = "PARTIALLY_COVERED"
    NOT_COVERED = "NOT_COVERED"


class SupportLabel(str, Enum):
    FULLY_SUPPORTED = "FULLY_SUPPORTED"
    PARTIALLY_SUPPORTED = "PARTIALLY_SUPPORTED"
    UNSUPPORTED = "UNSUPPORTED"
    CONTRADICTED = "CONTRADICTED"


class EvaluationInput(StrictModel):
    question: str
    report: FinalReport | None
    report_markdown: str
    sources: list[Source] = Field(default_factory=list)
    research_model: str = "unknown"


class EvaluationAspect(StrictModel):
    id: str
    description: str
    importance: AspectImportance


class AspectExtraction(StrictModel):
    aspects: list[EvaluationAspect] = Field(min_length=1, max_length=8)


class AspectJudgment(StrictModel):
    aspect_id: str
    status: CoverageStatus
    reason: str
    report_evidence: str


class CoverageJudgments(StrictModel):
    judgments: list[AspectJudgment]


class CoverageResult(StrictModel):
    status: StageStatus
    aspects: list[EvaluationAspect] = Field(default_factory=list)
    judgments: list[AspectJudgment] = Field(default_factory=list)
    core_coverage_rate: float | None = None
    overall_coverage_rate: float | None = None
    error: str | None = None


class SourceSupportJudgment(StrictModel):
    finding_id: str
    source_id: str
    support_label: SupportLabel
    reason: str


class CitationLLMJudgment(StrictModel):
    finding_id: str
    source_judgments: list[SourceSupportJudgment]
    combined_support: SupportLabel
    combined_reason: str


class FindingCitationResult(StrictModel):
    finding_id: str
    claim: str
    cited_source_ids: list[str]
    source_judgments: list[SourceSupportJudgment]
    combined_support: SupportLabel
    reason: str


class CitationResult(StrictModel):
    status: StageStatus
    findings: list[FindingCitationResult] = Field(default_factory=list)
    evaluated_findings: int = 0
    findings_with_evidence: int = 0
    findings_without_evidence: int = 0
    citation_completeness_rate: float | None = None
    citation_support_rate: float | None = None
    fully_supported_count: int = 0
    partially_supported_count: int = 0
    unsupported_count: int = 0
    contradicted_count: int = 0
    error: str | None = None


class DeterministicCheck(StrictModel):
    check_name: str
    passed: bool
    details: str | None = None


class DeterministicResult(StrictModel):
    checks: list[DeterministicCheck]
    passed_count: int
    failed_count: int
    all_passed: bool


class EvaluationMetadata(StrictModel):
    evaluator_model: str
    timestamp: str
    research_model: str = "unknown"


class EvaluationResult(StrictModel):
    evaluation_version: str
    question: str
    coverage: CoverageResult
    citations: CitationResult
    deterministic: DeterministicResult
    evaluation_metadata: EvaluationMetadata
