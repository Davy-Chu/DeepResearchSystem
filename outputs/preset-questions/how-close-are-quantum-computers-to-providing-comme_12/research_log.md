# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

**Status:** Completed

**Stop Reason:** sufficient_evidence

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 10 / 10

**Unique Sources:** 33

**OpenAI Calls:** 11

**Tavily Calls:** 10

**Started:** 2026-09-01T05:04:20-04:00

**Ended:** 2026-09-01T05:08:20-04:00

**Total Runtime:** 239.84s

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

- **S1 — Advantages and Disadvantages of Quantum Computing | Keyfactor**
  URL: https://www.keyfactor.com/blog/advantages-and-disadvantages-of-quantum-computing
- **S2 — Building business readiness for quantum computing: Key barriers and support mechanisms: Building business readiness for quantum computing**
  URL: https://www.oecd.org/en/publications/building-business-readiness-for-quantum-computing_ee847e5f-en/full-report/component-4.html
- **S3 — Quantum Computing vs Classical Computing: Key Differences**
  URL: https://www.bluequbit.io/blog/quantum-computing-vs-classical-computing
- **S4 — Quantum Computers Will Make AI Better - Quantinuum**
  URL: https://www.quantinuum.com/blog/quantum-computers-will-make-ai-better
- **S5 — Practical quantum advantage signals a new commercial era for quantum computing | Q-CTRL**
  URL: https://q-ctrl.com/blog/practical-quantum-advantage-signals-a-new-commercial-era-for-quantum-computing

**Search Duration:** 3.84s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The retrieved material distinguishes at least three notions of quantum advantage: a contrived benchmark demonstrating computational capability, “absolute” advantage against the best conceivable classical method, and “practical” advantage against the best available alternative on a commercially relevant task.

**Confidence:** Medium

**Why this confidence level**

The distinction is clearly stated, but the source is a vendor blog and does not independently validate the underlying demonstrations.

**Evidence**

- Q-CTRL explicitly contrasts Google’s 2019 supremacy-style demonstration, absolute advantage, and its definition of practical advantage as outperforming the available conventional alternative on a real-world problem. [S5]

#### Finding 2

**Claim**

A quantum computation can demonstrate a computational advantage without providing commercial value; the retrieved source characterizes Google’s 2019 milestone as scientifically important but commercially irrelevant because the task was designed to demonstrate quantum capability rather than solve a useful customer problem.

**Confidence:** Medium

**Why this confidence level**

This is a useful conceptual distinction, but it is presented by an interested commercial party and lacks the original publication or independent assessment here.

**Evidence**

- Q-CTRL says the 2019 demonstration solved a problem with no commercial or practical relevance, despite being infeasible for conventional supercomputers. [S5]

#### Finding 3

**Claim**

Theoretical or projected advantages are strongest for selected problem classes, especially simulation and some optimization or cryptographic applications, rather than for general-purpose computing.

**Confidence:** Medium

**Why this confidence level**

The sources support the narrowness of the claimed opportunity, but their descriptions of speedups and suitability are broad and not sufficient to establish practical superiority.

**Evidence**

- BlueQubit describes quantum systems as tools for specific problems and lists optimization, cryptography, and molecular-interaction simulation as potential application areas; Q-CTRL focuses on fermionic/materials simulation and describes it as a candidate for long-term advantage. [S3] [S5]

#### Finding 4

**Claim**

The main technical barriers identified in the retrieved material are noise and errors, insufficient scale, error correction, qubit sensitivity/decoherence, and demanding operating infrastructure.

**Confidence:** High

**Why this confidence level**

The barriers are directly and consistently described across two sources, although the material does not quantify thresholds or timelines.

**Evidence**

- Q-CTRL states that hardware size and errors limit useful algorithms and that noise has prevented useful results on relevant problems; BlueQubit describes decoherence from temperature, electromagnetic interference, and vibrations, along with specialized operating conditions and differing scalability/error-correction tradeoffs across hardware platforms. [S3] [S5]

#### Finding 5

**Claim**

The retrieved sources include a vendor claim of a present-day, commercially relevant quantum speedup, but this claim should not yet be treated as independently demonstrated commercial quantum advantage.

**Confidence:** Low

**Why this confidence level**

The claim is specific but comes from a directly interested vendor, and the retrieved excerpt does not permit evaluation of whether the comparison is apples-to-apples, whether all quantum overheads are included, or whether it has been independently reproduced.

**Evidence**

- Q-CTRL claims a publicly available IBM quantum computer, combined with its infrastructure software, solved a materials-related problem over 3,000 times faster in wall-clock time than an industry-standard classical alternative, with comparable or better accuracy and practical runtime. [S5]
- The same source defines this result as “Practical Quantum Advantage” and says it demonstrates positive ROI, but the retrieved evidence is only the company’s announcement and does not provide the underlying paper’s methods, baseline details, cost accounting, or independent replication. [S5]

#### Finding 6

**Claim**

Claims that quantum computing will soon improve AI and reduce costs remain projections or company objectives, not demonstrated commercial advantages in the supplied evidence.

**Confidence:** High

**Why this confidence level**

The source itself frames the AI benefits as an intended outcome and describes research activity rather than a completed comparative deployment, though it also contains strong promotional language.

**Evidence**

- Quantinuum presents quantum AI as a future solution to the cost and scalability problems of classical language models and describes ongoing work translating NLP methods into quantum systems; it does not report a commercial benchmark demonstrating superiority over classical AI. [S4]

#### Finding 7

**Claim**

The supplied evidence is insufficient to estimate how close quantum computers are to broadly commercially useful advantage or to establish a reliable timeline.

**Confidence:** High

**Why this confidence level**

This is an evidence-gap assessment based on what the retrieved excerpts do and do not contain.

**Evidence**

- The sources provide general barrier descriptions and one unverified vendor-reported speedup, but no independent, end-to-end comparisons across application domains, resource estimates for fault-tolerant systems, or validated deployment economics. [S3] [S4] [S5]

### Conflicts Found

- Q-CTRL presents practical commercial advantage as achieved today through its IBM-plus-software demonstration, while Quantinuum describes major AI benefits as forthcoming and the other general source describes quantum computers as not yet replacements for classical machines. These positions may be conditionally compatible—an isolated application-specific vendor claim versus broad or general-purpose advantage—but the supplied material does not independently resolve the condition. [S3] [S4] [S5]
- Q-CTRL reports a 3,000-times speedup, whereas the surrounding retrieved material does not report an independently verified speedup or commercial deployment. This is an evidentiary asymmetry rather than a direct numerical contradiction. [S3] [S5]

### Important Gaps

- What exact materials-simulation instance, algorithm, hardware execution time, preprocessing/postprocessing, repetitions, and classical baseline underlie Q-CTRL’s claimed 3,000-times speedup?
- Does the claimed speedup include quantum hardware access cost, calibration, compilation, error suppression, data loading, and the cost of achieving the stated accuracy?
- Has the Q-CTRL result been independently replicated or evaluated by an independent benchmark study?
- What logical-qubit count, physical-qubit overhead, gate fidelity, error-correction performance, and runtime are required for commercially important chemistry, materials, optimization, or cryptographic workloads?
- Which application domains have demonstrated end-to-end economic advantage rather than merely a favorable algorithmic or benchmark result?
- The OECD source excerpt supplied here contains navigation material but no substantive findings, so it cannot presently support conclusions about business readiness or barriers.

**Analysis Duration:** 19.04s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

Another search would materially improve the answer because the central present-day commercial claim is from a vendor source and lacks the independent technical details needed to separate genuine end-to-end advantage from a favorable benchmark setup. Authoritative primary papers and independent evaluations are also needed for demonstrated advantage and quantified barriers.

**Next Search**

> independent peer-reviewed evidence practical quantum advantage commercial utility 2024 2025 IBM materials simulation benchmark

---

# Iteration 2

## 1. Search

**Query**

> independent peer-reviewed evidence practical quantum advantage commercial utility 2024 2025 IBM materials simulation benchmark

**Why this query**

Another search would materially improve the answer because the central present-day commercial claim is from a vendor source and lacks the independent technical details needed to separate genuine end-to-end advantage from a favorable benchmark setup. Authoritative primary papers and independent evaluations are also needed for demonstrated advantage and quantified barriers.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S6 — What quantum computer to buy?**
  URL: https://arxiv.org/html/2604.04761v1
- **S7 — Q-CTRL Delivers 3,000x Speedup in Materials Discovery for the Energy Sector with Quantum Computing, Demonstrates Evidence of Practical Quantum Advantage | Q-CTRL**
  URL: https://q-ctrl.com/blog/q-ctrl-delivers-3-000x-speedup-in-materials-discovery-for-the-energy-sector-with-quantum-computing-and-demonstrates-evidence-of-practical-quantum-advantage
- **S8 — IBM Quantum's Role in Pharmaceutical Drug Discovery | IntuitionLabs**
  URL: https://intuitionlabs.ai/articles/ibm-quantum-drug-discovery
- **S9 — Evidence for the utility of quantum computing before fault tolerance**
  URL: https://www.nature.com/articles/s41586-023-06096-3
- **S10 — IBM's Three Quantum Advantage Claims, Fact-Checked**
  URL: https://postquantum.com/industry-news/ibm-trusted-quantum-advantage-three-papers

**Search Duration:** 4.08s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The evidence still does not establish broad, general-purpose commercial quantum advantage; the strongest current case is for narrow, application-specific benefits and procurement experiments rather than replacement of classical computing.

**Confidence:** High

**Why this confidence level**

The conclusion is supported by both the new procurement-oriented source and the accumulated evidence, and does not depend on accepting a single vendor’s performance claim.

**Evidence**

- The procurement manuscript frames quantum capability as a set of use cases—cloud exploration, reserved access, local methods development, or strategic infrastructure—and warns that promising research results and vendor roadmaps do not prove delivered capability or determine a hardware winner. [S6]
- The accumulated evidence identifies potential advantages mainly in selected simulation, optimization, and cryptographic workloads, not general-purpose computing. [S3] [S5]

#### Finding 2

**Claim**

The Q-CTRL materials-discovery result is a more specific and technically detailed claim than previously available, but it remains a vendor-reported demonstration rather than independently established commercial advantage in the supplied evidence.

**Confidence:** Low

**Why this confidence level**

The result is concrete and includes problem area, runtimes, and claimed accuracy, but all supplied evidence for it comes from Q-CTRL’s own announcement; the key methodological and economic questions remain unresolved.

**Evidence**

- Q-CTRL reports a 120-qubit fermionic-materials simulation completed in two minutes on IBM hardware with its software, versus more than 100 hours for an industry-standard classical implementation, while claiming comparable accuracy and commercial relevance. [S7]
- The announcement says the comparison used a state-of-the-art materials-science package and that the classical runtime increased when resolution was raised to improve agreement, but the retrieved material still does not provide independent replication, complete cost accounting, or a neutral benchmark assessment. [S7]
- The prior evidence already characterized the same 3,000-times result as unverified because the baseline, overheads, and methodology could not be independently assessed. [S5]

#### Finding 3

**Claim**

The Q-CTRL result, even if reproduced, would demonstrate a narrow practical advantage for a particular materials-simulation workflow, not proof that quantum computers are broadly commercially superior.

**Confidence:** High

**Why this confidence level**

This follows directly from the stated scope of the claimed demonstration and the procurement framework; it does not require accepting the claimed speedup as independently valid.

**Evidence**

- Q-CTRL defines practical advantage as outperforming the best available conventional alternative on a real-world application and describes its result specifically as fermionic simulation for materials science. [S7]
- The procurement source emphasizes that an industrial buyer may care only whether a target workload benefits, and that different capability layers and operating burdens must be evaluated separately. [S6]

#### Finding 4

**Claim**

Pre-fault-tolerant quantum computing has produced scientifically meaningful utility demonstrations, but the supplied Nature source does not provide enough article content here to determine whether those demonstrations constitute advantage over classical systems.

**Confidence:** Medium

**Why this confidence level**

The source’s title and publication status support the existence of a utility claim, but the supplied content is insufficient to characterize its magnitude, scope, or commercial relevance.

**Evidence**

- The Nature article is titled “Evidence for the utility of quantum computing before fault tolerance” and is presented as a peer-reviewed 2023 research article, indicating relevance to pre-fault-tolerance utility. [S9]
- The retrieved excerpt contains bibliographic and landing-page information but no abstract, results, classical baseline, or commercial-economics details. [S9]

#### Finding 5

**Claim**

Current procurement advice favors acquiring access, benchmarking, and expertise before purchasing large on-premises systems, unless an institution has a clear mission, facilities, staffing, governance, and upgrade rationale.

**Confidence:** Medium

**Why this confidence level**

This is a direct recommendation from a procurement framework rather than independent evidence of computational performance, but it is consistent with the accumulated evidence about immature economics and operational barriers.

**Evidence**

- The procurement manuscript recommends starting with the smallest capability layer that produces repeatable near-term value and says large local systems require clear mission requirements, site readiness, staffing, governance, and upgrade paths. [S6]

#### Finding 6

**Claim**

The principal technical barriers remain noise and error suppression/correction, scaling to sufficiently capable systems, and the infrastructure and workflow overhead surrounding quantum execution.

**Confidence:** High

**Why this confidence level**

The barriers are consistent across technical and procurement-oriented sources, though the supplied material still lacks quantitative thresholds for when they will be overcome.

**Evidence**

- The prior sources identify noise, decoherence, insufficient scale, error correction, and demanding operating conditions as central limitations. [S3] [S5]
- Q-CTRL’s announcement itself says noise and errors can prevent useful results and presents runtime error suppression as necessary to obtain the reported result. [S7]
- The procurement source adds practical barriers including facilities, staffing, service contracts, queue quality, software maturity, security, and upgrade pressure; it also warns that qubit counts alone do not reveal useful performance. [S6]

### Conflicts Found

- Q-CTRL presents its materials result as the first practical quantum advantage and as evidence of positive ROI from currently available systems, whereas the procurement source cautions that promising results do not guarantee a supported commercial product or useful institutional capability. These are conditionally compatible: a narrow vendor-reported application result could coexist with the absence of broad commercial readiness. [S6] [S7]
- Q-CTRL describes its result as an achieved practical advantage, but the supplied third-party commentary on other IBM advantage claims stresses that advantage claims can differ in evidentiary strength and that difficult results may remain active candidates rather than adjudicated demonstrations. This is not a direct contradiction about the Q-CTRL experiment, but it reinforces the need for independent validation. [S7] [S10]
- The Nature article’s title suggests pre-fault-tolerant utility, while the accumulated evidence emphasizes that commercially useful advantage remains unestablished in general. The disagreement is only apparent because the supplied Nature excerpt does not reveal whether its utility means scientific usefulness, computational advantage, or economic advantage. [S9] [S3] [S5]

### Important Gaps

- What are the complete methods, accuracy metrics, sampling requirements, preprocessing and postprocessing costs, and classical hardware specifications in the Q-CTRL materials benchmark?
- Does the reported two-minute quantum runtime include queueing, calibration, compilation, error-suppression overhead, repetitions, data loading, and the cost of obtaining comparable accuracy?
- Has the Q-CTRL result been independently reproduced, ideally by a team without a commercial stake in the software or hardware?
- What exactly does the Nature paper demonstrate, and does its utility result outperform the best classical method on an economically relevant end-to-end task?
- For commercially important chemistry and materials workloads, what logical-qubit counts, physical-qubit overheads, error rates, and runtimes are required?
- Which claimed advantages survive comparison with optimized classical algorithms, modern accelerators, and full workflow economics rather than only wall-clock QPU time?

**Analysis Duration:** 19.47s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

A focused additional search could materially improve the answer by retrieving the underlying technical manuscript for the most important present-day commercial-advantage claim and any independent assessment or replication. The current evidence supports a cautious conclusion but cannot determine whether the 3,000-times result is an apples-to-apples, end-to-end advantage.

**Next Search**

> Q-CTRL arXiv 2605.04025 3000x materials simulation independent analysis benchmark classical baseline overhead

---

# Iteration 3

## 1. Search

**Query**

> Q-CTRL arXiv 2605.04025 3000x materials simulation independent analysis benchmark classical baseline overhead

**Why this query**

A focused additional search could materially improve the answer by retrieving the underlying technical manuscript for the most important present-day commercial-advantage claim and any independent assessment or replication. The current evidence supports a cautious conclusion but cannot determine whether the 3,000-times result is an apples-to-apples, end-to-end advantage.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S11 — Q-CTRL Achieves 3,000x Speedup in Quantum Materials Simulation - Quantum Computing Report**
  URL: https://quantumcomputingreport.com/q-ctrl-achieves-3000x-speedup-in-quantum-materials-simulation
- **S12 — [2605.04025] Fast, accurate, high-resolution simulation of large-scale Fermi-Hubbard models on a digital quantum processor**
  URL: https://arxiv.org/abs/2605.04025
- **S13 — Q-CTRL Claims 3000x Quantum Speedup for Materials ... - HPC Wire**
  URL: https://www.hpcwire.com/off-the-wire/q-ctrl-claims-3000x-quantum-speedup-for-materials-science-simulations-on-ibm-quantum-platform
- **S14 — Quantum Revolution: Unlocking 3000x Speed in Materials Discovery with Q-CTRL (2026)**
  URL: https://zonneman.com/article/quantum-revolution-unlocking-3000x-speed-in-materials-discovery-with-q-ctrl

**Search Duration:** 7.17s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources add corroboration that Q-CTRL and IBM report a 3,000-fold wall-clock speedup for a 120-qubit Fermi–Hubbard simulation, but they do not independently establish commercial quantum advantage.

**Confidence:** Low

**Why this confidence level**

The numerical claim is repeated by a secondary report, but the available evidence ultimately traces to the Q-CTRL/IBM result and lacks independent replication, complete overhead accounting, and substantive access to the technical paper.

**Evidence**

- Quantum Computing Report describes a 120-qubit simulation completed in approximately two minutes, compared with more than 100 hours for a performance-optimized classical TDVP solver at comparable accuracy. [S11]
- HPC Wire repeats the two-minute versus 100-hour comparison, but its supplied text is only a brief report and does not independently analyze the benchmark methodology. [S13]
- The arXiv landing page identifies the technical manuscript, but the retrieved content provides no abstract, methods, results, or comparison details that can be evaluated here. [S12]

#### Finding 2

**Claim**

If the reported result is methodologically sound and survives independent replication, it would represent a narrow application-specific practical advantage rather than broad superiority over classical computers.

**Confidence:** High

**Why this confidence level**

The limited scope of the claimed demonstration is directly evident even without accepting the reported speedup; the conclusion about what it could establish is appropriately narrower than the vendor’s broader commercial interpretation.

**Evidence**

- The reported task is a specific one-dimensional Fermi–Hubbard materials simulation, using a 120-qubit processor and runtime error suppression, rather than a general-purpose workload. [S11]
- The source frames the claimed benefit relative to a particular classical TDVP/tensor-network workflow and acknowledges that future specialized classical algorithms or GPU-accelerated tensor networks could improve the baseline. [S11]
- The accumulated procurement evidence emphasizes evaluating advantage at the target-workload level and warns that promising results do not by themselves establish broad commercial readiness. [S6]

#### Finding 3

**Claim**

The reported experiment illustrates that error suppression and software-layer performance management are currently central to extracting useful results from noisy hardware, rather than eliminating the underlying hardware limitations.

**Confidence:** Medium

**Why this confidence level**

The operational details are reported by a secondary source summarizing the experiment, while the general conclusion is consistent with multiple accumulated sources.

**Evidence**

- The experiment reportedly used more than 10,000 two-qubit operations and up to 90 Trotter steps, while Q-CTRL applied runtime error suppression to maintain accuracy on NISQ hardware. [S11]
- The broader evidence identifies noise, decoherence, error correction, scaling, and infrastructure as persistent barriers; the new report adds software overhead and workflow dependence to that picture. [S3] [S5] [S6] [S11]

#### Finding 4

**Claim**

The new evidence does not materially change the overall assessment: quantum computers have not yet demonstrated broad, independently validated, end-to-end commercial advantage over classical systems, although a potentially important narrow materials-simulation result is emerging.

**Confidence:** High

**Why this confidence level**

The new material strengthens the case that a specific candidate result deserves technical scrutiny, but does not resolve the previously identified evidentiary gaps.

**Evidence**

- The new sources provide a concrete vendor-associated benchmark but no independent replication, full economic comparison, or demonstrated industrial deployment producing measurable business value. [S11] [S12] [S13]
- Prior evidence likewise finds that current support is strongest for narrow application-specific benefits and procurement experiments, not replacement of classical computing. [S6] [S3] [S5]

### Conflicts Found

- Q-CTRL-associated reporting presents the Fermi–Hubbard result as evidence of present practical advantage and positive ROI, while the available arXiv page supplies no evaluable technical details and the broader procurement evidence cautions that promising results do not prove supported commercial capability. These positions are conditionally compatible, but the commercial interpretation remains unverified. [S6] [S11] [S12]
- The new secondary report describes the classical comparison as performance-optimized and at comparable accuracy, whereas the accumulated evidence continues to identify unresolved questions about the exact classical hardware, preprocessing/postprocessing, sampling, error-suppression, and total workflow costs. This is an evidentiary gap rather than a demonstrated numerical contradiction. [S6] [S7] [S11]

### Important Gaps

- What are the full methods and results in arXiv:2605.04025, including the exact quantum and classical workloads, hardware specifications, accuracy metrics, and reproducibility information?
- Does the two-minute figure include queueing, calibration, compilation, repetitions, data loading, error suppression, postprocessing, and the cost of achieving comparable accuracy?
- Was the TDVP/tensor-network baseline optimized fairly across classical hardware, software, precision, and resolution settings?
- Has the result been independently reproduced or critically evaluated by researchers without a commercial stake in Q-CTRL or IBM?
- Does the claimed speedup translate into an end-to-end materials-discovery or industrial R&D benefit, rather than faster execution of a physics benchmark?
- What logical-qubit, physical-qubit, error-correction, and runtime requirements would be needed for commercially important workloads beyond this specific Fermi–Hubbard instance?

**Analysis Duration:** 18.12s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources materially strengthen the description of the claimed benchmark but do not answer the most important unresolved question: whether the result is independently validated and economically meaningful after full workflow costs and state-of-the-art classical alternatives are included. The arXiv landing-page excerpt is insufficient for technical adjudication.

**Next Search**

> 2605.04025 Fermi-Hubbard Q-CTRL independent analysis benchmark classical baseline overhead replication

---

# Iteration 4

## 1. Search

**Query**

> 2605.04025 Fermi-Hubbard Q-CTRL independent analysis benchmark classical baseline overhead replication

**Why this query**

The new sources materially strengthen the description of the claimed benchmark but do not answer the most important unresolved question: whether the result is independently validated and economically meaningful after full workflow costs and state-of-the-art classical alternatives are included. The arXiv landing-page excerpt is insufficient for technical adjudication.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S15 — How should problem-specific compilation be counted in the ...**
  URL: https://quantumcomputing.stackexchange.com/questions/46252/how-should-problem-specific-compilation-be-counted-in-the-q-ctrl-fermi-hubbard-q
- **S16 — Fermi-Hubbard on a quantum computer, part 5: quantum advantage or time-to-answer? - Edukaizen**
  URL: https://edukaizen.nl/fermi-hubbard-quantum-computer-part-5-quantum-advantage-or-time-to-answer
- **S17 — Efficient data replication in distributed clouds via quantum ...**
  URL: https://www.sciencedirect.com/science/article/pii/S2215016125006065
- **S18 — Pushing the Classical Frontier of 1D Fermi–Hubbard ...**
  URL: https://arxiv.org/html/2606.04771v1

**Search Duration:** 2.99s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new material strengthens the view that the Q-CTRL Fermi–Hubbard result should be evaluated as a task-specific time-to-answer comparison, not as proof of general quantum superiority.

**Confidence:** High

**Why this confidence level**

The source directly explains the scope and limitations of the comparison, consistent with the prior evidence that the result is narrow rather than general.

**Evidence**

- The analysis distinguishes circuit or execution time from full benchmark time, which may include queueing, preprocessing, compilation, calibration, error mitigation, postprocessing, and classical convergence studies. [S16]
- It states that the quantum result does not show that no classical method can solve the task, but may indicate a better practical time-to-answer for a particular observable and accuracy target. [S16]

#### Finding 2

**Claim**

The reported Q-CTRL speedup is sensitive to the definition of runtime and to the chosen classical approximation parameters.

**Confidence:** Medium

**Why this confidence level**

The numerical comparison is reported by a secondary commentary source and is not independently verified here, but the methodological dependence is explicit.

**Evidence**

- S16 reports an approximately 272.5-fold comparison using 9,033 seconds of classical MPS wall time versus a 33.15-second quantum execution proxy, but notes that alternative timing conventions produce different claims. [S16]
- The source says classical truncation choices affect both runtime and accuracy: a faster cutoff was insufficiently accurate, while a more accurate cutoff took substantially longer and required convergence validation. [S16]

#### Finding 3

**Claim**

Classical algorithms are actively improving against the Q-CTRL benchmark, so the claimed advantage is not a fixed comparison against an unchanging classical frontier.

**Confidence:** Medium

**Why this confidence level**

The sources establish an active classical response, but the supplied excerpt does not quantify the revised performance or establish which method is ultimately superior.

**Evidence**

- S16 says better symmetry-aware GPU tensor-network simulations can substantially reduce the original speedup and identifies a classical-response paper. [S16]
- S18 identifies the Q-CTRL simulation and presents a classical-frontier response concerning the one-dimensional Fermi–Hubbard problem. [S18]

#### Finding 4

**Claim**

Problem-specific compilation and workflow accounting remain important unresolved issues in assessing the Q-CTRL claim.

**Confidence:** High

**Why this confidence level**

These are directly identified methodological issues and align with the previously documented gaps concerning preprocessing, error suppression, and total workflow costs.

**Evidence**

- S15 explicitly raises how problem-specific compilation should be counted in the Q-CTRL Fermi–Hubbard advantage claim. [S15]
- S16 lists layout and calibration search, error mitigation, postprocessing, and classical tuning and validation as potentially relevant components of a fair comparison. [S16]

#### Finding 5

**Claim**

The overall assessment is unchanged: there is still no supplied evidence of broad, independently validated, end-to-end commercial quantum advantage, although the Fermi–Hubbard result remains a serious candidate for a narrow application-specific advantage.

**Confidence:** High

**Why this confidence level**

The new material adds methodological caution rather than contradictory validation; the central evidentiary gaps remain unresolved.

**Evidence**

- The new commentary characterizes the result as a candidate time-to-answer advantage for a specific Hamiltonian, observable, accuracy target, and workflow rather than a proof that classical methods are incapable. [S16]
- The prior evidence finds that the result is vendor-associated, lacks independent replication and complete economic accounting, and does not establish broad commercial superiority. [S6] [S7] [S11] [S12] [S13]

### Conflicts Found

- Q-CTRL-associated sources present the Fermi–Hubbard result as practical quantum advantage and positive ROI, while S16 recommends the more limited interpretation of a possible task-specific time-to-answer advantage. This is a conditional disagreement about the proper label and scope, not necessarily about the underlying measurements. [S7] [S11] [S16]
- The reported speedup depends on the selected classical method, truncation or convergence settings, hardware execution proxy, and whether full workflow costs are included. Thus, the large vendor-reported speedup and the smaller or potentially absent advantage after improved classical methods and broader accounting are competing evaluations rather than directly comparable figures. [S16] [S18]

### Important Gaps

- What are the quantitative results of the classical-response work in S18, and how do they compare with the Q-CTRL baseline under matched accuracy and hardware conditions?
- How should problem-specific compilation, calibration, error suppression, repetitions, postprocessing, and classical convergence studies be included in an end-to-end time-to-answer comparison?
- Does the reported result produce a downstream materials-science or industrial R&D benefit, rather than only a faster execution of a selected physics benchmark?
- Has the benchmark been independently reproduced by researchers without a commercial stake in the hardware or software?
- What are the complete methods and economic assumptions in the underlying technical paper, arXiv:2605.04025?
- What fault-tolerant resource requirements are needed for commercially important workloads beyond this narrow Fermi–Hubbard instance?

**Analysis Duration:** 15.09s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources materially clarify why the leading claimed demonstration is difficult to interpret, but they do not resolve the most important gap: an independent, quantitatively detailed comparison against the improved classical frontier using end-to-end time-to-answer and economic accounting.

**Next Search**

> independent quantitative critique Q-CTRL Fermi-Hubbard 2605.04025 classical response 2606.04771 benchmark time-to-answer

---

# Iteration 5

## 1. Search

**Query**

> independent quantitative critique Q-CTRL Fermi-Hubbard 2605.04025 classical response 2606.04771 benchmark time-to-answer

**Why this query**

The new sources materially clarify why the leading claimed demonstration is difficult to interpret, but they do not resolve the most important gap: an independent, quantitatively detailed comparison against the improved classical frontier using end-to-end time-to-answer and economic accounting.

**Results**

5 results retrieved.

1 new unique source added.

### Sources

- **S19 — [2606.04771] Pushing the Classical Frontier of 1D Fermi-Hubbard Quench Dynamics Beyond Current Quantum Simulations**
  URL: https://arxiv.org/abs/2606.04771

**Search Duration:** 3.84s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

A new arXiv paper explicitly presents itself as pushing the classical frontier of one-dimensional Fermi–Hubbard quench dynamics beyond current quantum simulations, reinforcing that classical methods remain an active and relevant comparator for the benchmark associated with the claimed quantum advantage.

**Confidence:** Medium

**Why this confidence level**

The title directly supports the existence and stated scope of a classical-frontier claim, but the retrieved page contains no abstract, methods, numerical results, or evidence that can establish the magnitude of the classical improvement.

**Evidence**

- The paper title states that it pushes the classical frontier of 1D Fermi–Hubbard quench dynamics beyond current quantum simulations. [S19]

#### Finding 2

**Claim**

The new source does not establish that the Q-CTRL/IBM Fermi–Hubbard result has been overturned, nor does it independently validate the claimed quantum speedup.

**Confidence:** High

**Why this confidence level**

No technical results from S19 are available in the supplied content, so stronger conclusions would exceed the evidence.

**Evidence**

- The supplied S19 content is only an arXiv landing page and provides no quantitative comparison, matched accuracy conditions, hardware specifications, or independent assessment of the Q-CTRL benchmark. [S19]
- Prior evidence already identified the classical baseline, workflow accounting, and independent-replication questions as unresolved. [S16] [S18]

#### Finding 3

**Claim**

The overall answer remains unchanged: the Fermi–Hubbard result is best treated as a candidate narrow, task-specific advantage, while broad commercially useful quantum advantage remains un demonstrated in the supplied evidence.

**Confidence:** High

**Why this confidence level**

The new source strengthens the case for treating the classical baseline as dynamic and unresolved, without supplying evidence that changes the prior conclusion.

**Evidence**

- S19 indicates an active classical response to the same class of dynamics, but does not provide enough information to determine whether the quantum result remains faster, under what accuracy target, or with what end-to-end costs. [S19]
- Accumulated evidence characterizes the result as vendor-associated, methodologically contested, and limited to a specific materials-simulation workflow rather than broad commercial superiority. [S6] [S7] [S11] [S16] [S18]

### Conflicts Found

- S19's title claims that classical simulation has been pushed beyond current quantum simulations, whereas Q-CTRL-associated sources present the Fermi–Hubbard computation as a practical quantum advantage. Because S19's abstract and results are unavailable, this is a potential or conditional conflict rather than an established numerical contradiction. [S7] [S11] [S19]
- The existence of a classical-frontier paper is consistent with prior commentary that improved tensor-network or GPU methods may reduce the reported quantum speedup, but the supplied material does not reveal whether S19 uses matched accuracy, comparable hardware, or full workflow accounting. [S16] [S18] [S19]

### Important Gaps

- What quantitative speedups, accuracy targets, system sizes, and hardware configurations does S19 report?
- Does S19 directly benchmark the Q-CTRL/IBM instance or a different Fermi–Hubbard quench problem?
- Under matched accuracy and complete time-to-answer accounting, does the classical method outperform the quantum workflow?
- Does S19 include preprocessing, compilation, calibration, error suppression, repetitions, postprocessing, and convergence costs on both sides?
- Has either the Q-CTRL result or the S19 classical result been independently replicated and peer reviewed?

**Analysis Duration:** 10.51s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

This source signals a potentially important classical response to the strongest current candidate for narrow quantum advantage, but the retrieved content contains no technical details. Obtaining the paper's abstract or full results could materially change the assessment of whether the claimed speedup survives an improved classical baseline.

**Next Search**

> arXiv:2606.04771 Fermi-Hubbard quench dynamics classical benchmark Q-CTRL 120 qubit results

---

# Iteration 6

## 1. Search

**Query**

> arXiv:2606.04771 Fermi-Hubbard quench dynamics classical benchmark Q-CTRL 120 qubit results

**Why this query**

This source signals a potentially important classical response to the strongest current candidate for narrow quantum advantage, but the retrieved content contains no technical details. Obtaining the paper's abstract or full results could materially change the assessment of whether the claimed speedup survives an improved classical baseline.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S20 — Pushing the Classical Frontier of 1D Fermi-Hubbard ...**
  URL: https://arxiv.org/pdf/2606.04771
- **S21 — Q-CTRL Claims Practical Quantum Advantage**
  URL: https://postquantum.com/industry-news/qctrl-fermi-hubbard-3000x-quantum-speedup
- **S22 — Pushing the Classical Frontier of Quantum Simulation**
  URL: https://multiversecomputing.com/resources/pushing-the-classical-frontier-of-quantum-simulation

**Search Duration:** 7.28s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The Q-CTRL/IBM Fermi–Hubbard result no longer supports a 3,000-fold quantum advantage when compared with the new classical implementation at a comparable bond dimension; the reported reduction is to approximately 36-fold based on the authors’ stated runtimes.

**Confidence:** Medium

**Why this confidence level**

The paper gives a specific quantitative rebenchmark, but it is a new arXiv preprint from a company with a direct interest in classical simulation and does not by itself establish the definitive best classical baseline or a complete end-to-end comparison.

**Evidence**

- The classical-frontier paper reports approximately 100 minutes on four NVIDIA H200 GPUs at a bond dimension comparable to Q-CTRL’s χ=4096 baseline, versus Q-CTRL’s roughly 166 seconds of bare QPU time, reducing the claimed 3,000-fold speedup to about 36-fold. [S20]
- The authors state that Q-CTRL’s original comparison used more than 160 CPU-cluster hours versus approximately 166 seconds of bare QPU execution. [S20]

#### Finding 2

**Claim**

The original Q-CTRL classical benchmark did not verify the most difficult portion of the simulated evolution, according to the new classical-frontier paper.

**Confidence:** Medium

**Why this confidence level**

This is a direct methodological criticism in the new paper, but the supplied evidence does not include an independent adjudication or the full Q-CTRL manuscript.

**Evidence**

- The paper says Q-CTRL’s χ=4096 TDVP calculation agreed with hardware only through approximately t=5.2 and diverged in the high-entanglement interval t∈[5.2,6], leaving that portion unverified. [S20]
- The paper claims its symmetry-enhanced, GPU-accelerated calculation achieves convergence across the entire interval and certifies the previously unresolved regime. [S20] [S22]

#### Finding 3

**Claim**

The classical frontier is materially stronger than the baseline used for the original Q-CTRL claim: exploiting additional Hamiltonian symmetry and GPUs enables bond dimensions up to approximately 62,000 and extends the simulation beyond the quantum experiment.

**Confidence:** Medium

**Why this confidence level**

The technical claims are detailed and consistent across the preprint and project summary, but both sources are associated with the same research group and the preprint has not been independently evaluated here.

**Evidence**

- The new study uses full U(1)×SU(2) symmetry and GPU-accelerated tensor contractions on four NVIDIA H200 GPUs, reaching χ≈62,000 and extending the evolution to t=7. [S20]
- The associated project description reports full convergence across the Q-CTRL window and extension beyond the quantum processor’s range. [S22]

#### Finding 4

**Claim**

The Q-CTRL result remains, at most, a candidate narrow task-specific advantage, not demonstrated broad commercial quantum advantage.

**Confidence:** High

**Why this confidence level**

Even accepting the reported measurements, the result is narrow, baseline-sensitive, and not an end-to-end industrial deployment. The new source strengthens rather than weakens this conclusion.

**Evidence**

- The classical response substantially narrows the headline speedup and establishes that a stronger classical method can fully certify the previously unresolved regime. [S20]
- The comparison remains specific to a one-dimensional Fermi–Hubbard quench and compares bare QPU execution with selected classical runtimes; the supplied text does not establish downstream materials-discovery value or complete economic advantage. [S20] [S21]
- The broader procurement evidence emphasizes workload-specific evaluation and warns that promising benchmark results do not establish broad commercial readiness. [S6]

#### Finding 5

**Claim**

The most important remaining barriers include not only hardware noise and scaling, but also fair benchmarking against rapidly improving classical algorithms and complete time-to-answer accounting.

**Confidence:** High

**Why this confidence level**

The new methodological evidence directly demonstrates baseline sensitivity, and the technical and procurement sources consistently identify the underlying hardware and operational barriers.

**Evidence**

- The new paper shows that symmetry exploitation and GPU acceleration can change the claimed advantage by roughly two orders of magnitude, while noting that Q-CTRL’s original comparison excluded compilation, readout-error mitigation, decay recovery, and post-processing. [S20]
- The accumulated evidence identifies noise, decoherence, error correction, scale, infrastructure, and workflow overhead as persistent limitations. [S3] [S5] [S6] [S7]

### Conflicts Found

- Q-CTRL-associated reporting presents the Fermi–Hubbard experiment as a 3,000-fold practical quantum advantage, while the new classical-frontier paper reports a comparable-bond-dimension classical runtime that reduces this to approximately 36-fold and fully resolves the previously unverified high-entanglement interval. [S7] [S11] [S20]
- The Q-CTRL comparison uses bare QPU execution time, whereas the new paper states that this excluded readout-error mitigation, decay recovery, circuit compilation, and post-processing. The resulting figures are therefore not necessarily apples-to-apples end-to-end time-to-answer comparisons. [S20]
- The new paper claims fully converged classical results beyond the quantum experiment, but the supplied material does not independently verify its hardware utilization, accuracy conditions, total workflow costs, or comparison with every relevant classical method. [S20] [S22]
- S21 reports a subsequent single-observable Majorana-Propagation result that may challenge the 3,000-fold claim, but also records Q-CTRL’s response that the quantum run produced many observables simultaneously and that the single-site comparison lacks quantitative all-site accuracy analysis. This remains a conditional methodological dispute, not a settled reversal. [S21]

### Important Gaps

- Does the approximately 36-fold residual comparison survive inclusion of quantum compilation, calibration, error suppression, readout mitigation, repetitions, post-processing, and classical preprocessing?
- Are the quantum and classical results matched for the same observables, accuracy target, system size, and output requirements?
- Does the new χ≈62,000 classical calculation produce all observables claimed by Q-CTRL, or only selected observables, and how should that difference affect time-to-answer comparisons?
- How does the new classical result compare with Majorana Propagation and other classical approaches under matched accuracy and output scope?
- Has either the Q-CTRL experiment or the classical-frontier rebenchmark been independently reproduced by a group without a commercial stake?
- Does the Fermi–Hubbard benchmark yield a downstream materials-science or industrial R&D benefit rather than only a faster simulation of a physics model?
- What logical-qubit and fault-tolerant resource requirements are needed for commercially important workloads beyond this benchmark?

**Analysis Duration:** 18.29s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new source materially changes the assessment of the strongest claimed present-day advantage, but it is a company-authored preprint and leaves unresolved whether any advantage survives full workflow accounting, matched output requirements, competing classical algorithms, and independent review. One focused search for independent technical evaluation or replication would materially improve the answer.

**Next Search**

> independent replication critique Q-CTRL IBM Fermi-Hubbard 3000x 36x Majorana Propagation matched accuracy time-to-answer

---

# Iteration 7

## 1. Search

**Query**

> independent replication critique Q-CTRL IBM Fermi-Hubbard 3000x 36x Majorana Propagation matched accuracy time-to-answer

**Why this query**

The new source materially changes the assessment of the strongest claimed present-day advantage, but it is a company-authored preprint and leaves unresolved whether any advantage survives full workflow accounting, matched output requirements, competing classical algorithms, and independent review. One focused search for independent technical evaluation or replication would materially improve the answer.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S23 — Fermi-Hubbard on a quantum computer, part 7: Majorana propagation as a laptop competitor - Edukaizen**
  URL: https://edukaizen.nl/fermi-hubbard-quantum-computer-part-7-majorana-propagation-as-a-laptop-competitor
- **S24 — Q-CTRL Claims Practical Quantum Advantage | Marin Ivezic**
  URL: https://www.linkedin.com/posts/marinivezic_q-ctrl-claims-practical-quantum-advantage-activity-7457729398838845441-azDK
- **S25 — Can a quantum computer beat classical methods on ...**
  URL: https://quantumcomputing.stackexchange.com/questions/46335/can-a-quantum-computer-beat-classical-methods-on-a-specific-fermi-hubbard-observ

**Search Duration:** 5.57s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

A Majorana-propagation classical method can outperform the quantum execution proxy for a selected observable, but its advantage depends strongly on the chosen accuracy cutoff.

**Confidence:** Medium

**Why this confidence level**

The source provides concrete timings and errors, but it is a project/blog report rather than an independent peer-reviewed benchmark.

**Evidence**

- For mean double occupancy in the 120-qubit/60-site/30-step benchmark, the source reports 20.96 seconds at cutoff 2—faster than the approximately 33-second quantum execution proxy—but with visibly larger error. At cutoff 4, the error is much smaller, but runtime rises to approximately 1,153.51 seconds. [S23]

#### Finding 2

**Claim**

The new Majorana comparison reinforces that fair quantum-advantage evaluation must include validation and convergence costs, not only the runtime of a selected classical approximation.

**Confidence:** High

**Why this confidence level**

The methodological point is directly stated in S23 and is consistent with multiple prior sources.

**Evidence**

- S23 explicitly notes that selecting a reliable cutoff may require a more expensive reference calculation or convergence study, making validation part of the practical time-to-answer workflow. [S23]
- Earlier evidence likewise identifies preprocessing, convergence studies, error mitigation, postprocessing, and other workflow components as unresolved components of fair comparisons. [S16] [S20]

#### Finding 3

**Claim**

The Majorana result weakens a simple claim that the quantum computer beats classical methods, but it does not establish that the classical method universally dominates the quantum workflow.

**Confidence:** Medium

**Why this confidence level**

The scope limitation is clear, but the reported output differences and total workflow costs are not independently verified.

**Evidence**

- S23 compares only mean double occupancy, which is narrower than the full charge/spin output, and states that the quantum route produced a full-instance measurement without requiring a cutoff choice in advance. [S23]
- The source itself characterizes the appropriate conclusion as a task- and observable-specific time-to-answer comparison rather than a general statement that quantum computing beats Majorana propagation. [S23]

#### Finding 4

**Claim**

S24 adds no independent evidence beyond repeating the vendor-associated 3,000-fold Fermi–Hubbard speedup claim.

**Confidence:** High

**Why this confidence level**

The source is plainly a brief repost and contributes no substantive validation.

**Evidence**

- The post restates that Q-CTRL achieved a 3,000-fold speedup for a 120-qubit Fermi–Hubbard simulation on IBM hardware, without methods, baseline details, cost accounting, or independent analysis. [S24]

#### Finding 5

**Claim**

S25 does not materially update the evidence because the supplied content contains only the question title and introductory sentence, with no technical result or evaluation.

**Confidence:** High

**Why this confidence level**

There is no substantive evidence in the supplied excerpt.

**Evidence**

- The retrieved Stack Exchange content ends before presenting an answer, benchmark, or analysis. [S25]

#### Finding 6

**Claim**

The overall assessment remains unchanged: the Fermi–Hubbard experiment is at most a candidate narrow, task-specific advantage, while broad independently validated commercial quantum advantage remains undemonstrated in the supplied evidence.

**Confidence:** High

**Why this confidence level**

The new material adds methodological nuance but no independent validation or broad commercial demonstration.

**Evidence**

- S23 shows that classical performance varies substantially by observable, approximation parameter, and validation requirements; S24 merely repeats the original vendor claim. [S23] [S24]
- Prior classical-frontier analysis reduced the headline comparison from roughly 3,000-fold to approximately 36-fold under a stronger classical baseline and identified incomplete end-to-end accounting. [S20]
- The accumulated evidence finds no independent replication, complete economic comparison, or demonstrated industrial deployment producing measurable business value. [S6] [S7] [S11] [S16] [S20]

### Conflicts Found

- Q-CTRL-associated sources present the Fermi–Hubbard experiment as a 3,000-fold practical advantage, whereas S23 shows that a classical method can be faster than the quantum execution proxy for one observable and that the result depends on accuracy and validation choices. This is a scope and benchmarking conflict, not a complete numerical contradiction, because S23 evaluates a narrower output than the full reported quantum output. [S7] [S11] [S23]
- S23 suggests a nuanced possible quantum benefit from producing a full-instance measurement without advance cutoff selection, while also acknowledging that Majorana propagation is faster at low accuracy and more accurate at a selected higher cutoff. The relative winner therefore depends on output scope, accuracy target, and whether validation costs are included. [S23]

### Important Gaps

- Does the Majorana-propagation method reproduce all observables in the Q-CTRL output, or only mean double occupancy?
- Are S23's classical and quantum timings measured with equivalent hardware, software, compilation, initialization, readout, repetitions, and postprocessing assumptions?
- Does the Majorana cutoff-convergence or reference-validation cost eliminate the reported local classical runtime advantage under a true end-to-end time-to-answer metric?
- How do the Majorana results compare with the newer symmetry-enhanced GPU classical calculation at matched observables, accuracy, and output scope?
- Has the Q-CTRL benchmark or any competing classical rebenchmark been independently reproduced and peer reviewed?
- Does the Fermi–Hubbard benchmark produce a downstream materials-science or industrial R&D benefit, rather than only a faster or more direct physics simulation?

**Analysis Duration:** 14.84s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new source materially sharpens the benchmark dispute by supplying observable-specific timings and accuracy tradeoffs, but it is not independent peer-reviewed validation and leaves the central questions—matched output scope, complete workflow accounting, and commercial value—unresolved. A focused search for the full technical paper and independent benchmark analysis could materially improve the assessment.

**Next Search**

> arXiv 2605.04025 independent benchmark Majorana propagation full observables end-to-end time-to-answer comparison

---

# Iteration 8

## 1. Search

**Query**

> arXiv 2605.04025 independent benchmark Majorana propagation full observables end-to-end time-to-answer comparison

**Why this query**

The new source materially sharpens the benchmark dispute by supplying observable-specific timings and accuracy tradeoffs, but it is not independent peer-reviewed validation and leaves the central questions—matched output scope, complete workflow accounting, and commercial value—unresolved. A focused search for the full technical paper and independent benchmark analysis could materially improve the assessment.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S26 — Introducing monoprop: propagation at escape velocity - Algorithmiq**
  URL: https://algorithmiq.fi/news/introducing-monoprop-propagation-at-escape-velocity
- **S27 — Code Review Bench: Towards Billion Dollar Benchmarks**
  URL: https://withmartian.com/post/code-review-bench-v0
- **S28 — ResearchClawBench: A Benchmark for End-to-End Autonomous Scientific Research**
  URL: https://arxiv.org/html/2606.07591v1

**Search Duration:** 4.89s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new source further weakens the case that the Q-CTRL/IBM Fermi–Hubbard experiment demonstrated a quantum advantage over classical computation.

**Confidence:** Medium

**Why this confidence level**

S26 provides a concrete, reproducible-looking classical result, but it is a company-authored source and the supplied text does not give enough detail to verify exact accuracy, output scope, or end-to-end timing against the quantum workflow.

**Evidence**

- Algorithmiq reports that its open-source monoprop engine reproduces the 60-site Fermi–Hubbard dynamics in approximately 10–15 seconds on a laptop, while explicitly limiting its claim to showing that classical methods can reach farther than often assumed. [S26]
- The accumulated evidence already reports stronger classical rebenchmarks reducing Q-CTRL’s headline comparison from roughly 3,000-fold to approximately 36-fold under a comparable bond-dimension baseline. [S20]

#### Finding 2

**Claim**

The classical frontier for this benchmark is active, accessible, and increasingly reproducible, making any claimed quantum advantage highly dependent on the selected classical algorithm and implementation.

**Confidence:** Medium

**Why this confidence level**

The evidence is technically specific and points toward reproducibility, but independent replication and matched benchmark conditions are still absent.

**Evidence**

- monoprop is released as open-source software, with benchmark scripts, settings, and hardware specifications stated to be available for reproduction; it implements both Majorana and Pauli propagation. [S26]
- The source reports matching physics between monoprop and MajoranaPropagation.jl on 1D Fermi–Hubbard instances, while improving runtime and memory usage as depth and system size increase. [S26]
- Earlier work reports that symmetry exploitation and GPU acceleration materially improve classical performance and challenge the original Q-CTRL baseline. [S20]

#### Finding 3

**Claim**

The monoprop result does not by itself establish that classical computation universally dominates the quantum approach.

**Confidence:** High

**Why this confidence level**

The scope limitation is explicit, and the unresolved comparison dimensions are consistently documented in the accumulated evidence.

**Evidence**

- S26 says it reproduces the benchmark for specific Fermi–Hubbard dynamics and makes no broader claim; the supplied content does not show all observables, accuracy targets, sampling requirements, or full workflow costs relative to the quantum experiment. [S26]
- Prior analysis found that classical-versus-quantum conclusions depend on observable scope, accuracy, convergence validation, and whether compilation, mitigation, postprocessing, and other costs are included. [S20] [S23]

#### Finding 4

**Claim**

The strongest current evidence still supports only a narrow, task-specific candidate advantage—not broad commercially useful quantum advantage.

**Confidence:** High

**Why this confidence level**

The conclusion is supported by the narrow scope of the new evidence and the persistent independent-validation and economics gaps.

**Evidence**

- The new classical result concerns a particular 60-site one-dimensional Fermi–Hubbard simulation rather than an industrial materials-discovery workflow or deployed commercial service. [S26]
- The accumulated record contains no independent replication, complete end-to-end economic comparison, or demonstrated industrial benefit from the Q-CTRL result. [S6] [S7] [S11] [S20] [S23]

#### Finding 5

**Claim**

S27 and S28 do not materially inform the question of quantum-computing commercial advantage.

**Confidence:** High

**Why this confidence level**

Their stated subjects are unrelated to the research question.

**Evidence**

- S27 concerns benchmarks for AI code-review systems, while S28 evaluates autonomous scientific-research agents; neither reports quantum hardware performance, quantum algorithms, classical comparisons for quantum workloads, or quantum commercialization. [S27] [S28]

### Conflicts Found

- Algorithmiq reports a 10–15 second laptop simulation of the 60-site Fermi–Hubbard dynamics, while Q-CTRL-associated sources present the corresponding quantum experiment as a roughly 3,000-fold speedup over a classical implementation. These are competing practical interpretations, but they may differ in observable set, accuracy, simulation interval, preprocessing, validation, and timing definitions; the supplied evidence does not make them directly comparable. [S7] [S11] [S23] [S26]
- Q-CTRL-associated sources characterize the experiment as practical quantum advantage and positive ROI, whereas Algorithmiq presents the benchmark as evidence that classical methods can reach further and avoids a broader advantage claim. The disagreement is about the appropriate scope and label, and remains unresolved without matched end-to-end benchmarking. [S7] [S26]
- S26 claims reproducible open-source benchmarks, but the source is produced by a company developing and promoting the classical method. This does not invalidate the result, but it means the new evidence is not independent adjudication of the quantum-versus-classical comparison. [S26]

### Important Gaps

- Does monoprop reproduce every observable and output requirement of the Q-CTRL quantum experiment, or only the reported dynamics/selected observables?
- Are the 10–15 second laptop figures matched to the same accuracy target, evolution interval, sampling uncertainty, and validation standard as the quantum result?
- Do monoprop timings include initialization, compilation, convergence checks, reference calculations, and postprocessing in the same way as the quantum workflow?
- How does monoprop compare with the symmetry-enhanced GPU calculation and other optimized tensor-network methods under identical hardware and accuracy conditions?
- Has the monoprop benchmark been independently reproduced by a group without a commercial interest in either the quantum or classical method?
- Does any Fermi–Hubbard benchmark yield downstream materials-science or industrial R&D value, rather than only faster simulation of a model problem?

**Analysis Duration:** 15.45s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new source materially strengthens the evidence that the headline Q-CTRL advantage is baseline-sensitive, but it does not resolve the key apples-to-apples questions: output scope, accuracy, validation, total workflow time, and independent replication. A focused search could determine whether an independent technical comparison has adjudicated these issues.

**Next Search**

> independent benchmark monoprop Q-CTRL IBM 60-site Fermi-Hubbard 10 seconds accuracy observables end-to-end

---

# Iteration 9

## 1. Search

**Query**

> independent benchmark monoprop Q-CTRL IBM 60-site Fermi-Hubbard 10 seconds accuracy observables end-to-end

**Why this query**

The new source materially strengthens the evidence that the headline Q-CTRL advantage is baseline-sensitive, but it does not resolve the key apples-to-apples questions: output scope, accuracy, validation, total workflow time, and independent replication. A focused search could determine whether an independent technical comparison has adjudicated these issues.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S29 — Fermi-Hubbard on a quantum computer, part 10: the official Monoprop benchmark - Edukaizen**
  URL: https://edukaizen.nl/fermi-hubbard-quantum-computer-part-11-official-monoprop-benchmark
- **S30 — Fast classical simulation of ‘Fast, accurate, high-resolution simulation of large-scale Fermi-Hubbard models on a digital quantum processor’**
  URL: https://arxiv.org/html/2608.13805
- **S31 — Performance Management - A Qiskit Function by Q-CTRL Fire Opal | IBM Quantum Documentation**
  URL: https://quantum.cloud.ibm.com/docs/en/guides/q-ctrl-performance-management

**Search Duration:** 3.58s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new benchmark provides a more demanding classical comparison than the earlier one-second demonstration and reports a 7.06-fold quantum runtime advantage on one narrowly defined observable under a local-execution metric.

**Confidence:** Medium

**Why this confidence level**

The benchmark specifies the observable, circuit, software version, timings, and approximation settings, but it is a project report rather than independent peer-reviewed adjudication and compares a quantum execution proxy with local classical wall-clock time.

**Evidence**

- For the 60-site, 120-mode, 30-step Fermi–Hubbard circuit and mean double occupancy across all 60 sites, EduKaizen reports 33.15 seconds for a local Fire Opal execution proxy versus 234.03 seconds for official Monoprop at a tighter cutoff. [S29]

#### Finding 2

**Claim**

The reported quantum advantage is sensitive to the chosen accuracy and approximation settings; the fastest classical result is less accurate, while the more accurate classical result is slower.

**Confidence:** High

**Why this confidence level**

The source supplies explicit timings, output values, and differences for multiple settings, directly demonstrating a time–accuracy tradeoff.

**Evidence**

- Monoprop takes 2.40 seconds at a loose threshold but differs from the MPS reference by about 0.04119; at a tighter threshold it takes 234.03 seconds and differs by about 0.01144. The EduKaizen Majorana result is closer to the MPS reference but takes 1,153.51 seconds. [S29]

#### Finding 3

**Claim**

The new result does not establish a matched-accuracy, end-to-end commercial quantum advantage.

**Confidence:** High

**Why this confidence level**

Multiple supplied sources identify concrete comparability problems, and S29 itself explicitly limits the conclusion to a local execution metric rather than an end-to-end advantage.

**Evidence**

- The quantum value is farther from the MPS reference than the official Monoprop value, the MPS calculation itself hit a configured bond cap, and the compared quantum number is an execution estimate rather than complete cloud time-to-answer. [S29]
- The source notes that the QPU figures exclude queueing and surrounding cloud workflow, while classical measurements are local wall-clock times; the Q-CTRL study also used a different shot budget and reports characterization-inclusive timing of 265 seconds rather than only 166 seconds of main-circuit QPU time. [S29]
- The accumulated classical-frontier evidence reports stronger classical baselines and unresolved questions about compilation, mitigation, postprocessing, validation, and full workflow accounting. [S20] [S23] [S26]

#### Finding 4

**Claim**

The appropriate interpretation of the Fermi–Hubbard evidence is a narrow, task- and observable-specific time–accuracy frontier, not general quantum superiority.

**Confidence:** High

**Why this confidence level**

The scope limitation is direct and consistent with the accumulated evidence.

**Evidence**

- S29 evaluates only mean double occupancy and states that the timing winner and accuracy winner differ; it characterizes the result as a specific runtime comparison with caveats rather than a general claim. [S29]
- Prior evidence shows that other classical methods can reduce the original 3,000-fold claim substantially and that output scope and validation requirements change the comparison. [S20] [S23] [S26]

#### Finding 5

**Claim**

Fire Opal’s documented role is error suppression and reduced sampling or execution burden on noisy hardware, but the documentation does not demonstrate commercial quantum advantage.

**Confidence:** High

**Why this confidence level**

The source directly documents the software’s claimed function and benchmark scope, but those claims are vendor documentation and do not establish commercial superiority.

**Evidence**

- IBM describes Fire Opal as applying automated AI-driven gate- and pulse-level error-suppression techniques and claims reduced shots and compute time; it also states that classical processing time remains a factor in total time. [S31]
- The listed benchmarks concern algorithmic accuracy and runtime on selected circuits, while the documentation does not provide an independent end-to-end business comparison against classical alternatives. [S31]

#### Finding 6

**Claim**

The overall assessment is unchanged: no broad, independently validated, commercially useful quantum advantage has been demonstrated in the supplied evidence, although the Fermi–Hubbard experiment remains a serious candidate for a narrow execution-time advantage under selected conditions.

**Confidence:** High

**Why this confidence level**

The new evidence adds a concrete benchmark but preserves the previously identified limitations and does not broaden the demonstrated scope.

**Evidence**

- S29 reports a 7.06-fold advantage over official Monoprop only for a local execution proxy, while also showing lower quantum accuracy relative to the cited MPS reference and non-equivalent timing definitions. [S29]
- Earlier evidence finds no independent replication, complete economic comparison, or demonstrated industrial deployment producing measurable business value; classical methods remain an active and improving comparator. [S6] [S20] [S23] [S26]

#### Finding 7

**Claim**

The biggest remaining technical and evaluation barriers remain error suppression/correction, scaling, and infrastructure overhead, supplemented by the need for fair benchmarking against rapidly improving classical algorithms.

**Confidence:** High

**Why this confidence level**

The barriers are consistently supported across technical, procurement, benchmark, and platform documentation.

**Evidence**

- Prior sources identify noise, decoherence, error correction, insufficient scale, and demanding operating conditions as persistent hardware barriers. [S3] [S5] [S6]
- S29 shows that coefficient thresholds, truncation, reference convergence, shot budgets, characterization, queueing, and workflow definitions materially affect the reported comparison. [S29]
- S31 states that Fire Opal still involves classical processing and presents runtime figures under particular shot assumptions, rather than removing all workflow costs. [S31]

### Conflicts Found

- S29 reports a 7.06-fold quantum advantage over official Monoprop on a local execution metric, while S20 reports that a stronger symmetry-enhanced GPU classical baseline reduces the original Q-CTRL comparison to approximately 36-fold and S26 reports a 10–15 second classical result for related dynamics. These figures are not directly comparable because observable scope, accuracy, hardware, implementation, and timing definitions differ. [S20] [S26] [S29]
- S29 characterizes the hardware as the runtime winner for mean double occupancy, but also reports that Monoprop is more accurate against the chosen MPS reference. Thus, the claim of advantage depends on prioritizing execution time over matched accuracy. [S29]
- Q-CTRL-associated reporting labels the experiment practical quantum advantage and positive ROI, whereas S29 limits the claim to a local execution proxy and explicitly says the comparison is not a perfectly interchangeable time-to-answer measure. This is a disagreement about evidentiary scope rather than necessarily about the recorded runtimes. [S7] [S11] [S29]

### Important Gaps

- Does official Monoprop reproduce the full 7,260-observable output claimed for the Q-CTRL study, or only mean double occupancy?
- Are the quantum and classical results matched for accuracy, sampling uncertainty, evolution interval, initialization, preprocessing, validation, and output scope?
- Does inclusion of compilation, calibration, readout mitigation, decay recovery, postprocessing, queueing, and cloud access costs eliminate or materially reduce the reported 7.06-fold execution advantage?
- How does official Monoprop compare with the newer symmetry-enhanced GPU calculation and monoprop results under identical hardware, accuracy, and output requirements?
- Has the benchmark been independently reproduced or peer reviewed by researchers without a commercial stake in the quantum or classical software?
- Does the Fermi–Hubbard benchmark produce a downstream materials-science or industrial R&D benefit rather than merely faster simulation of a model problem?
- What quantitative results and matched benchmark conditions are contained in S30? The supplied excerpt is incomplete and does not establish its conclusions.
- What fault-tolerant resource requirements are needed for commercially important workloads beyond this narrow benchmark?
- Do Fire Opal’s documented benchmark improvements persist under independently specified workloads and full economic accounting?

**Analysis Duration:** 20.28s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new source materially improves the narrow benchmark picture, but the central question still lacks independent, matched-accuracy, end-to-end evidence of commercial advantage. The most important remaining gap is a neutral or independent comparison of the complete Q-CTRL/IBM workflow against optimized classical methods on the same observables and accuracy target.

**Next Search**

> independent end-to-end benchmark Q-CTRL IBM Fermi-Hubbard Monoprop 7260 observables matched accuracy total time-to-solution

---

# Iteration 10

## 1. Search

**Query**

> independent end-to-end benchmark Q-CTRL IBM Fermi-Hubbard Monoprop 7260 observables matched accuracy total time-to-solution

**Why this query**

The new source materially improves the narrow benchmark picture, but the central question still lacks independent, matched-accuracy, end-to-end evidence of commercial advantage. The most important remaining gap is a neutral or independent comparison of the complete Q-CTRL/IBM workflow against optimized classical methods on the same observables and accuracy target.

**Results**

5 results retrieved.

2 new unique sources added.

### Sources

- **S32 — Q-CTRL announces a successful practical quantum ...**
  URL: https://runninginterference.substack.com/p/q-ctrl-announces-a-successful-practical
- **S33 — Fast, accurate, high-resolution simulation of large-scale ...**
  URL: https://arxiv.org/html/2605.04025v1

**Search Duration:** 3.66s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The Q-CTRL/IBM experiment is a technically substantial demonstration of pre-fault-tolerant quantum simulation, but not yet a demonstrated broad commercial advantage.

**Confidence:** High

**Why this confidence level**

The technical scope is directly documented in the paper, while the absence of an industrial deployment or broad workload demonstration is clear from the supplied material.

**Evidence**

- The paper reports a 120-qubit superconducting-processor simulation of the one-dimensional Fermi–Hubbard model, using up to 90 Trotter steps and error suppression. It reaches scales beyond exact statevector simulation and describes the task as challenging for tensor-network methods. [S33]
- The experiment is limited to a specific one-dimensional many-body-dynamics problem and does not demonstrate an industrial materials-discovery workflow, product, or measurable customer/business outcome. [S32] [S33]

#### Finding 2

**Claim**

The paper provides stronger evidence for a candidate narrow quantum-versus-classical runtime advantage than the earlier vendor announcements, but the headline 3,000-fold figure remains conditional and benchmark-dependent.

**Confidence:** Medium

**Why this confidence level**

S33 supplies detailed primary-source support for the reported comparison, but competing classical implementations and differing timing/output definitions prevent treating 3,000× as an established universal or end-to-end advantage.

**Evidence**

- At evolution times near the limit of quantum/classical agreement, the paper reports quantum-processor wall-clock runtime up to 3,000 times faster than an optimized TDVP simulation with bond dimension χ=4096. [S33]
- The comparison is made at the point where the quantum and approximate classical outputs agree with approximately 1% RMSE; beyond that region, the approaches diverge. Thus, the claim is tied to a particular model, evolution time, accuracy criterion, and classical algorithm. [S33]
- Independent or competing classical analyses in the accumulated evidence report much smaller advantages, including approximately 36-fold under a stronger GPU/symmetry-enhanced baseline and classical runtimes that can beat the quantum execution proxy for selected observables. [S20] [S23] [S26] [S29]

#### Finding 3

**Claim**

The experiment demonstrates useful scientific capability before fault tolerance, but not a general replacement for classical computing.

**Confidence:** High

**Why this confidence level**

The demonstrated scientific outputs and their narrow application scope are directly stated. Generalization to commercial workloads is not supported by the supplied evidence.

**Evidence**

- The processor observes spin-charge separation and extracts velocity ratios matching classical simulations across model parameters, and it produces quantitative outputs for a 60-site, 120-qubit instance. [S33]
- The reported results concern one-dimensional Fermi–Hubbard dynamics, where classical tensor-network methods remain an active and improving comparator; no evidence shows that the result generalizes to two- or three-dimensional materials or commercially important chemistry workloads. [S32] [S33] [S20] [S26]

#### Finding 4

**Claim**

The largest remaining barriers are reliable error correction, scaling useful logical computation, and fair end-to-end comparison with improving classical systems.

**Confidence:** High

**Why this confidence level**

These barriers are consistently supported by the primary paper and multiple accumulated technical comparisons.

**Evidence**

- The paper identifies hardware noise and machine size as limitations and relies on error suppression to obtain accurate results from a noisy superconducting processor. [S33]
- The reported quantum/classical agreement ends at a finite evolution time, with divergence afterward, illustrating the difficulty of verification and accuracy as dynamics become more complex. [S33]
- Classical methods using symmetry exploitation, GPUs, Majorana propagation, and open-source implementations materially change the apparent speedup, while prior analyses identify omitted or unequal costs such as compilation, calibration, mitigation, readout processing, postprocessing, convergence studies, queueing, and cloud access. [S20] [S23] [S26] [S29]
- The experiment is one-dimensional, leaving the harder question of scaling to two- and three-dimensional materials systems unresolved. [S32]

#### Finding 5

**Claim**

The most responsible overall assessment is that commercially useful quantum advantage has not yet been broadly demonstrated; quantum computing is at the stage of serious, narrow application experiments and benchmark-specific candidate advantages.

**Confidence:** High

**Why this confidence level**

The conclusion incorporates the new primary-source evidence while preserving unresolved validation, benchmarking, generalization, and economic gaps.

**Evidence**

- S33 strengthens the case that a contemporary quantum processor can perform a scientifically meaningful, large-scale simulation with competitive runtime under selected conditions. [S33]
- The supplied record still lacks independent replication, a fully matched end-to-end time-to-answer comparison, complete cost accounting, and evidence of downstream industrial or financial value. Competing classical baselines substantially narrow or potentially reverse the claimed advantage depending on observable and accuracy target. [S6] [S20] [S23] [S26] [S29] [S32]

### Conflicts Found

- S33 reports up to a 3,000-fold quantum runtime advantage over χ=4096 TDVP, while S20 reports approximately 36-fold against a stronger comparable-bond-dimension classical implementation, and S26/S29 report classical results that can approach or outperform the quantum execution proxy for narrower observables. These are not necessarily direct contradictions because the methods, hardware, output scope, accuracy, and timing conventions differ, but they show that the headline advantage is highly baseline-sensitive. [S20] [S26] [S29] [S33]
- The paper describes the quantum processor as competitive in a regime where tensor-network methods become prohibitively expensive, whereas S20 argues that a stronger symmetry- and GPU-enhanced classical calculation can extend beyond the quantum experiment and certify the previously difficult interval. The supplied evidence does not independently adjudicate the competing implementations. [S20] [S33]
- S32 notes that Q-CTRL’s comparison is made at the last point of classical/quantum agreement and raises verification and dimensional-scaling concerns. Therefore, the reported speedup does not establish correctness at larger evolution times or demonstrate a smooth path to commercially important two- or three-dimensional materials problems. [S32] [S33]

### Important Gaps

- Has the S33 result been independently replicated, peer reviewed, or benchmarked by researchers without a commercial stake in Q-CTRL or IBM?
- Does the reported quantum wall-clock time include compilation, calibration, repetitions, readout/error processing, postprocessing, and all classical work required to produce the compared observables?
- Are the quantum and TDVP results matched for the full observable set, sampling uncertainty, initialization, accuracy target, and validation procedure?
- Does the result produce a downstream materials-science or industrial R&D benefit rather than only a faster simulation of a one-dimensional model?
- How does the result compare under identical conditions with the strongest symmetry-enhanced GPU, Majorana, and monoprop classical implementations?
- What fault-tolerant logical-qubit counts, physical-qubit overheads, error rates, and runtimes would be required for commercially important chemistry and materials workloads?

**Analysis Duration:** 18.74s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The new primary paper materially improves the technical evidence for a narrow, pre-fault-tolerant simulation advantage, but it does not resolve the decisive questions for commercial usefulness: independent validation, apples-to-apples end-to-end benchmarking, economic value, and generalization beyond a one-dimensional benchmark. Further searches could add detail, but the supplied evidence is already sufficient for a responsible answer and another query is unlikely to change the central assessment without an independent replication or complete benchmark.

**Stop Reason:** sufficient_evidence

---

# Final Research Decision

**Research Stopped Because**

The analyzer determined that the important parts of the question could be answered responsibly.

**Stop Reason:** sufficient_evidence

**Searches Performed:** 10

**Unique Sources:** 33

**Remaining Uncertainty**

- An independent, matched benchmark of the Q-CTRL/IBM workflow against the strongest classical methods using the same observables, accuracy target, sampling uncertainty, initialization, and evolution interval.
- A complete end-to-end time-to-answer comparison including compilation, calibration, queueing, repetitions, error suppression or mitigation, readout correction, postprocessing, classical preprocessing, and convergence validation.
- A determination of whether the competing classical implementations reproduce the full output set reported for the quantum experiment or only selected observables.
- Evidence that the Fermi–Hubbard result produces downstream materials-science or industrial R&D value rather than only faster simulation of a model problem.
- Independent replication or peer review of both the Q-CTRL experiment and the principal classical rebenchmarks.
- Quantitative fault-tolerant resource estimates—logical qubits, physical-qubit overhead, error rates, and runtime—for commercially important chemistry, materials, optimization, or other workloads.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 10 | 46.89s |
| OpenAI Analysis | 10 | 169.84s |
| Report Generation | 1 | 23.11s |
| Total Run | — | 239.84s |
