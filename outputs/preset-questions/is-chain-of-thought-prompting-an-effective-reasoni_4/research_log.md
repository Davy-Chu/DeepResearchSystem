# Research Run Log

## Run Summary

**System Version:** evidence-ledger-decomposer-verifier-v1

**Research Question**

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 15

**OpenAI Calls:** 9

**Tavily Calls:** 3

**Verifier Model:** gpt-5.6-luna

**Started:** 2026-08-31T19:01:35-04:00

**Ended:** 2026-08-31T19:03:23-04:00

**Total Runtime:** 107.74s

---

# Research Plan

## Subquestions

### SQ1 [CORE]

**Question:**

What effects does chain-of-thought (CoT) prompting have on LLM task performance, and under what task, model, prompt, and evaluation conditions are improvements observed?

**Success criteria:**

Characterize the empirical evidence for and against CoT-based performance gains across relevant studies, preserving differences in tasks, model capabilities, prompting methods, baselines, and evaluation metrics rather than treating CoT as a single intervention.

**Initial status:** UNRESEARCHED

### SQ2 [CORE]

**Question:**

Do reported CoT gains reflect improved underlying reasoning, improved answer presentation or output formatting, or a mixture of both?

**Success criteria:**

Distinguish reasoning-process effects from formatting, answer-verification, compliance, and scoring effects using evidence such as process-sensitive evaluations, answer-only versus rationale-based scoring, robustness or transfer tests, and analyses of whether rationales are causally useful or merely correlated with correct answers.

**Initial status:** UNRESEARCHED

### SQ3 [CORE]

**Question:**

What methodological and conceptual fault lines explain conflicting findings in the CoT literature?

**Success criteria:**

Identify and compare disagreements involving definitions of reasoning and CoT, model scale and capability, task composition and difficulty, prompt wording and demonstrations, decoding and sampling, benchmark contamination or saturation, evaluator and metric design, rationale faithfulness, and statistical or replication practices.

**Initial status:** UNRESEARCHED

### SQ4 [SECONDARY]

**Question:**

How do alternative prompting and reasoning interventions compare with standard CoT, and what do those comparisons reveal about the source of observed gains?

**Success criteria:**

Use relevant comparisons—including direct answering, answer-format controls, scratchpads or hidden reasoning, self-consistency, decomposition, tool use, and rationale manipulation where available—to determine whether gains are specific to explicit natural-language reasoning or arise from broader changes in computation, search, or response constraints.

**Initial status:** UNRESEARCHED

### SQ5 [CORE]

**Question:**

What conclusions can responsibly be drawn about when CoT should be considered an effective reasoning strategy, and what uncertainty remains?

**Success criteria:**

Synthesize the literature into conditional conclusions rather than a binary verdict, specifying the settings in which CoT appears beneficial, neutral, or misleading, the strength and limits of the evidence, and unresolved questions or risks of overinterpreting benchmark results.

**Initial status:** UNRESEARCHED

## Synthesis Requirements

- Reconcile apparently conflicting results by comparing study designs and boundary conditions, not by averaging incompatible findings.
- Preserve the causal distinction between improving internal or effective reasoning and improving the format, inspectability, or scoring of outputs.
- Separate evidence about whether CoT improves final-task accuracy from evidence about whether generated rationales faithfully represent the computations producing that accuracy.
- Track relevant differences in model family, scale, task domain, prompt construction, decoding, evaluator, and timeframe across the literature.
- Represent uncertainty and distinguish established patterns from speculative explanations.

## Output Requirements

- Explain the real fault lines in the literature and what accounts for conflicting results.
- Answer the question as a nuanced comparison between CoT as a reasoning strategy and CoT as an output-formatting or evaluation aid.
- Present conclusions conditionally, with explicit attention to limitations and uncertainty.

---

# Iteration 1

## 1. Search

**Query**

> Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

**Purpose:** GENERAL

**Why this query**

This is the user's original research question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S1 — Hierarchical Chain-of-Thought Prompting: Enhancing LLM ...**
  URL: https://arxiv.org/html/2604.00130v1
- **S2 — What is chain of thought (CoT) prompting? - IBM**
  URL: https://www.ibm.com/think/topics/chain-of-thoughts
- **S3 — Chain of Thought Prompting (CoT): Everything you need to know**
  URL: https://www.vellum.ai/blog/chain-of-thought-prompting-cot-everything-you-need-to-know
- **S4 — Prompt Engineering: Chain of Thought & LLM Performance | Medium**
  URL: https://medium.com/data-science-collective/so-you-think-you-can-prompt-b3384664bafc
- **S5 — Contrastive Chain-Of-Thought Prompting**
  URL: https://www.kore.ai/blog/contrastive-chain-of-thought-prompting

**Search Duration:** 3.19s

---

## 2. Evidence Processing

- New claim proposals: 4
- Existing claim updates: 0
- New gaps: 4
- Resolved gaps: 0

**Processing Duration:** 15.34s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

The supplied sources describe CoT as improving final-answer performance most plausibly on multi-step arithmetic, mathematical, symbolic, and some commonsense tasks, but the magnitude of benefit is conditional on model capability, task difficulty, and prompt construction rather than being uniform across all tasks.

- S1 supports (direct): Reports prior CoT improvements on mathematical, arithmetic, commonsense, and symbolic reasoning tasks, while presenting Hi-CoT evaluations on five mathematical benchmarks and 13 model configurations.
- S2 supports (indirect): Characterizes CoT as particularly useful for complex multistep tasks and states that larger models and instruction-tuned models tend to perform better with CoT.
- S3 supports (indirect): States that CoT is useful for complex arithmetic, commonsense, and symbolic reasoning, and reports that it works especially well with larger models while smaller models may produce imprecise thought chains.
- S4 supports (indirect): Summarizes reported gains over standard few-shot prompting across arithmetic, commonsense, and symbolic reasoning, with gains varying by task and model scale.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C2

**Claim**

CoT performance depends materially on prompt format and exemplar construction: few-shot rationales, zero-shot instructions, exemplar number and ordering, and structured alternatives can produce different outcomes, so “CoT” is not a single experimentally invariant intervention.

- S1 supports (direct): Distinguishes conventional CoT, zero-shot CoT, Auto-CoT, Plan-and-Solve, and Hi-CoT, and reports that hierarchical structure and strict adherence affect accuracy and trace length.
- S3 supports (direct): Describes few-shot and zero-shot CoT as distinct variants and presents automated demonstration selection as another intervention.
- S4 supports (direct): Reports robustness analyses involving different rationale annotations, exemplar orders, and numbers of exemplars, while comparing CoT with standard few-shot prompting.
- S2 supports (indirect): Explains that CoT may be elicited through step-by-step instructions or exemplars and distinguishes it from prompt chaining.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C3

**Claim**

The supplied sources provide competing interpretations of CoT gains: some present intermediate steps as helping decomposition, attention, coherence, and error reduction, while S1 reports a cited view that modern LLM CoT exemplars may primarily enforce output format rather than improve reasoning quality.

- S1 supports (direct): Attributes CoT benefits to intermediate steps and reports Hi-CoT’s planning and execution structure as improving coherence and efficiency; it also states that Cheng et al. (2025) argues modern-LLM CoT exemplars primarily enforce output format.
- S2 supports (indirect): Characterizes CoT as guiding stepwise problem solving and notes observability and debugging benefits from surfacing intermediate steps.
- S3 supports (indirect): Describes CoT as breaking problems into manageable steps but separately notes that users may want reasoning to occur while only the final answer is displayed, distinguishing reasoning from presentation.

**Confidence:** MEDIUM

**Status:** CONFLICTING

### New Claim C4

**Claim**

Structured reasoning prompts can improve both accuracy and inference efficiency relative to flat CoT in at least the reported mathematical evaluations: S1 reports that Hi-CoT increased average accuracy by 6.2% and reduced reasoning-trace length by 13.9% across 13 model configurations and five benchmarks, although these results concern a specific proposed variant and evaluation setting.

- S1 supports (direct): Directly reports the average accuracy increase, trace-length reduction, model families, number of configurations, and mathematical benchmarks for Hi-CoT relative to CoT.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Gap G1

The supplied evidence does not directly establish whether CoT-generated rationales are causally used in producing correct answers, faithfully report the underlying computation, or mainly improve answer formatting, inspectability, compliance, or evaluator scoring.

### New Gap G2

There is insufficient controlled, primary evidence in the supplied sources to reconcile apparent differences across model families, parameter scales, task difficulty, prompt wording, decoding or sampling procedures, and evaluation metrics.

### New Gap G3

The reported Hi-CoT gains are not independently validated by the supplied sources, and the evidence does not establish how well they generalize beyond the stated mathematical benchmarks or distinguish structural reasoning benefits from changes in output constraints and token allocation.

### New Gap G4

The sources do not provide sufficient evidence about benchmark contamination, saturation, replication quality, statistical uncertainty, or evaluator sensitivity as explanations for conflicting CoT findings.

---

## 4. Current Research State

- Claims: 4
- Supported: 3
- Weak: 0
- Conflicting: 1
- Insufficient Evidence: 0
- Open Gaps: 4
- Remaining Searches: 2

### Subquestion Progress

**SQ1:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** UNRESEARCHED → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ3:** UNRESEARCHED → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ4:** UNRESEARCHED → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ5:** UNRESEARCHED → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → CONFLICTING (targeted searches: 0)
- SQ3 → CONFLICTING (targeted searches: 0)
- SQ5 → CONFLICTING (targeted searches: 0)

**SECONDARY:**

- SQ4 → CONFLICTING (targeted searches: 0)

**Remaining targeted searches:** 2

---

## 5. Independent Verification

### V1 — Claim C2

**Phase:** INITIAL

**Evidence source IDs:** S1, S3, S4, S2

**Verdict:** NEEDS_QUALIFICATION

**Reason**

The evidence supports treating CoT as a family of prompt interventions rather than a single invariant treatment: it distinguishes few-shot, zero-shot, automated, and structured/hierarchical variants, and reports that prompt quality can substantially affect outcomes. However, the supplied sources do not systematically establish the independent effects of exemplar number and ordering, and one secondary source reports robustness to those factors rather than differences. The claim should therefore be narrowed and conditioned on task, model, and evaluation setup.

**Missing assumptions**

- That the observed differences are attributable to prompt format or exemplar construction rather than model, task, decoding, or evaluation differences.
- That claims about exemplar number and ordering generalize beyond the particular tasks and models studied.
- That the cited performance differences were measured against comparable direct-answering and formatting-control baselines.

**Source concerns**

- Several sources are practitioner or secondary explainers rather than primary empirical studies.
- S1 is a recent arXiv preprint and reports results for a particular hierarchical method, model set, and mathematical benchmarks.
- The supplied excerpts provide limited methodological detail, uncertainty estimates, and direct comparisons isolating each prompt component.

**Counter-search status:** EXECUTED

**Counter-search query:**

> Find primary studies and replications testing CoT sensitivity to zero-shot versus few-shot rationales, exemplar number and ordering, rationale wording, and structured prompt formats, including negative or null results and formatting-control baselines.

**Counter-search evidence:** S6, S7, S8, S9, S10

---

## 6. Research Decision

**Decision:** Continue researching.

**Origin:** VERIFIER_COUNTERSEARCH

**Target:** CLAIM C2

**Why**

Independent verification of C2 identified a high-value falsification search: The evidence supports treating CoT as a family of prompt interventions rather than a single invariant treatment: it distinguishes few-shot, zero-shot, automated, and structured/hierarchical variants, and reports that prompt quality can substantially affect outcomes. However, the supplied sources do not systematically establish the independent effects of exemplar number and ordering, and one secondary source reports robustness to those factors rather than differences. The claim should therefore be narrowed and conditioned on task, model, and evaluation setup.

**Next Search**

> Find primary studies and replications testing CoT sensitivity to zero-shot versus few-shot rationales, exemplar number and ordering, rationale wording, and structured prompt formats, including negative or null results and formatting-control baselines.


---

# Iteration 2

## 1. Search

**Query**

> Find primary studies and replications testing CoT sensitivity to zero-shot versus few-shot rationales, exemplar number and ordering, rationale wording, and structured prompt formats, including negative or null results and formatting-control baselines.

**Target:** C2

**Purpose:** COUNTERSEARCH

**Why this query**

Independent verification of C2 identified a high-value falsification search: The evidence supports treating CoT as a family of prompt interventions rather than a single invariant treatment: it distinguishes few-shot, zero-shot, automated, and structured/hierarchical variants, and reports that prompt quality can substantially affect outcomes. However, the supplied sources do not systematically establish the independent effects of exemplar number and ordering, and one secondary source reports robustness to those factors rather than differences. The claim should therefore be narrowed and conditioned on task, model, and evaluation setup.

5 result(s) retrieved; 5 new unique source(s) added.

- **S6 — Few-Shot CoT: Enhancing LLM Reasoning**
  URL: https://www.emergentmind.com/topics/few-shot-cot
- **S7 — Revisiting Chain-of-Thought Prompting: Zero-shot Can ... - arXiv**
  URL: https://arxiv.org/html/2506.14641v3
- **S8 — Master Prompting Concepts: Zero-Shot and Few-Shot Prompting**
  URL: https://promptengineering.org/master-prompting-concepts-zero-shot-and-few-shot-prompting
- **S9 — Shot-Based Prompting: Zero-Shot, One-Shot, and Few-Shot Prompting**
  URL: https://learnprompting.org/docs/basics/few_shot
- **S10 — Zero-Shot vs Few-Shot vs Chain-of-Thought Prompting: Complete Guide 2026 | explainx.ai Blog | explainx.ai**
  URL: https://explainx.ai/blog/zero-shot-few-shot-chain-of-thought-prompting-guide-2026

**Search Duration:** 2.99s

---

## 2. Evidence Processing

- New claim proposals: 2
- Existing claim updates: 3
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 12.07s

---

## 3. Ledger Updates

### New Claim C5

**Claim**

In recent strong models evaluated on GSM8K and MATH, traditional few-shot CoT exemplars may fail to improve reasoning performance over zero-shot CoT; their primary observed contribution in the supplied study was aligning output format with human expectations, and enhanced exemplars were likewise reported not to improve reasoning because models tended to rely on the instruction rather than exemplar content.

- S7 supports (direct): Systematic experiments with recent Qwen2.5-series models on GSM8K and MATH report no reasoning-performance improvement from traditional or enhanced few-shot CoT over zero-shot CoT, while identifying output-format alignment as the primary function of exemplars.
- S6 contradicts (indirect): A broad secondary synthesis presents few-shot CoT as improving accuracy and supporting procedural generalization across complex tasks and domains, though it does not provide comparable controlled evidence for the specific strong-model mathematical setting.

**Confidence:** MEDIUM

**Status:** CONFLICTING

### New Claim C6

**Claim**

Evaluation implementation can materially affect apparent comparisons between zero-shot CoT and few-shot CoT: S7 reports that an open-source GSM8K evaluation bias significantly underestimated zero-shot CoT performance, so correcting the evaluator changed the apparent relative benefit of exemplars.

- S7 supports (direct): Reports identifying and correcting a common open-source GSM8K evaluation bias that significantly underestimated zero-shot CoT, after which recent strong models showed strong zero-shot reasoning and no observed reasoning gain from few-shot exemplars.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

The supplied sources describe CoT as improving final-answer performance most plausibly on multi-step arithmetic, mathematical, symbolic, and some commonsense tasks, but the magnitude of benefit is conditional on model capability, task difficulty, and prompt construction rather than being uniform across all tasks.

- S7 supports (direct): Finds that traditional few-shot CoT does not improve reasoning performance over zero-shot CoT in recent strong models on GSM8K and MATH, while noting that weaker models may benefit; this sharpens the claim's model-capability boundary.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

CoT performance can depend materially on how the intervention is instantiated—especially zero-shot versus few-shot rationales, exemplar construction, and the use of structured alternatives—with effects varying by model, task, and evaluation setup. Thus, “CoT” should not be treated as a single experimentally invariant intervention; evidence that exemplar number and ordering systematically matter is mixed.

- S7 supports (direct): Directly compares zero-shot CoT with traditional and enhanced few-shot CoT, showing that exemplar content, exemplar enhancement, and the instruction-only baseline can yield different outcomes; in the reported strong-model setting, exemplars mainly aligned output format.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C3

**Claim**

The supplied sources provide competing interpretations of CoT gains: some present intermediate steps as helping decomposition, attention, coherence, and error reduction, while S1 reports a cited view that modern LLM CoT exemplars may primarily enforce output format rather than improve reasoning quality.

- S7 supports (direct): In recent strong models on mathematical reasoning tasks, reports that few-shot CoT exemplars primarily align output format, do not improve reasoning over zero-shot CoT, and are often ignored in favor of the instruction.
- S6 contradicts (indirect): Presents few-shot CoT as improving accuracy, interpretability, and procedural generalization across complex tasks and domains, although this is a broad secondary account rather than a process-sensitive causal test.

**Confidence:** MEDIUM → HIGH

**Status:** CONFLICTING → CONFLICTING

---

## 4. Current Research State

- Claims: 6
- Supported: 3
- Weak: 1
- Conflicting: 2
- Insufficient Evidence: 0
- Open Gaps: 4
- Remaining Searches: 1

### Subquestion Progress

**SQ1:** PARTIAL → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ2:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ3:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ4:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ5:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

### Research Plan Status

**CORE:**

- SQ1 → CONFLICTING (targeted searches: 0)
- SQ2 → CONFLICTING (targeted searches: 0)
- SQ3 → CONFLICTING (targeted searches: 0)
- SQ5 → CONFLICTING (targeted searches: 0)

**SECONDARY:**

- SQ4 → CONFLICTING (targeted searches: 0)

**Remaining targeted searches:** 1

---

## 5. Independent Verification

### V2 — Claim C2

**Phase:** POST_COUNTERSEARCH

**Evidence source IDs:** S1, S3, S4, S2, S7

**Verdict:** NEEDS_QUALIFICATION

**Reason**

The supplied evidence supports that CoT is not experimentally invariant: zero-shot versus few-shot rationales can differ, and recent models may gain no reasoning benefit from traditional exemplars even when output format changes. The evidence also describes structured variants such as hierarchical, tree-, and graph-based reasoning, but does not establish their effects broadly. One cited summary reports robustness to exemplar order and number, so those factors should be presented as potentially task- and model-dependent rather than uniformly outcome-determining.

**Missing assumptions**

- The findings generalize beyond the mainly mathematical tasks and recent open-source models discussed in the evidence.
- Differences attributed to exemplar number and ordering are measured against matched baselines and are not artifacts of particular datasets, decoding settings, or evaluation procedures.
- Structured alternatives have been directly compared with standard CoT under comparable experimental conditions.

**Source concerns**

- The strongest direct evidence is a recent arXiv preprint rather than an established peer-reviewed synthesis.
- Several other sources are practitioner or explanatory articles and provide limited methodological detail.
- The supplied evidence contains conflicting summaries regarding robustness to exemplar order and number.

**Counter-search status:** NOT_REQUESTED

**Reconciliation**

Claim:

"CoT performance depends materially on prompt format and exemplar construction: few-shot rationales, zero-shot instructions, exemplar number and ordering, and structured alternatives can produce different outcomes, so “CoT” is not a single experimentally invariant intervention."
→
"CoT performance can depend materially on how the intervention is instantiated—especially zero-shot versus few-shot rationales, exemplar construction, and the use of structured alternatives—with effects varying by model, task, and evaluation setup. Thus, “CoT” should not be treated as a single experimentally invariant intervention; evidence that exemplar number and ordering systematically matter is mixed."

Confidence: HIGH → HIGH

Status: SUPPORTED → WEAK

---

## 6. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ2

**Why**

A high-importance core gap remains: the supplied evidence does not directly test whether rationales are causally used, faithful to the computation, or mainly improve formatting and evaluation. One focused search could materially strengthen the central reasoning-versus-presentation distinction.

**Next Search**

> Find primary causal and process-sensitive studies testing whether LLM chain-of-thought rationales are faithful and causally used: rationale ablation or manipulation, answer-only versus rationale scoring, hidden scratchpads, faithfulness probes, and cases where correct answers persist despite altered or incorrect rationales.


---

# Iteration 3

## 1. Search

**Query**

> Find primary causal and process-sensitive studies testing whether LLM chain-of-thought rationales are faithful and causally used: rationale ablation or manipulation, answer-only versus rationale scoring, hidden scratchpads, faithfulness probes, and cases where correct answers persist despite altered or incorrect rationales.

**Target:** SQ2

**Purpose:** SUBQUESTION

**Why this query**

A high-importance core gap remains: the supplied evidence does not directly test whether rationales are causally used, faithful to the computation, or mainly improve formatting and evaluation. One focused search could materially strengthen the central reasoning-versus-presentation distinction.

5 result(s) retrieved; 5 new unique source(s) added.

- **S11 — Testing Explainability of Chain of Thought for Large Language Models**
  URL: https://www.mdpi.com/2076-3417/16/7/3112
- **S12 — Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures**
  URL: https://arxiv.org/html/2603.16475v1
- **S13 — Causal Sufficiency and Necessity Improves Chain-of- ...**
  URL: https://haoxuanli-pku.github.io/papers/NeurIPS%2025%20-%20Causal%20Sufficiency%20and%20Necessity%20Improves%20Chain-of-Thought%20Reasoning.pdf
- **S14 — Post-hoc reasoning in chain of thought — LessWrong**
  URL: https://www.lesswrong.com/posts/ScyXz74hughga2ncZ/post-hoc-reasoning-in-chain-of-thought
- **S15 — What is faithful chain-of-thought reasoning and why is it ...**
  URL: https://blog.bluedot.org/p/faithful-chain-of-thought

**Search Duration:** 3.21s

---

## 2. Evidence Processing

- New claim proposals: 3
- Existing claim updates: 3
- New gaps: 2
- Resolved gaps: 0

**Processing Duration:** 14.99s

---

## 3. Ledger Updates

### New Claim C7

**Claim**

In one controlled preprint study of schema-guided intermediate structures, across eight models and three benchmarks, models sometimes failed to update their final predictions after the structures were edited—by up to 60% of cases—despite appearing self-consistent with their original structures. Delegating derivation of the final decision to an external tool substantially reduced this fragility, suggesting that these structures can influence decisions without reliably serving as causal mediators in this setting.

- S12 supports (direct): Uses counterfactual interventions in structured reasoning pipelines and reports up to 60% failure to update predictions after intermediate-structure edits, while external-tool derivation largely removes the fragility.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C8

**Claim**

Evidence from causal and mechanistic probes is consistent with post-hoc reasoning in some settings: models can show a reliably decodable answer representation before generating CoT, and prior intervention studies summarized in the source found that perturbing or corrupting generated reasoning often leaves the final answer unchanged.

- S14 supports (direct): Reports AUROC above 0.9 for probes predicting answers before CoT on three of four binary-classification tasks in Gemma-2 9B, and summarizes findings that CoT corruption or intermediate-step perturbation often does not change final answers.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C9

**Claim**

Causal pruning and reconstruction of CoT steps can reduce redundancy and token usage while preserving or improving accuracy on the reported mathematical and commonsense benchmarks, suggesting that some CoT gains may arise from selecting sufficient computation rather than from verbosity itself.

- S13 supports (direct): Introduces causal Probability of Necessity and Sufficiency to identify indispensable and redundant steps, and reports reduced reasoning redundancy and token use without sacrificing or potentially improving accuracy on GSM8K, MATH-500, AIME, and CommonsenseQA.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C3

**Claim**

The supplied sources provide competing interpretations of CoT gains: some present intermediate steps as helping decomposition, attention, coherence, and error reduction, while S1 reports a cited view that modern LLM CoT exemplars may primarily enforce output format rather than improve reasoning quality.

- S13 supports (direct): Treats CoT steps as varying in causal sufficiency and necessity, identifying redundant versus indispensable steps and reporting accuracy-preserving efficiency improvements.
- S12 contradicts (direct): Controlled edits to structured intermediate representations often failed to change model predictions, indicating that explicit intermediate content may be influential context rather than a stable causal mediator.
- S14 contradicts (direct): Reports pre-computed answer representations and summarizes cases where perturbing CoT leaves final answers unchanged, supporting post-hoc or partially independent answer generation.

**Confidence:** HIGH → HIGH

**Status:** CONFLICTING → CONFLICTING

### Updated Claim C4

**Claim**

Structured reasoning prompts can improve both accuracy and inference efficiency relative to flat CoT in at least the reported mathematical evaluations: S1 reports that Hi-CoT increased average accuracy by 6.2% and reduced reasoning-trace length by 13.9% across 13 model configurations and five benchmarks, although these results concern a specific proposed variant and evaluation setting.

- S13 supports (direct): Reports a distinct causal step-selection and reconstruction method that reduces redundancy and token usage while maintaining or improving accuracy across mathematical and commonsense benchmarks.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

In recent strong models evaluated on GSM8K and MATH, traditional few-shot CoT exemplars may fail to improve reasoning performance over zero-shot CoT; their primary observed contribution in the supplied study was aligning output format with human expectations, and enhanced exemplars were likewise reported not to improve reasoning because models tended to rely on the instruction rather than exemplar content.

- S14 supports (direct): Reports evidence that answers can be represented before CoT and that reasoning perturbations may leave conclusions unchanged, consistent with a formatting or post-hoc contribution in at least some tasks.

**Confidence:** MEDIUM → HIGH

**Status:** CONFLICTING → CONFLICTING

### New Gap G5

The new causal-faithfulness evidence concerns structured intermediate representations and a small set of binary-classification experiments, leaving unresolved how often the same intervention results hold for free-form natural-language CoT across difficult mathematical, scientific, coding, and knowledge tasks and across model families and scales.

### New Gap G6

The evidence does not yet establish whether CoT improves performance through additional effective computation, search, decomposition, or response constraints, nor how these mechanisms compare directly with hidden scratchpads, answer-only controls, self-consistency, or external tools under matched token and decoding budgets.

---

## 4. Current Research State

- Claims: 9
- Supported: 6
- Weak: 1
- Conflicting: 2
- Insufficient Evidence: 0
- Open Gaps: 6
- Remaining Searches: 0

### Subquestion Progress

**SQ1:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ2:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ3:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ4:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ5:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

### Research Plan Status

**CORE:**

- SQ1 → CONFLICTING (targeted searches: 0)
- SQ2 → CONFLICTING (targeted searches: 1)
- SQ3 → CONFLICTING (targeted searches: 0)
- SQ5 → CONFLICTING (targeted searches: 0)

**SECONDARY:**

- SQ4 → CONFLICTING (targeted searches: 0)

**Remaining targeted searches:** 0

---

## 5. Independent Verification

### V3 — Claim C7

**Phase:** INITIAL

**Evidence source IDs:** S12

**Verdict:** NEEDS_QUALIFICATION

**Reason**

S12 directly supports the core claim: it reports controlled interventions across eight models and three benchmarks, failures to update after edits in up to 60% of cases, and substantially less fragility when derivation is delegated to an external tool. However, the evidence concerns schema-guided structured mediators—not chain-of-thought generally—and comes from a single reported study. The source supports fragile causal faithfulness more directly than the broader wording that structures are merely correlated with decisions.

**Missing assumptions**

- The benchmark and intervention setup generalize beyond the studied schema-guided tasks and models.
- The reported intervention failures are not substantially driven by unusual prompt, task, or formatting effects.
- The distinction between correlation and causal determination is being applied to structured intermediate representations rather than all explicit reasoning traces.

**Source concerns**

- Only one arXiv source is supplied, with no independent corroboration or replication.
- The source is a versioned preprint, and the saved excerpt does not provide full methodological details, statistical uncertainty, or per-condition results.

**Counter-search status:** NOT_REQUESTED

**Reconciliation**

Claim:

"Controlled intervention evidence indicates that explicit intermediate reasoning structures can be correlated with, but need not causally determine, final model decisions: across eight models and three benchmarks, models sometimes failed to update predictions when the intermediate structure was edited, with failures occurring in up to 60% of cases; delegating derivation from the structure to an external tool substantially reduced this fragility."
→
"In one controlled preprint study of schema-guided intermediate structures, across eight models and three benchmarks, models sometimes failed to update their final predictions after the structures were edited—by up to 60% of cases—despite appearing self-consistent with their original structures. Delegating derivation of the final decision to an external tool substantially reduced this fragility, suggesting that these structures can influence decisions without reliably serving as causal mediators in this setting."

Confidence: HIGH → HIGH

Status: SUPPORTED → SUPPORTED

---

## 6. Research Decision

**Decision:** Stop researching.

**Origin:** BUDGET_STOP

**Why**

The maximum research iteration budget was reached.

**Stop Reason:** max_iterations


---

# Final Research Decision

**Stop Reason:** max_iterations

**Remaining Uncertainty**

- Whether free-form CoT rationales are causally used, faithfully report computation, or mainly improve formatting, inspectability, compliance, or scoring remains unresolved.
- Controlled evidence is insufficient to reconcile differences across model families, parameter scales, task difficulty, prompt wording, decoding or sampling, and evaluation metrics.
- The reported Hi-CoT gains lack independent validation in the supplied evidence and are not shown to generalize beyond the stated mathematical benchmarks.
- The supplied sources do not adequately assess benchmark contamination, benchmark saturation, replication quality, statistical uncertainty, or evaluator sensitivity as explanations for conflicting results.
- It remains unresolved how often causal-faithfulness findings for structured intermediates or binary-classification tasks transfer to free-form CoT on mathematics, science, coding, and knowledge tasks.
- Direct matched-budget comparisons are lacking for CoT versus hidden scratchpads, answer-only and formatting controls, self-consistency, decomposition, and external tools.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Question Decomposition | 1 | 9.49s |
| Tavily Search | 3 | 9.39s |
| Evidence Processing | 3 | 42.40s |
| Independent Verification | 3 | 21.20s |
| Research Decision | 1 | 2.65s |
| Report Generation | 1 | 22.60s |
| Total Run | — | 107.74s |

# Verifier Diagnostics

- Verification calls: 3
- Claims verified: 2
- VERIFIED verdicts: 0
- NEEDS_QUALIFICATION verdicts: 3
- CONTRADICTED verdicts: 0
- INSUFFICIENT_EVIDENCE verdicts: 0
- Counter-searches requested: 1
- Counter-searches executed: 1
- Counter-searches blocked by budget: 0
- Counter-searches blocked as duplicates: 0
- Claims whose wording changed: 2
- Claims whose confidence decreased: 0
- Claims whose status changed: 1
- Searches allocated to general research: 1
- Searches allocated to subquestions: 1
- Searches allocated to counter-search: 1
