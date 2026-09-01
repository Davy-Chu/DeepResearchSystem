# Research Run Log

## Run Summary

**System Version:** prior-guided-baseline-v0

**Research Question**

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 10 / 10

**Unique Sources:** 35

**OpenAI Calls:** 12

**Tavily Calls:** 10

**Started:** 2026-09-01T06:06:44-04:00

**Ended:** 2026-09-01T06:11:29-04:00

**Total Runtime:** 285.25s

---

## Prior-Knowledge Coverage Plan

### D1 — Synthetic data’s effects on model data quality and learning

**Importance:** CORE

**Research question**

How does using synthetic data for pretraining, continued pretraining, supervised fine-tuning, or preference optimization affect data quality, diversity, factuality, linguistic coverage, contamination, redundancy, and model performance compared with relevant human-generated or naturally occurring data?

**Why it matters**

Data quality is central to whether synthetic data provides useful training signal or introduces degradation, including loss of diversity, propagation of errors, and reduced capability on underrepresented inputs. The effects may differ substantially by training stage, generation method, filtering process, and the proportion of synthetic data used.

**Evidence needed**

Controlled comparisons between synthetic, human-generated, natural, and mixed-data training; measurements of factual accuracy, diversity, novelty, duplication, coverage, toxicity, instruction quality, and downstream task performance; analyses across generation models, domains, languages, data mixtures, and synthetic-data proportions; documentation of filtering, deduplication, and provenance procedures.

**Initial status:** UNRESEARCHED

### D2 — Bias, fairness, and representation risks and benefits

**Importance:** CORE

**Research question**

How does synthetic data change demographic, cultural, linguistic, ideological, and domain representation, and what are the resulting effects on bias, stereotyping, fairness, and performance across groups?

**Why it matters**

Synthetic generation can potentially fill gaps in scarce or sensitive datasets, but it can also amplify biases embedded in the generating model or prompt design and make those biases less visible. A high-quality answer must distinguish changes in representation from changes in measured fairness and account for intersectional and multilingual effects.

**Evidence needed**

Disaggregated evaluations across relevant demographic, cultural, linguistic, and socioeconomic groups; tests for stereotyping, disparate performance, toxicity, refusals, and allocation or recommendation harms; comparisons of synthetic-data generation and filtering strategies; documentation of prompting, annotator or curator choices, model provenance, and representational coverage; assessment of whether synthetic data improves or worsens performance for historically underrepresented groups.

**Initial status:** UNRESEARCHED

### D3 — Evaluation validity and methods for detecting synthetic-data effects

**Importance:** CORE

**Research question**

What evaluation designs can reliably determine whether synthetic data improves model quality, and how can they detect hidden degradation, distribution shift, bias amplification, or synthetic-data artifacts?

**Why it matters**

Standard benchmark gains may not capture real-world reliability, fairness, or robustness, and evaluations can be distorted by benchmark contamination or overlap with generated training data. The answer needs to assess not only what to measure but also whether the evaluation setup supports credible causal comparisons.

**Evidence needed**

Pre-registered or otherwise controlled ablation studies; held-out and temporally separated test sets; contamination and near-duplicate checks; evaluations of factuality, calibration, robustness, adversarial behavior, generalization, human preference, and group-wise outcomes; confidence intervals and statistical significance; independent replication and human review; evidence comparing automated metrics with expert and end-user judgments.

**Initial status:** UNRESEARCHED

### D4 — Failure modes, feedback loops, and model-collapse dynamics

**Importance:** CORE

**Research question**

Under what conditions does repeatedly generating training data from models, or mixing synthetic data recursively, cause error amplification, loss of diversity, memorization, reduced capability, or distributional drift?

**Why it matters**

Synthetic data pipelines may create feedback loops in which model assumptions and mistakes become increasingly dominant. These risks are distinct from ordinary data-quality problems and may emerge only over multiple generations, model updates, or changes in the synthetic-to-natural data ratio.

**Evidence needed**

Multi-generation and longitudinal experiments; comparisons of recursive and non-recursive pipelines; measurements of diversity, rare-event coverage, entropy, factuality, memorization, calibration, and capability retention; analyses of mixture ratios, model quality, sampling methods, filtering, and fresh human or natural data; tests across domains and languages.

**Initial status:** UNRESEARCHED

### D5 — Real-world utility, safety, and deployment externalities

**Importance:** CORE

**Research question**

Do models trained or fine-tuned with synthetic data behave more reliably, safely, and usefully in realistic deployment settings, and what harms or benefits may arise from errors that are difficult to observe in offline tests?

**Why it matters**

The practical value of synthetic data depends on downstream behavior, not just benchmark scores. Deployment can expose privacy, security, misinformation, overreliance, accessibility, and domain-specific safety issues that are not apparent from training metrics or static evaluations.

**Evidence needed**

Task- and domain-specific field studies, red-team assessments, user studies, incident and error analyses, monitoring data, robustness tests under distribution shift, privacy and memorization assessments, and comparisons of human workload, decision quality, and harm rates with appropriately matched baseline models.

**Initial status:** UNRESEARCHED

### D6 — Data provenance, privacy, and governance implications

**Importance:** SECONDARY

**Research question**

How do provenance, consent, licensing, privacy, auditability, and accountability differ between synthetic and source data, and how do those differences affect the legitimacy and risk profile of training or fine-tuning?

**Why it matters**

Synthetic data may reduce direct exposure of sensitive records or make data creation more scalable, but it may still encode or reproduce protected information and can obscure the origins of learned content. Governance conditions also affect whether quality and bias claims can be independently verified.

**Evidence needed**

Documentation and audits of source-data provenance, generation-model training history, privacy leakage and memorization tests, re-identification and membership-inference assessments, licensing and consent analysis, dataset and model cards, traceability mechanisms, and evidence on audit access and accountability practices.

**Initial status:** UNRESEARCHED

### D7 — Operational trade-offs and conditions for responsible use

**Importance:** SECONDARY

**Research question**

When do the costs and benefits of synthetic data—including scalability, controllability, domain customization, privacy protection, compute, human review, and pipeline complexity—justify its use relative to collecting or curating natural data?

**Why it matters**

A balanced assessment requires identifying the conditions under which synthetic data is beneficial rather than treating it as uniformly good or bad. The relevant trade-offs may vary by data scarcity, domain risk, language, task, model size, and required quality threshold.

**Evidence needed**

Total-cost and resource analyses covering generation, filtering, validation, and human oversight; matched comparisons with alternative data-collection strategies; sensitivity analyses by task and domain; evidence on scalability, reproducibility, latency, and maintenance; explicit risk-benefit frameworks that connect operational choices to measured quality, bias, and evaluation outcomes.

**Initial status:** UNRESEARCHED

### Synthesis requirements

- Separate evidence for pretraining, continued pretraining, supervised fine-tuning, preference optimization, and other training uses where relevant.
- Preserve the distinction between synthetic-only, mixed synthetic-and-natural, and recursively generated data, including the proportion and provenance of synthetic content.
- Evaluate benefits and risks separately for data quality, bias, and evaluation rather than relying only on aggregate benchmark performance.
- Prioritize causal or controlled comparisons and identify where evidence is uncertain, contradictory, difficult to generalize, or dependent on generation and filtering choices.
- Connect offline findings to real-world deployment outcomes and clearly distinguish measured effects from hypothesized risks.

Planner output is planning metadata, not evidence.

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

**Search Duration:** 2.42s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data can provide practical benefits when real or labeled data are scarce, costly, privacy-sensitive, or insufficiently representative; proposed uses include augmentation, minority-class coverage, domain adaptation, and generation of edge cases or evaluation scenarios.

**Confidence:** Medium

**Why this confidence level**

The benefits are consistently described, but the retrieved support is primarily practitioner and vendor-oriented material rather than controlled LLM studies with independently measured real-world outcomes.

**Evidence**

- Sources describe synthetic data as a scalable supplement for scarce labels, rare cases, privacy-constrained domains, class imbalance, and evaluation coverage. [S3] [S4]

#### Finding 2

**Claim**

Synthetic data quality depends strongly on generation and curation: filtering, deduplication, prompt or format diversity, validation, and retention of natural data matter more than volume alone.

**Confidence:** Medium

**Why this confidence level**

The sources offer a coherent operational principle, but provide limited methodological detail and mostly cite or summarize other work.

**Evidence**

- The decision guide contrasts curated synthetic training with indiscriminate generation, reports low duplication for Cosmopedia, and characterizes curation discipline as central to utility. [S2]
- The practitioner sources recommend measuring accuracy, diversity, realism, and anomalies with statistical and human review against trusted real-world data. [S4]

#### Finding 3

**Claim**

Replacing natural data with recursively generated synthetic data can cause model-collapse dynamics, including loss of low-probability or tail examples and degradation of model quality; additive mixtures that retain fresh real data are presented as safer than replacement regimes.

**Confidence:** Medium

**Why this confidence level**

Multiple retrieved sources agree, and S2 identifies peer-reviewed work, but the detailed experimental and analytical papers themselves were not retrieved, so regime assumptions and generalizability remain uncertain.

**Evidence**

- The sources describe recursive training as narrowing the learned distribution and report that purely synthetic self-training degraded OPT-125m perplexity, while an additive regime retaining real data has bounded-error results according to the cited analysis. [S1] [S2]
- A review warns that repeated training on model-generated content without new information or external verification can cause stagnation or degradation. [S5]

#### Finding 4

**Claim**

Synthetic data can amplify or reproduce biases from the generating model, prompts, source data, or filtering choices; it can also fail to represent some demographics and therefore worsen group-wise generalization despite increasing nominal dataset size.

**Confidence:** Medium

**Why this confidence level**

The risk is directly stated by two sources, but no retrieved source provides disaggregated demographic, linguistic, intersectional, or fairness measurements demonstrating the magnitude or direction of effects.

**Evidence**

- Sources explicitly identify bias amplification and demographic underrepresentation as risks, while presenting targeted generation as a possible response to class imbalance and representation gaps. [S3] [S4]

#### Finding 5

**Claim**

Synthetic data may improve task-specific performance, but aggregate benchmark gains do not establish broad quality, factuality, fairness, or deployment reliability.

**Confidence:** Medium

**Why this confidence level**

The distinction between narrow gains and broader reliability is supported, but the retrieved material does not supply controlled ablations, confidence intervals, independent replications, or direct deployment comparisons.

**Evidence**

- The sources report strong task-specific coding results for a curated synthetic-data regime and describe synthetic data as useful for particular tasks, while also warning that realistic performance requires validation on trusted real-world data. [S2] [S4]
- The review notes benchmark saturation, contamination or leakage, and the possibility that models perform well on standard tests while behaving unreliably in complex real-world settings. [S5]

#### Finding 6

**Claim**

Evaluation of synthetic-data effects should combine held-out trusted natural test data with checks of accuracy, diversity, realism, factuality, robustness, contamination, and group-wise outcomes, plus human or expert review where automated metrics are insufficient.

**Confidence:** Medium

**Why this confidence level**

These are well-supported evaluation principles in the retrieved content, but no source demonstrates that a specific evaluation protocol reliably identifies causal synthetic-data effects.

**Evidence**

- Sources recommend automated statistical analysis, visualization, and human evaluation of synthetic datasets, and emphasize benchmarking against trusted real-world data. [S4]
- The review highlights contamination, fairness, reproducibility, safety, robustness, and realistic task evaluation as limitations of relying on static benchmarks alone. [S5]

### Conflicts Found

- The retrieved sources present both substantial capability benefits and serious degradation risks. Curated, additive, quality-filtered synthetic data is portrayed as potentially highly effective, whereas recursive or replacement training is portrayed as causing collapse. This is a conditional difference by data mixture, provenance, and curation regime rather than a direct contradiction. [S2] [S4]
- S3 and S4 broadly describe synthetic data as capable of preserving statistical properties or privacy while noting risks, but the retrieved evidence does not establish that LLM-generated synthetic text reliably removes links to individuals or satisfies privacy requirements. The stronger privacy-preservation framing is therefore unsupported by the accompanying validation evidence. [S3] [S4]

### Important Gaps

- How do synthetic-only, mixed, and recursive mixtures compare under controlled, matched LLM pretraining and fine-tuning experiments?
- What are the measured effects on factuality, novelty, linguistic and demographic coverage, hallucination, and rare or underrepresented cases?
- Which generation models, prompting strategies, filters, deduplication methods, and synthetic-to-natural ratios produce reliable gains?
- Do synthetic data pipelines improve or worsen disaggregated fairness and bias outcomes across demographic, cultural, ideological, and multilingual groups?
- How frequently do synthetic examples overlap with benchmarks or source data, and how much do contamination and near-duplicate leakage inflate reported gains?
- Do offline improvements persist under temporally separated, adversarial, expert-reviewed, and real-world deployment evaluations?
- What evidence supports the privacy claims, including memorization, membership inference, re-identification, provenance, and consent assessments?

**Analysis Duration:** 21.25s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The retrieved material supports a cautious high-level account of benefits and failure modes, but all three core dimensions remain only partial. In particular, there are no directly retrieved controlled studies adequate to quantify data-quality effects, bias effects, or evaluation validity across training stages. Another focused search would materially improve the answer.

**Next Search**

> controlled study synthetic data LLM training fine-tuning data quality bias evaluation model collapse ablation human data mixture

---

## Coverage Map After Iteration 1

| Dimension | Importance | Status | Searches |
|---|---|---|---:|
| D1 — Synthetic data’s effects on model data quality and learning | CORE | PARTIAL | 1 |
| D2 — Bias, fairness, and representation risks and benefits | CORE | PARTIAL | 0 |
| D3 — Evaluation validity and methods for detecting synthetic-data effects | CORE | PARTIAL | 0 |
| D4 — Failure modes, feedback loops, and model-collapse dynamics | CORE | PARTIAL | 0 |
| D5 — Real-world utility, safety, and deployment externalities | CORE | PARTIAL | 0 |
| D6 — Data provenance, privacy, and governance implications | SECONDARY | PARTIAL | 0 |
| D7 — Operational trade-offs and conditions for responsible use | SECONDARY | PARTIAL | 0 |

**Next search target:** D1

**Reason:**

The retrieved material supports a cautious high-level account of benefits and failure modes, but all three core dimensions remain only partial. In particular, there are no directly retrieved controlled studies adequate to quantify data-quality effects, bias effects, or evaluation validity across training stages. Another focused search would materially improve the answer.

---

# Iteration 2

## 1. Search

**Query**

> controlled study synthetic data LLM training fine-tuning data quality bias evaluation model collapse ablation human data mixture

**Why this query**

The retrieved material supports a cautious high-level account of benefits and failure modes, but all three core dimensions remain only partial. In particular, there are no directly retrieved controlled studies adequate to quantify data-quality effects, bias effects, or evaluation validity across training stages. Another focused search would materially improve the answer.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S6 — The Impact of Synthetic Data Diversity on LLM Fine-Tuning - arXiv**
  URL: https://arxiv.org/html/2511.01490v1
- **S7 — Synthetic Data for LLM Fine-Tuning 2026**
  URL: https://futureagi.com/blog/synthetic-data-fine-tuning-llms
- **S8 — Synthetic Training Data Quality Collapse: How Feedback Loops Destroy Your Fine-Tuned Models**
  URL: https://tianpan.co/blog/2026-04-09-synthetic-training-data-quality-collapse

**Search Duration:** 1.95s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

In supervised fine-tuning, diversity among synthetic-data sources may reduce distribution collapse relative to single-source synthetic data.

**Confidence:** Medium

**Why this confidence level**

This is direct experimental evidence from a research paper, but only the retrieved paper excerpt is available and it does not provide full methodological details, effect sizes, or independent replication.

**Evidence**

- An arXiv study reports that synthetic data from diverse sources mitigated distribution collapse and preserved broader output and linguistic diversity, including experiments involving larger models such as Llama-3.1-70B. [S6]

#### Finding 2

**Claim**

Synthetic fine-tuning data can create a safety trade-off: it may preserve output quality while reducing adversarial robustness and weakening safeguards.

**Confidence:** Medium

**Why this confidence level**

The finding is presented as an empirical result for supervised fine-tuning, but the excerpt does not establish how broadly it generalizes across models, safety tasks, or deployment settings.

**Evidence**

- The arXiv study reports that both human and synthetic fine-tuning data can remove safeguards; synthetic data preserved higher output quality while decreasing adversarial robustness. [S6]
- The study further reports that source diversity and the size of the data-generating model jointly affect adversarial robustness. [S6]

#### Finding 3

**Claim**

Fine-tuning can alter evaluator-related bias, and single-source synthetic data may be less effective than human or multi-source data at reducing self-preference bias.

**Confidence:** Medium

**Why this confidence level**

This directly addresses an evaluation bias relevant to LLM-as-judge systems, but it is one study and does not show whether the result persists across judge models, tasks, or evaluation designs.

**Evidence**

- The arXiv study reports that fine-tuning reduced self-preference bias, with the strongest reduction from human data and the weakest from single-source synthetic data; multi-source synthetic data was intermediate. [S6]

#### Finding 4

**Claim**

The practical benefits of synthetic fine-tuning depend on task-shaped generation, quality filtering, and anchoring with real seed data rather than indiscriminate synthetic-data replacement.

**Confidence:** Medium

**Why this confidence level**

The operational recommendations are coherent with prior evidence, but the source is vendor-oriented and its numerical cost and scale claims are illustrative rather than controlled evidence.

**Evidence**

- A practitioner guide describes synthetic rows tailored to SFT, preference optimization, tool use, and retrieval tasks, with a pipeline involving human seeds, teacher generation, and judge-based filtering. It also identifies teacher-bias inheritance and recommends mixing teachers and retaining real data. [S7]
- The guide presents synthetic data as useful when large quantities of labeled examples are unaffordable or privacy-constrained, but acknowledges mode collapse and inherited teacher style as trade-offs. [S7]

#### Finding 5

**Claim**

Recursive or replacement-based synthetic-data pipelines risk progressively narrowing coverage, including rare cases, minority perspectives, vocabulary, and edge-case reasoning.

**Confidence:** Medium

**Why this confidence level**

The mechanism is consistent with multiple sources, including the research paper in S6 and prior evidence, but S8's stronger quantitative and universal claims are not independently substantiated in the retrieved material.

**Evidence**

- A practitioner account describes early collapse as loss of tail information and late collapse as repetitive, stylistically homogeneous, and brittle behavior. [S8]
- This extends prior findings that recursive self-training can reduce diversity and degrade modeling of human text. [S6] [S1] [S2]

#### Finding 6

**Claim**

Aggregate benchmark performance can hide distribution narrowing and evaluator or safety failures caused by synthetic-data fine-tuning.

**Confidence:** Medium

**Why this confidence level**

The need to evaluate beyond aggregate benchmarks is supported by the research study and prior sources; the broader claims about hidden degradation remain incompletely quantified.

**Evidence**

- S6 explicitly distinguishes benchmark performance from lower-level output-distribution changes and evaluates distribution collapse, adversarial robustness, and self-preference bias as separate outcomes. [S6]
- S8 similarly claims that common-case benchmark scores may improve while tail coverage silently narrows, although this account is not independently verified here. [S8]

### Conflicts Found

- S6 reports that multi-source synthetic data can mitigate distribution collapse, while S8 presents recursive synthetic feedback as broadly and progressively destructive. These are conditional rather than necessarily direct contradictions: source diversity, retention of natural data, replacement versus accumulation, and number of generations may determine the outcome. [S6] [S8] [S1] [S2]
- S6 reports synthetic fine-tuning preserving higher output quality while reducing adversarial robustness, whereas prior evidence emphasizes potential task-performance gains and S7 emphasizes quality-filtered utility. These findings concern different outcome dimensions; improved task or output quality does not imply improved safety or robustness. [S6] [S7] [S2] [S4]
- S8 makes strong quantitative claims about collapse occurring with very small synthetic contamination and about accumulation preventing collapse, but those claims are not supported by the detailed underlying studies in the retrieved content. They should not be treated as established to the same degree as the qualitative replacement-versus-mixture distinction. [S8] [S1] [S2]

### Important Gaps

- How large are the reported diversity and robustness effects, and do they replicate across fine-tuning objectives, model families, languages, and domains?
- Which demographic, cultural, linguistic, and intersectional groups benefit or suffer when synthetic data is used for augmentation or fine-tuning?
- Does multi-source synthetic data improve fairness, or merely reduce stylistic and distributional collapse while preserving substantive bias?
- How should evaluators be independently validated when an LLM judge is also used to filter or generate the synthetic training data?
- What controlled synthetic-only, mixed, and recursive experiments establish causal effects on factuality, hallucination, rare-case coverage, and deployment reliability?
- What are the actual privacy, provenance, consent, and contamination outcomes of the described pipelines?

**Analysis Duration:** 23.77s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new research source strengthens evidence about diversity, adversarial robustness, and self-preference in supervised fine-tuning, but the most important remaining gap is still disaggregated bias and fairness evidence. No retrieved source measures demographic, cultural, multilingual, or intersectional outcomes. Evaluation validity and deployment effects also remain only partially supported.

**Next Search**

> synthetic data LLM fine-tuning demographic fairness disaggregated evaluation bias amplification multilingual groups controlled study

---

## Coverage Map After Iteration 2

| Dimension | Importance | Status | Searches |
|---|---|---|---:|
| D1 — Synthetic data’s effects on model data quality and learning | CORE | PARTIAL | 1 |
| D2 — Bias, fairness, and representation risks and benefits | CORE | PARTIAL | 1 |
| D3 — Evaluation validity and methods for detecting synthetic-data effects | CORE | PARTIAL | 0 |
| D4 — Failure modes, feedback loops, and model-collapse dynamics | CORE | PARTIAL | 0 |
| D5 — Real-world utility, safety, and deployment externalities | CORE | PARTIAL | 0 |
| D6 — Data provenance, privacy, and governance implications | SECONDARY | PARTIAL | 0 |
| D7 — Operational trade-offs and conditions for responsible use | SECONDARY | PARTIAL | 0 |

**Next search target:** D2

**Reason:**

The new research source strengthens evidence about diversity, adversarial robustness, and self-preference in supervised fine-tuning, but the most important remaining gap is still disaggregated bias and fairness evidence. No retrieved source measures demographic, cultural, multilingual, or intersectional outcomes. Evaluation validity and deployment effects also remain only partially supported.

---

# Iteration 3

## 1. Search

**Query**

> synthetic data LLM fine-tuning demographic fairness disaggregated evaluation bias amplification multilingual groups controlled study

**Why this query**

The new research source strengthens evidence about diversity, adversarial robustness, and self-preference in supervised fine-tuning, but the most important remaining gap is still disaggregated bias and fairness evidence. No retrieved source measures demographic, cultural, multilingual, or intersectional outcomes. Evaluation validity and deployment effects also remain only partially supported.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S9 — Synthetic Data for Bias Mitigation 2026: 5 Methods + FAGI**
  URL: https://futureagi.com/blog/synthetic-data-generation-bias-2025
- **S10 — Fairness in AI Decisions About People: Evidence from LLM Experiments**
  URL: https://manhattan.institute/article/fairness-in-ai-decisions-about-people-evidence-from-llm-experiments
- **S11 — GitHub - junxu-ai/LLM_fairness: Collection of papers, tools ...**
  URL: https://github.com/junxu-ai/LLM_fairness
- **S12 — Bias Mitigation via Synthetic Data Generation: A Review**
  URL: https://www.mdpi.com/2079-9292/13/19/3909

**Search Duration:** 2.96s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Targeted synthetic examples may help address representation gaps and rare cases, but the retrieved new evidence presents this primarily as a proposed workflow rather than a demonstrated LLM outcome.

**Confidence:** Medium

**Why this confidence level**

The operational rationale is consistent across sources, but S9 is vendor-oriented and does not establish that targeted synthesis improves fairness or real-world performance.

**Evidence**

- S9 recommends auditing subgroup errors and coverage gaps, generating targeted examples for underrepresented slices, mixing them with real data, and re-auditing on held-out data. It asserts potential benefits for rare events and underrepresented languages, but does not report controlled effect sizes or independent validation. [S9]
- Prior evidence similarly identified augmentation, minority-class coverage, domain adaptation, and rare-case generation as plausible benefits, while noting limited controlled LLM evidence. [S3] [S4]

#### Finding 2

**Claim**

Synthetic-data bias mitigation requires measuring group-wise outcomes rather than assuming that rebalancing the training distribution produces fairness.

**Confidence:** Medium

**Why this confidence level**

The need for disaggregated evaluation is supported, but S10 and S11 do not test synthetic training data, and S9 does not provide causal evidence that its workflow works.

**Evidence**

- S9 proposes subgroup fairness metrics, coverage maps, held-out evaluation, and re-auditing after retraining, explicitly linking synthetic generation to an evaluation loop rather than treating generation alone as mitigation. [S9]
- S10 reports that LLM decisions can vary with demographic cues and prompt structure, and concludes that group-level monitoring remains necessary even when demographic information is masked. [S10]
- S11 catalogs counterfactual, group, embedding-, probability-, and generation-based fairness metrics, while emphasizing that LLM fairness depends on use case and evaluation framework. [S11]

#### Finding 3

**Claim**

Prompt and evaluator design can confound conclusions about fairness and quality, so synthetic-data pipelines should test structural effects and independently validate automated evaluators.

**Confidence:** Medium

**Why this confidence level**

The confounding risks are directly reported or logically operationalized in the sources, but no retrieved study validates a complete independent-evaluator protocol.

**Evidence**

- S10 finds that candidate ordering systematically influenced many LLM decisions and that demographic cues affected outcomes, showing that measured disparities can depend on prompt structure as well as model or data properties. [S10]
- Prior evidence found that synthetic fine-tuning affected self-preference bias and that LLM judges used for filtering or evaluation may themselves be biased. [S6]
- S9 recommends using fairness and quality evaluators before and after retraining, but does not establish their independence or validity when the same model family generates, filters, and evaluates data. [S9]

#### Finding 4

**Claim**

The new sources do not materially resolve the central causal questions about synthetic-only versus mixed training, demographic fairness effects, factuality, contamination, or deployment reliability.

**Confidence:** High

**Why this confidence level**

The retrieved content clearly lacks the experiments needed to answer these causal and deployment questions.

**Evidence**

- S9 provides recommendations and unverified claims about targeted generation, while S10 measures LLM decision disparities without manipulating synthetic training data. S11 is a collection of fairness resources, and the retrieved portion of S12 is bibliographic and does not provide substantive results. [S9] [S10] [S11] [S12]
- Prior findings already identified the absence of controlled matched comparisons, disaggregated fairness measurements, contamination checks, and field or deployment studies. [S1] [S2] [S4] [S5] [S6] [S7]

### Conflicts Found

- S9 presents targeted synthetic generation as a direct and potentially rapid way to reduce bias and close coverage gaps, whereas the accumulated evidence supports only conditional or proposed benefits and emphasizes that synthetic data can inherit or amplify generator, prompt, and filtering bias. This is an evidentiary-strength conflict rather than a direct empirical contradiction. [S9] [S3] [S4] [S6]
- S9 suggests that fairness gaps can be closed when subgroup metrics fall below a threshold and overall accuracy is maintained, but S10 shows that prompt structure and demographic cues can produce disparities even in otherwise controlled decisions. Passing aggregate accuracy and selected fairness metrics therefore may not establish robust fairness across contexts. [S9] [S10]

### Important Gaps

- What controlled LLM experiments compare synthetic-only, mixed, and natural-data fine-tuning while reporting disaggregated demographic, linguistic, and intersectional outcomes?
- Does targeted synthetic augmentation improve minority-group performance without increasing stereotyping, hallucination, or distributional artifacts?
- How should fairness evaluators be independently validated when an LLM is involved in generation, filtering, judging, and final evaluation?
- What are the effects of synthetic data on factuality, contamination, rare-case coverage, and deployment reliability across languages and domains?
- Do the proposed benefits in S9 persist under temporally separated, adversarial, expert-reviewed, and real-world tests?

**Analysis Duration:** 19.91s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new material strengthens the recommendation to use subgroup audits and independent evaluation, but it does not answer the most important remaining CORE gap: controlled, disaggregated evidence on whether synthetic data improves or worsens fairness and representation in LLM training or fine-tuning.

**Next Search**

> controlled study LLM synthetic data fine-tuning demographic fairness subgroup performance natural mixed synthetic data

---

## Coverage Map After Iteration 3

| Dimension | Importance | Status | Searches |
|---|---|---|---:|
| D1 — Synthetic data’s effects on model data quality and learning | CORE | PARTIAL | 1 |
| D2 — Bias, fairness, and representation risks and benefits | CORE | PARTIAL | 2 |
| D3 — Evaluation validity and methods for detecting synthetic-data effects | CORE | PARTIAL | 0 |
| D4 — Failure modes, feedback loops, and model-collapse dynamics | CORE | PARTIAL | 0 |
| D5 — Real-world utility, safety, and deployment externalities | CORE | PARTIAL | 0 |
| D6 — Data provenance, privacy, and governance implications | SECONDARY | PARTIAL | 0 |
| D7 — Operational trade-offs and conditions for responsible use | SECONDARY | PARTIAL | 0 |

**Next search target:** D2

**Reason:**

The new material strengthens the recommendation to use subgroup audits and independent evaluation, but it does not answer the most important remaining CORE gap: controlled, disaggregated evidence on whether synthetic data improves or worsens fairness and representation in LLM training or fine-tuning.

---

# Iteration 4

## 1. Search

**Query**

> controlled study LLM synthetic data fine-tuning demographic fairness subgroup performance natural mixed synthetic data

**Why this query**

The new material strengthens the recommendation to use subgroup audits and independent evaluation, but it does not answer the most important remaining CORE gap: controlled, disaggregated evidence on whether synthetic data improves or worsens fairness and representation in LLM training or fine-tuning.

**Results**

5 results retrieved.

2 new unique sources added.

### Sources

- **S13 — Auditing socio-demographic and cross-societal fairness in LLM-simulated public opinion | EPJ Data Science | Springer Nature Link**
  URL: https://link.springer.com/article/10.1140/epjds/s13688-026-00673-y
- **S14 — The Impact of Synthetic Data Diversity on LLM Fine-Tuning**
  URL: https://aclanthology.org/2026.findings-acl.360.pdf

**Search Duration:** 2.51s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data from diverse sources can mitigate some distribution-collapse effects in supervised fine-tuning, but this does not eliminate safety or evaluation risks.

**Confidence:** High

**Why this confidence level**

S14 is a direct peer-reviewed ACL study and provides more substantive primary evidence than the previously retrieved excerpt of S6, although it remains one study focused mainly on supervised fine-tuning.

**Evidence**

- The ACL study reports that greater diversity among synthetic-data sources preserved broader output and linguistic diversity and mitigated multiple measures of distribution collapse. [S14]
- The same study reports reduced adversarial robustness after synthetic fine-tuning and weaker reductions in self-preference bias than human-data fine-tuning, especially for single-source synthetic data. [S14]

#### Finding 2

**Claim**

Higher apparent quality or usability of synthetic fine-tuned outputs can coexist with weaker safety defenses, so quality gains should not be interpreted as overall model improvement.

**Confidence:** High

**Why this confidence level**

The distinction is directly reported in a primary study and is consistent with the accumulated evidence, though generalization across model families and safety tasks is not established.

**Evidence**

- S14 reports that synthetic fine-tuning preserved higher output quality while decreasing adversarial robustness and potentially making outputs more usable and dangerous. [S14]
- Prior findings similarly distinguish task or output quality from safety and robustness outcomes. [S6] [S7] [S2] [S4]

#### Finding 3

**Claim**

LLM-generated synthetic representations of social groups can be substantially uneven across countries and demographic groups, which is a warning against assuming that synthetic data is socially representative merely because it resembles aggregate human data.

**Confidence:** Medium

**Why this confidence level**

S13 provides direct, disaggregated evidence about LLM-simulated social responses, but it does not manipulate synthetic training data; therefore it supports a representation risk indirectly rather than establishing the causal effect of synthetic-data fine-tuning.

**Evidence**

- The fairness audit used nationally representative survey data from Chile and the United States and found that LLMs reproduced U.S. responses more faithfully than Chilean responses, with different disparities across race, political identity, gender, education, and religion. [S13]
- The study attributes the cross-national difference to predominantly U.S.-centric training data and characterizes the result as a risk in underrepresented and cross-cultural settings. [S13]

#### Finding 4

**Claim**

Fairness evaluation of synthetic-data pipelines should be disaggregated by relevant social and linguistic groups and tested against representative human data, rather than relying on aggregate benchmark performance or nominal distribution matching.

**Confidence:** High

**Why this confidence level**

The need for group-wise and cross-context evaluation is supported by direct fairness-audit evidence and multiple prior sources, even though the causal effect of training on synthetic data remains unresolved.

**Evidence**

- S13 reports substantial group- and country-level disparities despite the use of nationally representative survey comparisons. [S13]
- Accumulated evidence recommends subgroup metrics, held-out evaluation, prompt-sensitivity checks, and independent validation of evaluators. [S9] [S10] [S11] [S6]

#### Finding 5

**Claim**

The strongest current evidence supports conditional use of synthetic data: diverse, quality-filtered, source-mixed or additive pipelines may provide useful training signal, whereas single-source, recursive, or replacement-heavy pipelines carry greater risks of narrowing, inherited bias, and hidden degradation.

**Confidence:** High

**Why this confidence level**

The conditional pattern is consistent across the primary ACL study and accumulated evidence, although optimal mixture ratios and conditions are not yet established.

**Evidence**

- S14 finds that source diversity affects collapse, robustness, and self-preference outcomes in supervised fine-tuning. [S14]
- Prior sources distinguish curated additive mixtures from recursive or synthetic-only replacement and identify risks of tail loss, bias inheritance, and degradation. [S1] [S2] [S6] [S7] [S8]

### Conflicts Found

- S14 provides stronger evidence that multi-source synthetic data can mitigate distribution collapse, while recursive-training sources describe progressive narrowing. This is a conditional conflict involving source diversity, recursive generation, natural-data retention, and replacement versus additive mixtures, not a direct contradiction. [S14] [S6] [S8] [S1] [S2]
- S13 shows that LLM-simulated responses can reproduce some populations more faithfully than others, whereas sources presenting targeted synthetic generation describe representation balancing as a possible benefit. The evidence supports representation auditing but does not establish that targeted synthesis improves fairness. [S13] [S9] [S3] [S4]
- S14 reports higher output quality alongside weaker adversarial robustness, whereas other sources emphasize task-performance or workflow benefits. These findings concern different outcome dimensions and should not be aggregated into a single quality judgment. [S14] [S2] [S4] [S7]

### Important Gaps

- What are the causal effects of synthetic-only, mixed, and recursive training across pretraining, continued pretraining, supervised fine-tuning, and preference optimization?
- Does targeted synthetic augmentation improve minority-group performance without increasing stereotyping, hallucination, or other distributional artifacts?
- How do effects vary across demographic, intersectional, cultural, and multilingual groups, particularly outside U.S.-centric contexts?
- What are the effects on factuality, contamination, novelty, hallucination, calibration, and rare-case coverage under controlled matched experiments?
- How broadly do S14's diversity, robustness, and self-preference findings generalize across models, tasks, languages, source models, and mixture ratios?
- How should evaluators be independently validated when the same or related LLMs generate, filter, judge, and evaluate the data and outputs?
- Do offline quality and fairness changes persist under temporally separated, adversarial, expert-reviewed, and real-world deployment tests?

**Analysis Duration:** 19.70s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

A major core gap remains: no retrieved study causally compares synthetic-data training regimes and reports disaggregated demographic, linguistic, or intersectional outcomes. S13 strengthens the case for this evaluation but studies simulated opinion rather than synthetic training data. Further research would materially improve the answer.

**Next Search**

> controlled study synthetic data LLM fine-tuning demographic fairness subgroup multilingual intersectional evaluation synthetic versus human data

---

## Coverage Map After Iteration 4

| Dimension | Importance | Status | Searches |
|---|---|---|---:|
| D1 — Synthetic data’s effects on model data quality and learning | CORE | PARTIAL | 1 |
| D2 — Bias, fairness, and representation risks and benefits | CORE | PARTIAL | 3 |
| D3 — Evaluation validity and methods for detecting synthetic-data effects | CORE | PARTIAL | 0 |
| D4 — Failure modes, feedback loops, and model-collapse dynamics | CORE | PARTIAL | 0 |
| D5 — Real-world utility, safety, and deployment externalities | CORE | PARTIAL | 0 |
| D6 — Data provenance, privacy, and governance implications | SECONDARY | PARTIAL | 0 |
| D7 — Operational trade-offs and conditions for responsible use | SECONDARY | PARTIAL | 0 |

**Next search target:** D2

**Reason:**

A major core gap remains: no retrieved study causally compares synthetic-data training regimes and reports disaggregated demographic, linguistic, or intersectional outcomes. S13 strengthens the case for this evaluation but studies simulated opinion rather than synthetic training data. Further research would materially improve the answer.

---

# Iteration 5

## 1. Search

**Query**

> controlled study synthetic data LLM fine-tuning demographic fairness subgroup multilingual intersectional evaluation synthetic versus human data

**Why this query**

A major core gap remains: no retrieved study causally compares synthetic-data training regimes and reports disaggregated demographic, linguistic, or intersectional outcomes. S13 strengthens the case for this evaluation but studies simulated opinion rather than synthetic training data. Further research would materially improve the answer.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S15 — Synthetic Data Generation Strategies for Fine-Tuning LLMs**
  URL: https://scale.com/blog/synthetic-data-fine-tuning-llms
- **S16 — Creating and Validating Synthetic Datasets for LLM Evaluation & Experimentation - Arize AI**
  URL: https://arize.com/blog/creating-and-validating-synthetic-datasets-for-llm-evaluation-experimentation
- **S17 — GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub**
  URL: https://github.com/pengr/LLM-Synthetic-Data
- **S18 — Generating synthetic data with differentially private LLM inference**
  URL: https://research.google/blog/generating-synthetic-data-with-differentially-private-llm-inference

**Search Duration:** 2.15s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic-data generation strategy can materially affect supervised fine-tuning performance under limited query and seed-data budgets.

**Confidence:** Medium

**Why this confidence level**

S15 describes a controlled multi-task experiment, but the retrieved material is a company-authored summary, gives no effect sizes or uncertainty estimates, and does not establish generalization beyond the tested tasks and setup.

**Evidence**

- A controlled SFT experiment across mathematics, general question answering, and Text2SQL compared answer augmentation, question rephrasing, and new-question generation. The reported best strategy changed with the query-budget ratio: answer augmentation worked better under limited budgets, while new-question generation became more effective as the budget increased. [S15]

#### Finding 2

**Claim**

Synthetic data can reduce the fine-tuning data bottleneck and improve cost-effectiveness, but the benefit depends on task, seed-data availability, generation strategy, and inference budget.

**Confidence:** Medium

**Why this confidence level**

The source directly evaluates resource-constrained SFT strategies, but it does not provide an independent total-cost comparison with human data collection or curation.

**Evidence**

- S15 frames synthetic generation as a response to scarce task-specific datasets and reports that strategy choice matters most under constrained budgets, while differences diminish in data-rich scenarios. [S15]
- The source reports that question rephrasing remained effective with weaker augmentation models, suggesting a possible cost reduction for some fine-tuning settings. [S15]

#### Finding 3

**Claim**

Synthetic evaluation data can provide controlled, repeatable coverage for edge cases, application scenarios, debugging, and pre-launch experimentation, but it can also create misleading benchmark results if its sources overlap with model training data.

**Confidence:** Medium

**Why this confidence level**

The operational benefits and contamination concern are explicitly stated, but the retrieved excerpt does not quantify contamination or show that synthetic evaluation sets improve validity in deployment.

**Evidence**

- S16 describes synthetic datasets as useful for controlled experimentation, edge-case coverage, simulated application traffic, and repeatable 'golden' evaluation data. [S16]
- S16 cautions that publicly available datasets used as generation sources may already have appeared in model training, creating a benchmarking risk. [S16]

#### Finding 4

**Claim**

Differentially private inference can generate synthetic text with a formal privacy guarantee while retaining utility for downstream learning tasks, but privacy protection introduces quantity, quality, computational, and utility trade-offs.

**Confidence:** Medium

**Why this confidence level**

S18 describes a formal DP mechanism and downstream experiments, which is stronger evidence for a privacy-oriented benefit than generic privacy claims. However, the retrieved results are incomplete and do not establish privacy-utility performance across LLM training, demographic groups, or real sensitive datasets.

**Evidence**

- S18 presents an inference-only approach that aggregates predictions from many prompts under differential privacy, claiming generation of thousands of synthetic data points with DP guarantees; it evaluates synthetic data for GPT-3 in-context learning and BERT fine-tuning. [S18]
- S18 contrasts private prediction with private fine-tuning, describing a trade-off between releasing a limited number of higher-quality outputs and releasing larger quantities of lower-quality outputs, and discusses privacy-budget and computational-efficiency constraints. [S18]

#### Finding 5

**Claim**

The new evidence strengthens the case for conditional use of synthetic data in supervised fine-tuning and evaluation, but does not resolve whether synthetic data improves factuality, fairness, broad coverage, or deployment reliability.

**Confidence:** High

**Why this confidence level**

The positive findings are narrow and complementary, while the major evidence gaps remain explicit when compared with the accumulated findings.

**Evidence**

- S15 supplies task-specific SFT results under budget constraints, S16 supplies evaluation-workflow guidance and a contamination warning, and S18 supplies a privacy-preserving generation method with downstream utility tests. [S15] [S16] [S18]
- None of the new sources provides controlled matched demographic fairness outcomes, broad factuality measurements, independent replication, or real-world deployment comparisons for models trained on synthetic data. [S15] [S16] [S18]

### Conflicts Found

- S15 reports that synthetic-data strategy can improve task accuracy under constrained budgets, while accumulated evidence reports risks such as collapse, bias inheritance, and weakened adversarial robustness. These are conditional differences across task, generation strategy, mixture, and outcome metric rather than a direct contradiction. [S15] [S14] [S1] [S2]
- S18 presents differentially private synthetic data as a way to obtain formal privacy guarantees and useful downstream data, whereas prior sources caution that generic synthetic-data privacy claims are not established. The sources are compatible only when privacy is enforced and audited through an explicit DP mechanism; S18 does not validate ordinary synthetic generation as private. [S18] [S3] [S4]
- S15 reports that verification of synthetic responses had relatively little impact in its tested setting, while accumulated evidence emphasizes filtering, validation, and human or expert review as central to data quality. This may reflect differences in task, verification method, or measured outcome, and does not show that validation is generally unnecessary. [S15] [S4] [S7]
- S16 promotes synthetic evaluation data for repeatability and edge-case coverage but warns that public source datasets may contaminate benchmarks. Thus, synthetic evaluation data can improve experimental control while simultaneously reducing evaluation validity if provenance and overlap are not checked. [S16] [S5]

### Important Gaps

- What are the effect sizes and statistical uncertainty for S15's strategy comparisons, and do they replicate across model families, languages, domains, and larger datasets?
- Does synthetic-data strategy affect factuality, hallucination, calibration, diversity, rare-case coverage, or demographic outcomes beyond task accuracy?
- Does DP synthetic text preserve utility for LLM pretraining or fine-tuning at realistic privacy budgets, and how does it compare with private fine-tuning and non-private synthetic data?
- How much benchmark contamination or near-duplicate overlap occurs when synthetic evaluation data is generated from public datasets or model outputs?
- Does synthetic evaluation data correlate with expert and end-user judgments and with performance under temporally separated or deployment-like tests?
- How much human review, filtering, and independent evaluation is required for the benefits reported by S15 to remain reliable?

**Analysis Duration:** 22.20s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources add useful evidence on budget-sensitive SFT strategy, evaluation-data contamination, and a formal DP generation approach, but the central causal evaluation gap remains: there is no validated matched protocol showing when synthetic data improves overall model quality, fairness, or deployment reliability.

**Next Search**

> synthetic data LLM fine-tuning benchmark contamination held-out temporal evaluation causal ablation

---

## Coverage Map After Iteration 5

| Dimension | Importance | Status | Searches |
|---|---|---|---:|
| D1 — Synthetic data’s effects on model data quality and learning | CORE | PARTIAL | 1 |
| D2 — Bias, fairness, and representation risks and benefits | CORE | PARTIAL | 3 |
| D3 — Evaluation validity and methods for detecting synthetic-data effects | CORE | PARTIAL | 1 |
| D4 — Failure modes, feedback loops, and model-collapse dynamics | CORE | PARTIAL | 0 |
| D5 — Real-world utility, safety, and deployment externalities | CORE | PARTIAL | 0 |
| D6 — Data provenance, privacy, and governance implications | SECONDARY | PARTIAL | 0 |
| D7 — Operational trade-offs and conditions for responsible use | SECONDARY | PARTIAL | 0 |

**Next search target:** D3

**Reason:**

The new sources add useful evidence on budget-sensitive SFT strategy, evaluation-data contamination, and a formal DP generation approach, but the central causal evaluation gap remains: there is no validated matched protocol showing when synthetic data improves overall model quality, fairness, or deployment reliability.

---

# Iteration 6

## 1. Search

**Query**

> synthetic data LLM fine-tuning benchmark contamination held-out temporal evaluation causal ablation

**Why this query**

The new sources add useful evidence on budget-sensitive SFT strategy, evaluation-data contamination, and a formal DP generation approach, but the central causal evaluation gap remains: there is no validated matched protocol showing when synthetic data improves overall model quality, fairness, or deployment reliability.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S19 — Preprint 2025 CAUSCIBENCH: EVALUATING LLM CAUSAL REASON-**
  URL: https://zhijing-jin.com/files/papers/2025_CauSciBench.pdf
- **S20 — The benchmark leak: how your eval set quietly joins the training corpus**
  URL: https://tianpan.co/blog/2026-04-23-benchmark-leak-eval-contamination
- **S21 — GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub**
  URL: https://github.com/lyy1994/awesome-data-contamination
- **S22 — LLM Benchmark Datasets Should Be Contamination- ...**
  URL: https://arxiv.org/html/2605.19999v1

**Search Duration:** 2.12s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data can undermine evaluation validity when it reproduces or derives from public benchmark material, because the resulting evaluation may measure memorization or overlap rather than generalization.

**Confidence:** Medium

**Why this confidence level**

S22 provides a relevant research position grounded in cited studies, while S20 supplies operational suggestions but is a blog. The evidence concerns benchmark contamination generally and does not isolate synthetic-data pipelines.

**Evidence**

- CauSciBench explicitly combines real-world research problems with synthetic scenarios and describes the hybrid design as useful for diagnosing different failure sources; however, it does not study contamination caused by synthetic training data. [S19]
- The contamination-resistant benchmark paper states that public benchmarks can enter pretraining indirectly through derivative datasets, distillation, and continual pretraining, inflating reported accuracy and weakening generalization claims. [S22]
- The contamination-focused blog describes held-out twins, canary strings, and overlap analysis as ways to detect benchmark leakage, but its quantitative claims are not independently established in the retrieved material. [S20]

#### Finding 2

**Claim**

A credible evaluation of LLMs trained or fine-tuned with synthetic data should use fresh or contamination-resistant held-out tests rather than relying solely on public static benchmarks.

**Confidence:** High

**Why this confidence level**

The recommendation is consistent across the retrieved sources and prior findings, although the sources do not validate one complete causal protocol for synthetic-data effects.

**Evidence**

- S22 argues that contaminated public benchmarks no longer reliably measure generalization and discusses private, dynamically refreshed, decontaminated, and contamination-resistant alternatives, each with trade-offs. [S22]
- S20 recommends per-model held-out comparisons and fresh-evaluation rotation, while acknowledging that ordinary n-gram deduplication misses paraphrases and derivative artifacts. [S20]
- S19 illustrates a broader evaluation design that includes real-world research tasks, synthetic scenarios, and intermediate-step measurements rather than a single aggregate score. [S19]

#### Finding 3

**Claim**

Synthetic evaluation scenarios can improve controlled coverage and diagnosis, but they should complement rather than replace tests based on real-world data and representative deployment conditions.

**Confidence:** High

**Why this confidence level**

The distinction between controlled synthetic evaluation and real-world validation is directly supported by S19 and consistent with accumulated evaluation evidence.

**Evidence**

- S19 uses synthetic scenarios with user-defined ground truth alongside tasks derived from more than 100 real-world research papers, indicating that synthetic cases can support controlled diagnosis while real cases test practical complexity. [S19]
- Prior evidence recommends trusted natural, temporally separated, group-wise, adversarial, and expert-reviewed evaluations because synthetic or static benchmarks may miss factuality, fairness, robustness, and deployment failures. [S4] [S5] [S16]

#### Finding 4

**Claim**

Benchmark contamination is a meaningful evaluation risk for synthetic-data research, but the new sources do not establish how often synthetic training examples specifically overlap with benchmarks or how much such overlap inflates measured gains.

**Confidence:** High

**Why this confidence level**

The evidence clearly supports contamination as a general threat and clearly lacks the synthetic-specific causal measurement needed to estimate its impact.

**Evidence**

- S22 reports that benchmark material can enter training indirectly through derivative datasets and distillation, but does not quantify synthetic-data-specific pathways or effects. [S22]
- S20 gives strong contamination examples and detection proposals, but the retrieved content is a blog account and does not provide a controlled comparison of synthetic versus natural training data. [S20]
- The accumulated findings already identify contamination and near-duplicate leakage as unresolved issues in synthetic-data evaluation. [S16] [S5] [S15]

### Conflicts Found

- S19 presents synthetic scenarios as useful components of a rigorous benchmark, while S20 and S22 emphasize that publicly available or derivative evaluation material can contaminate training and inflate scores. These are conditional findings: synthetic evaluation data can improve control and coverage when provenance and separation are protected, but can reduce validity when it overlaps with training data. [S19] [S20] [S22]
- S22 favors contamination-resistant or controlled benchmarks but notes trade-offs involving independent verification and longitudinal comparability; S20 favors rotating or held-out evaluations. These approaches are complementary alternatives with operational trade-offs, not direct contradictions. [S20] [S22]

### Important Gaps

- How much benchmark overlap is introduced specifically by synthetic training and fine-tuning pipelines, including paraphrased or model-distilled derivatives?
- Do contamination-resistant or temporally held-out evaluations change the apparent advantage of synthetic, mixed, and natural-data training?
- What controlled synthetic-data experiments measure demographic and intersectional fairness outcomes across languages and cultures?
- Do evaluation gains observed on synthetic scenarios transfer to real-world, expert-reviewed, temporally separated, and deployment-like tasks?
- How should synthetic evaluation scenarios be validated against expert and end-user judgments?
- What are the effect sizes and uncertainty estimates for contamination-related score inflation in synthetic-data studies?

**Analysis Duration:** 18.41s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new evidence materially strengthens the evaluation-validity discussion, especially the need for held-out and contamination-resistant tests, but it does not resolve the most important remaining causal gap: whether synthetic training changes fairness and subgroup outcomes, nor does it quantify synthetic-specific contamination effects.

**Next Search**

> controlled study synthetic data LLM fine-tuning subgroup fairness held-out evaluation contamination matched natural mixed data

---

## Coverage Map After Iteration 6

| Dimension | Importance | Status | Searches |
|---|---|---|---:|
| D1 — Synthetic data’s effects on model data quality and learning | CORE | PARTIAL | 1 |
| D2 — Bias, fairness, and representation risks and benefits | CORE | PARTIAL | 4 |
| D3 — Evaluation validity and methods for detecting synthetic-data effects | CORE | SUFFICIENT | 1 |
| D4 — Failure modes, feedback loops, and model-collapse dynamics | CORE | PARTIAL | 0 |
| D5 — Real-world utility, safety, and deployment externalities | CORE | PARTIAL | 0 |
| D6 — Data provenance, privacy, and governance implications | SECONDARY | PARTIAL | 0 |
| D7 — Operational trade-offs and conditions for responsible use | SECONDARY | PARTIAL | 0 |

**Next search target:** D2

**Reason:**

The new evidence materially strengthens the evaluation-validity discussion, especially the need for held-out and contamination-resistant tests, but it does not resolve the most important remaining causal gap: whether synthetic training changes fairness and subgroup outcomes, nor does it quantify synthetic-specific contamination effects.

---

# Iteration 7

## 1. Search

**Query**

> controlled study synthetic data LLM fine-tuning subgroup fairness held-out evaluation contamination matched natural mixed data

**Why this query**

The new evidence materially strengthens the evaluation-validity discussion, especially the need for held-out and contamination-resistant tests, but it does not resolve the most important remaining causal gap: whether synthetic training changes fairness and subgroup outcomes, nor does it quantify synthetic-specific contamination effects.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S23 — Advancing Algorithmic Fairness via Selectively Fine-Tuning ...**
  URL: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_AIM-Fair_Advancing_Algorithmic_Fairness_via_Selectively_Fine-Tuning_Biased_Models_with_CVPR_2025_paper.pdf
- **S24 — Towards Understanding Bias in Synthetic Data for Evaluation | alphaXiv**
  URL: https://www.alphaxiv.org/abs/2506.10301
- **S25 — Synthetic Data + Evaluation Pipelines: Scaling Fine-Tuning ...**
  URL: https://medium.com/@akankshasinha247/synthetic-data-evaluation-pipelines-scaling-fine-tuning-without-losing-alignment-f469a81cdf9a

**Search Duration:** 2.22s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic-data fine-tuning can improve fairness in a controlled setting, but improvements may require addressing both synthetic-to-real domain shift and the quality or diversity of generated examples.

**Confidence:** Medium

**Why this confidence level**

S23 reports experiments on two image-classification datasets, not LLM training or fine-tuning. It is therefore relevant evidence for the mechanism and trade-off, but indirect for the original LLM question.

**Evidence**

- AIM-Fair fine-tunes a model initially trained on biased real-world data using balanced synthetic images. On CelebA and UTKFace, its contextual generation and selective fine-tuning reportedly improved fairness while maintaining utility, outperforming fully and partially fine-tuned alternatives. [S23]
- The paper identifies low synthetic-data quality, limited diversity, and gaps between real and synthetic data as causes of reduced utility when synthetic data is used without selective adaptation. [S23]

#### Finding 2

**Claim**

Balanced synthetic data does not automatically improve overall model quality or fairness; naive fine-tuning can trade aggregate utility for better subgroup outcomes or can fail because of domain mismatch.

**Confidence:** Medium

**Why this confidence level**

The reported controlled comparisons directly demonstrate a fairness–utility trade-off in the tested vision setting, but effect sizes, uncertainty, and transfer to LLMs are not provided in the retrieved excerpt.

**Evidence**

- The AIM-Fair paper contrasts real-data training, balanced synthetic-data training, and selective fine-tuning: balanced synthetic data improved fairness but produced poorer accuracy, while the proposed selective method reportedly maintained accuracy and improved fairness. [S23]
- Layer-freezing experiments show that different fine-tuning choices produce different overall-accuracy, worst-group-accuracy, and equalized-odds outcomes. [S23]

#### Finding 3

**Claim**

Synthetic evaluation data can introduce systematic evaluator and task-distribution bias, potentially overstating system performance even when it is useful for relative comparisons.

**Confidence:** Medium

**Why this confidence level**

S24 provides direct empirical analysis of synthetic evaluation bias with human and LLM comparisons, but it concerns information-retrieval test collections rather than evaluation of LLM training effects specifically.

**Evidence**

- The study of synthetic IR test collections reports that LLM-generated queries differ systematically from human queries, including query length and wording, and that GPT-4 relevance judgments were approximately 0.28 points more positive than human judgments on average. [S24]
- The study reports that these biases can significantly affect absolute system-performance estimates, while their effect may be smaller when comparing systems relatively. [S24]

#### Finding 4

**Claim**

Synthetic evaluation should not be treated as interchangeable with human or real-world evaluation, because generation and judging processes can favor particular query styles, relevance interpretations, or system architectures.

**Confidence:** High

**Why this confidence level**

The new empirical study and multiple accumulated sources consistently support using synthetic evaluation as a complement rather than a sole validation method.

**Evidence**

- S24 analyzes differences in synthetic versus human queries and judgments and models interactions among judge type, query characteristics, and system architecture, indicating that evaluation bias is conditional rather than a single universal offset. [S24]
- Prior evidence recommends fresh, contamination-resistant, held-out, group-wise, adversarial, and expert-reviewed tests in addition to synthetic scenarios. [S19] [S20] [S22] [S4] [S5] [S16]

#### Finding 5

**Claim**

The accumulated evidence supports conditional use of synthetic data, not a general claim that synthetic data is beneficial or harmful: quality-filtered, diverse, additive mixtures can provide scalable task-specific signal, while naive, single-source, recursive, or replacement-heavy pipelines risk bias, narrowing, and hidden degradation.

**Confidence:** High

**Why this confidence level**

The conditional pattern is consistent across the strongest retrieved primary study and multiple supporting sources, although optimal mixtures and generalization across LLM families, languages, and domains remain unknown.

**Evidence**

- The ACL study reports that source diversity can mitigate distribution collapse but also reports reduced adversarial robustness and weaker self-preference-bias reduction than human-data fine-tuning. [S14]
- Other sources describe benefits for scarce labels, rare cases, privacy-constrained settings, and task-specific fine-tuning, while warning about recursive collapse, inherited generator bias, and the need to retain natural data. [S1] [S2] [S3] [S4] [S6] [S7] [S15] [S18]
- S23 adds evidence that synthetic-data quality and real–synthetic domain shift can determine whether fairness gains preserve utility. [S23]

### Conflicts Found

- S23 reports that carefully designed, selectively fine-tuned balanced synthetic data can improve fairness while preserving utility, whereas prior sources warn that synthetic augmentation may inherit bias or reduce utility. This is a conditional difference reflecting generation quality, domain shift, and fine-tuning strategy rather than a direct contradiction. [S23] [S3] [S4] [S6]
- S24 suggests synthetic evaluation bias may substantially distort absolute scores but have a smaller effect on relative system rankings. Thus synthetic evaluations may be useful for some comparative purposes while remaining unreliable for absolute claims or deployment readiness. [S24]
- S23 concerns image classification rather than LLMs, so its positive fairness result cannot be directly combined with the absence of controlled demographic LLM fine-tuning evidence. [S23] [S9] [S10] [S13] [S14]

### Important Gaps

- Whether the fairness improvements in S23 transfer to LLM supervised fine-tuning, preference optimization, or continued pretraining.
- Whether targeted or balanced synthetic LLM data improves minority-group performance without increasing stereotyping, hallucination, or cultural misrepresentation.
- How synthetic-only, mixed, and recursive LLM training compare on factuality, calibration, diversity, rare-case coverage, and hallucination.
- How often synthetic training or evaluation examples overlap with benchmarks or their derivatives, and how much this inflates reported gains.
- Whether offline quality, fairness, and robustness changes persist under temporally separated, adversarial, expert-reviewed, and deployment-like tests.
- How evaluators should be independently validated when the same or related LLMs generate, filter, judge, and evaluate synthetic data.

**Analysis Duration:** 23.27s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new evidence materially strengthens evaluation-bias conclusions and provides indirect evidence that careful synthetic-data design can improve fairness while preserving utility. However, bias and fairness remain a central unanswered dimension for the original question because no retrieved source directly tests synthetic LLM training or fine-tuning with disaggregated demographic, cultural, linguistic, or intersectional outcomes. A focused search could materially improve the answer.

**Next Search**

> controlled LLM synthetic instruction tuning fairness subgroup performance multilingual demographic evaluation human versus synthetic data

---

## Coverage Map After Iteration 7

| Dimension | Importance | Status | Searches |
|---|---|---|---:|
| D1 — Synthetic data’s effects on model data quality and learning | CORE | PARTIAL | 1 |
| D2 — Bias, fairness, and representation risks and benefits | CORE | PARTIAL | 5 |
| D3 — Evaluation validity and methods for detecting synthetic-data effects | CORE | SUFFICIENT | 1 |
| D4 — Failure modes, feedback loops, and model-collapse dynamics | CORE | PARTIAL | 0 |
| D5 — Real-world utility, safety, and deployment externalities | CORE | PARTIAL | 0 |
| D6 — Data provenance, privacy, and governance implications | SECONDARY | PARTIAL | 0 |
| D7 — Operational trade-offs and conditions for responsible use | SECONDARY | PARTIAL | 0 |

**Next search target:** D2

**Reason:**

The new evidence materially strengthens evaluation-bias conclusions and provides indirect evidence that careful synthetic-data design can improve fairness while preserving utility. However, bias and fairness remain a central unanswered dimension for the original question because no retrieved source directly tests synthetic LLM training or fine-tuning with disaggregated demographic, cultural, linguistic, or intersectional outcomes. A focused search could materially improve the answer.

---

# Iteration 8

## 1. Search

**Query**

> controlled LLM synthetic instruction tuning fairness subgroup performance multilingual demographic evaluation human versus synthetic data

**Why this query**

The new evidence materially strengthens evaluation-bias conclusions and provides indirect evidence that careful synthetic-data design can improve fairness while preserving utility. However, bias and fairness remain a central unanswered dimension for the original question because no retrieved source directly tests synthetic LLM training or fine-tuning with disaggregated demographic, cultural, linguistic, or intersectional outcomes. A focused search could materially improve the answer.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S26 — A Methodology for Controlling Bias and Fairness in Synthetic Data Generation**
  URL: https://www.mdpi.com/2076-3417/12/9/4619
- **S27 — Diving Deep Into Fair Synthetic Data Generation (Fairness Series Part 5) - MOSTLY AI powered by Syntho**
  URL: https://mostly.ai/blog/diving-deep-into-fair-synthetic-data-generation-fairness-series-part-5
- **S28 — DS2-Instruct: Domain-Specific Data Synthesis for Large Language Models Instruction Tuning**
  URL: https://arxiv.org/html/2603.12932v2

**Search Duration:** 2.70s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

DS2-Instruct reports a domain-specific synthetic instruction-generation pipeline that uses task-informed keywords, cognitive-level variation, retrieval augmentation, and self-consistency filtering, with the aim of improving domain coverage and instruction diversity without human-written seeds.

**Confidence:** Medium

**Why this confidence level**

The retrieved paper directly describes the method and evaluated models, but the excerpt provides limited experimental detail and does not establish whether the gains are caused by the individual pipeline components.

**Evidence**

- The paper describes a zero-shot framework using keyword expansion, Bloom’s Taxonomy, retrieval augmentation, and self-consistency filtering; it generates data in seven domains and fine-tunes Llama3-8B, Mistral-7B, and Qwen2.5-7B. [S28]

#### Finding 2

**Claim**

In the reported DS2-Instruct experiments, models fine-tuned on the generated domain-specific data improved on seven domain-specific benchmarks relative to the authors’ comparison methods.

**Confidence:** Low

**Why this confidence level**

This is a single retrieved paper’s summary claim without effect sizes, uncertainty estimates, full baselines, contamination checks, or independent replication. It also does not show broad factuality, fairness, or deployment improvements.

**Evidence**

- The abstract and introduction report substantial improvements over existing data-generation methods across seven domain-specific benchmarks. [S28]

#### Finding 3

**Claim**

The DS2-Instruct results support a conditional benefit of task-shaped synthetic data for supervised fine-tuning, but do not establish that zero-shot synthetic generation is generally high quality or superior to human-curated data.

**Confidence:** Medium

**Why this confidence level**

The conditional interpretation is consistent with the new method and prior findings, but the new source does not compare its zero-shot data against matched human-written data across broader outcome measures.

**Evidence**

- The framework is designed around domain coverage, cognitive diversity, and self-consistency filtering, and reports benchmark gains in selected domains. [S28]
- Accumulated evidence shows that synthetic-data benefits depend on task, generation strategy, filtering, source diversity, and mixture with natural data, while causal comparisons with human data remain limited. [S14] [S15] [S2] [S4]

#### Finding 4

**Claim**

The new fairness-related sources do not provide direct evidence about demographic or intersectional effects of synthetic text used to train or fine-tune LLMs.

**Confidence:** High

**Why this confidence level**

The retrieved material does not report an LLM synthetic-training intervention with disaggregated demographic, linguistic, cultural, or intersectional outcomes.

**Evidence**

- S26 is an article page whose retrieved content contains bibliographic and navigation material but no substantive experimental findings in the available excerpt. [S26]
- S27 demonstrates fairness constraints and statistical-parity analysis for tabular Adult and COMPAS data, not LLM training or text generation. [S27]
- Prior evidence already found no controlled LLM subgroup or intersectional outcomes for synthetic-data fine-tuning. [S9] [S10] [S13] [S23]

#### Finding 5

**Claim**

Fairness constraints and rebalancing can target a selected statistical disparity, but passing one parity measure does not establish general fairness or preservation of task validity.

**Confidence:** Medium

**Why this confidence level**

The source gives a concrete fairness-control methodology and acknowledges proxy risks, but it concerns tabular datasets and does not test LLM outcomes or downstream deployment harms.

**Evidence**

- S27 explains statistical parity and describes adding a fairness constraint during synthetic-data generation, while also noting that removing sensitive attributes can leave proxy variables that preserve unfair correlations. [S27]
- Prior sources emphasize that fairness depends on the use case and requires subgroup, prompt-sensitivity, and held-out evaluation rather than assuming rebalancing is sufficient. [S9] [S10] [S11]

### Conflicts Found

- S28 presents self-consistency filtering and systematic domain/cognitive diversification as sufficient components of a high-quality zero-shot synthesis pipeline, whereas accumulated evidence treats automated filtering and benchmark gains as insufficient evidence of factuality, broad coverage, fairness, or deployment reliability. This is a difference in evidentiary strength, not a direct contradiction. [S28] [S4] [S5] [S14]
- S27 presents fairness-constrained synthetic generation as a way to reduce statistical disparity, while accumulated LLM evidence warns that generator, prompt, evaluator, and proxy-variable effects can preserve or introduce bias. The methods may improve a chosen metric without ensuring robust cross-context fairness. [S27] [S9] [S10] [S11]
- S28 claims benefits without human supervision or seed data, while prior operational evidence recommends human seeds, real-data anchoring, source mixing, and independent validation. The difference concerns pipeline design and validation burden rather than an established empirical contradiction. [S28] [S7] [S14]

### Important Gaps

- Do DS2-Instruct’s reported gains persist on contamination-resistant, temporally separated, human- or expert-reviewed tests?
- How does zero-shot domain-specific synthesis compare with matched human-written, natural-document-derived, and mixed synthetic-natural instruction data?
- What are the effects of DS2-style synthesis on factuality, hallucination, calibration, rare-case coverage, linguistic diversity, and demographic or intersectional fairness?
- Does self-consistency filtering remain reliable when the same model family generates, filters, and evaluates the data?
- Can fairness constraints or statistical rebalancing for synthetic data improve LLM subgroup outcomes without increasing stereotyping, cultural misrepresentation, or factual errors?
- What are the effect sizes, uncertainty estimates, and component-level ablations for keyword expansion, retrieval augmentation, Bloom-level diversification, and self-consistency filtering?

**Analysis Duration:** 19.86s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new evidence adds a potentially useful domain-specific SFT method but does not resolve the most important remaining core gap: controlled, disaggregated LLM evidence on whether synthetic data improves or worsens quality and fairness relative to natural or mixed data. S26 and S27 are not direct LLM evidence.

**Next Search**

> controlled LLM instruction tuning synthetic data subgroup fairness factuality ablation human data mixed synthetic data held-out evaluation

---

## Coverage Map After Iteration 8

| Dimension | Importance | Status | Searches |
|---|---|---|---:|
| D1 — Synthetic data’s effects on model data quality and learning | CORE | PARTIAL | 1 |
| D2 — Bias, fairness, and representation risks and benefits | CORE | PARTIAL | 6 |
| D3 — Evaluation validity and methods for detecting synthetic-data effects | CORE | SUFFICIENT | 1 |
| D4 — Failure modes, feedback loops, and model-collapse dynamics | CORE | PARTIAL | 0 |
| D5 — Real-world utility, safety, and deployment externalities | CORE | PARTIAL | 0 |
| D6 — Data provenance, privacy, and governance implications | SECONDARY | PARTIAL | 0 |
| D7 — Operational trade-offs and conditions for responsible use | SECONDARY | PARTIAL | 0 |

**Next search target:** D2

**Reason:**

The new evidence adds a potentially useful domain-specific SFT method but does not resolve the most important remaining core gap: controlled, disaggregated LLM evidence on whether synthetic data improves or worsens quality and fairness relative to natural or mixed data. S26 and S27 are not direct LLM evidence.

---

# Iteration 9

## 1. Search

**Query**

> controlled LLM instruction tuning synthetic data subgroup fairness factuality ablation human data mixed synthetic data held-out evaluation

**Why this query**

The new evidence adds a potentially useful domain-specific SFT method but does not resolve the most important remaining core gap: controlled, disaggregated LLM evidence on whether synthetic data improves or worsens quality and fairness relative to natural or mixed data. S26 and S27 are not direct LLM evidence.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S29 — How to Generate and Use Synthetic Data for Finetuning**
  URL: https://eugeneyan.com/writing/synthetic
- **S30 — Generating Synthetic Data for LLM Post-Training**
  URL: https://www.jonvet.com/blog/llm-synthetic-data
- **S31 — Synthetic data for LLM fine-tuning and alignment - Argilla**
  URL: https://argilla.io/blog/synthetic-data

**Search Duration:** 1.98s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data can reduce the cost and time of producing task-specific instruction, preference, and alignment data, and can support training at stages ranging from pretraining augmentation to instruction- and preference-tuning.

**Confidence:** Medium

**Why this confidence level**

The benefit is consistently described, but these sources are practitioner surveys and framework documentation rather than matched cost studies or independently validated deployment comparisons.

**Evidence**

- S29 describes synthetic data as faster and cheaper than human annotation and identifies applications in pretraining, instruction-tuning, and preference-tuning. [S29]
- S31 describes synthetic instructions, preferences, critiques, and AI-generated feedback as components of LLM fine-tuning and alignment workflows. [S31]

#### Finding 2

**Claim**

Synthetic data is most useful when generation is task-shaped and quality-controlled, especially where outputs can be externally verified.

**Confidence:** Medium

**Why this confidence level**

The sources provide concrete workflow evidence and examples, but do not isolate the causal contribution of each filter, verifier, or generation component.

**Evidence**

- S30 describes execution feedback, compilation, unit tests, calculators, code interpreters, self-consistency, and model-based filtering as ways to improve synthetic SFT data quality. [S30]
- S29 describes seed-task bootstrapping, filtering invalid or similar examples, and distillation from stronger models; S31 recommends separating instruction generation from response generation and curating instructions before producing responses. [S29] [S31]

#### Finding 3

**Claim**

Self-improvement and recursive synthetic-data generation remain vulnerable to inherited errors and biases because the model is limited by its initial capabilities and may reinforce its own outputs.

**Confidence:** High

**Why this confidence level**

The mechanism is directly stated in S29 and is consistent with the stronger primary evidence and prior model-collapse findings, although the precise thresholds and generation conditions remain unknown.

**Evidence**

- S29 explicitly states that self-improvement limits learning to the model’s initial abilities and can amplify biases and errors. [S29]
- Accumulated evidence reports distribution narrowing and quality degradation under recursive or replacement-heavy regimes, while additive mixtures retaining natural data are safer than synthetic-only replacement. [S1] [S2] [S6] [S14]

#### Finding 4

**Claim**

Synthetic data can improve coverage of specialized skills, underrepresented domains, tool use, safety behaviors, and less common languages, but increased nominal coverage does not establish accurate or fair representation.

**Confidence:** Medium

**Why this confidence level**

The sources document plausible and operationally concrete coverage benefits, but do not provide broad controlled measurements of factuality, subgroup representation, or multilingual transfer.

**Evidence**

- S30 describes generating tool-use examples, translating code into less common programming languages, creating adversarial safety data, and targeting underrepresented domains. [S30]
- S29 and S31 describe task-specific instruction and preference generation, while prior evidence warns that generated data may inherit generator or prompt biases and omit demographic or linguistic groups. [S29] [S31] [S3] [S4] [S13]

#### Finding 5

**Claim**

Synthetic-data pipelines can produce misleading quality assessments when the same or related models generate, filter, judge, and evaluate the data.

**Confidence:** High

**Why this confidence level**

The sources directly document reliance on model-based evaluation and an observed score-quality mismatch, reinforced by prior empirical evaluator-bias findings.

**Evidence**

- S30 lists LLM judging, scoring, self-verification, and self-correction as common filtering mechanisms; S31 reports a mismatch between an overall critique score and response quality in a practical workflow. [S30] [S31]
- Prior evidence shows evaluator self-preference and prompt-structure bias, and recommends independent evaluators and human or expert review. [S6] [S9] [S10] [S24]

#### Finding 6

**Claim**

Synthetic data may improve output or task performance while degrading safety, robustness, or broader generalization; these outcomes must be evaluated separately.

**Confidence:** High

**Why this confidence level**

The distinction between capability or output quality and safety robustness is directly supported by primary evidence and is consistent with the new workflow sources.

**Evidence**

- S30 describes synthetic SFT as improving capabilities such as coding, mathematics, and tool use, but does not claim that these gains imply safety or deployment reliability. [S30]
- The ACL study found higher output quality alongside reduced adversarial robustness after synthetic fine-tuning, with source diversity affecting collapse and self-preference outcomes. [S14]

#### Finding 7

**Claim**

Synthetic data does not inherently remove privacy or copyright risk; stronger privacy claims require an explicit mechanism and validation of provenance, leakage, consent, and licensing.

**Confidence:** Medium

**Why this confidence level**

S29 reveals both the proposed benefit and important legal limitations, while the accumulated evidence does not establish that ordinary synthetic text is private or copyright-safe.

**Evidence**

- S29 claims synthetic data can sidestep privacy and copyright concerns, but also notes legal and contractual risks when distilling external models or using their outputs. [S29]
- Prior evidence distinguishes formal differential-privacy mechanisms from ordinary synthetic generation and identifies unresolved memorization, provenance, re-identification, and consent questions. [S18] [S3] [S4]

### Conflicts Found

- S29 presents synthetic data as potentially cheaper, higher quality, more diverse, and privacy-preserving than human annotation, whereas accumulated primary evidence shows that synthetic fine-tuning can reduce adversarial robustness and that privacy, fairness, and broad quality benefits remain unproven. These are conditional and outcome-specific differences, not a direct contradiction. [S29] [S14] [S18] [S3] [S4]
- S30 emphasizes self-verification, model judges, and external feedback as quality controls, while S31 reports that critique scores can mismatch actual response quality and prior evidence warns that model-based evaluators have self-preference and prompt-structure biases. Automated verification may help, but cannot by itself establish data quality. [S30] [S31] [S6] [S10] [S24]
- S30 describes iterative SFT and self-correction as productive uses of synthetic data, while accumulated model-collapse evidence warns that recursive or replacement-heavy generation can narrow distributions. The outcome depends on whether fresh information, external verification, source diversity, and natural data are retained. [S30] [S1] [S2] [S8] [S14]

### Important Gaps

- What are the causal effects of synthetic-only, mixed, and recursively generated data across pretraining, continued pretraining, SFT, and preference optimization?
- How do synthetic-data methods affect factuality, hallucination, calibration, rare-case coverage, multilingual representation, and demographic or intersectional fairness?
- How much do model-based filtering and self-consistency checks improve quality when the generator and evaluator are from the same model family?
- Do reported task or benchmark gains persist on contamination-resistant, temporally separated, expert-reviewed, adversarial, and deployment-like tests?
- What are the actual total costs, including generation, compute, filtering, human review, and maintenance, compared with collecting or curating natural data?
- Do synthetic-data pipelines provide measurable privacy, consent, licensing, and provenance advantages, or merely obscure the origin of learned information?
- Under what mixture ratios and number of generations does recursive synthetic training cause measurable loss of diversity, tail coverage, or factuality?

**Analysis Duration:** 24.26s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources add practical detail about generation, verification, and training-stage uses, but do not resolve the most important core causal gap: controlled multi-generation comparisons of synthetic-only, mixed, and natural data with measurements of collapse, factuality, diversity, and rare-case coverage. This gap materially affects the responsible risk-benefit conclusion.

**Next Search**

> controlled multi-generation recursive synthetic data LLM training mixture ratio model collapse factuality diversity rare-case coverage natural data comparison

---

## Coverage Map After Iteration 9

| Dimension | Importance | Status | Searches |
|---|---|---|---:|
| D1 — Synthetic data’s effects on model data quality and learning | CORE | PARTIAL | 1 |
| D2 — Bias, fairness, and representation risks and benefits | CORE | PARTIAL | 6 |
| D3 — Evaluation validity and methods for detecting synthetic-data effects | CORE | SUFFICIENT | 1 |
| D4 — Failure modes, feedback loops, and model-collapse dynamics | CORE | PARTIAL | 1 |
| D5 — Real-world utility, safety, and deployment externalities | CORE | PARTIAL | 0 |
| D6 — Data provenance, privacy, and governance implications | SECONDARY | PARTIAL | 0 |
| D7 — Operational trade-offs and conditions for responsible use | SECONDARY | PARTIAL | 0 |

**Next search target:** D4

**Reason:**

The new sources add practical detail about generation, verification, and training-stage uses, but do not resolve the most important core causal gap: controlled multi-generation comparisons of synthetic-only, mixed, and natural data with measurements of collapse, factuality, diversity, and rare-case coverage. This gap materially affects the responsible risk-benefit conclusion.

---

# Iteration 10

## 1. Search

**Query**

> controlled multi-generation recursive synthetic data LLM training mixture ratio model collapse factuality diversity rare-case coverage natural data comparison

**Why this query**

The new sources add practical detail about generation, verification, and training-stage uses, but do not resolve the most important core causal gap: controlled multi-generation comparisons of synthetic-only, mixed, and natural data with measurements of collapse, factuality, diversity, and rare-case coverage. This gap materially affects the responsible risk-benefit conclusion.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S32 — Synthetic Data Generation Using Large Language Models: Advances in Text and Code**
  URL: https://arxiv.org/html/2503.14023v2
- **S33 — AI models collapse when trained on recursively generated data | Hacker News**
  URL: https://news.ycombinator.com/item?id=41058194
- **S34 — What happens when generative AI models train recursively on each others’ outputs?**
  URL: https://arxiv.org/html/2505.21677v3
- **S35 — Publications & Research**
  URL: https://mbrenndoerfer.com/publications

**Search Duration:** 3.20s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

LLM-generated synthetic text and code can expand low-resource training data and reduce annotation burden, but the benefits depend on task relevance, curation, and verification rather than synthetic volume alone.

**Confidence:** Medium

**Why this confidence level**

S32 is a survey synthesizing prior work rather than a new controlled comparison; its reported performance improvements are not accompanied here by full baselines, uncertainty, or deployment validation.

**Evidence**

- The survey identifies scarcity, annotation cost, and privacy constraints as motivations for synthetic data, and describes gains in low-resource classification, question answering, instruction tuning, and code tasks. It also emphasizes filtering, weighting, retrieval, and execution feedback. [S32]

#### Finding 2

**Claim**

Synthetic-data quality risks include factual inaccuracies, weak stylistic or distributional realism, and bias amplification; code generation offers a more directly verifiable setting when functional execution tests are available.

**Confidence:** Medium

**Why this confidence level**

The mechanisms and mitigations are clearly stated, but the retrieved survey excerpt does not quantify their effectiveness or establish that code verification transfers to open-ended text.

**Evidence**

- The survey explicitly lists factuality, realism, distributional mismatch, and bias amplification as challenges, while describing execution-based verification and reinforcement from feedback as mitigation strategies for code. [S32]

#### Finding 3

**Claim**

The distinction between beneficial augmentation and harmful recursive replacement is supported by newer empirical work: interactions among heterogeneous models can expose novel concepts, while repeated training on model outputs can homogenize performance on shared tasks.

**Confidence:** High

**Why this confidence level**

S34 presents both theory and experiments on LLMs and directly supports a conditional, regime-dependent conclusion. However, the retrieved excerpt does not provide detailed effect sizes or all experimental conditions.

**Evidence**

- S34 reports theoretical and experimental results in which training on novel synthetic data may improve performance or expose missed concepts, but data-mediated interactions among models can also homogenize performance. [S34]
- The same paper describes prior collapse findings involving tail loss and degradation, and distinguishes retaining real data and adding synthetic data from discarding the original data. [S34]

#### Finding 4

**Claim**

Source diversity alone should not be interpreted as eliminating recursive-training risk; novelty and retention of real or external information are important conditions for potential benefit.

**Confidence:** High

**Why this confidence level**

The conditional pattern is consistent across the new empirical/theoretical study and the prior primary ACL evidence, although precise thresholds and mixture ratios remain unknown.

**Evidence**

- S34 states that heterogeneous models and novel datasets can produce positive effects, while recursive training on the same data is associated with overfitting, collapse, and homogenization. [S34]
- Accumulated evidence similarly finds that source diversity can mitigate distribution collapse in supervised fine-tuning but does not remove safety, bias, or evaluation risks. [S14]

#### Finding 5

**Claim**

The new sources do not materially resolve the central causal questions about demographic fairness, intersectional representation, factuality, contamination, or deployment reliability for LLMs trained on synthetic data.

**Confidence:** High

**Why this confidence level**

The retrieved material clearly supplies relevant risks and mechanisms but lacks the matched, disaggregated, contamination-controlled, deployment-oriented experiments needed to answer these questions.

**Evidence**

- S32 is a survey that identifies these as open challenges, while S34 focuses on recursive interactions, novel concepts, and homogenization rather than disaggregated fairness or deployment outcomes. [S32] [S34]
- Accumulated findings report no controlled LLM synthetic-text intervention with demographic, linguistic, or intersectional outcomes, and no synthetic-specific measurement of contamination inflation or field performance. [S13] [S14] [S22] [S24]

### Conflicts Found

- S34 reports that synthetic outputs from heterogeneous models can introduce novel concepts and improve performance in some settings, while also finding homogenization and prior work reports collapse under recursive use. This is a conditional disagreement governed by novelty, source heterogeneity, real-data retention, and recursive versus additive training, not a direct contradiction. [S34] [S14] [S1] [S2]
- S32 presents synthetic data as potentially cost-effective and broadening coverage, whereas the accumulated primary evidence shows that apparent output-quality or task gains can coexist with weaker adversarial robustness. These claims concern different outcome dimensions and should not be combined into a single quality score. [S32] [S14]
- S33's discussion suggests that deliberate filtering can control collapse and that human filtering may be sufficient, but it is an informal comment thread rather than controlled evidence. Its claims cannot outweigh S34 and the prior primary studies, especially regarding loss of tail events that filtering cannot recreate. [S33] [S34] [S14]

### Important Gaps

- What are the effect sizes and conditions under which heterogeneous-model synthetic data exposes genuinely novel concepts rather than merely stylistic variation or shared errors?
- How do recursive, cross-model, mixed, and synthetic-only regimes compare across multiple generations, mixture ratios, languages, and training stages?
- Do synthetic-data benefits persist on factuality, calibration, rare-case coverage, contamination-resistant tests, and deployment-like evaluations?
- What controlled LLM experiments measure demographic, cultural, linguistic, and intersectional fairness effects of synthetic text fine-tuning?
- How should evaluators be independently validated when generation, filtering, and evaluation use related model families?

**Analysis Duration:** 20.25s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The runner reached the maximum research iteration budget. Analyzer assessment: The new S34 strengthens the evidence for conditional model-collapse and cross-model interaction effects, but the most important remaining core gap is direct evidence on demographic, cultural, linguistic, and intersectional bias outcomes from synthetic text used to train or fine-tune LLMs. Existing evidence discusses this risk or studies LLM fairness without manipulating synthetic training data.

**Stop Reason:** max_iterations

---

## Coverage Map After Iteration 10

| Dimension | Importance | Status | Searches |
|---|---|---|---:|
| D1 — Synthetic data’s effects on model data quality and learning | CORE | PARTIAL | 1 |
| D2 — Bias, fairness, and representation risks and benefits | CORE | PARTIAL | 6 |
| D3 — Evaluation validity and methods for detecting synthetic-data effects | CORE | SUFFICIENT | 1 |
| D4 — Failure modes, feedback loops, and model-collapse dynamics | CORE | SUFFICIENT | 1 |
| D5 — Real-world utility, safety, and deployment externalities | CORE | PARTIAL | 0 |
| D6 — Data provenance, privacy, and governance implications | SECONDARY | PARTIAL | 0 |
| D7 — Operational trade-offs and conditions for responsible use | SECONDARY | PARTIAL | 0 |

**Next search target:** None

**Reason:**

The new S34 strengthens the evidence for conditional model-collapse and cross-model interaction effects, but the most important remaining core gap is direct evidence on demographic, cultural, linguistic, and intersectional bias outcomes from synthetic text used to train or fine-tune LLMs. Existing evidence discusses this risk or studies LLM fairness without manipulating synthetic training data.

---

# Final Research Decision

**Research Stopped Because**

The runner reached the maximum research iteration budget.

**Stop Reason:** max_iterations

**Searches Performed:** 10

**Unique Sources:** 35

**Remaining Uncertainty**

- Controlled matched comparisons of synthetic-only, natural-only, additive mixed, and recursive regimes across LLM pretraining, continued pretraining, supervised fine-tuning, and preference optimization.
- Disaggregated demographic, cultural, multilingual, and intersectional measurements of fairness after synthetic-text training or fine-tuning.
- Effect sizes and replication evidence for factuality, hallucination, calibration, novelty, linguistic diversity, rare-case coverage, and adversarial robustness.
- Measurements of benchmark overlap, paraphrased contamination, and score inflation specifically attributable to synthetic training or evaluation pipelines.
- Validation of synthetic evaluation results against independent human or expert judgments, temporally separated tests, adversarial tests, and deployment-like outcomes.
- Independent validation of model-based filters and judges when generation, filtering, and evaluation involve related model families.
- Comprehensive evidence on privacy, memorization, membership inference, re-identification, provenance, consent, copyright, and licensing.
- Matched total-cost analyses including generation, compute, filtering, human review, maintenance, and natural-data collection.
- Generalization of reported source-diversity, domain-specific synthesis, and budget-sensitive strategy findings across models, languages, domains, and mixture ratios.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Prior-Knowledge Planning | 1 | 22.81s |
| Tavily Search | 10 | 24.21s |
| OpenAI Analysis | 10 | 212.88s |
| Report Generation | 1 | 25.34s |
| Total Run | — | 285.25s |
