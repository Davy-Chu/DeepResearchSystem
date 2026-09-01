# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

Can carbon capture and storage make a significant contribution to reducing global CO₂ emissions? Evaluate its demonstrated effectiveness, costs, scalability, energy requirements, and major arguments for and against large-scale deployment.

**Status:** Completed

**Stop Reason:** sufficient_evidence

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 7 / 10

**Unique Sources:** 27

**OpenAI Calls:** 8

**Tavily Calls:** 7

**Started:** 2026-09-01T04:48:52-04:00

**Ended:** 2026-09-01T04:51:57-04:00

**Total Runtime:** 185.21s

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
- **S2 — A Comprehensive Review of Carbon Capture, Storage, and Reduction Strategies Within the Built Environment**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12735339
- **S3 — The Environmental and Economic Sustainability of Carbon Capture and Storage**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC3108120
- **S4 — Carbon Capture and Storage (CCS): The Future of Climate Change Mitigation - Verde AgriTech - Blog (english)**
  URL: https://blog.verde.ag/en/carbon-capture-and-storage-ccs
- **S5 — Carbon capture and storage - Wikipedia**
  URL: https://en.wikipedia.org/wiki/Carbon_capture_and_storage

**Search Duration:** 4.06s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

CCS could make a meaningful contribution in particular hard-to-abate industrial sectors, but the provided evidence does not support treating it as a broad or dominant global emissions solution.

**Confidence:** Medium

**Why this confidence level**

The sector-specific qualification is supported by two scholarly reviews, but the sources provide little independent quantitative evidence of CCS's achievable global contribution.

**Evidence**

- The 2026 evidence-based review says CCS should not be categorically dismissed and identifies cement and legacy infrastructure retrofits as strategic applications where alternatives may be limited, while warning against relying on CCS generally. [S1]
- A sustainability review states that CCS is not applicable to every industry and that its role must be evaluated alongside other mitigation options and wider environmental and social impacts. [S3]
- The blog identifies cement, steel, and chemical production as potential applications and presents CCS as relevant to global climate goals, but this is advocacy-oriented secondary material. [S4]

#### Finding 2

**Claim**

Demonstrated deployment is currently very small relative to global CO₂ emissions, and several projects have experienced shortcomings involving capture performance, costs, or storage claims.

**Confidence:** Medium

**Why this confidence level**

S1 provides a direct quantitative claim and project critique, while S4 confirms that notable projects exist but is not an independent performance audit. The evidence is insufficient to establish a comprehensive global project record.

**Evidence**

- S1 reports that, despite more than $40 billion in global investment, CCS captures and stores less than 0.1% of annual global CO₂ emissions. It also cites Petra Nova, Gorgon, Sleipner, and In Salah as case studies involving recurring concerns such as cost overruns, suboptimal capture rates, geological uncertainty, and disputed assessments of durability or emissions offsets. [S1]
- S4 cites Sleipner and Petra Nova as operating large-scale projects and describes them as demonstrations of technical viability, although Petra Nova's use of CO₂ for enhanced oil recovery complicates its climate assessment. [S4]

#### Finding 3

**Claim**

CCS is energy- and capital-intensive, with costs varying widely by source concentration, technology, and project conditions.

**Confidence:** Medium

**Why this confidence level**

The ranges and qualitative cost concerns come from scholarly reviews, but the supplied material does not show their underlying assumptions, technology boundaries, currency basis, or how costs differ among power, industry, and direct-air-capture applications.

**Evidence**

- S1 gives an indicative energy requirement of 2.5–8 GJ per tonne of CO₂ and a cost range of $50–600 per tonne of CO₂, emphasizing variation by emissions context, scalability, and permanence. [S1]
- S3 characterizes CCS as one of the more expensive and technically challenging abatement options and says its full lifecycle assessment must include capital, energy, operating, environmental, and social costs. [S3]
- S1 links project failures and underperformance to cost overruns and identifies energy demand as a key comparison criterion. [S1]

#### Finding 4

**Claim**

Large-scale CCS faces significant infrastructure, storage, monitoring, liability, and environmental-risk challenges.

**Confidence:** Medium

**Why this confidence level**

The sources consistently identify these as important risks, but the retrieved excerpts do not quantify leakage probabilities, storage capacity, transport needs, water use, or the effectiveness of monitoring and regulatory systems.

**Evidence**

- S1 identifies geological uncertainty and public-liability transfer as recurring issues, and evaluates storage in terms of durability and permanence rather than capture alone. [S1]
- S4 notes the need for suitable storage sites and raises safety and environmental-impact concerns as barriers to large-scale implementation. [S4]
- S3 says sustainability requires long-term protection of the environment and human health and requires consideration of water, NOx, SOx, biodiversity, energy, and safety tradeoffs. [S3]

#### Finding 5

**Claim**

The main argument for deployment is that CCS can reduce emissions from concentrated industrial processes and potentially preserve options where direct substitution is difficult; the main arguments against broad deployment are poor demonstrated scale, high and uncertain costs, energy penalties, storage/permanence risks, and possible delay of more effective alternatives.

**Confidence:** Medium

**Why this confidence level**

The argument structure is consistent across the sources, but the pro-deployment case relies partly on a non-peer-reviewed blog and the comparative effectiveness of alternatives is not quantitatively established in the supplied material.

**Evidence**

- S1 supports targeted deployment in hard-to-abate sectors while warning that continued reliance on CCS may delay renewables, bio-based removals, and mineralization. [S1]
- S3 frames CCS as one component of an optimized mitigation portfolio, not a universally suitable technology, and stresses comparison with alternatives and full lifecycle impacts. [S3]
- S4 presents continued fossil-fuel use with reduced emissions, industrial capture, policy incentives, and climate-goal contribution as arguments for CCS, while acknowledging high cost, storage availability, and safety challenges. [S4]

### Conflicts Found

- S1 presents current CCS deployment as less than 0.1% of annual global CO₂ emissions and emphasizes missed promises and underperformance, whereas S4 describes existing projects as demonstrating viability and states that CCS could contribute up to 13% of required emissions reductions by 2060. These claims are not necessarily logically incompatible: technical viability and modeled future contribution can coexist with very limited current deployment, but S4's modeled contribution is not substantiated in the excerpt. [S1] [S4]
- S1 characterizes CCS as a high-cost gamble that risks delaying more effective solutions, while S3 and S4 retain a more favorable conditional role for CCS. The disagreement concerns the breadth and strategic priority of deployment, not whether CCS has any possible application. [S1] [S3] [S4]

### Important Gaps

- What is the independently verified current global capture and permanent-storage capacity, distinguished from CO₂ captured for enhanced oil recovery or utilization?
- What capture rates, uptime, net lifecycle emissions reductions, and storage permanence have actually been demonstrated across major CCS projects?
- How do levelized costs and energy penalties compare by application—cement, steel, hydrogen, power, natural-gas processing, and direct air capture—and under what assumptions do they fall?
- What is the realistically available geological storage capacity, including transport infrastructure, monitoring requirements, leakage risk, and long-term liability arrangements?
- How much CCS is represented in robust, authoritative net-zero scenarios, and how sensitive are those scenarios to deployment delays, cost overruns, and competing options?

**Analysis Duration:** 22.90s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The current sources support a cautious qualitative assessment, but important parts of the question—especially demonstrated effectiveness, verified scale, project-level costs and energy requirements, and authoritative estimates of future global contribution—remain inadequately documented. A focused search for authoritative current deployment and performance data would materially improve the answer.

**Next Search**

> IEA Global CCS Institute 2024 2025 CCS projects captured stored CO2 capacity capture rates costs energy penalty

---

# Iteration 2

## 1. Search

**Query**

> IEA Global CCS Institute 2024 2025 CCS projects captured stored CO2 capacity capture rates costs energy penalty

**Why this query**

The current sources support a cautious qualitative assessment, but important parts of the question—especially demonstrated effectiveness, verified scale, project-level costs and energy requirements, and authoritative estimates of future global contribution—remain inadequately documented. A focused search for authoritative current deployment and performance data would materially improve the answer.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S6 — Report Finds Growing CCS Sector**
  URL: https://jpt.spe.org/report-finds-growing-ccs-sector
- **S7 — A closer look at CCS: Problems and potential - Zero Carbon Analytics**
  URL: https://zerocarbon-analytics.org/insights/briefings/a-closer-look-at-ccs-problems-and-potential
- **S8 — Publications Archive | Global CCS Institute**
  URL: https://www.globalccsinstitute.com/publications
- **S9 — CCUS projects around the world are reaching new milestones – Analysis - IEA**
  URL: https://www.iea.org/commentaries/ccus-projects-around-the-world-are-reaching-new-milestones
- **S10 — A new era for CCUS – CCUS in Clean Energy Transitions – Analysis - IEA**
  URL: https://www.iea.org/reports/ccus-in-clean-energy-transitions/a-new-era-for-ccus

**Search Duration:** 4.10s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Current CCS/CCUS deployment remains small, although the project pipeline is expanding rapidly.

**Confidence:** High

**Why this confidence level**

The IEA provides a direct, recent assessment and the industry publication independently indicates a similar order of magnitude, though the reported 50 Mt and 64 Mt figures likely reflect different definitions or facility datasets.

**Evidence**

- The IEA reports just over 50 Mt CO₂ per year of capture-and-storage capacity in operation in the first quarter of 2025, with projected capture capacity of about 430 MtCO₂ per year by 2030 based on the existing pipeline. It explicitly states that current trends are insufficient for a net-zero-by-mid-century pathway. [S9]
- The Journal of Petroleum Technology, reporting the Global CCS Institute’s 2025 status report, states that 77 facilities have operating storage capability of 64 MtCO₂ per year, with another 44 MtCO₂ per year under construction and a projected fivefold increase in operating capture capacity by 2030. [S6]
- The IEA reports that eight projects began operating in 2024, but most were small, some with capacity as low as 5,000 tonnes per year; consequently, total operating capacity increased only marginally. [S9]

#### Finding 2

**Claim**

The strongest case for CCS is targeted use in hard-to-abate sectors and for some existing industrial assets, not reliance on CCS as a general substitute for rapid emissions reduction.

**Confidence:** High

**Why this confidence level**

The sector-specific role is supported by the IEA and a separate analytical briefing; the 8 Gt figure is a modeled strategic rationale, not demonstrated abatement.

**Evidence**

- The IEA identifies cement, iron and steel, chemicals, retrofits of existing facilities, low-carbon hydrogen, and—in combination with bioenergy or direct air capture—carbon removal as strategic applications where alternatives may be limited. [S10]
- The IEA says CCUS could address emissions from existing power and industrial plants that might otherwise emit 8 GtCO₂ in 2050, while also describing historical deployment as slow and its global impact as limited. [S10]
- Zero Carbon Analytics likewise concludes that CCS has potential in difficult-to-decarbonise sectors, but says most existing projects are associated with oil and gas and that non-oil-and-gas applications remain limited. [S7]

#### Finding 3

**Claim**

A substantial share of existing CCS capacity has been associated with oil and gas production or enhanced oil recovery, weakening the inference that current deployment demonstrates broad climate effectiveness.

**Confidence:** Medium

**Why this confidence level**

The sources clearly document the historical concentration in oil and gas, but S7 is an advocacy-oriented analysis and the figures use a different project count and may not be directly comparable with the IEA and Global CCS Institute datasets.

**Evidence**

- Zero Carbon Analytics reports that almost all of the world’s 41 operational CCS projects were connected to oil and gas and that 82.5% of existing CCS capacity used captured CO₂ for enhanced oil recovery. [S7]
- The briefing explains that EOR uses injected CO₂ to extract additional oil, so storage claims in such projects must be assessed separately from the additional emissions associated with producing and using the recovered oil. [S7]
- The IEA reports that more than 60% of operational capture capacity remains at natural-gas-processing facilities, while projects in hydrogen, carbon removal, and industry constitute over half of the projects that could operate by 2030. [S9]

#### Finding 4

**Claim**

CCS can make a significant future contribution in absolute terms only if the announced pipeline is delivered and expanded substantially; the evidence does not yet establish that this scale is achievable or that it will be sufficient globally.

**Confidence:** Medium

**Why this confidence level**

The numerical pipeline evidence is relatively strong, but announced or planned capacity is not equivalent to completed, continuously operating, independently verified and permanently stored CO₂.

**Evidence**

- The IEA projects approximately 430 MtCO₂ per year of capture capacity by 2030 from the current pipeline, but says present trends remain insufficient for a net-zero pathway. [S9]
- The Global CCS Institute’s reported pipeline includes 44 MtCO₂ per year under construction and anticipates a fivefold increase in operating capture capacity between 2025 and 2030. [S6]
- The IEA characterizes CCS deployment to date as having a history of unmet expectations and slow progress, despite recognizing substantial strategic value in net-zero transitions. [S10]

#### Finding 5

**Claim**

The principal arguments against broad CCS deployment remain high and uncertain costs, energy requirements, dependence on infrastructure and suitable storage, permanence and liability concerns, and the risk of diverting resources from alternatives.

**Confidence:** Medium

**Why this confidence level**

The objections are consistently identified, but the supplied material does not provide a common, application-specific accounting framework for net energy use, lifecycle emissions, costs, leakage, or opportunity costs.

**Evidence**

- Prior review evidence estimates energy requirements of 2.5–8 GJ per tonne of CO₂ and costs of roughly $50–600 per tonne, with large variation by source and project conditions. [S1]
- The IEA notes that CCUS investment historically accounted for less than 0.5% of global investment in clean-energy and efficiency technologies and describes deployment as slow and underperforming relative to earlier expectations. [S10]
- Prior sources identify geological uncertainty, long-term liability, monitoring, safety, environmental effects, and possible delay of renewables and other mitigation options as major concerns. [S1] [S3]
- Zero Carbon Analytics states that proposed projects have often depended on government support and that EOR-oriented subsidies can support continued oil production rather than unambiguously deliver net emissions reductions. [S7]

### Conflicts Found

- The IEA reports just over 50 MtCO₂ per year of operating capture-and-storage capacity in early 2025, while the Global CCS Institute report summarized by JPT gives 64 MtCO₂ per year of operating storage capability across 77 facilities. These are likely definitional or dataset differences—such as capture versus storage capacity, inclusion criteria, or facility boundaries—rather than a direct contradiction, but the sources cannot be combined into one precise global total. [S6] [S9]
- The IEA presents CCUS as strategically valuable for hard-to-abate sectors and potential net-zero pathways, while Zero Carbon Analytics emphasizes that current capacity is predominantly linked to oil and gas and EOR. These positions differ mainly over how much current deployment demonstrates climate effectiveness and how broadly CCS should be promoted. [S7] [S9] [S10]
- S6 reports strong sector growth and infrastructure expansion, whereas S9 says the increase in operating capacity during 2024 was marginal and that current trends remain insufficient for net zero. Growth in announced or nominal capacity is therefore not equivalent to demonstrated emissions reductions. [S6] [S9]

### Important Gaps

- What explains the discrepancy between the IEA’s approximately 50 MtCO₂ per year of operating capacity and the Global CCS Institute’s 64 MtCO₂ per year of storage capability?
- What fraction of reported operating capacity results in verified permanent geological storage rather than EOR or utilization, and what are the associated net lifecycle emissions?
- What are the independently measured capture rates, uptime, energy penalties, costs, and leakage or permanence records for projects outside natural-gas processing and EOR?
- How much of the announced 2030 pipeline will reach final investment decision, construction completion, and sustained operation?
- What application-specific cost and energy comparisons show where CCS is preferable to electrification, process changes, hydrogen, renewable energy, or material substitution?
- What authoritative net-zero scenarios quantify CCS’s required contribution and test sensitivity to delays, cost overruns, and storage or transport constraints?

**Analysis Duration:** 17.87s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources materially strengthen the evidence on current deployment, project-pipeline growth, and the sectoral concentration of CCS. However, the central evaluation still lacks comparable independent evidence on net lifecycle effectiveness, application-specific costs and energy requirements, and the fraction of planned capacity likely to operate. One focused search on authoritative project performance and lifecycle metrics would most improve the answer.

**Next Search**

> IEA Global CCS Institute verified CCS project capture rates energy penalty cost lifecycle emissions permanent storage EOR comparison

---

# Iteration 3

## 1. Search

**Query**

> IEA Global CCS Institute verified CCS project capture rates energy penalty cost lifecycle emissions permanent storage EOR comparison

**Why this query**

The new sources materially strengthen the evidence on current deployment, project-pipeline growth, and the sectoral concentration of CCS. However, the central evaluation still lacks comparable independent evidence on net lifecycle effectiveness, application-specific costs and energy requirements, and the fraction of planned capacity likely to operate. One focused search on authoritative project performance and lifecycle metrics would most improve the answer.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S11 — Power CCS: Potential for cost reductions and improvements**
  URL: https://ieaghg.org/publications/2024-04%20Power%20CCS%20-%20potential%20for%20cost%20reductions%20and%20improvements.pdf
- **S12 — Potential of CO2-enhanced oil recovery coupled with carbon capture and storage in mitigating greenhouse gas emissions in the UAE - ScienceDirect**
  URL: https://www.sciencedirect.com/science/article/abs/pii/S1750583621002371
- **S13 — Carbon Capture and Storage Projects**
  URL: https://acrcarbon.org/wp-content/uploads/2023/03/ACR-CCS-v1.1-2024-08-13.pdf
- **S14 — Frontiers | Potential of CO2-EOR for Near-Term Decarbonization**
  URL: https://www.frontiersin.org/journals/climate/articles/10.3389/fclim.2019.00005/full
- **S15 — Carbon Capture vs Renewable Energy**
  URL: https://energytracker.asia/carbon-capture-vs-renewable-energy

**Search Duration:** 3.54s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Commercial-scale power-sector CCS remains demonstrated at only a handful of plants, and further cost reductions are still considered necessary.

**Confidence:** High

**Why this confidence level**

This is a direct statement from a recent technical report, although the report is focused specifically on power CCS rather than the entire CCS sector.

**Evidence**

- The IEAGHG 2024 technical report identifies only four thermal power plants with commercial-scale capture deployment—Boundary Dam, Petra Nova, Jinjie, and Taizhou—while describing additional projects as pilots or proposals. It states that continued reductions in both capital and operating costs are essential for competitiveness, especially as traditional generators operate less often alongside variable renewables. [S11]

#### Finding 2

**Claim**

Power CCS may provide dispatchable low-carbon generation in some modeled systems, but this is prospective system modeling rather than demonstrated global emissions performance.

**Confidence:** Medium

**Why this confidence level**

The report provides modeled results and a relevant conditional rationale, but the findings depend on the study’s assumptions and do not demonstrate that power CCS is generally cheaper or preferable to renewables.

**Evidence**

- The IEAGHG report’s UK 2035 case study finds that power CCS can be cost-effective and provide flexible, dispatchable generation, and identifies pre-combustion blue-hydrogen combined-cycle technology as the most economical power-CCS option in its modeled alternatives. The same case study finds a system with high variable-renewable penetration has similar or slightly lower generation costs than a system relying only on dispatchable low-carbon generation. [S11]

#### Finding 3

**Claim**

CO₂-EOR can provide substantial CO₂ storage in some circumstances, but claims of net climate benefit are highly dependent on lifecycle-accounting boundaries and operational choices.

**Confidence:** Medium

**Why this confidence level**

S14 is a peer-reviewed review and directly documents the conditional nature of EOR climate claims, but it does not establish a general net-negative result for EOR projects.

**Evidence**

- The Frontiers review reports that some dynamic lifecycle analyses find CO₂-EOR oil can be net carbon negative during much of an operation because a large fraction of injected CO₂ remains trapped underground. It also notes that other lifecycle studies differ and that comparisons are difficult because studies use different emissions-accounting boundaries, including whether downstream refining and fuel combustion are included. [S14]
- The UAE article’s retrieved material identifies cost and carbon-pricing conditions as important determinants of CO₂-EOR/CCS feasibility, but the accessible excerpt does not provide quantified emissions results. [S12]

#### Finding 4

**Claim**

Credible CCS accounting requires explicit treatment of emissions from capture, transport, storage, and leakage, supported by monitoring, reporting, and verification.

**Confidence:** High

**Why this confidence level**

The source directly specifies the accounting and MRV components, though it is a crediting methodology rather than empirical evidence about how well existing projects perform.

**Evidence**

- The ACR methodology defines procedures for calculating baseline emissions, capture emissions, transport emissions, storage emissions, and atmospheric leakage, and requires a monitoring, reporting, and verification plan with validation and verification requirements. [S13]

#### Finding 5

**Claim**

The new sources reinforce a targeted rather than universal role for CCS, particularly by weakening the case for fossil-power CCS as a general replacement for renewable deployment.

**Confidence:** Medium

**Why this confidence level**

These sources support a conditional role, consistent with the prior IEA and review evidence, but they do not provide a comprehensive comparison across all sectors or mitigation alternatives.

**Evidence**

- S11 presents power CCS as potentially useful for flexible dispatchable generation but also states that high variable-renewable systems can have similar or slightly lower generation costs and that cost reductions remain essential. [S11]
- S14 frames EOR-based CCS as a transitional strategy and explicitly acknowledges environmental arguments that it may prolong fossil-fuel use; its claimed benefits depend on specific operational and accounting conditions. [S14]

### Conflicts Found

- S11 describes power CCS as cost-effective in its UK modeled systems and as potentially essential for decarbonizing traditional generators, while prior evidence and S15 argue that fossil-fuel CCS is generally more costly and less efficient than renewables. This is a conditional disagreement involving system assumptions, technology configuration, and the role assigned to dispatchable generation; it is not evidence that power CCS has been broadly demonstrated as the lowest-cost option. [S11] [S15] [S9] [S10]
- S14 presents studies finding that CO₂-EOR can produce net-negative-emissions oil under particular operational choices, whereas prior evidence and S7 emphasize that EOR can prolong oil production and complicate claims of permanent net reductions. S14 itself acknowledges that lifecycle studies use differing system boundaries, so the disagreement cannot be resolved from the retrieved material. [S14] [S7] [S1] [S13]
- S11’s statement that CCS will be essential in the power sector is a strong technology-policy judgment, while the same report’s UK case study finds high-renewable systems have similar or slightly lower generation costs. These claims can coexist if CCS is treated as a strategic option for residual dispatchable capacity rather than the dominant generation technology, but the source does not establish how much power CCS is actually required. [S11]

### Important Gaps

- What are the independently measured capture rates, uptime, net lifecycle emissions, and costs of the four commercial-scale power CCS plants identified by S11?
- How much of operating CCS capacity produces verified permanent storage rather than EOR-related storage, and how should downstream emissions from recovered oil be counted?
- Do the favorable power-CCS results in S11 persist under alternative assumptions about renewable costs, storage, fuel prices, utilization rates, hydrogen production, and carbon transport infrastructure?
- What share of announced CCS projects will reach operation and sustain high capture performance?
- What application-specific cost and energy comparisons establish where CCS is preferable to electrification, process substitution, renewable generation, or material efficiency?
- What is the independently verified global total of CO₂ permanently stored, distinguished from nominal capture or storage capacity?

**Analysis Duration:** 16.29s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources improve the assessment of power-sector demonstrations, EOR accounting, and MRV requirements, but the most important quantitative gaps remain: independently verified project performance, net lifecycle reductions, application-specific costs and energy penalties, and the amount of permanent storage actually achieved. A focused search could materially improve the answer by obtaining audited or authoritative data on operating projects.

**Next Search**

> independent assessment operating CCS projects capture rate uptime energy penalty cost permanent storage lifecycle emissions Boundary Dam Petra Nova Gorgon Sleipner 2024

---

# Iteration 4

## 1. Search

**Query**

> independent assessment operating CCS projects capture rate uptime energy penalty cost permanent storage lifecycle emissions Boundary Dam Petra Nova Gorgon Sleipner 2024

**Why this query**

The new sources improve the assessment of power-sector demonstrations, EOR accounting, and MRV requirements, but the most important quantitative gaps remain: independently verified project performance, net lifecycle reductions, application-specific costs and energy penalties, and the amount of permanent storage actually achieved. A focused search could materially improve the answer by obtaining audited or authoritative data on operating projects.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S16 — What Are The Top 6 Carbon Capture Plants For Permanent CO2 Storage? - Carbon Herald**
  URL: https://carbonherald.com/top-6-carbon-capture-plants-permanent-storage
- **S17 — The Carbon Capture Crux**
  URL: https://ieefa.org/sites/default/files/2022-09/The+Carbon+Capture+Crux.pdf
- **S18 — Boundary Dam or Petra Nova – Which is a better model for CCS ...**
  URL: https://www.sciencedirect.com/science/article/abs/pii/S1750583618307436

**Search Duration:** 5.35s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources provide further examples of large CCS projects, but do not materially establish their independently verified capture performance, net lifecycle emissions, costs, or permanence.

**Confidence:** Medium

**Why this confidence level**

The sources add corroboration that deployment is concentrated in a small number of projects and that underperformance is a documented concern, but the available excerpts lack detailed, independently verified operating data.

**Evidence**

- Carbon Herald lists Gorgon, Quest, Wabash, Sleipner, Snøhvit, and Illinois as prominent CCS projects, but the retrieved material is primarily descriptive and advocacy-oriented; it does not provide a consistent independent performance assessment. [S16]
- The IEEFA report states that several natural-gas-processing projects have underperformed their designed capture rates and examines In Salah, Petra Nova, Kemper, and Boundary Dam, but the retrieved excerpt does not provide the underlying quantitative results. [S17]
- A peer-reviewed article describes Boundary Dam and Petra Nova as the only commercial-scale coal-fired power plants using CCS at the time of publication, reinforcing that power-sector demonstration has been limited. [S18]

#### Finding 2

**Claim**

The evidence continues to support a distinction between technical feasibility and demonstrated large-scale climate effectiveness.

**Confidence:** High

**Why this confidence level**

The distinction is supported by both deployment data and project-level evidence: modeled future capacity and existence of operating plants do not demonstrate that the required scale, capture rates, and storage permanence have been achieved.

**Evidence**

- S16 presents CCS as applicable to industrial facilities and power plants and cites modeled US 2050 pathways involving substantial capture and storage, but these are prospective scenarios rather than evidence of achieved global deployment. [S16]
- S17 indicates that even within sectors containing successful projects, some facilities have operated below their designed capture rates. [S17]
- S9 and S10 previously report that operating capacity remains small and that historical deployment has been slow relative to net-zero requirements. [S9] [S10]

### Conflicts Found

- S16 uses favorable language about CCS's importance and cites modeled future capture and storage volumes, whereas S17 emphasizes underperformance in several projects. This is not a direct contradiction because modeled potential and technical feasibility can coexist with poor or inconsistent operating performance, but S16 does not establish that its projected volumes are deliverable. [S16] [S17]
- S16 reports historical counts and capacity figures for CCS facilities that differ from the more recent IEA and Global CCS Institute figures in the prior evidence. The discrepancy likely reflects publication date, project definitions, and whether facilities are operating, planned, or under development; the figures should not be combined as a single time series without methodological clarification. [S16] [S6] [S9]

### Important Gaps

- What quantitative capture rates, uptime, energy penalties, costs, and net lifecycle emissions were actually achieved at In Salah, Petra Nova, Kemper, Boundary Dam, Gorgon, Quest, Sleipner, and Snøhvit?
- How much CO₂ from the projects listed by S16 has been permanently stored, as distinct from captured, transported, injected for EOR, or otherwise utilized?
- Which of the reported project and capacity figures use comparable definitions of operating capture capacity, storage capability, and permanent storage?
- How representative are the four commercial-scale power projects of future power-sector CCS, given their differing designs, utilization rates, subsidies, and EOR arrangements?

**Analysis Duration:** 10.74s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The central conclusion is already supportable: CCS can make a potentially significant targeted contribution, especially in hard-to-abate industry, but current deployment is too small and performance evidence too limited to justify treating it as a dominant global solution. However, an important requested element—demonstrated effectiveness—still lacks project-level independent data on capture rates, uptime, net emissions, and permanent storage. The new sources flag this gap but do not resolve it.

**Next Search**

> independent review CCS project performance capture rate uptime net CO2 reduction Boundary Dam Petra Nova Gorgon Quest In Salah

---

# Iteration 5

## 1. Search

**Query**

> independent review CCS project performance capture rate uptime net CO2 reduction Boundary Dam Petra Nova Gorgon Quest In Salah

**Why this query**

The central conclusion is already supportable: CCS can make a potentially significant targeted contribution, especially in hard-to-abate industry, but current deployment is too small and performance evidence too limited to justify treating it as a dominant global solution. However, an important requested element—demonstrated effectiveness—still lacks project-level independent data on capture rates, uptime, net emissions, and permanent storage. The new sources flag this gap but do not resolve it.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S19 — Petra Nova is one of two carbon capture and sequestration power plants in the world -
		U.S. Energy Information Administration (EIA)**
  URL: https://www.eia.gov/todayinenergy/detail.php?id=33552
- **S20 — Carbon capture and storage: What can we learn from the ...**
  URL: https://www.catf.us/resource/carbon-capture-storage-what-can-learn-from-project-track-record
- **S21 — The ill-fated Petra Nova CCS project: NRG Energy throws in the towel | IEEFA**
  URL: https://ieefa.org/resources/ill-fated-petra-nova-ccs-project-nrg-energy-throws-towel

**Search Duration:** 3.59s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Petra Nova demonstrates that large-scale power-sector CCS is technically possible, but its climate performance and economics are disputed and its operation was not sustained continuously.

**Confidence:** Medium

**Why this confidence level**

EIA provides direct technical and scope information, while IEEFA supplies a more critical interpretation of operating and financial performance. The precise effective capture rate remains contested because the underlying owner data were not publicly provided.

**Evidence**

- The EIA reports that Petra Nova’s capture system began operating in 2017, was designed to capture about 90% of CO₂ from the treated flue-gas slipstream, and captured roughly 33% of total Unit 8 emissions because only about 37% of the unit’s emissions passed through the system. It also states that the process required a dedicated natural-gas unit to supply capture energy. [S19]
- IEEFA reports that Petra Nova was taken offline in May 2020 after technical problems and downtime involving the capture plant, coal unit, pipeline, and EOR field. It argues, using EPA emissions data, that the effective capture rate may have been approximately 65–70% before accounting for emissions from the gas-fired energy supply, or approximately 55–58% including those emissions. [S21]
- IEEFA reports that the project received substantial public and concessional financing, that the owners recorded approximately $310 million in impairment charges, and that one owner later sold its stake for about $3.6 million relative to roughly $1 billion in construction costs. [S21]

#### Finding 2

**Claim**

The historical CCS project record contains both successful high-performing projects and significant underperformance; therefore, technical feasibility should not be equated with consistently achieved climate abatement.

**Confidence:** High

**Why this confidence level**

The sources provide complementary evidence: CATF documents successful and challenging projects across sectors, while EIA and IEEFA provide a detailed power-sector counterexample. CATF is an advocacy organization, so its project classifications should still be interpreted with some caution.

**Evidence**

- CATF identifies Sleipner, the Alberta Carbon Trunk Line, and Quest as projects that consistently achieved high technical performance, while also documenting operational challenges and noting that some projects prioritize commercial or demonstration objectives over maximizing climate benefit. [S20]
- CATF states that only 41 commercial CCS projects were operating at the time of its assessment and that most were not developed primarily for climate purposes, with many using CO₂ for enhanced oil recovery. [S20]
- IEEFA characterizes Petra Nova and Kemper as examples of poor performance or financial risk in fossil-fuel power applications, while the EIA confirms that Kemper abandoned its planned coal-gasification CCS system and operates as a natural-gas combined-cycle plant. [S19] [S21]

#### Finding 3

**Claim**

Power-sector CCS has not yet demonstrated broad, economically competitive scalability, especially when capture is applied to only part of a plant and requires additional energy infrastructure.

**Confidence:** High

**Why this confidence level**

The evidence directly documents the limited number of power projects, partial capture configuration, large capital requirements, energy supply needs, and a major cost overrun. It does not establish that all future power CCS projects would have the same costs.

**Evidence**

- The EIA describes Petra Nova as one of only two operating CCS power plants worldwide in 2017, with a 240 MW capture system treating a slipstream of a 654 MW coal unit rather than the plant’s full emissions. [S19]
- The EIA reports Petra Nova retrofit costs of approximately $1 billion, or about $4,200 per kilowatt, and states that its capture process required a dedicated natural-gas unit for energy. [S19]
- IEEFA reports that Kemper’s estimated capital cost increased from roughly $2.4–3 billion to more than $7.5 billion before the CCS-related coal-gasification approach was abandoned. [S19] [S21]
- The IEAGHG evidence previously found only four commercial-scale thermal power plants with CCS and stated that further capital and operating-cost reductions remain essential. [S11]

#### Finding 4

**Claim**

The new evidence strengthens the case for distinguishing climate-oriented geological storage from CO₂ use in enhanced oil recovery.

**Confidence:** High

**Why this confidence level**

The sources consistently show that EOR is common and that its net climate effect depends on lifecycle boundaries. They do not establish one universal net-emissions result for EOR.

**Evidence**

- CATF states that many operating projects were motivated by commercial CO₂ sales for EOR rather than by maximizing atmospheric emissions reductions, while climate-oriented projects increasingly need saline-aquifer storage that adds transport and disposal costs. [S20]
- Both the EIA and IEEFA state that Petra Nova sent captured CO₂ through an 80-mile pipeline for EOR, meaning its storage result must be assessed alongside the emissions associated with additional oil production and use. [S19] [S21]
- The prior Frontiers review found that EOR lifecycle studies reach differing conclusions depending on operational choices and whether downstream refining and fuel combustion are included. [S14]

#### Finding 5

**Claim**

CCS could make a significant future contribution, but only as a targeted component of a much larger mitigation portfolio and not as a demonstrated substitute for rapid emissions reduction.

**Confidence:** High

**Why this confidence level**

The conclusion is supported by current deployment data, sector-specific rationale, and project-track-record evidence. The future contribution remains conditional because announced capacity is not equivalent to sustained, independently verified permanent storage.

**Evidence**

- CATF reports that climate pathways require several billion tonnes of geological CO₂ storage annually by 2050, compared with current experience at a much smaller scale, and argues that high-performing projects must become more common. [S20]
- The IEA previously estimated just over 50 MtCO₂ per year of operating capture-and-storage capacity in early 2025 and approximately 430 MtCO₂ per year by 2030 from the existing pipeline, while stating that current trends remain insufficient for a net-zero pathway. [S9]
- The IEA identifies cement, steel, chemicals, retrofits, low-carbon hydrogen, and carbon removal as strategic applications where alternatives may be limited; the supplied evidence does not show comparable demonstrated scale in these sectors. [S10]

### Conflicts Found

- The EIA reports that Petra Nova’s capture equipment was designed for approximately 90% capture from the treated slipstream and that the project was completed on budget and on time, whereas IEEFA argues that actual effective capture may have been only 55–58% after accounting for the capture system’s gas-fired energy supply and that the project suffered substantial financial losses. The disagreement reflects different boundaries and source perspectives; the retrieved material does not resolve the true net capture rate or full project economics. [S19] [S21]
- CATF identifies several projects as consistently high-performing, while IEEFA emphasizes failures and underperformance in fossil-power CCS. These are not necessarily contradictory because they concern different projects and sectors, but they imply that performance is heterogeneous and that successful examples may not be representative of fossil-power retrofits. [S20] [S21]
- The EIA describes Petra Nova as a completed, on-time retrofit, while IEEFA treats its later mothballing, impairments, and ownership sale as evidence of financial failure. Both can be true: construction execution was comparatively successful even if long-term commercial operation was not. [S19] [S21]

### Important Gaps

- What independently verified capture rate, uptime, energy consumption, and net lifecycle emissions did Petra Nova achieve during its operating period?
- What is the comparable global total of CO₂ permanently stored, excluding or separately accounting for EOR and utilization?
- How do application-specific CCS costs and energy penalties compare with electrification, process substitution, renewable generation, hydrogen, and material efficiency?
- How much of the announced 2030 CCS pipeline will reach operation and maintain high capture performance?
- What fraction of high-performing projects such as Sleipner and Quest is representative of future cement, steel, hydrogen, and power applications?
- What geological storage capacity, transport infrastructure, monitoring, and long-term liability arrangements are realistically available at multi-billion-tonne annual scale?

**Analysis Duration:** 20.00s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources materially improve the assessment of power-sector demonstration, especially Petra Nova’s partial capture configuration, energy requirements, cost, downtime, and EOR dependence. However, a key evidence gap remains: independently verified project-level performance data that reconcile claimed capture rates with whole-facility emissions, uptime, energy use, and net lifecycle emissions. Resolving this would materially improve the answer’s evaluation of demonstrated effectiveness and costs.

**Next Search**

> independent verification Petra Nova CCS capture rate uptime energy penalty net emissions GAO DOE EPA performance data

---

# Iteration 6

## 1. Search

**Query**

> independent verification Petra Nova CCS capture rate uptime energy penalty net emissions GAO DOE EPA performance data

**Why this query**

The new sources materially improve the assessment of power-sector demonstration, especially Petra Nova’s partial capture configuration, energy requirements, cost, downtime, and EOR dependence. However, a key evidence gap remains: independently verified project-level performance data that reconcile claimed capture rates with whole-facility emissions, uptime, energy use, and net lifecycle emissions. Resolving this would materially improve the answer’s evaluation of demonstrated effectiveness and costs.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S22 — Technical Comments on the Carbon Capture Utilization ...**
  URL: https://downloads.regulations.gov/EPA-HQ-OAR-2023-0072-0770/attachment_12.pdf
- **S23 — [PDF] GAO-22-105111, Carbon Capture and Storage**
  URL: https://www.gao.gov/assets/gao-22-105111.pdf
- **S24 — petra nova**
  URL: https://www.osti.gov/servlets/purl/1608572

**Search Duration:** 3.76s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Petra Nova provides direct evidence that commercial-scale post-combustion capture, CO₂ transport, and injection for EOR can be built and operated, but it demonstrates a limited configuration rather than full-plant capture or general climate effectiveness.

**Confidence:** High

**Why this confidence level**

S24 is a detailed government-funded project report and S19 independently clarifies the limited slipstream scope. However, the evidence concerns one EOR-linked project and does not establish broad sectoral or global effectiveness.

**Evidence**

- The DOE final technical report states that Petra Nova treated a 240-MW-equivalent flue-gas slipstream, was designed to capture at least 90% of the CO₂ in that treated stream, transported the CO₂ through an 81-mile pipeline, and injected it at the West Ranch oilfield for EOR. [S24]
- The project captured 3,542,537 metric tonnes of CO₂ during its three-year demonstration period and produced more than 4.2 million barrels of oil through EOR, according to the project’s final report. [S24]
- The EIA previously reported that the system treated only part of the coal unit’s emissions and captured approximately 33% of total Unit 8 emissions under its stated configuration. [S19]

#### Finding 2

**Claim**

Petra Nova’s reported capture total is substantial for an individual demonstration but remains small relative to the scale required for global emissions reduction.

**Confidence:** High

**Why this confidence level**

The project report supplies a concrete operating result, while the IEA provides a global comparison. The annualized Petra Nova figure is calculated from the reported three-year total and should be treated as approximate.

**Evidence**

- Petra Nova reports approximately 3.54 million tonnes captured over three years, equivalent to roughly 1.18 million tonnes per year during the demonstration period. [S24]
- The IEA estimates more than 50 MtCO₂ per year of operating capture-and-storage capacity globally in early 2025 and approximately 430 MtCO₂ per year by 2030 from the existing project pipeline, while judging current trends insufficient for net zero. [S9]
- The DOE report describes Petra Nova as the largest commercial-scale post-combustion capture deployment at a coal plant at the time, illustrating the limited number of comparable demonstrations. [S24]

#### Finding 3

**Claim**

Petra Nova required major capital investment and additional energy infrastructure, illustrating the cost and energy penalties that complicate power-sector CCS.

**Confidence:** High

**Why this confidence level**

The cost and energy-supply arrangements are directly described by the project report and corroborated by EIA. These figures are project-specific and do not establish a universal CCS cost.

**Evidence**

- The project report states that the original investment was approximately $1 billion; about 60% covered the capture and cogeneration facilities and related costs, with the remainder involving operating and administrative costs, the CO₂ pipeline, and West Ranch improvements. [S24]
- The project used a standalone cogeneration facility to supply process steam and power, rather than relying entirely on the host coal unit, according to the project’s stated objectives and design description. [S24]
- The EIA reports approximately $1 billion in retrofit cost and the need for a dedicated natural-gas unit to supply capture energy. [S19]

#### Finding 4

**Claim**

The DOE project report supports technical feasibility but is not sufficient to establish net climate benefit, economic competitiveness, or permanent storage independent of EOR.

**Confidence:** High

**Why this confidence level**

The absence of a full lifecycle result in the retrieved report is directly observable, and the accounting limitation is supported by the prior lifecycle review and critical assessment.

**Evidence**

- The report’s principal outcomes emphasize construction, operation, captured and transported CO₂, monitoring and verification activities, and EOR production; it does not provide a complete net-lifecycle accounting that includes capture energy, oil production, refining, and combustion of the recovered oil. [S24]
- Prior evidence shows that EOR climate conclusions vary with operational choices and accounting boundaries, including whether downstream fuel emissions are counted. [S14]
- Prior sources identify Petra Nova’s downtime, financial losses, and disputed effective capture rate, particularly after accounting for energy supplied by the gas-fired cogeneration system. [S19] [S21]

#### Finding 5

**Claim**

The new material reinforces the distinction between a project’s design capture rate and its achieved net or whole-facility emissions reduction.

**Confidence:** High

**Why this confidence level**

The scope distinction is directly supported by S24 and S19. The lower net-rate estimate is contested, so it is presented as an interpretation rather than settled fact.

**Evidence**

- Petra Nova’s design target was at least 90% capture from the treated 240-MW-equivalent slipstream, not 90% of the entire host unit’s emissions. [S24]
- EIA reports that the system captured about 33% of total Unit 8 emissions because only approximately 37% of the unit’s emissions passed through the capture system. [S19]
- IEEFA’s alternative estimate places effective capture at approximately 55–58% after including emissions from the gas-fired energy supply, but the underlying owner data were not publicly available and the precise rate remains disputed. [S21]

#### Finding 6

**Claim**

The newly retrieved industry comments raise substantial concerns about using existing North American power-CCUS experience as a reliable basis for projected costs, schedules, and rapid deployment, but their conclusions require caution because the document was prepared for utility trade associations.

**Confidence:** Medium

**Why this confidence level**

S22 is a relevant technical submission and identifies concrete deployment issues, but the retrieved content is largely structural rather than quantitative, and its commissioned perspective may favor a critical view of regulatory projections.

**Evidence**

- The comments’ table of contents explicitly challenges EPA’s cost basis, levelized $/tonne calculations, projected schedules, and the adequacy of available CCUS experience for determining whether the technology is adequately demonstrated. [S22]
- The document identifies Boundary Dam and Petra Nova as central North American utility-scale cases and includes analysis of pipeline permitting and real-world project schedules. [S22]

### Conflicts Found

- S24 presents Petra Nova as successfully built and operated and reports 3.54 million tonnes captured during the demonstration, whereas S19 and S21 emphasize that the system treated only a fraction of total plant emissions, later experienced downtime and closure, and may have delivered a much lower net capture rate after accounting for energy supply. These claims are compatible if construction and operation of the capture equipment are distinguished from sustained whole-plant and lifecycle performance. [S24] [S19] [S21]
- S24 reports that approximately $1 billion was invested and describes the project as demonstrating commercial-scale operation, while S21 interprets the project’s impairments, sale, and later shutdown as evidence of financial failure. The disagreement concerns the meaning of project success: technical demonstration versus durable commercial performance. [S24] [S21]
- S24 reports CO₂ injected for EOR and monitoring, while S14 and S7 caution that EOR storage cannot automatically be equated with net climate benefit because additional oil production and downstream emissions may offset or exceed storage benefits. [S24] [S14] [S7]
- S22 questions the adequacy of experience and cost assumptions used in regulatory projections, while S24 presents Petra Nova’s completed project as evidence of commercial-scale feasibility. A completed demonstration can provide engineering experience without validating projected costs or schedules for widespread deployment. [S22] [S24]

### Important Gaps

- What independently verified capture rate, uptime, energy consumption, and net lifecycle emissions did Petra Nova achieve over its operating period?
- How much of Petra Nova’s injected CO₂ remains permanently stored after accounting for EOR-associated production and downstream oil emissions?
- What are the comparable independently verified results for Boundary Dam and the other commercial-scale power CCS facilities?
- How much of the global operating CCS total represents permanent saline-aquifer storage rather than EOR or other utilization?
- What application-specific costs and energy penalties apply outside the Petra Nova configuration, especially for cement, steel, hydrogen, and non-EOR geological storage?
- How reliable are announced 2030 CCS capacity and regulatory deployment projections once permitting, financing, construction schedules, and sustained operation are considered?

**Analysis Duration:** 18.22s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The accumulated evidence answers the broad question provisionally: CCS is technically feasible and could contribute significantly in selected hard-to-abate sectors, but current deployment is tiny, power-sector performance is heterogeneous, and EOR-linked demonstrations do not establish broad net climate effectiveness. A further search would materially improve the evaluation by obtaining independent, comparable operating data on capture rates, uptime, energy use, lifecycle emissions, and permanent storage across major projects.

**Next Search**

> independent verified CCS project performance capture rate uptime energy penalty lifecycle emissions permanent storage Boundary Dam Quest Gorgon Sleipner Petra Nova

---

# Iteration 7

## 1. Search

**Query**

> independent verified CCS project performance capture rate uptime energy penalty lifecycle emissions permanent storage Boundary Dam Quest Gorgon Sleipner Petra Nova

**Why this query**

The accumulated evidence answers the broad question provisionally: CCS is technically feasible and could contribute significantly in selected hard-to-abate sectors, but current deployment is tiny, power-sector performance is heterogeneous, and EOR-linked demonstrations do not establish broad net climate effectiveness. A further search would materially improve the evaluation by obtaining independent, comparable operating data on capture rates, uptime, energy use, lifecycle emissions, and permanent storage across major projects.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S25 — Boundary Dam or Petra Nova-Which is a better model for CCS energy ...**
  URL: https://www.researchgate.net/publication/330321625_Boundary_Dam_or_Petra_Nova-Which_is_a_better_model_for_CCS_energy_supply
- **S26 — 92.4% Capture Rate at Petra Nova — that's a CCS Success**
  URL: https://ccsknowledge.com/insights/92-4-capture-rate-at-petra-nova-thats-a-ccs-success
- **S27 — Carbon Capture and Storage: An Evidence-Based Review ...**
  URL: https://www.researchgate.net/publication/396290251_Carbon_Capture_and_Storage_An_Evidence-Based_Review_of_its_Limitations_and_Missed_Promises

**Search Duration:** 3.18s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Petra Nova’s capture equipment reportedly achieved a high capture efficiency when operating, supporting technical feasibility of post-combustion capture in a large coal-fired power application.

**Confidence:** Medium

**Why this confidence level**

The figures are attributed to a DOE project report, but the retrieved source is an advocacy-oriented account written by a CCS engineering expert and does not independently reproduce the underlying operating dataset.

**Evidence**

- The CCS Knowledge Centre reports a 92.4% capture efficiency, exceeding Petra Nova’s 90% design target, based on the project’s final DOE technical report. It also reports lower-than-anticipated power and steam requirements and CO₂ purity above the project specification. [S26]

#### Finding 2

**Claim**

Petra Nova’s high process capture rate does not establish high whole-plant or net lifecycle emissions reduction.

**Confidence:** High

**Why this confidence level**

The distinction between treated-stream efficiency and whole-facility reduction is directly established by the project configuration and is consistent with the existing evidence; only the exact net rate remains contested.

**Evidence**

- The source itself concerns capture efficiency in the treated stream, while prior evidence shows that Petra Nova treated only about 37% of Unit 8’s emissions and captured approximately 33% of total unit emissions in its stated configuration. [S26] [S19]
- Prior critical analysis estimates a substantially lower effective rate after accounting for emissions from the gas-fired cogeneration system, although the precise rate is disputed. [S21]

#### Finding 3

**Claim**

Petra Nova’s capture facility appears to have improved operational availability over its first three years, but the overall project experienced downtime from multiple subsystems and was ultimately placed in reserve shutdown.

**Confidence:** Medium

**Why this confidence level**

The sources are compatible when capture-process availability is distinguished from whole-project availability, but S26 is not an independent audit and its availability calculation and boundaries are not fully documented in the retrieved excerpt.

**Evidence**

- S26 reports capture-process-related lost time declining from 41 days in 2017 to 29 days in 2019, which it characterizes as approximately 92–93% availability in 2019. It attributes other outages to the cogeneration facility, coal unit, oil field, and weather. [S26]
- Prior evidence reports that Petra Nova was taken offline in May 2020 after technical and operational problems involving the capture plant, coal unit, pipeline, and EOR field. [S21]

#### Finding 4

**Claim**

The Petra Nova evidence illustrates that CCS performance depends on the reliability of associated energy, transport, host-plant, and storage or EOR systems, not only on solvent capture efficiency.

**Confidence:** High

**Why this confidence level**

Multiple sources directly describe the integrated configuration and different causes of interruption, supporting the broader systems-level conclusion.

**Evidence**

- S26 identifies cogeneration, coal-unit, oil-field, weather, heat-exchanger, and other mechanical issues as contributors to downtime, while stating that the capture process itself met or exceeded its performance target when online. [S26]
- Prior sources document the project’s dedicated gas-fired energy supply, pipeline and EOR configuration, later shutdown, and disputed financial performance. [S19] [S21]

#### Finding 5

**Claim**

The new material does not materially change the overall conclusion: CCS is technically demonstrated in selected configurations, but broad climate effectiveness and economical scalability remain unproven.

**Confidence:** High

**Why this confidence level**

The favorable Petra Nova evidence complements rather than overturns the existing distinction between engineering feasibility and demonstrated large-scale, net climate abatement.

**Evidence**

- S26 provides a favorable account of Petra Nova’s capture-process efficiency and improving availability, but it does not provide a complete independently verified account of whole-plant capture, net lifecycle emissions, long-term storage permanence, or sustained commercial economics. [S26]
- The accumulated evidence shows limited global operating capacity, only a handful of commercial-scale power projects, major capital and energy requirements, project-specific underperformance, and uncertainty over EOR’s net climate benefit. [S9] [S11] [S14] [S19] [S20] [S21] [S24]

### Conflicts Found

- S26 characterizes Petra Nova as an operational success, citing 92.4% capture efficiency and improving capture-facility availability, whereas S21 emphasizes shutdown, financial losses, system-wide downtime, and a lower possible net capture rate. The disagreement is primarily about the definition of success: capture-process performance while online versus sustained whole-project, whole-plant, and lifecycle climate performance. [S26] [S21]
- S26 attributes most downtime to equipment and non-capture subsystems and reports improving availability, while S21 treats the project’s overall downtime and eventual mothballing as evidence of poor commercial performance. Both accounts can be true because they use different system boundaries and performance criteria. [S26] [S21]
- S26 reports lower-than-anticipated power and steam requirements, while prior evidence characterizes Petra Nova as requiring substantial additional energy infrastructure and potentially producing significant emissions from its gas-fired cogeneration supply. The sources do not provide a common energy-penalty metric, so they cannot establish the project’s net energy performance. [S26] [S19] [S21]

### Important Gaps

- What are the independently verified whole-plant capture rate, uptime, energy penalty, and net lifecycle emissions for Petra Nova?
- How should Petra Nova’s EOR-related oil production and downstream emissions be counted against its injected CO₂?
- Are the favorable capture efficiency and availability figures in S26 representative of other large CCS projects, or mainly of Petra Nova’s specific configuration and operating period?
- What application-specific costs and energy penalties apply to CCS outside this EOR-linked power demonstration?
- How much of announced global CCS capacity will achieve sustained operation and verified permanent storage rather than nominal capture or utilization?

**Analysis Duration:** 16.94s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The accumulated evidence is sufficient for a responsible answer: CCS has demonstrated technical feasibility and can plausibly contribute in targeted hard-to-abate applications, but current scale, heterogeneous project performance, costs, energy requirements, permanence accounting, and infrastructure constraints prevent claiming broad or dominant global effectiveness. The new source strengthens the evidence for process-level feasibility at Petra Nova but does not resolve the central whole-system and lifecycle gaps. Further research could refine numerical estimates but is not necessary to answer the original question with appropriate qualifications.

**Stop Reason:** sufficient_evidence

---

# Final Research Decision

**Research Stopped Because**

The analyzer determined that the important parts of the question could be answered responsibly.

**Stop Reason:** sufficient_evidence

**Searches Performed:** 7

**Unique Sources:** 27

**Remaining Uncertainty**

- No single independently verified dataset in the accumulated material reconciles capture rate, uptime, energy use, whole-facility emissions, lifecycle emissions, and permanent storage across major CCS projects.
- The exact global quantity of CO₂ permanently stored, separated from nominal capture capacity, utilization, and EOR-associated injection, remains unresolved.
- Application-specific costs and energy penalties for cement, steel, hydrogen, chemicals, power, direct air capture, and saline-aquifer storage are not presented on a common methodological basis.
- The share of announced 2030 capacity that will reach final investment decision, construction completion, sustained operation, and high capture performance is uncertain.
- The retrieved evidence does not quantify globally available geological storage, transport constraints, leakage risk, monitoring effectiveness, or long-term liability arrangements at multi-billion-tonne annual scale.
- The evidence does not establish how representative high-performing projects are of future deployments in sectors beyond natural-gas processing and EOR.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 7 | 27.58s |
| OpenAI Analysis | 7 | 122.97s |
| Report Generation | 1 | 34.65s |
| Total Run | — | 185.21s |
