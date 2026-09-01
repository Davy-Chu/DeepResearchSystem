"""Command-line entry point for selectable research architectures."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path
from typing import Sequence

from research.analyzer import ResearchAnalyzer
from research.config import (
    MAX_RESEARCH_ITERATIONS,
    load_llm_only_settings,
    load_settings,
)
from research.decision import ResearchDecisionMaker
from research.decomposer import QuestionDecomposer
from research.evidence_processor import EvidenceProcessor
from research.ledger_logger import LedgerResearchLogger
from research.ledger_runner import LedgerResearchRunner
from research.llm_only_runner import (
    STOP_REASON as LLM_ONLY_STOP_REASON,
    LLMOnlyResearchRunner,
    save_llm_only_artifacts,
)
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
from research.verifier import IndependentClaimVerifier
from research.versions import (
    DECOMPOSED_SYSTEM_VERSION,
    LEDGER_SYSTEM_VERSION,
    SYSTEM_VERSION_BY_MODE,
    VERIFIED_SYSTEM_VERSION,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run iterative evidence-backed web research.")
    parser.add_argument("question", help="The research question to investigate")
    parser.add_argument(
        "--mode",
        choices=tuple(SYSTEM_VERSION_BY_MODE),
        default="baseline",
        help=(
            "Research architecture: llm-only is one raw OpenAI generation with no "
            "retrieval or research infrastructure; baseline-zero remains the default; "
            "ledger, decomposed, and verified add the later research components."
        ),
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path("outputs"),
        help="Directory beneath which the question-specific run directory is created.",
    )
    return parser


def _run_llm_only(question: str, output_root: Path) -> int:
    question = question.strip()
    if not question:
        logging.error("Research question must not be empty")
        return 1
    try:
        settings = load_llm_only_settings()
        logging.info("Research model: %s", settings.model)
        logging.info("Architecture: %s", SYSTEM_VERSION_BY_MODE["llm-only"])
        result = LLMOnlyResearchRunner(
            settings.openai_api_key,
            settings.model,
            timeout_seconds=settings.openai_timeout_seconds,
            max_retries=settings.openai_max_retries,
        ).run(question)
        output_dir = create_output_directory(question, output_root)
        report_path, trace_path, research_log_path = save_llm_only_artifacts(
            result, output_dir
        )
    except KeyboardInterrupt:
        logging.error("LLM-only research interrupted.")
        return 130
    except Exception as error:
        logging.error("LLM-only research failed: %s", error)
        return 1

    logging.info("Research complete.")
    logging.info("Report:\n%s", report_path)
    logging.info("Human-readable research log:\n%s", research_log_path)
    logging.info("Machine trace:\n%s", trace_path)
    logging.info("Stop reason: %s", LLM_ONLY_STOP_REASON)
    return 0


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
                verifier_model=getattr(research_logger, "verifier_model", None),
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


def main(arguments: Sequence[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    effective_arguments = list(sys.argv[1:] if arguments is None else arguments)
    if effective_arguments and effective_arguments[0] == "evaluator":
        from evaluation.v1.cli import main as evaluator_v1_main

        return evaluator_v1_main(effective_arguments[1:])
    if effective_arguments and effective_arguments[0] == "evaluate":
        from evaluation.evaluator import evaluation_main

        return evaluation_main(effective_arguments[1:])
    args = build_parser().parse_args(effective_arguments)
    if args.mode == "llm-only":
        return _run_llm_only(args.question, args.output_root)
    research_logger: ResearchLogger | LedgerResearchLogger | None = None
    output_dir: Path | None = None
    runner: ResearchRunner | LedgerResearchRunner | None = None
    final_report: FinalReport | None = None
    failure_stage = "Initialization"

    try:
        settings = load_settings()
        logging.info("Research model: %s", settings.research_model)
        logging.info("Architecture: %s", SYSTEM_VERSION_BY_MODE[args.mode])
        output_dir = create_output_directory(args.question, args.output_root)
        if args.mode in {"ledger", "decomposed", "verified"}:
            research_logger = LedgerResearchLogger(
                question=args.question.strip(),
                model=settings.research_model,
                max_iterations=MAX_RESEARCH_ITERATIONS,
                system_version=(
                    VERIFIED_SYSTEM_VERSION
                    if args.mode == "verified"
                    else (
                        DECOMPOSED_SYSTEM_VERSION
                        if args.mode == "decomposed"
                        else LEDGER_SYSTEM_VERSION
                    )
                ),
                verifier_model=(
                    settings.verifier_model if args.mode == "verified" else None
                ),
            )
        else:
            research_logger = ResearchLogger(
                question=args.question.strip(),
                model=settings.research_model,
                max_iterations=MAX_RESEARCH_ITERATIONS,
            )
        search_client = TavilySearchClient(settings.tavily_api_key)
        report_generator = FinalReportGenerator(
            settings.openai_api_key,
            settings.research_model,
            timeout_seconds=settings.openai_timeout_seconds,
            max_retries=settings.openai_max_retries,
        )
        failure_stage = "Research Execution"
        if args.mode in {"ledger", "decomposed", "verified"}:
            assert isinstance(research_logger, LedgerResearchLogger)
            evidence_processor = EvidenceProcessor(
                settings.openai_api_key,
                settings.research_model,
                timeout_seconds=settings.openai_timeout_seconds,
                max_retries=settings.openai_max_retries,
            )
            if args.mode in {"decomposed", "verified"}:
                decision_maker = SubquestionResearchDecisionMaker(
                    settings.openai_api_key,
                    settings.research_model,
                    timeout_seconds=settings.openai_timeout_seconds,
                    max_retries=settings.openai_max_retries,
                )
                question_decomposer = QuestionDecomposer(
                    settings.openai_api_key,
                    settings.research_model,
                    timeout_seconds=settings.openai_timeout_seconds,
                    max_retries=settings.openai_max_retries,
                )
                claim_verifier = (
                    IndependentClaimVerifier(
                        settings.openai_api_key,
                        settings.verifier_model,
                        timeout_seconds=settings.openai_timeout_seconds,
                        max_retries=settings.openai_max_retries,
                    )
                    if args.mode == "verified"
                    else None
                )
            else:
                decision_maker = ResearchDecisionMaker(
                    settings.openai_api_key,
                    settings.research_model,
                    timeout_seconds=settings.openai_timeout_seconds,
                    max_retries=settings.openai_max_retries,
                )
                question_decomposer = None
                claim_verifier = None
            runner = LedgerResearchRunner(
                search_client,
                evidence_processor,
                decision_maker,
                report_generator,
                research_logger=research_logger,
                question_decomposer=question_decomposer,
                system_version=research_logger.system_version,
                claim_verifier=claim_verifier,
            )
        else:
            assert isinstance(research_logger, ResearchLogger)
            analyzer = ResearchAnalyzer(
                settings.openai_api_key,
                settings.research_model,
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
            settings.research_model,
            output_dir=output_dir,
            verifier_model=(settings.verifier_model if args.mode == "verified" else None),
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
