# Research Report

## Research Question

Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are.

## Summary

The accumulated evidence supports a compositional view of multi-agent LLM systems rather than one universal taxonomy. Three layers should be distinguished: (1) agent-level capabilities and control loops, (2) communication topology and state ownership, and (3) workflow or interaction protocols such as planning, debate, verification, and reflection. Centralized/hierarchical, peer-to-peer, graph/DAG, and blackboard systems are the main topology families. Empirical results indicate that architecture choice is conditional on task structure and involves accuracy, cost, latency, context, and failure-isolation trade-offs. The field’s principal gap is the absence of broad, independently replicated comparisons under matched budgets across domains.

## Findings

### Finding 1

**Claim**

A useful landscape model separates agent internals, system topology/state, and coordination protocols.

**Confidence:** High

**Why this confidence level**

Multiple sources independently support a layered, compositional representation.

**Evidence**

- The survey models agents through profile, perception, self-action, mutual interaction, and evolution, while other sources separately discuss centralized, decentralized, hierarchical, and blackboard architectures. [S2] [S6]
- The debate survey distinguishes participants, interaction mechanisms, and agreement protocols, supporting a separation between communication structure and decision procedure. [S8]
- Architecture-oriented sources identify topology, state ownership, observability, and failure domains as distinct dimensions. [S5] [S9]

### Finding 2

**Claim**

The major topology families are centralized/hierarchical coordination, decentralized peer networks, graph or DAG workflows, and shared-memory/blackboard systems.

**Confidence:** High

**Why this confidence level**

These families recur across academic-survey, implementation, and architecture sources, although category boundaries vary.

**Evidence**

- Sources describe centralized coordinators, decentralized peer-to-peer systems, layered or hierarchical teams, and blackboards as distinct architecture families. [S5] [S6] [S7] [S9]
- A LangGraph research system demonstrates graph-based routing with parallel specialists, gap analysis, citation auditing, synthesis, and bounded iteration. [S4]

### Finding 3

**Claim**

Centralized supervisor-worker and hierarchical systems offer control, auditability, structured decomposition, and clearer debugging, but create coordinator bottlenecks, single points of failure, context growth, and possible supervisor drift.

**Confidence:** Medium

**Why this confidence level**

The architectural trade-offs are consistent across sources, but performance results are domain-specific and not independently replicated in the retrieved material.

**Evidence**

- Hub-spoke systems route communication through a central hub that owns canonical state and synthesizes worker outputs; the hub is described as a single point of failure with potential context and routing degradation. [S5]
- Supervisor-worker systems decompose tasks among specialists but incur coordination overhead and may hide conflicts or suffer supervisor drift. [S1]
- A financial-document benchmark reported hierarchical orchestration as a favorable cost-accuracy point, with F1 0.921 at 1.4 times sequential-baseline cost in that setting. [S10]

### Finding 4

**Claim**

Peer-to-peer, swarm, and mesh systems increase agent autonomy and can avoid a single coordinator, but make global consistency, observability, semantic alignment, and coordination more difficult.

**Confidence:** Medium

**Why this confidence level**

The topology and risks are directly documented, but the comparative result comes from a limited company benchmark and conflicts conditionally with another domain-specific study.

**Evidence**

- Peer architectures permit many-to-many communication without a central supervisor, while sources identify contextual drift, semantic loss, and emergent behavior as coordination risks. [S3] [S7]
- A LangChain benchmark found swarm slightly outperforming supervisor on a modified Tau-bench distractor-context test, attributing the supervisor disadvantage partly to translation between sub-agents and the user. [S14]

### Finding 5

**Claim**

Graph/DAG architectures are best understood as explicit workflow/control structures that can compose parallelism, conditional routing, retries, verification, and iterative synthesis.

**Confidence:** Medium

**Why this confidence level**

The compositional role of graphs is well supported, but broad claims about production superiority are not established by matched evidence.

**Evidence**

- The deep-research implementation uses a graph containing classification, planning, parallel specialist dispatch, gap analysis, citation audit, writing, refinement, and bounded termination. [S4]
- The broader literature summary describes task-dependency DAGs and graph-based coordination policies for distributed planning. [S6]
- The taxonomy guide treats graph and hierarchical systems as commonly useful production patterns while also stating that systems often combine multiple patterns. [S1]

### Finding 6

**Claim**

Blackboard systems form a distinct shared-state control family: agents read and write a common workspace, while a controller dynamically selects participants based on workspace contents.

**Confidence:** Medium

**Why this confidence level**

The architecture is clearly specified and evaluated, but evidence comes from one implementation without enough detail on matched models, budgets, or independent replication.

**Evidence**

- The LbMAS implementation uses a shared blackboard as the communication medium, dynamic agent selection, iterative execution/update/evaluation, and a maximum four-round limit. [S13]
- The system reports competitive or best-average results across six knowledge, reasoning, and mathematics benchmarks, together with lower token use than several compared systems. [S13]

### Finding 7

**Claim**

Planning, reflection, debate, verifier-critic, proposer-aggregator, and citation auditing are interaction or control protocols that can be embedded within different topologies.

**Confidence:** High

**Why this confidence level**

The distinction is directly supported across taxonomy, implementation, and review sources.

**Evidence**

- Sources define plan-and-execute, debate, verifier-critic, and reflection as role or workflow patterns rather than communication topologies. [S1] [S4]
- The survey describes proposer-aggregator, planner-critic, and ReAct-like reasoning-action combinations. [S6]
- The debate review characterizes systems using participant, interaction, and agreement dimensions, indicating that debate configurations are not reducible to topology alone. [S8]

### Finding 8

**Claim**

Current empirical evidence favors conditional architecture selection rather than a universally best pattern.

**Confidence:** Medium

**Why this confidence level**

The studies provide concrete conditional comparisons, but they use different tasks, metrics, models, and experimental designs.

**Evidence**

- In financial document extraction, reflexive systems achieved the highest reported field-level F1 of 0.943 but cost 2.3 times the sequential baseline, while hierarchical systems achieved 0.921 F1 at 1.4 times baseline cost. [S10]
- In a modified Tau-bench distractor-context experiment, swarm slightly outperformed supervisor, while the single-agent baseline degraded as irrelevant domains were added; the source cautions that the test required little coordination. [S14]
- A blackboard implementation reports competitive performance and token efficiency on reasoning and knowledge benchmarks, but it was not compared with all other families under a shared benchmark. [S13]

### Finding 9

**Claim**

The central research frontier is systematic, cost-aware, reproducible comparison of topology, protocol, memory, and control-policy choices under matched budgets.

**Confidence:** High

**Why this confidence level**

This gap is explicitly identified by the systematic review and remains evident after the additional benchmark sources.

**Evidence**

- The debate review of 141 primary studies finds that static fully connected communication, verbatim exchange, short-term memory, and voting dominate by convention rather than systematic comparison, and calls for controlled benchmarking and executable specifications. [S8]
- The accumulated benchmark evidence does not yet provide a broad comparison across hierarchical, graph, peer, swarm, blackboard, debate, and hybrid systems against strong single-agent baselines. [S10] [S13] [S14]

## Conflicts and Uncertainty

- Taxonomy boundaries differ. One source proposes eight patterns in four quadrants; others use four orchestration categories, three enterprise topologies, or five architecture labels. These schemes appear to operate at different abstraction levels rather than establish a settled universal taxonomy. [S1] [S3] [S5] [S6] [S7]
- Hierarchical orchestration is reported as cost-effective in financial extraction, while swarm slightly outperforms supervisor in a Tau-bench distractor-context experiment. The results are conditional on task, metric, model, sample, and coordination requirements and cannot be ranked globally. [S10] [S14]
- A blackboard implementation reports strong performance and token efficiency, whereas another taxonomy guide characterizes blackboard and swarm patterns as rarely superior in practice. No matched benchmark resolves the difference. [S1] [S13]
- Several practitioner sources make broad quantitative claims about production coverage, performance variance, agent-count bottlenecks, operational gains, or ROI, but the retrieved material does not provide sufficient methods or independent corroboration for those claims. [S1] [S3] [S9] [S12]
- The retrieved S11 page contains article metadata and title information but insufficient substantive methods or results to inform comparison with the other benchmarks. [S11]
- The research stopped at the iteration limit. Questions about cross-domain generalization, adversarial settings, long-horizon behavior, and matched-budget architecture rankings remain unresolved. [S10] [S13] [S14]

## Remaining Gaps

- A standardized schema is needed to encode topology, workflow protocol, state and memory ownership, model diversity, communication semantics, and stopping rules together.
- Broad benchmarks should compare major architectures against strong single-agent baselines under matched model, tool, token, latency, and cost budgets.
- Future evaluations should span sequential, parallelizable, ill-structured, long-horizon, regulated, and interactive tasks rather than relying on one domain.
- Researchers need measures for semantic drift, protocol information loss, state inconsistency, coordination quality, calibration, failure recovery, and error propagation.
- It remains unclear whether blackboard token efficiency persists when shared workspaces become large, private, multimodal, or distributed.
- Debate and critique studies should disentangle gains from genuine diversity or verification from gains caused simply by additional model calls and tokens.
- Robustness under adversarial agents, tool failures, partial observability, distribution shift, and recursive execution is insufficiently characterized.
- The retrieved evidence does not establish general scalability thresholds for hub capacity, team size, context length, latency, or token consumption.

## Conclusion

The most defensible map is a design graph, not a mutually exclusive taxonomy. Agents operate through internal loops such as reasoning-action, reflection, memory, and adaptation. Those agents are connected by a topology—centralized/hierarchical, peer-to-peer, graph/DAG, or blackboard—and governed by protocols such as planning, debate, critique, verification, aggregation, retries, and dynamic scheduling. State ownership and memory placement cut across all of these choices. Architecture selection should therefore begin with task structure and operational constraints: decomposition and auditability favor supervisor or hierarchical designs; explicit dependencies and conditional execution favor graphs; flexible peer negotiation favors decentralized systems; dynamic ill-structured collaboration motivates blackboards; and reliability-sensitive outputs can add verification or critique protocols. However, the evidence does not justify a universal ranking. The field’s priority is controlled, cost-aware, independently reproducible evaluation of these composable design choices.

## Sources

- [S1] Agent Architecture Patterns: 2026 Taxonomy Guide - Digital Applied — https://www.digitalapplied.com/blog/agent-architecture-patterns-taxonomy-2026
- [S2] A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges — https://link.springer.com/article/10.1007/s44336-024-00009-2
- [S3] LLM Agent Orchestration Patterns: Architectural ... — https://www.c-sharpcorner.com/article/llm-agent-orchestration-patterns-architectural-frameworks-for-managing-complex
- [S4] Medium — https://medium.com/data-science-collective/building-a-multi-agent-deep-research-agent-with-langgraph-203547b5fb12
- [S5] Multi-Agent AI Architecture: Patterns for Enterprise Development | Augment Code — https://www.augmentcode.com/guides/multi-agent-ai-architecture-patterns-enterprise
- [S6] LLM-Based Multi-Agent Systems — https://www.emergentmind.com/topics/llm-based-multi-agent-systems
- [S7] Multi-Agent LLM Systems: Architecture, Communication, and Coordination | Samira Ghodratnama — https://samiranama.com/posts/LLM-Based-Multi-Agent-Systems-Architectures-and-Collaboration
- [S8] Multi-Agent Debate Strategies: Survey, Taxonomy, and Challenges — https://arxiv.org/html/2607.26212v1
- [S9] Architectures for Multi-Agent Systems — https://galileo.ai/blog/architectures-for-multi-agent-systems
- [S10] Benchmarking Multi-Agent LLM Architectures for Financial Document Processing: A Comparative Study of Orchestration Patterns, Cost-Accuracy Tradeoffs and Production Scaling Strategies — https://arxiv.org/html/2603.22651v1
- [S11] Comparing Single-Agent and Multi-Agent Strategies in ... — https://www.mdpi.com/2079-9292/15/8/1661
- [S12] Multi-agent system architecture: a comparison guide + best practices ... — https://www.openlayer.com/blog/multi-agent-system-architecture-guide
- [S13] Exploring Advanced LLM Multi-Agent Systems Based on Blackboard Architecture | alphaXiv — https://www.alphaxiv.org/abs/2507.01701
- [S14] Benchmarking Multi-Agent Architectures - LangChain — https://www.langchain.com/blog/benchmarking-multi-agent-architectures
