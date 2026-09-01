# Research Report

## Research Question

How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

## Summary

This is an automatically generated incomplete report. The research run ended with stop reason `max_iterations`, and normal finalization did not complete during OpenAI Ledger Report Generation. The validated findings collected before that point are preserved below without claiming that the evidence is complete.

## Findings

### Finding 1

**Claim**

S2 reports a 3,000-times wall-clock speedup for a fermionic-simulation materials-engineering task using an IBM quantum computer augmented with compiler and error-suppression software, while claiming practically relevant runtime and accuracy at least matching existing tooling.

**Confidence:** Low

**Why this confidence level**

The source directly makes the claim, but it is a vendor-authored technical blog dated May 2026, presents a promotional announcement, and the supplied excerpt does not provide independent replication, full benchmarking details, or enough information to assess whether the classical baseline was the strongest relevant alternative.

**Evidence**

- Q-CTRL states that its demonstration used an IBM quantum computer and infrastructure software to run an existing fermionic-simulation algorithm, reporting more than 3,000× faster wall-clock performance than an industry-standard classical alternative with comparable or better accuracy. [S2]

### Finding 2

**Claim**

The reported S2 demonstration, even if its benchmark comparison is accepted, is evidence for a specific application-level or practical-advantage claim rather than proof of broad quantum advantage across commercially important workloads.

**Confidence:** High

**Why this confidence level**

Independent reporting reinforces that a measured or classically hard task should not be generalized to broad commercial advantage.

**Evidence**

- S2 defines practical quantum advantage as outperforming the best available conventional alternative on a real-world application and contrasts this with Google's 2019 supremacy demonstration, which it characterizes as lacking commercial relevance. [S2]
- C&EN characterizes the IBM results as niche demonstrations and distinguishes classically hard sampling or quantum-phenomena experiments from useful modeling performance. [S6]
- IEEE Spectrum distinguishes calculations without a classical counterpart from the broader and harder question of what counts as advantage. [S8]

### Finding 3

**Claim**

Theoretical and projected quantum advantages are concentrated in selected problem classes—especially quantum-system simulation—and do not imply that quantum computers will outperform classical computers on ordinary small or moderate business problems.

**Confidence:** Medium

**Why this confidence level**

S4 provides an expert-framework characterization, while S5 supplies a forward-looking industry analysis and S3 gives generic application claims. None establishes broad practical superiority experimentally.

**Evidence**

- MIT Sloan reports a framework concluding that small- to moderate-sized problems generally will not benefit, while problems with exponential algorithmic gains or very large datasets may benefit; it gives simulation, drug discovery, optimization, and financial-pattern examples as potential application areas. [S4]
- S5 projects a narrow and uneven advantage map concentrated in applications aligned with quantum simulation, while stating that supply-chain optimization, machine learning, and derivatives pricing have no demonstrated advantage in its projected scenario. [S5]
- S3 describes optimization, cryptography, and large-scale simulation as potential application areas, but presents these as general potential rather than measured commercial results. [S3]

### Finding 4

**Claim**

Commercial usefulness depends on comparison against the actual available or comparably priced classical alternative, including runtime and cost, rather than on asymptotic complexity or the ability to solve a contrived benchmark.

**Confidence:** High

**Why this confidence level**

The additional source explicitly includes efficiency, cost-effectiveness, and accuracy alongside comparison with leading classical methods.

**Evidence**

- MIT Sloan describes 'quantum economic advantage' as solving a problem faster with a comparably priced quantum computer than with a classical computer and notes that classical machines may have faster processing despite less efficient algorithms. [S4]
- S2 distinguishes theoretical absolute advantage from practical advantage against the best available conventional alternative on a meaningful real-world task. [S2]
- IBM's advantage framework requires measurable separation in efficiency, cost-effectiveness, accuracy, or a combination, and tracks candidates against leading classical methods. [S9]

### Finding 5

**Claim**

The supplied sources identify noise, errors, decoherence, and the hardware/software needed for complex error-tolerant computation as major barriers to useful quantum applications.

**Confidence:** High

**Why this confidence level**

The new sources add several direct descriptions of error accumulation, validation, connectivity, circuit depth, and classical-quantum integration as barriers, though application-specific thresholds remain unresolved.

**Evidence**

- S2 states that hardware size and errors degrade performance and cause algorithms to fail, and that noise and errors have limited useful results on relevant problems. [S2]
- S3 explains that quantum systems are sensitive to temperature, electromagnetic interference, and vibration, and require specialized operating conditions and repeated runs with statistical analysis. [S3]
- MIT Sloan reports that hardware and software for the most complex problems may not be available until 2035 or later, according to the cited estimate. [S4]
- The reported demonstrations rely on spacetime codes, error detection, fidelity bounds, and error-mitigation techniques because verification and accumulated errors become limiting in classically hard circuits. [S7]
- IBM identifies hardware performance, gate errors, connectivity, SWAP overhead, circuit depth, and software as requirements for scaling advantage. [S9]
- C&EN reports that increasing non-Clifford T gates increases noise and can render outputs meaningless, while current systems remain noisy and error prone. [S6]

### Finding 6

**Claim**

A projected 2,000-logical-qubit, fault-tolerant machine executing approximately one billion error-corrected operations is presented by S5 as potentially useful for selected chemistry, pharmaceutical, and catalysis workloads by 2033, but this is a forecast rather than a demonstrated capability.

**Confidence:** Low

**Why this confidence level**

S5 is a forward-looking industry article; the excerpt provides projections and linked resource estimates but no demonstrated machine or independent validation of the commercial outcomes.

**Evidence**

- S5 describes a hypothetical 2033 machine with 2,000 logical qubits and one billion error-corrected operations, and projects useful applications in molecular simulation, drug metabolism, and catalysis under that scenario. [S5]

### Finding 7

**Claim**

IBM and collaborators report three 2026 demonstrations on Heron processors involving doped-Clifford sampling, quantum-magnet/Floquet-dynamics experiments, and validated quantum computations; the demonstrations are presented as producing results beyond leading classical simulations or as classically hard computations with built-in validation, but the papers were supplied as preprints rather than peer-reviewed publications.

**Confidence:** High

**Why this confidence level**

The new sources add detailed scale, runtime, validation, and comparison information and independently qualify the claims. The demonstrations are well supported as reported preprint results, although their broader commercial significance remains unestablished.

**Evidence**

- C&EN reports three IBM Heron R3 demonstrations and describes the sampling experiment as reaching 468 T gates, where no known classical algorithm could simulate the model, while noting that the papers were preprints and that classical reproduction cannot be absolutely ruled out. [S6]
- IBM describes three papers reporting advantage demonstrations using doped Clifford sampling, spacetime codes, and validated error-mitigation techniques, including a 70-logical-qubit computation and experiments up to 74 qubits. [S7]
- IEEE Spectrum reports IBM's claim that three results validated calculations out of reach of classical computers and describes the demonstrations as using new validation techniques on a 156-qubit Heron processor. [S8]
- QCR reports the three demonstrations, their hardware scales, classical comparison methods, validation frameworks, and public circuit repositories. [S11]
- IBM reports the University of Chicago demonstration as a structured hard-sampling computation with built-in error detection, 70 logical qubits, and approximately 15 minutes of execution. [S12]
- The fact-check confirms that the papers are preprints and details the 70-qubit experiment's 468 T gates, 10-fold error suppression, certified fidelity lower bound, and unresolved possibility of improved classical methods. [S13]

### Finding 8

**Claim**

The reported 2026 IBM demonstrations are evidence of narrow, task-specific beyond-classical performance or classically hard computation, not evidence of commercially useful advantage across general workloads.

**Confidence:** High

**Why this confidence level**

The sources consistently distinguish classically hard or beyond-classical demonstrations from useful application-level advantage. This conclusion is about characterization and scope, not a claim that the demonstrations lack scientific significance.

**Evidence**

- C&EN characterizes the demonstrations as applying to certain niche problems, says current quantum computers remain noisy and error prone, and reports that classical computers still outperform them at modeling. [S6]
- IBM states that quantum advantage requires validated quantum computation plus measurable separation in efficiency, cost-effectiveness, accuracy, or a combination, and frames the demonstrations as part of an ongoing tracker rather than a completed commercial milestone. [S7]
- IEEE Spectrum describes the results as calculations without a classical counterpart but emphasizes that defining advantage is difficult and reports them as IBM claims rather than as established commercial superiority. [S8]
- IBM's 2019 comparison argues that Google's random-circuit result should not be treated as proof of broad supremacy because a different classical simulation reduced the estimated runtime to 2.5 days and had higher fidelity. [S10]

### Finding 9

**Claim**

IBM's 2025 advantage framework treated rigorous validation and demonstrable separation in efficiency, cost-effectiveness, or accuracy as unmet criteria for its candidate advantage experiments, indicating that candidate demonstrations and validated beyond-classical results do not automatically establish practical advantage.

**Confidence:** High

**Why this confidence level**

The new source reinforces the distinction between IBM's practical-advantage criteria and the later demonstrations, while preserving the documented conflict between IBM's 2025 and 2026 characterizations.

**Evidence**

- IBM says its 2025 candidate experiments had not yet achieved advantage because they lacked both rigorous validation and demonstrable quantum separation measured by efficiency, cost-effectiveness, accuracy, or a combination. [S9]
- S13 emphasizes that IBM's three papers operate at different evidentiary levels, that the tracker treats the entries as active candidates requiring further benchmarking, and that the later claims do not uniformly establish practical advantage. [S13]

### Finding 10

**Claim**

The 2026 validation demonstrations improve evidence that noisy quantum computations can be trusted in classically hard regimes, but they do not demonstrate fault-tolerant, commercially useful computation at application-relevant scale.

**Confidence:** High

**Why this confidence level**

The new sources directly establish improved verification without demonstrating fault-tolerant, application-scale commercial computation.

**Evidence**

- IBM reports that spacetime-code validation produced a rigorous lower bound on logical-computation fidelity, reduced effective gate error by roughly 10×, and enabled a 70-logical-qubit computation. [S7]
- IEEE Spectrum reports that the demonstrations provided good evidence of correctness for calculations without a classical counterpart, while presenting them as validation techniques rather than commercial applications. [S8]
- C&EN reports a measured fidelity of approximately 32% for the reference calculation and an estimated lower bound of 28.4% after adding T gates, while noting that present systems remain noisy and error prone. [S6]
- QCR describes verification and error reduction in the 70-logical-qubit experiment but presents no application-level commercial benchmark or fault-tolerant scaling result. [S11]
- IBM characterizes the experiment as a milestone toward scaling and emphasizes error correction and trust rather than reporting commercially useful application performance. [S12]
- S13 explicitly states that the 70 data qubits are error-detected rather than fault-tolerant logical qubits and that the result does not settle scaling or practical advantage. [S13]

### Finding 11

**Claim**

Scaling toward useful advantage requires simultaneously improving physical error rates, validation and error correction, circuit depth, connectivity, and the integration of quantum processors with classical computation; improved qubit count alone is insufficient.

**Confidence:** High

**Why this confidence level**

The sources broaden and concretize the barrier set, including the distinction between error-detected demonstrations and fault-tolerant scaling, without undermining the existing claim.

**Evidence**

- IBM describes spacetime-code validation, noisy non-Clifford gates, and classical validation infrastructure as central to trusted computation beyond classical verification. [S7]
- IBM identifies high-performing hardware as necessary and links square topology and more couplers to fewer SWAP gates and more complex circuits; it also emphasizes software and classical-quantum system performance. [S9]
- C&EN explains that added T gates increase computational power but also accumulate errors, and reports that current machines remain noisy and lose information. [S6]
- S13 identifies verification, non-Clifford-gate error accumulation, heuristic error mitigation, connectivity and classical-simulation comparisons as unresolved issues affecting claims of advantage. [S13]
- QCR links useful scaling to error detection, classical benchmarking, cross-platform validation, noise stability, and quantum–classical software integration. [S11]

### Finding 12

**Claim**

The three 2026 IBM-associated demonstrations have materially different evidentiary strengths: the IBM–University of Chicago doped-Clifford experiment makes a complexity-based beyond-classical claim with a device-dependent fidelity certificate, whereas the Qedma Floquet and Algorithmiq Loschmidt-echo studies primarily report empirical failure or disagreement among tested classical methods and rely partly on error-mitigation or heuristic assumptions.

**Confidence:** High

**Why this confidence level**

The distinction is explicitly made by an independent analytical source and is consistent with the reported methods and comparisons in the ecosystem summary.

**Evidence**

- The fact-check distinguishes the flagship doped-Clifford result, which combines hardness arguments with a device-dependent fidelity certificate, from the Qedma and Algorithmiq papers, which make empirical claims about unreliable or conflicting classical methods. [S13]
- The source presents three demonstrations with different classical comparisons and validation methods: spacetime-code validation, Fugaku benchmarking with cross-platform checks, and process validation across IBM processors. [S11]

### Finding 13

**Claim**

The 70-qubit doped-Clifford demonstration used error-detected encoded data qubits rather than fault-tolerant logical qubits of the type assumed in large-scale fault-tolerant resource estimates; its reported 10-fold error suppression and approximately 15–16 minute execution therefore do not establish scalable fault-tolerant operation.

**Confidence:** High

**Why this confidence level**

S13 directly clarifies the logical-versus-error-detected distinction, while S12 independently supplies the scale and runtime figures. Neither source reports fault-tolerant application-scale operation.

**Evidence**

- S13 states that IBM's 70 'logical qubits' are error-detected data qubits, not fault-tolerant logical qubits, and reports roughly 10-fold effective error suppression, a 0.284 fidelity lower bound, and 16.1 minutes of QPU execution. [S13]
- IBM reports 70 logical qubits, 2,415 logical two-qubit operations, 468 T gates, and approximately 15 minutes, while describing the result as an error-correction and trust milestone rather than a commercial application. [S12]

## Conflicts and Uncertainty

- Evidence concerning ledger claim C9 is conflicting: IBM's 2025 advantage framework treated rigorous validation and demonstrable separation in efficiency, cost-effectiveness, or accuracy as unmet criteria for its candidate advantage experiments, indicating that candidate demonstrations and validated beyond-classical results do not automatically establish practical advantage. [S9] [S13] [S7]

## Remaining Gaps

- No independent, peer-reviewed or replicated evidence is supplied to verify S2's reported 3,000× speedup, the quality of its classical baseline, total cost, reproducibility, or commercial return.
- The sources do not provide a current, quantitative comparison between available hardware and application-specific requirements such as physical-to-logical-qubit overhead, logical error rates, circuit depth, runtime, data loading, connectivity, and total system cost.
- The projected application advantages in chemistry, pharmaceuticals, catalysis, batteries, optimization, cryptography, and finance lack sufficiently detailed assumptions about problem size, classical alternatives, error rates, input/output costs, and economic value to establish when they will become commercially superior.
- The supplied evidence does not systematically prioritize technical barriers by application category or establish a supported timeframe for broad commercial quantum advantage.
- The 2026 IBM demonstrations lack supplied independent replication and a complete, independently audited comparison with the strongest classical algorithms, including total quantum-plus-classical runtime, cost, sampling quality, reproducibility, and application-level value.
- The new validation results do not establish the physical-to-logical-qubit overhead, logical error rates, sustained circuit throughput, or resource requirements needed to determine whether the reported 70-logical-qubit and related demonstrations can scale to commercially relevant chemistry or materials workloads.
- For the Qedma Floquet and Algorithmiq Loschmidt-echo demonstrations, the supplied evidence does not establish quantitative accuracy against a known ground truth at the hardest scales: Qedma's extrapolated mitigation may introduce bias, while Algorithmiq's global-rescaling estimate lacks a quantitative error bound.
- SQ1: What quantum-computing demonstrations have established a measured advantage over classical computers, and how should that advantage be characterized in terms of task, comparison baseline, scale, reproducibility, and practical usefulness? (CONFLICTING: At least one linked ledger claim contains conflicting evidence.)
- SQ2: What commercially relevant quantum-computing applications show theoretical or projected advantages over classical methods, and what assumptions determine whether those advantages could materialize? (PARTIAL: At least one linked ledger claim is not yet supported.)
- SQ3: How close are current quantum computers to delivering commercially useful advantages, considering present hardware capabilities and the requirements of leading candidate applications? (PARTIAL: At least one linked ledger claim is not yet supported.)
- SQ4: What are the biggest remaining technical barriers to commercially useful quantum advantage, and which barriers are most decisive for different application categories? (PARTIAL: At least one linked ledger claim is not yet supported.)
- SQ5: How do claims of quantum advantage vary across definitions of 'advantage' and 'commercially useful,' and what uncertainty or caveats should qualify the overall assessment? (CONFLICTING: At least one linked ledger claim contains conflicting evidence.)

## Conclusion

The findings above reflect the evidence validated before the run ended. They should be treated as provisional because normal final synthesis did not complete and important gaps may remain.

## Sources

- [S1] Quantum computing - Wikipedia — https://en.wikipedia.org/wiki/Quantum_computing
- [S2] Practical quantum advantage signals a new commercial era for quantum computing | Q-CTRL — https://q-ctrl.com/blog/practical-quantum-advantage-signals-a-new-commercial-era-for-quantum-computing
- [S3] Quantum Computing vs Classical Computing: Key Differences — https://www.bluequbit.io/blog/quantum-computing-vs-classical-computing
- [S4] Quantum computing: What leaders need to know now | MIT Sloan — https://mitsloan.mit.edu/ideas-made-to-matter/quantum-computing-what-leaders-need-to-know-now
- [S5] Quantum Computing by 2033: Which Industries Win or Wait? — https://postquantum.com/quantum-utility-map/quantum-computing-2033-industries
- [S6] IBM claims its quantum computers outperform classical ones — https://cen.acs.org/physical-chemistry/computational-chemistry/quantum-advantage-ibm-proof/104/web/2026/08
- [S7] Quantum advantage through trusted quantum computation | IBM Quantum Computing Blog — https://www.ibm.com/quantum/blog/quantum-advantage
- [S8] IBM Verifiable Quantum Advantage On Noisy Hardware - IEEE Spectrum — https://spectrum.ieee.org/ibm-verifiable-quantum-advantage
- [S9] Scaling for quantum advantage and beyond | IBM Quantum Computing Blog — https://www.ibm.com/quantum/blog/qdc-2025
- [S10] On “quantum supremacy” | IBM Quantum Computing Blog — https://www.ibm.com/quantum/blog/on-quantum-supremacy
- [S11] IBM and Ecosystem Partners Demonstrate "Trusted Quantum Advantage" Beyond Classical Supercomputers - Quantum Computing Report — https://quantumcomputingreport.com/ibm-and-ecosystem-partners-demonstrate-trusted-quantum-advantage-beyond-classical-supercomputers
- [S12] IBM and The University of Chicago Demonstrate Quantum Advantage, Establishing Trusted Quantum Computation on Logical Circuits — https://newsroom.ibm.com/2026-07-30-ibm-and-the-university-of-chicago-demonstrate-quantum-advantage,-establishing-trusted-quantum-computation-on-logical-circuits
- [S13] IBM's Three Quantum Advantage Claims, Fact-Checked — https://postquantum.com/industry-news/ibm-trusted-quantum-advantage-three-papers
