"""Stable research-system identifiers and canonical ablation ordering."""

from __future__ import annotations


LLM_ONLY_SYSTEM_VERSION = "llm-only-baseline-v0"
BASELINE_SYSTEM_VERSION = "baseline-zero"
PRIOR_GUIDED_SYSTEM_VERSION = "prior-guided-baseline-v0"
LEDGER_SYSTEM_VERSION = "evidence-ledger-v1"
DECOMPOSED_SYSTEM_VERSION = "evidence-ledger-decomposer-v1"
VERIFIED_SYSTEM_VERSION = "evidence-ledger-decomposer-verifier-v1"

CANONICAL_SYSTEM_VERSION_BY_MODE = {
    "llm-only": LLM_ONLY_SYSTEM_VERSION,
    "baseline": BASELINE_SYSTEM_VERSION,
    "ledger": LEDGER_SYSTEM_VERSION,
    "decomposed": DECOMPOSED_SYSTEM_VERSION,
    "verified": VERIFIED_SYSTEM_VERSION,
}

EXPERIMENTAL_SYSTEM_VERSION_BY_MODE = {
    "prior-guided": PRIOR_GUIDED_SYSTEM_VERSION,
}

SYSTEM_VERSION_BY_MODE = {
    **CANONICAL_SYSTEM_VERSION_BY_MODE,
    **EXPERIMENTAL_SYSTEM_VERSION_BY_MODE,
}

CANONICAL_SYSTEM_VERSIONS = tuple(CANONICAL_SYSTEM_VERSION_BY_MODE.values())
EXPERIMENTAL_SYSTEM_VERSIONS = tuple(EXPERIMENTAL_SYSTEM_VERSION_BY_MODE.values())

CANONICAL_VERSION_LABELS = {
    LLM_ONLY_SYSTEM_VERSION: "V-1 — LLM Only",
    BASELINE_SYSTEM_VERSION: "V0 — Search Baseline",
    LEDGER_SYSTEM_VERSION: "V1 — Evidence Ledger",
    DECOMPOSED_SYSTEM_VERSION: "V2 — Decomposer",
    VERIFIED_SYSTEM_VERSION: "V3 — Verifier",
}

EXPERIMENTAL_VERSION_LABELS = {
    PRIOR_GUIDED_SYSTEM_VERSION: "Experimental — Prior-Guided Search",
}
