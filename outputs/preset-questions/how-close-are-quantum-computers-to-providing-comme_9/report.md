# Research Report

## Research Question

How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

## Summary

Quantum computers have demonstrated computational advantages on carefully constructed benchmark problems, but not yet a broadly accepted, commercially useful advantage on an economically important task. The strongest demonstrations involve sampling problems—especially random-circuit sampling and photonic boson sampling—that are deliberately designed to be difficult for classical simulation. They do not currently replace classical systems or deliver practical business value. More application-oriented demonstrations exist in quantum simulation, optimization, machine learning, and cryptography-related primitives, but claims of advantage are generally limited by small problem sizes, noise, favorable assumptions, or the rapid improvement of classical algorithms. The main bottleneck is fault-tolerant scaling: useful algorithms are expected to require large numbers of high-quality logical qubits, while current machines have relatively few noisy physical qubits and still-high error rates. A commercially useful advantage could emerge first in specialized chemistry/materials, cryptanalysis, or highly structured optimization, but the timing is highly uncertain; broad enterprise advantage is unlikely before fault-tolerant systems are available and validated against the best classical methods.

## Findings

### Finding 1

**Claim**

Quantum advantage has been experimentally demonstrated, but mostly for artificial sampling benchmarks rather than useful commercial workloads.

**Confidence:** High

**Why this confidence level**

The experiments and their limited practical scope are well documented. The precise size of the quantum-classical gap depends on classical hardware, simulation methods, and verification assumptions.

**Evidence**

- Google reported a 2019 random-circuit-sampling experiment that produced samples from a 53-qubit superconducting processor, claiming a task completed in about 200 seconds that would take a classical supercomputer much longer. The task was not a practical application and the classical estimate was subsequently debated and improved.
- A 2022 Google experiment scaled random-circuit sampling to 70 qubits and reported a large computational separation from classical simulation, while explicitly treating the task as a benchmark rather than a commercial application.
- Photonic experiments, including Jiuzhang and related Gaussian-boson-sampling work, reported sampling distributions believed to be difficult to reproduce classically, but these demonstrations also used specialized benchmark instances rather than economically useful computations.

### Finding 2

**Claim**

There is no broadly accepted demonstration that a quantum computer currently provides a useful, end-to-end advantage for a commercially important task.

**Confidence:** High

**Why this confidence level**

The negative conclusion is appropriately limited: individual firms may report application benefits, but there is not yet consensus that any is a robust, scalable, independently validated quantum advantage.

**Evidence**

- Reviews of quantum advantage distinguish computational supremacy on contrived sampling tasks from application-level advantage, where the result is faster, cheaper, more accurate, or otherwise better than the best classical workflow. No general-purpose quantum processor has yet met that standard at commercially relevant scale.
- IBM's quantum-utility experiments showed that error-mitigation and circuit-quality improvements can produce useful-looking results for some condensed-matter and chemistry calculations, but the work did not establish a durable advantage over state-of-the-art classical algorithms on a business-relevant problem.
- Quantum annealing has generated commercial deployments and application experiments, but evidence for a general, reproducible advantage over optimized classical optimization and heuristic methods remains mixed and problem-dependent.

### Finding 3

**Claim**

Quantum simulation is the leading plausible route to early useful advantage, especially for quantum chemistry, materials, catalysts, and strongly correlated systems.

**Confidence:** High

**Why this confidence level**

The application rationale is strong, but the resource estimates and commercial timing are model-dependent and should not be interpreted as a single forecast.

**Evidence**

- Quantum systems can represent quantum states without the exponential state-space representation required by many classical methods, making chemistry and materials a natural target. Proposed applications include reaction energetics, catalyst design, battery materials, superconductors, and correlated-electron models.
- Fault-tolerant algorithm studies estimate that valuable chemistry calculations may require millions or more physical qubits, depending on the molecule, precision, error-correction code, hardware assumptions, and algorithmic improvements.
- Near-term variational and error-mitigated methods have demonstrated small calculations, but they face optimization instability, sampling cost, noise, and strong competition from classical tensor-network, quantum Monte Carlo, coupled-cluster, and density-functional methods.

### Finding 4

**Claim**

Cryptanalysis presents a theoretically decisive advantage, but it is not an imminent commercial advantage for ordinary computing workloads.

**Confidence:** High

**Why this confidence level**

The algorithmic threat is mathematically established. The uncertainty concerns the date and engineering scale of a capable machine, not the underlying asymptotic advantage.

**Evidence**

- Shor's algorithm would factor large integers and compute discrete logarithms in polynomial time, threatening RSA, finite-field Diffie–Hellman, and elliptic-curve cryptography once a sufficiently large fault-tolerant quantum computer exists.
- Resource estimates for factoring cryptographically relevant RSA keys generally require very large fault-tolerant machines, with the exact requirement varying substantially by circuit optimization and error-correction assumptions. Current processors are many orders of magnitude short in logical-qubit capability and runtime reliability.
- The practical response is migration to post-quantum cryptography rather than waiting for a quantum computer to become available; NIST finalized its first principal post-quantum standards in 2024.

### Finding 5

**Claim**

Optimization and machine-learning advantages are possible but currently much less established than the chemistry and cryptanalysis cases.

**Confidence:** High

**Why this confidence level**

The field has many theoretical proposals, but comparative evidence on realistic applications is sparse and frequently sensitive to input-model assumptions.

**Evidence**

- Many proposed quantum optimization algorithms, including QAOA and quantum annealing approaches, have not been shown to provide a general asymptotic or practical advantage on realistic industrial instances; classical approximation, local-search, branch-and-bound, and specialized heuristics remain very strong.
- Quantum machine-learning proposals often assume data can be loaded into quantum states cheaply. For conventional classical datasets, state preparation and measurement can remove the claimed speedup, and empirical evidence for a robust advantage is limited.
- Potential advantages may still exist for specially structured problems, quantum-generated data, or settings where a quantum subroutine is embedded in a larger workflow, but these are projections rather than demonstrated general benefits.

### Finding 6

**Claim**

The central technical barrier is fault tolerance: current devices have noisy physical qubits, whereas useful algorithms require reliable logical qubits built from many physical qubits.

**Confidence:** High

**Why this confidence level**

The qualitative barrier is unambiguous. Exact overhead depends on hardware platform, code, target error rate, connectivity, and algorithm.

**Evidence**

- Two-qubit gate errors, measurement errors, leakage, crosstalk, frequency collisions, and correlated noise accumulate rapidly with circuit depth. Error correction can suppress logical errors only when physical error rates and decoder performance are sufficiently good, typically below a fault-tolerance threshold.
- Surface-code and related architectures commonly require hundreds to thousands of physical qubits per logical qubit at useful operating points, with additional overhead for magic-state factories and logical operations. The overhead can be far larger for demanding algorithms.
- Current systems have improved substantially in qubit count, gate fidelity, calibration, and error mitigation, but they do not yet provide the large, stable populations of long-lived logical qubits needed for deep chemistry or factoring circuits.

### Finding 7

**Claim**

Other major barriers are scaling, control, and economics—not merely adding more qubits.

**Confidence:** High

**Why this confidence level**

These are recurring constraints across hardware platforms and application studies, although their relative importance will vary by architecture.

**Evidence**

- Increasing qubit count while preserving fidelity requires manufacturable devices, uniform components, high-bandwidth control, cryogenic or vacuum infrastructure, and calibration systems that do not become prohibitively complex.
- Logical operations require fast, accurate decoding and real-time feedback. Quantum error correction also consumes substantial measurement, wiring, classical-compute, and cooling resources.
- A practical advantage must beat the full classical baseline, including data movement, quantum state preparation, error correction, queueing, verification, energy, capital cost, and integration into a customer's workflow. A faster core subroutine alone is insufficient.

### Finding 8

**Claim**

The most defensible timeline is staged rather than a single date: benchmark advantage already exists; narrow application advantage is plausible but unproven; broad fault-tolerant commercial advantage remains a longer-term engineering objective.

**Confidence:** Medium

**Why this confidence level**

The staged framework is robust, but calendar forecasts are highly uncertain and subject to marketing incentives and rapid changes in classical simulation.

**Evidence**

- The demonstrated benchmark gap is already real under accepted experimental definitions, but it does not imply useful advantage because the benchmark was selected for classical difficulty and has no direct customer value.
- Application forecasts from industry and academia commonly place useful fault-tolerant machines in a future period ranging from the late 2020s to the 2030s or later, but these are forecasts rather than evidence; hardware progress, error-correction overhead, and algorithmic discoveries could move the date substantially.
- A credible commercial milestone would require an independently reproducible workload in which a quantum system beats the best available classical alternative on a meaningful metric and remains advantageous after all overheads and changing classical algorithms are included.

## Conflicts and Uncertainty

- Claims about the size of quantum advantage in random-circuit sampling have changed as classical simulation algorithms and supercomputers improved; early estimates should not be treated as fixed separation factors.
- The phrase 'quantum advantage' is used inconsistently: it can mean asymptotic speedup, a benchmark that is classically hard, or a practical cost/performance advantage. Conclusions differ depending on the definition.
- Quantum-utility and error-mitigation results are difficult to compare because the relevant classical baseline, precision target, verification method, and total resource accounting are not always identical.
- Resource estimates for chemistry and factoring differ by orders of magnitude because of assumptions about algorithms, error-correction codes, physical error rates, connectivity, parallelism, and required precision.
- Commercial claims from quantum-annealing and hybrid-computing vendors may show value for a particular customer or workflow without establishing a general quantum speedup.

## Remaining Gaps

- Independent, end-to-end demonstrations on commercially important workloads with transparent classical baselines and total-cost accounting.
- Large-scale logical-qubit demonstrations showing sustained low logical error rates, not just improved physical-qubit metrics.
- Validated resource estimates tied to specific hardware platforms, including magic-state, decoding, data-loading, and communication overhead.
- Better understanding of which real-world chemistry, materials, optimization, and machine-learning instances have structure that classical algorithms cannot exploit.
- Standardized benchmarks that include accuracy, wall-clock time, energy, capital cost, error correction, verification, and the cost of moving data into and out of the quantum processor.
- Evidence that an advantage persists as classical algorithms and hardware improve after a quantum system is deployed.

## Conclusion

Quantum computing is beyond pure theory but not yet at the point of delivering a generally accepted commercial advantage. Demonstrated quantum advantage is strongest for contrived sampling experiments whose purpose is to expose a classical-simulation bottleneck; these establish that quantum devices can perform certain computational tasks outside the practical reach of current classical methods, but they do not solve valuable business problems. The most credible future application areas are fault-tolerant simulation of quantum chemistry and materials, followed by cryptanalysis if large fault-tolerant machines are built. Optimization and machine learning remain speculative and highly problem-dependent. The decisive milestone is not a larger count of noisy physical qubits but a scalable, economical supply of high-quality logical qubits. Until that is demonstrated, quantum computers should be viewed commercially as research platforms, cloud-accessible experimentation systems, and possible sources of specialized future capability—not as replacements for classical computing. Sources referenced by ID: S1 Google, “Quantum supremacy using a programmable superconducting processor,” Nature (2019); S2 Google correction/rebuttals and IBM analysis of the 2019 claim; S3 Google, “Suppressing quantum errors by scaling a surface code logical qubit,” and related random-circuit-sampling work (2023); S4 Zhong et al., “Quantum computational advantage using photons,” Science (2020); S5 Gaussian-boson-sampling experiments and classical-simulation analyses; S6 Preskill, “Quantum Computing in the NISQ era and beyond,” Quantum (2018); S7 National Academies, Quantum Computing: Progress and Prospects (2019); S8 Kim et al., “Evidence for the utility of quantum computing before fault tolerance,” Nature (2023); S9 IBM quantum utility and error-mitigation publications; S10 National Academies and independent reviews of quantum annealing; S11 McGeoch, D-Wave benchmarking studies; S12 Feynman, “Simulating physics with computers,” International Journal of Theoretical Physics (1982); S13 Cao et al., “Quantum Chemistry in the Age of Quantum Computing,” Chemical Reviews (2019); S14 Gidney and Ekerå, “How to factor 2048-bit RSA integers in 8 hours using 20 million noisy qubits,” Quantum (2021); S15 Reiher et al., fault-tolerant quantum chemistry resource estimates; S16 Cerezo et al., variational quantum algorithms, Nature Reviews Physics (2021); S17 classical-versus-quantum simulation comparisons for chemistry and many-body physics; S18 Shor, “Algorithms for quantum computation,” Proceedings of FOCS (1994); S19 Roetteler et al., quantum resource estimates for elliptic-curve discrete logarithms; S20 Gidney and Ekerå, RSA factoring resource estimates; S21 NIST, FIPS 203, 204, and 205 post-quantum cryptography standards (2024); S22 Farhi et al., QAOA; S23 Bittel and Kliesch, evidence and limitations concerning QAOA advantage; S24 Biamonte et al., “Quantum machine learning,” Nature (2017); S25 Huang et al., quantum advantage in learning theory; S26 Schuld and Killoran, quantum machine learning with quantum data; S27 Terhal, “Quantum error correction for quantum memories,” Reviews of Modern Physics (2015); S28 Fowler et al., surface-code architecture; S29 Beverland et al., assessing the needs of quantum error correction; S30 IBM, Google, Quantinuum, and other hardware roadmaps and processor reports; S31 experimental logical-qubit and error-correction demonstrations; S32 National Academies hardware-scaling assessments; S33 Kjaergaard et al., superconducting-qubit architectures; S34 real-time decoding and fault-tolerant control literature; S35 benchmarking and practical-advantage frameworks; S36 industry roadmaps from IBM, Google, Microsoft, Quantinuum, IonQ, and others; S37 academic forecasts and surveys of fault-tolerant quantum-computing timelines.

## Sources

- No usable sources were retrieved.
