# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions.

**Status:** Completed

**Stop Reason:** sufficient_evidence

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 2 / 10

**Unique Sources:** 10

**OpenAI Calls:** 3

**Tavily Calls:** 2

**Started:** 2026-09-01T06:32:01-04:00

**Ended:** 2026-09-01T06:32:58-04:00

**Total Runtime:** 56.89s

---

# Iteration 1

## 1. Search

**Query**

> Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions.

**Why this query**

This is the user's original research question.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S1 — Remote Work Productivity Study 2026: 50+ Studies | eMonitor**
  URL: https://www.employee-monitoring.net/blog/remote-work-productivity-research-meta-analysis
- **S2 — Are remote workers more productive? That’s the wrong question. - Stack Overflow**
  URL: https://stackoverflow.blog/2023/11/27/are-remote-workers-more-productive-that-s-the-wrong-question
- **S3 — The rise in remote work since the pandemic and its impact ...**
  URL: https://www.bls.gov/opub/btn/volume-13/remote-work-productivity.htm
- **S4 — In-Office vs Remote Productivity: What the Data Shows | Worklytics**
  URL: https://www.worklytics.co/blog/in-office-vs-remote-day-productivity-which-is-better
- **S5 — The Rise of Remote Work: Evidence on Productivity and ...**
  URL: https://www.hbs.edu/ris/download.aspx?name=20-138.pdf

**Search Duration:** 2.37s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Remote work does not have a uniform effect on productivity; effects vary by work arrangement, task type, worker experience, and management conditions.

**Confidence:** High

**Why this confidence level**

Multiple sources consistently identify heterogeneity and measurement differences as central explanations, although S4 is a vendor source and should receive less weight.

**Evidence**

- The BLS review states that effects depend on task type, technology, home environment, motivation, and management practices; it also distinguishes individual productivity from aggregate productivity. [S3]
- The Stack Overflow review notes that studies use different definitions and measures of productivity, and that full-time remote, hybrid, and office work are often conflated. [S2]
- The Worklytics article similarly reports better individual focus remotely but stronger collaboration advantages in offices, while emphasizing that leadership, meeting culture, and work design also matter. [S4]

#### Finding 2

**Claim**

The controlled-experiment evidence described in the retrieved material is generally positive or neutral for individual output, especially for call-center work and hybrid arrangements.

**Confidence:** Medium

**Why this confidence level**

The pattern is coherent, but the primary experimental papers are not directly retrieved here; most numerical details come through secondary summaries, and the sources describe somewhat different experiments and outcomes.

**Evidence**

- The reported 2015 Ctrip randomized experiment assigned 249 call-center employees to remote or office work and found remote workers completed 13.5% more calls, alongside lower attrition and higher job satisfaction. [S1]
- The BLS synthesis says randomized experiments at individual firms found small positive effects for hybrid and fully remote work using measures such as emails, calls, and manager-assigned ratings. [S3]
- The reported 2024 Trip.com randomized hybrid experiment assigned 1,612 employees to two remote days or five office days and found no statistically significant difference in performance reviews, promotions, coding output, or marketing revenue, while resignations fell by roughly one-third. [S1]
- The Stack Overflow review summarizes Stanford evidence as finding about a 10% productivity drop for fully remote work but no apparent productivity effect for hybrid work. [S2]

#### Finding 3

**Claim**

Some observational and survey evidence finds positive or improving productivity perceptions, but it is weaker for causal inference than randomized evidence.

**Confidence:** Medium

**Why this confidence level**

The sources provide broad observational and company-survey evidence, but associations can reflect industry composition, worker selection, simultaneous technological changes, and pandemic recovery rather than remote work itself.

**Evidence**

- In repeated surveys of small-business owners, 70% initially reported a productivity dip after the shift to remote work, but the median owner reported a positive effect by 2021. Owners attributed improvement partly to technology, training, task changes, and better remote management. [S5]
- The BLS analysis reports that total-factor-productivity growth from 2019–21 and 2019–22 was positively associated with the increase in remote work across 61 private-sector industries, after accounting for pre-pandemic productivity trends. [S3]
- The same BLS source reports that another aggregate analysis across 43 industries found little relationship between an industry's ability to work entirely remotely and labor-productivity growth. [S3]

#### Finding 4

**Claim**

Company-level and workplace-data evidence can show short-run declines or collaboration costs even when individual focused-task output is stable or higher.

**Confidence:** Medium

**Why this confidence level**

The task-level mechanism is plausible and consistently described, but the retrieved material does not provide enough primary methodological detail to verify all reported estimates or establish their generality.

**Evidence**

- The BLS review says a couple of single-firm pandemic case studies found short-run productivity declines, contrasting with positive findings from randomized experiments. [S3]
- The Worklytics source claims remote work improves focus productivity by roughly 5–15% but that offices facilitate collaboration, spontaneous problem-solving, knowledge sharing, mentoring, and innovation. [S4]
- The reported fully-remote research summary in S1 says output reductions of 10–20% occurred for some roles, particularly highly collaborative roles and newly hired workers. [S1]

#### Finding 5

**Claim**

Different studies reach conflicting conclusions largely because they measure different outcomes and populations, compare different arrangements, and observe different stages of organizational adaptation.

**Confidence:** High

**Why this confidence level**

These explanations are directly supported across several sources and account for both positive, neutral, and negative findings without assuming that one estimate applies to every setting.

**Evidence**

- The sources distinguish calls, emails, lines of code, revenue, performance reviews, hours worked, self-reported productivity, and industry-level TFP; these are not interchangeable measures. [S1] [S2] [S3]
- The evidence covers call centers, developers, knowledge workers, small firms, and broad industries, with different requirements for concentration, collaboration, training, and physical presence. [S1] [S3] [S4] [S5]
- Survey evidence shows an initial productivity decline followed by more positive assessments after firms invested in technology, training, task redesign, and management practices. [S5]
- Selection and retention can change measured productivity: workers who prefer remote work may select into it, while lower attrition can improve organizational performance even if per-worker output is unchanged. [S1] [S2] [S5]

### Conflicts Found

- The retrieved sources report different results for fully remote work: the Ctrip randomized experiment found a 13.5% increase in calls, whereas another Stanford-related study is summarized as finding about a 10% decline, and S1 reports 10–20% declines for some roles. [S1] [S2]
- Aggregate evidence is inconsistent: BLS reports a positive association between increased remote work and TFP growth across 61 industries, while another 43-industry analysis found little relationship between remote-work suitability and aggregate labor-productivity growth. [S3]
- Individual-level randomized evidence is described as positive or neutral, while pandemic-era single-firm case studies reportedly found short-run declines. These results may be conditional on adjustment period, firm, and outcome measure rather than directly contradictory. [S1] [S3] [S5]
- Employer perceptions changed from predominantly negative early in the pandemic to positive by 2021, but owners still reported monitoring and skill-learning difficulties, especially in larger firms. [S5]

### Important Gaps

- What are the exact designs, samples, treatment definitions, and peer-reviewed results of the primary Ctrip and Trip.com experiments?
- How much of the reported productivity effect reflects measured individual output versus coordination, innovation, onboarding, learning, and long-term organizational performance?
- Are the aggregate BLS associations robust to industry-specific pandemic shocks, worker selection, occupational mix, and reverse causality?
- How generalizable are call-center and knowledge-worker findings to other occupations and to fully remote firms rather than hybrid arrangements?
- Which management practices and task characteristics determine when remote work produces gains versus collaboration or onboarding losses?

**Analysis Duration:** 19.80s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The main qualitative answer can be stated responsibly, but the question specifically asks for comparison across controlled experiments, observational studies, and company-level data. The retrieved evidence relies heavily on secondary summaries and includes unverified numerical claims, while the primary experimental papers and stronger company-level datasets were not directly retrieved. A focused search for the primary randomized studies would materially improve precision and confidence.

**Next Search**

> Nicholas Bloom Trip.com randomized hybrid work experiment Nature 2024 Ctrip 2015 remote productivity primary paper

---

# Iteration 2

## 1. Search

**Query**

> Nicholas Bloom Trip.com randomized hybrid work experiment Nature 2024 Ctrip 2015 remote productivity primary paper

**Why this query**

The main qualitative answer can be stated responsibly, but the question specifically asks for comparison across controlled experiments, observational studies, and company-level data. The retrieved evidence relies heavily on secondary summaries and includes unverified numerical claims, while the primary experimental papers and stronger company-level datasets were not directly retrieved. A focused search for the primary randomized studies would materially improve precision and confidence.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S6 — Hybrid Work Statistics 2026: Schedules, Productivity Outcomes, and the Return-to-Office Debate**
  URL: https://speakwiseapp.com/blog/hybrid-work-statistics
- **S7 — Three-day hybrid work week is success, study published in Nature says**
  URL: https://www.cnbc.com/2024/06/14/three-day-hybrid-work-week-is-success-study-published-in-nature-says.html
- **S8 — Hybrid work is a “win-win-win” for companies, workers, study finds | Stanford Institute for Economic Policy Research (SIEPR)**
  URL: https://siepr.stanford.edu/news/hybrid-work-win-win-win-companies-workers-study-finds
- **S9 — New Nature paper on hybrid working from home | Nick Bloom posted on the topic | LinkedIn**
  URL: https://www.linkedin.com/posts/nick-bloom-stanford_new-nature-paper-on-hybrid-working-from-home-activity-7207011377243201537-1Is2
- **S10 — The Impact of Hybrid Working on Employee Retention and Performance**
  URL: https://voxchina.org/show-3-367.html

**Search Duration:** 1.98s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The strongest new evidence supports a neutral productivity effect for a structured hybrid schedule—two days working from home and three days in the office—among professional employees at Trip.com.

**Confidence:** High

**Why this confidence level**

The finding is consistently reported by the study authors’ institutional summary, the authors’ own post, and an independent news report. It directly concerns a randomized comparison, although generalizability beyond this firm and arrangement remains limited.

**Evidence**

- The Trip.com randomized trial assigned 1,612 employees in engineering, marketing, accounting, and finance to either two home days per week or full-time office work. It found no effect on performance reviews, promotions, innovation, development, leadership, code output, or other business measures. [S8] [S9] [S10]
- The study’s authors describe the trial as a six-month randomized experiment, with follow-up performance and promotion data extending for up to two years. [S8] [S10]

#### Finding 2

**Claim**

The Trip.com experiment found a substantial retention benefit without a measured productivity penalty.

**Confidence:** High

**Why this confidence level**

The result is reported consistently across multiple sources, including the institutional summary and author-linked material. The evidence is strongest for retention, not necessarily for total firm productivity.

**Evidence**

- Hybrid workers’ quit rates fell by approximately one-third; the reported non-manager quit rates were 2.4% for hybrid workers versus 7.2% for the office-only control group. [S7] [S8] [S10]
- Hybrid employees reported higher work-life-balance and life-satisfaction scores, and the retention effect was especially pronounced among women, non-managers, and workers with long commutes. [S7] [S8] [S10]

#### Finding 3

**Claim**

The new evidence strengthens the explanation that hybrid and fully remote work should not be treated as equivalent treatments.

**Confidence:** High

**Why this confidence level**

The distinction is directly stated in the new sources and is consistent with the accumulated evidence about differing occupations, outcomes, and work arrangements.

**Evidence**

- The institutional summary explicitly notes that critics often conflate hybrid work with fully remote work and that earlier studies focused heavily on call centers, data entry, and other easily measured jobs, whereas the Trip.com trial concerned university-trained professional roles. [S8] [S10]
- The Trip.com sample consisted of professional employees in engineering, marketing, accounting, and finance, while earlier evidence in the research state includes call-center workers and other occupations with different task structures. [S8] [S10] [S1] [S3]

#### Finding 4

**Claim**

Managers’ expectations about hybrid productivity can differ from measured outcomes and may update after direct experience with the arrangement.

**Confidence:** Medium

**Why this confidence level**

The directional change is consistently reported, but the precise numerical estimates come mainly from an author post and summaries rather than independently presented primary tables in the retrieved material.

**Evidence**

- Managers initially predicted that hybrid work would reduce productivity, but after the six-month experiment their assessments became neutral or slightly positive; the author’s post reports a shift from an expected 2.6% decline to an estimated 1% increase. [S8] [S9] [S10]

#### Finding 5

**Claim**

The new sources do not resolve whether fully remote work improves or reduces productivity across occupations; they mainly improve the evidence for hybrid work.

**Confidence:** High

**Why this confidence level**

The treatment definition is explicit, and the sources themselves distinguish the tested hybrid arrangement from fully remote work. The remaining uncertainty is therefore substantive rather than merely methodological.

**Evidence**

- The new randomized evidence tests two home days per week versus five office days, not fully remote work. [S8] [S10]
- The sources acknowledge that findings for fully remote work have been mixed and often negative in particular jobs, while the accumulated research includes both positive call-center results and reported declines for some collaborative or newly hired workers. [S8] [S1] [S2] [S3]

### Conflicts Found

- The new sources strongly support zero productivity loss for Trip.com’s structured hybrid arrangement, but this does not eliminate the accumulated conflict over fully remote work, where the sources report both gains and declines. These are conditional differences in treatment, occupation, and measurement rather than a direct contradiction. [S8] [S10] [S1] [S2] [S3]
- S6 presents the Trip.com result as broadly representative and describes the evidence as unusually clear, whereas the more specific study descriptions limit the sample to one Chinese technology firm and selected professional divisions. The broader generalization is therefore less supported than the trial’s internal result. [S6] [S8] [S10]

### Important Gaps

- How do productivity effects differ under fully remote arrangements rather than two-day hybrid schedules?
- How generalizable is the Trip.com result to other countries, firms, occupations, and organizational cultures?
- Do collaboration, mentoring, onboarding, innovation, and knowledge-sharing effects emerge over longer periods than the measured follow-up?
- How do management quality, task interdependence, worker seniority, and home working conditions moderate the effects?
- Can aggregate productivity studies separate remote-work effects from pandemic recovery, technology adoption, industry composition, and worker selection?

**Analysis Duration:** 13.88s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The new sources materially strengthen the controlled-experiment evidence and clarify the central source of apparent disagreement: hybrid work has stronger neutral/positive causal evidence than fully remote work, while observational and company-level estimates remain sensitive to selection, timing, occupation, and outcome measurement. The remaining gaps concern generalizability and fully remote work, but the accumulated evidence is sufficient to answer the original comparative question responsibly without another search.

**Stop Reason:** sufficient_evidence

---

# Final Research Decision

**Research Stopped Because**

The analyzer determined that the important parts of the question could be answered responsibly.

**Stop Reason:** sufficient_evidence

**Searches Performed:** 2

**Unique Sources:** 10

**Remaining Uncertainty**

- The causal effect of fully remote work across different occupations remains unresolved.
- The generalizability of the Trip.com hybrid trial to other countries, firms, occupations, and organizational cultures is uncertain.
- The retrieved evidence does not fully quantify long-term effects on onboarding, mentoring, innovation, knowledge sharing, or career development.
- Aggregate estimates may not fully separate remote-work effects from pandemic recovery, technology adoption, industry composition, occupational mix, worker selection, and reverse causality.
- More evidence is needed on which management practices, task characteristics, worker seniority, and home-working conditions produce gains versus coordination or learning losses.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 2 | 4.35s |
| OpenAI Analysis | 2 | 33.67s |
| Report Generation | 1 | 18.87s |
| Total Run | — | 56.89s |
