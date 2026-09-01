# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** quantum-commercial-advantage

**System Version:** baseline-zero

**Research Model:** gpt-4o-mini

**Evaluator Model:** gpt-5.6-luna

## Summary

- Overall: 49.6 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.26
- Coverage: 0.28
- Depth: 0.22
- Citation quality: 0.79
- Citation validity: 1.00
- Citation support: 0.67
- Citation completeness: 0.92
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.00
- Depth: 0.00
- Rationale: The introduction says the report distinguishes practical and theoretical potential, but it supplies neither operational definitions nor a time boundary.
- Candidate evidence:
- Missing:
  - No evidence date or period is stated.
  - The report does not define experimentally demonstrated advantage, commercially useful end-to-end advantage, theoretical algorithmic advantage, or projected/roadmap advantage.
  - It does not specify comparison metrics such as runtime, cost, throughput, reliability, or solution quality.

### R2

- Coverage: 0.25
- Depth: 0.25
- Rationale: There is one specific-sounding demonstration claim and one broad benchmark statement, but almost none of the technical or comparative detail required to evaluate experimental claims.
- Candidate evidence:
  - The report claims that "Q-CTRL has demonstrated practical quantum advantage by achieving a 3,000 times speedup in materials simulation" [S2].
  - It also generally states that benchmarks show quantum algorithms are promising while classical methods remain superior for small to moderate problems [S4].
- Missing:
  - The report does not identify the underlying task, quantum platform, experimental setup, workload size, or what the 3,000-times figure measures.
  - It gives no concrete classical baseline, including whether the comparison used the strongest practical classical method.
  - It does not discuss state preparation, sampling, error mitigation, repetitions, preprocessing, postprocessing, or other limitations.
  - It does not describe representative sampling or benchmark demonstrations and does not distinguish benchmark separations from useful scientific or commercial workloads.

### R3

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report treats a claimed application speedup as evidence relevant to commercialization but does not perform the required end-to-end commercial comparison.
- Candidate evidence:
  - The report says the Q-CTRL materials-simulation result is "relevant to commercial applications."
  - Its conclusion says quantum computing has made strides toward practical advantages in "specific applications like materials simulation," while significant barriers remain.
- Missing:
  - It does not establish that the workload is economically meaningful or that it outperformed the strongest practically relevant classical alternative.
  - It does not provide an end-to-end metric or clarify whether the speedup includes state preparation, error mitigation or correction, repeated runs, classical preprocessing/postprocessing, hardware access, and operating cost.
  - It does not examine subsequent classical algorithms or critiques that might weaken the claim.
  - It does not clearly answer whether commercially useful advantage has actually been demonstrated; relevance to commercial applications is not evidence of commercial advantage.

### R4

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report gestures at theory and forecasts but supplies no algorithmic claims, assumptions, resource analysis, or hardware-dependent projection.
- Candidate evidence:
  - The report states that quantum advantage is "theoretically understood" and that quantum algorithms are promising [S4].
  - It mentions that some sources project significant breakthroughs "years away" [S2] [S5].
- Missing:
  - No important candidate algorithm or application is analyzed in terms of complexity or performance benefit.
  - The report does not state assumptions about fault tolerance, logical-qubit counts, circuit depth, data loading, oracle access, sampling, or input/output costs.
  - It does not provide resource estimates or distinguish them from experiments.
  - Roadmaps and forecasts are listed as sources but are not discussed or labeled as projections.

### R5

- Coverage: 0.25
- Depth: 0.25
- Rationale: Only one application area is mentioned, and even that area is not assessed comparatively or in the required commercial and scientific dimensions.
- Candidate evidence:
  - Materials simulation is identified as a potentially relevant application through the Q-CTRL claim.
  - The report asks which industries will benefit most but leaves this as a stated gap.
- Missing:
  - It does not compare chemistry/materials with optimization, scientific computing, machine learning, finance, cryptography, or other candidate areas.
  - For materials simulation it does not distinguish theoretical promise, scientific usefulness, and commercial value.
  - It provides no evidence-based explanation of why any area is stronger or weaker than competing areas.
  - The many use-case links in the source list are not synthesized into an application assessment.

### R6

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report names several genuine high-level barriers, enough for partial coverage, but offers little causal, quantitative, prioritized, or architecture-specific analysis.
- Candidate evidence:
  - The report identifies "hardware limitations, error rates, and the need for specialized environments to maintain qubit stability" as major barriers.
  - It states that superconducting and trapped-ion systems require extreme conditions, creating scaling challenges [S3].
  - It says noise and error correction affect reliable computation [S2].
- Missing:
  - The report does not explain how these barriers affect useful workloads, such as achievable logical circuit depth, algorithm success probability, or total cost and throughput.
  - It omits logical-qubit scale, error-correction overhead, sustained logical depth, connectivity and routing, control and decoding, correlated errors, fabrication/material variability, and platform-specific issues such as photon loss.
  - It does not prioritize the barriers or distinguish general barriers from architecture-specific ones beyond naming superconducting and trapped-ion systems.
  - It does not explain what thresholds or milestones would constitute adequate performance.

### R7

- Coverage: 0.25
- Depth: 0.25
- Rationale: Confidence labels and a generic disagreement statement provide minimal uncertainty treatment, but the report does not critically assess evidence provenance or competing analyses.
- Candidate evidence:
  - The report labels some claims with confidence levels, including "Medium" for the materials-simulation claim and "High" for general barriers.
  - It acknowledges "differing opinions" about when practical advantage will become widespread and says some sources claim immediate viability while others project years [S2] [S5].
- Missing:
  - It does not classify sources into primary experiments, independent replications or critiques, classical red-team analyses, theory, vendor claims, and roadmaps.
  - The central 3,000-times claim relies chiefly on a Q-CTRL company blog, but the report does not discuss that source's incentives, methodology, or independent validation.
  - It does not report material disagreements about the experimental claim or sensitivity to improved classical methods.
  - It does not explain uncertainty in the negative conclusion that broad commercial advantage is not yet established.
  - Several sources are generic commercial, media, or promotional pages, but source authority and suitability are not evaluated.

### R8

- Coverage: 0.50
- Depth: 0.25
- Rationale: The conclusion is directionally cautious and avoids an unsupported precise date, but it remains generic and does not synthesize the required evidence categories into a specific maturity judgment.
- Candidate evidence:
  - The conclusion says quantum computing has made "notable strides towards practical advantages" in specific applications but that "significant barriers remain."
  - It says timelines for widespread application "vary widely among experts."
  - The report asks how long systems will take to outperform classical systems across broader applications.
- Missing:
  - The synthesis does not clearly separate demonstrated, theoretical, and projected maturity in the final judgment.
  - It does not provide a calibrated answer to how close the field is, beyond broad statements about progress and barriers.
  - It does not identify concrete measurable milestones, such as validated end-to-end advantage against a competitive classical baseline, fault-tolerant logical-qubit scale, circuit depth, or cost/throughput thresholds.
  - It does not explain what evidence would materially change the assessment and provides no support for resolving the claimed materials-simulation result.

### Novel Value

- No material benchmark-external value identified.

## Citations

### Support

#### F1: PARTIALLY_SUPPORTED

- Claim: Quantum computers have recently achieved practical quantum advantage in materials simulation, delivering performance benefits over classical machines.
- Sources: S2, S4
- Rationale: S2 directly reports a recent claimed demonstration of practical quantum advantage in materials simulation, including a solution obtained more than 3,000 times faster than a classical industry-standard alternative. However, the source is a Q-CTRL company blog describing its own demonstration, and the saved excerpt does not establish the claim more broadly for quantum computers generally. S4 discusses industrial quantum-computing evaluations but its saved content does not support practical advantage in materials simulation or a performance benefit over classical machines.
- Supporting text: S2 states that Q-CTRL and IBM demonstrated practical quantum advantage and that an IBM quantum computer achieved a solution “over 3,000 times faster in wall-clock time than the state-of-the-art industry-standard alternative,” in a materials-engineering/Fermionic Simulation context.

#### F2: PARTIALLY_SUPPORTED

- Claim: Quantum advantage, while theoretically understood, is still elusive in many practical applications, with significant regional and task-specific barriers present.
- Sources: S5, S4
- Rationale: The sources support that practical quantum advantage remains limited: S5 says the field is not ready for prime time, that common small-to-moderate business problems will not benefit, and that quantum advantage is still something scientists are striving to achieve. S4 likewise describes significant hurdles to practical application, including low qubit counts, limited connectivity, error susceptibility, scalability, runtime, and solution-quality concerns. However, the supplied text does not establish that quantum advantage is 'theoretically understood' or that barriers are specifically 'regional.'
- Supporting text: S5: “The current field of quantum computers isn’t quite ready for prime time” and “small to moderate-sized problems… will not benefit from quantum computing.” S4: practical use is assessed against “significant hurdles,” including “low qubit counts, limited connectivity, and error susceptibility,” with classical methods expected to remain superior in some cases.

#### F3: SUPPORTED

- Claim: Major technical barriers for quantum computing include hardware limitations, error rates, and the need for specialized environments to maintain qubit stability.
- Sources: S3, S2
- Rationale: S3 directly describes hardware approaches and their differing scalability and stability, explains that qubits are highly sensitive to temperature, electromagnetic interference, and vibrations, and states that specialized infrastructure and near-absolute-zero conditions are often required. S2 explicitly identifies hardware size, errors that degrade performance, and noise and errors that have limited useful results as challenges.
- Supporting text: S3: Quantum computers need highly controlled environments because qubits are extremely sensitive to their surroundings; temperature, electromagnetic interference, and vibrations can cause decoherence. Superconducting systems often require dilution refrigerators and other advanced infrastructure. S2: Quantum computers face challenges involving the size of hardware required and errors that degrade performance; noise and errors have limited useful results.

### Missing Citations

- Q14: The industry is progressing toward greater commercial viability, but timelines for widespread application vary widely among experts.

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
3. R3: Determine whether commercially useful quantum advantage has been demonstrated.
4. 2 cited finding(s) were not fully supported by saved evidence.
5. 1 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ae3a5680c375b6650be217402137fd59a302eee5fb85b0bc360a9292a5734293`
- Candidate report hash: `5e9afbd91f1ae016fc63fa42f0f4821f5889358e7c44c6b3fc6d6f89238878b7`
- LLM calls: 5
- Evaluated at: 2026-09-01T15:19:03.310777+00:00
