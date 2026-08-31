# Research Report

## Research Question

Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are.

## Summary

The research landscape is best understood as a layered design space rather than a single taxonomy. Topology describes how agents are organized; control flow describes how tasks and dependencies are executed; communication defines how agents exchange information; specialization defines agent roles; memory and evolution determine how state and experience persist; and verification, debate, and recovery provide quality and safety controls. Centralized and hierarchical systems emphasize explicit coordination, while decentralized systems emphasize peer interaction. Graph and workflow structures can implement control flow within either family, and hybrid systems combine these approaches. Across the literature, the principal unresolved issues are coordination reliability, semantic drift, scaling cost, evaluation, security, governance, and safe transition from prototypes to production.

Design graph:

```text
                           MULTI-AGENT LLM SYSTEM
                                      |
       ----------------------------------------------------------------
       |                 |                 |                 |          |
   TOPOLOGY          CONTROL FLOW      COMMUNICATION     AGENT ROLES  STATE/EVOLUTION
       |                 |                 |                 |          |
  -----------      -------------     -------------     ----------   -----------
  |    |    |      |     |     |     |     |     |     |        |   |         |
Centralized  Decentralized  Hierarchical  Fixed   Graph/  Plan-  Peer   Protocols  Shared/  Specialized  Generalist  Memory  Feedback
  |             |              |         workflow dependency execute messaging /goals   state   agents      agents    /RAG   /reflection
  |             |              |             \       |       /       |         |
  ----------------------------- HYBRID COMPOSITIONS -------------------------
                                      |
                        QUALITY / SAFETY CONTROL LOOPS
                                      |
                    verifier-critic | debate | judge | human oversight
                                      |
                              OPEN PROBLEMS
 reliability • semantic drift • state consistency • token/latency scaling
 benchmarking • collusion/conflict • security • provenance • governance
```

This graph is a synthesis of the retrieved taxonomies; the categories should not be treated as mutually exclusive.

## Findings

### Finding 1

**Claim**

LLM-based multi-agent systems consist of multiple specialized or differentiated agents that divide complex tasks, communicate intermediate information, use tools or environments, and combine their outputs.

**Confidence:** High

**Why this confidence level**

The core system model is supported consistently by an academic survey, an empirical study, and an independent overview.

**Evidence**

- The survey describes a unified workflow comprising profile, perception, self-action, mutual interaction, and evolution, with specialized agents communicating and collaborating toward objectives. [S5]
- The empirical study characterizes MAS as networks of specialist agents using orchestration, communication mechanisms, and control-flow strategies to divide tasks and hand off work. [S4]
- The practitioner overview describes decomposition into subtasks, role-specialized agents, tool use, information sharing, and final aggregation. [S1]

### Finding 2

**Claim**

Topology is one dimension of the landscape, with centralized, decentralized, hierarchical, and hybrid arrangements forming the principal organizational families.

**Confidence:** High

**Why this confidence level**

Multiple sources converge on the main topology families, although they use different labels and combine topology with other design dimensions.

**Evidence**

- The orchestration survey proposes centralized, decentralized, and hierarchical coordination topologies, with dynamic control treated as an additional axis. [S6]
- The empirical taxonomy explicitly includes centralized, decentralized, hybrid, and specialized categories. [S3] [S4]
- The practitioner architecture overview describes flat peer-to-peer, hierarchical, team-based, central-coordinator, and hybrid structures. [S8]

### Finding 3

**Claim**

Hierarchical or supervisor-worker systems use explicit delegation: a supervisor decomposes a goal, routes subtasks to workers or specialists, and aggregates or evaluates their results.

**Confidence:** High

**Why this confidence level**

The mechanism is directly described across several sources. Evidence does not establish that hierarchy is universally superior.

**Evidence**

- The taxonomy guide defines supervisor-worker as hierarchical coordination in which a supervisor decomposes tasks, routes them to specialized agents, and determines whether the task is complete. [S2]
- The travel-planning example shows a manager coordinating flight, hotel, transportation, and activity specialists. [S1]
- The hierarchical design description specifies downward task assignment and upward result aggregation. [S8]

### Finding 4

**Claim**

Decentralized or flat peer-to-peer systems allow agents to communicate without a single controlling supervisor, whereas hybrid systems combine peer interaction with explicit coordination or team structures.

**Confidence:** High

**Why this confidence level**

The distinction is architectural and consistently supported, though comparative performance evidence is limited.

**Evidence**

- The flat architecture is described as a many-to-many network in which all agents are peers and may publish results through direct messaging or a shared bus. [S8]
- The orchestration survey treats decentralized topology as distinct from centralized and hierarchical coordination. [S6]
- The empirical taxonomy and practitioner overview both identify hybrid arrangements as a separate or compositional pattern. [S3] [S4] [S8]

### Finding 5

**Claim**

Graph/workflow, plan-and-execute, and adaptive control are control-flow dimensions that can be layered onto different topologies rather than being mutually exclusive topology families.

**Confidence:** High

**Why this confidence level**

The layered interpretation reconciles taxonomies that classify graph, workflow, and planning at different abstraction levels.

**Evidence**

- The taxonomy guide distinguishes graph topologies and plan-and-execute as collaborative patterns, and identifies brittleness when a fixed plan cannot adapt to changing conditions. [S2]
- The orchestration survey separates topology from dynamic/adaptive control and also treats planning, sequencing, state management, and recovery as distinct mechanisms. [S6]
- The empirical study emphasizes network arrangements, handoffs, and control-flow strategies as reusable design elements. [S4]

### Finding 6

**Claim**

Communication is a foundational system layer involving architecture, communication goals, protocols, message strategies, shared context, and exchanged content.

**Confidence:** High

**Why this confidence level**

Communication is explicitly foregrounded by a dedicated survey and independently appears as a core orchestration mechanism and failure source.

**Evidence**

- The communication-centric survey defines LLM-MAS as protocol-constrained systems organized around communication goals and analyzes both system-level and internal communication. [S7]
- The orchestration survey treats inter-agent communication and context sharing as core mechanisms and distinguishes agent-to-tool from agent-to-agent protocol layers. [S6]
- The retrieved literature identifies divergent interpretations, semantic loss, context growth, and communication inefficiency as recurring problems. [S3] [S4] [S7]

### Finding 7

**Claim**

Specialization, memory, feedback, and evolution are cross-cutting capabilities that can be combined with multiple topologies and workflows.

**Confidence:** High

**Why this confidence level**

The separation of these capabilities from topology is explicit in the surveys and consistent across the accumulated evidence.

**Evidence**

- The survey's five-component workflow includes agent profiles, perception, action, interaction, and evolution, while describing distinct identities and specialized roles. [S5]
- The communication survey describes reasoning, perception, action, and short- and long-term memory as agent components, while analyzing communication separately. [S7]
- The retrieved taxonomies separately identify specialization, memory, reflection, verification, and adaptive control rather than reducing them to one topology. [S2] [S6]

### Finding 8

**Claim**

Quality-control and adversarial patterns include verifier-critic loops, multi-agent debate, judges or synthesizers, and human oversight; these are primarily intended to improve output quality or safety rather than to parallelize subtasks.

**Confidence:** Medium

**Why this confidence level**

The architectural distinction is clear, but the effectiveness of critique or debate depends on evaluator quality, model diversity, and task characteristics; controlled comparative evidence was not retrieved.

**Evidence**

- The taxonomy guide defines debate as competing arguments followed by synthesis or judgment, and verifier-critic as generation, critique, scoring, and revision. [S2]
- The overview states that human oversight and review remain part of many multi-agent workflows and presents cross-agent checking as a reliability mechanism. [S1]
- The accumulated taxonomy distinguishes critique and verification from task-decomposition patterns. [S2] [S5]

### Finding 9

**Claim**

The main open problem is system-level coordination reliability: preventing contradiction, duplication, inconsistent shared state, semantic drift, and unsafe collective behavior while retaining adaptability.

**Confidence:** High

**Why this confidence level**

Multiple surveys, an empirical paper, and an evaluation review converge on these failure classes.

**Evidence**

- The orchestration survey identifies contradiction, duplicated effort, inconsistent shared state, and super-linearly increasing coordination burdens as system-level concerns. [S6]
- The communication survey highlights communication efficiency, security, scalability, and inadequate benchmarking as unresolved challenges. [S7]
- The evaluation review distinguishes miscoordination, conflict, and collusion as multi-agent failure modes, with collusion especially underrepresented. [S9]
- Other sources report supervisor drift, unsurfaced conflicts, plan brittleness, semantic loss, and production reliability limitations. [S2] [S3] [S4]

### Finding 10

**Claim**

Evaluation and safety research currently do not provide a sufficiently broad basis for comparing architectures or covering important threat models.

**Confidence:** Medium

**Why this confidence level**

The quantitative review is self-described as non-comprehensive and is not a peer-reviewed source in the retrieved material, but its conclusion is independently supported by the survey evidence.

**Evidence**

- A review of 32 multi-agent evaluation papers found that 26 measured miscoordination but only 5 measured collusion, and that most did not target a specified real-world AI threat model. [S9]
- The communication survey identifies inadequate benchmarking and security vulnerabilities as current challenges. [S7]
- The accumulated research identifies the lack of common metrics isolating architecture effects on quality, cost, latency, robustness, and safety. [S4] [S5]

### Finding 11

**Claim**

The application landscape spans problem-solving and world simulation, including scientific, industrial, service, security, robotic, and game environments.

**Confidence:** High

**Why this confidence level**

The breadth of application areas is directly supported by the survey and independent case-study evidence.

**Evidence**

- The survey organizes applications into problem-solving and world simulation and cites industrial engineering, scientific experimentation, embodied agents, and gaming. [S5]
- The empirical study reports pilots involving telecommunications security, heritage asset management, and utilities customer service. [S4]
- The overview gives travel planning and continuously updated monitoring as examples of multi-agent applications. [S1]

## Conflicts and Uncertainty

- Sources disagree mainly in abstraction level. Some classify centralized, decentralized, and hierarchical topologies; others list flat, team-based, graph, swarm, debate, verifier-critic, or specialized patterns. These are best interpreted as different layers—topology, control flow, organization, specialization, or quality control—rather than mutually exclusive competing taxonomies. [S2] [S3] [S4] [S6] [S8]
- The taxonomy guide claims that eight patterns cover approximately 95% of production systems and that hierarchical and graph topologies generally earn their cost. The retrieved academic sources do not substantiate those coverage or superiority claims, so they should not be treated as established findings. [S2] [S4] [S5]
- Practitioner sources report strong quantitative gains in accuracy, completion time, semantic-error reduction, ROI, or deployment benefits, but the retrieved excerpts lack sufficient methodological detail for verification. The empirical paper is more cautious and emphasizes unresolved production-maturity limitations. [S1] [S3] [S4]
- The orchestration survey is identified on its page as not peer-reviewed, and the evaluation review is a self-described college-class literature review with a non-comprehensive search. Their quantitative and comparative claims warrant lower confidence than the peer-reviewed survey evidence. [S6] [S9]
- The evidence supports identifying open problems but does not establish which architecture is best for a given task, how many agents are optimal, or when coordination benefits outweigh token, latency, and monitoring costs. [S2] [S4] [S6] [S7]

## Remaining Gaps

- A standardized benchmark suite is needed to compare architectures while controlling for model quality, prompts, tools, domain engineering, agent count, and communication budget.
- The field lacks sufficiently controlled comparisons among centralized, hierarchical, decentralized, graph/workflow, adaptive, debate, and verifier-critic designs.
- Protocols and representations for preserving provenance, authorization, uncertainty, semantic fidelity, and shared-state consistency remain underdeveloped in the retrieved evidence.
- Long-running systems need better fault detection, rollback or recovery, termination, budget control, and human-oversight mechanisms.
- Safety evaluations need broader coverage of collusion, sabotage, privacy, cybersecurity, persuasion, and other threat models outside board-game settings.
- More evidence is needed on production transition: prototype speed and modularity do not by themselves establish reliability, scalability, governance, or economic value.

## Conclusion

The landscape is not a race between a small set of mutually exclusive architectures. It is a compositional design space. A system may be centralized or decentralized in topology, graph-based or plan-based in control flow, specialized in agent roles, protocol-driven in communication, memory-enabled and adaptive, and augmented with verifier-critic or debate loops. Hierarchical supervisor-worker designs are prominent because they provide explicit task decomposition and aggregation, while peer-to-peer designs provide flexible interaction; hybrid systems combine both. The strongest cross-source consensus concerns the importance of communication and the difficulty of system-level coordination. The field's central research agenda is therefore to make multi-agent coordination measurable, semantically reliable, cost-controlled, secure, and governable. Existing evidence maps the design space and its risks, but does not justify universal claims of architectural superiority.

## Sources

- [S1] Multi-agent LLMs in 2026 [+frameworks] — https://www.superannotate.com/blog/multi-agent-llms
- [S2] Agent Architecture Patterns: 2026 Taxonomy Guide — https://www.digitalapplied.com/blog/agent-architecture-patterns-taxonomy-2026
- [S3] LLM Agent Orchestration Patterns: Architectural ... — https://www.c-sharpcorner.com/article/llm-agent-orchestration-patterns-architectural-frameworks-for-managing-complex
- [S4] LLM-Enabled Multi-Agent Systems: Empirical Evaluation and Insights into Emerging Design Patterns & Paradigms — https://arxiv.org/html/2601.03328v1
- [S5] A survey on LLM-based multi-agent systems - Springer Nature — https://link.springer.com/article/10.1007/s44336-024-00009-2
- [S6] LLM-Based Multi-Agent Orchestration: A Survey of ... — https://www.preprints.org/manuscript/202604.2147
- [S7] Beyond Self-Talk: A Communication-Centric Survey of LLM ... — https://arxiv.org/html/2502.14321v3
- [S8] Multi-Agent LLM Systems: Architecture, Communication, and ... — https://samiranama.com/posts/LLM-Based-Multi-Agent-Systems-Architectures-and-Collaboration
- [S9] Survey of Multi-agent LLM Evaluations — LessWrong — https://www.lesswrong.com/posts/tGcLA596E8g3KnphE/survey-of-multi-agent-llm-evaluations
