# Research Report

## Research Question

How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

## Summary

The ledger supports a distinction between demonstrated computational advantages and commercially useful quantum economic advantage. Quantum computers have outperformed classical implementations on specially constructed or narrowly selected benchmark problems, including a vendor-reported materials-simulation result claiming a 3,000-times wall-clock speedup. However, the supplied evidence does not independently establish that this result is reproducible, cost-competitive, durable against improved classical methods, or broadly commercially useful. Prospective advantages are concentrated in selected large-scale molecular, materials, and physical-system simulations, with projections for fault-tolerant systems around 2033–2035 or later. The largest remaining barriers are noise and errors, decoherence, limited hardware scale, and immature fault-tolerant error-correction infrastructure.

## Findings

### Finding 1

**Claim**

Quantum computers have demonstrated computational performance advantages on specially constructed benchmark problems, but the supplied evidence does not establish that these demonstrations provide commercially useful advantages over classical computers.

**Confidence:** Medium

**Why this confidence level**

The sources consistently describe performance advantages on selected workloads, but do not establish independent, general, or commercially useful superiority.

**Evidence**

- Google’s 2019 supremacy result concerned a problem described as lacking commercial or practical relevance. [S2]
- A reported 120-qubit materials simulation took about two minutes versus more than 100 hours for a classical implementation, but the result was not independently confirmed as a commercial advantage. [S6] [S7]
- Q-CTRL reported a 3,000-times wall-clock speedup for a fermionic materials simulation, while the source was a company press release rather than independent confirmation. [S8]

### Finding 2

**Claim**

The strongest present-day evidence for commercial usefulness is a disputed, workload-specific claim rather than an established conclusion.

**Confidence:** Low

**Why this confidence level**

The ledger marks the claim as CONFLICTING. Supporting sources report a substantial speedup and characterize it as commercially relevant, while the supplied evidence does not independently validate the commercial comparison or its broader significance.

**Evidence**

- Q-CTRL and related reports characterize a materials-simulation calculation on IBM hardware, augmented with Q-CTRL software, as a practical quantum advantage: approximately two minutes of quantum runtime versus more than 100 hours for classical TDVP software, with claimed industry-standard accuracy. [S2] [S6] [S7] [S8]
- The claim is challenged by the absence of supplied independent validation of comparator optimality, end-to-end runtime, total cost, preprocessing, verification, reproducibility, or durability against improved classical algorithms and GPU acceleration. [S6] [S7] [S8]

### Finding 3

**Claim**

A commercially meaningful quantum advantage should be judged more strictly than an abstract algorithmic or computational advantage: it requires useful performance against a comparably priced or best available classical alternative on a relevant problem.

**Confidence:** Medium

**Why this confidence level**

Both sources distinguish computational advantage from practical or economic usefulness, although the supplied definitions are explanatory or vendor-based rather than independently adjudicated standards.

**Evidence**

- Quantum economic advantage is defined as solving a problem more quickly with a comparably priced classical alternative considered, rather than merely exhibiting a theoretical speedup. [S4]
- Practical advantage is described as outperforming the best conventional alternative on a real-world problem of commercial or scientific relevance while meeting useful speed, accuracy, and affordability requirements. [S2]

### Finding 4

**Claim**

Potential advantages are expected to be concentrated in selected large-scale problems—especially molecular, materials, and physical-system simulation—rather than applying broadly to ordinary business workloads.

**Confidence:** Medium

**Why this confidence level**

The evidence consistently indicates an application-dependent opportunity profile. Broader areas are being investigated, but the ledger does not show demonstrated advantage across them.

**Evidence**

- Typical small-to-moderate business problems generally are not expected to benefit, whereas problems with exponential algorithmic gains or very large datasets may benefit; matter simulation and drug discovery are cited as possible areas. [S4]
- A projected 2,000-logical-qubit fault-tolerant system is described as particularly suited to molecular, materials, and physical-system simulation, while no demonstrated advantage is identified for supply-chain optimization, machine learning, or derivatives pricing. [S5]
- Optimization, Hamiltonian simulation, partial differential equations, and machine learning are identified as research areas for possible value, not as established broad commercial advantages. [S9]

### Finding 5

**Claim**

The largest remaining technical barriers are noise and errors, decoherence, insufficient hardware scale, and immature fault-tolerance and error-correction infrastructure.

**Confidence:** High

**Why this confidence level**

Multiple sources independently identify noise, decoherence, scale, and error correction as central limitations, and the current demonstration itself reportedly required error-suppression software.

**Evidence**

- Noise, errors, hardware size, and the need for error suppression are identified as obstacles to useful larger-scale applications. [S2]
- Qubits are sensitive to temperature, electromagnetic interference, and vibrations; decoherence disrupts computation, and hardware platforms continue to differ in scalability, stability, speed, and error-correction properties. [S3]
- The projected use cases depend on machines with thousands of logical qubits and large error-corrected workloads, while other reporting indicates that complex-problem hardware and software may not be available until 2035 or later. [S4] [S5]
- Runtime performance-management and error-suppression software was presented as necessary to obtain useful accuracy in the reported 120-qubit materials simulation, underscoring that noise remains a practical current barrier. [S6] [S7] [S8]

### Finding 6

**Claim**

The timing of commercially useful quantum computing remains uncertain and workload-specific; the ledger does not support a single reliable timetable.

**Confidence:** Medium

**Why this confidence level**

The ledger marks the timing evidence as CONFLICTING. Present-day claims, conditional 2033 projections, and a 2035-or-later estimate may reflect different workloads and definitions, and the sources do not reconcile those differences.

**Evidence**

- One source estimates that hardware and software for the most complex problems may not be available until 2035 or later. [S4]
- Another projection anticipates competitive impact by 2033 for selected pharmaceutical, chemical, and battery applications, conditional on a 2,000-logical-qubit fault-tolerant machine. [S5]
- Q-CTRL and related reporting claim a present-day practical advantage for a narrowly defined materials-simulation workload. [S2] [S6] [S7] [S8]
- The present-day claim remains uncertain because it is vendor-reported, concerns a specific workload, and may be affected by future improvements to classical algorithms or GPU implementations. [S7] [S8]

## Conflicts and Uncertainty

- The Q-CTRL/IBM materials-simulation result is described by company and partner sources as present-day practical quantum advantage, but the supplied evidence does not independently verify the classical baseline, full end-to-end costs and runtimes, preprocessing, verification, reproducibility, or broader commercial value. [S2] [S6] [S7] [S8]
- Present-day claims for a narrow materials workload conflict with projections that complex useful workloads require large fault-tolerant systems available around 2033 or 2035 or later. The disagreement may reflect different workloads and definitions of advantage, but the ledger does not resolve it. [S4] [S5] [S6] [S7] [S8]
- The durability of the reported speedup is uncertain because future classical algorithm improvements or GPU acceleration could change the comparison. [S7]

## Remaining Gaps

- Independent, peer-reviewed or externally validated testing of the reported 3,000-times materials-simulation result against the best classical algorithms, including end-to-end runtime, accuracy, cost, preprocessing, and verification.
- Quantified requirements for physical-qubit overhead, error rates, logical-qubit performance, energy use, and operating costs for commercially useful fault-tolerant workloads.
- Evidence identifying specific commercial applications with reproducible advantage after accounting for data loading, classical post-processing, repeated probabilistic measurement, and state-of-the-art classical methods.
- A source-based assessment of the reliability of the projected 2033–2035 timelines and a systematic reconciliation of differing definitions of quantum, practical, absolute, and economic advantage.

## Conclusion

On the supplied evidence, quantum computers are not yet established as broadly commercially superior to classical computers. Demonstrated or reported advantages exist for specially selected problems, most notably a disputed materials-simulation result claiming a 3,000-times speedup. That should be treated as evidence of a promising, workload-specific claim—not as independently confirmed quantum economic advantage. The better-supported medium-term picture is conditional: meaningful benefits may emerge in molecular, materials, and related physical-system simulations once sufficiently large fault-tolerant systems are available. Noise, decoherence, hardware scale, and error-correction infrastructure remain the principal technical barriers, and the ledger leaves commercial reproducibility, cost competitiveness, and timeline reliability unresolved.

## Sources

- [S1] Quantum computing - Wikipedia — https://en.wikipedia.org/wiki/Quantum_computing
- [S2] Practical quantum advantage signals a new commercial ... — https://q-ctrl.com/blog/practical-quantum-advantage-signals-a-new-commercial-era-for-quantum-computing
- [S3] Quantum Computing vs Classical Computing: Key Differences — https://www.bluequbit.io/blog/quantum-computing-vs-classical-computing
- [S4] Quantum computing: What leaders need to know now — https://mitsloan.mit.edu/ideas-made-to-matter/quantum-computing-what-leaders-need-to-know-now
- [S5] Quantum Computing by 2033: Which Industries Win or Wait? — https://postquantum.com/quantum-utility-map/quantum-computing-2033-industries
- [S6] Q-CTRL Delivers 3,000x Speedup in Materials Discovery for the Energy Sector with Quantum Computing — https://thequantuminsider.com/2026/05/06/qctrl-practical-quantum-advantage-materials-discovery
- [S7] Q-CTRL’s Software Cuts Materials Simulation Time By 3,000x — https://quantumzeitgeist.com/materials-simulation-time-q-ctrls-software
- [S8] Q-CTRL Delivers 3,000x Speedup in Materials Discovery for the Energy Sector with Quantum Computing, Demonstrates Evidence of Practical Quantum Advantage | Q-CTRL — https://q-ctrl.com/blog/q-ctrl-delivers-3-000x-speedup-in-materials-discovery-for-the-energy-sector-with-quantum-computing-and-demonstrates-evidence-of-practical-quantum-advantage
- [S9] IBM Quantum Computing | Research and publications — https://www.ibm.com/quantum/research
