"""Small structured-output helper with one semantic repair attempt."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, TypeVar

from pydantic import BaseModel


OutputT = TypeVar("OutputT", bound=BaseModel)


@dataclass
class UsageTracker:
    llm_calls: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    usage_available: bool = False

    def record(self, response: Any) -> None:
        usage = getattr(response, "usage", None)
        if usage is None:
            return
        input_tokens = getattr(usage, "input_tokens", None)
        output_tokens = getattr(usage, "output_tokens", None)
        if isinstance(input_tokens, int):
            self.input_tokens += input_tokens
            self.usage_available = True
        if isinstance(output_tokens, int):
            self.output_tokens += output_tokens
            self.usage_available = True


def parse_with_repair(
    *,
    client: Any,
    model: str,
    system_prompt: str,
    user_prompt: str,
    text_format: type[OutputT],
    usage: UsageTracker,
    validate: Callable[[OutputT], None] | None = None,
) -> OutputT:
    """Parse a structured response, retrying once with an explicit repair instruction."""

    last_error: Exception | None = None
    for attempt in range(2):
        prompt = user_prompt
        if attempt:
            prompt += (
                "\n\nREPAIR INSTRUCTION: The prior response was missing, malformed, or violated "
                "the requested schema. Return a complete corrected object only. Re-check every ID, "
                "allowed enum, required field, and list cardinality."
            )
        try:
            usage.llm_calls += 1
            response = client.responses.parse(
                model=model,
                reasoning={"effort": "low"},
                input=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt},
                ],
                text_format=text_format,
            )
            usage.record(response)
            parsed = response.output_parsed
            if parsed is None:
                raise ValueError("OpenAI returned no parsed structured output")
            if validate is not None:
                validate(parsed)
            return parsed
        except Exception as error:  # The second failure becomes NOT_EVALUABLE upstream.
            last_error = error
            if attempt == 0:
                continue
    assert last_error is not None
    raise last_error
