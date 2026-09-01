# Research Report

## Research Question

Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are.

## Summary

The accumulated evidence supports a multidimensional landscape rather than a single canonical list of multi-agent patterns. The most useful axes are: (1) coordination topology—centralized, hierarchical, decentralized, or graph-based; (2) execution structure—sequential, parallel, handoff-based, event-driven, or hybrid; (3) interaction objective—cooperation, critique/debate, verification, or competition; (4) communication and state—direct messages, shared memory/blackboard, reports, relays, or typed contracts; and (5) control and assurance—planning, retries, termination limits, observability, policy enforcement, and human checkpoints. The evidence consistently recommends starting with a strong deterministic or single-agent baseline and adding coordination only when specialization, context partitioning, parallelism, or verification justifies its cost. Quantitative claims about architecture superiority, production prevalence, and cost remain insufficiently validated.

## Findings

### Finding 1

**Claim**

A useful visual taxonomy places single-agent and deterministic systems at the baseline, then branches by coordination topology, execution semantics, and interaction objective rather than treating patterns as mutually exclusive.

**Confidence:** High

**Why this confidence level**

Multiple sources converge on the multidimensional structure, even though they disagree about taxonomy granularity and canonical pattern counts.

**Evidence**

- Sources distinguish centralized, decentralized, and hierarchical topologies; dynamic/adaptive control; cooperation, competition, role structures, and multiple communication paradigms. [S8] [S10]
- Recurring engineering patterns include orchestrator-worker, hierarchical delegation, pipeline, fan-out/fan-in, swarm, mesh, debate, verifier-critic, and hybrid compositions. [S1] [S5] [S11] [S14] [S18] [S30]
- Dynamic graph routing and handoffs are implementation mechanisms that can realize several topologies rather than a standalone architecture family. [S29]

### Finding 2

**Claim**

The central design graph is: baseline workflow or single agent -> coordination need -> pipeline, fan-out, supervisor, hierarchy, decentralized handoff/mesh, or critique/verification -> hybrid systems with shared state, recovery, and governance.

**Confidence:** High

**Why this confidence level**

The relationship among the major branches is consistently described across the accumulated sources, although the performance boundaries between them are not established.

**Evidence**

- Single-agent ReAct or explicit graphs are presented as appropriate baselines for simple, sequential, well-scoped tasks; multi-agent systems are motivated by tool/context scaling, modularity, specialization, and parallelization. [S23] [S25] [S27] [S29]
- Pipelines fit strict dependencies; fan-out fits independent subtasks; supervisors fit dynamic routing, ordering, and synthesis; hierarchies extend centralized delegation; decentralized designs support peer interaction or exploration; debate and verification repeat or critique work for quality assurance. [S1] [S11] [S12] [S14] [S17] [S18] [S30]
- Production systems are commonly described as hybrids combining patterns such as supervisor planning with parallel execution or verification. [S5] [S12] [S18]

### Finding 3

**Claim**

Sequential pipelines are low-complexity and predictable, but their principal risk is cascading failure when an intermediate stage produces an incorrect result or cannot adapt to changed conditions.

**Confidence:** High

**Why this confidence level**

The qualitative mechanism and use-case fit are repeated across several sources.

**Evidence**

- Pipeline systems pass outputs through ordered stages and are recommended for deterministic dependencies; the trade-off is limited flexibility and cascade failure across downstream stages. [S11] [S14] [S17] [S18]

### Finding 4

**Claim**

Fan-out/fan-in is a distinct centralized-parallel pattern: a coordinator dispatches independent branches concurrently and an aggregator merges them; it should not be conflated with decentralized swarm execution.

**Confidence:** Medium

**Why this confidence level**

The distinction is explicit, but the sources are primarily engineering guides and use different implementations of the term swarm.

**Evidence**

- Fan-out is defined as parallel scatter-gather over independent subtasks, with wall-clock latency determined largely by the slowest branch and partial branch failure as a key concern. [S14]
- Swarm is contrasted with fan-out: the described swarm implementation uses distributed routing and one active agent at a time, whereas fan-out uses a central coordinator and concurrent workers. [S12] [S25]

### Finding 5

**Claim**

Supervisor or orchestrator-worker systems are the principal centralized multi-agent pattern: a coordinator decomposes a goal, routes subtasks to specialized workers, tracks state, and synthesizes results.

**Confidence:** High

**Why this confidence level**

The architecture and qualitative trade-offs are directly and repeatedly supported.

**Evidence**

- Supervisor-worker and orchestrator-worker are described as central routing architectures with specialized workers and result aggregation. [S1] [S5] [S11] [S18] [S30]
- The pattern offers centralized traceability and explicit ordering, but creates potential coordinator bottlenecks, single points of failure, and context-aggregation limits. [S5] [S11] [S18] [S22] [S30] [S31]

### Finding 6

**Claim**

Hierarchical delegation extends supervisor coordination into a tree: top-level supervisors assign subgoals to intermediate supervisors, which manage workers. It is useful when decomposition boundaries and authority levels are clear, but adds coordination layers and latency.

**Confidence:** Medium

**Why this confidence level**

The structural distinction is consistent, but the boundary between a supervisor with nested workers and a separate hierarchical category is not standardized.

**Evidence**

- Hierarchical systems are described as multi-level supervisor-worker trees in which each supervisor manages a scoped team and reports upward. [S6] [S7] [S18] [S30]
- Sources associate hierarchy with complex workflows and scoped budgets, while noting additional coordination overhead and the need for clear decomposition boundaries. [S1] [S6] [S7] [S9]

### Finding 7

**Claim**

Decentralized systems include peer-to-peer mesh, shared-blackboard, event-driven, and handoff-based variants, but the label 'swarm' is underspecified and may refer either to concurrent shared-state exploration or sequential handoffs.

**Confidence:** High

**Why this confidence level**

The conflicting definitions are directly documented and establish a terminology problem.

**Evidence**

- Mesh is described as explicit persistent peer connections, while swarm is described through local decisions, shared state, blackboards, or handoffs. [S30] [S31]
- Some sources define swarm as sequential decentralized handoffs with one active agent, while others describe shared-state or potentially concurrent exploration. [S12] [S18] [S23] [S25] [S30] [S31]

### Finding 8

**Claim**

Debate, verifier-critic, and critic-refiner systems form a quality-oriented interaction family distinct from task decomposition and throughput-oriented collaboration.

**Confidence:** High

**Why this confidence level**

The functional distinction is clear across several sources, although comparative effectiveness is not established.

**Evidence**

- Debate sends the same problem to multiple agents and uses a judge or synthesizer; verifier-critic generates, critiques against a rubric, and revises. [S1] [S11] [S14]
- Search and production taxonomies identify verifiers, verifier-guided search, critic-refiners, and guardrails as separate workflow components. [S4] [S5]

### Finding 9

**Claim**

Architecture choice should be conditioned primarily on task structure: independent subtasks favor fan-out or suitable decentralized execution; strict dependencies favor pipelines; dynamic routing and conflict resolution favor supervisors; repeated quality concerns favor verification or debate; and simple sequential work may favor a single-agent graph or deterministic workflow.

**Confidence:** High

**Why this confidence level**

This conditional design rule is consistent across the full accumulated state.

**Evidence**

- Sources repeatedly associate pipeline with strict dependencies, fan-out with independent subtasks, and supervisor with dynamic routing, ordering, and synthesis. [S11] [S12] [S17] [S18]
- Single-agent graphs and deterministic workflows are recommended when simplicity, predictability, and context coherence matter; multi-agent designs are justified by specialization, modularity, context partitioning, or growing complexity. [S22] [S23] [S25] [S27] [S29]

### Finding 10

**Claim**

Reliable systems require an assurance layer spanning typed contracts, bounded budgets, termination rules, timeouts, retries or fallbacks, observability, provenance, access control, and policy enforcement.

**Confidence:** High

**Why this confidence level**

The mechanisms are directly supported by academic and practitioner sources, even though controlled evidence of their relative effectiveness is limited.

**Evidence**

- Production guidance recommends strict JSON-schema interfaces, worker health checks, timeouts, deterministic fallbacks, bounded fan-out, and token ceilings. [S5]
- The architecture paper identifies typed tools, auditable control, observability, reproducibility, governance, verifiability, interoperability, and safe autonomy as production concerns. [S3]
- Component-oriented sources identify runtime state, retries, handoffs, memory, typed tools, tracing, evaluation, and guardrails as core layers. [S2] [S8]

### Finding 11

**Claim**

The principal research problem is not merely individual-agent capability but system-level coordination: inconsistent shared state, duplicated work, contradictions, routing errors, context loss, nontermination, and error propagation.

**Confidence:** High

**Why this confidence level**

The same failure classes recur across the academic-oriented survey, benchmark reports, and engineering guidance.

**Evidence**

- The orchestration survey identifies task allocation, communication, state management, sequencing, and error recovery as the core coordination mechanisms and notes contradictions, duplicated effort, and inconsistent state as system-level failures. [S8]
- Sources describe supervisor translation overhead, handoff context drift, routing loops, context-window bottlenecks, and swarm convergence and observability problems. [S5] [S12] [S22] [S23] [S30]

### Finding 12

**Claim**

Evaluation should measure more than final answer accuracy: outcome correctness, repeated-trial reliability, latency, token or monetary cost, safety and policy compliance, robustness to stateful interaction, and coordination-specific failures are all needed.

**Confidence:** High

**Why this confidence level**

The evaluation requirements are directly supported, although no complete standardized protocol is established in the retrieved material.

**Evidence**

- Agent benchmarks are described as outcome-based, including database-state correctness and passing tests, and as requiring repeated-trial metrics such as pass^k rather than only pass@k. [S19] [S21]
- The sources emphasize score-latency-cost trade-offs, policy-constrained tool use, partial observability, and the limitations of benchmark scores as production-readiness evidence. [S19] [S21]
- The proposed orchestration evaluation framework and related sources identify coordination quality, recovery, scalability, security, and reproducibility as additional dimensions. [S8] [S3]

### Finding 13

**Claim**

The strongest available architecture-level benchmark evidence is narrow and implementation-sensitive: a LangChain modified τ-bench experiment compared single-agent, swarm, and supervisor systems using one model and distractor domains, reporting a sharp single-agent decline with added irrelevant context and a slight swarm advantage over supervisor.

**Confidence:** Low

**Why this confidence level**

The experiment is described in a primary technical blog, but the retrieved material omits numerical scores, variance, complete cost results, and ablations separating topology from prompt, package, and context-management effects.

**Evidence**

- The benchmark used gpt-4o, 100 retail test examples, and up to six unrelated distractor environments; it compared a single tool-calling agent, sequential handoff swarm, and supervisor architecture. [S25] [S26]
- The source reports that single-agent performance dropped with multiple distractor domains and that swarm slightly outperformed supervisor, attributing the latter to supervisor translation and context-passing overhead. [S25] [S26]

### Finding 14

**Claim**

A financial-document benchmark may provide broader evidence about cost-accuracy trade-offs, but its reported numerical findings remain provisional in the accumulated state.

**Confidence:** Low

**Why this confidence level**

The paper's identity is confirmed, but the quantitative claims remain single-source and methodologically incomplete in the retrieved state.

**Evidence**

- The identified arXiv preprint reports comparisons of sequential pipeline, parallel fan-out/merge, hierarchical supervisor-worker, and reflexive self-correction across models and SEC filings using accuracy, F1, latency, cost, and token-efficiency metrics. [S32] [S34]
- The reported results favor reflexive systems on F1 and hierarchical systems on cost-accuracy trade-off, with hybrid routing, caching, and retries allegedly recovering much of the quality gain near baseline cost. [S32]
- The available arXiv and secondary excerpts do not provide the full methods, results, statistical treatment, code, or reproducibility evidence. [S33] [S34] [S35] [S36] [S37]

## Conflicts and Uncertainty

- Taxonomy counts and category boundaries differ. Sources propose eight canonical patterns, five production patterns, seven patterns, or three broad topologies. These differences appear to reflect classification granularity rather than a resolved canonical standard. [S1] [S5] [S8] [S9] [S14] [S18]
- The term swarm is used inconsistently: some sources mean sequential handoff with one active agent, while others mean concurrent shared-blackboard or event-driven exploration. Results cannot be compared without specifying concurrency, routing authority, and state-transfer semantics. [S12] [S18] [S23] [S25] [S30] [S31]
- Practitioner sources call orchestrator-worker the production default or most widely deployed, but no representative prevalence study is present. These claims should be treated as practitioner consensus, not validated market facts. [S1] [S9] [S11] [S14] [S18] [S30] [S31]
- The modified τ-bench evidence reports a slight swarm advantage over supervisor, while other sources provide no general architecture winner. The result may be caused by the specific sequential-handoff implementation, context translation, prompt design, or benchmark task structure rather than topology alone. [S20] [S22] [S25] [S26] [S1] [S3]
- Sources disagree or remain ambiguous about whether supervisor overhead is inherent to centralized topology or primarily caused by implementation choices such as translation layers, handoff messages, context forwarding, and package-specific prompts. [S11] [S14] [S22] [S25] [S26]
- Swarm may be resilient to individual-agent failure or centralized single points of failure while still being fragile with respect to correctness, convergence, observability, ordering, and coordination errors. Fault tolerance is therefore not operationally defined consistently. [S11] [S12] [S18]
- The financial-document benchmark reports precise quality and cost figures, but the available evidence does not establish peer review, full methodology, statistical uncertainty, code availability, or generalization beyond its domain. [S32] [S33] [S34] [S35] [S37]
- Many sources are practitioner guides, vendor-authored benchmark reports, preprints, or secondary summaries. Their qualitative design advice converges, but claims of superiority, prevalence, percentage improvement, and cost multipliers are not independently corroborated. [S1] [S6] [S7] [S9] [S11] [S14] [S16] [S20] [S30] [S32]

## Remaining Gaps

- A peer-reviewed, source-grounded canonical taxonomy mapping topology, workflow, concurrency, interaction objective, communication, state, and control layers is still missing.
- Full primary benchmark results are unavailable for the modified τ-bench comparison, including exact scores, token costs, repetitions, variance, prompts, retries, reasoning budgets, and implementation details.
- Controlled comparisons are missing across pipeline, fan-out, supervisor, hierarchy, debate, verifier, mesh, blackboard, and swarm systems against strong single-agent graph and deterministic baselines.
- The field lacks a reproducible evaluation contract combining outcome success, pass^k reliability, latency, cost, safety, policy compliance, coordination failures, and recovery behavior.
- It remains unclear when multi-agent coordination becomes worthwhile as tool count, context size, task length, specialization, or parallelism increases.
- The relative contributions of topology versus context partitioning, prompt design, model routing, handoff semantics, translation layers, caching, retries, and framework implementation are not isolated.
- Formal definitions and benchmarks are needed for swarm subtypes: sequential handoff, shared-blackboard, event-driven, mesh, and genuinely concurrent systems.
- Evidence is limited for debate, verification, blackboard, mesh, and decentralized systems outside selected task settings such as customer-service tool use and proposed financial-document extraction.
- Security and governance questions remain open around inter-agent privilege boundaries, prompt injection, privacy, provenance, collusion, unauthorized tool actions, and auditable shared state.
- The research stopped at the iteration limit; unresolved empirical questions should not be treated as answered.

## Conclusion

The landscape is best understood as a design space, not a leaderboard of universally superior architectures. Start with a deterministic workflow or strong single-agent graph. Add a pipeline when dependencies are fixed, fan-out when subtasks are independent and latency matters, supervisor or hierarchy when dynamic routing and synthesis are required, decentralized or mesh mechanisms when local autonomy or exploration is central, and debate or verification when independent checking justifies extra cost. In practice, hybrid systems combine these patterns with typed interfaces, shared or scoped state, bounded execution, recovery, observability, and governance. The clearest open problem is empirical: the available evidence does not yet establish architecture-independent winners. Reproducible, cross-domain evaluations must separate topology from implementation details and report quality, reliability, cost, latency, safety, and coordination failure together.

## Sources

- [S1] Agent Architecture Patterns: 2026 Taxonomy Guide — https://www.digitalapplied.com/blog/agent-architecture-patterns-taxonomy-2026
- [S2] LLM Agent Architectures 2026: Components and Patterns — https://futureagi.com/blog/llm-agent-architectures-core-components
- [S3] The Evolution of Agentic AI Software Architecture — https://arxiv.org/html/2602.10479v1
- [S4] The Landscape of LLM-Based Search Agents: A Survey — https://www.preprints.org/manuscript/202608.0572
- [S5] Multi-Agent Design Patterns: Architectural Topologies, Failure Modes, and Production Hardening — https://kenhuangus.substack.com/p/multi-agent-design-patterns-architectural
- [S6] Multi-agent system architecture: a comparison guide + best ... — https://www.openlayer.com/blog/multi-agent-system-architecture-guide
- [S7] Multi-agent system architecture: a comparison guide + best practices (March 2026) — Openlayer — https://www.openlayer.com/blog/post/multi-agent-system-architecture-guide
- [S8] LLM-Based Multi-Agent Orchestration: A Survey of Frameworks, Communication Protocols, and Emerging Patterns[v1] | Preprints.org — https://www.preprints.org/manuscript/202604.2147
- [S9] Multi-Agent Systems Explained: 2026 Patterns — https://decodethefuture.org/en/multi-agent-systems-explained
- [S10] LLMs for Multi-Agent Cooperation — https://xue-guang.com/post/llm-marl
- [S11] Multi-Agent Orchestration — Klu — https://klu.ai/glossary/multi-agent-orchestration
- [S12] Swarm vs. Supervisor: Multi-Agent Architecture Guide | Augment Code — https://www.augmentcode.com/guides/swarm-vs-supervisor
- [S13] Multi-Agent Systems: Orchestration Patterns | DataKnobs — https://www.dataknobs.com/agentic-ai/7-multi-ai-agent-systems.html
- [S14] Multi-Agent Orchestration: 5 Patterns That Work in 2026 — https://www.digitalapplied.com/blog/multi-agent-orchestration-5-patterns-that-work
- [S15] LLM-Based Multi-Agent Orchestration: A Survey of Frameworks, Communication Protocols, and Emerging Patterns — https://www.mdpi.com/1999-5903/18/6/326
- [S16] Benchmarking Multi-Agent Architectures - LangChain — https://www.langchain.com/blog/benchmarking-multi-agent-architectures
- [S17] Multi-Agent Architecture Patterns Guide 2026 | Supervisor vs Swarm vs Pipeline Design - How to Choose the Right Multi-Agent System Architecture — https://www.paperclipped.de/en/blog/multi-agent-architecture-patterns-design
- [S18] Agent Orchestration Patterns: Swarm vs Mesh vs Hierarchical — https://gurusup.com/en/blog/agent-orchestration-patterns
- [S19] Agent Benchmarks: tau-bench, SWE-bench, GAIA & pass^k — https://prefactor.tech/learn/agent-benchmarks
- [S20] Benchmarking Multi-Agent Architectures | daily.dev — https://daily.dev/posts/benchmarking-multi-agent-architectures-adykgmnac
- [S21] Benchmarking AI Agents: Stop Trusting Headline Scores ... — https://medium.com/alan/benchmarking-ai-agents-stop-trusting-headline-scores-start-measuring-trade-offs-0fdae3a418cf
- [S22] Evaluating Multi-Agent Architectures: A Performance Benchmark - Blockchain.News — https://blockchain.news/news/evaluating-multi-agent-architectures-performance-benchmark
- [S23] LangChain Comparison: Swarm vs Single Agent Architecture | Carmen Perez (she/her) posted on the topic | LinkedIn — https://www.linkedin.com/posts/carmen-a-perez_back-with-part-2-of-this-langchain-langgraph-activity-7413738338597228544-NkAW
- [S24] Exploring Multi-Agent Architectures: Supervisor, Graph, Tools & More — https://www.youtube.com/watch?v=gK9i6p2euVk
- [S25] Benchmarking Multi-Agent Architectures — https://blog.langchain.com/benchmarking-multi-agent-architectures
- [S26] Benchmarking Multi-Agent Architectures — https://www.blog.langchain.com/benchmarking-multi-agent-architectures
- [S27] Benchmarking Single Agent Performance — https://www.blog.langchain.com/react-agent-benchmarking
- [S28] Benchmarking Single Agent Performance — https://blog.langchain.com/react-agent-benchmarking
- [S29] Command: A new tool for building multi-agent architectures in LangGraph — https://www.blog.langchain.com/command-a-new-tool-for-multi-agent-architectures-in-langgraph
- [S30] Agent Orchestration Patterns: Swarm vs Mesh vs Hierarchical — https://gurusup.com/blog/agent-orchestration-patterns
- [S31] Agent Orchestration Patterns: Swarm vs Mesh vs Hierarchical — https://www.gurusup.com/blog/agent-orchestration-patterns
- [S32] Benchmarking Multi-Agent LLM Architectures for Financial Document Processing: A Comparative Study of Orchestration Patterns, Cost-Accuracy Tradeoffs and Production Scaling Strategies — https://www.catalyzex.com/paper/benchmarking-multi-agent-llm-architectures
- [S33] Benchmarking Multi-Agent LLM Architectures for Financial ... — https://chatpaper.com/chatpaper/paper/256194
- [S34] [2603.22651] Benchmarking Multi-Agent LLM Architectures for Financial Document Processing: A Comparative Study of Orchestration Patterns, Cost-Accuracy Tradeoffs and Production Scaling Strategies — https://arxiv.org/abs/2603.22651
- [S35] Benchmarking Multi-Agent LLM Architectures for Financial ... - GitHub — https://github.com/KatsuyaITO/indx-autoresearch-financeaiready/issues/913
- [S36] Siddhant Kulkarni — https://scholar.google.com/citations?user=JoO-FNUAAAAJ&hl=en
- [S37] Multi-Agent Finance Workflows Need Cost Curves, Not More ... — https://swarmsignal.net/multi-agent-finance-workflows-need-cost-curves
