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

**Unique Sources:** 14

**OpenAI Calls:** 6

**Tavily Calls:** 3

**Started:** 2026-08-31T17:44:13-04:00

**Ended:** 2026-08-31T17:45:29-04:00

**Total Runtime:** 76.20s

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

**Search Duration:** 2.60s

---

## 2. Evidence Processing

- New claim proposals: 6
- Existing claim updates: 0
- New gaps: 4
- Resolved gaps: 0

**Processing Duration:** 16.29s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

Synthetic data can benefit LLM training and fine-tuning by expanding scarce or expensive datasets, supporting domain adaptation, targeting underrepresented classes, and generating task-specific examples such as dialogues, code, reasoning traces, and classification items.

- S4 supports (direct): Describes synthetic data as useful for data augmentation, class-imbalance mitigation, domain adaptation, rapid prototyping, and task-specific LLM training examples.
- S5 supports (direct): Reports that existing models can generate reasoning traces, code examples, question-answer pairs, and other data that expand training resources and improve performance on specific tasks.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C2

**Claim**

Using model-generated data recursively or replacing real data with synthetic data can cause model collapse, including narrowing of the learned distribution, loss of low-probability valid examples, and degraded performance or perplexity.

- S1 supports (direct): Summarizes the Nature study's finding that indiscriminate use of model-generated content causes irreversible defects and describes distribution-tail loss and OPT-125m perplexity increases of 20–28 points after five epochs without retained real data.
- S2 supports (direct): States that recursive training on synthetic data narrows distributions until outputs degrade.
- S5 supports (direct): Warns that repeated training on other models' outputs without sufficient new information or external feedback can stagnate or degrade capabilities.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C3

**Claim**

Retaining and accumulating real data alongside synthetic data is presented as a way to reduce, or analytically bound, model-collapse risk; indiscriminate replacement of real data is riskier than additive use.

- S1 supports (direct): Reports Gerstgrasser et al.'s analytical result that test error has a finite upper bound when synthetic data accumulates alongside real data but grows without bound when synthetic data replaces real data; it also recommends an accumulate-not-replace regime.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C4

**Claim**

Synthetic-data quality depends on generation discipline and validation: curation, diversity, deduplication, quality filtering, lineage, and fidelity metadata are important controls against repetition, distribution drift, and audit failures.

- S1 supports (direct): Emphasizes that curated synthetic data rather than volume is associated with successful examples, and cites less than 1% duplicate content for Cosmopedia plus deduplication and quality filtering as controls.
- S2 supports (direct): States that ungoverned synthetic data creates audit gaps and that lineage and fidelity metadata are necessary.
- S4 supports (direct): States that synthetic-data utility depends critically on generation techniques, validation methods, and alignment with the target distribution and application requirements.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C5

**Claim**

Synthetic data can help construct evaluation sets by systematically covering edge cases, adversarial scenarios, decision boundaries, and conversational failure modes, but synthetic or conventional benchmark scores may not reliably represent real-world capability or safety.

- S4 supports (direct): Describes generating synthetic evaluation cases for edge cases, adversarial examples, ambiguous queries, multi-turn context, failure modes, decision boundaries, calibration, and robustness.
- S5 supports (direct): Warns that traditional benchmarks can be saturated or contaminated, and that static tests may miss complex real-world reliability, fairness, reproducibility, and safety issues.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C6

**Claim**

Synthetic data does not automatically remove bias or guarantee privacy: generated data can inherit problematic patterns from source or generator models, while privacy protection depends on whether individuals can still be re-identified and on governance controls.

- S1 supports (direct): Notes that synthetic-data use has distinct privacy-substitution risks and that GDPR treatment can still apply where re-identification is plausible.
- S4 supports (indirect): Presents synthetic data as potentially useful for privacy-sensitive settings and class imbalance, but defines its value as dependent on fidelity, validation, and alignment rather than as an automatic guarantee.
- S5 supports (direct): Identifies biased information and private data as risks affecting model performance and deployment, and emphasizes privacy protection and data-mixture design.

**Confidence:** LOW

**Status:** INSUFFICIENT_EVIDENCE

### New Gap G1

Direct, controlled real-world evidence is lacking on when synthetic data improves versus harms downstream LLM quality compared with equivalent quantities of human-authored or human-labeled data, especially across fine-tuning tasks and domains.

### New Gap G2

The sources do not quantify how synthetic-data generation affects demographic, cultural, or task-specific bias, nor whether targeted generation for minority classes improves fairness without introducing stereotyping or label artifacts.

### New Gap G3

The sources do not establish reliable privacy guarantees or measurable re-identification and memorization risks for LLM-generated training data derived from sensitive records or model outputs.

### New Gap G4

Evidence is insufficient on how to validate synthetic evaluation sets against independent real-world outcomes, contamination, benchmark gaming, and distribution shift, or on which metrics best detect these failures.

---

## 4. Current Research State

- Claims: 6
- Supported: 5
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 1
- Open Gaps: 4
- Remaining Searches: 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** GAP G2

**Why**

Bias is a central requested focus, but the current evidence is low-confidence and lacks measured findings on bias transfer and fairness effects.

**Next Search**

> controlled studies synthetic data LLM fine-tuning demographic bias fairness minority classes stereotyping label artifacts evaluation


---

# Iteration 2

## 1. Search

**Query**

> controlled studies synthetic data LLM fine-tuning demographic bias fairness minority classes stereotyping label artifacts evaluation

**Target:** G2

**Purpose:** GENERAL

**Why this query**

Bias is a central requested focus, but the current evidence is low-confidence and lacks measured findings on bias transfer and fairness effects.

5 result(s) retrieved; 5 new unique source(s) added.

- **S6 — Synthetic Data for Bias Mitigation 2026: 5 Methods + FAGI**
  URL: https://futureagi.com/blog/synthetic-data-generation-bias-2025
- **S7 — Evaluating LLMs for Detecting Demographic-Targeted Social Bias: A Comprehensive Benchmark Study**
  URL: https://arxiv.org/html/2510.04641v3
- **S8 — Towards Understanding Bias in Synthetic Data for Evaluation | alphaXiv**
  URL: https://www.alphaxiv.org/abs/2506.10301
- **S9 — Data bias in LLM and generative AI applications - MOSTLY AI powered by Syntho**
  URL: https://mostly.ai/blog/data-bias-types
- **S10 — Guide to Ethical Fine-Tuning of Large Language Models | Tonic.ai**
  URL: https://www.tonic.ai/guides/ethical-fine-tuning-llm-synthetic-data

**Search Duration:** 2.45s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 6
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 13.33s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Synthetic data can benefit LLM training and fine-tuning by expanding scarce or expensive datasets, supporting domain adaptation, targeting underrepresented classes, and generating task-specific examples such as dialogues, code, reasoning traces, and classification items.

- S6 supports (direct): Describes targeted synthetic records for under-represented subgroups, rare events, specialized domains, and under-represented languages as a way to expand and rebalance training data, conditional on validation.
- S9 supports (direct): Explains that synthetic data can address missing or imbalanced categories and simulate records when real data is scarce, including through rebalancing and conditional generation.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

Using model-generated data recursively or replacing real data with synthetic data can cause model collapse, including narrowing of the learned distribution, loss of low-probability valid examples, and degraded performance or perplexity.

- S9 supports (direct): Identifies training generative models on generated data as a negative recursive loop that can reduce output quality.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

Synthetic data can help construct evaluation sets by systematically covering edge cases, adversarial scenarios, decision boundaries, and conversational failure modes, but synthetic or conventional benchmark scores may not reliably represent real-world capability or safety.

- S8 supports (direct): An empirical study of LLM-generated synthetic IR test collections found systematic differences from human queries and judgments, including longer synthetic queries, approximately 0.28-point higher GPT-4 relevance scores, and distorted absolute system-performance estimates.
- S6 supports (direct): Recommends held-out evaluation, distributional-fit checks, task-utility checks, privacy screening, and re-auditing when synthetic data is used for targeted coverage and fairness work.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C6

**Claim**

Synthetic data does not automatically remove bias or guarantee privacy: generated data can inherit problematic patterns from source or generator models, while privacy protection depends on whether individuals can still be re-identified and on governance controls.

- S6 supports (direct): States that synthetic data can target under-represented slices and potentially reduce fairness gaps, but requires distributional-fit, utility, privacy, held-out evaluation, and re-audit checks; it presents fairness improvement as conditional rather than automatic.
- S7 supports (direct): A benchmark across twelve English datasets found that LLM-based demographic-bias detection has persistent disparities across demographic axes and weaknesses on intersectional cases, indicating that automated bias auditing itself is imperfect.
- S9 supports (direct): Describes selection, social, temporal, implicit, and automation biases in LLM and generative-AI data workflows, and recommends diverse, high-quality data plus human supervision rather than assuming generated outputs are trustworthy.
- S6 contradicts (indirect): Presents targeted synthetic generation as a potentially effective lever for reducing bias and closing subgroup coverage gaps when the proposed audit-and-retrain loop succeeds; this qualifies the claim's risk emphasis but does not refute that bias removal is not automatic.

**Confidence:** LOW → MEDIUM

**Status:** INSUFFICIENT_EVIDENCE → WEAK

### Updated Claim C4

**Claim**

Synthetic-data quality depends on generation discipline and validation: curation, diversity, deduplication, quality filtering, lineage, and fidelity metadata are important controls against repetition, distribution drift, and audit failures.

- S6 supports (direct): Specifies validation controls including distributional-fit testing, task-utility checks, privacy screening, held-out evaluation, fairness auditing, and re-auditing after retraining.
- S8 supports (direct): Uses comparisons of synthetic and human query characteristics, judgment distributions, statistical tests, and mixed-effects modeling to detect systematic evaluation bias.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C3

**Claim**

Retaining and accumulating real data alongside synthetic data is presented as a way to reduce, or analytically bound, model-collapse risk; indiscriminate replacement of real data is riskier than additive use.

- No new evidence relationship was added.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 6
- Supported: 5
- Weak: 1
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 4
- Remaining Searches: 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** GAP G1

**Why**

A controlled comparison of synthetic versus human-authored data would most directly clarify the central quality tradeoff and strengthen the answer beyond conditional claims.

**Next Search**

> controlled empirical study synthetic versus human-authored data LLM fine-tuning downstream performance quality domains tasks comparison


---

# Iteration 3

## 1. Search

**Query**

> controlled empirical study synthetic versus human-authored data LLM fine-tuning downstream performance quality domains tasks comparison

**Target:** G1

**Purpose:** GENERAL

**Why this query**

A controlled comparison of synthetic versus human-authored data would most directly clarify the central quality tradeoff and strengthen the answer beyond conditional claims.

5 result(s) retrieved; 4 new unique source(s) added.

- **S11 — Synthetic Data for LLM Fine-Tuning 2026**
  URL: https://futureagi.com/blog/synthetic-data-fine-tuning-llms
- **S12 — How Good Are Synthetic Requirements ? Evaluating LLM-Generated Datasets for AI4RE**
  URL: https://arxiv.org/html/2506.21138v1
- **S13 — Synthetic Data Generation Strategies for Fine-Tuning LLMs**
  URL: https://scale.com/blog/synthetic-data-fine-tuning-llms
- **S14 — Medium**
  URL: https://medium.com/@akankshasinha247/synthetic-data-evaluation-pipelines-scaling-fine-tuning-without-losing-alignment-f469a81cdf9a

**Search Duration:** 2.47s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 3
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 13.37s

---

## 3. Ledger Updates

### New Claim C7

**Claim**

The effectiveness of synthetic data for LLM fine-tuning depends on the generation strategy, task, seed-data size, and available generation budget; no single strategy is uniformly optimal across settings.

- S13 supports (direct): Controlled experiments across mathematics, general question answering, and Text2SQL found that answer augmentation works best under limited query budgets, while generating new questions becomes more effective as the budget increases.
- S12 supports (direct): Across four requirements-classification tasks, multi-sample prompting improved utility and diversity, while automated prompt optimization produced task-dependent gains and losses.

**Confidence:** HIGH

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

Synthetic data can benefit LLM training and fine-tuning by expanding scarce or expensive datasets, supporting domain adaptation, targeting underrepresented classes, and generating task-specific examples such as dialogues, code, reasoning traces, and classification items.

- S11 supports (direct): Describes synthetic rows tailored to SFT, preference optimization, tool-use, RAG, and reasoning fine-tuning, using a small real seed to expand task-specific data.
- S12 supports (direct): Reports that synthetic requirements matched or surpassed human-authored data on specific classification tasks, with additional gains from hybrid real-plus-synthetic training.
- S13 supports (direct): Controlled experiments across mathematics, general question answering, and Text2SQL show that synthetic-generation strategies can improve fine-tuning accuracy under constrained data budgets.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

Synthetic-data quality depends on generation discipline and validation: curation, diversity, deduplication, quality filtering, lineage, and fidelity metadata are important controls against repetition, distribution drift, and audit failures.

- S11 supports (direct): Describes quality filtering, faithfulness and instruction-adherence checks, teacher mixing, real-data anchoring, and diversity checks as controls for teacher-bias inheritance and mode collapse.
- S12 supports (direct): Finds that multi-sample prompting improves synthetic-data utility and diversity, demonstrating that generation and curation choices materially affect quality.
- S13 supports (direct): Evaluates multiple generation strategies under different budgets and tasks, emphasizing that dataset-construction choices affect downstream fine-tuning performance.
- S12 contradicts (direct): Similarity-based curation consistently improved diversity metrics but often reduced classification performance, showing that deduplication or diversity-oriented filtering is not universally beneficial for task utility.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

Synthetic data can help construct evaluation sets by systematically covering edge cases, adversarial scenarios, decision boundaries, and conversational failure modes, but synthetic or conventional benchmark scores may not reliably represent real-world capability or safety.

- S12 supports (direct): Uses comparisons with human-authored requirements and multiple classification tasks to show that synthetic data can perform well in specific evaluation settings, while task-dependent prompt and curation effects complicate general conclusions.
- S14 supports (indirect): Argues that synthetic-data workflows require human oversight and semantic, judgment-based evaluation rather than relying only on surface-form metrics such as BLEU or ROUGE.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 7
- Supported: 6
- Weak: 1
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 4
- Remaining Searches: 0

---

## 5. Research Decision

**Decision:** Stop researching.

**Origin:** BUDGET_STOP

**Why**

The maximum research iteration budget was reached.

**Stop Reason:** max_iterations


---

# Final Research Decision

**Stop Reason:** max_iterations

**Remaining Uncertainty**

- Direct controlled real-world evidence is lacking on when synthetic data improves versus harms downstream LLM quality compared with equivalent human-authored or human-labeled data across fine-tuning tasks and domains.
- The evidence does not quantify demographic, cultural, or task-specific bias effects, or establish whether minority-class targeting improves fairness without stereotyping or label artifacts.
- Reliable privacy guarantees and measurable re-identification or memorization risks for LLM-generated training data remain unestablished.
- The evidence does not establish how to validate synthetic evaluation sets against independent real-world outcomes, contamination, benchmark gaming, and distribution shift, or which metrics best detect these failures.
- The research process ended because the maximum number of iterations was reached. No separate ledger record documents counter-searches blocked by duplication, budget, or a one-search limit.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 7.52s |
| Evidence Processing | 3 | 42.99s |
| Research Decision | 2 | 4.26s |
| Report Generation | 1 | 21.43s |
| Total Run | — | 76.20s |
