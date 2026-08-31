"""Stable research-system identifiers and canonical ablation ordering."""

from __future__ import annotations


LLM_ONLY_SYSTEM_VERSION = "llm-only-baseline-v0"
BASELINE_SYSTEM_VERSION = "baseline-zero"
LEDGER_SYSTEM_VERSION = "evidence-ledger-v1"
DECOMPOSED_SYSTEM_VERSION = "evidence-ledger-decomposer-v1"
VERIFIED_SYSTEM_VERSION = "evidence-ledger-decomposer-verifier-v1"

SYSTEM_VERSION_BY_MODE = {
    "llm-only": LLM_ONLY_SYSTEM_VERSION,
    "baseline": BASELINE_SYSTEM_VERSION,
    "ledger": LEDGER_SYSTEM_VERSION,
    "decomposed": DECOMPOSED_SYSTEM_VERSION,
    "verified": VERIFIED_SYSTEM_VERSION,
}

CANONICAL_SYSTEM_VERSIONS = tuple(SYSTEM_VERSION_BY_MODE.values())

CANONICAL_VERSION_LABELS = {
    LLM_ONLY_SYSTEM_VERSION: "V-1 — LLM Only",
    BASELINE_SYSTEM_VERSION: "V0 — Search Baseline",
    LEDGER_SYSTEM_VERSION: "V1 — Evidence Ledger",
    DECOMPOSED_SYSTEM_VERSION: "V2 — Decomposer",
    VERIFIED_SYSTEM_VERSION: "V3 — Verifier",
}

