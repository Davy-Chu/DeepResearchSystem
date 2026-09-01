# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** remote-work-productivity

**System Version:** llm-only-baseline-v0

**Model:** gpt-5.6-luna

## Summary

- Overall: 57.4 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.79
- Coverage: 0.79
- Depth: 0.79
- Citation quality: 0.00
- Citation validity: 0.00
- Citation support: 0.00
- Citation completeness: 0.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report substantially differentiates work arrangements and productivity metrics, and it correctly separates productivity from retention, hours, collaboration, and career outcomes. Its treatment is somewhat distributed and does not establish a fully explicit framework for comparing all arrangements.
- Candidate evidence:
  - The summary distinguishes fully remote work from hybrid work and predominantly office-based work: “Controlled experiments generally find that remote work can improve measured output... while hybrid work often preserves productivity.”
  - Finding 8 explicitly states: “Full-time remote work and hybrid work are different interventions,” and contrasts hybrid with full-time office work.
  - Finding 9 distinguishes total output, output per hour, hours worked, quality, mentoring, innovation, customer relationships, and coordination costs.
  - The conclusion distinguishes productivity from office attendance and hours online and recommends measuring “quality, output per hour, retention, collaboration, innovation, and promotion.”
- Missing:
  - The report does not give a single explicit operational definition of productivity at the outset or clearly formalize the comparison conditions across all evidence categories.
  - Predominantly office-based work is mentioned mainly as the control condition in the hybrid experiment rather than systematically characterized as a distinct arrangement.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: The main experimental evidence is well selected and includes treatment, comparison, population, outcomes, magnitudes, and external-validity limits. Coverage falls short of full because several additional studies are described imprecisely and the report gives little information about estimate precision.
- Candidate evidence:
  - For Ctrip, the report identifies random assignment to work from home for nine months, a Chinese call-center population, approximately 13% higher performance, more minutes worked and fewer breaks, and roughly halved attrition.
  - For Trip.com, it identifies assignment to hybrid work versus full-time office work, thousands of employees, no detectable decline in performance reviews, promotion rates, or code output, and approximately one-third lower resignations.
  - For the U.S. Patent and Trademark Office, it reports that a work-from-anywhere policy increased examiner productivity by roughly 4.4%.
  - The report repeatedly limits generalization, noting that the experiments involve one company, specific occupations, measurable individual output, educated technology/travel-services employees, and particular schedules.
- Missing:
  - The report does not consistently specify the exact comparison or design for the patent-office and second call-center studies; “randomized or policy-based” is ambiguous.
  - It does not discuss statistical precision, confidence intervals, or whether the reported magnitudes are statistically distinguishable from zero beyond the Trip.com “no detectable decline” wording.
  - Some causal claims rely on studies described only generally rather than identifying their design and treatment conditions precisely.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report appropriately cautions against treating pandemic changes and collaboration proxies as causal and identifies major threats. It does not, however, fully evaluate comparison groups and identification strategies for the observational evidence.
- Candidate evidence:
  - The Indian IT study is identified as observational and pandemic-era; it reports an 8%–19% productivity reduction, longer hours, lower output per hour, and increased coordination time.
  - The report explicitly warns that health, childcare, demand, routines, and technology shocks make the Indian estimate specific to crisis conditions.
  - The Microsoft collaboration analysis is correctly described as a behavioral observational study that identifies siloing and fewer cross-group connections but “did not directly establish lower output or profits.”
  - The report states that firm-level before-and-after comparisons lack a credible counterfactual without assignment or plausibly exogenous policy change.
- Missing:
  - The observational evidence is not consistently described in terms of concrete comparison groups, timing designs, or identification strategies.
  - Selection and confounding are discussed generally, but the report does not distinguish clearly among cross-sectional associations, before-and-after estimates, quasi-experiments, and natural experiments.
  - It provides limited detail on how the Indian study constructed its counterfactual or addressed selection, and it does not give a broader set of observational estimates beyond a few examples.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: This category is clearly separated from individual causal evidence and its principal limitations are well explained. It lacks enough concrete company- or industry-level evidence and measurement detail for full coverage.
- Candidate evidence:
  - Finding 7 treats company-level and aggregate productivity evidence as a distinct category and states that firms commonly change demand, workforce composition, technology, and office policy simultaneously.
  - It notes that aggregate productivity statistics reflect industry composition, labor hoarding, supply constraints, demand shifts, digitization, and turnover in addition to work location.
  - Finding 6 identifies surveys as self-reported evidence vulnerable to self-reporting, question wording, selection, and differences between perceived and measured productivity.
  - The report states that company outcomes can coexist across teams and cannot identify effects on individual employees without a credible counterfactual.
- Missing:
  - Company and industry examples are mostly described generically rather than tied to specific measured outcomes, firms, industries, or estimates.
  - Representativeness and aggregation limits are explained, but the report could more explicitly distinguish firm productivity, industry productivity growth, employee perceptions, and team-level metrics.

### R5

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report directly answers the question and performs a clear, evidence-weighted cross-method synthesis. It compares direction, approximate magnitude, causal strength, and context rather than forcing a universal conclusion.
- Candidate evidence:
  - The summary gives a qualified direct answer: no universal increase or decrease; effects depend on job, remote intensity, selection, management, and measurement.
  - The report compares experimental gains in call centers and patent examination, experimental neutrality for hybrid work, pandemic observational losses, and noisy company-level evidence.
  - The conclusion identifies hybrid work as having the strongest evidence of short-run productivity neutrality with retention benefits, while full-time remote effects are conditional.
  - It distinguishes stronger causal evidence from weaker evidence, noting that Microsoft collaboration patterns do not prove lower output and that aggregate statistics cannot identify a causal effect.
  - It compares approximate magnitudes, including +13%, +4.4%, one-third lower resignations, and -8% to -19%, while acknowledging heterogeneity and measurement differences.
- Missing:

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: The explanation of disagreement is substantial and evidence-relevant, especially regarding occupation, selection, schedule, measurement, and pandemic conditions. It is not fully comprehensive because reporting bias and some methodological dimensions receive little or no treatment.
- Candidate evidence:
  - Finding 8 links conflicting results to task measurability, coordination, feedback, physical equipment, apprenticeship, creative interaction, worker selection, home conditions, management, and remote-work voluntariness.
  - It distinguishes full-time remote from hybrid work and connects that distinction to the Trip.com null output result versus losses in some full-remote studies.
  - Finding 9 explains conflicts arising from output-per-hour versus total output, and from short-run output measures that omit mentoring, innovation, quality, and coordination costs.
  - The conflicts section connects pandemic disruption to the Indian IT result and collaboration proxies to possible longer-run effects without treating them as proven output declines.
- Missing:
  - Publication or reporting bias is not addressed, despite being an explicit possible source of conflicting findings.
  - Implementation quality, study horizon, and management practices are mentioned but not developed as systematically as occupation, schedule, and pandemic conditions.
  - The report sometimes presents plausible mechanisms without tying them to specific comparative evidence or identifying which differences are demonstrated versus hypothesized.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report gives a strong account of heterogeneity, external-validity limitations, and unresolved long-run outcomes. Full coverage would require more evidence-based assessment of underrepresented populations and study-horizon effects rather than primarily identifying them as research gaps.
- Candidate evidence:
  - The report identifies heterogeneity across jobs, workers, firms, schedules, management quality, and remote-work voluntariness.
  - It notes limits for less experienced employees, new hires, managers, workers with unequal home-office conditions, and jobs requiring coordination or physical equipment.
  - It separates short-run measured output from unresolved outcomes including innovation, onboarding, promotion equity, organizational learning, mentoring, and career progression.
  - The remaining-gaps section calls for multi-company, cross-industry, cross-country, and longer-term studies.
- Missing:
  - Underrepresented settings are identified mainly as a list of gaps rather than assessed using evidence about how effects differ in those settings.
  - The report does not deeply evaluate duration effects or distinguish evidence for immediate, medium-term, and long-term outcomes.
  - Career progression and innovation are appropriately treated as unresolved, but the report offers limited evidence about their actual heterogeneity across worker groups or firms.

### Novel Value

- The report offers a useful cross-method synthesis distinguishing causal experimental evidence from pandemic-era observational estimates, collaboration proxies, surveys, and aggregate productivity data.
- It highlights an important measurement distinction: remote work may increase total output or retention while reducing output per hour or creating longer-run coordination and innovation costs.
- It presents hybrid work as a distinct intervention rather than treating it as equivalent to full-time remote work, and uses this distinction to reconcile apparently conflicting findings.

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

- Q1: The report concludes that remote work does not universally raise or lower productivity; effects vary by job, remote-work arrangement, employee selection, management practices, and productivity measurement.
- Q2: In a randomized experiment at Ctrip, employees assigned to work from home for nine months achieved approximately 13% higher performance, largely through more minutes worked and fewer breaks.
- Q3: In the Ctrip experiment, attrition among employees assigned to work from home was approximately halved.
- Q4: The Ctrip experiment involved call-center work with highly observable output and relatively limited dependence on face-to-face collaboration.
- Q5: A large randomized trial at Trip.com assigned thousands of employees to hybrid work or full-time office work.
- Q6: In the Trip.com trial, hybrid work produced no detectable decline in performance reviews, promotion rates, or code output, while resignations fell by approximately one-third.
- Q7: A study of the U.S. Patent and Trademark Office found that a work-from-anywhere policy increased examiner productivity by approximately 4.4%, while also improving retention and geographic flexibility.
- Q8: A randomized or policy-based study of call-center employees found that working from home increased measured productivity, while remote workers received fewer promotions.
- Q9: An Indian information-technology company study during the pandemic found that working from home reduced productivity by approximately 8% to 19%, depending on the specification.
- Q10: In the Indian IT study, employees worked longer hours while output per hour fell.
- Q11: The Indian IT study found that coordination and communication consumed more time under remote work.
- Q12: Analysis of Microsoft collaboration data found that remote work made workers' communication networks more static and siloed, with fewer cross-group connections and less synchronous interaction.
- Q13: The Microsoft collaboration analysis did not directly establish lower output or profits.
- Q14: The Survey of Working Arrangements and Attitudes and related U.S. research find that employees and managers generally perceive working from home as modestly less productive than office work, with a small and occupation-dependent gap.
- Q15: Post-pandemic employers have largely settled on hybrid arrangements rather than universal remote work or a complete return to the office.
- Q16: Firm-level studies and company reports have documented both stable or increasing output under remote or hybrid work and declines in innovation, coordination, or execution speed.
- Q17: Aggregate productivity statistics during and after the pandemic reflect industry composition, labor hoarding, supply constraints, demand shifts, digitization, and employee turnover in addition to work location.
- Q18: Remote work is more favorable for focused, individually measurable tasks and less favorable for tasks requiring frequent coordination, rapid informal feedback, physical equipment, apprenticeship, or creative interaction.
- Q19: Voluntary remote work differs from involuntary pandemic remote work because voluntary workers may have more suitable homes, stronger self-management, and jobs more compatible with distance, whereas forced remote work may involve childcare disruption, inadequate equipment, and organizational dislocation.
- Q20: Hybrid work can preserve face-to-face coordination while reducing commuting and improving retention.
- Q21: Call volume, completed patent applications, software commits, and hours worked measure short-run individual output but may miss mentoring, innovation, quality, customer relationships, and coordination costs.
- Q22: Remote work can raise total output while reducing productivity per hour, or preserve current output while increasing future coordination or innovation costs.
- Q23: The strongest hybrid experiment tested one schedule and one company and therefore cannot establish that every hybrid policy, industry, or managerial system will have the same effect.
- Q24: Long-run effects of remote work on innovation, onboarding, promotion equity, and organizational learning are less precisely estimated than short-run individual output effects.
- Q25: Full-time remote work often improves short-run individual output in jobs with clear, measurable tasks and substantial commuting or distraction costs, but can reduce productivity in coordination-heavy work or when introduced abruptly without adequate systems.
- Q26: Hybrid work has the strongest evidence of being productivity-neutral on average while improving retention.
- Q27: Conflicting findings arise because studies examine different occupations, worker populations, schedules, periods, and outcome measures.

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

1. 27 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `e50bc516d4d756493b41fcaa430b164facfcb05a718934b8d5eb88b93b7e7d02`
- Candidate report hash: `f7c9afa800fa80ddce4ad2c98251f3ad0051ceb34202ba4e0b3d10aeeec790d3`
- LLM calls: 2
- Evaluated at: 2026-09-01T06:00:45.254239+00:00
