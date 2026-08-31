"""Versioned evaluator-v1 configuration."""

from __future__ import annotations

import os

from research.config import DEFAULT_OPENAI_MODEL

EVALUATOR_VERSION = "evaluator-v1"
EVALUATOR_SCHEMA_VERSION = "1.0"
RUBRIC_VERSION = "1.0"
FIXTURE_VERSION = "1.0"

COMPREHENSIVENESS_WEIGHT = 0.60
CITATION_WEIGHT = 0.30
DETERMINISTIC_WEIGHT = 0.10

COVERAGE_WEIGHT = 0.70
DEPTH_WEIGHT = 0.30

CITATION_VALIDITY_WEIGHT = 0.15
CITATION_SUPPORT_WEIGHT = 0.55
CITATION_COMPLETENESS_WEIGHT = 0.30

RUBRIC_BUILDER_PROMPT_VERSION = "1.0"
RUBRIC_CRITIC_PROMPT_VERSION = "1.0"
COMPREHENSIVENESS_PROMPT_VERSION = "1.0"
CITATION_SUPPORT_PROMPT_VERSION = "1.0"
CITATION_COMPLETENESS_PROMPT_VERSION = "1.0"


def load_evaluator_model() -> str:
    """Load v1's model, retaining evaluator-v0's legacy variable as a fallback."""

    return (
        os.getenv("OPENAI_EVALUATOR_MODEL", "").strip()
        or os.getenv("EVALUATOR_MODEL", "").strip()
        or os.getenv("OPENAI_MODEL", "").strip()
        or DEFAULT_OPENAI_MODEL
    )


def scoring_weights() -> dict[str, float]:
    return {
        "comprehensiveness": COMPREHENSIVENESS_WEIGHT,
        "citations": CITATION_WEIGHT,
        "deterministic": DETERMINISTIC_WEIGHT,
    }


def prompt_versions() -> dict[str, str]:
    return {
        "rubric_builder": RUBRIC_BUILDER_PROMPT_VERSION,
        "rubric_critic": RUBRIC_CRITIC_PROMPT_VERSION,
        "comprehensiveness": COMPREHENSIVENESS_PROMPT_VERSION,
        "citation_support": CITATION_SUPPORT_PROMPT_VERSION,
        "citation_completeness": CITATION_COMPLETENESS_PROMPT_VERSION,
    }
