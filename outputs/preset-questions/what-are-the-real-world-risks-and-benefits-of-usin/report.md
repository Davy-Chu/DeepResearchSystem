# Research Report

## Research Question

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

## Summary

Synthetic data can address scarcity, annotation cost, privacy constraints, class imbalance, and rare-case coverage. Its benefits are conditional on careful generation, validation, and mixture design. The strongest evidence indicates that small, validated synthetic datasets can outperform larger unvalidated ones for some tasks, while synthetic benchmarks and training data can misrepresent real-world behavior, reproduce generator-specific artifacts, reduce diversity, or contribute to model collapse when recursively replacing real data. Evidence for demographic or subgroup-fairness effects remains insufficient.

## Findings

### Finding 1

**Claim**

Synthetic data is most useful as a supplement to real data for targeted tasks, rather than as a universal replacement.

**Confidence:** Medium

**Why this confidence level**

The practical benefits recur across sources and include empirical task-specific results, but most reported gains are domain- and configuration-dependent rather than universal.

**Evidence**

- Synthetic data is described as useful for data scarcity, expensive annotation, privacy-sensitive domains, class imbalance, rare or edge cases, rapid prototyping, and domain adaptation. [S1] [S4] [S13]
- Evidence from requirements classification reports benefits from hybrid real-plus-synthetic training, but also reports lower synthetic diversity and degradation when synthetic sources are mixed indiscriminately. [S13]
- A model-collapse analysis summarized in S1 recommends accumulating synthetic data alongside real data rather than replacing real data. [S1]

### Finding 2

**Claim**

Data quality and validation matter more than synthetic-data volume alone; validated synthetic data can outperform larger unvalidated datasets.

**Confidence:** High

**Why this confidence level**

S14 provides direct comparative experiments, and S13 supplies convergent evidence that quality-control interventions have non-uniform downstream effects.

**Evidence**

- In tool-use experiments across two benchmarks, models trained on smaller datasets that passed human-defined or model-driven quality checks performed better or comparably to models trained on larger unvalidated datasets. [S14]
- The same study found task-critical errors in generated instructions and ground-truth API-call sequences, showing that plausible examples may contain substantive mistakes. [S14]
- In requirements data, multi-sample prompting improved utility and diversity, while prompt optimization and similarity-based curation had task-dependent effects; improving diversity did not consistently improve classification performance. [S13]

### Finding 3

**Claim**

Recursive or replacement-based training on model-generated data can narrow the data distribution and cause model collapse, whereas additive use with retained real data is presented as safer.

**Confidence:** Medium

**Why this confidence level**

The direction of the risk is consistent across sources, but the retrieved material does not provide the primary papers or enough detail to establish how broadly the reported results apply to current architectures and fine-tuning regimes.

**Evidence**

- S1 describes model collapse as loss of low-probability but valid examples and reports severe perplexity degradation in an OPT-125m experiment using purely synthetic data. [S1]
- S2 independently warns that recursive synthetic-data training can narrow distributions until outputs degrade. [S2]
- S1 contrasts replacement with additive accumulation alongside real data and presents the latter as having bounded error under the cited analysis. [S1]

### Finding 4

**Claim**

Synthetic data can reproduce generator-specific errors, biases, and distribution artifacts; current evidence is stronger for reduced diversity and self-bias than for demographic fairness effects.

**Confidence:** Medium

**Why this confidence level**

There is direct evidence for generator–evaluator self-bias and distributional limitations, but the retrieved research does not include controlled measurements of protected-group fairness against matched real-data baselines.

**Evidence**

- Synthetic requirements data showed lower diversity than real data, and curation choices changed diversity and task performance in different directions. [S13]
- When an LLM both generated benchmark data and solved the task, smaller models performed somewhat better on their own generated data; larger models showed little or no significant self-bias. [S11] [S12]
- Sources warn that synthetic data reflects the generator’s learned patterns and can reproduce errors, artifacts, or biases from the generator, prompts, or filtering process. [S1] [S4] [S5]

### Finding 5

**Claim**

Synthetic evaluation sets can be useful for simple or targeted tasks, but their validity declines for more complex tasks and can produce misleading model comparisons.

**Confidence:** High

**Why this confidence level**

S11 directly compares synthetic and real benchmark behavior and measures generator–evaluator bias; the broader contamination and realism concerns are consistent with the other sources.

**Evidence**

- Across six datasets and three NLP tasks, synthetic benchmarks tracked real-data performance more effectively for intent classification than for named-entity recognition. [S11]
- Averaging data generated by multiple LLMs produced a more robust and representative benchmark than relying on one generator. [S11] [S12]
- Synthetic evaluation is exposed to evaluation overfitting, contamination, leakage, benchmark saturation, and weak correspondence with complex real-world behavior. [S1] [S5]

### Finding 6

**Claim**

Evaluation should combine synthetic tests with independent real-world or human-authored data and assess more than aggregate benchmark scores.

**Confidence:** Medium

**Why this confidence level**

The recommendation follows from empirical representativeness failures and evaluation risks, but the retrieved sources do not establish a single validated evaluation protocol.

**Evidence**

- The sources call for evaluation covering reliability, robustness, fairness, reproducibility, safety, realistic application settings, and complex or agentic behavior rather than relying only on static benchmarks. [S4] [S5]
- The task-dependent benchmark results show why synthetic evaluations should be checked against real-data performance and generated by multiple models where feasible. [S11] [S12]

### Finding 7

**Claim**

Synthetic data may reduce privacy and sharing barriers, but generating synthetic records does not by itself establish privacy protection.

**Confidence:** Medium

**Why this confidence level**

The sources support the conditional privacy benefit and governance need, but provide no quantitative re-identification, memorization, or formal privacy-guarantee results.

**Evidence**

- Synthetic data is presented as potentially useful for privacy-sensitive healthcare, financial, and communications data by removing direct links to original records. [S4]
- S1 notes that plausible re-identification remains relevant to privacy and compliance decisions, while S2 emphasizes lineage and fidelity metadata and warns about audit gaps. [S1] [S2]

## Conflicts and Uncertainty

- Some sources use broad language that synthetic data can replace human-labeled or real data, while the stronger cautionary evidence favors retaining real data and using synthetic data additively. The difference appears conditional on task, curation, and training mixture rather than a direct contradiction. [S1] [S4] [S13]
- Synthetic requirements data reportedly outperformed human-authored data on selected security and defect-classification tasks, yet the same study found lower diversity and harmful effects from indiscriminate mixing. This indicates task-specific benefits rather than general superiority. [S13]
- Diversity and downstream utility do not always move together: similarity-based curation improved diversity metrics but often reduced classification performance. [S13]
- Larger models showed little self-bias in one synthetic-benchmark study, whereas smaller models showed self-preference. This qualifies, but does not eliminate, concerns about generator–evaluator overlap. [S11] [S12]
- The research stopped at the iteration limit. Quantitative evidence on demographic or subgroup fairness, out-of-distribution performance, calibration, hallucination, safety, and privacy leakage remains unresolved. [S6] [S7] [S11] [S13] [S14]

## Remaining Gaps

- Controlled comparisons of subgroup and demographic fairness for synthetic-versus-real fine-tuning mixtures.
- Evidence on how synthetic fine-tuning affects out-of-distribution generalization, calibration, hallucination, rare-event recall, and safety.
- Validated cross-domain quality-control pipelines comparing human review, external-model checking, deduplication, provenance tracking, and verifier-based generation.
- More evidence on correlation between synthetic benchmarks and independent human-authored or real-world evaluations, especially for multilingual, generative, safety, and agentic tasks.
- Formal privacy guarantees and empirical re-identification or memorization tests for synthetic data generated from confidential records.
- Sensitivity analyses for generator size, prompt design, synthetic-to-real ratio, filtering thresholds, and model architecture.

## Conclusion

Synthetic data offers real operational benefits when used to fill specific gaps—especially scarce labels, rare cases, privacy-constrained data, and targeted task coverage. The defensible pattern in the accumulated evidence is quality-controlled, provenance-aware, additive use alongside real data, with independent validation. The main risks are erroneous or biased examples, reduced diversity, generator–evaluator self-bias, misleading synthetic benchmarks, and distribution collapse under recursive replacement. Because the evidence on subgroup fairness and several real-world deployment outcomes is incomplete—and research stopped at the iteration limit—synthetic data should be treated as a conditional instrument requiring real-data comparison and independent evaluation, not as an automatic substitute for authentic data.

## Sources

- [S1] Synthetic Data for LLM Training: Decision Guide 2026 — https://www.digitalapplied.com/blog/synthetic-data-generation-llm-training-decision-guide-2026
- [S2] Synthetic Data for AI Training: Use Cases and Risks [2026] — https://atlan.com/know/ai-agent/data-for-ai/synthetic-data-for-ai-training
- [S3] Using Synthetic Data to Improve LLM Fine‑Tuning | newline — https://www.newline.co/@Dipen/using-synthetic-data-to-improve-llm-finetuning--d453f658
- [S4] Synthetic Data Generation with LLMs: Techniques and Use Cases — https://tetrate.io/learn/ai/synthetic-data-generation-llms
- [S5] Large Language Models Are Still Getting Stronger, but ... — https://www.newswise.com/articles/large-language-models-are-still-getting-stronger-but-researchers-face-new-bottlenecks-in-data-evaluation-and-safety
- [S6] [2605.19999] LLM Benchmark Datasets Should Be Contamination-Resistant — https://arxiv.org/abs/2605.19999
- [S7] LLMSS 2026 — LLM & Social Sciences Conference — https://eps-academic.org/ai-conference
- [S8] Study with us — https://www.griffith.edu.au/research/institute-biomedicine-glycomics/study
- [S9] TMLE Papers - Sky Qiu — https://sky-stats.com/tmle-papers.html
- [S10] [2409.11968] Efficacy of Synthetic Data as a Benchmark — https://arxiv.org/abs/2409.11968
- [S11] Efficacy of Synthetic Data as a Benchmark — https://arxiv.org/html/2409.11968v1
- [S12] Unveiling the Potential of Synthetic Text Data: Evaluating LLM-Generated Benchmarks for NLP Tasks - Diabolocom — https://www.diabolocom.com/research/synthetic-text-data-evaluating-llm-generated-benchmarks-nlp-tasks
- [S13] How Good Are Synthetic Requirements ? Evaluating LLM-Generated Datasets for AI4RE — https://arxiv.org/html/2506.21138v1
- [S14] [PDF] Quality Matters: Evaluating Synthetic Data for Tool-Using LLMs — https://aclanthology.org/2024.emnlp-main.285.pdf
