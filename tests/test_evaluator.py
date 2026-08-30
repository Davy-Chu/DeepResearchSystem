from __future__ import annotations

import json
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from evaluation.evaluator import EvaluatorRunner, load_evaluation_input
from evaluation.models import (
    AspectImportance,
    AspectJudgment,
    CitationResult,
    CoverageResult,
    CoverageStatus,
    EvaluationAspect,
    FindingCitationResult,
    StageStatus,
    SupportLabel,
)
from evaluation.renderer import save_evaluation_result
from research.models import Confidence, EvidenceItem, FinalReport, Finding, ResearchState, Source
from research.report import save_research_outputs


class FixedStage:
    def __init__(self, result: object) -> None:
        self.result = result

    def evaluate(self, evaluation_input) -> object:
        return self.result


def synthetic_saved_run(root: Path) -> Path:
    sources = [
        Source(
            id=f"S{number}",
            title=f"Source {number}",
            url=f"https://example.com/{number}",
            content=f"Exact evidence text {number} used during research.",
        )
        for number in range(1, 5)
    ]
    findings = [
        Finding(
            claim=f"Finding {number}",
            evidence=[EvidenceItem(summary=f"Evidence {number}", source_ids=[f"S{number}"])],
            confidence=Confidence.MEDIUM,
            confidence_reason="Synthetic test evidence.",
        )
        for number in range(1, 5)
    ]
    report = FinalReport(
        question="What are the benefits, risks, and implementation limits?",
        summary="A synthetic report.",
        findings=findings,
        conflicts_and_uncertainties=[],
        remaining_gaps=["One question aspect is only partial."],
        conclusion="A bounded synthetic conclusion.",
    )
    state = ResearchState(question=report.question, sources=sources, stop_reason="sufficient_evidence")
    report_path, _ = save_research_outputs(state, report, "research-model", root)
    return report_path.parent


def test_entire_evaluator_loads_and_saves_all_sections_without_overwrite() -> None:
    aspects = [
        EvaluationAspect(id="A1", description="Benefits", importance=AspectImportance.CORE),
        EvaluationAspect(id="A2", description="Limits", importance=AspectImportance.CORE),
    ]
    coverage = CoverageResult(
        status=StageStatus.COMPLETED,
        aspects=aspects,
        judgments=[
            AspectJudgment(
                aspect_id="A1",
                status=CoverageStatus.COVERED,
                reason="Covered.",
                report_evidence="Finding 1.",
            ),
            AspectJudgment(
                aspect_id="A2",
                status=CoverageStatus.PARTIALLY_COVERED,
                reason="Partial.",
                report_evidence="Remaining gaps.",
            ),
        ],
        core_coverage_rate=0.75,
        overall_coverage_rate=0.75,
    )
    citation_findings = [
        FindingCitationResult(
            finding_id=f"F{number}",
            claim=f"Finding {number}",
            cited_source_ids=[f"S{number}"],
            source_judgments=[],
            combined_support=(
                SupportLabel.UNSUPPORTED if number == 4 else SupportLabel.FULLY_SUPPORTED
            ),
            reason="Synthetic evaluator judgment.",
        )
        for number in range(1, 5)
    ]
    citations = CitationResult(
        status=StageStatus.COMPLETED,
        findings=citation_findings,
        evaluated_findings=4,
        findings_with_evidence=4,
        findings_without_evidence=0,
        citation_completeness_rate=1.0,
        citation_support_rate=0.75,
        fully_supported_count=3,
        unsupported_count=1,
    )

    with TemporaryDirectory(dir=Path.cwd()) as temporary_directory:
        run_directory = synthetic_saved_run(Path(temporary_directory))
        evaluation_input = load_evaluation_input(run_directory)
        runner = EvaluatorRunner(
            "evaluator-model",
            FixedStage(coverage),
            FixedStage(citations),
        )
        result = runner.evaluate(evaluation_input)
        first_json, first_markdown = save_evaluation_result(run_directory, result)
        second_json, _ = save_evaluation_result(run_directory, result)

        saved = json.loads(first_json.read_text(encoding="utf-8"))
        markdown = first_markdown.read_text(encoding="utf-8")
        assert first_json.parent.name == "evaluator-v0"
        assert second_json.parent.name == "evaluator-v0_2"
        assert saved["coverage"]["overall_coverage_rate"] == pytest.approx(0.75)
        assert saved["citations"]["citation_support_rate"] == pytest.approx(0.75)
        assert saved["deterministic"]["all_passed"] is True
        assert "## Coverage" in markdown
        assert "## Citation Support" in markdown
        assert "## Deterministic Failures" in markdown


def test_loader_rejects_legacy_trace_without_saved_content() -> None:
    with TemporaryDirectory(dir=Path.cwd()) as temporary_directory:
        run_directory = Path(temporary_directory)
        (run_directory / "report.md").write_text("# Old report", encoding="utf-8")
        (run_directory / "trace.json").write_text(
            json.dumps({"question": "Old question", "sources": []}),
            encoding="utf-8",
        )
        with pytest.raises(ValueError, match="predates evaluator-v0"):
            load_evaluation_input(run_directory)


def test_runner_preserves_other_stages_when_one_llm_stage_fails(evaluation_input) -> None:
    class FailedStage:
        def evaluate(self, evaluation_input) -> object:
            raise RuntimeError("stage failed")

    citations = CitationResult(status=StageStatus.COMPLETED)
    result = EvaluatorRunner(
        "test-model",
        FailedStage(),
        FixedStage(citations),
    ).evaluate(evaluation_input)
    assert result.coverage.status == StageStatus.FAILED
    assert "stage failed" in (result.coverage.error or "")
    assert result.citations.status == StageStatus.COMPLETED
    assert result.deterministic.all_passed
