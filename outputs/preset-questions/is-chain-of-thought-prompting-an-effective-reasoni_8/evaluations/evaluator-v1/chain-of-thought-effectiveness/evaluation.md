# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** chain-of-thought-effectiveness

**System Version:** llm-only-baseline-v0

**Model:** gpt-5.6-luna

## Summary

- Overall: 51.2 / 100
- Evaluation completeness: 80%
- Comprehensiveness: 0.69
- Coverage: 0.69
- Depth: 0.69
- Citation quality: 0.00
- Citation validity: 0.00
- Citation support: 0.00
- Citation completeness: 0.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report identifies most relevant neighboring concepts, but it does not clearly establish the intervention and comparison conditions with enough precision.
- Candidate evidence:
  - The report characterizes CoT as producing “intermediate text” or “elicited rationales” and contrasts it with “direct answer” baselines.
  - It separately mentions “latent reasoning versus verbalized reasoning,” “hidden or internal computation,” self-consistency, tool augmentation, scratchpad training, and process supervision.
  - It notes that self-consistency combines “rationale generation with stochastic search and majority voting.”
- Missing:
  - There is no clear, standalone definition of CoT as a prompting intervention involving explicit intermediate reasoning before the final answer.
  - The distinctions among ordinary CoT, answer-format instructions, hidden/internal reasoning, scratchpads, and other inference-time procedures remain mostly implicit rather than systematically defined.
  - Answer formatting is discussed as a possible effect, but the report does not give a concrete format-only comparison condition.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report covers multiple mathematical, symbolic, algorithmic, and commonsense domains and acknowledges gains, nulls, and harms. Coverage is not complete because knowledge/open-ended reasoning and empirical detail are limited.
- Candidate evidence:
  - It reports gains on “arithmetic, symbolic, commonsense, and other reasoning benchmarks.”
  - It discusses few-shot rationales, zero-shot “Let’s think step by step,” and scratchpad supervision on algorithmic tasks.
  - It also notes null or negative effects when tasks are easy, when models are weak, and when CoT introduces errors into an otherwise correct answer.
- Missing:
  - Knowledge-intensive and genuinely open-ended reasoning tasks are not substantively assessed; commonsense is mentioned but not analyzed in detail.
  - The report provides few concrete comparative results, task examples, effect sizes, or study-specific findings across task families.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: Most requested moderators appear and are used to explain disagreement, but training-distribution similarity and evidential status of individual moderator claims are underdeveloped.
- Candidate evidence:
  - It identifies model scale and capability as moderators, stating that larger models benefit more and weak models may produce unhelpful rationales.
  - It discusses task structure, including whether problems require “multiple dependent operations” or benefit from decomposition.
  - It identifies prompt wording, demonstration number and quality, token limits, decoding temperature, and baseline construction as moderators.
  - It notes failures under “distribution shift” and adversarially misleading demonstrations.
- Missing:
  - Training-distribution similarity is not directly analyzed, despite being a specified moderator.
  - The report does not clearly distinguish which moderator findings are strongly established, contested, or based on limited testing.
  - Task difficulty is discussed generally but not tied to concrete difficulty gradients or interaction effects.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: The mechanisms are well framed and the report recognizes that multiple mechanisms can coexist, but the evidence separating them is described only generally.
- Candidate evidence:
  - The report explicitly states that some gains may come from “extra generated tokens, altered answer priors, decomposition cues, self-consistency voting, or formatting compliance.”
  - It says matched-token-budget comparisons can reduce apparent CoT advantages and that intermediate text can serve as a computational or attention-allocation aid.
  - It distinguishes final-answer usefulness from faithfulness, stating that a rationale can improve prediction or debugging without being a faithful transcript of internal computation.
  - It notes that controlled comparisons sometimes find residual benefits beyond formatting or token count.
- Missing:
  - The report does not give sufficiently concrete descriptions of the controlled experiments that separate reasoning-content effects from verbosity, formatting, or context effects.
  - It does not clearly distinguish answer-extraction effects from other formatting effects or discuss how extraction protocols can change measured accuracy.
  - The causal status of intermediate reasoning content remains asserted at a high level rather than evaluated with detailed evidence.

### R5

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report recognizes the main confounds and calls for compute- and length-matched baselines, but does not document enough concrete controls or comparisons.
- Candidate evidence:
  - It explicitly warns that self-consistency combines rationale generation with “stochastic search and majority voting.”
  - It discusses “equally long non-CoT continuations” and matched token budgets as relevant controls.
  - It distinguishes prompting from “search,” “tool use,” “verification,” and process-supervised reasoning.
  - It describes calculators or programs indirectly through “tool-augmented systems” that execute calculations or programs derived from intermediate reasoning.
- Missing:
  - Answer extraction is not directly analyzed as a separate source of improvement or error.
  - The report does not provide systematic like-for-like comparisons for sampling temperature, number of samples, generation length, tools, retrieval, calculators, or code execution.
  - It does not clearly separate ordinary single-sample CoT from longer-generation and externally scaffolded systems in the empirical claims.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: This requirement is substantially addressed conceptually, including the key accuracy-versus-faithfulness distinction, but the testing methodology and evidence are not developed deeply enough.
- Candidate evidence:
  - It states that verbal CoT is “not generally a faithful explanation” of the causal reasoning process.
  - It reports that rationale content can be manipulated without reliably changing the final prediction and that models can give incorrect or post-hoc reasons for correct answers.
  - It explicitly distinguishes plausibility, usefulness, accuracy, and causal relevance.
  - It refers to “intervention studies,” faithfulness evaluations, and the need to score intermediate validity separately from final-answer accuracy.
- Missing:
  - The report does not specifically discuss trace scrambling, corruption, irrelevant-chain controls, or counterfactual interventions in enough detail to show how each tests causal relevance.
  - Logical validity of the complete trace is mentioned only indirectly; the report does not explain how valid and invalid intermediate steps are evaluated.
  - The cited intervention findings are not tied to identifiable experimental designs, models, or results.

### R7

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report understands the major comparability problems, but it does not actually evaluate the cited literature at the evidential and source-specific level required.
- Candidate evidence:
  - The report identifies differences in models, prompt wording, demonstrations, decoding temperature, token limits, baselines, scoring, contamination, and whether invalid steps are penalized.
  - It warns that exact-match final-answer scoring ignores rationale validity and that headline results from different protocols are not directly comparable.
  - It mentions replication across prompting, scratchpad, and self-consistency settings and lists a range of named sources.
- Missing:
  - The report gives no study-level details about model versions or sizes, datasets, exact baselines, decoding settings, metrics, uncertainty, or replication outcomes.
  - The listed sources are not connected to specific claims with verifiable citations or results; the Sources section explicitly says, “No usable sources were retrieved.”
  - Source quality and the reliability of individual claims are not evaluated.
  - Claims about contamination, controlled comparisons, and replication remain broad and unsupported by concrete documentation.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The synthesis directly answers the central question and is appropriately conditional, but practical cost, latency, and deployment implications are incomplete.
- Candidate evidence:
  - The conclusion gives a qualified answer: CoT is effective for capable models and genuinely multi-step tasks, but is “not merely a formatting convention” and is not universal.
  - It synthesizes several mechanisms: final-answer accuracy, external scratchpad value, increased inference-time computation, and causal-faithfulness claims.
  - It recommends compute- and length-matched baselines, separate process and faithfulness scoring, and distinguishing prompting from search and process-supervised reasoning.
  - It notes practical value through verification, tools, critique, and process supervision.
- Missing:
  - Cost and latency implications are not explicitly discussed, despite the requirement; longer generation, sampling, verification, and tool use are mentioned but not translated into operational tradeoffs.
  - Reliability implications are present mainly through faithfulness and robustness discussion, but appropriate-use guidance is not developed into concrete recommendations.
  - The conclusion sometimes groups CoT with self-consistency, tools, and process supervision, which weakens the precision of claims about CoT prompting alone.

### Novel Value

- The report offers a useful synthesis that separates four meanings of “CoT works”: improved final accuracy, external scratchpad utility, increased inference-time computation, and faithful exposure of causal reasoning.
- It frames much of the disagreement as a mismatch between prompting, search, training, faithfulness, and evaluation protocols rather than as a simple contradiction in findings.
- It emphasizes compute- and length-matched baselines and separate process-faithfulness evaluation as practical ways to resolve the central dispute.

## Citations

### Support

#### F1: NOT_EVALUABLE

- Claim: CoT prompting can causally improve performance on genuinely multi-step tasks, rather than merely changing formatting.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F2: NOT_EVALUABLE

- Claim: CoT is most effective when the model already has the relevant capabilities and the task benefits from decomposition; it does not reliably create reasoning ability in an incapable model.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F3: NOT_EVALUABLE

- Claim: Some reported CoT gains are attributable to mechanisms other than better reasoning: extra generated tokens, altered answer priors, decomposition cues, self-consistency voting, or formatting compliance.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F4: NOT_EVALUABLE

- Claim: A verbal CoT is not generally a faithful explanation of the model’s actual causal reasoning process.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F5: NOT_EVALUABLE

- Claim: CoT can nevertheless be operationally valuable even when it is not faithful, because it exposes intermediate claims that can be checked, revised, aggregated, or used by external tools.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F6: NOT_EVALUABLE

- Claim: The literature’s disagreements are partly caused by benchmark and evaluation artifacts.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F7: NOT_EVALUABLE

- Claim: The strongest conclusion is that CoT is a conditional reasoning interface, not a universal reasoning strategy and not merely a formatting convention.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

### Missing Citations

- Q1: Few-shot chain-of-thought rationales have produced gains on arithmetic, symbolic, commonsense, and other reasoning benchmarks, with gains increasing with model scale.
- Q2: Zero-shot prompts such as “Let’s think step by step” have improved performance on several reasoning benchmarks.
- Q3: Scratchpad supervision has improved performance on algorithmic tasks requiring intermediate computation and has provided evidence that written intermediate states can function as computational workspace.
- Q4: Chain-of-thought prompting can causally improve performance on genuinely multi-step tasks rather than merely changing output formatting.
- Q5: Larger models benefit more from chain-of-thought prompting than smaller models, while weaker models may produce plausible but unhelpful or erroneous rationales.
- Q6: Chain-of-thought effectiveness depends on latent competence, prompt demonstrations, and the model’s ability to maintain coherent intermediate states.
- Q7: Training or search can improve reasoning beyond simply requesting a rationale, indicating that prompting alone is not the whole mechanism.
- Q8: Self-consistency improves results by sampling multiple reasoning paths and selecting the most common answer.
- Q9: The benefit of self-consistency derives at least partly from search and aggregation rather than necessarily from the correctness of any single rationale.
- Q10: Intermediate text can act as a computational or attention-allocation aid, but apparent chain-of-thought advantages depend on how the comparison baseline is constructed.
- Q11: Comparisons with equally long non-chain-of-thought continuations can reduce apparent chain-of-thought advantages.
- Q12: On tasks where the answer is accessible through pattern matching or short inference, chain-of-thought can increase verbosity without improving accuracy and can sometimes introduce errors into an otherwise correct answer.
- Q13: A verbal chain-of-thought is not generally a faithful explanation of the model’s actual causal reasoning process.
- Q14: Models can produce rationales that support an answer selected for other reasons, and rationale content can sometimes be manipulated without reliably changing the final prediction.
- Q15: Models sometimes state incorrect or post-hoc reasons while producing the correct answer, fail to mention decisive information, or do not follow the displayed derivation.
- Q16: Faithfulness evaluations distinguish rationale plausibility from causal relevance, so a rationale may be useful for prediction or debugging without being a faithful transcript of internal computation.
- Q17: Verifier-guided and process-supervised methods use intermediate steps for scoring, critique, or correction and can improve mathematical reasoning compared with relying only on final-answer supervision.
- Q18: Tool-augmented systems can execute calculations or programs derived from intermediate reasoning, using natural-language steps as an interface for external computation.
- Q19: Self-consistency and debate or critique methods can exploit multiple trajectories or intermediate judgments without requiring every displayed rationale to be a faithful mechanistic explanation.
- Q20: Benchmark contamination and familiarity, together with exact-match final-answer scoring, can make apparent reasoning gains reflect memorization, answer-format effects, or changes in error tolerance.
- Q21: Different studies compare chain-of-thought with different baselines, including direct answers, equally long neutral prompts, scratchpad training, self-consistency, and tool use, and these comparisons are not equivalent causal tests.
- Q22: Prompt wording, demonstration number and quality, decoding temperature, token limits, and penalties for invalid intermediate steps can change or reverse the observed chain-of-thought effect.
- Q23: Positive benchmark results showing improved final accuracy and faithfulness studies showing that displayed rationales may not explain the actual answer are compatible because causal usefulness and explanatory faithfulness are different properties.
- Q24: Some controlled comparisons find chain-of-thought benefits beyond formatting or token count, while other studies find that much of the gain disappears against length- or compute-matched baselines.
- Q25: Self-consistency combines rationale generation with stochastic search and majority voting, so attributing its entire gain to verbal reasoning is not justified.
- Q26: Results from instruction-tuned frontier models may not generalize to base models, small models, multimodal models, or newer reasoning-trained systems that perform hidden or extended internal computation.
- Q27: Final-answer accuracy is incomplete as an evaluation measure because a model may reach the correct answer through an invalid rationale, or a valid rationale may end in an arithmetic or transcription error.
- Q28: There is no universally accepted causal test separating latent computation, verbal scratchpad use, extra-token allocation, and search.
- Q29: Mechanistic evidence linking particular rationale tokens to internal computation remains limited, especially for frontier models.
- Q30: More evaluations are needed using contamination-resistant, procedurally generated tasks and process-level scoring rather than final-answer accuracy alone.
- Q31: The optimal relationship among hidden reasoning, visible reasoning, tool calls, verifiers, and user-facing explanations remains unsettled.
- Q32: Chain-of-thought benefits are not yet established as robust under distribution shift, adversarially misleading demonstrations, and tasks with long or branching intermediate reasoning.
- Q33: Chain-of-thought is effective in a specific regime involving capable models and problems requiring multiple dependent operations, particularly when combined with demonstrations, sufficient token budget, self-consistency, tools, verification, or process supervision.
- Q34: Chain-of-thought should not be interpreted as a reliable transcript of reasoning or as a universal method for making a weak model reason.
- Q35: The phrase “chain-of-thought works” can refer to increased final-answer accuracy, an external scratchpad, increased inference-time computation through longer generation or sampling, or faithful exposure of causal reasoning.
- Q36: The literature supports accuracy improvements, useful external scratchpads, and computation-allocation effects in many settings, but does not establish faithful exposure of causal reasoning in general.
- Q37: Some measured chain-of-thought gains arise from formatting and computation-allocation effects rather than improved reasoning alone.

## Deterministic Checks

- `run_metadata_loads`: PASS
- `report_exists`: PASS
- `sources_present`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `structured_report_parses`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `report_question_matches`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `source_ids_unique`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `source_ids_syntactically_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `source_urls_present`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `evidence_objects_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `confidence_values_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `citation_ids_syntactically_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `citation_ids_resolve`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `structured_claim_evidence_available`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `ledger_claim_ids_unique`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `ledger_evidence_relationships_resolve`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `ledger_confidence_values_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `ledger_evidence_ids_unique`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.

## Main Weaknesses

1. R1: Define chain-of-thought prompting and distinguish it from direct answering, answer-format instructions, hidden or internal reasoning, self-consistency, tool augmentation, and other inference-time procedures.
2. R7: Evaluate the evidential strength and comparability of the cited literature, including model versions and sizes, datasets, baselines, prompt protocols, decoding settings, metrics, uncertainty, replication, and source quality.
3. 37 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ac152f1d42cbe0f247f27e3225b834f4d7d35d3a27bade4d08806b371c248b6d`
- Candidate report hash: `753d737f9c555fe6386caa71b57d0c1ab7c2d03a3579deeba2b36470bebb4cf4`
- LLM calls: 2
- Evaluated at: 2026-09-01T05:46:43.235372+00:00
