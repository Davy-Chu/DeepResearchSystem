# Research Run Log

## Run Summary

**System Version:** evidence-ledger-v1

**Research Question**

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees-find the real fault lines and explain what accounts for the conflicting results.

**Status:** Failed

**Stop Reason:** max_iterations

**Failure Stage:** OpenAI Ledger Report Generation

**Error**

Ledger report finding 5 cites source ID(s) not attached to its ledger claims: S3

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 10

**OpenAI Calls:** 5

**Tavily Calls:** 3

**Started:** 2026-08-30T18:19:49-04:00

**Ended:** 2026-08-30T18:21:07-04:00

**Total Runtime:** 78.07s

---

# Iteration 1

## 1. Search

**Query**

> Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees-find the real fault lines and explain what accounts for the conflicting results.

**Why this query**

This is the user's original research question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S1 — Hierarchical Chain-of-Thought Prompting: Enhancing LLM ...**
  URL: https://arxiv.org/html/2604.00130v1
- **S2 — Chain-Of-Thought Prompting In LLMs | by Cobus Greyling | Medium**
  URL: https://cobusgreyling.medium.com/chain-of-thought-prompting-in-llms-1077164edf97
- **S3 — The Decreasing Value of Chain of Thought in Prompting**
  URL: https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought
- **S4 — Contrastive Chain-Of-Thought Prompting - Kore.ai**
  URL: https://www.kore.ai/blog/contrastive-chain-of-thought-prompting
- **S5 — What is chain of thought (CoT) prompting?**
  URL: https://www.ibm.com/think/topics/chain-of-thoughts

**Search Duration:** 0.60s

---

## 2. Evidence Processing

- New claim proposals: 5
- Existing claim updates: 0
- New gaps: 3
- Resolved gaps: 0

**Processing Duration:** 15.14s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

The effectiveness of generic chain-of-thought prompting is conditional rather than universal: in one reported GPQA Diamond study, it produced modest average gains for several non-reasoning models, but gains were mixed across accuracy thresholds and could increase answer variability.

- S3 supports (direct): The report found average improvements for non-reasoning models ranging from 4.4% to 13.5%, while perfect-accuracy results were mixed and some models declined; it also reported increased variability.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C2

**Claim**

For models with built-in reasoning capabilities, a generic instruction to think step by step may provide little additional accuracy and can impose substantial latency or token costs.

- S3 supports (direct): On the tested reasoning models, average gains were small for o3-mini and o4-mini, performance decreased for Gemini Flash 2.5, and CoT increased response time by 20–80%.
- S5 contradicts (indirect): IBM’s overview presents CoT as enhancing complex multistep reasoning generally, but it does not isolate built-in reasoning models or provide a controlled evaluation of marginal gains.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C3

**Claim**

Observed CoT gains can depend on the structure of the elicited reasoning process, not merely on requiring a longer verbal trace.

- S1 supports (direct): The Hi-CoT report argues that hierarchical planning and execution improves average accuracy by 6.2% while reducing trace length by 13.9% relative to conventional CoT across reported models and mathematical benchmarks.
- S1 contradicts (direct): The same source states that longer traces do not imply better reasoning and describes redundancy and drift in unstructured CoT, limiting any inference that verbosity itself causes improvement.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C4

**Claim**

CoT-style demonstrations may sometimes function primarily as output-format guidance rather than as a reliable improvement to underlying reasoning quality, especially for modern LLMs; the supplied evidence does not establish this claim conclusively.

- S1 supports (indirect): In its related-work discussion, the source attributes to Cheng et al. (2025) the finding that CoT exemplars primarily enforce output format for modern LLMs.
- S2 contradicts (indirect): The article characterizes CoT as enabling decomposition and significantly improving complex-task performance, but provides no controlled separation of reasoning gains from formatting effects.
- S5 contradicts (indirect): IBM describes intermediate steps as enhancing multistep problem solving and accuracy, but its supplied content is explanatory rather than a direct test of formatting versus reasoning.

**Confidence:** LOW

**Status:** INSUFFICIENT_EVIDENCE

### New Claim C5

**Claim**

Benchmarking choices and evaluation thresholds can materially change the apparent effect of CoT.

- S3 supports (direct): The study tested each question 25 times and reported separate complete-accuracy, high-accuracy, majority-correct, and average-rating metrics; effects differed across these metrics.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Gap G1

Direct, controlled evidence is needed to distinguish genuine improvements in problem solving from gains caused by output formatting, answer extraction, or compliance with requested response structure.

### New Gap G2

It remains unclear which task properties, model training characteristics, and CoT variants determine whether generic CoT helps, harms, or has negligible effect.

### New Gap G3

The supplied evidence does not independently verify the cited Cheng et al. finding about CoT exemplars primarily enforcing output format.

---

## 4. Current Research State

- Claims: 5
- Supported: 4
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 1
- Open Gaps: 3
- Remaining Searches: 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Target:** GAP G1

**Why**

The central dispute—reasoning gains versus formatting or extraction effects—still rests on indirect evidence. Controlled studies separating these mechanisms would materially improve the answer.

**Next Search**

> controlled study chain-of-thought prompting reasoning gains versus formatting effects answer extraction output format modern language models CoT exemplars Cheng 2025


---

# Iteration 2

## 1. Search

**Query**

> controlled study chain-of-thought prompting reasoning gains versus formatting effects answer extraction output format modern language models CoT exemplars Cheng 2025

**Why this query**

The central dispute—reasoning gains versus formatting or extraction effects—still rests on indirect evidence. Controlled studies separating these mechanisms would materially improve the answer.

5 result(s) retrieved; 2 new unique source(s) added.

- **S6 — Chain-of-Thought Prompting**
  URL: https://learnprompting.org/docs/intermediate/chain_of_thought
- **S7 — Language Models Perform Reasoning via Chain of Thought**
  URL: https://research.google/blog/language-models-perform-reasoning-via-chain-of-thought

**Search Duration:** 2.48s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 4
- New gaps: 2
- Resolved gaps: 0

**Processing Duration:** 16.65s

---

## 3. Ledger Updates

### New Claim C6

**Claim**

The reported early CoT literature identifies model scale as a major moderator: benefits were reported to emerge primarily for models around 100B parameters or larger, while smaller models could show little benefit or worse performance.

- S7 supports (direct): Google Research reports that successful CoT reasoning was an emergent property of scale, with benefits materializing at approximately 100B parameters, and that smaller models did not obtain the same gains on the evaluated reasoning tasks.
- S6 supports (indirect): The guide summarizes the limitation that CoT gains were reported for models of roughly 100B parameters, while smaller models could produce illogical chains and perform worse than with standard prompting.

**Confidence:** HIGH

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

The effectiveness of generic chain-of-thought prompting is conditional rather than universal: in one reported GPQA Diamond study, it produced modest average gains for several non-reasoning models, but gains were mixed across accuracy thresholds and could increase answer variability.

- S7 supports (direct): Google Research reports that CoT benefits are not universal across model scales: gains emerged strongly for sufficiently large models, especially on arithmetic tasks, while smaller models did not show the same improvement.
- S6 supports (indirect): The guide reports that CoT is particularly beneficial for complex tasks and larger models, whereas smaller models may perform worse.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

For models with built-in reasoning capabilities, a generic instruction to think step by step may provide little additional accuracy and can impose substantial latency or token costs.

- S7 contradicts (direct): In the earlier large-model evaluations summarized by Google Research, CoT produced substantial gains over standard prompting on arithmetic and some commonsense tasks, including a reported GSM8K improvement for PaLM 540B.
- S6 contradicts (indirect): The guide reports sizable CoT improvements on GSM8K, SVAMP, commonsense, and symbolic-reasoning benchmarks for PaLM 540B, although it does not evaluate models with built-in reasoning capabilities or latency costs.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

CoT-style demonstrations may sometimes function primarily as output-format guidance rather than as a reliable improvement to underlying reasoning quality, especially for modern LLMs; the supplied evidence does not establish this claim conclusively.

- S7 contradicts (direct): Google Research attributes CoT gains to decomposing multi-step problems into intermediate steps and reports improved performance over standard prompting on several reasoning benchmarks; this favors a reasoning-effect account but does not causally separate it from formatting.
- S6 contradicts (indirect): The guide describes CoT as improving complex-task accuracy through decomposition and reports benchmark gains, but it provides no controlled test distinguishing reasoning from output-format effects.

**Confidence:** LOW → LOW

**Status:** INSUFFICIENT_EVIDENCE → INSUFFICIENT_EVIDENCE

### Updated Claim C5

**Claim**

Benchmarking choices and evaluation thresholds can materially change the apparent effect of CoT.

- S7 supports (direct): Google Research reports that CoT effects vary by task: improvements were substantial on arithmetic reasoning, smaller on several commonsense tasks, and especially large on sports understanding, indicating task-dependent apparent effectiveness.
- S6 supports (indirect): The guide summarizes different reported gains across arithmetic, commonsense, and symbolic-reasoning benchmarks, further indicating that benchmark choice affects the measured effect.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### New Gap G4

It remains unresolved whether the large CoT gains reported in early large-model studies persist for current models with internal or explicitly trained reasoning mechanisms, and how much of any marginal gain is attributable to the prompt versus the model’s capabilities.

### New Gap G5

The supplied sources report scale and task moderators but do not jointly disentangle model scale, task complexity, prompting format, and use of tools such as external calculators as causes of the observed CoT gains.

---

## 4. Current Research State

- Claims: 6
- Supported: 5
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 1
- Open Gaps: 5
- Remaining Searches: 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Target:** GAP G1

**Why**

The central formatting-versus-reasoning fault line remains unresolved, with only indirect support and no controlled evidence separating genuine problem-solving gains from output-format or answer-extraction effects.

**Next Search**

> controlled experiments chain-of-thought reasoning benefit versus answer formatting output structure answer extraction LLMs CoT exemplars modern language models


---

# Iteration 3

## 1. Search

**Query**

> controlled experiments chain-of-thought reasoning benefit versus answer formatting output structure answer extraction LLMs CoT exemplars modern language models

**Why this query**

The central formatting-versus-reasoning fault line remains unresolved, with only indirect support and no controlled evidence separating genuine problem-solving gains from output-format or answer-extraction effects.

5 result(s) retrieved; 3 new unique source(s) added.

- **S8 — What is Chain-of-Thought (CoT) in LLMs?**
  URL: https://www.youtube.com/watch?v=xPly2h-gIcw
- **S9 — Chain-of-Thought (CoT): Prompting & LLM Reasoning Explained**
  URL: https://www.altexsoft.com/blog/chain-of-thought-prompting
- **S10 — What is Chain of Thought (CoT) Prompting?**
  URL: https://www.nvidia.com/en-us/glossary/cot-prompting

**Search Duration:** 2.36s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 4
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 18.96s

---

## 3. Ledger Updates

### New Claim C7

**Claim**

The supplied explanatory sources distinguish externally prompted CoT from internally generated or test-time reasoning in models trained to reason, but they do not provide controlled evidence establishing the relative accuracy or marginal benefit of these approaches.

- S9 supports (direct): The article describes a transition from user-prompted CoT to reasoning models that generate reasoning internally through additional fine-tuning and reinforcement learning.
- S10 supports (direct): NVIDIA distinguishes models that require a user prompt to elicit step-by-step reasoning from test-time-scaling models that initiate and manage reasoning internally.

**Confidence:** HIGH

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

The effectiveness of generic chain-of-thought prompting is conditional rather than universal: in one reported GPQA Diamond study, it produced modest average gains for several non-reasoning models, but gains were mixed across accuracy thresholds and could increase answer variability.

- S8 supports (indirect): The tutorial presents CoT as useful for complex multistep tasks while noting trade-offs such as longer responses, slower inference, and hallucinated reasoning; this is consistent with conditional rather than universal effectiveness.
- S9 supports (indirect): The article differentiates CoT variants by task complexity, describing zero-shot CoT as suited to relatively simple tasks and few-shot or other structured variants as useful for more complex problems.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

For models with built-in reasoning capabilities, a generic instruction to think step by step may provide little additional accuracy and can impose substantial latency or token costs.

- S9 supports (indirect): The article describes reasoning models as using internally generated CoT after additional fine-tuning, implying that user-visible generic prompting is not the only route to eliciting reasoning; it does not directly measure marginal accuracy gains from such prompting.
- S10 supports (indirect): NVIDIA distinguishes ordinary models that need user prompts from test-time-scaling models that self-direct their reasoning, supporting the relevance of built-in reasoning capabilities to the marginal value of generic CoT.
- S8 supports (direct): The tutorial explicitly identifies increased token generation, processing time, cost, and latency as trade-offs of CoT.
- S9 contradicts (indirect): The article claims that internally trained reasoning models can improve accuracy by generating longer chains, exploring multiple paths, or using search-based refinement; this supports reasoning benefits generally but does not test a generic user instruction on such models.
- S10 contradicts (indirect): NVIDIA claims that allowing more internal reasoning steps improves performance on complex tasks, but this concerns automated test-time scaling rather than the marginal effect of generic prompted CoT.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

CoT-style demonstrations may sometimes function primarily as output-format guidance rather than as a reliable improvement to underlying reasoning quality, especially for modern LLMs; the supplied evidence does not establish this claim conclusively.

- S8 contradicts (indirect): The tutorial presents intermediate-step generation as decomposing problems and improving accuracy, while also acknowledging hallucinated reasoning; this favors a possible reasoning effect but does not separate it from formatting or compliance.
- S9 contradicts (indirect): The article attributes CoT benefits to expanded working context, staged processing, and additional computation, and describes reasoning models trained to assess reasoning quality; these claims favor a substantive reasoning account but are not controlled tests of formatting versus reasoning.
- S10 contradicts (indirect): NVIDIA describes CoT as improving decomposition, error reduction, and complex-task performance, and separately discusses hidden thinking tokens in test-time scaling; neither analysis controls for output format or answer extraction.

**Confidence:** LOW → LOW

**Status:** INSUFFICIENT_EVIDENCE → INSUFFICIENT_EVIDENCE

### Updated Claim C5

**Claim**

Benchmarking choices and evaluation thresholds can materially change the apparent effect of CoT.

- S8 supports (indirect): The tutorial identifies arithmetic, logic, and multistep tasks as use cases and separately notes costs and hallucination risks, reinforcing that measured outcomes depend on task and evaluation dimensions.
- S9 supports (direct): The article describes different CoT variants, including zero-shot, few-shot, least-to-most, and self-consistency, with different intended task settings; this indicates that prompting format can affect apparent efficacy.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 7
- Supported: 6
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 1
- Open Gaps: 5
- Remaining Searches: 0

---

## 5. Research Decision

**Decision:** Stop researching.

**Why**

The maximum research iteration budget was reached.

**Stop Reason:** max_iterations


---

# Final Research Decision

**Research did not complete.**

**Failure Stage:** OpenAI Ledger Report Generation

**Remaining Uncertainty**

- Direct, controlled evidence is needed to distinguish genuine improvements in problem solving from gains caused by output formatting, answer extraction, or compliance with requested response structure.
- It remains unclear which task properties, model training characteristics, and CoT variants determine whether generic CoT helps, harms, or has negligible effect.
- The supplied evidence does not independently verify the cited Cheng et al. finding about CoT exemplars primarily enforcing output format.
- It remains unresolved whether the large CoT gains reported in early large-model studies persist for current models with internal or explicitly trained reasoning mechanisms, and how much of any marginal gain is attributable to the prompt versus the model’s capabilities.
- The supplied sources report scale and task moderators but do not jointly disentangle model scale, task complexity, prompting format, and use of tools such as external calculators as causes of the observed CoT gains.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 5.44s |
| Evidence Processing | 3 | 50.75s |
| Research Decision | 2 | 5.88s |
| Report Generation | 0 | 0.00s |
| Total Run | — | 78.07s |
