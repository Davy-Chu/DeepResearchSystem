# Research Report

## Research Question

What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation.

## Summary

Synthetic data can materially expand scarce, expensive, or sensitive training data and can target rare cases, class imbalance, and domain-specific tasks. Its benefits are conditional: quality, diversity, provenance, and alignment with real deployment data matter more than volume. The clearest risks are fidelity gaps, inherited or amplified bias, distribution collapse in recursive self-training, and evaluation that gives false reassurance when synthetic test data shares the generator’s assumptions. The accumulated evidence supports using synthetic data primarily as a curated supplement to fresh real data, with independent, subgroup-specific, production-like evaluation. The research stopped at the iteration limit, and important questions about safe mixture ratios, privacy, factuality, and transfer to real-world outcomes remain unresolved.

## Findings

### Finding 1

**Claim**

Synthetic data can reduce data scarcity and labeling constraints, while supporting targeted coverage of rare cases, underrepresented classes, domain-specific tasks, and evaluation scenarios.

**Confidence:** Medium

**Why this confidence level**

The use cases are consistent across several sources, and S11 provides a controlled domain-specific example, but broad transfer to general LLM training and deployment is not established.

**Evidence**

- Sources describe synthetic examples as useful for scarce labeled data, class imbalance, privacy-sensitive domains, rapid prototyping, domain adaptation, edge cases, adversarial inputs, ambiguous queries, multi-turn behavior, and decision-boundary testing. [S2] [S4] [S9]
- A requirements-engineering study reports that synthetic data improved selected classification tasks in a setting characterized by small, imbalanced, narrow-domain, and inconsistently labeled datasets. [S11]

### Finding 2

**Claim**

Synthetic-data utility depends on generation strategy, curation, validation, diversity, and distributional alignment—not simply on dataset size.

**Confidence:** High

**Why this confidence level**

Multiple sources, including controlled studies, support the general quality and alignment principle, although the magnitude and direction of effects vary by task.

**Evidence**

- Sources emphasize that synthetic-data quality depends on generation methods, validation, and alignment with the target distribution; curated synthetic data is contrasted with indiscriminate generation. [S1] [S4]
- Multi-sample prompting improved utility and diversity in requirements classification, but prompt optimization was task-dependent and similarity-based curation sometimes improved diversity while reducing task performance. [S11]
- A CVPR study identifies low synthetic-data quality and domain/bias gaps as obstacles, reporting that blind fine-tuning on synthetic data can reduce utility. [S6]

### Finding 3

**Claim**

Recursive or replacement-based training on model-generated data can narrow output distributions, reduce diversity, and degrade model quality; retaining fresh real data is presented as safer than replacing it.

**Confidence:** Medium

**Why this confidence level**

The direction of the risk is consistent and linked in the sources to peer-reviewed or research literature, but the primary studies and exact operating conditions were not retrieved directly.

**Evidence**

- S1 summarizes evidence that indiscriminate model-generated training causes irreversible defects and reports OPT-125m experiments with 20–28-point perplexity increases after five epochs of purely synthetic self-training. [S1]
- S2 independently identifies recursive synthetic training and narrowing distributions as major risks. [S2]
- S1 presents additive training alongside real data as lower risk than full replacement, while S8 notes that fresh real data can stabilize recursive training. [S1] [S8]

### Finding 4

**Claim**

Synthetic data can improve representation or fairness in some settings, but it does not automatically remove bias and may introduce domain, representational, preference, or subgroup-performance distortions.

**Confidence:** Medium

**Why this confidence level**

The evidence demonstrates that bias effects are conditional and multidimensional, including direct LLM studies, but it does not provide comprehensive demographic, linguistic, or representational fairness evidence across production LLMs.

**Evidence**

- The CVPR study reports that balanced synthetic data improved fairness but reduced accuracy because of a real-versus-synthetic domain gap; contextual generation and selective fine-tuning improved fairness while maintaining utility in its tested vision tasks. [S6]
- An LLM study reports that fine-tuning reduced self-preference bias, with human data most effective, multi-source synthetic data intermediate, and single-source synthetic data least effective. [S13]
- A self-consuming performative-loop study reports amplified preference bias and degraded generation quality over time, even while disparate bias tended to decrease. [S8]

### Finding 5

**Claim**

Synthetic-data diversity can mitigate distribution collapse, but improved diversity or apparent output quality does not guarantee improved safety or robustness.

**Confidence:** Medium

**Why this confidence level**

This is direct LLM fine-tuning evidence, but it comes from an arXiv preprint and tested conditions may not represent all models, data mixtures, or safety regimes.

**Evidence**

- S13 finds that greater diversity of synthetic source models preserves output-distribution breadth and linguistic diversity. [S13]
- The same study reports that synthetic fine-tuning preserved higher output quality while reducing adversarial robustness, with source diversity and generator size affecting the outcome. [S13]

### Finding 6

**Claim**

Synthetic evaluation sets can broaden coverage, but synthetic-set scores alone are insufficient evidence of real-world reliability.

**Confidence:** High

**Why this confidence level**

The benefit and limitation are supported by multiple sources and align directly with the requested evaluation focus, although no source quantifies false-reassurance rates or defines a universal validation standard.

**Evidence**

- Sources describe synthetic tests for edge cases, adversarial inputs, ambiguity, multi-turn context, failure modes, and decision boundaries. [S4]
- S5 warns that benchmark saturation, contamination, leakage, and limited realism can make scores unrepresentative of real-world performance; S10 and S6 describe fidelity and domain gaps that can omit unpredictable real inputs. [S5] [S6] [S10]
- The accumulated evidence therefore supports validating synthetic evaluations against independently collected human-authored, real-world, and production-like cases. [S4] [S5] [S6] [S10]

### Finding 7

**Claim**

Governance controls—especially provenance, deduplication, fidelity metadata, filtering, verification, and subgroup-specific checks—are necessary to make synthetic-data risks diagnosable and manageable.

**Confidence:** Medium

**Why this confidence level**

The recommendation is consistent across sources, but the evidence does not establish a universally effective control set or quantify the benefit of each control.

**Evidence**

- S2 identifies audit gaps from ungoverned synthetic data and calls lineage and fidelity metadata necessary. [S2]
- S1 highlights curation, deduplication, and quality filtering as central to successful synthetic-data use. [S1]
- S5 emphasizes novelty, reliability, verifiability, data cleaning, deduplication, privacy protection, and data-mixture design as core development concerns. [S5]

## Conflicts and Uncertainty

- Curated, additive synthetic data is presented as potentially effective and lower risk, while recursive or indiscriminate replacement can cause collapse. The apparent disagreement is conditional on training regime, curation, source diversity, and retention of fresh real data. [S1] [S2] [S8] [S13]
- Deduplication and similarity filtering are generally recommended, but S11 reports that similarity-based curation can improve diversity while harming classification performance. Removing redundancy may also remove useful task patterns. [S1] [S2] [S11]
- Bias outcomes are not uniform: some experiments find reduced self-preference or disparate bias, while others find increased preference bias and degraded quality in self-consuming or performative loops. Results depend on the bias metric, loop structure, data source, and fine-tuning setup. [S8] [S13]
- S6 provides useful evidence about domain shift and fairness tradeoffs, but it studies computer-vision classifiers rather than LLMs. Its mechanisms are relevant by analogy, not direct proof of equivalent LLM outcomes. [S6]
- S1 reports strong benchmark results from curated synthetic training, whereas S5 warns that benchmark contamination, saturation, and limited realism can make benchmark improvements poor indicators of deployment performance. [S1] [S5]
- S9 reports limited impact from response verification in its constrained experiments, while other sources treat validation and verification as central safeguards. The difference may reflect task and experimental-design differences; it should not be generalized to safety-critical or open-ended systems. [S9] [S2] [S5]
- The retrieved S12 material contains article metadata and title but not usable results, so it cannot establish conclusions about bias or behavioral diversity in real-world versus synthetic hotel-review annotations. [S12]

## Remaining Gaps

- A validated synthetic-to-real mixture ratio for particular LLM tasks, model scales, and recursive fine-tuning regimes is not established.
- The evidence does not determine which combination of demographic, linguistic, representational, preference, robustness, and safety metrics best detects harms that aggregate fairness scores conceal.
- The frequency and severity of factual, reasoning, coding, labeling, and instruction-following errors in synthetic examples—and the benefit of human or automated verification—remain unclear.
- There is no validated general standard for calibrating synthetic evaluation sets against independently collected human-authored data, production traffic, or real-world user outcomes.
- It remains unresolved whether multi-source synthetic data improves adversarial robustness, rather than primarily mitigating distribution collapse, across broader settings.
- The accumulated evidence does not establish privacy or memorization safety for treating synthetic data as a substitute for sensitive real data.
- Research stopped because the iteration limit was reached; unresolved questions should not be interpreted as answered.

## Conclusion

Synthetic data is best viewed as a controlled augmentation and evaluation tool, not a drop-in replacement for real data. Its practical benefits—greater coverage, lower data-acquisition burden, domain targeting, and faster experimentation—are most credible when generation is curated, diverse, traceable, and aligned with the target task. The main risks are fidelity and domain gaps, inherited or shifting biases, recursive distribution collapse, and evaluation leakage or false reassurance. A defensible deployment approach is to retain fresh real data, document provenance and filtering, monitor multiple bias and safety dimensions, and require independent human-authored or production-like evaluation before relying on synthetic-data gains. The evidence supports that direction, but does not provide universal mixture ratios or prove that synthetic-data improvements transfer to real-world outcomes.

## Sources

- [S1] Synthetic Data for LLM Training: Decision Guide 2026 — https://www.digitalapplied.com/blog/synthetic-data-generation-llm-training-decision-guide-2026
- [S2] Synthetic Data for AI Training: Use Cases and Risks [2026] — https://atlan.com/know/ai-agent/data-for-ai/synthetic-data-for-ai-training
- [S3] Using Synthetic Data to Improve LLM Fine‑Tuning | newline — https://www.newline.co/@Dipen/using-synthetic-data-to-improve-llm-finetuning--d453f658
- [S4] Synthetic Data Generation with LLMs: Techniques and Use Cases — https://tetrate.io/learn/ai/synthetic-data-generation-llms
- [S5] Large Language Models Are Still Getting Stronger, but Researchers Face New Bottlenecks in Data, Evaluation, and Safety | Newswise — https://www.newswise.com/articles/large-language-models-are-still-getting-stronger-but-researchers-face-new-bottlenecks-in-data-evaluation-and-safety
- [S6] Advancing Algorithmic Fairness via Selectively Fine-Tuning ... — https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_AIM-Fair_Advancing_Algorithmic_Fairness_via_Selectively_Fine-Tuning_Biased_Models_with_CVPR_2025_paper.pdf
- [S7] Bias Mitigation via Synthetic Data Generation: A Review — https://www.mdpi.com/2079-9292/13/19/3909
- [S8] Observations and Remedies for Large Language Model Bias in Self-Consuming Performative Loop — https://arxiv.org/html/2601.05184v1
- [S9] Synthetic Data Generation Strategies for Fine-Tuning LLMs | Scale AI — https://scale.com/blog/synthetic-data-fine-tuning-llms
- [S10] Medium — https://medium.com/foundation-models-deep-dive/challenges-and-pitfalls-of-using-synthetic-data-for-llms-7337fcda1316
- [S11] How Good Are Synthetic Requirements? Evaluating LLM- ... — https://hal.science/hal-05133432/file/2506.21138v1.pdf
- [S12] Biased by Design? Evaluating Bias and Behavioral Diversity in LLM Annotation of Real-World and Synthetic Hotel Reviews — https://www.mdpi.com/2673-2688/6/8/178
- [S13] The Impact of Synthetic Data Diversity on LLM Fine-Tuning — https://arxiv.org/html/2511.01490v1
- [S14] Medium — https://medium.com/@akankshasinha247/synthetic-data-evaluation-pipelines-scaling-fine-tuning-without-losing-alignment-f469a81cdf9a
