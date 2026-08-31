# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** inference-time-compute-scaling

**System Version:** evidence-ledger-v1

**Model:** gpt-5.6-luna

## Summary

- Overall: 79.9 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.70
- Coverage: 0.72
- Depth: 0.66
- Citation quality: 0.93
- Citation validity: 1.00
- Citation support: 0.88
- Citation completeness: 1.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report supplies a useful broad definition and several major forms, but the adjacent-intervention distinctions required by the rubric are incomplete and the mechanisms are not defined in much detail.
- Candidate evidence:
  - The report defines inference-time scaling as allocating additional computation during inference through “longer reasoning, repeated candidate generation, search, verification, retrieval, or iterative computation.”
  - It distinguishes inference-time scaling from training-time scaling by describing it as “complementary to training-time scaling.”
- Missing:
  - It does not explicitly distinguish inference-time scaling from increased model size or merely supplying more input context.
  - It does not discuss debatable boundaries, such as whether retrieval, tool use, or added context should count as inference compute scaling.
  - The taxonomy mentions retrieval and iterative computation but does not separately explain tool use, adaptive budgeting, or the operational meaning of each form. The evidence is also largely secondary.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: There is meaningful controlled evidence and appropriate qualification, especially around the primary MATH study, but the synthesis lacks the breadth and quantitative uncertainty reporting needed for full treatment.
- Candidate evidence:
  - The report cites a primary MATH study comparing test-time search and adaptive response-distribution updating against best-of-N, reporting “more than 4× efficiency improvement” and a FLOPs-matched result outperforming a 14× larger model in the evaluated setting.
  - It reports controlled findings on diminishing returns, task-dependent optimal thinking lengths, and correct answers becoming incorrect after extended reasoning.
  - It explicitly limits the conclusion to “at least some tasks” and states that universal superiority is not established.
- Missing:
  - Most cross-domain evidence is summarized vaguely as improvements on “mathematical, scientific, coding, and complex reasoning tasks,” without task-level results, baselines, sample sizes, confidence intervals, or variance.
  - The report does not clearly separate replicated findings from isolated results beyond noting that much of the evidence is concentrated in one primary MATH study.
  - The cited efficiency and benchmark effects are not fully contextualized with exact budgets, evaluation protocols, or uncertainty.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report covers several principal mechanisms and concrete failure modes, particularly revision, resampling, search, verification, and adaptive allocation. Treatment is strongest for the MATH/PaLM-2 setting and thinner for retrieval, tools, aggregation, and general mechanism-level comparisons.
- Candidate evidence:
  - The report distinguishes sequential revision, parallel resampling, and tree search with process-based verifiers.
  - It reports that revision may work better on easier problems, while resampling or verifier-guided search may be favored on harder problems.
  - It identifies verifier overfitting, static-verifier limitations, unfaithful traces manipulating judges, and rollout-cost disadvantages for lookahead search.
  - It discusses adaptive stopping and strategy selection as distinct ways to allocate compute.
- Missing:
  - Serial reasoning length is treated mainly through overthinking and diminishing returns, without a fuller comparison with the other mechanisms.
  - Repeated sampling is not analyzed in depth, including correlated samples or aggregation failure modes.
  - Retrieval, tool use, and iterative/agentic refinement are mentioned but not substantively compared or evaluated.
  - Error propagation and the conditions under which refinement or verification fails are only partially addressed.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: It directly addresses monotonicity, diminishing returns, saturation, and degradation and appropriately avoids a universal law. The empirical basis remains narrow and strategy-specific.
- Candidate evidence:
  - The report states that the relationship between reasoning-token budget and accuracy is “not reliably monotonic.”
  - It reports diminishing marginal returns, task-dependent optimal thinking lengths, correct-to-incorrect answer changes after extended reasoning, and a secondary report of plateaus around 100 samples.
  - It notes that patterns depend on prompt difficulty and base model and rejects universal superiority or a general scaling law.
- Missing:
  - The report does not provide a systematic characterization of saturation or degradation across multiple models, strategies, budgets, and task families.
  - The plateau claim relies on a weak secondary source, and the primary non-monotonicity evidence is concentrated in one study.
  - It does not clearly distinguish scaling behavior for serial length, sampling count, search depth, and verifier computation.

### R5

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes the central trade-off and includes one important compute-matched comparison, but realistic resource evaluation and alternatives are too thin for more than partial coverage.
- Candidate evidence:
  - The report identifies an accuracy-versus-cost and latency trade-off, including increased reasoning-token usage, latency, inference cost, and reduced throughput.
  - It reports a “more than 4× efficiency improvement” over best-of-N and a FLOPs-matched result outperforming a 14× larger model in one evaluated setting.
  - It explicitly says no standardized comparison against training-time or model scaling exists across matched budgets.
- Missing:
  - The qualitative cost discussion does not provide systematic measurements of tokens, FLOPs, latency, throughput, energy, or monetary cost across workloads.
  - The larger-model comparison is only one study and setting; deployment assumptions and matching conditions are not explained in enough detail.
  - The report does not adequately assess when extra inference is preferable to a larger or differently trained model, beyond identifying that the general comparison is unresolved.
  - It does not discuss serving constraints such as concurrency, batching, memory, or latency targets in a concrete way.

### R6

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report appropriately flags limited generalization and identifies some evaluated domains, but it does not perform the broad transfer assessment required by the rubric.
- Candidate evidence:
  - The report limits several findings to “studied settings” and says generalization across “models, domains, languages, prompting protocols, and budget ranges” is unresolved.
  - It identifies evidence on mathematical, scientific, coding, and complex reasoning tasks, while warning against universal conclusions.
  - It notes that the evidence is concentrated in MATH and a PaLM-2 setting and that adversarial or distribution-shifted reliability is not quantitatively established.
- Missing:
  - There is little actual assessment of transfer to knowledge-intensive/open-domain reasoning, planning, interactive or tool-using tasks, ambiguous tasks, safety-relevant workloads, or real-world data.
  - Languages, proprietary versus open models, and synthetic versus naturalistic evaluations are not substantively compared.
  - The report lists cross-domain gaps but does not characterize what evidence exists or how effects differ outside mathematics.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is one of the stronger sections: it clearly marks conditional and speculative claims and identifies important evidence limitations. Full coverage is withheld because several rubric-specified threats and evidence-needed prescriptions are absent or only implicit.
- Candidate evidence:
  - The report distinguishes high-, medium-, and low-confidence findings and explicitly labels the repeated-sampling numerical claims as too weakly evidenced for a reliable general conclusion.
  - It identifies concentrated primary evidence, reliance on secondary summaries, absent independent verification records, and unresolved generality of overthinking and optimal stopping.
  - It lists unresolved issues involving model scaling comparisons, verifier gaming, distribution shift, adaptive allocation, strategy selection, and reliability.
  - It notes that the research stopped at a maximum iteration limit and that no independent verification records are present.
- Missing:
  - It does not explicitly discuss benchmark contamination, selective reporting, weak baselines, or prompt/dataset limitations in concrete terms.
  - It does not discuss independence or replication in enough detail beyond saying that some sources are secondary and evidence is concentrated.
  - It gives few specific proposals for what experiments or evidence would resolve each open question.
  - Incomplete compute accounting is mentioned indirectly through lack of standardized comparisons, but not analyzed explicitly.

### R8

- Coverage: 1.00
- Depth: 0.75
- Rationale: The report answers the question directly with a conditional and uncertainty-preserving synthesis. It is substantially complete, though its depth is limited by the narrow evidence base and could make replication and generalization distinctions more explicit.
- Candidate evidence:
  - The conclusion states that extra inference computation improves reasoning “on at least some tasks,” that adaptive allocation can outperform uniform allocation in studied settings, and that strategy choice depends on difficulty and base model.
  - It separately identifies diminishing returns and overthinking as supported in at least one primary study.
  - It explicitly marks universal scaling laws, universal best methods, superiority over training/model scaling, and reliable verification under shift or adversarial conditions as unresolved.
  - It gives a balanced conclusion rather than endorsing or dismissing inference-time scaling wholesale.
- Missing:
  - The conclusion could more explicitly distinguish the strongest replicated evidence from single-study findings and secondary reports.
  - It could summarize the major domain-coverage limitation more directly, especially the thin evidence outside mathematics and related benchmark settings.

### Novel Value

- The report offers a bounded synthesis rather than a blanket claim: benefits are empirically supported in selected reasoning settings, while universal scaling laws and cross-domain superiority remain unestablished.
- It usefully emphasizes non-monotonicity and overthinking, difficulty-dependent allocation, and verifier reliability as central qualifications.
- It identifies a particularly concrete compute-matched result—more than 4× efficiency over best-of-N and performance exceeding a 14× larger model in one evaluated setting—while warning against generalizing it.

## Citations

### Support

#### F1: PARTIALLY_SUPPORTED

- Claim: Inference-time compute scaling is a broad family of methods that allocates additional inference resources through longer reasoning, repeated candidate generation, search, verification, retrieval, or iterative computation. The supplied sources present it as complementary to training-time scaling.
- Sources: S4, S5, S7, S8
- Rationale: The sources strongly support the definition as a broad family that spends additional compute during inference, including longer reasoning, multiple candidates or sampling, search, verification, and iterative refinement. They also support that inference-time and training-time scaling can be used together or are complementary. However, “retrieval” is not identified in the supplied text as an inference-time scaling method; S8 only mentions RAG in navigation and enterprise contexts without explaining it as part of the definition. Therefore, the full claim is only partially supported.
- Supporting text: S5 calls inference-time scaling an “umbrella term for methods that allocate more compute and time during inference” and lists chain-of-thought, self-consistency, best-of-N, rejection sampling with a verifier, self-refinement, and search over solution paths. S7 similarly lists chains of thought, revising answers, external verifiers, backtracking, and multiple sampling. S4 describes thinking longer, trying more candidate solutions, searching/verifying, and looping. S5 says it is “even better to do both” training and additional inference scaling; S8 explicitly states that the two are “complementary ones.”

#### F2: SUPPORTED

- Claim: Additional inference-time compute has been empirically shown to improve performance on at least some reasoning tasks, particularly in controlled mathematical-reasoning evaluations; one primary study also reports efficiency and compute-matched advantages over larger models in its evaluated setting.
- Sources: S9, S1, S3, S5, S6, S7, S8
- Rationale: S9 directly reports controlled experiments on the MATH benchmark showing that compute-optimal test-time scaling improves performance, is more than 4× more efficient than a best-of-N baseline, and can outperform a 14× larger model in a FLOPs-matched evaluation. The other sources provide corroborating, though generally less primary or less controlled, descriptions that additional inference computation improves reasoning performance. The claim is appropriately limited to at least some tasks and to S9’s evaluated setting.
- Supporting text: S9: “Using this compute-optimal strategy, we can improve the efficiency of test-time compute scaling by more than 4× compared to a best-of-N baseline.” It also reports: “in a FLOPs-matched evaluation, we find that ... test-time compute can be used to outperform a 14× larger model,” based on experiments on the MATH benchmark.

#### F3: SUPPORTED

- Claim: The relationship between reasoning-token budget and accuracy is not reliably monotonic in the supplied evidence: higher budgets can yield diminishing returns, and extended reasoning can cause a previously correct answer to become incorrect.
- Sources: S1, S6, S4, S5
- Rationale: S1 directly supports both key points: marginal returns diminish at higher reasoning-token budgets, and extended reasoning can lead a model to abandon a previously correct answer. S6 additionally describes performance plateauing with more samples, while S4 and S5 provide general context that additional inference compute often improves performance; they do not contradict S1.
- Supporting text: S1 states that “marginal returns diminish substantially at higher budgets” and describes “overthinking,” where extended reasoning is associated with abandoning previously correct answers.

#### F4: SUPPORTED

- Claim: Uniformly assigning the same reasoning budget to every problem is suboptimal in the supplied studies; difficulty-dependent stopping or strategy selection can reduce computation while maintaining comparable accuracy.
- Sources: S1, S9, S10
- Rationale: S1 explicitly states that optimal thinking length varies by problem difficulty, making uniform compute allocation suboptimal, and reports that stopping at moderate budgets can significantly reduce computation while maintaining comparable accuracy. S9 supports difficulty-dependent strategy selection and adaptive per-prompt allocation, reporting more than 4× improved efficiency over a best-of-N baseline. S10 independently summarizes difficulty-based allocation and reports substantially less compute, including up to a 4× reduction, while describing adaptive strategy selection.
- Supporting text: S1: “optimal thinking length varies across problem difficulty,” so “uniform compute allocation is suboptimal”; “stopping at moderate budgets can reduce computation significantly while maintaining comparable accuracy.” S9: effectiveness varies with prompt difficulty, motivating a strategy that “allocate[s] test-time compute adaptively per prompt.” S10: “Compute-Optimal Scaling” dynamically selects allocation by prompt difficulty and achieves “up to a 4x reduction in some cases.”

#### F5: SUPPORTED

- Claim: The effectiveness of a scaling strategy depends strongly on prompt difficulty and base model: revision may be favored on easier problems, while independent resampling or process-verifier-guided search may be favored on harder problems requiring exploration.
- Sources: S9, S10
- Rationale: Both sources directly support the claim. S9 explicitly states that strategy efficacy depends critically on problem nature and the base LLM, with iterative revision more effective on easier problems and independent resampling or process-based-reward-model tree search more effective on difficult problems requiring multiple high-level approaches. S10 independently summarizes the same difficulty-dependent tradeoff.
- Supporting text: S9: “the efficacy of a particular test-time compute strategy depends critically on both the nature of the specific problem at hand and the base LLM used.” It says easier problems may favor “iteratively refine[d]” answers, while harder problems may favor “re-sampling new responses independently in parallel or deploying tree-search against a process-based reward model.”

#### F6: SUPPORTED

- Claim: Verification is a central bottleneck and reliability concern for inference-time reasoning systems. The evidence indicates sensitivity to prompt difficulty, possible verifier overfitting, limitations of static verifiers, and vulnerability to unfaithful reasoning traces manipulating judges; it does not establish the general prevalence or severity of these risks.
- Sources: S3, S9, S10, S7
- Rationale: The cited sources collectively support the claim’s important factual content. S3 explicitly describes verification as a central challenge, static verifiers as a bottleneck, and unfaithful traces that manipulate verifiers. S9 reports that test-time strategies involving verifiers vary critically with prompt difficulty. S10 reports that beam search can overfit to the process reward model. The sources describe specific findings and failure modes, not their general prevalence or severity, consistent with the claim’s qualification.
- Supporting text: S3: verification is a “central challenge”; static discriminative verifiers “become a bottleneck”; agents can produce “unfaithful reasoning traces” that manipulate verifiers into accepting suboptimal actions. S9: strategy effectiveness “critically varies depending on the difficulty of the prompt.” S10: beam search “can overfit to the PRM.”

#### F7: SUPPORTED

- Claim: Repeated sampling and verification may produce substantial gains and approximately log-linear improvement before plateauing, but the supplied numerical claims are too weakly evidenced for a reliable general conclusion.
- Sources: S6
- Rationale: S6 explicitly states that repeated sampling and verification can increase coding performance by up to 40%, that performance scales log-linearly with the number of samples, and that verification methods plateau after approximately 100 samples. The wording appropriately qualifies these points as possible effects and notes that the numerical evidence is weak: the snapshot is a LinkedIn post summarizing a paper rather than presenting the paper’s underlying methods or results. Thus, the claim’s cautious conclusion is supported.
- Supporting text: The post says repeated sampling and verification can improve coding performance “by up to 40%,” that “performance scales log-linearly with number of samples,” and that verification methods “plateau after ~100 samples.”

#### F8: PARTIALLY_SUPPORTED

- Claim: Inference-time scaling creates a practical accuracy-versus-cost and latency trade-off because longer reasoning and repeated generation increase per-request computation and can reduce serving throughput.
- Sources: S6, S8
- Rationale: The sources support the accuracy-versus-cost/latency trade-off and increased per-request computation. S8 explicitly identifies latency and inference cost as bottlenecks, says costs are incurred per inference, and describes longer reasoning and multiple sampling passes. S6 supports repeated generation increasing performance and says the right balance between performance and cost must be found; a comment also mentions efficiency and requiring more tokens per second for adequate speed. However, the saved text does not directly establish that these techniques reduce serving throughput, so that portion is unsupported.
- Supporting text: S8: Inference-time scaling increases computation during response generation; its bottlenecks are “Latency and inference cost,” with costs “incurred per inference.” S6: repeated sampling can improve performance, and users should “find the right balance between performance and cost.”

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
- `structured_claim_evidence_available`: PASS
- `ledger_claim_ids_unique`: PASS
- `ledger_evidence_relationships_resolve`: PASS
- `ledger_confidence_values_valid`: PASS
- `ledger_evidence_ids_unique`: NOT_EVALUABLE — Current ledger relations have no independent evidence-ID field.

## Main Weaknesses

1. R5: Evaluate inference scaling against realistic resource constraints and alternatives.
2. R6: Assess how well reported inference-scaling effects transfer beyond the settings in which they were measured.
3. R1: Define inference-time compute scaling and distinguish its main forms from adjacent interventions.
4. 2 cited finding(s) were not fully supported by saved evidence.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `d32d6ea1035324f019e9421c7b216e4501bdab866df8e60cda19db2afb8a4c2f`
- Candidate report hash: `db50ecace99e36b880a7b6a3dd656770cb13ad707330515259b98096bc4dc33e`
- LLM calls: 11
- Evaluated at: 2026-08-31T21:48:56.106598+00:00
