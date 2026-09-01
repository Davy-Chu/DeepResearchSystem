# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** inference-time-compute-scaling

**System Version:** evidence-ledger-decomposer-v1

**Model:** gpt-5.6-luna

## Summary

- Overall: 74.8 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.68
- Coverage: 0.72
- Depth: 0.59
- Citation quality: 0.80
- Citation validity: 1.00
- Citation support: 0.83
- Citation completeness: 0.63
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.75
- Depth: 0.50
- Rationale: The taxonomy and core definition are substantially covered, but the requested separation from adjacent interventions is only implicit or absent.
- Candidate evidence:
  - The report defines inference-time scaling as “allocating additional computation during inference without changing model weights.”
  - It enumerates longer reasoning traces, multiple-sample decoding, self-consistency, search, verification, reranking, refinement, retrieval/tool-like loops, and adaptive stopping or allocation.
  - It distinguishes fixed-budget versus adaptive and parallel, sequential, or hybrid methods.
- Missing:
  - It does not explicitly distinguish inference-time scaling from increased model size, training or fine-tuning changes, or merely supplying more input context.
  - It does not discuss which boundaries are debatable, especially for retrieval, tools, controllers, or trained verifiers.

### R2

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report gives a credible conditional synthesis and some effect sizes, but the empirical evidence is not sufficiently detailed or comparative for deep coverage.
- Candidate evidence:
  - The report cites evaluations varying reasoning budgets up to 16,000 tokens and a study covering 30 LLMs and common reasoning datasets.
  - It reports selected quantitative comparisons, including Adaptive Parallel Reasoning versus serialized chain-of-thought and self-consistency on Countdown.
  - It explicitly states that selected improvements do not establish a universal model- or task-independent scaling law and notes incomplete replication and protocols.
- Missing:
  - Most evidence is described without model identities, task-by-task baselines, uncertainty, variance, or complete numerical outcomes.
  - The synthesis of replicated versus isolated findings is limited; the report acknowledges narrow and secondary evidence but does not establish which effects have independent replication.
  - The controlled comparisons are concentrated in a few settings rather than systematically synthesized across strategies and budgets.

### R3

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report identifies the principal mechanisms and several limitations, but it does not provide a sufficiently granular comparative account of their observed operating conditions.
- Candidate evidence:
  - The taxonomy distinguishes longer reasoning, repeated sampling/self-consistency, search, verification, refinement, retrieval/tool loops, and adaptive allocation.
  - It reports diminishing returns and overthinking for longer reasoning, aggressive-search degradation in some settings, task-specific adaptive-parallel benefits, and verifier/LLM-judge reliability problems.
  - It states that adaptive allocation and verification remain active but generally unestablished approaches.
- Missing:
  - The mechanisms are not compared systematically under matched conditions.
  - Correlated samples, error propagation in serial reasoning or refinement, verifier false positives/false negatives, and the specific conditions under which aggregation helps are not developed.
  - Refinement, search, and tool use receive mostly taxonomic treatment rather than mechanism-specific empirical success and failure analysis.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is one of the stronger sections: it directly addresses monotonicity, diminishing returns, degradation, conditionality, and the danger of universal laws, though quantitative characterization remains thin.
- Candidate evidence:
  - It reports diminishing marginal returns, an inverted-U relationship, correct-to-incorrect answer changes, and overthinking.
  - It also reports counterevidence of generally monotonic but sub-linear gains in some regimes.
  - It states that behavior depends on task difficulty, model, decoding procedure, and resource accounting, and rejects a universal scaling law.
- Missing:
  - Saturation is not separately characterized with evidence, and variation by model capability, budget range, and strategy is only briefly described.
  - The report does not provide a more systematic account of the shapes or transition points of scaling curves across tasks.

### R5

- Coverage: 0.50
- Depth: 0.50
- Rationale: It recognizes the relevant trade-offs and gives limited token/latency evidence, but realistic resource evaluation and alternatives are largely identified as gaps rather than analyzed.
- Candidate evidence:
  - The report notes comparable-latency and lower-compute results for adaptive parallel reasoning under particular Countdown and MATH conditions.
  - It explicitly calls for matched comparisons involving token budgets, latency, and total compute.
  - It states that substitution for model capability or training-time compute remains unestablished.
- Missing:
  - There is little actual accounting of tokens, FLOPs, throughput, energy, or monetary cost.
  - The report does not meaningfully compare extra inference with a larger model or differently trained model under matched deployment assumptions.
  - The cited efficiency results are narrow and do not establish when quality gains justify resource costs.

### R6

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report correctly marks generalization as uncertain, but it mostly lists the gap rather than evaluating transfer across the required domains and evaluation regimes.
- Candidate evidence:
  - The report explicitly says evidence is insufficient across model sizes, task types, domains, and evaluation protocols.
  - It notes that quantitative evidence is concentrated in Countdown and selected MATH settings.
  - It identifies unresolved distribution-shift and transfer questions and states that broad applicability is not established.
- Missing:
  - It does not separately assess mathematics/STEM versus coding, knowledge-intensive or open-domain reasoning, planning, interactive/tool-using tasks, ambiguous tasks, safety-relevant workloads, languages, or real-world data.
  - It does not distinguish proprietary from open models or synthetic from naturalistic evaluations in the evidence synthesis.
  - The 30-model study is mentioned, but its transfer implications cannot be assessed because results are omitted.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report is strong at marking uncertainty and unresolved questions, but it omits several requested evidence-quality threats and provides limited resolution criteria.
- Candidate evidence:
  - It repeatedly distinguishes selected empirical support from proposals, unresolved comparisons, and speculative extrapolations.
  - It discusses narrow or secondary quantitative sources, incomplete protocols, lack of independent replication, weak matched baselines, incomplete cost accounting, domain shift, verifier reliability, and limited model/task coverage.
  - Its remaining-gaps list identifies unresolved overthinking prevalence, adaptive allocation, verification, genuine reasoning versus sampling/search/retrieval gains, and training-versus-inference comparisons.
- Missing:
  - Benchmark contamination, prompt and dataset limitations, and selective reporting are not explicitly discussed.
  - The report gives few concrete examples of what new evidence or experimental designs would resolve each uncertainty.
  - The evidence-quality assessment relies on the supplied ledger and does not independently assess source quality beyond noting secondary or narrow sources.

### R8

- Coverage: 1.00
- Depth: 0.75
- Rationale: It directly answers the question with a conditional, non-universal synthesis and clearly identifies both validated effects and areas where evidence is too thin.
- Candidate evidence:
  - The conclusion calls inference-time scaling “a useful but conditional family of techniques” and identifies longer reasoning, sampling, search, and parallel/adaptive procedures as beneficial in selected evaluations.
  - It explicitly preserves the evidence for diminishing returns and occasional overthinking.
  - It states that adaptive allocation, verification, broad scaling laws, cross-domain transfer, equal-resource rankings, and substitution for training or model capability remain unestablished or insufficiently evidenced.
  - It concludes with a balanced characterization of promising empirical progress rather than a settled universal recipe.
- Missing:
  - The conclusion could more explicitly distinguish which findings are replicated versus based on narrow or secondary evidence, but it already communicates the main uncertainty structure.

### Novel Value

- The report provides a useful conditional synthesis linking validated gains, diminishing returns, overthinking, and uncertainty about adaptive allocation and verification.
- It explicitly identifies matched-resource comparisons, cross-domain transfer, and substitution for model capability as unresolved rather than extrapolating from narrow benchmark results.
- Its strongest value is evidence triage and limitation-mapping, rather than new empirical findings or a novel scaling theory.

## Citations

### Support

#### F1: SUPPORTED

- Claim: Inference-time compute scaling means allocating additional computation during inference without changing model weights. The supplied taxonomy includes longer reasoning traces, multiple-sample decoding and self-consistency, search, verification or reranking, self-refinement, retrieval or tool-like loops, and adaptive stopping or allocation. Methods can also be distinguished as fixed-budget versus adaptive, and as parallel, sequential, or hybrid.
- Sources: S1, S3, S5, S6, S7, S10, S12, S13
- Rationale: The cited snapshots directly support the definition and nearly all listed taxonomy categories. S5 explicitly describes inference-time scaling as allocating more compute during inference and identifies training-free methods that do not change model weights. S5 lists chain-of-thought, self-consistency, best-of-N, verifier-based rejection, self-refinement, and search; S3 and S7 support retrieval, search, verification, reranking, and extended reasoning. S6 explicitly distinguishes fixed-budget versus adaptive methods and classifies methods as parallel, sequential, or hybrid. S10 and S13 support adaptive allocation and early stopping. The phrase “tool-like loops” is not stated verbatim, but retrieval and iterative/agentic workflows are represented in the supplied material.
- Supporting text: S5: “allocate more compute and time during inference” and “training-free techniques that don’t change the model weights”; its overview lists self-consistency, best-of-N, verifier rejection, self-refinement, and search. S6: TTC methods are “broadly classified into Parallel and Sequential,” with hybrid methods, and distinguishes fixed L1 controllability from adaptive L2 methods. S13 describes multiple reasoning paths, adaptive sampling, and early stopping.

#### F2: SUPPORTED

- Claim: Increasing reasoning-token budgets has been empirically associated with improved accuracy on at least some reasoning tasks and models, but the supplied evidence does not establish a universal, model-independent, or task-independent scaling law.
- Sources: S1, S11, S8, S9, S6
- Rationale: The sources report accuracy improvements as inference-time computation or reasoning budgets increase in specific settings, including APR on the Countdown task and broader test-time-compute evaluations. They also describe diminishing returns, overthinking, task-difficulty dependence, and variation across models and tasks, which supports the stated limitation against treating the relationship as universal or task/model independent.
- Supporting text: S9 reports APR accuracy increasing to 80.1% at 20k total tokens on Countdown, compared with lower baselines. S1 states that research has observed accuracy improvements as token budgets increase but finds diminishing returns and overthinking, with optimal thinking length varying by problem difficulty. S6 notes trade-offs across models and tasks and says token usage does not always translate proportionally into performance.

#### F3: SUPPORTED

- Claim: Additional reasoning computation can have diminishing marginal returns and can sometimes cause overthinking, including changing a previously correct answer to an incorrect one; therefore, accuracy is not guaranteed to increase monotonically with reasoning length.
- Sources: S1, S6, S7, S8
- Rationale: S1 directly supports all key elements: diminishing marginal returns at higher reasoning budgets, overthinking involving abandonment of previously correct answers, and the challenge to monotonic accuracy improvement with thinking length. S7 independently supports sub-linear accuracy scaling and diminishing returns. S6 and S8 provide narrower supporting context about overthinking, trade-offs, and accuracy degradation under some allocation strategies.
- Supporting text: S1 states that marginal returns diminish substantially at higher budgets and that extended reasoning can involve “abandoning previously correct answers.” It also says the assumption that thinking length and answer quality are monotonically related is challenged. S7 describes “sub-linear scaling of accuracy with compute investment” and “sharply diminishing returns.” S8 reports that aggressive search may degrade accuracy for easy prompts and that revision models may erase correct context answers.

#### F4: SUPPORTED

- Claim: Uniformly assigning the same reasoning budget to every problem is not necessarily cost-optimal. The supplied evidence supports difficulty- or confidence-sensitive allocation as a promising efficiency strategy, but does not establish a generally optimal adaptive policy.
- Sources: S1, S8, S9, S6, S10, S12, S13
- Rationale: The sources directly report that optimal thinking length varies by problem difficulty and that uniform compute allocation can be suboptimal (S1). Multiple sources describe adaptive allocation based on difficulty, confidence, uncertainty, or answer concentration, with reported efficiency gains (S8, S9, S10, S12, S13). The claim appropriately characterizes these approaches as promising rather than asserting a universally optimal policy; the sources present particular methods, trade-offs, and limitations rather than establishing general optimality.
- Supporting text: S1 states that “optimal thinking length varies across problem difficulty, suggesting that uniform compute allocation is suboptimal,” and that moderate-budget stopping can reduce computation while maintaining comparable accuracy. S13 describes difficulty-adaptive sampling and confidence-informed self-consistency as reducing samples while preserving or improving accuracy; S6 identifies adaptive methods as dynamically scaling compute by difficulty or confidence.

#### F5: SUPPORTED

- Claim: Adaptive Parallel Reasoning was reported to outperform serialized chain-of-thought and self-consistency baselines on Countdown under the reviewed conditions, including higher accuracy at comparable latency and larger token budgets. This is evidence for a task-specific result, not for general dominance of parallel reasoning.
- Sources: S9
- Rationale: S9 explicitly reports APR results on the Countdown task against serialized chain-of-thought (SoS+) and self-consistency baselines. It gives higher accuracy at approximately 5,000 ms (75.2% vs. 57.3%) and at larger compute budgets (80.1% at 20k total tokens, exceeding the cited SoS+ baselines). The source limits these findings to Countdown, supporting the claim’s task-specific qualification rather than a general dominance claim.
- Supporting text: S9 reports: “Experiments on the Countdown reasoning task” showed “improved accuracy at equivalent latency (75.2% vs. 57.3% at approximately 5,000ms)” and “superior scalability with increased computation (80.1% vs. 66.6% at 20k total tokens).”

#### F6: SUPPORTED

- Claim: Verification and evaluation can be reliability bottlenecks. The supplied material reports limitations of static verifiers and susceptibility of LLM-judge evaluation to unfaithful reasoning traces or gaming, but does not characterize the prevalence or robustness of these failures across settings.
- Sources: S3
- Rationale: S3 explicitly states that static discriminative verifiers “become a bottleneck” because they cannot adapt verification compute to input complexity. It also reports that agents can produce unfaithful reasoning traces that manipulate verifiers into accepting suboptimal actions, identifying a failure mode in which agents game evaluation. The source describes these findings in the context of the thesis studies and does not provide prevalence estimates or characterize robustness across settings, so that limitation in the claim is also accurate.
- Supporting text: S3: “static discriminative verifiers become a bottleneck” because they cannot adaptively scale verification compute based on input complexity; agents can produce “unfaithful reasoning traces” that manipulate verifiers into accepting suboptimal actions, “revealing a failure mode in which agents game evaluation.”

#### F7: PARTIALLY_SUPPORTED

- Claim: The supplied evidence is insufficient to conclude how inference-time scaling transfers across model sizes, task types, domains, or evaluation protocols, or whether additional inference computation can reliably substitute for model capability or training-time compute.
- Sources: S6, S8, S9, S10, S11
- Rationale: The sources support a cautious limitation: the evidence is heterogeneous and often narrow. S9 reports APR results on the Countdown reasoning task, S8 reports MATH experiments with PaLM 2-S* and explicitly calls for extension beyond mathematical reasoning, and S6 notes imperfect controllability/adaptiveness and model/task robustness concerns. However, the supplied text also contains some direct cross-size and compute-substitution claims: S8 says a smaller model with optimal TTC can outperform a 14× larger model in certain tasks and claims additional inference compute can exceed pretraining or architecture scaling under specified conditions. S11 states that 30 LLMs and multiple model sizes were studied, though the snapshot provides no results. Therefore, the broad insufficiency claim is too strong if read as saying the evidence contains no conclusions at all; only a narrower claim about limited generalizability and lack of reliable universal substitution is supported.
- Supporting text: S8: experiments are on the MATH benchmark with PaLM 2-S*, and future work includes “extending methodology to domains beyond mathematical reasoning.” S9: experiments are conducted on the Countdown reasoning task. S6: prompting may lack “robustness across models/tasks,” and the survey reports imperfect budget control and limited adaptiveness. Conversely, S8 reports that a smaller model with optimal TTC can outperform a 14× larger model “on tasks where base model performance is nontrivial,” while S11 describes testing 30 LLMs across model sizes.

#### F8: PARTIALLY_SUPPORTED

- Claim: No reliable conclusion can currently be drawn about which inference-time scaling method dominates under equal resource constraints, because the supplied material lacks detailed, independently reproducible comparisons that match models, tasks, baselines, token budgets, latency, and total compute.
- Sources: S6, S8, S9, S10
- Rationale: The sources support the narrower conclusion that the material presents heterogeneous, method-specific comparisons rather than a comprehensive, independently reproducible ranking under uniformly matched resource constraints. S6 is primarily a survey summary; S8 and S10 make broad claims about compute-optimality and superiority; S9 reports a specific APR comparison on the Countdown task with selected token/latency conditions. However, the supplied text does not explicitly establish that no reliable conclusion can be drawn, nor does it document the absence of matching models, tasks, baselines, token budgets, latency, and total compute across all cited material.
- Supporting text: S6 describes a survey of diverse TTC methods and trade-offs. S9 reports APR results only for Countdown against particular baselines (e.g., 80.1% at 20k tokens and 75.2% at approximately 5,000 ms). S8 and S10 provide broad adaptive-allocation claims and examples, but not a standardized cross-method comparison covering all listed resource dimensions.

#### F9: PARTIALLY_SUPPORTED

- Claim: The effectiveness of reliability-aware adaptive self-consistency remains unverified in the supplied evidence. Its mechanism has been proposed, but no empirical effectiveness or robustness result is provided.
- Sources: S12
- Rationale: S12 explicitly states that Reliability-Aware Adaptive Self-Consistency (ReASC) is proposed and describes its mechanism. However, the snapshot does not provide the contents of the listed figures and tables or any explicit empirical results, so it supports the narrower observation that such results are absent from the supplied text, but does not conclusively establish that effectiveness remains unverified overall.
- Supporting text: “Reliability-Aware Adaptive Self-Consistency (ReASC) is proposed” and it reframes adaptive sampling around “evidence sufficiency,” using response-level confidence for information aggregation. The snapshot lists multiple figures and tables but supplies no accompanying empirical findings or robustness results.

### Missing Citations

- Q13: Matched, independently reproducible comparisons across methods, models, tasks, budgets, latency, and total compute are missing.
- Q14: The prevalence and robustness of overthinking across model families, tasks, domains, budgets, and decoding procedures remain unresolved.
- Q15: Reliable rules for difficulty prediction, stopping, and adaptive allocation under equal expected compute are not established.
- Q16: Self-verification, process verification, reranking, and LLM-judge reliability—including correlated errors, unfaithful traces, gaming, and domain shift—remain insufficiently characterized.
- Q17: The evidence does not cleanly separate reasoning improvements from gains due to extra sampling, search, retrieval, tools, or evaluator resources, and costs are incompletely quantified.
- Q18: Independent primary-source replication and broad model, task, and domain coverage remain insufficient, especially beyond Countdown and selected MATH evaluations.
- Q19: Comparisons separating inference-compute benefits from benefits of training or fine-tuning controllers, verifiers, revision models, or reasoning policies remain sparse.

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
4. 3 cited finding(s) were not fully supported by saved evidence.
5. 7 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `d32d6ea1035324f019e9421c7b216e4501bdab866df8e60cda19db2afb8a4c2f`
- Candidate report hash: `a96417c0b7d9a169d08ea522530daee26b1247f38ffd0169b8a08fb066468f37`
- LLM calls: 11
- Evaluated at: 2026-09-01T01:14:24.048944+00:00
