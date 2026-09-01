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

**Unique Sources:** 27

**OpenAI Calls:** 11

**Tavily Calls:** 10

**Started:** 2026-09-01T05:08:22-04:00

**Ended:** 2026-09-01T05:11:30-04:00

**Total Runtime:** 187.16s

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
- **S2 — 40+ remote work productivity statistics, trends & data for 2026**
  URL: https://www.worktime.com/blog/statistics/remote-work-productivity-statistics-trends-data
- **S3 — In-Office vs Remote Productivity: What the Data Shows | Worklytics**
  URL: https://www.worklytics.co/blog/in-office-vs-remote-day-productivity-which-is-better
- **S4 — The Rise of Remote Work: Evidence on Productivity and ...**
  URL: https://www.hbs.edu/ris/download.aspx?name=20-138.pdf
- **S5 — Work from home and employee well-being: a double-edged ...**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12333122

**Search Duration:** 3.82s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The best-supported conclusion from the retrieved material is conditional: remote work can improve individual output on focused tasks, while fully remote arrangements may reduce performance on collaboration-intensive or onboarding-related work; hybrid work appears neutral for measured individual performance in the cited Trip.com experiment.

**Confidence:** Medium

**Why this confidence level**

The sources converge on task- and arrangement-specific effects, but two are commercial secondary summaries and do not provide enough methodological detail to independently verify their quantitative claims.

**Evidence**

- The eMonitor synthesis reports a median +10% effect for focused tasks and −4% for collaborative tasks, and describes a 2023 working paper finding 10–20% lower output for some fully remote roles, especially highly collaborative or newly hired workers. [S1]
- Worklytics similarly summarizes higher remote focus productivity and advantages of offices for collaboration, knowledge sharing, mentoring, and creative problem-solving. [S3]
- The same Worklytics source states that hybrid arrangements often balance focus and collaboration, but its claims are presented as a secondary industry summary rather than a directly reported experiment. [S3]

#### Finding 2

**Claim**

A randomized Trip.com/Ctrip evidence base, as described in the retrieved sources, finds positive effects for a fully remote call-center treatment in one experiment and no detectable performance penalty for a later hybrid treatment.

**Confidence:** Medium

**Why this confidence level**

The reported experimental results are relevant and broadly consistent across the two summaries, but the retrieved content does not include the primary papers, treatment compliance, confidence intervals, or full outcome definitions.

**Evidence**

- The eMonitor account reports that the 2015 Ctrip randomized experiment assigned 249 call-center employees to mostly home-based work or office work and found 13.5% more calls, alongside higher satisfaction and lower attrition. [S1]
- It reports that a 2024 Trip.com randomized study of 1,612 employees found no statistically significant difference in performance reviews, promotions, coding, revenue, or hours between hybrid and office groups, while resignations fell by 33%. [S1] [S2]
- WorkTime independently repeats the headline that the Nature hybrid study found no productivity decline and a 33% turnover reduction. [S2]

#### Finding 3

**Claim**

Observational and survey evidence generally indicates stable or improving perceived productivity, but it is not sufficient by itself to establish that remote work caused the improvement.

**Confidence:** Medium

**Why this confidence level**

S4 is a research working paper with explicit survey design and limitations, while S2 reports an apparently relevant macro association without enough detail to assess identification or measurement.

**Evidence**

- A Harvard Business School working paper based on repeated surveys of small-business owners and workers reports that 70% of owners initially perceived a productivity dip in early 2020, while the median owner reported a positive effect by early 2021. [S4]
- The same paper says firms adapted through technology investment, training, task changes, and improved remote-management practices, while owners still reported monitoring and skill-learning difficulties, particularly in larger firms. [S4]
- WorkTime reports a positive association in a BLS analysis between remote-work adoption and total-factor-productivity growth, but the retrieved passage describes this as an association rather than a randomized causal estimate. [S2]

#### Finding 4

**Claim**

Differences in study conclusions can plausibly arise from differences in task mix, worker selection, outcome measurement, and adaptation over time.

**Confidence:** High

**Why this confidence level**

These mechanisms are directly supported by multiple retrieved sources and explain conditional rather than absolute disagreement. However, the evidence does not establish the relative size of each mechanism.

**Evidence**

- The sources distinguish focused individual output from collaboration, innovation, mentoring, and onboarding, which are affected differently by remote and office settings. [S1] [S3]
- The HBS paper reports that productivity perceptions shifted from negative to positive as firms invested in technology, training, task redesign, and management capability. [S4]
- The HBS paper also reports that workers and firms differ in their valuation of remote work, and that larger firms were less optimistic and had greater monitoring and learning concerns. [S4]
- The experimental account says the positive Ctrip result came from a relatively specific call-center setting, whereas negative effects were concentrated in some collaborative and newly hired roles. [S1]

#### Finding 5

**Claim**

Remote work may improve retention and worker satisfaction even when its effect on measured output is zero or negative, so organizational productivity cannot be inferred from individual task output alone.

**Confidence:** Medium

**Why this confidence level**

The direction of the retention and preference findings is repeated or reported in research material, but the long-run organizational effects of turnover, social isolation, and learning are not directly measured in the retrieved excerpts.

**Evidence**

- The reported hybrid experiment found equivalent measured performance but substantially lower resignations. [S1] [S2]
- The reported fully remote Ctrip experiment found higher satisfaction and lower attrition alongside higher call output, while many participants later preferred returning to the office because of social isolation. [S1]
- The HBS survey reports that a substantial minority of workers would accept a sizable pay cut to retain remote work, indicating meaningful amenity value. [S4]

### Conflicts Found

- The evidence contains a conditional disagreement over fully remote work: the reported Ctrip randomized trial finds a 13.5% increase in call output, whereas the reported later working paper finds 10–20% reductions for some roles. This is not necessarily a direct contradiction because the studies concern different roles, worker populations, and collaboration requirements. [S1]
- Perceived productivity changed over time: most small-business owners initially reported a productivity dip during the forced pandemic transition, but the median owner later reported a positive effect. This conflicts only if early-transition and adapted steady-state periods are treated as equivalent. [S4]
- Employee self-reports and business-owner perceptions are generally positive, while the sources also report concerns about monitoring, learning, collaboration, and innovation. Perceived individual productivity therefore does not uniformly align with broader organizational or team productivity. [S2] [S3] [S4]

### Important Gaps

- The retrieved material does not provide the primary controlled-experiment papers, so treatment effects, statistical precision, compliance, and external validity cannot be independently assessed.
- There is insufficient direct evidence on company-level outcomes such as total firm productivity, innovation, revenue, and long-run learning, as distinct from individual output or survey perceptions.
- The magnitude of remote-work effects by occupation, worker seniority, home-work conditions, and management practices remains unclear.
- The BLS and other macro/company claims lack enough methodological detail in the retrieved excerpts to determine whether they address selection into remote-capable industries and firms.
- The retrieved excerpt from the 2025 well-being study does not contain its results, so well-being mechanisms cannot be integrated reliably.

**Analysis Duration:** 19.89s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

Another search would materially improve the answer by retrieving primary sources for the key randomized experiments and a credible observational or company-level causal study. Current quantitative evidence is mostly reported through commercial summaries, and the main causal comparison is not independently documented.

**Next Search**

> primary study randomized hybrid remote work productivity Trip.com Nature 2024 Ctrip 2015 fully remote productivity observational firm-level causal evidence

---

# Iteration 2

## 1. Search

**Query**

> primary study randomized hybrid remote work productivity Trip.com Nature 2024 Ctrip 2015 fully remote productivity observational firm-level causal evidence

**Why this query**

Another search would materially improve the answer by retrieving primary sources for the key randomized experiments and a credible observational or company-level causal study. Current quantitative evidence is mostly reported through commercial summaries, and the main causal comparison is not independently documented.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S6 — Does Working from Home Increase Productivity? (2026)**
  URL: https://emailanalytics.com/does-working-from-home-increase-productivity
- **S7 — Three-day hybrid work week is success, study published in Nature says**
  URL: https://www.cnbc.com/2024/06/14/three-day-hybrid-work-week-is-success-study-published-in-nature-says.html
- **S8 — (PDF) Hybrid working from home improves retention ...**
  URL: https://www.researchgate.net/publication/381373698_Hybrid_working_from_home_improves_retention_without_damaging_performance
- **S9 — Is Hybrid Work the Best of Both Worlds? Evidence from a ...**
  URL: https://nacmnet.org/wp-content/uploads/Is-Hybrid-Work-the-Best-of-Both-Worlds-Evidence-from-a-Field-Experiment.pdf

**Search Duration:** 3.94s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Additional randomized evidence supports a conditional conclusion: hybrid work can preserve or improve measured performance while improving retention and worker well-being.

**Confidence:** High

**Why this confidence level**

Two distinct field experiments report broadly compatible results for hybrid work, and S9 provides substantially more methodological detail about randomization, sample, setting, and outcomes than the earlier secondary summaries. External validity remains limited.

**Evidence**

- The Trip.com randomized trial covered 1,612 employees and found that two days working from home did not reduce performance, while non-manager attrition fell from 7.2% to 2.4%; satisfaction and work-life-balance measures improved. [S7] [S8]
- A separate field experiment at BRAC randomized office days among 130 administrative workers, with complete data for 108. Intermediate hybrid schedules produced better manager performance ratings, more emails and recipients, and more information conveyed, as well as better work-life balance and less isolation. [S9]

#### Finding 2

**Claim**

The new evidence strengthens the distinction between hybrid work and fully remote work; results for hybrid arrangements should not be generalized to five-day remote work.

**Confidence:** High

**Why this confidence level**

The source directly distinguishes treatment types and summarizes several causal designs, although the cited earlier studies are not included in full here.

**Evidence**

- The Trip.com study tested a two-days-at-home schedule rather than fully remote work and found no performance penalty. [S7] [S9]
- The BRAC experiment randomized the number of office days and found that an intermediate level of office attendance improved communication and manager ratings relative to other schedules. [S9]
- S9 contrasts earlier causal productivity gains from fully remote work in a call center and work-from-anywhere among patent examiners with adverse team effects reported during pandemic-era firm-wide remote work. [S9]

#### Finding 3

**Claim**

Communication and coordination outcomes may explain why individual productivity can appear stable while broader team or organizational productivity differs.

**Confidence:** Medium

**Why this confidence level**

The experiments directly measure communication, ratings, retention, and satisfaction, but neither establishes long-run effects on innovation, firm revenue, or total-factor productivity.

**Evidence**

- The BRAC experiment measured email volume, unique recipients, and information conveyed, finding improved communication under intermediate hybrid work; it also measured isolation and work-life balance. [S9]
- The source summarizes evidence that all-remote pandemic transitions reduced formation of new intrafirm communication ties, while other studies found adverse effects on teams. [S9]
- The Trip.com results show equal performance alongside substantially lower attrition, illustrating that organizational benefits can occur without higher measured individual output. [S7] [S8]

#### Finding 4

**Claim**

The new source improves the explanation for conflicting findings: effects vary with work arrangement, task type, worker selection, and whether researchers measure individual output, communication, retention, or perceptions.

**Confidence:** High

**Why this confidence level**

The sources explicitly identify different populations, treatments, and outcome measures, providing a well-supported explanation for apparently conflicting results.

**Evidence**

- S9 notes that call-center and patent-examiner studies found causal output gains, whereas studies of pandemic-era firm-wide remote work found weaker team communication or lower call counts among workers who originally selected remote jobs. [S9]
- The BRAC sample consisted of HR administrative workers in Bangladesh, while Trip.com involved university-trained knowledge workers in a Chinese technology firm; these settings differ from call centers and IT workers. [S7] [S9]
- The experiments used different outcomes, including calls, manager ratings, email communication, promotions, retention, satisfaction, and isolation, which need not move together. [S7] [S9]

### Conflicts Found

- S6 presents the Stanford/Ctrip evidence as involving 16,000 call-center employees and reports a 22% gain when workers choose their location, whereas the accumulated evidence describes the original randomized Ctrip experiment as involving 249 employees and the later choice phase differently. S6 therefore appears to conflate studies or report figures without sufficient methodological precision. [S1] [S6] [S9]
- S6 claims to find consistent productivity gains from remote work, but the same source acknowledges an 8–19% decline in IT-worker output and no effect in the Trip.com randomized hybrid trial. Its broad conclusion is not consistent with its own cited study summaries or the more detailed experimental evidence. [S6] [S7] [S9]
- The BRAC experiment reports improved communication and manager ratings for an intermediate hybrid schedule, while the Trip.com experiment reports no statistically significant effect on several performance measures. This is a difference in estimated outcomes and settings rather than a clear contradiction, because the studies use different performance measures and treatment schedules. [S7] [S9]

### Important Gaps

- How do these experimental effects translate into company-level outcomes such as revenue, innovation, total-factor productivity, and long-run knowledge accumulation?
- Whether the BRAC communication findings persist beyond the nine-week treatment period is unknown.
- The retrieved evidence does not provide confidence intervals, treatment-compliance details, or complete outcome tables for all experiments.
- How effects differ by occupation, worker seniority, home conditions, managerial practices, and voluntary versus imposed remote work remains unresolved.
- The apparent 16,000-worker figure and 22% choice result in S6 require verification against the primary Ctrip study before being used.

**Analysis Duration:** 15.25s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The controlled-experiment evidence is now reasonably strong for a conditional comparison, especially for hybrid work, but an important part of the original question remains weak: company-level and observational evidence on aggregate productivity. A focused search for primary company-level or quasi-experimental studies would materially improve the answer and help distinguish individual output from firm productivity.

**Next Search**

> primary company-level observational quasi-experimental studies remote work productivity firm productivity revenue innovation total factor productivity

---

# Iteration 3

## 1. Search

**Query**

> primary company-level observational quasi-experimental studies remote work productivity firm productivity revenue innovation total factor productivity

**Why this query**

The controlled-experiment evidence is now reasonably strong for a conditional comparison, especially for hybrid work, but an important part of the original question remains weak: company-level and observational evidence on aggregate productivity. A focused search for primary company-level or quasi-experimental studies would materially improve the answer and help distinguish individual output from firm productivity.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S10 — The Effect of Remote Work on Firm Level Productivity**
  URL: https://cupola.gettysburg.edu/cgi/viewcontent.cgi?article=1079&context=ger
- **S11 — Economic Development Implications of Remote Work in the Post-Pandemic Environment**
  URL: https://www.congress.gov/crs-product/R48528
- **S12 — Winners and losers from remote work: How firm capabilities impact productivity | CEPR**
  URL: https://cepr.org/voxeu/columns/winners-and-losers-remote-work-how-firm-capabilities-impact-productivity

**Search Duration:** 5.40s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

New firm-level evidence supports a conditional, adaptation-dependent effect: pandemic-driven remote work initially reduced productivity in Italy, but the losses disappeared as firms adapted; digitally prepared and larger firms performed better, while firms with highly qualified workers eventually achieved gains.

**Confidence:** Medium

**Why this confidence level**

This is a relevant firm-level result using population-wide administrative coverage and an instrumental-variables strategy described in the source, but the retrieved excerpt does not provide effect sizes, statistical precision, outcome construction, or the complete study results.

**Evidence**

- The CEPR summary reports that Italy-wide data on remote workers show an initial productivity reduction, disappearance of those losses over time, better performance among larger and digitally prepared firms, and later gains among firms with highly qualified workers. [S12]

#### Finding 2

**Claim**

The new firm-level study attempts to address selection into remote work by instrumenting firm-level remote-work adoption with pre-pandemic local fibre-broadband availability.

**Confidence:** Medium

**Why this confidence level**

The source clearly describes the identification design and argues that fibre rollout was determined primarily by geography rather than pre-pandemic local economic conditions, but the excerpt does not provide enough diagnostic or robustness results to assess the instrument fully.

**Evidence**

- S12 says firms with stronger organizational and digital capabilities are more likely to adopt remote work, and describes an identification strategy using pre-pandemic fibre availability, pandemic timing, local labour-market comparisons, and narrow industry controls. [S12]

#### Finding 3

**Claim**

Firm capabilities and complementary investments are central explanations for conflicting productivity findings.

**Confidence:** High

**Why this confidence level**

The new firm-level evidence and prior survey evidence independently point to adaptation and organizational complements as important moderators.

**Evidence**

- S12 concludes that remote-work effects depend on complementary investments in digital technology, organizational capacity, and skills; it also reports that larger and digitally prepared firms weathered the transition better. [S12]
- Prior survey evidence found that productivity perceptions improved as firms invested in technology, training, task redesign, and remote-management practices. [S4]

#### Finding 4

**Claim**

A theoretical firm-level model predicts higher productivity when the share of remote workers rises, but only under a wage condition; this is not direct empirical evidence that remote work raises productivity.

**Confidence:** High

**Why this confidence level**

The source explicitly labels its contribution as theoretical and states the model assumptions and conditional conclusion. Its result should not be weighted like a controlled experiment or observed firm-level estimate.

**Evidence**

- S10 develops a representative-firm theoretical model treating labour as the only production factor and concludes that productivity rises with the remote-to-nonremote worker ratio when remote workers receive higher wages than nonremote workers. [S10]

#### Finding 5

**Claim**

The combined evidence still does not establish a universal effect of remote work on company-level productivity.

**Confidence:** High

**Why this confidence level**

The evidence spans multiple designs and points to heterogeneous effects rather than a single direction, while no source supplies a general estimate applicable across occupations and work arrangements.

**Evidence**

- Controlled experiments in the accumulated record find output gains in a specific fully remote call-center setting, no measured performance penalty under two-days-at-home hybrid work, and improved communication or manager ratings under an intermediate hybrid schedule. [S1] [S7] [S9]
- Firm-level evidence in Italy reports initial losses followed by recovery or gains depending on adaptation and firm capabilities. [S12]
- The theoretical model predicts a positive effect only under specified wage and modelling assumptions. [S10]

#### Finding 6

**Claim**

The new sources strengthen the distinction between individual-level experimental outcomes and firm-level productivity outcomes.

**Confidence:** High

**Why this confidence level**

The sources directly identify different units of analysis and outcome types, which can produce apparently conflicting conclusions even when individual task performance is unchanged.

**Evidence**

- S12 studies productivity at the firm level using administrative data across Italy, whereas the accumulated experiments measure calls, manager ratings, communication, promotions, performance reviews, retention, or satisfaction among selected employee populations. [S1] [S7] [S9] [S12]
- S10 explicitly models firm-level productivity but does not observe it empirically. [S10]

### Conflicts Found

- S12's reported initial firm-level productivity losses contrast with positive or neutral results from several controlled experiments. The difference is conditional rather than necessarily contradictory: S12 concerns pandemic-era, economy-wide adoption and firm adaptation, while the experiments concern particular firms, occupations, and scheduled hybrid arrangements. [S1] [S7] [S9] [S12]
- S10 predicts that a higher remote-worker share increases firm productivity under the assumption that remote workers are paid higher wages, whereas S12 reports initial productivity losses and heterogeneous recovery. The disagreement reflects a theoretical conditional prediction versus empirical evidence under different real-world conditions and assumptions. [S10] [S12]
- S12 emphasizes that larger and digitally capable firms perform better with remote work, while the accumulated survey evidence reports greater monitoring and learning concerns in larger firms. These findings may reflect different outcomes, periods, or measures of capability and are not directly reconciled in the retrieved material. [S4] [S12]

### Important Gaps

- What are the estimated magnitudes, confidence intervals, and complete outcome definitions in the Italian firm-level study summarized by S12?
- Does the Italian identification strategy isolate remote work itself, or partly capture the broader effects of broadband availability and digital capability?
- Which firm-level outcomes were measured in S12—such as revenue, value added, employment-adjusted productivity, innovation, or total-factor productivity—and over what period?
- How do the Italy-wide firm-level results generalize to other countries, occupations, and post-pandemic conditions?
- The retrieved S11 content contains navigation and metadata but no substantive evidence about remote-work productivity, so it does not resolve the company-level evidence gap.
- The new evidence does not resolve long-run effects on innovation, mentoring, onboarding, knowledge accumulation, or organizational communication.

**Analysis Duration:** 15.51s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

Another search would materially improve the answer by locating the primary Boeri et al. firm-level study behind S12 and extracting its sample, estimates, identification diagnostics, and measured productivity outcomes. This is the most important remaining gap because the original question specifically asks for company-level data, and S12 currently provides only a summary.

**Next Search**

> Boeri Crescenzi Rigo 2025 remote work firm productivity Italy fibre broadband administrative data paper

---

# Iteration 4

## 1. Search

**Query**

> Boeri Crescenzi Rigo 2025 remote work firm productivity Italy fibre broadband administrative data paper

**Why this query**

Another search would materially improve the answer by locating the primary Boeri et al. firm-level study behind S12 and extracting its sample, estimates, identification diagnostics, and measured productivity outcomes. This is the most important remaining gap because the original question specifically asks for company-level data, and S12 currently provides only a summary.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S13 — Professor Riccardo Crescenzi, Doctor Filippo Boeri, ...**
  URL: https://committees.parliament.uk/writtenevidence/141059/pdf
- **S14 — Work from Home and Firm Productivity: The Role of ICT ...**
  URL: https://openaccess.city.ac.uk/id/eprint/36254
- **S15 — Work from Home and Firm Productivity: The Role of ICT and Size**
  URL: https://ideas.repec.org/p/ces/ceswps/_12253.html
- **S16 — Work from Home and Firm Productivity: The Role of ICT and Size by Filippo Boeri, Riccardo Crescenzi, Davide Rigo :: SSRN**
  URL: https://papers.ssrn.com/sol3/Delivery.cfm/12253.pdf?abstractid=5737804&mirid=1
- **S17 — Work from Home and Firm Productivity: The Role of ICT and Size by Filippo Boeri, Riccardo Crescenzi, Davide Rigo :: SSRN**
  URL: https://papers.ssrn.com/sol3/Delivery.cfm/12253.pdf?abstractid=5737804&mirid=1&type=2

**Search Duration:** 7.50s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources independently confirm the Italian firm-level finding: work from home had a large negative effect on firm productivity during the pandemic, but the effect was no longer statistically significant in the longer term.

**Confidence:** High

**Why this confidence level**

Three records reproduce the same study abstract and conclusion. However, they are not independent studies; they are different listings of one working paper.

**Evidence**

- The paper’s abstract states that WFH reduced productivity substantially during the pandemic, while the longer-term effect was no longer significant. [S15] [S16] [S17]

#### Finding 2

**Claim**

Firm size and prior ICT investment moderated the negative productivity effect of WFH, while firms employing highly qualified workers showed suggestive longer-term productivity gains.

**Confidence:** High

**Why this confidence level**

The result is consistently stated in the paper’s abstract across multiple source records, though the evidence is still an abstract-level summary without estimates or robustness tables.

**Evidence**

- The paper reports that larger firms and firms with prior ICT investments mitigated pandemic productivity losses, and that highly qualified-worker firms may have experienced productivity gains. [S15] [S16] [S17]

#### Finding 3

**Claim**

The Italian study uses firm-level administrative data and an instrumental-variable strategy based on pre-pandemic firm-specific access to fibre broadband to address selection into WFH.

**Confidence:** Medium

**Why this confidence level**

The identification strategy and data source are clearly described, but the retrieved content does not show first-stage strength, exclusion-restriction tests, or sensitivity analyses.

**Evidence**

- The abstract says the study covers the universe of remote workers in Italy and instruments post-pandemic WFH adoption with exogenous pre-pandemic variation in firm-specific fibre-broadband access. [S15] [S16] [S17]

#### Finding 4

**Claim**

The new firm-level evidence strengthens, rather than overturns, the conditional conclusion that remote work’s productivity effect depends on timing, firm capabilities, and the distinction between individual and company-level outcomes.

**Confidence:** High

**Why this confidence level**

The contrast is directly supported across experimental and firm-level evidence and provides a coherent conditional explanation rather than a universal direction.

**Evidence**

- The Italian study finds short-run firm-level losses but longer-run recovery, with heterogeneous effects by size, ICT investment, and worker qualification; the accumulated experiments find neutral or positive individual-level outcomes in specific hybrid or fully remote settings. [S1] [S7] [S9] [S15] [S16]

### Conflicts Found

- The new paper’s pandemic-era firm-level negative effect differs from positive or neutral results in several controlled experiments. The studies are not necessarily contradictory: the firm-level study concerns economy-wide pandemic adoption and aggregate firm productivity, whereas the experiments concern selected workers, occupations, and specific remote or hybrid schedules. [S1] [S7] [S9] [S15] [S16]
- The Italian study reports no significant longer-term average effect but suggestive gains for firms with highly qualified workers. This qualifies—not directly contradicts—the broader experimental evidence of neutral or positive effects, because the subgroup result is heterogeneous and described as suggestive. [S15] [S16] [S17]

### Important Gaps

- What are the exact effect sizes, confidence intervals, productivity definitions, and time horizons in the Italian study?
- How strong is the fibre-broadband instrument, and does it isolate WFH adoption from broader digital capability or broadband-related productivity effects?
- Which company-level outcomes were used—such as value added per worker, revenue, employment-adjusted productivity, or total-factor productivity—and how do they compare with individual output measures?
- The retrieved material still provides limited direct evidence on long-run innovation, onboarding, mentoring, knowledge accumulation, and organizational communication.

**Analysis Duration:** 11.98s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The main qualitative conclusion is now well supported, but a focused retrieval of the full Italian paper could materially improve the company-level comparison by supplying effect sizes, outcome definitions, precision, and identification diagnostics. This is the most important remaining evidence gap.

**Next Search**

> Boeri Crescenzi Rigo 2025 WFH firm productivity Italy effect sizes confidence intervals fibre broadband instrument results

---

# Iteration 5

## 1. Search

**Query**

> Boeri Crescenzi Rigo 2025 WFH firm productivity Italy effect sizes confidence intervals fibre broadband instrument results

**Why this query**

The main qualitative conclusion is now well supported, but a focused retrieval of the full Italian paper could materially improve the company-level comparison by supplying effect sizes, outcome definitions, precision, and identification diagnostics. This is the most important remaining evidence gap.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S18 — How to Interpret Effect Sizes and Confidence Intervals**
  URL: https://academiquirk.com/article/effect-sizes-confidence-intervals-quick-guide
- **S19 — Guide to Effect Sizes and Confidence Intervals**
  URL: https://matthewbjane.quarto.pub/guide-to-effect-sizes-and-confidence-intervals
- **S20 — Evidence from the COVID-19 pandemic**
  URL: https://hoover-s3-website.s3.us-west-2.amazonaws.com/s3fs-public/2023-11/WFH_Covid19_firms_Stanford.pdf
- **S21 — Guide for Calculating and Interpreting Effect Sizes and Confidence Intervals in Intellectual and...**
  URL: https://www.researchgate.net/publication/224834353_Guide_for_calculating_and_interpreting_effect_sizes_and_confidence_intervals_in_intellectual_and_developmental_disability_research_studies

**Search Duration:** 5.05s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources do not materially change the substantive evidence on whether remote work affects productivity.

**Confidence:** High

**Why this confidence level**

The retrieved content contains no new remote-work productivity estimates or outcomes; the methodological sources are off-topic for the substantive question.

**Evidence**

- S18 and S19 are general methodological guides about effect sizes and confidence intervals, not studies of remote work or employee productivity. [S18] [S19]
- S21 discusses interpreting effect sizes and statistical significance in unrelated research contexts and provides no remote-work findings. [S21]
- S20 contains only a brief conference/PDF snippet mentioning the Italy remote-work study and broadband, without results, estimates, or methodological detail beyond what is already represented in the accumulated evidence. [S20]

#### Finding 2

**Claim**

The accumulated evidence continues to support a conditional rather than universal conclusion: hybrid work generally preserves measured individual performance, while fully remote work can either raise or reduce output depending on occupation, task interdependence, and firm capability.

**Confidence:** High

**Why this confidence level**

Evidence from multiple controlled experiments and firm-level analyses converges on heterogeneous effects, although the settings and outcomes differ.

**Evidence**

- Randomized studies report higher output in a specific fully remote call-center setting, no detectable performance loss under a two-days-at-home hybrid arrangement, and improved communication or manager ratings under an intermediate hybrid schedule. [S1] [S7] [S9]
- Italian firm-level evidence reports substantial short-run productivity losses during pandemic adoption, followed by recovery or gains for firms with stronger digital preparation, larger scale, or highly qualified workers. [S12] [S15] [S16] [S17]

#### Finding 3

**Claim**

Differences in statistical significance or reported effect sizes should not be treated as decisive without effect magnitudes, confidence intervals, outcome definitions, and study design information.

**Confidence:** High

**Why this confidence level**

The methodological point is directly stated in the new sources, and the evidence gaps are documented in the research state.

**Evidence**

- The new methodological sources emphasize that effect sizes indicate magnitude and confidence intervals indicate precision, whereas p-values alone do not establish practical importance. [S18] [S19] [S21]
- The accumulated remote-work evidence often lacks complete effect estimates, confidence intervals, compliance information, and precise productivity definitions, particularly in the retrieved summaries of the Italian study and some experiments. [S1] [S7] [S9] [S12] [S15] [S16] [S17]

### Conflicts Found

- No new substantive source conflict was introduced. S20's brief mention of the Italian study is consistent with, but too incomplete to independently verify, the already accumulated firm-level finding of pandemic-era productivity losses and broadband-based identification. [S12] [S15] [S16] [S17] [S20]

### Important Gaps

- What are the exact effect sizes, confidence intervals, productivity measures, and time horizons in the Italian firm-level study?
- How strong is the fibre-broadband instrument, and does it isolate remote-work adoption from broader digital capability and broadband-related productivity effects?
- What are the long-run effects on innovation, onboarding, mentoring, knowledge accumulation, and company-level productivity?
- How do experimental individual-output effects translate into firm outcomes such as value added, revenue, employment-adjusted productivity, or total-factor productivity?
- How generalizable are the results across occupations, countries, voluntary versus imposed remote work, and post-pandemic conditions?

**Analysis Duration:** 9.91s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources are largely irrelevant or insufficiently detailed. A focused search for the primary Italian firm-level paper and its full estimates would materially improve the comparison between company-level and experimental evidence, which remains the main evidence gap.

**Next Search**

> Boeri Crescenzi Rigo remote work firm productivity Italy fibre broadband working paper full text effect estimates confidence intervals

---

# Iteration 6

## 1. Search

**Query**

> Boeri Crescenzi Rigo remote work firm productivity Italy fibre broadband working paper full text effect estimates confidence intervals

**Why this query**

The new sources are largely irrelevant or insufficiently detailed. A focused search for the primary Italian firm-level paper and its full estimates would materially improve the comparison between company-level and experimental evidence, which remains the main evidence gap.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S22 — Winners and losers from remote work: How firm capabilities ...**
  URL: https://x.com/nodeskco/status/2024061422838173719
- **S23 — Work from Home and Firm Productivity: The Role of ICT ...**
  URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5737804
- **S24 — Work From Home and Firm Productivity: The Role of ICT ...**
  URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6560094

**Search Duration:** 7.21s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources do not materially change the substantive conclusion: remote work has heterogeneous productivity effects that depend on firm capabilities, ICT investment, firm size, timing, and work arrangement.

**Confidence:** High

**Why this confidence level**

The sources are directly relevant by title and description but add no usable quantitative or methodological findings beyond the accumulated evidence.

**Evidence**

- S22 points to the previously identified CEPR study on firm capabilities and productivity but provides only a title and date, with no substantive results. [S22]
- S23 identifies the Boeri et al. paper as estimating work-from-home effects on firm productivity and using fibre broadband as an instrument, but the retrieved excerpt does not report estimates or conclusions. [S23]
- S24 describes a related paper as estimating the causal effect of WFH adoption on firm productivity in the post-pandemic period, but gives no results or outcome details. [S24]

#### Finding 2

**Claim**

The new sources suggest that the Boeri et al. research may include a post-pandemic analysis, potentially extending the earlier evidence beyond the pandemic shock, but this cannot be established from the excerpts alone.

**Confidence:** Low

**Why this confidence level**

The snippets do not establish whether S23 and S24 are different versions, extensions, or closely related records, nor do they provide the sample period, estimates, or findings.

**Evidence**

- S24 explicitly describes estimation of WFH adoption effects in the post-pandemic period. [S24]
- S23 identifies a 2025 working paper concerning the role of ICT and firm size and mentions fibre broadband as an instrument. [S23]

### Conflicts Found

- No new substantive disagreement is introduced. The titles and snippets in S22–S24 are compatible with the accumulated finding that firm capabilities and timing moderate WFH productivity effects, but they do not independently verify the direction or magnitude of those effects. [S12] [S15] [S16] [S17] [S22] [S23] [S24]

### Important Gaps

- Whether S23 and S24 are distinct studies or versions of the same Boeri et al. research.
- Whether the post-pandemic analysis finds a positive, negative, or null average effect of WFH on firm productivity.
- The exact firm-level productivity outcome, sample period, effect size, confidence interval, and robustness checks in S23 and S24.
- Whether the fibre-broadband instrument isolates WFH adoption from broader digital capability and broadband-related productivity effects.
- Whether post-pandemic results differ from the reported pandemic-era productivity losses and longer-term average null effect.

**Analysis Duration:** 9.15s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The central company-level evidence gap remains important: the new records indicate potentially relevant post-pandemic causal evidence but provide no results. A primary-paper search could materially clarify whether firm productivity effects persist after the pandemic and provide the missing magnitudes and outcome definitions.

**Next Search**

> "Work from Home and Firm Productivity" Boeri Crescenzi Rigo post-pandemic results estimates

---

# Iteration 7

## 1. Search

**Query**

> "Work from Home and Firm Productivity" Boeri Crescenzi Rigo post-pandemic results estimates

**Why this query**

The central company-level evidence gap remains important: the new records indicate potentially relevant post-pandemic causal evidence but provide no results. A primary-paper search could materially clarify whether firm productivity effects persist after the pandemic and provide the missing magnitudes and outcome definitions.

**Results**

5 results retrieved.

1 new unique source added.

### Sources

- **S25 — Filippo Boeri's research works | City St George's, University ...**
  URL: https://www.researchgate.net/scientific-contributions/Filippo-Boeri-2167640130

**Search Duration:** 6.02s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

S25 provides no substantive new estimate of remote work’s productivity effect; it only indicates that a paper estimates the causal effect of post-pandemic work-from-home adoption on firm productivity using administrative firm-level data.

**Confidence:** Medium

**Why this confidence level**

The source is directly relevant by description, but the excerpt is incomplete and does not report results.

**Evidence**

- The available excerpt states that the paper estimates the causal effect of WFH adoption on firm productivity in the post-pandemic period using administrative firm-level data, but gives no direction, magnitude, outcome definition, or precision. [S25]

#### Finding 2

**Claim**

S25 is consistent with, but does not independently verify, the accumulated conclusion that company-level remote-work effects may differ from individual-level experimental effects and may vary between pandemic and post-pandemic periods.

**Confidence:** Medium

**Why this confidence level**

The difference in study period and unit of analysis is clear, but S25 does not reveal whether its result is positive, negative, or null.

**Evidence**

- S25 concerns post-pandemic firm-level productivity, while the accumulated evidence includes individual-level experiments and an Italian firm-level study reporting pandemic losses followed by longer-term recovery or null average effects. [S25] [S7] [S9] [S12] [S15] [S16] [S17]

### Conflicts Found

- No new substantive conflict is introduced. S25’s brief description is compatible with the existing evidence but does not report findings that can be compared with the experimental or Italian firm-level results. [S25] [S12] [S15] [S16] [S17]

### Important Gaps

- What is the direction and magnitude of the post-pandemic firm-level WFH productivity effect in S25?
- Which productivity measure is used, over what sample period, and with what confidence intervals or robustness checks?
- Is S25 a distinct post-pandemic study or another listing/version of the Boeri et al. research already represented by S23 and S24?
- Does its identification strategy adequately separate WFH adoption from broader digital capability, broadband access, or firm selection effects?

**Analysis Duration:** 6.85s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The original question can already be answered responsibly with a conditional conclusion, but company-level evidence—especially post-pandemic firm productivity—is an important part of the requested comparison. S25 signals potentially relevant evidence without supplying the result, so one focused search could materially improve the answer.

**Next Search**

> "causal effect of work from home adoption on firm productivity" post-pandemic Boeri

---

# Iteration 8

## 1. Search

**Query**

> "causal effect of work from home adoption on firm productivity" post-pandemic Boeri

**Why this query**

The original question can already be answered responsibly with a conditional conclusion, but company-level evidence—especially post-pandemic firm productivity—is an important part of the requested comparison. S25 signals potentially relevant evidence without supplying the result, so one focused search could materially improve the answer.

**Results**

5 results retrieved.

1 new unique source added.

### Sources

- **S26 — Work From Home and Firm Productivity: The Role of ICT and Size**
  URL: https://www.researchgate.net/publication/403752684_Work_From_Home_and_Firm_Productivity_The_Role_of_ICT_and_Size

**Search Duration:** 3.39s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

S26 identifies a post-pandemic firm-level study that estimates the causal effect of work-from-home adoption on firm productivity, with particular attention to ICT and firm size.

**Confidence:** Medium

**Why this confidence level**

The source directly describes the study’s research question and causal framing, but provides no results, productivity measure, sample period, identification details, or statistical precision.

**Evidence**

- The source title emphasizes ICT and firm size, and its description states that it estimates the causal effect of post-pandemic WFH adoption on firm productivity. [S26]

#### Finding 2

**Claim**

S26 does not materially change the substantive conclusion that remote work’s productivity effects are heterogeneous and depend on firm capabilities and context.

**Confidence:** Medium

**Why this confidence level**

The thematic consistency is clear, but S26 contributes no empirical estimate that can independently confirm the earlier Italian findings.

**Evidence**

- S26’s focus on ICT and firm size is consistent with accumulated evidence that digital preparation and firm scale moderate WFH productivity effects, but the excerpt does not report whether the post-pandemic effect is positive, negative, or null. [S26] [S12] [S15] [S16] [S17]

### Conflicts Found

- No substantive conflict is introduced. S26 is compatible with the existing firm-level evidence but does not disclose the direction or magnitude of its post-pandemic productivity estimate. [S26] [S12] [S15] [S16] [S17]

### Important Gaps

- What is the direction and magnitude of the post-pandemic WFH productivity effect in S26?
- Which firm-level productivity measure is used, and over what sample period?
- What identification strategy, instrument, treatment definition, confidence intervals, and robustness checks does S26 use?
- Is S26 a distinct study or another version of the Boeri et al. research already represented by S23–S25?
- Does the post-pandemic result differ from the reported pandemic-era losses and longer-term average null effect?

**Analysis Duration:** 6.26s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The original question specifically asks for comparison with company-level data. S26 appears potentially important because it addresses post-pandemic firm productivity causally, but the retrieved content contains no usable result. A focused search for the paper’s abstract or full text could materially resolve the direction, magnitude, and relationship to the earlier Italian study.

**Next Search**

> "Work From Home and Firm Productivity: The Role of ICT and Size" results estimate post-pandemic

---

# Iteration 9

## 1. Search

**Query**

> "Work From Home and Firm Productivity: The Role of ICT and Size" results estimate post-pandemic

**Why this query**

The original question specifically asks for comparison with company-level data. S26 appears potentially important because it addresses post-pandemic firm productivity causally, but the retrieved content contains no usable result. A focused search for the paper’s abstract or full text could materially resolve the direction, magnitude, and relationship to the earlier Italian study.

**Results**

5 results retrieved.

1 new unique source added.

### Sources

- **S27 — Work from Home and Firm Productivity: The Role of ICT and Size - ifo Institut**
  URL: https://www.ifo.de/en/cesifo/publications/2025/working-paper/work-home-and-firm-productivity-role-ict-and-size

**Search Duration:** 3.13s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

S27 identifies a post-pandemic firm-level study examining the relationship between work-from-home adoption and firm productivity, with attention to ICT and firm size.

**Confidence:** Medium

**Why this confidence level**

S27 directly identifies the research question and firm-level design, but the available content provides no direction, magnitude, productivity measure, identification details, or precision.

**Evidence**

- The source title emphasizes ICT and firm size, and its description states that the paper investigates the impact of post-pandemic WFH adoption on firm productivity using administrative firm-level data. [S27]

#### Finding 2

**Claim**

S27 does not materially change the substantive conclusion that remote-work productivity effects are heterogeneous and may depend on firm capabilities, ICT investment, size, and period.

**Confidence:** Medium

**Why this confidence level**

The thematic consistency is clear, but the source excerpt is too incomplete to establish whether the post-pandemic average effect is positive, negative, or null.

**Evidence**

- The ICT-and-size focus is consistent with the accumulated Italian evidence that digital preparation and firm size moderate WFH productivity effects, but S27 does not report empirical results that independently confirm or revise those findings. [S27] [S12] [S15] [S16] [S17]

### Conflicts Found

- No substantive new conflict is introduced. S27 is compatible with the existing firm-level evidence but does not disclose results that can be compared with the controlled experiments or the reported pandemic-era Italian productivity losses. [S27] [S7] [S9] [S12] [S15] [S16] [S17]

### Important Gaps

- What is the direction and magnitude of S27's post-pandemic WFH productivity effect?
- Which firm-level productivity measure, sample period, treatment definition, and identification strategy does S27 use?
- What are the confidence intervals and robustness checks, and does the design separate WFH adoption from broader ICT capability or firm selection?
- Is S27 a distinct study or another version of the Boeri et al. research already represented by S23–S26?
- Does the post-pandemic estimate differ from the reported pandemic-era losses and longer-term average null effect?

**Analysis Duration:** 6.61s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The original question specifically asks for comparison with company-level data. S27 confirms that relevant post-pandemic firm-level research exists but supplies no result, so a primary-paper or full-text search could materially improve the answer by resolving the direction, size, and credibility of that estimate.

**Next Search**

> "Work from Home and Firm Productivity: The Role of ICT and Size" full text results estimates Boeri Crescenzi Rigo

---

# Iteration 10

## 1. Search

**Query**

> "Work from Home and Firm Productivity: The Role of ICT and Size" full text results estimates Boeri Crescenzi Rigo

**Why this query**

The original question specifically asks for comparison with company-level data. S27 confirms that relevant post-pandemic firm-level research exists but supplies no result, so a primary-paper or full-text search could materially improve the answer by resolving the direction, size, and credibility of that estimate.

**Results**

5 results retrieved.

0 new unique sources added.

### Sources

No new unique sources were added.

**Search Duration:** 5.42s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Remote work does not have a universal productivity effect; the best-supported conclusion is conditional on work arrangement, task type, worker population, firm capabilities, and time period.

**Confidence:** High

**Why this confidence level**

Evidence from multiple experimental and firm-level designs consistently indicates heterogeneous rather than uniformly positive or negative effects.

**Evidence**

- Controlled experiments report positive output in a specific fully remote call-center setting, no measurable performance loss under a two-days-at-home hybrid schedule, and improved communication or manager ratings under an intermediate hybrid schedule. [S1] [S7] [S9]
- Firm-level Italian evidence reports substantial short-run productivity losses during pandemic adoption, followed by recovery or gains for firms with stronger digital preparation, larger scale, or highly qualified workers. [S12] [S15] [S16] [S17]

#### Finding 2

**Claim**

Controlled experiments generally support hybrid work as preserving measured individual performance while improving retention and worker well-being, but fully remote results are more context-dependent.

**Confidence:** High

**Why this confidence level**

Two field experiments directly support neutral or positive hybrid effects, while the fully remote positive result is confined to a specific call-center setting.

**Evidence**

- The Trip.com randomized trial found no significant difference in performance reviews, promotions, coding, revenue, or hours under a two-days-at-home hybrid arrangement, while resignations fell by 33%. [S1] [S7] [S8]
- The BRAC field experiment found that an intermediate hybrid schedule improved manager ratings, email communication, information conveyed, work-life balance, and isolation outcomes among administrative workers. [S9]
- The earlier Ctrip call-center experiment reported 13.5% more calls under mostly home-based work, alongside higher satisfaction and lower attrition. [S1]

#### Finding 3

**Claim**

Observational and survey evidence often reports stable or improving perceived productivity, but these studies cannot by themselves establish that remote work caused the improvement.

**Confidence:** Medium

**Why this confidence level**

The survey evidence is informative about perceptions and adaptation but remains vulnerable to selection, reporting, and changing-period biases; the BLS result lacks methodological detail.

**Evidence**

- An HBS working paper reports that many small-business owners perceived an initial productivity decline in early 2020 but that the median owner reported a positive effect by early 2021 after adaptation. [S4]
- The same study attributes improvement partly to technology investment, training, task redesign, and improved remote-management practices, while documenting continuing monitoring and learning difficulties. [S4]
- A reported BLS analysis finds a positive association between remote-work adoption and total-factor-productivity growth, but the retrieved material does not establish its causal identification. [S2]

#### Finding 4

**Claim**

Company-level evidence points to short-run losses during forced, economy-wide pandemic adoption, with effects attenuating or reversing as firms adapt; this differs from the mostly neutral or positive individual-level experimental results because the unit and context differ.

**Confidence:** Medium

**Why this confidence level**

The result is consistently reported across records of the study, but the available evidence is abstract-level and omits effect sizes, confidence intervals, outcome construction, and key identification diagnostics.

**Evidence**

- The Italian administrative-data study reports a large pandemic-period reduction in firm productivity, no statistically significant longer-term average effect, and better outcomes among larger, digitally prepared, or highly qualified-worker firms. [S12] [S15] [S16] [S17]
- The study uses pre-pandemic firm-specific fibre-broadband access as an instrument for WFH adoption, attempting to address selection into remote work, though the retrieved material does not report first-stage strength or full robustness results. [S12] [S15] [S16] [S17]

#### Finding 5

**Claim**

Different studies reach conflicting conclusions mainly because they study different treatments, tasks, populations, outcomes, and stages of adaptation.

**Confidence:** High

**Why this confidence level**

The sources directly document variation in treatment design, populations, outcomes, and timing, providing a coherent explanation for apparently contradictory findings.

**Evidence**

- Focused individual output can improve remotely, whereas collaboration, onboarding, mentoring, knowledge sharing, and creative problem-solving may require more coordination and can suffer under fully remote arrangements. [S1] [S3] [S9]
- The experiments measure calls, ratings, coding, promotions, communication, retention, satisfaction, and isolation, while the Italian study measures firm-level productivity; these outcomes need not move together. [S1] [S7] [S9] [S12]
- Pandemic-era forced transitions occurred before firms had fully invested in technology, training, task redesign, and remote-management practices, whereas later or deliberately designed hybrid treatments occurred under more stable conditions. [S4] [S12] [S15] [S16] [S17]

#### Finding 6

**Claim**

Remote work can improve organizational outcomes through retention and worker satisfaction even when measured individual productivity is unchanged; conversely, individual output measures may miss longer-run costs involving communication, innovation, onboarding, and learning.

**Confidence:** Medium

**Why this confidence level**

Retention and well-being effects are directly reported, but the longer-run company-level consequences remain unresolved.

**Evidence**

- The Trip.com experiment found equivalent measured performance but substantially lower attrition and improved satisfaction and work-life balance. [S7] [S8]
- The BRAC experiment measured communication and isolation outcomes, while the retrieved evidence does not establish long-run effects on innovation, mentoring, or firm productivity. [S9]

### Conflicts Found

- The fully remote Ctrip call-center experiment reported a 13.5% increase in calls, while another reported source describes 10–20% lower output for some fully remote, highly collaborative, or newly hired roles. This is a conditional disagreement across occupations and role requirements, not necessarily a direct contradiction. [S1]
- The Italian firm-level study reports pandemic-era productivity losses, contrasting with positive or neutral controlled-experiment results. The difference likely reflects economy-wide forced adoption and firm-level adjustment costs versus selected workers in specific occupations and deliberately assigned schedules. [S1] [S7] [S9] [S12] [S15] [S16]
- Early pandemic owner perceptions were negative, while later perceptions became positive. This reflects different adaptation stages rather than necessarily inconsistent estimates of the same steady-state effect. [S4]
- The BRAC experiment reports communication and manager-rating improvements under intermediate hybrid work, whereas Trip.com finds no significant change in several performance measures. The studies use different schedules, settings, samples, and outcomes. [S7] [S9]
- S6 presents inconsistent Ctrip figures and claims broadly consistent productivity gains while also acknowledging negative or null findings. Its summaries should not be relied upon without verification against primary studies. [S6] [S7] [S9]

### Important Gaps

- The retrieved material does not provide complete primary-study estimates, confidence intervals, treatment compliance, or outcome tables for all experiments.
- The exact effect sizes, productivity definitions, time horizons, and robustness checks for the Italian firm-level study remain unavailable.
- It is unclear how strongly the fibre-broadband instrument separates WFH adoption from broader digital capability and broadband-related productivity effects.
- Direct evidence remains limited on firm-level revenue, value added, total-factor productivity, innovation, onboarding, mentoring, and long-run knowledge accumulation.
- The generalizability of the findings across countries, occupations, worker seniority, home conditions, management practices, and voluntary versus imposed remote work remains uncertain.
- The post-pandemic firm-level studies identified in S23–S27 may be versions of the same research, and their empirical direction and magnitude are not reported.

**Analysis Duration:** 16.86s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The runner reached the maximum research iteration budget. Analyzer assessment: The central conditional conclusion is already supportable, so further searching is not needed merely to find more examples. However, one important evidence gap remains: direct, quantitative company-level estimates—especially post-pandemic results—with clearly defined productivity outcomes, confidence intervals, and identification diagnostics would materially improve the comparison requested by the question.

**Stop Reason:** max_iterations

---

# Final Research Decision

**Research Stopped Because**

The runner reached the maximum research iteration budget.

**Stop Reason:** max_iterations

**Searches Performed:** 10

**Unique Sources:** 27

**Remaining Uncertainty**

- Exact effect sizes, confidence intervals, treatment compliance, and complete outcome tables are unavailable for several controlled experiments.
- The Italian firm-level study’s precise productivity measure, estimates, time horizons, and identification diagnostics remain unavailable.
- Direct evidence is limited on company-level revenue, value added, total-factor productivity, innovation, onboarding, mentoring, and long-run knowledge accumulation.
- It remains unclear how experimental individual-output effects translate into aggregate firm outcomes.
- Generalizability across countries, occupations, worker seniority, home conditions, management practices, and voluntary versus imposed remote work is uncertain.
- The post-pandemic firm-level records S23–S27 may represent versions of the same Boeri et al. research; their empirical direction and magnitude are not reported.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 10 | 50.88s |
| OpenAI Analysis | 10 | 118.26s |
| Report Generation | 1 | 18.02s |
| Total Run | — | 187.16s |
