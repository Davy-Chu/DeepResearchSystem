# Research Report

## Research Question

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

## Summary

Synthetic data is most defensible as curated augmentation rather than a wholesale replacement for human or real-world data. It can reduce data-collection costs, scale task-specific examples, address class imbalance, and cover rare or privacy-sensitive cases. However, generated examples may contain factual errors, artificial regularities, domain mismatch, and inherited bias. Recursive, single-source, or predominantly synthetic training can narrow linguistic diversity and harm generalization. Evaluation therefore needs to examine both the synthetic dataset and the resulting model against independent, held-out human or real-world evidence.

## Findings

### Finding 1

**Claim**

Synthetic data provides operational benefits when human data is scarce, costly, privacy-sensitive, difficult to label, or missing rare and underrepresented cases.

**Confidence:** High

**Why this confidence level**

This benefit is consistently reported across the accumulated sources, although many supporting sources are surveys, practitioner guidance, or industry material rather than independently replicated controlled comparisons.

**Evidence**

- Sources describe synthetic data as useful for task-specific augmentation, class balancing, niche domains, rapid prototyping, low-resource tasks, privacy-constrained settings, and rare or edge-case coverage. [S2] [S5] [S6] [S9] [S12] [S16] [S20] [S21]

### Finding 2

**Claim**

Synthetic-data quality is not guaranteed by volume; factuality, realism, diversity, novelty, task alignment, and external verifiability determine whether it improves downstream performance.

**Confidence:** High

**Why this confidence level**

Multiple sources converge on the same quality requirements and failure modes, though no universal quality threshold is established.

**Evidence**

- Sources identify hallucinations, factual errors, inconsistency, irrelevant content, domain mismatch, insufficient realism, and loss of human linguistic nuance as failure modes. Recommended controls include filtering, reweighting, consistency checks, retrieval, refinement, curation, and verification. [S3] [S8] [S11] [S12] [S16] [S20] [S21]
- Automatically verifiable tasks such as executable code offer stronger validation than open-ended natural-language behavior, where correctness and realism are harder to establish independently. [S10] [S16] [S20]

### Finding 3

**Claim**

Recursive, single-source, or predominantly synthetic training can narrow the learned distribution, reduce linguistic diversity, and impair generalization to human text.

**Confidence:** High

**Why this confidence level**

The core risk has direct empirical support and is corroborated by multiple reviews and summaries.

**Evidence**

- An empirical study reports reductions in lexical, semantic, and syntactic diversity and poorer modeling of human text under recursive synthetic-data training. [S2] [S4]
- Other sources describe model collapse, simplification of the original distribution, and degraded or increasingly nonsensical outputs after repeated synthetic training. [S18] [S19] [S20]

### Finding 4

**Claim**

Retaining real data and using diverse, independently sourced synthetic data may reduce collapse risk, but no universal safe synthetic-data percentage or mixture has been established.

**Confidence:** High

**Why this confidence level**

The mitigation pattern and regime dependence are supported, while the amount of synthetic data that is safe remains unresolved.

**Evidence**

- The reported evidence indicates that diverse source models and additive mixtures retaining real data preserve more distributional breadth than single-source or replacement regimes. [S4] [S7]
- Reports of collapse with a small synthetic fraction arise under particular datasets and training conditions and do not establish a universal threshold. [S14] [S15] [S4] [S7]

### Finding 5

**Claim**

Synthetic data can reproduce or amplify bias from its source data or generator; controlled generation may improve representation, but fairness gains must be demonstrated downstream rather than assumed.

**Confidence:** Medium

**Why this confidence level**

The conditional risk-benefit pattern is consistent, but direct comparative measurements of demographic fairness remain limited.

**Evidence**

- Sources describe potential benefits such as class balancing, low-resource-language support, and targeted representation, while warning about inherited bias, demographic underrepresentation, and bias amplification. [S5] [S6] [S9] [S11] [S12] [S16] [S20] [S21]
- One empirical study reports self-preference and safety-related effects after synthetic fine-tuning, without establishing broad demographic fairness improvements. [S4]

### Finding 6

**Claim**

Synthetic fine-tuning can improve apparent output quality or benchmark performance while worsening adversarial robustness, safety, or real-world generalization.

**Confidence:** High

**Why this confidence level**

The quality-versus-robustness tradeoff is directly reported, and several sources caution against relying on narrow benchmark scores.

**Evidence**

- An empirical study reports higher output quality alongside reduced adversarial robustness after synthetic fine-tuning. [S4]
- Reviews warn that benchmark saturation or contamination, overfitting to artificial scenarios, and missing real-world nuance can make benchmark gains poor proxies for deployment reliability. [S3] [S11] [S13] [S18]

### Finding 7

**Claim**

Synthetic data may reduce direct exposure to human records, but synthetic status alone does not guarantee privacy, legal safety, or clean provenance.

**Confidence:** Medium

**Why this confidence level**

Both potential benefit and risk are represented, but the supplied material lacks systematic privacy measurements and definitive legal conclusions.

**Evidence**

- Sources present reduced direct exposure as a potential privacy benefit while identifying leakage, memorization, re-identification, provenance, and possible proprietary-content overlap as unresolved risks. [S5] [S6] [S9] [S11] [S13] [S17] [S18]

### Finding 8

**Claim**

The most defensible evaluation regime separately assesses the synthetic dataset and the downstream model using independent, held-out human or real-world evidence.

**Confidence:** High

**Why this confidence level**

Evaluation requirements are consistent across the accumulated sources, although no single protocol is proven to predict every deployment outcome.

**Evidence**

- Dataset checks should cover fidelity, factuality, realism, diversity, representativeness, bias, contamination, and task alignment. [S3] [S5] [S8] [S16] [S20] [S21]
- Model checks should include real-world generalization, robustness, adversarial behavior, safety, contamination, evaluator self-preference, and realistic multi-step performance—not only benchmark accuracy. [S3] [S4] [S16] [S18] [S20] [S21]
- Human, external, or independently verifiable checks are needed because generators and model-based evaluators may share errors or biases. [S4] [S5] [S8] [S10] [S11]

## Conflicts and Uncertainty

- Synthetic data is described both as improving diversity, representation, and coverage and as causing distribution narrowing and collapse. The evidence is conditional: curated, diverse, externally checked data may help, whereas recursive, single-source, or unverified data can worsen outcomes. [S2] [S4] [S5] [S7] [S20] [S21]
- Industry and practitioner sources present synthetic data as potentially improving fairness, privacy, and performance, while empirical and review evidence documents bias amplification, weakened robustness, collapse, and privacy leakage. The sources do not establish universal benefits or harms. [S4] [S5] [S6] [S9] [S11] [S17] [S18] [S20] [S21]
- Reports of collapse from a small synthetic fraction coexist with evidence that retaining real data and using diverse sources can mitigate collapse. These findings likely depend on datasets, model sizes, source models, and training procedures; no universal threshold is supported. [S4] [S7] [S14] [S15]
- Model-in-the-loop or benchmark evaluation can assist curation, but evaluators may share errors or biases with generators and miss adversarial or real-world failures. Such methods should supplement, not replace, independent human, external, and held-out testing. [S3] [S4] [S5] [S8] [S10] [S11]

## Remaining Gaps

- How synthetic datasets compare with equivalent amounts of high-quality human-curated data across model sizes, languages, domains, and deployment tasks.
- What synthetic-to-real mixture, source diversity, filtering, and deduplication strategy best preserves linguistic diversity and prevents collapse.
- Which independent methods reliably measure demographic fairness, factuality, shared generator/evaluator errors, adversarial robustness, and real-world distribution shift.
- What quantitative tests should detect privacy leakage, memorization, re-identification, provenance, and intellectual-property overlap.
- Whether reported adversarial-robustness and self-preference effects replicate across more models, languages, tasks, and deployment settings.
- How much independently validated human data is needed for open-ended natural-language fine-tuning.

## Conclusion

Synthetic data can be valuable for scaling and targeting LLM training, particularly where human data is scarce, expensive, sensitive, or unable to cover rare cases. Its benefits are not automatic: poor factuality, realism, bias, source narrowness, or insufficient validation can produce models that score well in controlled tests but generalize poorly or become less robust. The accumulated evidence supports using synthetic data as carefully curated, diverse augmentation alongside retained real or human data, with independent validation and deployment-oriented testing. The research stopped at the iteration limit, so the unresolved quantitative questions—especially safe mixture proportions, demographic fairness effects, privacy leakage, and generalization gains—should not be treated as answered.

## Sources

- [S1] Using Synthetic Data to Improve LLM Fine‑Tuning | newline — https://www.newline.co/@Dipen/using-synthetic-data-to-improve-llm-finetuning--d453f658
- [S2] Synthetic Data for AI Training: Use Cases and Risks [2026] — https://atlan.com/know/ai-agent/data-for-ai/synthetic-data-for-ai-training
- [S3] Large Language Models Are Still Getting Stronger, but Researchers Face New Bottlenecks in Data, Evaluation, and Safety | Newswise — https://www.newswise.com/articles/large-language-models-are-still-getting-stronger-but-researchers-face-new-bottlenecks-in-data-evaluation-and-safety
- [S4] Synthetic Eggs in Many Baskets:The Impact of Synthetic Data Diversity on LLM Fine-Tuning — https://arxiv.org/html/2511.01490v1
- [S5] Synthetic Data for ML: Uses, Risks, and Best Practices | CleverX Blog — https://cleverx.com/blog/synthetic-data-for-ml-the-game-changer-in-training-for-2025
- [S6] Synthetic Data Generation with LLMs: Techniques and Use ... — https://tetrate.io/learn/ai/synthetic-data-generation-llms
- [S7] Synthetic Data for LLM Training: Decision Guide 2026 — https://www.digitalapplied.com/blog/synthetic-data-generation-llm-training-decision-guide-2026
- [S8] On LLMs-Driven Synthetic Data Generation, Curation, and Evaluation: A Survey | alphaXiv — https://www.alphaxiv.org/abs/2406.15126
- [S9] What Is LLM Synthetic Data? Benefits & Key Uses — https://deepchecks.com/question/llm-synthetic-data-use-cases
- [S10] [D] Is Synthetic Data a Reliable Option for Training ... — https://www.reddit.com/r/MachineLearning/comments/1bosj2t/d_is_synthetic_data_a_reliable_option_for
- [S11] LLM synthetic data: Fine-tuning LLMs with AI-generated data | SuperAnnotate — https://www.superannotate.com/blog/llm-synthetic-data
- [S12] How to Generate Synthetic Data and Fine-Tune a Small Language ... — https://blog.monsterapi.ai/how-to-generate-synthetic-data-and-fine-tune-a-small-language-model-slm-on-monsterapi
- [S13] The Dangers and Risks of Depending on Synthetic Data from Large Language Models — https://www.linkedin.com/pulse/dangers-risks-depending-synthetic-data-from-large-language-jdihf
- [S14] This AI Paper from Meta AI Highlights the Risks of Using Synthetic Data to Train Large Language Models - MarkTechPost — https://www.marktechpost.com/2024/10/16/this-ai-paper-from-meta-ai-highlights-the-risks-of-using-synthetic-data-to-train-large-language-models?amp=
- [S15] This AI Paper from Meta AI Highlights the Risks of Using Synthetic Data to Train Large Language Models - MarkTechPost — https://www.marktechpost.com/2024/10/16/this-ai-paper-from-meta-ai-highlights-the-risks-of-using-synthetic-data-to-train-large-language-models
- [S16] Synthetic Data Generation Using Large Language Models: Advances in Text and Code (2025) – MECO — https://www.cs.ubbcluj.ro/~meco/synthetic-data-generation-using-large-language-models-advances-in-text-and-code-2025
- [S17] Synthetic Data and the Future of AI: The 2026 Expert Guide - Riseup Labs — https://riseuplabs.com/synthetic-data-and-the-future-of-ai
- [S18] Examining synthetic data: The promise, risks and realities | IBM — https://www.ibm.com/think/insights/ai-synthetic-data
- [S19] The Prominence of Synthetic Data, and Why It Will Expand Rather Than Replace Real Data - Dataversity — https://www.dataversity.net/articles/the-prominence-of-synthetic-data-and-why-it-will-expand-rather-than-replace-real-data
- [S20] Synthetic Data Generation Using Large Language Models: Advances in Text and Code — https://arxiv.org/html/2503.14023v2
- [S21] Best Practices and Lessons Learned on Synthetic Data for Language Models — https://arxiv.org/html/2404.07503v1
