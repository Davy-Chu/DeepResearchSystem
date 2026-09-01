# Research Run Log

## Run Summary

**System Version:** evidence-ledger-decomposer-v1

**Research Question**

How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

**Status:** Failed

**Stop Reason:** max_iterations

**Failure Stage:** OpenAI Ledger Report Generation

**Error**

Ledger report finding 10 cites source ID(s) not attached to its ledger claims: S4

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 13

**OpenAI Calls:** 7

**Tavily Calls:** 3

**Started:** 2026-08-31T21:08:15-04:00

**Ended:** 2026-08-31T21:09:55-04:00

**Total Runtime:** 99.66s

---

# Research Plan

## Subquestions

### SQ1 [CORE]

**Question:**

What quantum-computing demonstrations have established a measured advantage over classical computers, and how should that advantage be characterized in terms of task, comparison baseline, scale, reproducibility, and practical usefulness?

**Success criteria:**

Identify concrete demonstrations with evidence of performance exceeding a relevant classical baseline, distinguish experimental demonstrations from claims based on incomplete or disputed classical comparisons, and assess whether the advantage translated into useful computational output, cost, speed, accuracy, or other practical benefit.

**Initial status:** UNRESEARCHED

### SQ2 [CORE]

**Question:**

What commercially relevant quantum-computing applications show theoretical or projected advantages over classical methods, and what assumptions determine whether those advantages could materialize?

**Success criteria:**

Separate asymptotic speedups, algorithmic predictions, simulations, and resource estimates from experimentally demonstrated advantages; specify the application areas, required problem sizes and error rates, hardware assumptions, classical alternatives, and uncertainty in the projections.

**Initial status:** UNRESEARCHED

### SQ3 [CORE]

**Question:**

How close are current quantum computers to delivering commercially useful advantages, considering present hardware capabilities and the requirements of leading candidate applications?

**Success criteria:**

Compare the current state of quantum hardware and systems with application-specific thresholds for useful advantage, including qubit quality and scale, gate fidelity, connectivity, error correction, runtime, data movement, classical pre- and post-processing, and total cost or operational constraints; provide a calibrated timeframe or range only where supported by evidence.

**Initial status:** UNRESEARCHED

### SQ4 [CORE]

**Question:**

What are the biggest remaining technical barriers to commercially useful quantum advantage, and which barriers are most decisive for different application categories?

**Success criteria:**

Identify and prioritize bottlenecks such as error rates and error correction overhead, scalable fault-tolerant architectures, qubit count and quality, control and calibration, connectivity, algorithm and compilation efficiency, input/output and data-loading costs, verification, and system economics; connect each barrier to the applications it limits.

**Initial status:** UNRESEARCHED

### SQ5 [SECONDARY]

**Question:**

How do claims of quantum advantage vary across definitions of 'advantage' and 'commercially useful,' and what uncertainty or caveats should qualify the overall assessment?

**Success criteria:**

Define or distinguish metrics such as asymptotic complexity, time-to-solution, solution quality, energy use, cost, reliability, and business value; explain sensitivity to classical baselines, workloads, hardware assumptions, reproducibility, and evolving technology, without conflating a laboratory advantage with a commercial one.

**Initial status:** UNRESEARCHED

## Synthesis Requirements

- Maintain a clear separation between demonstrated quantum advantage and theoretical or projected advantage throughout the analysis.
- Compare quantum performance against the strongest relevant classical methods and distinguish benchmark or sampling tasks from commercially meaningful workloads.
- Synthesize the evidence into an overall assessment of proximity to commercial usefulness, while preserving uncertainty rather than presenting an unsupported single date or prediction.
- Prioritize the technical barriers by their impact on achieving practical advantage, rather than listing them without assessing significance.

## Output Requirements

- Answer the question directly and comparatively: explain how close quantum computers are to commercially useful advantages over classical computers.
- Use separate treatment or clearly labeled sections for demonstrated advantages, theoretical/projected advantages, and remaining technical barriers.
- Identify the biggest remaining technical barriers explicitly.
- Include relevant caveats about the meaning of 'advantage' and 'commercially useful,' and distinguish established evidence from forecasts or assumptions.

---

# Iteration 1

## 1. Search

**Query**

> How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

**Purpose:** GENERAL

**Why this query**

This is the user's original research question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S1 — Quantum computing - Wikipedia**
  URL: https://en.wikipedia.org/wiki/Quantum_computing
- **S2 — Practical quantum advantage signals a new commercial era for quantum computing | Q-CTRL**
  URL: https://q-ctrl.com/blog/practical-quantum-advantage-signals-a-new-commercial-era-for-quantum-computing
- **S3 — Quantum Computing vs Classical Computing: Key Differences**
  URL: https://www.bluequbit.io/blog/quantum-computing-vs-classical-computing
- **S4 — Quantum computing: What leaders need to know now | MIT Sloan**
  URL: https://mitsloan.mit.edu/ideas-made-to-matter/quantum-computing-what-leaders-need-to-know-now
- **S5 — Quantum Computing by 2033: Which Industries Win or Wait?**
  URL: https://postquantum.com/quantum-utility-map/quantum-computing-2033-industries

**Search Duration:** 2.36s

---

## 2. Evidence Processing

- New claim proposals: 6
- Existing claim updates: 0
- New gaps: 4
- Resolved gaps: 0

**Processing Duration:** 17.48s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

S2 reports a 3,000-times wall-clock speedup for a fermionic-simulation materials-engineering task using an IBM quantum computer augmented with compiler and error-suppression software, while claiming practically relevant runtime and accuracy at least matching existing tooling.

- S2 supports (direct): Q-CTRL states that its demonstration used an IBM quantum computer and infrastructure software to run an existing fermionic-simulation algorithm, reporting more than 3,000× faster wall-clock performance than an industry-standard classical alternative with comparable or better accuracy.

**Confidence:** LOW

**Status:** WEAK

### New Claim C2

**Claim**

The reported S2 demonstration, even if its benchmark comparison is accepted, is evidence for a specific application-level or practical-advantage claim rather than proof of broad quantum advantage across commercially important workloads.

- S2 supports (direct): S2 defines practical quantum advantage as outperforming the best available conventional alternative on a real-world application and contrasts this with Google's 2019 supremacy demonstration, which it characterizes as lacking commercial relevance.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C3

**Claim**

Theoretical and projected quantum advantages are concentrated in selected problem classes—especially quantum-system simulation—and do not imply that quantum computers will outperform classical computers on ordinary small or moderate business problems.

- S4 supports (direct): MIT Sloan reports a framework concluding that small- to moderate-sized problems generally will not benefit, while problems with exponential algorithmic gains or very large datasets may benefit; it gives simulation, drug discovery, optimization, and financial-pattern examples as potential application areas.
- S5 supports (direct): S5 projects a narrow and uneven advantage map concentrated in applications aligned with quantum simulation, while stating that supply-chain optimization, machine learning, and derivatives pricing have no demonstrated advantage in its projected scenario.
- S3 supports (indirect): S3 describes optimization, cryptography, and large-scale simulation as potential application areas, but presents these as general potential rather than measured commercial results.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C4

**Claim**

Commercial usefulness depends on comparison against the actual available or comparably priced classical alternative, including runtime and cost, rather than on asymptotic complexity or the ability to solve a contrived benchmark.

- S4 supports (direct): MIT Sloan describes 'quantum economic advantage' as solving a problem faster with a comparably priced quantum computer than with a classical computer and notes that classical machines may have faster processing despite less efficient algorithms.
- S2 supports (direct): S2 distinguishes theoretical absolute advantage from practical advantage against the best available conventional alternative on a meaningful real-world task.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C5

**Claim**

The supplied sources identify noise, errors, decoherence, and the hardware/software needed for complex error-tolerant computation as major barriers to useful quantum applications.

- S2 supports (direct): S2 states that hardware size and errors degrade performance and cause algorithms to fail, and that noise and errors have limited useful results on relevant problems.
- S3 supports (direct): S3 explains that quantum systems are sensitive to temperature, electromagnetic interference, and vibration, and require specialized operating conditions and repeated runs with statistical analysis.
- S4 supports (direct): MIT Sloan reports that hardware and software for the most complex problems may not be available until 2035 or later, according to the cited estimate.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C6

**Claim**

A projected 2,000-logical-qubit, fault-tolerant machine executing approximately one billion error-corrected operations is presented by S5 as potentially useful for selected chemistry, pharmaceutical, and catalysis workloads by 2033, but this is a forecast rather than a demonstrated capability.

- S5 supports (direct): S5 describes a hypothetical 2033 machine with 2,000 logical qubits and one billion error-corrected operations, and projects useful applications in molecular simulation, drug metabolism, and catalysis under that scenario.

**Confidence:** LOW

**Status:** WEAK

### New Gap G1

No independent, peer-reviewed or replicated evidence is supplied to verify S2's reported 3,000× speedup, the quality of its classical baseline, total cost, reproducibility, or commercial return.

### New Gap G2

The sources do not provide a current, quantitative comparison between available hardware and application-specific requirements such as physical-to-logical-qubit overhead, logical error rates, circuit depth, runtime, data loading, connectivity, and total system cost.

### New Gap G3

The projected application advantages in chemistry, pharmaceuticals, catalysis, batteries, optimization, cryptography, and finance lack sufficiently detailed assumptions about problem size, classical alternatives, error rates, input/output costs, and economic value to establish when they will become commercially superior.

### New Gap G4

The supplied evidence does not systematically prioritize technical barriers by application category or establish a supported timeframe for broad commercial quantum advantage.

---

## 4. Current Research State

- Claims: 6
- Supported: 4
- Weak: 2
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 4
- Remaining Searches: 2

### Subquestion Progress

**SQ1:** UNRESEARCHED → PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ2:** UNRESEARCHED → PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ3:** UNRESEARCHED → PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ4:** UNRESEARCHED → PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ5:** UNRESEARCHED → PARTIAL

Reason: At least one linked ledger claim is not yet supported.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → PARTIAL (targeted searches: 0)
- SQ3 → PARTIAL (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- SQ5 → PARTIAL (targeted searches: 0)

**Remaining targeted searches:** 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ1

**Why**

SQ1 is a CORE subquestion and the strongest apparent practical-advantage claim is a low-confidence vendor report. Independent evidence on demonstrated quantum advantage, especially the classical baseline, reproducibility, and practical usefulness, would materially improve the assessment.

**Next Search**

> peer-reviewed independent quantum advantage demonstrations 2024 2025 practical application classical baseline reproducibility IBM Google quantum computing benchmark


---

# Iteration 2

## 1. Search

**Query**

> peer-reviewed independent quantum advantage demonstrations 2024 2025 practical application classical baseline reproducibility IBM Google quantum computing benchmark

**Target:** SQ1

**Purpose:** SUBQUESTION

**Why this query**

SQ1 is a CORE subquestion and the strongest apparent practical-advantage claim is a low-confidence vendor report. Independent evidence on demonstrated quantum advantage, especially the classical baseline, reproducibility, and practical usefulness, would materially improve the assessment.

5 result(s) retrieved; 5 new unique source(s) added.

- **S6 — IBM claims its quantum computers outperform classical ones**
  URL: https://cen.acs.org/physical-chemistry/computational-chemistry/quantum-advantage-ibm-proof/104/web/2026/08
- **S7 — Quantum advantage through trusted quantum computation | IBM Quantum Computing Blog**
  URL: https://www.ibm.com/quantum/blog/quantum-advantage
- **S8 — IBM Verifiable Quantum Advantage On Noisy Hardware - IEEE Spectrum**
  URL: https://spectrum.ieee.org/ibm-verifiable-quantum-advantage
- **S9 — Scaling for quantum advantage and beyond | IBM Quantum Computing Blog**
  URL: https://www.ibm.com/quantum/blog/qdc-2025
- **S10 — On “quantum supremacy” | IBM Quantum Computing Blog**
  URL: https://www.ibm.com/quantum/blog/on-quantum-supremacy

**Search Duration:** 2.27s

---

## 2. Evidence Processing

- New claim proposals: 5
- Existing claim updates: 3
- New gaps: 2
- Resolved gaps: 0

**Processing Duration:** 22.18s

---

## 3. Ledger Updates

### New Claim C7

**Claim**

IBM and collaborators report three 2026 demonstrations on Heron processors involving doped-Clifford sampling, quantum-magnet/Floquet-dynamics experiments, and validated quantum computations; the demonstrations are presented as producing results beyond leading classical simulations or as classically hard computations with built-in validation, but the papers were supplied as preprints rather than peer-reviewed publications.

- S6 supports (direct): C&EN reports three IBM Heron R3 demonstrations and describes the sampling experiment as reaching 468 T gates, where no known classical algorithm could simulate the model, while noting that the papers were preprints and that classical reproduction cannot be absolutely ruled out.
- S7 supports (direct): IBM describes three papers reporting advantage demonstrations using doped Clifford sampling, spacetime codes, and validated error-mitigation techniques, including a 70-logical-qubit computation and experiments up to 74 qubits.
- S8 supports (direct): IEEE Spectrum reports IBM's claim that three results validated calculations out of reach of classical computers and describes the demonstrations as using new validation techniques on a 156-qubit Heron processor.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C8

**Claim**

The reported 2026 IBM demonstrations are evidence of narrow, task-specific beyond-classical performance or classically hard computation, not evidence of commercially useful advantage across general workloads.

- S6 supports (direct): C&EN characterizes the demonstrations as applying to certain niche problems, says current quantum computers remain noisy and error prone, and reports that classical computers still outperform them at modeling.
- S7 supports (direct): IBM states that quantum advantage requires validated quantum computation plus measurable separation in efficiency, cost-effectiveness, accuracy, or a combination, and frames the demonstrations as part of an ongoing tracker rather than a completed commercial milestone.
- S8 supports (direct): IEEE Spectrum describes the results as calculations without a classical counterpart but emphasizes that defining advantage is difficult and reports them as IBM claims rather than as established commercial superiority.
- S10 supports (indirect): IBM's 2019 comparison argues that Google's random-circuit result should not be treated as proof of broad supremacy because a different classical simulation reduced the estimated runtime to 2.5 days and had higher fidelity.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C9

**Claim**

IBM's 2025 advantage framework treated rigorous validation and demonstrable separation in efficiency, cost-effectiveness, or accuracy as unmet criteria for its candidate advantage experiments, indicating that candidate demonstrations and validated beyond-classical results do not automatically establish practical advantage.

- S9 supports (direct): IBM says its 2025 candidate experiments had not yet achieved advantage because they lacked both rigorous validation and demonstrable quantum separation measured by efficiency, cost-effectiveness, accuracy, or a combination.
- S7 contradicts (direct): IBM's 2026 post says three papers demonstrate quantum advantage through built-in validation and describes the field as entering an era of beyond-classical results with rigorous reliability evidence.

**Confidence:** MEDIUM

**Status:** CONFLICTING

### New Claim C10

**Claim**

The 2026 validation demonstrations improve evidence that noisy quantum computations can be trusted in classically hard regimes, but they do not demonstrate fault-tolerant, commercially useful computation at application-relevant scale.

- S7 supports (direct): IBM reports that spacetime-code validation produced a rigorous lower bound on logical-computation fidelity, reduced effective gate error by roughly 10×, and enabled a 70-logical-qubit computation.
- S8 supports (direct): IEEE Spectrum reports that the demonstrations provided good evidence of correctness for calculations without a classical counterpart, while presenting them as validation techniques rather than commercial applications.
- S6 supports (direct): C&EN reports a measured fidelity of approximately 32% for the reference calculation and an estimated lower bound of 28.4% after adding T gates, while noting that present systems remain noisy and error prone.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C11

**Claim**

Scaling toward useful advantage requires simultaneously improving physical error rates, validation and error correction, circuit depth, connectivity, and the integration of quantum processors with classical computation; improved qubit count alone is insufficient.

- S7 supports (direct): IBM describes spacetime-code validation, noisy non-Clifford gates, and classical validation infrastructure as central to trusted computation beyond classical verification.
- S9 supports (direct): IBM identifies high-performing hardware as necessary and links square topology and more couplers to fewer SWAP gates and more complex circuits; it also emphasizes software and classical-quantum system performance.
- S6 supports (direct): C&EN explains that added T gates increase computational power but also accumulate errors, and reports that current machines remain noisy and lose information.

**Confidence:** HIGH

**Status:** SUPPORTED

### Updated Claim C5

**Claim**

The supplied sources identify noise, errors, decoherence, and the hardware/software needed for complex error-tolerant computation as major barriers to useful quantum applications.

- S7 supports (direct): The reported demonstrations rely on spacetime codes, error detection, fidelity bounds, and error-mitigation techniques because verification and accumulated errors become limiting in classically hard circuits.
- S9 supports (direct): IBM identifies hardware performance, gate errors, connectivity, SWAP overhead, circuit depth, and software as requirements for scaling advantage.
- S6 supports (direct): C&EN reports that increasing non-Clifford T gates increases noise and can render outputs meaningless, while current systems remain noisy and error prone.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

The reported S2 demonstration, even if its benchmark comparison is accepted, is evidence for a specific application-level or practical-advantage claim rather than proof of broad quantum advantage across commercially important workloads.

- S6 supports (direct): C&EN characterizes the IBM results as niche demonstrations and distinguishes classically hard sampling or quantum-phenomena experiments from useful modeling performance.
- S8 supports (direct): IEEE Spectrum distinguishes calculations without a classical counterpart from the broader and harder question of what counts as advantage.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

Commercial usefulness depends on comparison against the actual available or comparably priced classical alternative, including runtime and cost, rather than on asymptotic complexity or the ability to solve a contrived benchmark.

- S9 supports (direct): IBM's advantage framework requires measurable separation in efficiency, cost-effectiveness, accuracy, or a combination, and tracks candidates against leading classical methods.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### New Gap G5

The 2026 IBM demonstrations lack supplied independent replication and a complete, independently audited comparison with the strongest classical algorithms, including total quantum-plus-classical runtime, cost, sampling quality, reproducibility, and application-level value.

### New Gap G6

The new validation results do not establish the physical-to-logical-qubit overhead, logical error rates, sustained circuit throughput, or resource requirements needed to determine whether the reported 70-logical-qubit and related demonstrations can scale to commercially relevant chemistry or materials workloads.

---

## 4. Current Research State

- Claims: 11
- Supported: 8
- Weak: 2
- Conflicting: 1
- Insufficient Evidence: 0
- Open Gaps: 6
- Remaining Searches: 1

### Subquestion Progress

**SQ1:** PARTIAL → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ2:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ3:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ4:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ5:** PARTIAL → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

### Research Plan Status

**CORE:**

- SQ1 → CONFLICTING (targeted searches: 1)
- SQ2 → PARTIAL (targeted searches: 0)
- SQ3 → PARTIAL (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- SQ5 → CONFLICTING (targeted searches: 0)

**Remaining targeted searches:** 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ1

**Why**

SQ1 is a CORE subquestion with conflicting evidence and two high-importance unresolved gaps. Independent, peer-reviewed counterevidence or replication of the reported IBM demonstrations—and a complete comparison with the strongest classical baselines—could materially change how demonstrated advantage should be characterized.

**Next Search**

> independent peer-reviewed replication or critique of IBM 2026 Heron quantum advantage demonstrations: doped-Clifford sampling, 70-logical-qubit spacetime-code validation, strongest classical baselines, total runtime, fidelity, and practical usefulness


---

# Iteration 3

## 1. Search

**Query**

> independent peer-reviewed replication or critique of IBM 2026 Heron quantum advantage demonstrations: doped-Clifford sampling, 70-logical-qubit spacetime-code validation, strongest classical baselines, total runtime, fidelity, and practical usefulness

**Target:** SQ1

**Purpose:** SUBQUESTION

**Why this query**

SQ1 is a CORE subquestion with conflicting evidence and two high-importance unresolved gaps. Independent, peer-reviewed counterevidence or replication of the reported IBM demonstrations—and a complete comparison with the strongest classical baselines—could materially change how demonstrated advantage should be characterized.

5 result(s) retrieved; 3 new unique source(s) added.

- **S11 — IBM and Ecosystem Partners Demonstrate "Trusted Quantum Advantage" Beyond Classical Supercomputers - Quantum Computing Report**
  URL: https://quantumcomputingreport.com/ibm-and-ecosystem-partners-demonstrate-trusted-quantum-advantage-beyond-classical-supercomputers
- **S12 — IBM and The University of Chicago Demonstrate Quantum Advantage, Establishing Trusted Quantum Computation on Logical Circuits**
  URL: https://newsroom.ibm.com/2026-07-30-ibm-and-the-university-of-chicago-demonstrate-quantum-advantage,-establishing-trusted-quantum-computation-on-logical-circuits
- **S13 — IBM's Three Quantum Advantage Claims, Fact-Checked**
  URL: https://postquantum.com/industry-news/ibm-trusted-quantum-advantage-three-papers

**Search Duration:** 2.25s

---

## 2. Evidence Processing

- New claim proposals: 2
- Existing claim updates: 4
- New gaps: 1
- Resolved gaps: 0

**Processing Duration:** 18.30s

---

## 3. Ledger Updates

### New Claim C12

**Claim**

The three 2026 IBM-associated demonstrations have materially different evidentiary strengths: the IBM–University of Chicago doped-Clifford experiment makes a complexity-based beyond-classical claim with a device-dependent fidelity certificate, whereas the Qedma Floquet and Algorithmiq Loschmidt-echo studies primarily report empirical failure or disagreement among tested classical methods and rely partly on error-mitigation or heuristic assumptions.

- S13 supports (direct): The fact-check distinguishes the flagship doped-Clifford result, which combines hardness arguments with a device-dependent fidelity certificate, from the Qedma and Algorithmiq papers, which make empirical claims about unreliable or conflicting classical methods.
- S11 supports (direct): The source presents three demonstrations with different classical comparisons and validation methods: spacetime-code validation, Fugaku benchmarking with cross-platform checks, and process validation across IBM processors.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C13

**Claim**

The 70-qubit doped-Clifford demonstration used error-detected encoded data qubits rather than fault-tolerant logical qubits of the type assumed in large-scale fault-tolerant resource estimates; its reported 10-fold error suppression and approximately 15–16 minute execution therefore do not establish scalable fault-tolerant operation.

- S13 supports (direct): S13 states that IBM's 70 'logical qubits' are error-detected data qubits, not fault-tolerant logical qubits, and reports roughly 10-fold effective error suppression, a 0.284 fidelity lower bound, and 16.1 minutes of QPU execution.
- S12 supports (direct): IBM reports 70 logical qubits, 2,415 logical two-qubit operations, 468 T gates, and approximately 15 minutes, while describing the result as an error-correction and trust milestone rather than a commercial application.

**Confidence:** HIGH

**Status:** SUPPORTED

### Updated Claim C7

**Claim**

IBM and collaborators report three 2026 demonstrations on Heron processors involving doped-Clifford sampling, quantum-magnet/Floquet-dynamics experiments, and validated quantum computations; the demonstrations are presented as producing results beyond leading classical simulations or as classically hard computations with built-in validation, but the papers were supplied as preprints rather than peer-reviewed publications.

- S11 supports (direct): QCR reports the three demonstrations, their hardware scales, classical comparison methods, validation frameworks, and public circuit repositories.
- S12 supports (direct): IBM reports the University of Chicago demonstration as a structured hard-sampling computation with built-in error detection, 70 logical qubits, and approximately 15 minutes of execution.
- S13 supports (direct): The fact-check confirms that the papers are preprints and details the 70-qubit experiment's 468 T gates, 10-fold error suppression, certified fidelity lower bound, and unresolved possibility of improved classical methods.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C9

**Claim**

IBM's 2025 advantage framework treated rigorous validation and demonstrable separation in efficiency, cost-effectiveness, or accuracy as unmet criteria for its candidate advantage experiments, indicating that candidate demonstrations and validated beyond-classical results do not automatically establish practical advantage.

- S13 supports (direct): S13 emphasizes that IBM's three papers operate at different evidentiary levels, that the tracker treats the entries as active candidates requiring further benchmarking, and that the later claims do not uniformly establish practical advantage.

**Confidence:** MEDIUM → HIGH

**Status:** CONFLICTING → CONFLICTING

### Updated Claim C10

**Claim**

The 2026 validation demonstrations improve evidence that noisy quantum computations can be trusted in classically hard regimes, but they do not demonstrate fault-tolerant, commercially useful computation at application-relevant scale.

- S11 supports (direct): QCR describes verification and error reduction in the 70-logical-qubit experiment but presents no application-level commercial benchmark or fault-tolerant scaling result.
- S12 supports (direct): IBM characterizes the experiment as a milestone toward scaling and emphasizes error correction and trust rather than reporting commercially useful application performance.
- S13 supports (direct): S13 explicitly states that the 70 data qubits are error-detected rather than fault-tolerant logical qubits and that the result does not settle scaling or practical advantage.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C11

**Claim**

Scaling toward useful advantage requires simultaneously improving physical error rates, validation and error correction, circuit depth, connectivity, and the integration of quantum processors with classical computation; improved qubit count alone is insufficient.

- S13 supports (direct): S13 identifies verification, non-Clifford-gate error accumulation, heuristic error mitigation, connectivity and classical-simulation comparisons as unresolved issues affecting claims of advantage.
- S11 supports (direct): QCR links useful scaling to error detection, classical benchmarking, cross-platform validation, noise stability, and quantum–classical software integration.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### New Gap G7

For the Qedma Floquet and Algorithmiq Loschmidt-echo demonstrations, the supplied evidence does not establish quantitative accuracy against a known ground truth at the hardest scales: Qedma's extrapolated mitigation may introduce bias, while Algorithmiq's global-rescaling estimate lacks a quantitative error bound.

---

## 4. Current Research State

- Claims: 13
- Supported: 10
- Weak: 2
- Conflicting: 1
- Insufficient Evidence: 0
- Open Gaps: 7
- Remaining Searches: 0

### Subquestion Progress

**SQ1:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ2:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ3:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ4:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ5:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

### Research Plan Status

**CORE:**

- SQ1 → CONFLICTING (targeted searches: 2)
- SQ2 → PARTIAL (targeted searches: 0)
- SQ3 → PARTIAL (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- SQ5 → CONFLICTING (targeted searches: 0)

**Remaining targeted searches:** 0

---

## 5. Research Decision

**Decision:** Stop researching.

**Origin:** BUDGET_STOP

**Why**

The maximum research iteration budget was reached.

**Stop Reason:** max_iterations


---

# Final Research Decision

**Research did not complete.**

**Failure Stage:** OpenAI Ledger Report Generation

**Remaining Uncertainty**

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

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Question Decomposition | 1 | 10.06s |
| Tavily Search | 3 | 6.89s |
| Evidence Processing | 3 | 57.96s |
| Research Decision | 2 | 6.96s |
| Report Generation | 1 | 0.00s |
| Total Run | — | 99.66s |
