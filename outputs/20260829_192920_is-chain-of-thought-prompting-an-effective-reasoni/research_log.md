# Research Run Log

## Run Summary

**Research Question**

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees-find the real fault lines and explain what accounts for the conflicting results.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 10

**OpenAI Calls:** 4

**Tavily Calls:** 3

**Started:** 2026-08-29T19:29:20-04:00

**Ended:** 2026-08-29T19:30:19-04:00

**Total Runtime:** 58.47s

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

- **S1 — Hierarchical Chain-of-Thought Prompting: Enhancing LLM Reasoning Performance and Efficiency**
  URL: https://arxiv.org/html/2604.00130v1
- **S2 — The Decreasing Value of Chain of Thought in Prompting**
  URL: https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought
- **S3 — Contrastive Chain-Of-Thought Prompting**
  URL: https://www.kore.ai/blog/contrastive-chain-of-thought-prompting
- **S4 — What is chain of thought (CoT) prompting?**
  URL: https://www.ibm.com/think/topics/chain-of-thoughts
- **S5 — Medium**
  URL: https://cobusgreyling.medium.com/chain-of-thought-prompting-in-llms-1077164edf97

**Search Duration:** 3.20s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Chain-of-thought prompting is not uniformly effective; its impact depends substantially on the model’s built-in reasoning capability, task, and evaluation metric.

**Confidence:** Medium

**Why this confidence level**

The source describes a repeated-trial evaluation across several models and metrics, but the retrieved material is an institutional summary rather than the full primary report.

**Evidence**

- A 2025 GPQA Diamond study reports modest average gains for non-reasoning models, minimal gains for reasoning models, and performance declines for some models. It also finds that results vary between average accuracy, majority accuracy, and perfect-accuracy thresholds. [S2]

#### Finding 2

**Claim**

For non-reasoning models, CoT can improve difficult-task accuracy, but it may also increase answer variability and harm cases that would have been answered correctly directly.

**Confidence:** Medium

**Why this confidence level**

The reported model-by-model pattern directly supports conditional benefits and costs, though detailed statistical tables are not included in the retrieved text.

**Evidence**

- On GPQA Diamond, CoT reportedly improved average performance for non-reasoning models, with gains ranging from 4.4% to 13.5%; however, perfect-accuracy results were mixed, including a 17.2% decline for Gemini Pro 1.5 and no significant change for GPT-4o. [S2]

#### Finding 3

**Claim**

For models with native reasoning mechanisms, a generic request to think step by step adds little reasoning value relative to its cost.

**Confidence:** Medium

**Why this confidence level**

The finding is based on a multi-model repeated-trial comparison, but the source does not expose the full experimental design or significance calculations.

**Evidence**

- The study reports only 2.9% and 3.1% average improvements for o3-mini and o4-mini, respectively, and a 3.3% decline for Gemini Flash 2.5, while CoT increased response time by 20–80%. [S2]

#### Finding 4

**Claim**

Some apparent CoT benefits may reflect elicitation of an output format or reasoning behavior that models already produce, rather than the prompt creating a new reasoning capability.

**Confidence:** Low

**Why this confidence level**

This is central to the formatting-versus-reasoning distinction, but the retrieved evidence is indirect: S1 cites the claim without presenting that study’s results, and S2 reports default CoT-like behavior without isolating formatting effects experimentally.

**Evidence**

- The retrieved Hi-CoT paper states that recent work finds CoT exemplars primarily enforce output format for modern LLMs. The Wharton summary likewise reports that many models produce CoT-like outputs by default even without an explicit CoT instruction. [S1] [S2]

#### Finding 5

**Claim**

The useful component of CoT may be structure rather than verbosity: imposing planning, decomposition, or intermediate constraints can outperform an unstructured linear trace while reducing token use.

**Confidence:** Low

**Why this confidence level**

The reported results are directly stated, but the source is a recent preprint and the retrieved excerpt does not provide controls, statistical analyses, or independent replication.

**Evidence**

- Hi-CoT reports a 6.2% average accuracy improvement and a 13.9% reduction in trace length relative to ordinary CoT across 13 model configurations and five mathematical benchmarks; it attributes the effect to adaptive planning and compression bottlenecks. [S1]

#### Finding 6

**Claim**

The main fault lines suggested by the retrieved evidence are model regime, task difficulty, metric choice, and prompt structure—not a simple opposition between CoT reasoning and formatting.

**Confidence:** Medium

**Why this confidence level**

Multiple retrieved sources converge on these conditional moderators, although only one source supplies empirical comparative results and the sources do not directly test every proposed mechanism.

**Evidence**

- Benefits differ between non-reasoning and reasoning models; difficult-task average accuracy differs from perfect-accuracy outcomes; default behavior sometimes already resembles CoT; and structured Hi-CoT claims gains over flat CoT. [S1] [S2]

### Conflicts Found

- S1 presents CoT as substantially improving reasoning and claims structured Hi-CoT produces large accuracy gains, whereas S2 finds generic CoT produces marginal benefits for reasoning models and sometimes decreases performance. [S1] [S2]
- The sources differ over whether CoT exemplars mainly improve reasoning or primarily enforce output format. S1 reports the latter as a finding from cited recent work, while S4 and S5 describe CoT as improving multistep reasoning; however, S4 and S5 are explanatory/promotional sources rather than controlled comparative studies. [S1] [S4] [S5]
- S2 reports that CoT can improve average performance while reducing perfect-accuracy performance for some models. Thus whether CoT is beneficial depends on the chosen correctness threshold, not only on the underlying task. [S2]

### Important Gaps

- Does CoT improve latent problem-solving ability when output format, answer length, and opportunity for additional tokens are carefully matched against direct prompting?
- Which specific tasks benefit from explicit intermediate reasoning, and which merely benefit from additional computation or answer-format constraints?
- Are the large Hi-CoT gains robust under independent replication and against strong baselines such as equal-token direct prompting, self-consistency, or native reasoning modes?
- How much of the apparent benefit comes from few-shot demonstrations versus the instruction to produce intermediate steps?
- Do visible reasoning traces faithfully represent the causal process producing the answer, or can formatting improve accuracy without making the trace a reliable explanation?

**Analysis Duration:** 13.67s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The retrieved material supports a conditional account but does not yet resolve the question’s central causal issue: whether CoT improves reasoning beyond formatting, extra computation, or output regularization. The strongest formatting claim is only second-hand, while the positive evidence includes non-peer-reviewed or explanatory sources. A primary controlled study directly comparing reasoning and formatting-matched conditions would materially improve the answer.

**Next Search**

> chain-of-thought prompting output format versus reasoning controlled study Cheng 2025

---

# Iteration 2

## 1. Search

**Query**

> chain-of-thought prompting output format versus reasoning controlled study Cheng 2025

**Why this query**

The retrieved material supports a conditional account but does not yet resolve the question’s central causal issue: whether CoT improves reasoning beyond formatting, extra computation, or output regularization. The strongest formatting claim is only second-hand, while the positive evidence includes non-peer-reviewed or explanatory sources. A primary controlled study directly comparing reasoning and formatting-matched conditions would materially improve the answer.

**Results**

5 results retrieved.

2 new unique sources added.

### Sources

- **S6 — PromptHub Blog: Chain of Thought Prompting Guide**
  URL: https://www.prompthub.us/blog/chain-of-thought-prompting-guide
- **S7 — Chain-of-Thought (CoT) Prompting**
  URL: https://www.promptingguide.ai/techniques/cot

**Search Duration:** 1.65s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources support the practical claim that CoT can improve performance on some elementary multistep arithmetic and classification examples, but they do not establish that it is a generally effective reasoning strategy.

**Confidence:** Low

**Why this confidence level**

The evidence consists of selected demonstrations on tutorial pages, without systematic baselines, model details, statistical analysis, or broad task coverage.

**Evidence**

- Prompting Guide presents examples where few-shot CoT and zero-shot “Let’s think step by step” produce correct arithmetic answers after direct prompting produced an incorrect answer. [S7]
- PromptHub describes CoT as useful for complex tasks and illustrates the same distinction between answer-only and step-by-step demonstrations. [S6]

#### Finding 2

**Claim**

Few-shot CoT and zero-shot CoT are distinct interventions, so claims about “CoT” can conflate demonstrations containing rationales with a simple instruction to generate intermediate steps.

**Confidence:** High

**Why this confidence level**

Both sources explicitly make this definitional distinction, although they do not experimentally isolate the causal contribution of each component.

**Evidence**

- Prompting Guide separately describes few-shot CoT, in which worked examples include reasoning chains, and zero-shot CoT, in which the prompt adds “Let’s think step by step.” [S7]
- PromptHub likewise distinguishes simple step-by-step instructions from elaborate few-shot, self-consistency, and automated variants. [S6]

#### Finding 3

**Claim**

CoT’s apparent benefit can depend on the structure and quality of demonstrations, not merely on asking for a longer visible rationale.

**Confidence:** Medium

**Why this confidence level**

The sources directly describe demonstration selection and variant structure, but provide no controlled comparison showing which component causes gains.

**Evidence**

- The description of Auto-CoT says it selects diverse demonstrations and generates rationale chains, while acknowledging that generated chains can contain mistakes and that diversity is used to mitigate this problem. [S7]
- PromptHub lists structured variants such as self-consistency, step-back, contrastive, faithful, and tabular CoT, implying that prompt structure changes the intervention being evaluated. [S6]

#### Finding 4

**Claim**

The new sources reinforce, rather than resolve, the formatting-versus-reasoning fault line: they define CoT partly by visible intermediate output and acknowledge that such traces may be unfaithful.

**Confidence:** Medium

**Why this confidence level**

The sources explicitly connect CoT to visible format and acknowledge faithfulness limitations, but they do not perform the controlled causal tests needed to settle the issue.

**Evidence**

- PromptHub defines CoT as requiring the model to show how it reached an answer and states that reasoning chains are not always faithful or correct. [S6]
- Prompting Guide presents intermediate reasoning steps as the mechanism enabling complex reasoning, but its examples do not test whether the steps causally improve latent problem solving or merely constrain output format. [S7]

#### Finding 5

**Claim**

The tutorials’ broad claims of effectiveness are in tension with the accumulated evidence that CoT benefits are conditional on model regime, metric, and task.

**Confidence:** Medium

**Why this confidence level**

The disagreement is clear, but the tutorial sources are not comparable in evidentiary strength to systematic evaluations and may be presenting pedagogical examples rather than general estimates.

**Evidence**

- PromptHub calls CoT broadly effective and applicable to essentially anything requiring reasoning. [S6]
- Prompting Guide says CoT enables complex reasoning and highlights successful examples. [S7]
- The accumulated GPQA evidence reports modest, mixed, or negative effects depending on whether the model is a native reasoning model and whether average or perfect accuracy is measured. [S2]

### Conflicts Found

- S6 and S7 make broad effectiveness claims based on illustrative examples, while S2 finds generic CoT gains are model- and metric-dependent, with declines for some models. The disagreement is likely partly explained by selective examples and by different model/task regimes, rather than a direct like-for-like contradiction. [S2] [S6] [S7]
- S6 and S7 treat producing intermediate steps as evidence of enhanced reasoning, but the accumulated findings note that modern models may already produce CoT-like behavior and that visible traces may primarily impose format. The tutorials do not test this alternative explanation. [S1] [S6] [S7]

### Important Gaps

- Whether the arithmetic examples in S6 and S7 survive equal-token or equal-computation direct-prompt baselines.
- Whether few-shot rationale demonstrations help because of reasoning supervision, answer-format imitation, additional contextual information, or some combination.
- Whether CoT gains generalize across difficult reasoning tasks rather than selected toy examples.
- Whether visible CoT traces are causally involved in solving or are post-hoc/partly unfaithful representations.
- How much of Auto-CoT’s reported value comes from demonstration diversity and selection versus the generated reasoning chains themselves.

**Analysis Duration:** 10.16s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources are tutorial and promotional material with anecdotal demonstrations. They clarify terminology and prompt variants but do not answer the central causal question or resolve the conflict with systematic, model-sensitive results. A focused search for controlled evaluations matching token budget, output format, and computation would materially improve the answer.

**Next Search**

> chain-of-thought prompting controlled comparison equal token budget output format reasoning versus formatting

---

# Iteration 3

## 1. Search

**Query**

> chain-of-thought prompting controlled comparison equal token budget output format reasoning versus formatting

**Why this query**

The new sources are tutorial and promotional material with anecdotal demonstrations. They clarify terminology and prompt variants but do not answer the central causal question or resolve the conflict with systematic, model-sensitive results. A focused search for controlled evaluations matching token budget, output format, and computation would materially improve the answer.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S8 — The Token Economics of Chain-of-Thought: When Thinking Out Loud Costs More Than It's Worth**
  URL: https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more
- **S9 — Chain of Thought Prompting in AI: A Comprehensive Guide [2026]**
  URL: https://orq.ai/blog/what-is-chain-of-thought-prompting
- **S10 — What is Chain of Thought Prompting? (2026)**
  URL: https://www.youtube.com/watch?v=Qe7DxM5PxPs&vl=en

**Search Duration:** 2.43s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources reinforce that CoT is conditionally useful rather than universally effective, especially for difficult sequential reasoning tasks and weaker/non-native reasoning models.

**Confidence:** Medium

**Why this confidence level**

S8 is consistent with S2, but it is an industry blog summarizing research rather than a primary controlled study.

**Evidence**

- S8 claims CoT improved average accuracy by 11–13% for non-reasoning models on difficult reasoning tasks, while also stating that it can fail to help or hurt on other task types. [S8]
- The accumulated GPQA evidence similarly found gains for some non-reasoning models but marginal or negative effects for native reasoning models. [S2]

#### Finding 2

**Claim**

CoT can impose substantial token and latency costs, making its value depend on the accuracy improvement relative to added computation.

**Confidence:** Medium

**Why this confidence level**

The direction of the cost tradeoff is supported by two sources, but the precise figures in S8 are secondary and the sources do not establish a standardized cost-controlled comparison.

**Evidence**

- S8 reports 2–5× higher token usage and substantially longer response times for CoT, while citing only modest gains for reasoning models and no significant improvement in some model-task combinations. [S8]
- The accumulated study summary reports 20–80% longer responses for native reasoning models under explicit CoT, with only 2.9–3.1% average gains for two models and a decline for another. [S2]

#### Finding 3

**Claim**

The new evidence supports an ‘overthinking’ mechanism: longer visible traces can introduce variability and errors after the model has already reached a correct answer.

**Confidence:** Medium

**Why this confidence level**

The two sources converge on the phenomenon, but the retrieved material does not provide the underlying trial-level analysis needed to distinguish overthinking from other causes.

**Evidence**

- S8 states that CoT can cause errors on questions answered correctly under direct prompting and attributes this to second-guessing, irrelevant tangents, and accumulated mistakes; it cites a 17.2% perfect-accuracy decline for Gemini Pro 1.5. [S8]
- S2 independently reports the same model-specific decline in perfect-accuracy performance and notes that CoT can increase answer variability. [S2]

#### Finding 4

**Claim**

Explicit CoT is plausibly redundant for models with native reasoning mechanisms, but the current sources do not establish that it is always redundant or that the extra tokens constitute ‘reasoning twice.’

**Confidence:** Medium

**Why this confidence level**

The performance pattern is supported, while the mechanistic explanation remains an interpretation rather than a directly tested result.

**Evidence**

- S8 characterizes explicit CoT on models with built-in reasoning as redundant and reports only small accuracy gains with increased latency. [S8]
- S2 reports minimal or negative gains for several reasoning models, but does not demonstrate that explicit CoT duplicates internal reasoning or identify the causal mechanism. [S2]

#### Finding 5

**Claim**

The token-cost results strengthen the case that useful CoT may be computation or structured intermediate state, not necessarily verbose natural-language explanation.

**Confidence:** Low

**Why this confidence level**

Both sources support the hypothesis, but S8 is a blog and S1 is a recent preprint excerpt; neither retrieved source supplies strong equal-computation, equal-token, or independent replication controls.

**Evidence**

- S8 reports that concise methods such as Chain-of-Draft, concise CoT, and token-budgeted reasoning can reduce output length substantially while reportedly preserving or sometimes improving accuracy. [S8]
- S1 similarly attributes gains over ordinary CoT to adaptive planning and compression, with shorter traces and higher reported accuracy. [S1]

#### Finding 6

**Claim**

The new tutorial and video sources should not be treated as evidence that CoT generally improves reasoning; they mainly provide conventional definitions and illustrative or pedagogical claims.

**Confidence:** High

**Why this confidence level**

The sources’ genre and content are directly observable: they explain or promote CoT rather than report comparative experimental evidence.

**Evidence**

- S9 presents CoT as a technique that enhances reasoning and accuracy, but the retrieved content supplies no controlled evaluation or causal comparison. [S9]
- S10 makes broad claims about improved accuracy, transparency, and reliability while acknowledging longer processing time and the possibility of flawed reasoning; it provides no systematic experiment. [S10]

### Conflicts Found

- S8 and S2 emphasize conditional, sometimes negative effects and substantial costs, whereas S9 and S10 describe CoT in broadly positive terms as an accuracy- and reasoning-improvement technique. This is primarily a difference in evidentiary standard and scope, not a direct like-for-like contradiction. [S2] [S8] [S9] [S10]
- S8 interprets weak gains on native reasoning models as redundancy of explicit CoT, while S2 reports the performance pattern without proving that redundancy is the cause. The disagreement is mechanistic rather than numerical. [S2] [S8]
- S8 presents concise reasoning methods and early stopping as preserving accuracy at much lower token cost, while S1 reports gains for structured Hi-CoT. These claims are compatible, but neither source provides the strong baseline controls needed to determine whether shorter traces, adaptive structure, or additional computation is responsible. [S1] [S8]

### Important Gaps

- Do CoT gains survive comparisons matched for output-token budget, total computation, latency, and answer-format constraints?
- Does visible natural-language reasoning causally improve solving, or does it mainly provide a workspace, format constraint, or additional sampling opportunity?
- Are the token-reduction and early-stopping figures in S8 supported by primary peer-reviewed or independently replicated studies?
- How do few-shot rationale demonstrations compare with zero-shot step-by-step instructions when context length and answer format are matched?
- Does CoT improve difficult reasoning tasks beyond benchmark-specific effects, and how does that interact with native internal reasoning modes?

**Analysis Duration:** 12.06s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The runner reached the maximum research iteration budget. Analyzer assessment: The new sources clarify the practical cost/benefit fault line but do not resolve the central causal question. The strongest remaining gap is controlled evidence separating reasoning from formatting, extra tokens, and computation; most new claims are secondary or tutorial material.

**Stop Reason:** max_iterations

---

# Final Research Decision

**Research Stopped Because**

The runner reached the maximum research iteration budget.

**Stop Reason:** max_iterations

**Searches Performed:** 3

**Unique Sources:** 10

**Remaining Uncertainty**

- A controlled comparison matching direct prompting and CoT for output-token budget, total computation, latency, and response format.
- A causal test separating rationale demonstrations from the mere instruction to produce intermediate steps.
- Evidence testing whether visible natural-language traces are faithful to the process that produced the answer.
- Independent replication of the reported Hi-CoT, Chain-of-Draft, early-stopping, and token-budget results.
- Broader evaluation across difficult reasoning tasks and realistic task mixtures, rather than selected examples or a single benchmark.
- A direct comparison of explicit CoT with models’ native internal reasoning modes under matched resource budgets.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 7.28s |
| OpenAI Analysis | 3 | 35.90s |
| Report Generation | 1 | 15.29s |
| Total Run | — | 58.47s |
