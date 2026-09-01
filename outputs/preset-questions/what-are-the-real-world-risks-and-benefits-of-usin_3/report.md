# Research Report

## Research Question

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

## Summary

This is an automatically generated incomplete report. The research run ended with stop reason `max_iterations`, and normal finalization did not complete during OpenAI Ledger Report Generation. The validated findings collected before that point are preserved below without claiming that the evidence is complete.

## Findings

### Finding 1

**Claim**

Synthetic data can provide scalable, task-specific training examples when real labeled or domain-specific data is scarce, expensive, privacy-sensitive, or difficult to collect; reported use cases include instruction examples, reasoning traces, code, class-imbalance augmentation, edge cases, and domain adaptation.

**Confidence:** Medium

**Why this confidence level**

Multiple sources directly describe these benefits, but the supplied evidence is largely practitioner-oriented and does not establish that they generalize across domains or tasks.

**Evidence**

- Describes synthetic fine-tuning data, edge-case augmentation, and privacy substitution as responses to data scarcity, annotation cost, and privacy constraints. [S1]
- Lists training augmentation, minority-class generation, privacy-sensitive data sharing, rapid prototyping, evaluation cases, and domain adaptation as practical uses. [S4]

### Finding 2

**Claim**

Synthetic data may improve downstream performance when it is curated, quality-filtered, deduplicated, and used alongside real data rather than indiscriminately replacing it; the supplied examples report strong coding-benchmark results for Phi-1 trained with curated synthetic textbooks and exercises plus real web data.

**Confidence:** High

**Why this confidence level**

The new study supplies direct comparative evidence that data quality can matter more than quantity for tool-using LLMs. The claim remains bounded because the evidence concerns two tool-use benchmarks rather than broad pretraining or general fine-tuning.

**Evidence**

- States that additive use of synthetic data with retained real data has a bounded-error rationale and emphasizes deduplication and quality filtering. [S1]
- Reports that high-quality, validated synthetic training data produced better or comparable tool-use performance than larger unverified datasets, supporting the benefit of curation and validation over indiscriminate volume. [S10]
- Corroborates that high-quality synthetic data outperformed unvalidated data even when smaller. [S12]

### Finding 3

**Claim**

Replacing real training data with recursively generated synthetic data can cause model collapse: distribution tails and diversity are lost, errors compound across generations, and model quality may degrade substantially.

**Confidence:** High

**Why this confidence level**

S7 provides additional, though practitioner-oriented and indirect, support for recursive degradation; it does not materially alter the existing conclusion or quantify the effect across settings.

**Evidence**

- Reports OPT-125m experiments in which five epochs of purely synthetic self-training increased perplexity by 20–28 points when no real data was retained. [S1]
- States that recursive synthetic training narrows distributions until outputs degrade. [S2]
- Warns that repeated training on model-generated content without new information or external feedback can stagnate or degrade capabilities. [S5]
- Describes a negative recursive loop in which training generative models on generated data can reduce output quality, consistent with degradation from repeated model-generated data. [S7]

### Finding 4

**Claim**

Synthetic-data quality depends on generation and curation choices: uncontrolled generation can introduce hallucinations, noise, duplication, limited novelty, and distributional narrowing, whereas prompting for varied audiences or formats, validation, filtering, and deduplication can improve coverage and consistency.

**Confidence:** High

**Why this confidence level**

S10 adds direct empirical evidence that uncontrolled synthetic generation can contain substantive task-specific errors and that validation and filtering improve dataset reliability. The broader claims about diversity, factuality, and coverage remain less directly quantified.

**Evidence**

- Contrasts volume without curation, which amplifies failure modes, with curated textbook-quality data; reports less than 1% duplicate content in the described Cosmopedia dataset after varying audience and format. [S1]
- States that utility depends on generation technique, validation, and alignment with target-distribution requirements, and that LLM generation can create varied contextual examples. [S4]
- Identifies low-quality, duplicated, noisy, biased, and insufficiently novel data as development bottlenecks and says synthetic data must be reliable, verifiable, and sustainable. [S5]
- Finds numerous errors in LLM-generated tool-use instructions and API-call sequences and shows that intrinsic quality checks can be used to filter unreliable instances. [S10]
- Summarizes the reported quality-assessment and filtering approach for synthetic tool-use data. [S12]

### Finding 5

**Claim**

Synthetic data can mitigate some representation and class-imbalance problems by deliberately generating examples for underrepresented classes or scenarios, but it can also preserve or reproduce biases inherited from the generating model and source distribution.

**Confidence:** High

**Why this confidence level**

The new review and practitioner source broaden support for inherited, selection, linguistic, and mitigation-related bias mechanisms. However, the evidence still does not provide controlled quantitative evidence specifically linking synthetic-data generation choices to fairness outcomes, so the confidence applies to the general conditional claim rather than a universal mitigation effect.

**Evidence**

- Describes targeted generation for underrepresented classes and rare edge cases as a way to address imbalance, while defining synthetic data as mimicking real-world patterns and distributions. [S4]
- Identifies biased information as a risk in training data and emphasizes fairness as an evaluation concern for LLMs. [S5]
- States that selection and coverage bias can arise when populations or linguistic patterns are underrepresented, and presents synthetic-data rebalancing and conditional generation as possible mitigation strategies when categories or records are missing. [S7]
- Reviews demographic, cultural, racial, gender, socioeconomic, and linguistic bias in LLMs, identifying nonrepresentative training data as a source and discussing resampling, augmentation, fairness constraints, and post-processing as mitigation approaches. [S8]
- Reports that demographic cues influenced LLM pairwise decisions and that masking explicit demographic information reduced some disparities, while prompt candidate order produced systematic selection effects; this illustrates that bias can persist through implicit cues and task structure even when explicit attributes are removed. [S6]

### Finding 6

**Claim**

Benchmark scores alone are insufficient to establish that a model trained or fine-tuned with synthetic data is reliable in deployment; evaluation should include contamination and leakage checks, realistic downstream tasks, factuality, robustness, safety, fairness, and reproducibility.

**Confidence:** High

**Why this confidence level**

S9 broadens support for tailored, multidimensional, human-plus-automated, and continuous evaluation, while S10 directly demonstrates why model-level scores alone can obscure training-data problems. These sources still do not validate a universal evaluation protocol.

**Evidence**

- States that standard benchmarks may be saturated or contaminated, can fail to distinguish models, and may not predict complex real-world reliability; it calls for realistic evaluation addressing contamination, fairness, reproducibility, and safety. [S5]
- Describes synthetic edge-case, adversarial, ambiguity, multi-turn, boundary, calibration, and robustness test generation as evaluation uses. [S4]
- Warns that synthetic evaluation sets have distinct risks, including distribution drift and evaluation overfitting, and treats evaluation as a separate use case from training. [S1]
- Provides experimental evidence that LLM decisions vary with gender and ethnicity cues and with candidate order, and recommends masking demographic information plus monitoring group-level outcomes in high-stakes settings. [S6]
- Reviews data-level, model-level, and output-level bias evaluation methods and mitigation strategies, supporting evaluation across multiple layers rather than reliance on a single benchmark. [S8]
- Identifies selection, automation, temporal, implicit, and social bias, and recommends human supervision for mission-critical applications; it also links generated-data recursion to quality degradation. [S7]
- States that evaluation should be use-case-specific and multidimensional, combining quantitative metrics with human judgments, and that continuous production monitoring is needed because static benchmarks may miss performance drift; it also identifies contamination and evaluation subjectivity as challenges. [S9]
- Distinguishes intrinsic evaluation of synthetic training data from extrinsic model evaluation and demonstrates that data-quality assessment changes the interpretation of downstream model results. [S10]
- Corroborates the distinction between assessing synthetic-data reliability and measuring final model performance. [S12]

### Finding 7

**Claim**

For synthetic data used to train tool-using LLMs, intrinsic quality assessment—using human-defined correctness criteria and automated or model-driven checks such as in-context evaluation—can identify errors in instructions and API-call traces, filter low-quality instances, and improve downstream performance; in the reported ToolBench and ToolAlpaca experiments, smaller high-quality datasets performed better or comparably to larger unverified datasets.

**Confidence:** High

**Why this confidence level**

S10 provides a detailed research report with intrinsic and extrinsic evaluations across two benchmarks, while S12 corroborates the central result. The finding is nevertheless specific to tool-using LLMs and does not establish general validity across all synthetic-data applications.

**Evidence**

- Directly reports errors in synthetic instructions and ground-truth API calls, proposes human-defined intrinsic criteria and model-driven In-Context Evaluation, and finds that filtered high-quality data yields better or comparable performance on two tool-use benchmarks despite smaller quantity. [S10]
- Independently presents the same study's finding that models trained on high-quality synthetic data outperform models trained on unvalidated data, even with less data. [S12]

## Conflicts and Uncertainty

- Evidence concerning ledger claim C3 is conflicting: Replacing real training data with recursively generated synthetic data can cause model collapse: distribution tails and diversity are lost, errors compound across generations, and model quality may degrade substantially. [S1] [S2] [S5] [S7]

## Remaining Gaps

- The supplied sources do not provide controlled, quantitative evidence on how synthetic training affects demographic, cultural, linguistic, or viewpoint fairness, nor how source-model choice, prompting, filtering, and human review change those outcomes.
- The supplied evidence does not establish validated methods or comparative results for measuring factuality, synthetic-data quality, generalization, robustness, safety, and downstream performance while avoiding synthetic-data contamination or evaluator bias.
- The evidence is insufficient to determine broadly applicable thresholds for the proportion of synthetic data, or when additive mixing, filtering, deduplication, external verification, and human review reliably outweigh risks across pretraining versus fine-tuning and across domains.
- The new sources broaden evidence about general LLM bias and bias evaluation, but do not isolate the causal effect of synthetic-data generation, filtering, or mixing on demographic, cultural, linguistic, or viewpoint fairness in models trained or fine-tuned with synthetic data.
- The new sources identify evaluation dimensions and mitigation techniques, but do not provide comparative validation of synthetic-data-specific evaluation protocols against independent real-world outcomes, including factuality, generalization, robustness, safety, contamination, and evaluator bias.
- SQ1: How does using synthetic data to train or fine-tune large language models affect data quality, including factual accuracy, diversity, coverage, consistency, noise, and the risk of recursive or model-induced errors? (PARTIAL: Open high- or medium-importance research gaps still block a sufficient answer.)
- SQ2: How does synthetic training data affect bias and fairness in large language models, including the introduction, amplification, preservation, or mitigation of demographic, cultural, linguistic, and viewpoint biases? (PARTIAL: Open high- or medium-importance research gaps still block a sufficient answer.)
- SQ3: How should large language models trained or fine-tuned with synthetic data be evaluated, and what limitations or risks arise when evaluating them? (PARTIAL: Open high- or medium-importance research gaps still block a sufficient answer.)
- SQ4: What practical conditions determine whether the benefits of synthetic data outweigh its risks when training or fine-tuning large language models? (PARTIAL: Open high- or medium-importance research gaps still block a sufficient answer.)

## Conclusion

The findings above reflect the evidence validated before the run ended. They should be treated as provisional because normal final synthesis did not complete and important gaps may remain.

## Sources

- [S1] Synthetic Data for LLM Training: Decision Guide 2026 — https://www.digitalapplied.com/blog/synthetic-data-generation-llm-training-decision-guide-2026
- [S2] Synthetic Data for AI Training: Use Cases and Risks [2026] — https://atlan.com/know/ai-agent/data-for-ai/synthetic-data-for-ai-training
- [S3] Using Synthetic Data to Improve LLM Fine‑Tuning - Newline — https://www.newline.co/@Dipen/using-synthetic-data-to-improve-llm-finetuning--d453f658
- [S4] Synthetic Data Generation with LLMs: Techniques and Use ... — https://tetrate.io/learn/ai/synthetic-data-generation-llms
- [S5] Large Language Models Are Still Getting Stronger, but ... — https://www.newswise.com/articles/large-language-models-are-still-getting-stronger-but-researchers-face-new-bottlenecks-in-data-evaluation-and-safety
- [S6] Fairness in AI Decisions About People: Evidence from LLM Experiments — https://manhattan.institute/article/fairness-in-ai-decisions-about-people-evidence-from-llm-experiments
- [S7] Data bias in LLM and generative AI applications — https://mostly.ai/blog/data-bias-types
- [S8] Bias in Large Language Models: Origin, Evaluation, and Mitigation — https://arxiv.org/html/2411.10915v1
- [S9] LLM Evaluation: Benchmarks to Test Model Quality in 2026 | Label Your Data — https://labelyourdata.com/articles/llm-fine-tuning/llm-evaluation
- [S10] Quality Matters: Evaluating Synthetic Data for Tool-Using LLMs — https://arxiv.org/html/2409.16341v2
- [S11] Assessment of fine-tuned large language models for real-world chemistry and material science applications† — https://pmc.ncbi.nlm.nih.gov/articles/PMC11629507
- [S12] Quality Matters: Evaluating Synthetic Data for Tool-Using LLMs | Abdullah Mamun — https://abdullah-mamun.com/talk/quality-matters-evaluating-synthetic-data-for-tool-using-llms
