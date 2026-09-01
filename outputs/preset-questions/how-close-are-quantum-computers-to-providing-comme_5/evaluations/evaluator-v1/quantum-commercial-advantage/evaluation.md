# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** quantum-commercial-advantage

**System Version:** llm-only-baseline-v0

**Model:** gpt-5.6-luna

## Summary

- Overall: Unavailable
- Evaluation completeness: 80%
- Comprehensiveness: Unavailable
- Coverage: Unavailable
- Depth: Unavailable
- Citation quality: 0.00
- Citation validity: 0.00
- Citation support: 0.00
- Citation completeness: 0.00
- Deterministic integrity: 1.00

## Comprehensiveness

**NOT EVALUABLE:** ValidationError: 1 validation error for ComprehensivenessJudgment
requirements.2
  Value error, Every score below 1 requires a missing-item explanation [type=value_error, input_value={'requirement_id': 'R3', ...d economic case study.'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.13/v/value_error

## Citations

### Support

### Missing Citations

- Q1: Quantum computers have demonstrated computational advantages over classical methods on specially constructed benchmark problems, including random-circuit sampling and boson-sampling-like tasks.
- Q2: These benchmark demonstrations generally do not provide commercially useful advantages because the tasks have little direct business value and the outputs can be difficult to verify.
- Q3: There is no broadly accepted demonstration of a fault-tolerant quantum computer delivering a superior real-world economic result to the best classical alternatives on commercially relevant workloads.
- Q4: Narrow commercially useful quantum applications may emerge first in the 2030s, while large-scale cryptographic impact is likely to require much larger fault-tolerant machines and may occur later.
- Q5: Shor’s algorithm provides polynomial-time factoring and discrete-logarithm algorithms, whereas the best known classical methods are sub-exponential; Grover’s algorithm provides an approximately quadratic speedup for unstructured search.
- Q6: Google reported that its 53-qubit Sycamore processor completed a random-circuit-sampling task in about 200 seconds that it estimated would require thousands of years on a classical supercomputer.
- Q7: The classical runtime estimate associated with Google’s 2019 Sycamore experiment was challenged and subsequently improved using better simulation methods.
- Q8: Google, IBM, USTC, and other groups have reported larger or more difficult random-circuit and sampling experiments, including USTC experiments involving Jiuzhang and Zuchongzhi.
- Q9: Boson-sampling output distributions are believed to be classically difficult to sample under plausible complexity assumptions.
- Q10: D-Wave has deployed large commercial quantum annealers and has reported performance advantages for some optimization and sampling problems.
- Q11: There is no consensus that quantum annealing has produced a broad, reproducible, economically decisive advantage over classical optimization software.
- Q12: Google’s 2023 surface-code experiment reported that increasing the size of a surface-code logical qubit reduced logical error rates.
- Q13: Quantum processors have simulated small molecules, spin systems, lattice models, and chemical dynamics, but current results remain below the threshold for commercial chemistry or materials discovery.
- Q14: Near-term variational algorithms such as VQE have not shown a reliable commercial advantage, with noise, barren optimization landscapes, measurement costs, and classical simulation improvements limiting their value.
- Q15: Quantum computers may eventually assist with molecular ground-state energies, reaction pathways, catalytic mechanisms, electronic structure, excited states, strongly correlated materials, and battery or photovoltaic materials.
- Q16: Many optimization problems are NP-hard, but quantum computers do not thereby automatically solve them efficiently, and no quantum optimization method has shown a robust, application-scale advantage over strong classical solvers on representative industrial datasets.
- Q17: Quantum amplitude estimation can provide a quadratic reduction in sampling complexity for certain Monte Carlo calculations.
- Q18: Shor’s algorithm threatens RSA, Diffie–Hellman, and elliptic-curve cryptography by factoring large integers and solving discrete logarithms.
- Q19: Breaking commonly used cryptographic keys is generally expected to require thousands or more logical qubits and potentially millions of physical qubits under surface-code assumptions.
- Q20: Organizations should already be migrating to post-quantum cryptography because encrypted data captured today may be decrypted later, creating a ‘harvest now, decrypt later’ risk.
- Q21: Current quantum processors generally have tens to thousands of physical qubits, imperfect gates and measurements, limited connectivity, short coherence relative to algorithmic requirements, and no full error correction.
- Q22: Error mitigation can improve results without the full qubit overhead of error correction, but its measurement costs generally increase and it does not scale indefinitely.
- Q23: Surface-code architectures may require hundreds or thousands of physical qubits per logical qubit, and practical machines may require millions of physical qubits for applications needing thousands of logical qubits.
- Q24: Many fault-tolerant algorithms require non-Clifford gates, especially T gates, which are often implemented using expensive magic-state preparation and distillation.
- Q25: For many quantum computations, especially sampling tasks, verifying the answer may be as hard as performing the computation.
- Q26: Classical algorithms and methods often improve after a quantum advantage claim is published, reducing early estimates of quantum advantage.
- Q27: Loading large classical datasets into a quantum processor can eliminate a theoretical speedup, and extracting a complete answer from a quantum state may require many measurements.
- Q29: The report’s overall conclusion is that quantum computers have demonstrated computational advantage in narrow, artificial tasks but have not demonstrated a broadly accepted, economically useful advantage on a real commercial workload.
- Q30: Timing for useful quantum applications is speculative: specialized quantum simulation may be among the earliest meaningful applications, optimization has no established general advantage, machine learning remains highly speculative, finance likely requires fault tolerance, and cryptanalysis is far beyond current hardware.

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

1. 29 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ae3a5680c375b6650be217402137fd59a302eee5fb85b0bc360a9292a5734293`
- Candidate report hash: `a44bc2c3be4dfdc9b20b7522425923b07a32980af9de1e30fa97721a6d39aa72`
- LLM calls: 3
- Evaluated at: 2026-08-31T23:45:41.185241+00:00
