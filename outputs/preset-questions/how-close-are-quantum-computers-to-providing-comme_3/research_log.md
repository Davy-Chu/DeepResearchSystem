# Research Run Log

## Run Summary

**System Version:** evidence-ledger-decomposer-v1

**Research Question**

How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

**Status:** Failed

**Stop Reason:** max_iterations

**Failure Stage:** OpenAI Ledger Report Generation

**Error**

Ledger report finding 1 cites source ID(s) not attached to its ledger claims: S1

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 14

**OpenAI Calls:** 7

**Tavily Calls:** 3

**Started:** 2026-08-31T18:17:42-04:00

**Ended:** 2026-08-31T18:19:24-04:00

**Total Runtime:** 102.05s

---

# Research Plan

## Subquestions

### SQ1 [CORE]

**Question:**

What quantum-computing advantages over classical computers have been experimentally demonstrated to date, and do any constitute commercially useful advantages?

**Success criteria:**

Identify credible demonstrations, the task or application involved, the relevant classical baseline, performance metric, scale, and whether the result delivered practical value such as lower cost, faster time-to-solution, better quality, or otherwise meaningful business utility. Distinguish computational advantage from demonstrations that are primarily proof-of-principle or benchmark-specific.

**Initial status:** UNRESEARCHED

### SQ2 [CORE]

**Question:**

What quantum-computing advantages are theoretically established or currently projected for commercially relevant applications, and how plausible and near-term are those projections?

**Success criteria:**

Cover relevant application areas and algorithms, distinguish formal asymptotic speedups from estimates under realistic hardware and error-correction assumptions, and state the conditions, resource requirements, timelines, and uncertainties behind projected advantages. Separate theoretical possibility from experimentally validated performance.

**Initial status:** UNRESEARCHED

### SQ3 [CORE]

**Question:**

What classical methods and hardware must quantum computers outperform for an advantage to be commercially meaningful?

**Success criteria:**

Compare quantum approaches with strong contemporary classical alternatives, including algorithms, specialized hardware, and practical workflows. Specify the business-relevant threshold for advantage—such as total cost, latency, accuracy, scale, reliability, or energy use—and account for data loading, error correction, compilation, communication, and integration overheads.

**Initial status:** UNRESEARCHED

### SQ4 [CORE]

**Question:**

What are the biggest remaining technical barriers preventing quantum computers from delivering commercially useful advantages, and how do those barriers affect the expected path to adoption?

**Success criteria:**

Rank the principal barriers, such as physical error rates, fault-tolerant error correction and overhead, qubit number and connectivity, control and calibration, algorithm and problem-encoding limitations, benchmarking, and system cost or reliability. Explain which barriers are demonstrated bottlenecks, which are engineering projections, and what milestones would materially change the assessment.

**Initial status:** UNRESEARCHED

## Synthesis Requirements

- Maintain a clear distinction between demonstrated quantum advantage and theoretical or projected advantage throughout the analysis.
- Compare quantum performance against the best relevant classical alternatives rather than against naive or outdated baselines.
- Assess commercial usefulness separately from computational advantage, incorporating practical cost, scale, reliability, latency, and integration requirements.
- Synthesize the evidence into an overall judgment of how close quantum computers are to commercially useful advantages, while making uncertainty and differing application timelines explicit.

## Output Requirements

- Answer the question comparatively and provide an overall assessment of proximity to commercially useful advantage.
- Separate demonstrated results from theoretical or projected results.
- Identify and rank the biggest remaining technical barriers.
- Preserve the distinction between computational advantage and commercial usefulness.

---

# Iteration 1

## 1. Search

**Query**

> How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

**Purpose:** GENERAL

**Why this query**

This is the user's original research question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S1 — 5 Key Quantum Computing Breakthroughs in 2026**
  URL: https://www.bqpsim.com/blogs/quantum-computing-breakthroughs
- **S2 — 8 Industry Use Cases for Quantum Computing**
  URL: https://thequantuminsider.com/2026/05/04/quantum-computing-use-cases-real-applications-industries
- **S3 — Quantum computing: What leaders need to know now**
  URL: https://mitsloan.mit.edu/ideas-made-to-matter/quantum-computing-what-leaders-need-to-know-now
- **S4 — Quantum Computing – Strategic Recommendations for the ...**
  URL: https://arxiv.org/html/2601.08578v1
- **S5 — Quantum technology firms race to market as the industry sees ‘inflection point’**
  URL: https://www.cnbc.com/2026/03/30/quantum-computing-firms-go-public-breakthroughs-commercialization.html

**Search Duration:** 2.51s

---

## 2. Evidence Processing

- New claim proposals: 5
- Existing claim updates: 0
- New gaps: 5
- Resolved gaps: 0

**Processing Duration:** 19.84s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

The supplied sources do not document a quantum-computing demonstration that delivered commercially useful superiority over a strong classical baseline; reported industrial demonstrations remain pilots, proof-of-concept studies, or projections.

- S2 supports (direct): States that small-molecule simulations have been demonstrated but have not reached systems complex enough to displace classical methods, and that current hardware lacks the error rates and qubit counts for practically useful molecular simulation.
- S4 supports (indirect): Describes industrial optimization and machine-learning experiments benchmarked against classical solvers, while framing the work as an evaluation of promise and practical hurdles rather than reporting an established commercial advantage.
- S5 supports (direct): Characterizes quantum computing as still experimental and reports practical advantage only as an expectation around 2028–2029, with wider commercial use in the 2030s.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C2

**Claim**

Quantum molecular simulation, particularly for chemistry, materials, and drug-discovery problems, is presented as the most credible near- or medium-term application area, but useful deployment is projected to require substantially more capable, lower-error hardware and is not experimentally validated at commercially relevant scale in the supplied evidence.

- S2 supports (direct): Explains that molecular systems map naturally onto quantum hardware, identifies chemistry and materials as credible application areas, and projects drug-discovery applications on a roughly 5–10 year horizon contingent on hundreds of error-corrected logical qubits.
- S2 contradicts (direct): The same source limits the current evidence by stating that small-molecule demonstrations have not displaced classical methods and that current hardware is insufficient for useful molecular simulation.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C3

**Claim**

Optimization and machine-learning applications have not established a general quantum advantage: strong classical algorithms remain important comparators, and the supplied industrial evaluation framework treats scalability, solution quality, runtime, and transferability as unresolved practical tests.

- S2 supports (direct): States that many optimization problems have highly tuned classical algorithms that quantum approaches have not demonstrated they can beat, and describes optimization as a use case where hype exceeds evidence.
- S4 supports (direct): Reports that QCHALLenge benchmarks quantum approaches against classical solvers using model formulation, scalability, solution quality, runtime, and transferability, with outcomes ranging from a possible path to advantage to significant practical hurdles.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C4

**Claim**

The principal hardware barrier identified in the supplied sources is achieving sufficiently low error rates and scalable fault-tolerant computation; current limitations also include limited qubit counts, restricted connectivity, and error susceptibility.

- S1 supports (direct): Reports that pre-2026 NISQ systems had roughly 50–200 error-prone physical qubits, gate-error rates of 10^-3 to 10^-2, and decoherence that restricted reliable computation to shallow circuits; it presents later error-correction progress as a claimed engineering milestone.
- S2 supports (direct): States that current hardware lacks the error rates and qubit counts required for useful molecular simulation.
- S4 supports (direct): Identifies low qubit counts, limited connectivity, and error susceptibility as hardware limitations affecting hybrid industrial algorithms.
- S1 contradicts (direct): Claims that 2026 demonstrations showed logical error rates decreasing with added scale and that first fault-tolerant systems advanced, suggesting progress on—rather than elimination of—the error-correction barrier.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C5

**Claim**

Commercial usefulness should be evaluated as quantum economic advantage—better performance than a comparably priced classical computer—rather than as quantum advantage alone; relevant comparisons include runtime, cost, scale, solution quality, and operational overhead.

- S3 supports (direct): Defines quantum economic advantage as solving a problem faster with a quantum computer than with a comparably priced classical computer, and warns that classical computers may remain faster despite a quantum algorithm using fewer steps.
- S4 supports (direct): Uses scalability, solution quality, runtime, and transferability as evaluation criteria for industrial use cases and emphasizes benchmarking against classical solvers.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Gap G1

No supplied source gives a reproducible, independent experimental benchmark showing a quantum processor beating the best relevant classical hardware or workflow on a commercially meaningful task, including total cost, latency, reliability, and data/integration overhead.

### New Gap G2

The supplied evidence does not provide detailed results from the QCHALLenge optimization and machine-learning experiments, so the status of each industrial use case and the magnitude of any quantum-versus-classical performance difference remain unresolved.

### New Gap G3

The sources provide conditional application projections and a broad 5–10 year molecular-simulation estimate, but do not specify validated resource estimates, fault-tolerant logical-qubit requirements, runtime thresholds, or uncertainty ranges for commercially relevant workloads.

### New Gap G4

The evidence does not independently verify the optimistic claims about 2026 error-correction breakthroughs or establish whether demonstrated logical-error scaling is sufficient for useful applications.

### New Gap G5

Important system-level barriers—such as error-correction overhead, compilation, qubit connectivity at application scale, control and calibration, data loading, system cost, and integration reliability—are mentioned only partially and are not quantitatively ranked.

---

## 4. Current Research State

- Claims: 5
- Supported: 5
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 5
- Remaining Searches: 2

### Subquestion Progress

**SQ1:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ3:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ4:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → PARTIAL (targeted searches: 0)
- SQ3 → PARTIAL (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- None

**Remaining targeted searches:** 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ1

**Why**

A high-priority gap remains on SQ1: the evidence does not establish whether any experimentally demonstrated quantum advantage beats the strongest relevant classical baseline on a commercially meaningful task. Resolving this is central to distinguishing benchmark-specific computational advantage from practical business value.

**Next Search**

> Experimental quantum advantage demonstrations commercially useful tasks: independent benchmarks against best classical algorithms and hardware, including cost, runtime, solution quality, reliability, data-loading and integration overhead; identify any reproducible quantum economic advantage


---

# Iteration 2

## 1. Search

**Query**

> Experimental quantum advantage demonstrations commercially useful tasks: independent benchmarks against best classical algorithms and hardware, including cost, runtime, solution quality, reliability, data-loading and integration overhead; identify any reproducible quantum economic advantage

**Target:** SQ1

**Purpose:** SUBQUESTION

**Why this query**

A high-priority gap remains on SQ1: the evidence does not establish whether any experimentally demonstrated quantum advantage beats the strongest relevant classical baseline on a commercially meaningful task. Resolving this is central to distinguishing benchmark-specific computational advantage from practical business value.

5 result(s) retrieved; 4 new unique source(s) added.

- **S6 — Practical quantum advantage signals a new commercial ...**
  URL: https://q-ctrl.com/blog/practical-quantum-advantage-signals-a-new-commercial-era-for-quantum-computing
- **S7 — Where to Look for Quantum Advantage in your Benchmarking Data | Qubits26**
  URL: https://www.youtube.com/watch?v=KzaxcV_HSCY
- **S8 — The Power of Quantum Advantage Explained**
  URL: https://www.bluequbit.io/quantum-advantage
- **S9 — Quantum Advantage is Universally Demonstrable**
  URL: https://www.quera.com/blog-posts/mythbuster---quantum-advantage-is-universally-demonstrable

**Search Duration:** 2.47s

---

## 2. Evidence Processing

- New claim proposals: 2
- Existing claim updates: 5
- New gaps: 2
- Resolved gaps: 0

**Processing Duration:** 17.20s

---

## 3. Ledger Updates

### New Claim C6

**Claim**

Q-CTRL reports a 2026 demonstration in which an IBM quantum computer, combined with compiler and error-suppression software, solved a Fermionic Simulation materials problem more than 3,000 times faster in wall-clock time than a stated industry-standard classical alternative while meeting or exceeding its accuracy; the supplied source is a vendor report and does not independently establish the result's reproducibility, end-to-end cost advantage, or generality.

- S6 supports (direct): Q-CTRL claims a publicly available IBM quantum computer plus infrastructure software achieved a 3,000-times wall-clock speedup on a known-value, commercially relevant materials-simulation problem with practically relevant runtime and comparable or better accuracy.
- S9 contradicts (indirect): Warns that advantage claims should be assessed using the task, classical baseline, and end-to-end time-to-answer, including compilation, queueing, execution, and post-processing; it does not specifically evaluate the Q-CTRL claim.

**Confidence:** LOW

**Status:** WEAK

### New Claim C7

**Claim**

Empirical claims of quantum advantage for quantum annealing are highly sensitive to benchmark design, including whether scaling or runtime is measured, whether anneal time or access time is counted, the solution-quality metric, hardware topology, and whether the classical solver addresses the physical or logically embedded problem.

- S7 supports (direct): A D-Wave literature review of roughly a decade of annealing-QPU studies reports conflicting outcomes and identifies experimental-design features that predict the observed result, including metrics, timing scope, topology, and problem-domain choice.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

The supplied sources do not document a quantum-computing demonstration that delivered commercially useful superiority over a strong classical baseline; reported industrial demonstrations remain pilots, proof-of-concept studies, or projections.

- S9 supports (direct): States that advantage remains workload-specific, that some demonstrations use specially designed problems with little practical use, and that end-to-end production metrics are often omitted.
- S6 contradicts (direct): Reports a claimed 3,000-times wall-clock speedup with comparable or better accuracy on a materials-simulation task of stated commercial relevance, which is a documented claim of practical advantage in the supplied sources.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → CONFLICTING

### Updated Claim C2

**Claim**

Quantum molecular simulation, particularly for chemistry, materials, and drug-discovery problems, is presented as the most credible near- or medium-term application area, but useful deployment is projected to require substantially more capable, lower-error hardware and is not experimentally validated at commercially relevant scale in the supplied evidence.

- S6 supports (direct): Reports a materials-engineering Fermionic Simulation demonstration and argues that chemistry and materials workloads are attractive because classical scaling is poor.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C3

**Claim**

Optimization and machine-learning applications have not established a general quantum advantage: strong classical algorithms remain important comparators, and the supplied industrial evaluation framework treats scalability, solution quality, runtime, and transferability as unresolved practical tests.

- S7 supports (direct): Finds published annealing-QPU benchmark results ranging from negative to highly favorable and attributes much of the disagreement to benchmark design choices.
- S9 supports (direct): Says advantage is limited and workload-specific, highlights moving classical baselines, and recommends end-to-end time-to-answer, solution quality, throughput, and stability metrics.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

The principal hardware barrier identified in the supplied sources is achieving sufficiently low error rates and scalable fault-tolerant computation; current limitations also include limited qubit counts, restricted connectivity, and error susceptibility.

- S6 supports (direct): States that noise and errors have historically prevented useful results on relevant problems and presents compiler and error-suppression infrastructure as necessary to reach larger useful calculations.
- S9 supports (direct): Identifies error correction, hardware and software maturity, and stability or recalibration requirements as practical obstacles to production use.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

Commercial usefulness should be evaluated as quantum economic advantage—better performance than a comparably priced classical computer—rather than as quantum advantage alone; relevant comparisons include runtime, cost, scale, solution quality, and operational overhead.

- S6 supports (direct): Defines practical quantum advantage as outperforming the best available conventional alternative on a real-world problem in a way that is better, faster, or more affordable.
- S9 supports (direct): Recommends production-oriented comparisons based on end-to-end time-to-answer, solution quality, throughput, and stability rather than headline benchmark results.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### New Gap G6

The S6 reported 3,000-times materials-simulation result lacks, in the supplied material, the full benchmark specification, classical hardware and software details, inclusion of queueing/compilation/data-transfer/post-processing time, total cost or energy comparison, uncertainty, and independent replication needed to determine whether it is a reproducible commercial advantage.

### New Gap G7

The supplied benchmarking evidence indicates that annealing-QPU conclusions depend strongly on experimental design, but does not quantify which benchmark conditions reliably produce a commercially meaningful advantage on current hardware or establish performance against contemporary production workflows.

---

## 4. Current Research State

- Claims: 7
- Supported: 5
- Weak: 1
- Conflicting: 1
- Insufficient Evidence: 0
- Open Gaps: 7
- Remaining Searches: 1

### Subquestion Progress

**SQ1:** PARTIAL → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ2:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ3:** PARTIAL → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ4:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

### Research Plan Status

**CORE:**

- SQ1 → CONFLICTING (targeted searches: 1)
- SQ2 → PARTIAL (targeted searches: 0)
- SQ3 → CONFLICTING (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- None

**Remaining targeted searches:** 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ1

**Why**

SQ1 is CORE, conflicting, and its central unresolved issue is whether the reported 3,000× materials result or any other demonstration survives independent scrutiny against a strong classical baseline with end-to-end commercial metrics. One focused countersearch could materially distinguish a vendor claim from validated quantum economic advantage.

**Next Search**

> Independent evaluation or replication of Q-CTRL 3,000× quantum materials simulation speedup: benchmark specification, classical hardware/software baseline, accuracy, compilation and queueing time, total cost/energy, reproducibility, and comparison with other experimentally demonstrated commercially relevant quantum advantages


---

# Iteration 3

## 1. Search

**Query**

> Independent evaluation or replication of Q-CTRL 3,000× quantum materials simulation speedup: benchmark specification, classical hardware/software baseline, accuracy, compilation and queueing time, total cost/energy, reproducibility, and comparison with other experimentally demonstrated commercially relevant quantum advantages

**Target:** SQ1

**Purpose:** SUBQUESTION

**Why this query**

SQ1 is CORE, conflicting, and its central unresolved issue is whether the reported 3,000× materials result or any other demonstration survives independent scrutiny against a strong classical baseline with end-to-end commercial metrics. One focused countersearch could materially distinguish a vendor claim from validated quantum economic advantage.

5 result(s) retrieved; 5 new unique source(s) added.

- **S10 — Q-CTRL Achieves 3,000x Speedup in Quantum Materials Simulation - Quantum Computing Report**
  URL: https://quantumcomputingreport.com/q-ctrl-achieves-3000x-speedup-in-quantum-materials-simulation
- **S11 — Q-CTRL Delivers 3000x Speedup in Materials Discovery for the Energy ...**
  URL: https://q-ctrl.com/blog/q-ctrl-delivers-3-000x-speedup-in-materials-discovery-for-the-energy-sector-with-quantum-computing-and-demonstrates-evidence-of-practical-quantum-advantage
- **S12 — Q-CTRL Claims Practical Quantum Advantage**
  URL: https://postquantum.com/industry-news/qctrl-fermi-hubbard-3000x-quantum-speedup
- **S13 — Q-CTRL Delivers 3000x Speedup in Materials Discovery ...**
  URL: https://thequantuminsider.com/2026/05/06/qctrl-practical-quantum-advantage-materials-discovery
- **S14 — Solve complex materials-science problems with the new ...**
  URL: https://q-ctrl.com/blog/solve-complex-materials-science-problems-with-the-new-fire-opal-quantum-dynamics-simulator

**Search Duration:** 3.77s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 5
- New gaps: 2
- Resolved gaps: 0

**Processing Duration:** 17.05s

---

## 3. Ledger Updates

### New Claim C8

**Claim**

A third-party report describes a classical Majorana Propagation method reproducing the Q-CTRL 120-qubit Fermi–Hubbard data for a single site in approximately 2 minutes 30 seconds on a standard MacBook Air, while noting that the comparison is incomplete because the method computes observables separately whereas the quantum processor produces many observables simultaneously; therefore, the reported 3,000-times speedup is sensitive to the observable scope and classical baseline.

- S12 supports (direct): Reports Algorithmiq results reproducing a single-site quantum simulation in 2 minutes 30 seconds and explains that Majorana Propagation computes one observable at a time, unlike the quantum processor's simultaneous generation of many observables.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

The supplied sources do not document a quantum-computing demonstration that delivered commercially useful superiority over a strong classical baseline; reported industrial demonstrations remain pilots, proof-of-concept studies, or projections.

- S12 supports (direct): Provides a third-party analysis that initially reports a classical method narrowing the claimed 3,000-times advantage, then explains that the full multi-observable and accuracy comparison remains unresolved; this supports treating the result as a reported demonstration rather than established commercial superiority.
- S13 supports (indirect): Reproduces the vendor-reported 3,000-times speedup and commercial-relevance framing, but does not independently validate the result.
- S14 supports (indirect): Reports Q-CTRL's claimed 3,000-times speedup and later productization of the workflow, while presenting the result as a company demonstration rather than independent evidence of broad commercial advantage.

**Confidence:** MEDIUM → MEDIUM

**Status:** CONFLICTING → CONFLICTING

### Updated Claim C2

**Claim**

Quantum molecular simulation, particularly for chemistry, materials, and drug-discovery problems, is presented as the most credible near- or medium-term application area, but useful deployment is projected to require substantially more capable, lower-error hardware and is not experimentally validated at commercially relevant scale in the supplied evidence.

- S10 supports (direct): Describes a 120-qubit Fermi–Hubbard simulation with reported 3,000-times wall-clock speedup against a TDVP classical benchmark and agreement within 1% RMSE.
- S12 supports (direct): Characterizes the Fermi–Hubbard demonstration as technically substantial and among the largest and most accurate reported gate-based digital simulations, while preserving uncertainty about the breadth of the advantage.
- S14 supports (direct): States that Q-CTRL's Fire Opal workflow applies the demonstrated dynamics-simulation techniques to materials science and energy problems, with reported agreement within 1% RMSE against high-resolution tensor-network simulations.
- S12 contradicts (direct): Reports a newer classical Majorana Propagation result that can reproduce a single-site output nearly as quickly as the quantum processor, indicating that the claimed advantage may depend on the observable set and selected classical baseline.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → CONFLICTING

### Updated Claim C5

**Claim**

Commercial usefulness should be evaluated as quantum economic advantage—better performance than a comparably priced classical computer—rather than as quantum advantage alone; relevant comparisons include runtime, cost, scale, solution quality, and operational overhead.

- S12 supports (direct): Shows that commercial comparison depends on what outputs are counted: the quantum processor produces many observables simultaneously, while a competing classical method computes them separately; it also raises accuracy and baseline-selection issues.
- S10 supports (direct): States that the comparison used wall-clock execution time and comparable accuracy against a TDVP solver, while noting that future classical algorithms or GPU-accelerated tensor networks could change the comparison.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C6

**Claim**

Q-CTRL reports a 2026 demonstration in which an IBM quantum computer, combined with compiler and error-suppression software, solved a Fermionic Simulation materials problem more than 3,000 times faster in wall-clock time than a stated industry-standard classical alternative while meeting or exceeding its accuracy; the supplied source is a vendor report and does not independently establish the result's reproducibility, end-to-end cost advantage, or generality.

- S10 supports (direct): Independent reporting describes the 120-qubit Fermi–Hubbard simulation, approximately two-minute quantum execution, over-100-hour TDVP comparison, and agreement within 1% RMSE.
- S11 supports (direct): Q-CTRL reports a 3,000-times speedup over performance-optimized industry-standard classical software on a known materials-science problem, with accuracy meeting stated expectations.
- S13 supports (indirect): Repeats the reported 3,000-times comparison and the use of Q-CTRL error-suppression software on a 120-qubit simulation.
- S14 supports (direct): Reports the demonstration's 1% RMSE comparison and says the associated Fire Opal workflow has been made available to users.
- S12 contradicts (direct): Reports that Algorithmiq's Majorana Propagation method reproduced a single-site output in about 2 minutes 30 seconds on a MacBook Air, narrowing the claimed advantage against at least one newer classical method; it also states that the full multi-observable comparison and quantitative accuracy remain under discussion.

**Confidence:** LOW → MEDIUM

**Status:** WEAK → CONFLICTING

### Updated Claim C3

**Claim**

Optimization and machine-learning applications have not established a general quantum advantage: strong classical algorithms remain important comparators, and the supplied industrial evaluation framework treats scalability, solution quality, runtime, and transferability as unresolved practical tests.

- S12 supports (direct): Shows that a claimed advantage can change when a newer classical method is used and when the comparison changes from one observable to the complete set of outputs, reinforcing sensitivity to classical baselines and benchmark scope.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### New Gap G8

The supplied sources do not independently adjudicate the full Q-CTRL-versus-Majorana Propagation comparison: it remains unclear whether the classical method can reproduce the complete set of observables at comparable accuracy and total time, including any required repeated runs and data-processing overhead.

### New Gap G9

The supplied sources mention independent tests of the Q-CTRL simulation but do not provide their methods, quantitative results, or scope, so the claimed 1% accuracy and 3,000-times advantage cannot yet be assessed as independently replicated across the full workload.

---

## 4. Current Research State

- Claims: 8
- Supported: 5
- Weak: 0
- Conflicting: 3
- Insufficient Evidence: 0
- Open Gaps: 9
- Remaining Searches: 0

### Subquestion Progress

**SQ1:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ2:** PARTIAL → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ3:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ4:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

### Research Plan Status

**CORE:**

- SQ1 → CONFLICTING (targeted searches: 2)
- SQ2 → CONFLICTING (targeted searches: 0)
- SQ3 → CONFLICTING (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- None

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

- No supplied source gives a reproducible, independent experimental benchmark showing a quantum processor beating the best relevant classical hardware or workflow on a commercially meaningful task, including total cost, latency, reliability, and data/integration overhead.
- The supplied evidence does not provide detailed results from the QCHALLenge optimization and machine-learning experiments, so the status of each industrial use case and the magnitude of any quantum-versus-classical performance difference remain unresolved.
- The sources provide conditional application projections and a broad 5–10 year molecular-simulation estimate, but do not specify validated resource estimates, fault-tolerant logical-qubit requirements, runtime thresholds, or uncertainty ranges for commercially relevant workloads.
- The evidence does not independently verify the optimistic claims about 2026 error-correction breakthroughs or establish whether demonstrated logical-error scaling is sufficient for useful applications.
- Important system-level barriers—such as error-correction overhead, compilation, qubit connectivity at application scale, control and calibration, data loading, system cost, and integration reliability—are mentioned only partially and are not quantitatively ranked.
- The S6 reported 3,000-times materials-simulation result lacks, in the supplied material, the full benchmark specification, classical hardware and software details, inclusion of queueing/compilation/data-transfer/post-processing time, total cost or energy comparison, uncertainty, and independent replication needed to determine whether it is a reproducible commercial advantage.
- The supplied benchmarking evidence indicates that annealing-QPU conclusions depend strongly on experimental design, but does not quantify which benchmark conditions reliably produce a commercially meaningful advantage on current hardware or establish performance against contemporary production workflows.
- The supplied sources do not independently adjudicate the full Q-CTRL-versus-Majorana Propagation comparison: it remains unclear whether the classical method can reproduce the complete set of observables at comparable accuracy and total time, including any required repeated runs and data-processing overhead.
- The supplied sources mention independent tests of the Q-CTRL simulation but do not provide their methods, quantitative results, or scope, so the claimed 1% accuracy and 3,000-times advantage cannot yet be assessed as independently replicated across the full workload.
- SQ1: What quantum-computing advantages over classical computers have been experimentally demonstrated to date, and do any constitute commercially useful advantages? (CONFLICTING: At least one linked ledger claim contains conflicting evidence.)
- SQ2: What quantum-computing advantages are theoretically established or currently projected for commercially relevant applications, and how plausible and near-term are those projections? (CONFLICTING: At least one linked ledger claim contains conflicting evidence.)
- SQ3: What classical methods and hardware must quantum computers outperform for an advantage to be commercially meaningful? (CONFLICTING: At least one linked ledger claim contains conflicting evidence.)
- SQ4: What are the biggest remaining technical barriers preventing quantum computers from delivering commercially useful advantages, and how do those barriers affect the expected path to adoption? (PARTIAL: Open high- or medium-importance research gaps still block a sufficient answer.)

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Question Decomposition | 1 | 8.71s |
| Tavily Search | 3 | 8.75s |
| Evidence Processing | 3 | 54.09s |
| Research Decision | 2 | 6.23s |
| Report Generation | 1 | 0.00s |
| Total Run | — | 102.05s |
