# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are.

**Status:** Completed

**Stop Reason:** sufficient_evidence

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 2 / 3

**Unique Sources:** 9

**OpenAI Calls:** 3

**Tavily Calls:** 2

**Started:** 2026-08-31T17:01:00-04:00

**Ended:** 2026-08-31T17:02:22-04:00

**Total Runtime:** 81.65s

---

# Iteration 1

## 1. Search

**Query**

> Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are.

**Why this query**

This is the user's original research question.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S1 — Multi-agent LLMs in 2026 [+frameworks]**
  URL: https://www.superannotate.com/blog/multi-agent-llms
- **S2 — Agent Architecture Patterns: 2026 Taxonomy Guide**
  URL: https://www.digitalapplied.com/blog/agent-architecture-patterns-taxonomy-2026
- **S3 — LLM Agent Orchestration Patterns: Architectural ...**
  URL: https://www.c-sharpcorner.com/article/llm-agent-orchestration-patterns-architectural-frameworks-for-managing-complex
- **S4 — LLM-Enabled Multi-Agent Systems: Empirical Evaluation and Insights into Emerging Design Patterns & Paradigms**
  URL: https://arxiv.org/html/2601.03328v1
- **S5 — A survey on LLM-based multi-agent systems - Springer Nature**
  URL: https://link.springer.com/article/10.1007/s44336-024-00009-2

**Search Duration:** 3.33s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

LLM-based multi-agent systems can be organized as networks of specialized agents that divide complex tasks, communicate intermediate results, act through tools/environments, and evolve through feedback or reflection.

**Confidence:** High

**Why this confidence level**

The central decomposition-and-interaction model is directly supported by an academic survey and a separate empirical paper, with consistent practitioner description.

**Evidence**

- The survey defines a unified MAS workflow with five components: profile, perception, self-action, mutual interaction, and evolution. It characterizes MAS as multiple specialized agents with distinct identities that communicate and collaborate toward objectives. [S5]
- The 2026 empirical paper describes MAS as specialist agents arranged in a network, with task division and handoffs between agents; it identifies orchestration, communication mechanisms, and control flow as core architectural components. [S4]
- The practitioner overview describes task decomposition, role-specialized agents, tool use, shared information, and final result aggregation. [S1]

#### Finding 2

**Claim**

A useful architectural taxonomy spans centralized/hierarchical orchestration, decentralized collaboration, specialized modular agents, and hybrid compositions.

**Confidence:** Medium

**Why this confidence level**

The categories are directly stated, but the retrieved excerpt does not provide the full formal definitions or comparative evaluation of each category. S3 is a practitioner-style article with unsupported quantitative claims, so it should not be treated as strong validation.

**Evidence**

- The empirical paper explicitly formalizes orchestration patterns around agent networks, communication, and control flow, and presents centralized, decentralized, hybrid, and specialized categories. [S3] [S4]
- The survey's workflow components provide a complementary functional taxonomy: agent profile, perception, action, interaction, and evolution. [S5]

#### Finding 3

**Claim**

Hierarchical supervisor-worker systems are a major pattern: a coordinator decomposes a goal, routes subtasks to specialized workers, and aggregates or validates their outputs.

**Confidence:** Medium

**Why this confidence level**

The pattern is clearly described across sources, but the claim that it is generally superior in production is not independently established by the retrieved evidence.

**Evidence**

- The taxonomy guide defines supervisor-worker as a hierarchical system in which a supervisor decomposes tasks, routes them to specialized sub-agents, and determines completion. [S2]
- The travel-planning example illustrates role-specialized agents coordinated by a manager, with subtasks such as flights, hotels, transport, and activities. [S1]
- The survey supports specialization and inter-agent communication as recurring properties of LLM-MAS. [S5]

#### Finding 4

**Claim**

Graph and workflow-based topologies support explicit task dependencies and adaptive control flow, while plan-and-execute separates planning from execution and may reduce execution cost at the expense of adaptability.

**Confidence:** Medium

**Why this confidence level**

The architectural distinction and trade-off are supported, but the retrieved material lacks a systematic head-to-head benchmark across graph, hierarchical, and plan-execute designs.

**Evidence**

- The taxonomy guide identifies graph topologies and plan-and-execute as canonical collaborative patterns, and notes plan brittleness when circumstances change or execution diverges from the plan. [S2]
- The survey cites graph-based multi-agent coordination for complex task dependencies as an example of LLM-MAS research. [S5]
- The empirical paper emphasizes network arrangements, handoffs, and control-flow strategies as reusable design elements. [S4]

#### Finding 5

**Claim**

Critique, verification, and debate form a distinct quality-control/adversarial family rather than merely a parallel task-decomposition family.

**Confidence:** Medium

**Why this confidence level**

The patterns are explicitly defined, but evidence for their effectiveness is limited in the retrieved sources and may depend strongly on task, evaluator quality, and model diversity.

**Evidence**

- The taxonomy guide distinguishes multi-agent debate, where agents present competing positions and a judge synthesizes them, from verifier-critic loops, where a critic evaluates and the generator revises. [S2]
- The overview claims that agents checking one another can improve reliability, but presents this as a general benefit rather than a controlled result in the excerpt. [S1]

#### Finding 6

**Claim**

The principal open problems are reliability under stochastic behavior, semantic drift and communication loss, scalability and token/latency cost, evaluation, governance, and transition from prototypes to production.

**Confidence:** High

**Why this confidence level**

The sources converge on these challenges, and the production-maturity limitation is stated directly in the academic empirical paper.

**Evidence**

- The empirical paper reports variability in LLM behavior as a barrier to production maturity and identifies reliability, scalability, and governance as critical research directions. [S4]
- The orchestration article identifies contextual drift, divergent interpretations, semantic loss through protocol formatting, emergent interaction failures, and resource/token scaling as problems. [S3]
- The taxonomy guide lists coordination overhead, supervisor drift, unsurfaced conflicts, premature convergence, critic bias, and plan brittleness as failure modes. [S2]
- The survey states that it discusses contemporary challenges and future directions, and frames interaction, reasoning, experience, and evolution as core areas requiring study. [S5]

#### Finding 7

**Claim**

The research landscape covers both problem-solving systems and simulated or embodied worlds, with applications including scientific discovery, industrial/utility workflows, telecommunications security, heritage management, customer service, robotics, and games.

**Confidence:** High

**Why this confidence level**

Application breadth and the problem-solving/world-simulation distinction are directly supported by the survey and independent case-study paper.

**Evidence**

- The survey organizes applications into problem-solving and world simulation, and gives examples across industrial engineering, scientific experimentation, embodied agents, and gaming. [S5]
- The empirical paper reports pilots in telecommunications security, national heritage asset management, and utilities customer-service automation. [S4]
- The overview gives travel planning and continuously updated monitoring as application examples. [S1]

### Conflicts Found

- The taxonomy guide claims that eight patterns cover approximately 95% of production systems and that hierarchical and graph topologies generally earn their cost, while the academic sources retrieved here do not establish those coverage or superiority percentages. These are unsupported generalizations rather than a demonstrated direct contradiction. [S2] [S4] [S5]
- The practitioner and orchestration sources make strong quantitative claims about accuracy, completion time, semantic error reduction, ROI, and deployment benefits, but the retrieved excerpts do not provide enough methodological detail to verify them. The academic empirical paper is more cautious, reporting promising prototype timelines while emphasizing unresolved production limitations. [S1] [S3] [S4]
- The taxonomy guide recommends starting with a single-agent baseline and escalating only when a measured failure is decomposable; the overview broadly presents multi-agent systems as better for complex tasks. These positions are conditionally compatible, but differ in how strongly they generalize multi-agent benefits. [S1] [S2]

### Important Gaps

- What common benchmark suite and metrics should compare multi-agent architectures on quality, cost, latency, robustness, and safety?
- How do centralized, decentralized, graph, swarm, debate, and verifier-critic designs compare under controlled task and model conditions?
- When does adding agents improve outcomes rather than amplify correlated errors, semantic drift, or coordination overhead?
- How should inter-agent communication be represented and validated to prevent information loss, ambiguity, and context-window growth?
- What mechanisms provide reliable fault detection, rollback, authorization, provenance, and human oversight in long-running systems?
- How much of the reported production benefit is attributable to architecture rather than model choice, prompting, tools, or domain-specific engineering?
- Can the categories in the retrieved taxonomies be reconciled into a stable design graph that separates topology, control flow, communication, agent specialization, memory/evolution, and quality control?

**Analysis Duration:** 21.80s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The current evidence is sufficient to identify broad components, application areas, patterns, and open-problem themes, but it is not sufficient for a responsible landscape report claiming a validated taxonomy, comparative architectural relationships, framework coverage, or empirical trade-offs. The strongest source is a survey plus one recent empirical paper; the remaining sources are practitioner articles, and several numerical or near-complete-taxonomy claims are weakly supported. A focused academic search for comparative evaluations and formal taxonomies would materially improve the answer.

**Next Search**

> academic survey comparative evaluation LLM-based multi-agent systems architectural patterns centralized decentralized hierarchical graph debate communication benchmarks

---

# Iteration 2

## 1. Search

**Query**

> academic survey comparative evaluation LLM-based multi-agent systems architectural patterns centralized decentralized hierarchical graph debate communication benchmarks

**Why this query**

The current evidence is sufficient to identify broad components, application areas, patterns, and open-problem themes, but it is not sufficient for a responsible landscape report claiming a validated taxonomy, comparative architectural relationships, framework coverage, or empirical trade-offs. The strongest source is a survey plus one recent empirical paper; the remaining sources are practitioner articles, and several numerical or near-complete-taxonomy claims are weakly supported. A focused academic search for comparative evaluations and formal taxonomies would materially improve the answer.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S6 — LLM-Based Multi-Agent Orchestration: A Survey of ...**
  URL: https://www.preprints.org/manuscript/202604.2147
- **S7 — Beyond Self-Talk: A Communication-Centric Survey of LLM ...**
  URL: https://arxiv.org/html/2502.14321v3
- **S8 — Multi-Agent LLM Systems: Architecture, Communication, and ...**
  URL: https://samiranama.com/posts/LLM-Based-Multi-Agent-Systems-Architectures-and-Collaboration
- **S9 — Survey of Multi-agent LLM Evaluations — LessWrong**
  URL: https://www.lesswrong.com/posts/tGcLA596E8g3KnphE/survey-of-multi-agent-llm-evaluations

**Search Duration:** 2.87s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

A robust landscape map should represent multi-agent LLM systems as a multidimensional design space rather than a single mutually exclusive taxonomy.

**Confidence:** High

**Why this confidence level**

Two surveys explicitly separate topology from communication and adaptivity, and the accumulated evidence independently supports treating specialization and quality control as cross-cutting dimensions.

**Evidence**

- S6 proposes three coordination topologies—centralized, decentralized, and hierarchical—with an independent dynamic/adaptive control axis, while also treating state management, planning, communication, control flow, and recovery as separate orchestration mechanisms. [S6]
- S7 distinguishes system-level communication—architecture, goals, and protocols—from internal communication strategies, paradigms, objects, and content. [S7]
- Prior findings identify specialization, topology, planning/control flow, memory/evolution, and critique as recurring but separable dimensions. [S2] [S4] [S5]

#### Finding 2

**Claim**

The core topology families can be organized as centralized, hierarchical, decentralized, and hybrid/adaptive systems, with graph/workflow structures describing control-flow arrangements that may occur within or across these families.

**Confidence:** High

**Why this confidence level**

The sources converge on the main topology families; the qualification about graph/workflow as a control-flow layer resolves overlapping terminology rather than asserting a disputed empirical result.

**Evidence**

- S6 explicitly identifies centralized, decentralized, and hierarchical topologies, each optionally augmented by dynamic/adaptive control. [S6]
- The prior empirical taxonomy includes centralized, decentralized, hybrid, and specialized categories, while the taxonomy guide identifies hierarchical, graph, and plan-and-execute patterns. [S2] [S3] [S4]
- S8 describes flat peer-to-peer, hierarchical, team-based, central-coordinator, and hybrid patterns, illustrating that practitioner labels often overlap or combine topology and organizational structure. [S8]

#### Finding 3

**Claim**

Communication is a foundational architectural layer: agents exchange structured information under protocols, and communication design includes both external/system-level protocols and internal message strategies and content.

**Confidence:** High

**Why this confidence level**

The communication-centric survey directly supports the claim, and the orchestration survey plus prior findings provide convergent architectural and failure-mode evidence.

**Evidence**

- S7 defines LLM-MAS as protocol-constrained systems driven by communication goals and organized by a communication architecture; its framework covers architecture, goals, protocols, strategies, paradigms, objects, and content. [S7]
- S6 treats inter-agent communication/context sharing as one of five orchestration mechanisms and discusses MCP as agent-to-tool and A2A as agent-to-agent protocol layers. [S6]
- Prior findings identify semantic loss, divergent interpretations, communication loss, and context growth as important failure modes. [S3] [S4] [S2]

#### Finding 4

**Claim**

Adaptivity, state management, and recovery should be shown as cross-cutting capabilities that can augment any topology, rather than as independent topology families.

**Confidence:** High

**Why this confidence level**

The dimensional separation is explicit in S6 and S7 and consistent with the accumulated functional taxonomy.

**Evidence**

- S6 explicitly places dynamic/adaptive control as an axis applicable to centralized, decentralized, and hierarchical topologies, and compares state-management granularity and failure-recovery options across frameworks. [S6]
- S7 describes agents as combining brain/reasoning, perception, action, and short- and long-term memory, while analyzing communication separately from agent components. [S7]
- Prior findings identify evolution/feedback, memory, verification, rollback-like recovery needs, and quality-control loops as distinct system functions. [S5] [S2] [S4]

#### Finding 5

**Claim**

Evaluation and safety research is substantially behind architectural experimentation, especially for collusion and threat-model coverage.

**Confidence:** Medium

**Why this confidence level**

S9 provides useful quantitative evidence but is a self-described, non-comprehensive LessWrong review; S7 independently supports the broader benchmarking and security gap.

**Evidence**

- A review of 32 multi-agent evaluation papers found miscoordination measured in 26 papers but collusion in only 5; most evaluations did not target a specified real-world AI threat model. [S9]
- S7 identifies inadequate benchmarking, security vulnerabilities, communication efficiency, and scalability as current challenges. [S7]
- Prior findings identify the absence of common benchmarks comparing quality, cost, latency, robustness, and safety across architectures as a central open problem. [S4] [S5]

#### Finding 6

**Claim**

The main open research frontier is system-level coordination reliability: preventing contradiction, duplication, inconsistent shared state, semantic drift, excessive interaction cost, and unsafe collective behavior while preserving adaptability.

**Confidence:** High

**Why this confidence level**

Multiple surveys and an evaluation review converge on these failure classes, although the relative effectiveness of particular mitigations remains unestablished.

**Evidence**

- S6 describes coordination failures as system-level degradation and highlights scaling interaction, state, error recovery, and security as orchestration concerns. [S6]
- S7 highlights communication efficiency, security, benchmarking, and scalability challenges. [S7]
- S9 emphasizes miscoordination, conflict, and collusion as distinct multi-agent failure modes, with collusion especially under-evaluated. [S9]
- Prior sources identify supervisor drift, critic bias, plan brittleness, semantic loss, governance, and production reliability as unresolved issues. [S2] [S3] [S4]

### Conflicts Found

- S6 presents centralized, decentralized, and hierarchical as the principal topology taxonomy, whereas S8 and prior sources additionally label flat, team-based, graph, swarm, debate, verifier-critic, and specialized designs as architectural patterns. This is primarily a difference in abstraction level: some labels describe topology, others control flow, organization, specialization, or quality control. [S6] [S8] [S2] [S4]
- S6 discusses published benchmarks and enterprise adoption claims, while S9 characterizes multi-agent evaluation coverage as narrow and non-comprehensive. These are compatible if benchmarks are understood as existing but insufficient for broad safety and architecture comparison; the evidence does not establish that current benchmarks are adequate. [S6] [S9] [S7]
- S6 is an un-peer-reviewed preprint according to its retrieved page, and S9 is a self-described college-class literature review. Their quantitative or comparative claims should therefore be presented more cautiously than claims from the academic surveys and empirical paper. [S6] [S9]

### Important Gaps

- How should the design graph operationally distinguish topology, control flow, communication protocol, specialization, memory/evolution, and quality-control mechanisms in a way that supports reproducible system comparison?
- Which benchmark tasks and metrics can isolate architecture effects from model quality, prompting, tools, and domain engineering?
- How do adaptive systems compare with fixed workflows under controlled changes in task uncertainty, agent count, communication budget, and failure rate?
- What protocols and representations best preserve provenance, authorization, uncertainty, and state consistency across agent-to-agent and agent-to-tool communication?
- How can evaluations cover collusion, sabotage, privacy, cybersecurity, persuasion, and other threat models outside game-based settings?
- When does adding agents improve performance enough to justify additional token, latency, monitoring, and coordination costs?

**Analysis Duration:** 19.99s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The new surveys materially resolve the key taxonomy gap by supporting a layered design graph, and S9 adds concrete evidence for the evaluation and safety gap. The remaining questions are important open problems for the report rather than blockers to responsibly mapping the landscape. Further searching could add examples, but is unlikely to materially improve the high-level taxonomy without a focused benchmark-comparison study.

**Stop Reason:** sufficient_evidence

---

# Final Research Decision

**Research Stopped Because**

The analyzer determined that the important parts of the question could be answered responsibly.

**Stop Reason:** sufficient_evidence

**Searches Performed:** 2

**Unique Sources:** 9

**Remaining Uncertainty**

- A standardized benchmark suite is needed to compare architectures while controlling for model quality, prompts, tools, domain engineering, agent count, and communication budget.
- The field lacks sufficiently controlled comparisons among centralized, hierarchical, decentralized, graph/workflow, adaptive, debate, and verifier-critic designs.
- Protocols and representations for preserving provenance, authorization, uncertainty, semantic fidelity, and shared-state consistency remain underdeveloped in the retrieved evidence.
- Long-running systems need better fault detection, rollback or recovery, termination, budget control, and human-oversight mechanisms.
- Safety evaluations need broader coverage of collusion, sabotage, privacy, cybersecurity, persuasion, and other threat models outside board-game settings.
- More evidence is needed on production transition: prototype speed and modularity do not by themselves establish reliability, scalability, governance, or economic value.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 2 | 6.20s |
| OpenAI Analysis | 2 | 41.78s |
| Report Generation | 1 | 33.66s |
| Total Run | — | 81.65s |
