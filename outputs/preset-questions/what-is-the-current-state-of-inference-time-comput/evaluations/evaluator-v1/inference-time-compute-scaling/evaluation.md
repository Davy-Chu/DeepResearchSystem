# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** inference-time-compute-scaling

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 77.9 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.70
- Coverage: 0.72
- Depth: 0.66
- Citation quality: 0.86
- Citation validity: 1.00
- Citation support: 0.75
- Citation completeness: 1.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report gives a useful taxonomy of several core mechanisms, but the requested definition and comparison with adjacent interventions is incomplete.
- Candidate evidence:
  - The report defines inference-time scaling as a family of inference procedures and distinguishes “single-trajectory sequential scaling, leaf-level sampling with terminal reduction, and prefix-level search.” [S10] [S11]
  - It separately discusses sampling, majority voting, best-of-N, verifier methods, tree search, and adaptive allocation. [S9] [S13]
- Missing:
  - It does not explicitly define the boundary between inference-time scaling and training changes, increased model size, or merely supplying more input context.
  - Tool use and refinement are not clearly treated as distinct forms, and debatable boundary cases are not discussed.

### R2

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report identifies controlled comparisons and appropriately limits their generality, but it does not provide the detailed quantitative uncertainty and replication synthesis needed for full treatment.
- Candidate evidence:
  - It reports that additional sampling improves performance until a plateau on GSM8K and MATH-related settings. [S9]
  - It cites dense process-verifier search and adaptive response-distribution updates, including a reported greater-than-4× efficiency advantage over best-of-N on math reasoning. [S13]
  - It reports a FLOPs-matched comparison in which Llemma-7B with tree search outperformed Llemma-34B with standard majority voting across tested MATH budgets. [S9]
- Missing:
  - The report provides few numerical accuracy effect sizes, confidence intervals, or variance estimates.
  - The evidence synthesis is concentrated in a small set of studies and mathematical benchmarks, with limited discussion of independent replication or direct controls across strategies.
  - Some claims rely on summarized source material whose experimental details the report says cannot be independently assessed.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The major benchmarked mechanisms and several important failure modes are covered, but the comparison is not comprehensive across all mechanisms named in the rubric.
- Candidate evidence:
  - It distinguishes sequential scaling, leaf-level sampling with terminal reduction, and prefix-level search. [S10] [S11]
  - It separately discusses majority voting, best-of-N, weighted voting, verifier methods, and tree search. [S9]
  - It identifies correlated or unreliable selection processes through “poorly aligned verifiers or likelihood-based selectors,” which can cause performance to decline as sampling budgets increase. [S6]
  - It reports overthinking, inverted-U relationships between reasoning length and accuracy, and cases where models abandon initially correct answers after extended reasoning. [S1]
  - It notes that candidate discovery can improve faster than reliable answer selection and discusses unfaithful traces and manipulated judges. [S3] [S6]
- Missing:
  - Refinement or iterative revision is not substantially analyzed as a distinct mechanism.
  - Tool use and interactive search are not substantively compared with the other mechanisms.
  - The report does not systematically compare the conditions of success and failure for every mechanism, such as sample correlation, search branching, verifier calibration, or error propagation.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: It clearly rejects simplistic monotonic scaling and names the principal observed regimes, but the cross-condition characterization remains mostly qualitative.
- Candidate evidence:
  - The report states that benefits are conditional rather than monotonic and identifies plateaus, diminishing returns, overthinking, and harmful answer changes. [S1] [S6] [S9] [S13]
  - It reports an eventual accuracy plateau as sampling compute increases. [S9]
  - It describes inverted-U relationships between reasoning length and accuracy. [S1]
  - It states that effects vary with model, task difficulty, inference regime, selector or verifier, and compute budget.
- Missing:
  - The report does not present broad accuracy-versus-compute curves or quantify how the curve changes across model capability, task difficulty, budgets, and strategies.
  - It gives limited evidence for saturation or degradation outside the cited math-oriented studies.
  - Although it rejects a universal law, it does not develop a more specific evidence-based characterization of the functional forms that have been observed.

### R5

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes compute matching and gives conditional smaller-versus-larger-model examples, but realistic deployment trade-offs are only lightly treated.
- Candidate evidence:
  - It cites a reported greater-than-4× efficiency improvement over a best-of-N baseline. [S13]
  - It reports FLOPs-matched mathematical comparisons where a smaller model with stronger inference can outperform a much larger model. [S9] [S13]
  - The remaining-gaps section calls for comparisons at equal FLOPs, latency, energy, and monetary cost.
- Missing:
  - Most resource dimensions requested by the rubric—latency, throughput, energy, and monetary cost—are not actually evaluated.
  - The report does not give the conditions or accounting details behind the efficiency ratio in enough detail to assess it.
  - It does not systematically compare extra inference with larger models or differently trained models under matched deployment assumptions.
  - There is little discussion of practical constraints such as parallelism, service-level latency, or throughput.

### R6

- Coverage: 0.50
- Depth: 0.50
- Rationale: It correctly identifies benchmark concentration and major untested domains, but it mainly lists gaps rather than assessing transfer across those settings.
- Candidate evidence:
  - It states that the strongest evidence is on mathematical and contest-style benchmarks, including GSM8K, MATH, AIME, HMMT, and BrUMO-style tasks. [S9] [S12] [S13]
  - It explicitly says evidence is too thin for real-world reasoning, faithfulness, and broad general intelligence.
  - The remaining-gaps section names coding, factuality, science, long-horizon agents, and distribution shift as areas lacking transfer evidence.
- Missing:
  - Coding, knowledge-intensive or open-domain reasoning, planning, interactive/tool-using tasks, ambiguous tasks, safety-relevant workloads, and language variation are not separately assessed.
  - The report does not distinguish proprietary versus open models or synthetic versus naturalistic evaluations in a developed way.
  - There is little analysis of why transfer may fail or which observed effects might plausibly generalize.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report does a strong job separating validated benchmark findings from conditional and speculative claims and identifying thin evidence, but several requested evidence-quality threats and resolution criteria are only implicit or absent.
- Candidate evidence:
  - It explicitly limits confidence because evidence is concentrated in mathematical benchmarks and notes that some source summaries do not expose enough detail to assess controls, curves, and efficiency ratios. [S6] [S7] [S9] [S13]
  - It identifies unfaithful reasoning traces, verifier vulnerabilities, incomplete system-level evaluation, and the distinction between candidate discovery and genuine reasoning competence. [S3] [S6] [S10] [S11]
  - The remaining gaps include independent replication, prompt and temperature variation, open versus closed models, uncertainty estimates, complete compute accounting, and reliable stopping policies.
  - The conclusion explicitly marks broad real-world reasoning, faithful explanations, and universal substitution for larger models as unsupported or unproven.
- Missing:
  - Benchmark contamination, selective reporting, weak baselines, and the independence of studies are not explicitly discussed in sufficient detail.
  - The report does not specify concrete evidence designs for resolving most gaps, beyond broad calls for controlled comparisons and replication.
  - Some source-quality concerns are noted, but the report does not systematically grade the evidence by source type or access limitations.

### R8

- Coverage: 1.00
- Depth: 0.75
- Rationale: The synthesis is balanced, direct, and uncertainty-aware. Its only limitation is that the final paragraph does not restate the evidentiary strength and replication status of each major claim in detail.
- Candidate evidence:
  - The conclusion gives a qualified positive assessment: inference-time scaling is validated for difficult mathematical reasoning tasks when paired with effective search, voting, reranking, or verification.
  - It states that scaling is not a general law that longer reasoning always helps and notes diminishing returns, plateaus, and declines.
  - It identifies adaptive compute and verifier-guided methods as promising but unproven in general.
  - It directly states that evidence is too thin to conclude broad improvement in real-world reasoning, faithful explanations, or universal replacement of larger models.
- Missing:
  - The conclusion could more explicitly distinguish which findings are replicated versus supported by only a few primary studies, but it otherwise directly answers the question with appropriate conditionality.

### Novel Value

- The report synthesizes inference-time scaling as a collection of distinct mechanisms rather than a single scalar budget.
- It emphasizes the difference between candidate discovery and reliable answer selection, highlighting verifier and judge failures as central limits.
- It offers a useful conditional synthesis: benchmark gains are validated mainly for mathematical reasoning, while broad transfer, faithfulness, and universal scaling remain unestablished.
- It highlights overthinking and harmful answer changes as counterevidence to a universal monotonic scaling claim.

## Citations

### Support

#### F1: SUPPORTED

- Claim: Additional inference-time compute improves reasoning accuracy in some controlled benchmark settings, especially mathematical problem solving.
- Sources: S13, S9
- Rationale: Both saved sources report performance improvements from allocating additional computation during inference in benchmarked settings. S13 specifically describes improved math-reasoning efficiency and cases where test-time compute outperforms a much larger model. S9 explicitly states that scaling inference compute increases task performance and reports results on MATH and GSM8K. The qualifiers “some controlled benchmark settings” and “especially mathematical problem solving” are consistent with the evidence.
- Supporting text: S13: “Using this compute-optimal strategy, we can improve the efficiency of test-time compute scaling for math reasoning problems by more than 4x...” S9: “Scaling inference compute by sampling more solutions leads to growing task performance,” with evaluations on MATH and GSM8K.

#### F2: SUPPORTED

- Claim: Inference-time scaling is a family of structurally different inference procedures, not a single technique that can be represented adequately by one token or FLOP budget.
- Sources: S10, S11, S9
- Rationale: S11 explicitly describes test-time scaling as covering diverse inference algorithms with different statistical structures, compute accounting, and failure modes, and identifies three distinct structural regimes. It also states that treating these procedures as interchangeable under a single scalar budget makes comparisons difficult. S9 independently lists multiple inference strategies and evaluates their cost-performance trade-offs under compute budgets, supporting the claim that the procedures are not one uniform technique. S10 contains no substantive paper text beyond metadata, so it provides little additional support.
- Supporting text: S11: Test-time scaling covers algorithms that extend a single trajectory, aggregate completed candidates, or search over unfinished partial states; these differ in statistical structure and compute accounting, and should not be treated as interchangeable under one scalar budget. S9: the study compares greedy search, majority voting, best-of-n, weighted voting, and tree-search algorithms under different compute budgets.

#### F3: SUPPORTED

- Claim: The benefits of additional inference compute are conditional rather than monotonically increasing: plateaus, diminishing returns, overthinking, and harmful answer changes can occur.
- Sources: S9, S1, S6
- Rationale: S9 directly reports eventual accuracy plateaus and diminishing returns from additional computation. S1 directly supports diminishing marginal returns, overthinking, and correct-to-incorrect answer flips as reasoning budgets increase. S6 further reports that performance can decline as sampling budgets increase when verifiers or likelihood scores are poorly aligned. Together, the sources support the claim’s important factual content, though the effects are presented as occurring in particular settings rather than universally.
- Supporting text: S9: “There is an eventual point at which the accuracy will reach a plateau,” so additional resources yield diminishing returns. S1: marginal returns “diminish substantially,” and extended reasoning can cause models to abandon previously correct answers. S6: performance can “decline as sampling budgets increase” with poorly aligned verifiers or likelihood scores.

#### F4: PARTIALLY_SUPPORTED

- Claim: Task-adaptive compute allocation is empirically promising, but no universal stopping or allocation rule has been validated.
- Sources: S13, S1
- Rationale: S13 directly supports the empirical promise of task-adaptive allocation: effectiveness varies with prompt difficulty, and a compute-optimal adaptive strategy improves test-time compute efficiency by more than 4× versus best-of-N on math reasoning. S1 supports that uniform allocation is suboptimal and that optimal thinking length varies by problem difficulty. However, neither source explicitly establishes the broad negative claim that no universal stopping or allocation rule has been validated; S1 discusses adaptive stopping strategies but the supplied text does not report validation of a universal rule.
- Supporting text: S13: effectiveness varies with prompt difficulty; adaptive compute allocation improves efficiency by more than 4× over a best-of-N baseline. S1: optimal thinking length varies across problem difficulty, making uniform allocation suboptimal; stopping at moderate budgets can reduce computation while maintaining comparable accuracy.

#### F5: SUPPORTED

- Claim: Selection and verification are central determinants of whether extra candidate-generation compute becomes a useful final answer.
- Sources: S10, S11, S3, S6
- Rationale: The saved sources directly support that additional candidate generation does not by itself ensure a better final answer: candidates must be selected or reduced, and verifier quality can bottleneck or even undermine scaling. S11 describes reducers, verifier-based selection, and evaluation of the complete inference system; S3 explicitly calls verification central and reports verifier bottlenecks and failure modes; S6 states that candidate discovery can improve faster than reliable answer selection and that poorly aligned verifiers can cause performance to decline as sampling increases. S10 contains no substantive usable evidence beyond bibliographic page material.
- Supporting text: S6: “candidate discovery often improves faster than reliable answer selection” and “poorly aligned verifiers or likelihood scores can cause performance to decline as sampling budgets increase.” S11: a reducer “selects or aggregates” candidates, including verifier-based selection, and the final output depends on the system’s decision rule. S3: “verification is central—not auxiliary” and static verifiers “become a bottleneck.”

#### F6: PARTIALLY_SUPPORTED

- Claim: Smaller models can sometimes outperform larger models when paired with stronger inference procedures and additional compute, but this is a conditional result rather than a general replacement for parameter scaling.
- Sources: S13, S9
- Rationale: The sources directly support the conditional performance claim: smaller models can outperform larger ones when given advanced inference strategies and comparable or fixed compute, including a case where test-time compute lets a smaller model outperform a 14x larger model. However, the sources do not explicitly establish that this is not a general replacement for parameter scaling; they only describe trade-offs, budget dependence, plateaus, and prompt/task dependence.
- Supporting text: S13 reports that, in a FLOPs-matched evaluation, test-time compute can let a smaller base model outperform a 14x larger model on some problems. S9 states that smaller models with advanced inference algorithms can outperform larger models and that the ideal model size varies with the computation budget.

#### F7: PARTIALLY_SUPPORTED

- Claim: Evaluation and ranking under test-time scaling are becoming more methodologically rigorous, but improved measurement does not establish broader reasoning capability.
- Sources: S12, S10, S11
- Rationale: S12 directly supports more rigorous ranking methodology, reporting reliable statistical ranking methods and quantified agreement with a Bayesian reference. S11 supports increasingly systematic evaluation through formalized inference regimes, protocol-matched compute and uncertainty reporting, and reproducibility requirements. However, the supplied text does not establish the claim's important caution that improved measurement does not demonstrate broader reasoning capability; it discusses evaluation limitations and protocol dependence but does not explicitly distinguish measurement quality from general reasoning capability.
- Supporting text: S12: The work formalizes benchmark ranking under test-time scaling and introduces paired-comparison, IRT, voting, graph, and spectral methods, identifying reliable methods across high- and low-budget regimes. S11: The authors call for systematic evaluation of the entire inference system, protocol-matched reporting of compute and uncertainty, and explicit reproducibility requirements.

#### F8: PARTIALLY_SUPPORTED

- Claim: Empirical validation is strongest for mathematical and contest-style benchmarks; claims about broad real-world reasoning, faithfulness, and general intelligence remain unsupported or speculative in the supplied evidence.
- Sources: S9, S12, S13, S3, S10, S11
- Rationale: The sources strongly support that the reported empirical evaluations concentrate on mathematical and contest-style benchmarks: S9 evaluates MATH and GSM8K, S12 evaluates four Olympiad-style math benchmarks, and S13 reports improvements specifically for math reasoning problems. The sources also support caution about faithfulness and reliability: S3 explicitly reports unfaithful reasoning traces and evaluation gaming. However, the supplied evidence does not establish the broader negative claim that real-world reasoning, faithfulness, and general intelligence are unsupported or speculative overall. S11 mentions broad-knowledge benchmarks, while S10 contains no usable abstract or results beyond its title and metadata. General intelligence is not directly addressed.
- Supporting text: S9: “Llemma-7B ... consistently outperforms ... on the MATH benchmark” and reports evaluation on GSM8K. S12: results are “on four Olympiad-style math benchmarks.” S13: “improve ... test-time compute scaling for math reasoning problems.” S3: agents can produce “unfaithful reasoning traces” that manipulate verifiers, revealing evaluation-gaming vulnerabilities.

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

1. R5: Evaluate inference scaling against realistic resource constraints and alternatives.
2. R6: Assess how well reported inference-scaling effects transfer beyond the settings in which they were measured.
3. R2: Synthesize controlled evidence about whether and where additional inference-time compute improves reasoning performance.
4. 4 cited finding(s) were not fully supported by saved evidence.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `d32d6ea1035324f019e9421c7b216e4501bdab866df8e60cda19db2afb8a4c2f`
- Candidate report hash: `d2caf2b1e30dc74361af4bfa0794f71555bd2b99bab3468fb5b688ca36714de7`
- LLM calls: 11
- Evaluated at: 2026-08-31T21:11:15.143030+00:00
