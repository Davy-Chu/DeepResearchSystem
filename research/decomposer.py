"""Structured question decomposition and deterministic subquestion status updates."""

from __future__ import annotations

from typing import Any

from openai import OpenAI

from research.config import DEFAULT_OPENAI_MAX_RETRIES, DEFAULT_OPENAI_TIMEOUT_SECONDS
from research.openai_utils import research_reasoning_kwargs
from research.models import (
    ClaimStatus,
    GapImportance,
    GapStatus,
    QuestionDecomposition,
    ResearchPlan,
    ResearchState,
    SubQuestion,
    SubQuestionStatus,
    SubQuestionStatusChange,
)


QUESTION_DECOMPOSER_SYSTEM_PROMPT = """You decompose one research question into a stable research plan.

Return between two and six distinct, answerable subquestions. Mark a subquestion CORE
when the original question cannot be answered responsibly without it; otherwise mark it
SECONDARY. Give each subquestion concrete success criteria describing the evidence needed
to answer it. Also identify cross-subquestion synthesis requirements and explicit output
requirements from the user's wording. Preserve comparisons, causal distinctions,
timeframes, jurisdictions, requested uncertainty, and requested presentation forms.

Do not answer the question, search for evidence, invent IDs, or add requirements not
grounded in the original question. The application assigns IDs after decomposition.
"""


class QuestionDecomposer:
    def __init__(
        self,
        api_key: str,
        model: str,
        client: Any | None = None,
        timeout_seconds: float = DEFAULT_OPENAI_TIMEOUT_SECONDS,
        max_retries: int = DEFAULT_OPENAI_MAX_RETRIES,
    ) -> None:
        self.client = client or OpenAI(
            api_key=api_key,
            timeout=timeout_seconds,
            max_retries=max_retries,
        )
        self.model = model

    def decompose(self, question: str) -> ResearchPlan:
        question = question.strip()
        if not question:
            raise ValueError("Research question must not be empty")
        response = self.client.responses.parse(
            model=self.model,
            **research_reasoning_kwargs(self.model),
            input=[
                {"role": "system", "content": QUESTION_DECOMPOSER_SYSTEM_PROMPT},
                {"role": "user", "content": question},
            ],
            text_format=QuestionDecomposition,
        )
        if response.output_parsed is None:
            raise ValueError("OpenAI returned no parsed QuestionDecomposition")
        decomposition = response.output_parsed
        return ResearchPlan(
            subquestions=[
                SubQuestion(
                    id=f"SQ{index}",
                    question=proposal.question,
                    importance=proposal.importance,
                    success_criteria=proposal.success_criteria,
                )
                for index, proposal in enumerate(decomposition.subquestions, start=1)
            ],
            synthesis_requirements=decomposition.synthesis_requirements,
            output_requirements=decomposition.output_requirements,
        )


def refresh_subquestion_statuses(
    state: ResearchState,
) -> list[SubQuestionStatusChange]:
    """Recompute plan progress from canonical claims and gaps, without an LLM."""
    if state.research_plan is None:
        return []

    changes: list[SubQuestionStatusChange] = []
    for subquestion in state.research_plan.subquestions:
        claims = state.claims_for(subquestion.id)
        gaps = [
            gap
            for gap in state.gaps_for_subquestion(subquestion.id)
            if gap.status == GapStatus.OPEN
        ]
        blocking_gaps = [
            gap
            for gap in gaps
            if gap.importance in {GapImportance.HIGH, GapImportance.MEDIUM}
        ]

        if not claims and not gaps:
            status = SubQuestionStatus.UNRESEARCHED
            reason = "No ledger claims or research gaps are linked to this subquestion."
        elif any(claim.status == ClaimStatus.CONFLICTING for claim in claims):
            status = SubQuestionStatus.CONFLICTING
            reason = "At least one linked ledger claim contains conflicting evidence."
        elif any(claim.status != ClaimStatus.SUPPORTED for claim in claims):
            status = SubQuestionStatus.PARTIAL
            reason = "At least one linked ledger claim is not yet supported."
        elif blocking_gaps:
            status = SubQuestionStatus.PARTIAL
            reason = (
                "Open high- or medium-importance research gaps still block a "
                "sufficient answer."
            )
        elif claims:
            status = SubQuestionStatus.SUFFICIENT
            reason = (
                "Linked ledger claims are supported and no open high- or "
                "medium-importance gap remains."
            )
        else:
            status = SubQuestionStatus.PARTIAL
            reason = "Research gaps are linked, but no ledger claim answers the subquestion."

        previous = subquestion.status
        subquestion.status = status
        subquestion.status_reason = reason
        if previous != status:
            changes.append(
                SubQuestionStatusChange(
                    subquestion_id=subquestion.id,
                    previous_status=previous,
                    current_status=status,
                    status_reason=reason,
                )
            )
    return changes
