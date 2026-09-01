# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** inference-time-compute-scaling

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 79.6 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.70
- Coverage: 0.75
- Depth: 0.59
- Citation quality: 0.91
- Citation validity: 1.00
- Citation support: 0.88
- Citation completeness: 0.94
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report identifies several important mechanisms and distinguishes inference from at least some training interventions, but scope and definitions are incomplete and mostly implicit.
- Candidate evidence:
  - The report defines inference-time scaling operationally through “repeated sampling with aggregation, sequential feedback or revision, and verifier-guided search.”
  - It distinguishes longer reasoning from these strategies and notes that some results combine inference procedures with “supervised fine-tuning or other training changes.”
- Missing:
  - It never gives a direct, comprehensive definition of allocating additional computation during inference.
  - It does not clearly distinguish inference scaling from increased model size or merely supplying more input context.
  - Tool use is not treated as a main form, and debatable boundaries are not discussed.

### R2

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report gives a useful qualitative synthesis of controlled comparisons and conditional effects, but it lacks the quantitative evidence and replication detail needed for full treatment.
- Candidate evidence:
  - The report cites a “multi-model, multi-task evaluation covering nine models and eight tasks” that compares parallel generations with aggregation and sequential generations with feedback.
  - It reports controlled findings for best-of-N, revision, verifier-guided search, and adaptive strategies, while noting that benefits vary by task and model.
  - It explicitly distinguishes broad evidence from narrower mathematics-focused studies and warns against universal benefit.
- Missing:
  - No actual effect sizes, confidence intervals, statistical uncertainty, or variance are reported.
  - The studies and baselines are identified only by source labels and broad descriptions, making the empirical comparisons difficult to independently assess.
  - Replication and independent confirmation of the main effects are not synthesized in detail.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report covers the principal mechanisms and several important failure modes, with reasonable comparative synthesis, but the mechanism-by-mechanism empirical detail is incomplete.
- Candidate evidence:
  - It separately discusses repeated sampling and aggregation, sequential feedback or revision, verifier-guided selection/search, and difficulty-dependent adaptive allocation.
  - It identifies correlated generator/verifier errors, verifier overfitting, token-length bias, unreliable learned verifiers, and rollout costs that can hurt equal-budget performance.
  - It reports that longer generations can reflect model struggle and that some scaling approaches fail on hard combinatorial instances.
- Missing:
  - Serial reasoning length itself is discussed mainly as “longer traces,” without a detailed comparison to other serial deliberation designs.
  - Observed conditions of success and failure for each mechanism are summarized qualitatively rather than with systematic cross-mechanism evidence.
  - Adaptive allocation is called empirically motivated, but the report does not explain which stopping or allocation policies were tested and how they failed.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: It directly addresses monotonicity, diminishing returns, saturation-like behavior, and degradation, while appropriately avoiding a universal law. Quantitative characterization is thin.
- Candidate evidence:
  - It states that scaling is “not guaranteed to remain beneficial or monotonic,” with diminishing returns and cases where models abandon initially correct answers.
  - It notes that benefits depend on model, task difficulty, verifier, and budget, and that gains can diminish as problem complexity increases.
  - It explicitly rejects broad claims of a universal test-time scaling law and describes behavior as task- and method-dependent.
- Missing:
  - The report does not characterize specific scaling curves, thresholds, or budget ranges.
  - Variation by model capability and strategy is asserted but not systematically quantified.
  - The evidence for saturation versus outright degradation is not separated carefully across mechanisms and tasks.

### R5

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report recognizes the central efficiency trade-off and includes an important matched-FLOPs result, but realistic resource accounting and deployment analysis remain largely absent.
- Candidate evidence:
  - It reports smaller models outperforming larger models in selected MATH-focused studies under FLOPs-matched, compute-optimized procedures.
  - It warns that these comparisons are limited to particular datasets, verifiers, budgets, and FLOPs accounting, and that other tasks retain substantial gaps.
  - It explicitly notes that supplied sources do not establish improvements in real-world latency, throughput, or monetary cost.
- Missing:
  - There are no concrete token, FLOP, latency, energy, throughput, or dollar figures or normalized quality-cost comparisons.
  - The report does not analyze hardware utilization, parallel-versus-serial latency, batching, or serving constraints in detail.
  - Comparison with additional training or larger models is conditional but not presented through matched total-cost or ownership-cost experiments.

### R6

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report draws a clear benchmark-versus-real-world boundary and names several important untested domains, but it omits multiple rubric-specified axes of generalization.
- Candidate evidence:
  - It identifies the strongest evidence as coming from curated math, STEM, planning, navigation, spatial, and algorithmic benchmarks.
  - It explicitly says evidence is lacking for knowledge-intensive work, software engineering, interactive agents, distribution shift, and broad real-world reliability.
  - The conclusion limits claims to selected mathematical benchmarks and calls transfer to realistic interactive deployments an open question.
- Missing:
  - Languages, multilingual transfer, ambiguous tasks, and safety-relevant workloads are not substantively assessed.
  - The report does not clearly distinguish proprietary from open models or synthetic from naturalistic evaluations.
  - Transfer evidence beyond benchmark families is mostly described as absent rather than compared where it exists.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is one of the strongest parts of the report: it separates supported, conditional, and uncertain claims and identifies many gaps. Some evidence-quality issues named in the rubric are missing or only implicit.
- Candidate evidence:
  - It discusses diminishing returns, overthinking, verifier unreliability, benchmark scope, missing deployment economics, and the limited attribution of results that combine training and inference changes.
  - The “Remaining Gaps” section identifies unresolved questions about replication, adaptive stopping, realistic verifiers, overthinking prevalence, distribution shift, compute accounting, and comparisons with training/model scaling.
  - It explicitly labels real-world reliability, interactive agents, economics, and broad out-of-distribution transfer as speculative or under-evidenced.
- Missing:
  - Replication and independence are acknowledged but not investigated in detail; there is no systematic accounting of how many studies replicate each finding.
  - Benchmark contamination, prompt dependence, selective reporting, and weak baselines are not explicitly discussed in sufficient detail.
  - The report does not specify concrete evidence or experimental designs that would resolve each major uncertainty, beyond broad calls for standardized accounting and broader evaluations.

### R8

- Coverage: 1.00
- Depth: 0.75
- Rationale: It directly answers the question with a balanced, conditional synthesis, identifies both validated benefits and thin evidence, and avoids blanket endorsement. Its only limitation is that the confidence hierarchy among individual mechanisms remains somewhat compressed.
- Candidate evidence:
  - The conclusion states that inference-time scaling “works” under conditions involving diverse sampling, aggregation, revision, or verified search.
  - It qualifies benefits by base model, task difficulty, verifier quality, and budget, and states that longer chains are unreliable and can produce diminishing or negative returns.
  - It says small-model victories do not generally replace stronger training or model capability and identifies realistic deployment, imperfect verifiers, and adaptive stopping as unresolved.
- Missing:
  - The conclusion could distinguish more explicitly between the highest-confidence replicated findings and merely plausible conditional interpretations, rather than grouping several mechanisms together.

### Novel Value

- No material benchmark-external value identified.

## Citations

### Support

#### F1: SUPPORTED

- Claim: Additional inference-time computation can improve reasoning performance, but the effect is task-, model-, verifier-, and budget-dependent rather than universal.
- Sources: S12, S17, S18, S6, S7, S9, S22, S25
- Rationale: The saved sources directly support both parts of the claim. S12, S17, and S18 report that inference-time scaling improves reasoning performance, while its effectiveness varies across tasks and diminishes with increasing complexity; they also state that more tokens do not necessarily yield higher accuracy. S22 and S25 explicitly say the compute-optimal strategy depends on the policy/model, verifier (PRM), and problem difficulty. S7 and S9 further support prompt-difficulty- and strategy-dependent effects, including differing outcomes for sequential, parallel, and verifier-guided methods and diminishing or negative gains in some settings.
- Supporting text: S12/S17: “Although inference-time scaling improves performance, its effectiveness varies between domains and tasks, with diminishing returns as task complexity increases”; “simply using more tokens does not necessarily translate to higher accuracy.” S22/S25: “The compute-optimal TTS strategy is highly dependent on the choice of policy model, PRM, and problem difficulty.” S9: strategy efficacy varies significantly by prompt difficulty, and some methods can perform worse at higher budgets.

#### F2: SUPPORTED

- Claim: The best-supported methods are repeated sampling with aggregation, sequential feedback or revision, and verifier-guided selection or search—not simply forcing longer chains of thought.
- Sources: S17, S18, S6, S7, S9, S12
- Rationale: The saved sources directly describe independent repeated generations followed by aggregation, sequential generations using feedback for another opportunity to improve, and verifier- or process-reward-model-guided selection/search. They also explicitly caution that longer generations or higher token usage do not necessarily improve accuracy. Although “best-supported” is a synthesis rather than a quoted ranking, the cited evidence supports the substantive comparison.
- Supporting text: S12/S17 report independent parallel generations that sample multiple answers and aggregate them; sequential generations that use feedback to improve an answer; and consistent gains from perfect verifiers. S6/S7/S9 describe dense/process verifiers, adaptive search, iterative revision, best-of-N, beam search, and lookahead search. S12 states that longer generations can indicate struggle and that higher token consumption does not indicate higher accuracy.

#### F3: SUPPORTED

- Claim: Longer reasoning traces are not a reliable proxy for better reasoning, and inference scaling is not guaranteed to be monotonic.
- Sources: S17, S18, S2
- Rationale: The cited sources directly support both parts of the claim. S17 and S18 report that higher token use does not necessarily correspond to higher accuracy and that longer generations can indicate struggling rather than improved reflection. S2 explicitly challenges the assumption that thinking length and answer quality are monotonically related, reporting diminishing returns and overthinking that can turn correct answers into incorrect ones.
- Supporting text: S17: “longer generations ... can sometimes be an indicator of models struggling” and “higher token usage is not always associated with better accuracy.” S18: “longer scratchpads do not guarantee higher accuracy.” S2: “the assumption that thinking length and answer quality are monotonically related” is challenged; extended reasoning can involve abandoning previously correct answers.

#### F4: PARTIALLY_SUPPORTED

- Claim: Difficulty-dependent allocation is empirically motivated in benchmark settings, but reliable adaptive stopping and production-grade cost optimization have not been demonstrated.
- Sources: S9, S22, S25, S17, S18, S2, S6, S7, S11
- Rationale: The sources strongly support the first part: benchmark experiments report that optimal test-time compute or strategy depends on prompt/problem difficulty, and that adaptive allocation can improve efficiency. They also support important limitations: scaling benefits vary by task and complexity, token use is nondeterministic, and more computation does not always improve accuracy. However, the supplied text does not establish the broad negative claim that reliable adaptive stopping and production-grade cost optimization have not been demonstrated. S2 explicitly reports early-stopping exploration and cost-aware evaluation, while the other sources do not provide a systematic production-deployment assessment. S11 discusses production inference economics but does not evaluate difficulty-adaptive stopping.
- Supporting text: S9: “dynamically selecting the test-time compute allocation based on an estimate of the prompt's difficulty”; S22: “The compute-optimal TTS strategy is highly dependent on ... problem difficulty”; S17/S18: scaling benefits vary and diminish with complexity, while token usage is highly variable and higher consumption does not ensure higher accuracy; S2: “stopping at moderate budgets can reduce computation significantly while maintaining comparable accuracy.”

#### F5: PARTIALLY_SUPPORTED

- Claim: Perfect-verifier experiments demonstrate substantial potential headroom, but realistic learned verifiers may not realize that potential and can select systematically wrong solutions.
- Sources: S16, S17, S18, S9, S22, S24
- Rationale: S16–S18 directly support substantial headroom: scaling with perfect verifiers produces significant gains, and conventional models can approach advanced reasoning models on some tasks while retaining large gaps on others. S24 supports limitations of realistic learned verifiers, reporting PRM over-criticism, error neglect, and token-length bias that affect performance. However, the supplied text does not clearly establish that learned verifiers select “systematically wrong solutions”; it reports biases and degraded performance, which supports a narrower claim about verifier unreliability. S9 discusses verifier overfitting but does not specifically document systematic selection of wrong solutions.
- Supporting text: S17: “all models demonstrate significant gains when inference is further scaled with perfect verifiers or strong feedback, suggesting ample potential for future improvements.” S24: “PRM limitations: Observed over-criticism, error neglect, and token-length bias in PRMs, impacting TTS performance.”

#### F6: SUPPORTED

- Claim: Small models can sometimes outperform much larger models under carefully matched and optimized inference compute, but this does not establish that inference scaling generally replaces model scaling or training.
- Sources: S6, S7, S21, S22, S25, S16, S17, S20
- Rationale: The sources directly support the qualified performance claim: S7 reports a FLOPs-matched evaluation in which test-time compute let a smaller base model outperform a 14× larger model, while S22 and S25 report compute-optimal TTS allowing 1B or 3B models to exceed 405B models on specified math benchmarks. The qualification that this is conditional is also supported: S22 says the optimal strategy depends heavily on the policy model, verifier, and problem difficulty, while S16 and S17 report task-dependent benefits, diminishing returns, and persistent gaps on some tasks. S20 explicitly states that models usually combine substantial training and inference compute, supporting the conclusion that the evidence does not show inference scaling generally replaces training or model scaling.
- Supporting text: S7: “In a FLOPs-matched evaluation… on problems where a smaller base model attains somewhat non-trivial success rates, test-time compute can be used to outperform a 14x larger model.” S22: “The compute-optimal TTS strategy is highly dependent on the choice of policy model, PRM, and problem difficulty.” S17: inference-time benefits “vary between domains and tasks” and “diminish as problem complexity increases”; some performance gaps remain even at very high scaling. S20: LLMs are usually improved by “combining” heavy train-time compute and increased test-time compute.

#### F7: SUPPORTED

- Claim: No single inference-time strategy dominates uniformly.
- Sources: S15, S22, S25
- Rationale: S15 states the claim directly and provides examples of different strategies leading on different task types. S22 and S25 independently support the broader conclusion by reporting that the compute-optimal strategy depends on the policy model, verifier/PRM, and problem difficulty, implying that no strategy is uniformly best.
- Supporting text: S15: “The findings reveal that no single strategy dominates uniformly.” It further reports that PRM-guided selection leads on arithmetic and compositional tasks, while multi-agent debate leads on object counting. S22/S25: “The compute-optimal TTS strategy is highly dependent on the choice of policy model, PRM, and problem difficulty.”

#### F8: SUPPORTED

- Claim: The evidence is strongest for curated reasoning benchmarks; broad claims about real-world reliability, interactive agents, distribution shift, and economics remain speculative or under-evidenced.
- Sources: S6, S7, S17, S18, S22, S11, S27
- Rationale: The sources primarily report inference-time-scaling results on curated benchmarks, especially MATH, AIME24, and other structured reasoning tasks. S17 and S18 explicitly state that prior work focuses largely on math benchmarks, that effects vary by task and diminish with complexity, and that some tasks retain substantial performance gaps even under high scaling. The sources mention agents and practical or economic implications, but largely as potential, commentary, or context rather than direct evidence about real-world reliability, interactive-agent performance, distribution shift, or validated economics. S11 is a general 2026 cost/latency guide and does not substantiate the claimed benchmark-versus-real-world evidentiary distinction.
- Supporting text: S6: evaluations focused on the MATH dataset and high-school competition problems. S17: “the broader impact ... on other tasks remains less clear”; benefits “vary across tasks and diminish as problem complexity increases.” S7: the presenter cautions that extracted general rules “probably will not generalize super well to other problems, other domains or even other benchmark data sets.” S27 discusses possible applications and economic tradeoffs, but frames them as implications and likely incentives rather than direct validation.

### Missing Citations

- Q17: The report identifies adaptive stopping, realistic verifier performance, transfer to interactive and distribution-shifted settings, standardized cost accounting, and comparisons with additional training as unresolved research gaps.

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

1. R1: Define inference-time compute scaling and distinguish its main forms from adjacent interventions.
2. R2: Synthesize controlled evidence about whether and where additional inference-time compute improves reasoning performance.
3. R5: Evaluate inference scaling against realistic resource constraints and alternatives.
4. 2 cited finding(s) were not fully supported by saved evidence.
5. 1 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `d32d6ea1035324f019e9421c7b216e4501bdab866df8e60cda19db2afb8a4c2f`
- Candidate report hash: `8683c5505010929c2b03404f6a86f807a8cf10faa7831f557ab3bf4c6ad66c52`
- LLM calls: 10
- Evaluated at: 2026-09-01T08:25:30.731737+00:00
