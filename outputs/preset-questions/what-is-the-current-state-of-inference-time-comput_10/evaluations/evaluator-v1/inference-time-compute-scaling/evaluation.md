# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** inference-time-compute-scaling

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 70.9 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.56
- Coverage: 0.56
- Depth: 0.56
- Citation quality: 0.90
- Citation validity: 1.00
- Citation support: 0.85
- Citation completeness: 0.95
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report names several relevant mechanisms but provides no explicit scope or definitions framework. Its treatment is therefore only a vague partial mention.
- Candidate evidence:
  - The report refers to “additional inference-time compute” through “multiple candidate solutions, verification, search, and multi-agent pipelines.”
  - It distinguishes inference-time scaling from universal accuracy-versus-compute laws and discusses multimodal versus language-only scaling.
- Missing:
  - It never explicitly defines inference-time compute scaling as allocating additional computation during inference.
  - It does not systematically distinguish serial reasoning length, parallel sampling, search, verification, refinement, tool use, or adaptive budgets.
  - It does not clearly separate these interventions from training changes, larger model size, or merely supplying more context, nor discuss debatable boundaries.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: There is substantial empirical comparison with models, tasks, budgets, strategies, and several quantitative effects. Coverage falls short of full because uncertainty and replication synthesis is limited and the evidence base is uneven across mechanisms.
- Candidate evidence:
  - Finding 1 synthesizes evidence from Sys2Bench across eleven datasets, seven models, and five task categories, reporting that no technique consistently wins.
  - Finding 2 compares self-consistency with generative verification and reports that self-consistency is stronger at lower budgets while GenRM wins after substantially more compute in tested mathematical settings.
  - Finding 3 reports matched-budget gains of 1.3 and 2.7 percentage points for debate and mixture-of-agents over self-consistency on MMLU-Pro and BBH.
  - Finding 6 reports larger gains on medium and hard MMLU-Pro tasks than easy tasks.
- Missing:
  - The report does not provide a sufficiently broad synthesis of effect sizes, uncertainty intervals, variance, or statistical significance across the cited studies.
  - Replication and independence of the controlled comparisons are discussed as limitations, but replicated versus isolated effects are not systematically classified.
  - Some major forms of scaling, including serial length, refinement, tool use, and search, receive little controlled comparative evidence.

### R3

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report gives meaningful treatment of sampling, verification, search-related methods, and multi-agent interaction, including several failure modes. It does not cover all principal mechanisms or provide a complete comparative account.
- Candidate evidence:
  - The report separately discusses self-consistency, verification, multi-agent debate, mixture-of-agents, cross-model consensus, speculative decoding, and tree-search methods.
  - Finding 4 identifies a coverage–precision trade-off between generating candidates and verifying them, and reports that verifier choice, aggregation, and candidate diversity matter.
  - Finding 5 reports verifier false positives, format and response-length sensitivity, domain limitations, and precision–recall trade-offs.
  - The report notes that semantic verification can improve acceptance while risking accuracy loss and that tree search depends strongly on verifier performance.
- Missing:
  - Serial reasoning length is not analyzed as a distinct mechanism, including possible error propagation or degradation from excessively long reasoning.
  - Refinement, best-of-N as a distinct method, and tool use are not substantively compared.
  - Adaptive allocation is mentioned mainly through the MMLU-Pro proposal, without evidence about when it succeeds or fails.
  - The report does not systematically compare search, sampling, verification, refinement, and interaction under common budgets.

### R4

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report correctly emphasizes conditional, budget-dependent behavior and rejects universal laws, but it offers only scattered evidence about curve shapes and does not fully characterize scaling behavior.
- Candidate evidence:
  - The report states that self-consistency can saturate earlier than interactive multi-agent methods.
  - It reports that self-consistency is better at lower budgets while GenRM becomes advantageous at higher budgets, indicating budget-dependent frontiers.
  - Finding 6 reports larger returns on medium and hard MMLU-Pro tasks than easy tasks.
  - Finding 10 explicitly rejects a universal, predictable accuracy-versus-compute scaling law.
- Missing:
  - Monotonicity is not directly assessed across complete compute curves.
  - Diminishing returns, saturation, and performance degradation are not quantitatively characterized across models, strategies, or budgets.
  - The report gives little evidence on how behavior varies with model capability beyond a brief unresolved statement about larger versus smaller models.
  - No functional scaling relationship or clear account of long-run limits is provided.

### R5

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes the need for realistic accounting and includes some matched-budget and speedup evidence, but it does not itself deliver a comprehensive resource-constrained evaluation.
- Candidate evidence:
  - Finding 3 reports explicitly matched-budget comparisons and quantitative accuracy differences between multi-agent methods and self-consistency.
  - Finding 7 reports a peak speedup increase from 1.4× to 2.1× for LOOKAHEAD while preserving quality on selected benchmarks.
  - The report repeatedly flags incomplete accounting for verifier computation, communication, memory transfer, batching, latency, and serving costs.
  - It notes that the crossover between larger models and smaller models with more inference compute is unresolved.
- Missing:
  - There is no systematic comparison using FLOPs, total tokens, wall-clock latency, throughput, energy, or monetary cost.
  - Matched-budget conditions are narrow and do not consistently specify whether all verifier, communication, or model-serving costs are included.
  - Alternatives such as a larger or differently trained model are not evaluated with matched deployment assumptions; the larger-versus-smaller claim is only identified as unresolved.
  - Quality-efficiency trade-offs for realistic multi-user deployment are not empirically synthesized.

### R6

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report includes several domains and explicitly warns against transfer, but the generalization assessment remains concentrated on mathematics, science, selected reasoning benchmarks, and multimodal tasks.
- Candidate evidence:
  - The report cites Sys2Bench across reasoning and planning tasks and VerifyBench across mathematics, physics, chemistry, and biology.
  - It discusses MMLU-Pro and BBH, selected GSM8K and AIME results, and a multimodal study across ten datasets.
  - It notes limited cross-domain verifier generalization, domain-dependent consensus ceilings, and that matched-budget multi-agent results are restricted to two benchmarks.
  - The remaining gaps explicitly call for testing code, science, planning, difficult proofs, contamination-resistant benchmarks, and out-of-distribution tasks.
- Missing:
  - Coding, knowledge-intensive/open-domain reasoning, interactive tool use, ambiguous tasks, safety-relevant workloads, and languages beyond the reported settings are not substantively evaluated.
  - Synthetic versus naturalistic data is not discussed.
  - Proprietary versus open models is addressed only indirectly through the statement that closed systems have undisclosed procedures and budgets.
  - Real-world transfer and deployment behavior are identified as gaps rather than analyzed.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is one of the strongest parts of the report: it clearly marks uncertainty, conflicts, narrow evidence, and concrete research gaps. Full coverage is withheld because several rubric-specific evidence-quality threats are only briefly or indirectly treated.
- Candidate evidence:
  - The report assigns confidence levels and repeatedly labels findings as conditional, preliminary, or unresolved.
  - The Conflicts and Uncertainty section explains disagreements through task, budget, interaction protocol, model heterogeneity, and accounting differences.
  - The report identifies narrow benchmark coverage, overlapping source versions, lack of independent replication, incomplete total-cost accounting, undisclosed proprietary procedures, verifier weaknesses, and limited out-of-domain testing.
  - The Remaining Gaps section specifies needed evidence, including full compute curves, independent replications, realistic serving accounting, transfer tests, and validation across models and tasks.
- Missing:
  - Benchmark contamination, selective reporting, and weak baselines are listed or implied only incompletely; they are not developed as evidence-quality problems in the main analysis.
  - The report does not clearly organize claims into established, plausible-but-conditional, and speculative categories beyond confidence labels and prose.
  - It gives few concrete proposals for resolving contamination, selective reporting, or replication concerns beyond broad calls for more studies.
  - Some cited evidence is secondary or preliminary, but source-quality differences are not systematically assessed.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The conclusion is balanced, conditional, and directly answers the question. It falls short of full synthesis because several mechanism-specific evidence statuses are not integrated into the final summary.
- Candidate evidence:
  - The conclusion states that inference-time scaling is “empirically real but conditional.”
  - It identifies additional sampling, verification, search, and multi-agent computation as useful in some settings while preserving self-consistency as a strong lower-budget baseline.
  - It explicitly says that no universal accuracy-versus-compute law, single compute-optimal strategy, or reliable cross-domain transfer has been established.
  - It characterizes newer directions such as speculative decoding, cross-model consensus, and multimodal scaling as promising but too narrow for broad claims.
- Missing:
  - The conclusion could more explicitly separate well-replicated findings from evidence based on single studies or limited benchmarks.
  - It does not directly summarize the status of serial reasoning length, refinement, tool use, or adaptive allocation, leaving the overall synthesis incomplete for the full rubric scope.
  - The confidence of specific claims is conveyed in the findings but not fully consolidated into a concise evidence hierarchy in the conclusion.

### Novel Value

- The report provides a useful conditional synthesis rather than asserting a universal scaling law.
- It combines matched-budget comparisons, verifier limitations, cross-domain caveats, and deployment-accounting gaps into a coherent account of why method rankings are not settled.
- It identifies concrete unresolved comparisons, including total-cost curves, independent replication, adaptive allocation, and transfer beyond mathematics and selected benchmarks.

## Citations

### Support

#### F1: SUPPORTED

- Claim: Additional inference-time compute has been empirically validated as useful for some LLM reasoning tasks, but its benefits are not universal.
- Sources: S5, S4, S12, S13
- Rationale: The saved sources report empirical evaluations showing accuracy improvements from increased inference-time computation on reasoning benchmarks, while also documenting task- and strategy-dependent limitations. S12/S13 report up to a 7.1 percentage-point improvement over chain-of-thought at higher budgets on MMLU-Pro and larger gains on harder tasks. S5 states that no single inference-time technique consistently performs well across all reasoning and planning tasks, and S4 likewise finds that no strategy dominates uniformly and that beam search often provides little benefit with increased width.
- Supporting text: S12/S13: “inference scaling improves accuracy by up to +7.1% points over chain-of-thought” on MMLU-Pro, with the greatest gains on harder tasks. S5: “simply scaling inference-time computation has limitations,” since “no single inference-time technique consistently performs well across all reasoning and planning tasks.” S4: “no single strategy dominates uniformly.”

#### F2: PARTIALLY_SUPPORTED

- Claim: Self-consistency and majority voting are well-supported practical baselines, especially at lower or moderate inference budgets.
- Sources: S4, S6, S12, S13
- Rationale: The sources support self-consistency/majority voting as established, straightforward, compute-efficient baseline methods, and S6 directly reports that self-consistency outperforms GenRM at lower compute budgets and is more efficient for most practical budgets. However, S12 and S13 qualify this: under equal budgets, debate and mixture-of-agents outperform self-consistency, which saturates earlier. The sources do not clearly establish the broader characterization that both self-consistency and majority voting are uniformly “well-supported” practical baselines at moderate budgets.
- Supporting text: S6 describes self-consistency as a “straightforward and effective” method using multiple solutions and majority voting, and reports that it outperforms GenRM at lower compute budgets. S4 says majority voting provides “reliable, compute-efficient improvements across most settings.”

#### F3: SUPPORTED

- Claim: Matched-budget evidence supports multi-agent methods, particularly mixture-of-agents and debate, as potentially more compute-efficient than self-consistency in selected settings.
- Sources: S12, S13
- Rationale: Both saved snapshots report matched or equal-compute comparisons in which debate and mixture-of-agents outperform self-consistency, by 1.3 and 2.7 percentage points respectively. They also limit the result to evaluated benchmarks/configurations and note stronger persistence on more complicated tasks, supporting the claim’s qualified wording about selected settings and potential efficiency.
- Supporting text: S12/S13: “With an equal computing budget, debate and mixture-of-agents outperform self-consistency by 1.3% and 2.7% points, respectively,” and “multi-agent gains persist, particularly on more complicated tasks.”

#### F4: SUPPORTED

- Claim: The optimal allocation of inference compute between candidate generation and verification is nontrivial and budget-dependent.
- Sources: S6, S1, S4, S8
- Rationale: S6 directly supports both key elements: allocating compute between solution generation and verification involves a tradeoff, and the preferred allocation changes with the total inference budget. It reports that self-consistency performs better at lower budgets while generative verification performs better at higher budgets, and explicitly frames the allocation as an optimization problem. S1, S4, and S8 provide related tradeoffs involving verification and compute, but are not necessary for the claim.
- Supporting text: S6 states that under a limited inference budget there is a tradeoff between scaling candidate solutions and allocating compute to verification. It further reports that self-consistency outperforms GenRM at lower compute budgets, whereas GenRM performs better at higher budgets, and asks how to split a given budget between generating solutions and verifying them for optimal performance.

#### F5: PARTIALLY_SUPPORTED

- Claim: Verifier reliability is a major bottleneck for inference-time scaling.
- Sources: S8, S1, S4
- Rationale: S8 directly characterizes verifier unreliability as a critical challenge and identifies bottlenecks in verifier technology, but frames the impact primarily for RLVR rather than inference-time scaling broadly. S1 supports a narrower inference-time claim: verifier judgment accuracy must be balanced against compute cost, since erroneous verification can reduce accuracy. S4 indicates verifier choice substantially affects PRM performance, but the supplied excerpt does not call reliability a major bottleneck. Together, the sources support that verifier reliability is an important limitation in some inference-time verification and scaling methods, not the broad claim as stated.
- Supporting text: S8: “the inherent unreliability of current verifier systems remains a critical challenge” and creates “critical bottlenecks in their current design.” S1: practical verifiers must balance “compute cost against judgment accuracy,” and loose verification “risks accuracy drop from erroneous steps.” S4: “verifier choice and aggregation method ... substantially affect PRM performance.”

#### F6: SUPPORTED

- Claim: Task difficulty appears to affect the return on inference-time compute, with larger gains reported on harder tasks in at least one matched-budget study.
- Sources: S12, S13
- Rationale: Both saved snapshots describe a study comparing inference strategies under matched compute budgets and explicitly report that the greatest inference-time compute gains occurred on harder tasks. The evidence supports the cautious wording that task difficulty appears to affect returns, and that this was observed in at least one study.
- Supporting text: S12/S13: The study analyzes four inference paradigms “under matched compute budgets” and reports: “The greatest inference-time compute gains were observed on harder tasks (+9 pp for 15–20x CoT budget),” while its figure summarizes gains of +2.2% on easy, +8.5% on medium, and +9.0% on hard tasks.

#### F7: PARTIALLY_SUPPORTED

- Claim: Step-level speculative decoding is a promising efficiency technique, but its quality and scalability are not yet field-wide validated.
- Sources: S1
- Rationale: S1 supports that step-level speculative decoding is presented as an efficiency technique with empirical speedup gains and better scaling with additional GPU throughput, and it notes verifier accuracy/speed tradeoffs. However, the source does not establish that quality and scalability are not yet field-wide validated; it reports results from the paper’s own benchmarks rather than a field-wide validation assessment.
- Supporting text: The paper describes step-level speculation as exposing “a coarser unit for speculation,” reports speedup improving from 1.4× to 2.1× while preserving answer quality, and states that speedup “scales better with additional GPU throughput.” It also says practical verifiers must balance compute cost against judgment accuracy.

#### F8: SUPPORTED

- Claim: Cross-model consensus is a promising verification signal, but its benefits and ceiling are domain-dependent.
- Sources: S7
- Rationale: S7 directly presents cross-model consensus as a verification signal, reports strong performance across multiple benchmarks, and explicitly describes a ceiling caused by shared errors that varies by domain: near zero on math but non-trivial on science. This supports both the promise of the method and the claim that its benefits and limitations depend on the domain.
- Supporting text: The source calls cross-model consensus a “training-free verifier,” reports that it outperforms self-consistency and several trained verifiers, and identifies a “shared-error floor” that is “near zero on math but non-trivial on science.”

#### F9: SUPPORTED

- Claim: Evidence for multimodal inference-time scaling is positive but preliminary and does not directly establish language-only scaling laws.
- Sources: S9
- Rationale: S9 explicitly presents the work as a “Preliminary Study” and reports positive results for multimodal inference-time scaling, including significantly better average performance and higher upper bounds than text-only thought. It also frames the study as focused on multimodal reasoning and does not claim to establish language-only scaling laws; therefore the claim’s qualification is supported by the source’s scope.
- Supporting text: The paper is titled “Investigating Inference-time Scaling for Chain of Multi-modal Thought: A Preliminary Study.” Its findings state that multimodal thought achieves “significantly better performance and higher upper bounds compared to text-only thought,” while the study focuses on multimodal reasoning across 10 datasets.

#### F10: SUPPORTED

- Claim: A universal, predictable accuracy-versus-compute scaling law and a universally optimal inference-time method remain speculative.
- Sources: S14, S5, S12, S13, S3
- Rationale: The sources support both parts of the claim. S14 says some studies observe scaling-law-like performance improvements but also states that the field lacks a unified framework and identifies open challenges. S5 directly reports that simply scaling inference-time computation has limitations and that no single technique consistently performs well across all evaluated tasks. S12/S13 show method- and task-dependent Pareto tradeoffs rather than a universal optimum, while S3 characterizes the scaling-law idea as something that only “seems” to be emerging and notes that the field is moving quickly.
- Supporting text: S14: “some studies ... observe patterns akin to scaling laws,” while the field “lacks a unified and systematic framework” and faces open challenges. S5: “no single inference-time technique consistently performs well across all reasoning and planning tasks.” S13: methods have different computational tradeoffs and MoA is recommended in the evaluated setting, not universally.

### Missing Citations

- Q21: The mechanisms and inference budgets of closed reasoning systems such as o1 or o3 are undisclosed in the supplied sources.

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
2. R3: Compare the principal inference-scaling mechanisms and their observed conditions of success or failure.
3. R4: Characterize how reasoning quality changes as inference compute increases.
4. 3 cited finding(s) were not fully supported by saved evidence.
5. 1 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `d32d6ea1035324f019e9421c7b216e4501bdab866df8e60cda19db2afb8a4c2f`
- Candidate report hash: `540e41c301de904fa35d9923b98e69604be59feea4baf1899c50fbf8c8cdd0ea`
- LLM calls: 13
- Evaluated at: 2026-09-01T09:20:50.006501+00:00
