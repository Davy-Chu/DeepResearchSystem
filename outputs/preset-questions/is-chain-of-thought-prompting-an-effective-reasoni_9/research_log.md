# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

**Status:** Completed

**Stop Reason:** sufficient_evidence

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 9 / 10

**Unique Sources:** 30

**OpenAI Calls:** 10

**Tavily Calls:** 9

**Started:** 2026-09-01T02:44:38-04:00

**Ended:** 2026-09-01T02:47:49-04:00

**Total Runtime:** 190.88s

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

- **S1 — Hierarchical Chain-of-Thought Prompting: Enhancing LLM ...**
  URL: https://arxiv.org/html/2604.00130v1
- **S2 — Medium**
  URL: https://medium.com/data-science-collective/so-you-think-you-can-prompt-b3384664bafc
- **S3 — What is chain of thought (CoT) prompting? - IBM**
  URL: https://www.ibm.com/think/topics/chain-of-thoughts
- **S4 — Contrastive Chain-Of-Thought Prompting**
  URL: https://www.kore.ai/blog/contrastive-chain-of-thought-prompting
- **S5 — The Decreasing Value of Chain of Thought in Prompting**
  URL: https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought

**Search Duration:** 3.33s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The literature does not support a universal verdict that CoT either reliably creates reasoning or merely changes formatting; its effect depends strongly on the model, task, and evaluation procedure.

**Confidence:** Medium

**Why this confidence level**

The model- and task-dependence is directly reported in S5, while S1 provides supporting but currently limited evidence from a single, recent preprint.

**Evidence**

- A 2025 technical report finds substantially different effects across non-reasoning and reasoning models, with improvements, null results, and declines depending on model and accuracy threshold. [S5]
- A separate proposed hierarchical variant reports gains over flat CoT on difficult mathematical benchmarks, suggesting that the structure of the elicited reasoning process matters rather than simply the presence of extra text. [S1]

#### Finding 2

**Claim**

CoT appears more useful for some non-reasoning models than for models that already have built-in reasoning behavior.

**Confidence:** Medium

**Why this confidence level**

S5 gives direct comparative results, but the evidence comes from one dataset and report rather than a broad independent replication.

**Evidence**

- On GPQA Diamond, the report says non-reasoning models had modest average gains, including 13.5% for Gemini Flash 2.0 and 11.7% for Sonnet 3.5, whereas reasoning models showed only small gains for o3-mini and o4-mini and a decline for Gemini Flash 2.5. [S5]
- The report observes that many models produce CoT-like reasoning by default even without an explicit step-by-step instruction. [S5]

#### Finding 3

**Claim**

Explicit CoT can increase average performance while reducing consistency or harming cases that a model would otherwise answer correctly.

**Confidence:** Medium

**Why this confidence level**

The repeated-trial design and reported threshold-sensitive effects directly support the claim, although the source is a technical report and the evidence is limited to GPQA Diamond.

**Evidence**

- For non-reasoning models, S5 reports average improvements but mixed effects on perfect accuracy, including a substantial decline for Gemini Pro 1.5; it attributes this pattern to added answer variability. [S5]
- The study tested each question 25 times and used multiple correctness thresholds, showing that one-shot benchmark scores can conceal inconsistency. [S5]

#### Finding 4

**Claim**

A major fault line is whether the evaluation measures final-answer accuracy, consistency, or the quality of the visible reasoning trace; these metrics can produce different conclusions.

**Confidence:** High

**Why this confidence level**

The source explicitly describes the repeated-trial methodology and multiple evaluation thresholds, directly establishing measurement as a source of disagreement.

**Evidence**

- S5 reports different outcomes under complete accuracy, high accuracy, majority correctness, and average-rating metrics, with some CoT effects changing direction or significance by threshold. [S5]
- The report contrasts default, direct-answer, and step-by-step conditions, finding that default behavior often already contains short CoT-like output. [S5]

#### Finding 5

**Claim**

CoT has a real inference-cost tradeoff, and its marginal value may be unattractive when a model already reasons internally.

**Confidence:** Medium

**Why this confidence level**

The cost/benefit pattern is directly reported, but the magnitude is model- and benchmark-specific; S1 is a single preprint with unusually broad claimed improvements.

**Evidence**

- S5 reports 35–600% longer response times for non-reasoning models and 20–80% longer times for reasoning models, while reasoning-model accuracy gains were generally small. [S5]
- S1 reports that its hierarchical structure reduced trace length by 13.9% relative to ordinary CoT while improving average accuracy by 6.2% across its tested settings. [S1]

#### Finding 6

**Claim**

Reasoning quality may depend on the organization and constraints of the trace, not simply on asking for more intermediate tokens.

**Confidence:** Low

**Why this confidence level**

The mechanism is a hypothesis advanced by the authors, and the reported comparison is not independently corroborated in the retrieved material.

**Evidence**

- S1 argues that flat CoT can be redundant or drift from the intended reasoning path, and proposes alternating planning and execution as a way to maintain subgoals and compress irrelevant state. [S1]
- S1 reports better accuracy and shorter traces for its hierarchical method than for its CoT baseline on five mathematical benchmarks. [S1]

#### Finding 7

**Claim**

The retrieved evidence does not yet establish the strongest version of the 'formatting-only' interpretation—that CoT exemplars primarily teach an output format rather than improve computation.

**Confidence:** High

**Why this confidence level**

The absence of direct evidence in the retrieved content is clear; the central formatting hypothesis is only named in S1 and not substantively documented.

**Evidence**

- S1 mentions a 2025 result claiming that CoT exemplars primarily enforce output format in modern LLMs, but the retrieved passage provides no methods, results, or direct citation details for that claim. [S1]
- S2 and S3 describe CoT as improving reasoning, but they are explanatory or secondary sources and do not provide a controlled test separating reasoning from formatting. [S2] [S3]

### Conflicts Found

- S2 and S3 present CoT as a broadly effective step-by-step reasoning aid, while S5 reports model-dependent, sometimes negligible or negative effects and substantial latency costs. [S2] [S3] [S5]
- S1 claims consistent accuracy improvements from structured CoT and argues that unstructured prompting underuses latent reasoning capacity, whereas S5 finds generic CoT offers only marginal benefits for built-in reasoning models. This is a conditional rather than necessarily direct contradiction: the methods, model families, tasks, and prompting variants differ. [S1] [S5]
- S1 reports shorter traces accompanying better performance for Hi-CoT, while S5 reports that ordinary step-by-step prompting often costs substantially more time with limited gains, indicating that 'more reasoning text' and 'better reasoning structure' should not be treated as equivalent. [S1] [S5]

### Important Gaps

- Does CoT improve latent problem-solving computation, or mainly induce a response format, when answer format and visible explanations are controlled?
- How much of the reported benefit comes from demonstrations carrying useful algorithms or solution patterns rather than from the chain-of-thought format itself?
- Do CoT effects generalize beyond GPQA and mathematical benchmarks to compositional, planning, factual, and adversarial tasks?
- How do model size, instruction tuning, reasoning-token training, decoding strategy, and prompt wording interact with CoT effectiveness?
- Are the large Hi-CoT gains robust under independent replication and against equally token-budgeted non-CoT baselines?

**Analysis Duration:** 18.87s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The current material identifies the principal conditional fault lines—model type, task, metric, default reasoning, and trace structure—but does not directly test the central formatting-versus-reasoning hypothesis. The key cited formatting claim is only reported secondhand, and most positive evidence is secondary or from a single preprint.

**Next Search**

> primary study chain-of-thought prompting formatting effect reasoning quality output format controlled experiment modern LLMs

---

# Iteration 2

## 1. Search

**Query**

> primary study chain-of-thought prompting formatting effect reasoning quality output format controlled experiment modern LLMs

**Why this query**

The current material identifies the principal conditional fault lines—model type, task, metric, default reasoning, and trace structure—but does not directly test the central formatting-versus-reasoning hypothesis. The key cited formatting claim is only reported secondhand, and most positive evidence is secondary or from a single preprint.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S6 — Prompt Engineering Guide: Chain-of-Thought, ReAct & Few-Shot Techniques [2026]**
  URL: https://www.meta-intelligence.tech/en/insight-prompt-engineering
- **S7 — Is Chain-of-Thought Reasoning of LLMs a Mirage? A Data Distribution Lens**
  URL: https://arxiv.org/html/2508.01191v2
- **S8 — Does Prompt Formatting Have Any Impact on LLM Performance?**
  URL: https://arxiv.org/html/2411.10541v1
- **S9 — Chain-of-Thought Prompting Elicits Reasoning in Large Language Models Jason Wei**
  URL: https://arxiv.org/pdf/2201.11903

**Search Duration:** 3.60s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The strongest new evidence supports a conditional, distribution-sensitive account of CoT rather than either a universal reasoning effect or a purely cosmetic formatting effect.

**Confidence:** High

**Why this confidence level**

S7 offers an explicit controlled framework for isolating distribution shifts, and its conditional pattern is consistent with the model- and metric-dependence already reported in S5.

**Evidence**

- S7 reports controlled experiments in which CoT works on in-distribution or near-distribution data but degrades sharply under shifts in task structure, reasoning length, and surface format; fluent traces can remain logically inconsistent. [S7]
- The accumulated S5 results likewise show improvements, null effects, and declines depending on model, task, and evaluation threshold. [S5]

#### Finding 2

**Claim**

CoT can produce genuine task-performance gains in favorable settings, but the original positive findings do not by themselves establish that the visible chain is a faithful account of the computation producing the answer.

**Confidence:** High

**Why this confidence level**

S9 directly documents benchmark gains, while S7 directly documents unfaithful or brittle traces. Together they distinguish effectiveness on some tasks from proof of faithful reasoning.

**Evidence**

- The original CoT study reports substantial gains from few-shot rationale demonstrations across arithmetic, commonsense, and symbolic reasoning, including a large GSM8K improvement for PaLM 540B over standard prompting. [S9]
- S7 gives examples of fluent chains that state correct intermediate rules but end in contradictory conclusions, and reports degradation under distribution shifts, challenging the inference from coherent-looking traces to generalizable reasoning. [S7]

#### Finding 3

**Claim**

A major fault line is distributional generalization: CoT appears substantially more reliable when test problems resemble the task, chain length, and formatting patterns represented in training or demonstrations.

**Confidence:** High

**Why this confidence level**

S7 directly tests the three relevant distribution dimensions; S5 supplies convergent evidence that the effect depends on the model’s learned/default reasoning behavior.

**Evidence**

- S7 frames CoT as a structured inductive bias learned from in-distribution data and reports failure under moderate shifts in task type, chain length, and query format. [S7]
- S5 finds heterogeneous effects across models and reports that some models already emit CoT-like reasoning by default, making the marginal benefit of an explicit cue dependent on the model’s prior behavior. [S5]

#### Finding 4

**Claim**

Prompt formatting is a genuine confound and can independently change benchmark scores, but formatting sensitivity does not demonstrate that CoT benefits are only formatting effects.

**Confidence:** High

**Why this confidence level**

The formatting effect is directly tested, while the limitation of its relevance to the CoT-versus-reasoning causal question follows from the study design described in the source.

**Evidence**

- S8 holds prompt content and meaning constant while varying plain text, Markdown, YAML, and JSON structure, and reports performance differences as large as 40% for GPT-3.5 on one code-translation task, with no universally best format. [S8]
- S8 evaluates general template sensitivity rather than a controlled comparison between a chain-of-thought rationale and a format-matched non-CoT prompt; therefore it establishes that format matters, not that CoT gains reduce to format. [S8]

#### Finding 5

**Claim**

The conflicting literature partly reflects different meanings of 'effective': final-answer accuracy may improve even when reasoning is brittle, inconsistent, or unfaithful under distribution shift.

**Confidence:** High

**Why this confidence level**

Both sources directly document divergences between accuracy, consistency, and trace quality.

**Evidence**

- S7 reports logically inconsistent reasoning despite fluent intermediate steps and sharp degradation under shifts, indicating that surface coherence and generalizable inference can diverge. [S7]
- S5 shows that average accuracy, perfect accuracy, majority correctness, and other thresholds can yield different conclusions, including increased variability and declines for some models. [S5]

#### Finding 6

**Claim**

The practical value of generic CoT is likely highest for models without strong native reasoning behavior and for tasks that align with familiar multistep patterns; its marginal value is smaller and potentially negative for reasoning models or distribution-shifted tasks.

**Confidence:** Medium

**Why this confidence level**

The pattern is supported by two sources but remains benchmark- and model-family-dependent.

**Evidence**

- S5 reports modest gains for some non-reasoning models, small gains or declines for reasoning models, and substantial latency increases from explicit step-by-step prompting. [S5]
- S7 reports that CoT’s apparent reasoning ability is brittle outside near-training distributions. [S7]

#### Finding 7

**Claim**

S6 is weak evidence for the universal effectiveness of CoT and should not override the controlled or comparative findings.

**Confidence:** High

**Why this confidence level**

The source’s genre and the available evidence limit its ability to adjudicate the causal question, even though it summarizes positive claims.

**Evidence**

- S6 presents large headline gains and describes CoT as activating latent reasoning, but the retrieved passage is a practitioner guide summarizing earlier work rather than reporting a controlled separation of reasoning, formatting, demonstrations, and decoding effects. [S6]

### Conflicts Found

- S9 presents CoT as a broadly powerful method across several reasoning benchmarks, whereas S7 argues that the apparent reasoning is brittle and can vanish under distribution shifts. This is a conditional disagreement: S9 emphasizes in-benchmark gains, while S7 tests out-of-distribution robustness and faithfulness. [S9] [S7]
- S6 makes broad practical claims about large CoT improvements, while S5 reports model-dependent gains, null effects, declines, and latency costs. The difference may reflect benchmark/model selection and the non-controlled, survey-like character of S6. [S6] [S5]
- S8 demonstrates that formatting alone can materially affect performance, strengthening the formatting-confound hypothesis; however, neither S8 nor the retrieved S7 passage proves that all CoT gains are formatting-only. [S8] [S7]

### Important Gaps

- Has any controlled study equalized output format, token budget, demonstrations, and answer visibility while comparing CoT against non-CoT prompts on genuinely novel task structures?
- How much of few-shot CoT’s benefit comes from informative solution demonstrations or algorithms rather than the chain format or step-by-step instruction?
- Do S7’s data-distribution findings replicate in pretrained frontier models, rather than only in its controlled from-scratch DataAlchemy setting?
- Can CoT improve performance when the model must provide a separately verifiable formal trace, rather than a natural-language explanation that may be post hoc or inconsistent?
- Are the positive S9-style gains robust under repeated trials, consistency metrics, and adversarial distractors rather than single benchmark accuracy?

**Analysis Duration:** 17.02s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources substantially clarify the fault lines—distribution shift, model capability, evaluation metric, and formatting—but the central causal distinction between computation and formatting remains unresolved. A focused search for controlled CoT-versus-format-matched experiments would materially improve the answer.

**Next Search**

> controlled study chain-of-thought reasoning versus formatting matched prompts output format causal computation faithfulness distribution shift

---

# Iteration 3

## 1. Search

**Query**

> controlled study chain-of-thought reasoning versus formatting matched prompts output format causal computation faithfulness distribution shift

**Why this query**

The new sources substantially clarify the fault lines—distribution shift, model capability, evaluation metric, and formatting—but the central causal distinction between computation and formatting remains unresolved. A focused search for controlled CoT-versus-format-matched experiments would materially improve the answer.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S10 — A comparison of chain-of-thought reasoning strategies across datasets and models**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11157560
- **S11 — Faithful Chain-of-Thought Reasoning - DebugML**
  URL: https://debugml.github.io/fcot
- **S12 — Chain of Thought Prompting Guide**
  URL: https://www.prompthub.us/blog/chain-of-thought-prompting-guide

**Search Duration:** 2.77s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

A small cross-model, cross-dataset study reports that zero-shot CoT-style strategies generally improved performance, but the gains varied by model, dataset, and prompt strategy.

**Confidence:** Medium

**Why this confidence level**

S10 is a peer-reviewed comparative study with multiple models and datasets, but the abstract describes a small-scale experiment and does not establish that the gains are independent of output-format or token-budget effects.

**Evidence**

- S10 compares six LLMs on six question-answering datasets involving real-world knowledge and logical verbal reasoning, and reports that CoT gains remained robust across models and datasets, with GPT-4 benefiting most from the tested strategies. [S10]
- S10 describes the study as small-scale and reports variation among reasoning strategies, so its result supports typical effectiveness in its tested settings rather than universal effectiveness. [S10]

#### Finding 2

**Claim**

The new evidence strengthens the conclusion that CoT can improve answer accuracy, but it does not show that the visible chain is the mechanism responsible for the improvement.

**Confidence:** High

**Why this confidence level**

S10 directly documents performance gains, while S11 directly documents the separate faithfulness problem. Together they support the distinction between effectiveness for final-answer accuracy and faithful causal explanation.

**Evidence**

- S10 reports robust gains from zero-shot reasoning strategies across six models and six datasets, indicating that CoT-like prompting can have practical predictive value. [S10]
- S11 explicitly identifies lack of faithfulness in vanilla CoT: the final answer may not follow from the generated chain, and it presents examples where the answer is absent from or inconsistent with the stated reasoning. [S11]
- S11 proposes a pipeline in which natural-language decomposition is translated into symbolic reasoning and the answer is deterministically computed by an external solver, distinguishing faithful execution from ordinary free-form CoT. [S11]

#### Finding 3

**Claim**

Faithfulness is a separate fault line from formatting: a response can have a reasoning-like format without providing a causally reliable account of how the answer was produced.

**Confidence:** High

**Why this confidence level**

The two sources converge on the distinction between fluent, structured explanations and faithful computation, although S11 is presented through a project webpage rather than the full paper.

**Evidence**

- S11 defines faithfulness as accurately representing the process behind a prediction and states that ordinary CoT does not guarantee that the answer follows from the generated chain. [S11]
- S7 in the accumulated evidence similarly reports fluent but logically inconsistent chains and degradation under distribution shift. [S7]

#### Finding 4

**Claim**

The apparent disagreement between positive CoT studies and skeptical studies is partly conditional: benchmark-aligned prompting can improve accuracy, while robustness, consistency, and faithfulness tests can reveal brittleness or unfaithful traces.

**Confidence:** High

**Why this confidence level**

The positive and skeptical results concern different models, tasks, and evaluation dimensions; the accumulated evidence directly documents these conditional differences.

**Evidence**

- S10 finds generally robust gains in its selected zero-shot QA settings across several models and datasets. [S10]
- S5 reports improvements, null effects, and declines depending on model and evaluation threshold, including increased variability and latency costs. [S5]
- S7 reports sharp degradation when task structure, reasoning length, or surface format shifts, and observes logically inconsistent fluent traces. [S7]

#### Finding 5

**Claim**

Practitioner descriptions of CoT as broadly effective should be treated as background claims rather than strong evidence about the reasoning-versus-formatting causal question.

**Confidence:** High

**Why this confidence level**

The source genre and the reported content clearly limit these sources' ability to adjudicate mechanism, even if they summarize positive practical experience.

**Evidence**

- S12 characterizes CoT as an effective prompt-engineering method and lists many variants, but it is a guide and does not report a controlled experiment equalizing demonstrations, output format, token budget, or answer visibility. [S12]
- S6 in the accumulated evidence has the same limitation: broad positive claims without controlled separation of reasoning, formatting, demonstrations, and decoding effects. [S6]

### Conflicts Found

- S10 reports CoT gains that remain robust across its tested models and datasets, whereas S5 and S7 report null, negative, inconsistent, or distribution-sensitive effects. This is a conditional conflict involving study scale, model generation, tasks, prompt variants, and evaluation criteria rather than a direct contradiction. [S10] [S5] [S7]
- S10 presents CoT-style prompting as improving predictive performance across diverse QA datasets, while S11 argues that vanilla CoT explanations are often unfaithful. These claims address different outcomes—accuracy versus faithful explanation—and therefore are compatible rather than mutually exclusive. [S10] [S11]
- S12 presents CoT as broadly useful and includes claims about variants such as few-shot, self-consistency, and faithful CoT, but its practitioner-guide format provides weaker causal evidence than S10, S5, and S7. [S12] [S10] [S5] [S7]

### Important Gaps

- Did S10 compare CoT against format-matched, token-budget-matched non-CoT prompts, or otherwise isolate intermediate reasoning from changes in output length and structure?
- How much of S10's cross-dataset benefit comes from the reasoning instruction itself versus prompt wording, demonstrations, decoding, or answer-extraction differences?
- Do the positive S10 results persist under repeated-trial consistency measures, adversarial distractors, novel task structures, and explicit faithfulness tests?
- Are Faithful CoT's reported gains in S11 independently replicated against equally token-budgeted and format-matched baselines?
- Can a controlled experiment separately estimate the effects of visible rationale text, latent computation, output formatting, and informative solution demonstrations?

**Analysis Duration:** 15.34s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new evidence improves coverage of positive cross-model results and the faithfulness issue, but it still does not resolve the central causal question: whether CoT's gains remain when formatting, output length, demonstrations, and answer presentation are controlled. That missing controlled comparison is material to the original question.

**Next Search**

> controlled experiment chain-of-thought versus format-matched non-CoT prompt output length token budget reasoning formatting effect

---

# Iteration 4

## 1. Search

**Query**

> controlled experiment chain-of-thought versus format-matched non-CoT prompt output length token budget reasoning formatting effect

**Why this query**

The new evidence improves coverage of positive cross-model results and the faithfulness issue, but it still does not resolve the central causal question: whether CoT's gains remain when formatting, output length, demonstrations, and answer presentation are controlled. That missing controlled comparison is material to the original question.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S13 — Token-Budget-Aware LLM Reasoning**
  URL: https://arxiv.org/html/2412.18547v4
- **S14 — Token-Budget-Aware LLM Reasoning | alphaXiv**
  URL: https://www.alphaxiv.org/abs/2412.18547
- **S15 — Chain of Thought Prompting (CoT): Everything you need to know**
  URL: https://www.vellum.ai/blog/chain-of-thought-prompting-cot-everything-you-need-to-know

**Search Duration:** 2.60s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

CoT reasoning can often be compressed substantially while preserving most answer accuracy, indicating that longer visible traces are not necessarily required for the performance benefit.

**Confidence:** Medium

**Why this confidence level**

The result is directly reported, but both sources describe the same study; S14 is a secondary presentation rather than an independent replication.

**Evidence**

- S13 reports that TALE-EP reduced CoT output tokens by an average of 67% with less than a 3% accuracy decrease, while TALE-PT reduced token use by around 50% with competitive performance. [S13]
- S14 repeats the reported tradeoff, including 81.03% accuracy versus 83.75% for vanilla CoT and large reductions in token use and inference time. [S14]

#### Finding 2

**Claim**

Token-budget interventions show that CoT's extra output has an efficiency cost and that the amount of generated reasoning affects the accuracy-cost tradeoff.

**Confidence:** Medium

**Why this confidence level**

The source provides experimental claims about token usage and accuracy, but it does not isolate whether compressed CoT preserves the same underlying computation or merely changes the response format.

**Evidence**

- S13 states that vanilla CoT produces substantial token overhead and that a reasonable token budget can reduce output from 258 to 86 tokens while retaining a correct answer in an example. [S13]
- S13 reports that overly restrictive budgets can paradoxically increase actual token use, a phenomenon termed “Token Elasticity.” [S13]

#### Finding 3

**Claim**

The new evidence supports treating trace length, reasoning quality, and formatting as separable variables, but it does not resolve whether CoT's accuracy gains are computation-driven or format-driven.

**Confidence:** High

**Why this confidence level**

The combined evidence establishes that output length and surface form matter independently of faithfulness, but no retrieved source performs the decisive format-matched causal comparison.

**Evidence**

- S13's method changes the permitted reasoning length and reports near-preserved accuracy, showing that verbose traces are not always necessary for correct answers. [S13]
- The accumulated S7 and S11 evidence shows that fluent natural-language traces can be logically inconsistent or unfaithful, while S8 shows that formatting alone can affect performance. [S7] [S8] [S11]

#### Finding 4

**Claim**

S14 and S15 add little independent evidence about the central causal question because they are an abstract/summary page and a practitioner guide, respectively.

**Confidence:** High

**Why this confidence level**

The source types and overlapping content limit their value for adjudicating reasoning versus formatting.

**Evidence**

- S14 presents the same TALE study and results as S13 rather than an independent experiment. [S14]
- S15 recommends CoT for non-reasoning models and describes it as useful for accuracy and transparency, but does not control token budget, output format, demonstrations, or answer visibility. [S15]

### Conflicts Found

- S13 reports that much of vanilla CoT's token output can be removed with only a slight accuracy reduction, whereas S1 reports that a structured hierarchical trace can improve accuracy while shortening the trace. These findings are compatible but imply that efficiency depends on how reasoning is organized, not simply on producing fewer tokens. [S13] [S1]
- S13/S14 portray CoT as useful but unnecessarily verbose, while S5 finds that explicit CoT can provide small or negative gains for reasoning-native models. The difference is conditional on model type, task, and the baseline used. [S13] [S14] [S5]
- S13 reports near-preserved benchmark accuracy after token compression, but S7 and S11 raise the separate concern that apparent accuracy and visible reasoning faithfulness can diverge. Thus token efficiency does not establish that the remaining trace is a faithful computation. [S13] [S7] [S11]

### Important Gaps

- Does CoT still improve accuracy when a non-CoT baseline is matched for output format, token budget, demonstrations, and opportunity for latent computation?
- How much of the TALE result reflects removal of redundant explanation tokens versus preservation of an actually useful intermediate computation?
- Are token-compression results robust under repeated-trial consistency, distribution shifts, adversarial distractors, and explicit faithfulness tests?
- Do the reported TALE gains replicate independently across models and tasks, rather than only within the authors' evaluation settings?

**Analysis Duration:** 12.40s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources strengthen the efficiency and model-dependence account, but the original question's decisive fault line remains unanswered: no retrieved study directly equalizes formatting, token budget, demonstrations, and answer visibility while testing whether CoT improves computation rather than merely eliciting a response style. This is an important causal evidence gap, not merely a request for more examples.

**Next Search**

> chain-of-thought prompting format-matched token-budget-matched non-CoT baseline causal experiment reasoning computation output format

---

# Iteration 5

## 1. Search

**Query**

> chain-of-thought prompting format-matched token-budget-matched non-CoT baseline causal experiment reasoning computation output format

**Why this query**

The new sources strengthen the efficiency and model-dependence account, but the original question's decisive fault line remains unanswered: no retrieved study directly equalizes formatting, token budget, demonstrations, and answer visibility while testing whether CoT improves computation rather than merely eliciting a response style. This is an important causal evidence gap, not merely a request for more examples.

**Results**

5 results retrieved.

2 new unique sources added.

### Sources

- **S16 — Chain-of-Thought Prompting — Improve Accuracy by Getting LLMs to Reason | Width.ai**
  URL: https://www.width.ai/post/chain-of-thought-prompting
- **S17 — Medium**
  URL: https://medium.com/@dan_43009/chain-of-thought-prompting-guide-3fdfd1972e03

**Search Duration:** 3.16s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources add little evidence for resolving whether CoT improves reasoning computation or primarily changes output format.

**Confidence:** High

**Why this confidence level**

The sources' genre and contents clearly limit their ability to adjudicate the causal mechanism.

**Evidence**

- S16 is a practitioner survey that reports zero-shot and few-shot CoT gains, but it summarizes earlier studies rather than presenting a controlled CoT-versus-format-matched experiment. [S16]
- S17 is a practitioner guide making broad effectiveness claims and illustrating CoT variants, without controlling output format, token budget, demonstrations, decoding, or answer visibility. [S17]

#### Finding 2

**Claim**

S16 provides additional, but weak, support that CoT-style prompting can improve final-answer accuracy on some arithmetic, symbolic, logical, and commonsense tasks.

**Confidence:** Medium

**Why this confidence level**

The source reports positive and negative outcomes and points to primary studies, but the retrieved content is a secondary summary rather than the underlying controlled results.

**Evidence**

- S16 states that zero-shot CoT outperforms baseline prompting on several tasks, especially arithmetic and symbolic reasoning, while also noting that performance can decrease on some tasks. [S16]
- S16 describes the original few-shot CoT results as outperforming baseline performance on several mathematical, logical, and commonsense datasets. [S16]

#### Finding 3

**Claim**

Zero-shot CoT procedures can alter answer extraction and output-format handling in addition to eliciting intermediate text, making their reported gains difficult to interpret as pure reasoning effects.

**Confidence:** High

**Why this confidence level**

The procedural difference is explicit in the source and directly establishes a confound relevant to the research question.

**Evidence**

- S16 describes a two-step procedure: first generating a rationale and then applying a separate answer-extraction prompt, sometimes followed by manual task- or format-specific cleansing rules. [S16]
- This procedure changes the generation and answer-extraction pipeline relative to a standard direct-answer baseline, so its gains cannot be attributed solely to the presence of reasoning steps. [S16]

#### Finding 4

**Claim**

S17 reinforces the practical consensus that CoT is often useful, but does not challenge the accumulated evidence that usefulness is conditional and does not establish faithful reasoning.

**Confidence:** High

**Why this confidence level**

The source directly makes practical claims while lacking the controls needed to answer the mechanism and faithfulness questions.

**Evidence**

- S17 characterizes CoT as effective and describes improvements from few-shot examples, self-consistency, and related prompting variants. [S17]
- The guide presents CoT as potentially improving transparency and accuracy but supplies no tests of whether the visible rationale causally determines the answer or generalizes under distribution shift. [S17]

### Conflicts Found

- S16 and S17 portray CoT as broadly effective, whereas S5 and S7 report model-, metric-, and distribution-dependent benefits, including null or negative effects and brittle traces. The disagreement is conditional and partly reflects the guides' reliance on selected benchmark results rather than controlled robustness tests. [S16] [S17] [S5] [S7]
- S16's zero-shot procedure includes separate answer extraction and answer-cleansing steps, while the central causal question requires comparing CoT with baselines that hold answer formatting and extraction constant. Thus S16's reported gains cannot directly adjudicate the formatting-only hypothesis. [S16]

### Important Gaps

- Isolate rationale generation from answer-extraction and formatting changes using format-matched, token-budget-matched, and decoding-matched non-CoT baselines.
- Determine how much few-shot CoT gains come from informative demonstrations or embedded solution algorithms rather than from the chain format itself.
- Test whether CoT improves performance on genuinely novel task structures while requiring separately verifiable intermediate steps.

**Analysis Duration:** 11.70s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources are secondary practitioner accounts and do not fill the central evidence gap: a controlled experiment separating visible rationale text, latent computation, output formatting, token budget, demonstrations, and answer extraction. More search could materially improve the answer if it finds such a primary study.

**Next Search**

> primary experiment chain-of-thought formatting-matched non-CoT baseline equal token budget answer extraction causal reasoning

---

# Iteration 6

## 1. Search

**Query**

> primary experiment chain-of-thought formatting-matched non-CoT baseline equal token budget answer extraction causal reasoning

**Why this query**

The new sources are secondary practitioner accounts and do not fill the central evidence gap: a controlled experiment separating visible rationale text, latent computation, output formatting, token budget, demonstrations, and answer extraction. More search could materially improve the answer if it finds such a primary study.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S18 — Causal Sufficiency and Necessity Improves Chain-of-Thought Reasoning**
  URL: https://arxiv.org/html/2506.09853v3
- **S19 — 8 Chain-of-Thought Techniques To Fix Your AI Reasoning | Galileo**
  URL: https://galileo.ai/blog/chain-of-thought-prompting-techniques
- **S20 — Escaping the chain-of-thought trap: What is next for LLM ...**
  URL: https://bdtechtalks.substack.com/p/escaping-the-chain-of-thought-trap

**Search Duration:** 3.32s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

S18 supports the view that CoT quality depends on whether intermediate steps are causally sufficient and necessary, not merely on producing a longer reasoning-like trace.

**Confidence:** Medium

**Why this confidence level**

S18 is a primary preprint with an explicit causal framework and multiple benchmarks, but the retrieved content does not provide detailed experimental controls or independent replication.

**Evidence**

- S18 defines sufficiency as whether the intermediate steps comprehensively support the conclusion and necessity as whether particular steps are indispensable; it reports that causal intervention can add missing steps and prune redundant ones. [S18]
- S18 describes redundant, incomplete, and ideally sufficient-and-necessary reasoning patterns, and reports improved efficiency with maintained or improved accuracy on GSM8K, MATH-500, AIME, and CommonsenseQA. [S18]

#### Finding 2

**Claim**

S18 adds evidence that verbose CoT is not inherently beneficial: unnecessary steps can increase inefficiency or even harm performance, while pruning can preserve accuracy.

**Confidence:** Medium

**Why this confidence level**

The direction of the reported result is clear, but the retrieved passage does not establish whether the gains come from better computation, better demonstrations, or altered output structure.

**Evidence**

- S18 identifies redundancy and “overthinking” as problems and presents causal pruning of unnecessary steps as a way to reduce token usage without sacrificing accuracy. [S18]
- The source reports improvements across mathematical and commonsense benchmarks after reconstructing shorter, causally informed reasoning traces. [S18]

#### Finding 3

**Claim**

S18 does not resolve the central reasoning-versus-formatting question because its intervention operates on reasoning traces and demonstrations rather than comparing CoT with a format-, token-, and decoding-matched non-CoT baseline.

**Confidence:** High

**Why this confidence level**

The stated method and experimental setup directly show that the source addresses trace optimization, not the decisive format-only causal comparison.

**Evidence**

- S18 reconstructs CoT responses and uses them as in-context demonstrations or fine-tuning data; it does not report a comparison that holds output format, token budget, demonstrations, answer extraction, and decoding constant while removing the rationale. [S18]
- Its causal sufficiency and necessity measures concern the influence of steps within a CoT trace, not whether the entire visible trace is causally responsible for the model’s improved answer relative to a non-CoT prompt. [S18]

#### Finding 4

**Claim**

S18’s results are compatible with both a computation-sensitive and a demonstration/format-sensitive interpretation of CoT.

**Confidence:** Medium

**Why this confidence level**

This is an inference from the described design; the source does not separately estimate the effects of trace content, trace format, and latent computation.

**Evidence**

- The source reports that optimized traces improve in-context learning and supervised fine-tuning, meaning the intervention changes the content and structure of demonstrations as well as the reasoning sequence. [S18]
- Because shorter, more logically complete demonstrations may convey useful algorithms or task structure, the reported gains cannot be attributed uniquely to causal internal reasoning by the model at inference time. [S18]

#### Finding 5

**Claim**

S19 provides practical positive claims about CoT but is weak evidence for the causal research question.

**Confidence:** High

**Why this confidence level**

The source genre and absence of the relevant controls make it unsuitable for deciding whether CoT improves reasoning computation or primarily changes formatting.

**Evidence**

- S19 characterizes standard and zero-shot CoT as improving accuracy on structured tasks and recommends several CoT variants, while acknowledging longer responses and plausible-sounding incorrect reasoning. [S19]
- The retrieved article is a practitioner guide and does not report a controlled comparison equalizing output format, token budget, demonstrations, answer extraction, or decoding. [S19]

#### Finding 6

**Claim**

S20 presents a strong skeptical interpretation of CoT, but the retrieved source is commentary and therefore does not materially strengthen the empirical case beyond the already accumulated faithfulness and distribution-shift evidence.

**Confidence:** Medium

**Why this confidence level**

Its claims align with S7 and S11, but the source itself is secondary and rhetorically framed.

**Evidence**

- S20 argues that models can produce correct answers with flawed or incoherent chains and logical chains with wrong answers, and portrays CoT as a potentially brittle output constraint rather than a faithful computation. [S20]
- S20 is a commentary article that summarizes other work; the retrieved passage does not supply the methods, datasets, controls, or effect sizes needed to independently verify those claims. [S20]

### Conflicts Found

- S18 portrays causally optimized CoT as improving accuracy and efficiency, whereas S20 portrays visible CoT as largely an illusion and costly text bottleneck. This is not a clean contradiction: S18 evaluates optimized traces on selected benchmarks, while S20 emphasizes faithfulness, distribution shift, and computational cost. [S18] [S20]
- S19 describes CoT as a practical transformation into a more transparent problem solver, while S20 argues that fluent traces can be structurally decoupled from the computation producing the answer. The disagreement concerns whether visible explanations should be interpreted as faithful reasoning, not whether CoT can sometimes improve benchmark accuracy. [S19] [S20]
- S18 reports that pruning and reconstructing reasoning traces can preserve or improve accuracy, while earlier S13/S1 evidence likewise suggests that shorter or better-structured traces can outperform verbose CoT. These results challenge the assumption that more intermediate text equals more reasoning, but they do not establish that less text is equivalent to no reasoning. [S18] [S13] [S1]

### Important Gaps

- Does S18’s causal intervention improve the model’s underlying problem-solving computation, or mainly improve the informativeness and format of demonstrations?
- Would S18’s method retain its gains against a format-matched, token-budget-matched non-CoT baseline with identical answer extraction and decoding?
- Are S18’s results independently replicated across models, especially reasoning-native frontier models, and under distribution shifts or adversarial distractors?
- Do causal sufficiency and necessity scores measure genuine causal dependence or only dependence within the generated textual trace?

**Analysis Duration:** 17.13s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new primary source improves the account of how useful CoT traces may be optimized, but the decisive causal question remains unanswered: no retrieved source isolates visible rationale text and formatting from latent computation, informative demonstrations, answer extraction, token budget, and decoding. The practitioner and commentary sources do not fill that gap.

**Next Search**

> Kambhampati chain-of-thought correct answers flawed reasoning format structural constraint controlled study faithfulness

---

# Iteration 7

## 1. Search

**Query**

> Kambhampati chain-of-thought correct answers flawed reasoning format structural constraint controlled study faithfulness

**Why this query**

The new primary source improves the account of how useful CoT traces may be optimized, but the decisive causal question remains unanswered: no retrieved source isolates visible rationale text and formatting from latent computation, informative demonstrations, answer extraction, token budget, and decoding. The practitioner and commentary sources do not fill that gap.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S21 — Faithful Chain-of-Thought Reasoning**
  URL: https://www.cis.upenn.edu/~ccb/publications/faithful-chain-of-thought-reasoning.pdf
- **S22 — What Is Chain-of-Thought Faithfulness? Why AI Reasoning Traces Are Unreliable | MindStudio**
  URL: https://www.mindstudio.ai/blog/what-is-chain-of-thought-faithfulness-ai-reasoning
- **S23 — Measuring and Improving the Faithfulness of Model-Generated Reasoning  — LessWrong**
  URL: https://www.lesswrong.com/posts/BKvJNzALpxS3LafEs/measuring-and-improving-the-faithfulness-of-model-generated
- **S24 — The “Unfaithful” Chain-of-Thought: Debunking Anthropomorphic Claims in LLM Research**
  URL: https://medium.com/@iryna.nozdrin/the-unfaithful-chain-of-thought-debunking-anthropomorphic-claims-in-llm-research-f6981f998116

**Search Duration:** 2.48s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Faithfulness is now supported as an independent fault line: standard CoT can improve accuracy while failing to faithfully represent the computation that produced the answer.

**Confidence:** High

**Why this confidence level**

S21 is a primary research paper with an explicit definition, concrete example, and proposed intervention; it converges with S7 and S11.

**Evidence**

- The primary Faithful CoT paper states that standard CoT chains do not necessarily reflect how the model arrives at an answer and gives a GSM8K example whose final answer is absent from, and unsupported by, the preceding rationale. [S21]
- S21 distinguishes faithfulness from correctness and plausibility: a chain can be understandable yet not causally determine the answer. [S21]
- This directly reinforces earlier evidence that fluent traces can be post-hoc or logically inconsistent even when benchmark accuracy improves. [S7] [S11]

#### Finding 2

**Claim**

A faithful, solver-grounded reasoning pipeline can outperform ordinary CoT, but this demonstrates the value of executable structure and verification—not necessarily that ordinary visible CoT improves latent computation.

**Confidence:** High

**Why this confidence level**

The method and comparative results are directly described in the primary source, while the causal limitation follows from the intervention design.

**Evidence**

- Faithful CoT translates natural-language queries into mixed natural-language and symbolic reasoning chains, then uses a deterministic solver to derive the answer. [S21]
- Across 10 datasets in four domains, S21 reports that Faithful CoT outperformed standard CoT on 9 of 10 benchmarks, with relative gains reported for math word problems, planning, multi-hop QA, and relational inference. [S21]
- The intervention changes both the reasoning representation and the answer-generation mechanism by adding symbolic execution, so its gains cannot be attributed specifically to ordinary CoT prompting. [S21]

#### Finding 3

**Claim**

Faithfulness and answer accuracy can be synergistic, but faithful explanation is achieved in S21 by enforcing execution of the reasoning chain rather than by trusting free-form natural-language rationales.

**Confidence:** High

**Why this confidence level**

The source makes the execution guarantee and its limitation explicit.

**Evidence**

- S21 reports state-of-the-art few-shot results on seven datasets with GPT-4 and Codex and argues that faithful reasoning need not trade off against performance. [S21]
- The paper explicitly guarantees faithfulness of the chain-to-answer stage because a deterministic solver executes the symbolic reasoning chain; it does not claim that the language-model translation stage itself is interpretable. [S21]

#### Finding 4

**Claim**

The newer faithfulness evidence supports a conditional account: whether a model uses its generated CoT depends on the task and model, rather than being uniformly causal or uniformly cosmetic.

**Confidence:** Medium

**Why this confidence level**

S23 summarizes primary-paper abstracts rather than presenting the full methods and results, but its conditional pattern converges with S5 and earlier evidence.

**Evidence**

- The summarized Anthropic experiments report large variation in answer sensitivity to CoT interventions: models rely heavily on CoT for some tasks and largely ignore it for others. [S23]
- The summary reports greater sensitivity for logical reasoning tasks and lower sensitivity for crystallized-knowledge tasks, consistent with CoT sometimes functioning as computation and sometimes as post-hoc explanation. [S23]
- S5 independently reports model-dependent gains, null effects, declines, and default CoT-like behavior. [S5]

#### Finding 5

**Claim**

The available evidence weakens two simplistic explanations of CoT gains—'just extra tokens' and 'just particular wording'—but does not establish a purely computation-driven effect.

**Confidence:** Medium

**Why this confidence level**

The evidence addresses filler-token and paraphrase hypotheses, but the decisive format- and pipeline-matched comparison remains absent from the retrieved material.

**Evidence**

- The Anthropic study summary reports evidence against CoT gains being solely due to additional test-time computation or the particular phrasing of the generated chain. [S23]
- However, S23 does not show that the relevant comparison held output format, answer extraction, demonstrations, decoding, and token budget fully constant. [S23]
- S8 shows that prompt formatting independently affects performance, while S16 shows that CoT procedures can change answer extraction and cleansing. [S8] [S16]

#### Finding 6

**Claim**

The apparent conflicts are best explained by differences in what studies mean by success: benchmark accuracy, causal dependence on the trace, faithfulness, consistency, robustness, and efficiency are distinct outcomes.

**Confidence:** High

**Why this confidence level**

Multiple sources directly document divergences among accuracy, faithfulness, consistency, and distributional robustness.

**Evidence**

- S21 reports strong accuracy gains from a solver-grounded approach while also arguing that ordinary CoT is not necessarily faithful. [S21]
- S5 finds that average accuracy, perfect accuracy, majority correctness, and variability can point in different directions. [S5]
- S7 reports degradation under shifts in task structure, reasoning length, and surface format, even where traces remain fluent. [S7]
- S23 reports task- and model-specific differences in whether answers depend on generated CoT. [S23]

#### Finding 7

**Claim**

The strongest current conclusion is neither 'CoT is reasoning' nor 'CoT is only formatting': CoT is an effective but conditional elicitation strategy, while visible natural-language chains are unreliable evidence of the underlying computation.

**Confidence:** High

**Why this confidence level**

This synthesis is supported by convergent positive, skeptical, and methodological evidence, with the remaining causal limitation explicitly identified.

**Evidence**

- Original and comparative studies report substantial gains on selected reasoning and QA benchmarks. [S9] [S10]
- Controlled and faithfulness-focused evidence reports brittle generalization, unfaithful traces, and task/model variation in dependence on CoT. [S7] [S21] [S23]
- Formatting, token length, extraction, and demonstration content remain plausible contributors because existing studies do not fully isolate them. [S8] [S13] [S16] [S18]

### Conflicts Found

- S21 reports that solver-grounded Faithful CoT outperforms standard CoT on most tested benchmarks, whereas S5 reports that generic explicit CoT can have small, null, or negative effects, especially for reasoning-native models. This is conditional rather than a direct contradiction because S21 changes the representation and adds deterministic solving. [S21] [S5]
- S21 presents a strong synergy between faithfulness and accuracy, while S23 summarizes evidence that ordinary models sometimes ignore their generated CoT and produce post-hoc rationalizations. The difference concerns ordinary free-form CoT versus an execution-grounded framework. [S21] [S23]
- S23 reports evidence against explaining CoT gains solely through extra test-time compute or rationale phrasing, but S8 and S16 show that formatting and answer-extraction changes can independently affect performance. These findings leave a narrower but unresolved formatting and pipeline confound. [S23] [S8] [S16]
- S23 reports inverse scaling in faithfulness, with larger models ignoring their generated reasoning more often on most studied tasks, while S21 reports strong GPT-4 and Codex results for Faithful CoT. This is compatible because S21 uses symbolic execution and evaluates accuracy, whereas S23 concerns faithfulness of ordinary generated CoT. [S23] [S21]
- S22 broadly claims that CoT traces are unreliable and often post-hoc, while S23 reports that CoT can be quite faithful for some task-model combinations. S22 is a practitioner article and does not establish the conditional empirical pattern as precisely as S23. [S22] [S23]

### Important Gaps

- Does ordinary CoT improve latent problem-solving computation when output format, token budget, demonstrations, answer extraction, and decoding are all matched against a non-CoT baseline?
- How much of few-shot CoT's benefit comes from informative demonstrations or embedded solution algorithms rather than the chain format itself?
- Do the Anthropic faithfulness findings in S23 replicate from the full primary study across modern frontier and reasoning-native models?
- Do S21's Faithful CoT gains persist against equally structured but non-executable, format-matched baselines?
- How much of Faithful CoT's improvement comes from deterministic symbolic solving versus better decomposition, more constrained outputs, or improved error checking?
- Can natural-language CoT itself be made reliably faithful without an external solver, especially under distribution shift?
- Do positive accuracy gains persist under repeated-trial consistency, adversarial distractors, and genuinely novel task structures?

**Analysis Duration:** 21.73s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new primary source substantially strengthens the distinction between accuracy and faithfulness, and the summarized Anthropic evidence narrows the hypotheses about extra tokens and phrasing. However, the central causal question—whether ordinary CoT beats a format-, token-, extraction-, demonstration-, and decoding-matched non-CoT baseline—remains unanswered in the retrieved material. A primary-source search for the Anthropic intervention experiments could materially improve precision about what was actually controlled.

**Next Search**

> "Measuring Faithfulness in Chain-of-Thought Reasoning" filler tokens paraphrasing early answering adding mistakes primary paper

---

# Iteration 8

## 1. Search

**Query**

> "Measuring Faithfulness in Chain-of-Thought Reasoning" filler tokens paraphrasing early answering adding mistakes primary paper

**Why this query**

The new primary source substantially strengthens the distinction between accuracy and faithfulness, and the summarized Anthropic evidence narrows the hypotheses about extra tokens and phrasing. However, the central causal question—whether ordinary CoT beats a format-, token-, extraction-, demonstration-, and decoding-matched non-CoT baseline—remains unanswered in the retrieved material. A primary-source search for the Anthropic intervention experiments could materially improve precision about what was actually controlled.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S25 — Measuring Faithfulness in Chain-of-Thought Reasoning | alphaXiv**
  URL: https://www.alphaxiv.org/abs/2307.13702
- **S26 — Measuring Faithfulness in Chain-of-Thought Reasoning**
  URL: https://arxiv.org/pdf/2307.13702
- **S27 — Zhihui Xie's Homepage | Measuring Faithfulness in Chain-of-Thought Reasoning**
  URL: https://zhxie.site/blog/2023-09-19-faithfulness
- **S28 — Measuring Faithfulness in Chain-of-Thought Reasoning | Takara TLDR**
  URL: https://tldr.takara.ai/p/2307.13702
- **S29 — Measuring Faithfulness in Chain-of-Thought Reasoning \ Anthropic**
  URL: https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning

**Search Duration:** 2.70s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources substantially strengthen the evidence that CoT is not uniformly faithful: its causal influence varies by task, and some generated chains appear partly post hoc.

**Confidence:** High

**Why this confidence level**

S26 is the primary paper and directly describes the interventions and conclusions; S27 independently summarizes the experimental patterns.

**Evidence**

- The primary paper uses truncation and injected-error interventions and reports that models sometimes rely heavily on CoT and sometimes largely ignore it, with large task-level variation. [S26]
- The same paper reports that the degree of faithfulness is not strongly correlated with the size of CoT’s accuracy improvement, so accuracy gains do not establish that the visible chain caused the answer. [S26] [S27]

#### Finding 2

**Claim**

The evidence weakens both the 'CoT is merely extra computation' and the 'CoT encodes useful information in its exact wording' explanations, but it does not prove that CoT gains are computation-driven rather than formatting- or pipeline-driven.

**Confidence:** High

**Why this confidence level**

The primary study directly tests filler and paraphrase hypotheses. The remaining limitation follows from what those interventions do and do not compare.

**Evidence**

- Replacing generated CoT with uninformative filler tokens did not produce an accuracy gain, arguing against a pure extra-token or context-length explanation. [S26]
- Paraphrased CoT produced similar performance to original CoT, arguing against the exact wording or hidden steganographic phrasing being the primary source of the benefit. [S26] [S27]
- These interventions do not equalize all relevant variables against a non-CoT baseline, including answer format, extraction procedure, demonstrations, and decoding. [S26] [S16] [S8]

#### Finding 3

**Claim**

CoT can be genuinely useful for final-answer accuracy while remaining an unreliable explanation of the model's underlying computation.

**Confidence:** High

**Why this confidence level**

This distinction is explicit in the primary paper and converges with the earlier Faithful CoT and distribution-shift evidence.

**Evidence**

- The study begins from observed CoT performance improvements across its tasks but finds that the model may ignore or alter the chain without correspondingly changing its answer. [S26]
- The paper defines faithfulness as accurately representing the process behind a prediction and treats answer sensitivity to interventions as a probe of that property, rather than equating readable rationales with faithful computation. [S26]

#### Finding 4

**Claim**

Faithfulness is conditional on task and model characteristics, with larger or more capable models in the study often producing less faithful chains rather than automatically more faithful ones.

**Confidence:** High

**Why this confidence level**

The result is directly reported in the primary paper, though its generality beyond the tested models and tasks remains uncertain.

**Evidence**

- S26 reports that faithfulness varies substantially across tasks and that smaller models often generate more faithful reasoning than larger models on the studied tasks. [S26]
- The study concludes that model size and task selection are useful levers for obtaining more faithful CoT, rather than faithfulness being an inherent property of the prompting method. [S26] [S29]

#### Finding 5

**Claim**

The new sources do not resolve the central causal question of whether ordinary CoT improves latent problem-solving computation or primarily changes response structure.

**Confidence:** High

**Why this confidence level**

The primary paper's design and the duplicated nature of the other new sources are clear from the retrieved content.

**Evidence**

- S26 tests whether the model uses the generated chain and whether filler or paraphrase preserve performance, but it does not present the decisive format-, token-, extraction-, demonstration-, and decoding-matched non-CoT comparison. [S26]
- S25, S27, S28, and S29 largely reproduce or summarize the same faithfulness study rather than providing independent causal evidence. [S25] [S27] [S28] [S29]
- Other accumulated evidence shows that formatting and answer extraction can independently affect results, leaving those factors as live confounds. [S8] [S16]

### Conflicts Found

- The new primary study reports that CoT can be ignored on some tasks and becomes less faithful with increasing model capability, whereas positive CoT studies report broad accuracy gains. This is a conditional disagreement between predictive effectiveness and causal faithfulness, not a direct contradiction. [S26] [S9] [S10]
- S26 finds no benefit from uninformative filler tokens, while the formatting-confound evidence shows that prompt structure can independently change performance. Thus filler-token failure rules out one simple extra-compute account but does not rule out broader formatting or answer-pipeline effects. [S26] [S8]
- S25, S27, S28, and S29 present the same 2023 faithfulness results through an aggregator, blog, TLDR, and institutional summary; they should not be counted as independent replications of S26. [S25] [S26] [S27] [S28] [S29]

### Important Gaps

- Does ordinary CoT outperform a non-CoT prompt when output format, token budget, demonstrations, answer extraction, and decoding are all matched?
- How much of few-shot CoT's benefit comes from informative solution demonstrations rather than from the chain format or step-by-step instruction?
- Do the faithfulness findings replicate in current reasoning-native frontier models and on genuinely novel task structures?
- Can CoT improve performance while requiring a separately verifiable intermediate trace, without relying on an external symbolic solver?
- How do repeated-trial consistency, adversarial distractors, and distribution shifts alter the apparent CoT benefit?

**Analysis Duration:** 14.76s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new material is valuable primary evidence about faithfulness and eliminates two simplistic explanations, but it duplicates evidence already accumulated and leaves the decisive formatting-versus-computation comparison unanswered. A focused search for a controlled, format- and budget-matched ablation could materially sharpen the answer.

**Next Search**

> chain-of-thought causal effect format-matched non-CoT baseline rationale ablation token-budget matched answer extraction

---

# Iteration 9

## 1. Search

**Query**

> chain-of-thought causal effect format-matched non-CoT baseline rationale ablation token-budget matched answer extraction

**Why this query**

The new material is valuable primary evidence about faithfulness and eliminates two simplistic explanations, but it duplicates evidence already accumulated and leaves the decisive formatting-versus-computation comparison unanswered. A focused search for a controlled, format- and budget-matched ablation could materially sharpen the answer.

**Results**

5 results retrieved.

1 new unique source added.

### Sources

- **S30 — Chain-of-Thought Prompting: Helping LLMs Learn by ...**
  URL: https://deepgram.com/learn/chain-of-thought-prompting-guide

**Search Duration:** 2.32s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

S30 provides additional secondary support that few-shot CoT can improve benchmark accuracy on arithmetic, commonsense, and symbolic reasoning tasks, especially for sufficiently large models and more difficult problems.

**Confidence:** Medium

**Why this confidence level**

The source is a secondary engineering guide summarizing the original study rather than presenting new experimental analysis or independent replication.

**Evidence**

- S30 summarizes Wei et al.’s results across several model families and reports that CoT benefits were small below roughly 100B parameters, while larger models showed substantially greater gains, including on GSM8K and other math benchmarks. [S30]
- S30 explains that the original comparison used ordinary few-shot input-output examples versus few-shot examples containing intermediate rationales, and reports gains on the selected arithmetic, commonsense, and symbolic tasks. [S30]

#### Finding 2

**Claim**

S30 does not materially resolve whether CoT’s gains reflect improved reasoning computation or changes in demonstrations and output format.

**Confidence:** High

**Why this confidence level**

The relevant comparison and the absence of causal controls are explicit in the source and directly concern the central research question.

**Evidence**

- S30 describes the original baseline as few-shot examples containing only final answers, while the CoT condition adds intermediate steps; this changes demonstration content, response structure, and likely generation length simultaneously. [S30]
- The source reports benchmark accuracy but does not describe format-matched, token-budget-matched, extraction-matched, or decoding-matched non-CoT controls, nor faithfulness or distribution-shift tests. [S30]
- This limitation is consistent with existing evidence that formatting and answer extraction can independently affect performance and that visible chains may be unfaithful. [S8] [S16] [S21] [S26]

#### Finding 3

**Claim**

S30 reinforces a model- and task-dependent account of CoT rather than a universal one, but it does not challenge the newer evidence that CoT can be brittle or post hoc.

**Confidence:** High

**Why this confidence level**

S30 adds descriptive evidence of scale and difficulty dependence, while the accumulated primary evidence independently establishes conditional effectiveness and faithfulness problems.

**Evidence**

- S30 reports that CoT benefits emerge mainly at large scale and increase with task difficulty, rather than appearing uniformly across model sizes and tasks. [S30]
- Existing controlled and faithfulness-focused studies report null or negative effects for some models, distribution-sensitive performance, and weak dependence of answers on the visible chain. [S5] [S7] [S26]

### Conflicts Found

- S30 presents the original CoT results as broad gains on selected benchmarks, whereas S5, S7, and S26 report model-dependent effects, distribution-shift failures, and cases where the model does not causally rely on its visible chain. This is a conditional disagreement: S30 emphasizes in-distribution benchmark accuracy, while the latter sources examine robustness, consistency, and faithfulness. [S30] [S5] [S7] [S26]
- S30’s comparison adds rationale-bearing demonstrations to final-answer-only demonstrations, so its positive result is compatible with the possibility that useful demonstration content, formatting, or answer-generation differences—not only a reasoning computation—caused part of the gain. [S30] [S8] [S16]

### Important Gaps

- Whether the original scale-dependent CoT gains persist against non-CoT prompts matched for demonstration information, output format, token budget, answer extraction, and decoding.
- How much of few-shot CoT’s benefit comes from the informative worked examples themselves rather than from the visible chain-of-thought format.
- Whether the reported gains remain under repeated-trial consistency tests, adversarial distractors, novel task structures, and explicit faithfulness interventions.

**Analysis Duration:** 11.91s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

S30 is a secondary summary of already represented positive CoT evidence and does not address the decisive causal gap. The accumulated research state already supports a responsible synthesis: CoT often improves final-answer accuracy under aligned conditions, but its benefits are model-, task-, metric-, and distribution-dependent, and visible natural-language traces are not reliable evidence of faithful reasoning. Further searching could locate the ideal format-matched experiment, but the current evidence is sufficient to explain the literature’s main fault lines without pretending that the causal question is resolved.

**Stop Reason:** sufficient_evidence

---

# Final Research Decision

**Research Stopped Because**

The analyzer determined that the important parts of the question could be answered responsibly.

**Stop Reason:** sufficient_evidence

**Searches Performed:** 9

**Unique Sources:** 30

**Remaining Uncertainty**

- A decisive experiment would compare ordinary CoT with a non-CoT baseline matched for output format, token budget, demonstrations, answer extraction, decoding, and opportunity for latent computation.
- The contribution of informative worked examples or embedded solution algorithms must be separated from the contribution of the chain format or step-by-step instruction.
- The robustness of positive CoT effects should be tested with repeated trials, strict consistency metrics, adversarial distractors, novel task structures, and distribution shifts.
- It remains unclear whether natural-language CoT can be made reliably faithful without symbolic execution or an external deterministic solver.
- The independent replication and generalization of the reported token-compression, hierarchical-CoT, causal-pruning, and Faithful-CoT gains remain incompletely established in the retrieved material.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 9 | 26.29s |
| OpenAI Analysis | 9 | 140.85s |
| Report Generation | 1 | 23.74s |
| Total Run | — | 190.88s |
