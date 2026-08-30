# Research Run Log

## Run Summary

**Research Question**

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees-find the real fault lines and explain what accounts for the conflicting results.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 12

**OpenAI Calls:** 4

**Tavily Calls:** 3

**Started:** 2026-08-30T17:20:02-04:00

**Ended:** 2026-08-30T17:21:10-04:00

**Total Runtime:** 68.13s

---

# Iteration 1

## 1. Search

**Query**

> Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees-find the real fault lines and explain what accounts for the conflicting results.

**Why this query**

This is the user's original research question.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S1 — Hierarchical Chain-of-Thought Prompting: Enhancing LLM ...**
  URL: https://arxiv.org/html/2604.00130v1
- **S2 — The Decreasing Value of Chain of Thought in Prompting**
  URL: https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought
- **S3 — Contrastive Chain-Of-Thought Prompting**
  URL: https://www.kore.ai/blog/contrastive-chain-of-thought-prompting
- **S4 — What is chain of thought (CoT) prompting?**
  URL: https://www.ibm.com/think/topics/chain-of-thoughts
- **S5 — Medium**
  URL: https://cobusgreyling.medium.com/chain-of-thought-prompting-in-llms-1077164edf97

**Search Duration:** 2.41s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

CoT is not uniformly effective: its value varies by model type, task difficulty, evaluation metric, and latency budget.

**Confidence:** Medium

**Why this confidence level**

The source describes a controlled repeated-trials comparison across several models, but the retrieved material is a technical-report summary rather than the full paper and covers one benchmark.

**Evidence**

- A 2025 GPQA Diamond study reports modest average gains for non-reasoning models, mixed effects on perfect accuracy, and minimal or negative effects for built-in reasoning models, with substantial time costs. [S2]
- The report also finds that many models produce CoT-like reasoning by default, making explicit step-by-step prompting less consequential. [S2]

#### Finding 2

**Claim**

One major fault line is whether the model already has an internal or built-in reasoning procedure. Generic CoT appears more useful for some non-reasoning models than for models designed to reason, where it may add little beyond cost.

**Confidence:** Medium

**Why this confidence level**

The model-type contrast is directly reported, but the evidence is limited to the models and benchmark described.

**Evidence**

- On GPQA Diamond, non-reasoning models showed average improvements ranging from 4.4% to 13.5%, while reasoning models showed only small gains for two models and a decrease for another. [S2]
- The report concludes that generic CoT has limited value compared with built-in reasoning in reasoning models, and that many models reason in their default output. [S2]

#### Finding 3

**Claim**

A second fault line is the distinction between reasoning assistance and output-format control. CoT exemplars may help models adopt an answer format or expose intermediate steps without necessarily improving the underlying solution process.

**Confidence:** Low

**Why this confidence level**

The format-versus-reasoning claim is only reported second-hand in S1; the underlying study is not retrieved. The Hi-CoT results are from a new, apparently non-peer-reviewed arXiv version and concern its own proposed method.

**Evidence**

- The Hi-CoT paper's related-work section states that a cited 2025 study found CoT exemplars primarily enforce output format rather than improve reasoning quality in modern LLMs. [S1]
- The same source presents standard CoT as unstructured and claims that hierarchical planning and execution improve accuracy while shortening traces, suggesting that the structure of the scaffold—not merely producing more text—can matter. [S1]

#### Finding 4

**Claim**

The relevant mechanism may be structured decomposition rather than verbosity. Unstructured CoT can introduce redundancy, drift, and propagation of mistaken intermediate steps, whereas explicit planning and local execution are claimed to improve coherence and efficiency.

**Confidence:** Low

**Why this confidence level**

These are mechanism claims from a proposal paper and an industry blog, not an independent synthesis or controlled causal comparison in the retrieved material.

**Evidence**

- S1 characterizes flat CoT as vulnerable to repetition, wandering, plan-execution drift, and error propagation, and describes hierarchical instruction/execution as compression bottlenecks that filter low-information content. [S1]
- S3 states that invalid intermediate demonstrations can propagate wrong assumptions down the chain and motivates contrastive positive/negative demonstrations as an improvement. [S3]

#### Finding 5

**Claim**

CoT can improve average accuracy while reducing consistency or harming already-easy cases, so conclusions depend on whether the metric is mean accuracy, majority accuracy, perfect accuracy, variance, or cost-adjusted performance.

**Confidence:** Medium

**Why this confidence level**

The source directly reports repeated-trial and threshold-dependent effects, though generalization beyond GPQA Diamond remains uncertain.

**Evidence**

- S2 reports average gains for several non-reasoning models but significant declines for some models under a 100%-correct criterion, and explicitly says CoT can increase answer variability. [S2]
- The study tested each question 25 times and used multiple correctness thresholds, arguing that one-shot benchmark comparisons can hide inconsistency. [S2]

#### Finding 6

**Claim**

The retrieved evidence supports a conditional conclusion, not a binary verdict: CoT can be an effective reasoning scaffold for some difficult multistep tasks and models, but generic 'think step by step' prompting is not reliably beneficial and may primarily affect presentation or induce costly, variable traces in other settings.

**Confidence:** Medium

**Why this confidence level**

The conditional pattern is consistent across the retrieved sources, but the strongest evidence for the format-only interpretation is missing and several sources are explanatory or vendor-authored.

**Evidence**

- IBM and an explanatory article describe CoT as decomposition into intermediate steps for multistep reasoning, while S2 reports model- and task-dependent gains and S1 reports that more structured variants can outperform flat CoT. [S4] [S5] [S1] [S2]
- S2 reports explicit latency increases of 35–600% for non-reasoning models and 20–80% for reasoning models, despite often small or inconsistent accuracy gains. [S2]

### Conflicts Found

- S4 and S5 present CoT as a generally effective step-by-step reasoning technique, whereas S2 finds benefits that are model- and metric-dependent, with negligible or negative effects in some conditions. [S4] [S5] [S2]
- S1 reports strong, broad gains from a hierarchical CoT variant and frames flat CoT as structurally deficient, while S2 finds that generic CoT often yields marginal benefits for reasoning models. This is a conditional rather than direct contradiction because the methods, models, benchmarks, and prompts differ. [S1] [S2]
- S1 relays the claim that CoT exemplars primarily enforce output format, but the retrieved S1 text does not provide the underlying study's methods or results; this conflicts with the stronger causal reasoning claims in S4/S5 only at the level of interpretation, not directly comparable experiments. [S1] [S4] [S5]

### Important Gaps

- What is the underlying 2025 study cited by S1 that separates formatting effects from genuine reasoning gains, and how does it operationalize those two outcomes?
- Do CoT gains survive controls that equalize output length, answer format, token budget, and opportunity to deliberate?
- How much do demonstrations, wording, self-consistency, verifier/tool use, and structured planning contribute separately from merely requesting an explanation?
- Are the reported effects robust across arithmetic, symbolic, commonsense, scientific, and open-ended tasks rather than primarily GPQA or mathematics benchmarks?
- Do generated CoT traces faithfully represent the causal process producing the answer, or can they be post-hoc rationalizations?
- How should CoT be evaluated when it improves majority accuracy but increases variance, latency, and token cost?

**Analysis Duration:** 15.87s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The central format-versus-reasoning issue is not resolved by the retrieved material. The strongest negative evidence is a single technical report on GPQA, while the strongest positive evidence for structured CoT comes from a new proposal paper. A focused search for controlled studies that equalize formatting and length, and test reasoning faithfulness, would materially improve the answer.

**Next Search**

> chain-of-thought prompting formatting effect reasoning ability controlled study equalized output format length faithfulness

---

# Iteration 2

## 1. Search

**Query**

> chain-of-thought prompting formatting effect reasoning ability controlled study equalized output format length faithfulness

**Why this query**

The central format-versus-reasoning issue is not resolved by the retrieved material. The strongest negative evidence is a single technical report on GPQA, while the strongest positive evidence for structured CoT comes from a new proposal paper. A focused search for controlled studies that equalize formatting and length, and test reasoning faithfulness, would materially improve the answer.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S6 — Chain of Thought Prompting Guide**
  URL: https://medium.com/@dan_43009/chain-of-thought-prompting-guide-3fdfd1972e03
- **S7 — Chain-of-Thought Prompting**
  URL: https://learnprompting.org/docs/intermediate/chain_of_thought
- **S8 — Chain of Thought Prompting Guide**
  URL: https://www.prompthub.us/blog/chain-of-thought-prompting-guide

**Search Duration:** 2.05s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources mainly repeat the conventional view that CoT can improve performance on difficult multistep tasks, especially when demonstrations show intermediate steps, but they do not materially establish the causal mechanism.

**Confidence:** Medium

**Why this confidence level**

The sources consistently describe the standard CoT paradigm, but they are explanatory guides rather than independent primary studies, and their numerical claims are not fully documented in the retrieved text.

**Evidence**

- S7 describes CoT as improving arithmetic, commonsense, and symbolic reasoning, and reports historical benchmark improvements for PaLM 540B over direct prompting. [S7]
- S6 presents CoT as a widely used method involving either a simple step-by-step instruction or few-shot reasoning demonstrations, and claims that few-shot CoT can outperform zero-shot CoT. [S6]
- S8 similarly describes CoT as decomposition into intermediate steps and discusses zero-shot, few-shot, self-consistency, contrastive, and faithful variants. [S8]

#### Finding 2

**Claim**

CoT effectiveness is strongly conditional on model scale and model capability, rather than being a universal prompting effect.

**Confidence:** Medium

**Why this confidence level**

The sources support a model-dependent fault line, but S7 summarizes older results and S2 covers one modern benchmark, so the exact boundary conditions remain uncertain.

**Evidence**

- S7 states that the original CoT results depended primarily on very large models, reporting that smaller models could generate illogical chains and perform worse than with standard prompting. [S7]
- S2 finds that explicit CoT produced larger gains for some non-reasoning models but small, mixed, or negative effects for built-in reasoning models. [S2]

#### Finding 3

**Claim**

The apparent disagreement is partly produced by comparing different CoT interventions: zero-shot instructions, few-shot demonstrations, self-consistency, and structured or faithful variants are not interchangeable.

**Confidence:** Medium

**Why this confidence level**

The intervention distinction is explicit in the sources and helps explain conditional results, but the retrieved material does not provide a controlled factorial comparison isolating each component.

**Evidence**

- S6 and S8 distinguish simple 'think step by step' instructions from few-shot demonstrations and self-consistency, while S8 also describes contrastive, faithful, and tabular variants. [S6] [S8]
- S1 argues that hierarchical planning and execution can outperform flat CoT, suggesting that explicit structure may contribute independently of merely requesting a visible reasoning trace. [S1]
- S2 evaluates generic CoT and reports limited benefits for some reasoning models, making it inappropriate to generalize those results to structured variants. [S2]

#### Finding 4

**Claim**

The new sources do not resolve whether CoT improves latent reasoning or primarily changes output format and answer presentation.

**Confidence:** High

**Why this confidence level**

The evidence gap is direct: the new sources provide descriptive claims and caveats but no decisive causal control. The unresolved format-versus-reasoning question remains.

**Evidence**

- S6, S7, and S8 interpret intermediate steps as reasoning and cite improved benchmark results, but do not control for output length, formatting, demonstrations, token budget, or answer-selection procedures. [S6] [S7] [S8]
- S1 relays the contrary claim that modern CoT exemplars may primarily enforce output format, but the underlying study is not included in the retrieved evidence. [S1]
- S8 explicitly acknowledges that generated reasoning chains may not be faithful to the process producing the final answer, weakening the inference from visible explanations to genuine reasoning. [S8]

#### Finding 5

**Claim**

Metric and evaluation design remain major fault lines: historical average-accuracy gains do not establish consistent, cost-effective, or faithful reasoning improvements.

**Confidence:** Medium

**Why this confidence level**

S2 supplies direct repeated-trial and cost evidence, while the guides illustrate why popular positive results may use different budgets and metrics. Cross-benchmark generality is still unresolved.

**Evidence**

- S7 reports large historical gains for PaLM 540B on selected benchmarks, but does not discuss repeated trials, variance, latency, or cost-adjusted performance. [S7]
- S2 reports model- and threshold-dependent effects, increased variability, and substantial latency costs, including cases where CoT reduced perfect accuracy. [S2]
- S6 says self-consistency can improve reliability by sampling multiple chains, but this changes the inference budget and therefore is not a free comparison with direct prompting. [S6]

### Conflicts Found

- S7 presents large historical gains from CoT on PaLM 540B, while S2 finds modest, mixed, or negative effects for some modern models and evaluation criteria. This is a conditional disagreement involving different model generations, benchmarks, and metrics rather than a direct replication conflict. [S7] [S2]
- S6-S8 portray CoT as a reasoning-enhancing technique, whereas S1 relays evidence that CoT exemplars may primarily impose an output format. The conflict is interpretive and cannot be adjudicated because the underlying format-control study is absent. [S6] [S7] [S8] [S1]
- S7 says CoT gains are mainly associated with very large models, while S2 finds useful gains for several modern non-reasoning models. The difference may reflect changes in model training and architecture, but the sources do not directly test that explanation. [S7] [S2]

### Important Gaps

- What is the primary study cited by S1 that separates output-format effects from genuine reasoning gains?
- Do CoT improvements remain after equalizing output length, token budget, answer format, and inference computation?
- How much of the benefit comes from demonstrations, decomposition, self-consistency, or structured planning rather than from producing a visible chain?
- Are the effects robust across task families and modern model architectures, rather than selected historical benchmarks or GPQA Diamond?
- Are CoT traces causally faithful, or can correct answers be accompanied by inaccurate or post-hoc explanations?

**Analysis Duration:** 12.64s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources add useful context about model scale and intervention variants, but they are largely secondary guides and do not answer the central causal question. The most valuable next step is to retrieve the underlying study cited by S1 and inspect its experimental controls.

**Next Search**

> "CoT exemplars" "output format" reasoning quality 2025 study

---

# Iteration 3

## 1. Search

**Query**

> "CoT exemplars" "output format" reasoning quality 2025 study

**Why this query**

The new sources add useful context about model scale and intervention variants, but they are largely secondary guides and do not answer the central causal question. The most valuable next step is to retrieve the underlying study cited by S1 and inspect its experimental controls.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S9 — Chain-of-Thought (CoT) Prompting - Prompt Engineering Guide**
  URL: https://www.promptingguide.ai/techniques/cot
- **S10 — Chain of Thought Prompting Explained (with examples) | Codecademy**
  URL: https://www.codecademy.com/article/chain-of-thought-cot-prompting
- **S11 — [PDF] Structured Chain-of-Thought Prompting for Code Generation - Ge Li**
  URL: https://ligechina.github.io/My%20Papers/2025%20-%20TOSEM%20-%20Structured%20Chain-of-Thought%20Prompting%20for%20Code%20Generation.pdf
- **S12 — Chain-of-thought (CoT) prompting: Complete overview**
  URL: https://www.superannotate.com/blog/chain-of-thought-cot-prompting

**Search Duration:** 1.62s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources do not resolve the central format-versus-reasoning question; most are instructional summaries that assume visible intermediate steps reflect reasoning rather than testing that causal claim.

**Confidence:** High

**Why this confidence level**

The sources are descriptive guides rather than controlled causal studies, and their stated benefits cannot distinguish reasoning improvement from presentation or prompting effects.

**Evidence**

- S9, S10, and S12 describe CoT as enabling or improving reasoning and present illustrative examples, but do not report controls for output format, length, token budget, inference compute, or answer-selection procedures. [S9] [S10] [S12]
- S12 acknowledges that model explanations may not match the process that produced the answer, while still presenting CoT as more transparent and reliable. [S12]
- The accumulated evidence already identifies the underlying format-control study as missing; the new sources do not supply it. [S1] [S6] [S7] [S8] [S9] [S10] [S12]

#### Finding 2

**Claim**

Structured intermediate representations may matter more than generic verbosity, at least for code generation.

**Confidence:** Medium

**Why this confidence level**

S11 is a primary, published study with multiple benchmarks, but it concerns code generation and does not isolate structure from all other prompt differences or establish generality to reasoning tasks.

**Evidence**

- The peer-reviewed SCoT study reports that ordinary CoT produces only slight code-generation improvements in one cited setting, while its structured variant explicitly represents sequence, branch, and loop structures and outperforms ordinary CoT by up to 13.79% Pass@1 across HumanEval, MBPP, and MBCPP. [S11]
- S11 characterizes ordinary natural-language CoT as verbose and limited in representing branch and loop structure, whereas SCoT is designed as a concise midpoint between natural language and code. [S11]
- This supports the accumulated hypothesis that decomposition structure—not simply generating a longer explanation—can account for some gains. [S1] [S11]

#### Finding 3

**Claim**

The literature's apparent disagreement is partly due to comparing generic CoT with specialized scaffolds that encode task-relevant structure.

**Confidence:** High

**Why this confidence level**

The sources explicitly describe materially different interventions, although they do not provide a full factorial experiment separating each component.

**Evidence**

- S11 compares flat natural-language CoT with a programming-structured scaffold tailored to code and reports materially larger gains for the latter. [S11]
- S9 and S10 distinguish zero-shot instructions, few-shot demonstrations, and Auto-CoT, while the accumulated sources also distinguish self-consistency and hierarchical variants. [S9] [S10] [S6] [S8] [S1]
- Therefore, a result for 'CoT' may reflect the wording, demonstrations, structure, or additional sampling procedure rather than a single common intervention. [S1] [S6] [S8] [S9] [S10] [S11]

#### Finding 4

**Claim**

Positive demonstrations can teach a solution format and procedure, but the new examples do not establish that the model has acquired a more reliable latent reasoning capability.

**Confidence:** High

**Why this confidence level**

The prompt examples directly show format and rationale imitation, while the arithmetic error provides concrete evidence that visible stepwise text is not automatically valid reasoning.

**Evidence**

- S9 and S10 show that few-shot examples lead models to reproduce stepwise answer patterns, and S9 describes Auto-CoT as generating demonstrations with selected lengths and numbers of steps. [S9] [S10]
- These demonstrations conflate several effects: task-specific examples, expected answer formatting, decomposition cues, and extra prompt tokens. [S9] [S10]
- S10 contains an arithmetic error in its worked example ('3+4 is 12'), illustrating that a plausible-looking rationale can itself be incorrect and should not be treated as direct evidence of reasoning. [S10]

#### Finding 5

**Claim**

The new evidence strengthens a conditional conclusion: generic CoT is not a universally effective reasoning strategy; task-aligned structured scaffolds can help, while ordinary CoT may yield small or inconsistent gains and impose verbosity costs.

**Confidence:** Medium

**Why this confidence level**

The conditional pattern is consistent with the strongest retrieved primary evidence and prior findings, but the format-only causal comparison and broad cross-task replication remain absent.

**Evidence**

- S11 reports slight gains from standard CoT in code generation but larger gains from structured CoT, including up to 13.79% Pass@1 improvement over ordinary CoT. [S11]
- S2 reports modest, mixed, or negative effects of generic CoT depending on model and metric, with substantial latency costs. [S2]
- S9, S10, and S12 present broad positive claims, but they are guides and examples rather than independent controlled evaluations. [S9] [S10] [S12]

### Conflicts Found

- S9, S10, and S12 present CoT as broadly reasoning-enhancing and often more accurate, whereas S2 reports model-, task-, metric-, and cost-dependent effects including negligible or negative outcomes. The sources use different evidentiary standards: instructional summaries versus repeated-trial evaluation. [S2] [S9] [S10] [S12]
- S11 reports substantial gains for a structured code-specific scaffold over ordinary CoT, while S2 finds generic CoT has limited value for some built-in reasoning models. This is a conditional disagreement, not a direct replication conflict, because the task, scaffold, models, and evaluation differ. [S2] [S11]
- S10's claim that a worked example teaches a correct reasoning sequence is weakened by an arithmetic mistake in the example itself, showing that demonstration quality can be a source of both gains and errors. [S10]

### Important Gaps

- What is the primary study cited by S1 that directly tests whether CoT exemplars improve reasoning or mainly enforce output format?
- Do CoT gains survive equalization of output length, answer format, token budget, and total inference computation?
- In S11, how much of the SCoT improvement comes specifically from programming structure rather than prompt wording, additional constraints, or differences in generated-token allocation?
- Are the effects observed in code generation transferable to arithmetic, symbolic, commonsense, scientific, and open-ended reasoning?
- Are correct CoT traces causally faithful, or can models generate incorrect or post-hoc rationales alongside correct answers?
- How do demonstrations, decomposition, structured planning, self-consistency, and verifier/tool use contribute independently?

**Analysis Duration:** 17.55s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The runner reached the maximum research iteration budget. Analyzer assessment: An important causal fault line remains unanswered: the retrieved material still lacks the primary controlled study that separates formatting and demonstration effects from genuine reasoning gains. S11 adds useful evidence that task-specific structure can outperform flat CoT, but it does not perform the necessary format-, length-, and compute-controlled comparison.

**Stop Reason:** max_iterations

---

# Final Research Decision

**Research Stopped Because**

The runner reached the maximum research iteration budget.

**Stop Reason:** max_iterations

**Searches Performed:** 3

**Unique Sources:** 12

**Remaining Uncertainty**

- The primary 2025 study cited by S1 separating output-format effects from genuine reasoning gains was not retrieved.
- No accumulated source provides a comparison equalizing output length, answer format, token budget, and total inference computation.
- The transferability of code-specific structured-CoT results to arithmetic, symbolic, commonsense, scientific, and open-ended reasoning remains unknown.
- The evidence does not establish whether CoT traces are causally faithful, rather than post-hoc or stylistically generated explanations.
- The research stopped at the iteration limit, so these unresolved causal questions should not be treated as answered.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 6.08s |
| OpenAI Analysis | 3 | 46.07s |
| Report Generation | 1 | 15.96s |
| Total Run | — | 68.13s |
