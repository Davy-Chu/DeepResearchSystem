# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

Can carbon capture and storage make a significant contribution to reducing global CO₂ emissions? Evaluate its demonstrated effectiveness, costs, scalability, energy requirements, and major arguments for and against large-scale deployment.

**Status:** Completed

**Stop Reason:** sufficient_evidence

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 5 / 10

**Unique Sources:** 25

**OpenAI Calls:** 6

**Tavily Calls:** 5

**Started:** 2026-09-01T06:19:34-04:00

**Ended:** 2026-09-01T06:21:45-04:00

**Total Runtime:** 130.99s

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
- **S3 — Q&A: The current state of ‘carbon dioxide removal’ around the world - Carbon Brief**
  URL: https://www.carbonbrief.org/qa-the-current-state-of-carbon-dioxide-removal-around-the-world
- **S4 — Carbon Capture and Storage, Explained | World Resources Institute**
  URL: https://www.wri.org/insights/carbon-capture-technology
- **S5 — CCUS in the transition to net-zero emissions – CCUS in Clean Energy Transitions – Analysis - IEA**
  URL: https://www.iea.org/reports/ccus-in-clean-energy-transitions/ccus-in-the-transition-to-net-zero-emissions

**Search Duration:** 2.87s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

CCS could make a significant contribution in principle, but current demonstrated deployment is far below the scale required by climate pathways.

**Confidence:** High

**Why this confidence level**

The present-scale and modeled-scale comparison is stated directly by WRI, while the IEA provides an independent account of the potential roles.

**Evidence**

- WRI reports that current CCUS captures about 50 million tonnes of CO₂ annually, roughly 0.1% of global emissions, while 1.5°C scenarios indicate about 1 billion tonnes by 2030 and several billion tonnes by 2050. [S4]
- The IEA describes CCUS as having four potential roles: reducing emissions from existing assets, addressing hard-to-abate sectors, enabling low-carbon hydrogen, and supporting carbon removal through approaches such as BECCS. [S5]

#### Finding 2

**Claim**

The strongest strategic case for CCS is concentrated in hard-to-abate industrial applications and selected existing infrastructure, rather than indiscriminate deployment across the energy system.

**Confidence:** High

**Why this confidence level**

The sectoral focus is consistent across the review, IEA material, and WRI explainer.

**Evidence**

- The review identifies cement and legacy-infrastructure retrofits as sectors where alternatives may be limited and CCS could remain strategically useful. [S1]
- The IEA identifies hard-to-abate sectors and existing energy assets as central roles for CCUS in net-zero transitions. [S5]
- WRI states that CCUS is one mitigation option among many and distinguishes source capture from atmospheric carbon removal; it presents emissions reductions as the dominant component of long-term plans. [S4]

#### Finding 3

**Claim**

The technology has been demonstrated in individual projects, but the evidence base indicates an uneven record of performance and does not establish reliable global effectiveness at large scale.

**Confidence:** Medium

**Why this confidence level**

There is direct evidence of project deployment and a cross-source characterization of mixed performance, but the retrieved excerpts do not provide comparable project-by-project capture, uptime, or storage-retention measurements.

**Evidence**

- A pro-CCS account cites Sleipner and Petra Nova as examples of operating or implemented projects and characterizes them as demonstrating viability. [S2]
- The critical review says case studies including Petra Nova, Gorgon, Sleipner, and In Salah show recurring concerns involving capture rates, cost overruns, geological uncertainty, durability, and the interpretation of project success. [S1]
- WRI characterizes the deployment record as mixed and says progress remains below modeled requirements. [S4]

#### Finding 4

**Claim**

CCS is generally costly and energy-intensive, creating an economic and system-efficiency disadvantage relative to simpler mitigation options in applications where alternatives exist.

**Confidence:** Medium

**Why this confidence level**

The retrieved material supplies a quantitative range from one review and qualitative corroboration from other sources, but costs and energy use vary substantially by source concentration, facility, capture technology, transport, and storage conditions.

**Evidence**

- The review gives indicative ranges of 2.5–8 GJ per tonne of CO₂ for energy demand and $50–600 per tonne for cost, while emphasizing high costs and recurring overruns. [S1]
- WRI identifies stubbornly high costs, regulatory challenges, and insufficient financial support as reasons deployment remains far below modeled levels. [S4]
- The pro-CCS source also acknowledges that large-scale implementation is expensive and may require carbon pricing, tax incentives, and other support. [S2]

#### Finding 5

**Claim**

Major arguments for large-scale deployment are emissions reduction from concentrated industrial sources, preservation or retrofit of existing assets, low-carbon hydrogen production, and possible negative emissions when paired with sustainable biomass or direct air capture.

**Confidence:** High

**Why this confidence level**

These proposed roles are explicitly stated by the IEA and WRI and are also reflected in the pro-deployment source.

**Evidence**

- The IEA lists existing assets, hard-to-abate sectors, hydrogen, and atmospheric carbon removal as four critical CCUS roles. [S5]
- WRI explains that source capture can be combined with permanent geological storage and that BECCS can constitute removal because biomass carbon was previously taken from the atmosphere. [S4]
- The pro-CCS source argues that CCS can address power generation and industrial emissions including cement, steel, and chemicals. [S2]

#### Finding 6

**Claim**

Major arguments against broad deployment include high costs, energy requirements, uncertain or difficult-to-scale storage and transport infrastructure, imperfect project performance, leakage or permanence concerns, and the risk that CCS delays direct emissions cuts or extends fossil-fuel use.

**Confidence:** High

**Why this confidence level**

The objections are directly documented by multiple sources, including a critical review and an institutional explainer; however, the excerpts do not quantify the frequency or severity of each risk.

**Evidence**

- The critical review highlights cost overruns, suboptimal capture rates, geological uncertainties, durability concerns, and possible transfer of liability to the public. [S1]
- WRI reports objections based on moral hazard, continued fossil-fuel use, mixed success, high costs, and potentially disproportionate impacts on vulnerable communities. [S4]
- The pro-CCS source acknowledges storage-site availability, safety, environmental impacts, and financing as unresolved implementation challenges. [S2]

### Conflicts Found

- Sources disagree in emphasis about what current projects demonstrate. S2 presents Sleipner and Petra Nova as evidence that CCS is viable, whereas S1 argues that projects commonly described as successful fall short when assessed for capture performance, durability, scale, and net emissions effects. This is a conditional disagreement: project-level technical operation does not necessarily imply cost-effective, durable, system-wide climate effectiveness. [S1] [S2]
- Sources differ on the breadth of CCS's appropriate role. The IEA presents CCUS as essential in its net-zero scenario, while WRI and the critical review argue that it should not displace direct emissions reductions and is most defensible in constrained, hard-to-abate applications. [S1] [S4] [S5]

### Important Gaps

- What are the independently verified capture rates, operating lifetimes, downtime, and net lifecycle emissions of major CCS facilities, including Petra Nova, Gorgon, Sleipner, and In Salah?
- How do levelized costs and energy penalties compare quantitatively with renewable power, electrification, efficiency, and alternative industrial processes for specific sectors?
- How much suitable, permitted, monitored geological storage capacity exists, and can CO₂ transport and storage infrastructure expand at the required multi-gigatonne scale?
- What are measured long-term leakage rates, monitoring requirements, and post-closure liability arrangements?
- Which portions of modeled CCS deployment represent fossil-source abatement, and which represent genuine durable carbon removal?
- How material are community, environmental-justice, water-use, and local air-pollution impacts under large-scale deployment?

**Analysis Duration:** 18.80s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The sources establish the central conclusion and major arguments, but important quantitative elements requested by the question—especially independently verified project effectiveness, sector-specific costs, energy penalties, storage scalability, and long-term permanence—remain weak or absent. A focused search for authoritative deployment and cost data would materially improve the assessment.

**Next Search**

> IEA Global CCS Institute 2024 2025 CCS projects capture capacity costs energy penalty storage capacity verified performance

---

# Iteration 2

## 1. Search

**Query**

> IEA Global CCS Institute 2024 2025 CCS projects capture capacity costs energy penalty storage capacity verified performance

**Why this query**

The sources establish the central conclusion and major arguments, but important quantitative elements requested by the question—especially independently verified project effectiveness, sector-specific costs, energy penalties, storage scalability, and long-term permanence—remain weak or absent. A focused search for authoritative deployment and cost data would materially improve the assessment.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S6 — Evolution of capture capacity either operational or under construction by sector between 2025 and 2026 editions of IEA CCUS Projects Database – Charts – Data & Statistics - IEA**
  URL: https://www.iea.org/data-and-statistics/charts/evolution-of-capture-capacity-either-operational-or-under-construction-by-sector-between-2025-and-2026-editions-of-iea-ccus-projects-database
- **S7 — Minimal role for carbon capture, utilization, and storage (CCUS) in IEA's World Energy Outlook 2025 | IEEFA**
  URL: https://ieefa.org/resources/minimal-role-carbon-capture-utilization-and-storage-ccus-ieas-world-energy-outlook-2025
- **S8 — Global Status of CCS | Global CCS Institute**
  URL: https://www.globalccsinstitute.com/global-status-of-ccs
- **S9 — A new era for CCUS – CCUS in Clean Energy Transitions – Analysis - IEA**
  URL: https://www.iea.org/reports/ccus-in-clean-energy-transitions/a-new-era-for-ccus
- **S10 — Global CCS Institute | Carbon Management at Scale**
  URL: https://www.globalccsinstitute.com

**Search Duration:** 4.93s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Recent industry reporting indicates that CCS deployment is growing, but growth in project numbers and planned capacity should not be equated with demonstrated emissions reductions.

**Confidence:** Medium

**Why this confidence level**

The figures are directly reported by a sector-focused organization, but the source has an advocacy role and the retrieved material does not independently validate project performance.

**Evidence**

- The Global CCS Institute reports 77 CCS projects operating and 47 under construction in 2025, with planned global capture capacity growing at more than 30% annually since 2017. [S8]
- The same source describes policy support, private-sector engagement, and expanding infrastructure as drivers of project growth, but does not provide independently verified aggregate capture, storage, or lifecycle-emissions results. [S8]

#### Finding 2

**Claim**

A recent IEEFA interpretation of the IEA’s 2025 net-zero scenario assigns CCUS a relatively small global role compared with renewables, electrification, fuel switching, and efficiency.

**Confidence:** Medium

**Why this confidence level**

The figures are attributed to the IEA but are presented through a critical third-party interpretation; the retrieved excerpt does not include the underlying IEA tables or methodology.

**Evidence**

- IEEFA reports that, according to its reading of the IEA World Energy Outlook 2025, CCUS contributes no more than 4.9% of total emissions reductions in the 2050 NZE Scenario: 1.2% from power and 3.7% from industry. [S7]
- The source says renewables, electrification, fuel switching, and efficiency together account for more than 82% of the reductions in that scenario. [S7]

#### Finding 3

**Claim**

End-to-end CCUS costs can be high enough to require sustained policy support or carbon prices, particularly in Europe.

**Confidence:** Medium

**Why this confidence level**

The source provides a specific recent cost range and comparison, but the estimate is for EU projects and may not generalize across facilities, regions, CO₂ concentrations, transport distances, or storage conditions.

**Evidence**

- IEEFA cites a 2025 Agora Industry/Öko-Institut estimate of EUR105–280 per tonne of CO₂ for end-to-end disposal in the EU, including capture, transport, and storage. [S7]
- The source reports that EU ETS prices averaged about EUR75 per tonne in 2025, below the cited lower-end disposal cost, implying that subsidies or higher carbon prices may be needed for deployment under those assumptions. [S7]

#### Finding 4

**Claim**

The IEA’s strategic case for CCS remains focused on applications where direct alternatives are limited, existing assets require retrofitting, hydrogen production is needed, or atmospheric removals are pursued.

**Confidence:** High

**Why this confidence level**

These roles and the historical deployment assessment are stated directly by the IEA and align with the accumulated findings from S4 and S5.

**Evidence**

- The IEA identifies retrofits to existing power and industrial plants, hard-to-abate sectors such as cement, iron and steel and chemicals, low-carbon hydrogen, and removals using bioenergy or direct air capture as strategic uses of CCUS. [S9]
- The IEA also states that historical CCUS deployment has been slow and has had only a limited impact on global CO₂ emissions, while identifying the 2020s as important for scaling investment. [S9]

### Conflicts Found

- There is a disagreement in emphasis between the IEA’s strategic framing and IEEFA’s interpretation of the IEA’s 2025 scenario. The IEA presents CCUS as strategically valuable for several sectors and pathways, whereas IEEFA argues that the technology contributes less than 5% of modeled emissions reductions and is not essential in that scenario. These positions can both be true: CCS may be important for specific hard-to-abate applications while making only a modest contribution to total global reductions. [S7] [S9]
- The Global CCS Institute presents rapid growth in operating, construction, and planned projects as evidence that CCS is scaling, while the accumulated WRI and IEA evidence shows that current captured volumes remain far below climate-pathway requirements. Project-pipeline growth is therefore a leading indicator, not proof that gigatonne-scale, cost-effective and durable storage has been achieved. [S4] [S8] [S9]
- S7 characterizes the IEA’s 2025 outlook as a downgrading of CCUS, while S9 is an earlier IEA report describing CCUS as having significant strategic value. This is a time-dependent difference in scenario assessment and emphasis, not necessarily a contradiction about the technology’s usefulness in selected sectors. [S7] [S9]

### Important Gaps

- The new sources do not provide independently verified facility-level capture rates, uptime, net lifecycle emissions, or long-term storage-retention results for major projects.
- S6 identifies a comparison of operational and under-construction capture capacity between IEA database editions, but the retrieved content does not expose the chart’s numerical values; current demonstrated capacity therefore remains insufficiently quantified.
- The reported 2025 project counts and planned-capacity growth from S8 need reconciliation with actual captured and permanently stored tonnes, since projects at development or construction stages may not operate as planned.
- The 4.9% scenario figure from S7 requires checking against the underlying IEA World Energy Outlook 2025 tables and definitions of emissions reductions, especially whether it includes removals and how CCUS is separated from direct air capture or BECCS.
- Comparative sector-specific costs and energy penalties versus electrification, efficiency, renewable power, and alternative industrial processes remain unresolved.
- The amount of permitted and monitored geological storage capacity, transport-network scalability, leakage rates, and long-term liability arrangements remain unresolved.

**Analysis Duration:** 15.73s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The overall conclusion is supportable: CCS can make a meaningful but likely targeted contribution, while current deployment is much too small to demonstrate a global-scale solution. However, an important remaining gap is the quantitative distinction between project-pipeline growth and actual operational capture and permanent storage. Resolving that would materially strengthen the evaluation of demonstrated effectiveness and scalability.

**Next Search**

> latest independently verified global CCS capacity tonnes CO2 captured stored operational projects capture rate 2025

---

# Iteration 3

## 1. Search

**Query**

> latest independently verified global CCS capacity tonnes CO2 captured stored operational projects capture rate 2025

**Why this query**

The overall conclusion is supportable: CCS can make a meaningful but likely targeted contribution, while current deployment is much too small to demonstrate a global-scale solution. However, an important remaining gap is the quantitative distinction between project-pipeline growth and actual operational capture and permanent storage. Resolving that would materially strengthen the evaluation of demonstrated effectiveness and scalability.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S11 — Carbon Capture and Storage Capacity Worldwide**
  URL: https://incorrys.com/environmental-data/carbon-capture-and-storage/carbon-capture-and-storage-capacity-worldwide
- **S12 — Largest operational CCS projects globally 2025 | Statista**
  URL: https://www.statista.com/statistics/1108355/largest-carbon-capture-and-storage-projects-worldwide-capacity
- **S13 — Around the world in 22 carbon capture projects - Carbon Brief**
  URL: https://www.carbonbrief.org/around-the-world-in-22-carbon-capture-projects
- **S14 — Report Finds Growing CCS Sector**
  URL: https://jpt.spe.org/report-finds-growing-ccs-sector
- **S15 — CCUS Projects Explorer – Data Tools**
  URL: https://www.iea.org/data-and-statistics/data-tools/ccus-projects-explorer

**Search Duration:** 2.33s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Current operational CCS capacity remains a very small fraction of global CO₂ emissions, despite recent growth.

**Confidence:** High

**Why this confidence level**

Independent institutional and data-oriented sources converge on the conclusion that present deployment is well below one percent of global emissions.

**Evidence**

- Incorrys reports 51 MtCO₂/year of operational capacity at the end of 2024, compared with 37,600 MtCO₂/year of energy and industrial-process emissions—about 0.16%. [S11]
- The accumulated WRI finding similarly estimates current CCUS capture at roughly 50 MtCO₂/year, about 0.1% of global emissions, far below modeled requirements of roughly 1 GtCO₂/year by 2030 and several gigatonnes by 2050. [S4]
- The IEA states that historical CCUS deployment has been slow and has had only limited impact on global CO₂ emissions. [S9]

#### Finding 2

**Claim**

The CCS project pipeline is expanding substantially, but planned, under-construction, and nominal operating capacity do not demonstrate equivalent quantities of CO₂ actually captured and permanently stored.

**Confidence:** High

**Why this confidence level**

The sources clearly document pipeline growth and the distinction between capacity and realized performance. Exact totals differ by source and definition.

**Evidence**

- The Global CCS Institute reports 77 operating facilities with 64 Mtpa storage capability, 44 Mtpa under construction, and projected fivefold growth in operating capture capacity by 2030. [S14]
- Incorrys reports 51 MtCO₂/year operational capacity and more than 50 MtCO₂/year under construction for 2025–2027, illustrating rapid prospective expansion but also a different estimate of current capacity. [S11]
- The accumulated evidence cautions that project counts and planned capacity are leading indicators rather than independently verified aggregate capture, uptime, lifecycle-emissions, or storage results. [S8]

#### Finding 3

**Claim**

Reported global capacity figures are not directly comparable because sources appear to use different definitions, dates, and possibly capture-versus-storage measures.

**Confidence:** Medium

**Why this confidence level**

The numerical discrepancy is directly observable, but the retrieved material does not provide enough methodological detail to identify precisely why every figure differs.

**Evidence**

- S11 reports 51 MtCO₂/year operational capacity at the end of 2024, whereas S12 reports approximately 64 Mtpa of operational facility capacity in 2025 and S14 reports 64 Mtpa storage capability for 77 facilities. [S11] [S12] [S14]
- The IEA database explicitly covers capture, transport, storage, and utilisation projects, including projects in planning, and defines inclusion thresholds and exclusions; this demonstrates that dataset scope and categorisation affect reported totals. [S15]

#### Finding 4

**Claim**

CCS can make a significant contribution in absolute terms only if it scales by orders of magnitude; its most defensible role is targeted rather than universal.

**Confidence:** High

**Why this confidence level**

The sectoral rationale is consistent across IEA, WRI, and review evidence; the historical pathway figures are older scenarios and should not be treated as current forecasts.

**Evidence**

- The IEA identifies retrofits, hard-to-abate industries, low-carbon hydrogen, and carbon removals as strategic applications for CCUS. [S9]
- WRI and the accumulated review identify cement, selected industrial sources, legacy infrastructure, and removals as stronger use cases than indiscriminate deployment across the energy system. [S1] [S4]
- Historical IEA and IPCC pathways cited by Carbon Brief envisaged growth from roughly 40 MtCO₂/year in the early project portfolio to approximately 2 GtCO₂/year by 2030 and 7–10 GtCO₂/year by 2050. [S13]

#### Finding 5

**Claim**

Individual projects demonstrate technical operation, but the retrieved evidence does not establish consistently cost-effective, high-uptime, end-to-end climate performance at global scale.

**Confidence:** Medium

**Why this confidence level**

There is evidence of real project operation and significant criticism, but no retrieved source supplies a consistent independent dataset of capture rates, uptime, net lifecycle emissions, and verified retention across major facilities.

**Evidence**

- S2 cites Sleipner and Petra Nova as evidence of operational or implemented CCS and technical viability. [S2]
- The critical review identifies capture-rate shortfalls, cost overruns, geological uncertainty, durability concerns, and disputed interpretations of success in projects including Petra Nova, Gorgon, Sleipner, and In Salah. [S1]
- Carbon Brief’s historical survey illustrates that many early projects were associated with natural-gas processing or enhanced oil recovery, limiting their direct comparability with broad fossil-power or industrial decarbonisation claims. [S13]

#### Finding 6

**Claim**

CCS imposes material energy and economic penalties, with costs highly dependent on the source, technology, transport distance, and storage conditions.

**Confidence:** Medium

**Why this confidence level**

Quantitative ranges are available, but mostly from review or third-party sources and are not a universal cost curve. The evidence supports high variability and an energy penalty, not one definitive global cost.

**Evidence**

- The review gives indicative energy requirements of 2.5–8 GJ per tonne of CO₂ and costs of approximately $50–600 per tonne, while noting substantial variability and overruns. [S1]
- IEEFA cites a 2025 EU estimate of €105–280 per tonne for end-to-end capture, transport, and storage, above an approximately €75/t EU ETS average under the cited assumptions. [S7]
- Carbon Brief explains that capture, compression, and injection consume energy that otherwise could serve the grid or industrial production. [S13]

#### Finding 7

**Claim**

The principal arguments for large-scale CCS are avoiding emissions from concentrated and hard-to-abate sources, retrofitting some existing assets, producing low-carbon hydrogen, and enabling potential negative emissions through BECCS or direct air capture.

**Confidence:** High

**Why this confidence level**

These are directly stated strategic applications, although their climate value depends on lifecycle emissions, sustainable biomass, permanence, and project performance.

**Evidence**

- The IEA lists these four roles explicitly. [S5] [S9]
- WRI distinguishes source capture with geological storage from atmospheric removal and identifies BECCS as a possible removal pathway. [S4]
- The pro-CCS source argues for applications in cement, steel, chemicals, and power generation. [S2]

#### Finding 8

**Claim**

The principal arguments against broad deployment are cost, energy use, infrastructure and storage scale, imperfect performance, permanence and liability risks, environmental impacts, and the possibility of delaying direct emissions reductions or extending fossil-fuel use.

**Confidence:** High

**Why this confidence level**

Multiple sources document the main objections. Their aggregate magnitude and probability remain insufficiently quantified in the retrieved evidence.

**Evidence**

- The critical review documents cost overruns, suboptimal capture, geological uncertainty, durability concerns, and potential transfer of liability to the public. [S1]
- WRI identifies moral hazard, continued fossil-fuel dependence, high costs, mixed project success, and disproportionate impacts on vulnerable communities as major objections. [S4]
- S14 reports growth in pipelines and storage infrastructure, but this indicates development rather than proof that multi-gigatonne networks can operate reliably and affordably. [S14]

### Conflicts Found

- Reported current capacity differs: S11 gives 51 MtCO₂/year operational capacity at the end of 2024, while S12 and S14 give approximately 64 Mtpa in 2025. This is likely a definitional, timing, or capture-versus-storage discrepancy, but the retrieved excerpts do not resolve it. [S11] [S12] [S14]
- S2 treats operating projects as evidence of CCS viability, while S1 argues that technical operation alone can conceal inadequate capture, high costs, uncertain permanence, or weak net climate benefits. The disagreement is conditional on what counts as effectiveness. [S1] [S2]
- The Global CCS Institute emphasizes rapid growth in projects and infrastructure, whereas WRI and the IEA emphasize that actual global emissions reductions remain very small relative to climate-pathway needs. Pipeline growth is not equivalent to delivered mitigation. [S4] [S8] [S9] [S14]

### Important Gaps

- What are independently verified capture rates, uptime, downtime, energy use, net lifecycle emissions, and stored tonnes for major operating projects?
- How much permitted and monitored geological storage capacity is available, and can transport and storage networks scale to multi-gigatonne annual flows?
- What are measured long-term leakage rates, monitoring obligations, and post-closure liability arrangements?
- How do sector-specific CCS costs and energy penalties compare with electrification, efficiency, alternative industrial processes, and renewable hydrogen?
- What share of projected CCS deployment represents fossil-source abatement versus genuine durable carbon removal?
- Why do recent sources report 51 versus 64 Mtpa of operational capacity, and are these figures measuring capture capacity, storage capability, or different project populations?

**Analysis Duration:** 20.81s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The accumulated evidence is sufficient to answer the broad conclusion: CCS can contribute materially in principle and may be important in selected hard-to-abate sectors, but current delivered mitigation is tiny and broad deployment faces substantial cost, energy, infrastructure, and performance uncertainties. However, a central part of the question—demonstrated effectiveness—still lacks independently verified facility-level performance and lifecycle evidence. Resolving that gap would materially improve the answer more than another general overview.

**Next Search**

> independent verification CCS project capture rates uptime net lifecycle emissions Petra Nova Gorgon Sleipner In Salah storage permanence

---

# Iteration 4

## 1. Search

**Query**

> independent verification CCS project capture rates uptime net lifecycle emissions Petra Nova Gorgon Sleipner In Salah storage permanence

**Why this query**

The accumulated evidence is sufficient to answer the broad conclusion: CCS can contribute materially in principle and may be important in selected hard-to-abate sectors, but current delivered mitigation is tiny and broad deployment faces substantial cost, energy, infrastructure, and performance uncertainties. However, a central part of the question—demonstrated effectiveness—still lacks independently verified facility-level performance and lifecycle evidence. Resolving that gap would materially improve the answer more than another general overview.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S16 — The ill-fated Petra Nova CCS project: NRG Energy throws in the towel | IEEFA**
  URL: https://ieefa.org/resources/ill-fated-petra-nova-ccs-project-nrg-energy-throws-towel
- **S17 — 92.4% Capture Rate at Petra Nova — that’s a CCS Success | CCS Knowledge Centre**
  URL: https://ccsknowledge.com/insights/92-4-capture-rate-at-petra-nova-thats-a-ccs-success
- **S18 — petra nova**
  URL: https://www.osti.gov/servlets/purl/1608572
- **S19 — Petra Nova Carbon Capture and Storage Monitoring | Gulf Coast Carbon Center**
  URL: https://gccc.beg.utexas.edu/research/petra-nova
- **S20 — Carbon capture and storage: What can we learn from the project track record? – Clean Air Task Force**
  URL: https://www.catf.us/resource/carbon-capture-storage-what-can-learn-from-project-track-record

**Search Duration:** 2.49s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Petra Nova demonstrates that post-combustion capture, CO₂ transport, and subsurface injection can operate at commercial-project scale, but it does not by itself demonstrate reliable, cost-effective climate mitigation over the long term.

**Confidence:** High

**Why this confidence level**

Official project and university monitoring materials directly establish operation and measured project totals, while the critical source documents the shutdown and presents a materially different whole-system interpretation. The evidence supports technical demonstration but not unqualified commercial or climate success.

**Evidence**

- The U.S. Department of Energy project report states that Petra Nova was designed to capture at least 90% of CO₂ from a 240-MW-equivalent coal-plant flue-gas slipstream, transported CO₂ through an 81-mile pipeline, and captured 3.54 million metric tonnes during its three-year demonstration period. [S18]
- The University of Texas monitoring center reports roughly 4 million short tons captured and describes mass-balance, pressure, geophysical, fluid-sampling, and groundwater-monitoring procedures; it reports 3.61 million short tons sequestered out of 3.64 million captured under the project accounting method. [S19]
- Petra Nova was taken offline in May 2020 and remained down in the IEEFA account; the source reports substantial technical downtime and argues that whole-system capture may have been closer to 55–58% after accounting for emissions from the cogeneration facility. [S16]

#### Finding 2

**Claim**

Reported Petra Nova capture performance depends strongly on the metric and system boundary used.

**Confidence:** High

**Why this confidence level**

The sources explicitly report the competing figures and boundaries. The disagreement is not merely numerical: it concerns whether success means capture efficiency at the capture unit, capture from the processed slipstream, or net reduction across the integrated facility and upstream fuel cycle.

**Evidence**

- The CCS Knowledge Centre cites Petra Nova's final technical report as reporting 92.4% capture efficiency from the processed flue-gas slipstream, exceeding the 90% target, and claims lower-than-expected power and steam consumption. [S17]
- IEEFA states that the underlying data supporting the public 90% claim were not made available and estimates 65–70% capture based on EPA emissions data, or 55–58% when the gas-fired cogeneration emissions are included. [S16]
- The DOE report defines the project as treating a flue-gas slipstream and reports capture of approximately 5,200 short tons per day at full capacity, rather than presenting a whole-facility net-emissions result. [S18]

#### Finding 3

**Claim**

Petra Nova's results provide evidence of storage monitoring and accounting, but the retrieved material does not establish decades-long permanence or lifecycle climate benefit.

**Confidence:** Medium

**Why this confidence level**

Monitoring and short-term accounting are directly documented, but the evidence gap is material for judging permanent climate mitigation, especially because the project used CO₂ for EOR.

**Evidence**

- The University of Texas monitoring program used reservoir modeling, pressure monitoring, geophysical logging, fluid sampling, groundwater characterization, soil-gas monitoring, and mass-balance accounting to assess containment and losses during the project period. [S19]
- The DOE report says Petra Nova transported captured CO₂ to the West Ranch oilfield for enhanced oil recovery and reports more than 4.2 million barrels of gross oil production associated with the project. [S18]
- The project materials describe monitoring during the demonstration period, but the retrieved excerpts do not provide long-term post-closure retention data, a full lifecycle emissions assessment, or an accounting of emissions associated with additional oil production. [S18] [S19]

#### Finding 4

**Claim**

The broader project record is mixed rather than uniformly unsuccessful or uniformly successful.

**Confidence:** High

**Why this confidence level**

The new review adds a more differentiated account: some projects meet strong technical standards, but motives, source types, system boundaries, and reporting practices vary substantially. This reconciles rather than eliminates the prior disagreement.

**Evidence**

- The Clean Air Task Force review identifies Sleipner, Alberta Carbon Trunk Line, and Quest as projects that consistently achieved high technical performance, while emphasizing that other projects experienced operational challenges and that transparent reporting is needed. [S20]
- The same review notes that many large-scale projects were developed for commercial purposes such as enhanced oil recovery rather than to maximize climate benefits, and that applying capture to cement, steel, and petrochemicals can be more costly than established high-purity CO₂ applications. [S20]
- The accumulated evidence documents both technical operation at projects such as Sleipner and Petra Nova and recurring concerns over downtime, costs, capture rates, and interpretation of success. [S1] [S2] [S4]

#### Finding 5

**Claim**

The new evidence strengthens the case for targeted CCS in industrial and otherwise difficult-to-decarbonize applications, while weakening the case for relying on CCS to preserve unabated fossil-fuel power generation.

**Confidence:** High

**Why this confidence level**

The sectoral conclusion is consistent across the new and accumulated sources, although it remains a strategic judgment dependent on alternatives, local costs, and project design.

**Evidence**

- The Clean Air Task Force identifies cement, steel, and petrochemicals as sectors with few decarbonization alternatives and notes that climate-oriented storage in saline aquifers adds costs beyond historically commercial CO₂ uses. [S20]
- IEEFA reports that Petra Nova required major public and concessional financial support, experienced technical and financial problems, and that the associated coal-power CCS approach was a significant risk. [S16]
- The IEA, WRI, and prior review similarly identify hard-to-abate industry, selected retrofits, hydrogen, and removals as stronger strategic roles than indiscriminate deployment. [S1] [S4] [S9]

### Conflicts Found

- The Petra Nova technical-performance claims conflict conditionally. S17 cites a 92.4% capture efficiency and high process availability when the capture facility was online; S16 estimates substantially lower whole-system capture and emphasizes extended project downtime. S18 and S19 report project-level capture and storage totals but do not resolve the whole-facility net-emissions question. [S16] [S17] [S18] [S19]
- S18 and S19 report successful capture, transport, monitoring, and accounting during Petra Nova's demonstration period, whereas S16 interprets the later shutdown, financial losses, and incomplete performance data as evidence of commercial and technological failure. These positions use different definitions of success: bounded demonstration versus durable, economically viable, whole-system climate mitigation. [S16] [S18] [S19]
- The new CATF review is more favorable than the critical IEEFA assessment: it identifies several projects with consistently high technical performance, while IEEFA generalizes from Petra Nova and other fossil-power projects to argue that CCS is far from proven. The sources can both be accommodated if performance is assessed project-by-project and by application rather than treated as a single technology-wide outcome. [S16] [S20]

### Important Gaps

- What are independently audited, comparable capture rates, uptime, energy use, and net lifecycle emissions for major CCS facilities using a common system boundary?
- How much of Petra Nova's reported stored CO₂ remains securely retained after operations ended, and how should EOR-related oil and upstream emissions be counted?
- What is the independently verified global quantity of CO₂ actually captured and permanently stored, as distinct from nominal capacity, planned capacity, or CO₂ used for EOR?
- How much permitted and monitored saline-aquifer storage capacity and transport infrastructure can be developed at multi-gigatonne annual scale?
- How do sector-specific CCS costs and energy penalties compare with electrification, efficiency, alternative industrial processes, and renewable hydrogen?
- What proportion of modeled CCS deployment is fossil-source abatement versus durable carbon removal, and what sustainability constraints apply to BECCS or direct air capture?
- What long-term leakage rates, monitoring obligations, and post-closure liability arrangements apply across different storage settings?

**Analysis Duration:** 18.66s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources materially improve the answer on demonstrated effectiveness by adding official Petra Nova performance and monitoring data and a more balanced project-track-record review. However, an important scalability question remains unanswered: independently verified, permitted geological storage capacity and transport capability at the multi-gigatonne scale. That evidence would materially improve evaluation of whether CCS can make a significant global contribution rather than merely operate in individual projects.

**Next Search**

> independent assessment global geological CO2 storage capacity permitted monitored transport scalability multi-gigatonne CCS 2024 2025

---

# Iteration 5

## 1. Search

**Query**

> independent assessment global geological CO2 storage capacity permitted monitored transport scalability multi-gigatonne CCS 2024 2025

**Why this query**

The new sources materially improve the answer on demonstrated effectiveness by adding official Petra Nova performance and monitoring data and a more balanced project-track-record review. However, an important scalability question remains unanswered: independently verified, permitted geological storage capacity and transport capability at the multi-gigatonne scale. That evidence would materially improve evaluation of whether CCS can make a significant global contribution rather than merely operate in individual projects.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S21 — Global CO2 storage capacity may be drastically overstated, study finds**
  URL: https://news.mongabay.com/2025/09/global-co2-storage-capacity-may-be-drastically-overstated-study-finds
- **S22 — The feasibility of reaching gigatonne scale CO2 storage by mid-century**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11358273
- **S23 — Publications Archive | Global CCS Institute**
  URL: https://www.globalccsinstitute.com/publications
- **S24 — Carbon capture and storage | Geoscience Australia**
  URL: https://www.ga.gov.au/aecr2025/carbon-capture-and-storage
- **S25 — Europe's geological storage bottleneck limits carbon removal**
  URL: https://carbongap.org/insights/europes-geological-storage-bottleneck-an-overlooked-barrier-to-scaling-carbon-removal

**Search Duration:** 2.16s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new evidence strengthens the conclusion that CCS could contribute significantly in absolute terms, but only after expansion by orders of magnitude and subject to substantial geological, geographic, and infrastructure constraints.

**Confidence:** High

**Why this confidence level**

The peer-reviewed scalability analysis complements multiple sources documenting the very small current baseline and supports a conditional rather than unlimited scalability claim.

**Evidence**

- A peer-reviewed feasibility study estimates a maximum global storage rate of 16 GtCO₂ per year by 2050 under highly favorable conditions, including a 60% contribution from the United States; it proposes 5–6 GtCO₂ per year as a more feasible benchmark. [S22]
- Current operational capacity is approximately 50–51 MtCO₂ per year, less than 1% of global emissions, indicating that even the 5–6 GtCO₂ benchmark would require roughly two orders of magnitude of growth. [S4] [S11] [S24]
- The IEA and other accumulated sources identify CCS as strategically useful mainly for hard-to-abate industry, selected retrofits, hydrogen, and carbon removal rather than as a universal substitute for direct emissions reductions. [S5] [S9]

#### Finding 2

**Claim**

Geological storage is potentially large but should be treated as a finite, geographically uneven and risk-constrained resource rather than as an effectively boundless sink.

**Confidence:** Medium

**Why this confidence level**

S22 is peer-reviewed and directly models geological and scale-up constraints. S21 is a journalistic account of a separate Nature study and provides useful figures, but the full study methods and results were not retrieved. S24 gives a concrete national example of the distinction between theoretical and usable resources.

**Evidence**

- The Nature study reports 11,800 GtCO₂ of mapped geological capacity but reduces the prudent usable estimate to about 1,460 Gt after excluding areas associated with water contamination, induced earthquakes, leakage risks, and proximity to populated areas. [S21]
- The study’s modeled feasible deployment depends heavily on particular regions, especially the United States, and finds that some IPCC deployment assumptions for China, Indonesia, and South Korea are difficult to realize. [S22]
- Geoscience Australia distinguishes demonstrated resources from sub-commercial resources requiring further exploration and appraisal, illustrating that nominal geological potential is not equivalent to commercially usable capacity. [S24]

#### Finding 3

**Claim**

Storage availability and permitting could become a practical bottleneck, especially for carbon removal and in regions without mature storage projects.

**Confidence:** Medium

**Why this confidence level**

The evidence is detailed for selected European countries and Australia but is not a complete global assessment. It nevertheless directly supports infrastructure and permitting as scalability constraints.

**Evidence**

- The European assessment reports that Finland has essentially no domestic geological storage, Germany has no operational storage sites and may require 7–10 years from exploration to commercial operation, and Spain has no operational storage sites despite estimated geological potential. [S25]
- The assessment says European climate pathways may require up to 600 MtCO₂ of annual combined CCS and CDR storage by 2050, while permitting, project concentration offshore, and cross-border export constraints limit near-term deployment. [S25]
- Geoscience Australia reports two operational commercial-scale full-chain projects as of December 2024, alongside many projects still in development or feasibility stages, showing that resource potential does not immediately translate into operating infrastructure. [S24]

#### Finding 4

**Claim**

The new evidence reinforces the case for prioritizing CCS in hard-to-abate industrial applications and durable removals, while weakening arguments for allocating scarce storage to applications with readily available alternatives.

**Confidence:** High

**Why this confidence level**

This application-specific conclusion is consistent with the IEA, WRI, prior reviews, and the new sources. It is a strategic implication rather than a direct measurement of comparative abatement costs.

**Evidence**

- The storage-feasibility study recommends judicious use of CCS for carbon-intensive applications that are difficult to replace with renewable alternatives, while noting opportunity costs such as transportation decarbonization. [S21]
- Geoscience Australia identifies iron, steel, aluminium, cement, chemicals, natural-gas processing and methane-based hydrogen as potential applications, and distinguishes dedicated geological abatement projects from utilization projects largely involving enhanced oil recovery. [S24]
- The European analysis reports that fossil CCS may take precedence over BECCS and DACCS in national plans, potentially leaving less storage for removals. [S25]

#### Finding 5

**Claim**

The new sources do not materially change the assessment of demonstrated effectiveness: CCS is technically demonstrated in individual projects, but global high-uptime, low-cost, net-lifecycle climate performance remains unproven.

**Confidence:** High

**Why this confidence level**

S24 adds an important classification of current projects but supplies no comprehensive independent dataset of uptime, lifecycle emissions, or long-term retention; the prior qualification therefore remains necessary.

**Evidence**

- Geoscience Australia reports around 46 commercial-scale projects capturing approximately 50 MtCO₂ per year globally, but says only about 14 have dedicated geological storage for carbon abatement while the remainder are largely utilization projects involving enhanced oil recovery. [S24]
- This distinction supports the existing finding that project counts and capture capacity are not equivalent to independently verified permanent climate mitigation, particularly where EOR is involved. [S24] [S18] [S19]
- The existing Petra Nova evidence continues to show that reported performance depends on system boundary: high capture efficiency at the processed slipstream does not establish whole-facility net emissions reduction or long-term permanence. [S16] [S17] [S18] [S19]

#### Finding 6

**Claim**

The new evidence adds no robust quantitative information that would narrow the existing wide cost and energy-penalty ranges.

**Confidence:** High

**Why this confidence level**

The absence of new cost and energy data is directly observable in the retrieved material; the accumulated ranges remain useful but heterogeneous.

**Evidence**

- The new sources discuss storage constraints, project development, and application choices but do not provide comparable global capture-energy or end-to-end cost estimates across sectors. [S21] [S22] [S24] [S25]
- The existing evidence remains the basis for the assessment that CCS commonly imposes material energy and financial penalties, with costs varying widely by source, technology, transport and storage conditions. [S1] [S7] [S13]

### Conflicts Found

- The new storage-capacity evidence is more restrictive than broad theoretical capacity estimates. S21 reports a prudent usable capacity of about 1,460 GtCO₂ after risk exclusions, while S22 finds that deployment could theoretically reach 16 GtCO₂ per year by 2050 but regards 5–6 GtCO₂ per year as a more feasible benchmark. These are not necessarily direct contradictions: one emphasizes cumulative prudent capacity and the other annual scale-up feasibility, and they use different methods and assumptions. [S21] [S22]
- S21 presents geological storage as potentially limited enough to reduce modeled climate benefits substantially, whereas the Global CCS Institute and S24 emphasize geological storage as safe, scalable, and strategically important. The disagreement concerns how much nominal capacity should count after risk, proximity, permitting, and social constraints are applied. [S21] [S23] [S24]
- S24 reports approximately 46 commercial-scale projects capturing about 50 MtCO₂ per year and says only around 14 have dedicated geological storage for abatement, whereas industry sources report larger project and storage-capability totals. The difference likely reflects project definitions and the distinction between capture, storage, utilization, and planned versus operating capacity. [S8] [S14] [S24]
- S25 argues that geological storage is a major European bottleneck for carbon removal, while broader industry perspectives describe storage as highly scalable. This is a conditional and regional disagreement: theoretical storage may be ample globally while accessible, permitted storage in particular countries and for particular uses is scarce. [S23] [S25]

### Important Gaps

- What are the full methods and uncertainties behind the 1,460 Gt prudent-storage estimate in the Nature study summarized by S21, and how does it compare with the methodology in S22?
- What is the independently verified global quantity of CO₂ actually captured and permanently stored, separated from nominal capacity, planned capacity, and EOR utilization?
- What are comparable facility-level capture rates, uptime, energy use, net lifecycle emissions, and long-term retention for major projects?
- How much permitted and monitored storage capacity and transport infrastructure can be delivered at 5–6 GtCO₂ per year, rather than merely identified geologically?
- How do sector-specific CCS costs and energy penalties compare with electrification, efficiency, renewable hydrogen, and alternative industrial processes?
- What share of projected CCS deployment represents fossil-source abatement versus durable carbon removal, and how should storage competition between these uses be managed?
- What long-term leakage rates, monitoring obligations, and post-closure liability arrangements apply across storage settings?

**Analysis Duration:** 21.88s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The accumulated and new evidence can support a responsible answer to the original question: CCS is technically demonstrated but currently tiny, costly and energy-intensive; it could make a substantial targeted contribution if scaled dramatically, especially in hard-to-abate industry and removals, but it should complement rather than replace direct emissions cuts. Remaining gaps concern precision and project-level verification rather than the central conclusion, and another broad search is unlikely to materially change it.

**Stop Reason:** sufficient_evidence

---

# Final Research Decision

**Research Stopped Because**

The analyzer determined that the important parts of the question could be answered responsibly.

**Stop Reason:** sufficient_evidence

**Searches Performed:** 5

**Unique Sources:** 25

**Remaining Uncertainty**

- A standardized, independently audited global dataset separating nominal capacity, actual capture, permanent geological storage and CO₂ utilization is still needed.
- Comparable facility-level data on uptime, energy consumption, capture rates, whole-system emissions and lifecycle climate performance are not available in the retrieved material.
- The full methods and uncertainties behind the risk-adjusted 1,460 GtCO₂ storage estimate have not been retrieved or compared systematically with other storage assessments.
- The amount of permitted and monitored storage and transport infrastructure that can operate at 5–6 GtCO₂ per year remains uncertain.
- The retrieved sources do not provide robust, sector-by-sector comparisons between CCS and electrification, efficiency, renewable hydrogen or alternative industrial processes.
- Long-term leakage rates, post-closure monitoring and liability arrangements are not quantified consistently across storage settings.
- The proportion of projected CCS deployment that would represent fossil-source abatement rather than durable carbon removal remains unresolved.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 5 | 14.79s |
| OpenAI Analysis | 5 | 95.88s |
| Report Generation | 1 | 20.32s |
| Total Run | — | 130.99s |
