# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** quantum-commercial-advantage

**System Version:** llm-only-baseline-v0

**Model:** gpt-5.6-luna

## Summary

- Overall: 55.0 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.75
- Coverage: 0.75
- Depth: 0.75
- Citation quality: 0.00
- Citation validity: 0.00
- Citation support: 0.00
- Citation completeness: 0.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report provides useful definitions and relevant comparison metrics, but omits the required time boundary and only partially formalizes the theoretical-versus-projected distinction.
- Candidate evidence:
  - The report defines four levels, including “Quantum computational advantage,” “Quantum utility,” “Commercial advantage,” and “Broad or general-purpose advantage.”
  - It states that commercial comparison must include “cost,” “quantum hardware access and queueing,” “error mitigation or error correction overhead,” “data-loading and readout costs,” “reliability and repeatability,” and the value of the improved answer.
  - It distinguishes benchmark advantage from commercial advantage and theoretical or projected applications.
- Missing:
  - It does not establish a clear evidence date or cutoff period for the assessment.
  - The four categories do not exactly and explicitly separate theoretical algorithmic advantages from hardware-dependent projected advantages; those are discussed later but not defined as formal categories at the outset.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is substantial coverage of representative experiments, their tasks, platforms, claimed separations, and limitations. It correctly separates artificial sampling benchmarks from useful workloads, but the classical-comparison analysis is not fully developed.
- Candidate evidence:
  - The report discusses Google’s 2019 Sycamore random-circuit-sampling experiment, including the 53-qubit platform, the reported approximately 200-second runtime, and Google’s classical-runtime estimate.
  - It discusses 2020 Chinese Gaussian boson-sampling and superconducting random-circuit-sampling experiments, including their limitations concerning verification, loss, distinguishability, and improved classical algorithms.
  - It discusses Google Willow’s 2024 below-threshold error-correction result and distinguishes that milestone from a commercially useful application.
  - It separately discusses quantum simulation, optimization, machine learning, and boson sampling rather than treating all demonstrations as equivalent.
- Missing:
  - The report gives limited concrete detail on the strongest classical comparison methods, hardware assumptions, or quantitative revisions for the representative sampling claims.
  - Some experimental claims are summarized at a high level without identifying independent replications or specific classical critiques.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report gives a well-supported overall negative assessment and identifies the relevant overheads, but it does not closely evaluate a specific commercial workload with an end-to-end quantitative comparison.
- Candidate evidence:
  - The executive summary says there is “not yet” a “generally accepted, economically valuable advantage on a real commercial task.”
  - The report says no broadly accepted optimization advantage exists after accounting for “problem encoding,” “embedding overhead,” “parameter tuning,” “repeated sampling,” “classical preprocessing and postprocessing,” “hardware access time,” and solution quality.
  - The definition of commercial advantage includes classical and quantum operating costs, access and queueing, error mitigation or correction, data loading, integration, reliability, and repeatability.
  - It explicitly notes that classical algorithms “often close or eliminate the apparent advantage” in optimization and that classical methods have improved sampling claims.
- Missing:
  - The report does not examine a specific economically meaningful end-to-end workload in enough detail to demonstrate how the full comparison would work.
  - It does not provide concrete measured cost, throughput, latency, or solution-quality results for a candidate commercial application.
  - The negative conclusion is broad and largely based on synthesis rather than cited evidence from named end-to-end commercial comparisons.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: The major theoretical candidates, claimed benefits, assumptions, and practical obstacles are covered well. The main gap is the limited use of concrete resource estimates and roadmap analysis outside cryptography.
- Candidate evidence:
  - For chemistry and materials, it explains the potential polynomial-versus-exponential representation advantage and lists phase estimation, block encoding, and related algorithms.
  - For Shor’s algorithm, it identifies factoring and discrete logarithm advantages and gives resource estimates of “hundreds of thousands to millions of physical qubits,” with potentially more under conservative assumptions.
  - For amplitude estimation, it states the ideal scaling improvement from approximately O(1/ε²) to O(1/ε).
  - For linear algebra and quantum machine learning, it identifies assumptions including sparse matrices, efficient state preparation, quantum data access, low condition numbers, and limited output extraction.
  - It repeatedly labels current claims as theoretical, says estimates vary, and distinguishes roadmaps and forecasts from demonstrated capability.
- Missing:
  - The report does not provide detailed, workload-specific resource estimates for chemistry, materials, or amplitude-estimation applications.
  - It mentions company roadmaps only generally and does not analyze particular roadmap assumptions, milestones, or failure risks.
  - The distinction between asymptotic complexity advantages and realistic end-to-end resource estimates could be made more systematic across all application areas.

### R5

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report compares many relevant areas and gives a plausible prioritization, but the evidence base and depth are uneven across applications.
- Candidate evidence:
  - The application table compares random sampling, chemistry, materials, cryptanalysis, finance Monte Carlo, optimization, machine learning, drug discovery, industrial chemistry, and networking.
  - The report calls fault-tolerant chemistry and materials simulation “the strongest long-term application area,” while describing cryptanalysis as theoretically clear but not imminent.
  - It characterizes optimization as uncertain because of problem-specific classical baselines and machine learning as weak because of data-loading and training issues.
  - It distinguishes benchmark value, scientific utility, theoretical promise, and commercial value in statements such as “Real quantum advantage, little direct business value” for sampling.
- Missing:
  - Several areas in the table receive only brief assessments rather than a developed comparison with competing application areas.
  - The report does not provide much direct evidence for why chemistry or materials are stronger than specific classical alternatives in commercially relevant workflows.
  - Finance, drug discovery, and scientific computing are discussed mainly through theoretical requirements rather than demonstrated scientific usefulness or commercial evidence.

### R6

- Coverage: 1.00
- Depth: 1.00
- Rationale: This requirement is fully addressed. The report prioritizes the main barriers, explains their impact on useful workloads, and distinguishes general obstacles from architecture-specific constraints.
- Candidate evidence:
  - It identifies fault tolerance and logical-qubit reliability as the central barrier and explains the need for below-threshold physical error rates, syndrome measurement, decoding, logical gates, state preparation, and measurement.
  - It explains physical-to-logical overhead, including code choice, connectivity, target error rate, algorithm depth, wiring, cryogenics or vacuum, control, decoding, calibration, heat management, and manufacturing yield.
  - It discusses circuit depth, non-Clifford and magic-state overhead, ancillas, repetitions, state preparation, and error-correction cycles.
  - It addresses scaling barriers for superconducting, trapped-ion, neutral-atom, photonic, and semiconductor-spin platforms, identifying platform-specific constraints such as cryogenic wiring, laser control, atom loss, photon loss, and device variability.
  - It also explains general algorithmic, benchmarking, software, error-mitigation, and system-economic barriers and ties them to useful workloads.
- Missing:

### R7

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes moving baselines and source-quality issues, but evidence provenance and disagreement analysis are too general for strong evidence-quality coverage.
- Candidate evidence:
  - The report notes that classical algorithms improved after the Sycamore claim and that competing researchers substantially revised the classical-runtime estimate.
  - It discusses tensor-network simulation, Monte Carlo, approximate sampling, GPU implementations, specialized heuristics, and quantum-inspired algorithms as moving classical baselines.
  - It cautions that company terms such as “quantum advantage,” “fault tolerant,” and “enterprise-ready” should be evaluated carefully and lists criteria for meaningful claims.
  - The source list includes primary experiments, theoretical work, National Academies material, NIST publications, and industry analyses, with the latter explicitly described as forecasts rather than evidence of achieved advantage.
- Missing:
  - It does not identify or analyze specific independent replications or named classical red-team critiques beyond general references to competing researchers.
  - It does not report material disagreements in sufficient detail, such as how competing estimates differ or which assumptions drive the disagreement.
  - Most substantive claims lack inline citations, making it difficult to connect evidence to conclusions.
  - It gives limited discussion of uncertainty in the negative conclusion that no commercial advantage has been demonstrated, including the limits of public evidence and proprietary customer results.
  - It does not clearly distinguish vendor claims from independent validation for each major experimental result.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report provides a clear and reasonably calibrated maturity judgment with concrete milestones, but the timeline projections and evidentiary basis could be more rigorously qualified.
- Candidate evidence:
  - The report gives a clear synthesis: narrow benchmark-defined advantage exists, but “not yet” commercially useful general advantage.
  - It offers a calibrated conclusion that the earliest credible benefits may emerge within the next decade while emphasizing high uncertainty.
  - It identifies measurable milestones including below-threshold logical error rates at increasing code sizes, long-lived logical qubits, fault-tolerant non-Clifford gates, end-to-end application demonstrations, strong classical comparisons, and reproducible economic benefits.
  - It explicitly warns that raw qubit count is not the key metric and instead emphasizes large numbers of high-quality logical qubits with useful gate speeds and manageable overhead.
- Missing:
  - The timeline statements, including “several years,” “at least a decade,” and “2030s or later,” are still relatively specific projections without a quantitative evidentiary basis, even though uncertainty is acknowledged.
  - The synthesis could more explicitly distinguish the maturity of experimentally demonstrated advantage, theoretical opportunity, projected hardware capability, and commercial deployment in one consolidated decision framework.
  - The conclusion relies primarily on the report’s qualitative synthesis rather than directly cited current evidence.

### Novel Value

- The report offers a useful end-to-end framing that separates benchmark advantage, quantum utility, commercial advantage, and broad general-purpose advantage.
- It emphasizes that logical-qubit quality, sustained fault-tolerant computation, and full system economics matter more than headline physical-qubit counts.
- It synthesizes application-specific promise with practical barriers and moving classical baselines rather than treating theoretical speedups as demonstrated commercial benefits.

## Citations

### Support

### Missing Citations

- Q1: Quantum computers have demonstrated computational advantages over classical computers, primarily on artificial benchmark problems such as random-circuit sampling and boson sampling.
- Q2: No generally accepted, economically valuable quantum advantage on a real commercial task has been publicly demonstrated.
- Q3: Random-circuit sampling experiments have demonstrated tasks that are difficult or infeasible for known classical simulation methods.
- Q4: Google reported in 2019 that its 53-qubit Sycamore processor completed a random-circuit-sampling task in about 200 seconds that it estimated would take a classical supercomputer thousands of years.
- Q5: Classical algorithms improved after the Sycamore publication, substantially reducing the original estimate of the classical runtime.
- Q6: Researchers associated with the University of Science and Technology of China reported large Gaussian-boson-sampling and superconducting random-circuit-sampling demonstrations in 2020.
- Q7: Google reported in 2024 that its Willow processor demonstrated below-threshold quantum error correction, with larger error-correcting codes producing lower logical error rates.
- Q8: Boson-sampling experiments have produced increasingly large demonstrations, but verification becomes difficult as systems grow and loss, photon distinguishability, and sampling noise complicate claims.
- Q9: Quantum simulation experiments have demonstrated small molecular and material simulations, spin-system dynamics, Fermi-Hubbard-type models, components of lattice gauge theories, quantum dynamics, phase transitions, and variational molecular-energy estimates.
- Q10: Most current quantum-simulation experiments have not shown a decisive end-to-end advantage over the best classical chemistry, materials, or physics methods.
- Q11: There is no broadly accepted evidence that quantum optimization systems outperform strong classical optimization methods on commercially relevant instances after accounting for relevant overheads.
- Q12: D-Wave has reported performance advantages for particular annealing workloads, and some customers use quantum annealers experimentally.
- Q13: There is no accepted commercial quantum-machine-learning advantage today.
- Q14: Quantum chemistry and materials are generally considered among the strongest long-term quantum-computing application areas.
- Q15: A sufficiently large fault-tolerant quantum computer could factor large integers and solve discrete logarithms using Shor’s algorithm, threatening RSA, Diffie–Hellman, elliptic-curve cryptography, and related public-key systems.
- Q16: A useful attack on RSA-2048 is commonly estimated to require hundreds of thousands to millions of physical qubits, potentially more under conservative assumptions.
- Q17: Governments and companies are migrating toward post-quantum cryptography before a cryptographically relevant quantum computer exists because encrypted data can be harvested now and decrypted later.
- Q18: Quantum amplitude-estimation algorithms can, in ideal fault-tolerant settings, improve Monte Carlo error scaling from approximately O(1/ε²) to O(1/ε).
- Q19: Quantum algorithms for linear systems, matrix operations, search, and sampling can have large asymptotic speedups under assumptions such as sparsity, efficient state preparation, suitable data access, low condition numbers, and limited output extraction.
- Q20: A logical qubit may require anywhere from hundreds to many thousands of physical qubits, depending on hardware and algorithm parameters.
- Q21: Chemistry, cryptography, and amplitude-estimation applications may require from hundreds to millions of logical qubits depending on the problem and algorithm, potentially implying millions or more physical qubits.
- Q22: No quantum-computing hardware platform has established a decisive scaling advantage over the others.
- Q23: Classical improvements in tensor-network simulation, Monte Carlo, approximate sampling, GPU implementations, specialized heuristics, and quantum-inspired algorithms can reduce or eliminate apparent quantum advantages.
- Q24: Error mitigation can extend the usefulness of noisy processors but often substantially increases circuit executions and does not provide the same guarantees as error correction.
- Q25: Current processors are generally useful for algorithm development, hardware research, education, benchmarking, small scientific simulations, error-mitigation experiments, and proof-of-concept customer projects, but generally do not provide reliable economic advantage.
- Q26: The earliest credible commercial benefits may emerge in specialized applications within the next decade, while broad economically decisive advantages depend on unresolved fault-tolerance, scaling, algorithmic-overhead, and system-economics challenges.

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
2. 26 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ae3a5680c375b6650be217402137fd59a302eee5fb85b0bc360a9292a5734293`
- Candidate report hash: `a532d9166f82e09ac012a767d50e9854267ac809fe3645f9160cae034aa4359a`
- LLM calls: 2
- Evaluated at: 2026-09-01T01:01:41.814584+00:00
