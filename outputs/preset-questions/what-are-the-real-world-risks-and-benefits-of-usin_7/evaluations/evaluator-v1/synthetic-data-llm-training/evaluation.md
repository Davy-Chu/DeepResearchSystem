# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** synthetic-data-llm-training

**System Version:** llm-only-baseline-v0

**Model:** gpt-5.6-luna

## Summary

- Overall: 68.1 / 100
- Evaluation completeness: 80%
- Comprehensiveness: 0.97
- Coverage: 0.97
- Depth: 0.97
- Citation quality: 0.00
- Citation validity: 0.00
- Citation support: 0.00
- Citation completeness: 0.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report avoids treating all synthetic data as equivalent and gives useful distinctions around generator provenance, training mixtures, and verification. However, the pretraining/fine-tuning distinction and programmatic-generation setting are not explicitly framed and compared.
- Candidate evidence:
  - The report distinguishes model-generated synthetic data, different generation and verification pipelines, and synthetic data used as a supplement versus replacement for real data.
  - It discusses instruction tuning, preference data, domain-specific examples, and recursive training, and notes that outcomes vary by task, model scale, generator quality, and synthetic-to-real ratio.
  - It distinguishes ordinary prompted generation from differentially private synthetic-data methods.
- Missing:
  - Pretraining is not explicitly distinguished from fine-tuning or instruction tuning, even though the rubric specifically asks about those different training settings.
  - Programmatically generated synthetic data is only implied through examples such as simulators, executable environments, compilation, and symbolic verification rather than clearly defined as a separate setting.
  - The report does not systematically explain how each setting changes the relevant risks and benefits.

### R2

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report thoroughly covers scale, cost-enabled quality improvements, coverage, rare and edge cases, controllable difficulty, diversity-related goals, and label or verification availability.
- Candidate evidence:
  - Finding 1 explains that synthetic data lowers the cost of producing large-scale instruction, preference, and domain-specific examples, citing Self-Instruct, Constitutional AI, and Phi-1-related work.
  - Finding 2 explains targeted coverage of rare skills, long-tail cases, structured formats, languages, safety scenarios, controllable difficulty, mathematics, coding, multilingual tasks, and tool use.
  - The report explains that automatically checkable answers and execution environments can improve quality control and that quality and task targeting can matter more than raw volume.
- Missing:

### R3

- Coverage: 1.00
- Depth: 1.00
- Rationale: The candidate addresses the principal data-quality failure modes and connects them to downstream effects and conditions under which they become more or less likely.
- Candidate evidence:
  - Finding 4 identifies hallucinations, internal inconsistencies, formatting artifacts, factual errors, repetitive phrasing, generic explanations, reduced lexical or conceptual diversity, and plausible errors retained by simplistic filtering.
  - Finding 5 explains recursive synthetic-data training, loss of distributional tails, distortion, and special vulnerability of rare events and minority patterns.
  - Finding 8 discusses contamination, train-test leakage, distribution mismatch, synthetic-test artifacts, and artificial ease.
  - The report connects these problems to degraded accuracy, generalization, robustness, factual reliability, and real-world reliability, and identifies moderating factors such as filtering, mixture ratios, model capacity, task, and external verification.
- Missing:

### R4

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report covers concrete bias-reduction mechanisms and clearly distinguishes balanced or targeted synthetic data from demonstrated improvement in real-world model behavior, including the needed validation comparison.
- Candidate evidence:
  - Finding 7 discusses counterfactual data augmentation, targeted prompts, balanced examples, and varying protected attributes while holding task content constant.
  - It warns that superficial balance may not improve naturally occurring cases and that generated counterfactuals may be unnatural, omit intersectional identities, or encode model and annotator assumptions.
  - It explicitly requires confirmation on independently collected human data before treating synthetic fairness-test improvements as meaningful.
- Missing:

### R5

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report comprehensively covers inherited, introduced, and amplified demographic and representational bias, including subgroup imbalance, stereotypes, spurious associations, filtering effects, and iterative amplification.
- Candidate evidence:
  - Finding 6 explains that synthetic data can inherit bias from the generator, source data, prompts, selection, ranking, and filtering pipelines.
  - It addresses dominant-language and cultural imbalance, demographic stereotypes, biased associations, suppression of minority or unconventional responses, and bias introduced by rejecting dialectal, minority, reclaimed, or culturally specific language.
  - Finding 5 explains amplification and loss of minority patterns through recursive training and large-scale model-generated distributions.
  - The report distinguishes synthetic-data or benchmark balance from downstream behavior by stating that direction and magnitude must be measured for each population, language, and use case.
- Missing:

### R6

- Coverage: 1.00
- Depth: 1.00
- Rationale: The candidate gives a genuinely multi-dimensional evaluation strategy covering correctness, fidelity and distributional concerns, diversity and coverage, utility, held-out real-data generalization, and limitations of automated, perplexity-style, and synthetic-aligned tests.
- Candidate evidence:
  - Finding 9 recommends held-out, independent, human- or domain-validated real-world data and separate provenance for training, development, and test sets.
  - It lists factuality, calibration, refusal behavior, robustness, confidence intervals, temporal holdouts, out-of-distribution inputs, adversarial testing, subgroup slices, and post-deployment monitoring.
  - Finding 4 warns that perplexity-only or similarity-only filtering can remove useful difficult examples while retaining plausible errors.
  - Finding 8 warns that synthetic tests can share templates, vocabulary, answer styles, and assumptions with synthetic training data, making generator-aligned or synthetic-only performance misleading.
  - Finding 10 recommends independent verification through compilation, tests, symbolic or numerical checks, database constraints, retrieval, simulators, experts, or humans, while acknowledging correlated generator errors.
- Missing:

### R7

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report specifies appropriate real-data validation and subgroup-sensitive evaluation, and it focuses on downstream performance and harm rather than dataset balance or prompts alone.
- Candidate evidence:
  - Finding 7 requires confirmation of counterfactual or balanced-data improvements on independently collected human data.
  - Finding 9 recommends subgroup and intersectional slices, worst-case behavior, adversarial and red-team testing, temporal holdouts, out-of-distribution inputs, and post-deployment incident monitoring.
  - The report states that fairness results are sensitive to language, culture, identity taxonomy, and deployment context, and that aggregate gains can conceal harm to smaller or intersecting groups.
  - The conclusion recommends measuring subgroup and tail performance and judging synthetic data by downstream reliability and harm rates rather than volume or benchmark gains.
- Missing:

### R8

- Coverage: 1.00
- Depth: 1.00
- Rationale: The candidate reaches a nuanced, evidence-based conclusion, explicitly acknowledges uncertainty and conflicting findings, identifies favorable and unfavorable conditions, and supplies practical safeguards and decision criteria.
- Candidate evidence:
  - The summary and conclusion give a conditional position: synthetic data is useful for targeted augmentation and development but should generally supplement rather than replace independently sourced real data.
  - Finding 10 identifies task-specific generation and cheap or independent verification as favorable conditions, while open-ended, consequential domains are unfavorable.
  - The report conditions outcomes on generator and target-model quality, task and domain, verification, filtering, mixture ratios, provenance, model scale, and evaluation contamination controls.
  - The conflicts and uncertainty section acknowledges unsettled evidence on model collapse, incomparable reported gains, lack of a universal synthetic-to-real ratio, and context-sensitive fairness results.
  - The conclusion provides safeguards including provenance, deduplication, executable or expert verification, subgroup and tail testing, independent real-world evaluation, and post-deployment monitoring.
- Missing:

### Novel Value

- The report adds useful synthesis by linking synthetic-data benefits to the availability of independent verification or an external oracle, distinguishing settings such as code and mathematics from open-ended factual or social claims.
- It emphasizes evaluation contamination and generator-aligned artifacts as a distinct risk, rather than treating benchmark performance as evidence of real-world quality.
- It integrates recursive distributional degradation with minority and long-tail loss, connecting data-quality risks to representational harms.
- It gives a practical hybrid-data strategy with provenance, deduplication, subgroup evaluation, independent real-data testing, and post-deployment monitoring.

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
- Q3: Differentially private synthetic-data methods can provide formal privacy guarantees when the generation pipeline is differentially private, whereas ordinary prompting of a model to produce synthetic records does not provide that guarantee.
- Q4: Language models can memorize and emit portions of their training data, including names, passages, confidential facts, or rare personal information.
- Q5: Synthetic data can degrade data quality through hallucinations, internal inconsistencies, formatting artifacts, and loss of information that is difficult for the generator to represent.
- Q6: Synthetic corpora can contain recognizable stylistic signatures, repetitive phrasing, generic explanations, and reduced lexical or conceptual diversity.
- Q7: Recursive training on model-generated data can cause distributional collapse, including loss of the tails of the original distribution and progressive distortion of the learned distribution.
- Q8: Synthetic data can reproduce and amplify social, cultural, linguistic, and demographic biases present in the generator, its source data, prompts, selection process, or filtering pipeline.
- Q9: Counterfactual or balanced synthetic examples can reduce some measured biases, but apparent balance may be superficial and may not improve behavior on naturally occurring cases.
- Q10: Synthetic data can make evaluation less reliable through benchmark contamination, distribution mismatch, and artificial ease.
- Q11: Training data generated by a model that has seen a benchmark, or generated from benchmark-like prompts, can produce apparent performance gains through memorization or format familiarity rather than generalization.
- Q12: Synthetic test sets can share templates, vocabulary, answer styles, and assumptions with synthetic training sets, allowing models to exploit generator-specific artifacts absent from real user interactions.
- Q13: Independent, human- or domain-validated real-world data should be used alongside synthetic tests, with assessment of average performance and worst-case subgroup behavior.
- Q14: Code can often be checked by compilation and tests, mathematics by symbolic or numerical verification, and structured extraction by database constraints, while open-ended factual, social, medical, and legal claims are harder to validate automatically.
- Q15: Strong teachers, retrieval systems, simulators, executable environments, or human/domain review can improve the trustworthiness of synthetic examples, but they add cost and do not eliminate correlated generator errors.
- Q16: The extent of model collapse in real production training is unsettled, and reported effects vary with synthetic-to-real ratios, filtering, model capacity, task, and data provenance.
- Q17: Reported gains from synthetic instruction tuning are difficult to compare because datasets, teacher models, filtering, real-data mixtures, and contamination controls differ substantially.
- Q18: There is no universal synthetic-to-real data ratio or filtering recipe; optimal choices vary by domain, model scale, generator quality, verification method, and target capability.
- Q19: Fairness results are sensitive to language, culture, identity taxonomy, and deployment context, and aggregate benchmark improvements can conceal harm to smaller or intersecting groups.
- Q20: A defensible strategy is to use synthetic data as a supplement rather than a replacement for independently sourced real data, retain provenance, deduplicate against training and test sets, verify examples, measure subgroup and tail performance, and reserve independent real-world data for final evaluation.

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

1. 20 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `36414e911184eea8ef62c41ba8423e71054770da6d3e515f90d477a9870e806e`
- Candidate report hash: `bf72923ebaeec6a9e93970f2c6a8a107a709faf3a45cb71b191114d06f7635de`
- LLM calls: 2
- Evaluated at: 2026-09-01T05:51:47.674658+00:00
