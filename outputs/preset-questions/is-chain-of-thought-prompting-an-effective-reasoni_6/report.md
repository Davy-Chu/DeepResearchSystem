# Is chain-of-thought prompting reasoning—or mostly formatting?

## Executive conclusion

Chain-of-thought (CoT) prompting is **not merely a formatting trick**, but neither is it a general-purpose reasoning algorithm. The best-supported conclusion is:

> **CoT can substantially improve task performance when the model already contains the relevant knowledge and computational competence, and when the task benefits from decomposing a problem into manageable intermediate steps. However, much of the observed gain can come from improved problem representation, search, and answer selection—not from the written chain being a faithful record of the computation that produced the answer.**

The literature appears contradictory because studies often use different meanings of “reasoning” and different experimental controls:

1. **Accuracy:** Does the final answer improve?
2. **Computation:** Does the model perform additional useful intermediate operations?
3. **Faithfulness:** Do the stated steps causally explain the answer?
4. **Generalization:** Does the method solve genuinely novel compositions rather than familiar templates?
5. **Calibration and reliability:** Does it reduce errors, or merely make answers look more justified?

CoT performs well on the first question under favorable conditions. Its evidence is weaker—and sometimes negative—on the others.

The central fault line is therefore not “reasoning versus formatting.” It is:

> **CoT is often an effective external control interface for eliciting, organizing, and selecting computations that the model can already perform, while the visible explanation may be only partially related to the computation actually used.**

---

## 1. What counts as chain-of-thought?

The term covers several distinct interventions that should not be conflated.

### 1.1 Few-shot CoT

A prompt provides solved examples with intermediate reasoning:

> Question → reasoning steps → answer

This was popularized by **Wei et al. (2022)**, who reported large gains on arithmetic, symbolic, and commonsense reasoning tasks, especially for sufficiently large language models.

### 1.2 Zero-shot CoT

A simple instruction such as:

> “Let’s think step by step.”

was shown by **Kojima et al. (2022)** to improve performance on several reasoning benchmarks without demonstrations.

### 1.3 Scratchpads

A scratchpad is an intermediate token sequence used to solve a problem, often in supervised or reinforcement-learning settings. **Nye et al. (2021)** showed that training models to produce intermediate computations could improve algorithmic tasks.

### 1.4 Self-consistency

**Wang et al. (2022)** sampled multiple CoT solutions and selected the most common final answer. This often improves accuracy, but the gain may arise from **search and aggregation**, not from the truth of any individual chain.

### 1.5 Program-of-thought and tool-augmented reasoning

Methods such as **Program-of-Thoughts** generate executable code rather than natural-language explanations. These often outperform ordinary CoT on numerical tasks because execution handles arithmetic and state updates more reliably.

### 1.6 Hidden or latent reasoning

More recent work distinguishes producing visible reasoning from performing internal intermediate computation. A model may reason using hidden states, latent tokens, or internal deliberation without exposing a textual chain. This is important because a visible explanation is not automatically a causal trace.

---

# 2. The strongest evidence that CoT does real computational work

## 2.1 It improves performance specifically on compositional and multistep tasks

The original CoT results were not simply gains in prose quality. On arithmetic word problems, symbolic manipulation, and logical tasks, intermediate steps can break a difficult transformation into smaller ones.

For example, a model may fail to calculate:

\[
37 \times 24
\]

in one leap but succeed when prompted to decompose it into:

\[
37 \times 20 + 37 \times 4 = 740 + 148 = 888.
\]

This is evidence for a **serial-computation benefit**: the model’s next-token prediction process can represent intermediate states that would be difficult to encode directly in one answer.

The effect is especially visible when:

- the task requires several dependent operations;
- each step is relatively easy;
- the problem is represented in a way familiar from training;
- the model is large enough to sustain coherent intermediate states;
- the answer space is not so broad that sampling becomes unstable.

Wei et al. reported a striking example: PaLM’s performance on the GSM8K grade-school math benchmark rose dramatically with CoT prompting. Subsequent work found similar patterns across arithmetic, symbolic reasoning, and some commonsense benchmarks.

## 2.2 Intermediate tokens provide additional computational bandwidth

A language model predicts one token at a time. Requiring a chain gives it more opportunities to transform and store information in the sequence.

This is related to the “scratchpad” idea in program synthesis and neural computation. Intermediate text can function as:

- external memory;
- a decomposition scaffold;
- a representation of variables and subgoals;
- a way to reduce the effective depth of a computation;
- a partial search trace.

This does not imply that the model executes formal symbolic algorithms. It means that **additional autoregressive steps can make some computations easier**.

Research by **Nye et al. (2021)** and later work on algorithmic reasoning supports this interpretation: models trained or prompted to write intermediate states often solve tasks they cannot solve when required to emit only the final result.

## 2.3 CoT gains are sometimes robust to paraphrase and answer-format controls

If CoT only improved formatting, then equivalent prompts that preserve the requested format but do not invite intermediate computation should perform similarly. In many studies they do not.

For example, prompts that ask the model to:

- solve step by step;
- write down intermediate calculations;
- decompose the problem;
- produce a scratchpad before the answer;

often outperform prompts that merely request a concise answer.

The gains are also sometimes preserved when the final response is constrained to a short answer after hidden or external reasoning. That suggests the benefit is not reducible to verbosity.

## 2.4 Self-consistency shows that reasoning traces can support search

**Wang et al. (2022)** found that sampling many CoT paths and taking the modal answer can improve results substantially.

This demonstrates at least one useful computational role for CoT:

1. generate multiple candidate derivations;
2. obtain multiple candidate answers;
3. exploit redundancy to suppress some local errors.

But it does **not** establish that the chains are individually faithful. Self-consistency can work even if each chain is a noisy heuristic and the majority answer is correlated with correctness.

## 2.5 CoT can induce useful intermediate representations

In some tasks, the model does not merely produce extra words; it changes the representation of the problem. For instance:

- translating a word problem into equations;
- identifying entities and relations;
- listing constraints;
- decomposing a planning problem into subgoals;
- converting natural language into executable code.

This is especially clear in **program-of-thought** methods such as Gao, Madaan, and colleagues’ work, where generated programs are executed externally. The advantage comes from separating linguistic interpretation from reliable calculation.

That is a stronger case for “reasoning” than ordinary explanatory prose, because the intermediate representation has independently testable consequences.

---

# 3. The strongest evidence that CoT can be mostly superficial

## 3.1 A correct chain does not guarantee correct reasoning

Language models can produce polished, plausible derivations containing invalid arithmetic, unsupported assumptions, or contradictions. The final answer may be correct by chance, from memorization, or because the model selected it before generating the explanation.

This is the **faithfulness problem**:

> Does the explanation reflect the actual causal basis of the answer, or is it a post hoc rationale?

Several lines of work show that textual explanations can be decoupled from model decisions.

### Turpin et al. (2023)

“Language Models Don’t Always Say What They Think” showed that CoT explanations can be influenced by irrelevant prompt features and can fail to reveal the actual basis of an answer. Models may rationalize a decision rather than transparently report the computation that generated it.

### Lanham et al. (2023)

“Measuring Faithfulness in Chain-of-Thought Reasoning” evaluated interventions such as removing or changing steps in a chain. The findings suggested that visible CoT is often not fully causally necessary or faithful, especially in larger models and certain task settings.

### Uesato et al. and related work

Studies of process supervision and verifier-based training found that rewarding step-by-step explanations can improve outcomes, but also that models may exploit superficial patterns or produce plausible-looking incorrect processes.

The key point is:

> **Unfaithful reasoning can still be useful reasoning-like behavior.**

A generated chain may help the model arrive at the answer even if it is not a transparent transcript of the internal computation.

## 3.2 CoT sometimes changes only the answer distribution

A prompt such as “think step by step” can alter:

- which answer options the model favors;
- how much probability it assigns to common response patterns;
- whether it commits immediately or explores alternatives;
- the likelihood of emitting a benchmark-approved format.

Thus, improvements may reflect **better search or answer calibration**, not a new reasoning capacity.

For multiple-choice tasks, the model may generate a chain that cues the expected answer style or activates associations learned during training. In such cases, the chain is functioning as a **prompt-induced latent state**, while the visible prose is incidental.

## 3.3 Models can solve some tasks without coherent chains

On many benchmarks, direct-answer prompting performs nearly as well as CoT. This happens when:

- questions are easy;
- answers are memorized;
- the task is primarily retrieval;
- the benchmark contains familiar templates;
- the problem requires little composition;
- answer options provide strong cues.

Conversely, CoT can harm performance by inducing unnecessary steps, arithmetic mistakes, or overthinking. This is common on simple factual tasks and sometimes on adversarial or ambiguous questions.

That pattern is inconsistent with CoT being a universally beneficial reasoning mechanism.

## 3.4 CoT is vulnerable to shortcuts and spurious correlations

A model may appear to reason while exploiting:

- lexical cues;
- answer-position biases;
- surface templates;
- known benchmark formats;
- demonstrations that accidentally reveal the solution structure;
- correlations between question wording and labels.

Work on **shortcut learning**, **adversarial examples**, and **counterfactual evaluation** shows that many CoT gains disappear when superficial regularities are controlled.

For example, if a benchmark’s questions have familiar phrasing, a model may reproduce a learned reasoning template without performing the intended abstract operation. Perturbing names, ordering, irrelevant details, or answer labels can reveal this.

## 3.5 CoT does not reliably solve out-of-distribution compositional reasoning

The most dramatic CoT results often come from benchmark tasks close to patterns represented in pretraining or demonstrations. On novel combinations of rules, systematic generalization, or distribution shifts, gains are less consistent.

This is a major fault line:

- **In-distribution multistep competence:** CoT often helps.
- **Out-of-distribution systematic reasoning:** CoT is much less reliable.

A model may know many instances of a task and use CoT to interpolate among them without acquiring a general algorithm.

---

# 4. Why the literature disagrees

## 4.1 Researchers measure different things under the same label

A paper may call a method successful if it increases exact-match accuracy. Another may ask whether the chain is causally faithful. These are not equivalent.

A model can:

- improve accuracy with CoT;
- use the chain as a useful scratchpad;
- generate explanations that are not faithful;
- fail on novel problems.

All four statements can be true simultaneously.

## 4.2 Model scale is a major moderator

The original CoT effect was strongly associated with model scale. Smaller models often cannot maintain coherent multistep reasoning and may produce rambling or invalid chains. Larger models can use the extra tokens more effectively.

This creates conflicting results when studies use different:

- parameter counts;
- pretraining corpora;
- instruction tuning;
- context lengths;
- decoding methods;
- numbers of demonstrations.

CoT is best understood as a **capability elicitation technique**. If the underlying model lacks the required competence, prompting cannot reliably manufacture it.

## 4.3 Task type matters more than the word “reasoning”

CoT is not equally effective across domains.

### Arithmetic and symbolic tasks

Often strong gains, especially when the problem decomposes naturally. But exact arithmetic remains fragile; generated code or external calculators are usually better.

### Commonsense reasoning

Results are mixed. Some tasks benefit from elaboration, but many can be solved through retrieval and social-script matching.

### Knowledge-intensive questions

CoT may increase confident hallucination. More explanation does not supply missing facts.

### Planning and search

CoT can help by enumerating subgoals, but unconstrained natural-language planning is error-prone. Tree search, verifiers, tools, or execution improve reliability.

### Logic and constraint satisfaction

CoT helps when the model can represent constraints, but it may lose track of them over long chains.

### Multiple-choice benchmarks

Gains may partly result from answer selection, option elimination, or benchmark artifacts rather than general reasoning.

## 4.4 Prompt wording and demonstrations are not neutral

Small changes can produce large differences:

- “Let’s think step by step”;
- “explain your answer”;
- “show your work”;
- “first derive, then answer”;
- “write a concise proof”;
- “use a calculator”;
- “generate and execute a program.”

Demonstrations also teach more than reasoning style. They reveal:

- what counts as a valid answer;
- how to parse the task;
- which operations are expected;
- which output format is rewarded;
- sometimes the underlying solution strategy.

Thus, “CoT versus no CoT” can be an unfair comparison unless the prompts are matched for information and output constraints.

## 4.5 Decoding and aggregation change the apparent effect

Greedy decoding, temperature sampling, beam search, self-consistency, and answer-verification produce different results.

A useful distinction is:

- **Single-chain CoT:** tests whether one generated trajectory helps.
- **Self-consistency:** tests whether multiple trajectories plus voting help.
- **Verifier-guided search:** tests whether external evaluation helps.
- **Tool use:** tests whether intermediate execution helps.

Many papers attribute gains to “CoT” when the actual intervention includes sampling ten or one hundred solutions and aggregating them. That is a search procedure, not merely a formatting instruction.

## 4.6 Evaluation contamination and benchmark familiarity

LLMs may have encountered benchmark questions, close paraphrases, or solution templates during pretraining or instruction tuning. CoT can make such memorized competence more visible.

This is particularly relevant for:

- GSM8K;
- MATH;
- popular commonsense datasets;
- standardized exams;
- heavily reused prompt formats.

Contamination does not invalidate CoT, but it weakens claims that performance demonstrates novel reasoning.

## 4.7 Exact-match scoring rewards answer production, not process quality

Most CoT benchmarks score only the final answer. A model receives full credit for:

- a correct chain and correct answer;
- a wrong chain and lucky answer;
- a memorized answer with fabricated explanation.

Process-aware metrics are therefore essential:

- step-level correctness;
- consistency under intervention;
- execution validity;
- counterfactual robustness;
- calibration;
- agreement between independent derivations;
- performance on novel compositions.

---

# 5. The key conceptual distinction: useful computation versus faithful explanation

These are often treated as the same, but they are different.

## 5.1 CoT as externalized computation

Under this view, generating intermediate text genuinely helps the model compute. The text acts as a scratchpad or state representation.

Predictions:

- suppressing or shortening intermediate steps should reduce performance;
- independent perturbations of the chain should affect subsequent computation;
- executable or structured intermediate states should outperform decorative explanations;
- longer tasks should benefit when the chain remains coherent.

This is supported by scratchpad and program-of-thought results.

## 5.2 CoT as latent activation steering

The words “let’s think step by step” may activate a learned reasoning mode. The actual useful effect may occur in hidden states, while the visible chain is only a byproduct.

Predictions:

- hidden or compressed reasoning could retain much of the benefit;
- requiring visible explanations may not be necessary;
- explanations could be changed without changing the final answer;
- answer quality could improve even when the chain is incoherent.

This helps explain why CoT can improve accuracy without being faithful.

## 5.3 CoT as search and answer aggregation

With sampling and self-consistency, CoT generates a distribution of candidate solutions. Majority voting can eliminate idiosyncratic mistakes.

Predictions:

- gains increase with the number of samples;
- diversity matters;
- the majority answer can be correct even when no single chain is fully valid;
- a verifier or execution engine may outperform voting.

## 5.4 CoT as format and benchmark compliance

Some gains arise because the model learns how to present an answer in the expected way or how to map a question to a benchmark’s label format.

Predictions:

- gains should disappear under format-matched controls;
- equivalent non-reasoning prompts should perform similarly;
- perturbing answer labels or surface form should expose the shortcut.

In practice, all four mechanisms can operate at once.

---

# 6. What the major research programs imply

## 6.1 Wei et al. (2022): CoT is a powerful elicitation method

The original paper established that CoT can unlock capabilities in large models, especially on multistep reasoning benchmarks. Its main contribution was empirical, not a proof that chains are faithful.

Interpretation: **strong evidence for performance gains under certain conditions; weak evidence about mechanism.**

## 6.2 Kojima et al. (2022): zero-shot prompting can induce reasoning-like behavior

The “Let’s think step by step” result showed that demonstrations are not always necessary.

Interpretation: the prompt may activate an existing learned procedure or useful response mode. It does not show that the model learned a new algorithm at inference time.

## 6.3 Wang et al. (2022): self-consistency adds search

Self-consistency improved CoT by sampling multiple paths.

Interpretation: part of the success attributed to CoT is actually due to **stochastic search plus aggregation**.

## 6.4 Nye et al. (2021): scratchpads support algorithmic computation

Scratchpad supervision showed that intermediate states can improve algorithmic performance.

Interpretation: this is among the stronger arguments that intermediate sequences can be computationally substantive, although trained scratchpads differ from zero-shot natural-language rationales.

## 6.5 Turpin et al. (2023), Lanham et al. (2023), and related faithfulness studies

These works demonstrate that verbalized reasoning is often not a reliable explanation of the internal decision process.

Interpretation: **accuracy improvements and explanation faithfulness must be evaluated separately.**

## 6.6 Process supervision and verifier work

OpenAI’s process-supervision work, including **Lightman et al. (2023)**, found that supervising intermediate steps can improve mathematical reasoning relative to outcome-only supervision.

Interpretation: checking or rewarding processes can improve reliability, but only if the process representation is sufficiently tied to the actual task and not merely stylistic. Process supervision is not identical to ordinary prompting.

## 6.7 Program-of-thought and tool use

Generating executable programs or calling calculators often produces larger and more dependable gains on formal tasks than free-form CoT.

Interpretation: the most effective “reasoning” systems increasingly use CoT as a translation layer into representations that can be verified or executed.

## 6.8 Reversal and symbolic generalization studies

Work on reversal tasks, novel symbol mappings, and compositional generalization finds that LLMs often struggle when familiar surface associations are removed.

Interpretation: CoT can improve local decomposition while failing to provide robust abstract algorithmic generalization.

---

# 7. A better taxonomy of CoT outcomes

| Outcome | What CoT may be doing |
|---|---|
| Higher accuracy on familiar multistep tasks | Eliciting latent competence or providing a scratchpad |
| Better arithmetic decomposition | Serial computation, though still error-prone |
| Better multiple-choice selection | Elimination, calibration, or answer-distribution steering |
| Better results from many sampled chains | Search and consensus |
| Correct final answer with invalid explanation | Post hoc rationalization or noisy computation |
| More verbose but equally inaccurate answers | Formatting without useful computation |
| Better performance with executable programs | Structured reasoning plus external verification |
| Failure on novel symbolic combinations | Lack of systematic generalization |

This taxonomy resolves much of the apparent disagreement.

---

# 8. How to test whether CoT is really reasoning

A convincing study should go beyond final-answer accuracy.

## 8.1 Format-matched controls

Compare:

1. direct answer;
2. verbose but non-reasoning response;
3. CoT;
4. hidden scratchpad;
5. structured decomposition;
6. executable program.

Keep token budget, demonstrations, and answer format as comparable as possible.

## 8.2 Causal intervention on the chain

Generate a chain, then:

- delete a key step;
- replace a number;
- negate an intermediate conclusion;
- reorder steps;
- insert a contradiction;
- ask the model to continue from the modified state.

If the final answer changes appropriately, the chain is more likely to be causally used. If it remains unchanged, the explanation may be decorative.

## 8.3 Counterfactual and adversarial tests

Change:

- names;
- order of facts;
- irrelevant wording;
- answer-option order;
- numerical surface form;
- familiar templates.

A genuine reasoning strategy should preserve the underlying solution while resisting irrelevant cues.

## 8.4 Novel compositional splits

Train or prompt on components separately and test on unseen combinations. This distinguishes:

- interpolation over familiar examples;
- genuine composition of rules.

## 8.5 Independent verification

Use:

- symbolic solvers;
- code execution;
- calculators;
- theorem provers;
- external verifiers;
- step-level human or model judges.

A chain should not receive credit merely for sounding plausible.

## 8.6 Measure calibration and error propagation

CoT can increase confidence and verbosity while preserving or worsening error rates. Studies should report:

- accuracy;
- confidence;
- abstention;
- self-consistency;
- error types;
- chain validity;
- robustness under perturbation.

---

# 9. Practical implications

## When CoT is likely to help

Use it when:

- the task is genuinely multistep;
- intermediate variables or subgoals are useful;
- the model is large and capable;
- the task resembles training or demonstrations;
- a verifier, tool, or execution environment is available;
- multiple sampled solutions can be aggregated.

## When CoT is unlikely to be enough

Do not rely on it alone when:

- facts are missing or uncertain;
- exact arithmetic matters;
- the task requires long constraint tracking;
- the distribution is novel;
- adversarial robustness is important;
- explanations must be auditable;
- hallucination costs are high.

In those cases, use structured representations, retrieval, tools, code execution, external checking, or specialized verifiers.

## The safest interpretation

Treat ordinary natural-language CoT as:

> **a probabilistic elicitation and search strategy, not a guaranteed transparent proof.**

For high-stakes use, separate:

1. the method used to obtain the answer;
2. the explanation shown to the user;
3. the evidence that the explanation is causally faithful;
4. the independent procedure used to verify the answer.

---

# Final assessment

The literature does not support either extreme:

- **“CoT is just formatting”** is too skeptical. Intermediate tokens can provide real computational scaffolding, improve decomposition, enable search, and substantially raise accuracy on appropriate tasks.
- **“CoT reveals the model’s reasoning”** is too strong. Visible chains are often incomplete, post hoc, strategically shaped, or only loosely connected to the actual causal computation.

The most accurate synthesis is:

> **Chain-of-thought is an effective reasoning interface under capability- and task-dependent conditions. Its performance gains arise from a mixture of serial computation, representation change, latent-mode activation, search, and answer-format effects. The visible chain is not reliably a faithful transcript of those processes.**

The real fault line is therefore between **eliciting useful computation** and **demonstrating faithful, generalizable reasoning**. CoT has fairly strong evidence for the former and substantially weaker, mixed evidence for the latter.

## Selected references

- Nye et al. (2021), *Show Your Work: Scratchpads for Intermediate Computation with Language Models*.
- Wei et al. (2022), *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*.
- Kojima et al. (2022), *Large Language Models Are Zero-Shot Reasoners*.
- Wang et al. (2022), *Self-Consistency Improves Chain of Thought Reasoning in Language Models*.
- Gao, Madaan et al. (2022), *PAL: Program-aided Language Models*.
- Turpin et al. (2023), *Language Models Don’t Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting*.
- Lanham et al. (2023), *改? Measuring Faithfulness in Chain-of-Thought Reasoning*.
- Lightman et al. (2023), *Let’s Verify Step by Step*.
- Zhou et al. (2023), *Least-to-Most Prompting Enables Complex Reasoning in Large Language Models*.
- Yao et al. (2023), *Tree of Thoughts: Deliberate Problem Solving with Large Language Models*.
- Dziri et al. (2023), work on the limits of compositional reasoning and hallucinated chains in language models.