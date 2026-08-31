"""Benchmark table persistence and offline ablation comparison."""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path

from evaluation.v1.models import EvaluationResult


@dataclass(frozen=True)
class BenchmarkEntry:
    run: str
    result: EvaluationResult


def _row(entry: BenchmarkEntry) -> dict[str, object]:
    result = entry.result
    return {
        "run": entry.run,
        "system_version": result.system_version,
        "fixture": result.metadata.fixture_id,
        "overall_score": result.overall_score,
        "coverage": result.comprehensiveness.coverage,
        "depth": result.comprehensiveness.depth,
        "comprehensiveness": result.comprehensiveness.score,
        "citation_validity": result.citations.validity,
        "citation_support": result.citations.support,
        "citation_completeness": result.citations.completeness,
        "citation_quality": result.citations.score,
        "deterministic_integrity": result.deterministic_integrity.score,
        "evaluation_completeness": result.evaluation_completeness,
    }


def _non_overwriting_directory(root: Path, name: str) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    candidate = root / name
    suffix = 2
    while candidate.exists():
        candidate = root / f"{name}_{suffix}"
        suffix += 1
    candidate.mkdir()
    return candidate


def save_benchmark(entries: list[BenchmarkEntry], root: Path) -> tuple[Path, Path, Path]:
    directory = _non_overwriting_directory(root, "benchmark")
    rows = [_row(entry) for entry in entries]
    json_path = directory / "benchmark.json"
    csv_path = directory / "benchmark.csv"
    markdown_path = directory / "benchmark.md"
    json_path.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    fieldnames = list(rows[0]) if rows else list(_row_placeholder())
    with csv_path.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    lines = [
        "# Evaluator v1 Benchmark",
        "",
        "| Run | System | Fixture | Overall | Coverage | Depth | Citation support |",
        "|---|---|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['run']} | {row['system_version'] or 'Unknown'} | "
            f"{row['fixture'] or 'Unavailable'} | {_fmt(row['overall_score'])} | "
            f"{_fmt(row['coverage'])} | {_fmt(row['depth'])} | "
            f"{_fmt(row['citation_support'])} |"
        )
    markdown_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return json_path, csv_path, markdown_path


def _row_placeholder() -> dict[str, object]:
    return {
        key: None
        for key in (
            "run",
            "system_version",
            "fixture",
            "overall_score",
            "coverage",
            "depth",
            "comprehensiveness",
            "citation_validity",
            "citation_support",
            "citation_completeness",
            "citation_quality",
            "deterministic_integrity",
            "evaluation_completeness",
        )
    }


def _fmt(value: object) -> str:
    return "—" if value is None else f"{float(value):.2f}"


def load_latest_evaluation(run_or_evaluation: Path) -> tuple[Path, EvaluationResult]:
    if run_or_evaluation.is_file():
        candidates = [run_or_evaluation]
    else:
        candidates = list(
            (run_or_evaluation / "evaluations" / "evaluator-v1").glob("*/evaluation.json")
        )
    if not candidates:
        raise ValueError(f"No evaluator-v1 result found beneath: {run_or_evaluation}")
    selected = max(candidates, key=lambda path: path.stat().st_mtime)
    return selected, EvaluationResult.model_validate_json(selected.read_text(encoding="utf-8"))


def save_comparison(
    baseline_path: Path, candidate_path: Path, root: Path
) -> tuple[Path, Path]:
    baseline_file, baseline = load_latest_evaluation(baseline_path)
    candidate_file, candidate = load_latest_evaluation(candidate_path)
    if baseline.metadata.fixture_id != candidate.metadata.fixture_id:
        raise ValueError("Ablation comparison requires evaluations using the same frozen fixture")
    metrics = {
        "coverage": (baseline.comprehensiveness.coverage, candidate.comprehensiveness.coverage),
        "depth": (baseline.comprehensiveness.depth, candidate.comprehensiveness.depth),
        "comprehensiveness": (
            baseline.comprehensiveness.score,
            candidate.comprehensiveness.score,
        ),
        "citation_support": (baseline.citations.support, candidate.citations.support),
        "citation_completeness": (
            baseline.citations.completeness,
            candidate.citations.completeness,
        ),
        "overall": (baseline.overall_score, candidate.overall_score),
    }
    comparison = {
        "fixture_id": baseline.metadata.fixture_id,
        "baseline_evaluation": str(baseline_file),
        "candidate_evaluation": str(candidate_file),
        "metrics": {
            name: {
                "baseline": before,
                "candidate": after,
                "delta": after - before if before is not None and after is not None else None,
            }
            for name, (before, after) in metrics.items()
        },
    }
    directory = _non_overwriting_directory(root / "comparisons", "comparison")
    json_path = directory / "comparison.json"
    markdown_path = directory / "comparison.md"
    json_path.write_text(json.dumps(comparison, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "# Evaluator v1 Ablation Comparison",
        "",
        f"**Fixture:** {baseline.metadata.fixture_id}",
        "",
        "| Metric | Baseline | Candidate | Δ |",
        "|---|---:|---:|---:|",
    ]
    for name, values in comparison["metrics"].items():
        lines.append(
            f"| {name.replace('_', ' ').title()} | {_fmt(values['baseline'])} | "
            f"{_fmt(values['candidate'])} | {_signed(values['delta'])} |"
        )
    markdown_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return json_path, markdown_path


def _signed(value: object) -> str:
    return "—" if value is None else f"{float(value):+.2f}"
