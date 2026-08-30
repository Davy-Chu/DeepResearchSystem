# Research Evaluation

**Evaluator:** evaluator-v0

**Model:** gpt-5.6-luna

**Timestamp:** 2026-08-30T22:05:01.294122+00:00

## Summary

- Coverage: 100%
- Core coverage: 100%
- Citation support: 90%
- Citation completeness: 100%
- Deterministic checks: 120 passed, 0 failed

## Coverage

### A1: Assess the real-world risks of using synthetic data to train or fine-tune large language models.

- Importance: Core
- Status: Covered
- Reason: The report substantively identifies real-world risks, including bias amplification, missing real-world complexity, distribution shift, recursive model collapse, privacy leakage, and misleading evaluation results.
- Report evidence: Findings 3–8 and the conclusion discuss bias, quality and generalization failures, recursive degradation, privacy and regulatory risk, and benchmark contamination.

### A2: Assess the real-world benefits of using synthetic data to train or fine-tune large language models.

- Importance: Core
- Status: Covered
- Reason: The report clearly addresses practical benefits, including scalability, lower-cost data creation, privacy-motivated use, rare-case coverage, prototyping, and task-specific fine-tuning.
- Report evidence: Findings 1, 2, 8, 9, and 10 describe operational benefits and report a domain-specific hybrid-training gain, while qualifying limited generality.

### A3: Evaluate how synthetic-data quality affects large language model training or fine-tuning outcomes.

- Importance: Core
- Status: Covered
- Reason: The report directly evaluates how fidelity, realism, diversity, coverage, domain alignment, teacher-style imitation, and recursive degradation affect training and fine-tuning outcomes.
- Report evidence: Findings 4–6 link data-quality problems to distribution shift, over-specialization, poor generalization, utility loss, and model collapse; Findings 9–10 describe task- and budget-dependent outcomes.

### A4: Evaluate bias risks and benefits associated with using synthetic data for large language models.

- Importance: Core
- Status: Covered
- Reason: The report addresses both bias risks and potential benefits: synthetic data may reproduce or amplify source and generator bias, omit demographic groups, or transfer teacher-model limitations, while targeted balancing may improve fairness with possible utility trade-offs.
- Report evidence: Finding 3 and the Conflicts and Uncertainty section cover bias amplification, underrepresentation, deliberate balancing, fairness improvements, and unresolved subgroup outcomes.

### A5: Address how the use of synthetic data should be evaluated, including the effectiveness and limitations of evaluation approaches.

- Importance: Core
- Status: Covered
- Reason: The report provides a substantive evaluation framework and discusses limitations, recommending multidimensional validation, human and automated checks, independent real-world data, fairness measures, realistic tasks, and contamination controls.
- Report evidence: Findings 6 and 7 specify fidelity, realism, diversity, coverage, bias, downstream effects, trusted independent evaluation, and subgroup metrics; the Remaining Gaps section notes the absence of a standardized protocol and reliable leakage-detection procedure.

## Citation Support

### F1

**Claim:** Synthetic data can provide practical benefits by supplementing scarce, expensive, privacy-sensitive, or difficult-to-label real data, enabling faster and potentially lower-cost dataset creation, prototyping, and task-specific fine-tuning.

- Sources: S3, S4, S5, S6, S8, S9, S11, S13
- Combined result: Fully Supported
- Reason: Taken together, the sources directly support the claim’s main components: supplementing scarce, costly, privacy-sensitive, and difficult-to-label real data; accelerating dataset creation and prototyping; reducing or improving cost efficiency; and enabling task-specific fine-tuning.

  - S3: Partially Supported — States that synthetic data can address limited high-quality data and expand resources for specific tasks, but does not directly establish lower cost, privacy benefits, or difficult labeling.
  - S4: Fully Supported — Directly describes synthetic data supplementing or replacing human-labeled data under scarcity, privacy, cost, and time constraints, while enabling rapid prototyping and task-oriented training.
  - S5: Fully Supported — Directly identifies scarcity, labeling expense, privacy risk, and time costs, and describes synthetic data for faster, lower-cost scaling and LLM fine-tuning.
  - S6: Fully Supported — Directly describes scarce and privacy-blocked real data, lower-cost synthetic expansion from small seeds, and task-specific fine-tuning workflows.
  - S8: Fully Supported — Directly states that synthetic data can be produced rapidly and cost-efficiently, address limited data and privacy issues, and support LLM fine-tuning.
  - S9: Partially Supported — Directly supports supplementing scarce, expensive-to-collect real data with synthetic data for more efficient fine-tuning, but does not directly support privacy or lower cost.
  - S11: Partially Supported — Describes generating missing domain-specific data when training data is insufficient and using it for fine-tuning, but provides little direct support for cost, privacy, or faster creation.
  - S13: Partially Supported — Directly addresses the fine-tuning data bottleneck and cost-efficiency of synthetic-data strategies, but does not directly cover privacy-sensitive or difficult-to-label data.

### F2

**Claim:** Targeted synthetic generation can expand coverage of underrepresented classes, rare cases, edge cases, and task-specific scenarios, with possible benefits for robustness and adaptability.

- Sources: S4, S5, S6, S9
- Combined result: Fully Supported
- Reason: Taken together, the sources directly support targeted synthetic generation to expand coverage across underrepresented, rare, edge-case, diverse, and task-specific scenarios, while documenting possible robustness, generalization, and adaptability benefits.

  - S4: Fully Supported — Directly describes targeted generation for underrepresented classes, rare edge cases, diverse examples, task-specific domains, and potential robustness benefits.
  - S5: Fully Supported — Describes synthetic generation of rare events, edge cases, hard-to-capture examples, and diverse task prompts, with reported robustness and generalization benefits.
  - S6: Partially Supported — Directly supports task-specific synthetic data generation and expansion from small seeds, but the supplied text does not clearly establish coverage of underrepresented classes or rare/edge cases, or resulting robustness benefits.
  - S9: Fully Supported — Describes synthetic personas and scenarios that enrich diversity and replicate rare, important, and edge-case scenarios, and reports improved robustness and adaptability in a domain-specific study.

### F3

**Claim:** Synthetic data can reproduce or amplify generator and source-data biases, underrepresent demographics, and transfer teacher-model style or domain limitations to the trained model, potentially harming fairness and generalizability.

- Sources: S3, S5, S6, S8, S10, S11
- Combined result: Fully Supported
- Reason: Taken together, the sources directly support bias reproduction or amplification, demographic coverage gaps, teacher-model bias/style inheritance, domain or distributional limitations, and resulting risks to fairness, utility, or generalizability.

  - S3: Partially Supported — Supports that synthetic data can introduce risks from biased or low-quality data and that repeated model-generated data may degrade capabilities, but does not directly address demographic underrepresentation or teacher-style/domain-bias transfer.
  - S5: Partially Supported — Directly states that generators can reproduce or exaggerate existing biases, underrepresent demographics, and affect fairness and generalizability, but does not address transfer of teacher-model style or domain limitations.
  - S6: Partially Supported — Directly describes teacher-bias inheritance, including copied formatting, refusal style, and length distribution, and notes mode collapse; it does not directly establish demographic underrepresentation or fairness harm.
  - S8: Partially Supported — States that biases in source human data may be magnified and that poorly constructed synthetic data can perform poorly on real-world data, but does not address demographic underrepresentation or teacher-model style transfer.
  - S10: Partially Supported — Identifies synthetic-data quality limits, bias shifts, domain gaps, and reduced utility from naive fine-tuning, while showing fairness–utility tradeoffs; it does not directly support demographic underrepresentation or teacher-style transfer.
  - S11: Partially Supported — States that teacher-model bias and incomplete domain coverage may transfer inadequately, and that distributional or domain discrepancies can limit student effectiveness; it does not directly address demographic underrepresentation.

### F4

**Claim:** Synthetic examples may lack realism and subtle real-world patterns, creating distribution shift, over-specialization, or poor generalization outside the synthetic training distribution.

- Sources: S4, S5, S6, S8, S10, S11, S13
- Combined result: Fully Supported
- Reason: Multiple sources directly support the claim's key components: missing realism and subtle patterns, over-specialization or mode collapse, domain shift, and degraded performance or generalization on real-world data.

  - S4: Partially Supported — The source states that synthetic-data utility depends on alignment between the synthetic distribution and the target application, but the supplied text does not directly describe realism gaps causing poor generalization.
  - S5: Fully Supported — It directly states that synthetic examples may lack realism and miss subtle patterns, reducing performance on real-world tasks, and emphasizes generalization to real-world scenarios.
  - S6: Fully Supported — It identifies mode collapse and teacher-bias inheritance, noting that students trained purely on synthetic data may mimic a teacher's format, refusal style, and length distribution.
  - S8: Fully Supported — It states that synthetic data may fail to mirror real-world complexities, perform poorly in practical situations, and cause overfitting to synthetic scenarios with degraded real-world performance.
  - S10: Fully Supported — It directly identifies domain gaps or shifts between real and synthetic data and states that blind fine-tuning on synthetic data can decrease utility.
  - S11: Fully Supported — It discusses failure to map the complexity and diversity of real-world distributions, limited transferability, and misalignment with domain-specific nuances.
  - S13: Partially Supported — It reports task-dependent differences in synthetic-data performance and strategy effectiveness, but does not directly establish realism deficits, distribution shift, or poor out-of-distribution generalization.

### F5

**Claim:** Repeated recursive training on model-generated data without sufficient novel information, retained real data, or external feedback can narrow the distribution and cause model collapse or capability degradation.

- Sources: S2, S3, S7
- Combined result: Fully Supported
- Reason: Together, the sources directly support recursive model-generated-data training causing distribution narrowing, model collapse, or degradation, especially without novel information, external feedback, or retained real data; S7 also supports mitigation through quality filtering and retaining real data.

  - S2: Partially Supported — States that recursive training on synthetic data causes model collapse and distributions narrow until outputs degrade, but the saved text does not support the added conditions about insufficient novel information, retained real data, or external feedback.
  - S3: Fully Supported — Directly states that repeated training on model-generated content without enough new information or reliable external feedback can cause capabilities to stagnate or degrade.
  - S7: Fully Supported — Describes collapse from repeated synthetic self-training, including distribution-tail loss and degradation, and contrasts it with lower-risk regimes retaining or accumulating real data and using curation.

### F6

**Claim:** Synthetic-data pipelines require validation of accuracy or fidelity, realism, diversity, coverage, bias, domain alignment, and downstream effects; automated or model-based checks should be supplemented by human evaluation where appropriate.

- Sources: S3, S4, S5, S6, S7, S8, S10, S11, S13
- Combined result: Fully Supported
- Reason: Collectively, the sources support validation of fidelity/realism, accuracy, diversity and coverage, bias, domain alignment, and downstream performance, while S5 and S8 directly support combining automated or model-based checks with human evaluation or oversight.

  - S3: Partially Supported — Discusses evaluating synthetic data for reliability, novelty, and verifiability, and broader evaluation for real-world performance, fairness, and safety, but does not directly provide the full validation checklist or human-evaluation recommendation.
  - S4: Partially Supported — States that validation methods and alignment with target-application requirements are critical and describes synthetic data as realistic and diverse, but the supplied text does not establish all listed checks or human supplementation.
  - S5: Fully Supported — Directly recommends evaluating accuracy, diversity, realism, representativeness, and robustness using automated/statistical and manual methods, with human evaluation and oversight; it also addresses bias and benchmarking against trusted real-world data.
  - S6: Partially Supported — Describes judge-model filtering, faithfulness and instruction-adherence checks, and diversity checks, but does not directly support human evaluation or the full range of listed validation dimensions.
  - S7: Partially Supported — Frames synthetic-data use cases as having distinct failure modes and quality metrics and emphasizes curation, but the supplied excerpt does not directly specify the complete validation process or human evaluation.
  - S8: Partially Supported — Supports checking realism, quality, relevance, bias, and real-world performance, and recommends combining model-in-the-loop evaluation with human data, but does not cover every listed validation dimension explicitly.
  - S10: Partially Supported — Directly identifies synthetic-data quality, diversity, domain gaps, bias gaps, and effects on accuracy, fairness, and utility, but does not recommend human evaluation or cover the complete checklist.
  - S11: Partially Supported — Explicitly calls for critical assessment of synthetic-data quality, domain coverage, bias, diversity, transferability, and domain-specific alignment, but does not support human supplementation or all downstream validation details.
  - S13: Partially Supported — Describes controlled comparisons across generation strategies, tasks, prompts, budgets, and accuracy, and mentions verification of synthetic responses, but does not establish the full validation checklist or human evaluation.

### F7

**Claim:** Models trained or fine-tuned with synthetic data should be evaluated on trusted real-world or independently grounded data and realistic tasks, using multiple utility and fairness measures rather than relying solely on static benchmark scores.

- Sources: S3, S5, S6, S7, S9, S10, S11, S13
- Combined result: Partially Supported
- Reason: Together, the sources support evaluating synthetic-data-trained models or datasets against real or ground-truth data, using realistic or varied tasks, and considering multiple metrics while recognizing benchmark limitations. However, coverage is uneven: no source directly supports every element of the claim as a general recommendation, especially the combined requirement for independently grounded evaluation and multiple utility and fairness measures rather than static benchmarks alone.

  - S3: Partially Supported — Supports realistic-task evaluation and warns that static benchmarks can be saturated, contaminated, or leaky, but does not directly establish evaluation against trusted real-world data or use of multiple utility and fairness measures.
  - S5: Partially Supported — Directly recommends benchmarking against trusted real-world datasets and comparing outputs with ground truth, and describes multiple quality metrics, but does not specifically support multiple fairness measures or realistic task evaluation of the trained model.
  - S6: Partially Supported — Supports using a small real-data seed as ground-truth anchoring and conducting diversity and quality checks, but provides little direct support for trusted independent evaluation, realistic tasks, or multiple fairness measures.
  - S7: Partially Supported — Distinguishes synthetic evaluation-set creation from other uses and discusses quality metrics and retaining real data, but the supplied text does not directly recommend the full evaluation procedure in the claim.
  - S9: Partially Supported — Reports evaluation of models trained under real and hybrid conditions across multiple metrics and diverse scenarios, but does not directly require trusted independent data, fairness measures, or avoiding static benchmarks.
  - S10: Partially Supported — Uses real-world datasets and explicitly reports both utility and subgroup fairness measures, while identifying the real–synthetic domain gap; it does not directly address realistic tasks or static benchmark limitations generally.
  - S11: Partially Supported — Explicitly calls for critical assessment of synthetic-data quality, transferability, domain alignment, bias, and real-world distributional differences, but gives no direct recommendation for trusted evaluation data or multiple utility and fairness metrics.
  - S13: Partially Supported — Evaluates synthetic-data strategies across mathematics, question answering, and Text2SQL tasks and discusses verification and accuracy, but does not directly support trusted real-world evaluation, fairness measures, or the rejection of static benchmark-only evaluation.

### F8

**Claim:** Synthetic data may provide privacy-related benefits by reducing direct exposure of actual records, but it is not established to be automatically private or disclosure-proof.

- Sources: S4, S5, S6, S8, S7
- Combined result: Fully Supported
- Reason: S4, S5, S6, and S8 provide evidence for privacy-related benefits or reduced exposure, while S7 directly supplies the important qualification that plausible generated records can still create re-identification and regulatory risk.

  - S4: Partially Supported — States synthetic data can remove direct links to individual records and avoid exposing actual personal information, but does not establish that it is not automatically private or disclosure-proof.
  - S5: Partially Supported — Describes synthetic data as useful where privacy constraints make real data risky to share and says it can avoid exposing patient data, but does not directly address whether it is automatically private or disclosure-proof.
  - S6: Partially Supported — Shows synthetic data being considered when privacy teams block real tickets, supporting a privacy-related benefit, but provides no direct evidence about exposure reduction or disclosure-proof status.
  - S8: Partially Supported — Claims synthetic data can avoid using personal information and provide privacy protection, but does not substantiate the caution that privacy is not automatic or disclosure-proof.
  - S7: Fully Supported — Explicitly identifies privacy substitution as carrying GDPR pseudonymization risk where re-identification is plausible, supporting the warning that synthetic data is not disclosure-proof.

### F9

**Claim:** A domain-specific study reported that combining real and synthetic conversational data outperformed real-only training and a base-model comparison on its reported metrics, but the result has limited external validity.

- Sources: S9
- Combined result: Partially Supported
- Reason: S9 supports the reported comparative performance, including the base-model comparison, but does not support the claim's limitation concerning external validity.

  - S9: Partially Supported — The source directly reports that the hybrid model outperformed the real-data-only and base-model conditions and had the highest scores across metrics. However, the saved text does not directly state that the result has limited external validity.

### F10

**Claim:** The best synthetic-generation strategy can depend on task and available generation budget: in one controlled study, answer augmentation was favored at low budgets, while new-question generation became more effective as the budget increased.

- Sources: S13
- Combined result: Fully Supported
- Reason: S13 directly supports the claim that the preferred synthetic-generation strategy varies with task and available budget, including the stated low-budget advantage of answer augmentation and increased-budget advantage of new-question generation.

  - S13: Fully Supported — The source describes a controlled experiment across mathematics, general question answering, and Text2SQL, and directly states that answer augmentation is most effective at a low query-budget ratio while generating new questions becomes advantageous as the ratio increases.

## Deterministic Failures

- None. All deterministic checks passed.
