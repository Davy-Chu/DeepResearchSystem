from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace

from main import _handle_incomplete_run
from research.models import (
    Confidence,
    EvidenceItem,
    Finding,
    IterationAnalysis,
    ResearchIteration,
    ResearchState,
    Source,
)
from research.research_logger import ResearchLogger


def test_failed_final_synthesis_saves_all_incomplete_artifacts() -> None:
    source = Source(
        id="S1",
        title="Existing Evidence",
        url="https://example.com/evidence",
        content="Raw content is preserved only in the machine trace.",
        score=0.8,
    )
    finding = Finding(
        claim="An evidence-backed finding survived the incomplete run.",
        evidence=[
            EvidenceItem(
                summary="The source directly supports the retained finding.",
                source_ids=["S1"],
            )
        ],
        confidence=Confidence.MEDIUM,
        confidence_reason="The evidence is direct but limited to one source.",
    )
    analysis = IterationAnalysis(
        findings=[finding],
        conflicts=[],
        unresolved_questions=["More evidence is still needed."],
        needs_more_research=True,
        research_reason="The evidence remains incomplete.",
        next_search_query="more evidence query",
    )
    state = ResearchState(
        question="A difficult question",
        sources=[source],
        iterations=[
            ResearchIteration(
                iteration_number=1,
                search_query="A difficult question",
                source_ids=["S1"],
                analysis=analysis,
            )
        ],
        stop_reason="max_iterations",
    )
    logger = ResearchLogger(state.question, "test-model", 1)
    logger.start_run()
    logger.record_search(
        1,
        state.question,
        "This is the user's original research question.",
        1,
        [source],
        0.2,
    )
    logger.record_analysis(1, analysis, 0.4)
    logger.record_decision(
        1,
        continue_research=False,
        reason=analysis.research_reason,
        stop_reason="max_iterations",
    )
    failure = RuntimeError("final synthesis failed")
    logger.record_failure("OpenAI Report Generation", failure, 0.8)
    runner = SimpleNamespace(last_state=state)

    with TemporaryDirectory(dir=Path.cwd()) as temporary_directory:
        output_dir = Path(temporary_directory) / "run"
        exit_code = _handle_incomplete_run(
            failure,
            "Research Execution",
            logger,
            output_dir,
            runner,  # type: ignore[arg-type]
            None,
        )

        assert exit_code == 1
        report_text = (output_dir / "report.md").read_text(encoding="utf-8")
        log_text = (output_dir / "research_log.md").read_text(encoding="utf-8")
        trace_text = (output_dir / "trace.json").read_text(encoding="utf-8")

    assert "automatically generated incomplete report" in report_text
    assert "An evidence-backed finding survived" in report_text
    assert "**Status:** Failed" in log_text
    assert "More evidence is still needed." in log_text
    assert '"stop_reason": "max_iterations"' in trace_text
    assert "Raw content is preserved only in the machine trace." not in report_text + log_text
    assert "Raw content is preserved only in the machine trace." in trace_text
