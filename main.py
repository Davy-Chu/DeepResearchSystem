"""Command-line entry point for baseline-zero deep research."""

from __future__ import annotations

import argparse
import logging

from research.analyzer import ResearchAnalyzer
from research.config import load_settings
from research.report import FinalReportGenerator, save_research_outputs
from research.runner import ResearchRunner
from research.search import TavilySearchClient


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run iterative evidence-backed web research.")
    parser.add_argument("question", help="The research question to investigate")
    return parser


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    args = build_parser().parse_args()

    try:
        settings = load_settings()
        search_client = TavilySearchClient(settings.tavily_api_key)
        analyzer = ResearchAnalyzer(settings.openai_api_key, settings.openai_model)
        report_generator = FinalReportGenerator(settings.openai_api_key, settings.openai_model)
        result = ResearchRunner(search_client, analyzer, report_generator).run(args.question)
        report_path, trace_path = save_research_outputs(
            result.state, result.report, settings.openai_model
        )
    except Exception as exc:
        logging.error("Research failed: %s", exc)
        return 1

    logging.info("Report:\n%s", report_path)
    logging.info("Trace:\n%s", trace_path)
    logging.info("Stop reason: %s", result.state.stop_reason)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
