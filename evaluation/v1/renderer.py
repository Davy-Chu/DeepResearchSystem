"""Auditable Markdown/JSON persistence for evaluator-v1."""

from __future__ import annotations

import json
from pathlib import Path

from evaluation.v1.config import EVALUATOR_VERSION
from evaluation.v1.models import (
    CheckStatus,
    ComponentStatus,
    EvaluationResult,
)


def _decimal(value: float | None) -> str:
    return "Unavailable" if value is None else f"{value:.2f}"


def _overall(value: float | None) -> str:
    return "Unavailable" if value is None else f"{value:.1f} / 100"


def render_evaluation(result: EvaluationResult) -> str:
    comp = result.comprehensiveness
    deterministic = result.deterministic_integrity
    lines = [
        "# Frozen Reference Research Evaluation",
        "",
        f"**Evaluator:** {result.evaluation_name}",
        "",
        f"**Fixture:** {result.metadata.fixture_id or 'REFERENCE_EVALUATION_UNAVAILABLE'}",
        "",
        f"**System Version:** {result.system_version or 'Unknown'}",
        "",
        f"**Research Model:** {result.metadata.research_model}",
        "",
        f"**Evaluator Model:** {result.metadata.evaluator_model}",
        "",
        "## Summary",
        "",
        f"- Overall: {_overall(result.overall_score)}",
        f"- Evaluation completeness: {result.evaluation_completeness:.0%}",
        f"- Coverage: {_decimal(comp.coverage)}",
        f"- Depth: {_decimal(comp.depth)}",
        "",
        "## Coverage and Depth",
        "",
    ]
    if comp.status == ComponentStatus.NOT_EVALUABLE:
        lines.extend([f"**NOT EVALUABLE:** {comp.error}", ""])
    else:
        for judgment in comp.requirements:
            lines.extend(
                [
                    f"### {judgment.requirement_id}",
                    "",
                    f"- Coverage: {judgment.coverage:.2f}",
                    f"- Depth: {judgment.depth:.2f}",
                    f"- Rationale: {judgment.rationale}",
                    "- Candidate evidence:",
                ]
            )
            lines.extend(f"  - {entry}" for entry in judgment.candidate_evidence)
            lines.append("- Missing:")
            lines.extend(f"  - {entry}" for entry in judgment.missing)
            lines.append("")
        lines.extend(["### Novel Value", ""])
        if comp.novel_value.present:
            lines.extend(f"- {entry}" for entry in comp.novel_value.findings)
        else:
            lines.append("- No material benchmark-external value identified.")
        lines.append("")

    lines.extend(["## Deterministic Diagnostics (Not Scored)", ""])
    lines.extend(
        f"- `{check.check_name}`: {check.status.value}"
        + (f" — {check.details}" if check.details else "")
        for check in deterministic.checks
    )
    lines.extend(["", "## Main Weaknesses", ""])
    lines.extend(
        [f"{number}. {weakness}" for number, weakness in enumerate(result.main_weaknesses, 1)]
        or ["1. No material weakness was identified by the available evaluation components."]
    )
    lines.extend(
        [
            "",
            "## Audit Metadata",
            "",
            f"- Fixture version: {result.metadata.fixture_version or 'Unavailable'}",
            f"- Rubric hash: `{result.metadata.rubric_hash or 'Unavailable'}`",
            f"- Candidate report hash: `{result.metadata.candidate_report_hash}`",
            f"- LLM calls: {result.metadata.usage.llm_calls}",
            f"- Evaluated at: {result.metadata.evaluated_at}",
            "",
        ]
    )
    return "\n".join(lines)


def create_evaluation_directory(run_directory: Path, fixture_id: str | None) -> Path:
    root = run_directory / "evaluations" / EVALUATOR_VERSION
    root.mkdir(parents=True, exist_ok=True)
    label = fixture_id or "no-reference"
    candidate = root / label
    suffix = 2
    while candidate.exists():
        candidate = root / f"{label}_{suffix}"
        suffix += 1
    candidate.mkdir()
    return candidate


def save_evaluation(run_directory: Path, result: EvaluationResult) -> tuple[Path, Path]:
    directory = create_evaluation_directory(run_directory, result.metadata.fixture_id)
    json_path = directory / "evaluation.json"
    markdown_path = directory / "evaluation.md"
    json_path.write_text(
        json.dumps(result.model_dump(mode="json"), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    markdown_path.write_text(render_evaluation(result), encoding="utf-8")
    return json_path, markdown_path
