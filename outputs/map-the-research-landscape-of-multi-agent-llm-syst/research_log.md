# Research Run Log

## Run Summary

**Research Question**

Map the research landscape of multi-agent LLM systems. Produce a structured report that includes a visual taxonomy or design graph showing the major architectural patterns, how they relate, and where the open problems are.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 14

**OpenAI Calls:** 4

**Tavily Calls:** 3

**Started:** 2026-08-30T17:27:02-04:00

**Ended:** 2026-08-30T17:35:30-04:00

**Total Runtime:** 507.49s

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

- **S1 — Agent Architecture Patterns: 2026 Taxonomy Guide - Digital Applied**
  URL: https://www.digitalapplied.com/blog/agent-architecture-patterns-taxonomy-2026
- **S2 — A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges**
  URL: https://link.springer.com/article/10.1007/s44336-024-00009-2
- **S3 — LLM Agent Orchestration Patterns: Architectural ...**
  URL: https://www.c-sharpcorner.com/article/llm-agent-orchestration-patterns-architectural-frameworks-for-managing-complex
- **S4 — Medium**
  URL: https://medium.com/data-science-collective/building-a-multi-agent-deep-research-agent-with-langgraph-203547b5fb12
- **S5 — Multi-Agent AI Architecture: Patterns for Enterprise Development | Augment Code**
  URL: https://www.augmentcode.com/guides/multi-agent-ai-architecture-patterns-enterprise

**Search Duration:** 3.48s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

A useful high-level model of LLM multi-agent systems separates agent internals from system-level coordination: agents have profiles, perception, self-action, mutual interaction, and evolution, while systems can be studied through workflows, infrastructure, applications, and challenges.

**Confidence:** High

**Why this confidence level**

This is a direct summary of a peer-reviewed survey's abstract and article description.

**Evidence**

- The 2024 survey proposes five workflow components—profile, perception, self-action, mutual interaction, and evolution—and organizes applications into problem-solving and world simulation. [S2]

#### Finding 2

**Claim**

The main architectural design space includes centralized hierarchical coordination, decentralized peer-to-peer interaction, specialized role-based collaboration, and hybrid combinations.

**Confidence:** Medium

**Why this confidence level**

The categories recur across sources, but S3 is a practitioner-oriented article and S5 is vendor-produced rather than an independent academic comparison.

**Evidence**

- The orchestration article explicitly proposes a four-category taxonomy: centralized, decentralized, hybrid, and specialized. [S3]
- The enterprise architecture guide presents hub-spoke, mesh, and hierarchical patterns as canonical topology choices, distinguished by communication topology, state ownership, and failure domains. [S5]

#### Finding 3

**Claim**

Hub-spoke or supervisor-worker systems centralize routing and state aggregation, making them suitable when auditability, specialist routing, and failure isolation are important, but they introduce hub overload and single-point-of-failure risks.

**Confidence:** Medium

**Why this confidence level**

The architectural trade-off is consistently described by two sources, but the sources do not provide independent controlled evaluations.

**Evidence**

- S5 describes a hub dispatching specialist agents, owning canonical state, and synthesizing outputs; it identifies the hub as a single point of failure and notes context growth and degraded routing in long workflows. [S5]
- S1 describes supervisor-worker systems as hierarchical decomposition into specialized workers, with coordination overhead, supervisor drift, and hidden subtask conflicts as failure modes. [S1]

#### Finding 4

**Claim**

Graph-based workflows provide explicit task dependencies, conditional routing, parallel branches, iterative gap checking, and staged synthesis; they can combine several other patterns rather than constitute a wholly separate agent behavior.

**Confidence:** Medium

**Why this confidence level**

S4 directly documents one implementation, and S1 supplies a broad taxonomy claim, but neither establishes general superiority across benchmarks.

**Evidence**

- S4 shows a LangGraph research workflow with classifier, planner/architect, parallel specialists, gap analyzer, citation audit, writer, and refiner nodes, including bounded iteration and conditional routing. [S4]
- S1 characterizes graph topologies and hierarchical topologies as the two multi-agent patterns it claims are most useful in production, while also stating that production systems commonly compose multiple patterns. [S1]

#### Finding 5

**Claim**

Plan-and-execute is a collaborative two-stage pattern in which a planner produces a plan and an executor carries it out; its central research problem is balancing plan efficiency against adaptation when execution conditions change.

**Confidence:** Medium

**Why this confidence level**

The pattern and trade-offs are directly stated, but the source is a taxonomy guide rather than a primary experimental paper.

**Evidence**

- S1 defines plan-and-execute as planner followed by executor and identifies plan brittleness, capability mismatch, and over-optimization for plan completion as failure modes; proposed mitigations include replanning triggers and bounded plans. [S1]

#### Finding 6

**Claim**

Debate and verifier-critic architectures use adversarial or evaluative roles to improve reliability, safety, and decision quality, but they risk correlated errors, premature convergence, judge bias, collusion, and over-correction.

**Confidence:** Medium

**Why this confidence level**

The role patterns are directly documented, but evidence that they improve outcomes relative to simpler baselines is limited in the retrieved material.

**Evidence**

- S1 describes multi-agent debate with arguing agents and a judge, and verifier-critic with generator, critic, and revision roles; it lists convergence, judge bias, collusion, and subjective-critique degradation as failure modes. [S1]
- S4 operationalizes skepticism and citation auditing as separate roles and structurally prevents report writing until citation auditing has occurred. [S4]

#### Finding 7

**Claim**

Decentralized mesh or swarm designs trade centralized observability and control for peer autonomy and potentially richer interaction; their open problems include semantic drift, error amplification, and difficult state ownership.

**Confidence:** Low

**Why this confidence level**

The sources identify plausible failure modes, but comparative performance evidence is asserted rather than demonstrated, and the practitioner sources use inconsistent terminology.

**Evidence**

- S3 discusses contextual drift, differing interpretations, semantic loss in communication, and emergent behavior as coordination problems in LLM-agent networks. [S3]
- S5 characterizes mesh as peer-to-peer and contrasts its failure domain and coordination properties with hub-spoke and hierarchical designs. [S5]
- S1 claims swarms and blackboard patterns are theoretically interesting but rarely outperform hierarchical or graph patterns in practice. [S1]

#### Finding 8

**Claim**

Important cross-cutting research problems are semantic coordination, context and memory management, resource usage, verification, observability, and termination/control of recursive workflows.

**Confidence:** High

**Why this confidence level**

Multiple sources independently identify overlapping problem dimensions, even though their depth and methodological quality differ.

**Evidence**

- S3 identifies contextual drift, protocol semantic loss, behavior complexity, and token-consumption/resource optimization as central coordination issues. [S3]
- S4 highlights citation verification, gap detection, bounded deep-research iterations, partial-result recovery, and cost control as explicit system properties. [S4]
- S5 frames state ownership, coordination complexity, observability, and failure isolation as architecture-defining dimensions. [S5]
- S2 states that the survey discusses contemporary challenges and future directions, though the retrieved excerpt does not enumerate them in detail. [S2]

### Conflicts Found

- The sources offer different counts and boundaries for the taxonomy. S1 claims eight canonical patterns across four quadrants and treats graph and hierarchical topologies as especially important; S3 uses four orchestration categories; S5 reduces enterprise topology choices to three canonical patterns. These are not necessarily mutually exclusive, but they operate at different abstraction levels and should not be presented as one settled universal taxonomy. [S1] [S3] [S5]
- S1 claims that hierarchical coordination 'wins over swarm in production almost every time' and that eight patterns cover about 95% of production systems, whereas the retrieved evidence provides no benchmark or sampling method supporting those quantitative/general claims. [S1]
- S3 reports large operational gains, including 30–45% faster completion, 25–80% lower token cost or semantic errors, and 130% ROI, while the other sources provide no corroboration, experimental design, baseline, or dataset for those figures. [S3]
- S1 states that Reflexion reduces repeated failures by 30–50%, but the retrieved material does not provide the underlying experiment or establish whether the figure transfers to multi-agent systems. [S1]

### Important Gaps

- What unified taxonomy best distinguishes behavioral patterns (debate, critique, planning), communication topologies (star, mesh, graph), and control policies (centralized, decentralized, hybrid)?
- Which multi-agent architectures outperform a strong single-agent baseline, and on which task classes, under matched model, tool, token, latency, and cost budgets?
- How should multi-agent systems be evaluated for coordination quality, task success, factuality, calibration, robustness, cost, latency, and failure recovery?
- How can semantic drift and protocol information loss be detected and measured across long agent interactions?
- What state and memory ownership models preserve consistency while avoiding hub context-window growth and excessive synchronization?
- When do debate, criticism, or redundant agents improve reliability rather than amplify correlated model errors or create expensive, unproductive loops?
- What benchmark suites and reproducible traces exist for comparing hierarchical, graph, mesh, swarm, blackboard, and hybrid systems?
- How do these architectures behave under adversarial agents, tool failures, partial observability, changing environments, and distribution shift?
- The retrieved excerpt from the academic survey identifies challenges generally but does not provide enough detail to map its challenge categories or cited primary studies.

**Analysis Duration:** 18.61s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The sources are sufficient to draft a preliminary taxonomy and design graph, but the original task asks for a research landscape. The current evidence is dominated by one academic survey and practitioner/vendor articles, with little primary experimental evidence, no systematic benchmark comparison, and incomplete coverage of evaluation, coordination protocols, memory, safety, and open-source infrastructure. One focused academic search should target comparative evaluations and taxonomies of LLM multi-agent architectures.

**Next Search**

> LLM multi-agent systems architecture taxonomy benchmark evaluation centralized decentralized hierarchical graph swarm debate memory coordination survey

---

# Iteration 2

## 1. Search

**Query**

> LLM multi-agent systems architecture taxonomy benchmark evaluation centralized decentralized hierarchical graph swarm debate memory coordination survey

**Why this query**

The sources are sufficient to draft a preliminary taxonomy and design graph, but the original task asks for a research landscape. The current evidence is dominated by one academic survey and practitioner/vendor articles, with little primary experimental evidence, no systematic benchmark comparison, and incomplete coverage of evaluation, coordination protocols, memory, safety, and open-source infrastructure. One focused academic search should target comparative evaluations and taxonomies of LLM multi-agent architectures.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S6 — LLM-Based Multi-Agent Systems**
  URL: https://www.emergentmind.com/topics/llm-based-multi-agent-systems
- **S7 — Multi-Agent LLM Systems: Architecture, Communication, and Coordination | Samira Ghodratnama**
  URL: https://samiranama.com/posts/LLM-Based-Multi-Agent-Systems-Architectures-and-Collaboration
- **S8 — Multi-Agent Debate Strategies: Survey, Taxonomy, and Challenges**
  URL: https://arxiv.org/html/2607.26212v1
- **S9 — Architectures for Multi-Agent Systems**
  URL: https://galileo.ai/blog/architectures-for-multi-agent-systems

**Search Duration:** 2.18s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

A robust taxonomy should separate at least three layers: agent control loops and capabilities, communication/topology, and coordination or decision protocols.

**Confidence:** High

**Why this confidence level**

Multiple sources independently support separating internal agent mechanisms from system topology and interaction or resolution protocols.

**Evidence**

- S6 describes agent-level MAPE-K-style control loops, memory, adaptation, and planning, while separately listing centralized, decentralized, hierarchical, layered, and blackboard architectures. [S6]
- S8 organizes multi-agent debate around participants, interaction mechanisms, and agreement protocols, demonstrating that topology alone does not capture the full design space. [S8]
- Prior sources distinguish agent internals from system-level workflows and coordination. [S2]

#### Finding 2

**Claim**

The major topology families are centralized or hierarchical, decentralized peer networks, shared-memory or blackboard systems, and graph or DAG workflows; these families can be composed into hybrids.

**Confidence:** High

**Why this confidence level**

The topology families recur across several sources, although terminology and category boundaries vary.

**Evidence**

- S6 explicitly identifies centralized, decentralized, layered or hierarchical, and blackboard architectures, and describes DAG-based decentralized coordination. [S6]
- S9 presents centralized orchestrator systems and decentralized systems as primary alternatives, emphasizing their differing information flow and failure modes. [S9]
- S4 and prior findings show graph workflows combining routing, parallel specialists, verification, and bounded iteration. [S4]
- S1 states that production systems commonly compose multiple patterns rather than using one pure architecture. [S1]

#### Finding 3

**Claim**

Debate, critique, proposer-aggregator, planning, and verification are interaction or control protocols that may be embedded within any topology rather than standalone topology classes.

**Confidence:** High

**Why this confidence level**

The sources directly describe these mechanisms as role and interaction designs, supporting their placement beneath or across topology categories.

**Evidence**

- S8 defines debate through participant configuration, interaction mechanisms, and agreement protocols, and reports that many studies implicitly use static fully connected communication, short-term memory, verbatim exchange, and voting. [S8]
- S6 describes proposer-aggregator mixture-of-agents systems, planner-critic combinations, and ReAct-like reasoning-action loops. [S6]
- S1 and S4 document plan-and-execute, verifier-critic, debate, citation auditing, and gap-checking as workflow or role patterns. [S1] [S4]

#### Finding 4

**Claim**

A useful design graph is a compositional graph rather than a single mutually exclusive tree: topology determines information flow, protocol determines coordination behavior, and shared state or memory determines context and consistency properties.

**Confidence:** High

**Why this confidence level**

Several sources explicitly identify these as separate but interacting design dimensions.

**Evidence**

- S9 links architecture to information flow, failure modes, scaling, token usage, latency, and context concentration. [S9]
- S5 identifies communication topology, state ownership, observability, and failure domains as distinct architecture dimensions. [S5]
- S6 separately discusses communication, short- and long-term memory, retrieval, adaptation, and experience reuse. [S6]

#### Finding 5

**Claim**

The strongest newly supported open problem is systematic, cost-aware comparison of debate and broader multi-agent configurations, because many design choices are conventionally fixed and often left implicit.

**Confidence:** High

**Why this confidence level**

S8 provides direct systematic-review evidence, while prior findings establish that the same evaluation gap affects multi-agent architectures generally.

**Evidence**

- S8 reports a systematic review of 141 primary studies and finds that static fully connected debate, verbatim exchange, short-term memory, and voting dominate by convention rather than demonstrated superiority. It calls for controlled benchmarking, executable specifications, cost-aware evaluation, and automated tuning. [S8]
- Prior findings identify the lack of matched comparisons against strong single-agent baselines and the need to evaluate success, factuality, calibration, robustness, cost, latency, and recovery. [S1] [S3] [S4]

#### Finding 6

**Claim**

Cross-cutting open problems include scalability and resource control, semantic coordination, memory and state ownership, safety and bias, observability, and adaptation under changing conditions.

**Confidence:** High

**Why this confidence level**

These concerns are repeated across academic-survey and architecture-oriented sources, even though their empirical measurement remains underdeveloped.

**Evidence**

- S6 identifies scalability, safety, bias mitigation, memory, adaptation, distributed planning, and reinforcement-learning-based coordination as central themes. [S6]
- S3 identifies contextual drift, semantic loss, emergent behavior, and token or resource optimization problems. [S3]
- S4 and S5 identify verification, bounded execution, cost control, state ownership, observability, and failure isolation as explicit system concerns. [S4] [S5]

### Conflicts Found

- S8's systematic review reports that debate research converges on static fully connected topologies, while S6 and prior sources present decentralized graphs, blackboards, adaptive policies, and other alternatives as active architectural directions. This is not a direct contradiction: S8 describes what is common in the surveyed debate literature, whereas S6 describes the broader space of proposed systems. [S6] [S8]
- S9 makes strong quantitative claims that token usage explains 80% of performance variance and that centralized orchestration becomes a bottleneck at roughly 10–20 agents; the retrieved material provides no methodology or independent corroboration for these figures. [S9]
- S6 cites recent reinforcement-learning and graph-policy methods as improving stability and scalability, but the retrieved excerpt does not provide comparative experimental details, task conditions, or evidence that these results generalize across LLM multi-agent systems. [S6]
- The taxonomy boundaries remain inconsistent: S7 uses flat, hierarchical, team-based, central-coordinator, and hybrid categories; S6 uses centralized, decentralized, hierarchical, layered, and blackboard categories; prior sources use topology, behavioral, and orchestration categories at different levels. [S6] [S7] [S1] [S3] [S5]

### Important Gaps

- Which architectures outperform a strong single-agent baseline under matched model, tool, token, latency, and cost budgets?
- How should topology, protocol, memory, and state ownership be represented in one benchmarkable design schema?
- When do debate, critique, voting, or redundancy improve reliability rather than amplify correlated errors, judge bias, or increase cost?
- What benchmark suites and reproducible execution traces compare hierarchical, graph, mesh, blackboard, swarm, and hybrid systems?
- How can semantic drift, protocol information loss, state inconsistency, and coordination failure be measured over long-horizon interactions?
- How do systems behave under adversarial agents, tool failures, partial observability, distribution shift, and changing environments?
- The retrieved sources do not establish reliable general performance thresholds for scalability, latency, token efficiency, or agent-team size.

**Analysis Duration:** 13.99s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The landscape and architectural taxonomy can now be mapped responsibly, but the report's most important unresolved component—comparative evidence about when each architecture works—remains weak. A focused search for controlled benchmark studies would materially improve the design recommendations and open-problem section.

**Next Search**

> controlled benchmark comparison multi-agent LLM architectures hierarchical graph debate blackboard swarm single-agent baseline cost latency

---

# Iteration 3

## 1. Search

**Query**

> controlled benchmark comparison multi-agent LLM architectures hierarchical graph debate blackboard swarm single-agent baseline cost latency

**Why this query**

The landscape and architectural taxonomy can now be mapped responsibly, but the report's most important unresolved component—comparative evidence about when each architecture works—remains weak. A focused search for controlled benchmark studies would materially improve the design recommendations and open-problem section.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S10 — Benchmarking Multi-Agent LLM Architectures for Financial Document Processing: A Comparative Study of Orchestration Patterns, Cost-Accuracy Tradeoffs and Production Scaling Strategies**
  URL: https://arxiv.org/html/2603.22651v1
- **S11 — Comparing Single-Agent and Multi-Agent Strategies in ...**
  URL: https://www.mdpi.com/2079-9292/15/8/1661
- **S12 — Multi-agent system architecture: a comparison guide + best practices ...**
  URL: https://www.openlayer.com/blog/multi-agent-system-architecture-guide
- **S13 — Exploring Advanced LLM Multi-Agent Systems Based on Blackboard Architecture | alphaXiv**
  URL: https://www.alphaxiv.org/abs/2507.01701
- **S14 — Benchmarking Multi-Agent Architectures - LangChain**
  URL: https://www.langchain.com/blog/benchmarking-multi-agent-architectures

**Search Duration:** 2.53s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Recent empirical work strengthens the case for treating architecture selection as a cost–accuracy–latency trade-off rather than a search for one universally best multi-agent pattern.

**Confidence:** Medium

**Why this confidence level**

The source describes a relatively large, multi-model benchmark with explicit metrics, but the retrieved content does not expose its detailed methods, statistical analysis, or independently replicated results.

**Evidence**

- A benchmark on 10,000 SEC filings compared sequential, parallel fan-out/merge, hierarchical supervisor-worker, and reflexive self-correcting architectures across five models and five evaluation axes. Reflexive systems achieved the highest field-level F1 (0.943) but cost 2.3 times the sequential baseline; hierarchical systems achieved F1 0.921 at 1.4 times baseline cost and occupied the reported cost–accuracy Pareto frontier. [S10]
- The benchmark reports architecture-specific scaling behavior from 1,000 to 100,000 documents per day, including non-linear throughput–accuracy degradation and architecture-specific capacity knee points. [S10]

#### Finding 2

**Claim**

Hybrid optimization mechanisms can substantially narrow the gap between high-quality reflexive systems and cheaper baselines in at least one regulated document-extraction setting.

**Confidence:** Low

**Why this confidence level**

This is a promising ablation result, but it is reported for one domain and the retrieved material does not provide enough detail to assess robustness or transferability.

**Evidence**

- S10 reports that combining semantic caching, model routing, and adaptive retries recovered 89% of reflexive architecture accuracy gains at 1.15 times sequential-baseline cost. [S10]

#### Finding 3

**Claim**

Blackboard systems deserve a distinct place in the taxonomy as shared-state, dynamically scheduled architectures rather than being treated simply as decentralized peer networks.

**Confidence:** Medium

**Why this confidence level**

The architecture is directly specified and the source reports multi-benchmark comparisons, but the evidence is a single implementation and the retrieved excerpt does not establish whether comparisons used matched models, token budgets, or strong contemporary baselines.

**Evidence**

- The proposed LbMAS system uses a shared blackboard as the sole communication medium, an LLM-based control unit that selects agents based on current blackboard contents, and repeated execution/update/evaluation cycles until a decision or a four-round limit. [S13]
- The system reports competitive or best-average results across six reasoning and knowledge benchmarks, with a 4.33% improvement over chain-of-thought and 5.02% over static multi-agent systems in the retrieved summary. [S13]

#### Finding 4

**Claim**

Blackboard coordination may improve token efficiency through selective activation and shared context management, but it introduces state-management and context-size questions that remain open.

**Confidence:** Medium

**Why this confidence level**

The efficiency mechanism and ablation are directly reported, while the scalability concern follows from the architecture and is independently identified by prior sources.

**Evidence**

- S13 reports that removing the control unit increased MATH token use from 4.7 million to 13.8 million with little performance impact, while a cleaner agent removed redundant messages; each selected agent nevertheless reads the entire blackboard. [S13]
- The prior landscape identifies memory ownership, context growth, synchronization, and consistency as unresolved cross-cutting problems. [S5] [S6] [S9]

#### Finding 5

**Claim**

A controlled benchmark from LangChain provides evidence that supervisor and swarm behavior depends on task structure and communication handoffs, and that multi-agent designs can outperform a single agent when irrelevant tool/context volume grows.

**Confidence:** Medium

**Why this confidence level**

The comparison uses a common model and an explicit baseline, but it is a company benchmark on 100 retail-domain examples and does not cover broad task classes or independent replication.

**Evidence**

- On a modified Tau-bench evaluation using GPT-4o, the single-agent baseline fell sharply when two or more distractor domains were added; swarm slightly outperformed supervisor across the reported experiments, with the supervisor loss attributed to translation between sub-agents and the user. [S14]
- The source explicitly frames the test as a distractor-context scaling experiment and warns that the result represents a best-case setting requiring little coordination beyond filtering irrelevant tools and instructions. [S14]

#### Finding 6

**Claim**

The new evidence supports representing blackboard/shared workspace as a state-and-memory dimension orthogonal to topology, while sequential, parallel, hierarchical, and reflexive designs are better represented as workflow/control patterns.

**Confidence:** High

**Why this confidence level**

The distinction is directly supported by the different architectural objects studied in the sources and is consistent with multiple prior taxonomy findings.

**Evidence**

- S10 compares sequential, parallel, hierarchical, and reflexive orchestration patterns, whereas S13 defines blackboard coordination through shared state, dynamic agent selection, and iterative control. [S10] [S13]
- Prior sources support separating topology, protocol, and state ownership rather than forcing all patterns into one mutually exclusive tree. [S5] [S6] [S8] [S9]

### Conflicts Found

- S10 reports hierarchical orchestration as the best cost–accuracy trade-off in financial extraction, while S14 reports swarm slightly outperforming supervisor on its Tau-bench distractor-context test. These results are conditional rather than directly contradictory: the tasks, metrics, sample sizes, model setup, and coordination demands differ. [S10] [S14]
- S13 reports blackboard performance improvements over static multi-agent systems and strong token efficiency, whereas prior S1 characterized blackboard and swarm patterns as rarely outperforming hierarchical or graph systems in practice. The comparison is unresolved because the sources use different tasks and do not share a matched benchmark. [S1] [S13]
- S12 makes broad practitioner claims about performance degradation, coordination overhead, and research growth, but the retrieved content does not provide methods or primary-study details sufficient to validate its quantitative claims. These claims should not be treated as equivalent to benchmark evidence from S10, S13, or S14. [S12] [S10] [S13] [S14]

### Important Gaps

- Do the architecture rankings reported by S10 and S14 transfer across domains, task structures, model families, and tool environments?
- Which multi-agent architectures outperform a strong single-agent baseline under matched token, latency, cost, and model-quality budgets?
- Can blackboard systems retain their reported token efficiency when the shared workspace becomes large, multi-document, multimodal, or partially private?
- How should performance gains from reflexive loops, debate, verification, caching, routing, and retries be disentangled from simply spending more tokens or making more model calls?
- What standardized benchmark and trace schema can compare topology, workflow protocol, memory/state ownership, model diversity, and control policy together?
- How do these systems behave under adversarial agents, tool failures, partial observability, distribution shift, and long-horizon recursive execution?
- The retrieved S11 page contains article metadata and title information but not enough substantive methods or results to inform the landscape.
- The retrieved excerpts do not establish general scalability thresholds or causal explanations for when supervisor translation, blackboard selection, or hierarchical decomposition helps.

**Analysis Duration:** 16.47s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The runner reached the maximum research iteration budget. Analyzer assessment: The new sources materially improve the landscape by adding domain-specific controlled comparisons, a blackboard implementation, and a single-agent distractor-context baseline. However, the central open question remains unanswered: there is no broad, independently reproducible benchmark comparing the major topology and protocol families under matched budgets across diverse tasks. A focused search could also recover the missing substantive results from S11, but the more important gap is cross-architecture generalization.

**Stop Reason:** max_iterations

---

# Final Research Decision

**Research Stopped Because**

The runner reached the maximum research iteration budget.

**Stop Reason:** max_iterations

**Searches Performed:** 3

**Unique Sources:** 14

**Remaining Uncertainty**

- A standardized schema is needed to encode topology, workflow protocol, state and memory ownership, model diversity, communication semantics, and stopping rules together.
- Broad benchmarks should compare major architectures against strong single-agent baselines under matched model, tool, token, latency, and cost budgets.
- Future evaluations should span sequential, parallelizable, ill-structured, long-horizon, regulated, and interactive tasks rather than relying on one domain.
- Researchers need measures for semantic drift, protocol information loss, state inconsistency, coordination quality, calibration, failure recovery, and error propagation.
- It remains unclear whether blackboard token efficiency persists when shared workspaces become large, private, multimodal, or distributed.
- Debate and critique studies should disentangle gains from genuine diversity or verification from gains caused simply by additional model calls and tokens.
- Robustness under adversarial agents, tool failures, partial observability, distribution shift, and recursive execution is insufficiently characterized.
- The retrieved evidence does not establish general scalability thresholds for hub capacity, team size, context length, latency, or token consumption.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 8.19s |
| OpenAI Analysis | 3 | 49.07s |
| Report Generation | 1 | 23.74s |
| Total Run | — | 507.49s |
