# Research Run Log

## Run Summary

**System Version:** evidence-ledger-decomposer-verifier-v1

**Research Question**

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 15

**OpenAI Calls:** 9

**Tavily Calls:** 3

**Verifier Model:** gpt-5.6-luna

**Started:** 2026-08-31T19:14:10-04:00

**Ended:** 2026-08-31T19:15:55-04:00

**Total Runtime:** 104.58s

---

# Research Plan

## Subquestions

### SQ1 [CORE]

**Question:**

How does using synthetic data to train or fine-tune large language models affect data quality, including factuality, diversity, coverage, consistency, distribution shift, and risks of error propagation or model collapse?

**Success criteria:**

Assess documented benefits and harms to training-data quality, distinguishing the effects of synthetic pretraining from synthetic fine-tuning and identifying the conditions under which synthetic data improves or degrades model performance.

**Initial status:** UNRESEARCHED

### SQ2 [CORE]

**Question:**

What forms of bias can synthetic data introduce, amplify, reduce, or conceal in large language models, and how do these effects compare with those of human-generated data?

**Success criteria:**

Identify relevant sources and mechanisms of bias, explain how generation procedures and filtering affect them, and assess evidence about disparate performance or harms across demographic, linguistic, cultural, and other relevant groups.

**Initial status:** UNRESEARCHED

### SQ3 [CORE]

**Question:**

How should models trained or fine-tuned with synthetic data be evaluated to detect changes in quality, bias, robustness, and real-world safety?

**Success criteria:**

Describe appropriate evaluation designs, benchmarks, human and automated measures, subgroup and out-of-distribution testing, contamination checks, and comparisons against models trained on non-synthetic or mixed data.

**Initial status:** UNRESEARCHED

### SQ4 [SECONDARY]

**Question:**

What real-world benefits and risks arise from synthetic-data use in LLM training or fine-tuning, given the limitations of current data-quality and bias evaluations?

**Success criteria:**

Synthesize evidence on practical benefits such as scalability, privacy, controllability, and targeted coverage with risks such as misleading confidence, hidden bias, poor transfer, and deployment failures, while making uncertainty and evidence limitations explicit.

**Initial status:** UNRESEARCHED

## Synthesis Requirements

- Distinguish training from fine-tuning where their risks and benefits differ.
- Integrate data quality, bias, and evaluation rather than treating evaluation results as equivalent to real-world outcomes.
- Compare synthetic data with human-generated data and with mixed-data approaches where evidence permits.
- Separate demonstrated effects from plausible or context-dependent risks, and state uncertainty explicitly.

## Output Requirements

- Focus on real-world risks and benefits of using synthetic data for large language model training or fine-tuning.
- Center the discussion on data quality, bias, and evaluation.

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

**Search Duration:** 0.57s

---

## 2. Evidence Processing

- New claim proposals: 8
- Existing claim updates: 0
- New gaps: 4
- Resolved gaps: 0

**Processing Duration:** 17.13s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

Synthetic data can improve LLM training efficiency and task-specific performance when it is carefully curated and used alongside substantial real data. The supplied examples describe Phi-1 achieving 50.6% HumanEval pass@1 and 55.5% MBPP after training on curated web data plus one billion synthetic textbook and exercise tokens, although the reported benchmark results are vendor-stated.

- S1 supports (direct): Reports that Phi-1 used 6B curated web tokens plus 1B GPT-3.5-generated synthetic tokens and achieved 50.6% HumanEval pass@1 and 55.5% MBPP.
- S4 supports (direct): States that synthetic augmentation can expand limited labeled datasets and improve robustness or generalization for specific tasks.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C2

**Claim**

Replacing real training data with recursively generated synthetic data can cause model collapse: successive models lose low-probability and diverse parts of the original distribution, and errors can compound across generations.

- S1 supports (direct): Describes the Nature study as finding irreversible defects from indiscriminate model-generated training content, including loss of distribution tails and compounding approximation errors; it also reports 20–28-point perplexity increases in OPT-125m experiments after five epochs without retained real data.
- S2 supports (direct): States that recursive synthetic training narrows distributions until outputs degrade.
- S5 supports (direct): Reports that repeated training on model-generated content without sufficient new information or external feedback can stagnate or degrade capabilities.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C3

**Claim**

Model-collapse risk is context-dependent rather than an inherent consequence of every use of synthetic data: the supplied evidence favors accumulating synthetic data alongside real data, with deduplication and quality filtering, over replacing real data entirely.

- S1 supports (direct): Reports an analytical result that error remains bounded when synthetic data is accumulated alongside real data but can grow without bound when synthetic data replaces real data; it recommends retaining real data and using filtering and deduplication.
- S2 supports (indirect): Identifies recursive training as the collapse mechanism, implying that controlled supplementation differs from unrestricted recursion.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C4

**Claim**

Synthetic data can provide practical benefits by scaling scarce task-specific examples, targeting rare or underrepresented cases, supporting privacy-sensitive development, and accelerating prototyping.

- S4 supports (direct): Lists augmentation for limited labeled data, generation of minority-class and edge-case examples, privacy-sensitive data sharing, and rapid prototyping as use cases.
- S2 supports (direct): States that synthetic data can address data scarcity, privacy constraints, and class imbalance.
- S1 supports (direct): Describes fine-tuning data, edge-case augmentation, and privacy substitution as distinct applications with different risk profiles.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C5

**Claim**

Synthetic data generation procedures can improve apparent diversity and coverage through controlled variation of audiences, formats, classes, or edge cases, but generated data remains dependent on the source model's learned distribution and validation quality.

- S1 supports (direct): Attributes Cosmopedia's reported low duplication to varying audience and format, and emphasizes that curation rather than raw volume determines usefulness.
- S4 supports (direct): Explains that prompting and sampling can create variation across conversational, classification, summarization, code, and extraction formats, while utility depends on validation and alignment with the target distribution.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C6

**Claim**

Synthetic-data use can make evaluation misleading if synthetic test cases are used without independent validation: benchmark scores may not reflect real-world reliability, and benchmark contamination or saturation can obscure failures.

- S4 supports (direct): Presents synthetic evaluation cases for edge, adversarial, boundary, and failure-mode testing, while stating that validation is critical to synthetic-data utility.
- S5 supports (direct): States that benchmark scores alone can be inadequate because of saturation, contamination, and leakage, and recommends realistic evaluation for reliability, fairness, reproducibility, and safety.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C7

**Claim**

The supplied sources do not provide empirical, subgroup-level evidence sufficient to determine whether synthetic data introduces, amplifies, reduces, or conceals demographic, linguistic, or cultural bias relative to human-generated or mixed data.

- No new evidence relationship was added.

**Confidence:** HIGH

**Status:** INSUFFICIENT_EVIDENCE

### New Claim C8

**Claim**

The supplied sources do not establish that synthetic records reliably satisfy privacy requirements; they describe privacy preservation as a use case while also noting that governance, lineage, fidelity metadata, and re-identification risk require attention.

- S4 supports (direct): Describes synthetic healthcare and financial records as a potential way to remove direct links to individuals.
- S1 supports (direct): Frames privacy substitution as a distinct use case and notes that GDPR-related re-identification concerns remain relevant.
- S2 supports (direct): States that ungoverned synthetic data creates audit gaps and that lineage and fidelity metadata are necessary.

**Confidence:** MEDIUM

**Status:** WEAK

### New Gap G1

Comparative empirical evidence is needed on demographic, linguistic, cultural, and other subgroup bias in models trained or fine-tuned with synthetic, human-generated, and mixed data, including how prompting and filtering affect outcomes.

### New Gap G2

Evidence is insufficient to distinguish the effects of synthetic pretraining from synthetic fine-tuning across factuality, transfer, distribution shift, robustness, and model-collapse risk.

### New Gap G3

Independent evaluation designs and real-world deployment studies are needed to determine whether synthetic benchmark and edge-case results predict factuality, safety, calibration, robustness, and failure rates outside controlled tests.

### New Gap G4

Formal privacy evaluations, including memorization and re-identification testing, are needed before treating LLM-generated synthetic data as a privacy-preserving substitute for sensitive human data.

---

## 4. Current Research State

- Claims: 8
- Supported: 6
- Weak: 1
- Conflicting: 0
- Insufficient Evidence: 1
- Open Gaps: 4
- Remaining Searches: 2

### Subquestion Progress

**SQ1:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** UNRESEARCHED → PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ3:** UNRESEARCHED → PARTIAL

Reason: At least one linked ledger claim is not yet supported.

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

## 5. Independent Verification

### V1 — Claim C2

**Phase:** INITIAL

**Evidence source IDs:** S1, S2, S5

**Verdict:** NEEDS_QUALIFICATION

**Reason**

The supplied evidence supports that recursive training in a replacement regime can produce model collapse, including loss of low-probability and diverse distributional regions and compounding errors. However, the claim should make clear that this risk is associated primarily with indiscriminate or predominantly synthetic recursive training, not synthetic data use generally; additive use with retained real data is presented as a mitigating condition.

**Missing assumptions**

- Synthetic outputs substantially replace rather than supplement real data.
- The generated data are used recursively across model generations without sufficient fresh real data, external validation, or quality filtering.
- The claim concerns a documented risk under particular training regimes, not an inevitable outcome of all synthetic-data training.

**Source concerns**

- The evidence is largely from secondary industry or explainer sources rather than the cited primary studies themselves.
- The quantitative and analytical claims attributed to Shumailov et al. and Gerstgrasser et al. cannot be independently assessed from the supplied excerpts.
- The sources are future-dated and include vendor- or practitioner-oriented summaries, which may overstate generalizability.

**Counter-search status:** EXECUTED

**Counter-search query:**

> Find independent primary studies and replications testing recursive synthetic-data training in LLMs, especially conditions that prevent or weaken model collapse, including mixtures retaining real data, quality filtering, deduplication, fresh external data, and fine-tuning rather than pretraining.

**Counter-search evidence:** S6, S7, S8, S9, S10

---

## 6. Research Decision

**Decision:** Continue researching.

**Origin:** VERIFIER_COUNTERSEARCH

**Target:** CLAIM C2

**Why**

Independent verification of C2 identified a high-value falsification search: The supplied evidence supports that recursive training in a replacement regime can produce model collapse, including loss of low-probability and diverse distributional regions and compounding errors. However, the claim should make clear that this risk is associated primarily with indiscriminate or predominantly synthetic recursive training, not synthetic data use generally; additive use with retained real data is presented as a mitigating condition.

**Next Search**

> Find independent primary studies and replications testing recursive synthetic-data training in LLMs, especially conditions that prevent or weaken model collapse, including mixtures retaining real data, quality filtering, deduplication, fresh external data, and fine-tuning rather than pretraining.


---

# Iteration 2

## 1. Search

**Query**

> Find independent primary studies and replications testing recursive synthetic-data training in LLMs, especially conditions that prevent or weaken model collapse, including mixtures retaining real data, quality filtering, deduplication, fresh external data, and fine-tuning rather than pretraining.

**Target:** C2

**Purpose:** COUNTERSEARCH

**Why this query**

Independent verification of C2 identified a high-value falsification search: The supplied evidence supports that recursive training in a replacement regime can produce model collapse, including loss of low-probability and diverse distributional regions and compounding errors. However, the claim should make clear that this risk is associated primarily with indiscriminate or predominantly synthetic recursive training, not synthetic data use generally; additive use with retained real data is presented as a mitigating condition.

5 result(s) retrieved; 5 new unique source(s) added.

- **S6 — Model Collapse via Synthetic Training Data**
  URL: https://www.emergentmind.com/topics/model-collapse-through-synthetic-training-data
- **S7 — How to Generate Synthetic Training Data for LLM Fine-Tuning (2026 Guide) - Plushcap**
  URL: https://plushcap.com/content/prem-ai/blog/prem-ai-how-to-generate-synthetic-training-data-for-llm-fine-tuning-2026-guide
- **S8 — Mixing Synthetic and Real Data for Pretraining**
  URL: https://apxml.com/courses/synthetic-data-llm-pretrain-finetune/chapter-3-synthetic-data-llm-pretraining-application/blending-synthetic-real-data
- **S9 — Synthetic Data Generation for Fine-Tuning: Using LLMs**
  URL: https://callsphere.tech/blog/synthetic-data-generation-fine-tuning-llms-training-data
- **S10 — Synthetic Data Generation for Agentic AI | Use Case | NVIDIA**
  URL: https://gretel.ai/blog/addressing-concerns-of-model-collapse-from-synthetic-data-in-ai

**Search Duration:** 4.67s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 6
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 17.72s

---

## 3. Ledger Updates

### New Claim C9

**Claim**

For synthetic fine-tuning data, generation alone is insufficient: practical pipelines commonly require quality filtering, validation, and deduplication before training, followed by held-out evaluation or regression testing.

- S9 supports (direct): Describes raw LLM output as not training-ready and specifies filtering, validation, deduplication, and held-out evaluation as pipeline stages.
- S7 supports (indirect): Summarizes quality filtering using difficulty and model-judge measures, accuracy verification for regulated domains, and final model evaluation.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C2

**Claim**

Replacing real training data with recursively generated synthetic data can cause model collapse: successive models lose low-probability and diverse parts of the original distribution, and errors can compound across generations.

- S6 supports (direct): Defines recursive retraining on model outputs as causing diversity loss, amplified errors and biases, tail depletion, and increased test error, especially when synthetic data replaces real data.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C3

**Claim**

Model-collapse risk is context-dependent rather than an inherent consequence of every use of synthetic data: the supplied evidence favors accumulating synthetic data alongside real data, with deduplication and quality filtering, over replacing real data entirely.

- S6 supports (direct): Contrasts full replacement with accumulation and accumulate-subsample regimes, reporting bounded error or slower bounded drift when real data is retained and collapse is mitigated through filtering and mixing.
- S8 supports (indirect): Describes blending synthetic text with existing data as a common strategy and emphasizes maintaining quality and coherence across the blended sources.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

Synthetic data can provide practical benefits by scaling scarce task-specific examples, targeting rare or underrepresented cases, supporting privacy-sensitive development, and accelerating prototyping.

- S7 supports (indirect): Identifies cost-effectiveness and efficiency relative to human annotation as benefits of synthetic fine-tuning data, while noting the need for quality control.
- S10 supports (direct): Presents synthetic data as a way to address scarce, siloed or sensitive domain data, reduce manual collection and labeling costs, and support low-resource languages, rare edge cases and specialized agentic systems.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

Synthetic data generation procedures can improve apparent diversity and coverage through controlled variation of audiences, formats, classes, or edge cases, but generated data remains dependent on the source model's learned distribution and validation quality.

- S9 supports (direct): Notes that LLMs tend to produce similar outputs across different seeds and recommends aggressive exact and fuzzy deduplication; it also describes seed variation and domain prompts for generating diverse examples.
- S10 supports (direct): States that seeding generation with real-world data and configuring structured fields can help preserve domain patterns and characteristics, with preview-based iteration and quality evaluation.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C6

**Claim**

Synthetic-data use can make evaluation misleading if synthetic test cases are used without independent validation: benchmark scores may not reflect real-world reliability, and benchmark contamination or saturation can obscure failures.

- S9 supports (direct): Recommends held-out evaluation and regression suites after synthetic-data fine-tuning, indicating that generation-time checks should not substitute for model-level evaluation.
- S10 supports (indirect): Recommends preview validation, automated quality metrics, LLM-based judges, and side-by-side comparison of models for targeted evaluation and benchmarking.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C8

**Claim**

The supplied sources do not establish that synthetic records reliably satisfy privacy requirements; they describe privacy preservation as a use case while also noting that governance, lineage, fidelity metadata, and re-identification risk require attention.

- S10 supports (indirect): Markets a synthesizer as producing privacy-safe versions of sensitive data with configurations designed for HIPAA and GDPR, while the supplied material provides no formal re-identification or memorization results.
- S7 supports (indirect): Acknowledges the need for accuracy verification and production quality control in enterprise fine-tuning, but supplies no formal privacy guarantee or re-identification evaluation.

**Confidence:** MEDIUM → MEDIUM

**Status:** WEAK → WEAK

---

## 4. Current Research State

- Claims: 9
- Supported: 7
- Weak: 1
- Conflicting: 0
- Insufficient Evidence: 1
- Open Gaps: 4
- Remaining Searches: 1

### Subquestion Progress

**SQ1:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ3:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ4:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → PARTIAL (targeted searches: 0)
- SQ3 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- SQ4 → PARTIAL (targeted searches: 0)

**Remaining targeted searches:** 1

---

## 5. Independent Verification

### V2 — Claim C2

**Phase:** POST_COUNTERSEARCH

**Evidence source IDs:** S1, S2, S5, S6

**Verdict:** VERIFIED

**Reason**

The supplied evidence consistently supports that recursive training in a full-replacement regime can degrade models by amplifying approximation errors and depleting rare or low-probability modes, reducing diversity across generations. The claim is appropriately conditional (“can cause”) rather than universal.

**Missing assumptions**

- The effect depends on the training regime, especially whether real data is discarded or retained, the synthetic-to-real ratio, sampling/decoding method, filtering, and data aggregation protocol.
- “Model collapse” should refer to degradation relative to the original data distribution, not necessarily complete convergence to a single output or failure in every benchmark.
- The cited findings may not generalize uniformly from theoretical, simulated, or smaller-model experiments to all LLM pretraining and fine-tuning settings.

**Source concerns**

- The strongest evidence is presented indirectly through secondary websites and summaries rather than the underlying peer-reviewed papers or released experimental data.
- S1 and S2 are future-dated practitioner/editorial sources and include vendor- or author-stated figures that are not independently established in the supplied excerpts.
- S6 is an aggregator overview and contains highly broad theoretical claims whose applicability to practical LLM training is not demonstrated by the excerpt itself.

**Counter-search status:** NOT_REQUESTED

**Reconciliation**

Confidence: HIGH → HIGH

Status: SUPPORTED → SUPPORTED

---

## 6. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ2

**Why**

SQ2 remains a CORE subquestion with a high-priority unresolved gap: the current evidence lacks empirical subgroup-level comparisons of bias in models trained or fine-tuned with synthetic versus human-generated or mixed data. One focused search could materially improve the answer by finding comparative studies and evidence on prompting or filtering effects.

**Next Search**

> Find independent empirical studies comparing demographic, linguistic, or cultural bias in LLMs trained or fine-tuned with synthetic versus human-generated or mixed data, including how prompting, filtering, or synthetic-data generation affects subgroup performance and harms.


---

# Iteration 3

## 1. Search

**Query**

> Find independent empirical studies comparing demographic, linguistic, or cultural bias in LLMs trained or fine-tuned with synthetic versus human-generated or mixed data, including how prompting, filtering, or synthetic-data generation affects subgroup performance and harms.

**Target:** SQ2

**Purpose:** SUBQUESTION

**Why this query**

SQ2 remains a CORE subquestion with a high-priority unresolved gap: the current evidence lacks empirical subgroup-level comparisons of bias in models trained or fine-tuned with synthetic versus human-generated or mixed data. One focused search could materially improve the answer by finding comparative studies and evidence on prompting or filtering effects.

5 result(s) retrieved; 5 new unique source(s) added.

- **S11 — WEIRD Bias: Western Over-representation in LLM Training Data | Synthetic Audiences Research**
  URL: https://cyberarctica.com/synthetic-audiences/05_weird_bias_western_over-representation_in_llm_training_data.html
- **S12 — The Impact of Synthetic Data Diversity on LLM Fine-Tuning**
  URL: https://arxiv.org/html/2511.01490v1
- **S13 — [PDF] Investigating and Mitigating Undesirable Biases in Large ...**
  URL: https://ojs.aaai.org/index.php/AAAI/article/view/35214/37369
- **S14 — Bias in Large Language Models: Origin, Evaluation, and Mitigation**
  URL: https://www.mdpi.com/2079-9292/15/9/1824
- **S15 — Data bias in LLM and generative AI applications**
  URL: https://mostly.ai/blog/data-bias-types

**Search Duration:** 3.21s

---

## 2. Evidence Processing

- New claim proposals: 2
- Existing claim updates: 4
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 16.78s

---

## 3. Ledger Updates

### New Claim C10

**Claim**

In supervised fine-tuning experiments, increasing the diversity of synthetic-data sources can mitigate distribution collapse and preserve output-text diversity; however, synthetic fine-tuning may reduce adversarial robustness while preserving output quality, creating outputs that remain usable but potentially easier to misuse. Human fine-tuning reportedly reduces both output quality and adversarial robustness, while multi-source synthetic data is less effective than human data at reducing self-preference bias.

- S12 supports (direct): Reports experiments in which higher synthetic-source diversity mitigated distribution collapse and preserved output diversity; synthetic fine-tuning decreased adversarial robustness while preserving output quality; human data was most effective at reducing self-preference bias, followed by multi-source synthetic data.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C11

**Claim**

Synthetic-data generation cannot be assumed to correct representational bias: models and synthetic personas may inherit or reproduce Western, English-language, majority-group, demographic, cultural, and occupational skews from their source models and training distributions, particularly for low-resource languages and underrepresented populations.

- S11 supports (direct): Reports Western and English-language over-representation, poorer performance for several non-Western and low-resource contexts, preference for majority/WEIRD personas, under-representation of some demographic and occupational groups, and cultural-alignment disparities in LLM-generated synthetic audiences.
- S13 supports (indirect): Reports measured social, cultural, persona, nationality, and low-resource-language biases in LLM outputs, including preferences for Western European nations and variation across demographic personas.
- S15 supports (indirect): Explains that nonrepresentative training data can produce selection bias and suggests synthetic rebalancing, while also warning that generated-data feedback loops can reduce quality.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C7

**Claim**

The supplied sources do not provide empirical, subgroup-level evidence sufficient to determine whether synthetic data introduces, amplifies, reduces, or conceals demographic, linguistic, or cultural bias relative to human-generated or mixed data.

- S11 supports (direct): Provides subgroup- and language-specific observations of Western/English over-representation, poorer performance in several non-Western and low-resource contexts, and demographic and occupational representation gaps in generated personas; these findings document relevant bias mechanisms but do not compare models fine-tuned on synthetic versus human or mixed data.
- S12 supports (direct): Reports comparative fine-tuning results for human and synthetic data on self-preference bias, but does not provide demographic, linguistic, or cultural subgroup disparity measurements.
- S13 supports (indirect): Reports social, cultural, persona, nationality, and low-resource-language bias evaluations in LLMs, but not comparative synthetic-data training effects.
- S14 supports (indirect): Provides a review framework covering bias origins, evaluation, and mitigation, but the supplied excerpt does not establish comparative outcomes for synthetic versus human-generated training data.

**Confidence:** HIGH → HIGH

**Status:** INSUFFICIENT_EVIDENCE → INSUFFICIENT_EVIDENCE

### Updated Claim C2

**Claim**

Replacing real training data with recursively generated synthetic data can cause model collapse: successive models lose low-probability and diverse parts of the original distribution, and errors can compound across generations.

- S12 supports (direct): Reports that synthetic fine-tuning affects multiple measures of distribution collapse and that greater diversity among synthetic sources mitigates collapse and preserves output diversity.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

Synthetic data generation procedures can be designed to increase variation and target underrepresented formats, classes, audiences, or edge cases. Whether this improves meaningful coverage depends on the prompts, source-model diversity, target distribution, and independent validation, because generated data inherits limitations and biases from the generating models and may exhibit distribution narrowing or other artifacts.

- S12 supports (direct): Finds that diversity across synthetic-data sources affects distribution collapse and linguistic/output diversity, with higher source diversity preserving broader output distributions.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C6

**Claim**

Synthetic-data use can make evaluation misleading if synthetic test cases are used without independent validation: benchmark scores may not reflect real-world reliability, and benchmark contamination or saturation can obscure failures.

- S12 supports (direct): Evaluates synthetic fine-tuning using distribution-collapse, linguistic-diversity, adversarial-robustness, output-quality, and self-preference measures, illustrating that benchmark or quality preservation alone can miss safety-relevant degradation.
- S13 supports (indirect): Describes subgroup-specific bias datasets and evaluations across social, cultural, persona, and low-resource-language dimensions, supporting the need for multidimensional and subgroup testing.
- S14 supports (indirect): Identifies bias evaluation as a distinct component of LLM assessment and mitigation, supporting evaluation beyond aggregate capability scores.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 11
- Supported: 9
- Weak: 1
- Conflicting: 0
- Insufficient Evidence: 1
- Open Gaps: 4
- Remaining Searches: 0

### Subquestion Progress

**SQ1:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ3:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ4:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → PARTIAL (targeted searches: 1)
- SQ3 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- SQ4 → PARTIAL (targeted searches: 0)

**Remaining targeted searches:** 0

---

## 5. Independent Verification

### V3 — Claim C5

**Phase:** INITIAL

**Evidence source IDs:** S1, S4, S9, S10, S12

**Verdict:** NEEDS_QUALIFICATION

**Reason**

The evidence supports that prompting and structured generation can target variation across formats, audiences, classes, and edge cases, and that synthetic data quality depends on validation and the generating model's learned distribution. However, the sources do not establish that such procedures reliably improve real-world diversity or coverage; apparent variation may coexist with distribution narrowing, source-model bias, or poor transfer. The arXiv study specifically indicates that source diversity can mitigate collapse, while single-source synthetic data has weaker outcomes on some measures.

**Missing assumptions**

- The target distribution and relevant coverage dimensions are explicitly defined.
- Generated examples are validated against independent real-world data and task-specific outcomes, not only surface-level diversity metrics.
- The generation process includes sufficient source, prompt, or model diversity to reduce dependence on one learned distribution.
- Synthetic examples transfer to deployment conditions without introducing systematic omissions or artifacts.

**Source concerns**

- S4 and S10 are practitioner/vendor sources and make broad benefit claims without presenting detailed independent evaluations.
- S12 is an arXiv preprint rather than a peer-reviewed publication, and its findings concern particular models, datasets, and fine-tuning settings.
- The supplied evidence provides limited direct measurement of factuality, demographic coverage, or real-world deployment transfer.

**Counter-search status:** NOT_REQUESTED

**Reconciliation**

Claim:

"Synthetic data generation procedures can improve apparent diversity and coverage through controlled variation of audiences, formats, classes, or edge cases, but generated data remains dependent on the source model's learned distribution and validation quality."
→
"Synthetic data generation procedures can be designed to increase variation and target underrepresented formats, classes, audiences, or edge cases. Whether this improves meaningful coverage depends on the prompts, source-model diversity, target distribution, and independent validation, because generated data inherits limitations and biases from the generating models and may exhibit distribution narrowing or other artifacts."

Confidence: HIGH → HIGH

Status: SUPPORTED → SUPPORTED

---

## 6. Research Decision

**Decision:** Stop researching.

**Origin:** BUDGET_STOP

**Why**

The maximum research iteration budget was reached.

**Stop Reason:** max_iterations


---

# Final Research Decision

**Stop Reason:** max_iterations

**Remaining Uncertainty**

- G1: Comparative empirical subgroup-bias studies across synthetic, human-generated, and mixed training data are needed, including effects of prompting and filtering.
- G2: Evidence is insufficient to distinguish synthetic pretraining from synthetic fine-tuning effects on factuality, transfer, distribution shift, robustness, and collapse risk.
- G3: Independent deployment-oriented studies are needed to test whether synthetic benchmarks and edge-case results predict real-world factuality, safety, calibration, robustness, and failure rates.
- G4: Formal memorization and re-identification evaluations are needed before treating synthetic data as a privacy-preserving substitute.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Question Decomposition | 1 | 6.06s |
| Tavily Search | 3 | 8.45s |
| Evidence Processing | 3 | 51.63s |
| Independent Verification | 3 | 20.25s |
| Research Decision | 1 | 3.30s |
| Report Generation | 1 | 14.87s |
| Total Run | — | 104.58s |

# Verifier Diagnostics

- Verification calls: 3
- Claims verified: 2
- VERIFIED verdicts: 1
- NEEDS_QUALIFICATION verdicts: 2
- CONTRADICTED verdicts: 0
- INSUFFICIENT_EVIDENCE verdicts: 0
- Counter-searches requested: 1
- Counter-searches executed: 1
- Counter-searches blocked by budget: 0
- Counter-searches blocked as duplicates: 0
- Claims whose wording changed: 1
- Claims whose confidence decreased: 0
- Claims whose status changed: 0
- Searches allocated to general research: 1
- Searches allocated to subquestions: 1
- Searches allocated to counter-search: 1
