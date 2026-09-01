# Research Report

## Research Question

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

## Summary

This is an automatically generated incomplete report. The research run ended before a normal research stop reason was recorded, and normal finalization did not complete during OpenAI Research Decision — Iteration 4. The validated findings collected before that point are preserved below without claiming that the evidence is complete.

## Findings

### Finding 1

**Claim**

Synthetic data can transform how developers fine-tune large language models (LLMs), addressing critical limitations of real-world datasets and enabling new capabilities.

**Confidence:** High

**Why this confidence level**

The combination of several new evidentiary sources supports the transition to synthetic data.

**Evidence**

- Synthetic data improves LLM fine-tuning by addressing limitations in real-world datasets. [S1]
- Synthetic data mirrors real distributions to address data scarcity and privacy constraints, making it advantageous for AI training. [S2]
- Synthetic data can help fill data gaps, improving model performance in specific tasks. [S3]
- Diversity in synthetic data sources mitigates risks like distribution collapse, thereby improving model behavior during fine-tuning. [S4]
- Model collapse is avoidable by accumulating real data alongside synthetic data, rather than replacing it entirely. [S6]
- The integration of synthetic data can reduce costs and address data scarcity, but overreliance can lead to significant quality issues. [S8]
- Synthetic data generation is becoming a necessity due to high-quality training data depletion. [S12]

### Finding 2

**Claim**

Fine-tuning models on synthetic data from diverse sources can mitigate issues like distribution collapse and self-preference bias while preserving output quality.

**Confidence:** High

**Why this confidence level**

Conclusive evidence from a dedicated study shows the benefits of diverse synthetic data sources in fine-tuning models.

**Evidence**

- Increased diversity in synthetic training data reduces distribution collapse and preserves the quality of outputs. [S4]

### Finding 3

**Claim**

Excessive reliance on synthetic data may lead to model collapse, resulting in output degradation or narrowing over time if not balanced with diverse training data.

**Confidence:** High

**Why this confidence level**

Additional evidence corroborates that model collapse remains a significant concern when relying solely on synthetic data.

**Evidence**

- Recursive training on synthetic data can cause models to stagnate or degrade due to lack of novel information. [S2]
- Repetitive training on synthetic data without feedback can lead to decreased model capabilities and reliability. [S3]
- Overreliance on single-source synthetic data can exacerbate self-preference bias and reduce model robustness. [S4]
- Training AI on synthetic data often leads to model collapse, where outputs degrade in quality as models rely on biased, self-generated data. [S9]
- Synthetic data introduces risks such as feedback loops and model collapse, potentially leading to nonsensical outputs. [S10]
- Model collapse is a prominent issue when synthetic data is poorly designed or unverified. [S11]

### Finding 4

**Claim**

Synthetic data generation is becoming a necessary infrastructure for AI development due to the diminishing availability of high-quality human-generated training data and the increasing legal complexities surrounding real data usage.

**Confidence:** High

**Why this confidence level**

New sources reinforce the necessity of synthetic data amid real-world data challenges.

**Evidence**

- The impending shortage of high-quality human-generated data is pushing AI teams towards synthetic data as a critical resource. [S12]
- Synthetic data is gaining focus due to the challenges in accessing high-quality human-generated data and privacy regulations. [S15]
- The use of synthetic data significantly helps alleviate the scarcity of high-quality datasets and addresses privacy concerns in AI applications. [S16]

### Finding 5

**Claim**

Model collapse poses a significant risk when training generative models on synthetic data, particularly if the data lacks grounding in real-world distributions.

**Confidence:** High

**Why this confidence level**

Recent evidence reiterates the link between synthetic data usage and the risk of model collapse if quality is not maintained.

**Evidence**

- Synthetic data can lead to degradation in model performance through feedback loops, known as model collapse. [S11]
- Without adequate verification mechanisms, iterative training on synthetic data may worsen model quality over time. [S13]
- Synthetic datasets help mimic real-world scenarios and are crucial for testing and validating model performance, highlighting the risks associated with poor data quality leading to model collapse. [S17]

## Conflicts and Uncertainty

- No material conflict was identified in the retrieved evidence.

## Remaining Gaps

- Normal final synthesis did not complete, so the completeness of the evidence could not be confirmed.

## Conclusion

The findings above reflect the evidence validated before the run ended. They should be treated as provisional because normal final synthesis did not complete and important gaps may remain.

## Sources

- [S1] Using Synthetic Data to Improve LLM Fine‑Tuning | newline — https://www.newline.co/@Dipen/using-synthetic-data-to-improve-llm-finetuning--d453f658
- [S2] Synthetic Data for AI Training: Use Cases and Risks [2026] — https://atlan.com/know/ai-agent/data-for-ai/synthetic-data-for-ai-training
- [S3] Large Language Models Are Still Getting Stronger, but Researchers ... — https://www.newswise.com/articles/large-language-models-are-still-getting-stronger-but-researchers-face-new-bottlenecks-in-data-evaluation-and-safety
- [S4] Synthetic Eggs in Many Baskets:The Impact of Synthetic Data Diversity on LLM Fine-Tuning — https://arxiv.org/html/2511.01490v1
- [S5] [D] Is Synthetic Data a Reliable Option for Training Machine Learning ... — https://www.reddit.com/r/MachineLearning/comments/1bosj2t/d_is_synthetic_data_a_reliable_option_for
- [S6] Synthetic Data for LLM Training: Decision Guide 2026 — https://www.digitalapplied.com/blog/synthetic-data-generation-llm-training-decision-guide-2026
- [S7] The Danger of AI Model Collapse — https://www.thedigitalspeaker.com/danger-of-ai-model-collapse-llms-trained-synthetic-data
- [S8] Examining synthetic data: The promise, risks and realities | IBM — https://www.ibm.com/think/insights/ai-synthetic-data
- [S9] AI model collapse: risks of synthetic data in generative AI | LGT — https://www.lgt.com/global-en/insights/perspectives-and-society/poisoning-the-ai-well-336294
- [S10] Synthetic data, real harm | Ada Lovelace Institute — https://www.adalovelaceinstitute.org/blog/synthetic-data-real-harm
- [S11] Preventing Model Collapse with Synthetic Data — https://apxml.com/courses/synthetic-data-llm-pretrain-finetune/chapter-6-evaluating-synthetic-data-challenges/countering-model-performance-degradation
- [S12] Medium — https://pub.towardsai.net/why-2026-is-the-year-synthetic-data-becomes-non-negotiable-b5a2a84d1b1b
- [S13] Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence — https://arxiv.org/html/2510.16657v2
- [S14] Synthetic Data Generation with LLMs: Techniques and Use Cases - Tetrate — https://tetrate.io/learn/ai/synthetic-data-generation-llms
- [S15] A Multi-Faceted Evaluation Framework for Assessing Synthetic Data Generated by Large Language Models — https://arxiv.org/html/2404.14445v2
- [S16] Beyond Scarcity: How LLM-Driven Synthetic Data Generation is Reshaping AI — https://pub.towardsai.net/beyond-scarcity-how-llm-driven-synthetic-data-generation-is-reshaping-ai-8936cf6413d5
- [S17] Creating and Validating Synthetic Datasets for LLM Evaluation ... — https://arize.com/blog/creating-and-validating-synthetic-datasets-for-llm-evaluation-experimentation
