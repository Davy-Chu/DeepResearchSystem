# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

**Status:** Completed

**Stop Reason:** sufficient_evidence

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 6 / 10

**Unique Sources:** 22

**OpenAI Calls:** 7

**Tavily Calls:** 6

**Started:** 2026-09-01T02:54:23-04:00

**Ended:** 2026-09-01T02:56:36-04:00

**Total Runtime:** 133.16s

---

# Iteration 1

## 1. Search

**Query**

> How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

**Why this query**

This is the user's original research question.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S1 — Quantum Computers Expected to Be Useful by 2026, Survey**
  URL: https://www.iotworldtoday.com/quantum/quantum-computers-expected-to-be-useful-by-2026-survey
- **S2 — IBM researchers demonstrate the advantage that quantum computers have over classical computers | ZDNET**
  URL: https://www.zdnet.com/article/ibm-researchers-demonstrate-the-advantage-that-quantum-computers-have-over-classical-computers
- **S3 — What are the advantages and disadvantages of traditional computers and quantum computers? - Quora**
  URL: https://www.quora.com/What-are-the-advantages-and-disadvantages-of-traditional-computers-and-quantum-computers
- **S4 — The potential advantages of quantum computers over classical computers – MindStick**
  URL: https://www.mindstick.com/blog/302611/the-potential-advantages-of-quantum-computers-over-classical-computers
- **S5 — What are the advantages of quantum computers? In what specific way do quantum computers outperform classical computers? - Science Alerts - Quora**
  URL: https://sciencealerts.quora.com/What-are-the-advantages-of-quantum-computers-In-what-specific-way-do-quantum-computers-outperform-classical-computers

**Search Duration:** 4.62s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

A claimed experimental quantum advantage has been demonstrated on a deliberately tiny, artificial task, but it is not evidence of commercially useful superiority.

**Confidence:** Medium

**Why this confidence level**

The source gives concrete experimental details, but it is a secondary news report describing IBM's own claim and the benchmark is highly specialized and constrained.

**Evidence**

- IBM reported a one-qubit-versus-one-bit majority-of-three task in which a calibrated noisy quantum circuit achieved 93% success, versus 87.5% for the restricted classical comparator. The article emphasizes that the comparison used severely limited memory and that current devices remain noisy. [S2]

#### Finding 2

**Claim**

For present business applications, the retrieved evidence does not establish a demonstrated advantage over the best unconstrained classical alternatives.

**Confidence:** Medium

**Why this confidence level**

This directly addresses practical usefulness, but it comes from a single secondary source and does not provide systematic benchmark data across applications.

**Evidence**

- The IBM report says that business applications such as supply-chain and shipping optimization remain areas of investigation, while researchers are mostly finding quantum and classical systems comparable on small-scale problems and only theorizing about future advantages. [S2]

#### Finding 3

**Claim**

Near-term commercial usefulness is a forecast rather than an established result, with respondents concentrating on the 2026–2030 period and disagreeing substantially about timing.

**Confidence:** Medium

**Why this confidence level**

The figures are specific and include uncertainty, but the source is a report of vendor sentiment rather than an independent technical or economic demonstration.

**Evidence**

- An Omdia vendor survey reported that 39% expected customers to use quantum computers operationally in 2026, while 56% expected a clear economic advantage in 2026. However, only 29% forecast at least 100 logical qubits with 99.999% two-qubit logical-gate fidelity in 2027; 25% placed that milestone in 2029 and another 25% in 2030 or later. [S1]

#### Finding 4

**Claim**

The most frequently identified early commercial opportunity in the retrieved material is quantum simulation of molecules, chemicals, and materials, but this remains prospective.

**Confidence:** Low

**Why this confidence level**

The opportunity areas are repeated, but S4 and S5 are general promotional or user-generated summaries and do not demonstrate application-level advantage.

**Evidence**

- The Omdia survey identified physical simulation of molecular and chemical reactions as a leading commercial opportunity. Other sources similarly describe chemistry, materials, drug discovery, optimization, cryptography, and machine learning as potential application areas, using possibility-oriented language rather than demonstrated production results. [S1] [S4] [S5]

#### Finding 5

**Claim**

The retrieved sources do not adequately document the biggest technical barriers, although they do establish that noise and the need for fault-tolerant hardware are central limitations.

**Confidence:** Medium

**Why this confidence level**

Noise and logical-qubit requirements are directly supported, but the sources do not provide a comprehensive treatment of error-correction overhead, scaling, control, interconnects, algorithmic limits, or operating cost.

**Evidence**

- The IBM account states that current quantum computers are too noisy to achieve the perfect result of the idealized experiment. The Omdia forecast frames useful performance in terms of large numbers of high-fidelity logical qubits, implying that error correction, logical-qubit scale, and gate fidelity are prerequisites for broader advantage. [S1] [S2]

### Conflicts Found

- The sources differ in what they call quantum advantage. S2 treats a narrowly constrained one-qubit experiment as an experimentally verified advantage, while S1 discusses economically meaningful advantages and explicitly distinguishes them from making classically intractable problems tractable. These claims are conditional on different benchmark definitions and are not directly comparable. [S1] [S2]
- Projected timelines are optimistic but internally dispersed: the survey reports substantial expectations for useful operations and economic advantage in 2026, while forecasts for the stated 100-logical-qubit, high-fidelity milestone extend from 2027 to 2030 or later. [S1]
- S4 and S5 make broad claims of exponential speedups and superiority across areas such as optimization, machine learning, and drug discovery, whereas S2 reports that practical systems are currently generally comparable to classical systems on small-scale problems. The broad claims are prospective and unsupported by the retrieved evidence as demonstrations. [S2] [S4] [S5]

### Important Gaps

- Has any quantum processor delivered a reproducible, end-to-end economic advantage on a commercially relevant workload against a strong, state-of-the-art classical baseline?
- Which application classes—especially chemistry, materials, optimization, or sampling—have the strongest independently validated evidence of future advantage?
- What are the quantitative requirements for fault tolerance, including physical-to-logical-qubit overhead, error-correction thresholds, circuit depth, and algorithm runtime?
- How much do data-loading, measurement, error-mitigation, calibration, cryogenic operation, and integration costs reduce any algorithmic speedup?
- What specific technical barriers currently dominate: physical error rates, error-correction overhead, scaling and connectivity, control electronics, or the absence of useful algorithms and workflows?

**Analysis Duration:** 15.80s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The sources support a careful distinction between a narrow demonstrated benchmark and projected commercial value, but they are insufficient to answer the central question responsibly: there is no independent, application-level evidence or rigorous treatment of the main technical barriers. Most supporting material beyond S2 is vendor sentiment or low-quality promotional/user-generated content.

**Next Search**

> independent review quantum computing commercial advantage demonstrated applications fault tolerance technical barriers logical qubits error correction 2024

---

# Iteration 2

## 1. Search

**Query**

> independent review quantum computing commercial advantage demonstrated applications fault tolerance technical barriers logical qubits error correction 2024

**Why this query**

The sources support a careful distinction between a narrow demonstrated benchmark and projected commercial value, but they are insufficient to answer the central question responsibly: there is no independent, application-level evidence or rigorous treatment of the main technical barriers. Most supporting material beyond S2 is vendor sentiment or low-quality promotional/user-generated content.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S6 — IonQ | Demystifying Logical Qubits and Fault Tolerance**
  URL: https://www.ionq.com/resources/demystifying-logical-qubits-and-fault-tolerance
- **S7 — Quantum Error Correction and Fault-Tolerant Computing: Recent Progress in Codes, Decoders, and Architectures[v1] | Preprints.org**
  URL: https://www.preprints.org/manuscript/202509.2149/v1
- **S8 — Quantinuum's Fault-Tolerance Advantage: Turning Quantum Reliability into Commercial Usefulness**
  URL: https://www.quantinuum.com/blog/quantinuums-fault-tolerance-advantage-turning-quantum-reliability-into-commercial-usefulness
- **S9 — What is next in quantum advantage? | Quantum Frontiers**
  URL: https://quantumfrontiers.com/2026/02/28/what-is-next-in-quantum-advantage
- **S10 — The road to useful quantum computing**
  URL: https://www.moodys.com/web/en/us/insights/quantum/the-road-to-useful-quantum-computing.html

**Search Duration:** 2.35s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Current quantum computers have demonstrated quantum advantage only under narrow, task-specific definitions—not commercially useful advantage over strong classical systems.

**Confidence:** High

**Why this confidence level**

Several sources consistently distinguish laboratory or benchmark-specific advantage from useful commercial performance. However, the evidence is not a systematic survey of every workload.

**Evidence**

- The accumulated evidence describes a tiny, artificially constrained majority-of-three experiment as an experimental advantage, while noting that present systems remain noisy and business applications have not shown superiority over unconstrained classical alternatives. [S2]
- Moody’s distinguishes “supremacy” experiments from commercial advantage: supremacy experiments may outperform classical computers on specially selected tasks that are not commercially relevant, and later classical algorithms have sometimes narrowed or eliminated the reported lead. [S10]
- A Caltech-affiliated analysis states that quantum computers can outperform classical ones in the sense of existing advantage experiments, but that current devices are still nowhere near advantageous applications in condensed-matter physics or quantum chemistry. [S9]

#### Finding 2

**Claim**

Fault-tolerant and logical-qubit demonstrations are important technical milestones, but they do not yet constitute application-level quantum advantage.

**Confidence:** Medium

**Why this confidence level**

The distinction between reliability milestones and commercial advantage is clear, but S8 is a company account and S1 is a vendor survey rather than independent validation.

**Evidence**

- Quantinuum reports logical qubits with substantially improved error rates, logical-qubit teleportation, error-correction milestones, and an early materials-and-magnetism computation using logical qubits. These are demonstrations of reliability and encoded computation, not evidence of an economic advantage over classical computation. [S8]
- The Caltech analysis characterizes fault tolerance as demonstrated for at least a few logical qubits, but says that combining fault tolerance with quantum advantage—and reaching useful application regimes—remains a future milestone. [S9]
- The Omdia survey forecasts commercial operation and economic advantage mainly in the 2026–2030 period, with substantial disagreement about when systems will reach 100 high-fidelity logical qubits. [S1]

#### Finding 3

**Claim**

A useful intermediate target may be roughly 100 well-functioning logical qubits, but even that regime is not clearly sufficient for the first major applications and is still far beyond current proof-of-principle systems.

**Confidence:** Medium

**Why this confidence level**

This is a technically informed expert assessment, but it is an opinionated roadmap rather than a consensus threshold or demonstrated application benchmark.

**Evidence**

- The Caltech analysis considers 100 logical qubits capable of perhaps 100,000 gates as a meaningful next regime, requiring thousands of physical qubits. It nevertheless estimates that this remains one or more orders of magnitude away from early applications such as some many-body simulations or cryptographic tasks. [S9]
- The same analysis identifies a further milestone—fault-tolerant quantum advantage that is classically verifiable—because existing random-circuit experiments are difficult to verify and cryptographic proofs of quantumness require much larger resources. [S9]

#### Finding 4

**Claim**

The dominant technical barrier is not merely increasing the physical-qubit count; it is scaling high-quality error correction into large, useful logical circuits at acceptable resource and operating cost.

**Confidence:** High

**Why this confidence level**

The sources independently converge on error correction, fidelity, scaling, control, and resource overhead as central barriers. S7 is not peer reviewed and S6 is vendor-authored, but the barrier categories are also consistent with the broader accumulated evidence.

**Evidence**

- IonQ explains that logical qubits require encoding multiple physical qubits, that useful logical qubits are difficult to build, and that present logical implementations can incur major disadvantages. It emphasizes the importance of physical-qubit fidelity and modular architecture. [S6]
- The QEC review identifies correlated and coherent noise, leakage, measurement errors, real-time decoder performance, cryogenic control, and scalable logical gates as critical engineering challenges. It reports progress toward below-threshold operation but says the reliability and resource efficiency needed for large-scale computation remain difficult. [S7]
- Moody’s notes that current NISQ devices have noise, short qubit lifetimes, and insufficient scale; accurate commercial computation requires error correction and therefore logical qubits. [S10]

#### Finding 5

**Claim**

The application areas most often projected to benefit are chemistry, materials and molecular simulation, with optimization and finance also frequently proposed, but the retrieved evidence does not demonstrate superior commercial performance in these areas.

**Confidence:** Medium

**Why this confidence level**

The opportunity areas are consistently identified, but there is no retrieved head-to-head, end-to-end evidence showing a customer-relevant advantage.

**Evidence**

- The Omdia survey identifies molecular and chemical simulation as a leading opportunity and lists other prospective use cases. [S1]
- Quantinuum describes early logical-qubit work involving materials and magnetism, but presents it as progress toward useful workloads rather than a comparative commercial benchmark. [S8]
- The accumulated sources report that practical quantum and classical systems are generally comparable on small-scale business problems, while broad claims of speedups remain theoretical or promotional. [S2] [S4] [S5]

### Conflicts Found

- Sources use different thresholds for “quantum advantage.” S2 treats a tightly constrained toy experiment as an advantage, whereas S1, S9, and S10 focus on commercial value, useful accuracy, verification, and comparison with strong classical baselines. These are conditional differences in definition rather than direct experimental contradictions. [S1] [S2] [S9] [S10]
- Industry sources describe logical-qubit and fault-tolerance progress as a practical path toward commercial usefulness, while the Caltech analysis emphasizes that even a few logical qubits and early logical computations remain far from advantageous chemistry or materials applications. The disagreement is primarily about interpretation and timeline, not about whether technical milestones occurred. [S6] [S8] [S9]
- S6 suggests that high-quality physical qubits and partial error mitigation or correction may generate early commercial value in the near term, whereas S10 states more categorically that advantage and utility require fault-tolerant computing. The sources therefore differ on whether useful pre-fault-tolerant value is plausible, while neither provides a demonstrated broad commercial advantage. [S6] [S10]

### Important Gaps

- Has any quantum processor delivered a reproducible, independently audited, end-to-end economic advantage on a commercially relevant workload against a state-of-the-art classical baseline?
- For chemistry, materials, optimization, and sampling, what concrete logical-qubit counts, circuit depths, accuracy levels, and runtimes are required for advantage?
- What is the physical-to-logical-qubit overhead for realistic codes and workloads, including decoding, connectivity, magic-state production, and fault-tolerant universal gates?
- Can quantum systems deliver a net advantage after accounting for data loading, measurement, error correction, calibration, cryogenics, control electronics, cloud access, and classical preprocessing?
- Which claims of early NISQ commercial value have been independently replicated with customer-relevant metrics rather than asserted by vendors?

**Analysis Duration:** 18.54s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources substantially improve the account of technical barriers and clarify that logical-qubit demonstrations are not application-level advantage. However, the central commercial question remains unresolved because the retrieved material still lacks an independent, end-to-end economic benchmark and robust workload-specific resource estimates.

**Next Search**

> independent benchmark quantum computing commercial advantage real-world workload classical baseline chemistry materials optimization 2024 2025

---

# Iteration 3

## 1. Search

**Query**

> independent benchmark quantum computing commercial advantage real-world workload classical baseline chemistry materials optimization 2024 2025

**Why this query**

The new sources substantially improve the account of technical barriers and clarify that logical-qubit demonstrations are not application-level advantage. However, the central commercial question remains unresolved because the retrieved material still lacks an independent, end-to-end economic benchmark and robust workload-specific resource estimates.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S11 — Setting the Benchmark: Independent Study Ranks Quantinuum #1 in Performance**
  URL: https://www.quantinuum.com/blog/setting-the-benchmark-independent-study-ranks-quantinuum-1-in-performance
- **S12 — Which Real-World Use Cases for Quantum Computers Are Now on the Way? | IDTechEx Research Article**
  URL: https://www.idtechex.com/en/research-article/which-real-world-use-cases-for-quantum-computers-are-now-on-the-way/31103
- **S13 — A Reality Check on Forbes’ "20 Real-World Quantum Computing Applications"**
  URL: https://postquantum.com/industry-news/forbes-20-quantum-computing
- **S14 — Practical quantum advantage signals a new commercial era for quantum computing**
  URL: https://q-ctrl.com/blog/practical-quantum-advantage-signals-a-new-commercial-era-for-quantum-computing
- **S15 — Real World Quantum: Exploring Current Use Cases | Industry Advancement | QWC 2025**
  URL: https://www.youtube.com/watch?v=uzU8hZg5BJo

**Search Duration:** 2.59s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources do not overturn the conclusion that commercially useful quantum advantage has not yet been independently established.

**Confidence:** High

**Why this confidence level**

The new material adds evidence of improving platform performance and early enterprise experimentation, but neither provides an independently audited, end-to-end commercial comparison.

**Evidence**

- Quantinuum reports that an independent study ranked its H1-1 and H2-1 systems highest among 19 QPUs on QAOA performance, but this is a hardware-performance benchmark, not a demonstration that a customer-relevant workload beats the best classical alternative economically or operationally. [S11]
- The industry conference transcript says enterprises are using quantum computing, particularly for exploratory optimization and many-body problems, but characterizes the field as still in its early stages, with relatively limited customer acquisition and revenue growth. [S15]
- The existing evidence distinguishes benchmark-specific or laboratory advantage from commercial advantage; the new benchmark evidence is consistent with that distinction. [S9] [S10] [S11]

### Conflicts Found

- Q-CTRL claims a 3,000-times wall-clock speedup for a materials-simulation problem against an industry-standard classical alternative and labels this “practical quantum advantage.” However, the retrieved material is a vendor announcement; it does not independently establish the baseline, total workflow cost, reproducibility, or whether the result has been externally validated. This conflicts with the accumulated conclusion only if the vendor claim is treated as established evidence rather than as a claim requiring verification. [S14] [S2] [S9] [S10]
- The new industry material presents current enterprise use and commercial momentum more positively than the accumulated evidence, but it still describes quantum computing as nascent and does not report customer-level superiority over classical systems. [S14] [S15] [S2]

### Important Gaps

- Whether Q-CTRL's reported 3,000-times materials-simulation speedup survives independent replication and a comparison including data preparation, compilation, error suppression, hardware access, and classical post-processing.
- What exact classical algorithm, hardware, accuracy target, and total wall-clock accounting underlie the S14 comparison.
- Whether current enterprise quantum use reported in S15 produces measurable improvements in cost, quality, runtime, or revenue rather than pilot-stage experimentation.
- Whether QAOA hardware benchmarks such as S11 correlate with performance on complete, commercially relevant optimization workflows.

**Analysis Duration:** 9.11s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The most important unresolved issue is the apparent new claim of practical commercial advantage in S14. It could materially change the answer, but the retrieved source is a vendor-authored announcement and does not provide enough independently verifiable methodological detail. A focused search for the underlying study and independent assessments would resolve whether this is a demonstrated advantage or a promotional claim.

**Next Search**

> Q-CTRL 3000x practical quantum advantage materials simulation arXiv 2605.04025 independent verification classical baseline

---

# Iteration 4

## 1. Search

**Query**

> Q-CTRL 3000x practical quantum advantage materials simulation arXiv 2605.04025 independent verification classical baseline

**Why this query**

The most important unresolved issue is the apparent new claim of practical commercial advantage in S14. It could materially change the answer, but the retrieved source is a vendor-authored announcement and does not provide enough independently verifiable methodological detail. A focused search for the underlying study and independent assessments would resolve whether this is a demonstrated advantage or a promotional claim.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S16 — Q-CTRL Achieves 3,000x Speedup in Quantum Materials Simulation - Quantum Computing Report**
  URL: https://quantumcomputingreport.com/q-ctrl-achieves-3000x-speedup-in-quantum-materials-simulation
- **S17 — Q-CTRL Delivers 3,000x Speedup in Materials Discovery for the Energy Sector with Quantum Computing, Demonstrates Evidence of Practical Quantum Advantage | Q-CTRL**
  URL: https://q-ctrl.com/blog/q-ctrl-delivers-3-000x-speedup-in-materials-discovery-for-the-energy-sector-with-quantum-computing-and-demonstrates-evidence-of-practical-quantum-advantage
- **S18 — Q-CTRL Claims Practical Quantum Advantage**
  URL: https://postquantum.com/industry-news/qctrl-fermi-hubbard-3000x-quantum-speedup
- **S19 — Q-CTRL Delivers 3,000x Speedup in Materials Discovery for the Energy Sector with Quantum Computing**
  URL: https://thequantuminsider.com/2026/05/06/qctrl-practical-quantum-advantage-materials-discovery

**Search Duration:** 3.36s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Q-CTRL and IBM report a potentially important application-level quantum advantage claim in materials simulation, but it remains a vendor-led result rather than an independently established commercial advantage.

**Confidence:** Medium

**Why this confidence level**

The result is more relevant than prior toy demonstrations and is described with concrete workload, accuracy, and runtime details, but the available evidence is still primarily company-reported and does not establish end-to-end economic advantage.

**Evidence**

- Q-CTRL reports that a 120-qubit IBM processor simulated Fermi–Hubbard dynamics in about two minutes, versus more than 100 hours for an industry-standard TDVP tensor-network implementation, with reported agreement within approximately 1% RMSE and more than 10,000 two-qubit operations. [S16] [S17] [S19]
- The claimed task concerns electron dynamics in a materials-science model of known scientific relevance, rather than an artificial sampling or supremacy benchmark. However, the commercial relevance is to a model problem and materials R&D workflow, not a demonstrated product, discovery, or customer-level economic outcome. [S16] [S17] [S19]
- The reporting is based principally on Q-CTRL's announcement and associated coverage; the retrieved material does not independently audit the classical baseline, total workflow costs, reproducibility, or the underlying manuscript's comparison methodology. [S16] [S17] [S19]

#### Finding 2

**Claim**

The 3,000-fold figure is conditional on the selected classical baseline and observable/comparison protocol, and its status as a general quantum advantage is contested.

**Confidence:** High

**Why this confidence level**

The conditional nature of the 3,000-fold result and the existence of a substantive baseline dispute are directly documented. The final technical verdict remains unresolved.

**Evidence**

- Q-CTRL's comparison uses the TDVP solver in ITensor and reports a 3,000-fold wall-clock difference after increasing classical simulation resolution; the claim is therefore relative to a specific implementation and hardware configuration. [S16] [S17] [S19]
- Algorithmiq reportedly reproduced a single-site result from the 120-qubit data on a MacBook Air in about 2.5 minutes using Majorana Propagation, potentially narrowing the claimed advantage. Q-CTRL responded that the quantum run simultaneously produces all 120 occupations and thousands of correlators, while the classical method computes observables separately, and challenged the absence of quantitative error analysis in the reproduction. [S18]
- The dispute remains unresolved: the available account says both sides intend to submit data to a quantum-advantage tracker, but it does not provide a settled, independently evaluated comparison across all observables, accuracy targets, and total costs. [S18]

#### Finding 3

**Claim**

This new result strengthens the case that pre-fault-tolerant hardware may have useful performance in narrowly selected scientific workloads, but it does not overturn the broader conclusion that commercially useful quantum advantage has not yet been independently demonstrated across real customer workflows.

**Confidence:** High

**Why this confidence level**

The new evidence is consistent with a more nuanced conclusion: isolated practical utility may be emerging, while general commercially useful advantage remains unproven.

**Evidence**

- The reported experiment used noisy hardware with runtime error suppression rather than a large fault-tolerant logical-qubit system, indicating that useful results may be possible before full fault tolerance for specialized tasks. [S16] [S17] [S18]
- The accumulated evidence distinguishes benchmark- or workload-specific advantage from broad commercial superiority, and the new materials result still lacks independent end-to-end validation and evidence of business outcomes such as lower total cost, faster discovery, or improved product performance. [S2] [S9] [S10] [S16] [S17] [S18]
- The result is a substantial technical milestone—large digital Fermi–Hubbard simulation with deep circuits and quantitative comparison—but a milestone is not itself proof that quantum computers are generally close to replacing or outperforming classical systems commercially. [S18]

#### Finding 4

**Claim**

The leading technical barriers remain controlling noise and scaling error suppression or correction without making the full workflow too expensive or slow.

**Confidence:** High

**Why this confidence level**

Independent accumulated sources and the new experiment converge on hardware noise, error-management overhead, scaling, and fair benchmarking as central barriers.

**Evidence**

- The experiment required extensive circuit compilation, more than 9,000–13,000 two-qubit gates in reported configurations, and software-based runtime error suppression to obtain the stated accuracy on noisy hardware. [S16] [S17] [S18]
- The broader evidence identifies correlated and coherent noise, leakage, measurement errors, decoder performance, cryogenic control, scalable logical gates, physical-to-logical-qubit overhead, and system scale as major obstacles to large useful circuits. [S6] [S7] [S10]
- The baseline dispute shows that algorithm choice, observable throughput, accuracy validation, and comparison against newly developed classical methods are themselves barriers to establishing a durable advantage. [S18]

### Conflicts Found

- Q-CTRL characterizes the Fermi–Hubbard result as the first practical quantum advantage and a basis for positive ROI, whereas the retrieved coverage notes that a newer classical method reproduced at least a single-site result nearly as quickly and that the full comparison remains disputed. The disagreement concerns whether beating one current industry-standard tool is sufficient, not whether the experiment occurred. [S17] [S18]
- Q-CTRL and affiliated coverage emphasize simultaneous production of many observables and approximately 1% RMSE across the output as evidence favoring the quantum comparison. Algorithmiq's reported reproduction challenges the runtime advantage for at least one observable, but the retrieved material lacks a common quantitative accuracy and workload comparison. [S16] [S17] [S18]
- The sources differ on whether present noisy hardware can already provide commercial value: Q-CTRL claims it has done so for materials simulation, while the accumulated independent assessments continue to treat fault-tolerant or independently validated application advantage as a future or unresolved milestone. [S9] [S10] [S17] [S18]

### Important Gaps

- Whether the underlying Q-CTRL/IBM result has been independently reproduced using the same full set of observables, accuracy target, and wall-clock accounting.
- Whether the comparison remains favorable against the best available classical algorithms, including Majorana Propagation and suitably optimized GPU or tensor-network implementations.
- Whether the two-minute quantum figure includes compilation, calibration, repeated measurements, error suppression, data transfer, and classical post-processing, and whether the classical figure includes equivalent end-to-end costs.
- Whether the simulated one-dimensional Fermi–Hubbard model translates into a real materials-discovery workflow that produces measurable scientific or economic value.
- What fraction of the claimed advantage comes from computing many observables simultaneously versus algorithmic or baseline-selection differences.

**Analysis Duration:** 19.54s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources introduce a potentially significant application-level result, but also a concrete and unresolved challenge to its classical baseline. A focused search for independent technical analysis or the primary manuscript's complete benchmarking methodology would materially improve the answer.

**Next Search**

> independent analysis Q-CTRL IBM 3000x Fermi-Hubbard quantum advantage TDVP Majorana Propagation benchmark

---

# Iteration 5

## 1. Search

**Query**

> independent analysis Q-CTRL IBM 3000x Fermi-Hubbard quantum advantage TDVP Majorana Propagation benchmark

**Why this query**

The new sources introduce a potentially significant application-level result, but also a concrete and unresolved challenge to its classical baseline. A focused search for independent technical analysis or the primary manuscript's complete benchmarking methodology would materially improve the answer.

**Results**

5 results retrieved.

2 new unique sources added.

### Sources

- **S20 — Q-CTRL and IBM Report 3,000x Speedup in Materials Simulation - Türkiye Kuantum Platformu**
  URL: https://kuantum.ssb.gov.tr/en/developments/q-ctrl-and-ibm-report-3000x-speedup-in-materials-simulation
- **S21 — Quantum advantage by Q-Ctrl and IBM**
  URL: https://www.youtube.com/watch?v=wRyVEJa4J64

**Search Duration:** 3.44s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources reinforce that the reported 3,000-fold materials-simulation advantage is a company-reported claim requiring independent verification, not an established commercial advantage.

**Confidence:** High

**Why this confidence level**

S20 directly and explicitly qualifies the claim. S21 independently reinforces the distinction between a technically meaningful benchmark and commercial relevance, although it is a low-authority commentary source.

**Evidence**

- S20 explicitly describes the result as a company statement and says that its quantum-advantage framing remains subject to independent verification, while reporting the 120-qubit Fermi–Hubbard experiment and runtime error suppression. [S20]
- S21 repeats the 3,000-fold comparison but also states that the experiment did not simulate a specific commercial compound and had no commercial or practical relevance, despite describing it as a scientific milestone. [S21]

#### Finding 2

**Claim**

The Fermi–Hubbard result may represent a more realistic scientific workload than a toy supremacy experiment, but it does not demonstrate end-to-end value for materials discovery or an energy-sector product.

**Confidence:** Medium

**Why this confidence level**

The sources support the characterization of the workload and its limits, but S21 is an informal video and S20 is derivative reporting rather than an independent technical evaluation.

**Evidence**

- S21 describes a 60-site Fermi–Hubbard system mapped onto 120 physical qubits and explains that the model represents electron behavior, but acknowledges that no specific commercial compound was simulated and that the problem itself lacked commercial or practical relevance. [S21]
- S20 reports the same result as a 120-qubit Fermi–Hubbard simulation using runtime error suppression, but limits its conclusion to highlighting the role of error suppression in near-term computing rather than documenting customer or economic outcomes. [S20]

#### Finding 3

**Claim**

The reported speedup depended materially on software-based error suppression and custom execution methods, underscoring that noise management and full-workflow accounting remain central barriers.

**Confidence:** Medium

**Why this confidence level**

The use of error suppression is directly reported, but the detailed mechanism and runtime accounting in S21 are not independently validated in the retrieved material.

**Evidence**

- S20 states that runtime error-suppression techniques were used in the reported 3,000-fold comparison. [S20]
- S21 attributes the result to custom fermionic mapping, dynamical decoupling, hardware-specific pulse adjustments, and machine-learning-based error suppression; it also distinguishes the two-minute core quantum runtime from an approximately 2.5-minute total process. [S21]
- The accumulated evidence identifies noise, error suppression or correction overhead, compilation, calibration, and fair end-to-end comparison as major barriers to durable advantage. [S16] [S17] [S18] [S20] [S21]

#### Finding 4

**Claim**

The new sources do not materially change the overall assessment: demonstrated quantum advantage exists for narrow or disputed benchmarks, while commercially useful advantage over strong classical systems remains unproven.

**Confidence:** High

**Why this confidence level**

The new evidence is consistent with, rather than contradictory to, the accumulated conclusion.

**Evidence**

- S20 explicitly preserves the distinction between a reported practical-advantage claim and independent verification. [S20]
- S21 calls the experiment a milestone but says the simulated problem had no commercial or practical relevance, which prevents it from establishing customer-level advantage. [S21]
- Prior sources consistently distinguish benchmark-specific advantage from reproducible, end-to-end commercial superiority and identify fault tolerance, scaling, and fair classical baselines as unresolved requirements. [S2] [S9] [S10] [S16] [S17] [S18]

### Conflicts Found

- S21's promotional framing calls the result a landmark practical quantum-advantage demonstration, but the same transcript says that the problem had no commercial or practical relevance. This is an internal tension between technical milestone language and the commercial-advantage definition. [S21]
- S21 presents the 3,000-fold comparison as a direct speedup against a classical supercomputer, while the accumulated evidence notes unresolved disputes over the classical algorithm, observable coverage, accuracy targets, and end-to-end cost accounting. S20 also explicitly says independent verification is still needed. [S18] [S20] [S21]

### Important Gaps

- Whether the underlying Q-CTRL/IBM result has been independently reproduced with the same observables, accuracy target, and complete runtime accounting.
- Whether the reported two-minute or 2.5-minute quantum runtime includes all relevant compilation, calibration, repeated measurement, error-suppression, data-transfer, and post-processing costs.
- Whether the result remains faster than the best current classical algorithms rather than only the selected TDVP implementation.
- Whether the Fermi–Hubbard benchmark produces useful outputs for a real materials-discovery workflow or measurable customer-level economic value.
- What logical-qubit scale and fault-tolerance overhead are required to extend such demonstrations to reliable, application-relevant workloads.

**Analysis Duration:** 12.38s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources add corroboration and clarify that the benchmark itself was not commercially relevant, but they do not resolve the most important outstanding issue: independent, end-to-end validation against the best classical baseline. That evidence would materially improve the answer.

**Next Search**

> independent reproduction Q-CTRL IBM 120-qubit Fermi-Hubbard 3000x speedup classical baseline full observables accuracy

---

# Iteration 6

## 1. Search

**Query**

> independent reproduction Q-CTRL IBM 120-qubit Fermi-Hubbard 3000x speedup classical baseline full observables accuracy

**Why this query**

The new sources add corroboration and clarify that the benchmark itself was not commercially relevant, but they do not resolve the most important outstanding issue: independent, end-to-end validation against the best classical baseline. That evidence would materially improve the answer.

**Results**

5 results retrieved.

1 new unique source added.

### Sources

- **S22 — Fast, accurate, high-resolution simulation of large-scale ...**
  URL: https://arxiv.org/html/2605.04025v1

**Search Duration:** 3.35s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new source provides a stronger technical basis for the Q-CTRL/IBM materials-simulation claim, but it still does not establish general commercially useful quantum advantage.

**Confidence:** Medium

**Why this confidence level**

The paper is a direct technical source and materially improves evidentiary quality over a company announcement, but the retrieved content is an arXiv preprint and the result remains narrow, conditional, and not an end-to-end commercial demonstration.

**Evidence**

- The arXiv paper reports experiments on a superconducting processor using up to 120 qubits for one-dimensional Fermi–Hubbard dynamics, with up to 90 Trotter steps and quantitative agreement with approximate classical TDVP simulations at roughly 1% RMSE over part of the evolution. [S22]
- The paper reports up to a 3,000-fold wall-clock advantage over an optimized TDVP simulation with bond dimension χ=4096 at evolution times near the limit of quantum/classical agreement. [S22]
- The workload is a scientifically relevant many-body simulation beyond exact statevector scale, but it is a one-dimensional model problem and the source does not report a customer workflow, product outcome, total economic cost, or comparison against every state-of-the-art classical method. [S22] [S18] [S20] [S21]

#### Finding 2

**Claim**

This is best classified as a conditional, workload-specific demonstrated advantage claim—not yet as independently established commercial advantage.

**Confidence:** High

**Why this confidence level**

The conditional baseline and scope are explicit in the paper, while the unresolved comparison issues are directly documented in the accumulated evidence.

**Evidence**

- The comparison is specifically against an optimized time-dependent variational-principle solver at χ=4096, and the reported speedup applies at evolution times where quantum and classical results still agree quantitatively. [S22]
- The source itself describes the quantum processor as competitive where leading classical methods become prohibitively expensive, but it does not demonstrate that the result survives alternative classical algorithms, different hardware, or full workflow accounting. [S22]
- Earlier retrieved evidence documents a substantive challenge from an alternative classical method and notes unresolved issues around observables, accuracy, reproducibility, and total runtime accounting. [S18] [S20] [S21]

#### Finding 3

**Claim**

The result narrows the gap between laboratory advantage and practical scientific utility, but not the gap to broad commercial usefulness.

**Confidence:** High

**Why this confidence level**

The distinction between a realistic scientific benchmark and commercial value is directly supported and consistent across the sources.

**Evidence**

- Unlike a deliberately constrained toy benchmark, the experiment addresses fermionic many-body dynamics, measures physical observables such as spin-charge behavior and velocity ratios, and operates at scales beyond exact statevector simulation. [S22]
- The model is nevertheless one-dimensional, and the source does not show that it leads to improved materials discovery, drug development, industrial design, revenue, or lower customer costs. [S22] [S21]
- The accumulated evidence continues to find no independently audited, end-to-end economic advantage on a customer-relevant workload. [S2] [S9] [S10] [S18] [S20]

#### Finding 4

**Claim**

Noise management remains a central barrier even in this more favorable result.

**Confidence:** High

**Why this confidence level**

The paper directly demonstrates dependence on error suppression and limited agreement windows, while multiple prior sources identify the broader engineering consequences.

**Evidence**

- The experiment relies on error suppression to obtain accurate dynamics, and the paper emphasizes hardware noise as a limitation of large-scale digital simulation. [S22]
- The reported circuits use up to 90 Trotter steps, while the claimed agreement and speedup apply only over a limited evolution-time regime; beyond that regime the approximate classical and quantum approaches diverge. [S22]
- Prior evidence identifies correlated and coherent noise, leakage, measurement errors, decoding, control, logical-gate scaling, and physical-to-logical-qubit overhead as unresolved obstacles to larger reliable computations. [S6] [S7] [S10] [S16] [S17] [S18]

#### Finding 5

**Claim**

Classical-baseline selection and fair benchmarking are themselves major remaining barriers to establishing durable advantage.

**Confidence:** High

**Why this confidence level**

The scope of the paper's baseline is explicit, and the unresolved methodological dispute is directly documented.

**Evidence**

- The 3,000-fold figure is relative to one optimized TDVP implementation and bond dimension, rather than a universal comparison with all competitive classical approaches. [S22]
- The accumulated record reports that another classical method reproduced at least a single-site result in comparable time and that the parties disputed observable coverage and accuracy analysis. [S18]
- The available evidence still lacks a common benchmark specifying equivalent observables, accuracy targets, preprocessing, compilation, measurement, error suppression, post-processing, and total wall-clock costs. [S18] [S20] [S21]

### Conflicts Found

- S22 presents the Fermi–Hubbard experiment as a competitive platform with up to 3,000-fold speedup over an optimized TDVP solver, while S18 reports a competing classical method that substantially narrows the advantage for at least one observable. This is a conditional disagreement over baseline, observable set, accuracy, and runtime accounting, not over whether the quantum experiment occurred. [S22] [S18]
- S22's language supports calling the result a workload-specific computational advantage, whereas S20 and S21 caution that the claim remains subject to independent verification and lacks commercial or practical relevance to a specific product. The difference reflects distinct meanings of “advantage.” [S22] [S20] [S21]
- The paper reports agreement with approximate classical simulation at about 1% RMSE before the approaches diverge, while the headline speedup applies near the boundary of that agreement. Thus the speedup is not evidence of unrestricted accuracy or superiority across all evolution times. [S22]

### Important Gaps

- Has the S22 result been independently reproduced using the full set of observables, the same accuracy target, and complete end-to-end runtime accounting?
- Does the 3,000-fold comparison survive the best current classical algorithms, including alternatives to the selected TDVP implementation and optimized accelerator-based methods?
- How much of the reported quantum runtime includes compilation, calibration, repeated measurement, error suppression, data transfer, and classical post-processing?
- Can the one-dimensional Fermi–Hubbard benchmark produce outputs that improve a real materials-discovery or industrial materials workflow?
- What logical-qubit scale and fault-tolerance overhead are required to extend this result to larger, deeper, higher-accuracy, and less structured applications?
- Whether pre-fault-tolerant error suppression can scale without exponential calibration, sampling, and control costs.

**Analysis Duration:** 15.88s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The important question can now be answered responsibly: narrow benchmark-specific advantages have been demonstrated or credibly reported, including a more relevant but conditional Fermi–Hubbard result; broad, independently verified commercial advantage has not been established. Further searching could refine the disputed benchmark, but the central conclusion and major barriers are already sufficiently supported.

**Stop Reason:** sufficient_evidence

---

# Final Research Decision

**Research Stopped Because**

The analyzer determined that the important parts of the question could be answered responsibly.

**Stop Reason:** sufficient_evidence

**Searches Performed:** 6

**Unique Sources:** 22

**Remaining Uncertainty**

- Independent reproduction of the Fermi–Hubbard result using the full observable set, common accuracy targets, and complete end-to-end runtime accounting.
- A comparison with the best current classical algorithms, including alternative tensor-network, accelerator-based, and other specialized methods.
- A transparent accounting of compilation, calibration, repeated measurements, error suppression, data transfer, classical post-processing, hardware access, and operating costs.
- Evidence that a quantum simulation improves a real materials-discovery, chemistry, optimization, or industrial workflow rather than only a scientifically relevant model problem.
- Workload-specific resource estimates for physical-to-logical-qubit overhead, circuit depth, decoding, connectivity, and fault-tolerant gate synthesis.
- Evidence that present enterprise deployments produce measurable improvements in cost, quality, runtime, revenue, or scientific outcomes.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 6 | 19.71s |
| OpenAI Analysis | 6 | 91.25s |
| Report Generation | 1 | 22.19s |
| Total Run | — | 133.16s |
