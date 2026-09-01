"""Run frozen fixture questions sequentially, then evaluate the saved runs."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Sequence


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from evaluation.v1.adapters import load_evaluation_input
from evaluation.v1.fixtures import discover_fixtures, normalize_question
from evaluation.v1.models import FrozenFixture
from research.versions import SYSTEM_VERSION_BY_MODE


ARCHITECTURE_COMPONENTS = {
    "llm-only": "one structured OpenAI generation (no retrieval or research components)",
    "baseline": "baseline analyzer only (no ledger, decomposer, or verifier)",
    "ledger": "evidence ledger only",
    "decomposed": "evidence ledger + question decomposer",
    "verified": (
        "evidence ledger + question decomposer + independent verifier + "
        "adversarial counter-search"
    ),
}
MAX_RESEARCH_OPENAI_CALLS = {
    "llm-only": 1,
    "baseline": 4,
    "ledger": 6,
    "decomposed": 7,
    "verified": 10,
}
MAX_TAVILY_CALLS = {
    "llm-only": 0,
    "baseline": 3,
    "ledger": 3,
    "decomposed": 3,
    "verified": 3,
}
LABELED_PATH = r"(?m)^{label}:\s*\r?\n(?P<path>[^\r\n]+)$"


@dataclass(frozen=True)
class CommandOutcome:
    returncode: int
    output: str


@dataclass(frozen=True)
class SuiteConfig:
    project_root: Path
    fixtures_root: Path
    outputs_root: Path
    results_root: Path
    python_executable: str
    mode: str = "verified"
    fixture_ids: tuple[str, ...] = ()
    dry_run: bool = False


@dataclass(frozen=True)
class SuiteOutcome:
    returncode: int
    manifest_path: Path | None


CommandRunner = Callable[[Sequence[str], Path], CommandOutcome]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Run frozen research questions sequentially, then evaluate all successful "
            "saved runs with Evaluator v1."
        )
    )
    parser.add_argument(
        "architecture",
        nargs="?",
        choices=tuple(SYSTEM_VERSION_BY_MODE),
        help=(
            "Research architecture: llm-only, baseline, ledger, decomposed, or verified "
            "(default: verified)."
        ),
    )
    parser.add_argument(
        "--mode",
        choices=tuple(SYSTEM_VERSION_BY_MODE),
        default=None,
        help="Backward-compatible alternative to the positional architecture.",
    )
    parser.add_argument(
        "--fixture",
        action="append",
        dest="fixture_ids",
        default=[],
        help=(
            "Run only this fixture ID; repeat to select several. By default all "
            "frozen fixtures are run in stable ID order."
        ),
    )
    parser.add_argument(
        "--fixtures-root",
        type=Path,
        default=PROJECT_ROOT / "evaluation" / "fixtures",
    )
    parser.add_argument(
        "--outputs-root",
        type=Path,
        default=PROJECT_ROOT / "outputs" / "preset-questions",
        help=(
            "Root for fixed-question research runs (default: "
            "outputs/preset-questions)."
        ),
    )
    parser.add_argument(
        "--results-root",
        type=Path,
        default=None,
        help=(
            "Root for aggregate suite artifacts (default: "
            "<outputs-root>/evaluation-results)."
        ),
    )
    parser.add_argument(
        "--python-executable",
        default=sys.executable,
        help="Python executable used for child research and evaluator commands.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate fixtures and print the execution plan without making API calls.",
    )
    return parser


def resolve_architecture(
    architecture: str | None, mode_option: str | None
) -> str:
    if architecture and mode_option and architecture != mode_option:
        raise ValueError(
            "Positional architecture and --mode must match when both are provided"
        )
    return architecture or mode_option or "verified"


def select_fixtures(
    fixtures_root: Path, fixture_ids: Sequence[str] = ()
) -> list[FrozenFixture]:
    fixtures = discover_fixtures(fixtures_root)
    by_id = {fixture.metadata.fixture_id: fixture for fixture in fixtures}
    if len(by_id) != len(fixtures):
        raise ValueError("Frozen fixture IDs must be unique")
    if fixture_ids:
        if len(set(fixture_ids)) != len(fixture_ids):
            raise ValueError("A fixture ID was selected more than once")
        missing = [fixture_id for fixture_id in fixture_ids if fixture_id not in by_id]
        if missing:
            raise ValueError("Unknown frozen fixture ID(s): " + ", ".join(missing))
        return [by_id[fixture_id] for fixture_id in fixture_ids]
    if not fixtures:
        raise ValueError(f"No frozen fixtures found beneath: {fixtures_root}")
    return sorted(fixtures, key=lambda fixture: fixture.metadata.fixture_id)


def research_command(config: SuiteConfig, fixture: FrozenFixture) -> list[str]:
    return [
        config.python_executable,
        str(config.project_root / "main.py"),
        fixture.question,
        "--mode",
        config.mode,
        "--output-root",
        str(config.outputs_root),
    ]


def benchmark_command(
    config: SuiteConfig, run_directories: Sequence[Path], suite_directory: Path
) -> list[str]:
    return [
        config.python_executable,
        str(config.project_root / "main.py"),
        "evaluator",
        "benchmark",
        *(str(path) for path in run_directories),
        "--fixtures-root",
        str(config.fixtures_root),
        "--results-root",
        str(suite_directory),
    ]


def run_streaming_command(command: Sequence[str], cwd: Path) -> CommandOutcome:
    environment = os.environ.copy()
    environment.setdefault("PYTHONUTF8", "1")
    environment.setdefault("PYTHONIOENCODING", "utf-8")
    process = subprocess.Popen(
        list(command),
        cwd=cwd,
        env=environment,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        bufsize=1,
    )
    assert process.stdout is not None
    output: list[str] = []
    for line in process.stdout:
        output.append(line)
        print(line, end="", flush=True)
    return CommandOutcome(process.wait(), "".join(output))


def extract_labeled_path(output: str, label: str, cwd: Path) -> Path:
    pattern = re.compile(LABELED_PATH.format(label=re.escape(label)))
    matches = list(pattern.finditer(output))
    if not matches:
        raise ValueError(f"Command output did not contain a {label!r} path")
    path = Path(matches[-1].group("path").strip())
    return (path if path.is_absolute() else cwd / path).resolve()


def research_run_directory(output: str, cwd: Path) -> Path:
    report_path = extract_labeled_path(output, "Report", cwd)
    if report_path.name != "report.md" or not report_path.is_file():
        raise ValueError(f"Research command reported an invalid report path: {report_path}")
    run_directory = report_path.parent
    if not (run_directory / "trace.json").is_file():
        raise ValueError(f"Research output is missing trace.json: {run_directory}")
    return run_directory


def validate_run_for_fixture(
    run_directory: Path, fixture: FrozenFixture, mode: str
) -> None:
    item = load_evaluation_input(run_directory)
    if normalize_question(item.question) != normalize_question(fixture.question):
        raise ValueError(
            f"Saved run question does not match fixture {fixture.metadata.fixture_id}"
        )
    expected_version = SYSTEM_VERSION_BY_MODE[mode]
    if item.system_version != expected_version:
        raise ValueError(
            f"Saved run system version is {item.system_version!r}; expected "
            f"{expected_version!r}"
        )


def _new_suite_directory(root: Path, mode: str) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    base = root / f"fixture-suite-{timestamp}-{mode}"
    candidate = base
    suffix = 2
    while candidate.exists():
        candidate = root / f"{base.name}_{suffix}"
        suffix += 1
    candidate.mkdir()
    return candidate


def _write_manifest(path: Path, manifest: dict[str, object]) -> None:
    manifest["updated_at"] = datetime.now(timezone.utc).isoformat()
    path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _evaluation_files(run_directory: Path) -> set[Path]:
    root = run_directory / "evaluations" / "evaluator-v1"
    return set(root.glob("*/evaluation.json")) if root.is_dir() else set()


def _print_plan(config: SuiteConfig, fixtures: Sequence[FrozenFixture]) -> None:
    count = len(fixtures)
    print(f"Fixtures: {count}")
    print(f"Mode: {config.mode}")
    print(f"Components: {ARCHITECTURE_COMPONENTS[config.mode]}")
    print(f"Preset-question outputs: {config.outputs_root}")
    print(f"Aggregate evaluation results: {config.results_root}")
    print(
        "Maximum research searches: "
        f"{count * MAX_TAVILY_CALLS[config.mode]} Tavily calls"
    )
    print(
        "Maximum research-model requests: "
        f"{count * MAX_RESEARCH_OPENAI_CALLS[config.mode]} OpenAI calls"
    )
    print(
        "Evaluator-v1 request count depends on the number of final findings; each "
        "structured judging stage may make one repair attempt."
    )
    print("Research phase:")
    for number, fixture in enumerate(fixtures, start=1):
        print(
            f"  {number}. {fixture.metadata.fixture_id}: "
            f"{subprocess.list2cmdline(research_command(config, fixture))}"
        )
    print("Evaluation phase: one evaluator benchmark command over all successful new runs.")


def execute_suite(
    config: SuiteConfig,
    command_runner: CommandRunner = run_streaming_command,
) -> SuiteOutcome:
    fixtures = select_fixtures(config.fixtures_root, config.fixture_ids)
    _print_plan(config, fixtures)
    if config.dry_run:
        print("Dry run complete; no research or evaluation commands were executed.")
        return SuiteOutcome(0, None)

    suite_directory = _new_suite_directory(config.results_root, config.mode)
    manifest_path = suite_directory / "manifest.json"
    entries = [
        {
            "fixture_id": fixture.metadata.fixture_id,
            "question": fixture.question,
            "research_status": "pending",
            "research_exit_code": None,
            "run_directory": None,
            "evaluation_status": "pending",
            "evaluation_directory": None,
            "error": None,
        }
        for fixture in fixtures
    ]
    manifest: dict[str, object] = {
        "suite_version": "1.0",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "updated_at": None,
        "status": "running_research",
        "mode": config.mode,
        "system_version": SYSTEM_VERSION_BY_MODE[config.mode],
        "fixtures_root": str(config.fixtures_root.resolve()),
        "suite_directory": str(suite_directory.resolve()),
        "benchmark_exit_code": None,
        "benchmark_json": None,
        "benchmark_csv": None,
        "benchmark_markdown": None,
        "entries": entries,
    }
    _write_manifest(manifest_path, manifest)

    successful: list[tuple[FrozenFixture, dict[str, object], Path]] = []
    for number, (fixture, entry) in enumerate(zip(fixtures, entries), start=1):
        print(
            f"\n=== Research {number}/{len(fixtures)}: "
            f"{fixture.metadata.fixture_id} ===",
            flush=True,
        )
        entry["research_status"] = "running"
        _write_manifest(manifest_path, manifest)
        try:
            outcome = command_runner(
                research_command(config, fixture), config.project_root
            )
            entry["research_exit_code"] = outcome.returncode
            if outcome.returncode != 0:
                raise RuntimeError(
                    f"Research command exited with code {outcome.returncode}"
                )
            run_directory = research_run_directory(
                outcome.output, config.project_root
            )
            validate_run_for_fixture(run_directory, fixture, config.mode)
            entry["research_status"] = "completed"
            entry["run_directory"] = str(run_directory)
            successful.append((fixture, entry, run_directory))
        except Exception as error:
            entry["research_status"] = "failed"
            entry["evaluation_status"] = "skipped"
            entry["error"] = f"{type(error).__name__}: {error}"
            print(f"Research failed for {fixture.metadata.fixture_id}: {error}")
        _write_manifest(manifest_path, manifest)

    manifest["status"] = "running_evaluation"
    _write_manifest(manifest_path, manifest)
    benchmark_exit_code = 1
    if successful:
        print(
            f"\n=== Evaluating {len(successful)} successful saved run(s) ===",
            flush=True,
        )
        before = {
            fixture.metadata.fixture_id: _evaluation_files(run_directory)
            for fixture, _, run_directory in successful
        }
        benchmark = benchmark_command(
            config,
            [run_directory for _, _, run_directory in successful],
            suite_directory,
        )
        try:
            evaluation_outcome = command_runner(benchmark, config.project_root)
            benchmark_exit_code = evaluation_outcome.returncode
            manifest["benchmark_exit_code"] = benchmark_exit_code
            for label, key in (
                ("Benchmark JSON", "benchmark_json"),
                ("Benchmark CSV", "benchmark_csv"),
                ("Benchmark Markdown", "benchmark_markdown"),
            ):
                try:
                    manifest[key] = str(
                        extract_labeled_path(
                            evaluation_outcome.output, label, config.project_root
                        )
                    )
                except ValueError:
                    manifest[key] = None
        except Exception as error:
            manifest["benchmark_exit_code"] = 1
            manifest["evaluation_error"] = f"{type(error).__name__}: {error}"
            print(f"Evaluator benchmark failed: {error}")

        for fixture, entry, run_directory in successful:
            created = sorted(
                _evaluation_files(run_directory)
                - before[fixture.metadata.fixture_id],
                key=lambda path: path.stat().st_mtime,
            )
            if created:
                entry["evaluation_status"] = "completed"
                entry["evaluation_directory"] = str(created[-1].parent.resolve())
            else:
                entry["evaluation_status"] = "failed"
                if entry["error"] is None:
                    entry["error"] = "No new Evaluator-v1 result was saved"
    else:
        manifest["benchmark_exit_code"] = None
        manifest["evaluation_error"] = "No research run completed successfully"

    complete = bool(entries) and all(
        entry["research_status"] == "completed"
        and entry["evaluation_status"] == "completed"
        for entry in entries
    )
    manifest["status"] = "completed" if complete else "completed_with_failures"
    _write_manifest(manifest_path, manifest)
    print(f"\nSuite manifest:\n{manifest_path.resolve()}")
    return SuiteOutcome(0 if complete and benchmark_exit_code == 0 else 1, manifest_path)


def _resolve_from_project(path: Path) -> Path:
    return (path if path.is_absolute() else PROJECT_ROOT / path).resolve()


def _configure_utf8_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8", errors="replace")


def main(arguments: Sequence[str] | None = None) -> int:
    _configure_utf8_stdio()
    parser = build_parser()
    args = parser.parse_args(arguments)
    try:
        mode = resolve_architecture(args.architecture, args.mode)
    except ValueError as error:
        parser.error(str(error))
    outputs_root = _resolve_from_project(args.outputs_root)
    results_root = (
        _resolve_from_project(args.results_root)
        if args.results_root is not None
        else outputs_root / "evaluation-results"
    )
    config = SuiteConfig(
        project_root=PROJECT_ROOT,
        fixtures_root=_resolve_from_project(args.fixtures_root),
        outputs_root=outputs_root,
        results_root=results_root,
        python_executable=args.python_executable,
        mode=mode,
        fixture_ids=tuple(args.fixture_ids),
        dry_run=args.dry_run,
    )
    try:
        return execute_suite(config).returncode
    except KeyboardInterrupt:
        print("Fixture suite interrupted.", file=sys.stderr)
        return 130
    except Exception as error:
        print(f"Fixture suite failed: {type(error).__name__}: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
