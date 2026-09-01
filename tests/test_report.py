import json
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from research.models import (
    Confidence,
    Conflict,
    EvidenceItem,
    FinalReport,
    Finding,
    IterationAnalysis,
    LedgerFinalReport,
    ResearchIteration,
    ResearchState,
    Source,
)
from research.report import (
    build_incomplete_report,
    build_trace,
    create_output_directory,
    normalize_ledger_final_report,
    render_markdown,
    save_research_outputs,
    validate_source_references,
)


def make_finding(source_id: str) -> Finding:
    return Finding(
        claim="A supported claim.",
        evidence=[
            EvidenceItem(
                summary="The source reports measurements supporting the claim.",
                source_ids=[source_id],
            )
        ],
        confidence=Confidence.HIGH,
        confidence_reason="Direct evidence supports it.",
    )


def make_report(source_id: str = "S1") -> FinalReport:
    return FinalReport(
        question="What happened?",
        summary="A concise summary.",
        findings=[make_finding(source_id)],
        conflicts_and_uncertainties=[],
        remaining_gaps=["Long-term effects remain unknown."],
        conclusion="The evidence supports a bounded conclusion.",
    )


def make_state() -> ResearchState:
    return ResearchState(
        question="What happened?",
        sources=[
            Source(
                id="S1",
                title="A source",
                url="https://example.com/source",
                content="Exact saved content used by the research agent.",
                score=0.9,
            )
        ],
    )


def test_report_source_validation_rejects_unknown_id() -> None:
    with pytest.raises(ValueError, match="S999"):
        validate_source_references(make_report("S999"), make_state())


def test_report_source_validation_rejects_uncited_finding() -> None:
    report = make_report()
    report.findings[0].evidence = []
    with pytest.raises(ValueError, match="no evidence items"):
        validate_source_references(report, make_state())


def test_ledger_report_normalization_omits_uncited_uncertainty() -> None:
    report = LedgerFinalReport(
        question="What happened?",
        summary="Summary.",
        conflicts_and_uncertainties=[
            Conflict(description="Uncited uncertainty.", source_ids=[]),
            Conflict(description="Cited uncertainty.", source_ids=["S1"]),
        ],
        conclusion="Conclusion.",
    )

    normalized = normalize_ledger_final_report(report)

    assert [item.description for item in normalized.conflicts_and_uncertainties] == [
        "Cited uncertainty."
    ]
    assert "1 model-generated conflict or uncertainty item(s) were omitted" in (
        normalized.remaining_gaps[-1]
    )


def test_markdown_rendering_contains_required_sections() -> None:
    markdown = render_markdown(make_report(), make_state().sources)
    assert "**Claim**" in markdown
    assert "**Evidence**" in markdown
    assert "**Confidence:** High" in markdown
    assert "## Sources" in markdown
    assert "[S1]" in markdown


def test_trace_preserves_source_content_for_offline_evaluation() -> None:
    trace_text = json.dumps(build_trace(make_state(), "test-model", 3))
    assert "Exact saved content used by the research agent." in trace_text
    assert "https://example.com/source" in trace_text


def test_saved_outputs_are_complete_and_do_not_overwrite() -> None:
    state = make_state()
    state.stop_reason = "sufficient_evidence"
    with TemporaryDirectory(dir=Path.cwd()) as temporary_directory:
        output_root = Path(temporary_directory)
        first_report, first_trace = save_research_outputs(
            state, make_report(), "test-model", output_root
        )
        second_report, second_trace = save_research_outputs(
            state, make_report(), "test-model", output_root
        )

        assert first_report.exists() and first_trace.exists()
        assert second_report.exists() and second_trace.exists()
        assert first_report.parent != second_report.parent
        trace = json.loads(first_trace.read_text(encoding="utf-8"))
        assert trace["stop_reason"] == "sufficient_evidence"
        assert trace["final_report"]["summary"] == "A concise summary."
        assert trace["sources"][0]["content"] == state.sources[0].content


def test_incomplete_report_preserves_existing_findings_and_gaps() -> None:
    state = make_state()
    state.stop_reason = "max_iterations"
    analysis = IterationAnalysis(
        findings=[make_finding("S1")],
        conflicts=[],
        unresolved_questions=["Independent replication remains missing."],
        needs_more_research=True,
        research_reason="An important evidence gap remains.",
        next_search_query="independent replication study",
    )
    state.iterations.append(
        ResearchIteration(
            iteration_number=1,
            search_query=state.question,
            source_ids=["S1"],
            analysis=analysis,
        )
    )

    report = build_incomplete_report(state, "OpenAI Report Generation")
    markdown = render_markdown(report, state.sources)

    assert "automatically generated incomplete report" in report.summary
    assert report.findings == analysis.findings
    assert "Independent replication remains missing." in report.remaining_gaps
    assert "A supported claim." in markdown
    assert "[S1]" in markdown


def test_incomplete_report_acknowledges_when_no_findings_exist() -> None:
    state = ResearchState(question="Unanswered question")
    report = build_incomplete_report(state, "Tavily Search — Iteration 1")
    assert report.findings == []
    assert "No validated evidence-backed findings" in report.conclusion


def test_output_directory_uses_question_and_numbers_duplicates() -> None:
    with TemporaryDirectory(dir=Path.cwd()) as temporary_directory:
        output_root = Path(temporary_directory)
        first = create_output_directory("What is Solar Energy?", output_root)
        second = create_output_directory("What is Solar Energy?", output_root)
        third = create_output_directory("What is Solar Energy?", output_root)

        assert first.name == "what-is-solar-energy"
        assert second.name == "what-is-solar-energy_2"
        assert third.name == "what-is-solar-energy_3"
