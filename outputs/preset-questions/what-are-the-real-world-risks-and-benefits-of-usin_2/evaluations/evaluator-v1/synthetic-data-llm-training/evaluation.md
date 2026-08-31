# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** synthetic-data-llm-training

**System Version:** evidence-ledger-v1

**Model:** gpt-5.6-luna

## Summary

- Overall: 78.4 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.71
- Coverage: 0.72
- Depth: 0.69
- Citation quality: 0.86
- Citation validity: 1.00
- Citation support: 0.83
- Citation completeness: 0.85
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes that synthetic-data regimes differ, especially replacement versus augmentation, but the required taxonomy of generator type, training stage, and pure versus mixed data is incomplete.
- Candidate evidence:
  - The report distinguishes additive use from replacing real data: “An additive, real-data-anchored approach is less risky than indiscriminate replacement of real data.”
  - It discusses both training/fine-tuning benefits and synthetic evaluation sets, including “task-specific fine-tuning” and “synthetic data can help construct evaluation sets.”
- Missing:
  - It does not clearly distinguish LLM-generated data from programmatically generated data.
  - It does not explicitly compare pretraining with fine-tuning as separate settings.
  - It does not systematically distinguish pure-synthetic from mixed synthetic–real training beyond the accumulate-versus-replace discussion or explain all implications of those differences.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report substantially covers scalability-enabled coverage, rare cases, task specificity, and some empirical utility, but has less detail on labels, broad diversity, and quantitative evidence.
- Candidate evidence:
  - Finding 1 states that synthetic data can expand “scarce or expensive datasets,” support “domain adaptation,” target “underrepresented classes,” and produce “task-specific examples.”
  - The evidence lists rare-event and subgroup coverage, dialogues, code, reasoning traces, question-answer pairs, tool use, RAG, and classification data.
  - The report cites controlled improvements on classification, mathematics, question-answering, and Text2SQL tasks, including gains from hybrid real-plus-synthetic training.
  - It notes that synthetic evaluation cases can cover “edge cases, adversarial scenarios, decision boundaries, and conversational failure modes.”
- Missing:
  - The report gives limited direct discussion of label availability and how synthetic labeling changes quality relative to human labels.
  - It provides limited evidence about broad pretraining-scale diversity or coverage improvements, rather than mostly task-specific fine-tuning examples.
  - The benefits are described largely through cited source summaries rather than detailed comparison conditions or effect sizes.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report provides strong coverage of recursive degradation, mode collapse, repetition, distribution narrowing, and task-utility tradeoffs, but some requested failure modes and causal conditions are underdeveloped.
- Candidate evidence:
  - Finding 2 describes recursive training risks including “narrowing of the learned distribution,” loss of “low-probability valid examples,” degraded outputs, and increased perplexity after repeated training without retained real data.
  - Finding 4 identifies repetition, drift, teacher-bias inheritance, mode collapse, and audit gaps, and recommends curation, deduplication, filtering, provenance, and real-data mixing.
  - Finding 5 reports that similarity-based curation improved diversity metrics but often reduced downstream classification performance.
  - The report warns about distribution mismatch and evaluation distributions that may not represent real-world performance, and connects failures to accuracy, generalization, robustness, and utility.
- Missing:
  - Factual hallucinations, semantic errors, and incorrect labels are mentioned only indirectly through “faithfulness checks” and “quality filtering,” not analyzed in concrete detail.
  - Contamination and memorization are discussed mainly under privacy or evaluation rather than as explicit training-data quality failure modes.
  - Conditions affecting failure likelihood—such as generator capability, domain distance, synthetic-to-real ratio, and filtering thresholds—are not systematically developed.

### R4

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report correctly presents targeted generation as conditional mitigation and calls for held-out fairness evaluation, but the intervention mechanisms and evidentiary standard are not fully specified.
- Candidate evidence:
  - Finding 6 says synthetic data can “target underrepresented groups and potentially reduce fairness gaps.”
  - It states that fairness improvement is conditional on “distributional-fit, utility, privacy, held-out evaluation, fairness auditing, and retraining.”
  - The report emphasizes that synthetic data “does not automatically remove bias” and that mitigation requires an audit-and-retrain loop.
  - The conclusion recommends fairness audits and checking performance against independent real-world behavior.
- Missing:
  - Counterfactual generation, fairness-aware generation, explicit rebalancing, filtering, and weighting are not separately explained as mechanisms.
  - The report does not clearly specify the comparisons needed to demonstrate bias reduction, such as real-only versus mixed-data baselines with matched data budgets.
  - It does not give concrete subgroup outcome measures for verifying that a more balanced synthetic dataset improves model behavior.

### R5

- Coverage: 0.75
- Depth: 0.75
- Rationale: Generator and inherited bias, underrepresentation, disparities, and intersectional weaknesses are covered, but the report does not fully unpack bias amplification mechanisms or the dataset/model measurement distinction.
- Candidate evidence:
  - Finding 6 states that generated data may inherit “source or generator-model biases.”
  - The report identifies selection, social, temporal, implicit, automation, and inherited model biases, and reports persistent disparities and weaknesses on intersectional cases.
  - It notes that synthetic data can target underrepresented groups but does not automatically remove bias, distinguishing potential mitigation from persistent risk.
  - Finding 4 identifies teacher-bias inheritance and mode collapse as risks, while the conclusion warns of inherited bias.
- Missing:
  - The report gives limited explicit treatment of stereotypical associations, spurious correlations, and class imbalance as distinct mechanisms.
  - Amplification through iterative or large-scale synthetic training is not directly connected to demographic bias; recursive amplification is discussed primarily as quality collapse.
  - The distinction between bias measured in the synthetic dataset and bias measured in the trained model is present only implicitly, not clearly articulated.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report presents a genuinely complementary evaluation perspective and warns against single metrics, but it lacks a fully specified metric framework and explicit discussion of several metric classes.
- Candidate evidence:
  - Finding 4 recommends curation, diversity checks, deduplication, quality filtering, lineage, fidelity metadata, faithfulness checks, instruction-adherence checks, and downstream utility testing.
  - Finding 5 shows that diversity metrics can conflict with downstream classification performance, demonstrating that surface metrics are insufficient.
  - Finding 8 recommends human oversight and “semantic, judgment-based evaluation” rather than relying solely on surface-form metrics.
  - The report recommends held-out testing, real-data anchoring, downstream utility testing, and checking performance against independent real-world behavior.
  - It warns that synthetic evaluation collections can differ systematically from human queries and judgments and distort absolute performance estimates.
- Missing:
  - Statistical, model-based, and perplexity-style metrics are not each explicitly characterized with their individual limitations.
  - Factuality, semantic correctness, label correctness, fidelity, diversity, and coverage are listed or implied but not organized into a concrete multi-metric evaluation protocol.
  - The report does not give detailed procedures for testing generalization on held-out real data, contamination, or generator-aligned evaluation bias.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report supports held-out fairness evaluation and recognizes subgroup and intersectional disparities, but the baseline design and concrete fairness measures remain underspecified.
- Candidate evidence:
  - Finding 6 calls for “held-out evaluation” and “fairness auditing” and says mitigation depends on retraining and validation.
  - The report identifies persistent demographic disparities and weaknesses on intersectional cases.
  - The conclusion recommends auditing fairness and checking performance against “independent real-world behavior.”
  - The report’s findings distinguish targeted synthetic data as a potential intervention from demonstrated fairness improvement.
- Missing:
  - A real-data-only or no-synthetic baseline is not explicitly required or described as the comparison condition.
  - The report does not concretely specify subgroup performance, error-rate, representation, or disparity metrics.
  - It does not clearly state that subgroup-sensitive evaluation should preferably use held-out real data rather than synthetic-only test sets, although held-out and independent evaluation are recommended.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The conclusion is appropriately conditional, evidence-aware, and practical, with strong safeguards and uncertainty acknowledgement, but several rubric-specified conditioning factors and operational decision criteria are only implicit.
- Candidate evidence:
  - The conclusion calls synthetic data “a conditional augmentation and evaluation tool, not a drop-in replacement” and rejects universal claims about quality, fairness, privacy, or deployment predictiveness.
  - Finding 9 states that effectiveness varies with task, seed-data size, prompting or generation method, and available budget.
  - Finding 3 recommends retaining real data while acknowledging that no universal safe mixing ratio is established.
  - The report recommends real-data anchoring, validation of fidelity and utility, fairness and privacy audits, held-out and human-supervised evaluation, and checks against independent real-world behavior.
  - The Conflicts and Uncertainty section explicitly acknowledges conditional mitigation, contradictory curation results, and unresolved evidence gaps.
- Missing:
  - Generator capability and target-model capability are not explicitly analyzed as decision factors.
  - The synthetic-to-real ratio and training regime are discussed only generally; no practical criteria are given for selecting proportions or regimes.
  - Deployment decision thresholds or clearer go/no-go criteria are not specified beyond broad safeguards.

### Novel Value

- The report offers a useful synthesis that treats synthetic data as conditional augmentation rather than replacement and connects this to recursive model-collapse risk.
- It highlights an important evaluation tension: higher diversity or similarity-based curation can improve dataset metrics while harming downstream task performance.
- It integrates data quality, bias, privacy, and evaluation into a coherent workflow centered on real-data anchoring, held-out testing, human oversight, and independent real-world validation.
- It explicitly distinguishes potential fairness mitigation from demonstrated model-level fairness improvement and acknowledges unresolved evidence gaps.

## Citations

### Support

#### F1: SUPPORTED

- Claim: Synthetic data can provide practical training and fine-tuning benefits by expanding scarce or expensive datasets, supporting domain adaptation, targeting underrepresented classes, and producing task-specific examples.
- Sources: S4, S5, S6, S9, S11, S12, S13
- Rationale: The saved sources collectively support all important elements of the claim. S4 describes synthetic data as addressing scarce, expensive, or time-consuming data collection; augmenting limited training sets; generating underrepresented-class examples; supporting domain adaptation; and tailoring examples to specific tasks or domains. S5 states that synthetic data can expand training resources and improve performance on specific tasks. S6 supports targeting underrepresented groups, rare events, and edge cases, and retraining or fine-tuning with real-plus-synthetic data. S11 explains that synthetic data is structured for particular fine-tuning recipes and that real labeled data is often unaffordable at the needed scale. S12 supports mitigating dataset scarcity and tailoring generation to tasks or domains. S13 describes the enterprise fine-tuning data bottleneck, dataset quantity increases, task-specific synthetic strategies, and cost-effectiveness under resource constraints.
- Supporting text: S4: Synthetic data can supplement or replace human-labeled data when real-world collection is expensive, time-consuming, or complex; it can augment limited datasets, address class imbalance, and support domain adaptation. S11: “Real labeled data is the ground truth but it is rarely affordable at the scale modern fine-tuning needs,” while synthetic data is shaped for the specific fine-tuning recipe. S12: LLM generation can mitigate dataset scarcity and improve coverage of underrepresented domains and requirement types. S13: Enterprises often lack high-quality task-specific datasets; synthetic generation can increase dataset quantity and improve cost-effectiveness under resource constraints.

#### F2: SUPPORTED

- Claim: Recursive use of model-generated data, or replacing real data with synthetic data, can cause model collapse and degrade learned quality.
- Sources: S1, S2, S5, S9
- Rationale: The cited sources consistently support the claim. S1 explicitly describes model collapse from iterative training on prior model outputs, reports degradation under purely synthetic self-training, and states that replacing real data causes unbounded error. S2 directly says recursive synthetic-data training causes model collapse and degraded outputs. S5 states that repeated training on model-generated content without sufficient new information can cause capabilities to stagnate or degrade. S9 describes a negative recursive loop that can significantly reduce output quality.
- Supporting text: S1: “experiments with OPT-125m showed perplexity degrading by 20–28 points” under purely synthetic self-training, and says error grows when synthetic data “replaces real data.” S2: “Recursive training on synthetic data causes model collapse, where distributions narrow until outputs degrade.” S5: repeated training on other models’ content can cause capabilities to “stagnate or degrade.” S9: training generative models on generated data can create a “negative loop” that “significantly reduce[s] output quality.”

#### F3: SUPPORTED

- Claim: An additive, real-data-anchored approach is less risky than indiscriminate replacement of real data, although the evidence does not establish a universal safe mixing ratio.
- Sources: S1
- Rationale: S1 explicitly describes the additive “accumulate, don’t replace” approach as mitigating model collapse and presents additive training alongside real data as lower risk than fully replacing real data. It also mentions 10% real-data retention as an example, not a universal rule; the source does not claim that any single mixing ratio is universally safe.
- Supporting text: S1 states that the fix is “accumulating real data alongside [synthetic data] rather than replacing it,” and its risk table rates “Fully replace real data” as high risk versus “Accumulate synthetic alongside real (additive)” as low risk. It separately reports that retaining 10% real data limits perplexity drift, without establishing a universal safe ratio.

#### F4: PARTIALLY_SUPPORTED

- Claim: Synthetic-data quality depends on generation discipline and validation, including curation, diversity checks, deduplication, quality filtering, lineage, fidelity metadata, real-data anchoring, and downstream utility testing.
- Sources: S1, S2, S4, S6, S11, S12, S13
- Rationale: The sources strongly support that synthetic-data quality depends on disciplined generation, curation, diversity, quality filtering, validation, real-data anchoring, and downstream/task utility testing. However, the saved excerpts do not meaningfully support every listed element: deduplication appears in S1 as a dataset characteristic, while lineage and fidelity metadata appear in S2 as governance requirements, but the excerpts do not establish all of these as components on which quality itself depends. The claim is therefore broader than the supplied evidence.
- Supporting text: S1 says Phi-1 worked because its data was “curated with discipline,” and describes a “deduped + quality-filtered synthetic + real” regime. S11 specifies a pipeline of seed prompts, teacher generation, quality filtering, and a diversity check, noting that a small real seed anchors the distribution. S4 states that quality and utility depend on generation techniques, validation methods, and alignment with application requirements. S6 lists validation of distributional fit, task utility, and privacy. S12 reports that prompting and post-generation curation affect quality, while multi-sample prompting improves utility and diversity.

#### F5: SUPPORTED

- Claim: Greater diversity or similarity-based filtering is not universally beneficial: a curation method can improve diversity metrics while reducing downstream classification performance.
- Sources: S12
- Rationale: The saved source explicitly states that similarity-based curation consistently improves diversity metrics but often hurts classification performance, directly supporting the claim that increased diversity or this filtering approach is not universally beneficial.
- Supporting text: The abstract reports: “similarity-based curation consistently improves diversity metrics but often hurts classification performance,” and concludes that “not all redundancy is detrimental to Machine Learning effectiveness.”

#### F6: PARTIALLY_SUPPORTED

- Claim: Synthetic data can target underrepresented groups and potentially reduce fairness gaps, but it does not automatically remove bias; generated data may inherit source or generator-model biases, and bias-auditing tools are themselves imperfect.
- Sources: S6, S5, S7, S9
- Rationale: S6 directly supports targeting underrepresented subgroups, rebalancing training data, and using fairness audits and re-audits to reduce gaps. S7 supports the limitation of auditing tools, reporting persistent disparities and weaknesses in intersectional cases. S5 and S9 support that synthetic data introduces risks and that biased or unrepresentative data can affect models, but the saved text does not clearly establish the specific claim that generated data inherits source or generator-model biases, nor does it explicitly say synthetic data does not automatically remove bias.
- Supporting text: S6 describes generating “targeted synthetic records for under-represented slices” and says the workflow is closed only after fairness gaps fall below a threshold and the model is re-audited. S7 reports “persistent gaps across demographic axes and multi-demographic targeted biases” and “persistent disparities across demographic groups.”

#### F7: PARTIALLY_SUPPORTED

- Claim: Synthetic data does not automatically provide privacy protection; privacy risk depends on possible re-identification, memorization, provenance, and governance controls.
- Sources: S1, S4, S6
- Rationale: The sources support the narrower claim that synthetic data is not automatically privacy-protective: S1 notes that privacy obligations apply where re-identification is plausible, S4 describes synthetic data as removing direct links rather than guaranteeing privacy, and S6 requires privacy validation, PII screening, and documented controls. However, the supplied text does not meaningfully address memorization or provenance, and it does not expressly develop governance controls beyond validation and audit documentation.
- Supporting text: S1: GDPR applies to datasets where “re-identification is plausible.” S4: synthetic data may preserve patterns “without exposing actual patient information,” but its quality and utility depend on validation. S6: the workflow includes checking the “privacy of synthetic set” with a PII screen, and notes that some differentially private workflows are validated and documented under audit.

#### F8: SUPPORTED

- Claim: Synthetic data can help construct evaluation sets that cover edge cases, adversarial scenarios, decision boundaries, and conversational failure modes, but synthetic or conventional benchmark scores may not reliably represent broad real-world capability or safety.
- Sources: S4, S6, S5, S8, S14
- Rationale: S4 directly states that LLMs can generate evaluation datasets covering edge cases, adversarial examples, diverse scenarios, ambiguous queries, multi-turn context, graceful failure modes, and examples near decision boundaries. S5 supports the limitation that conventional benchmark scores may not reflect complex real-world capability, reliability, or safety. S8 further documents bias in synthetic test collections and distortions in measured system performance, supporting the caution about synthetic evaluation scores. S6 and S14 provide additional, though less direct, support for targeted edge-case generation and the need for validation and human oversight.
- Supporting text: S4: LLMs can generate test cases covering “edge cases, adversarial examples, and diverse scenarios,” including ambiguous queries, multi-turn context, graceful failure modes, and examples near decision boundaries. S5: “A model may perform well on standard benchmarks while still behaving unreliably in complex real-world tasks.” S8: Synthetic test collections show evaluation bias and can produce “systematic overestimation of system performance.”

#### F9: SUPPORTED

- Claim: No single synthetic-data generation strategy is uniformly optimal: effectiveness varies with task, seed-data size, prompting or generation method, and available budget.
- Sources: S13, S12
- Rationale: S13 directly shows that the optimal strategy changes with task, initial seed-prompt size, and query budget: response augmentation is strongest under limited budgets, while generating new prompts becomes strongest as the budget increases. S12 further supports method- and task-dependence: multi-sample prompting improves performance, while automated prompt optimization substantially helps one task but degrades others. Together, the sources support the claim that no single strategy is uniformly optimal and that effectiveness depends on the listed factors, including resource budget.
- Supporting text: S13: “With a limited budget, creating new responses is most effective. However, as we increase our budget, creating new prompts yields the most effective results”; it also reports results across three task types and different numbers of starting prompts. S12: multi-sample prompting improved F1 by 6–44 points, while PACE improved functional classification but degraded other tasks.

### Missing Citations

- Q24: Direct controlled real-world evidence is lacking on when synthetic data improves versus harms downstream LLM quality compared with equivalent human-authored or human-labeled data across fine-tuning tasks and domains.
- Q25: The evidence does not quantify demographic, cultural, or task-specific bias effects, or establish whether minority-class targeting improves fairness without stereotyping or label artifacts.
- Q26: Reliable privacy guarantees and measurable re-identification or memorization risks for LLM-generated training data remain unestablished.
- Q27: The evidence does not establish how to validate synthetic evaluation sets against independent real-world outcomes, contamination, benchmark gaming, and distribution shift, or which metrics best detect these failures.

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

1. R1: Define the synthetic-data settings relevant to the analysis and explain why their differences matter.
2. R4: Assess whether and under what conditions synthetic data can reduce harmful bias.
3. 3 cited finding(s) were not fully supported by saved evidence.
4. 4 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `36414e911184eea8ef62c41ba8423e71054770da6d3e515f90d477a9870e806e`
- Candidate report hash: `e0b023d259b882a5dd9ff5424a391d77034a786c8739b819331e47b6f46fabb1`
- LLM calls: 11
- Evaluated at: 2026-08-31T21:55:33.255101+00:00
