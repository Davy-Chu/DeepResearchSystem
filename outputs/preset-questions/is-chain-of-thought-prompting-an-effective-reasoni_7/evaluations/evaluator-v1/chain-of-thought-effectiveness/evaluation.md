# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** chain-of-thought-effectiveness

**System Version:** evidence-ledger-decomposer-v1

**Model:** gpt-5.6-luna

## Summary

- Overall: 75.8 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.60
- Coverage: 0.62
- Depth: 0.53
- Citation quality: 1.00
- Citation validity: 1.00
- Citation support: 1.00
- Citation completeness: 1.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report supplies a basic description and mentions direct-answer, unprompted, and tool-based conditions, but the required taxonomy of neighboring interventions and comparison conditions is incomplete. The available evidence is largely descriptive rather than a carefully framed conceptual analysis.
- Candidate evidence:
  - The report describes CoT as asking models to show intermediate steps: “asking models to show intermediate steps” [S4].
  - It distinguishes explicit step-by-step prompting from “direct-answer and unprompted conditions” [S2].
  - It discusses external deterministic solvers and tool execution as distinct from visible reasoning traces [S6, S10].
- Missing:
  - It does not clearly define the intervention in a systematic way or distinguish few-shot demonstrations from zero-shot CoT.
  - Self-consistency, sampling/voting, hidden or internal reasoning, answer-format instructions, retrieval, calculators, and other inference-time procedures are not explicitly separated.
  - The report does not establish which comparison conditions are being used in each cited study.

### R2

- Coverage: 0.75
- Depth: 0.50
- Rationale: Multiple task families are represented, and the report acknowledges gains, null effects, and harms. However, the empirical assessment is thin and uneven: GPQA receives the most detail, while other task categories are summarized without enough methodological or quantitative context.
- Candidate evidence:
  - On GPQA Diamond, generic CoT is reported to produce gains for some non-reasoning models, nonsignificant effects for some combinations, and declines for others [S2, S11].
  - Hi-CoT is reported across five mathematical benchmarks and 13 model configurations, with claimed accuracy improvements relative to CoT [S1].
  - A comparison across six models and six datasets involving real-world knowledge and logical verbal reasoning reports robust but variable zero-shot CoT gains [S12].
- Missing:
  - The report provides little task-level detail about the mathematical, symbolic, knowledge, commonsense, and open-ended tasks, making it difficult to assess which kinds of reasoning benefit.
  - It does not systematically compare CoT with direct answering across all task families.
  - The evidence is mostly abstract-level or secondary-source reporting, with limited uncertainty, effect sizes, or replication.

### R3

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes several relevant moderators and explicitly lists important gaps, but it does not develop them into a literature-based explanation of conflicting results. The central boundary conditions remain largely unresolved.
- Candidate evidence:
  - The report describes different effects for non-reasoning and reasoning models, including small or negative effects for some reasoning models [S2, S11].
  - It reports variation across models and datasets and says that an automatically discovered prompt benefited GPT-4 most [S12].
  - It identifies missing evidence concerning “model scales and training regimes, prompt variants, decoding settings, and strong non-CoT baselines.”
- Missing:
  - Model capability is discussed mainly as a reasoning-versus-non-reasoning distinction; systematic scale effects are not established.
  - Task difficulty and structural properties are not analyzed in detail.
  - Training-distribution similarity is identified as a gap but not explained with evidence.
  - Prompt and demonstration design are only briefly mentioned, and baseline prompting behavior is not systematically analyzed beyond the claim that some models reason by default.
  - The report does not clearly distinguish supported moderators from hypotheses or contested findings.

### R4

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report identifies the key conceptual distinction and cites process-sensitive evidence, but it mostly states that the relevant controls are missing. It therefore frames the issue better than it resolves it.
- Candidate evidence:
  - Finding 4 states that performance improvements should not automatically be interpreted as faithful visible reasoning [S6, S7, S10].
  - The report distinguishes faithfulness from accuracy and cites editing, truncation, and answer-information-availability findings [S7, S10].
  - It explicitly identifies the need to control for “output-format instructions, generated-token or test-time-compute budgets, answer extraction procedures, and other evaluator-visible verbosity effects.”
- Missing:
  - There is little direct evidence separating formatting or extraction effects from genuine intermediate computation effects.
  - The report does not compare CoT with equivalent-length verbosity, answer-format controls, irrelevant rationales, or hidden-reasoning conditions.
  - It does not explain whether additional context, token allocation, or sequential computation could help even when the displayed trace is unfaithful.
  - The conclusion does not synthesize the competing mechanisms into a clear judgment.

### R5

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes cost and some tool-related confounding, but it does not perform the required attribution analysis across inference-time procedures.
- Candidate evidence:
  - The report reports substantial token and response-time increases from CoT [S2, S11].
  - It notes that external tool execution substantially reduced intervention fragility [S6].
  - It warns that gains may reflect “generated-token or test-time-compute budgets,” answer extraction, or other protocol differences.
- Missing:
  - Sampling, self-consistency, voting, and decoding temperature are not substantively analyzed.
  - Calculators, code, retrieval, and other tools are not separated from the CoT prompt in the empirical comparisons.
  - The report does not present like-for-like baselines that hold token budgets, compute, decoding, and extraction procedures constant.
  - It does not determine whether reported improvements come from the CoT instruction itself or from longer generation and extra computation.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is one of the strongest sections. It includes causal-intervention evidence and correctly separates trace faithfulness from answer accuracy, while acknowledging that the evidence does not generalize straightforwardly to all free-form CoT.
- Candidate evidence:
  - Finding 6 reports deterministic counterfactual interventions on structured reasoning mediators across eight models and three benchmarks, with failures to update predictions in up to 60% of cases [S6].
  - The report cites CoT perturbation, bias injection, editing, truncation, and cases where answer information may be available before the CoT is generated [S7, S10].
  - It explicitly distinguishes faithfulness from accuracy and notes that visible reasoning need not causally determine the final decision [S6, S10].
- Missing:
  - Most intervention evidence concerns structured intermediate representations or selected CoT-related behaviors rather than ordinary free-form CoT prompting.
  - The report does not assess the logical validity of traces in detail, such as premise validity, derivation correctness, or consistency with the final answer.
  - It does not systematically discuss scrambling, irrelevant-chain controls, or distribution-shift tests.
  - It does not establish how often unfaithful traces nonetheless provide useful causal computation.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report is appropriately cautious and directly flags major comparability and source-quality problems. Nevertheless, it does not supply the detailed cross-study audit needed to fully evaluate the literature.
- Candidate evidence:
  - The report labels the Hi-CoT evidence low confidence because detailed tables, statistical tests, baseline implementation details, and independent replication are unavailable [S1].
  - It characterizes the GPQA evidence as relying partly on an industry blog and notes that this does not materially broaden the direct evidence [S11].
  - It identifies missing comparability information about model scales, training regimes, prompt variants, decoding settings, statistical testing, dataset difficulty, and non-CoT baselines [S12].
  - It warns that the supplied material consists of one focused empirical report, one method paper, and primarily explanatory or industry sources rather than a balanced replicated literature.
- Missing:
  - The report does not systematically inventory model versions and sizes, datasets, metrics, decoding settings, or uncertainty for each study.
  - It does not independently verify the cited headline results or reconcile differences in evaluation protocols.
  - Replication quality and source quality are discussed, but not with a study-by-study comparative assessment.
  - The source set includes blogs and explanatory pages, yet the report does not clearly separate peer-reviewed evidence from secondary claims throughout.

### R8

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report provides useful caution and some practical cost information, but its own incomplete-status disclaimer substitutes for a final conclusion. It does not deliver the requested integrated answer or actionable implications.
- Candidate evidence:
  - The report repeatedly characterizes CoT as context-dependent, with gains, null effects, and declines across models [S2, S11].
  - It reports substantial increases in token use and response time [S2, S11].
  - The conclusion explicitly states that the evidence is provisional and that important gaps remain.
- Missing:
  - The conclusion does not directly answer whether CoT is effective, primarily formatting, or a combination of mechanisms.
  - It does not synthesize established findings versus hypotheses into a clear qualified position on the central question.
  - Practical implications for reliability, accuracy, latency, cost, and appropriate deployment are not developed beyond reporting cost and time increases.
  - It does not state when practitioners should prefer direct answering, CoT, structured reasoning, or external tools.
  - The report ends with unresolved gaps rather than a completed evidence-based synthesis.

### Novel Value

- No material benchmark-external value identified.

## Citations

### Support

#### F1: SUPPORTED

- Claim: In the supplied empirical report, generic CoT prompting produced context-dependent final-answer effects on GPQA Diamond: it generally improved average performance for tested non-reasoning models, but effects ranged from modest or nonsignificant gains to declines under a perfect-accuracy criterion; for tested reasoning models, gains were small and one model declined.
- Sources: S2, S11
- Rationale: S2 directly reports the GPQA Diamond methodology and findings summarized in the claim. It states that CoT generally improved average performance for non-reasoning models, including a smallest 4.4% gain that was not statistically significant, while perfect-accuracy results were mixed and some models declined. It also reports small gains for o3-mini and o4-mini and a decline for Gemini Flash 2.5 among reasoning models. S11 independently paraphrases several of these findings, though S2 is the primary direct support.
- Supporting text: S2: “CoT prompting generally improved average performance across non-reasoning models”; GPT-4o-mini had the “smallest gain” at “4.4%, not statistically significant,” while perfect accuracy was mixed and Gemini Pro 1.5 declined “-17.2%.” For reasoning models, o3-mini and o4-mini showed small average improvements of 2.9% and 3.1%, while Gemini Flash 2.5 declined by 3.3%. S11 likewise reports 11–13% average gains for selected non-reasoning models, a 17.2% perfect-accuracy decline for Gemini Pro 1.5, and only 2–3% gains for reasoning models.

#### F2: SUPPORTED

- Claim: The supplied evidence indicates that generic CoT can impose substantial inference-time cost, with reported increases in response time of 35–600% for non-reasoning models and 20–80% for reasoning models in the GPQA study.
- Sources: S2, S11
- Rationale: S2 directly reports that, in its GPQA Diamond study, CoT requests took 35–600% longer for non-reasoning models and 20–80% longer for reasoning models. S11 independently repeats both ranges and attributes them to the Wharton study.
- Supporting text: S2: “CoT requests took 35-600% (5-15 seconds) longer than direct requests” for non-reasoning models, and “required 20-80% (10-20 seconds) more time” for reasoning models. S11 likewise states that CoT requests take 35–600% longer and that reasoning models take 20–80% longer.

#### F3: SUPPORTED

- Claim: The supplied sources support a distinction between generic flat CoT and more structured inference procedures: the Hi-CoT paper reports higher accuracy and shorter traces than its CoT comparison on the evaluated mathematical benchmarks, attributing the proposed method to hierarchical decomposition and compression bottlenecks.
- Sources: S1
- Rationale: S1 explicitly contrasts conventional CoT as unstructured and flat with Hi-CoT as a structured, hierarchical procedure. It reports average accuracy improvements and shorter reasoning traces compared with CoT across five mathematical reasoning benchmarks, and attributes the method to hierarchical decomposition and compression bottlenecks.
- Supporting text: S1 states that conventional CoT uses “unstructured, flat reasoning chains,” while Hi-CoT “decomposes the reasoning process into hierarchical substeps.” It reports that Hi-CoT improves average accuracy by 6.2% and reduces reasoning-trace length by 13.9% “compared to CoT prompting” across five mathematical reasoning benchmarks. It also describes alternating instruction/execution steps as “compression bottlenecks.”

#### F4: SUPPORTED

- Claim: Several supplied sources describe CoT as eliciting or encouraging stepwise decomposition and improved final-task performance, but these descriptions do not by themselves establish that the visible rationale is faithful to the model’s causal reasoning process.
- Sources: S4, S5, S6, S7, S10, S12
- Rationale: The sources collectively support both parts of the claim. S4, S5, S10, and S12 describe CoT as prompting or encouraging sequential/intermediate reasoning and report improved accuracy or performance on complex or multistep tasks. S6, S7, and S10 explicitly distinguish apparent or visible reasoning from causal faithfulness, reporting failures under interventions, post-hoc reasoning, or that CoT is not always a faithful account. Thus, the claim’s qualified wording—that these descriptions alone do not establish causal faithfulness—is supported.
- Supporting text: S4: CoT “breaks down intricate problems into manageable steps” and leads to “more accurate final answers.” S5: it guides models through “a step-by-step reasoning process” and intermediate steps “significantly boost” accuracy. S10: CoT “encourages models to ‘think’ in stages,” but “is not always a faithful account” of the true reasoning process. S6 reports that intermediate structures can be “influential context rather than stable causal mediators,” while S7 describes models potentially going “through the motions” of CoT after deciding the answer.

#### F5: SUPPORTED

- Claim: The supplied report finds that many tested models produced CoT-like reasoning by default without an explicit step-by-step instruction, making an unprompted or default condition an important baseline when estimating the incremental value of generic CoT.
- Sources: S2
- Rationale: S2 explicitly states that the default condition produced short CoT-like output in most cases and that many models performed CoT-like reasoning without explicit instructions. It also describes a direct comparison between default behavior and step-by-step prompting, supporting the importance of the default condition for assessing incremental CoT value.
- Supporting text: The report defines “Default” as providing no specific suffix and says, “In most cases, this produces a short CoT-like thinking output.” It further states that “many models perform CoT-like reasoning by default, even without explicit instructions,” and reports comparisons between unprompted answers and Chain-of-Thought.

#### F6: SUPPORTED

- Claim: Controlled intervention evidence in the supplied sources indicates that explicit intermediate structures are not reliably causal mediators of LLM decisions: across eight models and three benchmarks, models sometimes failed to change predictions after the structures were edited, with failures reported in up to 60% of cases; external tool execution substantially reduced this fragility.
- Sources: S6
- Rationale: The saved source’s abstract directly reports evaluation across eight models and three benchmarks, failures to update predictions after controlled interventions in up to 60% of cases, and that delegating final-decision derivation to an external tool substantially reduces the fragility. Its conclusion characterizes intermediate structures as influential context rather than stable causal mediators.
- Supporting text: S6 states: “Across eight models and three benchmarks, models appear self-consistent with their own intermediate structures but fail to update predictions after intervention in up to 60% of cases.” It also says: “When derivation of the final decision from the structure is delegated to an external tool, this fragility largely disappears,” and concludes that intermediate structures function as “influential context rather than stable causal mediators.”

#### F7: SUPPORTED

- Claim: In a small-scale comparison across six LLMs and six question-answering datasets involving real-world knowledge and logical verbal reasoning, zero-shot CoT variants showed gains that the study describes as robust across models and datasets, with GPT-4 benefiting most from an automatically discovered reasoning prompt.
- Sources: S12
- Rationale: The saved abstract directly supports all major elements of the claim: the study is small-scale; compares six named LLMs and six question-answering datasets; the datasets involve real-world knowledge application and logical verbal reasoning; the strategies are induced by zero-shot prompting; gains from CoT strategies are described as robust across models and datasets; and GPT-4 benefits most from state-of-the-art strategies, performing best with a prompt previously discovered through automated discovery.
- Supporting text: The abstract states: “In this small-scale study, we compare different reasoning strategies induced by zero-shot prompting across six recently released LLMs” and “test them on six question-answering datasets that require real-world knowledge application and logical verbal reasoning.” It concludes that “gains from CoT reasoning strategies remain robust across different models and datasets” and that “GPT-4 benefits the most” and performs best with “a prompt previously discovered through automated discovery.”

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
- `structured_claim_evidence_available`: PASS
- `ledger_claim_ids_unique`: PASS
- `ledger_evidence_relationships_resolve`: PASS
- `ledger_confidence_values_valid`: PASS
- `ledger_evidence_ids_unique`: NOT_EVALUABLE — Current ledger relations have no independent evidence-ID field.

## Main Weaknesses

1. R1: Define chain-of-thought prompting and distinguish it from direct answering, answer-format instructions, hidden or internal reasoning, self-consistency, tool augmentation, and other inference-time procedures.
2. R3: Explain how observed effects vary with model capability or scale, task difficulty and structure, training-distribution similarity, prompt or demonstration design, and baseline prompting behavior.
3. R5: Separate the effects of the CoT prompt itself from effects of sampling, self-consistency or voting, longer generation, answer extraction, calculators, code, retrieval, or other external computation and scaffolding.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `ac152f1d42cbe0f247f27e3225b834f4d7d35d3a27bade4d08806b371c248b6d`
- Candidate report hash: `9bc47bacb9c81fd5d356682e24e68078275fcf3a27a382409718f6587db79a72`
- LLM calls: 9
- Evaluated at: 2026-09-01T01:19:00.250138+00:00
