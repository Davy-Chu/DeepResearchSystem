"""Pydantic data models shared by the research pipeline."""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, model_validator


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Confidence(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class ClaimStatus(str, Enum):
    SUPPORTED = "SUPPORTED"
    WEAK = "WEAK"
    CONFLICTING = "CONFLICTING"
    INSUFFICIENT_EVIDENCE = "INSUFFICIENT_EVIDENCE"


class EvidenceRelationType(str, Enum):
    SUPPORTS = "SUPPORTS"
    CONTRADICTS = "CONTRADICTS"


class EvidenceStrength(str, Enum):
    DIRECT = "DIRECT"
    INDIRECT = "INDIRECT"


class GapImportance(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class GapStatus(str, Enum):
    OPEN = "OPEN"
    RESOLVED = "RESOLVED"


class DecisionTargetType(str, Enum):
    CLAIM = "CLAIM"
    GAP = "GAP"
    GENERAL = "GENERAL"


class LedgerChangeType(str, Enum):
    NEW = "NEW"
    UPDATED = "UPDATED"


class GapChangeType(str, Enum):
    NEW = "NEW"
    RESOLVED = "RESOLVED"


class Source(StrictModel):
    id: str
    title: str
    url: str
    content: str
    score: float | None = None


class EvidenceRelation(StrictModel):
    source_id: str
    relation: EvidenceRelationType
    summary: str
    strength: EvidenceStrength

    @model_validator(mode="after")
    def require_content(self) -> "EvidenceRelation":
        self.source_id = self.source_id.strip()
        self.summary = self.summary.strip()
        if not self.source_id:
            raise ValueError("Evidence relation source_id must not be empty")
        if not self.summary:
            raise ValueError("Evidence relation summary must not be empty")
        return self


class LedgerClaim(StrictModel):
    id: str
    claim: str
    supporting_evidence: list[EvidenceRelation] = Field(default_factory=list)
    contradicting_evidence: list[EvidenceRelation] = Field(default_factory=list)
    confidence: Confidence
    confidence_reason: str
    status: ClaimStatus
    first_seen_iteration: int = Field(ge=1)
    last_updated_iteration: int = Field(ge=1)

    @model_validator(mode="after")
    def validate_claim(self) -> "LedgerClaim":
        self.id = self.id.strip()
        self.claim = self.claim.strip()
        if not self.id or not self.claim:
            raise ValueError("Ledger claim ID and claim text must not be empty")
        if self.last_updated_iteration < self.first_seen_iteration:
            raise ValueError("last_updated_iteration cannot precede first_seen_iteration")
        if any(
            item.relation != EvidenceRelationType.SUPPORTS
            for item in self.supporting_evidence
        ):
            raise ValueError("supporting_evidence must contain SUPPORTS relations")
        if any(
            item.relation != EvidenceRelationType.CONTRADICTS
            for item in self.contradicting_evidence
        ):
            raise ValueError("contradicting_evidence must contain CONTRADICTS relations")
        return self


class EvidenceLedger(StrictModel):
    claims: list[LedgerClaim] = Field(default_factory=list)

    @model_validator(mode="after")
    def require_unique_claim_ids(self) -> "EvidenceLedger":
        claim_ids = [claim.id for claim in self.claims]
        if len(claim_ids) != len(set(claim_ids)):
            raise ValueError("Evidence ledger claim IDs must be unique")
        return self

    def get_claim(self, claim_id: str) -> LedgerClaim | None:
        return next((claim for claim in self.claims if claim.id == claim_id), None)

    def add_claim(self, claim: LedgerClaim) -> None:
        if self.get_claim(claim.id) is not None:
            raise ValueError(f"Claim ID already exists: {claim.id}")
        self.claims.append(claim)

    def update_claim(self, claim: LedgerClaim) -> None:
        for index, current in enumerate(self.claims):
            if current.id == claim.id:
                self.claims[index] = claim
                return
        raise ValueError(f"Cannot update nonexistent claim: {claim.id}")

    def get_conflicting_claims(self) -> list[LedgerClaim]:
        return [claim for claim in self.claims if claim.status == ClaimStatus.CONFLICTING]

    def get_weak_claims(self) -> list[LedgerClaim]:
        return [claim for claim in self.claims if claim.status == ClaimStatus.WEAK]


class ResearchGap(StrictModel):
    id: str
    description: str
    importance: GapImportance
    status: GapStatus = GapStatus.OPEN
    related_claim_ids: list[str] = Field(default_factory=list)
    created_iteration: int = Field(ge=1)
    resolved_iteration: int | None = Field(default=None, ge=1)

    @model_validator(mode="after")
    def validate_resolution(self) -> "ResearchGap":
        self.id = self.id.strip()
        self.description = self.description.strip()
        if not self.id or not self.description:
            raise ValueError("Research gap ID and description must not be empty")
        if self.status == GapStatus.RESOLVED and self.resolved_iteration is None:
            raise ValueError("Resolved research gaps require resolved_iteration")
        if self.status == GapStatus.OPEN and self.resolved_iteration is not None:
            raise ValueError("Open research gaps cannot have resolved_iteration")
        if (
            self.resolved_iteration is not None
            and self.resolved_iteration < self.created_iteration
        ):
            raise ValueError("resolved_iteration cannot precede created_iteration")
        return self


class NewClaim(StrictModel):
    claim: str
    supporting_evidence: list[EvidenceRelation] = Field(default_factory=list)
    contradicting_evidence: list[EvidenceRelation] = Field(default_factory=list)
    confidence: Confidence
    confidence_reason: str
    status: ClaimStatus

    @model_validator(mode="after")
    def require_claim_content(self) -> "NewClaim":
        self.claim = self.claim.strip()
        self.confidence_reason = self.confidence_reason.strip()
        if not self.claim or not self.confidence_reason:
            raise ValueError("New claims require claim text and a confidence reason")
        return self


class ClaimUpdate(StrictModel):
    existing_claim_id: str
    new_supporting_evidence: list[EvidenceRelation] = Field(default_factory=list)
    new_contradicting_evidence: list[EvidenceRelation] = Field(default_factory=list)
    updated_confidence: Confidence
    updated_confidence_reason: str
    updated_status: ClaimStatus

    @model_validator(mode="after")
    def require_update_content(self) -> "ClaimUpdate":
        self.existing_claim_id = self.existing_claim_id.strip()
        self.updated_confidence_reason = self.updated_confidence_reason.strip()
        if not self.existing_claim_id or not self.updated_confidence_reason:
            raise ValueError("Claim updates require a claim ID and confidence reason")
        return self


class NewGap(StrictModel):
    description: str
    importance: GapImportance
    related_claim_ids: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def require_gap_content(self) -> "NewGap":
        self.description = self.description.strip()
        if not self.description:
            raise ValueError("New research gaps require a description")
        return self


class EvidenceProcessingResult(StrictModel):
    new_claims: list[NewClaim] = Field(default_factory=list)
    claim_updates: list[ClaimUpdate] = Field(default_factory=list)
    new_gaps: list[NewGap] = Field(default_factory=list)
    resolved_gap_ids: list[str] = Field(default_factory=list)


class LedgerClaimChange(StrictModel):
    claim_id: str
    change_type: LedgerChangeType
    previous_confidence: Confidence | None = None
    current_confidence: Confidence
    previous_status: ClaimStatus | None = None
    current_status: ClaimStatus
    added_supporting_evidence: list[EvidenceRelation] = Field(default_factory=list)
    added_contradicting_evidence: list[EvidenceRelation] = Field(default_factory=list)


class ResearchGapChange(StrictModel):
    gap_id: str
    change_type: GapChangeType
    description: str


class LedgerUpdateSummary(StrictModel):
    claim_changes: list[LedgerClaimChange] = Field(default_factory=list)
    gap_changes: list[ResearchGapChange] = Field(default_factory=list)


class ResearchDecision(StrictModel):
    needs_more_research: bool
    reason: str
    target_type: DecisionTargetType | None = None
    target_id: str | None = None
    next_search_query: str | None = Field(default=None, max_length=399)

    @model_validator(mode="after")
    def validate_research_action(self) -> "ResearchDecision":
        self.reason = self.reason.strip()
        if not self.reason:
            raise ValueError("Research decisions require a reason")
        if self.needs_more_research:
            if not self.next_search_query or not self.next_search_query.strip():
                raise ValueError(
                    "next_search_query must be non-empty when needs_more_research is true"
                )
            if self.target_type is None:
                raise ValueError(
                    "target_type must be provided when needs_more_research is true"
                )
            if self.target_type in {DecisionTargetType.CLAIM, DecisionTargetType.GAP}:
                if not self.target_id or not self.target_id.strip():
                    raise ValueError(
                        "target_id must be provided for a claim or gap research target"
                    )
            self.next_search_query = self.next_search_query.strip()
        else:
            self.next_search_query = None
            self.target_type = None
            self.target_id = None
        return self


class LedgerResearchIteration(StrictModel):
    iteration_number: int = Field(ge=1)
    search_query: str
    source_ids: list[str] = Field(default_factory=list)
    processing_result: EvidenceProcessingResult
    ledger_updates: LedgerUpdateSummary
    decision: ResearchDecision | None = None


class EvidenceItem(StrictModel):
    summary: str
    source_ids: list[str] = Field(default_factory=list)


class Finding(StrictModel):
    claim: str
    evidence: list[EvidenceItem] = Field(default_factory=list)
    confidence: Confidence
    confidence_reason: str


class Conflict(StrictModel):
    description: str
    source_ids: list[str] = Field(default_factory=list)


class IterationAnalysis(StrictModel):
    findings: list[Finding] = Field(default_factory=list)
    conflicts: list[Conflict] = Field(default_factory=list)
    unresolved_questions: list[str] = Field(default_factory=list)
    needs_more_research: bool
    research_reason: str
    next_search_query: str | None = Field(default=None, max_length=399)

    @model_validator(mode="after")
    def require_next_query_when_continuing(self) -> "IterationAnalysis":
        if self.needs_more_research:
            if not self.next_search_query or not self.next_search_query.strip():
                raise ValueError(
                    "next_search_query must be non-empty when needs_more_research is true"
                )
            self.next_search_query = self.next_search_query.strip()
        elif self.next_search_query is not None and not self.next_search_query.strip():
            self.next_search_query = None
        return self


class ResearchIteration(StrictModel):
    iteration_number: int = Field(ge=1)
    search_query: str
    source_ids: list[str] = Field(default_factory=list)
    analysis: IterationAnalysis


class ResearchState(StrictModel):
    question: str
    sources: list[Source] = Field(default_factory=list)
    iterations: list[ResearchIteration] = Field(default_factory=list)
    evidence_ledger: EvidenceLedger = Field(default_factory=EvidenceLedger)
    research_gaps: list[ResearchGap] = Field(default_factory=list)
    ledger_iterations: list[LedgerResearchIteration] = Field(default_factory=list)
    current_iteration: int = Field(default=0, ge=0)
    max_iterations: int = Field(default=3, ge=1)
    system_version: str = "baseline-zero"
    stop_reason: str | None = None

    @model_validator(mode="after")
    def validate_process_state(self) -> "ResearchState":
        if self.current_iteration > self.max_iterations:
            raise ValueError("current_iteration cannot exceed max_iterations")
        gap_ids = [gap.id for gap in self.research_gaps]
        if len(gap_ids) != len(set(gap_ids)):
            raise ValueError("Research gap IDs must be unique")
        claim_ids = {claim.id for claim in self.evidence_ledger.claims}
        for gap in self.research_gaps:
            unknown_claim_ids = sorted(set(gap.related_claim_ids) - claim_ids)
            if unknown_claim_ids:
                raise ValueError(
                    f"Research gap {gap.id} references unknown claim ID(s): "
                    + ", ".join(unknown_claim_ids)
                )
        return self

    def all_findings(self) -> list[Finding]:
        return [finding for item in self.iterations for finding in item.analysis.findings]

    def all_conflicts(self) -> list[Conflict]:
        return [conflict for item in self.iterations for conflict in item.analysis.conflicts]

    def all_unresolved_questions(self) -> list[str]:
        return [
            question
            for item in self.iterations
            for question in item.analysis.unresolved_questions
        ]

    def open_gaps(self) -> list[ResearchGap]:
        return [gap for gap in self.research_gaps if gap.status == GapStatus.OPEN]

    def remaining_budget(self) -> int:
        return max(self.max_iterations - self.current_iteration, 0)

    def conflicting_claims(self) -> list[LedgerClaim]:
        return self.evidence_ledger.get_conflicting_claims()

    def weak_claims(self) -> list[LedgerClaim]:
        return self.evidence_ledger.get_weak_claims()


class FinalReport(StrictModel):
    question: str
    summary: str
    findings: list[Finding] = Field(default_factory=list)
    conflicts_and_uncertainties: list[Conflict] = Field(default_factory=list)
    remaining_gaps: list[str] = Field(default_factory=list)
    conclusion: str


class LedgerReportFinding(Finding):
    ledger_claim_ids: list[str] = Field(min_length=1)


class LedgerFinalReport(StrictModel):
    question: str
    summary: str
    findings: list[LedgerReportFinding] = Field(default_factory=list)
    conflicts_and_uncertainties: list[Conflict] = Field(default_factory=list)
    remaining_gaps: list[str] = Field(default_factory=list)
    conclusion: str

    def to_final_report(self) -> FinalReport:
        return FinalReport(
            question=self.question,
            summary=self.summary,
            findings=[
                Finding(
                    claim=finding.claim,
                    evidence=finding.evidence,
                    confidence=finding.confidence,
                    confidence_reason=finding.confidence_reason,
                )
                for finding in self.findings
            ],
            conflicts_and_uncertainties=self.conflicts_and_uncertainties,
            remaining_gaps=self.remaining_gaps,
            conclusion=self.conclusion,
        )
