# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 13

**OpenAI Calls:** 4

**Tavily Calls:** 3

**Started:** 2026-08-31T17:02:25-04:00

**Ended:** 2026-08-31T17:03:49-04:00

**Total Runtime:** 84.10s

---

# Iteration 1

## 1. Search

**Query**

> How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

**Why this query**

This is the user's original research question.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S1 — 5 Key Quantum Computing Breakthroughs in 2026**
  URL: https://www.bqpsim.com/blogs/quantum-computing-breakthroughs
- **S2 — 8 Industry Use Cases for Quantum Computing**
  URL: https://thequantuminsider.com/2026/05/04/quantum-computing-use-cases-real-applications-industries
- **S3 — Quantum Computing – Strategic Recommendations for the Industry**
  URL: https://arxiv.org/html/2601.08578v1
- **S4 — Quantum computing: What leaders need to know now**
  URL: https://mitsloan.mit.edu/ideas-made-to-matter/quantum-computing-what-leaders-need-to-know-now
- **S5 — Quantum technology firms race to market as the industry sees ‘inflection point’**
  URL: https://www.cnbc.com/2026/03/30/quantum-computing-firms-go-public-breakthroughs-commercialization.html

**Search Duration:** 2.41s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The provided evidence does not establish a commercially useful quantum advantage over classical computers today.

**Confidence:** Medium

**Why this confidence level**

Three sources consistently characterize present systems as immature or application-limited, but none supplies a comprehensive, independently verified benchmark of commercial workloads.

**Evidence**

- The industry-use-case review says current quantum hardware has not reached molecular-simulation systems complex enough to displace classical methods, and that current error rates and qubit counts remain insufficient for practically useful simulation. [S2]
- The MIT Sloan summary says the field is “not quite ready for prime time” and emphasizes that most small- and moderate-sized business problems will not benefit from quantum computing. [S4]
- The industrial QCHALLenge paper describes benchmarking NISQ and hybrid algorithms against classical solvers, implying that competitiveness and practical applicability remain subjects of evaluation rather than established outcomes. [S3]

#### Finding 2

**Claim**

Some forms of quantum advantage have been demonstrated in specialized or artificial computational tasks, but the supplied sources do not document a demonstrated advantage on a commercially relevant workload.

**Confidence:** Medium

**Why this confidence level**

The sources support a distinction between laboratory milestones and business value, but they do not provide primary experimental evidence for or against all forms of demonstrated quantum advantage.

**Evidence**

- S4 distinguishes the goal of quantum advantage—solving problems beyond classical reach—from quantum economic advantage, where a quantum computer is faster than a comparably priced classical system; it does not report that either has been achieved commercially. [S4]
- S1 claims major 2026 error-correction and fault-tolerance milestones, but the retrieved excerpt does not provide enough detail to connect those milestones to a useful application or a fair classical comparison. [S1]
- S2 reports small-molecule demonstrations but explicitly says they have not reached systems capable of displacing classical methods. [S2]

#### Finding 3

**Claim**

The most credible projected application area in the supplied material is quantum chemistry and molecular simulation, especially drug discovery and materials science; optimization and quantum machine learning are less established.

**Confidence:** Medium

**Why this confidence level**

The application ranking is consistent across the industry review and the research whitepaper, but the timeline and commercial projections are conditional and not validated demonstrations.

**Evidence**

- S2 identifies molecular simulation as the most viable near-term application area because quantum systems map naturally onto quantum hardware, while describing optimization, AI, and climate modeling as longer-term or uncertain. [S2]
- S2 says likely early commercial applications would address specific bottlenecks rather than replace complete drug-discovery pipelines, with a commonly cited five-to-ten-year projection conditional on hundreds of error-corrected logical qubits. [S2]
- The QCHALLenge framework evaluates optimization and machine-learning use cases using model formulation, scalability, solution quality, runtime, and transferability, and explicitly allows outcomes in which classical methods remain superior. [S3]

#### Finding 4

**Claim**

The central technical barrier is scalable fault-tolerant computation: physical qubits must be converted into sufficiently numerous, high-quality logical qubits with low logical error rates.

**Confidence:** High

**Why this confidence level**

Multiple sources directly identify errors, scaling, logical-qubit supply, and connectivity as limiting factors.

**Evidence**

- S1 describes prior NISQ systems as having roughly 50–200 error-prone physical qubits, gate errors of 10^-3 to 10^-2, and decoherence on microsecond-to-millisecond timescales; it presents error correction as a major threshold still being crossed. [S1]
- S2 states that practically useful molecular simulation requires substantially lower error rates and larger qubit counts, citing hundreds of error-corrected logical qubits as a condition for a projected application. [S2]
- S3 highlights low qubit counts, limited connectivity, and error susceptibility as hardware limitations that hybrid software attempts to mitigate. [S3]

#### Finding 5

**Claim**

Even if fault-tolerant hardware becomes available, a quantum speedup will not automatically translate into commercial or economic advantage.

**Confidence:** High

**Why this confidence level**

The sources independently make the same methodological point: practical advantage requires end-to-end, cost-aware benchmarking against strong classical baselines.

**Evidence**

- MIT’s framework says classical computers generally process individual steps faster, so a quantum algorithm’s shorter algorithmic path may still lose in wall-clock time; it recommends comparing quantum performance with a comparably priced classical computer. [S4]
- The QCHALLenge methodology requires comparisons on runtime, solution quality, scalability, and transferability, rather than relying on qubit count or theoretical complexity alone. [S3]
- S2 notes that many optimization problems have highly tuned classical algorithms and that quantum approaches have not demonstrated an ability to beat them. [S2]

### Conflicts Found

- S1 presents 2026 error-correction and fault-tolerant progress as having shifted quantum computing toward commercially viable engineering, whereas S2 and S3 continue to describe practical application advantage as unproven or under evaluation. This is a conditional disagreement: hardware progress may improve future prospects without demonstrating present commercial superiority. [S1] [S2] [S3]
- S1 claims a Google Willow result showing logical error rates decreasing with scale and refers to “first fault-tolerant systems,” but the supplied excerpt is truncated and does not substantiate the scope, reproducibility, or application relevance of those claims. This conflicts with treating the claims as established evidence, not necessarily with the underlying experiments. [S1]
- Projected timelines differ in emphasis: S2 cites five-to-ten years for selected molecular-simulation applications conditional on major hardware progress, while S5 reports an analyst expectation of practical advantage around 2028–2029 and wider commercial use in the 2030s. These are forecasts, not demonstrations, and their assumptions are not specified consistently. [S2] [S5]

### Important Gaps

- Has any quantum processor demonstrated a reproducible advantage on a commercially relevant task using a fair comparison with the best classical algorithm, including data-loading, error-mitigation, runtime, and total cost?
- What exact logical-qubit count, logical error rate, circuit depth, and error-correction overhead are required for useful chemistry, materials, optimization, or cryptographic workloads?
- Do the 2026 hardware claims in S1 represent peer-reviewed, independently replicated results, and do they scale to application-sized circuits?
- How do the evaluated QCHALLenge use cases perform quantitatively against state-of-the-art classical solvers, rather than generic baselines?
- What are the full operational costs and reliability requirements of quantum systems, including cryogenics, control hardware, cloud access, compilation, and repeated measurements?

**Analysis Duration:** 18.59s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

A further search would materially improve the answer because the supplied material is dominated by future-dated commentary, forecasts, and industry or promotional sources. It lacks primary evidence for the key distinction requested: demonstrated quantum advantage versus projected advantage, especially fair commercial benchmarks and independently verified fault-tolerant results.

**Next Search**

> peer-reviewed demonstrated quantum advantage commercially relevant application benchmark versus state-of-the-art classical computer 2023 2024

---

# Iteration 2

## 1. Search

**Query**

> peer-reviewed demonstrated quantum advantage commercially relevant application benchmark versus state-of-the-art classical computer 2023 2024

**Why this query**

A further search would materially improve the answer because the supplied material is dominated by future-dated commentary, forecasts, and industry or promotional sources. It lacks primary evidence for the key distinction requested: demonstrated quantum advantage versus projected advantage, especially fair commercial benchmarks and independently verified fault-tolerant results.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S6 — Quantum Advantage is Universally Demonstrable**
  URL: https://www.quera.com/blog-posts/mythbuster---quantum-advantage-is-universally-demonstrable
- **S7 — Forecast for Quantum Computing Still Looks Bright | BCG**
  URL: https://www.bcg.com/publications/2024/long-term-forecast-for-quantum-computing-still-looks-bright
- **S8 — The Power of Quantum Advantage Explained**
  URL: https://www.bluequbit.io/quantum-advantage
- **S9 — Quantum advantage reassessed: More realistic benchmarks for quantum algorithms**
  URL: https://phys.org/news/2026-08-quantum-advantage-reassessed-realistic-benchmarks.html

**Search Duration:** 2.22s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources reinforce that quantum advantage is task-specific rather than a general replacement for classical computing, and that broad commercially useful advantage remains unestablished.

**Confidence:** High

**Why this confidence level**

Multiple sources, including a technical review summary and an industry source, consistently distinguish narrow demonstrations from broad commercial utility.

**Evidence**

- QuEra states that advantage is workload-specific and that demonstrations have been limited to specialized contexts, with some involving specially designed problems of little practical use. [S6]
- The review reported by Phys.org says practical advantage has not yet been demonstrated for many applications and that research relies substantially on theoretical models and simulations. [S9]
- Prior evidence similarly finds that current systems have not displaced classical methods on commercially relevant molecular simulations or typical business problems. [S2] [S4]

#### Finding 2

**Claim**

There is evidence for demonstrated beyond-classical performance in specialized or artificial tasks, but the new sources do not establish a reproducible commercial advantage against the best classical method.

**Confidence:** Medium

**Why this confidence level**

The sources support the conceptual and practical distinction, but S6 does not identify specific experiments, datasets, classical baselines, or independently verified performance results.

**Evidence**

- QuEra reports limited demonstrations in specialized contexts, while warning that some benchmark problems have little or no practical use. [S6]
- QuEra distinguishes task-specific quantum advantage from supremacy-style demonstrations such as random-circuit sampling, which may show beyond-classical behavior without providing application-level value. [S6]
- The existing evidence records small-molecule demonstrations and other hardware milestones but no commercially relevant workload with a complete, fair classical comparison. [S1] [S2] [S4]

#### Finding 3

**Claim**

Projected advantages remain most credible in quantum simulation, especially chemistry and materials, but realistic modeling substantially complicates the path from theory to useful applications.

**Confidence:** Medium

**Why this confidence level**

The evidence identifies plausible application areas and important caveats, but the chemistry and optimization results are projections, simulations, or methodological proposals rather than deployed commercial demonstrations.

**Evidence**

- S9 identifies quantum simulation as a promising route, but notes that much quantum-chemistry work uses idealized closed-system, unitary-dynamics and ground-state assumptions that do not fully describe real molecules and materials. [S9]
- S2 identifies molecular simulation as the strongest near-term candidate and conditions early commercial use on substantially larger numbers of error-corrected logical qubits. [S2]
- S9 reports that simulated QAOA portfolio-optimization results suggest scaling advantages may be possible over the examined range, but emphasizes that only large-instance scaling against classical methods could establish reliable advantage. [S9]

#### Finding 4

**Claim**

Scalable fault-tolerant computation remains the principal technical barrier, and application requirements are not yet sufficiently pinned down.

**Confidence:** High

**Why this confidence level**

The barrier is supported across several sources and includes both hardware scaling and algorithm/model realism.

**Evidence**

- Existing sources identify physical-qubit errors, limited connectivity, decoherence, insufficient qubit counts, and the need for many high-quality logical qubits as central constraints. [S1] [S2] [S3]
- S8 and S9 independently emphasize error correction, hardware and software maturity, and realistic benchmarking as prerequisites for practical utility. [S8] [S9]
- S9 adds that useful chemistry algorithms must handle open-system dynamics and dissipation, not only idealized closed-system calculations. [S9]

#### Finding 5

**Claim**

Commercial advantage requires end-to-end, workload-specific benchmarking, not merely a favorable asymptotic speedup, qubit count, or isolated device milestone.

**Confidence:** High

**Why this confidence level**

The same evaluation standard appears consistently across the new and prior sources.

**Evidence**

- QuEra recommends measuring time-to-answer including queueing, compilation, execution, and post-processing, alongside solution quality, throughput, reproducibility, and calibration stability. [S6]
- MIT’s framework requires comparison with a comparably priced classical computer, while QCHALLenge evaluates runtime, solution quality, scalability, and transferability. [S3] [S4]
- S9 likewise argues that small-scale QAOA demonstrations are insufficient and that scaling on large instances is the relevant test. [S9]

### Conflicts Found

- S6 says quantum advantage has been demonstrated in certain specialized optimization contexts, whereas the accumulated findings state that no demonstrated advantage on a commercially relevant workload has been established. These claims are compatible if “quantum advantage” includes narrow or artificial tasks but not commercial production workloads. [S6] [S2] [S3] [S4]
- S9 reports simulated portfolio-optimization scaling advantages as potentially possible, while S2 and S3 state that quantum approaches have not demonstrated superiority over strong classical optimization methods. The difference is between simulation-based projected scaling and experimentally demonstrated, end-to-end superiority. [S9] [S2] [S3]
- S6 is a vendor opinion article and S8 is an explanatory commercial article; their broad claims about use cases are less evidentially strong than the technical and peer-reviewed material summarized in S9. This is an evidence-quality difference rather than a direct factual contradiction. [S6] [S8] [S9]

### Important Gaps

- Has any specialized optimization demonstration cited by S6 survived comparison with the best current classical algorithms, including full end-to-end execution costs and independently reproducible results?
- What specific logical-qubit counts, logical error rates, circuit depths, and overheads are required for commercially valuable chemistry or materials workloads?
- Can the open-system approaches discussed in S9 be implemented at useful scale on fault-tolerant hardware, and do they improve performance over classical chemistry methods?
- Do the simulated QAOA scaling advantages in S9 persist on larger instances, realistic data, hardware execution, and strong state-of-the-art classical baselines?
- What are the total operating costs, throughput, queueing, calibration, and reliability characteristics of proposed commercial systems?

**Analysis Duration:** 15.40s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new material strengthens the conclusion that present advantage is narrow and that projected advantages are conditional, but it does not resolve the most important empirical gap: a reproducible, commercially relevant, end-to-end comparison against the best classical alternative. It also leaves the specific optimization demonstrations and hardware milestones insufficiently documented.

**Next Search**

> reproducible quantum advantage commercially relevant workload end-to-end benchmark best classical algorithm optimization chemistry 2024 2025

---

# Iteration 3

## 1. Search

**Query**

> reproducible quantum advantage commercially relevant workload end-to-end benchmark best classical algorithm optimization chemistry 2024 2025

**Why this query**

The new material strengthens the conclusion that present advantage is narrow and that projected advantages are conditional, but it does not resolve the most important empirical gap: a reproducible, commercially relevant, end-to-end comparison against the best classical alternative. It also leaves the specific optimization demonstrations and hardware milestones insufficiently documented.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S10 — Quantum Optimization Algorithms Guide (2026)**
  URL: https://www.bqpsim.com/quantum-optimization/quantum-optimization-algorithms-guide
- **S11 — Practical quantum advantage signals a new commercial era for quantum computing | Q-CTRL**
  URL: https://q-ctrl.com/blog/practical-quantum-advantage-signals-a-new-commercial-era-for-quantum-computing
- **S12 — Quantum Computing Companies in 2026 (76 Major Players)**
  URL: https://thequantuminsider.com/2025/09/23/top-quantum-computing-companies
- **S13 — Quantinuum Researchers Demonstrate a new Optimization Algorithm that delivers solutions on H2 Quantum Computer**
  URL: https://www.quantinuum.com/blog/quantinuum-researchers-demonstrate-a-new-optimization-algorithm-that-delivers-solutions-on-h2-quantum-computer

**Search Duration:** 2.63s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

S11 reports a potentially important new claim of practical quantum advantage in materials simulation, but it is not yet sufficiently independently established to overturn the accumulated conclusion that commercial advantage remains unproven.

**Confidence:** Medium

**Why this confidence level**

S11 gives a specific and commercially framed result rather than a generic roadmap claim, but it is self-reported, the source excerpt is incomplete, and key benchmarking details are unavailable.

**Evidence**

- Q-CTRL claims that, using an IBM quantum computer plus compiler and error-suppression software, it solved a materials-simulation problem over 3,000 times faster in wall-clock time than a state-of-the-art industry-standard alternative, at practically relevant time and with accuracy meeting or exceeding user expectations. [S11]
- The claim is presented in a company technical blog and refers to an arXiv paper, but the retrieved content does not provide the paper's full benchmark definition, classical implementation, hardware execution details, total cost, reproducibility, or independent replication. [S11]
- Earlier evidence requires end-to-end comparison against strong classical baselines, including compilation, execution, post-processing, solution quality, and cost, before classifying a result as commercially useful advantage. [S3] [S4] [S6]

#### Finding 2

**Claim**

The new optimization sources do not demonstrate quantum superiority over classical optimization; they mainly report resource reductions, simulations, or company marketing claims.

**Confidence:** High

**Why this confidence level**

S13 directly acknowledges the missing classical comparison. S10 contains potentially relevant numerical claims but is a vendor guide and lacks enough methodological detail for strong evidentiary weight.

**Evidence**

- Quantinuum reports small-scale H2 experiments and simulations for an IQP-based heuristic that uses resources comparable to one-layer QAOA and may improve the probability of good solutions relative to that quantum baseline. [S13]
- Quantinuum explicitly states that it still wants to determine how the algorithm's solution quality and runtime compare with the best classical algorithms. [S13]
- BQPSim claims a hybrid quantum-annealing benchmark matched classical solver accuracy within 1% while reducing traffic congestion by 25%, but the page does not identify the benchmark design, classical solver, execution platform, independent validation, or full end-to-end costs. [S10]

#### Finding 3

**Claim**

Hybrid methods and software improvements may produce useful near-term gains, but they do not remove the fundamental need to establish quantum-specific advantage and scalable fault tolerance.

**Confidence:** High

**Why this confidence level**

Multiple sources support the continued role of hybridization and the persistence of noise and scaling constraints, although the performance claims in S10 are not independently substantiated.

**Evidence**

- S10 presents QAOA, VQE, and quantum annealing as deployable through hybrid quantum-classical workflows on current NISQ hardware and advertises speedups and circuit compression. [S10]
- The accumulated evidence identifies error rates, logical-qubit scaling, connectivity, runtime overhead, and strong classical baselines as continuing barriers even for hybrid approaches. [S1] [S2] [S3] [S6] [S9]
- S13 emphasizes reducing circuit depth and quantum resources because noise remains an unavoidable constraint on near-term devices. [S13]

#### Finding 4

**Claim**

The most consequential new development is not a confirmed broad commercial transition, but a potentially testable application-level claim in materials simulation that could narrow the gap if independently validated.

**Confidence:** Medium

**Why this confidence level**

The result is directly relevant to the research question but remains a single vendor-reported demonstration with unresolved benchmarking and replication questions.

**Evidence**

- S11 frames its result as a real-world materials-engineering task of known value, unlike artificial random-circuit-sampling demonstrations, and claims performance beyond exact classical solution at the tested scale. [S11]
- The prior evidence says materials and molecular simulation are the strongest projected application areas, while no commercially relevant workload had previously been established as superior under a complete fair comparison. [S2] [S9]
- S11's claim is limited to the specific studied task and does not establish general advantage across chemistry, optimization, or business workloads. [S11] [S6]

### Conflicts Found

- S11 claims that practical quantum advantage has now been achieved in a commercially relevant materials-simulation task, while the accumulated findings conclude that no reproducible commercial advantage has been established. This is a substantive but currently unresolved conflict because S11's underlying benchmark details and independent validation are not included. [S11] [S2] [S3] [S4] [S6] [S9]
- S10 advertises near-term hybrid quantum optimization as deployable and cites numerical benefits, whereas S13 explicitly says comparison with the best classical algorithms remains future work. The claims may concern different applications, but S10 cannot be treated as general evidence of quantum advantage. [S10] [S13]
- S11 reports a 3,000-times wall-clock speedup, while prior sources stress that meaningful comparisons must include queueing, compilation, execution, post-processing, solution quality, and cost. It is unclear whether S11's figure uses the same end-to-end boundary. [S11] [S3] [S4] [S6]
- S13 reports improved performance relative to one-layer QAOA, but that is a comparison with another quantum heuristic rather than with a state-of-the-art classical optimizer. [S13]

### Important Gaps

- What exactly is the materials-simulation instance in S11, and is it representative of a real customer workload rather than a specially selected benchmark?
- What classical method and hardware produced S11's baseline, and does the 3,000-times figure include data preparation, compilation, queueing, repeated measurements, error suppression, post-processing, and total operating cost?
- Does S11's reported accuracy remain competitive when compared with the best exact and approximate classical methods, not merely the cited industry-standard alternative?
- Has the S11 result been peer-reviewed, independently reproduced, or replicated on another quantum processor?
- Do BQPSim's traffic-congestion results in S10 come from actual quantum hardware, a simulator, or quantum-inspired computation?
- Do the Quantinuum results in S13 scale beyond small experiments and outperform strong classical optimization methods?
- What logical-qubit, error-rate, and circuit-depth requirements follow from the specific materials problem in S11?
- How much of the reported performance comes from software, classical preprocessing, or problem-specific compilation rather than quantum computation itself?

**Analysis Duration:** 18.01s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The runner reached the maximum research iteration budget. Analyzer assessment: S11 introduces a potentially decisive application-level claim, but the available source is a vendor announcement with incomplete benchmark details. Verifying the underlying arXiv paper and independent coverage would materially improve the answer. The optimization sources add no comparably strong evidence and do not close this gap.

**Stop Reason:** max_iterations

---

# Final Research Decision

**Research Stopped Because**

The runner reached the maximum research iteration budget.

**Stop Reason:** max_iterations

**Searches Performed:** 3

**Unique Sources:** 13

**Remaining Uncertainty**

- Whether the Q-CTRL materials result has been peer-reviewed, independently reproduced, or replicated on another quantum processor.
- The exact materials-simulation instance, classical baseline, hardware configuration, timing boundary, accuracy metric, and total cost underlying the reported 3,000-times speedup.
- Whether the claimed performance persists against the best exact and approximate classical methods rather than only an industry-standard alternative.
- Whether specialized optimization demonstrations survive comparisons using realistic instances, strong classical solvers, hardware execution, and complete end-to-end costs.
- The logical-qubit counts, logical error rates, circuit depths, and error-correction overhead required for useful chemistry, materials, optimization, and other workloads.
- Whether hybrid and open-system algorithmic approaches scale to application-sized problems and deliver value beyond classical preprocessing or problem-specific compilation.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 7.27s |
| OpenAI Analysis | 3 | 51.99s |
| Report Generation | 1 | 24.84s |
| Total Run | — | 84.10s |
