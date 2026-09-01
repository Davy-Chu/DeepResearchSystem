# Research Report

## Research Question

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

## Summary

Synthetic data is most defensible as curated supplementation or targeted augmentation, not as an uncritical replacement for real data. It can expand scarce resources, support domain adaptation, cover rare cases, and enable controlled experimentation. However, recursive or large-scale replacement with model-generated data can narrow distributions, reduce diversity, and propagate errors or artifacts. Synthetic data may target underrepresented categories, but it does not inherently improve demographic, linguistic, cultural, or intersectional fairness; biases from source models and synthetic material can persist or intensify. Evaluation must therefore go beyond benchmark gains and include factuality, generalization, robustness, safety, fairness, contamination, distribution shift, and validation against human or real-world data. The ledger does not establish a general causal comparison between synthetic and real data across training roles, nor a validated end-to-end evaluation or privacy methodology.

## Findings

### Finding 1

**Claim**

Curated synthetic augmentation can provide practical benefits by expanding scarce training resources, generating domain- or task-specific examples, covering rare or edge cases, addressing class imbalance, and supporting privacy-sensitive or rapid-prototyping workflows.

**Confidence:** Medium

**Why this confidence level**

The ledger provides multiple direct and indirect examples of utility, but the evidence is heterogeneous, and language-specific quality failures and limited controlled comparisons constrain generalization.

**Evidence**

- Synthetic data is described as useful for augmentation, rare-case generation, class-imbalance mitigation, privacy-sensitive development, domain adaptation, and rapid prototyping. [S4]
- Curated synthetic textbooks and exercises supplemented real data in Phi-1 training and were associated with strong coding-benchmark results; synthetic data was also described as useful for edge-case augmentation. [S1]
- LLM-based augmentation is reported as useful for low-resource and cross-lingual tasks and for targeted task-specific example generation, subject to filtering. [S12]
- Synthetic datasets support controlled experimentation, edge-case coverage, debugging, and repeatable evaluation or golden datasets. [S15]

### Finding 2

**Claim**

Replacing real data with recursively generated synthetic data can cause model collapse, including loss of low-probability or tail-distribution content, reduced diversity, and degraded performance. Retaining or accumulating real data is presented as a mitigation.

**Confidence:** High

**Why this confidence level**

The ledger includes direct evidence from synthetic fine-tuning and supporting evidence about recursive training. The risk is conditional on recursive or substantial replacement use and should not be generalized to curated supplementation.

**Evidence**

- Indiscriminate iterative use of model-generated content is associated with irreversible defects and loss of distribution tails; purely synthetic self-training produced perplexity degradation in the reported OPT-125m example. [S1]
- Recursive synthetic training is described as narrowing distributions and degrading outputs. [S2]
- Synthetic fine-tuning is reported to produce distribution collapse and reduced linguistic diversity, with greater diversity of source models mitigating these effects. [S13]

### Finding 3

**Claim**

Synthetic-data quality depends on generation and curation—not volume alone. Filtering, deduplication, diversity controls, validation, and alignment with the target distribution are material conditions; uncurated generation can amplify errors, repetition, linguistic defects, and other artifacts.

**Confidence:** High

**Why this confidence level**

Several sources directly identify curation, validation, language coverage, and source diversity as determinants of quality, although the ledger does not establish optimal quality-control settings across all LLM applications.

**Evidence**

- Curated data, deduplication, and quality filtering are contrasted with indiscriminate generation, where additional volume can amplify failure modes. [S1]
- Utility is described as depending on generation methods, validation, and alignment between synthetic and target distributions. [S4]
- Novelty, reliability, verifiability, and external feedback are identified as requirements; repeated training without new information can stagnate or degrade capabilities. [S5]
- Low-resource-language generations are reported to include redundancy, repetition, linguistic errors, and poor comprehensibility; human review and logical-consistency filters are proposed mitigations. [S12]
- Source composition and source-model diversity affect distribution collapse, linguistic diversity, and adversarial robustness. [S13]

### Finding 4

**Claim**

Synthetic data can target underrepresented classes or scenarios and may improve representation of selected categories, but this does not establish broader demographic, linguistic, cultural, or intersectional fairness.

**Confidence:** Medium

**Why this confidence level**

The evidence supports targeted representation benefits and meaningful limitations, but no supplied source provides a direct controlled subgroup-level comparison establishing general demographic, cultural, linguistic, or intersectional fairness gains.

**Evidence**

- Generating additional examples for underrepresented classes is described as a possible class-imbalance and robustness intervention. [S4]
- Synthetic data may mirror real distributions and address class imbalance. [S2]
- Augmentation and resampling are reviewed as possible data-level bias mitigations, with important limitations. [S6]
- Multilingual and low-resource augmentation is associated with performance improvements in some settings, while persistent quality and language-bias problems are reported for some underrepresented languages. [S12]
- Iterative synthetic training can lose distribution tails, potentially undermining rare-group or rare-case representation when those tails are not deliberately preserved. [S1]

### Finding 5

**Claim**

Synthetic-data fine-tuning does not automatically remove foundation-model bias. Pre-existing biases may persist, while biases in fine-tuning material can be added or intensified; deliberate configuration of demographic perspectives is not evidence of improved fairness without outcome-level evaluation.

**Confidence:** Medium

**Why this confidence level**

The ledger supports persistence and possible amplification of bias, but does not directly compare demographic fairness outcomes for synthetic versus real fine-tuning across populations and applications.

**Evidence**

- Foundation-model biases are reported to persist through fine-tuning and may be extended by biases in fine-tuning materials; deliberate fine-tuning can also make models express demographic biases. [S9]
- Augmentation quality and language bias depend on the generating model and require filtering. [S12]
- Source-model diversity affects fine-tuned behavior and self-preference bias; human data reduced self-preference more strongly than single-source synthetic data in the reported study. [S13]

### Finding 6

**Claim**

Synthetic-data diversity is a material condition for safer LLM fine-tuning: multiple source models can mitigate distribution collapse and preserve broader output and linguistic diversity relative to single-source synthetic data, although downstream safety risks remain.

**Confidence:** Medium

**Why this confidence level**

The evidence comes from one reported study and does not establish how broadly the result generalizes across models, datasets, or training roles; it also indicates that diversity improvements do not eliminate safety risks.

**Evidence**

- The reported study links source diversity with distributional and diversity effects, while also finding that synthetic fine-tuning decreased adversarial robustness despite preserving output quality—making outputs potentially more usable and dangerous. [S13]

### Finding 7

**Claim**

Benchmark gains from synthetic-data training are insufficient by themselves to establish real-world improvement. Evaluation should test generalization, factuality, robustness, safety, fairness, contamination, distribution shift, and realistic task performance.

**Confidence:** High

**Why this confidence level**

The ledger combines direct evidence on benchmark limitations, intersectional disparities, and distributional or robustness changes. It does not provide a single validated protocol covering every relevant risk.

**Evidence**

- Benchmark saturation and contamination can make scores misleading; realistic evaluation should include reliability, safety, robustness, fairness, and complex tasks. [S5]
- Synthetic evaluation sets can target edge cases, adversarial examples, ambiguity, multi-turn context, calibration, and robustness, but their role has distinct failure modes including evaluation overfitting. [S4] [S1]
- High-stakes resume-screening evaluation revealed intersectional gender and racial disparities that aggregate capability scores would not establish. [S7]
- Truthfulness and hallucination evaluations, as well as bias-focused evaluation, are needed because common capability benchmarks do not address all training-data or response biases. [S9]
- Bias evaluation must examine data, models, outputs, demographic attributes, and application contexts. [S6]
- Standard performance benchmarks can miss distributional narrowing, robustness changes, and self-preference effects in synthetic fine-tuning. [S13]
- Synthetic evaluation or golden datasets should be validated for objectives and input breadth rather than assumed to be representative. [S15]

### Finding 8

**Claim**

Synthetic test collections can introduce systematic evaluation bias: LLM-generated queries and relevance judgments may differ from human data and judgments, potentially overestimating absolute system performance even when relative comparisons are less affected.

**Confidence:** Medium

**Why this confidence level**

The evidence is empirical but concerns information-retrieval test collections rather than direct evaluation of synthetic-data training interventions, limiting generalization.

**Evidence**

- Synthetic queries differed systematically from human queries, and LLM relevance judgments were more lenient; the reported effects were larger for absolute performance estimates than for relative system comparisons. [S11]

## Conflicts and Uncertainty

- The ledger contains no formally conflicting claim statuses, but evidence is conditional and heterogeneous: targeted augmentation can improve selected tasks or categories, while recursive replacement, poor curation, single-source generation, or low-resource-language generation can reduce diversity, quality, fairness, or robustness. [S1] [S4] [S12] [S13]
- The evidence does not establish that synthetic data improves broad demographic, linguistic, cultural, or intersectional fairness, even where it improves representation of selected classes or task performance. [S4] [S6] [S9] [S12]
- The evidence does not establish a validated evaluation methodology that jointly controls for contamination, synthetic-evaluation bias, leakage, distribution shift, privacy, safety, and real-world performance. [S5] [S11] [S15]

## Remaining Gaps

- G1: No supplied source provides direct, controlled subgroup-level evaluations of demographic, linguistic, cultural, or intersectional fairness effects, including whether targeted augmentation improves outcomes without creating new disparities.
- G2: No supplied source directly compares synthetic and real data across pretraining, continued training, instruction fine-tuning, and domain adaptation while jointly measuring factuality, diversity, coverage, noise, artifacts, and downstream failures.
- G3: No supplied source establishes a validated end-to-end evaluation methodology that jointly controls for benchmark contamination, synthetic-evaluation bias, data leakage, distribution shift, privacy, safety, and real-world task performance.
- G4: The privacy benefit of synthetic substitution remains unresolved because re-identification, memorization, privacy-leakage, and regulatory validation results are not supplied.

## Conclusion

The ledger supports a conditional rather than categorical conclusion. Synthetic data offers real operational benefits when it supplements real data or is deliberately targeted, curated, validated, and matched to the intended distribution. The main quality risk is uncontrolled self-training or replacement, which can amplify errors and narrow diversity. The main fairness risk is assuming that targeted synthetic examples or improved aggregate performance imply broad fairness; source-model and generation biases may persist or intensify. The main evaluation risk is mistaking gains on synthetic, contaminated, narrow, or biased benchmarks for real-world improvement. In practice, claims of benefit should be supported by role-specific comparisons against real-data baselines, subgroup and intersectional testing, factuality and robustness checks, contamination and leakage controls, human-validated evaluation data, and shifted or realistic task tests. The supplied evidence does not yet resolve which training roles or use cases reliably outperform real-data alternatives, nor whether synthetic substitution provides validated privacy protection.

## Sources

- [S1] Synthetic Data for LLM Training: Decision Guide 2026 — https://www.digitalapplied.com/blog/synthetic-data-generation-llm-training-decision-guide-2026
- [S2] Synthetic Data for AI Training: Use Cases and Risks [2026] — https://atlan.com/know/ai-agent/data-for-ai/synthetic-data-for-ai-training
- [S3] Using Synthetic Data to Improve LLM Fine‑Tuning | newline — https://www.newline.co/@Dipen/using-synthetic-data-to-improve-llm-finetuning--d453f658
- [S4] Synthetic Data Generation with LLMs: Techniques and Use Cases — https://tetrate.io/learn/ai/synthetic-data-generation-llms
- [S5] Large Language Models Are Still Getting Stronger, but ... — https://www.newswise.com/articles/large-language-models-are-still-getting-stronger-but-researchers-face-new-bottlenecks-in-data-evaluation-and-safety
- [S6] Bias in Large Language Models: Origin, Evaluation, and Mitigation — https://arxiv.org/html/2411.10915v1
- [S7] Measuring gender and racial biases in large language models: Intersectional evidence from automated resume evaluation — https://pmc.ncbi.nlm.nih.gov/articles/PMC11937954
- [S8] Tackling bias in large ML models: the role of synthetic data — https://syntheticus.ai/blog/tackling-bias-in-large-ml-models-the-role-of-synthetic-data
- [S9] Capturing Bias Diversity in LLMs — https://doras.dcu.ie/30827/1/Capturing_Bias_Diversity_in_LLMs.pdf
- [S10] Bias Mitigation via Synthetic Data Generation: A Review — https://www.mdpi.com/2079-9292/13/19/3909
- [S11] Towards Understanding Bias in Synthetic Data for Evaluation | alphaXiv — https://www.alphaxiv.org/abs/2506.10301
- [S12] LLM-Based Data Augmentation — https://www.emergentmind.com/topics/llm-based-data-augmentation
- [S13] The Impact of Synthetic Data Diversity on LLM Fine-Tuning — https://arxiv.org/html/2511.01490v1
- [S14] GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub — https://github.com/pengr/LLM-Synthetic-Data
- [S15] Creating and Validating Synthetic Datasets for LLM Evaluation & Experimentation - Arize AI — https://arize.com/blog/creating-and-validating-synthetic-datasets-for-llm-evaluation-experimentation
