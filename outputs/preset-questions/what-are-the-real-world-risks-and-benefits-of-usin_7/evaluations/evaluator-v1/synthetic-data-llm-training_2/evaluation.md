# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** synthetic-data-llm-training

**System Version:** llm-only-baseline-v0

**Model:** gpt-5.6-luna

## Summary

- Overall: 66.2 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.94
- Coverage: 0.94
- Depth: 0.94
- Citation quality: 0.00
- Citation validity: 0.00
- Citation support: 0.00
- Citation completeness: 0.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report meaningfully distinguishes several generation and mixture settings and explains why provenance, verification, and synthetic-to-real ratios matter. However, pretraining versus fine-tuning is not directly analyzed, and the categories of synthetic generation are presented somewhat implicitly rather than as an explicit scope framework.
- Candidate evidence:
  - The report distinguishes model-generated examples from outputs checked by “compilation and tests,” “symbolic or numerical verification,” database constraints, retrieval systems, simulators, and human/domain review.
  - It contrasts synthetic data that “replaces rather than supplements fresh human-originated data” with mixed pipelines and recommends using synthetic data “as a supplement rather than a replacement.”
  - It discusses synthetic instruction, preference, reasoning, coding, mathematical, multilingual, tool-use, and domain-specific data, but does not clearly distinguish pretraining from fine-tuning.
- Missing:
  - An explicit treatment of synthetic data in pretraining versus fine-tuning and why the risk profile differs.
  - A more systematic distinction between LLM-generated, programmatically generated, simulator-generated, and other synthetic-data settings.

### R2

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report covers scale, cost-enabled data creation, targeted coverage, rare and edge cases, specialized domains, controllable difficulty, and quality-oriented curation. It also connects these benefits to concrete training uses rather than merely asserting that synthetic data is cheaper.
- Candidate evidence:
  - The report states that synthetic data can “lower the marginal cost of producing large-scale instruction, preference, and domain-specific training examples.”
  - It explains that synthetic data can target “rare skills, long-tail cases, structured formats, languages, safety scenarios, and controllable difficulty levels.”
  - It gives examples involving mathematical, coding, multilingual, and tool-use data, including settings with automatically checkable answers or execution environments.
  - It cites Phi-1 as illustrating that “quality and task targeting” can matter more than raw volume.
- Missing:

### R3

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report addresses the major requested failure modes and connects them to downstream accuracy, generalization, robustness, long-tail retention, and evaluation reliability. It also identifies conditions affecting severity, including verification availability, filtering, model capacity, task, and mixture ratios.
- Candidate evidence:
  - It identifies “hallucinations, internal inconsistencies, formatting artifacts, and loss of information” as data-quality failures.
  - It discusses fluent but factually wrong outputs, repeated propagation of errors, repetitive phrasing, generic explanations, reduced lexical or conceptual diversity, and recognizable stylistic signatures.
  - It explains that recursive synthetic-data training can “lose the tails of the original distribution and progressively distort the learned distribution,” especially harming rare events and minority patterns.
  - It covers contamination, distribution mismatch, benchmark-like templates, and generator-specific artifacts that can produce misleading gains.
  - It links these failures to risks in medicine, law, finance, safety procedures, current events, generalization, and robustness.
- Missing:

### R4

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report covers mechanisms for bias reduction, including targeted coverage and counterfactual generation, while clearly distinguishing balanced or targeted synthetic examples from demonstrated improvements in real-world model behavior. It specifies the need for independent human-data confirmation.
- Candidate evidence:
  - It describes “counterfactual data augmentation and targeted prompts” that vary protected attributes while holding task content constant.
  - It notes that targeted augmentation can address “specific measured failure modes.”
  - It warns that generated counterfactuals may be unnatural, omit intersectional identities, or encode assumptions about bias.
  - It requires confirmation of apparent fairness improvements “on independently collected human data.”
  - It recommends subgroup and intersectional evaluation rather than relying on aggregate results.
- Missing:

### R5

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report comprehensively covers inherited generator bias, imbalance, stereotypes, minority underrepresentation, filtering effects, and amplification through augmentation or recursive training. It also distinguishes dataset-level balance or generated counterfactuals from actual model fairness by requiring downstream subgroup evaluation.
- Candidate evidence:
  - It states that synthetic data can reproduce and amplify bias from “the generator, its source data, its prompts, or the selection and filtering pipeline.”
  - It identifies overproduction of dominant languages, occupations, cultural assumptions, and demographic stereotypes from imbalanced web data.
  - It explains that confidence-based sampling or ranking can suppress minority or unconventional responses.
  - It notes that safety or quality filters may reject dialectal, minority, reclaimed, or culturally specific language.
  - It discusses recursive training and loss of minority patterns, as well as subgroup and intersectional evaluation.
- Missing:

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report gives a strong practical evaluation strategy and addresses factuality, validation, diversity, contamination, held-out real data, and downstream utility. It falls short of fully enumerating and explaining the limitations of all requested metric families, especially statistical distributional measures and model-based synthetic-data metrics.
- Candidate evidence:
  - It recommends held-out real-world data and separation of training, development, and test provenance.
  - It calls for evaluation of “factuality, calibration, refusal behavior, robustness,” subgroup slices, temporal holdouts, out-of-distribution inputs, and adversarial tests.
  - It recommends executable checks, retrieval, experts, or humans for validation and notes that these approaches vary by whether an independent oracle exists.
  - It warns that filtering based only on “perplexity or similarity” can remove useful difficult examples while retaining plausible errors.
  - It states that automated judges are “measurements with error, not ... ground truth.”
  - It identifies generator-specific artifacts, synthetic-text overfitting, and synthetic-only or aligned benchmark risks.
- Missing:
  - A more explicit, organized evaluation framework covering distribution fidelity, semantic or label correctness, diversity, coverage, and training utility as separate complementary dimensions.
  - More direct discussion of the limitations of statistical similarity metrics and model-based quality metrics beyond the treatment of perplexity, similarity, and automated judges.

### R7

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report directly specifies real-data baselines or independent held-out data, subgroup-sensitive and intersectional evaluation, and comparison of behavior rather than dataset balance. It also includes practical fairness and representational safeguards for deployment.
- Candidate evidence:
  - It recommends “independent, human- or domain-validated real-world data” and assessment of “average performance and worst-case subgroup behavior.”
  - It calls for “subgroup and intersectional slices,” out-of-distribution inputs, adversarial testing, and post-deployment incident monitoring.
  - It warns that fairness improvements on synthetic tests require confirmation on independently collected human data.
  - It states that aggregate benchmark improvements can conceal harm to smaller or intersecting groups.
  - It recommends measuring “subgroup and tail performance” and judging systems by “downstream reliability and harm rates, not by volume or benchmark gains alone.”
- Missing:

### R8

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report reaches a conditional and evidence-oriented conclusion, explicitly acknowledges uncertainty and conflicting findings, and provides concrete safeguards and decision criteria. It appropriately frames synthetic data as targeted augmentation whose value depends on task, generation, verification, composition, and evaluation conditions.
- Candidate evidence:
  - The conclusion states that synthetic data is “neither inherently beneficial nor inherently harmful.”
  - It relates outcomes to task type, generator strength, verification availability, filtering, mixture ratios, model scale, domain, and evaluation contamination controls.
  - It identifies open-ended factual, social, medical, and legal tasks as riskier than code, mathematics, and structured extraction with independent checks.
  - It acknowledges unsettled evidence on model collapse, conflicting findings, and the absence of a universal synthetic-to-real ratio or filtering recipe.
  - It recommends provenance retention, deduplication, executable or expert verification, subgroup and tail measurement, independent real-world final evaluation, and post-deployment monitoring.
- Missing:

### Novel Value

- The report offers a useful synthesis connecting synthetic-data benefits to the availability of independent verification or an external correctness oracle.
- It emphasizes that synthetic data can distort evaluation through generator-specific ease and artifacts, not merely through conventional train-test contamination.
- It integrates data quality, fairness, privacy, provenance, recursive training, and post-deployment monitoring into a practical hybrid-data strategy.

## Citations

### Support

#### F1: NOT_EVALUABLE

- Claim: Synthetic data can lower the marginal cost of producing large-scale instruction, preference, and domain-specific training examples.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F2: NOT_EVALUABLE

- Claim: Synthetic data is useful for coverage: it can target rare skills, long-tail cases, structured formats, languages, safety scenarios, and controllable difficulty levels that are expensive or difficult to collect from people.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F3: NOT_EVALUABLE

- Claim: Synthetic data can improve privacy and reduce some data-collection burdens, but it is not automatically private or safe from memorization and inference attacks.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F4: NOT_EVALUABLE

- Claim: Synthetic data can degrade data quality through hallucinations, internal inconsistencies, formatting artifacts, and loss of information that is difficult for the generator to represent.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F5: NOT_EVALUABLE

- Claim: Training recursively on model-generated data can cause distributional collapse, especially when synthetic data replaces rather than supplements fresh human-originated data.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F6: NOT_EVALUABLE

- Claim: Synthetic data can reproduce and amplify social, cultural, linguistic, and demographic biases present in the generator, its source data, its prompts, or the selection and filtering pipeline.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F7: NOT_EVALUABLE

- Claim: Synthetic data can reduce some measured biases when deliberately generated as counterfactual or balanced examples, but apparent balance may be superficial and may not improve behavior on naturally occurring cases.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F8: NOT_EVALUABLE

- Claim: Synthetic data can make evaluation less reliable by creating benchmark contamination, distribution mismatch, and artificial ease.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F9: NOT_EVALUABLE

- Claim: Evaluation should use independent, human- or domain-validated real-world data in addition to synthetic tests, and should assess both average performance and worst-case subgroup behavior.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F10: NOT_EVALUABLE

- Claim: The practical value of synthetic data is highest when generation is task-specific and verification is cheap or independent; it is lowest when correctness is open-ended and errors are consequential.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

### Missing Citations

- Q1: Synthetic data can lower the marginal cost of producing large-scale instruction, preference, and domain-specific training examples.
- Q2: Synthetic data can target rare skills, long-tail cases, structured formats, languages, safety scenarios, and controllable difficulty levels that are expensive or difficult to collect from people.
- Q3: Synthetic data can improve privacy and reduce some data-collection burdens, but ordinary synthetic generation is not automatically private or safe from memorization and inference attacks.
- Q4: Synthetic data can degrade data quality through hallucinations, internal inconsistencies, formatting artifacts, and loss of information that is difficult for the generator to represent.
- Q5: Recursive training on model-generated data can cause distributional collapse, particularly when synthetic data replaces rather than supplements fresh human-originated data.
- Q6: Synthetic data can reproduce and amplify social, cultural, linguistic, and demographic biases present in the generator, source data, prompts, or selection and filtering pipeline.
- Q7: Deliberately generated counterfactual or balanced synthetic examples can reduce some measured biases, but apparent balance may be superficial and may not improve behavior on naturally occurring cases.
- Q8: Synthetic data can make evaluation less reliable through benchmark contamination, distribution mismatch, and artificial ease.
- Q9: Evaluation should use independent, human- or domain-validated real-world data in addition to synthetic tests and assess both average performance and worst-case subgroup behavior.
- Q10: The practical value of synthetic data is highest when generation is task-specific and verification is cheap or independent, and lowest when correctness is open-ended and errors are consequential.
- Q11: Reported gains from synthetic instruction tuning are difficult to compare because datasets, teacher models, filtering, real-data mixtures, and evaluation-contamination controls differ substantially.
- Q12: There is no universal synthetic-to-real data ratio or filtering recipe; optimal choices vary by domain, model scale, generator quality, verification method, and target capability.
- Q13: Fairness results are sensitive to language, culture, identity taxonomy, and deployment context, and aggregate benchmark improvements can conceal harm to smaller or intersecting groups.
- Q14: Evidence remains limited on recursive use of synthetic data across multiple generations of commercial models and fine-tuning datasets.
- Q15: Evaluation methods for detecting subtle generator artifacts, synthetic-text overfitting, and loss of long-tail knowledge remain immature.
- Q16: Standardized reporting of synthetic-data provenance, generator checkpoints, prompt templates, filtering rules, human-review rates, and synthetic-to-real ratios is limited.
- Q17: Synthetic data should generally supplement rather than replace independently sourced real data, with provenance retention, deduplication, verification, subgroup and tail-performance measurement, and independent real-world final evaluation.

## Deterministic Checks

- `run_metadata_loads`: PASS
- `report_exists`: PASS
- `sources_present`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `structured_report_parses`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `report_question_matches`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `source_ids_unique`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `source_ids_syntactically_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `source_urls_present`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `evidence_objects_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `confidence_values_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `citation_ids_syntactically_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `citation_ids_resolve`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `structured_claim_evidence_available`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `ledger_claim_ids_unique`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `ledger_evidence_relationships_resolve`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `ledger_confidence_values_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `ledger_evidence_ids_unique`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.

## Main Weaknesses

1. 17 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `36414e911184eea8ef62c41ba8423e71054770da6d3e515f90d477a9870e806e`
- Candidate report hash: `bf72923ebaeec6a9e93970f2c6a8a107a709faf3a45cb71b191114d06f7635de`
- LLM calls: 2
- Evaluated at: 2026-09-01T06:02:21.040950+00:00
