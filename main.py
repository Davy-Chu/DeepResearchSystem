"""Command-line entry point for baseline-zero deep research."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from research.analyzer import ResearchAnalyzer
from research.config import MAX_RESEARCH_ITERATIONS, load_settings
from research.models import FinalReport
from research.report import (
    FinalReportGenerator,
    build_incomplete_report,
    create_output_directory,
    save_research_outputs,
)
from research.research_logger import ResearchLogger
from research.runner import ResearchRunner
from research.search import TavilySearchClient


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run iterative evidence-backed web research.")
    parser.add_argument("question", help="The research question to investigate")
    return parser


def _handle_incomplete_run(
    error: BaseException,
    failure_stage: str,
    research_logger: ResearchLogger | None,
    output_dir: Path | None,
    runner: ResearchRunner | None,
    final_report: FinalReport | None,
) -> int:
    logging.error("Research did not complete normally: %s", error or type(error).__name__)
    if research_logger is None or output_dir is None:
        return 1

    if research_logger.status != "Failed":
        research_logger.record_failure(stage=failure_stage, error=error)

    report_path = None
    trace_path = None
    try:
        state = runner.last_state if runner is not None else None
        if state is not None:
            recovered_report = final_report or build_incomplete_report(
                state, research_logger.failure_stage or failure_stage
            )
            research_logger.record_recovered_state(state, recovered_report)
            report_path, trace_path = save_research_outputs(
                state,
                recovered_report,
                research_logger.model,
                output_dir=output_dir,
            )
        research_log_path = research_logger.save(output_dir)
    except Exception as artifact_error:
        logging.error(
            "Additionally, writing incomplete research artifacts failed: %s",
            artifact_error,
        )
        return 1

    if report_path and trace_path:
        logging.error("Incomplete report:\n%s", report_path)
        logging.error("Human-readable research log:\n%s", research_log_path)
        logging.error("Machine trace:\n%s", trace_path)
    else:
        logging.error("Partial research log:\n%s", research_log_path)
    return 1


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    if len(sys.argv) > 1 and sys.argv[1] == "evaluate":
        from evaluation.evaluator import evaluation_main

        return evaluation_main(sys.argv[2:])
    args = build_parser().parse_args()
    research_logger: ResearchLogger | None = None
    output_dir: Path | None = None
    runner: ResearchRunner | None = None
    final_report: FinalReport | None = None
    failure_stage = "Initialization"

    try:
        settings = load_settings()
        output_dir = create_output_directory(args.question)
        research_logger = ResearchLogger(
            question=args.question.strip(),
            model=settings.openai_model,
            max_iterations=MAX_RESEARCH_ITERATIONS,
        )
        search_client = TavilySearchClient(settings.tavily_api_key)
        analyzer = ResearchAnalyzer(
            settings.openai_api_key,
            settings.openai_model,
            timeout_seconds=settings.openai_timeout_seconds,
            max_retries=settings.openai_max_retries,
        )
        report_generator = FinalReportGenerator(
            settings.openai_api_key,
            settings.openai_model,
            timeout_seconds=settings.openai_timeout_seconds,
            max_retries=settings.openai_max_retries,
        )
        failure_stage = "Research Execution"
        runner = ResearchRunner(
            search_client,
            analyzer,
            report_generator,
            research_logger=research_logger,
        )
        result = runner.run(args.question)
        final_report = result.report
        failure_stage = "Output Saving"
        report_path, trace_path = save_research_outputs(
            result.state,
            result.report,
            settings.openai_model,
            output_dir=output_dir,
        )
        research_log_path = research_logger.save(output_dir)
    except KeyboardInterrupt as exc:
        return _handle_incomplete_run(
            exc,
            failure_stage,
            research_logger,
            output_dir,
            runner,
            final_report,
        )
    except Exception as exc:
        return _handle_incomplete_run(
            exc,
            failure_stage,
            research_logger,
            output_dir,
            runner,
            final_report,
        )

    logging.info("Research complete.")
    logging.info("Report:\n%s", report_path)
    logging.info("Human-readable research log:\n%s", research_log_path)
    logging.info("Machine trace:\n%s", trace_path)
    logging.info("Stop reason: %s", result.state.stop_reason)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
