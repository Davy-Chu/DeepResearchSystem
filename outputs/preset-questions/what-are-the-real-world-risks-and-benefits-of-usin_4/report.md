# Research Report

## Research Question

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

## Summary

Synthetic data offers practical benefits for scaling task-specific examples, targeting edge cases, supporting privacy-sensitive development, and accelerating fine-tuning or prototyping. The evidence indicates that these benefits are conditional on curation, validation, deduplication, source diversity, and retention of independently sourced real data. The clearest quality risk is model collapse when recursively generated data replaces real data. Synthetic data can also reproduce source-model and dataset biases, but the supplied evidence is insufficient to determine whether synthetic, human-generated, or mixed data produces better subgroup outcomes. Evaluation should therefore combine held-out real-world tests, distribution and diversity measures, robustness and safety assessments, subgroup analysis, contamination checks, and comparisons with human-only and mixed-data baselines.

## Findings

### Finding 1

**Claim**

Synthetic data can improve training efficiency and task-specific performance when carefully curated and used with substantial real data, but the supplied performance evidence is limited in generalizability.

**Confidence:** Medium

**Why this confidence level**

The sources report a concrete performance example and plausible task-specific benefits, but the strongest numerical results are vendor-stated and the evidence does not establish broad performance gains across tasks or deployments.

**Evidence**

- A reported Phi-1 example used curated web data plus one billion synthetic tokens and achieved vendor-stated HumanEval and MBPP results; other sources describe gains from synthetic augmentation for limited labeled datasets and specific tasks. [S1] [S4]

### Finding 2

**Claim**

Synthetic data can scale scarce task-specific examples, target rare or underrepresented cases, support privacy-sensitive development, and accelerate prototyping; these are operational benefits rather than guaranteed real-world performance improvements.

**Confidence:** Medium

**Why this confidence level**

The use cases are consistently described, but much of the evidence is practitioner- or vendor-oriented and does not establish reliable deployed-system gains.

**Evidence**

- Sources describe use cases including limited-label augmentation, minority-class and edge-case generation, privacy-sensitive data sharing, low-resource-language adaptation, specialized systems, and reduced manual collection or annotation. [S1] [S2] [S4] [S7] [S10]

### Finding 3

**Claim**

Synthetic generation can target variation across formats, classes, audiences, and edge cases, but apparent diversity does not establish meaningful coverage, factuality, or transfer to deployment conditions.

**Confidence:** High

**Why this confidence level**

The evidence supports controllable variation and the need for validation, while explicitly limiting the claim that generated variation reliably improves real-world coverage.

**Evidence**

- Prompting, structured generation, seed variation, and diverse synthetic sources can create varied examples; however, generated data inherits source-model limitations and may narrow distributions or contain artifacts. Independent validation against the target distribution is required. [S1] [S4] [S9] [S10] [S12]

### Finding 4

**Claim**

When real data is replaced by recursively generated synthetic data, successive generations can undergo model collapse: errors and biases may compound, while rare, low-probability, and diverse portions of the original distribution become underrepresented or lost. This risk is conditional on the training regime and is not inherent to all synthetic-data use.

**Confidence:** High

**Why this confidence level**

The latest verification retained the conditional formulation and found consistent support for collapse under recursive replacement, while noting that findings may not generalize uniformly from theoretical, simulated, or smaller-model settings to all LLM training and fine-tuning.

**Evidence**

- Sources describe distribution-tail loss, diversity reduction, compounding approximation errors, and degradation under recursive full replacement. Retaining real data, filtering, deduplication, and using diverse synthetic sources are described as mitigating conditions. [S1] [S2] [S5] [S6] [S12]

### Finding 5

**Claim**

Synthetic fine-tuning has mixed quality and safety effects: greater source diversity can preserve output diversity and mitigate collapse, while one controlled study reports reduced adversarial robustness despite preserved output quality.

**Confidence:** Medium

**Why this confidence level**

The findings come from one supplied study involving particular models, datasets, and fine-tuning conditions; broader deployment effects remain uncertain.

**Evidence**

- The supplied fine-tuning study reports that multi-source synthetic data mitigated distribution collapse and preserved output diversity, but synthetic fine-tuning reduced adversarial robustness while maintaining output quality. [S12]

### Finding 6

**Claim**

Synthetic data generation can reproduce representational, linguistic, cultural, demographic, and occupational biases from source models and training distributions, particularly for Western, English-language, majority-group, and low-resource contexts.

**Confidence:** Medium

**Why this confidence level**

The evidence documents relevant bias mechanisms in LLM outputs and synthetic personas, but does not show that synthetic data consistently amplifies or reduces these biases relative to human-generated or mixed data.

**Evidence**

- The sources report Western and English-language over-representation, poorer performance in some non-Western and low-resource contexts, majority or WEIRD persona preferences, and demographic, cultural, nationality, and occupational representation gaps. [S11] [S13] [S15]

### Finding 7

**Claim**

A reliable comparative conclusion about demographic, linguistic, or cultural bias in models trained on synthetic versus human-generated or mixed data cannot currently be drawn from the supplied evidence.

**Confidence:** High

**Why this confidence level**

The latest verified wording explicitly limits the conclusion: relevant bias is documented, but comparative subgroup evidence is insufficient.

**Evidence**

- The sources provide subgroup observations and one synthetic-versus-human comparison involving self-preference bias, but do not provide sufficient comparative subgroup-disparity measurements across demographic, linguistic, or cultural groups. [S11] [S12] [S13] [S14]

### Finding 8

**Claim**

For synthetic fine-tuning, generation alone is insufficient: practical pipelines require filtering, validation, deduplication, and subsequent held-out or regression evaluation.

**Confidence:** Medium

**Why this confidence level**

The sources directly describe these controls, but they are largely practitioner- or vendor-oriented and do not establish that the controls reliably prevent downstream failures.

**Evidence**

- Pipeline descriptions characterize raw model output as not training-ready and recommend quality filtering, accuracy checks, deduplication, held-out evaluation, and regression testing. [S7] [S9]

### Finding 9

**Claim**

Evaluation should not rely on aggregate benchmark scores or synthetic test cases alone. It should include independently validated held-out tests, contamination and leakage checks, subgroup and low-resource-language analysis, distribution and linguistic-diversity measures, adversarial-robustness testing, safety and self-preference measures, and comparisons across synthetic, human, and mixed-data training regimes.

**Confidence:** High

**Why this confidence level**

The evidence supports a multidimensional evaluation design, while also stating that controlled metrics have not been shown to predict real-world deployment outcomes.

**Evidence**

- The sources warn that saturation, contamination, and leakage can make benchmark scores misleading; they recommend held-out and regression testing, multidimensional subgroup evaluation, distribution-collapse and diversity measures, adversarial testing, output-quality assessment, and self-preference analysis. [S4] [S5] [S9] [S10] [S12] [S13] [S14]

### Finding 10

**Claim**

Synthetic records should not be treated as reliably privacy-preserving without formal memorization and re-identification testing, lineage, governance, and fidelity metadata.

**Confidence:** Medium

**Why this confidence level**

Privacy-oriented use cases are documented, but the supplied evidence does not establish a formal privacy guarantee.

**Evidence**

- Sources present privacy substitution as a use case but retain concerns about re-identification, audit gaps, lineage, fidelity metadata, and the absence of formal privacy evaluations in the supplied material. [S1] [S2] [S4] [S7] [S10]

## Conflicts and Uncertainty

- The evidence supports both benefits from carefully curated, additive synthetic data and substantial degradation risk under recursive replacement. These are different data-generation and training regimes, so the evidence does not support treating synthetic data as uniformly beneficial or harmful. [S1] [S4] [S6] [S12]
- Synthetic fine-tuning may preserve output quality while reducing adversarial robustness; human fine-tuning reportedly reduces both output quality and adversarial robustness in the supplied study, while human data is more effective than multi-source synthetic data at reducing self-preference bias. The generality of these comparisons is uncertain. [S12]
- The evidence documents multiple forms of representational bias but does not resolve whether synthetic, human-generated, or mixed data yields lower subgroup bias. [S11] [S12] [S13] [S14]

## Remaining Gaps

- G1: Comparative empirical subgroup-bias studies across synthetic, human-generated, and mixed training data are needed, including effects of prompting and filtering.
- G2: Evidence is insufficient to distinguish synthetic pretraining from synthetic fine-tuning effects on factuality, transfer, distribution shift, robustness, and collapse risk.
- G3: Independent deployment-oriented studies are needed to test whether synthetic benchmarks and edge-case results predict real-world factuality, safety, calibration, robustness, and failure rates.
- G4: Formal memorization and re-identification evaluations are needed before treating synthetic data as a privacy-preserving substitute.

## Conclusion

The strongest evidence-based practical position is conditional: synthetic data can be useful for scaling, targeted coverage, and fine-tuning efficiency when it supplements rather than replaces independently sourced real data and is subjected to filtering, deduplication, validation, and rigorous model-level evaluation. The major risks are distribution narrowing and error propagation under recursive replacement, inherited or concealed bias, misleading benchmark results, degraded adversarial robustness, and unverified privacy assumptions. Current evidence does not support a reliable comparative judgment that synthetic data is less biased than human or mixed data, nor that controlled synthetic evaluations predict real-world outcomes. Deployment decisions should therefore require explicit synthetic-to-real comparisons, subgroup and out-of-distribution testing, contamination checks, robustness and safety evaluation, and documentation of data lineage and generation procedures.

## Sources

- [S1] Synthetic Data for LLM Training: Decision Guide 2026 — https://www.digitalapplied.com/blog/synthetic-data-generation-llm-training-decision-guide-2026
- [S2] Synthetic Data for AI Training: Use Cases and Risks [2026] — https://atlan.com/know/ai-agent/data-for-ai/synthetic-data-for-ai-training
- [S3] Using Synthetic Data to Improve LLM Fine‑Tuning - Newline — https://www.newline.co/@Dipen/using-synthetic-data-to-improve-llm-finetuning--d453f658
- [S4] Synthetic Data Generation with LLMs: Techniques and Use ... — https://tetrate.io/learn/ai/synthetic-data-generation-llms
- [S5] Large Language Models Are Still Getting Stronger, but ... — https://www.newswise.com/articles/large-language-models-are-still-getting-stronger-but-researchers-face-new-bottlenecks-in-data-evaluation-and-safety
- [S6] Model Collapse via Synthetic Training Data — https://www.emergentmind.com/topics/model-collapse-through-synthetic-training-data
- [S7] How to Generate Synthetic Training Data for LLM Fine-Tuning (2026 Guide) - Plushcap — https://plushcap.com/content/prem-ai/blog/prem-ai-how-to-generate-synthetic-training-data-for-llm-fine-tuning-2026-guide
- [S8] Mixing Synthetic and Real Data for Pretraining — https://apxml.com/courses/synthetic-data-llm-pretrain-finetune/chapter-3-synthetic-data-llm-pretraining-application/blending-synthetic-real-data
- [S9] Synthetic Data Generation for Fine-Tuning: Using LLMs — https://callsphere.tech/blog/synthetic-data-generation-fine-tuning-llms-training-data
- [S10] Synthetic Data Generation for Agentic AI | Use Case | NVIDIA — https://gretel.ai/blog/addressing-concerns-of-model-collapse-from-synthetic-data-in-ai
- [S11] WEIRD Bias: Western Over-representation in LLM Training Data | Synthetic Audiences Research — https://cyberarctica.com/synthetic-audiences/05_weird_bias_western_over-representation_in_llm_training_data.html
- [S12] The Impact of Synthetic Data Diversity on LLM Fine-Tuning — https://arxiv.org/html/2511.01490v1
- [S13] [PDF] Investigating and Mitigating Undesirable Biases in Large ... — https://ojs.aaai.org/index.php/AAAI/article/view/35214/37369
- [S14] Bias in Large Language Models: Origin, Evaluation, and Mitigation — https://www.mdpi.com/2079-9292/15/9/1824
- [S15] Data bias in LLM and generative AI applications — https://mostly.ai/blog/data-bias-types
