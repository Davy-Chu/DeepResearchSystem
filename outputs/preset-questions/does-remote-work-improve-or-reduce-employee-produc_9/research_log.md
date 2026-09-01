# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

Does remote work improve or reduce employee productivity? Compare evidence from controlled experiments, observational studies, and company-level data, and explain why different studies reach conflicting conclusions.

**Status:** Completed

**Stop Reason:** sufficient_evidence

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 10

**Unique Sources:** 14

**OpenAI Calls:** 4

**Tavily Calls:** 3

**Started:** 2026-09-01T02:56:39-04:00

**Ended:** 2026-09-01T02:57:52-04:00

**Total Runtime:** 73.16s

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
- **S3 — Work from home and employee well-being: a double-edged sword**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12333122
- **S4 — In-Office vs Remote Productivity: What the Data Shows | Worklytics**
  URL: https://www.worklytics.co/blog/in-office-vs-remote-day-productivity-which-is-better
- **S5 — The rise in remote work since the pandemic and its impact ...**
  URL: https://www.bls.gov/opub/btn/volume-13/remote-work-productivity.htm

**Search Duration:** 3.39s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Remote work does not have a uniform productivity effect; outcomes appear to depend on task type, work arrangement, worker characteristics, technology, and management practices.

**Confidence:** Medium

**Why this confidence level**

The conclusion is consistent across the BLS discussion and the reported synthesis, but the most specific effect-size claims in S1 come from a secondary commercial source.

**Evidence**

- The BLS review states that effects depend on task types, technology, home environment, motivation, and management, and describes positive individual experiments alongside negative short-run case studies and neutral aggregate evidence. [S5]
- The eMonitor synthesis reports positive effects for focused individual tasks but negative effects for collaborative tasks, and emphasizes differences between hybrid, fully remote, newly hired, and highly collaborative workers. [S1]

#### Finding 2

**Claim**

The reported controlled-experiment evidence is generally positive or neutral for individual productivity, especially in call-center work and hybrid arrangements.

**Confidence:** Medium

**Why this confidence level**

The BLS source corroborates the broad direction, but the detailed sample sizes and effect estimates are supplied only by S1, whose article is a secondary commercial synthesis rather than the original experiment reports.

**Evidence**

- The 2015 Ctrip experiment is reported as a randomized assignment of 249 call-center workers, with remote workers completing 13.5% more calls than office workers; the reported gains came from more minutes worked and more calls per minute. [S1]
- The reported 2024 Trip.com randomized hybrid experiment assigned 1,612 employees to two remote days or five office days and found no statistically significant difference in performance reviews, promotions, code output, or marketing revenue, while resignations fell by 33%. [S1]
- The BLS article summarizes randomized experiments as finding small positive effects on individual productivity and lower turnover, while noting that productivity measures differ across studies. [S5]

#### Finding 3

**Claim**

Observational survey evidence suggests that perceptions of remote-work productivity became more favorable as firms adapted, but also identifies persistent monitoring and training challenges.

**Confidence:** Medium

**Why this confidence level**

The study uses repeated firm and worker surveys and directly documents changing perceptions, but perceptions are not equivalent to objectively measured output and the paper is identified as a working paper.

**Evidence**

- Repeated surveys of small-business owners found that 70% perceived a productivity dip early in 2020, whereas the median owner reported a positive productivity effect by early 2021. [S2]
- The same study attributes improvement partly to technology investment, training, altered tasks, and improved remote management, but reports continuing difficulty monitoring employees and concerns about learning new skills, especially in larger firms. [S2]

#### Finding 4

**Claim**

Company- and industry-level evidence is mixed: one broad industry analysis finds a positive association between increased remote work and total-factor-productivity growth, while another cited aggregate analysis finds little relationship with labor productivity.

**Confidence:** Medium

**Why this confidence level**

The source directly reports both aggregate results, but the underlying studies and identification details are not included in the retrieved text.

**Evidence**

- The BLS analysis reports that, across 61 private-sector industries, growth in total factor productivity from 2019–21 and 2019–22 was positively associated with the increase in remote work, even after accounting for pre-pandemic productivity trends. [S5]
- The same BLS article reports that Fernald et al. found little relationship across 43 private-sector industries between labor productivity and the ability of workers in an industry to work entirely remotely. [S5]

#### Finding 5

**Claim**

Differences in measured outcomes help explain apparently conflicting conclusions.

**Confidence:** High

**Why this confidence level**

The distinction between outcomes, levels of analysis, and arrangements is directly documented in the sources and provides a well-supported explanation for conflicting findings.

**Evidence**

- Individual experiments use measures such as calls, emails, calls per minute, performance ratings, code, revenue, hours, and turnover; the BLS source notes that these are different proxies for individual labor productivity. [S1] [S5]
- Industry-level studies instead examine total-factor productivity, output, unit input costs, or labor productivity, which can incorporate organizational, sectoral, and measurement effects beyond an employee's direct output. [S5]
- S1 distinguishes focused work, collaborative work, hybrid work, and fully remote work, implying that averaging across these settings can conceal opposite effects. [S1]

#### Finding 6

**Claim**

Remote work may improve retention and job satisfaction even when it does not raise measured productivity, creating an organizational benefit that is separate from direct output.

**Confidence:** Medium

**Why this confidence level**

The broad finding is corroborated, but the precise attrition estimates rely mainly on S1.

**Evidence**

- The reported Ctrip experiment found higher job satisfaction and 50% lower attrition among remote workers; the reported Trip.com hybrid experiment found equal measured performance and a 33% reduction in resignations. [S1]
- The BLS summary likewise states that randomized experiments found lower turnover as job satisfaction rose, potentially reducing hiring costs. [S5]

### Conflicts Found

- Individual-level randomized and company experiments described in the sources report positive or neutral productivity effects, whereas some pandemic-era single-firm case studies reportedly found short-run declines. [S1] [S5]
- Aggregate company/industry conclusions differ: the BLS analysis reports a positive association between rising remote work and TFP growth across 61 industries, while the cited Fernald et al. analysis found little relationship between remote-work feasibility and labor productivity across 43 industries. [S5]
- Remote work is reported as beneficial for focused individual tasks but detrimental for collaborative tasks, so studies with different task compositions can reach conditional rather than genuinely incompatible conclusions. [S1] [S4]
- Employer perceptions changed from predominantly negative early in the pandemic to positive later, indicating that adaptation and study timing can produce different observational results. [S2]

### Important Gaps

- The retrieved material does not provide the original full reports for the cited Ctrip and Trip.com experiments, so their identification procedures, uncertainty intervals, and exact productivity definitions cannot be independently assessed here.
- The evidence does not establish how well call-center results generalize to software, professional services, creative work, managers, or jobs requiring physical presence.
- It remains unclear how much of aggregate productivity growth reflects remote work itself rather than worker selection, industry composition, technology investment, altered tasks, pandemic demand shocks, or other simultaneous changes.
- The retrieved sources provide limited direct evidence on innovation, mentoring, onboarding, and long-run team or firm productivity.
- Several claims in the commercial sources use surveys, analytics metrics, or unspecified studies; self-reported productivity and digital activity are not equivalent to output or total-factor productivity.

**Analysis Duration:** 17.27s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The overall pattern can be answered responsibly, but the most important controlled-experiment evidence is presented through a secondary commercial synthesis, and the aggregate findings are reported without the underlying studies' methods. A focused search for the original randomized experiment papers would materially improve confidence and comparability.

**Next Search**

> original randomized controlled trial remote work productivity Ctrip Trip.com 2015 2024 paper

---

# Iteration 2

## 1. Search

**Query**

> original randomized controlled trial remote work productivity Ctrip Trip.com 2015 2024 paper

**Why this query**

The overall pattern can be answered responsibly, but the most important controlled-experiment evidence is presented through a secondary commercial synthesis, and the aggregate findings are reported without the underlying studies' methods. A focused search for the original randomized experiment papers would materially improve confidence and comparability.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S6 — Does Working from Home Increase Productivity? (2026)**
  URL: https://emailanalytics.com/does-working-from-home-increase-productivity
- **S7 — Are Remote Workers More Productive? What The Research Actually Shows — FYIVT**
  URL: https://fyivt.com/are-remote-workers-more-productive-what-the-research-actually-shows
- **S8 — Hybrid working from home improves retention without ...**
  URL: https://www.nature.com/articles/s41586-024-07500-2
- **S9 — Experiment at Trip.com shows hybrid work is better | Cybernews**
  URL: https://cybernews.com/tech/hybrid-remote-work-trip-com-research

**Search Duration:** 1.85s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The strongest new evidence supports a distinction between fully remote and hybrid work: hybrid work did not reduce measured performance in the Trip.com experiment, while improving retention.

**Confidence:** High

**Why this confidence level**

The result is supported by the primary peer-reviewed article and prior corroborating summaries. It concerns hybrid rather than fully remote work and therefore should not be generalized to all remote arrangements.

**Evidence**

- The primary Nature article reports a randomized experiment involving university-educated employees at Trip.com and is titled “Hybrid working from home improves retention without damaging performance.” [S8]
- The accumulated research state reports that 1,612 employees were assigned to two remote days or five office days; the study found no statistically significant difference in performance reviews, promotions, code output, or marketing revenue, while resignations fell by 33%. [S1] [S5]

#### Finding 2

**Claim**

The new evidence reinforces that the positive Ctrip result is highly context-specific: it came from a measurable, relatively independent call-center job and does not establish a general productivity gain for knowledge work.

**Confidence:** Medium

**Why this confidence level**

The contextual interpretation is useful and consistent with the experiment’s reported outcome, but S7 is a secondary source and the original Ctrip report was not retrieved.

**Evidence**

- The source describes the Ctrip trial as involving call-center employees whose output was measured through calls handled, calls per minute, and logged time, and characterizes the work as repetitive and easy to monitor. [S7]
- The accumulated state reports a 13.5% increase in calls among remotely assigned workers in the Ctrip experiment, with gains attributed to more minutes worked and higher calls per minute. [S1] [S5]

#### Finding 3

**Claim**

Objective observational evidence from an Asian IT-services firm indicates that fully remote work can reduce productivity per hour even when total hours worked rise.

**Confidence:** Low

**Why this confidence level**

This is potentially important objective evidence from a large observational study, but the retrieved support is a secondary summary; the underlying paper, research design, and uncertainty estimates were not retrieved.

**Evidence**

- S7 reports that Gibbs, Mengel and Siemroth studied more than 10,000 skilled professionals using personnel and analytics data; hours worked rose by about 30%, average output did not significantly change, and output per hour fell by 8%–19%. [S7]
- The reported mechanism included more after-hours work, increased meetings, and reduced uninterrupted work time, which are consistent with coordination costs reducing hourly productivity. [S7]

#### Finding 4

**Claim**

Remote-work studies conflict partly because they examine different causal margins: home-based work in a repetitive individual task, hybrid work among professional employees, and fully remote work in coordination-intensive IT work are not equivalent treatments.

**Confidence:** High

**Why this confidence level**

The sources directly document materially different jobs, arrangements, and study designs, providing a strong explanation for conditional disagreement rather than a single universal effect.

**Evidence**

- Ctrip is described as a randomized call-center experiment, Trip.com as a randomized hybrid experiment among engineering, marketing, and finance staff, and the Gibbs et al. study as observational evidence from skilled IT professionals. [S7] [S8]
- The accumulated evidence indicates positive effects for focused individual tasks, negative effects for collaborative tasks, and neutral or positive effects for hybrid arrangements. [S1] [S4] [S5]

#### Finding 5

**Claim**

The new sources add suggestive evidence that remote work may affect innovation and professional networks even when short-run individual performance is unchanged, but this evidence is not sufficient to establish a productivity effect.

**Confidence:** Low

**Why this confidence level**

The finding is reported only through a secondary source, and the retrieved material does not provide the study’s design, measures, or causal interpretation.

**Evidence**

- S7 reports a Microsoft study finding that fully remote work made professional networks more siloed and that this was associated with lower innovation output and slower career development. [S7]
- The accumulated state identifies innovation, mentoring, onboarding, and long-run team or firm productivity as important evidence gaps. [S1] [S5]

### Conflicts Found

- The Ctrip randomized trial reports a substantial positive effect on call-center output, whereas the reported Gibbs, Mengel and Siemroth observational study finds an 8%–19% decline in output per hour among IT workers. The disagreement may reflect job and arrangement differences, but the observational result cannot be treated as equally causal without the original study details. [S7] [S1] [S5]
- The Trip.com randomized hybrid experiment finds no performance damage, while the reported IT-services study finds lower hourly productivity under fully remote work. These are conditional differences between hybrid and fully remote arrangements rather than necessarily contradictory estimates of the same treatment. [S7] [S8]
- S7 presents the Microsoft network finding as relevant to innovation, but the retrieved evidence does not establish that network siloing caused lower innovation; this is weaker than the directly measured short-run performance evidence in S8. [S7] [S8]

### Important Gaps

- What are the original identification strategy, productivity definitions, and uncertainty intervals in the Gibbs, Mengel and Siemroth IT-services study?
- How much do fully remote findings from call centers and one IT-services firm generalize to other professional, creative, managerial, and collaborative jobs?
- Do remote or hybrid arrangements affect long-run innovation, mentoring, onboarding, and promotion outcomes, independently of short-run performance measures?
- How much of industry-level productivity growth reflects remote work itself rather than selection, technology investment, industry composition, pandemic shocks, or changed tasks?
- The new commercial sources make additional claims about stress, monitoring, cost savings, and email-based productivity, but the retrieved content does not provide sufficiently transparent methods to treat those claims as reliable evidence.

**Analysis Duration:** 14.43s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The core comparison is now responsibly answerable: controlled experiments suggest positive effects in measurable individual work and neutral effects for hybrid professional work, while observational IT evidence suggests lower productivity per hour under fully remote work. However, the most important negative observational estimate is available only through a secondary summary, and resolving its design and measurement would materially improve the comparison.

**Next Search**

> Gibbs Mengel Siemroth remote work productivity IT workers 8 19 percent Journal of Political Economy Microeconomics original paper

---

# Iteration 3

## 1. Search

**Query**

> Gibbs Mengel Siemroth remote work productivity IT workers 8 19 percent Journal of Political Economy Microeconomics original paper

**Why this query**

The core comparison is now responsibly answerable: controlled experiments suggest positive effects in measurable individual work and neutral effects for hybrid professional work, while observational IT evidence suggests lower productivity per hour under fully remote work. However, the most important negative observational estimate is available only through a secondary summary, and resolving its design and measurement would materially improve the comparison.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S10 — Work from Home & Productivity: Evidence from Personnel & Analytics Data on IT Professionals | IZA@LISER Network**
  URL: https://www.iza.org/de/publications/dp/14336/work-from-home-productivity-evidence-from-personnel-analytics-data-on-it-professionals
- **S11 — Gibbs, M., Mengel, F., & Siemroth, C. (2023). Work from Home and Productivity Evidence from Personnel and Analytics Data on Information Technology Professionals. Journal of Political Economy Microeconomics, 1, 7-41. - References**
  URL: https://www.scirp.org/reference/referencespapers?referenceid=3912829
- **S12 — Work from Home and Productivity: Evidence from Personnel and Analytics Data on Information Technology Professionals 
			-
			Research Repository**
  URL: https://repository.essex.ac.uk/32705
- **S13 — Work from Home & Productivity: Evidence from Personnel & Analytics Data on IT Professionals**
  URL: https://ideas.repec.org/p/iza/izadps/dp14336.html
- **S14 — [PDF] COVID-19 and the shift to remote work - Bruegel**
  URL: https://www.bruegel.org/sites/default/files/2023-06/PC%2009%202022.pdf

**Search Duration:** 2.56s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The Gibbs, Mengel, and Siemroth study provides substantially stronger support for a negative short-run productivity effect of fully remote work among skilled IT professionals than the earlier secondary summaries did.

**Confidence:** High

**Why this confidence level**

The result is reported by an institutional repository and the IZA network, and the study is linked to a peer-reviewed journal publication. The exact decline is reported somewhat differently across abstracts, but all sources agree on the direction and mechanism.

**Evidence**

- The study uses personnel and analytics data from more than 10,000 professionals at a large Indian IT-services company and measures productivity as output per hour worked. Hours increased by roughly 30%, while average output did not significantly change; productivity therefore fell by 8%–19% in the repository abstract. [S12]
- The IZA source similarly reports increased hours, unchanged average output, and an approximately 20% productivity decline, attributing the result to increased coordination and meeting time and reduced uninterrupted work. [S10]
- The study is identified as a 2023 Journal of Political Economy: Microeconomics article, rather than merely an unspecified commercial study. [S10] [S12] [S13]

#### Finding 2

**Claim**

The observed decline is plausibly connected to coordination costs and reduced deep-work time rather than to lower total effort.

**Confidence:** High

**Why this confidence level**

These mechanisms and subgroup patterns are stated directly in the study abstracts across multiple research repositories.

**Evidence**

- During work from home, coordination and meeting time increased, uninterrupted work hours shrank, networking decreased, and employees received fewer coaching and one-to-one meetings with supervisors. [S10] [S12] [S13]
- Employees with children at home increased hours more than employees without children at home and experienced a larger productivity decline. [S10] [S13]

#### Finding 3

**Claim**

The new evidence strengthens the explanation that fully remote work can be less productive in coordination-intensive knowledge work, while not overturning the positive or neutral experimental findings from other settings.

**Confidence:** High

**Why this confidence level**

The evidence compares materially different treatments and populations: fully remote IT work, repetitive call-center work, and randomized hybrid knowledge work. The studies therefore support conditional rather than universal conclusions.

**Evidence**

- Gibbs et al. study fully remote work during the pandemic among skilled IT professionals and finds lower output per hour. [S12]
- The accumulated evidence includes a randomized call-center experiment with higher remote output and a randomized hybrid experiment with no performance reduction. [S1] [S5] [S8]
- The Bruegel review emphasizes that remote-work feasibility varies by sector and task, and that hybrid arrangements are likely to be especially common among knowledge workers. [S14]

#### Finding 4

**Claim**

The distinction between productivity per hour and total output is important: remote work may increase hours without increasing output, reducing hourly productivity.

**Confidence:** High

**Why this confidence level**

Both the IT study’s productivity definition and the earlier experiment’s reported decomposition are directly described in the retrieved material.

**Evidence**

- In the IT-services study, hours worked rose substantially but average output did not significantly change, producing a decline in output per hour. [S10] [S12] [S13]
- The previously retrieved Ctrip evidence attributed higher call-center output partly to more minutes worked as well as greater output per minute, illustrating that total output and efficiency per hour can diverge. [S1] [S5]

#### Finding 5

**Claim**

The observational IT-services result should not be interpreted as a clean universal causal estimate of remote work because it compares pre-pandemic and pandemic periods within one firm.

**Confidence:** High

**Why this confidence level**

The before/during-pandemic design is explicit, while the inability to isolate remote work from all contemporaneous changes follows directly from the observational setup and the documented evidence gaps.

**Evidence**

- The study compares productivity before and during the work-from-home period of the Covid-19 pandemic rather than describing random assignment to remote work. [S10] [S12] [S13]
- The broader research state identifies simultaneous changes—including technology investment, altered tasks, worker selection, pandemic shocks, and industry composition—as unresolved confounders in observational and aggregate evidence. [S2] [S5]

#### Finding 6

**Claim**

The Bruegel policy review supports the view that remote work preserved substantial productivity in many sectors during the pandemic, but it is contextual and not a direct estimate of the causal productivity effect.

**Confidence:** Medium

**Why this confidence level**

The source is a policy review and provides broad synthesis rather than a controlled productivity estimate. Its value is mainly in documenting sectoral heterogeneity and adaptation considerations.

**Evidence**

- The review states that remote work enabled many knowledge workers to continue working and maintained a high level of productivity in many economic sectors, while stressing that task suitability differs across sectors. [S14]
- It recommends managing based on results rather than hours and anticipates hybrid arrangements, implying that organizational practices affect outcomes. [S14]

### Conflicts Found

- The abstracts report a productivity decline of 8%–19% in one place and about 20% in another. This is a minor numerical inconsistency in presentation, not a disagreement about the direction of the result. [S10] [S12] [S13]
- The negative fully remote IT finding contrasts with positive call-center results and neutral hybrid results. The conditional difference is plausibly explained by differences in task independence, coordination demands, work arrangement, and productivity measurement rather than by estimates of the same treatment. [S1] [S8] [S12] [S14]
- The Bruegel review says productivity was maintained in many sectors, whereas the Gibbs study finds lower hourly productivity in one IT-services firm. The review is broad and descriptive; the Gibbs study is firm-specific and quantitatively measured, so the claims operate at different levels of generality. [S10] [S12] [S14]

### Important Gaps

- How much of the Gibbs et al. decline was caused specifically by remote work rather than pandemic conditions, changed demand, management adjustments, or other simultaneous changes?
- How generalizeable is the IT-services result to software development, creative work, professional services, managers, and other collaborative knowledge jobs?
- Do coordination costs decline as firms and workers adapt, or do long-run effects on innovation, mentoring, networking, and promotion remain negative?
- How should studies compare output per hour, total output, quality, innovation, retention, and firm-level productivity without conflating distinct outcomes?
- The retrieved material still does not provide the full identification strategy or uncertainty intervals for all major experiments and aggregate studies.

**Analysis Duration:** 16.01s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The new institutional and repository sources materially strengthen the key observational evidence and resolve the earlier uncertainty about whether the reported IT-services result was only a secondary claim. Together with the randomized call-center and hybrid evidence, the accumulated material supports a responsible answer: remote work has no universal effect; fully remote work can reduce hourly productivity in coordination-intensive settings, while hybrid or highly measurable individual work can be neutral or positive. Remaining gaps concern generalization and long-run outcomes, but they are not necessary to answer the original comparative question.

**Stop Reason:** sufficient_evidence

---

# Final Research Decision

**Research Stopped Because**

The analyzer determined that the important parts of the question could be answered responsibly.

**Stop Reason:** sufficient_evidence

**Searches Performed:** 3

**Unique Sources:** 14

**Remaining Uncertainty**

- How much of the IT-services productivity decline was caused specifically by remote work rather than pandemic conditions, changed demand, management adjustments, or other simultaneous changes.
- How well findings from call centers and one IT-services company generalize to software development, creative work, professional services, managers, and other collaborative knowledge jobs.
- Whether coordination and communication costs diminish as firms and employees adapt over longer periods.
- How remote and hybrid work affect long-run innovation, mentoring, onboarding, networking, and promotion outcomes.
- How best to compare output per hour, total output, quality, innovation, retention, and firm-level productivity without treating them as interchangeable measures.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 7.80s |
| OpenAI Analysis | 3 | 47.71s |
| Report Generation | 1 | 17.65s |
| Total Run | — | 73.16s |
