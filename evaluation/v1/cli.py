"""CLI commands for fixture authoring, evaluation, benchmarking, and comparison."""

from __future__ import annotations

import argparse
import logging
import os
import re
from pathlib import Path

from dotenv import load_dotenv

from evaluation.v1.adapters import load_evaluation_input
from evaluation.v1.benchmark import BenchmarkEntry, save_benchmark, save_comparison
from evaluation.v1.citations import CitationEvaluator
from evaluation.v1.comprehensiveness import ComprehensivenessEvaluator
from evaluation.v1.config import load_evaluator_model
from evaluation.v1.fixture_builder import FixtureBuilder
from evaluation.v1.fixtures import (
    discover_fixtures,
    match_fixture,
    normalize_question,
    resolve_fixture,
)
from evaluation.v1.openai_utils import UsageTracker
from evaluation.v1.renderer import save_evaluation
from evaluation.v1.runner import EvaluatorRunner
from research.config import load_openai_max_retries, load_openai_timeout_seconds


DEFAULT_FIXTURES_ROOT = Path("evaluation/fixtures")
DEFAULT_RESULTS_ROOT = Path("evaluation/results")


def _safe_error(error: Exception) -> str:
    message = re.sub(r"(?:sk|tvly)-[A-Za-z0-9_-]+", "[REDACTED]", str(error))
    return f"{type(error).__name__}: {message}"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Frozen reference evaluator-v1")
    commands = parser.add_subparsers(dest="command", required=True)

    build = commands.add_parser("build-fixture", help="Generate, critique, and freeze one rubric")
    build.add_argument("fixture_directory", type=Path)

    evaluate = commands.add_parser("evaluate", help="Evaluate one saved run")
    evaluate.add_argument("run_directory", type=Path)
    evaluate.add_argument("--fixture", help="Fixture ID or fixture directory")
    evaluate.add_argument("--fixtures-root", type=Path, default=DEFAULT_FIXTURES_ROOT)

    benchmark = commands.add_parser("benchmark", help="Evaluate compatible saved benchmark runs")
    benchmark.add_argument("run_directories", nargs="*", type=Path)
    benchmark.add_argument("--outputs-root", type=Path, default=Path("outputs"))
    benchmark.add_argument("--fixtures-root", type=Path, default=DEFAULT_FIXTURES_ROOT)
    benchmark.add_argument("--results-root", type=Path, default=DEFAULT_RESULTS_ROOT)

    compare = commands.add_parser("compare", help="Compare two existing evaluator-v1 results")
    compare.add_argument("baseline", type=Path)
    compare.add_argument("candidate", type=Path)
    compare.add_argument("--results-root", type=Path, default=DEFAULT_RESULTS_ROOT)
    return parser


def _runtime() -> tuple[str, str, float, int]:
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise ValueError("Missing required environment variable: OPENAI_API_KEY")
    return (
        api_key,
        load_evaluator_model(),
        load_openai_timeout_seconds(),
        load_openai_max_retries(),
    )


def _runner(api_key: str, model: str, timeout: float, retries: int) -> EvaluatorRunner:
    usage = UsageTracker()
    comprehensive = ComprehensivenessEvaluator(
        api_key,
        model,
        timeout_seconds=timeout,
        max_retries=retries,
        usage=usage,
    )
    citations = CitationEvaluator(
        api_key,
        model,
        timeout_seconds=timeout,
        max_retries=retries,
        usage=usage,
    )
    return EvaluatorRunner(model, comprehensive, citations, usage=usage)


def _evaluate_one(run_directory: Path, fixture, runner: EvaluatorRunner):
    item = load_evaluation_input(run_directory)
    if fixture is not None and normalize_question(item.question) != normalize_question(
        fixture.question
    ):
        raise ValueError("Candidate question does not exactly match the selected frozen fixture")
    result = runner.evaluate(item, fixture)
    json_path, markdown_path = save_evaluation(item.run_directory, result)
    logging.info("[RESULT] Overall: %s", "Unavailable" if result.overall_score is None else f"{result.overall_score:.1f}")
    logging.info("Machine evaluation:\n%s", json_path)
    logging.info("Human-readable evaluation:\n%s", markdown_path)
    return item, result


def main(arguments: list[str] | None = None) -> int:
    args = build_parser().parse_args(arguments)
    try:
        if args.command == "compare":
            json_path, markdown_path = save_comparison(
                args.baseline, args.candidate, args.results_root
            )
            logging.info("Comparison JSON:\n%s", json_path)
            logging.info("Comparison Markdown:\n%s", markdown_path)
            return 0

        api_key, model, timeout, retries = _runtime()
        if args.command == "build-fixture":
            builder = FixtureBuilder(
                api_key,
                model,
                timeout_seconds=timeout,
                max_retries=retries,
            )
            metadata = builder.build(args.fixture_directory)
            logging.info("[EVALUATOR] Frozen fixture: %s", metadata.fixture_id)
            logging.info("LLM calls: %d", builder.usage.llm_calls)
            return 0


        fixtures = discover_fixtures(args.fixtures_root)
        if args.command == "evaluate":
            item = load_evaluation_input(args.run_directory)
            fixture = resolve_fixture(args.fixture, args.fixtures_root) if args.fixture else match_fixture(
                item.question, fixtures, item.benchmark_fixture_id
            )
            _evaluate_one(args.run_directory, fixture, _runner(api_key, model, timeout, retries))
            return 0

        run_directories = args.run_directories or sorted(
            path
            for path in args.outputs_root.iterdir()
            if path.is_dir() and (path / "report.md").is_file() and (path / "trace.json").is_file()
        )
        entries: list[BenchmarkEntry] = []
        for run_directory in run_directories:
            item = load_evaluation_input(run_directory)
            fixture = match_fixture(item.question, fixtures, item.benchmark_fixture_id)
            _, result = _evaluate_one(
                run_directory,
                fixture,
                _runner(api_key, model, timeout, retries),
            )
            entries.append(BenchmarkEntry(run=run_directory.name, result=result))
        json_path, csv_path, markdown_path = save_benchmark(entries, args.results_root)
        logging.info("Benchmark JSON:\n%s", json_path)
        logging.info("Benchmark CSV:\n%s", csv_path)
        logging.info("Benchmark Markdown:\n%s", markdown_path)
        return 0
    except Exception as error:
        logging.error("Evaluator v1 failed: %s", _safe_error(error))
        return 1
