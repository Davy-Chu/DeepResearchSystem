from __future__ import annotations

from typing import Any

import pytest

import evaluation.citations as citations_module
import evaluation.coverage as coverage_module
import research.analyzer as analyzer_module
import research.report as report_module
from research.config import (
    DEFAULT_OPENAI_MAX_RETRIES,
    DEFAULT_OPENAI_TIMEOUT_SECONDS,
    load_openai_max_retries,
    load_openai_timeout_seconds,
)


@pytest.mark.parametrize(
    ("module", "factory"),
    [
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
