# Research Report

## Research Question

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

## Summary

The supplied evidence does not support a universal answer. Chain-of-thought (CoT) can improve measured performance, especially for some non-reasoning models and difficult tasks, but its effects vary by model, task, metric, prompt structure, and inference procedure. For models with built-in reasoning, generic requests to think step by step often add little accuracy while increasing latency. Visible natural-language traces are also not necessarily faithful records of the causal process producing an answer. Thus, formatting and elicitation likely contribute to some observed gains, but the evidence does not establish that CoT benefits are primarily formatting effects in general.

## Findings

### Finding 1

**Claim**

CoT is conditionally effective rather than uniformly effective: the result depends on model type, task, benchmark difficulty, and evaluation criterion.

**Confidence:** High

**Why this confidence level**

Multiple supplied sources directly report variation across models, tasks, and metrics. The broad positive claims are less specific and do not overturn the heterogeneity finding.

**Evidence**

- A GPQA Diamond evaluation found different CoT effects for non-reasoning and reasoning models, with average accuracy, perfect accuracy, and majority-performance metrics sometimes producing different conclusions. [S2]
- Other supplied studies report heterogeneous outcomes across mathematical, logical, and search-based evaluations, including mixed accuracy, efficiency, and diversity effects. [S1] [S7] [S8] [S9]
- General explainers describe broad benefits on complex reasoning tasks, but provide less direct comparative evidence than the evaluations reporting heterogeneity. [S3] [S4] [S5]

### Finding 2

**Claim**

For the tested non-reasoning models on difficult GPQA Diamond questions, generic CoT improved average performance but could increase variability and reduce perfect-accuracy performance for some models.

**Confidence:** High

**Why this confidence level**

The evidence directly reports the tested models, task, and differing evaluation outcomes, but does not justify generalization beyond that evaluation.

**Evidence**

- The reported average gains included 13.5% for Gemini Flash 2.0 and 11.7% for Sonnet 3.5, while perfect-accuracy effects were mixed and Gemini Pro 1.5 showed a particularly large decline. [S2]

### Finding 3

**Claim**

For the tested reasoning models, a generic step-by-step request produced marginal accuracy changes and increased response time, consistent with diminishing incremental value when reasoning is already built into the model.

**Confidence:** High

**Why this confidence level**

S2 directly compares prompting conditions for named reasoning models. The counterevidence is a broad claim rather than a matched comparison.

**Evidence**

- On GPQA Diamond, the reported changes for o3-mini and o4-mini were small, Gemini Flash 2.5 declined, and CoT requests increased response times by approximately 20–80%. [S2]
- A general account that more internal reasoning or test-time compute can improve answers does not distinguish this situation from generic prompting of models that already reason internally. [S4]

### Finding 4

**Claim**

Some apparent CoT benefits may arise from eliciting a response format or reasoning-like behavior rather than from reliably improving the underlying solution process, but the supplied evidence cannot determine the relative causal contribution of formatting and problem solving.

**Confidence:** High

**Why this confidence level**

The evidence strongly supports distinguishing visible explanations from underlying computation, but no supplied controlled ablation holds formatting constant while directly measuring solution quality.

**Evidence**

- The supplied discussion reports that some modern-model CoT exemplars primarily enforce output format and that simple CoT variants can have negligible effects when models already produce CoT-like reasoning by default. [S1] [S2]
- Faithfulness-focused evidence reports that model-generated CoTs can be plausible rationalizations: editing the displayed CoT often left final answers largely unchanged, and reported unfaithfulness increased with model size. [S9]
- Latent-reasoning work separates reasoning representations from verbalization, showing that reasoning-like computation can occur without an explicit natural-language CoT. [S7] [S8]
- Conversely, general explainers attribute improvements to decomposition into sequential intermediate steps and to structured intermediate reasoning. [S3] [S4] [S5]

### Finding 5

**Claim**

Additional structure can outperform flat CoT in some evaluations, indicating that the organization and constraints of a trace matter—not merely whether a trace is present.

**Confidence:** Medium

**Why this confidence level**

The results indicate that structured alternatives can change accuracy, efficiency, and search behavior, but the systems and evaluations are not sufficiently matched to establish broad superiority or to show that generic CoT improves latent reasoning.

**Evidence**

- Hi-CoT reported a 6.2% average accuracy improvement and a 13.9% reduction in trace length relative to CoT across 13 model configurations and five mathematical benchmarks. [S1]
- COCOT reported fewer forward passes than explicit CoT, while PLaT reported stronger Pass@k scaling and reasoning diversity under search-based inference. [S7] [S8]

### Finding 6

**Claim**

Latent-reasoning approaches suggest that reasoning and verbalization can be partially decoupled, with trade-offs among efficiency, accuracy, interpretability, and exploration.

**Confidence:** Medium

**Why this confidence level**

Both sources report task- and metric-dependent trade-offs, but they concern specialized trained latent systems rather than generic CoT prompting across matched models.

**Evidence**

- COCOT used fewer forward passes than explicit CoT, but its accuracy fell on GSM8k while increasing on two logical-reasoning benchmarks. [S7]
- PLaT reported lower greedy accuracy than baselines but stronger Pass@k scaling and greater reasoning diversity, indicating a trade-off between immediate precision and exploration potential. [S8]

### Finding 7

**Claim**

The main fault lines behind conflicting results are model regime, task structure, evaluation metric, inference budget, trace structure, and whether visible reasoning is treated as evidence of faithful computation.

**Confidence:** High

**Why this confidence level**

This synthesis is supported by several claims with direct evidence. The causal explanation remains qualified because the ledger identifies an unresolved need for controlled formatting-versus-process ablations.

**Evidence**

- Non-reasoning and reasoning models respond differently to generic CoT, and average accuracy can disagree with perfect-accuracy or majority-performance measures. [S2]
- Results differ across mathematical and logical tasks, including cases where latent methods are more efficient or better suited to backtracking and cases where accuracy declines. [S1] [S7] [S8]
- Faithfulness concerns mean that a successful or plausible written trace does not by itself establish that the trace caused the answer. [S9]
- Claims that sequential intermediate steps improve solving and claims that CoT mainly shapes output format represent competing interpretations, but the supplied sources do not provide a decisive controlled test between them. [S3] [S4] [S5] [S10]

## Conflicts and Uncertainty

- Direct evaluations support conditional or diminishing CoT effects, while general explainers portray CoT as broadly accuracy-improving. The direct evaluations are more specific to tested models and protocols; the supplied evidence does not establish that the broad claims apply universally. [S2] [S3] [S4] [S5]
- The evidence supports both a computational interpretation of intermediate steps and a formatting or elicitation interpretation. Faithfulness findings weaken the inference from a convincing trace to a genuine causal reasoning process, but do not show that all CoT gains are merely formatting effects. [S1] [S3] [S4] [S5] [S9] [S10]
- Latent-reasoning results suggest benefits from decoupling reasoning and verbalization, but they involve specialized trained systems and are not controlled apples-to-apples tests against generic CoT prompting. [S7] [S8]
- Some claims rely on secondary explainers or summaries rather than full comparative study details, limiting assessment of robustness and independent replication. [S1] [S3] [S4] [S5] [S9]

## Remaining Gaps

- A controlled ablation holding output formatting constant while measuring solution quality is needed to determine whether CoT gains arise from improved problem solving, formatting compliance, or both.
- The supplied evidence does not establish how effects vary across a broad range of task types, model sizes, prompting variants, and evaluation protocols beyond the reported evaluations.
- The reliability, statistical robustness, and independent replication of the reported findings—particularly the Hi-CoT results and the formatting interpretation—remain unclear.
- There is no matched comparison of latent and explicit reasoning under equivalent models, training data, inference compute, and output requirements.
- The research process stopped because the maximum iteration limit was reached; no separate material counter-search was recorded as blocked by duplication, budget, or a one-search limit.

## Conclusion

CoT is an effective but context-dependent elicitation strategy, not a universally reliable reasoning mechanism. It appears most useful in some difficult-task and non-reasoning-model settings, while offering diminishing returns for tested models with built-in reasoning. The literature conflicts because studies compare different model regimes, tasks, metrics, trace structures, and compute budgets, and because visible natural-language reasoning is not guaranteed to be faithful to the process that generated the answer. The supplied evidence supports the claim that formatting and elicitation can matter, but it does not justify the stronger conclusion that CoT primarily improves formatting rather than reasoning in all cases.

## Sources

- [S1] Hierarchical Chain-of-Thought Prompting: Enhancing LLM ... — https://arxiv.org/html/2604.00130v1
- [S2] The Decreasing Value of Chain of Thought in Prompting — https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought
- [S3] 🧠What is LLM Chain of Thought Prompting? | by Tahir — https://medium.com/@tahirbalarabe2/what-is-llm-chain-of-thought-prompting-1d4b57a4dd22
- [S4] What is Chain of Thought (CoT) Prompting? — https://www.nvidia.com/en-us/glossary/cot-prompting
- [S5] What is chain of thought (CoT) prompting? - IBM — https://www.ibm.com/think/topics/chain-of-thoughts
- [S6] Latent Reasoning in LLMs — https://www.emergentmind.com/topics/latent-reasoning-in-large-language-models
- [S7] Worries about latent reasoning in LLMs — EA Forum — https://forum.effectivealtruism.org/posts/sNkua636jSni6Jftt/worries-about-latent-reasoning-in-llms
- [S8] Latent Chain-of-Thought as Planning: Decoupling Reasoning from Verbalization — https://arxiv.org/html/2601.21358v1
- [S9] What is faithful chain-of-thought reasoning and why is it ... — https://blog.bluedot.org/p/faithful-chain-of-thought
- [S10] How Chain of Thought (CoT) Prompting Helps LLMs ... — https://www.splunk.com/en_us/blog/learn/chain-of-thought-cot-prompting.html
