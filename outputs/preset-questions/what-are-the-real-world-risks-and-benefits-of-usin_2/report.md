# Research Report

## Research Question

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

## Summary

Synthetic data can expand scarce, costly, specialized, or underrepresented training data and can improve task-specific fine-tuning when generation and curation are well controlled. The principal risks are quality degradation from recursive or indiscriminate synthetic-data use, inherited or newly introduced bias, privacy and provenance failures, and evaluation results that do not transfer reliably to real-world performance. Evidence supports additive use anchored in real data, rigorous validation, held-out testing, human oversight, and task-specific comparisons rather than assuming that more synthetic data or higher diversity is universally beneficial.

## Findings

### Finding 1

**Claim**

Synthetic data can provide practical training and fine-tuning benefits by expanding scarce or expensive datasets, supporting domain adaptation, targeting underrepresented classes, and producing task-specific examples.

**Confidence:** High

**Why this confidence level**

Multiple sources and controlled task-specific studies support the benefits, while also indicating that outcomes depend on the task, generation strategy, and data budget.

**Evidence**

- Sources describe synthetic data for augmentation, class-imbalance mitigation, domain adaptation, rare-event and subgroup coverage, and task-specific examples including dialogues, code, reasoning traces, question-answer pairs, tool-use, RAG, and classification data. [S4] [S5] [S6] [S9] [S11]
- Controlled or empirical studies report improvements on specific classification, mathematics, question-answering, and Text2SQL tasks, including additional gains from hybrid real-plus-synthetic training. [S12] [S13]

### Finding 2

**Claim**

Recursive use of model-generated data, or replacing real data with synthetic data, can cause model collapse and degrade learned quality.

**Confidence:** High

**Why this confidence level**

The risk is supported by multiple sources describing convergent failure modes rather than by a single isolated observation.

**Evidence**

- The evidence describes narrowing of the learned distribution, loss of low-probability valid examples, degraded outputs, and a reported increase in OPT-125m perplexity after repeated training without retained real data. [S1] [S2]
- Additional sources warn that repeatedly training on other models' outputs can stagnate or reduce capabilities and quality. [S5] [S9]

### Finding 3

**Claim**

An additive, real-data-anchored approach is less risky than indiscriminate replacement of real data, although the evidence does not establish a universal safe mixing ratio.

**Confidence:** Medium

**Why this confidence level**

The ledger contains direct support for the accumulate-versus-replace distinction but limited evidence testing the recommendation across models, tasks, and mixture proportions.

**Evidence**

- Analytical evidence reports a finite upper bound on test error when synthetic data accumulates alongside real data, compared with unbounded growth when synthetic data replaces real data, and recommends an accumulate-not-replace regime. [S1]

### Finding 4

**Claim**

Synthetic-data quality depends on generation discipline and validation, including curation, diversity checks, deduplication, quality filtering, lineage, fidelity metadata, real-data anchoring, and downstream utility testing.

**Confidence:** High

**Why this confidence level**

The need for controls is consistently supported, but the evidence qualifies rather than guarantees their effectiveness.

**Evidence**

- Sources identify curation, deduplication, quality filtering, provenance, lineage, fidelity metadata, faithfulness checks, instruction-adherence checks, and real-data mixing as controls against repetition, drift, teacher-bias inheritance, mode collapse, and audit gaps. [S1] [S2] [S4] [S6] [S11]
- Generation strategy and budget affect utility and diversity; multi-sample prompting improved some outcomes, while prompt optimization and other strategies produced task-dependent results. [S12] [S13]

### Finding 5

**Claim**

Greater diversity or similarity-based filtering is not universally beneficial: a curation method can improve diversity metrics while reducing downstream classification performance.

**Confidence:** High

**Why this confidence level**

The ledger records direct contradicting evidence that qualifies the broader quality-control claim.

**Evidence**

- Similarity-based curation improved diversity metrics but often reduced classification performance, showing that filtering criteria must be validated against the target task rather than optimized using surface diversity alone. [S12]

### Finding 6

**Claim**

Synthetic data can target underrepresented groups and potentially reduce fairness gaps, but it does not automatically remove bias; generated data may inherit source or generator-model biases, and bias-auditing tools are themselves imperfect.

**Confidence:** Medium

**Why this confidence level**

The evidence supports conditional mitigation and persistent risk, but does not quantify bias transfer or establish general fairness outcomes across LLM training settings.

**Evidence**

- Sources describe targeted generation for underrepresented slices and fairness improvement as conditional on distributional-fit, utility, privacy, held-out evaluation, fairness auditing, and retraining. [S6]
- Other evidence identifies selection, social, temporal, implicit, automation, and inherited model biases, while a demographic-bias benchmark found persistent disparities and weaknesses on intersectional cases in automated detection. [S5] [S7] [S9]

### Finding 7

**Claim**

Synthetic data does not automatically provide privacy protection; privacy risk depends on possible re-identification, memorization, provenance, and governance controls.

**Confidence:** Medium

**Why this confidence level**

The ledger supports the conditional nature of privacy protection but leaves measurable re-identification and memorization rates unresolved.

**Evidence**

- The evidence notes that synthetic-data workflows can retain privacy-substitution risks and that privacy obligations may still apply where re-identification is plausible. [S1]
- Privacy screening and governance are presented as required validation controls rather than automatic properties of generated data. [S4] [S6]

### Finding 8

**Claim**

Synthetic data can help construct evaluation sets that cover edge cases, adversarial scenarios, decision boundaries, and conversational failure modes, but synthetic or conventional benchmark scores may not reliably represent broad real-world capability or safety.

**Confidence:** High

**Why this confidence level**

The evidence supports both the coverage benefit and the limitation that synthetic evaluation distributions and scores may not reflect real-world outcomes.

**Evidence**

- Sources describe synthetic evaluation cases for edge cases, adversarial examples, ambiguous queries, multi-turn contexts, failure modes, calibration, and robustness. [S4] [S6]
- Evidence warns that benchmark saturation or contamination and static tests can miss real-world reliability, fairness, reproducibility, and safety issues; synthetic evaluation collections showed systematic differences from human queries and judgments and distorted absolute performance estimates. [S5] [S8]
- Human oversight and semantic, judgment-based evaluation are recommended instead of relying solely on surface-form metrics. [S14]

### Finding 9

**Claim**

No single synthetic-data generation strategy is uniformly optimal: effectiveness varies with task, seed-data size, prompting or generation method, and available budget.

**Confidence:** High

**Why this confidence level**

Two sources directly report task- and budget-dependent results, though the domains studied are limited.

**Evidence**

- Across mathematics, general question answering, and Text2SQL, different strategies performed better under different query budgets. [S13]
- Across requirements-classification tasks, multi-sample prompting improved some utility and diversity measures, while automated prompt optimization produced task-dependent gains and losses. [S12]

## Conflicts and Uncertainty

- C4 is broadly supported as a claim about the importance of curation and validation, but S12 shows that similarity-based curation can improve diversity while harming classification performance. Thus, diversity and deduplication criteria should not be treated as universally aligned with task utility. [S12]
- C6 emphasizes that synthetic data does not automatically remove bias, while S6 presents targeted synthetic generation as a potentially effective fairness intervention when an audit-and-retrain loop succeeds. The evidence supports conditional mitigation, not an unconditional conclusion in either direction. [S6] [S7] [S9]

## Remaining Gaps

- Direct controlled real-world evidence is lacking on when synthetic data improves versus harms downstream LLM quality compared with equivalent human-authored or human-labeled data across fine-tuning tasks and domains.
- The evidence does not quantify demographic, cultural, or task-specific bias effects, or establish whether minority-class targeting improves fairness without stereotyping or label artifacts.
- Reliable privacy guarantees and measurable re-identification or memorization risks for LLM-generated training data remain unestablished.
- The evidence does not establish how to validate synthetic evaluation sets against independent real-world outcomes, contamination, benchmark gaming, and distribution shift, or which metrics best detect these failures.
- The research process ended because the maximum number of iterations was reached. No separate ledger record documents counter-searches blocked by duplication, budget, or a one-search limit.

## Conclusion

Synthetic data is best understood as a conditional augmentation and evaluation tool, not a drop-in replacement for real data or a guarantee of fairness, privacy, quality, or safety. Its strongest demonstrated benefits are targeted expansion and task-specific fine-tuning under constrained data budgets. Its major risks are recursive quality collapse, distribution narrowing, inherited bias, privacy and lineage failures, and misleading evaluation results. A defensible workflow therefore retains real data, validates fidelity and downstream utility, audits fairness and privacy, uses held-out and human-supervised evaluation, and checks performance against independent real-world behavior. The ledger does not support universal claims about when synthetic data is superior, fairer, more private, or predictive of deployment performance.

## Sources

- [S1] Synthetic Data for LLM Training: Decision Guide 2026 — https://www.digitalapplied.com/blog/synthetic-data-generation-llm-training-decision-guide-2026
- [S2] Synthetic Data for AI Training: Use Cases and Risks [2026] — https://atlan.com/know/ai-agent/data-for-ai/synthetic-data-for-ai-training
- [S3] Using Synthetic Data to Improve LLM Fine‑Tuning - Newline — https://www.newline.co/@Dipen/using-synthetic-data-to-improve-llm-finetuning--d453f658
- [S4] Synthetic Data Generation with LLMs: Techniques and Use ... — https://tetrate.io/learn/ai/synthetic-data-generation-llms
- [S5] Large Language Models Are Still Getting Stronger, but ... — https://www.newswise.com/articles/large-language-models-are-still-getting-stronger-but-researchers-face-new-bottlenecks-in-data-evaluation-and-safety
- [S6] Synthetic Data for Bias Mitigation 2026: 5 Methods + FAGI — https://futureagi.com/blog/synthetic-data-generation-bias-2025
- [S7] Evaluating LLMs for Detecting Demographic-Targeted Social Bias: A Comprehensive Benchmark Study — https://arxiv.org/html/2510.04641v3
- [S8] Towards Understanding Bias in Synthetic Data for Evaluation | alphaXiv — https://www.alphaxiv.org/abs/2506.10301
- [S9] Data bias in LLM and generative AI applications - MOSTLY AI powered by Syntho — https://mostly.ai/blog/data-bias-types
- [S10] Guide to Ethical Fine-Tuning of Large Language Models | Tonic.ai — https://www.tonic.ai/guides/ethical-fine-tuning-llm-synthetic-data
- [S11] Synthetic Data for LLM Fine-Tuning 2026 — https://futureagi.com/blog/synthetic-data-fine-tuning-llms
- [S12] How Good Are Synthetic Requirements ? Evaluating LLM-Generated Datasets for AI4RE — https://arxiv.org/html/2506.21138v1
- [S13] Synthetic Data Generation Strategies for Fine-Tuning LLMs — https://scale.com/blog/synthetic-data-fine-tuning-llms
- [S14] Medium — https://medium.com/@akankshasinha247/synthetic-data-evaluation-pipelines-scaling-fine-tuning-without-losing-alignment-f469a81cdf9a
