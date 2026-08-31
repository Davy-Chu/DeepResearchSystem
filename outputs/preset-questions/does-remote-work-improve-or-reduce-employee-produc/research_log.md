# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions.

**Status:** Completed

**Stop Reason:** sufficient_evidence

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 14

**OpenAI Calls:** 4

**Tavily Calls:** 3

**Started:** 2026-08-31T17:03:52-04:00

**Ended:** 2026-08-31T17:05:08-04:00

**Total Runtime:** 75.75s

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
- **S2 — In-Office vs Remote Productivity: What the Data Shows | Worklytics**
  URL: https://www.worklytics.co/blog/in-office-vs-remote-day-productivity-which-is-better
- **S3 — The rise in remote work since the pandemic and its impact on ...**
  URL: https://www.bls.gov/opub/btn/volume-13/remote-work-productivity.htm
- **S4 — Remote Work Productivity Study: Surprising Findings From a 4-Year ...**
  URL: https://www.greatplacetowork.com/resources/blog/remote-work-productivity-study-finds-surprising-reality-2-year-study
- **S5 — [PDF] The Rise of Remote Work: Evidence on Productivity and Preferences ...**
  URL: https://www.hbs.edu/ris/download.aspx?name=20-138.pdf

**Search Duration:** 2.55s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Remote work does not have a uniform productivity effect; results vary by task, work arrangement, worker experience, and management practices.

**Confidence:** High

**Why this confidence level**

This explanation is directly and consistently supported by the official BLS synthesis and a separate review, although the latter is a commercial source.

**Evidence**

- The BLS review states that effects depend on task type, technology, home environment, worker motivation, and management, and distinguishes positive individual-level findings from negative single-firm pandemic case studies and near-zero aggregate effects. [S3]
- The Worklytics synthesis similarly reports higher individual focus productivity remotely but advantages for offices in collaboration and spontaneous problem-solving; it concludes that work design and leadership may matter more than location alone. [S2]

#### Finding 2

**Claim**

Controlled experiments generally find neutral to positive effects, especially for hybrid work and narrowly defined individual tasks.

**Confidence:** Medium

**Why this confidence level**

The findings are consistent across S1 and S3, but the retrieved material reports the experiments second-hand rather than providing the primary papers, and S1 is an industry meta-analysis with some unverified numerical detail.

**Evidence**

- The reported 2015 Ctrip randomized experiment assigned 249 call-center employees to remote or office work and found remote workers completed 13.5% more calls, with gains attributed to more minutes worked and fewer environmental interruptions. [S1]
- The reported 2024 Trip.com randomized hybrid experiment assigned 1,612 employees to hybrid or fully office schedules and found no statistically significant differences in performance reviews, promotions, lines of code, or marketing revenue, while resignations fell by roughly one-third. [S1]
- The BLS review characterizes randomized experiments as finding small positive effects on individual productivity proxies and lower turnover, while cautioning that these metrics vary across studies. [S3]

#### Finding 3

**Claim**

Fully remote work can reduce output in some roles, particularly work requiring substantial collaboration or involving newly hired employees.

**Confidence:** Medium

**Why this confidence level**

The mechanism and direction are supported by multiple sources, but the specific 10–20% estimate comes only from S1's summary of a working paper.

**Evidence**

- S1 reports a 2023 working paper finding 10–20% output reductions for some fully remote roles, especially highly collaborative jobs and newly hired workers. [S1]
- The BLS synthesis notes that randomized studies tend to measure individual productivity proxies, while concerns about coordination and learning remain relevant limitations of remote work. [S3]
- Worklytics reports reduced cross-team interaction under fully remote work and identifies mentoring, brainstorming, knowledge sharing, and creative problem-solving as activities that may benefit from physical proximity. [S2]

#### Finding 4

**Claim**

Observational and survey evidence often reports stable or improving productivity, but it is vulnerable to perception, selection, and adaptation effects.

**Confidence:** Medium

**Why this confidence level**

The sources show a consistent pattern of positive perceptions after adaptation, but these are not equivalent to randomized causal estimates and may reflect who works remotely, how productivity is defined, or changes over time.

**Evidence**

- In repeated surveys, 70% of small-business owners initially reported a productivity dip in early 2020, but the median owner reported a positive effect by 2021 after firms adopted technology, training, altered tasks, and improved remote-management practices. [S5]
- A four-year Great Place To Work analysis reported stable or improved productivity after transition to remote work, using employee survey measures of effort and adaptability rather than direct output measures. [S4]
- Worklytics summarizes reported 5–15% gains in individual focus productivity, but its article also relies on self-reported productivity and analytics-oriented measures. [S2]

#### Finding 5

**Claim**

Company- and industry-level data suggest that remote work need not reduce productivity, but aggregate results are mixed and should not be interpreted as individual causal effects.

**Confidence:** Medium

**Why this confidence level**

The official BLS source provides useful large-scale evidence and explicitly presents both positive and near-zero aggregate findings. However, industry-level associations and selected-company comparisons do not establish that remote work caused the productivity outcomes.

**Evidence**

- BLS reports that, across 61 private-sector industries, growth in total factor productivity from 2019–21 and 2019–22 was positively associated with the increase in remote work after accounting for pre-pandemic productivity trends. [S3]
- The same BLS article cites a separate analysis across 43 industries finding little relationship between an industry's ability to work entirely remotely and labor-productivity growth. [S3]
- S4 reports that 97 of the 2025 Fortune 100 Best Companies supported remote or hybrid work and that their employees reported substantially higher productivity than employees in typical workplaces, but this is a selected high-performing-company sample. [S4]

#### Finding 6

**Claim**

Conflicting conclusions can arise because studies measure different outcomes and levels of analysis.

**Confidence:** High

**Why this confidence level**

The measurement differences are explicitly documented in the sources and directly explain why apparently opposing results may not be measuring the same construct.

**Evidence**

- The evidence spans call volume, performance reviews, promotions, lines of code, revenue, emails or calls, employee perceptions, total factor productivity, and labor productivity; these measures can capture different parts of work and may omit collaboration, innovation, learning, or quality. [S1] [S3] [S4] [S5]
- S1 reports positive effects for focused tasks but negative effects for collaborative tasks, while S3 distinguishes individual labor productivity from economy-wide or industry-level productivity. [S1] [S3]

#### Finding 7

**Claim**

Adaptation and organizational design can change the observed effect over time.

**Confidence:** Medium

**Why this confidence level**

The temporal shift and organizational mechanisms are supported by repeated surveys and the reported experiment, but the evidence does not isolate which adaptation caused the change.

**Evidence**

- S5 documents a shift from widespread perceived productivity declines early in the pandemic to positive median assessments by 2021, associated with technology investments, training, task changes, and better remote management. [S5]
- S1 reports that the hybrid experiment found equivalent output with lower attrition, suggesting that hybrid arrangements may produce organizational benefits even when individual productivity is unchanged. [S1]

### Conflicts Found

- The reported Ctrip experiment finds a 13.5% productivity increase under mostly fully remote work, whereas the reported later working paper finds 10–20% reductions for some fully remote roles. This is a conditional disagreement rather than a universal contradiction: the studies differ in worker type, task collaboration, hiring status, and possibly the remote arrangement and outcome measure. [S1]
- Industry-level evidence is mixed: BLS reports a positive association between increased remote work and total-factor-productivity growth across 61 industries, while it cites another 43-industry analysis finding little relationship with labor-productivity growth. [S3]
- Employee and business-owner surveys report stable or improved productivity after adaptation, while some pandemic-era single-firm case studies found short-run declines. Early disruption and later organizational learning may account for part of the difference. [S3] [S5]

### Important Gaps

- The primary experimental papers are not retrieved here, so the exact designs, confidence intervals, attrition, compliance, and outcome definitions cannot be independently assessed.
- How much of the observed remote-work effect reflects selection into remote-capable jobs or voluntary arrangements rather than location itself?
- Do remote-work effects on innovation, mentoring, skill acquisition, and long-run team performance differ from effects on short-run individual output?
- How generalizeable are call-center and Trip.com results to other occupations, countries, firm sizes, and fully remote versus hybrid arrangements?
- The retrieved sources do not provide a systematic quantitative comparison of controlled experiments, observational studies, and company-level data with harmonized effect sizes.

**Analysis Duration:** 20.54s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

A focused search for primary controlled-experiment evidence would materially improve the answer, especially by verifying the reported Ctrip and Trip.com results and clarifying the conditions under which fully remote work helps or hurts productivity.

**Next Search**

> primary randomized controlled trial remote work productivity Ctrip Trip.com hybrid Nature 2024 full text

---

# Iteration 2

## 1. Search

**Query**

> primary randomized controlled trial remote work productivity Ctrip Trip.com hybrid Nature 2024 full text

**Why this query**

A focused search for primary controlled-experiment evidence would materially improve the answer, especially by verifying the reported Ctrip and Trip.com results and clarifying the conditions under which fully remote work helps or hurts productivity.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S6 — 40+ remote work productivity statistics, trends & data for 2026**
  URL: https://www.worktime.com/blog/statistics/remote-work-productivity-statistics-trends-data
- **S7 — Does Working from Home Increase Productivity? (2026)**
  URL: https://emailanalytics.com/does-working-from-home-increase-productivity
- **S8 — Three-day hybrid work week is success, study published in Nature says**
  URL: https://www.cnbc.com/2024/06/14/three-day-hybrid-work-week-is-success-study-published-in-nature-says.html
- **S9 — Study finds hybrid work benefits companies and employees**
  URL: https://news.stanford.edu/stories/2024/06/hybrid-work-is-a-win-win-win-for-companies-workers

**Search Duration:** 2.37s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The strongest new evidence reinforces that hybrid work can preserve measured productivity while improving retention, rather than uniformly increasing output.

**Confidence:** High

**Why this confidence level**

The result is reported consistently by an institutional Stanford source and an independent news account, and it concerns a randomized experiment. However, the retrieved material is still a summary rather than the full primary paper.

**Evidence**

- Stanford’s account of the randomized Trip.com experiment reports that employees working from home two days per week were as productive and as likely to be promoted as fully office-based employees, while resignations fell by 33%. [S9]
- CNBC reports the same experiment involved 1,612 employees and found equal performance across creative and team-oriented functions, with non-manager attrition falling from 7.2% to 2.4%. [S8]

#### Finding 2

**Claim**

The new sources provide a clearer explanation for why positive results from the Ctrip experiment do not contradict negative estimates for some fully remote jobs: hybrid and fully remote arrangements are different treatments.

**Confidence:** High

**Why this confidence level**

The conditional distinction is directly stated in S9 and aligns with the previously accumulated experimental evidence.

**Evidence**

- Stanford explicitly distinguishes its hybrid experiment from earlier fully remote research, noting that prior studies often focused on workers not required to come to an office and on jobs such as customer support or data entry; it suggests fully remote problems may arise when arrangements are poorly managed. [S9]
- The accumulated evidence reports a 13.5% gain in a Ctrip call-center experiment but 10–20% reductions in some fully remote, highly collaborative or newly hired roles. [S1]

#### Finding 3

**Claim**

Survey and commercial summaries continue to indicate that many remote workers perceive higher productivity, but these claims are substantially weaker than causal experimental evidence.

**Confidence:** Low

**Why this confidence level**

These are commercial secondary sources, several figures are described without adequate methodological detail, and the outcomes are largely self-reported or based on proprietary analyses. They support perceptions and possible mechanisms, not a reliable causal estimate.

**Evidence**

- WorkTime reports that 77% of remote employees say they are more productive remotely and that 70% find focused work easier at home, while also describing fewer interruptions and reduced hours. [S6]
- EmailAnalytics reports survey- or analysis-based claims about productivity gains, lower stress, fewer distractions, and higher effort among remote workers. [S7]

#### Finding 4

**Claim**

Company- and industry-level evidence remains compatible with stable or higher aggregate productivity but cannot establish that remote work itself caused the result.

**Confidence:** Medium

**Why this confidence level**

The positive association is repeated, but the new source does not add independent primary evidence, and the previously documented conflicting aggregate analysis remains unresolved.

**Evidence**

- WorkTime repeats the BLS finding that a one-percentage-point increase in remote-work adoption was associated with a 0.08–0.09 percentage-point increase in total-factor-productivity growth across 61 industries. [S6]
- The accumulated BLS evidence also includes a separate 43-industry analysis finding little relationship between remote-work suitability and labor-productivity growth. [S3]

#### Finding 5

**Claim**

Different studies conflict partly because they measure different productivity concepts: short-run individual output, performance ratings and promotions, retention, perceived productivity, labor productivity, or total-factor productivity.

**Confidence:** High

**Why this confidence level**

The sources directly document heterogeneous outcome measures and levels of analysis, making apparent disagreement partly a comparison of non-equivalent outcomes.

**Evidence**

- The new sources describe outcomes including calls, performance, promotions, satisfaction, and resignations, while the accumulated evidence includes code, revenue, survey responses, labor productivity, and total-factor productivity. [S6] [S7] [S8] [S9] [S3]

### Conflicts Found

- The new commercial sources present predominantly positive claims, including large self-reported gains and broad statements that research consistently shows improved output, whereas the accumulated evidence remains mixed and includes neutral hybrid effects, negative effects in some fully remote collaborative roles, and near-zero industry-level relationships. [S6] [S7] [S1] [S3]
- S7 states that the Stanford/Ctrip study involved 16,000 call-center employees, while the accumulated state and S1 describe the randomized Ctrip experiment as involving 249 employees. The retrieved material therefore contains an unresolved discrepancy about the study’s sample and possibly conflates multiple phases or studies. [S7] [S1]

### Important Gaps

- The primary Ctrip and Trip.com papers are still not available in the retrieved evidence, so sample definitions, treatment compliance, confidence intervals, attrition, and exact productivity measures cannot be independently checked.
- Whether fully remote work affects long-run innovation, mentoring, learning, and team performance differently from short-run individual output remains unanswered.
- The commercial statistics in S6 and S7 do not provide enough methodological detail to determine sample selection, survey wording, dates, or whether reported figures are independent estimates.
- The discrepancy between S7’s 16,000-person description and S1’s 249-person description of the Ctrip evidence needs resolution before quoting the Ctrip estimate precisely.

**Analysis Duration:** 14.36s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

A focused search for the primary Ctrip experiment and its sample/design would materially improve the answer because one new source gives a potentially conflated sample size, and the current experimental evidence is largely reported second-hand. This is more important than collecting additional commercial summaries.

**Next Search**

> Ctrip working from home randomized experiment 2015 Bloom Liang Roberts Ying primary paper sample 249 16000

---

# Iteration 3

## 1. Search

**Query**

> Ctrip working from home randomized experiment 2015 Bloom Liang Roberts Ying primary paper sample 249 16000

**Why this query**

A focused search for the primary Ctrip experiment and its sample/design would materially improve the answer because one new source gives a potentially conflated sample size, and the current experimental evidence is largely reported second-hand. This is more important than collecting additional commercial summaries.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S10 — WFH - The Squawk Point**
  URL: https://www.squawkpoint.com/wp-content/uploads/2018/06/wfh.pdf
- **S11 — nber working paper series**
  URL: https://law.yale.edu/sites/default/files/area/workshop/leo/document/Roberts_DoesWorkingFromHomeWork.pdf
- **S12 — Does Working from Home Work? Evidence from a Chinese Experiment: Working Paper**
  URL: https://www.gsb.stanford.edu/faculty-research/working-papers/does-working-home-work-evidence-chinese-experiment
- **S13 — Evidence from a Chinese Experiment on Working from Home | NBER**
  URL: https://www.nber.org/digest/sep13/evidence-chinese-experiment-working-home
- **S14 — Does Working from Home Work? Evidence from a Chinese Experiment: Journal Article**
  URL: https://www.gsb.stanford.edu/faculty-research/publications/does-working-home-work-evidence-chinese-experiment

**Search Duration:** 2.32s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new primary-source records resolve the apparent sample-size discrepancy in the Ctrip evidence: the firm had 16,000 employees, but the randomized call-center experiment included 249 eligible volunteers.

**Confidence:** High

**Why this confidence level**

The sample distinction is explicitly reported by the NBER summary and is consistent with the primary-paper descriptions.

**Evidence**

- The NBER Digest states that 503 of 994 call-center employees volunteered and 249 met the experiment’s conditions; 131 were assigned to work from home and 118 to the office. [S13]
- The journal and working-paper abstracts describe Ctrip as a 16,000-employee firm, but identify the participants as volunteer call-center employees rather than the entire workforce. [S11] [S14]

#### Finding 2

**Claim**

The Ctrip randomized experiment found a positive short-run productivity effect for eligible call-center employees assigned to a mostly remote schedule.

**Confidence:** High

**Why this confidence level**

The result is documented in the peer-reviewed journal record and detailed by the NBER account, including treatment assignment and outcome components.

**Evidence**

- Over nine months, home workers increased measured performance by 13%; approximately 9% came from more minutes worked per shift and 4% from more calls per minute, with no measurable difference in call quality. [S13] [S14]
- The experiment randomly assigned eligible volunteers to home or office work, using birth-date parity for assignment, which supports causal interpretation within this selected population. [S13]

#### Finding 3

**Claim**

The Ctrip experiment also shows that remote work can affect retention and career outcomes differently: attrition fell, but promotion rates conditional on performance were lower for home workers.

**Confidence:** High

**Why this confidence level**

Both the NBER and Stanford publication summaries report the retention and promotion results, though the visibility explanation is presented as a possibility rather than a directly established mechanism.

**Evidence**

- Home workers’ attrition was about half that of office workers, while their promotion rate conditional on performance was almost 50% lower, plausibly reflecting reduced visibility to office-based managers. [S13] [S14]

#### Finding 4

**Claim**

The Ctrip follow-up suggests that selection and learning can change the apparent productivity effect after workers gain experience with the arrangement.

**Confidence:** Medium

**Why this confidence level**

The pattern is directly reported, but the post-experiment self-selection is no longer randomized, so the 22% figure should not be treated as a causal estimate of remote work.

**Evidence**

- After the firm expanded WFH and allowed experimental workers to choose, more than half switched arrangements and the reported productivity gain nearly doubled to 22%; the NBER account says many weaker performers at home returned to the office. [S13] [S14]

### Conflicts Found

- The new primary-source material does not support the prior characterization of the Ctrip trial as a 16,000-person experiment. It describes a 16,000-employee company whose randomized sample was 249 eligible volunteers. The earlier 16,000 figure likely referred to the firm, not the treatment sample. [S1] [S7] [S11] [S13] [S14]

### Important Gaps

- The Ctrip participants were volunteers with at least six months of tenure, broadband access, and an independent home workspace; how representative they are of other workers or newly hired employees remains uncertain.
- The sources provide summary results but not the full statistical tables, confidence intervals, detailed compliance information, or subgroup estimates needed to compare the effect precisely with other experiments.
- The new sources strengthen evidence for a causal positive effect in one call-center setting, but do not resolve whether fully remote work harms collaboration, mentoring, innovation, or long-run team productivity in other occupations.

**Analysis Duration:** 9.18s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The new primary and institutional sources materially improve the key experimental evidence and resolve the sample-size confusion. The broader question is already responsibly answerable: controlled evidence is positive or neutral in the studied settings, observational evidence is often positive but confounded, and company- or industry-level evidence is mixed and noncausal. Further searching could add detail but is not necessary to support the comparative conclusion.

**Stop Reason:** sufficient_evidence

---

# Final Research Decision

**Research Stopped Because**

The analyzer determined that the important parts of the question could be answered responsibly.

**Stop Reason:** sufficient_evidence

**Searches Performed:** 3

**Unique Sources:** 14

**Remaining Uncertainty**

- The full primary Trip.com paper and complete statistical tables were not retrieved, so confidence intervals, detailed compliance, and subgroup estimates cannot be independently assessed here.
- The Ctrip participants were volunteers with at least six months of tenure, broadband access, and an independent home workspace; their representativeness of other workers, newly hired employees, and other occupations is uncertain.
- The available evidence does not provide harmonized effect sizes comparing controlled experiments, observational studies, and company-level data using common productivity definitions.
- The evidence does not determine whether fully remote work has different long-run effects from hybrid work on innovation, mentoring, learning, and team productivity.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 7.24s |
| OpenAI Analysis | 3 | 44.08s |
| Report Generation | 1 | 24.43s |
| Total Run | — | 75.75s |
