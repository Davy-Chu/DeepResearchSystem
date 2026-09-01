# Research Report

## Research Question

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

## Summary

Synthetic data can make LLM training and fine-tuning faster, cheaper, more scalable, and better suited to data-scarce, privacy-sensitive, or rare-event settings. However, these benefits are conditional. Generated examples may contain factual, labeling, stylistic, or distributional errors; source and generator biases may be reproduced or amplified; recursive use may narrow diversity; and synthetic data is not automatically private. The strongest evidence supports a hybrid, quality-controlled workflow: retain human or real-data anchors, inspect and filter generated examples, use diverse generators, test the resulting model on independent real-world data, and audit subgroup fairness, calibration, robustness, safety, and privacy. The research state stopped at the iteration limit, and direct evidence comparing real, synthetic, and mixed data for LLM fine-tuning—especially on subgroup fairness and production outcomes—remains limited.

## Findings

### Finding 1

**Claim**

Synthetic data can reduce the cost and time of obtaining task-specific fine-tuning data and can expand coverage in low-resource, specialized, rare-event, or privacy-sensitive settings.

**Confidence:** Medium

**Why this confidence level**

The practical benefits are consistently described, but the supplied evidence gives limited independent, production-level evidence about the size and durability of gains across LLM applications.

**Evidence**

- Synthetic examples can be generated rapidly and at scale, supporting augmentation, rapid prototyping, class-imbalance mitigation, and tasks where labeled data is expensive or scarce. [S1] [S2] [S5]
- Controlled experiments across mathematics, general question answering, and Text2SQL found that different generation strategies can improve cost-effectiveness depending on the available generation budget and task. [S18]

### Finding 2

**Claim**

Quality, rather than quantity alone, is a decisive factor: synthetic examples can be fluent yet factually incorrect, mislabeled, unrealistic, insufficiently diverse, or mismatched to the target task.

**Confidence:** High

**Why this confidence level**

Direct dataset inspection and downstream comparisons support this finding, with additional agreement from surveys and policy guidance. Generalization beyond the studied tasks remains uncertain.

**Evidence**

- A study of tool-use datasets found numerous errors in generated instructions and ground-truth API calls; models trained on validated subsets performed better or comparably to models trained on larger unverified datasets. [S8]
- Technical surveys identify factual inaccuracies, noise, inconsistency, weak stylistic or distributional realism, and limited diversity as recurring synthetic-data problems. [S2] [S9]
- Synthetic data that is poorly aligned with real-world inputs can lead to overfitting or degraded performance outside the synthetic scenarios. [S1] [S4]

### Finding 3

**Claim**

Synthetic data can improve representation of underrepresented groups and rare cases, but it can also reproduce or amplify source-data, annotator, or generator bias.

**Confidence:** High

**Why this confidence level**

The conditional benefit-and-risk pattern is consistent across the research state. However, direct subgroup-level evidence for LLMs fine-tuned on synthetic language data is still sparse.

**Evidence**

- Sources describe targeted generation and class balancing as ways to fill representation gaps and potentially improve fairness. [S1] [S2] [S5] [S16]
- Multiple sources warn that source biases may be propagated or magnified, and that balanced synthetic data can still create a real–synthetic domain or bias gap. [S1] [S2] [S4] [S15] [S20]
- Available fairness-focused studies describe performance–fairness trade-offs and do not establish that synthetic data is automatically fair after model training. [S29] [S30] [S33] [S34]

### Finding 4

**Claim**

Recursive or single-source synthetic training can narrow output and data distributions, although catastrophic 'model collapse' claims depend strongly on definitions and experimental assumptions.

**Confidence:** High

**Why this confidence level**

The evidence supports distribution narrowing as a genuine risk while also preserving meaningful uncertainty about its severity in realistic development settings.

**Evidence**

- Synthetic fine-tuning from more diverse sources mitigated several distribution-collapse measures and preserved broader output and linguistic diversity; single-source synthetic data showed weaker results on some evaluation dimensions. [S6]
- A position paper identifies multiple inconsistent definitions of model collapse and argues that some catastrophic scenarios rely on unrealistic replacement of real data by entirely synthetic data, while warning that distribution tails remain vulnerable. [S7]
- Other sources identify recursive self-training, narrowing distributions, and loss of diversity as risks and recommend retaining real data and tracking lineage. [S2] [S3] [S27]

### Finding 5

**Claim**

Synthetic data is not inherently private; generator memorization and fine-tuning can permit PII extraction, membership inference, or other leakage despite the absence of an obvious one-to-one record relationship.

**Confidence:** High

**Why this confidence level**

S22 directly studies the question's LLM-generated-data fine-tuning scenario using attack-based measurements. Exact risks vary by model, generator, data overlap, attack access, and pipeline, so the reported magnitudes should not be generalized universally.

**Evidence**

- Fine-tuning on LLM-generated data was associated in reported experiments with more than a 20% increase in PII extraction for Pythia and more than a 40% increase in membership-inference ROC-AUC for Pythia-6.9B after self-instruct tuning. [S22]
- Studies report that membership-inference attacks can exploit loss reduction during fine-tuning, and that repeated sensitive exposure can substantially increase leakage in tested models. [S21] [S24]
- Synthetic-data research warns that generators can memorize source records and enable reconstruction or re-identification; formal privacy protections can reduce utility. [S20]

### Finding 6

**Claim**

Evaluation should be layered and independent: assess the synthetic records, the fine-tuned model, and real-world or production-like behavior rather than relying only on aggregate benchmark accuracy or synthetic evaluation data.

**Confidence:** High

**Why this confidence level**

Multiple technical and applied sources support complementary evaluation layers, and S8 provides direct evidence that data-level inspection changes downstream conclusions. No universal evaluation standard is established.

**Evidence**

- Intrinsic correctness checks and model-driven in-context evaluation exposed errors in synthetic tool-use data, and filtering produced better or comparable downstream performance with less data. [S8]
- Recommended evaluation dimensions include factuality, task utility, distributional fit, diversity, robustness, safety, subgroup error rates, privacy leakage, and confidence calibration. [S2] [S6] [S11] [S12] [S26]
- A clinical validation framework compared model-extracted data with human abstraction, performed consistency checks, and replicated cohort-level outcomes, illustrating the value of human- and real-world-grounded validation. [S11]

### Finding 7

**Claim**

Fairness evaluation should include subgroup-specific accuracy, recall, precision, calibration, and uncertainty—not just aggregate accuracy or conventional parity metrics.

**Confidence:** High

**Why this confidence level**

The sources provide concrete examples of subgroup and uncertainty effects that aggregate accuracy can miss, although these methods have not been fully validated specifically for synthetic-data fine-tuning.

**Evidence**

- A clinical study found modest performance differences by race/ethnicity and lower recall for older patients even while downstream survival estimates remained broadly consistent. [S11]
- An uncertainty-aware fairness metric detected highly confident incorrect predictions that a conventional Equalized Odds analysis overlooked. [S12]
- Long-form generation requires evaluation of degrees of correctness and confidence because binary right/wrong metrics do not capture partially correct answers or calibration failures. [S26]

### Finding 8

**Claim**

A practical risk-reduction strategy is to combine synthetic data with human or real data, use multiple generation sources, filter and verify examples, preserve lineage, and re-audit the final model.

**Confidence:** High

**Why this confidence level**

This workflow is supported by convergent technical, empirical, and governance-oriented evidence, though the optimal mixture and thresholds remain task-dependent.

**Evidence**

- Sources recommend combining synthetic and human data, using model- or human-in-the-loop feedback, and retaining real data to anchor realism and coverage. [S1] [S2] [S9] [S27]
- Recommended workflows diagnose coverage and subgroup gaps, validate generated records, retrain on a real-plus-synthetic mixture, and repeat held-out fairness and quality audits. [S16]
- Source diversity reduced distribution collapse in reported synthetic fine-tuning experiments. [S6]

## Conflicts and Uncertainty

- Synthetic data is presented as potentially privacy-enhancing because it can reduce direct use or sharing of real records, but direct LLM fine-tuning studies report increased PII extraction and membership-inference risk. The apparent conflict is conditional: synthetic status alone does not establish privacy. [S1] [S4] [S20] [S22]
- Synthetic data may improve fairness through targeted representation and fairness-aware generation, yet it may also inherit or amplify bias and create a performance–fairness trade-off. Outcomes depend on generation controls, distributional alignment, model adaptation, and subgroup validation. [S1] [S2] [S15] [S20] [S29] [S30] [S33] [S34]
- Model-collapse research differs over the severity of the risk. Some sources emphasize recursive distribution narrowing, while S7 argues that catastrophic scenarios often use unrealistic all-synthetic assumptions. The evidence supports concern about diversity and distribution tails without establishing inevitable catastrophic failure. [S2] [S6] [S7]
- Automated or LLM-based judging can support scalable filtering and showed strong agreement with expert annotations in a tool-use study, but judge models can exhibit self-preference and other biases. Agreement in one setting does not establish reliability across domains, languages, or safety-critical cases. [S6] [S8] [S27]
- Some experiments report that response verification had limited incremental impact under particular constrained conditions, while broader evidence treats verification as important because unvalidated synthetic errors can materially harm training. The difference may reflect task and experimental-setting dependence. [S8] [S18]
- Fine-tuning may improve calibration in some settings, but improved calibration does not imply overall safety, factuality, robustness, fairness, or privacy; synthetic fine-tuning has separately been associated with reduced adversarial robustness in one study. [S6] [S26]
- Several sources report promising fairness-oriented synthetic-data methods, including causal-fairness approaches, but the supplied excerpts do not show whether those data improve LLM fine-tuning outcomes on independent real-world tests. [S34] [S35] [S36] [S37] [S38]

## Remaining Gaps

- Direct, independent comparisons of real-data, synthetic-data, and mixed-data fine-tuning for LLMs on factuality, calibration, subgroup fairness, robustness, privacy, and production-like performance.
- Subgroup-specific effects across demographic groups, languages, dialects, cultural contexts, and safety-critical populations.
- The amount and mixture of synthetic data that preserve tail coverage and real-world performance under distribution shift.
- How privacy findings vary with generator model, prompt design, source-data overlap, deduplication, synthetic-data proportion, and API-only versus logit-access threat models.
- The reliability of automated filters and LLM-as-a-judge systems for factual, cultural, minority-language, privacy, and safety-critical errors.
- Whether fairness-oriented or causal-fairness synthetic data produces downstream benefits after LLM fine-tuning, rather than only matching fairness metrics at the dataset level.
- Replication of reported cost-effectiveness, robustness, distribution-collapse, and privacy results across models, generators, tasks, and deployment conditions.

## Conclusion

Synthetic data is best treated as a controllable augmentation tool, not a drop-in replacement for real or human data. Its clearest benefits are scale, speed, lower labeling burden, targeted coverage, and the possibility of reducing direct exposure of sensitive records. Its central risks are low-quality or unrealistic examples, bias inheritance or amplification, distribution narrowing, hidden safety regressions, and privacy leakage through generator memorization or fine-tuning. The accumulated evidence favors a hybrid and auditable approach: anchor generation with human or real data, diversify sources, validate records before training, evaluate the final model on independent real-world-grounded tests, and measure subgroup performance, uncertainty, calibration, robustness, safety, and privacy attacks. Because research stopped at the maximum iteration limit, the report does not resolve how these trade-offs behave broadly in production LLM fine-tuning; that remains an important empirical gap.

## Sources

- [S1] LLM synthetic data: Fine-tuning LLMs with AI-generated data | SuperAnnotate — https://www.superannotate.com/blog/llm-synthetic-data
- [S2] Synthetic Data Generation Using Large Language Models: Advances in Text and Code — https://arxiv.org/html/2503.14023v1
- [S3] Synthetic Data for AI Training: Use Cases and Risks [2026] — https://atlan.com/know/ai-agent/data-for-ai/synthetic-data-for-ai-training
- [S4] Recommendations on the Use of Synthetic Data to Train AI Models | United Nations University — https://unu.edu/publication/recommendations-use-synthetic-data-train-ai-models
- [S5] Synthetic Data Generation with LLMs: Techniques and Use Cases — https://tetrate.io/learn/ai/synthetic-data-generation-llms
- [S6] The Impact of Synthetic Data Diversity on LLM Fine-Tuning - arXiv — https://arxiv.org/html/2511.01490v1
- [S7] 1Introduction — https://arxiv.org/html/2503.03150v2
- [S8] Quality Matters: Evaluating Synthetic Data for Tool-Using LLMs — https://arxiv.org/html/2409.16341v2
- [S9] On LLMs-Driven Synthetic Data Generation, Curation, and Evaluation: A Survey | alphaXiv — https://www.alphaxiv.org/abs/2406.15126
- [S10] How to Synthesize Text Data to Avoid Model Collapse? — https://openreview.net/forum?id=mVCcWCjeEz
- [S11] Fairness by design: End-to-end bias evaluation for LLM-generated data — https://resources.flatiron.com/publications/fairness-by-design-end-to-end-bias-evaluation-for-llm-generated-data
- [S12] Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs - Apple Machine Learning Research — https://machinelearning.apple.com/research/fairly-certain
- [S13] Guide to Ethical Fine-Tuning of Large Language Models | Tonic.ai — https://www.tonic.ai/guides/ethical-fine-tuning-llm-synthetic-data
- [S14] Using Synthetic Data to Improve LLM Fine‑Tuning - Newline — https://www.newline.co/@Dipen/using-synthetic-data-to-improve-llm-finetuning--d453f658
- [S15] Advancing Algorithmic Fairness via Selectively Fine-Tuning ... — https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_AIM-Fair_Advancing_Algorithmic_Fairness_via_Selectively_Fine-Tuning_Biased_Models_with_CVPR_2025_paper.pdf
- [S16] Synthetic Data for Bias Mitigation 2026: 5 Methods + FAGI — https://futureagi.com/blog/synthetic-data-generation-bias-2025
- [S17] Synthetic Data + Evaluation Pipelines: Scaling Fine-Tuning ... — https://medium.com/@akankshasinha247/synthetic-data-evaluation-pipelines-scaling-fine-tuning-without-losing-alignment-f469a81cdf9a
- [S18] Synthetic Data Generation Strategies for Fine-Tuning LLMs | Scale AI — https://scale.com/blog/synthetic-data-fine-tuning-llms
- [S19] LLM Security & Privacy — https://github.com/chawins/llm-sp
- [S20] Privacy-Preserving Fair Synthetic Tabular Data — https://arxiv.org/html/2503.02968v1
- [S21] SOFT: Selective Data Obfuscation for Protecting LLM Fine-tuning against Membership Inference Attacks | USENIX — https://www.usenix.org/conference/usenixsecurity25/presentation/zhang-kaiyuan
- [S22] Hidden Dangers of Fine-tuning Large Language Models ... — https://www.usenix.org/system/files/usenixsecurity25-akkus.pdf
- [S23] Targeted Training Data Extraction—Neighborhood Comparison-Based Membership Inference Attacks in Large Language Models — https://www.mdpi.com/2076-3417/14/16/7118
- [S24] Assessing and Mitigating Data Memorization Risks in Fine ... — https://arxiv.org/html/2508.14062v1
- [S25] Our Research on Membership Inference Attacks and Preventing Privacy Leaks - The JetBrains Blog — https://blog.jetbrains.com/research/2026/06/membership-inference
- [S26] Calibrating Long-form Generations from Large Language Models — https://arxiv.org/html/2402.06544v1
- [S27] Synthetic Data for LLM Fine-Tuning 2026 — https://futureagi.com/blog/synthetic-data-fine-tuning-llms
- [S28] Fair and square? Evaluating fairness of LLM-generated ... — https://doi.org/10.1016/j.infsof.2025.107980
- [S29] Fair and Square? Evaluating Fairness of LLM-Generated ... — https://papers.ssrn.com/sol3/Delivery.cfm/896be1ad-c96e-4eb7-b15d-e65aa71d30a0-MECA.pdf?abstractid=5246323&mirid=1
- [S30] Fair and square? Evaluating fairness of LLM-generated ... — https://dl.acm.org/doi/10.1016/j.infsof.2025.107980
- [S31] Fair and Square? Evaluating Fairness of LLM-Generated ... — https://figshare.com/s/fc0bdef65bef553d445a
- [S32] Fair and square? Evaluating fairness of LLM-generated ... — https://www.researchgate.net/publication/398255569_Fair_and_square_Evaluating_fairness_of_LLM-generated_synthetic_datasets
- [S33] Fair and Square? Evaluating Fairness of Llm-Generated ... — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5246323
- [S34] Towards Causally Fair LLM-augmented Synthetic Data ... — https://arxiv.org/html/2506.19082v1
- [S35] Towards Causally Fair LLM-augmented Synthetic Data ... — https://www.semanticscholar.org/paper/420adce71f6bc1496e559b8192685389078c6371
- [S36] Towards Causally Fair LLM-augmented Synthetic Data ... — https://www.researchgate.net/publication/398311961_FairCauseSyn_Towards_Causally_Fair_LLM-augmented_Synthetic_Data_Generation
- [S37] Towards Causally Fair LLM-Augmented Synthetic Data ... — https://futurehealth.uci.edu/projects/faircausesyn-towards-causally-fair-llm-augmented-synthetic-data-generation
- [S38] Towards Causally Fair LLM-Augmented Synthetic Data ... — https://www.themoonlight.io/en/review/faircausesyn-towards-causally-fair-llm-augmented-synthetic-data-generation
