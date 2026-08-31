# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

**Status:** Completed

**Stop Reason:** sufficient_evidence

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 10

**OpenAI Calls:** 4

**Tavily Calls:** 3

**Started:** 2026-08-31T16:56:31-04:00

**Ended:** 2026-08-31T16:57:52-04:00

**Total Runtime:** 81.45s

---

# Iteration 1

## 1. Search

**Query**

> Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

**Why this query**

This is the user's original research question.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S1 — Hierarchical Chain-of-Thought Prompting: Enhancing LLM Reasoning Performance and Efficiency**
  URL: https://arxiv.org/html/2604.00130v1
- **S2 — Medium**
  URL: https://medium.com/@tahirbalarabe2/what-is-llm-chain-of-thought-prompting-1d4b57a4dd22
- **S3 — Technical Report: The Decreasing Value of Chain of Thought in Prompting - Wharton Generative AI Labs**
  URL: https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought
- **S4 — What is chain of thought (CoT) prompting? - IBM**
  URL: https://www.ibm.com/think/topics/chain-of-thoughts
- **S5 — What is Chain of Thought (CoT) Prompting? | NVIDIA Glossary**
  URL: https://www.nvidia.com/en-us/glossary/cot-prompting

**Search Duration:** 2.94s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The retrieved evidence supports a conditional, not universal, answer: CoT can improve performance on difficult multi-step reasoning tasks, but its benefit depends strongly on model type, task, and prompting/evaluation design.

**Confidence:** Medium

**Why this confidence level**

The conditional pattern is directly reported by a controlled study, but the retrieved set contains only one substantial empirical comparison and several non-primary explainers.

**Evidence**

- The Wharton study reports model- and task-dependent effects: non-reasoning models had modest average gains, while reasoning models showed marginal gains; it concludes that CoT is not universally optimal. [S3]
- IBM and NVIDIA describe CoT as particularly useful for multi-step arithmetic, mathematical, symbolic, commonsense, and planning tasks, but these are explanatory sources rather than controlled comparative studies. [S4] [S5]

#### Finding 2

**Claim**

For contemporary models with built-in reasoning, a generic 'think step by step' instruction may add little reasoning capability while imposing substantial latency and token costs.

**Confidence:** Medium

**Why this confidence level**

The result is based on one reported benchmark and a limited model sample, but the cost and model-type distinction are directly measured in that study.

**Evidence**

- On GPQA Diamond, the Wharton report found only small average changes for o3-mini and o4-mini and a decline for Gemini Flash 2.5; CoT increased response time by roughly 20–80% for reasoning models. [S3]
- The report also says many models produce CoT-like reasoning by default without an explicit CoT instruction, making an added generic instruction redundant. [S3]

#### Finding 3

**Claim**

For non-reasoning models, CoT can improve average accuracy but can also increase output variability and harm performance on questions that direct answering would have gotten right.

**Confidence:** Medium

**Why this confidence level**

The evidence directly addresses both accuracy and consistency, but the retrieved content does not provide full tables, significance tests, or replication.

**Evidence**

- The Wharton report found average gains for several non-reasoning models, including 13.5% for Gemini Flash 2.0 and 11.7% for Sonnet 3.5, but mixed effects under a perfect-accuracy criterion; Gemini Pro 1.5 reportedly declined by 17.2%. [S3]
- The same study reports that CoT requests took 35–600% longer for non-reasoning models and increased variability. [S3]

#### Finding 4

**Claim**

One important fault line is whether intermediate reasoning changes the underlying solution process or mainly acts as a learned response format. The retrieved material explicitly reports this dispute but does not resolve it experimentally.

**Confidence:** Low

**Why this confidence level**

The formatting claim is only indirectly represented through S1’s citation to another work, while the opposing claims come from general explainers rather than independent experiments.

**Evidence**

- The Hi-CoT paper states that Cheng et al. (2025) found that CoT exemplars primarily enforce output format rather than improve reasoning quality in modern LLMs. [S1]
- In contrast, IBM and NVIDIA present CoT as improving reasoning by decomposition, maintaining context, and reducing errors, though neither source supplies a controlled causal test separating reasoning from formatting. [S4] [S5]

#### Finding 5

**Claim**

Structure may matter more than merely requesting a longer verbal chain: hierarchical planning and execution are reported to outperform flat CoT while using shorter traces, suggesting that organization, compression, and control can be causal factors in some settings.

**Confidence:** Low

**Why this confidence level**

The reported results are broad within that study but come from a very recent single preprint, mathematics-focused evaluation, and no independently retrieved replication.

**Evidence**

- Hi-CoT reports a 6.2% average accuracy improvement and a 13.9% reduction in reasoning-trace length relative to CoT across 13 model configurations and five mathematical benchmarks; it attributes the effect to adaptive planning, execution grounding, and compression bottlenecks. [S1]

### Conflicts Found

- The sources disagree about the mechanism: S4 and S5 characterize CoT as genuine stepwise reasoning that improves accuracy and error detection, whereas S1 reports that modern CoT exemplars may primarily enforce output format, citing Cheng et al. (2025). This is a mechanistic disagreement, not necessarily a contradiction in observed accuracy gains: formatting can improve task compliance even when it does not add reasoning. [S1] [S4] [S5]
- The claim that CoT broadly improves accuracy conflicts with the Wharton results showing small or negative effects for some models and metrics, especially built-in reasoning models and perfect-accuracy thresholds. The disagreement is conditional on model family, task difficulty, and evaluation metric. [S3] [S4] [S5]
- S1 presents structured CoT as improving accuracy while shortening traces, whereas S3 finds generic CoT often costly and marginal for reasoning models. These findings may differ because Hi-CoT changes the reasoning structure rather than simply adding a generic step-by-step instruction, and because the studies use different benchmarks and models. [S1] [S3]

### Important Gaps

- Do CoT prompts improve latent problem-solving ability, or do they mainly improve answer formatting, decomposition, and compliance? The retrieved set lacks a direct controlled comparison that holds output format constant while testing hidden versus visible reasoning.
- How much of the classic CoT effect is due to few-shot exemplars and learned answer formats versus the instruction to generate intermediate steps?
- Are the reported effects robust across non-mathematical tasks, open-ended tasks, and harder or adversarial examples rather than mainly benchmark-style questions?
- How do prompt wording, demonstration correctness, trace visibility, answer extraction, majority voting, and repeated-trial aggregation affect the measured benefit?
- Does structured CoT reliably outperform generic CoT after accounting for additional prompt tokens, implementation complexity, and model-specific reasoning defaults?
- The Wharton summary reports aggregate percentages but the retrieved content does not expose complete per-question results, confidence intervals, statistical tests, or all benchmark conditions.

**Analysis Duration:** 19.49s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

A further search would materially improve the answer because the central formatting-versus-reasoning fault line is supported only indirectly, and the current evidence lacks the primary study behind that claim. A targeted search should retrieve the controlled modern-LM study and compare its methodology with the Wharton experiment and original CoT work.

**Next Search**

> Cheng 2025 chain-of-thought exemplars primarily output format rather than reasoning quality paper

---

# Iteration 2

## 1. Search

**Query**

> Cheng 2025 chain-of-thought exemplars primarily output format rather than reasoning quality paper

**Why this query**

A further search would materially improve the answer because the central formatting-versus-reasoning fault line is supported only indirectly, and the current evidence lacks the primary study behind that claim. A targeted search should retrieve the controlled modern-LM study and compare its methodology with the Wharton experiment and original CoT work.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S6 — Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot**
  URL: https://arxiv.org/html/2506.14641v3
- **S7 — Chain of Thought Prompting Guide - PromptHub**
  URL: https://www.prompthub.us/blog/chain-of-thought-prompting-guide
- **S8 — [PDF] Structured Chain-of-Thought Prompting for Code Generation**
  URL: https://ligechina.github.io/My%20Papers/2025%20-%20TOSEM%20-%20Structured%20Chain-of-Thought%20Prompting%20for%20Code%20Generation.pdf

**Search Duration:** 2.06s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Recent strong models may receive little or no reasoning benefit from few-shot CoT exemplars beyond zero-shot CoT; the exemplars’ main measurable function can be output-format alignment.

**Confidence:** Medium

**Why this confidence level**

S6 directly studies the relevant comparison on two mathematical benchmarks and multiple recent open-source models, but it is a single recent preprint and its conclusions are limited primarily to mathematical reasoning.

**Evidence**

- Across GSM8K and MATH experiments, S6 reports that traditional CoT exemplars did not improve recent strong models over zero-shot CoT, and concludes that their primary function was aligning outputs with human-expected reasoning formats. [S6]

#### Finding 2

**Claim**

The apparent CoT advantage is strongly dependent on model capability: weaker or non-reasoning models can benefit, whereas stronger models may already possess the relevant reasoning behavior or may ignore demonstrations.

**Confidence:** Medium

**Why this confidence level**

The same conditional pattern appears in two sources, but the model samples, tasks, and evaluation protocols differ, and S6 is not yet independently replicated in the retrieved material.

**Evidence**

- S6 states that traditional CoT exemplars may benefit weaker models but do not enhance strong models; enhanced exemplars generated by Qwen2.5-Max and DeepSeek-R1 also failed to improve strong models, which tended to ignore exemplar content. [S6]
- The prior Wharton study found average gains for several non-reasoning models but marginal or negative effects for some built-in reasoning models. [S3]

#### Finding 3

**Claim**

Few-shot CoT and zero-shot CoT should not be treated as the same intervention. A strong zero-shot instruction may already elicit the model’s reasoning capability, making added demonstrations redundant or primarily stylistic.

**Confidence:** Medium

**Why this confidence level**

Both sources directly support redundancy in strong or reasoning-oriented models, although they examine different prompting variants and benchmarks.

**Evidence**

- S6 reports that, after correcting an evaluation bias in GSM8K, recent models performed strongly with zero-shot CoT and that adding traditional CoT exemplars produced no observable reasoning gain. [S6]
- The prior evidence reports that many contemporary reasoning models generate CoT-like traces by default, so an added generic step-by-step instruction can be redundant while increasing latency. [S3]

#### Finding 4

**Claim**

A major fault line is whether CoT changes problem solving or mainly changes the model’s response distribution and format. The new evidence strengthens the formatting interpretation for CoT exemplars but does not establish that all CoT prompting is merely formatting.

**Confidence:** Medium

**Why this confidence level**

The evidence supports a conditional mechanism rather than a single universal one, but the retrieved studies do not hold answer format, trace visibility, and decoding conditions constant to isolate latent reasoning.

**Evidence**

- S6 explicitly concludes that CoT exemplars primarily align output format and reports that models often focus on the instruction while ignoring exemplar content. [S6]
- S3 shows that CoT can change accuracy for non-reasoning models, including substantial average gains, which is consistent with an ability to elicit or organize reasoning rather than formatting alone. [S3]
- PromptHub describes decomposition and error reduction as benefits, but also acknowledges that generated chains are not always faithful; this is explanatory rather than controlled causal evidence. [S7]

#### Finding 5

**Claim**

The useful ingredient may be structured intermediate representations rather than verbosity or the generic instruction to think step by step.

**Confidence:** Medium

**Why this confidence level**

Two task-specific studies point in the same direction, but both modify the reasoning representation substantially and do not prove that the gains generalize to ordinary CoT or non-mathematical/non-code tasks.

**Evidence**

- S8 reports that Structured CoT, which represents sequential, branch, and loop structures, outperformed ordinary CoT by up to 13.79% Pass@1 across code-generation benchmarks and models. [S8]
- S1 similarly reports that hierarchical CoT improved accuracy while shortening traces, attributing the result to planning, execution grounding, and compression rather than simply longer verbal chains. [S1]

#### Finding 6

**Claim**

Conflicting results are plausibly accounted for by differences in model capability, prompting intervention, task structure, evaluation, and cost accounting—not necessarily by a simple contradiction over whether CoT works.

**Confidence:** High

**Why this confidence level**

The conditional sources directly identify several independent moderators—model family, evaluation procedure, task, and representation—providing a coherent explanation for divergent headline findings.

**Evidence**

- S3 varies effects by reasoning versus non-reasoning model, benchmark outcome criterion, and response cost; it reports both gains and declines. [S3]
- S6 identifies evaluation bias in GSM8K frameworks that underestimates zero-shot CoT, potentially making few-shot CoT appear more useful than it is. [S6]
- S8 finds only slight gains from ordinary CoT in code generation but larger gains from a task-aligned structured variant, indicating that task representation matters. [S8]

### Conflicts Found

- S6 says CoT exemplars primarily align output format and do not improve reasoning in recent strong mathematical models, while S3 reports accuracy gains from CoT for several non-reasoning models. This is a conditional disagreement by model capability and possibly task/evaluation, not a direct contradiction. [S6] [S3]
- S6 reports that strong models often ignore even enhanced exemplars, whereas conventional accounts describe exemplars as teaching a reasoning procedure. The disagreement concerns whether exemplars transmit useful reasoning content or merely establish a response format in strong models. [S6] [S7]
- S8 and S1 report meaningful gains from structured or hierarchical reasoning, while S3 finds generic CoT marginal and costly for reasoning models. The results may be reconciled because structured methods change the representation and control of reasoning rather than merely adding a generic step-by-step request. [S8] [S1] [S3]

### Important Gaps

- Does CoT improve hidden problem-solving ability when answer format, output length, trace visibility, and decoding procedure are held constant?
- How much of the classic few-shot CoT effect came from older/weaker models, exemplar-induced formatting, and evaluation pipelines that disadvantaged zero-shot CoT?
- Are S6’s findings robust outside GSM8K and MATH, especially on non-mathematical, adversarial, open-ended, and program-synthesis tasks?
- When structured CoT improves performance, is the causal factor planning, an intermediate representation closer to the target language, improved error checking, or simply better prompt engineering?
- How should CoT be evaluated when it increases latency, token use, and output variability, rather than accuracy alone?

**Analysis Duration:** 20.39s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The current evidence supports a responsible conditional answer and explains most conflicting results, but the central mechanistic question remains unresolved: no retrieved source cleanly separates genuine reasoning improvement from formatting, compliance, or answer-extraction effects under controlled output conditions. A targeted search for causal evaluations would materially strengthen the conclusion.

**Next Search**

> causal evaluation chain-of-thought prompting formatting versus reasoning hidden reasoning output format controlled experiment

---

# Iteration 3

## 1. Search

**Query**

> causal evaluation chain-of-thought prompting formatting versus reasoning hidden reasoning output format controlled experiment

**Why this query**

The current evidence supports a responsible conditional answer and explains most conflicting results, but the central mechanistic question remains unresolved: no retrieved source cleanly separates genuine reasoning improvement from formatting, compliance, or answer-extraction effects under controlled output conditions. A targeted search for causal evaluations would materially strengthen the conclusion.

**Results**

5 results retrieved.

2 new unique sources added.

### Sources

- **S9 — Chain-of-Thought (CoT) Prompting**
  URL: https://www.promptingguide.ai/techniques/cot
- **S10 — Master Prompting Concepts: Chain of Thought Prompting**
  URL: https://promptengineering.org/master-prompting-concepts-chain-of-thought-prompting

**Search Duration:** 3.27s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources reinforce the original, classical account that CoT can improve performance on multi-step problems by eliciting intermediate steps, but they do not provide new controlled evidence about whether this reflects genuine reasoning or output formatting.

**Confidence:** Low

**Why this confidence level**

Both sources are instructional explainers that reproduce or summarize established examples rather than reporting new experiments, controls, replications, or causal analyses.

**Evidence**

- S9 presents few-shot and zero-shot examples in which explicitly generated intermediate steps produce correct arithmetic answers where direct prompting allegedly fails. [S9]
- S10 similarly describes CoT as breaking problems into intermediate steps and gives arithmetic examples with correct final answers after step-by-step prompting. [S10]

#### Finding 2

**Claim**

The sources distinguish few-shot CoT from zero-shot CoT: few-shot prompting supplies worked rationales, while zero-shot CoT uses a generic instruction such as 'Let's think step by step.'

**Confidence:** Medium

**Why this confidence level**

The distinction is directly stated in both sources, although they are secondary explanatory pages.

**Evidence**

- S9 separately describes few-shot demonstrations and zero-shot CoT, including the generic step-by-step instruction and an arithmetic example. [S9]
- S10 likewise contrasts standard/few-shot prompting with intermediate-step demonstrations and describes zero-shot CoT as adding 'Let's think step by step.' [S10]

#### Finding 3

**Claim**

The apparent benefit of CoT can plausibly arise from task decomposition and answer-format elicitation, but the new sources cannot determine how much each mechanism contributes.

**Confidence:** High

**Why this confidence level**

The inability of these examples to separate mechanisms is clear from their design, and it is consistent with the prior evidence’s conditional findings.

**Evidence**

- The examples explicitly change both the requested process—producing intermediate calculations—and the response format, so their improved final answers do not isolate latent reasoning from formatting or compliance effects. [S9] [S10]
- The accumulated empirical evidence already reports that CoT exemplars can primarily align output format in strong models, while generic CoT can improve some non-reasoning models and structured representations can provide additional gains. [S6] [S3] [S1] [S8]

#### Finding 4

**Claim**

The new sources do not materially alter the main explanation for conflicting CoT results: outcomes vary with model capability, intervention type, task structure, evaluation procedure, and cost/consistency criteria.

**Confidence:** High

**Why this confidence level**

The new sources are narrow and non-comparative, while the accumulated evidence directly identifies the moderators that reconcile apparently conflicting findings.

**Evidence**

- S9 and S10 mainly present favorable arithmetic demonstrations and do not test built-in reasoning models, negative effects, latency, variability, or alternative evaluation criteria. [S9] [S10]
- The accumulated controlled and task-specific evidence reports gains for some non-reasoning models, marginal or negative effects for some reasoning models, possible formatting-only effects of exemplars, and benefits from structured rather than merely verbose reasoning. [S3] [S6] [S1] [S8]

### Conflicts Found

No meaningful conflicts were identified in this iteration.

### Important Gaps

- Whether CoT improves hidden problem-solving ability when answer format, output length, trace visibility, and decoding are held constant remains unresolved.
- The new sources do not test whether their favorable arithmetic examples generalize to non-mathematical, open-ended, adversarial, or out-of-distribution tasks.
- It remains unclear whether gains from structured or hierarchical CoT are caused by planning, intermediate representations, error checking, or prompt-specific formatting.

**Analysis Duration:** 11.33s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The new material consists of secondary instructional explainers that repeat canonical examples and add no controlled evidence addressing the central mechanism dispute. The accumulated research state already supports a responsible conditional conclusion: CoT is effective in some model-task-prompt regimes, while few-shot exemplars may chiefly impose a useful output format for strong modern models. Another search would be useful only for a direct causal study holding formatting and reasoning visibility constant, but the present sources do not identify one and further generic CoT explainers would not materially improve the answer.

**Stop Reason:** sufficient_evidence

---

# Final Research Decision

**Research Stopped Because**

The analyzer determined that the important parts of the question could be answered responsibly.

**Stop Reason:** sufficient_evidence

**Searches Performed:** 3

**Unique Sources:** 10

**Remaining Uncertainty**

- A controlled causal comparison holding output format, response length, trace visibility, and decoding conditions constant.
- Independent replication of the reported formatting-only effect of CoT exemplars.
- Systematic separation of zero-shot instructions, few-shot rationales, structured representations, and built-in model reasoning.
- Evaluation across non-mathematical, open-ended, adversarial, and out-of-distribution tasks.
- A common evaluation framework that jointly reports accuracy, consistency, latency, token usage, and cost.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 8.26s |
| OpenAI Analysis | 3 | 51.20s |
| Report Generation | 1 | 21.99s |
| Total Run | — | 81.45s |
