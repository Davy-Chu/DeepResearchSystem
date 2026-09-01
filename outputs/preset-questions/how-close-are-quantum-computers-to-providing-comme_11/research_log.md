# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 10 / 10

**Unique Sources:** 35

**OpenAI Calls:** 11

**Tavily Calls:** 10

**Started:** 2026-09-01T04:08:28-04:00

**Ended:** 2026-09-01T04:12:15-04:00

**Total Runtime:** 226.98s

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

- **S1 — Quantum Computing vs Classical Computing: Key Differences**
  URL: https://www.bluequbit.io/blog/quantum-computing-vs-classical-computing
- **S2 — Quantum computing - Wikipedia**
  URL: https://en.wikipedia.org/wiki/Quantum_computing
- **S3 — Practical quantum advantage signals a new commercial era for quantum computing | Q-CTRL**
  URL: https://q-ctrl.com/blog/practical-quantum-advantage-signals-a-new-commercial-era-for-quantum-computing
- **S4 — Quantinuum Unveils Accelerated Roadmap to Achieve Universal, Fully Fault-Tolerant Quantum Computing by 2030**
  URL: https://www.quantinuum.com/press-releases/quantinuum-unveils-accelerated-roadmap-to-achieve-universal-fault-tolerant-quantum-computing-by-2030
- **S5 — Quantum Computing by 2033: Which Industries Win or Wait?**
  URL: https://postquantum.com/quantum-utility-map/quantum-computing-2033-industries

**Search Duration:** 3.35s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The retrieved material supports a distinction between three notions of quantum advantage: demonstrations that are difficult for classical simulation but commercially irrelevant, theoretical or “absolute” advantage against the best conceivable classical method, and practical advantage against the best available method for a real-valued task.

**Confidence:** Medium

**Why this confidence level**

The distinction is clearly stated, but the source is a vendor blog and its account of current practical advantage is not independently corroborated in the retrieved material.

**Evidence**

- Q-CTRL explicitly contrasts Google’s 2019 supremacy demonstration, which it describes as commercially irrelevant, with “absolute Quantum Advantage” and its own definition of “Practical Quantum Advantage” as outperforming the best available conventional alternative on a real-world application. [S3]

#### Finding 2

**Claim**

At least one vendor claims a present-day, application-oriented quantum speedup: Q-CTRL reports more than 3,000-fold wall-clock acceleration for a materials-engineering/fermionic-simulation task using an IBM quantum computer plus compiler and error-suppression software.

**Confidence:** Low

**Why this confidence level**

This is a single self-reported claim from an interested vendor; the retrieved excerpt does not provide the benchmark details, classical hardware/software configuration, data, peer review outcome, or independent replication needed to classify it as demonstrated commercial quantum advantage.

**Evidence**

- Q-CTRL says its publicly available quantum computer and infrastructure software solved a problem of known value at meaningful scale, over 3,000 times faster in wall-clock time than an industry-standard classical alternative, with accuracy meeting or exceeding user expectations. [S3]

#### Finding 3

**Claim**

Earlier quantum-supremacy-style demonstrations do not by themselves establish commercially useful advantage.

**Confidence:** Medium

**Why this confidence level**

The source directly makes this point, and it is conceptually relevant, but only one retrieved source describes the specific demonstration.

**Evidence**

- Q-CTRL characterizes Google’s 2019 demonstration as a scientific milestone whose problem was designed to demonstrate that the quantum computer could run it and had no commercial or practical relevance. [S3]

#### Finding 4

**Claim**

The strongest projected use case in the retrieved material is fault-tolerant simulation of molecules, materials, and other quantum systems; projected benefits are not evidence that such advantages have already been delivered.

**Confidence:** Medium

**Why this confidence level**

The sources agree on simulation as the leading candidate, but S5 is an analysis/projection rather than a demonstrated result and S3 is promotional.

**Evidence**

- The 2033 scenario article argues that a 2,000-logical-qubit fault-tolerant machine would be especially suited to quantum-mechanical simulation, while stating that supply-chain optimization, machine learning, and derivatives pricing have no demonstrated advantage in that scenario. [S5]
- Q-CTRL similarly identifies fermionic and materials simulation as a candidate for durable advantage because the simulated systems follow quantum mechanics, while describing noise and errors as having prevented useful results on relevant problems until its claimed demonstration. [S3]

#### Finding 5

**Claim**

The central technical barrier is achieving scalable, reliable fault-tolerant computation: current systems require error suppression/correction and substantial growth from physical to logical qubits and from limited circuits to very large gate counts.

**Confidence:** High

**Why this confidence level**

The sources directly describe the engineering gap and provide a concrete logical-versus-physical-qubit milestone, although Quantinuum’s future milestones are company targets rather than independent validation.

**Evidence**

- Q-CTRL identifies hardware scale and errors as major obstacles, saying noise and errors degrade performance and have historically prevented useful results on relevant problems. [S3]
- Quantinuum’s roadmap targets thousands of physical qubits, hundreds of logical qubits, low error rates, and ultimately fully fault-tolerant operation capable of millions of gates; it reports 12 logical qubits on a 56-qubit system in 2024. [S4]

#### Finding 6

**Claim**

Additional barriers include decoherence and environmental sensitivity, specialized infrastructure, probabilistic outputs requiring repeated sampling, and the need to demonstrate end-to-end economic value against strong classical alternatives.

**Confidence:** Medium

**Why this confidence level**

These barriers are directly described, but S1 is a general commercial explainer and the retrieved sources do not quantify their current impact.

**Evidence**

- The overview source says quantum systems are sensitive to temperature, electromagnetic interference, and vibration; many platforms require highly controlled environments, and quantum programs require repeated runs and statistical analysis. [S1]
- Q-CTRL defines practical advantage in terms of solving a meaningful problem better, faster, or more affordably than the alternative users would actually buy, highlighting benchmarking and ROI as part of commercial usefulness. [S3]

### Conflicts Found

- The sources differ on whether practical commercial advantage has already arrived. Q-CTRL claims it has achieved practical advantage and positive ROI today, whereas its own discussion says useful results were previously prevented by noise and errors, and the other retrieved sources provide projections and roadmaps rather than an independently verified commercial deployment. [S3] [S4] [S5]
- Quantinuum presents 12 logical qubits and a roadmap toward commercial advantage by 2030, while S5 discusses a projected 2,000-logical-qubit capability around 2033. These are conditional company/analyst projections, not directly comparable demonstrations, and they imply different timelines and scale requirements. [S4] [S5]
- S1 says quantum systems can provide exponential scaling and practical advantages for optimization, cryptography, and simulation in general terms, while S5 specifically says there is no demonstrated advantage for supply-chain optimization, machine learning, or derivatives pricing in its projected scenario. [S1] [S5]

### Important Gaps

- Was Q-CTRL’s reported 3,000-fold speedup independently replicated or peer-reviewed, and what exact classical baseline, costs, preprocessing, error-mitigation overhead, and total workflow time were included?
- What commercially relevant tasks have been demonstrated by independent groups on current hardware, rather than merely claimed by hardware or software vendors?
- What logical-qubit count, logical error rate, circuit depth, runtime, data-loading cost, and total system cost are required for specific chemistry, materials, optimization, or cryptographic applications?
- How much of the projected advantage survives comparison with the best current classical algorithms, accelerators, heuristics, and approximate methods?
- Which hardware platforms have demonstrated scalable error correction rather than isolated logical-qubit milestones?
- The retrieved material does not adequately cover cryptographic applications, including the practical timeline and infrastructure implications of cryptographically relevant fault-tolerant algorithms.

**Analysis Duration:** 19.09s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

Another search would materially improve the answer. The current evidence is dominated by vendor and secondary sources, includes future-dated promotional claims, and lacks an independent, technically detailed assessment of demonstrated commercial advantage and present error-correction performance. The most important gap is verification of current practical-advantage claims against credible benchmarks.

**Next Search**

> independent peer-reviewed demonstrated practical quantum advantage 2024 2025 benchmark classical baseline commercial application error correction

---

# Iteration 2

## 1. Search

**Query**

> independent peer-reviewed demonstrated practical quantum advantage 2024 2025 benchmark classical baseline commercial application error correction

**Why this query**

Another search would materially improve the answer. The current evidence is dominated by vendor and secondary sources, includes future-dated promotional claims, and lacks an independent, technically detailed assessment of demonstrated commercial advantage and present error-correction performance. The most important gap is verification of current practical-advantage claims against credible benchmarks.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S6 — A Practical Framework for Evaluating Quantum Computing ...**
  URL: https://www.quera.com/blog-posts/a-practical-framework-for-evaluating-quantum-computing-claims
- **S7 — Quantum advantage through trusted quantum computation | IBM Quantum Computing Blog**
  URL: https://www.ibm.com/quantum/blog/quantum-advantage
- **S8 — Limits of quantum run-time advantage**
  URL: https://journals.aps.org/prapplied/abstract/10.1103/gpsf-pn1x
- **S9 — Benchmarking Quantum Computers: Towards a Standard Performance Evaluation Approach**
  URL: https://arxiv.org/html/2407.10941v3

**Search Duration:** 2.98s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The strongest current evidence supports the conclusion that commercially useful quantum advantage has not yet been demonstrated under rigorous, end-to-end comparisons on current hardware.

**Confidence:** High

**Why this confidence level**

The conclusion is supported by a peer-reviewed study with concrete case analyses and an independent benchmarking review. The sources address practical, real-world performance rather than only asymptotic complexity.

**Evidence**

- A peer-reviewed Physical Review Applied study concludes that, after including system-level overheads and using strong classical baselines, runtime-based quantum advantage has not yet been demonstrated on current NISQ hardware. Its Simon’s-problem case was about two orders of magnitude slower than a tuned classical implementation, and another reported optimization advantage disappeared under comprehensive benchmarking. [S8]
- A quantum-benchmarking review states that quantum computers have not yet demonstrated practical advantage over classical systems in real-world applications, while noting theoretical evidence for advantages on certain problems. [S9]

#### Finding 2

**Claim**

Recent demonstrations of computations beyond leading classical simulation methods should be classified as demonstrated technical or scientific quantum advantage, not demonstrated commercial advantage.

**Confidence:** Medium

**Why this confidence level**

The sources provide direct descriptions of technically difficult demonstrations and a useful classification framework, but S7 is an IBM account of its own work and the excerpt does not establish independent replication or commercial value.

**Evidence**

- IBM reports experiments using validation and error-mitigation methods on circuits of roughly 70–74 logical/physical-qubit scale that produced classically hard computations or quantum phenomena beyond leading simulations. The reported work emphasizes trustworthy validation of hard computations, not commercial production workloads or economic benefit. [S7]
- The evaluation framework separates quantum-supremacy experiments, which can show provable separation on commercially irrelevant problems, from useful case studies requiring real hardware, industry value, and demonstrated advantage. It says even examples approaching the useful category have not reached full industry scale. [S6]

#### Finding 3

**Claim**

Theoretical and projected advantages remain most credible for fault-tolerant simulation of molecules, materials, and other quantum systems, but these are prospective rather than delivered benefits.

**Confidence:** High

**Why this confidence level**

Multiple sources consistently distinguish theoretical algorithmic promise from practical demonstrations and converge on quantum-system simulation as the strongest prospective area.

**Evidence**

- The framework identifies production-scale drug-discovery simulation as a prospective use case with known industry value and theoretical advantage that awaits fault-tolerant hardware. [S6]
- The accumulated evidence identifies molecular, materials, and fermionic simulation as the leading projected use case, while reporting no demonstrated advantage for several proposed optimization, machine-learning, and finance applications in the cited scenario. [S3] [S5]
- The benchmarking review distinguishes theoretical evidence of significant advantage from the absence of practical real-world demonstrations. [S9]

#### Finding 4

**Claim**

A major obstacle is that quantum claims often omit or undercount the full end-to-end cost of computation, making apparent speedups unreliable.

**Confidence:** High

**Why this confidence level**

The issue is directly analyzed in a peer-reviewed study and independently expressed as a due-diligence requirement in the evaluation framework.

**Evidence**

- The runtime study says readout, transpilation, thermalization, and other system-level overheads cannot generally be excluded from current quantum runtime, and that doing so biases performance comparisons. [S8]
- The evaluation framework requires problem size, logical and physical resource estimates, computation time, solution cost, business benefit, and rigorous comparison with the best available classical solution. [S6]

#### Finding 5

**Claim**

The principal technical barrier remains scalable fault tolerance: sufficiently many reliable logical qubits, low logical error rates, and enough circuit depth to execute useful algorithms at production scale.

**Confidence:** High

**Why this confidence level**

The sources consistently identify error correction, logical scale, and circuit reliability as prerequisites; the precise application-specific thresholds remain unresolved.

**Evidence**

- The accumulated roadmap evidence describes a gap between current logical-qubit milestones and the thousands of logical qubits and very large gate counts expected for commercially important applications. [S4]
- IBM describes validation and error detection as steps toward fault-tolerant computation, including a reported roughly tenfold reduction in effective gate error in a 70-logical-qubit demonstration, indicating that error control and trustworthy execution remain central challenges. [S7]
- The prospective-use-case classification explicitly says production-scale applications such as drug-discovery simulation await fault-tolerant hardware. [S6]

#### Finding 6

**Claim**

Benchmarking and verification are themselves field-wide barriers: the community lacks sufficiently standardized, reproducible, fair, and application-relevant performance measures.

**Confidence:** High

**Why this confidence level**

Two sources independently identify inadequate benchmarking and verification as systemic obstacles, with overlapping concrete criteria.

**Evidence**

- The benchmarking review argues that quantum devices are difficult to compare using naive classical benchmarking methods and calls for metrics with relevance, reproducibility, fairness, verifiability, and usability; it also warns that vendor-defined benchmarks can create misleading incentives. [S9]
- The evaluation framework identifies independent verification, rigorous classical baselines, documentation quality, and production-scale problem sizing as essential criteria, noting that the intersection of industry value, working hardware, and provable advantage is rare. [S6]

### Conflicts Found

- Q-CTRL claims a present-day, application-oriented speedup, while the peer-reviewed runtime analysis concludes that no current NISQ runtime advantage has been demonstrated under end-to-end metrics. The disagreement may partly reflect different workloads, baselines, and accounting conventions, but the new study makes the Q-CTRL claim insufficient to establish general commercial advantage without independent full-workflow verification. [S3] [S8]
- IBM reports validated computations beyond leading classical simulation methods, whereas S8 and S9 define practical advantage more stringently in terms of real-world utility, total runtime, and comparison with the best classical alternatives. These claims are not necessarily contradictory: technical beyond-classical performance does not imply commercial advantage. [S7] [S8] [S9]
- S6 says some work is approaching the useful-case-study standard, while S9 states that practical real-world advantage has not yet been demonstrated. This is a difference in evidentiary threshold and degree of optimism, not a clear contradiction about full-scale commercial deployment. [S6] [S9]

### Important Gaps

- Which, if any, current application demonstrations meet all three requirements simultaneously: production-relevant problem size, real hardware execution, and independently verified advantage over the best classical workflow?
- For specific chemistry and materials workloads, what logical-qubit count, logical error rate, circuit depth, runtime, data-loading cost, and total system cost are required?
- Was the Q-CTRL 3,000-fold claim independently replicated using the end-to-end runtime and baseline standards described by S8?
- How much advantage remains after including quantum control, queueing, calibration, compilation, error mitigation/correction, readout, classical pre- and post-processing, and energy/capital costs?
- Which hardware platforms can scale from isolated logical-qubit demonstrations to sustained fault-tolerant computations with useful circuit depth?

**Analysis Duration:** 19.27s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new evidence substantially strengthens the answer that broad commercial advantage is not yet demonstrated, but an important question remains: whether any independent, application-specific case study has crossed the threshold from technical demonstration to commercially useful advantage. Resolving that would materially improve the answer's estimate of how close the field is.

**Next Search**

> independent peer-reviewed quantum computing practical advantage real-world application end-to-end classical benchmark 2025 2026

---

# Iteration 3

## 1. Search

**Query**

> independent peer-reviewed quantum computing practical advantage real-world application end-to-end classical benchmark 2025 2026

**Why this query**

The new evidence substantially strengthens the answer that broad commercial advantage is not yet demonstrated, but an important question remains: whether any independent, application-specific case study has crossed the threshold from technical demonstration to commercially useful advantage. Resolving that would materially improve the answer's estimate of how close the field is.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S10 — Why Quantum Is Here And Why It Is Not - The Innovator**
  URL: https://theinnovator.news/quantum-computing
- **S11 — The path to useful QC Special - The Week in Quantum Computing, July 6th 2026**
  URL: https://quantumpirates.substack.com/p/the-path-to-useful-qc-special-the
- **S12 — Quantum Computers: The Revolutionary Technology Transforming Computing in 2026 | SpinQ**
  URL: https://www.spinquanta.com/news-detail/quantum-computers-the-revolutionary-technology-transforming-computing-in-2026
- **S13 — Quantum computing: What leaders need to know now**
  URL: https://mitsloan.mit.edu/ideas-made-to-matter/quantum-computing-what-leaders-need-to-know-now

**Search Duration:** 3.51s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new material reinforces that quantum computing has produced important technical milestones and early commercial experiments, but has not yet become commercially indispensable or demonstrated broadly reproducible economic advantage.

**Confidence:** High

**Why this confidence level**

The new sources agree with the stronger prior evidence, although S10 and S11 are journalism/commentary rather than primary technical studies.

**Evidence**

- The Innovator describes extraordinary benchmarks and promising early commercial demonstrations, while explicitly stating that nothing is yet commercially indispensable and that a substantial gap remains to fault-tolerant systems. [S10]
- Quantum Pirates applies a strict standard requiring a real end-user task to outperform the state of the art in speed, accuracy, or cost, and reports that no quantum computer has delivered a practical commercial result under that standard. [S11]
- The accumulated peer-reviewed and benchmarking evidence likewise finds no demonstrated practical advantage under end-to-end comparisons on current NISQ hardware. [S8] [S9]

#### Finding 2

**Claim**

Google’s below-threshold error-correction result is a major technical milestone, not a demonstration of commercially useful quantum advantage.

**Confidence:** Medium

**Why this confidence level**

The source gives specific limitations and is consistent with the prior conclusion that technical supremacy and fault-tolerance milestones do not establish commercial value, but it is a secondary account and the underlying primary paper was not retrieved here.

**Evidence**

- The Innovator reports exponential error suppression as Google’s Willow code distance increased, but also states that the associated random-circuit benchmark was not practically useful, the logical error rate remained around 0.14% per cycle versus an estimated 10^-6 needed for meaningful large-scale algorithms, and the below-threshold result was shown in quantum memory rather than logic-gate operations. [S10]

#### Finding 3

**Claim**

Commercially relevant advantage remains most plausible for large, specialized problems—especially chemistry, materials, and quantum-system simulation—rather than ordinary business workloads.

**Confidence:** High

**Why this confidence level**

The conceptual conclusion is supported by MIT researchers’ framework and multiple prior sources, although the exact application boundaries remain problem-dependent.

**Evidence**

- MIT’s framework says small-to-moderate business problems generally will not benefit, while very large problems with exponential algorithmic gains or very large datasets are the more plausible beneficiaries. [S13]
- Prior sources identify fault-tolerant simulation of molecules and materials as the strongest projected use case, while lacking demonstrated advantage for several optimization, finance, and machine-learning workloads. [S3] [S5] [S6] [S9]

#### Finding 4

**Claim**

A key business test is economic advantage, not merely asymptotic speedup: the quantum workflow must beat a comparably priced classical alternative after accounting for the full system.

**Confidence:** High

**Why this confidence level**

The sources converge on the same end-to-end economic criterion, including a peer-reviewed runtime analysis and an independent academic framework.

**Evidence**

- MIT defines quantum economic advantage as solving a problem faster with a quantum computer than with a comparably priced classical computer, and emphasizes that classical systems often have much higher processing speed despite requiring more algorithmic steps. [S13]
- Prior benchmarking sources require inclusion of system-level overheads, strong classical baselines, solution quality, cost, and business benefit. [S6] [S8] [S9]

#### Finding 5

**Claim**

The main technical bottleneck remains scalable fault tolerance: current error-correction milestones are far below the reliability, logical-qubit, and circuit-depth requirements of production applications.

**Confidence:** High

**Why this confidence level**

Multiple sources identify error rates, logical scale, and sustained gate depth as the central engineering gap; company roadmaps remain projections rather than proof.

**Evidence**

- The Innovator reports Willow’s below-threshold memory result but notes that its logical error rate remains materially above the level estimated for large-scale algorithms and that logic-gate performance was not demonstrated by that result. [S10]
- Prior roadmap evidence identifies the gap between current logical-qubit milestones and the thousands of logical qubits and very large gate counts projected for useful applications. [S4] [S6] [S7]

### Conflicts Found

- S10 and S11 present or repeat optimistic claims about early commercial results, including IBM/HSBC bond-trading improvement, IBM molecule simulation, and IonQ medical-device simulation. These claims conflict with the stronger prior conclusion that practical advantage has not been independently demonstrated under rigorous end-to-end comparisons. The excerpts do not supply enough benchmark detail, independent replication, or full cost accounting to resolve the disagreement. [S10] [S11] [S8] [S9] [S12]
- S10 reports IBM’s claimed 34% improvement in bond-trading predictions and an alleged utility-scale molecule result, while S11’s stricter assessment says no quantum computer has delivered a practical commercial result. This may reflect different definitions of improvement, baseline, and utility rather than a direct logical contradiction, but the claims cannot be accepted as established commercial advantage from the supplied excerpts. [S10] [S11]
- S12 claims a 12% practical advantage for an IonQ medical-device simulation and presents broad application benefits, but it is a vendor source using promotional language and does not provide the independent, end-to-end evidence required by S8, S9, or the MIT economic framework. [S12] [S8] [S9] [S13]
- The new sources contain future-dated 2026 claims and roadmaps that differ in projected milestones and timelines, including IBM targets and reported logical-qubit counts. These are conditional projections or company-reported milestones, not comparable demonstrations of commercial capability. [S10] [S11] [S12]

### Important Gaps

- Can the IBM/HSBC, IBM/RIKEN, and IonQ medical-device claims be independently verified with disclosed problem sizes, classical hardware and algorithms, quantum execution data, total workflow time, and cost?
- Did Google’s below-threshold behavior extend from memory to useful logical gate operations at error rates suitable for application-scale circuits?
- Which specific applications can meet the economic-advantage standard after including calibration, queueing, compilation, error correction or mitigation, readout, classical processing, and infrastructure costs?
- What independently validated logical-qubit counts and logical error rates can be sustained over deep circuits, rather than demonstrated as isolated milestones?
- The supplied sources still do not adequately resolve the practical timeline and infrastructure implications of cryptographically relevant fault-tolerant algorithms.

**Analysis Duration:** 17.80s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The accumulated evidence is sufficient for the central conclusion—technical quantum advantage has been demonstrated on specialized benchmarks, but commercially useful advantage is not yet independently established. However, the new sources introduce several concrete commercial claims that could materially change the answer if independently validated. A focused search for primary or peer-reviewed evidence would therefore improve the assessment.

**Next Search**

> independent verification IBM HSBC 34% bond trading quantum Heron classical baseline 2025 quantum advantage

---

# Iteration 4

## 1. Search

**Query**

> independent verification IBM HSBC 34% bond trading quantum Heron classical baseline 2025 quantum advantage

**Why this query**

The accumulated evidence is sufficient for the central conclusion—technical quantum advantage has been demonstrated on specialized benchmarks, but commercially useful advantage is not yet independently established. However, the new sources introduce several concrete commercial claims that could materially change the answer if independently validated. A focused search for primary or peer-reviewed evidence would therefore improve the assessment.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S14 — HSBC and IBM Achieve 34% Performance Boost in Quantum-Enabled Bond Trading for 2025 | Quantum + AI Insiders**
  URL: https://quantumaiinsiders.com/hsbc-ibm-quantum-bond-trading-2025
- **S15 — HSBC and IBM achieve 34% improvement in bond trading with quantum computing | Liquid Technology posted on the topic | LinkedIn**
  URL: https://www.linkedin.com/posts/liquid-technology-inc_hsbcs-quantum-breakthrough-could-be-the-activity-7377357062411898880-kBAB
- **S16 — HSBC and IBM’s Quantum-Enabled Bond Trading Breakthrough**
  URL: https://postquantum.com/quantum-research/hsbc-ibm-quantum-advantage
- **S17 — Shtetl-Optimized » Blog Archive » HSBC unleashes yet another “qombie”: a zombie claim of quantum advantage that isn’t**
  URL: https://scottaaronson.blog?p=9170
- **S18 — HSBC demonstrates world’s first-known quantum-enabled algorithmic trading with IBM**
  URL: https://www.hsbc.com/news-and-views/news/media-releases/2025/hsbc-demonstrates-worlds-first-known-quantum-enabled-algorithmic-trading-with-ibm

**Search Duration:** 2.40s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The HSBC–IBM bond-trading result should be classified as an interesting hybrid quantum-machine-learning experiment, not established commercial quantum advantage.

**Confidence:** High

**Why this confidence level**

The sources consistently describe the result as a hybrid predictive-model experiment, and S16 provides important methodological detail. However, the primary paper itself was not retrieved in full here.

**Evidence**

- HSBC reports a trial using IBM Heron and quantum-generated features that improved bond-trade fill-prediction performance by up to 34% relative to classical-only methods. [S18] [S14] [S15]
- The workflow used quantum processing offline to transform historical data; classical models then performed the prediction, and the reported metric was an out-of-sample predictive-score improvement rather than a demonstrated reduction in total runtime or cost. [S16]
- The source describing the experiment explicitly notes that the authors did not claim quantum advantage, despite subsequent media and social-media descriptions doing so. [S16]

#### Finding 2

**Claim**

The reported HSBC improvement does not demonstrate a quantum computational speedup, and may depend on hardware noise rather than an advantage from quantum computation.

**Confidence:** Medium

**Why this confidence level**

The abstract’s observation is direct, but the stronger interpretation that the effect is an artifact is an expert critique rather than an established finding. It remains a serious unresolved validity concern.

**Evidence**

- The quoted abstract reports that quantum-hardware-transformed data produced gains over both original-data models and transforms generated by noiseless quantum simulation; it says the results suggest that noise in current hardware contributes to the effect. [S17]
- S17 argues that if the advantage disappears in noiseless classical simulation and appears only with hardware noise, the result may be an artifact of the selected feature transformation and comparison rather than a quantum speedup. [S17]

#### Finding 3

**Claim**

The HSBC result does not meet the stricter commercial-advantage standard because the retrieved material does not establish superiority over the best available classical workflow after full end-to-end accounting.

**Confidence:** High

**Why this confidence level**

The evidentiary gap is explicit and aligns with independent prior benchmarking standards. The claim is about what has not been established, not that the HSBC model cannot have practical value.

**Evidence**

- The experiment compares models using quantum-transformed data with models using original or noiseless-simulation transforms, but the retrieved description does not provide a comparison against all strong classical feature maps, optimized classical algorithms, quantum-processing cost, or total system cost. [S16] [S17]
- Prior peer-reviewed benchmarking evidence requires inclusion of system overheads, strong classical baselines, solution quality, cost, and business benefit; it concludes that such runtime-based advantage has not yet been demonstrated on current NISQ hardware. [S8] [S9]
- The MIT framework defines economic advantage as outperforming a comparably priced classical computer, not merely improving one predictive metric. [S13]

#### Finding 4

**Claim**

The new evidence strengthens the distinction between demonstrated technical advantage and commercially useful advantage.

**Confidence:** High

**Why this confidence level**

The sources support an intermediate classification: a technically interesting, real-data demonstration, but not validated commercial quantum advantage.

**Evidence**

- The HSBC experiment used a real financial dataset and current quantum hardware, so it is more application-oriented than a purely artificial supremacy benchmark. [S16] [S17]
- Nevertheless, prior peer-reviewed and review sources find no independently demonstrated practical advantage in real-world applications under rigorous end-to-end comparisons. [S8] [S9]
- The new critical analysis characterizes the result as potential complementary use of quantum hardware in quantitative finance, rather than proof of quantum computational speedup. [S17]

#### Finding 5

**Claim**

The overall answer remains that commercially useful quantum advantage is not yet established broadly; the most credible projected advantages remain fault-tolerant simulation of molecules, materials, and quantum systems.

**Confidence:** High

**Why this confidence level**

This conclusion is supported by multiple independent or relatively strong prior sources and is consistent with the methodological limitations of the newest case.

**Evidence**

- Prior independent benchmarking evidence finds no practical real-world advantage on current NISQ systems, while theoretical and projected benefits remain strongest for quantum-system simulation. [S8] [S9] [S6]
- Current technical milestones and roadmaps still indicate a substantial gap in logical-qubit count, logical error rate, sustained circuit depth, and full fault tolerance. [S4] [S6] [S7] [S10]
- The HSBC case does not close that gap because its reported benefit is a predictive-score gain in an offline hybrid workflow, not a demonstrated quantum runtime or economic advantage. [S16] [S17]

### Conflicts Found

- HSBC, IBM-related reporting, and secondary commentary present the 34% result as evidence of real-world financial value or a breakthrough, whereas the experiment’s described methodology and the critical analysis do not establish quantum computational speedup. The disagreement is primarily about terminology and evidentiary threshold: predictive improvement in a hybrid model versus advantage over the best complete classical workflow. [S14] [S15] [S16] [S17] [S18] [S8] [S9]
- The reported improvement is attributed in the abstract to quantum-hardware-transformed data, including an apparent contribution from hardware noise; the critique argues this undermines interpreting the result as a quantum-mechanical advantage. The source material does not resolve whether the noisy transformation generalizes or survives stronger classical controls. [S16] [S17]

### Important Gaps

- What exact classical baselines, feature-engineering methods, hyperparameter searches, and data-selection procedures were used in the HSBC–IBM comparison?
- Does the 34% gain persist against optimized classical feature transformations and independent out-of-sample datasets?
- What is the complete cost and resource profile, including quantum circuit execution, error mitigation, calibration, data transfer, and offline preprocessing?
- Can independent groups reproduce the result, and does it translate into measurable trading profit, risk reduction, or lower operational cost rather than predictive-score improvement alone?
- Is the observed effect caused by quantum structure, hardware noise, or an otherwise reproducible stochastic feature transformation?

**Analysis Duration:** 20.40s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources materially clarify the HSBC claim but leave the most important validation gap unresolved: the primary study and independent replications with strong classical controls and full economic accounting are still needed. This could change the classification of the specific finance result, though it is unlikely by itself to overturn the broader conclusion that general commercial advantage has not yet been demonstrated.

**Next Search**

> HSBC IBM arXiv 2509.17715 bond trading quantum feature map independent critique classical baseline replication

---

# Iteration 5

## 1. Search

**Query**

> HSBC IBM arXiv 2509.17715 bond trading quantum feature map independent critique classical baseline replication

**Why this query**

The new sources materially clarify the HSBC claim but leave the most important validation gap unresolved: the primary study and independent replications with strong classical controls and full economic accounting are still needed. This could change the classification of the specific finance result, though it is unlikely by itself to overturn the broader conclusion that general commercial advantage has not yet been demonstrated.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S19 — Quantum leap: HSBC, IBM improve bond RFQ fill rate by 34%  - The DESK - The leading source of information for bond traders**
  URL: https://www.fi-desk.com/quantum-leap-hsbc-ibm-improve-bond-rfq-fill-rate-up-by-34
- **S20 — Bond Trading, Quantum Bond Trading: A Deeper Look at HSBC And IBM's Bond Trading Study**
  URL: https://thequantuminsider.com/2025/09/28/bond-trading-quantum-bond-trading-a-deeper-look-at-hsbc-and-ibms-bond-trading-study
- **S21 — HSBC explores algorithmic trading with IBM quantum computers**
  URL: https://www.ibm.com/quantum/blog/hsbc-algorithmic-bond-trading
- **S22 — Enhanced fill probability estimates in institutional algorithmic bond tradingusing statistical learning algorithms with quantum computers**
  URL: https://arxiv.org/html/2509.17715v1

**Search Duration:** 2.82s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The HSBC–IBM bond-trading result is a real-data, current-hardware application experiment, but its authors explicitly present it as empirical evidence of potential rather than a general or causal demonstration of quantum advantage.

**Confidence:** High

**Why this confidence level**

This is stated directly in the primary retrieved paper, though the work is an arXiv preprint rather than an independently replicated peer-reviewed result.

**Evidence**

- The arXiv paper uses IBM Heron processors to transform production-scale European corporate-bond trading data and reports up to approximately 34% relative improvement in out-of-sample test scores for models using quantum-hardware-transformed data. [S22]
- The authors state that they report statistical observations, do not infer a generalizable theory or causal economic effect, and frame the work as an exploratory tool and complementary application of quantum computing. [S22]

#### Finding 2

**Claim**

The 34% figure is a predictive-score improvement, not evidence of quantum computational speedup or end-to-end commercial economic advantage.

**Confidence:** High

**Why this confidence level**

The distinction follows from the experiment’s stated design and the established end-to-end criteria in the prior evidence.

**Evidence**

- The quantum component is an offline data-transformation stage; conventional machine-learning models use the transformed features for prediction. The paper evaluates fill-prediction performance rather than total workflow runtime, cost, or profit. [S22]
- The paper compares original trading data and noiseless quantum-simulation transforms, but the retrieved material does not establish superiority over the full range of optimized classical feature-engineering and modeling alternatives. [S22]
- Independent benchmarking standards in the accumulated evidence require full system overheads, strong classical baselines, solution quality, cost, and business benefit before calling a result practical advantage. [S6] [S8] [S9] [S13]

#### Finding 3

**Claim**

The paper attributes part of the observed improvement to noise in current quantum hardware, leaving unresolved whether the effect reflects useful quantum computation, a noise-induced transformation, or a classical method that could reproduce the same benefit.

**Confidence:** High

**Why this confidence level**

The authors’ qualification is direct; the competing causal interpretations remain unresolved rather than established.

**Evidence**

- The abstract reports that hardware-transformed data outperformed both original data and noiseless quantum-simulation transforms, and says the results suggest that inherent hardware noise contributes to the effect. [S22]
- The paper expressly says it does not infer a causal explanation for the statistical observations. [S22]

#### Finding 4

**Claim**

The new primary source strengthens, but does not overturn, the conclusion that no commercially useful quantum advantage has yet been rigorously established.

**Confidence:** High

**Why this confidence level**

The primary paper is more relevant than vendor or media summaries, but it is explicitly exploratory and does not satisfy the stronger commercial-advantage standard.

**Evidence**

- Unlike artificial supremacy benchmarks, the study uses a real financial dataset, real quantum hardware, and an industry-relevant prediction problem. [S22]
- However, the authors characterize the result as emerging potential and encourage further applied research, while prior peer-reviewed benchmarking evidence finds no demonstrated practical advantage under comprehensive end-to-end comparisons. [S22] [S8] [S9]

#### Finding 5

**Claim**

The central timeline remains conditional: near-term hybrid experiments may produce application-specific benefits, whereas broad, durable advantages are still most credible for fault-tolerant simulation of molecules, materials, and quantum systems.

**Confidence:** High

**Why this confidence level**

The distinction between narrow exploratory hybrid benefits and scalable fault-tolerant applications is consistent across the retrieved sources.

**Evidence**

- The HSBC paper presents a possible near-term complementary use of noisy quantum processors, but does not claim a general advantage. [S22]
- Accumulated evidence identifies fault-tolerant simulation as the strongest projected area and reports that practical real-world advantage remains un demonstrated on current NISQ systems. [S6] [S8] [S9]
- Current logical-qubit, error-rate, and circuit-depth milestones remain below the projected requirements for production-scale applications. [S4] [S6] [S7] [S10]

### Conflicts Found

- IBM and media coverage describe the HSBC result as evidence that current quantum computers could provide substantial competitive advantage, while the paper itself limits the conclusion to statistical observations and potential complementary use. The disagreement is mainly between promotional interpretation and the authors’ stated evidentiary scope. [S19] [S20] [S21] [S22]
- The paper reports that noisy hardware-transformed features outperform noiseless simulations, whereas the accumulated critique treats this as a validity concern rather than proof of quantum advantage. The sources do not resolve whether the effect is uniquely quantum or reproducible through classical stochastic transformations. [S17] [S22]
- The 34% improvement is reported in several sources, but the commercial interpretation conflicts with rigorous benchmarking standards because the retrieved material does not show total runtime, total cost, trading-profit impact, or comparison against the best optimized classical workflow. [S19] [S20] [S21] [S22] [S8] [S9] [S13]

### Important Gaps

- Does the HSBC–IBM result persist against optimized classical feature maps, stochastic transformations, hyperparameter searches, and independent datasets?
- What is the complete end-to-end resource and cost profile, including quantum execution, calibration, queueing, data transfer, preprocessing, and postprocessing?
- Does the predictive-score improvement translate into statistically robust trading profit, risk reduction, or lower operational cost?
- Can independent groups reproduce the result, and is the effect attributable to quantum structure rather than hardware noise?
- Are there any current application demonstrations that simultaneously meet production-scale sizing, real hardware execution, independent verification, and economic superiority over the best classical workflow?

**Analysis Duration:** 15.02s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new source materially improves the evidence on the HSBC case by supplying the primary preprint and clarifying its limits, but the most important unresolved issue remains independent validation against strong classical alternatives and full economic accounting. That gap matters directly to the original question.

**Next Search**

> independent replication critique HSBC IBM quantum bond trading 34% classical stochastic feature map benchmark

---

# Iteration 6

## 1. Search

**Query**

> independent replication critique HSBC IBM quantum bond trading 34% classical stochastic feature map benchmark

**Why this query**

The new source materially improves the evidence on the HSBC case by supplying the primary preprint and clarifying its limits, but the most important unresolved issue remains independent validation against strong classical alternatives and full economic accounting. That gap matters directly to the original question.

**Results**

5 results retrieved.

1 new unique source added.

### Sources

- **S23 — HSBC and IBM test quantum trading algorithm, see 34% better results | Vincent P. posted on the topic | LinkedIn**
  URL: https://www.linkedin.com/posts/vincent-p-91b2672_hsbc-demonstrates-worlds-first-known-quantum-enabled-activity-7376912823265697792-ee9z

**Search Duration:** 2.17s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new source adds no independent evidence that the HSBC–IBM experiment constitutes commercial quantum advantage.

**Confidence:** High

**Why this confidence level**

The source’s provenance and content are explicit: it is commentary summarizing already retrieved claims rather than a primary or independent validation.

**Evidence**

- The post is an individual LinkedIn commentary that repeats the reported 34% prediction improvement and links to the HSBC announcement and arXiv paper; it provides no new benchmark, replication, cost analysis, or independent technical evaluation. [S23]

#### Finding 2

**Claim**

The LinkedIn post reinforces that the HSBC result was a hybrid quantum-classical experiment involving a quantum feature transformation on IBM’s Heron processor and classical prediction models.

**Confidence:** Medium

**Why this confidence level**

This is a clear description in the post, but it is secondary commentary and adds no methodological detail beyond the already retrieved primary paper.

**Evidence**

- The post describes classical models combined with a quantum feature transform, trained on more than a million trading requests, and reports up to 34% better prediction accuracy. [S23]

#### Finding 3

**Claim**

The post itself acknowledges that the HSBC result is not production-ready and highlights the unresolved role of hardware noise.

**Confidence:** Medium

**Why this confidence level**

These are the commentator’s observations, not an independent technical conclusion; they nevertheless align with the primary paper’s stated limitations and the existing critique.

**Evidence**

- The author says there is still a substantial gap before deployment in production and calls attention to the possibility that noise contributed to the improvement. [S23]

### Conflicts Found

- The post’s headline and some quoted reactions frame the 34% result as a quantum trading breakthrough or competitive benefit, while the post author also says there is a large gap before production. This is consistent with the accumulated distinction between an application-oriented experiment and validated commercial advantage, rather than evidence resolving that distinction. [S23] [S22] [S16] [S17] [S8] [S9]

### Important Gaps

- The new source does not resolve whether the 34% predictive improvement survives optimized classical feature maps, stochastic classical controls, independent datasets, or full end-to-end cost and latency accounting.
- It does not establish whether the effect translates into trading profit, risk reduction, or operational savings.
- It does not provide independent replication or determine whether hardware noise, rather than uniquely quantum computation, causes the observed effect.

**Analysis Duration:** 7.69s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The accumulated evidence already answers the central question responsibly: no broadly accepted, independently verified commercially useful quantum advantage has been demonstrated. S23 is derivative commentary and does not materially change the evidentiary picture or close the key HSBC-related gaps. Further searching would be useful only for narrower verification questions, not necessary for the overall conclusion.

**Next Search**

> How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers. additional evidence search 7

---

# Iteration 7

## 1. Search

**Query**

> How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers. additional evidence search 7

**Why this query**

The accumulated evidence already answers the central question responsibly: no broadly accepted, independently verified commercially useful quantum advantage has been demonstrated. S23 is derivative commentary and does not materially change the evidentiary picture or close the key HSBC-related gaps. Further searching would be useful only for narrower verification questions, not necessary for the overall conclusion.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S24 — The Potential of Commercial Quantum Computers**
  URL: https://www.quera.com/blog-posts/potential-of-commercial-quantum-computers
- **S25 — Quantum Computing – Strategic Recommendations for the Industry**
  URL: https://arxiv.org/html/2601.08578v1
- **S26 — Quantum Computing: How Close to Commercial Value? | IDTechEx Research Article**
  URL: https://www.idtechex.com/en/research-article/quantum-computing-how-close-to-commercial-value/33552

**Search Duration:** 3.42s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources do not materially change the accumulated conclusion: commercially useful quantum advantage has not yet been rigorously established broadly, although quantum computers are available commercially through cloud and as-a-service offerings.

**Confidence:** High

**Why this confidence level**

The strongest evidence remains the peer-reviewed runtime analysis and benchmarking review; the new commercial source is opinion/promotional material and the IDTechEx excerpt is substantively incomplete.

**Evidence**

- The accumulated peer-reviewed and benchmarking evidence finds no practical real-world advantage under comprehensive end-to-end comparisons on current hardware. [S8] [S9]
- QuEra describes commercialization primarily as access through quantum-as-a-service models and says useful commercial systems still face major stability and scalability challenges. [S24]
- IDTechEx’s retrieved content contains no substantive technical or benchmark evidence that would overturn this conclusion. [S26]

#### Finding 2

**Claim**

The most valuable contribution of S25 is methodological: industrial claims should be assessed using consistent criteria including scalability, solution quality, runtime, transferability, and comparison with classical solvers.

**Confidence:** Medium

**Why this confidence level**

The source is an arXiv whitepaper and the retrieved excerpt describes the framework and project scope but does not provide the detailed use-case results or independent validation.

**Evidence**

- The QCHALLenge whitepaper says its industrial use cases are evaluated using model formulation, scalability, solution quality, runtime, and transferability, with quantum implementations benchmarked against classical solvers. [S25]
- It describes real-world logistics and production use cases tested on IBM, IonQ, and D-Wave hardware, while emphasizing that hardware limitations such as low qubit counts, limited connectivity, and error susceptibility must be included in evaluation. [S25]

#### Finding 3

**Claim**

Optimization and machine-learning applications remain unresolved rather than demonstrated sources of general quantum advantage; hybrid approaches may be the most plausible near-term route, but their value is problem-specific.

**Confidence:** High

**Why this confidence level**

The new framework is consistent with the prior evidence and does not claim that the evaluated industrial applications have already achieved a verified advantage.

**Evidence**

- S25 frames optimization and machine learning as use cases requiring traffic-light evaluation and explicitly allows outcomes in which classical methods remain superior; it emphasizes hybrid classical-quantum strategies as a possible practical modality. [S25]
- Prior evidence reports no demonstrated practical advantage for several optimization, machine-learning, finance, and similar workloads under stricter benchmarking standards. [S5] [S8] [S9]

#### Finding 4

**Claim**

The principal technical barriers remain decoherence, gate and interaction errors, error-correction overhead, limited coherence, and scalable hardware/control integration.

**Confidence:** High

**Why this confidence level**

The barriers are described directly by the new source and independently recur across prior roadmap, benchmarking, and technical-milestone evidence, though S24 is promotional.

**Evidence**

- QuEra identifies environmental noise, cascading errors, the need for large numbers of physical qubits for error correction, limited coherence, two-qubit interaction errors, and difficult classical control and error mitigation as barriers to useful commercial machines. [S24]
- Prior sources identify the same central gap: insufficient logical-qubit scale, logical reliability, and sustained circuit depth for production workloads. [S4] [S6] [S7] [S10]

#### Finding 5

**Claim**

S24 presents several possible commercial application areas—quantum-system simulation, optimization, finance, machine learning, cryptography, random-number generation, and energy efficiency—but these are potential benefits, not demonstrated advantages in the supplied evidence.

**Confidence:** High

**Why this confidence level**

The distinction between proposed application areas and demonstrated advantage is clear; the stronger conclusion is supported by multiple prior sources.

**Evidence**

- QuEra lists exponential speedups, optimization, machine learning, finance, simulation, cryptographic uses, and lower energy consumption as possible benefits, while also stating that the technology remains in its infancy and faces stability and scalability challenges. [S24]
- Prior evidence finds the strongest projected case in fault-tolerant chemistry, materials, and quantum-system simulation, while practical advantages in optimization, finance, and machine learning remain unverified under rigorous standards. [S3] [S5] [S6] [S8] [S9]

### Conflicts Found

- S24 uses broad language suggesting potential advantages in optimization, machine learning, finance, cryptography, and energy consumption, whereas S5, S8, and S9 apply stricter standards and report no demonstrated practical advantage for several such workloads. This is primarily a difference between promotional/potential claims and empirical evidentiary standards. [S24] [S5] [S8] [S9]
- S25’s project is designed to evaluate industrial optimization and machine-learning use cases and may classify some as promising, while prior sources conclude that practical advantage has not yet been demonstrated. Without the detailed results section, it is unclear whether any apparent positive result meets the full end-to-end commercial standard. [S25] [S8] [S9]
- S24 discusses commercial availability through cloud access as evidence of ongoing commercialization, while the research question concerns commercially useful advantage over classical computers. Availability and market access are not equivalent to verified computational or economic advantage. [S24] [S13]

### Important Gaps

- The retrieved excerpt of S25 does not show the actual verdict for each QCHALLenge optimization and machine-learning use case, including whether any passed its classical benchmark and transferability criteria.
- S25 does not establish independent replication, full cost accounting, or production-scale quantum advantage for the industrial cases it describes.
- S24 does not quantify the claimed potential benefits or identify any independently verified end-to-end commercial advantage.
- The exact timeline to fault-tolerant systems capable of useful chemistry or materials simulation remains uncertain; vendor roadmaps and projections are conditional.
- The practical cryptographic timeline and infrastructure requirements remain insufficiently covered.
- The unresolved HSBC–IBM questions remain: optimized classical controls, independent replication, end-to-end cost and latency, and translation from predictive scores to trading economics.

**Analysis Duration:** 18.59s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new material reinforces existing conclusions and adds a useful evaluation framework, but does not supply the missing independent, end-to-end benchmark or detailed industrial results needed to change the answer. Further research could fill specific gaps, especially the full QCHALLenge results, but it is not necessary to answer the original question responsibly at the current stage.

**Next Search**

> How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers. additional evidence search 8

---

# Iteration 8

## 1. Search

**Query**

> How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers. additional evidence search 8

**Why this query**

The new material reinforces existing conclusions and adds a useful evaluation framework, but does not supply the missing independent, end-to-end benchmark or detailed industrial results needed to change the answer. Further research could fill specific gaps, especially the full QCHALLenge results, but it is not necessary to answer the original question responsibly at the current stage.

**Results**

5 results retrieved.

2 new unique sources added.

### Sources

- **S27 — What Quantum Computers Can Do Better Than Classical Computers**
  URL: https://postquantum.com/quantum-computing/quantum-classical
- **S28 — 8 Industry Use Cases for Quantum Computing**
  URL: https://thequantuminsider.com/2026/05/04/quantum-computing-use-cases-real-applications-industries

**Search Duration:** 2.63s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources reinforce that quantum advantage is problem-specific, not a general replacement for classical computing.

**Confidence:** Medium

**Why this confidence level**

The claim is consistent with the accumulated evidence, but both new sources are explanatory industry articles rather than primary or peer-reviewed benchmark studies.

**Evidence**

- S27 explains that superposition, entanglement, and interference provide useful speedups only for certain structured problems, and that only a limited number of algorithms achieve such advantages. [S27]
- S28 states that most ordinary computing workloads are unlikely to benefit from quantum hardware and that classical systems are expected to remain dominant for most applications. [S28]

#### Finding 2

**Claim**

Theoretical advantages are clearest for factoring and, more modestly, unstructured search, but these do not constitute current commercial advantages.

**Confidence:** High

**Why this confidence level**

The distinction between algorithmic theory and present capability is directly supported and agrees with the stronger prior benchmarking evidence. The specific qubit estimate is only reported by one secondary source.

**Evidence**

- S27 describes Shor’s algorithm as providing a theoretical polynomial-time advantage for factoring and Grover’s algorithm as providing a quadratic speedup for unstructured search. [S27]
- S27 says that a 2048-bit RSA attack would require an estimated roughly 20 million qubits, far beyond current hardware, so the cryptographic advantage remains prospective. [S27]
- The accumulated evidence distinguishes theoretical algorithmic speedups from practical real-world advantage and finds no current broad commercial demonstration. [S8] [S9] [S13]

#### Finding 3

**Claim**

Molecular and materials simulation remains the most credible projected commercial application, but current demonstrations are too small to displace classical methods.

**Confidence:** High

**Why this confidence level**

The application ranking is consistent across multiple sources. The 5–10 year estimate is a projection, not an independently validated forecast.

**Evidence**

- S28 identifies molecular simulation in drug discovery, chemistry, and materials science as the most viable near-term application area, while stating that demonstrations have not yet reached systems complex enough to replace classical methods. [S28]
- S28 gives a commonly cited 5–10 year projection for useful molecular simulation, conditional on obtaining hundreds of error-corrected logical qubits. [S28]
- Prior evidence likewise identifies fault-tolerant quantum-system simulation as the strongest projected use case and does not establish delivered advantage. [S3] [S5] [S6] [S8] [S9]

#### Finding 4

**Claim**

Optimization, finance, AI, and climate-modeling applications remain plausible research areas but lack established general quantum advantage over strong classical methods.

**Confidence:** High

**Why this confidence level**

The new source independently aligns with the prior methodological and application-specific evidence.

**Evidence**

- S28 says optimization, AI, and climate modeling face longer timelines and uncertain advantage, noting that many optimization problems have highly tuned classical algorithms that quantum methods have not beaten. [S28]
- The accumulated evidence reaches the same conclusion for optimization, machine learning, and finance, including the HSBC–IBM experiment, which did not demonstrate end-to-end quantum speedup or economic advantage. [S5] [S8] [S9] [S16] [S22]

#### Finding 5

**Claim**

The biggest remaining technical barrier is scalable fault-tolerant computation: low logical error rates, sufficiently many logical qubits, and enough sustained circuit depth for useful workloads.

**Confidence:** High

**Why this confidence level**

This is a consistent conclusion across roadmap, technical-milestone, and benchmarking evidence, even though exact application thresholds remain uncertain.

**Evidence**

- S28 states that current hardware has error rates and qubit counts insufficient for practically useful molecular simulation. [S28]
- Prior roadmap and milestone evidence identifies the same gap between current logical-qubit/error-rate achievements and production-scale applications. [S4] [S6] [S7] [S10] [S24]

#### Finding 6

**Claim**

The new sources do not provide evidence that commercially useful quantum advantage has already been demonstrated.

**Confidence:** High

**Why this confidence level**

The new material supports, rather than overturns, the existing conclusion.

**Evidence**

- S27 mainly presents theoretical algorithms and general explanations rather than an independently replicated commercial benchmark. [S27]
- S28 explicitly says current molecular-simulation demonstrations have not displaced classical methods and describes other applications as uncertain or longer-term. [S28]
- Peer-reviewed benchmarking evidence in the accumulated state finds no practical advantage under comprehensive end-to-end comparisons on current hardware. [S8] [S9]

### Conflicts Found

- S27 uses strong language about quantum computers eventually outperforming classical computers for factoring and search, while S28 emphasizes current limitations and uncertain application timelines. This is a difference between theoretical algorithmic advantage and present commercial capability, not a direct contradiction. [S27] [S28]
- S28 gives a 5–10 year projection for useful molecular simulation, whereas prior sources include different conditional timelines and hardware-scale projections. These estimates are not directly comparable and remain speculative. [S4] [S5] [S28]

### Important Gaps

- Whether any current application demonstration meets the full standard of production-relevant scale, real hardware execution, independent replication, strong classical baselines, and end-to-end economic advantage remains unresolved.
- The exact logical-qubit count, logical error rate, circuit depth, and total cost required for commercially valuable chemistry and materials workloads remain application-dependent and unsettled.
- The practical timeline for cryptographically relevant fault-tolerant computation remains insufficiently established; S27 supplies only a secondary estimate of required qubits.
- The 5–10 year molecular-simulation projection is not independently validated and should not be treated as a reliable forecast.
- The new sources do not resolve whether hybrid finance and optimization results can survive optimized classical and stochastic controls, independent datasets, and full cost accounting.

**Analysis Duration:** 15.48s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources add useful context on theoretical algorithms and reinforce molecular simulation as the leading projected application, but they do not materially improve the central evidentiary gaps. The strongest accumulated evidence already supports a responsible answer: technical quantum advantage has been demonstrated on selected artificial or simulation-hard tasks, but commercially useful end-to-end advantage has not yet been rigorously established. Further searching would be useful only for narrower questions such as cryptographic resource estimates or independent validation of particular vendor claims.

**Next Search**

> How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers. additional evidence search 9

---

# Iteration 9

## 1. Search

**Query**

> How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers. additional evidence search 9

**Why this query**

The new sources add useful context on theoretical algorithms and reinforce molecular simulation as the leading projected application, but they do not materially improve the central evidentiary gaps. The strongest accumulated evidence already supports a responsible answer: technical quantum advantage has been demonstrated on selected artificial or simulation-hard tasks, but commercially useful end-to-end advantage has not yet been rigorously established. Further searching would be useful only for narrower questions such as cryptographic resource estimates or independent validation of particular vendor claims.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S29 — Quantum firms race to market as the industry sees ‘inflection point’**
  URL: https://www.cnbc.com/2026/03/30/quantum-computing-firms-go-public-breakthroughs-commercialization.html
- **S30 — When will quantum computers beat classical computers? | The Coherence Times | IBM**
  URL: https://www.ibm.com/think/podcasts/the-coherence-times/when-will-quantum-beat-classical-computers
- **S31 — Quantum computer completes verified task beyond ...**
  URL: https://phys.org/news/2026-07-quantum-task-classical-simulations.html

**Search Duration:** 2.31s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new IBM–University of Chicago result is evidence of a stronger form of demonstrated technical quantum advantage, but not of commercially useful advantage.

**Confidence:** Medium

**Why this confidence level**

S31 reports concrete logical-circuit and verification metrics and links to a primary preprint, but the retrieved evidence is a secondary report of an arXiv paper and does not establish commercial relevance, independent replication, or complete system-level accounting.

**Evidence**

- The reported experiment executed a verified, classically intractable sampling task in approximately 15 minutes, using 70 logical qubits, 2,415 logical two-qubit operations, and 468 logical T gates; leading classical simulation approaches reportedly faced prohibitive runtimes. [S31]
- The task was a structured random-circuit-style computation designed to preserve classical hardness while enabling error detection, rather than a production scientific, industrial, or commercial workload. [S31]
- The accumulated benchmarking evidence defines practical advantage more stringently, requiring real-world value, strong classical baselines, total runtime and cost, and end-to-end validation. [S6] [S8] [S9] [S13]

#### Finding 2

**Claim**

Verification of classically hard quantum computations remains a major technical achievement and an important prerequisite for future useful quantum computing.

**Confidence:** High

**Why this confidence level**

The new report directly describes the verification method and measured logical operations, and its significance is consistent with multiple prior sources identifying verification and fault tolerance as prerequisites.

**Evidence**

- The experiment was designed to detect errors during a computation that is otherwise difficult to verify, and its authors identify verification as one of the biggest challenges in establishing experimental quantum advantage. [S31]
- The result reportedly demonstrated 70 logical qubits with substantial logical-gate depth while providing a lower bound on execution fidelity. [S31]
- Prior evidence also identifies trustworthy execution, error correction, benchmarking, and independent verification as central barriers. [S6] [S7] [S9]

#### Finding 3

**Claim**

The new result does not overturn the conclusion that current quantum computers lack broadly demonstrated economic advantage over classical computers.

**Confidence:** High

**Why this confidence level**

The classification follows directly from the workload and the independent practical-advantage criteria. S30 is especially notable because it is an IBM source that does not characterize the reported technical milestone as commercial advantage.

**Evidence**

- S31 concerns a computationally hard sampling benchmark, not a task with demonstrated business value, production deployment, cost savings, or superiority to a classical workflow that users would purchase. [S31]
- IBM’s own retrieved explainer says quantum computers have not yet reached the point of solving valuable problems faster, more accurately, or more cost-effectively than classical computers. [S30]
- Peer-reviewed benchmarking evidence similarly concludes that practical real-world advantage has not been demonstrated on current NISQ hardware under end-to-end accounting. [S8] [S9]

#### Finding 4

**Claim**

Projected timelines for practical advantage remain speculative and should be treated as industry expectations rather than established forecasts.

**Confidence:** Medium

**Why this confidence level**

The timeline is explicitly attributed to an analyst and is consistent with the existence of active commercialization efforts, but it is not technical evidence that useful advantage will arrive on that schedule.

**Evidence**

- CNBC reports an analyst expectation of practical quantum advantage around 2028–2029 and wider commercial use in the 2030s, alongside investor movement toward early-revenue opportunities. [S29]
- Prior sources give different conditional timelines and hardware requirements, including projections around 2030, 2033, or five to ten years for molecular simulation. [S4] [S5] [S28]
- The retrieved material provides no independent forecasting methodology that reconciles these timelines with application-specific logical-qubit, error-rate, depth, runtime, and cost requirements. [S29] [S4] [S5] [S28]

#### Finding 5

**Claim**

The largest remaining technical gap is still scalable fault tolerance, despite the 70-logical-qubit demonstration.

**Confidence:** High

**Why this confidence level**

The new result improves the demonstrated logical-computation baseline but leaves the application-scale requirements unresolved across the accumulated evidence.

**Evidence**

- S31 demonstrates a large logical computation and error-detection scheme, but does not show a production workload, broad fault-tolerant operation, or the sustained scale needed for chemistry, materials, cryptography, or other commercial applications. [S31]
- Prior sources identify the unresolved requirements as low logical error rates, many logical qubits, deep sustained circuits, and scalable hardware/control integration. [S4] [S6] [S7] [S10] [S24] [S28]
- Google’s and IBM’s reported error-control milestones have likewise been classified as technical steps toward fault tolerance rather than commercial advantage. [S7] [S10]

### Conflicts Found

- S31 says the IBM/UChicago experiment establishes quantum advantage for a verified classically hard computation, while S30 says quantum computers have not yet reached advantage on valuable problems. This is a definitional and workload distinction: demonstrated technical advantage on a hard benchmark versus commercially useful advantage on a valuable end-to-end task. [S30] [S31]
- S29 presents practical advantage around 2028–2029 as an analyst expectation, whereas the accumulated sources provide materially different conditional timelines and emphasize that exact application requirements remain unsettled. These are projections, not directly comparable demonstrations. [S29] [S4] [S5] [S28]
- S31 reports a 15-minute quantum execution and prohibitive classical simulation runtimes, but the retrieved excerpt does not show full quantum system overheads, the strongest possible classical algorithms, or an economic comparison. This creates a potential benchmarking gap rather than a demonstrated contradiction. [S31] [S6] [S8] [S9] [S13]

### Important Gaps

- Has the primary arXiv paper behind S31 been independently reviewed or replicated, and what exact classical baselines and hardware configurations were used?
- Does the 70-logical-qubit result sustain sufficiently low logical error rates and circuit depth for application workloads, rather than only this specially structured verification benchmark?
- Were calibration, compilation, queueing, readout, error-detection overhead, classical verification, and total energy/capital costs included in the reported 15-minute comparison?
- Can the verification and encoded-circuit techniques be transferred to chemistry, materials, cryptographic, or other commercially valuable computations?
- Which specific application, if any, can meet the full commercial standard: production-relevant scale, real hardware, independent replication, best-classical comparison, and lower total cost or higher value?
- The projected 2028–2029 timeline in S29 lacks an application-by-application technical basis and remains uncertain.

**Analysis Duration:** 19.06s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The accumulated answer is already robust on the original question, but S31 is a significant new technical-advantage claim. Verifying its primary paper and benchmarking details would materially improve the separation between demonstrated technical advantage and commercial advantage, especially because the report gives unusually concrete logical-qubit, gate-count, verification, and runtime claims.

**Next Search**

> arXiv 2607.25941 IBM UChicago 70 logical qubits verified high fidelity classical runtime benchmark independent analysis

---

# Iteration 10

## 1. Search

**Query**

> arXiv 2607.25941 IBM UChicago 70 logical qubits verified high fidelity classical runtime benchmark independent analysis

**Why this query**

The accumulated answer is already robust on the original question, but S31 is a significant new technical-advantage claim. Verifying its primary paper and benchmarking details would materially improve the separation between demonstrated technical advantage and commercial advantage, especially because the report gives unusually concrete logical-qubit, gate-count, verification, and runtime claims.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S32 — [2607.25941] Sampling hard circuits with verifiably high fidelity**
  URL: https://arxiv.org/abs/2607.25941
- **S33 — IBM quantum computer solves classically intractable problem in 15 minutes | ScienceDaily**
  URL: http://www.sciencedaily.com/releases/2026/08/260829035219.htm
- **S34 — IBM and University of Chicago report a verifiable 70-logical-qubit sampling run | MLQ News**
  URL: https://mlq.ai/news/ibm-and-university-of-chicago-report-a-verifiable-70-logical-qubit-sampling-run
- **S35 — IBM and University of Chicago Demonstrate Verified Logical Quantum Computation Beyond Classical Simulation**
  URL: https://thequantuminsider.com/2026/07/31/ibm-university-of-chicago-verified-logical-quantum-computation

**Search Duration:** 2.64s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new IBM–University of Chicago result is a stronger demonstration of technical quantum advantage than ordinary supremacy benchmarks, but it is not commercially useful quantum advantage.

**Confidence:** High

**Why this confidence level**

The new sources provide concrete technical details and independently reinforce the existing distinction between beyond-classical computation and commercially valuable performance.

**Evidence**

- The experiment reportedly executed a synthetic sampling task using 70 logical qubits, 2,415 logical two-qubit operations, and 468 T gates in about 15–16 minutes, while leading classical simulation approaches were estimated to be impractical. [S33] [S34] [S35]
- The workload was designed as a classically hard sampling benchmark, not as chemistry, materials science, finance, optimization, or another end-user application. [S34]
- The established practical-advantage standard requires real-world value, strong classical baselines, full runtime and cost accounting, and end-to-end validation. [S6] [S8] [S9] [S13]

#### Finding 2

**Claim**

The experiment materially advances verification and error-detected logical computation, which are prerequisites for future useful quantum computing.

**Confidence:** High

**Why this confidence level**

The technical contribution is described consistently across the retrieved report, with specific circuit, error-detection, and fidelity metrics.

**Evidence**

- The structured circuit preserved classical hardness while allowing syndrome checks and quantitative estimation of output fidelity; the reported fidelity lower bound was device-dependent but statistically supported. [S33] [S34] [S35]
- The detailed account reports detection of 92% of first-order errors, a 29-fold fidelity improvement over the unencoded circuit, and effective logical error rates below physical error rates. [S34]
- The work used 70 logical qubits and thousands of logical operations, making it a substantial logical-computation milestone even though it was not a production workload. [S33] [S34] [S35]

#### Finding 3

**Claim**

The new result has important limitations that prevent interpreting it as a scalable commercial capability.

**Confidence:** High

**Why this confidence level**

These are explicit methodological limitations in the detailed coverage and directly affect scalability and benchmarking.

**Evidence**

- Most experimental shots were rejected through post-selection; the reported acceptance rate was 5.90 × 10^-4, and only 2,051 samples were accepted in 16.1 minutes. [S34]
- The fidelity certificate was device-dependent and inferred from encoded-circuit structure and noise analysis rather than being a fully device-independent verification of the complete computation. [S34]
- The researchers acknowledged that post-selection overhead cannot grow indefinitely and that improved classical algorithms or hardware could alter the classical-runtime comparison. [S34]

#### Finding 4

**Claim**

The overall evidence still supports the conclusion that no broadly reproducible, commercially useful quantum advantage has yet been established.

**Confidence:** High

**Why this confidence level**

The new sources strengthen the technical-achievement category but do not address the missing commercial criteria identified by stronger benchmarking evidence.

**Evidence**

- The new benchmark has no demonstrated business value, production deployment, lower total cost, or superiority over a complete classical workflow that users would purchase. [S34] [S35]
- IBM’s reported milestone is described as a step toward useful applications rather than evidence that valuable problems are already solved faster, more accurately, or more cheaply than classically. [S33] [S34] [S30]
- Prior peer-reviewed and benchmarking sources conclude that practical real-world advantage has not been demonstrated under comprehensive end-to-end comparisons on current hardware. [S8] [S9]

#### Finding 5

**Claim**

The largest remaining technical barrier remains scalable fault tolerance: low logical error rates, many logical qubits, deep sustained circuits, and manageable error-correction overhead.

**Confidence:** High

**Why this confidence level**

The new result improves the demonstrated baseline but leaves the same application-scale engineering requirements unresolved.

**Evidence**

- Although the experiment demonstrated 70 logical qubits and lower effective error rates, its heavy post-selection and verification overhead are not shown to scale to application workloads. [S34]
- Prior evidence identifies insufficient logical scale, reliability, circuit depth, and hardware/control integration as the central gap before production-scale chemistry, materials, cryptographic, or other applications. [S4] [S6] [S7] [S10] [S24] [S28]

### Conflicts Found

- IBM and related coverage describe the new experiment as meeting criteria for quantum advantage or entering a quantum-advantage era, while the stricter benchmarking sources reserve practical advantage for useful end-to-end tasks with economic value. This is a definitional and workload distinction rather than a direct contradiction. [S33] [S35] [S6] [S8] [S9] [S13]
- S33 and S35 emphasize an approximately 15-minute quantum runtime against impractical classical simulation, whereas S34 cautions that the comparison includes severe post-selection overhead and unspecified assumptions about classical methods. The result is technically significant, but the full performance comparison remains conditional. [S33] [S34] [S35]
- The new experiment provides a device-dependent fidelity bound rather than device-independent verification, so claims that it definitively proves a correct computation are stronger than the methodological description supports. [S33] [S34]

### Important Gaps

- Can the 70-logical-qubit technique operate without prohibitive post-selection overhead on deeper or application-relevant circuits?
- What is the full end-to-end runtime and cost after including rejected shots, calibration, compilation, queueing, readout, verification, and classical processing?
- Would the benchmark remain beyond the reach of the best newly optimized classical algorithms and hardware?
- Can the verification and error-detection methods transfer to chemistry, materials, cryptographic, optimization, or other commercially valuable workloads?
- Which current application, if any, has independently replicated superiority over the best classical workflow at production-relevant scale?

**Analysis Duration:** 16.73s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The runner reached the maximum research iteration budget. Analyzer assessment: The new sources add useful technical detail about logical qubits, fidelity estimation, and post-selection, but they do not change the central answer. The important commercial question is already answerable responsibly: technical quantum advantage has advanced, while rigorous commercial advantage remains unproven. Further searches could investigate replication, but are not necessary to support the present conclusion.

**Stop Reason:** max_iterations

---

# Final Research Decision

**Research Stopped Because**

The runner reached the maximum research iteration budget.

**Stop Reason:** max_iterations

**Searches Performed:** 10

**Unique Sources:** 35

**Remaining Uncertainty**

- No supplied source independently establishes a production-scale application that beats the best complete classical workflow on total runtime, cost, quality, or economic value.
- The Q-CTRL 3,000-fold materials-simulation claim lacks the retrieved independent replication, benchmark details, and complete overhead accounting needed for classification.
- The HSBC–IBM result requires optimized classical controls, independent replication, full resource and cost accounting, and evidence that predictive improvement translates into trading economics.
- It remains unclear whether the 70-logical-qubit verification and error-detection techniques can operate without prohibitive overhead on chemistry, materials, cryptographic, or other application workloads.
- Application-specific requirements for logical-qubit count, logical error rate, circuit depth, runtime, data loading, and total cost remain unsettled.
- The practical timeline and infrastructure requirements for cryptographically relevant fault-tolerant computation are insufficiently covered.
- Research stopped at the stated iteration limit; these unresolved questions should not be treated as answered.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 10 | 28.24s |
| OpenAI Analysis | 10 | 169.13s |
| Report Generation | 1 | 29.61s |
| Total Run | — | 226.98s |
