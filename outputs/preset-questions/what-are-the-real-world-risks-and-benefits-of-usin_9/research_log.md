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

**Unique Sources:** 21

**OpenAI Calls:** 11

**Tavily Calls:** 10

**Started:** 2026-09-01T04:18:48-04:00

**Ended:** 2026-09-01T04:22:07-04:00

**Total Runtime:** 198.39s

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

- **S1 — Using Synthetic Data to Improve LLM Fine‑Tuning | newline**
  URL: https://www.newline.co/@Dipen/using-synthetic-data-to-improve-llm-finetuning--d453f658
- **S2 — Synthetic Data for AI Training: Use Cases and Risks [2026]**
  URL: https://atlan.com/know/ai-agent/data-for-ai/synthetic-data-for-ai-training
- **S3 — Large Language Models Are Still Getting Stronger, but Researchers Face New Bottlenecks in Data, Evaluation, and Safety | Newswise**
  URL: https://www.newswise.com/articles/large-language-models-are-still-getting-stronger-but-researchers-face-new-bottlenecks-in-data-evaluation-and-safety
- **S4 — Synthetic Eggs in Many Baskets:The Impact of Synthetic Data Diversity on LLM Fine-Tuning**
  URL: https://arxiv.org/html/2511.01490v1
- **S5 — Synthetic Data for ML: Uses, Risks, and Best Practices | CleverX Blog**
  URL: https://cleverx.com/blog/synthetic-data-for-ml-the-game-changer-in-training-for-2025

**Search Duration:** 3.21s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data can provide practical benefits when real-world data is scarce, expensive to label, privacy-sensitive, or missing rare/edge cases.

**Confidence:** Medium

**Why this confidence level**

The benefit is consistently described by two sources, but the supporting material is primarily industry guidance rather than controlled LLM-specific evidence.

**Evidence**

- Synthetic data is described as a way to address data scarcity, privacy constraints, class imbalance, and annotation cost; it can also generate uncommon scenarios that are difficult to observe in real-world data. [S2] [S5]

#### Finding 2

**Claim**

Synthetic data can improve fine-tuning outcomes on targeted tasks, but its usefulness depends on data quality, novelty, and verification.

**Confidence:** Medium

**Why this confidence level**

The sources support task-specific utility and identify relevant quality conditions, but they do not provide broad, independently replicated effect sizes.

**Evidence**

- Synthetic data can expand resources such as reasoning traces, code examples, question-answer pairs, and task-specific data, potentially improving performance on specific tasks. [S3] [S4]
- The LLM review identifies novelty, reliability, verifiability, and sustainability as central requirements for synthetic training data rather than simply generating more data. [S3]

#### Finding 3

**Claim**

Repeated or poorly controlled training on model-generated data can narrow the model's output distribution and reduce linguistic diversity, creating model-collapse risks.

**Confidence:** High

**Why this confidence level**

The arXiv study gives direct experimental findings and aligns with the governance-oriented source's warning about recursive training.

**Evidence**

- Recursive synthetic-data training is reported to narrow distributions and degrade outputs; the cited paper describes reductions in lexical, semantic, and especially syntactic diversity and reduced ability to model human text. [S2] [S4]

#### Finding 4

**Claim**

Using multiple, diverse synthetic-data sources can mitigate distribution collapse relative to relying on a single source model.

**Confidence:** Medium

**Why this confidence level**

This is direct evidence from one empirical study; its generality across models, datasets, and generation methods remains uncertain.

**Evidence**

- The study reports that greater source diversity preserves breadth of the output distribution and text diversity, while single-source synthetic fine-tuning performs worse on this dimension. [S4]

#### Finding 5

**Claim**

Synthetic data can reproduce or amplify bias, and synthetic-data fine-tuning can create safety and evaluation risks rather than automatically improving fairness.

**Confidence:** Medium

**Why this confidence level**

The sources identify several concrete risks, including demographic bias, weakened safeguards, adversarial vulnerability, and judge self-preference, but evidence for demographic bias in LLM synthetic data is not directly measured in the supplied material.

**Evidence**

- Synthetic generators may reproduce or exaggerate existing biases or underrepresent demographics, affecting fairness and generalizability. [S5]
- The empirical study finds that fine-tuning on synthetic data decreases adversarial robustness while preserving higher output quality, making outputs potentially more usable and dangerous; fine-tuning also affects self-preference bias, with human data performing best and single-source synthetic data worst. [S4]

#### Finding 6

**Claim**

Benchmark scores alone are insufficient to establish that synthetic-data-trained models are reliable in deployment.

**Confidence:** High

**Why this confidence level**

Two sources independently emphasize validation against real-world evidence and limitations of narrow benchmark evaluation, with S3 providing an LLM-specific lifecycle perspective.

**Evidence**

- The review warns that benchmarks may be saturated or contaminated and that strong standard scores may not predict reliability on complex real-world tasks; evaluation should cover robustness, safety, fairness, reproducibility, and realistic multi-step behavior. [S3]
- Synthetic datasets should be compared with trusted real-world data using automated, statistical, visualization, and human evaluation methods, including measures of accuracy, diversity, and realism. [S5]

#### Finding 7

**Claim**

A responsible evaluation regime should combine synthetic-data checks with downstream model testing on held-out human or real-world data, including quality, diversity, bias, robustness, safety, contamination, and judge-bias checks.

**Confidence:** Medium

**Why this confidence level**

This is a synthesis of recommendations and findings across the sources; the sources do not establish one universally validated evaluation protocol.

**Evidence**

- The supplied sources collectively recommend checking fidelity/realism, diversity, representativeness, human quality, real-world generalization, adversarial robustness, safeguards, contamination, and self-preference bias. [S3] [S4] [S5]

### Conflicts Found

- Synthetic data is presented both as a way to improve diversity and coverage and as a source of distribution narrowing. These claims are conditional: diverse, externally checked synthetic sources may mitigate collapse, whereas recursive or single-source generation can worsen it. [S2] [S4] [S5]
- Synthetic fine-tuning may preserve higher output quality while reducing adversarial robustness, so apparent quality gains can coexist with greater safety risk. [S4]
- Industry sources frame synthetic data as broadly beneficial for fairness and coverage, while the empirical LLM study reports risks involving safeguards, adversarial robustness, and self-preference bias. The sources do not directly resolve whether synthetic data improves demographic fairness in LLMs. [S4] [S5]

### Important Gaps

- How large are the quality and generalization gains from synthetic data compared with equivalent amounts of human-curated data across different LLM sizes and domains?
- Which specific generation, filtering, and mixing strategies reliably prevent demographic bias amplification and representation gaps?
- How much human or independently sourced data is needed to prevent distribution collapse during repeated synthetic-data training?
- Do the reported adversarial-robustness and self-preference effects replicate across more models, tasks, languages, and deployment settings?
- What privacy leakage risks remain when synthetic data is generated from sensitive source data, and how should privacy be measured alongside utility?
- The supplied sources provide recommendations for evaluation but no comprehensive empirical comparison of evaluation protocols or deployment outcomes.

**Analysis Duration:** 16.36s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The central trade-offs can be described responsibly, but important parts of the question—especially demographic bias, privacy, comparative real-world generalization, and replication of safety effects—remain weakly evidenced. A focused search for empirical studies would materially improve the answer.

**Next Search**

> empirical study synthetic data LLM fine-tuning bias fairness privacy real-world evaluation human data model collapse

---

# Iteration 2

## 1. Search

**Query**

> empirical study synthetic data LLM fine-tuning bias fairness privacy real-world evaluation human data model collapse

**Why this query**

The central trade-offs can be described responsibly, but important parts of the question—especially demographic bias, privacy, comparative real-world generalization, and replication of safety effects—remain weakly evidenced. A focused search for empirical studies would materially improve the answer.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S6 — Synthetic Data Generation with LLMs: Techniques and Use ...**
  URL: https://tetrate.io/learn/ai/synthetic-data-generation-llms
- **S7 — Synthetic Data for LLM Training: Decision Guide 2026**
  URL: https://www.digitalapplied.com/blog/synthetic-data-generation-llm-training-decision-guide-2026
- **S8 — On LLMs-Driven Synthetic Data Generation, Curation, and Evaluation: A Survey | alphaXiv**
  URL: https://www.alphaxiv.org/abs/2406.15126
- **S9 — What Is LLM Synthetic Data? Benefits & Key Uses**
  URL: https://deepchecks.com/question/llm-synthetic-data-use-cases

**Search Duration:** 2.87s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data can reduce data-collection costs and expand coverage when human data is scarce, expensive, privacy-sensitive, or deficient in rare and underrepresented cases.

**Confidence:** Medium

**Why this confidence level**

The benefit is consistently reported, but the new sources are primarily practitioner or industry guidance and do not establish uniform gains across LLMs.

**Evidence**

- LLM-generated data is presented as useful for augmentation, class balancing, niche domains, edge cases, rapid prototyping, and privacy-constrained settings. [S6] [S9]
- Prior sources similarly identify scarcity, annotation cost, privacy constraints, and rare scenarios as practical motivations. [S2] [S5]

#### Finding 2

**Claim**

Synthetic data is most useful when it is curated and aligned with the target task; increasing volume alone does not ensure better data quality or downstream performance.

**Confidence:** High

**Why this confidence level**

Multiple sources converge on the need for curation and verification, although the precise methods and thresholds are not universally validated.

**Evidence**

- The survey separates generation, curation, and evaluation, and reports that initial synthetic samples may contain noise, inconsistency, or irrelevant content. It describes filtering, re-weighting, consistency checks, and multi-step generation as quality controls. [S8]
- The survey and prior review emphasize novelty, reliability, verifiability, realism, diversity, and task alignment as requirements for useful synthetic training data. [S3] [S8]
- The practitioner guide contrasts curated synthetic data with indiscriminate generation and frames curation discipline—not merely token volume—as central to successful examples. [S7]

#### Finding 3

**Claim**

Replacing human or real-world data with recursively generated synthetic data can cause model collapse, narrowing the distribution and reducing linguistic diversity.

**Confidence:** High

**Why this confidence level**

The finding is supported by the prior empirical study and a source discussing the peer-reviewed collapse literature; the core risk is consistent even though the guide is secondary.

**Evidence**

- Prior empirical evidence reports reduced lexical, semantic, and syntactic diversity and poorer modeling of human text under recursive synthetic-data training. [S2] [S4]
- The guide summarizes reported degradation under purely synthetic self-training and characterizes collapse as loss of low-probability but valid outputs from the data distribution. [S7]

#### Finding 4

**Claim**

Keeping real data in the training mixture and using diverse, independently sourced synthetic data may reduce—but does not eliminate—distribution-collapse risk.

**Confidence:** Medium

**Why this confidence level**

The mitigation pattern is supported by an empirical study and a secondary summary of analytical work, but the amount of real data required and generality across training regimes remain unresolved.

**Evidence**

- The guide reports an analytical result distinguishing replacement of real data from accumulating synthetic data alongside real data, with bounded error in the additive regime as described by the cited work. [S7]
- The prior empirical study finds that multiple diverse source models preserve more distributional and textual breadth than single-source synthetic fine-tuning. [S4]

#### Finding 5

**Claim**

Synthetic data can reproduce or amplify bias rather than automatically improving fairness; deliberately balancing or conditioning generations is not sufficient evidence that demographic fairness has improved.

**Confidence:** Medium

**Why this confidence level**

The conditional nature of the claim is well supported, but the supplied material does not provide a broad, direct measurement of demographic fairness improvements or harms.

**Evidence**

- Industry guidance claims synthetic data can improve representation and reduce bias through controlled generation, while also acknowledging the need for diverse, high-quality data. [S6] [S9]
- Prior sources warn that generators can reproduce or exaggerate source biases or underrepresent demographic groups, and the empirical study reports safety, adversarial-robustness, and self-preference risks after synthetic fine-tuning. [S4] [S5]

#### Finding 6

**Claim**

Synthetic data can make apparent model quality or benchmark performance improve while leaving important deployment risks undetected or worsened.

**Confidence:** High

**Why this confidence level**

The sources provide both a concrete quality-versus-robustness tradeoff and broader evidence that narrow benchmark scores are insufficient.

**Evidence**

- The empirical study reports higher output quality alongside reduced adversarial robustness, meaning more usable outputs can coexist with weaker safeguards. [S4]
- Prior review evidence warns that benchmark saturation or contamination can make standard scores poor proxies for real-world reliability. [S3]
- The survey recommends evaluating the synthetic data itself and its downstream effects through a generation–curation–evaluation feedback loop rather than treating generation as sufficient. [S8]

#### Finding 7

**Claim**

Evaluation should include synthetic-data quality checks and downstream testing on held-out human or real-world data, covering fidelity, diversity, representativeness, bias, contamination, robustness, safety, and evaluator or judge bias.

**Confidence:** High

**Why this confidence level**

The recommended evaluation dimensions are consistent across the sources, even though no single universally validated protocol is established.

**Evidence**

- The survey organizes evaluation as a distinct lifecycle stage and describes curation and evaluation as iterative processes. [S8]
- Prior sources recommend comparing synthetic data with trusted real-world data using statistical, automated, visualization, and human measures, then testing realistic generalization and safety. [S3] [S5]
- The empirical study supplies concrete reasons to include adversarial robustness and self-preference checks, not just accuracy or output quality. [S4]

### Conflicts Found

- S6 and S9 present synthetic data as capable of improving diversity, robustness, privacy, and fairness, whereas S4 and S5 document risks of bias amplification, weakened adversarial robustness, and self-preference. These are conditional rather than necessarily irreconcilable: controlled, validated augmentation may help, while unverified or recursive generation can worsen outcomes. [S4] [S5] [S6] [S9]
- S7 frames additive use of synthetic data alongside retained real data as a practical way to avoid collapse, while prior evidence emphasizes that source diversity and generation regime also matter. Retaining real data alone may therefore be insufficient if synthetic sources remain narrow or biased. [S4] [S7]
- S6 and S9 imply that synthetic data can remove privacy risk, but prior research state identifies privacy leakage and re-identification as unresolved. Synthetic generation from sensitive data should therefore be treated as potentially privacy-reducing, not automatically privacy-safe. [S5] [S6] [S9]

### Important Gaps

- What quality and generalization gains result from synthetic data versus an equivalent amount of human-curated data across model sizes, languages, and domains?
- Which generation, filtering, deduplication, and real/synthetic mixing strategies reliably prevent demographic bias amplification and representation gaps?
- How much real or independently sourced data is needed to prevent collapse under repeated synthetic-data training?
- Do adversarial-robustness and self-preference effects replicate across more models, tasks, languages, and deployment settings?
- What privacy leakage or re-identification risk remains when LLM-generated data is derived from sensitive source data, and what privacy tests should be required?
- Which evaluation protocols best predict real-world deployment reliability, rather than only benchmark performance?

**Analysis Duration:** 19.57s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources reinforce the main conclusions about benefits, curation, collapse, conditional fairness, and evaluation, but they do not materially resolve the key empirical gaps. The supplied evidence is sufficient for a responsible answer if it clearly distinguishes practical potential from demonstrated, generalizable effects and treats privacy and fairness claims cautiously.

**Next Search**

> What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation. additional evidence search 3

---

# Iteration 3

## 1. Search

**Query**

> What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation. additional evidence search 3

**Why this query**

The new sources reinforce the main conclusions about benefits, curation, collapse, conditional fairness, and evaluation, but they do not materially resolve the key empirical gaps. The supplied evidence is sufficient for a responsible answer if it clearly distinguishes practical potential from demonstrated, generalizable effects and treats privacy and fairness claims cautiously.

**Results**

5 results retrieved.

1 new unique source added.

### Sources

- **S10 — [D] Is Synthetic Data a Reliable Option for Training ...**
  URL: https://www.reddit.com/r/MachineLearning/comments/1bosj2t/d_is_synthetic_data_a_reliable_option_for

**Search Duration:** 3.48s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data alone is not generally reliable for LLM training when the generated language cannot be rigorously validated against real-world usage; retaining and testing against human data remains important.

**Confidence:** Medium

**Why this confidence level**

The new evidence is an informal discussion rather than a controlled study, but its core distinction—synthetic data is safer when outputs are independently verifiable—aligns with the stronger prior evidence on verification and real-world evaluation.

**Evidence**

- A discussion contrasts domains with automatically checkable rules, such as games, with natural language, where an LLM-generated text evaluator may reproduce the generator's inaccuracies and biases. Participants characterize synthetic-only training as generally insufficient except for narrow, highly specific settings. [S10]
- Prior sources likewise recommend retaining real-world evidence and evaluating downstream generalization on held-out human or real-world data. [S3] [S5] [S7]

#### Finding 2

**Claim**

Synthetic data is especially valuable when generation outcomes can be checked with an external, reliable validation mechanism; this condition is substantially harder to satisfy for open-ended natural-language behavior than for narrowly specified tasks.

**Confidence:** Medium

**Why this confidence level**

The source provides an illustrative argument rather than systematic comparative evidence across task types; the broader requirement for verification is supported by prior reviews.

**Evidence**

- Commenters use rule-governed games as an example where generated trajectories can be validated automatically, while arguing that natural-language correctness is only approximately captured by an LLM and may contain bias or inaccuracies. [S10]
- The review and survey identify verifiability, reliability, task alignment, and curation as central requirements for useful synthetic training data. [S3] [S8]

### Conflicts Found

- S10 includes an informal rule of thumb that synthetic data alone is generally insufficient, while the discussion also notes narrow cases where synthetic-only training may work and prior findings identify meaningful task-specific benefits. The disagreement is conditional: synthetic-only approaches may be viable when the task has a reliable simulator or validator, but are less trustworthy for open-ended language without independent human or real-world checks. [S10] [S3] [S4] [S8]

### Important Gaps

- How much independently validated human data is required for open-ended LLM fine-tuning, relative to synthetic data, to preserve real-world generalization?
- Which automated validators or task-specific verifiers are sufficiently independent from the generating model to detect its errors and biases?
- Do the proposed advantages of synthetic-only or predominantly synthetic training replicate beyond narrowly specified, automatically verifiable tasks?

**Analysis Duration:** 10.37s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new source is low-quality anecdotal discussion and does not materially resolve the major evidence gaps already identified. The accumulated evidence is sufficient to answer the original question responsibly at a conditional level: synthetic data can improve coverage, cost, and targeted performance, but quality, bias, collapse, robustness, and evaluation risks require curation, source diversity, retained real-world data, and deployment-oriented testing. Further research would be useful for quantitative comparisons and privacy or demographic-fairness measurement, but another broad search is not necessary for the current answer.

**Next Search**

> What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation. additional evidence search 4

---

# Iteration 4

## 1. Search

**Query**

> What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation. additional evidence search 4

**Why this query**

The new source is low-quality anecdotal discussion and does not materially resolve the major evidence gaps already identified. The accumulated evidence is sufficient to answer the original question responsibly at a conditional level: synthetic data can improve coverage, cost, and targeted performance, but quality, bias, collapse, robustness, and evaluation risks require curation, source diversity, retained real-world data, and deployment-oriented testing. Further research would be useful for quantitative comparisons and privacy or demographic-fairness measurement, but another broad search is not necessary for the current answer.

**Results**

5 results retrieved.

1 new unique source added.

### Sources

- **S11 — LLM synthetic data: Fine-tuning LLMs with AI-generated data | SuperAnnotate**
  URL: https://www.superannotate.com/blog/llm-synthetic-data

**Search Duration:** 2.49s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data offers scalability and lower collection costs, but its practical value depends on preserving real-world linguistic nuance and task relevance.

**Confidence:** Medium

**Why this confidence level**

The source directly discusses the tradeoff, but it is practitioner guidance rather than controlled comparative evidence.

**Evidence**

- S11 describes synthetic data as rapidly scalable and less costly than collecting human data, while noting that human data better captures idioms, emotional detail, cultural references, and expert judgment. [S11]
- S11 warns that poorly constructed synthetic data may not reflect real-world complexity and can overfit models to artificial scenarios, reducing performance on real-world data. [S11]

#### Finding 2

**Claim**

Combining synthetic data with human data is presented as safer than relying exclusively on synthetic data because human data can supply authenticity, nuance, and quality control.

**Confidence:** Medium

**Why this confidence level**

The recommendation is consistent across sources, but S11 does not provide quantitative evidence about the optimal mixture or prove that blending always outperforms alternatives.

**Evidence**

- S11 recommends blending synthetic and human-generated data so synthetic data supplies scale and coverage while human data helps preserve realism and relevance. [S11]
- This aligns with prior findings that retaining real data and testing against held-out human or real-world data can reduce, but not eliminate, distributional and generalization risks. [S3] [S4] [S7] [S10]

#### Finding 3

**Claim**

Synthetic data can amplify biases inherited from its source data, although deliberate construction may improve representation; neither outcome should be assumed without demographic and downstream fairness evaluation.

**Confidence:** Medium

**Why this confidence level**

The conditional risk-benefit pattern is consistent, but the new source offers no direct fairness measurements or experimental comparisons.

**Evidence**

- S11 states that synthetic data may counteract imbalances when deliberately designed, but also warns that biases in the original human data can be magnified in generated data. [S11]
- Prior sources similarly identify bias reproduction or amplification and note that the supplied evidence does not establish broad demographic fairness gains from synthetic-data fine-tuning. [S4] [S5] [S6] [S9]

#### Finding 4

**Claim**

The claim that synthetic data is privacy-safe is too strong: it may reduce exposure to directly identifying human records, but privacy risk depends on how it is generated and validated.

**Confidence:** Medium

**Why this confidence level**

S11 supports a potential privacy benefit, but the broader state contains an unresolved privacy gap and no direct privacy-risk measurements.

**Evidence**

- S11 presents synthetic data as avoiding real personal information and reducing privacy concerns, particularly in sensitive domains. [S11]
- Prior research state explicitly identifies privacy leakage and re-identification as unresolved questions and warns against treating synthetic data as automatically privacy-safe. [S5] [S6] [S9]

#### Finding 5

**Claim**

Model-in-the-loop evaluation may help curate synthetic data, but an evaluator derived from or similar to the generating model may fail to detect shared errors or biases; independent human or real-world checks remain necessary.

**Confidence:** Medium

**Why this confidence level**

The source supports model-in-the-loop curation, while prior evidence establishes the limitation of relying only on model-based evaluation; no source demonstrates that S11's proposed feedback loop is independently reliable.

**Evidence**

- S11 recommends continuous model-in-the-loop evaluation to keep generated data relevant and effective. [S11]
- Prior sources warn that synthetic language requires independent verification, and recommend human evaluation, comparison with trusted real-world data, and checks for evaluator self-preference bias. [S3] [S4] [S5] [S8] [S10]

### Conflicts Found

- S11 characterizes synthetic data as privacy-protective because it contains no real personal information, while the accumulated research state treats privacy leakage and re-identification as unresolved. The appropriate conclusion is conditional: synthetic data can reduce direct data exposure but is not automatically private. [S11] [S5] [S6] [S9]
- S11 recommends a synthetic-plus-human mixture and model-in-the-loop process, whereas prior evidence indicates that model-in-the-loop or benchmark evaluation can share generator biases and miss adversarial or real-world failures. These approaches are complementary only if supplemented by independent human, held-out real-world, and safety testing. [S11] [S3] [S4] [S5] [S10]

### Important Gaps

- Does blending synthetic and human data produce consistent gains over equivalent human-only or synthetic-only datasets across LLM sizes, languages, and domains?
- What independent validation methods can reliably detect shared errors when both generation and evaluation use language models?
- How much synthetic data can be added before overfitting to artificial scenarios or distribution narrowing harms real-world generalization?
- What privacy leakage and re-identification tests are needed for synthetic data generated from sensitive source material?

**Analysis Duration:** 13.34s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

S11 largely corroborates the accumulated findings: synthetic data provides scale, cost, and potential privacy or coverage benefits, but can lose human nuance, overfit, amplify bias, and require human-data validation. It adds no strong empirical evidence resolving the major outstanding gaps, so another broad search is unlikely to materially improve the current answer without a more targeted empirical study.

**Next Search**

> What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation. additional evidence search 5

---

# Iteration 5

## 1. Search

**Query**

> What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation. additional evidence search 5

**Why this query**

S11 largely corroborates the accumulated findings: synthetic data provides scale, cost, and potential privacy or coverage benefits, but can lose human nuance, overfit, amplify bias, and require human-data validation. It adds no strong empirical evidence resolving the major outstanding gaps, so another broad search is unlikely to materially improve the current answer without a more targeted empirical study.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S12 — How to Generate Synthetic Data and Fine-Tune a Small Language ...**
  URL: https://blog.monsterapi.ai/how-to-generate-synthetic-data-and-fine-tune-a-small-language-model-slm-on-monsterapi
- **S13 — The Dangers and Risks of Depending on Synthetic Data from Large Language Models**
  URL: https://www.linkedin.com/pulse/dangers-risks-depending-synthetic-data-from-large-language-jdihf
- **S14 — This AI Paper from Meta AI Highlights the Risks of Using Synthetic Data to Train Large Language Models - MarkTechPost**
  URL: https://www.marktechpost.com/2024/10/16/this-ai-paper-from-meta-ai-highlights-the-risks-of-using-synthetic-data-to-train-large-language-models?amp=
- **S15 — This AI Paper from Meta AI Highlights the Risks of Using Synthetic Data to Train Large Language Models - MarkTechPost**
  URL: https://www.marktechpost.com/2024/10/16/this-ai-paper-from-meta-ai-highlights-the-risks-of-using-synthetic-data-to-train-large-language-models
- **S16 — Synthetic Data Generation Using Large Language Models: Advances in Text and Code (2025) – MECO**
  URL: https://www.cs.ubbcluj.ro/~meco/synthetic-data-generation-using-large-language-models-advances-in-text-and-code-2025

**Search Duration:** 4.73s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data can reduce the cost and time of creating task-specific fine-tuning data and can expand coverage when labeled human data is scarce, expensive, or sensitive.

**Confidence:** Medium

**Why this confidence level**

The benefit is consistent with the accumulated evidence, but S12 is vendor guidance and S16 is a survey rather than a controlled comparison with human-curated data.

**Evidence**

- Synthetic-data generation is presented as scalable for instruction, reasoning, summarization, coding, classification, and other task-specific examples, especially where real-world data is limited or costly. [S12] [S16]

#### Finding 2

**Claim**

Synthetic data does not automatically have high quality: factual errors, inconsistency, domain mismatch, and insufficient realism can reduce downstream performance.

**Confidence:** High

**Why this confidence level**

Multiple sources converge on concrete quality failure modes and the need for curation and validation.

**Evidence**

- The survey identifies factual inaccuracies and insufficient stylistic or distributional realism; the practical guide warns that domain mismatch can harm performance without validation. [S12] [S16]
- The accumulated survey evidence likewise reports noise, irrelevant content, and the need for filtering, consistency checks, and task alignment. [S8]

#### Finding 3

**Claim**

Synthetic data can reproduce or amplify biases in its source data or generating model, although deliberate construction may improve representation; fairness benefits must be demonstrated empirically rather than assumed.

**Confidence:** High

**Why this confidence level**

The conditional risk is consistently supported, while direct evidence of demographic fairness improvement remains limited.

**Evidence**

- The new sources warn that bias or inconsistencies in the original data or generation model are likely to appear in the synthetic output, while the survey identifies bias amplification as a central challenge. [S12] [S16]
- Prior evidence reports possible demographic underrepresentation and synthetic-fine-tuning effects involving self-preference and safety, without establishing broad demographic fairness gains. [S4] [S5]

#### Finding 4

**Claim**

Synthetic data can create distributional and generalization risks, including overfitting to artificial scenarios, loss of real-world linguistic nuance, and model collapse under some training regimes.

**Confidence:** High

**Why this confidence level**

The core collapse and generalization risks are supported by prior empirical findings and additional reporting, although the new reporting sources are secondary.

**Evidence**

- The new sources warn that synthetic data may lack real-world complexity and variability, become outdated as behavior changes, and cause models to perform well in controlled settings but fail in real-world scenarios. [S13]
- The reported Meta/NYU/UCLA analysis is summarized as finding deterioration when synthetic data is introduced, including in language-model experiments, with larger models more susceptible under the tested conditions. [S14] [S15]
- Prior empirical evidence reports reduced lexical, semantic, and syntactic diversity under recursive synthetic-data training. [S2] [S4]

#### Finding 5

**Claim**

The exact amount of synthetic data that is safe is not established; claims that even 1% causes collapse should be treated as condition-specific rather than a universal threshold.

**Confidence:** Medium

**Why this confidence level**

The sources suggest an important risk but do not provide the primary study here, and the reported threshold may depend heavily on model, data, and training regime.

**Evidence**

- S14 and S15 report collapse with as little as 1% synthetic data in particular experiments and datasets. [S14] [S15]
- Other accumulated evidence indicates that retaining real data, using diverse sources, and avoiding recursive or single-source generation may reduce collapse, but does not establish a universal safe proportion. [S4] [S7]

#### Finding 6

**Claim**

Synthetic data may expose organizations to privacy, intellectual-property, or provenance risks; synthetic status alone does not establish that data is private or legally unproblematic.

**Confidence:** Medium

**Why this confidence level**

The risk is plausible and consistent with the accumulated state, but the new example is an unsourced practitioner account and does not establish frequency or legal liability.

**Evidence**

- S13 reports a case in which synthetic data allegedly closely mirrored proprietary competitor content, alongside broader warnings about legal challenges. [S13]
- Prior evidence identifies privacy leakage and re-identification as unresolved and rejects treating synthetic data as automatically privacy-safe. [S5] [S6] [S9] [S11]

#### Finding 7

**Claim**

Evaluation should test both the synthetic dataset and the downstream model against independent, held-out human or real-world evidence; benchmark scores alone are inadequate.

**Confidence:** High

**Why this confidence level**

Evaluation requirements are consistent across the sources, including concrete evidence that output quality can improve while adversarial robustness worsens.

**Evidence**

- The new survey recommends filtering, weighting, automated verification, and robust evaluation, including execution feedback for code where functional correctness is independently checkable. [S16]
- Prior sources recommend checking fidelity, diversity, representativeness, bias, contamination, adversarial robustness, safety, self-preference, and realistic multi-step generalization against trusted real-world data. [S3] [S4] [S5] [S8]

#### Finding 8

**Claim**

External verification makes synthetic data more trustworthy for narrowly specified tasks than for open-ended natural-language behavior.

**Confidence:** Medium

**Why this confidence level**

The distinction is well motivated and supported by reviews and discussion, but comparative evidence across task types is limited.

**Evidence**

- The survey highlights automated verification of functional correctness in code and execution feedback as a mitigation, while identifying factual inaccuracies and realism problems in generated text. [S16]
- Prior discussion distinguishes automatically checkable tasks from open-ended language, where model-based evaluators may share generator errors and biases. [S10] [S3] [S8]

### Conflicts Found

- S14/S15 report substantial collapse from even a small synthetic fraction, whereas S7 and S4 indicate that additive mixtures retaining real data and using diverse sources may mitigate collapse. These findings may reflect different datasets, model sizes, source diversity, and training procedures; the evidence does not support a universal 1% threshold or guarantee that real-data mixing is sufficient. [S14] [S15] [S4] [S7]
- S12 presents synthetic generation as providing control over quality and diversity, but the same source acknowledges domain mismatch and inherited bias; S16 likewise documents factual inaccuracies and insufficient realism. Control is therefore a capability, not an outcome guaranteed by generation. [S12] [S16]
- S13 emphasizes static data, real-world drift, and failures outside controlled environments, while other sources emphasize scalability and broad coverage. The benefits apply to data creation and task coverage, but do not remove the need for refreshed real-world evaluation. [S12] [S13] [S16]

### Important Gaps

- How much synthetic data can be used safely across different LLM sizes, domains, languages, and generation regimes?
- Does the reported 1% collapse result replicate in primary, LLM-specific experiments beyond the summarized datasets and conditions?
- Which generation, filtering, deduplication, and real/synthetic mixing strategies reliably prevent bias amplification and distribution narrowing?
- How much human or independently sourced data is needed to preserve real-world linguistic nuance and generalization?
- What independent tests best detect privacy leakage, memorization, provenance problems, and intellectual-property overlap in generated data?
- Which evaluation protocols best predict deployment reliability rather than benchmark performance, especially when generation and evaluation models share biases?

**Analysis Duration:** 18.01s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources reinforce the existing conclusions about scalability, quality failure modes, bias, collapse, and the need for independent evaluation. They are mostly practitioner, survey, or secondary reporting sources and do not resolve the central quantitative gaps; another broad search is unlikely to materially improve the current responsible answer without targeting primary experimental studies.

**Next Search**

> What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation. additional evidence search 6

---

# Iteration 6

## 1. Search

**Query**

> What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation. additional evidence search 6

**Why this query**

The new sources reinforce the existing conclusions about scalability, quality failure modes, bias, collapse, and the need for independent evaluation. They are mostly practitioner, survey, or secondary reporting sources and do not resolve the central quantitative gaps; another broad search is unlikely to materially improve the current responsible answer without targeting primary experimental studies.

**Results**

5 results retrieved.

0 new unique sources added.

### Sources

No new unique sources were added.

**Search Duration:** 2.69s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data can reduce the cost and time of creating task-specific training data and expand coverage when human data is scarce, expensive, privacy-sensitive, or lacking rare cases.

**Confidence:** Medium

**Why this confidence level**

The benefit is consistently reported, but much of the evidence is survey, practitioner, or industry guidance rather than independently replicated LLM experiments.

**Evidence**

- Sources describe synthetic data as useful for augmentation, class balancing, niche domains, edge cases, rapid prototyping, and privacy-constrained settings. [S2] [S5] [S6] [S9] [S12] [S16]

#### Finding 2

**Claim**

Synthetic data improves downstream performance only conditionally: quality, task alignment, novelty, realism, and external verifiability matter more than volume alone.

**Confidence:** High

**Why this confidence level**

Multiple sources converge on the need for curation and verification, although no universal quality threshold or protocol is established.

**Evidence**

- Sources identify factual errors, inconsistency, irrelevant content, domain mismatch, insufficient realism, and lack of novelty as failure modes; they recommend filtering, reweighting, consistency checks, curation, and verification. [S3] [S8] [S12] [S16]
- Synthetic data is more trustworthy for narrowly specified tasks with reliable validators, such as executable code, than for open-ended natural-language behavior. [S10] [S16]

#### Finding 3

**Claim**

Recursive, single-source, or predominantly synthetic training can narrow the learned distribution, reduce linguistic diversity, and harm generalization to human text; retaining real data and using diverse sources may mitigate but not eliminate this risk.

**Confidence:** High

**Why this confidence level**

The core collapse risk is supported by empirical evidence, but the amount of synthetic data that is safe depends on model, data, source diversity, and training regime.

**Evidence**

- Empirical evidence reports reductions in lexical, semantic, and syntactic diversity and poorer modeling of human text under recursive synthetic-data training. [S2] [S4]
- Multiple and diverse source models preserve more distributional and textual breadth than single-source synthetic fine-tuning, while additive mixtures retaining real data may be safer than replacing real data. [S4] [S7]
- Reports of collapse with a small synthetic fraction occur under particular experimental conditions and do not establish a universal safe percentage. [S14] [S15] [S4] [S7]

#### Finding 4

**Claim**

Synthetic data can reproduce or amplify bias from its source data or generator, while deliberately controlled generation may improve representation; fairness gains must therefore be demonstrated rather than assumed.

**Confidence:** Medium

**Why this confidence level**

The conditional risk-benefit pattern is consistent, but direct comparative measurements of demographic fairness are limited.

**Evidence**

- Sources warn about inherited bias, demographic underrepresentation, and bias amplification, while industry guidance presents controlled generation as a possible way to improve coverage. [S5] [S6] [S9] [S11] [S12] [S16]
- Synthetic fine-tuning has also been associated with self-preference effects and safety-related changes, although the supplied evidence does not establish broad demographic fairness outcomes. [S4]

#### Finding 5

**Claim**

Synthetic data may improve apparent output quality or benchmark performance while worsening important deployment properties such as adversarial robustness, safety, or real-world generalization.

**Confidence:** High

**Why this confidence level**

The quality-versus-robustness tradeoff is directly reported, and independent reviews consistently caution against treating benchmark gains as deployment evidence.

**Evidence**

- One empirical study reports higher output quality alongside reduced adversarial robustness after synthetic fine-tuning. [S4]
- Reviews warn that benchmark saturation or contamination can make standard scores poor proxies for real-world reliability and that synthetic data may overfit artificial scenarios or omit real-world nuance. [S3] [S11] [S13]

#### Finding 6

**Claim**

Synthetic data can reduce direct exposure to human records, but it is not automatically private or free of provenance, memorization, re-identification, or intellectual-property risks.

**Confidence:** Medium

**Why this confidence level**

The potential benefit and risk are both supported, but the supplied material lacks systematic privacy measurements or established legal conclusions.

**Evidence**

- Sources describe potential privacy benefits while also identifying leakage and re-identification as unresolved; one report raises possible proprietary-content overlap. [S5] [S6] [S9] [S11] [S13]

#### Finding 7

**Claim**

Responsible evaluation should assess both the synthetic dataset and the downstream model using independent, held-out human or real-world evidence.

**Confidence:** High

**Why this confidence level**

Evaluation requirements are consistent across the sources, including concrete evidence that output quality alone can conceal degraded robustness.

**Evidence**

- Recommended checks include fidelity, realism, diversity, representativeness, factuality, bias, contamination, robustness, safety, adversarial behavior, self-preference, and realistic multi-step generalization. [S3] [S4] [S5] [S8] [S16]
- Model-based evaluation should be supplemented with human or external checks because generators and evaluators may share errors or biases. [S4] [S5] [S8] [S10] [S11]

### Conflicts Found

- Synthetic data is described both as improving coverage and diversity and as causing distribution narrowing. The claims are conditional: curated, diverse, externally checked data may help, while recursive or single-source data can worsen collapse. [S2] [S4] [S5] [S7]
- Industry guidance presents controlled synthetic generation as potentially improving fairness, privacy, and diversity, while empirical and review evidence warns of bias amplification, weakened robustness, and self-preference. The supplied evidence does not resolve the demographic fairness question. [S4] [S5] [S6] [S9] [S11]
- Some sources recommend model-in-the-loop evaluation, but other evidence warns that model-based evaluators can share the generator's errors or biases. Such evaluation is complementary, not a substitute for independent human, external, and held-out real-world testing. [S3] [S4] [S5] [S10] [S11]
- Reports of collapse from a small synthetic fraction coexist with evidence that retaining real data and using diverse sources can mitigate collapse. These results likely reflect different datasets and training conditions and do not support a universal percentage threshold. [S4] [S7] [S14] [S15]

### Important Gaps

- How do synthetic datasets compare with equivalent amounts of human-curated data across model sizes, languages, and domains?
- What generation, filtering, deduplication, and real/synthetic mixing strategies reliably limit bias amplification and distribution narrowing?
- How much real or independently sourced data is needed to preserve linguistic diversity and real-world generalization?
- Do adversarial-robustness and self-preference effects replicate across more models, tasks, languages, and deployment settings?
- What privacy, memorization, re-identification, provenance, and intellectual-property tests should be required?
- Which evaluation protocols best predict deployment reliability rather than benchmark performance?
- Which independent validators can detect shared errors when both generation and evaluation use language models?

**Analysis Duration:** 14.78s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

No usable new sources were retrieved, and the accumulated evidence is sufficient to answer the original question responsibly at a conditional level: synthetic data offers scalability and targeted coverage, but introduces quality, bias, collapse, privacy, and evaluation risks. The remaining gaps concern effect sizes, thresholds, replication, and protocol standardization rather than the core conclusion.

**Next Search**

> What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation. additional evidence search 7

---

# Iteration 7

## 1. Search

**Query**

> What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation. additional evidence search 7

**Why this query**

No usable new sources were retrieved, and the accumulated evidence is sufficient to answer the original question responsibly at a conditional level: synthetic data offers scalability and targeted coverage, but introduces quality, bias, collapse, privacy, and evaluation risks. The remaining gaps concern effect sizes, thresholds, replication, and protocol standardization rather than the core conclusion.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S17 — Synthetic Data and the Future of AI: The 2026 Expert Guide - Riseup Labs**
  URL: https://riseuplabs.com/synthetic-data-and-the-future-of-ai
- **S18 — Examining synthetic data: The promise, risks and realities | IBM**
  URL: https://www.ibm.com/think/insights/ai-synthetic-data
- **S19 — The Prominence of Synthetic Data, and Why It Will Expand Rather Than Replace Real Data - Dataversity**
  URL: https://www.dataversity.net/articles/the-prominence-of-synthetic-data-and-why-it-will-expand-rather-than-replace-real-data
- **S20 — Synthetic Data Generation Using Large Language Models: Advances in Text and Code**
  URL: https://arxiv.org/html/2503.14023v2
- **S21 — Best Practices and Lessons Learned on Synthetic Data for Language Models**
  URL: https://arxiv.org/html/2404.07503v1

**Search Duration:** 2.98s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources reinforce that synthetic data can reduce annotation cost and expand coverage for low-resource, privacy-sensitive, or edge-case tasks, but these benefits are conditional rather than universal.

**Confidence:** Medium

**Why this confidence level**

The sources provide relevant examples and survey-level support, but most evidence is review, industry, or reported case-study material rather than independent, controlled comparisons with equal amounts of human-curated data.

**Evidence**

- The LLM survey describes synthetic text and code as useful when labeled data is scarce, expensive, or sensitive, and reports performance gains in low-data regimes; the best-practices paper similarly emphasizes scalability, controllable class balance, and targeted coverage. [S20] [S21]
- IBM reports LAB models achieving competitive benchmark performance using taxonomy-guided synthetic generation, while also describing synthetic data as a supplement to real data for specialized scenarios. [S18]

#### Finding 2

**Claim**

Synthetic-data quality depends on factuality, fidelity, realism, diversity, and task alignment; generation at scale does not guarantee useful training data.

**Confidence:** High

**Why this confidence level**

The new sources consistently corroborate the accumulated evidence on concrete quality failure modes and the need for curation and verification.

**Evidence**

- The surveys identify hallucinations, factual inaccuracies, stylistic or distributional mismatch, noise, and insufficient realism as causes of poor generalization, and recommend filtering, weighting, refinement, retrieval, or external verification. [S20] [S21]
- IBM describes fidelity testing by comparing synthetic and real data distributions and reports that synthetic-data quality is central to downstream LLM performance. [S18]

#### Finding 3

**Claim**

Synthetic data may improve controlled-task performance while failing to preserve real-world behavior, especially when the task involves open-ended language rather than independently verifiable outputs.

**Confidence:** High

**Why this confidence level**

This directly strengthens the prior conclusion that benchmark or task scores do not by themselves establish deployment reliability, although the sources do not provide a universal evaluation protocol.

**Evidence**

- The survey distinguishes code settings where execution can verify functional correctness from text settings where factuality and realism are harder to validate; the best-practices paper warns that false or biased synthetic data can impair real-world generalization. [S20] [S21]
- IBM presents benchmark-competitive LAB results but states that synthetic data is likely to supplement rather than replace real-world data. [S18]

#### Finding 4

**Claim**

Synthetic data can improve representation or controllable diversity in principle, but it can also reproduce or amplify generator and source-data bias; fairness improvements must be measured downstream.

**Confidence:** High

**Why this confidence level**

The conditional benefit-risk pattern is consistently stated across the new sources and aligns with prior findings, but direct comparative demographic fairness measurements remain limited.

**Evidence**

- The best-practices paper says synthetic generation can balance classes or up-weight low-resource languages, while also warning that generated data may amplify or introduce biases without careful design and validation. [S21]
- IBM warns that synthetic data may fail to represent population diversity and thereby produce unequal performance across demographic groups. [S18]
- The newer survey explicitly lists bias amplification as a central challenge and recommends filtering and evaluation rather than assuming controlled generation produces fairness. [S20]

#### Finding 5

**Claim**

Repeated or predominantly synthetic training remains a model-collapse and distribution-narrowing risk; retaining real data and validating synthetic data are recurring mitigation recommendations.

**Confidence:** High

**Why this confidence level**

This is consistent with the accumulated empirical evidence, though the new industry summaries do not establish a universal safe synthetic-data percentage or mixture.

**Evidence**

- IBM cites the Nature model-collapse study and describes increasingly nonsensical outputs after repeated training on AI-generated text. [S18]
- Dataversity reports that synthetic data can simplify or condense the complexity of original data and emphasizes continued synchronization with real-world data, validation, and mixed datasets. [S19]
- The LLM survey recommends blending synthetic and real data and identifies loss of diversity, factuality, and robustness as risks of iterative self-training. [S20]

#### Finding 6

**Claim**

Evaluation should separately assess the synthetic dataset and the downstream model using independent, held-out human or real-world evidence.

**Confidence:** High

**Why this confidence level**

The evaluation recommendations converge with the prior research state and address the original focus directly, although no single protocol is shown to predict deployment outcomes reliably.

**Evidence**

- Recommended dataset checks include fidelity, factuality, realism, diversity, representativeness, and bias; downstream checks should include generalization, robustness, safety, and contamination rather than only benchmark accuracy. [S20] [S21]
- IBM specifically recommends statistical comparison with real-world data and continuous testing, while noting privacy, accuracy, bias, and compliance risks. [S18]

### Conflicts Found

- The new sources present synthetic data as capable of improving fairness, diversity, privacy, and performance, while simultaneously warning about bias amplification, model collapse, privacy leakage, and poor real-world fidelity. These are conditional claims: benefits are more plausible with curated, task-aligned, externally verified, mixed data; unverified or recursive use can worsen outcomes. [S17] [S18] [S19] [S20] [S21]
- IBM reports competitive benchmark results for LAB-trained models, whereas the accumulated evidence warns that benchmark gains can coexist with reduced adversarial robustness or poor deployment generalization. The LAB results therefore do not resolve real-world reliability. [S18] [S3] [S4]
- S17 makes strong claims that synthetic data can remove identifiers, achieve safe-harbor status, and lower regulatory burden, while IBM and the prior research state caution that generation from sensitive data can still permit privacy leakage or other violations. Synthetic status alone is not evidence of privacy or legal safety. [S17] [S18] [S5] [S11]

### Important Gaps

- How do the reported LAB and other synthetic-data gains compare with equal quantities of high-quality human-curated data across models, domains, languages, and deployment tasks?
- Which independent evaluation methods best detect factual errors, shared generator/evaluator bias, demographic disparities, adversarial weaknesses, and real-world distribution shift?
- What synthetic-to-real mixture and source diversity are needed to prevent collapse and preserve linguistic diversity under different training regimes?
- Do reported benefits replicate for open-ended natural-language fine-tuning, where correctness cannot be automatically verified as it can for executable code?
- What quantitative privacy, memorization, re-identification, provenance, and intellectual-property tests should be required before synthetic data is used in sensitive applications?

**Analysis Duration:** 15.21s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources largely corroborate the accumulated findings and add no decisive evidence resolving the major gaps. The original question can be answered responsibly with conditional benefits, concrete quality and bias risks, model-collapse concerns, and an evaluation framework centered on independent real-world testing. Further searching would likely add more guidance rather than materially change those conclusions.

**Next Search**

> What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation. additional evidence search 8

---

# Iteration 8

## 1. Search

**Query**

> What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation. additional evidence search 8

**Why this query**

The new sources largely corroborate the accumulated findings and add no decisive evidence resolving the major gaps. The original question can be answered responsibly with conditional benefits, concrete quality and bias risks, model-collapse concerns, and an evaluation framework centered on independent real-world testing. Further searching would likely add more guidance rather than materially change those conclusions.

**Results**

5 results retrieved.

0 new unique sources added.

### Sources

No new unique sources were added.

**Search Duration:** 3.19s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data can reduce the cost and time of creating task-specific training data and expand coverage when human data is scarce, expensive, privacy-sensitive, or lacking rare cases.

**Confidence:** Medium

**Why this confidence level**

The benefit is consistently reported, but much of the evidence is survey, practitioner, industry, or case-study material rather than independently replicated comparisons with equivalent human-curated data.

**Evidence**

- Sources describe uses including augmentation, class balancing, niche domains, edge cases, rapid prototyping, and privacy-constrained settings. [S2] [S5] [S6] [S9] [S12] [S16] [S20] [S21]

#### Finding 2

**Claim**

Synthetic data improves model performance only conditionally; factuality, realism, diversity, novelty, task alignment, and external verifiability matter more than volume alone.

**Confidence:** High

**Why this confidence level**

Multiple sources converge on the same quality requirements and failure modes, although no universal quality threshold is established.

**Evidence**

- Sources identify hallucinations, factual errors, inconsistency, irrelevant content, domain mismatch, insufficient realism, and lack of novelty as failure modes, and recommend filtering, weighting, consistency checks, curation, and verification. [S3] [S8] [S12] [S16] [S20] [S21]
- Automatically verifiable tasks such as executable code provide stronger validation than open-ended natural-language behavior, where correctness and realism are harder to establish independently. [S10] [S16] [S20]

#### Finding 3

**Claim**

Recursive, single-source, or predominantly synthetic training can narrow the learned distribution, reduce linguistic diversity, and harm generalization to human text; retaining real data and using diverse sources may mitigate but not eliminate the risk.

**Confidence:** High

**Why this confidence level**

The core collapse risk is supported by empirical evidence, while the mitigating conditions and safe proportions remain regime-dependent.

**Evidence**

- Empirical evidence reports reductions in lexical, semantic, and syntactic diversity and poorer modeling of human text under recursive synthetic-data training. [S2] [S4]
- Diverse source models and additive mixtures retaining real data preserve more distributional breadth than single-source or replacement regimes in the reported evidence. [S4] [S7]
- Reports of collapse with a small synthetic fraction occur under particular experimental conditions and do not establish a universal safe percentage. [S14] [S15] [S4] [S7]

#### Finding 4

**Claim**

Synthetic data can reproduce or amplify bias from its source data or generator, although controlled generation may improve representation; fairness gains must be demonstrated through downstream measurement.

**Confidence:** Medium

**Why this confidence level**

The conditional risk-benefit pattern is consistent, but direct comparative measurements of demographic fairness remain limited.

**Evidence**

- Sources warn about inherited bias, demographic underrepresentation, and bias amplification while describing class balancing or targeted generation as possible benefits. [S5] [S6] [S9] [S11] [S12] [S16] [S20] [S21]
- Synthetic fine-tuning has also been associated with self-preference effects and safety-related changes, without establishing broad demographic fairness improvements. [S4]

#### Finding 5

**Claim**

Synthetic data can improve apparent output quality or benchmark performance while worsening adversarial robustness, safety, or real-world generalization.

**Confidence:** High

**Why this confidence level**

The quality-versus-robustness tradeoff is directly reported, and multiple sources caution against treating benchmark gains as deployment evidence.

**Evidence**

- One empirical study reports higher output quality alongside reduced adversarial robustness after synthetic fine-tuning. [S4]
- Reviews warn that benchmark saturation or contamination and overfitting to artificial scenarios can make standard scores poor proxies for deployment reliability. [S3] [S11] [S13] [S18]

#### Finding 6

**Claim**

Synthetic data may reduce direct exposure to human records, but synthetic status alone does not guarantee privacy, legal safety, or clean provenance.

**Confidence:** Medium

**Why this confidence level**

Both potential benefit and risk are supported, but the supplied material lacks systematic privacy measurements or established legal conclusions.

**Evidence**

- Sources describe potential privacy benefits while identifying leakage and re-identification as unresolved; one report raises possible proprietary-content overlap and provenance concerns. [S5] [S6] [S9] [S11] [S13] [S17] [S18]

#### Finding 7

**Claim**

Responsible evaluation should separately assess the synthetic dataset and the downstream model using independent, held-out human or real-world evidence.

**Confidence:** High

**Why this confidence level**

Evaluation requirements are consistent across the sources, although no single protocol is shown to reliably predict all deployment outcomes.

**Evidence**

- Dataset checks should cover fidelity, factuality, realism, diversity, representativeness, bias, contamination, and task alignment. [S3] [S5] [S8] [S16] [S20] [S21]
- Model checks should include real-world generalization, robustness, adversarial behavior, safety, contamination, evaluator self-preference, and realistic multi-step performance—not only benchmark accuracy. [S3] [S4] [S16] [S18] [S20] [S21]
- Model-based evaluation should be supplemented with human, external, or independently verifiable checks because generators and evaluators may share errors or biases. [S4] [S5] [S8] [S10] [S11]

### Conflicts Found

- Synthetic data is described both as improving diversity, representation, and coverage and as causing distribution narrowing and collapse. The evidence is conditional: curated, diverse, externally checked data may help, whereas recursive or single-source data can worsen outcomes. [S2] [S4] [S5] [S7] [S20] [S21]
- Some industry sources present synthetic data as potentially improving fairness and privacy, while empirical and review evidence warns of bias amplification, self-preference, privacy leakage, and weakened robustness. The supplied evidence does not resolve the demographic fairness question or establish automatic privacy safety. [S4] [S5] [S6] [S9] [S11] [S17] [S18]
- Benchmark-competitive or higher-quality outputs can coexist with reduced adversarial robustness or poor real-world generalization; therefore apparent quality gains do not settle deployment safety. [S3] [S4] [S11] [S13] [S18]
- Reports of collapse from a small synthetic fraction coexist with evidence that retaining real data and using diverse sources can mitigate collapse. These results likely depend on datasets, model sizes, source diversity, and training procedures and do not support a universal percentage threshold. [S4] [S7] [S14] [S15]

### Important Gaps

- How do synthetic datasets compare with equivalent amounts of human-curated data across model sizes, languages, domains, and deployment tasks?
- Which generation, filtering, deduplication, and real/synthetic mixing strategies reliably limit demographic bias amplification and distribution narrowing?
- How much real or independently sourced data is needed to preserve linguistic diversity and real-world generalization?
- Do adversarial-robustness and self-preference effects replicate across more models, tasks, languages, and deployment settings?
- What quantitative tests best detect privacy leakage, memorization, re-identification, provenance, and intellectual-property overlap?
- Which evaluation protocols best predict deployment reliability when generation and evaluation models share errors or biases?
- Do predominantly synthetic approaches work beyond narrowly specified tasks with reliable external validators, especially for open-ended natural-language fine-tuning?

**Analysis Duration:** 15.17s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

No usable new sources were retrieved, but the accumulated evidence is sufficient to answer the original question responsibly: synthetic data offers conditional scalability and coverage benefits, while quality, bias, collapse, robustness, privacy, and evaluation risks require mixed data and independent real-world testing. Further research would refine quantitative thresholds and generalizability rather than change the central conclusion.

**Next Search**

> What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation. additional evidence search 9

---

# Iteration 9

## 1. Search

**Query**

> What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation. additional evidence search 9

**Why this query**

No usable new sources were retrieved, but the accumulated evidence is sufficient to answer the original question responsibly: synthetic data offers conditional scalability and coverage benefits, while quality, bias, collapse, robustness, privacy, and evaluation risks require mixed data and independent real-world testing. Further research would refine quantitative thresholds and generalizability rather than change the central conclusion.

**Results**

5 results retrieved.

0 new unique sources added.

### Sources

No new unique sources were added.

**Search Duration:** 2.74s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data offers real operational benefits, but mainly as curated augmentation rather than an unquestioned replacement for human data.

**Confidence:** High

**Why this confidence level**

The benefit-and-condition pattern is consistent across many sources, although quantitative comparisons with equivalent human-curated data are limited.

**Evidence**

- Sources consistently describe lower collection or annotation cost, scalability, class balancing, privacy-sensitive use, niche-domain coverage, and rare or edge-case generation as benefits. [S2] [S5] [S6] [S9] [S12] [S16] [S20] [S21]
- The evidence also repeatedly says that utility depends on factuality, realism, novelty, task alignment, curation, and external verification rather than volume alone. [S3] [S8] [S10] [S16] [S20] [S21]

#### Finding 2

**Claim**

The principal data-quality risk is that synthetic examples can contain errors or artificial regularities that improve controlled-task scores while harming real-world generalization.

**Confidence:** High

**Why this confidence level**

Multiple sources converge on these quality and evaluation limitations, including one empirical study with a concrete robustness tradeoff.

**Evidence**

- Sources identify hallucinations, factual errors, inconsistency, irrelevant content, domain mismatch, insufficient realism, and loss of human linguistic nuance as concrete failure modes. [S8] [S11] [S12] [S13] [S16] [S20] [S21]
- Benchmark saturation or contamination and a reported quality-versus-adversarial-robustness tradeoff show why apparent performance gains do not establish deployment reliability. [S3] [S4] [S18]

#### Finding 3

**Claim**

Recursive, single-source, or predominantly synthetic training can narrow the learned distribution and reduce linguistic diversity; retaining real data and using diverse sources may mitigate, but does not guarantee prevention of, collapse.

**Confidence:** High

**Why this confidence level**

The core risk has direct empirical support; the safe mixture and mitigation conditions remain unresolved.

**Evidence**

- Experimental evidence reports reduced lexical, semantic, and syntactic diversity and poorer modeling of human text under recursive synthetic-data training. [S2] [S4]
- Diverse source models and additive mixtures retaining real data preserve more breadth in the reported settings, while reports of collapse from a small synthetic fraction are condition-specific and do not establish a universal threshold. [S4] [S7] [S14] [S15]

#### Finding 4

**Claim**

Synthetic data can reproduce or amplify bias from its source data or generator, while controlled generation may improve representation; fairness benefits must be demonstrated downstream.

**Confidence:** Medium

**Why this confidence level**

The conditional risk-benefit pattern is consistent, but direct comparative demographic fairness measurements are sparse.

**Evidence**

- Sources describe possible class balancing, low-resource-language support, and targeted representation, but also warn of inherited bias, demographic underrepresentation, and bias amplification. [S5] [S6] [S9] [S11] [S12] [S16] [S20] [S21]
- Synthetic fine-tuning is associated in one empirical study with self-preference and safety-related effects, without establishing broad demographic fairness gains. [S4]

#### Finding 5

**Claim**

Synthetic data may reduce direct exposure to human records, but synthetic status alone does not establish privacy, provenance, or intellectual-property safety.

**Confidence:** Medium

**Why this confidence level**

Both benefit and risk are represented, but the supplied material lacks systematic privacy measurements and definitive legal conclusions.

**Evidence**

- Sources present reduced direct exposure as a potential privacy benefit while identifying leakage, re-identification, memorization, and possible proprietary-content overlap as unresolved risks. [S5] [S6] [S9] [S11] [S13] [S17] [S18]

#### Finding 6

**Claim**

The most defensible evaluation approach tests both the synthetic dataset and the downstream model against independent, held-out human or real-world evidence.

**Confidence:** High

**Why this confidence level**

Evaluation requirements are consistent across the accumulated sources, though no single protocol is proven to predict every deployment outcome.

**Evidence**

- Dataset evaluation should cover fidelity, factuality, realism, diversity, representativeness, bias, contamination, and task alignment; downstream evaluation should cover generalization, robustness, safety, adversarial behavior, and evaluator self-preference—not only benchmark accuracy. [S3] [S4] [S5] [S8] [S16] [S18] [S20] [S21]
- Human, external, or independently verifiable checks are needed because a generator and model-based evaluator may share errors or biases; automatic validation is stronger for narrowly specified tasks such as executable code than for open-ended language. [S4] [S5] [S8] [S10] [S16] [S20]

### Conflicts Found

- Industry and practitioner sources emphasize synthetic data's potential to improve privacy, fairness, diversity, and performance, while empirical and review evidence documents bias amplification, weakened robustness, collapse, and privacy leakage. These are conditional claims, not a resolved universal benefit or harm. [S4] [S5] [S6] [S9] [S11] [S17] [S18] [S20] [S21]
- Reports of collapse from a small synthetic fraction coexist with evidence that real-data retention and source diversity can mitigate collapse. The discrepancy likely reflects different datasets, model sizes, source models, and training procedures; no universal synthetic-data percentage is supported. [S4] [S7] [S14] [S15]
- Benchmark-competitive or higher-quality outputs can coexist with reduced adversarial robustness or poor real-world generalization, so benchmark gains do not resolve deployment safety. [S3] [S4] [S11] [S13] [S18]

### Important Gaps

- How do synthetic datasets compare with equivalent amounts of high-quality human-curated data across model sizes, languages, domains, and deployment tasks?
- What synthetic-to-real mixture, source diversity, and filtering strategy best preserve linguistic diversity and prevent collapse?
- Which independent methods reliably measure demographic fairness, factuality, shared generator/evaluator errors, adversarial robustness, and real-world distribution shift?
- What privacy, memorization, re-identification, provenance, and intellectual-property tests should be required for synthetic data derived from sensitive or proprietary sources?
- Do the reported adversarial-robustness and self-preference effects replicate across more models, languages, tasks, and deployment settings?
- Do predominantly synthetic approaches work for open-ended natural-language fine-tuning without reliable external validators?

**Analysis Duration:** 12.71s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

No usable new sources were retrieved, and the accumulated evidence is sufficient to answer the original question responsibly at a conditional level. Further searching could add studies, but the key conclusion is already stable: synthetic data can provide scale and targeted coverage, yet quality, bias, collapse, privacy, and deployment reliability must be established through independent evaluation rather than assumed.

**Next Search**

> What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation. additional evidence search 10

---

# Iteration 10

## 1. Search

**Query**

> What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation. additional evidence search 10

**Why this query**

No usable new sources were retrieved, and the accumulated evidence is sufficient to answer the original question responsibly at a conditional level. Further searching could add studies, but the key conclusion is already stable: synthetic data can provide scale and targeted coverage, yet quality, bias, collapse, privacy, and deployment reliability must be established through independent evaluation rather than assumed.

**Results**

5 results retrieved.

0 new unique sources added.

### Sources

No new unique sources were added.

**Search Duration:** 3.70s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Synthetic data provides practical benefits mainly as curated augmentation: it can lower collection and annotation costs, scale task-specific examples, address class imbalance, and cover rare, niche, low-resource, or privacy-sensitive cases.

**Confidence:** High

**Why this confidence level**

The benefit is consistently reported across many sources, although much of the evidence is survey, practitioner, industry, or case-study material rather than independently replicated controlled comparisons.

**Evidence**

- Multiple sources describe synthetic data as useful for augmentation, class balancing, edge cases, niche domains, rapid prototyping, and settings where human data is scarce, costly, or sensitive. [S2] [S5] [S6] [S9] [S12] [S16] [S20] [S21]

#### Finding 2

**Claim**

Synthetic-data quality is not guaranteed by scale or volume; factual errors, hallucinations, inconsistency, domain mismatch, irrelevant content, artificial regularities, and insufficient realism can harm downstream performance and real-world generalization.

**Confidence:** High

**Why this confidence level**

Multiple sources converge on the same failure modes and mitigation needs.

**Evidence**

- Sources identify concrete quality failure modes and recommend filtering, reweighting, consistency checks, curation, retrieval, refinement, and external verification. [S3] [S8] [S12] [S16] [S20] [S21]
- Human data is described as better at preserving linguistic nuance, cultural references, emotional detail, and expert judgment, while poorly constructed synthetic data can overfit artificial scenarios. [S11] [S13]

#### Finding 3

**Claim**

Synthetic data is more dependable for narrowly specified tasks with independent validators than for open-ended natural-language behavior.

**Confidence:** Medium

**Why this confidence level**

The distinction is consistently motivated, but the sources do not provide a comprehensive comparative study across task types.

**Evidence**

- Executable code and other rule-governed outputs can be checked through execution or external rules, whereas open-ended text is harder to validate and model-based evaluators may share the generator's errors or biases. [S10] [S16] [S20]

#### Finding 4

**Claim**

Recursive, single-source, or predominantly synthetic training can narrow the learned distribution, reduce lexical, semantic, and syntactic diversity, and impair generalization to human text.

**Confidence:** High

**Why this confidence level**

The core risk has direct empirical support and is corroborated by multiple reviews and summaries.

**Evidence**

- Experimental evidence reports reduced linguistic diversity and poorer modeling of human text under recursive synthetic-data training. [S2] [S4]
- Additional sources describe collapse, simplification of the original data distribution, and increasingly nonsensical outputs after repeated synthetic training. [S18] [S19] [S20]

#### Finding 5

**Claim**

Retaining real data and using diverse, independently sourced synthetic data may reduce distribution-collapse risk, but no universal safe synthetic-data percentage or mixture has been established.

**Confidence:** High

**Why this confidence level**

The mitigation pattern and regime dependence are supported, while the exact safe proportion remains unresolved.

**Evidence**

- Diverse source models and additive mixtures that retain real data preserve more distributional breadth in the reported settings than single-source or replacement regimes. [S4] [S7]
- Reports of collapse with a small synthetic fraction occur under particular datasets and training conditions and do not establish a universal threshold. [S14] [S15] [S4] [S7]

#### Finding 6

**Claim**

Synthetic data can reproduce or amplify bias from its source data or generator; controlled generation may improve representation, but demographic fairness gains must be measured downstream rather than assumed.

**Confidence:** Medium

**Why this confidence level**

The conditional risk-benefit pattern is consistent, but direct comparative demographic fairness measurements are sparse.

**Evidence**

- Sources describe possible class balancing, low-resource-language support, and targeted representation, while also warning about inherited bias, demographic underrepresentation, and bias amplification. [S5] [S6] [S9] [S11] [S12] [S16] [S20] [S21]
- One empirical study reports self-preference and safety-related effects after synthetic fine-tuning, without establishing broad demographic fairness improvements. [S4]

#### Finding 7

**Claim**

Synthetic fine-tuning can improve apparent output quality or benchmark performance while worsening adversarial robustness, safety, contamination resilience, or real-world generalization.

**Confidence:** High

**Why this confidence level**

The quality-versus-robustness tradeoff is directly reported, and several sources independently caution against relying on narrow benchmark scores.

**Evidence**

- An empirical study reports higher output quality alongside reduced adversarial robustness after synthetic fine-tuning. [S4]
- Reviews warn that benchmark saturation or contamination and overfitting to artificial scenarios can make benchmark gains poor proxies for deployment reliability. [S3] [S11] [S13] [S18]

#### Finding 8

**Claim**

Synthetic data may reduce direct exposure to human records, but it is not automatically private, legally safe, or free of provenance, memorization, re-identification, or intellectual-property risks.

**Confidence:** Medium

**Why this confidence level**

Both potential benefit and risk are represented, but the supplied material lacks systematic privacy measurements and definitive legal conclusions.

**Evidence**

- Sources present reduced direct exposure as a potential privacy benefit while identifying leakage and re-identification as unresolved; one report raises possible proprietary-content overlap and provenance concerns. [S5] [S6] [S9] [S11] [S13] [S17] [S18]

#### Finding 9

**Claim**

The most defensible evaluation regime separately assesses the synthetic dataset and the downstream model using independent, held-out human or real-world evidence.

**Confidence:** High

**Why this confidence level**

Evaluation requirements are consistent across the accumulated sources, although no single protocol is proven to predict every deployment outcome.

**Evidence**

- Dataset checks should cover fidelity, factuality, realism, diversity, representativeness, bias, contamination, and task alignment. [S3] [S5] [S8] [S16] [S20] [S21]
- Model checks should include real-world generalization, robustness, adversarial behavior, safety, contamination, evaluator self-preference, and realistic multi-step performance—not only benchmark accuracy. [S3] [S4] [S16] [S18] [S20] [S21]
- Human, external, or independently verifiable checks are needed because generators and model-based evaluators may share errors or biases. [S4] [S5] [S8] [S10] [S11]

### Conflicts Found

- Synthetic data is described both as improving diversity, representation, and coverage and as causing distribution narrowing and collapse. The evidence is conditional: curated, diverse, externally checked data may help, whereas recursive, single-source, or unverified data can worsen outcomes. [S2] [S4] [S5] [S7] [S20] [S21]
- Industry and practitioner sources present synthetic data as potentially improving fairness, privacy, and performance, while empirical and review evidence documents bias amplification, weakened robustness, collapse, and privacy leakage. The sources do not establish universal benefits or harms. [S4] [S5] [S6] [S9] [S11] [S17] [S18] [S20] [S21]
- Reports of collapse from a small synthetic fraction coexist with evidence that retaining real data and using diverse sources can mitigate collapse. These results likely depend on datasets, model sizes, source models, and training procedures; no universal threshold is supported. [S4] [S7] [S14] [S15]
- Model-in-the-loop or benchmark evaluation is recommended for curation, but may share errors or biases with the generator and miss adversarial or real-world failures. It should supplement, not replace, independent human, external, and held-out real-world testing. [S3] [S4] [S5] [S8] [S10] [S11]

### Important Gaps

- How do synthetic datasets compare with equivalent amounts of high-quality human-curated data across model sizes, languages, domains, and deployment tasks?
- What synthetic-to-real mixture, source diversity, filtering, and deduplication strategy best preserves linguistic diversity and prevents collapse?
- Which generation and curation strategies reliably limit demographic bias amplification, representation gaps, and self-preference?
- Do the reported adversarial-robustness and self-preference effects replicate across more models, languages, tasks, and deployment settings?
- What quantitative tests best detect privacy leakage, memorization, re-identification, provenance, and intellectual-property overlap?
- Which evaluation protocols best predict deployment reliability when generation and evaluation models share errors or biases?
- How much independently validated human data is needed for open-ended natural-language fine-tuning?

**Analysis Duration:** 14.79s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The runner reached the maximum research iteration budget. Analyzer assessment: The accumulated evidence is sufficient to answer the original question responsibly: synthetic data offers meaningful operational benefits but only conditionally, and the main risks and evaluation requirements are clear. Further searches could refine quantitative thresholds and replication evidence, but no remaining gap prevents a well-qualified answer.

**Stop Reason:** max_iterations

---

# Final Research Decision

**Research Stopped Because**

The runner reached the maximum research iteration budget.

**Stop Reason:** max_iterations

**Searches Performed:** 10

**Unique Sources:** 21

**Remaining Uncertainty**

- How synthetic datasets compare with equivalent amounts of high-quality human-curated data across model sizes, languages, domains, and deployment tasks.
- What synthetic-to-real mixture, source diversity, filtering, and deduplication strategy best preserves linguistic diversity and prevents collapse.
- Which independent methods reliably measure demographic fairness, factuality, shared generator/evaluator errors, adversarial robustness, and real-world distribution shift.
- What quantitative tests should detect privacy leakage, memorization, re-identification, provenance, and intellectual-property overlap.
- Whether reported adversarial-robustness and self-preference effects replicate across more models, languages, tasks, and deployment settings.
- How much independently validated human data is needed for open-ended natural-language fine-tuning.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 10 | 32.08s |
| OpenAI Analysis | 10 | 150.31s |
| Report Generation | 1 | 16.00s |
| Total Run | — | 198.39s |
