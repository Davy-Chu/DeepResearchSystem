# Research Run Log

## Run Summary

**System Version:** evidence-ledger-v1

**Research Question**

Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 10

**OpenAI Calls:** 6

**Tavily Calls:** 3

**Started:** 2026-08-31T17:41:39-04:00

**Ended:** 2026-08-31T17:42:53-04:00

**Total Runtime:** 74.58s

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
- **S3 — Work from home and employee well-being: a double-edged ...**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12333122
- **S4 — The rise in remote work since the pandemic and its impact on ...**
  URL: https://www.bls.gov/opub/btn/volume-13/remote-work-productivity.htm
- **S5 — Are remote workers more productive? That’s the wrong question. - Stack Overflow**
  URL: https://stackoverflow.blog/2023/11/27/are-remote-workers-more-productive-that-s-the-wrong-question

**Search Duration:** 2.97s

---

## 2. Evidence Processing

- New claim proposals: 6
- Existing claim updates: 0
- New gaps: 3
- Resolved gaps: 0

**Processing Duration:** 17.94s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

Controlled experiments reported in the supplied sources find that remote-work effects vary by arrangement and task: a 2015 Ctrip experiment reportedly found a 13.5% increase in calls completed under mostly remote work, whereas a 2024 Trip.com hybrid experiment reportedly found no statistically significant difference in performance-related outcomes from office work.

- S1 supports (direct): Reports results from the 2015 Ctrip randomized experiment and the 2024 Trip.com randomized hybrid experiment, including the positive fully remote result and null hybrid result.
- S4 supports (indirect): Summarizes randomized experiments as finding small positive effects on individual productivity, while noting that effects depend on tasks and measurement.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C2

**Claim**

Observational and quasi-experimental evidence in the supplied sources does not yield a uniform productivity effect: some pandemic-period single-firm case studies found short-run declines, while the BLS industry analysis found that increases in remote work were positively associated with total-factor-productivity growth across 61 private-sector industries after accounting for pre-pandemic trends.

- S4 supports (direct): Directly reports short-run declines in a couple of pandemic-era single-firm case studies and a positive association between the rise in remote work and TFP growth across 61 industries.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C3

**Claim**

At the company or aggregate-industry level, remote-work intensity may be associated with productivity outcomes that differ from individual-task results: Fernald et al. (as summarized by BLS) reportedly found little relationship between an industry's ability to work entirely remotely and aggregate labor-productivity performance, while the BLS analysis found positive associations with pandemic-period TFP growth.

- S4 supports (direct): Reports both the near-null aggregate relationship across 43 industries attributed to Fernald et al. and the positive TFP association in the BLS analysis across 61 industries.

**Confidence:** MEDIUM

**Status:** CONFLICTING

### New Claim C4

**Claim**

The supplied sources attribute conflicting conclusions partly to differences in what productivity means and how it is measured: studies use outcomes such as calls, emails, lines of code, performance ratings, self-reported productivity, and aggregate industry productivity, which are not interchangeable.

- S5 supports (direct): Explicitly states that productivity is not a straightforward metric and contrasts device-monitoring measures with self-reports and other measures such as lines of code and lead time.
- S4 supports (direct): States that studies examine individual labor productivity using various proxies and contrasts those results with aggregate economic-performance measures.
- S1 supports (indirect): Distinguishes individual focused tasks, collaborative tasks, and organizational outcomes in its synthesis.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C5

**Claim**

Work type and work design appear to moderate remote-work productivity: the supplied sources associate remote work with stronger individual focus or deep-work outcomes, while associating office work with faster collaboration, spontaneous problem-solving, knowledge sharing, mentoring, and innovation; hybrid arrangements are presented as potentially balancing these functions.

- S2 supports (direct): States that remote work improves individual focus productivity while offices support collaboration and spontaneous problem-solving, and presents hybrid work as balancing focus and collaboration.
- S1 supports (direct): Reports a positive effect for focused tasks and a negative effect for collaborative tasks, and describes the fully remote penalty as concentrated in some highly collaborative or newly hired roles.
- S4 supports (direct): States that effects depend on task type, technology, home environment, motivation, and management practices.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C6

**Claim**

Productivity effects should be distinguished from organizational outcomes: the supplied experimental summaries report higher job satisfaction and lower attrition under remote or hybrid arrangements even when productivity was unchanged or when productivity gains were accompanied by social-isolation concerns.

- S1 supports (direct): Reports higher satisfaction and lower attrition in the Ctrip and Trip.com experiments, while also noting social isolation and that hybrid productivity was not measurably different from office work.
- S4 supports (direct): States that randomized experiments found lower turnover as job satisfaction rose and that this could reduce hiring costs.
- S5 supports (indirect): Reports employee preference for flexibility and links return-to-office mandates to recruitment and retention concerns, while distinguishing these outcomes from productivity measurement.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Gap G1

The supplied sources do not provide the underlying full reports or sufficient methodological detail to directly compare the causal validity, worker populations, time horizons, and productivity definitions of the cited controlled experiments, observational studies, and company-level analyses.

### New Gap G2

The evidence does not establish a single causal estimate for fully remote work across occupations; the supplied material is concentrated on knowledge work and call-center or professional settings, with limited evidence for roles requiring physical presence or intensive synchronous collaboration.

### New Gap G3

The apparent difference between the near-null 43-industry relationship reported for Fernald et al. and the positive 61-industry BLS TFP association cannot be reconciled from the supplied excerpts because their model specifications, controls, industry samples, and treatment definitions are not given.

---

## 4. Current Research State

- Claims: 6
- Supported: 5
- Weak: 0
- Conflicting: 1
- Insufficient Evidence: 0
- Open Gaps: 3
- Remaining Searches: 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** GAP G1

**Why**

High-value gap: the supplied evidence is mostly secondary summaries and lacks methodological detail needed to compare causal strength and reconcile conflicting study results.

**Next Search**

> Underlying studies on remote-work productivity: Ctrip 2015 randomized experiment, Trip.com 2024 hybrid randomized trial, pandemic firm case studies, Fernald industry analysis, and BLS 61-industry TFP study—compare samples, designs, controls, productivity measures, and findings.


---

# Iteration 2

## 1. Search

**Query**

> Underlying studies on remote-work productivity: Ctrip 2015 randomized experiment, Trip.com 2024 hybrid randomized trial, pandemic firm case studies, Fernald industry analysis, and BLS 61-industry TFP study—compare samples, designs, controls, productivity measures, and findings.

**Target:** G1

**Purpose:** GENERAL

**Why this query**

High-value gap: the supplied evidence is mostly secondary summaries and lacks methodological detail needed to compare causal strength and reconcile conflicting study results.

5 result(s) retrieved; 3 new unique source(s) added.

- **S6 — Does Working from Home Increase Productivity? (2026)**
  URL: https://emailanalytics.com/does-working-from-home-increase-productivity
- **S7 — 40+ remote work productivity statistics, trends & data for 2026**
  URL: https://www.worktime.com/blog/statistics/remote-work-productivity-statistics-trends-data
- **S8 — Work From Home Productivity Statistics 2026: Remote Work Performance Analysis**
  URL: https://www.makerstations.io/work-from-home-productivity-statistics

**Search Duration:** 2.72s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 6
- New gaps: 1
- Resolved gaps: 0

**Processing Duration:** 17.62s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Controlled experiments reported in the supplied sources find that remote-work effects vary by arrangement and task: a 2015 Ctrip experiment reportedly found a 13.5% increase in calls completed under mostly remote work, whereas a 2024 Trip.com hybrid experiment reportedly found no statistically significant difference in performance-related outcomes from office work.

- S6 supports (direct): Reports the Ctrip randomized trial as finding about a 13% productivity gain and the 2024 randomized Trip.com trial as finding no effect on measured performance.
- S8 supports (direct): Reports a 13% performance increase in the Ctrip randomized trial and identical performance-review outcomes for Trip.com hybrid workers compared with office workers.
- S7 supports (direct): Summarizes the 2024 Nature hybrid-work study as finding no negative performance effect while reporting reduced turnover.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

Observational and quasi-experimental evidence in the supplied sources does not yield a uniform productivity effect: some pandemic-period single-firm case studies found short-run declines, while the BLS industry analysis found that increases in remote work were positively associated with total-factor-productivity growth across 61 private-sector industries after accounting for pre-pandemic trends.

- S6 supports (direct): Reports an 8% to 19% productivity decline among IT workers in the Gibbs, Mengel, and Siemroth study, adding a quantified example of an observational or quasi-experimental negative finding.
- S7 supports (direct): Repeats the BLS finding of a positive association between remote-work adoption and total-factor-productivity growth across 61 industries, including an estimated 0.08 to 0.09 percentage-point increase in TFP growth per percentage-point increase in remote work.
- S8 supports (direct): Repeats the positive BLS 61-industry association between remote-work adoption and TFP growth after controls for pre-pandemic trends.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C3

**Claim**

At the company or aggregate-industry level, remote-work intensity may be associated with productivity outcomes that differ from individual-task results: Fernald et al. (as summarized by BLS) reportedly found little relationship between an industry's ability to work entirely remotely and aggregate labor-productivity performance, while the BLS analysis found positive associations with pandemic-period TFP growth.

- S7 supports (direct): Reports a positive BLS association between remote-work adoption and aggregate TFP growth across 61 industries, consistent with the aggregate-level positive result already recorded.
- S8 supports (direct): Reports the same positive 61-industry BLS TFP association and its adjustment for pre-pandemic trends.

**Confidence:** MEDIUM → MEDIUM

**Status:** CONFLICTING → CONFLICTING

### Updated Claim C4

**Claim**

The supplied sources attribute conflicting conclusions partly to differences in what productivity means and how it is measured: studies use outcomes such as calls, emails, lines of code, performance ratings, self-reported productivity, and aggregate industry productivity, which are not interchangeable.

- S6 supports (direct): Contrasts measured performance gains in the Ctrip trial with self-reported productivity and recommends output-based rather than time-based measures, illustrating that reported outcomes depend on measurement choice.
- S7 supports (direct): Places self-reported productivity, manager assessments, hours worked, and macro-level output in the same synthesis, explicitly showing that these are distinct indicators.
- S8 supports (direct): Contrasts randomized-trial performance measures with self-reported productivity and aggregate TFP measures.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

Work type and work design appear to moderate remote-work productivity: the supplied sources associate remote work with stronger individual focus or deep-work outcomes, while associating office work with faster collaboration, spontaneous problem-solving, knowledge sharing, mentoring, and innovation; hybrid arrangements are presented as potentially balancing these functions.

- S6 supports (direct): Attributes reported remote-work gains to fewer distractions, reduced stress, commute elimination, and greater control over the work environment, while noting that home can also introduce distractions.
- S7 supports (direct): Reports that many remote workers find focused work easier and links reduced interruptions and digital collaboration to maintained or improved output.
- S8 supports (indirect): Reports that occupation drives substantial variation in telework prevalence and presents hybrid work as the dominant arrangement among remote-capable workers, consistent with heterogeneous effects by role and arrangement.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C6

**Claim**

Productivity effects should be distinguished from organizational outcomes: the supplied experimental summaries report higher job satisfaction and lower attrition under remote or hybrid arrangements even when productivity was unchanged or when productivity gains were accompanied by social-isolation concerns.

- S6 supports (direct): Reports higher satisfaction and a 50% reduction in attrition in the Ctrip study, while presenting retention and cost effects as distinct from measured productivity.
- S7 supports (direct): Reports a 33% reduction in employee turnover in the 2024 hybrid-work experiment despite no negative performance effect.
- S8 supports (direct): Reports 33% lower quitting in the Trip.com hybrid experiment alongside identical performance-review outcomes relative to office peers.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### New Gap G4

The newly retrieved sources repeat numerous survey-based percentages and large claims about stress, distractions, monitoring, savings, and productivity, but do not identify sufficient sampling, instruments, comparison groups, or underlying reports to assess their validity or comparability with the experimental and industry evidence.

---

## 4. Current Research State

- Claims: 6
- Supported: 5
- Weak: 0
- Conflicting: 1
- Insufficient Evidence: 0
- Open Gaps: 4
- Remaining Searches: 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** GAP G3

**Why**

Resolve the important aggregate-level conflict by comparing the Fernald and BLS analyses’ samples, specifications, controls, and productivity measures.

**Next Search**

> Fernald et al. remote work industry productivity 43 industries versus BLS 61-industry TFP analysis: find original reports and compare sample years, remote-work measures, controls, model specifications, and causal versus associational interpretation.


---

# Iteration 3

## 1. Search

**Query**

> Fernald et al. remote work industry productivity 43 industries versus BLS 61-industry TFP analysis: find original reports and compare sample years, remote-work measures, controls, model specifications, and causal versus associational interpretation.

**Target:** G3

**Purpose:** GENERAL

**Why this query**

Resolve the important aggregate-level conflict by comparing the Fernald and BLS analyses’ samples, specifications, controls, and productivity measures.

5 result(s) retrieved; 2 new unique source(s) added.

- **S9 — Productivity and Remote Work : U.S. Bureau of Labor Statistics**
  URL: https://www.bls.gov/productivity/articles-and-research/remote-work/productivity-and-remote-work.htm
- **S10 — 80+ Remote Work Statistics for 2026: The Complete Data ...**
  URL: https://remotive.com/blog/remote-work-statistics-hiring-trends

**Search Duration:** 2.22s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 2
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 7.14s

---

## 3. Ledger Updates

### Updated Claim C2

**Claim**

Observational and quasi-experimental evidence in the supplied sources does not yield a uniform productivity effect: some pandemic-period single-firm case studies found short-run declines, while the BLS industry analysis found that increases in remote work were positively associated with total-factor-productivity growth across 61 private-sector industries after accounting for pre-pandemic trends.

- S9 supports (direct): Official BLS research reports statistically significant positive associations between increases in remote work and TFP growth across 61 private-business industries: 0.08 percentage points of TFP growth per one-percentage-point increase in remote work in 2019–21, 0.09 in 2019–22, and 0.05 when using excess pandemic-period TFP growth relative to 2007–19 trends.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C3

**Claim**

At the company or aggregate-industry level, remote-work intensity may be associated with productivity outcomes that differ from individual-task results: Fernald et al. (as summarized by BLS) reportedly found little relationship between an industry's ability to work entirely remotely and aggregate labor-productivity performance, while the BLS analysis found positive associations with pandemic-period TFP growth.

- S9 supports (direct): Official BLS analysis reports statistically significant positive associations between the increase in remote work and TFP growth across 61 private-business industries, including a smaller but still positive association after comparing pandemic-period growth with 2007–19 trends.

**Confidence:** MEDIUM → MEDIUM

**Status:** CONFLICTING → CONFLICTING

---

## 4. Current Research State

- Claims: 6
- Supported: 5
- Weak: 0
- Conflicting: 1
- Insufficient Evidence: 0
- Open Gaps: 4
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

- The underlying full reports and sufficient methodological detail for the cited studies are not supplied.
- No single causal estimate for fully remote work across occupations can be established; the evidence is concentrated in call-center, knowledge-work, and professional settings.
- The discrepancy between the near-null 43-industry analysis and the positive 61-industry BLS analysis remains unresolved.
- Several reported survey percentages and claims about stress, distractions, monitoring, savings, and productivity lack sufficient information about sampling, instruments, comparison groups, or underlying reports.
- The ledger stopped because the maximum iteration limit was reached; no independent verification records were supplied.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 7.92s |
| Evidence Processing | 3 | 42.70s |
| Research Decision | 2 | 6.22s |
| Report Generation | 1 | 17.73s |
| Total Run | — | 74.58s |
