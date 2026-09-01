# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** chain-of-thought-effectiveness

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 82.6 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.71
- Coverage: 0.72
- Depth: 0.69
- Citation quality: 1.00
- Citation validity: 1.00
- Citation support: 1.00
- Citation completeness: 1.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report provides useful conceptual distinctions, but the intervention and comparison conditions are not defined comprehensively enough for full credit.
- Candidate evidence:
  - The report distinguishes “few-shot rationale demonstrations, a generic step-by-step instruction, extra serial computation, or process-aware search” as different interventions.
  - It contrasts “surface trace content, latent task-relevant state trajectories, and generic serial computation.”
  - It distinguishes visible CoT from “latent computation” and mentions “sampling,” “budget forcing,” and “process-aware search.”
- Missing:
  - It never gives a clear standalone definition of CoT as an inference-time prompt intervention involving intermediate natural-language reasoning steps.
  - Direct answering is not explicitly defined or used as a systematic comparison condition.
  - Answer-format instructions, hidden/internal reasoning, self-consistency or voting, tool augmentation, and other procedures are mentioned unevenly rather than cleanly distinguished from ordinary CoT.
  - The report does not explicitly warn that any verbose or stepwise output is not necessarily CoT.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report covers mathematical, commonsense, and knowledge-oriented tasks and avoids a single-benchmark generalization, but open-ended reasoning and broader task evidence are limited.
- Candidate evidence:
  - It reports gains on “multistep arithmetic and some commonsense tasks” in the original CoT work, including GSM8K.
  - It discusses GPQA, a knowledge-intensive reasoning benchmark, and reports average, mixed, or negative effects depending on model and criterion.
  - It discusses GSM8K and MATH for contemporary mathematical-reasoning models.
  - It states that CoT effects differ across “difficult multistep tasks” and identifies commonsense and knowledge-related evidence.
- Missing:
  - Open-ended reasoning is not substantively evaluated; it appears only indirectly through broad references to task types and as a proposed generalization gap.
  - The report supplies little concrete evidence for non-mathematical task families beyond commonsense and GPQA.
  - It does not systematically compare direct answering and CoT final-answer performance across the task families.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: Most major moderators are covered and connected to disagreement, but training-distribution similarity and the evidential status of several moderators are underdeveloped.
- Candidate evidence:
  - It reports CoT benefits emerging at roughly 100B-plus scale and contrasts earlier or non-reasoning models with strong reasoning-native models.
  - It identifies task dependence, especially difficult multistep mathematics, commonsense, GPQA, and model-specific budget-forcing behavior.
  - It discusses prompt and demonstration design, including few-shot rationale exemplars, zero-shot CoT, output-format alignment, filler tokens, and explicit terminal-answer formats.
  - It identifies baseline dependence: few-shot exemplars may help earlier models but add little over zero-shot CoT for recent Qwen2.5 models.
  - It states that “model generations, tasks, metrics, prompt variants, output formats, and compute budgets” account for conflicting results.
- Missing:
  - Training-distribution similarity is not directly analyzed. The report mentions a “shift in model capability and training regime,” but does not document how task or prompt similarity to pretraining or instruction-tuning data moderates CoT effects.
  - Some moderators are asserted from individual studies without a clear separation of well-supported findings from contested or insufficiently tested ones.
  - The interaction among capability, task difficulty, and baseline behavior is described more narratively than through controlled comparisons.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is one of the strongest parts of the report: it directly addresses the reasoning-versus-formatting dispute and cites relevant separating tests. Full credit is withheld because ordinary CoT mechanisms remain incompletely isolated.
- Candidate evidence:
  - The report says CoT is “not merely a formatting trick” while also arguing that few-shot exemplars can align output format rather than add reasoning capability.
  - It reports filler-token results in which “uninformative filler did not reproduce the performance gain,” arguing against a pure token-count explanation in that setting.
  - It reports answer-placement findings where sensitivity tracked terminal-answer location and models followed a wrong terminal answer over correct intermediate reasoning.
  - It explicitly distinguishes accuracy improvement from faithful explanation and separates “surface trace content, latent task-relevant state trajectories, and generic serial computation.”
  - It identifies executable symbolic reasoning, verification, repair, and selective search as mechanisms more tightly connected to computation.
- Missing:
  - The strongest positive computational evidence often concerns specialized executable or process-aware systems rather than ordinary free-form CoT, and the report acknowledges but does not resolve that limitation.
  - It does not provide a systematic like-for-like decomposition of intermediate-content effects, verbosity/extra context, formatting, and answer extraction for standard CoT.
  - It discusses causal evidence but does not fully specify which interventions establish computation versus merely dependence on textual context.

### R5

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report recognizes that inference-time computation and protocol changes can masquerade as CoT effects, but empirical separation is incomplete.
- Candidate evidence:
  - The report explicitly says different comparisons include “few-shot rationale demonstrations, a generic step-by-step instruction, extra serial computation, or process-aware search.”
  - It discusses single-path, sampling, and search baselines for CoT2-Meta and notes reported matched inference budgets.
  - It separately discusses budget forcing, selective expansion, pruning, repair, stopping, abstention, and generated length/time.
  - It identifies calculators, code, retrieval, or other external computation as unresolved comparison issues in the remaining gaps, especially whether matched budgets equalize controller, evaluator, memory, and model-computation costs.
- Missing:
  - Calculators, code, retrieval, and tool augmentation are not actually analyzed as empirical confounds; they are mainly listed as gaps or discussed only through executable reasoning.
  - Sampling and self-consistency/voting are mentioned but not carefully separated from CoT in a controlled comparison.
  - The report does not consistently provide like-for-like decoding settings, token budgets, call counts, or extraction procedures for the cited studies.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report clearly distinguishes faithfulness from accuracy and cites several appropriate intervention paradigms, but trace validity and the full range of diagnostic tests are not developed fully.
- Candidate evidence:
  - It explicitly states that visible rationales are not guaranteed to be “a faithful explanation of the causal process producing the answer.”
  - It discusses truncation, corruption, and paraphrase interventions and reports task-dependent answer changes and cases where models largely ignore displayed CoT.
  - It discusses misleading-hint studies and correctly notes that keyword analysis measures channel divergence rather than faithfulness itself.
  - It mentions CASE interventions designed to force dependence on reasoning chains and reports improved faithfulness.
  - It notes that faithfulness rates, answer sensitivity under corruption, and thinking-answer divergence are different measurements.
- Missing:
  - Logical validity of the traces themselves is not evaluated in much detail; the focus is primarily causal faithfulness and answer sensitivity.
  - Counterfactual interventions and distribution-shift evaluations are not substantively discussed beyond related corruption and misleading-hint paradigms.
  - The report does not explain how faithfulness tests distinguish dependence on a chain from dependence on a correlated or strategically formatted textual representation.

### R7

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report correctly identifies comparability as a central fault line, but it does not itself perform the detailed evidence-quality audit required by the rubric.
- Candidate evidence:
  - It repeatedly cautions that studies use different “models, tasks, and protocols.”
  - It identifies differences in “model generations, tasks, metrics, prompt variants, output formats, and compute budgets.”
  - It notes that GPQA average accuracy, majority correctness, and strict perfect-accuracy criteria yield different conclusions.
  - It identifies a GSM8K evaluation artifact that underestimated zero-shot CoT and discusses formatting-sensitive corruption protocols.
  - It acknowledges that the retrieved material lacks a unified cost-normalized comparison.
- Missing:
  - The report does not systematically document model versions and sizes, datasets, prompt wording, demonstrations, decoding settings, sample counts, metrics, or uncertainty for the cited studies.
  - Replication and confidence intervals or statistical uncertainty are largely absent despite several claims being assigned confidence levels.
  - Source quality and verifiability are not critically assessed. The source list mixes primary papers with blogs, commercial explainers, summaries, and several apparently future-dated or difficult-to-verify sources.
  - The report does not assess whether the cited studies’ protocols are directly comparable beyond broad statements that they differ.
  - Some strong conclusions rely on source labels and links without enough methodological detail for independent evaluation.

### R8

- Coverage: 1.00
- Depth: 0.75
- Rationale: The report reaches a qualified, direct, and evidence-based synthesis and covers the requested practical dimensions. Its main limitation is that the practical tradeoff analysis remains qualitative rather than cost-normalized.
- Candidate evidence:
  - The conclusion directly states that CoT is “an effective but conditional strategy—not a universal reasoning switch and not merely a formatting trick.”
  - It distinguishes clearer benefits for difficult multistep tasks and non-reasoning or earlier models from limited incremental value for strong modern reasoning-native models.
  - It recommends “format-controlled, compute-aware evaluations” and warns against treating a fluent visible chain as proof of reasoning or faithfulness.
  - It discusses accuracy, reliability, cost, latency, response time, calibration, selective prediction, repair, abstention, plateaus, and negative gains.
  - It states that process-aware search and executable reasoning may be more valuable than uniformly lengthening chains.
- Missing:
  - The practical implications are not supported by a unified quantitative accuracy–cost–latency comparison.
  - The report gives limited operational guidance about when practitioners should choose direct answering, CoT, self-consistency, tools, or process-aware methods.
  - The distinction between established findings and hypotheses is present but could be made more explicit for claims such as latent computation and model capability shifts.

### Novel Value

- The report offers a useful synthesis organized around a three-way fault line among surface CoT traces, latent task-relevant computation, and generic serial test-time computation.
- It emphasizes that formatting and terminal-answer placement can confound both performance and faithfulness measurements, rather than treating formatting as merely a superficial alternative explanation.
- It separates ordinary CoT prompting from specialized executable reasoning and process-aware search, helping explain why evidence for computational benefit may not transfer directly to free-form CoT.
- It highlights that disagreements can arise from the evaluation metric itself, including average accuracy, majority correctness, strict perfect accuracy, and format-sensitive extraction.

## Citations

### Support

#### F1: SUPPORTED

- Claim: CoT can produce substantial reasoning gains, but the gains are conditional on model generation, task, and baseline capability.
- Sources: S22, S1, S30
- Rationale: The sources support both parts of the claim. S22 reports substantial CoT gains on arithmetic and commonsense reasoning tasks, including PaLM’s 58% GSM8K result and a 95% result on sports understanding, while stating that benefits emerge only at sufficient model scale. S1 shows that effects vary by model type and task: non-reasoning models often improve, reasoning models gain little, and some models decline. S30 similarly reports that traditional CoT exemplars do not improve recent strong models, though they may benefit weaker models.
- Supporting text: S22: CoT benefits “only materialize with a sufficient number of model parameters (around 100B)” and improve performance across arithmetic and commonsense tasks. S1: effectiveness “varies significantly by model type and task”; non-reasoning models show gains, while reasoning models show minimal benefits. S30: CoT exemplars “do not enhance the reasoning performance of strong models, although they may benefit weaker models.”

#### F2: SUPPORTED

- Claim: For strong contemporary mathematical-reasoning models, few-shot CoT exemplars can primarily serve output-format and response-alignment functions rather than supplying additional reasoning capability.
- Sources: S30, S23, S24, S25
- Rationale: S30 directly evaluates recent strong models on mathematical reasoning and explicitly reports that traditional CoT exemplars do not improve reasoning performance relative to zero-shot CoT, while their primary function is aligning output format with human expectations. It also states that models tend to ignore exemplar content. S23, S24, and S25 describe the conventional view that few-shot CoT can improve reasoning, but they do not materially undermine the narrower, model-specific empirical claim supported by S30.
- Supporting text: S30: “for recent strong models such as the Qwen2.5 series, adding traditional CoT exemplars does not improve reasoning performance compared to Zero-Shot CoT. Instead, their primary function is to align the output format with human expectations.”

#### F3: SUPPORTED

- Claim: The formatting-only explanation is too broad: some structured intermediate computation appears to contribute beyond verbosity or presentation.
- Sources: S10, S13, S8
- Rationale: The cited sources collectively support the claim. S10 reports that CoT’s performance boost is not explained by extra test-time compute alone or by particular phrasing, while also finding that models sometimes rely heavily on CoT and that intervening in it changes answers. S13 describes structured trajectories, process evaluation, and controller actions, and reports gains that are not reducible to brute-force compute. S8 reports that a symbolic reasoning chain executed by a deterministic solver improves performance over standard CoT, indicating that structured intermediate computation can contribute beyond presentation. The evidence supports the broad finding, though it does not establish that every form of structured intermediate computation is causally necessary.
- Supporting text: S10: “CoT’s performance boost does not seem to come from CoT’s added test-time compute alone” and models sometimes rely on CoT heavily. S13: CoT2-Meta uses “tree-structured search,” process evaluation, repair, and pruning, with gains “not reducible to brute-force compute.” S8: Faithful CoT translates queries into symbolic reasoning chains and uses a deterministic solver; it “improves empirical performance” over standard CoT.

#### F4: SUPPORTED

- Claim: Visible CoT is not guaranteed to be a faithful explanation of the causal process producing the answer.
- Sources: S10, S6, S7, S15
- Rationale: The saved sources directly state that CoT may fail to faithfully represent the model’s actual reasoning or the factors driving its output. S10 reports that stated reasoning can be unfaithful and describes post-hoc reasoning and cases where models rely on or ignore CoT differently across tasks. S6 and S7 report divergences between reasoning traces, visible answers, and actual influences on outputs. S15 explicitly frames unfaithfulness as answers being driven by shortcuts that bypass the generated reasoning, including a direct instruction-to-answer causal path.
- Supporting text: S10: “it is unclear if the stated reasoning is a faithful explanation of the model’s actual reasoning”; “while chain of thought reasoning is not always faithful.” S15: “A model may produce a plausible reasoning chain, yet its answer is driven by shortcuts that bypass the generated reasoning.”

#### F5: SUPPORTED

- Claim: Formatting and answer placement can produce misleading evidence about whether reasoning is being used.
- Sources: S9, S10
- Rationale: S9 directly identifies explicit terminal-answer formatting and answer placement as a confound: corruption studies may measure where answer text appears rather than where computation occurs. S10 independently shows that interventions on stated reasoning produce task-dependent changes in model answers, demonstrating that such behavioral tests can be difficult to interpret as evidence of faithful reasoning. Together, the sources support the claim’s general point about misleading evidence, particularly in chain-of-thought faithfulness evaluations.
- Supporting text: S9: “These tests largely measure answer placement rather than where intermediate computation is carried out” and “corruption studies detect where the answer text appears, not where computation occurs.” S10: models show “large variation” in how strongly they condition on CoT, and each intervention test “is not meant to be conclusive evidence for CoT being faithful.”

#### F6: SUPPORTED

- Claim: The real fault line is between surface CoT, latent computation, and generic serial compute—not between two universally valid camps of 'reasoning' and 'formatting.'
- Sources: S14, S1, S8, S10, S11, S13
- Rationale: S14 explicitly frames three competing explanations—surface CoT, latent-state trajectories, and generic serial compute—and says they should be disentangled rather than treated as a binary debate. S8 and S10 support the distinction between surface reasoning traces and the model’s underlying reasoning, including evidence that CoT may be unfaithful or task-dependent. S1 and S11 show that CoT and additional sequential compute are not universally beneficial and vary by model and task. S13 further distinguishes reasoning trajectories from computation control, supporting the broader contrast with generic compute. The wording about 'universally valid camps' is an interpretive summary, but it is consistent with the sources’ repeated claims that effects are conditional and not universal.
- Supporting text: S14 distinguishes S (surface CoT), Z (latent-state trajectories), and B (generic serial compute), stating that current work supports three incompatible readings and recommending evaluations that explicitly disentangle them. S10 reports that models vary in how much they rely on CoT and that CoT can be unfaithful on some tasks. S1 concludes that CoT is not universally optimal; S11 says budget-performance scaling does not hold universally.

#### F7: SUPPORTED

- Claim: Evaluation design is a major reason the literature appears inconsistent.
- Sources: S1, S30, S9
- Rationale: The cited sources collectively identify substantial evaluation-design effects that can produce divergent findings: S1 reports that benchmarking approaches and correctness thresholds materially change outcomes; S30 identifies a common evaluation bias that underestimates Zero-shot CoT; and S9 demonstrates a format confound in corruption studies, where results track answer placement rather than computational depth. Together, this supports the claim that evaluation design is a major reason for apparent inconsistency.
- Supporting text: S1: “Perceived performance is critically affected by the benchmarking approach, as different correctness thresholds significantly transform assessment outcomes.” S30: “We first identify a common evaluation bias ... which significantly underestimates the performance of Zero-shot CoT.” S9: corruption studies “largely measure answer placement” rather than where intermediate computation occurs.

#### F8: SUPPORTED

- Claim: The practical value of CoT should be evaluated as an accuracy–reliability–cost tradeoff, not accuracy alone.
- Sources: S1, S11, S13
- Rationale: The cited sources collectively support all three dimensions. S1 explicitly reports accuracy changes, increased variability/inconsistency, and substantial time/token costs, and concludes that CoT decisions should weigh accuracy, consistency, and response time. S13 supports evaluating reasoning systems beyond aggregate accuracy through calibration, selective prediction, abstention, and compute-normalized performance. S11 further frames test-time scaling as spending additional inference compute and reports that gains can be small, negative, or non-universal across models.
- Supporting text: S1: CoT may improve average performance but introduce inconsistency; requests increase time/token usage; decisions should consider tradeoffs between accuracy, consistency, and response time. S13: gains are accompanied by improved calibration and selective prediction under matched inference budgets, with explicit stopping and abstention. S11: test-time scaling spends more inference compute, while budget forcing can yield little or negative gains depending on the model.

### Missing Citations

- None identified.

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

1. R1: Define chain-of-thought prompting and distinguish it from direct answering, answer-format instructions, hidden or internal reasoning, self-consistency, tool augmentation, and other inference-time procedures.
2. R7: Evaluate the evidential strength and comparability of the cited literature, including model versions and sizes, datasets, baselines, prompt protocols, decoding settings, metrics, uncertainty, replication, and source quality.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ac152f1d42cbe0f247f27e3225b834f4d7d35d3a27bade4d08806b371c248b6d`
- Candidate report hash: `e476497b268467e52dc0cca9a9eaa8b8685bf7e44ea34139c78903887094be96`
- LLM calls: 10
- Evaluated at: 2026-09-01T10:39:01.006388+00:00
