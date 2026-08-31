# Research Report

## Research Question

How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

## Summary

This is an automatically generated incomplete report. The research run ended with stop reason `max_iterations`, and normal finalization did not complete during OpenAI Ledger Report Generation. The validated findings collected before that point are preserved below without claiming that the evidence is complete.

## Findings

### Finding 1

**Claim**

The supplied sources do not document a quantum-computing demonstration that delivered commercially useful superiority over a strong classical baseline; reported industrial demonstrations remain pilots, proof-of-concept studies, or projections.

**Confidence:** Medium

**Why this confidence level**

The new sources strengthen documentation that Q-CTRL claims a practical materials-simulation advantage, but S12 also identifies a competing classical method and unresolved scope, accuracy, and baseline questions. The evidence therefore continues to conflict with any categorical conclusion that commercially useful superiority has been established.

**Evidence**

- States that small-molecule simulations have been demonstrated but have not reached systems complex enough to displace classical methods, and that current hardware lacks the error rates and qubit counts for practically useful molecular simulation. [S2]
- Describes industrial optimization and machine-learning experiments benchmarked against classical solvers, while framing the work as an evaluation of promise and practical hurdles rather than reporting an established commercial advantage. [S4]
- Characterizes quantum computing as still experimental and reports practical advantage only as an expectation around 2028–2029, with wider commercial use in the 2030s. [S5]
- States that advantage remains workload-specific, that some demonstrations use specially designed problems with little practical use, and that end-to-end production metrics are often omitted. [S9]
- Provides a third-party analysis that initially reports a classical method narrowing the claimed 3,000-times advantage, then explains that the full multi-observable and accuracy comparison remains unresolved; this supports treating the result as a reported demonstration rather than established commercial superiority. [S12]
- Reproduces the vendor-reported 3,000-times speedup and commercial-relevance framing, but does not independently validate the result. [S13]
- Reports Q-CTRL's claimed 3,000-times speedup and later productization of the workflow, while presenting the result as a company demonstration rather than independent evidence of broad commercial advantage. [S14]

### Finding 2

**Claim**

Quantum molecular simulation, particularly for chemistry, materials, and drug-discovery problems, is presented as the most credible near- or medium-term application area, but useful deployment is projected to require substantially more capable, lower-error hardware and is not experimentally validated at commercially relevant scale in the supplied evidence.

**Confidence:** Medium

**Why this confidence level**

The sources add substantial detail and a reported accuracy metric for the Fermi–Hubbard demonstration, but the competing classical result and vendor-originated evidence prevent concluding that molecular simulation has validated commercial advantage broadly.

**Evidence**

- Explains that molecular systems map naturally onto quantum hardware, identifies chemistry and materials as credible application areas, and projects drug-discovery applications on a roughly 5–10 year horizon contingent on hundreds of error-corrected logical qubits. [S2]
- Reports a materials-engineering Fermionic Simulation demonstration and argues that chemistry and materials workloads are attractive because classical scaling is poor. [S6]
- Describes a 120-qubit Fermi–Hubbard simulation with reported 3,000-times wall-clock speedup against a TDVP classical benchmark and agreement within 1% RMSE. [S10]
- Characterizes the Fermi–Hubbard demonstration as technically substantial and among the largest and most accurate reported gate-based digital simulations, while preserving uncertainty about the breadth of the advantage. [S12]
- States that Q-CTRL's Fire Opal workflow applies the demonstrated dynamics-simulation techniques to materials science and energy problems, with reported agreement within 1% RMSE against high-resolution tensor-network simulations. [S14]

### Finding 3

**Claim**

Optimization and machine-learning applications have not established a general quantum advantage: strong classical algorithms remain important comparators, and the supplied industrial evaluation framework treats scalability, solution quality, runtime, and transferability as unresolved practical tests.

**Confidence:** High

**Why this confidence level**

The new comparison provides a concrete example of why optimization and simulation advantage claims require strong, current classical baselines and explicit workload definitions.

**Evidence**

- States that many optimization problems have highly tuned classical algorithms that quantum approaches have not demonstrated they can beat, and describes optimization as a use case where hype exceeds evidence. [S2]
- Reports that QCHALLenge benchmarks quantum approaches against classical solvers using model formulation, scalability, solution quality, runtime, and transferability, with outcomes ranging from a possible path to advantage to significant practical hurdles. [S4]
- Finds published annealing-QPU benchmark results ranging from negative to highly favorable and attributes much of the disagreement to benchmark design choices. [S7]
- Says advantage is limited and workload-specific, highlights moving classical baselines, and recommends end-to-end time-to-answer, solution quality, throughput, and stability metrics. [S9]
- Shows that a claimed advantage can change when a newer classical method is used and when the comparison changes from one observable to the complete set of outputs, reinforcing sensitivity to classical baselines and benchmark scope. [S12]

### Finding 4

**Claim**

The principal hardware barrier identified in the supplied sources is achieving sufficiently low error rates and scalable fault-tolerant computation; current limitations also include limited qubit counts, restricted connectivity, and error susceptibility.

**Confidence:** High

**Why this confidence level**

The additional sources independently reinforce that errors, error mitigation or correction, and system stability remain central barriers, even where software improvements may improve current-device performance.

**Evidence**

- Reports that pre-2026 NISQ systems had roughly 50–200 error-prone physical qubits, gate-error rates of 10^-3 to 10^-2, and decoherence that restricted reliable computation to shallow circuits; it presents later error-correction progress as a claimed engineering milestone. [S1]
- States that current hardware lacks the error rates and qubit counts required for useful molecular simulation. [S2]
- Identifies low qubit counts, limited connectivity, and error susceptibility as hardware limitations affecting hybrid industrial algorithms. [S4]
- States that noise and errors have historically prevented useful results on relevant problems and presents compiler and error-suppression infrastructure as necessary to reach larger useful calculations. [S6]
- Identifies error correction, hardware and software maturity, and stability or recalibration requirements as practical obstacles to production use. [S9]

### Finding 5

**Claim**

Commercial usefulness should be evaluated as quantum economic advantage—better performance than a comparably priced classical computer—rather than as quantum advantage alone; relevant comparisons include runtime, cost, scale, solution quality, and operational overhead.

**Confidence:** High

**Why this confidence level**

The new evidence reinforces that commercial usefulness requires explicit specification of the workload, output scope, classical method, accuracy, and end-to-end metric rather than relying on a headline speedup.

**Evidence**

- Defines quantum economic advantage as solving a problem faster with a quantum computer than with a comparably priced classical computer, and warns that classical computers may remain faster despite a quantum algorithm using fewer steps. [S3]
- Uses scalability, solution quality, runtime, and transferability as evaluation criteria for industrial use cases and emphasizes benchmarking against classical solvers. [S4]
- Defines practical quantum advantage as outperforming the best available conventional alternative on a real-world problem in a way that is better, faster, or more affordable. [S6]
- Recommends production-oriented comparisons based on end-to-end time-to-answer, solution quality, throughput, and stability rather than headline benchmark results. [S9]
- Shows that commercial comparison depends on what outputs are counted: the quantum processor produces many observables simultaneously, while a competing classical method computes them separately; it also raises accuracy and baseline-selection issues. [S12]
- States that the comparison used wall-clock execution time and comparable accuracy against a TDVP solver, while noting that future classical algorithms or GPU-accelerated tensor networks could change the comparison. [S10]

### Finding 6

**Claim**

Q-CTRL reports a 2026 demonstration in which an IBM quantum computer, combined with compiler and error-suppression software, solved a Fermionic Simulation materials problem more than 3,000 times faster in wall-clock time than a stated industry-standard classical alternative while meeting or exceeding its accuracy; the supplied source is a vendor report and does not independently establish the result's reproducibility, end-to-end cost advantage, or generality.

**Confidence:** Medium

**Why this confidence level**

Multiple sources corroborate what Q-CTRL reports, and S10 supplies additional technical details, but they largely repeat or relay the vendor claim. S12 introduces a materially relevant competing baseline and unresolved observable-scope issue, so the result is better characterized as a substantial reported benchmark than independently established commercial advantage.

**Evidence**

- Q-CTRL claims a publicly available IBM quantum computer plus infrastructure software achieved a 3,000-times wall-clock speedup on a known-value, commercially relevant materials-simulation problem with practically relevant runtime and comparable or better accuracy. [S6]
- Independent reporting describes the 120-qubit Fermi–Hubbard simulation, approximately two-minute quantum execution, over-100-hour TDVP comparison, and agreement within 1% RMSE. [S10]
- Q-CTRL reports a 3,000-times speedup over performance-optimized industry-standard classical software on a known materials-science problem, with accuracy meeting stated expectations. [S11]
- Repeats the reported 3,000-times comparison and the use of Q-CTRL error-suppression software on a 120-qubit simulation. [S13]
- Reports the demonstration's 1% RMSE comparison and says the associated Fire Opal workflow has been made available to users. [S14]

### Finding 7

**Claim**

Empirical claims of quantum advantage for quantum annealing are highly sensitive to benchmark design, including whether scaling or runtime is measured, whether anneal time or access time is counted, the solution-quality metric, hardware topology, and whether the classical solver addresses the physical or logically embedded problem.

**Confidence:** Medium

**Why this confidence level**

The source directly describes the review's conclusion, but it is a conference presentation by a D-Wave-affiliated researcher and the supplied material does not provide the underlying paper or quantitative synthesis.

**Evidence**

- A D-Wave literature review of roughly a decade of annealing-QPU studies reports conflicting outcomes and identifies experimental-design features that predict the observed result, including metrics, timing scope, topology, and problem-domain choice. [S7]

### Finding 8

**Claim**

A third-party report describes a classical Majorana Propagation method reproducing the Q-CTRL 120-qubit Fermi–Hubbard data for a single site in approximately 2 minutes 30 seconds on a standard MacBook Air, while noting that the comparison is incomplete because the method computes observables separately whereas the quantum processor produces many observables simultaneously; therefore, the reported 3,000-times speedup is sensitive to the observable scope and classical baseline.

**Confidence:** Medium

**Why this confidence level**

S12 directly reports both the competing classical result and the qualification that it does not reproduce the full set of quantum outputs. The supplied material does not include the underlying quantitative publication or independently adjudicate the full comparison.

**Evidence**

- Reports Algorithmiq results reproducing a single-site quantum simulation in 2 minutes 30 seconds and explains that Majorana Propagation computes one observable at a time, unlike the quantum processor's simultaneous generation of many observables. [S12]

## Conflicts and Uncertainty

- Evidence concerning ledger claim C1 is conflicting: The supplied sources do not document a quantum-computing demonstration that delivered commercially useful superiority over a strong classical baseline; reported industrial demonstrations remain pilots, proof-of-concept studies, or projections. [S2] [S4] [S5] [S9] [S12] [S13] [S14] [S6]
- Evidence concerning ledger claim C2 is conflicting: Quantum molecular simulation, particularly for chemistry, materials, and drug-discovery problems, is presented as the most credible near- or medium-term application area, but useful deployment is projected to require substantially more capable, lower-error hardware and is not experimentally validated at commercially relevant scale in the supplied evidence. [S2] [S6] [S10] [S12] [S14]
- Evidence concerning ledger claim C4 is conflicting: The principal hardware barrier identified in the supplied sources is achieving sufficiently low error rates and scalable fault-tolerant computation; current limitations also include limited qubit counts, restricted connectivity, and error susceptibility. [S1] [S2] [S4] [S6] [S9]
- Evidence concerning ledger claim C6 is conflicting: Q-CTRL reports a 2026 demonstration in which an IBM quantum computer, combined with compiler and error-suppression software, solved a Fermionic Simulation materials problem more than 3,000 times faster in wall-clock time than a stated industry-standard classical alternative while meeting or exceeding its accuracy; the supplied source is a vendor report and does not independently establish the result's reproducibility, end-to-end cost advantage, or generality. [S6] [S10] [S11] [S13] [S14] [S9] [S12]

## Remaining Gaps

- No supplied source gives a reproducible, independent experimental benchmark showing a quantum processor beating the best relevant classical hardware or workflow on a commercially meaningful task, including total cost, latency, reliability, and data/integration overhead.
- The supplied evidence does not provide detailed results from the QCHALLenge optimization and machine-learning experiments, so the status of each industrial use case and the magnitude of any quantum-versus-classical performance difference remain unresolved.
- The sources provide conditional application projections and a broad 5–10 year molecular-simulation estimate, but do not specify validated resource estimates, fault-tolerant logical-qubit requirements, runtime thresholds, or uncertainty ranges for commercially relevant workloads.
- The evidence does not independently verify the optimistic claims about 2026 error-correction breakthroughs or establish whether demonstrated logical-error scaling is sufficient for useful applications.
- Important system-level barriers—such as error-correction overhead, compilation, qubit connectivity at application scale, control and calibration, data loading, system cost, and integration reliability—are mentioned only partially and are not quantitatively ranked.
- The S6 reported 3,000-times materials-simulation result lacks, in the supplied material, the full benchmark specification, classical hardware and software details, inclusion of queueing/compilation/data-transfer/post-processing time, total cost or energy comparison, uncertainty, and independent replication needed to determine whether it is a reproducible commercial advantage.
- The supplied benchmarking evidence indicates that annealing-QPU conclusions depend strongly on experimental design, but does not quantify which benchmark conditions reliably produce a commercially meaningful advantage on current hardware or establish performance against contemporary production workflows.
- The supplied sources do not independently adjudicate the full Q-CTRL-versus-Majorana Propagation comparison: it remains unclear whether the classical method can reproduce the complete set of observables at comparable accuracy and total time, including any required repeated runs and data-processing overhead.
- The supplied sources mention independent tests of the Q-CTRL simulation but do not provide their methods, quantitative results, or scope, so the claimed 1% accuracy and 3,000-times advantage cannot yet be assessed as independently replicated across the full workload.
- SQ1: What quantum-computing advantages over classical computers have been experimentally demonstrated to date, and do any constitute commercially useful advantages? (CONFLICTING: At least one linked ledger claim contains conflicting evidence.)
- SQ2: What quantum-computing advantages are theoretically established or currently projected for commercially relevant applications, and how plausible and near-term are those projections? (CONFLICTING: At least one linked ledger claim contains conflicting evidence.)
- SQ3: What classical methods and hardware must quantum computers outperform for an advantage to be commercially meaningful? (CONFLICTING: At least one linked ledger claim contains conflicting evidence.)
- SQ4: What are the biggest remaining technical barriers preventing quantum computers from delivering commercially useful advantages, and how do those barriers affect the expected path to adoption? (PARTIAL: Open high- or medium-importance research gaps still block a sufficient answer.)

## Conclusion

The findings above reflect the evidence validated before the run ended. They should be treated as provisional because normal final synthesis did not complete and important gaps may remain.

## Sources

- [S1] 5 Key Quantum Computing Breakthroughs in 2026 — https://www.bqpsim.com/blogs/quantum-computing-breakthroughs
- [S2] 8 Industry Use Cases for Quantum Computing — https://thequantuminsider.com/2026/05/04/quantum-computing-use-cases-real-applications-industries
- [S3] Quantum computing: What leaders need to know now — https://mitsloan.mit.edu/ideas-made-to-matter/quantum-computing-what-leaders-need-to-know-now
- [S4] Quantum Computing – Strategic Recommendations for the ... — https://arxiv.org/html/2601.08578v1
- [S5] Quantum technology firms race to market as the industry sees ‘inflection point’ — https://www.cnbc.com/2026/03/30/quantum-computing-firms-go-public-breakthroughs-commercialization.html
- [S6] Practical quantum advantage signals a new commercial ... — https://q-ctrl.com/blog/practical-quantum-advantage-signals-a-new-commercial-era-for-quantum-computing
- [S7] Where to Look for Quantum Advantage in your Benchmarking Data | Qubits26 — https://www.youtube.com/watch?v=KzaxcV_HSCY
- [S8] The Power of Quantum Advantage Explained — https://www.bluequbit.io/quantum-advantage
- [S9] Quantum Advantage is Universally Demonstrable — https://www.quera.com/blog-posts/mythbuster---quantum-advantage-is-universally-demonstrable
- [S10] Q-CTRL Achieves 3,000x Speedup in Quantum Materials Simulation - Quantum Computing Report — https://quantumcomputingreport.com/q-ctrl-achieves-3000x-speedup-in-quantum-materials-simulation
- [S11] Q-CTRL Delivers 3000x Speedup in Materials Discovery for the Energy ... — https://q-ctrl.com/blog/q-ctrl-delivers-3-000x-speedup-in-materials-discovery-for-the-energy-sector-with-quantum-computing-and-demonstrates-evidence-of-practical-quantum-advantage
- [S12] Q-CTRL Claims Practical Quantum Advantage — https://postquantum.com/industry-news/qctrl-fermi-hubbard-3000x-quantum-speedup
- [S13] Q-CTRL Delivers 3000x Speedup in Materials Discovery ... — https://thequantuminsider.com/2026/05/06/qctrl-practical-quantum-advantage-materials-discovery
- [S14] Solve complex materials-science problems with the new ... — https://q-ctrl.com/blog/solve-complex-materials-science-problems-with-the-new-fire-opal-quantum-dynamics-simulator
