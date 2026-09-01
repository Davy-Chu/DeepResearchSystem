# Research Report

## Research Question

How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

## Summary

Quantum computing has crossed important technical milestones, including computations designed to be beyond practical classical simulation and increasingly capable logical-qubit demonstrations. However, the accumulated evidence does not establish a broadly reproducible, commercially useful advantage over the best complete classical workflows. Current systems are commercially accessible through cloud and as-a-service offerings, but availability is not equivalent to economic advantage. The strongest projected opportunity is fault-tolerant simulation of molecules, materials, and other quantum systems; optimization, finance, machine learning, and general business workloads remain substantially more uncertain.

## Findings

### Finding 1

**Claim**

Demonstrated technical quantum advantage exists for specialized, synthetic or simulation-hard tasks, but this is not demonstrated commercial advantage.

**Confidence:** High

**Why this confidence level**

Multiple sources provide consistent technical details and explicitly distinguish the benchmark result from commercial usefulness.

**Evidence**

- IBM and University of Chicago reported a structured sampling experiment using 70 logical qubits, 2,415 logical two-qubit operations, and 468 T gates in approximately 15–16 minutes, with leading classical simulation approaches estimated to be impractical. [S33] [S34] [S35]
- The workload was a classically hard sampling benchmark designed to enable error detection, rather than chemistry, finance, optimization, or another production application. [S34]
- The benchmarking framework distinguishes technically hard supremacy-style experiments from useful case studies, which require industry value, real hardware, and demonstrated advantage over classical alternatives. [S6]

### Finding 2

**Claim**

No broadly accepted, independently verified end-to-end commercial quantum advantage has been established in the supplied evidence.

**Confidence:** High

**Why this confidence level**

The conclusion is supported by a peer-reviewed runtime study, a benchmarking review, and an IBM source, and concerns the stricter commercial standard rather than isolated technical demonstrations.

**Evidence**

- A Physical Review Applied analysis concludes that runtime-based advantage has not yet been demonstrated on current NISQ hardware after including system-level overheads and strong classical baselines; one examined quantum implementation was approximately two orders of magnitude slower than a tuned classical baseline. [S8]
- A benchmarking review states that quantum computers had not yet demonstrated practical advantage over classical systems in real-world applications, despite theoretical evidence for advantages on selected problems. [S9]
- IBM’s own explainer says quantum computers have not yet reached the point of solving valuable problems faster, more accurately, or more cost-effectively than classical computers. [S30]

### Finding 3

**Claim**

The HSBC–IBM bond-trading result is best classified as an application-oriented hybrid experiment showing potential, not as established quantum computational or economic advantage.

**Confidence:** High

**Why this confidence level**

The primary source clearly limits its conclusion to statistical observations and exploratory potential. Independent replication and full economic benchmarking are absent.

**Evidence**

- The primary preprint reports up to approximately 34% improvement in out-of-sample prediction scores when classical models use features transformed by IBM Heron hardware. [S22]
- The quantum processing was an offline feature-transformation stage; classical models performed the subsequent prediction, and the paper did not claim a generalizable theory or causal economic effect. [S22]
- The paper reports that hardware-transformed features outperformed noiseless quantum-simulation transforms and suggests that hardware noise contributed to the effect, leaving its cause and generality unresolved. [S22]
- The retrieved evidence does not establish superiority over the full range of optimized classical feature engineering, total workflow cost, total runtime, or realized trading profit. [S16] [S17] [S22]

### Finding 4

**Claim**

The most credible projected commercial advantage is in fault-tolerant simulation of molecules, materials, chemistry, and other quantum systems; current demonstrations remain too small or noisy to displace classical methods.

**Confidence:** High

**Why this confidence level**

Multiple sources converge on quantum-system simulation as the leading projected use case, while the timelines and required hardware levels remain conditional projections.

**Evidence**

- Several sources identify molecular and materials simulation as the strongest prospective application because the systems being simulated obey quantum mechanics, while stating that production-scale drug-discovery and related workloads await fault-tolerant hardware. [S3] [S5] [S6] [S28]
- The use-case analysis states that current molecular-simulation demonstrations have not reached systems complex enough to replace classical methods and gives a conditional 5–10 year projection for useful simulation requiring hundreds of error-corrected logical qubits. [S28]
- MIT’s framework says small- and moderate-sized business problems generally will not benefit, whereas very large problems with suitable algorithmic structure are more plausible candidates. [S13]

### Finding 5

**Claim**

Optimization, finance, machine learning, and most ordinary workloads remain unresolved areas rather than established sources of general quantum advantage.

**Confidence:** High

**Why this confidence level**

The conclusion is consistent across application analyses and methodological frameworks, although individual problem instances could produce different results.

**Evidence**

- The use-case assessment says many optimization problems have highly tuned classical algorithms that quantum approaches have not demonstrated the ability to beat, and describes optimization, AI, and climate modeling as longer-term or uncertain applications. [S28]
- The industrial QCHALLenge framework evaluates optimization and machine learning using scalability, solution quality, runtime, transferability, and comparison with classical solvers, while allowing outcomes in which classical methods remain superior. [S25]
- Most ordinary computing workloads are expected to remain on classical systems, and useful quantum speedups apply only to selected structured problems. [S27] [S28]

### Finding 6

**Claim**

The largest remaining technical barrier is scalable fault tolerance: reliable logical qubits, low logical error rates, deep sustained circuits, and manageable error-correction overhead.

**Confidence:** High

**Why this confidence level**

The same barriers recur across technical milestones, roadmaps, benchmarking studies, and engineering discussions. Exact application-specific thresholds remain unsettled.

**Evidence**

- Sources identify decoherence, environmental noise, gate and interaction errors, limited coherence, cascading errors, and the large physical-qubit overhead of error correction as central obstacles. [S1] [S24]
- Roadmaps describe thousands of physical qubits, hundreds of logical qubits, low error rates, and very large gate counts as requirements for broad commercial applications; current roadmaps are targets rather than demonstrations. [S4] [S6]
- The 70-logical-qubit benchmark improved error control but relied on severe post-selection: one detailed account reports an acceptance rate of 5.90 × 10^-4, with 2,051 accepted samples in 16.1 minutes. [S34]
- The experiment’s fidelity certificate was device-dependent, and the authors acknowledged that post-selection overhead may not scale indefinitely. [S34]

### Finding 7

**Claim**

Benchmarking, verification, and full-system accounting are themselves major barriers to determining whether an apparent advantage is commercially meaningful.

**Confidence:** High

**Why this confidence level**

These requirements are independently stated by peer-reviewed or academic benchmarking sources and directly explain why current claims remain difficult to classify.

**Evidence**

- The runtime analysis warns that readout, transpilation, thermalization, and other system-level overheads can materially bias comparisons if excluded. [S8]
- The benchmarking review calls for relevance, reproducibility, fairness, verifiability, and usability, warning that vendor-defined benchmarks can produce misleading conclusions. [S9]
- The evaluation framework requires problem size, logical and physical resource estimates, solution quality, runtime, cost, business benefit, and rigorous comparison with the best available classical workflow. [S6]
- MIT defines quantum economic advantage as outperforming a comparably priced classical computer, rather than merely achieving an asymptotic or isolated speedup. [S13]

## Conflicts and Uncertainty

- Some vendor and media sources describe Q-CTRL’s materials-simulation claim or IBM-related results as practical or commercial advantage, while peer-reviewed benchmarking evidence applies stricter end-to-end standards and finds no demonstrated practical advantage on current NISQ systems. [S3] [S8] [S9]
- The IBM–University of Chicago experiment is described by IBM-related sources as meeting criteria for quantum advantage, but the task was synthetic sampling rather than a valuable commercial workload. The disagreement is primarily definitional: technical beyond-classical computation versus commercially useful advantage. [S30] [S33] [S34] [S35]
- The HSBC–IBM experiment reports a 34% predictive-score gain, but the result may depend partly on hardware noise and has not been shown in the supplied material to survive optimized classical or stochastic controls, independent datasets, full cost accounting, or independent replication. [S17] [S22]
- Projected timelines range from the late 2020s to the 2030s or later, but these estimates depend on vendor roadmaps, uncertain application requirements, and unproven scaling assumptions. [S4] [S5] [S28] [S29]
- The latest technical benchmark includes a device-dependent fidelity bound and substantial post-selection overhead; therefore, claims of fully verified, scalable computation are stronger than the detailed methodological limitations support. [S33] [S34]

## Remaining Gaps

- No supplied source independently establishes a production-scale application that beats the best complete classical workflow on total runtime, cost, quality, or economic value.
- The Q-CTRL 3,000-fold materials-simulation claim lacks the retrieved independent replication, benchmark details, and complete overhead accounting needed for classification.
- The HSBC–IBM result requires optimized classical controls, independent replication, full resource and cost accounting, and evidence that predictive improvement translates into trading economics.
- It remains unclear whether the 70-logical-qubit verification and error-detection techniques can operate without prohibitive overhead on chemistry, materials, cryptographic, or other application workloads.
- Application-specific requirements for logical-qubit count, logical error rate, circuit depth, runtime, data loading, and total cost remain unsettled.
- The practical timeline and infrastructure requirements for cryptographically relevant fault-tolerant computation are insufficiently covered.
- Research stopped at the stated iteration limit; these unresolved questions should not be treated as answered.

## Conclusion

Quantum computers are no longer merely theoretical: specialized technical quantum advantage has been demonstrated, and logical-qubit error detection and verification have advanced substantially. But the field remains one major step short of the standard that matters commercially—an independently reproducible, production-relevant task that outperforms the best classical workflow after including all runtime, hardware, software, energy, and economic costs. The closest credible path is specialized fault-tolerant simulation of molecules and materials, potentially in the coming years but on uncertain timelines. For optimization, finance, machine learning, and general computing, current evidence supports experimentation and selective hybrid pilots rather than claims of established superiority. The decisive barrier is scalable fault tolerance, complemented by the need for rigorous, standardized, end-to-end benchmarking.

## Sources

- [S1] Quantum Computing vs Classical Computing: Key Differences — https://www.bluequbit.io/blog/quantum-computing-vs-classical-computing
- [S2] Quantum computing - Wikipedia — https://en.wikipedia.org/wiki/Quantum_computing
- [S3] Practical quantum advantage signals a new commercial era for quantum computing | Q-CTRL — https://q-ctrl.com/blog/practical-quantum-advantage-signals-a-new-commercial-era-for-quantum-computing
- [S4] Quantinuum Unveils Accelerated Roadmap to Achieve Universal, Fully Fault-Tolerant Quantum Computing by 2030 — https://www.quantinuum.com/press-releases/quantinuum-unveils-accelerated-roadmap-to-achieve-universal-fault-tolerant-quantum-computing-by-2030
- [S5] Quantum Computing by 2033: Which Industries Win or Wait? — https://postquantum.com/quantum-utility-map/quantum-computing-2033-industries
- [S6] A Practical Framework for Evaluating Quantum Computing ... — https://www.quera.com/blog-posts/a-practical-framework-for-evaluating-quantum-computing-claims
- [S7] Quantum advantage through trusted quantum computation | IBM Quantum Computing Blog — https://www.ibm.com/quantum/blog/quantum-advantage
- [S8] Limits of quantum run-time advantage — https://journals.aps.org/prapplied/abstract/10.1103/gpsf-pn1x
- [S9] Benchmarking Quantum Computers: Towards a Standard Performance Evaluation Approach — https://arxiv.org/html/2407.10941v3
- [S10] Why Quantum Is Here And Why It Is Not - The Innovator — https://theinnovator.news/quantum-computing
- [S11] The path to useful QC Special - The Week in Quantum Computing, July 6th 2026 — https://quantumpirates.substack.com/p/the-path-to-useful-qc-special-the
- [S12] Quantum Computers: The Revolutionary Technology Transforming Computing in 2026 | SpinQ — https://www.spinquanta.com/news-detail/quantum-computers-the-revolutionary-technology-transforming-computing-in-2026
- [S13] Quantum computing: What leaders need to know now — https://mitsloan.mit.edu/ideas-made-to-matter/quantum-computing-what-leaders-need-to-know-now
- [S14] HSBC and IBM Achieve 34% Performance Boost in Quantum-Enabled Bond Trading for 2025 | Quantum + AI Insiders — https://quantumaiinsiders.com/hsbc-ibm-quantum-bond-trading-2025
- [S15] HSBC and IBM achieve 34% improvement in bond trading with quantum computing | Liquid Technology posted on the topic | LinkedIn — https://www.linkedin.com/posts/liquid-technology-inc_hsbcs-quantum-breakthrough-could-be-the-activity-7377357062411898880-kBAB
- [S16] HSBC and IBM’s Quantum-Enabled Bond Trading Breakthrough — https://postquantum.com/quantum-research/hsbc-ibm-quantum-advantage
- [S17] Shtetl-Optimized » Blog Archive » HSBC unleashes yet another “qombie”: a zombie claim of quantum advantage that isn’t — https://scottaaronson.blog?p=9170
- [S18] HSBC demonstrates world’s first-known quantum-enabled algorithmic trading with IBM — https://www.hsbc.com/news-and-views/news/media-releases/2025/hsbc-demonstrates-worlds-first-known-quantum-enabled-algorithmic-trading-with-ibm
- [S19] Quantum leap: HSBC, IBM improve bond RFQ fill rate by 34%  - The DESK - The leading source of information for bond traders — https://www.fi-desk.com/quantum-leap-hsbc-ibm-improve-bond-rfq-fill-rate-up-by-34
- [S20] Bond Trading, Quantum Bond Trading: A Deeper Look at HSBC And IBM's Bond Trading Study — https://thequantuminsider.com/2025/09/28/bond-trading-quantum-bond-trading-a-deeper-look-at-hsbc-and-ibms-bond-trading-study
- [S21] HSBC explores algorithmic trading with IBM quantum computers — https://www.ibm.com/quantum/blog/hsbc-algorithmic-bond-trading
- [S22] Enhanced fill probability estimates in institutional algorithmic bond tradingusing statistical learning algorithms with quantum computers — https://arxiv.org/html/2509.17715v1
- [S23] HSBC and IBM test quantum trading algorithm, see 34% better results | Vincent P. posted on the topic | LinkedIn — https://www.linkedin.com/posts/vincent-p-91b2672_hsbc-demonstrates-worlds-first-known-quantum-enabled-activity-7376912823265697792-ee9z
- [S24] The Potential of Commercial Quantum Computers — https://www.quera.com/blog-posts/potential-of-commercial-quantum-computers
- [S25] Quantum Computing – Strategic Recommendations for the Industry — https://arxiv.org/html/2601.08578v1
- [S26] Quantum Computing: How Close to Commercial Value? | IDTechEx Research Article — https://www.idtechex.com/en/research-article/quantum-computing-how-close-to-commercial-value/33552
- [S27] What Quantum Computers Can Do Better Than Classical Computers — https://postquantum.com/quantum-computing/quantum-classical
- [S28] 8 Industry Use Cases for Quantum Computing — https://thequantuminsider.com/2026/05/04/quantum-computing-use-cases-real-applications-industries
- [S29] Quantum firms race to market as the industry sees ‘inflection point’ — https://www.cnbc.com/2026/03/30/quantum-computing-firms-go-public-breakthroughs-commercialization.html
- [S30] When will quantum computers beat classical computers? | The Coherence Times | IBM — https://www.ibm.com/think/podcasts/the-coherence-times/when-will-quantum-beat-classical-computers
- [S31] Quantum computer completes verified task beyond ... — https://phys.org/news/2026-07-quantum-task-classical-simulations.html
- [S32] [2607.25941] Sampling hard circuits with verifiably high fidelity — https://arxiv.org/abs/2607.25941
- [S33] IBM quantum computer solves classically intractable problem in 15 minutes | ScienceDaily — http://www.sciencedaily.com/releases/2026/08/260829035219.htm
- [S34] IBM and University of Chicago report a verifiable 70-logical-qubit sampling run | MLQ News — https://mlq.ai/news/ibm-and-university-of-chicago-report-a-verifiable-70-logical-qubit-sampling-run
- [S35] IBM and University of Chicago Demonstrate Verified Logical Quantum Computation Beyond Classical Simulation — https://thequantuminsider.com/2026/07/31/ibm-university-of-chicago-verified-logical-quantum-computation
