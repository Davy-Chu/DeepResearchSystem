from pathlib import Path
from tempfile import TemporaryDirectory

from research.models import (
    Confidence,
    EvidenceItem,
    FinalReport,
    Finding,
    IterationAnalysis,
    ResearchState,
    Source,
)
from research.research_logger import ResearchLogger
from research.report import save_research_outputs


RAW_CONTENT = "RAW PAGE CONTENT MUST NOT APPEAR"


def make_source() -> Source:
    return Source(
        id="S1",
        title="Synthetic Data Study",
        url="https://example.com/study",
        content=RAW_CONTENT,
        score=0.9,
    )


def make_analysis(
    more: bool = False,
    gaps: list[str] | None = None,
) -> IterationAnalysis:
    return IterationAnalysis(
        findings=[
            Finding(
                claim="Synthetic data can increase training-data coverage.",
                evidence=[
                    EvidenceItem(
                        summary="The study measured broader task coverage.",
                        source_ids=["S1"],
                    )
                ],
                confidence=Confidence.MEDIUM,
                confidence_reason="The evidence is direct but comes from one study.",
            )
        ],
        conflicts=[],
        unresolved_questions=gaps or [],
        needs_more_research=more,
        research_reason=(
            "Bias evidence remains incomplete."
            if more
            else "The important parts of the question are supported."
        ),
        next_search_query="synthetic data bias empirical study" if more else None,
    )


def make_report() -> FinalReport:
    return FinalReport(
        question="What are the benefits and risks?",
        summary="The evidence supports a qualified answer.",
        findings=make_analysis().findings,
        conflicts_and_uncertainties=[],
        remaining_gaps=[],
        conclusion="Benefits depend on data quality and evaluation.",
    )


def make_completed_logger() -> ResearchLogger:
    source = make_source()
    analysis = make_analysis()
    logger = ResearchLogger(
        question="What are the benefits and risks?",
        model="test-model",
        max_iterations=3,
    )
    logger.start_run()
    logger.record_search(
        iteration_number=1,
        search_query="What are the benefits and risks?",
        query_reason="This is the user's original research question.",
        results_returned=1,
        new_sources=[source],
        duration=0.82,
    )
    logger.record_analysis(1, analysis, duration=3.04)
    logger.record_decision(
        1,
        continue_research=False,
        reason=analysis.research_reason,
        stop_reason="sufficient_evidence",
    )
    state = ResearchState(
        question="What are the benefits and risks?",
        sources=[source],
        stop_reason="sufficient_evidence",
    )
    logger.finish_run(state, make_report(), report_duration=2.1, total_runtime=10.4)
    return logger


def test_successful_log_generation_and_readable_rendering() -> None:
    logger = make_completed_logger()
    with TemporaryDirectory(dir=Path.cwd()) as temporary_directory:
        path = logger.save(Path(temporary_directory))
        markdown = path.read_text(encoding="utf-8")

    assert path.name == "research_log.md"
    for heading in (
        "# Research Run Log",
        "## Run Summary",
        "# Iteration 1",
        "## 1. Search",
        "## 2. Evidence Analysis",
        "## 3. Research Decision",
        "# Final Research Decision",
    ):
        assert heading in markdown
    assert "Synthetic data can increase training-data coverage." in markdown
    assert "**Confidence:** Medium" in markdown
    assert "The evidence is direct but comes from one study." in markdown
    assert "The study measured broader task coverage. [S1]" in markdown
    assert "S1 — Synthetic Data Study" in markdown
    assert "https://example.com/study" in markdown
    assert RAW_CONTENT not in markdown


def test_empty_conflicts_and_gaps_are_human_readable() -> None:
    markdown = make_completed_logger().render_markdown()
    assert "No meaningful conflicts were identified in this iteration." in markdown
    assert "No major unanswered gaps were identified." in markdown
    assert "[]" not in markdown


def test_continue_decision_and_next_query_render() -> None:
    analysis = make_analysis(more=True, gaps=["Bias evidence remains incomplete."])
    logger = ResearchLogger("Question", "test-model", 3)
    logger.start_run()
    logger.record_search(1, "Question", "Original question.", 1, [make_source()], 0.5)
    logger.record_analysis(1, analysis, 1.25)
    logger.record_decision(
        1,
        continue_research=True,
        reason=analysis.research_reason,
        next_search_query=analysis.next_search_query,
    )
    markdown = logger.render_markdown()
    assert "**Decision:** Continue researching" in markdown
    assert "**Next Search**" in markdown
    assert "> synthetic data bias empirical study" in markdown


def test_stop_decision_and_fake_timings_render() -> None:
    markdown = make_completed_logger().render_markdown()
    assert "**Decision:** Stop researching" in markdown
    assert "**Stop Reason:** sufficient_evidence" in markdown
    assert "**Search Duration:** 0.82s" in markdown
    assert "**Analysis Duration:** 3.04s" in markdown
    assert "| Report Generation | 1 | 2.10s |" in markdown
    assert "| Total Run | — | 10.40s |" in markdown


def test_failed_run_renders_partial_log_and_redacts_key_like_values() -> None:
    logger = ResearchLogger("Question", "test-model", 3)
    logger.start_run()
    logger.record_search(1, "Question", "Original question.", 1, [make_source()], 0.4)
    logger.record_failure(
        "OpenAI Evidence Analysis — Iteration 1",
        RuntimeError("request failed with api_key=secret-value"),
        total_runtime=1.2,
    )
    markdown = logger.render_markdown()
    assert "**Status:** Failed" in markdown
    assert "**Failure Stage:** OpenAI Evidence Analysis — Iteration 1" in markdown
    assert "request failed with api_key=[REDACTED]" in markdown
    assert "secret-value" not in markdown
    assert "Analysis did not complete for this iteration." in markdown
    assert RAW_CONTENT not in markdown


def test_all_three_artifacts_share_the_run_directory() -> None:
    source = make_source()
    state = ResearchState(
        question="What are the benefits and risks?",
        sources=[source],
        stop_reason="sufficient_evidence",
    )
    report = make_report()
    logger = make_completed_logger()

    with TemporaryDirectory(dir=Path.cwd()) as temporary_directory:
        output_dir = Path(temporary_directory) / "run"
        report_path, trace_path = save_research_outputs(
            state,
            report,
            "test-model",
            output_dir=output_dir,
        )
        log_path = logger.save(output_dir)

        assert {path.name for path in (report_path, log_path, trace_path)} == {
            "report.md",
            "research_log.md",
            "trace.json",
        }
        assert {path.parent for path in (report_path, log_path, trace_path)} == {
            output_dir
        }
