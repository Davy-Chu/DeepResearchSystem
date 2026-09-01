# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** synthetic-data-llm-training

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 81.3 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.72
- Coverage: 0.72
- Depth: 0.72
- Citation quality: 0.94
- Citation validity: 1.00
- Citation support: 0.89
- Citation completeness: 1.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes replacement versus supplementation and recursive use, but the scope distinctions are incomplete. The evidence does not adequately cover generation method or pretraining/fine-tuning differences.
- Candidate evidence:
  - The report distinguishes “purely recursive or replacement-based synthetic training” from “real-data mixing” and discusses synthetic data for “fine-tuning” in Finding 3 and Finding 7.
  - It states that synthetic data may be generated from “one model” and recommends “diverse generation sources.”
- Missing:
  - It does not clearly define the major synthetic-data sources, such as LLM-generated text versus programmatically generated or simulated data.
  - It gives little or no treatment of pretraining versus fine-tuning as distinct regimes; most discussion centers on fine-tuning and recursive training.
  - It does not systematically explain why these setting differences change the relevant risks and benefits.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report covers the principal potential quality benefits and appropriately notes that volume alone is insufficient. However, evidence for actual model-quality gains is relatively general and partly based on practitioner sources.
- Candidate evidence:
  - The Summary says synthetic data can be “cheaper, faster, more scalable, and better targeted to rare or underrepresented cases.”
  - Finding 1 identifies augmentation of scarce resources, reduced annotation and collection costs, privacy-sensitive workflows, class-imbalance support, and rare or difficult scenarios.
  - Finding 4 explains that diversity and curation matter and that “volume alone does not ensure useful training data.”
- Missing:
  - The report gives limited concrete evidence about increased coverage, diversity, label availability, or improved downstream model quality across LLM tasks.
  - It does not sharply distinguish cost/scalability advantages from demonstrated improvements in model accuracy, generalization, or robustness.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is a strong treatment of distributional distortion, repetition, diversity loss, collapse, and robustness degradation. It is less complete on factuality, labeling errors, contamination, and other specific quality failures.
- Candidate evidence:
  - Finding 3 discusses distribution narrowing, reduced diversity, omitted low-probability valid cases, model collapse, and task-specific regressions.
  - It reports that aggregate translation quality could remain stable while markup-transfer capability declined.
  - Finding 7 reports reduced adversarial robustness despite preserved output quality.
  - The Summary and Conclusion identify unfiltered, repetitive, single-source, weakly filtered, or recursively recycled data as especially risky, and recommend source diversity, deduplication, filtering, and real-data retention.
- Missing:
  - Factual errors, semantic errors, and incorrect labels are mentioned only indirectly through “semantic validation” and “treated as ground truth,” rather than analyzed as distinct failure modes.
  - Artifacts, contamination, and distribution mismatch are not developed in detail.
  - The report gives limited explanation of how generator quality, target-model capability, domain, prompting, or synthetic-to-real ratios alter the likelihood of each failure.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report captures targeted coverage, balancing, validation, tradeoffs, and the distinction between dataset balance and model fairness. It would be stronger with a more explicit intervention taxonomy and LLM-specific causal comparisons.
- Candidate evidence:
  - Finding 1 identifies targeting rare or underrepresented examples as a benefit.
  - Finding 6 says targeted synthetic generation may improve subgroup coverage or downstream fairness but that nominal balancing may reduce utility or fail under deployment-distribution mismatch.
  - The report describes an “audit-diagnose-generate-validate-retrain-re-audit” workflow and recommends demographic and semantic bias audits.
  - It explicitly states that “a more balanced synthetic dataset” is not sufficient and that fairness claims require realistic distributions and strong baselines.
- Missing:
  - Counterfactual generation, fairness-aware prompting, weighting, and filtering are not explained as distinct intervention mechanisms.
  - The report does not specify a detailed evidence design for attributing fairness improvement to synthetic data, such as matched real-data-only and synthetic-augmentation ablations across multiple subgroups.
  - Most direct controlled evidence is acknowledged to concern non-LLM domains rather than LLM fine-tuning.

### R5

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report covers generator bias, stereotypes, demographic distortion, underrepresentation, and uncertainty about transfer to trained models. It needs more explicit treatment of spurious correlations and model-level amplification evidence.
- Candidate evidence:
  - Finding 5 reports stereotypes and demographic-distribution bias in profiles generated by all four examined LLMs.
  - It identifies reproduction of stereotypes, demographic distortions, incorrect associations, unrealistic subgroup examples, underrepresentation, and possible bias amplification.
  - The report states that the downstream effect on LLM fine-tuning is “less directly established,” distinguishing generated-content bias from downstream model effects.
  - Finding 6 and the Conflicts section discuss domain gaps, realistic imbalanced distributions, and amplification risks.
- Missing:
  - Spurious correlations and class or subgroup imbalance are not examined in as much detail as stereotypes and underrepresentation.
  - The mechanism by which iterative or large-scale synthetic training amplifies generator bias is asserted more than demonstrated.
  - Downstream model-level measurements of subgroup performance, error disparities, or representation are not supplied.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report gives a solid multidimensional and deployment-oriented evaluation framework, including real or human validation and capability-specific checks. Metric-specific limitations and fit-for-training criteria remain underdeveloped.
- Candidate evidence:
  - Finding 9 recommends multidimensional evaluation using human or trusted ground truth, plausibility and consistency checks, realistic population distributions, subgroup slices, edge and adversarial cases, and downstream outcome validation.
  - It notes that task-specific measures are needed because aggregate quality can remain stable while markup transfer or adversarial robustness declines.
  - Finding 8 warns that synthetic evaluation data can bias absolute performance estimates and should not be the sole basis for deployment decisions.
  - The Conclusion recommends held-out, realistic, adversarial, uncertainty-aware, and workflow-level tests.
- Missing:
  - The report does not organize the evaluation dimensions explicitly around factuality, semantic or label correctness, distribution fidelity, diversity, coverage, training utility, and held-out-real-data generalization.
  - Limitations of statistical metrics, human judgments, model-based metrics, and perplexity-style measures are not separately explained.
  - It does not explicitly warn that metrics aligned with the generator or tests using only synthetic data can reward generator artifacts, although related warnings are present.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: The required direction is present: use realistic or held-out data, subgroup-sensitive measures, and strong baselines rather than balance alone. The evaluation protocol lacks operational detail and explicit baseline specifications.
- Candidate evidence:
  - Finding 6 says fairness gains require realistic distributions and identifies fairness–utility tradeoffs and gaps between artificially balanced and realistic imbalanced tests.
  - The Conflicts section says fairness claims require “realistic distributions and comparison with strong baselines.”
  - Finding 9 recommends subgroup slices, realistic population distributions, downstream outcome validation, and uncertainty-aware fairness measures.
  - The Conclusion recommends subgroup-specific and uncertainty-aware tests rather than relying on balanced or synthetic benchmarks.
- Missing:
  - The report does not consistently specify a concrete no-synthetic or real-data-only baseline and matched ablation design.
  - It mentions subgroup slices and fairness measures but gives few concrete metrics for subgroup performance, error rates, representation, calibration, or disparity.
  - The distinction between fairness measured in the synthetic dataset and fairness observed in the trained model could be made more explicit.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report reaches a well-supported conditional conclusion and provides practical safeguards. It lacks a more systematic decision framework covering capability, prompting, training regime, and use case.
- Candidate evidence:
  - The Summary and Conclusion reject universal verdicts and recommend synthetic data as a “controlled supplement” or “targeted augmentation.”
  - The report conditions outcomes on source diversity, filtering, deduplication, real-data retention, task, data mixture, recycling regime, domain gaps, and evaluation protocol.
  - It acknowledges uncertainty about synthetic-to-real ratios, privacy guarantees, downstream bias transfer, and deployment validity.
  - The Conclusion provides safeguards including trusted real or human anchors, external grounding, demographic and semantic audits, held-out realistic tests, adversarial testing, and workflow-level evaluation.
- Missing:
  - Generator capability and target-model capability are not clearly analyzed as separate conditions.
  - Prompting and training-regime choices are only lightly addressed, and the report does not give practical decision criteria for choosing a synthetic-data fraction or stopping use.
  - The conclusion could more explicitly distinguish when synthetic data is likely beneficial for pretraining, instruction tuning, preference data, or safety fine-tuning.

### Novel Value

- The report offers a useful synthesis that separates synthetic-data benefits from claims of downstream model improvement and repeatedly emphasizes conditionality.
- It highlights the important possibility that aggregate quality can remain stable while specific capabilities, adversarial robustness, or safety safeguards deteriorate.
- It identifies evaluation-data bias as potentially more damaging to absolute performance estimates than to relative rankings, while cautioning against generalizing that result across deployment settings.
- It explicitly records unresolved evidence gaps, including synthetic-to-real ratios, downstream transfer of generator bias, privacy validation, and capability-specific regressions.

## Citations

### Support

#### F1: SUPPORTED

- Claim: Synthetic data provides practical benefits by expanding scarce training resources, reducing annotation and collection costs, supporting privacy-sensitive workflows, and targeting rare, edge-case, or underrepresented examples.
- Sources: S1, S3, S4, S9
- Rationale: The cited sources collectively support all important elements of the claim. S3 explicitly describes synthetic data as addressing scarce training data, supplementing human-labeled data, helping with privacy-sensitive information, and covering rare edge cases; it also says synthetic examples expand limited labeled datasets and reduce the need for expensive collection. S4 supports reduced annotation and collection costs, privacy-preserving training, and generation of rare or underrepresented examples. S9 states that synthetic data is cheaper, easier to iterate on, and lowers experiment and research costs. S1 summarizes benefits involving data scarcity, privacy constraints, and class imbalance.
- Supporting text: S3: Synthetic data can supplement or replace human-labeled data, is valuable for privacy-sensitive information and rare edge cases, and can expand limited labeled datasets. S4: It reduces annotation, collection, revision, and compliance costs; supports training without exposing patient data; and generates rare or underrepresented scenarios. S9: It is “far cheaper and easier to iterate on,” lowering the price of experiments and research.

#### F2: SUPPORTED

- Claim: Synthetic data is generally safer and more useful as a supplement to real or externally grounded data than as an unverified replacement for it.
- Sources: S1, S2, S5, S7, S9
- Rationale: The sources consistently support both parts of the claim: synthetic data can be useful for expanding training resources and improving specific tasks, while replacing real data or using unfiltered, unverified synthetic outputs creates risks such as model collapse, distribution narrowing, degraded generalization, and safety or audit problems. They also describe safer additive practices, including retaining or mixing real data, using diverse sources, deduplication, quality filters, and external verification.
- Supporting text: S2 states that “the fix is not avoiding synthetic data, it's accumulating real data alongside it rather than replacing it,” and reports bounded error when synthetic data accumulates with real data versus unbounded growth when it replaces real data. S9 similarly says that mixing real/human data, diverse teachers, deduplication, and strong quality filters largely avoid collapse, while S5 notes that synthetic data can expand resources and improve specific tasks but must be novel, reliable, verifiable, and sustainable.

#### F3: PARTIALLY_SUPPORTED

- Claim: The main data-quality risk is distributional distortion: repeated, single-source, or weakly filtered synthetic data can reduce diversity, omit low-probability valid cases, and cause model collapse or task-specific regressions.
- Sources: S2, S5, S7, S9, S19
- Rationale: S2, S7, and S9 directly support the distributional-distortion mechanism: repeated or indiscriminate synthetic training can narrow output distributions, reduce diversity, underrepresent rare or low-probability valid cases, and cause model collapse. They also support the risks of single-source data and the mitigating role of filtering and deduplication. S5 broadly supports stagnation or degradation when synthetic data lacks new information or external feedback. However, the claim’s wording that this is the “main” data-quality risk is not established, and S19 does not support a general regression claim: in its specific markup-translation study, synthetic data slightly worsened markup transfer but did not negatively affect translation quality. Thus, only a narrower version of the claim is supported.
- Supporting text: S2: indiscriminate model-generated training content causes irreversible defects and successive generations “lose the tails of the original data distribution.” S7: higher synthetic-source diversity mitigates distribution collapse; iterative self-tuning narrows output distributions and reduces linguistic diversity. S9: self-training on unfiltered, repetitive, single-model outputs can underrepresent rare facts and styles and worsen generalization; mixing real data, diverse teachers, deduplication, and quality filters reduces this risk.

#### F4: SUPPORTED

- Claim: Synthetic-data diversity and curation are important determinants of quality; volume alone does not ensure useful training data.
- Sources: S2, S7, S9, S22
- Rationale: The sources directly support both parts of the claim. S2 explicitly states that synthetic-data quality depends on curation discipline rather than volume, and that volume without curation amplifies failure modes. S7 reports that greater source diversity mitigates distribution collapse. S9 similarly links diverse teachers, deduplication, and quality filters to avoiding collapse, while S22 describes expert validation and curation as safeguards for accuracy and diversity.
- Supporting text: S2: “not volume, but curation discipline”; “Volume without curation amplifies failure modes.” S7: “higher source diversity mitigating” distribution collapse. S9: “using diverse teachers, deduplication, and strong quality filters largely avoids” collapse.

#### F5: SUPPORTED

- Claim: Synthetic data does not automatically reduce bias and can reproduce stereotypes, demographic distortions, incorrect associations, or unrealistic subgroup examples.
- Sources: S3, S4, S10, S14, S15
- Rationale: The sources collectively support the claim. S4 explicitly warns that synthetic data can amplify existing biases, underrepresent demographics, and lack realism. S14 reports that LLM-generated profiles exhibit stereotype bias and demographic-distribution deviation, including associations between demographic groups and personal attributes. S15 identifies limitations in synthetic-data diversity and quality, domain and bias gaps, and model misrepresentation. S10 also emphasizes that mitigation requires targeted generation, validation, and re-auditing rather than occurring automatically. S3 reinforces that synthetic-data utility depends on validation and alignment with the target distribution.
- Supporting text: S4: “poorly designed generators can reproduce or exaggerate existing biases,” may underrepresent demographics, and may produce examples lacking realism. S14: LLM-generated content showed “significant stereotype bias and deviation bias,” including demographic associations with attributes such as religion and sexual orientation. S15: synthetic data can have limited diversity and quality, domain/bias gaps, and misrepresentation.

#### F6: SUPPORTED

- Claim: Targeted synthetic generation may improve subgroup coverage or downstream fairness, but nominal balancing alone can reduce utility or fail to improve real-world fairness when the synthetic distribution differs from deployment data.
- Sources: S10, S13, S15
- Rationale: The sources collectively support the claim. S10 describes generating targeted records for under-represented subgroups and validating fairness, utility, distributional fit, and real-world performance. S15 directly reports that balanced synthetic data can improve fairness but reduce accuracy because of a domain gap, while blindly fine-tuning on synthetic data decreases utility; it also reports that a selective approach improves fairness while maintaining utility. S13 finds that fairness gains observed on artificially balanced test data may not generalize to realistic imbalanced distributions. The sources support the stated caveat, though “deployment data” is represented as real-world or realistic distributions rather than explicitly named deployment data.
- Supporting text: S10: “Produce targeted synthetic records for under-represented slices” and validate “distributional fit, task utility”; targeted expansion “can help reduce this gap when paired with held-out evaluation and real-world validation.” S15: “models trained on balanced synthetic data show better fairness but poorer accuracy due to a ‘domain gap’ between the real and synthetic data,” and “Fine-tuning blindly on the synthetic will result in a model with decreased utility.” S13: fairness improvements on “artificially balanced test sets” “may not generalize to real-world settings.”

#### F7: SUPPORTED

- Claim: Synthetic fine-tuning can preserve ordinary output quality while weakening adversarial robustness or safety safeguards.
- Sources: S7, S3, S5
- Rationale: S7 directly reports that synthetic fine-tuning decreases adversarial robustness while preserving output quality, and also states that synthetic fine-tuning can remove safeguards while preserving higher output quality. S3 and S5 provide only general context about synthetic data and safety, but S7 alone supports the claim’s important factual content.
- Supporting text: S7: “Synthetic fine-tuning data leads to decreases in LLMs’ adversarial robustness while preserving output quality,” and “fine-tuning models on synthetic data ... can remove safeguards, [while] the latter preserves higher output quality.”

#### F8: PARTIALLY_SUPPORTED

- Claim: Synthetic evaluation data can scale testing and support controlled or relative comparisons, but it can systematically bias absolute performance estimates and should not be the sole basis for deployment decisions.
- Sources: S16, S3, S4, S5, S8
- Rationale: S16 directly supports scalable evaluation, systematic bias in synthetic test collections, distortion of absolute performance estimates, and the possibility that relative comparisons are less affected. S8 supports controlled, diverse, and scalable testing environments. S3 supports evaluation benchmarking and systematic generation of test cases. S4 supports the need to benchmark synthetic-data-based systems against trusted real-world datasets and retain human oversight. However, the supplied text does not explicitly state that synthetic evaluation data should never be the sole basis for deployment decisions; that is a reasonable implication of the validation and oversight recommendations but is not directly established.
- Supporting text: S16: synthetic test collections can scale evaluation, exhibit significant bias when computing absolute system performance, and may have a smaller effect when comparing relative system performance. S8: synthetic data enables “controlled, diverse, and scalable testing environments.” S4: models still need benchmarking against trusted real-world datasets, and organizations need human oversight and evaluation loops.

#### F9: SUPPORTED

- Claim: Evaluation should be multidimensional and deployment-relevant rather than limited to aggregate benchmark accuracy.
- Sources: S3, S4, S12, S13, S17, S7, S19
- Rationale: The saved sources collectively support both elements of the claim. They describe evaluation across multiple dimensions—including fairness across subgroups, uncertainty, robustness, diversity, realism, safety, and self-preference—and emphasize realistic or real-world distributions and outcomes rather than relying solely on aggregate accuracy or benchmark scores.
- Supporting text: S12 describes a three-pronged evaluation using accuracy against human abstractors, consistency and plausibility checks, and replication of clinical outcomes. S17 states that conventional accuracy-based fairness metrics miss uncertainty and proposes a finer-grained metric. S13 warns that artificially balanced test sets may produce gains that do not generalize to real-world settings. S7 notes that standard performance benchmarks miss output-distribution changes and examines robustness and self-preference bias. S4 recommends evaluating accuracy, diversity, and realism, including against trusted real-world datasets and with human evaluation.

### Missing Citations

- None identified.

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

1. R1: Define the synthetic-data settings relevant to the analysis and explain why their differences matter.
2. 2 cited finding(s) were not fully supported by saved evidence.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `36414e911184eea8ef62c41ba8423e71054770da6d3e515f90d477a9870e806e`
- Candidate report hash: `2f415407da10166be6f915cf39f8d5fffd3306e565b249fb48009591db90e5cb`
- LLM calls: 11
- Evaluated at: 2026-09-01T10:48:00.524476+00:00
