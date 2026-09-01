# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** synthetic-data-llm-training

**System Version:** evidence-ledger-decomposer-verifier-v1

**Model:** gpt-5.6-luna

## Summary

- Overall: 77.1 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.71
- Coverage: 0.72
- Depth: 0.69
- Citation quality: 0.82
- Citation validity: 1.00
- Citation support: 0.70
- Citation completeness: 0.94
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report recognizes that training regime and the replacement-versus-mixing distinction matter, but it does not provide a complete, explicit taxonomy of synthetic-data settings or explain each distinction in sufficient depth.
- Candidate evidence:
  - The report distinguishes additive synthetic data from recursive replacement: “synthetic data can be useful ... when it supplements rather than replaces independently sourced real data.”
  - It separately discusses synthetic fine-tuning and notes a gap in distinguishing “synthetic pretraining from synthetic fine-tuning effects.”
  - It describes “synthetic, human, and mixed-data training regimes” as distinct comparison conditions.
- Missing:
  - It does not clearly define the full range of relevant settings, including LLM-generated versus programmatically generated data.
  - Pretraining, fine-tuning, pure-synthetic, and mixed synthetic-real regimes are mentioned but not systematically explained in terms of why their risks and benefits differ.
  - The report does not clearly distinguish synthetic data used for pretraining from synthetic data used for supervised fine-tuning beyond identifying this as an evidence gap.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report covers the main mechanisms by which synthetic data can improve scale, coverage, diversity, and rare-case availability, and appropriately distinguishes operational benefits from demonstrated performance. Evidence for broad real-world quality gains remains limited.
- Candidate evidence:
  - Finding 2 identifies benefits including scaling “scarce task-specific examples,” targeting “rare or underrepresented cases,” supporting “privacy-sensitive development,” and accelerating prototyping.
  - Finding 3 describes controllable variation across “formats, classes, audiences, and edge cases.”
  - The report mentions limited-label augmentation, minority-class generation, low-resource-language adaptation, and reduced manual collection or annotation.
- Missing:
  - The report provides limited concrete evidence that these data-quality improvements reliably improve downstream model quality; it mainly presents use cases and one vendor-stated performance example.
  - It does not substantially discuss label availability or label quality as a distinct benefit, beyond limited-label augmentation.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report gives a strong account of collapse, artifacts, distribution mismatch or narrowing, and robustness consequences, with useful conditionality around recursive replacement. Several requested failure modes are only implicit or underdeveloped.
- Candidate evidence:
  - Finding 3 states that synthetic data may “narrow distributions or contain artifacts” and that apparent diversity does not establish factuality or meaningful coverage.
  - Finding 4 covers “compounding approximation errors,” distribution-tail loss, diversity reduction, and degradation under recursive full replacement.
  - Finding 5 reports reduced adversarial robustness despite preserved output quality in one synthetic fine-tuning study.
  - The conclusion identifies “distribution narrowing and error propagation under recursive replacement” as major risks.
- Missing:
  - Factual or semantic errors and incorrect labels are mentioned only indirectly; the report does not clearly trace them to accuracy, generalization, or robustness failures.
  - Contamination is discussed mainly as an evaluation and benchmark problem rather than as a synthetic-data quality failure mode.
  - Repetition and low diversity are addressed through collapse and narrowing, but their distinct effects and conditions are not developed in detail.

### R4

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes targeted minority coverage and appropriately withholds a universal claim of bias reduction, but it offers little substantive treatment of how synthetic data could actively reduce bias or how such interventions should be validated.
- Candidate evidence:
  - Finding 2 says synthetic data can target “minority-class and edge-case generation.”
  - Finding 6 and Finding 7 acknowledge representational gaps and state that the evidence is insufficient to determine whether synthetic, human, or mixed data produces better subgroup outcomes.
  - The report recommends subgroup analysis and comparisons across synthetic, human, and mixed-data regimes.
- Missing:
  - It does not explain concrete bias-reduction mechanisms such as rebalancing, counterfactual generation, fairness-aware generation, filtering, or subgroup weighting.
  - It does not distinguish clearly between a more balanced synthetic dataset and an actual improvement in model behavior, although it implies this distinction through its call for subgroup evaluation.
  - It does not specify the fairness comparisons or outcome measures needed beyond general subgroup analysis and comparative baselines.

### R5

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report covers generator and source-distribution bias, imbalance, underrepresentation, and possible iterative amplification, while appropriately noting the lack of comparative subgroup evidence. Some specific mechanisms and the dataset-versus-model distinction need fuller treatment.
- Candidate evidence:
  - Finding 6 identifies reproduction of “representational, linguistic, cultural, demographic, and occupational biases” from source models and training distributions.
  - It reports Western and English-language over-representation, majority or WEIRD persona preferences, low-resource disadvantages, and demographic and occupational representation gaps.
  - Finding 4 explains that iterative replacement can compound biases and remove rare or low-probability portions of the distribution.
  - Finding 7 explicitly distinguishes documented bias observations from the absence of sufficient comparative evidence about synthetic versus human or mixed data.
- Missing:
  - Stereotypical associations and spurious correlations are not explicitly discussed.
  - The report does not substantially explain how large-scale generation can amplify particular demographic biases apart from the general model-collapse mechanism.
  - The distinction between bias measured in the generated dataset and bias observed in the trained model is present only indirectly and could be made more explicit.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: The proposed evaluation is broad and appropriately emphasizes held-out real-world validation, diversity, contamination, robustness, and downstream utility. However, the rubric’s requested critique of specific metric families is largely absent.
- Candidate evidence:
  - Finding 9 recommends held-out independent tests, contamination and leakage checks, distribution and linguistic-diversity measures, subgroup and low-resource-language analysis, adversarial robustness, safety, and self-preference testing.
  - Finding 3 calls for validation against the target distribution and warns that diversity does not establish factuality or transfer.
  - Finding 8 recommends filtering, accuracy checks, deduplication, held-out evaluation, and regression testing.
  - The report warns that aggregate benchmarks, synthetic test cases, saturation, contamination, and leakage can produce misleading results.
- Missing:
  - The report does not explicitly lay out semantic or label correctness as a separate evaluation dimension, though it refers to accuracy checks and factuality.
  - It does not specifically discuss limitations of statistical metrics, human evaluation, model-based metrics, or perplexity-style metrics.
  - Training utility is implied by performance comparisons but is not clearly framed as a complementary measure alongside data fidelity and generalization.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report has the correct comparative and subgroup-sensitive evaluation orientation and rejects synthetic-only evidence, but it could be more operational about metrics, held-out real data, and the distinction between representation and model behavior.
- Candidate evidence:
  - Finding 9 calls for “comparisons across synthetic, human, and mixed-data training regimes.”
  - The report recommends “subgroup and low-resource-language analysis” and concludes that deployment decisions should require “subgroup and out-of-distribution testing.”
  - It states that balance or synthetic evaluation is insufficient by noting that synthetic data may appear diverse without establishing transfer or real-world coverage, and that comparative subgroup evidence is currently inadequate.
- Missing:
  - The report does not specify concrete subgroup fairness outcomes such as subgroup error rates, performance gaps, calibration, or disparity measures.
  - It does not explicitly state that held-out evaluation should preferably use real data, although it repeatedly recommends independently validated held-out or real-world tests.
  - Representation effects are mentioned, but the recommended evaluation protocol does not clearly separate representation metrics from behavioral fairness metrics.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is a strong conditional conclusion with meaningful uncertainty and practical safeguards. It falls short of full depth because several key conditioning factors and explicit deployment decision thresholds are not integrated into the conclusion.
- Candidate evidence:
  - The conclusion gives a conditional judgment: synthetic data is useful when it supplements real data and undergoes “filtering, deduplication, validation, and rigorous model-level evaluation.”
  - The report contrasts benefits from carefully curated additive data with degradation under recursive replacement and explicitly rejects treating synthetic data as uniformly beneficial or harmful.
  - It identifies practical safeguards including synthetic-to-real comparisons, subgroup and out-of-distribution testing, contamination checks, robustness and safety evaluation, and data-lineage documentation.
  - The report acknowledges uncertainty, limited generalizability, conflicting findings, and gaps in deployment-oriented evidence.
- Missing:
  - The conclusion does not systematically relate outcomes to generator capability, target-model capability, synthetic-to-real ratio, task or domain, prompting, and training regime, although some of these appear in scattered findings or gaps.
  - Decision criteria for selecting an appropriate synthetic-to-real ratio or determining when evidence is sufficient for deployment are not specified.
  - The report does not substantially discuss how curation and filtering quality should be measured when making deployment decisions.

### Novel Value

- The report provides a useful synthesis distinguishing additive synthetic-data use from recursive replacement and linking that distinction to model-collapse risk.
- It identifies a meaningful evidence gap: documented bias in generated data does not establish whether synthetic, human, or mixed training improves subgroup outcomes.
- It connects data-level validation to model-level and deployment-oriented evaluation, including held-out real-world testing, contamination checks, robustness, safety, and subgroup analysis.
- It avoids a universal verdict and frames synthetic data as conditionally useful under curation, mixing with real data, and rigorous evaluation.

## Citations

### Support

#### F1: PARTIALLY_SUPPORTED

- Claim: Synthetic data can improve training efficiency and task-specific performance when carefully curated and used with substantial real data, but the supplied performance evidence is limited in generalizability.
- Sources: S1, S4
- Rationale: The sources support that curated synthetic data can improve task-specific performance and accelerate development, and S1 describes combining synthetic data with retained real data. However, they do not clearly establish improved training efficiency in a broad or measured sense, nor do they directly characterize the cited performance evidence as having limited generalizability. The evidence is narrow—specific models, benchmarks, and use cases—and S1 labels key results as vendor-stated, which supports a cautious narrower conclusion.
- Supporting text: S1 reports that a 1.3B-parameter Phi-1 trained on curated web data plus 1B synthetic tokens achieved 50.6% HumanEval pass@1, while emphasizing that synthetic data should accumulate alongside real data. S4 states that synthetic examples can improve robustness and model performance and enable rapid iteration, but that utility depends on validation and alignment with the target application.

#### F2: SUPPORTED

- Claim: Synthetic data can scale scarce task-specific examples, target rare or underrepresented cases, support privacy-sensitive development, and accelerate prototyping; these are operational benefits rather than guaranteed real-world performance improvements.
- Sources: S1, S2, S4, S7, S10
- Rationale: The saved sources directly support the operational benefits in the claim: scaling data where it is scarce, generating examples for rare or underrepresented cases, enabling privacy-sensitive development, and speeding prototyping. The qualification that these benefits are not guaranteed performance improvements is also supported by the sources’ repeated emphasis on validation, quality, distribution alignment, and risks such as bias and model collapse. S7 is only a summary of a removed post, but the other cited sources provide sufficient support.
- Supporting text: S4 states that synthetic data can expand limited training sets, create examples for underrepresented classes, support privacy-preserving sharing, and enable rapid prototyping. S10 describes creating diverse domain-specific datasets at scale to address scarcity, sensitivity, and cost/time constraints, while S1 emphasizes that utility depends on curation and generation regime and warns that indiscriminate use can degrade models.

#### F3: PARTIALLY_SUPPORTED

- Claim: Synthetic generation can target variation across formats, classes, audiences, and edge cases, but apparent diversity does not establish meaningful coverage, factuality, or transfer to deployment conditions.
- Sources: S1, S4, S9, S10, S12
- Rationale: The sources support the first part: synthetic data can be deliberately varied across formats, underrepresented classes, audiences, and rare or edge-case scenarios. They also support a narrower caution that diversity alone is insufficient: quality, validation, deduplication, alignment with the target distribution, and real-data seeding are emphasized, and S12 reports that diversity affects distribution collapse but does not establish all downstream properties. However, the supplied text does not directly establish the full negative formulation that apparent diversity fails to demonstrate factuality or transfer to deployment conditions. S4 and S10 recommend validation and alignment, but do not provide evidence specifically proving failures of factuality or deployment transfer.
- Supporting text: S4 describes generation across conversational dialogues, QA, classification, summarization, code, and structured extraction; targeted generation for underrepresented classes and edge cases; and says utility depends on validation and alignment with the target application. S9 says prompts can cover common cases, edge cases, and tricky scenarios, while raw LLM output requires filtering, validation, and deduplication. S1 says Cosmopedia varied audience and format, and warns that volume without curation amplifies failure modes. S10 says synthetic data can capture intent variations and rare edge cases, but recommends seeding with real data and evaluating quality. S12 finds that source diversity can mitigate distribution collapse while studying separate downstream effects.

#### F4: SUPPORTED

- Claim: When real data is replaced by recursively generated synthetic data, successive generations can undergo model collapse: errors and biases may compound, while rare, low-probability, and diverse portions of the original distribution become underrepresented or lost. This risk is conditional on the training regime and is not inherent to all synthetic-data use.
- Sources: S1, S2, S5, S6, S12
- Rationale: The saved sources directly support the claim. S1 and S6 describe recursive training with replacement of real data, compounding errors and biases, narrowing output diversity, and depletion of rare or low-probability modes. S1, S6, and S12 also indicate that outcomes depend on the data-aggregation or source-diversity regime, with real-data mixing, accumulation, or diverse synthetic sources mitigating collapse. S2 and S5 provide corroborating summaries that recursive synthetic training can narrow distributions or cause degradation, while synthetic data is not categorically unusable.
- Supporting text: S1: “successive generations ... progressively lose the tails of the original data distribution”; “All three errors compound across training generations”; and risk “depends on the generation regime.” S6: synthetic replacement “amplif[ies] errors and biases,” while rare modes are “systematically omitted”; collapse severity depends on “replacement vs. accumulation.” S12: “higher source diversity” mitigates distribution collapse.

#### F5: SUPPORTED

- Claim: Synthetic fine-tuning has mixed quality and safety effects: greater source diversity can preserve output diversity and mitigate collapse, while one controlled study reports reduced adversarial robustness despite preserved output quality.
- Sources: S12
- Rationale: S12 directly reports that higher synthetic-source diversity mitigates distribution collapse and preserves output-distribution breadth and text diversity. It also states that synthetic fine-tuning decreases adversarial robustness while preserving output quality. The source describes this as the paper’s study findings, supporting the claim’s characterization of mixed quality and safety effects.
- Supporting text: The abstract says diverse synthetic sources can “mitigate distribution collapse,” preserving output-distribution breadth and text diversity. Its listed main findings say synthetic fine-tuning decreases adversarial robustness while preserving output quality.

#### F6: PARTIALLY_SUPPORTED

- Claim: Synthetic data generation can reproduce representational, linguistic, cultural, demographic, and occupational biases from source models and training distributions, particularly for Western, English-language, majority-group, and low-resource contexts.
- Sources: S11, S13, S15
- Rationale: The sources substantially support that LLM-generated outputs can reproduce or express representational, linguistic, cultural, demographic, and occupational biases associated with model behavior and skewed training data. S11 specifically describes Western/English-language overrepresentation, majority/WEIRD preference, low-resource and non-Western degradation, demographic underrepresentation, and occupational imbalances. S13 supports social, cultural, persona-related, multilingual, and low-resource-language biases in LLMs. However, the claim specifically attributes these effects to “synthetic data generation,” while the sources primarily document biases in LLMs and generative-AI applications rather than directly demonstrating that synthetic data generation reproduces every listed bias from source models and training distributions.
- Supporting text: S11 states that LLMs inherit statistical artifacts from training corpora, perform worse for non-Western populations, prefer majority/WEIRD categories, underrepresent non-English and marginalized groups, and show occupational imbalances such as near-absence of Black workers. S13 reports social and cultural biases, varying interpretations across personas and nationalities, and stereotypes in low-resource languages. S15 explains that nonrepresentative training data causes models to learn patterns that do not reflect the broader population and warns that training generative models on generated data can create a quality-degrading feedback loop.

#### F7: SUPPORTED

- Claim: A reliable comparative conclusion about demographic, linguistic, or cultural bias in models trained on synthetic versus human-generated or mixed data cannot currently be drawn from the supplied evidence.
- Sources: S11, S12, S13, S14
- Rationale: The sources document demographic, linguistic, and cultural biases in LLMs generally, and S12 compares human and synthetic fine-tuning on distributional, robustness, and self-preference outcomes. However, the supplied text does not provide a direct, systematic comparison of demographic, linguistic, or cultural bias across models trained on synthetic versus human-generated or mixed data. Therefore, it supports the cautious conclusion that a reliable comparative claim cannot currently be drawn from this evidence.
- Supporting text: S12 reports that the study examines distribution collapse, adversarial robustness, and self-preference bias—not demographic, linguistic, or cultural bias—and states that human data is most effective for reducing self-preference bias, followed by multi-source synthetic data. S11, S13, and S14 discuss existing demographic, language, and cultural biases in LLMs but do not compare those biases by training-data origin.

#### F8: PARTIALLY_SUPPORTED

- Claim: For synthetic fine-tuning, generation alone is insufficient: practical pipelines require filtering, validation, deduplication, and subsequent held-out or regression evaluation.
- Sources: S7, S9
- Rationale: S9 directly supports that raw LLM output is not training-ready and requires filtering, validation, and deduplication. Its pipeline diagram also includes held-out evaluation and a regression suite. However, S7 is only a summary of a removed post and does not provide usable detailed evidence for all elements of the claim. Additionally, S9's explicit four-stage pipeline lists seed creation, generation, filtering, and deduplication, while validation and evaluation appear elsewhere rather than as clearly specified required stages.
- Supporting text: S9 states: “raw LLM output is not training-ready. It requires filtering, validation, and deduplication.” Its pipeline diagram shows “Held out eval plus regression suite.”

#### F9: PARTIALLY_SUPPORTED

- Claim: Evaluation should not rely on aggregate benchmark scores or synthetic test cases alone. It should include independently validated held-out tests, contamination and leakage checks, subgroup and low-resource-language analysis, distribution and linguistic-diversity measures, adversarial-robustness testing, safety and self-preference measures, and comparisons across synthetic, human, and mixed-data training regimes.
- Sources: S4, S5, S9, S10, S12, S13, S14
- Rationale: The sources support several important components of the claim: evaluation should go beyond a few aggregate benchmark scores; benchmarks can suffer from contamination and leakage; held-out evaluation is shown in the S9 pipeline; evaluation should address fairness, safety, and realistic settings; low-resource languages and subgroup bias warrant analysis; and S12 directly examines distribution collapse, linguistic diversity, adversarial robustness, safety-guardrail weakening, self-preference bias, and human versus synthetic training data. However, the sources do not establish the full prescriptive framework, especially the requirement for independently validated held-out tests, explicit mixed-data training comparisons, or the claim that synthetic test cases alone are insufficient. S4 and S10 mainly describe synthetic data generation and evaluation use cases rather than independently validating all listed evaluation dimensions.
- Supporting text: S5: “Determining whether an LLM is truly stronger is not as simple as looking at a few benchmark scores,” and traditional benchmarks face “data contamination, leakage,” fairness, reproducibility, and safety concerns. S9 includes “Held out eval plus regression suite.” S12 studies “distribution collapse, adversarial robustness, and self-preference bias,” including linguistic-diversity measures, safety-guardrail weakening, and comparisons involving human and synthetic fine-tuning data. S10 identifies low-resource/underrepresented languages and side-by-side model comparison as relevant evaluation concerns.

#### F10: PARTIALLY_SUPPORTED

- Claim: Synthetic records should not be treated as reliably privacy-preserving without formal memorization and re-identification testing, lineage, governance, and fidelity metadata.
- Sources: S1, S2, S4, S7, S10
- Rationale: The sources support caution about assuming synthetic data is automatically privacy-preserving and support governance, lineage, fidelity metadata, and validation. However, they do not specifically provide evidence for formal memorization testing or re-identification testing, nor do they establish all listed safeguards as necessary conditions. S4 and S10 make broad privacy-safety claims, while S2 explicitly says lineage and fidelity metadata are non-negotiable and S10 describes validation/evaluation tools.
- Supporting text: S2: “Ungoverned synthetic data creates audit gaps when models fail; lineage and fidelity metadata are non-negotiable.” S10: synthetic data is described as “privacy-safe,” but the source also recommends preview validation and comprehensive quality evaluation. S1 notes that privacy substitution has GDPR pseudonymization risk and distinct failure modes.

### Missing Citations

- Q14: The evidence is insufficient to distinguish synthetic pretraining from synthetic fine-tuning effects on factuality, transfer, distribution shift, robustness, and collapse risk.

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
- `structured_claim_evidence_available`: PASS
- `ledger_claim_ids_unique`: PASS
- `ledger_evidence_relationships_resolve`: PASS
- `ledger_confidence_values_valid`: PASS
- `ledger_evidence_ids_unique`: NOT_EVALUABLE — Current ledger relations have no independent evidence-ID field.

## Main Weaknesses

1. R4: Assess whether and under what conditions synthetic data can reduce harmful bias.
2. R1: Define the synthetic-data settings relevant to the analysis and explain why their differences matter.
3. 6 cited finding(s) were not fully supported by saved evidence.
4. 1 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `36414e911184eea8ef62c41ba8423e71054770da6d3e515f90d477a9870e806e`
- Candidate report hash: `316aa099176af4687560a34719f5bca25b0f215b9bad2b6744728773ad146369`
- LLM calls: 12
- Evaluated at: 2026-08-31T23:24:33.796690+00:00
