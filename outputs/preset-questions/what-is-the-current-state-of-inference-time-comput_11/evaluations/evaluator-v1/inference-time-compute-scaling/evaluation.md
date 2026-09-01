# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** inference-time-compute-scaling

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 73.8 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.61
- Coverage: 0.66
- Depth: 0.50
- Citation quality: 0.91
- Citation validity: 1.00
- Citation support: 0.83
- Citation completeness: 1.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.00
- Depth: 0.00
- Rationale: The report uses the term and names several mechanisms, but it provides no actual scope or definition section and does not make the requested distinctions.
- Candidate evidence:
- Missing:
  - The report does not define inference-time compute scaling explicitly.
  - It does not distinguish serial reasoning, parallel sampling, search, verification, refinement, tool use, or adaptive budgeting from training changes, model-size changes, or additional input context.
  - It does not discuss debatable boundaries of the concept.

### R2

- Coverage: 0.75
- Depth: 0.50
- Rationale: The candidate synthesizes positive and conditional evidence across focused and broad evaluations, but the empirical comparisons are mostly summarized at a high level rather than reported with the quantitative and uncertainty detail required for deep treatment.
- Candidate evidence:
  - Finding 1 reports a focused mathematical study of process-reward-model search and adaptive response-distribution updates, including improved test-time scaling and more than 4× efficiency over best-of-N in the tested setting.
  - Finding 1 also reports a broader evaluation of nine models across eight task types with improvements but heterogeneous benefits.
  - Finding 2 states that more tokens do not necessarily improve accuracy and that token usage varies among similarly accurate models.
- Missing:
  - The report gives few concrete accuracy effect sizes, confidence intervals, or variance estimates.
  - It does not describe the controlled baselines, budgets, model identities, or task-level results in enough detail to assess comparability.
  - Replication and separation of replicated patterns from isolated findings are discussed only generally in the gaps section.

### R3

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report identifies the main mechanism families and several conditional limitations, but it does not provide a mechanism-by-mechanism account of failure modes with enough empirical specificity.
- Candidate evidence:
  - Finding 4 distinguishes PRM-guided search, adaptive updates, revision, sampling, independent generations, aggregation, and sequential feedback, and states that their effectiveness varies by difficulty and task.
  - Finding 2 contrasts purposeful allocation with simply generating longer chains of thought.
  - The conflicts section notes that PRM- and MCTS-based approaches were unsuccessful in one development context while other evidence reports positive results.
  - Finding 6 explains that perfect verifiers and strong feedback can produce gains but may not be deployable.
- Missing:
  - Correlated samples are not explicitly analyzed as a limitation of repeated sampling or aggregation.
  - Error propagation in sequential reasoning or feedback is not discussed.
  - The report does not give a sufficiently detailed comparison of search, verification, refinement, and adaptive allocation conditions of success and failure.
  - The requested possibility of non-monotonic degradation from excessively long reasoning is only indirectly suggested by 'more tokens do not necessarily yield higher accuracy,' not examined directly.

### R4

- Coverage: 0.75
- Depth: 0.50
- Rationale: It correctly rejects a universal law and covers diminishing and conditional gains, but the characterization of the shape of scaling behavior remains incomplete and largely qualitative.
- Candidate evidence:
  - Finding 3 reports diminishing returns as problems become more complex and says effects vary across math, STEM, planning, navigation, spatial reasoning, and NP-hard problems.
  - Finding 2 states that longer generations can indicate struggle and that more tokens alone do not necessarily improve accuracy.
  - Finding 8 explicitly says there is no established universal quantitative inference-time scaling law and attributes variation to task, difficulty, model, verifier quality, and allocation strategy.
  - The conclusion says gains can diminish with problem difficulty.
- Missing:
  - The report does not systematically distinguish monotonic improvement, saturation, and actual performance degradation across budgets.
  - It supplies no accuracy-versus-compute curves, saturation points, or uncertainty intervals.
  - Variation by model capability and by specific budget range is asserted more than demonstrated with quantitative evidence.

### R5

- Coverage: 0.75
- Depth: 0.50
- Rationale: The candidate recognizes realistic systems constraints and includes one important FLOPs-matched comparison, but the efficiency analysis is not sufficiently quantitative or broad for full coverage.
- Candidate evidence:
  - Finding 5 reports a FLOPs-matched evaluation in which a smaller model with additional test-time computation outperformed a model 14 times larger on tasks where the smaller model already had nontrivial success.
  - Finding 9 identifies token-use and cost nondeterminism and reports KV-cache, memory, latency, throughput, and parallelism trade-offs for long reasoning traces.
  - The conclusion states that the evidence is too thin to claim broad replacement of parameter scaling or predictable deployment economics.
- Missing:
  - Most comparisons do not provide matched token, latency, energy, monetary-cost, throughput, or hardware conditions.
  - The report does not quantitatively compare inference scaling with additional training or differently trained models beyond the limited parameter-scaling example.
  - Deployment assumptions, concurrency, service pricing, and quality-per-cost trade-offs are not worked through in detail.

### R6

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report goes beyond mathematics into several structured domains and explicitly marks important gaps, but it does not adequately cover the broader generalization categories in the rubric.
- Candidate evidence:
  - Finding 7 reports evidence across calendar planning, navigation, spatial reasoning, NP-hard problems, mathematics, and STEM, with unequal benefits across domains.
  - The remaining gaps explicitly identify coding, factuality, open-ended reasoning, agentic workflows, and real-world applications as insufficiently supported.
  - The report notes that Table-R1 does not isolate deployment-time compute from post-training effects.
- Missing:
  - Coding is mentioned as a gap but not evaluated.
  - There is little or no analysis of knowledge-intensive/open-domain reasoning, interactive tool use, safety-relevant workloads, languages, or ambiguous tasks.
  - The report does not distinguish proprietary from open models or synthetic from naturalistic evaluations in a substantive way.
  - Transfer beyond benchmark settings is stated to be incomplete but not assessed with detailed evidence.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is one of the strongest parts of the report: it clearly marks conditional and speculative claims and identifies substantial evidence limitations. Several rubric-specific threats to validity and a concrete resolution agenda remain absent.
- Candidate evidence:
  - The report labels findings with confidence levels and repeatedly qualifies claims as conditional rather than universal.
  - The conflicts section discusses disagreement about PRM-guided search and MCTS, the difference between token length and useful computation, perfect-verifier upper bounds, confounding from post-training, and limited systems evidence.
  - The remaining gaps identify missing accuracy-versus-compute curves, imperfect-verifier evidence, independent replications, inconsistent compute accounting, nonstandardized deployment metrics, and limited real-world evidence.
  - Finding 8 explicitly frames the absence of a universal scaling law as an evidence-gap conclusion rather than proof of impossibility.
- Missing:
  - Benchmark contamination is not discussed.
  - Selective reporting and weak baselines are not explicitly assessed.
  - The report does not consistently distinguish independent replications from multiple descriptions of the same studies.
  - It offers limited discussion of what specific future experiments or evidence would resolve each uncertainty.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The conclusion is balanced, conditional, and directly responsive, but it could synthesize the evidence-quality distinctions and domain-specific unknowns more explicitly.
- Candidate evidence:
  - The conclusion states that inference-time scaling is 'empirically validated but not yet theoretically or operationally settled.'
  - It says additional computation can materially improve reasoning when allocated adaptively and coupled to sampling, feedback, verification, or search, while more tokens alone are not dependable.
  - It limits the conclusion by noting that benefits depend on base-model competence, can diminish, and do not establish a universal law, broad replacement of parameter scaling, or predictable economics.
- Missing:
  - The conclusion could more explicitly separate established findings, plausible conditional interpretations, and areas where evidence is too thin across each major domain.
  - It does not directly summarize the especially weak evidence for coding, safety-relevant, multilingual, interactive, and naturalistic workloads.

### Novel Value

- The report offers a useful conditional synthesis that distinguishes purposeful computation from raw token length.
- It combines efficacy, mechanism, scaling-shape, deployment-cost, and evidence-quality considerations rather than treating benchmark gains as universal.
- It explicitly separates perfect-verifier upper-bound results from deployable inference-time scaling and flags confounding from post-training.

## Citations

### Support

#### F1: SUPPORTED

- Claim: Purposeful inference-time computation can improve reasoning performance, especially in mathematical and other structured problem-solving settings.
- Sources: S6, S11, S14, S15, S17, S20
- Rationale: The saved sources consistently state that allocating additional inference-time/test-time computation can improve reasoning performance. They specifically report gains for mathematical reasoning and describe benefits across structured tasks including STEM reasoning, planning, NP-hard problems, navigation, and spatial reasoning. The evidence also appropriately qualifies that benefits vary by task and diminish as complexity increases.
- Supporting text: S6/S11/S14 report that compute-optimal test-time scaling improves math-reasoning efficiency by more than 4× and can let a smaller model outperform a 14× larger one. S15/S17/S20 state that inference-time scaling enhances reasoning on complex problems, with studied tasks including math, STEM, planning, NP-hard problems, navigation, and spatial reasoning, while noting variable benefits and diminishing returns.

#### F2: SUPPORTED

- Claim: The best-supported principle is adaptive or purposeful allocation of compute, not simply generating longer chains of thought.
- Sources: S15, S17, S20, S6, S11, S14
- Rationale: The sources directly support both parts of the claim: they report that longer generations or higher token usage do not reliably improve accuracy, while explicitly motivating “more purposeful and cost-effective scaling approaches.” They also describe compute-optimal strategies that adapt allocation to prompt difficulty and report improved efficiency. S15, S17, and S20 are largely duplicate versions of the same study, while S6, S11, and S14 provide additional support for adaptive, difficulty-dependent allocation.
- Supporting text: S15/S17: “longer generations ... can sometimes be an indicator of models struggling,” and “higher token usage is not always associated with better accuracy”; these findings “motivate the need for more purposeful and cost-effective scaling approaches.” S6/S11/S14: a “compute-optimal” strategy allocates test-time compute “per prompt in an adaptive manner,” with more than 4× improved efficiency versus a best-of-N baseline.

#### F3: SUPPORTED

- Claim: Scaling behavior depends strongly on task and difficulty, with diminishing returns as problems become more complex.
- Sources: S15, S17, S20, S6, S11, S14
- Rationale: The cited sources directly support both parts of the claim. S15, S17, and S20 report that inference-time scaling effectiveness varies across tasks and diminishes as problem complexity increases. S6, S11, and S14 independently state that the effectiveness of test-time compute scaling varies critically with prompt difficulty. The evidence is specifically about inference/test-time compute scaling, which matches the claim’s scaling context.
- Supporting text: S15: “its effectiveness varies between domains and tasks, with diminishing returns as task complexity increases.” S6: “the effectiveness of different approaches to scaling test-time compute critically varies depending on the difficulty of the prompt.”

#### F4: SUPPORTED

- Claim: Different mechanisms have different strengths; no single inference-time strategy is established as uniformly best.
- Sources: S11, S13, S14, S15, S17
- Rationale: The sources consistently report that the relative effectiveness of inference-time methods depends on prompt difficulty, task/domain, and complexity. They describe different approaches performing better in different settings and motivate adaptive strategy selection, which supports the conclusion that no single strategy is uniformly best.
- Supporting text: S11/S13 state that the effectiveness of different approaches varies with prompt difficulty: parallel sampling works well on easier problems, while sequential methods or beam search help more on harder ones. S15/S17 likewise report that scaling effectiveness varies across domains and tasks and diminishes with complexity; S14 notes conflicting results across methods in prior work.

#### F5: SUPPORTED

- Claim: Inference-time compute can sometimes substitute for parameter scaling under matched compute, but only within a restricted capability regime.
- Sources: S11, S13, S14, S15, S17, S20
- Rationale: S11, S13, and S14 directly report a FLOPs-matched result in which test-time compute lets a smaller model outperform a 14× larger model, supporting substitution for parameter scaling under matched compute. They restrict this result to problems where the smaller base model already has somewhat non-trivial success rates. S15, S17, and S20 further support the qualification that benefits vary by task and diminish as problem complexity increases, with significant performance gaps remaining for some tasks even at high inference scaling.
- Supporting text: S11/S13/S14: “in a FLOPs-matched evaluation,” test-time compute outperformed a 14× larger model on problems where the smaller base model had “somewhat non-trivial success rates.” S15/S17/S20: inference-time-scaling benefits “vary across tasks” and “diminish as problem complexity increases”; for some tasks, a significant gap remains even in very high scaling regimes.

#### F6: PARTIALLY_SUPPORTED

- Claim: Perfect-verifier and strong-feedback experiments demonstrate latent potential, but they are not equivalent to present deployable performance.
- Sources: S15, S17, S20
- Rationale: The sources directly support the latent-potential portion: the experiments use perfect verifiers or strong feedback, produce significant gains, and are described as approximating upper performance bounds and potential future improvements. However, the supplied text does not explicitly state that these experiments are not equivalent to present deployable performance. It does indicate that they involve simulated or repeated-call evaluation protocols and that performance gaps remain on some tasks, which supports a narrower distinction but not the full claim as worded.
- Supporting text: S15/S17/S20 describe the evaluations as approximating “lower and upper performance bounds and potential for future performance improvements,” and report that “all models demonstrate significant gains” with “perfect verifiers or strong feedback.” S15 also calls the approaches “simulate[d]” inference-time scaling methods.

#### F7: SUPPORTED

- Claim: Evidence now extends beyond mathematics, but transfer across domains is incomplete and heterogeneous.
- Sources: S15, S17, S20, S21
- Rationale: The sources document applications beyond mathematics, including STEM reasoning, planning, NP-hard problems, navigation, spatial reasoning, and table reasoning. They also explicitly report that benefits vary across tasks and domains, that the approach does not serve all domains equally, and that significant performance gaps remain for some tasks. S21 additionally reports generalization to out-of-domain table datasets, supporting evidence of transfer while indicating it is task-specific rather than uniform.
- Supporting text: S15/S17/S20: inference-time scaling was evaluated on math plus STEM, calendar planning, NP-hard, navigation, and spatial tasks; its effectiveness “varies between domains and tasks,” and the paradigm “does not serve all domains and tasks equally.” For some tasks a significant performance gap remains even at high scaling. S21: Table-R1 shows strong generalization to out-of-domain datasets while extending scaling to table reasoning.

#### F8: PARTIALLY_SUPPORTED

- Claim: There is no established universal quantitative inference-time scaling law comparable to pretraining scaling laws.
- Sources: S15, S17, S20, S11, S14, S3
- Rationale: The sources support the narrower point that inference-time scaling behavior is not yet uniform or reliably predictable: its effectiveness varies with task and difficulty, returns can diminish, and the literature contains mixed results. S3 explicitly contrasts highly standardized pretraining scaling laws with less consistent scaling work in other settings, but it discusses RL scaling rather than directly establishing the nonexistence of a universal inference-time law. None of the saved sources directly proves the broad negative claim that no comparable universal quantitative law exists.
- Supporting text: S11/S14: “little research attempted to understand the scaling behaviors” and effectiveness “critically varies depending on the difficulty of the prompt.” S15/S17/S20: benefits “vary across tasks,” improvements diminish with complexity, and more tokens do not necessarily yield higher accuracy. S3: pretraining scaling laws are “highly standardized,” whereas related non-pretraining scaling laws are “much messier and bespoke.”

#### F9: PARTIALLY_SUPPORTED

- Claim: Deployment economics and systems behavior remain important constraints rather than settled engineering details.
- Sources: S15, S17, S20, S4
- Rationale: The sources strongly support that inference-time scaling creates unresolved systems constraints and cost trade-offs: benefits vary by task, returns diminish, token use is variable, and repeated queries can produce cost nondeterminism. S4 further describes capacity, memory, communication, routing, scheduling, and latency bottlenecks requiring different deployment strategies. However, the broader phrase “deployment economics” is only partially evidenced; the sources discuss inference cost and efficiency but do not comprehensively establish deployment economics as a whole.
- Supporting text: S15/S17 state that the work presents “performance-cost tradeoffs,” that higher token consumption does not necessarily indicate higher accuracy, and that repeated queries introduce “cost nondeterminism.” S4 describes “critical bottlenecks,” KV-cache capacity limits, communication overhead, memory thrashing, scheduler preemption, nonlinear latency spikes, and the need for nuanced combinations of parallelism strategies.

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

1. R1: Define inference-time compute scaling and distinguish its main forms from adjacent interventions.
2. R2: Synthesize controlled evidence about whether and where additional inference-time compute improves reasoning performance.
3. R3: Compare the principal inference-scaling mechanisms and their observed conditions of success or failure.
4. 3 cited finding(s) were not fully supported by saved evidence.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `d32d6ea1035324f019e9421c7b216e4501bdab866df8e60cda19db2afb8a4c2f`
- Candidate report hash: `197df2de710eb72d24fabc1ff18dbe130895c2a6d971f7e6be9e0ce619f766f4`
- LLM calls: 12
- Evaluated at: 2026-09-01T10:40:26.029716+00:00
