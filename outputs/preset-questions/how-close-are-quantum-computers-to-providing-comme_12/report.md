# Research Report

## Research Question

How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

## Summary

Quantum computers have reached serious, technically meaningful application experiments, but the supplied evidence does not establish broad, independently validated, end-to-end commercial advantage over classical computers. The strongest current example is a 120-qubit, one-dimensional Fermi–Hubbard simulation on an IBM processor, for which Q-CTRL reports up to a 3,000-fold runtime advantage over a particular TDVP classical baseline. However, competing classical implementations reduce the reported gap substantially or outperform the quantum execution proxy for narrower observables. The result is therefore best regarded as a candidate, task-specific time-to-answer advantage—not proof that quantum computers are generally commercially superior.

## Findings

### Finding 1

**Claim**

Demonstrated quantum advantage is currently narrow and application-specific rather than general-purpose.

**Confidence:** High

**Why this confidence level**

The demonstrated task and its limited scope are directly documented in the primary paper and consistent with the procurement analysis.

**Evidence**

- The primary Fermi–Hubbard paper reports a 120-qubit superconducting-processor simulation with up to 90 Trotter steps, observation of spin-charge separation, and quantitative agreement with classical simulations for selected one-dimensional many-body dynamics. [S33]
- The procurement framework recommends evaluating quantum capability against a specific target workload and warns that promising research results and roadmaps do not prove delivered commercial capability. [S6]

### Finding 2

**Claim**

The Q-CTRL/IBM Fermi–Hubbard experiment is the strongest supplied evidence for a present-day candidate advantage, but the headline 3,000-fold figure is conditional on the selected classical baseline, accuracy criterion, output, and timing definition.

**Confidence:** Medium

**Why this confidence level**

The primary paper supports the original benchmark claim, but competing classical results demonstrate that its magnitude is highly baseline-sensitive and has not been adjudicated under one matched standard.

**Evidence**

- Q-CTRL’s paper reports up to a 3,000-fold quantum wall-clock advantage over an optimized TDVP simulation at bond dimension χ=4096 near the limit of quantum/classical agreement, with approximately 1% RMSE in that comparison. [S33]
- A symmetry-enhanced, GPU-accelerated classical study reports approximately 100 minutes on four NVIDIA H200 GPUs at a comparable bond dimension, reducing the stated comparison to roughly 36-fold, and claims convergence through and beyond the quantum experiment’s difficult interval. [S20] [S22]
- Other classical comparisons report a 10–15 second laptop simulation for related dynamics and a 7.06-fold advantage for a quantum execution proxy over official Monoprop on one selected observable; these comparisons use different output scopes and accuracy conditions. [S26] [S29]

### Finding 3

**Claim**

The Fermi–Hubbard result does not yet demonstrate end-to-end commercial value or broad commercial advantage.

**Confidence:** High

**Why this confidence level**

The absence of these demonstrations and accounting details is consistent across the supplied sources.

**Evidence**

- The experiment concerns a one-dimensional physics model and does not, in the supplied evidence, demonstrate a deployed materials-discovery product, downstream industrial result, customer economics, or measurable business outcome. [S32] [S33]
- The supplied record lacks independent replication, complete cost accounting, and a fully matched end-to-end comparison including compilation, calibration, repetitions, readout processing, postprocessing, queueing, and cloud workflow costs. [S6] [S20] [S29] [S31]

### Finding 4

**Claim**

Pre-fault-tolerant systems can provide scientifically useful results, but scientific utility should not be conflated with commercial quantum advantage.

**Confidence:** High

**Why this confidence level**

The Fermi–Hubbard scientific utility is directly documented; the Nature paper’s commercial significance remains unspecified in the supplied material.

**Evidence**

- The Fermi–Hubbard paper reports scientifically meaningful observables and dynamics before fault tolerance, including spin-charge separation and velocity ratios matching classical simulations. [S33]
- The Nature source is explicitly about utility before fault tolerance, but the supplied excerpt does not provide enough results to determine whether its utility constitutes computational or economic advantage over classical systems. [S9]

### Finding 5

**Claim**

Theoretical and projected advantages remain strongest for selected problem classes, especially quantum simulation, with broader claims for optimization, cryptography, chemistry, materials, and AI still prospective in the supplied evidence.

**Confidence:** High

**Why this confidence level**

The supplied sources consistently frame these broader benefits as selective opportunities, research goals, or projections rather than demonstrated commercial outcomes.

**Evidence**

- The sources describe quantum computing as suitable for specific problems such as molecular and materials simulation, optimization, and cryptography rather than as a replacement for classical machines. [S3] [S5]
- Quantinuum describes quantum-enhanced AI as an objective of ongoing research and does not supply a completed benchmark showing superiority over classical AI systems. [S4]
- The procurement source recommends cloud access, benchmarking, and expertise-building before large local purchases unless mission, facilities, staffing, governance, and upgrade requirements are clear. [S6]

### Finding 6

**Claim**

The biggest hardware barriers are noise, decoherence, error correction, and scaling to sufficiently capable reliable logical systems.

**Confidence:** High

**Why this confidence level**

These barriers are directly identified in technical and hardware-focused sources and are illustrated by the benchmark’s dependence on error suppression and finite validation range.

**Evidence**

- Quantum hardware is described as sensitive to temperature, electromagnetic interference, vibrations, and other sources of decoherence; the systems require specialized operating environments and have differing scalability and error-correction tradeoffs. [S3]
- The Fermi–Hubbard experiment relies on error suppression to obtain useful results from noisy hardware, and the paper identifies machine size and hardware noise as limitations. [S7] [S33]
- The experiment’s quantum/classical agreement ends at a finite evolution time, illustrating the difficulty of maintaining accuracy as circuit complexity and entanglement grow. [S33]

### Finding 7

**Claim**

Benchmarking and workflow accounting are themselves major remaining barriers to establishing commercial advantage.

**Confidence:** High

**Why this confidence level**

Multiple supplied sources document concrete, material differences in baselines, accuracy, output scope, and included costs.

**Evidence**

- Classical results vary substantially with symmetry exploitation, GPU acceleration, propagation method, truncation threshold, bond dimension, and convergence validation. [S20] [S23] [S26] [S29]
- The reported comparisons use different notions of time, including bare QPU execution, characterization-inclusive QPU time, local classical wall time, and full or partial workflow time; some figures exclude compilation, calibration, mitigation, readout processing, postprocessing, or queueing. [S20] [S29] [S31]
- The timing winner and accuracy winner differ in at least one comparison: quantum execution is faster than official Monoprop for mean double occupancy, while Monoprop is closer to the cited MPS reference. [S29]

## Conflicts and Uncertainty

- Q-CTRL-associated sources label the Fermi–Hubbard result a 3,000-fold practical quantum advantage and associate it with positive ROI, while stronger or alternative classical implementations report approximately 36-fold, 7.06-fold, or even faster classical results for narrower observables. These figures are not directly comparable because output scope, accuracy, implementation, hardware, and timing conventions differ. [S7] [S20] [S26] [S29] [S33]
- The primary paper reports agreement with TDVP only up to a finite evolution regime and a speedup at the limit of that agreement. The classical-frontier paper claims to resolve the previously difficult high-entanglement interval and extend beyond the quantum experiment. The supplied evidence does not independently adjudicate the competing implementations. [S20] [S33]
- A selected-observable classical method can be faster than the quantum execution proxy at a loose accuracy cutoff, but more accurate classical settings are slower and may require convergence validation. Whether the quantum workflow wins depends on the required accuracy, number of observables, validation standard, and complete time-to-answer definition. [S23] [S29]
- The Nature article suggests utility before fault tolerance, but the supplied excerpt does not reveal whether that utility involved a classical speedup, a commercially relevant workload, or economic advantage. [S9]
- The available evidence includes vendor announcements, vendor documentation, company-authored technical reports, and preprints. No supplied source provides independent peer-reviewed adjudication of the leading commercial-advantage claim or a complete neutral economic analysis. [S6] [S7] [S9] [S20] [S26] [S29] [S31] [S33]

## Remaining Gaps

- An independent, matched benchmark of the Q-CTRL/IBM workflow against the strongest classical methods using the same observables, accuracy target, sampling uncertainty, initialization, and evolution interval.
- A complete end-to-end time-to-answer comparison including compilation, calibration, queueing, repetitions, error suppression or mitigation, readout correction, postprocessing, classical preprocessing, and convergence validation.
- A determination of whether the competing classical implementations reproduce the full output set reported for the quantum experiment or only selected observables.
- Evidence that the Fermi–Hubbard result produces downstream materials-science or industrial R&D value rather than only faster simulation of a model problem.
- Independent replication or peer review of both the Q-CTRL experiment and the principal classical rebenchmarks.
- Quantitative fault-tolerant resource estimates—logical qubits, physical-qubit overhead, error rates, and runtime—for commercially important chemistry, materials, optimization, or other workloads.

## Conclusion

Quantum computers are close enough to justify serious, narrowly targeted experiments and cloud access, but not close enough—on the supplied evidence—to claim broad commercially useful superiority over classical computers. A technically substantial pre-fault-tolerant simulation has produced a plausible task-specific runtime advantage, yet the reported 3,000-fold figure is highly sensitive to the classical algorithm and to what costs and outputs are counted. Improved classical methods substantially narrow the gap, and some outperform the quantum execution proxy for selected observables. The practical frontier is therefore not yet “quantum computers replace classical computers”; it is identifying workloads where a quantum workflow delivers a reproducible, accuracy-matched, end-to-end time or cost advantage. The decisive remaining challenges are reliable error correction and scaling, control of noise and decoherence, expansion beyond narrow one-dimensional benchmarks, and neutral benchmarking that includes the full workflow and rapidly improving classical alternatives.

## Sources

- [S1] Advantages and Disadvantages of Quantum Computing | Keyfactor — https://www.keyfactor.com/blog/advantages-and-disadvantages-of-quantum-computing
- [S2] Building business readiness for quantum computing: Key barriers and support mechanisms: Building business readiness for quantum computing — https://www.oecd.org/en/publications/building-business-readiness-for-quantum-computing_ee847e5f-en/full-report/component-4.html
- [S3] Quantum Computing vs Classical Computing: Key Differences — https://www.bluequbit.io/blog/quantum-computing-vs-classical-computing
- [S4] Quantum Computers Will Make AI Better - Quantinuum — https://www.quantinuum.com/blog/quantum-computers-will-make-ai-better
- [S5] Practical quantum advantage signals a new commercial era for quantum computing | Q-CTRL — https://q-ctrl.com/blog/practical-quantum-advantage-signals-a-new-commercial-era-for-quantum-computing
- [S6] What quantum computer to buy? — https://arxiv.org/html/2604.04761v1
- [S7] Q-CTRL Delivers 3,000x Speedup in Materials Discovery for the Energy Sector with Quantum Computing, Demonstrates Evidence of Practical Quantum Advantage | Q-CTRL — https://q-ctrl.com/blog/q-ctrl-delivers-3-000x-speedup-in-materials-discovery-for-the-energy-sector-with-quantum-computing-and-demonstrates-evidence-of-practical-quantum-advantage
- [S8] IBM Quantum's Role in Pharmaceutical Drug Discovery | IntuitionLabs — https://intuitionlabs.ai/articles/ibm-quantum-drug-discovery
- [S9] Evidence for the utility of quantum computing before fault tolerance — https://www.nature.com/articles/s41586-023-06096-3
- [S10] IBM's Three Quantum Advantage Claims, Fact-Checked — https://postquantum.com/industry-news/ibm-trusted-quantum-advantage-three-papers
- [S11] Q-CTRL Achieves 3,000x Speedup in Quantum Materials Simulation - Quantum Computing Report — https://quantumcomputingreport.com/q-ctrl-achieves-3000x-speedup-in-quantum-materials-simulation
- [S12] [2605.04025] Fast, accurate, high-resolution simulation of large-scale Fermi-Hubbard models on a digital quantum processor — https://arxiv.org/abs/2605.04025
- [S13] Q-CTRL Claims 3000x Quantum Speedup for Materials ... - HPC Wire — https://www.hpcwire.com/off-the-wire/q-ctrl-claims-3000x-quantum-speedup-for-materials-science-simulations-on-ibm-quantum-platform
- [S14] Quantum Revolution: Unlocking 3000x Speed in Materials Discovery with Q-CTRL (2026) — https://zonneman.com/article/quantum-revolution-unlocking-3000x-speed-in-materials-discovery-with-q-ctrl
- [S15] How should problem-specific compilation be counted in the ... — https://quantumcomputing.stackexchange.com/questions/46252/how-should-problem-specific-compilation-be-counted-in-the-q-ctrl-fermi-hubbard-q
- [S16] Fermi-Hubbard on a quantum computer, part 5: quantum advantage or time-to-answer? - Edukaizen — https://edukaizen.nl/fermi-hubbard-quantum-computer-part-5-quantum-advantage-or-time-to-answer
- [S17] Efficient data replication in distributed clouds via quantum ... — https://www.sciencedirect.com/science/article/pii/S2215016125006065
- [S18] Pushing the Classical Frontier of 1D Fermi–Hubbard ... — https://arxiv.org/html/2606.04771v1
- [S19] [2606.04771] Pushing the Classical Frontier of 1D Fermi-Hubbard Quench Dynamics Beyond Current Quantum Simulations — https://arxiv.org/abs/2606.04771
- [S20] Pushing the Classical Frontier of 1D Fermi-Hubbard ... — https://arxiv.org/pdf/2606.04771
- [S21] Q-CTRL Claims Practical Quantum Advantage — https://postquantum.com/industry-news/qctrl-fermi-hubbard-3000x-quantum-speedup
- [S22] Pushing the Classical Frontier of Quantum Simulation — https://multiversecomputing.com/resources/pushing-the-classical-frontier-of-quantum-simulation
- [S23] Fermi-Hubbard on a quantum computer, part 7: Majorana propagation as a laptop competitor - Edukaizen — https://edukaizen.nl/fermi-hubbard-quantum-computer-part-7-majorana-propagation-as-a-laptop-competitor
- [S24] Q-CTRL Claims Practical Quantum Advantage | Marin Ivezic — https://www.linkedin.com/posts/marinivezic_q-ctrl-claims-practical-quantum-advantage-activity-7457729398838845441-azDK
- [S25] Can a quantum computer beat classical methods on ... — https://quantumcomputing.stackexchange.com/questions/46335/can-a-quantum-computer-beat-classical-methods-on-a-specific-fermi-hubbard-observ
- [S26] Introducing monoprop: propagation at escape velocity - Algorithmiq — https://algorithmiq.fi/news/introducing-monoprop-propagation-at-escape-velocity
- [S27] Code Review Bench: Towards Billion Dollar Benchmarks — https://withmartian.com/post/code-review-bench-v0
- [S28] ResearchClawBench: A Benchmark for End-to-End Autonomous Scientific Research — https://arxiv.org/html/2606.07591v1
- [S29] Fermi-Hubbard on a quantum computer, part 10: the official Monoprop benchmark - Edukaizen — https://edukaizen.nl/fermi-hubbard-quantum-computer-part-11-official-monoprop-benchmark
- [S30] Fast classical simulation of ‘Fast, accurate, high-resolution simulation of large-scale Fermi-Hubbard models on a digital quantum processor’ — https://arxiv.org/html/2608.13805
- [S31] Performance Management - A Qiskit Function by Q-CTRL Fire Opal | IBM Quantum Documentation — https://quantum.cloud.ibm.com/docs/en/guides/q-ctrl-performance-management
- [S32] Q-CTRL announces a successful practical quantum ... — https://runninginterference.substack.com/p/q-ctrl-announces-a-successful-practical
- [S33] Fast, accurate, high-resolution simulation of large-scale ... — https://arxiv.org/html/2605.04025v1
