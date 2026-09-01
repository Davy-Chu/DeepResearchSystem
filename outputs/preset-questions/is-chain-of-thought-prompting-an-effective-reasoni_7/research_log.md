# Research Run Log

## Run Summary

**System Version:** evidence-ledger-decomposer-v1

**Research Question**

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

**Status:** Failed

**Stop Reason:** max_iterations

**Failure Stage:** OpenAI Ledger Report Generation

**Error**

Ledger report finding 5 maps subquestion ID(s) not attached to its ledger claims: SQ2

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 13

**OpenAI Calls:** 7

**Tavily Calls:** 3

**Started:** 2026-08-31T21:03:36-04:00

**Ended:** 2026-08-31T21:04:51-04:00

**Total Runtime:** 74.51s

---

# Research Plan

## Subquestions

### SQ1 [CORE]

**Question:**

Under what task conditions and evaluation designs does chain-of-thought prompting improve LLM performance on reasoning tasks compared with appropriate non-CoT baselines?

**Success criteria:**

Identify and compare empirical findings across task types, model capabilities, prompting methods, and baselines; distinguish genuine accuracy or reasoning gains from changes attributable to answer formatting, verbosity, or additional computation.

**Initial status:** UNRESEARCHED

### SQ2 [CORE]

**Question:**

What evidence tests whether chain-of-thought produces or elicits better underlying reasoning versus primarily improving output structure, answer decomposition, or evaluator-visible formatting?

**Success criteria:**

Examine studies using process-sensitive evaluations, controlled output formats, rationale interventions or faithfulness tests, and outcome measures beyond final-answer accuracy; state what each design can and cannot establish.

**Initial status:** UNRESEARCHED

### SQ3 [CORE]

**Question:**

Which methodological and experimental factors account for conflicting findings about chain-of-thought effectiveness?

**Success criteria:**

Synthesize evidence on model scale and training, task difficulty and domain, prompt wording and demonstrations, decoding and token/computation budgets, benchmark contamination or saturation, baseline quality, and evaluation/reproducibility choices.

**Initial status:** UNRESEARCHED

### SQ4 [CORE]

**Question:**

How should the literature’s disagreement be characterized: as a dispute about causal reasoning ability, task performance, output formatting, or the meaning of 'reasoning' itself?

**Success criteria:**

Map the main competing interpretations and identify where results genuinely conflict versus where studies measure different constructs; provide a qualified overall assessment rather than treating all CoT effects as equivalent.

**Initial status:** UNRESEARCHED

## Synthesis Requirements

- Compare studies using like-for-like baselines and preserve distinctions between final-answer accuracy, process quality, faithfulness, calibration, and formatting effects.
- Separate causal claims about internal or underlying reasoning from claims about externally observable task performance.
- Account for interactions among model capability, task characteristics, prompting, inference budget, and evaluation methodology when explaining conflicting results.
- Identify the limits of the available evidence and distinguish robust conclusions from unresolved questions.

## Output Requirements

- Explain the real fault lines in the literature.
- Explain what accounts for the conflicting results.
- Answer whether chain-of-thought is an effective reasoning strategy, primarily improves output formatting, or has context-dependent effects.

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
- **S2 — The Decreasing Value of Chain of Thought in Prompting**
  URL: https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought
- **S3 — Contrastive Chain-Of-Thought Prompting**
  URL: https://www.kore.ai/blog/contrastive-chain-of-thought-prompting
- **S4 — What is Chain of Thought (CoT) Prompting?**
  URL: https://www.nvidia.com/en-us/glossary/cot-prompting
- **S5 — What is chain of thought (CoT) prompting? - IBM**
  URL: https://www.ibm.com/think/topics/chain-of-thoughts

**Search Duration:** 2.64s

---

## 2. Evidence Processing

- New claim proposals: 5
- Existing claim updates: 0
- New gaps: 5
- Resolved gaps: 0

**Processing Duration:** 15.91s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

In the supplied empirical report, generic CoT prompting produced context-dependent final-answer effects on GPQA Diamond: it generally improved average performance for tested non-reasoning models, but effects ranged from modest or nonsignificant gains to declines under a perfect-accuracy criterion; for tested reasoning models, gains were small and one model declined.

- S2 supports (direct): Reports average gains for several non-reasoning models, a nonsignificant gain for GPT-4o-mini, declines for some models under the 100%-correct metric, and only small or negative effects for reasoning models.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C2

**Claim**

The supplied evidence indicates that generic CoT can impose substantial inference-time cost, with reported increases in response time of 35–600% for non-reasoning models and 20–80% for reasoning models in the GPQA study.

- S2 supports (direct): Reports 35–600% longer response times for non-reasoning models and 20–80% longer times for reasoning models when prompted to think step by step.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C3

**Claim**

The supplied sources support a distinction between generic flat CoT and more structured inference procedures: the Hi-CoT paper reports higher accuracy and shorter traces than its CoT comparison on the evaluated mathematical benchmarks, attributing the proposed method to hierarchical decomposition and compression bottlenecks.

- S1 supports (direct): Claims a 6.2% average accuracy improvement, up to 61.4% on some configurations, and a 13.9% reduction in trace length versus CoT across 13 model configurations and five mathematical benchmarks.

**Confidence:** LOW

**Status:** WEAK

### New Claim C4

**Claim**

Several supplied sources describe CoT as eliciting or encouraging stepwise decomposition and improved final-task performance, but these descriptions do not by themselves establish that the visible rationale is faithful to the model’s causal reasoning process.

- S4 supports (indirect): Characterizes CoT as asking models to show intermediate steps and claims benefits for complex tasks such as mathematics, logic, and planning.
- S5 supports (indirect): Describes CoT as generating intermediate logical steps and presents explanatory examples of multistep problem solving.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C5

**Claim**

The supplied report finds that many tested models produced CoT-like reasoning by default without an explicit step-by-step instruction, making an unprompted or default condition an important baseline when estimating the incremental value of generic CoT.

- S2 supports (direct): States that many models perform CoT-like reasoning under the default condition and compares explicit step-by-step prompting with both direct-answer and unprompted conditions.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Gap G1

The supplied sources do not provide controlled process-sensitive tests—such as rationale perturbation, counterfactual interventions, independent process grading, or faithfulness analyses—capable of determining whether CoT improves underlying reasoning rather than only final-answer behavior or observable output structure.

### New Gap G2

There is insufficient like-for-like evidence across task types, model scales and training regimes, prompt variants, decoding settings, and strong non-CoT baselines to determine the general boundary conditions for CoT effectiveness.

### New Gap G3

The evidence does not establish whether reported CoT gains remain after controlling for output-format instructions, generated-token or test-time-compute budgets, answer extraction procedures, and other evaluator-visible verbosity effects.

### New Gap G4

The supplied evidence does not independently verify the broad performance claims in the Hi-CoT source or clarify how much of its advantage comes from hierarchical structure, altered computation or token allocation, prompt compliance, or other differences from the CoT baseline.

### New Gap G5

The literature-level fault lines cannot yet be mapped comprehensively because the supplied material contains one focused empirical report, one recent method paper, and primarily explanatory or industry sources rather than a balanced set of replicated comparative studies.

---

## 4. Current Research State

- Claims: 5
- Supported: 4
- Weak: 1
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 5
- Remaining Searches: 2

### Subquestion Progress

**SQ1:** UNRESEARCHED → PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ2:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ3:** UNRESEARCHED → PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ4:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → PARTIAL (targeted searches: 0)
- SQ3 → PARTIAL (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- None

**Remaining targeted searches:** 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ2

**Why**

A high-priority gap remains: the supplied evidence does not include process-sensitive or faithfulness tests that distinguish genuine reasoning improvements from plausible-looking rationales and output-structure effects. Resolving this is central to the question.

**Next Search**

> chain-of-thought faithfulness process evaluation rationale perturbation interventions independent process supervision studies LLM reasoning versus post hoc explanations


---

# Iteration 2

## 1. Search

**Query**

> chain-of-thought faithfulness process evaluation rationale perturbation interventions independent process supervision studies LLM reasoning versus post hoc explanations

**Target:** SQ2

**Purpose:** SUBQUESTION

**Why this query**

A high-priority gap remains: the supplied evidence does not include process-sensitive or faithfulness tests that distinguish genuine reasoning improvements from plausible-looking rationales and output-structure effects. Resolving this is central to the question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S6 — Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures**
  URL: https://arxiv.org/html/2603.16475v1
- **S7 — Post-hoc reasoning in chain of thought**
  URL: https://www.lesswrong.com/posts/ScyXz74hughga2ncZ/post-hoc-reasoning-in-chain-of-thought
- **S8 — What Is Chain-of-Thought Faithfulness? Why AI Reasoning ...**
  URL: https://www.mindstudio.ai/blog/what-is-chain-of-thought-faithfulness-ai-reasoning
- **S9 — Chain-of-Thought (CoT) Reasoning - Quarkus**
  URL: https://quarkus.io/ai-chain-of-thought
- **S10 — What is faithful chain-of-thought reasoning and why is it useful for AI safety?**
  URL: https://blog.bluedot.org/p/faithful-chain-of-thought

**Search Duration:** 2.61s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 1
- New gaps: 1
- Resolved gaps: 1

**Processing Duration:** 10.22s

---

## 3. Ledger Updates

### New Claim C6

**Claim**

Controlled intervention evidence in the supplied sources indicates that explicit intermediate structures are not reliably causal mediators of LLM decisions: across eight models and three benchmarks, models sometimes failed to change predictions after the structures were edited, with failures reported in up to 60% of cases; external tool execution substantially reduced this fragility.

- S6 supports (direct): Reports deterministic counterfactual interventions on structured reasoning mediators across eight models and three benchmarks; models failed to update predictions after interventions in up to 60% of cases, while delegating derivation to an external tool largely removed the fragility.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C4

**Claim**

Several supplied sources describe CoT as eliciting or encouraging stepwise decomposition and improved final-task performance, but these descriptions do not by themselves establish that the visible rationale is faithful to the model’s causal reasoning process.

- S6 supports (direct): A controlled intervention study finds that models can remain unchanged when explicit intermediate structures are edited, showing that visible intermediate reasoning need not causally determine the final decision.
- S7 supports (direct): Reports prior CoT perturbation and bias-injection findings, and describes experiments in which models could have answer information available before generating CoT, supporting the possibility of post-hoc reasoning.
- S10 supports (indirect): Distinguishes faithfulness from accuracy and summarizes evidence that editing or truncating CoT does not reliably alter answers; it also describes external deterministic solvers as a way to guarantee dependence on an explicit reasoning representation.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### New Gap G6

The new intervention evidence tests faithfulness of structured intermediate representations and selected CoT-related behaviors, but it does not determine how often ordinary free-form CoT prompting itself causally improves reasoning across task types, model families, prompt designs, and difficulty levels, nor whether unfaithfulness necessarily prevents useful performance gains.

### Resolved Gap G1

The supplied sources do not provide controlled process-sensitive tests—such as rationale perturbation, counterfactual interventions, independent process grading, or faithfulness analyses—capable of determining whether CoT improves underlying reasoning rather than only final-answer behavior or observable output structure.

---

## 4. Current Research State

- Claims: 6
- Supported: 5
- Weak: 1
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 5
- Remaining Searches: 1

### Subquestion Progress

**SQ1:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ2:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ3:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ4:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → PARTIAL (targeted searches: 1)
- SQ3 → PARTIAL (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- None

**Remaining targeted searches:** 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ1

**Why**

A final search is warranted because the central unresolved issue is whether CoT gains survive strong non-CoT, output-format, and inference-compute controls. Resolving this would directly inform the main performance-versus-formatting fault line and explain conflicting results.

**Next Search**

> chain-of-thought prompting controlled comparison direct answer baseline matched token budget output format inference-time compute reasoning tasks empirical study


---

# Iteration 3

## 1. Search

**Query**

> chain-of-thought prompting controlled comparison direct answer baseline matched token budget output format inference-time compute reasoning tasks empirical study

**Target:** SQ1

**Purpose:** SUBQUESTION

**Why this query**

A final search is warranted because the central unresolved issue is whether CoT gains survive strong non-CoT, output-format, and inference-compute controls. Resolving this would directly inform the main performance-versus-formatting fault line and explain conflicting results.

5 result(s) retrieved; 3 new unique source(s) added.

- **S11 — The Token Economics of Chain-of-Thought: When Thinking Out Loud Costs More Than It's Worth**
  URL: https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more
- **S12 — A comparison of chain-of-thought reasoning strategies across ...**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11157560
- **S13 — Chain-of-Thought Prompting: A Guide for LLM Apps and Agents**
  URL: https://www.comet.com/site/blog/chain-of-thought-prompting

**Search Duration:** 2.17s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 4
- New gaps: 1
- Resolved gaps: 0

**Processing Duration:** 11.66s

---

## 3. Ledger Updates

### New Claim C7

**Claim**

In a small-scale comparison across six LLMs and six question-answering datasets involving real-world knowledge and logical verbal reasoning, zero-shot CoT variants showed gains that the study describes as robust across models and datasets, with GPT-4 benefiting most from an automatically discovered reasoning prompt.

- S12 supports (direct): The 2024 PeerJ Computer Science study compares six models and six datasets and reports that CoT gains remained robust across models and datasets, although effectiveness varied and GPT-4 benefited most from an automatically discovered prompt.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

In the supplied empirical report, generic CoT prompting produced context-dependent final-answer effects on GPQA Diamond: it generally improved average performance for tested non-reasoning models, but effects ranged from modest or nonsignificant gains to declines under a perfect-accuracy criterion; for tested reasoning models, gains were small and one model declined.

- S11 supports (indirect): The article reports that CoT has no statistically significant improvement for one-third of model-task combinations and hurts performance in others, including a reported drop in one model's perfect-accuracy rate, reinforcing context-dependent effects.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

The supplied evidence indicates that generic CoT can impose substantial inference-time cost, with reported increases in response time of 35–600% for non-reasoning models and 20–80% for reasoning models in the GPQA study.

- S11 supports (indirect): Reports that CoT can increase token use by roughly 2–5 times and reiterates response-time increases of 35–600% for non-reasoning models and 20–80% for reasoning models.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

Several supplied sources describe CoT as eliciting or encouraging stepwise decomposition and improved final-task performance, but these descriptions do not by themselves establish that the visible rationale is faithful to the model’s causal reasoning process.

- S12 supports (indirect): The study frames CoT as both a performance and explainability technique, but its supplied abstract reports predictive comparisons rather than causal or faithfulness tests; this reinforces that performance gains should not automatically be interpreted as faithful underlying reasoning.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

The supplied report finds that many tested models produced CoT-like reasoning by default without an explicit step-by-step instruction, making an unprompted or default condition an important baseline when estimating the incremental value of generic CoT.

- No new evidence relationship was added.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### New Gap G7

The cross-model, cross-dataset comparison reports robust zero-shot CoT gains, but the supplied evidence does not provide enough methodological detail to determine how those gains depend on the exact prompt variants, quality of non-CoT baselines, statistical testing, dataset difficulty, or model training and scale.

---

## 4. Current Research State

- Claims: 7
- Supported: 6
- Weak: 1
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 6
- Remaining Searches: 0

### Subquestion Progress

**SQ1:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ2:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ3:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ4:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 1)
- SQ2 → PARTIAL (targeted searches: 1)
- SQ3 → PARTIAL (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- None

**Remaining targeted searches:** 0

---

## 5. Research Decision

**Decision:** Stop researching.

**Origin:** BUDGET_STOP

**Why**

The maximum research iteration budget was reached.

**Stop Reason:** max_iterations


---

# Final Research Decision

**Research did not complete.**

**Failure Stage:** OpenAI Ledger Report Generation

**Remaining Uncertainty**

- There is insufficient like-for-like evidence across task types, model scales and training regimes, prompt variants, decoding settings, and strong non-CoT baselines to determine the general boundary conditions for CoT effectiveness.
- The evidence does not establish whether reported CoT gains remain after controlling for output-format instructions, generated-token or test-time-compute budgets, answer extraction procedures, and other evaluator-visible verbosity effects.
- The supplied evidence does not independently verify the broad performance claims in the Hi-CoT source or clarify how much of its advantage comes from hierarchical structure, altered computation or token allocation, prompt compliance, or other differences from the CoT baseline.
- The literature-level fault lines cannot yet be mapped comprehensively because the supplied material contains one focused empirical report, one recent method paper, and primarily explanatory or industry sources rather than a balanced set of replicated comparative studies.
- The new intervention evidence tests faithfulness of structured intermediate representations and selected CoT-related behaviors, but it does not determine how often ordinary free-form CoT prompting itself causally improves reasoning across task types, model families, prompt designs, and difficulty levels, nor whether unfaithfulness necessarily prevents useful performance gains.
- The cross-model, cross-dataset comparison reports robust zero-shot CoT gains, but the supplied evidence does not provide enough methodological detail to determine how those gains depend on the exact prompt variants, quality of non-CoT baselines, statistical testing, dataset difficulty, or model training and scale.
- SQ1: Under what task conditions and evaluation designs does chain-of-thought prompting improve LLM performance on reasoning tasks compared with appropriate non-CoT baselines? (PARTIAL: At least one linked ledger claim is not yet supported.)
- SQ2: What evidence tests whether chain-of-thought produces or elicits better underlying reasoning versus primarily improving output structure, answer decomposition, or evaluator-visible formatting? (PARTIAL: Open high- or medium-importance research gaps still block a sufficient answer.)
- SQ3: Which methodological and experimental factors account for conflicting findings about chain-of-thought effectiveness? (PARTIAL: At least one linked ledger claim is not yet supported.)
- SQ4: How should the literature’s disagreement be characterized: as a dispute about causal reasoning ability, task performance, output formatting, or the meaning of 'reasoning' itself? (PARTIAL: Open high- or medium-importance research gaps still block a sufficient answer.)

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Question Decomposition | 1 | 7.70s |
| Tavily Search | 3 | 7.42s |
| Evidence Processing | 3 | 37.80s |
| Research Decision | 2 | 7.23s |
| Report Generation | 1 | 0.00s |
| Total Run | — | 74.51s |
