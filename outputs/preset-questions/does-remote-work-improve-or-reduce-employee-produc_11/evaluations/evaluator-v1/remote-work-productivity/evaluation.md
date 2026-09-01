# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** remote-work-productivity

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 81.8 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.77
- Coverage: 0.79
- Depth: 0.71
- Citation quality: 0.86
- Citation validity: 1.00
- Citation support: 0.75
- Citation completeness: 1.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 1.00
- Depth: 0.75
- Rationale: The report substantially distinguishes arrangements and outcomes and avoids treating productivity, hours, satisfaction, and retention as interchangeable. Its treatment is somewhat less systematic in defining and comparing the productivity metrics.
- Candidate evidence:
  - The report distinguishes “hybrid,” “fully remote,” and “office workers,” including two remote days per week, intermediate hybrid schedules, and mostly home-based work.
  - It identifies productivity outcomes including calls, coding, revenue, manager ratings, promotions, hours, firm productivity, and total-factor productivity.
  - It separately discusses retention, satisfaction, well-being, communication, and isolation, and notes that these can improve even when measured performance is unchanged.
- Missing:
  - The report does not give a single explicit operational definition of productivity or systematically explain how output per hour differs from output per employee, hours worked, quality, and performance ratings.
  - The predominantly office-based comparison condition is present mainly as a control group rather than fully characterized as a distinct work arrangement.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report covers the principal experiments, treatments, comparisons, outcomes, directions, and some limits. It falls short of fully evaluating each experiment because effect sizes, precision, populations, and design details are incomplete.
- Candidate evidence:
  - The randomized Trip.com study is described as comparing employees working from home two days per week with office workers, finding no significant differences in reported performance, promotions, coding, revenue, or hours, while resignations fell by about one-third.
  - The BRAC field experiment is described as randomizing office attendance among administrative workers and finding improved manager ratings, email communication, information conveyed, work-life balance, and isolation outcomes under an intermediate hybrid schedule.
  - The Ctrip randomized call-center experiment is reported to find about 13.5% higher call output for mostly home-based workers, attributed to more minutes worked and greater efficiency per minute.
  - The report explicitly limits generalization by noting that the experiments concern specific employers, occupations, countries, and relatively limited time periods, and acknowledges that some primary experimental evidence was available only through summaries.
- Missing:
  - The BRAC experiment lacks an approximate magnitude for its reported performance effects.
  - The report does not consistently state treatment compliance, trial duration, sample characteristics, or statistical precision for each experiment.
  - The causal interpretation and generalizability limits are acknowledged but not developed separately for each experiment, especially the Ctrip call-center result and the BRAC study.

### R3

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report correctly warns against treating observational associations and pandemic-era changes as causal, but its methodological evaluation of comparison groups and identification threats is comparatively thin.
- Candidate evidence:
  - The report distinguishes observational and survey evidence from causal evidence, stating that perceived productivity does not establish that remote work caused the outcomes.
  - It reports the HBS longitudinal survey finding that 70% of small-business owners initially perceived a decline, while the median owner reported a positive effect by early 2021.
  - It describes a BLS positive association between remote-work adoption and total-factor-productivity growth but says the available material lacks sufficient identification details to establish causality.
  - It identifies pandemic transition, technology investment, training, task redesign, and management practices as potential concurrent changes.
- Missing:
  - Comparison groups and explicit quasi-experimental or before-and-after designs are not systematically described.
  - Selection, confounding, timing, and concurrent-shock threats are mentioned only generally; the report does not explain how they affect each cited observational estimate.
  - The report provides few estimated magnitudes beyond the survey percentage and does not distinguish clearly between descriptive associations, longitudinal change, and credible causal estimates for each source.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report clearly separates company-level, survey, and aggregate evidence from individual causal evidence and identifies important limits, though its treatment of industry-level evidence and aggregation problems could be more explicit.
- Candidate evidence:
  - The Italian study is treated as firm-level evidence distinct from individual experiments and is described as measuring firm-level productivity using administrative data and a fibre-broadband instrumental-variable strategy.
  - The report separately discusses business-owner survey perceptions and the BLS aggregate association with total-factor-productivity growth.
  - It notes that experiments measure individual outcomes whereas the Italian study measures firm-level productivity, and explicitly states that it remains unclear how experimental individual-output effects translate into aggregate firm outcomes.
  - It identifies omitted or unavailable company-level measures including revenue, value added, total-factor productivity, and innovation, and notes representativeness and generalizability limitations across firms and countries.
- Missing:
  - Industry-level and aggregate evidence is not developed as a broad category beyond the brief BLS reference.
  - The report does not fully explain ecological inference problems—for example, why firm-level productivity changes cannot be assigned to individual employees or teams even when remote-work adoption is instrumented.
  - Survey representativeness and self-report bias are noted but not examined in detail.

### R5

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report provides a strong conditional synthesis and direct answer, but its cross-method comparison of magnitude, precision, and consistency is incomplete because it largely reports unavailable statistical detail.
- Candidate evidence:
  - The conclusion gives a qualified answer: “Remote work neither simply improves nor reduces productivity.”
  - It synthesizes hybrid evidence as generally preserving individual performance, fully remote evidence as positive for some measurable independent tasks but negative for some collaborative or onboarding-intensive work, and firm-level evidence as showing initial pandemic costs followed by adaptation.
  - It compares units of analysis and outcomes, noting that experiments measure calls, ratings, coding, promotions, communication, and retention, whereas the Italian study measures firm-level productivity.
  - It distinguishes stronger causal evidence from weaker evidence by labeling the experiments as causal and the BLS and survey results as associations or perceptions.
- Missing:
  - The report does not systematically compare precision, confidence intervals, or the relative consistency of the evidence; it mainly notes that such information is unavailable.
  - The magnitude comparison is incomplete: the 13.5% call-center estimate is reported, but most other directions lack comparable effect sizes.
  - The conclusion could more explicitly rank the evidentiary strength of controlled experiments versus firm-level instrumental-variable and survey evidence.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report offers a well-supported, evidence-linked explanation for conflicting results across tasks, schedules, outcomes, selection, and adaptation. It is not complete because reporting bias and several mechanisms are only lightly treated.
- Candidate evidence:
  - The report links conflicting findings to occupation and task, distinguishing focused individual work from collaboration, onboarding, mentoring, knowledge sharing, and creative problem-solving.
  - It identifies differences in remote-work intensity and schedule, contrasting fully remote call-center work with two-day hybrid and intermediate hybrid arrangements.
  - It explains that outcome definitions differ, including calls, ratings, coding, promotions, communication, retention, satisfaction, and firm-level productivity.
  - It connects pandemic-era negative results to forced adoption, incomplete technology and training, task redesign, and remote-management practices, and contrasts these with later adaptation.
  - It discusses selection and measurement concerns and notes possible broadband/ICT confounding in the Italian instrumental-variable design.
- Missing:
  - Publication or reporting bias is not meaningfully assessed, despite the rubric identifying it as a relevant possible source of conflict.
  - Worker and firm self-selection are mentioned but not tied in detail to particular studies or directions of bias.
  - The report gives limited concrete discussion of management implementation quality, study horizon, or how coordination demands generate specific measured effects beyond general statements.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report provides substantial heterogeneity, external-validity, duration, and long-run-outcome discussion. It remains incomplete because several underrepresented settings and longer-term mechanisms are identified mainly as unanswered questions.
- Candidate evidence:
  - The report identifies heterogeneity by occupation, collaboration demands, newly hired status, firm size, ICT investment, worker qualifications, country, seniority, home conditions, management practices, and voluntary versus imposed remote work.
  - It notes that experimental evidence concerns selected employers and limited periods and that generalizability across countries, occupations, worker seniority, home conditions, and firms is uncertain.
  - It separates immediate measured performance from unresolved long-run effects on innovation, mentoring, onboarding, knowledge accumulation, and organizational productivity.
  - It explicitly states that it remains unclear how individual-output effects translate into aggregate firm outcomes.
- Missing:
  - Career progression is mentioned only indirectly through promotions in the Trip.com study and is not evaluated as a longer-term uncertainty.
  - The report does not identify specific underrepresented populations or settings in enough detail, such as particular occupations, worker demographics, or low-resource home environments.
  - Long-run collaboration, learning, innovation, and progression are listed as gaps but are not synthesized into a more detailed assessment of the likely direction or uncertainty of those effects.

### Novel Value

- The report offers a useful cross-level synthesis: hybrid experiments can show neutral individual performance and improved retention, while firm-level pandemic evidence can show short-run productivity losses without implying a contradiction.
- It emphasizes organizational complements—ICT investment, training, task redesign, and remote-management capability—as a mechanism connecting adaptation over time to heterogeneous firm outcomes.
- It distinguishes measured individual output from broader organizational outcomes and uses that distinction to explain why retention, well-being, communication, and firm productivity may move differently.

## Citations

### Support

#### F1: SUPPORTED

- Claim: Hybrid work generally preserves measured individual performance and may improve retention, satisfaction, and communication.
- Sources: S1, S7, S8, S9
- Rationale: The cited snapshots provide direct evidence for the claim, especially for the studied hybrid-work settings. S1 and S7 report no measurable or equal performance relative to fully in-office work, alongside lower attrition and higher satisfaction. S8 independently summarizes reduced attrition and improved satisfaction without detectable performance damage. S9 reports better manager performance ratings, improved work-life balance, lower isolation, and increased email communication and information exchange. The word “generally” is a broad synthesis, but the sources collectively support it within the populations and contexts studied.
- Supporting text: S1: Hybrid employees had “zero negative effect on performance reviews or promotions,” while resignations dropped 33%. S7: the schedule “improved retention and satisfaction” and produced “equal employee success”; hybrid employees also reported higher work-life balance and life satisfaction. S8: hybrid work “reduced attrition and improved satisfaction without detectable damage to” performance. S9: intermediate office attendance produced better manager performance ratings, greater work-life balance, lower isolation, and more emails, recipients, and information conveyed.

#### F2: PARTIALLY_SUPPORTED

- Claim: Fully remote work can increase individual output in some settings, but its effects are more context-dependent than those of the studied hybrid arrangements.
- Sources: S1, S9
- Rationale: S1 directly supports the first part: it reports a 13% performance increase for fully remote call-center workers, while also describing 10–20% output reductions in some roles, especially highly collaborative roles and newly hired workers. This supports context dependence. S1 and S9 support favorable outcomes for hybrid arrangements, but the supplied text does not establish the comparative claim that fully remote effects are more context-dependent than those of the studied hybrid arrangements. S9 instead reports that hybrid effects varied with the number of office days and found benefits for intermediate hybrid work.
- Supporting text: S1: “The 2015 Ctrip study found a 13% performance increase for fully remote call center workers,” while a 2023 paper found fully remote work “reduced output by 10-20% for some roles.” S9: the experiment found that an “intermediate number of days in the office” improved work-life balance, communication, and manager performance ratings.

#### F3: SUPPORTED

- Claim: Observational and survey evidence often reports stable or improving perceived productivity, but it does not by itself establish that remote work caused those outcomes.
- Sources: S4, S2
- Rationale: Both sources report survey or observational associations indicating stable or improved productivity perceptions or output. S4 explicitly describes business owners’ and workers’ survey responses and reports that perceived productivity shifted from a dip to a positive impact over time. S2 summarizes survey and other observational findings of stable or improved output. The claim’s causal qualification is also supported: the reported evidence is presented as perceptions, associations, or correlations, not as proof that remote work caused the outcomes.
- Supporting text: S4: “70 percent of small business owners perceived a productivity dip due to remote work,” while “the median owner report[ed] a positive productivity impact by early 2021.” S2: “most research shows stable or improved output” and reports a “positive association” between remote-work adoption and productivity growth.

#### F4: SUPPORTED

- Claim: Company-level evidence indicates short-run productivity losses during forced pandemic adoption, followed by recovery or heterogeneous effects as firms adapt.
- Sources: S12, S15, S16, S17
- Rationale: The saved sources consistently report firm-level evidence of substantial productivity losses during the pandemic, followed by no significant longer-term effect and heterogeneous outcomes: larger and ICT-equipped firms mitigated losses, while firms with highly qualified workers showed suggestive productivity gains. “Forced” is not stated verbatim, but the sources describe pandemic-driven adoption and use the pandemic as a common shock.
- Supporting text: S12: “the COVID-19 pandemic-driven shift to work from home initially reduced productivity, but these losses disappeared as firms adapted.” S15/S16/S17: WFH had a “large negative impact on productivity during the pandemic”; in the longer term, its impact was “no longer significant,” with larger, ICT-investing, and highly qualified-worker firms experiencing different outcomes.

#### F5: PARTIALLY_SUPPORTED

- Claim: The apparent disagreement among studies is mainly explained by differences in treatment, tasks, populations, outcomes, and adaptation stage.
- Sources: S1, S3, S9, S7, S12, S4, S15, S16, S17
- Rationale: The sources support the broader idea that mixed findings vary with treatment or work arrangement, task type, population or firm characteristics, outcomes, and adaptation stage. However, the claim says these factors are the main explanation, which is a stronger synthesis than the supplied evidence explicitly establishes. S1 and S3 directly identify work type, collaboration requirements, and management or work-design factors; S12, S15, S16, and S17 describe differences by firm capabilities, ICT investment, worker qualifications, and adaptation over time. S9 and S7 show that hybrid versus fully remote or in-office treatments produce different outcomes. The supplied excerpts do not clearly discuss all cited studies collectively or demonstrate that these factors are mainly responsible.
- Supporting text: S1: “The answer depends on what you measure, who you study, and how you manage the transition,” and the difference is attributed to “which tasks and which workers benefit.” S12: productivity effects “depend on complementary investments in digital technologies, organisational capacity, and skills”; losses initially reduced productivity but “disappeared as firms adapted.” S4: perceived productivity shifted over time as firms made technological, training, and task-related adjustments.

#### F6: PARTIALLY_SUPPORTED

- Claim: Remote work can produce organizational benefits even when measured individual output is unchanged, while individual productivity measures may omit longer-run coordination and learning effects.
- Sources: S7, S8, S9
- Rationale: The sources support organizational or employee benefits alongside unchanged or undamaged measured performance: S7 reports improved retention and satisfaction with equal employee success, S8 says retention and satisfaction improved without detectable performance damage, and S9 reports greater communication, information conveyed, and better manager performance ratings. However, none of the supplied text supports the specific assertion that individual productivity measures may omit longer-run coordination and learning effects. The evidence is also primarily about hybrid work, not remote work generally.
- Supporting text: S7: The hybrid approach “improved retention and satisfaction” and resulted in “equal employee success.” S8: “hybrid working reduced attrition and improved satisfaction without detectable damage to” performance. S9: hybrid work produced “more unique information conveyed in the emails” and better manager performance ratings.

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

1. R3: Evaluate observational, quasi-experimental, before-and-after, or natural-experiment evidence, distinguishing descriptive associations from credible causal estimates and discussing relevant comparison groups, estimated effects, and threats from selection, confounding, timing, and concurrent shocks.
2. 3 cited finding(s) were not fully supported by saved evidence.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `e50bc516d4d756493b41fcaa430b164facfcb05a718934b8d5eb88b93b7e7d02`
- Candidate report hash: `83f944b5bd20337bdb8b192215715c386e9cf4db74327d8d5150e6d2dc326d55`
- LLM calls: 8
- Evaluated at: 2026-09-01T09:25:35.377581+00:00
