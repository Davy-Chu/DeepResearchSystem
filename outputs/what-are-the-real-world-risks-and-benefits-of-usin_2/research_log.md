# Research Run Log

## Run Summary

**System Version:** evidence-ledger-v1

**Research Question**

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 13

**OpenAI Calls:** 6

**Tavily Calls:** 3

**Started:** 2026-08-30T18:01:36-04:00

**Ended:** 2026-08-30T18:03:09-04:00

**Total Runtime:** 93.69s

---

# Iteration 1

## 1. Search

**Query**

> What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

**Why this query**

This is the user's original research question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S1 — Using Synthetic Data to Improve LLM Fine‑Tuning | newline**
  URL: https://www.newline.co/@Dipen/using-synthetic-data-to-improve-llm-finetuning--d453f658
- **S2 — Synthetic Data for AI Training: Use Cases and Risks [2026]**
  URL: https://atlan.com/know/ai-agent/data-for-ai/synthetic-data-for-ai-training
- **S3 — Large Language Models Are Still Getting Stronger, but Researchers Face New Bottlenecks in Data, Evaluation, and Safety | Newswise**
  URL: https://www.newswise.com/articles/large-language-models-are-still-getting-stronger-but-researchers-face-new-bottlenecks-in-data-evaluation-and-safety
- **S4 — Synthetic Data Generation with LLMs: Techniques and Use Cases**
  URL: https://tetrate.io/learn/ai/synthetic-data-generation-llms
- **S5 — Synthetic Data for ML: Uses, Risks, and Best Practices | CleverX Blog**
  URL: https://cleverx.com/blog/synthetic-data-for-ml-the-game-changer-in-training-for-2025

**Search Duration:** 2.91s

---

## 2. Evidence Processing

- New claim proposals: 8
- Existing claim updates: 0
- New gaps: 5
- Resolved gaps: 0

**Processing Duration:** 21.06s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

Synthetic data can supplement LLM training or fine-tuning when real-world data is scarce, expensive to label, privacy-sensitive, or difficult to collect, enabling faster dataset creation and prototyping.

- S4 supports (direct): States that LLM-generated data can address scarcity, privacy-sensitive domains, expensive collection, and limited labeled data; also describes rapid prototyping before real data is available.
- S5 supports (direct): Reports that real-world data is often scarce, expensive to label, and risky to share, and characterizes synthetic data as a scalable and lower-cost alternative.
- S3 supports (direct): Describes high-quality training data as a bottleneck and says synthetic data may help fill part of the gap by expanding training resources.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C2

**Claim**

Targeted synthetic examples can increase representation of underrepresented classes or rare and edge-case scenarios, potentially improving coverage and robustness.

- S4 supports (direct): Describes generating examples for underrepresented classes, rare cases, decision boundaries, adversarial cases, and diverse task contexts.
- S5 supports (direct): Reports use of synthetic data for rare autonomous-vehicle scenarios, uncommon actions, and class-imbalance problems.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C3

**Claim**

Synthetic data can reproduce or amplify biases present in its generator or design, and may still underrepresent demographics, harming fairness and generalizability.

- S5 supports (direct): Explicitly warns that poorly designed generators can reproduce or exaggerate existing biases and underrepresent demographics.
- S3 supports (indirect): Identifies biased information and data-mixture design as factors affecting model performance and deployment risk.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C4

**Claim**

Synthetic examples may lack realism or subtle real-world patterns, so models trained on them may generalize poorly outside the synthetic distribution.

- S5 supports (direct): Warns that synthetic examples may miss subtle patterns and recommends comparison with trusted real-world datasets.
- S4 supports (direct): States that synthetic-data utility depends on validation and alignment between the synthetic distribution and target application requirements.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C5

**Claim**

Repeated recursive training on model-generated data without sufficient novel information or external feedback can narrow the data distribution and cause model collapse or capability degradation.

- S2 supports (direct): States that recursive training on synthetic data causes model collapse, with distributions narrowing until outputs degrade.
- S3 supports (direct): Warns that repeated training on other models’ outputs without new information or reliable external feedback can cause stagnation or degradation.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C6

**Claim**

Synthetic data quality requires validation for accuracy or distributional fidelity, diversity, realism, and coverage, using automated/statistical checks together with human evaluation where appropriate.

- S5 supports (direct): Lists accuracy, diversity, and realism as evaluation metrics and recommends visualization, statistical analysis, and human evaluation.
- S4 supports (direct): Emphasizes that generation techniques and validation methods determine synthetic-data quality and utility.
- S3 supports (indirect): Highlights the need for reliable, verifiable, novel data and stronger evaluation beyond simple benchmark scores.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C7

**Claim**

Models trained or fine-tuned with synthetic data should be evaluated on trusted, real-world or otherwise independently grounded data and realistic tasks, because benchmark scores can be contaminated, saturated, or insufficiently representative.

- S5 supports (direct): States that synthetic-trained models still need benchmarking against trusted real-world datasets and comparison with ground truth.
- S3 supports (direct): Reports benchmark saturation and contamination/leakage concerns, and argues for evaluation in realistic settings rather than relying only on static tests.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C8

**Claim**

Synthetic data can create privacy-related benefits by enabling data sharing or training without directly exposing actual records, but the supplied evidence does not establish that LLM-generated synthetic data is automatically private or disclosure-proof.

- S4 supports (direct): Describes synthetic medical and financial records as preserving patterns while removing direct links to individual records, enabling privacy-sensitive development.
- S5 supports (indirect): Identifies privacy and compliance constraints as reasons organizations use synthetic data.

**Confidence:** MEDIUM

**Status:** WEAK

### New Gap G1

The supplied sources do not provide controlled, LLM-specific measurements comparing synthetic-only, real-only, and mixed-data fine-tuning across quality, bias, and downstream generalization.

### New Gap G2

The sources do not specify reliable procedures for detecting privacy leakage or memorization in LLM-generated synthetic training data.

### New Gap G3

The conditions under which synthetic data improves or worsens demographic fairness, including subgroup-specific evaluation results, remain unresolved.

### New Gap G4

The evidence does not establish how much synthetic data can be used before recursive-training degradation or model collapse becomes likely.

### New Gap G5

The sources do not identify a standardized evaluation protocol for synthetic-data fidelity, novelty, contamination, and real-world LLM performance.

---

## 4. Current Research State

- Claims: 8
- Supported: 7
- Weak: 1
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 5
- Remaining Searches: 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Target:** GAP G1

**Why**

Controlled LLM-specific comparisons are the highest-value gap for judging whether synthetic data improves quality, bias, and generalization versus real or mixed data.

**Next Search**

> LLM fine-tuning synthetic data versus real data mixed data controlled study quality bias generalization evaluation


---

# Iteration 2

## 1. Search

**Query**

> LLM fine-tuning synthetic data versus real data mixed data controlled study quality bias generalization evaluation

**Why this query**

Controlled LLM-specific comparisons are the highest-value gap for judging whether synthetic data improves quality, bias, and generalization versus real or mixed data.

5 result(s) retrieved; 4 new unique source(s) added.

- **S6 — Synthetic Data for LLM Fine-Tuning 2026**
  URL: https://futureagi.com/blog/synthetic-data-fine-tuning-llms
- **S7 — Synthetic Data for LLM Training: Decision Guide 2026**
  URL: https://www.digitalapplied.com/blog/synthetic-data-generation-llm-training-decision-guide-2026
- **S8 — LLM synthetic data: Fine-tuning LLMs with AI-generated data | SuperAnnotate**
  URL: https://www.superannotate.com/blog/llm-synthetic-data
- **S9 — Hybrid Training Approaches for LLMs: Leveraging Real and Synthetic Data to Enhance Model Performance in Domain-Specific Applications**
  URL: https://arxiv.org/html/2410.09168v1

**Search Duration:** 2.40s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 8
- New gaps: 1
- Resolved gaps: 0

**Processing Duration:** 22.49s

---

## 3. Ledger Updates

### New Claim C9

**Claim**

In at least one domain-specific fine-tuning study, combining real and synthetic conversational data produced better reported performance and adaptability than real-only training or a base-model comparison, but the result is limited to the study’s vertical application and evaluation setup.

- S9 supports (direct): Reports an experiment comparing a base model, a real-data fine-tuned model, and a hybrid model using real counseling interactions plus synthetic sessions; the hybrid model achieved the highest scores across the reported metrics and showed stronger adaptability in additional testing.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

Synthetic data can supplement LLM training or fine-tuning when real-world data is scarce, expensive to label, privacy-sensitive, or difficult to collect, enabling faster dataset creation and prototyping.

- S6 supports (direct): Describes synthetic rows as a way to scale task-specific fine-tuning data from a small human-written seed, particularly for SFT, preference optimization, tool use, and RAG tasks.
- S8 supports (direct): States that synthetic data can be generated rapidly and at large scale to reduce the time, cost, and labor of collecting training examples.
- S9 supports (direct): Uses synthetic personas and scenarios to supplement scarce, noisy, domain-specific real interactions in a fine-tuning dataset.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

Targeted synthetic examples can increase representation of underrepresented classes or rare and edge-case scenarios, potentially improving coverage and robustness.

- S6 supports (direct): Describes deliberately generating diverse instructions, safety prompts, function-calling traces, and RAG examples tailored to specific fine-tuning targets.
- S9 supports (direct): Reports using synthetic personas and scenarios to enrich diversity and address uncommon domain-specific interactions; the hybrid model showed improved adaptability in the reported study.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C3

**Claim**

Synthetic data can reproduce or amplify biases present in its generator or design, and may still underrepresent demographics, harming fairness and generalizability.

- S6 supports (direct): Warns that students trained purely on one teacher’s synthetic data may inherit that teacher’s formatting, refusal style, and length-distribution biases.
- S8 supports (direct): States that biases in the human data used to generate synthetic data can be magnified and that synthetic generation may introduce fairness issues through a less transparent process.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

Synthetic examples may lack realism or subtle real-world patterns, so models trained on them may generalize poorly outside the synthetic distribution.

- S6 supports (direct): Identifies mode collapse, teacher-style imitation, and over-specialization to generated formats as trade-offs requiring real-data seeds, multiple teachers, and diversity checks.
- S8 supports (direct): Warns that synthetic data may fail to mirror real-world complexity, can cause poor practical performance, and may lead to overfitting to synthetic scenarios.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

Repeated recursive training on model-generated data without sufficient novel information or external feedback can narrow the data distribution and cause model collapse or capability degradation.

- S7 supports (direct): Reports that purely synthetic self-training can substantially worsen perplexity, while cited analyses and examples indicate lower risk when synthetic data is accumulated alongside retained real data and quality filtered.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C6

**Claim**

Synthetic data quality requires validation for accuracy or distributional fidelity, diversity, realism, and coverage, using automated/statistical checks together with human evaluation where appropriate.

- S6 supports (direct): Describes filtering generated rows with judge-model rubrics and checking faithfulness, instruction adherence, and diversity before training.
- S8 supports (direct): Recommends human data and model-in-the-loop feedback to identify errors, correct bias, and keep synthetic data relevant and realistic.
- S7 supports (direct): Emphasizes curation, deduplication, quality filtering, and diversity checks rather than relying on synthetic volume alone.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C7

**Claim**

Models trained or fine-tuned with synthetic data should be evaluated on trusted, real-world or otherwise independently grounded data and realistic tasks, because benchmark scores can be contaminated, saturated, or insufficiently representative.

- S6 supports (direct): Recommends faithfulness and instruction-adherence checks and describes evaluation aligned with the particular fine-tuning recipe.
- S7 supports (direct): Distinguishes synthetic training, synthetic evaluation, edge-case augmentation, and privacy substitution as separate use cases with different metrics and failure modes; it also reports benchmark limitations and contamination concerns.
- S9 supports (direct): Compares multiple training conditions and performs additional testing for adaptability and contextual understanding in the target domain.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C8

**Claim**

Synthetic data can create privacy-related benefits by enabling data sharing or training without directly exposing actual records, but the supplied evidence does not establish that LLM-generated synthetic data is automatically private or disclosure-proof.

- S6 supports (direct): Describes a use case in which real customer-support tickets were blocked by privacy constraints and synthetic data was used instead, with a small real seed anchoring generation.
- S8 supports (direct): Presents synthetic data as potentially avoiding direct use of personal information and reducing privacy concerns in sensitive domains.
- S7 contradicts (direct): Warns that privacy substitution can still involve re-identification and GDPR-related risk when plausible, so synthetic data is not automatically free of privacy obligations.

**Confidence:** MEDIUM → MEDIUM

**Status:** WEAK → WEAK

### New Gap G6

The reported benefit of hybrid real-plus-synthetic fine-tuning has limited external validity: the supplied evidence does not show whether it replicates across domains, model sizes, task types, or against synthetic-only baselines.

---

## 4. Current Research State

- Claims: 9
- Supported: 8
- Weak: 1
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 6
- Remaining Searches: 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Target:** GAP G1

**Why**

A controlled LLM-specific comparison of synthetic-only, real-only, and mixed-data fine-tuning would most directly strengthen the answer’s central claims about quality, bias, and generalization.

**Next Search**

> controlled study LLM fine-tuning synthetic-only real-only mixed data comparison data quality bias fairness downstream generalization evaluation


---

# Iteration 3

## 1. Search

**Query**

> controlled study LLM fine-tuning synthetic-only real-only mixed data comparison data quality bias fairness downstream generalization evaluation

**Why this query**

A controlled LLM-specific comparison of synthetic-only, real-only, and mixed-data fine-tuning would most directly strengthen the answer’s central claims about quality, bias, and generalization.

5 result(s) retrieved; 4 new unique source(s) added.

- **S10 — [PDF] Advancing Algorithmic Fairness via Selectively Fine-Tuning Biased ...**
  URL: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_AIM-Fair_Advancing_Algorithmic_Fairness_via_Selectively_Fine-Tuning_Biased_Models_with_CVPR_2025_paper.pdf
- **S11 — LLM2LLM: Synthetic Data for Fine-Tuning (UC Berkeley)**
  URL: https://www.youtube.com/watch?v=OBk3d8UDQ4g
- **S12 — Synthetic Data + Evaluation Pipelines: Scaling Fine-Tuning ...**
  URL: https://medium.com/@akankshasinha247/synthetic-data-evaluation-pipelines-scaling-fine-tuning-without-losing-alignment-f469a81cdf9a
- **S13 — Synthetic Data Generation Strategies for Fine-Tuning LLMs**
  URL: https://scale.com/blog/synthetic-data-fine-tuning-llms

**Search Duration:** 2.18s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 5
- New gaps: 1
- Resolved gaps: 0

**Processing Duration:** 19.28s

---

## 3. Ledger Updates

### New Claim C10

**Claim**

For LLM fine-tuning under constrained query or generation budgets, the most effective synthetic-data strategy can depend on the available budget and task: answer augmentation was favored at low query-budget ratios, while generating new questions became more effective as the budget increased in experiments spanning mathematics, general question answering, and Text2SQL.

- S13 supports (direct): Reports a controlled experiment comparing answer augmentation, question rephrasing, and new-question generation across mathematics, general QA, and Text2SQL. It finds answer augmentation most effective with limited query budgets and new-question generation more effective as the budget increases.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C3

**Claim**

Synthetic data can reproduce or amplify biases present in its generator or design, and may still underrepresent demographics, harming fairness and generalizability.

- S10 supports (indirect): In a fairness-focused synthetic-data study, the authors identify a bias gap between real and synthetic data and show that balanced synthetic data can improve fairness while synthetic-data limitations and domain mismatch affect utility. The evidence is from computer vision rather than LLMs.
- S11 supports (indirect): The discussion warns that a synthetic-data teacher with incomplete domain coverage or its own biases may fail to reproduce the diversity and nuances of real-world data, potentially transferring those limitations to the student model.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

Synthetic examples may lack realism or subtle real-world patterns, so models trained on them may generalize poorly outside the synthetic distribution.

- S10 supports (indirect): Reports a domain gap between real and synthetic data and states that blindly fine-tuning on synthetic data can decrease utility; balanced synthetic training improved fairness but could reduce accuracy because of this gap.
- S11 supports (indirect): Warns that teacher-model knowledge gaps, biases, and failure to capture real-world complexity or domain-specific language can limit transfer from synthetic data to the student model.
- S13 supports (direct): Shows that synthetic-generation strategy affects fine-tuning accuracy differently as task type and query budget change, indicating that synthetic-data utility is distribution- and setup-dependent.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C6

**Claim**

Synthetic data quality requires validation for accuracy or distributional fidelity, diversity, realism, and coverage, using automated/statistical checks together with human evaluation where appropriate.

- S10 supports (indirect): Identifies synthetic-data quality, diversity, domain shift, and bias shift as distinct problems and uses controlled generation plus selective fine-tuning to address them, illustrating the need to validate both data and downstream effects.
- S11 supports (indirect): Explicitly recommends critical assessment of synthetic-data quality, transferability, domain alignment, diversity, and bias rather than relying on generated volume.
- S13 supports (direct): Uses controlled experiments across generation strategies, query budgets, and task types to assess synthetic-data effectiveness, providing an example of strategy-specific evaluation.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C7

**Claim**

Models trained or fine-tuned with synthetic data should be evaluated on trusted, real-world or otherwise independently grounded data and realistic tasks, because benchmark scores can be contaminated, saturated, or insufficiently representative.

- S10 supports (indirect): Evaluates both utility and fairness using demographic-group performance and equalized-odds measures, showing that synthetic-data methods should be assessed on multiple downstream criteria rather than accuracy alone.
- S13 supports (direct): Evaluates alternative synthetic-data strategies across three task types and varying query budgets, demonstrating the value of comparative, task-specific downstream evaluation.
- S11 supports (indirect): States that synthetic-data pipelines require critical assessment of quality, transferability, domain alignment, and model performance, while noting that simple claims of successful transfer are insufficient.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C1

**Claim**

Synthetic data can supplement LLM training or fine-tuning when real-world data is scarce, expensive to label, privacy-sensitive, or difficult to collect, enabling faster dataset creation and prototyping.

- S13 supports (direct): Reports a controlled framework for using synthetic data to address the fine-tuning data bottleneck and improve cost-effectiveness under different resource constraints.
- S11 supports (indirect): Describes using a stronger teacher LLM to generate missing domain-specific examples from a small seed set for fine-tuning a student model.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### New Gap G7

The controlled LLM study compares synthetic-data generation strategies but, in the supplied evidence, does not report whether its gains persist under independent real-world evaluation or when compared directly with real-only, synthetic-only, and mixed-data training regimes.

---

## 4. Current Research State

- Claims: 10
- Supported: 9
- Weak: 1
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 7
- Remaining Searches: 0

---

## 5. Research Decision

**Decision:** Stop researching.

**Why**

The maximum research iteration budget was reached.

**Stop Reason:** max_iterations


---

# Final Research Decision

**Stop Reason:** max_iterations

**Remaining Uncertainty**

- No controlled, LLM-specific comparison of synthetic-only, real-only, and mixed-data fine-tuning across data quality, bias, and downstream generalization is supplied.
- No reliable procedure for detecting privacy leakage or memorization in LLM-generated synthetic training data is supplied.
- The conditions under which synthetic data improves or worsens demographic fairness, including subgroup-specific outcomes, remain unresolved.
- The amount of synthetic data or recursive training needed before degradation or model collapse becomes likely is unknown.
- No standardized evaluation protocol is supplied for fidelity, novelty, contamination, bias shift, and real-world LLM performance.
- The external validity of reported hybrid-training benefits across domains, model sizes, task types, and synthetic-only baselines remains unresolved.
- The controlled LLM study does not establish whether its reported gains persist under independent real-world evaluation or against direct real-only, synthetic-only, and mixed-data baselines.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 7.49s |
| Evidence Processing | 3 | 62.83s |
| Research Decision | 2 | 4.35s |
| Report Generation | 1 | 19.02s |
| Total Run | — | 93.69s |
