# Research Report

## Research Question

Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are.

## Summary

The supplied evidence supports a multidimensional rather than canonical taxonomy. Multi-agent LLM systems distribute complex work among specialized agents that communicate, share information or state, and sequence or combine outputs. The strongest architectural distinction is organizational: centralized or hierarchical, decentralized or peer-to-peer, specialized-role or team-based, and hybrid systems. These structural patterns can be combined with functional patterns such as plan-and-execute, debate, and verifier-critic, and with orthogonal dimensions such as adaptive control, memory sharing, protocol layers, and tool interaction. The evidence supports identifying major patterns and their trade-offs, but it does not establish a complete or mutually exclusive field-wide taxonomy, standardized cross-architecture evaluation, or reliable comparative performance conclusions.

## Findings

### Finding 1

**Claim**

Multi-agent LLM systems are distributed workflows in which multiple specialized agents divide complex tasks, communicate or hand off information, and combine their work; tool and memory access may also be part of the system.

**Confidence:** High

**Why this confidence level**

The core distributed-specialization description is directly supported by two sources.

**Evidence**

- Specialized agents divide complex tasks into subtasks, communicate, share information, and assemble a final result. [S3]
- Multi-agent systems are described as networks of specialist agents that hand off successive process stages and use division of labour. [S5]

### Finding 2

**Claim**

The most defensible high-level taxonomy separates organizational topology and control structure from functional collaboration patterns. Organizational categories include centralized or hierarchical, decentralized or peer-to-peer, specialized-role or team-based, and hybrid systems; adaptive or dynamic control is better treated as an orthogonal axis rather than a separate topology.

**Confidence:** High

**Why this confidence level**

The organizational distinction is supported by several sources. However, the supplied evidence also shows overlapping classifications rather than one canonical list.

**Evidence**

- Multiple sources classify systems using centralized, decentralized, hierarchical, hybrid, specialized, peer-to-peer, team-based, blackboard, and swarm lenses, while emphasizing control, orchestration, information flow, and message flow. [S2] [S6] [S8] [S9] [S10] [S12]
- A survey explicitly proposes centralized, decentralized, and hierarchical topologies, with dynamic or adaptive control as an optional independent axis. [S6]

### Finding 3

**Claim**

Supervisor-worker is a hierarchical pattern: a supervisor decomposes and allocates work to specialized workers, monitors or determines completion, and aggregates results. Team-based or society architectures are a related configuration in which specialists operate under a team lead and commonly use shared state or memory. Hierarchy can improve delegation and scale, but introduces bottlenecks, single points of failure, robustness trade-offs, and explainability and safe-integration requirements.

**Confidence:** High

**Why this confidence level**

The supervisor-worker structure and hierarchical trade-offs are directly or consistently supported. The boundary between team-based and supervisor-worker systems remains incompletely specified.

**Evidence**

- Supervisor-worker systems use a supervisor for decomposition, routing, monitoring or completion decisions, and result aggregation. [S1] [S3] [S10] [S12]
- Team-based systems contain a team lead, specialist agents, and shared state or memory for preserving context and integrating outputs. [S10]
- Hierarchical organization supports divide-and-conquer delegation and multiple abstraction or temporal levels, but can reduce robustness and raises explainability, trust, scaling, and safe-integration concerns. [S11] [S12]

### Finding 4

**Claim**

Flat or peer-to-peer architectures use equal-status agents with direct or many-to-many communication and no central supervisor. They may support flexible local coordination and continued operation under some failures, but create greater protocol-design and global-consistency demands.

**Confidence:** Medium

**Why this confidence level**

The structure and trade-offs are directly supported, but the evidence does not establish general performance boundaries or conditions under which the pattern is preferable.

**Evidence**

- Flat systems are described as leaderless networks in which peers can directly message or call one another, with protocol design becoming important. [S10]
- Decentralized systems are associated with faster local decisions and continued operation under failures, but also harder coordination and global inconsistency. [S12]

### Finding 5

**Claim**

Plan-and-execute separates planning from execution: a planner creates an ordered plan and an executor performs it. Debate and verifier-critic are evaluative functional patterns: debate uses competing positions and a judge or synthesizer, while verifier-critic uses critique and revision. These patterns can be composed with centralized, hierarchical, or decentralized organization rather than being equivalent to a topology.

**Confidence:** Medium

**Why this confidence level**

The definitions come primarily from S1, with indirect support for cross-agent checking and its limitations from other sources.

**Evidence**

- Plan-and-execute is defined as a planner/executor split and is associated with lower execution cost or specialization, but can be brittle when conditions change or capabilities do not match the plan. [S1]
- Debate uses competing positions plus a judge or synthesizer; verifier-critic uses generation, critique, and revision. [S1]
- Cross-agent checking may improve reliability, but collaborative systems also incur coordination overhead and remain behaviorally variable. [S1] [S3] [S5]

### Finding 6

**Claim**

A useful comparison framework treats orchestration as the interaction of task allocation, communication and context sharing, state management and persistence, control-flow sequencing, and error detection or recovery. Additional comparison dimensions include control hierarchy, information flow, role and task delegation, temporal layering, communication structure, protocol layer, and degree of centralization.

**Confidence:** Medium

**Why this confidence level**

These dimensions are directly proposed by the supplied sources, but they are not shown to be sufficient, universally adopted, or consistently operationalized across architectures.

**Evidence**

- The orchestration layer is decomposed into five mechanisms: allocation, communication/context sharing, state persistence, sequencing, and error recovery. [S6]
- Hierarchical systems are compared using control hierarchy, information flow, role and task delegation, temporal layering, and communication structure. [S11]
- Agent-to-tool and agent-to-agent communication are distinguished as complementary protocol layers; decentralized discovery is treated separately. [S6]

### Finding 7

**Claim**

The principal open problems are coordination complexity, semantic drift and information loss in protocols, state and memory consistency, token and resource scaling, latency, reliability and hallucination, error propagation, scalability, security and governance, explainability, safe integration, and evaluation.

**Confidence:** High

**Why this confidence level**

The challenge categories are supported across numerous sources, although the evidence does not provide standardized measurements or comparative outcomes.

**Evidence**

- Sources identify contextual drift, semantic loss, coordination difficulty, token optimization, reliability, scalability, governance, protocol design, memory sharing, and production concerns. [S1] [S2] [S5] [S6] [S10]
- Topology-dependent concerns include bottlenecks and single points of failure in centralized or hierarchical systems, global inconsistency in decentralized systems, super-linear interaction and debugging burdens, latency, and orchestrator capacity limits. [S6] [S8] [S12]
- Hierarchical systems additionally face explainability, human-trust, scalable-coordination, and safe-integration challenges. [S11]

## Conflicts and Uncertainty

- The supplied sources offer several overlapping taxonomies—topology-based, role-based, pattern-based, practitioner-oriented, and domain-specific. They do not resolve whether supervisor, hierarchical, team-based, blackboard, swarm, debate, and verifier-critic are mutually exclusive categories or composable dimensions. [S2] [S6] [S8] [S9] [S10] [S11] [S12]
- The evidence supports multiple pattern lists, but does not establish a field-wide canonical taxonomy or fully define all patterns implied by the broader classification space. [S1] [S6] [S8] [S10] [S11] [S12]
- Quantitative claims about performance, efficiency, scalability, or reliability cannot be compared reliably because standardized benchmarks, baselines, and detailed methods are not supplied. [S1] [S2] [S5] [S6] [S8] [S10] [S11] [S12]

## Remaining Gaps

- G1: The evidence does not fully enumerate or define the claimed eight canonical patterns; several patterns remain unspecified.
- G2: No supplied source provides a complete visual taxonomy or design graph with explicit edges among all listed architectural and functional patterns.
- G3: Open problems are not systematically mapped to every architecture and comparison dimension, and comparative performance is not established.
- G4: Communication topology, memory or state sharing, execution model, tool interaction, and centralization lack consistent cross-architecture definitions and comparison.
- G5: Standardized benchmarks, baselines, and methods are insufficient for reliable quantitative cross-architecture conclusions.
- G6: Boundaries and compositional relationships among topology-, role-, and pattern-based taxonomies remain unresolved.
- G7: There is no standardized cross-architecture evaluation procedure connecting protocol, state, latency, security, and coordination dimensions to empirical outcomes.
- G8: Explainability, trust, scalable coordination, and safe integration lack cross-architecture evaluation criteria.

## Conclusion

The evidence supports a design graph in which organizational topology is the primary structural layer, functional collaboration patterns are composable mechanisms, and orchestration and system-capability dimensions cut across both. The graph below is therefore an evidence-based synthesis rather than a source-supplied canonical taxonomy:

```text
MULTI-AGENT LLM SYSTEM
│
├── Organizational topology / control
│   ├── Centralized or hierarchical
│   │   ├── Supervisor-worker
│   │   └── Team-based / society
│   │       Open problems: bottlenecks, single-point failure,
│   │       supervisor drift, explainability, safe integration
│   │
│   ├── Decentralized / flat peer-to-peer
│   │   └── Direct or many-to-many peer communication
│   │       Open problems: protocol design, coordination,
│   │       global consistency, error propagation
│   │
│   └── Hybrid / mixed control
│       └── Combines centralized, hierarchical, or peer structures
│           Open problems: boundary management, state consistency,
│           monitoring, governance
│
├── Functional collaboration patterns (composable with the above)
│   ├── Plan-and-execute
│   │   └── Planner → ordered plan → executor
│   │       Open problem: brittleness under changing conditions
│   ├── Debate
│   │   └── Competing positions → judge/synthesizer
│   │       Open problems: premature convergence, judge bias
│   └── Verifier-critic
│       └── Generator → critique → revision loop
│           Open problems: critique degradation, reliability
│
└── Cross-cutting design dimensions
    ├── Task allocation and role assignment
    ├── Communication, context sharing, and protocol layers
    ├── State / memory persistence and consistency
    ├── Control-flow sequencing and adaptive control
    ├── Error detection and recovery
    ├── Tool interaction and agent-to-agent interaction
    └── Resource, token, latency, security, governance, and evaluation
        Open problems: scalable coordination, reliability, safety,
        standardized benchmarks, explainability, production maturity
```

The CORE questions are only partially resolved: the evidence is sufficient for a provisional taxonomy and design graph, but not for a canonical classification, exhaustive architecture definitions, systematic problem-to-pattern mapping, or validated cross-architecture comparisons.

## Sources

- [S1] Agent Architecture Patterns: 2026 Taxonomy Guide — https://www.digitalapplied.com/blog/agent-architecture-patterns-taxonomy-2026
- [S2] LLM Agent Orchestration Patterns: Architectural ... — https://www.c-sharpcorner.com/article/llm-agent-orchestration-patterns-architectural-frameworks-for-managing-complex
- [S3] Multi-agent LLMs in 2026 [+frameworks] — https://www.superannotate.com/blog/multi-agent-llms
- [S4] From RAG to Multi-Agent Systems: A Survey of Modern Approaches in LLM Development — https://www.preprints.org/manuscript/202502.0406
- [S5] LLM-Enabled Multi-Agent Systems: Empirical Evaluation ... — https://arxiv.org/html/2601.03328v1
- [S6] LLM-Based Multi-Agent Orchestration: A Survey of ... — https://www.preprints.org/manuscript/202604.2147
- [S7] LLM-Based Multi-Agent Orchestration: A Survey of ... — https://www.mdpi.com/1999-5903/18/6/326
- [S8] Multi-agent system architecture: a comparison guide + best practices (March 2026) | Openlayer — https://www.openlayer.com/blog/multi-agent-system-architecture-guide
- [S9] A survey on LLM-based Multi-Agent Systems — https://www.sciencedirect.com/science/article/pii/S2405959526001189
- [S10] Multi-Agent LLM Systems: Architecture, Communication, and Coordination — https://samiranama.com/posts/LLM-Based-Multi-Agent-Systems-Architectures-and-Collaboration
- [S11] A Taxonomy of Hierarchical Multi-Agent Systems: Design Patterns, Coordination Mechanisms, and Industrial Applications — https://arxiv.org/html/2508.12683
- [S12] Architectures for Multi-Agent Systems — https://galileo.ai/blog/architectures-for-multi-agent-systems
