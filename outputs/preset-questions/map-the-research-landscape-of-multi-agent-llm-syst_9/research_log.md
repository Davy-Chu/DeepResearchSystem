# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 10 / 10

**Unique Sources:** 31

**OpenAI Calls:** 11

**Tavily Calls:** 10

**Started:** 2026-09-01T04:04:18-04:00

**Ended:** 2026-09-01T04:08:26-04:00

**Total Runtime:** 247.34s

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

- **S1 — Agent Architecture Patterns: 2026 Taxonomy Guide**
  URL: https://www.digitalapplied.com/blog/agent-architecture-patterns-taxonomy-2026
- **S2 — LLM Agent Orchestration Patterns: Architectural ...**
  URL: https://www.c-sharpcorner.com/article/llm-agent-orchestration-patterns-architectural-frameworks-for-managing-complex
- **S3 — How to Build a Multi-Agent Deep Research System with ...**
  URL: https://medium.com/data-science-collective/building-a-multi-agent-deep-research-agent-with-langgraph-203547b5fb12
- **S4 — From RAG to Multi-Agent Systems: A Survey of Modern Approaches in LLM Development**
  URL: https://www.preprints.org/manuscript/202502.0406
- **S5 — LLM-Enabled Multi-Agent Systems: Empirical Evaluation ...**
  URL: https://arxiv.org/html/2601.03328v1

**Search Duration:** 2.81s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The landscape can be organized along at least two complementary dimensions: interaction purpose (collaborative versus competitive/quality-control) and control topology (centralized, decentralized, specialized, or hybrid).

**Confidence:** Medium

**Why this confidence level**

The classifications are explicit and mutually useful, but come primarily from practitioner/overview sources rather than a consolidated peer-reviewed taxonomy.

**Evidence**

- One taxonomy separates single-agent, collaborative multi-agent, competitive multi-agent, and orchestration-topology quadrants; another proposes centralized, decentralized, hybrid, and specialized categories. [S1] [S2]

#### Finding 2

**Claim**

A practical architectural vocabulary includes sequential planning/execution, hierarchical supervisor-worker decomposition, debate, verifier-critic loops, and decentralized or graph-like coordination; systems commonly compose multiple patterns rather than use one in isolation.

**Confidence:** Medium

**Why this confidence level**

The patterns and one implementation are directly described, but the claim that this set is comprehensive is not independently established.

**Evidence**

- S1 identifies plan-and-execute, supervisor-worker, multi-agent debate, and verifier-critic among canonical patterns and states production systems often compose patterns. [S1]
- S2 frames centralized, decentralized, specialized, and hybrid orchestration as alternatives for multi-agent systems. [S2]
- S3 demonstrates a concrete graph workflow combining classification, scouting, planning, parallel specialists, gap analysis, citation auditing, synthesis, and refinement. [S3]

#### Finding 3

**Claim**

Division of labor and specialization are the central rationale for multi-agent LLM systems, especially when tasks are decomposable or require parallel perspectives.

**Confidence:** Medium

**Why this confidence level**

Multiple sources converge on the mechanism, but the retrieved material provides limited controlled comparative evidence against strong single-agent baselines.

**Evidence**

- S4 states that multi-agent architectures can handle intricate tasks, improve scalability, and mitigate hallucinations through collaboration. [S4]
- S5 describes specialist agents connected in networks, with complex tasks divided into smaller tasks assigned to distinct agents. [S5]
- S1 associates supervisor-worker with clear sub-task decomposition and worker specialization, and plan-and-execute with predictable workflows. [S1]

#### Finding 4

**Claim**

Coordination introduces major reliability and resource risks: semantic/context drift, conflicting or lost information, variable behavior, token and latency overhead, brittle plans, and difficulty moving from prototypes to production.

**Confidence:** High

**Why this confidence level**

The risks are directly and consistently reported across several sources, although their prevalence and magnitude are not uniformly benchmarked.

**Evidence**

- S2 discusses contextual drift, semantic loss during protocol formatting, interaction-induced errors, and scaling token consumption. [S2]
- S1 lists coordination overhead, supervisor drift, unsurfaced worker conflicts, plan brittleness, debate convergence, and critique failure modes. [S1]
- S5 reports variability in LLM behavior as a barrier to production maturity and identifies reliability, scalability, and governance as critical research directions. [S5]

#### Finding 5

**Claim**

Graph/state-machine orchestration is a prominent implementation pattern for enforcing control flow, parallelism, bounded iteration, and quality gates.

**Confidence:** High

**Why this confidence level**

The architectural behavior is directly documented in an implementation source and supported by a survey-level overview.

**Evidence**

- S3 describes a LangGraph state machine with parallel specialist dispatch, gap checking, citation auditing before writing, and a maximum-iteration termination condition. [S3]
- S4 identifies LangGraph and stateful multi-agent applications as part of the current tooling landscape. [S4]

#### Finding 6

**Claim**

The most important open-problem areas are evaluation and benchmarking, communication/context protocols, reliability and controllability, cost/latency scaling, governance and safety, and production observability.

**Confidence:** High

**Why this confidence level**

These gaps recur across conceptual, implementation, and empirical sources, though the sources do not provide a systematic prioritization or standardized research agenda.

**Evidence**

- S2 explicitly raises questions about preventing miscalculations, token use, trusted shared systems, and semantic coordination shortfalls. [S2]
- S3 operationalizes unresolved concerns through citation auditing, gap analysis, bounded termination, partial-result handling, and warnings that outputs require verification. [S3]
- S5 concludes that reliability, scalability, and governance require further work to mature design patterns. [S5]

### Conflicts Found

- S1 presents a strong production-oriented recommendation that hierarchical supervisor-worker and graph topologies generally outperform swarms, while S2 treats decentralized orchestration as one of four viable categories and S5 presents networked specialist arrangements without establishing a universal topology winner. This is a conditional disagreement about production performance, not about whether decentralized designs exist. [S1] [S2] [S5]
- S1 claims eight patterns cover approximately 95% of production systems and says the architecture vocabulary has stabilized, whereas S4 and S5 characterize the area as an evolving landscape with emerging patterns and unresolved maturation challenges. The numerical coverage claim is unsupported by the other retrieved sources. [S1] [S4] [S5]
- S1 reports specific benefits for Reflexion, including a 30–50% reduction in repeated failures, while the other sources do not corroborate that figure. The qualitative claim may be plausible within the cited pattern description, but the quantitative magnitude remains unverified. [S1]
- S2 reports precise improvements in completion time, semantic errors/token cost, and ROI, but provides no retrieved methodological detail sufficient to compare those figures with S5's case studies or establish generalizability. [S2] [S5]

### Important Gaps

- What standardized benchmarks and metrics should compare single-agent, hierarchical, graph, swarm/decentralized, debate, and verifier-critic systems under equal model, tool, token, and latency budgets?
- When does adding agents improve task success enough to justify coordination cost, and how does that threshold vary by task decomposability and uncertainty?
- Which communication protocols, shared-memory designs, schemas, or context-management methods best prevent semantic drift and information loss?
- How should multi-agent systems handle correlated failures, collusion, premature consensus, model homogeneity, and adversarial or unsafe agent behavior?
- How reproducible and generalizable are the quantitative improvements reported by S1 and S2?
- What governance, auditability, human-in-the-loop, and observability mechanisms are required for deployment in high-stakes domains?

**Analysis Duration:** 18.88s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The sources support a useful preliminary taxonomy and identify recurring risks, but the original request asks for a research landscape. The current evidence lacks primary research coverage of comparative benchmarks, communication protocols, decentralized/swarm systems, evaluation methodology, and governance. A focused search for a recent scholarly survey or benchmark would materially improve the map.

**Next Search**

> LLM multi-agent systems survey taxonomy benchmarks evaluation communication protocols reliability 2024 2025

---

# Iteration 2

## 1. Search

**Query**

> LLM multi-agent systems survey taxonomy benchmarks evaluation communication protocols reliability 2024 2025

**Why this query**

The sources support a useful preliminary taxonomy and identify recurring risks, but the original request asks for a research landscape. The current evidence lacks primary research coverage of comparative benchmarks, communication protocols, decentralized/swarm systems, evaluation methodology, and governance. A focused search for a recent scholarly survey or benchmark would materially improve the map.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S6 — Large Language Model based Multi-Agents: A Survey of ...**
  URL: https://github.com/taichengguo/LLM_MultiAgents_Survey_Papers
- **S7 — A Technical Taxonomy of LLM Agent Communication Protocols | alphaXiv**
  URL: https://www.alphaxiv.org/abs/2606.19135v1
- **S8 — LLMs for Multi-Agent Cooperation**
  URL: https://xue-guang.com/post/llm-marl
- **S9 — Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems**
  URL: https://arxiv.org/html/2502.14321v3
- **S10 — Adversarial robustness of LLM-based multi-agent systems ...**
  URL: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1784484/full

**Search Duration:** 2.63s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

A useful research map should treat communication as a first-class architectural dimension, alongside control topology and task purpose.

**Confidence:** High

**Why this confidence level**

The communication-centric framework is explicitly defined in a survey and complements, rather than contradicts, the earlier topology-based classifications.

**Evidence**

- S9 proposes a two-level framework separating system-level communication—architecture, goals, and protocols—from internal communication strategies, paradigms, objects, and content. [S9]
- The prior evidence already distinguishes interaction purpose from control topology, while S9 adds a systematic view of how information is exchanged within those architectures. [S1] [S2] [S9]

#### Finding 2

**Claim**

The landscape includes a broad application and research-stream taxonomy beyond task-solving workflows: frameworks, orchestration and efficiency, problem solving, world simulation, and datasets/benchmarks.

**Confidence:** High

**Why this confidence level**

The categories are explicitly listed in S6 and supported by the application coverage described in S9, although S6 is a curated repository rather than a formal systematic review.

**Evidence**

- S6 organizes the literature into five streams: multi-agent frameworks; orchestration and efficiency; problem solving; world simulation; and datasets and benchmarks, with problem-solving subareas including software, embodied agents, science, debate, and databases. [S6]
- S9 reports applications spanning social simulation, software engineering, and recommendation systems, supporting the distinction between architectural research and application-oriented research. [S9]

#### Finding 3

**Claim**

Within-agent communication can be classified into reusable paradigms including memory-based sharing, reporting, relay/sequential passing, and debate, implemented over multiple network topologies.

**Confidence:** Medium

**Why this confidence level**

The mechanisms are directly described, but their comparative effectiveness and completeness are not established by the retrieved material.

**Evidence**

- S8 identifies memory-based, report-based, relay, and debate communication paradigms, and lists bus, star, ring, and tree network configurations. [S8]
- S9 frames internal communication in terms of strategies, paradigms, objects, and content, providing a broader analytical structure for these mechanisms. [S8] [S9]

#### Finding 4

**Claim**

Communication protocols form an emerging infrastructure layer with important interoperability trade-offs: protocols differ in counterparties, payloads, interaction state, discovery, and schema flexibility.

**Confidence:** Medium

**Why this confidence level**

The taxonomy and sample-level observations are explicit, but the source analyzes only nine protocols and is hosted on an alphaXiv presentation of a future-dated paper.

**Evidence**

- S7 proposes five protocol dimensions: counterparty, payload, interaction state, discovery mechanism, and schema flexibility, based on analysis of nine open-source protocols. [S7]
- S7 reports that sampled agent-to-agent protocols generally combine hybrid payloads with session persistence, while decentralized discovery is uncommon and runtime schema negotiation is limited. [S7]

#### Finding 5

**Claim**

Security is not merely an agent-level concern; interaction structure, message order, role assignment, and communication can determine whether errors and attacks propagate through the system.

**Confidence:** High

**Why this confidence level**

S10 provides direct empirical evidence in engineering tasks, while S9 independently identifies security as a central open issue. Generalization beyond the studied domains remains uncertain.

**Evidence**

- S10 finds that adversarial robustness varies with task type, injected-error subtlety, and communication order, and that prompt framing and role assignment can affect resilience. [S10]
- S10 reports that misinformation, semantic error injection, collusion, prompt propagation, and message manipulation can undermine collective decisions and safety constraints; consensus alone does not guarantee robustness. [S10]
- S9 independently identifies security vulnerabilities as a major challenge for LLM-MAS. [S9]

#### Finding 6

**Claim**

A visual taxonomy can be structured as a compositional design graph rather than a single mutually exclusive hierarchy.

**Confidence:** High

**Why this confidence level**

Multiple sources describe orthogonal dimensions and concrete compositions, directly supporting a graph or matrix representation.

**Evidence**

- S1 and S2 provide partially overlapping topology and orchestration categories; S8 adds structures, strategies, and communication paradigms; S9 explicitly separates system-level and internal communication; and S3 shows a workflow combining several patterns. [S1] [S2] [S3] [S8] [S9]

### Conflicts Found

- The earlier disagreement about topology remains unresolved: S1 favors hierarchical supervisor-worker and graph designs for production, whereas S2 and S8 treat decentralized or peer-to-peer designs as viable alternatives, and S5 does not establish a universal winner. The new sources add trade-offs but no controlled comparison that resolves the conditional claim. [S1] [S2] [S5] [S8]
- S7 suggests convergence toward hybrid, session-stateful agent-to-agent protocols and a federated layered protocol stack, while its discussion characterizes context-oriented protocols as often stateless and structured. This is not a direct contradiction, but indicates that protocol properties depend strongly on whether the counterparty is another agent or a tool/context service. [S7]
- S8 describes the field as moving toward practical reality and reports explosive growth, whereas the prior evidence emphasizes immature production reliability and unresolved scaling and governance problems. These claims concern adoption and maturity, so they are compatible but should not be conflated. [S5] [S8]

### Important Gaps

- Which architectural dimensions should define the final taxonomy without making categories overlap confusingly—topology, interaction purpose, communication protocol, internal communication paradigm, application domain, or evaluation regime?
- What standardized benchmarks and metrics compare architectures under equal model, tool, token, latency, and security budgets?
- When does multi-agent specialization outperform a strong single-agent or compound-inference baseline, and how does this depend on task decomposability?
- How should protocol interoperability, schema negotiation, discovery, privacy, authentication, and policy enforcement be standardized?
- How can evaluations measure correlated failures, collusion, premature consensus, adversarial message propagation, and communication-order effects?
- How generalizable are S10's engineering-specific robustness findings to software, science, social simulation, and embodied tasks?
- What evidence supports or refutes claimed quantitative gains in prior sources, including the reported Reflexion and efficiency/ROI improvements?

**Analysis Duration:** 18.77s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources materially strengthen the landscape map by adding communication protocols, internal communication paradigms, application streams, benchmarks as a research stream, and adversarial robustness. The remaining gaps are themselves important open problems for the requested report, but another broad search is unlikely to improve the taxonomy enough to justify continuing. The report should qualify source limitations, especially curated repositories, practitioner surveys, and the future-dated S7 source.

**Next Search**

> Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are. additional evidence search 3

---

# Iteration 3

## 1. Search

**Query**

> Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are. additional evidence search 3

**Why this query**

The new sources materially strengthen the landscape map by adding communication protocols, internal communication paradigms, application streams, benchmarks as a research stream, and adversarial robustness. The remaining gaps are themselves important open problems for the requested report, but another broad search is unlikely to improve the taxonomy enough to justify continuing. The report should qualify source limitations, especially curated repositories, practitioner surveys, and the future-dated S7 source.

**Results**

5 results retrieved.

2 new unique sources added.

### Sources

- **S11 — The Landscape of LLM-Based Search Agents: A Survey**
  URL: https://www.preprints.org/manuscript/202608.0572
- **S12 — Multi-Agent LLM Systems: Architecture, Communication, and Coordination | Samira Ghodratnama**
  URL: https://samiranama.com/posts/LLM-Based-Multi-Agent-Systems-Architectures-and-Collaboration

**Search Duration:** 3.09s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

A comparison contract is a useful additional layer for mapping multi-agent systems: evaluations should jointly specify task regime, evidence environment, evidence unit, control policy, output artifact, and evaluation contract.

**Confidence:** Medium

**Why this confidence level**

The framework is explicitly proposed, but S11 is an unreviewed preprint and is focused on search agents rather than the full multi-agent LLM landscape.

**Evidence**

- S11 proposes a Search-Agent Comparison Contract with these fields to make heterogeneous agentic search systems comparable, distinguishing task, evidence, workflow-control, output, and evaluation conditions. [S11]

#### Finding 2

**Claim**

Search and deep-research systems instantiate many of the same compositional components found in general multi-agent LLM systems, including planners, retrievers, memories, verifiers, writers, browsing tools, and stateful workflows.

**Confidence:** High

**Why this confidence level**

The component overlap is directly described in S11 and is consistent with the previously retrieved architectural evidence, although this does not establish that search-agent workflows cover all multi-agent system types.

**Evidence**

- S11 describes agentic information-seeking systems that plan queries, browse, inspect evidence, maintain state, verify information, and synthesize reports; it notes overlap among web agents, search agents, agentic RAG, deep-research agents, and multimodal browsing agents. [S11]
- Prior sources identify planning, specialist workers, verification, memory, graph orchestration, and synthesis as recurring multi-agent components. [S1] [S3] [S8] [S9]

#### Finding 3

**Claim**

The landscape should distinguish architectural design from evaluation regime: the same topology or communication pattern can appear under materially different task, evidence, budget, output, and judging conditions.

**Confidence:** High

**Why this confidence level**

The new source directly articulates the comparison problem, while prior findings independently identify budget and evaluation standardization as gaps.

**Evidence**

- S11 argues that superficially similar search-agent systems operate under different task regimes, evidence environments, output artifacts, tool budgets, and judging protocols, making direct comparison difficult. [S11]
- Existing unresolved questions call for comparisons under equal model, tool, token, latency, and security budgets. [S1] [S2] [S5] [S10]

#### Finding 4

**Claim**

A flat peer-to-peer architecture is characterized by many-to-many communication among equal agents, whereas hierarchical architecture routes tasks downward and results upward through supervisors and workers.

**Confidence:** Medium

**Why this confidence level**

S12 gives explicit pattern descriptions, but it is a practitioner blog and does not provide comparative empirical evidence.

**Evidence**

- S12 describes flat peer-to-peer systems as leaderless networks using direct messaging or a shared bus, and hierarchical systems as supervisor-manager-worker trees with downward delegation and upward aggregation. [S12]
- Prior sources separately identify decentralized, supervisor-worker, and hybrid orchestration patterns. [S1] [S2] [S5]

#### Finding 5

**Claim**

Team-based or society architectures form an intermediate organizational pattern between flat peer networks and strict hierarchies, combining a team lead, specialists, and shared state or memory.

**Confidence:** Medium

**Why this confidence level**

The pattern is explicitly described and fits prior communication and topology taxonomies, but its distinctiveness and comparative value relative to hybrid hierarchies are not empirically established.

**Evidence**

- S12 defines team-based systems as groups of specialists coordinated by a team supervisor, with shared state or memory for maintaining context. [S12]
- Prior evidence identifies specialist networks, shared memory, and hybrid compositions as recurring design elements. [S5] [S8] [S9]

### Conflicts Found

- S12 presents flat peer-to-peer, hierarchical, team-based, central-coordinator, and hybrid patterns as a practical five-pattern classification, while prior sources use overlapping but different category systems, including centralized, decentralized, specialized, hybrid, sequential, debate, and verifier-critic categories. These are differences in taxonomy granularity rather than direct empirical contradictions. [S1] [S2] [S8] [S12]
- S11's emphasis on comparison contracts and heterogeneous evaluation conditions reinforces the unresolved status of quantitative architectural comparisons; it does not support S1's stronger production-performance or coverage claims. [S1] [S11]

### Important Gaps

- How should the search-agent comparison contract be generalized beyond information seeking to software engineering, science, simulation, embodied tasks, and social environments?
- Which evaluation-contract fields are mandatory for fair comparisons of multi-agent architectures, and how should success, quality, safety, cost, latency, and evidence traceability be jointly measured?
- Do flat, team-based, hierarchical, graph, debate, or verifier-critic designs differ in performance under matched model, tool, token, latency, and security budgets?
- Are S11's proposed comparison dimensions adopted or validated by independent benchmark studies?
- How much do shared state and memory improve coordination relative to their privacy, contamination, and context-drift risks?
- S12 provides descriptive architecture examples but no controlled evidence for its claims about suitability or scalability.

**Analysis Duration:** 15.29s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The research map is structurally well supported, and the new sources strengthen the case for treating evaluation as a separate design dimension. However, the most important unresolved issue remains comparative benchmarking: there is no retrieved controlled, cross-topology evidence under matched budgets and task regimes. A focused search for such studies would materially improve the report.

**Next Search**

> multi-agent LLM architecture benchmark controlled comparison hierarchical decentralized debate single-agent equal token latency budget

---

# Iteration 4

## 1. Search

**Query**

> multi-agent LLM architecture benchmark controlled comparison hierarchical decentralized debate single-agent equal token latency budget

**Why this query**

The research map is structurally well supported, and the new sources strengthen the case for treating evaluation as a separate design dimension. However, the most important unresolved issue remains comparative benchmarking: there is no retrieved controlled, cross-topology evidence under matched budgets and task regimes. A focused search for such studies would materially improve the report.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S13 — Single-Agent vs Multi-Agent LLMs — Tran & Kiela (2026) · Annotated Library · Íñigo Medina**
  URL: https://inigomedina.co/library/work/tran-kiela-single-agent-outperform-multi-agent
- **S14 — Single-Agent LLMs Outperform Multi-Agent Systems onMulti-Hop Reasoning Under Equal Thinking Token Budgets**
  URL: https://arxiv.org/html/2604.02460v1
- **S15 — Why Single-Agent LLMs Beat Multi-Agent Systems on Multi-Hop Reasoning — A Budget-Controlled Story | Zhongzhu (Charlie) Zhou**
  URL: https://www.zhongzhuzhou.org/blog/2026-05-18-singlevsmultiagent-technical-review-en
- **S16 — Architectures for Multi-Agent Systems**
  URL: https://galileo.ai/blog/architectures-for-multi-agent-systems
- **S17 — Multi-agent system architecture: a comparison guide + best ...**
  URL: https://www.openlayer.com/blog/multi-agent-system-architecture-guide

**Search Duration:** 2.92s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Multi-agent LLM systems should not be presumed superior to strong single-agent baselines; under equal thinking-token budgets, single-agent systems matched or outperformed multi-agent variants on the reported multi-hop reasoning tasks.

**Confidence:** Medium

**Why this confidence level**

The study uses multiple model families and matched budgets, strengthening the evidence, but it is a preprint, the evidence is concentrated on multi-hop QA, and the retrieved review is not an independent empirical replication.

**Evidence**

- A controlled preprint compared single-agent systems with sequential, parallel, debate, and ensemble multi-agent architectures across Qwen3, DeepSeek-R1-Distill-Llama, and Gemini 2.5, reporting that single-agent systems consistently matched or outperformed multi-agent systems when intermediate reasoning tokens were matched. [S14]
- The accompanying review reports the same result across FRAMES and four-hop MuSiQue, with single-agent systems matching the best multi-agent variant across tested budgets. [S15]

#### Finding 2

**Claim**

The value of multi-agent decomposition is regime-dependent and appears strongest when single-agent context utilization degrades, when tasks require parallel or independent specialization, or when additional computation is intentionally available.

**Confidence:** Medium

**Why this confidence level**

The conditional design principle is supported by both the new controlled study and prior architectural accounts, but evidence across software, science, embodied, simulation, and long-running tool-use tasks remains limited.

**Evidence**

- S14 states that multi-agent systems become competitive when single-agent effective context utilization is degraded or when more compute is expended, while single-agent systems are more information-efficient under idealized perfect context utilization and fixed reasoning-token budgets. [S14]
- S15 reports that sequential multi-agent systems become competitive or superior under heavy context substitution or masking, and recommends multi-agent designs when measured context degradation or unavoidable specialization exists. [S15]
- Earlier sources identify task decomposition, parallel perspectives, specialist agents, and distributed context as rationales for multi-agent systems. [S1] [S4] [S5] [S16] [S17]

#### Finding 3

**Claim**

Equal-resource evaluation is a central methodological requirement for the multi-agent research landscape; otherwise apparent architectural gains may primarily reflect higher computation, longer traces, or different context conditions.

**Confidence:** High

**Why this confidence level**

The methodological problem is directly identified by the controlled study and independently aligns with the comparison-contract and evaluation-gap findings.

**Evidence**

- S14 explicitly controls total intermediate reasoning tokens and reports artifacts in API-based budget control that can distort effective computation between single- and multi-agent systems. [S14]
- S11 argues that comparisons vary in task regime, evidence environment, tool budget, output artifact, and judging protocol, and proposes a comparison contract to expose these differences. [S11]
- Prior findings call for matched model, tool, token, latency, and security budgets when comparing architectures. [S1] [S2] [S5] [S10]

#### Finding 4

**Claim**

Inter-agent communication should be modeled as both a capability and a potential information bottleneck: handoffs, aggregation, and partial contexts can introduce information loss, drift, and extraction errors.

**Confidence:** Medium

**Why this confidence level**

The bottleneck mechanism is theoretically articulated and consistent with prior failure taxonomies, but the theoretical argument depends on idealized assumptions and does not imply that all useful coordination is harmful.

**Evidence**

- S14 grounds this claim in a Data Processing Inequality argument under fixed budgets and reports communication bottlenecks as a reason for single-agent advantages on the studied tasks. [S14]
- Prior sources report semantic/context drift, information loss, aggregation errors, and interaction-induced failures in multi-agent workflows. [S1] [S2] [S3] [S5] [S9]

#### Finding 5

**Claim**

The design graph should include an explicit single-agent baseline and an evaluation/resource layer, not only multi-agent topology categories.

**Confidence:** High

**Why this confidence level**

The recommendation follows directly from convergent evidence that architectural dimensions and evaluation conditions are orthogonal and that single-agent systems can be competitive.

**Evidence**

- S14 shows that topology comparisons can reverse when computation is normalized and therefore treats single-agent reasoning as a necessary comparator. [S14]
- S11 distinguishes architecture from task, evidence, budget, output, and judging conditions, supporting a separate evaluation-contract layer. [S11]
- S1, S2, S8, S9, and S12 provide orthogonal topology, communication, purpose, and organizational dimensions rather than one exclusive hierarchy. [S1] [S2] [S8] [S9] [S12]

### Conflicts Found

- The new controlled study challenges broad or implicit claims that multi-agent systems generally outperform single-agent systems. S16 and S17 describe parallel specialization and distributed context as performance advantages, while S14 finds single-agent systems superior on matched-budget multi-hop reasoning. This is a task- and resource-conditional disagreement, not a universal contradiction. [S14] [S15] [S16] [S17]
- S14's information-theoretic argument favors single-agent processing under fixed budgets and perfect context utilization, whereas the same study and S15 identify degraded context as a regime where multi-agent systems become competitive. The tension is between an idealized theoretical condition and realistic context-limited operation. [S14] [S15]
- S17 reports precise production claims, including 80% gains on parallel tasks and 39–70% degradation on sequential reasoning, but the retrieved material does not provide methodological details or independent corroboration. These figures should not be merged with S14's controlled multi-hop results. [S14] [S17]
- Prior sources describe hierarchical, graph, peer-to-peer, swarm, debate, and verifier-critic patterns as viable design choices, while S14 indicates that several such patterns can lose to a single agent under matched reasoning-token budgets. Viability therefore depends on task structure, context regime, and resource accounting rather than topology alone. [S1] [S2] [S8] [S12] [S14]

### Important Gaps

- Do the matched-budget single-agent findings generalize beyond multi-hop QA to parallel tool use, software engineering, scientific tasks, embodied environments, simulation, and long-running workflows?
- How should total compute, wall-clock latency, API reasoning tokens, prompt/context tokens, tool calls, and parallel hardware costs be jointly normalized?
- When does specialization or independent evidence gathering create benefits that cannot be reproduced by one agent with equivalent compute and context management?
- Which communication protocols and message representations preserve task-relevant information while limiting semantic drift and coordination overhead?
- How do topology and communication choices affect correlated failures, collusion, premature consensus, adversarial message propagation, and security under matched budgets?
- Are the quantitative production claims in S16 and S17 independently validated under controlled experiments?
- How should benchmark contamination, paraphrasing robustness, judge reliability, and evidence traceability be incorporated into a general multi-agent comparison contract?
- What is the empirical boundary at which context degradation makes multi-agent systems preferable to a single agent with retrieval, summarization, memory, or a larger context window?

**Analysis Duration:** 19.41s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new evidence materially improves the landscape map by adding a controlled single-agent versus multi-agent comparison and a stronger case for budget normalization. However, its empirical scope is mainly multi-hop reasoning, while the original question spans diverse architectures and application streams. A focused cross-domain controlled benchmark would materially improve the report and help resolve whether the observed boundary generalizes.

**Next Search**

> controlled benchmark single-agent vs multi-agent LLM systems matched compute budgets parallel tool use software engineering science embodied tasks

---

# Iteration 5

## 1. Search

**Query**

> controlled benchmark single-agent vs multi-agent LLM systems matched compute budgets parallel tool use software engineering science embodied tasks

**Why this query**

The new evidence materially improves the landscape map by adding a controlled single-agent versus multi-agent comparison and a stronger case for budget normalization. However, its empirical scope is mainly multi-hop reasoning, while the original question spans diverse architectures and application streams. A focused cross-domain controlled benchmark would materially improve the report and help resolve whether the observed boundary generalizes.

**Results**

5 results retrieved.

2 new unique sources added.

### Sources

- **S18 — Single-Agent LLMs vs Multi-Agent Systems: Equal-Budget Reasoning | Tandemly Research**
  URL: https://tandemly.ai/research/single-vs-multi-agent-reasoning
- **S19 — Single AI Agent vs Multi-Agent Systems | Unico Connect**
  URL: https://unicoconnect.com/blogs/single-ai-agent-vs-multi-agent-systems

**Search Duration:** 3.19s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

S18 independently reinforces the matched-thinking-token result: on the reported multi-hop reasoning tasks, a single agent generally matched or outperformed multi-agent variants when total intermediate reasoning tokens were held constant.

**Confidence:** Medium

**Why this confidence level**

S18 adds detailed corroboration but is a research-industry summary rather than the primary paper or an independent replication; the evidence remains concentrated on multi-hop QA.

**Evidence**

- S18 describes experiments across Qwen3, DeepSeek, and Gemini 2.5; five multi-agent designs; FRAMES and four-hop MuSiQue; and reports that single-agent systems matched or beat multi-agent variants at meaningful budgets. [S18]
- This is consistent with the controlled comparison previously reported in S14 and summarized by S15. [S14] [S15]

#### Finding 2

**Claim**

The relevant comparison variable is total reasoning computation, not merely the number of agents, model calls, or wall-clock latency.

**Confidence:** High

**Why this confidence level**

The methodological point is directly stated by two sources and aligns with the broader comparison-contract evidence in S11.

**Evidence**

- S18 emphasizes that multi-agent systems normally generate more intermediate reasoning text and make more calls, and defines the comparison around equal total thinking-token budgets. [S18]
- S14 likewise reports that API-based budget controls can create unequal effective computation and argues for explicit token normalization. [S14]

#### Finding 3

**Claim**

The tested multi-agent design space in S18 spans sequential decomposition, subtask parallelism, parallel role specialization, debate, and ensemble selection, strengthening the design graph's coverage of major reasoning-oriented patterns.

**Confidence:** High

**Why this confidence level**

The patterns are directly enumerated and map clearly onto previously retrieved architectural categories, although this does not establish that they cover all application domains.

**Evidence**

- S18 explicitly lists and describes five architectures: sequential, subtask-parallel, parallel-roles, debate, and ensemble. [S18]
- These correspond to the previously identified plan-and-execute, specialization, debate, and compositional orchestration patterns. [S1] [S3] [S8]

#### Finding 4

**Claim**

Multi-agent systems should be represented as conditional design choices rather than a default improvement over single-agent reasoning.

**Confidence:** Medium

**Why this confidence level**

The conditional conclusion is well supported for multi-hop reasoning, but evidence remains limited for software engineering, scientific tasks, embodied environments, simulation, and long-running tool-use workflows.

**Evidence**

- S18 states that the multi-agent advantage largely disappears under equal thinking-token budgets and that a single agent with full context is the strongest default for the studied reasoning regime. [S18]
- S14 and S15 identify degraded context utilization, extra available computation, or unavoidable specialization as conditions in which multi-agent systems can become competitive. [S14] [S15]

#### Finding 5

**Claim**

The new material does not materially change the overall taxonomy: a compositional graph should retain topology, communication, organizational pattern, task/application regime, and an explicit evaluation/resource layer.

**Confidence:** High

**Why this confidence level**

The new source supplies additional architectural examples while remaining compatible with the previously established multidimensional design-graph approach.

**Evidence**

- S18 adds concrete reasoning architectures but does not replace the prior orthogonal dimensions of topology, communication paradigm, protocol, purpose, and application stream. [S18] [S8] [S9]
- S11 and S14 support separating architecture from task, context, output, budget, and judging conditions, with single-agent reasoning as a baseline node. [S11] [S14]

### Conflicts Found

- S18's broad framing that single-agent systems are the strongest default could be read as stronger than the conditional conclusions in S14 and S15. The detailed evidence, however, concerns multi-hop reasoning under matched thinking-token budgets; it does not resolve whether multi-agent systems are superior in context-limited, parallel, tool-using, embodied, or long-running regimes. [S18] [S14] [S15]
- S18 reports aggregate accuracy values favoring single-agent systems at several budgets, while earlier sources describe specialization, parallelism, and distributed context as potential advantages. These claims are conditionally compatible, but no retrieved study establishes the boundary across task families. [S18] [S1] [S4] [S5] [S16] [S17]
- S19 is a general implementation-oriented comparison page, but the retrieved excerpt contains no substantive empirical results or methodological details relevant to the landscape. It therefore cannot corroborate or challenge the controlled findings. [S19]

### Important Gaps

- Do the matched-budget single-agent findings generalize beyond FRAMES and four-hop MuSiQue to software engineering, scientific discovery, embodied tasks, simulations, multi-step tool use, and long-running workflows?
- What is the empirical boundary at which context degradation, task parallelism, independent evidence gathering, or specialization makes multi-agent systems preferable to a single agent with retrieval, memory, summarization, or a larger context window?
- How should total compute, reasoning tokens, prompt/context tokens, tool calls, wall-clock latency, parallel hardware cost, and monetary cost be jointly normalized?
- Which communication protocols and context-management mechanisms preserve information well enough to overcome handoff bottlenecks without causing drift, contamination, or excessive coordination overhead?
- How do topology and communication choices affect correlated failures, collusion, premature consensus, adversarial message propagation, and safety under matched resource budgets?
- Are the production and efficiency claims in earlier practitioner sources independently validated under controlled experiments?
- Which benchmark and evaluation-contract fields should be mandatory for fair cross-domain comparisons?

**Analysis Duration:** 15.86s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The core landscape and design graph are sufficiently supported, and S18 strengthens the case for an explicit single-agent and equal-resource baseline. However, a major unresolved part of the original question is when multi-agent architectures actually provide value outside matched-budget multi-hop reasoning. A targeted search for controlled cross-domain evaluations would materially improve the report.

**Next Search**

> controlled benchmark single-agent vs multi-agent LLM systems software engineering scientific tasks embodied agents equal compute token latency budget

---

# Iteration 6

## 1. Search

**Query**

> controlled benchmark single-agent vs multi-agent LLM systems software engineering scientific tasks embodied agents equal compute token latency budget

**Why this query**

The core landscape and design graph are sufficiently supported, and S18 strengthens the case for an explicit single-agent and equal-resource baseline. However, a major unresolved part of the original question is when multi-agent architectures actually provide value outside matched-budget multi-hop reasoning. A targeted search for controlled cross-domain evaluations would materially improve the report.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S20 — Single-Agent vs Multi-Agent Systems: When Coordination Helps, Hurts ...**
  URL: https://medium.com/@mjgmario/single-agent-vs-multi-agent-systems-when-coordination-helps-hurts-and-pays-off-57735ee7916d
- **S21 — Single-Agent LLMs Outperform Multi-Agent Systems on ...**
  URL: https://www.alphaxiv.org/abs/2604.02460
- **S22 — Single Agent vs Multi-Agent: Trade-Offs, Efficiency & Control**
  URL: https://www.cognizant.com/us/en/ai-lab/blog/single-agent-vs-multi-agent

**Search Duration:** 3.18s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new evidence sharpens the taxonomy by adding an empirically grounded task-regime axis: static/non-agentic benchmarks versus genuinely agentic tasks requiring sustained interaction, partial observability, iterative information gathering, and feedback-driven adaptation.

**Confidence:** Medium

**Why this confidence level**

The distinction is clearly presented, but S20 is a secondary practitioner article and the underlying paper is not directly retrieved.

**Evidence**

- S20 reports a distinction from Kim et al. between static benchmarks solvable through single-shot reasoning and agentic benchmarks involving multi-step environment interaction and adaptive refinement. [S20]

#### Finding 2

**Claim**

A large controlled evaluation suggests that multi-agent performance is strongly topology- and task-dependent rather than uniformly superior: centralized systems reportedly excel on decomposable financial analysis, while decentralized systems help more on exploration-oriented web research; independent systems can substantially underperform.

**Confidence:** Low

**Why this confidence level**

The reported results are potentially important and broad, but they are available only through a Medium synthesis rather than the primary study, and the retrieved excerpt does not include the complete results or methods.

**Evidence**

- S20 describes 260 configurations across six agentic benchmarks and reports performance ranging from -70.0% for an independent PlanCraft configuration to +80.8% for centralized Finance-Agent, with decentralized systems strongest on BrowseComp-Plus exploration. [S20]
- S20 characterizes independent MAS as the weakest tested variant, centralized MAS as strongest on decomposable tasks, and decentralized MAS as useful for diverse-perspective exploration. [S20]

#### Finding 3

**Claim**

Coordination overhead varies dramatically by architecture and can outweigh benefits: reported additional-token overhead is approximately 58% for independent MAS, 285% for centralized MAS, 263% for decentralized MAS, and 515% for hybrid MAS.

**Confidence:** Low

**Why this confidence level**

These are precise quantitative claims from a secondary source without directly retrieved methodological detail or independent corroboration.

**Evidence**

- S20 provides topology-specific overhead estimates and states that hybrid systems require 6.2 times the single-agent token budget in the described evaluation. [S20]

#### Finding 4

**Claim**

The design graph should distinguish communication from coordination. Centralized systems can separate strategic direction by an orchestrator from message passing, whereas decentralized debate entangles the two; this distinction may explain efficiency differences.

**Confidence:** Medium

**Why this confidence level**

The conceptual distinction is explicit and consistent with prior findings, but its causal effect on efficiency is not independently established.

**Evidence**

- S20 explicitly distinguishes coordination as strategic direction from communication as message passing, and states that centralized systems separate them while decentralized debate combines them. [S20]
- Earlier evidence independently treats communication protocols and control topology as orthogonal dimensions. [S7] [S8] [S9]

#### Finding 5

**Claim**

The new sources reinforce specialization, modularity, focused context, interoperability, and embedded safeguards as practical motivations for multi-agent architectures, while also emphasizing that these are design rationales rather than proof of general superiority.

**Confidence:** Medium

**Why this confidence level**

The motivations are directly described, but S22 is an opinion-oriented industry-lab article and does not provide controlled comparative evidence.

**Evidence**

- S22 argues that modular agents enable reuse, specialization, smaller or on-premise models, agent interoperability, focused context, isolated testing, checks and balances, and human or rule-based fallbacks. [S22]
- Prior controlled evidence shows that multi-agent advantages can disappear under matched reasoning-token budgets, making these benefits conditional on task and system regime. [S14] [S15] [S18]

#### Finding 6

**Claim**

The most important unresolved empirical boundary is whether multi-agent systems outperform strong single-agent or compound-inference baselines on genuinely agentic, tool-using, context-limited tasks under jointly normalized resource and safety budgets.

**Confidence:** High

**Why this confidence level**

The evidence gap is explicit and remains unresolved despite the new secondary report; the task-domain boundary is central to the original landscape question.

**Evidence**

- S20 claims broad matched-budget evaluation across six agentic benchmarks, but the primary study and full methodology were not retrieved, so its results cannot yet resolve the gap responsibly. [S20]
- Prior evidence identifies the same unresolved boundary beyond multi-hop QA and calls for normalization of tokens, tools, latency, compute, security, and evaluation conditions. [S11] [S14] [S18]

### Conflicts Found

- S20 reports substantial multi-agent gains on some agentic benchmarks, especially centralized Finance-Agent and decentralized BrowseComp-Plus, whereas S14, S15, and S18 find single-agent systems generally match or outperform multi-agent variants under equal thinking-token budgets on multi-hop reasoning. This is a task-regime and benchmark conflict, not a universal contradiction, but S20's results would materially broaden the evidence if independently verified. [S20] [S14] [S15] [S18]
- S20 reports centralized MAS as an error-containment mechanism and decentralized MAS as useful for exploration, while earlier sources leave topology superiority unresolved and warn about coordination, drift, and communication failures. The new claims suggest conditional topology advantages but do not establish a general winner. [S20] [S1] [S2] [S5] [S8]
- S22 presents modularity, distributed redundancy, and safeguards as practical advantages of multi-agent systems, while matched-budget studies show that added agents can introduce information bottlenecks and fail to improve accuracy. Architectural maintainability or controllability benefits should therefore not be conflated with task-performance gains. [S22] [S14] [S18]

### Important Gaps

- Can the reported Kim et al. results in S20 be verified from the primary paper, including benchmark definitions, exact budget matching, baselines, statistical uncertainty, and per-topology results?
- Do the reported topology-specific gains persist when prompt/context tokens, tool calls, wall-clock latency, monetary cost, parallel hardware, and security controls are jointly normalized rather than only total tokens?
- How do the six agentic benchmarks in S20 compare with software engineering, scientific discovery, embodied environments, simulation, and long-running workflows?
- Are error-amplification figures such as 17.2x versus 4.4x measured consistently and causally attributable to communication topology?
- Which benefits of multi-agent systems are performance benefits versus engineering benefits such as modularity, interoperability, auditability, and fault isolation?
- How should the taxonomy represent task regime, topology, communication/coordination separation, organizational pattern, protocol, application domain, and evaluation contract without implying mutually exclusive categories?

**Analysis Duration:** 16.92s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new source potentially supplies the most relevant missing controlled evidence—cross-domain comparisons of topologies on genuinely agentic tasks—but it is only a secondary Medium article and the retrieved content is truncated. Verifying the underlying primary study would materially improve the report and could clarify the apparent contrast with matched-budget multi-hop reasoning results.

**Next Search**

> Kim et al. "Towards a Science of Scaling Agent Systems" primary paper 260 configurations Finance-Agent BrowseComp-Plus PlanCraft Workbench SWE-bench Terminal-Bench

---

# Iteration 7

## 1. Search

**Query**

> Kim et al. "Towards a Science of Scaling Agent Systems" primary paper 260 configurations Finance-Agent BrowseComp-Plus PlanCraft Workbench SWE-bench Terminal-Bench

**Why this query**

The new source potentially supplies the most relevant missing controlled evidence—cross-domain comparisons of topologies on genuinely agentic tasks—but it is only a secondary Medium article and the retrieved content is truncated. Verifying the underlying primary study would materially improve the report and could clarify the apparent contrast with matched-budget multi-hop reasoning results.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S23 — Towards a Science of Scaling Agent Systems**
  URL: https://arxiv.org/html/2512.08296v3
- **S24 — Capable language models can outgrow the benefits of collaboration**
  URL: https://www.nature.com/articles/s42256-026-01268-y
- **S25 — GitHub - ybkim95/agent-scaling: Towards a Science of Scaling Agent Systems · GitHub**
  URL: https://github.com/ybkim95/agent-scaling
- **S26 — Paper page - Towards a Science of Scaling Agent Systems**
  URL: https://huggingface.co/papers/2512.08296
- **S27 — Towards a Science of Scaling Agent Systems | Cool Papers - Immersive Paper Discovery**
  URL: https://papers.cool/arxiv/2512.08296

**Search Duration:** 4.61s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new primary study substantially strengthens the case for a task- and architecture-conditional landscape rather than a universal multi-agent advantage.

**Confidence:** High

**Why this confidence level**

S23 provides a detailed primary-source abstract with broad controlled coverage and directly addresses the central comparison question.

**Evidence**

- Across 260 configurations, six agentic benchmarks, five canonical architectures, and three LLM families, the study reports relative performance changes from +80.8% on decomposable financial reasoning to −70.0% on sequential planning. [S23]
- The study identifies capability saturation, tool-heavy-task overhead, and greater error propagation without centralized verification as recurring effects. [S23]

#### Finding 2

**Claim**

Agentic task regime should be a core axis of the taxonomy, distinct from static reasoning benchmarks.

**Confidence:** High

**Why this confidence level**

The distinction is explicitly defined and tied to the evaluation problem in the primary source, reinforcing the earlier secondary evidence.

**Evidence**

- S23 defines agentic tasks by sustained environmental interaction, iterative information gathering under partial observability, and adaptive refinement from feedback, contrasting them with static single-shot tasks. [S23]
- The study argues that much prior multi-agent evaluation on non-agentic tasks may give misleading guidance about collaboration in real deployments. [S23]

#### Finding 3

**Claim**

Coordination creates an intrinsic context-integration versus diversity trade-off: single agents preserve unified memory, while multi-agent systems gain parallel or diverse exploration at the cost of lossy inter-agent compression and synchronization.

**Confidence:** High

**Why this confidence level**

The new source provides a clear mechanism that is consistent with several prior failure analyses.

**Evidence**

- S23 describes unified single-agent memory as maximizing context integration and multi-agent communication as introducing information fragmentation, compression, synchronization overhead, and cognitive load. [S23]
- Earlier sources independently report semantic drift, information loss, and communication bottlenecks during handoffs and aggregation. [S1] [S2] [S9] [S14]

#### Finding 4

**Claim**

A quantitative scaling perspective is emerging: coordination benefits tend to diminish as single-agent capability rises, and measurable coordination metrics can predict preferred architectures better than agent count alone.

**Confidence:** Medium

**Why this confidence level**

The scaling direction is strongly supported, but the differing reported benchmark counts and R2 values indicate version or reporting differences that require reconciliation.

**Evidence**

- S23 reports a predictive model using coordination, capability, and task/system factors, with cross-validated R2=0.373 overall and R2=0.413 using a task-grounded capability metric; it identifies a robust capability-saturation effect. [S23]
- S26 and S27 summarize an earlier or alternate evaluation reporting R2=0.513 and prediction of the best strategy for 87% of held-out configurations. [S26] [S27]

#### Finding 5

**Claim**

The new evidence supports adding explicit process dynamics and coordination metrics to the evaluation layer, not relying only on final accuracy.

**Confidence:** High

**Why this confidence level**

This is directly stated by the primary study and aligns with the prior comparison-contract findings.

**Evidence**

- S23 states that prior evaluations conflate architecture with prompts, tools, and budgets and focus primarily on final accuracy, motivating analysis of coordination costs and system dynamics. [S23]
- The study identifies efficiency, overhead, error amplification, redundancy, and task-grounded capability as relevant predictive factors. [S23] [S26] [S27]

#### Finding 6

**Claim**

The released implementation improves reproducibility and makes the five-way comparison concrete: single, independent, centralized, decentralized, and hybrid systems can be run across browsing, planning, software, terminal, business-tool, and finance benchmarks.

**Confidence:** High

**Why this confidence level**

The repository directly documents available configurations and reproducibility artifacts, although code availability does not itself validate every reported result.

**Evidence**

- S25 lists runnable agent configurations and six benchmark configurations, including SWE-bench Verified, Terminal-Bench, BrowseComp-Plus, PlanCraft, Workbench, and Finance Agent. [S25]
- S25 describes the repository as the code release accompanying the scaling study and includes experiment, reproduction, dataset, and trace-related materials. [S25]

### Conflicts Found

- S23 reports 260 configurations across six benchmarks with cross-validated R2=0.373 overall, whereas S26 and S27 report 180 configurations across four benchmarks with R2=0.513. These appear to be different manuscript versions, evaluation scopes, or metrics, but the retrieved sources do not explain the discrepancy. [S23] [S26] [S27]
- The new primary source reports that agentic evaluations have often been conducted on non-agentic tasks, while earlier controlled evidence focused largely on multi-hop QA. This is a difference in task regime and limits direct comparison rather than a direct contradiction. [S14] [S18] [S23]
- S24 is a later Nature Machine Intelligence article with a title consistent with capability saturation, but the retrieved content provides no substantive results beyond bibliographic/title information; it should not be treated as independent confirmation of specific quantitative claims. [S24]

### Important Gaps

- Which version of the scaling study should anchor quantitative claims, and why do S23, S26, and S27 report different benchmark counts, configuration counts, and R2 values?
- Do the reported scaling relationships remain valid when prompt/context tokens, tool calls, wall-clock latency, monetary cost, parallel hardware, and security controls are jointly normalized?
- How do the reported architecture preferences generalize across the six evaluated domains, especially software engineering, terminal interaction, embodied planning, and long-running workflows?
- What process-level metrics best predict success: context fragmentation, coordination overhead, error amplification, redundancy, semantic diversity, or another measurable property?
- Can the scaling framework be independently replicated by researchers using the released repository and held-out models or benchmarks?
- What are the findings and methods of S24, and does that article provide independent validation beyond the S23 research line?

**Analysis Duration:** 19.06s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new evidence materially improves the landscape map and corroborates the conditional, task-regime-dependent view. However, the conflicting versions of the central scaling study and the still-unresolved cross-domain and independent-replication questions are important for a responsible report, especially because quantitative architectural claims are central to the research landscape.

**Next Search**

> "Towards a Science of Scaling Agent Systems" 260 configurations six benchmarks version 180 configurations R2 0.513

---

# Iteration 8

## 1. Search

**Query**

> "Towards a Science of Scaling Agent Systems" 260 configurations six benchmarks version 180 configurations R2 0.513

**Why this query**

The new evidence materially improves the landscape map and corroborates the conditional, task-regime-dependent view. However, the conflicting versions of the central scaling study and the still-unresolved cross-domain and independent-replication questions are important for a responsible report, especially because quantitative architectural claims are central to the research landscape.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S28 — Towards a Science of Scaling Agent Systems | alphaXiv**
  URL: https://www.alphaxiv.org/abs/2512.08296
- **S29 — Overview ‹ Towards a science of scaling agent systems**
  URL: https://www.media.mit.edu/projects/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/overview
- **S30 — Towards a science of scaling agent systems - Google Research**
  URL: https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work

**Search Duration:** 3.47s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources strongly reinforce a task- and architecture-conditional view of multi-agent LLM systems rather than a universal benefit from adding agents.

**Confidence:** High

**Why this confidence level**

The result is reported consistently by the primary-style abstract and two institutional summaries, and it directly addresses the central landscape question.

**Evidence**

- The study evaluates five architectures—single-agent, independent, centralized, decentralized, and hybrid—and reports that multi-agent coordination can improve parallelizable financial reasoning by about 81% but degrade sequential planning by 39–70%. [S28] [S29] [S30]
- The sources explicitly frame the central design principle as alignment between coordination strategy and task structure; mismatched coordination can reduce performance. [S28] [S30]

#### Finding 2

**Claim**

The canonical architecture graph should include single-agent, independent, centralized, decentralized, and hybrid systems as major comparison nodes.

**Confidence:** High

**Why this confidence level**

The five-way classification is explicitly defined and maps cleanly onto the previously accumulated taxonomy.

**Evidence**

- Single-agent systems use unified memory and sequential execution; independent systems work without inter-agent communication; centralized systems use an orchestrator and workers; decentralized systems use peer-to-peer interaction; hybrid systems combine hierarchical oversight with peer communication. [S28] [S29] [S30]
- These categories extend and organize earlier plan-and-execute, supervisor-worker, swarm/decentralized, debate, and graph-based patterns. [S1] [S2] [S3] [S8] [S12]

#### Finding 3

**Claim**

Agentic task regime should be a first-class taxonomy axis, distinct from static reasoning benchmarks.

**Confidence:** High

**Why this confidence level**

The definition is explicit and central to the study's evaluation design.

**Evidence**

- Agentic evaluations are defined by sustained environment interaction, iterative information gathering under partial observability, and adaptive refinement from feedback. [S29] [S30]
- The study contrasts these tasks with static benchmarks and argues that static evaluations may give misleading guidance about real-world collaboration. [S28] [S30]

#### Finding 4

**Claim**

Centralized coordination appears especially promising when tasks are decomposable and when centralized verification can contain errors; decentralized coordination may be useful when diverse exploration or peer interaction is valuable.

**Confidence:** Medium

**Why this confidence level**

The topology descriptions and centralized-task result are direct, but the retrieved new material does not provide sufficient detailed per-topology results to establish a general decentralized advantage.

**Evidence**

- Centralized coordination produced the largest reported gain on decomposable financial analysis, while the study associates centralized coordination with orchestration and verification. [S28] [S29] [S30]
- Decentralized systems are described as peer-to-peer debate or consensus architectures, while independent systems provide parallelization with minimal coordination. [S29] [S30]

#### Finding 5

**Claim**

Coordination is both a source of capability and a source of overhead, including context fragmentation, communication cost, and error propagation.

**Confidence:** High

**Why this confidence level**

The new sources provide direct mechanisms and measurements that corroborate several independent prior failure analyses.

**Evidence**

- The study attributes sequential-task degradation to fragmented reasoning and insufficient cognitive budget, and reports a disproportionate tool-coordination tax as tool requirements increase. [S29] [S30]
- It identifies greater error propagation in architectures without centralized verification and treats error amplification as a measurable reliability outcome. [S28] [S29]
- These mechanisms agree with earlier findings on semantic drift, lossy handoffs, synchronization overhead, and interaction-induced failures. [S1] [S2] [S9] [S14] [S23]

#### Finding 6

**Claim**

The evaluation layer of the design graph should include process and resource metrics, not only final task accuracy.

**Confidence:** High

**Why this confidence level**

The new study directly operationalizes several process variables and is consistent with the previously established methodological gap.

**Evidence**

- The study reports architectural scaling in relation to coordination, model capability, task factors, communication overhead, and error amplification. [S28] [S29] [S30]
- The architecture summaries explicitly distinguish communication overhead and coordination mechanisms across the five designs. [S29] [S30]
- This supports prior recommendations to normalize tokens, tools, latency, context, compute, and security conditions through an evaluation contract. [S11] [S14] [S23]

#### Finding 7

**Claim**

A quantitative scaling perspective is emerging in which coordination benefits diminish as baseline model capability rises and architecture choice can be predicted from task and system factors.

**Confidence:** Medium

**Why this confidence level**

The quantitative claims come from one study and are presented differently across retrieved versions, although the qualitative scaling direction is consistent.

**Evidence**

- The study reports a capability-saturation effect, diminishing coordination returns above stronger single-agent baselines, and a predictive model achieving cross-validated R² values of 0.373 overall and 0.413 with a task-grounded capability metric. [S28]
- It reports identifying the best architecture for 87% of held-out configurations and consistent preferences on unseen frontier models. [S28] [S29] [S30]

#### Finding 8

**Claim**

The final visual taxonomy should be a compositional design graph, not a single mutually exclusive hierarchy.

**Confidence:** High

**Why this confidence level**

The evidence consistently presents orthogonal dimensions rather than a single canonical hierarchy.

**Evidence**

- The new five-way architecture classification describes control topologies, while prior sources separately identify communication paradigms, protocols, organizational forms, task regimes, applications, and evaluation contracts. [S28] [S29] [S30] [S7] [S8] [S9] [S11]
- The same architecture can therefore be analyzed simultaneously by topology, communication, orchestration, task structure, and resource regime. [S11] [S14] [S23] [S28]

### Conflicts Found

- S28 reports 260 configurations across six agentic benchmarks and three LLM families, while S29 and S30 describe 180 configurations across four benchmarks. These may represent different manuscript versions, evaluation scopes, or reporting errors; the retrieved material does not reconcile them. [S28] [S29] [S30]
- The new sources report strong gains for centralized coordination on parallelizable financial reasoning and broad degradation on sequential planning, while earlier matched-thinking-token studies found single-agent systems competitive or superior on multi-hop QA. The disagreement is conditional on task regime, context conditions, and resource accounting rather than universal. [S14] [S15] [S18] [S28] [S29] [S30]
- The sources describe centralized coordination as useful for verification and error containment, but the available excerpts do not establish that centralized topology is generally superior to decentralized, hybrid, or single-agent designs across domains. [S1] [S2] [S5] [S20] [S28] [S29]

### Important Gaps

- Which study version and benchmark scope should anchor the quantitative report: 260 configurations across six benchmarks or 180 configurations across four benchmarks?
- Do the reported architecture preferences persist when prompt/context tokens, reasoning tokens, tool calls, wall-clock latency, monetary cost, parallel hardware, and security controls are jointly normalized?
- How do the reported results generalize to software engineering, scientific discovery, embodied environments, simulation, and long-running tool-use workflows?
- What process metrics best predict architecture choice: decomposability, context fragmentation, coordination overhead, error amplification, redundancy, or task-grounded capability?
- Does centralized verification causally reduce error propagation, or is the reported reliability advantage confounded by prompts, model allocation, or additional computation?
- How should the taxonomy distinguish communication topology, orchestration policy, communication protocol, and organizational pattern without treating them as interchangeable?

**Analysis Duration:** 18.91s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources materially strengthen the central conclusion and add useful architecture definitions and process metrics, but they introduce or preserve a consequential inconsistency in the study's reported scope (180 versus 260 configurations and four versus six benchmarks). Resolving the primary-paper version and exact methodology would improve the report's quantitative claims and prevent misrepresentation.

**Next Search**

> "Towards a Science of Scaling Agent Systems" 180 260 six benchmarks four benchmarks version

---

# Iteration 9

## 1. Search

**Query**

> "Towards a Science of Scaling Agent Systems" 180 260 six benchmarks four benchmarks version

**Why this query**

The new sources materially strengthen the central conclusion and add useful architecture definitions and process metrics, but they introduce or preserve a consequential inconsistency in the study's reported scope (180 versus 260 configurations and four versus six benchmarks). Resolving the primary-paper version and exact methodology would improve the report's quantitative claims and prevent misrepresentation.

**Results**

5 results retrieved.

1 new unique source added.

### Sources

- **S31 — The Science of Scaling AI Agents: A Briefing on New Methodologies and Failure Modes**
  URL: https://micheallanham.substack.com/p/the-science-of-scaling-ai-agents

**Search Duration:** 2.51s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new source reinforces the central conclusion that multi-agent scaling is task-dependent rather than uniformly beneficial.

**Confidence:** Medium

**Why this confidence level**

S31 is a secondary briefing, but its qualitative and headline quantitative claims agree with the stronger primary-study sources.

**Evidence**

- It reports approximately +81% improvement for parallel financial analysis and degradation of up to 70% on sequential planning, attributing the difference to decomposability, coordination overhead, and fragmented reasoning. [S31]
- This is consistent with the primary scaling-study evidence identifying strong architecture-by-task interactions and capability saturation. [S23] [S28]

#### Finding 2

**Claim**

The source provides a concrete four-benchmark comparison of architecture choices, suggesting that centralized coordination is particularly effective for decomposable financial analysis, while decentralized coordination may help exploration-oriented browsing.

**Confidence:** Medium

**Why this confidence level**

The pattern is consistent with prior findings, but S31 reproduces values from a secondary chart and does not provide full methods or uncertainty estimates.

**Evidence**

- The reported table shows centralized MAS leading on Finance Agent (+81%), decentralized MAS leading on BrowseComp-Plus (+9%), and all MAS variants underperforming on PlanCraft. [S31]
- Earlier primary-style summaries likewise associate centralized coordination with decomposable tasks and decentralized systems with peer exploration, while warning that no topology is universally best. [S28] [S29] [S30]

#### Finding 3

**Claim**

Error amplification is an important process-level failure mode, and centralized validation may reduce—but not eliminate—propagation.

**Confidence:** Medium

**Why this confidence level**

The qualitative mechanism is corroborated by primary-style sources; the precise 17x and 4x figures are only reported here through a secondary source.

**Evidence**

- S31 reports up to roughly 17-fold error amplification in an unsupervised parallel setup versus approximately 4-fold under centralized orchestration and review. [S31]
- The primary scaling-study material independently identifies error amplification and greater propagation in systems lacking centralized verification. [S23] [S28] [S29]

#### Finding 4

**Claim**

Predictive architecture selection is emerging as an alternative to assuming that more agents or a fixed topology is optimal.

**Confidence:** Medium

**Why this confidence level**

The direction is supported by multiple summaries, but the exact model, target definition, statistical procedure, and relationship to the differing study versions remain unclear.

**Evidence**

- S31 states that a predictive model selected the best configuration for 87% of held-out tasks. [S31]
- The broader scaling-study evidence reports predictive models based on task, capability, and coordination factors, with similar 87% held-out-selection claims. [S28] [S29] [S30]

#### Finding 5

**Claim**

The landscape extends beyond topology to agent training and improvement loops, including process-oriented feedback and continuous training.

**Confidence:** Low

**Why this confidence level**

These additions are relevant to the broader landscape, but S31 is a secondary article and the retrieved content does not establish the underlying methods, independent replication, or whether these techniques are specifically multi-agent rather than general agent training.

**Evidence**

- S31 describes Agent-RRM as providing explicit reasoning traces, focused critiques, and overall scores, and presents Agent Lightning as a framework for wrapping existing agents in training loops. [S31]

### Conflicts Found

- S31 repeats the 180-configuration, four-benchmark version of the scaling study, whereas S23 and S28 report 260 configurations across six benchmarks. The source does not explain whether these are different study versions, subsets, or reporting discrepancies. [S31] [S23] [S28]
- S31 presents precise 17x versus 4x error-amplification figures and a detailed benchmark table, but the retrieved primary-style sources provide only broader claims about error amplification and architecture-dependent performance. The exact figures should not be treated as independently validated. [S31] [S23] [S28] [S29]
- S31 frames richer process feedback and continuous training as major developments, but the accumulated landscape evidence primarily concerns architecture, communication, and evaluation. These training claims therefore broaden the scope without resolving the central topology and fair-comparison questions. [S31] [S11] [S23]

### Important Gaps

- Which scaling-study version is authoritative: the 180-configuration/four-benchmark scope repeated by S31 or the 260-configuration/six-benchmark scope reported by S23 and S28?
- Are the reported 17x and 4x error-amplification values measured under matched prompts, models, tools, and computation, and are they causal effects of topology?
- Do process-oriented reward models and continuous-training frameworks improve multi-agent coordination specifically, or primarily improve individual agent policies?
- Do the reported architecture preferences persist when reasoning tokens, context tokens, tool calls, wall-clock latency, monetary cost, parallel hardware, and safety controls are jointly normalized?
- How well do the reported topology effects generalize to software engineering, scientific discovery, embodied environments, simulation, and long-running tool-use tasks?

**Analysis Duration:** 16.90s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new source adds useful secondary corroboration for task-dependent scaling, error amplification, and predictive architecture selection, but it does not materially resolve the major remaining gaps. The accumulated evidence is sufficient to produce a responsible landscape report: a compositional design graph, task-regime axis, communication and coordination layers, and an explicit evaluation/resource contract. Further searching would be useful for quantitative verification, but is not necessary to answer the original mapping question and the new source does not identify a decisive missing architectural category.

**Next Search**

> Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are. additional evidence search 10

---

# Iteration 10

## 1. Search

**Query**

> Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are. additional evidence search 10

**Why this query**

The new source adds useful secondary corroboration for task-dependent scaling, error amplification, and predictive architecture selection, but it does not materially resolve the major remaining gaps. The accumulated evidence is sufficient to produce a responsible landscape report: a compositional design graph, task-regime axis, communication and coordination layers, and an explicit evaluation/resource contract. Further searching would be useful for quantitative verification, but is not necessary to answer the original mapping question and the new source does not identify a decisive missing architectural category.

**Results**

5 results retrieved.

0 new unique sources added.

### Sources

No new unique sources were added.

**Search Duration:** 3.00s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The accumulated evidence supports a compositional design graph rather than a single hierarchy for mapping multi-agent LLM systems.

**Confidence:** High

**Why this confidence level**

Multiple sources independently describe overlapping dimensions and compositional implementations, making a graph or layered taxonomy better supported than mutually exclusive categories.

**Evidence**

- The landscape contains orthogonal dimensions including baseline choice, control topology, organizational pattern, communication paradigm, protocol, task regime, application domain, and evaluation/resource conditions. [S1] [S2] [S7] [S8] [S9] [S11] [S14] [S23] [S28]
- Concrete systems commonly combine patterns such as planning, specialization, parallel dispatch, verification, shared state, and bounded graph execution. [S1] [S3] [S8] [S9]

#### Finding 2

**Claim**

The core architectural comparison should include single-agent, independent multi-agent, centralized, decentralized, and hybrid systems.

**Confidence:** High

**Why this confidence level**

The five-way classification is explicit and maps consistently onto the broader architectural vocabulary.

**Evidence**

- The scaling-study sources explicitly define these five comparison nodes: unified single-agent reasoning; independently operating agents; orchestrator-worker systems; peer-to-peer systems; and hybrids combining hierarchical oversight with peer communication. [S28] [S29] [S30]
- These nodes subsume or organize earlier patterns such as supervisor-worker, swarm, debate, ensemble, sequential decomposition, and graph orchestration. [S1] [S2] [S3] [S8] [S12] [S18]

#### Finding 3

**Claim**

Agentic task regime is a first-class taxonomy axis and should be distinguished from static reasoning benchmarks.

**Confidence:** High

**Why this confidence level**

The distinction is explicitly defined in the strongest newly accumulated study evidence and is central to interpreting benchmark results.

**Evidence**

- Agentic tasks involve sustained environment interaction, iterative information gathering under partial observability, and adaptive refinement from feedback, unlike static single-shot reasoning tasks. [S23] [S28] [S29] [S30]

#### Finding 4

**Claim**

Multi-agent systems do not provide a universal performance improvement; their value depends on task structure, context conditions, capability, and resource accounting.

**Confidence:** High

**Why this confidence level**

Different studies converge on conditional rather than universal superiority, although exact effect sizes and generalization boundaries remain unsettled.

**Evidence**

- Matched-thinking-token studies found single-agent systems generally matched or outperformed multi-agent variants on the reported multi-hop reasoning tasks. [S14] [S15] [S18]
- The larger agentic scaling study reports strong architecture-by-task interactions, including large gains for decomposable financial analysis and substantial degradation on sequential planning. [S23] [S28] [S29] [S30]
- The evidence attributes these differences to parallelizability, context integration, coordination overhead, tool-use demands, and error propagation. [S14] [S23] [S28] [S29] [S30]

#### Finding 5

**Claim**

Centralized coordination appears promising for decomposable tasks and verification, while decentralized coordination may be useful for exploration and diverse peer perspectives; neither is established as a general winner.

**Confidence:** Medium

**Why this confidence level**

The conditional pattern is supported, but detailed per-topology results and fair cross-domain comparisons are incomplete.

**Evidence**

- Centralized systems reportedly perform best on decomposable financial analysis and can provide orchestration and validation. [S28] [S29] [S30]
- Decentralized systems are associated with peer exploration, debate, and diverse perspectives, particularly in browsing-oriented settings. [S20] [S28] [S29] [S30]
- Earlier sources warn that topology comparisons remain conditional and that decentralized, hierarchical, graph, and debate designs each have distinct failure modes. [S1] [S2] [S5] [S8] [S12]

#### Finding 6

**Claim**

Communication and coordination should be modeled as separate but interacting design dimensions.

**Confidence:** High

**Why this confidence level**

The distinction is explicitly proposed and consistent across protocol, communication, and orchestration sources.

**Evidence**

- Communication taxonomies cover memory sharing, reporting, relay, debate, network topology, payloads, session state, discovery, and schema flexibility. [S7] [S8] [S9]
- Coordination concerns strategic task direction, whereas communication concerns message exchange; conflating them can obscure why architectures differ in cost and reliability. [S7] [S8] [S9] [S20]

#### Finding 7

**Claim**

Coordination creates a capability-versus-overhead trade-off involving context fragmentation, lossy handoffs, synchronization cost, tool-use tax, and error amplification.

**Confidence:** High

**Why this confidence level**

The mechanisms are consistently reported across conceptual, implementation, and empirical evidence.

**Evidence**

- Sources report semantic drift, information loss, aggregation errors, synchronization overhead, and communication bottlenecks. [S1] [S2] [S9] [S14] [S23]
- The scaling-study sources connect architecture-dependent degradation to fragmented reasoning, coordination overhead, and propagation of errors without centralized verification. [S23] [S28] [S29] [S30]

#### Finding 8

**Claim**

The evaluation layer must normalize resources and measure process dynamics, not only final accuracy.

**Confidence:** High

**Why this confidence level**

This methodological requirement is directly supported by controlled comparisons and the proposed comparison-contract framework.

**Evidence**

- Fair comparisons should expose task regime, evidence environment, model, reasoning and context tokens, tool calls, latency, monetary and parallel-hardware costs, output artifact, safety controls, and judging protocol. [S11] [S14] [S23]
- Relevant process metrics include communication overhead, context fragmentation, redundancy, error amplification, reliability, and evidence traceability. [S23] [S28] [S29] [S30]

#### Finding 9

**Claim**

The main open problem is determining when multi-agent specialization or coordination beats a strong single-agent or compound-inference baseline on genuinely agentic tasks under jointly normalized budgets.

**Confidence:** High

**Why this confidence level**

This gap remains central after the accumulated searches and is not resolved by the absence of new usable sources.

**Evidence**

- Existing matched-budget evidence is concentrated on multi-hop reasoning, while broader agentic results are not yet fully reconciled across versions, benchmarks, and resource definitions. [S14] [S18] [S23] [S28] [S29] [S30]
- The accumulated questions explicitly identify unresolved generalization to software engineering, science, embodied environments, simulation, and long-running tool use. [S11] [S14] [S18] [S23]

### Conflicts Found

- Matched-budget multi-hop studies favor single-agent systems, whereas the broader agentic scaling-study sources report substantial multi-agent gains on some decomposable or exploratory tasks. The disagreement is conditional on task regime, context limitations, topology, and resource accounting rather than universal. [S14] [S15] [S18] [S23] [S28] [S29] [S30]
- Different retrieved versions report different study scopes and predictive-fit values: approximately 260 configurations across six benchmarks versus 180 across four benchmarks, with differing reported R² values. The authoritative version and methodological relationship remain unresolved. [S23] [S26] [S27] [S28] [S29] [S30] [S31]
- Secondary sources report precise error-amplification and topology-specific performance figures, but the available primary-style evidence supports only the qualitative mechanisms and broader trends. Exact figures should not be treated as independently validated. [S23] [S28] [S29] [S31]
- Practitioner and overview sources sometimes imply hierarchical or graph architectures are generally preferable in production, while survey and empirical sources treat decentralized, hybrid, and peer-oriented systems as conditionally viable. No evidence establishes a universal topology winner. [S1] [S2] [S5] [S8] [S20] [S28] [S29]

### Important Gaps

- Which version of the scaling study is authoritative, and why do the retrieved sources disagree on benchmark count, configuration count, and R²?
- Do topology-specific effects persist when reasoning tokens, context tokens, tool calls, wall-clock latency, monetary cost, parallel hardware, and safety controls are jointly normalized?
- Do the results generalize beyond multi-hop QA and the currently reported agentic benchmarks to software engineering, scientific discovery, embodied environments, simulation, and long-running workflows?
- Which communication and context-management mechanisms preserve information while limiting drift, contamination, synchronization cost, and error propagation?
- Does centralized verification causally reduce error amplification, or is its apparent benefit confounded by prompts, model allocation, or additional computation?
- Which process metrics best predict architecture choice and success: decomposability, context fragmentation, coordination overhead, redundancy, diversity, or task-grounded capability?
- Which benefits are task-performance gains versus engineering benefits such as modularity, auditability, interoperability, fault isolation, and human fallback?
- How should evaluations measure collusion, correlated failures, premature consensus, adversarial message propagation, privacy, and governance under comparable budgets?

**Analysis Duration:** 19.91s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The runner reached the maximum research iteration budget. Analyzer assessment: No usable new sources were retrieved. The landscape taxonomy itself is sufficiently supported, but an important quantitative gap remains: the primary scaling-study version, methods, budget normalization, and cross-domain generalization have not been fully reconciled. Resolving this would materially improve the report's empirical foundation and prevent overclaiming topology-specific effects.

**Stop Reason:** max_iterations

---

# Final Research Decision

**Research Stopped Because**

The runner reached the maximum research iteration budget.

**Stop Reason:** max_iterations

**Searches Performed:** 10

**Unique Sources:** 31

**Remaining Uncertainty**

- Reconcile the authoritative version, benchmark scope, configuration count, budget definitions, and predictive metrics of the central scaling study.
- Run independent cross-domain evaluations covering software engineering, scientific discovery, embodied environments, simulation, and long-running tool-use workflows.
- Jointly normalize reasoning tokens, prompt/context tokens, tool calls, wall-clock latency, monetary cost, parallel hardware, and security controls.
- Test whether centralized verification causally reduces error amplification, rather than merely correlating with different prompts, model allocations, or compute levels.
- Identify which process metrics best predict architecture choice: task decomposability, context fragmentation, coordination overhead, redundancy, diversity, error amplification, or task-grounded capability.
- Determine which communication protocols and context-management mechanisms preserve task-relevant information while limiting semantic drift, contamination, synchronization cost, and privacy risks.
- Separate performance benefits from engineering benefits such as modularity, interoperability, auditability, fault isolation, and human fallback.
- Develop evaluations for collusion, correlated failures, premature consensus, adversarial message propagation, privacy, policy enforcement, and governance.
- Validate whether process-oriented training and continuous-improvement methods improve multi-agent coordination specifically or mainly improve individual-agent policies.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 10 | 31.42s |
| OpenAI Analysis | 10 | 179.90s |
| Report Generation | 1 | 36.01s |
| Total Run | — | 247.34s |
