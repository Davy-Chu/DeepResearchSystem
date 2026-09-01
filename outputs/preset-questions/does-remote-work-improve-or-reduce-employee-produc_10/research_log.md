# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 10 / 10

**Unique Sources:** 16

**OpenAI Calls:** 11

**Tavily Calls:** 10

**Started:** 2026-09-01T04:12:18-04:00

**Ended:** 2026-09-01T04:15:27-04:00

**Total Runtime:** 189.52s

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
- **S2 — The Rise of Remote Work: Evidence on Productivity and ...**
  URL: https://www.hbs.edu/ris/download.aspx?name=20-138.pdf
- **S3 — The rise in remote work since the pandemic and its impact ...**
  URL: https://www.bls.gov/opub/btn/volume-13/remote-work-productivity.htm
- **S4 — In-Office vs Remote Productivity: What the Data Shows | Worklytics**
  URL: https://www.worklytics.co/blog/in-office-vs-remote-day-productivity-which-is-better
- **S5 — Investigating the Role of Remote Working on Employees’ Performance and Well-Being: An Evidence-Based Systematic Review - PMC**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC9566387

**Search Duration:** 2.92s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Remote work does not have a uniform productivity effect; its impact varies by task, work arrangement, worker experience, and management context.

**Confidence:** High

**Why this confidence level**

This conditional conclusion is consistent across an official statistical review, a peer-reviewed systematic review, and a research synthesis, although the exact effect sizes are less secure.

**Evidence**

- The systematic review reports mixed consequences for employee performance and well-being and notes that remote-work terms cover different arrangements and proportions of time worked remotely. [S5]
- The BLS review states that effects depend on task type, technology, home environment, worker motivation, and management practices. [S3]
- The eMonitor synthesis reports positive effects for focused individual tasks but negative effects for some collaborative tasks and roles involving new hires or high collaboration. [S1]

#### Finding 2

**Claim**

The strongest controlled-experiment evidence suggests that hybrid work can maintain individual performance while improving retention, whereas fully remote work can improve measured output in some narrowly defined jobs.

**Confidence:** Medium

**Why this confidence level**

The direction of the experimental evidence is useful and partly corroborated by BLS, but the retrieved material gives the primary experiments only through secondary summaries rather than the original papers, and the settings are limited to particular firms and jobs.

**Evidence**

- The reported 2024 Trip.com randomized hybrid experiment found no statistically significant difference in performance reviews, promotions, coding output, or marketing revenue relative to five-day office work, while resignations fell by 33%. [S1]
- The reported 2015 Ctrip randomized experiment assigned 249 call-center employees to remote or office work and found 13.5% more calls among remote workers, attributed to fewer interruptions and more minutes worked. [S1]
- The BLS synthesis says randomized experiments at individual firms identify small positive effects of hybrid and fully remote work on individual productivity and lower turnover, while also noting that the measures are varied proxies. [S3]

#### Finding 3

**Claim**

Observational and survey evidence generally indicates that perceived productivity improved as firms adapted to remote work, but it also identifies persistent monitoring, training, and coordination problems.

**Confidence:** Medium

**Why this confidence level**

The sources directly describe survey and review findings, but perceptions and self-reports are weaker measures of output than experimentally recorded performance, and the systematic review covers heterogeneous studies.

**Evidence**

- Repeated surveys of U.S. small-business owners found that 70% perceived a productivity dip early in 2020, while the median owner reported a positive productivity effect by 2021. [S2]
- The same study attributes improvement partly to technology investment, training, changed task assignments, and better remote-team management; owners nevertheless reported difficulty monitoring remote workers and believed they were less able to learn new skills. [S2]
- The systematic review of 20 peer-reviewed papers found mixed effects on performance and well-being rather than a consistent productivity increase or decrease. [S5]

#### Finding 4

**Claim**

Company- and industry-level data give a more mixed picture than individual-level experiments: some aggregate analyses find a positive association with productivity growth, while others find little relationship.

**Confidence:** Medium

**Why this confidence level**

The official source clearly reports both aggregate results, but industry-level associations cannot by themselves establish that remote work caused productivity changes, and the results differ by measure and specification.

**Evidence**

- The BLS analysis of 61 private-sector industries reports that growth in total-factor productivity from 2019–21 and 2019–22 was positively associated with the increase in the share of remote workers, after accounting for pre-pandemic productivity trends. [S3]
- The same BLS article reports that another cross-industry analysis covering 43 industries found little relationship between an industry's ability to work entirely remotely and labor-productivity growth. [S3]
- The BLS source describes pandemic-era single-firm case studies in which productivity declined in the short run. [S3]

#### Finding 5

**Claim**

Different studies reach conflicting conclusions partly because they measure different outcomes and levels of analysis.

**Confidence:** High

**Why this confidence level**

The measurement and definition differences are explicitly documented across the retrieved sources and directly explain why results are not directly comparable.

**Evidence**

- The evidence uses calls, emails, hours, coding, revenue, manager ratings, performance reviews, turnover, total-factor productivity, and perceptions as productivity-related measures. [S1] [S2] [S3]
- BLS explicitly distinguishes individual labor productivity from aggregate economic performance and notes that studies use various proxies. [S3]
- The systematic review notes inconsistent terminology encompassing fully remote, hybrid, and other arrangements. [S5]

#### Finding 6

**Claim**

Selection and adaptation effects help explain why observational results may differ from randomized results or early pandemic estimates.

**Confidence:** High

**Why this confidence level**

The sources directly document nonrandom occupational selection, organizational adaptation, and narrow experimental populations.

**Evidence**

- Remote-work adoption tracks whether occupations are suitable for telework, so remote workers and firms are not a random sample of all workers and firms. [S2]
- Business owners' assessments changed from predominantly negative early in the pandemic to positive after investments, training, task redesign, and management learning. [S2]
- The reported randomized Ctrip experiment concerned a selected call-center population, while the hybrid experiment covered employees in one firm and included multiple role-specific outcomes. [S1]

### Conflicts Found

- Evidence differs on the aggregate productivity effect: BLS reports a positive association between increased remote work and TFP growth across 61 industries, whereas another 43-industry analysis found little relationship between remote-work feasibility and labor-productivity growth. [S3]
- Evidence differs by arrangement and task: the reported Ctrip experiment found higher output under mostly fully remote work for call-center employees, while the reported later evidence finds no performance gain or loss under hybrid work and a fully remote penalty for some collaborative or newly hired roles. [S1]
- Early and later employer perceptions conflict: 70% of small-business owners reported a productivity dip early in 2020, but the median owner reported a positive effect by 2021. [S2]
- Individual-level evidence is more favorable than some company-level or pandemic case-study evidence: randomized firm studies report small positive or neutral effects, while some single-firm pandemic studies report short-run declines and aggregate studies range from positive to null. [S1] [S3]

### Important Gaps

- The retrieved material does not provide the original experimental papers, so details such as confidence intervals, treatment compliance, subgroup effects, and the durability of the reported estimates cannot be independently assessed here.
- The evidence does not establish a general causal effect for fully remote work across industries; most controlled evidence concerns specific firms, occupations, or tasks.
- It remains unclear how much measured output gains reflect longer hours or fewer breaks rather than greater output per hour, especially in the reported Ctrip experiment.
- The sources provide limited direct evidence on innovation, mentoring, knowledge transfer, and long-run career development, despite identifying collaboration and learning as possible costs.
- The retrieved sources do not cleanly separate voluntary remote work from involuntary pandemic-era remote work in all observational comparisons.

**Analysis Duration:** 22.27s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The broad conclusion can be answered responsibly, but the central controlled-experiment comparison relies substantially on a commercial secondary summary. A focused search for the original randomized studies would materially improve causal interpretation and allow effect sizes and limitations to be checked directly.

**Next Search**

> original randomized controlled trial remote work productivity Ctrip Trip.com hybrid Nature 2024 full text

---

# Iteration 2

## 1. Search

**Query**

> original randomized controlled trial remote work productivity Ctrip Trip.com hybrid Nature 2024 full text

**Why this query**

The broad conclusion can be answered responsibly, but the central controlled-experiment comparison relies substantially on a commercial secondary summary. A focused search for the original randomized studies would materially improve causal interpretation and allow effect sizes and limitations to be checked directly.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S6 — Does Working from Home Increase Productivity? (2026)**
  URL: https://emailanalytics.com/does-working-from-home-increase-productivity
- **S7 — 40+ remote work productivity statistics, trends & data for 2026**
  URL: https://www.worktime.com/blog/statistics/remote-work-productivity-statistics-trends-data
- **S8 — Hybrid work is a “win-win-win” for companies, workers, study ...**
  URL: https://siepr.stanford.edu/news/hybrid-work-win-win-win-companies-workers-study-finds
- **S9 — Hybrid working from home improves retention without ... - PMC**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11208135

**Search Duration:** 2.77s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The strongest newly retrieved controlled evidence supports a neutral productivity effect for hybrid work, alongside substantially improved retention.

**Confidence:** High

**Why this confidence level**

The primary peer-reviewed trial and an institutional summary are consistent, and the trial includes randomized assignment, multiple years of performance reviews, and a large sample.

**Evidence**

- The primary Nature article reports a six-month randomized controlled trial of 1,612 employees at a Chinese technology company. Hybrid work improved job satisfaction, reduced quit rates by one-third, and did not affect performance grades over the following two years of reviews according to null-equivalence tests. [S9]
- The Stanford research summary reports that hybrid employees were just as productive and likely to be promoted as office-based employees, while resignations fell by 33%. [S8]

#### Finding 2

**Claim**

The new primary evidence does not establish that fully remote work has the same productivity effect as hybrid work.

**Confidence:** High

**Why this confidence level**

The scope of the primary experiment is explicit, and the source itself cautions against generalizing its findings to fully remote work.

**Evidence**

- The Nature trial studied employees working from home two days per week, not a fully remote arrangement. [S9]
- The Stanford summary explicitly distinguishes hybrid work from fully remote work and notes that fully remote studies, often involving customer support or data-entry jobs, have produced mixed and sometimes negative results. [S8]

#### Finding 3

**Claim**

The new source strengthens the explanation that study conclusions differ because remote-work arrangements and worker populations differ.

**Confidence:** High

**Why this confidence level**

The sources directly document differences in schedule, occupation, and worker population that limit direct comparison across studies.

**Evidence**

- The Trip.com experiment involved university-educated employees in engineering, marketing, accounting, and finance, using a two-days-at-home schedule. [S8] [S9]
- The Stanford summary contrasts this population and hybrid arrangement with earlier research focused on fully remote workers and narrower jobs such as customer support or data entry. [S8]
- Prior evidence also reports that effects vary by task, collaboration requirements, worker experience, and management context. [S1] [S3] [S5]

#### Finding 4

**Claim**

The randomized hybrid trial provides stronger causal evidence than the newly retrieved commercial summaries, while the latter should be treated mainly as secondary reports.

**Confidence:** High

**Why this confidence level**

The evidentiary distinction follows from the source types and the level of methodological detail provided in the retrieved content.

**Evidence**

- S9 identifies the study as a randomized controlled trial and reports its design, sample, outcomes, and statistical equivalence testing. [S9]
- S6 and S7 summarize research and present additional numerical claims, but they are commercial productivity/monitoring websites and the retrieved text does not document their methods or provide comparable primary-study detail. [S6] [S7]

#### Finding 5

**Claim**

The overall conclusion remains conditional: hybrid work appears capable of preserving measured individual performance, while the effect of fully remote work remains task- and context-dependent rather than universally positive or negative.

**Confidence:** High

**Why this confidence level**

The conclusion integrates consistent evidence on hybrid work with the previously documented heterogeneity of fully remote and observational results, without claiming a universal effect.

**Evidence**

- The randomized Trip.com evidence finds no performance penalty from hybrid work and a large retention benefit. [S9]
- The broader evidence base reports positive output effects in some narrowly defined fully remote jobs, mixed observational findings, and negative effects for some collaborative or newly hired roles. [S1] [S2] [S3] [S5]

### Conflicts Found

- S6 presents the evidence as showing consistent productivity gains from working at home, but the primary Nature trial in S9 finds no effect on performance under hybrid work, while the accumulated systematic review and BLS synthesis report mixed results. S6 is also internally inconsistent because it says studies disagree and later characterizes the gains as consistent. [S6] [S9] [S3] [S5]
- S7 uses the positive 61-industry BLS association to support a favorable conclusion, but the same accumulated BLS evidence includes a separate 43-industry analysis finding little relationship and warns that aggregate associations are not causal. [S7] [S3]
- The reported positive effect in the earlier Ctrip call-center experiment concerns a mostly or fully remote, narrowly defined call-center setting, whereas S9 finds a neutral performance effect for hybrid professional employees. This is a conditional disagreement by arrangement and occupation, not necessarily a direct contradiction. [S1] [S9]

### Important Gaps

- How large and durable are productivity effects of fully remote work outside call centers and other narrowly measurable occupations?
- To what extent did the Ctrip output gain reflect more minutes worked, fewer breaks, or higher productivity per hour?
- Do hybrid arrangements preserve innovation, mentoring, knowledge transfer, and career development over longer periods and across firms beyond Trip.com?
- How do voluntary choice, home working conditions, managerial practices, and coordination technology moderate the effects?
- The commercial sources S6 and S7 make many additional numerical claims, but their underlying samples, definitions, and methods are not available in the retrieved material.

**Analysis Duration:** 15.56s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new primary source substantially resolves the hybrid-work question but leaves the important fully remote causal question incompletely answered. A focused search for the original Ctrip experiment would materially improve comparison of fully remote evidence, especially by clarifying output-per-hour measures, treatment details, and external validity.

**Next Search**

> original Ctrip randomized experiment working from home productivity 13.5% calls output per hour Bloom Liang 2015 paper

---

# Iteration 3

## 1. Search

**Query**

> original Ctrip randomized experiment working from home productivity 13.5% calls output per hour Bloom Liang 2015 paper

**Why this query**

The new primary source substantially resolves the hybrid-work question but leaves the important fully remote causal question incompletely answered. A focused search for the original Ctrip experiment would materially improve comparison of fully remote evidence, especially by clarifying output-per-hour measures, treatment details, and external validity.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S10 — Evidence from a Chinese Experiment on Working from Home | NBER**
  URL: https://www.nber.org/digest/sep13/evidence-chinese-experiment-working-home
- **S11 — Does Working from Home Boost Productivity Growth?**
  URL: https://www.frbsf.org/research-and-insights/publications/economic-letter/2024/01/does-working-from-home-boost-productivity-growth
- **S12 — nber working paper series**
  URL: https://law.yale.edu/sites/default/files/area/workshop/leo/document/Roberts_DoesWorkingFromHomeWork.pdf
- **S13 — [PDF] DOES WORKING FROM HOME WORK? EVIDENCE FROM A ...**
  URL: https://enginyeriainformatica.cat/wp-content/uploads/2012/09/WFH.pdf
- **S14 — WFH - The Squawk Point**
  URL: https://www.squawkpoint.com/wp-content/uploads/2018/06/wfh.pdf

**Search Duration:** 2.60s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The CTrip randomized experiment provides strong causal evidence that mostly home-based work increased measured productivity in a narrowly defined call-center setting.

**Confidence:** High

**Why this confidence level**

The result is supported by the original working paper and the published QJE article text, with a randomized design and clearly described outcome measures. Generalizability remains limited.

**Evidence**

- Employees who volunteered and met eligibility conditions were randomly assigned to work from home four days per week or remain in the call center for nine months. The working-from-home group increased performance by 13%, with no measurable decline in call quality. [S10] [S12] [S14]
- Approximately 9 percentage points of the gain came from more minutes worked per shift, due to fewer breaks and sick days, while roughly 4 percentage points came from more calls per minute, which workers attributed to a quieter home environment. [S10] [S12] [S14]

#### Finding 2

**Claim**

The CTrip productivity gain was driven substantially by more time worked rather than solely by higher output per hour.

**Confidence:** High

**Why this confidence level**

Multiple versions of the experiment report the same decomposition. The evidence does not establish whether working longer was welfare-improving or whether it reflected pressure, altered breaks, or reduced absence.

**Evidence**

- The NBER account attributes 9.2% of the 13% performance increase to increased minutes worked, including fewer breaks and sick days; calls per minute increased by 3.3%. [S10]
- The working paper decomposes the gain similarly, reporting about 9% from more minutes per shift and about 4% from more calls per minute. [S12] [S14]

#### Finding 3

**Claim**

The CTrip experiment also illustrates that selection and worker choice can change estimated productivity effects after an organization adopts remote work.

**Confidence:** High

**Why this confidence level**

The sources directly describe the post-experiment re-selection and its association with a larger gain. The post-trial comparison is no longer randomized, so it should not be interpreted as a second causal estimate equivalent to the original experiment.

**Evidence**

- After the trial, employees could choose home or office work; more than half switched locations, and the reported productivity gain nearly doubled to about 22%. The source attributes this partly to learning and selection effects, including relatively weaker performers leaving the home-work arrangement. [S10] [S12] [S14]

#### Finding 4

**Claim**

The CTrip results do not contradict the later Trip.com hybrid experiment; they concern different arrangements and populations.

**Confidence:** High

**Why this confidence level**

The differences in schedule, occupation, and outcome measurement are explicit. They provide a plausible conditional explanation rather than evidence of a direct contradiction.

**Evidence**

- CTrip employees worked from home four days per week and were call-center workers with highly measurable output, whereas the later Trip.com trial involved professional employees working from home two days per week. [S10] [S12] [S14] [S8] [S9]
- CTrip found higher call-center performance, while the later randomized hybrid trial found no meaningful performance difference but substantially lower quits. [S9]

#### Finding 5

**Claim**

Industry-level evidence from the Federal Reserve Bank of San Francisco finds little evidence that teleworkability substantially changed productivity growth during the pandemic.

**Confidence:** Medium

**Why this confidence level**

This is a careful official industry-level analysis, but teleworkability is an indirect exposure measure and the design remains observational rather than randomized.

**Evidence**

- An analysis of 43 U.S. industries measured output per hour and found little statistical relationship between industry teleworkability and pandemic productivity performance after controlling for pre-pandemic trends. [S11]
- The authors conclude that remote work was unlikely to have been a major factor either boosting or holding back aggregate productivity growth through early 2023. [S11]

#### Finding 6

**Claim**

The new aggregate evidence strengthens the conclusion that company- and industry-level data are mixed and generally weaker for identifying causality than controlled experiments.

**Confidence:** High

**Why this confidence level**

The sources consistently show differing aggregate estimates and explicitly identify confounding factors. The disagreement is about aggregate associations and specifications, not necessarily about the causal effects found in firm-level experiments.

**Evidence**

- S11 reports a near-null industry relationship, while the accumulated BLS analysis reports a positive association in one 61-industry specification and little relationship in another 43-industry analysis; BLS also notes that aggregate associations are not causal. [S3] [S11]
- The industry analysis notes that aggregate productivity reflects other factors, including economic cycles, supply disruptions, social-distancing constraints, and differences in which tasks can be performed remotely. [S11]

#### Finding 7

**Claim**

Different studies reach conflicting conclusions because remote work is not one treatment: effects vary with intensity, task measurability, worker selection, voluntary versus forced adoption, and organizational adaptation.

**Confidence:** High

**Why this confidence level**

The explanation is supported by both direct contrasts across studies and explicit discussion of mechanisms and moderators in official and review sources.

**Evidence**

- CTrip's voluntary, mostly remote call-center experiment produced a positive output effect, while the Trip.com randomized hybrid trial found performance equivalence and the industry-level pandemic analysis found little aggregate effect. [S10] [S12] [S14] [S9] [S11]
- The San Francisco Fed notes that remote work can reduce disruptions and commuting costs but can also hinder idea sharing, learning, and coordination; net effects may change as firms and workers adapt. [S11]
- The accumulated review and BLS evidence similarly identify task type, technology, home environment, worker experience, and management practices as moderators. [S1] [S3] [S5]

### Conflicts Found

- The new FRBSF industry analysis finds little relationship between teleworkability and productivity growth, whereas the accumulated BLS analysis reports a positive association in a separate 61-industry specification. These are conditional differences in sample, period, productivity measure, and specification, not cleanly comparable causal estimates. [S3] [S11]
- CTrip reports a 13% productivity increase under four-days-per-week home work for call-center employees, while the Trip.com randomized hybrid trial reports no performance effect. The apparent disagreement is conditional on occupation and work arrangement. [S10] [S12] [S14] [S9]
- CTrip's post-trial 22% gain after employees reselected their work location is larger than the randomized 13% gain, but the post-trial estimate is subject to self-selection and should not be treated as equally causal. [S10] [S12] [S14]

### Important Gaps

- How large is the causal productivity effect of fully remote work outside call centers and other jobs with easily measured output?
- Do remote-work output gains reflect higher productivity per hour, longer effective working time, or both, and how do those changes affect employee welfare?
- What are the long-run effects on innovation, mentoring, knowledge transfer, promotion, and career development?
- How much do voluntary choice, home working conditions, management quality, and coordination technology moderate the effects?
- Why do industry-level specifications differ between the positive BLS association and the near-null FRBSF result, beyond their documented differences in samples and measures?

**Analysis Duration:** 18.49s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The evidence now supports a responsible comparison across controlled experiments, observational studies, and company/industry data. It consistently supports a conditional conclusion rather than a universal productivity effect: hybrid work can preserve measured performance, mostly remote work can raise output in selected call-center settings, and aggregate effects appear small or mixed. Further research could improve estimates for fully remote professional work and long-run organizational outcomes, but it is not necessary to answer the original question responsibly.

**Next Search**

> Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions. additional evidence search 4

---

# Iteration 4

## 1. Search

**Query**

> Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions. additional evidence search 4

**Why this query**

The evidence now supports a responsible comparison across controlled experiments, observational studies, and company/industry data. It consistently supports a conditional conclusion rather than a universal productivity effect: hybrid work can preserve measured performance, mostly remote work can raise output in selected call-center settings, and aggregate effects appear small or mixed. Further research could improve estimates for fully remote professional work and long-run organizational outcomes, but it is not necessary to answer the original question responsibly.

**Results**

5 results retrieved.

1 new unique source added.

### Sources

- **S15 — Remote Work Productivity Study: Surprising Findings From ...**
  URL: https://www.greatplacetowork.com/resources/blog/remote-work-productivity-study-finds-surprising-reality-2-year-study

**Search Duration:** 2.65s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new source reports positive productivity-related employee sentiment in remote-capable and high-trust workplaces, but it does not provide strong causal evidence that remote work itself increases productivity.

**Confidence:** Medium

**Why this confidence level**

The sample sizes are large, but the retrieved material does not describe the sampling, comparison group, statistical controls, or whether productivity was objectively measured. The source is also produced by an organization promoting workplace certification and rankings.

**Evidence**

- Great Place To Work says its 2022 study of more than 800,000 employees found stable or improved productivity after transition to remote work, based on survey responses about discretionary effort and adaptability rather than directly measured output. [S15]
- Its 2024 analysis of 1.3 million employees associates cooperation with discretionary effort, and its Fortune 100 Best Companies comparison reports higher productivity at firms where remote or hybrid work is widely supported. [S15]

#### Finding 2

**Claim**

S15 is consistent with the broader finding that organizational culture, trust, cooperation, and leadership may moderate remote-work outcomes.

**Confidence:** Medium

**Why this confidence level**

The moderator claim is coherent across sources, but S15 presents associations and organizational survey findings rather than an experimental test of these mechanisms.

**Evidence**

- The source states that cooperation is strongly associated with employees giving extra effort and emphasizes trust and leadership as conditions for sustaining performance remotely. [S15]
- Existing evidence likewise identifies management practices, technology, worker motivation, task type, and coordination as moderators of remote-work productivity. [S1] [S3] [S5]

#### Finding 3

**Claim**

The source illustrates why survey-based company comparisons can appear more favorable than causal studies: high-performing firms and engaged employees may be selected into the comparison, and the measures capture attitudes or effort rather than output per hour.

**Confidence:** High

**Why this confidence level**

The source explicitly describes its survey measures and comparison structure, and the contrast with the outcome measures in the experimental evidence is clear.

**Evidence**

- S15 compares Fortune 100 Best Companies with typical workplaces and reports substantially higher productivity alongside higher cooperation and psychological health; it does not establish that remote work caused those differences. [S15]
- The article measures productivity-related outcomes using employee statements about extra effort and adaptability, while the controlled studies use calls, performance reviews, coding output, revenue, or other operational measures. [S15] [S1] [S9] [S10]

#### Finding 4

**Claim**

S15 adds limited evidence about well-being: it reports higher engagement among fully remote workers but also lower well-being and more stress, anger, and loneliness, reinforcing that productivity and employee welfare are distinct outcomes.

**Confidence:** Low

**Why this confidence level**

These figures are reported secondhand in the retrieved article, and the underlying Gallup methods and causal interpretation are not available here.

**Evidence**

- The article reports Gallup figures showing fully remote workers with higher engagement than hybrid or on-site workers, while also reporting worse well-being indicators. [S15]

### Conflicts Found

- S15 presents remote environments and high-performing remote-supporting companies in strongly favorable terms, whereas the randomized Trip.com trial found productivity equivalence rather than an increase under hybrid work. This is likely a difference between survey associations and causal performance estimates, not a clean contradiction. [S15] [S9]
- S15's positive survey findings contrast with the broader systematic review and official syntheses reporting mixed effects, including problems for collaboration, monitoring, learning, and some roles. The disagreement may reflect different populations, definitions, and outcome measures. [S15] [S1] [S3] [S5]

### Important Gaps

- What was the design and response rate of the 800,000-employee study, and did it include a comparable office-based control group?
- Were the reported productivity improvements based on within-worker changes, employer assessments, or selected high-performing organizations?
- How much of the Fortune 100 productivity difference is attributable to remote work rather than industry composition, selection, pay, management quality, or preexisting organizational performance?
- Are the engagement and well-being figures independently measured and adjusted for worker and occupation differences?

**Analysis Duration:** 13.09s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new source does not materially resolve the key unanswered causal question. It adds a large but weakly documented survey and organizational-association perspective, while the existing evidence already adequately supports the conditional conclusion: hybrid work can preserve measured performance, fully remote effects vary by job and context, and aggregate or survey associations are not causal. Further research would be useful for long-run innovation and fully remote causal effects, but another search is not necessary to answer the original question responsibly.

**Next Search**

> Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions. additional evidence search 5

---

# Iteration 5

## 1. Search

**Query**

> Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions. additional evidence search 5

**Why this query**

The new source does not materially resolve the key unanswered causal question. It adds a large but weakly documented survey and organizational-association perspective, while the existing evidence already adequately supports the conditional conclusion: hybrid work can preserve measured performance, fully remote effects vary by job and context, and aggregate or survey associations are not causal. Further research would be useful for long-run innovation and fully remote causal effects, but another search is not necessary to answer the original question responsibly.

**Results**

5 results retrieved.

1 new unique source added.

### Sources

- **S16 — Work from home and employee well-being: a double-edged sword**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12333122

**Search Duration:** 3.17s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

S16 does not materially add evidence about whether remote work improves or reduces employee productivity.

**Confidence:** High

**Why this confidence level**

The provided source content does not report productivity findings or empirical results that can be evaluated.

**Evidence**

- The retrieved content identifies a 2025 BMC Psychology article focused on employee well-being, but the available excerpt contains bibliographic information and article metadata rather than its results, productivity measures, sample, or estimated effects. [S16]

#### Finding 2

**Claim**

The accumulated evidence supports a conditional rather than universal conclusion: hybrid work can preserve measured individual performance, while fully remote work has effects that vary substantially by occupation, task, intensity, and management context.

**Confidence:** High

**Why this confidence level**

The conclusion is supported by a primary randomized hybrid trial, the original CTrip experiment reports, and multiple broader syntheses. Generalization to all fully remote work remains limited.

**Evidence**

- The randomized Trip.com trial found no performance penalty under a two-days-per-week hybrid schedule and substantially lower quits among participating employees. [S9]
- The randomized CTrip call-center experiment found a 13% performance increase under working from home four days per week, with much of the gain attributable to more minutes worked and the remainder to more calls per minute. [S10] [S12] [S14]
- Reviews and official syntheses report positive effects for some focused, measurable tasks but mixed or negative effects for some collaborative, learning-intensive, or newly hired roles. [S1] [S3] [S5]

#### Finding 3

**Claim**

Company- and industry-level data do not establish a consistent aggregate productivity effect of remote work.

**Confidence:** High

**Why this confidence level**

The sources directly document both positive and near-null aggregate results and explain why those estimates are not clean causal tests.

**Evidence**

- A BLS analysis found a positive association between growth in remote work and total-factor productivity in one 61-industry specification, but also reported little relationship in a separate 43-industry analysis. [S3]
- The Federal Reserve Bank of San Francisco analysis of 43 industries found little statistical relationship between teleworkability and pandemic productivity growth after accounting for pre-pandemic trends. [S11]
- These aggregate analyses are observational and can be affected by industry composition, economic conditions, supply disruptions, task differences, and other concurrent pandemic factors. [S3] [S11]

#### Finding 4

**Claim**

Conflicting findings are largely explained by differences in the treatment being studied and in the outcomes measured, rather than by a single unresolved contradiction.

**Confidence:** High

**Why this confidence level**

Measurement, selection, arrangement, and adaptation differences are explicitly documented across the evidence base and directly account for much of the apparent disagreement.

**Evidence**

- Studies compare fully or mostly remote work with hybrid work, use different schedules, and examine different populations, including highly measurable call-center work versus professional engineering, marketing, accounting, and finance roles. [S8] [S9] [S10] [S12] [S14]
- Reported outcomes include calls, calls per minute, hours or minutes worked, coding, revenue, performance reviews, promotions, turnover, survey perceptions, labor productivity, and total-factor productivity. [S1] [S2] [S3] [S9] [S10] [S15]
- Remote workers and adopting firms are selected rather than randomly drawn in observational studies, while organizational adaptation, technology, training, task redesign, and management learning can change effects over time. [S2] [S3] [S11]

### Conflicts Found

- The CTrip randomized experiment found higher measured output under mostly home-based work, whereas the Trip.com randomized hybrid trial found performance equivalence. This is a conditional disagreement involving different occupations, schedules, and outcome measures rather than a direct test of the same treatment. [S9] [S10] [S12] [S14]
- Aggregate evidence ranges from a positive remote-work/productivity association in one BLS specification to a near-null relationship in the FRBSF analysis and another BLS specification. These results differ in samples, periods, measures, and specifications and remain observational. [S3] [S11]
- Employer perceptions shifted from predominantly negative early-pandemic assessments to more positive assessments after adaptation, illustrating that timing and organizational learning can change observed results. [S2]

### Important Gaps

- The evidence still does not identify a general causal effect of fully remote work across occupations and industries outside narrowly measurable jobs.
- It remains unclear how much output gains in the CTrip experiment reflect higher productivity per hour versus longer effective working time, fewer breaks, and fewer absences, and what those changes imply for employee welfare.
- Long-run effects on innovation, mentoring, knowledge transfer, promotion, and career development remain insufficiently measured.
- The relative importance of voluntary choice, home working conditions, management quality, collaboration technology, and worker experience remains uncertain.
- S16 may contain relevant well-being evidence, but the supplied excerpt does not provide its methods or results.

**Analysis Duration:** 12.30s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The important parts of the original question can be answered responsibly with the current evidence: controlled experiments show conditional positive or neutral effects, observational and survey studies are mixed and vulnerable to selection, and company- or industry-level data are inconsistent and non-causal. S16 does not supply usable productivity results, and another search is not necessary unless the goal is specifically to investigate long-run well-being or fully remote effects outside the studied occupations.

**Next Search**

> Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions. additional evidence search 6

---

# Iteration 6

## 1. Search

**Query**

> Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions. additional evidence search 6

**Why this query**

The important parts of the original question can be answered responsibly with the current evidence: controlled experiments show conditional positive or neutral effects, observational and survey studies are mixed and vulnerable to selection, and company- or industry-level data are inconsistent and non-causal. S16 does not supply usable productivity results, and another search is not necessary unless the goal is specifically to investigate long-run well-being or fully remote effects outside the studied occupations.

**Results**

5 results retrieved.

0 new unique sources added.

### Sources

No new unique sources were added.

**Search Duration:** 3.19s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Remote work has no universal productivity effect; results depend on whether work is hybrid or fully remote, the occupation and task, worker selection, and management context.

**Confidence:** High

**Why this confidence level**

This conditional pattern is consistently documented across randomized studies, official analyses, and reviews.

**Evidence**

- Reviews and official syntheses report positive effects for focused, measurable tasks but mixed or negative effects for collaborative, learning-intensive, or newly hired roles. [S1] [S3] [S5]
- The evidence compares different schedules and populations, including mostly remote call-center work and hybrid professional roles. [S8] [S9] [S10] [S12] [S14]

#### Finding 2

**Claim**

Controlled experiments provide the clearest evidence: mostly remote work increased measured output in a narrowly defined call-center experiment, while hybrid work preserved performance and reduced turnover in a larger professional workforce experiment.

**Confidence:** High

**Why this confidence level**

Both findings come from randomized experiments, including the primary Nature trial and original CTrip study reports, though their generalizability is limited by firm, occupation, and arrangement.

**Evidence**

- The CTrip randomized experiment found about a 13% performance increase for employees working from home four days per week; approximately 9 percentage points came from more minutes worked and about 4 percentage points from more calls per minute, with no measurable decline in call quality. [S10] [S12] [S14]
- The Trip.com randomized trial of 1,612 employees working from home two days per week found no meaningful effect on performance reviews, promotions, coding output, or marketing revenue, while resignations fell by about one-third. [S8] [S9]

#### Finding 3

**Claim**

The CTrip result should not be interpreted as evidence that fully remote work generally improves productivity.

**Confidence:** High

**Why this confidence level**

The differences in treatment, population, and outcome measurement are explicit.

**Evidence**

- CTrip studied volunteers in a highly measurable call-center setting and used a four-days-at-home schedule; much of the measured gain reflected more time worked rather than purely higher hourly productivity. [S10] [S12] [S14]
- The later randomized trial studied university-educated professional employees under a two-days-at-home hybrid schedule, not fully remote work. [S8] [S9]

#### Finding 4

**Claim**

Observational and survey evidence is mixed and is weaker for causal inference than the experiments.

**Confidence:** Medium

**Why this confidence level**

These sources are useful for perceptions and mechanisms, but self-reports, selection, and heterogeneous designs limit causal conclusions.

**Evidence**

- Small-business owners initially reported productivity declines early in 2020, but assessments became more positive by 2021 after technology investment, training, task redesign, and management adaptation. [S2]
- A systematic review of 20 peer-reviewed studies found mixed effects on performance and well-being rather than a consistent increase or decrease. [S5]
- Survey-based company comparisons report favorable productivity-related attitudes in remote-supporting organizations, but measure perceived effort and adaptability rather than directly measured output and lack a clear causal control group. [S15]

#### Finding 5

**Claim**

Company- and industry-level data do not establish a consistent aggregate productivity effect.

**Confidence:** High

**Why this confidence level**

The official sources directly report positive and near-null estimates and explain why they are not clean causal tests.

**Evidence**

- One BLS specification found a positive association between increased remote work and total-factor productivity growth across 61 industries, while another BLS analysis and a Federal Reserve Bank of San Francisco analysis of 43 industries found little relationship. [S3] [S11]
- The industry analyses are observational and may reflect economic cycles, supply disruptions, industry composition, task differences, and other pandemic-era factors. [S3] [S11]

#### Finding 6

**Claim**

Apparent conflicts largely arise because studies examine different treatments, outcomes, populations, and time periods rather than the identical remote-work intervention.

**Confidence:** High

**Why this confidence level**

Measurement, selection, adaptation, and mechanism differences are explicitly documented and provide a coherent explanation for divergent estimates.

**Evidence**

- Outcomes range from calls and calls per minute to hours worked, coding, revenue, performance reviews, promotions, turnover, survey perceptions, labor productivity, and total-factor productivity. [S1] [S2] [S3] [S9] [S10] [S15]
- Remote-work adoption is nonrandom, and organizational learning, technology, training, task redesign, and management changes can alter effects over time. [S2] [S3] [S11]
- Remote work may reduce interruptions and commuting costs while impairing coordination, idea sharing, mentoring, and learning; the balance varies by job and arrangement. [S1] [S3] [S5] [S11]

### Conflicts Found

- The CTrip randomized experiment found higher measured output under mostly remote work, whereas the Trip.com randomized hybrid trial found performance equivalence. This is a conditional disagreement involving different occupations, schedules, and metrics, not a direct contradiction. [S9] [S10] [S12] [S14]
- Aggregate estimates range from a positive BLS association to near-null BLS and FRBSF estimates. Differences in samples, periods, measures, and specifications—as well as observational confounding—limit direct comparison. [S3] [S11]
- Employer perceptions shifted from predominantly negative early-pandemic assessments to more positive assessments after adaptation, indicating that timing and organizational learning affect results. [S2]
- Positive survey-based company comparisons conflict with mixed reviews and neutral experimental performance estimates, likely because surveys capture perceptions and selected organizations rather than causal output changes. [S15] [S3] [S5] [S9]

### Important Gaps

- The evidence does not identify a general causal effect of fully remote work across occupations and industries outside narrowly measurable jobs.
- It remains unclear how much output gains in the CTrip experiment reflect higher productivity per hour versus longer effective working time, fewer breaks, and fewer absences, and what this implies for employee welfare.
- Long-run effects on innovation, mentoring, knowledge transfer, promotion, and career development remain insufficiently measured.
- The relative importance of voluntary choice, home conditions, management quality, collaboration technology, and worker experience remains uncertain.
- The retrieved material does not provide all original experimental details, such as confidence intervals, compliance, and subgroup effects.

**Analysis Duration:** 14.64s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The accumulated evidence is sufficient to answer the original comparison responsibly: controlled experiments show conditional positive or neutral effects, observational evidence is mixed and selection-prone, and aggregate data are inconsistent and noncausal. Further research could refine generalizability and long-run mechanisms but is not necessary for the main conclusion.

**Next Search**

> Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions. additional evidence search 7

---

# Iteration 7

## 1. Search

**Query**

> Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions. additional evidence search 7

**Why this query**

The accumulated evidence is sufficient to answer the original comparison responsibly: controlled experiments show conditional positive or neutral effects, observational evidence is mixed and selection-prone, and aggregate data are inconsistent and noncausal. Further research could refine generalizability and long-run mechanisms but is not necessary for the main conclusion.

**Results**

5 results retrieved.

0 new unique sources added.

### Sources

No new unique sources were added.

**Search Duration:** 3.15s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Remote work has no universal productivity effect; the best-supported conclusion is conditional on work arrangement, occupation, task, and management context.

**Confidence:** High

**Why this confidence level**

This pattern is consistent across randomized experiments, official analyses, and systematic reviews.

**Evidence**

- Reviews and official syntheses report positive effects for focused, measurable tasks but mixed or negative effects for collaborative, learning-intensive, or newly hired roles. [S1] [S3] [S5]
- The evidence compares mostly remote call-center work with hybrid professional roles, rather than one identical intervention. [S8] [S9] [S10] [S12] [S14]

#### Finding 2

**Claim**

Controlled experiments provide the clearest evidence, but they produce different results because they study different arrangements and populations.

**Confidence:** High

**Why this confidence level**

Both results come from randomized experiments, including primary or original study reports, though external validity is limited by firm, occupation, schedule, and outcome measure.

**Evidence**

- The randomized CTrip experiment found about a 13% increase in measured call-center performance when employees worked from home four days per week; about 9 percentage points came from more minutes worked and about 4 percentage points from more calls per minute, with no measurable decline in call quality. [S10] [S12] [S14]
- The randomized Trip.com trial of 1,612 professional employees working from home two days per week found no meaningful effect on performance reviews, promotions, coding output, or marketing revenue, while resignations fell by about one-third. [S8] [S9]

#### Finding 3

**Claim**

The CTrip productivity increase should not be interpreted as evidence that fully remote work generally improves productivity.

**Confidence:** High

**Why this confidence level**

The treatment, population, and measurement differences are explicit.

**Evidence**

- CTrip involved volunteers in a highly measurable call-center setting and used a four-days-at-home schedule; much of the gain reflected more time worked rather than solely higher hourly productivity. [S10] [S12] [S14]
- The later randomized trial studied university-educated professional employees under a two-days-at-home hybrid schedule, not fully remote work. [S8] [S9]

#### Finding 4

**Claim**

Observational and survey evidence is mixed and weaker for causal inference than the experiments.

**Confidence:** Medium

**Why this confidence level**

These sources provide useful evidence about perceptions and mechanisms, but self-reports, selection, and heterogeneous designs limit causal conclusions.

**Evidence**

- Small-business owners initially reported productivity declines early in 2020, but assessments became more positive by 2021 after technology investment, training, task redesign, and management adaptation. [S2]
- A systematic review of 20 peer-reviewed studies found mixed effects on performance and well-being. [S5]
- Survey-based company comparisons report favorable productivity-related attitudes in remote-supporting organizations, but measure perceived effort and adaptability rather than directly measured output and lack a clear causal control group. [S15]

#### Finding 5

**Claim**

Company- and industry-level data do not establish a consistent aggregate productivity effect.

**Confidence:** High

**Why this confidence level**

Official sources directly report positive and near-null estimates and explain why they are not clean causal tests.

**Evidence**

- One BLS specification found a positive association between increased remote work and total-factor productivity growth across 61 industries, while another BLS analysis and the FRBSF analysis of 43 industries found little relationship. [S3] [S11]
- These analyses are observational and may reflect economic cycles, supply disruptions, industry composition, task differences, and other pandemic-era factors. [S3] [S11]

#### Finding 6

**Claim**

Conflicting findings largely reflect differences in the treatment, outcomes, populations, and timing studied rather than one simple contradiction.

**Confidence:** High

**Why this confidence level**

Measurement, selection, adaptation, and mechanism differences are explicitly documented across the evidence base and coherently explain the divergent results.

**Evidence**

- Studies examine fully or mostly remote work versus hybrid work, with different schedules and populations, including measurable call-center work and professional engineering, marketing, accounting, and finance roles. [S8] [S9] [S10] [S12] [S14]
- Outcomes range from calls, calls per minute, and minutes worked to coding, revenue, performance reviews, promotions, turnover, survey perceptions, labor productivity, and total-factor productivity. [S1] [S2] [S3] [S9] [S10] [S15]
- Remote-work adoption is nonrandom, while organizational learning, technology, training, task redesign, and management changes can alter effects over time. [S2] [S3] [S11]
- Remote work may reduce interruptions and commuting costs but impair coordination, idea sharing, mentoring, and learning; the balance varies by job and arrangement. [S1] [S3] [S5] [S11]

### Conflicts Found

- CTrip found higher measured output under mostly remote work, while Trip.com found performance equivalence under hybrid work. This is a conditional disagreement involving different occupations, schedules, and metrics, not a direct test of the same treatment. [S9] [S10] [S12] [S14]
- Aggregate estimates range from a positive BLS association to near-null BLS and FRBSF estimates. Differences in samples, periods, measures, specifications, and observational confounding limit direct comparison. [S3] [S11]
- Employer perceptions shifted from predominantly negative early-pandemic assessments to more positive assessments after adaptation, indicating that timing and organizational learning affect results. [S2]
- Positive survey-based company comparisons contrast with mixed reviews and neutral experimental performance estimates, likely because surveys capture perceptions and selected organizations rather than causal output changes. [S15] [S3] [S5] [S9]

### Important Gaps

- The evidence does not identify a general causal effect of fully remote work across occupations and industries outside narrowly measurable jobs.
- It remains unclear how much CTrip's output gain reflected higher productivity per hour versus longer effective working time, fewer breaks, and fewer absences, and what this implies for employee welfare.
- Long-run effects on innovation, mentoring, knowledge transfer, promotion, and career development remain insufficiently measured.
- The relative importance of voluntary choice, home conditions, management quality, collaboration technology, and worker experience remains uncertain.
- The retrieved material does not provide all original experimental details, such as confidence intervals, compliance, and subgroup effects.

**Analysis Duration:** 11.88s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

No usable new sources were retrieved, and the accumulated evidence is sufficient to answer the original question responsibly. Further searching could add detail, but it is unlikely to change the central conclusion: hybrid work can preserve measured individual performance, fully remote effects are context-dependent, and aggregate evidence is mixed and noncausal.

**Next Search**

> Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions. additional evidence search 8

---

# Iteration 8

## 1. Search

**Query**

> Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions. additional evidence search 8

**Why this query**

No usable new sources were retrieved, and the accumulated evidence is sufficient to answer the original question responsibly. Further searching could add detail, but it is unlikely to change the central conclusion: hybrid work can preserve measured individual performance, fully remote effects are context-dependent, and aggregate evidence is mixed and noncausal.

**Results**

5 results retrieved.

0 new unique sources added.

### Sources

No new unique sources were added.

**Search Duration:** 2.42s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The accumulated evidence supports a conditional conclusion, not a universal productivity effect: hybrid work can preserve measured individual performance, while fully or mostly remote work ranges from positive to negative depending on occupation, task, intensity, and management context.

**Confidence:** High

**Why this confidence level**

The pattern is supported by two randomized experiments plus broader reviews and official analyses, although generalization beyond the studied firms and occupations remains limited.

**Evidence**

- The randomized Trip.com trial found no meaningful performance penalty under a two-days-per-week hybrid schedule and reduced resignations by about one-third. [S8] [S9]
- The randomized CTrip experiment found about a 13% increase in measured call-center performance under four-days-per-week home work, with much of the gain attributable to more minutes worked. [S10] [S12] [S14]
- Reviews and official syntheses report positive effects for focused, measurable tasks but mixed or negative effects for collaborative, learning-intensive, or newly hired roles. [S1] [S3] [S5]

#### Finding 2

**Claim**

Controlled experiments provide the strongest causal evidence, but their differing results are conditional rather than directly contradictory.

**Confidence:** High

**Why this confidence level**

Both findings derive from randomized designs, but the interventions, populations, work tasks, and outcome measures differ substantially.

**Evidence**

- CTrip studied volunteers in a highly measurable call-center setting, with employees working from home four days per week; output rose about 13% and call quality did not measurably decline. [S10] [S12] [S14]
- Trip.com's randomized trial studied 1,612 professional employees working from home two days per week and found no meaningful effect on reviews, promotions, coding output, or marketing revenue. [S8] [S9]

#### Finding 3

**Claim**

The CTrip output gain partly reflected more effective time worked, so it should not be interpreted simply as a rise in hourly productivity or employee welfare.

**Confidence:** High

**Why this confidence level**

The decomposition is reported consistently across the original working-paper and published-study accounts, though its welfare implications remain unresolved.

**Evidence**

- About 9 percentage points of the roughly 13% gain came from more minutes worked, including fewer breaks and sick days; about 4 percentage points came from more calls per minute. [S10] [S12] [S14]

#### Finding 4

**Claim**

Observational and survey evidence is mixed and weaker for causal inference than experiments.

**Confidence:** Medium

**Why this confidence level**

These sources identify useful perceptions and mechanisms, but self-reporting, selection, heterogeneous designs, and adaptation limit causal interpretation.

**Evidence**

- Small-business owners reported substantial early-pandemic productivity declines, but perceptions became more positive by 2021 after technology investment, training, task redesign, and management adaptation. [S2]
- A systematic review of 20 peer-reviewed studies found mixed effects on performance and well-being. [S5]
- Survey-based comparisons of remote-supporting companies report favorable perceived effort and adaptability, but do not establish that remote work caused higher objective output. [S15]

#### Finding 5

**Claim**

Company- and industry-level data do not establish a consistent aggregate productivity effect.

**Confidence:** High

**Why this confidence level**

Official sources directly report positive and near-null estimates and explain why these estimates are not clean causal tests.

**Evidence**

- One BLS specification found a positive association between increased remote work and total-factor productivity growth across 61 industries, while another BLS analysis and the FRBSF analysis of 43 industries found little relationship. [S3] [S11]
- The aggregate analyses are observational and may be affected by industry composition, economic cycles, supply disruptions, task differences, and other pandemic-era factors. [S3] [S11]

#### Finding 6

**Claim**

Different conclusions mainly reflect differences in the treatment, outcomes, populations, timing, and mechanisms studied.

**Confidence:** High

**Why this confidence level**

These differences are explicitly documented and provide a coherent explanation for apparently conflicting findings.

**Evidence**

- Studies compare fully or mostly remote work with hybrid work, use different schedules, and examine call-center work versus professional engineering, marketing, accounting, and finance roles. [S8] [S9] [S10] [S12] [S14]
- Productivity measures range from calls and minutes worked to coding, revenue, performance reviews, promotions, turnover, survey perceptions, labor productivity, and total-factor productivity. [S1] [S2] [S3] [S9] [S10] [S15]
- Remote work can reduce interruptions and commuting-related constraints while impairing coordination, idea sharing, mentoring, and learning; organizational adaptation and management quality can change the balance over time. [S1] [S3] [S5] [S11]

### Conflicts Found

- The CTrip experiment found higher measured output under mostly remote work, whereas the Trip.com experiment found performance equivalence under hybrid work. This is a conditional disagreement involving different occupations, schedules, and metrics, not a direct test of the same treatment. [S9] [S10] [S12] [S14]
- Aggregate estimates range from a positive BLS association to near-null BLS and FRBSF estimates. Differences in samples, periods, measures, specifications, and observational confounding limit direct comparison. [S3] [S11]
- Employer perceptions shifted from predominantly negative early-pandemic assessments to more positive later assessments after organizational learning and adaptation. [S2]
- Positive survey-based company comparisons are more favorable than mixed reviews and neutral experimental performance estimates, likely because they capture perceptions and selected organizations rather than causal output changes. [S15] [S3] [S5] [S9]

### Important Gaps

- The evidence does not identify a general causal effect of fully remote work across occupations and industries outside narrowly measurable jobs.
- It remains unclear how much CTrip's gain reflected higher productivity per hour versus longer effective working time, fewer breaks, and fewer absences, and what this implied for employee welfare.
- Long-run effects on innovation, mentoring, knowledge transfer, promotion, and career development remain insufficiently measured.
- The relative importance of voluntary choice, home conditions, management quality, collaboration technology, and worker experience remains uncertain.
- The underlying methods and estimates behind commercial sources S6 and S7 cannot be independently assessed from the retrieved material.

**Analysis Duration:** 11.92s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

No usable new sources were retrieved, and the accumulated evidence is sufficient to answer the original question responsibly. Further searching could add examples, but is unlikely to change the central conclusion: hybrid work is compatible with maintained measured performance, fully remote effects are heterogeneous, and aggregate evidence is mixed and noncausal.

**Next Search**

> Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions. additional evidence search 9

---

# Iteration 9

## 1. Search

**Query**

> Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions. additional evidence search 9

**Why this query**

No usable new sources were retrieved, and the accumulated evidence is sufficient to answer the original question responsibly. Further searching could add examples, but is unlikely to change the central conclusion: hybrid work is compatible with maintained measured performance, fully remote effects are heterogeneous, and aggregate evidence is mixed and noncausal.

**Results**

5 results retrieved.

0 new unique sources added.

### Sources

No new unique sources were added.

**Search Duration:** 2.61s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The accumulated evidence supports a conditional conclusion rather than a universal one: hybrid work can preserve measured individual performance, while fully or mostly remote work ranges from positive to negative depending on occupation, task, intensity, and management context.

**Confidence:** High

**Why this confidence level**

The conclusion is supported by two randomized experiments, official analyses, and a systematic review; however, generalization beyond the studied firms, occupations, and arrangements remains limited.

**Evidence**

- The randomized Trip.com trial found no meaningful performance penalty under a two-days-per-week hybrid schedule and reduced resignations by about one-third. [S8] [S9]
- The randomized CTrip experiment found about a 13% increase in measured call-center performance under four-days-per-week home work, with much of the gain attributable to more minutes worked. [S10] [S12] [S14]
- Reviews and official syntheses report positive effects for focused, measurable tasks but mixed or negative effects for collaborative, learning-intensive, or newly hired roles. [S1] [S3] [S5]

#### Finding 2

**Claim**

Controlled experiments provide the strongest causal evidence, but their apparently different results are conditional rather than direct contradictions.

**Confidence:** High

**Why this confidence level**

Both results derive from randomized designs, but the interventions, populations, tasks, and outcome measures differ substantially.

**Evidence**

- CTrip studied volunteers in a highly measurable call-center setting, with employees working from home four days per week; output rose about 13% and call quality did not measurably decline. [S10] [S12] [S14]
- Trip.com's randomized trial studied 1,612 professional employees working from home two days per week and found no meaningful effect on reviews, promotions, coding output, or marketing revenue. [S8] [S9]

#### Finding 3

**Claim**

The CTrip output gain partly reflected more effective time worked, so it should not be interpreted simply as a rise in hourly productivity or employee welfare.

**Confidence:** High

**Why this confidence level**

The decomposition is reported consistently across the original working-paper and published-study accounts, although its welfare implications remain unresolved.

**Evidence**

- About 9 percentage points of the roughly 13% gain came from more minutes worked, including fewer breaks and sick days; about 4 percentage points came from more calls per minute. [S10] [S12] [S14]

#### Finding 4

**Claim**

Observational and survey evidence is mixed and weaker for causal inference than the experiments.

**Confidence:** Medium

**Why this confidence level**

These sources provide useful evidence about perceptions and mechanisms, but self-reporting, selection, heterogeneous designs, and adaptation limit causal interpretation.

**Evidence**

- Small-business owners reported substantial early-pandemic productivity declines, but assessments became more positive by 2021 after technology investment, training, task redesign, and management adaptation. [S2]
- A systematic review of 20 peer-reviewed studies found mixed effects on performance and well-being. [S5]
- Survey-based comparisons of remote-supporting companies report favorable perceived effort and adaptability, but do not establish that remote work caused higher objective output. [S15]

#### Finding 5

**Claim**

Company- and industry-level data do not establish a consistent aggregate productivity effect.

**Confidence:** High

**Why this confidence level**

Official sources directly report positive and near-null estimates and explain why these estimates are not clean causal tests.

**Evidence**

- One BLS specification found a positive association between increased remote work and total-factor productivity growth across 61 industries, while another BLS analysis and the FRBSF analysis of 43 industries found little relationship. [S3] [S11]
- The aggregate analyses are observational and may be affected by industry composition, economic cycles, supply disruptions, task differences, and other pandemic-era factors. [S3] [S11]

#### Finding 6

**Claim**

Conflicting findings mainly reflect differences in the treatment, outcomes, populations, timing, and mechanisms studied.

**Confidence:** High

**Why this confidence level**

Measurement, selection, adaptation, and mechanism differences are explicitly documented across the evidence base and coherently explain the divergent results.

**Evidence**

- Studies compare fully or mostly remote work with hybrid work, use different schedules, and examine call-center work versus professional engineering, marketing, accounting, and finance roles. [S8] [S9] [S10] [S12] [S14]
- Productivity measures range from calls and minutes worked to coding, revenue, performance reviews, promotions, turnover, survey perceptions, labor productivity, and total-factor productivity. [S1] [S2] [S3] [S9] [S10] [S15]
- Remote work can reduce interruptions and commuting-related constraints while impairing coordination, idea sharing, mentoring, and learning; organizational adaptation and management quality can change the balance over time. [S1] [S3] [S5] [S11]

### Conflicts Found

- CTrip found higher measured output under mostly remote work, while Trip.com found performance equivalence under hybrid work. This is a conditional disagreement involving different occupations, schedules, and metrics, not a direct test of the same treatment. [S9] [S10] [S12] [S14]
- Aggregate estimates range from a positive BLS association to near-null BLS and FRBSF estimates. Differences in samples, periods, measures, specifications, and observational confounding limit direct comparison. [S3] [S11]
- Employer perceptions shifted from predominantly negative early-pandemic assessments to more positive later assessments after organizational learning and adaptation. [S2]
- Positive survey-based company comparisons are more favorable than mixed reviews and neutral experimental performance estimates, likely because they capture perceptions and selected organizations rather than causal output changes. [S15] [S3] [S5] [S9]

### Important Gaps

- The evidence does not identify a general causal effect of fully remote work across occupations and industries outside narrowly measurable jobs.
- It remains unclear how much CTrip's gain reflected higher productivity per hour versus longer effective working time, fewer breaks, and fewer absences, and what this implied for employee welfare.
- Long-run effects on innovation, mentoring, knowledge transfer, promotion, and career development remain insufficiently measured.
- The relative importance of voluntary choice, home conditions, management quality, collaboration technology, and worker experience remains uncertain.
- The underlying methods and estimates behind commercial sources S6 and S7 cannot be independently assessed from the retrieved material.

**Analysis Duration:** 10.69s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The important parts of the question can be answered responsibly with the accumulated evidence: controlled experiments, observational studies, and company- or industry-level data have been compared, and the main reasons for divergent conclusions are clear. Further searching could add detail but is unlikely to change the central conditional conclusion; the remaining gaps concern generalizability and long-run mechanisms rather than the answer's core direction.

**Next Search**

> Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions. additional evidence search 10

---

# Iteration 10

## 1. Search

**Query**

> Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions. additional evidence search 10

**Why this query**

The important parts of the question can be answered responsibly with the accumulated evidence: controlled experiments, observational studies, and company- or industry-level data have been compared, and the main reasons for divergent conclusions are clear. Further searching could add detail but is unlikely to change the central conditional conclusion; the remaining gaps concern generalizability and long-run mechanisms rather than the answer's core direction.

**Results**

5 results retrieved.

0 new unique sources added.

### Sources

No new unique sources were added.

**Search Duration:** 2.87s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Remote work has no universal productivity effect; the best-supported conclusion is conditional on work arrangement, occupation, task, intensity, and management context.

**Confidence:** High

**Why this confidence level**

This pattern is consistent across randomized experiments, official analyses, and a systematic review.

**Evidence**

- Reviews and official syntheses report positive effects for focused, measurable tasks but mixed or negative effects for collaborative, learning-intensive, or newly hired roles. [S1] [S3] [S5]
- The evidence compares mostly remote call-center work with hybrid professional roles, rather than one identical intervention. [S8] [S9] [S10] [S12] [S14]

#### Finding 2

**Claim**

Controlled experiments provide the strongest causal evidence, but their different results are conditional rather than directly contradictory.

**Confidence:** High

**Why this confidence level**

Both results come from randomized designs, but the firms, occupations, schedules, and outcome measures differ substantially.

**Evidence**

- The randomized CTrip experiment found about a 13% increase in measured call-center performance when employees worked from home four days per week; call quality did not measurably decline. [S10] [S12] [S14]
- The randomized Trip.com trial of 1,612 professional employees working from home two days per week found no meaningful effect on performance reviews, promotions, coding output, or marketing revenue, while resignations fell by about one-third. [S8] [S9]

#### Finding 3

**Claim**

The CTrip productivity gain partly reflected more time worked rather than solely higher hourly productivity.

**Confidence:** High

**Why this confidence level**

The decomposition is reported consistently across the original study accounts, although its implications for employee welfare remain unclear.

**Evidence**

- About 9 percentage points of the roughly 13% gain came from more minutes worked, including fewer breaks and sick days; about 4 percentage points came from more calls per minute. [S10] [S12] [S14]

#### Finding 4

**Claim**

Observational and survey evidence is mixed and weaker for causal inference than the experiments.

**Confidence:** Medium

**Why this confidence level**

These sources provide useful evidence about perceptions and mechanisms, but self-reporting, selection, heterogeneous designs, and adaptation limit causal interpretation.

**Evidence**

- Small-business owners reported substantial productivity declines early in 2020, but assessments became more positive by 2021 after technology investment, training, task redesign, and management adaptation. [S2]
- A systematic review of 20 peer-reviewed studies found mixed effects on performance and well-being. [S5]
- Survey-based comparisons of remote-supporting companies report favorable perceived effort and adaptability, but do not establish that remote work caused higher objective output. [S15]

#### Finding 5

**Claim**

Company- and industry-level data do not establish a consistent aggregate productivity effect.

**Confidence:** High

**Why this confidence level**

Official sources directly report positive and near-null estimates and explain why these estimates are not clean causal tests.

**Evidence**

- One BLS specification found a positive association between increased remote work and total-factor productivity growth across 61 industries, while another BLS analysis and the FRBSF analysis of 43 industries found little relationship. [S3] [S11]
- These analyses are observational and may be affected by industry composition, economic cycles, supply disruptions, task differences, and other pandemic-era factors. [S3] [S11]

#### Finding 6

**Claim**

Different conclusions mainly reflect differences in the treatment, outcomes, populations, timing, and mechanisms studied.

**Confidence:** High

**Why this confidence level**

Measurement, selection, adaptation, and mechanism differences are explicitly documented and coherently explain the divergent results.

**Evidence**

- Studies compare fully or mostly remote work with hybrid work and examine call-center work versus professional engineering, marketing, accounting, and finance roles. [S8] [S9] [S10] [S12] [S14]
- Productivity measures range from calls and minutes worked to coding, revenue, performance reviews, promotions, turnover, survey perceptions, labor productivity, and total-factor productivity. [S1] [S2] [S3] [S9] [S10] [S15]
- Remote work can reduce interruptions and commuting-related constraints while impairing coordination, idea sharing, mentoring, and learning; organizational adaptation and management quality can change the balance over time. [S1] [S3] [S5] [S11]

### Conflicts Found

- The CTrip experiment found higher measured output under mostly remote work, whereas the Trip.com experiment found performance equivalence under hybrid work. This is a conditional disagreement involving different occupations, schedules, and metrics, not a direct test of the same treatment. [S9] [S10] [S12] [S14]
- Aggregate estimates range from a positive BLS association to near-null BLS and FRBSF estimates. Differences in samples, periods, measures, specifications, and observational confounding limit direct comparison. [S3] [S11]
- Employer perceptions shifted from predominantly negative early-pandemic assessments to more positive later assessments after organizational learning and adaptation. [S2]
- Positive survey-based company comparisons are more favorable than mixed reviews and neutral experimental performance estimates, likely because they capture perceptions and selected organizations rather than causal output changes. [S15] [S3] [S5] [S9]

### Important Gaps

- The evidence does not identify a general causal effect of fully remote work across occupations and industries outside narrowly measurable jobs.
- It remains unclear how much CTrip's gain reflected higher productivity per hour versus longer effective working time, fewer breaks, and fewer absences, and what this implied for employee welfare.
- Long-run effects on innovation, mentoring, knowledge transfer, promotion, and career development remain insufficiently measured.
- The relative importance of voluntary choice, home conditions, management quality, collaboration technology, and worker experience remains uncertain.
- The underlying methods and estimates behind commercial sources S6 and S7 cannot be independently assessed from the retrieved material.

**Analysis Duration:** 12.32s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The runner reached the maximum research iteration budget. Analyzer assessment: The accumulated evidence is sufficient to answer the original comparison responsibly: randomized studies support positive effects in some narrowly measurable mostly-remote work and performance neutrality under hybrid work; observational and aggregate evidence is mixed and non-causal; and the main sources of disagreement are differences in treatment, tasks, populations, measures, timing, selection, and adaptation. Further research would improve generalizability, especially for fully remote work, but is not necessary to state the conditional conclusion.

**Stop Reason:** max_iterations

---

# Final Research Decision

**Research Stopped Because**

The runner reached the maximum research iteration budget.

**Stop Reason:** max_iterations

**Searches Performed:** 10

**Unique Sources:** 16

**Remaining Uncertainty**

- The evidence does not identify a general causal effect of fully remote work across occupations and industries outside narrowly measurable jobs such as the studied call-center setting.
- It remains unclear how much of the CTrip gain reflected higher productivity per hour versus longer effective working time, fewer breaks, and fewer absences, and what those changes imply for employee welfare.
- Long-run effects on innovation, mentoring, knowledge transfer, promotion, and career development remain insufficiently measured.
- The relative importance of voluntary choice, home working conditions, management quality, collaboration technology, and worker experience remains uncertain.
- The supplied material does not provide all experimental details, including complete confidence intervals, treatment compliance, and all subgroup estimates.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 10 | 28.36s |
| OpenAI Analysis | 10 | 143.15s |
| Report Generation | 1 | 18.01s |
| Total Run | — | 189.52s |
