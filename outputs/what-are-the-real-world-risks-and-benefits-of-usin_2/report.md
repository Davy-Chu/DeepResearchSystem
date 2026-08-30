# Research Report

## Research Question

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

## Summary

The ledger supports using synthetic data as a scalable supplement when real data is scarce, costly, privacy-sensitive, or difficult to label. Targeted generation may improve coverage of rare cases and underrepresented classes, and at least one domain-specific study reports gains from combining real and synthetic data. However, synthetic data can reproduce or amplify bias, omit subtle real-world patterns, narrow the training distribution through recursive use, and produce misleadingly strong results if evaluation data is contaminated or insufficiently independent. The evidence therefore favors controlled, quality-filtered, mixed-data use with multidimensional evaluation, but does not establish broad superiority over real-only data or a standardized safety and evaluation protocol.

## Findings

### Finding 1

**Claim**

Synthetic data can provide practical benefits by supplementing scarce, expensive, privacy-sensitive, or difficult-to-label real data, enabling faster and potentially lower-cost dataset creation, prototyping, and task-specific fine-tuning.

**Confidence:** High

**Why this confidence level**

Multiple sources directly support supplementation and efficiency benefits. The evidence does not establish that synthetic data is generally superior to real data.

**Evidence**

- Sources describe synthetic data as a scalable way to address scarce or expensive-to-label data, privacy constraints, rapid prototyping, and seed-based fine-tuning for tasks such as supervised fine-tuning, preference optimization, tool use, and retrieval-augmented generation. [S3] [S4] [S5] [S6] [S8] [S9] [S11] [S13]

### Finding 2

**Claim**

Targeted synthetic generation can expand coverage of underrepresented classes, rare cases, edge cases, and task-specific scenarios, with possible benefits for robustness and adaptability.

**Confidence:** Medium

**Why this confidence level**

The mechanisms for increasing coverage are directly supported, but consistent robustness gains across LLM tasks and domains are not established.

**Evidence**

- Sources describe deliberately generating rare, adversarial, underrepresented, diverse, and domain-specific examples; one domain-specific hybrid study reported improved adaptability. [S4] [S5] [S6] [S9]

### Finding 3

**Claim**

Synthetic data can reproduce or amplify generator and source-data biases, underrepresent demographics, and transfer teacher-model style or domain limitations to the trained model, potentially harming fairness and generalizability.

**Confidence:** High

**Why this confidence level**

Several sources directly identify bias amplification and representation gaps, and no supplied evidence contradicts the risk. The precise conditions under which synthetic data improves or worsens subgroup fairness remain unresolved.

**Evidence**

- Sources warn that synthetic generators may exaggerate existing bias, omit demographic groups, and transfer a teacher model’s formatting, refusal, distributional, or domain-coverage biases. Related fairness evidence indicates that deliberate balancing may improve fairness but can interact with utility and domain mismatch. [S3] [S5] [S6] [S8] [S10] [S11]

### Finding 4

**Claim**

Synthetic examples may lack realism and subtle real-world patterns, creating distribution shift, over-specialization, or poor generalization outside the synthetic training distribution.

**Confidence:** High

**Why this confidence level**

The ledger provides multiple direct warnings and empirical indications of real-versus-synthetic gaps, while qualifying that harm is not universal and depends on the generation and training setup.

**Evidence**

- Sources identify missing real-world complexity, mode collapse, teacher-style imitation, format over-specialization, domain gaps, and task-dependent performance. One study reports that blindly fine-tuning on synthetic data can reduce utility. [S4] [S5] [S6] [S8] [S10] [S11] [S13]

### Finding 5

**Claim**

Repeated recursive training on model-generated data without sufficient novel information, retained real data, or external feedback can narrow the distribution and cause model collapse or capability degradation.

**Confidence:** High

**Why this confidence level**

The claim is directly supported, including evidence distinguishing replacement-style self-training from additive use with real data. The amount of synthetic data or number of generations that creates substantial risk is unknown.

**Evidence**

- Sources report degradation under recursive or purely synthetic self-training and indicate lower risk when synthetic data is quality-filtered and accumulated alongside retained real data. [S2] [S3] [S7]

### Finding 6

**Claim**

Synthetic-data pipelines require validation of accuracy or fidelity, realism, diversity, coverage, bias, domain alignment, and downstream effects; automated or model-based checks should be supplemented by human evaluation where appropriate.

**Confidence:** High

**Why this confidence level**

The need for multidimensional validation is consistently supported. No single supplied method is shown to be sufficient.

**Evidence**

- Sources recommend statistical and automated checks, judge-model filtering, deduplication, faithfulness and instruction-adherence checks, diversity checks, human review, and controlled comparisons across generation strategies, tasks, and budgets. [S3] [S4] [S5] [S6] [S7] [S8] [S10] [S11] [S13]

### Finding 7

**Claim**

Models trained or fine-tuned with synthetic data should be evaluated on trusted real-world or independently grounded data and realistic tasks, using multiple utility and fairness measures rather than relying solely on static benchmark scores.

**Confidence:** High

**Why this confidence level**

The ledger strongly supports comparative, multidimensional evaluation, but does not provide a standardized protocol or broad independent validation.

**Evidence**

- Sources recommend comparison with trusted real-world data, ground truth, realistic settings, task-specific evaluation, subgroup fairness measures, and comparisons across training conditions. They also warn about benchmark saturation, contamination, and leakage. [S3] [S5] [S6] [S7] [S9] [S10] [S11] [S13]

### Finding 8

**Claim**

Synthetic data may provide privacy-related benefits by reducing direct exposure of actual records, but it is not established to be automatically private or disclosure-proof.

**Confidence:** Medium

**Why this confidence level**

The ledger contains meaningful support for privacy-motivated use and direct contrary evidence concerning re-identification and obligations. Reliable procedures for detecting leakage or memorization are not supplied.

**Evidence**

- Supporting sources describe synthetic data as useful when privacy or compliance constraints block direct data use and as potentially avoiding direct exposure of personal information. [S4] [S5] [S6] [S8]
- Contradicting evidence warns that privacy substitution can still involve re-identification and regulatory risk when generated records are plausible. [S7]

### Finding 9

**Claim**

A domain-specific study reported that combining real and synthetic conversational data outperformed real-only training and a base-model comparison on its reported metrics, but the result has limited external validity.

**Confidence:** Medium

**Why this confidence level**

The evidence is a direct comparative result, but it is limited to one vertical application and does not establish replication, broad task coverage, or superiority over synthetic-only training.

**Evidence**

- The reported experiment found the hybrid model had the highest scores and stronger adaptability in additional testing among the compared conditions. [S9]

### Finding 10

**Claim**

The best synthetic-generation strategy can depend on task and available generation budget: in one controlled study, answer augmentation was favored at low budgets, while new-question generation became more effective as the budget increased.

**Confidence:** Medium

**Why this confidence level**

The result spans three task types in a controlled study, but its generality to other models, domains, and training scales is not established.

**Evidence**

- A controlled comparison across mathematics, general question answering, and Text2SQL reported budget- and task-dependent differences among answer augmentation, question rephrasing, and new-question generation. [S13]

## Conflicts and Uncertainty

- Privacy benefits are supported, but synthetic data may still permit re-identification or create regulatory risk; the ledger does not establish when privacy protection is reliable. [S4] [S5] [S6] [S7] [S8]
- The ledger supports potential fairness improvements through targeted or balanced generation while also documenting bias amplification, demographic underrepresentation, and utility trade-offs. The conditions determining the outcome remain unresolved. [S5] [S8] [S10] [S11]
- Hybrid and strategy-specific performance gains are reported, but the evidence does not directly compare synthetic-only, real-only, and mixed-data fine-tuning across broad LLM settings. [S9] [S13]

## Remaining Gaps

- No controlled, LLM-specific comparison of synthetic-only, real-only, and mixed-data fine-tuning across data quality, bias, and downstream generalization is supplied.
- No reliable procedure for detecting privacy leakage or memorization in LLM-generated synthetic training data is supplied.
- The conditions under which synthetic data improves or worsens demographic fairness, including subgroup-specific outcomes, remain unresolved.
- The amount of synthetic data or recursive training needed before degradation or model collapse becomes likely is unknown.
- No standardized evaluation protocol is supplied for fidelity, novelty, contamination, bias shift, and real-world LLM performance.
- The external validity of reported hybrid-training benefits across domains, model sizes, task types, and synthetic-only baselines remains unresolved.
- The controlled LLM study does not establish whether its reported gains persist under independent real-world evaluation or against direct real-only, synthetic-only, and mixed-data baselines.

## Conclusion

Synthetic data offers clear operational benefits as a supplement: it can expand scarce training resources, target rare or underrepresented cases, and support faster fine-tuning. The principal risks are quality and distribution mismatch, inherited or amplified bias, recursive degradation, and potentially overstated results from weak or contaminated evaluation. On the supplied evidence, the most defensible approach is controlled, quality-filtered use—preferably retaining or mixing trusted real data—combined with independent real-world evaluation, realistic task testing, and explicit subgroup and privacy checks. A reliable general conclusion about synthetic-only training, fairness outcomes, privacy protection, or superiority over real-only training cannot currently be drawn.

## Sources

- [S1] Using Synthetic Data to Improve LLM Fine‑Tuning | newline — https://www.newline.co/@Dipen/using-synthetic-data-to-improve-llm-finetuning--d453f658
- [S2] Synthetic Data for AI Training: Use Cases and Risks [2026] — https://atlan.com/know/ai-agent/data-for-ai/synthetic-data-for-ai-training
- [S3] Large Language Models Are Still Getting Stronger, but Researchers Face New Bottlenecks in Data, Evaluation, and Safety | Newswise — https://www.newswise.com/articles/large-language-models-are-still-getting-stronger-but-researchers-face-new-bottlenecks-in-data-evaluation-and-safety
- [S4] Synthetic Data Generation with LLMs: Techniques and Use Cases — https://tetrate.io/learn/ai/synthetic-data-generation-llms
- [S5] Synthetic Data for ML: Uses, Risks, and Best Practices | CleverX Blog — https://cleverx.com/blog/synthetic-data-for-ml-the-game-changer-in-training-for-2025
- [S6] Synthetic Data for LLM Fine-Tuning 2026 — https://futureagi.com/blog/synthetic-data-fine-tuning-llms
- [S7] Synthetic Data for LLM Training: Decision Guide 2026 — https://www.digitalapplied.com/blog/synthetic-data-generation-llm-training-decision-guide-2026
- [S8] LLM synthetic data: Fine-tuning LLMs with AI-generated data | SuperAnnotate — https://www.superannotate.com/blog/llm-synthetic-data
- [S9] Hybrid Training Approaches for LLMs: Leveraging Real and Synthetic Data to Enhance Model Performance in Domain-Specific Applications — https://arxiv.org/html/2410.09168v1
- [S10] [PDF] Advancing Algorithmic Fairness via Selectively Fine-Tuning Biased ... — https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_AIM-Fair_Advancing_Algorithmic_Fairness_via_Selectively_Fine-Tuning_Biased_Models_with_CVPR_2025_paper.pdf
- [S11] LLM2LLM: Synthetic Data for Fine-Tuning (UC Berkeley) — https://www.youtube.com/watch?v=OBk3d8UDQ4g
- [S12] Synthetic Data + Evaluation Pipelines: Scaling Fine-Tuning ... — https://medium.com/@akankshasinha247/synthetic-data-evaluation-pipelines-scaling-fine-tuning-without-losing-alignment-f469a81cdf9a
- [S13] Synthetic Data Generation Strategies for Fine-Tuning LLMs — https://scale.com/blog/synthetic-data-fine-tuning-llms
