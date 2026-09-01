# How close are quantum computers to commercially useful advantages?

## Executive summary

Quantum computers have demonstrated **clear computational advantages over classical methods on specially constructed benchmark problems**, especially random-circuit sampling and boson-sampling-like tasks. However, these demonstrations generally do **not yet provide commercially useful advantages**: the problems are designed to be difficult for classical simulation but have little direct business value, and the quantum output is often hard to verify.

For commercially relevant workloads—drug discovery, materials design, optimization, machine learning, finance, logistics, and cryptanalysis—there is currently **no broadly accepted demonstration of a fault-tolerant quantum computer delivering a superior real-world economic result** at lower cost, higher accuracy, or faster time than the best classical alternatives.

The field is therefore in a transitional stage:

- **Demonstrated quantum advantage:** Yes, for artificial sampling and benchmarking tasks.
- **Demonstrated useful quantum advantage:** Not yet established.
- **Theoretical algorithms with potentially transformative value:** Yes, especially Shor’s algorithm and quantum simulation.
- **Likely timing:** Narrow, commercially useful applications may emerge first in the **2030s**, but timing is highly uncertain. Large-scale cryptographic impact requires much larger fault-tolerant machines, likely later.
- **Biggest barrier:** Not merely increasing the number of physical qubits, but building a reliable, scalable system of **logical qubits** with sufficiently low error rates, efficient error correction, fast control, and useful algorithms.

---

## 1. What counts as “quantum advantage”?

The phrase is used for several different claims that should not be conflated.

### 1.1 Quantum speedup

A quantum algorithm solves a problem asymptotically faster than the best known classical algorithm.

Examples:

- **Shor’s algorithm:** polynomial-time factoring and discrete logarithms versus the best known sub-exponential classical methods.
- **Grover’s algorithm:** roughly quadratic speedup for unstructured search.
- **Quantum simulation algorithms:** potentially exponential or otherwise substantial improvements for certain quantum systems.

These are theoretical or algorithmic claims. They do not necessarily imply that today’s hardware can realize the advantage.

### 1.2 Demonstrated quantum computational advantage

A quantum processor performs a computational task that is infeasible—or substantially less practical—for a classical computer.

Examples include:

- Random circuit sampling
- Boson sampling
- Certain many-body dynamics experiments
- Specialized sampling and linear-algebra benchmarks

The task may be deliberately artificial. Demonstrated advantage therefore does not automatically mean commercial usefulness.

### 1.3 Useful quantum advantage

A quantum system produces a better result on a commercially relevant problem, considering the complete workflow:

- Data loading
- Problem encoding
- Quantum execution
- Error mitigation or correction
- Classical post-processing
- Verification
- Hardware and operating cost
- Time-to-solution
- Quality of solution

On this stricter definition, **no generally accepted example has yet been demonstrated**.

---

# 2. What has actually been demonstrated?

## 2.1 Random-circuit sampling

The most prominent demonstrations use quantum processors to generate samples from the output distribution of random quantum circuits.

### Google Sycamore, 2019

Google reported that its 53-qubit Sycamore processor completed a random-circuit sampling task in about 200 seconds that it estimated would require thousands of years on a classical supercomputer.

The result was important as a proof that a programmable quantum processor could enter a regime difficult to simulate directly. However:

- The circuit had no known commercial application.
- It was a sampling benchmark, not an optimization, chemistry, or machine-learning task.
- The classical estimate was challenged and subsequently improved using better simulation methods.
- The quantum device itself produced noisy samples, making verification nontrivial.

The result is best interpreted as a **milestone in quantum hardware**, not a commercially useful speedup.

### Subsequent demonstrations

Google, IBM, USTC, and other groups have reported larger or more difficult random-circuit and sampling experiments. China’s USTC group demonstrated photonic boson sampling with **Jiuzhang** and superconducting random-circuit sampling with **Zuchongzhi**.

These experiments strengthen the evidence that quantum devices can outperform straightforward classical simulation for carefully chosen sampling tasks. They do not yet show an advantage on a practical workload.

## 2.2 Boson sampling and photonic experiments

Boson sampling uses photons passing through optical networks. The output distribution is believed to be difficult to sample classically under plausible complexity assumptions.

Important demonstrations include:

- **Jiuzhang**, beginning in 2020
- Subsequent higher-dimensional and Gaussian boson-sampling experiments
- Photonic systems from several academic and industrial groups

Strengths:

- Potentially high-dimensional quantum state spaces
- Natural suitability for sampling problems
- Photons can have relatively long coherence times

Limitations:

- Present systems are usually specialized rather than universal quantum computers.
- Photon loss and source/detector imperfections are major problems.
- The benchmark tasks generally lack direct commercial value.
- Classical simulators and approximate methods can narrow the claimed advantage.

## 2.3 Quantum annealing

D-Wave has deployed large commercial quantum annealers and has reported performance advantages for some optimization and sampling problems.

The evidence is mixed.

Quantum annealers have demonstrated that specialized quantum hardware can solve certain optimization instances and can sometimes be competitive with classical heuristics. But whether they deliver a **general quantum speedup** is disputed. Results depend heavily on:

- Instance selection
- Classical baseline
- Embedding overhead
- Parameter tuning
- Whether the comparison uses the best available classical solver
- Whether total wall-clock time includes input preparation and output processing

For some applications, D-Wave systems may be useful as experimental optimization accelerators. But there is no consensus that quantum annealing has produced a broad, reproducible, economically decisive advantage over classical optimization software.

## 2.4 Error-correction demonstrations

A more strategically important achievement is progress in quantum error correction.

Google’s 2023 surface-code experiment reported that increasing the size of a surface-code logical qubit reduced logical error rates, a key requirement for scalable fault-tolerant computing. IBM and other groups have also demonstrated increasingly capable error-correcting codes, logical operations, and fault-tolerant components.

These are not commercial application advantages. They are evidence that the field may be moving toward the architecture needed to obtain them.

The critical distinction is:

> A logical error rate below the physical error rate is encouraging, but it is not the same as having a large, useful fault-tolerant quantum computer.

A practical machine requires many logical qubits, long computations, fault-tolerant gates, memory, interconnects, decoding, and system-level reliability.

## 2.5 Quantum simulation experiments

Quantum processors have simulated small molecules, spin systems, lattice models, and chemical dynamics. These experiments demonstrate that quantum hardware can represent and manipulate quantum states in ways that are difficult to reproduce exactly classically as system size grows.

However, most current results remain below the threshold for commercial chemistry or materials discovery because:

- The systems are too small.
- Noise limits circuit depth.
- Classical approximations remain highly effective for many target molecules.
- Useful quantities often require extremely high precision.
- State preparation and measurement can dominate the cost.

Quantum simulation is among the strongest candidates for future useful advantage, but the advantage has not yet been demonstrated at commercial scale.

---

# 3. The leading commercially relevant applications

## 3.1 Chemistry and drug discovery

This is often presented as the most plausible early application.

Quantum computers could eventually help calculate:

- Molecular ground-state energies
- Reaction pathways
- Catalytic mechanisms
- Electronic structure
- Excited states
- Strongly correlated materials
- Battery and photovoltaic materials

The potential value is large because classical electronic-structure methods become difficult for certain strongly correlated systems. But practical requirements are demanding:

- High precision, often better than “chemical accuracy”
- Large numbers of logical qubits
- Deep fault-tolerant circuits
- Efficient state preparation
- Error correction over long computations
- Reliable extraction of small energy differences

Near-term variational algorithms such as VQE have not yet shown a reliable commercial advantage. They are useful research tools, but noise, barren optimization landscapes, measurement costs, and classical simulation improvements limit their current value.

**Assessment:** High long-term potential; no demonstrated commercial advantage yet.

## 3.2 Materials science

Possible targets include:

- Superconductors
- Magnetic materials
- Quantum materials
- Carbon capture catalysts
- Hydrogen catalysts
- Batteries
- Industrial chemical processes

These problems are attractive because quantum mechanics directly governs the phenomena of interest. The challenge is that industrially useful material design requires solving a complete chain of problems, not merely estimating one ground-state energy.

**Assessment:** Potentially transformative, but likely requires fault-tolerant quantum computers and strong integration with classical modeling and experimentation.

## 3.3 Optimization and logistics

Proposed applications include:

- Vehicle routing
- Scheduling
- Supply-chain optimization
- Portfolio construction
- Facility location
- Traffic control
- Manufacturing

The major problem is that many optimization problems are NP-hard, but that does not mean quantum computers automatically solve them efficiently. Quantum algorithms generally provide no known exponential speedup for arbitrary NP-hard optimization.

Potential approaches include:

- Quantum approximate optimization algorithm, or QAOA
- Quantum annealing
- Amplitude-amplification methods
- Quantum algorithms for structured graph problems
- Hybrid quantum-classical heuristics

To date, no quantum optimization method has shown a robust, application-scale advantage over strong classical solvers on representative industrial datasets.

Classical optimization is extraordinarily advanced, benefiting from decades of algorithm engineering, custom hardware, heuristics, relaxations, and machine learning. Quantum methods must beat this entire ecosystem, not an outdated baseline.

**Assessment:** Possible niche advantages for specially structured problems; no convincing general advantage yet.

## 3.4 Machine learning

Quantum machine learning is often discussed as a major opportunity, but the case remains speculative.

Potential sources of speedup include:

- Quantum linear-algebra subroutines
- Quantum kernels
- Quantum generative models
- Amplitude estimation
- Quantum-enhanced sampling

Practical obstacles are especially severe:

- Classical data must be loaded into the quantum system.
- Data loading may erase the theoretical speedup.
- Many proposed algorithms require fault-tolerant subroutines.
- Classical neural networks and specialized accelerators are improving rapidly.
- Evidence for a meaningful quantum advantage on real-world datasets is weak.

**Assessment:** Low confidence as an early commercial application; theoretical interest remains high.

## 3.5 Finance

Proposed applications include:

- Portfolio optimization
- Risk analysis
- Derivative pricing
- Monte Carlo acceleration
- Fraud detection
- Credit-risk modeling

The strongest theoretical case is quantum amplitude estimation, which can offer a quadratic reduction in sampling complexity for certain Monte Carlo calculations. But this requires:

- Fault-tolerant quantum computation
- Efficient state preparation
- Coherent evaluation of financial models
- High precision
- Significant logical-qubit resources

For portfolio optimization, quantum methods face the same problems as other combinatorial optimization applications.

**Assessment:** Some credible theoretical speedups, but practical deployment is likely fault-tolerant and long-term.

## 3.6 Cryptanalysis

Shor’s algorithm could factor large integers and solve discrete logarithms, threatening RSA, Diffie–Hellman, and elliptic-curve cryptography.

This is the clearest example of a potentially decisive quantum advantage. But it is not yet a current commercial advantage because the required machine is vastly larger and more reliable than today’s systems.

Resource estimates vary by architecture and assumptions, but breaking commonly used cryptographic keys is generally expected to require:

- Thousands of logical qubits, possibly more
- Millions of physical qubits under surface-code assumptions
- Very low logical error rates
- Long computations with fast error correction

The exact numbers depend strongly on code, gate speed, connectivity, architecture, and cryptographic parameters.

The practical implication is that organizations should already be migrating to **post-quantum cryptography**, because encrypted data captured today may be decrypted later—a “harvest now, decrypt later” risk.

**Assessment:** Theoretical advantage is exceptionally strong; hardware realization remains far away compared with current machines.

---

# 4. The most important distinction: NISQ versus fault-tolerant quantum computing

## 4.1 Noisy intermediate-scale quantum systems

Current processors are generally characterized by:

- Tens to thousands of physical qubits
- Imperfect gates and measurements
- Limited connectivity
- Short coherence relative to algorithmic requirements
- No full error correction
- Significant calibration overhead

These devices can perform experiments and small computations, but errors accumulate rapidly with circuit depth.

The main near-term strategies are:

- Error mitigation
- Variational algorithms
- Analog simulation
- Specialized sampling
- Hybrid quantum-classical algorithms

Error mitigation can improve results without adding all the qubits required for full error correction, but it usually increases measurement costs and does not scale indefinitely. In many cases, the cost grows rapidly as circuits become deeper or noise increases.

## 4.2 Fault-tolerant quantum computers

A fault-tolerant machine would encode logical qubits across many physical qubits and continuously detect and correct errors.

It needs:

1. Physical error rates below the threshold of the chosen code.
2. Sufficiently low logical error rates.
3. Efficient syndrome measurement and decoding.
4. Fault-tolerant gate operations.
5. Large numbers of logical qubits.
6. Fast execution relative to coherence and correction cycles.
7. Reliable initialization and measurement.
8. Interconnects and modular scaling.
9. Software capable of compiling useful algorithms efficiently.

Commercially important algorithms such as Shor’s algorithm and high-precision quantum chemistry are generally expected to require fault tolerance.

---

# 5. Biggest remaining technical barriers

## 5.1 Physical error rates and error correction overhead

Quantum gates, measurements, state preparation, and qubit memory are all imperfect. Error correction converts many unreliable physical qubits into fewer reliable logical qubits, but the overhead can be enormous.

For surface-code architectures, a single logical qubit may require hundreds or thousands of physical qubits depending on:

- Physical error rate
- Desired logical error rate
- Circuit depth
- Code distance
- Noise correlations
- Connectivity
- Leakage errors

A practical machine may therefore require millions of physical qubits for applications that need thousands of logical qubits.

## 5.2 Scaling from laboratory systems to engineered systems

Adding qubits is not enough. The system must preserve performance as it grows.

Challenges include:

- Crosstalk
- Wiring density
- Control electronics
- Calibration automation
- Frequency collisions
- Thermal load
- Fabrication variability
- Defects and leakage
- Uniformity across the processor

A 100-qubit system and a million-qubit system are not simply versions of the same engineering problem.

## 5.3 Logical-qubit quality

Useful computation depends more on logical-qubit metrics than raw physical-qubit counts.

Important measures include:

- Logical error rate per gate
- Error rate per cycle
- Number of reliable logical operations
- Logical-qubit lifetime
- Code-cycle speed
- Number of logical qubits
- Fault-tolerant two-qubit gate fidelity
- Magic-state production rate

A system with fewer physical qubits but better logical performance could be more useful than a much larger noisy machine.

## 5.4 Magic-state distillation and non-Clifford gates

Many fault-tolerant algorithms require non-Clifford gates, especially T gates. These are often implemented using magic states, which are expensive to prepare and distill.

For algorithms such as factoring and quantum chemistry, magic-state factories may consume a large fraction of the hardware and energy budget.

This is one reason why physical-qubit estimates can be misleading: the machine may need substantial dedicated infrastructure merely to produce the non-Clifford resources required by the algorithm.

## 5.5 Fast, low-latency classical control

Quantum error correction requires rapid interaction between:

- Qubits
- Measurement electronics
- Decoders
- Control systems
- Cryogenic hardware
- Classical processors

If decoding or feedback is too slow, errors accumulate. A practical architecture requires high-throughput, low-latency classical processing integrated with the quantum processor.

## 5.6 Verification and benchmarking

For many quantum computations, especially sampling tasks, verifying the answer may be as hard as performing the computation.

A useful commercial system must provide:

- Confidence that the result is correct
- Reproducibility
- Error bars
- Detectable failure modes
- Comparisons with classical methods

This is a major issue for quantum advantage claims. A processor can produce outputs that are hard for a classical computer to reproduce—but that does not necessarily prove the outputs are correct.

## 5.7 Algorithmic maturity

The number of known quantum algorithms with strong, practical speedups is limited.

The strongest results usually rely on assumptions such as:

- Efficient quantum access to data
- Sparse or structured inputs
- Fault-tolerant arithmetic
- Special mathematical structure
- Deep circuits

For many proposed applications, the gap between an asymptotic theorem and an end-to-end implementation is large.

## 5.8 Classical competition

Quantum computers are not competing against classical computers from a decade ago. They must outperform:

- GPUs and AI accelerators
- Supercomputers
- Specialized ASICs
- Tensor-network methods
- Monte Carlo techniques
- Approximate optimization
- Quantum-inspired algorithms
- Improved mathematical formulations
- Problem-specific heuristics

Classical algorithms often improve rapidly after a quantum claim is published. This has repeatedly reduced early estimates of quantum advantage.

## 5.9 Data movement and input/output

Quantum algorithms can offer speedups for data already encoded in quantum states. But commercial data is usually classical.

Loading a large classical dataset into a quantum processor may take enough time to eliminate the theoretical gain. Similarly, extracting a complete answer from a quantum state can require many measurements.

This is especially problematic for quantum machine learning and large-scale optimization.

## 5.10 Cost, reliability, and operational complexity

Even if a quantum processor is faster for a subroutine, the overall system may not be economically superior.

Relevant costs include:

- Cryogenic infrastructure
- Lasers or microwave electronics
- Vacuum and photonic systems
- Calibration
- Maintenance
- Error-correction overhead
- Classical co-processing
- Specialist personnel
- Cloud access and queueing
- Energy consumption

A commercial advantage must be measured at the system and workflow level, not just at the gate-operation level.

---

# 6. How close are we?

## Near term: current through approximately 2027

Expected progress:

- Larger and more reliable processors
- Better error mitigation
- Early logical-qubit demonstrations
- Specialized analog and sampling experiments
- More credible application benchmarks
- Continued claims of advantage on artificial tasks

Likely status:

- No broad commercially useful quantum advantage
- Possible niche value in experimentation, secure communications, sensing, and specialized optimization
- Quantum computing primarily used through cloud-access research platforms

## Medium term: approximately 2027–2035

This period could see the first credible application-specific advantages if hardware development succeeds.

Possible early areas:

- Small fault-tolerant chemistry calculations
- Materials and catalyst subproblems
- Quantum simulation of systems beyond classical exact simulation
- Specialized optimization or sampling
- Financial amplitude-estimation demonstrations
- Cryptographic migration pressure, even before cryptanalysis is possible

The key milestone is not a particular physical-qubit count but the availability of **useful logical qubits operating reliably for long circuits**.

## Longer term: mid-2030s and beyond

Potentially transformative applications include:

- Industrial-scale molecular and materials simulation
- Large-scale cryptanalysis
- Fault-tolerant quantum optimization
- High-precision Monte Carlo acceleration
- New quantum algorithms not yet discovered

This timeline is speculative. Hardware progress could be faster than expected, but algorithmic and engineering bottlenecks could also delay useful applications substantially.

---

# 7. What milestones would constitute convincing commercial advantage?

A credible claim should satisfy most of the following:

1. **Relevant problem:** The task matters to an industry or scientific workflow.
2. **Strong classical baseline:** Comparison uses the best practical classical algorithms and hardware.
3. **End-to-end measurement:** Includes data loading, compilation, queueing, error correction or mitigation, and post-processing.
4. **Economic value:** The quantum result improves cost, time, accuracy, or capability.
5. **Scalability:** Advantage persists as the problem grows.
6. **Verification:** Results can be independently checked.
7. **Reproducibility:** Other devices or repeated runs show similar performance.
8. **Operational viability:** The system is reliable and affordable enough to deploy.
9. **Sustained advantage:** It is not erased by a new classical algorithm.
10. **Customer-level impact:** The advantage improves a real product or decision.

Most present “quantum advantage” demonstrations satisfy only the narrower criterion of making a benchmark difficult for classical simulation.

---

# 8. Overall assessment

Quantum computing is no longer merely theoretical. Experimental systems have crossed important thresholds:

- Quantum processors can execute nontrivial circuits.
- Specialized machines can generate samples difficult to reproduce classically.
- Error-correction experiments increasingly show signs of scalability.
- Theoretical algorithms offer potentially enormous advantages for selected problems.

But the central commercial question remains unresolved.

The best current conclusion is:

> Quantum computers have demonstrated computational advantage in narrow, artificial tasks, but they have not yet demonstrated a broadly accepted, economically useful advantage over classical computers on a real commercial workload.

The distance to useful advantage depends on the application:

- **Sampling benchmarks:** Already demonstrated, though not generally useful.
- **Specialized quantum simulation:** Possibly the earliest meaningful application, but still not proven.
- **Optimization:** Uncertain; no general advantage established.
- **Machine learning:** Highly speculative.
- **Finance:** Theoretical speedups exist, but likely require fault tolerance.
- **Cryptanalysis:** Very strong theoretical advantage, but far beyond current hardware.

The decisive technical transition is from noisy physical qubits to large-scale, reliable logical qubits. Until quantum systems can execute long fault-tolerant computations with manageable overhead—and until algorithms can beat highly optimized classical workflows—the commercial value of quantum computing will remain primarily in research, experimentation, and strategic preparation rather than production deployment.

## Selected sources and reference points

- Arute et al., “Quantum supremacy using a programmable superconducting processor,” *Nature* (2019).
- Zhong et al., “Quantum computational advantage using photons,” *Science* (2020).
- Wu et al., “Strong quantum computational advantage using a superconducting quantum processor,” *Physical Review Letters* (2021).
- Google Quantum AI, surface-code error-correction experiments, *Nature* (2023).
- Preskill, work on NISQ-era quantum computing and fault tolerance.
- Shor, factoring and discrete-logarithm quantum algorithms.
- Grover, quantum search algorithm.
- Fowler et al., surface-code architecture and resource estimates.
- Gidney and Ekerå, resource estimates for factoring RSA with a fault-tolerant quantum computer.
- National Academies reports on quantum computing progress and prospects.
- IBM Quantum development-roadmap and processor-performance publications.
- D-Wave technical papers and independent benchmarking literature on quantum annealing.
