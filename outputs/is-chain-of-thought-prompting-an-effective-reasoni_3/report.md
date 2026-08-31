# Research Report

## Research Question

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

## Summary

The supplied evidence supports a conditional rather than universal answer. Chain-of-thought (CoT) is an inference-time technique that elicits intermediate natural-language steps, but its observed benefits vary substantially with model, task, prompt design, baseline, and evaluation metric. It can improve problem-solving accuracy in selected settings—especially some mathematical, symbolic, and difficult multistep tasks—but the evidence does not show that generic CoT uniformly improves reasoning or general reasoning ability. Longer, more coherent, or more structured rationales are not themselves evidence of faithful internal reasoning. The main disagreements concern whether measured gains arise from useful decomposition and additional inference-time search, or instead from answer elicitation, prompt-format effects, benchmark compliance, and evaluator perceptions. The supplied evidence cannot resolve these alternatives across the literature.

## Findings

### Finding 1

**Claim**

CoT denotes a family of inference-time methods that elicit intermediate steps before a final answer, including few-shot and zero-shot prompting, automatically generated demonstrations, self-consistency, and structured or hierarchical variants. The presence of intermediate text defines the method, not necessarily the quality or causal role of the reasoning.

**Confidence:** High

**Why this confidence level**

Multiple supplied sources consistently describe CoT as elicited intermediate representations while showing that the term covers materially different prompting, search, training, and structural methods.

**Evidence**

- Sources define conventional CoT as generating intermediate reasoning steps and distinguish zero-shot, few-shot, automatic, self-consistency, hierarchical, symbolic, program-based, and latent or structured variants. [S1] [S4] [S5] [S6] [S8] [S9]

### Finding 2

**Claim**

The supplied evidence does not support treating generic CoT as uniformly beneficial for task solving. In the reported GPQA Diamond evaluation, some non-reasoning models showed modest average gains, whereas tested reasoning models showed mostly small gains and, in some cases, declines; stricter accuracy thresholds also produced mixed or negative effects. These findings are conditional on the tested models, task, prompting conditions, and metrics.

**Confidence:** High

**Why this confidence level**

The latest verification preserved the qualified claim: direct evidence establishes heterogeneous rather than universal effects, but the strongest comparison is one technical report and broader generalization remains open.

**Evidence**

- The GPQA Diamond study reported average gains of 4.4%–13.5% for non-reasoning models, small gains for some reasoning models, a 3.3% decrease for another, and a 17.2% decline for one model under a perfect-accuracy measure. [S2]
- Other supplied syntheses report positive results in selected mathematical, symbolic, logic, commonsense, and knowledge-oriented settings, but combine generic CoT with optimized templates, self-consistency, distillation, or other specialized variants. [S1] [S6] [S8] [S9]

### Finding 3

**Claim**

CoT benefits appear task-dependent rather than reflecting a general reasoning improvement. The supplied synthesis reports stronger gains for mathematical and symbolic tasks, moderate gains for some logic tasks, and minimal or absent gains for factual recall and comprehension; explicit rationales can also hurt when they are noisy or incorrect. Positive reports outside mathematics indicate that the boundary is not settled.

**Confidence:** Medium

**Why this confidence level**

The evidence supports domain heterogeneity, but the underlying study details, matched baselines, computation budgets, contamination controls, and independent replications are insufficient to determine how robust the domain pattern is.

**Evidence**

- A supplied synthesis reports median gains above 12 percentage points for symbolic and mathematical tasks, moderate logic gains, and minimal or zero gains for factual recall and comprehension, while also describing harmful effects in some pattern-based in-context settings. [S8]
- Other summaries report gains across commonsense, science, medical, algorithmic, and broader QA benchmarks, though their evidence mixes prompt variants and training or search methods and lacks sufficient detail for direct cross-task comparison. [S6] [S9]

### Finding 4

**Claim**

Some apparent CoT gains may reflect prompt organization, answer elicitation, decomposition, or additional inference-time computation rather than the mere production of a rationale. Prompt-template optimization and hierarchical organization are associated with reported gains, while hierarchical compression also reports shorter traces; these results show that prompt design and search structure moderate outcomes.

**Confidence:** Medium

**Why this confidence level**

The studies directly report improvements associated with optimized or structured prompting and substantial cost changes, but they do not isolate reasoning from formatting, decomposition, selection, or matched-compute effects.

**Evidence**

- An automatically discovered step-by-step template reportedly outperformed direct answering by 12 points across six QA datasets, with gains depending on wording, validation, model capacity, instruction tuning, and domain coverage. [S9]
- Hi-CoT reportedly improved accuracy by 6.2% on average, reached up to 61.4% on some model-task combinations, and reduced trace length by 13.9% relative to conventional CoT on selected mathematical benchmarks. [S1]
- On GPQA Diamond, CoT increased inference time by 35%–600% for non-reasoning models and 20%–80% for reasoning models, while accuracy benefits were inconsistent. [S2]

### Finding 5

**Claim**

A visible rationale is not evidence by itself of faithful underlying reasoning. The supplied evidence describes post-hoc or shortcut explanations, broken logical dependencies, confirmation bias, hidden influences omitted from rationales, and cases in which conclusions appear to precede completion of the displayed trace. Coherent explanations may therefore improve inspectability or evaluator impressions without faithfully reporting the computation that caused the answer.

**Confidence:** High

**Why this confidence level**

The latest verification qualified the claim to distinguish external rationale faithfulness from unobservable internal reasoning. The evidence strongly supports that rationale length and surface structure are insufficient, but it does not establish the frequency of unfaithfulness across models and tasks.

**Evidence**

- Sources report redundant or disorganized long traces, default CoT-like outputs without explicit CoT instructions, post-hoc rationalizations, shortcut traces, confirmation bias, hidden-bias effects, early-truncation effects, and invalid step dependencies. [S1] [S2] [S6] [S10] [S11] [S12]
- Causal-intervention work argues that coherence, likelihood, attention, ablation, or final-answer agreement cannot by themselves establish that a step was necessary or sufficient. [S13]
- Some explanatory sources present stepwise rationales as transparent and useful for debugging, but do not provide causal faithfulness tests; this supports inspectability, not proof of faithful computation. [S4] [S5] [S7] [S8]

### Finding 6

**Claim**

Causality-inspired evaluation and trajectory-selection methods provide evidence that rationale quality can matter, but they do not yet demonstrate that generic CoT itself improves underlying reasoning. Perturbation, necessity, and sufficiency tests reportedly improve selected accuracy, exemplar quality, or token efficiency on mathematical and commonsense benchmarks, while their gains may derive from filtering or inference-time search.

**Confidence:** Medium

**Why this confidence level**

The reported results directly concern specialized evaluation or reconstruction methods, but the supplied evidence lacks matched comparisons with generic CoT, rationale-free methods, alternative decomposition, and equal-compute baselines.

**Evidence**

- FACT-E and related work use controlled perturbations or causal necessity/sufficiency measures to identify flawed, redundant, indispensable, or insufficient steps and report improvements on selected benchmarks. [S11] [S12] [S13]

## Conflicts and Uncertainty

- Positive accounts describe CoT as substantially improving multistep arithmetic, symbolic, commonsense, logic, or broader reasoning performance, whereas the more qualified empirical evidence reports small, null, or negative effects in some models and metrics. The disagreement is partly substantive and partly methodological: positive summaries often combine generic CoT with optimized prompts, self-consistency, distillation, hierarchical structure, or selected benchmarks, while the negative or mixed evidence emphasizes generic prompting, reasoning models, and stringent metrics. [S2] [S4] [S5] [S6] [S8] [S9]
- One interpretation treats articulated steps as useful reasoning and transparency; another treats them as potentially post-hoc, unfaithful, or evaluator-friendly explanations. The supplied evidence supports the latter concern through intervention and bias tests, but does not show how often it occurs or whether it explains measured accuracy gains. [S4] [S5] [S6] [S7] [S8] [S10] [S11] [S12] [S13]
- The evidence cannot determine whether domain differences are caused by task structure itself or by confounded factors such as model scale and training, prompt quality, demonstration selection, decoding, test-time computation, benchmark artifacts, contamination, or publication and selection effects. [S1] [S2] [S6] [S8] [S9]

## Remaining Gaps

- Generic CoT has not been adequately compared with rationale-free few-shot prompting, alternative decomposition methods, hidden test-time computation, self-consistency, and matched inference-token budgets across the relevant task families.
- The supplied evidence does not establish whether rationales are faithful causal accounts, how frequently they are unfaithful, or whether faithfulness mediates accuracy gains.
- The evidence does not identify the independent effects of rationale quality, demonstrations, model scale and training, decoding and sampling, distribution shift, contamination, benchmark design, or publication and selection effects.
- The strongest direct performance evidence comes from one GPQA Diamond technical report and one Hi-CoT preprint focused on mathematical benchmarks; broader independent replication is unresolved.
- The supplied causal faithfulness measures have not been sufficiently compared with one another or validated across model families, domains, and hidden-reasoning systems.
- The ledger indicates that a counter-search was executed for the main heterogeneous-effects claim, but the stop reason was max_iterations; the remaining gaps therefore reflect unresolved evidence, not a completed literature-wide resolution.

## Conclusion

CoT is an effective reasoning strategy in some conditions, but not a universally effective one and not demonstrably a faithful window into internal reasoning. Its most defensible role is as a conditional inference-time intervention that can provide useful decomposition, search, or answer elicitation—especially on some difficult mathematical, symbolic, and multistep tasks. Conflicting results arise because studies vary in model capabilities, task distributions, prompt and demonstration quality, rationale structure, decoding and test-time compute, baselines, and evaluation criteria. A rationale’s length, coherence, or apparent transparency should not be confused with causal reasoning. The central unresolved fault line is therefore not simply “CoT works” versus “CoT is formatting”: measured gains may be real improvements in external problem solving while still failing to show faithful internal reasoning. The supplied evidence is insufficient to determine how much of the gain, across the literature, is reasoning, search, decomposition, calibration, answer elicitation, or formatting.

## Sources

- [S1] Hierarchical Chain-of-Thought Prompting: Enhancing LLM Reasoning Performance and Efficiency — https://arxiv.org/html/2604.00130v1
- [S2] The Decreasing Value of Chain of Thought in Prompting — https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought
- [S3] Medium — https://cobusgreyling.medium.com/chain-of-thought-prompting-in-llms-1077164edf97
- [S4] What is chain of thought (CoT) prompting? - IBM — https://www.ibm.com/think/topics/chain-of-thoughts
- [S5] What is Chain of Thought (CoT) Prompting? | NVIDIA Glossary — https://www.nvidia.com/en-us/glossary/cot-prompting
- [S6] Chain-of-Thought Reasoning — https://www.emergentmind.com/topics/chain-of-thought-reasoning-fc14269b-22e7-4eea-ad24-c345984799e4
- [S7] Chain of Thought Prompting in AI: A Comprehensive Guide [2026] — https://futureagi.substack.com/p/chain-of-thought-prompting-in-ai
- [S8] Chain-of-Thought Reasoning — https://www.emergentmind.com/topics/chain-of-thought-cot-reasoning-fd86d712-e431-4308-affd-c5dbdf17030a
- [S9] GPT-4.1 Mini & Chain-of-Thought Prompting — https://www.emergentmind.com/topics/gpt-4-1-mini-with-chain-of-thought-prompting
- [S10] What Is Chain-of-Thought Faithfulness? Why AI Reasoning Traces Are Unreliable | MindStudio — https://www.mindstudio.ai/blog/what-is-chain-of-thought-faithfulness-ai-reasoning
- [S11] FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning - ACL Anthology — https://aclanthology.org/2026.findings-acl.1014
- [S12] FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning — https://arxiv.org/html/2604.10693v1
- [S13] Causal Sufficiency and Necessity Improves Chain-of- ... — https://haoxuanli-pku.github.io/papers/NeurIPS%2025%20-%20Causal%20Sufficiency%20and%20Necessity%20Improves%20Chain-of-Thought%20Reasoning.pdf
- [S14] Multi-Dimensional Evaluation of Auto-Generated Chain-of-Thought Traces in Reasoning Models — https://www.mdpi.com/2673-2688/7/1/35
