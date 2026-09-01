"""Research-side OpenAI request compatibility helpers."""

from __future__ import annotations

from typing import Any


def research_reasoning_kwargs(model: str) -> dict[str, Any]:
    """Return reasoning options only for models that support them.

    GPT-4o-mini supports structured Responses API output, but not the reasoning
    configuration used by the GPT-5 research models.  Keeping this decision at one
    boundary prevents architecture-specific prompts or behavior from diverging.
    """

    normalized = model.strip().lower()
    if normalized == "gpt-4o-mini" or normalized.startswith("gpt-4o-mini-"):
        return {}
    return {"reasoning": {"effort": "low"}}
