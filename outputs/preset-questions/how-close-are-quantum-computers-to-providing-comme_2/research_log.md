# Research Run Log

## Run Summary

**System Version:** evidence-ledger-v1

**Research Question**

How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 9

**OpenAI Calls:** 6

**Tavily Calls:** 3

**Started:** 2026-08-31T17:40:09-04:00

**Ended:** 2026-08-31T17:41:36-04:00

**Total Runtime:** 86.65s

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
- **S2 — Practical quantum advantage signals a new commercial ...**
  URL: https://q-ctrl.com/blog/practical-quantum-advantage-signals-a-new-commercial-era-for-quantum-computing
- **S3 — Quantum Computing vs Classical Computing: Key Differences**
  URL: https://www.bluequbit.io/blog/quantum-computing-vs-classical-computing
- **S4 — Quantum computing: What leaders need to know now**
  URL: https://mitsloan.mit.edu/ideas-made-to-matter/quantum-computing-what-leaders-need-to-know-now
- **S5 — Quantum Computing by 2033: Which Industries Win or Wait?**
  URL: https://postquantum.com/quantum-utility-map/quantum-computing-2033-industries

**Search Duration:** 3.24s

---

## 2. Evidence Processing

- New claim proposals: 6
- Existing claim updates: 0
- New gaps: 4
- Resolved gaps: 0

**Processing Duration:** 22.77s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

Quantum computers have demonstrated computational performance advantages on specially constructed benchmark problems, but the supplied sources do not establish that these demonstrations provide commercially useful advantages over classical computers.

- S2 supports (direct): Reports that Google claimed quantum computational supremacy in 2019 on a problem described as lacking commercial or practical relevance.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C2

**Claim**

The supplied evidence does not demonstrate a commercially useful quantum advantage over classical computing; a Q-CTRL blog claims a 3,000-times wall-clock speedup for a materials-simulation task on publicly available IBM hardware augmented with its software, but this claim is not independently validated here.

- S2 supports (direct): Claims that Q-CTRL and IBM demonstrated practical quantum advantage in fermionic simulation, reporting a more-than-3,000-times wall-clock speedup against an industry-standard classical alternative while meeting accuracy and practical-time requirements.

**Confidence:** LOW

**Status:** WEAK

### New Claim C3

**Claim**

Potential quantum advantages are expected to be concentrated in selected large-scale problems—especially quantum-system, molecular, and materials simulation—rather than applying broadly to ordinary business workloads.

- S4 supports (direct): MIT Sloan’s account of an MIT framework says small-to-moderate problems common in typical businesses generally will not benefit, while problems with exponential algorithmic gains or very large datasets may benefit; it identifies matter simulation, drug discovery, optimization, and related applications as examples of potential use.
- S5 supports (direct): Projects that a 2,000-logical-qubit fault-tolerant system would be particularly suited to molecular, materials, and physical-system simulation, while stating that no demonstrated advantage is available for supply-chain optimization, machine learning, or derivatives pricing.
- S2 supports (indirect): Explains that fermionic simulation is a candidate for future advantage because it scales poorly classically and is in BQP, while framing this as a materials-engineering use case.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C4

**Claim**

Quantum economic advantage is a stricter and more commercially relevant criterion than merely demonstrating a quantum algorithmic or computational advantage: it requires outperforming a comparably priced classical alternative for a particular problem.

- S4 supports (direct): Defines quantum economic advantage as solving a problem more quickly with a quantum computer than with a comparably priced classical computer, and warns that conventional quantum-advantage framing can overshadow usefulness and cost competitiveness.
- S2 supports (direct): Defines practical quantum advantage as outperforming the best available conventional alternative on a real-world problem of known commercial or scientific relevance, with useful speed, accuracy, and affordability.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C5

**Claim**

The largest technical barriers identified in the supplied sources are noise and errors, decoherence, insufficient hardware scale, and the lack of mature error-correction infrastructure needed for complex useful workloads.

- S2 supports (direct): Identifies hardware size and errors as major challenges, says noise and errors have prevented useful results on relevant problems, and describes error suppression as necessary to run applications at larger scales.
- S3 supports (direct): States that qubits are sensitive to temperature, electromagnetic interference, and vibrations; decoherence disrupts computation; and different hardware platforms remain under development with differing scalability, stability, speed, and error-correction properties.
- S4 supports (direct): Reports that hardware and software for handling the most complex problems may not be available until 2035 or later, indicating a substantial remaining infrastructure and capability gap.
- S5 supports (indirect): Bases its projected applications on fault-tolerant machines with thousands of logical qubits and large error-corrected workloads, implying that such fault-tolerant scale is a prerequisite for the projected advantages discussed.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C6

**Claim**

Near-term commercial usefulness remains uncertain and is likely to be workload-specific; one supplied projection says hardware and software for the most complex problems may not be available until 2035 or later, while other sources project meaningful fault-tolerant use cases around 2033 or claim a present-day practical demonstration.

- S4 supports (direct): Cites an estimate that hardware and software for the most complex problems will not be available until 2035 or later.
- S5 supports (direct): Projects competitive impact by 2033 for selected pharmaceutical, chemical, and battery applications assuming a 2,000-logical-qubit fault-tolerant machine.
- S2 supports (direct): Claims a present-day practical quantum-advantage demonstration for materials simulation.
- S4 contradicts (indirect): Its 2035-or-later estimate for complex workloads conflicts with S2’s claim of a present-day practical advantage, though the sources may be using different definitions and workload requirements.

**Confidence:** MEDIUM

**Status:** CONFLICTING

### New Gap G1

Independent, peer-reviewed or otherwise externally validated evidence is needed to determine whether the reported Q-CTRL/IBM 3,000-times materials-simulation result survives comparison with the best classical algorithms, including end-to-end runtime, accuracy, cost, preprocessing, and verification.

### New Gap G2

The supplied sources do not quantify the hardware resources, physical-qubit overhead, error rates, logical-qubit performance, energy use, or operating costs required for commercially useful fault-tolerant workloads.

### New Gap G3

The evidence does not establish which specific commercial applications, if any, have achieved a reproducible advantage after accounting for data loading, classical post-processing, repeated probabilistic measurement, and comparison against state-of-the-art classical methods.

### New Gap G4

Projected 2033–2035 timelines are not supported by a source-based assessment of roadmap reliability, and the sources provide no systematic reconciliation of their differing definitions of quantum, practical, absolute, and economic advantage.

---

## 4. Current Research State

- Claims: 6
- Supported: 4
- Weak: 1
- Conflicting: 1
- Insufficient Evidence: 0
- Open Gaps: 4
- Remaining Searches: 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** GAP G1

**Why**

The reported 3,000× materials-simulation advantage is the strongest potential counterexample to the conclusion yet lacks independent validation against state-of-the-art classical methods and full costs.

**Next Search**

> Independent peer-reviewed validation Q-CTRL IBM 3,000x speedup fermionic or materials simulation quantum advantage classical benchmark runtime accuracy cost


---

# Iteration 2

## 1. Search

**Query**

> Independent peer-reviewed validation Q-CTRL IBM 3,000x speedup fermionic or materials simulation quantum advantage classical benchmark runtime accuracy cost

**Target:** G1

**Purpose:** GENERAL

**Why this query**

The reported 3,000× materials-simulation advantage is the strongest potential counterexample to the conclusion yet lacks independent validation against state-of-the-art classical methods and full costs.

1 result(s) retrieved; 1 new unique source(s) added.

- **S6 — Q-CTRL Delivers 3,000x Speedup in Materials Discovery for the Energy Sector with Quantum Computing**
  URL: https://thequantuminsider.com/2026/05/06/qctrl-practical-quantum-advantage-materials-discovery

**Search Duration:** 2.82s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 4
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 12.88s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Quantum computers have demonstrated computational performance advantages on specially constructed benchmark problems, but the supplied sources do not establish that these demonstrations provide commercially useful advantages over classical computers.

- S6 supports (direct): Reports a 120-qubit materials simulation on IBM hardware that Q-CTRL says completed in about two minutes versus more than 100 hours for a classical implementation, with outputs meeting stated industry-standard accuracy expectations. This is a reported advantage on a specially selected simulation problem, not independent confirmation of commercial superiority.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

The supplied evidence does not demonstrate a commercially useful quantum advantage over classical computing; a Q-CTRL blog claims a 3,000-times wall-clock speedup for a materials-simulation task on publicly available IBM hardware augmented with its software, but this claim is not independently validated here.

- S6 supports (direct): The report specifies that the claimed 3,000-times comparison involved a two-minute quantum run versus more than 100 hours for a classical simulation, and says the quantum results met industry-standard accuracy expectations. However, it presents the claim through company and partner statements and does not independently establish end-to-end commercial advantage, cost competitiveness, or reproducibility.
- S6 contradicts (direct): S6 reports Q-CTRL’s claim that the materials-simulation demonstration constituted practical quantum advantage on a commercially relevant problem, using a state-of-the-art industry-standard classical software comparison and accuracy agreement. This challenges the claim that the supplied evidence does not demonstrate commercial usefulness, although the report does not independently validate the claim.

**Confidence:** LOW → LOW

**Status:** WEAK → CONFLICTING

### Updated Claim C5

**Claim**

The largest technical barriers identified in the supplied sources are noise and errors, decoherence, insufficient hardware scale, and the lack of mature error-correction infrastructure needed for complex useful workloads.

- S6 supports (direct): States that noise and errors can prevent useful results and reports that Q-CTRL used performance-management software for runtime error suppression to improve accuracy on the 120-qubit simulation, reinforcing noise control as a practical barrier.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C6

**Claim**

Near-term commercial usefulness remains uncertain and is likely to be workload-specific; one supplied projection says hardware and software for the most complex problems may not be available until 2035 or later, while other sources project meaningful fault-tolerant use cases around 2033 or claim a present-day practical demonstration.

- S6 supports (direct): Reports a present-day claimed practical-advantage demonstration on a materials-science problem using a 120-qubit simulation and commercially available IBM quantum infrastructure.
- S6 contradicts (direct): Its claim of present-day positive return on investment and practical quantum advantage conflicts with later projected timelines for complex fault-tolerant workloads, though it concerns a narrowly defined materials-simulation task and relies on company and partner assertions.

**Confidence:** MEDIUM → MEDIUM

**Status:** CONFLICTING → CONFLICTING

---

## 4. Current Research State

- Claims: 6
- Supported: 4
- Weak: 0
- Conflicting: 2
- Insufficient Evidence: 0
- Open Gaps: 4
- Remaining Searches: 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** GAP G1

**Why**

A final targeted search could materially clarify the central conflict over whether the reported Q-CTRL/IBM result constitutes a commercially useful advantage by finding independent validation or a rigorous classical comparison.

**Next Search**

> independent peer-reviewed validation or critique Q-CTRL IBM 3000x quantum advantage materials simulation classical benchmark end-to-end runtime accuracy preprocessing cost


---

# Iteration 3

## 1. Search

**Query**

> independent peer-reviewed validation or critique Q-CTRL IBM 3000x quantum advantage materials simulation classical benchmark end-to-end runtime accuracy preprocessing cost

**Target:** G1

**Purpose:** GENERAL

**Why this query**

A final targeted search could materially clarify the central conflict over whether the reported Q-CTRL/IBM result constitutes a commercially useful advantage by finding independent validation or a rigorous classical comparison.

5 result(s) retrieved; 3 new unique source(s) added.

- **S7 — Q-CTRL’s Software Cuts Materials Simulation Time By 3,000x**
  URL: https://quantumzeitgeist.com/materials-simulation-time-q-ctrls-software
- **S8 — Q-CTRL Delivers 3,000x Speedup in Materials Discovery for the Energy Sector with Quantum Computing, Demonstrates Evidence of Practical Quantum Advantage | Q-CTRL**
  URL: https://q-ctrl.com/blog/q-ctrl-delivers-3-000x-speedup-in-materials-discovery-for-the-energy-sector-with-quantum-computing-and-demonstrates-evidence-of-practical-quantum-advantage
- **S9 — IBM Quantum Computing | Research and publications**
  URL: https://www.ibm.com/quantum/research

**Search Duration:** 1.84s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 5
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 15.21s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Quantum computers have demonstrated computational performance advantages on specially constructed benchmark problems, but the supplied sources do not establish that these demonstrations provide commercially useful advantages over classical computers.

- S7 supports (direct): Reports a 120-qubit materials-simulation calculation completed in two minutes versus more than 100 hours using classical TDVP software, while noting that this is Q-CTRL’s reported result and not independent validation of commercial superiority.
- S8 supports (direct): Q-CTRL reports a 3,000-times wall-clock speedup for a fermionic materials simulation on the IBM Quantum Platform, with accuracy claimed to meet industry-standard expectations; the source is a company press release rather than independent confirmation.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

The supplied evidence does not demonstrate a commercially useful quantum advantage over classical computing; a Q-CTRL blog claims a 3,000-times wall-clock speedup for a materials-simulation task on publicly available IBM hardware augmented with its software, but this claim is not independently validated here.

- S7 supports (direct): Reports Q-CTRL’s claim of a 3,000-times speedup, using two minutes of quantum runtime versus more than 100 hours for classical TDVP, but presents the result through company claims and does not independently validate end-to-end commercial advantage.
- S8 contradicts (direct): Q-CTRL explicitly characterizes its IBM-platform materials-simulation result as evidence of practical quantum advantage over performance-optimized, industry-standard classical software on a commercially relevant problem, with claimed accuracy meeting user expectations and positive ROI potential.

**Confidence:** LOW → LOW

**Status:** CONFLICTING → CONFLICTING

### Updated Claim C3

**Claim**

Potential quantum advantages are expected to be concentrated in selected large-scale problems—especially quantum-system, molecular, and materials simulation—rather than applying broadly to ordinary business workloads.

- S9 supports (direct): IBM identifies optimization, Hamiltonian simulation, partial differential equations, and machine learning as areas where quantum algorithms may provide near-term value, while describing the work as algorithm research and testing rather than established broad commercial advantage.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

The largest technical barriers identified in the supplied sources are noise and errors, decoherence, insufficient hardware scale, and the lack of mature error-correction infrastructure needed for complex useful workloads.

- S7 supports (direct): States that Q-CTRL’s runtime performance-management software was central to mitigating noise and errors in the 120-qubit materials simulation, indicating that error suppression remains necessary for useful results on current hardware.
- S8 supports (direct): Says quantum noise and errors can prevent useful results and attributes the reported materials-simulation performance to infrastructure software providing runtime error suppression.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C6

**Claim**

Near-term commercial usefulness remains uncertain and is likely to be workload-specific; one supplied projection says hardware and software for the most complex problems may not be available until 2035 or later, while other sources project meaningful fault-tolerant use cases around 2033 or claim a present-day practical demonstration.

- S7 supports (direct): Reports a present-day claimed practical advantage on a narrowly defined materials-science problem using 120 qubits and commercially available IBM infrastructure, while noting that the claim concerns a specific workload.
- S8 supports (direct): Claims that current IBM quantum hardware augmented with Q-CTRL software achieved positive ROI potential and practical advantage for a commercially relevant materials-simulation task, but this is a vendor announcement rather than independent validation.
- S7 contradicts (indirect): Acknowledges that future classical algorithm improvements or GPU acceleration of TDVP could change the reported comparison, limiting the strength of the present-day claim and preserving uncertainty about its durability.

**Confidence:** MEDIUM → MEDIUM

**Status:** CONFLICTING → CONFLICTING

---

## 4. Current Research State

- Claims: 6
- Supported: 4
- Weak: 0
- Conflicting: 2
- Insufficient Evidence: 0
- Open Gaps: 4
- Remaining Searches: 0

---

## 5. Research Decision

**Decision:** Stop researching.

**Origin:** BUDGET_STOP

**Why**

The maximum research iteration budget was reached.

**Stop Reason:** max_iterations


---

# Final Research Decision

**Stop Reason:** max_iterations

**Remaining Uncertainty**

- Independent, peer-reviewed or externally validated testing of the reported 3,000-times materials-simulation result against the best classical algorithms, including end-to-end runtime, accuracy, cost, preprocessing, and verification.
- Quantified requirements for physical-qubit overhead, error rates, logical-qubit performance, energy use, and operating costs for commercially useful fault-tolerant workloads.
- Evidence identifying specific commercial applications with reproducible advantage after accounting for data loading, classical post-processing, repeated probabilistic measurement, and state-of-the-art classical methods.
- A source-based assessment of the reliability of the projected 2033–2035 timelines and a systematic reconciliation of differing definitions of quantum, practical, absolute, and economic advantage.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 7.90s |
| Evidence Processing | 3 | 50.86s |
| Research Decision | 2 | 6.96s |
| Report Generation | 1 | 20.93s |
| Total Run | — | 86.65s |
