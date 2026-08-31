# Executive Summary

Synthetic training data—e.g. LLM-generated or programmatically constructed text—can **address data scarcity** and **improve coverage** cheaply, especially for rare classes or sensitive domains.  Proponents report improved downstream performance in low-resource settings, lower labeling cost, and built-in privacy advantages.  In practice, however, **data quality issues** (hallucinations, noise, distribution shifts) and **amplified biases** are common risks.  Evaluating synthetic data is also challenging: there is no single metric for “realism,” and studies use mixed benchmarks (statistical, human, LLM-based).  Results vary widely by task, data domain, model scale, and evaluation method: some papers find synthetic sets boost performance (especially if diverse and well-filtered), while others show degraded accuracy or fairness.  This report contrasts benefits vs. risks across **data quality**, **bias**, and **evaluation**, surveys evidence from recent literature, and gives practical guidance on when and how to use synthetic data for LLM training.

## Data Quality

- **Benefits:** Synthetic augmentation can greatly expand training volume and diversity.  LLMs can “hallucinate” large labeled corpora on demand (e.g. instruction-following Q&A or paraphrases) at a tiny fraction of human labeling cost.  This can fill in **coverage gaps** (edge cases, underrepresented topics) that real data lacks.  In low-data regimes, doubling the dataset with synthetic examples has lifted accuracy by ~3–26% in some studies.  Synthetic data can also be tailored (via prompts) for particular classes or difficulty levels, giving fine-grained control over coverage and balance that is hard to achieve with arbitrary real corpora.

- **Risks:** Synthetic examples often lack full fidelity to reality. LLM outputs can include factual errors or repeated phrasing (e.g., a review that redundantly repeats “it’s a mess”).  Hallucinated labels are another problem: if a teacher model “misunderstands the task,” it can insert wrong labels into the training set, and those errors propagate.  Distributional mismatch is common: synthetic data may not match the true data distribution, causing **distribution shift** and model collapse over generations.  For instance, Hataya et al. (ICCV’23) simulated contamination of ImageNet with generated images and found downstream classifier performance *worsened* as more synthetic data was added.  In LLM settings, similar effects can appear: if the synthetic generator is weak or biased, the model may overfit spurious patterns or noise.  

- **Mitigations:**  Best practices emphasize **diversity, faithfulness, and balance**.  Ensure synthetic data covers the full range of inputs (lengths, topics, difficulty).  Use strong, well-prompted teacher models and diversified prompts to enrich variety.  Validate outputs with filters or critics: remove exact duplicates, format errors, and obviously wrong generations.  Ideally add a human-in-the-loop or automated classifier to catch low-quality samples.  Blend synthetic with real data (e.g. 50/50) to ground training and slow model collapse.  

## Bias

- **Benefits:** Properly generated synthetic data can *reduce* bias if used carefully.  By design, one can oversample underrepresented groups or phrasing, creating a **balanced** dataset for training.  For example, Liu et al. (2025) found that combining fairness pre-processing with synthetic data generation produced fairer outcomes than applying the same algorithms to real data alone.  In other words, synthetic augmentation can be used as a targeted tool to mitigate bias (e.g. by “de-biasing” the generator or selecting neutral templates).  

- **Risks:** If the generator is biased, synthetic data **amplifies** those biases.  Pre-trained LLMs carry social and demographic biases in their weights; when they generate text, they tend to overproduce majority or stereotypical patterns.  Recent work warns that iterative training on synthetic text can **compound** bias: Wang et al. (2024) show that even with distributions held fixed, repeated fine-tuning on LLM-generated text progressively intensifies model biases.  The biases manifest as “polluted” datasets (model collapse) and decreased performance or representation for minoritized groups.  In extreme cases, synthetic loops have been observed to reduce minority accuracy and skew demographic distributions over generations.  Even without multi-turn feedback loops, a single augmentation can backfire: if 80% of synthetic classification examples belong to one class, the model will *inherit* that imbalance.  

- **Spurious Correlations:** Synthetic generators may also latch onto irrelevant correlations. For example, if a generator always associates “doctor” with “he,” it reinforces a gender stereotype. Unlike real data, there is no chance for real-world counterexamples unless explicitly programmed. 

- **Mitigations:**  Monitor and control bias at generation time. Use *causal or fairness-aware generation*: e.g. inject prompts or constraints to equalize subgroups.  Filter or re-weight examples based on sensitive attributes.  Mixed training (synthetic + real) helps: even a small fraction of authentic data can slow bias drift.  Lastly, after training, apply fairness checks and debiasing algorithms as usual.  The literature suggests synthetic data can help *if treated as a de-biasing intervention*, but left unchecked it can worsen harms.

## Evaluation

- **Benefits:** Synthetic data is invaluable for creating **controlled benchmarks** and test sets. Developers can generate *“golden datasets”* covering needed scenarios (e.g. rare edge cases) and safely evaluate models without risking real user data leakage.  This is particularly useful pre-deployment: one can repeatedly test and debug models on exactly reproducible synthetic inputs.  Synthetic evaluation sets also enable privacy-safe testing in regulated domains.  

- **Risks:** Evaluating synthetic data itself is nontrivial. There is **no single fidelity metric**; practitioners use a patchwork of statistics (distribution overlaps, model accuracy on hold-out tasks, human judgment).  Studies have noted that evaluation protocols vary widely (intrinsic vs. extrinsic metrics, adversarial tests, etc.), so conclusions depend on how you measure success.  For example, a synthetic dataset might score well on a language model’s perplexity metric but still fail to capture important semantics.  Moreover, benchmark validity is a concern: a model might perform well on a synthetic “OOB” test (because it’s similar to what it generated) but poorly on real-world data.  In short, *out-of-distribution* tests and robustness checks are essential, but often neglected.  

- **Mitigations:** A checklist approach is recommended:  **(1)** *Fidelity tests:* measure statistical similarity (KL divergence, coverage of n-grams) between synthetic and real data; or use a separate LLM to flag unrealistic samples.  **(2)** *Utility tests:* train models on synthetic vs. real and compare held-out performance on actual labeled data.  **(3)** *Bias tests:* evaluate fairness metrics (e.g. demographic parity gaps) on models trained with and without synthetic augmentation.  **(4)** *OOD robustness:* hold out rare categories or future data and see if synthetic-augmented models generalize better.  **(5)** *Human review:* sample-check synthetic examples for plausibility. Industry guides (NIST, IBM) emphasize ongoing monitoring: even after deployment, re-evaluate model drift and synthetic/data alignment.

## Conflicting Findings in the Literature

Different studies reach different conclusions because of **methodological factors**.  For instance, many early successes on synthetic data (e.g. self-instruct and Alpaca methods) assumed a strong teacher LLM and simple tasks like classification. In contrast, other work (e.g. Hataya et al. on vision) found harm when synthetic overwhelmed real data. Key reasons for discrepancy include:

- **Data/Domain Dependence:** Results vary by task. Synthetic question-answer pairs may boost a reading-comprehension model, while synthetic fiction may confuse a summarizer. Biomedical text (clean, structured language) often sees different results than social media text or code.  

- **Model Scale & Quality:** The capability of the synthetic *generator* matters. High-end LLMs (GPT-4, Claude 3) tend to produce better data than smaller ones. Conversely, using a small generator for a large model can introduce noise.  

- **Training Mix:** Some works train models on *pure* synthetic data vs others use a mix. Wyllie et al. show that adding any real data can dramatically slow bias amplification. Thus 100% synthetic regimes often fail, whereas hybrid training can succeed.  

- **Evaluation Protocols:** Without standard benchmarks, papers pick different metrics. Some measure only accuracy on a standard test, others examine fairness or human-likeness. For example, Shaib et al. (2024) focus on diversity metrics and find synthetic diversity correlates with accuracy, whereas others focus on distributional drift and report negative effects.  

- **Dataset Curation:** Preprocessing and prompt design vary. A synthetic set generated with broad, well-engineered prompts (covering 620k topics) can vastly outperform a naively prompted set. Differences in filtering (e.g. human curation vs. none) also change outcomes.  

In sum, synthetic data can help or hurt depending on these factors. There is no one-size-fits-all verdict, which is why the literature contains both enthusiastic case studies and cautionary counterexamples.

## Recommendations for Practitioners

- **When to use synthetic data:** Ideal when real data is **scarce, costly, or sensitive** (e.g. legal/medical text), or when you need to cover **rare scenarios**. Synthetic generation accelerates iteration when prompt changes or new requirements arise. Avoid synthetic as a blanket replacement for abundant, high-quality real data unless necessary. For exploratory prototyping, synthetic can be very effective.

- **Generation/curation:** Use a strong teacher model (preferably larger than your target model) with clear prompts. Begin with a small set of accurate, representative seed examples. Implement diversity “mutations”: vary length, style, topic, and difficulty. Always include automatic validation: filter out duplicates, format errors, and off-topic or trivial examples. Consider a human review of a sample to gauge quality. Generate somewhat more data than needed (e.g. 2×) and then prune to desired volume.

- **Bias mitigation:** Proactively address sensitive attributes. If the task involves demographics, design prompts to balance groups (e.g. explicitly ask for equal male/female names) or use a debiasing LLM prompt. After generation, run fairness audits on the synthetic set: if disparities appear, either regenerate that part or weight examples to rebalance. Mix synthetic with real: even a small injection (10–20%) of actual data can curb feedback loops. Finally, apply standard fairness post-processing (e.g. adversarial debiasing or equalization) on the fine-tuned model.

- **Evaluation Checklist:** Before deployment, validate synthetic data rigorously. Confirm **fidelity** with metrics or human spot-checking (does the text “feel” real?). Measure **utility** by training a model on synthetic vs. a baseline on real: if your model’s accuracy on held-out tasks is worse with synthetic, investigate quality issues. Test for **outliers**: any synthetic outputs that are incoherent or repetitive should be removed. Include a few real examples in validation to ensure the model generalizes back to reality. For **bias**, compute demographic/fairness metrics on a held-out real validation set and check for adverse effects.  Plan to **monitor** the deployed model: track key metrics over time and compare performance on new real user data vs. synthetic-based predictions.  Maintain transparency by logging how synthetic data was generated (prompts, model version), as recommended by NIST/IBM.

## Synthetic vs. Real Data: Key Attributes

| Attribute              | Synthetic Data                                       | Real Data                                             |
|------------------------|------------------------------------------------------|-------------------------------------------------------|
| **Cost**               | Low marginal cost per example once setup complete; can generate large volumes cheaply.  | High cost: expensive to collect, label, and audit.    |
| **Scalability**        | Very high: easily scale up by re-running generators. Supports “on-demand” data.        | Limited: collection efforts (surveys, scraping, annotation) scale slowly.  |
| **Fidelity**           | Risk of inaccuracies/hallucinations in content and labels. Can be tuned for coverage but may lack nuance. | High fidelity: real data is authentic by definition, but may contain its own noise/errors.    |
| **Privacy Risk**       | Very low: contains no actual personal records (unless generator memorized data). Useful for sensitive domains. | Potentially high: may contain PII or confidential info, requiring de-identification or special handling.    |
| **Bias Risk**          | Controllable to some extent (engineer prompts), but inherent model biases may **amplify** to unknown degree.  | Reflects population biases; biased collection can lead to skew. Hard to correct without synthetic balancing.  |
| **Eval Difficulty**    | Hard to validate: needs custom metrics/human checks (no “ground truth” to compare). Evaluations may overestimate utility if not careful. | Easier to benchmark (direct test-train splits), but may lack coverage of rare events.    |

## Suggested Experiments and Benchmarks

1. **Performance vs. Data Mix:** Create 3 training sets for your LLM task: (a) real data only, (b) synthetic data only, and (c) combined (e.g. 50/50). Fine-tune identical model instances on each. Evaluate on a held-out real test set (metrics: accuracy/F1 for classification, BLEU for generation, etc.). *Expected:* The “combined” model should match or exceed the real-only baseline if synthetic quality is high; a pure-synth model often underperforms. The gap will reveal how much signal vs. noise the synthetic provides. 

2. **Data Size Scaling:** Vary the amount of synthetic data (e.g. 0.5×, 1×, 2× of real set size) and plot performance. If synthetic is beneficial, accuracy should improve with more data (plateauing eventually). Diminishing or negative returns indicate quality issues. Also measure the **perplexity** of synthetic vs. real validation sets (lower perplexity ≈ more “realistic” to a reference model).

3. **Bias Audit:** If your task involves protected classes (gender/race etc.), generate synthetic examples balancing those classes. Train two models: one on the unbalanced real data, one on real+balanced-synth. Evaluate demographic parity or equality metrics on a labeled test set. *Expected:* The augmented model should reduce disparity if synthetic did its job. Conversely, if bias worsens, inspect synthetic distribution for inadvertent skew.

4. **OOD/Edge-case Coverage:** Identify a rare category or scenario not well-covered in your real data. Generate synthetic examples specifically for that scenario. Fine-tune two models: one with, one without these synthetic edge cases. Test both on instances of that rare scenario (metric could be accuracy or recall). *Expected:* The synthetic-augmented model should perform better on this OOD subset, illustrating utility of synthetic coverage.

5. **Data Drift Robustness:** Periodically re-evaluate the model on new incoming real data (or a simulated “future” dataset). Compare models trained with and without synthetic augmentation. Check if synthetic training makes the model more or less robust to distribution shift. This tests “model collapse” over time. If synthetic was outdated, performance may degrade faster.

Each experiment should include baseline comparisons and, where possible, human judgment. For example, present model outputs to human annotators for factuality or fluency ratings. Track the *expected outcome*: balanced synthetic should help and noisy synthetic should hurt; large differences will inform how much to trust synthetic data in your pipeline.

## Sources

1. Nadăș et al. (2026) – **“Synthetic Data Generation Using LLMs”** (survey)  
2. Rao et al. (2026) – **Scoping Review of Synthetic Data (biomedical)**  
3. Wang et al. (2024) – **“Bias Amplification in LLMs”** (arXiv)  
4. Hataya et al. (2023) – **“Will Large-scale Generative Models Corrupt Future Datasets?”** (ICCV, images)  
5. Shaib et al. (2024) – **“Diversity of Synthetic Data & Impact on LLMs”** (arXiv)  
6. Liu et al. (2025) – **“Can Synthetic Data be Fair and Private?”** (arXiv, learning analytics)  
7. Lumitech (2024) – **Synthetic Data Guide** (industry blog, IBM/NIST)  
8. Distil Labs (2026) – **Synthetic Data Fine-Tuning Guide** (industry blog)  
9. Arize AI (2024) – **“Creating/Validating Synthetic Datasets for LLMs”** (industry blog)  

