# Research Run Log

## Run Summary

**System Version:** evidence-ledger-decomposer-verifier-v1

**Research Question**

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 14

**OpenAI Calls:** 9

**Tavily Calls:** 3

**Verifier Model:** gpt-5.6-luna

**Started:** 2026-08-31T15:02:23-04:00

**Ended:** 2026-08-31T15:04:30-04:00

**Total Runtime:** 127.02s

---

# Research Plan

## Subquestions

### SQ1 [CORE]

**Question:**

What does the literature mean by “chain-of-thought prompting,” and how is “reasoning effectiveness” operationalized versus improvements in output formatting, verbosity, answerability, or task compliance?

**Success criteria:**

Identify the main CoT variants and establish outcome measures that distinguish latent/task-solving performance from merely more structured, longer, or better-formatted outputs; note any limitations in measuring internal reasoning from external responses.

**Initial status:** UNRESEARCHED

### SQ2 [CORE]

**Question:**

Across studies, does chain-of-thought prompting causally improve task-solving accuracy or general reasoning ability relative to appropriate baselines, and under what task and model conditions?

**Success criteria:**

Compare CoT with relevant baselines such as direct-answer prompting, few-shot examples without rationales, alternative decomposition methods, and increased test-time computation; separate gains on arithmetic, symbolic, commonsense, knowledge-intensive, and other task types, while preserving model-size and timeframe distinctions.

**Initial status:** UNRESEARCHED

### SQ3 [CORE]

**Question:**

What evidence supports the claim that CoT mainly improves presentation, answer elicitation, or evaluator perception rather than underlying reasoning?

**Success criteria:**

Assess studies testing rationale faithfulness, process validity, answer-after-rationale effects, formatting controls, rationale-free reasoning methods, and evaluations resistant to verbosity or judge bias; distinguish improved external performance from evidence of improved internal reasoning.

**Initial status:** UNRESEARCHED

### SQ4 [CORE]

**Question:**

What methodological and experimental factors account for conflicting findings about CoT effectiveness?

**Success criteria:**

Identify and compare effects of prompt design, demonstrations and rationale quality, model family and scale, task difficulty and distribution shift, decoding and sampling, self-consistency or other inference-time compute, evaluation metrics and graders, contamination or benchmark artifacts, and publication or selection effects.

**Initial status:** UNRESEARCHED

### SQ5 [SECONDARY]

**Question:**

Which conclusions are robust across the literature, which remain conditional or disputed, and what experiments would best resolve the remaining fault lines?

**Success criteria:**

Synthesize convergent and divergent evidence into clearly qualified claims about when CoT helps, when it fails or misleads, and whether observed benefits reflect reasoning, search, decomposition, calibration, or formatting; propose discriminating tests grounded in the identified disagreements.

**Initial status:** UNRESEARCHED

## Synthesis Requirements

- Explicitly distinguish causal improvements in problem-solving or reasoning from changes in output format, verbosity, answer elicitation, evaluator judgments, or benchmark compliance.
- Explain the major fault lines in the literature rather than presenting only a chronological or study-by-study summary.
- Account for conflicting results through moderators and methodological differences, including model, task, prompt, inference-time computation, and evaluation choices.
- Preserve uncertainty and report where conclusions are robust versus conditional, disputed, or limited by the evidence.
- Compare findings against appropriate baselines and avoid treating the presence of a rationale alone as proof of faithful internal reasoning.

## Output Requirements

- Answer the question of whether CoT is an effective reasoning strategy, while qualifying the answer by task, model, and evaluation context.
- Explain what accounts for the conflicting results in the literature.
- Present the real disagreements or fault lines explicitly, with evidence-based distinctions between competing interpretations.

---

# Iteration 1

## 1. Search

**Query**

> Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

**Purpose:** GENERAL

**Why this query**

This is the user's original research question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S1 — Hierarchical Chain-of-Thought Prompting: Enhancing LLM Reasoning Performance and Efficiency**
  URL: https://arxiv.org/html/2604.00130v1
- **S2 — The Decreasing Value of Chain of Thought in Prompting**
  URL: https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought
- **S3 — Medium**
  URL: https://cobusgreyling.medium.com/chain-of-thought-prompting-in-llms-1077164edf97
- **S4 — What is chain of thought (CoT) prompting? - IBM**
  URL: https://www.ibm.com/think/topics/chain-of-thoughts
- **S5 — What is Chain of Thought (CoT) Prompting? | NVIDIA Glossary**
  URL: https://www.nvidia.com/en-us/glossary/cot-prompting

**Search Duration:** 3.05s

---

## 2. Evidence Processing

- New claim proposals: 5
- Existing claim updates: 0
- New gaps: 4
- Resolved gaps: 0

**Processing Duration:** 16.95s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

Chain-of-thought prompting is an inference-time method that elicits intermediate natural-language steps before a final answer; variants in the supplied sources include few-shot CoT, zero-shot CoT, automatic CoT, self-consistency, and structured or hierarchical CoT.

- S1 supports (direct): Defines conventional CoT as generating intermediate reasoning steps and identifies zero-shot, Auto-CoT, Self-Consistency, and Hi-CoT as variants.
- S4 supports (direct): Describes CoT as appending an instruction to explain an answer step by step and distinguishes it from multi-prompt prompt chaining.
- S5 supports (indirect): Describes CoT as using demonstrations and stepwise intermediate reasoning, and relates it to automated test-time scaling.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C2

**Claim**

The supplied empirical evidence does not support treating generic CoT as uniformly beneficial: effects vary by model type, task, and evaluation metric, with larger average gains reported for some non-reasoning models and small or negative effects for several reasoning models or stringent accuracy thresholds.

- S2 supports (direct): In a GPQA Diamond study with repeated trials, non-reasoning models showed average gains ranging from 4.4% to 13.5%, while reasoning models showed only small gains for some models and a 3.3% decrease for another; perfect-accuracy results were mixed, including a 17.2% decline for Gemini Pro 1.5.
- S1 supports (direct): Reports that its structured Hi-CoT variant improved accuracy over conventional CoT on five mathematical benchmarks, implying that the effectiveness of reasoning prompts depends on structure rather than generic CoT alone.
- S3 contradicts (indirect): Presents an unqualified general claim that CoT significantly improves complex-task reasoning, but provides no reported experimental details in the supplied text.
- S4 contradicts (indirect): States that CoT significantly boosts accuracy on multistep arithmetic, common-sense, and symbolic tasks, but the supplied material is an explanatory account rather than a controlled comparative study.
- S5 contradicts (indirect): Claims substantial and broad improvements in reasoning accuracy, but the supplied glossary does not report controlled results or uncertainty estimates.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C3

**Claim**

For the GPQA Diamond evaluation described in S2, CoT increased inference time and token-related cost substantially relative to direct answering, while its accuracy benefits were inconsistent; the reported cost was 35–600% longer for non-reasoning models and 20–80% longer for reasoning models.

- S2 supports (direct): Reports 5–15 additional seconds for non-reasoning models and 10–20 additional seconds for reasoning models, with the corresponding percentage increases and limited gains for reasoning models.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C4

**Claim**

The presence of a longer or more structured rationale is not, by itself, evidence that the model has improved faithful internal reasoning; the supplied sources explicitly note that longer traces can be redundant or disorganized, and S2 reports that many models produce CoT-like reasoning by default.

- S1 supports (direct): States that longer traces do not imply better reasoning and may reflect repetition, hedging, or unguided exploration; it motivates hierarchical compression to reduce redundancy.
- S2 supports (direct): Reports that many tested models produce CoT-like reasoning without an explicit CoT instruction, complicating comparisons between prompted and unprompted conditions.
- S4 contradicts (indirect): Frames articulated intermediate steps as a glimpse of the model’s reasoning process and as useful for transparency and debugging, but does not establish faithfulness experimentally.
- S5 contradicts (indirect): Associates showing work with improved reasoning and transparency, without supplying evidence that the displayed chain faithfully caused the answer.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C5

**Claim**

A structured hierarchical prompting variant, Hi-CoT, is reported to improve both accuracy and trace efficiency relative to conventional CoT on the study’s tested models and mathematical benchmarks, suggesting that prompt organization and compression may moderate CoT outcomes.

- S1 supports (direct): Reports a 6.2% average accuracy improvement, up to 61.4% on some model-task combinations, and a 13.9% reduction in trace length across 13 Qwen3 and DeepSeek-R1 configurations and five mathematical benchmarks.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Gap G1

The supplied evidence does not directly establish whether CoT rationales are faithful causal accounts of the computations that produced answers, nor whether improvements persist when evaluations control for verbosity, formatting, answer elicitation, and evaluator or judge bias.

### New Gap G2

Evidence is insufficient to compare generic CoT against all appropriate baselines, including rationale-free few-shot prompting, alternative decomposition methods, hidden test-time computation, self-consistency, and matched inference-token budgets across arithmetic, symbolic, commonsense, and knowledge-intensive tasks.

### New Gap G3

The sources do not identify how rationale quality, demonstration selection, model scale and training, decoding or sampling settings, distribution shift, contamination, or publication and selection effects account for conflicting findings.

### New Gap G4

The reported S2 results come from one GPQA Diamond study and the S1 results from one Hi-CoT preprint focused on mathematical benchmarks; robustness across datasets, model families, task domains, and independent replications remains unresolved.

---

## 4. Current Research State

- Claims: 5
- Supported: 5
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 4
- Remaining Searches: 2

### Subquestion Progress

**SQ1:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ3:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ4:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ5:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → PARTIAL (targeted searches: 0)
- SQ3 → PARTIAL (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- SQ5 → PARTIAL (targeted searches: 0)

**Remaining targeted searches:** 2

---

## 5. Independent Verification

### V1 — Claim C2

**Phase:** INITIAL

**Evidence source IDs:** S2, S1, S3, S4, S5

**Verdict:** NEEDS_QUALIFICATION

**Reason**

S2 directly supports non-uniform effects across model types and evaluation thresholds: non-reasoning models showed larger average gains, while several reasoning models had small or negative changes, especially under stringent accuracy metrics. However, the supplied empirical evidence is largely one GPQA Diamond study, so variation across task types and broader literature cannot be established confidently. S1 provides only indirect support because it evaluates a structured Hi-CoT variant rather than generic CoT.

**Missing assumptions**

- The GPQA Diamond results generalize beyond this dataset and experimental setup.
- The observed differences are attributable to generic CoT rather than prompt wording, decoding, sampling, or other protocol choices.
- Claims about task-dependent effects require evidence from multiple task domains, not only GPQA Diamond.
- The model categories and comparisons are sufficiently matched for causal interpretation.

**Source concerns**

- S2 is a single 2025 technical report and the saved material does not provide full statistical tables, baselines, or independent replication details.
- S1 is a preprint evaluating hierarchical CoT, not generic CoT, and its reported results cannot directly validate the claim about generic CoT.
- S3-S5 are explanatory or promotional sources rather than independent empirical syntheses.

**Counter-search status:** EXECUTED

**Counter-search query:**

> independent empirical studies or meta-analyses comparing generic chain-of-thought prompting with direct-answer and rationale-free baselines across non-reasoning and reasoning models, tasks, and strict accuracy metrics; include null, negative, replication, and formatting-only findings

**Counter-search evidence:** S6, S7, S8, S9

---

## 6. Research Decision

**Decision:** Continue researching.

**Origin:** VERIFIER_COUNTERSEARCH

**Target:** CLAIM C2

**Why**

Independent verification of C2 identified a high-value falsification search: S2 directly supports non-uniform effects across model types and evaluation thresholds: non-reasoning models showed larger average gains, while several reasoning models had small or negative changes, especially under stringent accuracy metrics. However, the supplied empirical evidence is largely one GPQA Diamond study, so variation across task types and broader literature cannot be established confidently. S1 provides only indirect support because it evaluates a structured Hi-CoT variant rather than generic CoT.

**Next Search**

> independent empirical studies or meta-analyses comparing generic chain-of-thought prompting with direct-answer and rationale-free baselines across non-reasoning and reasoning models, tasks, and strict accuracy metrics; include null, negative, replication, and formatting-only findings


---

# Iteration 2

## 1. Search

**Query**

> independent empirical studies or meta-analyses comparing generic chain-of-thought prompting with direct-answer and rationale-free baselines across non-reasoning and reasoning models, tasks, and strict accuracy metrics; include null, negative, replication, and formatting-only findings

**Target:** C2

**Purpose:** COUNTERSEARCH

**Why this query**

Independent verification of C2 identified a high-value falsification search: S2 directly supports non-uniform effects across model types and evaluation thresholds: non-reasoning models showed larger average gains, while several reasoning models had small or negative changes, especially under stringent accuracy metrics. However, the supplied empirical evidence is largely one GPQA Diamond study, so variation across task types and broader literature cannot be established confidently. S1 provides only indirect support because it evaluates a structured Hi-CoT variant rather than generic CoT.

5 result(s) retrieved; 4 new unique source(s) added.

- **S6 — Chain-of-Thought Reasoning**
  URL: https://www.emergentmind.com/topics/chain-of-thought-reasoning-fc14269b-22e7-4eea-ad24-c345984799e4
- **S7 — Chain of Thought Prompting in AI: A Comprehensive Guide [2026]**
  URL: https://futureagi.substack.com/p/chain-of-thought-prompting-in-ai
- **S8 — Chain-of-Thought Reasoning**
  URL: https://www.emergentmind.com/topics/chain-of-thought-cot-reasoning-fd86d712-e431-4308-affd-c5dbdf17030a
- **S9 — GPT-4.1 Mini & Chain-of-Thought Prompting**
  URL: https://www.emergentmind.com/topics/gpt-4-1-mini-with-chain-of-thought-prompting

**Search Duration:** 4.86s

---

## 2. Evidence Processing

- New claim proposals: 3
- Existing claim updates: 3
- New gaps: 2
- Resolved gaps: 0

**Processing Duration:** 21.31s

---

## 3. Ledger Updates

### New Claim C6

**Claim**

Across the supplied synthesis, CoT benefits appear task-dependent: reported gains are strongest for mathematical, symbolic, and logical tasks, while factual recall, comprehension, and some softer reasoning tasks show minimal or no benefit; one source also reports that CoT can hurt in pattern-based in-context learning when explicit rationales are noisy or incorrect.

- S8 supports (indirect): Summarizes a meta-analysis and empirical studies reporting median gains above 12 percentage points for symbolic and mathematical tasks, moderate gains for logic, and minimal or zero gains for factual recall and comprehension; it also describes cases where explicit CoT hurts pattern-based in-context learning.
- S6 contradicts (indirect): Claims broad improvements across arithmetic, logic, commonsense, algorithmic, and mathematical QA tasks, including large gains over non-CoT baselines, although the supplied text is a secondary synthesis and mixes prompting with distillation and other variants.
- S9 contradicts (indirect): Reports gains from a discovered CoT template across commonsense, science, and medical QA datasets, suggesting benefits beyond mathematical and symbolic tasks; the reported evidence is limited to one summarized evaluation.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C7

**Claim**

CoT rationales may be post-hoc or unfaithful explanations rather than faithful records of the computations that determine an answer; the supplied material describes logically inconsistent or shortcut traces and reports that strong prior beliefs can cause rationales to reaffirm an answer rather than revise it.

- S6 supports (direct): States that studies have found unfaithful or post-hoc rationalizations, including inconsistent or shortcut traces, and describes confirmation-bias effects in which prior answer beliefs suppress rationale informativeness.
- S8 supports (indirect): Describes a confirmation-bias account in which rationales often reaffirm initial priors, especially when the model is highly confident, and notes unresolved mechanisms behind CoT success.
- S7 contradicts (indirect): Presents visible stepwise explanations as transparent and useful for verification and debugging, but supplies no causal faithfulness test.
- S8 contradicts (indirect): Also presents CoT as human-auditable and reports improved transparency, though this concerns inspectability rather than demonstrated causal faithfulness.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C8

**Claim**

Automated search and engineering of CoT prompt templates can improve performance relative to direct-answer prompting, but the reported gains depend on prompt wording, validation procedures, model capacity, and domain coverage rather than on the mere presence of a rationale.

- S9 supports (direct): Reports a 12-point accuracy difference between a direct prompt and a discovered step-by-step template and describes beam-search prompt optimization, cross-domain validation, diversity controls, and greater gains for higher-capacity instruction-tuned models.
- S7 contradicts (indirect): States that explicit CoT can add latency without benefit on simple tasks, can hurt with small models, and may be redundant for models that reason natively; this is a practical guide rather than a controlled study.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

Chain-of-thought prompting is an inference-time method that elicits intermediate natural-language steps before a final answer; variants in the supplied sources include few-shot CoT, zero-shot CoT, automatic CoT, self-consistency, and structured or hierarchical CoT.

- S6 supports (direct): Defines CoT as generating a rationale sequence before an answer and distinguishes zero-shot triggers from few-shot demonstrations.
- S8 supports (direct): Extends the supplied variant space to program-based, symbolic-aided, fine-tuned, and latent or structured forms of CoT.
- S9 supports (direct): Describes direct cues and in-context exemplars that elicit explicit intermediate steps and discusses automated template discovery.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

The supplied empirical evidence does not support treating generic CoT as uniformly beneficial: effects vary by model type, task, and evaluation metric, with larger average gains reported for some non-reasoning models and small or negative effects for several reasoning models or stringent accuracy thresholds.

- S8 supports (indirect): Summarizes task-level heterogeneity, with larger reported benefits for mathematical and symbolic reasoning, smaller logic gains, and little benefit for factual recall and comprehension; it also describes cases where explicit CoT hurts.
- S9 supports (direct): Reports a 12-point gain from an optimized CoT template over direct answering across six QA datasets and links gains to model capacity, instruction tuning, and prompt construction.
- S7 supports (indirect): States that CoT is not useful for all tasks and may be redundant or harmful for simple tasks, small models, and models with native reasoning modes.
- S6 contradicts (indirect): Reports broad gains across BBH, mathematical QA, logic, commonsense, and algorithmic benchmarks, including large improvements from CoT-related distillation and self-consistency; these results combine generic CoT with specialized variants and training methods.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

The presence of a longer or more structured rationale is not, by itself, evidence that the model has improved faithful internal reasoning; the supplied sources explicitly note that longer traces can be redundant or disorganized, and S2 reports that many models produce CoT-like reasoning by default.

- S6 supports (direct): Explicitly reports unfaithful or post-hoc rationalizations, shortcut traces, and confirmation-bias effects that can reduce the informativeness of rationales.
- S8 supports (indirect): Describes pattern-matching and explicit-implicit-duality accounts in which visible chains may reflect learned output patterns or introduce noisy explicit reasoning rather than improve latent inference.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### New Gap G5

The supplied sources report task-level meta-analytic and cross-domain patterns, but do not provide enough underlying study details to determine whether the apparent domain differences survive matched baselines, equalized inference-time computation, contamination controls, and independent replication.

### New Gap G6

The new sources describe rationale unfaithfulness and confirmation bias but do not establish how frequently these occur, whether they mediate accuracy gains, or which causal faithfulness tests best distinguish genuine intermediate computation from post-hoc explanation.

---

## 4. Current Research State

- Claims: 8
- Supported: 8
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 6
- Remaining Searches: 1

### Subquestion Progress

**SQ1:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ3:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ4:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ5:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → PARTIAL (targeted searches: 0)
- SQ3 → PARTIAL (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- SQ5 → PARTIAL (targeted searches: 0)

**Remaining targeted searches:** 1

---

## 5. Independent Verification

### V2 — Claim C2

**Phase:** POST_COUNTERSEARCH

**Evidence source IDs:** S2, S1, S8, S9, S7, S3, S4, S5, S6

**Verdict:** VERIFIED

**Reason**

S2 directly reports heterogeneous effects: non-reasoning models show larger average gains, while reasoning models show marginal gains or declines; threshold-based accuracy metrics also produce mixed and sometimes negative effects. The broader sources do not materially negate this qualified formulation, although they emphasize positive results in selected tasks and variants.

**Missing assumptions**

- The comparison concerns generic, explicit CoT prompts rather than structured variants, distillation, self-consistency, or other enhanced methods.
- The reported pattern is conditional on the tested GPQA Diamond task, model set, prompting conditions, and evaluation thresholds; it should not be generalized to all models or tasks.
- “Reasoning models” refers to the specific tested models with built-in reasoning capabilities, not a uniformly defined model category.

**Source concerns**

- The strongest direct evidence is one 2025 technical report rather than a broad independently replicated literature synthesis.
- Several other sources are industry or tertiary summaries and report selected positive results without providing enough methodological detail for strong cross-study inference.
- The supplied evidence does not establish that model type, task, or metric independently causes the variation; these factors may be confounded.

**Counter-search status:** NOT_REQUESTED

**Reconciliation**

Confidence: HIGH → HIGH

Status: SUPPORTED → SUPPORTED

---

## 6. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ3

**Why**

A final search could materially improve the answer by addressing the central unresolved fault line: whether CoT rationales are causally faithful reasoning traces or mainly post-hoc, formatting, or evaluator-facing explanations. Existing evidence is only summarized and does not establish prevalence, mediation of accuracy gains, or robustness to verbosity and judge bias controls.

**Next Search**

> Empirical studies testing chain-of-thought rationale faithfulness and causal necessity: do answer interventions, rationale perturbation, process supervision, hidden-reasoning controls, verbosity-matched evaluations, and evaluator-bias-resistant tests show genuine reasoning gains versus post-hoc explanation or formatting effects?


---

# Iteration 3

## 1. Search

**Query**

> Empirical studies testing chain-of-thought rationale faithfulness and causal necessity: do answer interventions, rationale perturbation, process supervision, hidden-reasoning controls, verbosity-matched evaluations, and evaluator-bias-resistant tests show genuine reasoning gains versus post-hoc explanation or formatting effects?

**Target:** SQ3

**Purpose:** SUBQUESTION

**Why this query**

A final search could materially improve the answer by addressing the central unresolved fault line: whether CoT rationales are causally faithful reasoning traces or mainly post-hoc, formatting, or evaluator-facing explanations. Existing evidence is only summarized and does not establish prevalence, mediation of accuracy gains, or robustness to verbosity and judge bias controls.

5 result(s) retrieved; 5 new unique source(s) added.

- **S10 — What Is Chain-of-Thought Faithfulness? Why AI Reasoning Traces Are Unreliable | MindStudio**
  URL: https://www.mindstudio.ai/blog/what-is-chain-of-thought-faithfulness-ai-reasoning
- **S11 — FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning - ACL Anthology**
  URL: https://aclanthology.org/2026.findings-acl.1014
- **S12 — FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning**
  URL: https://arxiv.org/html/2604.10693v1
- **S13 — Causal Sufficiency and Necessity Improves Chain-of- ...**
  URL: https://haoxuanli-pku.github.io/papers/NeurIPS%2025%20-%20Causal%20Sufficiency%20and%20Necessity%20Improves%20Chain-of-Thought%20Reasoning.pdf
- **S14 — Multi-Dimensional Evaluation of Auto-Generated Chain-of-Thought Traces in Reasoning Models**
  URL: https://www.mdpi.com/2673-2688/7/1/35

**Search Duration:** 3.06s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 2
- New gaps: 2
- Resolved gaps: 0

**Processing Duration:** 14.35s

---

## 3. Ledger Updates

### New Claim C9

**Claim**

Causality-inspired evaluation and selection methods can improve CoT trajectory quality by testing step-level dependence, sufficiency, and necessity rather than relying only on rationale coherence or final-answer agreement; the supplied studies report improved accuracy or reduced token use on selected mathematical and commonsense benchmarks.

- S11 supports (direct): FACT-E uses controlled perturbations to estimate intra-chain faithfulness and combines this with CoT-to-answer consistency; experiments on GSM8K, MATH, and CommonsenseQA report improved trajectory selection and stronger in-context exemplars.
- S12 supports (direct): Describes the limitations of answer-centric and self-evaluation methods and reports that FACT-E improves answer accuracy, in-context learning, and detection of flawed reasoning under noisy conditions.
- S13 supports (direct): Uses causal Probability of Necessity and Sufficiency to identify indispensable and redundant steps; experiments on mathematical and commonsense benchmarks report reduced reasoning redundancy and token usage while maintaining or improving accuracy.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C4

**Claim**

Longer or more structured rationales are not, by themselves, evidence that an LLM has improved faithful reasoning: the supplied evidence notes that longer traces can be redundant or disorganized, and S2 reports that many models produce CoT-like outputs by default. Such traces may improve answer elicitation or presentation without demonstrating that the stated rationale faithfully reflects the computation producing the answer.

- S10 supports (direct): Defines faithfulness as correspondence between stated reasoning and the computation influencing the answer, and describes bias-injection and truncation tests in which model behavior can diverge from the displayed rationale.
- S11 supports (direct): States that coherent-looking explanations can contain unfaithful intermediate steps and that ordinary self-evaluation can endorse invalid step-to-step implications.
- S12 supports (direct): Reports that models can produce correct, persuasive traces with broken logical dependencies and that answer-centric self-evaluation can miss intra-chain unfaithfulness.
- S13 supports (direct): Argues that correlation-based indicators such as likelihood, attention, or ablation accuracy can misidentify genuinely necessary or sufficient steps, motivating causal intervention.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C7

**Claim**

CoT rationales may be post-hoc or unfaithful explanations rather than faithful records of the computations that determine an answer; the supplied material describes logically inconsistent or shortcut traces and reports that strong prior beliefs can cause rationales to reaffirm an answer rather than revise it.

- S10 supports (direct): Reports bias-injection findings in which answers shift in response to hidden bias cues while rationales omit the influential cue, and describes early-truncation results as evidence that some conclusions precede completion of the stated trace.
- S11 supports (direct): Motivates FACT-E by noting that models often generate coherent explanations with unfaithful intermediate steps and that self-evaluators may confidently validate invalid logical links.
- S12 supports (direct): Describes broken dependencies, inaccurate content, self-affirmation bias, and a closed-loop failure in which LLM evaluators overrate their own reasoning traces.
- S13 supports (direct): Notes that correlation-based measures can associate prominent or frequent steps with correctness without demonstrating causal contribution, and uses causal interventions to assess necessity and sufficiency.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### New Gap G7

The supplied causal faithfulness methods report improved trajectory selection, efficiency, or accuracy, but the evidence does not establish whether these improvements reflect better underlying problem solving rather than better filtering, exemplar construction, or inference-time search; direct comparisons with generic CoT, rationale-free methods, and matched-compute baselines remain absent.

### New Gap G8

The new sources propose perturbation, truncation, error-injection, and necessity/sufficiency tests, but do not provide enough comparative evidence to determine which faithfulness measure is valid, how their estimates agree, or how robust they are across model families, task domains, and hidden reasoning systems.

---

## 4. Current Research State

- Claims: 9
- Supported: 9
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 8
- Remaining Searches: 0

### Subquestion Progress

**SQ1:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ3:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ4:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ5:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → PARTIAL (targeted searches: 0)
- SQ3 → PARTIAL (targeted searches: 1)
- SQ4 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- SQ5 → PARTIAL (targeted searches: 0)

**Remaining targeted searches:** 0

---

## 5. Independent Verification

### V3 — Claim C4

**Phase:** INITIAL

**Evidence source IDs:** S1, S2, S6, S8, S10, S11, S12, S13, S4, S5

**Verdict:** NEEDS_QUALIFICATION

**Reason**

The evidence supports the core methodological point: rationale length or visible structure does not establish faithful underlying computation. S1 explicitly warns that longer traces may be redundant or disorganized, and S2 reports that many models generate CoT-like outputs by default. However, the claim should distinguish external rationale faithfulness from unobservable 'internal reasoning,' and the evidence directly supports length more clearly than structure in general.

**Missing assumptions**

- That the cited observations generalize beyond the models, tasks, and prompting conditions studied.
- That a CoT-like default output reflects reasoning-like presentation, not necessarily a particular internal computational process.
- That 'structured' rationale refers to surface organization rather than independently validated causal or process structure.

**Source concerns**

- S1 is an arXiv preprint and includes claims from a future-dated work context.
- S2 is a technical report rather than a peer-reviewed publication, and the supplied excerpt does not provide full statistical details.
- The strongest direct evidence for unfaithfulness comes from secondary or summary sources, while the cited claim relies mainly on S1 and S2.

**Counter-search status:** NOT_REQUESTED

**Reconciliation**

Claim:

"The presence of a longer or more structured rationale is not, by itself, evidence that the model has improved faithful internal reasoning; the supplied sources explicitly note that longer traces can be redundant or disorganized, and S2 reports that many models produce CoT-like reasoning by default."
→
"Longer or more structured rationales are not, by themselves, evidence that an LLM has improved faithful reasoning: the supplied evidence notes that longer traces can be redundant or disorganized, and S2 reports that many models produce CoT-like outputs by default. Such traces may improve answer elicitation or presentation without demonstrating that the stated rationale faithfully reflects the computation producing the answer."

Confidence: HIGH → HIGH

Status: SUPPORTED → SUPPORTED

---

## 6. Research Decision

**Decision:** Stop researching.

**Origin:** BUDGET_STOP

**Why**

The maximum research iteration budget was reached.

**Stop Reason:** max_iterations


---

# Final Research Decision

**Stop Reason:** max_iterations

**Remaining Uncertainty**

- Generic CoT has not been adequately compared with rationale-free few-shot prompting, alternative decomposition methods, hidden test-time computation, self-consistency, and matched inference-token budgets across the relevant task families.
- The supplied evidence does not establish whether rationales are faithful causal accounts, how frequently they are unfaithful, or whether faithfulness mediates accuracy gains.
- The evidence does not identify the independent effects of rationale quality, demonstrations, model scale and training, decoding and sampling, distribution shift, contamination, benchmark design, or publication and selection effects.
- The strongest direct performance evidence comes from one GPQA Diamond technical report and one Hi-CoT preprint focused on mathematical benchmarks; broader independent replication is unresolved.
- The supplied causal faithfulness measures have not been sufficiently compared with one another or validated across model families, domains, and hidden-reasoning systems.
- The ledger indicates that a counter-search was executed for the main heterogeneous-effects claim, but the stop reason was max_iterations; the remaining gaps therefore reflect unresolved evidence, not a completed literature-wide resolution.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Question Decomposition | 1 | 12.20s |
| Tavily Search | 3 | 10.98s |
| Evidence Processing | 3 | 52.60s |
| Independent Verification | 3 | 25.09s |
| Research Decision | 1 | 3.12s |
| Report Generation | 1 | 23.02s |
| Total Run | — | 127.02s |

# Verifier Diagnostics

- Verification calls: 3
- Claims verified: 2
- VERIFIED verdicts: 1
- NEEDS_QUALIFICATION verdicts: 2
- CONTRADICTED verdicts: 0
- INSUFFICIENT_EVIDENCE verdicts: 0
- Counter-searches requested: 1
- Counter-searches executed: 1
- Counter-searches blocked by budget: 0
- Counter-searches blocked as duplicates: 0
- Claims whose wording changed: 1
- Claims whose confidence decreased: 0
- Claims whose status changed: 0
- Searches allocated to general research: 1
- Searches allocated to subquestions: 1
- Searches allocated to counter-search: 1
