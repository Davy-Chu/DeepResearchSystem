# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** multi-agent-llm-landscape

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 77.0 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.68
- Coverage: 0.68
- Depth: 0.66
- Citation quality: 0.88
- Citation validity: 1.00
- Citation support: 0.85
- Citation completeness: 0.87
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report recognizes that scope is multidimensional and includes a baseline, but it does not establish the requested operational boundary or address the specified adjacent configurations.
- Candidate evidence:
  - The report says the map includes “a single-agent baseline; independent multi-agent execution; centralized supervisor-worker coordination; decentralized peer-to-peer coordination; and hybrid systems.”
  - It states that the landscape should be “multidimensional” and “compositional” rather than one authoritative taxonomy.
- Missing:
  - No explicit operational inclusion or exclusion criteria are provided.
  - Single-agent tool use, prompt chains, multiple roles instantiated by one model, classical non-LLM multi-agent systems, and hybrid LLM/non-LLM designs are not separately handled.
  - Borderline cases are not defined consistently; the single-agent baseline is included in the graph but not clearly distinguished from systems in scope.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is a strong landscape sketch with materially distinct topologies and compositional overlays, but it does not provide a full per-pattern architectural characterization.
- Candidate evidence:
  - The report identifies five core topologies: “single-agent, independent multi-agent, centralized, decentralized, and hybrid systems.”
  - It further identifies plan-and-execute, supervisor-worker, role specialization, team organization, debate, verifier-critic, ensemble selection, relay workflows, and graph/state-machine orchestration.
  - The graph labels independent systems as parallel with no communication, centralized systems as supervisor-to-workers-to-merge, decentralized systems as peer-to-peer/debate/consensus, and hybrid systems as hierarchy plus lateral communication.
  - It gives limitations including “information loss, context fragmentation, latency, cost, and error propagation,” and discusses task-dependent suitability such as decomposable financial analysis, exploration, and sequential planning.
- Missing:
  - The patterns are not characterized systematically across all requested dimensions: control structure, agent arrangement, information flow, coordination mechanism, representative applications, and limitations.
  - Applications are mentioned unevenly and many patterns lack concrete representative systems or use cases.
  - Some organizational patterns are listed as overlays without explaining how their control and information flows differ in practice.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report offers substantial cross-cutting analysis, especially around topology, parallelism, communication, and overhead, but leaves important dimensions and their consequences underdeveloped.
- Candidate evidence:
  - The report explicitly separates dimensions including “control topology,” communication paradigm, protocol, task regime, and resource conditions.
  - It discusses centralized versus decentralized coordination, parallel versus sequential work, context fragmentation, synchronization overhead, semantic drift, lossy handoffs, redundancy, and error amplification.
  - It states that coordination may help when work is “decomposable, parallelizable, context-limited, or benefits from diverse perspectives,” while introducing overhead and consistency problems.
  - The graph and open-problem list include shared memory, session state, discovery, context preservation, and dynamic architecture selection.
- Missing:
  - Several rubric dimensions are not explicitly analyzed: hierarchical versus peer coordination as a general axis, synchronous versus asynchronous execution, message passing versus shared state as a direct comparison, context isolation versus sharing, and static versus dynamic agent allocation.
  - Consequences for independence, consistency, and scalability are discussed only partially and are not systematically tied to each design choice.
  - The report mostly enumerates dimensions and mechanisms rather than comparing their effects across architectures.

### R4

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report has broad component coverage and one concrete workflow, but the requested compositional and essential-versus-optional analysis is largely implicit.
- Candidate evidence:
  - The report names planners, specialized workers, skepticism and critics, gap analysis, citation auditing, synthesis, refinement, tools, shared memory, human review, bounded iteration, and graph/state-machine orchestration.
  - Its deep-research example combines “scouting, planning, parallel specialists, skepticism, gap analysis, citation auditing, synthesis, refinement, and bounded iteration.”
  - The graph presents planning, specialization, debate, verifier-critic, ensemble, relay, shared memory, graph/state machine, and human review as composable overlays.
- Missing:
  - The roles and mechanisms are not explained in enough detail to show how they combine with each topology.
  - Synthesizers, retrieval, memory/shared state, tools, and evidence/provenance tracking are mostly named rather than operationally analyzed.
  - The report does not clearly distinguish essential architectural features from optional overlays or implementation choices; for example, verification, shared memory, human review, and bounded iteration are grouped together without that distinction.

### R5

- Coverage: 1.00
- Depth: 1.00
- Rationale: The visualization is legible, labeled, self-contained enough to interpret, and expresses alternatives, composition, layers, and cross-cutting open problems rather than being an unstructured list.
- Candidate evidence:
  - The conclusion provides a labeled ASCII design graph with separate layers for evaluation/resources, core control topology, composable overlays, communication, and application streams.
  - The graph explicitly shows the single-agent baseline, independent/centralized/decentralized alternatives, hybrid composition, and overlays such as planning, debate, verification, shared memory, and graph execution.
  - The prose explains that the landscape is “best represented as a layered design graph” and that overlays are “composable with any topology.”
  - The report notes a classification limitation by stating that a “multidimensional, compositional map” is preferable to one mutually exclusive taxonomy.
- Missing:

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: The comparative reasoning is notably conditional and includes budget normalization, but empirical detail and evidence qualification are insufficient for full credit.
- Candidate evidence:
  - The report makes the conditional synthesis that multi-agent systems help for decomposable, parallelizable, context-limited, or diversity-dependent work but can incur fragmentation, latency, cost, and error propagation.
  - It reports matched-thinking-token findings in which single-agent systems matched or outperformed multi-agent variants on FRAMES and four-hop MuSiQue, contrasted with broader scaling results showing architecture-by-task interactions and gains for decomposable financial reasoning.
  - It identifies evaluation controls including model, reasoning tokens, context tokens, tool calls, latency, monetary cost, parallel hardware, and safety conditions.
  - It explicitly avoids universal rankings, saying centralized, decentralized, and hybrid systems are conditionally useful and that “neither is established as a general winner.”
- Missing:
  - The quantitative claims do not consistently provide the full task, baseline, metric, and experimental context required by the rubric; for example, the “large gains,” “substantial degradation,” and “87%” claims lack detailed metric and baseline specification in the report.
  - Trade-offs involving fault tolerance, evidence sharing, monetary cost, and scalability are less developed than quality, coordination overhead, and latency.
  - The report sometimes relies on source clusters rather than distinguishing which findings are measured results, reported limitations, or design hypotheses.

### R7

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes important evaluation dimensions and system-level risks, but mitigation and detection guidance—the core of this requirement—is largely absent.
- Candidate evidence:
  - The report calls for final-outcome and process-level metrics including reliability, communication overhead, context fragmentation, redundancy, error amplification, and evidence traceability.
  - It identifies hallucination-like misinformation propagation, semantic error injection, collusion, prompt propagation, message manipulation, synchronization failures, and error amplification.
  - It says fair evaluation requires single-agent comparisons, matched budgets, normalized tokens, tool calls, latency, cost, and safety conditions.
  - It identifies open evaluation needs for collusion, correlated failures, premature consensus, adversarial propagation, privacy, policy enforcement, and governance.
- Missing:
  - The report does not link each major risk to concrete safeguards, monitoring procedures, or human-oversight mechanisms.
  - Contradiction handling, memory failures, runaway execution, tool misuse, and opacity are not substantively addressed despite being central rubric risks.
  - Evaluation of coordination behavior and factuality/evidence support is mentioned, but concrete protocols, ablations, failure detection methods, and appropriate baselines are not developed.
  - Risks are listed more than analyzed causally or operationally.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is a strong open-problem and sourcing section with identifiable references and explicit uncertainty, but source quality qualification and problem-by-problem research framing are incomplete.
- Candidate evidence:
  - The “Remaining Gaps” section lists specific problems involving authoritative study reconciliation, cross-domain evaluation, jointly normalized budgets, causal testing of centralized verification, predictive process metrics, context preservation, communication protocols, security, governance, training, and interoperability.
  - The report explains why several gaps matter, for example by linking them to fair architecture selection, generalization, semantic drift, privacy, cost, and reliability.
  - Sources are identifiable through numbered references with titles and URLs, including a scaling study, communication survey, adversarial robustness study, and equal-budget reasoning study.
  - The report distinguishes confidence levels and explicitly flags unresolved study-version discrepancies, uncertain generality, and differences between primary-style and secondary evidence.
- Missing:
  - Many source entries are secondary, informal, practitioner, or future-dated pages, and the report does not consistently qualify their evidentiary status beyond a few caveats.
  - Open problems are often presented as a list of experiments rather than organized into clearly defined unresolved questions with mechanisms, hypotheses, and success criteria.
  - The report does not substantively cover some possible open-problem areas such as interoperability standards, adaptive resource allocation, persistent memory, and learning/adaptation beyond brief mentions.
  - The cited quantitative findings are not independently contextualized with complete benchmark, baseline, metric, and experimental details.

### Novel Value

- The report's layered design graph usefully separates core control topologies from composable organizational overlays, communication protocols, application streams, and evaluation/resource conditions.
- It synthesizes the landscape conditionally rather than asserting that either single-agent or multi-agent systems universally dominate.
- It explicitly surfaces conflicts between matched-budget reasoning results and broader agentic scaling results, including unresolved study-version discrepancies and cross-domain generalization gaps.

## Citations

### Support

#### F1: PARTIALLY_SUPPORTED

- Claim: A compositional design graph is better supported than a single hierarchical taxonomy for representing multi-agent LLM systems.
- Sources: S1, S3, S7, S8, S9, S11, S14, S23, S28
- Rationale: The sources support representing multi-agent systems through composable graphs, multiple architectural dimensions, and task-dependent topologies. They also describe hierarchical/supervisor-worker systems as useful patterns. However, none directly establishes that a compositional design graph is superior to a single hierarchical taxonomy; several sources instead emphasize that architecture effectiveness depends on task structure and coordination regime.
- Supporting text: S1 states that production systems are often “compositions of two or three” canonical patterns and treats hierarchical and graph topologies as distinct multi-agent patterns. S8 says graph-based workflows provide “maximum flexibility for complex processes,” while S23/S28 report that architecture-task alignment determines success and that mismatched coordination can degrade performance.

#### F2: SUPPORTED

- Claim: The core architecture graph should include five comparison nodes: single-agent, independent multi-agent, centralized, decentralized, and hybrid systems.
- Sources: S28, S29, S30, S1, S2, S3, S8, S12, S18
- Rationale: S28, S29, and S30 explicitly identify five canonical architectures consisting of one single-agent system and four multi-agent variants: independent, centralized, decentralized, and hybrid. The remaining sources discuss related architecture taxonomies but do not undermine this five-node comparison.
- Supporting text: S30: “We evaluated five canonical architectures: one single-agent system (SAS) and four multi-agent variants (independent, centralized, decentralized, and hybrid).”

#### F3: PARTIALLY_SUPPORTED

- Claim: Major organizational and execution patterns are composable overlays on the five core topologies.
- Sources: S1, S3, S8, S12, S18
- Rationale: The sources support that agent systems use multiple architectural, organizational, and execution patterns, and that these can be combined or implemented in different topologies. However, they do not establish the specific framework that there are exactly five “core topologies” with major organizational and execution patterns functioning as composable overlays on them. S1 instead describes eight canonical patterns across four quadrants, while S8 and S12 present alternative categorizations.
- Supporting text: S1: “most production agent systems are compositions of two or three from across those quadrants” and “New agent designs almost always reduce to a composition of these eight.” S8 describes centralized, decentralized, hierarchical, network, assembly-line, role-based, and graph-based structures. S12 says architectures can be categorized into five patterns: “flat, hierarchical, team-based, central coordinator, hybrid.”

#### F4: SUPPORTED

- Claim: Agentic task regime should be a first-class taxonomy axis, distinct from static reasoning benchmarks.
- Sources: S23, S28, S29, S30
- Rationale: The saved sources explicitly distinguish agentic tasks from traditional static benchmarks and define agentic tasks by sustained interaction, iterative information gathering under partial observability, and adaptive refinement from environmental feedback. They further state that this distinction changes evaluation and coordination behavior, supporting treating the agentic regime as a separate taxonomy dimension.
- Supporting text: S23: Agentic tasks are differentiated from “traditional static benchmarks” because they require sustained multi-step environmental interaction, iterative information gathering, and adaptive strategy refinement. S29/S30 similarly state that static benchmarks do not capture deployment complexity and explicitly define “agentic” evaluation separately.

#### F5: SUPPORTED

- Claim: Communication and coordination should be modeled as separate but interacting design dimensions.
- Sources: S7, S8, S9, S20
- Rationale: The saved sources support both components of the claim: communication and coordination are treated as distinct analytical or functional concepts, while also being described as related in multi-agent system design. S9 explicitly separates system-level communication from system-internal communication and identifies coordination workflows as critical; S8 distinguishes collaboration channels from orchestration platforms that manage coordination and communication. S20 states directly that communication (message passing) and coordination (strategic direction) are distinct, while noting that they can be intertwined in some architectures. S7 further supports modeling communication through multiple independent taxonomy dimensions, though it focuses more narrowly on communication protocols.
- Supporting text: S20: “The paper makes an important distinction between communication (message passing) and coordination (strategic direction of activities).” It also says that in decentralized systems they are “intertwined,” whereas architectures separating them scale more efficiently. S9 describes a framework covering communication while noting that communication and coordination workflows are both critical to collaboration. S8 distinguishes “collaboration channels” from “orchestration platforms” handling coordination and communication.

#### F6: SUPPORTED

- Claim: Communication protocols are an emerging infrastructure layer with interoperability trade-offs.
- Sources: S7
- Rationale: The source explicitly describes robust communication protocols as becoming essential infrastructure for distributed agent networks and identifies a fragmented protocol landscape as a significant interoperability challenge. It also discusses trade-offs among versatility, efficiency, and portability, supporting the claim’s trade-off component.
- Supporting text: The abstract states that communication protocols are “becoming essential infrastructure for distributed agent networks,” while the “fragmented protocol landscape presents a significant interoperability challenge.” It further says no single protocol is likely to maximize “versatility, efficiency, and portability simultaneously.”

#### F7: SUPPORTED

- Claim: Multi-agent systems do not provide a universal performance improvement; their value depends on task structure, context conditions, model capability, and resource accounting.
- Sources: S14, S15, S18, S23, S28, S29, S30
- Rationale: The saved sources collectively support the claim. S23, S28, S29, and S30 explicitly report that multi-agent performance varies with task structure, coordination strategy, model capability, and architecture, including large gains on decomposable/parallel tasks and substantial degradation on sequential or tool-heavy tasks. S14, S15, and S18 further show that apparent MAS advantages can disappear under equal thinking-token budgets, and that MAS becomes competitive when single-agent context utilization is degraded or when additional computation is used. Together, the sources support the non-universality and the stated dependencies, including resource accounting.
- Supporting text: S23/S28: relative performance ranges from +80.8% on decomposable financial reasoning to −70.0% on sequential planning; effectiveness depends on coordination-task alignment and model capability. S14/S15/S18: under matched thinking-token budgets, single agents often match or outperform MAS; MAS can benefit when context utilization is degraded or when more compute is expended. S29/S30: MAS is not a universal solution and may boost or degrade performance depending on configuration, task structure, and tool-coordination overhead.

#### F8: PARTIALLY_SUPPORTED

- Claim: Centralized coordination appears promising for decomposable work and verification, while decentralized coordination may be useful for exploration and diverse peer perspectives; neither is established as a general winner.
- Sources: S28, S29, S30, S20, S1, S2, S5, S8, S12
- Rationale: The saved sources directly support the centralized portion: centralized systems are described as strong for decomposable or parallelizable tasks and as providing orchestration, synthesis, and verification/error containment. They also support the non-universal conclusion: performance depends on task structure and coordination strategy, with multi-agent approaches sometimes degrading performance. However, the cited saved text does not clearly establish that decentralized coordination is specifically useful for exploration or diverse peer perspectives. S20 asserts this, but it is a secondary article’s characterization rather than corroborated evidence in the other supplied sources; S8 and S12 mainly describe flexibility, resilience, or peer collaboration, not demonstrated exploration benefits.
- Supporting text: S30: “On parallelizable tasks like financial reasoning… centralized coordination improved performance by 80.9%… [through] decompose[ing] complex problems into sub-tasks.” It also states that multi-agent systems “are not a universal solution” and can boost or degrade performance depending on configuration. S29 describes centralized coordination as a hub-and-spoke model that delegates and synthesizes outputs, while S20 characterizes decentralized systems as strongest on exploration tasks requiring diverse perspectives.

#### F9: SUPPORTED

- Claim: Coordination creates a capability-versus-overhead trade-off involving context fragmentation, lossy handoffs, synchronization cost, tool-use overhead, and error amplification.
- Sources: S1, S2, S9, S14, S23, S28, S29, S30
- Rationale: The saved sources directly support the overall trade-off and each major component. S1 states that collaborative multi-agent systems add coordination overhead in exchange for parallelism or specialization. S23 explicitly describes information fragmentation, lossy inter-agent compression, synchronization overhead, and cascading errors. S14 identifies communication bottlenecks and information loss under multi-agent decomposition. S28–S30 report disproportionate overhead on tool-heavy tasks and measure error amplification. S2 and S9 further discuss contextual drift, semantic loss, communication efficiency, and coordination challenges.
- Supporting text: S23: multi-agent systems incur a “coordination tax” because global context must be compressed into inter-agent messages; this “lossy communication increases synchronization overhead,” while errors cascade through execution chains. S30: as tasks require more tools, the “tax” of coordinating multiple agents increases disproportionately, and communication can fragment reasoning. S28–S29: architectures without centralized verification propagate errors more, with independent systems reported to amplify errors substantially.

#### F10: SUPPORTED

- Claim: Fair evaluation requires an explicit comparison contract and process-level metrics, not final accuracy alone.
- Sources: S11, S14, S23, S28, S29, S30
- Rationale: The sources directly support both key elements: S11 explicitly advocates a comparison contract specifying task, evidence, control, output, and evaluation dimensions. S23 states that existing evaluations often differ in prompts, tools, or computational budgets and focus exclusively on final accuracy without examining process dynamics. S14 further supports controlling computation and diagnosing evaluation artifacts. Together, they support the claim that fair evaluation requires explicit comparison protocols and process-level analysis beyond final accuracy.
- Supporting text: S11: The survey argues that systems should be compared through a “Search-Agent Comparison Contract” covering the task regime, evidence environment, control policy, output artifact, and evaluation contract. S23: evaluations may use different prompts, tools, and compute budgets, while focusing exclusively on final accuracy rather than process dynamics. S14: comparisons should be conducted under matched reasoning-token budgets and with attention to budgeting artifacts and benchmark vulnerabilities.

#### F11: SUPPORTED

- Claim: Security and reliability are system-level properties affected by interaction structure, not only by individual-agent quality.
- Sources: S10, S9
- Rationale: The sources directly state that multi-agent robustness depends on systemic interaction and coordination dynamics, not merely individual agent design. They also identify communication architecture, protocols, and interaction structure as central to system security and reliability.
- Supporting text: S10 states that “robustness depends not just on individual agent design, but also on the systemic dynamics of interaction and coordination,” and reports that robustness varies with communication order and structural complexity. S9 presents a communication-centric framework covering system-level architecture and protocols, and identifies security vulnerabilities and robust system design as communication-related challenges.

#### F12: PARTIALLY_SUPPORTED

- Claim: The principal open problem is determining when specialization or coordination beats a strong single-agent or compound-inference baseline on genuinely agentic tasks under jointly normalized budgets.
- Sources: S14, S18, S23, S28, S29, S30, S11
- Rationale: The sources strongly support that the key unresolved question concerns the conditions under which multi-agent specialization or coordination provides genuine benefits over strong single-agent baselines, especially on genuinely agentic tasks and with controlled or standardized compute. However, they do not establish that this is the singular or “principal” open problem, and they do not specifically substantiate the term “compound-inference baseline.” The sources also describe standardized compute or matched thinking-token budgets, but not a fully defined joint normalization of all relevant budgets.
- Supporting text: S23 states that the conditions under which multi-agent systems provide genuine benefits remain underexplored and that there is “no principled quantitative framework” for predicting when coordination improves performance versus adding costs. It defines agentic tasks through sustained environmental interaction, partial observability, and adaptive feedback. S14 reports that single agents match or outperform multi-agent systems under matched reasoning-token budgets and asks “when do MAS become competitive.” S23/S28/S29/S30 report that coordination gains depend on task structure, with benefits on decomposable/parallelizable tasks and degradation on sequential or tool-heavy tasks.

#### F13: SUPPORTED

- Claim: A quantitative scaling perspective is emerging in which coordination benefits diminish as baseline model capability rises and architecture selection can be predicted from task and system factors.
- Sources: S23, S28, S29, S30
- Rationale: The saved sources directly describe quantitative scaling principles and a predictive model relating performance to coordination, model capability, and measurable task/system factors. They also explicitly report diminishing coordination returns once single-agent baseline performance exceeds a threshold, and state that the framework identifies the best architecture for 87% of held-out or unseen configurations.
- Supporting text: S23/S28: the model captures performance variation with coordination, model capability, and system/task factors; coordination yields diminishing returns once single-agent baselines exceed certain performance; the best-performing architecture is identified for 87% of held-out configurations. S29/S30 likewise describe quantitative scaling principles, a predictive model for optimal architecture on 87% of unseen tasks, and a ceiling for the “more agents” approach.

### Missing Citations

- Q23: The report's visual taxonomy organizes evaluation/resource conditions, control topology, composable organizational overlays, communication, and application streams as separate layers.
- Q24: Single-agent systems are the necessary baseline, particularly for coherent reasoning under equal budgets.
- Q25: Centralized or hybrid systems are plausible choices when tasks decompose cleanly and verification is valuable, while decentralized systems may be appropriate when exploration or peer diversity is genuinely required.

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
- `structured_claim_evidence_available`: NOT_EVALUABLE — This run predates or does not use an evidence ledger.
- `ledger_claim_ids_unique`: NOT_EVALUABLE — Evidence ledger unavailable.
- `ledger_evidence_relationships_resolve`: NOT_EVALUABLE — Evidence ledger unavailable.
- `ledger_confidence_values_valid`: NOT_EVALUABLE — Evidence ledger unavailable.
- `ledger_evidence_ids_unique`: NOT_EVALUABLE — Evidence ledger unavailable.

## Main Weaknesses

1. R1: Define an operational scope for multi-agent LLM systems and distinguish included systems from adjacent configurations.
2. R7: Explain how multi-agent systems are evaluated and how their characteristic failure modes and risks can be detected or mitigated.
3. R4: Explain the principal agent roles and supporting mechanisms used to compose multi-agent systems.
4. 4 cited finding(s) were not fully supported by saved evidence.
5. 3 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `3ba296f97ad2c98be185e194bbae89b363b2bc81a38fd31abf5dbf056e9a34b0`
- Candidate report hash: `a4636b80618be0353813f6b30f678ac76789ba26d369ff253d6131f26d58d683`
- LLM calls: 15
- Evaluated at: 2026-09-01T08:28:12.488248+00:00
