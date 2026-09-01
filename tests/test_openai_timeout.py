from __future__ import annotations

from typing import Any

import pytest

import evaluation.citations as citations_module
import evaluation.coverage as coverage_module
import evaluation.v1.citations as v1_citations_module
import evaluation.v1.comprehensiveness as comprehensiveness_module
import evaluation.v1.fixture_builder as fixture_builder_module
import research.analyzer as analyzer_module
import research.decision as decision_module
import research.decomposer as decomposer_module
import research.evidence_processor as processor_module
import research.llm_only_runner as llm_only_module
import research.report as report_module
import research.subquestion_decision as subquestion_decision_module
import research.verifier as verifier_module
from research.config import (
    DEFAULT_OPENAI_MAX_RETRIES,
    DEFAULT_OPENAI_TIMEOUT_SECONDS,
    load_openai_max_retries,
    load_llm_only_settings,
    load_settings,
    load_openai_timeout_seconds,
)


@pytest.mark.parametrize(
    ("module", "factory"),
    [
        (
            llm_only_module,
            lambda: llm_only_module.LLMOnlyResearchRunner("test-key", "test-model"),
        ),
        (
            analyzer_module,
            lambda: analyzer_module.ResearchAnalyzer("test-key", "test-model"),
        ),
        (
            report_module,
            lambda: report_module.FinalReportGenerator("test-key", "test-model"),
        ),
        (
            coverage_module,
            lambda: coverage_module.CoverageEvaluator("test-key", "test-model"),
        ),
        (
            citations_module,
            lambda: citations_module.CitationEvaluator("test-key", "test-model"),
        ),
        (
            processor_module,
            lambda: processor_module.EvidenceProcessor("test-key", "test-model"),
        ),
        (
            decision_module,
            lambda: decision_module.ResearchDecisionMaker("test-key", "test-model"),
        ),
        (
            decomposer_module,
            lambda: decomposer_module.QuestionDecomposer("test-key", "test-model"),
        ),
        (
            subquestion_decision_module,
            lambda: subquestion_decision_module.SubquestionResearchDecisionMaker(
                "test-key", "test-model"
            ),
        ),
        (
            verifier_module,
            lambda: verifier_module.IndependentClaimVerifier(
                "test-key", "test-model"
            ),
        ),
        (
            comprehensiveness_module,
            lambda: comprehensiveness_module.ComprehensivenessEvaluator(
                "test-key", "test-model"
            ),
        ),
        (
            v1_citations_module,
            lambda: v1_citations_module.CitationEvaluator("test-key", "test-model"),
        ),
        (
            fixture_builder_module,
            lambda: fixture_builder_module.FixtureBuilder("test-key", "test-model"),
        ),
    ],
)
def test_every_openai_client_receives_default_timeout(
    monkeypatch: pytest.MonkeyPatch,
    module: Any,
    factory: Any,
) -> None:
    captured: list[dict[str, object]] = []

    class FakeOpenAI:
        def __init__(self, **kwargs: object) -> None:
            captured.append(kwargs)

    monkeypatch.setattr(module, "OpenAI", FakeOpenAI)
    factory()

    assert captured == [
        {
            "api_key": "test-key",
            "timeout": DEFAULT_OPENAI_TIMEOUT_SECONDS,
            "max_retries": DEFAULT_OPENAI_MAX_RETRIES,
        }
    ]


def test_timeout_can_be_configured_from_environment(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("OPENAI_TIMEOUT_SECONDS", "45.5")
    assert load_openai_timeout_seconds() == 45.5


@pytest.mark.parametrize("value", ["0", "-1", "not-a-number"])
def test_timeout_must_be_positive(
    monkeypatch: pytest.MonkeyPatch,
    value: str,
) -> None:
    monkeypatch.setenv("OPENAI_TIMEOUT_SECONDS", value)
    with pytest.raises(ValueError, match="positive number"):
        load_openai_timeout_seconds()


def test_max_retries_can_be_configured_from_environment(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("OPENAI_MAX_RETRIES", "0")
    assert load_openai_max_retries() == 0


@pytest.mark.parametrize("value", ["-1", "1.5", "not-a-number"])
def test_max_retries_must_be_a_non_negative_integer(
    monkeypatch: pytest.MonkeyPatch,
    value: str,
) -> None:
    monkeypatch.setenv("OPENAI_MAX_RETRIES", value)
    with pytest.raises(ValueError, match="non-negative integer"):
        load_openai_max_retries()


def test_verifier_model_falls_back_to_researcher_model(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "test-openai-key")
    monkeypatch.setenv("TAVILY_API_KEY", "test-tavily-key")
    monkeypatch.setenv("OPENAI_MODEL", "researcher-model")
    monkeypatch.setenv("RESEARCH_MODEL", "split-research-model")
    monkeypatch.setenv("VERIFIER_MODEL", "")

    settings = load_settings()
    assert settings.research_model == "split-research-model"
    assert settings.openai_model == "split-research-model"
    assert settings.verifier_model == "split-research-model"

    monkeypatch.setenv("VERIFIER_MODEL", "independent-verifier-model")
    assert load_settings().verifier_model == "independent-verifier-model"


def test_llm_only_model_falls_back_without_requiring_tavily(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "test-openai-key")
    monkeypatch.delenv("TAVILY_API_KEY", raising=False)
    monkeypatch.setenv("OPENAI_MODEL", "researcher-model")
    monkeypatch.setenv("RESEARCH_MODEL", "split-research-model")
    monkeypatch.delenv("LLM_ONLY_MODEL", raising=False)

    assert load_llm_only_settings().model == "split-research-model"

    monkeypatch.setenv("LLM_ONLY_MODEL", "llm-only-model")
    assert load_llm_only_settings().model == "llm-only-model"
