# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** synthetic-data-llm-training

**System Version:** baseline-zero

**Research Model:** gpt-4o-mini

**Evaluator Model:** gpt-5.6-luna

## Summary

- Overall: 55.1 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.38
- Coverage: 0.44
- Depth: 0.25
- Citation quality: 0.74
- Citation validity: 1.00
- Citation support: 0.60
- Citation completeness: 0.87
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report recognizes training-regime differences, especially pure-synthetic versus hybrid use, but does not provide the requested setting definitions or a substantive analysis of how those differences affect outcomes.
- Candidate evidence:
  - The report discusses synthetic data for both “training large language models” and “LLM fine-tuning.”
  - It distinguishes “solely using synthetic data” from “combining synthetic data with real data” and recommends a “hybrid approach.”
- Missing:
  - It does not define or distinguish LLM-generated data from programmatically generated data.
  - It does not explain how pretraining differs from fine-tuning in the relevant risks and benefits.
  - It mentions pure-synthetic versus mixed training but gives little explanation of why the distinction matters beyond degradation risk.

### R2

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report identifies scarcity, domain coverage, and diversity as potential benefits, but treats them mostly as assertions and does not develop the important mechanisms or quality consequences.
- Candidate evidence:
  - The report states that synthetic data can address “data scarcity or privacy concerns.”
  - It says synthetic data expansion can improve models in “domain-specific tasks where real data is insufficient.”
  - It claims that “diverse synthetic data sources” and “targeted synthetic data for under-represented subgroups” can improve balance.
- Missing:
  - It does not substantially explain scale, label availability, rare-event or edge-case coverage, or controlled diversity as data-quality benefits.
  - It provides little evidence connecting these benefits to improved generalization or model quality beyond broad claims.
  - Privacy is mentioned as a benefit, but the report does not assess its relationship to data quality.

### R3

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report covers degradation and collapse, which are important failure modes, but gives little diagnosis of their causes, manifestations, or downstream effects.
- Candidate evidence:
  - The report warns of “model degradation and distribution collapse.”
  - It states that “recursive training on solely synthetic data can degrade model performance.”
  - It connects hybrid training with maintaining “robustness.”
- Missing:
  - It does not discuss factual or semantic errors, incorrect labels, repetition, low diversity, artifacts, contamination, or distribution mismatch in detail.
  - It does not explain how particular failure modes affect accuracy, generalization, or robustness.
  - It does not identify conditions that make these failures more or less likely, apart from recursive or solely synthetic training.

### R4

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report identifies targeted subgroup generation and validation as possible mitigation mechanisms and acknowledges the need for validation, but does not develop the mechanisms or evaluation standard sufficiently.
- Candidate evidence:
  - It claims that “targeted synthetic data for under-represented subgroups can enhance balance and reduces bias in outputs.”
  - It mentions “quality control measures” and validation intended to prevent biases.
  - It says diverse synthetic sources can “help mitigate” bias and appropriately labels this claim medium confidence, noting that “empirical validation is required.”
- Missing:
  - It does not explain counterfactual generation, fairness-aware generation, reweighting, or filtering as distinct interventions.
  - It does not distinguish a balanced synthetic dataset from demonstrated improvement in model behavior in a systematic way.
  - It does not specify the baseline comparisons or bias evidence needed to substantiate a reduction claim.

### R5

- Coverage: 0.50
- Depth: 0.25
- Rationale: Bias is acknowledged, including amplification as an open concern, but the report offers little substantive account of the mechanisms or measurement distinction required by the rubric.
- Candidate evidence:
  - The report repeatedly identifies “bias” as a risk and lists “bias amplification risk in synthetic data generation processes” as an unresolved gap.
  - It mentions “self-preference bias” and claims that diverse synthetic sources can reduce it.
  - It refers to under-represented subgroups and the possibility of improving or worsening balance.
- Missing:
  - It does not explain generator bias, stereotypical associations, spurious correlations, class imbalance, or minority underrepresentation in concrete terms.
  - It does not analyze how iterative or large-scale generation can amplify bias.
  - It does not distinguish bias measured in generated data from bias observed in the trained model.

### R6

- Coverage: 0.25
- Depth: 0.25
- Rationale: Evaluation is identified as important, and human review is mentioned, but the report does not explain how synthetic-data quality should actually be evaluated.
- Candidate evidence:
  - The report says “validation measures” are needed to ensure synthetic datasets reflect desired characteristics.
  - It says automation should be complemented by “human evaluation.”
  - It notes a shift toward “holistic assessments” including fairness and real-world applicability.
- Missing:
  - It does not specify complementary measures for factuality, semantic or label correctness, distribution fidelity, diversity, coverage, training utility, and held-out-real-data generalization.
  - It does not explain limitations of statistical, human, model-based, or perplexity-style metrics.
  - It does not warn that synthetic-only or generator-aligned tests can give misleading assurance.
  - It provides no concrete evaluation protocol for deciding fitness for training or fine-tuning.

### R7

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report recognizes fairness evaluation as a broad need but supplies almost none of the required comparative or subgroup-specific methodology.
- Candidate evidence:
  - The report says evaluation should include “fairness and real-world applicability.”
  - It mentions targeted data for under-represented subgroups and claims possible reductions in output bias.
  - It lists systematic identification and mitigation of bias in hybrid datasets as a remaining gap.
- Missing:
  - It does not recommend comparison with real-data-only or no-synthetic baselines.
  - It does not specify held-out, preferably real, subgroup-sensitive evaluation.
  - It does not identify subgroup performance, error rates, representation, or disparity as metrics to compare.
  - It does not explain why dataset balance or generation prompts alone are insufficient evidence of fairness.

### R8

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report avoids a wholly unconditional verdict and names several safeguards, but its conclusion remains generic and does not synthesize the key conditional factors or operational criteria.
- Candidate evidence:
  - The conclusion gives a conditional overall judgment: synthetic data offers benefits, but “bias, performance degradation, and evaluation standards demand thorough consideration.”
  - It recommends “combining synthetic data with real data,” quality control, validation, and human evaluation.
  - It labels the benefit of diverse sources as medium confidence and notes that “empirical validation is required.”
- Missing:
  - It does not systematically relate outcomes to generator and target-model capability, task or domain, synthetic-to-real ratio, prompting, or training regime.
  - It does not discuss conflicting findings in substance; it merely states that “No material conflict was identified.”
  - It does not provide practical deployment decision criteria, thresholds, monitoring, or safeguards beyond generic quality control and hybrid data use.
  - It does not explain when synthetic data is likely to be harmful versus beneficial with enough specificity.

### Novel Value

- The report combines several relevant themes—hybrid real/synthetic training, recursive-training degradation, targeted subgroup generation, synthetic-source diversity, and the need for human and holistic evaluation.
- It identifies unresolved questions about optimizing hybrid datasets and bias amplification, although these are not developed into a detailed analysis.

## Citations

### Support

#### F1: SUPPORTED

- Claim: Synthetic data can alleviate limitations of real-world datasets, particularly in data-scarce or privacy-sensitive domains.
- Sources: S2, S11, S1
- Rationale: The saved sources directly state that synthetic data addresses limitations of real-world data, including scarcity and privacy constraints. S2 says it addresses “data scarcity” and “privacy constraints,” S11 describes real-data scarcity and privacy/compliance pressures, and S1 explicitly says synthetic data addresses critical limitations of real-world datasets.
- Supporting text: S2: “Synthetic data mirrors real distributions to address data scarcity, privacy constraints, and class imbalance.” S11: “real data scarcity has become a genuine constraint” and privacy pressures push practitioners toward “privacy-substitution alternatives that synthetic data can potentially satisfy.” S1: “Synthetic data is transforming ... addressing critical limitations of real-world datasets.”

#### F2: PARTIALLY_SUPPORTED

- Claim: Using synthetic data requires careful management to prevent model degradation and distribution collapse.
- Sources: S21, S18, S2
- Rationale: S21 supports the need to manage synthetic data carefully because synthetic–real discrepancies can cause poor real-world performance and generalization, and it discusses strategies to mitigate the domain gap. S2 explicitly supports model degradation and distribution collapse from recursive synthetic-data training and states that governance and lineage metadata are necessary. S18 does not meaningfully address synthetic-data risks, model degradation, or distribution collapse. The sources support a narrower claim about managing synthetic data to address domain gaps and avoid collapse, but do not establish that all use of synthetic data requires such management.
- Supporting text: S21: Synthetic–real data disparity creates a “domain gap” leading to poor performance and generalization in real-world scenarios; mixed training is presented as a mitigation strategy. S2: “Recursive training on synthetic data causes model collapse, where distributions narrow until outputs degrade,” and “ungoverned synthetic data creates audit gaps.”

#### F3: PARTIALLY_SUPPORTED

- Claim: Quality control measures are essential for effective synthetic data usage and bias mitigation.
- Sources: S25, S26
- Rationale: S26 directly supports the importance of quality evaluation for reliable synthetic-data use and describes validation and human oversight. It also identifies bias amplification as a risk, but does not explicitly state that quality-control measures mitigate bias. S25 supports that data quality affects model outcomes and notes that synthetic data can counter bias through targeted augmentation, but the saved excerpt does not connect this specifically to quality-control measures.
- Supporting text: S26: “Ensuring the quality of synthetic data is essential for building reliable machine learning models,” and organizations should “rigorously evaluate” datasets using accuracy, diversity, realism, visualization, statistical analysis, and human evaluation. It also warns that poorly designed generators can amplify bias.

#### F4: PARTIALLY_SUPPORTED

- Claim: Diverse synthetic data sources can help mitigate negative impacts such as distribution collapse and bias.
- Sources: S4, S12, S22
- Rationale: S4 directly supports that synthetic data from diverse sources can mitigate distribution collapse and discusses self-preference bias, but it does not establish broad mitigation of bias in general. S22 supports that synthetic data can reduce algorithmic bias through balanced and diverse datasets, but it does not specifically tie this effect to diversity of synthetic data sources. S12 discusses diversity and possible robustness benefits, but the supplied text does not directly support mitigation of distribution collapse or bias. Thus, the claim is supported only in separate, narrower respects.
- Supporting text: S4: “fine-tuning models on synthetic data from diverse sources can mitigate distribution collapse”; S22: synthetic data can create “balanced, diverse training datasets” intended to reduce algorithmic bias.

#### F5: PARTIALLY_SUPPORTED

- Claim: Evaluation standards for LLMs are shifting towards holistic assessments that include fairness and real-world applicability.
- Sources: S3, S20
- Rationale: S3 directly supports a shift away from narrow benchmark scoring toward evaluations of reliable, safe, transparent performance in realistic settings, and explicitly says future systems should address fairness. S20 discusses bias and fairness in AI data and models, but does not address changing LLM evaluation standards. Thus, the real-world applicability and fairness components are supported mainly by S3, while the broader claim that evaluation standards are shifting holistically is only partially supported.
- Supporting text: S3 states that evaluation is moving beyond correct answers toward operating "reliably, safely, and transparently in realistic settings," and that future evaluation should be closer to real applications while addressing "fairness, reproducibility, and safety." S20 describes the need to measure bias and fairness metrics, but not an LLM-evaluation shift.

### Missing Citations

- Q14: Synthetic data presents substantial benefits for LLM training, particularly by enhancing dataset diversity and addressing privacy issues.
- Q15: Synthetic-data use creates challenges related to bias, performance degradation, and evaluation standards.

## Deterministic Checks

- `run_metadata_loads`: PASS
- `report_exists`: PASS
- `sources_present`: PASS
- `structured_report_parses`: PASS
- `report_question_matches`: PASS
- `source_ids_unique`: PASS
- `source_ids_syntactically_valid`: PASS
- `source_urls_present`: PASS
- `evidence_objects_valid`: PASS
- `confidence_values_valid`: PASS
- `citation_ids_syntactically_valid`: PASS
- `citation_ids_resolve`: PASS
- `structured_claim_evidence_available`: NOT_EVALUABLE — This run predates or does not use an evidence ledger.
- `ledger_claim_ids_unique`: NOT_EVALUABLE — Evidence ledger unavailable.
- `ledger_evidence_relationships_resolve`: NOT_EVALUABLE — Evidence ledger unavailable.
- `ledger_confidence_values_valid`: NOT_EVALUABLE — Evidence ledger unavailable.
- `ledger_evidence_ids_unique`: NOT_EVALUABLE — Evidence ledger unavailable.

## Main Weaknesses

1. R6: Explain how to evaluate whether synthetic data is fit for LLM training or fine-tuning using multiple complementary measures.
2. R7: Specify how to evaluate the representational and fairness effects of using synthetic data.
3. R1: Define the synthetic-data settings relevant to the analysis and explain why their differences matter.
4. 4 cited finding(s) were not fully supported by saved evidence.
5. 2 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `36414e911184eea8ef62c41ba8423e71054770da6d3e515f90d477a9870e806e`
- Candidate report hash: `5f3befbb2397ca747223ccf6cc5b25e239370b160d85b26904950f572ea728a5`
- LLM calls: 7
- Evaluated at: 2026-09-01T15:21:06.059393+00:00
