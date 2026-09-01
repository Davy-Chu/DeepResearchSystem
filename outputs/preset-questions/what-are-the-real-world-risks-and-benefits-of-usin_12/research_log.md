# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

**Status:** Completed

**Stop Reason:** no_search_results

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 6 / 10

**Unique Sources:** 22

**OpenAI Calls:** 7

**Tavily Calls:** 6

**Started:** 2026-09-01T06:34:36-04:00

**Ended:** 2026-09-01T06:36:41-04:00

**Total Runtime:** 125.77s

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

- **S1 — Synthetic Data for AI Training: Use Cases and Risks [2026]**
  URL: https://atlan.com/know/ai-agent/data-for-ai/synthetic-data-for-ai-training
- **S2 — Synthetic Data for LLM Training: Decision Guide 2026**
  URL: https://www.digitalapplied.com/blog/synthetic-data-generation-llm-training-decision-guide-2026
- **S3 — Synthetic Data Generation with LLMs: Techniques and Use Cases**
  URL: https://tetrate.io/learn/ai/synthetic-data-generation-llms
- **S4 — Synthetic Data for ML: Uses, Risks, and Best Practices | CleverX Blog**
  URL: https://cleverx.com/blog/synthetic-data-for-ml-the-game-changer-in-training-for-2025
- **S5 — Large Language Models Are Still Getting Stronger, but Researchers Face New Bottlenecks in Data, Evaluation, and Safety | Newswise**
  URL: https://www.newswise.com/articles/large-language-models-are-still-getting-stronger-but-researchers-face-new-bottlenecks-in-data-evaluation-and-safety

**Search Duration:** 0.54s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data can reduce data scarcity, annotation cost, privacy constraints, and class imbalance, and can provide targeted coverage of rare or edge cases.

**Confidence:** Medium

**Why this confidence level**

The benefit is consistently described across multiple sources, but the retrieved evidence is primarily practitioner and industry material rather than independent comparative studies.

**Evidence**

- Sources describe synthetic data as a way to expand limited labeled datasets, reduce collection and labeling costs, support privacy-sensitive work, and generate underrepresented classes or difficult edge cases. [S1] [S3] [S4]

#### Finding 2

**Claim**

Synthetic data is most useful as a supplement to, rather than a replacement for, real data.

**Confidence:** Medium

**Why this confidence level**

The sources agree on the direction of the risk and cite academic work, but the retrieved content does not provide the underlying papers in full or enough detail to independently assess their experimental scope.

**Evidence**

- The decision guide contrasts successful curated synthetic-data regimes with degradation from fully synthetic self-training, and reports that retaining or accumulating real data limits model-collapse risk. [S2]
- Atlan warns that recursive training on synthetic outputs can narrow the learned distribution and degrade outputs. [S1]

#### Finding 3

**Claim**

A central data-quality risk is distributional narrowing or model collapse when generated data is repeatedly reused without sufficient real, novel, or externally verified information.

**Confidence:** Medium

**Why this confidence level**

Multiple sources identify the same mechanism, but the quantitative results are reported second-hand in the retrieved material and may depend strongly on the generation and mixing regime.

**Evidence**

- The guide describes successive generations losing low-probability but valid examples and reports substantial perplexity degradation in a purely synthetic OPT-125m regime. [S2]
- The news summary says repeated training on model-generated content can cause capability stagnation or degradation, especially without reliable external feedback. [S5]

#### Finding 4

**Claim**

Synthetic data can improve task-specific performance when it is carefully curated, filtered, deduplicated, and aligned with the target task; sheer volume is not sufficient.

**Confidence:** Medium

**Why this confidence level**

The sources provide plausible examples and operational guidance, but the strongest performance figures are vendor-stated or industry-reported rather than independently replicated here.

**Evidence**

- The guide attributes Phi-1's reported coding performance to curated synthetic textbooks and exercises combined with real web data, and highlights deduplication and quality filtering in Cosmopedia. [S2]
- The practitioner sources emphasize that utility depends on validation, generation technique, and alignment between the synthetic and target distributions. [S3] [S4]

#### Finding 5

**Claim**

Synthetic data does not automatically remove bias; generators can reproduce, amplify, or introduce bias and may still underrepresent demographics or rare populations.

**Confidence:** Medium

**Why this confidence level**

The risk is directly stated by multiple sources, but the retrieved material does not quantify bias changes or establish which mitigation methods work across LLM tasks.

**Evidence**

- CleverX explicitly identifies bias amplification and demographic underrepresentation as risks, while Tetrate presents class-balancing as a potential benefit that requires alignment with the target distribution. [S3] [S4]
- The news summary lists biased information and poor data mixture design among factors affecting model quality and deployment risk. [S5]

#### Finding 6

**Claim**

Evaluation should combine automated statistical and task metrics with human review and testing on trusted real-world data, edge cases, fairness slices, and realistic workflows.

**Confidence:** Medium

**Why this confidence level**

There is convergent guidance on multi-dimensional evaluation, but no retrieved source supplies a validated standard protocol or direct evidence comparing synthetic versus human-authored evaluation sets.

**Evidence**

- CleverX recommends comparing synthetic data with real data using accuracy, diversity, realism, visualization, statistical analysis, and human evaluation, and says trained models should be benchmarked against trusted real-world ground truth. [S4]
- Tetrate describes synthetic evaluation sets for ambiguity, multi-turn context, decision boundaries, adversarial cases, and failure modes. [S3]
- Newswise warns that static benchmarks can be saturated or contaminated and may not predict reliability in complex real-world, tool-using, or agentic tasks. [S5]

#### Finding 7

**Claim**

Synthetic evaluation data creates a distinct risk of misleading evaluation if it is too similar to the generator's assumptions, contaminated, overfit, or insufficiently representative of real users and failures.

**Confidence:** Medium

**Why this confidence level**

The concern follows directly from the evaluation limitations described by the sources, but the retrieved material does not present a controlled study specifically measuring synthetic-evaluation bias.

**Evidence**

- The sources recommend real-world benchmarking and warn that conventional benchmarks can suffer from contamination, leakage, saturation, and weak correlation with realistic reliability; Tetrate emphasizes deliberately generated edge and adversarial cases rather than relying on routine examples. [S3] [S4] [S5]

### Conflicts Found

- The sources differ in how broadly they characterize synthetic data's performance benefits. S2 presents strong positive examples and labels carefully curated additive regimes as very low risk, while S1, S4, and S5 emphasize degradation, realism gaps, bias, and the need for real-data validation. This is a conditional disagreement: outcomes depend on curation, filtering, real-data retention, and evaluation regime. [S1] [S2] [S4] [S5]
- S3 describes privacy-oriented synthetic data as potentially preserving useful patterns without direct links to individuals, whereas S2 notes that privacy substitution remains conditional and that re-identification and legal/compliance questions must be checked. The retrieved sources do not establish that synthetic data is inherently anonymous. [S2] [S3]

### Important Gaps

- How much synthetic data can be mixed with real data before performance, diversity, or fairness materially deteriorates for different LLM tasks and model sizes?
- Do synthetic examples improve subgroup fairness when the generator itself inherits demographic or cultural biases, and which auditing or reweighting methods are effective?
- What independent, reproducible studies compare synthetic and human-authored fine-tuning data on real-world generalization, hallucination, calibration, and safety?
- How often do synthetic evaluation sets fail to predict deployment performance, especially for long-context, tool-use, and agentic tasks?
- What privacy guarantees and disclosure or re-identification tests are required before synthetic text can responsibly substitute for sensitive data?

**Analysis Duration:** 19.81s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The current evidence supports a conditional benefits-and-risks answer, but it is dominated by blogs and a secondary news summary. The most important gaps concern independent primary evidence on bias, privacy, real-world generalization, and the validity of synthetic evaluation sets.

**Next Search**

> peer-reviewed study synthetic data LLM fine-tuning bias real-world generalization evaluation model collapse

---

# Iteration 2

## 1. Search

**Query**

> peer-reviewed study synthetic data LLM fine-tuning bias real-world generalization evaluation model collapse

**Why this query**

The current evidence supports a conditional benefits-and-risks answer, but it is dominated by blogs and a secondary news summary. The most important gaps concern independent primary evidence on bias, privacy, real-world generalization, and the validity of synthetic evaluation sets.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S6 — Why 2026 is the Year Synthetic Data Becomes Non- ...**
  URL: https://pub.towardsai.net/why-2026-is-the-year-synthetic-data-becomes-non-negotiable-b5a2a84d1b1b
- **S7 — The Impact of Synthetic Data Diversity on LLM Fine-Tuning - arXiv**
  URL: https://arxiv.org/html/2511.01490v1
- **S8 — GitHub - ahmad-alismail/LLM_based_Synthetic_Data_Generation: A curated and continuously updated collection of papers, tools, and datasets on synthetic data generation using LLMs and agentic workflows. · GitHub**
  URL: https://github.com/ahmad-alismail/LLM_based_Synthetic_Data_Generation
- **S9 — Synthetic Data & Distillation - Nathan Lambert**
  URL: https://rlhfbook.com/c/12-synthetic-data

**Search Duration:** 3.92s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data can substantially reduce the cost and difficulty of producing instruction-tuning and post-training data, particularly when generated by a stronger model for a weaker model.

**Confidence:** Medium

**Why this confidence level**

The source provides a coherent account and examples, but it is a tutorial-style secondary source rather than an independent comparative evaluation of all claimed benefits.

**Evidence**

- Synthetic data is described as cheaper and easier to iterate on than human data, and as supporting generated prompts, completions, preference data, feedback, and filtering. The source reports prominent synthetic datasets used for instruction tuning, preference optimization, and reasoning tasks. [S9]

#### Finding 2

**Claim**

Synthetic-data diversity is an important quality-control variable: using multiple generation sources can mitigate distribution collapse more effectively than relying on one source model.

**Confidence:** Medium

**Why this confidence level**

The evidence is directly relevant and includes an empirical preprint plus convergent practical guidance, but the reported findings may depend on the studied models, tasks, and definitions of collapse.

**Evidence**

- The arXiv study reports that higher diversity in synthetic-data sources mitigated several measures of distribution collapse and preserved broader output and linguistic diversity, including experiments involving Llama-3.1-70B. [S7]
- The tutorial identifies single-model, repetitive, unfiltered self-training as the regime most associated with collapse and recommends diverse teachers, real-data mixing, deduplication, and quality filtering. [S9]

#### Finding 3

**Claim**

Synthetic fine-tuning can create safety and robustness risks even when ordinary output quality remains high.

**Confidence:** Medium

**Why this confidence level**

This is a direct experimental claim from a relevant research paper, but the retrieved material is an abstract and partial text, so the exact evaluation setup and external validity cannot be fully assessed.

**Evidence**

- The arXiv study reports that synthetic fine-tuning decreased adversarial robustness while preserving higher output quality; it also reports that both human and synthetic fine-tuning could remove safeguards, with synthetic data potentially leaving outputs more usable and therefore more dangerous. [S7]
- The study specifically examines accidental weakening of safety guardrails as a downstream effect of fine-tuning, rather than treating benchmark performance as sufficient evidence of safety. [S7]

#### Finding 4

**Claim**

Fine-tuning with synthetic data may reduce self-preference bias, but single-source synthetic data appears less effective than multi-source synthetic data, and both are less effective than human data in the reported study.

**Confidence:** Medium

**Why this confidence level**

The finding is explicitly reported, but it comes from one study and addresses a specific bias in LLM-as-judge settings rather than demographic or societal bias generally.

**Evidence**

- The paper reports that fine-tuning reduced self-preference bias, with human data producing the strongest reduction, followed by multi-source synthetic data, and single-source synthetic data the weakest reduction. [S7]

#### Finding 5

**Claim**

Human data remains especially important for establishing ground truth, evaluating frontier capabilities, and tasks where synthetic generators are not reliably better than people.

**Confidence:** Medium

**Why this confidence level**

The sources converge on a human-plus-synthetic evaluation strategy, but the tutorial's broad claims about where models exceed human reliability are not independently established in the retrieved material.

**Evidence**

- The tutorial distinguishes instruction data, where synthetic generation is portrayed as highly effective, from preference data and evaluation, where human data remains important; it states that underlying evaluation benchmarks and ground-truth labels still require human creation. [S9]
- The prior evidence likewise recommends benchmarking against trusted real-world data and human review rather than relying solely on synthetic evaluation sets. [S3] [S4] [S5]

#### Finding 6

**Claim**

Synthetic evaluation can be scalable and controlled, but it should not be treated as a substitute for human-authored ground truth or realistic deployment testing.

**Confidence:** Medium

**Why this confidence level**

The operational advantage and evaluation caveat are consistently supported, but S8 is a repository and survey index rather than primary evidence, and no controlled comparison of synthetic versus human evaluation sets was retrieved.

**Evidence**

- The survey repository describes synthetic data as useful for controlled, diverse, scalable benchmark creation, while its listed benchmark survey emphasizes dynamic evaluation to address contamination. The tutorial states that synthetic scoring can scale, but benchmark foundations and ground-truth labels still require human involvement. [S8] [S9]
- Earlier sources warn that synthetic or static benchmarks can be contaminated, saturated, overfit, or weakly predictive of real-world tool-use and agentic reliability. [S3] [S4] [S5]

#### Finding 7

**Claim**

The strongest overall conclusion is conditional: synthetic data is beneficial when it is diverse, filtered, deduplicated, mixed with real or externally grounded data, and evaluated against trusted real-world criteria; unfiltered single-model recycling creates substantial quality and safety risks.

**Confidence:** High

**Why this confidence level**

The central conditional conclusion is supported by multiple sources with complementary evidence and is consistent with the accumulated findings, although exact safe mixing ratios and domain-specific guarantees remain unknown.

**Evidence**

- The new empirical study links source diversity to reduced distribution collapse and examines robustness and self-preference effects. [S7]
- The tutorial recommends real-data mixing, diverse teachers, deduplication, and quality filters, while prior sources identify collapse, bias, realism gaps, and misleading evaluation as risks of poorly designed pipelines. [S1] [S2] [S3] [S4] [S5] [S9]

### Conflicts Found

- S9 presents a relatively optimistic view that modern frontier pipelines can use synthetic data at scale without the catastrophic regressions implied by strong model-collapse claims, whereas S2 and S5 emphasize degradation from recursive synthetic training. S7 partially reconciles the disagreement by showing that source diversity changes the collapse outcome. The disagreement is conditional on data mixture, source diversity, filtering, and whether the pipeline repeatedly recycles model outputs. [S2] [S5] [S7] [S9]
- S9 characterizes synthetic instruction data as often higher quality than human writing at scale, while the accumulated sources caution that synthetic quality depends on alignment, filtering, realism, and validation. This is not a direct contradiction about all synthetic data; it reflects different task and pipeline conditions. [S1] [S3] [S4] [S9]
- S7 reports that synthetic fine-tuning can preserve output quality while reducing adversarial robustness, whereas ordinary task benchmarks may show acceptable or improved performance. Thus benchmark gains and safety robustness can move in opposite directions. [S3] [S5] [S7]

### Important Gaps

- How reproducible are S7's diversity, adversarial-robustness, and self-preference findings across domains, model families, data sizes, and fine-tuning objectives?
- What synthetic-to-real mixing ratios and source-diversity levels reliably prevent distribution narrowing for different LLM tasks?
- Does synthetic data improve or worsen demographic, cultural, and linguistic subgroup fairness when the generator inherits biases from its training data?
- How often do synthetic evaluation sets fail to predict deployment behavior, especially for long-context, tool-use, agentic, and safety-critical applications?
- What independent tests establish factuality, calibration, provenance, contamination resistance, and privacy properties of synthetic text?
- Are the broad data-scarcity and internet-exhaustion claims in S6 independently supported by primary sources? The retrieved excerpt is advocacy-oriented and includes claims that cannot be verified from the excerpt alone.

**Analysis Duration:** 16.98s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The accumulated evidence now supports a responsible high-level answer, especially on conditional benefits, collapse, source diversity, and evaluation design. However, an important original focus—bias—remains weakly answered: the new study addresses self-preference bias, not demographic or societal bias. Independent comparative evidence on real-world generalization, fairness, and synthetic evaluation validity would materially improve the answer.

**Next Search**

> independent empirical study synthetic versus human data LLM fine-tuning demographic bias fairness real-world evaluation

---

# Iteration 3

## 1. Search

**Query**

> independent empirical study synthetic versus human data LLM fine-tuning demographic bias fairness real-world evaluation

**Why this query**

The accumulated evidence now supports a responsible high-level answer, especially on conditional benefits, collapse, source diversity, and evaluation design. However, an important original focus—bias—remains weakly answered: the new study addresses self-preference bias, not demographic or societal bias. Independent comparative evidence on real-world generalization, fairness, and synthetic evaluation validity would materially improve the answer.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S10 — Synthetic Data for Bias Mitigation 2026: 5 Methods + FAGI**
  URL: https://futureagi.com/blog/synthetic-data-generation-bias-2025
- **S11 — Fairness in AI Decisions About People: Evidence from LLM ...**
  URL: https://manhattan.institute/article/fairness-in-ai-decisions-about-people-evidence-from-llm-experiments
- **S12 — Fairness by design: End-to-end bias evaluation for LLM-generated data**
  URL: https://resources.flatiron.com/publications/fairness-by-design-end-to-end-bias-evaluation-for-llm-generated-data
- **S13 — LLMs Are Not a Silver Bullet: A Case Study on Software Fairness**
  URL: https://arxiv.org/html/2604.12640v1
- **S14 — Measuring stereotype and deviation biases in large language models**
  URL: https://www.nature.com/articles/s41598-026-52923-8

**Search Duration:** 1.95s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data can target documented coverage gaps and underrepresented subgroups, but fairness improvement is conditional on auditing, validation, and real-plus-synthetic retraining.

**Confidence:** Medium

**Why this confidence level**

The workflow is clearly described, but S10 is vendor-authored guidance rather than an independent comparative study demonstrating that the workflow reliably improves fairness.

**Evidence**

- S10 proposes an audit-diagnose-generate-validate-retrain-re-audit workflow, using targeted examples for underrepresented slices and requiring distributional-fit, utility, privacy, and held-out fairness checks. [S10]
- This supports the existing finding that synthetic data can address class imbalance and rare cases, while adding an explicit closed-loop fairness process rather than assuming generated examples are corrective. [S10] [S3] [S4]

#### Finding 2

**Claim**

LLM-generated data can reproduce substantial stereotype and demographic-distribution biases, so synthetic data generation should itself be treated as a bias source requiring measurement.

**Confidence:** Medium

**Why this confidence level**

S14 is a peer-reviewed journal article and directly measures bias in generated content, but the retrieved abstract does not establish how the findings transfer to synthetic fine-tuning datasets or other generation prompts.

**Evidence**

- A Scientific Reports study reports that all four examined LLMs exhibited significant stereotype bias and deviation bias across multiple demographic groups when generating individual profiles and inferred attributes. [S14]
- The result strengthens the prior concern that a generator may reproduce or introduce demographic and cultural distortions rather than automatically produce balanced data. [S14] [S3] [S4]

#### Finding 3

**Claim**

Fairness evaluations can look substantially better on artificially balanced test sets than on realistic imbalanced distributions, creating a serious risk of overstating real-world performance.

**Confidence:** Medium

**Why this confidence level**

This is a large-scale empirical comparison on real-world tabular datasets, but it evaluates LLM-based bias mitigation rather than synthetic text fine-tuning specifically. The methodological lesson about evaluation realism is nevertheless directly relevant.

**Evidence**

- S13 reports that prior favorable LLM fairness results were largely driven by artificially balanced test data; under real-world imbalanced distributions, traditional ML methods outperformed LLM-based methods in both fairness and predictive performance. [S13]
- The study reports that balanced distributions improved measured fairness by 36.2%–138.4%, but cautions that these gains may not generalize to deployment. [S13]

#### Finding 4

**Claim**

A robust evaluation of LLM-generated or synthetic data should compare against human or trusted ground truth, include subgroup slices and realistic population distributions, and verify downstream outcomes rather than relying on aggregate benchmark scores.

**Confidence:** Medium

**Why this confidence level**

The sources provide convergent evaluation principles and one applied validation example, but no universal validated protocol or controlled comparison of synthetic versus human-authored LLM fine-tuning data.

**Evidence**

- S12 describes a three-part validation framework: comparison with human abstractors, consistency and plausibility checks, and replication of clinical outcomes in large cohorts; it found small subgroup differences despite broadly similar downstream results. [S12]
- S13 demonstrates why realistic imbalanced distributions matter, while earlier evidence recommends held-out real-world, edge-case, fairness, and workflow testing. [S13] [S3] [S4] [S5]

#### Finding 5

**Claim**

Synthetic-data benefits and risks remain highly dependent on whether generated examples reflect the deployment distribution; adding examples for a subgroup can improve nominal coverage while still introducing incorrect associations or unrealistic cases.

**Confidence:** High

**Why this confidence level**

The conditional relationship is supported by both empirical bias measurement and convergent evaluation guidance, although the magnitude of downstream effects varies by task and generator.

**Evidence**

- S10 recommends checking distributional fit and subgroup fairness before retraining, and S14 finds that LLM-generated profiles contain systematic stereotype and deviation biases. [S10] [S14]
- S3 and S4 likewise condition class balancing and targeted generation on alignment with the target distribution and validation against real data. [S3] [S4]

### Conflicts Found

- S10 presents targeted synthetic generation as a direct and practical way to close fairness gaps, whereas S13 finds that LLM-based fairness methods can underperform traditional ML methods and that apparent gains may depend on unrealistic balanced testing. These are conditional rather than absolute contradictions: targeted generation may help, but its benefit must be demonstrated on realistic distributions and against strong baselines. [S10] [S13]
- S12 reports broadly consistent downstream clinical outcomes between LLM-extracted and human-abstracted datasets despite small subgroup performance differences, while S14 reports significant stereotype and demographic-distribution biases in generated profiles. The findings concern different tasks—clinical extraction versus free-form profile generation—so they indicate task-dependent risk rather than a direct contradiction. [S12] [S14]

### Important Gaps

- Do targeted synthetic fine-tuning examples measurably improve demographic, cultural, or linguistic fairness on realistic deployment distributions, rather than only on balanced or synthetic tests?
- How do generator stereotype and deviation biases measured in S14 translate into downstream LLM behavior after fine-tuning?
- Which fairness, quality, and privacy checks best detect harmful synthetic examples before they enter a training mixture?
- How reproducible are the evaluation effects reported by S13 across text generation, instruction tuning, preference optimization, and agentic tasks?
- What mixing ratios, source diversity, and human-review levels are needed to preserve real-world calibration, robustness, and subgroup performance?

**Analysis Duration:** 14.59s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources materially strengthen the evaluation and bias portions of the answer, especially the danger of artificially balanced tests and the presence of generator bias. However, the most important remaining gap is direct, independent evidence on synthetic text used for LLM training or fine-tuning, measured on realistic real-world and subgroup outcomes. Existing evidence is mostly indirect, task-specific, or guidance-oriented.

**Next Search**

> empirical study synthetic text data LLM fine-tuning demographic fairness realistic imbalanced real-world evaluation

---

# Iteration 4

## 1. Search

**Query**

> empirical study synthetic text data LLM fine-tuning demographic fairness realistic imbalanced real-world evaluation

**Why this query**

The new sources materially strengthen the evaluation and bias portions of the answer, especially the danger of artificially balanced tests and the presence of generator bias. However, the most important remaining gap is direct, independent evidence on synthetic text used for LLM training or fine-tuning, measured on realistic real-world and subgroup outcomes. Existing evidence is mostly indirect, task-specific, or guidance-oriented.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S15 — [PDF] Advancing Algorithmic Fairness via Selectively Fine-Tuning Biased ...**
  URL: http://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_AIM-Fair_Advancing_Algorithmic_Fairness_via_Selectively_Fine-Tuning_Biased_Models_with_CVPR_2025_paper.pdf
- **S16 — Towards Understanding Bias in Synthetic Data for Evaluation**
  URL: https://www.alphaxiv.org/abs/2506.10301
- **S17 — Is Your Model Fairly Certain? Uncertainty-Aware Fairness ...**
  URL: https://machinelearning.apple.com/research/fairly-certain

**Search Duration:** 2.28s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data can improve fairness in a downstream model, but only when its quality, diversity, and domain alignment are actively controlled.

**Confidence:** Medium

**Why this confidence level**

S15 is a recent peer-reviewed CVPR paper with experiments, but it studies image classification rather than LLM training or fine-tuning, so transfer to language models is indirect.

**Evidence**

- The AIM-Fair study identifies low synthetic-data quality and domain/bias gaps between real and synthetic data as key obstacles. Its contextual generation and selective fine-tuning approach improved fairness while maintaining utility on CelebA and UTKFace, outperforming fully and partially fine-tuned alternatives. [S15]

#### Finding 2

**Claim**

Blindly fine-tuning on balanced synthetic data can improve nominal fairness while reducing overall utility because of the synthetic-to-real domain gap.

**Confidence:** Medium

**Why this confidence level**

The result is experimentally supported in two vision datasets, but its applicability to LLM fine-tuning and language-specific fairness metrics is uncertain.

**Evidence**

- S15 reports that models trained on balanced synthetic data showed better fairness but poorer accuracy, attributing the tradeoff to domain gaps and inadequate selective fine-tuning. [S15]
- The source further reports that selective layer-wise fine-tuning can preserve more utility while improving worst-group performance and equalized-odds measures. [S15]

#### Finding 3

**Claim**

Synthetic evaluation sets can introduce measurable systematic bias and overestimate system performance, even when they are useful for scalable comparisons.

**Confidence:** Medium

**Why this confidence level**

The source describes an empirical study using TREC data and statistical modeling, but the retrieved content is an alphaXiv-hosted summary rather than the primary paper text, and the findings concern information retrieval rather than general LLM evaluation.

**Evidence**

- The synthetic-test-collection study found that LLM-generated queries differed systematically from human queries, including query length and vocabulary patterns, and that GPT-4 relevance judgments were approximately 0.28 points higher on average than human judgments. [S16]
- The study reports that these query and judgment differences produced biased evaluation results; the effect could be substantial for estimating absolute performance, although it was less consequential for some relative system comparisons. [S16]

#### Finding 4

**Claim**

Synthetic evaluation may preserve some usefulness for ranking or comparing systems while remaining unreliable for absolute performance estimates.

**Confidence:** Medium

**Why this confidence level**

This is a direct reported result, but it is based on one IR setting, 82 queries, and particular generators and judging configurations.

**Evidence**

- S16 distinguishes significant bias in absolute performance estimates from a smaller effect on relative system comparisons. [S16]

#### Finding 5

**Claim**

Fairness evaluation should include uncertainty or confidence differences, not just accuracy-based group metrics.

**Confidence:** Medium

**Why this confidence level**

S17 is presented as an ICML paper and supplies a concrete metric and benchmark, but it does not directly test synthetic training data. Its relevance is to evaluating downstream effects that synthetic data might introduce.

**Evidence**

- S17 argues that conventional discrete fairness measures can miss cases where a model has similar accuracy across groups but is substantially more confident when making incorrect predictions for one group. Its UCerF metric is designed to capture this dimension, and its benchmark found such behavior in an open-source LLM. [S17]

#### Finding 6

**Claim**

Synthetic data designed to correct demographic imbalance can itself encode incorrect stereotypes or unrealistic demographic associations, so generated-data audits must measure both coverage and semantic correctness.

**Confidence:** High

**Why this confidence level**

The claim is supported by a peer-reviewed bias measurement study and a separate empirical fairness study, although neither directly quantifies the effect on LLM language fine-tuning.

**Evidence**

- S15 explicitly identifies bias shifts and low-quality or low-diversity generation as challenges even when the synthetic data is intended to be unbiased. [S15]
- The accumulated evidence finds systematic stereotype and demographic-distribution bias in LLM-generated profiles, reinforcing that nominal subgroup balancing does not establish unbiased content. [S14]

### Conflicts Found

- S15 presents synthetic data as capable of improving fairness while maintaining utility through controlled generation and selective fine-tuning, whereas earlier sources warn that synthetic balancing can create domain-shift losses or fail to improve fairness. These findings are conditional rather than directly contradictory: the outcome depends on generation quality, real-data alignment, model-update strategy, and evaluation distribution. [S3] [S10] [S13] [S15]
- S16 indicates that synthetic evaluation bias may have a limited effect on relative system rankings, while the accumulated evidence warns that synthetic or static benchmarks can be misleading for deployment reliability. Relative ranking in one IR experiment therefore should not be generalized to valid absolute or real-world evaluation. [S5] [S8] [S16]
- S17 emphasizes uncertainty-aware fairness metrics, while prior evidence often focuses on accuracy, equalized odds, or aggregate task performance. This is a measurement disagreement or limitation: conventional metrics may report acceptable fairness while missing unequal confidence or risk. [S13] [S15] [S17]

### Important Gaps

- How do the fairness and domain-gap effects observed in S15's vision experiments transfer to synthetic instruction tuning, preference optimization, and language-model behavior?
- Do synthetic evaluation biases like those reported in S16 systematically affect LLM safety, factuality, calibration, tool use, and agentic-task evaluation?
- Can uncertainty-aware metrics such as the approach in S17 detect harms caused by synthetic fine-tuning better than accuracy-only subgroup metrics?
- What independent studies compare human-authored and synthetic LLM fine-tuning data on realistic deployment distributions, calibration, hallucination, robustness, and subgroup outcomes?
- What source diversity, real-data mixing, and human-review levels are sufficient to prevent synthetic data from worsening domain shift or demographic bias?

**Analysis Duration:** 16.30s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources materially strengthen the evidence about evaluation bias, uncertainty-aware fairness, and the domain-gap mechanism, but they do not resolve the most important direct evidence gap: independent real-world comparisons of synthetic versus human data for LLM training or fine-tuning.

**Next Search**

> empirical study synthetic instruction tuning versus human data LLM real-world generalization calibration subgroup fairness

---

# Iteration 5

## 1. Search

**Query**

> empirical study synthetic instruction tuning versus human data LLM real-world generalization calibration subgroup fairness

**Why this query**

The new sources materially strengthen the evidence about evaluation bias, uncertainty-aware fairness, and the domain-gap mechanism, but they do not resolve the most important direct evidence gap: independent real-world comparisons of synthetic versus human data for LLM training or fine-tuning.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S18 — Instruction Tuning for Large Language Models: A Survey**
  URL: https://arxiv.org/html/2308.10792v5
- **S19 — How Effective is Synthetic Data and Instruction Fine-tuning ...**
  URL: https://aclanthology.org/2024.amta-research.8.pdf
- **S20 — Human data vs. synthetic data: What's the difference? | Label Studio**
  URL: https://labelstud.io/learning-center/human-data-vs-synthetic-data
- **S21 — Live LLM-Synthetic-Data Papers (Updated to July,2025)**
  URL: https://github.com/pengr/LLM-Synthetic-Data
- **S22 — High-Quality Synthetic Data Training for LLMs | Turin**
  URL: https://www.turing.com/services/llm-synthetic-data-training

**Search Duration:** 2.34s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Instruction tuning can improve controllability, instruction following, and domain adaptation efficiently, but its gains may be concentrated on behaviors represented in the instruction-tuning data rather than generalizing broadly.

**Confidence:** Medium

**Why this confidence level**

S18 is a literature survey and directly relevant to instruction tuning, but the retrieved excerpt summarizes prior work rather than presenting a new controlled comparison of synthetic and human data.

**Evidence**

- The survey describes instruction tuning as bridging the pretraining objective and user instructions, improving controllability and enabling efficient domain adaptation. It also reports concerns that instruction tuning mainly improves tasks represented in the training dataset and may capture surface patterns or styles rather than robust task understanding. [S18]

#### Finding 2

**Claim**

In a specialized machine-translation task, word-alignment-generated synthetic data produced slightly worse markup transfer than high-quality human-curated data, but did not reduce translation quality.

**Confidence:** Medium

**Why this confidence level**

S19 is a conference research paper with a direct empirical comparison, but it covers one structured translation task, five language directions, and one synthetic-data construction method; generalization to broad LLM fine-tuning is uncertain.

**Evidence**

- The study evaluated English-to-five-language translation with markup and found that synthetic data created through word alignments yielded inferior markup transfer relative to original marked-up data, while translation quality was not negatively affected. Instruction fine-tuning improved translation quality more than few-shot prompting. [S19]

#### Finding 3

**Claim**

Synthetic data quality should be evaluated for both task performance and preservation of the specific structure or behavior being targeted; aggregate quality metrics can hide localized degradation.

**Confidence:** Medium

**Why this confidence level**

The evidence is consistent across a specialized empirical study and a survey, but it does not establish a universal evaluation protocol.

**Evidence**

- S19 found a divergence between translation quality and markup-transfer quality: the synthetic data did not harm general translation quality but slightly harmed markup handling. [S19]
- S18 notes that instruction-tuning datasets may improve represented tasks while failing to ensure robust understanding or handling of unanticipated responses. [S18]

#### Finding 4

**Claim**

The new sources reinforce that synthetic-data benefits are conditional on dataset coverage, quality, and validation rather than guaranteed by scale alone.

**Confidence:** High

**Why this confidence level**

The conclusion is supported by a survey-level synthesis and a direct empirical study, and it is consistent with the accumulated evidence on filtering, distribution alignment, and real-world validation.

**Evidence**

- S18 identifies limited quantity, diversity, and creativity in instruction datasets and warns that fine-tuning gains may be narrow or surface-level. [S18]
- S19 reports that synthetic data was usable without harming one quality dimension, but remained inferior on the task-specific markup-transfer dimension. [S19]

### Conflicts Found

- S19 finds that synthetic data can reduce a targeted capability such as markup transfer without reducing overall translation quality, whereas broader sources describe synthetic data as capable of causing general degradation or collapse. These are conditional differences involving task scope, synthetic-data generation method, and whether data is recursively recycled. [S2] [S5] [S7] [S19]
- S18 presents instruction tuning as broadly beneficial for controllability and efficient adaptation, while also reporting criticism that gains can be narrow or surface-level. This is a qualification rather than a direct contradiction: aggregate task improvements may coexist with weak out-of-distribution generalization. [S18]
- S20 and S22 make strong practical claims about synthetic data being bias-reducing, privacy-safe, and performance-enhancing, but these claims are promotional and are not supported in the retrieved content by independently reported experiments. They should not be weighed equally with S18 or S19. [S20] [S22]

### Important Gaps

- How much do the S19 findings transfer from structured translation to instruction tuning, preference optimization, reasoning, tool use, and safety fine-tuning?
- What evaluation methods best detect capability-specific regressions when aggregate task quality remains stable?
- What independent controlled studies compare synthetic and human-authored instruction data on realistic deployment distributions, calibration, hallucination, robustness, safety, and subgroup outcomes?
- What mixing ratios, source diversity, and human-review levels preserve rare and ambiguous real-world cases across LLM tasks?
- How do synthetic-data generator biases translate into downstream demographic, cultural, and linguistic disparities after fine-tuning?
- What privacy guarantees and re-identification tests are necessary before synthetic text is used in place of sensitive real data?
- Do synthetic evaluation sets systematically overestimate performance for safety, factuality, calibration, tool use, and agentic tasks?

**Analysis Duration:** 11.74s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

S19 adds useful independent evidence, but only for a narrow translation-with-markup setting. S18 is a survey, while S20 and S22 are commercial promotional sources and S21 is a bibliography rather than primary evidence. Important gaps remain around broad real-world generalization, bias outcomes, safety, and evaluation validity.

**Next Search**

> independent empirical comparison synthetic vs human instruction-tuning data LLM real-world generalization fairness calibration hallucination safety

---

# Iteration 6

## 1. Search

**Query**

> independent empirical comparison synthetic vs human instruction-tuning data LLM real-world generalization fairness calibration hallucination safety

**Why this query**

S19 adds useful independent evidence, but only for a narrow translation-with-markup setting. S18 is a survey, while S20 and S22 are commercial promotional sources and S21 is a bibliography rather than primary evidence. Important gaps remain around broad real-world generalization, bias outcomes, safety, and evaluation validity.

**Results**

0 results retrieved.

0 new unique sources added.

### Sources

No new unique sources were added.

**Search Duration:** 3.78s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data offers practical benefits for LLM training and fine-tuning, especially lower data-generation and annotation costs, scalable instruction or preference data, privacy-sensitive workflows, and targeted coverage of rare or underrepresented cases.

**Confidence:** Medium

**Why this confidence level**

The benefit is consistently reported, but much of the evidence is practitioner or tutorial material rather than independent head-to-head studies.

**Evidence**

- Multiple sources describe synthetic data as a way to expand scarce labeled datasets, reduce collection and labeling costs, support privacy-sensitive work, and generate targeted examples for rare classes or edge cases. [S1] [S3] [S4] [S9]

#### Finding 2

**Claim**

The main data-quality risk is distributional distortion: repeated, single-source, or weakly filtered synthetic training can narrow diversity, omit low-probability but valid cases, and contribute to model collapse or capability-specific regressions.

**Confidence:** High

**Why this confidence level**

The mechanism is supported by several sources, including an empirical study, and is consistent across broad collapse concerns and task-specific degradation.

**Evidence**

- Sources describe degradation from recursive synthetic training and report that source diversity, real-data mixing, deduplication, and quality filtering mitigate distribution collapse. [S2] [S5] [S7] [S9]
- A translation study found that synthetic data preserved overall translation quality but degraded the targeted capability of markup transfer, illustrating that aggregate metrics can hide localized regressions. [S19]

#### Finding 3

**Claim**

Synthetic data is generally safest and most useful as a carefully controlled supplement to real or externally grounded data, not as an unverified replacement for it.

**Confidence:** High

**Why this confidence level**

This conditional conclusion is supported by convergent evidence and reconciles the sources that report strong benefits with those documenting collapse and realism risks.

**Evidence**

- The accumulated evidence recommends real-data mixing, diverse generation sources, filtering, deduplication, and validation against trusted real-world criteria; purely recursive synthetic regimes are associated with degradation. [S1] [S2] [S5] [S7] [S9]

#### Finding 4

**Claim**

Synthetic data does not automatically reduce bias and can reproduce stereotypes, demographic distortions, incorrect associations, or unrealistic subgroup examples.

**Confidence:** High

**Why this confidence level**

The generator-bias finding is directly measured in a peer-reviewed study and is reinforced by separate fairness and data-quality evidence, although downstream effects on language-model fine-tuning remain incompletely measured.

**Evidence**

- A peer-reviewed study found significant stereotype and demographic-distribution biases in profiles generated by all four examined LLMs. [S14]
- Other sources identify bias amplification and underrepresentation as risks, while fairness-oriented guidance requires auditing coverage, semantic correctness, distributional fit, and held-out subgroup outcomes. [S3] [S4] [S10] [S15]

#### Finding 5

**Claim**

Targeted synthetic generation may improve subgroup coverage or downstream fairness, but nominal balancing alone can worsen utility or overstate fairness when the synthetic distribution differs from deployment data.

**Confidence:** Medium

**Why this confidence level**

The evidence is strong on the conditional nature of fairness gains, but the most direct controlled results come from vision or tabular settings rather than LLM fine-tuning.

**Evidence**

- Fairness-oriented sources report possible gains from targeted generation and controlled fine-tuning, but also identify quality and domain gaps as obstacles and report fairness–utility tradeoffs when balanced synthetic data is used blindly. [S10] [S15]
- A large empirical comparison found that fairness gains were substantially larger on artificially balanced tests than on realistic imbalanced distributions, cautioning against deployment claims based only on balanced evaluation. [S13]

#### Finding 6

**Claim**

Synthetic evaluation data can be useful for scalable, controlled testing and relative system comparisons, but it can systematically overestimate performance and is unreliable as sole evidence of absolute or deployment performance.

**Confidence:** Medium

**Why this confidence level**

The evaluation bias is empirically supported in an information-retrieval setting, but generalization to all LLM evaluation domains is not established.

**Evidence**

- An empirical study found systematic differences between human and LLM-generated queries and higher automated relevance judgments for synthetic evaluations, producing biased absolute estimates while having a smaller effect on some relative rankings. [S16]
- Other sources warn that synthetic or static benchmarks can be contaminated, saturated, overfit, or weakly predictive of realistic tool-use, agentic, safety, and workflow behavior. [S3] [S4] [S5] [S8]

#### Finding 7

**Claim**

Evaluation should test more than aggregate accuracy or benchmark scores: it should include trusted human or real-world ground truth, realistic population distributions, subgroup slices, edge and adversarial cases, capability-specific measures, calibration or uncertainty, and downstream workflow outcomes.

**Confidence:** High

**Why this confidence level**

Multiple sources converge on the need for multidimensional, deployment-relevant evaluation, even though no universally validated protocol or safe mixing ratio was retrieved.

**Evidence**

- Sources recommend comparison with human or trusted ground truth, plausibility and consistency checks, subgroup and edge-case testing, realistic imbalanced distributions, and downstream outcome validation. [S3] [S4] [S12] [S13]
- The evidence also indicates that unequal confidence or uncertainty can reveal fairness problems missed by accuracy-only metrics. [S17]
- Task-specific evaluation is necessary because overall quality can remain stable while a targeted behavior, such as markup transfer or adversarial robustness, deteriorates. [S7] [S19]

#### Finding 8

**Claim**

Synthetic fine-tuning can preserve or improve ordinary output quality while weakening robustness or safety, so benchmark gains should not be interpreted as evidence of safe deployment.

**Confidence:** Medium

**Why this confidence level**

The safety finding is direct but comes primarily from one study whose exact setup and external validity are only partially available.

**Evidence**

- The empirical fine-tuning study reports reduced adversarial robustness despite higher output quality and examines weakening of safety safeguards as a distinct downstream effect. [S7]
- Other sources warn that static benchmark success may not predict reliability in realistic or adversarial workflows. [S3] [S5]

### Conflicts Found

- Sources reporting strong synthetic-data benefits and optimistic large-scale pipelines differ from sources documenting collapse, narrow generalization, bias, and safety degradation. The disagreement is conditional on source diversity, filtering, real-data retention, task, and whether outputs are recursively recycled. [S2] [S5] [S7] [S9] [S18]
- Targeted synthetic data is presented as a possible fairness intervention, but other evidence shows that balanced or synthetic tests can exaggerate fairness and that domain gaps can reduce utility. These findings are compatible only if fairness gains are demonstrated on realistic distributions against strong baselines. [S10] [S13] [S15]
- Synthetic evaluation may support relative ranking in some settings while still biasing absolute performance estimates and failing to predict deployment reliability. Results from one information-retrieval study should not be generalized to safety-critical or agentic evaluation. [S5] [S16]
- Human data is described as costly and less scalable, while also remaining important for ground truth, frontier-capability evaluation, realistic user behavior, and independent validation. The tradeoff is operational rather than a contradiction. [S4] [S9] [S12]

### Important Gaps

- What source diversity, real-data mixing ratio, and human-review level reliably prevent quality, robustness, and fairness degradation across different LLM tasks and model sizes?
- How do generator stereotype and demographic-distribution biases translate into downstream demographic, cultural, and linguistic disparities after LLM fine-tuning?
- Which independent controlled studies compare human-authored and synthetic instruction, preference, or safety data on realistic deployment distributions, calibration, hallucination, robustness, and subgroup outcomes?
- How often do synthetic evaluation sets overestimate safety, factuality, calibration, tool-use, and agentic-task performance?
- What privacy and re-identification tests are necessary before synthetic text can substitute for sensitive real data?
- Which evaluation methods best detect capability-specific regressions when aggregate task quality remains stable?

**Analysis Duration:** 15.58s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

No usable new sources were retrieved and no further query was selected. Analyzer assessment: No usable new sources were retrieved, and the accumulated evidence supports a responsible conditional answer: synthetic data can reduce cost and expand coverage, but risks arise from distribution narrowing, generator bias, domain shift, misleading evaluation, and hidden safety regressions. Further research would improve quantitative guidance—especially mixing ratios, cross-domain fairness effects, and deployment validity—but is not necessary to answer the original question responsibly.

**Stop Reason:** no_search_results

---

# Final Research Decision

**Research Stopped Because**

No usable new sources were retrieved and no further meaningful query was selected.

**Stop Reason:** no_search_results

**Searches Performed:** 6

**Unique Sources:** 22

**Remaining Uncertainty**

- Independent controlled comparisons of human-authored versus synthetic instruction, preference, and safety data for LLMs on realistic deployment distributions.
- Quantitative guidance on source diversity, synthetic-to-real mixing ratios, and required levels of human review across LLM tasks and model sizes.
- Direct measurement of how generator stereotypes and demographic-distribution biases affect downstream LLM fairness after fine-tuning.
- Evidence on whether synthetic evaluation sets overestimate safety, factuality, calibration, tool-use, and agentic-task performance.
- Validated privacy and re-identification tests for synthetic text used in place of sensitive real data.
- Evaluation methods that reliably detect capability-specific regressions when aggregate task scores remain stable.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 6 | 14.81s |
| OpenAI Analysis | 6 | 94.99s |
| Report Generation | 1 | 15.98s |
| Total Run | — | 125.77s |
