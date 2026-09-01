"""Evaluator orchestration, saved-run loading, and CLI."""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Protocol

from dotenv import load_dotenv
from pydantic import ValidationError

from evaluation.citations import CitationEvaluator
from evaluation.coverage import CoverageEvaluator
from evaluation.deterministic import DeterministicEvaluator
from evaluation.models import (
    EVALUATION_VERSION,
    CitationResult,
    CoverageResult,
    EvaluationInput,
    EvaluationMetadata,
    EvaluationResult,
    StageStatus,
)
from evaluation.renderer import save_evaluation_result
from evaluation.v1.config import load_evaluator_model
from research.config import (
    DEFAULT_OPENAI_MODEL,
    load_openai_max_retries,
    load_openai_timeout_seconds,
)
from research.models import FinalReport, Source


class _EvaluationStage(Protocol):
    def evaluate(self, evaluation_input: EvaluationInput) -> Any: ...


def _safe_error(error: Exception) -> str:
    message = re.sub(r"sk-[A-Za-z0-9_-]+", "[REDACTED]", str(error))
    return f"{type(error).__name__}: {message}"


def load_evaluation_input(run_directory: Path) -> EvaluationInput:
    run_directory = run_directory.resolve()
    if not run_directory.is_dir():
        raise ValueError(f"Research run directory does not exist: {run_directory}")
    report_path = run_directory / "report.md"
    trace_path = run_directory / "trace.json"
    if not report_path.is_file():
        raise ValueError(f"Missing research report: {report_path}")
    if not trace_path.is_file():
        raise ValueError(f"Missing research trace: {trace_path}")

    try:
        trace = json.loads(trace_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"Malformed research trace: {error}") from error
    if not isinstance(trace, dict):
        raise ValueError("Malformed research trace: expected a JSON object")

    question = trace.get("question")
    if not isinstance(question, str) or not question.strip():
        raise ValueError("Missing research question in trace.json")
    report_data = trace.get("final_report")
    if not isinstance(report_data, dict):
        raise ValueError(
            "Saved structured final report is unavailable. This run predates evaluator-v0 "
            "snapshot support and cannot be evaluated reproducibly."
        )
    source_data = trace.get("sources")
    if not isinstance(source_data, list):
        raise ValueError("Malformed research state: trace sources must be a list")
    for number, item in enumerate(source_data, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Malformed saved source at position {number}")
        if not isinstance(item.get("content"), str) or not item["content"].strip():
            label = item.get("id", number)
            raise ValueError(
                f"Saved source content unavailable for source {label}. The evaluator will "
                "not download replacement content."
            )

    try:
        report = FinalReport.model_validate(report_data)
        sources = [Source.model_validate(item) for item in source_data]
    except ValidationError as error:
        raise ValueError(f"Malformed saved research state: {error}") from error
    return EvaluationInput(
        question=question.strip(),
        report=report,
        report_markdown=report_path.read_text(encoding="utf-8"),
        sources=sources,
        research_model=(
            trace.get("research_model", "unknown").strip() or "unknown"
            if isinstance(trace.get("research_model"), str)
            else "unknown"
        )
    )


class EvaluatorRunner:
    def __init__(
        self,
        evaluator_model: str,
        coverage_evaluator: _EvaluationStage,
        citation_evaluator: _EvaluationStage,
        deterministic_evaluator: DeterministicEvaluator | None = None,
    ) -> None:
        self.evaluator_model = evaluator_model
        self.coverage_evaluator = coverage_evaluator
        self.citation_evaluator = citation_evaluator
        self.deterministic_evaluator = deterministic_evaluator or DeterministicEvaluator()

    def evaluate(self, evaluation_input: EvaluationInput) -> EvaluationResult:
        deterministic = self.deterministic_evaluator.evaluate(evaluation_input)
        try:
            coverage = self.coverage_evaluator.evaluate(evaluation_input)
        except Exception as error:
            coverage = CoverageResult(
                status=StageStatus.FAILED,
                error=_safe_error(error),
            )
        try:
            citations = self.citation_evaluator.evaluate(evaluation_input)
        except Exception as error:
            citations = CitationResult(
                status=StageStatus.FAILED,
                error=_safe_error(error),
            )
        return EvaluationResult(
            evaluation_version=EVALUATION_VERSION,
            question=evaluation_input.question,
            coverage=coverage,
            citations=citations,
            deterministic=deterministic,
            evaluation_metadata=EvaluationMetadata(
                evaluator_model=self.evaluator_model,
                timestamp=datetime.now(timezone.utc).isoformat(),
                research_model=evaluation_input.research_model,
            ),
        )


def build_evaluation_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate an existing saved research run.")
    parser.add_argument("run_directory", type=Path, help="Path to outputs/<run>")
    return parser


def evaluation_main(arguments: list[str] | None = None) -> int:
    args = build_evaluation_parser().parse_args(arguments)
    try:
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY", "").strip()
        if not api_key:
            raise ValueError("Missing required environment variable: OPENAI_API_KEY")
        evaluator_model = load_evaluator_model()
        timeout_seconds = load_openai_timeout_seconds()
        max_retries = load_openai_max_retries()
        evaluation_input = load_evaluation_input(args.run_directory)
        runner = EvaluatorRunner(
            evaluator_model=evaluator_model,
            coverage_evaluator=CoverageEvaluator(
                api_key,
                evaluator_model,
                timeout_seconds=timeout_seconds,
                max_retries=max_retries,
            ),
            citation_evaluator=CitationEvaluator(
                api_key,
                evaluator_model,
                timeout_seconds=timeout_seconds,
                max_retries=max_retries,
            ),
        )
        result = runner.evaluate(evaluation_input)
        json_path, markdown_path = save_evaluation_result(args.run_directory, result)
    except Exception as error:
        logging.error("Evaluation failed: %s", _safe_error(error))
        return 1

    logging.info("Evaluation complete.")
    logging.info("Machine evaluation:\n%s", json_path)
    logging.info("Human-readable evaluation:\n%s", markdown_path)
    if result.coverage.status == StageStatus.FAILED or result.citations.status == StageStatus.FAILED:
        logging.error("One or more LLM evaluation stages failed; completed results were preserved.")
        return 1
    return 0


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    raise SystemExit(evaluation_main())
