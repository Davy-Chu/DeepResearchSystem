# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** multi-agent-llm-landscape

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 68.4 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.56
- Coverage: 0.59
- Depth: 0.50
- Citation quality: 0.82
- Citation validity: 1.00
- Citation support: 0.79
- Citation completeness: 0.81
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report establishes nearby baselines and frames the landscape, but it does not provide the required scope definition or explicit inclusion/exclusion rules.
- Candidate evidence:
  - The summary defines a multidimensional landscape using coordination topology, execution structure, interaction objective, communication/state, and control/assurance axes.
  - The report identifies single-agent ReAct or deterministic workflows as baselines and says multi-agent systems are motivated by specialization, context partitioning, and parallelization.
  - The conclusion recommends starting with a deterministic workflow or strong single-agent graph before adding coordination.
- Missing:
  - It does not state an explicit operational inclusion criterion for what counts as a multi-agent LLM system.
  - It does not consistently distinguish single-agent tool use, prompt chains, multiple roles instantiated by one model, classical non-LLM multi-agent systems, or hybrid LLM/non-LLM designs.
  - It does not explain how borderline configurations are classified, despite acknowledging that taxonomy boundaries vary.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is one of the strongest sections: it covers materially distinct patterns and explains their relationships and several trade-offs. Coverage is not complete because application/system representation and depth are uneven.
- Candidate evidence:
  - Finding 1 identifies centralized, decentralized, hierarchical, and graph-based topologies and recurring patterns including orchestrator-worker, hierarchical delegation, pipeline, fan-out/fan-in, swarm, mesh, debate, verifier-critic, and hybrid compositions.
  - Finding 2 explains the control and information-flow logic of pipelines, fan-out, supervisors, hierarchies, decentralized designs, debate, and verification.
  - Findings 3-8 characterize specific patterns and give limitations such as cascading pipeline failures, fan-out partial failure, coordinator bottlenecks, hierarchy overhead, swarm ambiguity, and uncertain comparative effectiveness.
  - Finding 9 conditionally associates patterns with task structures such as fixed dependencies, independent subtasks, dynamic routing, and repeated quality concerns.
- Missing:
  - Representative applications or concrete systems are only lightly addressed; most examples are pattern descriptions or source labels rather than systematic application/system profiles.
  - Information flow, coordination mechanisms, and limitations are unevenly detailed across decentralized, mesh, blackboard, debate, and verifier variants.
  - The report does not clearly separate architectural features from implementation variants for every pattern.

### R3

- Coverage: 0.50
- Depth: 0.50
- Rationale: Many relevant axes are named and some consequences are explained, but the cross-cutting analysis is incomplete and uneven rather than a full comparative design analysis.
- Candidate evidence:
  - The summary explicitly lists centralized/decentralized control, hierarchical/peer topology, sequential/parallel/handoff/event-driven execution, direct messages/shared memory/blackboards, and multiple control dimensions.
  - Finding 4 explains that fan-out is centralized concurrent execution whereas the described swarm variant uses distributed routing and one active agent at a time.
  - Findings 5-7 discuss centralized traceability, coordinator bottlenecks, hierarchy overhead, peer interaction, shared state, handoffs, and observability/convergence issues.
  - The report notes that hybrid systems combine supervisor planning with parallel execution or verification.
- Missing:
  - The consequences of synchronous versus asynchronous operation are not analyzed explicitly.
  - Context isolation versus sharing is mentioned mainly as motivation or a bottleneck, not systematically compared for consistency, independence, or error propagation.
  - Static versus dynamic agent allocation is not developed beyond brief references to dynamic routing/adaptive control.
  - The report does not provide a cross-pattern matrix or systematic synthesis of how each dimension affects coordination, independence, consistency, scalability, latency, and fault tolerance.

### R4

- Coverage: 0.75
- Depth: 0.50
- Rationale: The principal roles and many supporting mechanisms are present, but the required compositional explanation and essential-versus-optional distinction are only partial.
- Candidate evidence:
  - Finding 5 describes coordinators/orchestrators, specialized workers, state tracking, routing, and result synthesis.
  - Finding 8 covers judges or synthesizers, verifiers, critics, revision, and guardrails.
  - Finding 10 identifies typed interfaces, tools, health checks, retries, fallbacks, budgets, observability, provenance, access control, and policy enforcement.
  - The report discusses shared or scoped state, memory, handoffs, typed tools, tracing, and evaluation as component layers.
- Missing:
  - Tool use and retrieval are not explained as composition mechanisms in their own right.
  - Memory/shared state and evidence/provenance tracking are mostly listed rather than integrated into concrete architectural examples.
  - The report does not clearly distinguish essential architectural features from optional overlays or implementation choices.
  - The role interactions among planner, worker, critic, synthesizer, retrieval, memory, and provenance components are not systematically mapped.

### R5

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report describes what a visualization should contain but does not supply the required interpretable visual artifact.
- Candidate evidence:
  - Finding 1 describes a proposed visual taxonomy with a baseline branching by topology, execution semantics, and interaction objective.
  - Finding 2 gives a textual relationship chain: baseline workflow or single agent -> coordination need -> pipeline, fan-out, supervisor, hierarchy, decentralized handoff/mesh, or critique/verification -> hybrid systems with shared state, recovery, and governance.
  - The summary presents several taxonomic axes.
- Missing:
  - No actual visual taxonomy, diagram, ASCII graph, table, or design graph is provided.
  - There is no self-contained legend or visual encoding of alternatives, composition, hierarchy, or overlays.
  - The prose does not explain how to read an actual visualization or show open problems located on the graph.
  - Important relationships among cross-cutting overlays and architectural patterns remain implicit.

### R6

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report is appropriately conditional and unusually transparent about weak evidence, but the breadth and depth of empirical comparison remain limited.
- Candidate evidence:
  - Findings 3-9 provide conditional trade-offs involving predictability, cascade failure, wall-clock latency, partial branch failure, bottlenecks, single points of failure, coordination overhead, dynamic routing, verification cost, and task suitability.
  - Finding 12 identifies quality, repeated-trial reliability, latency, token/monetary cost, safety, and coordination-specific failures as evaluation dimensions.
  - Finding 13 reports a modified tau-bench comparison using gpt-4o, 100 retail examples, distractor environments, and single-agent, swarm, and supervisor systems, while explicitly noting missing numerical scores, variance, costs, and topology-isolating ablations.
  - Finding 14 reports a financial-document comparison using accuracy, F1, latency, cost, and token efficiency, while qualifying the evidence as methodologically incomplete.
- Missing:
  - Most comparisons are qualitative engineering claims rather than evidence-based empirical comparisons.
  - Fault tolerance, evidence sharing, and scalability are not systematically compared across patterns.
  - The report does not consistently distinguish measured findings from design intuition for the many qualitative claims.
  - Quantitative evidence is narrow and lacks full baseline, variance, statistical treatment, cost details, and reproducible experimental context.

### R7

- Coverage: 0.75
- Depth: 0.50
- Rationale: Evaluation dimensions, failure classes, and a broad assurance layer are well covered, but risk-to-safeguard linkage and operational detection guidance are incomplete.
- Candidate evidence:
  - Finding 12 covers outcome correctness, pass^k/repeated-trial reliability, latency, cost, safety/policy compliance, stateful interaction, and coordination failures, and recommends strong single-agent and deterministic baselines.
  - Finding 11 identifies inconsistent shared state, duplicated work, contradictions, routing errors, context loss, nontermination, and error propagation.
  - Finding 10 proposes typed contracts, budgets, termination rules, timeouts, retries/fallbacks, observability, provenance, access control, and policy enforcement.
  - Remaining Gaps identifies prompt injection, privacy, provenance, collusion, unauthorized tool actions, privilege boundaries, and auditable shared state as unresolved governance/security issues.
- Missing:
  - Hallucination propagation, correlated errors/groupthink, contradiction and memory failures, runaway execution, tool misuse, and opacity are not each linked to a specific detection or mitigation procedure.
  - Human oversight is mentioned as checkpoints in the summary but is not developed as a mitigation strategy.
  - The report does not clearly distinguish which risks are architecture-specific versus common only to certain system designs.
  - Coordination-behavior evaluation and recovery testing are mentioned but not operationalized with concrete protocols or metrics.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report gives a strong, specific and well-qualified open-problem agenda with identifiable sourcing. It falls short of full depth because problem statements are not uniformly converted into researchable protocols and the evidence base is uneven.
- Candidate evidence:
  - Remaining Gaps organizes specific problems involving canonical taxonomy, reproducible benchmarks, controlled architecture comparisons, evaluation contracts, crossover conditions, topology-versus-implementation effects, swarm definitions, decentralized-system evidence, and security/governance.
  - The report explains why several gaps matter, including inability to establish architecture-independent winners, inability to isolate topology effects, and missing evidence for cost, reliability, safety, and scalability.
  - The Sources section provides identifiable URLs for surveys, architecture reports, benchmark descriptions, LangChain experiments, and a financial-document preprint.
  - The report repeatedly qualifies evidence, distinguishing practitioner consensus, narrow benchmark results, preprints, secondary summaries, and unvalidated prevalence or superiority claims.
- Missing:
  - Several open problems are listed more than analyzed; the unresolved mechanism, proposed research design, or success criterion is not specified for every major problem.
  - Source quality is uneven, with substantial reliance on practitioner blogs, vendor material, social media, and secondary summaries; primary literature and peer-reviewed evidence are limited.
  - The report does not consistently connect each open problem to a representative benchmark, system, or documented study.
  - Some source dates and identities appear future-dated or difficult to validate from the report alone, weakening source reliability even though the URLs are identifiable.

### Novel Value

- The report offers a useful multidimensional rather than mutually exclusive taxonomy.
- It explicitly flags the ambiguity of the term “swarm” and warns against comparing implementations without specifying concurrency, routing authority, and state-transfer semantics.
- It provides unusually cautious treatment of limited architecture-level benchmark evidence and emphasizes topology-versus-implementation confounding.
- It synthesizes a practical assurance layer—typed contracts, bounded execution, recovery, observability, provenance, access control, and governance—as an overlay across patterns.

## Citations

### Support

#### F1: PARTIALLY_SUPPORTED

- Claim: A useful visual taxonomy places single-agent and deterministic systems at the baseline, then branches by coordination topology, execution semantics, and interaction objective rather than treating patterns as mutually exclusive.
- Sources: S8, S10, S1, S5, S11, S14, S18, S30, S29
- Rationale: The sources support a baseline of single-agent systems and describe multiple classification dimensions, including coordination topology, communication structure, execution flow, and interaction type. They also explicitly state that systems may combine patterns or use hybrids. However, the specific framing that deterministic systems are at the baseline, that the taxonomy branches exactly by the three named axes, and that the patterns should not be treated as mutually exclusive is not fully established across the cited text.
- Supporting text: S1 says to “Start single-agent” and that production systems are often “compositions of two or three” patterns. S8 proposes centralized, decentralized, and hierarchical topologies with an adaptive axis. S10 distinguishes actors, cooperation/competition, structures, strategies, and protocols; S11 and S14 describe sequential, hierarchical, swarm, debate, and other distinct patterns. S18 explicitly says systems map to “one of five orchestration patterns, or a hybrid of two or more.”

#### F2: PARTIALLY_SUPPORTED

- Claim: The central design graph is: baseline workflow or single agent -> coordination need -> pipeline, fan-out, supervisor, hierarchy, decentralized handoff/mesh, or critique/verification -> hybrid systems with shared state, recovery, and governance.
- Sources: S23, S25, S27, S29, S1, S11, S12, S14, S17, S18, S30, S5
- Rationale: The saved sources collectively support most of the proposed progression: they describe starting with deterministic workflows or a single-agent baseline, adding multi-agent coordination when complexity, context, specialization, or parallelism requires it, and using pipeline, fan-out, supervisor, hierarchical, swarm/mesh, and critique or debate patterns. They also support hybrid compositions and discuss shared state, recovery, guardrails, validation, and access control. However, the sources do not establish this exact sequence as the single or central design graph, and the final combination of shared state, recovery, and governance is presented unevenly across sources rather than as a unified endpoint.
- Supporting text: S23 says to consider deterministic workflows or a single agent first and to use swarm or supervisor systems as complexity grows. S25 identifies single agent as the baseline and presents swarm and supervisor architectures. S14 lists fan-out, pipeline, debate, supervisor, and swarm as distinct patterns. S18 states that production systems map to these patterns or hybrids and describes shared state and error recovery. S5 adds deterministic state machines, state recovery, access control, validation, and fallback handling.

#### F3: SUPPORTED

- Claim: Sequential pipelines are low-complexity and predictable, but their principal risk is cascading failure when an intermediate stage produces an incorrect result or cannot adapt to changed conditions.
- Sources: S11, S14, S17, S18
- Rationale: The cited sources collectively support the claim. S11 explicitly characterizes sequential pipelines as predictable, low in system complexity, and low in fault tolerance, while noting limited flexibility for unexpected edge cases. S14 directly describes pipeline failure as a cascade in which a bad mid-stage contaminates all subsequent stages. S17 independently characterizes the pattern as linear, deterministic, and easy to debug. S18 supports the sequential stage-based architecture and contrasts it with patterns offering different fault-tolerance and flexibility trade-offs.
- Supporting text: S11: “System Complexity: Low,” “Fault Tolerance: Low,” and the pipeline is “highly predictable but lacks the flexibility to dynamically adjust… if an unexpected edge case arises.” S14: “A pipeline failure is a cascade — a bad mid-stage contaminates everything after it.”

#### F4: SUPPORTED

- Claim: Fan-out/fan-in is a distinct centralized-parallel pattern: a coordinator dispatches independent branches concurrently and an aggregator merges them; it should not be conflated with decentralized swarm execution.
- Sources: S14, S12, S25
- Rationale: S14 explicitly defines fan-out as a distinct pattern in which a coordinator dispatches parallel branches and aggregates their results, and distinguishes it from swarm. S12 directly contrasts fan-out parallelism with decentralized swarm handoffs, including central coordination versus distributed routing and parallel versus sequential execution. S25 further characterizes swarm as decentralized handoffs with only one active agent at a time.
- Supporting text: S14: “A coordinator dispatches ... specialized subtasks ... simultaneously, then aggregates the results.” S12: the table contrasts “Fan-Out Parallelism” (truly parallel, central coordinator) with “Swarm” (sequential, distributed routing, no coordinator). S25: “Only one agent can be active at any given time” in a swarm.

#### F5: SUPPORTED

- Claim: Supervisor or orchestrator-worker systems are the principal centralized multi-agent pattern: a coordinator decomposes a goal, routes subtasks to specialized workers, tracks state, and synthesizes results.
- Sources: S1, S5, S11, S18, S30, S22, S31
- Rationale: The saved sources consistently describe supervisor/orchestrator-worker as a centralized or hierarchical pattern in which a coordinator decomposes goals, delegates subtasks to specialized workers, tracks progress or global state, and aggregates or synthesizes their outputs. Several sources also characterize it as common, default, or widely deployed, supporting the claim that it is a principal centralized pattern. S22 confirms the central delegation structure, though its benchmark reports that Swarm slightly outperformed Supervisor in that study; this does not contradict the architectural claim.
- Supporting text: S5: “A central supervisor agent parses the high-level intent, decomposes the objective into targeted subtasks, dispatches work to specialized sub-agents, and synthesizes the outputs”; the supervisor “tracks execution progress.” S18/S30/S31: the orchestrator-worker pattern is “the most widely deployed in production” and the “default starting pattern,” with the orchestrator maintaining global state and deciding when the task is complete. S11 similarly calls hierarchical supervision “the most common and intuitive” approach.

#### F6: SUPPORTED

- Claim: Hierarchical delegation extends supervisor coordination into a tree: top-level supervisors assign subgoals to intermediate supervisors, which manage workers. It is useful when decomposition boundaries and authority levels are clear, but adds coordination layers and latency.
- Sources: S6, S7, S18, S30, S1, S9
- Rationale: The saved sources directly support the architecture, use case, and trade-off portions of the claim. S6/S7 describe multiple supervisor layers in which a top coordinator assigns subgoals to mid-level supervisors that manage worker agents, and say the pattern works for complex workflows with clear decomposition boundaries. S18/S30 explicitly characterize hierarchical delegation as tree-structured. S9 states that supervisor/mid-level/worker layers incur coordination latency, including a three-level example where each level adds delay. The phrase “authority levels” is a reasonable characterization of the layered supervisory roles, though the sources more explicitly describe scope and tactical responsibility than the term authority itself.
- Supporting text: S6/S7: “Hierarchical architectures stack multiple supervisor layers. A top coordinator breaks down goals into subgoals, assigns each to mid-level supervisors… Those supervisors manage their own worker agents.” They also state: “This pattern works for complex workflows with clear decomposition boundaries.” S18/S30 call hierarchical architecture “tree-structured delegation.” S9: “A supervisor agent sits at the top, sub-coordinators sit in the middle, worker agents sit at the bottom,” and identifies the cost as “coordination latency.”

#### F7: PARTIALLY_SUPPORTED

- Claim: Decentralized systems include peer-to-peer mesh, shared-blackboard, event-driven, and handoff-based variants, but the label 'swarm' is underspecified and may refer either to concurrent shared-state exploration or sequential handoffs.
- Sources: S30, S31, S12, S18, S23, S25
- Rationale: The sources support peer-to-peer mesh, shared-blackboard coordination, and handoff-based swarm variants. They also show that “swarm” is used inconsistently: S30 describes autonomous agents coordinating through shared state and acting simultaneously, while S12 and S25 define swarm as decentralized sequential handoffs with only one active agent. However, the supplied text does not substantiate an event-driven variant, so the complete list of variants and therefore the full claim is only partially supported.
- Supporting text: S30 describes swarm agents as autonomous peers using shared state and says they “typically share a blackboard” and use handoff protocols. S12 and S25 characterize swarm as sequential control transfer: “only one agent can be active at any given time.” S30/S18 also distinguish mesh as “direct peer-to-peer communication.”

#### F8: PARTIALLY_SUPPORTED

- Claim: Debate, verifier-critic, and critic-refiner systems form a quality-oriented interaction family distinct from task decomposition and throughput-oriented collaboration.
- Sources: S1, S11, S14, S4, S5
- Rationale: The saved sources clearly support the quality-oriented and interaction distinctions for debate and verifier-critic systems, and contrast them with decomposition-oriented supervisor/orchestrator patterns and parallel or efficiency-oriented collaboration. However, the cited content does not explicitly describe a “critic-refiner” system or establish that all three form a named interaction family. S4 contains no relevant usable passage in the saved excerpt, and S5’s free excerpt does not discuss critic-refiners.
- Supporting text: S1 identifies a “multi-agent competitive and adversarial” quadrant as involving “tension or critique” and says it is used “for quality and safety improvement, not parallel work”; it describes debate and verifier-critic. S11 says Debate is for “high accuracy, critical thinking, or objective evaluation,” while hierarchical supervision decomposes goals into subtasks and sequential pipelines minimize token overhead. S14 distinguishes debate from supervisor: debate sends the same question to multiple agents for disagreement and adjudication, whereas supervisors delegate non-overlapping tasks; it also describes debate as “multi-perspective critique.”

#### F9: SUPPORTED

- Claim: Architecture choice should be conditioned primarily on task structure: independent subtasks favor fan-out or suitable decentralized execution; strict dependencies favor pipelines; dynamic routing and conflict resolution favor supervisors; repeated quality concerns favor verification or debate; and simple sequential work may favor a single-agent graph or deterministic workflow.
- Sources: S11, S12, S17, S18, S22, S23, S25, S27, S29
- Rationale: The saved sources collectively support the claim’s decision framework. They explicitly tie pattern selection to task structure, recommend parallel fan-out for independent subtasks, sequential pipelines for strict dependencies, and supervisors for dynamic routing, ordering, validation, and conflict resolution. They also describe debate/review patterns for accuracy and quality control, and single-agent graphs or deterministic workflows for simpler, well-scoped sequential work. The wording is a concise synthesis rather than a verbatim rule, but all important components are materially supported.
- Supporting text: S12 states that architecture depends on task interdependency: swarms fit independent workloads, while supervisors fit dynamic routing, ordered execution, and conflict resolution. S17 says pipelines work when tasks have strict dependencies and parallel fan-out when subtasks are independent. S11 describes debate as effective for high-accuracy evaluation, fact-checking, and code review. S23 says single-agent graphs suit simpler, well-scoped workflows, while deterministic or rules-based workflows may be preferable when an agent is unnecessary.

#### F10: PARTIALLY_SUPPORTED

- Claim: Reliable systems require an assurance layer spanning typed contracts, bounded budgets, termination rules, timeouts, retries or fallbacks, observability, provenance, access control, and policy enforcement.
- Sources: S5, S3, S2, S8
- Rationale: The sources collectively support many elements of the claim: typed contracts/interfaces, execution or token budgets, termination policies, timeouts, fallbacks, observability, access control, and runtime policy enforcement. However, they do not clearly establish the full universal claim that reliable systems require every listed element, and provenance is not meaningfully supported in the supplied excerpts. Retries are mentioned as a runtime capability or ad-hoc practice, but not clearly presented as a required assurance-layer component.
- Supporting text: S5 describes production reliability as requiring “bounded execution budgets” and “fine-grained access control,” and gives strict JSON-schema contracts, timeout budgets, and deterministic fallback handling. S3 identifies “typed contracts,” “observability,” “reproducibility,” governance, and policy enforcement as production mechanisms. S2 lists runtime “retries” and “termination policy,” plus typed tools, observability, and guardrails. S8 identifies error detection and recovery and warns that systems can “loop without termination.”

#### F11: SUPPORTED

- Claim: The principal research problem is not merely individual-agent capability but system-level coordination: inconsistent shared state, duplicated work, contradictions, routing errors, context loss, nontermination, and error propagation.
- Sources: S8, S5, S12, S22, S23, S30
- Rationale: The sources collectively support the claim’s central contrast between individual-agent capability and system-level coordination, and substantiate each listed issue: inconsistent shared state, duplicated work, contradictions, routing failures, context loss, nontermination, and cascading/error propagation. S8 states that coordination failures are distinct from individual model errors and identifies duplicated effort, contradictions, and inconsistent shared state. S5, S12, S23, and S30 provide additional evidence for routing failures, context drift/loss, loops, and cascading errors.
- Supporting text: S8: Without orchestration, systems may “duplicate effort, contradict one another, or loop without termination”; coordination failures are distinct from individual model errors. S5: uncoordinated agents cause “compounding error loops,” with supervisor routing failures and cascading token/error risks. S12: mismatched architectures can produce contradictory outputs, unexpected routing, context loss across handoffs, and infinite re-dispatch cycles. S23: handoffs can cause context drift/loss. S30: orchestration determines fault tolerance and debugging complexity; swarms face observability, ordering, and termination challenges.

#### F12: SUPPORTED

- Claim: Evaluation should measure more than final answer accuracy: outcome correctness, repeated-trial reliability, latency, token or monetary cost, safety and policy compliance, robustness to stateful interaction, and coordination-specific failures are all needed.
- Sources: S19, S21, S8, S3
- Rationale: The cited sources collectively support the claim's main components. S19 distinguishes outcome-based evaluation from output-text matching and explicitly discusses repeated-trial reliability, while noting that latency, cost, and safety are often omitted. S21 supports measuring score alongside latency and cost, and describes stateful database evaluation, policy following, coordination, and pass^k reliability. S8 identifies state management, error handling, token cost, and coordination failures as multi-agent evaluation concerns. S3 supports evaluation and production requirements involving persistent state, governance, observability, reproducibility, reliability, security, and coordination failure modes.
- Supporting text: S19: Benchmarks commonly score whether the environment ends in the correct state rather than matching output text; pass^k measures consistency across repeated trials; benchmarks often omit cost, latency, and safety. S21: production decisions require balancing score, latency, and cost; Tau-bench checks resulting database state and policy adherence, while Tau2-bench tests coordination under partial observability. S8: the survey compares systems on state management and token cost and identifies coordination failures as distinct from individual model errors. S3: production architectures require persistent state, runtime governance, observability, reproducibility, and attention to reliability and security.

#### F13: SUPPORTED

- Claim: The strongest available architecture-level benchmark evidence is narrow and implementation-sensitive: a LangChain modified τ-bench experiment compared single-agent, swarm, and supervisor systems using one model and distractor domains, reporting a sharp single-agent decline with added irrelevant context and a slight swarm advantage over supervisor.
- Sources: S25, S26
- Rationale: The saved sources describe experiments on a modified τ-bench dataset using three architectures—single agent, swarm, and supervisor—with gpt-4o for all experiments. They used added unrelated environments as distractors and the first 100 retail test examples. The reported results say the single-agent baseline falls off sharply with two or more distractor domains and that swarm slightly outperforms supervisor. The implementation and setup are explicitly specific to LangGraph packages, one model, and this benchmark configuration, supporting the claim’s narrow, implementation-sensitive characterization.
- Supporting text: The source says the experiments used a modified τ-bench dataset, added six unrelated environments as “distractors,” tested the first 100 retail test examples, and used `gpt-4o` for all three architectures. It reports that the “single agent baseline falls off sharply” with two or more distractor domains and that “the swarm architecture slightly outperforms supervisor architecture across the board.”

#### F14: PARTIALLY_SUPPORTED

- Claim: A financial-document benchmark may provide broader evidence about cost-accuracy trade-offs, but its reported numerical findings remain provisional in the accumulated state.
- Sources: S32, S34, S33, S35, S36, S37
- Rationale: S32 directly describes a financial-document benchmark measuring cost and accuracy and reports numerical trade-offs. However, the supplied sources do not establish that the findings are provisional; S34 is largely bibliographic, and S33/S35/S36/S37 provide only fragmentary references without evidence about evidentiary status or validation. The wording “may provide broader evidence” is also more qualified than the source’s direct claim that the benchmark provides guidance.
- Supporting text: S32 reports a systematic benchmark on 10,000 SEC filings measuring field-level F1, accuracy, latency, and cost, including reflexive architectures with F1 0.943 at 2.3× sequential cost and hierarchical architectures with F1 0.921 at 1.4× cost.

### Missing Citations

- Q25: A peer-reviewed, source-grounded canonical taxonomy covering topology, workflow, concurrency, interaction objective, communication, state, and control layers is still missing.
- Q27: Controlled cross-architecture comparisons against strong single-agent and deterministic baselines are missing across the listed multi-agent patterns.
- Q28: The field lacks a reproducible evaluation contract combining outcome success, pass^k reliability, latency, cost, safety, policy compliance, coordination failures, and recovery behavior.
- Q29: It remains unclear when multi-agent coordination becomes worthwhile as tool count, context size, task length, specialization, or parallelism increases.
- Q30: The relative contributions of topology, context partitioning, prompt design, model routing, handoff semantics, translation layers, caching, retries, and framework implementation have not been isolated.
- Q32: Evidence is limited for debate, verification, blackboard, mesh, and decentralized systems outside selected task settings.
- Q33: Open security and governance questions include inter-agent privilege boundaries, prompt injection, privacy, provenance, collusion, unauthorized tool actions, and auditable shared state.

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
2. R5: Provide an interpretable visual taxonomy or design graph showing the major patterns, their relationships, and relevant cross-cutting overlays.
3. R3: Analyze design dimensions that cut across architectural patterns and explain their consequences.
4. 6 cited finding(s) were not fully supported by saved evidence.
5. 7 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `3ba296f97ad2c98be185e194bbae89b363b2bc81a38fd31abf5dbf056e9a34b0`
- Candidate report hash: `10801843f833b1dd97fb855d5337bff9f18c20a60fe6ae561b511c9f844f8060`
- LLM calls: 16
- Evaluated at: 2026-09-01T09:23:37.512529+00:00
