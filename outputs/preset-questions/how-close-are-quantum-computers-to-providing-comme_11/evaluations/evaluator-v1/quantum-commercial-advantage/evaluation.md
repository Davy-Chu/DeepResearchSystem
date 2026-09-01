# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** quantum-commercial-advantage

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 72.9 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.64
- Coverage: 0.65
- Depth: 0.60
- Citation quality: 0.82
- Citation validity: 1.00
- Citation support: 0.71
- Citation completeness: 0.94
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report uses several relevant distinctions and metrics, but its scope boundary and category definitions remain implicit and incomplete.
- Candidate evidence:
  - The report distinguishes “specialized technical quantum advantage” from “commercial advantage,” stating that current cloud availability is not equivalent to economic advantage.
  - It distinguishes synthetic sampling benchmarks from production applications and labels timelines and roadmaps as conditional projections: “Projected timelines range from the late 2020s to the 2030s or later.”
  - It identifies comparison metrics including runtime, cost, solution quality, business benefit, hardware, software, energy, and economic costs.
- Missing:
  - No explicit evidence date or cutoff period is stated, despite the requirement for a time boundary.
  - The four required categories are not cleanly and explicitly defined as separate categories: demonstrated computational advantage, commercially useful end-to-end advantage, theoretical algorithmic advantage, and projected resource- or roadmap-based advantage.
  - The report does not clearly define the comparison metric for each category or explain how the categories relate to one another.

### R2

- Coverage: 0.50
- Depth: 0.50
- Rationale: One recent logical-qubit sampling demonstration and one hybrid application experiment are analyzed with useful limitations, but the representative experimental landscape is too narrow.
- Candidate evidence:
  - It describes the IBM–University of Chicago experiment as a 70-logical-qubit, 2,415-logical-two-qubit-operation, 468-T-gate structured sampling experiment completed in approximately 15–16 minutes.
  - It states that classical simulation approaches were estimated to be impractical and explains that the workload was a synthetic, error-detection-oriented sampling benchmark rather than chemistry, finance, or optimization.
  - It discusses limitations including severe post-selection, a 5.90 × 10^-4 acceptance rate, device-dependent fidelity certification, and concerns about scaling post-selection overhead.
- Missing:
  - The report does not cover a representative range of major experimental claims, such as different platforms or earlier sampling, random-circuit, boson-sampling, or application-oriented demonstrations.
  - The classical comparison is mostly described as impracticality estimates rather than detailed strongest-classical runtime, cost, or approximation comparisons.
  - The report does not fully explain how the 70-logical-qubit experiment compares with other demonstrated-advantage claims or independent classical red-team results.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is one of the report’s strongest sections: it applies a demanding commercial standard and exposes important weaknesses in the HSBC–IBM claim, but the end-to-end accounting is not fully worked through for a demonstrated workload.
- Candidate evidence:
  - The report concludes that “no broadly accepted, independently verified end-to-end commercial quantum advantage has been established.”
  - It cites a runtime analysis finding no current NISQ runtime advantage after system-level overheads and gives an example quantum implementation approximately two orders of magnitude slower than a tuned classical baseline.
  - It assesses the HSBC–IBM bond-trading result as an offline quantum feature-transformation experiment rather than established economic advantage, noting missing comparisons against optimized classical feature engineering, total workflow cost, runtime, and realized trading profit.
  - It explicitly mentions readout, transpilation, thermalization, postprocessing, solution quality, cost, and business benefit as relevant benchmarking factors.
- Missing:
  - The report does not systematically address all relevant end-to-end factors for a concrete workload, especially state preparation/data loading, repeated-run requirements, error mitigation versus correction, system availability, and energy or operating cost.
  - The discussion of subsequent classical algorithm improvements is present mainly as a general concern; it does not identify specific classical algorithmic advances that weakened particular quantum claims.
  - The negative conclusion relies substantially on the “supplied evidence” formulation rather than a clearly delimited survey of all major candidate commercial claims.

### R4

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report appropriately labels projections and gives some resource estimates, but it does not substantially explain the algorithmic benefits and practical assumptions underlying the main theoretical claims.
- Candidate evidence:
  - It identifies fault-tolerant molecule and materials simulation as the strongest projected opportunity and states that current demonstrations are too small or noisy.
  - It reports a conditional projection of useful simulation requiring “hundreds of error-corrected logical qubits” and a 5–10 year estimate, while noting that timelines and hardware levels are conditional.
  - It labels vendor roadmaps as “targets rather than demonstrations” and notes that projected timelines depend on uncertain application requirements and scaling assumptions.
- Missing:
  - The report does not state concrete theoretical complexity or performance benefits for major algorithms, such as polynomial or exponential speedups, quantum simulation scaling, amplitude estimation, or factoring.
  - Assumptions about fault-tolerant gate counts, logical error rates, circuit depth, data access, state preparation, and output measurement are only listed as unresolved gaps, not analyzed for candidate applications.
  - Optimization, machine learning, finance, and cryptography are characterized as uncertain without separating their theoretical algorithmic promises from hardware-dependent projections.

### R5

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report gives a useful high-level application ranking and distinguishes promise from demonstrated value in several examples, but the comparative application analysis is uneven.
- Candidate evidence:
  - It compares chemistry and materials simulation with optimization, finance, machine learning, ordinary computing, and general business workloads.
  - It identifies quantum-system simulation as the strongest prospective area because the systems being simulated are quantum mechanical, while saying current demonstrations are not yet large enough to replace classical methods.
  - It characterizes optimization, AI, and climate modeling as longer-term or uncertain because classical algorithms are highly tuned and quantum methods have not demonstrated superiority.
  - It treats the HSBC–IBM bond-trading experiment as potential rather than commercial value because realized profit and complete workflow comparisons are absent.
- Missing:
  - The areas are not assessed consistently one by one against the three dimensions of theoretical promise, scientific usefulness, and commercial value.
  - Scientific computing, cryptography, and finance receive limited treatment; cryptography is explicitly acknowledged as insufficiently covered.
  - The report does not compare application-specific resource requirements or explain in detail why chemistry/materials is stronger than competing areas beyond broad statements about quantum-system structure.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report explains the central fault-tolerance problem and several consequences well, but it undercovers architecture-specific engineering barriers and their workload-specific effects.
- Candidate evidence:
  - It prioritizes scalable fault tolerance and explains its consequences through reliable logical qubits, low logical error rates, deep sustained circuits, and error-correction overhead.
  - It discusses decoherence, environmental noise, gate and interaction errors, limited coherence, cascading errors, physical-qubit overhead, post-selection, and scaling concerns.
  - It notes requirements involving thousands of physical qubits, hundreds of logical qubits, low error rates, and very large gate counts, and connects these to broad commercial applications.
  - It identifies system-level benchmarking barriers such as readout, transpilation, thermalization, verification, and full workflow accounting.
- Missing:
  - The report does not clearly separate general barriers from architecture-specific ones; cryogenics, photon loss, connectivity/routing, control electronics, decoding latency, correlated errors, fabrication variability, and material/platform constraints are largely absent or only implicit.
  - It does not prioritize barriers beyond broadly naming scalable fault tolerance as the largest one, nor quantify how each barrier affects particular workloads.
  - The relationship between physical error rates, code choice, logical-qubit overhead, sustained logical circuit depth, and application-level runtime is not developed in detail.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report is attentive to source type, disagreement, replication, and uncertainty, but its evidence-quality assessment is not as rigorous or source-critical as the requirement calls for.
- Candidate evidence:
  - It distinguishes vendor and media claims from peer-reviewed benchmarking evidence, explicitly contrasting Q-CTRL and IBM-related descriptions with stricter end-to-end analyses.
  - It discusses independent replication gaps and classical-control weaknesses for the HSBC–IBM result, including missing optimized classical, stochastic, independent-dataset, and economic controls.
  - It reports disagreement over whether the IBM–University of Chicago result constitutes “quantum advantage” as primarily definitional: technical beyond-classical computation versus commercially useful advantage.
  - It acknowledges uncertainty in negative conclusions by saying the conclusion concerns the supplied evidence and listing unresolved questions, while labeling roadmaps as targets rather than demonstrations.
- Missing:
  - Independent replications or detailed classical red-team analyses are not actually presented in depth; they are mostly identified as absent.
  - The source set includes vendor, media, blog, Wikipedia, and future-dated or low-authority sources, but the report does not systematically assess their relative reliability or reconcile them with primary papers.
  - The report does not provide a detailed account of how improved classical algorithms changed specific experimental claims.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report gives a clear and appropriately cautious overall judgment with useful milestones, but the closeness assessment could be made more operational and application-specific.
- Candidate evidence:
  - The conclusion gives a calibrated synthesis: technical advantage has been demonstrated, but an independently reproducible production-relevant task beating the best classical workflow has not.
  - It identifies fault-tolerant chemistry and materials simulation as the closest credible path while treating optimization, finance, machine learning, and general computing as experimental or uncertain.
  - It avoids asserting a precise arrival date and says timelines are uncertain.
  - It identifies concrete milestones and decision criteria, including scalable logical error detection, hundreds of logical qubits, deep circuits, full runtime/cost/quality accounting, independent replication, and end-to-end comparisons.
- Missing:
  - The report does not organize the milestones into a particularly explicit threshold for changing the overall maturity judgment.
  - “One major step short” is rhetorically clear but not operationally defined in terms of a specific workload, logical-qubit performance, or economic threshold.
  - The conclusion could more explicitly distinguish how close demonstrated technical advantage is from how close commercial advantage is across different application classes.

### Novel Value

- The report provides a useful synthesis separating a recent verified logical-qubit sampling benchmark from commercial usefulness rather than treating them as equivalent.
- Its treatment of the HSBC–IBM bond-trading result adds value by examining the hybrid workflow, hardware-noise dependence, missing classical controls, and absent economic accounting.
- It usefully frames scalable fault tolerance and standardized end-to-end benchmarking as distinct but complementary prerequisites for commercial advantage.

## Citations

### Support

#### F1: SUPPORTED

- Claim: Demonstrated technical quantum advantage exists for specialized, synthetic or simulation-hard tasks, but this is not demonstrated commercial advantage.
- Sources: S33, S34, S35, S6
- Rationale: S33 and S35 report a quantum computation beyond the practical reach of leading classical simulation methods. S34 more specifically identifies the experiment as a synthetic sampling task rather than an end-user application and explicitly says it was a benchmark claim, not a real-world speedup. S6 distinguishes quantum-supremacy experiments that demonstrate advantage from useful case studies requiring industry value and notes that the intersection is rare. Together, the sources support both the existence of a specialized technical advantage and the absence of demonstrated commercial advantage for this example.
- Supporting text: S34: “The experiment targeted a synthetic sampling task rather than chemistry, optimization or another end-user application” and “It does not establish that quantum computing has delivered a practical advantage for chemistry, finance, optimization or another commercial workload.”

#### F2: PARTIALLY_SUPPORTED

- Claim: No broadly accepted, independently verified end-to-end commercial quantum advantage has been established in the supplied evidence.
- Sources: S8, S9, S30
- Rationale: The sources support the narrower conclusion that practical or end-to-end quantum advantage has not yet been demonstrated under rigorous performance comparisons. However, they do not explicitly establish the broader propositions that no claim is broadly accepted, independently verified, or commercial in scope.
- Supporting text: S8 states that run-time-based quantum advantage has not yet been demonstrated under experimentally grounded metrics and emphasizes end-to-end time accounting. S9 says quantum computers have not yet demonstrated a practical advantage over classical systems in real-world applications. S30 states that quantum computers have not yet reached the point at which they achieve quantum advantage.

#### F3: SUPPORTED

- Claim: The HSBC–IBM bond-trading result is best classified as an application-oriented hybrid experiment showing potential, not as established quantum computational or economic advantage.
- Sources: S22, S16, S17
- Rationale: The saved sources support the claim’s key classification. S22 describes an applied bond-trading study using quantum hardware to transform data for classical machine-learning models, with the quantum component decoupled offline. It explicitly calls the work an empirical, explorative tool, reports only statistical observations, disclaims generalizable theory or causal economic effects, and describes the result as “emerging potential.” S16 likewise characterizes the workflow as hybrid and notes that the authors never claimed quantum advantage. S17 reinforces that the reported benefit does not establish quantum computational speedup. The sources therefore support treating the result as a promising application experiment rather than established computational or economic advantage.
- Supporting text: S22: the study uses “an actual quantum computer as an explorative tool,” reports “only statistical observations,” and says it does not infer “any generalizable theory or causal economic effect”; its conclusion describes “emerging potential.” S16: “The methodology centered on a hybrid workflow” and “The authors never claimed quantum advantage.” S17: the reported benefit “can have nothing to do with quantum computational speedup.”

#### F4: SUPPORTED

- Claim: The most credible projected commercial advantage is in fault-tolerant simulation of molecules, materials, chemistry, and other quantum systems; current demonstrations remain too small or noisy to displace classical methods.
- Sources: S3, S5, S6, S28, S13
- Rationale: The saved sources consistently identify molecular, materials, chemical, and broader quantum-system simulation as the strongest or most credible projected application area, particularly at fault-tolerant scale. They also state that current hardware is noisy or lacks sufficient qubits, and that demonstrations are toy-scale or small enough that they have not displaced classical methods. S3 describes materials/fermionic simulation as a candidate for sustainable advantage while noting that noise and errors have historically prevented useful results; its claim of a current practical advantage is a notable counterpoint, but does not undermine the broader support for the projected-advantage and current-limit portions of the claim.
- Supporting text: S5: “Its power is specific. It excels at one thing above all others: simulating the quantum-mechanical behavior of molecules, materials, and physical systems.” S6: “Drug discovery simulation at production scale is the canonical example” of prospective use cases awaiting fault-tolerant hardware, while many demonstrations are “at sub-scale sizes without proven advantage.” S28: “Molecular simulation in drug discovery, materials science, and chemistry emerges as the most viable near-term application area”; demonstrations “have not yet reached systems complex enough to displace classical methods,” and current hardware lacks the required error rates and qubit counts. S13 says the field “isn’t quite ready for prime time” and that hardware/software for the most complex problems may not be available until 2035 or later.

#### F5: PARTIALLY_SUPPORTED

- Claim: Optimization, finance, machine learning, and most ordinary workloads remain unresolved areas rather than established sources of general quantum advantage.
- Sources: S28, S25, S27
- Rationale: The sources support that optimization and machine learning have not established general quantum advantage, and that most ordinary workloads are unlikely to benefit from quantum hardware. S28 specifically says optimization has not yet demonstrated superiority over classical algorithms, most data processing and general software applications are poor fits, and most workloads are expected to remain classical. S25 describes evaluations of optimization and machine learning in terms of maturity, practical hurdles, and whether a clear path to advantage exists. However, the supplied excerpts do not directly establish the claim about finance as a whole; S28 only introduces financial portfolio optimization and risk analysis, without the subsequent assessment in the saved content. “Unresolved areas” is therefore supported for optimization and machine learning, and broadly for ordinary workloads, but not fully for finance.
- Supporting text: S28: “Many optimization problems have highly tuned classical algorithms that quantum approaches have not yet demonstrated the ability to beat”; “Problems ... include most data processing, general software applications”; and “The vast majority of computing workloads are expected to remain on classical systems.” S25: the evaluation framework distinguishes cases where “a clear path to a quantum advantage is shown” from those where “significant hurdles prevent practical application.”

#### F6: PARTIALLY_SUPPORTED

- Claim: The largest remaining technical barrier is scalable fault tolerance: reliable logical qubits, low logical error rates, deep sustained circuits, and manageable error-correction overhead.
- Sources: S1, S24, S4, S6, S34
- Rationale: The sources strongly support that fault tolerance and its scalability remain major technical challenges, including reliable logical qubits, lower error rates, longer circuits, and error-correction overhead. However, they do not establish that this is the single “largest” remaining barrier, and some evidence describes progress or roadmaps rather than a general assessment of the field.
- Supporting text: S24 identifies “stability and scalability” as considerable challenges and notes that error correction requires many physical qubits, while qubit stability determines algorithm length and error rates must be reduced. S4 describes the need for “hundreds of logical qubits, low error rates,” and circuits with millions of gates. S34 reports 92% error detection but a very low post-selection rate, noting that this overhead cannot grow indefinitely.

#### F7: PARTIALLY_SUPPORTED

- Claim: Benchmarking, verification, and full-system accounting are themselves major barriers to determining whether an apparent advantage is commercially meaningful.
- Sources: S8, S9, S6, S13
- Rationale: S8 directly supports the difficulty of evaluating apparent advantage when system-level overheads are excluded, and says credible claims require careful time accounting, appropriate metrics, and strong classical baselines. S9 describes benchmarking as a challenge and emphasizes relevance, reproducibility, fairness, and verifiability. S6 likewise calls rigorous classical benchmarking critical and frames evaluation around provable advantage and industry value. However, the sources do not clearly establish that these issues are themselves “major barriers” specifically to commercial meaningfulness; S13 provides no usable support for that narrower formulation.
- Supporting text: S8: conventional analyses that exclude readout, transpilation, and thermalization can bias performance assessments; credible claims require careful time accounting and appropriate classical references. S9: fair comparison and verifiable, standardized benchmarking remain challenging. S6: rigorous comparison with the best classical solution is “perhaps the most critical criterion,” alongside industry value.

### Missing Citations

- Q3: Quantum-computing systems are commercially accessible through cloud and as-a-service offerings, although availability is not equivalent to economic advantage.
- Q30: No supplied source independently establishes a production-scale application that beats the best complete classical workflow on total runtime, cost, quality, or economic value.

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
3. R4: Separate theoretical algorithmic advantages from hardware-dependent projections.
4. 4 cited finding(s) were not fully supported by saved evidence.
5. 2 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ae3a5680c375b6650be217402137fd59a302eee5fb85b0bc360a9292a5734293`
- Candidate report hash: `e8f56acdc9467204214cb643ebeb377854cc3e39ddb3457cd153eadfb201acd2`
- LLM calls: 9
- Evaluated at: 2026-09-01T08:29:31.943131+00:00
