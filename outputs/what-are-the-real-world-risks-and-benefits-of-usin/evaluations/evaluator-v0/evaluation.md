# Research Evaluation

**Evaluator:** evaluator-v0

**Model:** gpt-5.6-luna

**Timestamp:** 2026-08-30T21:01:06.423315+00:00

## Summary

- Coverage: 90%
- Core coverage: 90%
- Citation support: 70%
- Citation completeness: 100%
- Deterministic checks: 156 passed, 0 failed

## Coverage

### A1: Assess the real-world risks of using synthetic data to train or fine-tune large language models.

- Importance: Core
- Status: Covered
- Reason: The report substantively assesses major real-world risks, including factual degradation, recursive model collapse, loss of rare cases, privacy leakage or overconfidence, bias amplification, and misleading evaluation.
- Report evidence: Findings 4–7 and 9, plus the Conclusion, describe these risks and their practical consequences for training and fine-tuning LLMs.

### A2: Assess the real-world benefits of using synthetic data to train or fine-tune large language models.

- Importance: Core
- Status: Covered
- Reason: The report substantively identifies and qualifies practical benefits, including reducing data scarcity and annotation costs, targeting rare or domain-specific cases, privacy-sensitive prototyping, and potentially improving smaller-model performance.
- Report evidence: Findings 1, 2, and 9 and the Conclusion discuss these benefits while noting that they depend on task fit, curation, and validation.

### A3: Evaluate how synthetic-data quality affects the risks and benefits of training or fine-tuning large language models.

- Importance: Core
- Status: Covered
- Reason: The report directly evaluates how quality dimensions such as factual correctness, seed coverage, label accuracy, diversity, novelty, distributional fidelity, filtering, and deduplication condition outcomes and risks.
- Report evidence: Finding 3 presents the quality requirements, while Finding 4 links poor or recursively generated data to reduced diversity, factual reliability, and distribution coverage; Finding 10 recommends quality controls.

### A4: Evaluate bias-related risks and benefits associated with using synthetic data for large language models.

- Importance: Core
- Status: Partially Covered
- Reason: Bias-related risks are meaningfully addressed, including inheritance or amplification from generators, prompts, and seed data, and the failure of simple oversampling to establish fairness. Potential bias-reduction benefits are only mentioned as unverified claims, without substantive evidence or comparative analysis.
- Report evidence: Finding 5 and the Conflicts and Uncertainty section discuss bias risks and the lack of controlled measurements; Finding 8 addresses subgroup and uncertainty-aware fairness evaluation, while the report says bias-reduction claims remain unproven.

### A5: Address how the use of synthetic data should be evaluated, including the evaluation of resulting model performance or behavior.

- Importance: Core
- Status: Covered
- Reason: The report provides a detailed evaluation framework covering independent human-authored or deployment-derived holdouts, synthetic evaluation bias, factuality, diversity, subgroup performance, uncertainty, robustness, contamination, and real-world generalization.
- Report evidence: Findings 6–8 and 10 explain evaluation distortions and recommended safeguards, including independent validation and separate assessment of subgroup and behavioral outcomes.

## Citation Support

### F1

**Claim:** Synthetic data can reduce data scarcity and annotation effort while enabling targeted coverage of domain-specific, rare, imbalanced, or edge-case examples.

- Sources: S3, S4, S13, S14
- Combined result: Fully Supported
- Reason: Together, the sources directly support reducing data scarcity and annotation burden and generating targeted examples for domain-specific, rare, imbalanced, and edge-case coverage.

  - S3: Fully Supported — The source directly describes real-data scarcity and expensive human annotation, and identifies edge-case augmentation and domain-specific data as synthetic-data use cases.
  - S4: Fully Supported — The source explicitly states that synthetic data addresses data scarcity, supplements human-labeled data, and supports rare edge cases, class-imbalance correction, and domain adaptation.
  - S13: Fully Supported — The source states that expert annotation is expensive and that 50–200 real seed examples can generate thousands of domain-specific examples, while emphasizing coverage of edge cases.
  - S14: Fully Supported — The source directly contrasts scarce samples and costly manual annotation with generating thousands of examples, including varied prompts and edge-case coverage.

### F2

**Claim:** Carefully curated synthetic data can improve task-specific performance or allow a smaller model to approach the performance of a much larger model, but the causal contribution of synthetic data is not always demonstrated.

- Sources: S3, S10
- Combined result: Partially Supported
- Reason: Together, the sources support the general possibility that carefully curated or task-specific training data can enable strong performance from smaller models and that synthetic-data regimes can have differing outcomes. They do not fully support the claim that synthetic data itself caused the reported gains, and S10 lacks the cited synthetic-augmentation results.

  - S3: Partially Supported — S3 directly supports that curated synthetic data contributed to Phi-1's strong coding performance and contrasts it with degradation from purely synthetic self-training. However, it does not directly establish that the causal contribution of synthetic data was not demonstrated; it presents the mixed-data result as evidence of contribution.
  - S10: Partially Supported — S10 supports that an 8B fine-tuned model approached the performance of a 70B baseline on a narrow task, and it describes planned comparisons using synthetic data. The retrieved passage does not include synthetic-augmentation results, so it does not show that synthetic data caused the performance or that it improved it.

### F3

**Claim:** Synthetic-data quality depends heavily on seed coverage, factual correctness, label accuracy, diversity, novelty, distributional fidelity, filtering, and deduplication.

- Sources: S13, S14, S5
- Combined result: Partially Supported
- Reason: Together, the sources cover most listed quality considerations, especially coverage, correctness, diversity, novelty, filtering, deduplication, and distributional concerns. However, label accuracy and the claim that quality depends heavily on the entire enumerated set are not directly established.

  - S13: Partially Supported — Directly supports seed coverage and diversity constraints, factual correctness risks, filtering, deduplication, and preserving distributional fidelity, but does not directly establish label accuracy, novelty, or all listed factors as a unified dependency.
  - S14: Partially Supported — Supports diverse seed coverage, response accuracy checks, filtering, and deduplication; it does not directly support distributional fidelity, novelty, or label accuracy as stated.
  - S5: Partially Supported — Supports cleaning, deduplication, filtering, data-mixture design, novelty, reliability, and verifiability as important data requirements, but does not address seed coverage or label accuracy specifically.

### F4

**Claim:** Recursive training on model-generated data can narrow the learned distribution, remove rare or low-probability cases, and degrade quality, diversity, and factual reliability.

- Sources: S3, S1, S5, S13
- Combined result: Fully Supported
- Reason: Taken together, the sources directly support the claim that recursive training on model-generated data can narrow the learned distribution, eliminate rare cases, and degrade performance, diversity, and factual reliability; S13 explicitly covers the full set of effects, while S3 and the other sources provide additional support.

  - S3: Partially Supported — Directly supports recursive synthetic training narrowing distribution tails, loss of rare valid outputs, and degradation measured by increased perplexity, but does not directly establish factual reliability degradation.
  - S1: Partially Supported — States that recursive synthetic-data training causes model collapse, with distributions narrowing and outputs degrading, but provides little detail on diversity loss or factual reliability.
  - S5: Partially Supported — States that repeated training on model-generated content can cause capabilities to stagnate or degrade, but does not directly support distribution narrowing, rare-case loss, or factual unreliability.
  - S13: Fully Supported — Directly states that recursive training narrows output distributions, removes rare and tail cases, degrades factual accuracy while preserving fluency, and produces brittle-looking outputs.

### F5

**Claim:** Synthetic data may reproduce or amplify biases in the generator, seed data, prompts, or evaluation process; generating more examples for underrepresented groups does not by itself establish fairness.

- Sources: S4, S13, S5, S12
- Combined result: Partially Supported
- Reason: The evidence supports a narrower claim that synthetic-data distributions can inherit source or seed limitations, lose rare cases, and require validation and fairness evaluation. It does not directly support all specified bias sources, especially generators and prompts, or directly establish that generating more underrepresented-group examples alone fails to establish fairness.

  - S4: Partially Supported — It describes generating examples for underrepresented classes and stresses that synthetic-data quality depends on validation and alignment, but it does not directly state that generation reproduces or amplifies biases in the generator, prompts, or evaluation process.
  - S13: Partially Supported — It directly states that seed-data quality and diversity constrain generated data and that missing edge-case diversity cannot be recovered later; it also describes loss of rare cases through recursive generation. It does not specifically address bias or fairness.
  - S5: Partially Supported — It identifies biased information as a data risk, warns that synthetic data can introduce risks, and says evaluation should address fairness. It does not directly establish the claim about generator, seed, prompt, or evaluation bias, nor the insufficiency of adding examples alone.
  - S12: Unsupported — It promotes synthetic data as reducing bias and increasing diversity, but supplies no comparative subgroup measurements or other evidence supporting the claim's caution about bias reproduction or fairness.

### F6

**Claim:** Synthetic evaluation sets and LLM-generated judgments can systematically distort measured performance.

- Sources: S6
- Combined result: Fully Supported
- Reason: S6 directly supports the claim that synthetic evaluation sets and LLM-generated judgments can systematically distort measured performance, including through query-generation differences and judgment leniency.

  - S6: Fully Supported — The source directly reports systematic differences between synthetic and human queries, positive/lenient GPT-4 relevance judgments, and resulting systematic overestimation of performance. It also states that effects can differ for absolute versus relative performance comparisons.

### F7

**Claim:** Synthetic evaluation can expand coverage of edge cases, adversarial scenarios, ambiguity, multi-turn behavior, calibration, and robustness, but it should not replace independent human-authored or deployment-derived evaluation.

- Sources: S4, S10, S13, S3, S5, S6
- Combined result: Partially Supported
- Reason: The sources collectively support synthetic evaluation for several listed edge cases and support retaining real or independently authored evaluation because synthetic methods can introduce blind spots, bias, contamination, and overfitting. However, the evidence does not directly establish the full claim’s reference to deployment-derived evaluation, so the combined claim is only partially supported.

  - S4: Partially Supported — Directly supports synthetic generation for edge cases, adversarial behavior, ambiguity, multi-turn context, calibration, and robustness, but does not establish that it should not replace independent evaluation.
  - S10: Partially Supported — Supports retaining a separate real holdout to avoid overfitting, but discusses fine-tuning evaluation rather than the full claim about synthetic evaluation coverage and deployment-derived evaluation.
  - S13: Fully Supported — Directly states that synthetic validation creates blind spots and recommends validation on real examples; it also states synthetic data should not replace the real foundation.
  - S3: Partially Supported — Supports accumulating real data alongside synthetic data rather than replacing it and identifies evaluation overfitting and distribution-related risks, but does not directly cover all listed evaluation dimensions or deployment-derived evaluation.
  - S5: Partially Supported — Supports synthetic data expanding resources and identifies contamination, leakage, benchmark saturation, and poor correspondence to real-world behavior, but does not directly frame the specific replacement recommendation.
  - S6: Partially Supported — Supports synthetic evaluation as scalable and identifies systematic bias relative to human evaluation, implying the need for human-grounded validation, but does not support the full set of claimed coverage areas or deployment-derived evaluation.

### F8

**Claim:** Fairness evaluation should examine subgroup-specific performance and uncertainty, not only aggregate accuracy or conventional discrete fairness metrics.

- Sources: S9, S7
- Combined result: Fully Supported
- Reason: S9 directly supports examining subgroup-specific performance together with uncertainty rather than relying only on aggregate or conventional discrete fairness metrics; S7 provides additional support for subgroup-specific evaluation but not the uncertainty component.

  - S9: Fully Supported — The source explicitly states that conventional accuracy-based fairness metrics can miss unequal confidence across groups and presents uncertainty-aware fairness evaluation across a gender-occupation dataset.
  - S7: Partially Supported — The source reports performance differences across race/ethnicity and age groups and uses multiple validation checks, but it does not address uncertainty or explicitly contrast these evaluations with conventional discrete fairness metrics.

### F9

**Claim:** Synthetic data can offer privacy benefits, but synthetic outputs should not automatically be treated as anonymous or compliant.

- Sources: S3, S4
- Combined result: Partially Supported
- Reason: Together, the sources support that synthetic data can provide privacy benefits and that anonymity should not be assumed where re-identification is plausible. They do not fully substantiate the broader statement that synthetic outputs should not automatically be treated as compliant, nor provide dataset-specific leakage or re-identification evidence.

  - S3: Partially Supported — S3 states that synthetic data may serve as a privacy substitute and that re-identification remains relevant where re-identification is plausible, supporting privacy benefits and caution against assuming anonymity. It does not directly establish the broader claim that outputs are not automatically compliant.
  - S4: Partially Supported — S4 directly describes privacy-preserving uses of synthetic medical and financial data and removal of direct links to individuals, supporting potential privacy benefits. The supplied text does not address re-identification risk or compliance, so it does not support the full caution.

### F10

**Claim:** The most defensible operational strategy is to supplement, not replace, curated real data; preserve provenance; filter and deduplicate aggressively; and evaluate factuality, diversity, subgroup performance, uncertainty, and real-world generalization separately.

- Sources: S3, S13, S1, S5, S14, S6, S10
- Combined result: Partially Supported
- Reason: Taken together, the sources support supplementing rather than replacing real data, preserving lineage, filtering and deduplicating synthetic data, using independent real holdouts, and distinguishing some evaluation measures. They do not directly establish the claim’s full “most defensible” prescription or explicitly support separately evaluating every listed dimension, especially uncertainty and subgroup performance.

  - S3: Partially Supported — Supports accumulating synthetic data alongside retained real data and using curation, quality controls, and deduplication, but does not directly establish all listed evaluation dimensions or provenance preservation.
  - S13: Partially Supported — Directly supports retaining a non-shrinking real-data anchor, tracking AI-generated proportions, provenance tracking, aggressive filtering, and real-example holdouts, but not the full evaluation framework.
  - S1: Partially Supported — Supports lineage and fidelity metadata and warns about recursive synthetic-data training, but provides little support for the complete operational strategy or separate evaluation dimensions.
  - S5: Partially Supported — Supports deduplication, filtering, quality and safety checks, and evaluation in realistic settings, but does not directly support provenance preservation, non-replacement of real data, or every listed metric.
  - S14: Partially Supported — Directly supports independent judging, rubric-based scoring, format and toxicity checks, aggressive filtering, deduplication, and diverse realistic seeds, but not provenance, uncertainty, subgroup performance, or real-world generalization as a whole.
  - S6: Partially Supported — Supports evaluating synthetic test collections against human-based evaluation because synthetic evaluations can be biased, but does not support the data-retention and pipeline-control recommendations or all listed evaluation dimensions.
  - S10: Partially Supported — Supports independent real holdouts and shows that training metrics may not predict the target F1 outcome, but does not address most of the proposed data-governance and evaluation strategy.

## Deterministic Failures

- None. All deterministic checks passed.
