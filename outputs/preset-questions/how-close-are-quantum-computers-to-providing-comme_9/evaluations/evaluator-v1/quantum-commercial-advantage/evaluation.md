# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** quantum-commercial-advantage

**System Version:** llm-only-baseline-v0

**Model:** gpt-5.6-luna

## Summary

- Overall: 55.8 / 100
- Evaluation completeness: 80%
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
- Rationale: The report supplies most of the required conceptual distinctions and relevant comparison metrics, but it does not set a clear time boundary. Definitions are substantially present but somewhat distributed and informal.
- Candidate evidence:
  - The Summary distinguishes demonstrated benchmark advantage, commercially useful advantage, theoretical promise, and projected fault-tolerant advantages.
  - The report distinguishes benchmark/sampling tasks from application-level advantage and discusses metrics including speed, cost, accuracy, wall-clock time, energy, capital cost, and total workflow cost.
  - The Conflicts and Uncertainty section explicitly notes that “quantum advantage” can mean asymptotic speedup, classical hardness, or practical cost/performance advantage.
- Missing:
  - No explicit evidence date or cutoff period is stated.
  - The categories are discussed throughout the report rather than defined in a single precise scope statement.
  - The distinction between theoretical algorithmic advantage and hardware-dependent projection is present but not fully formalized for every category.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report correctly identifies representative superconducting and photonic demonstrations and avoids equating them with useful applications. Coverage is substantial, but the experimental comparisons and limitations are not consistently detailed enough for full credit.
- Candidate evidence:
  - Finding 1 describes Google’s 2019 53-qubit random-circuit-sampling experiment, its claimed approximately 200-second result, and the much longer original classical estimate.
  - It discusses Google’s 2022 70-qubit random-circuit-sampling result and identifies it as a benchmark rather than a commercial application.
  - It covers photonic Jiuzhang and Gaussian-boson-sampling experiments as specialized sampling demonstrations.
  - The report notes that classical simulation methods and supercomputer improvements weakened or changed the original size of the claimed separation.
- Missing:
  - The classical comparison is not consistently quantified or tied to the strongest practically relevant classical implementations.
  - The report gives limited experimental detail about verification, sampling fidelity, or the precise platform and limitations of each photonic demonstration.
  - It does not discuss a wider range of representative experiments, such as specific logical-qubit, quantum-utility, or application-oriented demonstrations, in comparable task/platform/result/classical-baseline detail.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The conclusion is well calibrated and the relevant accounting issues are recognized. However, the report lacks a concrete economically meaningful comparison and detailed accounting of all end-to-end overheads.
- Candidate evidence:
  - Finding 2 states that there is “no broadly accepted demonstration” of useful, end-to-end advantage on a commercially important task.
  - It defines application-level advantage as being faster, cheaper, more accurate, or otherwise better than the best classical workflow.
  - It discusses IBM quantum-utility and error-mitigation experiments, noting that they did not establish durable advantage over state-of-the-art classical algorithms.
  - It notes mixed, problem-dependent evidence for quantum annealing and explicitly says commercial claims may not establish general speedup.
  - Finding 7 lists state preparation, error correction, queueing, verification, energy, capital cost, and workflow integration as part of the full baseline.
- Missing:
  - The report does not provide a concrete workload-level end-to-end comparison with measured quantum and classical runtime, cost, quality, or throughput.
  - Subsequent classical algorithms are acknowledged generally but not illustrated through a specific overturned or weakened claim.
  - System availability, repeated-run requirements, and preprocessing/postprocessing are mentioned only generally rather than evaluated in a representative case.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report clearly separates established algorithmic results such as Shor’s algorithm from hardware-dependent projections and identifies important assumptions. It would need more systematic complexity and resource-condition treatment across application areas for full credit.
- Candidate evidence:
  - For cryptanalysis, the report identifies Shor’s polynomial-time factoring and discrete-logarithm advantage and explains the requirement for a sufficiently large fault-tolerant machine.
  - For chemistry, it explains the state-representation motivation and identifies assumptions involving molecule, precision, code, hardware, and algorithm choice.
  - It labels million-plus physical-qubit chemistry estimates and RSA factoring estimates as resource estimates whose values vary with assumptions.
  - For optimization and machine learning, it identifies input-model and data-loading assumptions and says proposed benefits are projections rather than demonstrated general benefits.
- Missing:
  - Complexity or performance benefits are not stated with comparable precision for chemistry, optimization, or machine learning.
  - The report does not systematically separate asymptotic theoretical speedups, heuristic advantages, and concrete hardware projections for each candidate area.
  - Data-access, communication, precision, and verification conditions are discussed but not tied to specific end-to-end resource estimates or algorithms in most areas.

### R5

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report compares several important candidate areas and explains why chemistry and cryptanalysis appear stronger than optimization and machine learning. Coverage is incomplete across application categories and the scientific-versus-commercial distinction is not consistently developed.
- Candidate evidence:
  - Finding 3 identifies chemistry and materials simulation as the leading plausible route and lists catalysts, batteries, superconductors, and correlated-electron systems.
  - Finding 4 treats cryptanalysis as theoretically decisive but engineering-limited and distinguishes it from ordinary commercial workloads.
  - Finding 5 compares optimization and machine learning, noting strong classical heuristics and data-loading limitations.
  - The Conclusion ranks chemistry/materials and cryptanalysis ahead of optimization and machine learning.
- Missing:
  - Scientific usefulness and commercial value are not separately evaluated in a consistent way for each application area.
  - Finance and scientific computing beyond chemistry/materials receive little or no substantive treatment.
  - The comparison among areas is mainly qualitative; it lacks concrete workload, market, or deployment considerations explaining why one area would mature earlier than another.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is a strong qualitative barrier analysis tied to useful workloads, not merely a specification list. Full coverage would require clearer prioritization, architecture-specific comparison, and more explicit quantitative scale requirements.
- Candidate evidence:
  - Finding 6 explains physical gate, measurement, leakage, crosstalk, correlated-noise, and circuit-depth problems and connects them to logical-error accumulation.
  - It discusses error-correction overhead, logical-qubit populations, surface-code physical-to-logical overhead, magic-state factories, and decoder performance.
  - Finding 7 addresses manufacturability, component uniformity, control bandwidth, calibration, cryogenic or vacuum infrastructure, real-time decoding, wiring, cooling, and classical feedback.
  - The report explains that useful workloads require sustained populations of long-lived logical qubits rather than merely more noisy physical qubits.
- Missing:
  - The barriers are not explicitly prioritized beyond identifying fault tolerance as central.
  - Connectivity and routing, fabrication/material variability, photon loss, and other architecture-specific constraints are not treated in comparable detail.
  - The report does not clearly label which barriers are universal versus superconducting-, ion-, neutral-atom-, or photonic-specific.
  - Quantitative thresholds for logical error rates, logical depth, or scale are largely absent.

### R7

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report recognizes the main evidence-quality distinctions and important uncertainties, especially classical red-team effects and roadmap uncertainty. Depth is limited because the source list is not usable and the report does not substantively document independent replication or source-by-source reliability.
- Candidate evidence:
  - The report distinguishes experimental demonstrations, classical simulation analyses, theoretical algorithm studies, resource estimates, industry roadmaps, and vendor claims.
  - It notes that Google’s original classical-runtime estimate was debated and improved, and that sampling claims change with classical algorithms and hardware.
  - It discusses inconsistent definitions of advantage and uncertainty in chemistry and factoring resource estimates.
  - It states that the negative commercial conclusion is limited and that individual firms may report application benefits without consensus validation.
- Missing:
  - The report does not identify specific independent replications or critiques in enough detail, despite referring generally to rebuttals and analyses.
  - The cited source IDs are not accompanied by usable links, quotations, bibliographic details, or source-specific attribution in the body.
  - Vendor claims, primary experiments, independent analyses, and theoretical work are listed in the source inventory but are not systematically weighed for reliability.
  - Material disagreements are described generally rather than tied to named competing results or quantified changes.

### R8

- Coverage: 1.00
- Depth: 0.75
- Rationale: The report provides a clear, calibrated synthesis answering the question, separates demonstrated from projected maturity, avoids unsupported precise dates, and identifies evidence that would change the assessment. Its depth is slightly limited by the absence of quantitative milestone thresholds.
- Candidate evidence:
  - The Conclusion states that quantum computing is beyond pure theory but not yet at a generally accepted commercial advantage.
  - Finding 8 gives a staged judgment: benchmark advantage exists, narrow application advantage is plausible but unproven, and broad fault-tolerant commercial advantage remains a longer-term objective.
  - The report avoids committing to a single precise date and explicitly describes late-2020s-to-2030s forecasts as uncertain projections.
  - It identifies concrete milestones: independently reproducible commercially relevant workloads, transparent classical baselines, total-cost accounting, sustained low logical-error rates, and validated platform-specific resource estimates.
- Missing:
  - The milestone conditions are concrete but are not accompanied by quantitative acceptance thresholds, such as target logical error rates, sustained logical depth, or cost/performance margins.
  - The conclusion could more explicitly distinguish how close the field is for different application classes rather than primarily giving a global assessment.

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

- Q1: Quantum computers have demonstrated computational advantages on carefully constructed benchmark problems, especially sampling problems, but not a broadly accepted commercially useful advantage on an economically important task.
- Q2: Google reported a 2019 random-circuit-sampling experiment using a 53-qubit superconducting processor and claimed the task took about 200 seconds, compared with a much longer classical estimate.
- Q3: Google reported a 2022 random-circuit-sampling experiment scaled to 70 qubits and described a large separation from classical simulation.
- Q4: Photonic experiments, including Jiuzhang and Gaussian-boson-sampling work, reported sampling distributions believed to be difficult to reproduce classically.
- Q5: There is no broadly accepted, independently validated, scalable, end-to-end quantum advantage for a commercially important task at commercially relevant scale.
- Q6: IBM quantum-utility experiments used error mitigation and circuit-quality improvements to produce useful-looking results for some condensed-matter and chemistry calculations, but did not establish durable advantage over state-of-the-art classical algorithms on a business-relevant problem.
- Q7: Quantum annealing has generated commercial deployments and application experiments, but evidence for a general, reproducible advantage over optimized classical methods remains mixed and problem-dependent.
- Q8: Quantum simulation is presented as the leading plausible route to early useful advantage, particularly in quantum chemistry, materials, catalysts, and strongly correlated systems.
- Q9: Proposed quantum-simulation applications include reaction energetics, catalyst design, battery materials, superconductors, and correlated-electron models.
- Q10: Fault-tolerant chemistry calculations may require millions or more physical qubits, depending on the molecule, precision, error-correction code, hardware assumptions, and algorithmic improvements.
- Q11: Near-term variational and error-mitigated methods have demonstrated small calculations but face optimization instability, sampling cost, noise, and competition from classical methods such as tensor networks, quantum Monte Carlo, coupled cluster, and density functional methods.
- Q12: Shor’s algorithm would factor large integers and compute discrete logarithms in polynomial time, threatening RSA, finite-field Diffie–Hellman, and elliptic-curve cryptography once a sufficiently large fault-tolerant quantum computer exists.
- Q13: Resource estimates for factoring cryptographically relevant RSA keys generally require very large fault-tolerant machines, and current processors are many orders of magnitude short in logical-qubit capability and runtime reliability.
- Q14: NIST finalized its first principal post-quantum cryptography standards in 2024.
- Q15: Optimization and machine-learning advantages are possible but less established than the chemistry and cryptanalysis cases.
- Q16: Quantum optimization algorithms, including QAOA and quantum annealing approaches, have not been shown to provide a general asymptotic or practical advantage on realistic industrial instances.
- Q17: Quantum machine-learning proposals often assume that data can be loaded into quantum states cheaply, while state preparation and measurement can remove claimed speedups for conventional classical datasets.
- Q18: The central technical barrier is fault tolerance: current devices use noisy physical qubits, while useful algorithms require reliable logical qubits constructed from many physical qubits.
- Q19: Two-qubit-gate errors, measurement errors, leakage, crosstalk, frequency collisions, and correlated noise accumulate with circuit depth, while error correction requires sufficiently low physical error rates and adequate decoder performance.
- Q20: Surface-code and related architectures commonly require hundreds to thousands of physical qubits per logical qubit at useful operating points, with additional overhead for magic-state factories and logical operations.
- Q21: Current systems do not yet provide large, stable populations of long-lived logical qubits needed for deep chemistry or factoring circuits.
- Q22: Scaling quantum systems while preserving fidelity requires manufacturable devices, uniform components, high-bandwidth control, cryogenic or vacuum infrastructure, and calibration systems whose complexity remains manageable.
- Q23: Quantum error correction consumes measurement, wiring, classical-compute, and cooling resources, and logical operations require fast, accurate decoding and real-time feedback.
- Q24: A practical quantum advantage must outperform the full classical baseline, including data movement, state preparation, error correction, queueing, verification, energy, capital cost, and workflow integration.
- Q26: Industry and academic forecasts commonly place useful fault-tolerant machines in a period ranging from the late 2020s to the 2030s or later.

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
2. 25 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ae3a5680c375b6650be217402137fd59a302eee5fb85b0bc360a9292a5734293`
- Candidate report hash: `17b9435da465c5b16eacc3f9837371efc895f04788276593e1167d718ef1ce0a`
- LLM calls: 2
- Evaluated at: 2026-09-01T05:49:57.388636+00:00
