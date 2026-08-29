import json
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from research.models import (
    Confidence,
    EvidenceItem,
    FinalReport,
    Finding,
    ResearchState,
    Source,
)
from research.report import (
    build_trace,
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
                content="Full retrieved content must not enter the trace.",
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


def test_markdown_rendering_contains_required_sections() -> None:
    markdown = render_markdown(make_report(), make_state().sources)
    assert "**Claim**" in markdown
    assert "**Evidence**" in markdown
    assert "**Confidence:** High" in markdown
    assert "## Sources" in markdown
    assert "[S1]" in markdown


def test_trace_excludes_source_content() -> None:
    trace_text = json.dumps(build_trace(make_state(), "test-model", 3))
    assert "Full retrieved content" not in trace_text
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
