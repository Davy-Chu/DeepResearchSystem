from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import pytest

import main as main_module
import research.llm_only_runner as llm_only_module
from evaluation.v1.adapters import load_evaluation_input
from evaluation.v1.deterministic import DeterministicEvaluator
from evaluation.v1.models import CheckStatus
from research.config import LLMOnlySettings
from research.llm_only_runner import (
    LLMOnlyResearchRunner,
    PROMPT_PREFIX,
    STOP_REASON,
    save_llm_only_artifacts,
)
from research.models import Confidence, EvidenceItem, FinalReport, Finding
from research.versions import LLM_ONLY_SYSTEM_VERSION


STRUCTURED_REPORT = FinalReport(
    question="What is X?",
    summary="A concise summary.",
    findings=[
        Finding(
            claim="X has a documented property.",
            evidence=[EvidenceItem(summary="The property is described.")],
            confidence=Confidence.MEDIUM,
            confidence_reason="The model has no retrieved evidence.",
        )
    ],
    conflicts_and_uncertainties=[],
    remaining_gaps=["No external sources were retrieved."],
    conclusion="The answer remains unverified.",
)


class FakeResponses:
    def __init__(self, output_parsed: FinalReport | None = STRUCTURED_REPORT) -> None:
        self.output_parsed = output_parsed
        self.calls: list[dict[str, object]] = []

    def parse(self, **kwargs: object):
        self.calls.append(kwargs)
        return SimpleNamespace(
            output_parsed=(
                self.output_parsed.model_copy(deep=True)
                if self.output_parsed is not None
                else None
            ),
            usage=SimpleNamespace(input_tokens=17, output_tokens=29),
        )


def test_one_call_uses_exact_minimal_prompt_and_no_tools() -> None:
    responses = FakeResponses()
    runner = LLMOnlyResearchRunner(
        "unused",
        "research-model",
        client=SimpleNamespace(responses=responses),
    )

    result = runner.run("What is X?")

    assert len(responses.calls) == 1
    assert responses.calls[0] == {
        "model": "research-model",
        "reasoning": {"effort": "low"},
        "input": [
            {
                "role": "user",
                "content": (
                    "Do deep research and create a report on the following question:\n\n"
                    "What is X?"
                ),
            }
        ],
        "text_format": FinalReport,
    }
    assert "tools" not in responses.calls[0]
    assert "instructions" not in responses.calls[0]
    assert result.openai_calls == 1
    assert result.tavily_calls == 0
    assert result.report == STRUCTURED_REPORT


def test_four_o_mini_is_used_without_unsupported_reasoning_parameter() -> None:
    responses = FakeResponses()
    runner = LLMOnlyResearchRunner(
        "unused",
        "gpt-4o-mini",
        client=SimpleNamespace(responses=responses),
    )

    runner.run("What is X?")

    assert responses.calls[0]["model"] == "gpt-4o-mini"
    assert "reasoning" not in responses.calls[0]


def test_empty_question_is_rejected_before_model_call() -> None:
    responses = FakeResponses()
    runner = LLMOnlyResearchRunner(
        "unused", "research-model", client=SimpleNamespace(responses=responses)
    )

    with pytest.raises(ValueError, match="must not be empty"):
        runner.run("   ")

    assert responses.calls == []


def test_missing_parsed_response_fails_without_semantic_retry() -> None:
    responses = FakeResponses(None)
    runner = LLMOnlyResearchRunner(
        "unused", "research-model", client=SimpleNamespace(responses=responses)
    )

    with pytest.raises(ValueError, match="no parsed LLM-only FinalReport"):
        runner.run("What is X?")

    assert len(responses.calls) == 1


def test_canonical_report_and_minimal_trace_are_preserved_without_fake_provenance(
    tmp_path: Path,
) -> None:
    model_report = STRUCTURED_REPORT.model_copy(deep=True)
    model_report.findings[0].evidence[0].source_ids = ["S99"]
    responses = FakeResponses(model_report)
    result = LLMOnlyResearchRunner(
        "unused",
        "research-model",
        client=SimpleNamespace(responses=responses),
    ).run("What is X?")

    report_path, trace_path, log_path = save_llm_only_artifacts(result, tmp_path)

    report_markdown = report_path.read_text(encoding="utf-8")
    assert report_markdown.startswith("# Research Report\n")
    assert "## Research Question" in report_markdown
    assert "## Summary" in report_markdown
    assert "## Findings" in report_markdown
    assert "## Sources" in report_markdown
    assert "S99" not in report_markdown
    trace = json.loads(trace_path.read_text(encoding="utf-8"))
    assert trace["system_version"] == LLM_ONLY_SYSTEM_VERSION
    assert trace["openai_calls"] == 1
    assert trace["tavily_calls"] == 0
    assert trace["sources"] == []
    assert trace["iterations"] == []
    assert trace["research_plan"] is None
    assert trace["evidence_ledger"] is None
    assert trace["claim_verifications"] == []
    assert trace["stop_reason"] == STOP_REASON
    assert trace["final_report"]["findings"][0]["evidence"][0]["source_ids"] == []
    assert "No Tavily calls occurred" in log_path.read_text(encoding="utf-8")

    evaluation_input = load_evaluation_input(tmp_path)
    assert evaluation_input.report == result.report
    assert evaluation_input.sources == []
    assert evaluation_input.report_markdown == report_markdown


def test_deterministic_research_checks_are_not_applicable(tmp_path: Path) -> None:
    result = LLMOnlyResearchRunner(
        "unused",
        "research-model",
        client=SimpleNamespace(responses=FakeResponses()),
    ).run("What is X?")
    save_llm_only_artifacts(result, tmp_path)

    integrity = DeterministicEvaluator().evaluate(load_evaluation_input(tmp_path))

    assert integrity.score == 1.0
    assert integrity.passed_count == 2
    assert integrity.failed_count == 0
    assert all(
        check.status == CheckStatus.NOT_APPLICABLE
        for check in integrity.checks
        if check.check_name not in {"run_metadata_loads", "report_exists"}
    )


def test_cli_llm_only_does_not_construct_other_research_components(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    responses = FakeResponses()

    class FakeOpenAI:
        def __init__(self, **kwargs: object) -> None:
            self.responses = responses

    def forbidden(*args: object, **kwargs: object) -> None:
        raise AssertionError("A non-LLM-only research component was constructed")

    monkeypatch.setattr(llm_only_module, "OpenAI", FakeOpenAI)
    monkeypatch.setattr(
        main_module,
        "load_llm_only_settings",
        lambda: LLMOnlySettings("test-key", "research-model", 10.0, 0),
    )
    for name in (
        "TavilySearchClient",
        "ResearchAnalyzer",
        "EvidenceProcessor",
        "ResearchDecisionMaker",
        "SubquestionResearchDecisionMaker",
        "QuestionDecomposer",
        "IndependentClaimVerifier",
        "FinalReportGenerator",
        "ResearchRunner",
        "LedgerResearchRunner",
    ):
        monkeypatch.setattr(main_module, name, forbidden)

    exit_code = main_module.main(
        ["What is X?", "--mode", "llm-only", "--output-root", str(tmp_path)]
    )

    assert exit_code == 0
    assert len(responses.calls) == 1
    run_directories = [path for path in tmp_path.iterdir() if path.is_dir()]
    assert len(run_directories) == 1
    report_text = (run_directories[0] / "report.md").read_text(encoding="utf-8")
    assert report_text.startswith("# Research Report\n")
    assert "## Findings" in report_text
