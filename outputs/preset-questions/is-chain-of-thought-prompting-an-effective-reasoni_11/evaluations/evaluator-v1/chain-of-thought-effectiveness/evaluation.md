# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** chain-of-thought-effectiveness

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 76.3 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.66
- Coverage: 0.69
- Depth: 0.59
- Citation quality: 0.89
- Citation validity: 1.00
- Citation support: 0.93
- Citation completeness: 0.77
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report gives useful high-level framing, but the central intervention and comparison conditions are not operationally defined in enough detail.
- Candidate evidence:
  - The report defines the intervention broadly as a bundle that can “allocate extra serial computation,” provide “an external scratchpad or task schema,” alter “answer readout,” and induce “a particular output format.”
  - The conclusion distinguishes “ordinary prompted CoT” from “process-trained or latent reasoning systems.”
- Missing:
  - It does not explicitly define standard CoT as eliciting intermediate natural-language reasoning before the final answer.
  - It does not clearly distinguish CoT from direct answering, answer-format instructions, self-consistency, sampling, tool augmentation, or other inference-time procedures.
  - The report discusses latent reasoning and process-trained systems, but not as a systematic comparison of alternative interventions.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: It covers multiple task families and avoids a universal claim, but coverage of knowledge and open-ended reasoning is limited and mostly asserted through source labels.
- Candidate evidence:
  - It reports gains over direct or standard few-shot prompting on “arithmetic, symbolic, and some commonsense tasks.”
  - It qualifies the effects as concentrated on “difficult, decomposable questions” and potentially “neutral or negative on simpler tasks.”
  - It separately discusses code generation, where generic CoT reportedly produced only “slight gains,” and arithmetic versus CommonsenseQA results for latent CoT.
- Missing:
  - Knowledge-intensive tasks and genuinely open-ended reasoning are only lightly covered; the evidence is primarily arithmetic, symbolic, commonsense, and code benchmarks.
  - The report does not provide concrete comparative effect sizes, uncertainty, or sufficiently detailed task-level results.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The major fault lines are identified, especially task structure, distribution shift, and model regime, but scale, prompt design, and baseline behavior receive incomplete empirical treatment.
- Candidate evidence:
  - The report identifies task difficulty and decomposability as moderators: gains are concentrated on “difficult, decomposable questions.”
  - It discusses distribution similarity and robustness, citing fragility under changes in “task structure, chain length, and surface format.”
  - It distinguishes ordinary prompted CoT from “trained reasoning models” and says generic step-by-step instructions offer little incremental benefit for some built-in reasoning models.
  - It discusses structured and strategic demonstrations, including “strategic CoT” and structured code representations.
- Missing:
  - Model scale or capability is not analyzed systematically; the report refers to model regimes but gives little evidence about scaling thresholds or size effects.
  - Prompt demonstrations, delimiters, and baseline prompting behavior are mentioned mainly as confounds or gaps rather than documented moderators with controlled comparisons.
  - The report does not consistently distinguish well-supported moderators from speculative explanations.

### R4

- Coverage: 1.00
- Depth: 0.75
- Rationale: This is one of the strongest sections: it directly addresses reasoning versus formatting and avoids equating improved outcomes with faithful visible reasoning. The remaining limitation is evidential detail rather than conceptual coverage.
- Candidate evidence:
  - The summary explicitly presents a three-way account: “useful intermediate computation can occur; generic additional computation can help; and surface format/readout conventions can independently alter performance.”
  - It states that “accuracy and faithfulness are separate properties” and that the visible chain is not reliably the computation producing the answer.
  - It discusses terminal-answer effects, compression, latent/nonverbal representations, and the possibility that chains are redundant, post-hoc, or causally used.
- Missing:
  - Although the mechanisms are clearly separated conceptually, the report does not give a fully systematic account of which experiments cleanly discriminate semantic reasoning from verbosity or formatting across task types.

### R5

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes compute and protocol confounds, but it does not adequately cover the full range of inference-time procedures required by the rubric.
- Candidate evidence:
  - The report says ordinary CoT changes “surface CoT, latent-state trajectories, and generic serial compute” simultaneously.
  - It calls for controls matching “total generated tokens, inference-time compute, demonstrations, delimiters, answer placement, and output format.”
  - It discusses token budgets, compression, truncation, and additional computation.
- Missing:
  - Sampling and self-consistency or voting are not substantively discussed.
  - Calculators, code execution, retrieval, and other external tools are not separated from CoT effects.
  - Answer extraction is mentioned indirectly through “readout” and terminal-answer effects but is not treated as a distinct protocol variable.
  - There are no actual like-for-like comparisons reported; the report mainly identifies the need for them.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: It addresses both causal relevance and faithfulness and names appropriate intervention methods, but methodological interpretation is relatively compressed.
- Candidate evidence:
  - It explicitly separates “accuracy and faithfulness” and states that correct final answers do not establish that the visible chain was followed.
  - It cites causal mediation and causal-abstraction studies, including evidence that some models partially realize the causal structure described by their chains.
  - It mentions “early answering,” chain truncation, corruption, conflicting-answer controls, and reasoning errors in correct-answer chains.
- Missing:
  - The report does not explain the designs, assumptions, or limitations of these faithfulness tests in enough detail to assess their validity.
  - Logical validity of traces is discussed only briefly through “reasoning errors”; the distinction between a logically invalid but causally used trace and a valid but causally irrelevant trace could be sharper.
  - It does not substantially discuss counterfactual interventions or distribution-shift tests as direct faithfulness tests, beyond brief references.

### R7

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report recognizes comparability problems and some evidence limitations, but it does not itself perform the detailed evidence-quality assessment required by the rubric.
- Candidate evidence:
  - The report repeatedly qualifies its synthesis, noting that sources “do not form a formal meta-analysis.”
  - It states that headline claims are “not directly comparable” and cites differences between explanatory sources and intervention studies.
  - It acknowledges unresolved generalization across “model scales, free-response tasks, domains, open versus closed models, and frontier systems.”
- Missing:
  - There is little concrete comparison of model versions or sizes, datasets, baselines, decoding settings, metrics, uncertainty, replication, or effect sizes.
  - The source list mixes peer-reviewed papers with blogs, YouTube, Medium, vendor material, Substack, and position pieces, but the report does not systematically assess source quality or explain how weaker sources affect confidence.
  - Confidence labels such as “High” are not supported by a transparent evidence inventory or replication analysis.
  - Several claims are attributed only to source numbers without enough study details for independent comparability assessment.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The synthesis answers the question well and provides sensible evaluation guidance, but practical implications for cost, latency, and deployment reliability are only partially developed.
- Candidate evidence:
  - The conclusion directly rejects both extremes: CoT is “neither merely cosmetic nor universally faithful or necessary.”
  - It gives a qualified use condition: CoT can help on “difficult, decomposable, in-distribution tasks” and should be treated as “a conditional tool, not a universal reasoning mechanism.”
  - It recommends compute- and format-matched controls and causal-use testing.
  - It discusses efficiency through “token reductions,” “verbosity,” and “additional computation,” and identifies brittleness and misleading chains as reliability concerns.
- Missing:
  - Cost and latency implications are not discussed explicitly enough beyond token usage and inference-time computation.
  - The practical guidance is not stratified by application risk, task type, or whether external verification is available.
  - The conclusion could more clearly distinguish established empirical findings from hypotheses such as the exact division among semantic computation, generic serial compute, and formatting effects.

### Novel Value

- The report offers a useful three-way synthesis separating semantic intermediate computation, generic additional serial computation, and formatting/readout effects.
- It emphasizes that final-answer gains, causal use of traces, faithfulness, and robustness are distinct outcomes.
- It identifies a concrete unresolved experimental ideal: controls matching tokens, compute, demonstrations, delimiters, answer placement, and output format simultaneously.

## Citations

### Support

#### F1: SUPPORTED

- Claim: CoT is an effective accuracy intervention in some regimes, especially difficult tasks requiring sequential or compositional reasoning, but not a universal improvement.
- Sources: S4, S9, S13, S18, S1
- Rationale: The sources collectively support the claim. S4 and S9 report substantial accuracy gains from CoT on complex, multi-step, arithmetic, commonsense, and symbolic reasoning tasks. S9 and S13 specifically connect CoT’s value to sequential or compositional reasoning and task difficulty. S13 states that CoT is often unnecessary for simple questions and may not always help challenging ones, while S18 reports mixed results across benchmarks and no improvement from an additional latent-reasoning iteration. S1 further shows only slight gains from ordinary CoT in code generation, indicating that improvement is not universal.
- Supporting text: S9: CoT “dramatically improved performance” on arithmetic, commonsense, and symbolic-manipulation tasks and addresses “sequential reasoning.” S13: CoT is “often unnecessary for simple questions”; for challenging questions it is more likely to alter the initial choice, “though not always positively.” S18: verbalized/latent CoT improved some benchmarks but reduced CommonsenseQA accuracy; S1 says CoT brought only “slight improvements” in code generation.

#### F2: SUPPORTED

- Claim: The visible chain is not a reliable proxy for the computation that produced the answer. Accuracy and faithfulness are separate properties.
- Sources: S23, S33, S6, S13
- Rationale: The cited sources collectively support both parts of the claim. S23 and S33 explain that a generated chain may be plausible yet not causally determine the final answer, while S6 reports that corruption sensitivity can track explicit answer text rather than computation. S13 directly distinguishes final-answer correctness from reasoning correctness, reporting that many correct answers contain erroneous reasoning.
- Supporting text: S33: “there is no guarantee that the LLM is using its generated CoT tokens to work out its answer.” S13: “many responses, although correct in their final answer, contain errors in their reasoning process.” S6: “Sensitivity follows the answer text, not the computation.”

#### F3: SUPPORTED

- Claim: Answer placement and output format are major confounds, particularly in studies that infer reasoning from chain corruption.
- Sources: S6, S3, S5
- Rationale: S6 directly identifies answer placement and chain format as a systematic confound in corruption studies, showing that sensitivity can track explicit answer text rather than computation. S3 and S5 independently support the broader point that formatting can substantially change model performance, though they do not specifically examine chain-corruption studies. Together, the sources support the claim, with the strongest evidence coming from S6.
- Supporting text: S6: “We identify a systematic confound” in which corruption studies detect “where the answer text appears, not where computation occurs”; it also reports that models follow explicit terminal answers over intermediate reasoning. S3: small formatting changes reportedly shift performance from 3% to over 80%. S5: semantically identical instructions produced large performance differences across formats.

#### F4: PARTIALLY_SUPPORTED

- Claim: Many apparent CoT gains reflect a mixture of intermediate computation, additional serial compute, and learned schemas rather than natural-language wording alone.
- Sources: S19, S20, S16, S18, S34, S38, S41
- Rationale: The snapshots strongly support that CoT effects cannot be attributed to natural-language wording alone: S19/S20 explicitly distinguish surface traces, latent-state trajectories, and generic serial compute, and note that CoT changes visible traces and compute allocation simultaneously. S16 and S18 provide examples of non-verbal or latent intermediate representations retaining or improving performance, while S34/S38 and S41 document extra token computation, token overhead, and concise reasoning. However, the cited material does not meaningfully establish the specific role of “learned schemas,” nor does it demonstrate that many apparent gains quantitatively reflect all three factors as a mixture. Thus, the broader decomposition is supported, but the claim’s learned-schema and “many gains” components are not fully supported.
- Supporting text: S19/S20: CoT prompting changes both visible traces and compute allocation; the sources distinguish surface CoT, latent-state dynamics, and generic serial compute. S16: Abstract-CoT uses a learned abstract reasoning language and matches verbalized-CoT performance with far fewer tokens. S18: latent vectors can provide performance uplift over a matched direct-answer mode. S41: CoT effectiveness is attributed to additional computation from intermediate tokens, whose number also drives inference cost.

#### F5: SUPPORTED

- Claim: Representation quality matters: structured, strategic, executable, or causally selected intermediate steps can outperform generic verbal CoT.
- Sources: S1, S2, S10, S37
- Rationale: The supplied sources collectively support the claim’s important components. S1 reports that structured CoT outperforms ordinary CoT by up to 13.79% in Pass@1. S2 reports that eliciting strategy before generating CoT improves results, including gains on GSM8K and Tracking_Objects. S10 describes executable symbolic reasoning chains and reports that Faithful CoT outperforms vanilla CoT on 9 of 10 datasets. S37 reports that causally sufficient and necessary step selection reduces redundancy and token use while maintaining or improving accuracy. Although the methods and task domains differ, together they directly support the broader claim that intermediate-step representation and selection quality can matter relative to generic verbal CoT.
- Supporting text: S1: “SCoT prompting outperforms CoT prompting by up to 13.79% in Pass@1.” S2: SCoT first elicits an effective problem-solving strategy to guide high-quality CoT paths and reports substantial accuracy improvements. S10: Faithful CoT “outperforms vanilla CoT on 9 out of the 10 datasets,” using chains executed by a deterministic solver. S37: causal sufficiency/necessity selection “significantly reduces reasoning redundancy while maintaining or improving prediction accuracy.”

#### F6: SUPPORTED

- Claim: Task distribution and model regime explain much of the disagreement. Ordinary prompted CoT, trained reasoning models, and latent-reasoning systems are different interventions.
- Sources: S11, S8, S14, S27, S18
- Rationale: The sources collectively support both parts of the claim. S11 reports that CoT performance depends strongly on task and distribution shift. S8 finds that CoT effects vary by model type and task, distinguishing non-reasoning from built-in reasoning models. S14 and S27 describe trained reasoning models as a distinct intervention from standard prompted CoT, involving training and additional inference-time thinking. S18 explicitly distinguishes natural-language CoT from latent reasoning in vector space and evaluates it as a separate framework.
- Supporting text: S11: CoT is dissected across task, length, and format, and becomes fragile under distribution shifts. S8: CoT effectiveness varies significantly by model type and task; reasoning models receive only minimal benefits from generic CoT prompts. S27: o1 was trained through reinforcement learning to perform CoT automatically, unlike merely prompting an LLM to think in steps. S18: latent reasoning generates the reasoning process in the model’s latent space rather than as natural-language tokens.

#### F7: SUPPORTED

- Claim: Additional computation can help, but more tokens or verbosity are not automatically better.
- Sources: S15, S34, S38, S41, S37
- Rationale: The saved sources support both parts of the claim. S15 states that increasing inference-time computation can improve reasoning, while also describing uncontrolled, extended reasoning chains and presenting methods that achieve concise, efficient reasoning under constrained budgets. S34 and S38 report that CoT adds token overhead, that token-budget choice matters, and that reasonable budgets can reduce tokens while largely preserving accuracy; overly small budgets can even lead to greater actual usage. S41 identifies redundant tokens and reports that concise reasoning can reduce output length while maintaining accuracy. S37 similarly distinguishes necessary from unnecessary steps and reports that pruning redundancy reduces token usage without sacrificing accuracy.
- Supporting text: S15: “Increasing computation during inference ... has been shown to improve the reasoning capabilities of LLMs,” but the paper also targets “controllable reasoning” and more concise outputs. S34/S38: a reasonable token budget reduced output from 258 to 86 tokens while retaining the correct answer, whereas a smaller budget produced 157 tokens; the choice of budget is crucial. S41: reasoning traces contain “many redundant tokens,” and its method reduced output tokens by 30% while maintaining average accuracy. S37: unnecessary steps can reduce efficiency or hinder performance, while pruning redundant steps reduces token usage without sacrificing accuracy.

### Missing Citations

- Q25: The proportions of CoT gains attributable to semantic intermediate content, generic serial computation, learned schemas, and terminal-answer or readout conventions remain unknown.
- Q26: It remains unclear whether structured, executable, concise, or latent methods improve out-of-distribution reasoning and calibration rather than mainly benchmark accuracy and efficiency.
- Q27: The generality of causal-abstraction and mediation findings across model scales, domains, task formats, and frontier systems remains unresolved.
- Q28: It remains uncertain whether latent-reasoning findings from specialized post-trained models transfer to ordinary pretrained or instruction-tuned models using prompted verbal CoT.
- Q29: Chain-of-thought prompting is a bundle of interventions that can allocate extra serial computation, provide an external scratchpad or task schema, alter answer readout, and induce a particular output format.
- Q30: On difficult, decomposable, in-distribution tasks and in models capable of using intermediate representations, CoT can improve problem solving.
- Q31: Visible chains can be redundant or unfaithful, can be unnecessary when the answer is already selected, and can become misleading under distribution shift or answer-conditioned generation.

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
3. R5: Separate the effects of the CoT prompt itself from effects of sampling, self-consistency or voting, longer generation, answer extraction, calculators, code, retrieval, or other external computation and scaffolding.
4. 1 cited finding(s) were not fully supported by saved evidence.
5. 7 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ac152f1d42cbe0f247f27e3225b834f4d7d35d3a27bade4d08806b371c248b6d`
- Candidate report hash: `0f1c059fd0608a44f4bfb8161665e7d23e98652304bf5b2612594a1513601a97`
- LLM calls: 9
- Evaluated at: 2026-09-01T09:19:18.485788+00:00
