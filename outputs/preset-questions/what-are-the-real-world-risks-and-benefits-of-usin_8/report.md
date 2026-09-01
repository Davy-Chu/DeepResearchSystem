# Research Report

## Research Question

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

## Summary

Synthetic data can be valuable for targeted augmentation, distillation, rare-case coverage, class balancing, and privacy-constrained development. Its benefits are conditional: raw generated outputs may contain factual errors, distributional distortions, repetition, and bias, while recursive or replacement-based training can narrow model behavior and reduce generalization. The evidence favors using curated synthetic data alongside fresh human or real-world data, with independent, contamination-aware evaluation covering factuality, diversity, fairness, privacy, robustness, and safety. The optimal real-to-synthetic mixture and evaluation thresholds remain unresolved.

## Findings

### Finding 1

**Claim**

Synthetic data can reduce data bottlenecks by supplying task-specific examples where real data is scarce, expensive to annotate, sensitive, imbalanced, or difficult to collect.

**Confidence:** High

**Why this confidence level**

Multiple sources consistently identify these practical benefits, although their magnitude varies by task and is not uniformly quantified.

**Evidence**

- Surveys and best-practices research describe LLM-generated text and code as scalable, relatively low-cost sources for low-resource, privacy-constrained, and expensive labeling settings. [S3] [S4] [S5]
- The use-case literature describes augmentation, class balancing, privacy-sensitive development, rapid prototyping, domain adaptation, and edge-case generation as applications of synthetic data. [S15]

### Finding 2

**Claim**

Synthetic data can improve downstream performance, particularly for low-data or specialized tasks, when it is targeted, curated, and used as augmentation or teacher-to-student distillation rather than as indiscriminate replacement data.

**Confidence:** Medium

**Why this confidence level**

The direction of benefit is supported by multiple sources, but several performance examples are secondary, vendor-reported, or limited to particular tasks and models.

**Evidence**

- The survey reports performance improvements in low-data regimes and describes gains from task-specific generation, prompting, and curation. [S3] [S4]
- IBM reports competitive benchmark performance for LAB-trained models and describes improvements over other fine-tuned versions of the same base models. [S1]
- The fine-tuning literature describes teacher-generated domain examples as a way to transfer capability to smaller student models while reducing annotation requirements. [S18] [S19]
- Reported successful recipes, including Phi-model examples, combine curated synthetic material with high-quality real data rather than relying on unfiltered synthetic replacement. [S2] [S6]

### Finding 3

**Claim**

Synthetic-data quality cannot be inferred from fluency: generated examples may contain factual errors, hallucinations, irrelevant or inconsistent content, unrealistic styles or distributions, repetition, and insufficient coverage of rare but valid cases.

**Confidence:** High

**Why this confidence level**

This risk is consistent across academic surveys, best-practices material, and operational accounts; exact failure rates are not established.

**Evidence**

- Surveys identify factual inaccuracy, weak distributional or stylistic realism, diversity drift, and poor real-world generalization as central risks. [S3] [S4] [S5]
- The generation-and-curation literature reports that raw generations commonly contain noise, inconsistencies, and irrelevant samples, requiring filtering and re-weighting. [S10]
- Practitioner sources describe formatting failures, hallucinations, repetition, and off-task responses in raw outputs, while emphasizing that only filtered data should reach training. [S18] [S19] [S23]

### Finding 4

**Claim**

Narrow or unrepresentative seed data can propagate its coverage gaps into the synthetic dataset, so synthetic generation does not recover diversity that was absent from the starting distribution.

**Confidence:** Medium

**Why this confidence level**

The mechanism is clearly described, but the retrieved evidence does not quantify how seed coverage translates into downstream performance.

**Evidence**

- The domain-fine-tuning guidance states that real seed data defines the target distribution and that narrow seeds can omit real-world edge cases and minority patterns even if generation is later scaled. [S18]
- Use-case guidance emphasizes that synthetic utility depends on alignment between the generated distribution and the target application. [S15]

### Finding 5

**Claim**

Synthetic data can preserve, amplify, or introduce bias; controlled generation may improve representation of minority classes or low-resource groups, but fairness benefits are conditional on validation against real populations and outcomes.

**Confidence:** High

**Why this confidence level**

The conditional nature of the claim is directly supported by several sources; no evidence establishes that synthetic generation automatically improves fairness.

**Evidence**

- The literature identifies bias amplification and new modeling biases as risks while also describing controlled balancing and up-weighting of underrepresented classes or languages as potential benefits. [S3] [S4] [S5]
- IBM warns that synthetic data may fail to represent demographic diversity, leading to inequitable performance across groups. [S1]
- The evaluation-framework source motivates synthesis partly through imbalance and underrepresentation, but treats fidelity, utility, and privacy as separate dimensions requiring measurement. [S7]

### Finding 6

**Claim**

Recursive or replacement-based synthetic training can cause model collapse or distribution narrowing, including loss of diversity, factuality, precision, recall, or low-probability cases.

**Confidence:** Medium

**Why this confidence level**

The phenomenon and its dependence on training regime are supported, but precise mixture requirements and generality across tasks and model sizes remain uncertain.

**Evidence**

- The reported Nature findings describe degradation when successive models are trained on model-generated content, including increasingly nonsensical outputs and irreversible defects under indiscriminate use. [S1] [S6]
- Surveys describe progressive loss of distributional breadth and recommend blending synthetic data with real data to reduce collapse risk. [S2] [S3] [S4]
- The evidence distinguishes risky replacement or self-training from additive use that retains real-data anchors, but does not establish a universal safe mixture threshold. [S6] [S20]

### Finding 7

**Claim**

Greater diversity of synthetic sources can mitigate some distribution-collapse and diversity problems, but it does not guarantee better safety, factuality, or fairness.

**Confidence:** Medium

**Why this confidence level**

The directly relevant study reinforces prior evidence but covers limited models, languages, and fine-tuning settings; its findings should not be generalized universally.

**Evidence**

- The Synthetic Eggs study reports that multi-source synthetic fine-tuning better preserves output-distribution breadth and lexical diversity than lower-diversity synthetic data. [S20]
- The same study reports reduced adversarial robustness and possible safeguard removal after synthetic fine-tuning, despite preserved output quality; effects vary with target and source-model configuration. [S20] [S21]

### Finding 8

**Claim**

Synthetic fine-tuning can change safety and behavioral alignment in ways that ordinary task accuracy or fluency metrics fail to detect.

**Confidence:** Medium

**Why this confidence level**

The safety finding is important and supported by a primary-paper source and a summary, but the reported experiments have narrow scope and do not establish prevalence.

**Evidence**

- The Synthetic Eggs study reports that synthetic fine-tuning may remove safety guardrails while retaining output quality, potentially making harmful outputs more usable. [S20] [S21]
- Domain-fine-tuning guidance warns that a model can remain fluent while factual or knowledge quality deteriorates and recommends validation on real examples rather than synthetic validation alone. [S18]

### Finding 9

**Claim**

Evaluation of synthetic training data should be multidimensional and should include independent human or real-world data rather than relying only on similarity metrics or aggregate benchmark scores.

**Confidence:** High

**Why this confidence level**

Sources converge strongly on the need for independent, multidimensional evaluation, although they do not establish one universally validated protocol.

**Evidence**

- SynEval separates fidelity, downstream utility, and privacy, including comparison with real-world validation data and re-identification-risk analysis. [S7]
- The broader literature calls for checks of factuality, fidelity, diversity, fairness, robustness, privacy, generalization, and collapse. [S3] [S4] [S5] [S10]
- Operational guidance recommends real-data holdouts and regression suites because synthetic validation can miss deployment-relevant failures. [S18] [S19]

### Finding 10

**Claim**

Synthetic evaluation benchmarks are task-dependent: they may approximate real-data comparisons for simpler tasks but become less representative for more complex tasks.

**Confidence:** Medium

**Why this confidence level**

The finding comes from systematic experiments, but the retrieved evidence does not show whether the pattern generalizes broadly.

**Evidence**

- Across six datasets and three tasks, S11 reports stronger synthetic-benchmark utility for intent classification than for named entity recognition, assessing both absolute performance and method rankings. [S11]

### Finding 11

**Claim**

Synthetic evaluation can be biased when the same or related model generates the test data and evaluates or solves it; multiple generators and independent references improve validity.

**Confidence:** Medium

**Why this confidence level**

The pattern is supported by multiple studies, but the optimal generator mix, judge calibration, and aggregation method remain unknown.

**Evidence**

- S11 reports self-generation bias for smaller models, recommends multiple larger generators, and finds that averaging across generators produces more representative benchmarks. [S11]
- The fine-tuning study reports self-preference and pro-synthetic preference effects in LLM-as-judge evaluation, with human data more effective than synthetic data at reducing these effects. [S20] [S21]

### Finding 12

**Claim**

Contamination and memorization can inflate benchmark results, so evaluations should include exact and semantic-overlap checks, perturbation tests, temporal or newly collected data, and adversarial cases.

**Confidence:** Medium

**Why this confidence level**

The general principle is strongly supported, but some numerical contamination estimates come from individual or commercial sources and should not be treated as general rates.

**Evidence**

- S12 reports that benchmark contamination can inflate conventional performance in a fake-news task and proposes human-adversarial, dynamically sourced, and entity-controlled evaluation. [S12]
- S13 advocates n-gram alignment, canary insertion, and perturbation testing to distinguish memorization from generalization. [S13]
- Operational guidance recommends n-gram and embedding-space checks against evaluation sets because teacher models may reproduce benchmark items or paraphrases. [S23]

### Finding 13

**Claim**

Synthetic data may reduce direct exposure to sensitive records, but privacy is a conditional benefit that requires leakage, memorization, and re-identification testing.

**Confidence:** Medium

**Why this confidence level**

The need for privacy auditing is well established, but the retrieved evidence does not quantify leakage risk for free-form LLM text.

**Evidence**

- SynEval treats privacy preservation as a separate evaluation dimension and proposes re-identification-risk analysis rather than assuming synthetic data is safe. [S7]
- IBM and the best-practices literature warn that synthetic data can still reveal personal details or reproduce source biases and therefore requires safeguards and validation. [S1] [S5]
- Vendor workflows present privacy-preserving evaluation use cases, but do not independently demonstrate that leakage or re-identification risk is eliminated. [S14]

## Conflicts and Uncertainty

- Some sources allow synthetic data to augment or potentially substitute for real data in constrained settings, while the stronger operational conclusion is to retain fresh real data because replacement and recursive use increase collapse and distribution-loss risks. [S1] [S2] [S3] [S4] [S6] [S15] [S18]
- Source diversity improves some distributional and lexical-diversity measures, yet the same evidence reports possible safety-guardrail degradation and increased harmful-output susceptibility. Better diversity does not imply safer behavior. [S20] [S21]
- Synthetic benchmarks can be useful for simpler tasks but misleading for complex tasks, especially when generator–evaluator bias or contamination is present. [S11] [S12] [S13]
- Several sources make quantitative claims about filtering rates, leakage, benchmark performance, or privacy safety, but those claims are not independently corroborated in the retrieved material and should be treated as source-specific rather than general estimates. [S6] [S14] [S22] [S23]
- The evidence does not establish a universal real-to-synthetic ratio, source-diversity requirement, refresh rate, or quality threshold that prevents collapse across model sizes, domains, and objectives. [S6] [S18] [S20]

## Remaining Gaps

- Independent controlled studies across more model families, languages, domains, and multi-turn settings are needed to determine whether reported synthetic fine-tuning gains persist on deployment-like real data.
- A validated LLM-specific evaluation protocol combining factuality, distributional coverage, subgroup fairness, privacy leakage, contamination, robustness, safety, and downstream utility is not established by the retrieved sources.
- The amount and type of fresh real data needed to prevent collapse, and how this varies with source diversity and training objective, remain unresolved.
- It remains unclear how to evaluate factuality and bias in open-ended synthetic text where formal verification is unavailable.
- The effectiveness of privacy safeguards against memorization and re-identification in free-form LLM training data remains insufficiently quantified.

## Conclusion

Synthetic data is best treated as a controlled supplement or distillation resource, not an automatically safe replacement for human or real-world data. Its real-world benefits—scale, lower labeling burden, targeted coverage, privacy-sensitive development, and potential low-data performance gains—are most credible when generation is grounded in representative seeds, aggressively filtered, deduplicated, provenance-tracked, and mixed with fresh real data. The principal risks are factual and distributional distortion, inherited or amplified bias, contamination-driven overestimation of capability, privacy leakage, model collapse, and safety degradation that may be invisible to fluency or aggregate benchmark scores. A responsible deployment decision therefore requires independent human/real-data holdouts, multiple evaluation sources, contamination and memorization tests, subgroup and fairness analysis, factuality checks, diversity and robustness measures, privacy audits, and safety regression testing. The evidence supports this evaluation-oriented approach but does not yet specify universal thresholds or mixture rules.

## Sources

- [S1] Examining synthetic data: The promise, risks and realities | IBM — https://www.ibm.com/think/insights/ai-synthetic-data
- [S2] The Prominence of Synthetic Data, and Why It Will Expand Rather Than Replace Real Data - Dataversity — https://www.dataversity.net/articles/the-prominence-of-synthetic-data-and-why-it-will-expand-rather-than-replace-real-data
- [S3] Synthetic Data Generation Using Large Language Models — https://arxiv.org/pdf/2503.14023
- [S4] Synthetic Data Generation Using Large Language Models: Advances in Text and Code — https://arxiv.org/html/2503.14023v2
- [S5] Best Practices and Lessons Learned on Synthetic Data for Language Models — https://arxiv.org/html/2404.07503v1
- [S6] Synthetic Data for LLM Training: Decision Guide 2026 — https://www.digitalapplied.com/blog/synthetic-data-generation-llm-training-decision-guide-2026
- [S7] A Multi-Faceted Evaluation Framework for Assessing Synthetic Data Generated by Large Language Models — https://arxiv.org/html/2404.14445v2
- [S8] Biased by Design? Evaluating Bias and Behavioral Diversity in LLM Annotation of Real-World and Synthetic Hotel Reviews — https://www.mdpi.com/2673-2688/6/8/178
- [S9] Medium — https://medium.com/foundation-models-deep-dive/challenges-and-pitfalls-of-using-synthetic-data-for-llms-7337fcda1316
- [S10] On LLMs-Driven Synthetic Data Generation, Curation, and Evaluation: A Survey | alphaXiv — https://www.alphaxiv.org/abs/2406.15126
- [S11] Efficacy of Synthetic Data as a Benchmark — https://arxiv.org/html/2409.11968v1
- [S12] Defending Data Contamination in the Evaluation of LLM- ... — https://aclanthology.org/2025.acl-long.431.pdf
- [S13] Data Contamination or Genuine Generalization? Disentangling LLM Performance on Benchmarks | Academic Journal of Natural Science — https://www.suaspress.org/ojs/index.php/AJNS/article/view/v2n2a03
- [S14] How to Build Privacy-Preserving Evaluation Benchmarks with Synthetic Data | NVIDIA Technical Blog — https://developer.nvidia.com/blog/how-to-build-privacy-preserving-evaluation-benchmarks-with-synthetic-data
- [S15] Synthetic Data Generation with LLMs: Techniques and Use Cases — https://tetrate.io/learn/ai/synthetic-data-generation-llms
- [S16] Synthetic Data Generation for Fine-Tuning LLMs — https://pub.towardsai.net/synthetic-data-generation-for-fine-tuning-llms-de9fe22bd1e6
- [S17] [Literature Review] Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning — https://www.themoonlight.io/en/review/synthetic-eggs-in-many-baskets-the-impact-of-synthetic-data-diversity-on-llm-fine-tuning
- [S18] Synthetic Data Pipelines for Domain-Specific LLM Fine-Tuning — https://tianpan.co/blog/2026-03-04-synthetic-data-pipelines-domain-llm-fine-tuning
- [S19] Synthetic Data Generation for Fine-Tuning: Using LLMs — https://callsphere.tech/blog/synthetic-data-generation-fine-tuning-llms-training-data
- [S20] Synthetic Eggs in Many Baskets:The Impact of Synthetic Data Diversity on LLM Fine-Tuning — https://arxiv.org/html/2511.01490v3
- [S21] Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning | Albert Gatt — https://www.linkedin.com/posts/albert-gatt_synthetic-eggs-in-many-baskets-the-impact-activity-7392500258229993472-EQUP
- [S22] Synthetic Data in AI: Breaking the Foundation Model Data Wall — https://theholyquran.co.in/articles/synthetic-data-generation-privacy-preserving-diffusion-models-llm-pretraining-2026
- [S23] Synthetic Data Pipelines for LLM Training - bards.ai — https://www.bards.ai/services/synthetic-data
