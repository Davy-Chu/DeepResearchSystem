# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** quantum-commercial-advantage

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 67.8 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.58
- Coverage: 0.60
- Depth: 0.54
- Citation quality: 0.76
- Citation validity: 1.00
- Citation support: 0.57
- Citation completeness: 1.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report gestures toward the relevant categories and metrics, but it does not establish a time boundary or provide explicit operational definitions for all four categories.
- Candidate evidence:
  - The report distinguishes a “candidate, task-specific time-to-answer advantage” from “end-to-end commercial advantage,” and separately discusses “Theoretical and projected advantages.”
  - It refers to runtime, accuracy, output scope, timing definitions, and cost-accounting omissions.
- Missing:
  - No explicit evidence date or cutoff period is stated.
  - The four required categories are not clearly defined as a structured framework, especially the distinction between theoretical algorithmic advantage and hardware-dependent projections.
  - Metrics such as throughput, reliability, solution quality, and operating cost are not systematically defined.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: The central demonstration is described with unusually good technical and comparative detail, but the requirement asks for representative demonstrations plural and broader coverage of experimental claims.
- Candidate evidence:
  - It describes the 120-qubit superconducting IBM Fermi–Hubbard experiment, including up to 90 Trotter steps, spin-charge separation, quantitative agreement with classical simulations, and the reported 3,000-fold runtime comparison against TDVP at bond dimension χ=4096.
  - It reports competing classical results: approximately 100 minutes on four NVIDIA H200 GPUs, a roughly 36-fold residual comparison, a 10–15 second laptop result for related dynamics, and a 7.06-fold quantum execution-proxy comparison for one observable.
  - It explains limitations involving output scope, accuracy, finite evolution time, baseline choice, and timing conventions, and explicitly says the result is not equivalent to a general commercial advantage.
- Missing:
  - The report presents essentially one major experimental demonstration rather than multiple representative platforms or task types, such as random-circuit sampling, photonic sampling, or other application experiments.
  - The classical comparisons are reported but not fully normalized into a clear assessment of which comparison is strongest and practically relevant.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: It gives a well-supported negative assessment of the leading supplied claim and addresses classical red-teaming and workflow accounting, but its commercial-usefulness evaluation is concentrated on one benchmark and lacks a broader workload survey.
- Candidate evidence:
  - Finding 3 states that the Fermi–Hubbard result “does not yet demonstrate end-to-end commercial value or broad commercial advantage.”
  - The report notes the absence of a deployed materials-discovery product, downstream industrial result, customer economics, measurable business outcome, independent replication, complete cost accounting, and a fully matched end-to-end comparison.
  - It specifically identifies omitted compilation, calibration, repetitions, readout processing, postprocessing, queueing, and cloud workflow costs.
  - It discusses improved classical algorithms that narrow or reverse the claimed advantage for selected observables and notes that timing and accuracy winners can differ.
- Missing:
  - The report does not systematically evaluate other claimed economically meaningful workloads or commercial demonstrations beyond the Fermi–Hubbard case.
  - It does not quantify operating costs or show an explicit end-to-end economic comparison, even as an example of what would be required.

### R4

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report correctly labels broad claims as prospective, but it does not substantively analyze theoretical algorithms or hardware-dependent projections.
- Candidate evidence:
  - Finding 5 labels broader benefits for optimization, cryptography, chemistry, materials, and AI as “prospective” rather than demonstrated commercial outcomes.
  - It says quantum simulation is among the strongest selected problem classes and identifies Quantinuum’s quantum-enhanced AI as an ongoing research objective rather than a completed benchmark.
  - The report’s remaining gaps request quantitative fault-tolerant resource estimates involving logical qubits, physical-qubit overhead, error rates, and runtime.
- Missing:
  - No important candidate area is given a concrete complexity or performance claim, such as polynomial or exponential scaling, quadratic speedup, or a stated algorithmic advantage.
  - The assumptions behind theoretical advantages are not explained, including oracle/access models, sparsity, fault tolerance, precision, data loading, or input/output costs.
  - Hardware-dependent projections, company roadmaps, and resource estimates are not actually presented and compared; they are mostly mentioned as absent or prospective.
  - The practical conditions that could eliminate an end-to-end advantage are not developed separately for the candidate algorithms.

### R5

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report identifies plausible areas and gives a useful caution about materials simulation and AI, but it does not perform the requested comparative application assessment.
- Candidate evidence:
  - It names quantum simulation, chemistry, materials, optimization, cryptography, and AI as candidate areas.
  - It says quantum simulation appears strongest in the supplied evidence, while AI lacks a completed benchmark and the Fermi–Hubbard result has not shown downstream materials-science or industrial value.
  - It distinguishes the scientific usefulness of the Fermi–Hubbard observables from commercial advantage.
- Missing:
  - The candidate areas are not compared systematically against one another.
  - For most areas, the report does not distinguish theoretical promise, scientific usefulness, and commercial value.
  - It provides little explanation of why chemistry, materials, optimization, finance, machine learning, or cryptography are stronger or weaker candidates than competing areas.
  - Finance and scientific computing beyond the Fermi–Hubbard example receive no substantive assessment.

### R6

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report goes beyond merely listing noise and decoherence, but its technical-barrier treatment remains high-level and omits several rubric-specified bottlenecks.
- Candidate evidence:
  - It identifies noise, decoherence, error correction, scaling, specialized operating environments, machine size, finite quantum/classical agreement time, and error suppression as barriers.
  - The conclusion prioritizes reliable error correction and scaling, control of noise and decoherence, and expansion beyond narrow one-dimensional benchmarks.
  - It explains that accuracy degrades as circuit complexity and entanglement grow and that noisy experiments rely on error suppression.
- Missing:
  - Logical-qubit scale, physical-to-logical overhead, sustained logical circuit depth, connectivity and routing, control and decoding, correlated errors, fabrication variability, and platform-specific constraints are not developed.
  - The barriers are not clearly prioritized by their effect on particular useful workloads.
  - There is no explicit separation of general barriers from architecture-specific barriers such as cryogenics, photon loss, or platform-dependent connectivity.
  - The report does not explain threshold behavior or what error rates and logical performance would be needed for commercial workloads.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is one of the report’s strongest areas: it openly handles conflicts, source types, classical red-team results, and uncertainty, though source-quality evaluation could be more systematic.
- Candidate evidence:
  - The report distinguishes primary-paper evidence, vendor announcements, company-authored reports, preprints, classical rebenchmarks, and procurement analysis.
  - It explicitly reports disagreement between the Q-CTRL-associated 3,000-fold claim and classical results of approximately 36-fold, 7.06-fold, or faster classical performance for narrower observables.
  - It states that the competing implementations are not independently adjudicated and that no supplied source provides independent peer-reviewed adjudication or a neutral complete economic analysis.
  - It notes sensitivity to classical algorithm improvements, output scope, accuracy, implementation, and timing conventions, and identifies the uncertainty in concluding that commercial advantage is absent.
- Missing:
  - The report does not consistently characterize the authority and methodological quality of each cited source, particularly the informal blog, LinkedIn, Stack Exchange, and Substack sources.
  - It does not provide independent replication evidence for other major experimental claims, limiting the evidence base largely to one focal experiment.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The maturity judgment is clear, appropriately cautious, and tied to evidence and measurable next steps, but the milestones remain procedural rather than quantitatively specified.
- Candidate evidence:
  - The conclusion gives a calibrated judgment: quantum computers are close enough for narrowly targeted experiments and cloud access but not for broad commercially useful superiority.
  - It synthesizes the candidate experimental advantage, baseline sensitivity, improved classical methods, commercial gaps, and technical barriers without asserting an unsupported date.
  - It identifies concrete evidence that would change the assessment: matched independent benchmarks, full end-to-end time-to-answer accounting, downstream industrial value, independent replication, and quantitative fault-tolerant resource estimates.
- Missing:
  - The report does not define quantitative milestone thresholds, such as a reproducible advantage margin, logical-qubit count, circuit depth, error rate, or cost advantage, that would decisively establish commercial usefulness.
  - The conclusion is primarily centered on the Fermi–Hubbard case and therefore gives limited synthesis across distinct theoretical and projected application areas.

### Novel Value

- The report provides a valuable baseline-sensitive synthesis of the Q-CTRL/IBM Fermi–Hubbard claim, contrasting the headline 3,000-fold figure with substantially different classical results.
- It usefully separates scientific utility and task-specific runtime claims from end-to-end commercial advantage.
- It highlights the distinction between timing advantage and accuracy advantage, and identifies workflow accounting and classical rebenchmarking as central to judging practical quantum advantage.

## Citations

### Support

#### F1: PARTIALLY_SUPPORTED

- Claim: Demonstrated quantum advantage is currently narrow and application-specific rather than general-purpose.
- Sources: S33, S6
- Rationale: S33 documents a specific demonstrated quantum-simulation result and describes it as competitive in a particular fermionic many-body-dynamics regime, supporting the claim's application-specific aspect. S6 frames quantum capability around particular institutional goals and says an industrial group may care whether a benchmark workload benefits, but it does not establish that demonstrated quantum advantage is currently narrow or exclude general-purpose advantage. The sources therefore do not fully support the broad current-state claim.
- Supporting text: S33: the work reports digital quantum simulation of the 1D Fermi–Hubbard model and calls the processor competitive where leading classical methods can become prohibitively expensive. S6: procurement should begin with the smallest capability that produces repeatable near-term value, and an industrial group may ask whether a benchmark workload gains anything from quantum resources.

#### F2: PARTIALLY_SUPPORTED

- Claim: The Q-CTRL/IBM Fermi–Hubbard experiment is the strongest supplied evidence for a present-day candidate advantage, but the headline 3,000-fold figure is conditional on the selected classical baseline, accuracy criterion, output, and timing definition.
- Sources: S33, S20, S22, S26, S29
- Rationale: The sources support the experiment’s reported 3,000× comparison and clearly document that it depends on a specific TDVP baseline, bond dimension, agreement/accuracy window, simulated output, and timing metric. They also support treating the result as a candidate rather than an established general advantage: S20 reports a stronger classical implementation reducing the figure to about 36×, while S29 shows that changing the observable, approximation, and timing definition materially changes the comparison. However, the supplied sources do not establish that this experiment is definitively the strongest evidence among all possible present-day evidence; they only describe it as a leading or recent benchmark.
- Supporting text: S33 reports a 3000× wall-clock comparison against optimized TDVP at χ=4096, with roughly 1% RMSE before divergence. S20 says the claim used over 160 CPU-cluster hours versus about 166 seconds of bare QPU time, excluding mitigation and post-processing, and that a stronger classical method reduced the comparison to ~36×. S29 further notes that observable choice, accuracy, and whether one counts bare execution or characterization-inclusive time change the result.

#### F3: SUPPORTED

- Claim: The Fermi–Hubbard result does not yet demonstrate end-to-end commercial value or broad commercial advantage.
- Sources: S32, S33, S6, S20, S29, S31
- Rationale: The saved sources support the claim’s central qualification. Although the result reports a large runtime advantage, the evidence is limited to a one-dimensional Fermi–Hubbard simulation and a narrowly defined comparison. The result was still awaiting peer review, its high-entanglement regime initially lacked verification, its scaling to real-world materials research remained uncertain, and the benchmark does not establish a general end-to-end or broad commercial advantage. S6 is broadly about procurement and S31 documents Fire Opal’s commercial availability, but neither demonstrates commercial value for this Fermi–Hubbard result.
- Supporting text: S32 notes that the result was announced in a preprint, raises verification concerns, and asks whether and how quickly the approach will scale to real-world materials researchers; it also cautions that customers do not base purchases on time savings alone. S29 says the benchmark’s caveats prevent a general matched-accuracy, end-to-end quantum-advantage claim. S20 reports that improved classical methods reduced the claimed 3000× speedup to about 36× and emphasize the need for rigorous classical verification.

#### F4: PARTIALLY_SUPPORTED

- Claim: Pre-fault-tolerant systems can provide scientifically useful results, but scientific utility should not be conflated with commercial quantum advantage.
- Sources: S33, S9
- Rationale: S9 directly supports the first part: its title identifies evidence for quantum-computing utility before fault tolerance. S33 provides a concrete example of scientifically useful results from a noisy superconducting processor, including quantitatively accurate Fermi–Hubbard simulations and observed spin–charge separation. However, the supplied excerpts do not discuss commercial quantum advantage or explicitly distinguish scientific utility from commercial advantage.
- Supporting text: S9: “Evidence for the utility of quantum computing before fault tolerance.” S33: the experiment reports observing spin–charge separation and obtaining results that “match classical simulations,” while describing contemporary digital processors as a platform for studying fermionic many-body dynamics.

#### F5: PARTIALLY_SUPPORTED

- Claim: Theoretical and projected advantages remain strongest for selected problem classes, especially quantum simulation, with broader claims for optimization, cryptography, chemistry, materials, and AI still prospective in the supplied evidence.
- Sources: S3, S5, S4, S6
- Rationale: The sources support that advantages are problem-specific and that quantum simulation—particularly fermionic simulation and materials-related simulation—is a prominent demonstrated or targeted area. They also support that optimization and cryptography are described as potential applications, and that AI advantages are presented as goals or projections. However, the claim overstates the evidentiary status of all broader areas: S5 reports a claimed practical materials-simulation speedup, while S3 describes optimization and cryptography as practical advantages rather than merely prospective. S6 mainly supports caution about distinguishing research results, offerings, and roadmaps, but does not directly establish the full comparative claim.
- Supporting text: S3: quantum computers are “designed to handle specific problems,” with examples including optimization and cryptography. S5: fermionic simulation is called a “prime candidate” for long-term advantage, while the authors report a 3,000-times-faster materials-simulation result. S4 describes quantum AI as a project whose “ultimate goal” is to benefit from quantum advantages and claims future improvements in efficiency, cost, and scalability.

#### F6: PARTIALLY_SUPPORTED

- Claim: The biggest hardware barriers are noise, decoherence, error correction, and scaling to sufficiently capable reliable logical systems.
- Sources: S3, S7, S33
- Rationale: The sources clearly support noise and errors as major hardware limitations, and S3 specifically explains that environmental factors can cause decoherence. S3 also mentions differences among technologies in scalability, stability, and error correction. However, the saved excerpts do not establish that these are the “biggest” barriers, do not specifically discuss scaling to sufficiently capable reliable logical systems, and do not substantiate error correction as a barrier itself; they mainly describe error suppression or the differing role of error correction.
- Supporting text: S3: Qubits are “extremely sensitive to their surroundings”; temperature, electromagnetic interference, and vibrations can cause decoherence. It also says technologies differ in “scalability, stability, speed, and error correction.” S7: quantum computers “can be limited by noise and errors,” which can degrade performance and prevent useful results. S33: quantum computers have been limited by “machine size and the impact of hardware noise and error.”

#### F7: PARTIALLY_SUPPORTED

- Claim: Benchmarking and workflow accounting are themselves major remaining barriers to establishing commercial advantage.
- Sources: S20, S23, S26, S29, S31
- Rationale: The sources support that rigorous benchmarking, fair classical baselines, validation, and complete time-to-answer/workflow accounting are important unresolved challenges for demonstrating quantum advantage. However, they do not establish that these are themselves “major remaining barriers” specifically to establishing “commercial advantage”; the evidence is mainly about technical quantum-advantage claims and benchmark methodology, not commercial adoption or business advantage.
- Supporting text: S20 says establishing quantum advantage requires comparison against the best achievable classical simulation and that reliable classical verification is essential. S23 notes that truncation validation belongs in the workflow and that runtime alone can misrepresent time-to-answer. S29 says QPU and classical timings are not perfectly interchangeable and cautions against a general end-to-end advantage claim. S31 states that classical processing time remains a factor in total time.

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
3. R6: Identify and prioritize the principal technical barriers to commercially useful quantum computing.
4. 6 cited finding(s) were not fully supported by saved evidence.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ae3a5680c375b6650be217402137fd59a302eee5fb85b0bc360a9292a5734293`
- Candidate report hash: `7dd8117219f67ec9274e81533f3015d651caaf0e952e6c15bed197a5e6708c61`
- LLM calls: 9
- Evaluated at: 2026-09-01T09:24:39.223052+00:00
