# Research Report

## Research Question

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees-find the real fault lines and explain what accounts for the conflicting results.

## Summary

The accumulated evidence does not support either universal claim. Chain-of-thought (CoT) can improve accuracy on some difficult, multistep problems, but generic “think step by step” prompting is model-, task-, metric-, and budget-dependent. Much of the disagreement comes from treating different interventions as one method: zero-shot instructions, few-shot demonstrations, self-consistency, hierarchical planning, and task-specific structured representations differ substantially. The evidence also does not establish that visible reasoning traces reflect improved latent reasoning rather than formatting, procedure imitation, or extra inference computation. The strongest conclusion is that task-aligned structure may be useful, whereas merely eliciting longer explanations is not reliably effective.

## Findings

### Finding 1

**Claim**

Generic CoT is conditionally effective rather than universally beneficial.

**Confidence:** Medium

**Why this confidence level**

The conditional pattern is supported by a controlled repeated-trial report and historical benchmark summaries, but the retrieved evidence does not provide a broad, standardized replication across tasks and model families.

**Evidence**

- A repeated-trial GPQA Diamond study found average gains for some non-reasoning models, but mixed or negative effects under stricter accuracy criteria and minimal or negative effects for some built-in reasoning models. [S2]
- Historical and instructional sources report substantial CoT gains on selected arithmetic, commonsense, and symbolic benchmarks, particularly for very large models, but these results use different models, tasks, and evaluation procedures. [S7] [S9]

### Finding 2

**Claim**

Model capability is a major fault line: explicit CoT tends to be more useful when the model does not already provide effective reasoning, while built-in reasoning models may gain little from a generic CoT cue.

**Confidence:** Medium

**Why this confidence level**

The model-type contrast is directly reported, but the evidence combines older summarized results with one modern benchmark and does not isolate architecture, training, and prompting effects.

**Evidence**

- On GPQA Diamond, several non-reasoning models showed average improvements, whereas reasoning models showed only small gains for two models and a decline for another. [S2]
- An instructional summary of earlier CoT work states that smaller models could produce illogical chains and perform worse than with direct prompting, while gains were associated with very large models. [S7]
- The GPQA study also reports that many models produce CoT-like reasoning by default, reducing the incremental effect of an explicit instruction. [S2]

### Finding 3

**Claim**

The label “CoT” hides materially different interventions, which is a central source of conflicting findings.

**Confidence:** High

**Why this confidence level**

The sources explicitly describe different procedures under the broad CoT label. However, the retrieved research does not provide a factorial experiment separating every component.

**Evidence**

- The sources distinguish zero-shot step-by-step instructions, few-shot reasoning demonstrations, Auto-CoT, self-consistency, contrastive CoT, faithful CoT, tabular CoT, and hierarchical or task-specific structured variants. [S1] [S6] [S8] [S9] [S10]
- Self-consistency adds multiple sampled reasoning paths and answer selection, changing the inference budget rather than merely changing the prompt. [S6]
- Hierarchical CoT and structured CoT impose planning or domain-specific representations that are not equivalent to asking for a longer natural-language explanation. [S1] [S11]

### Finding 4

**Claim**

Task-aligned structure may account for some gains more than verbosity or the mere presence of an explanation.

**Confidence:** Medium

**Why this confidence level**

The code-generation study provides stronger primary evidence for task-specific structure, but it does not fully isolate structure from wording, constraints, or token allocation, and generalization beyond code is unresolved.

**Evidence**

- Hi-CoT reports higher accuracy and shorter traces than flat CoT, attributing the improvement to alternating planning and execution plus compression bottlenecks that reduce redundancy and drift. [S1]
- In code generation, the published SCoT study reports slight gains from ordinary CoT but up to a 13.79% Pass@1 improvement over ordinary CoT when reasoning explicitly represents sequence, branch, and loop structures. [S11]
- S11 characterizes ordinary natural-language CoT as verbose and poorly suited to representing programming branches and loops, while SCoT is designed as a concise intermediate representation between natural language and code. [S11]

### Finding 5

**Claim**

Visible CoT should not automatically be interpreted as evidence of improved underlying reasoning or faithful explanations.

**Confidence:** High

**Why this confidence level**

The sources directly establish that visible rationales can be incorrect or non-faithful and that the strongest format-versus-reasoning study is missing. They do not, however, quantify how often formatting rather than reasoning explains CoT gains.

**Evidence**

- The retrieved guides acknowledge that generated explanations may not match the process that produced the answer, even when they appear plausible. [S8] [S12]
- Few-shot demonstrations teach both a stepwise response format and a procedure, so their accuracy gains cannot be attributed solely to improved latent reasoning without controls for formatting and demonstration content. [S9] [S10]
- One worked example in S10 contains the arithmetic error “3+4 is 12,” demonstrating that a plausible stepwise rationale can itself be invalid. [S10]
- S1 relays a 2025 claim that CoT exemplars primarily enforce output format rather than improve reasoning quality, but the underlying study is not included in the retrieved material. [S1]

### Finding 6

**Claim**

Evaluation design can make CoT appear more or less effective.

**Confidence:** Medium

**Why this confidence level**

The repeated-trial evidence directly supports metric and cost sensitivity, but it is concentrated in one benchmark and does not establish the best evaluation protocol.

**Evidence**

- The GPQA study tested each question 25 times and used average accuracy, majority accuracy, high-accuracy, and perfect-accuracy thresholds, finding that conclusions changed with the metric and that CoT could increase variability or harm easy cases. [S2]
- The same study reports substantial latency increases: 35–600% for non-reasoning models and 20–80% for reasoning models, sometimes for small or negligible accuracy gains. [S2]
- Historical summaries report point-estimate accuracy improvements but do not control for repeated-trial variance, latency, token use, or cost-adjusted performance. [S7] [S9]

## Conflicts and Uncertainty

- Instructional and industry-oriented sources portray CoT as broadly accuracy-enhancing, while the repeated-trial GPQA study finds model-, metric-, and cost-dependent effects, including negligible or negative outcomes. [S2] [S4] [S5] [S9] [S10] [S12]
- Historical sources associate CoT gains with very large models, whereas the modern GPQA report finds useful gains for some non-reasoning models. This may reflect differences in model training and architecture, but the accumulated evidence does not directly test that explanation. [S2] [S7]
- The strong gains reported for hierarchical or structured CoT do not directly contradict weak results for generic CoT: they use different scaffolds, tasks, models, and evaluation conditions. [S1] [S2] [S11]
- The format-only interpretation is unresolved. S1 cites a study claiming that CoT exemplars mainly enforce output format, but that primary study and its controls are absent from the retrieved material. [S1]
- The causal contribution of demonstrations, decomposition, structured planning, additional generated tokens, self-consistency, and answer-selection procedures has not been separately identified. [S1] [S6] [S8] [S9] [S10] [S11]

## Remaining Gaps

- The primary 2025 study cited by S1 separating output-format effects from genuine reasoning gains was not retrieved.
- No accumulated source provides a comparison equalizing output length, answer format, token budget, and total inference computation.
- The transferability of code-specific structured-CoT results to arithmetic, symbolic, commonsense, scientific, and open-ended reasoning remains unknown.
- The evidence does not establish whether CoT traces are causally faithful, rather than post-hoc or stylistically generated explanations.
- The research stopped at the iteration limit, so these unresolved causal questions should not be treated as answered.

## Conclusion

CoT is best understood as a conditional prompting scaffold, not a universally effective reasoning strategy. It can help when a model benefits from explicit decomposition, particularly on difficult multistep tasks, but generic step-by-step prompting often adds latency and verbosity while producing small, variable, or even negative gains. The real fault lines are model capability, task structure, intervention design, evaluation metric, inference budget, and explanation faithfulness. The evidence favors task-aligned structure over unstructured longer traces, but it does not establish that ordinary CoT improves latent reasoning rather than output format or procedure imitation. Therefore, the literature’s disagreement is largely explained by non-equivalent experiments and evaluation standards, while the central formatting-versus-reasoning question remains unresolved in the accumulated research.

## Sources

- [S1] Hierarchical Chain-of-Thought Prompting: Enhancing LLM ... — https://arxiv.org/html/2604.00130v1
- [S2] The Decreasing Value of Chain of Thought in Prompting — https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought
- [S3] Contrastive Chain-Of-Thought Prompting — https://www.kore.ai/blog/contrastive-chain-of-thought-prompting
- [S4] What is chain of thought (CoT) prompting? — https://www.ibm.com/think/topics/chain-of-thoughts
- [S5] Medium — https://cobusgreyling.medium.com/chain-of-thought-prompting-in-llms-1077164edf97
- [S6] Chain of Thought Prompting Guide — https://medium.com/@dan_43009/chain-of-thought-prompting-guide-3fdfd1972e03
- [S7] Chain-of-Thought Prompting — https://learnprompting.org/docs/intermediate/chain_of_thought
- [S8] Chain of Thought Prompting Guide — https://www.prompthub.us/blog/chain-of-thought-prompting-guide
- [S9] Chain-of-Thought (CoT) Prompting - Prompt Engineering Guide — https://www.promptingguide.ai/techniques/cot
- [S10] Chain of Thought Prompting Explained (with examples) | Codecademy — https://www.codecademy.com/article/chain-of-thought-cot-prompting
- [S11] [PDF] Structured Chain-of-Thought Prompting for Code Generation - Ge Li — https://ligechina.github.io/My%20Papers/2025%20-%20TOSEM%20-%20Structured%20Chain-of-Thought%20Prompting%20for%20Code%20Generation.pdf
- [S12] Chain-of-thought (CoT) prompting: Complete overview — https://www.superannotate.com/blog/chain-of-thought-cot-prompting
