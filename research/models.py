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


class Source(StrictModel):
    id: str
    title: str
    url: str
    content: str
    score: float | None = None


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
    stop_reason: str | None = None

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


class FinalReport(StrictModel):
    question: str
    summary: str
    findings: list[Finding] = Field(default_factory=list)
    conflicts_and_uncertainties: list[Conflict] = Field(default_factory=list)
    remaining_gaps: list[str] = Field(default_factory=list)
    conclusion: str
