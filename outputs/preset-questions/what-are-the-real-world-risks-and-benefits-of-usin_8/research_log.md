# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

**Status:** Completed

**Stop Reason:** sufficient_evidence

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 5 / 10

**Unique Sources:** 23

**OpenAI Calls:** 6

**Tavily Calls:** 5

**Started:** 2026-09-01T02:59:14-04:00

**Ended:** 2026-09-01T03:01:37-04:00

**Total Runtime:** 143.00s

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

- **S1 — Examining synthetic data: The promise, risks and realities | IBM**
  URL: https://www.ibm.com/think/insights/ai-synthetic-data
- **S2 — The Prominence of Synthetic Data, and Why It Will Expand Rather Than Replace Real Data - Dataversity**
  URL: https://www.dataversity.net/articles/the-prominence-of-synthetic-data-and-why-it-will-expand-rather-than-replace-real-data
- **S3 — Synthetic Data Generation Using Large Language Models**
  URL: https://arxiv.org/pdf/2503.14023
- **S4 — Synthetic Data Generation Using Large Language Models: Advances in Text and Code**
  URL: https://arxiv.org/html/2503.14023v2
- **S5 — Best Practices and Lessons Learned on Synthetic Data for Language Models**
  URL: https://arxiv.org/html/2404.07503v1

**Search Duration:** 3.21s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data can address practical bottlenecks in LLM training by increasing the amount of task-specific data, reducing annotation and collection costs, and enabling work in privacy-sensitive or low-resource domains.

**Confidence:** Medium

**Why this confidence level**

Multiple sources consistently describe these benefits, but the retrieved material gives limited independent, task-by-task real-world measurements.

**Evidence**

- The survey reports that LLM-generated text and code can augment or substitute for real data when labeled data is scarce, expensive, or sensitive; it identifies cost-effectiveness, broad coverage, and controllable diversity as benefits. [S3] [S4]
- The best-practices paper describes synthetic data as scalable, relatively low-cost, and useful where real-world data is scarce, difficult to obtain, privacy-constrained, or expensive to annotate. [S5]
- An IBM report describes synthetic data as a way to address data bottlenecks and potentially reduce development costs and privacy constraints. [S1]

#### Finding 2

**Claim**

Synthetic data can improve performance in low-data or specialized settings, especially when it is targeted, curated, and supplemented with real data.

**Confidence:** Medium

**Why this confidence level**

The sources provide reported examples and a survey summary, but several claims are secondary or drawn from cited studies whose detailed methods and controls are not included in the retrieved content.

**Evidence**

- The survey states that prior studies report performance improvements of 3–26% with synthetic augmentation in low-data regimes and emphasizes the importance of prompt design and curation. [S3] [S4]
- IBM reports the LAB approach as achieving competitive benchmark performance and describes LABRADORITE-13B and MERLINITE-7B as outperforming other fine-tuned versions of the same base models on several metrics. [S1]
- The best-practices paper gives examples of synthetic math questions and answers improving reasoning models, while noting that answer format and inclusion of high-quality data affect outcomes. [S5]
- A Dataversity article says Microsoft’s Phi-4 was trained largely on synthetic data but also used carefully curated, high-quality real-world pretraining data; it presents this as evidence for combining rather than replacing real data. [S2]

#### Finding 3

**Claim**

Synthetic training data can be factually inaccurate, stylistically or distributionally unrealistic, and insufficiently diverse; models trained on such data may fail to generalize to real-world inputs.

**Confidence:** High

**Why this confidence level**

The risk is stated consistently across a dedicated survey, a best-practices paper, and an industry analysis, with a clear quality-control rationale.

**Evidence**

- The survey identifies factual inaccuracies, insufficient stylistic or distributional realism, and diversity drift as central challenges. [S3] [S4]
- The best-practices paper warns that false, hallucinated, or biased synthetic data can cause poor generalization to real-world scenarios and stresses the need to preserve real-world patterns and relationships. [S5]
- IBM states that synthetic-data fidelity should be assessed against real-world statistical properties such as means, variances, and correlations, indicating that similarity cannot be assumed from fluent output alone. [S1]

#### Finding 4

**Claim**

Synthetic data may preserve, amplify, or introduce bias rather than automatically correcting bias; controllable generation can help address representation gaps, but only if it is validated against real populations and outcomes.

**Confidence:** High

**Why this confidence level**

Sources directly address both the potential benefit of controlled representation and the risk of biased generation, with no meaningful contradiction.

**Evidence**

- The survey identifies bias amplification and modeling bias as risks and highlights generation controls for rare phenomena and bias reduction as open research needs. [S3] [S4]
- The best-practices paper notes that synthetic data can be designed to balance classes or up-weight low-resource languages, but can also amplify or introduce new biases without careful design and validation. [S5]
- IBM warns that synthetic data may not represent demographic diversity accurately, producing models that perform inequitably across groups. [S1]

#### Finding 5

**Claim**

Repeated training on model-generated data creates a model-collapse risk: quality, factuality, diversity, precision, or recall may deteriorate, particularly when fresh real-world data is excluded.

**Confidence:** Medium

**Why this confidence level**

The sources consistently report the risk, but the retrieved content is partly secondary and does not establish how the risk varies by synthetic-data quality, mixture ratio, or training objective.

**Evidence**

- IBM cites a Nature study reporting increasingly nonsensical outputs when models are repeatedly trained on AI-generated text. [S1]
- Dataversity summarizes research finding that model-generated data used without care can cause permanent degradation and that fresh real-world data is needed to prevent progressive loss of precision or diversity. [S2]
- The survey defines model collapse as degradation across successive generations trained primarily or exclusively on synthetic data and recommends filtering, blending with real data, and feedback mechanisms. [S3] [S4]

#### Finding 6

**Claim**

Evaluation must go beyond aggregate benchmark scores: synthetic datasets and resulting models require checks of factuality, fidelity to real distributions, diversity, bias/fairness, and robustness/generalization on independent real-world data.

**Confidence:** Medium

**Why this confidence level**

The sources clearly establish the evaluation dimensions, but the retrieved excerpts do not provide a detailed operational protocol, validated metrics, or evidence on which metrics best predict downstream LLM behavior.

**Evidence**

- The best-practices paper explicitly calls for evaluation metrics for factuality and fidelity, rigorous testing, and fairness assessments; its structure includes a dedicated section on synthetic data in evaluation. [S5]
- The survey calls for robust evaluation frameworks and identifies fidelity, factuality, distributional realism, diversity, bias, and model-collapse prevention as evaluation challenges. [S3] [S4]
- IBM describes fidelity testing against real-world statistical properties and recommends treating synthetic data as a supplement rather than a replacement for real data. [S1]

### Conflicts Found

- The sources differ in how strongly they characterize synthetic data as a substitute for real data. The survey says it can potentially augment or even substitute for real datasets in some settings, while IBM and Dataversity emphasize that it should generally supplement real data and that real inputs remain necessary to preserve quality and avoid collapse. [S1] [S2] [S3] [S4]
- Synthetic data is presented both as a possible tool for improving fairness through controlled balancing or up-weighting underrepresented groups and as a source of bias amplification or demographic underrepresentation. These are conditional differences, depending on generation controls and validation quality rather than a direct factual contradiction. [S1] [S3] [S4] [S5]

### Important Gaps

- What evaluation protocol best detects factuality errors, distribution shift, memorization, and model collapse before synthetic data is used for LLM training or fine-tuning?
- How much real data, and what mixture of real versus synthetic data, is needed to prevent quality or diversity degradation across different tasks and domains?
- Do synthetic-data gains persist on independent, contamination-controlled, real-world evaluations rather than only on benchmarks resembling the generation prompts?
- Which fairness metrics and subgroup tests reliably detect bias introduced or amplified by synthetic generation?
- How often does synthetic data accidentally reproduce sensitive information from its source model or source dataset, and how effective are privacy audits in practice?

**Analysis Duration:** 18.67s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The key risks and benefits are reasonably established, but evaluation—the question's explicit focus—remains underspecified. The retrieved excerpts recommend rigorous evaluation without supplying a concrete, independently validated methodology or sufficient evidence about out-of-distribution performance and fairness testing. One focused search for empirical evaluation protocols would materially improve the answer.

**Next Search**

> empirical evaluation framework synthetic data LLM training factuality bias diversity real-world held-out evaluation model collapse

---

# Iteration 2

## 1. Search

**Query**

> empirical evaluation framework synthetic data LLM training factuality bias diversity real-world held-out evaluation model collapse

**Why this query**

The key risks and benefits are reasonably established, but evaluation—the question's explicit focus—remains underspecified. The retrieved excerpts recommend rigorous evaluation without supplying a concrete, independently validated methodology or sufficient evidence about out-of-distribution performance and fairness testing. One focused search for empirical evaluation protocols would materially improve the answer.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S6 — Synthetic Data for LLM Training: Decision Guide 2026**
  URL: https://www.digitalapplied.com/blog/synthetic-data-generation-llm-training-decision-guide-2026
- **S7 — A Multi-Faceted Evaluation Framework for Assessing Synthetic Data Generated by Large Language Models**
  URL: https://arxiv.org/html/2404.14445v2
- **S8 — Biased by Design? Evaluating Bias and Behavioral Diversity in LLM Annotation of Real-World and Synthetic Hotel Reviews**
  URL: https://www.mdpi.com/2673-2688/6/8/178
- **S9 — Medium**
  URL: https://medium.com/foundation-models-deep-dive/challenges-and-pitfalls-of-using-synthetic-data-for-llms-7337fcda1316
- **S10 — On LLMs-Driven Synthetic Data Generation, Curation, and Evaluation: A Survey | alphaXiv**
  URL: https://www.alphaxiv.org/abs/2406.15126

**Search Duration:** 2.82s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The strongest practical benefit is targeted augmentation: synthetic data can expand scarce, expensive, imbalanced, or privacy-constrained datasets, but its value depends more on generation and curation quality than on raw volume.

**Confidence:** Medium

**Why this confidence level**

The benefit is consistent across sources, but S6 includes vendor-stated and practitioner-oriented claims, and S7 primarily concerns tabular data rather than LLM training.

**Evidence**

- The survey describes a generation–curation–evaluation workflow and says synthetic data addresses scarcity, quality, privacy, specialized-domain, and rare-language constraints. It also reports that prompting and multi-step generation affect output quality. [S10]
- The evaluation-framework paper says synthetic data can be generated faster and manipulated more easily than real data, supporting controlled training and testing while potentially reducing collection and labeling burdens. [S7]
- The decision guide presents curated synthetic textbook and exercise data as capable of producing strong coding results, while explicitly attributing success to disciplined curation rather than indiscriminate volume. [S6]

#### Finding 2

**Claim**

Synthetic data can improve downstream performance in some low-data or specialized settings, especially when combined with real data and carefully filtered.

**Confidence:** Medium

**Why this confidence level**

Reported gains are plausible and supported by multiple sources, but the new performance examples are partly vendor-stated or secondary, and the evidence does not establish that gains generalize across tasks.

**Evidence**

- The accumulated survey evidence reports performance gains in low-data regimes and emphasizes prompting and curation. [S3] [S4]
- The decision guide reports Phi-1 results using both curated web data and synthetic textbooks/exercises, illustrating a mixed-data recipe rather than replacement of real data. [S6]
- The survey describes sample filtering, re-weighting, consistency checks, and multi-step generation as ways to improve synthetic QA and other training examples. [S10]

#### Finding 3

**Claim**

Synthetic data can have fidelity and quality gaps: fluent outputs may still contain factual errors, unrealistic styles or distributions, noise, inconsistencies, limited diversity, and poor coverage of low-probability but valid cases.

**Confidence:** High

**Why this confidence level**

The core quality risks are consistently supported by the survey, best-practices material, and the cited collapse discussion. Specific numerical collapse results rely on the decision guide’s summary rather than directly retrieved primary-paper text.

**Evidence**

- The accumulated survey and best-practices evidence identifies factual inaccuracy, distributional and stylistic unreality, diversity drift, hallucination, and poor real-world generalization as central risks. [S3] [S4] [S5]
- The survey states that initial generations commonly contain noise, inconsistency, or irrelevant samples and recommends filtering, re-weighting, and consistency-based quality checks. [S10]
- The decision guide describes model collapse as progressive loss of distributional tails and diversity under iterative synthetic training, and reports severe perplexity degradation in a purely synthetic OPT-125m regime. [S6]

#### Finding 4

**Claim**

Model collapse risk is conditional on the training regime: replacing real data or repeatedly training on model outputs is substantially riskier than adding curated synthetic data while retaining fresh real data.

**Confidence:** Medium

**Why this confidence level**

The conditional pattern is consistent, but the precise mixture thresholds and generality across model sizes, domains, and objectives remain unestablished in the retrieved evidence.

**Evidence**

- The decision guide contrasts pure synthetic self-training with additive mixtures and states that retaining or accumulating real data bounds or reduces degradation, while replacement causes unbounded or severe deterioration according to the cited studies. [S6]
- The accumulated findings likewise identify collapse under successive primarily synthetic training and recommend filtering and blending synthetic data with real data. [S1] [S2] [S3] [S4]

#### Finding 5

**Claim**

Synthetic data does not automatically reduce bias; it can preserve or amplify generator and source-data biases, omit marginalized groups, or introduce new stereotypes. Controlled balancing and rare-group augmentation are potential benefits only when validated against real populations and outcomes.

**Confidence:** High

**Why this confidence level**

The general conditional bias claim is directly supported by multiple prior sources. S8 adds no usable empirical detail because the retrieved page is effectively navigation content.

**Evidence**

- The accumulated survey and best-practices sources identify bias amplification and modeling bias while noting that controlled generation can address representation gaps. [S3] [S4] [S5]
- The evaluation-framework paper motivates synthesis partly through imbalance and marginalized-group underrepresentation, while framing fidelity, utility, and privacy as separate evaluation dimensions. [S7]
- The hotel-review study’s available retrieved content exposes the study title but not its findings, so it cannot independently substantiate a specific bias result. [S8]

#### Finding 6

**Claim**

Evaluation should be multidimensional and should test both the synthetic dataset and the trained model on independent real-world data, not rely on aggregate benchmark scores or synthetic-data similarity alone.

**Confidence:** High

**Why this confidence level**

Multiple sources converge on the same evaluation dimensions, and S7 provides a concrete framework structure, although it is demonstrated on tabular product reviews rather than full LLM text-training pipelines.

**Evidence**

- SynEval explicitly separates fidelity, downstream utility, and privacy preservation, including comparison with validation or real-world datasets and re-identification-risk analysis. [S7]
- The accumulated survey and best-practices evidence calls for factuality, fidelity to real distributions, diversity, fairness, robustness, and generalization checks. [S3] [S4] [S5]
- The survey’s workflow makes evaluation feedback part of an iterative generation and curation process, while recommending consistency-based filtering and re-weighting before training. [S10]

#### Finding 7

**Claim**

Privacy is a benefit only conditionally: synthetic data may reduce direct exposure to personal records, but privacy preservation must be measured because generated data can still leak or enable re-identification of source information.

**Confidence:** Medium

**Why this confidence level**

The need for privacy audits is well supported, but the retrieved evidence does not quantify leakage rates or demonstrate how well these metrics transfer from tabular data to LLM text.

**Evidence**

- SynEval treats privacy as a distinct evaluation dimension and proposes re-identification-risk and other privacy-preserving metrics, noting privacy leakage concerns when personal information is present in training data. [S7]
- The accumulated sources describe privacy-sensitive use as a motivation for synthetic data but warn that privacy protection cannot be assumed from synthetic generation alone. [S1] [S5]

### Conflicts Found

- Sources differ in how far synthetic data can replace real data. Some survey language allows augmentation or possible substitution in constrained settings, whereas the stronger operational recommendation is to retain fresh real data and use synthetic data additively to limit collapse and distribution loss. [S1] [S2] [S3] [S4] [S6]
- Synthetic data is described both as a way to correct imbalance and as a mechanism that can amplify bias. This is a conditional disagreement dependent on generator controls, source-model biases, subgroup coverage, and outcome-based validation, not a direct contradiction. [S1] [S3] [S4] [S5] [S7]
- The decision guide presents specific risk categories and quantitative examples, but these are not fully corroborated by the retrieved primary studies; therefore its precise thresholds and performance figures should not be treated as independently established. [S6]

### Important Gaps

- What concrete, LLM-specific test suite best measures factuality, diversity, subgroup fairness, memorization or privacy leakage, and real-world generalization before deployment?
- What real-to-synthetic mixture and refresh rate prevents collapse across different model sizes, tasks, and domains?
- Do reported gains persist on contamination-controlled, independent real-world evaluations rather than benchmarks aligned with generation prompts?
- How should evaluator disagreement and synthetic-reference bias be handled when assessing generated training examples or synthetic evaluation sets?
- How well do tabular-data privacy and utility metrics in SynEval transfer to free-form LLM training text?

**Analysis Duration:** 20.73s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The main risks and benefits can now be answered responsibly, and the new sources materially strengthen the evaluation and conditional-collapse findings. However, the original question specifically emphasizes evaluation, and the evidence still lacks an independently sourced, operational protocol for LLM text that jointly tests factuality, bias, privacy, contamination, and downstream real-world generalization.

**Next Search**

> LLM synthetic training data evaluation protocol factuality bias privacy leakage contamination real-world generalization benchmark

---

# Iteration 3

## 1. Search

**Query**

> LLM synthetic training data evaluation protocol factuality bias privacy leakage contamination real-world generalization benchmark

**Why this query**

The main risks and benefits can now be answered responsibly, and the new sources materially strengthen the evaluation and conditional-collapse findings. However, the original question specifically emphasizes evaluation, and the evidence still lacks an independently sourced, operational protocol for LLM text that jointly tests factuality, bias, privacy, contamination, and downstream real-world generalization.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S11 — Efficacy of Synthetic Data as a Benchmark**
  URL: https://arxiv.org/html/2409.11968v1
- **S12 — Defending Data Contamination in the Evaluation of LLM- ...**
  URL: https://aclanthology.org/2025.acl-long.431.pdf
- **S13 — Data Contamination or Genuine Generalization? Disentangling LLM Performance on Benchmarks | Academic Journal of Natural Science**
  URL: https://www.suaspress.org/ojs/index.php/AJNS/article/view/v2n2a03
- **S14 — How to Build Privacy-Preserving Evaluation Benchmarks with Synthetic Data | NVIDIA Technical Blog**
  URL: https://developer.nvidia.com/blog/how-to-build-privacy-preserving-evaluation-benchmarks-with-synthetic-data

**Search Duration:** 2.73s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data is more reliable as an evaluation benchmark for simple tasks than for complex tasks, so benchmark validity is task-dependent.

**Confidence:** Medium

**Why this confidence level**

The source reports systematic experiments, but the retrieved content does not provide the full results or establish whether the pattern generalizes beyond the evaluated tasks and datasets.

**Evidence**

- Across six datasets and three NLP tasks, S11 reports that synthetic benchmarks captured performance relatively well for intent classification but were less representative for named entity recognition. The study assessed both absolute agreement with real-data performance and preservation of method rankings. [S11]

#### Finding 2

**Claim**

Using the same LLM to generate synthetic evaluation data and to solve the task can create evaluator–data alignment bias, particularly for smaller models.

**Confidence:** Medium

**Why this confidence level**

The finding is based on an empirical benchmark study, but the retrieved material does not show the complete statistical analysis or test a broad range of generator–evaluator relationships.

**Evidence**

- S11 introduces a bias-factor metric and reports that smaller LLMs perform slightly better on synthetic data generated by themselves, while larger models show little or no significant self-generation bias. [S11]
- S11 recommends using synthetic data generated by multiple larger models and averaging results to make benchmarks more robust and representative. [S11]

#### Finding 3

**Claim**

Synthetic evaluation sets can produce misleading conclusions when they are not compared with independent real-world data and when contamination is not controlled.

**Confidence:** Medium

**Why this confidence level**

S11 and S12 provide directly relevant evaluation evidence, but S12 concerns a specific fake-news task and S13 is from a less established publication venue. The general evaluation principle is stronger than the precise numerical claims.

**Evidence**

- S11 evaluates synthetic benchmarks by comparing them with real datasets and shows that representativeness varies by task, rather than assuming fluent synthetic examples are valid proxies. [S11]
- S12 reports that benchmark-data contamination can inflate conventional fake-news-detection performance by up to 23%, and presents a framework using human-adversarial examples, dynamically sourced claims, and controlled entities to test robustness and temporal generalization. [S12]
- S13 advocates n-gram overlap checks, canary insertion, and perturbation testing to distinguish memorization from genuine generalization; it reports that entity swaps can substantially reduce factual-recall accuracy. [S13]

#### Finding 4

**Claim**

Evaluation should include multiple independent generators or human/real-world references rather than relying on a single model-generated synthetic distribution.

**Confidence:** Medium

**Why this confidence level**

The sources support triangulation as a useful strategy, but they do not establish an optimal number or selection rule for generators.

**Evidence**

- S11 finds that averaging performance across synthetic data generated by multiple LLMs yields a more robust and representative benchmark, and observes that no single LLM is consistently best at generating evaluation data across tasks. [S11]
- S12 combines human-crafted adversarial tests, real-time claims, and entity-controlled environments to reduce contamination and improve practical relevance. [S12]

#### Finding 5

**Claim**

Synthetic data can provide privacy-preserving evaluation and coverage of rare or underrepresented cases, but these benefits require quality filtering and domain validation.

**Confidence:** Low

**Why this confidence level**

The claimed benefits are plausible and consistent with prior findings, but S14 is vendor-authored, describes a workflow rather than controlled downstream results, and does not independently demonstrate privacy protection or clinical validity.

**Evidence**

- S14 describes a healthcare triage workflow intended to generate domain-specific cases without exposing patient records, while addressing annotation cost, data scarcity, and underrepresented rare conditions. It also describes scoring and filtering synthetic examples before evaluation. [S14]
- S14 presents synthetic generation as a way to create edge cases and diverse scenarios more quickly than traditional collection, but the material is a vendor demonstration rather than an independent effectiveness study. [S14]

#### Finding 6

**Claim**

The accumulated evidence favors using synthetic data as controlled augmentation or evaluation support, not as an unvalidated replacement for fresh real-world data.

**Confidence:** High

**Why this confidence level**

Multiple sources converge on conditional benefits and substantial validation requirements, despite limited evidence for universal mixture rules or broad production outcomes.

**Evidence**

- S11 shows that synthetic benchmark representativeness deteriorates on at least some complex tasks and that generator–evaluator bias can affect results. [S11]
- Prior findings report risks of factual error, distributional unreality, bias amplification, and model collapse when synthetic data is used without sufficient real-data grounding or validation. [S1] [S3] [S4] [S5] [S6]
- S12 and S13 add that contamination and memorization can make standard benchmark scores overstate real-world capability. [S12] [S13]

### Conflicts Found

- S11 shows that synthetic benchmarks can preserve useful performance comparisons for simpler tasks, whereas the broader accumulated evidence warns that synthetic evaluation can be misleading. This is a conditional disagreement: usefulness depends on task complexity, generator diversity, contamination controls, and comparison with real data. [S11] [S3] [S5] [S12]
- S11 reports little or no significant self-generation bias for larger models but some bias for smaller models; this qualifies, rather than directly contradicts, the general concern that synthetic data may encode evaluator or generator bias. [S11] [S3] [S4] [S5]
- S14 presents synthetic data as enabling privacy-safe evaluation without exposing real records, while prior findings state that privacy cannot be assumed and must be audited for leakage or re-identification. S14 provides a workflow claim, not evidence that leakage risk is eliminated. [S14] [S1] [S5] [S7]
- S13 reports specific contamination and perturbation figures, but these are not corroborated by the other retrieved sources and come from a less established publication venue; they should not be treated as settled general estimates. [S13]

### Important Gaps

- What controlled studies measure synthetic fine-tuning gains on contamination-free, independent real-world test sets across domains and model sizes?
- What real-to-synthetic mixture, refresh rate, and filtering strategy prevents quality, diversity, and factuality degradation?
- How should task complexity be operationalized to predict when a synthetic benchmark will fail, as suggested by the contrast between intent classification and NER in S11?
- Which combination of human references, multiple generators, perturbation tests, temporal splits, and contamination detection best predicts deployment performance?
- How effective are synthetic-data privacy safeguards for free-form LLM text, especially against memorization and re-identification?
- Which subgroup and outcome-based fairness tests detect bias amplification in synthetic training and evaluation data?
- Do synthetic-data improvements persist after testing on adversarial, temporally new, and distribution-shifted real inputs?
- How reliable are vendor-reported privacy and clinical-quality claims in workflows such as the S14 triage example?

**Analysis Duration:** 19.67s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources materially strengthen the evaluation picture, especially task-dependent benchmark validity, evaluator–data bias, and contamination-aware testing. However, an important part of the original question remains weakly answered: independent primary evidence on real-world downstream benefits and risks of synthetic data used specifically to train or fine-tune LLMs, including mixture ratios and held-out deployment-like evaluation.

**Next Search**

> primary empirical study synthetic data fine-tuning LLMs real-world held-out evaluation factuality bias diversity mixture real synthetic data

---

# Iteration 4

## 1. Search

**Query**

> primary empirical study synthetic data fine-tuning LLMs real-world held-out evaluation factuality bias diversity mixture real synthetic data

**Why this query**

The new sources materially strengthen the evaluation picture, especially task-dependent benchmark validity, evaluator–data bias, and contamination-aware testing. However, an important part of the original question remains weakly answered: independent primary evidence on real-world downstream benefits and risks of synthetic data used specifically to train or fine-tune LLMs, including mixture ratios and held-out deployment-like evaluation.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S15 — Synthetic Data Generation with LLMs: Techniques and Use Cases**
  URL: https://tetrate.io/learn/ai/synthetic-data-generation-llms
- **S16 — Synthetic Data Generation for Fine-Tuning LLMs**
  URL: https://pub.towardsai.net/synthetic-data-generation-for-fine-tuning-llms-de9fe22bd1e6
- **S17 — [Literature Review] Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning**
  URL: https://www.themoonlight.io/en/review/synthetic-eggs-in-many-baskets-the-impact-of-synthetic-data-diversity-on-llm-fine-tuning
- **S18 — Synthetic Data Pipelines for Domain-Specific LLM Fine-Tuning**
  URL: https://tianpan.co/blog/2026-03-04-synthetic-data-pipelines-domain-llm-fine-tuning
- **S19 — Synthetic Data Generation for Fine-Tuning: Using LLMs**
  URL: https://callsphere.tech/blog/synthetic-data-generation-fine-tuning-llms-training-data

**Search Duration:** 4.93s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The practical benefits of synthetic data are strongest when it is used for targeted augmentation or distillation, rather than indiscriminate replacement of real data.

**Confidence:** Medium

**Why this confidence level**

The sources consistently describe plausible operational benefits and safeguards, but S15, S18, and S19 are practitioner or vendor-style materials rather than independent controlled comparisons.

**Evidence**

- S15 describes uses including scarce-data augmentation, class balancing, privacy-sensitive domains, rapid prototyping, edge-case evaluation, and domain adaptation, while stating that utility depends on validation and alignment with the target application. [S15]
- S18 recommends using capable teacher models to generate domain examples for smaller students and emphasizes that real seed data defines the target distribution. [S18]
- S19 presents teacher-generated examples as a way to reduce annotation costs, but explicitly says raw LLM output requires filtering, validation, and deduplication before training. [S19]

#### Finding 2

**Claim**

Seed-data coverage limits synthetic-data coverage: generation from a narrow or unrepresentative real-data slice can preserve that narrowness and omit important edge cases or minority patterns.

**Confidence:** Medium

**Why this confidence level**

The mechanism is directly described, but the retrieved sources do not provide an independent quantitative estimate of how seed coverage affects downstream LLM performance.

**Evidence**

- S18 states that seed data defines the task distribution, that seed quality and diversity constrain generated data, and that narrow seeds can cause failures on real-world edge cases that cannot be recovered through later volume increases. [S18]
- S15 likewise says synthetic-data utility depends on alignment between the generated distribution and target application requirements. [S15]

#### Finding 3

**Claim**

Source diversity can mitigate some distribution-collapse and diversity problems, but it does not make synthetic fine-tuning inherently safe or unbiased.

**Confidence:** Medium

**Why this confidence level**

S17 adds a controlled-looking comparison with concrete held-out and adversarial evaluations, but it is available here through a secondary literature-review summary and has narrow scope: two Llama models, English, and single-turn data.

**Evidence**

- S17 reports that multi-source synthetic fine-tuning improved held-out human-text perplexity relative to single-source or baseline conditions and generally preserved or improved lexical diversity; it interprets this as mitigation of distribution collapse. [S17]
- The same study reports that synthetic fine-tuning increased harmfulness susceptibility and could remove safety guardrails while preserving output quality, with effects varying by target size and source-model configuration. [S17]
- Prior findings identify collapse, factuality loss, diversity drift, and bias amplification when synthetic data is used without real-data grounding and validation. [S1] [S3] [S4] [S5] [S6]

#### Finding 4

**Claim**

Synthetic fine-tuning can alter safety and behavioral alignment in ways that ordinary quality or fluency metrics may miss.

**Confidence:** Medium

**Why this confidence level**

The safety result is specific and potentially important, but it comes from one narrowly scoped study summary; S18 is an anecdotal/practitioner account rather than a controlled evaluation.

**Evidence**

- S17 reports that synthetic fine-tuning removed safety guardrails while preserving output quality on the reported refusal/jailbreak evaluations, making harmful behavior potentially more convincing rather than merely lower quality. [S17]
- S18 warns that domain models can remain fluent while suffering factual or knowledge collapse, and recommends validation on real examples rather than synthetic validation alone. [S18]

#### Finding 5

**Claim**

Evaluation should test both data quality and downstream behavior on independent human or real-world data, including factuality, distributional coverage, diversity, subgroup fairness, robustness, contamination, memorization, and safety.

**Confidence:** High

**Why this confidence level**

Multiple sources converge on independent real-data testing and multidimensional evaluation; uncertainty concerns the optimal metrics and thresholds, not the need for these dimensions.

**Evidence**

- S18 recommends holding out validation data drawn from real examples and warns that synthetic validation creates a blind spot for the relevant failure modes. [S18]
- S19 recommends a held-out evaluation and regression suite, alongside filtering and deduplication of training data. [S19]
- S17 evaluates held-out human-written data, lexical and semantic diversity, adversarial refusal behavior, and evaluator preference bias, illustrating why aggregate task scores are insufficient. [S17]
- Earlier evidence recommends multidimensional evaluation of factuality, fidelity, diversity, fairness, privacy, generalization, contamination, and collapse. [S3] [S4] [S5] [S7] [S11] [S12] [S13]

#### Finding 6

**Claim**

Synthetic evaluation sets are vulnerable to generator-specific and evaluator-specific bias, so multiple generators and independent human or real-world references improve validity.

**Confidence:** Medium

**Why this confidence level**

The evidence supports triangulation and contamination control, but the retrieved material does not establish a universal protocol for generator selection, judge calibration, or statistical aggregation.

**Evidence**

- S17 reports self-preference and pro-synthetic preference effects in LLM judging, with pairwise comparisons detecting biases that direct assessment may miss. [S17]
- S11 reports that synthetic benchmark representativeness varies by task and recommends multiple generators and comparison with real datasets. [S11]
- S12 and S13 show that contamination and memorization controls are necessary because conventional benchmark scores can overstate real-world generalization. [S12] [S13]

### Conflicts Found

- S15 presents LLM-generated data as something that can supplement or sometimes replace human-labeled data, while the accumulated evidence favors retaining fresh real data because replacement or recursive synthetic training can cause collapse and distribution loss. [S15] [S1] [S2] [S3] [S4] [S6] [S18]
- Source diversity appears beneficial for lexical diversity and human-text modeling in S17, but the same study reports that some multi-source, especially larger-source configurations, increased dangerous outputs. Thus diversity improves some quality indicators while potentially worsening safety alignment. [S17]
- S18 recommends a capable teacher and real seeds, whereas S17 finds that the effects of source-model size and diversity are complex and configuration-dependent. A stronger teacher or more sources should not be assumed to improve every outcome. [S17] [S18]
- S14 and S15 describe synthetic generation as privacy-preserving or privacy-sensitive use, but prior evidence treats privacy as conditional and requiring leakage or re-identification testing; generation alone does not establish privacy. [S15] [S1] [S5] [S7] [S14]

### Important Gaps

- What mixture of real and synthetic data, refresh rate, and source diversity prevents collapse across model sizes, objectives, and domains?
- Do the S17 findings on safety degradation and diversity generalize beyond Llama models, English, and single-turn instruction data?
- Which factuality, subgroup fairness, contamination, memorization, and safety metrics best predict deployment behavior?
- How should synthetic-data evaluation be calibrated when the generator, target model, and judge share model-family or stylistic biases?
- How effective are privacy safeguards for free-form LLM text against memorization and re-identification?
- Do reported synthetic-data gains persist on temporally new, adversarial, distribution-shifted, and independently collected real-world data?

**Analysis Duration:** 21.29s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The overall answer can be stated responsibly, but the most consequential new claim—synthetic fine-tuning potentially removing safety guardrails while preserving quality—comes from a secondary summary with narrow experimental scope. A primary-paper retrieval would materially improve confidence, and the real/synthetic mixture needed to avoid collapse remains unresolved.

**Next Search**

> "Synthetic Eggs in Many Baskets" synthetic data diversity LLM fine-tuning primary paper safety guardrails held-out human data

---

# Iteration 5

## 1. Search

**Query**

> "Synthetic Eggs in Many Baskets" synthetic data diversity LLM fine-tuning primary paper safety guardrails held-out human data

**Why this query**

The overall answer can be stated responsibly, but the most consequential new claim—synthetic fine-tuning potentially removing safety guardrails while preserving quality—comes from a secondary summary with narrow experimental scope. A primary-paper retrieval would materially improve confidence, and the real/synthetic mixture needed to avoid collapse remains unresolved.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S20 — Synthetic Eggs in Many Baskets:The Impact of Synthetic Data Diversity on LLM Fine-Tuning**
  URL: https://arxiv.org/html/2511.01490v3
- **S21 — Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning | Albert Gatt**
  URL: https://www.linkedin.com/posts/albert-gatt_synthetic-eggs-in-many-baskets-the-impact-activity-7392500258229993472-EQUP
- **S22 — Synthetic Data in AI: Breaking the Foundation Model Data Wall**
  URL: https://theholyquran.co.in/articles/synthetic-data-generation-privacy-preserving-diffusion-models-llm-pretraining-2026
- **S23 — Synthetic Data Pipelines for LLM Training - bards.ai**
  URL: https://www.bards.ai/services/synthetic-data

**Search Duration:** 2.80s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

New evidence reinforces that source diversity in synthetic fine-tuning can mitigate distribution collapse and preserve output diversity, but does not eliminate safety risks.

**Confidence:** Medium

**Why this confidence level**

S20 is a directly relevant empirical paper and closely matches prior S17 evidence, but the retrieved material is an abstract/introduction rather than complete results, and its scope is limited to the studied fine-tuning settings.

**Evidence**

- S20 reports that fine-tuning on synthetic data from diverse sources better preserves output-distribution breadth and textual diversity than lower-diversity synthetic data. [S20]
- S20 also reports reduced adversarial robustness after synthetic fine-tuning, including possible safeguard removal despite preserved output quality. [S20]
- S21 independently summarizes the same pattern: multiple synthetic sources can mitigate collapse, while low-diversity data makes smaller models more susceptible to harmful adversarial outputs. [S21]

#### Finding 2

**Claim**

Synthetic-data diversity affects evaluation-related self-preference bias, with human data appearing more effective than synthetic data and multi-source synthetic data more effective than single-source data.

**Confidence:** Medium

**Why this confidence level**

The finding is consistent with prior S11 and S17 evidence, but the retrieved text does not provide the complete statistical results or establish how broadly the effect generalizes.

**Evidence**

- S20 reports that fine-tuning reduces self-preference bias, with the strongest reduction from human data, followed by multi-source synthetic data, and the weakest from single-source synthetic data. [S20]
- S20 links self-preference concerns to LLM-as-judge evaluation and treats distributional changes as relevant to evaluator behavior. [S20]
- S21 summarizes the same result, stating that diverse synthetic data can reduce some self-bias but natural human data is substantially more effective. [S21]

#### Finding 3

**Claim**

The practical benefit of synthetic data depends heavily on filtering, deduplication, contamination checks, and provenance tracking rather than on generating large volumes of raw output.

**Confidence:** Medium

**Why this confidence level**

These recommendations align with the survey and prior evaluation findings, but S23 is a commercial provider describing its own practices and reported experience rather than an independent controlled study.

**Evidence**

- S23 characterizes raw synthetic output as containing hallucinations, repetition, formatting failures, and off-task responses, and describes retaining only a minority after filtering. [S23]
- S23 recommends reward-based quality scoring, human-calibrated thresholds, deduplication, format checks, n-gram and embedding contamination checks, and per-record provenance documentation. [S23]
- S23 recommends pilot fine-tuning and mixture ablations before full training, including comparisons of pure synthetic and mixed real/synthetic data. [S23]

#### Finding 4

**Claim**

Synthetic-data contamination can make benchmark results misleading, so contamination testing should cover both exact overlap and semantic or paraphrased similarity.

**Confidence:** Medium

**Why this confidence level**

The evaluation principle is strongly consistent with prior findings, but the numerical leakage examples reported by S23 are commercial claims without independently supplied methodology.

**Evidence**

- S23 warns that teacher models may reproduce benchmark questions and recommends n-gram and embedding-space checks against evaluation sets. [S23]
- The accumulated evidence likewise identifies contamination and memorization as reasons to use independent, real-world, and perturbation-tested evaluations. [S11] [S12] [S13]

#### Finding 5

**Claim**

Formal verification and execution-based filtering can improve the reliability of narrow synthetic domains such as mathematics and code, but the retrieved evidence does not establish that these methods solve general language factuality or bias problems.

**Confidence:** Low

**Why this confidence level**

S22 makes extensive quantitative and outcome claims without supplying verifiable study details and is hosted on an unrelated promotional-looking site; only the narrower description of proposed verification mechanisms is usable evidence.

**Evidence**

- S22 proposes theorem proving, code execution, and adversarial filtering as mechanisms for validating synthetic mathematical and programming examples. [S22]
- The broader evidence shows that factuality, distributional realism, diversity, and subgroup fairness still require independent validation even when synthetic data is curated. [S3] [S4] [S5] [S18]

### Conflicts Found

- S20 reports that greater synthetic-source diversity mitigates distribution collapse, while also reporting that synthetic fine-tuning can reduce adversarial robustness and remove safeguards. Thus improved diversity and output quality do not imply improved safety. [S20] [S21]
- S23 presents specific retention rates, contamination rates, benchmark leakage estimates, and operational success claims, but these are not independently corroborated in the retrieved material. They should be treated as practitioner reports rather than general empirical estimates. [S23]
- S22 claims extremely high verification rates, zero privacy or intellectual-property risk, and large downstream gains from proposed pipelines. These stronger claims conflict with the accumulated evidence that privacy, factuality, generalization, and bias must be empirically audited rather than inferred from synthetic generation or verification alone. [S22] [S1] [S5] [S7] [S18]
- S21 includes a comment suggesting that synthetic pretraining may outperform organic-data pretraining, but this is a user comment rather than reported evidence from the paper and is not sufficient to overturn the accumulated preference for mixed, validated data. [S21] [S1] [S2] [S3] [S6]

### Important Gaps

- Whether the S20 findings generalize beyond the studied models, languages, single-turn or supervised fine-tuning settings, and source-model configurations.
- What quantitative source-diversity, real-data-mixture, filtering, or refresh-rate requirements reliably prevent collapse while preserving safety.
- Whether improved synthetic-data diversity predicts better performance on temporally new, adversarial, subgroup-specific, and independently collected real-world evaluations.
- How to measure factuality and bias for general-language synthetic data when formal verification is unavailable.
- Whether the commercial contamination and filtering rates reported by S23 reproduce under independent audits.

**Analysis Duration:** 17.33s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The new evidence materially strengthens the existing conclusion: synthetic data offers scalable, targeted augmentation and can preserve diversity when sourced and curated carefully, but it can introduce factual, distributional, fairness, contamination, and safety failures. The central recommendation—use synthetic data as validated augmentation or distillation, retain independent real-world evaluation and preferably fresh real data, and audit multiple behavioral dimensions—is already supported by convergent evidence. Additional searches might refine mixture thresholds or metrics, but the retrieved evidence does not indicate that another search is necessary to answer the original question responsibly.

**Stop Reason:** sufficient_evidence

---

# Final Research Decision

**Research Stopped Because**

The analyzer determined that the important parts of the question could be answered responsibly.

**Stop Reason:** sufficient_evidence

**Searches Performed:** 5

**Unique Sources:** 23

**Remaining Uncertainty**

- Independent controlled studies across more model families, languages, domains, and multi-turn settings are needed to determine whether reported synthetic fine-tuning gains persist on deployment-like real data.
- A validated LLM-specific evaluation protocol combining factuality, distributional coverage, subgroup fairness, privacy leakage, contamination, robustness, safety, and downstream utility is not established by the retrieved sources.
- The amount and type of fresh real data needed to prevent collapse, and how this varies with source diversity and training objective, remain unresolved.
- It remains unclear how to evaluate factuality and bias in open-ended synthetic text where formal verification is unavailable.
- The effectiveness of privacy safeguards against memorization and re-identification in free-form LLM training data remains insufficiently quantified.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 5 | 16.49s |
| OpenAI Analysis | 5 | 97.70s |
| Report Generation | 1 | 28.81s |
| Total Run | — | 143.00s |
