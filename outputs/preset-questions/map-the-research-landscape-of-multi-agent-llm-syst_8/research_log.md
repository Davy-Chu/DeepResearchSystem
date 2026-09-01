# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are.

**Status:** Completed

**Stop Reason:** sufficient_evidence

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 7 / 10

**Unique Sources:** 29

**OpenAI Calls:** 8

**Tavily Calls:** 7

**Started:** 2026-09-01T02:51:14-04:00

**Ended:** 2026-09-01T02:54:20-04:00

**Total Runtime:** 185.75s

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
- **S2 — LLM Agent Orchestration Patterns: Architectural Frameworks for Managing Complex Multi-Agent Systems**
  URL: https://www.c-sharpcorner.com/article/llm-agent-orchestration-patterns-architectural-frameworks-for-managing-complex
- **S3 — Medium**
  URL: https://medium.com/data-science-collective/building-a-multi-agent-deep-research-agent-with-langgraph-203547b5fb12
- **S4 — LLM-Enabled Multi-Agent Systems: Empirical Evaluation and Insights into Emerging Design Patterns & Paradigms**
  URL: https://arxiv.org/html/2601.03328v1
- **S5 — From RAG to Multi-Agent Systems: A Survey of Modern Approaches in LLM Development**
  URL: https://www.preprints.org/manuscript/202502.0406

**Search Duration:** 3.07s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The retrieved material frames multi-agent LLM systems primarily as compositions of agent roles, communication mechanisms, and control-flow topologies rather than as a single architecture.

**Confidence:** Medium

**Why this confidence level**

Multiple sources converge on architectural dimensions, but the sources differ in terminology and some are non-peer-reviewed or practitioner-oriented.

**Evidence**

- The empirical survey identifies agent orchestration, communication mechanisms, and control-flow strategies as key architectural components of LLM-enabled multi-agent systems. [S4]
- The orchestration article organizes systems into centralized, decentralized, specialized, and hybrid categories. [S2]
- The taxonomy guide groups patterns into single-agent, collaborative multi-agent, competitive multi-agent, and orchestration-topology quadrants. [S1]

#### Finding 2

**Claim**

A useful high-level taxonomy includes centralized hierarchical systems, decentralized or swarm-like systems, specialized/parallel systems, competitive or critique-based systems, and graph/workflow-based hybrids.

**Confidence:** Medium

**Why this confidence level**

The categories are supported across sources, but the retrieved content does not establish a standardized field-wide taxonomy or provide full details for every topology.

**Evidence**

- S2 explicitly distinguishes centralized, decentralized, specialized, and hybrid orchestration models. [S2]
- S1 describes plan-and-execute, supervisor-worker, multi-agent debate, and verifier-critic patterns, while noting that production systems often compose several patterns. [S1]
- S3 presents a graph workflow combining classification, planning, parallel specialist agents, gap analysis, citation auditing, synthesis, writing, and refinement. [S3]
- S4 describes networks of specialist agents that hand off subtasks and emphasizes repeatable design patterns for domain-specific pipelines. [S4]

#### Finding 3

**Claim**

Supervisor-worker and graph/workflow architectures provide explicit decomposition and control, while parallel specialist designs trade coordination complexity for task specialization and concurrency.

**Confidence:** Medium

**Why this confidence level**

The architectural mechanisms are directly described, but comparative performance evidence between these designs is limited.

**Evidence**

- S1 characterizes supervisor-worker systems as hierarchical decomposition with specialized workers, and graph topologies as production-relevant orchestration patterns. [S1]
- S3 uses an architect to dispatch multiple role-specialized researchers in parallel, followed by gap analysis, citation auditing, synthesis, and refinement. [S3]
- S4 attributes MAS efficiency to division of labor, with complex tasks divided among specialized agents connected in a network. [S4]

#### Finding 4

**Claim**

Critique-oriented architectures are intended to improve reliability through adversarial review, verification, or revision, but they introduce extra latency and may share correlated failures.

**Confidence:** Medium

**Why this confidence level**

Failure modes and intended benefits are consistently described, but the retrieved sources do not provide robust controlled evidence quantifying reliability gains.

**Evidence**

- S1 describes multi-agent debate and verifier-critic as competitive/adversarial patterns for quality and safety, and lists premature convergence, judge bias, collusion, and over-correction as failure modes. [S1]
- S3 structurally requires citation auditing before writing and assigns a skeptic role to identify weak claims, illustrating a critique-and-verification design. [S3]
- S5 states that collaboration may mitigate hallucinations, while surveying open challenges in multi-agent architectures. [S5]

#### Finding 5

**Claim**

The central open problems are semantic coordination, context and protocol management, reliability under variable LLM behavior, cost/latency scaling, and production governance.

**Confidence:** High

**Why this confidence level**

The same broad problem areas recur across academic-style, survey, engineering, and practitioner sources, although their severity and proposed solutions are not consistently evaluated.

**Evidence**

- S2 identifies contextual drift, semantic interpretation mismatch, protocol-related semantic loss, and token-consumption/resource optimization as challenges in LLM-agent networks. [S2]
- S4 reports that variable LLM behavior complicates the transition from prototypes to production and calls for advances in reliability, scalability, and governance. [S4]
- S3 highlights citation discipline, gap detection, termination guarantees, partial-failure handling, and runaway research-loop costs as engineering concerns. [S3]
- S5 includes context management, agent architectures, frameworks, and open challenges as major areas in the modern LLM development landscape. [S5]

#### Finding 6

**Claim**

The evidence supports a design graph in which a single-agent baseline can escalate to planning, parallel specialization, hierarchical supervision, graph/workflow orchestration, and optional debate or verifier loops, with shared communication, memory/context, evaluation, and governance layers.

**Confidence:** Medium

**Why this confidence level**

The graph is a defensible synthesis of the retrieved evidence, but it is not itself presented as a validated canonical model by the sources.

**Evidence**

- S1 recommends establishing a single-agent baseline before adding multi-agent coordination and describes compositions across patterns. [S1]
- S3 demonstrates a concrete graph that combines routing, planning, parallel specialists, auditing, synthesis, and refinement. [S3]
- S4 identifies orchestration, communication, and control flow as cross-cutting components of MAS design. [S4]
- S2’s centralized, decentralized, specialized, and hybrid categories support treating topology as a composable design choice. [S2]

### Conflicts Found

- S1 claims that eight canonical patterns cover approximately 95% of production agent systems and that hierarchical or graph topologies generally outperform swarms, whereas the other sources present broader or different taxonomies and provide no evidence supporting those quantitative or dominance claims. [S1] [S2] [S4] [S5]
- S1 recommends starting with a single-agent baseline and escalating only when failure modes are decomposable; S5 emphasizes that multi-agent systems can handle intricate tasks, improve scalability, and mitigate hallucinations, but the retrieved material does not resolve when those benefits outweigh coordination cost. [S1] [S5]
- S2 reports large operational improvements, including reduced completion time, semantic errors, token cost, and increased ROI, while S4 describes promising prototype delivery but stresses difficulty achieving production maturity. These claims are not directly comparable because their evaluation settings and metrics are unspecified. [S2] [S4]
- S1 presents its taxonomy as stabilized in 2024–2026, but S1 is a practitioner guide published in 2026 and its retrieved excerpt does not provide enough methodological detail to establish field-wide consensus; S4 and S5 instead describe the design-pattern landscape as emerging and still requiring formalization. [S1] [S4] [S5]

### Important Gaps

- What is the complete set of patterns in S1? The retrieved excerpt ends during the verifier-critic discussion and does not show patterns 7–8.
- Which architecture performs best under controlled comparisons for accuracy, cost, latency, robustness, and human oversight?
- How should communication protocols, shared memory, context windows, and state synchronization be designed to prevent semantic drift and information loss?
- What benchmarks and evaluation methodologies measure coordination quality, error propagation, emergent behavior, and failure recovery across multi-agent systems?
- When does adding agents improve outcomes relative to a strong single-agent or RAG baseline, and how does this vary by task decomposition quality?
- What governance, security, privacy, and human-in-the-loop mechanisms are required for deployment in high-stakes domains?
- Are the large percentage improvements reported by S2 independently reproduced, and what were the baselines, workloads, sample sizes, and cost accounting methods?
- How do model heterogeneity, critic independence, tool reliability, and adversarial or malicious agents affect system safety?

**Analysis Duration:** 20.11s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

A further search would materially improve the report by supplying peer-reviewed or benchmark-based evidence on comparative architecture performance, evaluation criteria, and open problems. The current sources support a provisional taxonomy and design graph, but include practitioner material, a non-peer-reviewed preprint, incomplete excerpts, and unsupported aggregate performance claims.

**Next Search**

> LLM multi-agent systems architecture taxonomy benchmark centralized decentralized supervisor swarm debate evaluation cost reliability

---

# Iteration 2

## 1. Search

**Query**

> LLM multi-agent systems architecture taxonomy benchmark centralized decentralized supervisor swarm debate evaluation cost reliability

**Why this query**

A further search would materially improve the report by supplying peer-reviewed or benchmark-based evidence on comparative architecture performance, evaluation criteria, and open problems. The current sources support a provisional taxonomy and design graph, but include practitioner material, a non-peer-reviewed preprint, incomplete excerpts, and unsupported aggregate performance claims.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S6 — Benchmarking Multi-Agent Architectures**
  URL: https://www.langchain.com/blog/benchmarking-multi-agent-architectures
- **S7 — Single Agent vs Multi-Agent Systems 2026: When Swarms Help**
  URL: https://swarmsignal.net/single-vs-multi-agent-comparison-2026
- **S8 — Medium**
  URL: https://medium.com/mitb-for-all/a-field-guide-to-multi-agent-architectures-f6f8c689c406
- **S9 — Multi-Agent Debate Strategies: Survey, Taxonomy, and Challenges**
  URL: https://arxiv.org/html/2607.26212v1
- **S10 — Architectures for Multi-Agent Systems**
  URL: https://galileo.ai/blog/architectures-for-multi-agent-systems

**Search Duration:** 2.88s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The research landscape is best represented as a set of composable architectural dimensions rather than a single canonical taxonomy: control topology, delegation/control flow, communication and memory, specialization, and verification/agreement.

**Confidence:** High

**Why this confidence level**

The dimensions are supported by multiple sources and S9 provides a systematic treatment of a major subfield, although no source establishes a universally accepted taxonomy.

**Evidence**

- The prior sources identify orchestration, communication mechanisms, and control-flow strategies as core components, while distinguishing centralized, decentralized, specialized, competitive, and hybrid systems. [S1] [S2] [S4]
- The debate survey defines debate configurations through participant structure, interaction mechanisms, and agreement protocols, adding dimensions that apply specifically to critique-oriented systems. [S9]

#### Finding 2

**Claim**

A useful top-level taxonomy contains centralized hierarchical orchestration, explicit graph/workflow orchestration, decentralized or swarm-like interaction, parallel specialist composition, and adversarial/debate or verifier-critic loops; these patterns can be combined.

**Confidence:** High

**Why this confidence level**

The major families recur across independent sources, though labels such as swarm, decentralized, and collaborative are not used consistently.

**Evidence**

- The prior sources distinguish centralized, decentralized, specialized, hybrid, supervisor-worker, debate, verifier-critic, and graph/workflow patterns. [S1] [S2] [S3] [S4]
- S8 separately describes hierarchical systems, explicit multi-agent workflows, and agent swarms, and presents them as alternative organizational patterns. [S8]
- S9 surveys multi-agent debate as a distinct architecture family organized by participants, interaction, and agreement resolution. [S9]

#### Finding 3

**Claim**

Hierarchical supervisor-worker systems provide modular delegation and clear accountability but create routing bottlenecks and a central point of failure.

**Confidence:** High

**Why this confidence level**

The tradeoff is directly and consistently described by two architecture-focused sources.

**Evidence**

- S8 describes supervisors delegating to specialist agents and notes modularity and extensibility, while identifying the supervisor as a routing bottleneck and single point of failure. [S8]
- S10 characterizes centralized systems as predictable and debuggable because routing and global state are centralized, but reports bottleneck and failure risks as the number of agents grows. [S10]

#### Finding 4

**Claim**

Explicit graph/workflow architectures offer stronger control-flow boundaries, concurrency, auditability, and termination control than unconstrained supervisor systems, but require developers to specify branching, synchronization, recovery, and refinement behavior.

**Confidence:** High

**Why this confidence level**

The architectural distinction is directly illustrated and conceptually consistent across sources.

**Evidence**

- S8 states that explicit workflows define permitted nodes, edges, branches, convergence points, and termination, but cannot invent new control flow unless it is explicitly implemented. [S8]
- The prior graph example combines planning, parallel specialists, auditing, synthesis, and refinement, illustrating how multiple patterns can be encoded into one controlled workflow. [S3]

#### Finding 5

**Claim**

Parallel specialization is most plausibly beneficial when subtasks are genuinely independent or decomposable; it is not established as superior for sequential reasoning.

**Confidence:** Medium

**Why this confidence level**

The task-structure hypothesis is supported by convergent design reasoning, but quantitative comparative evidence is incomplete and S7's strong numerical claims cannot be independently assessed from the retrieved content.

**Evidence**

- S6 motivates multi-agent systems partly through context and tool-count scaling, modularity, maintainability, and parallelization, and reports experiments on a modified τ-bench benchmark, but the retrieved excerpt does not include the benchmark results. [S6]
- S7 claims large gains on parallelizable tasks and degradation on sequential tasks, but presents these claims through a practitioner article whose underlying study details are not included in the retrieved content. [S7]
- S1 recommends establishing a strong single-agent baseline and adding agents when failure modes are decomposable. [S1]

#### Finding 6

**Claim**

Debate and critique architectures constitute a substantial research sublandscape, but their design space is under-specified and poorly standardized.

**Confidence:** High

**Why this confidence level**

S9 offers the strongest systematic evidence in the retrieved set, while the failure-mode evidence is consistent with prior sources.

**Evidence**

- S9 reports a systematic review of 141 primary studies and proposes three dimensions: debate participants, interaction mechanisms, and agreement protocols. [S9]
- S9 states that studies commonly use static fully connected topologies, verbatim exchange, short-term memory, and voting, while alternative configurations remain marginal and cross-study comparison is unreliable when design decisions are implicit. [S9]
- Prior sources identify judge bias, collusion, premature convergence, over-correction, latency, and correlated failures as debate or verifier-critic risks. [S1] [S3]

#### Finding 7

**Claim**

The principal open problems span coordination semantics, context and memory management, reliability and failure recovery, cost/latency scaling, evaluation, and deployment governance.

**Confidence:** High

**Why this confidence level**

These gaps recur across survey, engineering, and architecture sources, and S9 adds a systematic evaluation and specification gap.

**Evidence**

- Prior sources identify contextual drift, semantic mismatch, protocol loss, variable model behavior, token costs, termination, partial failures, reliability, scalability, and governance as unresolved issues. [S2] [S3] [S4] [S5]
- S9 specifically calls for executable debate specifications, cost-aware benchmarking, and automated tuning because interacting design choices currently impede reliable comparison. [S9]
- S8 emphasizes that explicit workflows shift responsibility for orchestration, concurrency, and recovery to system designers. [S8]

### Conflicts Found

- S7 makes strong quantitative claims that centralized multi-agent systems improve parallelizable tasks by 80.9% but degrade sequential reasoning by 39–70%, while S6 says it benchmarked modified τ-bench but the retrieved excerpt does not provide outcomes. These claims cannot yet be treated as independently corroborated. [S6] [S7]
- S10 asserts that token usage accounts for 80% of performance variance and that centralized orchestration bottlenecks at roughly 10–20 agents, while the other retrieved sources do not establish these figures. They should be treated as source-specific practitioner claims rather than field-wide results. [S10] [S1] [S2] [S4] [S9]
- S8 presents hierarchical systems as common in the author's practical experience but explicitly says there are no official prevalence statistics; this qualifies any claim that hierarchy is the dominant architecture in the field. [S8] [S1] [S4]
- S9 characterizes debate literature as converging on narrow conventional configurations, whereas S1 presents debate and verifier-critic as only some members of a broader production-pattern taxonomy. This is a scope difference rather than a direct contradiction: S9 focuses on MAD, while S1 covers multi-agent systems generally. [S1] [S9]

### Important Gaps

- What are the actual comparative results, baselines, workloads, sample sizes, and cost accounting in S6's modified τ-bench benchmark?
- Are S7's numerical scaling claims supported by a peer-reviewed or fully inspectable study, and do they generalize beyond the cited task types?
- Which topology and communication protocol performs best under controlled comparisons across accuracy, latency, cost, robustness, and auditability?
- When does multi-agent decomposition outperform a strong single-agent, tool-using, or RAG baseline?
- How should shared memory, message schemas, context compression, and state synchronization prevent semantic drift and correlated failures?
- How can debate configurations be benchmarked while varying topology, number and diversity of agents, rounds, memory, exchange format, and agreement protocol independently?
- What standards address security, privacy, authorization, malicious agents, tool failures, human oversight, and rollback in production deployments?
- What evidence supports prevalence claims about hierarchical, workflow, swarm, or debate architectures across real systems?

**Analysis Duration:** 21.77s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources materially improve the taxonomy—especially by adding a systematic debate taxonomy and clearer distinctions between supervisor and explicit workflow designs—but the most important landscape question remains unresolved: controlled, inspectable evidence comparing architectures. S6 is especially promising but its retrieved content stops before benchmark results, while S7 provides strong figures without sufficient methodological detail. One focused search should target the underlying benchmark results and study.

**Next Search**

> LangChain Benchmarking Multi-Agent Architectures modified tau-bench results supervisor parallel agents score token cost June 2025

---

# Iteration 3

## 1. Search

**Query**

> LangChain Benchmarking Multi-Agent Architectures modified tau-bench results supervisor parallel agents score token cost June 2025

**Why this query**

The new sources materially improve the taxonomy—especially by adding a systematic debate taxonomy and clearer distinctions between supervisor and explicit workflow designs—but the most important landscape question remains unresolved: controlled, inspectable evidence comparing architectures. S6 is especially promising but its retrieved content stops before benchmark results, while S7 provides strong figures without sufficient methodological detail. One focused search should target the underlying benchmark results and study.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S11 — Tau-bench Leaderboard**
  URL: https://llm-stats.com/benchmarks/tau-bench
- **S12 — HAL: TAU-bench Airline**
  URL: https://hal.cs.princeton.edu/taubench_airline
- **S13 — Evaluating Multi-Agent Architectures: A Performance Benchmark - Blockchain.News**
  URL: https://blockchain.news/news/evaluating-multi-agent-architectures-performance-benchmark
- **S14 — Benchmarking Multi-Agent LLM Architectures for Financial Document Processing: A Comparative Study of Orchestration Patterns, Cost-Accuracy Tradeoffs and Production Scaling Strategies**
  URL: https://arxiv.org/html/2603.22651v1

**Search Duration:** 2.86s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

New evidence strengthens the case for empirical comparison of orchestration patterns, especially sequential, parallel, hierarchical, and reflexive/self-correcting designs, rather than relying only on conceptual taxonomies.

**Confidence:** Medium

**Why this confidence level**

The sources describe concrete comparative studies, but S13 is a secondary report and the retrieved S14 content has not been independently corroborated here.

**Evidence**

- S14 reports a benchmark comparing sequential pipelines, parallel fan-out/merge, hierarchical supervisor-worker, and reflexive loops across five models, 10,000 SEC filings, 25 extraction field types, and metrics including F1, accuracy, latency, cost, and token efficiency. [S14]
- S13 reports a LangChain comparison of single-agent, swarm, and supervisor architectures on a modified τ-bench dataset containing retail, flight-booking, tech-support, and automotive scenarios. [S13]

#### Finding 2

**Claim**

In the financial-document benchmark described by S14, reflexive/self-correcting loops achieved the highest reported extraction F1, while hierarchical systems offered the most favorable reported cost-accuracy tradeoff.

**Confidence:** Low

**Why this confidence level**

The numerical results are direct claims in one newly retrieved source, but no independent source, detailed tables, statistical intervals, or inspectable experimental traces are provided in the retrieved content.

**Evidence**

- S14 reports field-level F1 of 0.943 for reflexive architectures at 2.3 times the sequential-baseline cost, versus F1 0.921 for hierarchical architectures at 1.4 times cost; it characterizes hierarchical systems as lying on the favorable cost-accuracy Pareto frontier. [S14]

#### Finding 3

**Claim**

The new benchmark evidence supports hybrid architectures that combine orchestration with caching, routing, and adaptive retries as a promising open design direction for improving the cost-accuracy frontier.

**Confidence:** Low

**Why this confidence level**

Both sources suggest the direction, but the quantitative S14 result is uncorroborated and S13 does not provide full experimental details.

**Evidence**

- S14 claims that combining semantic caching, model routing, and adaptive retries recovered 89% of reflexive accuracy gains at 1.15 times baseline cost. [S14]
- S13 reports that supervisor performance improved after information-handling and context-management changes, and identifies removal or optimization of supervisor translation layers as a future direction. [S13]

#### Finding 4

**Claim**

τ-bench provides evidence that reliability and policy-following remain difficult even for strong tool-using agents, making reliability evaluation a central layer in the multi-agent research landscape.

**Confidence:** High

**Why this confidence level**

S11 and S12 independently describe the benchmark’s purpose and reliability focus; S12 additionally reports verified results, though these are domain-specific and do not directly compare multi-agent topologies.

**Evidence**

- S11 describes τ-bench as testing dynamic user interaction, domain-specific policies, API tools, consistency, and multi-trial reliability; its cited source-paper summary reports fewer than 50% task success for prior state-of-the-art function-calling agents and pass^8 below 25% in retail. [S11]
- S12 provides a public airline-domain evaluation with 26 tasks and reports verified accuracies ranging from 36% to 56% across listed agent/model configurations, with costs ranging from $5.43 to $180.49 for the displayed runs. [S12]

#### Finding 5

**Claim**

The new sources do not establish that swarm, supervisor, hierarchical, or reflexive architectures universally dominate; benefits appear task- and implementation-dependent.

**Confidence:** High

**Why this confidence level**

The sources provide contrasting conditional outcomes and explicitly measured tradeoffs, even though their tasks and experimental setups are not directly comparable.

**Evidence**

- S13 reports that swarm slightly outperformed supervisor in its modified τ-bench comparison, while supervisor issues were partly mitigated through context-management improvements. [S13]
- S14 reports a reflexive accuracy advantage but a hierarchical cost advantage in financial extraction, implying different winners under different objectives. [S14]
- S12 compares agent scaffolds and models on airline tasks but does not isolate topology effects across matched models and workloads. [S12]

### Conflicts Found

- S14 reports reflexive loops as highest accuracy and hierarchical systems as best cost-accuracy tradeoff in financial extraction, whereas S13 reports swarm slightly outperforming supervisor on a modified τ-bench task. This is likely a conditional task and implementation difference, not a direct contradiction, but it prevents a universal architecture ranking. [S13] [S14]
- S11’s third-party leaderboard reports a current leader score of 0.882 and says its results are self-reported, while S12’s HAL leaderboard reports verified airline-domain accuracies of at most 56% for the displayed runs. The figures are not directly comparable because the pages may use different τ-bench domains, tasks, scaffolds, model versions, and scoring aggregation. [S11] [S12]
- S14 makes strong claims about a 10,000-document, 500-configuration benchmark and precise cost/accuracy improvements, but the retrieved material does not provide enough methodological detail or independent corroboration to resolve whether those figures generalize beyond financial extraction. [S14]

### Important Gaps

- Can the primary LangChain benchmark source be inspected to verify the modified τ-bench task construction, matched model conditions, statistical significance, and complete results for single-agent, swarm, and supervisor systems?
- Are S14's reported numerical results independently reproducible, and do they generalize beyond financial-document extraction, the listed models, and the stated throughput range?
- How much of the observed advantage comes from topology itself versus prompt design, model selection, routing, context management, retry policy, or evaluator implementation?
- Can multi-agent architectures be compared on common workloads using verified accuracy, pass^k-style reliability, latency, token cost, failure recovery, and auditability metrics?
- What architectural interventions improve τ-bench-style policy adherence and multi-trial consistency specifically, rather than only single-run task success?

**Analysis Duration:** 15.11s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources materially improve the landscape by adding task-specific comparative evidence and verified reliability measurements, but the most important controlled architecture comparison (S13) is available only through a secondary report, while S14's strong results are currently single-source claims. A focused search for the primary LangChain study would improve confidence without reopening the entire taxonomy.

**Next Search**

> LangChain benchmarking multi-agent architectures Tau-bench single agent swarm supervisor primary study results

---

# Iteration 4

## 1. Search

**Query**

> LangChain benchmarking multi-agent architectures Tau-bench single agent swarm supervisor primary study results

**Why this query**

The new sources materially improve the landscape by adding task-specific comparative evidence and verified reliability measurements, but the most important controlled architecture comparison (S13) is available only through a secondary report, while S14's strong results are currently single-source claims. A focused search for the primary LangChain study would improve confidence without reopening the entire taxonomy.

**Results**

5 results retrieved.

2 new unique sources added.

### Sources

- **S15 — Benchmarking Single Agent Performance - LangChain**
  URL: https://www.langchain.com/blog/react-agent-benchmarking
- **S16 — 𝜏-Bench: Benchmarking AI agents for the real-world | Sierra**
  URL: https://sierra.ai/blog/benchmarking-ai-agents

**Search Duration:** 2.76s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Single-agent systems degrade as the number of domains, instructions, and tools increases, strengthening the case for decomposition or multi-agent escalation when responsibilities become too broad.

**Confidence:** Medium

**Why this confidence level**

The evidence directly supports overload as a design concern, but it comes from one practitioner study using an internal email-assistant task family; generalization across models and workloads is uncertain.

**Evidence**

- LangChain’s single-agent study explicitly tests when a ReAct agent becomes overloaded and concludes that more context and tools degrade performance, with longer trajectories degrading more quickly. [S15]
- The study defines domains as bundles of instructions and tools, directly linking performance degradation to expanding responsibility scope. [S15]

#### Finding 2

**Claim**

Single-agent baselines remain essential in the taxonomy because multi-agent decomposition should be justified against the performance loss caused by excessive context, tools, or trajectory length.

**Confidence:** High

**Why this confidence level**

The recommendation is supported by both the new empirical motivation and prior architectural guidance, although the precise escalation threshold remains unknown.

**Evidence**

- S15 frames the central architectural choice as a single agent with many tools versus multiple agents with clearer domains of responsibility. [S15]
- Prior evidence recommends establishing a strong single-agent baseline before adding agents, particularly when failure modes are not decomposable. [S1]

#### Finding 3

**Claim**

τ-bench is a particularly relevant evaluation layer for multi-agent systems because it measures dynamic user interaction, programmatic tool use, policy adherence, state correctness, and repeated-trial reliability rather than only conversational quality.

**Confidence:** High

**Why this confidence level**

The benchmark design and metrics are described directly by the benchmark authors’ source and align with the previously retrieved τ-bench evidence.

**Evidence**

- τ-bench combines realistic databases and APIs, domain-specific policies, and an LLM-based user simulator; evaluation compares the final database state with the expected goal state. [S16]
- The benchmark introduces pass^k to measure whether an agent repeatedly completes the same task successfully, addressing reliability beyond average single-run success. [S16]

#### Finding 4

**Claim**

Simple function-calling and ReAct agents perform poorly on realistic, policy-constrained, multi-turn tasks, indicating that reliability—not only task capability—is a major motivation for richer orchestration architectures.

**Confidence:** High

**Why this confidence level**

The claims are directly reported in the benchmark source, though they characterize baseline agents and do not by themselves prove that any particular multi-agent topology solves the problem.

**Evidence**

- S16 reports that all 12 evaluated models had difficulty on τ-bench and that the best reported GPT-4o agent achieved under 50% average success across the retail and airline domains. [S16]
- S16 states that the benchmark targets long-horizon interaction, complex domain policies, and consistency at scale, and reports that ReAct did not significantly improve results over function calling in the displayed comparison. [S16]

#### Finding 5

**Claim**

The new sources reinforce a landscape organized around a progression from single-agent systems to decomposed or multi-agent architectures, but they do not identify a universally superior architecture.

**Confidence:** High

**Why this confidence level**

The sources jointly support the motivation for architectural diversity while preserving the previously identified task- and implementation-dependent results.

**Evidence**

- S15 documents degradation under growing single-agent scope, motivating domain-specialized decomposition. [S15]
- S16 demonstrates substantial reliability limitations in simple agent constructs, while prior comparative evidence shows different winners for swarm, hierarchical, and reflexive designs depending on task and objective. [S16] [S13] [S14]

### Conflicts Found

- S15 studies overload in a single ReAct agent, whereas S16 reports poor performance for simple function-calling/ReAct agents on τ-bench. These findings are compatible, but neither establishes that a specific multi-agent architecture reliably outperforms the single-agent baseline under matched conditions. [S15] [S16]
- S15 evaluates instruction and tool scaling in an internal email-assistant setting, while S16 evaluates realistic simulated-user/tool interactions in retail and airline domains. Their degradation and success-rate findings should not be treated as directly comparable performance measurements. [S15] [S16]

### Important Gaps

- At what measurable level of domain count, tool count, context length, or trajectory length should a system switch from one agent to multiple agents?
- Do supervisor, workflow, swarm, debate, or reflexive architectures improve τ-bench pass^k and policy adherence relative to a carefully matched single-agent baseline?
- How much of any multi-agent improvement is caused by decomposition itself versus better prompts, context management, routing, retries, or model selection?
- Can the results from S15’s internal email-assistant tasks and S16’s retail/airline benchmark generalize to research, coding, planning, and high-stakes decision tasks?

**Analysis Duration:** 13.44s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources improve the evidence for single-agent overload and reliability-focused evaluation, but the central comparative gap remains: there is no independently verified, controlled comparison of major multi-agent topologies against strong single-agent baselines across common tasks and metrics.

**Next Search**

> controlled benchmark single-agent supervisor swarm workflow debate multi-agent LLM pass^k cost latency reliability matched comparison

---

# Iteration 5

## 1. Search

**Query**

> controlled benchmark single-agent supervisor swarm workflow debate multi-agent LLM pass^k cost latency reliability matched comparison

**Why this query**

The new sources improve the evidence for single-agent overload and reliability-focused evaluation, but the central comparative gap remains: there is no independently verified, controlled comparison of major multi-agent topologies against strong single-agent baselines across common tasks and metrics.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S17 — How to Orchestrate Multi-Agent Systems in LangGraph (Supervisor vs Swarm Patterns) | Focused**
  URL: https://focused.io/lab/multi-agent-orchestration-in-langgraph-supervisor-vs-swarm-tradeoffs-and-architecture
- **S18 — Swarm vs. Supervisor: Multi-Agent Architecture Guide**
  URL: https://www.augmentcode.com/guides/swarm-vs-supervisor
- **S19 — Medium**
  URL: https://medium.com/@mjgmario/single-agent-vs-multi-agent-systems-when-coordination-helps-hurts-and-pays-off-57735ee7916d
- **S20 — Rethinking the Value of Multi-Agent Workflow: A Strong Single Agent Baseline**
  URL: https://arxiv.org/html/2601.12307v1
- **S21 — Comparing Single-Agent and Multi-Agent Strategies in ...**
  URL: https://www.mdpi.com/2079-9292/15/8/1661

**Search Duration:** 2.62s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

New evidence reinforces that architecture choice should be conditioned on task structure, especially dependency structure, rather than on agent count alone.

**Confidence:** Medium

**Why this confidence level**

The task-structure principle is consistent across sources, but S17 and S18 are practitioner sources and their reported measurements are not independently validated.

**Evidence**

- S18 states that swarms fit relatively independent workloads with distributed handoffs, whereas supervisors fit dynamic routing, ordered execution, and conflict resolution; it also recommends hybrids for supervisor planning with parallel execution. [S18]
- S17 reports a customer-service comparison in which swarm had lower latency and token use, while supervisor had higher routing accuracy, illustrating a speed-versus-routing-quality tradeoff. [S17]
- Prior evidence similarly found different winners across swarm, hierarchical, and reflexive systems depending on workload and objective. [S13] [S14]

#### Finding 2

**Claim**

Swarm is a decentralized sequential handoff topology and should not be conflated with fan-out parallelism.

**Confidence:** High

**Why this confidence level**

The conceptual distinction is explicit in S18 and agrees with the accumulated taxonomy.

**Evidence**

- S18 explicitly distinguishes swarm handoffs, in which one agent is active at a time, from fan-out parallelism, in which multiple agents execute simultaneously under coordination. [S18]
- The prior taxonomy separately identified decentralized/swarm systems and parallel specialist composition. [S1] [S2] [S3] [S8]

#### Finding 3

**Claim**

Supervisor architectures improve routing visibility, ordering, validation, and conflict handling, but incur coordination overhead and can become bottlenecks or loop indefinitely without safeguards.

**Confidence:** High

**Why this confidence level**

The tradeoff is supported by multiple sources, although the numerical S17 results are source-specific.

**Evidence**

- S18 assigns supervisors dynamic routing, output validation/order enforcement, and conflict or loop prevention, while warning that central coordination adds overhead for parallel work. [S18]
- S17 reports more LLM calls, latency, and tokens for supervisor routing than swarm handoffs, but higher routing accuracy in its customer-service prototype. [S17]
- Prior sources identify supervisor bottlenecks, central failure points, and routing overhead as principal limitations. [S8] [S10]

#### Finding 4

**Claim**

A major unresolved distinction in the landscape is between architectural topology and execution shape: decentralized handoff, centralized fan-out, sequential pipelines, and reflexive loops represent different dimensions that can be composed.

**Confidence:** High

**Why this confidence level**

Several sources directly support treating topology, execution, communication, and verification as separate but composable axes.

**Evidence**

- S18 separates swarm topology from fan-out execution and describes their different routing authorities and concurrency models. [S18]
- S19 describes single-agent, independent, centralized, decentralized, and hybrid configurations, while distinguishing orchestrator presence from peer communication. [S19]
- Prior sources organize systems using topology, control flow, specialization, communication, memory, and verification dimensions rather than one canonical taxonomy. [S1] [S4] [S9]

#### Finding 5

**Claim**

Controlled benchmark evidence, as reported by S19, suggests that multi-agent benefits are highly task-dependent: centralized systems performed strongly on decomposable financial analysis, decentralized systems helped exploration, and independent parallel agents could substantially degrade performance.

**Confidence:** Low

**Why this confidence level**

The results are presented through a Medium synthesis rather than the primary study, and the retrieved excerpt does not provide inspectable tables, statistical uncertainty, or full methods.

**Evidence**

- S19 reports 260 configurations across six agentic benchmarks, with centralized MAS reaching a reported +80.8% on Finance-Agent, decentralized MAS +9.2% on BrowseComp-Plus, and performance ranging to -70.0% for an independent configuration on PlanCraft. [S19]
- S19 reports independent MAS as the weakest listed variant, with greater trace-level error amplification than centralized MAS but lower token overhead. [S19]

#### Finding 6

**Claim**

The evidence increasingly supports a strong single-agent baseline, particularly for homogeneous workflows whose role distinctions are prompt- or tool-based rather than model-based.

**Confidence:** High

**Why this confidence level**

S20 is a direct research paper and aligns with prior baseline recommendations, though its generalizability depends on benchmark and implementation details.

**Evidence**

- S20 reports experiments across seven benchmarks in which a single agent using multi-turn conversations and KV-cache reuse matched homogeneous multi-agent workflows while reducing inference cost; it introduces OneFlow for single-agent workflow execution. [S20]
- S15 and S1 previously recommended testing a strong single-agent baseline before adding agents, especially when responsibilities are not cleanly decomposable. [S15] [S1]

#### Finding 7

**Claim**

True model heterogeneity remains a distinct open research direction because single-agent simulation cannot reproduce workflows whose agents use different base models.

**Confidence:** High

**Why this confidence level**

The limitation and research direction are explicitly stated in S20 and supported by the accumulated open-problem inventory.

**Evidence**

- S20 states that single-LLM execution cannot capture truly heterogeneous workflows because different models cannot share the same KV cache, and identifies the value of model diversity relative to coordination cost as unresolved. [S20]
- Prior open questions explicitly include model heterogeneity, critic independence, and whether diversity improves safety or capability enough to justify coordination cost. [S9] [S4]

#### Finding 8

**Claim**

The design graph should include an explicit single-agent or single-LLM-simulation branch alongside genuinely distributed multi-agent branches.

**Confidence:** High

**Why this confidence level**

This is a direct synthesis of the new and prior evidence and materially improves the taxonomy.

**Evidence**

- S20 shows that homogeneous workflows may be executable by one agent through multi-turn role sequencing, while heterogeneous workflows remain genuinely multi-model. [S20]
- S15 and S1 position the single-agent system as the baseline and escalation point for multi-agent decomposition. [S15] [S1]

#### Finding 9

**Claim**

The empirical literature still does not establish a universal architecture ranking; cost, latency, routing accuracy, reliability, and task quality can favor different designs.

**Confidence:** High

**Why this confidence level**

The sources provide multiple conditional comparisons pointing in different directions, despite differences in tasks and methods.

**Evidence**

- S17 reports supervisor advantages in routing accuracy but swarm advantages in latency, calls, and tokens. [S17]
- S19 reports topology-specific gains and degradations across different benchmarks, while S14 found reflexive systems strongest on extraction accuracy and hierarchical systems preferable on cost-accuracy tradeoff. [S19] [S14]
- S20 reports that a single agent can match homogeneous workflows at lower cost, further challenging claims that separate agents are intrinsically superior. [S20]

### Conflicts Found

- S19 reports large topology-dependent gains, including +80.8% for centralized MAS on Finance-Agent, whereas S20 reports that a single agent can match homogeneous workflows across seven benchmarks at lower cost. These findings may reflect different task sets, workflow implementations, and baselines; they prevent treating multi-agent gains as intrinsic to having separate agents. [S19] [S20]
- S17 reports supervisor routing accuracy of 94% versus 91% for swarm, while S13 previously reported swarm slightly outperforming supervisor on a modified τ-bench comparison. The difference is plausibly due to workload, implementation, and metric differences, but no matched cross-study conclusion is possible. [S17] [S13]
- S18 characterizes swarm as suitable for independent workloads, while S19 describes decentralized debate as useful for exploration despite high redundancy and communication overhead. These are not necessarily contradictory: both imply that decentralized interaction may help when diversity is valuable, but they differ in whether the relevant execution is sequential handoff or peer debate. [S18] [S19]
- S19 presents precise benchmark-wide overhead and performance figures, but the retrieved material does not independently corroborate the underlying primary study; these figures are weaker evidence than S20's directly presented research claims. [S19] [S20]
- S21 is a journal article on title-abstract screening, but the retrieved content contains mainly metadata and navigation rather than methods or results. It cannot currently support comparative claims about single-agent versus multi-agent performance. [S21]

### Important Gaps

- Can the primary study behind S19's 260-configuration results be inspected to verify task definitions, matched compute budgets, statistical uncertainty, and complete topology results?
- When does a separately instantiated multi-agent workflow outperform an equivalent single agent with multi-turn role sequencing, especially when prompts, tools, and context are held constant?
- What measurable task features—parallel decomposability, dependency depth, state sharing, exploration need, or conflict frequency—predict the best topology?
- How should topology, execution shape, communication protocol, memory, model heterogeneity, and verification be benchmarked independently rather than confounded?
- Do heterogeneous models or genuinely independent critics produce benefits that exceed the cost of coordination and loss of shared KV-cache reuse?
- Can τ-bench-style evaluations measure topology effects using matched single-agent, supervisor, swarm, fan-out, debate, and reflexive systems with pass^k, policy adherence, cost, latency, and recovery metrics?
- What are the results and methodology of S21's title-abstract screening comparison?
- How can decentralized systems provide sufficient observability, auditability, state consistency, and loop termination without recreating a central coordinator?

**Analysis Duration:** 22.52s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The landscape and architectural dimensions are now sufficiently supported, but an important empirical gap remains: the strongest comparative claims are either secondary/practitioner reports or task-specific studies, and the new single-agent result changes the interpretation of what counts as a genuine multi-agent advantage. Inspecting the primary controlled benchmark behind S19 would materially improve the report's evidence base.

**Next Search**

> "Towards a Science of Scaling Agent Systems" Kim 2512.08296 centralized decentralized hybrid independent MAS Finance-Agent

---

# Iteration 6

## 1. Search

**Query**

> "Towards a Science of Scaling Agent Systems" Kim 2512.08296 centralized decentralized hybrid independent MAS Finance-Agent

**Why this query**

The landscape and architectural dimensions are now sufficiently supported, but an important empirical gap remains: the strongest comparative claims are either secondary/practitioner reports or task-specific studies, and the new single-agent result changes the interpretation of what counts as a genuine multi-agent advantage. Inspecting the primary controlled benchmark behind S19 would materially improve the report's evidence base.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S22 — GitHub - ybkim95/agent-scaling: Towards a Science of Scaling Agent Systems · GitHub**
  URL: https://github.com/ybkim95/agent-scaling
- **S23 — Towards a science of scaling agent systems**
  URL: https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work
- **S24 — Towards a Science of Scaling Agent Systems | alphaXiv**
  URL: https://www.alphaxiv.org/abs/2512.08296
- **S25 — Paper page - Towards a Science of Scaling Agent Systems**
  URL: https://huggingface.co/papers/2512.08296
- **S26 — Towards a Science of Scaling Agent Systems | Cool Papers - Immersive Paper Discovery**
  URL: https://papers.cool/arxiv/2512.08296

**Search Duration:** 4.26s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

New evidence strengthens the taxonomy around five canonical system-level configurations: single-agent, independent multi-agent, centralized, decentralized, and hybrid architectures.

**Confidence:** High

**Why this confidence level**

The categories are repeated across the research paper summaries and its accompanying reproducibility repository, and they align with the accumulated taxonomy.

**Evidence**

- The scaling-study repository provides runnable configurations for single-agent, centralized, decentralized, hybrid, and independent systems, explicitly treating them as distinct agent types. [S22]
- The associated study describes the same five configurations and defines their coordination mechanisms: unified sequential execution, noncommunicating parallel agents, hub-and-spoke orchestration, peer-to-peer coordination, and a combination of hierarchical and peer coordination. [S23] [S24] [S25] [S26]

#### Finding 2

**Claim**

The new scaling framework supports treating topology, orchestration policy, environment, and agent-level reasoning/tool/memory components as separate design dimensions rather than collapsing them into an agent-count taxonomy.

**Confidence:** High

**Why this confidence level**

The formal decomposition in S24 directly supports the multidimensional design-graph interpretation and is consistent with several prior sources.

**Evidence**

- S24 formalizes an agent system as a tuple containing agents, a shared environment, communication topology, and orchestration policy; it further characterizes each agent by its model, action space, memory, and decision function. [S24]
- The accumulated evidence similarly distinguishes topology from execution shape, communication, memory, specialization, and verification. [S1] [S4] [S9] [S18] [S19]

#### Finding 3

**Claim**

Architecture-task alignment is the strongest emerging empirical organizing principle: multi-agent coordination helps substantially on decomposable or parallelizable work but can harm sequential reasoning.

**Confidence:** Medium

**Why this confidence level**

The result is reported consistently across several secondary presentations of the same study, but the retrieved materials do not expose full experimental tables or independent replication.

**Evidence**

- The study reports a centralized improvement of 80.9% over a single-agent baseline on parallelizable financial reasoning, while all tested multi-agent variants degraded performance by 39–70% on sequential planning tasks. [S23] [S24] [S25] [S26]
- The study’s stated alignment principle attributes the difference to whether subtasks can be decomposed and executed concurrently without fragmenting a sequential reasoning process. [S23]

#### Finding 4

**Claim**

The evidence identifies a measurable coordination tax: tool-heavy tasks and high-performing single-agent baselines reduce or eliminate the expected benefit of adding agents.

**Confidence:** Medium

**Why this confidence level**

The qualitative principle is supported by multiple sources, but the precise threshold and coefficient come from one study presentation and require verification against the primary paper.

**Evidence**

- S24 reports disproportionate multi-agent overhead on tool-heavy tasks and diminishing or negative coordination returns once single-agent performance exceeds approximately 45%, with a reported negative saturation coefficient. [S24]
- S23 describes a tool-coordination tradeoff and warns that the heuristic that more agents are always better reaches a ceiling or degrades performance when coordination is mismatched to the task. [S23]
- S20 independently supports retaining a strong single-agent baseline because homogeneous multi-agent workflows can be matched by one agent at lower inference cost. [S20]

#### Finding 5

**Claim**

Topology affects error propagation and therefore belongs in the reliability and safety layer of the design graph, not only in the performance layer.

**Confidence:** Medium

**Why this confidence level**

The direction of the finding is coherent and directly reported, but the numerical amplification factors are not independently corroborated in the retrieved material.

**Evidence**

- S24 reports substantially greater error amplification for independent systems than for centralized coordination, attributing the difference to unchecked propagation versus centralized containment and verification. [S24]
- S23 explicitly frames architecture as a safety feature and measures the rate at which one agent’s mistake propagates to the final result. [S23]
- Prior evidence identifies correlated failures, judge bias, semantic drift, and weak verification as unresolved reliability risks. [S1] [S2] [S4] [S9]

#### Finding 6

**Claim**

The repository materially improves the field’s reproducibility infrastructure by exposing datasets, configurations, prompts, traces, tests, and experiment scripts for the canonical architectures.

**Confidence:** Medium

**Why this confidence level**

The repository contents directly support an available reproduction framework, but repository availability does not by itself establish that all reported results are independently reproduced.

**Evidence**

- S22 lists runnable configurations for six benchmarks, multiple agent types, experiment scripts, example traces, prompts, tests, and reproduction/data-availability documentation. [S22]

#### Finding 7

**Claim**

The design graph should represent adaptive or mixed strategies as an open frontier: select or combine topology and execution shape according to task properties instead of assuming a fixed architecture.

**Confidence:** Medium

**Why this confidence level**

The evidence supports adaptive architecture selection as a research direction, but the predictive result and its generalization require primary-source and cross-benchmark validation.

**Evidence**

- S24 presents measurable task- and coordination-dependent architecture preferences and reports that its predictive model identifies the best architecture for 87% of held-out configurations. [S24]
- The five-architecture comparison includes hybrid coordination, while prior evidence distinguishes topology from execution shape and reports different winners across workloads. [S23] [S24] [S18] [S19] [S20]

### Conflicts Found

- The new presentations of the same scaling study disagree on evaluation scope: S23 and S25 describe 180 configurations across four benchmarks and report cross-validated R^2=0.513, whereas S24 and S26 describe 260 configurations across six benchmarks and report different scope and predictive-model details. This likely reflects different paper versions, but the retrieved evidence does not resolve which results should be treated as final. [S23] [S24] [S25] [S26]
- The new study’s large numerical effects, including +80.9% or +80.8% financial gains, -70% sequential-task degradation, 17.2x versus 4.4x error amplification, and 87% held-out architecture selection, are presented consistently in some versions but remain dependent on one study and are not independently replicated in the retrieved sources. [S23] [S24] [S25] [S26]
- The new scaling results reinforce architecture-task dependence, but they do not resolve the earlier disagreement between studies favoring swarm, centralized, hierarchical, reflexive, or single-agent systems: the reported winner varies by benchmark, objective, implementation, and baseline. [S13] [S14] [S17] [S19] [S20] [S23] [S24]

### Important Gaps

- Which version of the scaling study is authoritative: the four-benchmark/180-configuration version or the six-benchmark/260-configuration version?
- Can the primary paper and released code verify the reported effect sizes, error-amplification factors, saturation threshold, confidence intervals, and matched compute budgets?
- Which measurable task features best predict the optimal architecture: parallel decomposability, dependency depth, tool count, state-sharing requirements, exploration need, or conflict frequency?
- Does adaptive topology selection outperform a fixed centralized, decentralized, hybrid, or single-agent strategy under preregistered cross-task evaluation?
- How much of the reported architecture effect is caused by topology itself rather than prompts, model choice, context management, retries, aggregation, or evaluator design?

**Analysis Duration:** 18.70s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The landscape can now be mapped responsibly, and the qualitative architecture-task alignment principle is substantially stronger. However, the newly retrieved sources contain a material version conflict about study size, benchmarks, and predictive-model results, while the headline numerical claims remain largely uncorroborated. Inspecting the primary paper version and its methods/results would materially improve the report’s empirical section.

**Next Search**

> arXiv 2512.08296 v3 primary paper methods results 260 configurations 180 configurations agent scaling

---

# Iteration 7

## 1. Search

**Query**

> arXiv 2512.08296 v3 primary paper methods results 260 configurations 180 configurations agent scaling

**Why this query**

The landscape can now be mapped responsibly, and the qualitative architecture-task alignment principle is substantially stronger. However, the newly retrieved sources contain a material version conflict about study size, benchmarks, and predictive-model results, while the headline numerical claims remain largely uncorroborated. Inspecting the primary paper version and its methods/results would materially improve the report’s empirical section.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S27 — [2512.08296] Towards a Science of Scaling Agent Systems**
  URL: https://arxiv.org/abs/2512.08296
- **S28 — [2512.08296] Towards a Science of Scaling Agent Systems**
  URL: https://arxiv.org/abs/2512.08296?hl=ko-KR
- **S29 — Towards a Science of Scaling Agent Systems**
  URL: https://arxiv.org/html/2512.08296v3

**Search Duration:** 2.77s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The primary arXiv HTML source strengthens the empirical basis for treating multi-agent architectures as task-conditional rather than universally superior.

**Confidence:** High

**Why this confidence level**

This is a direct abstract-level report from the primary paper rather than a secondary summary, though full methods and benchmark tables are not available in the retrieved excerpt.

**Evidence**

- S29 reports controlled evaluations across 260 configurations, six agentic benchmarks, five canonical architectures, and three LLM families, with tools, prompts, and compute standardized to isolate architectural effects. [S29]
- S29 reports relative performance changes ranging from +80.8% on decomposable financial reasoning to −70.0% on sequential planning. [S29]

#### Finding 2

**Claim**

The five-configuration framework used by the scaling study is a useful canonical backbone for the taxonomy: Single-Agent, Independent, Centralized, Decentralized, and Hybrid.

**Confidence:** High

**Why this confidence level**

The categories are stated in the primary source and align with the previously accumulated framework.

**Evidence**

- S29 explicitly evaluates one single-agent architecture and four multi-agent architectures: Independent, Centralized, Decentralized, and Hybrid. [S29]
- S24 and S22 previously described the same five-way configuration scheme and its reproducibility resources. [S22] [S24]

#### Finding 3

**Claim**

The study’s central explanatory principle is architecture-task alignment: coordination helps when work is decomposable and can hurt when reasoning is sequential or tightly state-dependent.

**Confidence:** High

**Why this confidence level**

The principle and proposed mechanism are directly articulated in the primary paper’s abstract and introduction.

**Evidence**

- S29 reports a large positive effect on decomposable financial reasoning and a large negative effect on sequential planning, and attributes success to alignment between coordination and task structure. [S29]
- S29 explains the contrast through the tradeoff between unified context integration in single agents and diversity with fragmented, lossy inter-agent communication in multi-agent systems. [S29]

#### Finding 4

**Claim**

Multi-agent systems impose an intrinsic coordination tax arising from information fragmentation, message compression, synchronization, and divergent agent states.

**Confidence:** High

**Why this confidence level**

The mechanism is directly explained by S29 and is consistent with multiple earlier sources.

**Evidence**

- S29 contrasts a single unified memory stream with multi-agent systems that must compress global context into inter-agent messages, producing lossy communication and synchronization overhead. [S29]
- S2, S3, S4, and S9 independently identify semantic loss, context drift, synchronization, token cost, and coordination complexity as major challenges. [S2] [S3] [S4] [S9]

#### Finding 5

**Claim**

The design graph should distinguish agentic tasks from static reasoning benchmarks when interpreting architecture comparisons.

**Confidence:** High

**Why this confidence level**

This distinction is explicit in the primary source and materially refines the evaluation layer of the taxonomy.

**Evidence**

- S29 defines agentic tasks as requiring sustained multi-step environmental interaction, iterative information gathering under partial observability, and adaptive refinement from feedback. [S29]
- S29 warns that multi-agent evaluations on static tasks may show monotonic scaling that does not transfer to interactive tasks where coordination overhead and error propagation dominate. [S29]

#### Finding 6

**Claim**

The scaling study provides a predictive but incomplete quantitative framework for architecture selection rather than a universal ranking.

**Confidence:** Medium

**Why this confidence level**

The reported predictive results come directly from the primary paper, but the retrieved content does not expose uncertainty intervals, feature definitions, or complete held-out evaluations.

**Evidence**

- S29 reports cross-validated R² of 0.373 across six benchmarks and 0.413 with a task-grounded capability metric, while identifying the best architecture for 87% of held-out configurations. [S29]
- S29 states that architecture preferences vary with task structure and that mismatched coordination degrades performance. [S29]

#### Finding 7

**Claim**

The primary source supports placing context integration versus diversity, rather than agent count alone, at the center of the landscape’s conceptual model.

**Confidence:** High

**Why this confidence level**

The conceptual mechanism is explicit in S29 and reinforced by independent prior findings.

**Evidence**

- S29 identifies context integration and diversity as the core tradeoff: single agents preserve global context, while multi-agent systems enable diverse exploration at the cost of fragmented information. [S29]
- S20 and S24 previously showed that homogeneous workflows may be matched by a single agent and that coordination returns diminish as baseline capability rises. [S20] [S24]

### Conflicts Found

- Earlier summaries of the scaling study reported conflicting scopes, including four benchmarks and 180 configurations versus six benchmarks and 260 configurations. S29 explicitly states the six-benchmark, 260-configuration scope, resolving the likely version discrepancy in favor of the current v3 paper, although earlier-version results may still differ. [S23] [S24] [S25] [S26] [S29]
- S29’s primary-source results support large conditional architecture effects, while S20 reports that a single agent can match homogeneous multi-agent workflows at lower cost. These are not directly contradictory because the studies use different tasks and workflow implementations; together they rule out intrinsic superiority from agent multiplicity alone. [S20] [S29]
- The primary source emphasizes agentic benchmark validity and warns about static-task evaluations, whereas several earlier comparative claims come from narrower or practitioner benchmarks. Their numerical results should not be pooled without matching task definitions, prompts, tools, and compute. [S7] [S13] [S14] [S17] [S29]

### Important Gaps

- What are the complete methods, benchmark-by-benchmark results, confidence intervals, and compute-accounting details behind S29’s reported effect sizes?
- Which task features are most predictive of the optimal architecture: decomposability, dependency depth, tool count, state sharing, exploration need, or conflict frequency?
- How much of the reported architecture effect remains after independently matching prompts, routing policies, retries, memory, model heterogeneity, and verification procedures?
- Do the reported architecture preferences replicate across domains such as coding, browsing, research, and high-stakes decision-making?
- Can adaptive architecture selection outperform fixed single-agent, centralized, decentralized, and hybrid strategies under preregistered cross-task tests?
- How should pass^k reliability, policy adherence, error propagation, recovery, latency, cost, and auditability be combined in a common evaluation protocol?
- Do heterogeneous models or genuinely independent critics provide benefits that exceed their communication and coordination costs?
- How can decentralized systems preserve observability, state consistency, termination, and governance without recreating a central coordinator?

**Analysis Duration:** 16.55s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The new primary source materially resolves the most important prior gap: it provides a direct, controlled, six-benchmark comparison and a principled account of task-dependent scaling. The research landscape can now be mapped responsibly, provided the final report labels detailed numerical claims as study-specific and notes that replication and full methodological inspection remain open issues. Further searching could improve completeness but is not necessary to answer the original taxonomy-and-open-problems question.

**Stop Reason:** sufficient_evidence

---

# Final Research Decision

**Research Stopped Because**

The analyzer determined that the important parts of the question could be answered responsibly.

**Stop Reason:** sufficient_evidence

**Searches Performed:** 7

**Unique Sources:** 29

**Remaining Uncertainty**

- Full benchmark tables, confidence intervals, compute accounting, and per-task results for the primary scaling study are not present in the accumulated excerpts.
- The field still lacks a common, controlled protocol comparing single-agent, centralized, decentralized, independent, hybrid, workflow, debate, and reflexive systems under matched prompts, tools, models, and budgets.
- The most predictive task features remain unresolved: decomposability, dependency depth, tool count, state-sharing requirements, exploration need, conflict frequency, and trajectory length.
- It remains unclear when separate agent instances outperform a single agent executing the same homogeneous workflow through multi-turn role sequencing.
- The benefits of heterogeneous models and genuinely independent critics versus their communication, cost, and context-sharing disadvantages are not established.
- Common evaluation should combine task quality, pass^k reliability, policy adherence, error propagation, recovery, latency, token cost, auditability, and human-oversight burden.
- Decentralized systems need stronger solutions for observability, state consistency, authorization, loop termination, rollback, privacy, and malicious or faulty agents.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 7 | 21.22s |
| OpenAI Analysis | 7 | 128.21s |
| Report Generation | 1 | 36.32s |
| Total Run | — | 185.75s |
