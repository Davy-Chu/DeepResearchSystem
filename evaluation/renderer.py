"""Deterministic Markdown rendering and non-overwriting artifact saving."""

from __future__ import annotations

import json
from pathlib import Path

from evaluation.models import EVALUATION_VERSION, EvaluationResult, StageStatus


def _percent(value: float | None) -> str:
    return "Unavailable" if value is None else f"{value:.0%}"


def _label(value: str) -> str:
    return value.replace("_", " ").title()


def render_evaluation_markdown(result: EvaluationResult) -> str:
    coverage = result.coverage
    citations = result.citations
    deterministic = result.deterministic
    lines = [
        "# Research Evaluation",
        "",
        f"**Evaluator:** {result.evaluation_version}",
        "",
        f"**Model:** {result.evaluation_metadata.evaluator_model}",
        "",
        f"**Timestamp:** {result.evaluation_metadata.timestamp}",
        "",
        "## Summary",
        "",
        f"- Coverage: {_percent(coverage.overall_coverage_rate)}",
        f"- Core coverage: {_percent(coverage.core_coverage_rate)}",
        f"- Citation support: {_percent(citations.citation_support_rate)}",
        f"- Citation completeness: {_percent(citations.citation_completeness_rate)}",
        f"- Deterministic checks: {deterministic.passed_count} passed, "
        f"{deterministic.failed_count} failed",
        "",
        "## Coverage",
        "",
    ]
    if coverage.status == StageStatus.FAILED:
        lines.extend([f"Coverage evaluation failed: {coverage.error}", ""])
    else:
        judgment_map = {item.aspect_id: item for item in coverage.judgments}
        for aspect in coverage.aspects:
            judgment = judgment_map.get(aspect.id)
            if judgment is None:
                continue
            lines.extend(
                [
                    f"### {aspect.id}: {aspect.description}",
                    "",
                    f"- Importance: {_label(aspect.importance.value)}",
                    f"- Status: {_label(judgment.status.value)}",
                    f"- Reason: {judgment.reason}",
                    f"- Report evidence: {judgment.report_evidence}",
                    "",
                ]
            )

    lines.extend(["## Citation Support", ""])
    if citations.status == StageStatus.FAILED:
        lines.extend([f"Citation evaluation failed: {citations.error}", ""])
    else:
        for finding in citations.findings:
            sources = ", ".join(finding.cited_source_ids) or "None"
            lines.extend(
                [
                    f"### {finding.finding_id}",
                    "",
                    f"**Claim:** {finding.claim}",
                    "",
                    f"- Sources: {sources}",
                    f"- Combined result: {_label(finding.combined_support.value)}",
                    f"- Reason: {finding.reason}",
                    "",
                ]
            )
            for source_judgment in finding.source_judgments:
                lines.append(
                    f"  - {source_judgment.source_id}: "
                    f"{_label(source_judgment.support_label.value)} — "
                    f"{source_judgment.reason}"
                )
            if finding.source_judgments:
                lines.append("")

    lines.extend(["## Deterministic Failures", ""])
    failures = [check for check in deterministic.checks if not check.passed]
    if failures:
        for check in failures:
            lines.append(f"- `{check.check_name}`: {check.details}")
    else:
        lines.append("- None. All deterministic checks passed.")
    lines.append("")
    return "\n".join(lines)


def create_evaluation_directory(run_directory: Path) -> Path:
    root = run_directory / "evaluations"
    root.mkdir(parents=True, exist_ok=True)
    candidate = root / EVALUATION_VERSION
    suffix = 2
    while candidate.exists():
        candidate = root / f"{EVALUATION_VERSION}_{suffix}"
        suffix += 1
    candidate.mkdir()
    return candidate


def save_evaluation_result(
    run_directory: Path, result: EvaluationResult
) -> tuple[Path, Path]:
    output_directory = create_evaluation_directory(run_directory)
    json_path = output_directory / "evaluation.json"
    markdown_path = output_directory / "evaluation.md"
    json_path.write_text(
        json.dumps(result.model_dump(mode="json"), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    markdown_path.write_text(render_evaluation_markdown(result), encoding="utf-8")
    return json_path, markdown_path
