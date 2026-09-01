# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** chain-of-thought-effectiveness

**System Version:** llm-only-baseline-v0

**Model:** gpt-5.6-luna

## Summary

- Overall: 50.1 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.67
- Coverage: 0.69
- Depth: 0.62
- Citation quality: 0.00
- Citation validity: 0.00
- Citation support: 0.00
- Citation completeness: 0.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report names several relevant comparison conditions and recognizes that the literature uses “CoT” inconsistently, but it does not provide the foundational definition and clean intervention taxonomy required by the rubric.
- Candidate evidence:
  - The summary distinguishes “latent reasoning versus verbalized reasoning,” “prompting versus training,” and “final-answer performance versus process quality.”
  - The report separately discusses self-consistency, scratchpad supervision, tool augmentation, and hidden or newer “internal computation.”
  - It contrasts CoT with “direct answer” and “equally long neutral prompt” baselines.
- Missing:
  - It never clearly defines CoT as a prompting intervention that elicits or supplies intermediate natural-language steps before the final answer.
  - It does not systematically distinguish ordinary visible CoT from answer-format instructions, hidden/internal reasoning, self-consistency, tool use, scratchpads, and other inference-time procedures.
  - The distinction between verbose formatting and actual CoT is asserted rather than operationalized.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report covers multiple mathematical, symbolic, algorithmic, and commonsense domains and includes gains, null effects, and harms. It falls short of full depth because open-ended and knowledge tasks are not substantively analyzed and the empirical evidence is not concretely documented.
- Candidate evidence:
  - The report discusses “arithmetic, symbolic, commonsense, and other reasoning benchmarks.”
  - It reports gains from few-shot rationales, zero-shot “Let’s think step by step,” and scratchpad supervision on algorithmic and intermediate-computation tasks.
  - It notes null or harmful effects when tasks are easy, when pattern matching suffices, and when CoT introduces errors into an otherwise correct answer.
- Missing:
  - Knowledge-heavy, factual, and genuinely open-ended reasoning tasks are mentioned only indirectly through “commonsense” and “other reasoning benchmarks.”
  - The evidence is presented as broad literature summaries without concrete study-level results, task names, effect sizes, or clearly separated findings by task family.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report gives a useful account of capability, scale, task decomposition, prompting, demonstrations, baselines, and shift. It lacks a focused treatment of training-distribution similarity and more precise evidence about the strength and limits of each moderator.
- Candidate evidence:
  - It states that gains increase with model scale and that weaker models may produce “plausible but unhelpful or erroneous rationales.”
  - It says CoT works best when tasks benefit from decomposition and fails more often on easy tasks or tasks where pattern matching suffices.
  - It identifies prompt wording, demonstration number and quality, token limits, decoding temperature, baseline construction, and distribution shift as moderators.
  - It says results may reverse depending on “how the comparison baseline is constructed.”
- Missing:
  - Training-distribution similarity is not directly analyzed; contamination and familiarity are mentioned, but similarity between demonstrations/training data and evaluation tasks is not developed as a moderator.
  - The report does not clearly separate well-established moderators from contested or insufficiently tested ones.
  - Task structure and difficulty are treated somewhat generally, with little analysis of which structures benefit or fail.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is one of the stronger sections: it directly addresses reasoning versus formatting, additional computation, and faithfulness. Full depth is not warranted because the proposed mechanisms are not tied to sufficiently specific separating experiments.
- Candidate evidence:
  - It explicitly argues that CoT is “not merely a formatting trick” while acknowledging effects from “extra generated tokens, altered answer priors, decomposition cues.”
  - It says matched-token-budget and equally long non-CoT comparisons can reduce apparent advantages.
  - It distinguishes useful intermediate representations from faithful explanations and states that “causal usefulness and explanatory faithfulness are different properties.”
  - The conclusion says some gains come from “formatting and computation-allocation effects.”
- Missing:
  - The report does not give a detailed account of evidence that isolates intermediate-step content—for example, content-preserving versus content-corrupting interventions or irrelevant-chain controls.
  - It does not clearly distinguish answer extraction and presentation effects from verbosity/context effects in empirical terms.
  - The mechanism discussion remains largely at the level of plausible alternatives rather than a systematic comparison of tests and findings.

### R5

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report correctly separates prompting from self-consistency, longer generation, verification, and tools, and recognizes the need for matched baselines. It lacks concrete protocol-level comparisons and a full treatment of extraction and external-computation confounds.
- Candidate evidence:
  - The report states that self-consistency combines multiple rationale samples with majority voting and that its gains should not be attributed entirely to verbal reasoning.
  - It mentions “equally long non-CoT continuations” and “matched token budgets.”
  - It separately discusses verification, tools, calculators/program execution in tool-augmented systems, and process supervision.
  - It warns that different studies compare direct answering, neutral prompts, scratchpad training, self-consistency, or tool use, which are not equivalent causal tests.
- Missing:
  - Calculators, code, retrieval, and external computation are listed or exemplified but not systematically compared with CoT-only conditions.
  - The report does not provide concrete like-for-like comparisons with matched sampling count, generation length, latency, or total inference compute.
  - Answer extraction effects are mentioned only indirectly through formatting and exact-match evaluation.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report captures the central distinction between correlation, accuracy, and causal faithfulness and points to intervention evidence. It does not deeply explain the actual diagnostic designs or their limitations.
- Candidate evidence:
  - It reports that rationale content can be manipulated “without reliably changing the final prediction.”
  - It notes incorrect or post-hoc reasons, omitted decisive information, and failure to follow the displayed derivation.
  - It explicitly distinguishes rationale plausibility from causal relevance and faithfulness from accuracy.
  - It calls for scoring intermediate validity and causal faithfulness separately and mentions intervention studies and distribution-shift evaluations.
- Missing:
  - The report does not identify or explain concrete tests such as scrambling, trace corruption, irrelevant-chain controls, or counterfactual token-level interventions in enough detail.
  - It does not assess logical validity systematically apart from saying that models may produce incorrect or post-hoc reasons.
  - The cited intervention findings are not documented with specific models, tasks, procedures, or results.

### R7

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report understands the main comparability problems, but evidential documentation is insufficient. The absence of usable retrieved sources and concrete study-level details prevents strong evaluation of evidence quality.
- Candidate evidence:
  - It warns that headline scores are not directly comparable because papers use different baselines, prompt wording, demonstrations, temperatures, token limits, and invalid-step penalties.
  - It mentions contamination, exact-match scoring, model family differences, and generalization limits to base, small, multimodal, and newer reasoning-trained models.
  - The report lists a substantial set of named sources and source categories.
- Missing:
  - There are no concrete model versions or sizes, dataset names and configurations, decoding settings, metrics beyond generic exact-match, uncertainty estimates, effect sizes, or replication details.
  - The report does not evaluate the quality or reliability of individual sources, and several citations are vague (“and related work”).
  - The Sources section explicitly says: “No usable sources were retrieved,” leaving the literature claims unsupported and difficult to verify.
  - Methodological differences are enumerated but not tied to specific studies in a way that demonstrates why particular results conflict.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The synthesis is qualified, directly answers the central question, and separates established outcome effects from unresolved mechanistic claims. It loses depth because cost, latency, and deployment reliability implications are only implicit or partial.
- Candidate evidence:
  - The conclusion directly characterizes CoT as effective in a “specific but important regime,” not universal and not merely formatting.
  - It states that the literature supports final-answer gains, useful scratchpad functions, and increased inference-time computation in many settings, but not faithful transcripts in general.
  - It recommends compute- and length-matched baselines and separate scoring of intermediate validity and causal faithfulness.
  - It discusses practical use with capable models, demonstrations, token budgets, self-consistency, tools, verification, and process supervision.
- Missing:
  - Cost and latency implications are not explicitly analyzed, despite longer generation, sampling, verification, and tool use likely changing both.
  - Reliability implications are discussed mainly through faithfulness and robustness, but not as a concrete deployment tradeoff involving error propagation, monitoring, or user trust.
  - The practical recommendation does not clearly distinguish when visible CoT should be exposed to users versus used privately or replaced by tools/verifiers.

### Novel Value

- The report offers a useful synthesis that separates final-answer effectiveness, scratchpad/computation-allocation effects, search and voting, and mechanistic faithfulness.
- It identifies a coherent explanation for conflicting findings: varying baselines, task and model regimes, protocol changes, evaluation targets, and conflation of visible rationales with internal reasoning.

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

- Q1: Few-shot chain-of-thought rationales produced large gains on arithmetic, symbolic, commonsense, and other reasoning benchmarks, with gains increasing with model scale.
- Q2: Zero-shot prompts such as “Let’s think step by step” improved performance on several reasoning benchmarks.
- Q3: Scratchpad supervision improved performance on algorithmic tasks requiring intermediate computation and provided evidence that written intermediate states can function as computational workspace.
- Q4: Larger models benefit more from CoT than smaller models, while weaker models may produce plausible but unhelpful or erroneous rationales.
- Q5: CoT effectiveness depends on latent competence, prompt demonstrations, and the model’s ability to maintain coherent intermediate states.
- Q6: Training or search can improve reasoning beyond simply requesting a rationale, indicating that prompting alone is not the whole mechanism.
- Q7: Self-consistency improves results by sampling multiple reasoning paths and selecting the most common answer.
- Q8: Intermediate text can act as a computational or attention-allocation aid, but direct comparisons with equally long non-CoT continuations can reduce apparent CoT advantages.
- Q9: On tasks where the answer is accessible through pattern matching or short inference, CoT can increase verbosity without improving accuracy and can sometimes introduce errors into an otherwise correct answer.
- Q10: Models can produce rationales that support an answer selected for other reasons, and rationale content can sometimes be manipulated without reliably changing the final prediction.
- Q11: Models sometimes state incorrect or post-hoc reasons while producing the correct answer, fail to mention decisive information, or do not follow the displayed derivation.
- Q12: Faithfulness evaluations distinguish plausibility from causal relevance: a rationale may be useful for prediction or debugging without being a faithful transcript of internal computation.
- Q13: Verifier-guided and process-supervised methods use intermediate steps for scoring, critique, or correction and can improve mathematical reasoning compared with relying only on final-answer supervision.
- Q14: Tool-augmented systems can execute calculations or programs derived from intermediate reasoning, turning natural-language steps into an interface for external computation.
- Q15: Self-consistency and debate or critique-style methods can exploit multiple trajectories or intermediate judgments without requiring every displayed rationale to be a faithful mechanistic explanation.
- Q16: Benchmark contamination and familiarity, together with exact-match final-answer scoring, can make apparent reasoning gains reflect memorization, answer-format effects, or changes in error tolerance.
- Q17: Comparisons against direct answering, equally long neutral prompts, scratchpad training, self-consistency, or tool use are not equivalent causal tests.
- Q18: Prompt wording, demonstration quality and quantity, decoding temperature, token limits, and penalties for invalid intermediate steps can reverse the observed CoT effect.
- Q19: The combined literature reports improvements from elicited rationales, scratchpad training, search, verification, and process supervision, while also reporting failures under weak models, adversarial prompts, distribution shift, and faithfulness tests.
- Q20: Displayed rationales may not explain the actual answer even when CoT improves final accuracy, because causal usefulness and explanatory faithfulness are different properties.
- Q21: Some controlled comparisons find that CoT retains benefits beyond formatting or token count, whereas other comparisons find that much of the gain disappears against length- or compute-matched baselines.
- Q22: Self-consistency combines rationale generation with stochastic search and majority voting, so its entire gain should not be attributed to verbal reasoning.
- Q23: Results from instruction-tuned frontier models may not generalize to base models, small models, multimodal models, or newer reasoning-trained systems.
- Q24: Final-answer accuracy is incomplete as a measure because a model may reach the correct answer through an invalid rationale, or a valid rationale may end in an arithmetic or transcription error.
- Q25: There is no universally accepted causal test separating latent computation, verbal scratchpad use, extra-token allocation, and search.
- Q26: Mechanistic evidence linking particular rationale tokens to internal computation remains limited, especially for frontier models.
- Q28: The optimal relationship among hidden reasoning, visible reasoning, tool calls, verifiers, and user-facing explanations remains unsettled.
- Q29: CoT benefits may be non-robust under distribution shift, adversarially misleading demonstrations, and tasks involving long or branching intermediate reasoning.
- Q30: CoT is effective in a specific regime involving capable models and tasks requiring multiple dependent operations, particularly when paired with demonstrations, sufficient token budget, self-consistency, tools, verification, or process supervision.
- Q31: CoT should not be interpreted as a reliable transcript of reasoning or as a universal way to make a weak model reason.
- Q32: The literature supports final-answer improvements, useful external scratchpad functionality, and increased effective inference-time computation through longer generation or sampling in many settings, but does not support faithful exposure of the causal reasoning process in general.
- Q33: Some measured CoT gains result from formatting and computation-allocation effects.

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
3. 32 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ac152f1d42cbe0f247f27e3225b834f4d7d35d3a27bade4d08806b371c248b6d`
- Candidate report hash: `753d737f9c555fe6386caa71b57d0c1ab7c2d03a3579deeba2b36470bebb4cf4`
- LLM calls: 2
- Evaluated at: 2026-09-01T05:56:52.222152+00:00
