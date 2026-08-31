# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** quantum-commercial-advantage

**System Version:** evidence-ledger-v1

**Model:** gpt-5.6-luna

## Summary

- Overall: 72.6 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.64
- Coverage: 0.66
- Depth: 0.60
- Citation quality: 0.80
- Citation validity: 1.00
- Citation support: 0.67
- Citation completeness: 0.95
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report supplies a useful basic distinction between computational and commercial advantage and mentions projections, but it lacks the required time boundary and a complete, explicit category framework.
- Candidate evidence:
  - The report distinguishes computational advantage from commercially useful or economic advantage: “Quantum computers have demonstrated computational performance advantages... but... [not] commercially useful advantages.”
  - It defines commercial usefulness using “runtime,” “accuracy,” “affordability,” and a “comparably priced classical alternative.”
  - It distinguishes present demonstrations from “projected” fault-tolerant advantages and mentions theoretical or exponential algorithmic gains.
- Missing:
  - No explicit evidence date or cutoff period is stated, despite citing a 2026 source.
  - The four required categories are not cleanly and explicitly defined: experimentally demonstrated advantage, end-to-end commercial advantage, theoretical algorithmic advantage, and hardware-dependent projected advantage.
  - The report does not systematically define comparison metrics such as throughput, reliability, total cost, availability, or solution quality for each category.

### R2

- Coverage: 0.75
- Depth: 0.50
- Rationale: Several representative claims are identified and appropriately differentiated, but the experimental descriptions and classical comparisons are too thin for deep evaluation.
- Candidate evidence:
  - It discusses Google’s 2019 supremacy experiment and notes that it involved a problem “lacking commercial or practical relevance.” [S2]
  - It discusses a 120-qubit materials simulation reported as taking about two minutes versus more than 100 hours classically. [S6][S7]
  - It discusses Q-CTRL’s claimed 3,000-times wall-clock speedup for a fermionic materials simulation and identifies that it was reported by a company rather than independently confirmed. [S8]
  - It distinguishes specially constructed benchmarks from potentially useful materials workloads and says the evidence does not establish general or commercial superiority.
- Missing:
  - The Google experiment is not described with sufficient platform, task, classical-comparison, or limitation detail.
  - The materials demonstrations lack important technical particulars, including the exact algorithm and output, accuracy validation, baseline hardware/software, and whether the quoted times are comparable end-to-end.
  - The report does not discuss independent classical red-team results or subsequent improved classical methods in detail; it only flags them as a concern.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is one of the stronger sections: it applies an appropriate commercial standard and identifies major weaknesses in the only prominent current claim. It stops short of a detailed end-to-end audit.
- Candidate evidence:
  - The conclusion says quantum computers are “not yet established as broadly commercially superior to classical computers.”
  - The Q-CTRL/IBM materials result is explicitly treated as a “disputed, workload-specific claim rather than an established conclusion.”
  - The report identifies missing checks for “end-to-end runtime, total cost, preprocessing, verification, reproducibility,” comparator optimality, and improved classical algorithms or GPU acceleration. [S6][S7][S8]
  - It states that commercial usefulness requires a relevant problem, useful speed and accuracy, affordability, and comparison with a best or comparably priced classical alternative.
- Missing:
  - It does not independently determine whether any economically meaningful workload has actually passed the required end-to-end test; it mainly says the evidence is insufficient.
  - State preparation, repeated runs, probabilistic measurement, system availability, and postprocessing are mentioned only in the Remaining Gaps section, not analyzed for the central claim.
  - Operating cost, energy, access/queueing, and availability are not quantitatively or concretely assessed.

### R4

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report correctly labels roadmaps and conditional forecasts as projections, but gives little substantive account of the underlying algorithms, assumptions, or resource requirements.
- Candidate evidence:
  - The report labels a 2,000-logical-qubit machine and 2033 competitive impact as a “projection” conditional on fault-tolerant hardware. [S5]
  - It identifies molecular, materials, and physical-system simulation as projected use cases and says these require large error-corrected workloads. [S4][S5]
  - It mentions “exponential algorithmic gains” and large datasets as reasons some problems might benefit. [S4]
- Missing:
  - It does not explain important algorithmic advantages in complexity terms, such as the assumptions and scaling behind factoring, quantum simulation, amplitude estimation, or optimization proposals.
  - It does not provide resource estimates for circuits, logical depth, physical-qubit overhead, error rates, data loading, or measurement repetitions.
  - The practical conditions that could erase end-to-end gains are mostly listed as gaps rather than analyzed for each candidate area.
  - The distinction between theoretical algorithmic results and hardware-dependent projections is asserted but not systematically developed.

### R5

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report identifies plausible early areas and weaker candidates, but the application comparison is broad and largely citation-driven rather than analytical.
- Candidate evidence:
  - It identifies molecular, materials, and physical-system simulation as the leading projected areas.
  - It mentions drug discovery, optimization, Hamiltonian simulation, partial differential equations, and machine learning as possible research or value areas. [S4][S9]
  - It says no demonstrated advantage is identified for supply-chain optimization, machine learning, or derivatives pricing. [S5]
  - It contrasts specialized large-scale problems with ordinary business workloads, which are “generally not expected to benefit.”
- Missing:
  - The areas are not compared systematically on theoretical promise, scientific usefulness, and commercial value.
  - Chemistry/materials simulation is not explained in terms of why quantum evidence is stronger there than in optimization, finance, or machine learning.
  - Cryptography is omitted, and scientific computing, finance, optimization, and machine learning receive only brief mentions.
  - The report does not assess data-loading, validation, accuracy, or workflow-integration barriers separately by application.

### R6

- Coverage: 0.75
- Depth: 0.50
- Rationale: The central barriers are correctly identified and tied somewhat to useful workloads, but the required technical prioritization and architecture-specific analysis are incomplete.
- Candidate evidence:
  - It identifies noise, errors, decoherence, insufficient hardware scale, and immature fault tolerance/error correction as the largest barriers.
  - It explains that qubits are sensitive to temperature, electromagnetic interference, and vibrations and that decoherence disrupts computation. [S3]
  - It links useful projected workloads to “thousands of logical qubits” and large error-corrected computations. [S4][S5]
  - It notes that the current materials result required error-suppression software, showing that noise affects useful accuracy rather than only benchmark specifications.
- Missing:
  - Error-correction overhead, logical error rates, sustained logical circuit depth, decoding, correlated errors, connectivity/routing, and control are not explained.
  - Fabrication/material variability and architecture-specific constraints such as cryogenics or photon loss are absent.
  - The report does not prioritize barriers beyond a general list or distinguish clearly between barriers common to all platforms and platform-specific ones.
  - It does not connect each barrier quantitatively or concretely to the requirements of commercial workloads.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report is appropriately cautious and directly discusses conflicts and source limitations, especially for the vendor claim. Its evidence-quality audit is not comprehensive or source-authoritative enough for full credit.
- Candidate evidence:
  - The report identifies the Q-CTRL result as company-reported and lacking independent validation. [S8]
  - It explicitly notes missing independent validation of comparator optimality, reproducibility, end-to-end metrics, and durability against improved classical methods.
  - It records conflicting evidence between present-day vendor claims and 2033–2035 projections and explains that the disagreement may reflect different workloads and definitions.
  - It uses confidence labels of Medium, Low, and High and qualifies the negative conclusion as being based on supplied evidence.
- Missing:
  - The sources are not systematically classified into primary experiments, independent replications, critiques, theoretical work, vendor claims, and roadmaps.
  - The source base relies substantially on vendor, trade-publication, Wikipedia, and general explainer material; authoritative peer-reviewed or independent primary evidence is limited.
  - No concrete independent replication or classical red-team analysis is cited; these are primarily identified as missing.
  - The report does not assess the reliability of the 2033–2035 projections beyond saying they are uncertain.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report provides a well-calibrated overall conclusion and concrete categories of needed evidence. It could synthesize the milestones and present maturity more sharply.
- Candidate evidence:
  - The conclusion gives a calibrated judgment: quantum computers are “not yet established as broadly commercially superior,” while a disputed materials claim is treated as promising but unconfirmed.
  - It synthesizes demonstrated, projected, and barrier evidence and says meaningful benefits may emerge conditionally in molecular, materials, and related simulations.
  - It avoids a single precise date and states that timing is workload-specific, with conditional 2033 and 2035-or-later estimates.
  - The Remaining Gaps section identifies measurable evidence that would change the assessment, including independent testing, end-to-end runtime, accuracy, cost, preprocessing, verification, physical/logical resource requirements, and reproducibility.
- Missing:
  - The answer to “how close” remains somewhat qualitative and does not clearly distinguish current demonstrated status from the distance to fault-tolerant commercial deployment using a milestone ladder.
  - The proposed milestones are mostly framed as missing evidence rather than prioritized go/no-go thresholds.
  - The conclusion does not clearly state which specific milestone—such as a reproducible end-to-end workload advantage against a best classical baseline or a demonstrated logical-qubit scale—would most materially change the judgment.

### Novel Value

- No material benchmark-external value identified.

## Citations

### Support

#### F1: PARTIALLY_SUPPORTED

- Claim: Quantum computers have demonstrated computational performance advantages on specially constructed benchmark problems, but the supplied evidence does not establish that these demonstrations provide commercially useful advantages over classical computers.
- Sources: S2, S6, S7, S8
- Rationale: The sources support a demonstrated quantum speed advantage on a specific materials-science simulation involving a 120-qubit Fermi–Hubbard model, compared with a stated classical software baseline (two minutes versus more than 100 hours). However, they characterize the problem as commercially relevant or practically useful and explicitly describe the result as evidence of practical quantum advantage and positive ROI. Thus, the evidence does not support the claim’s assertion that commercial usefulness has not been established. Also, the sources describe a specific materials-science application rather than generally “specially constructed benchmark problems.”
- Supporting text: S6/S8 report that the quantum algorithm ran in two minutes versus over 100 hours for the classical tools, on a materials-science problem described as commercially relevant and practically useful. S2 calls Google’s earlier problem commercially irrelevant, but distinguishes it from Q-CTRL’s claimed real-world practical advantage.

#### F2: PARTIALLY_SUPPORTED

- Claim: The strongest present-day evidence for commercial usefulness is a disputed, workload-specific claim rather than an established conclusion.
- Sources: S2, S6, S7, S8
- Rationale: The sources support that the evidence is centered on a specific materials-science workload and is presented as a claim or demonstration by Q-CTRL, rather than as broad evidence across commercial applications. However, the supplied text does not explicitly show that the claim is disputed: the independent reports largely repeat or endorse Q-CTRL’s characterization, while S7 mentions only possible future classical-algorithm or GPU improvements. Nor do the sources establish that this is definitively the strongest present-day evidence.
- Supporting text: S2 defines practical quantum advantage in terms of a real-world application and describes Q-CTRL’s Fermionic Simulation demonstration. S6–S8 report a claimed 3,000× speedup for a specific materials-science problem; S8 labels it “evidence of practical quantum advantage,” while S7 notes that future classical-algorithm improvements or GPU acceleration could affect the comparison.

#### F3: SUPPORTED

- Claim: A commercially meaningful quantum advantage should be judged more strictly than an abstract algorithmic or computational advantage: it requires useful performance against a comparably priced or best available classical alternative on a relevant problem.
- Sources: S4, S2
- Rationale: S4 distinguishes abstract quantum advantage from “quantum economic advantage,” defined by outperforming a comparably priced classical computer. S2 similarly contrasts computational supremacy and theoretically framed absolute advantage with practical advantage, which requires outperforming the best available conventional alternative on a real-world problem of known commercial or scientific relevance and delivering useful, faster, or more affordable results. Together, the sources support the claim’s important factual content.
- Supporting text: S4: “quantum economic advantage” occurs when a problem is solved more quickly with a comparably priced classical computer. S2: Practical Quantum Advantage means outperforming the best available conventional alternative in a real-world application of known relevance, enabling users to solve meaningful problems better, faster, or more affordably.

#### F4: SUPPORTED

- Claim: Potential advantages are expected to be concentrated in selected large-scale problems—especially molecular, materials, and physical-system simulation—rather than applying broadly to ordinary business workloads.
- Sources: S4, S5, S9
- Rationale: S4 explicitly states that typical small- to moderate-sized business problems will not benefit, while large problems with exponential algorithmic gains or very large datasets may benefit. S5 describes the advantage map as narrow and concentrated, highlights molecular, materials, and physical-system simulation, and contrasts these with ordinary workloads such as supply-chain optimization, machine learning, and derivatives pricing. S9 further identifies Hamiltonian simulation of quantum systems and difficult physical problems as key research areas. Together, the sources support the claim's central distinction, although S9 also lists other potential application areas.
- Supporting text: S4: “small to moderate-sized problems, the most common types for typical businesses, will not benefit,” whereas large problems may derive advantages. S5: “The quantum advantage map is narrow, uneven, and concentrated,” with particular strength in simulating “molecules, materials, and physical systems”; it says demonstrated advantage does not extend to supply chains, machine learning pipelines, or derivatives pricing. S9: Hamiltonian simulation enables study of “quantum systems,” including ground-state energies and time dynamics.

#### F5: PARTIALLY_SUPPORTED

- Claim: The largest remaining technical barriers are noise and errors, decoherence, insufficient hardware scale, and immature fault-tolerance and error-correction infrastructure.
- Sources: S2, S3, S4, S5, S6, S7, S8
- Rationale: The snapshots clearly support noise and errors as major technical barriers, and they support hardware-size/scaling limitations. S3 also supports decoherence as a problem caused by environmental sensitivity. However, the sources do not meaningfully establish that fault-tolerance and error-correction infrastructure is immature as a distinct barrier, nor do they substantiate the superlative framing that these are the “largest” remaining barriers. Several cited sources instead describe error-suppression software and projected fault-tolerant capabilities without directly assessing their maturity.
- Supporting text: S2: quantum computers face challenges from “the size of the hardware required” and “errors that degrade performance”; it also says systems have been “limited by noise and errors.” S3: temperature, electromagnetic interference, and vibrations can cause “decoherence.” S4: the hardware and software for the most complex problems may not be available until 2035 or later.

#### F6: PARTIALLY_SUPPORTED

- Claim: The timing of commercially useful quantum computing remains uncertain and workload-specific; the ledger does not support a single reliable timetable.
- Sources: S4, S5, S2, S6, S7, S8
- Rationale: The sources strongly support the workload-specific part: MIT says quantum computing will not be better for everything, but only for some problems, and S5 describes advantages as depending entirely on the business and being narrow and uneven. However, the sources do not consistently support the claim that timing remains uncertain or that no reliable timetable exists. S4 gives differing estimates (quantum advantage by 2030 versus complex-problem hardware and software in 2035 or later), which indicates uncertainty, but S2, S6, S7, and S8 present a claimed practical commercial advantage already demonstrated in 2026 and cite near-term or current utility. Thus, the evidence supports a narrower conclusion that commercial usefulness is workload-specific and that forecasts vary, rather than the full claim as stated.
- Supporting text: S4: “The current field of quantum computers isn’t quite ready for prime time” and estimates the most complex capabilities may not be available until “2035 or later,” while some estimate quantum advantage “by 2030.” S4 also says, “Quantum computing is not going to be better for everything, just for some things.” S5 says the answer “depends entirely on what your business does” and that the advantage map is “narrow, uneven.”

### Missing Citations

- Q17: The report concludes that quantum computers are not yet established as broadly commercially superior to classical computers.

## Deterministic Checks

- `run_metadata_loads`: PASS
- `report_exists`: PASS
- `sources_present`: PASS
- `structured_report_parses`: PASS
- `report_question_matches`: PASS
- `source_ids_unique`: PASS
- `source_ids_syntactically_valid`: PASS
- `source_urls_present`: PASS
- `evidence_objects_valid`: PASS
- `confidence_values_valid`: PASS
- `citation_ids_syntactically_valid`: PASS
- `citation_ids_resolve`: PASS
- `structured_claim_evidence_available`: PASS
- `ledger_claim_ids_unique`: PASS
- `ledger_evidence_relationships_resolve`: PASS
- `ledger_confidence_values_valid`: PASS
- `ledger_evidence_ids_unique`: NOT_EVALUABLE — Current ledger relations have no independent evidence-ID field.

## Main Weaknesses

1. R1: Set a time boundary and define the categories used to answer the question.
2. R4: Separate theoretical algorithmic advantages from hardware-dependent projections.
3. R2: Evaluate representative experimental claims of quantum advantage against classical computation.
4. 4 cited finding(s) were not fully supported by saved evidence.
5. 1 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ae3a5680c375b6650be217402137fd59a302eee5fb85b0bc360a9292a5734293`
- Candidate report hash: `64f4d72255f7e1016b27b8c03b94d932fd6848c1205da78c5294af547adcd87a`
- LLM calls: 8
- Evaluated at: 2026-08-31T21:52:30.164499+00:00
