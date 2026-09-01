# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** chain-of-thought-effectiveness

**System Version:** llm-only-baseline-v0

**Model:** gpt-5.6-luna

## Summary

- Overall: Unavailable
- Evaluation completeness: 80%
- Comprehensiveness: 0.84
- Coverage: 0.84
- Depth: 0.84
- Citation quality: Unavailable
- Citation validity: 0.00
- Citation support: 0.00
- Citation completeness: Unavailable
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report establishes the main intervention and separates several related procedures, but its taxonomy does not fully and explicitly distinguish all required comparison conditions.
- Candidate evidence:
  - The report defines few-shot CoT, zero-shot CoT, and scratchpads as interventions involving intermediate reasoning or computation.
  - It explicitly distinguishes self-consistency, tree or graph search, process supervision, and externalized reasoning, stating that “these are not equivalent.”
  - It notes that visible rationales are not necessarily the model’s internal reasoning process.
- Missing:
  - Direct answering is discussed implicitly as the alternative to CoT, but it is not explicitly defined as a comparison condition.
  - The distinction between externally displayed CoT and hidden or internal reasoning is present but not developed as a separate intervention category.
  - Answer-format instructions are discussed later, but not clearly separated in the initial conceptual definition.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: It covers multiple task classes and avoids a single-benchmark generalization, but evidence for knowledge and open-ended tasks is less concrete than evidence for mathematics, algorithms, and symbolic reasoning.
- Candidate evidence:
  - The report cites gains from Wei et al. on “arithmetic, commonsense, and symbolic reasoning benchmarks.”
  - It discusses algorithmic scratchpads, arithmetic, symbolic tasks, compositional tasks, multi-hop tasks, and real-world reasoning.
  - It states that CoT can help on multistep tasks but can fail or hurt on simple, ambiguous, adversarial, or knowledge-limited tasks.
- Missing:
  - Knowledge-intensive and open-ended reasoning are treated mainly through general discussion of retrieval and real-world reasoning rather than through concrete empirical findings or named studies.
  - The report does not systematically compare CoT effects across task families using specific results, null effects, or harms.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report gives a broad and useful moderator framework that directly explains disagreement, but it provides limited evidence grading and study-by-study support for the individual moderators.
- Candidate evidence:
  - The report identifies model scale as a moderator, citing Wei et al.’s finding that CoT had little or negative effect in smaller models and stronger effects at larger scales.
  - It discusses task structure, decomposition, verification difficulty, and whether a task genuinely requires intermediate computation.
  - It identifies training-distribution similarity, instruction tuning, exposure to worked solutions, prompt wording, demonstrations, context length, decoding temperature, language, and domain as relevant factors.
  - It compares direct answering, single-chain CoT, and self-consistency, and explains that CoT can be harmful when the task is simple or the model lacks competence.
- Missing:
  - The report does not clearly classify which moderators are firmly established, contested, or insufficiently tested.
  - Several moderators, especially training-distribution similarity, prompt design, and baseline behavior, are asserted as plausible influences without detailed comparative evidence across studies.

### R4

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report directly evaluates reasoning, verbosity, formatting, extraction, and combined mechanisms, while distinguishing improved outcomes from faithful causal explanation and proposing tests that separate them.
- Candidate evidence:
  - The report separates “accuracy versus faithful explanation” and states that a visible rationale is not necessarily the causal process producing the answer.
  - It proposes mechanisms including increased effective computation, decomposition, external memory, search, instructional alignment, formatting, and answer extraction.
  - It explicitly says some gains may come from “better compliance with answer-format instructions,” “reducing premature answer emission,” and easier extraction.
  - It proposes controlled comparisons involving free-form CoT, meaningless equal-length tokens, structured variables, code execution, and rationales fed back to the model.
- Missing:

### R5

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report repeatedly warns against attributing gains from sampling, voting, tools, or protocol changes to CoT alone and provides relevant comparison designs. Although it does not report many concrete like-for-like numerical comparisons, the conceptual and methodological separation is comprehensive.
- Candidate evidence:
  - The report explicitly distinguishes single-sample CoT from self-consistency, tree search, and other forms of inference-time search.
  - It states that self-consistency gains may result from sampling multiple solutions and majority voting rather than from one faithful chain.
  - It discusses code, calculators, retrieval, tools, verifiers, and ReAct-like external scaffolding as distinct from natural-language CoT.
  - Its proposed controlled comparisons include direct answer, free-form CoT, equal-length meaningless tokens, structured variables, code execution, and rationale feedback.
- Missing:

### R6

- Coverage: 1.00
- Depth: 1.00
- Rationale: It directly addresses both logical/process validity and causal relevance, distinguishes faithfulness from accuracy, and describes appropriate intervention and distribution-shift tests.
- Candidate evidence:
  - The report cites Turpin et al. and Lanham et al. as evidence that rationales can be unfaithful, post-hoc, or causally irrelevant.
  - It distinguishes final-answer accuracy from faithfulness and notes that models can retain answers when rationales are removed or altered and can accept misleading steps.
  - It recommends modifying, removing, or replacing intermediate steps; counterfactual interventions; process-level scoring; robustness to misleading demonstrations; and compositional generalization.
- Missing:

### R7

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report identifies important comparability threats and cites relevant literature, but it does not perform the detailed evidence-quality and protocol comparison required for strong coverage.
- Candidate evidence:
  - The report names major studies and methods, including Wei et al., Kojima et al., Wang et al., Nye et al., Turpin et al., Lanham et al., and Lightman et al.
  - It warns about training overlap, memorization, repeated templates, answer-position biases, synthetic regularities, and leakage.
  - It notes that task structure, model scale, instruction tuning, context length, temperature, prompt wording, language, and domain affect outcomes.
- Missing:
  - It does not provide concrete model versions or sizes, datasets, baselines, decoding settings, metrics, uncertainty estimates, or replication results for the cited studies.
  - It does not systematically assess source quality or explain which reported results are directly comparable and which are not.
  - Claims about the literature are largely presented without numerical results, study limitations, or independent replication evidence.

### R8

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report directly answers the central question with a qualified synthesis and gives practical implications for accuracy, reliability, cost, latency, and appropriate deployment.
- Candidate evidence:
  - The executive conclusion states that CoT is neither merely formatting nor uniformly reliable, and characterizes it as context-dependent inference-time computation.
  - The final assessment separates outcome, mechanism, faithfulness, and generalization, concluding that CoT often improves accuracy, plausibly contributes through computation and search, is unreliable as a faithful explanation, and remains task-dependent.
  - The practical guidance addresses when to use CoT, when to prefer direct answers, and when to use calculators, code, formal solvers, retrieval, verifiers, or process supervision.
  - It explicitly discusses token cost, latency, reliability, error accumulation, false confidence, and output parsing.
- Missing:

### Novel Value

- The report’s most useful synthesis is its separation of four often-conflated dimensions: outcome, mechanism, faithfulness, and generalization.
- It frames CoT as an inference-time interface that can provide computation, memory, decomposition, or search without making the visible trace a faithful transcript.
- It identifies formatting, extraction, benchmark artifacts, scale, task structure, and protocol differences as joint explanations for apparently conflicting literature.

## Citations

### Support

### Missing Citations

- None identified.

## Deterministic Checks

- `run_metadata_loads`: PASS
- `report_exists`: PASS
- `sources_present`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `structured_report_parses`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `report_question_matches`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `source_ids_unique`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `source_ids_syntactically_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `source_urls_present`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `evidence_objects_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `confidence_values_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `citation_ids_syntactically_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `citation_ids_resolve`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `structured_claim_evidence_available`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `ledger_claim_ids_unique`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `ledger_evidence_relationships_resolve`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `ledger_confidence_values_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `ledger_evidence_ids_unique`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.

## Main Weaknesses

1. R7: Evaluate the evidential strength and comparability of the cited literature, including model versions and sizes, datasets, baselines, prompt protocols, decoding settings, metrics, uncertainty, replication, and source quality.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ac152f1d42cbe0f247f27e3225b834f4d7d35d3a27bade4d08806b371c248b6d`
- Candidate report hash: `f77b77426a8b3113912734d448e721255758a2fa02239f754dab3968bca4c8bd`
- LLM calls: 4
- Evaluated at: 2026-08-31T23:42:08.800369+00:00
