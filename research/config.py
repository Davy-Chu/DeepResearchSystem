"""Small, explicit configuration surface for baseline zero."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

MAX_RESEARCH_ITERATIONS = 3
TAVILY_MAX_RESULTS = 5
MAX_SOURCE_CHARS = 8000
DEFAULT_OPENAI_MODEL = "gpt-5.6-terra"


@dataclass(frozen=True)
class Settings:
    openai_api_key: str
    tavily_api_key: str
    openai_model: str = DEFAULT_OPENAI_MODEL


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

    model = os.getenv("OPENAI_MODEL", DEFAULT_OPENAI_MODEL).strip()
    return Settings(
        openai_api_key=openai_api_key,
        tavily_api_key=tavily_api_key,
        openai_model=model or DEFAULT_OPENAI_MODEL,
    )
