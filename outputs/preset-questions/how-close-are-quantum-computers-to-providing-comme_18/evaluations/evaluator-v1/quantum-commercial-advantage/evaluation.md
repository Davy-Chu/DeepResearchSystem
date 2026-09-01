# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** quantum-commercial-advantage

**System Version:** evidence-ledger-decomposer-v1

**Research Model:** gpt-4o-mini

**Evaluator Model:** gpt-5.6-luna

## Summary

- Overall: 25.0 / 100
- Evaluation completeness: 100%
- Coverage: 0.28
- Depth: 0.22

## Coverage and Depth

### R1

- Coverage: 0.00
- Depth: 0.00
- Rationale: The report uses terms such as “practical,” “theoretical,” and “commercial,” but does not define them or delimit the evidence period.
- Candidate evidence:
- Missing:
  - No evidence date or time boundary is stated.
  - The report does not define experimentally demonstrated advantage, commercially useful end-to-end advantage, theoretical algorithmic advantage, or projected advantage.
  - It does not establish comparison metrics such as runtime, cost, throughput, reliability, or solution quality.

### R2

- Coverage: 0.25
- Depth: 0.25
- Rationale: The Q-CTRL claim is a potentially relevant example, but it is presented as an unsupported headline rather than an analysis of an experimental claim against a classical baseline.
- Candidate evidence:
  - Finding 1 states: “Q-CTRL has demonstrated a practical quantum advantage with a 3,000 times speedup in materials simulation. [S3]”
  - Finding 1 also generally claims that quantum computers can outperform classical systems for specific problems.
- Missing:
  - The report does not describe the underlying task, quantum platform, experimental setup, workload, or claimed quantum result in sufficient detail.
  - It gives no description of the classical comparator, its hardware, algorithm, or whether the comparison was independently validated.
  - It does not discuss limitations or distinguish sampling/benchmark demonstrations from useful scientific or commercial workloads.
  - Other representative demonstrations, such as sampling or circuit benchmarks, are not evaluated.

### R3

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report discusses commercial domains and a claimed materials-simulation speedup, but supplies no evidence that a complete economically relevant workflow currently beats a classical alternative.
- Candidate evidence:
  - Finding 4 claims quantum computing is “beginning to show utility in several high-value commercial domains such as drug discovery, grid optimization, and finance.”
  - The conclusion says quantum computing is “on the brink of achieving practical advantages over classical computing.”
- Missing:
  - No economically meaningful workload is examined using an end-to-end metric.
  - The report does not account for state preparation, error mitigation or correction, repeated sampling, preprocessing, postprocessing, availability, or operating cost.
  - It does not identify the strongest practically relevant classical alternative or compare against it.
  - It does not address whether improved classical algorithms weaken the stated claims.
  - The commercial-utility conclusion is asserted rather than demonstrated.

### R4

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report recognizes a theoretical category but does not explain the claimed benefits or the conditions required for them to become end-to-end advantages.
- Candidate evidence:
  - Finding 2 states that quantum computing offers “theoretical advantages in simulation, optimization, and cryptography.”
  - Finding 2 mentions “predictive analyses” and “simulation studies” indicating potential speedups.
- Missing:
  - No complexity advantages are specified, such as polynomial versus exponential scaling or the assumptions behind particular algorithms.
  - The report does not distinguish mathematical algorithmic advantages from hardware-dependent projections, vendor roadmaps, or forecasts.
  - It does not discuss practical resource requirements, including logical-qubit counts, circuit depth, fault tolerance, data loading, sampling, or output extraction.
  - The cited industry predictions are not labeled and assessed explicitly as projections rather than demonstrations.

### R5

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report names several plausible domains but provides no comparative assessment of which are most likely to yield early commercial value.
- Candidate evidence:
  - Finding 1 mentions materials simulation and optimization.
  - Finding 2 mentions simulation, optimization, cryptography, supply chains, and drug discovery.
  - Finding 4 mentions drug discovery, energy systems, grid optimization, finance, pharmaceuticals, and materials science.
- Missing:
  - The application areas are listed rather than compared.
  - For each area, the report does not distinguish theoretical promise, scientific usefulness, and commercial value.
  - It does not explain why chemistry/materials, optimization, finance, machine learning, scientific computing, or cryptography have stronger or weaker evidence relative to one another.
  - No application-specific evidence demonstrates an early useful advantage.

### R6

- Coverage: 0.50
- Depth: 0.25
- Rationale: Several central barriers are named, but the treatment is largely a list of specifications and does not connect them to commercially useful computation.
- Candidate evidence:
  - Finding 3 identifies “decoherence, error correction, and the demand for sophisticated operating conditions” as major barriers.
  - It also cites “hardware scaling and error management,” the number of qubits needed for error correction, environmental noise, and scaling issues.
  - The conclusion again identifies decoherence, robust error correction, scalability, and error rates as unresolved issues.
- Missing:
  - The report does not prioritize the barriers or explain which are most limiting for useful workloads.
  - It does not discuss logical error rates, logical-qubit scale, sustained logical circuit depth, connectivity and routing, control and decoding, correlated errors, fabrication variability, or platform-specific constraints in meaningful detail.
  - It does not explain how physical errors and error-correction overhead translate into runtime, cost, data throughput, or workload feasibility.
  - It does not distinguish general barriers from architecture-specific barriers such as cryogenics, photon loss, or platform-dependent control constraints.

### R7

- Coverage: 0.25
- Depth: 0.25
- Rationale: A source list is present, but the evidence is not critically evaluated and the report does not substantiate its confidence levels or conflict assessment.
- Candidate evidence:
  - The report says its findings are “supported by multiple sources.”
  - It lists sources including benchmarking literature, company blogs, industry forecasts, journalism-style sources, and vendor claims.
  - The “Conflicts and Uncertainty” section states: “No material conflict was identified in the retrieved evidence.”
- Missing:
  - The report does not classify or weigh primary experiments, independent replications, classical red-team analyses, theoretical work, vendor claims, and roadmaps.
  - It does not analyze the reliability of the Q-CTRL, Quantinuum, or other vendor claims.
  - It does not report material disagreements or sensitivity to improved classical algorithms.
  - The assertion that no material conflict exists is unsupported and does not address uncertainty in the negative conclusion that commercial advantage has not yet been demonstrated.
  - Many claims rely on secondary, commercial, or promotional sources without explaining their authority or limitations.

### R8

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report provides a clear overall conclusion and names broad unresolved issues, but the maturity judgment is insufficiently evidenced and lacks concrete decision criteria.
- Candidate evidence:
  - The conclusion states that quantum computing is “on the brink of achieving practical advantages over classical computing.”
  - It distinguishes practical applications from “theoretical potential” and identifies decoherence, error correction, scalability, and error rates as remaining issues.
  - It says further research is needed on scalability, error rates, and industry comparisons.
- Missing:
  - The “on the brink” judgment is not calibrated with quantified or workload-specific evidence.
  - The synthesis does not clearly separate demonstrated advantage, theoretical advantage, projected advantage, and commercially useful advantage.
  - It does not identify concrete measurable milestones that would change the assessment, such as demonstrated logical-qubit scale, sustained logical depth, reproducible end-to-end cost or runtime advantage, or independent validation.
  - It does not adequately address uncertainty or avoid relying on the unsupported Q-CTRL and industry-optimism claims.

### Novel Value

- No material benchmark-external value identified.

## Deterministic Diagnostics (Not Scored)

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

1. R1: Set a time boundary and define the categories used to answer the question.
2. R2: Evaluate representative experimental claims of quantum advantage against classical computation.
3. R3: Determine whether commercially useful quantum advantage has been demonstrated.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ae3a5680c375b6650be217402137fd59a302eee5fb85b0bc360a9292a5734293`
- Candidate report hash: `8ccc94f40072803d6d3ab58a4543187a7e1a3f789c9e0c58bd8f03f2bf4bf73e`
- LLM calls: 1
- Evaluated at: 2026-09-01T16:51:11.260819+00:00
