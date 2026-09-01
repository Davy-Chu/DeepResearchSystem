# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** remote-work-productivity

**System Version:** evidence-ledger-v1

**Research Model:** gpt-4o-mini

**Evaluator Model:** gpt-5.6-luna

## Summary

- Overall: 32.2 / 100
- Evaluation completeness: 100%
- Coverage: 0.39
- Depth: 0.25

## Coverage and Depth

### R1

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report provides some arrangement and task heterogeneity, but it lacks an explicit outcome definition and does not adequately separate productivity from related outcomes.
- Candidate evidence:
  - The report distinguishes “individual focused tasks” from “collaborative tasks,” stating effects of “+10%” and “-4%,” and mentions “hybrid work models” alongside office-based peers.
  - It identifies job type, boundary clarity, cooperation structures, and interruption management as relevant factors.
- Missing:
  - It does not clearly distinguish fully remote, hybrid, and predominantly office-based comparison conditions.
  - It does not define the productivity measures used. The report does not say whether the cited effects refer to output per hour, output per employee, quality, performance ratings, or another metric.
  - It does not distinguish productivity from hours worked, satisfaction, retention, or work-life balance; in fact, it treats work-life balance and satisfaction as possible productivity-related benefits without clarifying the distinction.
  - It does not explain how measurement choices affect findings.

### R2

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report offers several unattributed effect-size claims but does not evaluate controlled experimental evidence as a distinct category or explain what experiments causally establish.
- Candidate evidence:
  - The report cites claims that remote work can produce “+10%” for individual focused tasks and “-4%” for collaborative tasks.
  - It states that remote workers can be “35-40% more productive than their office-based peers” and that some roles experience an “8–19%” or “20%” decline.
- Missing:
  - No controlled or randomized experiment is identified by design, treatment, comparison group, population, setting, or trial duration.
  - The principal productivity outcome and measurement method are not provided for any purported experiment.
  - The report does not establish which cited figures come from experiments rather than meta-analyses, surveys, opinion pieces, or other sources.
  - It gives no discussion of causal limitations, study-specific external validity, statistical precision, or generalization beyond particular firms, occupations, schedules, or trial periods.

### R3

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report gestures toward aggregate and economy-wide evidence but does not assess observational methodology or causal credibility.
- Candidate evidence:
  - The report mentions “aggregate productivity growth across 61 industries” and says this suggests effects depend on specific job types and management practices.
  - It cites pandemic-related and economy-wide productivity claims as part of the evidence.
- Missing:
  - No observational, quasi-experimental, before-and-after, or natural-experiment study is described with its comparison group or design.
  - The report does not distinguish descriptive associations from credible causal estimates.
  - It does not discuss selection, confounding, timing, concurrent pandemic shocks, worker composition, or other threats to causal interpretation.
  - It does not explain why observational findings might differ from experimental findings.

### R4

- Coverage: 0.25
- Depth: 0.25
- Rationale: There is a minimal reference to industry-level aggregate evidence, but almost none of the required assessment of company- and industry-level evidence is supplied.
- Candidate evidence:
  - It reports “little relationship between remote work and aggregate productivity growth across 61 industries.”
  - It refers to “economy-wide productivity growth” and to remote workers being more productive than office-based peers.
- Missing:
  - Company-level, industry-level, survey, and aggregate evidence are not separated into distinct evidence types.
  - The report does not identify what the company, industry, or survey measures actually capture.
  - It does not explain why aggregate productivity, firm performance, or self-reported perceptions cannot straightforwardly establish effects on individual employees or teams.
  - It omits discussion of representativeness, selection into remote work, and ecological inference limitations.

### R5

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report gives a qualified context-dependent conclusion and recognizes divergent directions, but it lacks cross-method synthesis and evidence weighting.
- Candidate evidence:
  - The conclusion says remote-work effectiveness “is contingent on numerous factors” and rejects “a universal setting.”
  - The report contrasts gains for “individual productivity” or focused tasks with drawbacks in “collaborative environments.”
  - It notes that aggregate industry data show “little relationship” while some cited studies report sizable positive or negative effects.
- Missing:
  - The report does not systematically compare experiments, observational studies, and company- or industry-level data because those categories are not identified and evaluated separately.
  - It does not compare precision, consistency, or evidentiary strength across methods.
  - It provides no evidence-weighted judgment about which findings are more credible or causal.
  - The direct answer remains largely generic and does not specify whether the strongest evidence indicates improvement, reduction, or near-zero average effects under particular arrangements.

### R6

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report identifies occupation and collaboration as plausible sources of heterogeneity, but its explanation of conflicting findings is not methodologically developed or study-linked.
- Candidate evidence:
  - The report attributes conflicting outcomes to “job type,” “interruption management,” “cooperation structures,” “boundary clarity,” “management practices,” and “organizational culture.”
  - It specifically contrasts individual-focused tasks with collaborative tasks and roles relying on “teamwork” and “immediate feedback.”
- Missing:
  - The explanations are mostly listed rather than connected to identified studies, designs, populations, or measured outcomes.
  - It does not discuss remote-work intensity or schedule, implementation quality in concrete terms, study horizon, measurement method, pandemic conditions, worker or firm selection, or publication/reporting bias in explaining the conflicts.
  - It does not show how any of these factors could produce the reported differences or distinguish causal mechanisms from generic possibilities.

### R7

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report acknowledges broad contextual variation but does not substantively evaluate external validity or unresolved short- versus long-term effects.
- Candidate evidence:
  - The report says effects vary by “job type, management practices, and organizational culture,” and mentions individual adaptability, focused versus collaborative work, and hybrid arrangements.
  - It states that remote work may affect satisfaction and work-life balance and that collaboration may be hindered.
- Missing:
  - It does not assess heterogeneity across workers, occupations, firms, management practices, or durations in a concrete evidence-based way.
  - It does not identify underrepresented settings or limits to external validity.
  - It does not separate immediate measured output from longer-term effects on collaboration, innovation, learning, mentoring, or career progression.
  - The statement “No major remaining gap was identified” is inconsistent with the report's failure to address long-run outcomes and other important uncertainties.
  - It does not discuss uncertainty, statistical precision, or the implications of short trial periods and pandemic-era evidence.

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

1. R2: Evaluate controlled or randomized evidence on remote work and productivity, stating the treatment and comparison, population or setting, principal productivity outcome, direction and approximate magnitude of the effect when available, and key limits on causal interpretation or generalization.
2. R3: Evaluate observational, quasi-experimental, before-and-after, or natural-experiment evidence, distinguishing descriptive associations from credible causal estimates and discussing relevant comparison groups, estimated effects, and threats from selection, confounding, timing, and concurrent shocks.
3. R1: Distinguish the remote-work arrangements and comparison conditions being evaluated, including fully remote, hybrid, and predominantly office-based work where relevant, and define productivity using measures such as output per hour, output per employee, quality, or performance ratings.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `e50bc516d4d756493b41fcaa430b164facfcb05a718934b8d5eb88b93b7e7d02`
- Candidate report hash: `e9f5dcd117cabcfb2a926c210c398ee755e6ef02f6474c66477c2db9f68bb2ec`
- LLM calls: 1
- Evaluated at: 2026-09-01T16:19:54.247225+00:00
