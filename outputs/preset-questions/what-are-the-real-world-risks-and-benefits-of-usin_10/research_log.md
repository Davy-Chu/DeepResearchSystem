# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 10 / 10

**Unique Sources:** 38

**OpenAI Calls:** 11

**Tavily Calls:** 10

**Started:** 2026-09-01T05:13:30-04:00

**Ended:** 2026-09-01T05:16:49-04:00

**Total Runtime:** 199.07s

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

- **S1 — LLM synthetic data: Fine-tuning LLMs with AI-generated data | SuperAnnotate**
  URL: https://www.superannotate.com/blog/llm-synthetic-data
- **S2 — Synthetic Data Generation Using Large Language Models: Advances in Text and Code**
  URL: https://arxiv.org/html/2503.14023v1
- **S3 — Synthetic Data for AI Training: Use Cases and Risks [2026]**
  URL: https://atlan.com/know/ai-agent/data-for-ai/synthetic-data-for-ai-training
- **S4 — Recommendations on the Use of Synthetic Data to Train AI Models | United Nations University**
  URL: https://unu.edu/publication/recommendations-use-synthetic-data-train-ai-models
- **S5 — Synthetic Data Generation with LLMs: Techniques and Use Cases**
  URL: https://tetrate.io/learn/ai/synthetic-data-generation-llms

**Search Duration:** 4.13s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data can reduce the cost and time of obtaining training or fine-tuning data, and can expand datasets when labeled, domain-specific, or rare examples are difficult to collect.

**Confidence:** Medium

**Why this confidence level**

Multiple sources agree on the practical benefits, but the supplied material provides limited independent, task-specific evidence for the magnitude or durability of performance gains.

**Evidence**

- Synthetic examples can be generated rapidly and at scale, helping address data scarcity and high annotation costs; the survey reports benefits in low-resource tasks and cites performance improvements of 3–26% with synthetic augmentation in low-data regimes. [S1] [S2]
- Synthetic data is described as useful for rapid prototyping, data augmentation, class-imbalance mitigation, and domains where real data is expensive or unavailable. [S5]

#### Finding 2

**Claim**

Synthetic data can improve privacy and enable data sharing in sensitive domains, but it should not automatically be treated as anonymous or risk-free.

**Confidence:** Medium

**Why this confidence level**

The privacy benefit is consistently stated, while the material does not quantify re-identification, memorization, or leakage risk for LLM-generated datasets.

**Evidence**

- Sources identify privacy protection as a principal benefit because synthetic datasets can avoid directly using personal or sensitive records and can support work in healthcare and finance. [S1] [S2] [S5]
- The UNU policy brief says synthetic data can address privacy constraints but also identifies security and cybersecurity risks requiring responsible-use safeguards. [S4]

#### Finding 3

**Claim**

Synthetic data quality is conditional: generated text may contain factual errors, unrealistic style or distributional patterns, low diversity, and labels or examples that do not transfer reliably to real-world inputs.

**Confidence:** High

**Why this confidence level**

The quality limitations and possible generalization failure are directly and consistently described by multiple sources, including an institutional policy brief and a technical survey.

**Evidence**

- The survey identifies factual inaccuracies, insufficient stylistic or distributional realism, and the need for filtering, weighting, retrieval, and feedback-based validation. [S2]
- SuperAnnotate warns that poorly constructed synthetic data may produce models that perform poorly in practical settings and that training on synthetic scenarios can cause overfitting and weak real-world performance. [S1]
- The UNU brief cautions that synthetic data should not be assumed to be equivalent or superior to physical-world data and lists increased model error as a risk. [S4]

#### Finding 4

**Claim**

Bias may be reduced when generation is deliberately designed to fill representation gaps, but synthetic generation can also reproduce or amplify the biases of its source data or generator.

**Confidence:** High

**Why this confidence level**

The conditional nature of the bias benefit and the amplification risk are repeated across several sources; however, no subgroup-specific empirical results are supplied.

**Evidence**

- Synthetic data may be targeted at underrepresented classes and can provide more balanced representation when carefully designed. [S1] [S2] [S5]
- Sources warn that biases in human-generated or source data can be propagated or magnified, and the UNU brief specifically identifies bias propagation as a risk. [S1] [S2] [S4]

#### Finding 5

**Claim**

Recursive or poorly governed use of model-generated data can narrow the effective data distribution and degrade model quality, while weak provenance creates audit and failure-analysis problems.

**Confidence:** Medium

**Why this confidence level**

The sources converge on the risk and governance remedy, but the supplied excerpts do not provide controlled real-world measurements of collapse thresholds or audit effectiveness.

**Evidence**

- The survey identifies model collapse from iterative self-training on AI-generated data and recommends blending synthetic with real data. [S2]
- Atlan describes recursive synthetic-data training as causing model collapse and says lineage and fidelity metadata are needed to investigate failures. [S3]
- SuperAnnotate recommends combining synthetic and human data and using human or model-in-the-loop feedback to monitor and refine generated data. [S1]

#### Finding 6

**Claim**

Evaluation should test both the synthetic data and the resulting model against independent, human- or real-world-grounded criteria rather than relying only on synthetic benchmarks or automated model judges.

**Confidence:** Medium

**Why this confidence level**

The sources support a multi-layer evaluation approach, but they do not establish a validated standard metric or demonstrate when automated evaluation agrees with human and production outcomes.

**Evidence**

- The survey calls for robust evaluation frameworks and proposes filtering, weighting, retrieval, and execution feedback; it also notes automated verification for code. [S2]
- Synthetic data can be used to generate edge-case and adversarial evaluation sets, but its utility depends on validation and alignment with the target application's requirements. [S5]
- Human data and feedback loops are presented as ways to check realism, correct errors, and address bias; model-in-the-loop evaluation is proposed as a monitoring mechanism. [S1]

### Conflicts Found

- Synthetic data is characterized both as a privacy-preserving substitute that can avoid personal information and as a source of security or privacy risk. These claims are conditional: protection depends on how the data is generated, whether the generator memorizes source records, and whether privacy is actually tested. [S1] [S4] [S5]
- Synthetic data is described as capable of improving diversity and fairness, while other passages warn that it can amplify existing bias. This is not a direct factual contradiction; the outcome depends on generation controls, source-data bias, and subgroup evaluation. [S1] [S2] [S4]
- Some sources suggest synthetic data can sometimes replace human-labeled data, whereas other sources recommend blending it with human or real-world data because synthetic data may lack human nuance and realism. [S1] [S2] [S5]

### Important Gaps

- How much synthetic data can be added before performance on independent real-world data declines, and how does this vary by task, model, and domain?
- Which evaluation protocols best detect factuality errors, distribution shift, subgroup bias, memorization, and model collapse in LLM fine-tuning?
- Do reported low-resource performance gains persist on production workloads and under distribution shift, or mainly reflect improvements on synthetic or closely related benchmarks?
- What privacy testing is required to substantiate claims that LLM-generated data contains no exploitable personal information?
- How reliable are LLM-as-a-judge and other automated filters compared with expert human review, especially for minority-language, culturally specific, or safety-critical examples?

**Analysis Duration:** 16.51s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The current sources adequately identify the main benefits and risks, but they are mostly surveys, policy guidance, and vendor explainers. The central evaluation question remains weakly answered: there are no detailed controlled studies, independent benchmark results, subgroup analyses, or evidence on privacy leakage and real-world generalization. A focused search for empirical comparisons would materially improve the answer.

**Next Search**

> empirical study synthetic data LLM fine-tuning real-world evaluation bias model collapse data quality human data

---

# Iteration 2

## 1. Search

**Query**

> empirical study synthetic data LLM fine-tuning real-world evaluation bias model collapse data quality human data

**Why this query**

The current sources adequately identify the main benefits and risks, but they are mostly surveys, policy guidance, and vendor explainers. The central evaluation question remains weakly answered: there are no detailed controlled studies, independent benchmark results, subgroup analyses, or evidence on privacy leakage and real-world generalization. A focused search for empirical comparisons would materially improve the answer.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S6 — The Impact of Synthetic Data Diversity on LLM Fine-Tuning - arXiv**
  URL: https://arxiv.org/html/2511.01490v1
- **S7 — 1Introduction**
  URL: https://arxiv.org/html/2503.03150v2
- **S8 — Quality Matters: Evaluating Synthetic Data for Tool-Using LLMs**
  URL: https://arxiv.org/html/2409.16341v2
- **S9 — On LLMs-Driven Synthetic Data Generation, Curation, and Evaluation: A Survey | alphaXiv**
  URL: https://www.alphaxiv.org/abs/2406.15126
- **S10 — How to Synthesize Text Data to Avoid Model Collapse?**
  URL: https://openreview.net/forum?id=mVCcWCjeEz

**Search Duration:** 4.07s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data can deliver practical fine-tuning benefits when it is carefully validated: high-quality synthetic data may outperform much larger, unverified datasets, especially where human-labeled examples are scarce or expensive.

**Confidence:** High

**Why this confidence level**

S8 supplies direct comparative experiments, while prior sources provide convergent practical rationale. The evidence is strongest for tool-use tasks and does not establish universal gains across LLM applications.

**Evidence**

- In experiments on ToolBench and ToolAlpaca, models trained on smaller datasets filtered for quality performed better or comparably to models trained on larger, unverified synthetic datasets. [S8]
- The accumulated evidence identifies reduced collection and annotation costs, rapid generation, and usefulness in low-resource or specialized tasks as recurring benefits. [S1] [S2] [S5]

#### Finding 2

**Claim**

Synthetic-data quality is a central determinant of downstream performance; fluent generated examples can still contain incorrect instructions, invalid labels, faulty tool calls, or other errors that impair training.

**Confidence:** High

**Why this confidence level**

Direct dataset inspection and controlled downstream evaluation support the claim, although the error rates and generality beyond tool-use data are not established.

**Evidence**

- Inspection of synthetic tool-use datasets found numerous errors in both instructions and ground-truth API calls, and the authors emphasize that output-only evaluation can obscure these data problems. [S8]
- The survey describes synthetic data as vulnerable to noise, inconsistency, irrelevance, factual error, weak realism, and limited diversity, recommending filtering and reweighting. [S2] [S9]

#### Finding 3

**Claim**

Data curation and validation can improve the quality–quantity tradeoff: a smaller verified dataset may be more useful than a larger unvalidated one.

**Confidence:** High

**Why this confidence level**

S8 reports direct extrinsic comparisons on two benchmarks, supported by the survey’s broader workflow. The result remains task- and benchmark-dependent.

**Evidence**

- Human-defined correctness checks and model-driven in-context evaluation were used to filter data; models trained on the resulting high-quality subsets achieved better or comparable benchmark performance despite using less data. [S8]
- The survey presents generation, curation, and evaluation as an iterative workflow involving filtering, reweighting, and feedback from downstream performance. [S9]

#### Finding 4

**Claim**

Synthetic-data-induced distribution collapse is a genuine risk, but its severity depends on the data-generation process, source diversity, retention of real data, and how collapse is defined; catastrophic claims should not be generalized from unrealistic all-synthetic recursive-training setups.

**Confidence:** High

**Why this confidence level**

The new sources add both empirical findings and an important qualification to the earlier collapse narrative. Some uncertainty remains because definitions, experimental conditions, and real-world scaling behavior differ across studies.

**Evidence**

- S7 identifies at least eight inconsistent definitions of model collapse and argues that prominent catastrophic scenarios often assume repeated replacement of real data with purely synthetic data, conditions it considers unlike common frontier-model development. It nevertheless warns that the tails of the data distribution remain vulnerable. [S7]
- S6 reports that synthetic fine-tuning affects several distribution-collapse measures and that greater diversity of synthetic sources mitigates collapse and preserves broader output and linguistic diversity. [S6]
- Earlier sources also identify recursive self-training and narrowing distributions as risks and recommend retaining real data and tracking lineage. [S2] [S3]

#### Finding 5

**Claim**

Using multiple synthetic-data sources can reduce distribution narrowing, but synthetic fine-tuning may create distinctive safety and evaluation risks even when output quality remains high.

**Confidence:** Medium

**Why this confidence level**

These are direct findings from a new empirical study, but the supplied content does not provide full details on task breadth, replication, or deployment conditions.

**Evidence**

- S6 finds that source diversity mitigates distribution collapse. It also reports reduced adversarial robustness after synthetic fine-tuning while preserving higher output quality, potentially making weakened-safeguard outputs more usable and dangerous. [S6]
- S6 reports that fine-tuning can reduce self-preference bias, but the reduction is weakest for data generated by a single source model and strongest for human data. [S6]

#### Finding 6

**Claim**

Synthetic data can either reduce or amplify bias; representation balancing is a possible benefit, but generator and source-data biases can be propagated, and subgroup-specific testing is necessary.

**Confidence:** Medium

**Why this confidence level**

The conditional risk-benefit pattern is consistent across sources, but no supplied study reports robust subgroup-level fairness results for LLM fine-tuning.

**Evidence**

- Prior sources describe targeted synthesis as a way to fill representation gaps while warning that source or generator biases may be reproduced or magnified. [S1] [S2] [S4]
- The survey identifies human annotation bias and data-quality problems as motivations for synthetic data, but also frames curation and evaluation as necessary lifecycle stages rather than assuming generated data is neutral. [S9]

#### Finding 7

**Claim**

Evaluation should be layered: inspect synthetic examples directly, measure resulting models on independent human- or real-world-grounded tests, and test robustness, safety, diversity, and subgroup behavior rather than relying only on synthetic benchmarks or automated judges.

**Confidence:** High

**Why this confidence level**

Multiple sources support complementary evaluation layers, and S8 provides direct evidence that intrinsic data quality predicts downstream results. No universal evaluation standard is established.

**Evidence**

- S8 evaluates intrinsic data correctness and then measures downstream model performance, showing that data inspection changes conclusions that would be missed by extrinsic evaluation alone. [S8]
- S6 evaluates distributional diversity, adversarial robustness, and self-preference bias, illustrating evaluation dimensions beyond ordinary task accuracy. [S6]
- The survey recommends an iterative generation–curation–evaluation workflow, while prior sources recommend human review, feedback loops, and real-world validation. [S1] [S2] [S9]

### Conflicts Found

- Earlier sources present model collapse as a major recursive-training risk, while S7 argues that many catastrophic collapse claims rely on unrealistic assumptions and inconsistent definitions. The sources agree that distribution-tail and diversity degradation can occur, but disagree about how broadly catastrophic collapse should be expected. [S2] [S6] [S7]
- Synthetic data is described as capable of improving fairness through targeted representation, yet it may also reproduce or amplify bias. This is conditional rather than a direct contradiction; the outcome depends on generation controls, source diversity, and subgroup evaluation. [S1] [S2] [S4] [S9]
- Automated model-driven quality assessment is presented as agreeing substantially with expert annotations in S8, while the accumulated evidence cautions that automated judges can have self-preference and other biases. Agreement in one tool-use study does not establish reliability across domains or minority and safety-critical cases. [S6] [S8]

### Important Gaps

- What subgroup-specific empirical effects does synthetic fine-tuning have on fairness, representation, and error rates across languages and demographic or cultural groups?
- How well do intrinsic quality metrics and automated evaluators transfer beyond tool-use datasets, and when do they fail relative to expert human review?
- What mixture of real and synthetic data best preserves tail coverage and production performance under distribution shift?
- How much do the reported robustness and self-preference effects in S6 replicate across models, generators, and fine-tuning tasks?
- What privacy and memorization tests are needed to verify that generated training data does not expose information from its source records?

**Analysis Duration:** 17.01s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new evidence substantially improves the answer on data quality, evaluation design, and the conditional nature of model collapse. However, the original question’s bias focus remains supported mainly by general warnings rather than subgroup-level empirical evidence, which is an important gap for assessing real-world risk.

**Next Search**

> empirical fairness bias evaluation synthetic data fine-tuning large language models subgroup performance real-world

---

# Iteration 3

## 1. Search

**Query**

> empirical fairness bias evaluation synthetic data fine-tuning large language models subgroup performance real-world

**Why this query**

The new evidence substantially improves the answer on data quality, evaluation design, and the conditional nature of model collapse. However, the original question’s bias focus remains supported mainly by general warnings rather than subgroup-level empirical evidence, which is an important gap for assessing real-world risk.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S11 — Fairness by design: End-to-end bias evaluation for LLM-generated data**
  URL: https://resources.flatiron.com/publications/fairness-by-design-end-to-end-bias-evaluation-for-llm-generated-data
- **S12 — Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs - Apple Machine Learning Research**
  URL: https://machinelearning.apple.com/research/fairly-certain
- **S13 — Guide to Ethical Fine-Tuning of Large Language Models | Tonic.ai**
  URL: https://www.tonic.ai/guides/ethical-fine-tuning-llm-synthetic-data
- **S14 — Using Synthetic Data to Improve LLM Fine‑Tuning - Newline**
  URL: https://www.newline.co/@Dipen/using-synthetic-data-to-improve-llm-finetuning--d453f658

**Search Duration:** 3.58s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Fairness evaluation for LLM-generated or LLM-curated data should examine subgroup-specific performance and validate downstream real-world outcomes, not rely on aggregate accuracy alone.

**Confidence:** Medium

**Why this confidence level**

S11 provides a concrete, real-world healthcare example and a multi-part validation framework, but it concerns LLM-generated/curated clinical data rather than synthetic data used directly for LLM fine-tuning.

**Evidence**

- A clinical EHR study evaluated LLM-extracted data by comparing it with human abstraction, checking consistency and plausibility, and replicating clinical outcomes in large cohorts. It found modest differences by race/ethnicity and lower recall for patients aged 75 and older, while downstream survival estimates were largely consistent. [S11]
- The study illustrates that small subgroup differences can coexist with acceptable aggregate or downstream performance, making explicit subgroup analysis necessary. [S11]

#### Finding 2

**Claim**

Conventional fairness metrics based only on prediction correctness can miss important disparities in model confidence and uncertainty.

**Confidence:** Medium

**Why this confidence level**

S12 is a named research benchmark with evaluations across ten open-source LLMs, but the supplied material does not establish how well the metric predicts deployment harms or how it applies specifically to synthetic-data fine-tuning.

**Evidence**

- The proposed UCerF metric evaluates uncertainty-aware fairness and reports that Mistral-7B made highly confident incorrect predictions that were not captured by Equalized Odds. [S12]

#### Finding 3

**Claim**

Synthetic-data evaluation should include fairness dimensions beyond accuracy, including confidence calibration, subgroup error rates, and representation or data-quality differences.

**Confidence:** High

**Why this confidence level**

The new sources complement multiple prior sources and jointly support a multidimensional evaluation approach, although no universal standard is established.

**Evidence**

- S12 identifies dataset diversity and clarity limitations and proposes a larger gender-occupation dataset to support more fine-grained fairness evaluation. [S12]
- S11 demonstrates that race/ethnicity- and age-specific recall and precision differences can be detected through comparison with human-labeled data and real-world outcome replication. [S11]
- Prior evidence already supports layered evaluation of synthetic examples, downstream task performance, robustness, diversity, safety, and subgroup behavior. [S6] [S8] [S9]

#### Finding 4

**Claim**

The new sources strengthen the case that synthetic data may support scalable, privacy-sensitive or domain-specific workflows only when paired with independent validation; they do not provide strong new evidence that synthetic data itself improves LLM fine-tuning outcomes.

**Confidence:** High

**Why this confidence level**

The scope of each new source is explicit in the retrieved content; the direct evidence remains concentrated in earlier tool-use and synthetic-fine-tuning studies.

**Evidence**

- S11 reports successful validation of LLM-curated clinical datasets against human abstraction and cohort-level outcomes, but does not study fine-tuning on synthetic data. [S11]
- S12 evaluates fairness benchmarks and metrics for existing LLMs rather than comparing real-data and synthetic-data fine-tuning. [S12]
- S13 and S14 are primarily practitioner or commercial guidance pages in the supplied excerpts and provide no detailed empirical comparison of fine-tuning outcomes. [S13] [S14]

### Conflicts Found

- S11 reports minor subgroup differences alongside broadly consistent downstream clinical outcomes, while S12 argues that confidence-sensitive metrics can reveal fairness problems missed by conventional accuracy metrics. These are complementary rather than direct contradictions: acceptable aggregate outcomes do not rule out subgroup or uncertainty-related harms. [S11] [S12]
- The accumulated evidence recommends human- and real-world-grounded evaluation, while S12 introduces an automated uncertainty-aware benchmark. The sources differ in emphasis, but the benchmark should be treated as an additional diagnostic rather than a replacement for human and deployment validation. [S11] [S12] [S8] [S9]

### Important Gaps

- What subgroup-specific fairness effects result directly from fine-tuning on synthetic data, rather than from using LLMs to extract or generate evaluation data?
- Whether uncertainty-aware fairness metrics such as UCerF reliably predict production harms across domains, languages, and safety-critical applications remains untested in the supplied evidence.
- How do synthetic-data mixtures affect confidence calibration and subgroup error disparities compared with equivalent real-data mixtures?
- The supplied material still lacks direct privacy and memorization tests for LLM-generated training examples.
- S13 and S14 do not add independently verifiable quantitative evidence about quality, bias, or real-world fine-tuning benefits.

**Analysis Duration:** 11.58s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources materially improve the evaluation discussion, especially subgroup validation and uncertainty-aware fairness, but the most important remaining gap is direct empirical evidence on fairness and calibration after synthetic-data fine-tuning. A focused search could determine whether such comparisons exist.

**Next Search**

> empirical study synthetic data fine-tuning LLM subgroup fairness calibration bias real-world evaluation

---

# Iteration 4

## 1. Search

**Query**

> empirical study synthetic data fine-tuning LLM subgroup fairness calibration bias real-world evaluation

**Why this query**

The new sources materially improve the evaluation discussion, especially subgroup validation and uncertainty-aware fairness, but the most important remaining gap is direct empirical evidence on fairness and calibration after synthetic-data fine-tuning. A focused search could determine whether such comparisons exist.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S15 — Advancing Algorithmic Fairness via Selectively Fine-Tuning ...**
  URL: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_AIM-Fair_Advancing_Algorithmic_Fairness_via_Selectively_Fine-Tuning_Biased_Models_with_CVPR_2025_paper.pdf
- **S16 — Synthetic Data for Bias Mitigation 2026: 5 Methods + FAGI**
  URL: https://futureagi.com/blog/synthetic-data-generation-bias-2025
- **S17 — Synthetic Data + Evaluation Pipelines: Scaling Fine-Tuning ...**
  URL: https://medium.com/@akankshasinha247/synthetic-data-evaluation-pipelines-scaling-fine-tuning-without-losing-alignment-f469a81cdf9a
- **S18 — Synthetic Data Generation Strategies for Fine-Tuning LLMs | Scale AI**
  URL: https://scale.com/blog/synthetic-data-fine-tuning-llms

**Search Duration:** 4.10s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data can improve fairness when deliberately targeted at underrepresented groups, but its benefits depend on synthetic-data quality and the gap between synthetic and real data distributions.

**Confidence:** Medium

**Why this confidence level**

S15 is a peer-reviewed CVPR study with experiments, but it concerns image classification rather than LLM fine-tuning, so transfer to language models is indirect.

**Evidence**

- AIM-Fair reports that balanced synthetic data can improve worst-group fairness, but naïve synthetic fine-tuning may reduce overall utility because of low-quality generation and domain and bias shifts between synthetic and real data. [S15]
- The study’s proposed selective fine-tuning and contextual generation improved fairness while maintaining utility on CelebA and UTKFace, indicating that generation and fine-tuning strategy jointly affect outcomes. [S15]

#### Finding 2

**Claim**

The new evidence reinforces that synthetic-data quality and distributional alignment are prerequisites for reliable bias mitigation; synthetic data is not automatically fair merely because it is balanced.

**Confidence:** High

**Why this confidence level**

This conclusion is consistent with the prior technical and empirical evidence, although S16 is practitioner guidance rather than independent research.

**Evidence**

- S15 identifies low quality, low diversity, and domain/bias gaps as central failure modes. It reports that balanced synthetic data alone may improve fairness while harming accuracy because of the real–synthetic domain gap. [S15]
- S16 recommends validating distributional fit, utility, privacy, and subgroup fairness before retraining, then re-auditing on held-out tests and using a real-plus-synthetic mixture. [S16]

#### Finding 3

**Claim**

Synthetic-data generation strategies can be selected for cost-effectiveness rather than maximizing dataset size; the best strategy depends on the available generation budget and task.

**Confidence:** Medium

**Why this confidence level**

S18 describes controlled experiments across multiple tasks, but it is a vendor account of its own work and the supplied excerpt provides no detailed effect sizes, statistical uncertainty, or independent replication.

**Evidence**

- Scale’s experiments across mathematics, general question answering, and Text2SQL found that answer augmentation was most effective under limited query budgets, while generating new questions became more effective as the budget increased. [S18]
- The study reports that rephrasing was relatively robust to weaker augmentation models and that strategy differences mattered less in data-rich settings. [S18]

#### Finding 4

**Claim**

Evaluation should be treated as a closed loop: diagnose subgroup and coverage gaps, validate synthetic records, compare models on held-out real-world data, and repeat the fairness audit after fine-tuning.

**Confidence:** High

**Why this confidence level**

The evaluation recommendation is supported by multiple prior sources and is consistent with the new workflow guidance, though no universal evaluation standard has been established.

**Evidence**

- S16 proposes subgroup error analysis, coverage mapping, synthetic-data validation, retraining on real-plus-synthetic data, and re-auditing on held-out tests. [S16]
- Prior evidence independently supports inspecting synthetic examples and evaluating downstream performance, robustness, safety, diversity, confidence, and subgroup behavior. [S6] [S8] [S9] [S11] [S12]

#### Finding 5

**Claim**

The new sources do not resolve the main evidence gap: there is still little direct, independent evidence on how synthetic data affects subgroup fairness, privacy, and production performance when used specifically to fine-tune LLMs.

**Confidence:** High

**Why this confidence level**

The scope and limitations of the new sources are explicit, and they leave the previously identified LLM-specific evidence gaps substantially unresolved.

**Evidence**

- S15 studies synthetic-data fairness in computer-vision classification rather than language-model fine-tuning. [S15]
- S16 and S17 provide practitioner guidance, while S18 reports vendor-led experiments focused primarily on cost and task accuracy rather than subgroup fairness, privacy, or deployment outcomes. [S16] [S17] [S18]
- Prior sources likewise identify the absence of direct privacy/memorization tests and robust subgroup-specific synthetic-fine-tuning results for LLMs. [S6] [S11] [S12]

### Conflicts Found

- S15 shows that balanced synthetic data can improve fairness but lower utility because of domain shift, whereas its proposed selective fine-tuning preserves utility. This qualifies—not contradicts—the broader claim that synthetic data may improve fairness: the outcome depends on how the model handles the synthetic–real gap. [S15]
- S18 reports that verification of synthetic responses had less impact in its constrained experiments, while the broader evidence recommends strong verification and independent evaluation because synthetic errors can substantially impair downstream performance. The difference may reflect task, dataset, or experimental-setting dependence rather than a general disagreement. [S8] [S18]
- S16 presents synthetic generation as a practical route to correcting representation gaps, while prior empirical and survey evidence warns that generators can reproduce or amplify source and model biases. The claims are conditional and require subgroup-level validation. [S1] [S2] [S4] [S15] [S16]

### Important Gaps

- What are the subgroup-specific effects of synthetic-data fine-tuning on LLMs across demographic groups, languages, dialects, and cultural contexts?
- How much synthetic data can be mixed with real data before factuality, calibration, tail coverage, or production performance declines?
- Do synthetic-data fairness gains persist under real-world distribution shift rather than only on held-out benchmark tests?
- What privacy, memorization, and re-identification tests establish that generated training examples do not expose source-record information?
- How reliable are automated filters and LLM-as-a-judge systems for detecting factual, cultural, minority-language, and safety-critical errors?
- How well do the cost-effectiveness findings in S18 replicate across larger models, generators, domains, and deployment settings?

**Analysis Duration:** 13.95s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources strengthen the general conclusion that synthetic data can be useful when curated and evaluated, and provide evidence that targeted synthesis can improve fairness in computer vision. However, the original question is specifically about large language models, and direct evidence on LLM subgroup fairness, privacy leakage, and real-world performance remains insufficient. A focused search could materially improve the answer.

**Next Search**

> empirical study synthetic data fine-tuning LLM fairness subgroup bias real-world evaluation privacy memorization

---

# Iteration 5

## 1. Search

**Query**

> empirical study synthetic data fine-tuning LLM fairness subgroup bias real-world evaluation privacy memorization

**Why this query**

The new sources strengthen the general conclusion that synthetic data can be useful when curated and evaluated, and provide evidence that targeted synthesis can improve fairness in computer vision. However, the original question is specifically about large language models, and direct evidence on LLM subgroup fairness, privacy leakage, and real-world performance remains insufficient. A focused search could materially improve the answer.

**Results**

5 results retrieved.

2 new unique sources added.

### Sources

- **S19 — LLM Security & Privacy**
  URL: https://github.com/chawins/llm-sp
- **S20 — Privacy-Preserving Fair Synthetic Tabular Data**
  URL: https://arxiv.org/html/2503.02968v1

**Search Duration:** 4.73s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data is not inherently private: generators may memorize training records, permit re-identification or reconstruction, and require explicit privacy testing or formal protections.

**Confidence:** High

**Why this confidence level**

S20 provides a direct discussion of memorization, reconstruction, differential privacy, and the privacy–utility tradeoff, although the evidence concerns tabular generators rather than LLM-generated text.

**Evidence**

- S20 states that synthetic-data generators can memorize training data, allowing real samples to reappear or enabling reconstruction attacks; it describes differential privacy as a mitigation but notes that added noise reduces utility. [S20]
- This directly strengthens the prior conclusion that synthetic data should not automatically be treated as anonymous or risk-free. [S4] [S20]

#### Finding 2

**Claim**

Privacy, fairness, and utility in synthetic data are coupled objectives: improving privacy or fairness can reduce fidelity or downstream usefulness, so evaluation must measure all three rather than treating any one as sufficient.

**Confidence:** Medium

**Why this confidence level**

The source reports comparative experiments, but they are on tabular data and do not establish how the tradeoffs behave for LLM fine-tuning.

**Evidence**

- S20 presents a generator with simultaneous privacy and fairness constraints and reports a tradeoff among utility, privacy, and fairness across four tabular datasets. [S20]
- S20 explains that differential-privacy noise can reduce synthetic-data utility and that fairness constraints address, but do not automatically eliminate, bias. [S20]

#### Finding 3

**Claim**

Fairness improvements require deliberate controls and validation; synthetic data can reproduce or amplify source-data bias unless the generation process explicitly addresses it.

**Confidence:** High

**Why this confidence level**

The conditional risk-benefit pattern is consistent across the new and accumulated sources, though direct subgroup results for synthetic-data fine-tuning of LLMs remain absent.

**Evidence**

- S20 says biases in real or de-identified data can lead to unfair outcomes and describes fairness-constrained generation as a way to address those biases. [S20]
- This is consistent with prior evidence that balancing or targeting underrepresented groups can help, but generator and source-data biases can also be propagated. [S1] [S2] [S4] [S15]

#### Finding 4

**Claim**

The new material adds little direct evidence about the benefits or risks of using synthetic data specifically to train or fine-tune LLMs; the strongest new evidence is domain-general and tabular.

**Confidence:** High

**Why this confidence level**

The scope and content of both new sources are explicit. They inform privacy and security framing but do not close the LLM-specific evidence gap.

**Evidence**

- S20 evaluates privacy, fairness, and utility for synthetic tabular-data generators, not language-model training or fine-tuning. [S20]
- S19 is a curated GitHub bibliography of LLM security and privacy papers. Its displayed content mainly lists prompt-injection and application-security work and does not report an empirical study of synthetic training data, data quality, bias, or fine-tuning outcomes. [S19]

### Conflicts Found

- S20 presents synthetic data as offering enhanced privacy because it lacks a one-to-one relationship with real records, but also documents memorization, re-identification, and reconstruction risks. The apparent tension is conditional: privacy depends on generator behavior and testing, not merely on synthetic status. [S20]
- S20 reports that fairness-constrained generation can improve fairness, while also stating that biased source data can produce unfair synthetic data. These claims are compatible: fairness gains require explicit constraints and validation and may involve utility tradeoffs. [S20] [S15]
- S20 reports privacy–utility and fairness–utility tradeoffs, whereas prior sources emphasize synthetic data's scalability and practical usefulness. These are not direct contradictions, but they indicate that cost and scale benefits may come at the expense of fidelity, privacy, or fairness unless carefully managed. [S1] [S2] [S5] [S20]

### Important Gaps

- What privacy and memorization tests—such as extraction, membership-inference, reconstruction, or re-identification tests—are effective for LLM-generated training examples?
- How do privacy-preserving mechanisms affect the quality, factuality, calibration, subgroup performance, and fine-tuning utility of synthetic text?
- Do privacy and fairness tradeoffs observed in tabular synthetic data transfer to LLM-generated text and instruction data?
- What direct empirical evidence compares real-data, synthetic-data, and mixed-data LLM fine-tuning on independent production-like evaluations?
- How reliable are automated quality and fairness filters for detecting privacy leakage and subgroup-specific harms in synthetic language data?

**Analysis Duration:** 10.86s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

An important original-question gap remains: the new sources strengthen general privacy and fairness cautions but do not provide direct, independent evidence on LLM fine-tuning outcomes, privacy leakage, or subgroup effects. A focused search for empirical LLM-specific privacy and memorization studies would materially improve the answer.

**Next Search**

> empirical study LLM synthetic data fine-tuning privacy memorization membership inference data extraction subgroup fairness

---

# Iteration 6

## 1. Search

**Query**

> empirical study LLM synthetic data fine-tuning privacy memorization membership inference data extraction subgroup fairness

**Why this query**

An important original-question gap remains: the new sources strengthen general privacy and fairness cautions but do not provide direct, independent evidence on LLM fine-tuning outcomes, privacy leakage, or subgroup effects. A focused search for empirical LLM-specific privacy and memorization studies would materially improve the answer.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S21 — SOFT: Selective Data Obfuscation for Protecting LLM Fine-tuning against Membership Inference Attacks | USENIX**
  URL: https://www.usenix.org/conference/usenixsecurity25/presentation/zhang-kaiyuan
- **S22 — Hidden Dangers of Fine-tuning Large Language Models ...**
  URL: https://www.usenix.org/system/files/usenixsecurity25-akkus.pdf
- **S23 — Targeted Training Data Extraction—Neighborhood Comparison-Based Membership Inference Attacks in Large Language Models**
  URL: https://www.mdpi.com/2076-3417/14/16/7118
- **S24 — Assessing and Mitigating Data Memorization Risks in Fine ...**
  URL: https://arxiv.org/html/2508.14062v1
- **S25 — Our Research on Membership Inference Attacks and Preventing Privacy Leaks - The JetBrains Blog**
  URL: https://blog.jetbrains.com/research/2026/06/membership-inference

**Search Duration:** 3.26s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Fine-tuning on LLM-generated data does not necessarily provide privacy protection and may increase privacy leakage relative to the presumed benefit of avoiding real records.

**Confidence:** High

**Why this confidence level**

S22 directly evaluates the specific scenario in the question—LLM fine-tuning on generated data—with attack-based privacy measurements. Generalization beyond the reported models and setups remains uncertain.

**Evidence**

- S22 empirically studies supervised fine-tuning and self-instruct tuning using LLM-generated data, measuring personally identifiable information extraction and membership-inference attacks. In its reported experiments, PII extraction for Pythia increased by more than 20% after fine-tuning on unstructured generated data, while the ROC-AUC of membership-inference attacks against Pythia-6.9B increased by more than 40% after self-instruct tuning. [S22]
- S22 attributes the risk to the increasing indistinguishability between generated and real data and concludes that generated data can exacerbate, rather than mitigate, privacy risk. [S22]

#### Finding 2

**Claim**

Fine-tuning itself can make membership information easier to infer, so privacy evaluation should include attacks against the final fine-tuned model rather than assessing only the source dataset.

**Confidence:** Medium

**Why this confidence level**

The sources provide direct empirical claims, but S24 is an arXiv preprint and the supplied excerpts do not give enough methodological detail to assess robustness or reproduce the headline percentages.

**Evidence**

- S21 reports a study across six domains, multiple LLM architectures, and model scales finding that membership-inference attacks exploit loss reduction during fine-tuning and can reveal whether examples were included in the fine-tuning data. [S21]
- S24 reports controlled experiments with GPT-2, Phi-3, and Gemma-2 in which repeated exposure to sensitive data increased reported leakage rates from 0–5% at baseline to 60–75%, and evaluates deduplication, differential privacy, entropy filtering, and pattern filtering as mitigations. [S24]

#### Finding 3

**Claim**

Synthetic-data privacy benefits are conditional: generated examples can reduce direct use of real records, but generator memorization, fine-tuning dynamics, and overlap with pretraining data can still expose sensitive information.

**Confidence:** High

**Why this confidence level**

The new evidence directly resolves the earlier uncertainty about whether synthetic status alone establishes privacy: it does not. Exact risk levels for different generation pipelines remain unresolved.

**Evidence**

- S22 explains that developers may choose generated data to avoid privacy risks associated with real-data fine-tuning, but reports PII extraction and membership-inference increases after generated-data fine-tuning. [S22]
- S20 previously documented memorization, reconstruction, and re-identification risks in synthetic-data generation, while S21 and S24 show that fine-tuning can create or amplify leakage risks in the resulting LLM. [S20] [S21] [S24]

#### Finding 4

**Claim**

Privacy evaluation for synthetic-data fine-tuning should measure both data exposure and model-level attackability, including PII extraction, membership inference, memorization or reconstruction tests, and leakage through the deployed access interface.

**Confidence:** High

**Why this confidence level**

Multiple sources converge on attack-based, model-level privacy testing and cover complementary threat models. No single standardized privacy evaluation protocol is established.

**Evidence**

- S22 uses PII extraction and membership-inference attacks to evaluate generated-data fine-tuning, including both ordinary querying and, in a more severe threat model, access to output logits. [S22]
- S21 frames membership inference as a practical risk for fine-tuned models and evaluates a defense intended to balance privacy protection against retained model utility. [S21]
- S24 evaluates memorization through leakage tests and proposes multiple preprocessing and training-time mitigations rather than relying on aggregate task accuracy alone. [S24]

#### Finding 5

**Claim**

Privacy mitigations introduce a utility tradeoff, so a privacy intervention should be evaluated jointly on leakage reduction and independent task performance.

**Confidence:** Medium

**Why this confidence level**

The tradeoff is supported by empirical and comparative evidence, but S20 concerns tabular generators and S24 is a preprint; the reported utility retention should not be treated as universal.

**Evidence**

- S21 describes SOFT as using selective data obfuscation with an adjustable privacy–utility parameter and reports reduced privacy risk with competitive model performance. [S21]
- S20 reports privacy–utility tradeoffs for synthetic data, and S24 reports that its proposed combination of protections reduced leakage while retaining 94.7% of original utility in its experiments. [S20] [S24]

#### Finding 6

**Claim**

The new evidence strengthens the privacy-risk portion of the answer but leaves the central LLM-specific evidence gaps on data quality, subgroup bias, and production evaluation largely unresolved.

**Confidence:** High

**Why this confidence level**

The scope of the new sources is explicit, and none directly supplies the missing quality, bias, or production-comparison evidence.

**Evidence**

- S22 focuses on privacy attacks in generated-data fine-tuning and does not report subgroup fairness, factuality, or production-distribution outcomes. [S22]
- S21 evaluates privacy defenses for fine-tuned LLMs rather than comparing real, synthetic, and mixed training data on quality or fairness outcomes. [S21]
- S23 concerns targeted training-data extraction, but the supplied page content does not provide substantive results about synthetic-data fine-tuning, data quality, or subgroup behavior. [S23]
- Prior evidence still lacks robust, independent comparisons of synthetic versus real or mixed data for LLM fine-tuning across subgroup fairness, calibration, factuality, and deployment performance. [S6] [S8] [S11] [S12] [S15] [S18] [S20]

### Conflicts Found

- Synthetic data is often presented as a privacy-preserving alternative to real data, but S22 finds that fine-tuning on LLM-generated data can increase PII extraction and membership-inference success. The claims are conditional rather than mutually exclusive: synthetic data may reduce direct record sharing while still transferring or amplifying sensitive information through the generator or fine-tuned model. [S1] [S4] [S20] [S22]
- S21 presents SOFT as reducing membership-inference risk while preserving competitive utility, whereas S22 and S24 emphasize that fine-tuning— including on generated data—can increase leakage. These findings concern different interventions and data conditions, so they support a mitigation-versus-baseline distinction rather than a direct contradiction. [S21] [S22] [S24]
- S22 reports substantial privacy risk from generated-data fine-tuning, while earlier sources mainly describe synthetic data as potentially privacy-enhancing. The new source provides more direct evidence for the previously noted caveat that synthetic data should not be presumed anonymous. [S1] [S2] [S5] [S22]
- S24 reports very large leakage increases and near-complete mitigation with its combined methods, but the supplied evidence does not establish whether those magnitudes or mitigation results replicate across generation procedures, datasets, and production LLMs. [S24]

### Important Gaps

- How do S22's privacy findings vary with the generator model, prompt design, source-data overlap, synthetic-data deduplication, and the proportion of synthetic data used?
- Do PII extraction and membership-inference increases reported by S22 persist under API-only access, or are they substantially dependent on logit access and attack assumptions?
- What direct experiments compare real-data, synthetic-data, and mixed-data LLM fine-tuning on factuality, data quality, subgroup fairness, calibration, robustness, and production-like tasks?
- Which privacy defenses remain effective when synthetic data is used for instruction tuning, preference optimization, or repeated recursive generation?
- How should privacy risk be balanced against utility, factuality, tail coverage, and subgroup performance when applying obfuscation, deduplication, filtering, or differential privacy?
- Do the reported privacy findings transfer across languages, dialects, rare populations, and safety-critical domains?
- How reliable are attack-based privacy metrics as predictors of real-world disclosure harm under deployed model interfaces?

**Analysis Duration:** 18.68s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources materially improve the answer on privacy and memorization, including direct evidence for generated-data fine-tuning, but important parts of the original question remain weakly evidenced—especially direct LLM-specific effects on data quality, subgroup bias, calibration, and real-world performance.

**Next Search**

> empirical comparison real synthetic mixed data LLM fine-tuning subgroup fairness factuality calibration production evaluation

---

# Iteration 7

## 1. Search

**Query**

> empirical comparison real synthetic mixed data LLM fine-tuning subgroup fairness factuality calibration production evaluation

**Why this query**

The new sources materially improve the answer on privacy and memorization, including direct evidence for generated-data fine-tuning, but important parts of the original question remain weakly evidenced—especially direct LLM-specific effects on data quality, subgroup bias, calibration, and real-world performance.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S26 — Calibrating Long-form Generations from Large Language Models**
  URL: https://arxiv.org/html/2402.06544v1
- **S27 — Synthetic Data for LLM Fine-Tuning 2026**
  URL: https://futureagi.com/blog/synthetic-data-fine-tuning-llms
- **S28 — Fair and square? Evaluating fairness of LLM-generated ...**
  URL: https://doi.org/10.1016/j.infsof.2025.107980

**Search Duration:** 3.80s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Calibration is an important additional evaluation dimension for models fine-tuned on synthetic data, especially for long-form generation where answers can be partially correct rather than simply right or wrong.

**Confidence:** High

**Why this confidence level**

S26 directly addresses calibration methodology for LLM text generation, though it does not specifically study synthetic-data fine-tuning.

**Evidence**

- S26 proposes treating both response correctness and model confidence as distributions over degrees of correctness, because binary accuracy does not adequately represent long-form QA and summarization quality. [S26]

#### Finding 2

**Claim**

Fine-tuning can improve calibration, but calibration results depend on the metric and evaluation method; larger or stronger models are not necessarily better calibrated.

**Confidence:** Medium

**Why this confidence level**

The source reports experiments across long-form QA and summarization, but the supplied content does not establish whether the findings transfer to synthetic-data fine-tuning or production settings.

**Evidence**

- S26 reports that calibration is metric-dependent, larger models do not necessarily calibrate better, and fine-tuning and temperature scaling improved calibration across the study's metrics. [S26]

#### Finding 3

**Claim**

Synthetic-data workflows can be economically attractive because they scale task-specific examples from a small human seed, but the claimed benefits depend on filtering, diversity controls, and retaining real data.

**Confidence:** Medium

**Why this confidence level**

S27 gives a clear practitioner description of the workflow and risks, but it is vendor-authored guidance rather than independent empirical evidence and provides no reproducible effect sizes.

**Evidence**

- S27 describes workflows that expand a small set of human-written seeds into instruction, preference, tool-use, or retrieval examples and presents this as a way to reduce labeling cost and increase coverage. [S27]
- S27 explicitly identifies mode collapse and inheritance of a single teacher's formatting, refusal style, and length distribution as tradeoffs, recommending multiple teachers, real-data seeds, and diversity checks. [S27]

#### Finding 4

**Claim**

Synthetic-data quality must be evaluated against the fine-tuning objective and schema, not merely judged by fluent text or aggregate benchmark scores.

**Confidence:** High

**Why this confidence level**

The recommendation is supported by direct tool-use evidence in S8 and a consistent workflow description in S27, although broader domain-specific validation remains limited.

**Evidence**

- S27 distinguishes SFT pairs, preference triples, tool-call traces, and RAG examples, and recommends a pipeline of seed design, generation, quality filtering, and format conversion tailored to the target recipe. [S27]
- This complements S8's finding that inspecting instructions and ground-truth tool calls can reveal errors that output-only model evaluation misses. [S8] [S27]

#### Finding 5

**Claim**

Evaluation of synthetic-data fine-tuning should include confidence calibration and uncertainty-sensitive subgroup analysis in addition to accuracy, factuality, robustness, and privacy tests.

**Confidence:** High

**Why this confidence level**

The combined evidence supports calibration as a useful additional diagnostic, while acknowledging that S26 does not specifically test synthetic-data training.

**Evidence**

- S26 shows that long-form correctness is graded and uncertain, and provides metrics for comparing confidence with degrees of correctness; prior evidence identifies subgroup error rates and confidence disparities as necessary fairness dimensions. [S26] [S11] [S12]
- The accumulated evidence already supports layered evaluation of the data itself and the resulting model on independent real-world-grounded tests. [S6] [S8] [S9] [S11] [S12]

### Conflicts Found

- S27 presents synthetic data as a practical way to scale fine-tuning data and reduce labeling costs, while the accumulated empirical evidence warns that scale alone can worsen quality, distribution coverage, bias, or privacy. These positions are conditional rather than directly contradictory: the benefit depends on validation, teacher diversity, and real-data anchoring. [S27] [S8] [S15] [S22]
- S26 reports that fine-tuning can improve calibration, whereas the broader evidence warns that synthetic fine-tuning can reduce adversarial robustness and create other hidden failures. Improved confidence calibration therefore should not be interpreted as evidence of overall safety or quality. [S26] [S6]
- S27 recommends judge-based filtering as a practical quality-control step, while earlier evidence cautions that automated judges may have self-preference or domain and subgroup biases. Judge agreement must therefore be checked against human and independent real-world evaluation. [S27] [S6] [S8]

### Important Gaps

- Does synthetic-data fine-tuning improve calibration relative to equivalent real-data or mixed-data fine-tuning, and does calibration improvement persist under real-world distribution shift?
- Do the workflow claims in S27 replicate independently across models, teachers, domains, and fine-tuning objectives?
- What fairness, privacy, factuality, and calibration effects result from the specific synthetic workflows described in S27, especially DPO, constitutional, tool-use, and RAG data?
- What empirical results and methodology are reported in S28, including subgroup metrics, dataset construction, model-training conditions, and independent test performance?
- Can confidence-calibration metrics for long-form generation reliably predict production harms, particularly for minority-language, culturally specific, or safety-critical outputs?

**Analysis Duration:** 13.21s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources add a useful calibration dimension and practical workflow context, but they do not close the central evidence gap: independent, LLM-specific comparisons of real, synthetic, and mixed fine-tuning on data quality, subgroup bias, calibration, privacy, and production-like outcomes. S28 appears potentially relevant to fairness but the retrieved content is incomplete.

**Next Search**

> "Fair and square? Evaluating fairness of LLM-generated" synthetic datasets empirical study results subgroup performance

---

# Iteration 8

## 1. Search

**Query**

> "Fair and square? Evaluating fairness of LLM-generated" synthetic datasets empirical study results subgroup performance

**Why this query**

The new sources add a useful calibration dimension and practical workflow context, but they do not close the central evidence gap: independent, LLM-specific comparisons of real, synthetic, and mixed fine-tuning on data quality, subgroup bias, calibration, privacy, and production-like outcomes. S28 appears potentially relevant to fairness but the retrieved content is incomplete.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S29 — Fair and Square? Evaluating Fairness of LLM-Generated ...**
  URL: https://papers.ssrn.com/sol3/Delivery.cfm/896be1ad-c96e-4eb7-b15d-e65aa71d30a0-MECA.pdf?abstractid=5246323&mirid=1
- **S30 — Fair and square? Evaluating fairness of LLM-generated ...**
  URL: https://dl.acm.org/doi/10.1016/j.infsof.2025.107980
- **S31 — Fair and Square? Evaluating Fairness of LLM-Generated ...**
  URL: https://figshare.com/s/fc0bdef65bef553d445a
- **S32 — Fair and square? Evaluating fairness of LLM-generated ...**
  URL: https://www.researchgate.net/publication/398255569_Fair_and_square_Evaluating_fairness_of_LLM-generated_synthetic_datasets

**Search Duration:** 5.13s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources indicate a trade-off between model performance and fairness when training on LLM-generated synthetic datasets.

**Confidence:** Medium

**Why this confidence level**

Both sources concern the target topic directly, but the supplied excerpts do not provide subgroup metrics, effect sizes, task details, or experimental comparisons sufficient to characterize the trade-off precisely.

**Evidence**

- The SSRN record explicitly identifies a trade-off between model performance and fairness when synthetic datasets are used. [S29]
- The ACM record reports that models trained with synthetic data—especially data generated with simpler prompts—can achieve competitive performance, implying that competitive aggregate performance does not by itself establish fairness. [S30]

#### Finding 2

**Claim**

Prompt complexity or generation strategy may affect the fairness and performance of synthetic-data-trained models.

**Confidence:** Low

**Why this confidence level**

The available content does not report the direction or magnitude of fairness changes by prompt type, and the repository contents were not supplied in detail.

**Evidence**

- The ACM abstract states that synthetic data generated using simpler prompts can produce competitive model performance, suggesting that prompt design is an experimental factor in downstream outcomes. [S30]
- The paper repository contains datasets, code, visualizations, and supplementary materials that may support examination of how generation conditions affect fairness and performance. [S31]

#### Finding 3

**Claim**

The new paper is directly relevant to the previously unresolved question of subgroup fairness in LLM fine-tuning, but the retrieved excerpts do not yet establish which groups, metrics, or real-world tests were used.

**Confidence:** Medium

**Why this confidence level**

The source relevance is direct, but the supplied material lacks the methodology and quantitative results needed to assess robustness or generalizability.

**Evidence**

- The title and descriptions identify an evaluation of fairness in LLM-generated synthetic datasets, and the abstract snippets discuss fairness and model performance after training on synthetic data. [S29] [S30] [S32]
- The repository advertises accompanying datasets, code, visualizations, and supplementary materials, indicating that detailed empirical results may be available beyond the snippets. [S31]

### Conflicts Found

- The new sources add a more specific qualification to the broader claim that synthetic data can improve fairness: synthetic training may achieve competitive performance while creating a performance–fairness trade-off. This does not directly contradict earlier evidence, which also described fairness gains as conditional on data quality, distributional alignment, and controls. [S29] [S30] [S15] [S20]
- The apparent benefit of competitive performance from simpler-prompt synthetic data cannot be compared directly with S8 or S18's quality and cost findings because the supplied excerpts do not state whether the same tasks, models, baselines, or evaluation settings were used. [S30] [S8] [S18]

### Important Gaps

- What fairness metrics and protected subgroups were evaluated in S29–S32?
- How large and statistically reliable was the performance–fairness trade-off?
- Were models trained on real, synthetic, and mixed data, and were they evaluated on independent real-world data?
- How did prompt complexity, generator identity, data volume, and filtering affect subgroup performance, calibration, factuality, and robustness?
- Does the reported fairness behavior transfer across languages, demographic groups, software-engineering tasks, and production-like distributions?

**Analysis Duration:** 9.49s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources are promising and directly address the main evidence gap on subgroup fairness, but the retrieved content consists only of title/abstract-level snippets and a repository pointer. A focused retrieval of the paper's full empirical results could materially improve the answer by supplying subgroup metrics, baselines, methodology, and independent evaluation details.

**Next Search**

> "Fair and Square" "Evaluating Fairness of LLM-Generated Synthetic Datasets" subgroup metrics real synthetic mixed data

---

# Iteration 9

## 1. Search

**Query**

> "Fair and Square" "Evaluating Fairness of LLM-Generated Synthetic Datasets" subgroup metrics real synthetic mixed data

**Why this query**

The new sources are promising and directly address the main evidence gap on subgroup fairness, but the retrieved content consists only of title/abstract-level snippets and a repository pointer. A focused retrieval of the paper's full empirical results could materially improve the answer by supplying subgroup metrics, baselines, methodology, and independent evaluation details.

**Results**

5 results retrieved.

2 new unique sources added.

### Sources

- **S33 — Fair and Square? Evaluating Fairness of Llm-Generated ...**
  URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5246323
- **S34 — Towards Causally Fair LLM-augmented Synthetic Data ...**
  URL: https://arxiv.org/html/2506.19082v1

**Search Duration:** 4.70s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources provide limited additional evidence that LLM-augmented synthetic data can satisfy fairness requirements, but they do not yet establish broad benefits for LLM training or fine-tuning.

**Confidence:** Medium

**Why this confidence level**

The sources are directly relevant to fairness-aware synthetic-data generation, but the supplied excerpts are too brief to assess experimental design, statistical reliability, generalization, or implications for LLM fine-tuning.

**Evidence**

- S33 states that synthetic-data generation may be a viable way to address fairness requirements in machine-learning systems, but the retrieved content provides no methods, subgroup metrics, effect sizes, or downstream model results. [S33]
- S34 reports that generated data deviated by less than 10% from real data on causal-fairness metrics and discusses training on causally fair predictors, indicating a fairness-oriented generation approach. [S34]

#### Finding 2

**Claim**

Causal-fairness evaluation is a potentially useful addition to subgroup accuracy and calibration tests because it examines whether generated data preserves fairness-relevant relationships rather than only matching surface distributions.

**Confidence:** Medium

**Why this confidence level**

S34 directly supports the relevance of causal-fairness metrics, while the claim that they complement—not replace—other evaluation layers follows from the broader accumulated evidence. The supplied material does not show whether causal metrics predict deployment harms.

**Evidence**

- S34 evaluates the distance between generated and real data using causal-fairness metrics and reports less than 10% deviation, suggesting an evaluation framework beyond aggregate task accuracy. [S34]
- Prior evidence recommends subgroup-specific error rates, confidence calibration, representation checks, and real-world outcome validation; causal metrics could complement these dimensions rather than replace them. [S11] [S12] [S26]

#### Finding 3

**Claim**

The new evidence does not resolve whether fairness improvements from synthetic data persist after LLM fine-tuning or under real-world distribution shift.

**Confidence:** High

**Why this confidence level**

The limitations are explicit in the retrieved excerpts and align with the previously documented evidence gap.

**Evidence**

- S33 does not report whether models trained on the synthetic data were compared with real-data or mixed-data baselines, nor whether subgroup performance was tested on independent real-world data. [S33]
- S34 reports causal-fairness similarity between generated and real data, but the excerpt does not provide downstream LLM fine-tuning results, subgroup outcomes, calibration, robustness, or production-like evaluation. [S34]
- The accumulated evidence continues to identify direct comparisons of real, synthetic, and mixed LLM fine-tuning on subgroup fairness and deployment performance as an unresolved gap. [S6] [S8] [S15] [S22] [S29] [S30]

### Conflicts Found

- S33 presents synthetic-data generation as potentially viable for meeting fairness requirements, while prior evidence warns that synthetic data can reproduce or amplify source and generator bias and can trade fairness gains against utility. This is conditional rather than a direct contradiction: fairness depends on causal controls, generation quality, distributional alignment, and independent subgroup validation. [S33] [S34] [S1] [S2] [S15] [S20]
- S34 reports less than 10% deviation from real data on causal-fairness metrics, but prior evidence shows that similarity or balanced representation does not guarantee good downstream utility, calibration, robustness, privacy, or subgroup outcomes after fine-tuning. Causal-metric agreement should therefore not be treated as sufficient evidence of overall fairness or safety. [S34] [S8] [S12] [S15] [S22] [S26]

### Important Gaps

- What causal-fairness metrics, protected attributes, data-generating processes, and statistical tests were used in S34?
- Does the less-than-10% causal-fairness deviation in S34 translate into improved subgroup performance after LLM fine-tuning?
- Were S33–S34 models evaluated on independent real-world data and compared against real-data and mixed-data fine-tuning baselines?
- Do causal-fairness gains persist under distribution shift, across languages and dialects, and for minority or safety-critical groups?
- How do causal-fairness constraints affect factuality, calibration, robustness, privacy leakage, tail coverage, and overall utility?

**Analysis Duration:** 10.64s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources strengthen the conceptual and methodological case for fairness-aware, including causal, evaluation, but the central question still lacks direct quantitative evidence comparing real, synthetic, and mixed data for LLM fine-tuning on independent subgroup, calibration, factuality, privacy, and production-like tests.

**Next Search**

> "Towards Causally Fair LLM-augmented Synthetic Data" experiments causal fairness downstream model performance real synthetic data

---

# Iteration 10

## 1. Search

**Query**

> "Towards Causally Fair LLM-augmented Synthetic Data" experiments causal fairness downstream model performance real synthetic data

**Why this query**

The new sources strengthen the conceptual and methodological case for fairness-aware, including causal, evaluation, but the central question still lacks direct quantitative evidence comparing real, synthetic, and mixed data for LLM fine-tuning on independent subgroup, calibration, factuality, privacy, and production-like tests.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S35 — Towards Causally Fair LLM-augmented Synthetic Data ...**
  URL: https://www.semanticscholar.org/paper/420adce71f6bc1496e559b8192685389078c6371
- **S36 — Towards Causally Fair LLM-augmented Synthetic Data ...**
  URL: https://www.researchgate.net/publication/398311961_FairCauseSyn_Towards_Causally_Fair_LLM-augmented_Synthetic_Data_Generation
- **S37 — Towards Causally Fair LLM-Augmented Synthetic Data ...**
  URL: https://futurehealth.uci.edu/projects/faircausesyn-towards-causally-fair-llm-augmented-synthetic-data-generation
- **S38 — Towards Causally Fair LLM-Augmented Synthetic Data ...**
  URL: https://www.themoonlight.io/en/review/faircausesyn-towards-causally-fair-llm-augmented-synthetic-data-generation

**Search Duration:** 4.46s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources describe FairCauseSyn as an LLM-augmented method intended to improve causal fairness in synthetic health data.

**Confidence:** Medium

**Why this confidence level**

All four sources consistently describe the method and its purpose, but the supplied excerpts do not provide implementation details, quantitative results, or independent comparisons.

**Evidence**

- The sources characterize FairCauseSyn as a framework for generating synthetic tabular health data with explicit causal-fairness objectives, using real-world health data. [S35] [S36] [S37] [S38]

#### Finding 2

**Claim**

The new sources reinforce causal fairness as a potentially useful evaluation and generation objective, but add no direct evidence about synthetic data used to fine-tune LLMs.

**Confidence:** High

**Why this confidence level**

The source descriptions clearly concern data generation rather than LLM training or fine-tuning, and they provide no downstream language-model evaluation.

**Evidence**

- FairCauseSyn concerns synthetic tabular health-data generation augmented by an LLM; the excerpts do not report fine-tuning an LLM on the generated data or measuring downstream language-model performance. [S35] [S36] [S37] [S38]
- Earlier evidence already identified causal-fairness similarity as a complementary metric, while noting that it does not establish downstream utility, calibration, robustness, privacy, or subgroup outcomes after fine-tuning. [S34] [S8] [S12] [S15] [S22] [S26]

#### Finding 3

**Claim**

Causal-fairness alignment in generated health data should not be interpreted as proof that the resulting data is suitable for LLM training or safe deployment.

**Confidence:** High

**Why this confidence level**

The limitation follows directly from the narrow scope of the new excerpts and is consistent with multiple prior findings.

**Evidence**

- The excerpts identify causal fairness as the main contribution but do not report factuality, data quality, privacy leakage, calibration, robustness, or production-like model evaluations. [S35] [S36] [S37] [S38]
- Accumulated evidence shows that fairness-oriented synthetic data can still involve real–synthetic distribution gaps, utility tradeoffs, privacy leakage, and subgroup harms after model training. [S15] [S20] [S22] [S26] [S29] [S30] [S34]

### Conflicts Found

- The new sources present causal-fairness generation as a promising fairness intervention, while accumulated evidence warns that fairness similarity or constraints do not guarantee downstream subgroup performance, utility, calibration, privacy, or robustness. This is a conditional qualification, not a direct contradiction. [S35] [S36] [S37] [S38] [S15] [S20] [S22] [S26] [S34]

### Important Gaps

- What causal-fairness metrics, protected attributes, causal graphs, and statistical tests does FairCauseSyn use?
- What quantitative improvements does FairCauseSyn achieve versus real-data, conventional synthetic-data, and other fairness-aware baselines?
- Does FairCauseSyn-generated data improve subgroup performance after LLM fine-tuning, and does any improvement persist under independent real-world distribution shift?
- How does the method affect factuality, calibration, privacy leakage, tail coverage, and overall utility?
- Does the approach generalize beyond tabular health data to language instruction, preference, tool-use, or multilingual fine-tuning data?

**Analysis Duration:** 7.59s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The runner reached the maximum research iteration budget. Analyzer assessment: The new sources are relevant but only provide high-level descriptions of a fairness-aware synthetic-data generator. They do not close the central evidence gap: direct, independent comparisons of real, synthetic, and mixed data for LLM fine-tuning on data quality, subgroup bias, calibration, privacy, and production-like outcomes.

**Stop Reason:** max_iterations

---

# Final Research Decision

**Research Stopped Because**

The runner reached the maximum research iteration budget.

**Stop Reason:** max_iterations

**Searches Performed:** 10

**Unique Sources:** 38

**Remaining Uncertainty**

- Direct, independent comparisons of real-data, synthetic-data, and mixed-data fine-tuning for LLMs on factuality, calibration, subgroup fairness, robustness, privacy, and production-like performance.
- Subgroup-specific effects across demographic groups, languages, dialects, cultural contexts, and safety-critical populations.
- The amount and mixture of synthetic data that preserve tail coverage and real-world performance under distribution shift.
- How privacy findings vary with generator model, prompt design, source-data overlap, deduplication, synthetic-data proportion, and API-only versus logit-access threat models.
- The reliability of automated filters and LLM-as-a-judge systems for factual, cultural, minority-language, privacy, and safety-critical errors.
- Whether fairness-oriented or causal-fairness synthetic data produces downstream benefits after LLM fine-tuning, rather than only matching fairness metrics at the dataset level.
- Replication of reported cost-effectiveness, robustness, distribution-collapse, and privacy results across models, generators, tasks, and deployment conditions.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 10 | 41.96s |
| OpenAI Analysis | 10 | 129.51s |
| Report Generation | 1 | 27.59s |
| Total Run | — | 199.07s |
