# Research Run Log

## Run Summary

**System Version:** evidence-ledger-decomposer-v1

**Research Question**

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

**Status:** Failed

**Failure Stage:** OpenAI Evidence Processing — Iteration 1

**Error**

New claim 5 contains CONTRADICTS evidence in the SUPPORTS collection

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 1 / 3

**Unique Sources:** 5

**OpenAI Calls:** 2

**Tavily Calls:** 1

**Started:** 2026-08-31T18:11:57-04:00

**Ended:** 2026-08-31T18:12:29-04:00

**Total Runtime:** 32.03s

---

# Research Plan

## Subquestions

### SQ1 [CORE]

**Question:**

What does the literature mean by “chain-of-thought prompting,” “reasoning,” and “output formatting,” and what operational measures are used to distinguish genuine reasoning improvements from better-structured or more compliant answers?

**Success criteria:**

Establish explicit definitions and measurement criteria, including task accuracy, generalization or transfer, robustness, calibration or reliability where relevant, and formatting or instruction-following outcomes; identify whether studies use different constructs under the same labels.

**Initial status:** UNRESEARCHED

### SQ2 [CORE]

**Question:**

Across empirical studies, when and on which tasks, models, prompting methods, and evaluation setups does chain-of-thought prompting improve performance relative to appropriate baselines?

**Success criteria:**

Synthesize results across relevant task types, model scales or families, prompting variants, and comparison conditions, while preserving whether improvements concern final-answer accuracy, intermediate reasoning quality, formatting, or other outcomes.

**Initial status:** UNRESEARCHED

### SQ3 [CORE]

**Question:**

What evidence supports the claim that chain-of-thought prompting primarily improves output formatting, answer elicitation, or evaluator-visible behavior rather than underlying reasoning?

**Success criteria:**

Identify studies testing or challenging the formatting/elicitation explanation, including analyses of answer-equivalent rationales, rationale faithfulness, process interventions, hidden-state or behavioral evidence, and cases where verbose reasoning fails to improve or harms task performance.

**Initial status:** UNRESEARCHED

### SQ4 [CORE]

**Question:**

What evidence supports the claim that chain-of-thought prompting can produce genuine reasoning gains, and what limits or qualifications apply to that claim?

**Success criteria:**

Assess evidence from controlled interventions, compositional or out-of-distribution tasks, process-sensitive evaluations, and comparisons with alternative methods, distinguishing improved problem solving from improved verbalization or search-like decomposition.

**Initial status:** UNRESEARCHED

### SQ5 [CORE]

**Question:**

What methodological, model-related, task-related, and publication or evaluation factors account for conflicting findings in the literature?

**Success criteria:**

Explain disagreements in terms of baseline selection, prompt wording and demonstrations, model capabilities and scale, task difficulty and contamination, answer-verification and scoring procedures, rationale faithfulness, sampling and decoding, dataset and benchmark effects, and statistical or reporting practices, without treating all explanations as equivalent.

**Initial status:** UNRESEARCHED

### SQ6 [CORE]

**Question:**

What overall conclusion is justified about whether chain-of-thought prompting is an effective reasoning strategy, a formatting aid, or both, and under what conditions?

**Success criteria:**

Produce a conditional synthesis that separates causal claims about internal reasoning from observable performance and presentation effects, states the strength and uncertainty of evidence, and identifies the conditions under which each interpretation is best supported.

**Initial status:** UNRESEARCHED

## Synthesis Requirements

- Reconcile apparently conflicting findings rather than merely listing them, identifying the specific fault lines along which results diverge.
- Keep distinct the causal question of improved underlying reasoning from the observational questions of final-answer accuracy, rationale quality, answer elicitation, and output formatting.
- Compare studies using appropriate baselines and preserve differences in models, tasks, prompts, evaluation protocols, and timeframes where relevant.
- Assess the quality and limitations of evidence and explicitly represent uncertainty rather than presenting a single undifferentiated verdict.

## Output Requirements

- Explain the real fault lines in the literature and what accounts for the conflicting results.
- Answer the either/or framing while allowing for a conditional or mixed conclusion if supported by the evidence.
- Present the result as a literature-grounded synthesis, not as an unsupported assertion.

---

# Iteration 1

## 1. Search

**Query**

> Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

**Purpose:** GENERAL

**Why this query**

This is the user's original research question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S1 — Hierarchical Chain-of-Thought Prompting: Enhancing LLM ...**
  URL: https://arxiv.org/html/2604.00130v1
- **S2 — Contrastive Chain-Of-Thought Prompting**
  URL: https://www.kore.ai/blog/contrastive-chain-of-thought-prompting
- **S3 — 🧠What is LLM Chain of Thought Prompting? | by Tahir**
  URL: https://medium.com/@tahirbalarabe2/what-is-llm-chain-of-thought-prompting-1d4b57a4dd22
- **S4 — What is Chain of Thought (CoT) Prompting?**
  URL: https://www.nvidia.com/en-us/glossary/cot-prompting
- **S5 — Chain-of-Thought Prompting: Helping LLMs Learn by Example**
  URL: https://deepgram.com/learn/chain-of-thought-prompting-guide

**Search Duration:** 2.56s

---

## 2. Evidence Processing

Evidence processing did not complete.

---

## 3. Ledger Updates

No ledger update was completed.

---

## 4. Current Research State

- Claims: 0
- Supported: 0
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 2

---

## 5. Research Decision

No research decision was completed for this iteration.

---

# Final Research Decision

**Research did not complete.**

**Failure Stage:** OpenAI Evidence Processing — Iteration 1

**Remaining Uncertainty**

- SQ1: What does the literature mean by “chain-of-thought prompting,” “reasoning,” and “output formatting,” and what operational measures are used to distinguish genuine reasoning improvements from better-structured or more compliant answers? (UNRESEARCHED: No evidence has been processed yet.)
- SQ2: Across empirical studies, when and on which tasks, models, prompting methods, and evaluation setups does chain-of-thought prompting improve performance relative to appropriate baselines? (UNRESEARCHED: No evidence has been processed yet.)
- SQ3: What evidence supports the claim that chain-of-thought prompting primarily improves output formatting, answer elicitation, or evaluator-visible behavior rather than underlying reasoning? (UNRESEARCHED: No evidence has been processed yet.)
- SQ4: What evidence supports the claim that chain-of-thought prompting can produce genuine reasoning gains, and what limits or qualifications apply to that claim? (UNRESEARCHED: No evidence has been processed yet.)
- SQ5: What methodological, model-related, task-related, and publication or evaluation factors account for conflicting findings in the literature? (UNRESEARCHED: No evidence has been processed yet.)
- SQ6: What overall conclusion is justified about whether chain-of-thought prompting is an effective reasoning strategy, a formatting aid, or both, and under what conditions? (UNRESEARCHED: No evidence has been processed yet.)

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Question Decomposition | 1 | 9.03s |
| Tavily Search | 1 | 2.56s |
| Evidence Processing | 1 | 0.00s |
| Research Decision | 0 | 0.00s |
| Report Generation | 0 | 0.00s |
| Total Run | — | 32.03s |
