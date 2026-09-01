"""Single normalization boundary from saved runs to evaluator-v1."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from pydantic import ValidationError

from evaluation.v1.models import EvaluationInput
from research.models import FinalReport, Source
from research.versions import BASELINE_SYSTEM_VERSION, PRIOR_GUIDED_SYSTEM_VERSION


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _source_from_saved(item: object, number: int) -> Source | None:
    if not isinstance(item, dict):
        return None
    raw_score = item.get("score")
    try:
        score = float(raw_score) if raw_score is not None else None
    except (TypeError, ValueError):
        score = None
    return Source(
        id=str(item.get("id") or "").strip(),
        title=str(item.get("title") or f"Saved source {number}").strip(),
        url=str(item.get("url") or "").strip(),
        content=str(item.get("content") or ""),
        score=score,
    )


def load_evaluation_input(run_directory: Path) -> EvaluationInput:
    """Load old and new saved runs without mutating or downloading anything."""

    run_directory = run_directory.resolve()
    report_path = run_directory / "report.md"
    trace_path = run_directory / "trace.json"
    if not run_directory.is_dir():
        raise ValueError(f"Research run directory does not exist: {run_directory}")
    if not report_path.is_file():
        raise ValueError(f"Missing research report: {report_path}")
    if not trace_path.is_file():
        raise ValueError(f"Missing research trace: {trace_path}")

    report_markdown = report_path.read_text(encoding="utf-8")
    try:
        trace = json.loads(trace_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"Malformed research trace: {error}") from error
    if not isinstance(trace, dict):
        raise ValueError("Malformed research trace: expected a JSON object")

    question = str(trace.get("question") or "").strip()
    if not question:
        raise ValueError("Missing research question in trace.json")

    report = None
    report_validation_error = None
    if isinstance(trace.get("final_report"), dict):
        try:
            report = FinalReport.model_validate(trace["final_report"])
        except ValidationError as error:
            report_validation_error = str(error)

    sources = [
        source
        for number, item in enumerate(trace.get("sources") or [], start=1)
        if (source := _source_from_saved(item, number)) is not None
    ]
    evidence_ledger = trace.get("evidence_ledger")
    if not isinstance(evidence_ledger, dict):
        evidence_ledger = None
    fixture_id = trace.get("benchmark_fixture_id")
    if not isinstance(fixture_id, str) or not fixture_id.strip():
        fixture_id = None

    iterations = trace.get("iterations") if isinstance(trace.get("iterations"), list) else []
    system_version = (
        str(trace["system_version"]).strip()
        if trace.get("system_version") is not None
        else None
    )
    research_model = (
        str(trace["research_model"]).strip()
        if isinstance(trace.get("research_model"), str)
        and str(trace["research_model"]).strip()
        else "unknown"
    )
    metadata = {
        "stop_reason": trace.get("stop_reason"),
        "model": trace.get("model"),
        "research_model": research_model,
        "verifier_model": trace.get("verifier_model"),
        "report_validation_error": report_validation_error,
        "tavily_calls": len(iterations),
        "unique_sources": len(sources),
        "logical_research_openai_calls": (
            len(iterations)
            + 1
            + (1 if system_version == PRIOR_GUIDED_SYSTEM_VERSION else 0)
            if system_version
            in {BASELINE_SYSTEM_VERSION, PRIOR_GUIDED_SYSTEM_VERSION}
            else None
        ),
        "coverage_diagnostics": trace.get("coverage_diagnostics"),
    }
    return EvaluationInput(
        run_directory=run_directory,
        question=question,
        report_markdown=report_markdown,
        report=report,
        sources=sources,
        system_version=system_version,
        research_model=research_model,
        benchmark_fixture_id=fixture_id,
        evidence_ledger=evidence_ledger,
        trace_metadata=metadata,
        candidate_report_sha256=sha256_text(report_markdown),
    )
