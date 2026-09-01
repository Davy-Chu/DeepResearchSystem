# Research Report

## Research Question

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? What explains the conflicting findings in the literature?

## Summary

The evidence supports a conditional answer. Chain-of-thought (CoT) prompting is not merely a formatting trick: on many compositional, arithmetic, symbolic, and multi-step tasks, requiring intermediate text can substantially improve answer accuracy, especially for sufficiently capable models and when demonstrations, decoding, verification, or training reinforce valid intermediate steps. However, ordinary CoT is not a guaranteed report of the computation that produced an answer, and its gains are often smaller—or absent—when tasks are easy, models are too weak, prompts are poorly designed, or evaluation rewards only the final answer. In some settings, CoT mainly improves answer presentation, encourages additional sampling or computation, or provides a useful interface for external verification rather than creating new reasoning ability. The conflicting literature largely compares different phenomena under the same label: latent reasoning versus verbalized reasoning, prompting versus training, accuracy versus faithfulness, and final-answer performance versus process quality.

## Findings

### Finding 1

**Claim**

CoT prompting can causally improve performance on genuinely multi-step tasks, rather than merely changing formatting.

**Confidence:** High

**Why this confidence level**

The result has been replicated across prompting, supervised scratchpad, and self-consistency settings, although effect sizes vary substantially by task and model.

**Evidence**

- Few-shot rationales produced large gains on arithmetic, symbolic, commonsense, and other reasoning benchmarks, with gains increasing with model scale; the authors argue that intermediate steps allow the model to decompose problems.
- Zero-shot prompts such as “Let’s think step by step” improved performance on several reasoning benchmarks, suggesting that eliciting a multi-step trajectory can matter even without demonstrations.
- Scratchpad supervision improved performance on algorithmic tasks, including tasks requiring intermediate computation, and provided evidence that written intermediate states can function as computational workspace.

### Finding 2

**Claim**

CoT is most effective when the model already has the relevant capabilities and the task benefits from decomposition; it does not reliably create reasoning ability in an incapable model.

**Confidence:** High

**Why this confidence level**

Model-capability dependence is a consistent finding, though the precise threshold and mechanism differ across architectures and tasks.

**Evidence**

- The original CoT results show strong scaling effects: larger models benefit much more than smaller ones, while weaker models may produce plausible but unhelpful or erroneous rationales.
- Later analyses characterize CoT as an elicitation method whose effectiveness depends on latent competence, prompt demonstrations, and the model’s ability to maintain coherent intermediate states.
- Work on process supervision and outcome-supervised reasoning finds that training or search can improve reasoning beyond simply requesting a rationale, indicating that prompting alone is not the whole mechanism.

### Finding 3

**Claim**

Some reported CoT gains are attributable to mechanisms other than better reasoning: extra generated tokens, altered answer priors, decomposition cues, self-consistency voting, or formatting compliance.

**Confidence:** Medium

**Why this confidence level**

The alternative explanations are well supported conceptually and in controlled studies, but their quantitative contribution varies by model, decoding setup, and benchmark.

**Evidence**

- Self-consistency improves results by sampling multiple reasoning paths and selecting the most common answer; much of its benefit therefore comes from search and aggregation, not necessarily from any single rationale being correct.
- Studies using controlled prompts and matched token budgets show that intermediate text can act as a computational or attention-allocation aid, but also that gains depend on how the comparison baseline is constructed; direct comparisons with equally long non-CoT continuations can reduce apparent CoT advantages.
- On tasks where the answer is already accessible through pattern matching or short inference, CoT can increase verbosity without improving accuracy, and can sometimes introduce errors into an otherwise correct answer.

### Finding 4

**Claim**

A verbal CoT is not generally a faithful explanation of the model’s actual causal reasoning process.

**Confidence:** High

**Why this confidence level**

The distinction between usefulness and faithfulness is supported by intervention studies and multiple evaluation frameworks, though measuring internal causal processes remains difficult.

**Evidence**

- Models can be induced to produce rationales that support an answer selected for other reasons, and rationale content can be manipulated without reliably changing the final prediction; this undermines the assumption that the displayed steps are the true basis of the answer.
- Models sometimes state incorrect or post-hoc reasons while producing the correct answer, and can fail to mention decisive information or follow the displayed derivation.
- Faithfulness evaluations distinguish plausibility from causal relevance: a rationale may be useful for prediction or debugging while not being a faithful transcript of internal computation.

### Finding 5

**Claim**

CoT can nevertheless be operationally valuable even when it is not faithful, because it exposes intermediate claims that can be checked, revised, aggregated, or used by external tools.

**Confidence:** High

**Why this confidence level**

These methods demonstrate practical value of intermediate representations, while not resolving whether ordinary CoT itself is faithful.

**Evidence**

- Verifier-guided and process-supervised methods use intermediate steps as objects for scoring, critique, or correction, often improving mathematical reasoning compared with relying only on final-answer supervision.
- Tool-augmented systems can execute calculations or programs derived from intermediate reasoning, turning natural-language steps into an interface for external computation.
- Self-consistency and debate/critique-style methods exploit multiple trajectories or intermediate judgments without requiring every displayed rationale to be a faithful mechanistic explanation.

### Finding 6

**Claim**

The literature’s disagreements are partly caused by benchmark and evaluation artifacts.

**Confidence:** High

**Why this confidence level**

These are methodological differences visible across the literature and are sufficient to explain many apparently contradictory results.

**Evidence**

- Many CoT benchmarks are contaminated or familiar, and exact-match final-answer scoring ignores whether the rationale is valid; apparent reasoning gains can therefore reflect memorization, answer-format effects, or changes in error tolerance.
- Different papers compare CoT against different baselines: direct answer, an equally long neutral prompt, scratchpad training, self-consistency, or tool use. These are not equivalent causal tests.
- Prompt wording, number and quality of demonstrations, decoding temperature, token limits, and whether invalid intermediate steps are penalized can reverse the observed effect.

### Finding 7

**Claim**

The strongest conclusion is that CoT is a conditional reasoning interface, not a universal reasoning strategy and not merely a formatting convention.

**Confidence:** High

**Why this confidence level**

This conclusion reconciles positive capability and engineering results with negative mechanistic and robustness results.

**Evidence**

- The combined literature shows improvements from elicited rationales, scratchpad training, search, verification, and process supervision, but also shows failures under weak models, adversarial prompts, distribution shift, and faithfulness tests.

## Conflicts and Uncertainty

- Positive benchmark results show that CoT can improve final accuracy, while faithfulness studies show that displayed rationales may not explain the actual answer. These findings are compatible because causal usefulness and explanatory faithfulness are different properties.
- Some controlled comparisons find that CoT retains benefits beyond formatting or token count; others find that much of the gain disappears against length- or compute-matched baselines. The residual benefit is task- and model-dependent.
- Self-consistency is often discussed as a CoT result, but it combines rationale generation with stochastic search and majority voting. Attributing its entire gain to verbal reasoning is not justified.
- Results from instruction-tuned frontier models may not generalize to base models, small models, multimodal models, or newer reasoning-trained systems that perform hidden or extended internal computation.
- Final-answer accuracy is an incomplete measure: a model may reach the right answer through an invalid rationale, or a valid rationale may end in an arithmetic or transcription error.

## Remaining Gaps

- There is no universally accepted causal test separating latent computation, verbal scratchpad use, extra-token allocation, and search.
- Mechanistic evidence linking particular rationale tokens to the model’s internal computation remains limited, especially for frontier models.
- More evaluations are needed with contamination-resistant, procedurally generated tasks and with process-level scoring rather than final-answer accuracy alone.
- The optimal relationship between hidden reasoning, visible reasoning, tool calls, verifiers, and user-facing explanations remains unsettled.
- It is still unclear how robust CoT benefits are under distribution shift, adversarially misleading demonstrations, and tasks where intermediate reasoning is long or branching.

## Conclusion

Chain-of-thought prompting is an effective strategy in a specific but important regime: capable models solving problems that genuinely require multiple dependent operations, particularly when CoT is paired with good demonstrations, sufficient token budget, self-consistency, tools, verification, or process supervision. It should not be interpreted as a reliable transcript of reasoning, nor as a universal way to make a weak model reason. The apparent disagreement arises because “CoT works” can mean at least four different things: it raises final-answer accuracy; it supplies a useful external scratchpad; it increases effective inference-time computation through longer generation or sampling; or it faithfully exposes the causal reasoning process. The literature supports the first three in many settings, but not the fourth in general. Thus, CoT is more than output formatting, yet some measured gains do come from formatting and computation-allocation effects. The scientifically defensible position is conditional: evaluate CoT against compute- and length-matched baselines, score intermediate validity and causal faithfulness separately, and distinguish prompting from search and process-supervised reasoning.

Key sources: S1 Wei et al., “Chain-of-Thought Prompting Elicits Reasoning in Large Language Models” (2022); S2 Kojima et al., “Large Language Models are Zero-Shot Reasoners” (2022); S3 Nye et al., “Show Your Work: Scratchpads for Intermediate Computation with Language Models” (2021); S4 Turpin et al., “Language Models Don’t Always Say What They Think” (2023); S5 Merrill and Sabharwal, work on the expressive/complexity limits of CoT (2023–2024); S6 Lightman et al., “Let’s Verify Step by Step” (2023); S7 Uesato et al., “Solving Math Word Problems with Process- and Outcome-Based Feedback” (2022); S8 Wang et al., “Self-Consistency Improves Chain of Thought Reasoning in Language Models” (2023); S9 Lanham et al., “The Truthful or Useful Nature of Chain-of-Thought Reasoning” (2023/2024); S10 Kambhampati and colleagues, critiques of CoT and reasoning claims using controlled baselines (2024); S11 Zheng et al. and related work on when CoT hurts or fails (2023–2024); S12 Turpin et al. (2023), faithfulness interventions; S13 Wiegreffe et al., “Measuring Coherence and Faithfulness of Rationales” (2021); S14 Lanham et al. (2023/2024), rationale faithfulness; S15 Jacovi and Goldberg, “Towards Faithfully Interpretable NLP Systems” (2020); S16 Cobbe et al., “Training Verifiers to Solve Math Word Problems” (2021); S17 Gao et al., “PAL: Program-aided Language Models” (2023); S18 Du et al., “Improving Factuality and Reasoning in Language Models through Multiagent Debate” (2023); S19 Zhou et al. and related benchmark-contamination studies; S20 Soudani et al. and related work on reasoning-benchmark artifacts; S21 OpenAI, “Learning to Reason with LLMs” (2024), illustrating the distinction between prompting and reasoning-oriented training.

## Sources

- No usable sources were retrieved.
