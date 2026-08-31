# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

Can carbon capture and storage make a significant contribution to reducing global CO₂ emissions? Evaluate its demonstrated effectiveness, costs, scalability, energy requirements, and major arguments for and against large-scale deployment.

**Status:** Completed

**Stop Reason:** sufficient_evidence

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 2 / 3

**Unique Sources:** 10

**OpenAI Calls:** 3

**Tavily Calls:** 2

**Started:** 2026-08-31T16:54:57-04:00

**Ended:** 2026-08-31T16:56:27-04:00

**Total Runtime:** 90.35s

---

# Iteration 1

## 1. Search

**Query**

> Can carbon capture and storage make a significant contribution to reducing global CO₂ emissions? Evaluate its demonstrated effectiveness, costs, scalability, energy requirements, and major arguments for and against large-scale deployment.

**Why this query**

This is the user's original research question.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S1 — Carbon capture and storage: An evidence-based review of its limitations and missed promises**
  URL: https://www.sciencedirect.com/science/article/pii/S2096249525000973
- **S2 — Carbon Capture and Storage (CCS): The Future of Climate Change Mitigation - Verde AgriTech - Blog (english)**
  URL: https://blog.verde.ag/en/carbon-capture-and-storage-ccs
- **S3 — Carbon Capture**
  URL: https://www.c2es.org/content/carbon-capture
- **S4 — 7 Things to Know About Carbon Capture, Utilization and ...**
  URL: https://www.wri.org/insights/carbon-capture-technology
- **S5 — A Vision for Carbon Capture, Utilisation, and Storage in the EU – Clean Air Task Force**
  URL: https://www.catf.us/resource/a-vision-carbon-capture-utilisation-and-storage-eu

**Search Duration:** 2.90s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

CCS is currently making only a small demonstrated contribution to global emissions reduction, despite a substantial project pipeline.

**Confidence:** Medium

**Why this confidence level**

The small current global contribution is reported by two sources, but project counts and dates differ, and the sources do not provide a single independently verified current capacity dataset.

**Evidence**

- A 2023 WRI explainer states that CCUS captures around 0.1% of global emissions, approximately 50 million tonnes of CO₂, while 1.5°C scenarios indicate roughly 1 billion tonnes by 2030 and several billion tonnes by 2050. [S4]
- A 2026 peer-reviewed review likewise reports that CCS captures and stores less than 0.1% of annual global CO₂ emissions, despite more than $40 billion in global investment. [S1]
- C2ES reports 30 commercial-scale projects operating, 11 under construction, and 153 at various development stages, although its figures are from an earlier snapshot and are more optimistic than the WRI and review assessments of current impact. [S3]

#### Finding 2

**Claim**

Capture performance can be high at individual facilities, but demonstrated effectiveness does not automatically translate into equivalent net climate reductions.

**Confidence:** Medium

**Why this confidence level**

The sources support a clear distinction between facility capture rates and whole-system climate performance, but the supplied material lacks project-by-project measured capture, energy-penalty and leakage data.

**Evidence**

- C2ES states that capture technologies can capture more than 90% of CO₂ emissions from power plants and industrial facilities and identifies commercial operation in natural-gas processing, fertilizer, ethanol, refinery hydrogen, coal gasification and coal-fired power generation. [S3]
- The review describes recurring problems including suboptimal capture rates, cost overruns, geological uncertainties and projects whose claimed success falls short when assessed for durability, scale and emissions-offset claims; it discusses Petra Nova, Gorgon, Sleipner and In Salah. [S1]
- WRI emphasizes that storage permanence varies by use: geological storage and some concrete applications can be permanent, whereas synthetic fuels re-release the CO₂ when burned. [S4]

#### Finding 3

**Claim**

CCS has a stronger strategic case in hard-to-abate industrial sectors and for some forms of carbon dioxide removal than as a general justification for continued fossil-fuel use.

**Confidence:** Medium

**Why this confidence level**

Multiple sources converge on sectoral targeting and the distinction between CCS and removal, but the case for sector-specific cost advantage is asserted rather than demonstrated quantitatively in the retrieved text.

**Evidence**

- The review recommends strategically targeted deployment in sectors such as cement and legacy industrial retrofits where alternatives are limited. [S1]
- The EU CCUS vision identifies cement, lime, chemicals, steel and waste incineration as sectors with process or high-temperature emissions that may be difficult to eliminate through electrification or alternative fuels alone. [S5]
- The same report identifies BECCS and direct-air capture with geological storage as potential sources of permanent atmospheric carbon removal, including for residual emissions and historical emissions. [S5]
- WRI distinguishes source capture from atmospheric carbon removal and states that emissions reductions should provide the vast majority of mitigation, with removals addressing a smaller residual share. [S4]

#### Finding 4

**Claim**

Large-scale CCS would require a rapid and very substantial expansion from today’s level, involving capture facilities, transport networks and durable storage.

**Confidence:** Medium

**Why this confidence level**

The scale gap is consistently described, but the figures are scenario requirements rather than demonstrated feasible capacity, and the sources do not establish whether storage, transport, materials or workforce constraints would bind first.

**Evidence**

- WRI contrasts current capture of about 50 MtCO₂ per year with scenario requirements of about 1 Gt by 2030 and several billion tonnes by 2050. [S4]
- The EU working-group report estimates that the EU may need to capture, use or store 300–640 MtCO₂ annually by 2050, including at least 150 Mt/year of atmospheric or biogenic-origin CO₂ stored for removal. [S5]
- The report presents a global IPCC-based median of 665 Gt of CO₂ captured and stored cumulatively by 2100 in a 1.5°C-compatible scenario. [S5]

#### Finding 5

**Claim**

Costs and energy requirements are major barriers, and available estimates vary widely by source, concentration and application.

**Confidence:** Medium

**Why this confidence level**

The review supplies quantitative ranges, but the retrieved material does not show the underlying cost methodology, lifecycle boundaries or energy penalties by technology; the policy figures are incentives, not actual costs.

**Evidence**

- The peer-reviewed review gives indicative energy requirements of 2.5–8 GJ per tonne of CO₂ and costs of $50–600 per tonne, while describing CCS as high-cost and vulnerable to cost overruns. [S1]
- WRI identifies stubbornly high costs, regulatory challenges and inadequate financial support as reasons deployment remains below modeled requirements. [S4]
- C2ES reports that U.S. policy support includes tax credits of $85/t for industrial and power-sector saline storage and $180/t for direct-air-capture saline storage, indicating the scale of public incentives being used to improve project economics. [S3]

#### Finding 6

**Claim**

The principal arguments against indiscriminate large-scale deployment concern opportunity cost, moral hazard, public liability, uncertain storage performance and potentially continued fossil-fuel dependence.

**Confidence:** Medium

**Why this confidence level**

These are well-defined arguments reflected in multiple sources, but the retrieved content provides limited empirical evidence quantifying health, environmental, liability or opportunity-cost impacts.

**Evidence**

- WRI reports NGO and stakeholder objections that CCUS may create a moral hazard, function as a temporary fix rather than address fossil-fuel use, carry high costs, have a mixed record and impose disproportionate impacts on vulnerable communities. [S4]
- The review argues that reliance on CCS could delay more effective solutions and highlights liability transfer and geological uncertainty among recurring concerns. [S1]
- The EU report notes that storage and transport development require cross-border coordination and regulatory action, indicating institutional and infrastructure barriers in addition to technical ones. [S5]

#### Finding 7

**Claim**

The supplied sources do not justify the categorical conclusion that CCS alone—or CCS broadly applied—is sufficient for global decarbonization; the most defensible conclusion is conditional.

**Confidence:** High

**Why this confidence level**

The conditional synthesis is supported by both critical and supportive sources: CCS has plausible important niche roles, but its present performance, cost and scale do not support treating it as a standalone or universal solution.

**Evidence**

- The critical review does not reject CCS entirely and instead supports targeted use in hard-to-abate sectors, while warning that continued broad reliance is a high-cost gamble. [S1]
- WRI describes CCUS as one mitigation option, distinguishes it from removal, and notes that current deployment is far below modeled needs. [S4]
- C2ES and CATF present a more favorable view, arguing that CCS can provide 14% of needed global reductions by 2050 or is essential to modeled net-zero pathways, especially in industry and the EU. [S3] [S5]

### Conflicts Found

- Sources disagree in emphasis about the strategic importance of CCS. C2ES says CCS can provide 14% of global emissions reductions needed by 2050 and calls it the only practical route to deep industrial decarbonization; CATF’s EU report concludes “no CCUS, no net zero.” By contrast, WRI presents it as one option with serious cost and deployment concerns, and the peer-reviewed review characterizes broad reliance as a high-cost gamble while supporting only targeted deployment. [S1] [S3] [S4] [S5]
- Reported deployment levels and project counts are not directly comparable. WRI and the 2026 review emphasize approximately 0.1% of global emissions, while C2ES reports a larger number of operating and planned commercial-scale projects based on an earlier date. The disagreement may reflect different years, definitions of commercial scale, and whether capacity or actual captured-and-stored output is being counted. [S1] [S3] [S4]
- The sources differ on whether CCS is essential or merely useful in power and fossil-fuel applications. C2ES and CATF emphasize fossil power, blue hydrogen and dispatchable generation as potential uses; WRI and the critical review stress that CCS should not displace direct emissions reductions and should be concentrated where alternatives are limited. [S1] [S3] [S4] [S5]

### Important Gaps

- What are the independently verified current capture and permanent-storage volumes, excluding CO₂ used for enhanced oil recovery and short-lived utilization?
- What are the lifecycle emissions and net capture rates of representative projects after accounting for energy penalties, upstream methane, transport, compression, leakage and equipment downtime?
- How do levelized costs vary across cement, steel, hydrogen, power, natural-gas processing, direct air capture, BECCS and retrofits, and how do they compare with non-CCS alternatives?
- What is the realistic global geological storage capacity, and can storage permitting, monitoring, transport infrastructure and public acceptance expand at the rates required by 1.5°C scenarios?
- Which existing projects provide durable, independently monitored storage over sufficiently long periods, and what evidence exists on leakage risk and long-term liability?
- How much of the modeled requirement represents point-source emissions reduction versus net-negative removal, and how sensitive are those pathways to assumptions about renewables, electrification and fossil-fuel availability?

**Analysis Duration:** 30.02s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The current sources support a conditional assessment, but they are insufficient for the question’s requested evaluation of demonstrated effectiveness, costs, scalability and energy requirements. They are also imbalanced: C2ES and CATF are advocacy-oriented, WRI is an explainer, and the critical review is a single review whose displayed publication date is 2026. A focused search for authoritative, recent project-status and cost/lifecycle data would materially improve the answer.

**Next Search**

> IEA Global Status of CCS 2024 2025 actual capture capacity costs energy penalty project performance

---

# Iteration 2

## 1. Search

**Query**

> IEA Global Status of CCS 2024 2025 actual capture capacity costs energy penalty project performance

**Why this query**

The current sources support a conditional assessment, but they are insufficient for the question’s requested evaluation of demonstrated effectiveness, costs, scalability and energy requirements. They are also imbalanced: C2ES and CATF are advocacy-oriented, WRI is an explainer, and the critical review is a single review whose displayed publication date is 2026. A focused search for authoritative, recent project-status and cost/lifecycle data would materially improve the answer.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S6 — Global Status of CCS 2025 report highlights policy advancements and scaling up of CCS projects | Global CCS Institute posted on the topic | LinkedIn**
  URL: https://www.linkedin.com/posts/global-ccs-institute_global-status-of-ccs-activity-7382041437422583808-1cAp
- **S7 — CCUS projects around the world are reaching new milestones – Analysis - IEA**
  URL: https://www.iea.org/commentaries/ccus-projects-around-the-world-are-reaching-new-milestones
- **S8 — Global Status Report | Global CCS Institute**
  URL: https://www.globalccsinstitute.com/resources/global-status-report
- **S9 — CCUS Projects Database - Data product - IEA**
  URL: https://www.iea.org/data-and-statistics/data-product/ccus-projects-database
- **S10 — Carbon capture and storage: What can we learn from the ...**
  URL: https://www.catf.us/resource/carbon-capture-storage-what-can-learn-from-project-track-record

**Search Duration:** 1.80s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

CCS is expanding, but its demonstrated current climate contribution remains small relative to what net-zero pathways require.

**Confidence:** High

**Why this confidence level**

The IEA provides a recent operational estimate and directly compares the pipeline with net-zero requirements; this is consistent with the prior evidence that current deployment is far below modeled needs.

**Evidence**

- The IEA reports just over 50 MtCO₂ per year of capture and storage capacity in operation in the first quarter of 2025, while the current project pipeline could reach about 430 MtCO₂/year of capture capacity by 2030 and 670 MtCO₂/year of storage capacity. [S7]
- The IEA explicitly concludes that current trends remain insufficient for a pathway to net-zero emissions by mid-century. [S7]
- Earlier sources estimate that current CCS captures roughly 0.1% of global emissions, compared with requirements of roughly 1 Gt by 2030 and several billion tonnes by 2050 in 1.5°C scenarios. [S1] [S4]

#### Finding 2

**Claim**

The latest project pipeline indicates meaningful momentum, but announced or planned capacity should not be treated as demonstrated emissions reduction.

**Confidence:** Medium

**Why this confidence level**

The IEA clearly documents the gap between operating and pipeline capacity. The GCCSI figure is useful evidence of expansion but is not directly comparable without its definitions and underlying report.

**Evidence**

- The IEA reports that 60% of the 2030 pipeline is at advanced stages or under construction, but also notes that eight projects began operating in 2024 and were relatively small, producing only a marginal increase in operational capture capacity. [S7]
- The Global CCS Institute reports a 54% year-on-year increase in operational projects and total capture capacity of 513 MtCO₂/year, but the retrieved material does not clarify how this figure is defined or how much CO₂ is actually captured and permanently stored. [S6]
- The IEA database distinguishes projects by status and covers announced capacity, while its 2025 commentary separately reports just over 50 Mt/year actually in operation. [S7] [S9]

#### Finding 3

**Claim**

Individual CCS projects demonstrate that high technical performance is achievable, but the project record is heterogeneous and does not establish uniformly reliable whole-system climate effectiveness.

**Confidence:** Medium

**Why this confidence level**

The evidence supports demonstrated feasibility at selected facilities but also shows that performance varies and that transparent, independently comparable operating data remain limited.

**Evidence**

- CATF’s review of 13 large projects identifies Sleipner, the Alberta Carbon Trunk Line and Quest as projects that consistently met high technical performance levels. [S10]
- The same review states that projects have faced operational and technical challenges at larger scales or in more diverse applications, and recommends transparent reporting of performance data and problems. [S10]
- The prior evidence reports that capture rates above 90% are technically possible at individual facilities, while also identifying suboptimal capture, cost overruns, geological uncertainty and shortcomings in durability or emissions-offset claims at other projects. [S1] [S3]

#### Finding 4

**Claim**

Most existing large-scale CCS experience is concentrated in relatively favorable applications, so broader deployment in cement, steel, power and other sectors remains less demonstrated and generally more difficult.

**Confidence:** High

**Why this confidence level**

The IEA and CATF independently support the distinction between current experience in favorable source types and the harder challenge of applying CCS across industrial sectors.

**Evidence**

- The IEA reports that more than 60% of operational capture capacity remains at natural-gas-processing facilities, where capture costs are relatively low; hydrogen, carbon dioxide removal and industrial projects comprise over half of the pipeline expected to operate by 2030. [S7]
- CATF notes that historically commercial CO₂ capture has focused on high-purity sources, whereas climate-oriented deployment must increasingly address cement, steel and petrochemicals, where capture is often more expensive, and transport and saline-aquifer storage add costs. [S10]
- The sources identify cement and other process-emissions sectors as important potential applications because alternatives may be limited. [S1] [S5] [S7]

#### Finding 5

**Claim**

CCS can make a significant contribution if deployed selectively and at very large scale, particularly for hard-to-abate process emissions and some carbon-removal pathways, but it is not demonstrated as a universal or standalone decarbonization strategy.

**Confidence:** High

**Why this confidence level**

Supportive and critical sources converge on a conditional conclusion: CCS has potentially material niche and system-level roles, but current scale, costs, energy needs, and performance evidence do not support broad reliance or substitution for direct emissions reductions.

**Evidence**

- The IEA describes CCUS as potentially important for a low-emissions energy system but says current trends are insufficient for net zero. [S7]
- Prior sources support targeted deployment in cement and other difficult industrial sectors, as well as BECCS and direct-air capture with geological storage for durable removals. [S1] [S4] [S5]
- CATF concludes that billions of tonnes of capture and geological storage will be needed by mid-century and that several projects demonstrate achievable high performance, while acknowledging that climate-oriented applications can be more costly and complex. [S10]

#### Finding 6

**Claim**

The principal arguments for large-scale deployment are the treatment of unavoidable industrial process emissions, the possibility of durable atmospheric removals, use of existing industrial and transport expertise, and the potential for hub-based infrastructure to reduce costs and coordinate networks.

**Confidence:** Medium

**Why this confidence level**

The technical and strategic rationale is well supported, but the sources do not establish that hubs will deliver projected cost reductions or that all cited applications will be competitive with alternatives.

**Evidence**

- The IEA identifies renewed momentum around business models organized around CCUS hubs and networks and reports first-of-a-kind projects advancing in power, cement, carbon removal and storage. [S7]
- The IEA and prior sources identify cement, chemicals, steel, waste and other high-temperature or process-emissions sectors as potential applications where electrification or alternative fuels may not eliminate all emissions. [S5] [S7]
- CATF reports decades of experience with capture, CO₂ pipelines and geological injection, although combining these components for climate mitigation remains relatively new. [S10]

#### Finding 7

**Claim**

The principal arguments against indiscriminate deployment are high and uncertain costs, energy penalties, infrastructure and permitting requirements, imperfect or nontransparent performance, long-term storage liability, opportunity costs, and the risk of prolonging fossil-fuel use.

**Confidence:** Medium

**Why this confidence level**

The barriers are consistently identified and some quantitative cost and energy ranges are available, but the retrieved evidence does not provide comparable lifecycle assessments across technologies or robust quantification of opportunity costs and social impacts.

**Evidence**

- The prior review estimates energy requirements of 2.5–8 GJ per tonne of CO₂ and costs of approximately $50–600 per tonne, with substantial variation by application and risk of cost overruns. [S1]
- CATF states that saline-aquifer storage and transport to distant sites add costs and complexity, while many existing projects were driven by commercial motives such as enhanced oil recovery rather than maximizing climate benefit. [S10]
- WRI and the prior review identify moral hazard, delay of more effective alternatives, liability transfer, geological uncertainty and disproportionate community impacts as major concerns. [S1] [S4]

### Conflicts Found

- The GCCSI-linked source reports 513 MtCO₂/year of total capture capacity and a 54% increase in operational projects, whereas the IEA reports only just over 50 MtCO₂/year of operational capture and storage capacity. This is likely a definitional difference involving total, announced, or nominal capture capacity versus actually operating capture-and-storage capacity, but the retrieved GCCSI material does not resolve it. [S6] [S7] [S9]
- CATF emphasizes that several projects have consistently achieved high technical performance, while the prior critical review highlights projects with suboptimal capture, cost overruns, geological uncertainty and shortcomings in claimed climate benefits. These positions are conditionally compatible: high performance is demonstrated at some projects, not universally across the project population. [S1] [S10]

### Important Gaps

- What does the GCCSI figure of 513 MtCO₂/year measure, and how much of it is operational capture actually connected to permanent storage rather than announced or nominal capacity?
- What are independently verified net CO₂ reductions for representative projects after energy use, upstream emissions, transport, compression, downtime and leakage are included?
- How do full lifecycle costs and energy penalties compare with non-CCS alternatives across cement, steel, hydrogen, power, DAC and BECCS?
- Can permitting, monitoring, transport networks, storage characterization and long-term liability arrangements expand fast enough to support multi-gigaton deployment?
- What proportion of modeled CCS deployment is required for point-source emissions reduction versus carbon removal, and how sensitive are those pathways to faster electrification and renewable deployment?

**Analysis Duration:** 22.61s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The new IEA evidence materially strengthens the answer on current operational scale, pipeline growth and the distinction between announced capacity and demonstrated output. Together with the prior sources and CATF project review, the evidence supports a responsible conditional conclusion covering effectiveness, scalability, energy, costs and arguments for and against. Further research would improve quantitative comparisons, especially lifecycle costs and net project-level emissions, but is not necessary to answer the original question without overstating certainty.

**Stop Reason:** sufficient_evidence

---

# Final Research Decision

**Research Stopped Because**

The analyzer determined that the important parts of the question could be answered responsibly.

**Stop Reason:** sufficient_evidence

**Searches Performed:** 2

**Unique Sources:** 10

**Remaining Uncertainty**

- A harmonized, independently verified measure of operating capture and permanent storage, excluding short-lived utilization and applications whose climate benefit is uncertain.
- Comparable lifecycle costs and energy requirements across cement, steel, hydrogen, power, natural-gas processing, direct air capture and BECCS, including comparison with non-CCS alternatives.
- Project-level data on capture rates, downtime, transport emissions, upstream emissions, leakage and long-term storage performance.
- A robust assessment of whether geological storage characterization, permitting, transport infrastructure, monitoring and long-term liability systems can expand at the rates required by modeled pathways.
- A clearer separation between CCS for point-source emissions reduction and CCS-linked carbon removal, together with analysis of how deployment needs change under faster electrification and renewable expansion.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 2 | 4.70s |
| OpenAI Analysis | 2 | 52.63s |
| Report Generation | 1 | 33.02s |
| Total Run | — | 90.35s |
