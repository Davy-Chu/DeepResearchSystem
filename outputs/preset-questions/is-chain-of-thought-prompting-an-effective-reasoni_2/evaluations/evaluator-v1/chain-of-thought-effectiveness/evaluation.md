# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** chain-of-thought-effectiveness

**System Version:** evidence-ledger-v1

**Model:** gpt-5.6-luna

## Summary

- Overall: 70.5 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.55
- Coverage: 0.56
- Depth: 0.53
- Citation quality: 0.91
- Citation validity: 1.00
- Citation support: 0.86
- Citation completeness: 0.96
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report identifies the central visible-trace versus latent-reasoning distinction, but it does not establish the full set of relevant baselines and neighboring procedures required by the rubric.
- Candidate evidence:
  - The report characterizes CoT as a “generic step-by-step request” and distinguishes visible natural-language traces from latent reasoning or “reasoning-like behavior.”
  - It notes that some CoT exemplars may primarily enforce output format and that some models produce CoT-like reasoning by default.
- Missing:
  - It does not clearly define CoT as an inference intervention involving demonstrations or a request to generate intermediate steps before the answer.
  - It does not explicitly distinguish CoT from direct answering, answer-format instructions, self-consistency, voting, tool use, calculators, retrieval, or other inference-time procedures.
  - The distinctions that are present are scattered and partial rather than a complete conceptual framing of the comparison conditions.

### R2

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report covers multi-step mathematical and symbolic reasoning reasonably well and includes logical/search tasks, but it does not substantially address the required knowledge, commonsense, or open-ended categories.
- Candidate evidence:
  - It reports results on GPQA Diamond, including model-specific accuracy changes and differences between average accuracy, perfect accuracy, and majority performance.
  - It discusses mathematical, logical, and search-based evaluations, including Hi-CoT across five mathematical benchmarks and latent methods on GSM8k and logical-reasoning benchmarks.
  - It explicitly cautions that the evidence does not establish effects across a broad range of task types.
- Missing:
  - There is little or no direct assessment of knowledge, commonsense, or open-ended reasoning tasks beyond GPQA and mathematical/logical benchmarks.
  - The report mostly summarizes a small set of evaluations rather than systematically comparing gains, null effects, and harms across multiple task families.
  - The claims rely partly on general explainers rather than detailed primary evidence for broad task coverage.

### R3

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report offers a strong high-level moderator synthesis, especially for model regime, task structure, metrics, and trace design, but leaves an important moderator—training-distribution similarity—and several protocol-level moderators underdeveloped.
- Candidate evidence:
  - It identifies model regime as a major moderator, contrasting non-reasoning models with models having built-in reasoning.
  - It reports task and metric dependence, including differences between average accuracy, perfect accuracy, majority performance, mathematical tasks, logical tasks, and search-based evaluations.
  - It discusses trace structure and organized alternatives, citing Hi-CoT, COCOT, and PLaT.
  - It notes diminishing returns when models already produce internal or built-in reasoning and identifies inference budget as a fault line.
- Missing:
  - Training-distribution similarity is not substantively discussed.
  - Prompt and demonstration design are mentioned only indirectly through “generic” requests, exemplars, and structured traces; the report does not analyze demonstrations, wording, or prompt-control effects in detail.
  - Baseline prompting behavior is addressed mainly through the built-in-reasoning distinction, without a systematic comparison to direct-answer or naturally occurring CoT behavior.
  - The report does not clearly distinguish well-supported moderators from those that remain contested or untested, aside from a general limitations discussion.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is one of the report’s strongest sections: it directly addresses the reasoning-versus-formatting question, distinguishes outcome gains from causal faithfulness, and identifies a decisive missing control. It falls short of full coverage because the relevant ablations and alternative explanations are not examined in detail.
- Candidate evidence:
  - Finding 4 explicitly says that benefits may arise from response formatting or reasoning-like behavior rather than reliably improving the underlying solution process.
  - It states that visible explanations are not necessarily faithful records of the causal process and reports that editing displayed CoTs often left final answers largely unchanged.
  - It presents both computational explanations involving sequential intermediate steps and formatting/elicitation explanations.
  - It identifies the need for a controlled ablation holding formatting constant while measuring solution quality.
- Missing:
  - The report does not provide a detailed account of existing controlled evidence that separates additional context, verbosity, answer extraction, and formatting effects from intermediate-step execution.
  - It does not clearly distinguish whether extra generated tokens or context alone can account for gains, beyond mentioning latency and trace length.
  - The causal evidence remains largely summarized rather than technically analyzed, so the relative contribution of the proposed mechanisms remains unresolved.

### R5

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes additional computation, decoding, search, and output requirements as confounds, but it does not systematically separate these procedures from the effect of the CoT prompt itself.
- Candidate evidence:
  - The report identifies inference budget and compute as fault lines and notes that CoT increased response time by approximately 20–80% in the GPQA comparison.
  - It discusses Pass@k, search-based inference, majority performance, forward-pass counts, and the trade-off between explicit CoT and latent approaches.
  - It cautions that latent and explicit systems are not matched for models, training data, inference compute, and output requirements.
- Missing:
  - It does not cleanly isolate the CoT prompt from sampling, self-consistency, voting, or majority aggregation effects.
  - Answer extraction and formatting effects are mentioned conceptually but not evaluated as separate protocol components.
  - Calculators, code, retrieval, and other external tools are not meaningfully discussed.
  - Like-for-like baseline comparisons are limited; the report itself acknowledges that several comparisons are not apples-to-apples.

### R6

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report correctly foregrounds faithfulness and includes one relevant intervention-style finding, but treatment of the testing methodology and logical validity is too limited for full coverage.
- Candidate evidence:
  - It states that generated CoTs can be “plausible rationalizations.”
  - It reports that editing the displayed CoT often left final answers largely unchanged and that reported unfaithfulness increased with model size.
  - It explicitly distinguishes a successful or plausible written trace from evidence that the trace caused the answer.
- Missing:
  - Logical validity of the traces is not assessed separately from causal faithfulness.
  - The report does not discuss or evaluate trace scrambling, irrelevant-chain controls, counterfactual interventions, or systematic distribution-shift tests.
  - The editing result is summarized without explaining its design, controls, scope, or limitations.
  - It does not provide a nuanced assessment of when traces are faithful versus merely correlated with correctness.

### R7

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report understands that evidence is heterogeneous and flags secondary-source and replication limitations, but it does not perform the detailed methodological comparability assessment required by the rubric.
- Candidate evidence:
  - It notes differences in models, tasks, metrics, trace structures, and compute budgets as reasons headline results conflict.
  - It identifies variation among average accuracy, perfect accuracy, majority performance, Pass@k, efficiency, and diversity measures.
  - It acknowledges that some claims rely on secondary explainers or summaries and that robustness and independent replication are unclear.
  - It explicitly states that the evidence does not establish effects across a broad range of model sizes, prompts, and protocols.
- Missing:
  - The report does not systematically document model versions and sizes, datasets, exact baselines, prompting protocols, decoding settings, sample counts, or statistical uncertainty across studies.
  - It does not assess source quality in enough detail; it lists primary-looking papers alongside blogs, explainers, and forum posts without a structured reliability hierarchy.
  - Replication evidence is noted as unclear but not investigated or compared.
  - The report sometimes presents precise numerical results without enough protocol context to judge comparability.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The synthesis answers the central question in a qualified and evidence-sensitive way and addresses several practical trade-offs. It is not fully comprehensive on operational guidance, cost, and reliability.
- Candidate evidence:
  - The conclusion directly characterizes CoT as “effective but context-dependent,” not universally reliable, and rejects the claim that it is primarily formatting in all cases.
  - It identifies likely-useful settings—some difficult tasks and non-reasoning models—and diminishing returns for models with built-in reasoning.
  - It discusses latency, efficiency, accuracy, faithfulness, and inference-compute trade-offs.
  - It maintains uncertainty by stating that formatting and elicitation can matter without establishing that they explain all gains.
- Missing:
  - Cost is not discussed concretely beyond latency and forward-pass/compute implications.
  - Practical recommendations for when practitioners should use direct answering, CoT, self-consistency, tools, or hidden reasoning are limited.
  - Reliability implications are mostly framed through faithfulness and metric variation, without a fuller discussion of error modes, calibration, or robustness.
  - The conclusion could more clearly separate established empirical findings from hypotheses about the causal mechanism.

### Novel Value

- The report offers a useful synthesis that CoT effectiveness is conditional rather than universal, with particularly clear emphasis on differences between non-reasoning and reasoning-model regimes.
- It highlights the important distinction between visible trace plausibility and causal faithfulness, including the observation that editing traces may leave answers unchanged.
- It identifies metric choice—average accuracy, perfect accuracy, majority performance, Pass@k, efficiency, and diversity—as a concrete source of apparently conflicting conclusions.
- It usefully frames latent-reasoning results as evidence that reasoning and verbalization can be decoupled, while acknowledging that these are not matched tests of generic CoT prompting.

## Citations

### Support

#### F1: PARTIALLY_SUPPORTED

- Claim: CoT is conditionally effective rather than uniformly effective: the result depends on model type, task, benchmark difficulty, and evaluation criterion.
- Sources: S2, S1, S7, S8, S9, S3, S4, S5
- Rationale: S2 directly supports the central claim that CoT is not uniformly effective and that outcomes vary by model type and task. It also reports differing results under multiple evaluation thresholds, including average performance, majority accuracy, and perfect accuracy. S7 provides a further task-dependent example, reporting that a latent alternative outperformed CoT on some logical benchmarks but underperformed it on GSM8k. However, the supplied sources do not clearly establish benchmark difficulty as an independent determinant of CoT effectiveness; S2 mainly identifies model type, task, and evaluation criterion, while S1 discusses benchmarks of varying difficulty for Hi-CoT rather than standard CoT. The remaining sources largely make general positive claims about CoT and do not substantiate the full conditional formulation.
- Supporting text: S2: “its effectiveness varies significantly by model type and task”; non-reasoning models showed average gains but mixed perfect-accuracy results, while reasoning models saw minimal or negative effects. S2 also says that “different correctness thresholds significantly transform assessment outcomes.” S7 reports mixed benchmark results: COCONUT had lower accuracy than CoT on GSM8k but higher accuracy on two logical-reasoning benchmarks.

#### F2: SUPPORTED

- Claim: For the tested non-reasoning models on difficult GPQA Diamond questions, generic CoT improved average performance but could increase variability and reduce perfect-accuracy performance for some models.
- Sources: S2
- Rationale: S2 directly reports that CoT generally improved average performance across the tested non-reasoning models, while also increasing answer variability and producing mixed perfect-accuracy results, including significant declines for some models. The GPQA Diamond methodology and tested non-reasoning models are explicitly identified.
- Supporting text: S2 states: “CoT prompting generally improved average performance across non-reasoning models.” It also reports that perfect accuracy showed mixed results, with “other models” declining significantly, particularly Gemini Pro 1.5 (-17.2%), and concludes that CoT “can also introduce variability.”

#### F3: SUPPORTED

- Claim: For the tested reasoning models, a generic step-by-step request produced marginal accuracy changes and increased response time, consistent with diminishing incremental value when reasoning is already built into the model.
- Sources: S2, S4
- Rationale: S2 directly reports that, in the tested reasoning models, generic Chain-of-Thought prompting produced only small average accuracy changes (including decreases for one model) while increasing response time by 20–80%. It also explicitly attributes the limited value to built-in reasoning. S4 provides broader contextual support that reasoning models can self-direct their Chain-of-Thought process, though it does not independently substantiate the measured accuracy or time effects.
- Supporting text: S2 reports small average improvements for o3-mini (2.9%) and o4-mini (3.1%), a decrease for Gemini Flash 2.5 (-3.3%), and 20–80% longer response times; it concludes that generic CoT prompts provide limited value compared with models’ built-in reasoning.

#### F4: PARTIALLY_SUPPORTED

- Claim: Some apparent CoT benefits may arise from eliciting a response format or reasoning-like behavior rather than from reliably improving the underlying solution process, but the supplied evidence cannot determine the relative causal contribution of formatting and problem solving.
- Sources: S1, S2, S9, S7, S8, S3, S4, S5
- Rationale: The sources support important components of the claim: S1 explicitly reports that CoT exemplars may primarily enforce output format, while S9 states that displayed CoTs are often unfaithful and can be after-the-fact rationalizations. S2 further shows that CoT effects vary by model and task, with minimal benefits for reasoning models and many models producing CoT-like reasoning by default. However, the supplied excerpts do not directly establish that the observed benefits specifically arise from formatting rather than genuine problem solving, nor do they provide a causal decomposition of the relative contributions. Thus the uncertainty clause is reasonable, but the full causal claim is only partly supported.
- Supporting text: S1: modern LLM CoT exemplars “primarily serve to enforce output format rather than improve reasoning quality.” S9: “the CoT that a model provides is not always a faithful account of its true reasoning process,” and CoTs are often “after-the-fact rationalisation[s].” S2: CoT effectiveness varies by model and task; reasoning models receive only marginal benefits, and many models reason in a CoT-like way by default.

#### F5: SUPPORTED

- Claim: Additional structure can outperform flat CoT in some evaluations, indicating that the organization and constraints of a trace matter—not merely whether a trace is present.
- Sources: S1, S7, S8
- Rationale: S1 directly compares hierarchical, structured reasoning with conventional flat CoT and reports higher accuracy across multiple models and benchmarks, while also stating that strict adherence to the hierarchy maximizes accuracy and efficiency. S7 supplies a separate comparison in which latent COCONUT outperforms CoT on two logical-reasoning benchmarks, though not on GSM8K, supporting the qualified wording “in some evaluations.” S8 further reports that PLaT outperforms baselines on Pass@k scaling, but its lower greedy accuracy makes it supplementary rather than direct evidence for the full claim.
- Supporting text: S1: Hi-CoT “consistently improves average accuracy by 6.2%” and reports that accuracy and efficiency are maximized when models “strictly adhere to the hierarchical structure,” compared with conventional flat CoT. S7: COCONUT had higher accuracy than CoT on two logical-reasoning benchmarks, despite lower accuracy on GSM8K.

#### F6: SUPPORTED

- Claim: Latent-reasoning approaches suggest that reasoning and verbalization can be partially decoupled, with trade-offs among efficiency, accuracy, interpretability, and exploration.
- Sources: S7, S8
- Rationale: Both sources support the claim's central content. S8 explicitly presents latent reasoning as decoupled from verbalization and describes trade-offs involving accuracy and exploration, while also discussing efficiency and interpretability. S7 independently supports efficiency gains, reduced interpretability, mixed accuracy results, and exploration of multiple reasoning paths.
- Supporting text: S8 describes a Planner-Decoder architecture that “fundamentally decouples the reasoning process from verbalization,” with latent reasoning occurring before text decoding. It reports lower greedy accuracy but greater reasoning diversity and exploration potential, alongside dynamic termination and interpretability. S7 describes latent reasoning as more efficient but less interpretable than chain-of-thought, with mixed accuracy results and the ability to explore multiple paths simultaneously.

#### F7: SUPPORTED

- Claim: The main fault lines behind conflicting results are model regime, task structure, evaluation metric, inference budget, trace structure, and whether visible reasoning is treated as evidence of faithful computation.
- Sources: S2, S1, S7, S8, S9, S3, S4, S5, S10
- Rationale: Taken together, the sources support all six identified dimensions as factors that change reported reasoning outcomes. S2 explicitly reports variation by model type, task, evaluation threshold, and time/token cost. S1 and S8 discuss task complexity, reasoning-trace structure, path diversity, fixed versus dynamic inference steps, and differing metrics such as greedy accuracy and Pass@k. S7 and S9 distinguish visible language traces from latent reasoning and warn that visible CoT may not faithfully represent computation. The wording “main fault lines behind conflicting results” is a synthesis of these documented contrasts rather than a direct quotation.
- Supporting text: S2: CoT effectiveness “varies significantly by model type and task,” while different correctness thresholds produce different assessment outcomes and CoT increases time/token costs. S1/S8: unstructured versus hierarchical or latent traces, fixed versus dynamic inference budgets, and greedy accuracy versus Pass@k yield different results. S7/S9: latent reasoning is less interpretable, and visible CoT “is not always a faithful account” of the model’s true reasoning process.

### Missing Citations

- Q25: There is no matched comparison of latent and explicit reasoning under equivalent models, training data, inference compute, and output requirements.

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
- `structured_claim_evidence_available`: PASS
- `ledger_claim_ids_unique`: PASS
- `ledger_evidence_relationships_resolve`: PASS
- `ledger_confidence_values_valid`: PASS
- `ledger_evidence_ids_unique`: NOT_EVALUABLE — Current ledger relations have no independent evidence-ID field.

## Main Weaknesses

1. R1: Define chain-of-thought prompting and distinguish it from direct answering, answer-format instructions, hidden or internal reasoning, self-consistency, tool augmentation, and other inference-time procedures.
2. R2: Assess CoT’s effects on final-answer performance across multiple task types, including at least multi-step mathematical or symbolic tasks and tasks involving knowledge, commonsense, or open-ended reasoning.
3. R5: Separate the effects of the CoT prompt itself from effects of sampling, self-consistency or voting, longer generation, answer extraction, calculators, code, retrieval, or other external computation and scaffolding.
4. 2 cited finding(s) were not fully supported by saved evidence.
5. 1 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ac152f1d42cbe0f247f27e3225b834f4d7d35d3a27bade4d08806b371c248b6d`
- Candidate report hash: `b66d704067181df0a8fbb37c9394d4e28576e1f61469a6d999754a9b7081104e`
- LLM calls: 9
- Evaluated at: 2026-08-31T21:47:41.724134+00:00
