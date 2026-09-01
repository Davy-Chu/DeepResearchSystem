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

**Unique Sources:** 42

**OpenAI Calls:** 11

**Tavily Calls:** 10

**Started:** 2026-09-01T04:52:00-04:00

**Ended:** 2026-09-01T04:56:01-04:00

**Total Runtime:** 240.90s

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

- **S1 — [PDF] Structured Chain-of-Thought Prompting for Code Generation - Ge Li**
  URL: https://ligechina.github.io/My%20Papers/2025%20-%20TOSEM%20-%20Structured%20Chain-of-Thought%20Prompting%20for%20Code%20Generation.pdf
- **S2 — Strategic Chain-of-Thought: Guiding Accurate Reasoning in LLMs through Strategy Elicitation**
  URL: https://arxiv.org/html/2409.03271v1
- **S3 — LLM Prompt FORMATS make or break your LLM and RAG**
  URL: https://www.youtube.com/watch?v=M5i3rQfEw_A
- **S4 — Master Prompting Concepts: Chain of Thought Prompting**
  URL: https://promptengineering.org/master-prompting-concepts-chain-of-thought-prompting
- **S5 — Medium**
  URL: https://medium.com/data-science-collective/so-you-think-you-can-prompt-b3384664bafc

**Search Duration:** 4.25s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The provided sources support a qualified conclusion: CoT can improve task accuracy, but its effectiveness is not separable from the prompt’s format, structure, and task-specific inductive bias.

**Confidence:** Medium

**Why this confidence level**

The evidence points in both directions, but S3 is a video/transcript rather than a controlled primary research paper, and the sources do not provide a direct CoT-versus-format-only experiment.

**Evidence**

- The instructional description of CoT presents intermediate steps as improving multi-step problem solving, while the formatting source reports very large accuracy changes from semantically equivalent changes in separators, spacing, and connectors. [S4] [S3]

#### Finding 2

**Claim**

CoT appears more useful when the task genuinely requires decomposed, multi-step reasoning than when the task can be solved by direct pattern matching or answer formatting.

**Confidence:** Medium

**Why this confidence level**

The sources distinguish task types and report task-specific outcomes, but they do not establish a systematic meta-analysis across reasoning and non-reasoning tasks.

**Evidence**

- S4 defines CoT around intermediate steps for complex, multi-step problems and describes gains over standard few-shot prompting on arithmetic and some commonsense tasks; it also says gains on commonsense tasks can be minimal. [S4]
- S1 reports that generic CoT produces only slight improvements in code generation, including a cited 0.82-point improvement on a real-world benchmark, suggesting that merely eliciting prose steps is not uniformly effective. [S1]

#### Finding 3

**Claim**

A major fault line is generic verbal CoT versus structured or strategically constrained intermediate representations. Adding explicit programming structures or a prior problem-solving strategy can outperform ordinary CoT.

**Confidence:** Medium

**Why this confidence level**

Both sources report direct comparisons involving modified CoT methods, but S2 is an arXiv version and the retrieved material does not expose full controls, baselines, or statistical analysis.

**Evidence**

- S1 argues that ordinary CoT mainly represents sequential structure and is poorly suited to branches and loops; its Structured CoT explicitly represents input/output, sequence, branching, and looping, and reportedly improves Pass@1 over CoT by up to 13.79% across code-generation benchmarks and models. [S1]
- S2 reports a two-stage Strategic CoT that elicits a strategy before generating the reasoning path, with reported gains on eight reasoning datasets, including 21.05% on GSM8K and 24.13% on Tracking_Objects for Llama3-8b. [S2]

#### Finding 4

**Claim**

Some apparent CoT gains may be attributable to output/intermediate-format effects rather than a uniquely causal reasoning process.

**Confidence:** Medium

**Why this confidence level**

The evidence strongly motivates format and representation as confounds, but S3 and S5 are secondary sources and do not specifically isolate CoT reasoning from all other prompt changes.

**Evidence**

- S3’s transcript describes accuracy ranging from about 3% to above 80% while keeping content fixed and changing only separators, connectors, spacing, and layout in in-context prompts. [S3]
- S5 summarizes research reporting large performance ranges among semantically equivalent instructions, including Llama-2-70B-chat scores of 0.094 versus 0.549, and frames prompt quality as a robustness problem. [S5]
- S1 characterizes its structured representation as a concise midpoint between natural language and code, explicitly contrasting it with verbose CoT and attributing gains partly to the imposed programming structure. [S1]

#### Finding 5

**Claim**

The presence of a plausible chain does not guarantee correct reasoning; the quality and strategy of the generated path are themselves failure points.

**Confidence:** Medium

**Why this confidence level**

These are direct claims from research papers, but the retrieved excerpts do not provide independent verification or detailed causal analyses of why paths fail.

**Evidence**

- S2 states that CoT is unstable because generated reasoning paths vary in quality, and that even a path resembling valid reasoning can lead to an incorrect final answer. [S2]
- S1 says generic CoT accuracy remains insufficient for practical code generation and gives a 53.29% Pass@1 example for gpt-3.5-turbo on HumanEval. [S1]

### Conflicts Found

- The sources disagree in emphasis about whether CoT is broadly robust and reasoning-enhancing or highly sensitive to presentation. S4/S5 describe CoT as generally robust and beneficial relative to standard few-shot prompting, whereas S3/S5’s formatting evidence indicates that semantically irrelevant prompt changes can cause very large accuracy swings. These claims may be conditionally compatible: CoT can help relative to a matched baseline while the absolute size of the gain remains format- and model-sensitive. [S4] [S5] [S3]
- Generic CoT is described as state-of-the-art and substantially useful in broad reasoning accounts, but S1 reports only slight gains for code generation and motivates replacing generic CoT with a structured representation. This is likely a domain and representation disagreement rather than a direct contradiction. [S1] [S4]
- S2 presents Strategic CoT as substantially improving reliability, while its own motivation concedes that ordinary CoT paths are unstable. The reported improvements therefore support constrained/strategic reasoning more directly than they establish that unconstrained CoT itself is effective. [S2]

### Important Gaps

- Do controlled experiments show that CoT improves latent problem-solving ability after matching token count, delimiters, answer format, and additional computation against non-CoT prompts?
- How often are intermediate CoT steps causally used by the model, rather than being post-hoc rationalizations accompanying an answer selected through pattern matching?
- Are reported gains concentrated in sufficiently large models, particular benchmarks, or tasks with arithmetic/compositional structure?
- How much of the S1 and S2 improvements comes from extra generated tokens, explicit schemas, strategy selection, or better demonstrations rather than from chain-of-thought language itself?
- Do CoT prompts improve final-answer accuracy at the cost of calibration, error detection, or robustness under paraphrase?
- The supplied evidence lacks primary controlled studies directly testing the ‘formatting versus reasoning’ distinction and lacks a systematic comparison across model scales and task families.

**Analysis Duration:** 19.29s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The current sources establish the key hypotheses—genuine task-dependent reasoning benefits, strong format sensitivity, and improvements from structured representations—but they do not directly resolve the central causal question. A focused search for controlled ablations and faithfulness studies would materially improve the answer.

**Next Search**

> chain-of-thought prompting reasoning versus formatting controlled ablation faithfulness prompt format matched baseline

---

# Iteration 2

## 1. Search

**Query**

> chain-of-thought prompting reasoning versus formatting controlled ablation faithfulness prompt format matched baseline

**Why this query**

The current sources establish the key hypotheses—genuine task-dependent reasoning benefits, strong format sensitivity, and improvements from structured representations—but they do not directly resolve the central causal question. A focused search for controlled ablations and faithfulness studies would materially improve the answer.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S6 — The Last Word Often Wins: A Format Confound in Chain-of-Thought Corruption Studies**
  URL: https://arxiv.org/html/2605.10799v1
- **S7 — Faithful Chain of Thought Reasoning Guide**
  URL: https://www.prompthub.us/blog/faithful-chain-of-thought-reasoning-guide
- **S8 — The Decreasing Value of Chain of Thought in Prompting**
  URL: https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought
- **S9 — Chain-of-Thought Prompting: A Guide for LLM Apps and Agents**
  URL: https://www.comet.com/site/blog/chain-of-thought-prompting
- **S10 — Faithful Chain-of-Thought Reasoning - DebugML**
  URL: https://debugml.github.io/fcot

**Search Duration:** 3.56s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

A major fault line is between CoT’s effect on solving and CoT’s effect on reading out an answer: models may use intermediate computation in some cases, yet still preferentially follow an explicit terminal answer statement at readout.

**Confidence:** Medium

**Why this confidence level**

S6 supplies detailed within-dataset ablations and conflicting-answer tests, but it is a single recent preprint and directly studies faithfulness/corruption rather than the overall accuracy benefit of ordinary CoT.

**Evidence**

- S6 reports that, in corruption studies, models followed an explicitly presented wrong terminal answer despite correct intermediate reasoning. Removing only the answer suffix while preserving the reasoning reduced suffix sensitivity by approximately 19× at 3B and 9.3× at 7B; the effect replicated across architectures and on MATH. [S6]
- S6’s generation-time probes found early commitment below 5%, while consumption-time behavior systematically tracked explicit answer text. The authors therefore distinguish computation during generation from answer-text dominance during readout. [S6]

#### Finding 2

**Claim**

The evidence increasingly supports a hybrid account: CoT is not merely cosmetic formatting, but its observed benefit is strongly mediated by presentation format, intermediate representation, and how the final answer is elicited.

**Confidence:** Medium

**Why this confidence level**

The sources converge on representation and formatting as important causal variables, while S1 and S10 also indicate that structured intermediate computation can improve accuracy. However, the retrieved evidence does not establish that all CoT gains reduce to formatting.

**Evidence**

- S6 shows that answer placement can dominate behavioral sensitivity even when reasoning content is held fixed, demonstrating that benchmark CoT formats introduce a causal readout confound. [S6]
- S3 reported large accuracy changes from semantically equivalent changes in separators, spacing, connectors, and layout, while S1 found that imposing structured programming representations could substantially outperform generic verbal CoT. [S3] [S1]
- S10 describes Faithful CoT, which translates natural-language problems into symbolic programs and derives answers through deterministic execution; it reportedly outperformed vanilla CoT on 9 of 10 datasets across four domains. [S10]

#### Finding 3

**Claim**

CoT’s usefulness depends substantially on model type: it tends to offer more benefit to models without built-in reasoning, while generic prompting adds little and can sometimes hurt models that already reason internally.

**Confidence:** Medium

**Why this confidence level**

S8 describes repeated trials and multiple model categories, but it is a technical-report summary rather than the full retrieved experimental paper, and the results come from one difficult multiple-choice benchmark.

**Evidence**

- In a GPQA Diamond study, S8 reports average CoT gains for non-reasoning models ranging from 4.4% to 13.5%, but mixed effects on perfect accuracy, including a 17.2% decline for Gemini Pro 1.5. [S8]
- For reasoning models, S8 reports only small average changes for o3-mini and o4-mini and a 3.3% decrease for Gemini Flash 2.5, alongside 20–80% increases in response time. [S8]
- S8 also reports that many models produced CoT-like reasoning by default, making an explicit step-by-step instruction a weak treatment contrast for those systems. [S8]

#### Finding 4

**Claim**

Faithfulness is a separate dimension from accuracy: a chain can improve performance without being a reliable causal account of how the answer was obtained.

**Confidence:** Medium

**Why this confidence level**

Multiple sources distinguish accuracy from faithfulness, but S7 is a secondary blog and S6 itself leaves open whether its readout effect reflects a broad rationalization mechanism or a narrower instruction-tuned answer-presentation heuristic.

**Evidence**

- S7 summarizes tests involving truncation, inserted mistakes, paraphrasing, and filler tokens, reporting mixed faithfulness results alongside continuing performance benefits from CoT. It states that paraphrasing often preserved accuracy while filler tokens did not reproduce the full benefit. [S7]
- S10 gives examples in which the final answer does not follow from the natural-language chain and motivates a deterministic symbolic-execution method precisely to guarantee alignment between reasoning and answer. [S10]
- S6 cautions that corruption-based evidence for computationally important positions can be invalid when it merely detects answer placement. [S6]

#### Finding 5

**Claim**

The conflicting literature can be reconciled by separating several treatment contrasts that are often labeled ‘CoT’: direct answer versus verbal CoT, generic verbal CoT versus structured/strategic decomposition, and explicit CoT versus a model’s native hidden reasoning.

**Confidence:** High

**Why this confidence level**

This interpretation is supported consistently across the accumulated and new sources, even though the sources do not constitute a formal meta-analysis.

**Evidence**

- S4/S9 describe gains from few-shot or zero-shot CoT on arithmetic and other multi-step tasks, whereas S1 reports only slight generic-CoT gains in code generation and stronger results from structured representations. [S4] [S9] [S1]
- S2 and S10 report improvements from strategic or executable variants, which alter the schema, decomposition, or solver rather than simply adding a request to explain. [S2] [S10]
- S8 finds limited incremental value when models already have built-in reasoning and notes that default behavior often already resembles CoT. [S8]

### Conflicts Found

- S6 finds strong answer-suffix/readout effects and warns that corruption studies may locate answer text rather than computation, while S7 reports that filler tokens do not reproduce CoT’s performance benefit and that the gist of reasoning can matter. These are not necessarily contradictory: reasoning content may contribute to solving, while terminal-answer format independently controls readout and can contaminate faithfulness tests. [S6] [S7]
- S8 reports that generic CoT has little value for built-in reasoning models, whereas S9 presents CoT as broadly valuable and reports large classic benchmark gains. The disagreement is plausibly driven by model generation, benchmark/task choice, baseline definition, and whether the comparison is against direct answering or against a model’s default hidden reasoning. [S8] [S9]
- S6 shows models can follow a wrong explicit answer over correct intermediate computation, whereas S10’s Faithful CoT derives the answer deterministically from symbolic execution. This is a difference between unconstrained natural-language CoT and executable/faithful reasoning, not evidence that all intermediate computation is absent. [S6] [S10]

### Important Gaps

- Do accuracy comparisons remain positive for verbal CoT after matching total computation/token budget, answer placement, delimiters, demonstrations, and output format against a non-CoT control?
- How much of classic CoT’s gain comes from intermediate reasoning versus additional generation time, learned demonstration patterns, or answer-position/readout heuristics?
- Are the model-type effects in S8 replicated across broader task families, model scales, open and closed models, and non-multiple-choice settings?
- Does structured or executable CoT improve underlying generalization and robustness, or mainly make benchmark outputs easier to parse and verify?
- How often do models use correct intermediate steps causally while still producing unfaithful explanations or obeying an explicit but incorrect final answer?
- The new evidence does not directly settle whether ordinary CoT improves latent reasoning ability under tightly format-matched controls.

**Analysis Duration:** 18.16s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The central question remains only partly resolved. The new sources substantially strengthen the case that format and answer placement confound faithfulness claims, and S8 adds model-dependent efficacy evidence, but there is still no retrieved, broad controlled study directly comparing ordinary CoT with format-, token-, computation-, and answer-placement-matched non-CoT alternatives across task families.

**Next Search**

> controlled experiment chain-of-thought versus format-matched non-CoT token-matched reasoning accuracy answer placement

---

# Iteration 3

## 1. Search

**Query**

> controlled experiment chain-of-thought versus format-matched non-CoT token-matched reasoning accuracy answer placement

**Why this query**

The central question remains only partly resolved. The new sources substantially strengthen the case that format and answer placement confound faithfulness claims, and S8 adds model-dependent efficacy evidence, but there is still no retrieved, broad controlled study directly comparing ordinary CoT with format-, token-, computation-, and answer-placement-matched non-CoT alternatives across task families.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S11 — Is Chain-of-Thought Reasoning of LLMs a Mirage? A Data Distribution Lens**
  URL: https://arxiv.org/html/2508.01191v2
- **S12 — Testing Explainability of Chain of Thought for Large Language Models**
  URL: https://www.mdpi.com/2076-3417/16/7/3112
- **S13 — [PDF] Chain-of-Probe: Examining the Necessity and Accuracy of CoT Step ...**
  URL: https://aclanthology.org/2025.findings-naacl.140.pdf
- **S14 — Demystifying Reasoning Models - by Cameron R. Wolfe, Ph.D.**
  URL: https://cameronrwolfe.substack.com/p/demystifying-reasoning-models

**Search Duration:** 3.07s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

New evidence strengthens the conclusion that ordinary CoT is not a uniformly reliable reasoning mechanism; its success depends on distributional familiarity with the task, chain length, and surface format.

**Confidence:** Medium

**Why this confidence level**

S11 presents a controlled experimental framework and a coherent explanatory account, but the retrieved material is an arXiv preprint and does not provide the detailed numerical results needed to assess effect sizes or generality.

**Evidence**

- S11 reports controlled DataAlchemy experiments in which CoT works on in-distribution or near-distribution data but degrades sharply under moderate shifts in task structure, reasoning length, and query format. The authors describe fluent but logically inconsistent chains under these shifts. [S11]

#### Finding 2

**Claim**

CoT can be unnecessary when the model has already selected an answer, especially on simpler questions; generating a chain does not by itself establish that the chain caused the answer.

**Confidence:** Medium

**Why this confidence level**

The evidence converges across two studies, but S13’s probe infers causal dependence from confidence and answer changes rather than directly observing hidden computation.

**Evidence**

- S13 finds early answering across models and multiple-choice reasoning datasets: models often maintain the same answer throughout generation, and early-answer cases are associated with simpler questions. The paper reports that forcibly interrupting or corrupting reasoning often leaves the final answer unchanged. [S13]
- S6 similarly reports that models can follow an explicit terminal answer despite correct intermediate reasoning, separating answer readout from computation during generation. [S6]

#### Finding 3

**Claim**

Correct final answers are not reliable evidence that the accompanying CoT is correct or causally used.

**Confidence:** Medium

**Why this confidence level**

Both sources directly address reasoning-path reliability, but the reported rates and improvements are task- and method-dependent.

**Evidence**

- S13 reports that approximately 20% of CoTs with correct answers contain reasoning errors and argues that answer correctness cannot validate the reasoning path. Its confidence-based filtering and resampling procedure improves accuracy when CoT correctness is also considered. [S13]
- S11 gives examples of fluent chains containing logical contradictions and interprets them as evidence that CoT-style text can reflect learned surface patterns rather than consistent inference. [S11]

#### Finding 4

**Claim**

The literature’s apparent contradiction is partly explained by different notions of ‘reasoning’: elicited verbal CoT in a standard LLM is not equivalent to trained long-horizon reasoning in a reasoning model.

**Confidence:** Medium

**Why this confidence level**

The distinction is conceptually clear and supported by the sources, but S14 is an overview and its performance claims rely partly on reported vendor evaluations.

**Evidence**

- S14 distinguishes standard LLM prompting from reasoning models trained to spend variable inference-time compute, decompose problems, critique partial solutions, and explore alternatives. It describes long internal trajectories as a different generation and training regime from ordinary prompted explanations. [S14]
- S8 finds limited incremental benefit from explicit CoT for models that already produce reasoning-like behavior by default, consistent with the treatment contrast becoming weak for such systems. [S8]

#### Finding 5

**Claim**

The strongest synthesis is a conditional or hybrid account: CoT can improve accuracy by providing useful intermediate computation or decomposition, but its gains are mediated by learned format/schema, distributional familiarity, extra inference, and answer readout conventions; it is therefore not best characterized as either pure reasoning or mere formatting.

**Confidence:** High

**Why this confidence level**

The accumulated evidence now converges across distribution-shift, early-answering, readout, and structured-representation findings. It supports a qualified synthesis, though not the stronger claim that all CoT benefits reduce to formatting.

**Evidence**

- S11 attributes CoT success to structured inductive biases learned from in-distribution data and reports brittleness under task, length, and format shifts. [S11]
- S13 finds that CoT is more often unnecessary on simple questions, while difficult questions are more likely—but not guaranteed—to have their answers changed by the chain. [S13]
- S1, S2, and S10 show that strategic, structured, or executable representations can outperform generic verbal CoT, indicating that the intermediate representation itself is causally important in at least some settings. [S1] [S2] [S10]
- S6 shows that terminal-answer placement can independently dominate behavioral sensitivity, creating a readout confound in faithfulness tests. [S6]

### Conflicts Found

- S11 characterizes CoT as a brittle mirage outside the training distribution, whereas S4, S9, S1, S2, and S10 report meaningful gains from CoT or structured variants. This is a conditional disagreement: benchmark-near-distribution performance can improve while out-of-distribution generalization and logical consistency remain poor. [S11] [S4] [S9] [S1] [S2] [S10]
- S13 reports that early answering is more common and often more accurate on simple questions, suggesting CoT is unnecessary there; S4 and S9 present CoT as broadly useful. The claims can coexist if CoT’s incremental value is concentrated in genuinely difficult, decomposable tasks rather than easy pattern-recognition cases. [S13] [S4] [S9]
- S14 presents trained reasoning models as performing extended search-like computation, while S11 and S13 question whether ordinary generated chains reflect genuine inference. This is primarily a regime distinction, not a direct contradiction between claims about the same intervention. [S14] [S11] [S13]
- S13’s estimate that roughly 20% of correct-answer CoTs contain errors and S6’s answer-suffix effects complicate interpretations of faithfulness tests: a chain may contribute useful computation in some cases while the final answer is independently controlled by readout heuristics. [S13] [S6]

### Important Gaps

- Do verbal CoT gains persist after matching total generated tokens, inference-time compute, delimiters, demonstrations, answer placement, and output format against a non-CoT control?
- How much of CoT’s benefit is due to intermediate computation versus learned task templates, additional sampling time, or answer-position/readout effects?
- Does the distribution-shift brittleness reported by S11 replicate in pretrained frontier models rather than only in the controlled from-scratch DataAlchemy setting?
- Are structured or executable CoT methods improving generalizable problem solving, or mainly supplying a better benchmark-specific schema and verification mechanism?
- How do these effects vary across open versus closed models, model scale, task families, and free-response versus multiple-choice evaluation?
- Can confidence/probing methods such as S13 reliably distinguish causal reasoning from fluent post-hoc explanation without assuming that confidence changes reveal internal computation?

**Analysis Duration:** 17.37s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources substantially clarify the fault lines—task difficulty, distribution shift, representation, model regime, and early answering—but the central causal question remains unresolved: no supplied source directly compares verbal CoT with a computation- and format-matched non-CoT control across broad tasks. That experiment would materially improve the answer.

**Next Search**

> controlled chain-of-thought ablation matched token budget format delimiters answer position non-CoT baseline latent reasoning

---

# Iteration 4

## 1. Search

**Query**

> controlled chain-of-thought ablation matched token budget format delimiters answer position non-CoT baseline latent reasoning

**Why this query**

The new sources substantially clarify the fault lines—task difficulty, distribution shift, representation, model regime, and early answering—but the central causal question remains unresolved: no supplied source directly compares verbal CoT with a computation- and format-matched non-CoT control across broad tasks. That experiment would materially improve the answer.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S15 — SCALABLE CHAIN OF THOUGHTS VIA ELASTIC REA**
  URL: https://proceedings.iclr.cc/paper_files/paper/2026/file/eb0965da1d2cb3fbbbb8dbbad5fa0bfc-Paper-Conference.pdf
- **S16 — Thinking Without Words: Efficient Latent Reasoning with Abstract Chain-of-Thought**
  URL: https://arxiv.org/html/2604.22709v2
- **S17 — LLM Reasoning Is Latent, Not the Chain of Thought (Apr 2026)**
  URL: https://www.youtube.com/watch?v=zAR0Bm6WVWA
- **S18 — Can we interpret latent reasoning using current mechanistic interpretability tools? — LessWrong**
  URL: https://www.lesswrong.com/posts/YGAimivLxycZcqRFR/can-we-interpret-latent-reasoning-using-current-mechanistic

**Search Duration:** 4.27s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

New evidence strengthens the distinction between explicit verbal CoT and intermediate computation: useful reasoning can occur through non-verbal latent or abstract representations, so human-readable chains are not necessary for performance gains.

**Confidence:** Medium

**Why this confidence level**

The results directly compare alternative intermediate representations, but S16 is a recent preprint and S18 is a preliminary interpretability report using a small model trained on narrow datasets.

**Evidence**

- Abstract-CoT replaces natural-language rationales with short reserved-token sequences and reports comparable performance across mathematical, instruction-following, and multi-hop tasks while using up to 11.6 times fewer reasoning tokens. [S16]
- A latent-CoT study compares direct-answer, verbal-CoT, and latent-CoT modes within one shared model and finds latent-CoT improvements over direct answering on GSM8K, MultiArith, and SVAMP, though not on CommonsenseQA. [S18]

#### Finding 2

**Claim**

At least in a specially trained model, intermediate latent vectors can contribute causally beyond the model's direct-answer mode, but this does not show that ordinary prompted verbal CoT has the same causal status.

**Confidence:** Medium

**Why this confidence level**

The shared-weight design is substantially stronger than an independently trained baseline, but it evaluates a post-trained latent-reasoning system rather than zero-shot or few-shot verbal CoT in ordinary pretrained models.

**Evidence**

- S18 uses a shared-weight three-mode model, allowing latent CoT to be compared with a direct-answer mode that receives the same training exposure. Latent CoT improves accuracy by 4.88 points on GSM8K, 15.55 points on MultiArith, and 2.73 points on SVAMP, while slightly decreasing CommonsenseQA performance. [S18]
- S18 explicitly argues that the original latent-CoT versus No-CoT comparison was confounded because the latent-CoT model also benefited from co-training on verbal reasoning traces; its shared-weight baseline is intended to remove that confound. [S18]

#### Finding 3

**Claim**

The effectiveness of intermediate reasoning depends on task structure: latent or explicit reasoning helps on some multi-step arithmetic tasks but can provide little or negative benefit on commonsense or simpler pattern-based tasks.

**Confidence:** High

**Why this confidence level**

The task-dependent pattern is consistent across the new and accumulated evidence, although the magnitude and generality of the effects remain model- and benchmark-dependent.

**Evidence**

- In S18, latent CoT improves MultiArith by 15.55 points and GSM8K by 4.88 points over direct answering, but decreases CommonsenseQA by 0.25 points; verbal CoT also decreases CommonsenseQA by 2.41 points. [S18]
- S13 and S4 previously indicated that CoT's incremental value is concentrated in difficult, decomposable tasks and is often unnecessary for simpler questions. [S13] [S4]

#### Finding 4

**Claim**

Longer reasoning trajectories can be useful as additional inference-time computation, but raw chain length is not itself the essential mechanism; allocating computation between thinking and solution generation matters.

**Confidence:** Medium

**Why this confidence level**

S15 is a conference paper with experimental comparisons, but its methods are trained reasoning models and therefore do not isolate the effect of ordinary prompting or verbal formatting.

**Evidence**

- S15 treats extended CoT as a form of test-time scaling and reports that separate budgets for thinking and solution generation outperform direct truncation or undifferentiated budget control under tight token constraints. [S15]
- S15 reports that preserving a solution segment is important: emitting a transition to a final-answer phase performs better than simply truncating the reasoning trajectory, and budget-constrained training improves robustness to incomplete thinking. [S15]

#### Finding 5

**Claim**

The new evidence supports a three-way account rather than a binary reasoning-versus-formatting choice: intermediate representations may carry task-relevant information, extra serial computation may help, and surface language is only one possible interface.

**Confidence:** High

**Why this confidence level**

The sources converge on multiple causal components and reject both extremes: verbal CoT is not proven to be the complete reasoning process, but its benefits cannot be reduced to cosmetic formatting alone.

**Evidence**

- S16 shows that learned abstract tokens can replace verbal rationales while preserving performance, suggesting that natural-language formatting is not required for the intermediate process. [S16]
- S18 finds latent-CoT gains under a shared-weight direct-answer control, suggesting that intermediate latent states can add computation beyond direct output in a trained system. [S18]
- S15 reports performance scaling with controllable reasoning budgets and emphasizes separate thinking and solution phases, supporting a role for additional computation and answer-readout structure. [S15]
- The accumulated evidence shows that prompt separators, answer placement, schemas, and structured representations can independently affect results. [S3] [S6] [S10]

### Conflicts Found

- S16 and S18 suggest that non-verbal intermediate states can preserve or improve performance, while S17's position-paper summary claims that ordinary surface CoT is often merely an unfaithful interface and that latent trajectories explain reasoning almost entirely. The stronger 'almost entirely' conclusion is not established by S16 or S18: both show that latent representations can work, not that verbal CoT never contributes causally. [S16] [S17] [S18]
- S15 presents extended reasoning and test-time computation as major sources of performance and robustness, whereas S18 shows meaningful gains from only a small fixed number of latent iterations in a 1B model. These findings may reflect different regimes: trained long-horizon reasoning models versus a narrowly trained latent-CoT model, rather than a disagreement about whether intermediate computation can help. [S15] [S18]
- S18 reports that latent CoT is slightly worse than direct answering on CommonsenseQA, while its arithmetic results are positive. This reinforces the accumulated task-dependence finding but conflicts with any claim that latent intermediate computation is uniformly beneficial. [S18]
- S15's success from controlling thinking and solution budgets could be interpreted as evidence for reasoning computation, but the comparison does not match verbal-CoT and non-CoT prompts on all surface variables. Thus it does not resolve whether classic prompted CoT gains are formatting-mediated. [S15]

### Important Gaps

- Do ordinary pretrained models show a causal benefit from verbal CoT after matching total tokens, inference-time computation, delimiters, demonstrations, answer placement, and output format against a direct-answer control?
- How much of the performance of trained latent or abstract CoT comes from latent-state computation versus additional positions, post-training exposure to rationales, or task-specific supervision?
- Do latent or abstract representations generalize better than verbal CoT under task-structure, reasoning-length, and prompt-format distribution shifts?
- Can the results from the small, narrowly trained CODI model in S18 replicate across larger models, broader domains, and free-response tasks?
- Does separating thinking from solution generation improve underlying reasoning, or mainly prevent truncation and answer-readout failures?
- The supplied new material does not provide a direct, format-matched verbal-CoT-versus-non-CoT ablation for standard prompting.

**Analysis Duration:** 18.79s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The central unresolved issue remains unanswered: whether ordinary verbal CoT itself improves problem solving when formatting, token budget, answer placement, demonstrations, and computation are carefully matched. The new sources clarify that latent and trained reasoning can be effective, but they do not isolate the causal contribution of prompted natural-language chains in standard LLMs.

**Next Search**

> controlled causal study verbal chain-of-thought versus latent reasoning versus direct answer matched token budget delimiters answer position inference compute

---

# Iteration 5

## 1. Search

**Query**

> controlled causal study verbal chain-of-thought versus latent reasoning versus direct answer matched token budget delimiters answer position inference compute

**Why this query**

The central unresolved issue remains unanswered: whether ordinary verbal CoT itself improves problem solving when formatting, token budget, answer placement, demonstrations, and computation are carefully matched. The new sources clarify that latent and trained reasoning can be effective, but they do not isolate the causal contribution of prompted natural-language chains in standard LLMs.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S19 — LLM Reasoning Is Latent, Not the Chain of Thought**
  URL: https://arxiv.org/html/2604.15726v1
- **S20 — LLM Reasoning Is Latent, Not the Chain of Thought Wenshuo Wang**
  URL: https://arxiv.org/pdf/2604.15726
- **S21 — Brevity is the Soul of Inference Efficiency**
  URL: https://www.datologyai.com/blog/brevity-is-the-soul-of-inference-efficiency
- **S22 — Inference Budget**
  URL: https://www.aussieai.com/research/inference-budget

**Search Duration:** 3.52s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new position paper sharpens the debate into three distinct causal hypotheses: explicit surface CoT, latent-state trajectories, and generic serial computation.

**Confidence:** High

**Why this confidence level**

The distinction is stated directly and consistently in two versions of the same source, though they are not independent evidence.

**Evidence**

- S19/S20 explicitly distinguish surface trace content, task-relevant hidden-state trajectories, and additional serial compute, arguing that standard CoT changes at least surface traces and compute allocation simultaneously. [S19] [S20]

#### Finding 2

**Claim**

S19/S20 support treating latent-state dynamics as a useful default object of study, but they do not establish that ordinary verbal CoT is causally ineffective or merely formatting.

**Confidence:** Medium

**Why this confidence level**

This is a position paper's synthesis rather than a clearly reported independent controlled result; the retrieved excerpt does not provide enough detail about its claimed compute-audited exemplars to evaluate them.

**Evidence**

- The paper argues that current evidence favors latent-trajectory mediation as a working hypothesis because verbal CoT is often useful without being faithful and because latent reasoning can operate without natural-language traces. [S19] [S20]
- The paper itself presents H1 as a default working hypothesis rather than a task-independent verdict, and acknowledges boundary regimes where surface traces or serial compute may dominate. [S19] [S20]

#### Finding 3

**Claim**

The most defensible interpretation remains a three-way hybrid account: CoT outcomes can reflect latent computation, generic extra serial compute, and surface schemas or readout conventions, with their relative contribution varying by task and model.

**Confidence:** High

**Why this confidence level**

The new source provides a useful causal framework that is consistent with multiple accumulated findings; it does not require the stronger claim that all CoT gains are formatting effects.

**Evidence**

- S19/S20 state that CoT, latent-reasoning methods, and test-time scaling move surface traces, hidden-state dynamics, and compute budgets together, making causal attribution difficult. [S19] [S20]
- Prior evidence shows task-dependent gains, structured and latent representations that can outperform direct answering, and independent effects of answer placement and prompt formatting. [S1] [S6] [S10] [S13] [S18]

#### Finding 4

**Claim**

Evidence about longer outputs and inference budgets supports the importance of computation allocation and cost, but does not by itself show that ordinary verbal CoT improves reasoning.

**Confidence:** Low

**Why this confidence level**

S21 concerns curated vision-language models and S22 is a secondary research overview; neither isolates the causal contribution of CoT language, latent computation, or answer formatting in standard LLM prompting.

**Evidence**

- S21 reports that concise VLMs can match or exceed verbose models at substantially lower token cost and that generic verbosity need not improve accuracy, while distinguishing reasoning-structured verbosity from generic verbosity. [S21]
- S22 lists budget-based CoT and reasoning methods, but is an overview/catalogue rather than a controlled comparison of verbal CoT against a format-matched direct-answer baseline. [S22]

### Conflicts Found

- S19/S20 favor latent trajectories as the default explanatory object, while S16/S18 show that latent or abstract intermediate representations can work but do not prove that ordinary verbal CoT is non-causal. The disagreement is therefore between a methodological/position claim and narrower empirical demonstrations. [S19] [S20] [S16] [S18]
- S21 suggests that generic verbosity can add no accuracy and may be wasteful, whereas S15 and other prior sources find benefits from extended reasoning budgets. These claims concern different treatments: generic verbosity or VLM output length versus trained reasoning procedures with allocated thinking and solution phases. [S21] [S15]
- S19/S20 identify generic serial compute as a competing explanation, but the accumulated evidence includes both compute-sensitive gains and representation-specific gains. Current sources do not determine whether compute alone explains most classic CoT improvements. [S19] [S20] [S15] [S16] [S18]

### Important Gaps

- The central causal gap remains unresolved: there is no supplied primary experiment matching total generated tokens, inference-time compute, delimiters, demonstrations, answer placement, and output format between verbal CoT and a non-CoT control in ordinary pretrained models.
- S19/S20 refer to compute-audited worked exemplars, but the retrieved content does not expose their numerical results, controls, or independent replication.
- It remains unclear how much classic CoT gains derive from semantic intermediate content versus additional serial computation, learned task schemas, and answer-position/readout heuristics.
- The latent-trajectory hypothesis has not been shown to generalize across model scales, domains, free-response tasks, and distribution shifts.
- The evidence does not establish whether concise or abstract reasoning representations preserve robustness and causal faithfulness, rather than only benchmark accuracy and efficiency.
- S21's VLM findings cannot be directly generalized to text-only LLM CoT.

**Analysis Duration:** 12.54s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

A further search would materially improve the answer because the original question specifically asks whether CoT has a reasoning effect beyond formatting. The accumulated sources support a nuanced hybrid account but still lack the decisive matched-control experiment for ordinary verbal CoT.

**Next Search**

> chain-of-thought versus direct answer matched token budget format answer position controlled ablation latent reasoning causal effect

---

# Iteration 6

## 1. Search

**Query**

> chain-of-thought versus direct answer matched token budget format answer position controlled ablation latent reasoning causal effect

**Why this query**

A further search would materially improve the answer because the original question specifically asks whether CoT has a reasoning effect beyond formatting. The accumulated sources support a nuanced hybrid account but still lack the decisive matched-control experiment for ordinary verbal CoT.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S23 — Making Reasoning Matter**
  URL: https://debjitpaul.github.io/reasoningmatter
- **S24 — Answer-Conditioned Chains of Thought Degrade Verifiable-Reasoning Distillation in Large Language Models**
  URL: https://arxiv.org/html/2607.14552v1
- **S25 — Dynamics Within Latent Chain-of-Thought: An Empirical Study of Causal Structure**
  URL: https://arxiv.org/html/2602.08783v3
- **S26 — The Token Economics of Chain-of-Thought: When Thinking Out Loud Costs More Than It's Worth**
  URL: https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more

**Search Duration:** 4.81s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Causal mediation evidence indicates that ordinary CoT is often not faithfully used as an intermediate reasoning process, especially by vanilla small and medium-sized zero-shot LMs.

**Confidence:** Medium

**Why this confidence level**

S23 reports a direct causal-analysis framework across 11 models and multiple tasks, but the retrieved material provides summary results rather than complete tables, statistical details, or independent replication.

**Evidence**

- S23 treats the reasoning chain as a mediator between problem and answer and reports that vanilla LMs below 20B are systematically unfaithful and consistently fail to reason over their own generated mediator; instruction tuning and CoT-related training improve the indirect effect, but do not make it uniformly strong. [S23]

#### Finding 2

**Claim**

Faithfulness varies by training regime, model capability, and task; larger or more capable models are not automatically more causally dependent on their verbal CoT.

**Confidence:** Medium

**Why this confidence level**

The reported conditional patterns directly address model and task heterogeneity, but they come primarily from one study and causal mediation estimates can depend on the intervention design.

**Evidence**

- S23 reports that instruction-tuned or CoT-trained models have better indirect effects, while RLHF models can show stronger direct than indirect effects. It also reports inverse scaling on some tasks, where the indirect effect worsens as models become more capable. [S23]
- S23 reports different mediation patterns for GPT-4 and ChatGPT: GPT-4 has higher natural indirect effects on StrategyQA and causal understanding, whereas ChatGPT has a higher indirect effect on GSM8K; GPT-4 sometimes rejects intervened reasoning and regenerates its own solution. [S23]

#### Finding 3

**Claim**

The new evidence strengthens the distinction between CoT improving answer accuracy and CoT being a faithful explanation of the computation that produced the answer.

**Confidence:** High

**Why this confidence level**

Independent sources converge on accuracy–faithfulness dissociation, although they use different faithfulness tests and do not establish a single universal mechanism.

**Evidence**

- S23 explicitly reports plausible but unfaithful chains and inconsistent reasoning over self-generated traces, while proposing FRODO to separately train correct inference steps and a reasoner that uses them faithfully. [S23]
- This is consistent with S6 and S13, which found terminal-answer/readout effects and reasoning errors in chains accompanying correct answers. [S6] [S13]

#### Finding 4

**Claim**

Answer-conditioned rationalization is a concrete failure mode showing that a correct-looking chain can be generated by working backward from the answer rather than deriving it.

**Confidence:** Medium

**Why this confidence level**

The one-bit intervention and length-matched controls are unusually relevant to causal interpretation, but S24 is a recent preprint, concerns reasoning distillation rather than ordinary inference-time prompting, and contains apparent formatting/number-rendering artifacts in the retrieved text.

**Evidence**

- S24 reports a controlled distillation experiment holding the generator, problems, correctness filter, data volume, and chain length fixed while varying whether the gold answer and rationalize-toward instruction are used. Answer-conditioned chains produced substantially worse verifiable-reasoning students, with the penalty increasing on harder math and code tasks; a prompt ablation attributes the harm mainly to the instruction to rationalize toward the answer. [S24]

#### Finding 5

**Claim**

The answer-conditioned-chain result does not show that all verbal CoT is merely formatting; it shows that the provenance and generation policy of the chain can determine whether it teaches or supports derivation.

**Confidence:** High

**Why this confidence level**

The task-dependent pattern is consistent across the new and accumulated evidence, though the sources do not isolate every contribution of format, compute, and semantic content.

**Evidence**

- S24 finds no penalty on multiple-choice knowledge and science benchmarks, while observing large degradation on tasks requiring derived answers. This makes the effect conditional on whether a genuine derivation is needed. [S24]
- S1, S2, and S10 similarly show that structured, strategic, or executable intermediate representations can outperform generic verbal CoT, suggesting that semantic organization and verification—not verbosity alone—matter. [S1] [S2] [S10]

#### Finding 6

**Claim**

Latent-CoT causal structure is heterogeneous and staged rather than equivalent to uniform extra depth, supporting a three-way account involving latent computation, serial compute, and surface/readout effects.

**Confidence:** Medium

**Why this confidence level**

S25 provides intervention-based evidence rather than mere correlation, but it studies specialized latent-reasoning systems and does not directly compare them with ordinary prompted verbal CoT under matched compute and formatting.

**Evidence**

- S25 applies step-wise interventions to Coconut and CODI and reports that a small subset of latent steps has outsized causal influence, effects can propagate non-locally, and output preference can appear before representational commitment. [S25]
- These findings complement S18 and S19/S20: latent states can contribute causally in trained systems, but surface CoT, latent trajectories, and computation budgets are distinct causal variables. [S18] [S19] [S20]

#### Finding 7

**Claim**

The accumulated evidence now supports a conditional hybrid conclusion, not either extreme: CoT can provide useful intermediate computation or task decomposition, but many observed gains and failures are mediated by learned schemas, answer readout, distributional familiarity, and extra computation; verbalization itself is neither necessary nor sufficient.

**Confidence:** High

**Why this confidence level**

The new findings reinforce rather than overturn the prior synthesis and add stronger causal evidence for unfaithfulness, rationalization, and latent computation. They still do not identify the average causal contribution of verbal CoT itself in standard prompting.

**Evidence**

- S23 finds weak and inconsistent mediation for vanilla LMs; S24 shows answer-conditioned rationalization can corrupt learning; S25 finds causally influential latent steps; and prior sources show task-dependent gains, formatting sensitivity, structured-representation benefits, and answer-placement confounds. [S23] [S24] [S25] [S1] [S6] [S11] [S18] [S19] [S20]

### Conflicts Found

- S23 reports that vanilla LMs often fail to use their own reasoning chains causally, whereas classic CoT literature reports accuracy improvements. This is a faithfulness-versus-performance conflict: CoT can improve outputs without the visible chain being a faithful mediator, or can help only on a subset of examples and tasks. [S23] [S4] [S9] [S13]
- S23 reports inverse scaling of indirect effects on some tasks, while S25 finds causally influential latent steps in specialized latent-reasoning systems. The difference likely reflects regime: ordinary or instruction-tuned verbal CoT versus explicitly trained latent-CoT models, not a direct contradiction about all intermediate computation. [S23] [S25]
- S24 shows that answer-conditioned chains can damage reasoning distillation even after correctness filtering, while S10 and S24's answer-blind condition support the usefulness of derivational or executable chains. Thus final-answer correctness is insufficient to distinguish genuine reasoning from rationalization. [S24] [S10]
- S26 presents broad claims about token costs, model categories, and benchmark effects, but it is a blog summary and does not provide the controlled methods needed to adjudicate the formatting-versus-reasoning question. Its practical conclusions should therefore carry less evidentiary weight than S23–S25 or the primary studies summarized earlier. [S26]

### Important Gaps

- Do ordinary pretrained or instruction-tuned LMs show a positive verbal-CoT effect after matching total generated tokens, inference-time compute, delimiters, demonstrations, answer placement, and output format against a direct-answer control?
- What proportion of classic CoT accuracy gains is caused by semantic intermediate content, generic serial computation, learned task schemas, or terminal-answer/readout conventions?
- Does the causal mediation pattern in S23 replicate across larger frontier models, free-response tasks, model scales, and broader domains?
- Are the latent-step causal findings in S25 generalizable beyond Coconut and CODI, and do they explain gains that would otherwise be attributed to verbal CoT?
- Can faithfulness interventions distinguish useful but incomplete reasoning from post-hoc rationalization without conflating answer placement with computation?
- Do structured, executable, or latent CoT methods improve out-of-distribution reasoning rather than mainly improving benchmark-specific schemas or verification?
- How much of S24's distillation penalty transfers to ordinary inference-time CoT, where no student is trained on the generated chains?
- The retrieved material still lacks a direct, fully format-matched primary experiment isolating verbal CoT language from extra computation and output/readout effects.

**Analysis Duration:** 20.76s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources materially strengthen the faithfulness and latent-computation sides of the synthesis, but they do not resolve the central causal comparison for ordinary prompted verbal CoT. A focused search for a primary controlled ablation is warranted; further general summaries or token-cost articles would add little.

**Next Search**

> primary controlled study verbal chain-of-thought versus direct answer matched token budget output format answer position delimiters inference compute LLM

---

# Iteration 7

## 1. Search

**Query**

> primary controlled study verbal chain-of-thought versus direct answer matched token budget output format answer position delimiters inference compute LLM

**Why this query**

The new sources materially strengthen the faithfulness and latent-computation sides of the synthesis, but they do not resolve the central causal comparison for ordinary prompted verbal CoT. A focused search for a primary controlled ablation is warranted; further general summaries or token-cost articles would add little.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S27 — Chain of Thought Reasoning, the New LLM Breakthrough – Artificial Intelligence Management**
  URL: https://blog.iese.edu/artificial-intelligence-management/2024/chain-of-thought-reasoning-the-new-llm-breakthrough
- **S28 — Dynamic Micro-Batch and Token-Budget Scheduling for IoT-Scale Pipeline-Parallel LLM Inference**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12944026
- **S29 — What is chain of thought (CoT) prompting? - IBM**
  URL: https://www.ibm.com/think/topics/chain-of-thoughts
- **S30 — Medium**
  URL: https://cobusgreyling.medium.com/concise-chain-of-thought-ccot-prompting-6d9119fc0fdf

**Search Duration:** 3.79s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources do not materially resolve whether ordinary verbal CoT improves reasoning beyond formatting and extra computation.

**Confidence:** High

**Why this confidence level**

The retrieved content is either explanatory, secondary, focused on trained reasoning rather than ordinary prompting, or unrelated to the causal question.

**Evidence**

- S27 discusses trained reasoning systems and process supervision, but does not report a format-matched inference-time comparison between verbal CoT and direct answering in ordinary pretrained models. [S27]
- S29 provides a general explanation of CoT’s intended mechanism and claimed benefits, without controlled ablations or causal tests. [S29]
- S30 reports comparisons between verbose and concise CoT, but the retrieved account is a secondary summary using limited prompts and GPT models; it does not match computation, answer placement, delimiters, and output format against a non-CoT control. [S30]
- S28 concerns inference scheduling and token-budget allocation for serving LLMs, not CoT’s reasoning or formatting effects. [S28]

#### Finding 2

**Claim**

S27 reinforces the distinction between prompted verbal CoT and reasoning models trained to carry out and refine multi-step processes.

**Confidence:** Medium

**Why this confidence level**

The distinction is relevant and consistent with S14, S15, S18, and S19/S20, but S27 is a blog post quoting other work rather than the primary experimental reports.

**Evidence**

- S27 contrasts asking an LLM to think step by step with o1-like models trained through reinforcement learning to refine strategies, correct mistakes, decompose problems, and allocate additional inference-time computation. [S27]
- S27 cites process supervision work as finding that feedback on intermediate steps outperformed outcome-only supervision on MATH, indicating that training a reliable process is a different intervention from merely eliciting a rationale. [S27]

#### Finding 3

**Claim**

The CCoT evidence suggests that shorter or more compressed chains can preserve performance in some settings, but it also shows task-specific penalties and does not establish that verbal chain content is the causal source of CoT gains.

**Confidence:** Low

**Why this confidence level**

The result is relevant to verbosity and computation allocation, but the source is a secondary summary and lacks enough methodological detail for strong causal inference.

**Evidence**

- S30 reports that concise CoT reduced response length and average token cost while preserving performance in multiple-choice tasks, but incurred a reported 27.69% penalty on math problems. [S30]
- S30 states that its comparison used one CoT and one CCoT prompt and only GPT models, leaving open whether the result reflects semantic reasoning content, formatting, prompt selection, or model-specific behavior. [S30]

#### Finding 4

**Claim**

The accumulated evidence still supports a three-way hybrid account: CoT outcomes may involve task-relevant intermediate computation, generic extra serial computation, and surface schemas or answer-readout conventions.

**Confidence:** High

**Why this confidence level**

The new material is consistent with, but does not substantially strengthen beyond, the prior convergent synthesis.

**Evidence**

- Prior controlled and intervention-based findings report latent-step effects, weak or inconsistent mediation by visible chains, answer-placement effects, task dependence, and benefits from structured or executable representations. [S6] [S13] [S18] [S23] [S25]
- S27’s distinction between prompted explanations and process-trained reasoning models further supports separating verbal elicitation from trained inference-time computation. [S27]
- S30’s mixed results for concise versus verbose chains are compatible with the view that raw verbosity is not the essential mechanism, while task-appropriate intermediate structure may still matter. [S30]

### Conflicts Found

- S29 presents CoT as a generally effective step-by-step method for complex reasoning, while S23, S6, and S13 show that visible chains can be unfaithful, unnecessary, or dominated by answer-readout effects. This is chiefly a difference between an instructional account of intended behavior and empirical evidence about causal use. [S29] [S23] [S6] [S13]
- S30 reports that concise CoT can preserve multiple-choice performance and reduce token use, whereas S30 also reports a substantial math penalty. This reinforces task dependence and conflicts with any claim that shorter chains are uniformly equivalent to standard CoT. [S30]
- S27 emphasizes process-trained reasoning and additional inference-time search, while classic prompting sources such as S29 discuss eliciting verbal explanations. These are different interventions and should not be treated as direct evidence for or against ordinary prompted CoT. [S27] [S29]

### Important Gaps

- The central causal gap remains unresolved: no supplied source directly compares ordinary verbal CoT with a non-CoT control while matching total generated tokens, inference-time compute, delimiters, demonstrations, answer placement, and output format.
- It remains unclear how much classic CoT gains derive from semantic intermediate content versus generic serial computation, learned task schemas, and terminal-answer/readout conventions.
- S27’s process-supervision discussion does not establish whether process-trained models’ gains transfer to inference-time verbal prompting in ordinary pretrained or instruction-tuned models.
- S30’s concise-CoT findings need primary-paper verification and broader replication across model families, model scales, free-response tasks, and distribution shifts.
- The evidence still does not quantify how often visible CoT is causally used in standard prompting, as opposed to functioning as an unfaithful explanation or output scaffold.

**Analysis Duration:** 21.46s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

Another search would materially improve the answer by targeting the still-unanswered central comparison: a primary, format- and compute-matched causal ablation of verbal CoT versus direct answering in ordinary LLMs. The new sources add context but do not provide that experiment.

**Next Search**

> primary study verbal chain-of-thought versus direct answer matched compute token budget answer position delimiters causal ablation ordinary language models

---

# Iteration 8

## 1. Search

**Query**

> primary study verbal chain-of-thought versus direct answer matched compute token budget answer position delimiters causal ablation ordinary language models

**Why this query**

Another search would materially improve the answer by targeting the still-unanswered central comparison: a primary, format- and compute-matched causal ablation of verbal CoT versus direct answering in ordinary LLMs. The new sources add context but do not provide that experiment.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S31 — Verbalizable Representations Form a Global Workspace in ...**
  URL: https://transformer-circuits.pub/2026/workspace
- **S32 — Token-budget ablation for 10% of the persetting optimal ...**
  URL: https://www.researchgate.net/figure/Token-budget-ablation-for-10-of-the-persetting-optimal-token-count-The-x-axis-shows-the_fig2_400856240
- **S33 — Causal Abstraction for Chain-of-Thought Reasoning in ...**
  URL: https://aclanthology.org/2023.blackboxnlp-1.12.pdf
- **S34 — Token-Budget-Aware LLM Reasoning**
  URL: https://arxiv.org/html/2412.18547v4

**Search Duration:** 5.24s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

New evidence directly supports a conditional causal role for verbal CoT in at least some arithmetic reasoning settings, rather than reducing all CoT gains to output formatting.

**Confidence:** Medium

**Why this confidence level**

S33 is a direct causal study relevant to the question, but it is limited to arithmetic word problems and reports heterogeneous results; it also states that other internal processes may contribute.

**Evidence**

- S33 evaluates whether generated intermediate tokens causally affect final answers using causal-abstraction interventions. Among cases with correct chains and answers, models substantially realize the causal model implied by their chains, and greater realization is associated with higher overall accuracy. [S33]

#### Finding 2

**Claim**

CoT faithfulness and causal use vary across models and examples, so aggregate CoT accuracy cannot be interpreted as proof that the visible chain produced the answer.

**Confidence:** High

**Why this confidence level**

The new causal-abstraction evidence and several prior intervention/mediation studies converge on heterogeneous causal use rather than a single universal mechanism.

**Evidence**

- S33 reports high correlation between correct chains and correct answers, but only says that some models use their chains to reason at least partly; other internal processes appear important for some models. [S33]
- The accumulated evidence reports unfaithful chains, answer-suffix/readout effects, early answering, and weak mediation in vanilla models. [S6] [S13] [S23]

#### Finding 3

**Claim**

The strongest new clarification is that verbal CoT can be an operational intermediate representation, but this does not establish that language itself is necessary; causal use of intermediate tokens is distinct from the causal necessity of their surface wording.

**Confidence:** High

**Why this confidence level**

The sources distinguish causal intermediate processing from the particular natural-language form used to express it, although no study supplied here fully matches verbal and nonverbal representations on all relevant controls.

**Evidence**

- S33 treats intermediate CoT tokens as variables in a causal model and finds partial realization of the described reasoning process. [S33]
- Prior sources show that latent, abstract, structured, and executable intermediate representations can also improve performance, while prompt separators and answer placement independently affect results. [S1] [S6] [S10] [S16] [S18]

#### Finding 4

**Claim**

Token length and computation budget are important mediators of CoT performance and cost, but shortening a chain while preserving accuracy does not show that the remaining verbal content caused the gain.

**Confidence:** Medium

**Why this confidence level**

S34 provides useful budget ablations and efficiency results, but it does not compare verbal CoT with a format-matched non-CoT control at equal inference compute.

**Evidence**

- S34 reports that prompt-specified or post-trained token budgets can reduce CoT token usage substantially while preserving most accuracy; its example reduces output from 258 to 86 tokens without losing the correct answer, and TALE-EP reports a 67% average reduction with less than a 3% accuracy decrease. [S34]

#### Finding 5

**Claim**

The new sources reinforce a three-way causal account: visible chain content, intermediate computation, and generic extra serial computation/readout format can each matter, with their contributions varying by task and model.

**Confidence:** High

**Why this confidence level**

The evidence is mutually consistent with a hybrid account and does not support either the claim that CoT is purely cosmetic or the claim that every visible chain is a faithful reasoning trace.

**Evidence**

- S33 finds that some models realize the causal structure represented by their CoTs, while acknowledging other internal processes. [S33]
- S34 shows that the quantity and allocation of reasoning tokens affect cost and performance. [S34]
- S31 describes intervenable, verbalizable internal representations used for report, modulation, and intermediate reasoning, but the retrieved excerpt does not present task-level CoT ablations. [S31]
- Prior findings independently identify latent-step effects, formatting and answer-placement effects, task dependence, and benefits from structured representations. [S6] [S11] [S18] [S19] [S20] [S25]

### Conflicts Found

- S33 provides evidence that some CoT-prompted models causally use intermediate tokens in arithmetic, whereas S23, S6, and S13 report frequent unfaithfulness, answer-readout dominance, or answer stability under chain interventions. This is a conditional conflict resolved partly by model, task, example, and intervention differences: causal use can occur without being universal. [S33] [S23] [S6] [S13]
- S34 shows that much CoT output can be compressed with little accuracy loss, while S15 and other accumulated sources report benefits from extended reasoning budgets. These results concern different regimes and do not determine whether the essential resource is semantic chain content, allocated computation, or a suitable stopping/solution format. [S34] [S15]
- S31's global-workspace interpretation suggests privileged verbalizable internal representations that support flexible reasoning, while the accumulated faithfulness evidence warns that reported chains may be unfaithful. S31 concerns internal representations poised for verbalization, not necessarily the literal output chain, so it does not directly contradict the faithfulness findings. [S31] [S6] [S23]

### Important Gaps

- Does the causal-abstraction result in S33 replicate across model scales, domains, free-response tasks, and non-arithmetic reasoning?
- Can verbal CoT's causal contribution be isolated while matching total tokens, inference-time computation, demonstrations, delimiters, answer placement, and output format against a direct-answer or nonverbal-scratchpad control?
- What proportion of classic CoT gains is due to semantic intermediate content, generic serial computation, learned task schemas, and terminal-answer/readout conventions?
- Does S31's proposed workspace-like representation causally mediate ordinary prompted CoT benefits, or does it mainly describe internal states of models with separately trained reasoning behavior?
- Do compressed CoT methods preserve robustness, error detection, and out-of-distribution generalization, rather than only benchmark accuracy?

**Analysis Duration:** 16.64s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

S33 materially improves the evidence by supplying direct causal-abstraction results, but the central formatting-versus-reasoning question remains unresolved: no supplied study fully matches verbal CoT against a non-CoT or nonverbal control across surface format, token count, and inference computation. S34 addresses budget allocation but not this causal isolation, and S31's excerpt is mechanistic and incomplete rather than a direct CoT ablation.

**Next Search**

> arithmetic LLM chain-of-thought causal abstraction matched non-CoT scratchpad token budget answer format intervention

---

# Iteration 9

## 1. Search

**Query**

> arithmetic LLM chain-of-thought causal abstraction matched non-CoT scratchpad token budget answer format intervention

**Why this query**

S33 materially improves the evidence by supplying direct causal-abstraction results, but the central formatting-versus-reasoning question remains unresolved: no supplied study fully matches verbal CoT against a non-CoT or nonverbal control across surface format, token count, and inference computation. S34 addresses budget allocation but not this causal isolation, and S31's excerpt is mechanistic and incomplete rather than a direct CoT ablation.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S35 — Token-Budget-Aware LLM Reasoning**
  URL: https://www.alphaxiv.org/abs/2412.18547
- **S36 — Chain-of-Thought Prompting — Improve Accuracy by Getting LLMs to Reason | Width.ai**
  URL: https://www.width.ai/post/chain-of-thought-prompting
- **S37 — Causal Sufficiency and Necessity Improves Chain-of- ...**
  URL: https://haoxuanli-pku.github.io/papers/NeurIPS%2025%20-%20Causal%20Sufficiency%20and%20Necessity%20Improves%20Chain-of-Thought%20Reasoning.pdf
- **S38 — Token-Budget-Aware LLM Reasoning**
  URL: https://arxiv.org/html/2412.18547v3

**Search Duration:** 3.41s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources do not resolve the central causal question of whether ordinary verbal CoT improves reasoning beyond formatting and extra computation.

**Confidence:** High

**Why this confidence level**

The methods and reported comparisons address CoT efficiency and step selection, not the required verbal-CoT-versus-non-CoT causal ablation.

**Evidence**

- S35/S38 evaluate how token budgets compress an existing CoT process; they do not compare ordinary verbal CoT with a format-matched direct-answer condition holding computation, demonstrations, delimiters, answer placement, and output format constant. [S35] [S38]
- S37 proposes causal sufficiency and necessity measures for selecting, adding, and pruning CoT steps, but evaluates an optimized CoT procedure rather than isolating the causal contribution of natural-language CoT itself. [S37]

#### Finding 2

**Claim**

CoT traces often contain redundant steps, and reducing their length can preserve most accuracy; therefore verbosity is not itself the reasoning mechanism.

**Confidence:** Medium

**Why this confidence level**

Both sources directly study redundancy, but neither matches compressed CoT against a non-CoT control at equal computation or tests robustness and causal faithfulness broadly.

**Evidence**

- S38 reports that a 50-token budget reduced an example from 258 to 86 output tokens while retaining the correct answer, and reports an average 68.64% token reduction with less than a 5% accuracy decrease. [S38]
- S37 categorizes generated steps as sufficient but unnecessary, necessary but insufficient, or both sufficient and necessary, and proposes pruning redundant steps while maintaining or improving accuracy. [S37]

#### Finding 3

**Claim**

Token-budget effects support a role for computation allocation and stopping/readout structure, but do not establish that semantic verbal chain content causes the gain.

**Confidence:** Medium

**Why this confidence level**

The evidence demonstrates budget-sensitive behavior, but it does not distinguish useful intermediate computation from formatting constraints or generic additional serial processing.

**Evidence**

- S38 finds that the specified budget changes actual token use non-monotonically: a stricter 10-token budget can yield more output than a 50-token budget, a phenomenon termed Token Elasticity. [S38]
- S35/S38 report that dynamic budget estimation reduces cost while retaining competitive accuracy, indicating that the amount and allocation of inference-time generation affect outcomes. [S35] [S38]

#### Finding 4

**Claim**

Causal evaluation of CoT steps is a more informative standard than correlation-based prominence or chain length, but the new causal framework remains an optimization method rather than a definitive test of visible-chain faithfulness.

**Confidence:** Medium

**Why this confidence level**

The source explicitly uses interventions and addresses causal relevance, but the retrieved content does not show a direct comparison with latent or nonverbal computation, nor a standard-prompting format-matched baseline.

**Evidence**

- S37 argues that attention weights, likelihood scores, and simple ablations can mistake frequent or prominent steps for causally important ones; its Probability of Necessity and Sufficiency framework uses interventions to identify steps that affect outcomes. [S37]
- S37 reports improved efficiency and maintained or improved accuracy after constructing causally sufficient and necessary traces across mathematical and commonsense benchmarks. [S37]

#### Finding 5

**Claim**

The accumulated three-way hybrid account remains best supported: CoT effects can involve task-relevant intermediate computation, generic extra serial computation, and surface schemas or answer-readout conventions, with their relative contributions varying by task and model.

**Confidence:** High

**Why this confidence level**

The new evidence is consistent with and modestly sharpens the prior synthesis: some intermediate steps matter, many are redundant, and token allocation matters, but no result isolates ordinary verbal CoT from computation and formatting.

**Evidence**

- S37 shows that some steps can be causally necessary or sufficient while others are redundant, supporting a role for semantically meaningful intermediate structure without implying that every generated token matters. [S37]
- S35/S38 show that large portions of CoT can be compressed with limited accuracy loss, supporting the importance of compute allocation and rejecting raw verbosity as essential. [S35] [S38]
- Earlier intervention, mediation, latent-reasoning, formatting, and answer-placement findings identify independent roles for hidden computation, visible traces, and readout conventions. [S6] [S13] [S18] [S23] [S25] [S33]

### Conflicts Found

- S35/S38 present CoT as an effective reasoning process whose token use can be compressed, while the accumulated evidence shows that visible chains can be unfaithful, unnecessary, or dominated by answer-readout effects. These claims are conditionally compatible: CoT may improve benchmark accuracy while containing redundant or non-causal explanatory text. [S35] [S38] [S6] [S13] [S23]
- S37 frames causal step selection as improving CoT reasoning, whereas prior sources show that latent or structured representations can work without ordinary verbal chains. S37 establishes causal relevance for selected intermediate steps within its procedure, not the necessity of natural-language wording. [S37] [S16] [S18] [S33]
- S35/S38 report substantial compression with little accuracy loss, whereas S15 reports benefits from extended reasoning budgets. The likely distinction is between redundant verbal verbosity and useful additional computation or appropriately structured thinking/solution phases; the sources do not determine how much each contributes. [S35] [S38] [S15]

### Important Gaps

- Does ordinary verbal CoT retain a positive accuracy effect after matching total generated tokens, inference-time compute, delimiters, demonstrations, answer placement, and output format against a direct-answer control?
- How much of the benefit of S37's selected steps comes from their semantic content, versus the extra rollout computation and improved demonstrations or fine-tuning data?
- Do causally sufficient-and-necessary traces improve out-of-distribution reasoning and faithfulness, rather than mainly benchmark accuracy and token efficiency?
- Are token-budget compression results replicated across larger model families, free-response tasks, distribution shifts, and settings without post-training or specialized reasoning behavior?
- Can a single experiment independently manipulate visible verbal content, latent intermediate states, total serial computation, and terminal-answer formatting?

**Analysis Duration:** 16.29s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources improve understanding of redundancy, budget allocation, and causal step selection but leave the central format-matched causal comparison unanswered. A focused search for a primary controlled ablation could materially improve the answer.

**Next Search**

> primary controlled experiment verbal chain-of-thought versus direct answer matched inference compute token budget delimiters answer placement format LLM

---

# Iteration 10

## 1. Search

**Query**

> primary controlled experiment verbal chain-of-thought versus direct answer matched inference compute token budget delimiters answer placement format LLM

**Why this query**

The new sources improve understanding of redundancy, budget allocation, and causal step selection but leave the central format-matched causal comparison unanswered. A focused search for a primary controlled ablation could materially improve the answer.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S39 — Escaping the chain-of-thought trap: What is next for LLM ...**
  URL: https://bdtechtalks.substack.com/p/escaping-the-chain-of-thought-trap
- **S40 — Quantum combinatorial reasoning for large language models**
  URL: http://link.aps.org/doi/10.1103/kk5d-tb9b
- **S41 — Self-Training Elicits Concise Reasoning in Large ...**
  URL: https://aclanthology.org/2025.findings-acl.1289.pdf
- **S42 — Why LLMs should stop thinking out loud (and what comes ...**
  URL: https://bdtechtalks.com/2026/06/15/llm-chain-of-thought-limitations

**Search Duration:** 4.26s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

New primary evidence supports the view that ordinary CoT often contains redundant verbal material: reducing chain length can preserve accuracy while lowering inference cost, especially on GSM8K and MATH.

**Confidence:** High

**Why this confidence level**

S41 is a primary ACL 2025 paper with experiments across multiple model families and two reasoning benchmarks. However, it studies fine-tuned concise reasoning, not a fully matched verbal-CoT versus non-CoT causal ablation.

**Evidence**

- S41 reports a self-training method that reduces output tokens by about 30% on average across five model families while maintaining average accuracy, and argues that default reasoning traces contain repetitive or verbose tokens. [S41]

#### Finding 2

**Claim**

S41 treats CoT’s benefit as involving additional inference-time computation, but its results imply that raw verbosity is not essential; models can retain useful computation with shorter traces.

**Confidence:** Medium

**Why this confidence level**

The paper directly measures token reduction and accuracy preservation, but does not separate semantic intermediate computation from formatting, learned task schemas, or generic serial computation.

**Evidence**

- S41 describes each intermediate token as enabling another forward pass, while showing that carefully selected shorter reasoning paths preserve accuracy and adapt their length to problem difficulty. [S41]

#### Finding 3

**Claim**

The new evidence reinforces task- and model-dependence rather than establishing a universal CoT effect.

**Confidence:** High

**Why this confidence level**

The new multi-model evidence is consistent with several prior task-dependent findings, although it does not constitute a broad meta-analysis.

**Evidence**

- S41 reports results across five model families and GSM8K/MATH, with adaptive length behavior across problem difficulty and additional tests in business, chemistry, and physics domains. [S41]
- S18, S13, and S8 previously found that intermediate reasoning helps more reliably on difficult decomposable tasks and can be neutral or harmful on simpler, commonsense, or already-reasoning systems. [S18] [S13] [S8]

#### Finding 4

**Claim**

S39’s claim that CoT is ‘largely an illusion’ is too strong for the supplied evidence; the defensible conclusion is that visible verbal chains are neither necessary nor sufficient for reasoning, and may combine useful computation with formatting and rationalization effects.

**Confidence:** High

**Why this confidence level**

The synthesis is supported by multiple primary or research-oriented sources. S39 itself is a commentary and should carry less weight than the intervention and causal-abstraction studies.

**Evidence**

- S39 argues that models can produce correct answers with flawed chains, that CoT can be brittle under distribution shift, and that latent-space alternatives may be more efficient. [S39]
- S33 finds that some models causally use intermediate CoT tokens in arithmetic, while S23, S6, and S13 find frequent unfaithfulness, answer-readout effects, or answer stability under chain interventions. [S33] [S23] [S6] [S13]
- S16 and S18 show that abstract or latent intermediate representations can preserve or improve performance without ordinary natural-language rationales. [S16] [S18]

#### Finding 5

**Claim**

S40 provides no material evidence about the formatting-versus-reasoning fault line.

**Confidence:** Low

**Why this confidence level**

The source excerpt is too sparse to assess methodology or relevance beyond a high-level comparison with CoT aggregation.

**Evidence**

- S40 only states that a quantum-combinatorial method outperforms standard CoT aggregation at matched sampling budget; the retrieved content gives no controlled analysis of verbal chain content, latent computation, or output formatting. [S40]

### Conflicts Found

- S41 shows that much CoT text can be removed without accuracy loss, whereas S15 and related work report benefits from extended reasoning budgets. This is a conditional rather than direct contradiction: redundant verbal exposition may be removable while useful serial computation or structured intermediate steps remain valuable. [S41] [S15]
- S39 presents CoT as largely an illusion and latent reasoning as the future, while S33 reports causal use of intermediate verbal tokens in at least some arithmetic cases. The stronger claim that visible CoT is generally non-causal is not established by the new sources. [S39] [S33]
- S39 describes CoT as broadly brittle and potentially accuracy-reducing under distribution shift, whereas S41 reports preserved benchmark accuracy after concise-reasoning fine-tuning. These results concern different regimes: distributional robustness versus in-distribution efficiency and accuracy. [S39] [S41]
- S40 reports an advantage over CoT aggregation at matched sampling budget, but this does not conflict directly with positive CoT results because aggregation, sampling budget, and the causal contribution of individual chains are distinct treatments. [S40]

### Important Gaps

- Does ordinary prompted verbal CoT improve accuracy after matching total generated tokens, inference-time computation, delimiters, demonstrations, answer placement, and output format against a direct-answer or nonverbal-scratchpad control?
- What fraction of the gains preserved by S41’s concise traces comes from semantic intermediate content versus generic serial computation and task-specific fine-tuning?
- Do concise chains preserve robustness, calibration, error detection, and out-of-distribution generalization, rather than only benchmark accuracy?
- Can the causal-use findings in S33 be replicated across model scales, domains, and free-response tasks?
- Do latent or abstract representations outperform verbal CoT under matched compute and matched training exposure?

**Analysis Duration:** 14.99s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The runner reached the maximum research iteration budget. Analyzer assessment: The new primary paper materially strengthens the evidence that verbosity is not essential, but it does not close the central causal gap: no supplied source isolates natural-language CoT from extra computation, learned schemas, and answer-readout formatting in ordinary prompting.

**Stop Reason:** max_iterations

---

# Final Research Decision

**Research Stopped Because**

The runner reached the maximum research iteration budget.

**Stop Reason:** max_iterations

**Searches Performed:** 10

**Unique Sources:** 42

**Remaining Uncertainty**

- No supplied study directly compares ordinary verbal CoT with a direct-answer or nonverbal-scratchpad control while simultaneously matching total generated tokens, inference-time compute, demonstrations, delimiters, answer placement, and output format.
- The proportion of classic CoT gains attributable to semantic intermediate content, generic serial computation, learned task schemas, and terminal-answer/readout conventions remains unknown.
- It is unclear whether structured, executable, concise, or latent methods improve out-of-distribution reasoning and calibration, rather than primarily benchmark accuracy and efficiency.
- The generality of causal-abstraction and mediation findings across model scales, free-response tasks, domains, open versus closed models, and frontier systems remains unresolved.
- It remains uncertain whether latent reasoning findings from specialized post-trained models transfer to ordinary pretrained or instruction-tuned models using prompted verbal CoT.
- Because research stopped at the iteration limit, these questions were not resolved by the accumulated search.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 10 | 40.17s |
| OpenAI Analysis | 10 | 176.29s |
| Report Generation | 1 | 24.43s |
| Total Run | — | 240.90s |
