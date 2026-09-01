# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** quantum-commercial-advantage

**System Version:** llm-only-baseline-v0

**Research Model:** gpt-4o-mini

**Evaluator Model:** gpt-5.6-luna

## Summary

- Overall: 22.5 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.21
- Coverage: 0.22
- Depth: 0.18
- Citation quality: 0.00
- Citation validity: 0.00
- Citation support: 0.00
- Citation completeness: 0.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.00
- Depth: 0.00
- Rationale: The report uses terms such as “demonstrated advantages,” “theoretical advantages,” and “commercial advantages,” but does not define them or establish a scope boundary.
- Candidate evidence:
- Missing:
  - No evidence date or time boundary is stated.
  - The report does not define demonstrated experimental advantage, commercially useful end-to-end advantage, theoretical algorithmic advantage, or projected advantage as distinct categories.
  - It provides no comparison metrics such as runtime, cost, throughput, reliability, solution quality, or end-to-end resource use.

### R2

- Coverage: 0.25
- Depth: 0.25
- Rationale: There are two brief demonstration claims, but they lack the task-specific evidence and limitations needed to evaluate representative experimental claims.
- Candidate evidence:
  - The report states that “Google's Sycamore processor completed a specific task in 200 seconds that a classical supercomputer would take approximately 10,000 years to complete.”
  - It also claims that “IBM achieved a quantum advantage in chemistry simulations, demonstrating faster computations for small molecules than classical methods.”
- Missing:
  - The Sycamore task is not identified precisely as a sampling or benchmark task, and the report does not describe the platform or experimental setup beyond naming Sycamore.
  - It gives no details about the classical comparison, including the target classical algorithm, hardware, extrapolation, or subsequent improved classical methods.
  - The IBM chemistry claim lacks a task, platform, metric, baseline, and limitations.
  - Factoring is described as a demonstrated advantage in Finding 1, but no factoring experiment or demonstration is provided; this conflates a theoretical algorithm with an experimental result.
  - The report does not distinguish benchmark or sampling separations from useful scientific workloads.

### R3

- Coverage: 0.00
- Depth: 0.00
- Rationale: The report asserts commercial potential but does not determine whether commercially useful quantum advantage has actually been demonstrated.
- Candidate evidence:
- Missing:
  - No economically meaningful workload is evaluated using an end-to-end comparison against the strongest practically relevant classical alternative.
  - The report does not assess state preparation, error mitigation or correction, repeated runs, preprocessing, postprocessing, availability, or operating cost.
  - It does not analyze whether later classical algorithms weakened any claimed advantage.
  - The conclusion merely says “niche applications” and “commercial settings” without identifying a demonstrated commercial workload.

### R4

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report identifies several theoretical algorithms and areas, but gives no meaningful separation between asymptotic theory and hardware-dependent projections or practical resource analysis.
- Candidate evidence:
  - The report names Shor's and Grover's algorithms and says they “provide exponential speedup over classical counterparts for factoring and search problems.”
  - It mentions optimization, cryptography, complex simulations, and quantum machine learning as areas of theoretical potential.
- Missing:
  - The report does not state the assumptions underlying Shor's or Grover's advantages, such as fault-tolerant execution, oracle or data-access assumptions, and sufficiently large inputs.
  - It does not provide resource estimates for logical qubits, circuit depth, error correction, data loading, or runtime.
  - No hardware-dependent projections, company roadmaps, or forecasts are discussed or labeled as projections.
  - It does not explain why practical resource and data-access conditions could prevent an end-to-end advantage.

### R5

- Coverage: 0.25
- Depth: 0.25
- Rationale: Several candidate application areas are listed, but there is almost no application-specific assessment.
- Candidate evidence:
  - The report mentions chemistry simulations, optimization, cryptography, complex simulations, and quantum machine learning.
  - It says quantum computers show potential “in specific areas” and refers to “niche applications.”
- Missing:
  - The areas are not compared against one another or ranked by plausibility of early useful advantage.
  - For each area, the report does not distinguish theoretical promise, scientific usefulness, and commercial value.
  - It does not explain why chemistry, optimization, machine learning, cryptography, or other areas have stronger or weaker evidence than competing areas.
  - The chemistry claim is too vague to establish scientific or commercial relevance.

### R6

- Coverage: 0.50
- Depth: 0.25
- Rationale: The core barriers of error correction, coherence, and scaling are correctly identified, with a little causal explanation, but the treatment is incomplete and not prioritized.
- Candidate evidence:
  - The report identifies “error correction, coherence times, and qubit scaling” as significant barriers.
  - It explains that quantum error correction requires “a high number of physical qubits to create a logical qubit,” affecting scalability.
  - It states that coherence times are “too short for many calculations” and require improvements in materials and qubit design.
  - It also notes that scalable architectures remain challenging.
- Missing:
  - The report does not prioritize the barriers or connect them concretely to useful workloads, sustained logical circuit depth, or end-to-end runtime and cost.
  - It omits or does not explain logical error rates, threshold behavior, decoder and control requirements, correlated errors, connectivity and routing, fabrication variability, and system-level reliability.
  - It does not distinguish general barriers from architecture-specific constraints such as cryogenics, photon loss, or platform-specific control and fabrication issues.
  - User-facing software and programming tools are mentioned as a gap but are not tied to commercial computational advantage.

### R7

- Coverage: 0.25
- Depth: 0.25
- Rationale: There are generic confidence and uncertainty statements, but no auditable evidence-quality assessment.
- Candidate evidence:
  - The report claims the examples “have been verified by independent researchers and are documented in credible sources.”
  - It acknowledges that “the timeline for achieving commercially viable quantum computing is highly uncertain” and that experts have differing opinions.
- Missing:
  - No sources are supplied; the Sources section explicitly says, “No usable sources were retrieved.”
  - The report does not distinguish primary experiments, independent replications, classical red-team analyses, theoretical work, vendor claims, or roadmaps.
  - It provides no material disagreements or examples of classical algorithmic improvements weakening claims.
  - The confidence labels are unsupported because the underlying evidence is not identified.
  - It does not discuss uncertainty specifically surrounding negative conclusions about the absence of commercial advantage.

### R8

- Coverage: 0.25
- Depth: 0.25
- Rationale: The conclusion is directionally cautious but generic and does not synthesize the required evidence into a specific maturity assessment.
- Candidate evidence:
  - The conclusion says quantum computers have shown “promising capabilities with demonstrated advantages, particularly in niche applications,” but face “substantial challenges” before commercial use.
  - The report states that timelines are “highly uncertain” and that predictions vary by application and technological progress.
- Missing:
  - The report does not clearly distinguish demonstrated, theoretical, and projected maturity in its final judgment.
  - It does not answer how close the field is in a calibrated way beyond general statements of promise and difficulty.
  - It offers no concrete measurable milestones, such as demonstrated logical-qubit scale, fault-tolerant circuit execution, end-to-end application benchmarks, or cost-adjusted comparisons, that would change the assessment.
  - It makes the unsupported assertion that factoring is a demonstrated advantage and does not resolve whether any commercial advantage has actually been shown.
  - No dates or bounded forecasts are given, but the report also provides no evidence-based basis for its uncertainty.

### Novel Value

- No material benchmark-external value identified.

## Citations

### Support

#### F1: NOT_EVALUABLE

- Claim: Demonstrated quantum advantage has been achieved in specific tasks, such as quantum simulation and factoring.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F2: NOT_EVALUABLE

- Claim: Theoretical advantages of quantum computing include optimization problems, cryptography, and complex simulations that are infeasible for classical computers.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F3: NOT_EVALUABLE

- Claim: The most significant technical barriers to quantum computing include error correction, coherence times, and qubit scaling.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

### Missing Citations

- Q1: Quantum computers show potential for commercial advantages in specific areas but still face significant technical barriers.
- Q2: Some demonstrated quantum advantages exist, while many projected advantages remain theoretical.
- Q3: Demonstrated quantum advantage has been achieved in specific tasks, such as quantum simulation and factoring.
- Q4: Google's Sycamore processor completed a specific task in 200 seconds that a classical supercomputer would take approximately 10,000 years to complete.
- Q5: IBM achieved a quantum advantage in chemistry simulations, demonstrating faster computations for small molecules than classical methods.
- Q6: Theoretical advantages of quantum computing include optimization problems, cryptography, and complex simulations that are infeasible for classical computers.
- Q7: Quantum algorithms such as Shor's and Grover's provide exponential speedup over classical counterparts for factoring and search problems.
- Q8: Research into quantum machine learning suggests potential improvements in training algorithms that may not yet be practically demonstrated.
- Q9: The most significant technical barriers to quantum computing include error correction, coherence times, and qubit scaling.
- Q10: Current quantum error-correction methods require a high number of physical qubits to create a logical qubit, impacting scalability.
- Q11: Qubit coherence times are still too short for many calculations, requiring advances in materials and qubit design.
- Q12: The timeline for achieving commercially viable quantum computing is highly uncertain, with experts differing on when practical applications will emerge.
- Q13: Predictions about the impact of quantum computing on industries vary greatly depending on the application and level of technological advancement achieved.
- Q14: Theoretical understanding of error correction and qubit stability needs improvement.
- Q15: Practical implementation of scalable quantum architectures remains a challenge.
- Q16: Development of user-friendly quantum programming languages and tools is still ongoing.
- Q17: Quantum computers have shown promising capabilities with demonstrated advantages, particularly in niche applications.
- Q18: Substantial challenges remain before quantum computers can realize their full potential in commercial settings.

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

1. R1: Set a time boundary and define the categories used to answer the question.
2. R3: Determine whether commercially useful quantum advantage has been demonstrated.
3. R2: Evaluate representative experimental claims of quantum advantage against classical computation.
4. 18 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ae3a5680c375b6650be217402137fd59a302eee5fb85b0bc360a9292a5734293`
- Candidate report hash: `d64b7d01211eace550312dd30e14826da0df20cf73b45f810e6f35bd8715ab52`
- LLM calls: 2
- Evaluated at: 2026-09-01T14:48:55.344296+00:00
