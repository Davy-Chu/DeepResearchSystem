# Research Report

## Research Question

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

## Summary

Synthetic data offers a conditional benefit rather than a universally safe substitute for natural or human-labeled data. It can expand scarce task-specific datasets, cover selected edge cases, support specialized skills, and reduce annotation bottlenecks. The strongest evidence favors task-shaped, quality-filtered, source-diverse synthetic data used additively with retained natural data. The main risks are factual and distributional errors, inherited or amplified bias, loss of rare or minority cases through recursive training, weakened adversarial robustness, and misleading evaluation caused by contaminated or model-biased test sets. Evidence remains insufficient to determine how synthetic text affects demographic fairness, factuality, privacy, or deployment reliability across LLMs in general.

## Findings

### Finding 1

**Claim**

Synthetic data can reduce data bottlenecks and provide useful task-specific training signal when real or labeled data are scarce, costly, private, or difficult to collect.

**Confidence:** Medium

**Why this confidence level**

The benefit is consistently supported, including by a controlled multi-task SFT comparison, but most evidence is practitioner or survey material and does not establish broad deployment gains or matched cost savings.

**Evidence**

- Sources describe applications including instruction and preference tuning, low-resource tasks, domain adaptation, edge-case generation, tool-use training, class-imbalance mitigation, and privacy-constrained development. [S3] [S4] [S15] [S29] [S30] [S32]
- A controlled SFT study across mathematics, question answering, and Text2SQL found that the most effective generation strategy varied with the available query and seed-data budget. [S15]

### Finding 2

**Claim**

Data quality depends more on task relevance, diversity, verification, and curation than on synthetic volume alone.

**Confidence:** Medium

**Why this confidence level**

The operational pattern is consistent across sources, but component-level ablations and independent comparisons are limited.

**Evidence**

- Sources recommend task-shaped generation, seed or real-data anchoring, deduplication, filtering, statistical checks, human review, and external verification such as execution tests for code or calculators for mathematical outputs. [S2] [S4] [S29] [S30] [S32]
- DS2-Instruct describes keyword-based domain coverage, cognitive-level diversification, retrieval augmentation, and self-consistency filtering as components of a domain-specific synthesis pipeline. [S28]

### Finding 3

**Claim**

Recursive, single-source, or replacement-heavy use of synthetic data can narrow the learned distribution and remove low-probability, rare, or minority examples; retaining natural data and adding novel synthetic data is safer.

**Confidence:** High

**Why this confidence level**

The regime-dependent distinction is supported by primary research and multiple reviews, although precise safe mixture ratios and generation limits remain unknown.

**Evidence**

- Research and review sources describe model-collapse effects including reduced linguistic diversity, loss of distribution tails, and degradation when models repeatedly train on generated outputs. [S1] [S2] [S6] [S14] [S32]
- A newer study reports that heterogeneous-model interactions can introduce useful novel concepts, but repeated or insufficiently novel interactions can homogenize performance; it distinguishes additive mixtures from discarding original data. [S34]

### Finding 4

**Claim**

Source diversity can mitigate some distribution-collapse effects, but it does not eliminate other risks such as weakened adversarial robustness or evaluator bias.

**Confidence:** High

**Why this confidence level**

This is direct peer-reviewed evidence, though it focuses mainly on supervised fine-tuning and one study’s experimental settings.

**Evidence**

- The ACL study found that greater diversity among synthetic-data sources preserved broader output and linguistic diversity and mitigated several measures of distribution collapse. [S14]
- The same study found reduced adversarial robustness after synthetic fine-tuning and weaker reduction of self-preference bias for single-source synthetic data than for human or multi-source data. [S14]

### Finding 5

**Claim**

Synthetic data can reproduce or amplify generator, source-data, prompt, and filtering biases; nominally increasing representation does not demonstrate fair or culturally accurate representation.

**Confidence:** Medium

**Why this confidence level**

There is direct evidence that LLM-generated social representations are uneven and consistent evidence of bias mechanisms, but no retrieved controlled intervention measures the demographic effects of synthetic text fine-tuning itself.

**Evidence**

- Sources identify bias amplification and demographic underrepresentation as risks and recommend targeted generation only as part of an audit-and-retraining loop. [S3] [S4] [S9]
- An audit of LLM-simulated public opinion found substantially better reproduction of U.S. than Chilean survey responses and different disparities across race, political identity, gender, education, and religion. [S13]
- Fairness resources emphasize group, counterfactual, probability-based, embedding-based, and generation-based measures, while noting that fairness is use-case dependent. [S11]

### Finding 6

**Claim**

Fairness improvements from synthetic augmentation are possible in principle but are not established for LLM training and may involve utility or domain-shift trade-offs.

**Confidence:** Medium

**Why this confidence level**

The positive intervention evidence is from vision rather than LLMs, and the LLM-specific sources do not provide controlled demographic, cultural, linguistic, or intersectional outcomes.

**Evidence**

- AIM-Fair reports improved fairness and maintained utility in two image-classification settings using balanced synthetic data with contextual generation and selective fine-tuning, while also identifying synthetic–real domain gaps and quality limitations. [S23]
- Sources recommend subgroup audits, coverage maps, held-out tests, prompt-sensitivity checks, and re-auditing rather than assuming that balancing synthetic data is sufficient. [S9] [S10] [S11] [S27]

### Finding 7

**Claim**

Synthetic fine-tuning can improve apparent output quality or task capability while reducing safety robustness, so these outcomes must be evaluated separately.

**Confidence:** High

**Why this confidence level**

The quality–robustness distinction is directly reported in a primary study and is consistent with the broader evidence, though generalization across models and safety tasks is unresolved.

**Evidence**

- The ACL study reports higher output quality alongside reduced adversarial robustness after synthetic fine-tuning, making outputs potentially more usable but also more dangerous if safeguards weaken. [S14]
- Other sources describe capability gains in coding, mathematics, tool use, and domain adaptation without showing that these gains imply improved safety or real-world reliability. [S2] [S30] [S32]

### Finding 8

**Claim**

Synthetic evaluation data can improve controlled coverage and repeatability, but it should complement—not replace—real-world, expert-reviewed, and contamination-resistant evaluation.

**Confidence:** High

**Why this confidence level**

The complement-versus-replacement conclusion is supported by direct studies and multiple evaluation sources, although the exact transfer from synthetic evaluation scenarios to deployment performance remains unmeasured.

**Evidence**

- Synthetic scenarios can support edge-case testing, debugging, simulated traffic, and repeatable golden datasets; hybrid benchmarks can combine synthetic cases with real-world tasks and intermediate-step evaluation. [S16] [S19]
- Synthetic queries and judgments can differ systematically from human ones; one IR study reports that GPT-4 relevance judgments were about 0.28 points more positive on average than human judgments and that synthetic-test bias can distort absolute performance estimates. [S24]
- Contamination-resistant, private, dynamically refreshed, or held-out tests are recommended because public benchmarks and derivative data can enter training and inflate apparent generalization. [S20] [S22]

### Finding 9

**Claim**

Model-based filtering and judging can create circular evaluation bias when related models generate, filter, and assess the same synthetic data.

**Confidence:** High

**Why this confidence level**

The risk is directly documented through workflow observations and evaluator-bias findings.

**Evidence**

- Sources describe widespread use of LLM judges, self-verification, and self-correction, while also reporting a mismatch between critique scores and response quality and documenting self-preference and prompt-structure biases. [S6] [S10] [S24] [S30] [S31]

### Finding 10

**Claim**

Formal differential privacy is distinct from ordinary synthetic-data generation; generic claims that synthetic text is private or copyright-safe are not established by the retrieved evidence.

**Confidence:** Medium

**Why this confidence level**

The distinction between explicit DP mechanisms and ordinary synthesis is clear, but the retrieved material lacks comprehensive audits of LLM memorization, consent, provenance, and re-identification.

**Evidence**

- A Google Research method uses differentially private inference and aggregated predictions to generate synthetic data with formal privacy guarantees, while describing privacy-budget, quantity, quality, and computational trade-offs. [S18]
- Other sources present privacy benefits more generally but also acknowledge contractual, provenance, memorization, re-identification, and licensing concerns. [S3] [S4] [S29]

## Conflicts and Uncertainty

- Synthetic data is described both as highly effective for selected tasks and as a source of collapse, bias, and robustness failures. The evidence indicates that outcomes depend on source diversity, novelty, natural-data retention, verification, and replacement versus additive use rather than showing a universal benefit or harm. [S2] [S14] [S34]
- Targeted or balanced synthesis is presented as a possible way to improve representation, but no retrieved study directly demonstrates improved demographic, cultural, linguistic, or intersectional fairness after synthetic text fine-tuning. [S9] [S13] [S23] [S28]
- Higher output quality and benchmark performance may coexist with lower adversarial robustness or weaker evaluation validity; these metrics should not be combined into a single overall quality judgment. [S14] [S24] [S32]
- Synthetic evaluation can improve coverage and repeatability but can also introduce query, judgment, system, and contamination biases. Its usefulness therefore depends on provenance controls and comparison with human and real-world tests. [S16] [S19] [S20] [S22] [S24]
- Some practitioner sources make stronger claims about cost, privacy, or quality than the retrieved controlled evidence supports. These claims should be treated as proposed benefits or workflow observations rather than established general results. [S7] [S9] [S28] [S29]

## Remaining Gaps

- Controlled matched comparisons of synthetic-only, natural-only, additive mixed, and recursive regimes across LLM pretraining, continued pretraining, supervised fine-tuning, and preference optimization.
- Disaggregated demographic, cultural, multilingual, and intersectional measurements of fairness after synthetic-text training or fine-tuning.
- Effect sizes and replication evidence for factuality, hallucination, calibration, novelty, linguistic diversity, rare-case coverage, and adversarial robustness.
- Measurements of benchmark overlap, paraphrased contamination, and score inflation specifically attributable to synthetic training or evaluation pipelines.
- Validation of synthetic evaluation results against independent human or expert judgments, temporally separated tests, adversarial tests, and deployment-like outcomes.
- Independent validation of model-based filters and judges when generation, filtering, and evaluation involve related model families.
- Comprehensive evidence on privacy, memorization, membership inference, re-identification, provenance, consent, copyright, and licensing.
- Matched total-cost analyses including generation, compute, filtering, human review, maintenance, and natural-data collection.
- Generalization of reported source-diversity, domain-specific synthesis, and budget-sensitive strategy findings across models, languages, domains, and mixture ratios.

## Conclusion

The accumulated evidence supports cautious, conditional use of synthetic data—not wholesale replacement of natural or human-generated data. The most defensible pattern is to use synthetic examples for clearly defined tasks or coverage gaps, retain original natural data, seek genuinely novel and diverse sources, apply factuality and quality controls, and evaluate separately for capability, diversity, subgroup fairness, safety robustness, contamination, and deployment realism. Synthetic benchmark or “golden” data can aid controlled experimentation, but public or model-derived evaluation material may measure memorization or evaluator preference rather than generalization. The central unresolved issue is not whether synthetic data can ever work; it is when its benefits survive independent, disaggregated, contamination-resistant, and real-world evaluation.

## Sources

- [S1] Synthetic Data for AI Training: Use Cases and Risks [2026] — https://atlan.com/know/ai-agent/data-for-ai/synthetic-data-for-ai-training
- [S2] Synthetic Data for LLM Training: Decision Guide 2026 — https://www.digitalapplied.com/blog/synthetic-data-generation-llm-training-decision-guide-2026
- [S3] Synthetic Data Generation with LLMs: Techniques and Use Cases — https://tetrate.io/learn/ai/synthetic-data-generation-llms
- [S4] Synthetic Data for ML: Uses, Risks, and Best Practices | CleverX Blog — https://cleverx.com/blog/synthetic-data-for-ml-the-game-changer-in-training-for-2025
- [S5] Large Language Models Are Still Getting Stronger, but Researchers Face New Bottlenecks in Data, Evaluation, and Safety | Newswise — https://www.newswise.com/articles/large-language-models-are-still-getting-stronger-but-researchers-face-new-bottlenecks-in-data-evaluation-and-safety
- [S6] The Impact of Synthetic Data Diversity on LLM Fine-Tuning - arXiv — https://arxiv.org/html/2511.01490v1
- [S7] Synthetic Data for LLM Fine-Tuning 2026 — https://futureagi.com/blog/synthetic-data-fine-tuning-llms
- [S8] Synthetic Training Data Quality Collapse: How Feedback Loops Destroy Your Fine-Tuned Models — https://tianpan.co/blog/2026-04-09-synthetic-training-data-quality-collapse
- [S9] Synthetic Data for Bias Mitigation 2026: 5 Methods + FAGI — https://futureagi.com/blog/synthetic-data-generation-bias-2025
- [S10] Fairness in AI Decisions About People: Evidence from LLM Experiments — https://manhattan.institute/article/fairness-in-ai-decisions-about-people-evidence-from-llm-experiments
- [S11] GitHub - junxu-ai/LLM_fairness: Collection of papers, tools ... — https://github.com/junxu-ai/LLM_fairness
- [S12] Bias Mitigation via Synthetic Data Generation: A Review — https://www.mdpi.com/2079-9292/13/19/3909
- [S13] Auditing socio-demographic and cross-societal fairness in LLM-simulated public opinion | EPJ Data Science | Springer Nature Link — https://link.springer.com/article/10.1140/epjds/s13688-026-00673-y
- [S14] The Impact of Synthetic Data Diversity on LLM Fine-Tuning — https://aclanthology.org/2026.findings-acl.360.pdf
- [S15] Synthetic Data Generation Strategies for Fine-Tuning LLMs — https://scale.com/blog/synthetic-data-fine-tuning-llms
- [S16] Creating and Validating Synthetic Datasets for LLM Evaluation & Experimentation - Arize AI — https://arize.com/blog/creating-and-validating-synthetic-datasets-for-llm-evaluation-experimentation
- [S17] GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub — https://github.com/pengr/LLM-Synthetic-Data
- [S18] Generating synthetic data with differentially private LLM inference — https://research.google/blog/generating-synthetic-data-with-differentially-private-llm-inference
- [S19] Preprint 2025 CAUSCIBENCH: EVALUATING LLM CAUSAL REASON- — https://zhijing-jin.com/files/papers/2025_CauSciBench.pdf
- [S20] The benchmark leak: how your eval set quietly joins the training corpus — https://tianpan.co/blog/2026-04-23-benchmark-leak-eval-contamination
- [S21] GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub — https://github.com/lyy1994/awesome-data-contamination
- [S22] LLM Benchmark Datasets Should Be Contamination- ... — https://arxiv.org/html/2605.19999v1
- [S23] Advancing Algorithmic Fairness via Selectively Fine-Tuning ... — https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_AIM-Fair_Advancing_Algorithmic_Fairness_via_Selectively_Fine-Tuning_Biased_Models_with_CVPR_2025_paper.pdf
- [S24] Towards Understanding Bias in Synthetic Data for Evaluation | alphaXiv — https://www.alphaxiv.org/abs/2506.10301
- [S25] Synthetic Data + Evaluation Pipelines: Scaling Fine-Tuning ... — https://medium.com/@akankshasinha247/synthetic-data-evaluation-pipelines-scaling-fine-tuning-without-losing-alignment-f469a81cdf9a
- [S26] A Methodology for Controlling Bias and Fairness in Synthetic Data Generation — https://www.mdpi.com/2076-3417/12/9/4619
- [S27] Diving Deep Into Fair Synthetic Data Generation (Fairness Series Part 5) - MOSTLY AI powered by Syntho — https://mostly.ai/blog/diving-deep-into-fair-synthetic-data-generation-fairness-series-part-5
- [S28] DS2-Instruct: Domain-Specific Data Synthesis for Large Language Models Instruction Tuning — https://arxiv.org/html/2603.12932v2
- [S29] How to Generate and Use Synthetic Data for Finetuning — https://eugeneyan.com/writing/synthetic
- [S30] Generating Synthetic Data for LLM Post-Training — https://www.jonvet.com/blog/llm-synthetic-data
- [S31] Synthetic data for LLM fine-tuning and alignment - Argilla — https://argilla.io/blog/synthetic-data
- [S32] Synthetic Data Generation Using Large Language Models: Advances in Text and Code — https://arxiv.org/html/2503.14023v2
- [S33] AI models collapse when trained on recursively generated data | Hacker News — https://news.ycombinator.com/item?id=41058194
- [S34] What happens when generative AI models train recursively on each others’ outputs? — https://arxiv.org/html/2505.21677v3
- [S35] Publications & Research — https://mbrenndoerfer.com/publications
