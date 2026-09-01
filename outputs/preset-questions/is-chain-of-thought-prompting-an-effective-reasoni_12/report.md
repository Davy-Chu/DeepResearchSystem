# Research Report

## Research Question

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

## Summary

Chain-of-thought (CoT) is neither universally effective reasoning nor merely formatting. It can improve accuracy, especially for difficult multistep tasks and earlier or non-reasoning models, but its incremental value depends on what is being compared: few-shot rationale demonstrations, a generic step-by-step instruction, extra serial computation, or process-aware search are different interventions. For strong modern reasoning models, few-shot exemplars may add little beyond output-format alignment. Meanwhile, visible rationales are not guaranteed to faithfully represent the computation that produced an answer, and answer formatting can distort both performance and faithfulness measurements.

## Findings

### Finding 1

**Claim**

CoT can produce substantial reasoning gains, but the gains are conditional on model generation, task, and baseline capability.

**Confidence:** High

**Why this confidence level**

The conclusion is supported by both the original research account and later comparative studies, although the studies use different models, tasks, and protocols.

**Evidence**

- The original CoT work reported substantial improvements on multistep arithmetic and some commonsense tasks for sufficiently large models, including a reported 58% GSM8K result for PaLM 540B and benefits emerging at roughly 100B-plus scale. [S22]
- A later GPQA study found average gains for several non-reasoning models, but mixed or negative effects under stricter accuracy criteria and minimal gains for reasoning-native models. [S1]
- The published EMNLP 2025 study found that recent Qwen2.5 models did not gain reasoning performance from adding few-shot CoT exemplars to zero-shot CoT on GSM8K and MATH. [S30]

### Finding 2

**Claim**

For strong contemporary mathematical-reasoning models, few-shot CoT exemplars can primarily serve output-format and response-alignment functions rather than supplying additional reasoning capability.

**Confidence:** High

**Why this confidence level**

S30 is a published empirical study directly comparing the relevant conditions, though its result is limited mainly to recent models and mathematical benchmarks.

**Evidence**

- The EMNLP 2025 study reports that traditional and enhanced rationale exemplars failed to improve over zero-shot CoT for recent Qwen2.5 models; it concludes that exemplars mainly align output format and that models focus on instructions while often ignoring exemplar content. [S30]
- The study also identifies an evaluation bias in common GSM8K frameworks that underestimates zero-shot CoT, which can create an artificial appearance of few-shot superiority. [S30]
- Few-shot CoT demonstrations inherently combine rationale content with task examples, response structure, answer placement, and stylistic cues, so their effects are not automatically attributable to reasoning. [S23] [S24] [S25]

### Finding 3

**Claim**

The formatting-only explanation is too broad: some structured intermediate computation appears to contribute beyond verbosity or presentation.

**Confidence:** Medium

**Why this confidence level**

These results support a computational contribution, but S8 and S13 evaluate specialized systems rather than isolating ordinary free-form CoT alone, and S10 covers a particular model/task regime.

**Evidence**

- Lanham et al. report that replacing CoT with uninformative filler did not reproduce the performance gain in their tested setting, while paraphrased CoT performed similarly, suggesting that neither mere token count nor exact wording fully explains the effect there. [S10]
- CoT2-Meta reports improvements over single-path, sampling, and search baselines under its reported matched inference budgets, attributing gains to selective expansion, pruning, repair, stopping, and abstention rather than simply generating more text. [S13]
- Faithful CoT improves over standard CoT by translating natural-language problems into symbolic reasoning chains executed by a deterministic solver, making the intermediate derivation computationally binding. [S8]

### Finding 4

**Claim**

Visible CoT is not guaranteed to be a faithful explanation of the causal process producing the answer.

**Confidence:** High

**Why this confidence level**

Multiple intervention and architectural studies converge on the distinction between useful reasoning output and faithful explanation, although their operational definitions of faithfulness differ.

**Evidence**

- Interventions that truncate, corrupt, or paraphrase chains produce strongly task-dependent changes in answers; models sometimes rely heavily on displayed CoT and sometimes largely ignore it. The study also reports lower faithfulness for larger models on many tasks examined. [S10]
- Misleading-hint studies find substantial divergence between what reasoning models acknowledge in thinking tokens and what they acknowledge in visible answers; one study explicitly states that its keyword analysis measures channel divergence rather than faithfulness itself. [S6] [S7]
- CASE formalizes the possibility of a direct instruction-to-answer shortcut and reports improved faithfulness after training and attention-masking interventions designed to force greater dependence on the reasoning chain. [S15]

### Finding 5

**Claim**

Formatting and answer placement can produce misleading evidence about whether reasoning is being used.

**Confidence:** Medium

**Why this confidence level**

The ablations directly support a formatting/readout confound, but their scope is primarily explicit-answer-line formats and tested open-weight models.

**Evidence**

- A corruption study reports that when benchmark chains end with an explicit terminal answer line, measured sensitivity often tracks the location of that answer text: removing the final answer statement while preserving the reasoning sharply reduces apparent suffix importance, and models may follow a wrong terminal answer over correct intermediate reasoning. [S9]
- This creates tension with studies that interpret answer changes after truncation or corruption as evidence that intermediate CoT is causally used. [S9] [S10]

### Finding 6

**Claim**

The real fault line is between surface CoT, latent computation, and generic serial compute—not between two universally valid camps of 'reasoning' and 'formatting.'

**Confidence:** High

**Why this confidence level**

The distinction is explicit in S14 and consistently reflected in the empirical differences across the other sources.

**Evidence**

- A position paper explicitly separates surface trace content, latent task-relevant state trajectories, and generic serial computation, arguing that ordinary CoT often changes all three at once. [S14]
- The accumulated studies compare different interventions: few-shot rationale demonstrations, generic step-by-step prompts, default model behavior, filler tokens, budget forcing, and process-aware search. [S1] [S8] [S10] [S11] [S13]
- The evidence that default outputs may already be CoT-like, that reasoning-native models need less prompting, and that budget increases can plateau or hurt all indicates that 'more visible steps' is not a single causal treatment. [S1] [S11]

### Finding 7

**Claim**

Evaluation design is a major reason the literature appears inconsistent.

**Confidence:** High

**Why this confidence level**

These are direct methodological findings that explain how positive, neutral, and negative results can coexist without a simple contradiction.

**Evidence**

- Repeated-trial GPQA evaluation showed that average accuracy, majority correctness, and strict perfect-accuracy criteria can lead to different conclusions; CoT may improve average performance while increasing variability or reducing perfect consistency for some models. [S1]
- The EMNLP study reports that a GSM8K evaluation artifact underestimated zero-shot CoT performance, potentially inflating apparent few-shot benefits. [S30]
- Formatting-sensitive corruption protocols can attribute effects to answer placement rather than intermediate computation. [S9]

### Finding 8

**Claim**

The practical value of CoT should be evaluated as an accuracy–reliability–cost tradeoff, not accuracy alone.

**Confidence:** Medium

**Why this confidence level**

The cost and model-dependence findings are directly reported, but the retrieved material does not provide a unified cost-normalized comparison across all CoT variants.

**Evidence**

- The GPQA study reports substantially longer response times for both non-reasoning and reasoning models under CoT, with 20–80% additional time for reasoning-native models and larger increases in some non-reasoning conditions. [S1]
- Budget-forcing results show that additional reasoning budget helps some model families but produces plateaus, fluctuations, or negative gains for others; the keyword used to induce continuation is also model-specific. [S11]
- Process-aware control systems report better calibration, selective prediction, repair, and abstention in addition to benchmark accuracy, suggesting that allocation and verification may matter more than uniformly lengthening chains. [S13]

## Conflicts and Uncertainty

- Classic studies report large few-shot CoT gains, while the EMNLP 2025 study finds no incremental reasoning benefit from few-shot exemplars for recent Qwen2.5 models. The most plausible explanation supported by the sources is a shift in model capability and training regime: demonstrations that helped earlier models may be redundant when strong models already reason under zero-shot CoT. [S22] [S30] [S1]
- Some sources describe CoT as the computation itself, while faithfulness-focused studies show that visible rationales can be post-hoc, incomplete, or bypassed. Accuracy improvement and faithful explanation are therefore separate claims. [S10] [S14] [S15] [S23] [S24]
- Filler-token experiments argue against explaining all CoT gains as generic extra time, whereas answer-placement studies show that formatting and readout can dominate some measured effects. These findings concern different interventions and do not identify one universal mechanism. [S9] [S10]
- Matched-budget gains from CoT2-Meta coexist with weak or negative results from simple budget forcing. Selective expansion, verification, repair, and abstention may be useful where uniform additional token generation is not. [S11] [S13]
- Faithfulness rates, thinking-answer divergence rates, and answer sensitivity under corruption are different measurements. They should not be treated as interchangeable evidence for or against faithful reasoning. [S6] [S7] [S9] [S10]
- The strongest formatting-only result is restricted to few-shot exemplars for recent mathematical models, while the strongest evidence for computational benefit often concerns other interventions such as free-form CoT, executable reasoning, or process-aware search. [S8] [S13] [S30]

## Remaining Gaps

- Whether classic few-shot CoT gains survive a fully controlled comparison equalizing rationale length, answer format, terminal-answer placement, demonstrations, decoding, and total test-time computation.
- How much zero-shot CoT itself contributes through latent-state changes, visible intermediate text, generic serial computation, or answer-selection effects.
- Whether the EMNLP 2025 format-alignment result generalizes beyond Qwen2.5, GSM8K, and MATH to coding, planning, commonsense, symbolic, retrieval, and multimodal tasks.
- Whether models can ignore the literal content of exemplars while still benefiting from their latent distributional or formatting effects.
- Whether visible CoT can be causally useful while remaining incomplete or misleading, and whether existing faithfulness measures predict correctness or safety.
- Whether formatting and terminal-answer effects generalize beyond explicit answer-line formats and across larger or proprietary reasoning models.
- Whether the reported matched-budget comparisons equalize all relevant costs, including model computation, controller calls, evaluator calls, generated tokens, and memory use.

## Conclusion

CoT prompting is an effective but conditional strategy—not a universal reasoning switch and not merely a formatting trick. Its clearest historical benefit appears on difficult multistep tasks for sufficiently capable but not already reasoning-native models. For strong modern models, especially in the studied mathematical settings, few-shot rationale exemplars may add little reasoning value beyond standardizing the response format. At the same time, structured intermediate computation, selective search, verification, and executable reasoning can improve accuracy beyond presentation effects. The literature conflicts because it often compares different model generations, tasks, metrics, prompt variants, output formats, and compute budgets, while using different definitions of faithfulness. The defensible operational rule is therefore to test the exact model–task–prompt combination with format-controlled, compute-aware evaluations, and not to treat a fluent visible chain as proof of either reasoning or faithful explanation.

## Sources

- [S1] The Decreasing Value of Chain of Thought in Prompting — https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought
- [S2] What is Chain of Thought (CoT) Prompting? — https://www.nvidia.com/en-us/glossary/cot-prompting
- [S3] What is chain of thought (CoT) prompting? — https://www.ibm.com/think/topics/chain-of-thoughts
- [S4] Chain of Thought Prompting (CoT): Everything you need to know — https://www.vellum.ai/blog/chain-of-thought-prompting-cot-everything-you-need-to-know
- [S5] 8 Chain-of-Thought Techniques To Fix Your AI Reasoning — https://galileo.ai/blog/chain-of-thought-prompting-techniques
- [S6] Why Models Know But Don’t Say:Chain-of-Thought Faithfulness Divergence Between Thinking Tokensand Answers in Open-Weight Reasoning Models — https://arxiv.org/html/2603.26410
- [S7] Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models? — https://arxiv.org/html/2603.22582v1
- [S8] Faithful Chain-of-Thought Reasoning Qing Lyu ∗ Shreya Havaldar∗ Adam Stein∗ — https://www.cis.upenn.edu/~ccb/publications/faithful-chain-of-thought-reasoning.pdf
- [S9] The Last Word Often Wins: A Format Confound in Chain-of-Thought Corruption Studies — https://arxiv.org/html/2605.10799
- [S10] Measuring Faithfulness in Chain-of-Thought Reasoning Tamera Lanham — https://www-cdn.anthropic.com/827afa7dd36e4afbb1a49c735bfbb2c69749756e/measuring-faithfulness-in-chain-of-thought-reasoning.pdf
- [S11] Wait, Do We Need to Wait? Revisiting Budget Forcing for Sequential Test-Time Scaling | ICLR Blogposts 2026 — https://iclr-blogposts.github.io/2026/blog/2026/wait-do-we-need-to-wait
- [S12] Chain-of-Thought Prompting: A Guide for LLM Apps and Agents — https://www.comet.com/site/blog/chain-of-thought-prompting
- [S13] CoT2-Meta: Budgeted Metacognitive Control for Test-Time Reasoning — https://arxiv.org/html/2603.28135v1
- [S14] [PDF] LLM Reasoning Is Latent, Not the Chain of Thought - arXiv — https://arxiv.org/pdf/2604.15726
- [S15] CASE: Causal Alignment and Structural Enforcement for Improving Chain-of-Thought Faithfulness — https://arxiv.org/html/2607.18820v1
- [S16] [Paper Summary] Chain-of-Thought Prompting Elicits Reasoning in Large Language Models — https://dhruvil.substack.com/p/paper-summary-chain-of-thought-prompting
- [S17] What Is Chain-of-Thought Reasoning in LLMs? | VDF AI — https://vdf.ai/resources/chain-of-thought
- [S18] Chain-of-Thought Prompting Explained: The Complete Step-by-Step Guide — https://appliedaihub.org/blog/chain-of-thought-prompting-explained
- [S19] Few-Shot & Chain-of-Thought Prompting — https://www.emergentmind.com/topics/few-shot-and-chain-of-thought-prompting
- [S20] How Chain of Thought (CoT) Prompting Helps LLMs Reason More Like Humans | Splunk — https://www.splunk.com/en_us/blog/learn/chain-of-thought-cot-prompting.html
- [S21] Chain of Thought Prompting Guide — https://www.prompthub.us/blog/chain-of-thought-prompting-guide
- [S22] Language Models Perform Reasoning via Chain of Thought — https://research.google/blog/language-models-perform-reasoning-via-chain-of-thought
- [S23] Few-Shot CoT: Enhancing LLM Reasoning — https://www.emergentmind.com/topics/few-shot-cot
- [S24] Medium — https://gregrobison.medium.com/chain-of-thought-in-large-language-models-elicited-reasoning-or-constrained-imitation-5e4ee0c811ad
- [S25] Chain-of-Thought (CoT) Prompting — https://www.promptingguide.ai/techniques/cot
- [S26] Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot — https://arxiv.org/html/2506.14641v3
- [S27] Chain of Thought Prompting Guide - Medium — https://medium.com/@dan_43009/chain-of-thought-prompting-guide-3fdfd1972e03
- [S28] Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot — https://arxiv.org/html/2506.14641
- [S29] Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot — https://arxiv.org/html/2506.14641v1
- [S30] [PDF] Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger ... — https://aclanthology.org/2025.findings-emnlp.729.pdf
- [S31] [PDF] Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger ... — https://openreview.net/pdf/4401d48b1ca2a45307cd7e3d2b2e5b079270c496.pdf
