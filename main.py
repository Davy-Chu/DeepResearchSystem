"""Command-line entry point for baseline-zero deep research."""

from __future__ import annotations

import argparse
import logging

from research.analyzer import ResearchAnalyzer
from research.config import MAX_RESEARCH_ITERATIONS, load_settings
from research.report import (
    FinalReportGenerator,
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


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    args = build_parser().parse_args()
    research_logger: ResearchLogger | None = None
    output_dir = None
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
        analyzer = ResearchAnalyzer(settings.openai_api_key, settings.openai_model)
        report_generator = FinalReportGenerator(settings.openai_api_key, settings.openai_model)
        failure_stage = "Research Execution"
        result = ResearchRunner(
            search_client,
            analyzer,
            report_generator,
            research_logger=research_logger,
        ).run(args.question)
        failure_stage = "Output Saving"
        report_path, trace_path = save_research_outputs(
            result.state,
            result.report,
            settings.openai_model,
            output_dir=output_dir,
        )
        research_log_path = research_logger.save(output_dir)
    except Exception as exc:
        partial_log_path = None
        if research_logger is not None and output_dir is not None:
            if research_logger.status != "Failed":
                research_logger.record_failure(
                    stage=failure_stage,
                    error=exc,
                    total_runtime=research_logger.total_runtime or 0.0,
                )
            try:
                partial_log_path = research_logger.save(output_dir)
            except Exception as log_exc:
                logging.error("Research failed: %s", exc)
                logging.error(
                    "Additionally, writing research_log.md failed: %s", log_exc
                )
                return 1
        logging.error("Research failed: %s", exc)
        if partial_log_path:
            logging.error("Partial research log:\n%s", partial_log_path)
        return 1

    logging.info("Research complete.")
    logging.info("Report:\n%s", report_path)
    logging.info("Human-readable research log:\n%s", research_log_path)
    logging.info("Machine trace:\n%s", trace_path)
    logging.info("Stop reason: %s", result.state.stop_reason)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
