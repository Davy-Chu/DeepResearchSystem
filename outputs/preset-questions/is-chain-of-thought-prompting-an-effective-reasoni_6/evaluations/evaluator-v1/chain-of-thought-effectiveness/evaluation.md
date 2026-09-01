# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** chain-of-thought-effectiveness

**System Version:** llm-only-baseline-v0

**Model:** gpt-5.6-luna

## Summary

- Overall: 56.9 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.78
- Coverage: 0.78
- Depth: 0.78
- Citation quality: 0.00
- Citation validity: 0.00
- Citation support: 0.00
- Citation completeness: 0.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report establishes the main intervention and distinguishes most relevant neighboring methods, but the comparison taxonomy could be more explicit and systematic.
- Candidate evidence:
  - The report defines few-shot CoT as examples containing “reasoning steps,” zero-shot CoT as “Let’s think step by step,” and distinguishes scratchpads, self-consistency, program-of-thought, tool augmentation, and hidden or latent reasoning.
  - It explicitly states that “a visible explanation is not automatically a causal trace” and contrasts CoT with direct-answer prompting in the proposed controls.
- Missing:
  - Direct answering is discussed mainly as a baseline rather than explicitly defined as the comparison intervention.
  - The report does not clearly distinguish CoT from every other inference-time procedure, such as generic verbosity or beam search, in the initial conceptual framing.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: It covers the required task diversity and avoids a single-benchmark generalization, but empirical detail is uneven and strongest for mathematical or symbolic tasks.
- Candidate evidence:
  - It discusses arithmetic and symbolic tasks, including GSM8K and multistep multiplication, and reports that CoT often produces strong gains there.
  - It separately covers commonsense reasoning, knowledge-intensive questions, planning, logic, constraint satisfaction, and multiple-choice tasks, noting mixed results and possible harms such as hallucination or overthinking.
  - It states that direct-answer prompting can perform nearly as well on easy, retrieval-like, or familiar-template tasks.
- Missing:
  - Evidence for open-ended reasoning is relatively thin; the discussion is mostly categorical rather than reporting concrete studies or metrics across open-ended tasks.
  - The report gives few specific comparative results beyond the general claim about PaLM/GSM8K.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The major moderators are all addressed and connected to conflicting results, but the evidential status and quantitative support for individual moderators are limited.
- Candidate evidence:
  - It identifies model scale, parameter count, pretraining, instruction tuning, context length, and decoding as moderators, stating that larger models generally use extra tokens more effectively.
  - It discusses task decomposition, difficulty, task structure, distribution similarity, benchmark familiarity, out-of-distribution composition, prompt wording, demonstrations, and direct-answer baselines.
  - It explains that demonstrations teach parsing, operations, solution structure, and output format, so CoT/no-CoT comparisons may not be information-matched.
- Missing:
  - The report often presents moderators as broad tendencies without separating well-established findings from contested or under-tested ones.
  - It does not provide much study-level evidence showing how each moderator changes effect size.

### R4

- Coverage: 1.00
- Depth: 1.00
- Rationale: This requirement is treated in substantial mechanistic and experimental detail, including the distinction between improved outcomes and faithful displayed reasoning.
- Candidate evidence:
  - The report distinguishes serial computation, scratchpad/context effects, representation change, latent activation steering, search and aggregation, and formatting or benchmark-compliance effects.
  - It explicitly says that “accuracy improvements and explanation faithfulness must be evaluated separately” and that a correct final answer can coexist with an invalid or post hoc explanation.
  - It proposes format-matched controls, hidden scratchpads, executable programs, chain perturbations, and counterfactual tests to separate mechanisms.
- Missing:

### R5

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report clearly separates the prompt intervention from added sampling, computation, tools, extraction, and verification, and recommends like-for-like controls.
- Candidate evidence:
  - It separately defines single-chain CoT, self-consistency, verifier-guided search, and tool use, warning that gains from sampling many solutions should not automatically be attributed to CoT.
  - It discusses greedy decoding, temperature sampling, beam search, voting, calculators, code execution, retrieval, symbolic solvers, and external verification.
  - It recommends comparing direct answer, CoT, hidden scratchpad, structured decomposition, and executable-program conditions with matched token budgets, demonstrations, and output formats.
- Missing:

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: It identifies the right validity and causal tests and acknowledges that accuracy is not faithfulness, but the literature assessment remains mostly high-level.
- Candidate evidence:
  - It defines the faithfulness problem as whether the chain is “the actual causal basis of the answer” or a post hoc rationale.
  - It cites Turpin et al. and Lanham et al. on explanations being influenced by irrelevant features and not always causally necessary.
  - It proposes deleting, replacing, negating, reordering, or contradicting intermediate steps, plus counterfactual, adversarial, execution-validity, and step-level correctness tests.
- Missing:
  - The report summarizes cited findings but gives limited methodological detail about their exact tasks, intervention results, or limitations.
  - It does not deeply distinguish logical validity, causal faithfulness, and fidelity under distribution shift using concrete comparative evidence.

### R7

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report understands the comparability problem and names many relevant dimensions, but it does not perform the evidence-quality audit required to explain disagreements from documented study-level differences.
- Candidate evidence:
  - It warns that results are not directly comparable when studies differ in parameter count, pretraining, instruction tuning, context length, demonstrations, decoding, sampling, and aggregation.
  - It notes contamination, benchmark familiarity, exact-match scoring, and the need for calibration, process metrics, perturbation robustness, and replication-like checks.
  - It cites major research programs including Wei, Kojima, Wang, Nye, Turpin, Lanham, Lightman, PAL, and related work.
- Missing:
  - It does not systematically report model versions or sizes, datasets, baselines, decoding settings, metrics, uncertainty, effect-size variation, or replication status for the cited studies.
  - Several claims about “subsequent work,” contamination, and limits are not tied to specific sources or documented comparisons.
  - The selected references are not critically evaluated for source quality, scope, or reproducibility, and one citation is visibly malformed: “改? Measuring Faithfulness...”.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The synthesis is strong and directly answers the question, but the requested practical treatment of cost and latency is incomplete.
- Candidate evidence:
  - The conclusion directly rejects both extremes: CoT is “not merely a formatting trick,” but visible chains are not reliably faithful transcripts.
  - It gives a qualified synthesis involving serial computation, representation change, latent-mode activation, search, and formatting effects, and distinguishes eliciting useful computation from faithful, generalizable reasoning.
  - It provides practical guidance about when CoT helps, when tools or verifiers are needed, and the risks of hallucination, novel distributions, exact arithmetic, and high-stakes use.
- Missing:
  - Cost and latency implications are only implicit through longer generation and multiple samples; the report does not explicitly analyze their operational tradeoffs.
  - Reliability implications are discussed, but there is limited concrete guidance on calibration, abstention, or when the accuracy gain justifies added computation.

### Novel Value

- The report offers a useful synthesis that separates final-answer accuracy, computational usefulness, faithfulness, generalization, and calibration rather than treating them as one claim.
- Its central framing of CoT as an “external control interface” combining scratchpad, representation, latent steering, search, and formatting mechanisms is a substantive integrative perspective.

## Citations

### Support

### Missing Citations

- Q1: Chain-of-thought prompting can substantially improve task performance when the model has relevant knowledge and competence and the task benefits from decomposition.
- Q2: Observed CoT gains can arise from improved problem representation, search, and answer selection rather than from the written chain faithfully recording the computation that produced the answer.
- Q3: Wei et al. (2022) reported gains from few-shot CoT prompting on arithmetic, symbolic, and commonsense reasoning tasks, especially for sufficiently large language models.
- Q4: Kojima et al. (2022) found that the instruction “Let’s think step by step” improved performance on several reasoning benchmarks without demonstrations.
- Q5: Nye et al. (2021) showed that training models to produce intermediate computations improved performance on algorithmic tasks.
- Q6: Wang et al. (2022) improved CoT accuracy by sampling multiple reasoning paths and selecting the modal final answer.
- Q7: Program-of-thought methods generate executable code and often outperform ordinary CoT on numerical tasks because execution handles arithmetic and state updates more reliably.
- Q8: Intermediate autoregressive tokens can provide additional computational bandwidth and function as external memory, decomposition scaffolds, variable or subgoal representations, and partial search traces.
- Q9: PaLM’s performance on GSM8K rose dramatically with CoT prompting.
- Q10: CoT gains are sometimes preserved under paraphrase and answer-format controls, and short final-answer constraints after hidden or external reasoning can retain benefits.
- Q11: Self-consistency can improve accuracy through search and aggregation without establishing that any individual chain is faithful.
- Q12: CoT can induce useful intermediate representations such as equations, entities and relations, constraints, subgoals, or executable code.
- Q13: Turpin et al. (2023) found that CoT explanations can be influenced by irrelevant prompt features and may rationalize decisions rather than transparently report the computation that generated them.
- Q14: Lanham et al. (2023) found, using interventions such as removing or changing chain steps, that visible CoT is often not fully causally necessary or faithful.
- Q15: Process-supervision and verifier-based studies found that rewarding step-by-step explanations can improve outcomes, while models may still exploit superficial patterns or produce plausible-looking incorrect processes.
- Q16: Direct-answer prompting performs nearly as well as CoT on some benchmarks, while CoT can harm performance on simple factual, adversarial, or ambiguous tasks.
- Q17: CoT is vulnerable to lexical cues, answer-position biases, surface templates, benchmark formats, and other spurious correlations, and some gains disappear when such regularities are controlled.
- Q18: CoT gains are less consistent for novel combinations, systematic generalization, and distribution shifts than for benchmark tasks close to pretraining or demonstration patterns.
- Q19: The original CoT effect was strongly associated with model scale, and smaller models often have greater difficulty maintaining coherent multistep reasoning.
- Q20: CoT effectiveness varies by task type: it often helps arithmetic and symbolic tasks, has mixed effects on commonsense tasks, may increase hallucination on knowledge-intensive questions, and is error-prone for planning and long constraint tracking.
- Q21: Prompt wording, demonstrations, decoding methods, sampling, self-consistency, and verifier use can substantially change the apparent effect attributed to CoT.
- Q22: Many papers attribute gains to CoT even when the intervention also includes sampling many solutions and aggregating them, which constitutes a search procedure rather than merely a formatting instruction.
- Q23: Benchmark contamination or familiarity with questions, paraphrases, and solution templates can weaken claims that CoT performance demonstrates novel reasoning.
- Q24: Exact-match scoring gives full credit to correct answers paired with invalid chains, lucky answers, or fabricated explanations, so process-aware metrics are needed.
- Q25: Nye et al. (2021) provides relatively strong evidence that intermediate sequences can be computationally substantive, while trained scratchpads differ from zero-shot natural-language rationales.
- Q26: Turpin et al. (2023), Lanham et al. (2023), and related faithfulness studies show that verbalized reasoning is often not a reliable explanation of the internal decision process.
- Q27: Lightman et al. (2023) found that supervising intermediate steps can improve mathematical reasoning relative to outcome-only supervision.
- Q28: Generating executable programs or using calculators often produces larger and more dependable gains on formal tasks than free-form CoT.
- Q29: Reversal, novel-symbol, and compositional-generalization studies find that language models often struggle when familiar surface associations are removed.

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
2. 29 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ac152f1d42cbe0f247f27e3225b834f4d7d35d3a27bade4d08806b371c248b6d`
- Candidate report hash: `6c7b6c2066ee75cdc903faa7954209fc0777ccfdfa1017baef6dd1972e2fd57a`
- LLM calls: 2
- Evaluated at: 2026-09-01T01:00:58.572562+00:00
