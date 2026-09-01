# Research Run Log

## Run Summary

**System Version:** evidence-ledger-decomposer-verifier-v1

**Research Question**

How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

**Status:** Failed

**Stop Reason:** max_iterations

**Failure Stage:** OpenAI Ledger Report Generation

**Error**

Ledger report finding 4 cites source ID(s) not attached to its ledger claims: S10, S8

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 15

**OpenAI Calls:** 9

**Tavily Calls:** 3

**Verifier Model:** gpt-5.6-luna

**Started:** 2026-08-31T19:08:54-04:00

**Ended:** 2026-08-31T19:10:47-04:00

**Total Runtime:** 112.76s

---

# Research Plan

## Subquestions

### SQ1 [CORE]

**Question:**

What quantum-computing demonstrations have established a quantum advantage over classical computers, and how strong is the evidence that the advantage is genuine, reproducible, and relevant to useful computation?

**Success criteria:**

Identify leading experimental demonstrations, the task performed, the claimed classical baseline, relevant performance metric, reproducibility or verification status, and whether the result represents a practical computational benefit or primarily a benchmark milestone.

**Initial status:** UNRESEARCHED

### SQ2 [CORE]

**Question:**

What theoretical or projected quantum advantages are expected for commercially relevant applications, and under what assumptions about algorithms, fault tolerance, hardware scale, error rates, and classical competitors?

**Success criteria:**

Distinguish proven asymptotic speedups from estimates or projections; describe application areas, required resources, assumptions, and the strength and uncertainty of evidence supporting commercial usefulness.

**Initial status:** UNRESEARCHED

### SQ3 [CORE]

**Question:**

What commercially useful quantum advantages, if any, are available today or plausibly achievable in the near, medium, and longer term, relative to classical alternatives?

**Success criteria:**

Assess practical usefulness using relevant criteria such as cost, speed, accuracy, scalability, reliability, deployment status, and economic value; preserve explicit time horizons and distinguish demonstrated use from anticipated milestones.

**Initial status:** UNRESEARCHED

### SQ4 [CORE]

**Question:**

What are the biggest remaining technical barriers to commercially useful quantum advantage, and how do they constrain the path from current demonstrations to useful systems?

**Success criteria:**

Prioritize barriers such as error correction and fault tolerance, physical error rates, qubit count and connectivity, control and fabrication, algorithm and software maturity, data-loading and input/output overhead, verification, and system economics, explaining their impact on practical advantage.

**Initial status:** UNRESEARCHED

### SQ5 [SECONDARY]

**Question:**

How should claims of quantum advantage be compared fairly with state-of-the-art classical computing, and what uncertainty remains in judging how close quantum computers are to commercial usefulness?

**Success criteria:**

Specify appropriate classical baselines, resource and cost accounting, problem-size and scaling considerations, benchmark limitations, and major sources of uncertainty or disagreement in current assessments.

**Initial status:** UNRESEARCHED

## Synthesis Requirements

- Separate experimentally demonstrated quantum advantage from theoretical speedups and forward-looking projections throughout the analysis.
- Compare quantum systems with the best relevant classical methods and hardware, not only older or deliberately weakened baselines.
- Connect each proposed advantage to commercial usefulness, including practical resource requirements, economic value, and deployment feasibility.
- Rank the technical barriers by their importance to achieving useful advantage and explain how they affect the timeline.
- Preserve uncertainty by distinguishing established results, plausible projections, and speculative claims.

## Output Requirements

- Provide a direct assessment of how close quantum computers are to commercially useful advantages over classical computers.
- Use a clear comparison between demonstrated, theoretical/projected, and commercially useful advantages.
- Identify and prioritize the biggest remaining technical barriers.
- State relevant assumptions, time horizons, and uncertainty rather than presenting a single unsupported forecast.

---

# Iteration 1

## 1. Search

**Query**

> How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

**Purpose:** GENERAL

**Why this query**

This is the user's original research question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S1 — 5 Key Quantum Computing Breakthroughs in 2026**
  URL: https://www.bqpsim.com/blogs/quantum-computing-breakthroughs
- **S2 — 8 Industry Use Cases for Quantum Computing**
  URL: https://thequantuminsider.com/2026/05/04/quantum-computing-use-cases-real-applications-industries
- **S3 — Quantum computing: What leaders need to know now**
  URL: https://mitsloan.mit.edu/ideas-made-to-matter/quantum-computing-what-leaders-need-to-know-now
- **S4 — Quantum technology firms race to market as the industry sees ‘inflection point’**
  URL: https://www.cnbc.com/2026/03/30/quantum-computing-firms-go-public-breakthroughs-commercialization.html
- **S5 — Quantum Computing – Strategic Recommendations for the ...**
  URL: https://arxiv.org/html/2601.08578v1

**Search Duration:** 2.65s

---

## 2. Evidence Processing

- New claim proposals: 6
- Existing claim updates: 0
- New gaps: 5
- Resolved gaps: 0

**Processing Duration:** 17.71s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

The supplied sources do not establish a commercially useful quantum advantage that has already displaced or outperformed state-of-the-art classical methods in a real industrial deployment.

- S2 supports (direct): States that demonstrations have simulated only small molecules and have not reached systems complex enough to displace classical methods; it also says current hardware lacks the required error rates and qubit counts for useful molecular simulation.
- S5 supports (direct): Describes industrial optimization and machine-learning experiments as evaluations against classical solvers, with verdicts ranging from promise to significant hurdles, rather than reporting an established commercial advantage.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C2

**Claim**

The strongest projected near- or medium-term application area identified in the supplied sources is quantum simulation for chemistry, materials science, and drug discovery; however, the projection depends on substantially larger and more reliable fault-tolerant systems.

- S2 supports (direct): Identifies molecular simulation in drug discovery, materials science, and chemistry as the most viable near-term application area, while noting that current systems are too small and noisy. It cites a commonly stated 5–10 year timeline contingent on hundreds of error-corrected logical qubits.
- S3 supports (direct): Lists matter simulation and drug discovery among areas where quantum algorithms could potentially provide speedups, while emphasizing that usefulness depends on the particular problem and comparison with classical systems.
- S2 contradicts (direct): The same source reports that present molecular demonstrations have not displaced classical methods, so the projected application is not current commercial advantage.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C3

**Claim**

Optimization and machine-learning applications currently have weaker and more uncertain evidence of quantum advantage than quantum simulation, because industrial evaluations must contend with strong classical solvers, limited connectivity, low qubit counts, and hardware errors.

- S5 supports (direct): Reports benchmarking hybrid algorithms against classical solvers for logistics, production, optimization, and machine learning, and explicitly identifies low qubit counts, limited connectivity, and error susceptibility as limitations. Its evaluation framework includes scalability, solution quality, runtime, and transferability.
- S2 supports (direct): States that optimization has highly tuned classical algorithms and that quantum approaches have not demonstrated the ability to beat them; it characterizes optimization, AI, and climate modeling as longer-term or uncertain areas.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C4

**Claim**

A quantum advantage benchmark is not by itself equivalent to commercial usefulness: practical assessment must compare the quantum system with a comparably priced classical alternative while accounting for runtime, solution quality, scalability, and deployment costs.

- S3 supports (direct): Introduces 'quantum economic advantage' as solving a problem faster with a quantum computer than with a comparably priced classical computer, and explains that slower quantum processing can offset algorithmic efficiency.
- S5 supports (direct): Uses model formulation, scalability, solution quality, runtime, and transferability as common evaluation criteria for industrial quantum applications and stresses benchmarking against classical solvers.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C5

**Claim**

The principal technical barriers identified in the supplied sources are error correction and fault tolerance, physical error and decoherence rates, scaling to sufficient logical-qubit counts, connectivity, and reliable control; these barriers currently restrict useful computations to small or shallow workloads.

- S1 supports (direct): Characterizes pre-2026 systems as noisy and error-prone, with decoherence and gate errors limiting reliable computation, and presents error correction, scaling, and fault tolerance as central engineering challenges.
- S2 supports (direct): Says current hardware has error rates and qubit counts insufficient for practically useful molecular simulation.
- S5 supports (direct): Explicitly identifies low qubit counts, limited connectivity, and error susceptibility as hardware limitations affecting industrial hybrid algorithms.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C6

**Claim**

Most ordinary small- to moderate-sized business problems are not expected to benefit from quantum computing, whereas potential benefits are concentrated in problems with suitable structure and very large scale, particularly where an exponential algorithmic improvement could outweigh quantum hardware's lower processing speed.

- S3 supports (direct): Reports the MIT framework's conclusion that small to moderate-sized problems generally will not benefit, while some very large problems with exponential algorithmic gains may; it also notes that quantum processors can be slower than classical computers.
- S2 supports (direct): States that most classical workloads are not good quantum-computing fits and that suitable candidates tend to involve quantum systems or exceptionally large solution spaces.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Gap G1

No supplied source provides a rigorous, independently verified account of a leading experimental quantum-advantage demonstration, including the task, best classical baseline, reproducibility, verification, and total resource cost.

### New Gap G2

The evidence does not establish quantitative fault-tolerant resource requirements—such as physical-to-logical qubit overhead, target error rates, circuit depth, or runtime—for any commercially relevant application.

### New Gap G3

The sources provide projections such as a 5–10 year molecular-simulation horizon and wider commercial timelines, but no independent, systematically justified forecast with explicit hardware, algorithm, and classical-competitor assumptions.

### New Gap G4

The evidence does not quantify the economics of quantum systems versus classical alternatives, including acquisition or cloud cost, energy, throughput, reliability, data-loading overhead, and end-to-end application cost.

### New Gap G5

The supplied material does not rank the remaining barriers quantitatively or demonstrate that proposed error-correction progress is reproducible across platforms and sufficient for useful workloads.

---

## 4. Current Research State

- Claims: 6
- Supported: 6
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 5
- Remaining Searches: 2

### Subquestion Progress

**SQ1:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ3:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ4:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ5:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → PARTIAL (targeted searches: 0)
- SQ3 → PARTIAL (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- SQ5 → PARTIAL (targeted searches: 0)

**Remaining targeted searches:** 2

---

## 5. Independent Verification

### V1 — Claim C3

**Phase:** INITIAL

**Evidence source IDs:** S5, S2

**Verdict:** NEEDS_QUALIFICATION

**Reason**

The supplied sources support the broad comparison: optimization and machine-learning applications are described as more uncertain than molecular or quantum simulation, with strong classical methods and current hardware limitations constraining results. However, the evidence is largely narrative and does not establish a systematic, field-wide comparison or show that each listed barrier is the primary cause of weaker evidence. The claim should be framed as an assessment of current industrial evaluations rather than a definitive ranking of all applications.

**Missing assumptions**

- The comparison is limited to current industrial and near-term evaluations, not theoretical algorithmic results or every optimization and machine-learning subfield.
- ‘Quantum simulation’ refers mainly to molecular and materials simulation, which the sources identify as a more natural prospective application area, not to demonstrated commercial advantage.
- The listed hardware limitations materially affect the evaluated workloads and are not fully offset by algorithmic, error-mitigation, or hybrid methods.
- Strong classical solvers remain the relevant state-of-the-art baseline for the particular optimization and machine-learning instances considered.

**Source concerns**

- S5 is a recent whitepaper and the supplied excerpt describes its framework but does not provide detailed results for the specific optimization and machine-learning cases.
- S2 is a journalistic industry article rather than a primary experimental or systematic benchmarking source.
- The supplied evidence does not report quantitative performance comparisons, independent replication, or detailed classical resource and cost accounting.
- The source dates and future-dated publication metadata warrant verification before relying on them as established evidence.

**Counter-search status:** EXECUTED

**Counter-search query:**

> Find primary studies or independent benchmarks reporting quantum optimization or quantum machine-learning performance that matches or exceeds state-of-the-art classical solvers on practically relevant instances, and studies testing whether limited connectivity, qubit counts, and hardware errors are actually decisive barriers rather than mitigable implementation issues.

**Counter-search evidence:** S6, S7, S8, S9, S10

---

## 6. Research Decision

**Decision:** Continue researching.

**Origin:** VERIFIER_COUNTERSEARCH

**Target:** CLAIM C3

**Why**

Independent verification of C3 identified a high-value falsification search: The supplied sources support the broad comparison: optimization and machine-learning applications are described as more uncertain than molecular or quantum simulation, with strong classical methods and current hardware limitations constraining results. However, the evidence is largely narrative and does not establish a systematic, field-wide comparison or show that each listed barrier is the primary cause of weaker evidence. The claim should be framed as an assessment of current industrial evaluations rather than a definitive ranking of all applications.

**Next Search**

> Find primary studies or independent benchmarks reporting quantum optimization or quantum machine-learning performance that matches or exceeds state-of-the-art classical solvers on practically relevant instances, and studies testing whether limited connectivity, qubit counts, and hardware errors are actually decisive barriers rather than mitigable implementation issues.


---

# Iteration 2

## 1. Search

**Query**

> Find primary studies or independent benchmarks reporting quantum optimization or quantum machine-learning performance that matches or exceeds state-of-the-art classical solvers on practically relevant instances, and studies testing whether limited connectivity, qubit counts, and hardware errors are actually decisive barriers rather than mitigable implementation issues.

**Target:** C3

**Purpose:** COUNTERSEARCH

**Why this query**

Independent verification of C3 identified a high-value falsification search: The supplied sources support the broad comparison: optimization and machine-learning applications are described as more uncertain than molecular or quantum simulation, with strong classical methods and current hardware limitations constraining results. However, the evidence is largely narrative and does not establish a systematic, field-wide comparison or show that each listed barrier is the primary cause of weaker evidence. The claim should be framed as an assessment of current industrial evaluations rather than a definitive ranking of all applications.

5 result(s) retrieved; 5 new unique source(s) added.

- **S6 — The Quantum Optimization Benchmarking Library**
  URL: https://www.nature.com/articles/s43588-026-00991-1
- **S7 — Setting the Benchmark: Independent Study Ranks Quantinuum #1 in Performance**
  URL: https://www.quantinuum.com/blog/setting-the-benchmark-independent-study-ranks-quantinuum-1-in-performance
- **S8 — Quantum benchmarking**
  URL: https://www.ionq.com/quantum-benchmarks
- **S9 — SoK: Benchmarking the Performance of a Quantum Computer**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC9601621
- **S10 — Scaling from Hundreds to Millions of Qubits - arXiv**
  URL: https://arxiv.org/html/2411.10406v2

**Search Duration:** 3.37s

---

## 2. Evidence Processing

- New claim proposals: 3
- Existing claim updates: 5
- New gaps: 2
- Resolved gaps: 0

**Processing Duration:** 18.92s

---

## 3. Ledger Updates

### New Claim C7

**Claim**

Utility-scale quantum computing is currently described as requiring integration with heterogeneous classical high-performance-computing infrastructure and a full-stack hybrid quantum–classical architecture, rather than replacement of general-purpose classical processors.

- S10 supports (direct): States that quantum computers are better understood as specialized accelerators or coprocessors, that hybrid quantum–classical frameworks will be crucial, and that utility-scale systems require integration with heterogeneous HPC infrastructure and a hybrid full stack.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C8

**Claim**

System-level application benchmarks should include the complete quantum workflow—including compilation, execution, error mitigation or correction, classical post-processing, solution quality, and time-to-solution—because component metrics such as qubit count or gate fidelity alone do not establish useful advantage.

- S8 supports (direct): Specifies full-stack evaluation and says that time-to-solution includes job submission, compilation, quantum execution, error mitigation, and classical co-processing; it also requires predefined quality thresholds.
- S9 supports (direct): Reviews physical, aggregative, and application-level benchmarking and warns that qubit count alone is a misleading performance measure.
- S6 supports (direct): Introduces standardized, reproducible problem instances and metrics, with state-of-the-art classical solver baselines, to enable fair comparison across algorithms and hardware platforms.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C9

**Claim**

The new sources do not demonstrate a quantum optimization advantage over state-of-the-art classical solvers; instead, they establish benchmarking frameworks and report vendor-selected performance comparisons or hardware rankings.

- S6 supports (direct): Describes a library intended to drive the field toward quantum advantage and says that fair systematic benchmarking is a prerequisite, indicating that the advantage remains a target rather than an established result in this material.
- S7 supports (direct): Reports an independent QPU comparison in which Quantinuum systems performed best on QAOA, but the supplied text does not report superiority over classical solvers or commercial cost-effectiveness.
- S8 supports (direct): Presents IonQ-versus-peer benchmark results and a benchmark methodology, but the supplied material does not establish that the quantum systems outperform the best relevant classical alternatives on end-to-end cost or time.

**Confidence:** HIGH

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

The supplied sources do not establish a commercially useful quantum advantage that has already displaced or outperformed state-of-the-art classical methods in a real industrial deployment.

- S6 supports (direct): Frames optimization benchmarking as progress toward demonstrating quantum advantage and identifies fair comparison with state-of-the-art classical solvers as a prerequisite, not as an already established commercial result.
- S7 supports (direct): Reports Quantinuum leading other QPUs on QAOA, but does not establish displacement of classical methods or industrial commercial advantage.
- S8 supports (indirect): Reports quantum-system benchmark outcomes against peer quantum systems, while the supplied material does not show an end-to-end advantage over classical alternatives.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C3

**Claim**

Optimization and machine-learning applications currently have weaker and more uncertain evidence of quantum advantage than quantum simulation, because industrial evaluations must contend with strong classical solvers, limited connectivity, low qubit counts, and hardware errors.

- S6 supports (direct): Selects optimization instances that are challenging for state-of-the-art classical solvers, supplies baseline results, and explicitly positions the library as a framework for tracking progress toward quantum advantage rather than evidence that advantage has already been achieved.
- S7 supports (direct): Shows that QPU performance varies materially by architecture and connectivity in QAOA benchmarking, reinforcing the importance of hardware-specific limitations in optimization applications.
- S8 supports (direct): States that application-level optimization benchmarks must account for quality, time-to-solution, compilation, error handling, and classical co-processing, all of which can weaken practical quantum advantage.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

A quantum advantage benchmark is not by itself equivalent to commercial usefulness: practical assessment must compare the quantum system with a comparably priced classical alternative while accounting for runtime, solution quality, scalability, and deployment costs.

- S6 supports (direct): Calls for fair, reproducible comparisons using fixed problem instances, standardized metrics, and state-of-the-art classical solver baselines across varying hardware platforms.
- S8 supports (direct): Defines time-to-solution, energy-to-solution, and cost-to-solution using verified quality thresholds and includes compilation and classical co-processing in end-to-end timing.
- S9 supports (direct): Classifies benchmarking approaches and emphasizes that qubit count alone is misleading, supporting application-level and system-level comparison.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

The principal technical barriers identified in the supplied sources are error correction and fault tolerance, physical error and decoherence rates, scaling to sufficient logical-qubit counts, connectivity, and reliable control; these barriers currently restrict useful computations to small or shallow workloads.

- S10 supports (direct): Identifies unresolved hardware, fabrication, software-architecture, algorithmic, control, communication, memory-access, data-movement, and information-extraction challenges; it further states that fault-tolerant computation requires much lower logical error rates and substantial physical-resource overhead.
- S8 supports (direct): Notes that error correction increases physical-qubit requirements and circuit depth, and that full-stack performance depends on compiler, runtime, mitigation, correction, and optimization layers.
- S9 supports (indirect): Shows that benchmarking must span physical and application-level metrics, indicating that hardware specifications alone do not capture useful computational capability.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

The strongest projected near- or medium-term application area identified in the supplied sources is quantum simulation for chemistry, materials science, and drug discovery; however, the projection depends on substantially larger and more reliable fault-tolerant systems.

- S10 supports (direct): Identifies efficient quantum simulation and learning quantum data from physical systems as promising applications, and reports resource and sensitivity analysis for classically hard quantum-chemistry calculations under surface-code error correction.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### New Gap G6

The new vendor benchmark claims report superior performance among quantum platforms or against selected peer systems, but the supplied evidence does not independently establish the best classical baseline, full economic cost, statistical reproducibility, or commercial superiority for those workloads.

### New Gap G7

The supplied review identifies many full-stack scaling issues—including fabrication quality, control electronics, communication bandwidth, memory access, data movement, information extraction, and integration with classical HPC—but does not quantitatively rank their contribution to the path toward utility-scale systems.

---

## 4. Current Research State

- Claims: 9
- Supported: 9
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 7
- Remaining Searches: 1

### Subquestion Progress

**SQ1:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ3:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ4:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ5:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → PARTIAL (targeted searches: 0)
- SQ3 → PARTIAL (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- SQ5 → PARTIAL (targeted searches: 0)

**Remaining targeted searches:** 1

---

## 5. Independent Verification

### V2 — Claim C3

**Phase:** POST_COUNTERSEARCH

**Evidence source IDs:** S5, S2, S6, S7, S8

**Verdict:** VERIFIED

**Reason**

The supplied evidence supports the comparative assessment: industrial optimization and machine-learning applications are described as uncertain or longer-term prospects, while molecular simulation is presented as the more credible application area. The cited barriers—strong classical solvers, limited connectivity, low qubit counts, and hardware errors—are explicitly identified in the evidence.

**Missing assumptions**

- The comparison with quantum simulation is qualitative rather than based on a common quantitative evidence metric.
- The claim concerns current evidence and industrial relevance, not a proof that simulation will ultimately outperform optimization or machine learning.
- 'Quantum simulation' should be understood primarily as quantum chemistry or materials simulation, rather than every simulation workload.

**Source concerns**

- Several sources are industry or trade publications and may contain promotional framing, particularly the vendor benchmark material.
- The evidence does not provide a systematic, independently corroborated survey quantifying the relative strength of evidence across application areas.
- Some supplied sources are dated 2026, so their applicability depends on the report's time frame.

**Counter-search status:** NOT_REQUESTED

**Reconciliation**

Confidence: HIGH → MEDIUM

Status: SUPPORTED → SUPPORTED

---

## 6. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ1

**Why**

A final targeted search could materially improve the answer by filling the highest-priority gap: a rigorous account of leading experimental quantum-advantage demonstrations, including independent verification, best classical baselines, reproducibility, and practical resource cost. This is necessary to distinguish genuine benchmark advantage from commercially useful advantage.

**Next Search**

> Primary studies and independent analyses of quantum computational advantage demonstrations (Google Sycamore random-circuit sampling, USTC Jiuzhang/Zuchongzhi, photonic boson sampling): task, strongest classical simulation baseline, verification and reproducibility, resource/runtime/energy cost, and whether the result is practically useful.


---

# Iteration 3

## 1. Search

**Query**

> Primary studies and independent analyses of quantum computational advantage demonstrations (Google Sycamore random-circuit sampling, USTC Jiuzhang/Zuchongzhi, photonic boson sampling): task, strongest classical simulation baseline, verification and reproducibility, resource/runtime/energy cost, and whether the result is practically useful.

**Target:** SQ1

**Purpose:** SUBQUESTION

**Why this query**

A final targeted search could materially improve the answer by filling the highest-priority gap: a rigorous account of leading experimental quantum-advantage demonstrations, including independent verification, best classical baselines, reproducibility, and practical resource cost. This is necessary to distinguish genuine benchmark advantage from commercially useful advantage.

5 result(s) retrieved; 5 new unique source(s) added.

- **S11 — Quantum Supremacy: Complete 2026 Guide To The Milestone**
  URL: https://quantumzeitgeist.com/what-is-quantum-supremacy
- **S12 — Quantum computational advantage via 60-qubit 24-cycle random circuit sampling**
  URL: https://inspirehep.net/literature/2728130
- **S13 — A brief history of quantum vs classical computational advantage**
  URL: https://arxiv.org/html/2412.14703v1
- **S14 — Quantum supremacy**
  URL: https://en.wikipedia.org/wiki/Quantum_supremacy
- **S15 — China’s Jiuzhang Achieves Photonic Quantum Advantage**
  URL: https://postquantum.com/industry-news/china-jiuzhang-quantum

**Search Duration:** 3.61s

---

## 2. Evidence Processing

- New claim proposals: 3
- Existing claim updates: 3
- New gaps: 2
- Resolved gaps: 0

**Processing Duration:** 15.73s

---

## 3. Ledger Updates

### New Claim C10

**Claim**

Experimental quantum-advantage demonstrations in the supplied sources are concentrated on specialized sampling tasks—random circuit sampling and Gaussian boson sampling—rather than useful commercial computations; their classical-superiority claims remain provisional because later work has refuted or challenged several headline results.

- S13 supports (direct): Reviews the experimental record and lists Google Sycamore as refuted, the Jiuzhang experiments as weakly refuted, and the Zuchongzhi experiments as challenged. It also distinguishes computational advantage from practical utility.
- S11 supports (direct): Explains that supremacy benchmarks are generally contrived, noncommercial tasks and that classical algorithms can narrow or erase claimed gaps over time.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C11

**Claim**

The Zuchongzhi 2.1 experiment reported a 60-qubit, 24-cycle random-circuit-sampling result, estimating approximately 4.8×10^4 years for classical simulation versus about 4.2 hours on the quantum system; the supplied review nevertheless records the Zuchongzhi results as challenged.

- S12 supports (direct): Reports 60 qubits and 24 cycles, an XEB fidelity of (3.66 ± 0.345)×10^-4, and the stated classical-versus-quantum time estimates.
- S13 supports (direct): Lists the September 2021 Zuchongzhi random-circuit-sampling experiment as challenged by subsequent work.
- S13 contradicts (direct): Its status table characterizes the Zuchongzhi experiment as challenged, limiting the strength of the original claimed classical gap as an uncontested demonstration.

**Confidence:** MEDIUM

**Status:** CONFLICTING

### New Claim C12

**Claim**

Theoretical quantum speedups do not automatically survive physical implementation: error-correction overhead can eliminate an algorithmic speedup, making fault-tolerant error correction a central requirement for experimentally realizing advantages such as Shor's algorithm.

- S13 supports (direct): States that some theoretically advantageous quantum algorithms can lose their speedup because of error-correction overhead and identifies error correction as the frontier for experimentally demonstrating advantage in Shor's algorithm.

**Confidence:** HIGH

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

The supplied sources do not establish a commercially useful quantum advantage that has already displaced or outperformed state-of-the-art classical methods in a real industrial deployment.

- S13 supports (direct): The review catalogs claimed advantage experiments but reports refutations or challenges for major sampling demonstrations and does not identify a useful commercial computation that displaced classical methods.
- S11 supports (direct): States that supremacy is a benchmark rather than a product and that useful, error-corrected advantage had not been achieved in the described period.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

Major remaining barriers include quantum error correction and fault-tolerant operation, sufficiently low physical error and decoherence rates, scaling to enough high-quality logical qubits, connectivity, and reliable control. The supplied sources also emphasize fabrication, software and algorithm maturity, data movement and input/output overhead, verification, classical integration, and system economics. Together, these constraints mean that reliable, commercially relevant workloads remain limited, although small demonstrations and hybrid experiments are feasible.

- S13 supports (direct): Links the realization of theoretically advantageous algorithms to fault-tolerant error correction and notes that error-correction overhead can remove the theoretical speedup.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C8

**Claim**

System-level application benchmarks should include the complete quantum workflow—including compilation, execution, error mitigation or correction, classical post-processing, solution quality, and time-to-solution—because component metrics such as qubit count or gate fidelity alone do not establish useful advantage.

- S13 supports (direct): Shows that advantage status changes as classical algorithms improve, reinforcing the need for current, best-classical-baseline comparisons rather than treating a historical benchmark as permanent.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### New Gap G8

The supplied evidence does not determine whether the challenged or weakly refuted sampling demonstrations remain classically infeasible under the latest independently verified algorithms and hardware, nor whether any such result has reproducibly transferred to a useful workload.

### New Gap G9

The sources discuss theoretical advantages and error-correction overhead qualitatively but do not provide application-specific quantitative thresholds showing when the overhead preserves or destroys the projected speedup for commercially relevant workloads.

---

## 4. Current Research State

- Claims: 12
- Supported: 10
- Weak: 1
- Conflicting: 1
- Insufficient Evidence: 0
- Open Gaps: 9
- Remaining Searches: 0

### Subquestion Progress

**SQ1:** PARTIAL → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ2:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ3:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ4:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ5:** PARTIAL → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

### Research Plan Status

**CORE:**

- SQ1 → CONFLICTING (targeted searches: 1)
- SQ2 → PARTIAL (targeted searches: 0)
- SQ3 → PARTIAL (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- SQ5 → CONFLICTING (targeted searches: 0)

**Remaining targeted searches:** 0

---

## 5. Independent Verification

### V3 — Claim C5

**Phase:** INITIAL

**Evidence source IDs:** S1, S2, S5, S10, S8, S9, S13

**Verdict:** NEEDS_QUALIFICATION

**Reason**

The supplied evidence supports error correction/fault tolerance, physical errors and decoherence, scaling, connectivity, and control as major barriers, and indicates that current demonstrations are generally small, noisy, or shallow. However, calling these the principal barriers is somewhat overbroad because the sources also identify fabrication, software and algorithm maturity, data movement/input-output, verification, integration, and system cost as important constraints. The phrase “useful computations” should also be limited to broad commercial or application-level usefulness, not all useful quantum workloads.

**Missing assumptions**

- The statement concerns application-level or commercially useful workloads rather than proof-of-principle demonstrations.
- “Small or shallow” refers to the scale and depth of reliable, application-relevant computations, not every computation currently executable on quantum hardware.
- The listed barriers are representative major barriers, not an exhaustive ranking.

**Source concerns**

- S1 and S2 are future-dated, industry-oriented articles and include promotional or vendor-linked claims.
- S8 is a vendor-produced benchmarking source and may not provide independent evidence of overall field performance.
- The strongest general support comes from S10 and S13, but the supplied excerpts do not fully substantiate a precise prioritization among all barriers.

**Counter-search status:** NOT_REQUESTED

**Reconciliation**

Claim:

"The principal technical barriers identified in the supplied sources are error correction and fault tolerance, physical error and decoherence rates, scaling to sufficient logical-qubit counts, connectivity, and reliable control; these barriers currently restrict useful computations to small or shallow workloads."
→
"Major remaining barriers include quantum error correction and fault-tolerant operation, sufficiently low physical error and decoherence rates, scaling to enough high-quality logical qubits, connectivity, and reliable control. The supplied sources also emphasize fabrication, software and algorithm maturity, data movement and input/output overhead, verification, classical integration, and system economics. Together, these constraints mean that reliable, commercially relevant workloads remain limited, although small demonstrations and hybrid experiments are feasible."

Confidence: HIGH → HIGH

Status: SUPPORTED → WEAK

---

## 6. Research Decision

**Decision:** Stop researching.

**Origin:** BUDGET_STOP

**Why**

The maximum research iteration budget was reached.

**Stop Reason:** max_iterations


---

# Final Research Decision

**Research did not complete.**

**Failure Stage:** OpenAI Ledger Report Generation

**Remaining Uncertainty**

- No supplied source provides a rigorous, independently verified account of a leading experimental quantum-advantage demonstration, including the task, best classical baseline, reproducibility, verification, and total resource cost.
- The evidence does not establish quantitative fault-tolerant resource requirements—such as physical-to-logical qubit overhead, target error rates, circuit depth, or runtime—for any commercially relevant application.
- The sources provide projections such as a 5–10 year molecular-simulation horizon and wider commercial timelines, but no independent, systematically justified forecast with explicit hardware, algorithm, and classical-competitor assumptions.
- The evidence does not quantify the economics of quantum systems versus classical alternatives, including acquisition or cloud cost, energy, throughput, reliability, data-loading overhead, and end-to-end application cost.
- The supplied material does not rank the remaining barriers quantitatively or demonstrate that proposed error-correction progress is reproducible across platforms and sufficient for useful workloads.
- The new vendor benchmark claims report superior performance among quantum platforms or against selected peer systems, but the supplied evidence does not independently establish the best classical baseline, full economic cost, statistical reproducibility, or commercial superiority for those workloads.
- The supplied review identifies many full-stack scaling issues—including fabrication quality, control electronics, communication bandwidth, memory access, data movement, information extraction, and integration with classical HPC—but does not quantitatively rank their contribution to the path toward utility-scale systems.
- The supplied evidence does not determine whether the challenged or weakly refuted sampling demonstrations remain classically infeasible under the latest independently verified algorithms and hardware, nor whether any such result has reproducibly transferred to a useful workload.
- The sources discuss theoretical advantages and error-correction overhead qualitatively but do not provide application-specific quantitative thresholds showing when the overhead preserves or destroys the projected speedup for commercially relevant workloads.
- SQ1: What quantum-computing demonstrations have established a quantum advantage over classical computers, and how strong is the evidence that the advantage is genuine, reproducible, and relevant to useful computation? (CONFLICTING: At least one linked ledger claim contains conflicting evidence.)
- SQ2: What theoretical or projected quantum advantages are expected for commercially relevant applications, and under what assumptions about algorithms, fault tolerance, hardware scale, error rates, and classical competitors? (PARTIAL: At least one linked ledger claim is not yet supported.)
- SQ3: What commercially useful quantum advantages, if any, are available today or plausibly achievable in the near, medium, and longer term, relative to classical alternatives? (PARTIAL: At least one linked ledger claim is not yet supported.)
- SQ4: What are the biggest remaining technical barriers to commercially useful quantum advantage, and how do they constrain the path from current demonstrations to useful systems? (PARTIAL: At least one linked ledger claim is not yet supported.)
- SQ5: How should claims of quantum advantage be compared fairly with state-of-the-art classical computing, and what uncertainty remains in judging how close quantum computers are to commercial usefulness? (CONFLICTING: At least one linked ledger claim contains conflicting evidence.)

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Question Decomposition | 1 | 8.20s |
| Tavily Search | 3 | 9.63s |
| Evidence Processing | 3 | 52.36s |
| Independent Verification | 3 | 19.31s |
| Research Decision | 1 | 3.15s |
| Report Generation | 1 | 0.00s |
| Total Run | — | 112.76s |

# Verifier Diagnostics

- Verification calls: 3
- Claims verified: 2
- VERIFIED verdicts: 1
- NEEDS_QUALIFICATION verdicts: 2
- CONTRADICTED verdicts: 0
- INSUFFICIENT_EVIDENCE verdicts: 0
- Counter-searches requested: 1
- Counter-searches executed: 1
- Counter-searches blocked by budget: 0
- Counter-searches blocked as duplicates: 0
- Claims whose wording changed: 1
- Claims whose confidence decreased: 1
- Claims whose status changed: 1
- Searches allocated to general research: 1
- Searches allocated to subquestions: 1
- Searches allocated to counter-search: 1
