# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

**Status:** Completed

**Stop Reason:** sufficient_evidence

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 8 / 10

**Unique Sources:** 31

**OpenAI Calls:** 9

**Tavily Calls:** 8

**Started:** 2026-09-01T06:21:48-04:00

**Ended:** 2026-09-01T06:24:36-04:00

**Total Runtime:** 167.82s

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

- **S1 — The Decreasing Value of Chain of Thought in Prompting**
  URL: https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought
- **S2 — What is Chain of Thought (CoT) Prompting?**
  URL: https://www.nvidia.com/en-us/glossary/cot-prompting
- **S3 — What is chain of thought (CoT) prompting?**
  URL: https://www.ibm.com/think/topics/chain-of-thoughts
- **S4 — Chain of Thought Prompting (CoT): Everything you need to know**
  URL: https://www.vellum.ai/blog/chain-of-thought-prompting-cot-everything-you-need-to-know
- **S5 — 8 Chain-of-Thought Techniques To Fix Your AI Reasoning**
  URL: https://galileo.ai/blog/chain-of-thought-prompting-techniques

**Search Duration:** 2.95s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

CoT is not uniformly effective; its value depends strongly on model type, task difficulty, and evaluation metric.

**Confidence:** Medium

**Why this confidence level**

The pattern is directly reported in S1, but most corroborating material is secondary and promotional rather than independent primary research.

**Evidence**

- A 2025 GPQA Diamond study reports modest average gains for non-reasoning models but minimal or negative effects for reasoning-native models, with results changing substantially under perfect-accuracy, high-accuracy, and majority-correct metrics. [S1]
- Industry explainers characterize CoT as especially useful for multistep arithmetic, symbolic, commonsense, and planning tasks, while warning that smaller or reasoning-native models may gain less. [S2] [S3] [S4]

#### Finding 2

**Claim**

For older or non-reasoning models, explicit CoT can improve difficult-task accuracy, but it may also increase variability and harm cases where a direct answer would have been correct.

**Confidence:** Medium

**Why this confidence level**

The evidence supports conditional gains, but the GSM8K statistic is presented secondhand and the retrieved material does not establish whether gains arise from reasoning, demonstrations, extra tokens, or benchmark-specific effects.

**Evidence**

- On GPQA Diamond, S1 reports average improvements for several non-reasoning models, including larger gains for Gemini Flash 2.0 and Sonnet 3.5, while some models declined on the stricter 100%-correct metric; Gemini Pro 1.5 reportedly fell by 17.2%. [S1]
- The same study says CoT-like reasoning often occurs under the default prompt, and that forcing a direct answer can prevent useful natural reasoning. [S1]
- S4 reports the classic GSM8K contrast in which a CoT intervention raised accuracy from 17.7% to 40.7%, illustrating that large gains are possible on particular multistep benchmarks. [S5]

#### Finding 3

**Claim**

For reasoning-native models, generic “think step by step” prompting appears to add little accuracy relative to its latency and token cost.

**Confidence:** Medium

**Why this confidence level**

S1 provides direct comparative results, but only one retrieved empirical study is available and its exact statistical tables and experimental controls are not included in the source content.

**Evidence**

- S1 reports only 2.9% and 3.1% average improvements for o3-mini and o4-mini, a 3.3% decline for Gemini Flash 2.5, and 20–80% longer response times for reasoning models. [S1]
- S4 similarly states that newer reasoning models incorporate step-by-step processing natively, reducing the need for ordinary CoT prompts. [S4]

#### Finding 4

**Claim**

The central conceptual fault line is between eliciting additional computation and merely eliciting a longer, more structured-looking answer; the retrieved sources do not resolve that distinction.

**Confidence:** Medium

**Why this confidence level**

The sources clearly motivate the distinction, but none of the retrieved material directly tests rationale faithfulness or isolates formatting effects from extra test-time compute.

**Evidence**

- S1 compares direct, explicit step-by-step, and default conditions, and notes that default outputs are often already CoT-like. This suggests that visible CoT wording is not equivalent to uniquely added reasoning. [S1]
- S2–S5 describe intermediate text as helping decomposition, error checking, and transparency, but they do not provide evidence that displayed rationales are causally faithful accounts of the computation producing the answer. [S2] [S3] [S4] [S5]
- S4 explicitly recommends allowing the model to reason while surfacing only the final answer, separating internal computation from output formatting in deployment practice. [S4]

#### Finding 5

**Claim**

Benchmarking methodology is a major source of apparently conflicting results.

**Confidence:** High

**Why this confidence level**

This methodological distinction is explicitly described in the empirical source and directly explains how positive and negative findings can coexist.

**Evidence**

- S1 repeats each GPQA question 25 times and evaluates complete accuracy, high accuracy, majority correctness, and average rating; it states that one-shot testing can hide inconsistency and that different correctness thresholds materially change conclusions. [S1]
- S1 finds that CoT can improve average performance while reducing perfect accuracy for some models, showing how the selected metric can reverse the apparent judgment about effectiveness. [S1]

#### Finding 6

**Claim**

CoT has practical costs that complicate claims of effectiveness even when accuracy improves.

**Confidence:** Medium

**Why this confidence level**

The cost findings are directly reported by S1, while the broader reliability claims are mainly from practitioner explainers.

**Evidence**

- S1 reports 35–600% longer responses for non-reasoning models and 20–80% longer responses for reasoning models, with corresponding latency and token-use increases. [S1]
- S4 and S5 also identify longer outputs, cost, and plausible-but-wrong rationales as limitations. [S4] [S5]

### Conflicts Found

- Promotional and explanatory sources present CoT as substantially improving reasoning and accuracy, whereas S1 finds diminishing or negative returns, especially for reasoning-native models. [S1] [S2] [S3] [S4] [S5]
- S1 reports that explicit CoT can improve average performance but reduce perfect accuracy for some non-reasoning models. Thus, CoT is beneficial under average or majority metrics but harmful under strict consistency metrics for particular model/task combinations. [S1]
- The sources differ in what they call CoT: some describe few-shot demonstrations containing written rationales, while S1 primarily tests a generic “think step by step” suffix and compares it with default behavior. These are not necessarily the same intervention. [S1] [S3] [S4] [S5]

### Important Gaps

- How much of classic CoT’s reported benefit comes from demonstrations and task-specific exemplars versus the generic instruction to think step by step?
- Do visible rationales causally mediate correct answers, or are they post-hoc verbalizations whose main effects are formatting, verbosity, and answer-selection behavior?
- How do results change when controlling for the number of generated tokens or equalizing test-time compute across direct and CoT conditions?
- Are the GPQA findings general across mathematics, symbolic reasoning, commonsense reasoning, coding, planning, and factual retrieval, or are they specific to expert multiple-choice questions?
- How much do temperature, sampling strategy, self-consistency, prompt wording, and answer-format constraints account for the observed variability?
- The retrieved evidence does not include the primary classic CoT papers or systematic studies designed specifically to separate reasoning gains from formatting and extra-compute effects.

**Analysis Duration:** 18.38s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The current evidence supports a conditional answer and identifies likely fault lines, but it does not adequately adjudicate the original literature dispute. In particular, primary comparative evidence is needed on rationale faithfulness, token-matched controls, few-shot versus zero-shot CoT, and task/model differences.

**Next Search**

> chain-of-thought prompting causal reasoning versus formatting token-matched control rationale faithfulness primary study

---

# Iteration 2

## 1. Search

**Query**

> chain-of-thought prompting causal reasoning versus formatting token-matched control rationale faithfulness primary study

**Why this query**

The current evidence supports a conditional answer and identifies likely fault lines, but it does not adequately adjudicate the original literature dispute. In particular, primary comparative evidence is needed on rationale faithfulness, token-matched controls, few-shot versus zero-shot CoT, and task/model differences.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S6 — Why Models Know But Don’t Say:Chain-of-Thought Faithfulness Divergence Between Thinking Tokensand Answers in Open-Weight Reasoning Models**
  URL: https://arxiv.org/html/2603.26410
- **S7 — Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?**
  URL: https://arxiv.org/html/2603.22582v1
- **S8 — Faithful Chain-of-Thought Reasoning Qing Lyu ∗ Shreya Havaldar∗ Adam Stein∗**
  URL: https://www.cis.upenn.edu/~ccb/publications/faithful-chain-of-thought-reasoning.pdf
- **S9 — The Last Word Often Wins: A Format Confound in Chain-of-Thought Corruption Studies**
  URL: https://arxiv.org/html/2605.10799
- **S10 — Measuring Faithfulness in Chain-of-Thought Reasoning Tamera Lanham**
  URL: https://www-cdn.anthropic.com/827afa7dd36e4afbb1a49c735bfbb2c69749756e/measuring-faithfulness-in-chain-of-thought-reasoning.pdf

**Search Duration:** 3.01s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Visible CoT should not be treated as a faithful transcript of the computation that produced an answer.

**Confidence:** High

**Why this confidence level**

Multiple sources using intervention, executable reasoning, and cross-channel methods converge on the distinction between generated explanation text and the actual causal basis of an answer, although they operationalize faithfulness differently.

**Evidence**

- Lanham et al. find that models vary substantially across tasks in how much their answers depend on the displayed CoT; truncating, corrupting, or paraphrasing the chain sometimes changes answers and sometimes does not. They also report that larger models can become less faithful on many studied tasks. [S10]
- The proposed Faithful CoT framework explicitly distinguishes interpretability from correctness and guarantees faithfulness only because a deterministic solver executes the generated symbolic reasoning chain; the natural-language translation itself is not claimed to be interpretable. [S8]
- In misleading-hint experiments, reasoning models often acknowledge the hint in thinking tokens while omitting it from the visible answer, and faithfulness varies widely by model and hint type. The study measures acknowledgment/divergence rather than faithfulness directly, so it is evidence of channel mismatch rather than a complete causal account. [S6] [S7]

#### Finding 2

**Claim**

The literature’s apparent disagreement partly reflects different meanings of “CoT” and different causal questions: prompting for a rationale, supplying few-shot rationale demonstrations, generating extra tokens, and exposing a reasoning trace are not equivalent interventions.

**Confidence:** High

**Why this confidence level**

The sources explicitly distinguish these interventions and show that changing the intervention changes both performance and interpretability conclusions.

**Evidence**

- S1’s comparison primarily concerns direct answering, a generic step-by-step suffix, and default prompting, while the classic CoT framing in S8 describes few-shot exemplars containing written reasoning chains. [S1] [S8]
- Lanham et al. separately test extra tokens, particular phrasing, and dependence on the generated chain. Replacing CoT with uninformative filler did not produce the same accuracy gain, while paraphrased CoT performed similarly, arguing against a simple explanation based solely on token count or exact wording in their setting. [S10]
- Faithful CoT changes the architecture by translating natural language into executable symbolic steps and using a deterministic solver; its improvements therefore cannot be interpreted as evidence that ordinary free-form CoT alone is faithful. [S8]

#### Finding 3

**Claim**

Formatting and answer placement can create strong apparent evidence for reasoning dependence, especially in corruption-based faithfulness tests.

**Confidence:** Medium

**Why this confidence level**

The reported ablations directly support a formatting confound, but the result is recent, scoped to particular formats and models, and does not by itself explain performance gains during original answer generation.

**Evidence**

- S9 reports that, for benchmark chains ending in an explicit terminal answer line, removing or corrupting only that suffix changes measured sensitivity dramatically, while preserving intermediate reasoning. Models often follow a wrong explicit terminal answer over correct intermediate reasoning, indicating a readout or answer-placement effect. [S9]
- S9’s scope is limited mainly to explicit-answer-line formats and 3B–32B open-weight models; it does not establish that all CoT benefits are formatting effects or that naturally occurring chains behave identically. [S9]

#### Finding 4

**Claim**

The strongest current interpretation is conditional: CoT can improve task accuracy for some non-reasoning models and difficult tasks, but its benefit is not equivalent to faithful reasoning and may disappear or reverse for other models, metrics, or formats.

**Confidence:** High

**Why this confidence level**

The evidence supports a conditional rather than universal judgment and covers benchmark performance, causal interventions, and an explicitly faithful alternative. However, the sources do not establish one universal mechanism for every CoT prompt.

**Evidence**

- S1 reports gains for several non-reasoning models but small or negative effects for some reasoning-native models, with conclusions changing under average, majority-correct, and perfect-accuracy metrics. [S1]
- S10 finds that CoT performance boosts are not explained by filler-token computation alone or by exact rationale phrasing, but also finds substantial task-dependent variation in whether models causally use the chain. [S10]
- S8 reports consistent gains from a constrained, executable reasoning framework over standard CoT on nine of ten benchmarks, suggesting that making intermediate structure computationally binding can improve both accuracy and explanation faithfulness. [S8]

### Conflicts Found

- S10 reports that replacing CoT with filler text did not preserve the CoT performance gain, whereas the broader question and some prior interpretations allow extra test-time computation to be a possible mechanism. This is not necessarily a direct contradiction: S10 tests a particular filler intervention and model/task set, while later reasoning-native systems and other prompts may use hidden or differently structured computation. [S1] [S10]
- S9 argues that corruption studies can primarily measure terminal-answer placement, while S10 interprets changes after truncation or corruption as evidence about whether models condition on CoT. The studies use different formats and controls, so some published “faithfulness” effects may be format sensitivity rather than dependence on intermediate reasoning. [S9] [S10]
- S8 reports that executable symbolic reasoning improves accuracy and guarantees a faithful answer derivation, while S6 and S7 show that ordinary reasoning traces can diverge from visible answers or from the factors influencing them. These findings concern different systems: Faithful CoT binds solving to an external solver, whereas the divergence studies examine free-form reasoning models. [S6] [S7] [S8]
- Faithfulness rates in S7 and channel-divergence rates in S6 are not interchangeable. S7 uses a classifier/judge to estimate acknowledgment of hint influence, while S6 uses keyword matching separately on thinking and answer channels and explicitly says it does not directly measure faithfulness. [S6] [S7]

### Important Gaps

- How much of classic few-shot CoT’s benefit survives controls for demonstrations, answer placement, output format, and equalized test-time compute?
- Do the S10 filler results generalize to modern reasoning-native models, hidden thinking tokens, and tasks beyond its evaluated assistant model?
- Can accuracy gains be decomposed into genuine intermediate computation, answer-selection/readout heuristics, improved error checking, and formatting or compliance effects?
- How general is S9’s terminal-answer confound when chains do not end with an explicit answer line or when the answer is extracted independently from the rationale?
- Do faithfulness interventions predict correctness, or can a rationale be causally used yet still be wrong, misleading, or incomplete?
- The new sources are recent preprints and mostly study open-weight or specific proprietary models; independent replications and broader task coverage remain limited.

**Analysis Duration:** 17.65s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

A focused search would materially improve the answer by addressing the central unresolved fault line: studies that directly compare CoT with direct answering while controlling for generated-token budget, answer placement, and rationale demonstrations. The current sources establish that both genuine conditional benefits and formatting/readout confounds exist, but do not quantify their relative contribution across model generations.

**Next Search**

> chain-of-thought prompting controlled test-time compute answer format demonstrations direct answering token budget empirical study

---

# Iteration 3

## 1. Search

**Query**

> chain-of-thought prompting controlled test-time compute answer format demonstrations direct answering token budget empirical study

**Why this query**

A focused search would materially improve the answer by addressing the central unresolved fault line: studies that directly compare CoT with direct answering while controlling for generated-token budget, answer placement, and rationale demonstrations. The current sources establish that both genuine conditional benefits and formatting/readout confounds exist, but do not quantify their relative contribution across model generations.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S11 — Wait, Do We Need to Wait? Revisiting Budget Forcing for Sequential Test-Time Scaling | ICLR Blogposts 2026**
  URL: https://iclr-blogposts.github.io/2026/blog/2026/wait-do-we-need-to-wait
- **S12 — Chain-of-Thought Prompting: A Guide for LLM Apps and Agents**
  URL: https://www.comet.com/site/blog/chain-of-thought-prompting
- **S13 — CoT2-Meta: Budgeted Metacognitive Control for Test-Time Reasoning**
  URL: https://arxiv.org/html/2603.28135v1

**Search Duration:** 2.22s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Additional test-time reasoning can improve accuracy for reasons beyond merely producing longer or better-formatted outputs, but the benefit depends on how computation is allocated and controlled.

**Confidence:** Medium

**Why this confidence level**

S13 directly reports token-matched improvements across many benchmarks, but it is a single recent preprint and the retrieved text does not provide enough methodological detail to independently assess its controls or whether the controller’s gains are attributable specifically to natural-language CoT.

**Evidence**

- CoT2-Meta reports gains over single-path, sampling, and search baselines under matched inference budgets across MATH, GPQA, GSM8K, BBEH, MMMU-Pro, HLE, and a broader 15-benchmark suite. It attributes the gains to selective expansion, pruning, repair, stopping, and abstention rather than brute-force token increases. [S13]
- The matched-budget claim complements S10’s finding that uninformative filler tokens did not reproduce the performance of CoT, suggesting that some structured intermediate computation—not merely verbosity—can matter. [S10] [S13]

#### Finding 2

**Claim**

The meaningful mechanism is not simply “asking for more words,” but structuring and selectively managing intermediate computation.

**Confidence:** Medium

**Why this confidence level**

The sources support a control-versus-verbosity distinction, but S13 evaluates a compound framework rather than isolating each component, and S11 is an ICLR blogpost rather than a primary peer-reviewed study.

**Evidence**

- CoT2-Meta separates object-level thought generation from meta-level control and makes explicit decisions about expanding, pruning, repairing, stopping, or abstaining; its reported advantages include better scaling, calibration, selective prediction, and targeted repair under matched budgets. [S13]
- Budget-forcing results show that increasing the reasoning budget produces gains for some models but plateaus or fluctuates for others, undermining a universal relationship between more thinking tokens and better performance. [S11]

#### Finding 3

**Claim**

Prompt wording and formatting can themselves control whether and how a model continues reasoning, so lexical triggers are not evidence of a universally shared reasoning mechanism.

**Confidence:** Medium

**Why this confidence level**

Both sources directly report format- and keyword-sensitive effects, but they cover limited model families and formats and do not establish how often these effects explain original CoT accuracy gains.

**Evidence**

- S11 reports that budget forcing is model-family dependent, that instruction-tuned models can sometimes benefit from ellipsis structures, and that “Wait” is not special: alternatives such as “Let” or “Perhaps” can work better depending on the model. [S11]
- S9 finds that explicit terminal-answer placement can dominate measured sensitivity in corruption tests; models may follow a wrong terminal answer despite correct intermediate reasoning, indicating a readout or answer-placement effect. [S9]

#### Finding 4

**Claim**

The new evidence sharpens the central fault line: ordinary CoT prompting, sequential test-time scaling, and metacognitive search are related but distinct interventions.

**Confidence:** High

**Why this confidence level**

The sources explicitly describe materially different interventions, supporting the conclusion that conflicting results may compare unlike forms of “CoT.”

**Evidence**

- S11 treats budget forcing as sequential test-time scaling that controls continuation and truncation of a reasoning block, while S13 adds branching, process evaluation, repair, and abstention. These interventions manipulate computation allocation, not just the surface request to show work. [S11] [S13]
- S1 primarily compares direct answering, a generic step-by-step suffix, and default prompting; S8 describes few-shot rationale demonstrations; S10 separately tests extra tokens, wording, and causal dependence on generated chains. [S1] [S8] [S10]

### Conflicts Found

- S13 reports robust matched-budget gains from a process-aware CoT controller, whereas S11 finds that simply increasing or forcing reasoning budgets often plateaus, fluctuates, or hurts performance. This is a conditional rather than direct contradiction: selective control may help where uniform budget expansion does not. [S11] [S13]
- S11 suggests that arbitrary alternative keywords can trigger useful continuation, which supports a formatting or control-channel account; S13 attributes gains to process-aware trajectory management. The results concern different interventions, so keyword sensitivity does not refute computation-based gains from structured control. [S11] [S13]
- S12 presents classic CoT as a broadly effective reasoning technique and repeats large benchmark gains, while S1, S9, S10, and S11 show model-, metric-, format-, and intervention-dependent effects. S12 is a secondary practitioner guide and does not resolve these causal distinctions. [S12] [S1] [S9] [S10] [S11]

### Important Gaps

- Does CoT2-Meta’s advantage come from the reasoning traces themselves, from the process oracle and controller, or from search, verification, and abstention independently of visible rationales?
- Do the matched-budget comparisons in S13 equalize total model FLOPs, generated tokens, controller calls, and evaluator computation, or only a subset of inference costs?
- How much of classic few-shot CoT’s benefit survives controls for demonstrations, answer placement, output format, and equalized test-time compute?
- Do keyword- and delimiter-sensitive effects in S11 generalize beyond the tested model families and reasoning-token formats?
- Can process-aware systems improve correctness while still generating explanations that are non-faithful or post-hoc?
- Independent replications are still needed, especially for the recent S11 and S13 claims and for tasks beyond the reported benchmarks.

**Analysis Duration:** 14.84s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources strengthen the case that structured, selectively allocated inference computation can improve accuracy beyond formatting alone, but they do not isolate the causal contribution of ordinary visible CoT from demonstrations, search, verification, controller decisions, or extra computation. That unresolved distinction is central to the original question.

**Next Search**

> chain-of-thought causal ablation matched compute demonstrations answer format rationale mediation LLM reasoning

---

# Iteration 4

## 1. Search

**Query**

> chain-of-thought causal ablation matched compute demonstrations answer format rationale mediation LLM reasoning

**Why this query**

The new sources strengthen the case that structured, selectively allocated inference computation can improve accuracy beyond formatting alone, but they do not isolate the causal contribution of ordinary visible CoT from demonstrations, search, verification, controller decisions, or extra computation. That unresolved distinction is central to the original question.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S14 — [PDF] LLM Reasoning Is Latent, Not the Chain of Thought - arXiv**
  URL: https://arxiv.org/pdf/2604.15726
- **S15 — CASE: Causal Alignment and Structural Enforcement for Improving Chain-of-Thought Faithfulness**
  URL: https://arxiv.org/html/2607.18820v1
- **S16 — [Paper Summary] Chain-of-Thought Prompting Elicits Reasoning in Large Language Models**
  URL: https://dhruvil.substack.com/p/paper-summary-chain-of-thought-prompting
- **S17 — What Is Chain-of-Thought Reasoning in LLMs? | VDF AI**
  URL: https://vdf.ai/resources/chain-of-thought
- **S18 — Chain-of-Thought Prompting Explained: The Complete Step-by-Step Guide**
  URL: https://appliedaihub.org/blog/chain-of-thought-prompting-explained

**Search Duration:** 2.25s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

A useful synthesis is to distinguish surface CoT, latent-state trajectories, and generic serial compute; apparent disagreement often arises because experiments change all three simultaneously.

**Confidence:** High

**Why this confidence level**

The distinction is made explicitly in S14 and is consistent with the prior empirical sources, though the sources do not establish a single mechanism across all tasks.

**Evidence**

- S14 explicitly separates surface trace content (S), latent task-relevant state trajectories (Z), and generic serial computation (B), arguing that ordinary CoT changes both visible traces and compute allocation rather than isolating one causal factor. [S14]
- The accumulated evidence likewise distinguishes few-shot rationale demonstrations, generic step-by-step instructions, extra token generation, sequential budget forcing, and process-aware search as different interventions. [S1] [S8] [S10] [S11] [S13]

#### Finding 2

**Claim**

The newest evidence favors latent computation as the default interpretation of reasoning, not faithful visible CoT, but this is a working hypothesis rather than a universal conclusion.

**Confidence:** Medium

**Why this confidence level**

S14 is a position paper that reorganizes evidence and reports additional analyses, not an independent consensus review; its conclusion is therefore informative but not decisive.

**Evidence**

- S14 argues that current evidence most strongly supports latent-state trajectory mediation (H1), while treating surface CoT as a partial interface; it also says surface-trace and generic-compute explanations can remain locally valid in some regimes. [S14]
- Lanham et al. found task-dependent causal dependence on displayed chains, and the prior evidence shows that visible rationales can diverge from answer-generating factors. [S10] [S6] [S7]

#### Finding 3

**Claim**

Faithful CoT is not a property that ordinary autoregressive prompting guarantees; it requires suppressing shortcuts from the instruction directly to the answer.

**Confidence:** Medium

**Why this confidence level**

The causal formulation is direct, but CASE is a recent preprint and its reported improvement does not show that ordinary CoT gains generally arise through the enforced causal path.

**Evidence**

- S15 formalizes faithfulness as an instruction-to-reasoning-to-answer path and notes that conventional models can condition the answer on both the instruction and generated CoT, permitting an instruction-to-answer shortcut. [S15]
- S15 proposes training and attention-masking interventions that increase answer dependence on the reasoning chain and reports improved faithfulness while retaining competitive accuracy on four benchmarks. [S15]
- Earlier intervention studies found that changing or truncating a rationale sometimes changes answers and sometimes does not, demonstrating that visible-chain dependence is variable rather than guaranteed. [S10]

#### Finding 4

**Claim**

The new sources reinforce that CoT can be computationally useful without being a faithful explanation, and that formatting effects are a confound rather than the whole story.

**Confidence:** High

**Why this confidence level**

Multiple independent lines of evidence support both conclusions: formatting can distort measurement, but structured intermediate computation and causal dependence can also matter.

**Evidence**

- S14 treats latent-state mediation, surface traces, and serial compute as competing explanations and recommends compute-audited designs that factorize them. [S14]
- S9 identifies explicit terminal-answer placement as a major source of measured sensitivity in some corruption tests, while S10 reports that uninformative filler did not reproduce CoT gains in its setting. [S9] [S10]
- S15’s structural enforcement results show that changing the causal answer-generation path can improve faithfulness, suggesting that mere output formatting is insufficient for faithful reasoning. [S15]

### Conflicts Found

- S14 favors latent-state trajectories as the default object of reasoning, whereas S16–S18 describe CoT more straightforwardly as the computation itself or as a generally effective reasoning technique. The latter sources are explanatory or promotional summaries and do not perform the causal disentangling proposed by S14. [S14] [S16] [S17] [S18]
- S14 presents latent mediation as the strongest default hypothesis, while S13 reports gains from a process-aware CoT controller and S15 reports gains from structurally enforcing CoT dependence. These results show that explicit traces or trace-conditioned mechanisms can be useful, but they do not establish that surface text is the primary substrate of reasoning. [S13] [S14] [S15]
- S15 reports improved faithfulness from an architectural attention mask, while S10 and S14 treat ordinary CoT faithfulness as variable. This is a difference between a specially trained/enforced system and conventional prompting, not a direct contradiction. [S10] [S14] [S15]

### Important Gaps

- Do S14's compute-audited worked exemplars provide independently verifiable causal results, and how do they compare with matched-budget controls across model families?
- How much of classic few-shot CoT's benefit comes from demonstrations and task-specific exemplars versus latent computation induced by the prompt?
- Does CASE's faithfulness improvement generalize beyond its four benchmarks, and what accuracy or latency tradeoffs does structural enforcement impose?
- Can visible CoT be causally useful while still being incomplete or misleading, and do faithfulness metrics predict correctness?
- Are formatting and terminal-answer effects general outside explicit answer-line formats and the models studied by S9?
- Do latent-state findings generalize across mathematics, coding, planning, commonsense reasoning, retrieval, and multimodal tasks?

**Analysis Duration:** 14.28s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The accumulated evidence supports a responsible conditional answer, but the most important causal gap remains: a primary, independently replicated comparison that separately matches surface output format, generated-token budget/serial compute, demonstrations, and latent-state interventions. The new S14 paper is explicitly a position paper, and S15 is a recent preprint, so they do not fully close that gap.

**Next Search**

> primary empirical study chain-of-thought matched compute formatting control latent reasoning causal mediation few-shot CoT

---

# Iteration 5

## 1. Search

**Query**

> primary empirical study chain-of-thought matched compute formatting control latent reasoning causal mediation few-shot CoT

**Why this query**

The accumulated evidence supports a responsible conditional answer, but the most important causal gap remains: a primary, independently replicated comparison that separately matches surface output format, generated-token budget/serial compute, demonstrations, and latent-state interventions. The new S14 paper is explicitly a position paper, and S15 is a recent preprint, so they do not fully close that gap.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S19 — Few-Shot & Chain-of-Thought Prompting**
  URL: https://www.emergentmind.com/topics/few-shot-and-chain-of-thought-prompting
- **S20 — How Chain of Thought (CoT) Prompting Helps LLMs Reason More Like Humans | Splunk**
  URL: https://www.splunk.com/en_us/blog/learn/chain-of-thought-cot-prompting.html
- **S21 — Chain of Thought Prompting Guide**
  URL: https://www.prompthub.us/blog/chain-of-thought-prompting-guide
- **S22 — Language Models Perform Reasoning via Chain of Thought**
  URL: https://research.google/blog/language-models-perform-reasoning-via-chain-of-thought

**Search Duration:** 2.05s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The classic CoT literature provides strong evidence of benchmark improvement on sufficiently large, older language models, especially for multi-step arithmetic and some commonsense tasks, but it does not by itself establish that visible rationales are the causal mechanism.

**Confidence:** High

**Why this confidence level**

S22 is a direct account from the original research group and reports concrete comparative results, but it is a research blog summary and does not provide the causal controls needed to attribute gains specifically to visible reasoning text.

**Evidence**

- Google’s account of the original work reports that few-shot CoT substantially outperformed standard prompting on arithmetic tasks, with benefits emerging at roughly 100B-plus model scale; PaLM 540B reached 58% on GSM8K, compared with 17.7% for a standard-prompting baseline in the classic comparison. [S22]
- The same source reports additional, generally smaller gains on CommonsenseQA, StrategyQA, date understanding, and sports understanding. [S22]
- The source describes the intervention as providing demonstrations containing intermediate reasoning steps, whereas newer studies distinguish demonstrations, generic step-by-step instructions, extra tokens, and process-aware search as different interventions. [S22] [S1] [S8] [S10] [S11] [S13]

#### Finding 2

**Claim**

Few-shot CoT can simultaneously function as a reasoning scaffold and an output-format/alignment cue; the new sources reinforce that these effects should not be conflated.

**Confidence:** Medium

**Why this confidence level**

The distinction is supported by multiple sources, but S19’s newer mechanistic claims are summarized rather than presented as directly verifiable primary results, and the existing experiments do not fully factorize format, demonstrations, and computation.

**Evidence**

- S19 explicitly characterizes few-shot examples as serving both to induce multi-step reasoning and to align output format and style, and reports that some newer analyses find demonstrations mainly act as output-alignment cues for strong models. [S19]
- S1 finds that default model outputs may already be CoT-like and that conclusions change across direct, explicit-CoT, and default conditions, while S9 shows that explicit terminal-answer placement can dominate some sensitivity measurements. [S1] [S9]
- S10 reports that filler text did not reproduce CoT gains in its tested setting, arguing against the claim that CoT is only verbosity or formatting, although this does not eliminate format effects in other settings. [S10]

#### Finding 3

**Claim**

The main fault lines in the literature are model scale and training regime, task structure, the exact CoT intervention, evaluation metric, and the amount and type of test-time computation.

**Confidence:** High

**Why this confidence level**

These dimensions are directly reported across several sources and explain why apparently opposing findings can be simultaneously valid under different experimental conditions.

**Evidence**

- S22 reports that classic few-shot CoT benefits emerged primarily at very large scale, while S1 reports small, negative, or inconsistent effects for some modern reasoning-native models. [S22] [S1]
- S22 focuses on manually authored few-shot rationale demonstrations; S1 tests a generic step-by-step suffix and default prompting; S11 studies sequential budget forcing; and S13 studies branching, pruning, repair, verification, and abstention. [S22] [S1] [S11] [S13]
- S1 reports that average, majority-correct, and perfect-accuracy metrics can yield different judgments, including average gains alongside declines in strict consistency. [S1]
- S11 finds that uniform increases in reasoning budget can plateau or hurt, whereas S13 reports gains from selective process-aware allocation under matched budgets. [S11] [S13]

#### Finding 4

**Claim**

Visible CoT is not guaranteed to be a faithful transcript of the computation producing the answer, even when it improves accuracy.

**Confidence:** High

**Why this confidence level**

Intervention studies and specially enforced systems converge on the distinction between useful intermediate computation and faithful natural-language explanation.

**Evidence**

- S10 finds task-dependent effects of truncating, corrupting, or paraphrasing generated chains; larger models were sometimes less faithful, indicating that answer dependence on displayed CoT is variable. [S10]
- S19 and S21 acknowledge that ordinary reasoning chains can diverge from the final answer and contrast them with Faithful CoT systems that use symbolic translation and deterministic solving. [S19] [S21] [S8]
- S15 formalizes a possible direct instruction-to-answer shortcut and reports that architectural enforcement can increase answer dependence on the reasoning chain, implying that ordinary prompting does not guarantee such dependence. [S15]

#### Finding 5

**Claim**

The evidence does not support either extreme conclusion: CoT is neither merely formatting nor a universally reliable reasoning strategy.

**Confidence:** High

**Why this confidence level**

The conclusion is supported by convergent performance, intervention, formatting-ablation, and mechanistic evidence, while remaining appropriately conditional.

**Evidence**

- Classic results show substantial task-specific gains from few-shot rationale demonstrations on large models, while S1 documents weak or negative effects in some modern models and metrics. [S22] [S1]
- S10 finds that filler does not reproduce CoT gains in its setting, and S13 reports matched-budget gains from structured, selective computation, supporting a computational contribution beyond mere verbosity. [S10] [S13]
- S9 demonstrates that answer placement and formatting can create or distort apparent evidence of reasoning dependence, so some measured effects are readout or compliance effects rather than faithful mediation. [S9]
- S14’s decomposition into visible trace, latent state trajectory, and generic serial computation provides the most useful synthesis: ordinary CoT often changes all three at once. [S14]

### Conflicts Found

- S22 presents classic CoT as broadly improving reasoning at sufficient scale, whereas S1 reports diminishing, neutral, or negative returns for some newer reasoning-native models. This is primarily a difference in model generation, training regime, and prompt intervention rather than a direct contradiction. [S22] [S1]
- S19 and practitioner sources emphasize CoT’s usefulness and interpretability, but S10, S15, and S21 indicate that visible rationales can be non-faithful or bypassed. Claimed transparency therefore should not be equated with causal faithfulness. [S19] [S20] [S21] [S10] [S15]
- S19 suggests that few-shot exemplars may mainly align output format for some strong models, while S22 attributes classic gains to elicited intermediate reasoning. The sources concern different model generations and do not isolate demonstration content, format, and computation identically. [S19] [S22]

### Important Gaps

- How much of the original few-shot CoT gain survives controls for answer format, answer placement, demonstration count and quality, and equalized test-time compute?
- Do S19’s claims about demonstrations acting mainly as alignment cues generalize across tasks and model families, or are they specific to the cited newer analyses?
- Can accuracy gains be decomposed into latent computation, visible-rationale conditioning, answer-selection effects, and formatting/compliance effects?
- Do faithfulness interventions predict correctness, or can a model causally use an intermediate chain that is still wrong or misleading?

**Analysis Duration:** 16.21s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources strengthen the historical and conceptual synthesis but do not supply the missing primary, controlled comparison that directly separates few-shot demonstrations, generic rationale prompting, output formatting, and equalized computation. That gap is central to the original question.

**Next Search**

> primary study chain-of-thought matched compute formatting control few-shot rationale demonstrations causal ablation answer placement faithfulness

---

# Iteration 6

## 1. Search

**Query**

> primary study chain-of-thought matched compute formatting control few-shot rationale demonstrations causal ablation answer placement faithfulness

**Why this query**

The new sources strengthen the historical and conceptual synthesis but do not supply the missing primary, controlled comparison that directly separates few-shot demonstrations, generic rationale prompting, output formatting, and equalized computation. That gap is central to the original question.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S23 — Few-Shot CoT: Enhancing LLM Reasoning**
  URL: https://www.emergentmind.com/topics/few-shot-cot
- **S24 — Medium**
  URL: https://gregrobison.medium.com/chain-of-thought-in-large-language-models-elicited-reasoning-or-constrained-imitation-5e4ee0c811ad
- **S25 — Chain-of-Thought (CoT) Prompting**
  URL: https://www.promptingguide.ai/techniques/cot

**Search Duration:** 2.13s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources reinforce that few-shot CoT is a distinct intervention from generic zero-shot “think step by step” prompting: it supplies demonstrations containing intermediate rationales, final answers, and an expected response format.

**Confidence:** Medium

**Why this confidence level**

The sources agree on the intervention’s surface definition, but all three are explanatory or secondary sources and do not provide causal ablations.

**Evidence**

- S23 defines few-shot CoT as in-context demonstrations with explicit intermediate rationales and final answers, while S25 presents the original few-shot format and contrasts it with zero-shot CoT. [S23] [S25]
- S24 likewise distinguishes few-shot CoT, zero-shot CoT, and Auto-CoT, describing few-shot CoT as demonstrations of complete reasoning chains rather than merely a verbal instruction. [S24]

#### Finding 2

**Claim**

The examples in the new sources show that CoT can improve performance on simple arithmetic by inducing a correct decomposition, but they do not establish that the visible rationale itself causes the gain.

**Confidence:** Low

**Why this confidence level**

These are illustrative examples and an informal mechanistic explanation, not controlled experiments equalizing token budgets, answer format, demonstrations, or hidden computation.

**Evidence**

- S25 gives examples where adding “Let’s think step by step” changes an incorrect direct arithmetic answer into a correct stepwise answer, and where rationale demonstrations improve parity-classification accuracy. [S25]
- S24 describes CoT as allocating additional generated tokens and reconditioning later predictions on prior intermediate text, offering a computational account of the observed improvement. [S24]

#### Finding 3

**Claim**

Few-shot demonstrations plausibly combine at least three effects—task exemplars, reasoning decomposition, and output-format alignment—so their gains cannot be attributed to reasoning from these sources alone.

**Confidence:** Medium

**Why this confidence level**

The sources directly describe these functions of demonstrations, but they do not experimentally factorize them.

**Evidence**

- S23 describes demonstrations as providing procedural templates, structured decomposition, and a canonical task-context/rationale/answer format. [S23]
- S24 says high-quality demonstrations guide both the reasoning pattern and the expected format and style, while S25’s prompt examples visibly specify answer placement and rationale wording. [S24] [S25]

#### Finding 4

**Claim**

The new evidence does not materially weaken the accumulated conclusion that CoT is neither merely formatting nor a universally reliable reasoning strategy.

**Confidence:** High

**Why this confidence level**

The new material is consistent with, but does not substantially extend or contradict, the stronger empirical and intervention-based findings already accumulated.

**Evidence**

- The prior intervention evidence found that filler did not reproduce CoT gains, while formatting and terminal-answer placement can distort faithfulness measurements; the new sources add only standard claims and demonstrations rather than contrary causal evidence. [S9] [S10] [S23] [S24] [S25]
- The new sources present broad effectiveness claims, but do not address the accumulated model-, metric-, compute-, and faithfulness-dependent negative or mixed results. [S1] [S10] [S11] [S14] [S23] [S24] [S25]

### Conflicts Found

- S23–S25 describe few-shot or zero-shot CoT as broadly effective and improving interpretability, whereas S10, S14, and S15 show that accuracy improvement and visible explanations do not guarantee causal faithfulness. This is primarily a difference between performance-oriented summaries and faithfulness-focused empirical analyses. [S10] [S14] [S15] [S23] [S24] [S25]
- S24 attributes CoT gains to additional generated-token computation and sequential recontextualization, while S9 shows that some measured effects can arise from answer placement or formatting. The sources do not test the same controls, so the mechanistic account remains underdetermined. [S9] [S24]
- S23 claims substantial cross-domain gains, including code and multimodal tasks, but the accumulated evidence emphasizes strong task- and model-dependence. S23 does not provide enough primary-study detail to establish that its broad generalization claims survive matched-compute and formatting controls. [S1] [S13] [S23]

### Important Gaps

- How much of few-shot CoT’s benefit comes from rationale content and decomposition versus demonstrations’ task format, answer placement, and example-induced alignment?
- Do the broad cross-domain claims summarized by S23 generalize under matched token/FLOP budgets and independent answer extraction?
- Do classic few-shot CoT gains survive controls that separately equalize demonstration count, rationale length, output format, terminal-answer placement, and test-time computation?

**Analysis Duration:** 14.74s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources are mostly secondary explainers and illustrative prompt demonstrations. They clarify terminology but do not fill the central causal gap: whether classic few-shot CoT gains remain after independently controlling for rationale content, formatting, demonstrations, and extra computation. A primary controlled study would materially improve the answer.

**Next Search**

> primary study few-shot chain-of-thought rationale content output format matched token budget control demonstrations causal ablation

---

# Iteration 7

## 1. Search

**Query**

> primary study few-shot chain-of-thought rationale content output format matched token budget control demonstrations causal ablation

**Why this query**

The new sources are mostly secondary explainers and illustrative prompt demonstrations. They clarify terminology but do not fill the central causal gap: whether classic few-shot CoT gains remain after independently controlling for rationale content, formatting, demonstrations, and extra computation. A primary controlled study would materially improve the answer.

**Results**

5 results retrieved.

2 new unique sources added.

### Sources

- **S26 — Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot**
  URL: https://arxiv.org/html/2506.14641v3
- **S27 — Chain of Thought Prompting Guide - Medium**
  URL: https://medium.com/@dan_43009/chain-of-thought-prompting-guide-3fdfd1972e03

**Search Duration:** 1.89s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new primary study strengthens the claim that few-shot CoT is not universally an added reasoning intervention for current strong mathematical-reasoning models; in its tested setting, zero-shot CoT matched or exceeded few-shot CoT.

**Confidence:** Medium

**Why this confidence level**

S26 is a direct empirical preprint with systematic experiments, but the retrieved content does not provide full tables, controls, or independent replication, and coverage is limited mainly to recent open-source models and mathematics.

**Evidence**

- S26 reports systematic GSM8K and MATH experiments with recent Qwen2.5 models and finds that traditional CoT exemplars do not improve reasoning performance over zero-shot CoT; enhanced exemplars generated by Qwen2.5-Max and DeepSeek-R1 also fail to improve performance. [S26]

#### Finding 2

**Claim**

For the recent strong models studied in S26, few-shot CoT exemplars appear to function primarily as output-format and response-alignment cues rather than as a source of additional reasoning capability.

**Confidence:** Medium

**Why this confidence level**

This is the study's direct interpretation and is consistent with the observed zero-shot/few-shot comparison, but exemplar content, format, and computation are not fully factorized in the retrieved material.

**Evidence**

- S26 explicitly concludes that the primary function of CoT exemplars is aligning output format with human expectations, while models tend to focus on the instruction and ignore exemplar content. [S26]
- S26 distinguishes few-shot CoT demonstrations from zero-shot CoT, where only a reasoning instruction is supplied, and reports no reasoning gain from adding the demonstrations. [S26]

#### Finding 3

**Claim**

S26 provides a concrete explanation for part of the classic-versus-modern disagreement: strong newer models may already possess the relevant mathematical reasoning capability under zero-shot CoT, leaving demonstrations mainly to standardize presentation.

**Confidence:** Medium

**Why this confidence level**

The cross-source synthesis is plausible and directly supported by the reported model/task contrasts, but the studies do not use identical prompts, models, or evaluation protocols.

**Evidence**

- S26 argues that recent strong models exhibit strong reasoning in the zero-shot CoT condition and that traditional or enhanced exemplars do not transfer additional reasoning ability. [S26]
- This complements S22's classic result that few-shot CoT produced large gains on earlier large models and S1's finding that CoT effects vary by model generation and training regime. [S22] [S1]

#### Finding 4

**Claim**

The new evidence sharpens, but does not eliminate, the distinction between few-shot CoT and generic zero-shot step-by-step prompting.

**Confidence:** High

**Why this confidence level**

The intervention distinction is explicit in S26 and consistent with multiple accumulated sources.

**Evidence**

- S26 defines few-shot CoT as adding rationale-bearing demonstrations and compares it with zero-shot CoT; the absence of an incremental gain indicates that the demonstration component may be dispensable for strong models. [S26]
- Prior evidence treats few-shot demonstrations, generic step-by-step instructions, extra token generation, and process-aware search as distinct interventions rather than one homogeneous CoT treatment. [S1] [S8] [S10] [S11] [S13]

#### Finding 5

**Claim**

S26 does not show that CoT is merely formatting in general; it shows that the incremental value of few-shot rationale exemplars can be mostly formatting-related in a restricted modern-math regime.

**Confidence:** High

**Why this confidence level**

The scope limitation is explicit from S26's described datasets and models, and the broader accumulated evidence directly argues against a universal formatting-only conclusion.

**Evidence**

- S26 concerns GSM8K and MATH, recent Qwen2.5-series models, and exemplar addition to zero-shot CoT. It does not test all zero-shot prompts, older models, non-mathematical tasks, or matched hidden-compute interventions. [S26]
- S10 reports that uninformative filler did not reproduce CoT gains in its setting, while S13 reports matched-budget gains from structured selective computation, supporting computational contributions beyond mere verbosity or formatting. [S10] [S13]

### Conflicts Found

- S26 finds no reasoning benefit from traditional or enhanced few-shot CoT over zero-shot CoT for recent Qwen2.5 models on GSM8K and MATH, whereas S22 reports substantial classic few-shot CoT gains. The likely fault line is model generation/training regime and baseline capability, compounded by different experimental setups. [S26] [S22]
- S26 characterizes CoT exemplars as primarily output-format alignment for its tested strong models, while S10 finds that filler text does not reproduce CoT gains and S13 finds gains from structured, selective intermediate computation under reported matched budgets. These are not direct contradictions: exemplar formatting, free-form CoT generation, and process-aware search are different interventions. [S26] [S10] [S13]
- S27 claims few-shot CoT generally outperforms zero-shot CoT and can raise accuracy substantially, but it is a practitioner guide and its cited table is not independently detailed in the retrieved content. This broad claim conflicts with S26 only at the level of generality; S26 supplies a narrower primary result for recent mathematical models. [S27] [S26]

### Important Gaps

- Does S26's format-alignment result replicate across model families beyond Qwen2.5 and across coding, planning, commonsense, symbolic, and multimodal tasks?
- Were zero-shot and few-shot conditions equalized for total generated tokens, hidden reasoning compute, exemplar length, answer placement, and decoding strategy in S26?
- Does S26's claim that models ignore exemplar content hold when demonstrations are task-matched, harder than the target problems, contrastive, or designed to teach a novel procedure?
- How much of classic few-shot CoT's benefit survives controls that independently equalize demonstration content, output format, answer placement, and test-time computation?
- Does the evaluation-bias correction described by S26 account for some prior apparent few-shot advantage, and does it generalize beyond GSM8K's open-source evaluation frameworks?
- Can a model ignore the literal exemplar content while still benefiting from its latent distributional or formatting effects?

**Analysis Duration:** 15.73s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new source materially strengthens one side of the central fault line—few-shot exemplars may be formatting/alignment for strong modern math models—but it does not resolve generalization, compute controls, or the causal role of zero-shot CoT itself. A focused search for the full primary study or independent replication with matched format and compute would materially improve the answer.

**Next Search**

> "Revisiting Chain-of-Thought Prompting" zero-shot stronger few-shot Qwen2.5 GSM8K MATH independent replication matched format compute

---

# Iteration 8

## 1. Search

**Query**

> "Revisiting Chain-of-Thought Prompting" zero-shot stronger few-shot Qwen2.5 GSM8K MATH independent replication matched format compute

**Why this query**

The new source materially strengthens one side of the central fault line—few-shot exemplars may be formatting/alignment for strong modern math models—but it does not resolve generalization, compute controls, or the causal role of zero-shot CoT itself. A focused search for the full primary study or independent replication with matched format and compute would materially improve the answer.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S28 — Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot**
  URL: https://arxiv.org/html/2506.14641
- **S29 — Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot**
  URL: https://arxiv.org/html/2506.14641v1
- **S30 — [PDF] Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger ...**
  URL: https://aclanthology.org/2025.findings-emnlp.729.pdf
- **S31 — [PDF] Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger ...**
  URL: https://openreview.net/pdf/4401d48b1ca2a45307cd7e3d2b2e5b079270c496.pdf

**Search Duration:** 4.03s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

A peer-reviewed EMNLP 2025 study strengthens the evidence that few-shot CoT is not universally beneficial for strong contemporary mathematical models.

**Confidence:** High

**Why this confidence level**

S30 is a published Findings of EMNLP paper and reports systematic experiments on two established mathematical benchmarks, although its model and task coverage remains limited.

**Evidence**

- Across GSM8K and MATH experiments with recent Qwen2.5 models, the study reports that traditional CoT exemplars do not improve reasoning performance relative to zero-shot CoT; enhanced exemplars built from Qwen2.5-Max and DeepSeek-R1 also fail to produce gains. [S30]

#### Finding 2

**Claim**

For the tested recent Qwen2.5 models, the incremental effect of few-shot CoT appears predominantly to be output-format alignment rather than added reasoning capability.

**Confidence:** Medium

**Why this confidence level**

The format-alignment interpretation is the authors’ explanation of their comparisons, but the retrieved material does not fully factorize exemplar content, answer placement, formatting, and hidden computation.

**Evidence**

- The study concludes that zero-shot CoT already elicits strong reasoning, while few-shot exemplars mainly align responses with expected human-readable formats; its analyses indicate that models focus on the instruction and tend to ignore exemplar content. [S30]
- The reported figure shows zero-shot prompting consistently achieving strong performance across the tested GSM8K and MATH settings, despite the addition of rationale-bearing exemplars in other conditions. [S30]

#### Finding 3

**Claim**

An evaluation artifact can make zero-shot CoT appear weaker than it is, thereby producing an artificial advantage for few-shot CoT.

**Confidence:** Medium

**Why this confidence level**

The paper directly reports this artifact, but the retrieved content does not describe its exact implementation or establish how broadly it affects other datasets and evaluators.

**Evidence**

- S30 identifies a bias in commonly used open-source GSM8K evaluation frameworks that significantly underestimates zero-shot CoT performance; correcting the issue is part of the study’s comparison of zero-shot and few-shot prompting. [S30]

#### Finding 4

**Claim**

The new evidence supports a model-generation and capability explanation for conflicting CoT results: demonstrations that helped earlier or weaker models may become redundant when stronger models can already reason under zero-shot CoT.

**Confidence:** High

**Why this confidence level**

The contrast is consistent across the new and prior sources, though the studies use different models, prompts, and evaluation protocols.

**Evidence**

- S30 reports that traditional and enhanced exemplars fail to improve recent Qwen2.5 models, which already perform strongly with zero-shot CoT. [S30]
- This contrasts with the classic large-scale results reported for earlier models and with accumulated evidence that CoT effects vary by model generation, training regime, and baseline capability. [S22] [S1]

#### Finding 5

**Claim**

S30 does not support the universal conclusion that CoT is merely formatting.

**Confidence:** High

**Why this confidence level**

The scope limitation is explicit, and independent accumulated evidence indicates that structured computation can contribute beyond presentation effects.

**Evidence**

- The study tests the incremental value of few-shot rationale exemplars over zero-shot CoT on GSM8K and MATH; it does not test all forms of CoT, non-mathematical tasks, older models, or matched-compute alternatives. [S30]
- Other intervention evidence finds that uninformative filler does not reproduce CoT gains in some settings and that structured, selective intermediate computation can improve performance under reported matched budgets. [S10] [S13]

### Conflicts Found

- S30’s published findings that few-shot CoT adds no reasoning benefit for recent Qwen2.5 models contrast with classic reports of substantial few-shot CoT gains. The discrepancy is best explained conditionally by model generation, baseline zero-shot ability, task regime, evaluation practices, and the exact intervention—not by a universal contradiction. [S30] [S22]
- S30 attributes the remaining value of exemplars mainly to format alignment, while S10 and S13 provide evidence that some CoT-like interventions involve computational benefits beyond formatting. These studies manipulate different interventions and therefore do not establish the same mechanism. [S30] [S10] [S13]
- S30 reports that models tend to ignore exemplar content, but this does not show that demonstrations never provide procedural information: the result is limited to the tested recent models and mathematical tasks, and task-matched or novel-procedure demonstrations could behave differently. [S30]

### Important Gaps

- Whether S30’s format-alignment result generalizes beyond Qwen2.5 models and GSM8K/MATH to coding, planning, commonsense, symbolic, retrieval, and multimodal tasks.
- Whether zero-shot and few-shot conditions in S30 were fully equalized for total generated tokens, hidden reasoning compute, exemplar length, answer placement, and decoding strategy.
- How much classic few-shot CoT benefit survives controls that separately equalize demonstration content, output format, terminal-answer placement, and test-time computation.
- Whether models can ignore the literal content of exemplars while still benefiting from their latent distributional, task-format, or answer-selection effects.
- Whether evaluation-bias corrections like the GSM8K issue identified in S30 explain some earlier reports of few-shot superiority more broadly.

**Analysis Duration:** 13.21s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The new published study materially strengthens the model-generation, evaluation, and format-alignment parts of the synthesis. The accumulated evidence already supports a responsible answer: CoT is neither universally effective reasoning nor merely formatting. Further research would clarify causal mechanisms and generalization, but another search is unlikely to change that central conclusion given the existing intervention, faithfulness, matched-budget, and benchmark evidence.

**Stop Reason:** sufficient_evidence

---

# Final Research Decision

**Research Stopped Because**

The analyzer determined that the important parts of the question could be answered responsibly.

**Stop Reason:** sufficient_evidence

**Searches Performed:** 8

**Unique Sources:** 31

**Remaining Uncertainty**

- Whether classic few-shot CoT gains survive a fully controlled comparison equalizing rationale length, answer format, terminal-answer placement, demonstrations, decoding, and total test-time computation.
- How much zero-shot CoT itself contributes through latent-state changes, visible intermediate text, generic serial computation, or answer-selection effects.
- Whether the EMNLP 2025 format-alignment result generalizes beyond Qwen2.5, GSM8K, and MATH to coding, planning, commonsense, symbolic, retrieval, and multimodal tasks.
- Whether models can ignore the literal content of exemplars while still benefiting from their latent distributional or formatting effects.
- Whether visible CoT can be causally useful while remaining incomplete or misleading, and whether existing faithfulness measures predict correctness or safety.
- Whether formatting and terminal-answer effects generalize beyond explicit answer-line formats and across larger or proprietary reasoning models.
- Whether the reported matched-budget comparisons equalize all relevant costs, including model computation, controller calls, evaluator calls, generated tokens, and memory use.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 8 | 20.52s |
| OpenAI Analysis | 8 | 125.04s |
| Report Generation | 1 | 22.25s |
| Total Run | — | 167.82s |
