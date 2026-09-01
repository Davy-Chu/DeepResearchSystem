# Research Report

## Research Question

How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

## Summary

This is an automatically generated incomplete report. The research run ended with stop reason `max_iterations`, and normal finalization did not complete during OpenAI Ledger Report Generation. The validated findings collected before that point are preserved below without claiming that the evidence is complete.

## Findings

### Finding 1

**Claim**

The supplied sources do not establish a commercially useful quantum advantage that has already displaced or outperformed state-of-the-art classical methods in a real industrial deployment.

**Confidence:** High

**Why this confidence level**

The historical review adds direct evidence that headline experimental claims are specialized and contested, reinforcing rather than weakening the conclusion that no commercially useful deployment advantage is established in the supplied material.

**Evidence**

- States that demonstrations have simulated only small molecules and have not reached systems complex enough to displace classical methods; it also says current hardware lacks the required error rates and qubit counts for useful molecular simulation. [S2]
- Describes industrial optimization and machine-learning experiments as evaluations against classical solvers, with verdicts ranging from promise to significant hurdles, rather than reporting an established commercial advantage. [S5]
- Frames optimization benchmarking as progress toward demonstrating quantum advantage and identifies fair comparison with state-of-the-art classical solvers as a prerequisite, not as an already established commercial result. [S6]
- Reports Quantinuum leading other QPUs on QAOA, but does not establish displacement of classical methods or industrial commercial advantage. [S7]
- Reports quantum-system benchmark outcomes against peer quantum systems, while the supplied material does not show an end-to-end advantage over classical alternatives. [S8]
- The review catalogs claimed advantage experiments but reports refutations or challenges for major sampling demonstrations and does not identify a useful commercial computation that displaced classical methods. [S13]
- States that supremacy is a benchmark rather than a product and that useful, error-corrected advantage had not been achieved in the described period. [S11]

### Finding 2

**Claim**

The strongest projected near- or medium-term application area identified in the supplied sources is quantum simulation for chemistry, materials science, and drug discovery; however, the projection depends on substantially larger and more reliable fault-tolerant systems.

**Confidence:** Medium

**Why this confidence level**

The source independently reinforces simulation as a promising application and explicitly conditions projected performance on error correction, hardware specifications, and algorithmic improvements, but supplies no demonstrated commercial result or definitive timeline.

**Evidence**

- Identifies molecular simulation in drug discovery, materials science, and chemistry as the most viable near-term application area, while noting that current systems are too small and noisy. It cites a commonly stated 5–10 year timeline contingent on hundreds of error-corrected logical qubits. [S2]
- Lists matter simulation and drug discovery among areas where quantum algorithms could potentially provide speedups, while emphasizing that usefulness depends on the particular problem and comparison with classical systems. [S3]
- Identifies efficient quantum simulation and learning quantum data from physical systems as promising applications, and reports resource and sensitivity analysis for classically hard quantum-chemistry calculations under surface-code error correction. [S10]

### Finding 3

**Claim**

Optimization and machine-learning applications currently have weaker and more uncertain evidence of quantum advantage than quantum simulation, because industrial evaluations must contend with strong classical solvers, limited connectivity, low qubit counts, and hardware errors.

**Confidence:** Medium

**Why this confidence level**

Independent verification: The supplied evidence supports the comparative assessment: industrial optimization and machine-learning applications are described as uncertain or longer-term prospects, while molecular simulation is presented as the more credible application area. The cited barriers—strong classical solvers, limited connectivity, low qubit counts, and hardware errors—are explicitly identified in the evidence.

**Evidence**

- Reports benchmarking hybrid algorithms against classical solvers for logistics, production, optimization, and machine learning, and explicitly identifies low qubit counts, limited connectivity, and error susceptibility as limitations. Its evaluation framework includes scalability, solution quality, runtime, and transferability. [S5]
- States that optimization has highly tuned classical algorithms and that quantum approaches have not demonstrated the ability to beat them; it characterizes optimization, AI, and climate modeling as longer-term or uncertain areas. [S2]
- Selects optimization instances that are challenging for state-of-the-art classical solvers, supplies baseline results, and explicitly positions the library as a framework for tracking progress toward quantum advantage rather than evidence that advantage has already been achieved. [S6]
- Shows that QPU performance varies materially by architecture and connectivity in QAOA benchmarking, reinforcing the importance of hardware-specific limitations in optimization applications. [S7]
- States that application-level optimization benchmarks must account for quality, time-to-solution, compilation, error handling, and classical co-processing, all of which can weaken practical quantum advantage. [S8]

### Finding 4

**Claim**

A quantum advantage benchmark is not by itself equivalent to commercial usefulness: practical assessment must compare the quantum system with a comparably priced classical alternative while accounting for runtime, solution quality, scalability, and deployment costs.

**Confidence:** High

**Why this confidence level**

The new sources substantially strengthen the requirement for fair, end-to-end, reproducible, economically relevant comparison.

**Evidence**

- Introduces 'quantum economic advantage' as solving a problem faster with a quantum computer than with a comparably priced classical computer, and explains that slower quantum processing can offset algorithmic efficiency. [S3]
- Uses model formulation, scalability, solution quality, runtime, and transferability as common evaluation criteria for industrial quantum applications and stresses benchmarking against classical solvers. [S5]
- Calls for fair, reproducible comparisons using fixed problem instances, standardized metrics, and state-of-the-art classical solver baselines across varying hardware platforms. [S6]
- Defines time-to-solution, energy-to-solution, and cost-to-solution using verified quality thresholds and includes compilation and classical co-processing in end-to-end timing. [S8]
- Classifies benchmarking approaches and emphasizes that qubit count alone is misleading, supporting application-level and system-level comparison. [S9]

### Finding 5

**Claim**

Major remaining barriers include quantum error correction and fault-tolerant operation, sufficiently low physical error and decoherence rates, scaling to enough high-quality logical qubits, connectivity, and reliable control. The supplied sources also emphasize fabrication, software and algorithm maturity, data movement and input/output overhead, verification, classical integration, and system economics. Together, these constraints mean that reliable, commercially relevant workloads remain limited, although small demonstrations and hybrid experiments are feasible.

**Confidence:** High

**Why this confidence level**

Independent verification: The supplied evidence supports error correction/fault tolerance, physical errors and decoherence, scaling, connectivity, and control as major barriers, and indicates that current demonstrations are generally small, noisy, or shallow. However, calling these the principal barriers is somewhat overbroad because the sources also identify fabrication, software and algorithm maturity, data movement/input-output, verification, integration, and system cost as important constraints. The phrase “useful computations” should also be limited to broad commercial or application-level usefulness, not all useful quantum workloads.

**Evidence**

- Characterizes pre-2026 systems as noisy and error-prone, with decoherence and gate errors limiting reliable computation, and presents error correction, scaling, and fault tolerance as central engineering challenges. [S1]
- Says current hardware has error rates and qubit counts insufficient for practically useful molecular simulation. [S2]
- Explicitly identifies low qubit counts, limited connectivity, and error susceptibility as hardware limitations affecting industrial hybrid algorithms. [S5]
- Identifies unresolved hardware, fabrication, software-architecture, algorithmic, control, communication, memory-access, data-movement, and information-extraction challenges; it further states that fault-tolerant computation requires much lower logical error rates and substantial physical-resource overhead. [S10]
- Notes that error correction increases physical-qubit requirements and circuit depth, and that full-stack performance depends on compiler, runtime, mitigation, correction, and optimization layers. [S8]
- Shows that benchmarking must span physical and application-level metrics, indicating that hardware specifications alone do not capture useful computational capability. [S9]
- Links the realization of theoretically advantageous algorithms to fault-tolerant error correction and notes that error-correction overhead can remove the theoretical speedup. [S13]

### Finding 6

**Claim**

Most ordinary small- to moderate-sized business problems are not expected to benefit from quantum computing, whereas potential benefits are concentrated in problems with suitable structure and very large scale, particularly where an exponential algorithmic improvement could outweigh quantum hardware's lower processing speed.

**Confidence:** Medium

**Why this confidence level**

The sources agree on workload selectivity, but the claim about exponential gains is a general characterization within the supplied articles rather than evidence of a realized commercial speedup.

**Evidence**

- Reports the MIT framework's conclusion that small to moderate-sized problems generally will not benefit, while some very large problems with exponential algorithmic gains may; it also notes that quantum processors can be slower than classical computers. [S3]
- States that most classical workloads are not good quantum-computing fits and that suitable candidates tend to involve quantum systems or exceptionally large solution spaces. [S2]

### Finding 7

**Claim**

Utility-scale quantum computing is currently described as requiring integration with heterogeneous classical high-performance-computing infrastructure and a full-stack hybrid quantum–classical architecture, rather than replacement of general-purpose classical processors.

**Confidence:** Medium

**Why this confidence level**

The source directly presents this architectural view, but it is a review and describes a proposed path rather than a demonstrated commercial deployment.

**Evidence**

- States that quantum computers are better understood as specialized accelerators or coprocessors, that hybrid quantum–classical frameworks will be crucial, and that utility-scale systems require integration with heterogeneous HPC infrastructure and a hybrid full stack. [S10]

### Finding 8

**Claim**

System-level application benchmarks should include the complete quantum workflow—including compilation, execution, error mitigation or correction, classical post-processing, solution quality, and time-to-solution—because component metrics such as qubit count or gate fidelity alone do not establish useful advantage.

**Confidence:** High

**Why this confidence level**

The review provides additional direct evidence that classical baselines and benchmark status are moving targets, strengthening the existing full-workflow and contemporary-baseline requirement.

**Evidence**

- Specifies full-stack evaluation and says that time-to-solution includes job submission, compilation, quantum execution, error mitigation, and classical co-processing; it also requires predefined quality thresholds. [S8]
- Reviews physical, aggregative, and application-level benchmarking and warns that qubit count alone is a misleading performance measure. [S9]
- Introduces standardized, reproducible problem instances and metrics, with state-of-the-art classical solver baselines, to enable fair comparison across algorithms and hardware platforms. [S6]
- Shows that advantage status changes as classical algorithms improve, reinforcing the need for current, best-classical-baseline comparisons rather than treating a historical benchmark as permanent. [S13]

### Finding 9

**Claim**

The new sources do not demonstrate a quantum optimization advantage over state-of-the-art classical solvers; instead, they establish benchmarking frameworks and report vendor-selected performance comparisons or hardware rankings.

**Confidence:** High

**Why this confidence level**

The sources provide performance and benchmarking evidence but no direct result showing quantum optimization beating state-of-the-art classical methods on a commercially relevant metric. This is consistent with the existing evidence that optimization advantage remains uncertain.

**Evidence**

- Describes a library intended to drive the field toward quantum advantage and says that fair systematic benchmarking is a prerequisite, indicating that the advantage remains a target rather than an established result in this material. [S6]
- Reports an independent QPU comparison in which Quantinuum systems performed best on QAOA, but the supplied text does not report superiority over classical solvers or commercial cost-effectiveness. [S7]
- Presents IonQ-versus-peer benchmark results and a benchmark methodology, but the supplied material does not establish that the quantum systems outperform the best relevant classical alternatives on end-to-end cost or time. [S8]

### Finding 10

**Claim**

Experimental quantum-advantage demonstrations in the supplied sources are concentrated on specialized sampling tasks—random circuit sampling and Gaussian boson sampling—rather than useful commercial computations; their classical-superiority claims remain provisional because later work has refuted or challenged several headline results.

**Confidence:** High

**Why this confidence level**

The review directly catalogs claimed demonstrations and their subsequent status, while the additional source explicitly distinguishes benchmark milestones from useful computation. The sources support the characterization of demonstrated advantage as specialized and contested, not commercially useful.

**Evidence**

- Reviews the experimental record and lists Google Sycamore as refuted, the Jiuzhang experiments as weakly refuted, and the Zuchongzhi experiments as challenged. It also distinguishes computational advantage from practical utility. [S13]
- Explains that supremacy benchmarks are generally contrived, noncommercial tasks and that classical algorithms can narrow or erase claimed gaps over time. [S11]

### Finding 11

**Claim**

The Zuchongzhi 2.1 experiment reported a 60-qubit, 24-cycle random-circuit-sampling result, estimating approximately 4.8×10^4 years for classical simulation versus about 4.2 hours on the quantum system; the supplied review nevertheless records the Zuchongzhi results as challenged.

**Confidence:** Medium

**Why this confidence level**

The numerical performance and comparison are directly reported by the experiment record, but the independent review documents challenges to the interpretation or classical baseline. The result is therefore a reported experimental claim, not settled evidence of an enduring advantage.

**Evidence**

- Reports 60 qubits and 24 cycles, an XEB fidelity of (3.66 ± 0.345)×10^-4, and the stated classical-versus-quantum time estimates. [S12]
- Lists the September 2021 Zuchongzhi random-circuit-sampling experiment as challenged by subsequent work. [S13]

### Finding 12

**Claim**

Theoretical quantum speedups do not automatically survive physical implementation: error-correction overhead can eliminate an algorithmic speedup, making fault-tolerant error correction a central requirement for experimentally realizing advantages such as Shor's algorithm.

**Confidence:** High

**Why this confidence level**

The review explicitly connects theoretical advantage, error-correction overhead, and experimental realization. It does not provide complete resource estimates, so it strengthens the qualitative barrier claim without resolving quantitative resource uncertainty.

**Evidence**

- States that some theoretically advantageous quantum algorithms can lose their speedup because of error-correction overhead and identifies error correction as the frontier for experimentally demonstrating advantage in Shor's algorithm. [S13]

## Conflicts and Uncertainty

- Evidence concerning ledger claim C2 is conflicting: The strongest projected near- or medium-term application area identified in the supplied sources is quantum simulation for chemistry, materials science, and drug discovery; however, the projection depends on substantially larger and more reliable fault-tolerant systems. [S2] [S3] [S10]
- Evidence concerning ledger claim C11 is conflicting: The Zuchongzhi 2.1 experiment reported a 60-qubit, 24-cycle random-circuit-sampling result, estimating approximately 4.8×10^4 years for classical simulation versus about 4.2 hours on the quantum system; the supplied review nevertheless records the Zuchongzhi results as challenged. [S12] [S13]

## Remaining Gaps

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

## Conclusion

The findings above reflect the evidence validated before the run ended. They should be treated as provisional because normal final synthesis did not complete and important gaps may remain.

## Sources

- [S1] 5 Key Quantum Computing Breakthroughs in 2026 — https://www.bqpsim.com/blogs/quantum-computing-breakthroughs
- [S2] 8 Industry Use Cases for Quantum Computing — https://thequantuminsider.com/2026/05/04/quantum-computing-use-cases-real-applications-industries
- [S3] Quantum computing: What leaders need to know now — https://mitsloan.mit.edu/ideas-made-to-matter/quantum-computing-what-leaders-need-to-know-now
- [S4] Quantum technology firms race to market as the industry sees ‘inflection point’ — https://www.cnbc.com/2026/03/30/quantum-computing-firms-go-public-breakthroughs-commercialization.html
- [S5] Quantum Computing – Strategic Recommendations for the ... — https://arxiv.org/html/2601.08578v1
- [S6] The Quantum Optimization Benchmarking Library — https://www.nature.com/articles/s43588-026-00991-1
- [S7] Setting the Benchmark: Independent Study Ranks Quantinuum #1 in Performance — https://www.quantinuum.com/blog/setting-the-benchmark-independent-study-ranks-quantinuum-1-in-performance
- [S8] Quantum benchmarking — https://www.ionq.com/quantum-benchmarks
- [S9] SoK: Benchmarking the Performance of a Quantum Computer — https://pmc.ncbi.nlm.nih.gov/articles/PMC9601621
- [S10] Scaling from Hundreds to Millions of Qubits - arXiv — https://arxiv.org/html/2411.10406v2
- [S11] Quantum Supremacy: Complete 2026 Guide To The Milestone — https://quantumzeitgeist.com/what-is-quantum-supremacy
- [S12] Quantum computational advantage via 60-qubit 24-cycle random circuit sampling — https://inspirehep.net/literature/2728130
- [S13] A brief history of quantum vs classical computational advantage — https://arxiv.org/html/2412.14703v1
- [S14] Quantum supremacy — https://en.wikipedia.org/wiki/Quantum_supremacy
- [S15] China’s Jiuzhang Achieves Photonic Quantum Advantage — https://postquantum.com/industry-news/china-jiuzhang-quantum
