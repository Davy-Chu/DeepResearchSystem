# Research Run Log

## Run Summary

**System Version:** evidence-ledger-decomposer-v1

**Research Question**

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

**Status:** Failed

**Stop Reason:** max_iterations

**Failure Stage:** OpenAI Ledger Report Generation

**Error**

Final report finding 7 has no evidence items

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 12

**OpenAI Calls:** 7

**Tavily Calls:** 3

**Started:** 2026-08-31T18:53:05-04:00

**Ended:** 2026-08-31T18:54:27-04:00

**Total Runtime:** 81.84s

---

# Research Plan

## Subquestions

### SQ1 [CORE]

**Question:**

How does using synthetic data to train or fine-tune large language models affect data quality, including factual accuracy, diversity, coverage, consistency, noise, and the risk of recursive or model-induced errors?

**Success criteria:**

Assess documented real-world benefits and risks to training-data quality, distinguishing improvements such as scalable coverage and controlled examples from problems such as hallucinated content, distributional narrowing, duplicated patterns, and error amplification. Identify the conditions under which each outcome occurs.

**Initial status:** UNRESEARCHED

### SQ2 [CORE]

**Question:**

How does synthetic training data affect bias and fairness in large language models, including the introduction, amplification, preservation, or mitigation of demographic, cultural, linguistic, and viewpoint biases?

**Success criteria:**

Compare evidence of bias reduction benefits with evidence of bias propagation or amplification, and specify how the source model, prompting or generation process, filtering, demographic and linguistic coverage, and human oversight influence outcomes.

**Initial status:** UNRESEARCHED

### SQ3 [CORE]

**Question:**

How should large language models trained or fine-tuned with synthetic data be evaluated, and what limitations or risks arise when evaluating them?

**Success criteria:**

Identify evaluation methods and metrics for factuality, generalization, robustness, safety, bias, and downstream task performance; distinguish intrinsic data-quality evaluation from model-level evaluation; and assess risks from benchmark contamination, synthetic-data leakage, evaluator bias, poor proxy metrics, and failure to measure real-world performance.

**Initial status:** UNRESEARCHED

### SQ4 [SECONDARY]

**Question:**

What practical conditions determine whether the benefits of synthetic data outweigh its risks when training or fine-tuning large language models?

**Success criteria:**

Synthesize evidence into actionable conditions concerning synthetic-data generation, provenance and documentation, mixing with human or real-world data, filtering, validation, human review, proportion of synthetic data, domain and task, and ongoing monitoring, while preserving uncertainty where evidence is limited.

**Initial status:** UNRESEARCHED

## Synthesis Requirements

- Distinguish benefits from risks rather than treating synthetic data as uniformly positive or negative.
- Connect data quality, bias, and evaluation: explain how weaknesses in one area can affect the others.
- Preserve the distinction between pretraining and fine-tuning where evidence or impacts differ.
- Focus on real-world consequences and conditions, including uncertainty and variation by domain, task, and synthetic-data generation method.

## Output Requirements

- Answer the question in terms of real-world risks and benefits.
- Focus specifically on data quality, bias, and evaluation.
- Present a balanced assessment rather than an unqualified conclusion.

---

# Iteration 1

## 1. Search

**Query**

> What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

**Purpose:** GENERAL

**Why this query**

This is the user's original research question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S1 — Synthetic Data for LLM Training: Decision Guide 2026**
  URL: https://www.digitalapplied.com/blog/synthetic-data-generation-llm-training-decision-guide-2026
- **S2 — Synthetic Data for AI Training: Use Cases and Risks [2026]**
  URL: https://atlan.com/know/ai-agent/data-for-ai/synthetic-data-for-ai-training
- **S3 — Using Synthetic Data to Improve LLM Fine‑Tuning - Newline**
  URL: https://www.newline.co/@Dipen/using-synthetic-data-to-improve-llm-finetuning--d453f658
- **S4 — Synthetic Data Generation with LLMs: Techniques and Use ...**
  URL: https://tetrate.io/learn/ai/synthetic-data-generation-llms
- **S5 — Large Language Models Are Still Getting Stronger, but ...**
  URL: https://www.newswise.com/articles/large-language-models-are-still-getting-stronger-but-researchers-face-new-bottlenecks-in-data-evaluation-and-safety

**Search Duration:** 2.40s

---

## 2. Evidence Processing

- New claim proposals: 6
- Existing claim updates: 0
- New gaps: 3
- Resolved gaps: 0

**Processing Duration:** 17.55s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

Synthetic data can provide scalable, task-specific training examples when real labeled or domain-specific data is scarce, expensive, privacy-sensitive, or difficult to collect; reported use cases include instruction examples, reasoning traces, code, class-imbalance augmentation, edge cases, and domain adaptation.

- S1 supports (direct): Describes synthetic fine-tuning data, edge-case augmentation, and privacy substitution as responses to data scarcity, annotation cost, and privacy constraints.
- S4 supports (direct): Lists training augmentation, minority-class generation, privacy-sensitive data sharing, rapid prototyping, evaluation cases, and domain adaptation as practical uses.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C2

**Claim**

Synthetic data may improve downstream performance when it is curated, quality-filtered, deduplicated, and used alongside real data rather than indiscriminately replacing it; the supplied examples report strong coding-benchmark results for Phi-1 trained with curated synthetic textbooks and exercises plus real web data.

- S1 supports (indirect): States that additive use of synthetic data with retained real data has a bounded-error rationale and emphasizes deduplication and quality filtering.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C3

**Claim**

Replacing real training data with recursively generated synthetic data can cause model collapse: distribution tails and diversity are lost, errors compound across generations, and model quality may degrade substantially.

- S1 supports (direct): Reports OPT-125m experiments in which five epochs of purely synthetic self-training increased perplexity by 20–28 points when no real data was retained.
- S2 supports (direct): States that recursive synthetic training narrows distributions until outputs degrade.
- S5 supports (direct): Warns that repeated training on model-generated content without new information or external feedback can stagnate or degrade capabilities.
- S1 contradicts (direct): Reports analytical and applied evidence that collapse risk can be mitigated when synthetic data accumulates alongside real data, rather than replacing it.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C4

**Claim**

Synthetic-data quality depends on generation and curation choices: uncontrolled generation can introduce hallucinations, noise, duplication, limited novelty, and distributional narrowing, whereas prompting for varied audiences or formats, validation, filtering, and deduplication can improve coverage and consistency.

- S1 supports (direct): Contrasts volume without curation, which amplifies failure modes, with curated textbook-quality data; reports less than 1% duplicate content in the described Cosmopedia dataset after varying audience and format.
- S4 supports (direct): States that utility depends on generation technique, validation, and alignment with target-distribution requirements, and that LLM generation can create varied contextual examples.
- S5 supports (direct): Identifies low-quality, duplicated, noisy, biased, and insufficiently novel data as development bottlenecks and says synthetic data must be reliable, verifiable, and sustainable.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C5

**Claim**

Synthetic data can mitigate some representation and class-imbalance problems by deliberately generating examples for underrepresented classes or scenarios, but it can also preserve or reproduce biases inherited from the generating model and source distribution.

- S4 supports (direct): Describes targeted generation for underrepresented classes and rare edge cases as a way to address imbalance, while defining synthetic data as mimicking real-world patterns and distributions.
- S5 supports (indirect): Identifies biased information as a risk in training data and emphasizes fairness as an evaluation concern for LLMs.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C6

**Claim**

Benchmark scores alone are insufficient to establish that a model trained or fine-tuned with synthetic data is reliable in deployment; evaluation should include contamination and leakage checks, realistic downstream tasks, factuality, robustness, safety, fairness, and reproducibility.

- S5 supports (direct): States that standard benchmarks may be saturated or contaminated, can fail to distinguish models, and may not predict complex real-world reliability; it calls for realistic evaluation addressing contamination, fairness, reproducibility, and safety.
- S4 supports (direct): Describes synthetic edge-case, adversarial, ambiguity, multi-turn, boundary, calibration, and robustness test generation as evaluation uses.
- S1 supports (indirect): Warns that synthetic evaluation sets have distinct risks, including distribution drift and evaluation overfitting, and treats evaluation as a separate use case from training.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Gap G1

The supplied sources do not provide controlled, quantitative evidence on how synthetic training affects demographic, cultural, linguistic, or viewpoint fairness, nor how source-model choice, prompting, filtering, and human review change those outcomes.

### New Gap G2

The supplied evidence does not establish validated methods or comparative results for measuring factuality, synthetic-data quality, generalization, robustness, safety, and downstream performance while avoiding synthetic-data contamination or evaluator bias.

### New Gap G3

The evidence is insufficient to determine broadly applicable thresholds for the proportion of synthetic data, or when additive mixing, filtering, deduplication, external verification, and human review reliably outweigh risks across pretraining versus fine-tuning and across domains.

---

## 4. Current Research State

- Claims: 6
- Supported: 6
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 3
- Remaining Searches: 2

### Subquestion Progress

**SQ1:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ3:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ4:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → PARTIAL (targeted searches: 0)
- SQ3 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- SQ4 → PARTIAL (targeted searches: 0)

**Remaining targeted searches:** 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ2

**Why**

SQ2 remains a CORE subquestion with a high-priority open gap: the current evidence supports only general claims about imbalance mitigation and inherited bias, without controlled quantitative findings on demographic, cultural, linguistic, or viewpoint fairness or the effects of generation, filtering, and human review.

**Next Search**

> controlled empirical studies synthetic data LLM training demographic cultural linguistic viewpoint bias fairness source model prompting filtering human review quantitative results


---

# Iteration 2

## 1. Search

**Query**

> controlled empirical studies synthetic data LLM training demographic cultural linguistic viewpoint bias fairness source model prompting filtering human review quantitative results

**Target:** SQ2

**Purpose:** SUBQUESTION

**Why this query**

SQ2 remains a CORE subquestion with a high-priority open gap: the current evidence supports only general claims about imbalance mitigation and inherited bias, without controlled quantitative findings on demographic, cultural, linguistic, or viewpoint fairness or the effects of generation, filtering, and human review.

5 result(s) retrieved; 3 new unique source(s) added.

- **S6 — Fairness in AI Decisions About People: Evidence from LLM Experiments**
  URL: https://manhattan.institute/article/fairness-in-ai-decisions-about-people-evidence-from-llm-experiments
- **S7 — Data bias in LLM and generative AI applications**
  URL: https://mostly.ai/blog/data-bias-types
- **S8 — Bias in Large Language Models: Origin, Evaluation, and Mitigation**
  URL: https://arxiv.org/html/2411.10915v1

**Search Duration:** 2.80s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 3
- New gaps: 2
- Resolved gaps: 0

**Processing Duration:** 11.48s

---

## 3. Ledger Updates

### Updated Claim C3

**Claim**

Replacing real training data with recursively generated synthetic data can cause model collapse: distribution tails and diversity are lost, errors compound across generations, and model quality may degrade substantially.

- S7 supports (indirect): Describes a negative recursive loop in which training generative models on generated data can reduce output quality, consistent with degradation from repeated model-generated data.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

Synthetic data can mitigate some representation and class-imbalance problems by deliberately generating examples for underrepresented classes or scenarios, but it can also preserve or reproduce biases inherited from the generating model and source distribution.

- S7 supports (direct): States that selection and coverage bias can arise when populations or linguistic patterns are underrepresented, and presents synthetic-data rebalancing and conditional generation as possible mitigation strategies when categories or records are missing.
- S8 supports (direct): Reviews demographic, cultural, racial, gender, socioeconomic, and linguistic bias in LLMs, identifying nonrepresentative training data as a source and discussing resampling, augmentation, fairness constraints, and post-processing as mitigation approaches.
- S6 supports (indirect): Reports that demographic cues influenced LLM pairwise decisions and that masking explicit demographic information reduced some disparities, while prompt candidate order produced systematic selection effects; this illustrates that bias can persist through implicit cues and task structure even when explicit attributes are removed.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C6

**Claim**

Benchmark scores alone are insufficient to establish that a model trained or fine-tuned with synthetic data is reliable in deployment; evaluation should include contamination and leakage checks, realistic downstream tasks, factuality, robustness, safety, fairness, and reproducibility.

- S6 supports (direct): Provides experimental evidence that LLM decisions vary with gender and ethnicity cues and with candidate order, and recommends masking demographic information plus monitoring group-level outcomes in high-stakes settings.
- S8 supports (direct): Reviews data-level, model-level, and output-level bias evaluation methods and mitigation strategies, supporting evaluation across multiple layers rather than reliance on a single benchmark.
- S7 supports (indirect): Identifies selection, automation, temporal, implicit, and social bias, and recommends human supervision for mission-critical applications; it also links generated-data recursion to quality degradation.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### New Gap G4

The new sources broaden evidence about general LLM bias and bias evaluation, but do not isolate the causal effect of synthetic-data generation, filtering, or mixing on demographic, cultural, linguistic, or viewpoint fairness in models trained or fine-tuned with synthetic data.

### New Gap G5

The new sources identify evaluation dimensions and mitigation techniques, but do not provide comparative validation of synthetic-data-specific evaluation protocols against independent real-world outcomes, including factuality, generalization, robustness, safety, contamination, and evaluator bias.

---

## 4. Current Research State

- Claims: 6
- Supported: 6
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 5
- Remaining Searches: 1

### Subquestion Progress

**SQ1:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ3:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ4:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → PARTIAL (targeted searches: 1)
- SQ3 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- SQ4 → PARTIAL (targeted searches: 0)

**Remaining targeted searches:** 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ3

**Why**

A final search is warranted for SQ3: evaluation remains a high-importance unresolved core subquestion, with no targeted attempt yet. Evidence currently lists evaluation dimensions but lacks validated, synthetic-data-specific methods and comparative evidence on contamination, factuality, generalization, robustness, safety, fairness, and real-world performance.

**Next Search**

> empirical studies evaluating LLMs trained or fine-tuned with synthetic data: factuality, generalization, robustness, safety, fairness, benchmark contamination, synthetic-data leakage, evaluator bias, and correlation with real-world performance


---

# Iteration 3

## 1. Search

**Query**

> empirical studies evaluating LLMs trained or fine-tuned with synthetic data: factuality, generalization, robustness, safety, fairness, benchmark contamination, synthetic-data leakage, evaluator bias, and correlation with real-world performance

**Target:** SQ3

**Purpose:** SUBQUESTION

**Why this query**

A final search is warranted for SQ3: evaluation remains a high-importance unresolved core subquestion, with no targeted attempt yet. Evidence currently lists evaluation dimensions but lacks validated, synthetic-data-specific methods and comparative evidence on contamination, factuality, generalization, robustness, safety, fairness, and real-world performance.

5 result(s) retrieved; 4 new unique source(s) added.

- **S9 — LLM Evaluation: Benchmarks to Test Model Quality in 2026 | Label Your Data**
  URL: https://labelyourdata.com/articles/llm-fine-tuning/llm-evaluation
- **S10 — Quality Matters: Evaluating Synthetic Data for Tool-Using LLMs**
  URL: https://arxiv.org/html/2409.16341v2
- **S11 — Assessment of fine-tuned large language models for real-world chemistry and material science applications†**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11629507
- **S12 — Quality Matters: Evaluating Synthetic Data for Tool-Using LLMs | Abdullah Mamun**
  URL: https://abdullah-mamun.com/talk/quality-matters-evaluating-synthetic-data-for-tool-using-llms

**Search Duration:** 2.63s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 3
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 13.05s

---

## 3. Ledger Updates

### New Claim C7

**Claim**

For synthetic data used to train tool-using LLMs, intrinsic quality assessment—using human-defined correctness criteria and automated or model-driven checks such as in-context evaluation—can identify errors in instructions and API-call traces, filter low-quality instances, and improve downstream performance; in the reported ToolBench and ToolAlpaca experiments, smaller high-quality datasets performed better or comparably to larger unverified datasets.

- S10 supports (direct): Directly reports errors in synthetic instructions and ground-truth API calls, proposes human-defined intrinsic criteria and model-driven In-Context Evaluation, and finds that filtered high-quality data yields better or comparable performance on two tool-use benchmarks despite smaller quantity.
- S12 supports (direct): Independently presents the same study's finding that models trained on high-quality synthetic data outperform models trained on unvalidated data, even with less data.

**Confidence:** HIGH

**Status:** SUPPORTED

### Updated Claim C2

**Claim**

Synthetic data may improve downstream performance when it is curated, quality-filtered, deduplicated, and used alongside real data rather than indiscriminately replacing it; the supplied examples report strong coding-benchmark results for Phi-1 trained with curated synthetic textbooks and exercises plus real web data.

- S10 supports (direct): Reports that high-quality, validated synthetic training data produced better or comparable tool-use performance than larger unverified datasets, supporting the benefit of curation and validation over indiscriminate volume.
- S12 supports (direct): Corroborates that high-quality synthetic data outperformed unvalidated data even when smaller.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

Synthetic-data quality depends on generation and curation choices: uncontrolled generation can introduce hallucinations, noise, duplication, limited novelty, and distributional narrowing, whereas prompting for varied audiences or formats, validation, filtering, and deduplication can improve coverage and consistency.

- S10 supports (direct): Finds numerous errors in LLM-generated tool-use instructions and API-call sequences and shows that intrinsic quality checks can be used to filter unreliable instances.
- S12 supports (direct): Summarizes the reported quality-assessment and filtering approach for synthetic tool-use data.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C6

**Claim**

Benchmark scores alone are insufficient to establish that a model trained or fine-tuned with synthetic data is reliable in deployment; evaluation should include contamination and leakage checks, realistic downstream tasks, factuality, robustness, safety, fairness, and reproducibility.

- S9 supports (direct): States that evaluation should be use-case-specific and multidimensional, combining quantitative metrics with human judgments, and that continuous production monitoring is needed because static benchmarks may miss performance drift; it also identifies contamination and evaluation subjectivity as challenges.
- S10 supports (direct): Distinguishes intrinsic evaluation of synthetic training data from extrinsic model evaluation and demonstrates that data-quality assessment changes the interpretation of downstream model results.
- S12 supports (direct): Corroborates the distinction between assessing synthetic-data reliability and measuring final model performance.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 7
- Supported: 7
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 5
- Remaining Searches: 0

### Subquestion Progress

**SQ1:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ3:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ4:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → PARTIAL (targeted searches: 1)
- SQ3 → PARTIAL (targeted searches: 1)

**SECONDARY:**

- SQ4 → PARTIAL (targeted searches: 0)

**Remaining targeted searches:** 0

---

## 5. Research Decision

**Decision:** Stop researching.

**Origin:** BUDGET_STOP

**Why**

The maximum research iteration budget was reached.

**Stop Reason:** max_iterations


---

# Final Research Decision

**Research did not complete.**

**Failure Stage:** OpenAI Ledger Report Generation

**Remaining Uncertainty**

- The supplied sources do not provide controlled, quantitative evidence on how synthetic training affects demographic, cultural, linguistic, or viewpoint fairness, nor how source-model choice, prompting, filtering, and human review change those outcomes.
- The supplied evidence does not establish validated methods or comparative results for measuring factuality, synthetic-data quality, generalization, robustness, safety, and downstream performance while avoiding synthetic-data contamination or evaluator bias.
- The evidence is insufficient to determine broadly applicable thresholds for the proportion of synthetic data, or when additive mixing, filtering, deduplication, external verification, and human review reliably outweigh risks across pretraining versus fine-tuning and across domains.
- The new sources broaden evidence about general LLM bias and bias evaluation, but do not isolate the causal effect of synthetic-data generation, filtering, or mixing on demographic, cultural, linguistic, or viewpoint fairness in models trained or fine-tuned with synthetic data.
- The new sources identify evaluation dimensions and mitigation techniques, but do not provide comparative validation of synthetic-data-specific evaluation protocols against independent real-world outcomes, including factuality, generalization, robustness, safety, contamination, and evaluator bias.
- SQ1: How does using synthetic data to train or fine-tune large language models affect data quality, including factual accuracy, diversity, coverage, consistency, noise, and the risk of recursive or model-induced errors? (PARTIAL: Open high- or medium-importance research gaps still block a sufficient answer.)
- SQ2: How does synthetic training data affect bias and fairness in large language models, including the introduction, amplification, preservation, or mitigation of demographic, cultural, linguistic, and viewpoint biases? (PARTIAL: Open high- or medium-importance research gaps still block a sufficient answer.)
- SQ3: How should large language models trained or fine-tuned with synthetic data be evaluated, and what limitations or risks arise when evaluating them? (PARTIAL: Open high- or medium-importance research gaps still block a sufficient answer.)
- SQ4: What practical conditions determine whether the benefits of synthetic data outweigh its risks when training or fine-tuning large language models? (PARTIAL: Open high- or medium-importance research gaps still block a sufficient answer.)

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Question Decomposition | 1 | 7.41s |
| Tavily Search | 3 | 7.83s |
| Evidence Processing | 3 | 42.09s |
| Research Decision | 2 | 5.21s |
| Report Generation | 1 | 0.00s |
| Total Run | — | 81.84s |
