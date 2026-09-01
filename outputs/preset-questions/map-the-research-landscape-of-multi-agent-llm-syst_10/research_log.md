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

**Unique Sources:** 37

**OpenAI Calls:** 11

**Tavily Calls:** 10

**Started:** 2026-09-01T04:59:51-04:00

**Ended:** 2026-09-01T05:04:17-04:00

**Total Runtime:** 265.69s

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
- **S2 — LLM Agent Architectures 2026: Components and Patterns**
  URL: https://futureagi.com/blog/llm-agent-architectures-core-components
- **S3 — The Evolution of Agentic AI Software Architecture**
  URL: https://arxiv.org/html/2602.10479v1
- **S4 — The Landscape of LLM-Based Search Agents: A Survey**
  URL: https://www.preprints.org/manuscript/202608.0572
- **S5 — Multi-Agent Design Patterns: Architectural Topologies, Failure Modes, and Production Hardening**
  URL: https://kenhuangus.substack.com/p/multi-agent-design-patterns-architectural

**Search Duration:** 3.65s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Multi-agent LLM systems can be organized primarily by coordination topology and interaction objective: collaborative decomposition, hierarchical orchestration, competitive critique/debate, and workflow-oriented graph or pipeline structures.

**Confidence:** Medium

**Why this confidence level**

The sources converge on recurring topology families, but two are practitioner sources and the academic source excerpt does not provide the full taxonomy or comparative empirical results.

**Evidence**

- A taxonomy groups systems into single-agent, collaborative multi-agent, competitive multi-agent, and orchestration-topology quadrants, including plan-and-execute, supervisor-worker, debate, and verifier-critic patterns. [S1]
- An engineering taxonomy identifies orchestrator-worker, pipelines, fan-out/fan-in map-reduce, critic-refiners, multi-tier hierarchies, event buses, and sidecar guardrails as production patterns. [S5]
- An academic architecture paper frames multi-agent systems as an evolution from single-agent control loops toward coordinated topologies, with explicit attention to failure modes and mitigations. [S3]

#### Finding 2

**Claim**

The dominant collaborative architecture is hierarchical supervisor/orchestrator-worker coordination: a central agent decomposes a goal, routes subtasks to specialized workers, and synthesizes their outputs.

**Confidence:** High

**Why this confidence level**

The architectural description is direct and consistent across three sources, although the claim that it is broadly dominant in practice is less strongly established.

**Evidence**

- The supervisor-worker pattern is described as a hierarchical system in which a supervisor decomposes tasks, routes them to specialized workers, and aggregates results. [S1]
- The orchestrator-worker pattern uses a central routing gateway, worker interface contracts, health checks, timeouts, and deterministic fallbacks. [S5]
- The academic reference architecture separates cognitive reasoning from execution through typed tool interfaces and identifies hierarchical memory, governance, and coordination as production concerns. [S3]

#### Finding 3

**Claim**

Parallel and staged workflows are important alternatives to hierarchical coordination, especially when subtasks can be statically partitioned or executed through predictable stages.

**Confidence:** Medium

**Why this confidence level**

The pattern families and their intended uses are supported, but the sources do not provide a unified comparison of when parallel, pipeline, or hierarchical designs outperform one another.

**Evidence**

- Plan-and-execute separates planning from execution and is positioned for predictable workflows, while acknowledging brittleness when conditions change. [S1]
- The production taxonomy includes pipelines and fan-out/fan-in map-reduce as distinct communication and execution structures. [S5]
- The search-agent survey describes workflows combining planners, retrievers, memories, verifiers, and writers under explicit tool budgets and evaluation contracts. [S4]

#### Finding 4

**Claim**

Critique, verification, and debate constitute a separate competitive/adversarial family intended to improve reliability rather than merely increase parallel throughput.

**Confidence:** Medium

**Why this confidence level**

The functional distinction between collaboration and critique is clear, but evidence for improved accuracy, safety, or cost is not quantified consistently in the retrieved material.

**Evidence**

- Multi-agent debate uses multiple positions and a judge or synthesizer; verifier-critic uses generation, rubric-based critique, and revision. [S1]
- The production guide includes critic-refiners and sidecar guardrails among its multi-agent patterns. [S5]
- The search-agent survey identifies verifiers and verifier-guided search as workflow components and learning/evaluation approaches. [S4]

#### Finding 5

**Claim**

Reliable multi-agent design depends on explicit contracts and bounded control, including typed inputs and outputs, execution budgets, timeouts, retries or fallbacks, observability, and policy enforcement.

**Confidence:** High

**Why this confidence level**

The engineering mechanisms are stated directly and align across the academic and practitioner sources, though their effectiveness is not established by controlled comparative evidence.

**Evidence**

- The academic paper argues for typed tool interfaces, auditable control mechanisms, observability, reproducibility, and layered governance; it identifies verifiability, interoperability, and safe autonomy as persistent challenges. [S3]
- The orchestrator-worker guide recommends strict JSON-schema worker contracts, health validation, timeout budgets, deterministic fallback handlers, bounded fan-out, and token ceilings. [S5]
- The component-oriented architecture source presents typed function calls, runtime state/retries/handoffs, memory, tools, and observability/evaluation as core layers. [S2]

#### Finding 6

**Claim**

A major design trade-off is adaptability versus predictability: generative planners and decentralized coordination offer flexibility, while symbolic constraints, explicit state machines, and governed execution improve verification and control.

**Confidence:** High

**Why this confidence level**

The trade-off is explicitly articulated in multiple sources and is not dependent on a single specific benchmark.

**Evidence**

- The academic paper contrasts symbolic/classical architectures with neural/generative designs and reports that hybrid systems increasingly use LLM decomposition with symbolic constraints on execution. [S3]
- The production guide recommends deterministic state machines, bounded budgets, access control, and avoidance of uncoordinated swarms because of cascading errors and unauthorized actions. [S5]
- The taxonomy describes plan-and-execute as cheaper and predictable but brittle under environmental change, and supervisor-worker as vulnerable to coordination overhead and surfaced conflicts. [S1]

### Conflicts Found

- The sources differ in how complete their taxonomies claim to be. S1 claims eight canonical patterns cover approximately 95% of production systems and presents hierarchical and graph topologies as the main production defaults, whereas S5 presents seven patterns and emphasizes orchestrator-worker and fan-out/fan-in. These are likely different classification schemes rather than a direct factual contradiction, but they cannot be reconciled into a single canonical count from the available evidence. [S1] [S5]
- S1 states that swarms and blackboard patterns are theoretically interesting but rarely outperform hierarchical or graph designs, while the retrieved excerpt from S3 discusses topologies and failure modes without supplying comparative results. The production-superiority claim is therefore unsupported by the academic evidence shown. [S1] [S3]
- S1 reports a 30–50% reduction in repeated failures for Reflexion, but no retrieved source independently confirms that figure or establishes that it transfers to multi-agent systems. This is not a direct contradiction, but it is a notable evidence-quality disparity. [S1] [S2]

### Important Gaps

- What is the complete, source-grounded taxonomy of multi-agent LLM architectures across peer-reviewed and primary research, including peer-to-peer, blackboard, swarm, graph, event-driven, and market/competitive systems?
- Under what task conditions do supervisor-worker, fan-out/fan-in, pipelines, graphs, debate, and decentralized swarms improve quality, latency, cost, or robustness relative to a strong single-agent baseline?
- How should multi-agent systems be evaluated consistently across task success, coordination overhead, error propagation, calibration, safety, cost, latency, and reproducibility?
- What empirical evidence supports claims that hierarchical systems outperform swarms or that verifier/debate systems improve reliability, rather than merely increasing token use?
- How are inter-agent communication, shared memory, provenance, privacy, prompt injection, privilege boundaries, and collusion handled in deployed systems?
- Which architectural choices are genuinely model-independent, and which depend on model capability, context length, tool-use reliability, or training procedure?
- The retrieved material is heavily oriented toward 2026 practitioner guidance and future-dated sources; the landscape needs validation against established primary papers, benchmarks, and implementation reports.

**Analysis Duration:** 20.46s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The current sources support a preliminary design taxonomy and identify key engineering trade-offs, but they are insufficient for a research landscape report: primary research coverage, empirical comparisons, benchmark evidence, and several topology families are missing. Another search would materially improve the answer by locating surveys and foundational papers that compare multi-agent architectures and evaluation methods.

**Next Search**

> multi-agent LLM systems survey architectural topologies benchmarks evaluation supervisor worker debate swarm blackboard peer-to-peer

---

# Iteration 2

## 1. Search

**Query**

> multi-agent LLM systems survey architectural topologies benchmarks evaluation supervisor worker debate swarm blackboard peer-to-peer

**Why this query**

The current sources support a preliminary design taxonomy and identify key engineering trade-offs, but they are insufficient for a research landscape report: primary research coverage, empirical comparisons, benchmark evidence, and several topology families are missing. Another search would materially improve the answer by locating surveys and foundational papers that compare multi-agent architectures and evaluation methods.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S6 — Multi-agent system architecture: a comparison guide + best ...**
  URL: https://www.openlayer.com/blog/multi-agent-system-architecture-guide
- **S7 — Multi-agent system architecture: a comparison guide + best practices (March 2026) — Openlayer**
  URL: https://www.openlayer.com/blog/post/multi-agent-system-architecture-guide
- **S8 — LLM-Based Multi-Agent Orchestration: A Survey of Frameworks, Communication Protocols, and Emerging Patterns[v1] | Preprints.org**
  URL: https://www.preprints.org/manuscript/202604.2147
- **S9 — Multi-Agent Systems Explained: 2026 Patterns**
  URL: https://decodethefuture.org/en/multi-agent-systems-explained
- **S10 — LLMs for Multi-Agent Cooperation**
  URL: https://xue-guang.com/post/llm-marl

**Search Duration:** 3.76s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new survey source offers a useful unifying taxonomy: coordination topology can be classified as centralized, decentralized, or hierarchical, with a separate dynamic/adaptive-control axis.

**Confidence:** Medium

**Why this confidence level**

This is a direct claim from a survey, but the source is a preprint and its taxonomy should be validated against the peer-reviewed version or primary papers.

**Evidence**

- The survey explicitly proposes a three-topology, one-adaptivity taxonomy and treats task allocation, communication, state management, sequencing, and recovery as the core orchestration mechanisms. [S8]

#### Finding 2

**Claim**

The landscape is better represented as multiple orthogonal dimensions than as a single list of canonical patterns: topology, control adaptivity, interaction objective, workflow structure, and communication/state mechanism.

**Confidence:** High

**Why this confidence level**

The sources converge on distinct architectural dimensions, even though they use different labels and granularity.

**Evidence**

- S8 separates topology from dynamic/adaptive control and identifies five orchestration mechanisms. [S8]
- S10 distinguishes cooperation, competition, and coopetition; centralized, peer-to-peer, and distributed structures; role-based and model-based strategies; and memory-based, report-based, relay, and debate communication. [S10]
- Prior sources distinguish supervisor-worker, hierarchy, pipelines, fan-out/fan-in, critique, event-driven, graph, and guardrail patterns. [S1] [S3] [S5]

#### Finding 3

**Claim**

Peer-to-peer, blackboard, and swarm designs are important decentralized branches, but the retrieved evidence characterizes them mainly by trade-offs rather than reliable superiority.

**Confidence:** Medium

**Why this confidence level**

The architectural distinctions are supported, but comparative performance claims remain weak and largely practitioner-reported.

**Evidence**

- S6/S7 describe peer-to-peer, blackboard, and swarm as core patterns; swarm agents coordinate through shared state or a bus without central control and trade auditability for parallelism and resilience. [S6] [S7]
- S10 describes decentralized peer-to-peer systems as more resilient but more coordination-complex, and identifies memory-based communication and bus/network structures as alternatives to centralized coordination. [S10]
- Prior evidence says claims that hierarchical or graph systems outperform swarms lack independent academic comparative support. [S1] [S3]

#### Finding 4

**Claim**

The most important empirical boundary is task structure: multi-agent systems may help with parallelizable, specialized, or critique-heavy work, but can hurt sequential reasoning because coordination adds latency, tokens, and failure opportunities.

**Confidence:** Medium

**Why this confidence level**

The direction of the trade-off is consistent, but the numerical degradation and improvement figures are not independently corroborated in the retrieved material.

**Evidence**

- S6/S7 report that multi-agent systems outperform single agents on parallelizable tasks but degrade on sequential reasoning, while describing supervisor bottlenecks and chain error propagation. [S6] [S7]
- S1 describes plan-and-execute as predictable but brittle under changing conditions and supervisor-worker as vulnerable to coordination overhead. [S1]
- S8 identifies coordination failures, duplicated effort, contradictions, and inconsistent shared state as system-level degradation mechanisms. [S8]

#### Finding 5

**Claim**

Coordination complexity and evaluation are emerging as central research problems, not merely implementation concerns.

**Confidence:** High

**Why this confidence level**

Multiple sources directly identify coordination scaling, evaluation, recovery, and security as persistent gaps.

**Evidence**

- S8 notes that pairwise interaction channels grow from 10 for five agents to 45 for ten agents, and proposes a six-dimension evaluation framework while identifying open challenges in state, planning, recovery, scalability, and security. [S8]
- Prior sources emphasize typed contracts, budgets, observability, provenance, governance, privacy, prompt injection, and reproducibility as unresolved or essential concerns. [S2] [S3] [S5]
- S10 adds communication paradigms, shared memory, role specialization, graph workflows, and adaptive/co-evolutionary behavior as active research directions. [S10]

#### Finding 6

**Claim**

Protocols and frameworks form a distinct infrastructure layer in the landscape, alongside architectural topology.

**Confidence:** Medium

**Why this confidence level**

The infrastructure distinction is clear, but the retrieved excerpts do not provide independent benchmark evidence for framework comparisons.

**Evidence**

- S8 compares LangGraph, CrewAI, AutoGen/Microsoft Agent Framework, and OpenAI Agents SDK by state management, token cost, recovery, and design philosophy, and distinguishes MCP agent-to-tool protocols from A2A agent-to-agent protocols. [S8]
- S10 describes orchestration platforms as infrastructure for interaction, communication, planning, and learning, while identifying framework examples for centralized, decentralized, hierarchical, role-based, and graph designs. [S10]

### Conflicts Found

- S6/S7 and S9 make strong quantitative production claims: supervisor improvements of 80% on parallel tasks, 39–70% degradation on sequential reasoning, approximately 58% token overhead for independent systems, 285% for centralized systems, and roughly 70% orchestrator-worker production prevalence. These figures are not independently confirmed by S8, S10, or the prior sources; S9 additionally gives a different high-level topology count than the broader taxonomies. [S6] [S7] [S9] [S8] [S10]
- S6/S7 state that supervisor coordination overhead scales linearly, whereas S8 describes multi-agent interaction and debugging burdens as super-linear or compounded, and S9 describes centralized systems as having substantial overhead. These statements may refer to different communication models—star-shaped supervisor routing versus general peer interaction—but the distinction is not made rigorously in the retrieved excerpts. [S6] [S7] [S8] [S9]
- S8 presents centralized, decentralized, and hierarchical as the principal topology taxonomy, while S9 says three topologies dominate production and treats supervisor/hierarchical and orchestrator-worker as partly separate categories. This is a classification-granularity disagreement rather than necessarily a substantive architectural contradiction. [S8] [S9]

### Important Gaps

- Which claims and numerical results in S6/S7/S9 come from identifiable primary benchmarks, and what were the models, tasks, baselines, and cost accounting methods?
- Does the peer-reviewed version of S8 provide validated empirical comparisons and a complete six-dimension evaluation framework, or only a survey proposal?
- How should the final visual taxonomy distinguish topology from workflow pattern, communication protocol, memory/state architecture, evaluation/guardrail layer, and adaptation?
- What primary research establishes when debate, verification, blackboard, peer-to-peer, or swarm architectures outperform strong single-agent and centralized baselines?
- How do protocol choices such as MCP, A2A, ACP, and ANP affect interoperability, security, latency, and coordination quality in actual systems?
- Are the reported production-prevalence and token-overhead figures representative, or are they vendor/blog claims with unclear sampling and methodology?

**Analysis Duration:** 19.15s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources improve the conceptual taxonomy and identify protocols and evaluation as separate layers, but the most consequential quantitative claims are unverified, and the accumulated state still lacks primary-paper and benchmark evidence for architecture comparisons. Another focused search would materially improve the report by grounding the taxonomy and trade-offs in primary empirical studies.

**Next Search**

> primary benchmark multi-agent LLM architectures supervisor orchestrator worker debate swarm peer-to-peer single-agent baseline cost latency reliability

---

# Iteration 3

## 1. Search

**Query**

> primary benchmark multi-agent LLM architectures supervisor orchestrator worker debate swarm peer-to-peer single-agent baseline cost latency reliability

**Why this query**

The new sources improve the conceptual taxonomy and identify protocols and evaluation as separate layers, but the most consequential quantitative claims are unverified, and the accumulated state still lacks primary-paper and benchmark evidence for architecture comparisons. Another focused search would materially improve the report by grounding the taxonomy and trade-offs in primary empirical studies.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S11 — Multi-Agent Orchestration — Klu**
  URL: https://klu.ai/glossary/multi-agent-orchestration
- **S12 — Swarm vs. Supervisor: Multi-Agent Architecture Guide | Augment Code**
  URL: https://www.augmentcode.com/guides/swarm-vs-supervisor
- **S13 — Multi-Agent Systems: Orchestration Patterns | DataKnobs**
  URL: https://www.dataknobs.com/agentic-ai/7-multi-ai-agent-systems.html
- **S14 — Multi-Agent Orchestration: 5 Patterns That Work in 2026**
  URL: https://www.digitalapplied.com/blog/multi-agent-orchestration-5-patterns-that-work

**Search Duration:** 3.60s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The five-pattern decomposition—fan-out, pipeline, supervisor, swarm, and debate—clarifies distinctions that are often collapsed in broader taxonomies.

**Confidence:** Medium

**Why this confidence level**

The distinction is explicit and useful, but both new sources are practitioner-oriented and do not establish a peer-reviewed canonical taxonomy.

**Evidence**

- S14 distinguishes fan-out parallel scatter-gather from sequential pipelines, debate from supervisor delegation, and swarm from centralized coordination, emphasizing different control flows and failure modes. [S14]
- S11 independently presents hierarchical supervisor, sequential pipeline, swarm/peer-to-peer, and debate as common orchestration patterns, while describing orchestration as routing, scheduling, memory management, and conflict resolution. [S11]

#### Finding 2

**Claim**

Fan-out parallelism should be treated as distinct from swarm architectures: fan-out uses centralized dispatch and concurrent execution, whereas the described swarm pattern uses decentralized sequential handoffs.

**Confidence:** Medium

**Why this confidence level**

The architectural distinction is direct across two sources, although the sources are engineering guides rather than controlled comparative studies.

**Evidence**

- S12 explicitly contrasts fan-out parallelism—central coordination with multiple simultaneous workers—with swarm control, in which one agent is active at a time and routing is distributed through handoffs. [S12]
- S14 defines fan-out as parallel scatter-gather and swarm as dynamic peer-agent coordination with distinct cost and failure characteristics. [S14]

#### Finding 3

**Claim**

Architecture selection should be conditioned on task dependency structure: independent subtasks favor fan-out or decentralized execution, while dynamic dependencies, ordering, and conflict resolution favor a supervisor or hybrid supervisor-plus-parallel design.

**Confidence:** High

**Why this confidence level**

The conditional design principle is consistent across several sources, even though its quantitative performance boundaries remain unvalidated.

**Evidence**

- S12 states that swarm patterns fit independent workloads with embedded routing, while supervisors fit dynamic routing, ordered execution, and conflict resolution; it recommends hybrids combining supervisor planning with parallel execution. [S12]
- S11 characterizes pipelines as efficient and predictable for deterministic dependencies, supervisors as suitable for complex planning and synthesis, and swarms as flexible but difficult to control. [S11]
- Prior findings similarly identify parallelizable work as a favorable condition and sequential reasoning as a setting where coordination can add cost and failure opportunities. [S1] [S6] [S7]

#### Finding 4

**Claim**

The principal engineering trade-offs across patterns are coordination overhead, latency, complexity, predictability, and fault tolerance; no pattern dominates on all dimensions.

**Confidence:** Medium

**Why this confidence level**

The qualitative trade-offs converge, but the comparison matrices are asserted by practitioner sources and lack standardized measurements.

**Evidence**

- S11 provides a comparison matrix: pipelines have low overhead and complexity but low fault tolerance; supervisors have higher overhead and medium-to-high latency; swarms have very high overhead and complexity but high fault tolerance; debate has high cost and latency with high fault tolerance. [S11]
- S14 attributes different failure modes to fan-out, pipeline, debate, supervisor, and swarm, including partial branch failure, cascade failure, repeated perspective costs, routing loops, and emergent coordination problems. [S14]
- Prior sources describe the broader adaptability-versus-predictability trade-off and recommend bounded execution, explicit contracts, and deterministic controls. [S3] [S5]

#### Finding 5

**Claim**

The new sources reinforce that debate is an interaction objective and control pattern, not simply another form of supervisor delegation.

**Confidence:** High

**Why this confidence level**

The functional distinction is explicit and consistent across new and prior evidence, though effectiveness relative to strong baselines remains uncertain.

**Evidence**

- S14 differentiates supervisor systems, which delegate non-overlapping subtasks, from debate systems, which send the same question to multiple agents and adjudicate disagreement with a judge. [S14]
- S11 describes debate as multi-perspective critique and adjudication for fact-checking, code review, and high-accuracy tasks, with increased latency and token use. [S11]
- Prior findings classify critique, verification, and debate as an adversarial or reliability-oriented family distinct from throughput-oriented collaboration. [S1] [S4] [S5]

#### Finding 6

**Claim**

Claims of production prevalence and numerical cost or quality improvements in the new sources should not be treated as established landscape facts without primary-source verification.

**Confidence:** High

**Why this confidence level**

The evidence directly shows that the figures are reported claims with incomplete or non-independent methodological support; this is an evidence-quality finding rather than a judgment that the numbers are false.

**Evidence**

- S11 reports a 90.2% improvement on an internal research evaluation and approximately 15× token use for a multi-agent system, attributing the figures to an Anthropic engineering write-up; the excerpt is incomplete and does not provide benchmark methodology. [S11]
- S14 reports approximately 2.5× debate cost and large swarm scale claims, but presents them in a practitioner guide without detailed experimental protocols or independent corroboration. [S14]
- Prior findings already flag unverified claims about production prevalence, token overhead, and performance from S6/S7/S9. [S6] [S7] [S9]

### Conflicts Found

- S14 calls supervisor the 2026 production default and S11 calls hierarchical supervisor the most common or intuitive approach, while the accumulated evidence explicitly warns that production-prevalence figures and canonical pattern counts are weakly sourced. These sources support a practitioner perception, not a validated prevalence estimate. [S11] [S14] [S1] [S5] [S9]
- S11's matrix labels swarm as highly fault-tolerant, whereas S12 emphasizes swarm brittleness, chaotic behavior, redundant work, and difficult debugging. This is a conditional disagreement: swarms may tolerate individual-agent failure or single points of failure while remaining vulnerable to coordination and correctness failures. [S11] [S12]
- S12 states that swarm execution is strictly sequential with one active agent, while S11 describes swarm/peer-to-peer as highly scalable and suitable for distributed workflows. Scalability here may refer to agent population or routing distribution rather than concurrent execution; the sources do not define the metric consistently. [S11] [S12]
- S11 and S14 describe pipelines as low-overhead and predictable, but S14 emphasizes cascade failure in pipelines. Thus efficiency and predictability do not imply robustness when an intermediate stage is wrong. [S11] [S14]

### Important Gaps

- Which of the five patterns are supported by peer-reviewed primary research, and how should they be mapped to the broader topology/adaptivity/objective/state dimensions?
- Under controlled evaluations, when do fan-out, supervisor, pipeline, debate, and swarm outperform a strong single-agent baseline on quality, cost, latency, and robustness?
- Does the Anthropic internal evaluation cited by S11 generalize beyond research tasks, and how were token costs and baselines measured?
- What operational definition of fault tolerance distinguishes recovery from agent failure, resilience to routing failure, and correctness under coordination errors?
- Are swarm systems genuinely concurrent in the target architecture, or are decentralized sequential handoff systems being conflated with parallel multi-agent execution?
- How do hybrid architectures combine centralized planning, parallel execution, verification, shared state, and recovery without reproducing supervisor bottlenecks?

**Analysis Duration:** 21.23s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources improve the visual taxonomy by separating fan-out from swarm and clarifying task-structure matching, but they are predominantly practitioner guides and introduce additional unverified prevalence, cost, and scale claims. The original question asks for a research landscape, so primary academic architectures and benchmark evidence are still needed to support the taxonomy and identify empirically grounded open problems.

**Next Search**

> peer-reviewed survey primary benchmarks multi-agent LLM architectures fan-out supervisor pipeline debate swarm single-agent baseline evaluation

---

# Iteration 4

## 1. Search

**Query**

> peer-reviewed survey primary benchmarks multi-agent LLM architectures fan-out supervisor pipeline debate swarm single-agent baseline evaluation

**Why this query**

The new sources improve the visual taxonomy by separating fan-out from swarm and clarifying task-structure matching, but they are predominantly practitioner guides and introduce additional unverified prevalence, cost, and scale claims. The original question asks for a research landscape, so primary academic architectures and benchmark evidence are still needed to support the taxonomy and identify empirically grounded open problems.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S15 — LLM-Based Multi-Agent Orchestration: A Survey of Frameworks, Communication Protocols, and Emerging Patterns**
  URL: https://www.mdpi.com/1999-5903/18/6/326
- **S16 — Benchmarking Multi-Agent Architectures - LangChain**
  URL: https://www.langchain.com/blog/benchmarking-multi-agent-architectures
- **S17 — Multi-Agent Architecture Patterns Guide 2026 | Supervisor vs Swarm vs Pipeline Design - How to Choose the Right Multi-Agent System Architecture**
  URL: https://www.paperclipped.de/en/blog/multi-agent-architecture-patterns-design
- **S18 — Agent Orchestration Patterns: Swarm vs Mesh vs Hierarchical**
  URL: https://gurusup.com/en/blog/agent-orchestration-patterns

**Search Duration:** 4.96s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources do not materially strengthen the evidence for a complete research taxonomy because S15 provides only bibliographic and webpage metadata, without substantive survey content.

**Confidence:** High

**Why this confidence level**

The available source excerpt is visibly limited to page metadata and navigation.

**Evidence**

- S15 identifies a survey on frameworks, communication protocols, and emerging patterns, but the retrieved content contains no abstract, taxonomy, methods, or findings. [S15]

#### Finding 2

**Claim**

A practitioner benchmark exists that directly compares multi-agent architectures on a modified τ-bench dataset, making it potentially relevant to the unresolved question of controlled architecture comparisons.

**Confidence:** Medium

**Why this confidence level**

The source directly describes a benchmark and its evaluation dimensions, but the retrieved excerpt ends before reporting architecture-level results, baselines, or methodology.

**Evidence**

- S16 states that it benchmarks common multi-agent architectures on a modified τ-bench dataset and evaluates performance and token cost; it also reports an improvement to its supervisor implementation. [S16]

#### Finding 3

**Claim**

The available benchmark source motivates multi-agent systems partly by context and tool-scaling problems, modularity, maintainability, parallelization, and integration of separately developed agents.

**Confidence:** Medium

**Why this confidence level**

These are explicit motivations in a technical blog, but they are not independently validated causal findings in the retrieved material.

**Evidence**

- S16 identifies degradation of a single agent as tool and context size increase, along with modularity, evaluation, maintenance, parallelization, and organizational integration as motivations for multi-agent architectures. [S16]

#### Finding 4

**Claim**

Generic multi-agent architectures may be easier to adopt, while custom domain-specific cognitive architectures may perform better for particular applications; this reinforces the need to distinguish reusable patterns from application-specific designs.

**Confidence:** Medium

**Why this confidence level**

The distinction is clearly stated, but the source provides no comparative experiments supporting the performance claim.

**Evidence**

- S16 contrasts generic architectures, which ease adoption and support bring-your-own-agent integration, with custom architectures that may yield better domain-specific results. [S16]

#### Finding 5

**Claim**

The five-pattern engineering decomposition is consistent with the accumulated landscape: orchestrator-worker, swarm, mesh or peer-to-peer, hierarchical delegation, and pipeline, with hybrids treated as common combinations.

**Confidence:** Medium

**Why this confidence level**

The new sources reinforce recurring practitioner categories, but they do not establish a peer-reviewed canonical list or resolve classification-granularity differences.

**Evidence**

- S18 presents orchestrator-worker, swarm, mesh, hierarchical, and pipeline as five main orchestration patterns and states that production systems may combine two or more patterns. [S18]
- S17 summarizes sequential pipeline, coordinator/router, parallel fan-out, hierarchical delegation, consensus, competitive evaluation, human checkpoints, and dynamic spawning as design patterns. [S17]
- Prior evidence independently distinguishes fan-out, pipeline, supervisor, swarm, debate, peer-to-peer, and hierarchical structures. [S11] [S12] [S14]

#### Finding 6

**Claim**

The new practitioner material supports conditional architecture selection: sequential pipelines fit strict dependencies, coordinators or supervisors fit dynamic routing and synthesis, and fan-out fits independent subtasks where latency is the primary bottleneck.

**Confidence:** High

**Why this confidence level**

The design rule is consistent across several sources, though quantitative performance boundaries remain unavailable.

**Evidence**

- S17 associates sequential pipelines with strict dependencies, coordinator/router systems with known task categories and dynamic dispatch, and parallel fan-out with independent subtasks and latency reduction. [S17]
- S18 associates orchestrator-worker with centralized decomposition and aggregation, and pipeline with sequential stage processing; it also identifies bottlenecks and context limitations in orchestrator-worker systems. [S18]
- Prior sources make the same conditional distinction between independent or parallelizable workloads and dynamically ordered or conflict-heavy work. [S11] [S12]

#### Finding 7

**Claim**

Decentralized swarm and mesh systems trade centralized auditability and ordering guarantees for local autonomy, exploration, and potential resilience, but require explicit termination and distributed observability mechanisms.

**Confidence:** Medium

**Why this confidence level**

The trade-offs are convergent, but S18 is a practitioner source and does not establish that swarms deliver superior exploration or resilience under controlled evaluation.

**Evidence**

- S18 describes swarms as decentralized systems using shared state or handoffs, with risks in observability, convergence, strict ordering, and transactional guarantees; it recommends termination conditions and distributed tracing or event sourcing. [S18]
- Prior evidence characterizes peer-to-peer, blackboard, and swarm systems as more flexible or resilient but harder to audit, debug, and control. [S6] [S7] [S10] [S12]

#### Finding 8

**Claim**

The new material does not resolve the central empirical question of whether particular architectures outperform strong single-agent or alternative multi-agent baselines on quality, cost, latency, and robustness.

**Confidence:** High

**Why this confidence level**

The sources either lack results in the retrieved excerpt or are qualitative practitioner guidance; therefore the prior evidence gap remains.

**Evidence**

- S16 announces a τ-bench comparison but the retrieved excerpt omits results, experimental configuration, and baseline comparisons. [S16]
- S17 refers to LangChain benchmarking and claims a performance gap, but the excerpt stops before presenting the underlying measurements and methodology. [S17]
- S18 provides qualitative claims and operational examples but no controlled benchmark results. [S18]

### Conflicts Found

- S18 describes swarm systems as potentially exploring many branches in parallel, while prior S12 characterized a swarm implementation as sequential handoffs with one active agent. This is likely an implementation distinction—parallel blackboard-style swarm versus sequential handoff swarm—but the new source does not define the execution model rigorously enough to reconcile them. [S12] [S18]
- S18 calls orchestrator-worker the most widely deployed production pattern and says it is a default starting point, while the accumulated state warns that prevalence claims from practitioner sources are not validated. The new source reinforces practitioner consensus but does not establish representative prevalence. [S18] [S1] [S5] [S9]
- S17 presents hierarchical delegation, consensus, competitive evaluation, human checkpoints, and dynamic spawning as patterns to postpone for many teams, whereas the broader taxonomy treats critique, debate, guardrails, and hierarchy as important architectural branches. This is a recommendation about adoption priority, not a contradiction about existence or relevance. [S17] [S1] [S3] [S5]

### Important Gaps

- What are the actual architecture-level results, models, prompts, datasets, and cost accounting in the LangChain modified τ-bench benchmark referenced by S16?
- Does the full S15 survey provide a validated taxonomy, primary-paper mapping, benchmark synthesis, and treatment of blackboard, market, event-driven, and competitive systems?
- Are swarm systems being compared consistently when some implementations are parallel shared-state systems and others are sequential handoff systems?
- Do the practitioner claims about production prevalence and architecture superiority generalize beyond vendor-specific or internal evaluations?
- What peer-reviewed primary studies provide controlled comparisons across pipeline, fan-out, supervisor, debate, mesh, and swarm architectures against strong single-agent baselines?

**Analysis Duration:** 21.35s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources reinforce the qualitative taxonomy and conditional design rules, but the most important unresolved part of the original task—an evidence-grounded research landscape with empirical comparisons and open-problem boundaries—remains weak. S15 is substantively unavailable, and S16/S17 do not include benchmark results in the retrieved excerpts. A focused search for primary comparative benchmarks would materially improve the report.

**Next Search**

> peer-reviewed primary benchmark compare multi-agent LLM architectures supervisor fan-out pipeline debate swarm single-agent tau-bench GAIA cost latency reliability

---

# Iteration 5

## 1. Search

**Query**

> peer-reviewed primary benchmark compare multi-agent LLM architectures supervisor fan-out pipeline debate swarm single-agent tau-bench GAIA cost latency reliability

**Why this query**

The new sources reinforce the qualitative taxonomy and conditional design rules, but the most important unresolved part of the original task—an evidence-grounded research landscape with empirical comparisons and open-problem boundaries—remains weak. S15 is substantively unavailable, and S16/S17 do not include benchmark results in the retrieved excerpts. A focused search for primary comparative benchmarks would materially improve the report.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S19 — Agent Benchmarks: tau-bench, SWE-bench, GAIA & pass^k**
  URL: https://prefactor.tech/learn/agent-benchmarks
- **S20 — Benchmarking Multi-Agent Architectures | daily.dev**
  URL: https://daily.dev/posts/benchmarking-multi-agent-architectures-adykgmnac
- **S21 — Benchmarking AI Agents: Stop Trusting Headline Scores ...**
  URL: https://medium.com/alan/benchmarking-ai-agents-stop-trusting-headline-scores-start-measuring-trade-offs-0fdae3a418cf

**Search Duration:** 4.32s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Public agent benchmarks emphasize outcome-based evaluation and repeated-trial reliability, but a benchmark score alone does not establish production readiness.

**Confidence:** High

**Why this confidence level**

Both sources directly describe outcome-based and reliability-oriented evaluation, while their methodological and production caveats are consistent.

**Evidence**

- S19 describes benchmarks that score environment outcomes such as database state or passing tests, distinguishes pass@k from stricter pass^k reliability, and warns that benchmark-domain capability does not guarantee fitness for a specific deployment. [S19]
- S21 explains that Tau-bench evaluates both final responses and resulting database state, and argues that production decisions require score-latency-cost trade-offs rather than headline accuracy alone. [S21]

#### Finding 2

**Claim**

Tau-bench and Tau2-bench are relevant evaluation environments for multi-agent research because they test stateful tool use, policy compliance, interaction, and partial observability rather than only text generation.

**Confidence:** High

**Why this confidence level**

The benchmark structure is described directly and consistently by two sources.

**Evidence**

- S19 identifies tau-bench and tau2-bench as customer-service benchmarks involving simulated users, domain APIs, policy following, and final database-state checks. [S19]
- S21 describes agent and user simulators with distinct tools and databases in Tau2-bench, creating coordination under partial observability. [S21]

#### Finding 3

**Claim**

The newly retrieved material provides only limited evidence about architecture-level comparisons: a secondary report says a LangChain experiment compared single-agent, swarm, and supervisor systems on a modified Tau-bench dataset, with swarm best overall and an optimized supervisor improving substantially.

**Confidence:** Low

**Why this confidence level**

S20 is a secondary summary, omits experimental configuration and detailed results, and does not establish whether the comparison was independently reproduced or statistically robust.

**Evidence**

- S20 reports that LangChain researchers compared single agent, swarm, and supervisor architectures on a modified Tau-bench dataset with distractor domains; it states that swarm performed best overall and that supervisor changes produced nearly a 50% improvement. [S20]

#### Finding 4

**Claim**

The new evidence reinforces that architecture comparisons are highly sensitive to prompts, reasoning budgets, retries, user simulators, and other evaluation settings, making published scores difficult to compare directly.

**Confidence:** High

**Why this confidence level**

The methodological concerns are explicit in both sources and directly bear on multi-agent architecture benchmarking.

**Evidence**

- S21 reports that optimized prompts, undisclosed reasoning effort, different user simulators, and retry logic can materially affect Tau-bench results and make comparisons apples-to-oranges. [S21]
- S19 recommends fixing model version, temperature, tools, and prompts, using enough repeated trials, and reporting reliability metrics rather than a single run. [S19]

#### Finding 5

**Claim**

A useful evaluation layer for the taxonomy should include task success, repeated-trial reliability, latency, cost, safety or policy compliance, and robustness under realistic stateful interaction.

**Confidence:** High

**Why this confidence level**

The dimensions are directly supported, although the sources do not prescribe a complete standardized multi-agent evaluation protocol.

**Evidence**

- S19 identifies capability, pass^k reliability, domain fit, and limitations involving cost, latency, and safety. [S19]
- S21 recommends mapping score against latency and cost and describes policy-constrained, state-changing interactions as part of Tau-bench evaluation. [S21]

### Conflicts Found

- S20 reports that swarm performed best overall in a modified Tau-bench comparison, whereas prior evidence says no architecture has established superiority across task types and warns that hierarchy-versus-swarm claims lack independent comparative support. This is not necessarily a direct contradiction: S20 may reflect one benchmark configuration, but it cannot support a general swarm advantage. [S20] [S1] [S3] [S16]
- S20 reports a nearly 50% supervisor improvement after implementation changes, while the accumulated state treats similar architecture-improvement figures as unverified without primary methodology and full results. The difference is evidence quality rather than a demonstrated factual contradiction. [S20] [S16] [S6] [S7]
- S19 presents pass^k as a strict reliability signal, while common pass@k reporting can make systems appear stronger by counting success on any attempt. Results using these metrics are not directly interchangeable. [S19] [S21]

### Important Gaps

- What are the full architecture-level results, task splits, models, prompts, reasoning settings, retry policies, and statistical treatment in the LangChain modified Tau-bench comparison reported by S20?
- Does the reported swarm advantage persist against a strong single-agent baseline and optimized supervisor when prompts, model budgets, tool access, and retries are standardized?
- How do fan-out, pipeline, debate, blackboard, mesh, and other architectures compare on benchmarks beyond customer-service tool use, such as coding, web navigation, long-horizon planning, and safety-critical tasks?
- Which evaluation protocol combines quality, pass^k reliability, latency, token or monetary cost, safety, and coordination failure metrics in a reproducible architecture comparison?
- Are the reported improvements caused by topology, by implementation details such as removing handoff messages and forwarding context, or by differences in prompt and context management?

**Analysis Duration:** 14.94s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources materially strengthen the evaluation and benchmarking layer of the landscape, but they do not close the central empirical gap: controlled, primary comparisons of multi-agent architectures against strong single-agent and alternative-architecture baselines. The key new architecture result is available only through a secondary summary with incomplete methodology.

**Next Search**

> LangChain blog modified tau-bench single agent swarm supervisor full results methodology architecture comparison

---

# Iteration 6

## 1. Search

**Query**

> LangChain blog modified tau-bench single agent swarm supervisor full results methodology architecture comparison

**Why this query**

The new sources materially strengthen the evaluation and benchmarking layer of the landscape, but they do not close the central empirical gap: controlled, primary comparisons of multi-agent architectures against strong single-agent and alternative-architecture baselines. The key new architecture result is available only through a secondary summary with incomplete methodology.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S22 — Evaluating Multi-Agent Architectures: A Performance Benchmark - Blockchain.News**
  URL: https://blockchain.news/news/evaluating-multi-agent-architectures-performance-benchmark
- **S23 — LangChain Comparison: Swarm vs Single Agent Architecture | Carmen Perez (she/her) posted on the topic | LinkedIn**
  URL: https://www.linkedin.com/posts/carmen-a-perez_back-with-part-2-of-this-langchain-langgraph-activity-7413738338597228544-NkAW
- **S24 — Exploring Multi-Agent Architectures: Supervisor, Graph, Tools & More**
  URL: https://www.youtube.com/watch?v=gK9i6p2euVk

**Search Duration:** 3.29s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new benchmark summary provides more specific, but still secondary, evidence that a modified τ-bench comparison evaluated single-agent, swarm, and supervisor architectures under distractor domains.

**Confidence:** Medium

**Why this confidence level**

The architecture definitions, task setting, and distractor-domain design are described directly, but S22 is a news summary rather than the primary benchmark report.

**Evidence**

- The report says LangChain compared a single agent with access to all tools and instructions, a swarm using agent-to-agent handoffs, and a supervisor delegating to sub-agents on modified retail, flight-booking, tech-support, and automotive environments designed to test irrelevant-tool and instruction filtering. [S22]

#### Finding 2

**Claim**

In the modified τ-bench setting, the reported qualitative result favors swarm slightly over supervisor when direct inter-agent communication is useful, while single-agent performance deteriorates as distractor domains increase.

**Confidence:** Low

**Why this confidence level**

The result is reported without numerical scores, statistical analysis, model configuration, or the primary study text; it should not be generalized beyond this benchmark configuration.

**Evidence**

- S22 reports that the single-agent system struggled with multiple distractor domains and that swarm slightly outperformed supervisor because agents could communicate directly. [S22]

#### Finding 3

**Claim**

The benchmark summary reinforces that context-routing and translation overhead are plausible explanations for supervisor cost or performance differences, rather than evidence that topology alone determines outcomes.

**Confidence:** Medium

**Why this confidence level**

Both sources identify concrete implementation mechanisms—translation, context forwarding, handoffs, and call count—but neither isolates topology from prompt and state-management choices experimentally.

**Evidence**

- S22 says supervisor token use was higher because of a translation layer between the supervisor and sub-agents, and that information-handling and context-management changes mitigated initial supervisor weaknesses. [S22]
- S23 reports that handoffs can cause context drift and that a single-agent graph typically uses fewer LLM calls, while emphasizing that implementation quality affects the comparison. [S23]

#### Finding 4

**Claim**

The new material supports a sharper boundary between multi-agent architecture and single-agent workflow graphs: a custom graph can retain explicit routing and guardrails without introducing multiple independent reasoning loops.

**Confidence:** Medium

**Why this confidence level**

The distinction is directly illustrated by an engineering comparison, but it is a practitioner demonstration rather than a controlled study.

**Evidence**

- S23 describes a single-agent state graph with explicit routing among tool use, user questioning, and finalization, plus an eight-call termination guardrail. [S23]
- S23 contrasts this with a swarm in which each agent runs its own reasoning loop and handoffs increase model calls, cost, latency, and possible context drift. [S23]

#### Finding 5

**Claim**

The architecture-selection principle is strengthened: use a single-agent graph or deterministic workflow for simple, well-scoped, sequential tasks; use specialized multi-agent systems when modular roles, heterogeneous tools, or growing task complexity justify coordination overhead.

**Confidence:** High

**Why this confidence level**

The conditional recommendation is consistent with the accumulated evidence, though the boundary at which multi-agent coordination becomes worthwhile remains unquantified.

**Evidence**

- S23 recommends single-agent graphs for simple task-management or data-update workflows where predictability and context coherence matter, and multi-agent or supervisor-style designs as complexity and role specialization grow. [S23]
- S22 motivates multi-agent systems by tool/context scaling, modularity, maintainability, and contributions by separately developed teams. [S22]
- Prior evidence conditions fan-out, pipelines, supervisors, and swarms on dependency structure, specialization, and conflict-resolution needs. [S11] [S12] [S17] [S18]

#### Finding 6

**Claim**

The visual taxonomy should include a baseline branch for deterministic workflows and single-agent graphs, rather than treating all alternatives as multi-agent topologies.

**Confidence:** High

**Why this confidence level**

This follows directly from the new comparison and the established evaluation requirement for strong single-agent or non-agentic baselines.

**Evidence**

- S23 explicitly asks whether an agent is needed at all and describes deterministic rules, forms, or workflows as potentially sufficient; it also compares a single-agent state graph against swarm architecture. [S23]
- S19 and S21 establish that architecture comparisons require strong baselines and task-appropriate outcome, reliability, cost, and latency measures. [S19] [S21]

### Conflicts Found

- S22 says swarm slightly outperformed supervisor in a modified τ-bench setting, while the accumulated evidence finds no general architecture winner and treats earlier swarm-superiority claims as weakly supported. This is a conditional benchmark result, not a landscape-wide contradiction. [S22] [S20] [S1] [S3]
- S23 presents swarm handoffs as typically sequential and costly, whereas S18 and other sources describe swarm or blackboard systems as potentially parallel. The disagreement reflects different swarm implementations—sequential handoff versus shared-state or event-driven execution—and confirms that 'swarm' is not a sufficiently precise execution category by itself. [S23] [S18] [S12]
- S22 attributes supervisor cost to a translation layer, while broader sources describe supervisor overhead as a general coordination cost. The sources do not establish how much overhead is topology-inherent versus caused by a particular implementation. [S22] [S5] [S11] [S14]

### Important Gaps

- What are the primary LangChain benchmark's exact scores, models, prompts, retry policies, token accounting, statistical treatment, and architecture implementations?
- Does the reported swarm advantage persist against an optimized supervisor, a strong single-agent graph, and deterministic workflow baselines when context handling and reasoning budgets are standardized?
- Which aspects of the reported supervisor improvement arise from removing translation layers or improving context management rather than changing the coordination topology?
- How should swarm be subdivided in the taxonomy into sequential handoff, shared-blackboard, event-driven, and genuinely concurrent variants?
- At what task complexity, tool count, or degree of specialization does multi-agent coordination outperform a single-agent graph after latency and cost are included?

**Analysis Duration:** 16.61s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources improve the qualitative architecture comparison and expose implementation-sensitive factors, but they do not close the most important empirical gap: a primary, reproducible comparison of architectures against strong baselines across quality, reliability, cost, and latency. The next search should target the primary LangChain study rather than additional practitioner taxonomies.

**Next Search**

> site:blog.langchain.com benchmarking multi-agent architectures modified Tau-bench single agent swarm supervisor results methodology

---

# Iteration 7

## 1. Search

**Query**

> site:blog.langchain.com benchmarking multi-agent architectures modified Tau-bench single agent swarm supervisor results methodology

**Why this query**

The new sources improve the qualitative architecture comparison and expose implementation-sensitive factors, but they do not close the most important empirical gap: a primary, reproducible comparison of architectures against strong baselines across quality, reliability, cost, and latency. The next search should target the primary LangChain study rather than additional practitioner taxonomies.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S25 — Benchmarking Multi-Agent Architectures**
  URL: https://blog.langchain.com/benchmarking-multi-agent-architectures
- **S26 — Benchmarking Multi-Agent Architectures**
  URL: https://www.blog.langchain.com/benchmarking-multi-agent-architectures
- **S27 — Benchmarking Single Agent Performance**
  URL: https://www.blog.langchain.com/react-agent-benchmarking
- **S28 — Benchmarking Single Agent Performance**
  URL: https://blog.langchain.com/react-agent-benchmarking
- **S29 — Command: A new tool for building multi-agent architectures in LangGraph**
  URL: https://www.blog.langchain.com/command-a-new-tool-for-multi-agent-architectures-in-langgraph

**Search Duration:** 4.66s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new benchmark source provides a more precise operational comparison of single-agent, swarm, and supervisor architectures, but only within a narrow modified τ-bench setting.

**Confidence:** High

**Why this confidence level**

The experimental setup and architecture definitions are stated directly in the primary benchmark blog, although the benchmark is limited in task scope and scale.

**Evidence**

- The experiment uses gpt-4o, the first 100 retail test examples, and up to six unrelated distractor environments, comparing a single tool-calling agent, a handoff-based swarm, and a supervisor delegating to sub-agents. [S25] [S26]
- The distractor domains are intentionally irrelevant to the target tasks, so the benchmark primarily probes context/tool filtering and routing rather than difficult multi-agent collaboration. [S25] [S26]

#### Finding 2

**Claim**

In this benchmark, adding irrelevant tools and instructions harms the single-agent baseline more sharply than the tested multi-agent alternatives.

**Confidence:** Medium

**Why this confidence level**

The finding is replicated across related LangChain experiments, but both are vendor-authored studies and the multi-agent comparison uses only one model, one task domain, and 100 examples.

**Evidence**

- The single-agent baseline reportedly drops sharply once two or more distractor domains are introduced, while it performs slightly better with one distractor domain. [S25] [S26]
- The earlier single-agent study similarly reports that increasing context and tool count degrades ReAct-agent performance, with longer trajectories degrading faster. [S27] [S28]

#### Finding 3

**Claim**

The benchmark reports a slight swarm advantage over supervisor, attributing the difference to supervisor-mediated translation rather than proving a general topology advantage.

**Confidence:** Low

**Why this confidence level**

The result is qualitative and the retrieved content omits numerical scores, variance, complete cost results, and ablations separating topology from context-passing and prompt implementation.

**Evidence**

- The source says swarm slightly outperforms supervisor across the tested conditions because swarm agents can communicate directly with the user, whereas supervisor sub-agents must return information through the supervisor. [S25] [S26]
- The swarm implementation has one active agent at a time, so this result does not establish that decentralized concurrency or parallelism is responsible for the advantage. [S25] [S26]

#### Finding 4

**Claim**

The new evidence strengthens the interpretation that implementation details—especially context translation and handoff design—can dominate apparent architecture effects.

**Confidence:** Medium

**Why this confidence level**

The proposed mechanism is concrete and consistent with prior findings about context drift and translation overhead, but it is not isolated through controlled ablations.

**Evidence**

- LangChain attributes supervisor performance loss to the translation required when sub-agents cannot answer the user directly. [S25] [S26]
- The benchmark uses distinct framework packages for swarm and supervisor, so the comparison includes package- and prompt-level design choices in addition to topology. [S25] [S26]

#### Finding 5

**Claim**

A single-agent graph or deterministic workflow should remain an explicit baseline and design branch in the landscape, particularly when tasks are sequential and context can be kept coherent.

**Confidence:** High

**Why this confidence level**

The need for a strong single-agent baseline is directly supported by the benchmark design and consistent with prior architectural comparisons.

**Evidence**

- The single-agent experiments define a ReAct/tool-calling baseline and show that its behavior changes with tool and context load, providing a necessary comparison point for multi-agent designs. [S25] [S27]
- The broader accumulated evidence already indicates that explicit graphs and deterministic workflows can preserve routing and guardrails without multiple independent reasoning loops. [S23] [S29]

#### Finding 6

**Claim**

Dynamic graph control and handoffs are an infrastructure mechanism that cuts across topology categories rather than constituting a separate architectural family.

**Confidence:** High

**Why this confidence level**

The source directly documents the mechanism and its intended use; the classification implication follows from its ability to implement multiple flow patterns.

**Evidence**

- LangGraph's Command allows a node to update shared state and dynamically select the next node, including nodes in a parent graph, enabling handoffs and hierarchical communication. [S29]
- The source presents event-driven execution, graph representations, edgeless dynamic routing, and handoffs as implementation mechanisms for expressing multi-agent flows. [S29]

#### Finding 7

**Claim**

The taxonomy should distinguish execution topology from control-transfer semantics: a 'swarm' may denote sequential handoffs in one implementation, while other decentralized systems may use shared state, event buses, or concurrent execution.

**Confidence:** High

**Why this confidence level**

The sources directly exhibit the terminology ambiguity and provide contrasting execution models.

**Evidence**

- The LangChain benchmark defines swarm as decentralized handoffs with only one active agent at a time. [S25] [S26]
- Prior sources describe swarm, blackboard, and event-driven systems as potentially shared-state or parallel designs, creating incompatible uses of the swarm label. [S12] [S18]
- LangGraph's dynamic handoff mechanism can be embedded in graph or hierarchical structures, showing that handoff is a control primitive rather than a unique topology. [S29]

### Conflicts Found

- The new benchmark reports swarm slightly outperforming supervisor, but this remains a configuration-specific result and does not resolve prior claims that no architecture has general superiority. The tested swarm is sequential handoff rather than necessarily concurrent decentralized execution. [S25] [S26] [S20] [S22]
- The new benchmark attributes supervisor underperformance to translation overhead, while broader sources frame overhead as a general property of supervisor coordination. The evidence does not determine how much is topology-inherent versus caused by the particular implementation. [S25] [S26] [S22] [S11] [S14]
- The source's claim that the benchmark tests multi-agent scaling is conditional: the tasks require very little coordination, so the experiment mainly tests irrelevant-context filtering and routing rather than decomposition, debate, recovery, or long-horizon collaboration. [S25] [S26]

### Important Gaps

- What are the exact numerical scores, token costs, repetitions, and variance in the full modified τ-bench comparison?
- Does the swarm result persist against an optimized supervisor, a single-agent graph, and deterministic workflow baselines under matched prompts, reasoning budgets, retries, and context policies?
- Which benefits attributed to multi-agent topology arise instead from domain-specific context partitioning or improved tool selection?
- How should the taxonomy subdivide swarm into sequential handoff, shared-blackboard, event-driven, and genuinely concurrent variants?
- Do these architecture effects generalize beyond retail customer support and distractor-tool filtering to coding, web navigation, planning, safety, and stateful environments?
- Which peer-reviewed primary papers provide controlled comparisons of supervisor, pipeline, fan-out, debate, blackboard, mesh, and swarm systems?

**Analysis Duration:** 20.11s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources materially clarify benchmark setup, handoff semantics, and the role of context translation, but they do not close the central evidence gap: independent, controlled architecture comparisons across task types and strong baselines. The landscape report can responsibly present the taxonomy and open problems, but empirical superiority claims remain weak.

**Next Search**

> peer-reviewed primary study controlled comparison multi-agent LLM architectures supervisor pipeline fan-out debate swarm blackboard single-agent baseline cost latency reliability

---

# Iteration 8

## 1. Search

**Query**

> peer-reviewed primary study controlled comparison multi-agent LLM architectures supervisor pipeline fan-out debate swarm blackboard single-agent baseline cost latency reliability

**Why this query**

The new sources materially clarify benchmark setup, handoff semantics, and the role of context translation, but they do not close the central evidence gap: independent, controlled architecture comparisons across task types and strong baselines. The landscape report can responsibly present the taxonomy and open problems, but empirical superiority claims remain weak.

**Results**

5 results retrieved.

1 new unique source added.

### Sources

- **S30 — Agent Orchestration Patterns: Swarm vs Mesh vs Hierarchical**
  URL: https://gurusup.com/blog/agent-orchestration-patterns

**Search Duration:** 3.23s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

S30 reinforces the five-pattern engineering decomposition— orchestrator-worker, swarm, mesh, hierarchical, and pipeline—while treating hybrids as common.

**Confidence:** Medium

**Why this confidence level**

This aligns with S11, S14, S17, and S18, but S30 is another practitioner guide and does not establish a peer-reviewed canonical taxonomy.

**Evidence**

- S30 explicitly names these five patterns and describes them as recurring production coordination models; it states that systems may combine two or more patterns. [S30]

#### Finding 2

**Claim**

S30 further distinguishes mesh from swarm: mesh uses persistent, explicit peer connections, whereas swarm coordination emerges through local decisions, shared state, or handoffs.

**Confidence:** Medium

**Why this confidence level**

The distinction is useful and consistent with the broader topology-versus-control-transfer framing, but the retrieved mesh discussion is incomplete and does not provide formal definitions or empirical comparisons.

**Evidence**

- S30 describes swarm as decentralized coordination through shared state and handoff protocols, and introduces mesh as direct communication among explicitly connected peers. [S30]

#### Finding 3

**Claim**

The taxonomy should represent orchestrator-worker and hierarchical delegation as related but distinct levels of centralized control: hub-and-spoke routing versus tree-structured delegation.

**Confidence:** Medium

**Why this confidence level**

The classification distinction is supported across practitioner sources, but the boundary between a supervisor with nested workers and a hierarchy is not standardized.

**Evidence**

- S30 characterizes orchestrator-worker as a central agent assigning work directly to specialized workers, while its title and pattern list separately identify hierarchical tree-structured delegation. [S30]
- Prior sources separately identify supervisor/orchestrator-worker and multi-tier hierarchies as related production patterns. [S1] [S5] [S18]

#### Finding 4

**Claim**

S30 adds operational failure modes for centralized orchestration: the orchestrator can become a single point of failure, throughput bottleneck, and context-window bottleneck as worker-result volume grows.

**Confidence:** High

**Why this confidence level**

The qualitative mechanisms are consistent across sources, although S30's numerical illustrations and deployment claims are not independently validated.

**Evidence**

- S30 explicitly identifies centralized orchestrator failure and bottleneck risks, including accumulation of task descriptions and worker results in the orchestrator context. [S30]
- Prior sources similarly identify supervisor bottlenecks, context limitations, coordination overhead, and the need for bounded fan-out and budgets. [S5] [S11] [S18] [S22]

#### Finding 5

**Claim**

S30 characterizes swarm systems as suitable for exploration and parallel branch discovery, but its description does not resolve the accumulated ambiguity between genuinely concurrent swarms, shared-blackboard systems, and sequential handoff implementations.

**Confidence:** Medium

**Why this confidence level**

S30 supplies another implementation description but confirms rather than resolves the terminology and execution-model ambiguity.

**Evidence**

- S30 presents swarms as autonomous peers that may explore different search branches in parallel and share discoveries through a blackboard or handoffs. [S30]
- Prior sources define some swarms as one-active-agent sequential handoffs and others as shared-state or potentially concurrent systems. [S12] [S18] [S23] [S25]

#### Finding 6

**Claim**

S30 does not materially strengthen the empirical evidence for architecture superiority, production prevalence, or quantitative trade-offs.

**Confidence:** High

**Why this confidence level**

The source is qualitative engineering guidance and does not supply the missing controlled evidence.

**Evidence**

- S30 asserts that orchestrator-worker is the most widely deployed and mentions support systems with resolution rates above 90%, but provides no sampling, benchmark methodology, primary citations, or architecture-controlled comparison. [S30]
- The accumulated evidence already treats similar practitioner prevalence, performance, and cost claims as weakly supported or configuration-specific. [S1] [S9] [S11] [S14] [S18] [S20] [S25]

#### Finding 7

**Claim**

The strongest landscape synthesis remains a multidimensional taxonomy rather than a canonical list: topology, hierarchy/centralization, execution concurrency, interaction objective, communication/state mechanism, and control or recovery layer should be represented separately.

**Confidence:** High

**Why this confidence level**

The new source reinforces the accumulated multidimensional model without supplying evidence for a single definitive taxonomy.

**Evidence**

- S30 distinguishes centralized orchestrator-worker, hierarchical, decentralized swarm, explicit peer mesh, and sequential pipeline patterns, while discussing shared state, handoffs, observability, and termination. [S30]
- Prior sources explicitly separate topology, adaptivity, objective, workflow structure, communication, memory, protocols, and guardrails. [S8] [S10] [S29]

### Conflicts Found

- S30 calls orchestrator-worker the most widely deployed production pattern and describes it as a default starting point, while the accumulated evidence cautions that production-prevalence claims are practitioner assertions without representative sampling. This supports practitioner consensus, not validated prevalence. [S30] [S1] [S5] [S9] [S18]
- S30 describes swarm agents as exploring many branches in parallel, whereas S12, S23, and the LangChain benchmark in S25 define swarm as sequential handoffs with one active agent at a time. This is an implementation-model disagreement and demonstrates that 'swarm' must be subdivided by concurrency and state-transfer semantics. [S30] [S12] [S23] [S25]
- S30 presents swarm, mesh, and orchestrator-worker as distinct top-level patterns, while S8 and S10 use broader centralized/decentralized/hierarchical axes. The difference is classification granularity rather than a demonstrated substantive contradiction. [S30] [S8] [S10]

### Important Gaps

- What formal operational definition separates mesh, swarm, blackboard, event-driven, and sequential handoff systems?
- Does S30's claimed production prevalence and customer-support performance have identifiable primary evidence, and are the claims representative?
- Under controlled benchmarks, do mesh or shared-blackboard architectures outperform supervisor, fan-out, pipeline, or single-agent graph baselines?
- Which reported swarm benefits arise from concurrency and decentralized topology versus context partitioning, handoff design, or implementation-specific prompts?
- What are the quantitative scaling limits of orchestrator context, routing latency, and worker-result aggregation across task sizes?

**Analysis Duration:** 17.18s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

S30 mainly repeats and elaborates practitioner taxonomy. It does not address the most important remaining gap: peer-reviewed or primary controlled comparisons across architectures against strong single-agent and deterministic workflow baselines. Another search should target primary comparative studies rather than additional pattern guides.

**Next Search**

> peer-reviewed primary study controlled comparison multi-agent LLM architectures supervisor pipeline fan-out debate swarm blackboard mesh single-agent baseline benchmark cost latency reliability

---

# Iteration 9

## 1. Search

**Query**

> peer-reviewed primary study controlled comparison multi-agent LLM architectures supervisor pipeline fan-out debate swarm blackboard mesh single-agent baseline benchmark cost latency reliability

**Why this query**

S30 mainly repeats and elaborates practitioner taxonomy. It does not address the most important remaining gap: peer-reviewed or primary controlled comparisons across architectures against strong single-agent and deterministic workflow baselines. Another search should target primary comparative studies rather than additional pattern guides.

**Results**

5 results retrieved.

2 new unique sources added.

### Sources

- **S31 — Agent Orchestration Patterns: Swarm vs Mesh vs Hierarchical**
  URL: https://www.gurusup.com/blog/agent-orchestration-patterns
- **S32 — Benchmarking Multi-Agent LLM Architectures for Financial Document Processing: A Comparative Study of Orchestration Patterns, Cost-Accuracy Tradeoffs and Production Scaling Strategies**
  URL: https://www.catalyzex.com/paper/benchmarking-multi-agent-llm-architectures

**Search Duration:** 4.53s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources reinforce the multidimensional taxonomy: orchestrator-worker, swarm, mesh, hierarchical, and pipeline are recurring coordination patterns, but they should be modeled as combinations of topology, delegation structure, concurrency, and communication/state semantics rather than as mutually exclusive categories.

**Confidence:** Medium

**Why this confidence level**

S31 is a practitioner guide that reinforces an already convergent taxonomy, but it does not establish a peer-reviewed canonical classification.

**Evidence**

- S31 presents five recurring patterns—centralized orchestrator-worker, decentralized swarm, peer-to-peer mesh, tree-structured hierarchy, and sequential pipeline—and notes that production systems may combine them as hybrids. [S31]
- The accumulated evidence already distinguishes topology, workflow structure, concurrency, communication, shared state, and control-transfer mechanisms as separate dimensions. [S8] [S10] [S29] [S30]

#### Finding 2

**Claim**

Orchestrator-worker systems have a clear operational advantage in centralized traceability and routing, but their orchestrator creates potential single points of failure, throughput bottlenecks, and context-aggregation limits.

**Confidence:** High

**Why this confidence level**

The qualitative mechanisms are consistent across multiple sources, although the numerical examples in S31 are illustrative rather than controlled measurements.

**Evidence**

- S31 describes the orchestrator as maintaining global state, assigning work, recovering from errors, and aggregating worker results; it identifies centralized failure, throughput, and context-window bottlenecks as failure modes. [S31]
- Prior sources independently identify supervisor bottlenecks, context limitations, coordination overhead, bounded fan-out requirements, and the need for observability and fallbacks. [S5] [S11] [S18] [S30]

#### Finding 3

**Claim**

Swarm terminology remains underspecified: S31 describes autonomous peers with shared blackboards and potentially parallel exploration, while other sources describe swarms as sequential handoff systems with one active agent at a time.

**Confidence:** High

**Why this confidence level**

The sources directly document incompatible execution interpretations, establishing a taxonomy and terminology problem rather than a performance conclusion.

**Evidence**

- S31 defines swarm around decentralized local decisions, shared state, blackboards, handoffs, and simultaneous exploration. [S31]
- Prior benchmark and engineering sources define some swarm implementations as sequential handoffs, while others describe shared-state or concurrent variants. [S12] [S18] [S23] [S25] [S30]

#### Finding 4

**Claim**

S32 reports a potentially important controlled benchmark of orchestration patterns for financial-document extraction, including sequential pipeline, parallel fan-out/merge, hierarchical supervisor-worker, and reflexive self-correction.

**Confidence:** Medium

**Why this confidence level**

The source presents a specific benchmark design with relevant baselines and metrics, but the retrieved content is only an abstract-like listing and does not establish authorship, peer-review status, implementation details, statistical treatment, or code reproducibility.

**Evidence**

- The abstract states that four architectures were compared across five frontier and open-weight models on 10,000 SEC filings and evaluated using field-level F1, document accuracy, latency, cost, and token efficiency. [S32]

#### Finding 5

**Claim**

According to S32, reflexive self-correction achieved the highest reported extraction F1 but at substantially higher cost, while hierarchical supervisor-worker offered a more favorable cost-accuracy trade-off; hybrid routing, caching, and retries reportedly recovered much of the accuracy gain at near-baseline cost.

**Confidence:** Low

**Why this confidence level**

These are precise but currently single-source claims. The excerpt lacks per-model results, confidence intervals, baseline quality, cost accounting, ablations, and independently verifiable paper or code details.

**Evidence**

- S32 reports F1 0.943 for reflexive architectures at 2.3× sequential-baseline cost, F1 0.921 for hierarchical architectures at 1.4× cost, and hybrid configurations recovering 89% of reflexive gains at 1.15× baseline cost. [S32]

#### Finding 6

**Claim**

S32, if validated, would extend the empirical landscape beyond customer-service tool-use benchmarks by showing architecture-dependent cost-accuracy trade-offs in large-scale, structured financial-document extraction.

**Confidence:** Low

**Why this confidence level**

The domain and proposed evaluation axes are materially different from prior benchmarks, but the result's reliability and publication provenance remain unresolved.

**Evidence**

- S32 uses SEC filings, 25 extraction field types, multiple model families, and production-scale document throughput rather than a customer-service simulator. [S32]

### Conflicts Found

- S31 describes swarm as capable of simultaneous exploration through shared blackboards, whereas S12, S23, and S25 describe swarm as sequential handoffs with one active agent. This reinforces that swarm must be subdivided by concurrency and state-transfer semantics. [S31] [S12] [S23] [S25]
- S31 asserts that orchestrator-worker is the most widely deployed production pattern and cites support systems with resolution rates above 90%, while the accumulated evidence treats such prevalence and performance claims as practitioner assertions without representative sampling or controlled validation. [S31] [S1] [S9] [S18] [S30]
- S32 reports a reflexive architecture as the quality leader and hierarchical architecture as the cost-accuracy leader in financial extraction, whereas prior evidence finds no architecture-wide winner. This is compatible only as a domain- and configuration-specific result until independently verified. [S32] [S1] [S3] [S20] [S25]

### Important Gaps

- Is S32 a genuine peer-reviewed paper or a provisional/metadata listing, and are its paper, authors, datasets, implementations, and code independently verifiable?
- What are the full per-model and per-architecture results in S32, including variance, confidence intervals, error categories, latency distributions, and exact monetary/token cost accounting?
- Do S32's reported reflexive and hierarchical trade-offs generalize beyond financial-document extraction and beyond the five tested models?
- Are the reported hybrid gains caused by orchestration topology, semantic caching, model routing, adaptive retries, or their interaction?
- Does the claimed scaling behavior from 1K to 100K documents per day measure real system throughput or extrapolated capacity planning?
- The central gap remains controlled, reproducible comparisons across pipeline, fan-out, supervisor, debate, blackboard, mesh, and swarm against strong single-agent graph and deterministic baselines.

**Analysis Duration:** 18.41s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

S32 potentially supplies the strongest empirical evidence yet, but its precise quantitative claims are not sufficiently documented in the retrieved content. Verifying its provenance and methodology would materially improve the landscape report and determine whether its results can be used as primary comparative evidence.

**Next Search**

> "Benchmarking Multi-Agent LLM Architectures for Financial Document Processing" paper code authors

---

# Iteration 10

## 1. Search

**Query**

> "Benchmarking Multi-Agent LLM Architectures for Financial Document Processing" paper code authors

**Why this query**

S32 potentially supplies the strongest empirical evidence yet, but its precise quantitative claims are not sufficiently documented in the retrieved content. Verifying its provenance and methodology would materially improve the landscape report and determine whether its results can be used as primary comparative evidence.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S33 — Benchmarking Multi-Agent LLM Architectures for Financial ...**
  URL: https://chatpaper.com/chatpaper/paper/256194
- **S34 — [2603.22651] Benchmarking Multi-Agent LLM Architectures for Financial Document Processing: A Comparative Study of Orchestration Patterns, Cost-Accuracy Tradeoffs and Production Scaling Strategies**
  URL: https://arxiv.org/abs/2603.22651
- **S35 — Benchmarking Multi-Agent LLM Architectures for Financial ... - GitHub**
  URL: https://github.com/KatsuyaITO/indx-autoresearch-financeaiready/issues/913
- **S36 — Siddhant Kulkarni**
  URL: https://scholar.google.com/citations?user=JoO-FNUAAAAJ&hl=en
- **S37 — Multi-Agent Finance Workflows Need Cost Curves, Not More ...**
  URL: https://swarmsignal.net/multi-agent-finance-workflows-need-cost-curves

**Search Duration:** 7.66s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

S34 confirms that the financial-document architecture benchmark is an identifiable arXiv preprint, rather than only an unattributed metadata record.

**Confidence:** High

**Why this confidence level**

The arXiv landing page directly establishes the preprint identifier and title, resolving the provenance question at the level of existence and bibliographic identity.

**Evidence**

- The arXiv page identifies the paper as arXiv:2603.22651, with a title matching the previously reported benchmark of multi-agent orchestration patterns, cost-accuracy trade-offs, and production scaling. [S34]

#### Finding 2

**Claim**

The new sources do not yet validate the benchmark's methods, quantitative findings, reproducibility, or peer-review status.

**Confidence:** High

**Why this confidence level**

All available excerpts remain incomplete or secondary; none supplies the missing full paper content or independently reproducible results.

**Evidence**

- S34 contains bibliographic metadata and access/navigation elements but no abstract, experimental setup, results, authors, code, or statistical analysis in the retrieved content. [S34]
- S33 only states that four orchestration architectures are proposed, without naming the complete methods or reporting results. [S33]
- S35 contains a broad promotional statement rather than a paper text, methodology, or independently verifiable benchmark results. [S35]
- S36 provides author-profile metadata and no substantive benchmark evidence; S37 is commentary about the topic rather than primary experimental reporting. [S36] [S37]

#### Finding 3

**Claim**

S33 provides weak corroboration that the benchmark concerns four multi-agent orchestration architectures for financial document processing, but it does not materially extend the taxonomy or empirical comparison.

**Confidence:** Low

**Why this confidence level**

The statement is direct but extremely incomplete and comes from a secondary paper-summary page.

**Evidence**

- The ChatPaper listing describes a systematic benchmark comparing four multi-agent orchestration architectures for financial document processing, but the excerpt ends after introducing the methods. [S33]

### Conflicts Found

- S33 says the benchmark compares four architectures, while prior S32 reported specific architecture categories and numerical results. The new material does not provide enough detail to determine whether the four architectures match S32's categories or whether the apparent discrepancy reflects omitted methods. [S33] [S32]
- S35 describes the work as establishing evaluation and orchestration standards, but S34, S33, and the accumulated evidence provide no basis for treating it as an established standard; the claim appears promotional or premature rather than empirically demonstrated. [S35] [S34] [S33]

### Important Gaps

- What are the four architectures named in the full paper, and do they correspond to the sequential, fan-out, hierarchical, and reflexive categories reported in S32?
- What are the complete per-model and per-architecture results, including variance, confidence intervals, error categories, latency, and exact token or monetary cost accounting?
- Is arXiv:2603.22651 peer-reviewed, and are its implementations, datasets, prompts, and code independently verifiable?
- Do the reported cost-accuracy and production-scaling findings generalize beyond financial-document extraction?

**Analysis Duration:** 10.95s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The runner reached the maximum research iteration budget. Analyzer assessment: The new evidence resolves the paper's bibliographic identity but leaves the most important empirical gap unresolved: no full methods or results are available. A focused retrieval of the paper's full text or abstract is likely to materially improve the landscape report, particularly by validating or revising S32's precise claims.

**Stop Reason:** max_iterations

---

# Final Research Decision

**Research Stopped Because**

The runner reached the maximum research iteration budget.

**Stop Reason:** max_iterations

**Searches Performed:** 10

**Unique Sources:** 37

**Remaining Uncertainty**

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

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 10 | 43.66s |
| OpenAI Analysis | 10 | 180.38s |
| Report Generation | 1 | 41.64s |
| Total Run | — | 265.69s |
