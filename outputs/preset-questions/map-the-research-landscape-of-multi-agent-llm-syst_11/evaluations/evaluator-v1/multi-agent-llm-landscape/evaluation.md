# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** multi-agent-llm-landscape

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 56.5 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.42
- Coverage: 0.45
- Depth: 0.35
- Citation quality: 0.72
- Citation validity: 1.00
- Citation support: 0.64
- Citation completeness: 0.73
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.00
- Depth: 0.00
- Rationale: The report discusses taxonomic layers and composition but never defines what counts as a multi-agent LLM system or what falls outside scope.
- Candidate evidence:
- Missing:
  - No operational inclusion or exclusion criteria are provided.
  - The report does not distinguish multi-agent systems from single-agent tool use, prompt chains, multiple roles instantiated by one model, classical non-LLM multi-agent systems, or hybrid designs.
  - Borderline cases and the non-universality of possible definitions are not handled explicitly.

### R2

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report identifies a reasonably broad set of recurring patterns and gives meaningful treatment of centralized versus decentralized arrangements, but it does not supply the required substantive characterization for each major pattern.
- Candidate evidence:
  - Finding 2 identifies “single-agent loops, plan-and-execute, hierarchical supervisor-worker systems, graph or workflow systems, decentralized or swarm-like systems, multi-agent debate, and verifier-critic loops.”
  - Finding 4 explains that centralized and hierarchical systems provide global coordination and accountability but create bottlenecks and single points of failure.
  - Finding 5 explains that decentralized or peer-to-peer systems can improve local resilience but make global consistency and coordination more difficult.
  - Finding 3 states that systems can combine specialization, hierarchical orchestration, graph control flow, planning, and critique.
- Missing:
  - Most patterns are listed rather than individually characterized in terms of control structure, agent arrangement, information flow, coordination mechanism, applications, and limitations.
  - Single-agent loops and plan-and-execute are named but not clearly distinguished from multi-agent systems.
  - Representative systems or applications are not concretely identified beyond generic references to specialized agents, managers, and handoffs.
  - Debate and verifier-critic architectures receive little separate analysis of their control and information flows or limitations.

### R3

- Coverage: 0.50
- Depth: 0.50
- Rationale: There is useful analysis of control topology and communication, but coverage of the rubric’s broader cross-cutting dimensions is incomplete and unsystematic.
- Candidate evidence:
  - Finding 4 analyzes centralized and hierarchical control, including global state, traceability, bottlenecks, and single points of failure.
  - Finding 5 analyzes decentralized peer communication, local decisions, resilience, inconsistency, and coordination difficulty.
  - Finding 6 distinguishes communication protocols from topology and internal communication strategies.
  - The Remaining Gaps section calls for measuring interactions among topology, protocol, agent count, model heterogeneity, memory design, and task structure.
  - The Conclusion distinguishes role structure, control topology, workflow, communication protocol, and messaging strategy.
- Missing:
  - Sequential versus parallel execution is mentioned as a motivation but not analyzed as a design dimension with consequences.
  - Synchronous versus asynchronous operation is not addressed substantively.
  - Message passing versus shared state, context isolation versus sharing, and static versus dynamic agent allocation are not analyzed.
  - The report does not systematically explain how the dimensions affect independence, consistency, scalability, latency, or resource use across patterns.
  - Hierarchical versus peer coordination is discussed only indirectly and not as a complete cross-cutting comparison.

### R4

- Coverage: 0.25
- Depth: 0.25
- Rationale: A few roles and orchestration functions are named, but the report does not provide the requested component-level composition analysis.
- Candidate evidence:
  - Finding 8 mentions specialized agents, managerial coordination, parallel work, distributed context, debate, and critique.
  - Finding 4 describes centralized orchestrators that allocate tasks, maintain global state, monitor workers, and synthesize results.
  - The Conclusion refers to roles, protocols, messaging strategies, and evaluation layers.
- Missing:
  - Planner or orchestrator roles are not systematically distinguished from workers, critics, verifiers, or synthesizers.
  - Tools and retrieval are not discussed as compositional mechanisms.
  - Memory and shared state receive only passing mention and are not explained.
  - Evidence, provenance, and audit tracking are not discussed as mechanisms.
  - The report does not distinguish essential architectural features from optional overlays or implementation choices.
  - The interactions between roles and the identified architectural patterns are largely left implicit.

### R5

- Coverage: 0.00
- Depth: 0.00
- Rationale: The report describes a proposed layered design graph conceptually but does not provide the required visual synthesis.
- Candidate evidence:
- Missing:
  - No actual visual taxonomy, diagram, graph, table, or other interpretable visual is provided.
  - The phrase “layered design graph” appears in the prose, but the graph itself is absent.
  - Relationships among patterns, alternatives, compositions, and overlays are therefore not made visually explicit.
  - There is no legend, reading guidance for a visualization, or discussion of classification limitations tied to an actual visual.

### R6

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report offers qualified, non-universal trade-off reasoning and recognizes baseline limitations, but its empirical comparison is not sufficiently detailed or quantitative.
- Candidate evidence:
  - Finding 4 gives the conditional trade-off that centralized or hierarchical systems improve traceability and global coordination but create throughput bottlenecks and single points of failure.
  - Finding 5 contrasts local resilience in decentralized systems with weaker global consistency and coordination.
  - Finding 7 states that protocol performance varies by scenario across utility, latency, overhead, and failure resilience, citing ProtocolBench.
  - Finding 11 cautions that multi-agent superiority over strong single-agent or workflow baselines has not been established under matched cost and reliability constraints.
  - The Conclusion states that benefits are most plausible when work is decomposable, specialization or parallelism is valuable, or disagreement improves quality, while costs may outweigh benefits.
- Missing:
  - The report does not provide quantitative details from ProtocolBench such as task, baseline, metric values, or experimental context.
  - Trade-offs involving monetary cost, token cost, scalability, fault tolerance, and latency are mostly asserted rather than compared systematically.
  - Measured findings are not consistently separated from design intuitions or reported practitioner claims.
  - There is no structured comparison table or pattern-by-criterion analysis.
  - Conditions for trade-offs are discussed at a high level but not tied to specific workloads, agent counts, or implementation regimes.

### R7

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report has strong breadth on evaluation dimensions and risks, but only limited treatment of concrete detection, mitigation, and oversight mechanisms.
- Candidate evidence:
  - Finding 10 identifies behavior, capabilities, reliability, safety, task utility, latency or throughput, communication overhead, and failure-time robustness as evaluation dimensions.
  - Finding 11 recommends single-agent baselines and notes the lack of common baselines and comparable methodology.
  - Finding 9 identifies semantic drift, lossy handoffs, correlated errors, coordination overhead, token and latency costs, scalability limits, security vulnerabilities, and governance failures.
  - The report also names premature consensus, judge bias, generator-critic collusion, prompt-injection propagation, and agent or tool failures in the Remaining Gaps section.
  - The Remaining Gaps section calls for benchmarks covering cascading errors, collusion, supervisor drift, prompt injection, failures, recovery, provenance, human intervention, and containment.
- Missing:
  - Concrete mitigations and monitoring procedures are largely absent; risks are listed more often than linked to safeguards.
  - Human oversight, access control, sandboxing, tool-use restrictions, rollback, provenance checks, and termination policies are not explained operationally.
  - Contradiction and memory failures are mentioned in the open-problem list but not analyzed as failure modes with detection or mitigation methods.
  - The report does not clearly distinguish risks that are characteristic of particular architectures from risks that apply only under certain configurations.
  - Evaluation design lacks detailed ablations, coordination-behavior measures, and protocols for detecting correlated or propagated errors.

### R8

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report provides a substantial and specific open-problem inventory with identifiable sources and some uncertainty qualification, but sourcing and problem-by-problem explanation are not sufficiently deep.
- Candidate evidence:
  - The Remaining Gaps section identifies specific problems involving matched single-agent baselines, taxonomy design, topology-protocol interactions, semantic-preserving communication, provenance, correlated hallucinations, cascading errors, long-horizon evaluation, governance, and generalization.
  - Finding 11 identifies the unresolved question of whether multi-agent systems outperform strong baselines under matched quality, cost, latency, and reliability constraints.
  - The report states that protocol results do not resolve interactions with topology, agent count, model heterogeneity, memory, or long-horizon control flow.
  - Sources are identifiable through labeled entries [S1]–[S10], including surveys, benchmarks, empirical work, and architecture discussions.
  - The report qualifies evidence by labeling findings with confidence levels and noting that the evidence is provisional and lacks a settled scholarly consensus.
- Missing:
  - Most open problems are presented as terse research questions without explaining in detail what remains unresolved, why it matters, or how it could be investigated.
  - Source quality and evidentiary status are uneven: several sources are practitioner blogs, and the report does not clearly distinguish peer-reviewed evidence, preprints, surveys, and informal commentary.
  - Specific benchmark findings, study designs, baselines, metrics, and limitations are not supplied for most cited claims.
  - The report does not map each major open problem to particular sources, reported limitations, or proposed future directions in a detailed way.
  - Memory, learning or adaptation, interoperability, and resource allocation are only briefly represented rather than developed as organized research areas.

### Novel Value

- The report usefully frames the landscape as a layered, compositional design space rather than a single mutually exclusive taxonomy.
- It separates communication protocols from broader topology and highlights scenario-dependent protocol trade-offs.
- It explicitly cautions against assuming universal multi-agent superiority and emphasizes matched single-agent and workflow baselines.
- It identifies interactions among topology, protocol, agent count, heterogeneity, memory, and long-horizon control as an important unresolved research area.

## Citations

### Support

#### F1: PARTIALLY_SUPPORTED

- Claim: A multi-dimensional taxonomy is more appropriate than a mutually exclusive list of architectures.
- Sources: S1, S4, S5, S8
- Rationale: The sources support using multiple dimensions or categories to describe agent systems, but they do not directly establish the comparative judgment that this approach is more appropriate than a mutually exclusive list. S8 provides the strongest support by explicitly proposing a framework spanning system-level and internal communication dimensions. S1 describes four quadrants and notes that production systems commonly compose patterns across quadrants, which weighs against treating architectures as mutually exclusive. S4 and S5 describe taxonomies or multiple architectural patterns, but do not clearly make the claimed comparison.
- Supporting text: S8: The survey proposes a framework integrating system-level communication (architecture, goals, and protocols) with system-internal communication (strategies, paradigms, objects, and content). S1: “most production agent systems are compositions of two or three from across those quadrants.”

#### F2: PARTIALLY_SUPPORTED

- Claim: The major architectural patterns include single-agent loops, plan-and-execute, hierarchical supervisor-worker systems, graph or workflow systems, decentralized or swarm-like systems, multi-agent debate, and verifier-critic loops.
- Sources: S1, S3, S4, S5, S2
- Rationale: S1 directly supports single-agent loops, plan-and-execute, hierarchical supervisor-worker, multi-agent debate, and verifier-critic patterns. S4 and S5 support decentralized and centralized/orchestrated architectures, while S3 describes networked specialist-agent arrangements. However, the supplied excerpts do not explicitly establish “graph or workflow systems” as a named architectural pattern, and the sources do not collectively demonstrate that this list constitutes the major or exhaustive patterns.
- Supporting text: S1 names ReAct as the “canonical agent loop” and explicitly defines Plan-and-execute, Supervisor-worker, Multi-agent debate, and Verifier-critic. S4 identifies decentralized orchestration; S5 discusses decentralized systems and provides a LangGraph supervisor/agent workflow implementation.

#### F3: PARTIALLY_SUPPORTED

- Claim: The design space is compositional: a system may combine specialization, hierarchical orchestration, graph control flow, planning, and critique.
- Sources: S1, S2, S3
- Rationale: The sources support a compositional design space involving specialist agents, hierarchical orchestration, planning, and critique. S1 explicitly says production systems are compositions of multiple patterns and describes plan-and-execute, supervisor-worker, graph topologies, and verifier-critic. S2 supports specialized agents collaborating through a manager and planning/execution. S3 supports specialist agents arranged in networks and identifies orchestration and control-flow strategies. However, the supplied S1 excerpt does not actually define or substantiate graph control flow in detail, and the sources do not clearly establish that all five listed elements may be combined within one system. Thus, only a narrower compositional claim is supported.
- Supporting text: S1: “most production agent systems are compositions of two or three” patterns; it describes “Plan-and-execute,” “Supervisor-worker” hierarchical orchestration, and “Verifier-critic.” S2: specialized agents “share information, and sequence their efforts through the manager.” S3: “specialist agents” can be arranged “in a network” with “agent orchestration” and “control-flow strategies.”

#### F4: SUPPORTED

- Claim: Centralized and hierarchical systems provide global coordination and clearer accountability, but create bottlenecks and single points of failure.
- Sources: S5, S1
- Rationale: S5 directly supports the centralized-system portions: it states that centralized systems route data through one hub, ensuring consistency; the orchestrator maintains global state, makes routing decisions, and provides clear accountability. It also explicitly identifies bottlenecks and a single point of failure. S1 supports the hierarchical aspect by defining supervisor-worker as hierarchical multi-agent coordination, though it does not itself state all of the claimed benefits and drawbacks.
- Supporting text: S5: “In centralized systems, all data flows through one hub, creating a bottleneck but ensuring consistency.” It says the orchestrator “maintains global state,” provides “clear accountability,” becomes a bottleneck, and that if it fails, “all return processing stops.” S1: “Supervisor-worker. Hierarchical multi-agent,” where the supervisor decomposes tasks, routes them to workers, and aggregates results.

#### F5: PARTIALLY_SUPPORTED

- Claim: Decentralized or peer-to-peer systems can improve local resilience and reduce dependence on a central hub, but make global consistency and coordination more difficult.
- Sources: S4, S5
- Rationale: S5 directly supports the tradeoff: decentralized systems enable faster local decisions, avoid reliance on a single point of failure, but risk global inconsistency and make coordination harder. However, the cited text does not explicitly state that decentralized systems reduce dependence on a central hub in those terms, and S4 provides only general discussion of decentralized architectures without the specific resilience claim.
- Supporting text: S5 states that decentralized systems allow direct peer communication and faster local decisions while risking global inconsistency; they can continue operating when multiple agents fail, but coordination becomes exponentially harder.

#### F6: SUPPORTED

- Claim: Communication protocols are a distinct architectural layer whose choice affects system behavior.
- Sources: S8, S9
- Rationale: S8 explicitly distinguishes system-level communication, including protocols and architecture, from system-internal communication. S9 directly identifies a separate “communication protocol layer” and states that protocol choice significantly influences system behavior, with measured differences in latency, completion time, and failure resilience.
- Supporting text: S8: “we propose a two-level analytical framework distinguishing between system-level communication and system-internal communication”; LLM-MAS are “communication protocol-constrained” and operate within a “predefined communication architecture.” S9: “the communication protocol layer has become a critical…factor shaping performance and reliability” and “the choice of protocol significantly influences system behavior.”

#### F7: PARTIALLY_SUPPORTED

- Claim: No communication protocol is uniformly best; protocol performance is scenario-dependent across utility, latency, overhead, and failure resilience.
- Sources: S9
- Rationale: S9 strongly supports scenario-dependent performance and trade-offs across task utility, latency, and failure resilience. It explicitly reports four evaluation axes, including message/byte overhead, but the supplied results do not provide comparative overhead findings sufficient to establish that performance varies across that axis. The broader claim that no protocol is uniformly best is supported by the reported scenario-specific winners and trade-offs, though not as an absolute universal conclusion.
- Supporting text: S9 states that ProtocolBench reveals “clear, scenario-dependent trade-offs”: A2A has the highest task utility in GAIA, ACP the lowest latency in Streaming Queue, and A2A the strongest Fail-Storm resilience. It also describes comparisons across “task success/quality, end-to-end latency/throughput, message/byte overhead, and failure-time robustness.”

#### F8: PARTIALLY_SUPPORTED

- Claim: The principal motivations for multi-agent systems are decomposition, specialization, parallelism, distributed context, and access to multiple perspectives.
- Sources: S2, S3, S5, S8
- Rationale: The sources clearly support decomposition, specialization, parallelism, and distributing context. They also support collaboration and exchanging ideas, but do not clearly establish “access to multiple perspectives” as a principal motivation, nor do they present this exact five-item list as the principal motivations.
- Supporting text: S2 describes breaking complex work into subtasks assigned to specialized agents, parallel processing, and dividing extended context across agents. S3 states that MAS divides complex tasks into smaller tasks assigned to distinct agents and highlights specialist agents. S5 describes simultaneous specialized agents and says multi-agent architectures distribute context across agents with separate windows. S8 says multiple agents address goals beyond a single agent’s capacity and that communication facilitates idea exchange and coordinated planning.

#### F9: PARTIALLY_SUPPORTED

- Claim: The main research and deployment risks are semantic drift, lossy handoffs, correlated errors, coordination overhead, token and latency costs, scalability limits, security vulnerabilities, and governance failures.
- Sources: S1, S4, S3, S8
- Rationale: The sources substantiate several listed risks: semantic/contextual drift, semantic loss during protocol handoffs, correlated or undetected errors, coordination overhead, token consumption, latency costs, scalability issues, and security vulnerabilities. However, the supplied excerpts do not meaningfully establish governance failures as a risk, and they do not clearly support the broad framing that these are the main risks. S3 mentions governance as a research direction, but not governance failures specifically.
- Supporting text: S4 describes “contextual drift,” “interaction protocol semantic loss,” similar agents producing undetected errors, and escalating token consumption. S1 identifies coordination overhead and a latency tax. S8 explicitly lists security vulnerabilities and scalability issues among current challenges. S3 notes variability in LLM behavior and calls for improved reliability, scalability, and governance.

#### F10: SUPPORTED

- Claim: Evaluation should be multi-dimensional and end-to-end rather than limited to final-answer quality.
- Sources: S10, S9
- Rationale: S10 explicitly presents evaluation across multiple objectives and processes, including behavior, capabilities, reliability, safety, interaction modes, metrics, tooling, and environments, and states that standard LLM evaluation is insufficient for interactive agents. S9 directly contrasts task-level/final accuracy with broader end-to-end measures, arguing that evaluations should also capture latency, communication overhead, and failure robustness.
- Supporting text: S10: The survey proposes a two-dimensional taxonomy covering evaluation objectives and processes, and says agent evaluation is more complex than evaluating text generation or question answering alone. S9: ProtocolBench measures task success/quality, end-to-end latency/throughput, message/byte overhead, and robustness under failures; it notes that prior work mainly focused on final task accuracy while missing efficiency and stability signals.

#### F11: PARTIALLY_SUPPORTED

- Claim: Current evidence does not establish that multi-agent systems generally outperform strong single-agent or alternative workflow baselines under matched cost and reliability constraints.
- Sources: S1, S2, S3, S4, S5
- Rationale: The sources support a cautious, non-universal conclusion: S1 recommends establishing a single-agent baseline and notes coordination overhead, while S3 reports case-study results but also emphasizes behavioral variability and unresolved reliability, scalability, and governance limitations. However, the saved content does not provide a systematic comparison under matched cost and reliability constraints, so it cannot directly establish the full claim about the state of current evidence.
- Supporting text: S1: “Start single-agent. Escalate to multi-agent only when single-agent caps out on a measured quality dimension,” and supervisor-worker systems can incur coordination overhead. S3: findings reinforce “variability in LLM behaviour” and identify further work needed to improve reliability and scalability.

### Missing Citations

- Q1: The research landscape is best represented as a layered, compositional design space rather than a single taxonomy.
- Q2: Agent roles and relationships, control topology, communication protocols, and evaluation constitute distinct dimensions of the multi-agent LLM design space.
- Q3: There is no universally superior architecture or protocol established by the available evidence.
- Q29: Multi-agent systems offer plausible benefits when work is decomposable, specialization or parallelism is valuable, or disagreement improves quality.
- Q30: Multi-agent systems introduce coordination, communication, cost, security, and reliability problems that can outweigh their benefits.
- Q31: The field is mature enough for a structured taxonomy and targeted comparative benchmarks, but not mature enough to support a universal architecture recommendation.

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
2. R5: Provide an interpretable visual taxonomy or design graph showing the major patterns, their relationships, and relevant cross-cutting overlays.
3. R2: Identify and characterize the major architectural patterns in multi-agent LLM systems.
4. 8 cited finding(s) were not fully supported by saved evidence.
5. 6 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `3ba296f97ad2c98be185e194bbae89b363b2bc81a38fd31abf5dbf056e9a34b0`
- Candidate report hash: `dde17025de5d2290fbd0fb3edb6e63f6facee474c05c3852bc1cb73f615c7a41`
- LLM calls: 13
- Evaluated at: 2026-09-01T10:43:16.858155+00:00
