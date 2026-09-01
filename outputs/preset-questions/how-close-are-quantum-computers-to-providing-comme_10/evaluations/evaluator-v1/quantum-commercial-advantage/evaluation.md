# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** quantum-commercial-advantage

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 73.8 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.64
- Coverage: 0.68
- Depth: 0.53
- Citation quality: 0.85
- Citation validity: 1.00
- Citation support: 0.72
- Citation completeness: 1.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report makes several useful distinctions and mentions relevant metrics, but it does not establish the requested temporal boundary or systematically define all four categories.
- Candidate evidence:
  - The summary distinguishes “narrow, carefully defined benchmarks” from “commercially meaningful superiority.”
  - The report distinguishes benchmark advantage, scientific utility, and “end-to-end commercial advantage,” especially in Findings 2, 4, and 9.
  - The report discusses runtime, accuracy, wall-clock speedup, operating costs, and workflow value, for example the “3,000-fold wall-clock speedup” and the need for “complete workflow integration.”
- Missing:
  - No explicit evidence date or time boundary is stated in the report itself.
  - The four required categories are not cleanly and explicitly defined: demonstrated experimental advantage, commercial end-to-end advantage, theoretical algorithmic advantage, and projected resource/roadmap advantage.
  - Theoretical advantage is only briefly mentioned, without a definition based on asymptotic complexity or algorithmic assumptions.
  - The comparison metrics are discussed unevenly and are not organized into a clear evaluative framework covering runtime, cost, throughput, reliability, and solution quality.

### R2

- Coverage: 0.75
- Depth: 0.50
- Rationale: The two discussed examples are relevant and appropriately qualified, especially the Fermi–Hubbard case, but the treatment is not a broad representative survey and lacks some platform and standardized-comparison detail.
- Candidate evidence:
  - The report describes IBM’s one-qubit majority-of-three experiment, including its 93% quantum success rate versus 87.5% for a restricted classical comparator, and explains that artificial memory limitations make it noncommercial.
  - It describes the 120-qubit Fermi–Hubbard experiment, including the one-dimensional simulation task, up to 90 Trotter steps, approximately 1% RMSE over part of the evolution, and a reported 3,000-fold wall-clock speedup against a specified TDVP implementation.
  - It explains important limitations: dependence on the selected classical algorithm, bond dimension, observables, accuracy range, and runtime accounting; limited evolution-time agreement; and lack of a product or customer outcome.
  - It explicitly contrasts scientifically meaningful simulation with artificial random-circuit or toy benchmarks.
- Missing:
  - The set of representative demonstrations is narrow and omits other major experimental claims, such as random-circuit sampling, Google’s Sycamore result, quantum annealing claims, or other sampling and simulation demonstrations.
  - The hardware platform is not consistently identified in sufficient detail for each experiment.
  - The report does not systematically compare the demonstrations using common criteria such as total resources, sampling quality, classical hardware, or reproducibility.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is one of the strongest parts of the report: it directly answers whether commercial advantage has been demonstrated and identifies the required end-to-end accounting. Full coverage is withheld because no complete economic comparison is supplied and the classical red-team analysis remains partial.
- Candidate evidence:
  - The conclusion states that the evidence does not show “broad, independently verified commercial superiority over classical computers.”
  - The Fermi–Hubbard claim is explicitly described as not demonstrating “a product improvement, completed materials discovery, customer savings, or other end-to-end commercial outcome.”
  - The report identifies dependence on a particular TDVP baseline and notes that a competing classical method reproduced at least one result in about 2.5 minutes on a MacBook Air.
  - The Remaining Gaps section calls for accounting for compilation, calibration, repeated measurements, error suppression, data transfer, post-processing, hardware access, and operating costs.
  - Finding 9 explains that commercial usefulness requires reliable outputs, workflow integration, and measurable economic or scientific value rather than merely a fast quantum subroutine.
- Missing:
  - The report does not provide a fully worked end-to-end comparison for any economically meaningful workload.
  - The treatment of system availability, hardware depreciation or access cost, energy consumption, and customer-level total cost is mostly limited to identifying them as missing.
  - The report does not establish whether any claimed advantage survives all relevant classical algorithmic improvements; it gives only a partial counterexample involving one observable.

### R4

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report recognizes projections and labels them as uncertain, but it does not provide the requested algorithmic benefits, assumptions, or concrete resource conditions in sufficient depth.
- Candidate evidence:
  - The report labels chemistry and materials simulation as theoretically well matched to quantum processors and describes optimization, finance, machine learning, and drug discovery as potential applications.
  - It identifies survey forecasts for economically advantageous use cases in 2026–2030 and distinguishes forecasts for logical-qubit availability from demonstrated results.
  - It states that vendor forecasts and roadmaps are optimistic but uncertain and calls them future milestones rather than current commercial evidence.
  - The Remaining Gaps section requests workload-specific estimates for physical-to-logical-qubit overhead, circuit depth, decoding, connectivity, and fault-tolerant gate synthesis.
- Missing:
  - The report does not state the principal theoretical complexity or performance benefits for candidate algorithms, such as polynomial speedups, exponential state-space advantages, amplitude-estimation scaling, or quantum simulation complexity.
  - It does not clearly spell out the assumptions behind important algorithms, including oracle access, fault tolerance, input loading, sparsity, precision, sampling, or data access.
  - Hardware-dependent resource estimates are mentioned but not actually presented in a structured way.
  - Projected advantages are not consistently separated from theoretical algorithmic advantages; the discussion is mainly application-level rather than algorithm-level.

### R5

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report identifies plausible early areas and appropriately emphasizes chemistry/materials, but the per-application comparison and causal explanation are incomplete.
- Candidate evidence:
  - The report ranks chemistry, materials, molecular, and many-body simulation as the most credible projected application areas.
  - It separately discusses optimization, finance, machine learning, cryptography, and drug discovery as more speculative or primarily potential applications.
  - It explains that chemistry and materials are theoretically well matched, whereas the evidence for the other areas is mainly theoretical, projected, or industry commentary.
  - It states that current enterprise activity is early-stage experimentation and that there is no independently validated commercial superiority in the listed areas.
- Missing:
  - The areas are not compared using a consistent framework that separately evaluates theoretical promise, scientific usefulness, and commercial value for each one.
  - Cryptography is mentioned but not analyzed as a special case involving strategic security value rather than ordinary runtime-based commercial advantage.
  - Optimization, finance, machine learning, and scientific computing receive little explanation of the specific reasons their evidence is weaker or what practical assumptions block advantage.
  - The report does not discuss important counterconsiderations, such as data-loading costs in machine learning or approximation and verification issues in optimization and finance.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: The barrier analysis is technically substantial and connects most barriers to useful workloads. It falls short of full coverage mainly because architecture-specific distinctions and some requested platform constraints are absent.
- Candidate evidence:
  - Finding 6 prioritizes reliable logical scaling and explains that error correction can make systems prohibitively resource-intensive or slow.
  - The report discusses physical fidelity, logical-qubit encoding overhead, correlated and coherent noise, leakage, measurement errors, real-time decoding, cryogenic control, scalable logical gates, short lifetimes, and insufficient scale.
  - Finding 7 connects noise, specialized compilation, calibration, error suppression, thousands of two-qubit operations, limited circuit depth, and divergence from classical results to workload performance.
  - The report identifies control, connectivity, decoding, and software/hardware co-design as unresolved obstacles rather than merely listing specifications.
- Missing:
  - The report does not clearly classify which barriers are general across architectures and which are platform-specific.
  - Fabrication and material variability are not substantively discussed.
  - Photon loss and photonic-platform constraints are not discussed, and cryogenics is mentioned mainly in the context of control rather than as a platform-specific systems barrier.
  - The prioritization among error rates, logical-qubit scale, decoding, connectivity, and operating infrastructure is qualitative rather than tied to explicit workload thresholds.

### R7

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report does a good job surfacing disputes and labeling vendor claims and forecasts, but the evidence-quality assessment is weakened by heterogeneous sources and limited independent validation.
- Candidate evidence:
  - The report distinguishes an arXiv preprint, company claims, reviews, vendor material, forecasts, and competing classical analyses.
  - It explicitly notes that the Fermi–Hubbard result is conditional, that its commercial interpretation is disputed, and that it requires independent verification.
  - It reports a competing classical reproduction, disagreement over observable coverage and accuracy, and sensitivity to the selected TDVP implementation and bond dimension.
  - The report states that negative conclusions are based on accumulated evidence rather than a systematic survey and identifies unresolved benchmarking and accounting questions.
- Missing:
  - There is no independent replication of the central Fermi–Hubbard result; the report identifies this as a gap but cannot evaluate replication evidence beyond the reported critique.
  - The source base includes low-authority sources such as Quora, MindStick, ZDNET, company blogs, and industry commentary, without a clear source-quality hierarchy or weighting.
  - The report does not give detailed bibliographic treatment of primary experiments, independent critiques, or classical red-team work sufficient to assess methods and reproducibility.
  - Uncertainty about the absence of commercial advantage is acknowledged but not quantified or systematically bounded.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The synthesis is clear, nuanced, and supported by the body of the report, with concrete milestones and no false precision. Full coverage is withheld because the temporal framing and operational maturity thresholds are underdeveloped.
- Candidate evidence:
  - The conclusion gives a calibrated synthesis: narrow experimental advantages exist, the Fermi–Hubbard result is conditional and technically substantial, but broad independently verified commercial superiority has not been shown.
  - It places the field as “approaching specialized scientific utility” while remaining “substantially short of dependable, scalable, end-to-end commercial advantage.”
  - It avoids an unsupported precise date and identifies concrete milestones: more numerous high-fidelity logical qubits, manageable error-correction and decoding overhead, scalable connectivity and operation, and transparent benchmarking against strong classical methods.
  - The Remaining Gaps section specifies measurable evidence that would change the assessment, including independent reproduction, common accuracy targets, complete runtime accounting, real workflow outcomes, and workload-specific resource estimates.
- Missing:
  - The report does not provide a time-bounded maturity assessment because it never states an evidence date or explicitly anchors the conclusion to a particular period.
  - The phrase “approaching specialized scientific utility” is useful but not operationalized with clear quantitative thresholds for utility or commercial advantage.
  - The conclusion could more explicitly separate the confidence levels for demonstrated advantage, projected advantage, and the forecast timing of commercial usefulness.

### Novel Value

- The report’s most distinctive substantive value is its detailed treatment of the contested 3,000-fold Fermi–Hubbard claim, including baseline dependence, a competing classical reproduction, observable and accuracy disputes, and the distinction between a scientifically meaningful benchmark and an end-to-end commercial result.
- It also usefully frames fair benchmarking, total workflow accounting, and classical red-team analysis as central unresolved issues rather than treating hardware benchmark speedups as commercial proof.

## Citations

### Support

#### F1: SUPPORTED

- Claim: Demonstrated quantum advantage exists, but only under narrow or conditional definitions.
- Sources: S2, S9, S10
- Rationale: The sources describe demonstrated quantum advantage, while clearly limiting or qualifying its scope. S2 reports an experimental advantage only for a miniature, highly constrained one-bit/one-qubit task. S9 says quantum computers can outperform classical ones but emphasizes that existing devices are not useful for advantageous real-world applications and distinguishes proof-of-principle advantage from classically verifiable advantage. S10 states that the meaning of “advantage” has evolved and that current claims should be treated skeptically because the field remains in the NISQ era.
- Supporting text: S2: IBM observed a 93% success rate versus the classical system in a “microscopic experiment” with only one bit or qubit. S9: quantum computers “can outperform classical ones,” yet current devices are “nowhere near being useful” for advantageous applications; it also calls for “classically verifiable quantum advantage.” S10: “claims of utility and advantage must be met with skepticism” before fault-tolerant quantum computing.

#### F2: SUPPORTED

- Claim: The 120-qubit Fermi–Hubbard experiment is a more relevant demonstrated computational milestone, and supports a conditional, workload-specific advantage claim—but not yet an independently established commercial advantage.
- Sources: S22, S18, S20, S21
- Rationale: The sources support the experiment’s demonstrated 120-qubit scale and computational comparison: S22 reports a 120-qubit simulation and a quantum runtime up to 3,000× faster than an optimized TDVP simulation at the limit of agreement. S18 characterizes the technical achievement as substantial but says whether it constitutes quantum advantage depends on the comparison standard, and notes that the result was against TDVP and may not hold against newer classical methods. S20 explicitly states that the advantage framing is a company claim subject to independent verification. S21 further says the model was not a specific commercial compound and had no commercial or practical relevance, supporting the distinction between a workload-specific computational milestone and an independently established commercial advantage.
- Supporting text: S22: “We then extend experiments to L=60 (120 qubits)… outputs agree quantitatively with approximate classical simulations… [with] wall-clock runtime… up to 3000× faster than an optimized TDVP simulation.” S18: “Whether it constitutes ‘quantum advantage’ depends on how precisely you draw the line…” S20: “The quantum advantage framing is a company claim and remains subject to independent verification.” S21: “the algorithm did not simulate a specific commercial compound” and “had no commercial or practical relevance.”

#### F3: SUPPORTED

- Claim: The reported 3,000-fold materials-simulation advantage has not been conclusively validated against all relevant classical alternatives or through an independent end-to-end comparison.
- Sources: S16, S17, S19, S22, S18, S20
- Rationale: The saved sources support the claim’s central qualification. The technical paper and Q-CTRL-related reports describe the speedup as a comparison with an optimized TDVP/tensor-network approach, not all possible classical alternatives. S18 specifically reports an independent Majorana Propagation result that reproduced a single-site output slightly faster, while noting that the comparison is incomplete and raises unresolved accuracy and scope questions. S20 explicitly states that the framing is a company claim subject to independent verification. Thus, the sources support the absence of conclusive, comprehensive independent validation, although they do not establish that every relevant classical alternative has been tested.
- Supporting text: S20: “The quantum advantage framing is a company claim and remains subject to independent verification.” S18: Majorana Propagation reportedly reproduced the 120-qubit data for a single site in 2 minutes 30 seconds, and the article says “the full comparison is more nuanced” and that “there are still some open questions.” S22: the 3,000× figure is specifically against “an optimized TDVP simulation using χ=4096.”

#### F4: SUPPORTED

- Claim: Logical-qubit and fault-tolerance demonstrations are important progress, but current systems remain far from the scale and reliability associated with major application-level advantages.
- Sources: S8, S9
- Rationale: S8 documents substantial logical-qubit and fault-tolerance milestones, including improved logical-qubit reliability, teleportation, error correction, and meaningful logical-qubit computations. S9 explicitly states that fault tolerance has been demonstrated for a few logical qubits, while current devices are still nowhere near useful advantageous applications; it also describes the 100-logical-qubit regime as beyond existing proof-of-principle experiments and still one or more orders of magnitude from early applications. Together, the sources support both the progress and the remaining gap in scale and application-level usefulness.
- Supporting text: S8: Quantinuum reports progress toward fault tolerance, improved logical-qubit reliability, and demonstrations including logical-qubit teleportation and error-correction milestones. S9: “fault-tolerance is possible for at least a few logical qubits,” but devices are “still nowhere near being useful for any advantageous application”; the 100-logical-qubit regime is “well beyond” existing experiments and “one or more orders of magnitude away” from early applications.

#### F5: PARTIALLY_SUPPORTED

- Claim: The most credible projected application areas are chemistry, materials, molecular and many-body simulation; optimization, finance, cryptography, and other areas remain more speculative in the retrieved evidence.
- Sources: S1, S4, S5, S9, S13, S2, S15
- Rationale: The sources strongly support chemistry, materials, molecular, and many-body simulation as promising or foundational application areas. They also support that optimization is being explored but remains early-stage or speculative. However, the claim overgeneralizes cryptography: S13 describes quantum-secured communication and QRNG as already operational, while S9 discusses cryptographic proofs of quantumness as a possible application. The supplied sources do not specifically address finance enough to establish its speculative status, and they do not provide a systematic basis for ranking these areas by credibility.
- Supporting text: S1 says physical simulation of molecular and chemical reactions “may be the prime commercial opportunity.” S9 says the promise lies in condensed-matter physics and quantum chemistry and mentions simulating the Fermi–Hubbard model. S13 calls chemistry/materials simulation “one of the most promising use cases” with “firm evidence,” while describing optimization-related AV simulation as “decades premature.” S15 says enterprises are exploring optimization and many-body problems but characterizes the field as “really ... early stages.”

#### F6: PARTIALLY_SUPPORTED

- Claim: The biggest technical barrier is scaling reliable logical computation without making the system prohibitively resource-intensive or operationally slow.
- Sources: S6, S7, S10
- Rationale: The sources support that reliable logical or fault-tolerant computation is difficult to scale and that doing so requires substantial resources. However, they do not establish that this is definitively the “biggest” technical barrier, nor do the supplied excerpts directly support the specific claim that operations become prohibitively slow. S6 mentions “immense cost and other performance disadvantages” when using thousands of physical qubits for hundreds of logical qubits; S7 explicitly says resource efficiency and reliability for large-scale computation remain challenging; and S10 describes the need for higher qubit counts, longer lifetimes, and error correction for useful computation.
- Supporting text: S6: systems may require “thousands of physical qubits” for “a few hundred logical qubits,” trading “immense cost and other performance disadvantages.” S7: “achieving the resource efficiency and reliability required for large-scale quantum computation remains challenging.” S10: fault tolerance requires higher qubit counts, longer qubit lifetimes, and error correction to complete useful computations.

#### F7: PARTIALLY_SUPPORTED

- Claim: Noise management, compilation, calibration, and error-suppression overhead currently constrain circuit depth and the durability of claimed advantages.
- Sources: S16, S17, S18, S22, S21, S6, S7, S10
- Rationale: The sources strongly support that present-day noise and errors limit useful quantum computation, that compilation and error suppression are needed to execute deeper circuits, and that claimed advantages may be sensitive to improved classical methods. However, they do not collectively establish the full claim that calibration overhead currently constrains circuit depth, nor do they directly quantify compilation, calibration, or error-suppression overhead as limiting factors. In the cited Q-CTRL case, the sources instead characterize the error-suppression techniques as overhead-free or operating at native speed.
- Supporting text: S22 states that quantum simulations are limited by hardware noise and error, while S18 says compilation determines circuit depth and error-proneness and reports circuits up to 452 layers deep. S10 notes that noise, short qubit lifetimes, and the lack of fault tolerance limit useful computation, and that later classical approaches can negate earlier advantage claims. S16/S22 describe runtime error suppression as avoiding massive sampling or additional execution overhead.

#### F8: PARTIALLY_SUPPORTED

- Claim: Fair benchmarking and classical-baseline selection are themselves major barriers to establishing durable quantum advantage.
- Sources: S22, S18, S20, S21
- Rationale: The sources support that classical-baseline choice and independent verification materially affect quantum-advantage claims. S18 explicitly contrasts TDVP with a newer Majorana Propagation method and says the claimed speedup may depend on the available tools; it also notes unresolved accuracy and comparison questions. S20 says the advantage framing remains subject to independent verification. However, the sources do not establish that fair benchmarking and baseline selection are themselves “major barriers,” nor do they directly support the broader notion of “durable” advantage.
- Supporting text: S18: the 3,000× speedup holds against TDVP but “appears not to hold against this newer method,” and whether it is quantum advantage depends on whether one compares against today’s best tools or tools that could theoretically exist. S20: the quantum-advantage framing “remains subject to independent verification.”

#### F9: PARTIALLY_SUPPORTED

- Claim: Commercial usefulness requires more than a fast quantum subroutine: it requires reliable outputs, complete workflow integration, and measurable economic or scientific value.
- Sources: S9, S10, S20, S21, S22, S15
- Rationale: The sources support the narrower point that usefulness requires more than speed: S10 distinguishes speed-oriented supremacy from commercially useful utility and says useful computation requires sufficiently low error rates, while S9 emphasizes classical verification and trustworthy outputs. S22 reports quantitatively accurate results and a speedup in a scientific simulation. However, the supplied text does not establish a general requirement for complete workflow integration, nor does it directly state that commercial usefulness requires measurable economic or scientific value in precisely those terms. S20 and S21 also describe the reported advantage as subject to independent verification, and S21 explicitly says the simulated problem had no commercial or practical relevance.
- Supporting text: S10: “Claims of utility and advantage are going to require accurate solutions,” and supremacy experiments may demonstrate speed without commercial interest. S9: verification should convince users that the computation was performed by a quantum computer and address distrust of the server and its data. S22: outputs agreed quantitatively with approximate classical simulations, with runtime up to 3000× faster.

### Missing Citations

- None identified.

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
2. R4: Separate theoretical algorithmic advantages from hardware-dependent projections.
3. R2: Evaluate representative experimental claims of quantum advantage against classical computation.
4. 5 cited finding(s) were not fully supported by saved evidence.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ae3a5680c375b6650be217402137fd59a302eee5fb85b0bc360a9292a5734293`
- Candidate report hash: `08fbc65f786be71d22aca6e6ede6e4f96b6bf0cf30d68bc68cdea88e2ef0145f`
- LLM calls: 11
- Evaluated at: 2026-09-01T07:10:39.570163+00:00
