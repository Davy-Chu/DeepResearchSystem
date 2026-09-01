# Research Report

## Research Question

Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are.

## Summary

The accumulated evidence supports a multidimensional, compositional map rather than one mutually exclusive taxonomy. The central architectural choices are: a single-agent baseline; independent multi-agent execution; centralized supervisor-worker coordination; decentralized peer-to-peer coordination; and hybrid systems combining hierarchy with lateral communication. These topologies can be combined with organizational patterns such as planning, specialization, debate, verifier-critic loops, graph/state-machine workflows, shared memory, and ensemble selection. Communication protocol, task regime, application domain, and evaluation/resource conditions should be treated as separate axes. The strongest consistent conclusion is conditional: multi-agent systems can help when work is decomposable, parallelizable, context-limited, or benefits from diverse perspectives, but coordination can also introduce information loss, context fragmentation, latency, cost, and error propagation. Research stopped at the iteration limit, so the authoritative version of a central scaling study and the generality of its quantitative results remain unresolved.

## Findings

### Finding 1

**Claim**

A compositional design graph is better supported than a single hierarchical taxonomy for representing multi-agent LLM systems.

**Confidence:** High

**Why this confidence level**

Multiple sources independently describe overlapping dimensions and compositional implementations.

**Evidence**

- The sources describe orthogonal dimensions including baseline choice, control topology, organizational pattern, communication paradigm, protocol, task regime, application domain, and evaluation/resource conditions. Concrete workflows combine planning, specialization, parallel dispatch, verification, shared state, and bounded graph execution. [S1] [S3] [S7] [S8] [S9] [S11] [S14] [S23] [S28]

### Finding 2

**Claim**

The core architecture graph should include five comparison nodes: single-agent, independent multi-agent, centralized, decentralized, and hybrid systems.

**Confidence:** High

**Why this confidence level**

The five-way classification is explicit and maps consistently onto the broader architectural vocabulary.

**Evidence**

- The scaling-study sources define single-agent systems as unified sequential reasoning; independent systems as noncommunicating parallel agents; centralized systems as orchestrator-worker architectures; decentralized systems as peer-to-peer systems; and hybrid systems as combinations of hierarchical and peer communication. [S28] [S29] [S30]
- These categories organize earlier patterns such as supervisor-worker, swarm, debate, ensemble, sequential decomposition, and graph orchestration. [S1] [S2] [S3] [S8] [S12] [S18]

### Finding 3

**Claim**

Major organizational and execution patterns are composable overlays on the five core topologies.

**Confidence:** High

**Why this confidence level**

The patterns are directly described across taxonomy, survey, and implementation sources, although their completeness as a universal vocabulary is not established.

**Evidence**

- The retrieved material identifies plan-and-execute, supervisor-worker, role specialization, team-based organization, debate, verifier-critic, ensemble selection, relay workflows, and graph/state-machine orchestration. [S1] [S3] [S8] [S12] [S18]
- A concrete deep-research workflow combines scouting, planning, parallel specialists, skepticism, gap analysis, citation auditing, synthesis, refinement, and bounded iteration. [S3]

### Finding 4

**Claim**

Agentic task regime should be a first-class taxonomy axis, distinct from static reasoning benchmarks.

**Confidence:** High

**Why this confidence level**

The distinction is explicitly defined in the strongest retrieved empirical study and is central to interpreting reported results.

**Evidence**

- Agentic tasks are defined as requiring sustained interaction with an external environment, iterative information gathering under partial observability, and adaptive refinement based on feedback; static tasks can be solved through single-shot reasoning without those properties. [S23] [S28] [S29] [S30]
- The scaling-study sources warn that evaluations focused on static or non-agentic tasks may give misleading guidance about collaboration in real deployments. [S23] [S30]

### Finding 5

**Claim**

Communication and coordination should be modeled as separate but interacting design dimensions.

**Confidence:** High

**Why this confidence level**

The distinction is explicitly proposed in survey and protocol sources and is consistent with the orchestration literature.

**Evidence**

- Communication taxonomies cover memory sharing, reporting, relay, debate, payload type, session state, discovery, schema flexibility, and network topology. [S7] [S8] [S9]
- Coordination concerns strategic task direction, whereas communication concerns message exchange; centralized systems can separate these functions more clearly than peer debate systems. [S9] [S20]

### Finding 6

**Claim**

Communication protocols are an emerging infrastructure layer with interoperability trade-offs.

**Confidence:** Medium

**Why this confidence level**

The dimensions and sample observations are explicit, but the evidence is limited to nine protocols and a future-dated hosted presentation of the work.

**Evidence**

- A protocol taxonomy classifies systems by counterparty, payload, interaction state, discovery mechanism, and schema flexibility. In its sample of nine open-source protocols, agent-to-agent systems commonly used hybrid payloads and session persistence, while decentralized discovery and runtime schema negotiation were less common. [S7]

### Finding 7

**Claim**

Multi-agent systems do not provide a universal performance improvement; their value depends on task structure, context conditions, model capability, and resource accounting.

**Confidence:** High

**Why this confidence level**

Different studies converge on a conditional rather than universal-superiority conclusion, although exact effect sizes and generalization boundaries remain unsettled.

**Evidence**

- Matched-thinking-token studies found single-agent systems generally matched or outperformed multi-agent variants on the reported FRAMES and four-hop MuSiQue reasoning tasks. [S14] [S15] [S18]
- The broader scaling study reports strong architecture-by-task interactions, including large gains for decomposable financial reasoning and substantial degradation on sequential planning. [S23] [S28] [S29] [S30]
- The sources attribute these differences to parallelizability, context integration, coordination overhead, tool-use demands, and error propagation. [S14] [S23] [S28] [S29] [S30]

### Finding 8

**Claim**

Centralized coordination appears promising for decomposable work and verification, while decentralized coordination may be useful for exploration and diverse peer perspectives; neither is established as a general winner.

**Confidence:** Medium

**Why this confidence level**

The conditional pattern is supported, but detailed per-topology results and fair cross-domain comparisons are incomplete.

**Evidence**

- The scaling-study sources associate centralized coordination with the strongest reported result on decomposable financial analysis and with centralized orchestration or validation. [S28] [S29] [S30]
- Secondary evidence associates decentralized systems with peer exploration, debate, and diverse perspectives in browsing-oriented settings. [S20] [S28] [S29] [S30]
- Other sources describe distinct failure modes for hierarchical, decentralized, graph, debate, and swarm designs rather than identifying one universally superior topology. [S1] [S2] [S5] [S8] [S12]

### Finding 9

**Claim**

Coordination creates a capability-versus-overhead trade-off involving context fragmentation, lossy handoffs, synchronization cost, tool-use overhead, and error amplification.

**Confidence:** High

**Why this confidence level**

The mechanisms recur across conceptual, implementation, survey, and empirical sources.

**Evidence**

- Sources report semantic drift, information loss, aggregation errors, synchronization overhead, and communication bottlenecks in multi-agent workflows. [S1] [S2] [S9] [S14] [S23]
- The scaling-study sources connect sequential-task degradation and tool-heavy-task costs to fragmented reasoning and coordination overhead, and report greater error propagation in systems without centralized verification. [S23] [S28] [S29] [S30]

### Finding 10

**Claim**

Fair evaluation requires an explicit comparison contract and process-level metrics, not final accuracy alone.

**Confidence:** High

**Why this confidence level**

This requirement is directly supported by controlled comparisons and the proposed evaluation framework.

**Evidence**

- A proposed comparison contract specifies task regime, evidence environment, evidence unit, control policy, output artifact, and evaluation contract. [S11]
- The accumulated evidence additionally indicates the need to normalize model, reasoning tokens, context tokens, tool calls, latency, monetary cost, parallel hardware, and safety conditions. [S11] [S14] [S23]
- Relevant process metrics include communication overhead, context fragmentation, redundancy, error amplification, reliability, and evidence traceability. [S23] [S28] [S29] [S30]

### Finding 11

**Claim**

Security and reliability are system-level properties affected by interaction structure, not only by individual-agent quality.

**Confidence:** High

**Why this confidence level**

The security concern is supported by direct engineering-task research and an independent survey, though generalization across domains remains uncertain.

**Evidence**

- Adversarial robustness varies with task type, injected-error subtlety, communication order, prompt framing, and role assignment. Reported threats include misinformation propagation, semantic error injection, collusion, prompt propagation, and message manipulation. [S10]
- A communication-centric survey independently identifies security vulnerabilities, scalability, and inadequate benchmarking as major challenges. [S9]

### Finding 12

**Claim**

The principal open problem is determining when specialization or coordination beats a strong single-agent or compound-inference baseline on genuinely agentic tasks under jointly normalized budgets.

**Confidence:** High

**Why this confidence level**

This gap remains central after the accumulated searches and was not resolved before the iteration limit.

**Evidence**

- Matched-budget evidence is concentrated on multi-hop reasoning, while broader agentic results have not been fully reconciled across study versions, benchmarks, and resource definitions. [S14] [S18] [S23] [S28] [S29] [S30]
- The accumulated sources explicitly leave open generalization to software engineering, scientific discovery, embodied environments, simulation, and long-running tool-use workflows. [S11] [S14] [S18] [S23]

### Finding 13

**Claim**

A quantitative scaling perspective is emerging in which coordination benefits diminish as baseline model capability rises and architecture selection can be predicted from task and system factors.

**Confidence:** Medium

**Why this confidence level**

The qualitative direction is consistent, but quantitative scope and predictive-fit figures vary across retrieved versions.

**Evidence**

- The scaling-study sources report capability saturation, diminishing coordination returns as single-agent baselines become stronger, and predictive models based on task, capability, and coordination factors. [S23] [S28]
- The same research line reports selecting the best architecture for 87% of held-out configurations, though reported study versions differ. [S28] [S29] [S30]

## Conflicts and Uncertainty

- Matched-budget multi-hop studies favor single-agent systems, whereas the broader agentic scaling study reports substantial multi-agent gains on some decomposable or exploratory tasks. The disagreement is conditional on task regime, context limitations, topology, and resource accounting rather than universal. [S14] [S15] [S18] [S23] [S28] [S29] [S30]
- Retrieved versions of the scaling study report different scopes: approximately 260 configurations across six benchmarks versus 180 configurations across four benchmarks, with differing reported R² values. The authoritative version and methodological relationship remain unresolved. [S23] [S26] [S27] [S28] [S29] [S30] [S31]
- Secondary sources report precise error-amplification and topology-specific performance figures, but the available primary-style evidence supports mainly the qualitative mechanisms and broader trends. Exact figures should not be treated as independently validated. [S23] [S28] [S29] [S31]
- Practitioner and overview sources sometimes imply that hierarchical or graph architectures are generally preferable in production, while survey and empirical sources treat decentralized, hybrid, and peer-oriented systems as conditionally viable. No retrieved evidence establishes a universal topology winner. [S1] [S2] [S5] [S8] [S20] [S28] [S29]
- Architectural benefits such as modularity, auditability, interoperability, fault isolation, and human fallback are not equivalent to task-performance gains. Industry-oriented sources emphasize these engineering benefits, while matched-budget studies show that additional agents can reduce reasoning performance in some regimes. [S14] [S18] [S22]

## Remaining Gaps

- Reconcile the authoritative version, benchmark scope, configuration count, budget definitions, and predictive metrics of the central scaling study.
- Run independent cross-domain evaluations covering software engineering, scientific discovery, embodied environments, simulation, and long-running tool-use workflows.
- Jointly normalize reasoning tokens, prompt/context tokens, tool calls, wall-clock latency, monetary cost, parallel hardware, and security controls.
- Test whether centralized verification causally reduces error amplification, rather than merely correlating with different prompts, model allocations, or compute levels.
- Identify which process metrics best predict architecture choice: task decomposability, context fragmentation, coordination overhead, redundancy, diversity, error amplification, or task-grounded capability.
- Determine which communication protocols and context-management mechanisms preserve task-relevant information while limiting semantic drift, contamination, synchronization cost, and privacy risks.
- Separate performance benefits from engineering benefits such as modularity, interoperability, auditability, fault isolation, and human fallback.
- Develop evaluations for collusion, correlated failures, premature consensus, adversarial message propagation, privacy, policy enforcement, and governance.
- Validate whether process-oriented training and continuous-improvement methods improve multi-agent coordination specifically or mainly improve individual-agent policies.

## Conclusion

The research landscape is best represented as a layered design graph:

```text
                                   ┌──────────────────────────────┐
                                   │ Evaluation / resource layer │
                                   │ task regime · evidence ·    │
                                   │ tokens · tools · latency ·  │
                                   │ cost · safety · judging     │
                                   └──────────────┬───────────────┘
                                                  │ constrains comparison
┌──────────────────────┐                          ▼
│ Single-agent baseline│                 ┌──────────────────────┐
│ unified context      │                 │ Core control topology│
└──────────┬───────────┘                 └──────────┬───────────┘
           │                                         │
           │ alternative / baseline                  │
           ▼                                         ▼
 ┌────────────────┐  ┌─────────────────┐  ┌────────────────────┐
 │ Independent MAS│  │ Centralized MAS │  │ Decentralized MAS  │
 │ parallel, no   │  │ supervisor →    │  │ peer-to-peer,      │
 │ communication  │  │ workers → merge │  │ debate / consensus  │
 └───────┬────────┘  └────────┬────────┘  └─────────┬──────────┘
         │                    │                      │
         └────────────────────┴──────────┬───────────┘
                                          ▼
                                ┌────────────────────┐
                                │ Hybrid MAS         │
                                │ hierarchy + lateral│
                                │ peer communication  │
                                └──────────┬─────────┘
                                           │
                 overlays composable with any topology
                                           ▼
      ┌─────────────────────────────────────────────────────────┐
      │ Planning · specialization · team/society · debate      │
      │ verifier-critic · ensemble · relay · shared memory     │
      │ graph/state machine · bounded iteration · human review  │
      └───────────────────────┬─────────────────────────────────┘
                              ▼
      ┌─────────────────────────────────────────────────────────┐
      │ Communication layer                                     │
      │ memory/report/relay/debate · structured/conversational  │
      │ payloads · session state · discovery · schema flexibility│
      │ agent-to-agent and agent-to-tool/context protocols      │
      └───────────────────────┬─────────────────────────────────┘
                              ▼
      ┌─────────────────────────────────────────────────────────┐
      │ Application streams                                     │
      │ problem solving · software · science · search/RAG       │
      │ embodied systems · databases · simulation · benchmarks  │
      └─────────────────────────────────────────────────────────┘

Open problems cut across every layer: fair comparison, context preservation,
coordination cost, reliability, security, interoperability, governance,
and cross-domain generalization.
```

The practical synthesis is not “more agents are better” or “single agents always win.” Instead, architecture should be selected against task structure and measured resource conditions. Single-agent systems are the necessary baseline, especially for coherent reasoning under equal budgets. Centralized or hybrid systems are plausible choices when tasks decompose cleanly and verification is valuable; decentralized systems may be appropriate when exploration or peer diversity is genuinely required. These are conditional design hypotheses, not universal conclusions. Because research stopped at the maximum iteration limit, unresolved study-version discrepancies and cross-domain generalization should remain explicit rather than being treated as settled.

## Sources

- [S1] Agent Architecture Patterns: 2026 Taxonomy Guide — https://www.digitalapplied.com/blog/agent-architecture-patterns-taxonomy-2026
- [S2] LLM Agent Orchestration Patterns: Architectural ... — https://www.c-sharpcorner.com/article/llm-agent-orchestration-patterns-architectural-frameworks-for-managing-complex
- [S3] How to Build a Multi-Agent Deep Research System with ... — https://medium.com/data-science-collective/building-a-multi-agent-deep-research-agent-with-langgraph-203547b5fb12
- [S4] From RAG to Multi-Agent Systems: A Survey of Modern Approaches in LLM Development — https://www.preprints.org/manuscript/202502.0406
- [S5] LLM-Enabled Multi-Agent Systems: Empirical Evaluation ... — https://arxiv.org/html/2601.03328v1
- [S6] Large Language Model based Multi-Agents: A Survey of ... — https://github.com/taichengguo/LLM_MultiAgents_Survey_Papers
- [S7] A Technical Taxonomy of LLM Agent Communication Protocols | alphaXiv — https://www.alphaxiv.org/abs/2606.19135v1
- [S8] LLMs for Multi-Agent Cooperation — https://xue-guang.com/post/llm-marl
- [S9] Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems — https://arxiv.org/html/2502.14321v3
- [S10] Adversarial robustness of LLM-based multi-agent systems ... — https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1784484/full
- [S11] The Landscape of LLM-Based Search Agents: A Survey — https://www.preprints.org/manuscript/202608.0572
- [S12] Multi-Agent LLM Systems: Architecture, Communication, and Coordination | Samira Ghodratnama — https://samiranama.com/posts/LLM-Based-Multi-Agent-Systems-Architectures-and-Collaboration
- [S13] Single-Agent vs Multi-Agent LLMs — Tran & Kiela (2026) · Annotated Library · Íñigo Medina — https://inigomedina.co/library/work/tran-kiela-single-agent-outperform-multi-agent
- [S14] Single-Agent LLMs Outperform Multi-Agent Systems onMulti-Hop Reasoning Under Equal Thinking Token Budgets — https://arxiv.org/html/2604.02460v1
- [S15] Why Single-Agent LLMs Beat Multi-Agent Systems on Multi-Hop Reasoning — A Budget-Controlled Story | Zhongzhu (Charlie) Zhou — https://www.zhongzhuzhou.org/blog/2026-05-18-singlevsmultiagent-technical-review-en
- [S16] Architectures for Multi-Agent Systems — https://galileo.ai/blog/architectures-for-multi-agent-systems
- [S17] Multi-agent system architecture: a comparison guide + best ... — https://www.openlayer.com/blog/multi-agent-system-architecture-guide
- [S18] Single-Agent LLMs vs Multi-Agent Systems: Equal-Budget Reasoning | Tandemly Research — https://tandemly.ai/research/single-vs-multi-agent-reasoning
- [S19] Single AI Agent vs Multi-Agent Systems | Unico Connect — https://unicoconnect.com/blogs/single-ai-agent-vs-multi-agent-systems
- [S20] Single-Agent vs Multi-Agent Systems: When Coordination Helps, Hurts ... — https://medium.com/@mjgmario/single-agent-vs-multi-agent-systems-when-coordination-helps-hurts-and-pays-off-57735ee7916d
- [S21] Single-Agent LLMs Outperform Multi-Agent Systems on ... — https://www.alphaxiv.org/abs/2604.02460
- [S22] Single Agent vs Multi-Agent: Trade-Offs, Efficiency & Control — https://www.cognizant.com/us/en/ai-lab/blog/single-agent-vs-multi-agent
- [S23] Towards a Science of Scaling Agent Systems — https://arxiv.org/html/2512.08296v3
- [S24] Capable language models can outgrow the benefits of collaboration — https://www.nature.com/articles/s42256-026-01268-y
- [S25] GitHub - ybkim95/agent-scaling: Towards a Science of Scaling Agent Systems · GitHub — https://github.com/ybkim95/agent-scaling
- [S26] Paper page - Towards a Science of Scaling Agent Systems — https://huggingface.co/papers/2512.08296
- [S27] Towards a Science of Scaling Agent Systems | Cool Papers - Immersive Paper Discovery — https://papers.cool/arxiv/2512.08296
- [S28] Towards a Science of Scaling Agent Systems | alphaXiv — https://www.alphaxiv.org/abs/2512.08296
- [S29] Overview ‹ Towards a science of scaling agent systems — https://www.media.mit.edu/projects/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/overview
- [S30] Towards a science of scaling agent systems - Google Research — https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work
- [S31] The Science of Scaling AI Agents: A Briefing on New Methodologies and Failure Modes — https://micheallanham.substack.com/p/the-science-of-scaling-ai-agents
