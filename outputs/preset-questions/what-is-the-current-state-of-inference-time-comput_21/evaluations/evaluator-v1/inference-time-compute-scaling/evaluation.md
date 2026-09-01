# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** inference-time-compute-scaling

**System Version:** evidence-ledger-decomposer-v1

**Research Model:** gpt-4o-mini

**Evaluator Model:** gpt-5.6-luna

## Summary

- Overall: 37.5 / 100
- Evaluation completeness: 100%
- Coverage: 0.41
- Depth: 0.34

## Coverage and Depth

### R1

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report gives scattered examples of methods and notes that weights are not changed, but it does not establish the requested scope or taxonomy.
- Candidate evidence:
  - The report describes inference-time scaling as generating “multiple candidates and select[ing] the best” and mentions “adaptive reasoning lengths,” “sampling and selection,” and “tree search.”
  - Finding 3 states that inference-time scaling improves performance “without altering model weights.”
- Missing:
  - No explicit definition of inference-time compute scaling as a general allocation of computation during inference.
  - Serial reasoning, parallel sampling, search, verification, refinement, tool use, and adaptive budgeting are not systematically distinguished.
  - No clear contrast with training changes, larger model size, or merely adding input context.
  - No discussion of debatable boundaries, such as retrieval, tools, or context expansion.

### R2

- Coverage: 0.50
- Depth: 0.25
- Rationale: There is a broad positive synthesis and a few comparative claims, but little of the controlled-evidence detail needed to assess empirical validation.
- Candidate evidence:
  - The report claims that “Inference-time scaling can improve LLMs' performance” and cites extended reasoning, compute-optimal inference, Quiet-STaR, multilingual sampling, and AB-MCTS.
  - It reports that “Llemma-7B often provides similar or better performance compared to Llemma-34B with halved compute.”
  - It notes that “optimal thinking lengths vary across problem difficulties.”
- Missing:
  - No controlled comparisons are presented with numerical effect sizes, sample sizes, confidence intervals, or variance.
  - Models, tasks, baselines, and inference budgets are generally unspecified.
  - The report does not separate replicated results from isolated or promotional benchmark results.
  - It does not synthesize where gains are reliable versus where they fail, and several cited claims are only asserted through source IDs.

### R3

- Coverage: 0.50
- Depth: 0.50
- Rationale: Several mechanisms and two important failure modes are named, but the required comparative mechanistic analysis is incomplete.
- Candidate evidence:
  - The report separately mentions extended/serial reasoning, generating multiple candidates, sampling and selection, adaptive reasoning lengths, and AB-MCTS tree search.
  - It identifies “overthinking,” including “abandoning correct answers,” and says models “amplify errors when they self-condition on prior mistakes.”
  - It characterizes AB-MCTS as balancing “exploration and exploitation” and dynamically combining candidate generation with answer refinement.
- Missing:
  - Verification is not treated as a distinct mechanism, and refinement is only briefly implicit in AB-MCTS.
  - Repeated sampling, aggregation, search, and serial reasoning are not compared under common conditions.
  - The report does not explain correlated samples, verifier unreliability, error propagation, or when each mechanism succeeds or fails.
  - Evidence for the mechanisms is mostly conclusory, without ablations or quantitative comparisons.

### R4

- Coverage: 0.75
- Depth: 0.50
- Rationale: The qualitative characterization of diminishing and sometimes negative returns is reasonably present, but the evidence is not quantified or broad enough for a strong scaling-behavior assessment.
- Candidate evidence:
  - The report repeatedly describes “diminishing returns” and says extended reasoning can produce worse outcomes through “overthinking.”
  - It states that “optimal thinking lengths vary across problem difficulties,” supporting task-dependent scaling.
  - It reports that Quiet-STaR shows improvement “at a high compute cost” while performance “may plateau,” and that long-horizon execution exhibits increasing per-step error rates.
- Missing:
  - No actual scaling curves, fitted relationships, or budget ranges are provided.
  - Variation by model capability, task type, and strategy is only partially addressed.
  - The report does not clearly distinguish monotonic gains followed by saturation from genuine degradation across broad settings.
  - It does not explicitly caution that no universal functional scaling law is established.

### R5

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report gestures at compute cost and a model-size trade-off but does not evaluate efficiency rigorously.
- Candidate evidence:
  - Finding 6 claims that Llemma-7B can match or outperform Llemma-34B “with halved compute.”
  - Finding 7 describes “a high cost in terms of compute resources.”
  - Finding 3 frames inference-time scaling as improving performance “without retraining.”
- Missing:
  - No specified accounting of tokens, FLOPs, latency, throughput, energy, or monetary cost.
  - The Llemma comparison lacks matched conditions, quality metrics, and deployment assumptions.
  - No systematic comparison with larger models, fine-tuning, distillation, retrieval, or other alternatives.
  - No analysis of when additional inference is preferable under realistic service constraints.

### R6

- Coverage: 0.25
- Depth: 0.25
- Rationale: A few domains are named, but transferability and coverage of the requested task landscape are largely unassessed.
- Candidate evidence:
  - It mentions “multilingual tasks,” “complex coding tasks,” ARC-AGI-2, long-horizon execution, and political persuasion.
  - Finding 4 claims gains “across diverse languages and tasks.”
- Missing:
  - No structured distinction between mathematics/STEM, coding, knowledge-intensive, open-domain, planning, interactive/tool-use, ambiguous, or safety-relevant workloads.
  - No assessment of synthetic versus naturalistic data or benchmark-to-real-world transfer.
  - No comparison of proprietary and open models, despite AB-MCTS involving multiple frontier models and Llemma examples involving open models.
  - The report does not evaluate whether the cited effects transfer beyond the specific benchmarks.

### R7

- Coverage: 0.25
- Depth: 0.25
- Rationale: Some gaps are acknowledged, but evidence-quality criticism is minimal and the high-confidence framing is not justified by the report's sparse details.
- Candidate evidence:
  - The report identifies “substantial gaps,” including uncertainty about “thresholds of performance limitations” and “optimal reasoning lengths.”
  - It lists open questions about model-size effects in long-horizon tasks and integrating methods to mitigate degradation.
  - The “Conflicts and Uncertainty” section says, “No material conflict was identified,” while also noting that eight uncertainty items were omitted for lack of source IDs.
- Missing:
  - No analysis of replication, study independence, benchmark contamination, prompt and dataset limitations, selective reporting, or weak baselines.
  - No discussion of proprietary-model access or incomplete compute accounting.
  - The report labels several strong claims “High” confidence without showing evidence quality or uncertainty.
  - It does not clearly separate established findings, conditional interpretations, and speculative extrapolations.
  - It does not identify what experiments or data would resolve the open questions, nor adequately mark domains where evidence is too thin.

### R8

- Coverage: 0.50
- Depth: 0.50
- Rationale: The conclusion is directionally balanced, but it remains generic and more confident than the supplied evidence warrants.
- Candidate evidence:
  - The conclusion says there is “robust support for the benefits of inference-time scaling” while acknowledging “substantial gaps,” especially around performance limits and optimal reasoning lengths.
  - The report repeatedly qualifies benefits with “diminishing returns” and possible performance degradation, and identifies adaptive strategies as unresolved.
- Missing:
  - The conclusion is not sufficiently conditional about which tasks, models, mechanisms, and budgets support the claimed benefits.
  - It does not clearly identify specific domains or claims for which evidence is too thin to conclude.
  - It does not synthesize the relative status of serial reasoning, sampling, search, verification, refinement, and adaptive allocation.
  - The broad assertion of “robust support” is not reconciled with the report's lack of quantitative comparisons and evidence-quality analysis.

### Novel Value

- No material benchmark-external value identified.

## Deterministic Diagnostics (Not Scored)

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
- `structured_claim_evidence_available`: PASS
- `ledger_claim_ids_unique`: PASS
- `ledger_evidence_relationships_resolve`: PASS
- `ledger_confidence_values_valid`: PASS
- `ledger_evidence_ids_unique`: NOT_EVALUABLE — Current ledger relations have no independent evidence-ID field.

## Main Weaknesses

1. R1: Define inference-time compute scaling and distinguish its main forms from adjacent interventions.
2. R5: Evaluate inference scaling against realistic resource constraints and alternatives.
3. R6: Assess how well reported inference-scaling effects transfer beyond the settings in which they were measured.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `d32d6ea1035324f019e9421c7b216e4501bdab866df8e60cda19db2afb8a4c2f`
- Candidate report hash: `f41596c8911d8adec46da55b393bb5efe18b27a8f4802c1b43db311d04ef7985`
- LLM calls: 1
- Evaluated at: 2026-09-01T17:52:13.081305+00:00
