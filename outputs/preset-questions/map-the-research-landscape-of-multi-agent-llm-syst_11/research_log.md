# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are.

**Status:** Completed

**Stop Reason:** sufficient_evidence

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 2 / 10

**Unique Sources:** 10

**OpenAI Calls:** 3

**Tavily Calls:** 2

**Started:** 2026-09-01T06:28:18-04:00

**Ended:** 2026-09-01T06:29:28-04:00

**Total Runtime:** 70.29s

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
- **S2 — Multi-agent LLMs in 2026 [+frameworks] - SuperAnnotate**
  URL: https://www.superannotate.com/blog/multi-agent-llms
- **S3 — LLM-Enabled Multi-Agent Systems: Empirical Evaluation and Insights into Emerging Design Patterns & Paradigms**
  URL: https://arxiv.org/html/2601.03328v1
- **S4 — LLM Agent Orchestration Patterns: Architectural ...**
  URL: https://www.c-sharpcorner.com/article/llm-agent-orchestration-patterns-architectural-frameworks-for-managing-complex
- **S5 — Architectures for Multi-Agent Systems**
  URL: https://galileo.ai/blog/architectures-for-multi-agent-systems

**Search Duration:** 2.77s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The landscape can be organized along at least two complementary dimensions: agent relationship (single-agent, collaborative, competitive/adversarial) and control topology (centralized, decentralized, specialized, or hybrid).

**Confidence:** Medium

**Why this confidence level**

The categorization is consistent across multiple sources, but the retrieved taxonomy sources are primarily practitioner articles rather than established systematic reviews.

**Evidence**

- One taxonomy groups patterns into single-agent, collaborative multi-agent, competitive multi-agent, and orchestration-topology quadrants. [S1]
- An orchestration-focused source distinguishes centralized, decentralized, specialized, and hybrid architectures. [S4]
- Another architecture overview contrasts centralized orchestrators with decentralized peer communication and discusses their differing information-flow and failure properties. [S5]

#### Finding 2

**Claim**

A useful visual design graph should treat multi-agent architectures as compositions of recurring patterns rather than mutually exclusive categories.

**Confidence:** Medium

**Why this confidence level**

The compositional principle is directly described, but the evidence does not establish how prevalent each composition is across the research field.

**Evidence**

- The taxonomy source states that production systems commonly compose two or three patterns from different quadrants, including hierarchical and graph topologies combined with critique or planning. [S1]
- The empirical paper describes systems as configured specialist agents arranged in networks that hand off successive parts of a process. [S3]
- The travel-planning example uses specialized agents coordinated by a manager, illustrating specialization plus centralized orchestration. [S2]

#### Finding 3

**Claim**

The principal collaborative patterns are plan-and-execute, supervisor-worker/hierarchical delegation, and graph or workflow-based arrangements.

**Confidence:** Medium

**Why this confidence level**

The patterns recur across sources, although the retrieved material provides limited independent experimental comparison among them.

**Evidence**

- Plan-and-execute separates planning from execution; supervisor-worker decomposes a task and routes subtasks to specialized workers. [S1]
- The empirical paper formalizes orchestration, communication mechanisms, and control-flow strategies, and describes specialist agents handing off work through a network. [S3]
- The centralized orchestrator pattern maintains global state, allocates tasks, monitors progress, and synthesizes worker results; the source also references map-reduce and graph implementation support. [S5]

#### Finding 4

**Claim**

Competitive or quality-control patterns include multi-agent debate and verifier-critic loops, which use disagreement or critique rather than parallel specialization as the main mechanism.

**Confidence:** Medium

**Why this confidence level**

The architectural distinction is clear, but claims about reliability improvements are not fully substantiated by the excerpts with controlled comparative results.

**Evidence**

- The taxonomy defines debate as agents arguing positions before a judge or synthesizer, and verifier-critic as generation followed by rubric-based critique and revision. [S1]
- The overview claims that agents can check one another's work to improve reliability, particularly for complex or high-stakes tasks. [S2]

#### Finding 5

**Claim**

Multi-agent systems are motivated by task decomposition, specialization, parallelism, distributed context, and multiple perspectives, but these benefits introduce coordination and resource costs.

**Confidence:** High

**Why this confidence level**

The benefit/cost trade-off is directly and consistently described across several sources, even though its quantitative magnitude remains uncertain.

**Evidence**

- Sources describe dividing complex tasks among specialized agents, parallel processing, and separate context windows as advantages over a single agent. [S2] [S3] [S5]
- The taxonomy identifies coordination overhead, brittle plans, supervisor drift, unsurfaced worker conflicts, and debate or critique costs as failure modes. [S1]
- The architecture overview characterizes centralized systems as easier to debug but vulnerable to orchestrator bottlenecks and single points of failure, while decentralized systems improve local resilience at the cost of global consistency. [S5]

#### Finding 6

**Claim**

The central research problem is production reliability: LLM behavioral variability, semantic drift, incomplete or lossy inter-agent communication, scalability, token cost, and governance.

**Confidence:** High

**Why this confidence level**

These limitations are convergent across sources and are also framed as explicit limitations or failure modes rather than inferred benefits.

**Evidence**

- The empirical paper reports variability in LLM behavior as a barrier to moving from prototypes to production and explicitly identifies reliability, scalability, and governance as research directions. [S3]
- The orchestration study discusses contextual drift, semantic misinterpretation, protocol-related semantic loss, and escalating token consumption in agent networks. [S4]
- The architecture overview identifies centralized bottlenecks and single points of failure, while decentralized designs risk global inconsistency and increasingly difficult coordination. [S5]
- The taxonomy lists repeated mistakes, plan brittleness, supervisor drift, hidden subtask conflicts, premature debate convergence, judge bias, and generator-critic collusion. [S1]

#### Finding 7

**Claim**

The field has evidence of practical prototyping across domains, but the retrieved evidence is insufficient to conclude that multi-agent systems generally outperform well-designed single-agent baselines or to quantify the claimed production gains.

**Confidence:** High

**Why this confidence level**

The distinction between demonstrated pilots and unproven general superiority follows directly from the reported evidence and its methodological limitations.

**Evidence**

- The empirical paper reports containerized pilots in telecommunications security, heritage management, and utilities customer service, with rapid prototype and pilot delivery, but also notes production-maturity limitations. [S3]
- Practitioner sources make broad claims about improved accuracy, efficiency, work-completion time, token cost, and ROI, but the excerpts do not provide enough methodological detail, baseline definitions, or independently verifiable comparisons. [S2] [S4] [S5]
- The taxonomy explicitly recommends establishing a single-agent baseline and escalating only when a measured failure mode is decomposable. [S1]

### Conflicts Found

- The sources differ in how they define the top-level taxonomy. S1 uses four quadrants combining relationship type and topology, S4 uses four orchestration categories, and S5 emphasizes centralized versus decentralized organization. These are better understood as different abstraction levels than as directly competing classifications. [S1] [S4] [S5]
- S1 recommends hierarchical or graph topologies as the practical defaults and claims swarms rarely outperform them, whereas S5 presents centralized and decentralized designs as context-dependent trade-offs and highlights resilience advantages of decentralization. The retrieved evidence does not resolve when decentralized or swarm designs win. [S1] [S5]
- S2 presents multi-agent systems as generally better for complex tasks and claims improved accuracy and efficiency, while S1 cautions that teams often incur coordination overhead before a single-agent quality ceiling is reached. The sources do not provide a common benchmark or baseline to reconcile these conditional claims. [S1] [S2]
- S4 reports large operational improvements and ROI claims, but S3 emphasizes behavioral variability and the difficulty of achieving production maturity. The evidence does not show whether S4's reported gains generalize beyond its study setting. [S3] [S4]

### Important Gaps

- What is the agreed scholarly taxonomy of multi-agent LLM systems, and how should relationship type, topology, communication protocol, memory, and control flow be represented without conflating them?
- Under what task, agent-count, model-diversity, and failure-mode conditions does multi-agent coordination outperform a strong single-agent baseline?
- Which communication mechanisms—natural-language messages, structured schemas, shared state, blackboards, or direct peer-to-peer protocols—best preserve semantics while controlling context and token cost?
- How should systems evaluate emergent failure modes such as correlated hallucinations, collusion, premature consensus, supervisor drift, cascading errors, and loss of information during handoffs?
- What benchmarks measure end-to-end utility together with latency, token cost, reliability, resilience to agent or tool failure, and governance requirements?
- How do centralized, decentralized, hierarchical, graph, swarm, and hybrid systems scale as the number of agents and dependencies increases?
- What forms of human oversight, auditability, access control, provenance, and intervention are required for high-stakes multi-agent deployments?
- The sources provide limited evidence about learning or adaptation over time, agent memory interoperability, model heterogeneity, and security threats such as prompt injection propagating between agents.

**Analysis Duration:** 26.93s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The sources are sufficient to draft a provisional taxonomy and design graph, but the research landscape remains weakly grounded in systematic academic evidence. The most important gap is comparative evaluation: no retrieved source establishes when particular architectures outperform strong single-agent or alternative multi-agent baselines, especially under matched cost and reliability constraints.

**Next Search**

> systematic survey benchmark comparative evaluation LLM multi-agent architectures centralized decentralized hierarchical debate communication protocols

---

# Iteration 2

## 1. Search

**Query**

> systematic survey benchmark comparative evaluation LLM multi-agent architectures centralized decentralized hierarchical debate communication protocols

**Why this query**

The sources are sufficient to draft a provisional taxonomy and design graph, but the research landscape remains weakly grounded in systematic academic evidence. The most important gap is comparative evaluation: no retrieved source establishes when particular architectures outperform strong single-agent or alternative multi-agent baselines, especially under matched cost and reliability constraints.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S6 — LLM-Based Multi-Agent Orchestration: A Survey of ...**
  URL: https://www.mdpi.com/1999-5903/18/6/326
- **S7 — LLM-Powered Multi-Agent Systems: A Survey of ...**
  URL: https://dl.acm.org/doi/10.1145/3806262.3806263
- **S8 — Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems**
  URL: https://arxiv.org/html/2502.14321v2
- **S9 — ProtocolBench: Which LLM MultiAgent Protocol to Choose?**
  URL: https://arxiv.org/pdf/2510.17149
- **S10 — Evaluation and Benchmarking of LLM Agents: A Survey - arXiv**
  URL: https://arxiv.org/html/2507.21504v1

**Search Duration:** 3.17s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

A communication-centric taxonomy complements topology- and relationship-based taxonomies by separating system-level communication from internal agent communication.

**Confidence:** High

**Why this confidence level**

S8 explicitly presents the framework and directly addresses a limitation in architecture-only taxonomies; it is also consistent with the prior multi-dimensional findings.

**Evidence**

- S8 proposes a two-level framework: system-level communication covers architecture, goals, and protocols; system-internal communication covers strategies, paradigms, communication objects, and exchanged content. [S8]
- Existing findings identify relationship type and control topology as complementary dimensions, rather than a single mutually exclusive classification. [S1] [S4] [S5]

#### Finding 2

**Claim**

Communication protocols should be represented as a distinct architectural layer in the design graph, alongside topology, control flow, and agent specialization.

**Confidence:** High

**Why this confidence level**

Both sources directly distinguish communication protocols from broader system architecture and show why this separation matters empirically.

**Evidence**

- S8 defines LLM-based multi-agent systems as protocol-constrained systems organized around communication goals and architectures, with multiple communication strategies, paradigms, objects, and content types. [S8]
- S9 treats protocol choice as an independently variable factor and evaluates protocols while holding models, prompts, hardware, and other non-protocol factors constant. [S9]

#### Finding 3

**Claim**

Protocol selection creates scenario-dependent trade-offs rather than a universally dominant communication mechanism.

**Confidence:** Medium

**Why this confidence level**

The reported benchmark results are concrete, but they come from one benchmark and the retrieved material does not establish broad generalization across models, tasks, or implementations.

**Evidence**

- S9 reports that protocols differ in task success, latency, message or byte overhead, and robustness under failures; completion time varied by up to 36.5% across protocols in the Streaming Queue scenario. [S9]
- S9 reports different protocols performing best for different scenarios, including A2A for selected GAIA and failure-resilience results and ACP for Streaming Queue latency. [S9]
- S9's ProtocolRouter improves targeted metrics under explicit constraints but is described as avoiding blanket dominance over every fixed-protocol baseline. [S9]

#### Finding 4

**Claim**

The open-problem landscape can be organized around communication efficiency, security, benchmarking, scalability, and reliability under dynamic interaction and failure.

**Confidence:** High

**Why this confidence level**

The challenges recur across the new survey and benchmark sources and align with the previously accumulated evidence.

**Evidence**

- S8 identifies communication efficiency, security vulnerabilities, inadequate benchmarking, and scalability as major challenges. [S8]
- S9 operationalizes several of these gaps through metrics for task utility, latency, communication overhead, and failure-time robustness. [S9]
- S10 argues that agent evaluation must cover behavior, capabilities, reliability, safety and alignment, while also varying interaction mode, data, metrics, tooling, and evaluation context. [S10]
- Prior findings add semantic drift, lossy handoffs, token cost, governance, cascading errors, supervisor drift, and correlated or collusive failure modes. [S1] [S3] [S4] [S5]

#### Finding 5

**Claim**

Evaluation of multi-agent LLM systems should be multi-dimensional and end-to-end, not limited to final answer quality.

**Confidence:** High

**Why this confidence level**

The evaluation dimensions are explicitly specified by two sources, while the baseline limitation is directly supported by prior evidence.

**Evidence**

- S10 separates evaluation objectives—behavior, capabilities, reliability, and safety—from evaluation processes such as interaction mode, datasets, metrics, tooling, and context. [S10]
- S9 demonstrates a protocol-level evaluation using task success or quality, latency or throughput, message or byte overhead, and robustness under failures. [S9]
- Prior findings note that existing evidence is insufficient to establish general superiority over strong single-agent baselines. [S1] [S2] [S3] [S4] [S5]

#### Finding 6

**Claim**

The most defensible visual taxonomy is layered and compositional: agent roles and relationships feed into control topology and workflow, which are implemented through communication protocols and evaluated under operational constraints.

**Confidence:** High

**Why this confidence level**

This is a synthesis supported by convergent taxonomic, empirical, and evaluation evidence; it avoids treating categories as mutually exclusive.

**Evidence**

- Prior evidence describes specialization, hierarchical delegation, plan-and-execute, graph workflows, debate, verifier-critic loops, centralized orchestration, decentralized peers, and hybrids as recurring patterns that can be composed. [S1] [S2] [S3] [S4] [S5]
- S8 adds communication goals, protocols, strategies, paradigms, objects, and content as a separate analytical layer. [S8]
- S9 shows that protocol choice affects the operational behavior of otherwise comparable multi-agent systems. [S9]
- S10 supplies an evaluation layer spanning quality, capability, reliability, safety, interaction, metrics, and deployment context. [S10]

### Conflicts Found

- S8 criticizes architecture- or application-centered surveys for underrepresenting communication, whereas prior sources use topology and relationship type as primary organizing dimensions. These are not direct contradictions: they emphasize different layers of the same design space. [S1] [S4] [S5] [S8]
- S9 presents measurable scenario-dependent protocol differences and gains from protocol routing, but this does not resolve the earlier disagreement about when centralized, decentralized, hierarchical, graph, or swarm topologies are preferable. Protocol performance and topology performance remain distinct unresolved questions. [S1] [S5] [S9]
- S10 advocates holistic evaluation, while some practitioner-oriented prior sources make broad accuracy, efficiency, or ROI claims without comparable multi-dimensional baselines. The evidence supports the need for broader evaluation but does not validate those broad claims. [S2] [S4] [S5] [S10]

### Important Gaps

- Whether the communication-centric framework in S8 will become a broadly adopted scholarly taxonomy rather than one useful proposal among several.
- How communication protocols interact with topology, agent count, model heterogeneity, memory design, and control flow; S9 isolates protocol effects but does not answer these interaction effects comprehensively.
- Whether protocol benchmark results generalize across independent implementations, models, domains, scales, and long-horizon deployments.
- What structured representations, shared-state mechanisms, or message compression methods best preserve semantics while reducing token and latency costs.
- How to evaluate multi-agent-specific failures such as correlated hallucinations, collusion, premature consensus, cascading errors, supervisor drift, and protocol-mediated security propagation.
- How to compare multi-agent systems fairly against strong single-agent, tool-augmented, and conventional workflow baselines using the dimensions in S10.
- How governance, access control, provenance, auditability, human intervention, and prompt-injection containment should be integrated into the architecture and benchmark layers.

**Analysis Duration:** 16.93s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The new sources materially strengthen the landscape map by adding a communication layer and concrete protocol-level evaluation, while S10 supplies a broader evaluation framework. The remaining gaps are substantive open research problems rather than missing basic landscape coverage. S6 and S7 provide titles and landing-page material but no usable substantive evidence, so they should not be relied upon; however, the accessible S8-S10 sources are sufficient to answer the original mapping request responsibly.

**Stop Reason:** sufficient_evidence

---

# Final Research Decision

**Research Stopped Because**

The analyzer determined that the important parts of the question could be answered responsibly.

**Stop Reason:** sufficient_evidence

**Searches Performed:** 2

**Unique Sources:** 10

**Remaining Uncertainty**

- Determine when multi-agent coordination outperforms a strong single-agent, tool-augmented, or conventional workflow baseline under matched quality, cost, latency, and reliability constraints.
- Develop a common taxonomy that represents roles, relationships, topology, control flow, memory, communication protocols, and governance without conflating these layers.
- Measure interactions among topology, protocol, agent count, model heterogeneity, memory design, and task structure.
- Develop structured messaging, shared-state, compression, and provenance mechanisms that preserve semantics while reducing token and latency costs.
- Create benchmarks for correlated hallucinations, cascading errors, collusion, premature consensus, supervisor drift, prompt-injection propagation, and agent or tool failures.
- Establish realistic long-horizon and open-world evaluations covering task utility, capability, reliability, safety, security, latency, throughput, communication overhead, and recovery.
- Clarify governance requirements for access control, auditability, provenance, human intervention, compliance, and containment of unsafe inter-agent behavior.
- Test whether reported protocol and orchestration results generalize across independent implementations, domains, models, scales, and production deployments.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 2 | 5.94s |
| OpenAI Analysis | 2 | 43.85s |
| Report Generation | 1 | 20.50s |
| Total Run | — | 70.29s |
