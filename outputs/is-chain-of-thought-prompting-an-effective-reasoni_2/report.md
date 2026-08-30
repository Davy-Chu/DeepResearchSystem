# Research Report

## Research Question

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees-find the real fault lines and explain what accounts for the conflicting results.

## Summary

This is an automatically generated incomplete report. The research run ended with stop reason `max_iterations`, and normal finalization did not complete during OpenAI Ledger Report Generation. The validated findings collected before that point are preserved below without claiming that the evidence is complete.

## Findings

### Finding 1

**Claim**

The effectiveness of generic chain-of-thought prompting is conditional rather than universal: in one reported GPQA Diamond study, it produced modest average gains for several non-reasoning models, but gains were mixed across accuracy thresholds and could increase answer variability.

**Confidence:** Medium

**Why this confidence level**

The new sources reinforce task and prompting-condition dependence, but they are explanatory sources and do not add controlled results comparable to the GPQA evidence.

**Evidence**

- The report found average improvements for non-reasoning models ranging from 4.4% to 13.5%, while perfect-accuracy results were mixed and some models declined; it also reported increased variability. [S3]
- Google Research reports that CoT benefits are not universal across model scales: gains emerged strongly for sufficiently large models, especially on arithmetic tasks, while smaller models did not show the same improvement. [S7]
- The guide reports that CoT is particularly beneficial for complex tasks and larger models, whereas smaller models may perform worse. [S6]
- The tutorial presents CoT as useful for complex multistep tasks while noting trade-offs such as longer responses, slower inference, and hallucinated reasoning; this is consistent with conditional rather than universal effectiveness. [S8]
- The article differentiates CoT variants by task complexity, describing zero-shot CoT as suited to relatively simple tasks and few-shot or other structured variants as useful for more complex problems. [S9]

### Finding 2

**Claim**

For models with built-in reasoning capabilities, a generic instruction to think step by step may provide little additional accuracy and can impose substantial latency or token costs.

**Confidence:** Medium

**Why this confidence level**

The new sources sharpen the distinction between prompted CoT and internal/test-time reasoning and independently confirm cost trade-offs, but they remain non-controlled explanatory material and do not overturn the direct S3 evidence about limited marginal gains on tested reasoning models.

**Evidence**

- On the tested reasoning models, average gains were small for o3-mini and o4-mini, performance decreased for Gemini Flash 2.5, and CoT increased response time by 20–80%. [S3]
- The article describes reasoning models as using internally generated CoT after additional fine-tuning, implying that user-visible generic prompting is not the only route to eliciting reasoning; it does not directly measure marginal accuracy gains from such prompting. [S9]
- NVIDIA distinguishes ordinary models that need user prompts from test-time-scaling models that self-direct their reasoning, supporting the relevance of built-in reasoning capabilities to the marginal value of generic CoT. [S10]
- The tutorial explicitly identifies increased token generation, processing time, cost, and latency as trade-offs of CoT. [S8]

### Finding 3

**Claim**

Observed CoT gains can depend on the structure of the elicited reasoning process, not merely on requiring a longer verbal trace.

**Confidence:** Medium

**Why this confidence level**

The source directly reports a structured-CoT comparison and explicitly separates trace length from organization, but it is a single reported study and its results concern Hi-CoT rather than generic CoT alone.

**Evidence**

- The Hi-CoT report argues that hierarchical planning and execution improves average accuracy by 6.2% while reducing trace length by 13.9% relative to conventional CoT across reported models and mathematical benchmarks. [S1]

### Finding 4

**Claim**

CoT-style demonstrations may sometimes function primarily as output-format guidance rather than as a reliable improvement to underlying reasoning quality, especially for modern LLMs; the supplied evidence does not establish this claim conclusively.

**Confidence:** Low

**Why this confidence level**

The new sources add several explanatory accounts in which intermediate or hidden reasoning contributes to performance, but all are secondary or non-controlled and therefore do not resolve whether observed gains arise from reasoning, formatting, compliance, or additional computation.

**Evidence**

- In its related-work discussion, the source attributes to Cheng et al. (2025) the finding that CoT exemplars primarily enforce output format for modern LLMs. [S1]

### Finding 5

**Claim**

Benchmarking choices and evaluation thresholds can materially change the apparent effect of CoT.

**Confidence:** High

**Why this confidence level**

The new sources add further variation in prompting format and task suitability, although they do not provide quantitative controlled comparisons that would replace the direct evidence from S3 and S7.

**Evidence**

- The study tested each question 25 times and reported separate complete-accuracy, high-accuracy, majority-correct, and average-rating metrics; effects differed across these metrics. [S3]
- Google Research reports that CoT effects vary by task: improvements were substantial on arithmetic reasoning, smaller on several commonsense tasks, and especially large on sports understanding, indicating task-dependent apparent effectiveness. [S7]
- The guide summarizes different reported gains across arithmetic, commonsense, and symbolic-reasoning benchmarks, further indicating that benchmark choice affects the measured effect. [S6]
- The tutorial identifies arithmetic, logic, and multistep tasks as use cases and separately notes costs and hallucination risks, reinforcing that measured outcomes depend on task and evaluation dimensions. [S8]
- The article describes different CoT variants, including zero-shot, few-shot, least-to-most, and self-consistency, with different intended task settings; this indicates that prompting format can affect apparent efficacy. [S9]

### Finding 6

**Claim**

The reported early CoT literature identifies model scale as a major moderator: benefits were reported to emerge primarily for models around 100B parameters or larger, while smaller models could show little benefit or worse performance.

**Confidence:** High

**Why this confidence level**

S7 directly describes scale-dependent CoT results across arithmetic and commonsense evaluations; S6 independently summarizes the same moderator, though as a secondary educational source.

**Evidence**

- Google Research reports that successful CoT reasoning was an emergent property of scale, with benefits materializing at approximately 100B parameters, and that smaller models did not obtain the same gains on the evaluated reasoning tasks. [S7]
- The guide summarizes the limitation that CoT gains were reported for models of roughly 100B parameters, while smaller models could produce illogical chains and perform worse than with standard prompting. [S6]

### Finding 7

**Claim**

The supplied explanatory sources distinguish externally prompted CoT from internally generated or test-time reasoning in models trained to reason, but they do not provide controlled evidence establishing the relative accuracy or marginal benefit of these approaches.

**Confidence:** High

**Why this confidence level**

Both sources explicitly make the distinction, but neither supplies a controlled comparison of externally prompted and internally generated reasoning or isolates the marginal effect of a generic CoT instruction.

**Evidence**

- The article describes a transition from user-prompted CoT to reasoning models that generate reasoning internally through additional fine-tuning and reinforcement learning. [S9]
- NVIDIA distinguishes models that require a user prompt to elicit step-by-step reasoning from test-time-scaling models that initiate and manage reasoning internally. [S10]

## Conflicts and Uncertainty

- Evidence concerning ledger claim C2 is conflicting: For models with built-in reasoning capabilities, a generic instruction to think step by step may provide little additional accuracy and can impose substantial latency or token costs. [S3] [S9] [S10] [S8] [S5] [S7] [S6]
- Evidence concerning ledger claim C3 is conflicting: Observed CoT gains can depend on the structure of the elicited reasoning process, not merely on requiring a longer verbal trace. [S1]
- Evidence concerning ledger claim C4 is conflicting: CoT-style demonstrations may sometimes function primarily as output-format guidance rather than as a reliable improvement to underlying reasoning quality, especially for modern LLMs; the supplied evidence does not establish this claim conclusively. [S1] [S2] [S5] [S7] [S6] [S8] [S9] [S10]

## Remaining Gaps

- Direct, controlled evidence is needed to distinguish genuine improvements in problem solving from gains caused by output formatting, answer extraction, or compliance with requested response structure.
- It remains unclear which task properties, model training characteristics, and CoT variants determine whether generic CoT helps, harms, or has negligible effect.
- The supplied evidence does not independently verify the cited Cheng et al. finding about CoT exemplars primarily enforcing output format.
- It remains unresolved whether the large CoT gains reported in early large-model studies persist for current models with internal or explicitly trained reasoning mechanisms, and how much of any marginal gain is attributable to the prompt versus the model’s capabilities.
- The supplied sources report scale and task moderators but do not jointly disentangle model scale, task complexity, prompting format, and use of tools such as external calculators as causes of the observed CoT gains.

## Conclusion

The findings above reflect the evidence validated before the run ended. They should be treated as provisional because normal final synthesis did not complete and important gaps may remain.

## Sources

- [S1] Hierarchical Chain-of-Thought Prompting: Enhancing LLM ... — https://arxiv.org/html/2604.00130v1
- [S2] Chain-Of-Thought Prompting In LLMs | by Cobus Greyling | Medium — https://cobusgreyling.medium.com/chain-of-thought-prompting-in-llms-1077164edf97
- [S3] The Decreasing Value of Chain of Thought in Prompting — https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought
- [S4] Contrastive Chain-Of-Thought Prompting - Kore.ai — https://www.kore.ai/blog/contrastive-chain-of-thought-prompting
- [S5] What is chain of thought (CoT) prompting? — https://www.ibm.com/think/topics/chain-of-thoughts
- [S6] Chain-of-Thought Prompting — https://learnprompting.org/docs/intermediate/chain_of_thought
- [S7] Language Models Perform Reasoning via Chain of Thought — https://research.google/blog/language-models-perform-reasoning-via-chain-of-thought
- [S8] What is Chain-of-Thought (CoT) in LLMs? — https://www.youtube.com/watch?v=xPly2h-gIcw
- [S9] Chain-of-Thought (CoT): Prompting & LLM Reasoning Explained — https://www.altexsoft.com/blog/chain-of-thought-prompting
- [S10] What is Chain of Thought (CoT) Prompting? — https://www.nvidia.com/en-us/glossary/cot-prompting
