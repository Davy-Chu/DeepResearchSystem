# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

**Status:** Completed

**Stop Reason:** sufficient_evidence

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 7 / 10

**Unique Sources:** 23

**OpenAI Calls:** 8

**Tavily Calls:** 7

**Started:** 2026-09-01T06:29:31-04:00

**Ended:** 2026-09-01T06:31:58-04:00

**Total Runtime:** 147.49s

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

- **S1 — The Potential of Commercial Quantum Computers**
  URL: https://www.quera.com/blog-posts/potential-of-commercial-quantum-computers
- **S2 — Quantum computing: What leaders need to know now | MIT Sloan**
  URL: https://mitsloan.mit.edu/ideas-made-to-matter/quantum-computing-what-leaders-need-to-know-now
- **S3 — Quantum firms race to market as the industry sees ' ...**
  URL: https://www.cnbc.com/2026/03/30/quantum-computing-firms-go-public-breakthroughs-commercialization.html
- **S4 — Quantum Computing: Potential and Challenges aheadPlain Concepts**
  URL: https://www.plainconcepts.com/quantum-computing-potential-challenges
- **S5 — How long before quantum computers can benefit society? That’s Google’s US$5 million question**
  URL: https://theconversation.com/how-long-before-quantum-computers-can-benefit-society-thats-googles-us-5-million-question-226257

**Search Duration:** 2.98s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Commercially useful quantum advantage has not yet been established by the supplied evidence; current systems remain experimental or early-stage commercial services rather than broadly superior replacements for classical computing.

**Confidence:** Medium

**Why this confidence level**

Several sources independently describe the technology as immature, but the sources do not provide standardized performance benchmarks or a systematic survey of deployed commercial workloads.

**Evidence**

- MIT Sloan describes the field as “not quite ready for prime time” and says the hardware and software for the most complex problems may not be available until 2035 or later. [S2]
- The Conversation reports a lack of progress in developing quantum computers that outperform classical predecessors and says practical applications are still being actively sought through a major competition. [S5]
- CNBC characterizes quantum computing as still experimental, while reporting expectations of practical advantage around 2028–2029 and wider commercial use in the 2030s. [S3]

#### Finding 2

**Claim**

A distinction is needed between demonstrated quantum advantage and theoretical or projected advantages. The supplied sources describe Google’s 2019 “quantum supremacy” as a milestone, but do not establish that it delivered commercially useful performance on a practical business task.

**Confidence:** Medium

**Why this confidence level**

The conceptual distinction is directly supported, but the evidence supplied lacks primary experimental results needed to assess particular demonstrations rigorously.

**Evidence**

- Plain Concepts says Google achieved quantum supremacy in 2019 and presents this as evidence that useful purposes are feasible, but its account does not identify a practical commercial workload, compare end-to-end costs, or establish economic advantage. [S4]
- MIT Sloan defines quantum advantage as solving problems beyond classical reach, while proposing the separate standard of “quantum economic advantage”: solving a problem faster than a comparably priced classical computer. [S2]
- The Conversation says there are only a few notable quantum algorithms with theoretical advantages and emphasizes the continuing bottleneck of demonstrating an advantage over classical computers. [S5]

#### Finding 3

**Claim**

The strongest theoretical or projected opportunities are concentrated in specialized problem classes, especially quantum-system simulation, some cryptographic tasks, and possibly large optimization or machine-learning workloads; advantages are not expected to apply broadly to ordinary business problems.

**Confidence:** Medium

**Why this confidence level**

The sources agree on specialization and identify plausible domains, but several application claims are prospective and are not accompanied by practical-scale demonstrations.

**Evidence**

- MIT researchers’ framework concludes that small to moderate-sized problems, which are common in typical businesses, generally will not benefit; large problems with exponential algorithmic gains or very large datasets are more promising. [S2]
- The sources identify simulation of molecules and materials, drug discovery, optimization, finance, machine learning, and cryptography as possible application areas. [S1] [S2] [S5]
- The Conversation notes that Shor’s algorithm and BB84 are prominent examples of quantum algorithms or protocols associated with advantages, while few additional advantageous algorithms have followed. [S5]

#### Finding 4

**Claim**

The largest technical barriers are reliable scaling and fault tolerance: reducing physical and two-qubit error rates, preserving coherence, implementing error correction with manageable overhead, and controlling increasingly large interconnected systems.

**Confidence:** High

**Why this confidence level**

Multiple sources consistently identify the same engineering bottlenecks, with direct descriptions of error, control, cooling, manufacturing, and scale limitations.

**Evidence**

- Quera identifies environmental noise, decoherence, cascading errors, limited coherence, interaction errors, and the large physical-qubit requirements of error correction as central obstacles. [S1]
- Plain Concepts lists fidelity at scale, gate speed, multi-qubit networking, individual-qubit control, cooling, manufacturing, interconnection, decoherence, and external noise as major challenges. [S4]
- Plain Concepts reports technology-specific scaling problems, including control and cooling for superconducting systems, scale and electronics challenges for spin qubits, uncertain million-qubit scaling and error rates for neutral atoms, and increasing qubit numbers as the key obstacle for trapped ions. [S4]

#### Finding 5

**Claim**

Even a technically successful quantum processor will need to beat classical alternatives on total cost, speed, accuracy, and system-level overhead; an asymptotic algorithmic advantage alone may not produce commercial value.

**Confidence:** High

**Why this confidence level**

The economic comparison is explicitly articulated by MIT Sloan and is consistent with the broader caution in Quera’s discussion.

**Evidence**

- MIT Sloan explains that classical computers may run faster even when quantum algorithms use fewer computational steps, and frames usefulness in terms of quantum economic advantage against a comparably priced classical system. [S2]
- Quera notes that classical computers will remain important and that some proposed applications may ultimately prove not to offer an advantage. [S1]

### Conflicts Found

- Plain Concepts presents Google’s 2019 quantum-supremacy result as indicating that useful applications are feasible, whereas The Conversation emphasizes that practical quantum computers outperforming classical systems remain largely unachieved. This is a conditional disagreement: the former concerns a narrow computational milestone, while the latter concerns practical, socially or commercially useful advantage. [S4] [S5]
- Forecasts differ in timing and are not directly comparable: CNBC cites practical advantage around 2028–2029 and broader use in the 2030s, while MIT Sloan relays an estimate that complex hardware and software may not be available until 2035 or later. [S2] [S3]
- The sources describe optimization, finance, machine learning, and energy savings as promising possibilities, but do not demonstrate that these areas currently provide a useful quantum advantage. These claims therefore remain projections rather than established results. [S1] [S2] [S5]

### Important Gaps

- What specific recent experiments, if any, demonstrate end-to-end quantum advantage on a commercially relevant task against the best classical method, including data-loading, error mitigation, runtime, accuracy, and hardware costs?
- What logical-qubit count, logical error rate, circuit depth, connectivity, and error-correction overhead are required for leading applications such as chemistry simulation or cryptanalysis?
- Which proposed optimization, machine-learning, finance, or materials applications retain an advantage after accounting for input/output overhead and strong classical heuristics?
- How do competing hardware modalities compare on independently verified, application-level benchmarks rather than qubit count or isolated gate fidelity?
- The supplied material includes future-dated or forecast-oriented reporting, but does not provide primary-source validation of the cited 2028–2035 timelines.

**Analysis Duration:** 17.96s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The central question cannot yet be answered responsibly on demonstrated advantage because the supplied sources are mainly explanatory, opinion, or media accounts and lack primary benchmark data. A focused search for peer-reviewed or official results on practical quantum advantage would materially improve the assessment and help separate narrow laboratory demonstrations from commercial usefulness.

**Next Search**

> 2023 2024 2025 peer reviewed practical quantum advantage commercially relevant benchmark error correction classical comparison

---

# Iteration 2

## 1. Search

**Query**

> 2023 2024 2025 peer reviewed practical quantum advantage commercially relevant benchmark error correction classical comparison

**Why this query**

The central question cannot yet be answered responsibly on demonstrated advantage because the supplied sources are mainly explanatory, opinion, or media accounts and lack primary benchmark data. A focused search for peer-reviewed or official results on practical quantum advantage would materially improve the assessment and help separate narrow laboratory demonstrations from commercial usefulness.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S6 — Practical quantum advantage signals a new commercial era for quantum computing | Q-CTRL**
  URL: https://q-ctrl.com/blog/practical-quantum-advantage-signals-a-new-commercial-era-for-quantum-computing
- **S7 — Mind the gaps: The fraught road to quantum advantage - arXiv**
  URL: https://arxiv.org/html/2510.19928v3
- **S8 — Setting the Benchmark: Independent Study Ranks Quantinuum #1 in Performance**
  URL: https://www.quantinuum.com/blog/setting-the-benchmark-independent-study-ranks-quantinuum-1-in-performance
- **S9 — Quantum computer completes verified task beyond practical reach of classical simulations**
  URL: https://phys.org/news/2026-07-quantum-task-classical-simulations.html
- **S10 — IBM, UChicago demonstrate ‘quantum advantage,’ outperforming traditional computers with a quantum computer | University of Chicago News**
  URL: https://news.uchicago.edu/story/ibm-uchicago-demonstrate-quantum-advantage-outperforming-traditional-computers-quantum

**Search Duration:** 2.58s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new evidence strengthens the distinction between demonstrated computational advantage and commercially useful advantage: IBM/UChicago report a verified quantum computation beyond the practical reach of leading classical simulations, but this is not evidence of a commercial workload or positive economic return.

**Confidence:** Medium

**Why this confidence level**

The result is reported by a university news source and a science-news outlet with a linked arXiv preprint, but the supplied material is secondary or institutional reporting and does not independently establish commercial usefulness.

**Evidence**

- The reported experiment used a structured alternative to random-circuit sampling designed to permit error detection and verification, executed 70 logical qubits, 2,415 logical two-qubit operations, and 468 logical T gates; the quantum computation took about 15 minutes while leading classical simulation methods faced prohibitive runtimes. [S9] [S10]
- The task is described as a hard sampling/computational benchmark, not as chemistry, optimization, finance, cryptography, or another end-user business application. The sources do not report customer value, total system cost, input/output overhead, or a useful classical workflow being displaced. [S9] [S10]
- The prior evidence already distinguished Google’s narrow 2019 milestone from quantum economic advantage; the new demonstration supports that distinction rather than showing that it has been overcome. [S2] [S4] [S5] [S9] [S10]

#### Finding 2

**Claim**

A verified, error-protected demonstration indicates meaningful technical progress toward fault-tolerant quantum computing, but it does not show that broadly useful fault-tolerant systems are close.

**Confidence:** Medium

**Why this confidence level**

The sources provide concrete reported milestones and a clear technical gap, but the supplied excerpt does not provide enough detail to independently assess logical error rates, code distance, scaling behavior, or how representative the demonstration is.

**Evidence**

- IBM/UChicago report successful execution of 70 logical qubits while shielding them from errors, with thousands of logical operations and a verification method intended to increase confidence in hard quantum states. [S9] [S10]
- The perspective article describes the transition from NISQ devices to fault-tolerant, application-scale quantum computers as nascent, arduous, expensive, prolonged, and highly uncertain; it estimates a large gap between fewer than 10^4 two-qubit operations on leading NISQ machines and roughly 10^12 or more for broadly useful systems. [S7]

#### Finding 3

**Claim**

Q-CTRL claims a commercially relevant practical quantum advantage in materials simulation, including a 3,000-times wall-clock speedup, but this claim should be treated as unverified and promotional pending examination of the underlying research and independent benchmarking.

**Confidence:** Low

**Why this confidence level**

This is a potentially important new claim, but only the interested vendor’s account is supplied and the relevant research is not included. The magnitude and commercial interpretation cannot responsibly be accepted without primary-paper and independent evidence.

**Evidence**

- Q-CTRL says its software-augmented IBM quantum system solved a materials-related fermionic-simulation problem more than 3,000 times faster than a state-of-the-art industry-standard classical alternative, with practically relevant runtime and accuracy meeting or exceeding user expectations. [S6]
- The claim comes from the vendor whose software and technology are being credited, and the supplied content does not identify the exact benchmark, classical implementation, hardware/system costs, data-transfer overhead, reproducibility, or independent replication. The page is also dated May 6, 2026. [S6]
- Q-CTRL itself characterizes Google’s 2019 result as scientifically important but commercially irrelevant, implicitly applying a stricter standard to its own claimed practical advantage. [S6]

#### Finding 4

**Claim**

The leading technical barriers remain largely unchanged: scalable error correction and fault tolerance, verification, and the development of mature algorithms with demonstrable application-level value.

**Confidence:** High

**Why this confidence level**

The new perspective and the earlier technical sources converge on the same barriers, while the IBM/UChicago report confirms that verification remains difficult.

**Evidence**

- The arXiv perspective identifies four gaps: moving from error mitigation to active correction, scaling fault tolerance, moving from heuristics to mature and verifiable algorithms, and establishing credible quantum-simulation advantage. [S7]
- IBM/UChicago explicitly identify verification of hard quantum results as a major challenge, even while presenting their experiment as progress on that problem. [S9] [S10]
- Earlier sources identify noise, decoherence, gate errors, control, cooling, interconnects, and error-correction overhead as central engineering barriers. [S1] [S4]

### Conflicts Found

- S7 states that practically useful and economically viable quantum computations had not yet been achieved, whereas S6 claims Q-CTRL achieved practical quantum advantage and positive ROI in materials simulation. This is a direct but unresolved disagreement: S6 is a vendor claim about a 2026 demonstration, while S7 is a perspective assessment whose publication/version timing and coverage relative to S6 are not clear from the supplied material. [S6] [S7]
- S9 and S10 describe the IBM/UChicago experiment as meeting the fundamental criteria for quantum advantage, while the broader accumulated evidence says commercially useful advantage remains unestablished. The disagreement is conditional rather than necessarily factual: the experiment demonstrates a verified computational separation on a hard sampling task, not necessarily an economically useful application. [S2] [S5] [S9] [S10]
- S6 reports a 3,000-times speedup against an industry-standard classical alternative, but S7 emphasizes that credible advantage requires a useful answer, quantifiable quantum resources, and a persuasive comparison against classical methods. The supplied material does not show whether the Q-CTRL result satisfies all those criteria. [S6] [S7]

### Important Gaps

- Does the IBM/UChicago 70-logical-qubit demonstration have any intrinsic scientific or commercial value beyond establishing a verified computational benchmark?
- What exactly is the Q-CTRL materials-simulation task, and does the 3,000-times figure include state preparation, compilation, error suppression, data movement, repetitions, post-processing, and comparable hardware and operating costs?
- Was Q-CTRL’s claimed result independently reproduced or evaluated against the best available classical method rather than an industry-standard baseline?
- What logical error rates, code distances, physical-qubit overheads, and scaling trends underlie the IBM/UChicago demonstration?
- Do the new demonstrations materially shorten the timeline to economically useful applications, or do they mainly advance verification and fault-tolerant engineering?

**Analysis Duration:** 17.34s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources introduce two major claims that could substantially change the answer: a verified IBM/UChicago computational advantage and Q-CTRL’s claimed commercial materials-simulation advantage. The first is not clearly commercially useful, and the second is unverified vendor-reported evidence. Primary papers and independent assessments are needed before revising the conclusion about commercial advantage.

**Next Search**

> 2026 Q-CTRL 3000x materials simulation practical quantum advantage arXiv independent benchmark IBM

---

# Iteration 3

## 1. Search

**Query**

> 2026 Q-CTRL 3000x materials simulation practical quantum advantage arXiv independent benchmark IBM

**Why this query**

The new sources introduce two major claims that could substantially change the answer: a verified IBM/UChicago computational advantage and Q-CTRL’s claimed commercial materials-simulation advantage. The first is not clearly commercially useful, and the second is unverified vendor-reported evidence. Primary papers and independent assessments are needed before revising the conclusion about commercial advantage.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S11 — Q-CTRL Achieves 3,000x Speedup in Quantum Materials Simulation - Quantum Computing Report**
  URL: https://quantumcomputingreport.com/q-ctrl-achieves-3000x-speedup-in-quantum-materials-simulation
- **S12 — Q-CTRL Claims 3,000x Quantum Speedup for Materials Science Simulations on IBM Quantum Platform - HPCwire**
  URL: https://www.hpcwire.com/off-the-wire/q-ctrl-claims-3000x-quantum-speedup-for-materials-science-simulations-on-ibm-quantum-platform
- **S13 — Q-CTRL Delivers 3,000x Speedup in Materials Discovery for the Energy Sector with Quantum Computing, Demonstrates Evidence of Practical Quantum Advantage | Q-CTRL**
  URL: https://q-ctrl.com/blog/q-ctrl-delivers-3-000x-speedup-in-materials-discovery-for-the-energy-sector-with-quantum-computing-and-demonstrates-evidence-of-practical-quantum-advantage
- **S14 — Q-CTRL Claims Practical Quantum Advantage**
  URL: https://postquantum.com/industry-news/qctrl-fermi-hubbard-3000x-quantum-speedup
- **S15 — Q-CTRL Delivers 3,000x Speedup in Materials Discovery for the Energy Sector with Quantum Computing**
  URL: https://thequantuminsider.com/2026/05/06/qctrl-practical-quantum-advantage-materials-discovery

**Search Duration:** 2.01s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources strengthen the case that a potentially application-relevant quantum speedup has been reported, but they do not yet establish commercially useful quantum advantage conclusively.

**Confidence:** Medium

**Why this confidence level**

Multiple sources consistently report the same concrete experiment and benchmark, making the technical result more substantial than a purely promotional claim. However, independent commercial validation and full-system benchmarking are still absent.

**Evidence**

- Q-CTRL and several industry outlets report a 120-qubit Fermi–Hubbard materials simulation completed in roughly two to three minutes, versus more than 100 hours for an ITensor/TDVP classical benchmark, with reported agreement around 1% RMSE. [S11] [S13] [S15]
- The task concerns interacting-electron dynamics relevant to materials science and energy research, rather than an artificial random-circuit benchmark; the reported output includes multiple physical observables and phenomena such as spin–charge separation. [S11] [S13] [S14]
- The evidence remains primarily vendor-originated or derivative reporting. The supplied sources do not independently establish total cost, data preparation and transfer overhead, repeated-run requirements, or commercial customer outcomes. [S11] [S12] [S13] [S15]

#### Finding 2

**Claim**

The reported 3,000-fold figure is conditional on the selected classical baseline and therefore should not be treated as a general quantum-versus-classical advantage.

**Confidence:** Medium

**Why this confidence level**

The source directly documents a meaningful baseline dispute and a relevant alternative classical method, but the supplied material does not include the underlying paper, code, or a standardized apples-to-apples benchmark.

**Evidence**

- The comparison is specifically against the TDVP solver in the ITensor tensor-network package, with the classical runtime increasing substantially when higher resolution was required. [S11] [S13] [S14]
- A subsequent account reports that Algorithmiq reproduced a single-site result in about 2.5 minutes on a standard MacBook Air using Majorana Propagation, a method published before the Q-CTRL announcement and previously used as a classical benchmark in a Google Fermi–Hubbard experiment. [S14]
- The same account says the comparison is not decisive because the quantum run produced many observables simultaneously, whereas the classical method reportedly computes them one at a time; it also notes that quantitative error comparisons across all observables remain unresolved. [S14]

#### Finding 3

**Claim**

Relative to the accumulated evidence, the Q-CTRL result moves one specialized materials-simulation case from purely projected advantage toward reported practical advantage, but it does not overturn the broader conclusion that commercially useful advantage is not yet broadly demonstrated.

**Confidence:** Medium

**Why this confidence level**

The result is more application-oriented than earlier supremacy-style demonstrations, but its scope and independent validation are limited.

**Evidence**

- Q-CTRL defines practical advantage as outperforming the best available conventional alternative on a real-world problem of known commercial or scientific relevance and claims its experiment meets that definition. [S13]
- The broader prior evidence distinguishes narrow computational separation from quantum economic advantage and reports no established general commercial replacement for classical computing. [S2] [S5] [S7]
- The new result is confined to a particular one-dimensional Fermi–Hubbard simulation, software configuration, hardware platform, and classical comparison; no evidence shows that the advantage generalizes to routine industrial workloads or produces demonstrated business value. [S11] [S13] [S14]

#### Finding 4

**Claim**

The main technical barriers identified previously remain: suppressing errors in deep circuits, scaling control and hardware, and validating useful results against strong classical methods.

**Confidence:** High

**Why this confidence level**

The new experiment provides a concrete example of the importance of error suppression and benchmarking, while multiple prior sources consistently identify the same engineering and validation barriers.

**Evidence**

- The reported simulation required more than 9,000–10,000 two-qubit operations and relied on compilation improvements and runtime error suppression to obtain the claimed accuracy on present hardware. [S11] [S14]
- The broader evidence identifies fault-tolerant error correction, physical-qubit overhead, coherence, control, cooling, interconnects, verification, and mature application algorithms as unresolved barriers. [S1] [S4] [S7] [S9] [S10]
- The Algorithmiq comparison illustrates that classical algorithm development can materially change whether a claimed speedup persists. [S14]

### Conflicts Found

- Q-CTRL, IBM, and derivative coverage characterize the Fermi–Hubbard experiment as practical quantum advantage, while the reported Algorithmiq result challenges the headline speedup using a newer classical method. The disagreement is conditional: Q-CTRL’s 3,000x figure may hold against TDVP while failing, narrowing, or requiring qualification against other classical algorithms and multi-observable comparisons. [S11] [S13] [S14]
- Q-CTRL and its supporting coverage imply that the experiment establishes positive ROI or a commercial signal, but the supplied evidence does not report an actual customer workflow, procurement cost, end-to-end system cost, or realized business return. This conflicts with the stricter accumulated standard for quantum economic advantage. [S2] [S7] [S13] [S15]
- The new result is more application-relevant than the IBM/UChicago sampling demonstration, but both remain consistent with the broader finding that a verified computational or scientific advantage is not automatically a commercially useful economic advantage. [S2] [S7] [S9] [S10] [S13]

### Important Gaps

- Does the underlying Q-CTRL paper provide a complete apples-to-apples comparison against all credible classical methods, including Majorana Propagation and GPU-accelerated alternatives?
- Does the reported timing include state preparation, compilation, queueing, calibration, measurement repetitions, error-suppression overhead, data transfer, and post-processing?
- Is the approximately 1% RMSE maintained across all reported observables and evolution times, or only for selected outputs?
- How many useful observables does the quantum processor obtain per run compared with the classical alternatives, and how should that be reflected in a fair runtime comparison?
- Has the result been independently reproduced on IBM hardware or another platform?
- Does the simulation generate actionable materials-discovery information beyond reproducing dynamics in a one-dimensional benchmark model?
- What are the hardware, software, energy, and operating costs, and is there evidence of positive ROI for an actual industrial workflow?
- What logical error rates and fault-tolerance overheads will be required to extend this type of simulation to scientifically decisive, larger and less idealized materials problems?

**Analysis Duration:** 18.02s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources materially improve the evidence for a specialized reported advantage, but the central question remains unresolved because the headline speedup is baseline-sensitive and the strongest counterevidence and validation claims are not supported by the supplied primary paper or independent benchmarking. One focused search for the underlying manuscript and independent evaluation would materially improve the answer.

**Next Search**

> arXiv 2605.04025 Fermi-Hubbard Q-CTRL independent benchmark Majorana Propagation TDVP 3000x

---

# Iteration 4

## 1. Search

**Query**

> arXiv 2605.04025 Fermi-Hubbard Q-CTRL independent benchmark Majorana Propagation TDVP 3000x

**Why this query**

The new sources materially improve the evidence for a specialized reported advantage, but the central question remains unresolved because the headline speedup is baseline-sensitive and the strongest counterevidence and validation claims are not supported by the supplied primary paper or independent benchmarking. One focused search for the underlying manuscript and independent evaluation would materially improve the answer.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S16 — [2605.04025] Fast, accurate, high-resolution simulation of large-scale Fermi-Hubbard models on a digital quantum processor**
  URL: https://arxiv.org/abs/2605.04025
- **S17 — [2605.04025v1] Fast, accurate, high-resolution simulation of large-scale Fermi-Hubbard models on a digital quantum processor**
  URL: https://arxiv.org/abs/2605.04025v1
- **S18 — Q-CTRL announces a successful practical quantum ...**
  URL: https://runninginterference.substack.com/p/q-ctrl-announces-a-successful-practical

**Search Duration:** 1.78s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The Q-CTRL Fermi–Hubbard result is a more application-oriented reported advantage than a random-circuit or purely artificial benchmark, but it remains a single specialized demonstration rather than evidence of broad commercial usefulness.

**Confidence:** Medium

**Why this confidence level**

The new source gives concrete experimental and benchmarking details, but it is commentary based largely on the vendor announcement and preprint rather than an independent peer-reviewed validation.

**Evidence**

- The experiment reportedly simulated a one-dimensional Fermi–Hubbard model, a model relevant to correlated-electron materials research, using an IBM quantum processor and Q-CTRL software; the reported runtime was about two minutes versus more than 100 hours for an ITensor TDVP calculation on a 32-vCPU, 64-GB AWS instance. [S18]
- The source explicitly distinguishes this kind of practical or commercial advantage from mathematically provable computational advantage and notes that the result is confined to a specific calculation and comparison. [S18]
- The accumulated evidence indicates that no broad, independently validated quantum economic advantage has yet displaced classical workflows across commercial applications. [S2] [S7] [S13] [S15]

#### Finding 2

**Claim**

The headline 3,000-fold speedup is conditional on the chosen classical baseline and should not be generalized to quantum computing overall.

**Confidence:** High

**Why this confidence level**

The conditional nature of the benchmark is directly stated, and the prior evidence supplies a concrete competing-classical-method concern.

**Evidence**

- The comparison used the ITensor package's time-dependent variational principle solver on a specified AWS classical instance; the result therefore concerns that implementation, hardware configuration, and problem formulation. [S18]
- The source cautions that future classical innovation could change the comparison and explains that commercial advantage can depend on what alternative the customer uses. [S18]
- The accumulated evidence reports an alternative classical method, Majorana Propagation, that reproduced at least a single-site result quickly, while noting that the comparison is not yet apples-to-apples across all observables. [S14]

#### Finding 3

**Claim**

The Q-CTRL experiment depended substantially on software and error-suppression improvements rather than fault-tolerant logical qubits, reinforcing that present practical demonstrations do not eliminate the fault-tolerance barrier.

**Confidence:** High

**Why this confidence level**

The source provides concrete details about the techniques used, and multiple independent prior sources identify the same remaining engineering problems.

**Evidence**

- Q-CTRL reportedly customized circuits for the specific IBM hardware, reduced two-qubit gates by about 60% relative to the native implementation, and used real-time error suppression rather than relying only on post-run error mitigation. [S18]
- The broader evidence identifies active error correction, scalable fault tolerance, physical-qubit overhead, verification, and deep-circuit reliability as unresolved barriers. [S1] [S4] [S7] [S9] [S10] [S11] [S14]

#### Finding 4

**Claim**

Verification and scaling remain important limitations even for the reported materials-simulation result.

**Confidence:** High

**Why this confidence level**

These are explicit limitations in the new source and align with the accumulated concerns about verification, generalization, and independent benchmarking.

**Evidence**

- The source says the reported speed advantage applies at the last problem size where the classical computer can still keep up and agree with the quantum result; larger instances raise the problem of checking quantum outputs when classical replication is infeasible. [S18]
- The experiment used a one-dimensional model, while practically important materials often require two- or three-dimensional modeling; the source states that the route from this demonstration to such applications may not be linear. [S18]
- The preprint had not yet undergone peer review according to the commentary, and the supplied arXiv pages provide bibliographic information but no substantive abstract or independent validation details. [S16] [S17] [S18]

### Conflicts Found

- S18 characterizes the Q-CTRL result as an unusually strong, objectively measured practical advantage against a best-in-class classical solution, while S14 reports a competing classical approach and unresolved apples-to-apples comparisons. The disagreement concerns whether the selected TDVP baseline is sufficiently comprehensive to support the headline speedup, not whether the reported experiment occurred. [S18] [S14]
- S18 presents the result as a meaningful commercial-advantage signal, but also acknowledges that it is a preprint, uses a one-dimensional model, and may not scale smoothly to realistic two- or three-dimensional materials. This qualifies, rather than resolves, the broader conflict between vendor claims of practical advantage and the stricter standard of demonstrated quantum economic advantage. [S18] [S6] [S7] [S13]

### Important Gaps

- Does the full preprint provide an apples-to-apples comparison against all credible classical algorithms, including Majorana Propagation, GPU implementations, and optimized tensor-network methods?
- Do the reported quantum runtimes include circuit compilation, calibration, queueing, measurement repetitions, error-suppression overhead, data transfer, and post-processing?
- Is the reported accuracy maintained across all observables and parameter regimes, or primarily at the last classically verifiable point?
- Can the method scale from the one-dimensional benchmark to two- and three-dimensional materials problems with scientifically decisive outputs and manageable hardware cost?
- Has the result been independently reproduced and peer-reviewed?
- Does it produce actionable materials-discovery or industrial value, rather than only a faster simulation of a benchmark model?

**Analysis Duration:** 14.75s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new source materially improves the characterization of the Q-CTRL claim and its limitations, but the central unresolved issue remains the full primary-paper benchmark: whether the claimed classical baseline is genuinely state of the art, what the end-to-end quantum cost and accuracy are, and whether the result generalizes beyond a one-dimensional model.

**Next Search**

> 2605.04025 Fermi-Hubbard Q-CTRL independent benchmark Majorana Propagation TDVP full paper runtime overhead

---

# Iteration 5

## 1. Search

**Query**

> 2605.04025 Fermi-Hubbard Q-CTRL independent benchmark Majorana Propagation TDVP full paper runtime overhead

**Why this query**

The new source materially improves the characterization of the Q-CTRL claim and its limitations, but the central unresolved issue remains the full primary-paper benchmark: whether the claimed classical baseline is genuinely state of the art, what the end-to-end quantum cost and accuracy are, and whether the result generalizes beyond a one-dimensional model.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S19 — Fast, accurate, high-resolution simulation of large-scale Fermi-Hubbard models on a digital quantum processor**
  URL: https://arxiv.org/html/2605.04025v1
- **S20 — Fermi-Hubbard on a quantum computer, part 7: Majorana propagation as a laptop competitor - Edukaizen**
  URL: https://edukaizen.nl/fermi-hubbard-quantum-computer-part-7-majorana-propagation-as-a-laptop-competitor
- **S21 — Fermi-Hubbard on a quantum computer, part 5: quantum advantage or time-to-answer? - Edukaizen**
  URL: https://edukaizen.nl/fermi-hubbard-quantum-computer-part-5-quantum-advantage-or-time-to-answer

**Search Duration:** 1.99s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The Q-CTRL Fermi–Hubbard experiment is a reported application-oriented quantum-versus-classical performance result, but it remains conditional rather than conclusive evidence of commercially useful quantum advantage.

**Confidence:** Medium

**Why this confidence level**

S19 is a primary preprint with concrete experimental and comparison details, but it is not yet independent peer-reviewed validation and does not establish economic value.

**Evidence**

- The preprint reports a 120-qubit digital simulation of one-dimensional Fermi–Hubbard dynamics, with quantum outputs agreeing with TDVP simulations at approximately 1% RMSE over part of the evolution range and a claimed wall-clock advantage of up to 3,000× against an optimized TDVP solver with bond dimension 4096. [S19]
- The task models strongly correlated electron dynamics relevant to materials science, making it more application-oriented than random-circuit sampling or an abstract computational-supremacy benchmark. [S19]
- The result is limited to a specific one-dimensional model, hardware platform, compilation strategy, error-suppression method, observable set, and TDVP baseline; it does not establish customer value, total cost, or displacement of an industrial classical workflow. [S19] [S18]

#### Finding 2

**Claim**

The 3,000× figure should be interpreted as a benchmark-specific comparison, not a general quantum speedup.

**Confidence:** High

**Why this confidence level**

The conditionality is explicit in the primary preprint and reinforced by a concrete alternative classical-method comparison.

**Evidence**

- The reported comparison is specifically against an optimized TDVP tensor-network simulation at bond dimension χ=4096 and at evolution times near the limit where quantum and classical results still agree. [S19]
- The classical cost depends strongly on bond dimension, evolution time, system size, and the chosen observable; the preprint states that the quantum and TDVP approaches diverge beyond the agreement range. [S19]
- A Majorana-propagation comparison reports substantially different results for a single observable: a low cutoff was faster than the quantum execution proxy but visibly less accurate, while a higher cutoff was more accurate but took roughly 19 minutes. [S20] [S21]

#### Finding 3

**Claim**

The new material strengthens the case for a narrow present-day practical or time-to-answer advantage in one specialized simulation, while leaving broad quantum economic advantage unestablished.

**Confidence:** Medium

**Why this confidence level**

There is meaningful evidence of a specialized technical advantage under stated conditions, but the evidence does not satisfy a strong end-to-end economic standard.

**Evidence**

- The quantum route reportedly obtains a full set of local charge and spin-related measurements from a 60-site simulation, whereas some classical alternatives target selected observables or require truncation and convergence choices. [S19] [S20] [S21]
- The alternative-method discussion emphasizes that the relevant comparison includes accuracy targets, parameter selection, convergence validation, preprocessing, error suppression, post-processing, and other workflow costs—not merely circuit execution time. [S20] [S21]
- No supplied source reports an actual industrial customer workflow, procurement or operating costs, end-to-end data movement, repeated-run requirements, or realized financial return from the experiment. [S19] [S20] [S21] [S2] [S7]

#### Finding 4

**Claim**

Classical-algorithm choice and validation are major remaining barriers to credible claims of quantum advantage, in addition to hardware error correction.

**Confidence:** High

**Why this confidence level**

The new sources provide a concrete benchmark example, while multiple earlier sources independently support the hardware and fault-tolerance barriers.

**Evidence**

- Majorana propagation can be substantially faster for a selected observable, but its accuracy depends on a cutoff whose adequacy may require convergence studies or comparison with a more expensive reference. [S20] [S21]
- The comparison illustrates that a classical method need not reproduce the complete quantum state to compete on a specific business or scientific output; fair benchmarking must define the required observables and accuracy beforehand. [S20] [S21]
- The broader evidence continues to identify scalable fault tolerance, error correction, deep-circuit reliability, verification, control, cooling, and physical-qubit overhead as unresolved engineering barriers. [S1] [S4] [S7] [S9] [S10] [S19]

#### Finding 5

**Claim**

The experiment does not remove the fault-tolerance barrier because it relies on error suppression and hardware-specific compilation rather than demonstrating a broadly scalable fault-tolerant application system.

**Confidence:** High

**Why this confidence level**

The methods are described directly in S19 and align with the established distinction between near-term error suppression and scalable fault tolerance.

**Evidence**

- The preprint attributes its accuracy to an efficient fermion-to-qubit mapping, reduced circuit complexity, and error suppression, while using up to 90 Trotter steps and thousands of operations. [S19]
- The accumulated evidence distinguishes error suppression or mitigation from active, scalable error correction and identifies the latter as necessary for application-scale systems. [S7] [S11] [S14]
- The experiment concerns a one-dimensional benchmark model; extending it to scientifically decisive two- or three-dimensional materials problems is explicitly unresolved in the supplied commentary. [S18]

### Conflicts Found

- S19 presents the result as a competitive platform with up to a 3,000× runtime advantage over optimized TDVP, while S20 reports that a different classical method can beat the quantum execution proxy for a single observable at a lower cutoff and approach the reference more closely at a higher cutoff. This is a conditional benchmark disagreement, not evidence that either reported experiment did not occur. [S19] [S20]
- S19 compares a quantum calculation producing multiple observables with a TDVP baseline, whereas S20 focuses on one observable using Majorana propagation. The sources therefore do not establish an apples-to-apples winner unless the required outputs, accuracy, validation work, and total workflow are fixed in advance. [S19] [S20] [S21]
- The vendor/preprint framing supports a practical quantum advantage for this materials-simulation case, while the accumulated stricter standard requires independent benchmarking and demonstrated economic value. The disagreement concerns the definition and evidentiary threshold for “commercially useful,” not the existence of the reported benchmark. [S19] [S18] [S2] [S7]

### Important Gaps

- Does the 3,000× result survive comparison with all credible classical approaches, including Majorana propagation, symmetry-aware tensor-network methods, GPU implementations, and methods optimized for the particular observables required?
- Do the reported quantum timings include compilation, calibration, queueing, measurement repetitions, error-suppression overhead, data transfer, and post-processing?
- Is the approximately 1% RMSE maintained across all observables and relevant parameter regimes, or only at selected evolution times and against selected TDVP settings?
- Has the experiment been independently reproduced, peer-reviewed, or evaluated by users outside the vendor and affiliated research groups?
- Does the simulation produce actionable materials-discovery information or only demonstrate dynamics in a one-dimensional benchmark model?
- What hardware, software, energy, and operating costs would apply in a real materials-science workflow, and is there evidence of positive ROI?
- Can the approach scale to two- and three-dimensional models and larger scientifically decisive instances without losing accuracy or incurring prohibitive sampling and error-suppression costs?

**Analysis Duration:** 18.41s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new primary preprint materially improves the evidence for a narrow technical advantage, but the central commercial question remains unresolved because independent replication, comprehensive classical benchmarking, full workflow accounting, and actual economic value are absent. One focused search for independent evaluation would materially improve the answer.

**Next Search**

> independent benchmark replication Q-CTRL Fermi-Hubbard 120 qubit 3000x TDVP Majorana propagation full workflow cost

---

# Iteration 6

## 1. Search

**Query**

> independent benchmark replication Q-CTRL Fermi-Hubbard 120 qubit 3000x TDVP Majorana propagation full workflow cost

**Why this query**

The new primary preprint materially improves the evidence for a narrow technical advantage, but the central commercial question remains unresolved because independent replication, comprehensive classical benchmarking, full workflow accounting, and actual economic value are absent. One focused search for independent evaluation would materially improve the answer.

**Results**

5 results retrieved.

1 new unique source added.

### Sources

- **S22 — Anastasia Marchenkova on X: "BREAKING: Q-CTRL's Practical Quantum Advantage has landed 🛬 Big thanks to Michael Biercuk (@MJBiercuk) , Yuval Baum, and Gavin Hartnett at @qctrlHQ for the pre-publication briefing on their new results. Conversations like these are what make writing about this field… / X**
  URL: https://x.com/amarchenkova/status/2051883294191693892

**Search Duration:** 2.13s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new source adds operational detail supporting Q-CTRL’s reported narrow, application-oriented advantage, but does not establish broad commercially useful quantum advantage.

**Confidence:** Medium

**Why this confidence level**

The source supplies concrete experimental details and is consistent with the primary preprint evidence, but it is an X post based on a pre-publication briefing and does not independently validate the result or its commercial significance.

**Evidence**

- An independent commentator reports a one-dimensional Fermi–Hubbard simulation on IBM’s ibm_boston processor using 120 qubits and 9,057 two-qubit gates across 152 layers; the reported quantum runtime was about two minutes versus about 100 hours for ITensor TDVP on a 32-core CPU node, yielding up to a 3,000× speedup at the agreement boundary. [S22]
- The task is a materials-relevant interacting-electron simulation rather than a random-circuit benchmark, but it remains a single one-dimensional model and does not demonstrate customer value, end-to-end economic savings, or displacement of an industrial workflow. [S22] [S19] [S18]

#### Finding 2

**Claim**

The reported Q-CTRL benchmark was run on publicly accessible IBM hardware without privileged access or special calibration, which strengthens its relevance as a reproducible cloud-available demonstration.

**Confidence:** Low

**Why this confidence level**

This is a useful methodological claim, but the supplied evidence is a single secondary social-media account and does not include logs, code, calibration records, or independent replication.

**Evidence**

- The commentator states that the experiment used the public IBM Quantum API and did not receive privileged access or special calibration. [S22]

#### Finding 3

**Claim**

The Q-CTRL result has a defined validity boundary rather than demonstrating an unlimited 3,000× advantage: agreement with the classical baseline is reported through approximately t=5.2, with residual error around 4% at the longest tested times.

**Confidence:** Medium

**Why this confidence level**

The details are consistent with the primary preprint and clarify the conditional nature of the result, but the new source does not provide the underlying error analysis or full observable-by-observable validation.

**Evidence**

- The source reports approximately 1% RMSE against the classical baseline up to t≈5.2 and approximately 4% residual error at the longest tested evolution times, while explicitly identifying where correctness becomes indeterminate. [S22]
- The accumulated preprint evidence likewise limits the claimed advantage to the regime where the quantum and TDVP results agree, and notes that the comparison depends on evolution time, bond dimension, observables, and other benchmark choices. [S19] [S20] [S21]

#### Finding 4

**Claim**

The new source does not resolve the central classical-baseline dispute or the distinction between technical speedup and quantum economic advantage.

**Confidence:** High

**Why this confidence level**

The source confirms the selected benchmark but leaves the principal economic and apples-to-apples benchmarking gaps unchanged.

**Evidence**

- The reported 3,000× comparison remains specifically against ITensor TDVP at a stated bond dimension and CPU configuration; the source does not compare total workflow costs or alternative methods such as Majorana Propagation, GPU implementations, and other optimized solvers. [S22] [S19] [S20]
- No evidence is supplied for state preparation, compilation, queueing, calibration, measurement repetitions, data transfer, post-processing, energy use, hardware cost, or actual customer return on investment. [S22] [S19] [S18] [S2] [S7]

### Conflicts Found

- S22 presents the experiment’s public-access execution and explicit error boundary as evidence of rigor and trustworthiness, whereas S14, S20, and S21 show that the headline speedup remains conditional on the selected classical algorithm, observable set, accuracy target, and workflow definition. These positions are not necessarily contradictory about the experiment itself, but they differ on whether the reported benchmark is sufficient to establish practical advantage. [S22] [S14] [S20] [S21]
- The source supports Q-CTRL’s framing of a practical advantage, while the accumulated evidence continues to require independent benchmarking and demonstrated economic value before classifying the result as commercially useful quantum advantage. [S22] [S19] [S18] [S2] [S7]

### Important Gaps

- Can the public-API execution, absence of privileged calibration, and reported error figures be independently verified from run logs, code, and raw data?
- Does the 3,000× comparison survive a complete apples-to-apples benchmark against Majorana Propagation, GPU implementations, and other classical methods for the same observables and accuracy?
- Do the reported runtimes include all relevant end-to-end costs, including compilation, calibration, repetitions, error suppression, data transfer, and post-processing?
- Does this one-dimensional benchmark produce actionable materials-science information or scale to scientifically decisive two- and three-dimensional problems?
- Is there any actual industrial customer workflow or measured return on investment associated with the result?

**Analysis Duration:** 12.72s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new source strengthens the evidence for a narrowly defined technical demonstration and provides useful reproducibility details, but it is not independent validation and does not answer the most important question: whether the advantage survives comprehensive classical benchmarking and produces end-to-end commercial value.

**Next Search**

> Q-CTRL Fermi-Hubbard 3000x independent benchmark Majorana Propagation peer review public IBM API

---

# Iteration 7

## 1. Search

**Query**

> Q-CTRL Fermi-Hubbard 3000x independent benchmark Majorana Propagation peer review public IBM API

**Why this query**

The new source strengthens the evidence for a narrowly defined technical demonstration and provides useful reproducibility details, but it is not independent validation and does not answer the most important question: whether the advantage survives comprehensive classical benchmarking and produces end-to-end commercial value.

**Results**

5 results retrieved.

1 new unique source added.

### Sources

- **S23 — Quantum advantage by Q-Ctrl and IBM**
  URL: https://www.youtube.com/watch?v=wRyVEJa4J64

**Search Duration:** 1.37s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new source reinforces that the Q-CTRL/IBM Fermi–Hubbard experiment was a specialized technical benchmark, not a demonstrated commercial materials-discovery workflow.

**Confidence:** High

**Why this confidence level**

The source directly makes this qualification, which is consistent with the accumulated evidence that no customer workflow, actionable discovery result, or realized economic return has been demonstrated.

**Evidence**

- The video describes the experiment as relevant to the physics of electron behavior but explicitly states that it did not simulate a specific commercial compound and that the problem had no commercial or practical relevance. [S23]

#### Finding 2

**Claim**

The source reports the same conditional approximately 3,000-fold runtime comparison previously attributed to Q-CTRL and IBM: about two minutes of quantum execution versus about 100 hours for a TDVP classical calculation.

**Confidence:** Medium

**Why this confidence level**

The details are consistent with the primary preprint and prior sources, but this is derivative video reporting and does not independently validate the benchmark.

**Evidence**

- The video reports a 120-qubit IBM Heron experiment representing a 60-site Fermi–Hubbard system, with a two-minute core quantum runtime and a 100-hour TDVP comparison, yielding the stated 3,000× ratio. [S23]

#### Finding 3

**Claim**

The reported result depended on hardware-specific compilation and runtime error-suppression techniques rather than demonstrating scalable fault-tolerant computation.

**Confidence:** High

**Why this confidence level**

The source provides concrete descriptions of the reported techniques, and the broader evidence consistently identifies the absence of scalable fault tolerance as a remaining limitation.

**Evidence**

- The video attributes the result to custom fermionic mapping, dynamical decoupling, hardware-aware machine-learning control, and Q-CTRL software that modifies physical microwave pulses during gate execution. [S23]
- The accumulated evidence distinguishes such error suppression and mitigation from active, scalable error correction and identifies fault tolerance as an unresolved barrier. [S7] [S19] [S22]

#### Finding 4

**Claim**

The source does not resolve the central benchmark and economic questions surrounding the Q-CTRL result.

**Confidence:** High

**Why this confidence level**

These omissions are apparent from the source content and match the unresolved gaps already identified in the research state.

**Evidence**

- It repeats the selected TDVP comparison but provides no comparison with alternative classical methods, no apples-to-apples accounting of all observables and accuracy targets, and no evidence about compilation, repetitions, data transfer, post-processing, hardware cost, or operating cost. [S23]
- It reports no industrial customer, actionable materials-discovery output, or measured return on investment. [S23]

### Conflicts Found

- The video initially frames the result as a 3,000× speedup for materials discovery in the energy sector, but later says the simulated problem was not a specific commercial compound and had no commercial or practical relevance. This supports treating the demonstration as application-motivated physics benchmarking rather than commercial advantage. [S23]
- The video uses promotional language such as “quantum advantage” and “materials discovery,” while its own qualifications and the accumulated evidence indicate that the experiment does not establish quantum economic advantage or a commercially useful replacement for a classical workflow. [S23] [S2] [S7] [S19]

### Important Gaps

- Does the claimed speedup survive comparison with Majorana propagation, GPU implementations, and other strong classical methods for identical observables and accuracy requirements?
- Do the reported timings include all relevant end-to-end costs, including compilation, calibration, repetitions, error suppression, data transfer, and post-processing?
- Can the one-dimensional Fermi–Hubbard benchmark produce actionable materials-discovery information or scale to scientifically decisive two- and three-dimensional problems?
- Has the result been independently reproduced, peer-reviewed, or evaluated in an actual industrial workflow?

**Analysis Duration:** 9.61s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The new source is derivative and largely repeats the existing Q-CTRL/IBM claims. It adds a useful qualification—that no specific commercial compound or practically relevant task was simulated—but does not materially resolve the major unanswered questions about classical baselines, end-to-end costs, independent replication, scalability, or commercial value. The accumulated evidence is sufficient to conclude that the experiment is a narrow reported technical advantage, not established broad commercial quantum advantage.

**Stop Reason:** sufficient_evidence

---

# Final Research Decision

**Research Stopped Because**

The analyzer determined that the important parts of the question could be answered responsibly.

**Stop Reason:** sufficient_evidence

**Searches Performed:** 7

**Unique Sources:** 23

**Remaining Uncertainty**

- A complete independent benchmark of the Q-CTRL experiment against Majorana Propagation, GPU implementations, optimized tensor-network methods, and other credible classical solvers.
- End-to-end timing and cost accounting, including compilation, calibration, queueing, repetitions, error suppression, data movement, post-processing, energy, hardware, and operating costs.
- Independent replication, peer review, raw data, run logs, and code sufficient to verify the Q-CTRL performance and accuracy claims.
- Evidence that the Fermi–Hubbard result produces actionable materials-discovery information or scales from a one-dimensional model to scientifically decisive two- and three-dimensional problems.
- Measured customer outcomes or return on investment from a real industrial quantum-computing workflow.
- Application-specific logical-qubit counts, logical error rates, code distances, and physical-qubit overheads required for chemistry, materials, optimization, or cryptanalytic workloads.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 7 | 14.83s |
| OpenAI Analysis | 7 | 108.82s |
| Report Generation | 1 | 23.84s |
| Total Run | — | 147.49s |
