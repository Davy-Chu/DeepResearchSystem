# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** remote-work-productivity

**System Version:** llm-only-baseline-v0

**Model:** gpt-5.6-luna

## Summary

- Overall: 63.4 / 100
- Evaluation completeness: 80%
- Comprehensiveness: 0.89
- Coverage: 0.93
- Depth: 0.79
- Citation quality: 0.00
- Citation validity: 0.00
- Citation support: 0.00
- Citation completeness: 0.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 1.00
- Depth: 0.75
- Rationale: The report clearly avoids treating all remote arrangements and productivity measures as interchangeable. It distinguishes full-time remote from hybrid work, output per hour from hours worked, and short-run output from broader organizational outcomes. The treatment is substantial, though the definitions and evidence for quality-related measures could be more explicit.
- Candidate evidence:
  - The summary distinguishes fully remote and hybrid work and states that effects depend on “the job, the degree of remote work, employee selection, management practices, and how productivity is measured.”
  - The report distinguishes output per hour from total output and notes measures including “call volume, completed patent applications, software commits, and hours worked.”
  - It explicitly separates productivity from retention, promotion, collaboration, innovation, quality, and career outcomes, noting that “productivity and career outcomes can diverge.”
- Missing:
  - Productivity is discussed through examples rather than given a concise formal definition at the outset.
  - Some outcomes, especially quality and customer outcomes, are identified as important but are not evaluated with much evidence.

### R2

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report gives treatment and comparison conditions, settings, outcomes, approximate magnitudes, causal interpretation, and external-validity limits for multiple controlled or quasi-controlled examples. It appropriately distinguishes full remote from hybrid and does not generalize the results universally.
- Candidate evidence:
  - The Ctrip randomized experiment is described as assigning call-center employees to work from home for nine months versus an implied office comparison, finding about 13% higher performance and roughly halved attrition.
  - The report explains the mechanism and outcome: the Ctrip gain was “largely through more minutes worked and fewer breaks,” in a setting with highly observable output and limited face-to-face collaboration.
  - The Trip.com randomized trial is described as assigning thousands of employees to hybrid work versus full-time office work, with no detectable decline in performance reviews, promotion rates, or code output and resignations falling by approximately one-third.
  - The report identifies limits: Ctrip covered “one company and one occupational setting,” while Trip.com mainly involved educated employees in one technology/travel-services company and tested a specific hybrid schedule.
  - The USPTO policy study is reported as finding an approximately 4.4% productivity increase, with an explicit caveat that not all policy-based studies are pure randomized experiments and that the occupations have unusually measurable output.
- Missing:

### R3

- Coverage: 1.00
- Depth: 0.75
- Rationale: The report substantially evaluates observational and quasi-experimental evidence and correctly distinguishes pandemic associations and collaboration proxies from causal output estimates. It would be stronger with more concrete comparison-group and design details for the cited observational studies.
- Candidate evidence:
  - The Indian IT study is identified as observational and is reported to find an 8% to 19% productivity reduction, with longer hours but lower output per hour.
  - The report explains that pandemic health, childcare, demand, routine, and technology shocks make the estimate specific to crisis conditions.
  - It identifies coordination and communication time as a mechanism in the Indian study rather than treating longer hours as higher productivity.
  - The Microsoft collaboration analysis is explicitly described as using proxies rather than directly establishing lower output or profits.
  - The report states that firm-level before-and-after comparisons lack a credible counterfactual unless work location changed for reasons unrelated to expected productivity, and notes selection, technology, workforce-composition, demand, and policy confounding.
- Missing:
  - The observational section gives limited detail about specific comparison groups, timing, or identification strategies beyond general warnings about confounding and counterfactuals.
  - Selection and timing threats are discussed more generally than demonstrated study by study, and the report does not clearly classify which estimates are credible causal estimates versus descriptive associations in every example.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report treats aggregate, company, and survey evidence as distinct from individual-level causal evidence and explains important inferential limits. Coverage is not full because the empirical assessment of this category remains relatively nonspecific.
- Candidate evidence:
  - A dedicated finding states that “Company-level productivity data do not provide a clean verdict” because firms changed many things at once and measure output imperfectly.
  - The report distinguishes firm-level studies and company reports from aggregate productivity statistics, noting that aggregate figures reflect “industry composition, labor hoarding, supply constraints, demand shifts, digitization, and employee turnover.”
  - It separately discusses surveys, stating that employee and manager perceptions are vulnerable to self-reporting, question wording, selection, and differences between perceived and measured productivity.
  - It explains that company-level evidence cannot identify effects on individual employees or teams and that stable output and declines in innovation or coordination can coexist across teams.
- Missing:
  - The company- and industry-level evidence is described largely in general terms; few concrete company or industry datasets, effect estimates, or survey results are identified beyond the broad perception that the gap is small.
  - Representativeness and selection limitations are mentioned but not developed separately for company reports, aggregate statistics, and surveys.

### R5

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report provides a well-qualified answer and meaningful cross-method synthesis with several magnitudes and caveats. It falls short of full depth because precision and consistency are discussed qualitatively rather than evaluated directly.
- Candidate evidence:
  - The conclusion gives a qualified direct answer: remote work “neither universally improves nor universally reduces productivity.”
  - It synthesizes that full-time remote work often improves short-run individual output in measurable jobs, can reduce productivity in coordination-heavy or abruptly disrupted settings, and that hybrid work has the strongest evidence of being productivity-neutral while improving retention.
  - The report compares approximate magnitudes including 13% higher Ctrip performance, 4.4% higher USPTO productivity, 8% to 19% lower Indian IT productivity, and no detectable Trip.com performance decline.
  - It explicitly distinguishes stronger causal evidence from weaker evidence, noting that the Microsoft study identifies a mechanism but “does not directly establish lower output or profits,” and that aggregate statistics cannot identify the causal effect.
- Missing:
  - The cross-method comparison does not systematically assess precision, confidence intervals, statistical power, or consistency of estimates.
  - The relative evidentiary strength of company-level versus observational versus experimental findings is conveyed, but not summarized in a compact, explicit hierarchy or synthesis of where methods converge and diverge.

### R6

- Coverage: 1.00
- Depth: 0.75
- Rationale: The report gives connected, evidence-relevant explanations rather than a generic list. It covers most major sources of conflict and ties them to particular findings, although publication or reporting bias and some implementation mechanisms are omitted.
- Candidate evidence:
  - The report attributes conflicting results to different occupations and tasks, contrasting focused, individually measurable work with coordination-heavy, feedback-intensive, physical, apprenticeship, or creative work.
  - It distinguishes voluntary remote work from involuntary pandemic remote work, citing differences in suitable homes, self-management, childcare disruption, equipment, and organizational dislocation.
  - It distinguishes full-time remote from hybrid work and connects hybrid's preserved face-to-face coordination to the Trip.com finding of no output penalty.
  - It explains that measurement choices matter: output per hour, total output, quality, mentoring, innovation, customer relationships, and coordination costs can produce different apparent effects.
  - It discusses pandemic timing and concurrent shocks, management quality, implementation conditions, study horizon, and selection.
  - It links Microsoft’s more siloed communication to a plausible long-run mechanism while explicitly warning that the proxy does not prove lower productivity.
- Missing:
  - Publication or reporting bias is not discussed.
  - Some mechanisms, such as management quality and implementation quality, are identified but receive less study-specific evidence than occupation, schedule, and pandemic conditions.

### R7

- Coverage: 1.00
- Depth: 0.75
- Rationale: The report strongly addresses external validity, heterogeneity, underrepresented settings, and the distinction between short-run output and longer-run organizational effects. Depth is somewhat limited because most subgroup and long-horizon claims are caveats or research gaps rather than quantified evidence.
- Candidate evidence:
  - The report repeatedly identifies heterogeneity by occupation, task, worker selection, firm, management practices, remote-work intensity, and schedule.
  - It identifies underrepresented or uncertain groups and settings, including less experienced employees, new hires, managers, workers with unequal home-office conditions, multiple industries, occupations, and countries.
  - It separates immediate measured output from longer-term outcomes, stating that innovation, onboarding, promotion equity, and organizational learning remain less precisely estimated.
  - It calls for longer follow-up on innovation, mentoring, promotion, employee development, and organizational learning, and for measures of quality, rework, customer outcomes, and coordination costs.
  - It notes that the strongest hybrid experiment tested one schedule and one company and therefore cannot establish effects for every industry or managerial system.
- Missing:
  - The report does not provide much concrete evidence about how effects vary by specific worker groups, firms, or management practices; these differences are mainly framed as plausible or unresolved heterogeneity.
  - Long-term outcomes are identified as uncertain, but the report offers limited empirical estimates of their direction or magnitude.

### Novel Value

- The report offers a useful evidence-weighted synthesis distinguishing full-time remote work from hybrid work rather than treating remote work as a single intervention.
- It combines causal estimates, observational estimates, aggregate limitations, measurement issues, and longer-run uncertainty into a conditional conclusion.
- It explicitly separates productivity from retention, promotion, collaboration, innovation, and hours worked, which helps explain why apparently conflicting findings can coexist.

## Citations

### Support

#### F1: NOT_EVALUABLE

- Claim: In controlled experiments, fully remote work can increase productivity in jobs with individually measurable output, but the result is not generalizable to all occupations.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F2: NOT_EVALUABLE

- Claim: Hybrid work appears capable of maintaining performance while improving retention, at least for knowledge workers whose jobs can be performed partly remotely.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F3: NOT_EVALUABLE

- Claim: Other controlled or quasi-controlled studies find remote-work productivity gains, especially where workers benefit from geographic flexibility and have clear individual output measures.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F4: NOT_EVALUABLE

- Claim: Observational studies often report productivity losses when remote work is introduced during disruption, especially when hours rise without a proportional increase in output.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F5: NOT_EVALUABLE

- Claim: Observational evidence also indicates that remote work can impair collaboration and innovation even when individual task completion is unaffected.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F6: NOT_EVALUABLE

- Claim: Surveys and broad observational datasets usually find a smaller average effect than simple claims of either a large productivity gain or a large productivity loss.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F7: NOT_EVALUABLE

- Claim: Company-level productivity data do not provide a clean verdict because firms changed many things at once and commonly measure output imperfectly.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F8: NOT_EVALUABLE

- Claim: The main reason studies conflict is that they estimate different treatment effects for different people, jobs, schedules, and periods rather than estimating one common effect.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F9: NOT_EVALUABLE

- Claim: Measurement choices substantially affect the apparent productivity effect.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

### Missing Citations

- Q1: In a randomized experiment at Ctrip, employees assigned to work from home for nine months achieved approximately 13% higher performance, largely through more minutes worked and fewer breaks, and attrition was roughly halved.
- Q2: The Ctrip experiment involved call-center work with highly observable output and relatively limited dependence on face-to-face collaboration.
- Q3: A large randomized trial at Trip.com found that hybrid employees had no detectable decline in performance reviews, promotion rates, or code output, while resignations fell by approximately one-third.
- Q4: The Trip.com experiment tested a schedule involving two remote days per week.
- Q5: A study of the U.S. Patent and Trademark Office found that a work-from-anywhere policy increased examiner productivity by approximately 4.4% and improved worker retention and geographic flexibility.
- Q6: A randomized or policy-based study of call-center employees found that working from home increased measured productivity but was associated with fewer promotions for remote workers.
- Q7: Using detailed records from an Indian information-technology company during the pandemic, researchers estimated that working from home reduced productivity by roughly 8% to 19%, depending on the specification, while employees worked longer hours and output per hour fell.
- Q8: The Indian information-technology-company study found that coordination and communication consumed more time under remote work.
- Q9: Analysis of Microsoft collaboration data found that remote work made communication networks more static and siloed, with fewer cross-group connections and less synchronous interaction.
- Q10: The Microsoft collaboration analysis did not directly establish lower output or profits.
- Q11: The Survey of Working Arrangements and Attitudes and related U.S. research find that employees and managers generally perceive working from home as modestly less productive than office work, with a small gap that varies by occupation and worker circumstances.
- Q12: Post-pandemic evidence shows that employers have largely settled on hybrid arrangements rather than universal remote work or a complete return to the office.
- Q13: Firm-level studies and company reports have documented both stable or increasing output under remote or hybrid work and declines in innovation, coordination, or speed of execution, sometimes within the same company across teams.
- Q14: Aggregate productivity statistics during and after the pandemic reflect industry composition, labor hoarding, supply constraints, demand shifts, digitization, and employee turnover in addition to work location.
- Q15: Remote work is generally more favorable for focused, individually measurable tasks and less favorable for work requiring frequent coordination, rapid informal feedback, physical equipment, apprenticeship, or creative interaction.
- Q16: Employees who voluntarily choose remote work may have more suitable homes, stronger self-management, and jobs more compatible with distance than employees subjected to remote work involuntarily during the pandemic.
- Q17: Hybrid work can preserve face-to-face coordination while reducing commuting and improving retention.
- Q18: Call volume, completed patent applications, software commits, and hours worked measure short-run individual output but may omit mentoring, innovation, quality, customer relationships, and coordination costs.
- Q19: Remote work can increase total output while reducing productivity per hour, or preserve current output while increasing future coordination or innovation costs.
- Q20: Long-run effects of remote work on innovation, onboarding, promotion equity, and organizational learning are less precisely estimated than short-run effects on individual output.
- Q21: The strongest cited hybrid experiment tested one schedule and one company and therefore cannot establish that every hybrid policy, industry, or managerial system will have the same effect.
- Q22: Remote work neither universally improves nor universally reduces productivity; effects vary by occupation, worker population, schedule, period, and outcome measure.
- Q23: Full-time remote work often improves short-run individual output in jobs with clear, measurable tasks and substantial commuting or distraction costs, but can reduce productivity in coordination-heavy work or when introduced abruptly without adequate systems.
- Q24: Hybrid work has evidence of being productivity-neutral on average while improving retention.

## Deterministic Checks

- `run_metadata_loads`: PASS
- `report_exists`: PASS
- `sources_present`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `structured_report_parses`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `report_question_matches`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `source_ids_unique`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `source_ids_syntactically_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `source_urls_present`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `evidence_objects_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `confidence_values_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `citation_ids_syntactically_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `citation_ids_resolve`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `structured_claim_evidence_available`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `ledger_claim_ids_unique`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `ledger_evidence_relationships_resolve`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `ledger_confidence_values_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `ledger_evidence_ids_unique`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.

## Main Weaknesses

1. 24 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `e50bc516d4d756493b41fcaa430b164facfcb05a718934b8d5eb88b93b7e7d02`
- Candidate report hash: `f7c9afa800fa80ddce4ad2c98251f3ad0051ceb34202ba4e0b3d10aeeec790d3`
- LLM calls: 2
- Evaluated at: 2026-09-01T05:50:35.440657+00:00
