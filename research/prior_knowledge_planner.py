"""Pre-retrieval topic coverage planning that never produces research evidence."""

from __future__ import annotations

from typing import Any

from openai import OpenAI

from research.config import DEFAULT_OPENAI_MAX_RETRIES, DEFAULT_OPENAI_TIMEOUT_SECONDS
from research.openai_utils import research_reasoning_kwargs
from research.models import (
    PriorKnowledgePlanProposal,
    PriorKnowledgeResearchPlan,
    ResearchDimension,
)


PRIOR_KNOWLEDGE_PLANNER_SYSTEM_PROMPT = """You are creating a research coverage map before web research begins.

Use your general pretrained knowledge only to identify the important dimensions that a
strong research process should investigate.

You are NOT answering the question.
You are NOT establishing facts.
You are NOT providing evidence.
You are identifying what should be investigated.

For each research dimension:
1. state the research question;
2. explain why it matters to answering the user's question;
3. describe what evidence would be needed;
4. mark it CORE or SECONDARY.

You may identify important dimensions that are not explicitly named in the user's wording
when they are reasonably necessary for a high-quality answer.

Do not include factual conclusions, numerical claims, named study results, current
statistics, or claims about what the evidence shows. Phrase dimensions as questions to
investigate, never as conclusions.

Treat all resulting dimensions as hypotheses about research scope, not truth.
Return 4-8 distinct dimensions.

Preserve explicit comparisons, timeframes, jurisdictions, uncertainty, contradictions,
and requested output forms from the original question.

Do not search the web. Do not cite sources. Do not invent dimension IDs; the application
assigns stable IDs after planning.
"""


class PriorKnowledgeResearchPlanner:
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

    def plan(self, question: str) -> PriorKnowledgeResearchPlan:
        question = question.strip()
        if not question:
            raise ValueError("Research question must not be empty")
        response = self.client.responses.parse(
            model=self.model,
            **research_reasoning_kwargs(self.model),
            input=[
                {"role": "system", "content": PRIOR_KNOWLEDGE_PLANNER_SYSTEM_PROMPT},
                {"role": "user", "content": question},
            ],
            text_format=PriorKnowledgePlanProposal,
        )
        if response.output_parsed is None:
            raise ValueError("OpenAI returned no parsed PriorKnowledgePlanProposal")
        proposal = response.output_parsed
        return PriorKnowledgeResearchPlan(
            dimensions=[
                ResearchDimension(
                    id=f"D{index}",
                    title=item.title,
                    research_question=item.research_question,
                    why_it_matters=item.why_it_matters,
                    evidence_needed=item.evidence_needed,
                    importance=item.importance,
                )
                for index, item in enumerate(proposal.dimensions, start=1)
            ],
            synthesis_requirements=proposal.synthesis_requirements,
        )
