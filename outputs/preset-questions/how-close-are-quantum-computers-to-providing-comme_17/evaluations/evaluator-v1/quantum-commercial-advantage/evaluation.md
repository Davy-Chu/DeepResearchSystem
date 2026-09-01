# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** quantum-commercial-advantage

**System Version:** evidence-ledger-v1

**Research Model:** gpt-4o-mini

**Evaluator Model:** gpt-5.6-luna

## Summary

- Overall: 31.5 / 100
- Evaluation completeness: 100%
- Coverage: 0.32
- Depth: 0.32

## Coverage and Depth

### R1

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report gestures at a demonstrated-versus-projected distinction but does not establish the requested analytical framework.
- Candidate evidence:
  - The report distinguishes noisy current systems from future fault-tolerant systems and says advantages are demonstrated only 'in specific tasks' while practical applications are 'projected'.
- Missing:
  - No evidence date or time boundary is stated.
  - The categories are not explicitly defined as demonstrated computational advantage, end-to-end commercial advantage, theoretical algorithmic advantage, and projected resource/roadmap advantage.
  - No comparison metrics such as runtime, cost, throughput, reliability, solution quality, or end-to-end resource accounting are defined.

### R2

- Coverage: 0.25
- Depth: 0.25
- Rationale: It names two headline claims but supplies almost none of the technical or comparative detail needed to evaluate them.
- Candidate evidence:
  - Finding 1 states that IBM researchers demonstrated an advantage with a '93% success rate in a specific task.'
  - The report also mentions Google's quantum-supremacy result in [S7].
- Missing:
  - The task, hardware platform, circuit or workload, and exact claimed result are not described.
  - The relevant classical comparison, including the algorithm, hardware, runtime, or cost, is absent.
  - Limitations and later classical improvements are not discussed.
  - The report does not distinguish sampling or benchmark separations from useful scientific or commercial workloads; instead it calls the IBM result a 'practical scenario' without substantiation.

### R3

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report implies commercial usefulness has not arrived, but it neither explicitly evaluates the criterion nor provides the required end-to-end evidence.
- Candidate evidence:
  - The conclusion says quantum computing has demonstrated advantages 'in specific tasks' but that 'significant challenges persist.'
  - Finding 3 says current systems cannot effectively solve complex problems at large scales because of noise and scalability issues.
- Missing:
  - There is no direct determination of whether any economically meaningful workload has demonstrated end-to-end advantage.
  - No accounting is given for state preparation, mitigation or correction, repeated sampling, preprocessing, postprocessing, availability, or operating cost.
  - The report does not compare against the strongest practically relevant classical alternative.
  - It does not assess whether improved classical algorithms weakened any claimed advantage.

### R4

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report uses broad claims about exponential speedups and dates but does not separate algorithmic theory from hardware-dependent, resource-constrained projections.
- Candidate evidence:
  - Finding 2 claims potential advantages in 'optimization, cryptography, and simulation tasks' and says quantum computers can solve problems 'exponentially faster.'
  - Finding 2 cites predictions of practical advantages by 2026.
  - Findings 4–6 discuss projected fault-tolerant systems and company roadmaps, including OQC's 2028 and Quantinuum's 2029 targets.
- Missing:
  - No specific algorithms or complexity claims are explained, such as the assumptions behind factoring, amplitude estimation, quantum simulation, or optimization algorithms.
  - Data-loading, oracle, fault-tolerance, precision, sampling, and input/output assumptions are not addressed.
  - No resource estimates are supplied for logical qubits, circuit depth, runtime, error correction, or data access.
  - Company forecasts and roadmaps are not consistently labeled and critically assessed as projections rather than demonstrations.

### R5

- Coverage: 0.25
- Depth: 0.25
- Rationale: Application areas are merely enumerated, with no evidence-based prioritization or application-specific analysis.
- Candidate evidence:
  - Finding 2 lists optimization, cryptography, and simulation as potential application areas and mentions pharmaceuticals and finance in a 2026 prediction.
- Missing:
  - The areas are not compared against one another.
  - For each area, the report does not distinguish theoretical promise, scientific usefulness, and commercial value.
  - Chemistry/materials, scientific computing, machine learning, and other relevant areas are not assessed.
  - No explanation is given for why the evidence is stronger or weaker in any application area.

### R6

- Coverage: 0.50
- Depth: 0.50
- Rationale: Noise, scaling, and fault tolerance receive meaningful high-level attention, but most of the rubric's technically important mechanisms and prioritization are missing.
- Candidate evidence:
  - The report repeatedly identifies noise, decoherence, physical error rates, scalability, qubit management, and fault-tolerant engineering as barriers.
  - Finding 5 specifically emphasizes stable operation of error correction systems and large-scale qubit integration.
  - The sources and findings mention logical qubits, error-correction codes, decoders, ion traps, optical qubits, cryogenic or architecture-related development indirectly through the cited material.
- Missing:
  - The barriers are not prioritized by their effect on useful workloads.
  - There is no explanation of error-correction overhead, required logical-qubit scale, sustained logical circuit depth, connectivity/routing, control, decoding latency, correlated errors, or fabrication/material variability.
  - Platform-specific constraints such as cryogenics, photon loss, or ion-trap limitations are not explained.
  - The report does not clearly separate barriers common to all architectures from architecture-specific barriers.

### R7

- Coverage: 0.25
- Depth: 0.25
- Rationale: A bibliography and confidence labels are insufficient evidence-quality analysis; the report does not critically characterize its evidence base.
- Candidate evidence:
  - The report labels some claims with confidence levels and provides a source list containing academic, government/industry, vendor, media, and blog sources.
  - The report states under 'Conflicts and Uncertainty' that 'No material conflict was identified.'
- Missing:
  - It does not distinguish primary experiments, independent replications, classical red-team analyses, theoretical work, vendor claims, and roadmaps in the discussion.
  - The evidence is heavily dependent on secondary, promotional, or vendor sources, without assessing source authority or methodological quality.
  - It does not report known disagreements or sensitivity to improved classical methods.
  - The assertion that no conflict exists is unsupported and is especially inadequate for controversial advantage claims.
  - Uncertainty in the negative conclusion that commercial advantage has not been demonstrated is not addressed.

### R8

- Coverage: 0.50
- Depth: 0.50
- Rationale: There is a generally appropriate high-level conclusion, but it lacks the evidence-based calibration, milestone criteria, and uncertainty needed for a strong answer.
- Candidate evidence:
  - The conclusion gives a calibrated broad judgment: specific-task advantages have been demonstrated, but practical applications remain projected and noise, scalability, and fault tolerance remain significant challenges.
  - It identifies 2026 as an expected period for meaningful capabilities and mentions 2028 and 2029 milestones in cited findings.
  - The report recognizes that scalable, reliable architecture remains an ongoing challenge.
- Missing:
  - The judgment is not grounded in a careful synthesis of demonstrated benchmark results, theoretical algorithms, projected resources, commercial economics, and application evidence.
  - The 2026 expectation is presented without adequate qualification or justification and is an unsupported precise forecast under the rubric.
  - No concrete measurable milestones are specified, such as a useful workload beating a strong classical baseline on an end-to-end cost/runtime/quality metric, sustained logical operation, or reproducible fault-tolerant performance.
  - The report does not explain what evidence would materially change the assessment.

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
- Candidate report hash: `afaa3d3a561b78d14a24310ee7b65c9de7cc9ddff3df17b5dc6d6987aad4ae2a`
- LLM calls: 1
- Evaluated at: 2026-09-01T16:02:49.748474+00:00
