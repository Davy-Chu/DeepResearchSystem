# Chain-of-Thought Prompting: Reasoning Strategy or Output Formatting?

## Executive conclusion

Chain-of-thought (CoT) prompting is neither merely a formatting trick nor a uniformly reliable reasoning mechanism.

The strongest interpretation of the literature is:

1. **CoT is an effective inference-time computation strategy for many sufficiently capable language models**, especially on multistep arithmetic, symbolic, commonsense, and compositional tasks.
2. **Its benefits are highly conditional.** They depend on model scale, task structure, prompt quality, decoding method, answer-verification difficulty, and whether the task actually requires intermediate computation.
3. **A written rationale is not necessarily the model’s true causal reasoning process.** Models can produce persuasive explanations after arriving at an answer, follow misleading rationales, or exploit superficial regularities.
4. **Some reported gains are indeed due to output organization, answer-format regularization, or improved search—not “reasoning” in the strong sense.**
5. The disagreement largely arises because different studies use “reasoning” to mean different things: higher accuracy, more computation, faithful causal explanation, or generalizable problem-solving.

Thus, the most defensible claim is:

> CoT often improves problem-solving by inducing additional structured computation and intermediate-state generation, but the resulting text should not automatically be interpreted as a faithful transcript of the computation that produced the answer.

---

## 1. What counts as chain-of-thought?

The term covers several related interventions:

- **Few-shot CoT prompting:** demonstrations include intermediate reasoning, e.g. “Let’s think step by step.”
- **Zero-shot CoT:** a trigger such as “Let’s think step by step” is appended to a question.
- **Scratchpads:** intermediate calculations are generated before the final answer, often in program-like or symbolic form.
- **Self-consistency:** sample multiple reasoning traces and choose the most common final answer.
- **Tree or graph search:** generate and evaluate multiple partial reasoning paths.
- **Process supervision:** train or score intermediate steps rather than only final answers.
- **Externalized reasoning:** use tools, code, retrieval, or an explicit workspace.

These are not equivalent. A result showing that “self-consistency plus CoT” improves accuracy does not establish that a single textual rationale is faithful or that CoT alone caused the improvement.

A useful decomposition is:

\[
\text{Observed gain}
=
\text{additional computation}
+
\text{search}
+
\text{formatting/scaffolding}
+
\text{answer filtering}
+
\text{possible genuine reasoning}
\]

Most experiments do not isolate all of these components.

---

## 2. Evidence that CoT improves reasoning performance

### 2.1 The original scaling result

Wei et al. (2022), “Chain-of-Thought Prompting Elicits Reasoning in Large Language Models,” reported large gains on arithmetic, commonsense, and symbolic reasoning benchmarks when large models were shown worked-out examples.

Their central finding was not simply that longer answers look better. It was that:

- CoT had little or negative effect in smaller models.
- Benefits appeared sharply at larger scales.
- The gains were especially large on tasks involving multiple intermediate steps.
- CoT sometimes produced qualitatively new capabilities absent under direct-answer prompting.

This scale dependence is difficult to explain as mere formatting alone. If changing the requested format were the whole story, one would expect comparable effects across model sizes. Instead, CoT often acts as a **capability elicitation mechanism**: the model may possess relevant procedural knowledge but fail to deploy it under a one-shot answer format.

However, scale dependence does not prove human-like reasoning. Larger models are also better at imitating the style of worked solutions, recognizing benchmark patterns, and maintaining long structured outputs.

### 2.2 Zero-shot CoT

Kojima et al. (2022), “Large Language Models are Zero-Shot Reasoners,” showed that appending “Let’s think step by step” improved performance on several reasoning datasets without task-specific demonstrations.

This result supports the view that a simple linguistic cue can alter the model’s inference trajectory. But it also introduces an important caveat: the cue may function as a **distributional instruction**. It tells the model to produce the kind of text associated with successful solutions. That may induce useful internal computation, but it may also mainly activate a learned answer template.

### 2.3 Scratchpads and intermediate computation

Nye et al. (2021), “Show Your Work: Scratchpads for Intermediate Computation with Language Models,” found that allowing models to write intermediate steps can substantially improve algorithmic tasks.

Scratchpad settings are especially important because they more clearly separate:

- producing a final answer in one pass, from
- generating intermediate states that can be used in subsequent prediction.

For algorithmic tasks, a scratchpad can function like an external memory or working space. The model’s next token is conditioned on its own previous intermediate outputs, increasing effective computational depth.

This is stronger evidence for CoT as computation than for CoT as explanation. A scratchpad need not be faithful to an internal mental process; it can still be causally useful because the generated symbols provide state that the model can read back.

### 2.4 Self-consistency

Wang et al. (2022), “Self-Consistency Improves Chain of Thought Reasoning in Language Models,” sampled multiple CoT solutions and selected the most frequent answer.

This often improves performance substantially, particularly on arithmetic and symbolic tasks. But it complicates the interpretation:

- The gain may result from **search over multiple candidate solutions**.
- Majority voting can suppress idiosyncratic mistakes.
- The model need not have a single correct reasoning trace.
- Accuracy can improve even when individual rationales are unreliable.

Self-consistency therefore demonstrates that CoT can create a useful search space, but it does not by itself show that the text is a faithful explanation.

### 2.5 Training with rationales

Several training approaches provide stronger evidence that intermediate steps can be computationally useful:

- **STaR** (Zelikman et al., 2022): generate rationales, retain those leading to correct answers, and fine-tune on them.
- **Verifier-based approaches** (Cobbe et al., 2021): train models to judge solutions, improving mathematical problem-solving.
- **Process supervision** (Lightman et al., 2023): supervise individual steps rather than only final answers.
- **Program-aided reasoning** and tool use: translate parts of reasoning into executable code or formal operations.

These results suggest that intermediate representations can be useful targets for learning and verification. They also reveal that not all rationales are equally valuable: correct final answers can be accompanied by bad steps, while a seemingly imperfect rationale may still lead to a correct result.

---

## 3. Evidence that CoT can be “formatting,” post-hoc explanation, or unreliable reasoning

### 3.1 Rationales are often unfaithful

Turpin et al. (2023), “Language Models Don’t Always Say What They Think,” showed that models can give explanations that do not reflect the actual basis of their answers. When irrelevant biases were introduced into prompts, models often used those biases while producing rationales that ignored or denied them.

The implication is not that CoT never causes computation. It is that:

> The visible chain of thought is not guaranteed to be the causal chain of thought.

A model may:

1. compute or recognize an answer using latent representations,
2. generate a plausible justification afterward, or
3. use a mixture of genuine intermediate computation and post-hoc rationalization.

### 3.2 Models can follow incorrect rationales

Studies including Lanham et al. (2023), “Measuring Faithfulness in Chain-of-Thought Reasoning,” tested whether models’ answers actually depended on their stated intermediate steps. They found substantial failures of faithfulness:

- Models sometimes reached the same answer when rationales were removed or altered.
- They sometimes accepted misleading intermediate steps.
- They could produce different explanations without changing the answer.
- Their final predictions were not always causally sensitive to the rationale.

This weakens the claim that a natural-language rationale is an interpretable execution trace.

### 3.3 CoT can increase verbosity without improving competence

On tasks that are simple, ambiguous, adversarial, or outside the model’s knowledge, CoT can:

- create more opportunities for arithmetic or logical errors,
- encourage confident elaboration,
- produce plausible but unsupported intermediate claims,
- obscure a wrong answer behind a long explanation.

In such settings, direct answers may be as accurate or more accurate. CoT is not a general-purpose guarantee of improved reasoning.

### 3.4 Formatting and answer extraction matter

Many benchmark protocols require the model to produce a final answer in a particular format. CoT can help by separating reasoning from the answer:

```text
Reasoning: ...
Answer: C
```

This may improve exact-match scoring because the final answer becomes more salient and standardized. Conversely, a model may solve the problem correctly but lose credit because it mixes explanation with the required answer format.

Some apparent CoT improvements can therefore arise from:

- better compliance with answer-format instructions,
- reducing premature answer emission,
- making the final answer easier to extract,
- generating text that resembles benchmark demonstrations.

These effects are real and useful, but they are not necessarily reasoning in the cognitive or algorithmic sense.

---

## 4. The central fault lines in the literature

### Fault line 1: Accuracy versus faithful explanation

Two questions are often conflated:

1. **Does CoT improve the answer?**
2. **Does the rationale faithfully explain how the answer was obtained?**

The answer to the first is often yes under appropriate conditions. The answer to the second is often no or only partially.

A calculator can improve arithmetic accuracy without explaining its internal operations. Similarly, a scratchpad can causally improve prediction without being a transparent record of the model’s internal computation.

### Fault line 2: Elicitation versus creation

CoT may expose reasoning ability already present in the model rather than create a new capability.

Evidence for elicitation:

- large models often benefit sharply from CoT;
- small models often do not;
- few-shot examples can unlock performance without parameter updates.

But CoT can also provide genuinely useful computation by:

- extending the number of sequential prediction steps,
- supplying external memory,
- decomposing a difficult problem,
- enabling sampling and verification.

The best interpretation is usually **elicitation plus computation**, not one or the other.

### Fault line 3: Natural-language reasoning versus symbolic execution

CoT is most convincing when intermediate steps are:

- explicit,
- checkable,
- compositional,
- causally necessary,
- connected to an executable operation.

Arithmetic scratchpads, code generation, formal proofs, and tool calls offer stronger evidence than free-form prose. Natural-language chains are ambiguous because they can simultaneously serve as reasoning, communication, imitation, and rationalization.

### Fault line 4: Single-sample CoT versus search

A single chain may fail, while self-consistency or tree search succeeds. If the improvement comes mainly from sampling multiple paths, then the active ingredient may be **inference-time search**, with CoT serving as the representation in which search occurs.

This distinction matters operationally:

- “CoT improves reasoning” may mean one chain is better.
- It may instead mean many chains plus majority voting are better.
- Those have different cost, reliability, and interpretability properties.

### Fault line 5: Benchmark reasoning versus real-world reasoning

CoT gains are strongest on tasks with:

- a known answer,
- short or moderate solution paths,
- regular structure,
- objective verification,
- limited ambiguity.

Real-world reasoning often requires:

- identifying the relevant facts,
- deciding what information is missing,
- managing uncertainty,
- selecting tools,
- pursuing long-horizon plans,
- detecting when the problem is ill-posed.

CoT alone does not solve these problems. Retrieval, tools, planning, verification, and interaction are often more important.

### Fault line 6: Model scale and training distribution

CoT is highly sensitive to:

- parameter count,
- instruction tuning,
- pretraining exposure to worked solutions,
- context length,
- decoding temperature,
- prompt wording,
- language and domain.

Large instruction-tuned models may have learned extensive associations between “step by step” language and successful solutions. Smaller models may lack the underlying competence and merely produce longer errors.

### Fault line 7: Dataset artifacts and contamination

Some benchmark gains may be inflated by:

- training-set overlap,
- memorized solution patterns,
- repeated templates,
- answer-position biases,
- synthetic task regularities,
- leakage through few-shot examples.

A model can appear to reason when it is recognizing a familiar schema. CoT makes this harder to diagnose because a plausible rationale can be generated for either a memorized or genuinely constructed answer.

---

## 5. What mechanisms plausibly explain CoT gains?

### 5.1 Increased effective computation

Autoregressive models ordinarily have only one opportunity to map a question directly to an answer. CoT gives them many sequential prediction steps. Each generated token can act as an intermediate computational state.

This resembles recurrent computation:

\[
h_{t+1}=f(h_t, \text{generated intermediate token}_t)
\]

Even if the model’s internal hidden states are opaque, the generated scratchpad extends the computation through the context window.

### 5.2 Decomposition

CoT encourages the model to turn a difficult mapping into a sequence of easier mappings:

\[
x \rightarrow z_1 \rightarrow z_2 \rightarrow \cdots \rightarrow y
\]

This is especially effective when the task naturally decomposes into subgoals.

### 5.3 External memory

Long intermediate outputs preserve quantities, entities, and partial conclusions that might otherwise be lost or interfered with. This is particularly useful for multi-hop tasks and arithmetic.

### 5.4 Search and error averaging

Multiple chains allow the model to explore alternatives. If errors are partly independent, majority voting can improve accuracy.

### 5.5 Instructional and distributional alignment

Worked examples teach the model:

- what counts as a relevant step,
- how much detail to provide,
- where to place the final answer,
- which operations are expected.

Some of the benefit is therefore pedagogical formatting, even when the final result improves.

### 5.6 Self-conditioning

Once a model writes an intermediate statement, it conditions on that statement in later steps. This can stabilize a solution, but it can also lock in an early mistake. CoT is therefore both a memory aid and an error-propagation channel.

---

## 6. Why CoT sometimes hurts

CoT is not monotonic with answer quality.

### Error accumulation

Each intermediate step is another opportunity for an incorrect assertion. Long chains can amplify early mistakes.

### Unsupported decomposition

The model may invent subproblems or assumptions not warranted by the prompt.

### Premature commitment

Once an incorrect intermediate result is written, later steps often rationalize it rather than revise it.

### Distractor susceptibility

Models can be induced to follow irrelevant or malicious reasoning steps. This is relevant to prompt injection and adversarial examples.

### Overthinking

For simple questions, additional generation introduces noise and latency without adding useful computation.

### False confidence

A detailed explanation can make incorrect answers appear more credible to users and evaluators.

---

## 7. How to test whether CoT is doing real reasoning

A rigorous evaluation should go beyond final accuracy.

### 7.1 Causal intervention on intermediate steps

Modify, remove, or replace a stated step and measure whether the final answer changes appropriately.

A faithful chain should satisfy something like:

- changing a crucial step changes the answer;
- changing an irrelevant stylistic phrase does not;
- replacing a correct step with an incorrect one causes an appropriate downstream error.

This is the logic behind faithfulness tests such as those discussed by Lanham et al.

### 7.2 Process correctness

Score each intermediate step, not only the final answer. This distinguishes:

- correct answer with correct reasoning,
- correct answer with faulty reasoning,
- incorrect answer with partially correct reasoning.

Process supervision research suggests this can improve reliability, but step-level labels are costly and may themselves encode evaluator assumptions.

### 7.3 Counterfactual and compositional generalization

Use novel combinations of familiar operations, changed superficial details, and longer instances. Memorization and formatting strategies tend to degrade under these tests.

### 7.4 Controlled scratchpad comparisons

Compare:

- direct answer,
- free-form CoT,
- meaningless tokens of equal length,
- structured variables,
- code execution,
- rationale shown only to the evaluator,
- rationale fed back to the model.

This helps separate length, formatting, and actual intermediate computation.

### 7.5 Calibration and abstention

A reasoning method should improve not only accuracy but also uncertainty estimation and willingness to say “insufficient information.” CoT often improves neither automatically.

### 7.6 Robustness to misleading demonstrations

Provide demonstrations with incorrect rationales but correct answers, or correct rationales with incorrect answers. This tests whether the model follows the reasoning, the answer pattern, or superficial correlations.

---

## 8. Practical implications

### Use CoT when:

- the task has genuine multistep structure;
- intermediate states are useful or checkable;
- the model is sufficiently capable;
- latency and token cost are acceptable;
- multiple samples or verification are available;
- the output can be parsed separately from the rationale.

### Prefer direct answers when:

- the task is simple fact retrieval;
- the answer must be concise;
- the problem is ambiguous and extra prose may create unsupported assumptions;
- the model lacks the competence to execute the required steps;
- long explanations would increase attack surface or error risk.

### Prefer structured or executable reasoning when reliability matters:

- calculators for arithmetic;
- code for deterministic transformations;
- formal solvers for logic;
- retrieval for factual grounding;
- verifiers for candidate solutions;
- process supervision for high-stakes domains.

A useful production pattern is:

1. generate a structured solution or tool call;
2. independently verify it;
3. return a concise answer;
4. expose a rationale only when needed and label it as an explanation, not necessarily a faithful internal trace.

---

## 9. Overall assessment

The literature does not support either extreme:

### Too strong

> “CoT reveals the model’s actual reasoning and reliably produces faithful explanations.”

This is false. Rationales can be post-hoc, strategically generated, incomplete, or causally irrelevant.

### Too weak

> “CoT is only formatting and never improves reasoning.”

This is also false. CoT, scratchpads, self-consistency, and process-based methods can materially improve performance, often in ways consistent with increased computation, decomposition, memory, and search.

The more accurate position is:

> Chain-of-thought is an inference-time interface that can induce useful intermediate computation. Its visible text is a computational artifact and communication layer, not a guaranteed transcript of internal cognition.

The conflicting results largely disappear once four dimensions are separated:

1. **Outcome:** Does accuracy improve?
2. **Mechanism:** Is the gain from computation, search, formatting, or memorization?
3. **Faithfulness:** Does the rationale causally determine the answer?
4. **Generalization:** Does the method transfer beyond familiar benchmark structures?

CoT scores well on the first dimension in many settings, plausibly contributes on the second, is unreliable on the third, and remains highly task-dependent on the fourth.

---

## Selected literature

- Nye, M. et al. (2021). **Show Your Work: Scratchpads for Intermediate Computation with Language Models.**
- Cobbe, K. et al. (2021). **Training Verifiers to Solve Math Word Problems.**
- Wei, J. et al. (2022). **Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.**
- Kojima, T. et al. (2022). **Large Language Models are Zero-Shot Reasoners.**
- Wang, X. et al. (2022). **Self-Consistency Improves Chain of Thought Reasoning in Language Models.**
- Zelikman, E. et al. (2022). **STaR: Bootstrapping Reasoning With Reasoning.**
- Yao, S. et al. (2023). **ReAct: Synergizing Reasoning and Acting in Language Models.**
- Turpin, M. et al. (2023). **Language Models Don’t Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting.**
- Lanham, T. et al. (2023). **Measuring Faithfulness in Chain-of-Thought Reasoning.**
- Lightman, H. et al. (2023). **Let’s Verify Step by Step.**
- Huang, J. and Chang, K. (2023). **Towards Reasoning in Large Language Models: A Survey.**
- OpenAI (2023–2024). Work on process supervision, verifiers, and reasoning models, which further distinguishes final-answer optimization from step-level reliability.