# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** remote-work-productivity

**System Version:** evidence-ledger-decomposer-verifier-v1

**Research Model:** gpt-4o-mini

**Evaluator Model:** gpt-5.6-luna

## Summary

- Overall: 31.6 / 100
- Evaluation completeness: 100%
- Coverage: 0.38
- Depth: 0.25

## Coverage and Depth

### R1

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report mentions several productivity measures and task categories, but it does not establish the arrangements, comparison groups, or measurement distinctions needed to avoid treating remote work and productivity as interchangeable.
- Candidate evidence:
  - The report distinguishes focused tasks from collaborative tasks: “Remote work can enhance productivity for focused tasks, but its impact on collaborative tasks varies.”
  - It mentions “13% more output per hour,” “total factor productivity growth,” self-reported productivity, and fewer hours worked.
- Missing:
  - It does not distinguish fully remote, hybrid, and predominantly office-based arrangements or specify the comparison condition in the cited findings.
  - It does not consistently define or separate output per hour, output per employee, quality, performance ratings, satisfaction, retention, and hours worked.
  - The report does not explain how different productivity measures affect the apparent result.

### R2

- Coverage: 0.25
- Depth: 0.25
- Rationale: A numerical experimental result is mentioned, but the report does not evaluate the experiment's design or applicability. A conclusion about a causal effect is asserted without the supporting experimental context.
- Candidate evidence:
  - It reports that a “Stanford study found a 13% performance boost for remote workers.”
  - It also states that a “controlled study” found “13% more output per hour from remote workers.”
- Missing:
  - The treatment and comparison conditions are not described.
  - The population, occupation, firm, schedule, and duration of the experiment are not identified.
  - The principal outcome is not clearly distinguished between performance, output, and output per hour.
  - The report does not explain causal limits, trial-specific conditions, statistical precision, or generalizability.
  - The two 13% claims may refer to the same study, but the report does not clarify this.

### R3

- Coverage: 0.25
- Depth: 0.25
- Rationale: The Microsoft communication finding is an observational-style claim, but its design and causal status are not explained. The report provides almost none of the comparison or bias analysis required for observational evidence.
- Candidate evidence:
  - The report cites a study of Microsoft employees showing that remote work made workers “more siloed in communication.”
  - It notes “contradictory evidence” suggesting productivity drops and says that studies use “differing methodologies and contexts.”
- Missing:
  - No observational, quasi-experimental, before-and-after, or natural-experiment designs are identified or evaluated.
  - There are no comparison groups, estimated effects, timing details, or credible causal estimates.
  - The report does not distinguish descriptive associations from causal evidence.
  - It does not discuss selection, confounding, concurrent shocks, or pandemic-era timing in a methodologically specific way.

### R4

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report recognizes aggregate and self-reported evidence, but it largely treats both as positive support and does not explain why either type is weaker or different from individual-level causal evidence.
- Candidate evidence:
  - It reports that “A BLS analysis found a positive link between remote work and total productivity growth.”
  - It separately reports that “77% of remote workers self-report higher productivity when working remotely.”
  - It labels the latter as a survey pattern and calls the former company/industry-level evidence.
- Missing:
  - The BLS measure, level of aggregation, time period, and analytical comparison are not described.
  - The report does not explain the limits of inferring individual or team effects from aggregate total-factor-productivity growth.
  - It does not discuss survey selection, representativeness, self-report bias, or the difference between perceived and measured productivity.
  - Firm-level evidence is not substantively assessed as a distinct category.

### R5

- Coverage: 0.50
- Depth: 0.25
- Rationale: There is a qualified overall conclusion, but the requested cross-method evidence weighting and comparison are largely absent.
- Candidate evidence:
  - The conclusion gives a qualified direction: remote work may improve productivity for focused tasks while creating challenges for collaborative work.
  - The report contrasts “productivity gains” with “productivity drops” and says outcomes vary by methodology and context.
- Missing:
  - It does not systematically compare experiments, observational studies, and company/industry data.
  - It does not compare magnitude, precision, consistency, or evidentiary strength across methods.
  - It does not identify which conclusions are supported by stronger causal evidence versus weaker descriptive or self-reported evidence.
  - The direct answer remains broad and does not explain whether the best evidence implies a typical positive, negative, or near-zero effect under specified arrangements.

### R6

- Coverage: 0.50
- Depth: 0.25
- Rationale: Task and collaboration differences are relevant explanations, but the report does not provide the broader methodological and institutional account of disagreement requested by the rubric.
- Candidate evidence:
  - The report attributes variation to “task type, communication practices, and individual circumstances.”
  - It distinguishes focused from collaborative work and says findings reflect “differing methodologies and contexts.”
  - It mentions that remote workers can become “more siloed in communication” and that communication and team-building may affect collaboration.
- Missing:
  - The report does not connect specific conflicts to identifiable study designs or settings in detail.
  - It does not discuss worker or firm selection, remote-work intensity or hybrid schedules, implementation quality beyond generic communication strategies, study horizon, pandemic conditions, or publication/reporting bias.
  - The explanations are mostly listed as general possibilities rather than demonstrated reasons for particular studies' conflicting results.

### R7

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report acknowledges broad heterogeneity and the need for more research, but it does not analyze external validity or distinguish short-term measured productivity from longer-term organizational effects.
- Candidate evidence:
  - It states that effects vary by “task type,” “job types,” and demographic factors including educational attainment and job sectors.
  - It says further research is needed on productivity across job sectors and educational levels.
  - It notes communication and collaboration challenges in remote work.
- Missing:
  - It does not assess heterogeneity across workers, occupations, firms, management practices, remote-work intensity, hybrid arrangements, or duration in a substantive way.
  - It does not identify important underrepresented settings or explain external-validity limits.
  - It does not separate immediate measured output from longer-term collaboration, innovation, learning, mentoring, or career progression.
  - Burnout is identified as a research gap, but the report does not address the major unresolved long-run productivity channels.

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

1. R1: Distinguish the remote-work arrangements and comparison conditions being evaluated, including fully remote, hybrid, and predominantly office-based work where relevant, and define productivity using measures such as output per hour, output per employee, quality, or performance ratings.
2. R2: Evaluate controlled or randomized evidence on remote work and productivity, stating the treatment and comparison, population or setting, principal productivity outcome, direction and approximate magnitude of the effect when available, and key limits on causal interpretation or generalization.
3. R3: Evaluate observational, quasi-experimental, before-and-after, or natural-experiment evidence, distinguishing descriptive associations from credible causal estimates and discussing relevant comparison groups, estimated effects, and threats from selection, confounding, timing, and concurrent shocks.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `e50bc516d4d756493b41fcaa430b164facfcb05a718934b8d5eb88b93b7e7d02`
- Candidate report hash: `2e9732576804e4a1030e1d0333bd6ea07e7cd1a44114099c10c2c1f6b2f434ae`
- LLM calls: 1
- Evaluated at: 2026-09-01T18:17:59.498460+00:00
