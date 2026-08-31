# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** quantum-commercial-advantage

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 72.3 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.65
- Coverage: 0.65
- Depth: 0.65
- Citation quality: 0.77
- Citation validity: 1.00
- Citation support: 0.64
- Citation completeness: 0.90
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report uses several of the required distinctions and metrics, but it lacks a clear time boundary and systematic definitions of all four categories.
- Candidate evidence:
  - The report distinguishes “beyond-classical performance on narrow, specialized tasks” from “commercially useful advantage.”
  - It separately discusses “projected routes” and conditional forecasts, especially for chemistry and materials simulation.
  - It identifies comparison metrics including “runtime,” “solution quality,” “throughput,” “reproducibility,” “wall-clock time,” and “cost.”
- Missing:
  - No explicit evidence date or cutoff period is stated, despite references to an “accumulated evidence” record.
  - The categories are not fully defined at the outset, especially the distinction between theoretical algorithmic advantage and hardware-dependent projected advantage.
  - The report does not clearly define demonstrated quantum computational advantage as a category distinct from benchmark or sampling advantage.

### R2

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report correctly distinguishes artificial benchmark separations from application-level claims and gives useful caveats, but it does not provide sufficiently detailed representative experimental case studies.
- Candidate evidence:
  - The report discusses random-circuit-sampling-style demonstrations as “beyond-classical demonstrations” and notes that some are specially designed problems with little practical use. [S6]
  - It discusses Quantinuum’s optimization experiment, including its comparison to a one-layer QAOA baseline and the absence of comparison with the best classical algorithms. [S13]
  - It discusses Q-CTRL’s materials-simulation claim on an IBM quantum computer, including the claimed 3,000-times wall-clock speedup and missing benchmark details. [S11]
- Missing:
  - The demonstrations are not described with enough experimental specificity: platforms, task instances, quantum outputs, classical algorithms, and measured results are largely absent for the sampling examples.
  - There is no detailed representative account of major experimental claims such as a specific sampling experiment, its classical red-team comparison, or the relevant hardware limitations.
  - The report acknowledges that its source material does not document complete primary benchmark results, limiting evaluation of the claims.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is one of the strongest parts of the report: it directly assesses commercial usefulness and identifies the appropriate comparison boundary. It falls short of full depth because no complete workload comparison or detailed classical red-team analysis is presented.
- Candidate evidence:
  - The central conclusion is that “no broadly established, independently verified commercial quantum advantage is demonstrated.”
  - The Q-CTRL claim is evaluated as potentially commercially relevant but unresolved because the report lacks details on “the instance, classical implementation, end-to-end timing boundary, total cost, reproducibility, or independent replication.” [S11]
  - The report explicitly asks whether performance persists against “the best exact and approximate classical methods rather than only an industry-standard alternative.”
  - It identifies required end-to-end metrics including data preparation, compilation, queueing, repeated measurements, error suppression, post-processing, and operating cost.
- Missing:
  - The report does not analyze a demonstrated economically meaningful workload with a fully documented end-to-end comparison; its conclusion is therefore primarily an assessment of absence and evidentiary insufficiency.
  - System availability and sustained operational throughput are mentioned indirectly through queueing and benchmarking, but not assessed concretely.
  - The effect of specific subsequent classical algorithmic improvements is noted generally, not demonstrated through a detailed case study.

### R4

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report appropriately separates projections from demonstrations and identifies several practical assumptions, but it does not substantially explain the underlying theoretical algorithmic advantages or their resource requirements.
- Candidate evidence:
  - The report labels five-to-ten-year chemistry projections and broader 2028–2030s forecasts as “conditional forecasts,” not demonstrated milestones. [S2] [S5]
  - It states that projected chemistry and materials advantages depend on “hundreds of error-corrected logical qubits.” [S2]
  - It notes that simulated QAOA results require larger-instance comparisons against classical methods and that Quantinuum’s result leaves comparison with the best classical algorithms for future work. [S9] [S13]
  - It identifies practical conditions such as realistic data access, problem modeling, logical-qubit scale, error correction, and end-to-end cost.
- Missing:
  - The report gives little account of the actual theoretical complexity or performance claims of important algorithms, such as exponential versus polynomial speedups, Hamiltonian simulation, amplitude estimation, or factoring.
  - Assumptions behind theoretical advantages are not systematically stated, including oracle access, fault-tolerant gates, precision, state preparation, measurement, and input/output costs.
  - Resource estimates are mentioned qualitatively rather than quantified by logical gate counts, circuit depth, physical-qubit overhead, or runtime.

### R5

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report offers a useful comparison of chemistry/materials against optimization and QML and explains relative evidentiary strength, but its application survey is incomplete and uneven.
- Candidate evidence:
  - It identifies “quantum chemistry and materials simulation” as the most credible projected route to useful advantage and explains that quantum systems map naturally onto quantum hardware. [S2]
  - It contrasts optimization and quantum machine learning with chemistry, noting that tuned classical algorithms have not generally been beaten. [S2]
  - It discusses optimization evidence through QCHALLenge and Quantinuum, including scalability, runtime, solution quality, transferability, and missing best-classical comparisons. [S3] [S13]
  - It distinguishes application-level commercial claims from artificial sampling benchmarks and states that early applications would target specific bottlenecks rather than replace entire workflows.
- Missing:
  - Finance, cryptography, and scientific computing beyond chemistry/materials are not meaningfully compared.
  - The report does not consistently separate theoretical promise, scientific usefulness, and commercial value for every application area discussed.
  - The reasons chemistry/materials would produce commercial value—such as valuable accuracy thresholds, workflow integration, and customer economics—remain mostly qualitative.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report explains the central fault-tolerance bottleneck and connects several hardware and system constraints to useful workloads. It is less complete on architecture-specific barriers and the quantitative prioritization of sub-barriers.
- Candidate evidence:
  - It prioritizes scalable fault tolerance as the biggest barrier: converting noisy physical qubits into enough reliable logical qubits for deep, application-sized circuits.
  - It discusses physical error rates, decoherence, logical-qubit scale, connectivity, circuit depth, error correction, compilation, and circuit-resource reduction. [S1] [S2] [S3] [S8] [S9] [S13]
  - It explains that useful molecular simulation requires lower errors and larger systems, including projections involving hundreds of error-corrected logical qubits. [S2]
  - It also identifies realistic modeling, strong classical baselines, queueing, post-processing, solution quality, throughput, reproducibility, calibration stability, and cost as end-to-end barriers.
- Missing:
  - Control and decoding, correlated errors, fabrication/material variability, and sustained logical error rates are not developed in detail.
  - Platform-specific constraints such as cryogenics, photon loss, or architecture-specific connectivity and routing are not clearly separated from general barriers.
  - The report does not quantitatively prioritize error correction overhead, logical depth, and logical-qubit count for particular workloads.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report handles uncertainty and source limitations responsibly and identifies important conflicts. Full depth is missing because it does not substantively examine primary experiments, independent replications, or concrete classical critiques.
- Candidate evidence:
  - It distinguishes a company technical blog claim from more independent or methodological material, describing Q-CTRL’s evidence as lacking independent validation. [S11]
  - It notes that Quantinuum’s optimization claim does not compare against the best classical algorithms. [S13]
  - It reports conflicts between the Q-CTRL claim and broader conclusions that reproducible commercial advantage remains unestablished.
  - It explicitly identifies missing peer review, independent reproduction, exact benchmark details, classical baselines, and end-to-end cost.
  - It qualifies its high-confidence conclusion by stating that the source set is “not a comprehensive survey of all experiments.”
- Missing:
  - The report does not identify or analyze concrete independent replications or classical red-team critiques in detail.
  - The source base is heavily composed of vendor, industry, news, and secondary sources; primary experimental papers and their methodological quality are not substantively assessed.
  - The report mentions sensitivity to improved classical methods but does not document specific revisions or disagreements in classical estimates.
  - Some cited material is future-dated or described as truncated, creating additional source-validity uncertainty that is noted but not resolved.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report gives a clear, calibrated synthesis and concrete evidence requirements without relying on a single unsupported date. It would be stronger with a sharper distinction between narrow early deployments and broad commercial replacement and more explicit milestone thresholds.
- Candidate evidence:
  - The conclusion states that quantum computers are “close enough to commercial relevance to justify targeted experimentation, benchmarking, and hybrid workflows, but not close enough…to claim a general commercially useful advantage.”
  - It synthesizes narrow demonstrated advantage, stronger projected chemistry/materials promise, the unresolved Q-CTRL exception, and fault-tolerance requirements.
  - It gives a concrete decision criterion: “reproducible, end-to-end performance on a valuable workload against the best available classical alternative at competitive cost.”
  - The remaining-gaps section lists measurable milestones including logical-qubit counts, logical error rates, circuit depths, error-correction overhead, replication, accuracy, cost, and classical-baseline comparisons.
- Missing:
  - The maturity judgment could more explicitly distinguish proximity to a first narrow commercial advantage from proximity to broad commercial advantage.
  - The report repeats external forecasts such as 2028–2029 and the 2030s, although it labels them conditional; these dates are not independently converted into a calibrated probability or milestone-based forecast.
  - It does not specify threshold values for the proposed milestones or identify which single milestone would most strongly change the conclusion.

### Novel Value

- The report usefully treats the Q-CTRL 3,000-times materials-simulation result as a consequential but unresolved possible exception rather than accepting or dismissing it outright.
- It emphasizes an end-to-end commercial test—including preparation, compilation, queueing, repeated runs, post-processing, reproducibility, and cost—rather than isolated qubit or benchmark metrics.
- It identifies the gap between quantum-versus-weak-baseline claims and comparisons against the strongest evolving classical algorithms as a central uncertainty.

## Citations

### Support

#### F1: PARTIALLY_SUPPORTED

- Claim: No broadly established, independently verified commercial quantum advantage is demonstrated in the accumulated evidence.
- Sources: S2, S4, S3, S9
- Rationale: The sources support the narrower conclusion that practical quantum advantage has generally not yet been demonstrated and that current industrial applications remain prospective, limited, or under evaluation. However, they do not directly establish the full claim's stronger and broader elements—particularly “commercial,” “independently verified,” and “no broadly established” across the accumulated evidence.
- Supporting text: S2 says demonstrations have simulated only small molecules and have not reached systems complex enough to displace classical methods. S9 states that quantum advantage has not yet been demonstrated for many practical applications and that small-scale demonstrations are insufficient. S3 describes benchmarking industrial use cases against classical solvers and evaluates where practical application is currently hindered, while S4 says the field is “not quite ready for prime time.”

#### F2: SUPPORTED

- Claim: Demonstrated quantum advantage exists only in narrow or specialized contexts, and some demonstrations use artificial tasks with little practical value.
- Sources: S6, S13
- Rationale: S6 directly states that quantum advantage is not universal, remains workload-specific, and has been demonstrated in very limited, specialized contexts. It also explicitly says that several demonstrations involve specially designed problems with little or no practical use. S13 is consistent with the narrow-context aspect by describing a specific optimization algorithm and noting that its comparison with the best classical algorithms remained to be understood, though it does not independently support the artificial-task portion.
- Supporting text: S6: “Quantum advantage ... is not yet universal and remains workload-specific,” and has been demonstrated in “very limited, specialized contexts”; several demonstrations solve specially designed problems with “little or no practical use.”

#### F3: PARTIALLY_SUPPORTED

- Claim: A potentially important application-level claim is Q-CTRL's reported 3,000-times wall-clock speedup for a materials-simulation task, but it remains unverified in the accumulated record.
- Sources: S11, S3, S4, S6
- Rationale: S11 directly supports that Q-CTRL reported a more-than-3,000-times wall-clock speedup for a Fermionic Simulation/materials-engineering task. The saved sources do not independently verify that result. S6 supports treating vendor advantage claims as hypotheses requiring workload-specific, end-to-end benchmarking, but it does not specifically assess or disprove Q-CTRL's claim. S3 and S4 provide general context rather than direct evidence about this particular result.
- Supporting text: S11: Q-CTRL says its quantum system can reach a solution “over 3,000 times faster in wall-clock time” than the industry-standard alternative for Fermionic Simulation. S6: “Treat ‘advantage’ claims as workload hypotheses to test, not facts to accept,” and many reports omit end-to-end time-to-answer metrics.

#### F4: SUPPORTED

- Claim: Quantum chemistry and materials simulation are the most credible projected routes to useful quantum advantage.
- Sources: S2, S11, S9
- Rationale: The cited sources consistently identify chemistry, molecular simulation, and materials simulation as especially credible or promising paths toward practical quantum advantage. S2 explicitly calls chemistry and materials science among the most credible near-term application areas and describes molecular simulation as the most viable near-term area. S11 reports a materials-simulation demonstration framed as practical quantum advantage, while S9 calls quantum simulation promising and discusses quantum chemistry and materials science in relation to realistic advantage. The wording “projected routes” is supported, although the sources also emphasize that useful advantage remains conditional and not broadly established.
- Supporting text: S2: “Molecular simulation in drug discovery, materials science, and chemistry emerges as the most viable near-term application area” and “chemistry and materials science are among the more credible near-term application areas.” S11: “3,000 times speedup in materials simulation” and materials simulation is described as a prime candidate for sustainable advantage. S9: “Quantum simulation is considered a promising path toward genuine quantum advantage.”

#### F5: PARTIALLY_SUPPORTED

- Claim: Optimization and quantum machine learning remain substantially less established than chemistry and materials simulation.
- Sources: S2, S3, S9, S13
- Rationale: The sources support a narrower comparison: chemistry and materials simulation are described as credible or promising near-term areas, while optimization and machine learning still face uncertain advantage, significant hurdles, and reliance on theoretical or simulated evidence. However, the saved excerpts do not directly establish that both optimization and quantum machine learning are 'substantially less established' than chemistry and materials simulation as a broad comparative conclusion. S13 reports an optimization demonstration, and the excerpts provide little specific evidence about the maturity of quantum machine learning.
- Supporting text: S2 calls molecular simulation in drug discovery, materials science, and chemistry the most viable near-term area, while saying optimization and AI face longer timelines and uncertain advantage. S3 describes optimization and machine-learning evaluations as assessing promise and practical hurdles, including cases where classical methods are expected to remain superior. S9 states that quantum advantage has not yet been demonstrated for many practical applications and discusses QAOA and quantum machine learning largely in the context of scaling, theory, and future applicability.

#### F6: PARTIALLY_SUPPORTED

- Claim: The biggest technical barrier is scalable fault-tolerant computation: converting noisy physical qubits into enough reliable logical qubits for deep, application-sized circuits.
- Sources: S1, S2, S3, S8, S9, S13
- Rationale: The sources support the core idea that noise, error correction, limited qubit counts, and fault tolerance are major technical obstacles to practical, deep, application-scale quantum computation. However, they do not establish that this is definitively the “biggest” barrier, nor do they consistently describe the full process of converting physical qubits into enough logical qubits for deep circuits. Some cited material instead focuses on algorithm scaling, benchmarking, or resource reduction.
- Supporting text: S1 states that pre-2026 devices were noisy and limited to roughly 50–200 error-prone physical qubits, with decoherence making results unreliable beyond shallow circuits. S2 says current hardware lacks the error rates and qubit counts required for useful molecular simulation and cites a need for hundreds of error-corrected logical qubits. S3 identifies low qubit counts and error susceptibility as hardware limitations. S8 calls strong error correction necessary and scalable processors critical. S13 describes unavoidable quantum noise as a technical challenge and says resources must be minimized to protect algorithms.

#### F7: PARTIALLY_SUPPORTED

- Claim: Other major barriers are algorithmic and economic: realistic problem modeling, strong classical baselines, and end-to-end system performance.
- Sources: S9, S6, S4, S3
- Rationale: The sources support barriers involving realistic problem formulation/modeling, comparison with strong classical methods, and end-to-end or runtime performance. However, they do not clearly establish that these are specifically “economic” barriers as a group, nor do they directly support the exact characterization of realistic modeling as a major barrier beyond noting idealized assumptions and evaluation criteria.
- Supporting text: S9 contrasts idealized closed-system models with “realistic physical and algorithmic conditions” and says small-scale demonstrations are insufficient as problem size grows. S6 highlights “moving classical baselines” and omitted end-to-end metrics such as compilation, queueing, execution, and post-processing. S3 evaluates model formulation, scalability, solution quality, and runtime, and benchmarks quantum algorithms against classical solvers. S4 discusses slower quantum processing, the need to compare against classical computers, and “quantum economic advantage.”

### Missing Citations

- Q19: The report concludes that quantum computers are close enough to commercial relevance to justify targeted experimentation and hybrid workflows, but not close enough to claim a general commercially useful advantage over classical computers.
- Q20: The decisive test of commercial usefulness is reproducible, end-to-end performance on a valuable workload against the best available classical alternative at competitive cost.

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

1. R1: Set a time boundary and define the categories used to answer the question.
2. R2: Evaluate representative experimental claims of quantum advantage against classical computation.
3. R4: Separate theoretical algorithmic advantages from hardware-dependent projections.
4. 5 cited finding(s) were not fully supported by saved evidence.
5. 2 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ae3a5680c375b6650be217402137fd59a302eee5fb85b0bc360a9292a5734293`
- Candidate report hash: `6b4a4d9d18aba6e3f41351dc1fc2e8623b6b1f4d62991e8eb81d1d1a7dcded27`
- LLM calls: 9
- Evaluated at: 2026-08-31T21:15:19.000052+00:00
