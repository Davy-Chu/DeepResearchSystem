# Research Run Log

## Run Summary

**System Version:** evidence-ledger-v1

**Research Question**

Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 15

**OpenAI Calls:** 6

**Tavily Calls:** 3

**Started:** 2026-08-30T18:28:53-04:00

**Ended:** 2026-08-30T18:30:22-04:00

**Total Runtime:** 89.03s

---

# Iteration 1

## 1. Search

**Query**

> Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are.

**Why this query**

This is the user's original research question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S1 — Multi-agent LLMs in 2026 [+frameworks]**
  URL: https://www.superannotate.com/blog/multi-agent-llms
- **S2 — LLM Architectures in Action: Building a Multi-Agent Research Assistant with LangChain and LangGraph**
  URL: https://medium.com/infinitgraph/llm-architectures-in-action-building-a-multi-agent-research-assistant-with-langchain-and-langgraph-1627f6770101
- **S3 — From RAG to Multi-Agent Systems: A Survey of Modern Approaches in LLM Development**
  URL: https://www.preprints.org/manuscript/202502.0406
- **S4 — A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges**
  URL: https://link.springer.com/article/10.1007/s44336-024-00009-2
- **S5 — LLM Agent Orchestration Patterns: Architectural ...**
  URL: https://www.c-sharpcorner.com/article/llm-agent-orchestration-patterns-architectural-frameworks-for-managing-complex

**Search Duration:** 3.01s

---

## 2. Evidence Processing

- New claim proposals: 6
- Existing claim updates: 0
- New gaps: 4
- Resolved gaps: 0

**Processing Duration:** 16.70s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

A useful systems-level workflow model for LLM-based multi-agent systems consists of five components: agent profile, perception, self-action, mutual interaction, and evolution.

- S4 supports (direct): The survey explicitly presents a unified five-component structure for LLM-based multi-agent-system workflows.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C2

**Claim**

Multi-agent LLM systems commonly decompose a high-level task into subtasks, assign them to specialized agents, allow agents to reason and use tools or memory, exchange information, and assemble a final result.

- S1 supports (direct): The described workflow begins with task decomposition and role-based assignment, followed by agent reasoning, planning, tool and memory use, communication, and result aggregation.
- S3 supports (indirect): The survey abstract characterizes multi-agent architectures as a way to handle intricate tasks through collaborative efforts and discusses stateful multi-agent applications.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C3

**Claim**

Centralized, decentralized, specialized, and hybrid orchestration are four proposed architectural categories for organizing LLM-agent collaboration.

- S5 supports (direct): The article explicitly introduces a four-category taxonomy: centralized, decentralized, hybrid, and specialized.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C4

**Claim**

The architectural space includes both sequential delegation or hand-off patterns and more collaborative interaction patterns, and frameworks such as CrewAI, LangChain/LangGraph, and AutoGen are presented as implementation options.

- S2 supports (direct): The article's structure explicitly lists Hand-off Pattern and Collaborative Filtering under multi-agent patterns, and lists CrewAI, LangChain, and Microsoft AutoGen as frameworks; its title documents a LangChain/LangGraph implementation.
- S3 supports (direct): The survey abstract identifies LangGraph as a tool for implementing stateful, multi-agent LLM applications.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C5

**Claim**

Coordination reliability is an open problem because natural-language interaction can produce contextual drift, semantic misinterpretation, protocol-related information loss, and compounding undetected errors.

- S5 supports (direct): The article identifies contextual drift, behavioral complexity, and interaction-protocol semantic loss as coordination shortfalls in LLM-agent networks.
- S4 supports (indirect): The survey states that it discusses contemporary challenges and future directions for LLM-based multi-agent systems, supporting the framing of coordination as an active research area.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C6

**Claim**

The supplied literature frames multi-agent systems as potentially useful for complex-task problem solving and world simulation, with claimed benefits including scalability, parallelism, extended-context handling, and collaborative error checking.

- S4 supports (direct): The survey identifies problem-solving and world simulation as principal application areas and describes multi-agent systems as a pathway for complex autonomous systems.
- S1 supports (direct): The overview claims benefits over single-agent systems in complex-task decomposition, extended-context processing, parallel multitasking, and peer checking.
- S3 supports (direct): The survey abstract associates multi-agent architectures with intricate-task handling, scalability, and collaborative mitigation of hallucinations.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Gap G1

No supplied source provides a consistent design graph that formally relates centralized, decentralized, specialized, hybrid, hand-off, and collaborative patterns or defines when one pattern should be selected over another.

### New Gap G2

Comparative empirical evidence is insufficient: the sources do not establish standardized benchmarks, workloads, cost/latency measures, or reproducible comparisons among orchestration patterns and frameworks.

### New Gap G3

The evidence does not adequately specify evaluation methods for coordination failures, hallucination reduction, semantic drift, protocol information loss, or robustness as agent count and task complexity increase.

### New Gap G4

The supplied excerpts do not establish the detailed infrastructure dimensions of multi-agent systems, including shared state and memory design, communication protocols, agent lifecycle/evolution, permissions, and human oversight mechanisms.

---

## 4. Current Research State

- Claims: 6
- Supported: 6
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 4
- Remaining Searches: 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Target:** GAP G1

**Why**

The report’s central design graph is not yet grounded in a coherent scholarly taxonomy relating orchestration patterns or explaining pattern selection.

**Next Search**

> scholarly survey taxonomy design space multi-agent LLM architectures centralized decentralized hierarchical peer-to-peer handoff collaboration orchestration pattern selection


---

# Iteration 2

## 1. Search

**Query**

> scholarly survey taxonomy design space multi-agent LLM architectures centralized decentralized hierarchical peer-to-peer handoff collaboration orchestration pattern selection

**Why this query**

The report’s central design graph is not yet grounded in a coherent scholarly taxonomy relating orchestration patterns or explaining pattern selection.

5 result(s) retrieved; 5 new unique source(s) added.

- **S6 — LLM-Based Multi-Agent Orchestration: A Survey of ...**
  URL: https://www.preprints.org/manuscript/202604.2147
- **S7 — Multi-Agent Topology Taxonomy: Centralized, Decentralized - AgentPatterns.ai**
  URL: https://agentpatterns.ai/patterns/multi-agent/multi-agent-topology-taxonomy
- **S8 — Survey Tracks the Evolution from Language Models to Autonomous AI Agents**
  URL: https://bioengineer.org/survey-tracks-the-evolution-from-language-models-to-autonomous-ai-agents
- **S9 — A Taxonomy of Hierarchical Multi-Agent Systems: Design Patterns, Coordination Mechanisms, and Industrial Applications**
  URL: https://arxiv.org/html/2508.12683v1
- **S10 — Agent Architecture Patterns: 2026 Taxonomy Guide**
  URL: https://www.digitalapplied.com/blog/agent-architecture-patterns-taxonomy-2026

**Search Duration:** 2.26s

---

## 2. Evidence Processing

- New claim proposals: 6
- Existing claim updates: 3
- New gaps: 3
- Resolved gaps: 0

**Processing Duration:** 21.57s

---

## 3. Ledger Updates

### New Claim C7

**Claim**

S6 proposes a taxonomy with three coordination topologies—centralized, decentralized, and hierarchical—plus an optional dynamic/adaptive control axis.

- S6 supports (direct): The survey abstract explicitly proposes a three-topology taxonomy consisting of centralized, decentralized, and hierarchical coordination, with dynamic/adaptive control as an additional axis.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C8

**Claim**

The supplied sources use non-uniform architectural taxonomies: centralized/decentralized/hybrid categories, hierarchical multi-agent dimensions, and a centralized/decentralized/hierarchical topology scheme with adaptivity are all presented as distinct organizational lenses.

- S5 supports (direct): S5 presents centralized, decentralized, hybrid, and specialized categories.
- S6 supports (direct): S6 proposes centralized, decentralized, and hierarchical topologies plus an adaptive axis.
- S9 supports (direct): S9 characterizes hierarchical systems using five dimensions: control hierarchy, information flow, role/task delegation, temporal layering, and communication structure.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C9

**Claim**

Coordination topology can be treated as a design-selection variable associated with different task characteristics: centralized coordination for sequential dependencies or shared global state, decentralized coordination for independent subtasks, and hybrid coordination for phased workflows with intra-phase parallelism and inter-phase dependencies.

- S7 supports (direct): S7 directly maps task characteristics to centralized, decentralized, and hybrid topologies and describes their operational definitions.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C10

**Claim**

LLM multi-agent orchestration is described as involving task decomposition/allocation, inter-agent communication and context sharing, state persistence, control-flow sequencing, and error detection/recovery.

- S6 supports (direct): S6 explicitly enumerates five interrelated orchestration mechanisms: task decomposition and allocation, communication/context sharing, state management and persistence, control-flow sequencing, and error detection/recovery.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C11

**Claim**

The interaction and debugging burden of multi-agent systems can grow super-linearly with agent count because the number of pairwise interaction channels increases as the system grows.

- S6 supports (direct): S6 gives the examples of 5 agents yielding 10 pairwise channels and 10 agents yielding 45, and characterizes debugging, monitoring, and testing burdens as increasing super-linearly.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C12

**Claim**

S6 characterizes MCP as an agent-to-tool protocol layer and A2A as an agent-to-agent protocol layer, with ACP–A2A merger activity indicating protocol convergence and ANP addressing decentralized discovery.

- S6 supports (direct): The abstract explicitly describes MCP and A2A as complementary layers, mentions ACP–A2A protocol convergence, and identifies ANP with decentralized discovery.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C4

**Claim**

The architectural space includes both sequential delegation or hand-off patterns and more collaborative interaction patterns, and frameworks such as CrewAI, LangChain/LangGraph, and AutoGen are presented as implementation options.

- S6 supports (direct): S6 compares LangGraph, CrewAI, AutoGen/Microsoft Agent Framework, and OpenAI Agents SDK and frames framework choice within orchestration design.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

Coordination reliability is an open problem because natural-language interaction can produce contextual drift, semantic misinterpretation, protocol-related information loss, and compounding undetected errors.

- S6 supports (direct): S6 identifies coordination failures such as contradiction, duplicated effort, inconsistent shared state, and super-linearly increasing debugging and testing burdens as central orchestration concerns.
- S7 supports (direct): S7 lists topology-specific failures including context saturation, single points of failure, coordination storms, conflicting edits, lack of global coherence, self-verification bias, doom loops, and context blindness.
- S9 supports (direct): S9 identifies explainability, scalability, and safe integration of LLM agents into hierarchical systems as open challenges.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C3

**Claim**

Centralized, decentralized, specialized, and hybrid orchestration are four proposed architectural categories for organizing LLM-agent collaboration.

- S7 supports (direct): S7 independently describes centralized, decentralized, and hybrid topology categories and relates them to coordination choices.
- S9 supports (direct): S9 provides a dedicated hierarchical taxonomy and treats hierarchy as an architectural organization with distinct coordination dimensions.
- S6 contradicts (indirect): S6 uses a different top-level taxonomy—centralized, decentralized, and hierarchical topologies with an adaptive axis—rather than the four-category scheme in C3, demonstrating that the category boundaries are not settled.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### New Gap G5

The relationship between S6's hierarchical topology, S7's hybrid topology, S9's multidimensional hierarchy, and the specialized category in C3 remains underspecified; the evidence does not establish a canonical mapping or whether these are orthogonal dimensions versus competing top-level categories.

### New Gap G6

S6 mentions a six-dimension evaluation framework for coordination quality and published benchmarks, but the supplied excerpt does not specify the dimensions, benchmark tasks, metrics, datasets, or results needed to assess reproducibility and comparative validity.

### New Gap G7

The supplied evidence identifies MCP, A2A, ACP, and ANP roles but does not provide protocol specifications, interoperability experiments, security analyses, or evidence about how protocol choices affect coordination reliability and cost.

---

## 4. Current Research State

- Claims: 12
- Supported: 12
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 7
- Remaining Searches: 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Target:** GAP G1

**Why**

The central design-graph gap remains unresolved, especially how topology, hierarchy, specialization, hand-off, and collaboration relate as orthogonal or competing dimensions.

**Next Search**

> survey design space taxonomy multi-agent LLM architectures topology hierarchy specialization handoff collaboration orthogonal dimensions architectural pattern selection


---

# Iteration 3

## 1. Search

**Query**

> survey design space taxonomy multi-agent LLM architectures topology hierarchy specialization handoff collaboration orthogonal dimensions architectural pattern selection

**Why this query**

The central design-graph gap remains unresolved, especially how topology, hierarchy, specialization, hand-off, and collaboration relate as orthogonal or competing dimensions.

5 result(s) retrieved; 5 new unique source(s) added.

- **S11 — Large Language Model Agents: A Comprehensive Survey on Architectures, Capabilities, and Applications**
  URL: https://www.preprints.org/manuscript/202512.2119
- **S12 — A Taxonomy of Hierarchical Multi-Agent Systems: Design Patterns, Coordination Mechanisms, and Industrial Applications**
  URL: https://arxiv.org/html/2508.12683
- **S13 — Multi-Agent LLM Systems: Architecture, Communication, and Coordination | Samira Ghodratnama**
  URL: https://samiranama.com/posts/LLM-Based-Multi-Agent-Systems-Architectures-and-Collaboration
- **S14 — Choosing the Right Multi-Agent Architecture - LangChain**
  URL: https://www.langchain.com/blog/choosing-the-right-multi-agent-architecture
- **S15 — Multi-Agent AI Architecture: Patterns for Enterprise ...**
  URL: https://www.augmentcode.com/guides/multi-agent-ai-architecture-patterns-enterprise

**Search Duration:** 2.18s

---

## 2. Evidence Processing

- New claim proposals: 4
- Existing claim updates: 5
- New gaps: 2
- Resolved gaps: 0

**Processing Duration:** 19.29s

---

## 3. Ledger Updates

### New Claim C13

**Claim**

S11 presents a cross-cutting taxonomy of LLM agents with four categories: reasoning-enhanced, tool-augmented, multi-agent, and memory-augmented agents; multi-agent systems are therefore positioned as one agent capability/architecture category alongside reasoning, tools, and memory.

- S11 supports (direct): The preprint abstract explicitly organizes LLM agents into reasoning-enhanced, tool-augmented, multi-agent, and memory-augmented categories.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C14

**Claim**

Hierarchical multi-agent systems can be analyzed along five dimensions: control hierarchy, information flow, role and task delegation, temporal layering, and communication structure.

- S12 supports (direct): S12 explicitly proposes a five-axis taxonomy for hierarchical multi-agent systems covering control, information, delegation, temporal, and communication dimensions.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C15

**Claim**

Subagents, skills, handoffs, and routers are presented as four foundational application patterns distinguished by coordination, state management, and sequencing; subagents and routers emphasize centralized or parallel dispatch, while handoffs support stateful sequential transitions.

- S14 supports (direct): The LangChain article explicitly defines subagents, skills, handoffs, and routers and describes their respective orchestration, state, and execution properties.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C16

**Claim**

A hub-spoke architecture routes communication through one orchestrator, producing a star topology with centralized state and a hub single-point-of-failure; the supplied enterprise guide characterizes its coordination edge count as linear in the number of workers.

- S15 supports (direct): S15 defines hub-spoke as a central hub dispatching to specialists, reports a star graph with 2n directed edges, centralized state, and hub-centered failure risk.

**Confidence:** LOW

**Status:** WEAK

### Updated Claim C3

**Claim**

Centralized, decentralized, specialized, and hybrid orchestration are four proposed architectural categories for organizing LLM-agent collaboration.

- S13 supports (direct): S13 describes flat peer-to-peer, hierarchical, team-based, central-coordinator, and hybrid patterns, adding another overlapping taxonomy of collaboration architectures.
- S14 supports (direct): S14 identifies subagents, skills, handoffs, and routers as foundational application patterns, further demonstrating that architectural taxonomies depend on the chosen abstraction level.
- S15 supports (direct): S15 presents hub-spoke, mesh, and hierarchical patterns as canonical enterprise topologies.
- S13 contradicts (indirect): S13 uses a five-pattern scheme rather than C3's four categories, indicating that the categories are not canonical or mutually exclusive.
- S14 contradicts (indirect): S14 uses a different pattern vocabulary, including skills, handoffs, and routers, so C3's categories do not exhaust the supplied architectural lenses.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

Coordination reliability is an open problem because natural-language interaction can produce contextual drift, semantic misinterpretation, protocol-related information loss, and compounding undetected errors.

- S12 supports (direct): S12 identifies explainability, scalability, and safe integration of learning-based and LLM agents into layered systems as open challenges, and notes hierarchy's efficiency-versus-robustness trade-off.
- S13 supports (direct): S13 emphasizes robust communication protocols and memory sharing as prerequisites for collective multi-agent behavior and notes that flat many-to-many designs require careful protocol design.
- S15 supports (direct): S15 describes overloaded hubs, error-amplifying meshes, and drifting deep hierarchies as architecture-related failure modes.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C8

**Claim**

The supplied sources use non-uniform architectural taxonomies: centralized/decentralized/hybrid categories, hierarchical multi-agent dimensions, and a centralized/decentralized/hierarchical topology scheme with adaptivity are all presented as distinct organizational lenses.

- S11 supports (direct): S11 supplies a different, cross-cutting taxonomy that places multi-agent systems alongside reasoning-, tool-, and memory-augmented agents.
- S13 supports (direct): S13 distinguishes flat, hierarchical, team-based, central, and hybrid patterns by roles and message flows.
- S14 supports (direct): S14 distinguishes subagents, skills, handoffs, and routers by coordination and state-management behavior.
- S15 supports (direct): S15 organizes enterprise architectures as hub-spoke, mesh, and hierarchical topologies with different state and failure models.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C9

**Claim**

Coordination topology can be treated as a design-selection variable associated with different task characteristics: centralized coordination for sequential dependencies or shared global state, decentralized coordination for independent subtasks, and hybrid coordination for phased workflows with intra-phase parallelism and inter-phase dependencies.

- S12 supports (direct): S12 links hierarchy to scalability, layered abstraction, delegated decision-making, and structured conflict resolution while acknowledging robustness trade-offs.
- S14 supports (direct): S14 recommends centralized subagents for distinct domains and context isolation, handoffs for sequential stateful workflows, and routers for parallel dispatch and synthesis.
- S15 supports (direct): S15 associates hub-spoke with centralized auditability and isolated worker failures, and mesh with different coordination and failure characteristics.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C11

**Claim**

The interaction and debugging burden of multi-agent systems can grow super-linearly with agent count because the number of pairwise interaction channels increases as the system grows.

- S15 supports (indirect): S15 contrasts linear edge growth for hub-spoke with mesh and hierarchy failure/coordination concerns, providing an additional topology-level account of how interaction structure affects system burden.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### New Gap G8

The supplied sources now provide several pattern vocabularies and qualitative selection heuristics, but do not establish a normalized mapping between capability-level categories, topologies, routing patterns, state models, and role hierarchies for a single visual design graph.

### New Gap G9

Claims about hub, mesh, and hierarchical failure modes and complexity lack independent, reproducible measurements comparing observability, latency, cost, robustness, and failure isolation as agent populations and communication edges scale.

---

## 4. Current Research State

- Claims: 16
- Supported: 15
- Weak: 1
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 9
- Remaining Searches: 0

---

## 5. Research Decision

**Decision:** Stop researching.

**Why**

The maximum research iteration budget was reached.

**Stop Reason:** max_iterations


---

# Final Research Decision

**Stop Reason:** max_iterations

**Remaining Uncertainty**

- No supplied source provides a formal, normalized design graph relating centralized, decentralized, specialized, hybrid, handoff, collaborative, hierarchical, routing, and state-management patterns or defines when one should be selected.
- Comparative empirical evidence is insufficient: standardized benchmarks, workloads, cost and latency measures, and reproducible comparisons among architectures and frameworks are not supplied.
- Evaluation methods for coordination failures, hallucination reduction, semantic drift, protocol information loss, and robustness under increasing agent count or task complexity remain unspecified.
- The supplied excerpts do not adequately specify shared-state and memory architectures, communication protocols, agent lifecycle or evolution, permissions, or human-oversight mechanisms.
- The supplied taxonomy claims do not establish whether the dimensions of hierarchy, topology, routing, capability, and state are orthogonal, nested, or mutually exclusive.
- Protocol claims about MCP, A2A, ACP, and ANP lack supplied specifications, interoperability experiments, security analyses, and evidence of effects on reliability or cost.
- Claims about hub, mesh, and hierarchical failure modes and complexity lack independent reproducible measurements of observability, latency, cost, robustness, and failure isolation as systems scale.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 7.44s |
| Evidence Processing | 3 | 57.57s |
| Research Decision | 2 | 4.25s |
| Report Generation | 1 | 19.76s |
| Total Run | — | 89.03s |
