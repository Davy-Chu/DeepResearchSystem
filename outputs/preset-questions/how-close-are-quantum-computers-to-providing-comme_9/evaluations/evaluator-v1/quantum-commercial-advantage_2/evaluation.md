# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** quantum-commercial-advantage

**System Version:** llm-only-baseline-v0

**Model:** gpt-5.6-luna

## Summary

- Overall: 55.8 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.76
- Coverage: 0.78
- Depth: 0.72
- Citation quality: 0.00
- Citation validity: 0.00
- Citation support: 0.00
- Citation completeness: 0.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report covers the requested conceptual distinctions and comparison metrics well, but lacks an explicit time boundary and fully formal category definitions.
- Candidate evidence:
  - The report sets an implicit evidence boundary through references to experiments from 2019, 2022, 2023, and standards finalized in 2024.
  - It distinguishes benchmark advantage from commercial advantage: “Quantum computers have demonstrated computational advantages on carefully constructed benchmark problems, but not yet a broadly accepted, commercially useful advantage.”
  - It discusses theoretical and projected advantages separately, including Shor’s algorithm, chemistry resource estimates, and industry or academic timelines.
  - It identifies relevant metrics including speed, cost, accuracy, wall-clock time, energy, capital cost, verification, and data-transfer overhead.
- Missing:
  - It does not explicitly state a clear evidence date or cutoff period, such as “as of 2024” or “as of [month/year].”
  - The four categories are discussed but not explicitly defined as a structured taxonomy, and the distinction between theoretical algorithmic advantage and projected hardware-dependent advantage could be sharper.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report appropriately distinguishes sampling demonstrations from useful workloads and includes representative superconducting and photonic examples. Its treatment is substantial but not fully technically comparative.
- Candidate evidence:
  - It describes Google’s 2019 53-qubit random-circuit-sampling experiment, including the claimed approximately 200-second runtime and the much longer initial classical estimate.
  - It describes Google’s 2022 70-qubit random-circuit-sampling result and identifies it as a benchmark rather than a commercial application.
  - It discusses photonic Jiuzhang and Gaussian-boson-sampling experiments as specialized sampling demonstrations.
  - It notes limitations including classical simulation improvements, debated classical estimates, verification assumptions, and the artificial or noncommercial nature of the tasks.
- Missing:
  - The classical comparisons are mostly qualitative and do not provide a consistent, current comparison metric across demonstrations.
  - The report gives limited detail on verification and the precise nature of the claimed separations, such as sampling fidelity, instance size, or subsequent best classical simulations.
  - It does not discuss a broader set of representative demonstrations, such as specific logical-qubit or application-oriented experiments, in comparable task/platform/result/limitation detail.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The maturity judgment and accounting framework are strong, but the requirement calls for evaluating whether at least one economically meaningful workload meets the end-to-end standard; the report mainly establishes absence through summary rather than detailed comparative evidence.
- Candidate evidence:
  - It concludes that there is “no broadly accepted demonstration” of useful end-to-end advantage on a commercially important task.
  - It defines application-level advantage in terms of being “faster, cheaper, more accurate, or otherwise better than the best classical workflow.”
  - It states that total accounting must include state preparation, error mitigation, error correction, repeated runs, preprocessing, postprocessing, verification, energy, capital cost, queueing, and workflow integration.
  - It explicitly notes that classical algorithm improvements weakened early random-circuit-sampling claims and remain a problem for application claims.
  - It discusses IBM utility experiments and quantum annealing while stating that neither established a durable, general advantage.
- Missing:
  - No specific economically meaningful workload is examined end-to-end with an actual quantum result, strongest practical classical baseline, accuracy target, repeated-run cost, and operating-cost comparison.
  - The conclusion relies on general reviews and claims of consensus rather than presenting a detailed case study or independent evaluation of a particular commercial claim.
  - The report does not quantify how much state preparation, mitigation, verification, or system availability changes any reported application result.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report makes the key theoretical/projected distinction and identifies assumptions and resource constraints, but the treatment is uneven across application classes and lacks a systematic resource-to-performance analysis.
- Candidate evidence:
  - For chemistry and materials, it explains the claimed state-representation benefit and identifies competing classical methods, noise, sampling cost, and resource estimates involving millions or more physical qubits.
  - For cryptanalysis, it states Shor’s polynomial-time factoring and discrete-logarithm advantage and explains that large fault-tolerant machines are required.
  - For optimization, it notes that QAOA and annealing lack demonstrated general asymptotic or practical advantage against strong classical heuristics.
  - For quantum machine learning, it identifies data-loading and measurement assumptions that can erase proposed speedups.
  - It explicitly labels late-2020s and 2030s forecasts as forecasts rather than evidence.
- Missing:
  - Complexity or performance benefits are not stated with comparable precision for chemistry, optimization, and machine-learning candidates; the chemistry discussion is mostly qualitative.
  - The report does not systematically connect resource estimates to particular hardware assumptions, logical-qubit counts, runtimes, or end-to-end data-access conditions for each candidate area.
  - It does not clearly separate asymptotic advantage, practical scientific advantage, and commercially relevant advantage within every area.

### R5

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report provides a useful comparative ranking of major areas and explains why evidence differs, but the area-by-area distinction among theoretical promise, scientific usefulness, and commercial value is incomplete.
- Candidate evidence:
  - It identifies chemistry and materials simulation as the leading plausible route to early useful advantage and lists catalysts, batteries, superconductors, and correlated-electron systems.
  - It treats cryptanalysis as theoretically decisive but not an imminent ordinary commercial workload, with post-quantum migration as the practical response.
  - It compares optimization and machine learning as less established, citing strong classical heuristics, state-preparation costs, and limited empirical evidence.
  - It distinguishes projections from demonstrations and states that chemistry/materials and cryptanalysis are more credible than optimization and machine learning.
- Missing:
  - Scientific usefulness and commercial value are not separately assessed in a consistent way for every area.
  - Finance and scientific computing beyond chemistry/materials are not meaningfully considered, despite being relevant candidate domains.
  - The comparison does not provide concrete workload thresholds or evidence explaining when chemistry’s scientific promise would translate into customer-level economic value.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report explains the main general engineering barriers and their workload consequences well, but it gives limited architecture-specific analysis and only moderate prioritization and quantification.
- Candidate evidence:
  - It identifies fault tolerance as the central barrier and explains how two-qubit errors, measurement errors, leakage, crosstalk, frequency collisions, and correlated noise limit circuit depth.
  - It explains physical-to-logical overhead, including “hundreds to thousands of physical qubits per logical qubit” and additional magic-state-factory overhead.
  - It discusses scaling constraints involving fabrication, component uniformity, high-bandwidth control, cryogenic or vacuum infrastructure, calibration, decoding, feedback, wiring, and cooling.
  - It connects barriers to useful chemistry and factoring circuits and emphasizes that useful systems need large populations of stable, long-lived logical qubits.
  - It notes that relative importance varies by architecture.
- Missing:
  - The report does not explicitly classify barriers as general versus architecture-specific in a systematic way.
  - Photon loss, photonic-component/fabrication constraints, ion-trap or neutral-atom-specific constraints, and other platform-specific limitations are largely absent.
  - It does not prioritize barriers beyond calling fault tolerance central, nor does it quantify required sustained logical depth, logical error rates, connectivity/routing overhead, or decoder performance for representative workloads.

### R7

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report has a good conceptual treatment of evidence types and uncertainty, but the absence of usable retrieved sources and limited source-specific evaluation prevents deeper evidence-quality coverage.
- Candidate evidence:
  - It distinguishes primary demonstrations from later classical challenges, noting that the 2019 Google classical estimate was “subsequently debated and improved.”
  - It identifies independent or adversarial perspectives through “Google correction/rebuttals and IBM analysis,” classical-simulation analyses, independent reviews, and classical red-team-style concerns.
  - It discusses disagreements over random-circuit-sampling separation sizes, utility-result baselines, chemistry and factoring resource estimates, and vendor claims.
  - It labels company and academic roadmaps as forecasts and warns that quantum-annealing claims may show customer-specific value without general speedup.
- Missing:
  - The report provides source IDs but ends with “No usable sources were retrieved,” so the evidence is not actually documented with accessible, current citations or links.
  - It does not identify specific independent replications, critiques, or classical algorithms and explain their methodological consequences in enough detail.
  - The uncertainty surrounding the negative conclusion about no commercial advantage is acknowledged but not supported through a systematic survey of failed, disputed, or independently validated commercial claims.
  - Vendor claims, primary experiments, theoretical work, and roadmaps are categorized only broadly rather than evaluated source by source.

### R8

- Coverage: 1.00
- Depth: 0.75
- Rationale: The report gives a calibrated and well-synthesized maturity judgment, distinguishes evidence classes, and identifies evidence that would change the assessment. Its depth is slightly limited by the lack of quantitative milestone thresholds.
- Candidate evidence:
  - The conclusion clearly states that the field is “beyond pure theory but not yet at the point of delivering a generally accepted commercial advantage.”
  - It synthesizes the stages: demonstrated benchmark advantage, plausible but unproven narrow application advantage, and longer-term broad fault-tolerant commercial advantage.
  - It avoids an unsupported precise date and explicitly says timing is highly uncertain.
  - It identifies a concrete milestone: an independently reproducible workload that beats the best classical alternative on a meaningful metric after all overheads and changing classical algorithms are included.
  - It identifies additional milestones involving scalable, economical populations of high-quality logical qubits and standardized benchmarks covering accuracy, time, energy, cost, error correction, verification, and data movement.
- Missing:
  - The milestones are concrete in criteria but are not tied to quantitative thresholds, such as logical-qubit counts, sustained logical depth, error rates, or an explicit economic margin.

### Novel Value

- No material benchmark-external value identified.

## Citations

### Support

#### F1: NOT_EVALUABLE

- Claim: Quantum advantage has been experimentally demonstrated, but mostly for artificial sampling benchmarks rather than useful commercial workloads.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F2: NOT_EVALUABLE

- Claim: There is no broadly accepted demonstration that a quantum computer currently provides a useful, end-to-end advantage for a commercially important task.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F3: NOT_EVALUABLE

- Claim: Quantum simulation is the leading plausible route to early useful advantage, especially for quantum chemistry, materials, catalysts, and strongly correlated systems.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F4: NOT_EVALUABLE

- Claim: Cryptanalysis presents a theoretically decisive advantage, but it is not an imminent commercial advantage for ordinary computing workloads.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F5: NOT_EVALUABLE

- Claim: Optimization and machine-learning advantages are possible but currently much less established than the chemistry and cryptanalysis cases.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F6: NOT_EVALUABLE

- Claim: The central technical barrier is fault tolerance: current devices have noisy physical qubits, whereas useful algorithms require reliable logical qubits built from many physical qubits.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F7: NOT_EVALUABLE

- Claim: Other major barriers are scaling, control, and economics—not merely adding more qubits.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F8: NOT_EVALUABLE

- Claim: The most defensible timeline is staged rather than a single date: benchmark advantage already exists; narrow application advantage is plausible but unproven; broad fault-tolerant commercial advantage remains a longer-term engineering objective.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

### Missing Citations

- Q1: Quantum computers have demonstrated computational advantages on carefully constructed benchmark problems, but not yet a broadly accepted, commercially useful advantage on an economically important task.
- Q2: The strongest demonstrations involve random-circuit sampling and photonic boson sampling, which are designed to be difficult for classical simulation.
- Q3: These sampling demonstrations do not currently replace classical systems or deliver practical business value.
- Q4: A 2019 Google random-circuit-sampling experiment used a 53-qubit superconducting processor and reported a task completed in about 200 seconds that was estimated to take a classical supercomputer much longer.
- Q5: The classical estimate associated with Google's 2019 experiment was subsequently debated and improved.
- Q6: A 2022 Google experiment scaled random-circuit sampling to 70 qubits and reported a large separation from classical simulation while treating the task as a benchmark rather than a commercial application.
- Q7: Photonic experiments including Jiuzhang and related Gaussian-boson-sampling work reported sampling distributions believed to be difficult to reproduce classically, but used specialized benchmark instances rather than economically useful computations.
- Q8: There is no broadly accepted demonstration that a quantum computer currently provides a useful, end-to-end advantage for a commercially important task.
- Q9: IBM quantum-utility experiments produced useful-looking results for some condensed-matter and chemistry calculations through error mitigation and circuit-quality improvements, but did not establish a durable advantage over state-of-the-art classical algorithms on a business-relevant problem.
- Q10: Quantum annealing has generated commercial deployments and application experiments, but evidence for a general, reproducible advantage over optimized classical optimization and heuristic methods remains mixed and problem-dependent.
- Q11: Quantum simulation is the leading plausible route to early useful advantage, especially in quantum chemistry, materials, catalyst design, and strongly correlated systems.
- Q12: Quantum systems can represent quantum states without the exponential state-space representation required by many classical methods, making chemistry and materials a natural target.
- Q13: Fault-tolerant algorithm studies estimate that valuable chemistry calculations may require millions or more physical qubits, depending on algorithmic and hardware assumptions.
- Q14: Near-term variational and error-mitigated methods have demonstrated small calculations but face optimization instability, sampling cost, noise, and strong competition from classical methods.
- Q15: Shor's algorithm can factor large integers and compute discrete logarithms in polynomial time, threatening RSA, finite-field Diffie–Hellman, and elliptic-curve cryptography once a sufficiently large fault-tolerant quantum computer exists.
- Q16: Resource estimates for factoring cryptographically relevant RSA keys generally require very large fault-tolerant machines, while current processors are far short in logical-qubit capability and runtime reliability.
- Q17: The practical response to quantum cryptographic risk is migration to post-quantum cryptography, and NIST finalized its first principal post-quantum standards in 2024.
- Q18: Optimization and machine-learning advantages are possible but less established than the chemistry and cryptanalysis cases.
- Q19: Proposed quantum optimization algorithms, including QAOA and quantum annealing approaches, have not been shown to provide a general asymptotic or practical advantage on realistic industrial instances.
- Q20: Quantum machine-learning proposals often assume cheap loading of classical data into quantum states, and state preparation and measurement can remove the claimed speedup.
- Q21: The central technical barrier is fault tolerance: current devices use noisy physical qubits, whereas useful algorithms require reliable logical qubits constructed from many physical qubits.
- Q22: Two-qubit gate errors, measurement errors, leakage, crosstalk, frequency collisions, and correlated noise accumulate with circuit depth.
- Q23: Error correction can suppress logical errors only when physical error rates and decoder performance are sufficiently good, typically below a fault-tolerance threshold.
- Q24: Surface-code and related architectures commonly require hundreds to thousands of physical qubits per logical qubit at useful operating points, with additional overhead for magic-state factories and logical operations.
- Q25: Current systems do not yet provide the large, stable populations of long-lived logical qubits needed for deep chemistry or factoring circuits.
- Q26: Major barriers beyond qubit count include scaling, control, and economics.
- Q27: Increasing qubit count while preserving fidelity requires manufacturable devices, uniform components, high-bandwidth control, cryogenic or vacuum infrastructure, and scalable calibration systems.
- Q28: Quantum error correction consumes substantial measurement, wiring, classical-compute, and cooling resources, and practical advantage must include data movement, state preparation, verification, energy, capital cost, and workflow integration.
- Q29: Benchmark advantage has already been demonstrated, narrow application advantage is plausible but unproven, and broad fault-tolerant commercial advantage remains a longer-term engineering objective.
- Q30: Industry and academic forecasts commonly place useful fault-tolerant machines in a period ranging from the late 2020s to the 2030s or later, but these are forecasts rather than evidence.
- Q32: Claims about the size of quantum advantage in random-circuit sampling have changed as classical simulation algorithms and supercomputers improved.
- Q33: Quantum-utility and error-mitigation results are difficult to compare because classical baselines, precision targets, verification methods, and total resource accounting are not always identical.
- Q34: Resource estimates for chemistry and factoring can differ by orders of magnitude because of assumptions about algorithms, error-correction codes, physical error rates, connectivity, parallelism, and required precision.
- Q35: Commercial claims from quantum-annealing and hybrid-computing vendors may show value for a particular customer or workflow without establishing a general quantum speedup.
- Q37: Quantum computing is beyond pure theory but not yet at the point of delivering a generally accepted commercial advantage.
- Q38: The most credible future application areas are fault-tolerant simulation of quantum chemistry and materials, followed by cryptanalysis if large fault-tolerant machines are built; optimization and machine learning remain speculative and problem-dependent.
- Q39: The decisive milestone is a scalable, economical supply of high-quality logical qubits rather than merely a larger count of noisy physical qubits.
- Q40: Until scalable logical qubits are demonstrated, quantum computers should be viewed commercially as research platforms, cloud-accessible experimentation systems, and possible sources of specialized future capability rather than replacements for classical computing.

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

1. R7: Assess the reliability and limits of the evidence used to support the maturity judgment.
2. 38 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ae3a5680c375b6650be217402137fd59a302eee5fb85b0bc360a9292a5734293`
- Candidate report hash: `17b9435da465c5b16eacc3f9837371efc895f04788276593e1167d718ef1ce0a`
- LLM calls: 2
- Evaluated at: 2026-09-01T05:59:57.145882+00:00
