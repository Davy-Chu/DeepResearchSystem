# Research Report

## Research Question

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

## Summary

Synthetic data can provide substantial practical benefits by expanding scarce, costly, or sensitive training and fine-tuning data; targeting rare cases, minority classes, domain tasks, reasoning traces, code, and preference examples; and improving scalability and, in some settings, inference efficiency. These benefits are conditional: generated data must be relevant, sufficiently accurate, diverse, and aligned with the target distribution. Major risks include factual or label errors, stylistic and distributional artifacts, concealed or amplified bias, domain shift, evaluation contamination, and recursive degradation or model collapse when synthetic data replaces rather than supplements real data. The supplied evidence supports careful mixing with real data, filtering, task-specific verification, subgroup evaluation, and independent evaluation data, but does not provide controlled LLM-specific evidence sufficient to determine demographic effects, privacy guarantees, or comparative real-world outcomes across generation and training conditions.

## Findings

### Finding 1

**Claim**

Synthetic data can expand the quantity and coverage of data available for LLM pretraining or fine-tuning, particularly for low-resource domains, rare edge cases, underrepresented classes, reasoning traces, code, instruction-following, and preference optimization. The benefit depends on generation quality and alignment with the target task distribution.

**Confidence:** High

**Why this confidence level**

The claim is supported by multiple direct sources and a broad survey, although the evidence conditions benefits on task relevance and generation quality.

**Evidence**

- Sources describe synthetic data as a response to scarce real-world and domain-specific data and report uses in augmentation, minority-class generation, domain adaptation, edge-case generation, instruction tuning, code, question answering, and preference data. [S2] [S4] [S5] [S7] [S9] [S10]

### Finding 2

**Claim**

Synthetic data can improve scalability, consistency, class balance, privacy-oriented data sharing, annotation cost, and—in a specific low-resource classification setting—inference efficiency. These operational benefits do not establish factual accuracy, representativeness, safety, or privacy by themselves.

**Confidence:** High

**Why this confidence level**

The operational benefits and their limitations are supported by several sources; the efficiency result is narrower and task-specific.

**Evidence**

- Sources identify scarcity, privacy constraints, class imbalance, annotation cost, and controllable coverage as motivations or potential benefits of synthetic data. [S1] [S4] [S7] [S10]
- A low-resource classification experiment reported accuracy comparable to or better than in-context learning and approximately two- to five-times faster inference after synthetic-data PEFT, but only in the reported task and method setting. [S9]
- Other evidence warns that synthetic data may lack novelty or reliability, exhibit insufficient stylistic or distributional realism, and trade off accuracy against balancing or scalability benefits when a domain gap exists. [S5] [S6] [S10]

### Finding 3

**Claim**

Replacing real data with recursively generated synthetic data can cause model collapse: later training generations may lose low-probability or tail examples, accumulate errors, reduce diversity, and degrade factuality, robustness, or general quality. This risk is conditional rather than inevitable; accumulating synthetic data alongside real data is reported as a mitigation.

**Confidence:** High

**Why this confidence level**

Multiple sources directly support recursive-degradation risks and distinguish replacement from mixed-data conditions.

**Evidence**

- Sources warn that recursive training on model-generated content can narrow the distribution, lose distribution tails, and degrade capabilities. [S1] [S3] [S5] [S10]
- Evidence also reports that error can remain bounded when synthetic data is accumulated with real data rather than used as a replacement, and identifies blending real and synthetic data as a mitigation. [S3] [S10]

### Finding 4

**Claim**

Synthetic generation can reduce observed class imbalance and improve coverage of rare cases, but prompting, sampling, filtering, and generator characteristics can encode, amplify, or conceal bias. The supplied evidence does not directly quantify demographic or linguistic disparities in LLM outcomes.

**Confidence:** Medium

**Why this confidence level**

The mechanistic account of how generation pipelines can affect bias is supported, but direct LLM-specific subgroup evidence is absent.

**Evidence**

- Sources describe minority-class and rare-case generation as potential mitigation and identify selection, linguistic coverage, prompt design, filtering, weighting, and controlled generation as determinants of bias. [S1] [S4] [S6] [S8] [S10]
- The supplied evidence explicitly notes that direct empirical measurements of demographic or linguistic disparities in LLM training or fine-tuning outcomes are unavailable. [S1] [S4] [S6] [S8] [S10]

### Finding 5

**Claim**

Fairness interventions using synthetic data involve a utility trade-off unless generation quality and synthetic-to-real domain and bias shifts are addressed. Balanced synthetic data may improve fairness while reducing accuracy, whereas contextual generation and selective fine-tuning were reported to improve fairness while maintaining utility in the supplied non-LLM image-classification evidence.

**Confidence:** Medium

**Why this confidence level**

The evidence is empirical but comes from image classification rather than LLM training or fine-tuning, so its transfer to LLMs is indirect.

**Evidence**

- Experiments reported improved fairness from balanced synthetic data but possible accuracy loss under a real-versus-synthetic domain gap; contextual generation plus selective fine-tuning improved fairness while maintaining utility. [S6]

### Finding 6

**Claim**

Evaluation should not rely only on conventional benchmarks, synthetic test data, or automated judgments produced by the same or similar models as the training-data generator. A stronger evaluation program uses realistic held-out tasks and independent checks for factuality, label quality, robustness, calibration, contamination, subgroup disparities, safety, and deployment behavior. Synthetic data can still be useful for targeted edge-case, adversarial, calibration, and robustness testing when validated against the target distribution.

**Confidence:** High

**Why this confidence level**

The need for broader and more independent evaluation is supported by multiple sources. The evidence also directly exposes limitations of same-model filtering and automated judging.

**Evidence**

- Sources identify benchmark saturation, contamination and leakage, static-test limitations, and failures to detect reasoning, agentic, fairness, reproducibility, and safety problems. [S3] [S5] [S10]
- Synthetic examples can support edge-case, adversarial, ambiguity, calibration, and robustness testing, but their utility depends on validation and target-distribution alignment. [S4]
- Reward-model filtering and same-LLM label-consistency filtering provide automated quality-control signals for synthetic fine-tuning data, while execution feedback offers task-specific verification for code. [S7] [S9] [S10]
- The same-model filtering and LLM-as-a-judge approaches do not independently establish factuality, robustness, subgroup fairness, contamination resistance, or detection of shared generator errors. [S9] [S11]
- The supplied evidence recommends semantic or judgment-based evaluation and human oversight because conventional string matching is insufficient for generative responses, while also indicating that such judgment systems require independent validation. [S11]

## Conflicts and Uncertainty

- Synthetic data is reported to improve scale, coverage, controllability, privacy-oriented sharing, and class balance, but other evidence reports factual unreliability, insufficient realism, domain shift, and accuracy-utility trade-offs. Whether the net result is beneficial depends on generation and verification conditions. [S1] [S4] [S5] [S6] [S7] [S9] [S10]
- Recursive synthetic-data training is associated with model collapse and loss of distribution tails, while evidence indicates that retaining or accumulating real data alongside synthetic data can bound error or mitigate degradation. The evidence therefore distinguishes replacement from mixed-data use rather than establishing a universal effect. [S3] [S5] [S10]
- Synthetic balancing and fairness-focused generation may improve subgroup fairness, but blindly using balanced synthetic data can reduce accuracy or utility under domain shift. The direct empirical evidence for this trade-off is from image classification, not LLMs. [S6]
- Automated filtering or evaluation can improve scalability and provide useful quality signals, but filtering with the same generator or judging with a similar model may share generator-specific errors and cannot independently establish factuality, fairness, robustness, or contamination resistance. [S9] [S11]

## Remaining Gaps

- G1: No supplied source directly measures how synthetic-data generation, prompting, filtering, or mixing affects demographic representation, stereotyping, linguistic coverage, or subgroup fairness in LLM training or fine-tuning.
- G2: No supplied source provides a controlled, independent comparison of factual accuracy, label quality, calibration, robustness, contamination, or deployment outcomes against comparable real-data baselines.
- G3: The evidence does not establish when privacy-oriented synthetic data is genuinely non-identifying or how privacy protection trades off against fidelity and downstream model quality.
- G4: The evidence does not clearly separate pretraining effects from supervised fine-tuning effects across generation methods, synthetic-to-real ratios, verification procedures, and deployment contexts.

## Conclusion

The ledger supports a conditional conclusion: synthetic data is most promising as a targeted supplement to real data, especially where data are scarce, costly, privacy-sensitive, or insufficient for rare cases and domain-specific tasks. Its benefits are not guaranteed by scale or balance. Poorly verified or distributionally misaligned data can introduce factual and label errors, distort coverage, hide or amplify bias, and contribute to recursive degradation if it displaces real data. Models should therefore be evaluated with independent, held-out and human-authored or otherwise independently sourced data, realistic tasks, subgroup analyses, factuality and robustness checks, contamination checks, and deployment-relevant outcomes. The supplied ledger does not support a firm general conclusion about demographic fairness, privacy protection, or comparative real-world performance across pretraining and fine-tuning settings.

## Sources

- [S1] Synthetic Data for AI Training: Use Cases and Risks [2026] — https://atlan.com/know/ai-agent/data-for-ai/synthetic-data-for-ai-training
- [S2] Using Synthetic Data to Improve LLM Fine‑Tuning | newline — https://www.newline.co/@Dipen/using-synthetic-data-to-improve-llm-finetuning--d453f658
- [S3] Synthetic Data for LLM Training: Decision Guide 2026 — https://www.digitalapplied.com/blog/synthetic-data-generation-llm-training-decision-guide-2026
- [S4] Synthetic Data Generation with LLMs: Techniques and Use Cases — https://tetrate.io/learn/ai/synthetic-data-generation-llms
- [S5] Large Language Models Are Still Getting Stronger, but ... — https://www.newswise.com/articles/large-language-models-are-still-getting-stronger-but-researchers-face-new-bottlenecks-in-data-evaluation-and-safety
- [S6] Advancing Algorithmic Fairness via Selectively Fine-Tuning ... — http://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_AIM-Fair_Advancing_Algorithmic_Fairness_via_Selectively_Fine-Tuning_Biased_Models_with_CVPR_2025_paper.pdf
- [S7] Medium — https://medium.com/@wonseok.chris.choi/generating-synthetic-datasets-for-direct-preference-optimization-fine-tuning-of-llms-slms-f8c6c9fd7e07
- [S8] Data bias in LLM and generative AI applications - MOSTLY AI powered by Syntho — https://mostly.ai/blog/data-bias-types
- [S9] Enhancing Low-Resource LLMs Classification with PEFT ... — https://aclanthology.org/2024.lrec-main.533.pdf
- [S10] Synthetic Data Generation Using Large Language Models — https://arxiv.org/html/2503.14023v2
- [S11] Medium — https://medium.com/@akankshasinha247/synthetic-data-evaluation-pipelines-scaling-fine-tuning-without-losing-alignment-f469a81cdf9a
- [S12] Assessment of fine-tuned large language models for real-world chemistry and material science applications† — https://pmc.ncbi.nlm.nih.gov/articles/PMC11629507
