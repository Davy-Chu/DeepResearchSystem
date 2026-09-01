"""Evidence-only analysis augmented with a non-evidence research coverage map."""

from __future__ import annotations

import json
from typing import Any

from openai import OpenAI

from research.analyzer import ANALYZER_SYSTEM_PROMPT
from research.config import DEFAULT_OPENAI_MAX_RETRIES, DEFAULT_OPENAI_TIMEOUT_SECONDS
from research.openai_utils import research_reasoning_kwargs
from research.models import (
    PriorGuidedIterationAnalysis,
    PriorKnowledgeResearchPlan,
    ResearchState,
    Source,
)


PRIOR_GUIDED_ANALYZER_SYSTEM_PROMPT = ANALYZER_SYSTEM_PROMPT + """

This experimental run also supplies a research coverage map. It is explicitly labeled
PLANNING METADATA - NOT EVIDENCE. The map may guide what to investigate next, but none of
its wording establishes a fact and it may never support a finding or confidence judgment.

After analyzing the retrieved evidence, assess EVERY listed dimension as UNRESEARCHED,
PARTIAL, or SUFFICIENT. Base every status only on retrieved source content and accumulated
evidence-backed findings:
- UNRESEARCHED: no meaningful retrieved evidence addresses the dimension;
- PARTIAL: some evidence addresses it, but requested evidence is absent, weak, indirect,
  or conflicting;
- SUFFICIENT: retrieved evidence is strong enough to address its important substance.

Never mark a dimension SUFFICIENT because you already know or assume the answer. Use only
the supplied D* IDs. When more research is needed, preferentially target an UNRESEARCHED
CORE dimension, then a PARTIAL CORE dimension, then an UNRESEARCHED SECONDARY dimension,
then a major conflict. Return the selected target_dimension_id when targeting a dimension.
Set blocking_conflict true only when a retrieved-evidence contradiction materially blocks
a responsible answer. Avoid near-duplicate follow-up queries.
"""


class PriorGuidedResearchAnalyzer:
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

    def analyze(
        self,
        state: ResearchState,
        new_sources: list[Source],
    ) -> PriorGuidedIterationAnalysis:
        if state.prior_knowledge_plan is None:
            raise ValueError("Prior-guided analysis requires a coverage plan")
        prompt = self._build_prompt(state, state.prior_knowledge_plan, new_sources)
        response = self.client.responses.parse(
            model=self.model,
            **research_reasoning_kwargs(self.model),
            input=[
                {"role": "system", "content": PRIOR_GUIDED_ANALYZER_SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            text_format=PriorGuidedIterationAnalysis,
        )
        if response.output_parsed is None:
            raise ValueError("OpenAI returned no parsed PriorGuidedIterationAnalysis")
        analysis = response.output_parsed
        validate_dimension_updates(analysis, state.prior_knowledge_plan)
        return analysis

    @staticmethod
    def _build_prompt(
        state: ResearchState,
        plan: PriorKnowledgeResearchPlan,
        new_sources: list[Source],
    ) -> str:
        prior_state = {
            "executed_queries": [item.search_query for item in state.iterations],
            "findings": [item.model_dump(mode="json") for item in state.all_findings()],
            "conflicts": [item.model_dump(mode="json") for item in state.all_conflicts()],
            "unresolved_questions": [
                question
                for item in state.iterations
                for question in item.analysis.unresolved_questions
            ],
        }
        planning_metadata = {
            "dimensions": [item.model_dump(mode="json") for item in plan.dimensions],
            "synthesis_requirements": plan.synthesis_requirements,
        }
        source_blocks = [
            f"[{source.id}]\nTitle: {source.title}\nURL: {source.url}\n"
            f"Content:\n{source.content}"
            for source in new_sources
        ]
        sources_text = "\n\n".join(source_blocks) or "No usable new sources were retrieved."
        return (
            f"ORIGINAL QUESTION\n\n{state.question}\n\n"
            "CURRENT RESEARCH STATE - RETRIEVED EVIDENCE ONLY\n\n"
            f"{json.dumps(prior_state, indent=2, ensure_ascii=False)}\n\n"
            "PLANNING METADATA - NOT EVIDENCE\n\n"
            f"{json.dumps(planning_metadata, indent=2, ensure_ascii=False)}\n\n"
            f"NEW RETRIEVED SOURCES\n\n{sources_text}"
        )


def validate_dimension_updates(
    analysis: PriorGuidedIterationAnalysis,
    plan: PriorKnowledgeResearchPlan,
) -> None:
    expected = {item.id for item in plan.dimensions}
    actual = [item.dimension_id for item in analysis.dimension_status_updates]
    if len(actual) != len(set(actual)):
        raise ValueError("Dimension status updates contain duplicate IDs")
    if set(actual) != expected:
        missing = sorted(expected - set(actual))
        unknown = sorted(set(actual) - expected)
        details = []
        if missing:
            details.append("missing: " + ", ".join(missing))
        if unknown:
            details.append("unknown: " + ", ".join(unknown))
        raise ValueError("Dimension status updates must cover the plan (" + "; ".join(details) + ")")
    if (
        analysis.target_dimension_id is not None
        and analysis.target_dimension_id not in expected
    ):
        raise ValueError(
            "Prior-guided analysis targets unknown dimension ID: "
            + analysis.target_dimension_id
        )
