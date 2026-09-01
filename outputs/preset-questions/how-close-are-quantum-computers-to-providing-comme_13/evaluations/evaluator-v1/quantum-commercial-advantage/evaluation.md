# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** quantum-commercial-advantage

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 76.3 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.66
- Coverage: 0.66
- Depth: 0.64
- Citation quality: 0.90
- Citation validity: 1.00
- Citation support: 0.81
- Citation completeness: 1.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report substantially gestures toward the requested distinctions and metrics, but it lacks an explicit evidence boundary and a structured definition of all four categories.
- Candidate evidence:
  - The report distinguishes “narrow computational separation” from “quantum economic advantage” and defines the latter as solving a problem faster with a comparably priced quantum system than with a classical alternative. [S2]
  - It separately discusses demonstrated benchmarks, theoretical opportunities, and forecasts, including projected dates of 2028–2029, the 2030s, and 2035 or later, while labeling forecasts as projections. [S2] [S3]
  - The report refers to runtime, accuracy, cost, operating expense, verification, and return on investment as relevant comparison dimensions.
- Missing:
  - No clear evidence date or cutoff period is stated at the beginning of the report; the source list contains future-dated material but does not establish a formal time boundary.
  - The four categories are not explicitly and systematically defined as separate categories: experimentally demonstrated advantage, end-to-end commercial advantage, theoretical algorithmic advantage, and hardware/resource-based projections.
  - The comparison metrics are discussed throughout, but not consolidated into clear definitions for each category.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report covers two representative demonstrations with results and limitations and avoids treating them as commercially equivalent. Some experimental and comparative detail remains incomplete.
- Candidate evidence:
  - It describes the IBM/University of Chicago demonstration: a 70-logical-qubit verified hard-sampling computation, roughly 15 minutes on quantum hardware, and prohibitive runtimes for leading classical simulations. [S9] [S10]
  - It describes the Q-CTRL/IBM experiment: a 120-qubit one-dimensional Fermi–Hubbard simulation, approximately 1% RMSE over part of the evolution range, and a claimed up-to-3,000× speedup against an ITensor/TDVP solver. [S19]
  - It identifies important limitations: the IBM task is a benchmark rather than a commercial workload, while the Q-CTRL task is a one-dimensional model with conditional accuracy and baseline dependence. [S9] [S10] [S19] [S22]
  - It notes an alternative classical result in which Majorana Propagation reproduced a result quickly and took about 19 minutes at a higher-accuracy setting. [S14] [S20]
- Missing:
  - The IBM demonstration is not described in enough technical detail regarding platform, exact task structure, classical algorithms, verification procedure, or the strength and practical relevance of the classical comparison.
  - The report relies heavily on institutional, vendor, and secondary accounts and does not present an independent replication of either demonstration.
  - The demonstrations are differentiated, but the report could more explicitly compare their evidentiary status and explain why sampling separation is weaker evidence of useful advantage than an application-oriented simulation benchmark.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is one of the report’s strongest areas: it directly answers the commercial-usefulness question and addresses baseline sensitivity and workflow accounting. It falls short of full credit because no actual end-to-end economic benchmark is presented.
- Candidate evidence:
  - The conclusion states that the field has not crossed the threshold of “broad, independently validated, end-to-end commercially useful advantage over classical computing.”
  - For Q-CTRL, the report says there is no demonstrated industrial customer workflow, actionable materials-discovery result, end-to-end savings, procurement or operating costs, or return on investment. [S19] [S20] [S21] [S23]
  - It explicitly warns that the 3,000× result depends on the selected TDVP baseline, hardware configuration, evolution range, accuracy boundary, and observable set. [S19] [S22]
  - It identifies missing end-to-end accounting for compilation, calibration, queueing, repetitions, error suppression, data movement, post-processing, energy, hardware, and operating costs.
  - It discusses subsequent or alternative classical methods, including Majorana Propagation, that materially change the apparent advantage. [S14] [S20] [S21]
- Missing:
  - The report does not provide a fully worked end-to-end comparison for any economically meaningful workload, including quantified costs, availability, preprocessing, postprocessing, and repeated-run requirements.
  - It does not assess whether the IBM sampling result could have any economic value under a specific commercial use case; it mainly establishes that no such value is supplied by the sources.
  - The conclusion about absence of commercial advantage is appropriately qualified but is based on the supplied evidence rather than a systematic survey of all commercial deployments.

### R4

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes the distinction between theory and projection and labels forecasts appropriately, but it lacks the algorithm-specific complexity, assumptions, and resource analysis required for deep treatment.
- Candidate evidence:
  - The report identifies Shor’s algorithm and BB84 as examples of clearer theoretical advantages, while describing optimization and machine learning as less established. [S5] [S7]
  - It identifies quantum-system simulation, drug and materials discovery, optimization, finance, machine learning, and cryptographic tasks as candidate areas. [S1] [S2] [S5]
  - It states that many proposed business applications remain prospective and that resource estimates and roadmaps are projections rather than validated timelines. [S2] [S3]
  - It notes that useful advantages may require very large problems, exponential algorithmic gains, or very large datasets. [S2]
- Missing:
  - The report generally does not state the claimed complexity or performance benefit for each important algorithmic area, such as Shor, Grover, quantum simulation, optimization, or quantum machine learning.
  - It provides few concrete resource estimates, logical-qubit requirements, circuit-depth requirements, data-loading assumptions, or fault-tolerance assumptions.
  - It does not systematically separate purely asymptotic theoretical advantages from hardware-dependent projections and explain the end-to-end conditions that could eliminate those advantages.

### R5

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report gives a useful high-level ranking—simulation appears stronger than optimization and machine learning—but does not provide the requested per-area comparative analysis.
- Candidate evidence:
  - It identifies simulation and materials discovery as the most concrete motivation and says optimization and machine learning are substantially less established. [S7]
  - It lists chemistry, materials, optimization, finance, machine learning, and cryptography as possible application areas. [S1] [S2] [S5]
  - It characterizes likely early utility as specialized, scientific, and hybrid rather than broad replacement of classical systems.
- Missing:
  - Most application areas are only listed rather than compared in terms of theoretical promise, scientific usefulness, commercial value, and evidence strength.
  - There is little area-specific discussion of why chemistry/materials may be stronger than optimization, finance, or machine learning, beyond broad assertions from the cited sources.
  - Scientific computing and cryptography receive no detailed assessment of practical conditions, timelines, or commercial relevance.
  - The report does not identify concrete early-use milestones for the competing application areas.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report provides a strong barrier overview, explains several mechanisms, and distinguishes general from platform-specific constraints. It lacks quantitative and workload-specific prioritization needed for full credit.
- Candidate evidence:
  - It prioritizes the transition from error suppression/NISQ hardware to scalable fault-tolerant computing as the central barrier. [S1] [S4] [S7]
  - It explains effects of decoherence, gate errors, cascading errors, limited coherence, and physical-qubit overhead on deep useful circuits. [S1] [S4]
  - It identifies connectivity, routing-related control issues, cooling, manufacturing, wiring, classical control, and system integration as scaling constraints. [S1] [S4]
  - It distinguishes platform-specific obstacles, including superconducting cooling and control, neutral-atom scaling and error-rate uncertainty, and trapped-ion scaling. [S4]
  - It treats verification and fair classical benchmarking as barriers to credible advantage claims, not merely performance specifications. [S9] [S14] [S19] [S20]
- Missing:
  - Logical-qubit scale, sustained logical circuit depth, logical error-rate targets, decoding, correlated errors, fabrication variability, and quantitative error-correction overhead are mentioned incompletely or not developed.
  - The report does not clearly rank the barriers by workload impact beyond calling fault tolerance the biggest barrier.
  - The consequences for particular workloads—such as chemistry, materials, optimization, or cryptanalysis—are mostly left as a list of missing application-specific requirements rather than explained in detail.
  - Photon loss and other architecture-specific constraints outside the platforms discussed are not covered.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: Evidence provenance, disagreement, classical sensitivity, and uncertainty are handled well. Full credit is withheld because independent replication and systematic source criticism are absent.
- Candidate evidence:
  - The report distinguishes primary preprints, institutional reports, vendor claims, secondary reporting, commentary, and roadmaps; it explicitly says the Q-CTRL evidence is primarily institutional or secondary reporting. [S16] [S19]
  - It notes that the Q-CTRL work lacks established peer review or independent replication of the commercial interpretation. [S16] [S17] [S18] [S19]
  - It reports disagreement over the Q-CTRL interpretation: Q-CTRL describes practical advantage, while commentary qualifies it as a one-dimensional benchmark with no direct commercial task. [S13] [S19] [S20] [S23]
  - It reports sensitivity to classical methods, including Majorana Propagation and the selected TDVP baseline. [S14] [S19] [S20] [S21]
  - It qualifies negative conclusions by stating that the material does not provide a systematic survey of deployed commercial workloads.
- Missing:
  - No independent replication or formal peer-reviewed critique is actually presented; the report mainly notes their absence.
  - The source-quality assessment does not systematically evaluate the IBM/UChicago claim against independent classical red-team analyses or alternative verification methods.
  - The report does not give a detailed assessment of source authority, methodological quality, or possible conflicts of interest for each major claim.
  - The uncertainty analysis could better distinguish uncertainty about whether an advantage exists from uncertainty about whether it is commercially valuable.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report directly answers the closeness question, integrates the major evidence categories, and identifies meaningful milestones without overclaiming. It lacks quantitative milestone criteria and a more explicit maturity calibration.
- Candidate evidence:
  - The conclusion gives a calibrated synthesis: narrow technical advantage has been demonstrated or credibly reported, while broad commercial advantage has not been established.
  - It distinguishes verified hard computations, a specialized Fermi–Hubbard speedup, theoretical opportunities, and uncertain commercial applicability.
  - It avoids asserting a precise date as fact and explicitly labels forecasts such as 2028–2029, the 2030s, and 2035 or later as projections. [S2] [S3]
  - It identifies concrete evidence that would change the assessment: independent benchmarking, end-to-end cost accounting, replication, actionable materials-discovery results, customer ROI, and application-specific logical-qubit/error-rate/resource data.
- Missing:
  - The phrase “closer to specialized technical utility” is useful but not tied to a more explicit maturity scale or probability/confidence assessment for reaching commercial advantage.
  - The report does not specify quantitative milestone thresholds—for example, required logical error rates, workload sizes, cost ratios, or sustained throughput—that would demonstrate commercial advantage.
  - The synthesis could more explicitly state how far demonstrated benchmark advantage is from end-to-end commercial advantage in terms of missing stages of deployment.

### Novel Value

- The report’s most useful synthesis is its separation of narrow benchmark/time-to-answer advantage from commercially meaningful end-to-end economic advantage.
- It highlights verification and fair classical benchmarking as substantive technical and evidentiary barriers, rather than treating them as ancillary concerns.
- It usefully frames the Q-CTRL result as potentially important but conditional on the classical baseline, accuracy target, observable, and full workflow accounting.

## Citations

### Support

#### F1: SUPPORTED

- Claim: Narrow computational quantum advantage has been demonstrated, but this should not be equated with commercially useful advantage.
- Sources: S9, S10, S2
- Rationale: S9 and S10 explicitly report a demonstrated quantum advantage on a trusted computation beyond the practical reach of leading classical simulation methods. S2 distinguishes computational quantum advantage from “quantum economic advantage,” noting that the former can overshadow usefulness and that businesses must assess whether quantum computing is faster than a comparably priced classical computer. Together, the sources support both the narrow demonstration and the warning against equating it with commercial usefulness.
- Supporting text: S10: the demonstration met the criteria for “quantum advantage” on trusted computations and was beyond leading classical simulation methods. S2: the focus on quantum advantage can overshadow usefulness; “quantum economic advantage” requires outperforming a comparably priced classical computer.

#### F2: PARTIALLY_SUPPORTED

- Claim: The Q-CTRL/IBM Fermi–Hubbard experiment is the strongest supplied evidence for a present-day, application-oriented advantage, but it remains a benchmark-specific reported result rather than established broad commercial advantage.
- Sources: S19, S11, S13, S15, S22, S23, S20, S21
- Rationale: The supplied sources strongly support the existence of a reported Q-CTRL/IBM Fermi–Hubbard benchmark showing up to a 3,000× wall-clock speedup against a specified TDVP classical comparison, with agreement at approximately 1% RMSE in the relevant regime and application relevance to materials science. They also support caution: S20 and S21 explicitly say the result does not establish that no classical method can handle the task, that the comparison depends on observable, timing definition, tuning, and validation, and that better classical methods can reduce the apparent speedup. However, the sources do not establish that this experiment is the “strongest supplied evidence” among all possible evidence, nor do they directly prove the broader characterization “not established broad commercial advantage”; they mainly show a benchmark-specific result and describe it as evidence or a demonstration of “practical quantum advantage.”
- Supporting text: S19 reports a 120-qubit simulation whose quantum-processor runtime was “up to 3000× faster” than optimized TDVP at the limit of agreement. S13 describes the problem as commercially relevant and reports two minutes versus over 100 hours, but labels it “evidence of practical quantum advantage.” S22 states the comparison was “up to 3,000× faster at the agreement boundary” and validated within “~1% RMSE” only to a specified evolution time. S21 cautions that the processor “does not prove that no classical method can handle this task,” while S20 says the result “does not win on every observable” and that Majorana propagation weakens a simple advantage claim.

#### F3: SUPPORTED

- Claim: The reported 3,000× Q-CTRL speedup is conditional and should not be generalized to quantum computing as a whole.
- Sources: S19, S22, S14, S20, S21
- Rationale: The sources consistently present the 3,000× figure as a specific comparison for a 1D Fermi–Hubbard simulation, against an ITensor TDVP classical baseline, at particular system sizes, evolution times, accuracy conditions, and timing definitions. They also explicitly caution that the result does not establish that no classical method can handle the task and that the meaning of “quantum advantage” depends on the benchmark and comparator. This supports both the conditional nature of the speedup and the warning against generalizing it to quantum computing as a whole.
- Supporting text: S19: the processor was “up to 3000× faster than an optimized TDVP simulation using χ=4096” at the limit of quantum/classical agreement. S22: “up to 3,000× faster at the agreement boundary.” S14: “the 3,000x speedup holds against TDVP” and whether it constitutes quantum advantage depends on how the comparison is defined. S21: “The quantum processor does not prove that no classical method can handle this task.”

#### F4: SUPPORTED

- Claim: Theoretical and projected advantages remain concentrated in specialized problem classes rather than ordinary business computing.
- Sources: S2, S1, S5, S7
- Rationale: The saved sources consistently state that quantum computing advantages apply to particular or select classes of difficult problems, while typical business problems and broad practical uses do not yet show comparable benefits. S2 directly contrasts advantages for large, exponentially improved problems with the small-to-moderate problems common in typical businesses. S1 describes quantum computing as useful for only a few select problem classes. S5 says only a few notable algorithms outperform classical computing on particular tasks. S7 emphasizes that practical, economically viable applications have not yet been achieved and that proposed optimization and machine-learning benefits remain largely aspirational.
- Supporting text: S2: “small to moderate-sized problems, the most common types for typical businesses, will not benefit from quantum computing,” whereas large problems with exponential algorithmic gains or very large datasets may benefit. S1: “there are a few select classes of problems” for which industries seek quantum computers. S5: “only a few notable quantum algorithms” outperform classical ones on particular tasks. S7: “practically useful and economically viable” quantum computations have not yet been achieved.

#### F5: SUPPORTED

- Claim: Quantum computers are not close to broadly replacing classical computers; likely early utility is specialized and hybrid, with classical systems remaining central.
- Sources: S2, S5, S7, S1
- Rationale: The saved sources consistently support the claim’s core points. S2 says the field is not ready for prime time, that typical small-to-moderate business problems will not benefit, and that quantum computing will be better only for some tasks. S5 says practical applications remain limited and doubts that people will have quantum computers in their homes within 20 years. S7 describes substantial unresolved gaps before broadly useful machines, says no immediate practical uses have emerged, and characterizes early applications as primarily scientific. S1 explicitly states that classical computers will not be going away and identifies only select problem classes for quantum use. The exact term “hybrid” is not directly established, but S1 does mention classical control and machine-learning systems alongside quantum hardware.
- Supporting text: S1: “The first useful commercially available quantum computer will not be a panacea… Classical computers will not be going away. Instead, there are a few select classes of problems…” S7: “practically useful and economically viable” quantum computations “have not yet been achieved,” and “Early applications… will be primarily scientific.” S2: “The current field… isn’t quite ready for prime time” and quantum computing “is not going to be better for everything, just for some things.”

#### F6: PARTIALLY_SUPPORTED

- Claim: The biggest technical barrier is the transition from noisy intermediate-scale devices and error suppression to scalable fault-tolerant quantum computing.
- Sources: S1, S4, S7, S19, S23, S9, S10
- Rationale: S7 directly supports the transition from NISQ devices to fault-tolerant, application-scale quantum computers and explicitly describes it as a daunting, arduous, expensive, prolonged, and colossal engineering challenge. S1 and S4 support the underlying technical problems involving noise, error mitigation/correction, stability, and scalability. However, the sources do not establish that this transition is definitively the single “biggest” technical barrier. S19, S23, S9, and S10 mainly document error suppression, error correction, verification, or demonstrations rather than ranking this transition as the biggest barrier.
- Supporting text: S7: “substantial gaps separate today’s noisy intermediate-scale quantum (NISQ) devices from tomorrow’s fault-tolerant application-scale quantum (FASQ) machines,” including the transition “from error mitigation to active error detection and correction” and “from rudimentary error correction to scalable fault tolerance.” It calls the path “arduous, expensive, and prolonged” and “a particularly daunting gap.”

#### F7: PARTIALLY_SUPPORTED

- Claim: Scaling the physical machine remains a major engineering challenge involving connectivity, control, cooling, manufacturing, and system integration.
- Sources: S4, S1
- Rationale: S4 strongly supports scaling as a major challenge and explicitly identifies multi-qubit connectivity, individual-qubit control, cooling, and manufacturing as scaling considerations. S1 also supports control, cooling, and hardware-integration challenges, including wires extending outside the cryogenic environment. However, the supplied text does not explicitly identify “system integration” as a distinct challenge, and S1 does not materially support connectivity or manufacturing.
- Supporting text: S4 lists “Multi-qubit networks,” “Control over individual qubits at scale,” “Cooling and environmental control,” and “Manufacturing” among key challenges; it also states that quantum computing faces technological hurdles limiting scalability. S1 describes considerable challenges in stability and scalability and notes that superconducting-qubit wires can introduce noise outside the processor’s cryogenic environment.

#### F8: SUPPORTED

- Claim: Verification and classical benchmarking are not secondary details; they are essential barriers to credible claims of advantage.
- Sources: S9, S10, S18, S19, S22, S14, S20, S21
- Rationale: The saved sources directly characterize verification as a major challenge to establishing quantum advantage and describe classical benchmarking, including choice of comparator, timing definition, accuracy validation, and convergence checks, as central to assessing such claims. Some wording is interpretive, but the claim’s important factual content is well supported.
- Supporting text: S10 states that “verification remains one of the biggest challenges in firmly establishing experimental quantum advantage.” S18 notes that results must be checked against classical computation and that the Q-CTRL result still required peer review. S21 explains that a fair benchmark must account for classical tuning, validation, preprocessing, and post-processing, while S14 shows how a newer classical method could narrow the reported speedup.

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
3. R5: Assess which application areas appear most plausible for early useful advantage.
4. 3 cited finding(s) were not fully supported by saved evidence.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ae3a5680c375b6650be217402137fd59a302eee5fb85b0bc360a9292a5734293`
- Candidate report hash: `a35d985d814f25ede782d33be1a1baf21ffc7a6c3e98bc20c5ef7d80c453047e`
- LLM calls: 10
- Evaluated at: 2026-09-01T10:44:30.961736+00:00
