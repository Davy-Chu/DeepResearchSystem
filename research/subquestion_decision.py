"""Subquestion-aware next-action selection for decomposed research."""

from __future__ import annotations

import json
from typing import Any

from openai import OpenAI

from research.config import DEFAULT_OPENAI_MAX_RETRIES, DEFAULT_OPENAI_TIMEOUT_SECONDS
from research.decision import validate_decision_target
from research.openai_utils import research_reasoning_kwargs
from research.models import (
    DecisionTargetType,
    ResearchDecision,
    ResearchState,
)


SUBQUESTION_DECISION_SYSTEM_PROMPT = """You choose the next search for a decomposed research plan.

Use only the supplied structured state. If further research would materially improve the
answer, select exactly one unresolved subquestion and return one focused search query
under 400 characters. Prioritize unresolved CORE subquestions, their success criteria,
conflicts, important open gaps, few prior attempts, and remaining budget. Do not target
a SUFFICIENT subquestion while any CORE subquestion remains unresolved. Stop when the
plan can be answered responsibly or another search has low expected value.

For a continuing decision target_type must be SUBQUESTION and target_id must be a plan
subquestion ID. Do not inspect raw source text, update the ledger, or answer the question.
"""


class SubquestionResearchDecisionMaker:
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
        if state.research_plan is None:
            raise ValueError("Subquestion decision-making requires a research plan")
        payload = {
            "original_question": state.question,
            "research_plan": state.research_plan.model_dump(mode="json"),
            "evidence_ledger_summary": state.evidence_ledger.model_dump(mode="json"),
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
            **research_reasoning_kwargs(self.model),
            input=[
                {"role": "system", "content": SUBQUESTION_DECISION_SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": json.dumps(payload, indent=2, ensure_ascii=False),
                },
            ],
            text_format=ResearchDecision,
        )
        if response.output_parsed is None:
            raise ValueError("OpenAI returned no parsed ResearchDecision")
        validate_subquestion_decision_target(response.output_parsed, state)
        return response.output_parsed


def validate_subquestion_decision_target(
    decision: ResearchDecision, state: ResearchState
) -> None:
    if not decision.needs_more_research:
        return
    if state.research_plan is None:
        raise ValueError("Subquestion decision requires a research plan")
    if decision.target_type != DecisionTargetType.SUBQUESTION:
        raise ValueError("A decomposed research decision must target a SUBQUESTION")
    validate_decision_target(decision, state)
