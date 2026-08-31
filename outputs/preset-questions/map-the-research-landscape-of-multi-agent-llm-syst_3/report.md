# Research Report

## Research Question

Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are.

## Summary

This is an automatically generated incomplete report. The research run ended with stop reason `max_iterations`, and normal finalization did not complete during OpenAI Ledger Report Generation. The validated findings collected before that point are preserved below without claiming that the evidence is complete.

## Findings

### Finding 1

**Claim**

LLM-based multi-agent systems can be characterized by agents with distinct profiles or identities that perceive information, act, interact with other agents, and evolve through experience or reflection.

**Confidence:** High

**Why this confidence level**

The original survey framing is independently echoed by S7, strengthening support for the general component characterization.

**Evidence**

- The survey proposes a unified workflow with five components: profile, perception, self-action, mutual interaction, and evolution. [S4]
- S7 repeats the profile, perception, self-action, mutual interaction, and evolution components and describes agents as capable of perception, reasoning, planning, and collaborative action. [S7]

### Finding 2

**Claim**

A major collaborative architectural pattern is hierarchical supervisor-worker orchestration, in which a supervisor decomposes a task, routes subtasks to specialized workers, and aggregates their results.

**Confidence:** High

**Why this confidence level**

The pattern is now directly described across several additional architecture guides and taxonomies.

**Evidence**

- The described travel-planning system assigns specialized subtasks to agents and sequences and integrates their efforts through a manager. [S1]
- The supervisor-worker pattern is defined as a hierarchical system where a supervisor decomposes tasks, routes them to specialized workers, and determines completion. [S2]
- S6 defines hierarchical systems as layered command-and-control structures in which supervisors or managers delegate downward and aggregate results upward. [S6]
- S7 describes centralized and multi-level hierarchical supervision, including supervisors managing specialized workers or other supervisors. [S7]
- S9 defines supervisor and hierarchical patterns as centralized task decomposition, routing, aggregation, and multi-level delegation. [S9]

### Finding 3

**Claim**

Plan-and-execute is a two-phase collaborative pattern in which a planner produces an ordered plan and an executor carries it out step by step.

**Confidence:** Medium

**Why this confidence level**

The pattern is directly described by one taxonomy source, but the supplied evidence does not establish its prevalence independently.

**Evidence**

- S2 explicitly defines plan-and-execute as a planner emitting an ordered plan followed by executor actions. [S2]

### Finding 4

**Claim**

Multi-agent debate and verifier-critic are adversarial or evaluative patterns that use disagreement, critique, judging, or revision to improve output quality and safety.

**Confidence:** Medium

**Why this confidence level**

The architectural functions are explicitly defined in S2; S1 provides only general supporting rationale for cross-agent checking.

**Evidence**

- S2 places multi-agent debate and verifier-critic in a competitive/adversarial quadrant and describes their judge, critique, scoring, and revision functions. [S2]
- S1 states that agents can check one another's work to improve reliability and reduce mistakes. [S1]

### Finding 5

**Claim**

Parallel specialist-agent workflows are a compositional architecture for research tasks: work is split among role-specific agents, their findings are checked or audited, and a synthesis agent produces the report.

**Confidence:** High

**Why this confidence level**

Two sources directly describe this decomposition-and-integration structure, including a concrete research workflow in S5.

**Evidence**

- The LangGraph workflow dispatches specialized researchers in parallel, then performs synthesis, gap analysis, citation auditing, writing, and refinement. [S5]
- The travel example decomposes a complex task among specialized flight, hotel, transportation, and activity agents whose results are integrated. [S1]

### Finding 6

**Claim**

Communication and context management are central coordination challenges because natural-language interaction can produce contextual drift, semantic misinterpretation, and information loss across agents.

**Confidence:** High

**Why this confidence level**

The new surveys independently reinforce communication and protocol design as central system dimensions and coordination concerns.

**Evidence**

- S3 identifies contextual drift, differing interpretations, and semantic loss when agent outputs are transformed through interaction protocols. [S3]
- The survey identifies mutual interaction and communication as core parts of LLM-based MAS operation. [S4]
- S7 treats communication channels and coordination protocols as critical dimensions and distinguishes memory-based, report-based, relay, and debate communication. [S7]
- S6 emphasizes robust communication protocols and memory-sharing mechanisms as requirements for collective performance. [S6]
- S12 defines LLM-MAS as communication-protocol-constrained systems and identifies communication efficiency, security, and scalability as challenges. [S12]
- S10 treats inter-agent communication and context sharing as a core orchestration mechanism and discusses communication protocols. [S10]

### Finding 7

**Claim**

Multi-agent architectures introduce coordination and resource costs, including additional model calls, token consumption, latency, and possible scalability problems.

**Confidence:** High

**Why this confidence level**

The sources add direct discussion of interaction growth, context-size effects, token cost, communication efficiency, and scalability, while leaving quantitative generalization unresolved.

**Evidence**

- S2 repeatedly identifies coordination overhead and latency taxes as failure or trade-off dimensions for collaborative and critique-based patterns. [S2]
- S3 frames token consumption and resource optimization as important problems in agent networks. [S3]
- S5 notes that repeated specialist searches, model calls, and synthesis passes can create substantial cost and therefore uses iteration limits. [S5]
- S6 notes that many-to-many peer communication requires careful protocol design and that hierarchy is motivated partly by managing coordination at scale. [S6]
- S7 identifies centralized bottlenecks, decentralized coordination complexity, and differing overheads across network, assembly-line, role-based, and graph structures. [S7]
- S9 identifies bottlenecks, error propagation, and coordination overhead as production risks, while reporting architecture-dependent performance differences. [S9]
- S10 identifies token cost structure, scalability, and coordination complexity as production design considerations and notes super-linear growth in pairwise interaction channels. [S10]
- S12 identifies communication efficiency and scalability as open challenges in LLM-based multi-agent systems. [S12]
- S13 motivates multi-agent designs partly by context-size degradation and reports token cost as a benchmark dimension. [S13]

### Finding 8

**Claim**

A graph-based workflow can enforce procedural safeguards such as requiring citation auditing before report writing and imposing a maximum number of research iterations.

**Confidence:** High

**Why this confidence level**

These safeguards are explicitly described as properties of the reported workflow.

**Evidence**

- S5 describes a LangGraph topology in which the writer runs only after citation_audit and a maximum-iteration condition prevents unbounded gap-analysis loops. [S5]

### Finding 9

**Claim**

The supplied sources indicate that LLM-based multi-agent systems are applied across problem-solving and world-simulation settings, with examples spanning industrial engineering, scientific experimentation, embodied agents, gaming, and research assistance.

**Confidence:** Medium

**Why this confidence level**

S4 provides broad survey coverage and S5 adds a concrete research workflow, but the evidence does not support comparative claims about field maturity across applications.

**Evidence**

- The survey identifies problem-solving and world simulation as two principal application areas and lists industrial, scientific, embodied, and gaming examples. [S4]
- S5 presents a multi-agent deep-research assistant as a research-assistance application. [S5]

### Finding 10

**Claim**

A flat or peer-to-peer architecture organizes agents as equals with many-to-many communication, without a central supervisor; it enables flexible or emergent coordination but increases the need for communication-protocol design and may be better suited to smaller collaborative tasks.

**Confidence:** High

**Why this confidence level**

The architectural definition and its principal trade-offs are described directly by S6 and S7, with related organizational trade-offs in S8.

**Evidence**

- S6 defines flat architecture as peer-to-peer, leaderless communication in which any agent can message or task another, and identifies flexibility alongside protocol-design requirements and small-scale use cases. [S6]
- S7 characterizes decentralized systems as peer-to-peer and resilient, while noting increased coordination complexity. [S7]
- S8 contrasts fully decentralized organizations' resilience and equality with lower efficiency in large groups. [S8]

### Finding 11

**Claim**

Multi-agent architecture can be analyzed across separable design dimensions rather than as a single mutually exclusive pattern taxonomy, including control hierarchy, information flow, role/task delegation, temporal layering, communication topology, collaboration type, and communication protocol.

**Confidence:** High

**Why this confidence level**

The new surveys further support treating architecture as a multidimensional design space rather than a single mutually exclusive taxonomy.

**Evidence**

- S8 proposes a five-axis taxonomy covering control hierarchy, information flow, role and task delegation, temporal layering, and communication structure. [S8]
- S7 distinguishes actors, collaboration types, structures, strategies, coordination protocols, and communication paradigms such as memory-based, report-based, relay, and debate mechanisms. [S7]
- S6 describes flat, hierarchical, team-based, central-coordinator, and hybrid patterns through roles, message flows, and functions. [S6]
- S10 distinguishes coordination topology from an adaptive-control axis and compares systems using state management, cost, recovery, and design dimensions. [S10]
- S12 organizes the design space across system-level architecture, goals, protocols, and internal communication strategies, paradigms, objects, and content. [S12]

### Finding 12

**Claim**

Hierarchical multi-agent designs trade coordination efficiency and scalability for reduced robustness or resilience, while hybridizing hierarchical and decentralized mechanisms is presented as a way to balance these properties.

**Confidence:** High

**Why this confidence level**

The same trade-off is reported across sources describing hierarchical, centralized, and decentralized designs, although the evidence is largely conceptual rather than controlled comparative evaluation.

**Evidence**

- S8 states that hierarchy can simplify coordination, support scale, and improve global efficiency, but may reduce robustness; it identifies hybrid hierarchical/decentralized mechanisms as an important direction. [S8]
- S7 describes centralized coordination as controllable but bottleneck-prone, decentralized coordination as more resilient but more complex, and hierarchical systems as multi-level supervision. [S7]
- S9 describes hierarchical systems as useful for complex decomposition while identifying supervisor bottlenecks and single points of failure. [S9]

### Finding 13

**Claim**

Hierarchical multi-agent systems have open problems involving explainability to human operators, scalability to very large populations, and safe integration of learning-based or LLM agents into layered control structures.

**Confidence:** High

**Why this confidence level**

These challenges are explicitly stated in the supplied taxonomy source, but their prevalence and empirical severity across architectures are not established.

**Evidence**

- S8 explicitly identifies explainability, very-large-population scaling, and safe integration of LLM-based agents as open challenges for hierarchical systems. [S8]

### Finding 14

**Claim**

A communication-centric framework analyzes LLM-based multi-agent systems at two levels: system-level communication (architecture, goals, and protocols) and system-internal communication (strategies, paradigms, communication objects, and exchanged content).

**Confidence:** High

**Why this confidence level**

The framework and its dimensions are directly stated in the survey, although the source is a survey-level synthesis rather than a controlled empirical validation.

**Evidence**

- S12 explicitly proposes a two-level framework separating system-level from system-internal communication and enumerates the dimensions included at each level. [S12]

### Finding 15

**Claim**

A recent orchestration taxonomy groups multi-agent LLM systems into centralized, decentralized, and hierarchical coordination topologies, with dynamic or adaptive control treated as an optional cross-cutting axis.

**Confidence:** Medium

**Why this confidence level**

The taxonomy is explicitly proposed by S10, but the source is a survey and does not establish that these categories are universally accepted or operationally non-overlapping.

**Evidence**

- S10 proposes a three-topology taxonomy consisting of centralized, decentralized, and hierarchical coordination, augmented by an optional dynamic/adaptive control axis. [S10]

### Finding 16

**Claim**

Multi-agent orchestration can be decomposed into task allocation, inter-agent communication and context sharing, state management and persistence, control-flow sequencing, and error detection or recovery.

**Confidence:** Medium

**Why this confidence level**

The decomposition is directly reported as a survey framework, but the supplied evidence does not independently validate its completeness or separability.

**Evidence**

- S10 identifies these five mechanisms as interrelated components of the orchestration layer. [S10]

### Finding 17

**Claim**

On a modified version of the τ-bench dataset, a reported supervisor implementation achieved an approximately 50% performance increase relative to the comparison described by the authors, but this is application- and benchmark-specific evidence rather than a general architecture result.

**Confidence:** Low

**Why this confidence level**

The result is directly reported by a vendor-authored blog, but the supplied excerpt does not provide the full experimental protocol, baselines, statistical analysis, or independent replication.

**Evidence**

- S13 states that its benchmark compares multi-agent architectures on a modified τ-bench dataset and reports a nearly 50% performance increase from improvements to its supervisor implementation. [S13]

## Conflicts and Uncertainty

- No material conflict was identified in the retrieved evidence.

## Remaining Gaps

- The supplied evidence does not provide a validated, non-overlapping taxonomy covering agent roles, communication protocols, memory, tool use, and execution structure; the presented taxonomies mix workflow patterns, coordination topologies, and single-agent baselines.
- There is insufficient comparative evidence to determine when centralized, decentralized, hierarchical, graph, swarm, debate, or other architectures outperform one another under controlled conditions.
- The evidence identifies coordination, semantic drift, cost, latency, and scalability concerns but does not provide a systematic mapping of open problems to architectural patterns or robust evaluation results for those problems.
- The sources do not establish a reliable landscape of benchmarks, standardized metrics, reproducibility practices, or relative research coverage and maturity across application areas.
- Claims about quantitative gains, including accuracy improvements, completion-time reductions, token savings, and return on investment, are not sufficiently corroborated by independent evidence in the supplied materials.
- The new sources broaden the architecture space with peer-to-peer, team-based, assembly-line, blackboard, swarm, and hybrid patterns, but do not establish consistent operational boundaries or controlled comparisons among these patterns and the existing supervisor, plan-and-execute, debate, and graph-workflow categories.
- Claims about architecture-dependent performance and field growth remain weakly validated: the supplied sources report bottlenecks, resilience, efficiency, and numerical gains, but do not provide sufficiently transparent datasets, experimental protocols, or independent benchmarks to support general comparative conclusions.
- The evidence identifies explainability, safe LLM integration, very-large-population scaling, and human oversight as hierarchical-system challenges, but does not provide evaluation methods or empirical results showing how these risks vary across architectures.
- The supplied sources identify communication security, protocol design and convergence, and agent-to-tool or agent-to-agent interoperability as important concerns, but do not provide a systematic cross-architecture analysis of security threats, protocol guarantees, or interoperability outcomes.
- SQ1: What are the major architectural patterns used in multi-agent LLM systems, and how can they be defined and distinguished? (PARTIAL: Open high- or medium-importance research gaps still block a sufficient answer.)
- SQ2: How do the major multi-agent LLM architectural patterns relate to one another? (PARTIAL: At least one linked ledger claim is not yet supported.)
- SQ3: What are the principal open problems and research gaps across multi-agent LLM systems? (PARTIAL: Open high- or medium-importance research gaps still block a sufficient answer.)
- SQ4: What evidence and research coverage characterize the current multi-agent LLM landscape? (PARTIAL: At least one linked ledger claim is not yet supported.)

## Conclusion

The findings above reflect the evidence validated before the run ended. They should be treated as provisional because normal final synthesis did not complete and important gaps may remain.

## Sources

- [S1] Multi-agent LLMs in 2026 [+frameworks] — https://www.superannotate.com/blog/multi-agent-llms
- [S2] Agent Architecture Patterns: 2026 Taxonomy Guide — https://www.digitalapplied.com/blog/agent-architecture-patterns-taxonomy-2026
- [S3] LLM Agent Orchestration Patterns: Architectural ... — https://www.c-sharpcorner.com/article/llm-agent-orchestration-patterns-architectural-frameworks-for-managing-complex
- [S4] A survey on LLM-based multi-agent systems - Springer Nature — https://link.springer.com/article/10.1007/s44336-024-00009-2
- [S5] How to Build a Multi-Agent Deep Research System with ... — https://medium.com/data-science-collective/building-a-multi-agent-deep-research-agent-with-langgraph-203547b5fb12
- [S6] Multi-Agent LLM Systems: Architecture, Communication, and ... — https://samiranama.com/posts/LLM-Based-Multi-Agent-Systems-Architectures-and-Collaboration
- [S7] LLMs for Multi-Agent Cooperation | Xueguang Lyu — https://xue-guang.com/post/llm-marl
- [S8] A Taxonomy of Hierarchical Multi-Agent Systems: Design Patterns, Coordination Mechanisms, and Industrial Applications — https://arxiv.org/html/2508.12683
- [S9] Multi-agent system architecture: a comparison guide + best ... — https://www.openlayer.com/blog/multi-agent-system-architecture-guide
- [S10] LLM-Based Multi-Agent Orchestration: A Survey of ... — https://www.preprints.org/manuscript/202604.2147
- [S11] LLM-Based Multi-Agent Orchestration: A Survey of ... — https://www.mdpi.com/1999-5903/18/6/326
- [S12] Beyond Self-Talk: A Communication-Centric Survey of LLM ... — https://arxiv.org/html/2502.14321v3
- [S13] Benchmarking Multi-Agent Architectures — https://www.langchain.com/blog/benchmarking-multi-agent-architectures
