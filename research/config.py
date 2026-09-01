"""Small, explicit configuration surface for baseline zero."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

MAX_RESEARCH_ITERATIONS = 10
TAVILY_MAX_RESULTS = 5
MAX_SOURCE_CHARS = 8000
DEFAULT_OPENAI_MODEL = "gpt-5.6-terra"
DEFAULT_OPENAI_TIMEOUT_SECONDS = 120.0
DEFAULT_OPENAI_MAX_RETRIES = 1


@dataclass(frozen=True)
class Settings:
    openai_api_key: str
    tavily_api_key: str
    research_model: str = DEFAULT_OPENAI_MODEL
    openai_timeout_seconds: float = DEFAULT_OPENAI_TIMEOUT_SECONDS
    openai_max_retries: int = DEFAULT_OPENAI_MAX_RETRIES
    verifier_model: str = DEFAULT_OPENAI_MODEL

    @property
    def openai_model(self) -> str:
        """Legacy alias retained for callers that have not migrated yet."""

        return self.research_model


@dataclass(frozen=True)
class LLMOnlySettings:
    openai_api_key: str
    model: str = DEFAULT_OPENAI_MODEL
    openai_timeout_seconds: float = DEFAULT_OPENAI_TIMEOUT_SECONDS
    openai_max_retries: int = DEFAULT_OPENAI_MAX_RETRIES


def load_openai_timeout_seconds() -> float:
    raw_value = os.getenv("OPENAI_TIMEOUT_SECONDS", "").strip()
    if not raw_value:
        return DEFAULT_OPENAI_TIMEOUT_SECONDS
    try:
        timeout = float(raw_value)
    except ValueError as error:
        raise ValueError("OPENAI_TIMEOUT_SECONDS must be a positive number") from error
    if timeout <= 0:
        raise ValueError("OPENAI_TIMEOUT_SECONDS must be a positive number")
    return timeout


def load_openai_max_retries() -> int:
    raw_value = os.getenv("OPENAI_MAX_RETRIES", "").strip()
    if not raw_value:
        return DEFAULT_OPENAI_MAX_RETRIES
    try:
        max_retries = int(raw_value)
    except ValueError as error:
        raise ValueError("OPENAI_MAX_RETRIES must be a non-negative integer") from error
    if max_retries < 0:
        raise ValueError("OPENAI_MAX_RETRIES must be a non-negative integer")
    return max_retries


def load_research_model() -> str:
    """Resolve the shared model for all research-architecture calls."""

    legacy_model = os.getenv("OPENAI_MODEL", "").strip() or DEFAULT_OPENAI_MODEL
    return os.getenv("RESEARCH_MODEL", "").strip() or legacy_model


def load_settings() -> Settings:
    """Load .env and return validated runtime settings."""
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY", "").strip()
    tavily_api_key = os.getenv("TAVILY_API_KEY", "").strip()

    missing = [
        name
        for name, value in (
            ("OPENAI_API_KEY", openai_api_key),
            ("TAVILY_API_KEY", tavily_api_key),
        )
        if not value
    ]
    if missing:
        names = ", ".join(missing)
        raise ValueError(
            f"Missing required environment variable(s): {names}. "
            "Copy .env.example to .env and add your API keys."
        )

    research_model = load_research_model()
    verifier_model = os.getenv("VERIFIER_MODEL", "").strip() or research_model
    return Settings(
        openai_api_key=openai_api_key,
        tavily_api_key=tavily_api_key,
        research_model=research_model,
        verifier_model=verifier_model,
        openai_timeout_seconds=load_openai_timeout_seconds(),
        openai_max_retries=load_openai_max_retries(),
    )


def load_llm_only_settings() -> LLMOnlySettings:
    """Load the one-call baseline without requiring an unused Tavily key."""

    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not openai_api_key:
        raise ValueError("Missing required environment variable: OPENAI_API_KEY")
    research_model = load_research_model()
    model = os.getenv("LLM_ONLY_MODEL", "").strip() or research_model
    return LLMOnlySettings(
        openai_api_key=openai_api_key,
        model=model,
        openai_timeout_seconds=load_openai_timeout_seconds(),
        openai_max_retries=load_openai_max_retries(),
    )
