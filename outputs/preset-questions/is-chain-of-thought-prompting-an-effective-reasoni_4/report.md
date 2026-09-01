# Research Report

## Research Question

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

## Summary

The supplied evidence supports a conditional rather than binary conclusion. CoT can improve final-answer performance on some multistep arithmetic, mathematical, symbolic, and commonsense tasks, particularly under particular model-capability and prompt conditions. However, gains are not uniform, and in recent strong models on the supplied GSM8K and MATH evaluations, few-shot CoT exemplars did not improve reasoning performance over zero-shot CoT; their clearest contribution was output-format alignment. Causal-faithfulness studies further indicate that displayed intermediate reasoning may not reliably mediate the final answer. At the same time, structured and causally pruned reasoning interventions report accuracy or efficiency gains, suggesting that some benefits may come from additional effective computation, decomposition, search, or selective intermediate processing rather than verbosity or the mere presence of a rationale.

## Findings

### Finding 1

**Claim**

CoT improves final-task performance most plausibly on selected multistep arithmetic, mathematical, symbolic, and some commonsense tasks, but the benefit depends on model capability, task difficulty, prompt construction, and evaluation conditions rather than applying uniformly.

**Confidence:** Medium

**Why this confidence level**

The evidence converges on conditional benefits but does not provide sufficiently controlled comparisons across model families, task domains, decoding methods, and metrics to support a universal effect.

**Evidence**

- The supplied sources report prior gains on mathematical, arithmetic, commonsense, and symbolic tasks and describe CoT as particularly useful for complex multistep problems. [S1] [S2] [S3] [S4]
- A recent evaluation found that traditional few-shot CoT did not improve over zero-shot CoT in strong models on GSM8K and MATH, while noting that weaker models may benefit. [S7]

### Finding 2

**Claim**

“CoT” is not a single experimentally invariant intervention. Zero-shot and few-shot rationales, exemplar construction, and structured variants can yield different outcomes, but the independent effects of exemplar number and ordering remain mixed and task- or model-dependent.

**Confidence:** High

**Why this confidence level**

This is the current qualified wording after verification. The evidence strongly supports intervention heterogeneity, but not a universal effect of exemplar count or order.

**Evidence**

- The sources distinguish conventional few-shot, zero-shot, automated, hierarchical, and other structured variants, with reported effects depending on adherence, rationale construction, and evaluation setup. [S1] [S2] [S3] [S4]
- In strong recent models, few-shot and enhanced exemplars sometimes changed output format without improving reasoning relative to zero-shot prompting; the evidence does not establish broad effects for exemplar number or ordering. [S7]

### Finding 3

**Claim**

The literature contains a genuine causal interpretation conflict: some accounts treat intermediate steps as computational scaffolds that support decomposition, coherence, attention, error reduction, or procedural generalization, whereas other evidence indicates that displayed reasoning can be post-hoc, weakly causal, or primarily formatting-related.

**Confidence:** High

**Why this confidence level**

The evidence clearly supports competing interpretations, but the causal-faithfulness results are heterogeneous and bounded: some concern schema-guided structures or a 9B model and binary-classification tasks, not free-form CoT universally.

**Evidence**

- Some supplied sources describe stepwise reasoning as helping decomposition, coherence, observability, debugging, and procedural generalization. [S1] [S2] [S3] [S6]
- In recent strong-model mathematical evaluations, few-shot exemplars were reported to align output format without improving reasoning over zero-shot prompting. [S7]
- A controlled study of schema-guided intermediate structures found that models sometimes failed to update final predictions after those structures were edited, by up to 60% of cases; external-tool derivation substantially reduced this fragility. [S12]
- Probing and intervention evidence in one set of experiments found answer representations decodable before CoT and summarized cases where corrupting or perturbing reasoning left final answers unchanged. [S14]
- A causal step-selection study identified redundant and indispensable steps and reported accuracy-preserving efficiency improvements, supporting the possibility that some intermediate computation is useful even when full displayed rationales are not faithful. [S13]

### Finding 4

**Claim**

Structured reasoning can outperform flat CoT and reduce inference cost in the reported evaluations, indicating that gains may depend on organization and sufficient computation rather than rationale verbosity itself.

**Confidence:** Medium

**Why this confidence level**

The reported results are direct for the specific interventions and benchmarks, but Hi-CoT lacks independent validation in the supplied evidence, and the two methods are not shown to have identical mechanisms.

**Evidence**

- Hi-CoT reportedly increased average accuracy by 6.2% and reduced trace length by 13.9% across 13 model configurations and five mathematical benchmarks relative to CoT. [S1]
- Causal pruning and reconstruction reportedly reduced redundancy and token usage while preserving or improving accuracy on mathematical and commonsense benchmarks. [S13]

### Finding 5

**Claim**

In the supplied strong-model study, few-shot CoT exemplars may primarily improve presentation and evaluator-facing format rather than reasoning accuracy; this conclusion is bounded to the tested models, tasks, exemplars, and evaluation implementation.

**Confidence:** High

**Why this confidence level**

The claim is directly supported for the specified setting, but it should not be generalized to all models, tasks, or forms of CoT. A broad secondary account reports accuracy and procedural-generalization benefits in other settings.

**Evidence**

- Experiments with recent Qwen2.5-series models on GSM8K and MATH reported no reasoning-performance improvement from traditional or enhanced few-shot CoT over zero-shot CoT, while identifying output-format alignment as the primary contribution of exemplars. [S7]
- Evidence that answers can be represented before CoT and that some reasoning perturbations leave conclusions unchanged is consistent with a formatting or post-hoc contribution in at least some settings. [S14]

### Finding 6

**Claim**

Evaluation implementation can change the apparent relative benefit of zero-shot and few-shot CoT: correcting a reported GSM8K evaluator bias substantially increased measured zero-shot CoT performance.

**Confidence:** Medium

**Why this confidence level**

The source directly reports the implementation effect, but the supplied ledger contains no independent evidence establishing how widespread this evaluator problem is.

**Evidence**

- The supplied study reports that an open-source GSM8K evaluation bias underestimated zero-shot CoT, changing the apparent comparison with few-shot exemplars. [S7]

### Finding 7

**Claim**

The strongest fault lines are differences in model capability, task composition and difficulty, prompt instantiation, the amount and organization of effective computation, causal faithfulness of rationales, and evaluator design—not simply disagreement over whether CoT exists as a single treatment.

**Confidence:** High

**Why this confidence level**

These dimensions are repeatedly represented in the supplied claims, but their relative contributions have not been isolated through a common controlled factorial design.

**Evidence**

- Reported benefits vary with model scale and capability, task type and difficulty, and zero-shot versus few-shot or structured prompt construction. [S1] [S2] [S3] [S4] [S7]
- Causal probes and interventions produce evidence both for useful intermediate computation and for rationales that do not reliably determine final answers. [S12] [S13] [S14]
- Evaluator correction changed the measured zero-shot/few-shot comparison in GSM8K. [S7]

## Conflicts and Uncertainty

- The supplied evidence conflicts over whether CoT rationales improve reasoning itself or mainly provide useful structure, inspectability, and format. S6 presents broad benefits for accuracy and procedural generalization, while S7, S12, and S14 provide bounded evidence for formatting-related or post-hoc reasoning and weak causal mediation. [S6] [S7] [S12] [S14]
- Structured reasoning interventions report accuracy and efficiency benefits, but it remains uncertain whether these results establish a general CoT effect, a benefit from additional computation or search, or an effect of response constraints and token allocation. [S1] [S13]
- The evidence does not reconcile results across model families, scales, task domains, prompt wording, decoding or sampling procedures, and evaluation metrics. [S1] [S7] [S13] [S14]
- The causal-faithfulness evidence is not yet general for free-form natural-language CoT: one study concerns schema-guided structures, and another concerns a 9B instruction-tuned model and four binary-classification tasks. [S12] [S14]
- The supplied record reached the maximum research iterations. No additional evidence is supplied to resolve benchmark contamination or saturation, replication quality, statistical uncertainty, evaluator sensitivity beyond the reported GSM8K issue, or matched comparisons with hidden scratchpads, answer-only controls, self-consistency, and external tools. [S7] [S12] [S13] [S14]

## Remaining Gaps

- Whether free-form CoT rationales are causally used, faithfully report computation, or mainly improve formatting, inspectability, compliance, or scoring remains unresolved.
- Controlled evidence is insufficient to reconcile differences across model families, parameter scales, task difficulty, prompt wording, decoding or sampling, and evaluation metrics.
- The reported Hi-CoT gains lack independent validation in the supplied evidence and are not shown to generalize beyond the stated mathematical benchmarks.
- The supplied sources do not adequately assess benchmark contamination, benchmark saturation, replication quality, statistical uncertainty, or evaluator sensitivity as explanations for conflicting results.
- It remains unresolved how often causal-faithfulness findings for structured intermediates or binary-classification tasks transfer to free-form CoT on mathematics, science, coding, and knowledge tasks.
- Direct matched-budget comparisons are lacking for CoT versus hidden scratchpads, answer-only and formatting controls, self-consistency, decomposition, and external tools.

## Conclusion

CoT should be treated as a conditional reasoning intervention, not as a universally effective reasoning strategy and not as merely a formatting trick. It appears beneficial when the prompt and model can exploit intermediate computation, decomposition, or structured search, with reported gains on selected multistep tasks and from structured or pruned reasoning methods. Yet explicit rationales are not reliable proof of faithful internal reasoning: in some strong-model settings they add little beyond zero-shot prompting except output-format alignment, and causal probes show that displayed intermediate content can be post-hoc or non-mediating. The responsible conclusion is therefore mixed: CoT can improve effective problem solving, but its observable rationale may simultaneously function as a presentation, compliance, or evaluation aid. Conflicting findings primarily reflect different models, tasks, prompt variants, computation budgets, causal tests, and evaluators. The supplied evidence does not justify a universal claim about when the rationale itself is the mechanism.

## Sources

- [S1] Hierarchical Chain-of-Thought Prompting: Enhancing LLM ... — https://arxiv.org/html/2604.00130v1
- [S2] What is chain of thought (CoT) prompting? - IBM — https://www.ibm.com/think/topics/chain-of-thoughts
- [S3] Chain of Thought Prompting (CoT): Everything you need to know — https://www.vellum.ai/blog/chain-of-thought-prompting-cot-everything-you-need-to-know
- [S4] Prompt Engineering: Chain of Thought & LLM Performance | Medium — https://medium.com/data-science-collective/so-you-think-you-can-prompt-b3384664bafc
- [S5] Contrastive Chain-Of-Thought Prompting — https://www.kore.ai/blog/contrastive-chain-of-thought-prompting
- [S6] Few-Shot CoT: Enhancing LLM Reasoning — https://www.emergentmind.com/topics/few-shot-cot
- [S7] Revisiting Chain-of-Thought Prompting: Zero-shot Can ... - arXiv — https://arxiv.org/html/2506.14641v3
- [S8] Master Prompting Concepts: Zero-Shot and Few-Shot Prompting — https://promptengineering.org/master-prompting-concepts-zero-shot-and-few-shot-prompting
- [S9] Shot-Based Prompting: Zero-Shot, One-Shot, and Few-Shot Prompting — https://learnprompting.org/docs/basics/few_shot
- [S10] Zero-Shot vs Few-Shot vs Chain-of-Thought Prompting: Complete Guide 2026 | explainx.ai Blog | explainx.ai — https://explainx.ai/blog/zero-shot-few-shot-chain-of-thought-prompting-guide-2026
- [S11] Testing Explainability of Chain of Thought for Large Language Models — https://www.mdpi.com/2076-3417/16/7/3112
- [S12] Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures — https://arxiv.org/html/2603.16475v1
- [S13] Causal Sufficiency and Necessity Improves Chain-of- ... — https://haoxuanli-pku.github.io/papers/NeurIPS%2025%20-%20Causal%20Sufficiency%20and%20Necessity%20Improves%20Chain-of-Thought%20Reasoning.pdf
- [S14] Post-hoc reasoning in chain of thought — LessWrong — https://www.lesswrong.com/posts/ScyXz74hughga2ncZ/post-hoc-reasoning-in-chain-of-thought
- [S15] What is faithful chain-of-thought reasoning and why is it ... — https://blog.bluedot.org/p/faithful-chain-of-thought
