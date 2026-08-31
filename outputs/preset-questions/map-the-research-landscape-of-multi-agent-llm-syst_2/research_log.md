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

**Unique Sources:** 13

**OpenAI Calls:** 6

**Tavily Calls:** 3

**Started:** 2026-08-31T17:34:30-04:00

**Ended:** 2026-08-31T17:36:01-04:00

**Total Runtime:** 90.32s

---

# Iteration 1

## 1. Search

**Query**

> Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are.

**Purpose:** GENERAL

**Why this query**

This is the user's original research question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S1 — Multi-agent LLMs in 2026 [+frameworks]**
  URL: https://www.superannotate.com/blog/multi-agent-llms
- **S2 — Agent Architecture Patterns: 2026 Taxonomy Guide**
  URL: https://www.digitalapplied.com/blog/agent-architecture-patterns-taxonomy-2026
- **S3 — LLM Agent Orchestration Patterns: Architectural ...**
  URL: https://www.c-sharpcorner.com/article/llm-agent-orchestration-patterns-architectural-frameworks-for-managing-complex
- **S4 — A survey on LLM-based multi-agent systems - Springer Nature**
  URL: https://link.springer.com/article/10.1007/s44336-024-00009-2
- **S5 — How to Build a Multi-Agent Deep Research System with ...**
  URL: https://medium.com/data-science-collective/building-a-multi-agent-deep-research-agent-with-langgraph-203547b5fb12

**Search Duration:** 3.13s

---

## 2. Evidence Processing

- New claim proposals: 9
- Existing claim updates: 0
- New gaps: 5
- Resolved gaps: 0

**Processing Duration:** 21.26s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

LLM-based multi-agent systems commonly comprise multiple specialized agents that communicate and collaborate to solve complex tasks, often using tools, memory, task decomposition, and result aggregation.

- S1 supports (direct): Describes specialized agents assigned distinct roles, tool use and memory, communication, task decomposition, and assembly of a final output.
- S4 supports (direct): Defines LLM-based multi-agent systems as multiple specialized agents with distinct identities that communicate and collaborate toward task objectives.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C2

**Claim**

A useful design taxonomy distinguishes centralized or hierarchical orchestration, decentralized collaboration, specialized role-based systems, hybrid compositions, and competitive or critique-oriented interactions; these categories may overlap rather than form mutually exclusive alternatives.

- S3 supports (direct): Explicitly proposes centralized, decentralized, specialized, and hybrid orchestration categories and discusses their interaction protocols and context management.
- S2 supports (direct): Separates collaborative, competitive, and orchestration-oriented patterns and states that production systems often compose multiple patterns.
- S1 supports (indirect): Provides a concrete role-specialized team coordinated through a manager.
- S2 contradicts (direct): Presents a different four-quadrant taxonomy—single-agent, collaborative multi-agent, competitive multi-agent, and orchestration topology—rather than the four categories in S3.

**Confidence:** HIGH

**Status:** CONFLICTING

### New Claim C3

**Claim**

A manager or supervisor-worker topology routes decomposed subtasks to specialized workers and aggregates their outputs, making it a representative centralized multi-agent architecture.

- S1 supports (direct): Travel-planning example assigns flight, hotel, transportation, and activity subtasks to specialized agents and sequences them through a manager.
- S2 supports (direct): Defines supervisor-worker as a hierarchical pattern in which a supervisor decomposes tasks, routes them to specialized workers, and aggregates results.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C4

**Claim**

Plan-and-execute architectures separate planning from execution, while graph-based orchestration represents dependencies and routes work through explicit workflow nodes; both support decomposition and parallel or staged execution.

- S2 supports (direct): Defines plan-and-execute as a planner producing an ordered plan for an executor and identifies graph topologies as a multi-agent pattern.
- S4 supports (direct): Cites a graph-based multi-agent framework for coordinating complex task dependencies.
- S5 supports (direct): Describes a LangGraph workflow with planning, parallel specialist dispatch, synthesis, gap analysis, citation auditing, writing, and refinement.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C5

**Claim**

Competitive or critique-oriented architectures include multi-agent debate and verifier-critic loops, in which agents challenge, score, or revise outputs to improve reliability or compliance.

- S2 supports (direct): Defines debate as agents presenting opposing positions before synthesis and verifier-critic as generation followed by rubric-based critique and revision.
- S1 supports (indirect): States that agents can check one another's work to reduce mistakes and improve reliability.
- S5 supports (direct): Includes skeptic, citation-audit, and refinement stages in a research workflow.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C6

**Claim**

A workflow-oriented decomposition of LLM-based multi-agent systems includes agent profile, perception, self-action, mutual interaction, and evolution.

- S4 supports (direct): The survey explicitly synthesizes these five components as a general structure for LLM-based multi-agent systems.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C7

**Claim**

Important architectural challenges include semantic or contextual drift during natural-language coordination, interaction-protocol information loss, token and resource scaling, coordination overhead, and failure propagation or insufficient verification.

- S3 supports (direct): Discusses contextual drift, semantic coordination shortfalls, protocol-induced semantic loss, and resource/token optimization problems.
- S2 supports (direct): Lists coordination overhead, supervisor drift, subtask conflicts, plan brittleness, debate convergence, and critic failure modes.
- S4 supports (indirect): States that the survey discusses contemporary challenges and future directions for LLM-based multi-agent systems.
- S5 supports (direct): Uses citation auditing, gap analysis, bounded iterations, and partial finalization to address verification, missing evidence, and runaway cost risks in one research workflow.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C8

**Claim**

A practical deep-research system can combine a classifier, scout, architect, parallel role-specialist agents, synthesis, gap analysis, citation audit, writer, and refiner in a graph, with structural controls such as writer-after-audit and bounded iterations.

- S5 supports (direct): Describes a LangGraph state machine with these stages and explicitly states that the writer runs only after citation auditing and that iteration limits ensure termination.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C9

**Claim**

The supplied sources do not establish a validated universal taxonomy, a reliable ranking of architectural patterns, or general quantitative superiority of multi-agent systems over single-agent baselines.

- S2 contradicts (indirect): Claims that eight patterns cover approximately 95% of production systems and that hierarchical systems usually outperform swarms, but provides no comparative evidence in the supplied excerpt.
- S3 contradicts (indirect): Reports large completion-time, semantic-error, token-cost, and ROI improvements, but the supplied material does not provide enough experimental design or benchmark detail to validate generality.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Gap G1

No standardized, cross-domain empirical comparison is supplied for centralized, decentralized, graph, debate, verifier-critic, and hybrid architectures against single-agent baselines.

### New Gap G2

The sources do not define a consensus taxonomy or formal design graph that cleanly specifies how the proposed categories and patterns compose, overlap, or transition from one another.

### New Gap G3

Evidence is insufficient on how to evaluate semantic drift, coordination failures, hallucination reduction, citation quality, cost, latency, and reliability consistently across multi-agent systems.

### New Gap G4

The supplied material identifies token scaling, protocol semantic loss, failure propagation, and human oversight as concerns but does not provide general mitigation guarantees or validated resource-allocation methods.

### New Gap G5

Framework support and implementation guidance are mentioned, but there is no systematic evidence comparing LangGraph, AutoGen, CrewAI, or other frameworks under matched workloads and operational constraints.

---

## 4. Current Research State

- Claims: 9
- Supported: 8
- Weak: 0
- Conflicting: 1
- Insufficient Evidence: 0
- Open Gaps: 5
- Remaining Searches: 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** GAP G2

**Why**

The report’s central taxonomy and design graph remain weakly grounded because the supplied sources offer conflicting category schemes. A consensus taxonomy or systematic mapping would materially improve the answer.

**Next Search**

> systematic survey taxonomy multi-agent LLM architectures centralized decentralized hierarchical peer-to-peer debate graph orchestration design patterns


---

# Iteration 2

## 1. Search

**Query**

> systematic survey taxonomy multi-agent LLM architectures centralized decentralized hierarchical peer-to-peer debate graph orchestration design patterns

**Target:** G2

**Purpose:** GENERAL

**Why this query**

The report’s central taxonomy and design graph remain weakly grounded because the supplied sources offer conflicting category schemes. A consensus taxonomy or systematic mapping would materially improve the answer.

5 result(s) retrieved; 3 new unique source(s) added.

- **S6 — LLM-Based Multi-Agent Orchestration: A Survey of ...**
  URL: https://www.preprints.org/manuscript/202604.2147
- **S7 — LLM-Based Multi-Agent Orchestration: A Survey of Frameworks, Communication Protocols, and Emerging Patterns**
  URL: https://www.mdpi.com/1999-5903/18/6/326
- **S8 — Multi-Agent Architectures**
  URL: https://www.emergentmind.com/topics/multi-agent-architectures

**Search Duration:** 2.91s

---

## 2. Evidence Processing

- New claim proposals: 2
- Existing claim updates: 4
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 12.38s

---

## 3. Ledger Updates

### New Claim C10

**Claim**

A recent orchestration survey proposes a taxonomy with three coordination topologies—centralized, decentralized, and hierarchical—crossed by an optional dynamic/adaptive control axis.

- S6 supports (direct): The survey abstract explicitly proposes a three-topology, one-adaptivity taxonomy consisting of centralized, decentralized, and hierarchical coordination, with dynamic/adaptive control as an additional axis.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C11

**Claim**

Multi-agent orchestration can be analyzed through mechanisms for task decomposition and allocation, inter-agent communication and context sharing, state management and persistence, control-flow sequencing, and error detection and recovery.

- S6 supports (direct): S6 explicitly identifies these five interrelated mechanisms as the scope of orchestration.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

LLM-based multi-agent systems commonly comprise multiple specialized agents that communicate and collaborate to solve complex tasks, often using tools, memory, task decomposition, and result aggregation.

- S6 supports (direct): Defines LLM-based multi-agent orchestration as specialized agents assuming distinct roles, exchanging information through structured protocols, and coordinating actions toward tasks beyond a single agent.
- S8 supports (direct): Characterizes multi-agent architectures as multiple autonomous agents interacting and collaborating on tasks that a single agent may not efficiently handle.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

A useful design taxonomy distinguishes centralized or hierarchical orchestration, decentralized collaboration, specialized role-based systems, hybrid compositions, and competitive or critique-oriented interactions; these categories may overlap rather than form mutually exclusive alternatives.

- S6 supports (direct): Proposes centralized, decentralized, and hierarchical coordination topologies, optionally augmented by a dynamic/adaptive axis.
- S8 supports (direct): Describes hierarchical, decentralized, hybrid, and publish–subscribe archetypes and distinguishes organizational hierarchy from collaboration style as taxonomy axes.
- S6 contradicts (direct): Uses a three-topology taxonomy with adaptivity as an axis, which differs from the category set in C2 and reinforces that no single canonical partition is established.
- S8 contradicts (direct): Presents a four-archetype taxonomy including publish–subscribe and hybrid designs, rather than treating the categories in C2 as a single fixed set.

**Confidence:** HIGH → HIGH

**Status:** CONFLICTING → CONFLICTING

### Updated Claim C7

**Claim**

Important architectural challenges include semantic or contextual drift during natural-language coordination, interaction-protocol information loss, token and resource scaling, coordination overhead, and failure propagation or insufficient verification.

- S6 supports (direct): Identifies orchestration challenges involving coordination, state management, control flow, error recovery, scalability, and security; it also notes that interaction channels and coordination burdens grow super-linearly with agent count.
- S8 supports (direct): Describes communication-overhead controls, dynamic rescheduling, feedback loops, failure recovery, and resource-aware task allocation as architectural concerns and mechanisms.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C9

**Claim**

The supplied sources do not establish a validated universal taxonomy, a reliable ranking of architectural patterns, or general quantitative superiority of multi-agent systems over single-agent baselines.

- S6 supports (direct): Proposes a taxonomy and evaluation framework and reports framework comparisons, but the supplied excerpt does not provide sufficient standardized comparative results to establish universal rankings or superiority.
- S8 supports (indirect): Reports several architecture-specific quantitative improvements, but these are tied to particular systems and tasks rather than a universal cross-architecture comparison.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 11
- Supported: 10
- Weak: 0
- Conflicting: 1
- Insufficient Evidence: 0
- Open Gaps: 5
- Remaining Searches: 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** GAP G2

**Why**

A focused search could materially strengthen the report’s core unresolved issue: whether a consensus taxonomy or compositional design graph exists beyond the conflicting frameworks already found.

**Next Search**

> multi-agent LLM systems unified taxonomy compositional architecture design space graph centralized decentralized hierarchical debate planner executor workflow survey


---

# Iteration 3

## 1. Search

**Query**

> multi-agent LLM systems unified taxonomy compositional architecture design space graph centralized decentralized hierarchical debate planner executor workflow survey

**Target:** G2

**Purpose:** GENERAL

**Why this query**

A focused search could materially strengthen the report’s core unresolved issue: whether a consensus taxonomy or compositional design graph exists beyond the conflicting frameworks already found.

5 result(s) retrieved; 5 new unique source(s) added.

- **S9 — Multi-Agent Debate Strategies: Survey, Taxonomy, and Challenges**
  URL: https://arxiv.org/html/2607.26212v1
- **S10 — Multi-Agent LLM Systems: Architecture, Communication, and ...**
  URL: https://samiranama.com/posts/LLM-Based-Multi-Agent-Systems-Architectures-and-Collaboration
- **S11 — A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges | Semantic Scholar**
  URL: https://www.semanticscholar.org/paper/A-survey-on-LLM-based-multi-agent-systems%3A-and-Li-Wang/fc8ce12d6186ddaa797e2b36d5e8eb7921425308
- **S12 — Multi-Agent Systems and Their Evolution: A Comparative Survey[v1] | Preprints.org**
  URL: https://www.preprints.org/manuscript/202606.0358
- **S13 — A field guide to multi-agent architectures | by Tituslhy**
  URL: https://medium.com/mitb-for-all/a-field-guide-to-multi-agent-architectures-f6f8c689c406

**Search Duration:** 2.62s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 6
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 21.99s

---

## 3. Ledger Updates

### New Claim C12

**Claim**

A systematic survey of multi-agent debate characterizes MAD configurations along three dimensions: debate participants, interaction mechanisms, and agreement protocols; it reports that static fully connected topologies, verbatim exchange, short-term memory, and voting resolution are prevalent by convention rather than validated comparison.

- S9 supports (direct): The survey of 141 primary studies explicitly derives a three-dimensional MAD taxonomy and reports convergence on a narrow conventional design pattern without systematic comparison.

**Confidence:** HIGH

**Status:** SUPPORTED

### Updated Claim C2

**Claim**

A useful design taxonomy distinguishes centralized or hierarchical orchestration, decentralized collaboration, specialized role-based systems, hybrid compositions, and competitive or critique-oriented interactions; these categories may overlap rather than form mutually exclusive alternatives.

- S9 supports (direct): Provides an additional multidimensional taxonomy for debate architectures and emphasizes that debate design dimensions interact, supporting taxonomy axes that overlap rather than a single mutually exclusive partition.
- S10 supports (direct): Organizes architectures across flat, hierarchical, team-based, central-coordinator, and hybrid patterns, reinforcing recurring but non-identical organizational categories.
- S13 supports (direct): Describes hierarchical, explicit workflow, swarm, blackboard, and adversarial architectures as different answers to coordination and control, supporting a landscape of composable patterns rather than one canonical partition.

**Confidence:** HIGH → HIGH

**Status:** CONFLICTING → CONFLICTING

### Updated Claim C3

**Claim**

A manager or supervisor-worker topology routes decomposed subtasks to specialized workers and aggregates their outputs, making it a representative centralized multi-agent architecture.

- S10 supports (direct): Describes hierarchical systems in which supervisors delegate to managers or specialists and integrate results flowing back up the hierarchy.
- S13 supports (direct): Characterizes a supervisor as an agent that delegates to specialist agents, potentially across multiple nested levels, and identifies the supervisor as a routing bottleneck and single point of failure.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

Plan-and-execute architectures separate planning from execution, while graph-based orchestration represents dependencies and routes work through explicit workflow nodes; both support decomposition and parallel or staged execution.

- S13 supports (direct): Contrasts supervisor-driven delegation with explicit workflows whose nodes, edges, branches, convergence points, concurrency, and termination conditions are defined directly; it describes fan-out and downstream consolidation.
- S10 supports (indirect): Presents architectural patterns with explicit planning, execution, evaluation, and message-flow functions, including parallel collaboration in some configurations.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

Competitive or critique-oriented architectures include multi-agent debate and verifier-critic loops, in which agents challenge, score, or revise outputs to improve reliability or compliance.

- S9 supports (direct): Reviews 141 MAD studies in which agents exchange arguments, critique outputs, and iteratively converge; it also identifies participant, interaction, and agreement-protocol dimensions.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C7

**Claim**

Important architectural challenges include semantic or contextual drift during natural-language coordination, interaction-protocol information loss, token and resource scaling, coordination overhead, and failure propagation or insufficient verification.

- S9 supports (direct): Reports that MAD has roughly a dozen interacting design decisions, that implicit choices make cross-study comparison unreliable, and that cost-aware benchmarking and automated tuning remain future work.
- S10 supports (direct): Identifies communication-protocol design, memory sharing, coordination, and supervisor bottlenecks or single points of failure as practical concerns.
- S12 supports (direct): Highlights explainability, security, computational cost, and human-in-the-loop requirements as design issues for MAS frameworks.
- S13 supports (direct): Identifies supervisor routing failure, communication and recovery responsibilities in explicit workflows, and the need to deliberately design control flow as architectural weaknesses or concerns.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C9

**Claim**

The supplied sources do not establish a validated universal taxonomy, a reliable ranking of architectural patterns, or general quantitative superiority of multi-agent systems over single-agent baselines.

- S9 supports (direct): States that MAD research is fragmented, terminology and design dimensions are inconsistently consolidated, and cross-study comparison is unreliable when design decisions are implicit.
- S13 supports (direct): States that there are no official statistics on architecture prevalence and presents practical pattern guidance rather than a validated universal ranking.
- S12 supports (indirect): Proposes comparative framework criteria and case studies, but the supplied excerpt does not provide standardized results sufficient to establish universal superiority across architectures or domains.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 12
- Supported: 11
- Weak: 0
- Conflicting: 1
- Insufficient Evidence: 0
- Open Gaps: 5
- Remaining Searches: 0

---

## 5. Research Decision

**Decision:** Stop researching.

**Origin:** BUDGET_STOP

**Why**

The maximum research iteration budget was reached.

**Stop Reason:** max_iterations


---

# Final Research Decision

**Stop Reason:** max_iterations

**Remaining Uncertainty**

- G1: No standardized, cross-domain empirical comparison is supplied for centralized, decentralized, graph, debate, verifier-critic, and hybrid architectures against single-agent baselines.
- G2: The sources do not define a consensus taxonomy or formal design graph that cleanly specifies how categories compose, overlap, or transition.
- G3: Evidence is insufficient for consistent evaluation of semantic drift, coordination failures, hallucination reduction, citation quality, cost, latency, and reliability.
- G4: The material identifies scaling, protocol loss, failure propagation, and human oversight concerns but provides no general mitigation guarantees or validated resource-allocation methods.
- G5: No matched-workload comparison of LangGraph, AutoGen, CrewAI, or other frameworks is supplied.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 8.66s |
| Evidence Processing | 3 | 55.62s |
| Research Decision | 2 | 4.61s |
| Report Generation | 1 | 21.43s |
| Total Run | — | 90.32s |
