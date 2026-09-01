# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** chain-of-thought-effectiveness

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 73.3 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.62
- Coverage: 0.62
- Depth: 0.62
- Citation quality: 0.86
- Citation validity: 1.00
- Citation support: 0.83
- Citation completeness: 0.84
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report uses several relevant distinctions, but it assumes rather than defines the evaluated intervention and does not provide the requested conceptual taxonomy.
- Candidate evidence:
  - The report refers to “ordinary free-form natural-language CoT,” “standard prompting,” “reasoning-native models,” and “self-consistency or voting” among unresolved pipeline differences.
  - The report distinguishes visible rationales from “internal reasoning” indirectly by stating that a visible rationale may be “post hoc” or may not represent the computation that produced the answer.
- Missing:
  - It does not explicitly define chain-of-thought prompting as an intervention involving elicited intermediate reasoning steps.
  - It does not clearly distinguish CoT from direct answering, answer-format instructions, hidden/internal reasoning, self-consistency as a separate procedure, tool augmentation, or other inference-time methods.
  - It does not establish comparison conditions systematically.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: It covers multiple task families and acknowledges positive, null, and negative results, but the empirical comparison across those families remains mostly high-level.
- Candidate evidence:
  - Finding 1 reports gains over standard prompting across “arithmetic, commonsense, and symbolic reasoning tasks,” including GSM8K, and cites variation across six models and six question-answering datasets.
  - Finding 8 discusses math, planning, multi-hop QA, and relational inference benchmarks.
  - The conclusion limits the claim to tasks requiring familiar multistep decomposition and aligned evaluation conditions, rather than generalizing universally.
- Missing:
  - The report gives little concrete characterization of effects on knowledge-intensive, open-ended, or genuinely commonsense tasks beyond naming categories.
  - It does not provide enough task-level results to compare gains, nulls, and harms across the different task families.
  - It does not clearly separate final-answer accuracy from other outcomes for each task type.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The major moderators are present and plausibly connected to conflicting results, but the evidence-status and causal contribution of individual moderators are not fully unpacked.
- Candidate evidence:
  - Finding 4 discusses model scale, task difficulty, training or demonstration alignment, reasoning length, and surface-format shifts.
  - Finding 3 contrasts non-reasoning models, which may gain from CoT, with reasoning-native models, which may show marginal gains or declines.
  - Finding 5 and Finding 6 identify prompt format, demonstrations, extraction, token budgets, and broader prompt structure as moderators or confounds.
  - The Conflicts and Uncertainty section attributes disagreement to model generation, task selection, distribution shift, baselines, and metrics.
- Missing:
  - The report does not systematically identify which moderators are well established versus contested or insufficiently tested.
  - Baseline prompting behavior is mentioned, but its role is not developed with concrete like-for-like comparisons.
  - Prompt and demonstration design are identified as factors, but their independent effects are not analyzed in detail.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report directly addresses reasoning-versus-formatting and identifies relevant controls, but concludes that decisive causal isolation is unresolved and does not fill that gap with detailed comparative evidence.
- Candidate evidence:
  - Finding 5 states that formatting materially affects performance and reports format changes producing differences as large as 40% on one code-translation task.
  - Finding 6 reports that uninformative filler does not reproduce the CoT gain, while paraphrasing produces similar performance, arguing against purely token-count or exact-wording explanations.
  - Finding 2 and the conclusion distinguish improved final-answer accuracy from the possibility that the visible rationale is post hoc, incomplete, or inconsistent with the answer.
  - The report explicitly says that a fully format-, token-, demonstration-, extraction-, and decoding-matched non-CoT comparison remains unresolved.
- Missing:
  - It does not provide a sufficiently direct decomposition of the contribution of informative intermediate content, generic extra context, verbosity, and answer-format effects.
  - The evidence separating these mechanisms is summarized but not described in enough methodological detail to establish what each intervention rules out.
  - It does not clearly distinguish whether paraphrase preservation reflects preserved reasoning content, generic context, or another prompt-level property.

### R5

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes several protocol confounds and gives one clear tool/scaffolding distinction, but it does not comprehensively evaluate the requested inference-time procedures.
- Candidate evidence:
  - Finding 6 notes unresolved effects of “decoding” and “general prompt structure,” in addition to demonstrations, answer presentation, and extraction.
  - Finding 8 explicitly distinguishes ordinary free-form CoT from a method adding symbolic representation and a deterministic solver.
  - The report mentions “self-consistency or voting,” calculators, code, retrieval, and other external procedures in the rubric-relevant discussion only indirectly; it does discuss symbolic execution and deterministic solvers as added computation.
- Missing:
  - It does not actually compare CoT with and without sampling, self-consistency, voting, longer generation, or matched decoding protocols.
  - Calculators, code execution, retrieval, and external tools are not substantively analyzed as separate sources of improvement.
  - Answer extraction and token length are identified as confounds, but their effects are not quantified or separated using like-for-like baselines.
  - The report does not clearly distinguish the CoT prompt effect from the effects of additional inference-time computation.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is one of the stronger sections: it includes appropriate causal interventions and explicitly separates faithfulness from accuracy, but the assessment remains summarized rather than methodologically comprehensive.
- Candidate evidence:
  - Finding 2 reports truncation and injected-mistake interventions that test whether models depend on their generated chains.
  - It states that some traces are not logically entailing of the final answer and distinguishes faithfulness from correctness and plausibility.
  - Finding 6 reports filler-token replacement and paraphrase interventions.
  - Finding 4 discusses fluent but logically inconsistent chains and degradation under distribution shift.
- Missing:
  - The report does not discuss scrambling or systematic trace-corruption tests in detail beyond truncation and injected mistakes.
  - It does not clearly distinguish all measures of logical validity from causal faithfulness in the reported studies.
  - The intervention findings are summarized without enough task-specific detail to assess when traces are causally relevant versus merely correlated.

### R7

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report shows good awareness of evidence-quality problems and source dependence, but it lacks the concrete methodological audit needed for deep evaluation of the cited literature.
- Candidate evidence:
  - The report warns that headline results are not directly comparable because of differing models, tasks, distributions, baselines, metrics, prompt formats, extraction, and decoding.
  - The Conflicts and Uncertainty section notes that several sources are secondary summaries of the same Anthropic study and should not be counted as independent replications.
  - It explicitly characterizes practitioner guides as weaker evidence than primary comparative and intervention studies.
  - It mentions repeated-trial evaluation, strict correctness thresholds, variability, and declines under some metrics.
- Missing:
  - Model versions and sizes, dataset composition, exact baselines, decoding settings, and metric definitions are rarely specified concretely.
  - Uncertainty is expressed as confidence labels but not supported with statistical uncertainty, effect sizes, or replication details.
  - The source list includes many practitioner, blog, and secondary sources, but the report does not systematically verify or rank the underlying evidence.
  - Comparability limitations are identified more often than demonstrated through detailed study-by-study comparison.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report directly answers the central question with an appropriately conditional synthesis and addresses accuracy, reliability, and cost, but practical decision rules and quantitative tradeoffs are limited.
- Candidate evidence:
  - The conclusion gives a qualified verdict: CoT is “effective but conditional,” “not merely a formatting trick,” but also not reliable evidence of faithful reasoning.
  - It identifies suitable conditions involving model capability, familiar multistep task structure, and aligned final-answer evaluation.
  - Finding 9 and the conclusion discuss reliability limitations, distribution-shift brittleness, token use, response time, and marginal benefit for reasoning-native models.
  - The Remaining Gaps section states practical and research implications, including stricter controls, adversarial distractors, distribution shifts, and external verification.
- Missing:
  - Practical guidance about when to deploy CoT versus direct answering, self-consistency, tools, or solver-grounded methods is only implicit.
  - Cost and latency implications are mentioned but not quantified or balanced against accuracy gains.
  - The conclusion could more explicitly separate established empirical findings from hypotheses about the underlying computation.

### Novel Value

- The report provides a useful synthesis that reframes the disagreement as a distinction between final-answer effectiveness and trace faithfulness rather than a binary reasoning-versus-formatting dispute.
- It identifies an important unresolved methodological gap: a fully matched non-CoT baseline controlling format, demonstrations, token budget, extraction, and decoding.
- It cautions against treating solver-grounded or executable reasoning improvements as evidence about ordinary free-form CoT itself.
- It highlights source dependence and the risk of counting multiple summaries of the same faithfulness study as independent confirmations.

## Citations

### Support

#### F1: SUPPORTED

- Claim: CoT is effective for final-answer accuracy in some settings, especially difficult and distribution-aligned reasoning tasks, but it is not universally beneficial.
- Sources: S9, S10, S5
- Rationale: S9 directly reports improved performance and accuracy on complex arithmetic, commonsense, and symbolic reasoning tasks, including a large GSM8K gain. S5 explicitly states that CoT effectiveness varies by model and task, reports benefits on difficult questions, and concludes that it is not universally optimal. The supplied excerpts support the overall claim, although the specific phrase “distribution-aligned” is not stated verbatim; S10 instead reports robustness across the tested models and datasets.
- Supporting text: S9: CoT “significantly improves” performance on complex reasoning and improves accuracy across arithmetic, commonsense, and symbolic tasks. S5: CoT “can improve performance on difficult questions” but may introduce errors and “is not universally optimal”; its effectiveness depends on model type and use case.

#### F2: SUPPORTED

- Claim: The most important fault line is the distinction between predictive effectiveness and faithful reasoning. CoT can improve accuracy even when its visible rationale is post hoc, incomplete, or inconsistent with the answer.
- Sources: S21, S26, S7
- Rationale: The sources jointly support the distinction between CoT’s performance benefits and the faithfulness of its visible reasoning. S21 states that CoT boosts performance but its reasoning chain does not necessarily reflect how the model arrives at the answer, and gives an example where the answer does not follow from the chain. S26 explicitly discusses post-hoc reasoning and finds that CoT is unfaithful on some tasks while still producing performance gains. S7 describes fluent but logically inconsistent CoT outputs and reports that CoT can be effective despite superficial or brittle reasoning. The wording “incomplete” is not stated verbatim, but is reasonably captured by the examples of reasoning that does not entail or fully account for the answer.
- Supporting text: S21: CoT “boosts” performance, but the generated reasoning chain “does not necessarily reflect how the model arrives at the answer”; standard CoT is not guaranteed to be faithful, and the answer may not follow from the chain. S26: models may produce post-hoc reasoning, and CoT is “not always faithful” despite its performance benefits. S7: CoT can produce “fluent yet logically inconsistent reasoning steps,” with apparent reasoning sometimes reflecting shallow pattern replication.

#### F3: SUPPORTED

- Claim: CoT is neither uniformly causal nor uniformly cosmetic: its influence depends on the task and model.
- Sources: S26, S5
- Rationale: Both cited sources directly support the claim. S26 reports that models vary across tasks in how strongly they condition on CoT, from largely ignoring it to relying heavily on it. S5 reports that CoT effectiveness varies significantly by model type and task, with different gains or declines across models.
- Supporting text: S26: “Models show large variation across tasks in how strongly they condition on the CoT,” and “not using CoT at all for some tasks while relying upon it heavily for other tasks.” S5: “its effectiveness varies significantly by model type and task.”

#### F4: PARTIALLY_SUPPORTED

- Claim: Distributional alignment explains part of the disagreement: CoT is strongest when test problems resemble the task structures, reasoning lengths, and formats represented in training or demonstrations, and becomes brittle under shifts.
- Sources: S7, S9, S30, S5
- Rationale: S7 directly supports the central distributional-alignment claim: it frames CoT as learned from in-distribution data, explicitly analyzes task, length, and format, and reports fragility under distribution shifts. S9 and S30 support that CoT relies on few-shot demonstrations and improves several familiar reasoning benchmarks, but they do not establish that performance is strongest specifically when test instances resemble training structures, lengths, and formats. S5 supports variability by model and task, but discusses diminishing or inconsistent gains rather than distributional shift. Thus the core claim is well supported by S7, while the broader wording and attribution across all citations are only partially supported.
- Supporting text: S7: CoT effectiveness is “fundamentally bounded by the degree of distribution discrepancy” and is studied across “task, length, and format”; it “works effectively” on in-distribution or near-in-distribution data but becomes “fragile and prone to failure” under moderate shifts. S9/S30: CoT uses a few demonstrations containing intermediate reasoning steps and improves arithmetic, commonsense, and symbolic reasoning tasks.

#### F5: SUPPORTED

- Claim: Formatting is a genuine confound, but the retrieved evidence does not establish that all CoT gains are formatting-only.
- Sources: S8, S16, S26
- Rationale: S8 directly supports that prompt formatting can substantially affect performance, establishing formatting as a genuine confound. S16 reports that zero-shot and few-shot CoT outperform baselines on several tasks, while noting performance can decrease on some tasks. S26 further reports that CoT’s performance boost does not come from particular CoT phrasing and that replacing CoT with uninformative filler text produced no accuracy gain, which weighs against the claim that all CoT gains are merely formatting effects. Together, the sources support the qualified claim, though they do not directly provide a comprehensive causal separation of formatting from every CoT gain.
- Supporting text: S8: “GPT-3.5-turbo’s performance varies by up to 40% ... depending on the prompt template.” S16: “Zero-shot CoT outperforms the baseline LLM on several tasks.” S26: “CoT’s performance boost does not seem to come from ... the particular phrasing of the CoT”; replacing CoT with “uninformative filler text” yielded no accuracy gain.

#### F6: PARTIALLY_SUPPORTED

- Claim: The evidence argues against two simplistic explanations—CoT gains are not merely the result of extra context tokens or the exact wording of the rationale—but leaves broader pipeline and formatting effects unresolved.
- Sources: S26, S8, S16
- Rationale: S26 directly supports the two negative findings: CoT performance gains did not appear to come from extra test-time computation alone, and similar performance with paraphrased CoT suggests the particular phrasing was not the driver. S8 supports that prompt formatting can affect LLM performance, but it does not specifically establish that such formatting effects remain unresolved as an explanation for CoT gains. S16 discusses CoT benefits and describes prompting and answer-extraction steps, but the saved excerpt does not substantiate the claim about broader pipeline effects being unresolved.
- Supporting text: S26 states that replacing CoT with uninformative filler text produced no accuracy gain and that paraphrased CoT had similar performance. S8 reports performance differences of up to 40% across prompt templates, while S16 describes CoT as a multi-step prompting process involving reasoning and answer extraction.

#### F7: PARTIALLY_SUPPORTED

- Claim: More visible reasoning text is not equivalent to better reasoning. Efficient or structured traces can preserve accuracy, but shorter traces are not the same as no reasoning.
- Sources: S13, S1, S18
- Rationale: The sources support that longer reasoning traces do not necessarily indicate better reasoning, and that structured or compressed traces can reduce token use while maintaining or improving accuracy. However, they do not directly establish the broader wording that shorter traces are specifically different from having no reasoning.
- Supporting text: S1 states that “longer traces do not imply better reasoning” and reports that hierarchical structure improved accuracy while reducing trace length. S13 reports reducing CoT output from 258 to 86 tokens while still reaching the correct answer, with only a slight average performance reduction. S18 describes an ideal balance of sufficient and necessary steps and reports pruning redundancy without sacrificing accuracy.

#### F8: SUPPORTED

- Claim: Solver-grounded or executable reasoning can improve both accuracy and faithfulness, but this does not prove that ordinary free-form CoT itself improves latent reasoning.
- Sources: S21
- Rationale: The source directly supports the first part: Faithful CoT uses executable symbolic reasoning with a deterministic solver, guarantees that the reasoning chain faithfully explains the final answer, and empirically outperforms standard CoT on 9 of 10 benchmarks. It also states that standard CoT explanations are not necessarily faithful and can misrepresent the model’s reasoning, so the reported gains from solver-grounded reasoning do not establish that ordinary free-form CoT improves latent reasoning. The final wording is a cautious inference rather than a direct experimental claim, but it is consistent with the source.
- Supporting text: The framework translates queries into symbolic reasoning chains and executes them with a deterministic solver; the authors state this “guarantees” a faithful explanation and report that it outperforms standard CoT on 9 of 10 benchmarks. They also state that standard CoT faithfulness is not guaranteed and that CoT can “lie” about the model’s true reasoning process.

#### F9: SUPPORTED

- Claim: The practical conclusion is to treat CoT as an elicitation and control strategy, not as proof that an LLM is faithfully exposing its internal reasoning.
- Sources: S9, S10, S7, S21, S26, S5, S13
- Rationale: The sources support both parts of the conclusion. S9, S10, S5, and S13 describe CoT as a prompting method that elicits intermediate steps and can affect performance, cost, and behavior. S21 and S26 explicitly state that generated CoT does not necessarily reflect the model’s actual reasoning and may be unfaithful; S7 likewise reports fluent but logically inconsistent chains and cautions against equating CoT-style output with human thinking. Together, they support treating CoT as an elicitation/control technique rather than evidence of faithful internal reasoning.
- Supporting text: S9 defines CoT prompting as providing demonstrations that elicit chains of intermediate steps. S21 states that generated reasoning “does not necessarily reflect how the model arrives at the answer” and that standard CoT can “lie” about the model’s true reasoning process. S26 similarly finds that CoT is “not always faithful,” with faithfulness varying by task and model.

### Missing Citations

- Q21: CoT is an effective but conditional strategy for improving LLM answers, not merely a formatting trick and not reliable evidence of faithful reasoning.
- Q22: CoT benefits are most credible when the model lacks native reasoning behavior, the task requires familiar multistep decomposition, and evaluation measures final-answer accuracy under aligned conditions.
- Q23: The visible rationale can be post hoc, unfaithful, or fragile under distribution shift, while formatting, demonstrations, extraction procedures, and token budgets materially affect results.
- Q24: The strongest causal comparison would match CoT and non-CoT conditions for output format, token budget, demonstrations, answer extraction, decoding, and opportunity for latent computation, and that comparison remains unresolved in the retrieved material.

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
2. R5: Separate the effects of the CoT prompt itself from effects of sampling, self-consistency or voting, longer generation, answer extraction, calculators, code, retrieval, or other external computation and scaffolding.
3. R7: Evaluate the evidential strength and comparability of the cited literature, including model versions and sizes, datasets, baselines, prompt protocols, decoding settings, metrics, uncertainty, replication, and source quality.
4. 3 cited finding(s) were not fully supported by saved evidence.
5. 4 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ac152f1d42cbe0f247f27e3225b834f4d7d35d3a27bade4d08806b371c248b6d`
- Candidate report hash: `12c91a66eba2363e57920aa6ebbd39432b75bd84376f42f2ed96cd85a5044cb5`
- LLM calls: 12
- Evaluated at: 2026-09-01T07:04:36.152175+00:00
