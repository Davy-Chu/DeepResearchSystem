# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** multi-agent-llm-landscape

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 70.9 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.64
- Coverage: 0.65
- Depth: 0.62
- Citation quality: 0.75
- Citation validity: 1.00
- Citation support: 0.71
- Citation completeness: 0.68
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report recognizes that scope and taxonomy are unsettled and mentions several relevant adjacent cases, but it does not establish the explicit operational boundary required by the rubric. The evidence is limited to baseline treatment and taxonomy caveats rather than a scope definition.
- Candidate evidence:
  - The report recommends establishing a “strong single-agent baseline” and distinguishes “single-agent baseline,” “Single agent: ReAct / tool use,” and “Single-LLM simulation of homogeneous workflow.”
  - The report states that “the taxonomy is a synthesis” and that terminology is not standardized.
- Missing:
  - No explicit operational inclusion and exclusion criteria are provided.
  - The report does not consistently address prompt chains, classical non-LLM multi-agent systems, or hybrid LLM/non-LLM designs.
  - It does not clearly distinguish multiple roles instantiated by one model from genuinely multi-agent systems, beyond briefly listing single-LLM simulation.
  - Borderline cases are not resolved under a consistent rule.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report covers a broad and materially differentiated set of architectural patterns and provides meaningful trade-offs for several of them. Coverage is not full because the depth and evidence are uneven across patterns, especially for applications and complete per-pattern characterization.
- Candidate evidence:
  - Finding 2 identifies single-agent baseline, independent parallel agents, centralized supervisor-worker, decentralized swarm/peer-to-peer, explicit graph/workflow, and hybrid systems.
  - The graph describes control and information flow such as “supervisor -> workers -> validation -> supervisor,” “agent -> agent -> agent,” and “specialist A ... specialist B ... merge/synthesis.”
  - Findings 5–8 explain supervisor-worker bottlenecks, the distinction between swarm and parallel fan-out, workflow control-flow benefits, and debate/verifier-critic limitations.
  - Finding 9 supplies task-dependent evidence: coordination improves decomposable work but can harm tightly sequential reasoning.
- Missing:
  - Some patterns are primarily named or sketched rather than systematically characterized across all requested dimensions: control structure, agent arrangement, information flow, coordination mechanism, applications, and limitations.
  - Representative applications or systems are unevenly supplied; the report gives a deep-research workflow and some benchmark contexts but not representative systems for every major architectural family.
  - Debate, verifier-critic, planning, and reflexive patterns are treated more as overlays or subpatterns than fully characterized architectures, without always explaining their relationship to the main families.

### R3

- Coverage: 0.75
- Depth: 0.50
- Rationale: Several important design axes and consequences are present, particularly topology, execution shape, communication, and synchronization. However, the analysis is distributed across findings and does not fully cover the rubric’s requested dimensions or provide a systematic cross-pattern treatment.
- Candidate evidence:
  - The summary explicitly identifies control topology, execution shape, communication and memory, and verification as cross-cutting dimensions.
  - The report discusses centralized versus decentralized control, hierarchical supervision versus peer interaction, sequential versus parallel execution, message passing, shared/context memory, synchronization, and fragmented global context.
  - Finding 10 links message passing, context compression, synchronization, duplicated reasoning, and divergent states to coordination cost.
  - The remaining gaps mention state consistency, observability, authorization, rollback, privacy, and loop termination for decentralized systems.
- Missing:
  - The report does not systematically analyze synchronous versus asynchronous operation, static versus dynamic agent allocation, or context isolation versus sharing as explicit dimensions.
  - Consequences for independence, consistency, and scalability are discussed unevenly and mostly qualitatively.
  - The cross-cutting dimensions are not clearly mapped back to each architectural pattern in a structured comparison.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report names and illustrates most relevant roles and mechanisms and shows how they combine in workflow and supervisor designs. It falls short of full depth because the essential-versus-optional distinction and several mechanism interactions remain implicit.
- Candidate evidence:
  - The graph includes planning, specialists, validation, synthesis, communication schemas, shared/context memory, tools/environment, debate or verifier-critic, citation/quality audit, and observability/governance.
  - The deep-research example combines “planning, parallel specialists, auditing, synthesis, writing, and refinement within a graph.”
  - Finding 5 explains supervisor delegation, routing, validation, ordering, and conflict handling.
  - Finding 7 describes typed nodes, branches, joins, retries, bounded iterations, citation auditing, and refinement.
- Missing:
  - The report does not clearly distinguish essential architectural features from optional overlays or implementation choices, despite listing them as layers.
  - Evidence/provenance tracking is mentioned through citation auditing, but its mechanisms and relationship to memory, retrieval, and synthesis are not developed in depth.
  - Retrieval, tools, memory/shared state, and human oversight are listed or briefly discussed rather than systematically explained as compositional mechanisms.

### R5

- Coverage: 0.75
- Depth: 0.75
- Rationale: The visualization is legible, self-contained enough to interpret, and shows alternatives, composition, feedback, overlays, and open-problem locations. It is not fully comprehensive because its legend/readout and several cross-cutting dimensions are underdeveloped.
- Candidate evidence:
  - Finding 3 provides a labeled ASCII design graph from “USER/TASK” through task diagnosis to single-agent, sequential, parallel, supervisor, swarm, workflow, and hybrid branches.
  - The graph includes explicit relationships such as planner/executor flow, fan-out and merge, supervisor feedback, peer handoff, and cross-cutting layers.
  - The graph labels open-problem hotspots including task diagnosis, lossy handoffs, context synchronization, error propagation, cost/latency, adaptive topology, heterogeneity, evaluation, and governance.
  - The report states that the graph is “a research map, not a claim that the field has formally adopted this exact graph,” and notes varying terminology.
- Missing:
  - The prose does not explicitly provide a concise legend or step-by-step explanation of how to read the graph.
  - The graph’s relation between primary architectural families and overlays such as debate, memory, tools, and observability is indicated but not fully formalized.
  - Some important cross-cutting axes, such as synchronous/asynchronous execution and static/dynamic allocation, are absent from the visual.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is one of the stronger sections: it gives conditional rather than universal rankings, discusses quality, cost, latency, tokens, and coordination overhead, and includes uncertainty qualifications. Full credit is withheld because empirical context is incomplete and several criteria and evidence-quality distinctions are uneven.
- Candidate evidence:
  - Finding 9 reports conditional effects of “+80.8% on decomposable financial reasoning to −70.0% on sequential planning” and attributes them to parallel exploration versus communication and fragmentation costs.
  - Finding 10 analyzes message, synchronization, context, duplication, tool-heavy-task, and single-agent-capability effects on cost and benefit.
  - Finding 12 compares swarm latency/token advantages with supervisor routing-accuracy advantages and contrasts reflexive accuracy with hierarchical cost-accuracy performance.
  - The uncertainty section warns that results come from different tasks and methods and should not be pooled as field-wide estimates.
- Missing:
  - The quantitative claims do not consistently identify all required experimental details, including precise baselines, metrics, prompts/models, budgets, and experimental contexts; the report itself notes missing full tables and compute accounting.
  - Fault tolerance, evidence sharing, and human or operational cost are not compared systematically across patterns.
  - Some comparisons rely on practitioner or secondary sources with limited methodological detail, as the report acknowledges.
  - Measured findings and design intuitions are not always explicitly separated within each comparison.

### R7

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes many relevant evaluation dimensions and failure modes and gives a few concrete controls, such as bounded iterations and citation auditing. However, the rubric requires linked risk-to-mitigation analysis, which is substantially incomplete.
- Candidate evidence:
  - Finding 11 discusses outcome success, database state, policy adherence, repeated-trial pass^k reliability, and τ-bench-style evaluation.
  - The report identifies hallucination/error propagation, information fragmentation, premature convergence, judge bias, collusion, over-correction, correlated failures, tool interaction difficulty, loop termination, authorization, privacy, and governance concerns.
  - The remaining gaps propose evaluating quality, pass^k reliability, policy adherence, error propagation, recovery, latency, token cost, auditability, and human-oversight burden.
  - The graph includes citation/quality audit and observability/governance layers; the deep-research workflow uses bounded iterations and citation auditing.
- Missing:
  - Major risks are not consistently paired with concrete safeguards, monitoring procedures, or human-oversight mechanisms.
  - Contradictory memory/state failures, runaway execution, tool misuse, security, and governance are mostly listed as gaps rather than explained and mitigated.
  - The report gives little detail on coordination-behavior metrics, agent-level versus system-level fault diagnosis, or ablations against single-agent and no-verification baselines.
  - It does not consistently qualify which risks are architecture-specific rather than shared by all systems.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report provides a substantial, organized open-problem agenda with identifiable sources and useful uncertainty qualification. It does not reach full credit because problem statements and evidence qualification are uneven, and source provenance and researchability are not consistently developed.
- Candidate evidence:
  - Finding 14 organizes open problems into semantic coordination/state management, reliability/error recovery, cost/scalability, evaluation standardization, model heterogeneity, adaptive topology, and governance.
  - The Remaining Gaps section specifies unresolved questions about task-feature prediction, homogeneous workflow equivalence, heterogeneous models, controlled benchmarking, observability, state consistency, authorization, rollback, privacy, and malicious or faulty agents.
  - The report explains why several problems matter through links to context drift, semantic loss, token consumption, partial failures, architecture-task mismatch, and non-comparable evaluations.
  - Sources are identifiable through numbered entries with titles and URLs, including the scaling study, debate survey, τ-bench, and architecture comparisons.
  - The report distinguishes confidence levels, reported limitations, source conflicts, study-specific effects, and future directions.
- Missing:
  - Open problems are not always framed as sharply testable research questions with proposed measurements or experimental designs.
  - Source quality is uneven: several claims rely on blogs, Medium posts, practitioner guides, or aggregator pages, and the report does not always distinguish peer-reviewed or primary evidence from these sources at the point of use.
  - Some major open problems, especially provenance, interoperability, memory, and governance, receive limited explanation of the precise unresolved mechanism and its consequences.
  - The report cites sources by identifiers but does not provide standard bibliographic metadata such as authors, publication venue, or dates for many entries.

### Novel Value

- The report offers a useful compositional design graph that combines topology, execution shape, communication/memory, verification, and governance overlays rather than treating architectures as mutually exclusive.
- It synthesizes a conditional architecture-task alignment principle and explicitly counters universal claims about multi-agent superiority.
- It highlights the distinction between decentralized swarm handoffs and concurrent parallel fan-out, a potentially useful taxonomy clarification.
- It identifies adaptive topology and principled architecture selection as central open problems, supported by reported held-out prediction results and acknowledged replication uncertainty.

## Citations

### Support

#### F1: PARTIALLY_SUPPORTED

- Claim: The research landscape is best modeled as composable architectural dimensions rather than a single canonical taxonomy.
- Sources: S24, S4, S9, S18
- Rationale: The sources support modeling agent-system research through multiple architectural dimensions and patterns: S24 defines systems using agents, environment, communication topology, and orchestration; S4 identifies orchestration, communication, and control-flow components; S9 presents a three-dimensional taxonomy and notes many interacting design decisions; and S18 contrasts composable patterns such as swarm, supervisor, and hybrids. However, the stronger evaluative claim that this is “best” and the contrast with a “single canonical taxonomy” are not directly established. In fact, S9 explicitly presents a taxonomy, though it also describes the field as fragmented and its taxonomy as a descriptive map.
- Supporting text: S24: the framework models systems with agents, environment, communication topology, and orchestration policy. S4: it formalizes orchestration, communication mechanisms, and control-flow strategies. S9: it derives a three-dimensional taxonomy and says configurations involve roughly a dozen interacting design decisions. S18: it describes swarm, supervisor, and hybrid architectures as alternatives selected according to task structure.

#### F2: PARTIALLY_SUPPORTED

- Claim: A useful visual taxonomy is: single-agent baseline; independent parallel agents; centralized supervisor-worker; decentralized swarm or peer-to-peer systems; explicit graph/workflow systems; and hybrid systems combining hierarchical control with lateral communication. These can be augmented by planning, debate, verifier-critic, memory, and evaluation layers.
- Sources: S29, S1, S8, S18, S3
- Rationale: The saved sources support most of the main taxonomy: single-agent systems, independent/parallel agents, centralized supervisor-worker systems, decentralized swarm or handoff systems, explicit graph/workflow systems, and hybrid systems. They also explicitly describe planning, debate, and verifier-critic as patterns or layers. However, the sources do not meaningfully support the full claim that memory and evaluation layers augment every taxonomy category, nor do they clearly establish the exact proposed taxonomy as a single visual taxonomy. Peer-to-peer is also only indirectly supported through S18's description of swarm topology as a mesh/peer-to-peer structure.
- Supporting text: S29 identifies five canonical architectures: “Single-Agent and four Multi-Agent: Independent, Centralized, Decentralized, Hybrid.” S18 distinguishes decentralized swarm handoffs from centralized supervisor and fan-out parallelism, while S8 describes hierarchical systems and “explicit multi agent workflows” with node-and-edge control flow. S18 states that production teams deploy hybrids such as “supervisor planning with parallel execution.” S1 explicitly lists plan-and-execute, multi-agent debate, and verifier-critic patterns; S3 describes planning, parallel investigation, claim checking, citation verification, and synthesis in a graph workflow.

#### F3: PARTIALLY_SUPPORTED

- Claim: Visual taxonomy/design graph:

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
- Sources: S29, S8, S18, S3, S20
- Rationale: The saved sources substantiate the diagram's main architectural taxonomy and several relationships: task-architecture alignment; single-agent/ReAct tool use; homogeneous-workflow simulation; sequential, parallel, supervisor, swarm, explicit workflow, and hybrid patterns; specialist roles, synthesis, citation auditing, termination, communication loss, context fragmentation, error propagation, and heterogeneous-model limitations. However, the claim presents a comprehensive graph whose exact structure and all labels are not established by the snapshots. In particular, the sources do not clearly support every diagnostic criterion (such as high-stakes or state-sharing), every single-agent branch (such as Reflexion), typed nodes, optional replanning, peer sharing in the hybrid, or the full list of governance and adaptive-topology hotspots.
- Supporting text: S29 describes five canonical architectures—Single-Agent, Independent, Centralized, Decentralized, and Hybrid—and says architecture-task alignment matters. S8 describes hierarchical supervisor systems and explicit workflows with sequential or concurrent fan-out. S18 characterizes swarms as decentralized sequential handoffs and supervisors as centralized routing with validation, while identifying supervisor planning plus parallel execution as a hybrid. S3 describes a graph with planning, six parallel specialists, synthesis, citation auditing, and bounded termination. S29 discusses lossy inter-agent communication, context fragmentation, synchronization overhead, and error cascades; S20 supports single-LLM simulation of homogeneous workflows and identifies heterogeneous workflows as a limitation/open direction.

#### F4: PARTIALLY_SUPPORTED

- Claim: Single-agent systems are an essential baseline and may be preferable when the task is sequential, context-integrated, or not cleanly decomposable.
- Sources: S29, S15, S20
- Rationale: The sources support treating single-agent systems as a strong or important baseline and indicate advantages for sequential and context-integrated tasks. S29 reports that multi-agent systems can substantially underperform on sequential planning and explains that single agents maintain unified access to global context. S20 explicitly calls single-agent execution a strong baseline and finds comparable performance to homogeneous multi-agent workflows with lower cost. However, the sources do not directly establish the broader claim that single-agent systems are preferable whenever a task is not cleanly decomposable, nor do they justify the normative term “essential” in all settings.
- Supporting text: S29: “Relative performance change compared to single-agent baseline ranges from ... +80.8% on decomposable financial reasoning to −70.0% on sequential planning,” and single-agent systems “maximize context integration” through a unified memory stream. S20: “These results position the single-LLM implementation of multi-agent workflows as a strong baseline for MAS research.”

#### F5: SUPPORTED

- Claim: Centralized supervisor-worker systems offer modular delegation, routing visibility, validation, ordering, and conflict handling, but introduce routing overhead, bottlenecks, and a central failure point.
- Sources: S8, S18, S10, S17
- Rationale: The saved sources collectively support all material elements of the claim. S8 describes supervisors delegating to specialist agents, reusable modular teams, and centralized routing as a bottleneck and single point of failure. S18 explicitly lists dynamic routing, output validation and ordering, and conflict/loop prevention as supervisor responsibilities. S10 supports centralized visibility/consistency and identifies coordination overhead, throughput bottlenecks, and orchestrator failure as weaknesses. S17 further supports routing visibility through traceable routing decisions and identifies extra routing calls and latency as supervisor overhead.
- Supporting text: S18: the supervisor provides “dynamic task routing,” “output validation and ordering,” and “conflict and loop prevention.” S8: specialists are reusable building blocks, but “every request flows through that central coordinator,” making it “both a routing bottleneck and a single point of failure.” S10: centralized systems ensure consistency, while “latency increases due to sequential coordination” and the orchestrator can become a bottleneck; if it fails, processing stops.

#### F6: SUPPORTED

- Claim: Decentralized swarm systems should be distinguished from parallel fan-out. Swarms use distributed, generally sequential handoffs, whereas fan-out runs multiple specialists concurrently under some coordinating mechanism.
- Sources: S18, S1, S3, S8
- Rationale: S18 directly states the distinction: swarm control is decentralized and sequential, with one active agent at a time, while fan-out executes multiple agents simultaneously and requires coordination. S8 independently describes fan-out as concurrent specialist execution dispatched by a router and contrasts it with supervisor-based delegation. S3 describes six specialized researchers working in parallel, supporting the fan-out characterization. S1 supports the broader distinction between swarm and supervisor/worker coordination, though the supplied excerpt does not itself define swarm in detail.
- Supporting text: S18: “Swarm is strictly decentralized sequential control transfer where each agent acts in turn”; its table contrasts this with “Fan-Out Parallelism,” where “N agents run simultaneously” and a central coordinator assigns work. S8: a workflow can “fan them out concurrently,” with both specialists running concurrently after a router produces a plan.

#### F7: SUPPORTED

- Claim: Explicit graph/workflow architectures provide stronger control-flow boundaries, auditability, synchronization, and termination guarantees, but shift responsibility for branching, recovery, concurrency, and refinement to system designers.
- Sources: S8, S3
- Rationale: S8 directly states that explicit workflows define control-flow boundaries, branches, convergence, and termination, provide more control, and require designers to define orchestration and concurrent execution. It also identifies auditable control-flow boundaries as a use case. S3 describes graph-enforced citation auditing, bounded iteration as a structural termination guarantee, parallel specialist execution, and explicit refinement. Together, the sources support the claim’s main contrast, although “synchronization” is conveyed through convergence and downstream combination rather than stated using that exact term.
- Supporting text: S8: Explicit workflows define “which nodes may run, how work can move between them, where branches converge, and when execution must end”; they offer “more control” but require designers to design the orchestration and concurrent execution. S3: the graph enforces citation auditing before writing, uses a maximum iteration condition as a structural termination guarantee, dispatches specialists in parallel, and ends after refinement.

#### F8: SUPPORTED

- Claim: Debate, verifier-critic, and other adversarial architectures form a distinct research sublandscape focused on quality, robustness, safety, and agreement rather than only task parallelization.
- Sources: S9, S1
- Rationale: S9 explicitly presents Multi-Agent Debate as a research paradigm and systematic literature review, describing a fragmented field with its own taxonomy of participants, interaction mechanisms, and agreement protocols. It links debate to accuracy, robustness, critique, iterative refinement, and consensus. S1 independently places debate and verifier-critic in a distinct “competitive and adversarial” quadrant, contrasting them with collaborative multi-agent patterns that trade coordination overhead for parallelism or specialization, and states that they are used for quality and safety rather than parallel work.
- Supporting text: S9: MAD improves “accuracy and robustness,” lets agents “critique each other’s outputs,” and converge toward a solution; the review provides a taxonomy of debate participants, interaction mechanisms, and agreement protocols. S1: “Multi-agent competitive and adversarial” architectures involve agents in “tension or critique,” used for “quality and safety improvement, not parallel work,” including multi-agent debate and verifier-critic.

#### F9: SUPPORTED

- Claim: The strongest emerging empirical principle is architecture-task alignment: multi-agent coordination can improve decomposable or parallelizable work but can degrade tightly sequential reasoning.
- Sources: S29, S18
- Rationale: S29 directly reports controlled evaluations showing large gains on decomposable financial reasoning and substantial declines on sequential planning, and explicitly concludes that architecture-task alignment determines collaborative success. S18 independently describes the same task-structure dependency, stating that parallel or swarm patterns fit independent workloads while mismatched coordination degrades performance. The cited sources support both the improvement and degradation components of the claim.
- Supporting text: S29: Relative performance ranged from +80.8% on decomposable financial reasoning to −70.0% on sequential planning; “architecture-task alignment determines collaborative success.” S18: “Multi-agent systems fail when the orchestration pattern mismatches the task structure”; parallel patterns fit independent workloads, while supervisors handle complex dependencies.

#### F10: PARTIALLY_SUPPORTED

- Claim: Multi-agent systems incur a coordination tax arising from message passing, context compression, synchronization, duplicated reasoning, and divergent agent states; tool-heavy tasks and strong single-agent baselines can reduce the benefit of adding agents.
- Sources: S29, S23, S24, S20
- Rationale: The sources directly support a coordination tax involving inter-agent message passing, lossy context compression, synchronization overhead, and divergent agent/world states. They also support that tool-heavy tasks incur greater multi-agent overhead and that coordination can yield diminishing returns when single-agent baselines are already strong. However, the supplied text does not clearly support duplicated reasoning as a component of the coordination tax, nor does it explicitly establish that strong single-agent baselines reduce the benefit in general beyond the stated diminishing-returns finding.
- Supporting text: S29 states that multi-agent systems incur an “unavoidable coordination tax” because global context must be compressed into inter-agent messages, increasing synchronization overhead; it also says agents operate on progressively divergent world states. S23 reports that tool-heavy tasks increase the coordination “tax” disproportionately. S29 and S24 report diminishing returns once single-agent baselines exceed certain performance, while S20 finds a single agent can match homogeneous multi-agent workflows with lower inference cost.

#### F11: PARTIALLY_SUPPORTED

- Claim: Reliability should be treated as a first-class architectural objective. τ-bench-style evaluations show that simple tool-calling and ReAct agents struggle with dynamic user interaction, policy adherence, state changes, and repeated execution.
- Sources: S16, S12
- Rationale: S16 directly supports the evaluation finding: τ-bench assesses dynamic interaction with users and tools, policy following, database-state changes, and repeated-task reliability via pass^k; it also reports that simple function-calling and ReAct agents perform poorly. However, “reliability should be treated as a first-class architectural objective” is a prescriptive interpretation rather than a directly stated conclusion, and S12 mainly supplies leaderboard context rather than evidence about all listed failure dimensions. The sources support a narrower claim that reliability is important to measure and that simple agents struggle on τ-bench tasks.
- Supporting text: S16 states that robust measurement of agent performance and reliability is “critical to their successful deployment”; τ-bench requires interaction with humans and APIs over long horizons, adherence to complex policies, consistency at scale, and correct final database state. It introduces pass^k to test whether agents complete the same task repeatedly, and reports that agents built with function calling or ReAct “perform poorly,” with even GPT-4o below 50% average success across two domains.

#### F12: SUPPORTED

- Claim: No architecture is established as universally superior. Different objectives and workloads favor different designs: swarm may reduce latency, supervisors may improve routing visibility, reflexive systems may improve accuracy, hierarchical systems may improve cost-accuracy tradeoffs, and single-agent execution may match homogeneous workflows more cheaply.
- Sources: S17, S14, S29, S20
- Rationale: The sources collectively support the claim’s main content. S29 explicitly reports that architecture-task alignment determines success and that relative performance varies substantially by task, supporting the absence of a universally superior design. S17 reports lower latency for swarm and higher routing accuracy for supervisors, while noting that the choice depends on whether latency or misroutes are the bottleneck; its description that supervisor routing decisions are visible in traces supports the visibility point. S14 reports that reflexive architectures achieve the highest F1 and that hierarchical architectures have the most favorable cost-accuracy Pareto position. S20 reports that single-agent execution can match homogeneous workflows while reducing cost.
- Supporting text: S29: “architecture-task alignment determines collaborative success.” S17: swarm latency ~2.8s versus supervisor ~4.2s, while supervisor routing accuracy is 94% versus swarm’s 91%; “the right choice depends on whether your bottleneck is latency or misroutes.” S14: reflexive achieves the highest field-level F1, while hierarchical has the most favorable cost-accuracy Pareto position. S20: a single agent can reach comparable performance to homogeneous workflows “while reducing cost.”

#### F13: PARTIALLY_SUPPORTED

- Claim: The current evidence supports adaptive or mixed architecture selection as a major research direction: select topology, execution shape, verification, and model allocation according to measurable task properties rather than fixed agent count.
- Sources: S29, S18, S24
- Rationale: The sources strongly support selecting architecture and coordination patterns based on task structure and measurable task/system factors rather than assuming that more agents are better. They also support mixed or hybrid architectures and centralized verification. However, the cited text does not establish the full claim that topology, execution shape, verification, and model allocation should all be selected adaptively, nor does it explicitly characterize this as a major research direction or address model allocation.
- Supporting text: S29/S24 state that performance varies with measurable system and task factors, that architecture-task alignment determines success, and that mismatched coordination degrades performance. S18 says pattern selection matters more than agent count and describes hybrids combining supervisor planning with parallel execution; it also identifies dynamic routing and output validation as supervisor responsibilities.

#### F14: PARTIALLY_SUPPORTED

- Claim: The principal open problems are semantic coordination and state management, reliability and error recovery, cost and scalability, evaluation standardization, model heterogeneity, adaptive topology, and governance.
- Sources: S2, S3, S4, S5, S9, S29, S20
- Rationale: The sources collectively identify most of these as challenges or future directions: semantic coordination and context/state handling (S2, S3, S5), reliability and error propagation (S3, S4, S29), cost and scalability (S2, S3, S4, S9, S20, S29), evaluation comparability and standardization (S9, S29), heterogeneity (S20), topology design and alternatives to static topologies (S9), and governance (S4). However, the saved excerpts do not establish that this exact set is exhaustive or definitively constitutes the principal open problems, and state management and adaptive topology receive less direct support than the other categories.
- Supporting text: S4 calls for further work on “reliability, scalability, and governance.” S9 reports “inconsistent terminology,” unreliable cross-study comparison, and a field dominated by “static, fully connected topologies,” proposing controlled benchmarking and automated tuning. S20 says that developing effective heterogeneous workflows remains an open direction. S29 highlights coordination costs, error propagation, and the lack of a principled framework for predicting when multi-agent coordination helps.

### Missing Citations

- Q20: The field lacks a common, controlled protocol comparing the listed architectures under matched prompts, tools, models, and budgets.
- Q21: The most predictive task features remain unresolved, including decomposability, dependency depth, tool count, state-sharing requirements, exploration need, conflict frequency, and trajectory length.
- Q22: It remains unclear when separate agent instances outperform a single agent executing the same homogeneous workflow through multi-turn role sequencing.
- Q23: The benefits and disadvantages of heterogeneous models and genuinely independent critics are not established.
- Q25: Decentralized systems need stronger solutions for observability, state consistency, authorization, loop termination, rollback, privacy, and malicious or faulty agents.
- Q26: The landscape supports a conditional design principle rather than a race toward larger agent teams.
- Q27: Multi-agent LLM systems are best understood as combinations of topology, execution shape, communication and memory, specialization, and verification.
- Q28: Centralized or explicit workflow designs are appropriate when decomposition, ordering, validation, and auditability matter; parallel specialists are appropriate when subtasks are genuinely independent; decentralized handoffs or peer debate are appropriate when local autonomy or diverse perspectives are valuable.
- Q29: The central open research challenge is to make architecture selection principled and adaptive using reproducible task features and common reliability- and cost-aware evaluations.

## Deterministic Checks

- `run_metadata_loads`: PASS
- `report_exists`: PASS
- `sources_present`: PASS
- `structured_report_parses`: PASS
- `report_question_matches`: PASS
- `source_ids_unique`: PASS
- `source_ids_syntactically_valid`: PASS
- `source_urls_present`: PASS
- `evidence_objects_valid`: PASS
- `confidence_values_valid`: PASS
- `citation_ids_syntactically_valid`: PASS
- `citation_ids_resolve`: PASS
- `structured_claim_evidence_available`: NOT_EVALUABLE — This run predates or does not use an evidence ledger.
- `ledger_claim_ids_unique`: NOT_EVALUABLE — Evidence ledger unavailable.
- `ledger_evidence_relationships_resolve`: NOT_EVALUABLE — Evidence ledger unavailable.
- `ledger_confidence_values_valid`: NOT_EVALUABLE — Evidence ledger unavailable.
- `ledger_evidence_ids_unique`: NOT_EVALUABLE — Evidence ledger unavailable.

## Main Weaknesses

1. R1: Define an operational scope for multi-agent LLM systems and distinguish included systems from adjacent configurations.
2. R7: Explain how multi-agent systems are evaluated and how their characteristic failure modes and risks can be detected or mitigated.
3. R3: Analyze design dimensions that cut across architectural patterns and explain their consequences.
4. 8 cited finding(s) were not fully supported by saved evidence.
5. 9 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `3ba296f97ad2c98be185e194bbae89b363b2bc81a38fd31abf5dbf056e9a34b0`
- Candidate report hash: `0abdba96c79eca0e62a44dfaa85d3320308719452d6b500c810bde3e289102cf`
- LLM calls: 16
- Evaluated at: 2026-09-01T07:09:14.578209+00:00
