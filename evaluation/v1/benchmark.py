"""Benchmark table persistence and offline ablation comparison."""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path

from evaluation.v1.models import EvaluationResult
from research.versions import CANONICAL_SYSTEM_VERSIONS, CANONICAL_VERSION_LABELS


@dataclass(frozen=True)
class BenchmarkEntry:
    run: str
    result: EvaluationResult
    trace_metadata: dict[str, object] | None = None


def _row(entry: BenchmarkEntry) -> dict[str, object]:
    result = entry.result
    trace = entry.trace_metadata or {}
    coverage = trace.get("coverage_diagnostics")
    coverage = coverage if isinstance(coverage, dict) else {}
    return {
        "run": entry.run,
        "system_version": result.system_version,
        "fixture": result.metadata.fixture_id,
        "research_model": result.metadata.research_model or "unknown",
        "evaluator_model": result.metadata.evaluator_model or "unknown",
        "overall_score": result.overall_score,
        "coverage": result.comprehensiveness.coverage,
        "depth": result.comprehensiveness.depth,
        "deterministic_integrity": result.deterministic_integrity.score,
        "evaluation_completeness": result.evaluation_completeness,
        "tavily_calls": trace.get("tavily_calls"),
        "unique_sources": trace.get("unique_sources"),
        "research_openai_calls": trace.get("logical_research_openai_calls"),
        "core_dimensions": coverage.get("core_dimensions"),
        "core_sufficient": coverage.get("core_sufficient"),
        "core_partial": coverage.get("core_partial"),
        "core_unresearched": coverage.get("core_unresearched"),
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
    rank = {
        system_version: index
        for index, system_version in enumerate(CANONICAL_SYSTEM_VERSIONS)
    }
    ordered = sorted(
        entries,
        key=lambda entry: rank.get(
            entry.result.system_version or "", len(CANONICAL_SYSTEM_VERSIONS)
        ),
    )
    rows = [_row(entry) for entry in ordered]
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
        "| Run | System | Fixture | Research Model | Evaluator Model | Overall | Coverage | Depth | Searches | Core sufficient |",
        "|---|---|---|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['run']} | {row['system_version'] or 'Unknown'} | "
            f"{row['fixture'] or 'Unavailable'} | {row['research_model']} | "
            f"{row['evaluator_model']} | {_fmt(row['overall_score'])} | "
            f"{_fmt(row['coverage'])} | {_fmt(row['depth'])} | "
            f"{_fmt(row['tavily_calls'])} | "
            f"{_coverage_fmt(row['core_sufficient'], row['core_dimensions'])} |"
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
            "research_model",
            "evaluator_model",
            "overall_score",
            "coverage",
            "depth",
            "deterministic_integrity",
            "evaluation_completeness",
            "tavily_calls",
            "unique_sources",
            "research_openai_calls",
            "core_dimensions",
            "core_sufficient",
            "core_partial",
            "core_unresearched",
        )
    }


def _fmt(value: object) -> str:
    return "—" if value is None else f"{float(value):.2f}"


def _coverage_fmt(sufficient: object, total: object) -> str:
    if sufficient is None or total is None:
        return "—"
    return f"{int(sufficient)}/{int(total)}"


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


def _load_benchmark_rows(path: Path) -> list[dict[str, object]]:
    path = path.resolve()
    candidates = (
        [path]
        if path.is_file()
        else [path / "benchmark.json", path / "benchmark" / "benchmark.json"]
    )
    selected = next((item for item in candidates if item.is_file()), None)
    if selected is None:
        raise ValueError(f"Benchmark JSON not found at: {path}")
    payload = json.loads(selected.read_text(encoding="utf-8"))
    if not isinstance(payload, list) or not all(isinstance(row, dict) for row in payload):
        raise ValueError(f"Malformed benchmark JSON: {selected}")
    return payload


def _family_summary(paths: list[Path]) -> dict[str, dict[str, object]]:
    rows = [row for path in paths for row in _load_benchmark_rows(path)]
    summary: dict[str, dict[str, object]] = {}
    for system_version in CANONICAL_SYSTEM_VERSIONS:
        matching = [row for row in rows if row.get("system_version") == system_version]
        coverage = [float(row["coverage"]) for row in matching if row.get("coverage") is not None]
        depth = [float(row["depth"]) for row in matching if row.get("depth") is not None]
        if not matching:
            continue
        summary[system_version] = {
            "coverage": sum(coverage) / len(coverage) if coverage else None,
            "depth": sum(depth) / len(depth) if depth else None,
            "evaluated_reports": len(matching),
            "research_models": sorted(
                {str(row.get("research_model") or "unknown") for row in matching}
            ),
            "evaluator_models": sorted(
                {str(row.get("evaluator_model") or "unknown") for row in matching}
            ),
        }
    return summary


def save_model_family_comparison(
    baseline_paths: list[Path],
    candidate_paths: list[Path],
    root: Path,
    *,
    baseline_label: str = "Luna",
    candidate_label: str = "GPT-4o-mini",
) -> tuple[Path, Path]:
    """Compare architecture levels and within-family deltas across model families."""

    if not baseline_paths or not candidate_paths:
        raise ValueError("Model-family comparison requires both benchmark families")
    families = {
        baseline_label: _family_summary(baseline_paths),
        candidate_label: _family_summary(candidate_paths),
    }
    transitions: list[dict[str, object]] = []
    for before, after in zip(CANONICAL_SYSTEM_VERSIONS, CANONICAL_SYSTEM_VERSIONS[1:]):
        entry: dict[str, object] = {
            "from_system": before,
            "to_system": after,
            "families": {},
        }
        for label, summary in families.items():
            before_values = summary.get(before, {})
            after_values = summary.get(after, {})
            family_delta: dict[str, float | None] = {}
            for metric in ("coverage", "depth"):
                first = before_values.get(metric)
                second = after_values.get(metric)
                family_delta[metric] = (
                    float(second) - float(first)
                    if first is not None and second is not None
                    else None
                )
            entry["families"][label] = family_delta
        transitions.append(entry)

    payload = {
        "families": families,
        "architecture_deltas": transitions,
        "primary_metrics": ["coverage", "depth"],
    }
    directory = _non_overwriting_directory(
        root / "comparisons", "model-family-comparison"
    )
    json_path = directory / "comparison.json"
    markdown_path = directory / "comparison.md"
    json_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    lines = [
        "# Cross-Model Architecture Comparison",
        "",
        f"| Architecture | {baseline_label} Coverage | {baseline_label} Depth | "
        f"{candidate_label} Coverage | {candidate_label} Depth |",
        "|---|---:|---:|---:|---:|",
    ]
    for version in CANONICAL_SYSTEM_VERSIONS:
        baseline = families[baseline_label].get(version, {})
        candidate = families[candidate_label].get(version, {})
        lines.append(
            f"| {CANONICAL_VERSION_LABELS[version]} | "
            f"{_fmt(baseline.get('coverage'))} | {_fmt(baseline.get('depth'))} | "
            f"{_fmt(candidate.get('coverage'))} | {_fmt(candidate.get('depth'))} |"
        )
    lines.extend(
        [
            "",
            "## Marginal Architecture Deltas",
            "",
            f"| Transition | Metric | {baseline_label} Delta | {candidate_label} Delta |",
            "|---|---|---:|---:|",
        ]
    )
    for transition in transitions:
        transition_label = (
            f"{CANONICAL_VERSION_LABELS[transition['from_system']]} -> "
            f"{CANONICAL_VERSION_LABELS[transition['to_system']]}"
        )
        family_values = transition["families"]
        for metric in ("coverage", "depth"):
            lines.append(
                f"| {transition_label} | {metric.title()} | "
                f"{_signed(family_values[baseline_label][metric])} | "
                f"{_signed(family_values[candidate_label][metric])} |"
            )
    markdown_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return json_path, markdown_path


def _signed(value: object) -> str:
    return "—" if value is None else f"{float(value):+.2f}"
