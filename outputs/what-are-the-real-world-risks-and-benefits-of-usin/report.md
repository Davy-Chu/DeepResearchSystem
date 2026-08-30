# Research Report

## Research Question

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

## Summary

Synthetic data can be useful for expanding scarce training data, targeting rare cases, reducing annotation burdens, and adapting smaller models to specialized tasks. However, these benefits are conditional on careful curation and validation. The strongest recurring risks are degraded factuality and diversity, recursive model collapse, inherited or amplified bias, privacy overconfidence, and misleading evaluation results. The accumulated research supports using synthetic data as a supplement to—rather than a replacement for—high-quality real data, with provenance tracking and independent evaluation.

## Findings

### Finding 1

**Claim**

Synthetic data can reduce data scarcity and annotation effort while enabling targeted coverage of domain-specific, rare, imbalanced, or edge-case examples.

**Confidence:** Medium

**Why this confidence level**

The benefit is consistently described, but most evidence is secondary or instructional and does not establish uniform gains across tasks.

**Evidence**

- Sources describe synthetic data as useful when real data is scarce, expensive, proprietary, privacy-sensitive, or difficult to label, including augmentation, class-imbalance correction, rapid prototyping, and domain adaptation. [S3] [S4]
- Practitioner sources describe generating thousands of examples from smaller sets of real seed prompts through teacher generation, prompt variation, judging, filtering, and deduplication. [S13] [S14]

### Finding 2

**Claim**

Carefully curated synthetic data can improve task-specific performance or allow a smaller model to approach the performance of a much larger model, but the causal contribution of synthetic data is not always demonstrated.

**Confidence:** Medium

**Why this confidence level**

The sources provide concrete examples of conditional performance benefits, but independent controlled comparisons and complete synthetic-data results are limited.

**Evidence**

- The Phi-1 account attributes strong coding results to a curated mixture of real web data and synthetic textbooks and exercises, contrasting this with degradation from purely synthetic self-training. [S3]
- A Databricks case study reports approximately 70% F1 for an 8B fine-tuned model versus a 71% baseline from a 70B model, illustrating the potential efficiency of narrow-domain fine-tuning; the retrieved passage does not include the later synthetic-augmentation results. [S10]

### Finding 3

**Claim**

Synthetic-data quality depends heavily on seed coverage, factual correctness, label accuracy, diversity, novelty, distributional fidelity, filtering, and deduplication.

**Confidence:** High

**Why this confidence level**

This control principle is consistent across multiple sources, although the evidence does not identify a universally best metric or filter.

**Evidence**

- Narrow or unrepresentative seed data constrains the diversity and coverage of generated examples, while generation volume without filtering can propagate errors and duplicates. [S13] [S14]
- The broader LLM survey identifies cleaning, deduplication, filtering, privacy protection, data-mixture design, novelty, reliability, and verifiability as central data requirements. [S5]

### Finding 4

**Claim**

Recursive training on model-generated data can narrow the learned distribution, remove rare or low-probability cases, and degrade quality, diversity, and factual reliability.

**Confidence:** Medium

**Why this confidence level**

The general risk is supported across sources, but some quantitative or universal claims come from secondary sources and were not independently verified in the accumulated material.

**Evidence**

- The Nature-based account describes model collapse as progressive loss of distribution tails and reports OPT-125m experiments in which purely synthetic training increased perplexity by 20–28 points after five epochs. [S3]
- Other sources warn that repeated training on outputs from earlier models can lead to stylistic homogenization, loss of edge cases, factual drift, and fluent but brittle outputs. [S1] [S5] [S13]

### Finding 5

**Claim**

Synthetic data may reproduce or amplify biases in the generator, seed data, prompts, or evaluation process; generating more examples for underrepresented groups does not by itself establish fairness.

**Confidence:** Medium

**Why this confidence level**

The mechanism and risk are well supported conceptually, but the accumulated sources do not provide a controlled study measuring demographic, dialect, cultural, or domain-specific bias changes after synthetic fine-tuning.

**Evidence**

- Sources warn that generated data reflects the properties of its source distribution and that missing groups or edge cases in seed data may not be recoverable through generation alone. [S4] [S13]
- The evidence base identifies bias and distribution mismatch as risks, while a promotional source claims bias reduction without supplying comparative subgroup measurements. [S5] [S12]

### Finding 6

**Claim**

Synthetic evaluation sets and LLM-generated judgments can systematically distort measured performance.

**Confidence:** High

**Why this confidence level**

S6 reports a direct empirical comparison with human queries and judgments and statistical analysis, although its generality beyond information retrieval is uncertain.

**Evidence**

- An empirical IR study found that synthetic queries differed from human queries, including longer queries and different question-type distributions; GPT-4 relevance judgments were about 0.28 points higher on average than human judgments, leading to leniency and performance overestimation. [S6]
- The same study indicates that synthetic-evaluation bias may affect absolute performance estimates more than relative system comparisons, though effects depend on query characteristics, judge type, and system architecture. [S6]

### Finding 7

**Claim**

Synthetic evaluation can expand coverage of edge cases, adversarial scenarios, ambiguity, multi-turn behavior, calibration, and robustness, but it should not replace independent human-authored or deployment-derived evaluation.

**Confidence:** High

**Why this confidence level**

The recommendation is supported by both procedural guidance and empirical evidence of synthetic evaluation bias.

**Evidence**

- Synthetic test generation is described as a way to probe ambiguous queries, multi-turn context, failure modes, decision boundaries, and adversarial behavior. [S4]
- Sources recommend real or independently authored holdouts because synthetic validation can conceal the same generator-specific failure modes present in training data. [S10] [S13]
- Benchmark contamination, leakage, saturation, overfitting, and poor correspondence to real-world behavior are identified as broader evaluation risks. [S3] [S5] [S6]

### Finding 8

**Claim**

Fairness evaluation should examine subgroup-specific performance and uncertainty, not only aggregate accuracy or conventional discrete fairness metrics.

**Confidence:** Medium

**Why this confidence level**

These sources support evaluation methodology, but they do not directly measure the causal effect of synthetic training data on fairness.

**Evidence**

- The UCerF work argues that conventional accuracy-based fairness metrics can miss unequal confidence in incorrect predictions and introduces uncertainty-aware evaluation across a gender-occupation dataset. [S9]
- A clinical extraction study found modest performance differences across race/ethnicity and age groups, while external verification and replicated clinical outcomes were broadly consistent with human-abstracted data. [S7]

### Finding 9

**Claim**

Synthetic data can offer privacy benefits, but synthetic outputs should not automatically be treated as anonymous or compliant.

**Confidence:** Medium

**Why this confidence level**

The potential benefit and residual risk are both supported, but empirical privacy guarantees for particular generation methods are not established here.

**Evidence**

- Sources describe synthetic medical and financial data as a potential way to preserve useful patterns without directly exposing individual records. [S3] [S4]
- The same evidence notes that re-identification remains relevant where linkage or memorization is plausible, and provides no dataset-specific leakage or re-identification rates. [S3]

### Finding 10

**Claim**

The most defensible operational strategy is to supplement, not replace, curated real data; preserve provenance; filter and deduplicate aggressively; and evaluate factuality, diversity, subgroup performance, uncertainty, and real-world generalization separately.

**Confidence:** High

**Why this confidence level**

The control framework is consistent across the accumulated evidence, although the optimal synthetic-to-real ratio and effectiveness of individual safeguards remain unresolved.

**Evidence**

- Sources recommend retaining a non-shrinking anchor of human-generated data, tracking the proportion of AI-generated content, and preventing recursive replacement of real examples. [S3] [S13]
- Recommended controls include lineage and fidelity metadata, independent judging, rubric-based quality scoring, format and toxicity checks, deduplication, and external or human validation. [S1] [S5] [S14]
- Independent real or deployment-derived holdouts are recommended because standard training metrics and synthetic validation sets may not predict the target task or real-world behavior. [S6] [S10] [S13]

## Conflicts and Uncertainty

- Some sources present synthetic data as broadly enabling privacy, compliance, bias reduction, and domain accuracy, while the stronger accumulated evidence treats these outcomes as conditional and requiring leakage, subgroup, and deployment validation. The promotional claims are not supported by comparative measurements. [S12] [S3] [S4] [S5]
- Sources agree that retaining real data and accumulating synthetic data is safer than recursively replacing real data, but they do not establish a universally safe synthetic-to-real ratio across model sizes, tasks, or training regimes. [S3] [S5] [S8] [S13]
- Synthetic evaluation bias may sometimes affect absolute scores more than relative rankings, but broader sources warn that contamination, overfitting, architecture interactions, and distribution mismatch can also undermine comparisons. [S6] [S3] [S5]
- A Databricks case study reports near-baseline performance from a smaller fine-tuned model, but the retrieved passage does not contain the promised results from synthetic-data augmentation; therefore it does not establish that synthetic data caused an improvement. [S10]
- Several strong quantitative claims in practitioner sources—such as specific collapse thresholds or the consistent superiority of a particular number of validated examples—lack study designs or independently verified primary evidence in the accumulated material. [S8] [S13]
- The evidence on fairness methods comes mainly from evaluation or extraction settings rather than matched experiments comparing synthetic-data fine-tuning with real-data fine-tuning. Thus, the direction and size of fairness effects remain uncertain. [S6] [S7] [S9]

## Remaining Gaps

- Controlled comparisons of synthetic-only, real-only, and mixed training for the same LLM task and data budget.
- Measured changes in demographic, dialect, cultural, and domain-specific bias after synthetic fine-tuning.
- Quality metrics that reliably predict independent real-world performance, especially factuality, label correctness, diversity, novelty, calibration, and distributional fidelity.
- Evidence on how often synthetic benchmarks agree with human-authored or deployment-derived evaluations outside information retrieval.
- Validated synthetic-to-real mixing requirements for different model sizes, tasks, and recursive training regimes.
- Dataset-specific memorization, privacy leakage, and re-identification testing procedures and results.
- Complete results from the Databricks synthetic-augmentation case study and statistically robust replication of similar practitioner reports.
- Evidence on the reliability and independence of LLM-as-judge systems when generator and judge share factual or stylistic biases.

## Conclusion

Synthetic data is best viewed as a controlled augmentation and distillation tool, not a drop-in replacement for real data. Its practical benefits—scale, lower annotation burden, targeted coverage, privacy-sensitive prototyping, and potentially cheaper specialized models—are credible but highly dependent on data quality and task fit. The principal real-world risks are recursive distribution collapse, loss of rare cases, inherited or amplified bias, factual hallucination, privacy overconfidence, and evaluation results that reward similarity to the generator rather than real-world usefulness. Organizations should retain representative human or real-world data, document provenance, filter and deduplicate generated examples, test subgroup performance and uncertainty, and use independent human-authored or deployment-derived holdouts. The accumulated research does not yet establish how synthetic fine-tuning changes fairness or real-world performance relative to matched real-data baselines, so claims of automatic bias reduction, privacy, or superior accuracy remain unproven.

## Sources

- [S1] Synthetic Data for AI Training: Use Cases and Risks [2026] — https://atlan.com/know/ai-agent/data-for-ai/synthetic-data-for-ai-training
- [S2] Using Synthetic Data to Improve LLM Fine‑Tuning | newline — https://www.newline.co/@Dipen/using-synthetic-data-to-improve-llm-finetuning--d453f658
- [S3] Synthetic Data for LLM Training: Decision Guide 2026 — https://www.digitalapplied.com/blog/synthetic-data-generation-llm-training-decision-guide-2026
- [S4] Synthetic Data Generation with LLMs: Techniques and Use Cases — https://tetrate.io/learn/ai/synthetic-data-generation-llms
- [S5] Large Language Models Are Still Getting Stronger, but Researchers Face New Bottlenecks in Data, Evaluation, and Safety | Newswise — https://www.newswise.com/articles/large-language-models-are-still-getting-stronger-but-researchers-face-new-bottlenecks-in-data-evaluation-and-safety
- [S6] Towards Understanding Bias in Synthetic Data for Evaluation | alphaXiv — https://www.alphaxiv.org/abs/2506.10301
- [S7] Fairness by design: End-to-end bias evaluation for LLM-generated data — https://resources.flatiron.com/publications/fairness-by-design-end-to-end-bias-evaluation-for-llm-generated-data
- [S8] Synthetic Training Data Quality Collapse: How Feedback Loops Destroy Your Fine-Tuned Models — https://tianpan.co/blog/2026-04-09-synthetic-training-data-quality-collapse
- [S9] Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs - Apple Machine Learning Research — https://machinelearning.apple.com/research/fairly-certain
- [S10] Medium — https://medium.com/@hiydavid/structured-extraction-with-llm-on-databricks-part-2-fine-tuning-with-synthetic-data-021cc4b1776b
- [S11] Synthetic Data for LLM Fine-Tuning — https://apxml.com/courses/synthetic-data-llm-pretrain-finetune/chapter-4-llm-fine-tuning-synthetic-data-enhancement
- [S12] LLM & SLM Fine-Tuning with Synthetic Data | DataXID — https://www.dataxid.com/solutions/llm-fine-tuning
- [S13] Synthetic Data Pipelines for Domain-Specific LLM Fine-Tuning — https://tianpan.co/blog/2026-03-04-synthetic-data-pipelines-domain-llm-fine-tuning
- [S14] Synthetic Data for Fine-Tuning: How to Generate Your Own Training Set — ai.rs — https://ai.rs/ai-developer/synthetic-data-for-fine-tuning
