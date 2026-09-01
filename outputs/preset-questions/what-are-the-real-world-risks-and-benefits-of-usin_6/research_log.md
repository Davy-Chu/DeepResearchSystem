# Research Run Log

## Run Summary

**System Version:** evidence-ledger-decomposer-v1

**Research Question**

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 15

**OpenAI Calls:** 7

**Tavily Calls:** 3

**Started:** 2026-08-31T21:11:36-04:00

**Ended:** 2026-08-31T21:13:02-04:00

**Total Runtime:** 85.92s

---

# Research Plan

## Subquestions

### SQ1 [CORE]

**Question:**

How does using synthetic data to train or fine-tune large language models affect data quality, including factual accuracy, diversity, coverage, noise, artifacts, and the risk of model-generated errors being amplified or propagated?

**Success criteria:**

Assess documented benefits and harms to training-data quality, distinguishing cases where synthetic data supplements, transforms, or replaces real data, and identify evidence about downstream model performance and failure modes.

**Initial status:** UNRESEARCHED

### SQ2 [CORE]

**Question:**

How does synthetic training data affect bias, fairness, representation, and the inclusion or exclusion of demographic, linguistic, cultural, or other underrepresented groups?

**Success criteria:**

Identify mechanisms through which synthetic data can reduce or reproduce bias, including inheritance of biases from source models, distributional narrowing, feedback loops, and targeted data generation, with evidence from relevant evaluations.

**Initial status:** UNRESEARCHED

### SQ3 [CORE]

**Question:**

What evaluation methods and benchmarks are needed to determine whether synthetic data improves or degrades large language model performance and safety?

**Success criteria:**

Compare evaluation approaches for data quality, generalization, robustness, factuality, toxicity, fairness, privacy, and distribution shift; explain what each can and cannot establish, including risks of contamination or misleading benchmark gains.

**Initial status:** UNRESEARCHED

### SQ4 [SECONDARY]

**Question:**

What practical benefits and risks arise from using synthetic data in different roles—augmentation, instruction fine-tuning, domain adaptation, or replacement of real data—and how do these vary by use case?

**Success criteria:**

Synthesize evidence on benefits such as scalability, controllability, privacy, cost, and rare-case coverage against risks such as reduced diversity, hidden errors, privacy leakage, and capability collapse, while preserving distinctions among training roles and use cases.

**Initial status:** UNRESEARCHED

## Synthesis Requirements

- Synthesize benefits and risks rather than treating synthetic data as uniformly beneficial or harmful.
- Distinguish effects on data quality, bias, and evaluation, and explain how these dimensions interact—for example, how quality defects can create or mask bias and how evaluation choices can misrepresent gains.
- Preserve distinctions between synthetic data used for pretraining, continued training, instruction fine-tuning, and targeted augmentation where evidence differs.
- Represent uncertainty and identify conditions under which observed benefits or risks are likely to hold.

## Output Requirements

- Focus on real-world risks and benefits of synthetic data for training or fine-tuning large language models.
- Organize the analysis around data quality, bias, and evaluation.
- Include both positive and negative consequences.

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
- **S3 — Using Synthetic Data to Improve LLM Fine‑Tuning | newline**
  URL: https://www.newline.co/@Dipen/using-synthetic-data-to-improve-llm-finetuning--d453f658
- **S4 — Synthetic Data Generation with LLMs: Techniques and Use Cases**
  URL: https://tetrate.io/learn/ai/synthetic-data-generation-llms
- **S5 — Large Language Models Are Still Getting Stronger, but ...**
  URL: https://www.newswise.com/articles/large-language-models-are-still-getting-stronger-but-researchers-face-new-bottlenecks-in-data-evaluation-and-safety

**Search Duration:** 2.23s

---

## 2. Evidence Processing

- New claim proposals: 5
- Existing claim updates: 0
- New gaps: 4
- Resolved gaps: 0

**Processing Duration:** 15.84s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

Synthetic data can provide practical benefits when used as curated augmentation or targeted generation: it can expand scarce training resources, create domain- or task-specific examples, cover rare or edge cases, address class imbalance, and support rapid prototyping where real data is costly, limited, or sensitive.

- S4 supports (direct): Describes augmentation, rare-edge-case generation, class-imbalance mitigation, privacy-sensitive data use, domain adaptation, and rapid prototyping as uses of LLM-generated synthetic data.
- S1 supports (indirect): Reports that curated synthetic textbooks and exercises supplemented real data in Phi-1 training and were associated with strong coding-benchmark results; presents edge-case augmentation as a distinct use case.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C2

**Claim**

Replacing real training data with recursively generated synthetic data can cause model collapse: successive training generations may lose low-probability or tail-distribution content, with degradation in diversity and performance; retaining or accumulating real data is presented as a mitigation.

- S1 supports (direct): Summarizes the Nature study's finding that indiscriminate iterative use of model-generated content causes irreversible defects and loss of distribution tails, and reports OPT-125m perplexity degradation after purely synthetic self-training.
- S2 supports (direct): States that recursive synthetic training narrows distributions and degrades outputs.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C3

**Claim**

The quality of synthetic data depends on generation and curation rather than volume alone: filtering, deduplication, diversity controls, validation, and alignment with the target distribution are material conditions for usefulness, while uncurated generation can amplify errors and artifacts.

- S1 supports (direct): Contrasts curated synthetic training data with indiscriminate generation, states that volume without curation amplifies failure modes, and describes deduplication and quality filtering as part of a lower-risk regime.
- S4 supports (direct): States that synthetic-data utility depends critically on generation techniques, validation, and alignment between synthetic and target distributions.
- S5 supports (direct): Identifies novelty, reliability, verifiability, and sustainability as requirements, and warns that repeated training without new information or external feedback can stagnate or degrade capabilities.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C4

**Claim**

Synthetic data can be used to target underrepresented classes or scenarios and may therefore improve representation of selected categories, but this does not establish broader demographic, linguistic, or cultural fairness.

- S4 supports (direct): Describes generating additional examples for underrepresented classes to mitigate class imbalance and improve robustness.
- S2 supports (direct): States that synthetic data can mirror real distributions and address class imbalance.
- S1 contradicts (indirect): Reports that iterative synthetic training can lose the tails of the original distribution, which could undermine representation of rare groups or cases when those tails are not deliberately preserved.

**Confidence:** LOW

**Status:** WEAK

### New Claim C5

**Claim**

Benchmark gains from synthetic-data training are insufficient by themselves to establish real-world improvement: evaluation must also examine generalization, factuality, robustness, safety, fairness, contamination, and performance on realistic or shifted tasks.

- S5 supports (direct): Warns that benchmark saturation and contamination can make scores misleading, and argues for realistic evaluation covering reliability, safety, robustness, fairness, and complex tasks.
- S4 supports (direct): Describes synthetic evaluation sets for edge cases, adversarial examples, ambiguity, multi-turn context, calibration, and robustness.
- S1 supports (indirect): Notes that the four synthetic-data roles, including evaluation-set creation, have different failure modes and metrics, including evaluation overfitting.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Gap G1

No supplied source provides direct, controlled subgroup-level evaluations of how synthetic training data affects demographic, linguistic, cultural, or intersectional bias and fairness, including whether targeted augmentation improves outcomes without creating new disparities.

### New Gap G2

The evidence does not directly compare synthetic data with real data across pretraining, continued training, instruction fine-tuning, and domain adaptation while measuring factuality, diversity, coverage, noise, artifacts, and downstream failures.

### New Gap G3

No supplied source establishes a validated evaluation methodology for synthetic-data interventions that jointly controls for benchmark contamination, synthetic-evaluation bias, data leakage, distribution shift, privacy, safety, and real-world task performance.

### New Gap G4

The privacy benefit of synthetic substitution remains unresolved: the sources describe possible removal of direct links to individuals but do not provide re-identification, memorization, privacy-leakage, or regulatory validation results for LLM-generated datasets.

---

## 4. Current Research State

- Claims: 5
- Supported: 4
- Weak: 1
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 4
- Remaining Searches: 2

### Subquestion Progress

**SQ1:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** UNRESEARCHED → PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ3:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ4:** UNRESEARCHED → PARTIAL

Reason: At least one linked ledger claim is not yet supported.

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

A high-importance CORE gap remains unresolved: there is no direct evidence on subgroup-level demographic, linguistic, cultural, or intersectional fairness effects of synthetic training data or targeted augmentation. This is central to the requested bias focus and can materially improve the answer.

**Next Search**

> peer-reviewed empirical studies LLM synthetic training data demographic bias fairness subgroup evaluation targeted augmentation underrepresented languages cultures intersectional


---

# Iteration 2

## 1. Search

**Query**

> peer-reviewed empirical studies LLM synthetic training data demographic bias fairness subgroup evaluation targeted augmentation underrepresented languages cultures intersectional

**Target:** SQ2

**Purpose:** SUBQUESTION

**Why this query**

A high-importance CORE gap remains unresolved: there is no direct evidence on subgroup-level demographic, linguistic, cultural, or intersectional fairness effects of synthetic training data or targeted augmentation. This is central to the requested bias focus and can materially improve the answer.

5 result(s) retrieved; 5 new unique source(s) added.

- **S6 — Bias in Large Language Models: Origin, Evaluation, and Mitigation**
  URL: https://arxiv.org/html/2411.10915v1
- **S7 — Measuring gender and racial biases in large language models: Intersectional evidence from automated resume evaluation**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11937954
- **S8 — Tackling bias in large ML models: the role of synthetic data**
  URL: https://syntheticus.ai/blog/tackling-bias-in-large-ml-models-the-role-of-synthetic-data
- **S9 — Capturing Bias Diversity in LLMs**
  URL: https://doras.dcu.ie/30827/1/Capturing_Bias_Diversity_in_LLMs.pdf
- **S10 — Bias Mitigation via Synthetic Data Generation: A Review**
  URL: https://www.mdpi.com/2079-9292/13/19/3909

**Search Duration:** 2.54s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 2
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 12.19s

---

## 3. Ledger Updates

### New Claim C6

**Claim**

Synthetic-data fine-tuning does not automatically remove foundation-model bias: pre-existing biases may persist, while biases in the fine-tuning material can be added or intensified; deliberately configuring or combining models to represent demographic perspectives is therefore not evidence of improved fairness without outcome-level evaluation.

- S9 supports (direct): States that biases embedded in a foundation model persist during fine-tuning and may be extended by biases in fine-tuning materials; also demonstrates deliberate fine-tuning of models to express demographic biases.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C4

**Claim**

Synthetic data can be used to target underrepresented classes or scenarios and may therefore improve representation of selected categories, but this does not establish broader demographic, linguistic, or cultural fairness.

- S6 supports (direct): Reviews how non-representative, incomplete, or imbalanced training data can produce gender, racial, cultural, and socioeconomic bias, and identifies augmentation and resampling as possible data-level mitigation strategies, while noting their limitations.
- S9 supports (direct): Reports that foundation-model biases persist through fine-tuning and may be extended by biases in the fine-tuning material, indicating that targeted synthetic fine-tuning is not inherently fairness-improving.
- S10 supports (indirect): Provides a review specifically focused on synthetic-data generation for bias mitigation, establishing that synthetic generation is studied as a mitigation approach but does not, in the supplied excerpt, provide outcome-level evidence sufficient to establish general fairness benefits.

**Confidence:** LOW → MEDIUM

**Status:** WEAK → WEAK

### Updated Claim C5

**Claim**

Benchmark gains from synthetic-data training are insufficient by themselves to establish real-world improvement: evaluation must also examine generalization, factuality, robustness, safety, fairness, contamination, and performance on realistic or shifted tasks.

- S7 supports (direct): Demonstrates that LLM evaluation in a high-stakes resume-screening task can reveal intersectional gender and racial disparities, including differing effects across social groups, showing why aggregate capability scores are insufficient.
- S9 supports (direct): Lists TruthfulQA and hallucination-oriented evaluation alongside capability benchmarks, and notes that common benchmarks do not address bias in training data or model responses; crowdsourced rankings measure user popularity rather than objective quality.
- S6 supports (direct): Reviews data-level, model-level, and output-level bias evaluation methods and emphasizes that bias can manifest across demographic attributes and application contexts.

**Confidence:** MEDIUM → HIGH

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

### Subquestion Progress

**SQ1:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ3:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ4:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

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

**Target:** SUBQUESTION SQ2

**Why**

A final search is likely to materially improve the answer by addressing the highest-priority unresolved gap: direct empirical subgroup-level evidence on whether synthetic-data augmentation improves or worsens demographic, linguistic, cultural, or intersectional fairness. SQ2 remains only weakly supported, while the other core gaps can be responsibly framed as limitations and open questions.

**Next Search**

> empirical controlled study synthetic data augmentation LLM fine-tuning demographic fairness bias intersectional subgroup evaluation underrepresented languages cultures synthetic versus real data


---

# Iteration 3

## 1. Search

**Query**

> empirical controlled study synthetic data augmentation LLM fine-tuning demographic fairness bias intersectional subgroup evaluation underrepresented languages cultures synthetic versus real data

**Target:** SQ2

**Purpose:** SUBQUESTION

**Why this query**

A final search is likely to materially improve the answer by addressing the highest-priority unresolved gap: direct empirical subgroup-level evidence on whether synthetic-data augmentation improves or worsens demographic, linguistic, cultural, or intersectional fairness. SQ2 remains only weakly supported, while the other core gaps can be responsibly framed as limitations and open questions.

5 result(s) retrieved; 5 new unique source(s) added.

- **S11 — Towards Understanding Bias in Synthetic Data for Evaluation | alphaXiv**
  URL: https://www.alphaxiv.org/abs/2506.10301
- **S12 — LLM-Based Data Augmentation**
  URL: https://www.emergentmind.com/topics/llm-based-data-augmentation
- **S13 — The Impact of Synthetic Data Diversity on LLM Fine-Tuning**
  URL: https://arxiv.org/html/2511.01490v1
- **S14 — GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub**
  URL: https://github.com/pengr/LLM-Synthetic-Data
- **S15 — Creating and Validating Synthetic Datasets for LLM Evaluation & Experimentation - Arize AI**
  URL: https://arize.com/blog/creating-and-validating-synthetic-datasets-for-llm-evaluation-experimentation

**Search Duration:** 2.87s

---

## 2. Evidence Processing

- New claim proposals: 2
- Existing claim updates: 6
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 17.80s

---

## 3. Ledger Updates

### New Claim C7

**Claim**

Synthetic-data diversity is a material condition for safer LLM fine-tuning: using synthetic data from multiple source models can mitigate distribution collapse and preserve broader output and linguistic diversity relative to single-source synthetic data, although it does not eliminate downstream safety risks.

- S13 supports (direct): Reports that synthetic fine-tuning decreased adversarial robustness while preserving output quality, making outputs potentially more usable and dangerous.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C8

**Claim**

Synthetic test collections can introduce systematic evaluation bias: LLM-generated queries and relevance judgments may differ from human data and judgments, potentially overestimating absolute system performance even when relative system comparisons are less affected.

- S11 supports (direct): Reports that synthetic queries differed systematically from human queries and that GPT-4 relevance judgments were more lenient than human judgments; the study found significant effects on absolute performance estimates but smaller effects when comparing relative system performance.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

Synthetic data can provide practical benefits when used as curated augmentation or targeted generation: it can expand scarce training resources, create domain- or task-specific examples, cover rare or edge cases, address class imbalance, and support rapid prototyping where real data is costly, limited, or sensitive.

- S12 supports (direct): Describes LLM augmentation as useful for low-resource and cross-lingual tasks, reporting accuracy gains and targeted generation of task-specific examples, while emphasizing human or automated filtering.
- S15 supports (direct): Describes synthetic datasets as useful for controlled experimentation, edge-case coverage, privacy-sensitive development, debugging, and repeatable golden datasets.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

Replacing real training data with recursively generated synthetic data can cause model collapse: successive training generations may lose low-probability or tail-distribution content, with degradation in diversity and performance; retaining or accumulating real data is presented as a mitigation.

- S13 supports (direct): Finds that synthetic fine-tuning can produce distribution collapse and reduced linguistic diversity, while showing that greater diversity of source models mitigates these effects.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C3

**Claim**

The quality of synthetic data depends on generation and curation rather than volume alone: filtering, deduplication, diversity controls, validation, and alignment with the target distribution are material conditions for usefulness, while uncurated generation can amplify errors and artifacts.

- S12 supports (direct): Documents redundant, repetitive, linguistically erroneous, and poorly understandable outputs in low-resource languages, and identifies human-in-the-loop review and quality or logical-consistency filters as mitigations.
- S13 supports (direct): Shows that diversity of synthetic sources affects distribution collapse, linguistic diversity, and adversarial robustness, indicating that source composition is part of data quality control.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

Synthetic data can be used to target underrepresented classes or scenarios and may therefore improve representation of selected categories, but this does not establish broader demographic, linguistic, or cultural fairness.

- S12 supports (direct): Reports performance improvements from LLM-generated augmentation in multilingual and low-resource settings, while documenting persistent quality and language-bias problems in underrepresented languages such as Tamil.
- S12 contradicts (direct): Reports repetitive, grammatically erroneous, ambiguous, and poorly understandable generations in some low-resource languages, showing that augmentation may fail to improve or may degrade representation quality without language-specific validation.

**Confidence:** MEDIUM → MEDIUM

**Status:** WEAK → WEAK

### Updated Claim C5

**Claim**

Benchmark gains from synthetic-data training are insufficient by themselves to establish real-world improvement: evaluation must also examine generalization, factuality, robustness, safety, fairness, contamination, and performance on realistic or shifted tasks.

- S11 supports (direct): Empirically finds that synthetic queries and LLM relevance judgments produce systematic evaluation bias, including overestimation of absolute system performance, while relative comparisons may be less affected.
- S13 supports (direct): Shows that standard performance benchmarks can miss distributional narrowing and robustness changes, and evaluates synthetic fine-tuning using output diversity, adversarial robustness, and self-preference measures.
- S15 supports (indirect): Emphasizes defining evaluation objectives, covering expected input breadth, and validating synthetic evaluation or golden datasets rather than treating them as automatically representative.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C6

**Claim**

Synthetic-data fine-tuning does not automatically remove foundation-model bias: pre-existing biases may persist, while biases in the fine-tuning material can be added or intensified; deliberately configuring or combining models to represent demographic perspectives is therefore not evidence of improved fairness without outcome-level evaluation.

- S12 supports (indirect): Notes that augmentation quality and language bias depend on the generating model and that filtering is needed, supporting the conclusion that synthetic fine-tuning is not inherently fairness-improving.
- S13 supports (direct): Finds source-model diversity affects fine-tuned model behavior and self-preference bias, with human data reducing self-preference more strongly than synthetic data from a single source.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 8
- Supported: 7
- Weak: 1
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 4
- Remaining Searches: 0

### Subquestion Progress

**SQ1:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ3:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ4:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → PARTIAL (targeted searches: 2)
- SQ3 → PARTIAL (targeted searches: 0)

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

**Stop Reason:** max_iterations

**Remaining Uncertainty**

- G1: No supplied source provides direct, controlled subgroup-level evaluations of demographic, linguistic, cultural, or intersectional fairness effects, including whether targeted augmentation improves outcomes without creating new disparities.
- G2: No supplied source directly compares synthetic and real data across pretraining, continued training, instruction fine-tuning, and domain adaptation while jointly measuring factuality, diversity, coverage, noise, artifacts, and downstream failures.
- G3: No supplied source establishes a validated end-to-end evaluation methodology that jointly controls for benchmark contamination, synthetic-evaluation bias, data leakage, distribution shift, privacy, safety, and real-world task performance.
- G4: The privacy benefit of synthetic substitution remains unresolved because re-identification, memorization, privacy-leakage, and regulatory validation results are not supplied.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Question Decomposition | 1 | 8.03s |
| Tavily Search | 3 | 7.64s |
| Evidence Processing | 3 | 45.83s |
| Research Decision | 2 | 5.44s |
| Report Generation | 1 | 18.98s |
| Total Run | — | 85.92s |
