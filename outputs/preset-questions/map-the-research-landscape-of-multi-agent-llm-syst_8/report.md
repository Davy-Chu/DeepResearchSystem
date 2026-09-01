# Research Report

## Research Question

Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are.

## Summary

The accumulated evidence supports a multidimensional landscape rather than one universally accepted taxonomy. The most useful backbone separates: (1) the number and specialization of agents, (2) control topology, (3) execution shape, (4) communication and memory, and (5) verification or agreement mechanisms. A practical design progression is to establish a strong single-agent baseline, then add decomposition, parallelism, supervision, peer interaction, or verification only when the task structure justifies the coordination cost. The strongest primary empirical evidence indicates that architecture-task alignment is decisive: coordination can help substantially on decomposable work but harm tightly sequential tasks. Important unresolved issues concern semantic coordination, cost, reliability, evaluation comparability, model heterogeneity, adaptive topology selection, and production governance.

## Findings

### Finding 1

**Claim**

The research landscape is best modeled as composable architectural dimensions rather than a single canonical taxonomy.

**Confidence:** High

**Why this confidence level**

The multidimensional structure is directly supported by the primary formalization and converges with multiple taxonomy and architecture sources.

**Evidence**

- The primary scaling study formalizes an agent system using agents, a shared environment, communication topology, and orchestration policy, while characterizing each agent by its model, actions/tools, memory, and decision function. [S24]
- Other sources separately identify orchestration, communication, control flow, specialization, memory, and agreement protocols as design dimensions. [S4] [S9] [S18]

### Finding 2

**Claim**

A useful visual taxonomy is: single-agent baseline; independent parallel agents; centralized supervisor-worker; decentralized swarm or peer-to-peer systems; explicit graph/workflow systems; and hybrid systems combining hierarchical control with lateral communication. These can be augmented by planning, debate, verifier-critic, memory, and evaluation layers.

**Confidence:** High

**Why this confidence level**

The major families and their composability recur across primary, survey, and implementation-oriented sources, although terminology is not standardized.

**Evidence**

- The primary scaling study evaluates Single-Agent, Independent, Centralized, Decentralized, and Hybrid configurations. [S29]
- Architecture guides distinguish hierarchical supervision, explicit workflows, swarms, and parallel fan-out, while broader taxonomies add plan-and-execute, debate, and verifier-critic patterns. [S1] [S8] [S18]
- The deep-research implementation demonstrates composition of planning, parallel specialists, auditing, synthesis, writing, and refinement within a graph. [S3]

### Finding 3

**Claim**

Visual taxonomy/design graph:

USER/TASK
   |
   v
[Task diagnosis: sequential? decomposable? exploratory? state-sharing? high-stakes?]
   |
   +--> [Single agent: ReAct / tool use]
   |          |
   |          +--> [Reflexion / self-critique]
   |          +--> [Single-LLM simulation of homogeneous workflow]
   |
   +--> [Decomposition needed]
              |
              +--> [Sequential pipeline or plan-and-execute]
              |          +--> planner -> executor -> optional re-plan
              |
              +--> [Parallel fan-out / independent specialists]
              |          +--> specialist A --+
              |          +--> specialist B ----+--> merge/synthesis
              |
              +--> [Centralized supervisor-worker]
              |          +--> supervisor -> workers -> validation -> supervisor
              |
              +--> [Decentralized swarm / peer handoff]
              |          +--> agent -> agent -> agent
              |
              +--> [Explicit graph/workflow]
              |          +--> typed nodes, branches, joins, retries, termination
              |
              +--> [Hybrid]
                         +--> supervisor planning + parallel execution + peer sharing

Cross-cutting layers:
[communication schemas] [shared/context memory] [tools/environment]
[debate or verifier-critic] [citation/quality audit] [observability/governance]

Open-problem hotspots: task diagnosis; lossy handoffs; context synchronization; error propagation; cost/latency; adaptive topology; heterogeneous models; evaluation and governance.

**Confidence:** High

**Why this confidence level**

This is a synthesis of directly described patterns. It is a research map, not a claim that the field has formally adopted this exact graph.

**Evidence**

- The graph combines the five system-level configurations from the primary scaling study with execution and verification patterns described in the architecture sources. [S29] [S8] [S18]
- The graph's composition of planning, parallel specialists, auditing, synthesis, and refinement is illustrated by the LangGraph research workflow. [S3]
- The single-LLM simulation branch is supported by evidence that homogeneous multi-agent workflows can be executed by one agent through multi-turn role sequencing. [S20]

### Finding 4

**Claim**

Single-agent systems are an essential baseline and may be preferable when the task is sequential, context-integrated, or not cleanly decomposable.

**Confidence:** High

**Why this confidence level**

The baseline recommendation is supported by both controlled research and practitioner benchmarking, though exact escalation thresholds remain unresolved.

**Evidence**

- The primary scaling study explains that single agents preserve a unified memory stream, whereas multi-agent systems fragment information through inter-agent messages. [S29]
- LangChain's single-agent study reports degradation as domains, instructions, tools, and trajectory length increase, motivating decomposition only when scope becomes excessive. [S15]
- OneFlow experiments report that a single agent can match homogeneous multi-agent workflows with lower inference cost through multi-turn execution and KV-cache reuse. [S20]

### Finding 5

**Claim**

Centralized supervisor-worker systems offer modular delegation, routing visibility, validation, ordering, and conflict handling, but introduce routing overhead, bottlenecks, and a central failure point.

**Confidence:** High

**Why this confidence level**

The qualitative tradeoff is consistently documented; the numerical comparison is implementation-specific.

**Evidence**

- Architecture sources describe the supervisor as a coordinator that delegates to specialists, validates outputs, enforces ordering, and can prevent loops. [S8] [S18]
- The supervisor's central position is also identified as a routing bottleneck and single point of failure as systems grow. [S8] [S10]
- A customer-service comparison reports higher supervisor latency, calls, and token use than swarm, but higher routing accuracy in that implementation. [S17]

### Finding 6

**Claim**

Decentralized swarm systems should be distinguished from parallel fan-out. Swarms use distributed, generally sequential handoffs, whereas fan-out runs multiple specialists concurrently under some coordinating mechanism.

**Confidence:** High

**Why this confidence level**

The distinction is explicit and resolves a common taxonomy ambiguity.

**Evidence**

- The architecture guide explicitly states that swarm has one active agent at a time and contrasts it with concurrent fan-out parallelism. [S18]
- Other sources separately classify decentralized/swarm systems and parallel specialist composition. [S1] [S3] [S8]

### Finding 7

**Claim**

Explicit graph/workflow architectures provide stronger control-flow boundaries, auditability, synchronization, and termination guarantees, but shift responsibility for branching, recovery, concurrency, and refinement to system designers.

**Confidence:** High

**Why this confidence level**

The architectural distinction is directly described and illustrated by an implemented workflow.

**Evidence**

- Explicit workflows define permitted nodes, edges, branches, convergence points, and termination, and cannot invent unimplemented control flow. [S8]
- The deep-research graph uses bounded iterations, citation auditing before writing, gap analysis, synthesis, and refinement as structural controls. [S3]

### Finding 8

**Claim**

Debate, verifier-critic, and other adversarial architectures form a distinct research sublandscape focused on quality, robustness, safety, and agreement rather than only task parallelization.

**Confidence:** High

**Why this confidence level**

The subfield is supported by a systematic survey and consistent architectural descriptions, although comparative evidence for particular debate designs remains limited.

**Evidence**

- The debate survey reviews 141 primary studies and organizes debate systems by participants, interaction mechanisms, and agreement protocols. [S9]
- The broader taxonomy describes debate and verifier-critic systems as quality and safety mechanisms involving critique, judging, scoring, and revision. [S1]
- Reported risks include premature convergence, judge bias, collusion, over-correction, correlated failures, and additional latency. [S1] [S9]

### Finding 9

**Claim**

The strongest emerging empirical principle is architecture-task alignment: multi-agent coordination can improve decomposable or parallelizable work but can degrade tightly sequential reasoning.

**Confidence:** High

**Why this confidence level**

The principle is directly reported by the primary study and supported by independent architectural reasoning. The exact effect sizes remain study-specific.

**Evidence**

- The primary scaling study reports relative performance changes from +80.8% on decomposable financial reasoning to −70.0% on sequential planning across its controlled evaluation. [S29]
- The study attributes the contrast to the balance between diverse parallel exploration and the information fragmentation and coordination tax of multi-agent communication. [S29]
- Architecture guides independently recommend matching supervisors, swarms, or hybrids to dependency structure and execution requirements. [S18]

### Finding 10

**Claim**

Multi-agent systems incur a coordination tax arising from message passing, context compression, synchronization, duplicated reasoning, and divergent agent states; tool-heavy tasks and strong single-agent baselines can reduce the benefit of adding agents.

**Confidence:** Medium

**Why this confidence level**

The qualitative mechanism is well supported, but precise thresholds and coefficients come from study-specific results and require broader replication.

**Evidence**

- The primary study describes lossy inter-agent communication, synchronization overhead, and fragmented global context as intrinsic costs of multi-agent systems. [S29]
- The study reports disproportionate overhead on tool-heavy tasks and diminishing or negative returns as single-agent capability rises. [S23] [S24]
- OneFlow reports lower-cost single-agent execution for homogeneous workflows, reinforcing that separate agent instances are not intrinsically beneficial. [S20]

### Finding 11

**Claim**

Reliability should be treated as a first-class architectural objective. τ-bench-style evaluations show that simple tool-calling and ReAct agents struggle with dynamic user interaction, policy adherence, state changes, and repeated execution.

**Confidence:** High

**Why this confidence level**

The benchmark design and reliability motivation are directly documented, although these results do not isolate the effect of multi-agent topology.

**Evidence**

- τ-bench evaluates realistic databases and APIs, domain-specific policies, simulated users, final database state, and pass^k repeated-trial reliability. [S16]
- The benchmark source reports that all 12 evaluated models had difficulty and that the best displayed GPT-4o result achieved under 50% average success across the two domains. [S16]
- A public airline evaluation reports verified accuracies between 36% and 56% for the displayed configurations, illustrating the difficulty of reliable tool-agent interaction. [S12]

### Finding 12

**Claim**

No architecture is established as universally superior. Different objectives and workloads favor different designs: swarm may reduce latency, supervisors may improve routing visibility, reflexive systems may improve accuracy, hierarchical systems may improve cost-accuracy tradeoffs, and single-agent execution may match homogeneous workflows more cheaply.

**Confidence:** High

**Why this confidence level**

The conditional outcomes are mutually consistent in ruling out a universal ranking, even though the underlying studies use different tasks and methods.

**Evidence**

- A customer-service comparison reports swarm advantages in latency and tokens but supervisor advantages in routing accuracy. [S17]
- A financial-document study reports the highest extraction F1 for reflexive systems but a more favorable cost-accuracy position for hierarchical systems. [S14]
- The scaling study reports topology-dependent gains and losses across benchmarks, while OneFlow reports comparable performance from single-agent execution of homogeneous workflows. [S29] [S20]

### Finding 13

**Claim**

The current evidence supports adaptive or mixed architecture selection as a major research direction: select topology, execution shape, verification, and model allocation according to measurable task properties rather than fixed agent count.

**Confidence:** Medium

**Why this confidence level**

The direction is supported, but the predictive result and generalization of adaptive selection require replication and full methodological inspection.

**Evidence**

- The primary scaling study reports that its predictive framework identifies the best architecture for 87% of held-out configurations, while still showing task-dependent preferences. [S29]
- Hybrid architectures combine hierarchical oversight and peer communication, and architecture guides recommend supervisor planning with parallel execution when both forms of coordination are needed. [S18] [S24]

### Finding 14

**Claim**

The principal open problems are semantic coordination and state management, reliability and error recovery, cost and scalability, evaluation standardization, model heterogeneity, adaptive topology, and governance.

**Confidence:** High

**Why this confidence level**

These gaps recur across primary research, surveys, benchmark sources, and implementation reports.

**Evidence**

- Sources identify contextual drift, semantic mismatch, protocol-related semantic loss, token consumption, variable model behavior, partial failures, and production governance as unresolved challenges. [S2] [S3] [S4] [S5]
- The debate survey calls for executable specifications, cost-aware benchmarking, and automated tuning because implicit design choices impede comparison. [S9]
- The primary scaling paper highlights information fragmentation, error propagation, architecture-task mismatch, and the lack of principled prediction as continuing research gaps. [S29]
- OneFlow identifies genuinely heterogeneous multi-agent workflows as an open direction because single-agent simulation cannot reproduce different base models. [S20]

## Conflicts and Uncertainty

- The scaling study appears in different retrieved versions with different scopes: earlier summaries describe 180 configurations across four benchmarks, while the current v3 primary HTML source describes 260 configurations across six benchmarks. The v3 scope is used here, but version-specific numerical differences may remain. [S23] [S25] [S29]
- The primary scaling study reports large conditional effects, including +80.8% and −70.0%, but these do not establish universal gains. Other studies report single-agent equivalence for homogeneous workflows, swarm advantages on some tasks, and reflexive or hierarchical advantages under different objectives. [S14] [S17] [S20] [S29]
- Some precise claims about cost, routing accuracy, architecture prevalence, bottlenecks, and benchmark performance come from practitioner or secondary sources with limited methodological detail. They should not be pooled as field-wide estimates. [S1] [S7] [S10] [S13] [S17] [S19]
- τ-bench results from different pages are not directly comparable: the retrieved sources use different domains, scaffolds, model versions, aggregation methods, and verification status. [S11] [S12] [S16]
- The taxonomy is a synthesis. Although the five system-level configurations are directly used in the primary scaling study, labels such as swarm, decentralized, workflow, graph, debate, and verifier-critic are used with varying scope across sources. [S1] [S4] [S8] [S9] [S18] [S29]
- The reported financial-document results favoring reflexive accuracy and hierarchical cost-accuracy performance come from one source and are not independently corroborated in the retrieved material. [S14]

## Remaining Gaps

- Full benchmark tables, confidence intervals, compute accounting, and per-task results for the primary scaling study are not present in the accumulated excerpts.
- The field still lacks a common, controlled protocol comparing single-agent, centralized, decentralized, independent, hybrid, workflow, debate, and reflexive systems under matched prompts, tools, models, and budgets.
- The most predictive task features remain unresolved: decomposability, dependency depth, tool count, state-sharing requirements, exploration need, conflict frequency, and trajectory length.
- It remains unclear when separate agent instances outperform a single agent executing the same homogeneous workflow through multi-turn role sequencing.
- The benefits of heterogeneous models and genuinely independent critics versus their communication, cost, and context-sharing disadvantages are not established.
- Common evaluation should combine task quality, pass^k reliability, policy adherence, error propagation, recovery, latency, token cost, auditability, and human-oversight burden.
- Decentralized systems need stronger solutions for observability, state consistency, authorization, loop termination, rollback, privacy, and malicious or faulty agents.

## Conclusion

The research landscape is converging on a conditional design principle rather than a race toward larger agent teams. Multi-agent LLM systems are best understood as combinations of topology, execution shape, communication and memory, specialization, and verification. Start with a strong single-agent baseline; use centralized or explicit workflow designs when decomposition, ordering, validation, and auditability matter; use parallel specialists when subtasks are genuinely independent; use decentralized handoffs or peer debate when local autonomy or diverse perspectives are valuable; and use hybrid or reflexive mechanisms when their additional cost is justified by the reliability or quality objective. The central open research challenge is to make this selection principled and adaptive, using reproducible task features and common reliability- and cost-aware evaluations rather than agent count or anecdotal architecture preference.

## Sources

- [S1] Agent Architecture Patterns: 2026 Taxonomy Guide — https://www.digitalapplied.com/blog/agent-architecture-patterns-taxonomy-2026
- [S2] LLM Agent Orchestration Patterns: Architectural Frameworks for Managing Complex Multi-Agent Systems — https://www.c-sharpcorner.com/article/llm-agent-orchestration-patterns-architectural-frameworks-for-managing-complex
- [S3] Medium — https://medium.com/data-science-collective/building-a-multi-agent-deep-research-agent-with-langgraph-203547b5fb12
- [S4] LLM-Enabled Multi-Agent Systems: Empirical Evaluation and Insights into Emerging Design Patterns & Paradigms — https://arxiv.org/html/2601.03328v1
- [S5] From RAG to Multi-Agent Systems: A Survey of Modern Approaches in LLM Development — https://www.preprints.org/manuscript/202502.0406
- [S6] Benchmarking Multi-Agent Architectures — https://www.langchain.com/blog/benchmarking-multi-agent-architectures
- [S7] Single Agent vs Multi-Agent Systems 2026: When Swarms Help — https://swarmsignal.net/single-vs-multi-agent-comparison-2026
- [S8] Medium — https://medium.com/mitb-for-all/a-field-guide-to-multi-agent-architectures-f6f8c689c406
- [S9] Multi-Agent Debate Strategies: Survey, Taxonomy, and Challenges — https://arxiv.org/html/2607.26212v1
- [S10] Architectures for Multi-Agent Systems — https://galileo.ai/blog/architectures-for-multi-agent-systems
- [S11] Tau-bench Leaderboard — https://llm-stats.com/benchmarks/tau-bench
- [S12] HAL: TAU-bench Airline — https://hal.cs.princeton.edu/taubench_airline
- [S13] Evaluating Multi-Agent Architectures: A Performance Benchmark - Blockchain.News — https://blockchain.news/news/evaluating-multi-agent-architectures-performance-benchmark
- [S14] Benchmarking Multi-Agent LLM Architectures for Financial Document Processing: A Comparative Study of Orchestration Patterns, Cost-Accuracy Tradeoffs and Production Scaling Strategies — https://arxiv.org/html/2603.22651v1
- [S15] Benchmarking Single Agent Performance - LangChain — https://www.langchain.com/blog/react-agent-benchmarking
- [S16] 𝜏-Bench: Benchmarking AI agents for the real-world | Sierra — https://sierra.ai/blog/benchmarking-ai-agents
- [S17] How to Orchestrate Multi-Agent Systems in LangGraph (Supervisor vs Swarm Patterns) | Focused — https://focused.io/lab/multi-agent-orchestration-in-langgraph-supervisor-vs-swarm-tradeoffs-and-architecture
- [S18] Swarm vs. Supervisor: Multi-Agent Architecture Guide — https://www.augmentcode.com/guides/swarm-vs-supervisor
- [S19] Medium — https://medium.com/@mjgmario/single-agent-vs-multi-agent-systems-when-coordination-helps-hurts-and-pays-off-57735ee7916d
- [S20] Rethinking the Value of Multi-Agent Workflow: A Strong Single Agent Baseline — https://arxiv.org/html/2601.12307v1
- [S21] Comparing Single-Agent and Multi-Agent Strategies in ... — https://www.mdpi.com/2079-9292/15/8/1661
- [S22] GitHub - ybkim95/agent-scaling: Towards a Science of Scaling Agent Systems · GitHub — https://github.com/ybkim95/agent-scaling
- [S23] Towards a science of scaling agent systems — https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work
- [S24] Towards a Science of Scaling Agent Systems | alphaXiv — https://www.alphaxiv.org/abs/2512.08296
- [S25] Paper page - Towards a Science of Scaling Agent Systems — https://huggingface.co/papers/2512.08296
- [S26] Towards a Science of Scaling Agent Systems | Cool Papers - Immersive Paper Discovery — https://papers.cool/arxiv/2512.08296
- [S27] [2512.08296] Towards a Science of Scaling Agent Systems — https://arxiv.org/abs/2512.08296
- [S28] [2512.08296] Towards a Science of Scaling Agent Systems — https://arxiv.org/abs/2512.08296?hl=ko-KR
- [S29] Towards a Science of Scaling Agent Systems — https://arxiv.org/html/2512.08296v3
