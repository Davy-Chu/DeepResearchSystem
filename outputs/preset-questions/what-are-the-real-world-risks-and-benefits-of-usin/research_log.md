# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 14

**OpenAI Calls:** 4

**Tavily Calls:** 3

**Started:** 2026-08-31T17:06:33-04:00

**Ended:** 2026-08-31T17:07:42-04:00

**Total Runtime:** 68.97s

---

# Iteration 1

## 1. Search

**Query**

> What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

**Why this query**

This is the user's original research question.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S1 — Synthetic Data for LLM Training: Decision Guide 2026**
  URL: https://www.digitalapplied.com/blog/synthetic-data-generation-llm-training-decision-guide-2026
- **S2 — Synthetic Data for AI Training: Use Cases and Risks [2026]**
  URL: https://atlan.com/know/ai-agent/data-for-ai/synthetic-data-for-ai-training
- **S3 — Using Synthetic Data to Improve LLM Fine‑Tuning | newline**
  URL: https://www.newline.co/@Dipen/using-synthetic-data-to-improve-llm-finetuning--d453f658
- **S4 — Synthetic Data Generation with LLMs: Techniques and Use Cases**
  URL: https://tetrate.io/learn/ai/synthetic-data-generation-llms
- **S5 — Large Language Models Are Still Getting Stronger, but ...**
  URL: https://www.newswise.com/articles/large-language-models-are-still-getting-stronger-but-researchers-face-new-bottlenecks-in-data-evaluation-and-safety

**Search Duration:** 2.71s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data can reduce data scarcity and annotation costs, and can be useful for domain adaptation, privacy-sensitive development, class-imbalance mitigation, edge-case generation, and rapid prototyping.

**Confidence:** Medium

**Why this confidence level**

The use cases are consistently described by two sources, but both are practitioner-oriented secondary sources rather than direct comparative studies.

**Evidence**

- S4 describes synthetic data as useful where real data is scarce, expensive, privacy-sensitive, ethically difficult to collect, or contains rare classes and edge cases. It also identifies augmentation, privacy-preserving data sharing, prototyping, evaluation, and domain adaptation as use cases. [S4]
- S1 distinguishes four applications—fine-tuning data, evaluation sets, edge-case augmentation, and privacy substitution—and states that each has different failure modes and quality metrics. [S1]

#### Finding 2

**Claim**

Synthetic data can improve task-specific performance when it is carefully curated and combined with real data, but the evidence does not support treating synthetic data as a universal replacement for real data.

**Confidence:** Medium

**Why this confidence level**

The sources provide a plausible conditional benefit and one concrete case, but the reported benchmark results are summarized second-hand and may not establish that synthetic data itself caused the improvement.

**Evidence**

- S1 reports that Microsoft’s Phi-1 used curated web data plus approximately one billion synthetic textbook and exercise tokens and achieved reported HumanEval and MBPP results; the source presents this as evidence for disciplined curation rather than raw synthetic-data volume. [S1]
- S1 states that the recommended regime is to accumulate synthetic data alongside real data rather than replace real data, citing an analytical result attributed to Gerstgrasser et al. [S1]
- S4 says that synthetic-data utility depends critically on generation technique, validation, and alignment between the synthetic distribution and the target application. [S4]

#### Finding 3

**Claim**

Training recursively on model-generated data can cause model collapse or distribution narrowing, especially when synthetic data replaces rather than supplements real data.

**Confidence:** Medium

**Why this confidence level**

The collapse risk is described consistently by multiple sources, but the retrieved material does not include the primary papers or enough experimental detail to assess regime, metric, and generalizability.

**Evidence**

- S1 describes the Nature study by Shumailov et al. as finding irreversible defects from indiscriminate use of model-generated content, including loss of low-probability (“tail”) examples and compounding approximation errors. [S1]
- S1 reports OPT-125m experiments in which five epochs of training with purely synthetic data led to a 20–28 point perplexity increase, and contrasts this with additive regimes retaining real data. [S1]
- S2 independently identifies recursive synthetic-data training as a cause of model collapse and warns that distributions can narrow until outputs degrade. [S2]

#### Finding 4

**Claim**

Synthetic data can reproduce or amplify errors, artifacts, and biases present in the generator or in the prompting and filtering process; targeted augmentation may also distort the training distribution.

**Confidence:** Low

**Why this confidence level**

The sources support a general bias and distribution-risk mechanism, but they provide no direct subgroup-bias measurements, causal comparisons, or evidence about which generation methods reduce or worsen specific biases.

**Evidence**

- S4 presents synthetic data as reflecting the source model’s learned patterns and says its quality depends on alignment with the target distribution and validation. [S4]
- S5 notes that synthetic data may lack new information and can cause stagnation or degradation when repeatedly generated by models without external feedback; it also emphasizes that biased and low-quality source data affect model risks. [S5]
- S1 says that different synthetic-data use cases have different failure modes, including distribution drift, and emphasizes curation and quality filtering. [S1]

#### Finding 5

**Claim**

Evaluation is a major risk area: synthetic examples can make tests easier to optimize against, fail to represent real-world variation, or produce misleading benchmark gains; evaluation should include independent, real-world, contamination-resistant and safety-oriented tests.

**Confidence:** Medium

**Why this confidence level**

The evaluation concerns are mutually consistent and directly relevant, but the sources do not provide a validated protocol or quantitative evidence comparing synthetic and human-built evaluation sets.

**Evidence**

- S1 explicitly lists eval-set creation as a distinct use case with a risk of evaluation overfitting. [S1]
- S5 warns that benchmark scores may be misleading because of saturation, contamination, leakage, and weak correspondence to complex real-world behavior. It calls for evaluation covering reliability, robustness, fairness, reproducibility, safety, agentic tasks, and realistic application settings. [S5]
- S4 says synthetic test cases can probe edge cases, adversarial examples, ambiguity, multi-turn context, confidence calibration, and robustness, but also states that validation is critical. [S4]

#### Finding 6

**Claim**

Privacy substitution is not automatically privacy protection: synthetic records require disclosure, re-identification, memorization, and linkage testing before they can be treated as safer than the original data.

**Confidence:** Medium

**Why this confidence level**

The need for governance and testing is supported, but the retrieved sources do not quantify privacy leakage or compare formal privacy mechanisms.

**Evidence**

- S4 describes synthetic data as potentially useful for privacy-preserving sharing but frames the benefit as preserving statistical properties while removing direct links, without presenting a formal privacy guarantee. [S4]
- S1 notes that plausible re-identification remains relevant to privacy and compliance decisions and treats privacy substitution as a separate use case with its own risk profile. [S1]
- S2 says ungoverned synthetic data creates audit gaps and that lineage and fidelity metadata are necessary. [S2]

### Conflicts Found

- S1 presents additive synthetic-data training as having bounded or low collapse risk, while S1 and S2 also describe recursive or replacement training as capable of severe degradation. This is a conditional difference by training regime, not a direct contradiction. [S1] [S2]
- S4 uses broad language that synthetic data can “supplement or even replace” human-labeled data, whereas S1’s stronger evidence and recommendation favor retaining and accumulating real data rather than replacing it. The sources differ in how broadly they state the replacement benefit. [S1] [S4]
- S1 reports precise performance and dataset claims for Phi-1 and Cosmopedia, but the retrieved source labels some results vendor-stated and does not provide the primary-study details; these claims should not be treated as independently verified evidence. [S1]

### Important Gaps

- How do synthetic-data mixtures affect subgroup fairness and bias on specific LLM tasks, compared with real-data baselines?
- Which quality controls—human review, model-based filtering, deduplication, provenance tracking, or verifier-based generation—most reliably prevent factual errors, label errors, mode collapse, and distribution drift?
- What is the measured effect of synthetic fine-tuning on out-of-distribution performance, rare-event recall, calibration, hallucination, and safety?
- How often do synthetic evaluation sets correlate with independent human-authored or real-world evaluations, and how vulnerable are they to generator/model contamination?
- What privacy guarantees and empirical re-identification or memorization tests are required for synthetic data generated from confidential records?
- Are the reported Phi-1, OPT-125m, Cosmopedia, and collapse results applicable to current LLM architectures, fine-tuning regimes, and data mixtures?

**Analysis Duration:** 18.36s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The central qualitative picture is clear—synthetic data offers useful scarcity, privacy, and coverage benefits, but can degrade quality, amplify bias, and produce misleading evaluations. However, the original question specifically asks about real-world risks and benefits focused on data quality, bias, and evaluation. The current evidence is mostly vendor or industry commentary, gives little direct quantitative fairness evidence, and lacks primary studies comparing synthetic and real data or validating synthetic evaluation sets.

**Next Search**

> peer-reviewed study synthetic data LLM fine-tuning bias fairness evaluation real data benchmark contamination

---

# Iteration 2

## 1. Search

**Query**

> peer-reviewed study synthetic data LLM fine-tuning bias fairness evaluation real data benchmark contamination

**Why this query**

The central qualitative picture is clear—synthetic data offers useful scarcity, privacy, and coverage benefits, but can degrade quality, amplify bias, and produce misleading evaluations. However, the original question specifically asks about real-world risks and benefits focused on data quality, bias, and evaluation. The current evidence is mostly vendor or industry commentary, gives little direct quantitative fairness evidence, and lacks primary studies comparing synthetic and real data or validating synthetic evaluation sets.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S6 — [2605.19999] LLM Benchmark Datasets Should Be Contamination-Resistant**
  URL: https://arxiv.org/abs/2605.19999
- **S7 — LLMSS 2026 — LLM & Social Sciences Conference**
  URL: https://eps-academic.org/ai-conference
- **S8 — Study with us**
  URL: https://www.griffith.edu.au/research/institute-biomedicine-glycomics/study
- **S9 — TMLE Papers - Sky Qiu**
  URL: https://sky-stats.com/tmle-papers.html
- **S10 — [2409.11968] Efficacy of Synthetic Data as a Benchmark**
  URL: https://arxiv.org/abs/2409.11968

**Search Duration:** 3.88s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The newly retrieved material does not add reliable substantive evidence about synthetic data for LLM training, fine-tuning, bias, data quality, or evaluation.

**Confidence:** High

**Why this confidence level**

The retrieved content is either plainly unrelated or lacks substantive study content.

**Evidence**

- S6 and S10 provide bibliographic pages and titles but no abstract, methods, results, or conclusions from which their claims can be assessed. [S6] [S10]
- S7 is a conference announcement that lists synthetic-data generation, bias mitigation, and evaluation as conference themes, but it reports no empirical findings. [S7]
- S8 concerns biomedical research training and scholarships, and S9 is a list of targeted-learning-estimation papers; neither addresses synthetic data for LLMs. [S8] [S9]

#### Finding 2

**Claim**

The evidence base remains stronger for general evaluation risks than for quantitative comparisons of synthetic and human-authored evaluation data.

**Confidence:** Medium

**Why this confidence level**

The prior evaluation evidence is consistent but largely advisory, while the potentially most relevant new studies are unavailable beyond metadata.

**Evidence**

- Prior findings identify evaluation overfitting, contamination, leakage, weak real-world correspondence, and the need for independent and realistic tests. [S1] [S4] [S5]
- S6's title indicates relevance to contamination-resistant benchmarks, but the retrieved page contains no substantive evidence that could refine or verify that implication. [S6]
- S10's title indicates a direct study of synthetic benchmarks, but its retrieved page likewise contains no abstract or results. [S10]

### Conflicts Found

No meaningful conflicts were identified in this iteration.

### Important Gaps

- What does the study titled “Efficacy of Synthetic Data as a Benchmark” find about correlation with real or human-authored evaluations, failure modes, and contamination?
- Does “LLM Benchmark Datasets Should Be Contamination-Resistant” provide concrete protocols or empirical evidence relevant to synthetic evaluation-set contamination?
- How do synthetic-data mixtures affect subgroup fairness, out-of-distribution performance, calibration, hallucination, and safety relative to real-data baselines?
- Which generation, filtering, deduplication, provenance, and human-verification controls most reliably improve synthetic-data quality?

**Analysis Duration:** 7.53s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources are mostly irrelevant or truncated. A focused retrieval of the abstract or full text for the directly relevant synthetic-benchmark study would materially improve the answer's evaluation section, which remains an important evidence gap.

**Next Search**

> "Efficacy of Synthetic Data as a Benchmark" abstract results synthetic benchmark LLM

---

# Iteration 3

## 1. Search

**Query**

> "Efficacy of Synthetic Data as a Benchmark" abstract results synthetic benchmark LLM

**Why this query**

The new sources are mostly irrelevant or truncated. A focused retrieval of the abstract or full text for the directly relevant synthetic-benchmark study would materially improve the answer's evaluation section, which remains an important evidence gap.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S11 — Efficacy of Synthetic Data as a Benchmark**
  URL: https://arxiv.org/html/2409.11968v1
- **S12 — Unveiling the Potential of Synthetic Text Data: Evaluating LLM-Generated Benchmarks for NLP Tasks - Diabolocom**
  URL: https://www.diabolocom.com/research/synthetic-text-data-evaluating-llm-generated-benchmarks-nlp-tasks
- **S13 — How Good Are Synthetic Requirements ? Evaluating LLM-Generated Datasets for AI4RE**
  URL: https://arxiv.org/html/2506.21138v1
- **S14 — [PDF] Quality Matters: Evaluating Synthetic Data for Tool-Using LLMs**
  URL: https://aclanthology.org/2024.emnlp-main.285.pdf

**Search Duration:** 1.92s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data can be effective for specific tasks, but its usefulness depends strongly on task complexity and domain; it should not be assumed to represent real-world data generally.

**Confidence:** Medium

**Why this confidence level**

The evidence includes a primary empirical preprint and a domain-specific empirical preprint, but generalization beyond the studied tasks and domains remains uncertain.

**Evidence**

- Across six datasets and three NLP tasks, synthetic benchmarks were effective for simpler intent-classification tasks but less representative for complex named-entity-recognition tasks. [S11]
- In requirements classification, synthetic data matched or exceeded human-authored data for selected security and defect-detection tasks, while results varied by prompting, curation, and task. [S13]
- Prior sources similarly describe utility as dependent on generation method, validation, and alignment with the target distribution. [S1] [S4]

#### Finding 2

**Claim**

High-quality validation and filtering can yield better fine-tuning outcomes than simply increasing the volume of unvalidated synthetic data.

**Confidence:** High

**Why this confidence level**

S14 provides direct empirical comparisons across two tool-use benchmarks, and S13 provides convergent task-specific evidence that quality controls have non-uniform effects.

**Evidence**

- In tool-using LLM experiments, models trained on smaller datasets that passed human-defined or model-driven quality checks performed better or comparably to models trained on larger unvalidated datasets. [S14]
- The study found errors in both generated instructions and ground-truth API-call sequences, demonstrating that plausible synthetic examples can contain task-critical mistakes. [S14]
- Requirements-data experiments found that multi-sample prompting improved utility and diversity, while some automated prompt optimization and similarity-based curation had task-dependent or negative effects. [S13]

#### Finding 3

**Claim**

Synthetic data can improve performance when combined with real data or carefully curated, but indiscriminate mixing or replacement can reduce diversity and performance.

**Confidence:** Medium

**Why this confidence level**

The direction of the risk is consistent, but the magnitude and applicability to modern LLM fine-tuning regimes vary by task, mixture, and generation process.

**Evidence**

- The requirements study reports that hybrid real-plus-synthetic training produced large gains on selected classification tasks, but also found lower diversity in synthetic data and degradation when synthetic sources were combined indiscriminately. [S13]
- Prior evidence recommends accumulating synthetic data alongside real data rather than replacing real data, and warns that recursive or replacement training can cause distribution narrowing and model collapse. [S1] [S2]

#### Finding 4

**Claim**

Synthetic evaluation sets can produce misleading conclusions when task complexity is high or when the evaluator and data generator are related models.

**Confidence:** High

**Why this confidence level**

S11 directly evaluates absolute and relative agreement with real benchmarks and introduces a bias-factor measure; the findings are reinforced by the associated research summary and prior evaluation guidance.

**Evidence**

- Synthetic benchmarks tracked real-data performance reasonably for intent detection but were less representative for NER, indicating that benchmark validity is task-dependent. [S11] [S12]
- The same-model bias analysis found that smaller LLMs performed somewhat better on their own generated data, whereas larger models showed little or no significant self-bias. [S11] [S12]
- Averaging data generated by multiple LLMs produced a more robust and representative benchmark than relying on one generator. [S11] [S12]
- Prior sources identify evaluation overfitting, contamination, leakage, and weak correspondence with real-world behavior as risks requiring independent and realistic tests. [S1] [S5]

#### Finding 5

**Claim**

Synthetic data can reduce scarcity, annotation cost, and privacy barriers, while enabling targeted coverage of rare or underrepresented cases, but these benefits are conditional rather than automatic.

**Confidence:** Medium

**Why this confidence level**

The practical benefits are well supported as use cases, but the new empirical evidence is concentrated in requirements engineering and does not establish universal real-world gains.

**Evidence**

- Prior sources identify scarcity, annotation expense, privacy sensitivity, class imbalance, edge cases, prototyping, and domain adaptation as major use cases. [S1] [S4]
- The requirements study frames synthetic generation as a response to small, imbalanced, restricted-access datasets and reports the ability to tailor generated data to task or domain properties. [S13]

#### Finding 6

**Claim**

Synthetic data may reproduce generator-specific bias and distribution artifacts; current evidence is stronger for self-bias and representativeness problems than for subgroup fairness effects.

**Confidence:** Medium

**Why this confidence level**

There is direct evidence for generator self-bias and reduced diversity, but no retrieved controlled measurements of demographic subgroup fairness relative to real-data baselines.

**Evidence**

- Smaller models showed a bias toward data they generated themselves when used as evaluators, while larger models showed less such bias. [S11] [S12]
- Synthetic requirements had lower diversity than real data, and curation choices changed diversity and task performance in different directions. [S13]
- Prior sources warn that synthetic data reflects generator patterns and can reproduce errors, artifacts, and biases in the source model or filtering process. [S1] [S4] [S5]

### Conflicts Found

- S13 reports that synthetic requirements can outperform human-authored data on selected security and defect-classification tasks, while prior findings caution that synthetic data is not a universal replacement and may have lower diversity or cause degradation when mixed indiscriminately. These are conditional differences by task, curation, and training mixture rather than direct contradictions. [S1] [S13]
- S11 finds little self-bias for larger models but some self-preference among smaller models. This qualifies, rather than contradicts, the broader warning that generator–evaluator overlap can bias synthetic benchmarks. [S1] [S11]
- S13 finds similarity-based curation improves diversity but often harms classification performance, showing that a quality metric such as diversity does not necessarily align with downstream utility. [S13]

### Important Gaps

- How do synthetic-data mixtures affect demographic and subgroup fairness compared with matched real-data baselines?
- Which quality-control pipeline—human review, external-model checking, deduplication, provenance tracking, or verifier-based generation—best prevents factual and label errors across different LLM tasks?
- How do synthetic fine-tuning data affect out-of-distribution performance, calibration, hallucination, rare-event recall, and safety?
- How well do synthetic benchmarks correlate with independent human-authored and real-world evaluations for generative, multilingual, safety, and agentic tasks?
- What privacy guarantees and empirical re-identification or memorization tests are needed when synthetic data is generated from confidential records?
- How sensitive are the reported findings to generator size, prompt design, synthetic-to-real ratio, filtering thresholds, and model architecture?
- Whether synthetic data improves or worsens fairness remains especially underdetermined because the retrieved studies measure self-bias, diversity, and task performance rather than protected-group outcomes.

**Analysis Duration:** 15.83s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The runner reached the maximum research iteration budget. Analyzer assessment: The new sources materially strengthen the answer on data quality and evaluation, including direct evidence that validated data can outperform larger unvalidated datasets and that synthetic benchmark validity is task-dependent. However, the original question explicitly includes bias, and there is still no strong quantitative evidence on subgroup fairness or bias relative to real-data training. One focused search on controlled fairness comparisons would materially improve the answer.

**Stop Reason:** max_iterations

---

# Final Research Decision

**Research Stopped Because**

The runner reached the maximum research iteration budget.

**Stop Reason:** max_iterations

**Searches Performed:** 3

**Unique Sources:** 14

**Remaining Uncertainty**

- Controlled comparisons of subgroup and demographic fairness for synthetic-versus-real fine-tuning mixtures.
- Evidence on how synthetic fine-tuning affects out-of-distribution generalization, calibration, hallucination, rare-event recall, and safety.
- Validated cross-domain quality-control pipelines comparing human review, external-model checking, deduplication, provenance tracking, and verifier-based generation.
- More evidence on correlation between synthetic benchmarks and independent human-authored or real-world evaluations, especially for multilingual, generative, safety, and agentic tasks.
- Formal privacy guarantees and empirical re-identification or memorization tests for synthetic data generated from confidential records.
- Sensitivity analyses for generator size, prompt design, synthetic-to-real ratio, filtering thresholds, and model architecture.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 8.51s |
| OpenAI Analysis | 3 | 41.73s |
| Report Generation | 1 | 18.73s |
| Total Run | — | 68.97s |
