# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** remote-work-productivity

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 82.1 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.75
- Coverage: 0.75
- Depth: 0.75
- Citation quality: 0.90
- Citation validity: 1.00
- Citation support: 0.86
- Citation completeness: 0.94
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report provides a strong treatment and outcome taxonomy and explicitly distinguishes hours from productivity. It falls short of full coverage because quality and related non-productivity outcomes are not analyzed in comparable depth.
- Candidate evidence:
  - The report distinguishes fully remote work in the IT study, remote versus office work in the Ctrip experiment, and hybrid versus five-office-days work in the Trip.com experiment.
  - It distinguishes total output, output per hour, calls per minute, performance reviews, promotions, code output, revenue, labor productivity, and total-factor productivity.
  - It explicitly states that “total effort, total output, and productivity per hour can move in different directions” and warns against treating “output per hour, total output, quality, innovation, retention, and firm-level productivity” as interchangeable.
- Missing:
  - Quality is mentioned as a relevant measure but is not substantively evaluated in the evidence.
  - The report discusses retention and satisfaction, but could more sharply separate these outcomes from productivity throughout the analysis.
  - Predominantly office-based work is represented mainly as the comparison condition rather than discussed as a distinct arrangement.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report identifies the experimental treatments, populations, outcomes, and one approximate effect, and appropriately limits generalization. It does not fully evaluate the experiments’ precision, trial implementation, or causal-estimation details.
- Candidate evidence:
  - It describes the 2015 randomized Ctrip assignment of call-center workers to remote or office conditions and reports about 13.5% more calls, attributed to more minutes worked and more calls per minute.
  - It describes the 2024 Trip.com randomized experiment with 1,612 professional employees assigned to hybrid work or five office days, finding no statistically significant difference in performance reviews, promotions, code output, or marketing revenue.
  - It notes that the experiments cover a repetitive call-center setting and engineering, marketing, and finance employees, and warns that these settings do not represent all work.
- Missing:
  - The Ctrip treatment duration and comparison details are not supplied, and the report acknowledges that the original article was not retrieved.
  - The Trip.com experiment’s null result is not accompanied by effect sizes or confidence intervals, so precision and practical equivalence are unclear.
  - Limits on causal interpretation and generalization are present but relatively brief; the report does not discuss compliance, attrition, statistical power, or possible spillovers in detail.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is substantial observational treatment with an effect estimate and several threats to causal inference. Full coverage would require more detail on the comparison design, identification credibility, and how the reported estimate should be interpreted causally.
- Candidate evidence:
  - The Gibbs, Mengel, and Siemroth study is identified as using personnel and analytics data from more than 10,000 IT professionals and as comparing productivity before and during the pandemic rather than randomly assigning remote work.
  - The report gives the estimated pattern: hours increased by roughly 30%, average output did not significantly change, and output per hour declined by 8%–19%.
  - It explicitly identifies pandemic shocks, worker selection, industry composition, changed tasks, technology investment, changed task assignments, training, and remote-management changes as threats to attribution.
- Missing:
  - The report does not clearly explain the study’s specific comparison group or identification strategy beyond the before/during comparison.
  - It does not distinguish in much detail between a descriptive before-and-after association and a more credible quasi-experimental estimate.
  - Timing, demand changes, and other confounders are listed, but the report does not assess their likely direction or how the study attempts to address them.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report correctly separates aggregate evidence and explains the ecological and confounding limitations. It does not fully develop survey evidence or company-level measurement and representativeness.
- Candidate evidence:
  - The report treats company- and industry-level evidence as a separate category and reports BLS analyses across 61 and 43 private-sector industries.
  - It distinguishes total-factor-productivity growth from labor productivity and notes that one analysis found a positive association while another found little relationship.
  - It states that aggregate measures operate at a different level from individual output and may reflect sector composition and concurrent changes; it also notes that company and sector evidence cannot always separate remote work from technology, management, selection, and pandemic changes.
- Missing:
  - Survey evidence is only mentioned indirectly through “survey evidence” about simultaneous adjustments; its sample, measure, and representativeness are not described.
  - The report gives limited detail about the company-level metrics or how firm-level results map—or fail to map—to individual employees and teams.
  - Selection and representativeness limitations are stated generally rather than evaluated for each aggregate or survey source.

### R5

- Coverage: 0.75
- Depth: 0.75
- Rationale: The direct answer is appropriately conditional and evidence-weighted, with useful cross-method comparison. It lacks a fuller treatment of precision, uncertainty intervals, and comparative evidentiary strength.
- Candidate evidence:
  - The conclusion gives a qualified answer: remote work “neither universally improves nor universally reduces productivity.”
  - It synthesizes positive call-center results, a null measured-performance result for hybrid professional work, and negative hourly-productivity results for fully remote coordination-intensive IT work.
  - It distinguishes stronger randomized evidence from observational and aggregate evidence and explains that company- and industry-level results are mixed and less able to isolate remote work.
- Missing:
  - The comparison of precision and magnitude across methods is incomplete: only some effects have approximate magnitudes, and null-result precision is not assessed.
  - The report does not systematically compare consistency or evidentiary strength across all three categories, particularly the quality and limitations of the aggregate analyses.
  - The synthesis could more explicitly state which conclusion is best supported overall—for example, preservation under hybrid work versus uncertain effects of fully remote work.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: The conflict explanation is substantially evidence-linked rather than merely generic, especially regarding task type, arrangement, coordination, and measurement. It is not fully comprehensive because implementation and reporting bias receive little or no treatment.
- Candidate evidence:
  - The report connects conflicting results to concrete differences between a repetitive call-center experiment, a hybrid professional-worker experiment, and a fully remote IT-services study.
  - It links coordination-intensive work to more meetings, less uninterrupted work, reduced networking, and fewer coaching and one-to-one meetings.
  - It identifies differences in remote-work intensity, task coordination, outcome measures, worker and firm characteristics, pandemic conditions, technology investment, management changes, and study horizon.
- Missing:
  - Implementation quality is not examined in a concrete way, such as how firms managed hybrid coordination, training, or monitoring.
  - Publication or reporting bias is not discussed.
  - Some factors, including occupation and collaboration demands, are well connected to study evidence, but others are presented mainly as plausible methodological possibilities rather than evaluated explanations.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report handles heterogeneity, external validity, and long-run uncertainty well at a high level and avoids treating unmeasured outcomes as established effects. Full coverage would require deeper assessment of duration, adaptation, and underrepresented populations.
- Candidate evidence:
  - The report notes differences across call centers, IT professionals, and engineering, marketing, and finance employees, and identifies uncertainty about generalization to software development, creative work, professional services, managers, and other collaborative knowledge jobs.
  - It states that effects may depend on task requirements, coordination demands, management practices, and whether work is hybrid or fully remote.
  - It separates short-run output findings from unresolved longer-run outcomes including innovation, mentoring, onboarding, networking, promotion, and career development, and explicitly says the material does not establish causal effects for those outcomes.
- Missing:
  - Underrepresented workers and settings are listed but not assessed in detail; for example, managerial work, lower-wage occupations, and firms with different organizational capabilities are not analyzed.
  - The report provides little evidence about duration beyond pandemic-era or trial-period observations and does not quantify how effects evolve with adaptation.
  - It mentions possible innovation and career effects but does not evaluate the evidence or uncertainty around each outcome in depth.

### Novel Value

- The report offers a useful conditional synthesis separating fully remote from hybrid work rather than treating remote work as a single treatment.
- It clearly decomposes productivity into hours, total output, and output per hour, showing how these can move in opposite directions.
- It explains the apparent conflict by aligning study results with task coordination demands, work arrangement, population, and measurement rather than forcing a universal conclusion.

## Citations

### Support

#### F1: SUPPORTED

- Claim: Controlled experiments suggest that remote work can improve individual productivity in highly measurable, relatively independent jobs, but hybrid work appears mainly to preserve performance rather than increase it.
- Sources: S1, S5, S7, S8
- Rationale: The cited sources directly support both parts of the claim. S1 and S7 describe randomized evidence of a productivity increase for call-center work, characterized as measurable and relatively independent, while S5 summarizes randomized experiments as finding small positive effects on individual productivity. S7 and S8 report that the Trip.com hybrid experiment found no performance damage or statistically significant productivity improvement, supporting the characterization that hybrid work mainly preserves performance. The claim appropriately uses qualified language (“can,” “suggest,” and “appears”).
- Supporting text: S7: The Ctrip randomized trial found a 13% performance increase, and the subjects’ work was described as “one of the most measurable, most independent, least collaborative job categories.” S8: The hybrid study is titled “improves retention without damaging performance”; S1 reports no measurable productivity difference between hybrid and in-office workers.

#### F2: PARTIALLY_SUPPORTED

- Claim: The strongest observational evidence in the retrieved material indicates that fully remote work can reduce productivity per hour in coordination-intensive IT work, even when employees work more hours.
- Sources: S10, S12, S13
- Rationale: The sources consistently report observational evidence from more than 10,000 IT professionals showing increased hours, little or slightly lower average output, and an 8–20% decline in productivity per hour during the work-from-home period. They also report increased coordination and meeting time and reduced uninterrupted work. However, the snapshots do not explicitly establish that the work was fully remote, do not directly characterize it as the “strongest” evidence, and do not formally define the work as coordination-intensive. S10 and S13 are duplicate versions of the same abstract, while S12 is a related published-version abstract.
- Supporting text: S12: “Hours worked increased… Average output declined slightly and employee productivity fell 8-19%.” It attributes the decline in part to “higher communication costs,” with coordination and meeting time increasing while uninterrupted work hours shrank. S10/S13 similarly report roughly 30% more hours, unchanged average output, and productivity falling by about 20%.

#### F3: SUPPORTED

- Claim: Total effort, total output, and productivity per hour can move in different directions.
- Sources: S10, S12, S13, S1, S5
- Rationale: S10 and S13 directly provide an example in which total hours worked increased, average output did not significantly change, and productivity fell. S12 likewise reports increased hours, a slight decline in average output, and an 8–19% fall in productivity per hour. This demonstrates that the three measures can move in different directions. S5 adds broader context that productivity findings vary by level and measure.
- Supporting text: S10/S13: “Total hours worked increased by roughly 30%... Average output did not significantly change. Therefore, productivity fell by about 20%.” S12: “Hours worked increased... Average output declined slightly and employee productivity fell 8-19%.”

#### F4: SUPPORTED

- Claim: Company- and industry-level data do not yield a uniform conclusion.
- Sources: S5, S14
- Rationale: The cited sources report mixed or differentiated findings rather than a single consistent conclusion. S5 describes positive effects in some firm experiments, declines in some single-firm case studies, little aggregate industry relationship in one study, and a positive association between remote work and TFP growth across 61 industries. S14 likewise states that remote work manifests differently across sectors because tasks vary in suitability.
- Supporting text: S5: “A few randomized experiments at individual firms identify small positive effects,” while “a couple of single-firm case studies” found short-run productivity declines; its 61-industry analysis found a positive association with TFP growth. S14: “The shift has however manifested differently in different sectors and for different groups, primarily because some tasks are more suitable for remote work than others.”

#### F5: SUPPORTED

- Claim: Remote work may produce organizational benefits even when it does not increase direct measured output.
- Sources: S1, S5, S8
- Rationale: The saved sources directly support this claim, particularly for hybrid remote work: measured performance or output was unchanged, while retention improved and turnover-related costs could fall. S1 and S8 report no significant productivity/performance difference alongside lower resignation or improved retention; S5 explicitly notes that lower turnover can reduce firms’ hiring costs.
- Supporting text: S8: “Hybrid working from home improves retention without damaging performance.” S1: hybrid workers showed “no measurable productivity difference” while reporting higher satisfaction and lower attrition. S5: remote work was associated with “lower job turnover,” which “could substantially reduce firms’ hiring costs.”

#### F6: SUPPORTED

- Claim: Different studies conflict because they examine different treatments, populations, tasks, and outcomes rather than one identical version of remote work.
- Sources: S7, S8, S12, S1, S4, S10, S14, S5
- Rationale: The saved sources directly support the claim’s central explanation: studies vary in work arrangement, populations and sectors, task characteristics, and productivity measures. They describe contrasting findings across fully remote and hybrid treatments, call-center workers, IT professionals, university-educated employees, and industry-level data, while noting different outcome measures such as output per hour, performance ratings, turnover, and aggregate productivity.
- Supporting text: S5 states that results depend on “the types of tasks workers perform, the available technology, the home environment, worker motivation, and management practices,” and that studies use “various proxies” for productivity. S14 adds that remote work’s effects differ across sectors and groups because “some tasks are more suitable for remote work than others,” while distinguishing remote work from work from home. S7 contrasts a call-center RCT, a hybrid trial of engineers, marketers and finance staff, IT-professional data, surveys, and industry-level correlations.

#### F7: PARTIALLY_SUPPORTED

- Claim: Observational and aggregate studies cannot cleanly attribute all observed productivity changes to remote work alone.
- Sources: S10, S12, S13, S2, S5
- Rationale: The sources support the broader caution that productivity findings vary across study designs, measures, firms, industries, and contextual factors, making attribution difficult. However, they do not explicitly state that observational and aggregate studies cannot cleanly attribute all changes to remote work alone. S10, S12, and S13 describe a before/during-WFH comparison and associated communication and coordination changes, while S2 reports survey-based perceptions that shifted over time and mentions accompanying technological, training, and task changes. S5 explicitly notes that productivity depends on factors beyond remote work, including task type, technology, home environment, motivation, and management practices, and presents differing individual and aggregate findings.
- Supporting text: S5: “The answer likely depends on several factors, including the types of tasks workers perform, the available technology, the home environment, worker motivation, and management practices.” It also reports that individual studies find both positive and negative effects, while an aggregate 43-industry study found little relationship between remote-work suitability and labor productivity.

### Missing Citations

- Q30: The conclusion states that fully remote work can raise output in measurable, relatively independent jobs, hybrid work can preserve professional employees’ measured performance while improving retention, and fully remote work can lower output per hour in coordination-intensive IT work.
- Q31: The conclusion states that company- and industry-level results are mixed because they capture broader organizational and sector effects and cannot always separate remote work from technology, management, selection, and pandemic changes.

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

1. 2 cited finding(s) were not fully supported by saved evidence.
2. 2 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `e50bc516d4d756493b41fcaa430b164facfcb05a718934b8d5eb88b93b7e7d02`
- Candidate report hash: `678e94fa50bebac5855cf8650843158efca18b63308243a693e5ab71d6e240a9`
- LLM calls: 9
- Evaluated at: 2026-09-01T07:11:48.317538+00:00
