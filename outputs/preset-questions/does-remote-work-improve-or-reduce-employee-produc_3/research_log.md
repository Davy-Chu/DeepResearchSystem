# Research Run Log

## Run Summary

**System Version:** evidence-ledger-decomposer-v1

**Research Question**

Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 10

**OpenAI Calls:** 7

**Tavily Calls:** 3

**Started:** 2026-08-31T18:32:45-04:00

**Ended:** 2026-08-31T18:34:13-04:00

**Total Runtime:** 88.49s

---

# Research Plan

## Subquestions

### SQ1 [CORE]

**Question:**

What do controlled experiments and quasi-experimental studies find about the effect of remote work on employee productivity?

**Success criteria:**

Identify relevant experimental or quasi-experimental evidence, define the remote-work intervention and productivity outcome, report the direction and size of estimated effects where available, and describe uncertainty, sample characteristics, and study limitations.

**Initial status:** UNRESEARCHED

### SQ2 [CORE]

**Question:**

What do observational studies find about the relationship between remote work and employee productivity?

**Success criteria:**

Summarize observational evidence, distinguish correlation from causal estimates, explain how remote workers and non-remote workers were compared, and report key productivity measures, effect directions, uncertainty, and confounding risks.

**Initial status:** UNRESEARCHED

### SQ3 [CORE]

**Question:**

What does company-level data show about remote work and productivity?

**Success criteria:**

Assess evidence using firm, team, or aggregate company data, clarify whether outcomes are employee-level or organizational, report productivity measures and estimated effects, and note selection, composition, measurement, and generalizability limitations.

**Initial status:** UNRESEARCHED

### SQ4 [CORE]

**Question:**

Why do studies of remote work reach conflicting conclusions about productivity?

**Success criteria:**

Synthesize differences in research design, identification, worker and job selection, remote-work intensity and context, management practices, technology, time period, productivity definitions and measurement, and workplace or industry characteristics, distinguishing plausible explanations from established evidence.

**Initial status:** UNRESEARCHED

### SQ5 [CORE]

**Question:**

How should the overall evidence be reconciled regarding whether remote work improves or reduces employee productivity?

**Success criteria:**

Compare findings across the three evidence types, identify where conclusions converge or remain uncertain, preserve distinctions between individual and company-level productivity, and state a qualified overall conclusion rather than treating all studies as equally causal or comparable.

**Initial status:** UNRESEARCHED

## Synthesis Requirements

- Compare controlled experiments, observational studies, and company-level data explicitly rather than presenting them as a single undifferentiated evidence base.
- Distinguish causal effects from associations and account for differences in productivity definitions, measurement, populations, work arrangements, and study periods.
- Explain conflicting findings through methodological and contextual differences, while preserving uncertainty and limitations.
- Clarify whether conclusions concern employee productivity, team or firm productivity, or broader organizational outcomes.

## Output Requirements

- Answer the directional question of whether remote work improves or reduces productivity with an appropriately qualified conclusion.
- Present comparisons across the three specified evidence categories.
- Explain why different studies reach conflicting conclusions.

---

# Iteration 1

## 1. Search

**Query**

> Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions.

**Purpose:** GENERAL

**Why this query**

This is the user's original research question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S1 — Remote Work Productivity Study 2026: 50+ Studies | eMonitor**
  URL: https://www.employee-monitoring.net/blog/remote-work-productivity-research-meta-analysis
- **S2 — In-office vs remote day productivity: Which is better?**
  URL: https://www.worklytics.co/blog/in-office-vs-remote-day-productivity-which-is-better
- **S3 — The rise in remote work since the pandemic and its impact on ...**
  URL: https://www.bls.gov/opub/btn/volume-13/remote-work-productivity.htm
- **S4 — Remote Work Productivity Study: Surprising Findings From a 4-Year ...**
  URL: https://www.greatplacetowork.com/resources/blog/remote-work-productivity-study-finds-surprising-reality-2-year-study
- **S5 — Remote Working and Work Effectiveness: A Leader Perspective**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC9690707

**Search Duration:** 2.63s

---

## 2. Evidence Processing

- New claim proposals: 7
- Existing claim updates: 0
- New gaps: 5
- Resolved gaps: 0

**Processing Duration:** 21.92s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

The supplied evidence does not support a single direction for remote work's effect on productivity; effects vary by task, work arrangement, worker, management practices, technology, and productivity measure.

- S3 supports (direct): The BLS review states that effects likely depend on task type, technology, home environment, worker motivation, and management practices, and reports both positive experimental findings and short-run declines in some case studies.
- S2 supports (direct): A workplace-analytics industry source reports higher focus productivity remotely but better collaboration and spontaneous problem-solving in offices, with outcomes depending on work design and management.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C2

**Claim**

In the 2015 Ctrip randomized experiment described in the supplied sources, call-center employees assigned to work from home four days per week completed approximately 13.5% more calls than office-based peers; the reported mechanisms were more minutes worked and more calls per minute.

- S1 supports (direct): The source describes a randomized experiment of 249 Ctrip call-center employees and reports 13.5% more calls for the work-from-home group, attributing the increase to more minutes worked and higher within-minute processing.
- S3 supports (indirect): The BLS article independently summarizes randomized experiments as finding small positive effects on individual productivity, though it does not identify this estimate specifically.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C3

**Claim**

In the Trip.com randomized hybrid-work experiment described in the supplied sources, assigning employees to two remote days per week produced no statistically significant difference in reported performance, promotions, coding output, or marketing revenue relative to five-day office work over six months, while reducing resignations by roughly one-third.

- S1 supports (direct): The source reports a randomized study of 1,612 Trip.com employees assigned to Wednesday-and-Friday remote work or five office days; it reports no significant output difference and a 33% reduction in resignations.
- S3 supports (indirect): The BLS review characterizes randomized experiments as finding small positive effects for hybrid and fully remote work and lower turnover, consistent with no productivity penalty in this hybrid study.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C4

**Claim**

The supplied company- and industry-level evidence is mixed: a BLS analysis finds positive associations between increases in remote work and total-factor-productivity growth across 61 private-sector industries in 2019–21 and 2019–22, while the cited aggregate study across 43 industries found little relationship between remote-work feasibility and labor-productivity growth.

- S3 supports (direct): The BLS article reports positive associations between the rise in primarily remote workers and TFP growth across 61 industries after accounting for pre-pandemic productivity trends, and separately summarizes Fernald et al. as finding little relationship across 43 industries.
- S3 contradicts (direct): Within the same source, the summarized 43-industry analysis reports little relationship, contrasting with the positive 61-industry associations.

**Confidence:** HIGH

**Status:** CONFLICTING

### New Claim C5

**Claim**

Observational and survey-based evidence in the supplied sources generally reports stable or higher perceived productivity among remote workers, but it is vulnerable to selection, self-report, and organizational-composition confounding rather than providing a clean causal estimate.

- S4 supports (direct): Great Place To Work reports stable or improved productivity after remote transitions in a two-year study of more than 800,000 employees and higher discretionary effort in highly rated companies; its measures include employee survey responses and company comparisons.
- S5 supports (direct): A 2022 study of 141 managers finds that perceived benefits predict some dimensions of remote-work effectiveness, while technical and communication limitations predict team and external-cooperation effectiveness.
- S2 supports (direct): The source reports that many remote workers report higher productivity and describes remote-work advantages for focus, but presents these largely as survey and analytics-based evidence.

**Confidence:** MEDIUM

**Status:** WEAK

### New Claim C6

**Claim**

Different findings can plausibly arise because studies examine different outcomes: individual focused-task output may improve remotely, whereas collaboration, knowledge sharing, mentoring, and innovation may be weaker under fully remote arrangements.

- S1 supports (direct): The source reports a claimed median positive effect for focused tasks and negative effect for collaborative tasks, and describes lower output for some highly collaborative or newly hired roles.
- S2 supports (direct): The source distinguishes remote advantages for deep focus from office advantages for spontaneous collaboration, mentoring, and creative problem-solving.
- S5 supports (direct): Managers identified technical and communication limitations as predictors of lower team and external-cooperation effectiveness.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C7

**Claim**

Remote and hybrid arrangements may produce organizational benefits through lower turnover even when measured individual output is unchanged.

- S1 supports (direct): The Ctrip experiment is reported to show lower attrition for fully remote workers, and the Trip.com hybrid experiment is reported to show a roughly one-third reduction in resignations without a measurable output penalty.
- S3 supports (direct): The BLS review states that randomized studies found lower job turnover as job satisfaction rose, potentially reducing firms' hiring costs.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Gap G1

The supplied material lacks primary reports and complete methodological details for the cited randomized and quasi-experimental studies, including confidence intervals, treatment compliance, attrition, worker characteristics, and whether effects persist beyond the reported periods.

### New Gap G2

There is insufficient detailed observational evidence to compare remote and non-remote workers while separating causal effects from worker self-selection, job selection, pre-existing productivity, and pandemic-period confounding.

### New Gap G3

Company-level evidence is incomplete: the sources do not provide comparable firm or team productivity measures, specifications, effect sizes, or reconciliation of the 61-industry positive association with the 43-industry near-zero result.

### New Gap G4

The evidence does not establish how effects differ by remote-work intensity, onboarding status, job type, industry, management practice, technology quality, or time period; these are proposed explanations for heterogeneity but are not fully tested in the supplied material.

### New Gap G5

The supplied sources provide no direct, rigorous synthesis comparing employee-level productivity with team, firm, innovation, or broader organizational productivity using common definitions and outcomes.

---

## 4. Current Research State

- Claims: 7
- Supported: 5
- Weak: 1
- Conflicting: 1
- Insufficient Evidence: 0
- Open Gaps: 5
- Remaining Searches: 2

### Subquestion Progress

**SQ1:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** UNRESEARCHED → PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ3:** UNRESEARCHED → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ4:** UNRESEARCHED → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ5:** UNRESEARCHED → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → PARTIAL (targeted searches: 0)
- SQ3 → CONFLICTING (targeted searches: 0)
- SQ4 → CONFLICTING (targeted searches: 0)
- SQ5 → CONFLICTING (targeted searches: 0)

**SECONDARY:**

- None

**Remaining targeted searches:** 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ2

**Why**

Observational evidence remains a high-importance unresolved core component: the ledger mainly contains self-reported or industry-survey findings and lacks credible comparisons that address worker/job selection and pandemic confounding. One focused search could materially improve the causal-versus-correlational comparison.

**Next Search**

> Find rigorous observational or quasi-experimental studies of remote work and employee productivity that compare remote and non-remote workers, reporting productivity measures, effect sizes or uncertainty, controls for selection/confounding, sample and period, and key limitations.


---

# Iteration 2

## 1. Search

**Query**

> Find rigorous observational or quasi-experimental studies of remote work and employee productivity that compare remote and non-remote workers, reporting productivity measures, effect sizes or uncertainty, controls for selection/confounding, sample and period, and key limitations.

**Target:** SQ2

**Purpose:** SUBQUESTION

**Why this query**

Observational evidence remains a high-importance unresolved core component: the ledger mainly contains self-reported or industry-survey findings and lacks credible comparisons that address worker/job selection and pandemic confounding. One focused search could materially improve the causal-versus-correlational comparison.

5 result(s) retrieved; 2 new unique source(s) added.

- **S6 — 40+ remote work productivity statistics, trends & data for 2026**
  URL: https://www.worktime.com/blog/statistics/remote-work-productivity-statistics-trends-data
- **S7 — [PDF] The Rise of Remote Work: Evidence on Productivity and Preferences ...**
  URL: https://www.hbs.edu/ris/download.aspx?name=20-138.pdf

**Search Duration:** 3.66s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 3
- New gaps: 1
- Resolved gaps: 0

**Processing Duration:** 10.08s

---

## 3. Ledger Updates

### New Claim C8

**Claim**

In repeated surveys of small-business owners and workers during the COVID-19 period, perceived productivity effects of remote work shifted from predominantly negative early in 2020 to positive by early 2021; reported contributors included technology investments, training, changed task assignments, and improved remote-management ability, while monitoring and worker-learning difficulties remained.

- S7 supports (direct): The working paper reports that 70% of small-business owners perceived a productivity dip at the start of the pandemic, whereas the median owner reported a positive productivity impact by early 2021. It attributes the shift partly to technological investments, training, altered job characteristics and tasks, and improved managerial ability, while also reporting continuing monitoring and learning challenges.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

The supplied evidence does not support a single direction for remote work's effect on productivity; effects vary by task, work arrangement, worker, management practices, technology, and productivity measure.

- S7 supports (direct): Repeated surveys show that perceived effects changed from an early productivity dip to a positive median effect over time, with variation linked to management, technology, training, task changes, firm size, and persistent monitoring or learning difficulties.
- S6 supports (indirect): The industry article summarizes positive associations, stable or higher reported output, and differences between focused work and collaboration, while noting that its evidence is largely survey- or secondary-source-based.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

Observational and survey-based evidence in the supplied sources generally reports stable or higher perceived productivity among remote workers, but it is vulnerable to selection, self-report, and organizational-composition confounding rather than providing a clean causal estimate.

- S7 supports (direct): Repeated surveys of small-business owners and workers found that perceived productivity shifted from negative early in 2020 to positive by early 2021; the paper also reports worker preferences for remote work and continuing concerns about monitoring and learning.
- S6 supports (direct): The article reports that 77% of remote employees say they are more productive remotely, but presents this as survey-based evidence and is produced by a remote-monitoring vendor.

**Confidence:** MEDIUM → MEDIUM

**Status:** WEAK → SUPPORTED

### Updated Claim C6

**Claim**

Different findings can plausibly arise because studies examine different outcomes: individual focused-task output may improve remotely, whereas collaboration, knowledge sharing, mentoring, and innovation may be weaker under fully remote arrangements.

- S7 supports (direct): The paper identifies monitoring and learning difficulties as challenges of remote work and reports that technology, training, task reassignment, and better remote management contributed to perceived productivity improvements over time.
- S6 supports (indirect): The article distinguishes easier focused work remotely from collaboration advantages associated with office work and reports that outcomes depend on work design and management.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### New Gap G6

The new survey evidence measures perceived productivity and reports changing perceptions over the pandemic, but does not establish whether objective employee, team, or firm productivity changed after accounting for simultaneous technological, managerial, task, and worker-composition changes.

---

## 4. Current Research State

- Claims: 8
- Supported: 7
- Weak: 0
- Conflicting: 1
- Insufficient Evidence: 0
- Open Gaps: 6
- Remaining Searches: 1

### Subquestion Progress

**SQ1:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ3:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ4:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ5:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → PARTIAL (targeted searches: 1)
- SQ3 → CONFLICTING (targeted searches: 0)
- SQ4 → CONFLICTING (targeted searches: 0)
- SQ5 → CONFLICTING (targeted searches: 0)

**SECONDARY:**

- None

**Remaining targeted searches:** 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ1

**Why**

SQ1 remains only partially resolved, with a high-importance gap concerning primary methodological details, uncertainty, compliance, attrition, and persistence in the controlled and quasi-experimental evidence. One focused search could materially strengthen the causal comparison before synthesis.

**Next Search**

> Find primary randomized or quasi-experimental studies of remote or hybrid work and employee productivity (including Ctrip and Trip.com), reporting intervention, sample, objective productivity outcomes, effect sizes with confidence intervals, compliance/attrition, follow-up duration, and limitations.


---

# Iteration 3

## 1. Search

**Query**

> Find primary randomized or quasi-experimental studies of remote or hybrid work and employee productivity (including Ctrip and Trip.com), reporting intervention, sample, objective productivity outcomes, effect sizes with confidence intervals, compliance/attrition, follow-up duration, and limitations.

**Target:** SQ1

**Purpose:** SUBQUESTION

**Why this query**

SQ1 remains only partially resolved, with a high-importance gap concerning primary methodological details, uncertainty, compliance, attrition, and persistence in the controlled and quasi-experimental evidence. One focused search could materially strengthen the causal comparison before synthesis.

5 result(s) retrieved; 3 new unique source(s) added.

- **S8 — Hybrid working from home improves retention without ... - PMC**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11208135
- **S9 — Does Working from Home Increase Productivity? (2026)**
  URL: https://emailanalytics.com/does-working-from-home-increase-productivity
- **S10 — Remote & hybrid work, Part 3**
  URL: https://media.crai.com/wp-content/uploads/2025/01/04165228/Labor-Employment-Literature-Watch-2025-03-PART-3-1.pdf

**Search Duration:** 2.83s

---

## 2. Evidence Processing

- New claim proposals: 2
- Existing claim updates: 4
- New gaps: 2
- Resolved gaps: 0

**Processing Duration:** 13.44s

---

## 3. Ledger Updates

### New Claim C9

**Claim**

In a randomized experiment at a data-entry firm in India, employees assigned to work from home for a short-term job were almost 20% less productive than employees assigned to work in the office. Approximately one-third of the gap was attributed to faster learning in the office, while roughly two-thirds was present from the first day. The study also found that workers who preferred working from home were intrinsically more capable, but performed relatively worse when working from home than workers who preferred the office.

- S10 supports (direct): The literature review summarizes Atkin, Schoar, and Shinde's randomized experiment, reporting nearly 20% lower productivity at home, the learning and day-one components of the gap, and heterogeneous effects by worker preference and characteristics.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C10

**Claim**

A field experiment at a large nongovernmental organization in Bangladesh suggests that an intermediate hybrid schedule can improve some outcomes without a clear productivity penalty: employees averaging two in-office days per week reported higher job satisfaction and work-life balance, managers received higher ratings for work quality and creativity, and non-managers showed no performance disadvantage relative to employees spending more or less time in the office.

- S10 supports (direct): S10 summarizes Choudhury, Khanna, Makridis, and Schirmann's experiment, in which administrative employees were randomly assigned daily to home or office work and grouped by average in-office days.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C2

**Claim**

In the 2015 Ctrip randomized experiment described in the supplied sources, call-center employees assigned to work from home four days per week completed approximately 13.5% more calls than office-based peers; the reported mechanisms were more minutes worked and more calls per minute.

- S9 contradicts (indirect): S9 gives a substantially different description of the Ctrip result, referring to approximately 16,000 call-center employees and a 13% increase, rather than the 249-employee description and approximately 13.5% estimate in S1. Because S9 is a secondary commercial article, this creates a source-description conflict but does not by itself establish that the underlying experimental result is false.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → CONFLICTING

### Updated Claim C3

**Claim**

In the Trip.com randomized hybrid-work experiment described in the supplied sources, assigning employees to two remote days per week produced no statistically significant difference in reported performance, promotions, coding output, or marketing revenue relative to five-day office work over six months, while reducing resignations by roughly one-third.

- S8 supports (direct): The Nature article reports a six-month randomized trial of 1,612 employees at a Chinese technology company in 2021–22. Hybrid work improved job satisfaction and reduced quit rates by one-third, while equivalence tests found no effect on performance grades over the following two years and no evidence of a promotion difference.
- S10 supports (direct): The literature review independently summarizes the Trip.com experiment as finding 33% lower attrition and no statistically significant effect on performance reviews, promotion rates, or lines of code written; it also reports fewer hours on home days offset by longer hours on office days and weekends.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C1

**Claim**

The supplied evidence does not support a single direction for remote work's effect on productivity; effects vary by task, work arrangement, worker, management practices, technology, and productivity measure.

- S10 supports (direct): The review contrasts a nearly 20% productivity reduction in a fully remote data-entry experiment with no significant performance penalty in the Trip.com hybrid experiment and an intermediate-schedule result in Bangladesh, reinforcing dependence on work arrangement, task, worker type, and outcome.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C6

**Claim**

Different findings can plausibly arise because studies examine different outcomes: individual focused-task output may improve remotely, whereas collaboration, knowledge sharing, mentoring, and innovation may be weaker under fully remote arrangements.

- S10 supports (direct): The Indian data-entry experiment indicates that learning speed, worker preferences, caregiving or other time demands, income, and age can contribute to differing effects; the Bangladesh experiment suggests that hybrid intensity and managerial status affect performance outcomes.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### New Gap G7

The newly summarized Indian and Bangladesh experiments add evidence on fully remote and hybrid arrangements, but the supplied material still lacks their complete primary-study methods, sample details, confidence intervals, compliance information, and evidence on persistence beyond the short-term settings.

### New Gap G8

The conflicting supplied descriptions of the Ctrip experiment's sample size and estimate are not reconciled, leaving uncertainty about the precise study population and numerical effect despite agreement on a positive direction.

---

## 4. Current Research State

- Claims: 10
- Supported: 8
- Weak: 0
- Conflicting: 2
- Insufficient Evidence: 0
- Open Gaps: 8
- Remaining Searches: 0

### Subquestion Progress

**SQ1:** PARTIAL → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ2:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ3:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ4:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ5:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

### Research Plan Status

**CORE:**

- SQ1 → CONFLICTING (targeted searches: 1)
- SQ2 → PARTIAL (targeted searches: 1)
- SQ3 → CONFLICTING (targeted searches: 0)
- SQ4 → CONFLICTING (targeted searches: 0)
- SQ5 → CONFLICTING (targeted searches: 0)

**SECONDARY:**

- None

**Remaining targeted searches:** 0

---

## 5. Research Decision

**Decision:** Stop researching.

**Origin:** BUDGET_STOP

**Why**

The maximum research iteration budget was reached.

**Stop Reason:** max_iterations


---

# Final Research Decision

**Stop Reason:** max_iterations

**Remaining Uncertainty**

- G1: Complete primary-study methods and uncertainty estimates for the cited randomized and quasi-experimental evidence are unavailable.
- G2: The supplied observational evidence does not adequately separate causal effects from worker selection, job selection, pre-existing productivity, and pandemic confounding.
- G3: Company-level measures, specifications, effect sizes, and reconciliation of the 61-industry and 43-industry findings are incomplete.
- G4: The evidence does not establish how effects vary by intensity, onboarding, job type, industry, management, technology, or time period.
- G5: There is no rigorous common-outcome synthesis linking employee productivity to team, firm, innovation, or broader organizational productivity.
- G6: Survey-reported changes in perceived productivity are not shown to equal objective employee, team, or firm productivity changes.
- G7: The Indian and Bangladesh experiments lack complete primary methods, sample details, uncertainty, compliance information, and long-term evidence.
- G8: The conflicting Ctrip descriptions are not reconciled.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Question Decomposition | 1 | 8.65s |
| Tavily Search | 3 | 9.11s |
| Evidence Processing | 3 | 45.44s |
| Research Decision | 2 | 6.59s |
| Report Generation | 1 | 18.69s |
| Total Run | — | 88.49s |
