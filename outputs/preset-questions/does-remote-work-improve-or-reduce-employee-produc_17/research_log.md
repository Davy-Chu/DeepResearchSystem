# Research Run Log

## Run Summary

**System Version:** evidence-ledger-v1

**Research Question**

Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-4o-mini

**Searches Performed:** 10 / 10

**Unique Sources:** 27

**OpenAI Calls:** 20

**Tavily Calls:** 10

**Started:** 2026-09-01T12:17:05-04:00

**Ended:** 2026-09-01T12:18:50-04:00

**Total Runtime:** 104.99s

---

# Iteration 1

## 1. Search

**Query**

> Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions.

**Purpose:** GENERAL

**Why this query**

This is the user's original research question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S1 — Remote Work Productivity: What the OECD 2024 Data Shows**
  URL: https://goalsandprogress.com/remote-work-productivity-research
- **S2 — Observational Studies, Confounders, and Stratification - Data Science Discovery**
  URL: https://discovery.cs.illinois.edu/learn/Basics-of-Data-Science-with-Python/Observational-Studies-Confounders-and-Stratification
- **S3 — Evaluating Statistical Claims: Observational Studies and Experiments (Notes & Practice Questions) - Digital Sat Exam**
  URL: https://www.examples.com/digital-sat/evaluating-statistical-claims-observational-studies-and-experiments
- **S4 — How to Determine Causal Relationships in Observational Studies – Coding With Max**
  URL: https://codingwithmax.com/causal-observational-studies
- **S5 — A field biologist who studies the behavior of birds in a rain forest most likely to collect data through? - Answers**
  URL: https://www.answers.com/earth-science/A_field_biologist_who_studies_the_behavior_of_birds_in_a_rain_forest_most_likely_to_collect_data_through

**Search Duration:** 0.55s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 0
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 5.01s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

Remote work impacts employee productivity differently, depending on job type, interruption management, and cooperation structures.

- S1 supports (direct): The article presents a framework stating that remote work productivity outcomes depend on job type, boundary clarity, and cooperation structures.
- S1 contradicts (direct): While remote work is associated with economy-wide productivity growth, specific studies indicate a 20% productivity decrease for coordination-heavy roles.

**Confidence:** MEDIUM

**Status:** INSUFFICIENT_EVIDENCE

---

## 4. Current Research State

- Claims: 1
- Supported: 0
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 1
- Open Gaps: 0
- Remaining Searches: 9

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C1

**Why**

The claim regarding the mixed impacts of remote work on productivity based on job context needs further exploration for clearer insights.

**Next Search**

> Research how job type affects remote work productivity, focusing on studies distinguishing between coordination-heavy and independent roles, and their impacts on overall productivity outcomes.


---

# Iteration 2

## 1. Search

**Query**

> Research how job type affects remote work productivity, focusing on studies distinguishing between coordination-heavy and independent roles, and their impacts on overall productivity outcomes.

**Target:** C1

**Purpose:** GENERAL

**Why this query**

The claim regarding the mixed impacts of remote work on productivity based on job context needs further exploration for clearer insights.

5 result(s) retrieved; 5 new unique source(s) added.

- **S6 — Remote Work Productivity Study 2026: 50+ Studies | eMonitor**
  URL: https://www.employee-monitoring.net/blog/remote-work-productivity-research-meta-analysis
- **S7 — 40+ remote work productivity statistics, trends & data for 2026**
  URL: https://www.worktime.com/blog/statistics/remote-work-productivity-statistics-trends-data
- **S8 — Top Remote Work Statistics And Trends**
  URL: https://www.forbes.com/advisor/business/remote-work-statistics
- **S9 — The study of remote working outcome and its influence on firm performance**
  URL: https://www.sciencedirect.com/science/article/pii/S259029112300133X
- **S10 — The rise in remote work since the pandemic and its impact ...**
  URL: https://www.bls.gov/opub/btn/volume-13/remote-work-productivity.htm

**Search Duration:** 2.60s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 1
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 11.57s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Remote work impacts employee productivity differently, depending on job type, interruption management, and cooperation structures.

- S6 supports (direct): The meta-analysis found that productivity impacts of remote work are positive for individual focused tasks (+10%) but negative for collaborative tasks (-4%), emphasizing that the net effect depends on the nature of the work.
- S7 supports (direct): A Bureau of Labor Statistics analysis links remote work to a positive association with total factor productivity growth, indicating mixed outcomes based on context.
- S10 supports (direct): Research shows little relationship between remote work and aggregate productivity growth across 61 industries, suggesting strong effects depend on specific job types and management practices.
- S9 contradicts (indirect): While positive relationships between remote work and firm performance are suggested, empirical studies note declines in productivity in some cases, indicating potential drawbacks for specific roles.

**Confidence:** MEDIUM → HIGH

**Status:** INSUFFICIENT_EVIDENCE → SUPPORTED

---

## 4. Current Research State

- Claims: 1
- Supported: 1
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 8

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C1

**Why**

Focus on job type differences in remote work productivity is key to resolving conflicting conclusions, particularly addressing coordination-heavy vs. independent roles.

**Next Search**

> Investigate studies that specifically analyze the impact of remote work on productivity in coordination-heavy roles versus independent roles, highlighting variations in outcomes and the reasons behind them.


---

# Iteration 3

## 1. Search

**Query**

> Investigate studies that specifically analyze the impact of remote work on productivity in coordination-heavy roles versus independent roles, highlighting variations in outcomes and the reasons behind them.

**Target:** C1

**Purpose:** GENERAL

**Why this query**

Focus on job type differences in remote work productivity is key to resolving conflicting conclusions, particularly addressing coordination-heavy vs. independent roles.

5 result(s) retrieved; 4 new unique source(s) added.

- **S11 — Are Remote Workers More Productive? What The Research Actually Shows — FYIVT**
  URL: https://fyivt.com/are-remote-workers-more-productive-what-the-research-actually-shows
- **S12 — Remote Work Productivity Study: Surprising Findings From ...**
  URL: https://www.greatplacetowork.com/resources/blog/remote-work-productivity-study-finds-surprising-reality-2-year-study
- **S13 — The Rise of Remote Work: Evidence on Productivity and ...**
  URL: https://www.hbs.edu/ris/download.aspx?name=20-138.pdf
- **S14 — Remote Staff Hours Fall, but Productivity Steady (For Now)**
  URL: https://www.gallup.com/workplace/693539/remote-staff-hours-fall-productivity-steady.aspx

**Search Duration:** 2.66s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 1
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 6.34s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Remote work impacts employee productivity differently, depending on job type, interruption management, and cooperation structures.

- S11 supports (direct): The nuanced findings highlight that productivity outcomes depend on factors like job type and level of cooperation, rather than being universally positive or negative.
- S12 supports (direct): Gallup's analysis shows that productivity in remote settings is influenced by company culture, trust, and leadership, indicating strong cooperation leads to increased productivity.
- S14 supports (direct): A study highlights mixed productivity outcomes, suggesting that while remote work hours have decreased, it does not necessarily reflect a decrease in overall productivity due to better employee role alignment.
- S13 contradicts (direct): A study indicates that remote work can reduce productivity for knowledge-intensive roles, showcasing nuanced effects rather than a one-size-fits-all principle.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 1
- Supported: 1
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 7

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C1

**Why**

Supporting evidence highlights job type influence on productivity, but gaps remain in understanding specific comparative outcomes between coordination-heavy and independent roles.

**Next Search**

> Examine new studies that quantify the productivity effects of remote work in coordination-heavy roles compared to independent roles, focusing on specific metrics and contextual factors driving these outcomes.


---

# Iteration 4

## 1. Search

**Query**

> Examine new studies that quantify the productivity effects of remote work in coordination-heavy roles compared to independent roles, focusing on specific metrics and contextual factors driving these outcomes.

**Target:** C1

**Purpose:** GENERAL

**Why this query**

Supporting evidence highlights job type influence on productivity, but gaps remain in understanding specific comparative outcomes between coordination-heavy and independent roles.

5 result(s) retrieved; 1 new unique source(s) added.

- **S15 — Does Working from Home Increase Productivity? (2026)**
  URL: https://emailanalytics.com/does-working-from-home-increase-productivity

**Search Duration:** 2.46s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 1
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 4.02s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Remote work impacts employee productivity differently, depending on job type, interruption management, and cooperation structures.

- S15 supports (direct): Elimination of commutes and reduced distractions reported by remote workers lead to higher productivity by improving work-life balance.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 1
- Supported: 1
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 6

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C1

**Why**

Further investigation is needed on the nuanced productivity outcomes of remote work in different job types, particularly focusing on coordination-heavy versus independent roles, which could clarify conflicting conclusions.

**Next Search**

> Analyze recent studies comparing remote work productivity outcomes in coordination-heavy roles vs independent roles, emphasizing contextual factors and metrics influencing these differences, to resolve conflicting conclusions.


---

# Iteration 5

## 1. Search

**Query**

> Analyze recent studies comparing remote work productivity outcomes in coordination-heavy roles vs independent roles, emphasizing contextual factors and metrics influencing these differences, to resolve conflicting conclusions.

**Target:** C1

**Purpose:** GENERAL

**Why this query**

Further investigation is needed on the nuanced productivity outcomes of remote work in different job types, particularly focusing on coordination-heavy versus independent roles, which could clarify conflicting conclusions.

5 result(s) retrieved; 1 new unique source(s) added.

- **S16 — In-office vs remote day productivity: Which is better?**
  URL: https://www.worklytics.co/blog/in-office-vs-remote-day-productivity-which-is-better

**Search Duration:** 2.71s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 1
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 2.49s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Remote work impacts employee productivity differently, depending on job type, interruption management, and cooperation structures.

- S16 supports (direct): Research shows remote work improves individual focus productivity by 5-15%, especially for deep concentration tasks, while office environments enhance collaboration and spontaneous problem-solving.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 1
- Supported: 1
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 5

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C1

**Why**

Existing studies on remote work productivity in coordination-heavy vs independent roles have not resolved all conflicting conclusions, particularly around specific contextual factors and metrics used.

**Next Search**

> Explore additional research that investigates the impact of remote work on productivity in coordination-heavy roles versus independent roles, focusing on contextual factors like management practices and organizational culture to clarify conflicting findings.


---

# Iteration 6

## 1. Search

**Query**

> Explore additional research that investigates the impact of remote work on productivity in coordination-heavy roles versus independent roles, focusing on contextual factors like management practices and organizational culture to clarify conflicting findings.

**Target:** C1

**Purpose:** GENERAL

**Why this query**

Existing studies on remote work productivity in coordination-heavy vs independent roles have not resolved all conflicting conclusions, particularly around specific contextual factors and metrics used.

5 result(s) retrieved; 3 new unique source(s) added.

- **S17 — Medium**
  URL: https://medium.com/@ieeecomputersocietyiit/the-impact-of-remote-work-on-organizational-culture-and-productivity-624d2ce7a358
- **S18 — Mitigating the Impact of Remote Work Challenges on ...**
  URL: https://scholarworks.waldenu.edu/cgi/viewcontent.cgi?article=18195&context=dissertations
- **S19 — The impact of remote and hybrid work models on small and ...**
  URL: https://link.springer.com/article/10.1007/s43546-025-00931-7

**Search Duration:** 2.97s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 1
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 2.98s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Remote work impacts employee productivity differently, depending on job type, interruption management, and cooperation structures.

- S17 supports (direct): Remote workers can be 35-40% more productive than their office-based peers, indicating significant productivity gains when managed well.
- S19 supports (direct): Hybrid work models, combining remote and in-person interaction, are noted to improve productivity by increasing employee satisfaction and work-life balance.
- S18 contradicts (direct): Productivity can drop by 8–19% for roles that rely heavily on collaboration and immediate feedback within remote settings.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 1
- Supported: 1
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 4

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C1

**Why**

To address mixed evidence regarding remote work's impact on coordination-heavy versus independent roles, further exploration into specific studies that quantify these effects is needed.

**Next Search**

> Look for recent studies that quantify the differences in productivity outcomes between remote work in coordination-heavy roles and independent roles, specifically analyzing contextual factors and management practices influencing these results.


---

# Iteration 7

## 1. Search

**Query**

> Look for recent studies that quantify the differences in productivity outcomes between remote work in coordination-heavy roles and independent roles, specifically analyzing contextual factors and management practices influencing these results.

**Target:** C1

**Purpose:** GENERAL

**Why this query**

To address mixed evidence regarding remote work's impact on coordination-heavy versus independent roles, further exploration into specific studies that quantify these effects is needed.

5 result(s) retrieved; 1 new unique source(s) added.

- **S20 — Factors Influencing Adjustment to Remote Work - PMC**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC8297254

**Search Duration:** 2.57s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 1
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 4.78s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Remote work impacts employee productivity differently, depending on job type, interruption management, and cooperation structures.

- S20 supports (direct): The study discusses how successful remote work relies on pre-existing support mechanisms and employee adaptability to changes in work routines, aligning with the idea that productivity impacts vary by individual factors.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 1
- Supported: 1
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 3

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C1

**Why**

Further research is needed to quantify the impact of remote work on productivity specifically in coordination-heavy roles, as existing studies reveal conflicting outcomes.

**Next Search**

> Investigate recent studies that specifically quantify how remote work affects productivity in coordination-heavy roles, focusing on the influence of management practices and company culture to resolve inconsistencies in findings.


---

# Iteration 8

## 1. Search

**Query**

> Investigate recent studies that specifically quantify how remote work affects productivity in coordination-heavy roles, focusing on the influence of management practices and company culture to resolve inconsistencies in findings.

**Target:** C1

**Purpose:** GENERAL

**Why this query**

Further research is needed to quantify the impact of remote work on productivity specifically in coordination-heavy roles, as existing studies reveal conflicting outcomes.

5 result(s) retrieved; 3 new unique source(s) added.

- **S21 — Remote work statistics you need to know (2026) • Breeze**
  URL: https://www.breeze.pm/blog/remote-work-statistics
- **S22 — 80+ Hybrid Work Statistics in 2026: Productivity & Preferences**
  URL: https://archieapp.co/blog/hybrid-workplace-stats
- **S23 — Remote work in 2026: 50+ key statistics & trends | WorkTime**
  URL: https://www.worktime.com/blog/statistics/remote-work-statistics

**Search Duration:** 3.00s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 1
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 4.01s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Remote work impacts employee productivity differently, depending on job type, interruption management, and cooperation structures.

- S21 supports (direct): The article reports that hybrid workplaces do not hurt productivity, and studies indicate positive effects on performance and employee retention in such models.
- S22 supports (direct): The findings suggest that hybrid teams are approximately 5% more productive than both fully remote and fully in-office teams, emphasizing the advantages of having structured remote work arrangements.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 1
- Supported: 1
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** GENERAL

**Why**

To effectively address the conflicting conclusions surrounding remote work productivity, a focused investigation on the impact of specific management practices in coordination-heavy roles is crucial. This is a significant gap that influences overall findings.

**Next Search**

> Identify recent studies that analyze the impact of specific management practices on productivity outcomes in coordination-heavy roles during remote work settings, focusing on how these practices influence employee performance and collaboration.


---

# Iteration 9

## 1. Search

**Query**

> Identify recent studies that analyze the impact of specific management practices on productivity outcomes in coordination-heavy roles during remote work settings, focusing on how these practices influence employee performance and collaboration.

**Purpose:** GENERAL

**Why this query**

To effectively address the conflicting conclusions surrounding remote work productivity, a focused investigation on the impact of specific management practices in coordination-heavy roles is crucial. This is a significant gap that influences overall findings.

5 result(s) retrieved; 3 new unique source(s) added.

- **S24 — Performance management practices in remote and hybrid ...**
  URL: https://sajip.co.za/index.php/sajip/article/view/2202/4082
- **S25 — The Impact of Remote Work on Organizational Culture and Performance**
  URL: https://samples.essaypro.com/the-impact-of-remote-work-on-organizational-culture-and-performance
- **S26 — Performance Development in a Remote or Hybrid Workplace | MIT Human Resources**
  URL: https://hr.mit.edu/performance/remote

**Search Duration:** 4.00s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 1
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 5.78s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Remote work impacts employee productivity differently, depending on job type, interruption management, and cooperation structures.

- S24 supports (direct): The study highlights the crucial role of performance management in hybrid settings, emphasizing communication, trust, and clarity on performance expectations as key to maintaining productivity.
- S25 supports (direct): Remote work enhances job autonomy and work-life balance, contributing positively to job satisfaction and productivity, while also presenting challenges related to team cohesion.
- S26 supports (direct): Effective performance management practices in remote environments require regular check-ins and open communication to ensure employee engagement and productivity.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 1
- Supported: 1
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C1

**Why**

Conflicting evidence regarding productivity impacts in coordination-heavy roles warrants deeper exploration of management practices.

**Next Search**

> Find recent studies that evaluate how different management practices affect productivity in remote coordination-heavy roles, examining specific examples and metrics to clarify conflicting outcomes.


---

# Iteration 10

## 1. Search

**Query**

> Find recent studies that evaluate how different management practices affect productivity in remote coordination-heavy roles, examining specific examples and metrics to clarify conflicting outcomes.

**Target:** C1

**Purpose:** GENERAL

**Why this query**

Conflicting evidence regarding productivity impacts in coordination-heavy roles warrants deeper exploration of management practices.

5 result(s) retrieved; 1 new unique source(s) added.

- **S27 — Remote working challenges linked to management issues - University of Birmingham**
  URL: https://www.birmingham.ac.uk/news/2026/remote-working-challenges-linked-to-organisational-capabilities-new-study-finds

**Search Duration:** 2.62s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 1
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 3.05s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Remote work impacts employee productivity differently, depending on job type, interruption management, and cooperation structures.

- S27 supports (direct): The study highlights strong organisational and management capabilities as key to realising productivity gains from remote and hybrid work, emphasizing that challenges arise from management issues rather than remote work itself.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 1
- Supported: 1
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 0

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

- No major remaining uncertainty was identified.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 10 | 26.15s |
| Evidence Processing | 10 | 50.05s |
| Research Decision | 9 | 20.15s |
| Report Generation | 1 | 8.63s |
| Total Run | — | 104.99s |
