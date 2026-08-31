"""Command-line entry point for selectable research architectures."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from research.analyzer import ResearchAnalyzer
from research.config import MAX_RESEARCH_ITERATIONS, load_settings
from research.decision import ResearchDecisionMaker
from research.decomposer import QuestionDecomposer
from research.evidence_processor import EvidenceProcessor
from research.ledger_logger import LedgerResearchLogger
from research.ledger_runner import LedgerResearchRunner
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
from research.subquestion_decision import SubquestionResearchDecisionMaker


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run iterative evidence-backed web research.")
    parser.add_argument("question", help="The research question to investigate")
    parser.add_argument(
        "--mode",
        choices=("baseline", "ledger", "decomposed"),
        default="baseline",
        help=(
            "Research architecture: baseline-zero (default), evidence-ledger-v1, "
            "or evidence-ledger-decomposer-v1"
        ),
    )
    return parser


def _handle_incomplete_run(
    error: BaseException,
    failure_stage: str,
    research_logger: ResearchLogger | LedgerResearchLogger | None,
    output_dir: Path | None,
    runner: ResearchRunner | LedgerResearchRunner | None,
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
    if len(sys.argv) > 1 and sys.argv[1] == "evaluator":
        from evaluation.v1.cli import main as evaluator_v1_main

        return evaluator_v1_main(sys.argv[2:])
    if len(sys.argv) > 1 and sys.argv[1] == "evaluate":
        from evaluation.evaluator import evaluation_main

        return evaluation_main(sys.argv[2:])
    args = build_parser().parse_args()
    research_logger: ResearchLogger | LedgerResearchLogger | None = None
    output_dir: Path | None = None
    runner: ResearchRunner | LedgerResearchRunner | None = None
    final_report: FinalReport | None = None
    failure_stage = "Initialization"

    try:
        settings = load_settings()
        output_dir = create_output_directory(args.question)
        if args.mode in {"ledger", "decomposed"}:
            research_logger = LedgerResearchLogger(
                question=args.question.strip(),
                model=settings.openai_model,
                max_iterations=MAX_RESEARCH_ITERATIONS,
                system_version=(
                    "evidence-ledger-decomposer-v1"
                    if args.mode == "decomposed"
                    else "evidence-ledger-v1"
                ),
            )
        else:
            research_logger = ResearchLogger(
                question=args.question.strip(),
                model=settings.openai_model,
                max_iterations=MAX_RESEARCH_ITERATIONS,
            )
        search_client = TavilySearchClient(settings.tavily_api_key)
        report_generator = FinalReportGenerator(
            settings.openai_api_key,
            settings.openai_model,
            timeout_seconds=settings.openai_timeout_seconds,
            max_retries=settings.openai_max_retries,
        )
        failure_stage = "Research Execution"
        if args.mode in {"ledger", "decomposed"}:
            assert isinstance(research_logger, LedgerResearchLogger)
            evidence_processor = EvidenceProcessor(
                settings.openai_api_key,
                settings.openai_model,
                timeout_seconds=settings.openai_timeout_seconds,
                max_retries=settings.openai_max_retries,
            )
            if args.mode == "decomposed":
                decision_maker = SubquestionResearchDecisionMaker(
                    settings.openai_api_key,
                    settings.openai_model,
                    timeout_seconds=settings.openai_timeout_seconds,
                    max_retries=settings.openai_max_retries,
                )
                question_decomposer = QuestionDecomposer(
                    settings.openai_api_key,
                    settings.openai_model,
                    timeout_seconds=settings.openai_timeout_seconds,
                    max_retries=settings.openai_max_retries,
                )
            else:
                decision_maker = ResearchDecisionMaker(
                    settings.openai_api_key,
                    settings.openai_model,
                    timeout_seconds=settings.openai_timeout_seconds,
                    max_retries=settings.openai_max_retries,
                )
                question_decomposer = None
            runner = LedgerResearchRunner(
                search_client,
                evidence_processor,
                decision_maker,
                report_generator,
                research_logger=research_logger,
                question_decomposer=question_decomposer,
                system_version=research_logger.system_version,
            )
        else:
            assert isinstance(research_logger, ResearchLogger)
            analyzer = ResearchAnalyzer(
                settings.openai_api_key,
                settings.openai_model,
                timeout_seconds=settings.openai_timeout_seconds,
                max_retries=settings.openai_max_retries,
            )
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
