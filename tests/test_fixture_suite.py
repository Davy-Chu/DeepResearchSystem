from __future__ import annotations

import json
from pathlib import Path
from typing import Sequence

from evaluation.v1.fixtures import normalize_question
from scripts.run_fixture_suite import (
    ARCHITECTURE_COMPONENTS,
    CommandOutcome,
    SuiteConfig,
    build_parser,
    execute_suite,
    extract_labeled_path,
    resolve_architecture,
    select_fixtures,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
FIXTURES_ROOT = PROJECT_ROOT / "evaluation" / "fixtures"


def config(
    tmp_path: Path,
    fixture_ids: tuple[str, ...],
    *,
    dry_run: bool = False,
) -> SuiteConfig:
    return SuiteConfig(
        project_root=tmp_path,
        fixtures_root=FIXTURES_ROOT,
        outputs_root=tmp_path / "outputs" / "preset-questions",
        results_root=tmp_path / "outputs" / "preset-questions" / "evaluation-results",
        python_executable="test-python",
        mode="verified",
        fixture_ids=fixture_ids,
        dry_run=dry_run,
    )


def write_research_output(
    tmp_path: Path, fixture_id: str, question: str
) -> CommandOutcome:
    run_directory = tmp_path / "outputs" / fixture_id
    run_directory.mkdir(parents=True)
    report_path = run_directory / "report.md"
    report_path.write_text("# Test report\n", encoding="utf-8")
    (run_directory / "trace.json").write_text(
        json.dumps(
            {
                "question": question,
                "system_version": "evidence-ledger-decomposer-verifier-v1",
                "sources": [],
            }
        ),
        encoding="utf-8",
    )
    return CommandOutcome(
        0,
        f"Research complete.\nReport:\n{report_path}\nStop reason: max_iterations\n",
    )


def write_benchmark_outputs(command: Sequence[str]) -> CommandOutcome:
    fixture_flag = command.index("--fixtures-root")
    result_flag = command.index("--results-root")
    run_directories = [Path(value) for value in command[4:fixture_flag]]
    for run_directory in run_directories:
        trace = json.loads((run_directory / "trace.json").read_text(encoding="utf-8"))
        fixture = next(
            item
            for item in select_fixtures(FIXTURES_ROOT)
            if normalize_question(item.question)
            == normalize_question(trace["question"])
        )
        evaluation_directory = (
            run_directory
            / "evaluations"
            / "evaluator-v1"
            / fixture.metadata.fixture_id
        )
        evaluation_directory.mkdir(parents=True)
        (evaluation_directory / "evaluation.json").write_text(
            "{}\n", encoding="utf-8"
        )
    benchmark_directory = Path(command[result_flag + 1]) / "benchmark"
    benchmark_directory.mkdir(parents=True)
    for filename in ("benchmark.json", "benchmark.csv", "benchmark.md"):
        (benchmark_directory / filename).write_text("test\n", encoding="utf-8")
    return CommandOutcome(
        0,
        "\n".join(
            [
                "Benchmark JSON:",
                str(benchmark_directory / "benchmark.json"),
                "Benchmark CSV:",
                str(benchmark_directory / "benchmark.csv"),
                "Benchmark Markdown:",
                str(benchmark_directory / "benchmark.md"),
                "",
            ]
        ),
    )


def test_repository_contains_nine_frozen_fixtures() -> None:
    assert len(select_fixtures(FIXTURES_ROOT)) == 9


def test_positional_architectures_and_legacy_mode_are_supported() -> None:
    for architecture in ("baseline", "ledger", "decomposed", "verified"):
        args = build_parser().parse_args([architecture, "--dry-run"])
        assert resolve_architecture(args.architecture, args.mode) == architecture
        assert ARCHITECTURE_COMPONENTS[architecture]

    legacy = build_parser().parse_args(["--mode", "ledger", "--dry-run"])
    assert resolve_architecture(legacy.architecture, legacy.mode) == "ledger"
    assert resolve_architecture(None, None) == "verified"


def test_conflicting_architecture_arguments_are_rejected() -> None:
    try:
        resolve_architecture("ledger", "verified")
    except ValueError as error:
        assert "must match" in str(error)
    else:
        raise AssertionError("Conflicting architecture arguments should fail")


def test_extract_labeled_path_resolves_relative_output(tmp_path: Path) -> None:
    path = extract_labeled_path(
        "Report:\noutputs/example/report.md\n", "Report", tmp_path
    )
    assert path == (tmp_path / "outputs" / "example" / "report.md").resolve()


def test_dry_run_makes_no_commands_or_result_directory(
    tmp_path: Path, capsys
) -> None:
    def forbidden_runner(command: Sequence[str], cwd: Path) -> CommandOutcome:
        raise AssertionError("dry-run must not execute child commands")

    outcome = execute_suite(
        config(
            tmp_path,
            ("chain-of-thought-effectiveness", "remote-work-productivity"),
            dry_run=True,
        ),
        forbidden_runner,
    )

    assert outcome.returncode == 0
    assert outcome.manifest_path is None
    assert not (tmp_path / "outputs" / "preset-questions").exists()
    output = capsys.readouterr().out
    assert "Fixtures: 2" in output
    assert "Dry run complete" in output


def test_suite_runs_all_research_before_one_benchmark(tmp_path: Path) -> None:
    fixture_ids = (
        "chain-of-thought-effectiveness",
        "remote-work-productivity",
    )
    fixtures = select_fixtures(FIXTURES_ROOT, fixture_ids)
    by_question = {normalize_question(item.question): item for item in fixtures}
    commands: list[list[str]] = []

    def fake_runner(command: Sequence[str], cwd: Path) -> CommandOutcome:
        command = list(command)
        commands.append(command)
        if "--mode" in command:
            fixture = by_question[normalize_question(command[2])]
            return write_research_output(tmp_path, fixture.metadata.fixture_id, fixture.question)
        return write_benchmark_outputs(command)

    outcome = execute_suite(config(tmp_path, fixture_ids), fake_runner)

    assert outcome.returncode == 0
    assert outcome.manifest_path is not None
    assert ["--mode" in command for command in commands] == [True, True, False]
    for command in commands[:2]:
        output_flag = command.index("--output-root")
        assert Path(command[output_flag + 1]) == config(tmp_path, fixture_ids).outputs_root
    assert commands[-1][2:4] == ["evaluator", "benchmark"]
    manifest = json.loads(outcome.manifest_path.read_text(encoding="utf-8"))
    assert manifest["status"] == "completed"
    assert manifest["benchmark_exit_code"] == 0
    assert all(
        entry["research_status"] == "completed"
        and entry["evaluation_status"] == "completed"
        for entry in manifest["entries"]
    )


def test_failed_research_is_skipped_but_successes_are_evaluated(
    tmp_path: Path,
) -> None:
    fixture_ids = (
        "chain-of-thought-effectiveness",
        "remote-work-productivity",
    )
    fixtures = select_fixtures(FIXTURES_ROOT, fixture_ids)
    calls = 0
    benchmark_command: list[str] | None = None

    def fake_runner(command: Sequence[str], cwd: Path) -> CommandOutcome:
        nonlocal calls, benchmark_command
        command = list(command)
        if "--mode" in command:
            calls += 1
            if calls == 1:
                return CommandOutcome(1, "Research failed.\n")
            fixture = fixtures[1]
            return write_research_output(tmp_path, fixture.metadata.fixture_id, fixture.question)
        benchmark_command = command
        return write_benchmark_outputs(command)

    outcome = execute_suite(config(tmp_path, fixture_ids), fake_runner)

    assert outcome.returncode == 1
    assert outcome.manifest_path is not None
    assert benchmark_command is not None
    fixture_flag = benchmark_command.index("--fixtures-root")
    assert len(benchmark_command[4:fixture_flag]) == 1
    manifest = json.loads(outcome.manifest_path.read_text(encoding="utf-8"))
    assert manifest["status"] == "completed_with_failures"
    assert manifest["entries"][0]["research_status"] == "failed"
    assert manifest["entries"][0]["evaluation_status"] == "skipped"
    assert manifest["entries"][1]["evaluation_status"] == "completed"
