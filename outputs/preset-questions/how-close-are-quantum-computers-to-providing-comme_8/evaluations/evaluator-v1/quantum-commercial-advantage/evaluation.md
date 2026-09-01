# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** quantum-commercial-advantage

**System Version:** evidence-ledger-decomposer-verifier-v1

**Model:** gpt-5.6-luna

## Summary

- Overall: 69.1 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.59
- Coverage: 0.60
- Depth: 0.57
- Citation quality: 0.79
- Citation validity: 1.00
- Citation support: 0.62
- Citation completeness: 1.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report supplies useful distinctions and metrics, but omits the required evidence period and does not clearly establish a complete taxonomy with operational definitions.
- Candidate evidence:
  - The report distinguishes “narrow laboratory demonstrations,” “theoretically established algorithmic speedups,” and “commercially useful advantage.”
  - It identifies runtime, accuracy, reliability, cost, affordability, and practical usefulness as commercial metrics: “Commercial quantum advantage should be evaluated… using end-to-end outcomes.”
- Missing:
  - No evidence date or time boundary is stated.
  - The categories are not fully and explicitly defined as four separate categories, especially projected advantage based on resource estimates or roadmaps.
  - The relationship between the categories and comparison metrics is only implicit rather than systematically defined.

### R2

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report appropriately distinguishes benchmark/sampling separation from a materials claim and discusses classical challenge, but it does not substantially survey representative experimental claims.
- Candidate evidence:
  - It describes the Sycamore demonstration as a 53-qubit benchmark, reporting 200 seconds quantum runtime versus Google's 10,000-year estimate and IBM's approximately 2.5-day estimate.
  - It explains that the result is contested and is a laboratory benchmark rather than a useful scientific or commercial workload.
  - It also mentions the Q-CTRL/IBM materials-simulation claim and its lack of independent validation.
- Missing:
  - The experimental coverage is narrow and does not provide a broader set of representative demonstrations or independent replications.
  - The Sycamore task and platform details are minimal, and state preparation, verification, sampling, and postprocessing limitations are not explained.
  - The Q-CTRL result lacks enough task-specific description to evaluate what was actually computed.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The central commercial judgment is well supported and the report identifies the right end-to-end criteria, but most of those criteria remain identified as gaps rather than actually measured.
- Candidate evidence:
  - The conclusion states that quantum computers are “not yet shown to provide a broadly commercially useful advantage.”
  - It evaluates the Q-CTRL/IBM 3,000-times claim as vendor-authored and lacking independent validation of the classical baseline, reproducibility, full costs, and commercial return.
  - It defines commercial evaluation using runtime, accuracy, reliability, cost, affordability, and practical usefulness against a comparably priced classical alternative.
  - It explicitly notes that subsequent classical methods materially weaken the Sycamore claim.
- Missing:
  - The report does not evaluate a specific economically meaningful workload with a complete end-to-end accounting of state preparation, mitigation/correction, repeated runs, preprocessing, postprocessing, availability, and operating cost.
  - It does not establish a systematic assessment of the strongest practically relevant classical alternatives across candidate workloads.

### R4

- Coverage: 0.50
- Depth: 0.50
- Rationale: It correctly separates theoretical algorithms from projected hardware-dependent applications, but provides limited complexity detail and almost no quantitative or workload-specific resource analysis.
- Candidate evidence:
  - It identifies Shor's polynomial-time factoring algorithm and Grover's approximately quadratic speedup as theoretical results for specific problem classes.
  - It states that projected simulation benefits depend on fault-tolerant systems, logical-qubit resources, classical baselines, and economic conditions.
  - It labels the assumed 2,000 logical qubits and one billion error-corrected operations as a projection rather than a demonstration.
- Missing:
  - The report does not give practical resource estimates for Shor, Grover, or simulation, such as logical gates, physical qubits, error-correction overhead, data loading, or execution time.
  - Required assumptions are discussed only generally; data access, oracle construction, input/output costs, and fault-tolerance conditions are not analyzed in detail.
  - Roadmaps and forecasts, including the cited 2030 and 2035-or-later expectations, are mentioned but not systematically separated or evaluated.

### R5

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report identifies plausible leading areas and weaker candidates, but the comparative application analysis is relatively shallow.
- Candidate evidence:
  - The report identifies chemistry, catalysis, pharmaceuticals, batteries, and energy as projected simulation opportunities.
  - It reports no demonstrated advantage for supply-chain optimization, machine learning, or derivatives pricing.
  - It characterizes quantum simulation as the strongest prospective area and says ordinary small-to-moderate business problems generally may not benefit.
  - It notes that the digital-health QML evidence is insufficient to determine superiority.
- Missing:
  - The application areas are not compared in a structured, area-by-area assessment of theoretical promise, scientific usefulness, and commercial value.
  - Optimization, finance, machine learning, cryptography, and scientific computing receive little analysis beyond brief claims or caveats.
  - The reasons simulation is stronger than competing areas are stated generally rather than tied to algorithmic structure, data access, accuracy requirements, and classical baselines.

### R6

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report covers several principal barriers and connects them generally to fault-tolerant workloads, but lacks the requested technical depth, prioritization, and architecture-specific analysis.
- Candidate evidence:
  - It identifies noise and physical errors, error-correction overhead, insufficient hardware scale, scalable control, and verification complexity as major barriers.
  - It states that these barriers are decisive for large-scale simulation and long fault-tolerant computations.
  - It notes missing information on logical-qubit availability, coherence, connectivity, decoding, throughput, operating cost, and integration requirements.
  - It illustrates the scale gap with the projected requirement of 2,000 logical qubits and one billion error-corrected operations and with infeasibility of practical RSA-2048 factoring.
- Missing:
  - The barriers are mostly listed rather than explained mechanistically in terms of workload performance.
  - There is little prioritization of which barriers dominate and no discussion of sustained logical circuit depth, routing, correlated errors, fabrication variability, or control/decoder latency in substantive detail.
  - The report does not clearly distinguish general barriers from architecture-specific constraints such as cryogenics, photon loss, or platform-dependent connectivity.

### R7

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report is unusually candid about uncertainty and source type, but its evidentiary foundation is not strong enough for full coverage or depth.
- Candidate evidence:
  - It distinguishes the contested Sycamore comparison, the vendor-authored Q-CTRL claim, theoretical algorithmic claims, and forward-looking industry projections.
  - It reports classical red-team criticism through IBM's approximately 2.5-day estimate and emphasizes sensitivity to improving classical methods.
  - It repeatedly states uncertainty around independent replication, baseline quality, reproducibility, cost, and commercial ROI.
  - It explicitly says the evidence does not support a reliable general timeline.
- Missing:
  - The source base relies substantially on secondary, vendor, industry, and general explanatory sources; primary experiments and independent replications are not actually presented.
  - Material disagreements beyond Sycamore are not developed, and the report does not assess the methodological authority or limitations of each cited source in detail.
  - Some claims, especially application projections and barriers, are supported by relatively weak sources rather than authoritative primary or peer-reviewed evidence.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The maturity assessment is clear, cautious, and well synthesized, with useful candidate milestones, but the requested concrete measurable evidence that would change the assessment is only partially articulated.
- Candidate evidence:
  - The conclusion gives a clear judgment: no broad commercially useful advantage has yet been shown.
  - It synthesizes demonstrated, theoretical, and projected evidence, describing current demonstrations as narrow or low-confidence and future value as application-dependent.
  - It avoids a precise unsupported date and states that no supplied evidence supports a reliable general timeline.
  - It identifies decisive conditions including sufficient scale, accuracy, throughput, reliability, and total cost against improving classical alternatives.
  - The remaining-gaps section lists measurable areas such as logical errors, qubit counts, error-correction overhead, throughput, operating cost, reproducibility, and end-to-end application comparisons.
- Missing:
  - The report does not turn the listed gaps into a prioritized milestone framework specifying what result would materially change the judgment.
  - It offers limited quantitative thresholds or concrete decision criteria for declaring commercial advantage in a workload.

### Novel Value

- The report usefully separates the contested Sycamore benchmark from the unindependently verified Q-CTRL/IBM materials-simulation claim rather than treating either as established commercial advantage.
- It emphasizes the distinction between quantum computational advantage and quantum economic advantage, including end-to-end cost, reliability, accuracy, and availability.
- It identifies improving classical baselines and independent validation as central uncertainties, and avoids assigning an unsupported commercialization date.

## Citations

### Support

#### F1: SUPPORTED

- Claim: Experimentally demonstrated quantum advantage remains narrow and does not yet establish broad commercial usefulness. The Google Sycamore benchmark was reported as 200 seconds on a 53-qubit processor versus Google's estimate of 10,000 years classically, but IBM estimated approximately 2.5 days for the classical computation. The supplied evidence therefore supports a contested laboratory benchmark, not an unqualified practical advantage.
- Sources: S9
- Rationale: S9 directly reports the 53-qubit Sycamore result, Google's 200-second versus 10,000-year estimate, and IBM's counterestimate of 2.5 days. It also characterizes the result as a proof-of-concept and says the advantage applies only to specific problem types, with only a few algorithms achieving useful advantages so far. These points support the claim's qualified conclusion about a contested benchmark rather than an unqualified practical advantage.
- Supporting text: S9 states that Sycamore's 53-qubit processor completed the calculation in 200 seconds, which Google estimated would take 10,000 years on the fastest supercomputer; IBM argued it could be done in 2.5 days. The source calls this a “dramatic proof-of-concept,” says the result was debated, and notes that the advantage applies only to specific kinds of problems and that only a few algorithms achieve it so far.

#### F2: PARTIALLY_SUPPORTED

- Claim: A Q-CTRL report claims a 3,000-times wall-clock speedup for an IBM-based fermionic or materials-simulation task while meeting stated accuracy and practical-time requirements, but a reliable conclusion about genuine, reproducible, or commercially valuable advantage cannot currently be drawn.
- Sources: S2
- Rationale: S2 directly supports that Q-CTRL reports using an IBM quantum computer for Fermionic Simulation and claims a wall-clock speedup of more than 3,000 times, alongside practically relevant completion time and accuracy meeting or exceeding existing tooling and user expectations. However, the saved source does not substantiate the added qualification that a reliable conclusion about genuine, reproducible, or commercially valuable advantage cannot currently be drawn; it instead presents Q-CTRL's own conclusion that practical quantum advantage and positive ROI were achieved.
- Supporting text: Q-CTRL states that its IBM-based demonstration involved Fermionic Simulation and reached a solution “over 3,000 times faster in wall-clock time,” while completing the task in a practically relevant time and delivering accuracy that met or exceeded existing expectations.

#### F3: SUPPORTED

- Claim: Theoretical and projected advantage is application-specific rather than general. The strongest prospects are selected large problems with favorable quantum algorithms, especially quantum-system or materials simulation; small-to-moderate business problems generally are not expected to benefit unless hardware and end-to-end economics clearly outperform classical alternatives.
- Sources: S4, S5, S9
- Rationale: The sources support the claim's main components. S4 explicitly says quantum computing will not be better for everything, identifies large problems with exponential algorithmic gains or very large datasets as the likely beneficiaries, and states that small-to-moderate problems common in businesses will not benefit. It also describes quantum economic advantage as requiring faster performance than a comparably priced classical computer. S5 identifies the advantage as narrow and concentrated in applications aligned with quantum algorithms, especially simulation of molecules, materials, and physical systems. S9 likewise says the advantage applies only to specific problem types with suitable algorithms. The wording 'end-to-end economics' is somewhat broader than S4's comparably priced-computer benchmark, but is materially supported by the economic-advantage discussion.
- Supporting text: S4: “small to moderate-sized problems, the most common types for typical businesses, will not benefit,” while large problems with exponential algorithmic gains or very large datasets “will derive advantages”; quantum economic advantage means solving a problem faster than with a comparably priced classical computer. S5: the advantage map is “narrow, uneven,” and concentrated where the underlying physics aligns with quantum computers, which “excels” at simulating molecules, materials, and physical systems. S9: quantum advantage applies “only to specific kinds of problems” for which suitable algorithms exist.

#### F4: PARTIALLY_SUPPORTED

- Claim: Shor's factoring algorithm and Grover's unstructured-search algorithm provide theoretically established algorithmic speedups, but the supplied evidence does not show current hardware delivering a commercial advantage from either result.
- Sources: S9
- Rationale: S9 explicitly describes Shor's algorithm as offering exponential speedup in principle and Grover's algorithm as offering a quadratic speedup. It also states that the hardware needed for practical Shor-based RSA factoring is far beyond current hardware. However, the source does not establish the broader negative claim that current hardware delivers no commercial advantage from either algorithm, nor does the supplied excerpt discuss commercial advantage specifically.
- Supporting text: S9 says Shor's algorithm can factor large numbers “exponentially faster than any known classical method” and that Grover's algorithm searches an unstructured database in roughly O(√N) steps versus O(N) classically. It also says the estimated hardware for factoring a 2048-bit RSA key is “far beyond today’s quantum hardware.”

#### F5: PARTIALLY_SUPPORTED

- Claim: Fault-tolerant quantum simulation is projected as a potentially high-value area in chemistry, catalysis, pharmaceuticals, and batteries or energy, but the cited resource requirements, timelines, and economic impacts are projections rather than demonstrated commercial advantages.
- Sources: S5
- Rationale: S5 supports the future-oriented, potentially high-impact framing for pharmaceuticals, chemicals/catalysis, and battery technology, and gives resource estimates, a 2033 timeline, and an economic valuation. However, it does not clearly establish that these specific commercial advantages have not been demonstrated; its explicit “demonstrated advantage” caveat applies to other applications such as supply-chain optimization, machine learning, and derivatives pricing. The source also presents some claims assertively rather than labeling every estimate as merely projected.
- Supporting text: The article describes a hypothetical “by 2033” fault-tolerant system, rates pharmaceuticals and chemicals/catalysis as having “High” competitive impact and batteries as “Significant,” and cites estimates such as approximately 4,900 logical qubits, 73 hours of runtime, and a catalyst calculation valued at approximately $200,000.

#### F6: PARTIALLY_SUPPORTED

- Claim: The most important remaining technical barriers are noise and physical errors, error-correction overhead, insufficient hardware scale, scalable hardware and control, and verification complexity. These barriers are especially decisive for large-scale simulation and other applications requiring long fault-tolerant computations.
- Sources: S2, S4, S5, S8, S9
- Rationale: The sources directly identify several of the claimed barriers: noise and errors, hardware size or scalability, error-correction overhead, and verification complexity. They also indicate that useful large-scale or fault-tolerant applications require substantially more capable hardware. However, the supplied text does not establish that this is the definitive list of the “most important” barriers, does not clearly discuss scalable control as a distinct barrier, and provides only limited direct support for the claim that these barriers are especially decisive for all large-scale simulations and other long fault-tolerant computations.
- Supporting text: S2 says quantum computers face challenges involving the size of hardware and errors that degrade performance; S8 explicitly cites “error correction overhead, hardware scalability, and verification complexity” as ongoing challenges and describes current machines as noisy and error-prone. S4 says hardware and software for the most complex problems may not be available until 2035 or later. S9 notes that the hardware needed for practical large-scale applications such as breaking RSA is far beyond current systems.

#### F7: PARTIALLY_SUPPORTED

- Claim: Commercial quantum advantage should be evaluated against a comparably priced and available classical alternative using end-to-end outcomes, including runtime, accuracy, reliability, cost, affordability, and practical usefulness, rather than a theoretical speedup or isolated benchmark.
- Sources: S4, S2
- Rationale: The sources support comparing quantum systems with classical alternatives using real-world, commercially relevant performance rather than theoretical or isolated benchmarks. S4 explicitly defines “quantum economic advantage” using a comparably priced classical computer, while S2 emphasizes the best available alternative, wall-clock time, accuracy, practical relevance, affordability, and user value. However, the supplied text does not clearly establish all claimed criteria together—particularly reliability—and S4’s available excerpt is truncated before its full evaluation framework is provided.
- Supporting text: S4: The framework establishes “quantum economic advantage” when a problem can be solved more quickly with a quantum computer than with a “comparably priced classical computer.” S2 defines practical quantum advantage as outperforming the “best available” conventional alternative in a real-world application of known relevance, delivering results “better, faster, or more affordably,” with relevant wall-clock time and accuracy; it contrasts this with theoretical advantage and commercially irrelevant benchmark problems.

#### F8: PARTIALLY_SUPPORTED

- Claim: For quantum machine learning in digital health, a reliable conclusion about superiority over classical methods cannot currently be drawn from the supplied evidence.
- Sources: S6
- Rationale: S6 identifies a systematic review specifically assessing whether quantum machine-learning algorithms outperform classical methods, but the supplied snapshot ends before reporting the review’s findings or conclusion. Thus, it supports the topic and comparison, but does not directly establish that a reliable superiority conclusion cannot be drawn.
- Supporting text: The review “assesses whether quantum machine learning (QML) algorithms outperform existing classical methods for clinical decisioning or health service delivery,” but the saved text provides no results or conclusion.

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
- `structured_claim_evidence_available`: PASS
- `ledger_claim_ids_unique`: PASS
- `ledger_evidence_relationships_resolve`: PASS
- `ledger_confidence_values_valid`: PASS
- `ledger_evidence_ids_unique`: NOT_EVALUABLE — Current ledger relations have no independent evidence-ID field.

## Main Weaknesses

1. R1: Set a time boundary and define the categories used to answer the question.
2. R2: Evaluate representative experimental claims of quantum advantage against classical computation.
3. R4: Separate theoretical algorithmic advantages from hardware-dependent projections.
4. 6 cited finding(s) were not fully supported by saved evidence.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ae3a5680c375b6650be217402137fd59a302eee5fb85b0bc360a9292a5734293`
- Candidate report hash: `2ae5d4f7e4fdc61299cee53955f7c70f4bf67ac52747a67bbf1acaf76d677465`
- LLM calls: 10
- Evaluated at: 2026-09-01T01:25:59.804278+00:00
