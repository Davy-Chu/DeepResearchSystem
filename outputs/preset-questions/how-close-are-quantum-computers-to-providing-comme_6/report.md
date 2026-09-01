# How close are quantum computers to commercially useful advantages?

## Executive summary

Quantum computers have **demonstrated computational advantages over classical computers**, but almost entirely on artificial benchmark problems designed to be difficult for classical simulation. They have **not yet demonstrated a generally accepted, economically valuable advantage on a real commercial task**.

The field is best characterized as follows:

- **Demonstrated quantum advantage:** Yes, for specialized sampling benchmarks such as random-circuit sampling and boson sampling. These experiments show that quantum hardware can perform certain tasks that are infeasible for known classical methods.
- **Demonstrated commercial advantage:** No convincing public demonstration yet.
- **Theoretical or projected advantage:** Strong evidence exists for several areas—quantum chemistry, materials, cryptanalysis, and some linear-algebra or Monte Carlo applications—but these require large numbers of error-corrected logical qubits.
- **Near-term prospects:** Hybrid quantum-classical workflows, quantum simulation, and optimization may produce useful niche results before fully fault-tolerant machines arrive, but evidence remains limited and highly problem-dependent.
- **Main obstacle:** The industry must move from noisy physical qubits to reliable, scalable **fault-tolerant logical qubits**. That requires much better error correction, control, connectivity, software, and system engineering—often by several orders of magnitude.

A reasonable conclusion is:

> Quantum computers are probably several years away from the first narrowly useful commercial advantages, and likely at least a decade away from broad, high-confidence advantages in major industrial applications. The timing is highly uncertain because it depends on whether scalable error correction and manufacturing can be achieved economically.

---

## 1. What counts as “quantum advantage”?

The term is used inconsistently. It is useful to distinguish four levels.

### 1.1 Quantum computational advantage

A quantum processor solves a specified problem faster, or with fewer resources, than the best known classical method.

This does not necessarily imply economic value. A benchmark may be deliberately constructed to favor a quantum processor and have no practical application.

### 1.2 Quantum utility

A quantum computer produces a result that is scientifically useful or more accurate than an available approximate method, even if a classical computer can still solve the problem faster or more cheaply.

Examples might include improved estimates of molecular properties, better modeling of a material, or a useful optimization solution.

### 1.3 Commercial advantage

A quantum system delivers a measurable benefit—such as lower cost, higher accuracy, faster design cycles, or better investment returns—on a real customer problem.

The comparison must include:

- Classical hardware and software costs
- Quantum hardware access and queueing
- Error mitigation or error correction overhead
- Data-loading and readout costs
- Engineering and integration costs
- Reliability and repeatability
- The value of the improved answer

### 1.4 Broad or general-purpose advantage

A quantum computer provides economically meaningful benefits across a substantial class of industrial problems. No such advantage has been demonstrated.

---

# 2. What has actually been demonstrated?

## 2.1 Random-circuit sampling

The clearest demonstrations involve **random-circuit sampling**: a quantum processor executes a large random circuit, and the output distribution is sampled. Classical computers can verify small instances, but simulation becomes exponentially harder as circuit depth and qubit count increase.

### Google Sycamore

In 2019, Google reported that its 53-qubit Sycamore processor completed a random-circuit sampling task in about 200 seconds that Google estimated would take a classical supercomputer thousands of years.

The claim was important but narrow:

- The task was not commercially useful.
- It was designed as a benchmark.
- Classical algorithms rapidly improved after publication.
- The estimated classical runtime was revised downward substantially by competing researchers.

The experiment demonstrated a computational separation for a particular sampling task, not an advantage in business or science.

### Chinese photonic and superconducting experiments

In 2020, researchers associated with the University of Science and Technology of China reported large demonstrations of:

- **Gaussian boson sampling** using photons
- **Random-circuit sampling** using superconducting qubits

These experiments extended the size of sampling problems that were difficult to reproduce classically. As with Sycamore, the results were significant evidence of quantum computational capability, but the benchmark itself lacked a direct commercial application.

### Google Willow

In 2024, Google reported results from its Willow processor showing **below-threshold quantum error correction**: increasing the size of the error-correcting code reduced the logical error rate. Google also reported a random-circuit sampling result that it estimated would take a classical supercomputer an extremely long time.

The important part of the Willow result was not the benchmark runtime. It was evidence that the system had crossed an important error-correction threshold: larger encoded qubits could become more reliable rather than less reliable.

However, Willow was not a fault-tolerant, commercially useful quantum computer. It demonstrated progress toward scalable error correction, not a practical industrial advantage.

---

## 2.2 Boson sampling

Boson sampling uses photons passing through interferometers. Certain output distributions are believed to be classically hard to sample efficiently.

Experiments from groups in China, Canada, and elsewhere have produced increasingly large boson-sampling demonstrations. They establish that photonic systems can generate distributions beyond the reach of straightforward classical simulation.

Limitations include:

- The task is not itself a standard business application.
- Verification becomes difficult as the system grows.
- Classical simulation algorithms and approximations continue to improve.
- Loss, distinguishability of photons, and sampling noise complicate claims.

Boson sampling is strong evidence for specialized quantum computational power, but weak evidence for near-term commercial value.

---

## 2.3 Quantum simulation experiments

Quantum simulation is the area most naturally matched to quantum hardware. A quantum system can represent another quantum system without the severe exponential overhead that often affects classical simulation.

Experiments have demonstrated:

- Small molecular and material simulations
- Spin-system dynamics
- Fermi-Hubbard-type models
- Lattice gauge theory components
- Quantum dynamics and phase transitions
- Variational estimates of molecular energies

These experiments are scientifically meaningful, but most have not shown a decisive end-to-end advantage over the best classical chemistry, materials, or physics methods.

The key issue is scale and accuracy. A demonstration involving a small molecule may be reproducible classically. Industrial applications often require:

- Chemical accuracy
- Large active spaces
- Correlation effects
- Finite-temperature behavior
- Nuclear motion
- Open-system effects
- High confidence in energy differences or reaction rates

Current noisy systems generally cannot deliver all of these requirements simultaneously.

---

## 2.4 Optimization and machine learning

Quantum optimization has received substantial commercial attention. Proposed applications include:

- Vehicle routing
- Scheduling
- Portfolio optimization
- Supply-chain design
- Manufacturing
- Traffic management
- Staffing and resource allocation
- Machine learning

The main approaches include quantum annealing, the Quantum Approximate Optimization Algorithm, quantum-inspired classical algorithms, and hybrid variational methods.

### Current status

There are many demonstrations that quantum devices can produce good solutions to small or specially structured problems. However, there is no broadly accepted evidence that they outperform strong classical optimization methods on commercially relevant instances after accounting for:

- Problem encoding
- Embedding overhead
- Parameter tuning
- Repeated sampling
- Classical preprocessing and postprocessing
- Hardware access time
- Solution quality rather than just runtime

D-Wave has reported performance advantages for particular annealing workloads, and some customers use quantum annealers experimentally. Nevertheless, these claims remain highly problem-specific, and classical algorithms often close or eliminate the apparent advantage.

Optimization may ultimately be valuable, but it is not currently a demonstrated general quantum advantage.

---

## 2.5 Quantum machine learning

Quantum machine learning is theoretically attractive because some quantum algorithms can manipulate high-dimensional vectors or probability distributions efficiently.

In practice, current evidence is weak:

- Data loading can remove the theoretical speedup.
- Classical neural networks are extremely competitive.
- Quantum models can be difficult to train.
- Noise limits circuit depth.
- Many proposed advantages assume quantum-accessible data or special mathematical structure.

There is no accepted commercial quantum machine-learning advantage today.

---

# 3. Theoretical and projected advantages

## 3.1 Quantum chemistry and materials

This is generally considered the strongest long-term application area.

Quantum systems naturally encode molecules and materials. Algorithms such as:

- Quantum phase estimation
- Variational quantum eigensolvers
- Quantum imaginary-time evolution
- Block-encoding and quantum singular-value transformation
- Fault-tolerant Hamiltonian simulation

could eventually calculate molecular energies, reaction rates, electronic structures, and material properties more efficiently than classical approaches.

Potential commercial uses include:

- Drug discovery
- Catalysts
- Fertilizers
- Batteries
- Solar materials
- Carbon-capture chemistry
- Superconducting materials
- Industrial process chemistry

### Why the advantage is plausible

For general interacting quantum systems, classical simulation can require resources that grow exponentially with system size. Fault-tolerant quantum computers may represent the same systems with polynomial resource growth.

### Why it is not yet demonstrated

Useful chemistry calculations typically need:

- Thousands to millions of logical operations per useful result
- Low logical error rates
- Accurate phase estimation or equivalent methods
- Many logical qubits
- Efficient state preparation
- Fault-tolerant arithmetic
- Better algorithms for realistic molecules

Current noisy processors are generally far below these requirements.

---

## 3.2 Shor’s algorithm and cryptanalysis

A sufficiently large fault-tolerant quantum computer could factor large integers and solve discrete logarithms using Shor’s algorithm. This threatens:

- RSA
- Diffie–Hellman
- Elliptic-curve cryptography
- Some public-key infrastructure
- Digital signatures

This is a clear theoretical advantage, not a projected speedup based on uncertain heuristics. The challenge is resource scale.

Estimates vary widely depending on:

- Hardware error rates
- Code choice
- Gate speed
- Parallelism
- Circuit optimization
- Target cryptographic key
- Desired runtime

A useful attack on RSA-2048 is commonly estimated to require **hundreds of thousands to millions of physical qubits**, and potentially millions more under conservative assumptions. It would also require a large number of logical qubits operating for a long time.

No current device is close to this capability. But the threat is serious because encrypted data can be harvested now and decrypted later. Governments and companies are therefore migrating toward post-quantum cryptography before a cryptographically relevant quantum computer exists.

---

## 3.3 Quantum amplitude estimation and Monte Carlo

Many financial, engineering, and scientific calculations rely on Monte Carlo sampling. Quantum amplitude-estimation algorithms can, in ideal fault-tolerant settings, improve the error scaling from approximately

\[
O(1/\epsilon^2)
\]

to

\[
O(1/\epsilon),
\]

where \(\epsilon\) is the desired estimation error.

Potential applications include:

- Derivative pricing
- Risk analysis
- Value-at-risk calculations
- Insurance
- Portfolio analytics
- Reliability engineering
- Numerical integration
- Fluid and financial simulations

The advantage is theoretically strong, but implementation requires:

- Fault-tolerant circuits
- Efficient state preparation
- Oracle construction
- Large numbers of repeated logical operations
- Careful treatment of data and model representation

Near-term demonstrations using simplified finance models should not be confused with commercial advantage.

---

## 3.4 Linear algebra and quantum machine learning

Quantum algorithms for linear systems, matrix operations, search, and sampling can show large asymptotic speedups under strong assumptions.

Typical assumptions include:

- Sparse or structured matrices
- Efficient quantum state preparation
- Efficient access to data through an oracle or quantum memory
- Low condition numbers
- Ability to extract only a compact statistic from the answer

Those assumptions are difficult to satisfy in practical data-processing pipelines. Reading out a full classical answer can eliminate the speedup.

Thus these algorithms remain promising but speculative for most commercial data workloads.

---

## 3.5 Search and combinatorial problems

Grover’s algorithm provides a quadratic speedup for unstructured search. This is real but modest compared with the exponential speedups associated with Shor’s algorithm or quantum simulation.

A quadratic speedup can still be valuable at very large scale, but only if:

- The search oracle is efficient
- The problem is genuinely unstructured
- The quantum computer can run sufficiently deep circuits
- Classical preprocessing does not dominate

There is no current commercial demonstration of Grover-style advantage.

---

# 4. The largest remaining technical barriers

## 4.1 Quantum error correction

The central problem is that quantum states are fragile. Errors arise from:

- Environmental noise
- Control imperfections
- Crosstalk
- Leakage outside the computational basis
- Measurement errors
- Frequency drift
- Thermal effects
- Photon loss
- Fabrication variation

Quantum error correction distributes one logical qubit across many physical qubits. But the overhead can be enormous.

A practical computer needs:

1. Physical error rates below the fault-tolerance threshold  
2. Error correction that actually lowers logical error rates as code size increases  
3. Fast syndrome measurement  
4. Real-time decoding  
5. Logical gates with low overhead  
6. Reliable state preparation and measurement  
7. Fault-tolerant memory lasting long enough for algorithms  

Recent experiments have shown important milestones, including below-threshold surface-code behavior and increasingly reliable logical qubits. But a few logical qubits are very different from a machine with thousands or millions of useful logical qubits.

---

## 4.2 Physical-to-logical qubit overhead

A logical qubit may require anywhere from hundreds to many thousands of physical qubits, depending on:

- Physical gate fidelity
- Connectivity
- Error bias
- Code family
- Algorithm depth
- Target logical error rate
- Required operating time

For chemistry, cryptography, and amplitude estimation, the number of logical qubits may need to range from hundreds to millions depending on the problem and algorithm. The physical system may therefore need millions or more high-quality qubits.

This is not merely a matter of increasing the qubit count. The entire system must support:

- Dense wiring
- Cryogenics or vacuum
- Control electronics
- Fast feedback
- Error-decoding hardware
- Calibration
- Heat management
- Manufacturing yield

---

## 4.3 Circuit depth and algorithmic overhead

Many theoretically promising algorithms require long sequences of gates. Current devices can execute only relatively shallow circuits before noise overwhelms the result.

The practical resource estimate must include:

- Number of logical qubits
- Number of logical gates
- T-gate or non-Clifford overhead
- Magic-state distillation
- Ancillary qubits
- State preparation
- Measurement repetitions
- Error-correction cycles
- Classical decoding

A headline qubit count without circuit-depth and error-rate information is not enough to assess usefulness.

---

## 4.4 Scaling and manufacturing

Different hardware platforms face different scaling challenges.

### Superconducting qubits

Strengths:

- Fast gates
- Mature microfabrication
- Large demonstrated processors

Challenges:

- Cryogenic wiring
- Crosstalk
- Frequency collisions
- Calibration complexity
- Relatively short coherence times
- Two-dimensional connectivity constraints

### Trapped ions

Strengths:

- Very high gate fidelities
- Long coherence times
- Flexible connectivity

Challenges:

- Slower gates
- Difficult scaling of large ion chains
- Laser and control complexity
- Shuttling and modular networking

### Neutral atoms

Strengths:

- Large arrays
- Reconfigurable connectivity
- Promising scalability

Challenges:

- Laser control
- Atom loss
- Gate fidelity
- Cooling and loading
- Error correction at scale

### Photonics

Strengths:

- Potentially room-temperature computation and communication
- Natural suitability for networking
- Large optical modes

Challenges:

- Photon loss
- Nondeterministic interactions
- Source and detector quality
- Large resource overhead
- Fault-tolerant photonic architectures

### Semiconductor spin qubits

Strengths:

- Potential compatibility with semiconductor manufacturing
- Small physical footprint
- Long-term integration potential

Challenges:

- Device variability
- Control complexity
- Readout
- Wiring and yield
- Limited large-scale demonstrations

No platform has yet established a decisive scaling advantage.

---

## 4.5 Useful quantum algorithms remain difficult to implement

Theoretical speedups often depend on assumptions that are hard to realize. For example:

- Data must be loaded into quantum states efficiently.
- The quantum oracle must be built without negating the speedup.
- The output may be a global statistic rather than a full solution.
- Error correction must be included in the runtime.
- The classical baseline must be the best modern algorithm, not a weak reference implementation.

There is a substantial gap between asymptotic algorithmic complexity and end-to-end application performance.

---

## 4.6 Benchmarking and classical competition

Quantum claims are unusually vulnerable to moving baselines. Classical researchers can often improve:

- Tensor-network simulations
- Monte Carlo methods
- Approximate sampling
- GPU implementations
- Specialized heuristics
- Quantum-inspired algorithms

As a result, an experiment that appears to exceed classical capability may later be simulated or approximated more efficiently.

A credible advantage claim must specify:

- The best known classical algorithm
- Hardware and energy assumptions
- Exact versus approximate accuracy
- Total wall-clock time
- Preprocessing and postprocessing
- Verification cost
- Problem-size scaling

---

## 4.7 Software, compilers, and error mitigation

Current machines require substantial calibration and optimization. Useful operation depends on:

- Hardware-aware compilation
- Pulse-level control
- Scheduling
- Crosstalk management
- Error mitigation
- Automatic calibration
- Runtime feedback
- Hybrid classical orchestration

Error mitigation can extend the usefulness of noisy processors, but it often increases the number of circuit executions dramatically and does not provide the same guarantees as error correction.

---

## 4.8 Economics and system-level integration

Even if a quantum processor has an algorithmic speedup, it must beat a complete classical solution.

Commercial deployment requires:

- High utilization
- Low latency or predictable scheduling
- Stable operation
- Reproducibility
- Security
- Integration with classical data systems
- Acceptable capital and operating costs
- Technical support
- Clear return on investment

A quantum computer that needs hours of calibration, specialized cryogenics, and extensive algorithm tuning may be valuable for research but not competitive for ordinary enterprise workloads.

---

# 5. How close are the main application areas?

| Application | Current status | Likely requirement for clear advantage | Assessment |
|---|---|---|---|
| Random-circuit and boson sampling | Demonstrated specialized advantage | No commercial requirement | Real quantum advantage, little direct business value |
| Quantum chemistry | Small demonstrations, no decisive advantage | Fault-tolerant logical qubits and deep circuits | One of the strongest long-term candidates |
| Materials science | Early simulations | Larger accurate simulations with validated predictions | Promising but not yet practical |
| Cryptanalysis | Theoretical advantage | Large fault-tolerant machine | Technically plausible, not imminent |
| Finance Monte Carlo | Theoretical asymptotic advantage | Fault tolerance and efficient state preparation | Interesting, but heavily assumption-dependent |
| Optimization | Many experiments, no consensus advantage | Problem-specific proof against strong classical baselines | Uncertain |
| Machine learning | Mostly theoretical or exploratory | Data-loading and training advantage | Currently weak evidence |
| Drug discovery | Mostly indirect chemistry opportunity | Accurate molecular and materials calculations | Potentially significant, but not near-term proven |
| Energy and industrial chemistry | Strong theoretical motivation | Fault-tolerant simulation | High-value long-term target |
| Quantum networking | Early demonstrations | Repeaters, memories, error correction | Important infrastructure, not yet a computational advantage |

---

# 6. Commercial timelines

Predictions vary widely, but the technology can be divided into stages.

## Stage 1: NISQ experimentation — now

Current processors are useful for:

- Algorithm development
- Hardware research
- Education
- Benchmarking
- Small scientific simulations
- Error-mitigation experiments
- Proof-of-concept customer projects

They generally do not provide a reliable economic advantage.

## Stage 2: Early logical-qubit systems — possibly late 2020s to early 2030s

The key milestone will be systems with:

- Multiple high-quality logical qubits
- Repeated below-threshold error correction
- Demonstrated logical operations
- Useful algorithmic depth
- Reduced calibration and operating costs

These systems may enable narrow scientific utility, especially in simulation, but it is uncertain whether they will beat classical alternatives.

## Stage 3: Early fault-tolerant applications — roughly 2030s, highly uncertain

Potential first advantages could appear in:

- Specialized chemistry
- Materials modeling
- Cryptographic research
- Structured simulation
- Selected Monte Carlo problems

The first advantage may be narrow and expensive rather than a general-purpose computing breakthrough.

## Stage 4: Broad commercial deployment — 2030s or later

Large-scale fault-tolerant machines could eventually support:

- Industrial chemistry
- Drug discovery
- New materials
- Large-scale risk analysis
- Cryptanalysis
- Complex physical simulation

Whether this occurs in the 2030s, 2040s, or later remains uncertain. Hardware roadmaps are ambitious, but the gap between prototype demonstrations and economically useful machines is substantial.

---

# 7. How to interpret company claims

Companies often use terms such as:

- Quantum advantage
- Quantum utility
- Quantum supremacy
- Production-ready
- Fault tolerant
- Enterprise-ready
- Quantum-inspired advantage

These terms should be evaluated carefully.

A meaningful claim should answer:

1. What exact problem was solved?
2. Was the problem commercially relevant?
3. What is the best classical baseline?
4. Were all overheads included?
5. Was the result exact or approximate?
6. How does performance scale with problem size?
7. Is the result reproducible?
8. Does the quantum system improve cost, speed, accuracy, or revenue?
9. Does it work without extensive human tuning?
10. Can the result be integrated into an existing workflow?

A benchmark speedup without economic value is still scientifically important, but it should not be described as commercial advantage.

---

# 8. Overall assessment

Quantum computing has crossed an important scientific threshold: quantum processors have performed specialized computations that are infeasible for classical machines under reasonable assumptions. This is a genuine achievement.

It has not crossed the more important commercial threshold. There is currently no broadly accepted demonstration that a quantum computer:

- Solves a real industrial problem
- Beats the best classical method
- Includes all costs and overheads
- Produces a repeatable economic benefit

The most credible path to commercial value is **fault-tolerant quantum simulation**, especially for chemistry and materials. Cryptanalysis is another clear theoretical application, although it is more a future security requirement than a near-term business opportunity. Optimization and machine learning may produce useful niche results, but their advantages are less theoretically robust and more vulnerable to classical competition.

The single most important indicator to watch is not raw qubit count. It is the production of **large numbers of high-quality logical qubits with low error rates, useful gate speeds, and manageable overhead**. Other important indicators are:

- Below-threshold logical error rates at increasing code sizes
- Logical qubits operating for long computations
- Fault-tolerant non-Clifford gates
- End-to-end application demonstrations
- Comparisons against strong, current classical systems
- Reproducible economic benefits

## Bottom line

Quantum computers are **already capable of narrow, benchmark-defined quantum advantage**, but they are **not yet providing commercially useful general advantages over classical computers**. The field is likely in the transition from scientific proof-of-principle to engineering scale-up. The earliest credible commercial benefits may emerge in specialized applications within the next decade, but broad and economically decisive advantages depend on solving fault tolerance, scaling, algorithmic overhead, and system economics—problems that remain unresolved.

## Selected sources and reference points

- Arute et al., “Quantum supremacy using a programmable superconducting processor,” *Nature*, 2019.
- Zhong et al., “Quantum computational advantage using photons,” *Science*, 2020.
- Wu et al., “Strong quantum computational advantage using a superconducting quantum processor,” *Physical Review Letters*, 2021.
- Google Quantum AI, “Suppressing quantum errors by scaling a surface code logical qubit,” *Nature*, 2023.
- Google Quantum AI, “Quantum error correction below the surface code threshold,” and Willow processor announcements, 2024.
- Preskill, “Quantum Computing in the NISQ era and beyond,” *Quantum*, 2018.
- National Academies of Sciences, Engineering, and Medicine, *Quantum Computing: Progress and Prospects*, 2019.
- Gidney and Ekerå, “How to factor 2048-bit RSA integers in 8 hours using 20 million noisy qubits,” *Quantum*, 2021.
- National Institute of Standards and Technology, post-quantum cryptography standardization publications, 2024.
- McKinsey, BCG, and other industry analyses of quantum-computing commercialization, which provide useful market context but should be treated as forecasts rather than evidence of achieved advantage.