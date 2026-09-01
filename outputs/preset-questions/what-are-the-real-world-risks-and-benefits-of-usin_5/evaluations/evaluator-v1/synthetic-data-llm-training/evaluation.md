# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** synthetic-data-llm-training

**System Version:** llm-only-baseline-v0

**Model:** gpt-5.6-luna

## Summary

- Overall: 68.1 / 100
- Evaluation completeness: 100%
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
- Rationale: The report avoids treating all synthetic data as equivalent and identifies several important settings, uses, and mixture concerns. However, the programmatic-generation distinction and a more explicit comparison of pure-synthetic versus mixed regimes are incomplete.
- Candidate evidence:
  - The report distinguishes synthetic instructions, demonstrations, preference data, reasoning traces, conversations, domain data, augmented natural data, and generated test data in the table in section 1.
  - It explicitly contrasts augmentation with replacement and discusses mixtures: “how much independent human data remain in the training mixture.”
  - It separately addresses synthetic uses in instruction tuning, alignment, safety testing, factual pretraining, and fine-tuning-related supervision.
- Missing:
  - The report does not clearly and systematically distinguish LLM-generated data from programmatically generated data, even though the question’s scope includes both.
  - The distinction between pure-synthetic and mixed synthetic–real training is discussed operationally but not analyzed as a structured comparison across pretraining versus fine-tuning.

### R2

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report thoroughly covers scale, coverage, rare cases, low-resource settings, supervision, controllability, and the conditions needed for these to translate into useful data-quality improvements.
- Candidate evidence:
  - Section 2 explains scalable creation of instructions, domain examples, edge cases, multilingual variants, negative examples, and preference comparisons.
  - It identifies targeted coverage of “underrepresented intents, languages, formats, safety scenarios, or rare failure cases.”
  - It discusses low-resource domains and languages, controlled demographic and scenario variation, improved supervision, and systematic safety testing.
  - It provides conditions under which benefits are strongest: authoritative sources, verified documents, APIs, human-authored seeds, and objectively checkable tasks.
- Missing:

### R3

- Coverage: 1.00
- Depth: 1.00
- Rationale: This is a comprehensive treatment of synthetic-data quality failure modes and their downstream consequences, including both immediate data defects and recursive degradation.
- Candidate evidence:
  - Section 3 covers fabricated facts, incorrect advice, invalid code, inconsistent labels, contradictions, unsafe instructions, and plausible but invalid reasoning.
  - It explains error amplification when labels are not independently verified, errors recur, synthetic data dominate, or imitation is rewarded.
  - It addresses correlated errors, effective sample-size inflation, repetitive templates, homogenization, distribution mismatch, contamination, and recursive-training degradation.
  - It connects these failures to accuracy, factuality, robustness, multilingual performance, long-tail retention, diversity, calibration, and deployment performance.
  - It identifies moderating conditions including retention of original data, synthetic proportion, decoding method, filtering, generator diversity, task, and architecture.
- Missing:

### R4

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report covers mechanisms for reducing bias and, importantly, distinguishes intended dataset balancing from demonstrated improvement in model behavior. It also specifies the comparative and subgroup-sensitive evidence needed to support a fairness claim.
- Candidate evidence:
  - The report describes targeted generation for underrepresented groups, rare intents, dialects, safety cases, and counterfactual scenarios.
  - It discusses filtering and selection as potential sources of imbalance and recommends weighting synthetic examples by confidence and validation quality.
  - It explicitly warns that numerical balancing may create stereotyped or inaccurate representations and states that “numerical balance in the synthetic dataset is not evidence of fair representation.”
  - Section 9 recommends baseline comparisons, controlled synthetic-data proportions, subgroup metrics, counterfactual tests, and fresh human-authored evaluation data.
- Missing:

### R5

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report addresses preservation, introduction, and amplification of demographic and representational bias, including generator, filter, preference-label, cultural, and recursive-feedback mechanisms. It also distinguishes data-level appearance from model-level effects.
- Candidate evidence:
  - Section 4 explains generator bias from pretraining data, language and geographic distribution, moderation policy, institutional objectives, and social-group representation.
  - It covers bias introduced by filtering, subgroup underrepresentation, majority-language dominance, stereotypical occupations and social associations, dialect discrimination, and culturally narrow representations.
  - It discusses bias in synthetic preference and alignment labels, including over-refusal, paternalism, excessive hedging, and suppression of viewpoints.
  - It describes feedback loops in which generated content re-enters future datasets and amplifies existing biases.
  - It explicitly warns that a dataset can appear numerically balanced while increasing biased examples and recommends measuring model performance and error types rather than relying on dataset composition.
- Missing:

### R6

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report provides a broad, complementary evaluation framework spanning correctness, fidelity, diversity, coverage, utility, contamination, and held-out real-world generalization, while explaining limitations of automated, model-based, and benchmark-style metrics.
- Candidate evidence:
  - Section 8.3 specifies example-level checks for factuality, label correctness, privacy, consistency, and source verification; dataset-level checks for deduplication, diversity, subgroup balance, coverage, source concentration, and deployment distribution; and model-level checks for capability, calibration, hallucination, robustness, and generalization.
  - Section 5 explains why fluency, standard benchmarks, synthetic tests, and sole reliance on LLM judges are insufficient.
  - It recommends exact or executable checks, expert review, human evaluation, adversarial testing, user studies, contamination checks, and held-out human-authored data.
  - It explicitly warns that synthetic-only or generator-aligned tests can reward style, share errors with the generator, or measure imitation rather than capability.
- Missing:

### R7

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report directly specifies appropriate no-synthetic baselines, held-out preferably real evaluation, subgroup-sensitive metrics, disparity analysis, and representation tests. It clearly rejects balance or prompting alone as proof of fairness.
- Candidate evidence:
  - Section 9 begins with a human/natural-data-only baseline and recommends comparing multiple synthetic proportions.
  - It requires subgroup metrics, tail-performance comparisons, dialect and language variation, intersectional groups, culturally specific scenarios, counterfactual tests, and false-positive, false-negative, refusal, and helpfulness disparities.
  - It states that evaluation should use fresh, human-authored, real or realistically sampled, and expert-verified examples.
  - It explicitly says numerical balance in the synthetic dataset is not evidence of fair representation.
- Missing:

### R8

- Coverage: 1.00
- Depth: 1.00
- Rationale: The conclusion is appropriately conditional and evidence-oriented rather than universal. It relates outcomes to task, domain, generator, mixture, validation, and evaluation factors, acknowledges uncertainty and conflicting effects, and supplies concrete deployment safeguards and decision criteria.
- Candidate evidence:
  - The executive summary concludes that value depends on generation, filtering, mixing with human data, and evaluation, and recommends synthetic data primarily as a targeted supplement.
  - Sections 7 and 10 condition benefits on authoritative grounding, verifiability, task stakes, provenance, synthetic proportion, generator quality, and retention of human data.
  - It identifies higher-risk settings such as medicine, law, finance, social judgments, multilingual communication, open-ended factual knowledge, and preference labeling.
  - It recommends practical safeguards including provenance tracking, human or expert validation, deduplication, source mixtures, independent evaluation, contamination testing, subgroup monitoring, and prevention of recursive contamination.
  - The conclusion states: “Use synthetic data to fill known gaps, not to obscure unknown ones.”
- Missing:

### Novel Value

- The report offers a useful operational framing of synthetic data as a targeted supplement rather than a generic replacement.
- It provides a concrete staged evaluation protocol: baseline, controlled synthetic additions, ablations, independent evaluation, contamination testing, and deployment monitoring.
- It integrates data quality, bias, privacy, provenance, recursive contamination, and model-level evaluation into one practical risk-benefit framework.
- The distinction between nominal dataset balance and demonstrated subgroup-level model improvement is especially valuable.

## Citations

### Support

### Missing Citations

- Q1: Synthetic data can produce large quantities of instructions, explanations, domain examples, and edge cases at substantially lower cost than manual annotation.
- Q2: Synthetic generation can target underrepresented intents, languages, formats, safety scenarios, or rare failure cases.
- Q3: Properly designed synthetic data can reduce exposure to personal or confidential information, especially for prototyping and supervised fine-tuning.
- Q4: Model-generated rationales, critiques, preference comparisons, and tool-use traces can support instruction tuning and alignment.
- Q5: Generated examples can contain factual errors, logical mistakes, invalid code, unnatural language, or mislabeled outputs, and these errors may be amplified during training.
- Q6: A generator reflects aspects of its training data, safety policies, demographic biases, and linguistic biases, which synthetic datasets may transfer or amplify.
- Q7: Repeatedly training on model-generated outputs can cause loss of rare events, linguistic diversity, and calibration, particularly when human data are progressively displaced.
- Q8: Synthetic training data generated from benchmark questions or resembling benchmark distributions can inflate reported performance without corresponding real-world capability.
- Q9: Large synthetic datasets may contain repeated templates, correlated errors, and limited independent information despite appearing broad.
- Q10: Synthetic data is generally safest and most effective as a targeted supplement to high-quality human or naturally occurring data rather than as an unverified replacement.
- Q12: Risk depends not only on the proportion of synthetic examples but also on their use, label verification, and the amount of independent human data retained.
- Q13: Human annotation is expensive, slow, and difficult to scale.
- Q14: Generated examples for SQL, code formatting, structured extraction, or arithmetic can often be automatically checked.
- Q15: Synthetic data can help in settings where naturally occurring data are scarce, including minority languages, specialized fields, rare safety incidents, and new products or APIs.
- Q16: Synthetic data is more reliable when anchored to verified documents, databases, APIs, or human-authored seed examples than when produced through purely free-form generation.
- Q17: Synthetic data may reduce the need to distribute raw personal or confidential records, but it is not automatically private.
- Q18: A model can memorize and reproduce training examples, and synthetic data can preserve sensitive attributes or enable re-identification when combined with external information.
- Q19: Membership-inference, extraction, nearest-neighbor, memorization, attack-simulation, and formal-privacy testing can be used to assess privacy risks.
- Q20: Synthetic generation can deliberately produce examples for underrepresented groups, rare intents, difficulty levels, dialects, safety edge cases, and counterfactual scenarios.
- Q21: Self-Instruct, Constitutional AI, distillation methods, and preference optimization use generated data or model-generated supervision in forms described by the report.
- Q22: Synthetic supervision can improve helpfulness, refusal behavior, formatting, and instruction adherence, while the resulting model may inherit the teacher’s omissions and preferences.
- Q23: Synthetic red-teaming is useful for searching for safety failures but is not a complete substitute for real-world incident data.
- Q24: Language models are optimized to produce likely continuations rather than verified statements, so synthetic examples can be fluent but wrong.
- Q25: Fluency-based automated quality checks are weak at detecting stylistically polished errors.
- Q26: Generated data can cause models to learn generator mistakes as authoritative, especially when labels are not independently verified or synthetic data dominate the mixture.
- Q27: Many generated examples may share model priors, templates, misconceptions, refusal policies, writing styles, and blind spots, reducing their independent information content.
- Q28: Heavy training on repetitive synthetic structures can reduce adaptability to natural variation, informal language, dialects, code-switching, and domain-specific conventions.
- Q29: Simulated users tend to be more articulate, cooperative, explicit, and free of typos or slang than real users.
- Q30: Recursive training on model-generated data can eliminate low-probability modes and degrade diversity, with severity affected by data retention, synthetic proportion, decoding, filtering, generator diversity, task, and architecture.
- Q31: Synthetic data can accidentally include benchmark questions, public evaluation answers, proprietary documents, personal information, confidential prompts, or text from prior model releases.
- Q32: Synthetic data can make training appear more effective than it is and create legal, privacy, or intellectual-property problems through contamination or leakage.
- Q33: Synthetic data inherits generator biases, and filtering can further favor dominant dialects, culturally familiar examples, majority-group contexts, or one institution’s standards of politeness.
- Q34: Synthetic augmentation can increase the number of biased examples while making a dataset appear numerically balanced.
- Q35: Synthetic translations or multilingual generations may be grammatically acceptable but culturally unnatural and may erase regional, dialectal, indigenous, legal, or medical distinctions.
- Q36: Model-generated preference labels can produce over-refusal, paternalism, excessive hedging, or suppression of legitimate viewpoints when model judgments diverge from community or user preferences.
- Q37: AI-generated content can enter future datasets through search results, social media, customer-service logs, or educational materials, creating feedback loops that increase the prevalence of original model biases.
- Q38: Synthetic data can inflate benchmark scores through contamination, benchmark-like generation, optimization toward known formats, or evaluation on data resembling training data.
- Q39: Using another language model as the sole evaluator can produce shared errors and preferences, reward verbosity and polish, miss subtle errors, and encourage judge hacking.
- Q40: Generated tests may be too easy because they contain explicit instructions, clean formatting, obvious answers, limited ambiguity, and familiar phrasing.
- Q41: Fine-tuning on synthetic demonstrations can improve imitation of answer style without improving underlying capability, factuality, reasoning, or calibration.
- Q42: Aggregate accuracy can improve while performance worsens for minority dialects, low-frequency intents, long-tail entities, non-English languages, disabled users, informal inputs, adversarial inputs, or high-stakes domains.
- Q43: Self-Instruct demonstrated that a model can generate instruction-following data that improves another model’s instruction following.
- Q44: Constitutional AI used model-generated critiques and revisions guided by stated principles and reduced the need for some human preference labels.
- Q45: Alpaca, Vicuna, Orca, and related distillation approaches showed that relatively small amounts of model-generated instruction data can produce substantial behavioral improvements.
- Q46: Research on recursive training has found that preserving original data and controlling synthetic-data mixtures can mitigate, though not necessarily eliminate, model collapse.
- Q47: Dataset quality and provenance can matter as much as raw quantity, and redundant or noisy data can produce diminishing returns or harm.
- Q48: Synthetic examples can improve subgroup coverage only when target groups and scenarios are carefully defined and outputs are checked by relevant cultural or domain experts.
- Q50: Synthetic data cannot reliably indicate how people actually behave unless it is calibrated against real observations.
- Q51: Numerical balance in a synthetic dataset is not evidence of fair representation.
- Q54: Synthetic data’s benefits are most reliable when generation is constrained by authoritative sources and outputs can be independently verified.
- Q55: Generated examples are not independent observations, and their fluency can conceal factual errors, stereotypes, and narrow assumptions.

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

1. 51 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `36414e911184eea8ef62c41ba8423e71054770da6d3e515f90d477a9870e806e`
- Candidate report hash: `0dfa276706b552afbac3452ef7cf602786841b65db6e5ed52a2af4c1547c432a`
- LLM calls: 2
- Evaluated at: 2026-08-31T23:48:40.497780+00:00
