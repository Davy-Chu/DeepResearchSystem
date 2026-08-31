"""Research action selection from structured ledger state."""

from __future__ import annotations

import json
from typing import Any

from openai import OpenAI

from research.config import DEFAULT_OPENAI_MAX_RETRIES, DEFAULT_OPENAI_TIMEOUT_SECONDS
from research.models import (
    DecisionTargetType,
    ResearchDecision,
    ResearchState,
    SubQuestionStatus,
)

RESEARCH_DECISION_SYSTEM_PROMPT = """You are deciding the next research action.

Use only the supplied structured Research State. Your goal is not to eliminate every
uncertainty. Prioritize unresolved issues that materially affect the ability to answer
the original question. Consider importance to the question, open gaps, weak important
claims, conflicting important claims, previous search attempts, and remaining budget.
Low confidence alone is not enough reason to research a minor detail.

When more research would materially improve the answer, choose ONE highest-value claim,
gap, or general target and produce ONE focused search query under 400 characters.
Otherwise stop. Keep the reason short and suitable for logging. Do not analyze raw
sources or update the evidence ledger.
"""


class ResearchDecisionMaker:
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

    def decide(self, state: ResearchState) -> ResearchDecision:
        payload = {
            "original_question": state.question,
            "evidence_ledger": state.evidence_ledger.model_dump(mode="json"),
            "open_research_gaps": [
                gap.model_dump(mode="json") for gap in state.open_gaps()
            ],
            "search_history": [
                {
                    "iteration_number": item.iteration_number,
                    "search_query": item.search_query,
                }
                for item in state.ledger_iterations
            ],
            "current_iteration": state.current_iteration,
            "maximum_iterations": state.max_iterations,
            "remaining_search_budget": state.remaining_budget(),
        }
        response = self.client.responses.parse(
            model=self.model,
            reasoning={"effort": "low"},
            input=[
                {"role": "system", "content": RESEARCH_DECISION_SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": json.dumps(payload, indent=2, ensure_ascii=False),
                },
            ],
            text_format=ResearchDecision,
        )
        if response.output_parsed is None:
            raise ValueError("OpenAI returned no parsed ResearchDecision")
        validate_decision_target(response.output_parsed, state)
        return response.output_parsed


def validate_decision_target(decision: ResearchDecision, state: ResearchState) -> None:
    if not decision.needs_more_research:
        return
    if decision.target_type == DecisionTargetType.CLAIM:
        if state.evidence_ledger.get_claim(decision.target_id or "") is None:
            raise ValueError(
                f"Research decision targets nonexistent claim: {decision.target_id}"
            )
    elif decision.target_type == DecisionTargetType.GAP:
        gap = next(
            (item for item in state.research_gaps if item.id == decision.target_id),
            None,
        )
        if gap is None:
            raise ValueError(
                f"Research decision targets nonexistent gap: {decision.target_id}"
            )
        if gap not in state.open_gaps():
            raise ValueError(
                f"Research decision targets resolved gap: {decision.target_id}"
            )
    elif decision.target_type == DecisionTargetType.GENERAL and decision.target_id:
        raise ValueError("A GENERAL research decision must not provide target_id")
    elif decision.target_type == DecisionTargetType.SUBQUESTION:
        target = state.get_subquestion(decision.target_id or "")
        if target is None:
            raise ValueError(
                f"Research decision targets nonexistent subquestion: {decision.target_id}"
            )
        unresolved_core = [
            item
            for item in state.core_subquestions()
            if item.status != SubQuestionStatus.SUFFICIENT
        ]
        if target.status == SubQuestionStatus.SUFFICIENT and unresolved_core:
            raise ValueError(
                "Research decision targets a sufficient subquestion while a core "
                "subquestion remains unresolved"
            )
