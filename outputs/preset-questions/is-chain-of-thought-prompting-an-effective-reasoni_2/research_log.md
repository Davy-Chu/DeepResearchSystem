# Research Run Log

## Run Summary

**System Version:** evidence-ledger-v1

**Research Question**

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 10

**OpenAI Calls:** 6

**Tavily Calls:** 3

**Started:** 2026-08-31T17:30:40-04:00

**Ended:** 2026-08-31T17:31:58-04:00

**Total Runtime:** 77.41s

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
- **S3 — 🧠What is LLM Chain of Thought Prompting? | by Tahir**
  URL: https://medium.com/@tahirbalarabe2/what-is-llm-chain-of-thought-prompting-1d4b57a4dd22
- **S4 — What is Chain of Thought (CoT) Prompting?**
  URL: https://www.nvidia.com/en-us/glossary/cot-prompting
- **S5 — What is chain of thought (CoT) prompting? - IBM**
  URL: https://www.ibm.com/think/topics/chain-of-thoughts

**Search Duration:** 2.73s

---

## 2. Evidence Processing

- New claim proposals: 5
- Existing claim updates: 0
- New gaps: 3
- Resolved gaps: 0

**Processing Duration:** 17.65s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

Chain-of-thought prompting is not uniformly effective; its impact varies with model type, task, and evaluation criterion.

- S2 supports (direct): A 2025 GPQA Diamond study reports that CoT effects differ across non-reasoning and reasoning models, and that average-accuracy, perfect-accuracy, and majority-performance metrics can yield different conclusions.
- S1 supports (indirect): The Hi-CoT paper reports that reasoning-prompting outcomes vary across model configurations and benchmark difficulty, while claiming improvements from a particular structured variant.
- S3 contradicts (indirect): The explainer presents CoT as broadly useful for complex reasoning and claims improved accuracy across math, common-sense, and causal tasks without reporting comparative study details.
- S4 contradicts (indirect): NVIDIA’s explainer characterizes CoT as substantially improving accuracy and reliability on complex reasoning tasks in general terms.
- S5 contradicts (indirect): IBM’s explainer describes CoT as enhancing LLM outputs and significantly aiding multistep problem solving in general terms.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C2

**Claim**

For the tested non-reasoning models, generic CoT tends to improve average performance on difficult GPQA Diamond questions, but it can increase answer variability and reduce perfect-accuracy performance for some models.

- S2 supports (direct): The report describes average gains for non-reasoning models, including 13.5% for Gemini Flash 2.0 and 11.7% for Sonnet 3.5, while reporting mixed perfect-accuracy effects and a particularly large decline for Gemini Pro 1.5.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C3

**Claim**

For the tested reasoning models, a generic request to think step by step produces only marginal accuracy changes while increasing response time, suggesting diminishing incremental value when reasoning is already built into the model.

- S2 supports (direct): On GPQA Diamond, the report gives small average changes for o3-mini and o4-mini, a decline for Gemini Flash 2.5, and 20–80% longer response times for CoT requests.
- S4 contradicts (indirect): NVIDIA’s explainer presents longer internal reasoning or test-time compute as generally improving answers, without distinguishing generic prompting from models with built-in reasoning.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C4

**Claim**

Some apparent CoT benefits may reflect elicitation of a response format or reasoning-like behavior rather than a reliably improved underlying solution process; however, the supplied sources do not directly establish this causal distinction.

- S1 supports (indirect): The Hi-CoT paper states that a cited 2025 study found CoT exemplars primarily enforce output format in modern LLMs, and it frames hierarchical structure and compression bottlenecks as performance-relevant.
- S2 supports (indirect): The report notes that many models produce CoT-like reasoning by default and that different simple CoT prompt variants had negligible effects, which is consistent with prompt-format and baseline-behavior effects being important.
- S3 contradicts (indirect): The explainer attributes improved accuracy to breaking problems into smaller sequential reasoning steps.
- S4 contradicts (indirect): The explainer attributes gains to structured intermediate reasoning, error reduction, and improved problem solving.
- S5 contradicts (indirect): The explainer claims that generating intermediate steps enhances multistep problem-solving accuracy.

**Confidence:** LOW

**Status:** INSUFFICIENT_EVIDENCE

### New Claim C5

**Claim**

Imposing additional structure on a reasoning trace can improve both accuracy and efficiency relative to flat CoT in at least the Hi-CoT evaluation, although this does not demonstrate that generic CoT itself improves latent reasoning.

- S1 supports (direct): The Hi-CoT paper reports a 6.2% average accuracy improvement and a 13.9% reduction in reasoning-trace length relative to CoT across 13 model configurations and five mathematical benchmarks; it also reports larger gains on some model-task combinations.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Gap G1

Direct controlled evidence is needed to determine whether CoT accuracy gains arise from improved problem solving, output-format compliance, or both. The supplied sources do not provide a clear ablation that holds formatting constant while measuring solution quality.

### New Gap G2

The evidence does not establish how CoT effects vary across a broad range of task types, model sizes, prompting variants, and evaluation protocols beyond the reported GPQA and mathematical-benchmark results.

### New Gap G3

The supplied sources do not permit a strong assessment of the reliability, statistical robustness, or independent replication of the reported findings, particularly for the Hi-CoT results and the formatting interpretation.

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

**Origin:** RESEARCH_CONTROLLER

**Target:** GAP G1

**Why**

The central causal fault line—better reasoning versus output-format compliance—remains weakly supported and materially determines the answer.

**Next Search**

> controlled studies chain-of-thought output format versus reasoning ability ablation format-matched prompts solution accuracy latent reasoning LLMs


---

# Iteration 2

## 1. Search

**Query**

> controlled studies chain-of-thought output format versus reasoning ability ablation format-matched prompts solution accuracy latent reasoning LLMs

**Target:** G1

**Purpose:** GENERAL

**Why this query**

The central causal fault line—better reasoning versus output-format compliance—remains weakly supported and materially determines the answer.

5 result(s) retrieved; 3 new unique source(s) added.

- **S6 — Latent Reasoning in LLMs**
  URL: https://www.emergentmind.com/topics/latent-reasoning-in-large-language-models
- **S7 — Worries about latent reasoning in LLMs — EA Forum**
  URL: https://forum.effectivealtruism.org/posts/sNkua636jSni6Jftt/worries-about-latent-reasoning-in-llms
- **S8 — Latent Chain-of-Thought as Planning: Decoupling Reasoning from Verbalization**
  URL: https://arxiv.org/html/2601.21358v1

**Search Duration:** 3.17s

---

## 2. Evidence Processing

- New claim proposals: 2
- Existing claim updates: 3
- New gaps: 1
- Resolved gaps: 0

**Processing Duration:** 15.10s

---

## 3. Ledger Updates

### New Claim C6

**Claim**

Latent-reasoning approaches provide evidence that reasoning and verbalization can be partially decoupled, but their reported benefits are task-dependent and involve trade-offs between efficiency, accuracy, interpretability, and exploration.

- S7 supports (direct): The discussion of COCONUT reports substantially fewer forward passes than CoT across tested benchmarks, but an 8-point accuracy drop on GSM8k alongside higher accuracy on two logical-reasoning benchmarks.
- S8 supports (direct): PLaT reports lower greedy accuracy than baselines but stronger Pass@k scaling and reasoning diversity, explicitly identifying a trade-off between greedy precision and exploration potential.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C7

**Claim**

Explicit token-level CoT can constrain search by committing to a discrete reasoning path, whereas latent methods may preserve or explore multiple candidate reasoning paths; this is a proposed mechanism rather than established evidence that generic CoT mainly improves formatting.

- S7 supports (direct): The COCONUT account describes continuous thoughts as supporting breadth-first exploration and reports advantages on logical tasks requiring backtracking, while contrasting this with deterministic CoT paths.
- S8 supports (direct): PLaT frames discrete-token reasoning as vulnerable to reasoning-path collapse and reports greater solution-space diversity under search-based inference.
- S3 contradicts (indirect): The explainer attributes CoT gains to decomposing problems into sequential intermediate steps, which is compatible with explicit reasoning being computationally useful rather than merely formatting.
- S4 contradicts (indirect): The explainer attributes gains to structured intermediate reasoning and error reduction, without testing the proposed path-collapse mechanism.
- S5 contradicts (indirect): The explainer claims that intermediate steps improve multistep problem solving, but provides no direct comparison with latent alternatives.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

Chain-of-thought prompting is not uniformly effective; its impact varies with model type, task, and evaluation criterion.

- S7 supports (direct): COCONUT shows different outcomes across GSM8k and two logical benchmarks, including an efficiency gain with mixed accuracy effects.
- S8 supports (direct): PLaT reports lower greedy accuracy but stronger Pass@k scaling and diversity, adding evidence that evaluation criterion changes the apparent effectiveness of a reasoning strategy.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

Some apparent CoT benefits may reflect elicitation of a response format or reasoning-like behavior rather than a reliably improved underlying solution process; however, the supplied sources do not directly establish this causal distinction.

- S7 supports (direct): COCOT demonstrates that a model can be trained to reason in continuous hidden states and then produce an answer without an explicit CoT, while reporting efficiency and task-dependent accuracy effects.
- S8 supports (direct): PLaT explicitly separates a latent Planner from a Decoder, treating language as a grounding or verbalization interface and reporting latent-state reasoning behavior distinct from text generation.

**Confidence:** LOW → MEDIUM

**Status:** INSUFFICIENT_EVIDENCE → SUPPORTED

### Updated Claim C5

**Claim**

Imposing additional structure on a reasoning trace can improve both accuracy and efficiency relative to flat CoT in at least the Hi-CoT evaluation, although this does not demonstrate that generic CoT itself improves latent reasoning.

- S7 supports (direct): COCOT reports fewer forward passes than explicit CoT on its tested benchmarks, showing that a structured alternative to token-level traces can improve efficiency, though accuracy is mixed.
- S8 supports (direct): PLaT reports reduced diversity saturation and stronger Pass@k scaling under search-based inference, while separating latent planning from verbalization.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### New Gap G4

The new latent-reasoning results do not provide a controlled, apples-to-apples comparison with generic CoT prompting across matched models, training data, inference compute, and output requirements; therefore they cannot determine whether latent or explicit reasoning is intrinsically superior.

---

## 4. Current Research State

- Claims: 7
- Supported: 7
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 4
- Remaining Searches: 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** GAP G1

**Why**

High-value gap G1 remains unresolved: direct evidence separating genuine reasoning gains from formatting or compliance effects is central to the question.

**Next Search**

> controlled ablation chain-of-thought reasoning versus formatting output-format matched prompts accuracy solution process faithfulness LLM study


---

# Iteration 3

## 1. Search

**Query**

> controlled ablation chain-of-thought reasoning versus formatting output-format matched prompts accuracy solution process faithfulness LLM study

**Target:** G1

**Purpose:** GENERAL

**Why this query**

High-value gap G1 remains unresolved: direct evidence separating genuine reasoning gains from formatting or compliance effects is central to the question.

5 result(s) retrieved; 2 new unique source(s) added.

- **S9 — What is faithful chain-of-thought reasoning and why is it ...**
  URL: https://blog.bluedot.org/p/faithful-chain-of-thought
- **S10 — How Chain of Thought (CoT) Prompting Helps LLMs ...**
  URL: https://www.splunk.com/en_us/blog/learn/chain-of-thought-cot-prompting.html

**Search Duration:** 2.40s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 2
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 10.45s

---

## 3. Ledger Updates

### New Claim C8

**Claim**

Natural-language CoT is not necessarily a faithful record of the process that produced an answer; reported studies find that models can provide plausible rationalizations whose content does not reliably determine the final answer, with unfaithfulness reportedly increasing with model size.

- S9 supports (direct): The source reports studies in which editing model-generated CoTs often left final answers largely unchanged and states that CoTs are frequently unfaithful, with greater unfaithfulness as model size increases.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

Chain-of-thought prompting is not uniformly effective; its impact varies with model type, task, and evaluation criterion.

- S9 supports (indirect): The source describes heterogeneous outcomes and limitations: CoT may aid difficult tasks, but faithfulness concerns and reports that faithfulness techniques can reduce accuracy complicate broad claims of effectiveness.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

Some apparent CoT benefits may reflect elicitation of a response format or reasoning-like behavior rather than a reliably improved underlying solution process; however, the supplied sources do not directly establish this causal distinction.

- S9 supports (direct): The source reports that CoT can be an unfaithful after-the-fact rationalization and that faithful-CoT methods have limited usefulness and may reduce accuracy, directly strengthening the distinction between visible reasoning format and underlying solution process.
- S10 supports (indirect): The explainer presents CoT as an instructional sequence of examples and intermediate steps that guides the format and context of the response, supporting the possibility that elicitation and formatting contribute to observed effects.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 8
- Supported: 8
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 4
- Remaining Searches: 0

---

## 5. Research Decision

**Decision:** Stop researching.

**Origin:** BUDGET_STOP

**Why**

The maximum research iteration budget was reached.

**Stop Reason:** max_iterations


---

# Final Research Decision

**Stop Reason:** max_iterations

**Remaining Uncertainty**

- A controlled ablation holding output formatting constant while measuring solution quality is needed to determine whether CoT gains arise from improved problem solving, formatting compliance, or both.
- The supplied evidence does not establish how effects vary across a broad range of task types, model sizes, prompting variants, and evaluation protocols beyond the reported evaluations.
- The reliability, statistical robustness, and independent replication of the reported findings—particularly the Hi-CoT results and the formatting interpretation—remain unclear.
- There is no matched comparison of latent and explicit reasoning under equivalent models, training data, inference compute, and output requirements.
- The research process stopped because the maximum iteration limit was reached; no separate material counter-search was recorded as blocked by duplication, budget, or a one-search limit.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 8.30s |
| Evidence Processing | 3 | 43.21s |
| Research Decision | 2 | 5.47s |
| Report Generation | 1 | 20.43s |
| Total Run | — | 77.41s |
