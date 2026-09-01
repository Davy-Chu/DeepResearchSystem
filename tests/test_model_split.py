from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

import pytest

import main as main_module
from evaluation.v1.cli import _runner as build_evaluator_runner
from evaluation.v1.config import load_evaluator_model
from research.analyzer import ResearchAnalyzer
from research.config import load_llm_only_settings, load_settings
from research.decomposer import QuestionDecomposer
from research.decision import ResearchDecisionMaker
from research.evidence_processor import EvidenceProcessor
from research.models import (
    ClaimStatus,
    Confidence,
    FinalReport,
    LedgerClaim,
    ResearchPlan,
    ResearchState,
    SubQuestion,
    SubQuestionImportance,
    VerificationPhase,
)
from research.report import FinalReportGenerator, build_trace
from research.subquestion_decision import SubquestionResearchDecisionMaker
from research.verifier import IndependentClaimVerifier


def test_model_resolution_and_fallbacks(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("TAVILY_API_KEY", "test-tavily")
    monkeypatch.setenv("OPENAI_MODEL", "legacy-model")
    monkeypatch.setenv("RESEARCH_MODEL", "gpt-4o-mini")
    monkeypatch.setenv("LLM_ONLY_MODEL", "")
    monkeypatch.setenv("VERIFIER_MODEL", "")
    monkeypatch.setenv("EVALUATOR_MODEL", "fallback-judge")
    monkeypatch.setenv("OPENAI_EVALUATOR_MODEL", "gpt-5.6-luna")

    settings = load_settings()
    assert settings.research_model == "gpt-4o-mini"
    assert settings.openai_model == "gpt-4o-mini"
    assert settings.verifier_model == "gpt-4o-mini"
    assert load_llm_only_settings().model == "gpt-4o-mini"
    assert load_evaluator_model() == "gpt-5.6-luna"

    monkeypatch.setenv("RESEARCH_MODEL", "")
    monkeypatch.setenv("OPENAI_EVALUATOR_MODEL", "")
    assert load_settings().research_model == "legacy-model"
    assert load_llm_only_settings().model == "legacy-model"
    assert load_evaluator_model() == "fallback-judge"


def test_v0_through_v3_route_every_component_to_research_model(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    research_model = "gpt-4o-mini"
    evaluator_model = "gpt-5.6-luna"
    observed: dict[str, list[str]] = {}

    def component(name: str):
        class RecordedComponent:
            def __init__(self, api_key: str, model: str, **kwargs) -> None:
                observed.setdefault(name, []).append(model)
                self.model = model

        return RecordedComponent

    class FakeSearch:
        def __init__(self, api_key: str) -> None:
            pass

    class FakeRunner:
        def __init__(self, *args, **kwargs) -> None:
            self.last_state = None

        def run(self, question: str):
            state = ResearchState(question=question, stop_reason="test_complete")
            self.last_state = state
            return SimpleNamespace(
                state=state,
                report=FinalReport(
                    question=question,
                    summary="Test summary.",
                    conclusion="Test conclusion.",
                ),
            )

    settings = SimpleNamespace(
        openai_api_key="test-key",
        tavily_api_key="test-tavily",
        research_model=research_model,
        verifier_model=research_model,
        openai_timeout_seconds=10.0,
        openai_max_retries=0,
    )
    monkeypatch.setattr(main_module, "load_settings", lambda: settings)
    monkeypatch.setattr(main_module, "TavilySearchClient", FakeSearch)
    monkeypatch.setattr(main_module, "ResearchAnalyzer", component("analyzer"))
    monkeypatch.setattr(main_module, "EvidenceProcessor", component("processor"))
    monkeypatch.setattr(main_module, "ResearchDecisionMaker", component("decision"))
    monkeypatch.setattr(
        main_module, "SubquestionResearchDecisionMaker", component("subquestion_decision")
    )
    monkeypatch.setattr(main_module, "QuestionDecomposer", component("decomposer"))
    monkeypatch.setattr(main_module, "IndependentClaimVerifier", component("verifier"))
    monkeypatch.setattr(main_module, "FinalReportGenerator", component("report"))
    monkeypatch.setattr(main_module, "ResearchRunner", FakeRunner)
    monkeypatch.setattr(main_module, "LedgerResearchRunner", FakeRunner)
    monkeypatch.setattr(
        main_module,
        "create_output_directory",
        lambda question, root: tmp_path / question.replace(" ", "-"),
    )
    monkeypatch.setattr(
        main_module,
        "save_research_outputs",
        lambda *args, **kwargs: (tmp_path / "report.md", tmp_path / "trace.json"),
    )
    monkeypatch.setattr(
        main_module.ResearchLogger,
        "save",
        lambda self, output_dir: tmp_path / "research_log.md",
    )
    monkeypatch.setattr(
        main_module.LedgerResearchLogger,
        "save",
        lambda self, output_dir: tmp_path / "research_log.md",
    )

    for mode in ("baseline", "ledger", "decomposed", "verified"):
        assert main_module.main([f"Question {mode}", "--mode", mode]) == 0

    assert observed
    assert all(
        model == research_model
        for models in observed.values()
        for model in models
    )
    assert observed["verifier"] == [research_model]
    assert evaluator_model not in {
        model for models in observed.values() for model in models
    }


def test_evaluator_components_use_luna_not_research_model() -> None:
    runner = build_evaluator_runner("unused", "gpt-5.6-luna", 10.0, 0)

    assert runner.evaluator_model == "gpt-5.6-luna"
    assert runner.comprehensiveness_evaluator.model == "gpt-5.6-luna"
    assert not hasattr(runner, "citation_evaluator")
    assert runner.evaluator_model != "gpt-4o-mini"


def test_every_research_component_calls_four_o_mini_without_reasoning() -> None:
    class RecordingResponses:
        def __init__(self) -> None:
            self.calls: list[dict[str, object]] = []

        def parse(self, **kwargs):
            self.calls.append(kwargs)
            return SimpleNamespace(output_parsed=None, usage=None)

    state = ResearchState(question="Test question")
    plan = ResearchPlan(
        subquestions=[
            SubQuestion(
                id="SQ1",
                question="First part?",
                importance=SubQuestionImportance.CORE,
                success_criteria="Find direct evidence.",
            ),
            SubQuestion(
                id="SQ2",
                question="Second part?",
                importance=SubQuestionImportance.SECONDARY,
                success_criteria="Find contextual evidence.",
            ),
        ]
    )
    decomposed_state = state.model_copy(update={"research_plan": plan})
    claim = LedgerClaim(
        id="C1",
        claim="Test claim.",
        confidence=Confidence.LOW,
        confidence_reason="No evidence yet.",
        status=ClaimStatus.INSUFFICIENT_EVIDENCE,
        first_seen_iteration=1,
        last_updated_iteration=1,
    )
    invocations = [
        lambda client: ResearchAnalyzer("unused", "gpt-4o-mini", client=client).analyze(state, []),
        lambda client: EvidenceProcessor("unused", "gpt-4o-mini", client=client).process(state, []),
        lambda client: ResearchDecisionMaker("unused", "gpt-4o-mini", client=client).decide(state),
        lambda client: QuestionDecomposer("unused", "gpt-4o-mini", client=client).decompose("Test question"),
        lambda client: SubquestionResearchDecisionMaker(
            "unused", "gpt-4o-mini", client=client
        ).decide(decomposed_state),
        lambda client: IndependentClaimVerifier(
            "unused", "gpt-4o-mini", client=client
        ).verify(state, claim, VerificationPhase.INITIAL, False),
        lambda client: FinalReportGenerator(
            "unused", "gpt-4o-mini", client=client
        ).generate(state),
    ]

    for invoke in invocations:
        responses = RecordingResponses()
        with pytest.raises(ValueError, match="no parsed"):
            invoke(SimpleNamespace(responses=responses))
        assert responses.calls[0]["model"] == "gpt-4o-mini"
        assert "reasoning" not in responses.calls[0]


def test_trace_persists_resolved_research_and_verifier_models() -> None:
    trace = build_trace(
        ResearchState(question="Test question"),
        "gpt-4o-mini",
        10,
        verifier_model="gpt-4o-mini",
    )
    assert trace["research_model"] == "gpt-4o-mini"
    assert trace["verifier_model"] == "gpt-4o-mini"
