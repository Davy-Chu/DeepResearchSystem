# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** late-bronze-age-collapse

**System Version:** evidence-ledger-decomposer-verifier-v1

**Research Model:** gpt-4o-mini

**Evaluator Model:** gpt-5.6-luna

## Summary

- Overall: 28.3 / 100
- Evaluation completeness: 100%
- Coverage: 0.32
- Depth: 0.25

## Coverage and Depth

### R1

- Coverage: 0.00
- Depth: 0.00
- Rationale: The report assumes the subject without establishing its temporal, geographic, or societal boundaries.
- Candidate evidence:
- Missing:
  - The report does not define the relevant chronology, geographic scope, or societies.
  - It does not explain whether the collapse was a single event or a regionally uneven sequence.
  - It does not distinguish the failure of palatial institutions from population or cultural disappearance.

### R2

- Coverage: 0.75
- Depth: 0.50
- Rationale: Climate evidence and a basic causal mechanism are presented, along with a limited acknowledgment of uncertainty. However, regional variation, counterevidence, and the distinction between environmental stress and political causation receive insufficient treatment.
- Candidate evidence:
  - Finding 1 states that “severe climate conditions and agricultural failures around 1250 BCE” contributed to destabilization.
  - Finding 2 cites “pollen-derived climatic proxy” evidence for drier conditions in Syria in the late 13th and early 12th centuries BC.
  - Finding 3 refers to climate modeling showing “compounded drought conditions” in the Eastern Mediterranean.
  - The report acknowledges that “the extent to which climate change alone caused societal collapse” remains debated.
- Missing:
  - The report does not systematically connect specific climate proxies to the timing and locations of individual political or settlement disruptions.
  - Regional variation and counterexamples are largely absent; Syria and the Eastern Mediterranean are mentioned, but divergent outcomes are not analyzed.
  - The report often treats correlation between drought, agricultural stress, and collapse as support for causation without carefully separating environmental change from proof of political collapse.
  - The high-confidence claims that climate was a “primary cause” are not adequately justified.

### R3

- Coverage: 0.50
- Depth: 0.25
- Rationale: Warfare and destruction are mentioned, but the treatment is highly compressed and relies on an overconfident Sea Peoples interpretation rather than evaluating the evidentiary uncertainties required by the rubric.
- Candidate evidence:
  - Finding 4 claims that the Sea Peoples caused “significant destruction and decline in various civilizations.”
  - The report cites historical records describing the Sea Peoples as “a coalition of groups responsible for widespread havoc across coastal cities.”
  - The conclusion identifies warfare as one of several contributing factors.
- Missing:
  - The report does not distinguish evidence that destruction occurred from evidence identifying perpetrators or causal responsibility.
  - It does not examine the dating, scale, coordination, or geographic distribution of destruction events.
  - It presents the Sea Peoples as responsible for widespread destruction without adequately addressing whether they constituted a unified invasion or whether the evidence supports that interpretation.
  - It does not assess warfare independently of the Sea Peoples hypothesis or explain whether conflict was a cause, consequence, or amplifier.

### R4

- Coverage: 0.25
- Depth: 0.25
- Rationale: Migration is named but not substantively investigated.
- Candidate evidence:
  - The report mentions “migration” as a possible contributor in the summary and Finding 3.
  - Finding 4 links the Sea Peoples to “migration and military incursions.”
- Missing:
  - No direct evidence for population movement is presented.
  - The report does not distinguish migration evidence from inferences based on artifacts, language, or cultural change.
  - It does not assess the timing, scale, geographic distribution, or causal role of mobility, or its relationship to warfare and environmental stress.

### R5

- Coverage: 0.25
- Depth: 0.25
- Rationale: Trade disruption and economic instability appear only as labels in the summary and conclusion, with no substantive causal or evidentiary assessment.
- Candidate evidence:
  - The summary mentions “trade disruptions” as a contributor.
  - The conclusion refers to “economic instability” alongside climate change and warfare.
  - The report states that the relative contribution of “economic instability” remains part of the broader debate.
- Missing:
  - There is no evidence-based analysis of trade, tribute, resource-supply networks, or pre-crisis interdependence.
  - Internal political or institutional vulnerabilities are not examined through evidence of fiscal pressure, dynastic conflict, administrative weakness, or similar mechanisms.
  - The report does not distinguish causes from consequences or amplifiers.
  - It does not compare different polities or justify generalizing across the region.

### R6

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report signals uncertainty in general terms, but its confidence levels are not supported by a critical evaluation of evidence quality or methodological limitations.
- Candidate evidence:
  - The report uses confidence labels, including “High” for climate claims and “Medium” for the Sea Peoples claim.
  - It acknowledges that the extent to which climate change alone caused collapse is “debated.”
  - The report includes a general statement that “multiple factors collectively contributed to societal instability.”
- Missing:
  - It does not evaluate the quality, directness, chronology, geographic scope, or independence of the cited evidence.
  - Proxy uncertainty, model assumptions, incomplete archaeological records, propagandistic texts, and small genetic samples are not discussed.
  - It does not distinguish primary observations from later interpretations.
  - Temporal coincidence and correlation are repeatedly used without a sufficiently explicit warning against inferring causation.

### R7

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report favors a multiple-cause interpretation but does not actually compare explanatory power in a structured way.
- Candidate evidence:
  - The report says the collapse was a “complex interplay of various factors.”
  - The conclusion identifies “climate change, warfare, and economic instability” as combined contributors.
  - Finding 3 describes climate as exacerbating agricultural stresses while allowing that other factors contributed to instability.
- Missing:
  - No explicit and consistently applied comparison criteria are used.
  - The hypotheses are not compared for temporal fit, geographic reach, mechanisms, evidentiary support, or ability to explain survival and adaptation.
  - Systemic or cascading collapse is not developed as an integrative model; the report merely uses general language about interdependencies.
  - The report does not classify hypotheses as direct causes, contributing factors, consequences, or feedback mechanisms.

### R8

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report acknowledges uncertainty but provides no regional analysis or sufficiently differentiated classification of evidentiary confidence.
- Candidate evidence:
  - The report states that the relative contributions of climate, warfare, and economic instability remain debated.
  - The conclusion uses uncertainty-aware language, saying that “ongoing debate” remains about the factors’ relative contributions.
- Missing:
  - No divergent regional cases of collapse, continuity, adaptation, or reorganization are compared.
  - The conclusion does not test hypotheses against regional variation.
  - It does not clearly distinguish well-supported claims, plausible but unresolved claims, and speculation.
  - The conclusion is proportionate only at a general level and is not anchored in comparative evidence.

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

1. R1: Define the Late Bronze Age collapse in chronological, geographic, and societal terms before evaluating its causes.
2. R5: Assess whether trade disruption and internal political or institutional vulnerabilities contributed to the crisis.
3. R6: Evaluate the quality, directness, chronology, geographic scope, and independence of the evidence used for causal claims.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `9021488f3cc8dc340173f7d6fc6f0e3a242e7c5f64d05800f03f1c21158cde96`
- Candidate report hash: `a71d421cb3a3a2ac0d47bdaf7d0ea869293d5593ac153a9296bb074865b503d5`
- LLM calls: 1
- Evaluated at: 2026-09-01T18:17:21.021428+00:00
