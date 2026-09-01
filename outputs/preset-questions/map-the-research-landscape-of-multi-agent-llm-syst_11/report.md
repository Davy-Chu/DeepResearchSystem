# Research Report

## Research Question

Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are.

## Summary

The research landscape is best represented as a layered, compositional design space rather than a single taxonomy. Agent roles and relationships determine whether systems are specialized, collaborative, or adversarial; control topology determines how work and state are routed; communication protocols determine how agents exchange information; and evaluation determines whether the resulting system is useful, efficient, reliable, safe, and governable. The evidence supports a provisional map of recurring patterns, but does not establish a universally superior architecture or protocol.

## Findings

### Finding 1

**Claim**

A multi-dimensional taxonomy is more appropriate than a mutually exclusive list of architectures.

**Confidence:** High

**Why this confidence level**

The distinction is explicit across architecture and communication-focused sources and is reinforced by the compositional nature of the described systems.

**Evidence**

- Existing classifications organize systems by agent relationship, orchestration topology, and communication structure. These dimensions describe different aspects of the same system rather than competing categories. [S1] [S4] [S5] [S8]

### Finding 2

**Claim**

The major architectural patterns include single-agent loops, plan-and-execute, hierarchical supervisor-worker systems, graph or workflow systems, decentralized or swarm-like systems, multi-agent debate, and verifier-critic loops.

**Confidence:** Medium

**Why this confidence level**

The patterns recur across the retrieved sources, but the sources do not establish a definitive scholarly standard or exhaustive enumeration.

**Evidence**

- The taxonomy identifies ReAct, Reflexion, plan-and-execute, supervisor-worker, multi-agent debate, and verifier-critic as recurring patterns; other sources add centralized, decentralized, specialized, hybrid, and graph-based orchestration arrangements. [S1] [S3] [S4] [S5]
- Specialized agents coordinated by a manager and agents handing off successive process stages illustrate how these patterns appear in applied systems. [S2] [S3]

### Finding 3

**Claim**

The design space is compositional: a system may combine specialization, hierarchical orchestration, graph control flow, planning, and critique.

**Confidence:** High

**Why this confidence level**

Composition is directly described in multiple sources and is central to the proposed layered design graph.

**Evidence**

- Production systems are described as compositions of patterns from different quadrants, while empirical and applied examples combine specialist agents with managerial coordination and network handoffs. [S1] [S2] [S3]

### Finding 4

**Claim**

Centralized and hierarchical systems provide global coordination and clearer accountability, but create bottlenecks and single points of failure.

**Confidence:** High

**Why this confidence level**

These trade-offs are directly stated in the architecture descriptions and failure-mode analyses.

**Evidence**

- Centralized orchestrators allocate tasks, maintain global state, monitor workers, and synthesize results, making behavior easier to trace and debug; the orchestrator can also limit throughput and halt the system if it fails. [S5]
- Supervisor-worker systems introduce coordination overhead, supervisor drift, and the risk that conflicts among subtasks are not surfaced. [S1]

### Finding 5

**Claim**

Decentralized or peer-to-peer systems can improve local resilience and reduce dependence on a central hub, but make global consistency and coordination more difficult.

**Confidence:** High

**Why this confidence level**

The sources consistently present decentralization as a resilience-versus-coordination trade-off.

**Evidence**

- The architecture comparison contrasts centralized information flow and bottlenecks with decentralized peer communication, which supports local decisions but risks inconsistency and harder coordination. [S4] [S5]

### Finding 6

**Claim**

Communication protocols are a distinct architectural layer whose choice affects system behavior.

**Confidence:** High

**Why this confidence level**

Both sources explicitly distinguish communication mechanisms from topology and show their independent operational significance.

**Evidence**

- A communication-centric survey separates system-level architecture and protocols from internal communication strategies, paradigms, objects, and content. [S8]
- ProtocolBench evaluates protocol choice while controlling models, prompts, hardware, and other factors, demonstrating that protocols can be studied independently from broader topology. [S9]

### Finding 7

**Claim**

No communication protocol is uniformly best; protocol performance is scenario-dependent across utility, latency, overhead, and failure resilience.

**Confidence:** Medium

**Why this confidence level**

The benchmark provides concrete comparative evidence, but the retrieved material does not establish generalization across all models, domains, scales, or implementations.

**Evidence**

- ProtocolBench reports differences across task success or quality, end-to-end latency, message or byte overhead, and robustness under failures. Different protocols perform best in different scenarios, and completion time varied substantially in the reported Streaming Queue experiment. [S9]

### Finding 8

**Claim**

The principal motivations for multi-agent systems are decomposition, specialization, parallelism, distributed context, and access to multiple perspectives.

**Confidence:** High

**Why this confidence level**

These motivations are consistently described across applied, empirical, and survey sources.

**Evidence**

- Sources describe assigning subtasks to specialized agents, processing independent work in parallel, distributing context across agents, and using debate or critique to introduce alternative perspectives. [S2] [S3] [S5] [S8]

### Finding 9

**Claim**

The main research and deployment risks are semantic drift, lossy handoffs, correlated errors, coordination overhead, token and latency costs, scalability limits, security vulnerabilities, and governance failures.

**Confidence:** High

**Why this confidence level**

The risks recur across sources and are presented as explicit limitations or open challenges.

**Evidence**

- Sources identify contextual drift, protocol-related semantic loss, escalating token consumption, supervisor drift, brittle plans, hidden subtask conflicts, premature consensus, judge bias, and generator-critic collusion. [S1] [S4]
- Survey and empirical sources identify communication efficiency, security, scalability, reliability, governance, and the difficulty of moving from variable-behavior prototypes to production maturity. [S3] [S8]

### Finding 10

**Claim**

Evaluation should be multi-dimensional and end-to-end rather than limited to final-answer quality.

**Confidence:** High

**Why this confidence level**

The evaluation dimensions are explicitly proposed and operationalized in the retrieved sources.

**Evidence**

- The agent-evaluation survey separates behavior, capabilities, reliability, and safety objectives from interaction modes, datasets, metrics, tooling, and evaluation contexts. [S10]
- ProtocolBench adds task utility, latency or throughput, communication overhead, and failure-time robustness as measurable dimensions. [S9]

### Finding 11

**Claim**

Current evidence does not establish that multi-agent systems generally outperform strong single-agent or alternative workflow baselines under matched cost and reliability constraints.

**Confidence:** High

**Why this confidence level**

The limitation follows from the stated methodological gaps and the contrast between practitioner claims and more qualified empirical evidence.

**Evidence**

- One taxonomy recommends establishing a single-agent baseline and adding multi-agent coordination only when a measured, decomposable failure mode warrants it. [S1]
- Applied sources make broad claims about accuracy, efficiency, and ROI, while the empirical source reports useful pilots but also emphasizes production-maturity limitations; the retrieved evidence lacks common baselines and comparable methodology. [S2] [S3] [S4] [S5]

## Conflicts and Uncertainty

- Top-level taxonomies differ. One source uses relationship-based quadrants, another uses centralized, decentralized, specialized, and hybrid orchestration categories, while another emphasizes centralized versus decentralized information flow. These should be treated as different abstraction levels rather than directly competing taxonomies. [S1] [S4] [S5]
- One source favors hierarchical or graph arrangements as practical defaults and is skeptical of swarms, while another presents decentralization as potentially more resilient. The evidence does not resolve which topology is preferable under specific scales, failure patterns, or workloads. [S1] [S5]
- Some practitioner sources characterize multi-agent systems as broadly superior for complex tasks, whereas another recommends first testing whether a single agent has reached its measured quality ceiling. No shared benchmark reconciles these conditional claims. [S1] [S2]
- Protocol-level benchmark results demonstrate scenario-dependent differences, but they do not answer how protocols interact with topology, agent count, model heterogeneity, memory, or long-horizon control flow. [S8] [S9]
- The accessible evidence supports a provisional landscape map, not a settled scholarly consensus. S6 and S7 provide insufficient substantive content in the retrieved material for strong conclusions. [S6] [S7]

## Remaining Gaps

- Determine when multi-agent coordination outperforms a strong single-agent, tool-augmented, or conventional workflow baseline under matched quality, cost, latency, and reliability constraints.
- Develop a common taxonomy that represents roles, relationships, topology, control flow, memory, communication protocols, and governance without conflating these layers.
- Measure interactions among topology, protocol, agent count, model heterogeneity, memory design, and task structure.
- Develop structured messaging, shared-state, compression, and provenance mechanisms that preserve semantics while reducing token and latency costs.
- Create benchmarks for correlated hallucinations, cascading errors, collusion, premature consensus, supervisor drift, prompt-injection propagation, and agent or tool failures.
- Establish realistic long-horizon and open-world evaluations covering task utility, capability, reliability, safety, security, latency, throughput, communication overhead, and recovery.
- Clarify governance requirements for access control, auditability, provenance, human intervention, compliance, and containment of unsafe inter-agent behavior.
- Test whether reported protocol and orchestration results generalize across independent implementations, domains, models, scales, and production deployments.

## Conclusion

The most defensible landscape map is a layered design graph: begin with an agent relationship and role structure; select a control topology and workflow; implement communication through a protocol and internal messaging strategy; then evaluate the complete system under operational, reliability, safety, and governance constraints. Multi-agent systems offer plausible benefits when work is decomposable, specialization or parallelism is valuable, or disagreement improves quality. They also introduce coordination, communication, cost, security, and reliability problems that can outweigh those benefits. The field therefore appears mature enough for a structured taxonomy and targeted comparative benchmarks, but not mature enough to support a universal architecture recommendation.

## Sources

- [S1] Agent Architecture Patterns: 2026 Taxonomy Guide — https://www.digitalapplied.com/blog/agent-architecture-patterns-taxonomy-2026
- [S2] Multi-agent LLMs in 2026 [+frameworks] - SuperAnnotate — https://www.superannotate.com/blog/multi-agent-llms
- [S3] LLM-Enabled Multi-Agent Systems: Empirical Evaluation and Insights into Emerging Design Patterns & Paradigms — https://arxiv.org/html/2601.03328v1
- [S4] LLM Agent Orchestration Patterns: Architectural ... — https://www.c-sharpcorner.com/article/llm-agent-orchestration-patterns-architectural-frameworks-for-managing-complex
- [S5] Architectures for Multi-Agent Systems — https://galileo.ai/blog/architectures-for-multi-agent-systems
- [S6] LLM-Based Multi-Agent Orchestration: A Survey of ... — https://www.mdpi.com/1999-5903/18/6/326
- [S7] LLM-Powered Multi-Agent Systems: A Survey of ... — https://dl.acm.org/doi/10.1145/3806262.3806263
- [S8] Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems — https://arxiv.org/html/2502.14321v2
- [S9] ProtocolBench: Which LLM MultiAgent Protocol to Choose? — https://arxiv.org/pdf/2510.17149
- [S10] Evaluation and Benchmarking of LLM Agents: A Survey - arXiv — https://arxiv.org/html/2507.21504v1
