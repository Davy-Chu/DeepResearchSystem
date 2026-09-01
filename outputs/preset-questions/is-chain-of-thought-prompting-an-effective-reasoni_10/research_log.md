# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 10 / 10

**Unique Sources:** 28

**OpenAI Calls:** 11

**Tavily Calls:** 10

**Started:** 2026-09-01T03:52:47-04:00

**Ended:** 2026-09-01T03:56:06-04:00

**Total Runtime:** 198.89s

---

# Iteration 1

## 1. Search

**Query**

> Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

**Why this query**

This is the user's original research question.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S1 — Hierarchical Chain-of-Thought Prompting: Enhancing LLM Reasoning Performance and Efficiency**
  URL: https://arxiv.org/html/2604.00130v1
- **S2 — What is chain of thought (CoT) prompting? - IBM**
  URL: https://www.ibm.com/think/topics/chain-of-thoughts
- **S3 — Chain of Thought Prompting (CoT): Everything you need to know**
  URL: https://www.vellum.ai/blog/chain-of-thought-prompting-cot-everything-you-need-to-know
- **S4 — Contrastive Chain-Of-Thought Prompting**
  URL: https://www.kore.ai/blog/contrastive-chain-of-thought-prompting
- **S5 — The Decreasing Value of Chain of Thought in Prompting**
  URL: https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought

**Search Duration:** 2.60s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

CoT is not uniformly effective: its value depends strongly on model type, task difficulty, and evaluation metric.

**Confidence:** Medium

**Why this confidence level**

The Wharton report provides a comparatively detailed experiment, but the retrieved material is a technical-report summary rather than the full peer-reviewed paper. S3 is secondary corroboration.

**Evidence**

- A 2025 GPQA Diamond study reports modest average gains for non-reasoning models, but mixed effects on perfect accuracy; reasoning models receive only marginal gains or sometimes regress. [S5]
- A practitioner overview likewise reports that CoT is more useful for non-reasoning models and complex tasks, while newer reasoning-native models often already produce structured reasoning. [S3]

#### Finding 2

**Claim**

For non-reasoning models, CoT can improve difficult-task accuracy, but it can also increase answer variability and reduce performance on items the model could otherwise answer directly.

**Confidence:** Medium

**Why this confidence level**

The source gives concrete experimental details and metric distinctions, but independent replication is not present in the retrieved set.

**Evidence**

- On GPQA Diamond, the reported average improvements for non-reasoning models ranged from 4.4% to 13.5%, while some models declined on the 100%-correct metric; Gemini Pro 1.5 reportedly fell by 17.2%. [S5]
- The study tested each question 25 times and found that one-shot evaluation can hide inconsistency; CoT increased variability in some conditions. [S5]

#### Finding 3

**Claim**

For reasoning-native models, generic ‘think step by step’ prompting appears to add little reasoning ability and imposes a substantial latency/token cost.

**Confidence:** Medium

**Why this confidence level**

The experimental result is fairly direct, but it covers one benchmark and a limited model sample.

**Evidence**

- The Wharton study reports only 2.9% and 3.1% average gains for two reasoning models, a 3.3% decline for another, and 20–80% longer response times. [S5]
- S3 states that newer reasoning models incorporate step-by-step reasoning natively, making explicit CoT prompting less necessary. [S3]

#### Finding 4

**Claim**

Some apparent CoT benefits may be caused by output-format or response-policy effects rather than improved underlying reasoning.

**Confidence:** Low

**Why this confidence level**

The key formatting claim is only cited indirectly through S1’s related-work summary; the underlying study was not retrieved. S3 is explanatory rather than empirical.

**Evidence**

- The Hi-CoT paper’s related-work section explicitly reports a 2025 result that CoT exemplars for modern LLMs primarily enforce output format rather than improve reasoning quality. [S1]
- CoT changes the requested response from a direct answer to an answer with intermediate steps; S3 describes separating hidden reasoning from the surfaced final answer, underscoring that reasoning generation and displayed formatting can be distinct interventions. [S1] [S3]

#### Finding 5

**Claim**

Structured variants of CoT can outperform unstructured CoT, suggesting that some disagreements concern the design of the reasoning scaffold rather than whether intermediate tokens are intrinsically useful.

**Confidence:** Low

**Why this confidence level**

The results come primarily from a single, apparently very recent preprint and a commercial blog; the retrieved evidence does not establish independent replication or isolate formatting from reasoning.

**Evidence**

- Hi-CoT alternates planning and execution and reports a 6.2% average accuracy improvement and a 13.9% shorter trace relative to ordinary CoT across 13 model configurations and five mathematical benchmarks. [S1]
- S1 attributes the proposed gains to compression bottlenecks, adaptive planning, reduced redundancy, and less plan–execution drift. [S1]
- Contrastive CoT uses positive and negative demonstrations and is presented as a way to improve reasoning, while noting that invalid intermediate demonstrations can propagate wrong assumptions. [S4]

#### Finding 6

**Claim**

The major fault lines in the reported literature are model regime, task and difficulty, baseline condition, metric, and prompt/scaffold design.

**Confidence:** Medium

**Why this confidence level**

These moderators are directly documented across the retrieved sources, although the evidence base is heterogeneous and includes secondary summaries.

**Evidence**

- S5 compares direct, step-by-step, and default prompting, finding that many models already generate CoT-like reasoning by default; this makes the incremental effect of an explicit instruction depend on the baseline. [S5]
- S5 reports different conclusions for average accuracy, majority correctness, and perfect accuracy, demonstrating metric sensitivity. [S5]
- S1 contrasts flat CoT with hierarchical planning and argues that trace length alone is not evidence of better reasoning. [S1]

### Conflicts Found

- The conventional view says CoT improves reasoning on multistep tasks, whereas the newer critical result says modern CoT exemplars may primarily enforce output format. These claims may both hold under different model/task/prompt regimes, but the retrieved sources do not provide the underlying controlled comparison needed to resolve the issue. [S1] [S2] [S3] [S5]
- Hi-CoT reports large and consistent gains over flat CoT, while the Wharton study finds generic CoT gains small or inconsistent, especially for reasoning models. This is a conditional disagreement involving different tasks, models, and scaffolds rather than a clean contradiction. [S1] [S5]
- S2 and S3 present CoT as a generally effective reasoning technique, while S5 finds that it can harm perfect accuracy and adds substantial latency. The discrepancy likely reflects explanatory/practical summaries versus controlled repeated-trial evaluation. [S2] [S3] [S5]

### Important Gaps

- Does CoT improve latent problem-solving competence, or mainly induce a response format that makes already-available computation visible?
- What is the underlying 2025 study claiming that modern CoT exemplars primarily enforce output format, and does it control for answer length, parsing format, hidden reasoning, and additional token budget?
- How much of Hi-CoT’s reported improvement comes from hierarchical planning/compression versus simply changing the number and distribution of generated tokens?
- Do CoT effects generalize beyond GPQA and mathematical benchmarks to knowledge-intensive, adversarial, compositional, and real-world tasks?
- How do prompt wording, demonstrations, sampling temperature, answer parsing, and repeated-trial aggregation affect the reported results?

**Analysis Duration:** 18.73s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The central formatting-versus-reasoning claim is supported only indirectly, and the retrieved evidence does not include the primary comparative literature needed to explain the disagreement mechanistically. A focused search for that primary study and controlled evaluations would materially improve the answer.

**Next Search**

> chain-of-thought prompting output format rather than reasoning quality Cheng 2025 study

---

# Iteration 2

## 1. Search

**Query**

> chain-of-thought prompting output format rather than reasoning quality Cheng 2025 study

**Why this query**

The central formatting-versus-reasoning claim is supported only indirectly, and the retrieved evidence does not include the primary comparative literature needed to explain the disagreement mechanistically. A focused search for that primary study and controlled evaluations would materially improve the answer.

**Results**

5 results retrieved.

2 new unique sources added.

### Sources

- **S6 — Chain of Thought Prompting Guide**
  URL: https://www.prompthub.us/blog/chain-of-thought-prompting-guide
- **S7 — So you think you can prompt?**
  URL: https://medium.com/data-science-collective/so-you-think-you-can-prompt-b3384664bafc

**Search Duration:** 1.68s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources support the view that CoT can improve benchmark performance, especially when tasks are multi-step and models are sufficiently capable, but they do not establish that the improvement reflects a general increase in latent reasoning ability.

**Confidence:** Low

**Why this confidence level**

Both sources are secondary, non-peer-reviewed explainers that largely repeat the conventional CoT interpretation; neither isolates reasoning improvement from formatting, extra tokens, or answer-selection effects.

**Evidence**

- S6 describes CoT as breaking complex tasks into intermediate steps and presents few-shot CoT, self-consistency, and related methods as ways to improve outputs; it also acknowledges that reasoning chains may be incorrect or unfaithful. [S6]
- S7 summarizes the original CoT literature as finding gains over standard few-shot prompting on arithmetic and some common-sense and symbolic tasks, particularly at larger model scales. [S7]

#### Finding 2

**Claim**

Prompt and scaffold design are themselves major sources of variance in CoT results, beyond the binary question of whether CoT is used.

**Confidence:** Medium

**Why this confidence level**

The sources directly document many prompt variants and prompt sensitivity, but they do not provide a controlled decomposition of which design feature causes each gain.

**Evidence**

- S6 distinguishes zero-shot, few-shot, self-consistency, automatic, contrastive, faithful, tabular, analogical, and other CoT variants, indicating that different interventions change both the reasoning process and the output structure. [S6]
- S7 reports large performance variation across semantically similar prompts and describes CoT results as depending on exemplar selection, order, and number, although it characterizes the original findings as comparatively robust. [S7]

#### Finding 3

**Claim**

Visible reasoning is not a reliable proxy for faithful or improved internal reasoning; CoT may produce plausible explanations that diverge from the actual basis of the answer.

**Confidence:** Medium

**Why this confidence level**

The unfaithfulness caveat is explicit in S6 and consistent with the prior formatting concern, but the retrieved material lacks a direct causal experiment comparing displayed explanations with hidden or independently verified reasoning.

**Evidence**

- S6 explicitly states that reasoning chains are not always faithful or correct and describes faithful CoT as a separate method intended to align reasoning with the final answer. [S6]
- The prior evidence reports that modern CoT exemplars may primarily enforce output format, while S6 frames showing intermediate steps as both an accuracy intervention and a transparency feature. [S1] [S6]

#### Finding 4

**Claim**

The added sources do not materially overturn the existing fault-line analysis: model regime, task difficulty, baseline prompting, metric, token budget, and scaffold design remain the most plausible explanations for conflicting results.

**Confidence:** Medium

**Why this confidence level**

The new sources are consistent with the accumulated findings, but are too informal and derivative to strengthen the causal conclusion substantially.

**Evidence**

- S6 presents CoT as broadly useful but lists numerous variants and notes limitations, while S7 emphasizes prompt-quality sensitivity and scale-dependent results. [S6] [S7]
- The prior controlled GPQA evidence found gains for some non-reasoning models, small or negative incremental effects for reasoning-native models, metric-dependent outcomes, and latency costs; these more specific results are not contradicted by the new sources. [S5]

### Conflicts Found

- S6 and S7 present the conventional conclusion that CoT improves reasoning, whereas the prior evidence includes a critical result that modern CoT exemplars may mainly enforce output format. This remains a conditional disagreement rather than a resolved contradiction because the new sources do not control for extra output tokens, answer formatting, or whether the model already reasons by default. [S1] [S5] [S6] [S7]
- S7 characterizes CoT as relatively robust across exemplar variation, while the prior evidence emphasizes substantial sensitivity to baseline condition, metric, and repeated-trial variability. These claims may refer to different notions of robustness: robustness across selected demonstrations versus stability of individual answers and aggregate accuracy. [S5] [S7]

### Important Gaps

- Does CoT improve problem-solving when answer format, response length, computation/token budget, and sampling procedure are held constant?
- What is the primary underlying study behind the claim that modern CoT exemplars mostly improve output format, and does it directly compare visible CoT with hidden reasoning or equivalent-length non-CoT outputs?
- How much of reported CoT benefit comes from demonstrations, intermediate computation, self-consistency/majority voting, or simply changing the model’s response policy?
- Do the observed effects generalize beyond mathematics, arithmetic, symbolic tasks, and GPQA-style benchmarks?
- Are improvements accompanied by independently verified, faithful intermediate reasoning, or only by higher final-answer accuracy?

**Analysis Duration:** 12.98s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The central causal issue remains unanswered. The new material consists of practitioner and community summaries and mainly repeats established claims; it does not supply the controlled evidence needed to distinguish genuine reasoning gains from formatting, extra-token, demonstration, or aggregation effects.

**Next Search**

> chain-of-thought prompting output format rather than reasoning study controlled comparison answer length token budget faithfulness 2025

---

# Iteration 3

## 1. Search

**Query**

> chain-of-thought prompting output format rather than reasoning study controlled comparison answer length token budget faithfulness 2025

**Why this query**

The central causal issue remains unanswered. The new material consists of practitioner and community summaries and mainly repeats established claims; it does not supply the controlled evidence needed to distinguish genuine reasoning gains from formatting, extra-token, demonstration, or aggregation effects.

**Results**

5 results retrieved.

1 new unique source added.

### Sources

- **S8 — Zhihui Xie's Homepage | Measuring Faithfulness in Chain-of-Thought Reasoning**
  URL: https://zhxie.site/blog/2023-09-19-faithfulness

**Search Duration:** 2.46s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

CoT faithfulness varies substantially by task and is not strongly correlated with CoT’s accuracy gain, so higher benchmark accuracy does not by itself establish that the displayed reasoning caused the improvement.

**Confidence:** Medium

**Why this confidence level**

S8 reports concrete experimental procedures and task-level results, but it is a blog summary of the underlying work rather than the primary paper.

**Evidence**

- The summarized experiments used early-answering and injected-mistake tests; they found wide task variation and little correlation between faithfulness measures and CoT performance gains. AQuA showed strong dependence on continuing the chain, while several ARC and OpenBookQA tasks changed answers less than 10% when CoT was truncated. [S8]

#### Finding 2

**Claim**

The evidence supports separating at least three mechanisms that can be conflated under 'CoT reasoning': genuine stepwise reasoning, extra test-time computation, and post-hoc verbalization of an answer already selected.

**Confidence:** Medium

**Why this confidence level**

The source directly reports the conceptual decomposition and experiments, but the evidence comes from one model and a limited task set.

**Evidence**

- S8 explicitly frames faithfulness tests around post-hoc reasoning, test-time computation, and encoded reasoning. Early answering and mistake injection test whether later text affects the answer, while filler-token replacement tests whether mere additional tokens improve performance. [S8]
- Filler tokens did not improve accuracy in the summarized experiment, weakening the simple claim that any extra token budget is equivalent to useful reasoning. [S8]

#### Finding 3

**Claim**

Visible CoT is not a reliable proxy for the model's actual decision process: some answers appear to be determined before the full explanation is generated, while other tasks rely more heavily on the generated steps.

**Confidence:** Medium

**Why this confidence level**

The findings are relevant direct interventions, but they do not establish a universal account of internal reasoning and are limited to one RLHF-tuned 175B model and eight tasks.

**Evidence**

- Early-answering and mistake-injection results reportedly show low post-hoc reasoning for some tasks and much higher dependence on continued CoT for others; AQuA and LogiQA were described as among the more faithful tasks. [S8]
- The source reports that paraphrasing CoT caused no significant accuracy gap relative to original CoT, making encoded information in the exact wording an unlikely general explanation in that experiment. [S8]

#### Finding 4

**Claim**

The new evidence strengthens the conclusion that the literature's conflict is partly about causal interpretation, not merely whether final-answer accuracy rises: CoT can improve outputs without its displayed steps faithfully representing the causal computation.

**Confidence:** Medium

**Why this confidence level**

S8 supplies an important causal/faithfulness perspective consistent with the prior fault-line analysis, although it does not independently resolve all confounds.

**Evidence**

- CoT improved performance over no CoT on seven of eight reported tasks, yet faithfulness varied widely and was weakly related to the size of the performance gain. [S8]
- The accumulated evidence already distinguishes benchmark gains from latent reasoning claims and reports metric-, baseline-, model-regime-, and scaffold-dependent effects. [S5] [S6] [S7]

#### Finding 5

**Claim**

The most defensible synthesis is conditional: CoT is an effective prompting intervention for some non-reasoning models and difficult tasks, but it is not established as a general-purpose improvement to latent reasoning, and its visible explanation may primarily function as a response scaffold or output policy in some regimes.

**Confidence:** Medium

**Why this confidence level**

Multiple sources support the conditional synthesis, but the key formatting claim remains indirect and the experiments do not fully control for token budget, answer format, and baseline reasoning.

**Evidence**

- S5 reports gains for some non-reasoning models, small or negative incremental effects for reasoning-native models, metric sensitivity, and latency costs. [S5]
- S8 reports that CoT often improves task accuracy while faithfulness varies by task and is not strongly correlated with the gain. [S8]
- S1 and S6 document that CoT variants and structured scaffolds can change results substantially, while S1 relays a newer claim that modern CoT exemplars may mainly enforce output format. [S1] [S6]

### Conflicts Found

- S8 reports that filler tokens alone did not improve accuracy, which argues against a simple 'more tokens equals more computation' explanation. This does not rule out useful computation in semantically structured CoT, so it qualifies rather than directly contradicts the broader claim that CoT can add test-time computation. [S8]
- S8 finds that CoT improves accuracy on most tested tasks but that faithfulness is weakly correlated with the gain. This qualifies conventional interpretations in S6 and S7 that accuracy gains straightforwardly demonstrate improved reasoning; the sources use different standards for 'effective'—output accuracy versus faithful causal reasoning. [S6] [S7] [S8]
- S8's paraphrasing result disfavors exact wording as a carrier of hidden encoded information in its setting, while the accumulated findings leave open that structured intermediate tokens can still alter computation or answer selection. These are not mutually exclusive because paraphrase invariance does not test whether the existence and semantic content of intermediate steps matter. [S8] [S1] [S5]

### Important Gaps

- What is the primary underlying study summarized by S8, and do its results replicate across current frontier models, reasoning-native models, and non-RLHF models?
- Does CoT retain an advantage when answer format, response length, token budget, sampling procedure, and parsing are matched against non-CoT controls?
- How much of CoT's benefit comes from semantic intermediate computation versus demonstrations, changed response policy, self-consistency, or majority voting?
- Can the task-dependent faithfulness patterns in S8 be replicated beyond its eight tasks, especially on knowledge-intensive, adversarial, compositional, and real-world problems?
- What exact controlled evidence supports the claim that modern CoT exemplars primarily improve output format rather than reasoning quality?

**Analysis Duration:** 14.98s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new source materially improves the answer by supplying direct faithfulness tests, but it is a secondary summary of one model and does not resolve the central formatting-versus-reasoning claim or provide the missing controlled comparisons. The highest-value next step is to retrieve the underlying faithfulness paper and the 2025 formatting claim.

**Next Search**

> chain-of-thought exemplars primarily enforce output format rather than improve reasoning quality 2025 study

---

# Iteration 4

## 1. Search

**Query**

> chain-of-thought exemplars primarily enforce output format rather than improve reasoning quality 2025 study

**Why this query**

The new source materially improves the answer by supplying direct faithfulness tests, but it is a secondary summary of one model and does not resolve the central formatting-versus-reasoning claim or provide the missing controlled comparisons. The highest-value next step is to retrieve the underlying faithfulness paper and the 2025 formatting claim.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S9 — 8 Chain-of-Thought Techniques To Fix Your AI Reasoning**
  URL: https://galileo.ai/blog/chain-of-thought-prompting-techniques
- **S10 — Medium**
  URL: https://cobusgreyling.medium.com/a-benchmark-for-verifying-chain-of-thought-904db5ebeefa
- **S11 — Multi-Dimensional Evaluation of Auto-Generated Chain-of- ...**
  URL: https://www.mdpi.com/2673-2688/7/1/35

**Search Duration:** 2.82s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources reinforce the distinction between final-answer correctness and correctness or faithfulness of the displayed reasoning chain.

**Confidence:** Medium

**Why this confidence level**

S10 summarizes a research benchmark and states the distinction directly, but it is a secondary account rather than the primary paper.

**Evidence**

- The REVEAL discussion explicitly notes that an answer can be correct even when its reasoning is incorrect, and describes step-level labels for logical correctness, relevance, and evidence attribution. [S10]

#### Finding 2

**Claim**

CoT evaluation requires verification at the step level; final-answer accuracy alone cannot establish that CoT improved reasoning.

**Confidence:** Medium

**Why this confidence level**

The source gives a concrete evaluation framework relevant to the research question, though it does not itself compare CoT against direct prompting.

**Evidence**

- REVEAL is presented as a benchmark for automated verifiers of complex reasoning chains, motivated by the lack of fine-grained step-level evaluation data. [S10]
- The benchmark separates answer correctness from whether each reasoning step is logically correct and supported by the supplied evidence. [S10]

#### Finding 3

**Claim**

S9 supports the conventional performance-based interpretation of CoT, especially for structured multi-step tasks, but provides little evidence about whether gains reflect genuine reasoning rather than formatting or altered response policy.

**Confidence:** Low

**Why this confidence level**

S9 is a commercial practitioner article, its cited result is not independently established by the retrieved content, and it does not control for answer format, token budget, or faithfulness.

**Evidence**

- The article presents CoT as useful for multi-step mathematics, logic, multi-hop questions, and policy checks, and cites a GSM8K accuracy increase from 17.7% to 40.7%. [S9]
- It also acknowledges longer responses and the possibility of plausible-sounding but incorrect reasoning, recommending systematic comparison of prompts and examples. [S9]

#### Finding 4

**Claim**

The diversity of CoT variants is itself evidence that ‘CoT’ is not one intervention: prompting can combine intermediate verbalization, decomposition, search, self-consistency, retrieval, or latent computation.

**Confidence:** Medium

**Why this confidence level**

The taxonomy is directly reported, although the article is secondary and does not causally isolate the variants’ mechanisms.

**Evidence**

- S9 lists standard and zero-shot CoT alongside self-consistency, Tree of Thoughts, least-to-most, latent CoT, retrieval-based Chain-of-Knowledge, and Auto-CoT, assigning them different use cases. [S9]

#### Finding 5

**Claim**

The new sources do not resolve the central formatting-versus-reasoning dispute.

**Confidence:** High

**Why this confidence level**

The retrieved material plainly lacks the controlled causal evidence needed to decide whether the reported gains are reasoning gains or output-policy effects.

**Evidence**

- S10 establishes that displayed chains can be incorrect despite correct answers, but does not test whether generating a chain caused the answer or merely verbalized it afterward. [S10]
- S9 reports benchmark gains but does not match output format, response length, token budget, or baseline reasoning against non-CoT controls. [S9]
- S11 is an article titled ‘Multi-Dimensional Evaluation of Auto-Generated Chain-of-Thought Traces in Reasoning Models,’ but the retrieved content contains bibliographic and navigation material without its abstract, methods, results, or conclusions. [S11]

### Conflicts Found

- S9 presents CoT as transforming models into transparent problem solvers and as producing substantial accuracy gains, whereas S10 emphasizes that correct answers may have incorrect reasoning chains. These are not direct contradictions about accuracy, but they use different meanings of ‘effective’: output performance versus faithful reasoning. [S9] [S10]
- S9 treats visible intermediate steps as a transparency and debugging benefit, while S10’s step-level verification framing shows that visibility does not guarantee logical correctness or evidential support. [S9] [S10]
- S11 appears to offer potentially relevant multidimensional evidence about auto-generated traces in reasoning models, but the retrieved excerpt does not expose results, so it cannot currently corroborate or challenge the existing findings. [S11]

### Important Gaps

- What is the primary 2025 controlled study behind the claim that modern CoT exemplars primarily enforce output format rather than reasoning quality?
- Does that study match answer format, response length, token budget, sampling, and parsing against non-CoT controls?
- Do the multidimensional evaluations in S11 directly measure trace validity, faithfulness, and final accuracy, and do they compare CoT with direct-answer baselines?
- Can REVEAL-style step-level verification results be connected to causal interventions such as early answering, mistake injection, or hidden reasoning across multiple model regimes?
- How much of classic CoT’s GSM8K-style improvement survives when reasoning traces are independently verified and output-format or length effects are controlled?
- Are results consistent across non-reasoning models, reasoning-native models, and tasks outside mathematics and symbolic benchmarks?

**Analysis Duration:** 13.27s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

An important gap remains unresolved: the primary controlled evidence for the output-format explanation has not been retrieved. S10 improves the measurement framework, but neither S9 nor S10 answers the causal question, and S11’s results are absent from the retrieved excerpt.

**Next Search**

> 2025 study chain-of-thought exemplars primarily enforce output format rather than reasoning quality controlled experiment

---

# Iteration 5

## 1. Search

**Query**

> 2025 study chain-of-thought exemplars primarily enforce output format rather than reasoning quality controlled experiment

**Why this query**

An important gap remains unresolved: the primary controlled evidence for the output-format explanation has not been retrieved. S10 improves the measurement framework, but neither S9 nor S10 answers the causal question, and S11’s results are absent from the retrieved excerpt.

**Results**

5 results retrieved.

1 new unique source added.

### Sources

- **S12 — Medium**
  URL: https://gregrobison.medium.com/chain-of-thought-in-large-language-models-elicited-reasoning-or-constrained-imitation-5e4ee0c811ad

**Search Duration:** 2.69s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

S12 presents the conventional account of CoT: generating intermediate steps can make difficult multi-step tasks easier by expanding the model’s effective context and allocating more generated tokens to the problem.

**Confidence:** Low

**Why this confidence level**

S12 is a secondary Medium article and presents a conceptual explanation rather than a controlled empirical test separating useful computation from formatting or response-policy effects.

**Evidence**

- The article explains CoT as converting a direct answer prediction into sequential predictions conditioned on intermediate steps, and frames generated tokens as additional computational resources. [S12]

#### Finding 2

**Claim**

S12 distinguishes few-shot, zero-shot, and automatic CoT, indicating that ‘CoT’ comprises materially different interventions with different demonstrations, effort, and reliability.

**Confidence:** Medium

**Why this confidence level**

These distinctions are directly stated in the source, though S12 does not provide comparative experimental results or causal attribution for their differences.

**Evidence**

- The article describes few-shot CoT as using manually crafted reasoning exemplars, zero-shot CoT as using a generic step-by-step instruction, and Auto-CoT as generating exemplars automatically through clustering and model-produced chains. [S12]

#### Finding 3

**Claim**

S12 does not resolve whether CoT improves underlying reasoning or primarily induces constrained imitation and a particular output format.

**Confidence:** High

**Why this confidence level**

The source’s retrieved content lacks the methods and results needed to answer the central causal question.

**Evidence**

- Although the article explicitly frames the debate as genuine reasoning versus sophisticated mimicry, the retrieved content provides no controlled comparison matching answer format, output length, token budget, sampling, or baseline reasoning behavior. [S12]
- Its claims that CoT improves problem solving and allocates additional computation are explanatory assertions, not evidence from an experiment that isolates those mechanisms. [S12]

#### Finding 4

**Claim**

S12 is consistent with the accumulated conclusion that CoT’s effects should be analyzed by model regime, task complexity, prompt variant, and baseline rather than treated as a single universal strategy.

**Confidence:** Medium

**Why this confidence level**

S12 supplies contextual corroboration but no new controlled evidence; the stronger support comes from the previously retrieved experimental summaries.

**Evidence**

- The article contrasts standard prompting with several CoT variants and discusses their differing reliability and implementation requirements. [S12]
- This is consistent with the more specific prior evidence showing model-, task-, metric-, baseline-, and scaffold-dependent effects. [S5] [S6] [S8]

### Conflicts Found

- S12 repeats the conventional interpretation that CoT unlocks latent reasoning and improves difficult-task performance, while S8 and the critical result summarized in S1 caution that visible chains may be post-hoc, unfaithful, or primarily formatting-related. This is a difference in causal interpretation, not a direct contradiction about whether some benchmark scores improve. [S1] [S8] [S12]
- S12 describes extra generated tokens as computational resources, whereas S8 found that filler tokens alone did not improve accuracy. The findings are compatible if semantic, structured intermediate steps matter, but S12 does not establish that its additional tokens perform useful computation. [S8] [S12]

### Important Gaps

- What controlled experiment underlies the claim that modern CoT exemplars primarily enforce output format rather than improve reasoning quality?
- Does CoT retain an advantage when answer format, response length, token budget, sampling, and parsing are matched against direct-answer controls?
- How much of the benefit comes from semantic intermediate computation versus demonstrations, changed response policy, self-consistency, or majority voting?
- Do the reported effects generalize across reasoning-native and non-reasoning models and beyond mathematical or symbolic benchmarks?

**Analysis Duration:** 9.69s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

S12 adds no primary empirical evidence and leaves the central formatting-versus-reasoning question unresolved. Another search would materially improve the answer by locating the underlying controlled 2025 study explicitly claiming that CoT exemplars mainly enforce output format.

**Next Search**

> 2025 study chain-of-thought exemplars enforce output format rather than reasoning quality controlled experiment

---

# Iteration 6

## 1. Search

**Query**

> 2025 study chain-of-thought exemplars enforce output format rather than reasoning quality controlled experiment

**Why this query**

S12 adds no primary empirical evidence and leaves the central formatting-versus-reasoning question unresolved. Another search would materially improve the answer by locating the underlying controlled 2025 study explicitly claiming that CoT exemplars mainly enforce output format.

**Results**

5 results retrieved.

1 new unique source added.

### Sources

- **S13 — A comparison of chain-of-thought reasoning strategies across datasets and models**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11157560

**Search Duration:** 2.86s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

A small 2024 cross-model, cross-dataset study finds that zero-shot CoT strategies generally improve performance across varied question-answering tasks, including scientific, medical, real-world knowledge, and logical reasoning datasets.

**Confidence:** Medium

**Why this confidence level**

S13 is a peer-reviewed/open-access study with direct comparative experiments across models and datasets. However, the abstract describes it as small-scale, and the retrieved content does not provide detailed effect sizes, controls, or full methodological results.

**Evidence**

- The study compares six LLMs and six QA datasets and reports that gains from CoT reasoning strategies remain robust across models and datasets, with GPT-4 benefiting most from state-of-the-art prompting. [S13]

#### Finding 2

**Claim**

S13 broadens the evidence that CoT can improve final-answer accuracy beyond mathematics and symbolic benchmarks, but it does not establish that the gains reflect genuine latent reasoning rather than altered response behavior.

**Confidence:** Medium

**Why this confidence level**

The task diversity is directly stated, but the retrieved material is insufficient to identify the causal mechanism behind the accuracy improvements.

**Evidence**

- The tested datasets include scientific and medical question answering, real-world knowledge application, and logical verbal reasoning, and the paper reports robust CoT gains across them. [S13]
- The retrieved abstract describes predictive performance and explainability benefits but does not report controls matching output format, response length, token budget, parsing, or hidden versus visible reasoning. [S13]

#### Finding 3

**Claim**

The new study supports treating prompt design as a substantive source of CoT variation: the best strategy was not necessarily a generic step-by-step instruction but a prompt discovered through automated search, and effects varied by model.

**Confidence:** Medium

**Why this confidence level**

This conclusion follows directly from the study’s stated comparison, though the retrieved excerpt does not show which prompt components caused the advantage.

**Evidence**

- S13 reports variations in effectiveness across models and strategies, with GPT-4 performing best using a prompt previously discovered through automated discovery. [S13]

#### Finding 4

**Claim**

S13 is compatible with, but does not overturn, the conditional synthesis that CoT is useful in some regimes rather than universally effective.

**Confidence:** Medium

**Why this confidence level**

The sources examine different model sets, tasks, prompting regimes, and evaluation details; the apparent tension is conditional rather than a clean contradiction.

**Evidence**

- S13 reports broadly robust gains across its selected models and datasets. [S13]
- Prior evidence reports small or negative incremental effects for reasoning-native models, metric-sensitive outcomes, increased variability, and substantial latency costs in other settings. [S5]

### Conflicts Found

- S13 reports robust CoT gains across six models and six datasets, whereas S5 reports modest, inconsistent, or negative incremental effects for some models, especially reasoning-native systems. This likely reflects differences in model generation, task selection, baseline prompting, metrics, and experimental protocol; S13's retrieved excerpt does not provide enough detail to determine which moderator explains the difference. [S13] [S5]
- S13 presents performance gains in diverse QA settings, while S1 and S8 caution that improved final answers do not demonstrate that visible reasoning chains are causally responsible or faithful. These positions address different outcomes—accuracy versus causal/step-level reasoning quality—rather than directly contradicting one another. [S13] [S1] [S8]

### Important Gaps

- Did S13 match CoT and direct-answer conditions for output format, response length, token budget, sampling, and answer parsing?
- How large were the gains for each model and dataset, and were they statistically reliable across repeated trials?
- Were the six models reasoning-native or ordinary instruction-tuned models, and how do the results compare with current reasoning-native systems?
- Does the automated-discovery prompt improve reasoning specifically, or mainly induce a more effective response policy or answer format?
- Were intermediate reasoning chains independently evaluated for logical correctness and faithfulness?
- Can S13's cross-domain gains be reconciled quantitatively with the negative or weak effects reported in S5 under matched experimental conditions?

**Analysis Duration:** 11.06s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

S13 adds useful positive evidence from non-mathematical datasets and supports prompt/task/model dependence, but it does not address the central causal fault line: whether CoT improves reasoning beyond output-format, response-policy, and extra-token effects. The most valuable next search is for the full methods/results or a controlled replication of S13 that matches these confounds.

**Next Search**

> "A comparison of chain-of-thought reasoning strategies across datasets and models" full text methods output length controls

---

# Iteration 7

## 1. Search

**Query**

> "A comparison of chain-of-thought reasoning strategies across datasets and models" full text methods output length controls

**Why this query**

S13 adds useful positive evidence from non-mathematical datasets and supports prompt/task/model dependence, but it does not address the central causal fault line: whether CoT improves reasoning beyond output-format, response-policy, and extra-token effects. The most valuable next search is for the full methods/results or a controlled replication of S13 that matches these confounds.

**Results**

5 results retrieved.

2 new unique sources added.

### Sources

- **S14 — When More is Less: Understanding Chain-of-Thought Length in LLMs**
  URL: https://arxiv.org/html/2502.07266v1
- **S15 — Chain-of-Thought Training Data**
  URL: https://www.emergentmind.com/topics/chain-of-thought-training-data

**Search Duration:** 4.42s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

CoT length is a substantive moderator of performance: increasing the number of reasoning steps can help initially but eventually reduce accuracy.

**Confidence:** Medium

**Why this confidence level**

S14 presents theory and experiments across synthetic and real-world math settings, but it is a single recent preprint and does not directly compare CoT with format-matched non-CoT controls.

**Evidence**

- S14 reports an empirical inverted-U relationship between CoT length and performance on synthetic arithmetic and real-world mathematical tasks: decomposition helps at first, while excessively long chains suffer from noise and error accumulation. [S14]

#### Finding 2

**Claim**

The optimal reasoning depth depends jointly on model capability and task difficulty, providing a concrete explanation for conflicting results about long or short CoT.

**Confidence:** Medium

**Why this confidence level**

The source directly links length, model capability, and difficulty, but the generality beyond the tested mathematical settings remains uncertain.

**Evidence**

- S14 states that harder tasks require deeper decomposition, whereas more capable models can solve moderately complex subtasks in fewer steps; it derives an optimal-length scaling relationship and reports corresponding experiments. [S14]

#### Finding 3

**Claim**

Longer CoT can harm reliability through accumulated intermediate errors, so more visible reasoning is not automatically better reasoning.

**Confidence:** Medium

**Why this confidence level**

The mechanism is supported by the paper's theoretical framing and experiments, though independent replication and direct faithfulness measurements are not available.

**Evidence**

- S14 attributes late-stage performance deterioration to increasing susceptibility to noise and the possibility that one mistaken step misleads the rest of the chain. [S14]

#### Finding 4

**Claim**

The new evidence strengthens the view that CoT is not a single intervention: reasoning depth, decomposition structure, and aggregation policy can materially change outcomes.

**Confidence:** Medium

**Why this confidence level**

S14 adds a specific length mechanism consistent with the broader accumulated evidence, but it does not isolate length from semantic reasoning content or sampling effects.

**Evidence**

- S14 proposes Length-filtered Vote, which selects answers associated with an empirically appropriate CoT length rather than treating all sampled chains as equivalent. [S14]
- Prior evidence already shows differences among zero-shot, few-shot, structured, contrastive, and self-consistency variants, as well as baseline- and metric-dependent effects. [S1] [S5] [S6] [S8]

#### Finding 5

**Claim**

The evidence continues to support a conditional, performance-level conclusion: CoT can improve final answers in suitable regimes, but this does not establish a general improvement in latent reasoning or faithful displayed reasoning.

**Confidence:** Medium

**Why this confidence level**

The sources converge on conditional effectiveness and a distinction between accuracy and reasoning faithfulness, but the central causal confound remains unresolved.

**Evidence**

- S14 shows that appropriately calibrated CoT length can improve performance, while excessive length degrades it. [S14]
- S8 reports that CoT often improves accuracy even though faithfulness varies widely and is weakly correlated with the size of the accuracy gain. [S8]
- S5 reports model-regime-, metric-, and baseline-dependent gains, including small or negative incremental effects for some reasoning-native models. [S5]

#### Finding 6

**Claim**

CoT training data may improve learning and generalization, but the retrieved S15 material does not provide sufficiently reliable or direct evidence for the inference-time formatting-versus-reasoning question.

**Confidence:** Low

**Why this confidence level**

The source is secondary, heterogeneous, and includes broad claims without enough methodological detail to attribute gains specifically to CoT reasoning.

**Evidence**

- S15 describes rationale-supervised datasets, self-training, grounding, compression, and claimed improvements in sample complexity and generalization. [S15]
- S15 is an aggregated secondary topic page and the excerpt does not establish controlled comparisons that separate rationale supervision, answer format, data scale, and other training changes. [S15]

### Conflicts Found

- S14 challenges the implicit assumption that longer or more elaborate CoT is generally better, whereas conventional accounts in S6, S7, and S12 describe intermediate steps as broadly beneficial. The disagreement is conditional: S14 predicts an optimal length dependent on task and model, not universal harm from CoT. [S6] [S7] [S12] [S14]
- S14 explains some performance differences through useful decomposition followed by noise and error accumulation; S8 additionally finds that displayed chains can be unfaithful or post-hoc. These mechanisms are compatible, but S14 does not test whether its optimal-length chains are causally faithful. [S8] [S14]
- S15 presents broad claims that CoT training data improves generalization and interpretability, while the accumulated evidence shows that visible traces may be incorrect or primarily response-policy effects. The conflict reflects stronger claims in S15 than its retrieved evidence can substantiate. [S8] [S10] [S15]

### Important Gaps

- Does the optimal-length effect in S14 survive controls matching output format, response length, token budget, sampling, and answer parsing against direct-answer baselines?
- Are S14's length effects caused by useful semantic decomposition, by additional computation, or by altered response policy and answer selection?
- Do the optimal-length and error-accumulation results generalize to knowledge-intensive, adversarial, compositional, and non-mathematical tasks?
- Are appropriately length-calibrated CoT traces more faithful at the step level, or merely more accurate at the final-answer level?
- What controlled primary study supports the claim that modern CoT exemplars mainly enforce output format rather than improve reasoning quality?
- How do CoT length effects differ between reasoning-native and ordinary instruction-tuned models?
- Do the training-data claims in S15 remain after controlling for dataset size, rationale correctness, answer supervision, and changes in model training procedure?

**Analysis Duration:** 15.01s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new source materially improves the account of one fault line—reasoning length and error accumulation—but the central formatting-versus-reasoning dispute remains unanswered. The most important missing evidence is the primary controlled study behind the claim that modern CoT exemplars mainly enforce output format, with matched-length, matched-format, token-budget, and hidden/visible-reasoning controls.

**Next Search**

> "chain-of-thought" exemplars "output format" reasoning quality controlled study

---

# Iteration 8

## 1. Search

**Query**

> "chain-of-thought" exemplars "output format" reasoning quality controlled study

**Why this query**

The new source materially improves the account of one fault line—reasoning length and error accumulation—but the central formatting-versus-reasoning dispute remains unanswered. The most important missing evidence is the primary controlled study behind the claim that modern CoT exemplars mainly enforce output format, with matched-length, matched-format, token-budget, and hidden/visible-reasoning controls.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S16 — Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot**
  URL: https://arxiv.org/html/2506.14641v1
- **S17 — Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot**
  URL: https://arxiv.org/html/2506.14641v3
- **S18 — Chain-of-Thought Prompting Elicits Reasoning in Large ...**
  URL: https://interpretable-ml-class.github.io/slides/Lecture_23_CoT.pdf
- **S19 — Chain-of-Thought Reasoning**
  URL: https://www.emergentmind.com/topics/chain-of-thought-cot-reasoning-fd86d712-e431-4308-affd-c5dbdf17030a
- **S20 — Chain - of - Thought Prompting Elicits Reasoning**
  URL: https://opis-cdn.tinkoffjournal.ru/mercury/chain-of-thought.ozukbqfqvqcr..pdf

**Search Duration:** 4.21s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new primary study directly supports the formatting-versus-reasoning critique, but only for few-shot CoT exemplars in recent open-source models on mathematical tasks.

**Confidence:** Medium

**Why this confidence level**

The source is a recent primary preprint and directly addresses the disputed claim, but the retrieved material does not expose complete tables, statistical tests, or the full control design.

**Evidence**

- S16 and S17 report systematic experiments on GSM8K and MATH with recent models, especially the Qwen2.5 series. After correcting a GSM8K evaluation bias, traditional few-shot CoT did not improve reasoning performance relative to zero-shot CoT; the authors identify output-format alignment as its primary function. [S16] [S17]

#### Finding 2

**Claim**

The apparent disagreement is substantially explained by model capability and the choice of baseline: older or weaker models may benefit from CoT exemplars, whereas strong recent models may already obtain the relevant benefit from zero-shot step-by-step prompting.

**Confidence:** High

**Why this confidence level**

The sources converge on baseline and model-regime dependence, though they compare different generations of models and protocols.

**Evidence**

- S16 and S17 state that traditional CoT exemplars may benefit weaker models but do not enhance strong models, whose zero-shot CoT performance is already strong. [S16] [S17]
- The original CoT study reports large gains for sufficiently large PaLM and other models over standard prompting, while explicitly presenting CoT as an emergent ability dependent on model scale. [S18] [S20]
- S5 likewise reports gains for some non-reasoning models but marginal or negative incremental effects for reasoning-native models. [S5]

#### Finding 3

**Claim**

Few-shot CoT exemplars and zero-shot CoT are not interchangeable interventions; exemplar content can add little when the model mainly follows the instruction rather than learning from the demonstrations.

**Confidence:** Medium

**Why this confidence level**

The distinction is directly reported, but the retrieved excerpt does not independently verify the authors’ behavioral diagnosis that models ignored the exemplars.

**Evidence**

- S16 and S17 report that enhanced exemplars built from Qwen2.5-Max and DeepSeek-R1 still failed to improve strong models, which reportedly tended to ignore exemplar content and focus on instructions. [S16] [S17]
- The original study used input–rationale–answer triples and found gains over standard few-shot prompting, showing that the earlier result tested a different intervention from zero-shot CoT. [S18] [S20]

#### Finding 4

**Claim**

The new evidence strengthens the claim that some CoT gains are output-policy or formatting effects, but it does not show that all CoT accuracy gains are merely formatting effects.

**Confidence:** Medium

**Why this confidence level**

The evidence supports a mixed-mechanism account, but the new study does not isolate formatting from all possible semantic or computational contributions across models and tasks.

**Evidence**

- S16 and S17 explicitly attribute the primary effect of few-shot exemplars in their tested strong models to aligning output format, while finding no reasoning-performance gain over zero-shot CoT. [S16] [S17]
- S20 reports a large PaLM 540B improvement over standard prompting on GSM8K and describes intermediate steps as enabling decomposition and additional computation. [S20]
- S8 reports accuracy improvements alongside wide variation in faithfulness, and filler tokens alone did not improve accuracy; this is consistent with semantic computation sometimes mattering, without proving that it always does. [S8]

#### Finding 5

**Claim**

Evaluation artifacts can reverse the apparent comparison between zero-shot and few-shot CoT, making implementation and metric choices a major fault line.

**Confidence:** High

**Why this confidence level**

Both sources directly report metric or evaluation-protocol sensitivity, although the precise implementation bug is not included in the retrieved excerpt.

**Evidence**

- S16 and S17 identify a common open-source GSM8K evaluation bias that significantly underestimates zero-shot CoT performance; correcting it changes the comparison with few-shot CoT. [S16] [S17]
- S5 finds different conclusions depending on average accuracy, majority correctness, perfect accuracy, and repeated-trial variability. [S5]

#### Finding 6

**Claim**

The original evidence establishes an output-performance effect, not the stronger claim that visible CoT is faithful internal reasoning.

**Confidence:** High

**Why this confidence level**

The sources directly separate benchmark accuracy from faithful causal reasoning.

**Evidence**

- S18 and S20 describe improved benchmark performance and interpretability potential, but the original paper itself cautions that the generated chain only mimics a thought process and does not establish whether the neural network is actually reasoning. [S18] [S20]
- S8 finds that CoT faithfulness varies by task and is weakly correlated with accuracy gains; S10 distinguishes final-answer correctness from step-level reasoning correctness. [S8] [S10]

#### Finding 7

**Claim**

The most defensible synthesis is that CoT is an effective conditional test-time scaffold, not a universally effective reasoning strategy or a reliable measure of latent reasoning.

**Confidence:** High

**Why this confidence level**

This conditional conclusion is supported by both the classic positive result and the newer critical result, while avoiding the unsupported claim that either mechanism explains every setting.

**Evidence**

- The original study reports substantial gains over standard prompting on arithmetic, commonsense, and symbolic tasks, especially at large scale. [S18] [S20]
- Recent evidence finds no incremental reasoning gain from few-shot exemplars over zero-shot CoT in strong models and identifies formatting as their primary role. [S16] [S17]
- Across the accumulated evidence, effects vary with model regime, task difficulty, baseline, metric, length, scaffold, and faithfulness. [S1] [S5] [S8] [S14]

### Conflicts Found

- S16/S17 find that few-shot CoT exemplars do not improve strong models beyond zero-shot CoT and mainly align output format, whereas S18/S20 report striking gains from few-shot CoT over standard prompting. This is primarily a baseline-and-model-generation difference: the classic comparison is against standard direct prompting on older models, while the new comparison is against already-effective zero-shot CoT on recent strong models. [S16] [S17] [S18] [S20]
- S16/S17 report that even enhanced exemplars are ignored by strong models, while conventional accounts treat exemplar rationales as demonstrations that teach a decomposition strategy. The retrieved sources do not establish whether this reflects model capability, exemplar quality, instruction-following preferences, or the specific mathematical tasks. [S16] [S17] [S18] [S20]
- S16/S17 attribute the incremental few-shot effect primarily to output-format alignment, while S20 frames CoT as enabling decomposition and additional computation. These claims may both apply: formatting can explain the exemplar increment in strong models, while semantically structured generated steps can still improve some weaker-model or difficult-task settings. [S16] [S17] [S8] [S20]

### Important Gaps

- Do the S16/S17 results survive format-matched controls that equalize answer structure, output length, token budget, sampling, and parsing?
- How large are the effects for each model and dataset, and how reliable are they across repeated trials?
- Does the claimed exemplar-insensitivity generalize beyond Qwen2.5 and GSM8K/MATH to frontier proprietary models, reasoning-native systems, and non-mathematical tasks?
- Does zero-shot CoT itself improve reasoning over a format-matched direct-answer condition, or does it also partly induce a response policy?
- Can the evaluation bias identified in GSM8K explain some earlier few-shot-versus-zero-shot discrepancies, and does it occur in other benchmarks?
- Are the generated chains in settings where CoT improves accuracy independently verified as logically correct and causally involved in answer selection?

**Analysis Duration:** 20.09s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

This is the first retrieved source that directly addresses the underlying formatting claim, substantially improving the evidence base. However, the central causal question remains open because the available excerpt does not provide the full matched-control results, effect sizes, repeated-trial analyses, or cross-domain replication needed to distinguish formatting, semantic computation, and changed response policy.

**Next Search**

> "Revisiting Chain-of-Thought Prompting" 2506.14641 experiments output format zero-shot few-shot GSM8K MATH tables

---

# Iteration 9

## 1. Search

**Query**

> "Revisiting Chain-of-Thought Prompting" 2506.14641 experiments output format zero-shot few-shot GSM8K MATH tables

**Why this query**

This is the first retrieved source that directly addresses the underlying formatting claim, substantially improving the evidence base. However, the central causal question remains open because the available excerpt does not provide the full matched-control results, effect sizes, repeated-trial analyses, or cross-domain replication needed to distinguish formatting, semantic computation, and changed response policy.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S21 — [PDF] Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot | Semantic Scholar**
  URL: https://www.semanticscholar.org/paper/Revisiting-Chain-of-Thought-Prompting%3A-Zero-shot-Be-Cheng-Pan/63917b69c838c109f3e83c65f0ec8d04e01079ab
- **S22 — Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot - ACL Anthology**
  URL: https://aclanthology.org/2025.findings-emnlp.729
- **S23 — Few-Shot & Chain-of-Thought Prompting**
  URL: https://www.emergentmind.com/topics/few-shot-and-chain-of-thought-prompting
- **S24 — Zero-Shot vs Few-Shot vs Chain-of-Thought Prompting: Complete Guide 2026 | explainx.ai Blog | explainx.ai**
  URL: https://explainx.ai/blog/zero-shot-few-shot-chain-of-thought-prompting-guide-2026

**Search Duration:** 3.36s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources strengthen, but do not broaden without qualification, the finding that few-shot CoT exemplars may add no reasoning benefit over zero-shot CoT for strong recent models.

**Confidence:** Medium

**Why this confidence level**

S21 provides a study summary and S22 identifies the ACL Findings publication, but the retrieved ACL page contains no abstract, methods, results tables, or detailed controls.

**Evidence**

- The 2025 study reports that traditional and enhanced CoT exemplars failed to improve reasoning performance over zero-shot CoT for recent strong models, particularly Qwen2.5-series systems. [S21] [S22]

### Conflicts Found

- The new study’s conclusion appears to conflict with the classic finding that few-shot CoT substantially improves performance over standard prompting. The comparison is conditional rather than direct: the classic work compares few-shot CoT with ordinary direct prompting on earlier large models, whereas the newer work compares few-shot CoT with already-effective zero-shot CoT on recent strong models. [S18] [S20] [S21] [S22]
- S23 presents few-shot CoT as serving both multi-step reasoning and output-format alignment, while S21/S22 report no incremental reasoning benefit from exemplars in strong recent models. This suggests that exemplar usefulness depends on whether the model already possesses an effective step-by-step response policy. [S21] [S22] [S23]

### Important Gaps

- What exact controls and evaluation procedures were used in the ACL study, especially for answer format, response length, token budget, sampling, and parsing?
- How much of the reported zero-shot-versus-few-shot difference is caused by the identified GSM8K evaluation bias?
- Do the findings generalize beyond Qwen2.5, GSM8K, and MATH to reasoning-native systems, proprietary frontier models, and non-mathematical tasks?
- Does zero-shot CoT itself outperform a format-matched direct-answer or hidden-reasoning condition?
- Are the improved or unchanged final-answer scores accompanied by independently verified, causally involved reasoning steps?

**Analysis Duration:** 9.43s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new source materially clarifies one major fault line—model generation and baseline—but the central causal question remains underdetermined. The primary publication is now identified, yet its retrieved content does not expose the methods needed to judge whether ‘format alignment’ was isolated from semantic computation, output length, and evaluation artifacts.

**Next Search**

> "Revisiting Chain-of-Thought Prompting" output format alignment evaluation bias GSM8K MATH

---

# Iteration 10

## 1. Search

**Query**

> "Revisiting Chain-of-Thought Prompting" output format alignment evaluation bias GSM8K MATH

**Why this query**

The new source materially clarifies one major fault line—model generation and baseline—but the central causal question remains underdetermined. The primary publication is now identified, yet its retrieved content does not expose the methods needed to judge whether ‘format alignment’ was isolated from semantic computation, output length, and evaluation artifacts.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S25 — Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot**
  URL: https://arxiv.org/html/2506.14641v2
- **S26 — Revisiting Chain-of-Thought Prompting: Zero-shot Can Be ...**
  URL: https://www.alphaxiv.org/abs/2506.14641
- **S27 — Language Models Perform Reasoning via Chain of Thought**
  URL: https://research.google/blog/language-models-perform-reasoning-via-chain-of-thought
- **S28 — Daily Papers - Hugging Face**
  URL: https://huggingface.co/papers?q=chain-of-thought

**Search Duration:** 2.07s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The newly retrieved primary source directly strengthens the model-regime and baseline explanation for conflicting CoT results: few-shot CoT exemplars can add little or no reasoning benefit when compared with zero-shot CoT on strong recent models, even though older comparisons found large gains over direct prompting.

**Confidence:** High

**Why this confidence level**

S25 is a primary preprint directly addressing the comparison, and S27 provides the classic contrasting baseline. The studies nevertheless use different model generations and protocols.

**Evidence**

- S25 reports systematic GSM8K and MATH experiments in which traditional few-shot CoT did not improve recent strong models, such as the Qwen2.5 series, relative to zero-shot CoT; it states that weaker models may still benefit. [S25]
- The classic account evaluated few-shot CoT against standard direct prompting and reported substantial gains for sufficiently large PaLM models, especially on arithmetic reasoning. [S27]

#### Finding 2

**Claim**

In the setting tested by S25, few-shot CoT exemplars appear primarily to align output format rather than teach additional mathematical reasoning.

**Confidence:** Medium

**Why this confidence level**

The source directly reports the authors' controlled conclusion, but the retrieved material does not expose complete ablation tables or all controls needed to generalize the result beyond the tested models and mathematical tasks.

**Evidence**

- S25 explicitly states that exemplar ablations and comparisons identify output-format alignment as the primary function of few-shot CoT for recent strong models, with no observable improvement over zero-shot CoT in reasoning performance. [S25]

#### Finding 3

**Claim**

A major methodological fault line is answer extraction: evaluation errors can make zero-shot CoT appear weaker than it is and thereby exaggerate the apparent value of few-shot exemplars.

**Confidence:** High

**Why this confidence level**

Both sources directly identify evaluation or metric sensitivity as capable of changing the result.

**Evidence**

- S25 reports that common GSM8K evaluation frameworks extract the last number and can miss answers expressed in \boxed{} format; correcting this bias substantially improves measured zero-shot CoT performance and often makes it comparable to or better than few-shot CoT. [S25]
- S5 likewise found that conclusions changed across average accuracy, majority correctness, perfect accuracy, and repeated-trial variability. [S5]

#### Finding 4

**Claim**

S25 provides a plausible behavioral account of exemplar failure in strong models: they attend more to the instruction and target question than to the semantic content of demonstrations.

**Confidence:** Medium

**Why this confidence level**

The reported analyses are directly relevant, but the retrieved source does not provide detailed attention methodology, quantitative results, or independent replication.

**Evidence**

- The source reports attention analyses and corrupted-exemplar tests indicating low reliance on exemplar content; enhanced exemplars generated by Qwen2.5-Max and DeepSeek-R1 also failed to improve performance. [S25]

#### Finding 5

**Claim**

The classic positive evidence demonstrates that CoT can improve final-answer performance, but it does not establish that visible chains are faithful internal reasoning or that the same mechanism remains effective in current models.

**Confidence:** High

**Why this confidence level**

S27 directly supports an output-performance effect, while S8 and S10 support the distinction between answer accuracy and faithful reasoning.

**Evidence**

- S27 reports large improvements over standard prompting on arithmetic tasks and smaller gains on several commonsense tasks, with benefits emerging at large model scale. [S27]
- The accumulated evidence reports task-dependent faithfulness and notes that correct answers can be accompanied by incorrect or post-hoc explanations. [S8] [S10]

#### Finding 6

**Claim**

The new material does not support the stronger universal claim that CoT is merely formatting; a mixed-mechanism account remains best supported.

**Confidence:** High

**Why this confidence level**

The sources jointly support conditional formatting effects without warranting their extension to every model, task, or form of CoT.

**Evidence**

- S25 supports a formatting explanation for few-shot exemplars in strong recent mathematical models, whereas S27 reports substantial gains from few-shot CoT over direct prompting in earlier large models. [S25] [S27]
- S8 found that filler tokens alone did not improve accuracy, while structured CoT sometimes improved accuracy despite variable faithfulness, suggesting that semantic structure or altered computation can matter in at least some regimes. [S8]

#### Finding 7

**Claim**

The newly retrieved source S28 offers potentially relevant but currently weak evidence that CoT benefits are concentrated in mathematical and symbolic tasks and may depend on training-distribution alignment.

**Confidence:** Low

**Why this confidence level**

S28 is an aggregator snippet rather than the underlying papers, and the retrieved text is incomplete; it should not be treated as decisive evidence.

**Evidence**

- The S28 listing summarizes a meta-analysis and evaluations claiming strong CoT benefits primarily for math or logic, with much smaller gains elsewhere; it also lists a separate study arguing that CoT can be brittle under distribution shift. [S28]

### Conflicts Found

- S25 finds that few-shot exemplars add no reasoning benefit over zero-shot CoT for strong recent models, while S27 presents few-shot CoT as enabling substantial gains over standard prompting. The difference is largely explained by baseline and model generation: zero-shot CoT was not the relevant comparator in the classic result, and newer models may already possess the elicited response policy. [S25] [S27]
- S25 attributes the exemplar effect primarily to output-format alignment, whereas S27 describes intermediate steps as enabling decomposition and improved reasoning. This is a causal-interpretation disagreement, not a direct disagreement that benchmark accuracy can improve. [S25] [S27]
- S28's aggregator claims that CoT helps mainly on math and symbolic reasoning and that it can be distributionally brittle, but the current evidence is too incomplete to compare those claims reliably with S13's broader cross-domain gains. [S28] [S13]

### Important Gaps

- Does zero-shot CoT itself outperform a format-matched direct-answer or hidden-reasoning condition when response length, token budget, sampling, and parsing are held constant?
- Do S25's exemplar-format findings generalize beyond Qwen2.5 and GSM8K/MATH to proprietary frontier models, reasoning-native systems, and non-mathematical tasks?
- How much of the classic S27 gain survives corrected answer extraction and matched output-format controls?
- Are accuracy-improving CoT traces independently verified as logically correct and causally involved in answer selection?
- Does the apparent concentration of CoT benefits in mathematical and symbolic tasks reported by S28 replicate in the underlying meta-analysis and full experiments?

**Analysis Duration:** 18.49s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The runner reached the maximum research iteration budget. Analyzer assessment: The new primary source substantially clarifies one fault line—few-shot versus zero-shot CoT on strong recent mathematical models—and identifies an evaluation artifact. However, the central causal question remains unresolved: the retrieved evidence still lacks a broad, format- and token-budget-matched comparison that separates semantic intermediate computation from response-policy and parsing effects.

**Stop Reason:** max_iterations

---

# Final Research Decision

**Research Stopped Because**

The runner reached the maximum research iteration budget.

**Stop Reason:** max_iterations

**Searches Performed:** 10

**Unique Sources:** 28

**Remaining Uncertainty**

- Whether zero-shot CoT itself improves reasoning over a format-matched direct-answer or hidden-reasoning condition when output format, response length, token budget, sampling, and parsing are held constant.
- Whether the formatting findings from S25 generalize beyond Qwen2.5 and GSM8K/MATH to proprietary frontier models, reasoning-native systems, and non-mathematical tasks.
- How much of the classic CoT gains survive corrected answer extraction and matched-format controls.
- Whether accuracy-improving chains are independently verified as logically correct and causally involved in answer selection.
- How model capability, task difficulty, chain length, semantic content, and aggregation methods interact under a common experimental protocol.
- Whether claims about CoT’s brittleness under distribution shift and concentration of benefits in math or symbolic tasks replicate in the underlying studies summarized by S28.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 10 | 29.18s |
| OpenAI Analysis | 10 | 143.73s |
| Report Generation | 1 | 25.97s |
| Total Run | — | 198.89s |
