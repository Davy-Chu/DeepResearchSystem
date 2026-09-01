# Research Report

## Research Question

How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

## Summary

The supplied evidence supports a cautious separation between narrow laboratory demonstrations, theoretically established algorithmic speedups, and commercially useful advantage. The Google Sycamore result is a contested benchmark whose classical comparison was materially challenged, while the Q-CTRL/IBM materials-simulation result is a low-confidence vendor claim lacking independent validation. The strongest prospective opportunities are application-specific, particularly selected large quantum- and materials-simulation problems, but projected benefits depend on fault-tolerant hardware, substantial logical-qubit resources, competitive classical baselines, and favorable end-to-end economics. The evidence does not establish a calibrated timeline for broad commercial advantage.

## Findings

### Finding 1

**Claim**

Experimentally demonstrated quantum advantage remains narrow and does not yet establish broad commercial usefulness. The Google Sycamore benchmark was reported as 200 seconds on a 53-qubit processor versus Google's estimate of 10,000 years classically, but IBM estimated approximately 2.5 days for the classical computation. The supplied evidence therefore supports a contested laboratory benchmark, not an unqualified practical advantage.

**Confidence:** Medium

**Why this confidence level**

The evidence directly records the competing comparisons, but comes from a secondary source and does not establish independent reproduction, a settled best-classical baseline, verification cost, or commercial relevance.

**Evidence**

- S9 reports both Google's original Sycamore comparison and IBM's substantially lower classical-runtime estimate, which directly challenges the magnitude of the claimed advantage. [S9]

### Finding 2

**Claim**

A Q-CTRL report claims a 3,000-times wall-clock speedup for an IBM-based fermionic or materials-simulation task while meeting stated accuracy and practical-time requirements, but a reliable conclusion about genuine, reproducible, or commercially valuable advantage cannot currently be drawn.

**Confidence:** Low

**Why this confidence level**

The claim is vendor-authored and the supplied evidence does not independently establish the task definition, strongest classical baseline, reproducibility, full costs, or commercial return.

**Evidence**

- Q-CTRL states that its demonstration exceeded an industry-standard classical alternative by more than 3,000 times and met accuracy and practical-time requirements. [S2]

### Finding 3

**Claim**

Theoretical and projected advantage is application-specific rather than general. The strongest prospects are selected large problems with favorable quantum algorithms, especially quantum-system or materials simulation; small-to-moderate business problems generally are not expected to benefit unless hardware and end-to-end economics clearly outperform classical alternatives.

**Confidence:** High

**Why this confidence level**

The latest verification supports the qualified, application-specific formulation. However, the evidence does not independently validate commercial outcomes or all application projections.

**Evidence**

- MIT Sloan describes advantage as concentrated in sufficiently large problems with major algorithmic gains and identifies matter simulation as a candidate area; it reports that small-to-moderate business problems generally may not benefit. [S4]
- The industry analysis projects a narrow advantage map concentrated in quantum-mechanical simulation and reports no demonstrated advantage for supply-chain optimization, machine learning, or derivatives pricing. [S5]
- The algorithm overview presents Shor's and Grover's results as advantages for specific structured problem classes rather than as general-purpose improvements. [S9]

### Finding 4

**Claim**

Shor's factoring algorithm and Grover's unstructured-search algorithm provide theoretically established algorithmic speedups, but the supplied evidence does not show current hardware delivering a commercial advantage from either result.

**Confidence:** Medium

**Why this confidence level**

The algorithmic claims are directly reported, but the evidence is secondary and lacks resource estimates, fault-tolerant implementation evidence, and commercial comparisons.

**Evidence**

- S9 describes Shor's polynomial-time factoring approach and Grover's approximately quadratic speedup, while providing no current-hardware or end-to-end commercial demonstration. [S9]

### Finding 5

**Claim**

Fault-tolerant quantum simulation is projected as a potentially high-value area in chemistry, catalysis, pharmaceuticals, and batteries or energy, but the cited resource requirements, timelines, and economic impacts are projections rather than demonstrated commercial advantages.

**Confidence:** Low

**Why this confidence level**

The source is a forward-looking industry analysis, and the supplied material does not independently validate its assumptions, timelines, resource estimates, or business outcomes.

**Evidence**

- The industry analysis projects significant impact in these sectors under assumed future fault-tolerant capabilities, resource estimates, and economic conditions. [S5]

### Finding 6

**Claim**

The most important remaining technical barriers are noise and physical errors, error-correction overhead, insufficient hardware scale, scalable hardware and control, and verification complexity. These barriers are especially decisive for large-scale simulation and other applications requiring long fault-tolerant computations.

**Confidence:** High

**Why this confidence level**

Multiple supplied sources support the existence of these barriers. Their relative ranking, current numerical values, and application-specific thresholds remain unresolved.

**Evidence**

- Q-CTRL identifies hardware size, noise, and errors as obstacles to obtaining useful results on relevant problems. [S2]
- MIT Sloan reports that hardware and software for the most complex problems may not be available until 2035 or later. [S4]
- The industry projection assumes a fault-tolerant system with 2,000 logical qubits and one billion error-corrected operations, illustrating the scale gap underlying projected applications. [S5]
- The review identifies noisy current devices, error-correction overhead, hardware scalability, and verification complexity as continuing challenges. [S8]
- The article describes current hardware as insufficient for practical RSA-2048 factoring, illustrating the scale gap for cryptographic applications. [S9]

### Finding 7

**Claim**

Commercial quantum advantage should be evaluated against a comparably priced and available classical alternative using end-to-end outcomes, including runtime, accuracy, reliability, cost, affordability, and practical usefulness, rather than a theoretical speedup or isolated benchmark.

**Confidence:** High

**Why this confidence level**

The latest verification confirms this as the appropriate commercial-evaluation standard, although the supplied evidence does not provide complete measurements for candidate workloads.

**Evidence**

- MIT Sloan distinguishes quantum advantage from quantum economic advantage and emphasizes comparison with a comparably priced classical computer. [S4]
- Q-CTRL defines practical advantage relative to the best available conventional alternative and emphasizes useful time, accuracy, and affordability. [S2]

### Finding 8

**Claim**

For quantum machine learning in digital health, a reliable conclusion about superiority over classical methods cannot currently be drawn from the supplied evidence.

**Confidence:** Low

**Why this confidence level**

The source establishes the review's scope, not its results; therefore it cannot establish either a QML advantage or its absence.

**Evidence**

- The systematic review is described as evaluating whether QML outperforms existing classical methods, but the supplied excerpt does not provide its findings or quantitative comparisons. [S6]

## Conflicts and Uncertainty

- The Sycamore claim has meaningful supporting and contradicting evidence: Google's reported 200-second versus 10,000-year comparison is supported, while IBM's approximately 2.5-day estimate contradicts the original classical baseline. The supplied evidence does not settle which comparison is definitive or whether the benchmark has practical value. [S9]
- The Q-CTRL/IBM 3,000-times speedup is supported only by a vendor report and lacks independent validation of baseline quality, reproducibility, cost, and commercial ROI. [S2]
- Projected advantages in simulation-related industries are conditional scenarios, not empirical demonstrations. Their hardware assumptions, timelines, and economic impacts are not independently established in the supplied ledger. [S5]
- The evidence does not quantify physical error rates, logical-qubit availability, error-correction overhead, coherence, connectivity, decoding, throughput, operating cost, or integration requirements relative to commercial workloads. [S2] [S4] [S5] [S8] [S9]

## Remaining Gaps

- G1: Independent, peer-reviewed verification of the Q-CTRL/IBM materials-simulation speedup, including task definition, classical baseline, costs, accuracy, runtime, reproducibility, and commercial value.
- G2: Quantitative current-versus-required measurements for physical and logical errors, error-correction overhead, logical qubits, coherence, connectivity, decoding, throughput, and operating cost.
- G3: Independent application-specific comparisons for chemistry, pharmaceuticals, catalysis, batteries, optimization, cryptography, and machine learning against the strongest evolving classical methods.
- G4: A calibrated timeline or probability for commercially useful advantage; the cited 2030 and 2035-or-later expectations remain projections with unstated assumptions.
- G5: End-to-end commercial data covering deployment and access costs, energy use, integration, input/output and data-loading costs, reliability, and workload value.
- G6: Primary, peer-reviewed, independently reproduced analysis of the Sycamore benchmark using settled strong classical baselines and accounting for verification and practical relevance.
- G7: Results and quantitative comparisons from the cited digital-health QML review.
- G8: Application-specific resource estimates and end-to-end comparisons for theoretically advantageous algorithms such as factoring and search.

## Conclusion

On the supplied evidence, quantum computers are not yet shown to provide a broadly commercially useful advantage over classical computers. Demonstrated advantages are confined to narrow laboratory or vendor-reported results: Sycamore is contested, and the Q-CTRL/IBM result is low-confidence and unindependently verified. The theoretical case is stronger but conditional and concentrated in selected large, structured workloads—especially quantum simulation—rather than ordinary small-to-moderate business problems. Commercial usefulness is therefore best characterized as a future, application-dependent possibility rather than an established capability. The decisive unknown is not whether quantum algorithms can have asymptotic advantages, but whether fault-tolerant systems can deliver them at sufficient scale, accuracy, throughput, reliability, and total cost against improving classical alternatives. No supplied evidence supports a reliable general timeline.

## Sources

- [S1] Quantum computing - Wikipedia — https://en.wikipedia.org/wiki/Quantum_computing
- [S2] Practical quantum advantage signals a new commercial era for quantum computing | Q-CTRL — https://q-ctrl.com/blog/practical-quantum-advantage-signals-a-new-commercial-era-for-quantum-computing
- [S3] Quantum Computing vs Classical Computing: Key Differences — https://www.bluequbit.io/blog/quantum-computing-vs-classical-computing
- [S4] Quantum computing: What leaders need to know now | MIT Sloan — https://mitsloan.mit.edu/ideas-made-to-matter/quantum-computing-what-leaders-need-to-know-now
- [S5] Quantum Computing by 2033: Which Industries Win or Wait? — https://postquantum.com/quantum-utility-map/quantum-computing-2033-industries
- [S6] A systematic review of quantum machine learning for digital health — https://pmc.ncbi.nlm.nih.gov/articles/PMC12048600
- [S7] What is Quantum Machine Learning (QML)? Complete 2026 Guide — https://www.articsledge.com/post/quantum-machine-learning-qml
- [S8] Frontiers | Quantum computing: foundations, algorithms, and emerging applications — https://www.frontiersin.org/journals/quantum-science-and-technology/articles/10.3389/frqst.2025.1723319/full
- [S9] What Quantum Computers Can Do Better Than Classical Computers — https://postquantum.com/quantum-computing/quantum-classical
