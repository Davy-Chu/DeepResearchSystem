# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** chain-of-thought-effectiveness

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 77.3 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.64
- Coverage: 0.66
- Depth: 0.59
- Citation quality: 0.97
- Citation validity: 1.00
- Citation support: 0.94
- Citation completeness: 1.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report recognizes that CoT is not a single uniform intervention, but it does not establish the conceptual boundaries and comparison conditions required by the rubric.
- Candidate evidence:
  - The report states that “CoT” denotes several interventions and lists “few-shot and zero-shot CoT,” “self-consistency,” “contrastive prompting,” “hierarchical planning,” “Tree of Thoughts,” “least-to-most decomposition,” and “latent CoT” as distinct variants.
  - The report’s conclusion characterizes CoT as a “conditional test-time scaffold.”
- Missing:
  - It does not clearly define ordinary chain-of-thought prompting as eliciting intermediate step-by-step text before the final answer.
  - Direct answering is mentioned only indirectly, without an explicit comparison definition.
  - Hidden or internal reasoning is not substantively distinguished from visible CoT.
  - Self-consistency, tools, and other procedures are listed but not clearly separated in terms of what they add or how they differ experimentally.
  - It does not explain that verbose or stepwise text is not necessarily CoT in the relevant causal sense.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: It covers mathematical, symbolic, commonsense, knowledge, scientific, medical, and logical tasks and acknowledges heterogeneity, but open-ended reasoning and detailed cross-task comparison are underdeveloped.
- Candidate evidence:
  - The report cites gains on arithmetic, commonsense, and symbolic reasoning tasks, including GSM8K.
  - It reports cross-model, cross-dataset gains across scientific, medical, knowledge-based, and logical QA datasets.
  - It states that benefits may be concentrated in mathematical and symbolic reasoning while also noting positive cross-domain evidence.
- Missing:
  - Open-ended reasoning is not substantively assessed as a distinct task type.
  - The report gives few concrete null or harmful results by task family beyond general statements about marginal or negative effects for reasoning-native models.
  - The evidence is summarized largely through secondary or high-level source descriptions rather than detailed task-by-task comparisons.

### R3

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report explains several major sources of disagreement, especially model regime, difficulty, length, and baseline, but omits or only gestures toward training-distribution similarity and gives limited comparative moderator analysis.
- Candidate evidence:
  - The report identifies model capability and scale as moderators, citing emergent benefits at sufficiently large scales and different effects for non-reasoning versus reasoning-native models.
  - It discusses task difficulty and structure, including larger effects on challenging arithmetic tasks and an inverted-U relationship between CoT length and performance.
  - It identifies baseline prompting behavior and prompt design as major fault lines, especially few-shot CoT versus zero-shot CoT.
  - It discusses chain length, structured versus flat CoT, and the possibility that stronger models need fewer steps.
- Missing:
  - Training-distribution similarity is not directly analyzed as a moderator.
  - Prompt and demonstration design are discussed mainly through the few-shot/zero-shot distinction; exemplar quality, ordering, domain match, and wording are not systematically treated.
  - The report does not clearly distinguish well-established moderators from those supported only by limited recent preprints.
  - Interactions among capability, task structure, prompt design, and baseline behavior are proposed but not demonstrated with matched evidence.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is one of the report’s strongest areas: it directly rejects both the simplistic ‘reasoning’ and ‘mere formatting’ interpretations and cites relevant interventions, while acknowledging that causal isolation remains incomplete.
- Candidate evidence:
  - It explicitly states that final-answer accuracy and faithful reasoning are distinct and that a displayed CoT need not be what caused the answer.
  - It reports that filler tokens alone did not improve accuracy, suggesting that mere verbosity is insufficient.
  - It discusses output-format alignment as a possible primary function of few-shot exemplars for strong recent models.
  - It cites faithfulness tests involving truncation and injected mistakes, and notes that structured Hi-CoT can outperform flat CoT while acknowledging that this does not isolate semantic reasoning from other prompt effects.
- Missing:
  - The report does not provide a systematic taxonomy of additional-context, verbosity, semantic computation, and answer-extraction mechanisms.
  - The evidence separating these mechanisms remains limited; format-, token-, and length-matched controls are mostly proposed as gaps rather than reported results.
  - It does not deeply analyze whether displayed intermediate content changes computation or merely changes the response policy.

### R5

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes the confounding problem but does not adequately evaluate the effects of decoding, computation budget, extraction, and external scaffolding separately.
- Candidate evidence:
  - The report says that CoT variants may add demonstrations, decomposition, search, aggregation, retrieval, or formatting constraints and should not be pooled as one mechanism.
  - It identifies self-consistency and other structured variants as distinct interventions.
  - It lists as an unresolved gap whether zero-shot CoT improves reasoning when output format, response length, token budget, sampling, and parsing are held constant.
- Missing:
  - Sampling and self-consistency/voting are not quantitatively separated from the CoT prompt itself.
  - Longer generation and additional token computation are discussed but not controlled in reported comparisons.
  - Calculators, code execution, retrieval, and other external tools are not actually evaluated or separated from CoT effects.
  - The report offers few like-for-like baseline results; most controls appear as recommendations or remaining gaps.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: It covers the crucial accuracy-versus-faithfulness distinction and names meaningful causal tests, but the empirical treatment of validity and causal relevance is summarized rather than comprehensive.
- Candidate evidence:
  - It explicitly distinguishes correct final answers from logically correct, relevant, and evidence-supported reasoning steps.
  - It cites faithfulness tests using early answering, chain truncation, and injected mistakes, reporting substantial task variation and weak correlation between faithfulness and accuracy gains.
  - It notes that traces can be post-hoc, incorrect, or weakly related to the accuracy gain.
  - It identifies independent verification of logically correct and causally involved chains as an unresolved gap.
- Missing:
  - Trace scrambling and irrelevant-chain controls are not discussed in concrete detail.
  - Counterfactual interventions are not clearly distinguished from truncation or mistake injection.
  - Distribution-shift tests of trace faithfulness are mentioned only indirectly as a remaining concern, not presented as evidence.
  - The report does not assess the logical validity of traces across a broad set of tasks in detail.

### R7

- Coverage: 0.50
- Depth: 0.50
- Rationale: It correctly identifies comparability and evaluation problems, but it does not perform the detailed evidence-quality audit required by the rubric.
- Candidate evidence:
  - The report repeatedly warns that studies use different model generations, baselines, tasks, and protocols and that headline scores should not be treated as universal.
  - It notes that common GSM8K evaluators mishandled boxed-answer formats and that different GPQA metrics produced different conclusions.
  - It flags that hierarchical and length-calibrated claims come primarily from recent preprints and lack independent replication.
  - It acknowledges that the retrieved material lacks matched protocols sufficient to reconcile cross-domain claims quantitatively.
- Missing:
  - Model versions and sizes are not systematically reported across the cited studies.
  - Datasets, prompt wording, demonstrations, decoding settings, token budgets, and metrics are not presented in enough detail to assess comparability.
  - Uncertainty, confidence intervals, effect-size variability, and statistical significance are largely absent.
  - Replication quality and source reliability are not evaluated systematically; the source list includes blogs, news pages, Medium posts, aggregators, and incomplete excerpts alongside primary papers.
  - The report sometimes gives high confidence while relying on summarized or secondary evidence without documenting the underlying methods.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The synthesis is qualified, directly answers the central question, and gives useful evaluation guidance, but it omits explicit treatment of cost and latency and provides limited concrete deployment guidance.
- Candidate evidence:
  - The conclusion directly characterizes CoT as conditional rather than universally effective or merely formatting.
  - It states that CoT can improve final answers in earlier-model and difficult multi-step settings while few-shot exemplars may mainly standardize format for strong recent models.
  - It recommends format- and token-matched controls and separate measures of final accuracy, step-level validity, and faithfulness.
  - The report explicitly identifies unresolved gaps and limits confidence in claims about hierarchical and length-calibrated CoT.
- Missing:
  - Cost and latency implications are not substantively discussed, despite the rubric explicitly requiring them.
  - The practical tradeoff between longer traces, additional sampling, reliability, and computational expense is not evaluated.
  - Recommendations for when practitioners should use direct answering, zero-shot CoT, few-shot CoT, or external tools are only implicit rather than operationalized.
  - Some practical conclusions depend on evidence whose comparability and source quality the report itself has not fully established.

### Novel Value

- The report usefully reframes the dispute as conditional rather than binary: CoT can improve accuracy in some model/task regimes while few-shot exemplars may mainly align format for stronger models.
- It identifies baseline choice—classic CoT versus direct prompting versus few-shot CoT versus zero-shot CoT—as a central explanation for apparently conflicting findings.
- It separates final-answer accuracy from faithfulness and emphasizes that visible traces are not automatically causal explanations.
- It highlights evaluation and answer-extraction errors, including boxed-answer parsing, as a potentially decisive source of disagreement.
- It brings together model regime, task difficulty, chain length, prompt design, parsing, and faithfulness as interacting fault lines rather than treating CoT as a single intervention.

## Citations

### Support

#### F1: SUPPORTED

- Claim: CoT is an effective conditional intervention for final-answer performance, especially in some earlier-model and difficult multi-step settings.
- Sources: S20, S27, S13
- Rationale: The saved sources directly report that chain-of-thought prompting improves final-answer performance relative to standard prompting on arithmetic, commonsense, and symbolic reasoning tasks. S20 and S27 especially support effectiveness in difficult multi-step problems and show that benefits are strongest for sufficiently large models, while S13 reports gains across multiple models and datasets. The phrase “conditional intervention” is an interpretation of the prompting comparison, but the important factual content is supported.
- Supporting text: S20: “chain-of-thought prompting improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks” and “outperforms standard prompting.” S27: CoT enables models to solve “complex reasoning problems that are not solvable with standard prompting,” with a 58% GSM8K result for PaLM 540B versus 55% prior state of the art. S13: “gains from CoT reasoning strategies remain robust across different models and datasets.”

#### F2: SUPPORTED

- Claim: For strong recent models, the incremental value of few-shot CoT exemplars may be primarily output-format alignment rather than additional reasoning.
- Sources: S25
- Rationale: S25 directly reports that, for recent strong models such as the Qwen2.5 series, traditional CoT exemplars do not improve reasoning performance over Zero-Shot CoT and primarily align output format with human expectations. The claim’s cautious wording (“may be”) is supported, though the source specifically concerns mathematical reasoning tasks.
- Supporting text: The abstract states that adding traditional CoT exemplars “does not improve reasoning performance compared to Zero-Shot CoT” and that their “primary function is to align the output format with human expectations.”

#### F3: PARTIALLY_SUPPORTED

- Claim: The classic positive result and the newer formatting result use different baselines, which explains much of their apparent contradiction.
- Sources: S20, S27, S25, S5
- Rationale: The sources support that the classic study reported substantial gains for few-shot CoT relative to standard prompting, while newer work reports that CoT exemplars mainly align output format and do not improve reasoning for recent strong models. However, the saved text does not explicitly establish that the studies use different baselines in a way that explains “much” of the contradiction. S5 mentions differing benchmarking approaches and thresholds, but does not directly connect that difference to the classic-versus-newer result.
- Supporting text: S20/S27: CoT prompting is reported to outperform standard prompting, including 58% on GSM8K versus a 15% standard-prompting result in the cited figure. S25: for recent strong models, traditional CoT exemplars do not improve reasoning performance and their primary function is to align output format. S5: “Perceived performance is critically affected by the benchmarking approach,” and the study compares direct, step-by-step, and default conditions using multiple accuracy thresholds.

#### F4: SUPPORTED

- Claim: Final-answer accuracy and faithful reasoning are distinct outcomes; a correct answer does not establish that the displayed CoT caused the answer or accurately represents the model’s computation.
- Sources: S8, S10, S18, S20
- Rationale: The cited sources collectively support both parts of the claim. S10 explicitly states that an answer can be correct even when the reasoning is incorrect. S8 discusses post-hoc reasoning and reports that faithfulness is not strongly correlated with accuracy improvement, directly separating answer performance from reasoning faithfulness. S18 and S20 describe CoT as an interpretable or human-like representation while acknowledging that this does not establish whether the neural network is actually reasoning; S20 also says the chain “can [be] interpreted as” a solution but “mimics” a step-by-step thought process. Together, these support the caution that displayed CoT need not be the causal or faithful representation of the model’s underlying computation.
- Supporting text: S10: “the answer can be correct even when the reasoning is incorrect.” S8: faithfulness “is not strongly correlated with the accuracy improvement” conferred by CoT. S18/S20: CoT may provide an “interpretable window” and “suggest” how the model arrived at an answer, but the cited limitation says this does not answer whether the network is actually reasoning; S20 says the chain “mimics” a step-by-step thought process.

#### F5: SUPPORTED

- Claim: The evidence does not support the universal claim that CoT is merely formatting.
- Sources: S25, S27, S8, S1
- Rationale: The sources provide evidence against interpreting CoT as merely formatting in all cases. S27 reports that CoT improves arithmetic and commonsense reasoning, S8 describes tasks where models rely on generated reasoning steps and finds that filler tokens do not reproduce the gains, and S1 reports accuracy improvements from structured Hi-CoT. Although S25 finds that CoT exemplars primarily align output format for recent strong models, it also notes possible benefits for weaker models, so its finding is not universal.
- Supporting text: S27: CoT enables decomposition into intermediate steps and improves performance across arithmetic and commonsense tasks. S8: AQuA and LogiQA models must rely on generated reasoning steps, while replacing CoT with filler tokens produces no accuracy increase. S1: Hi-CoT improves average accuracy by 6.2% over standard CoT.

#### F6: SUPPORTED

- Claim: Model capability and task difficulty are major moderators of CoT effectiveness.
- Sources: S20, S27, S5, S25
- Rationale: The saved sources consistently indicate that CoT effectiveness varies with model capability and task characteristics. S20 and S27 report that CoT benefits emerge particularly for sufficiently large models and improve performance on complex or multi-step reasoning tasks. S5 explicitly says effectiveness varies by model type and use case, with different effects for non-reasoning versus reasoning models and benefits on difficult questions. S25 reports that CoT exemplars may benefit weaker models but do not improve strong models, further supporting model capability as a moderator.
- Supporting text: S27: CoT benefits “only materialize with a sufficient number of model parameters (around 100B)” and apply to complex reasoning problems. S5: “its effectiveness varies significantly by model type and task.” S25: traditional CoT exemplars “may benefit weaker models” but do not enhance strong models.

#### F7: SUPPORTED

- Claim: CoT length and structure create another fault line: more reasoning steps are not automatically better.
- Sources: S14, S1
- Rationale: S14 directly supports the length claim, finding that performance initially improves as reasoning steps increase but eventually declines, with an optimal CoT length. S1 supports the structure claim by describing unstructured flat chains as redundant and stating that longer traces do not imply better reasoning; it also reports improved accuracy and shorter traces from hierarchical structure.
- Supporting text: S14: “as the number of reasoning steps increases, performance initially improves but eventually decreases” and “longer is not always better.” S1: “Longer traces do not imply better reasoning” and hierarchical CoT improves accuracy while reducing reasoning-trace length.

#### F8: SUPPORTED

- Claim: Evaluation protocol can materially change the apparent value of CoT.
- Sources: S25, S5
- Rationale: Both sources directly support the claim. S25 reports that an evaluation bias in open-source GSM8K frameworks significantly underestimated Zero-shot CoT performance, changing the comparison with Few-shot CoT. S5 states that perceived performance is critically affected by the benchmarking approach and shows that conclusions vary across metrics such as average performance, perfect accuracy, and majority correctness.
- Supporting text: S25: An evaluation bias in GSM8K “significantly underestimates the performance of Zero-shot CoT”; after correcting it, the authors reassessed Few-shot versus Zero-shot CoT. S5: “Perceived performance is critically affected by the benchmarking approach,” with CoT producing different results under average-performance versus threshold-based metrics.

#### F9: SUPPORTED

- Claim: “CoT” denotes several different interventions, not one uniform treatment.
- Sources: S6, S9, S12, S1
- Rationale: The saved sources consistently describe CoT as having multiple implementations, variants, or techniques that differ in prompting instructions, examples, sampling, structure, or automation. This directly supports the claim that “CoT” is not one uniform treatment.
- Supporting text: S6 says there is “not a single Chain of Thought prompt template” and describes “various ways to implement” it, including zero-shot, few-shot, self-consistency, contrastive, faithful, tabular, and automatic CoT. S12 calls them “several distinct variants,” including Few-Shot, Zero-Shot, and Auto-CoT. S9 lists eight distinct CoT techniques, while S1 distinguishes standard CoT, Zero-Shot CoT, Self-Consistency, Auto-CoT, and other extensions.

### Missing Citations

- None identified.

## Deterministic Checks

- `run_metadata_loads`: PASS
- `report_exists`: PASS
- `sources_present`: PASS
- `structured_report_parses`: PASS
- `report_question_matches`: PASS
- `source_ids_unique`: PASS
- `source_ids_syntactically_valid`: PASS
- `source_urls_present`: PASS
- `evidence_objects_valid`: PASS
- `confidence_values_valid`: PASS
- `citation_ids_syntactically_valid`: PASS
- `citation_ids_resolve`: PASS
- `structured_claim_evidence_available`: NOT_EVALUABLE — This run predates or does not use an evidence ledger.
- `ledger_claim_ids_unique`: NOT_EVALUABLE — Evidence ledger unavailable.
- `ledger_evidence_relationships_resolve`: NOT_EVALUABLE — Evidence ledger unavailable.
- `ledger_confidence_values_valid`: NOT_EVALUABLE — Evidence ledger unavailable.
- `ledger_evidence_ids_unique`: NOT_EVALUABLE — Evidence ledger unavailable.

## Main Weaknesses

1. R1: Define chain-of-thought prompting and distinguish it from direct answering, answer-format instructions, hidden or internal reasoning, self-consistency, tool augmentation, and other inference-time procedures.
2. R5: Separate the effects of the CoT prompt itself from effects of sampling, self-consistency or voting, longer generation, answer extraction, calculators, code, retrieval, or other external computation and scaffolding.
3. R7: Evaluate the evidential strength and comparability of the cited literature, including model versions and sizes, datasets, baselines, prompt protocols, decoding settings, metrics, uncertainty, replication, and source quality.
4. 1 cited finding(s) were not fully supported by saved evidence.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ac152f1d42cbe0f247f27e3225b834f4d7d35d3a27bade4d08806b371c248b6d`
- Candidate report hash: `585124eefa44979165eaf3eadaca72ea397d2b1099964366728a0f3c695742a9`
- LLM calls: 11
- Evaluated at: 2026-09-01T08:24:30.448604+00:00
