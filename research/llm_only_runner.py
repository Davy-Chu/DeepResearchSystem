"""Deliberately primitive one-call, no-retrieval research baseline."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from time import perf_counter
from typing import Any

from openai import OpenAI

from research.config import DEFAULT_OPENAI_MAX_RETRIES, DEFAULT_OPENAI_TIMEOUT_SECONDS
from research.versions import LLM_ONLY_SYSTEM_VERSION


PROMPT_PREFIX = "Do deep research and create a report on the following question:\n\n"
STOP_REASON = "single_llm_call_complete"


@dataclass(frozen=True)
class LLMOnlyRunResult:
    question: str
    system_version: str
    model: str
    report: str
    duration_seconds: float
    input_tokens: int | None
    output_tokens: int | None
    openai_calls: int = 1
    tavily_calls: int = 0
    success: bool = True
    error: str | None = None


class LLMOnlyResearchRunner:
    """Send one minimal prompt and return the model's raw text unchanged."""

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

    def run(self, question: str) -> LLMOnlyRunResult:
        question = question.strip()
        if not question:
            raise ValueError("Research question must not be empty")

        prompt = PROMPT_PREFIX + question
        started = perf_counter()
        response = self.client.responses.create(
            model=self.model,
            reasoning={"effort": "low"},
            input=[{"role": "user", "content": prompt}],
        )
        duration = perf_counter() - started
        report = response.output_text
        if not isinstance(report, str) or not report.strip():
            raise ValueError("OpenAI returned an empty LLM-only report")

        usage = getattr(response, "usage", None)
        return LLMOnlyRunResult(
            question=question,
            system_version=LLM_ONLY_SYSTEM_VERSION,
            model=self.model,
            report=report,
            duration_seconds=duration,
            input_tokens=_optional_int(usage, "input_tokens"),
            output_tokens=_optional_int(usage, "output_tokens"),
        )


def save_llm_only_artifacts(
    result: LLMOnlyRunResult, output_directory: Path
) -> tuple[Path, Path, Path]:
    """Persist raw report text plus honest minimal trace and readable log."""

    output_directory.mkdir(parents=True, exist_ok=True)
    report_path = output_directory / "report.md"
    trace_path = output_directory / "trace.json"
    log_path = output_directory / "research_log.md"

    with report_path.open("w", encoding="utf-8", newline="") as output:
        output.write(result.report)

    trace = {
        "system_version": result.system_version,
        "question": result.question,
        "model": result.model,
        "openai_calls": result.openai_calls,
        "tavily_calls": result.tavily_calls,
        "input_tokens": result.input_tokens,
        "output_tokens": result.output_tokens,
        "duration_seconds": result.duration_seconds,
        "sources": [],
        "iterations": [],
        "research_plan": None,
        "evidence_ledger": None,
        "research_gaps": [],
        "claim_verifications": [],
        "stop_reason": STOP_REASON,
    }
    trace_path.write_text(
        json.dumps(trace, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    log_path.write_text(_render_log(result), encoding="utf-8")
    return report_path, trace_path, log_path


def _optional_int(value: object, attribute: str) -> int | None:
    candidate = getattr(value, attribute, None)
    return candidate if isinstance(candidate, int) else None


def _render_log(result: LLMOnlyRunResult) -> str:
    input_tokens = result.input_tokens if result.input_tokens is not None else "Unavailable"
    output_tokens = result.output_tokens if result.output_tokens is not None else "Unavailable"
    return f"""# Research Log

**System:** {result.system_version}

**Question:** {result.question}

## Architecture

Question → one OpenAI call → raw report

## Execution

1. Sent the user question to the configured OpenAI model with the minimal deep-research instruction.
2. No external retrieval or tools were used.
3. No Tavily calls occurred.
4. No decomposition occurred.
5. No Evidence Ledger or Research State was created.
6. No verification or counter-search occurred.
7. The model response was saved unchanged as `report.md`.

## Performance

- Model: {result.model}
- OpenAI calls: {result.openai_calls}
- Tavily calls: {result.tavily_calls}
- Research iterations: 0
- Input tokens: {input_tokens}
- Output tokens: {output_tokens}
- Duration: {result.duration_seconds:.3f} seconds
- Stop reason: {STOP_REASON}
"""

