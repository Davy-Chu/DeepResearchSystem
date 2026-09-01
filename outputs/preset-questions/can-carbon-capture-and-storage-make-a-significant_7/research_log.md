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

**Unique Sources:** 31

**OpenAI Calls:** 8

**Tavily Calls:** 7

**Started:** 2026-09-01T02:41:45-04:00

**Ended:** 2026-09-01T02:44:35-04:00

**Total Runtime:** 170.21s

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
- **S2 — CCUS in the transition to net-zero emissions**
  URL: https://www.iea.org/reports/ccus-in-clean-energy-transitions/ccus-in-the-transition-to-net-zero-emissions
- **S3 — Anticipating a potential deficit in global carbon capture demand in 2030 despite benchmarking strategies**
  URL: https://www.nature.com/articles/s44432-025-00002-0
- **S4 — What is carbon dioxide removal and capture in the context of climate change? | Brookings**
  URL: https://www.brookings.edu/articles/what-is-carbon-dioxide-removal-and-capture-in-the-context-of-climate-change
- **S5 — A Vision for Carbon Capture, Utilisation, and Storage in the EU**
  URL: https://www.catf.us/resource/a-vision-carbon-capture-utilisation-and-storage-eu

**Search Duration:** 2.57s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

CCS currently makes only a very small demonstrated contribution to global emissions reduction, despite substantial investment.

**Confidence:** Medium

**Why this confidence level**

The claim is directly stated in a peer-reviewed review abstract, but the underlying global inventory and accounting methods are not provided in the retrieved text.

**Evidence**

- A 2026 evidence-based review states that more than $40 billion has been invested globally, while CCS captures and stores less than 0.1% of annual global CO₂ emissions. [S1]

#### Finding 2

**Claim**

Observed CCS performance has included recurring problems with cost, capture rates, storage uncertainty, and project delivery.

**Confidence:** Medium

**Why this confidence level**

The source explicitly reports these recurring problems, but the retrieved abstract does not provide project-by-project data needed to quantify their frequency or severity.

**Evidence**

- The review identifies cost overruns, suboptimal capture rates, geological uncertainties, and disputes over liability, drawing on cases including Petra Nova, Gorgon, Sleipner, and In Salah. [S1]

#### Finding 3

**Claim**

CCS is energy-intensive and its cost varies widely by application and CO₂ source.

**Confidence:** Medium

**Why this confidence level**

The figures are directly reported, but the abstract does not specify whether costs are capture-only or full-chain costs, nor how they vary across sectors.

**Evidence**

- The review gives an energy-demand range of 2.5–8 GJ per tonne of CO₂ and a cost range of $50–600 per tonne of CO₂. [S1]

#### Finding 4

**Claim**

Major proponents argue that CCUS can be important or essential for net zero, particularly for hard-to-abate industrial emissions, existing assets, hydrogen production, and carbon dioxide removal.

**Confidence:** Medium

**Why this confidence level**

The roles and sectoral arguments are clearly stated by the IEA and the EU CCUS working group, but these are partly scenario- and policy-dependent claims rather than direct evidence of achieved emissions reductions.

**Evidence**

- The IEA identifies four roles: addressing emissions from existing energy assets, reducing emissions in hard-to-abate sectors, enabling clean hydrogen production, and removing atmospheric CO₂ to balance residual emissions. [S2]
- A European CCUS working group argues that cement, steel, chemicals, waste incineration, fossil or biomass power, low-carbon hydrogen, and atmospheric or biogenic removals may all require CCUS in some circumstances. [S5]

#### Finding 5

**Claim**

Large-scale deployment would require a substantial expansion from current levels and faces economic and geographic coordination barriers.

**Confidence:** Medium

**Why this confidence level**

The sources provide explicit deployment estimates and barriers, but the retrieved material does not establish whether the estimates use comparable definitions of capture, utilization, storage, or removal.

**Evidence**

- The EU working group estimates that the EU may need to capture and use or store 300–640 MtCO₂ annually by 2050, including at least 150 Mt annually of atmospheric or biogenic CO₂ removals; it describes cross-border coordination and infrastructure development as urgent requirements. [S5]
- A 2026 Nature article reports that CCUS development is policy-driven, cost barriers impede economies of scale, global development inequality remains high, and an optimized strategy could double capture scale by 2030 while still leaving a one-third shortfall against climate targets. [S3]

#### Finding 6

**Claim**

CCS should not be treated as a universal substitute for emissions avoidance or renewable deployment; even supportive analyses generally frame its strongest case as targeted deployment.

**Confidence:** High

**Why this confidence level**

The sources converge on a conditional rather than universal role: CCS may be valuable in difficult applications, while other options address much of the broader energy system.

**Evidence**

- The critical review does not reject CCS categorically but recommends strategic use in hard-to-abate sectors such as cement and legacy-infrastructure retrofits, while warning that overreliance could delay alternatives. [S1]
- The EU working group says renewables are expected to decarbonize most of the power sector, with CCUS potentially assisting in specific situations such as existing fossil capacity, dispatchable generation, and industrial process emissions. [S5]

#### Finding 7

**Claim**

Carbon capture and storage is distinct from carbon dioxide removal: conventional CCS prevents some emissions from entering the atmosphere, whereas removal extracts atmospheric CO₂ and stores it durably.

**Confidence:** High

**Why this confidence level**

The retrieved source gives explicit definitions relevant to evaluating whether CCS reduces current emissions versus removes historical atmospheric CO₂.

**Evidence**

- Brookings defines carbon dioxide removal as intentionally removing CO₂ from the atmosphere and durably storing it, and distinguishes this from carbon capture performed before emissions enter the atmosphere. [S4]

### Conflicts Found

- The sources disagree in emphasis about CCS's strategic importance. The critical review portrays current CCS as a high-cost, low-contribution technology that risks delaying more effective solutions, whereas the IEA and EU CCUS working group present CCUS as important or essential for net zero, especially in hard-to-abate sectors and removals. [S1] [S2] [S5]
- The sources conditionally disagree about whether large-scale deployment is achievable by 2030–2050. The EU working group and IEA describe large future roles in modeled pathways, while the Nature study reports persistent cost, inequality, and policy barriers and a projected shortfall even under an optimized strategy. [S2] [S3] [S5]
- The sources differ in the breadth of proposed applications: the EU working group includes fossil power, low-carbon hydrogen, and broad CCUS infrastructure, while the critical review favors narrower deployment in hard-to-abate sectors and warns against generalized reliance. [S1] [S5]

### Important Gaps

- What is the independently verified current global capture and permanent-storage capacity, and how does it compare with gross capture claims?
- What are the capture rates, availability, lifecycle emissions, and net climate benefits of major operating projects on a consistent basis?
- How do full-system costs of CCS compare with electrification, renewable energy, alternative fuels, efficiency, and other mitigation options in cement, steel, power, hydrogen, and direct-air-capture applications?
- How much additional electricity or fuel would global CCS deployment require, and what would the associated upstream emissions and opportunity costs be?
- What is the technically and politically feasible global geological-storage capacity, including transport infrastructure, monitoring, leakage risk, and long-term liability?
- Which parts of the projected future role concern fossil-source abatement, and which concern genuine carbon dioxide removal? These should not be combined when assessing atmospheric impact.

**Analysis Duration:** 19.79s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The current sources establish the central balance—very limited demonstrated deployment versus potentially important modeled roles—but they do not adequately quantify verified operating capacity, project-level effectiveness, comparative costs, or system-wide energy requirements. Those gaps are essential to answering whether CCS can make a significant global contribution rather than merely whether models assign it a role.

**Next Search**

> IEA Global CCS Institute 2024 2025 operating projects captured stored CO2 capacity capture rates costs energy penalty

---

# Iteration 2

## 1. Search

**Query**

> IEA Global CCS Institute 2024 2025 operating projects captured stored CO2 capacity capture rates costs energy penalty

**Why this query**

The current sources establish the central balance—very limited demonstrated deployment versus potentially important modeled roles—but they do not adequately quantify verified operating capacity, project-level effectiveness, comparative costs, or system-wide energy requirements. Those gaps are essential to answering whether CCS can make a significant global contribution rather than merely whether models assign it a role.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S6 — Commercial Carbon Capture Plants: International Operating CCS Projects | CCS Knowledge Centre**
  URL: https://ccsknowledge.com/carbon-management-101/international-ccs-projects
- **S7 — Carbon Capture and Storage Capacity Worldwide**
  URL: https://incorrys.com/environmental-data/carbon-capture-and-storage/carbon-capture-and-storage-capacity-worldwide
- **S8 — A new era for CCUS – CCUS in Clean Energy Transitions – Analysis - IEA**
  URL: https://www.iea.org/reports/ccus-in-clean-energy-transitions/a-new-era-for-ccus
- **S9 — Global Status of CCS | Global CCS Institute**
  URL: https://www.globalccsinstitute.com/global-status-of-ccs
- **S10 — Global Status Report | Global CCS Institute**
  URL: https://www.globalccsinstitute.com/resources/global-status-report

**Search Duration:** 3.03s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Current operating CCS capacity is approximately 51–56 MtCO₂ per year, which is a very small fraction of global emissions—roughly 0.1–0.16% depending on the emissions denominator and capacity dataset.

**Confidence:** Medium

**Why this confidence level**

Multiple sources agree that present deployment is small, but the reported totals differ and appear to use different inclusion criteria and definitions.

**Evidence**

- As of the end of 2024, operational CCS capacity was reported as 51 MtCO₂/yr, compared with 37,600 MtCO₂/yr of energy and industrial-process emissions, or 0.16%. [S7]
- A separate 2025 compilation of commercial facilities above 100,000 tonnes per year reports 55.73 Mtpa from pre-combustion facilities, 7.97 Mtpa from post-combustion facilities, and 0.20 Mtpa from oxy-fuel facilities—approximately 64 Mtpa in total across the listed categories, although its regional totals sum to 63.9 Mtpa. [S6]
- The IEA characterizes CCUS's historical deployment as slow and its impact on global CO₂ emissions as limited. [S8]

#### Finding 2

**Claim**

The sector is expanding, but announced and constructed capacity should not be equated with demonstrated emissions reductions.

**Confidence:** High

**Why this confidence level**

The sources consistently document strong pipeline growth and simultaneously distinguish it from the limited historical contribution.

**Evidence**

- The Global CCS Institute reports 77 operating projects and 47 under construction in 2025, with planned capacity growing at more than 30% annually since 2017. [S9]
- A 2025 capacity summary reports more than 50 MtCO₂/yr under construction for 2025–2027 and describes a potential doubling of operational capacity if those projects are completed. [S7]
- The IEA reports that more than 30 integrated facilities had been announced since 2017, but also states that CCUS deployment had historically been slow and had not lived up to expectations. [S8]

#### Finding 3

**Claim**

The strongest case for CCS is targeted use in applications with few alternatives, rather than universal deployment across the energy system.

**Confidence:** High

**Why this confidence level**

Supportive and critical sources converge on a conditional role, even though they differ on how broad that role should be.

**Evidence**

- The IEA identifies retrofits of existing power and industrial assets, cement, iron and steel, chemicals, low-carbon hydrogen, synthetic fuels, and atmospheric removal as strategic applications. [S8]
- Prior evidence from the critical review recommends strategic deployment in hard-to-abate sectors and legacy-infrastructure retrofits while warning against overreliance. [S1]
- Prior evidence indicates renewables are expected to decarbonize most power-sector emissions, with CCUS potentially serving more specific industrial and dispatchable-generation roles. [S5]

#### Finding 4

**Claim**

CCS can make a significant contribution in future climate pathways, but only if deployment expands by orders of magnitude and the projects deliver verified permanent storage or removal.

**Confidence:** Medium

**Why this confidence level**

The evidence supports substantial modeled potential, but the retrieved material does not establish that the required scale, permanence, infrastructure, and economics are currently achievable.

**Evidence**

- The IEA describes CCUS as potentially important for avoiding emissions from existing assets, addressing hard-to-abate sectors, producing hydrogen, and balancing residual emissions through removals. [S8]
- The EU working group estimates a possible requirement for 300–640 MtCO₂ per year of EU CCUS by 2050, including at least 150 Mt per year of atmospheric or biogenic removals. [S5]
- The Nature study previously retrieved reports that an optimized strategy could double capture scale by 2030 but still leave a one-third shortfall against climate targets. [S3]

#### Finding 5

**Claim**

Reported operating capacity is not necessarily equivalent to net atmospheric removal or permanent geological storage.

**Confidence:** High

**Why this confidence level**

The distinction between capture, utilization, storage, and removal is explicit, while the evidence gap about net permanent storage remains material.

**Evidence**

- The operating-project compilation notes that capture facilities and storage sites may be geographically separate and includes the Weyburn enhanced-oil-recovery project as an example of cross-border transport and storage. [S6]
- Prior evidence distinguishes conventional point-source CCS from carbon dioxide removal: CCS prevents some emissions from entering the atmosphere, whereas removal extracts atmospheric CO₂ and stores it durably. [S4]
- The capacity sources report capture capacity, but the retrieved text does not provide a consistent independent accounting of injected, retained, monitored, and permanently stored CO₂. [S6] [S7]

#### Finding 6

**Claim**

Large-scale CCS faces substantial cost, energy, delivery, and coordination barriers.

**Confidence:** Medium

**Why this confidence level**

The barriers and broad energy/cost ranges are directly reported, but the retrieved evidence lacks a consistent full-system comparison with alternatives and does not quantify global energy demand at target deployment levels.

**Evidence**

- The prior review reports energy requirements of 2.5–8 GJ per tonne of CO₂ and costs of $50–600 per tonne, while noting cost overruns and suboptimal capture rates in projects including Petra Nova and Gorgon. [S1]
- The Nature study reports cost barriers to economies of scale, policy dependence, and geographic inequality in CCUS development. [S3]
- The EU working group identifies cross-border coordination and infrastructure development as urgent requirements for projected deployment. [S5]

### Conflicts Found

- Reported current capacity differs: S7 gives 51 MtCO₂/yr operational capacity at the end of 2024, while S6 lists roughly 64 Mtpa across commercial capture categories as of July 2025. The difference may reflect timing, project inclusion thresholds, and capture-versus-operational-capacity definitions, but the retrieved material does not reconcile them. [S6] [S7]
- The Global CCS Institute presents rapid project and capacity growth as evidence that CCS is scaling, whereas the IEA and prior critical review emphasize that historical deployment has been slow and has produced only a very small global emissions contribution. These are not strictly contradictory: they concern pipeline growth versus realized impact. [S1] [S8] [S9]
- Supportive pathway analyses assign CCUS an important or essential future role, especially for hard-to-abate sectors and removals, while critical evidence warns that high costs, underperformance, and overreliance could delay alternatives. The disagreement is primarily about strategic breadth and feasibility, not whether CCS has any possible niche role. [S1] [S2] [S3] [S5] [S8]

### Important Gaps

- What share of the reported 51–64 MtCO₂/yr is actually injected into geological storage rather than used for enhanced oil recovery or otherwise counted as captured?
- What are the independently verified capture rates, operating availability, lifecycle emissions, leakage rates, and net climate benefits of major projects?
- Are the reported cost figures full-chain costs, and how do they compare with electrification, efficiency, renewable energy, alternative fuels, and process substitution in each sector?
- How much additional low-carbon electricity or fuel would deployment at hundreds of millions or billions of tonnes per year require?
- What storage capacity is technically, legally, and politically available, and can transport, monitoring, and long-term liability systems expand at the required rate?
- How much of modeled future CCUS deployment represents fossil-source emissions avoidance versus genuine atmospheric carbon dioxide removal?

**Analysis Duration:** 19.67s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources improve the current-capacity and pipeline picture, but they do not resolve the most important qualification for the original question: whether gross capture claims translate into verified permanent storage and meaningful net global emissions reductions. They also do not adequately quantify full-system costs or energy requirements at scale.

**Next Search**

> independent assessment operating CCS projects verified permanent storage capture rates lifecycle emissions energy penalty full-chain cost

---

# Iteration 3

## 1. Search

**Query**

> independent assessment operating CCS projects verified permanent storage capture rates lifecycle emissions energy penalty full-chain cost

**Why this query**

The new sources improve the current-capacity and pipeline picture, but they do not resolve the most important qualification for the original question: whether gross capture claims translate into verified permanent storage and meaningful net global emissions reductions. They also do not adequately quantify full-system costs or energy requirements at scale.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S11 — Carbon capture and storage: What can we learn from the project track record? – Clean Air Task Force**
  URL: https://www.catf.us/resource/carbon-capture-storage-what-can-learn-from-project-track-record
- **S12 — Carbon capture and storage enters a new era of progress | articles | ING THINK**
  URL: https://think.ing.com/articles/energy-ccs-entering-a-new-era-of-progress
- **S13 — Carbon Capture and Storage: An Unproven Technology | IEEFA**
  URL: https://ieefa.org/ccs
- **S14 — Publications Archive | Global CCS Institute**
  URL: https://www.globalccsinstitute.com/publications

**Search Duration:** 2.82s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The project track record shows that technically strong CCS performance is achievable, but it is not yet representative of the sector as a whole.

**Confidence:** Medium

**Why this confidence level**

The sources provide direct but contrasting project-track-record assessments. S11 documents successful examples, while S13 reports weaker aggregate performance; the evidence does not establish a standardized, independently audited global average.

**Evidence**

- A review of 13 large-scale projects identifies Sleipner, the Alberta Carbon Trunk Line, and Quest as projects that consistently achieved high technical performance, while also reporting recurring operational challenges across the wider sample. [S11]
- The same review cautions that many large-scale projects were developed for commercial purposes, technology demonstration, or enhanced oil recovery rather than to maximize climate benefit, and that relatively few were required to do so. [S11]
- IEEFA reports that, in its review of 16 projects, no project consistently captured more than 80% of CO₂, despite industry claims that 95% capture is achievable. [S13]

#### Finding 2

**Claim**

Much reported CCS experience does not directly demonstrate net climate mitigation because some projects capture CO₂ for commercial use, especially enhanced oil recovery, rather than maximizing permanent storage.

**Confidence:** High

**Why this confidence level**

The limitation is explicitly described by CATF and is consistent with the prior evidence gap concerning capture versus permanent storage.

**Evidence**

- CATF states that many operating projects were motivated by commercial CO₂ sales, particularly enhanced oil recovery, and were not required to minimize atmospheric emissions or maximize stored CO₂. [S11]
- The existing research state distinguishes gross capture capacity from injected, retained, monitored, and permanently stored CO₂, and identifies enhanced-oil-recovery accounting as an unresolved issue. [S6] [S7] [S11]

#### Finding 3

**Claim**

CCS must expand by many times its present scale to make a significant global contribution, and the required expansion is not yet demonstrated.

**Confidence:** High

**Why this confidence level**

The large gap between present capacity and multi-billion-tonne pathway requirements is consistent across the sources, although future project completion and actual storage performance remain uncertain.

**Evidence**

- CATF says climate pathways require storage of several billion tonnes of CO₂ annually by 2050, a scale many times greater than current operations. [S11]
- The prior research state reports current operating capacity of approximately 51–64 MtCO₂ per year and identifies this as roughly 0.1–0.16% of global emissions, depending on dataset definitions. [S6] [S7]
- CATF characterizes the current wave of planned deployment as potentially capable of major growth but emphasizes the need for transparent performance data and policies that maximize climate impact. [S11]

#### Finding 4

**Claim**

Current CCS costs are high and strongly dependent on the emissions source and full value-chain design, making deployment heavily reliant on policy support.

**Confidence:** Medium

**Why this confidence level**

The sources give useful current cost ranges and cost drivers, but they do not provide a consistent apples-to-apples comparison with alternative mitigation options or a single standardized cost basis.

**Evidence**

- ING reports total capture, transport, and storage costs of approximately €50–300 per tonne, with many projects in the $100–250 per tonne range; ethanol and ammonia are at the lower end, while cement and steel are at the higher end. [S12]
- ING states that high costs are a greater obstacle to widespread adoption than technical challenges and that subsidies, carbon pricing, or tax incentives are generally needed for current business models. [S12]
- CATF explains that capture is generally more expensive for dilute or technically difficult industrial sources, while saline-aquifer storage and long-distance transport add costs compared with commercially motivated CO₂ use. [S11]

#### Finding 5

**Claim**

There is a plausible pathway for CCS to improve through learning, standardization, clustering, and better-integrated transport and storage systems, but cost reductions are uncertain and insufficiently demonstrated.

**Confidence:** Medium

**Why this confidence level**

The evidence supports mechanisms for improvement and cites projected reductions, but these are forecasts or policy/industry assessments rather than demonstrated system-wide outcomes.

**Evidence**

- ING reports that cluster-based infrastructure and alignment among emitters, transport operators, and storage providers are needed to address the sector’s coordination problem; it cites DNV estimates of roughly 14% lower average capital costs by 2030 and up to 40% lower costs by 2050. [S12]
- CATF argues that operational experience and innovation have improved reliability and performance in some projects, while also calling for transparent reporting because continuous climate performance has often been subordinate to demonstration or commercial goals. [S11]

#### Finding 6

**Claim**

The strongest argument for large-scale CCS is targeted deployment in hard-to-abate sectors and for some carbon-dioxide-removal pathways; the strongest argument against indiscriminate deployment is its high cost, energy use, limited current impact, and risk of delaying alternatives.

**Confidence:** High

**Why this confidence level**

Supportive and critical sources converge on the central conditional conclusion: CCS may have an important niche, but its present performance and economics do not support treating it as a universal decarbonization substitute.

**Evidence**

- The prior IEA and EU evidence identifies cement, steel, chemicals, existing assets, hydrogen, and removals as potential applications where alternatives may be limited. [S2] [S5] [S8]
- CATF identifies cement, steel, and petrochemicals as sectors with few decarbonization alternatives and says climate pathways require billions of tonnes of geological storage by mid-century. [S11]
- IEEFA argues that CCS is expensive, has not consistently achieved claimed capture rates in its project review, and could distract from renewable energy, efficiency, and methane reduction. [S13]
- The prior critical review likewise recommends strategic use while warning that overreliance could delay alternatives. [S1]

### Conflicts Found

- CATF presents several projects as consistently achieving high technical performance, whereas IEEFA reports that no project in its 16-project review consistently exceeded 80% capture. This may reflect different project samples, definitions of capture rate, operating periods, or evaluation criteria; the retrieved material does not reconcile them. [S11] [S13]
- CATF and the IEA/EU evidence view CCS as potentially necessary for hard-to-abate sectors and future climate pathways, while IEEFA argues that its contribution will remain minimal and that it diverts attention from established solutions. The disagreement concerns aggregate feasibility and strategic importance, not whether individual projects can operate. [S1] [S2] [S5] [S11] [S13]
- ING projects substantial future cost reductions from scale and standardization, while the critical and financial evidence emphasizes that current costs are substantially higher than earlier expectations and remain dependent on public support. Projected reductions therefore should not be treated as demonstrated cost competitiveness. [S1] [S12] [S13]

### Important Gaps

- What standardized capture-rate, availability, lifecycle-emissions, and net-storage measurements would the apparently conflicting CATF and IEEFA project assessments produce?
- What share of current reported capacity is injected into durable geological storage rather than used for enhanced oil recovery or otherwise counted as captured?
- How much additional low-carbon energy would deployment at billion-tonne scale require, including upstream emissions and opportunity costs?
- How do full-chain CCS costs compare with electrification, efficiency, renewable energy, alternative fuels, or process substitution in each target sector?
- What geological storage capacity is technically, legally, politically, and environmentally available, and can monitoring and long-term liability systems scale accordingly?

**Analysis Duration:** 18.15s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources improve the assessment of project performance and cost drivers, but they do not resolve the most important quantitative gap: consistent, independent evidence on actual capture rates, energy penalties, lifecycle emissions, and net permanent storage at operating projects. This is material to judging demonstrated effectiveness and scalability.

**Next Search**

> IEA IPCC independent CCS project capture rates energy penalty lifecycle emissions permanent storage verified operating projects

---

# Iteration 4

## 1. Search

**Query**

> IEA IPCC independent CCS project capture rates energy penalty lifecycle emissions permanent storage verified operating projects

**Why this query**

The new sources improve the assessment of project performance and cost drivers, but they do not resolve the most important quantitative gap: consistent, independent evidence on actual capture rates, energy penalties, lifecycle emissions, and net permanent storage at operating projects. This is material to judging demonstrated effectiveness and scalability.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S15 — [PDF] Carbon capture and storage: What can we learn from the project ...**
  URL: https://cdn.catf.us/wp-content/uploads/2024/07/16151022/CCS-Project-Track-Record-Report.pdf
- **S16 — Carbon Capture and Storage (CCS) | World Resources Institute**
  URL: https://www.wri.org/initiatives/carbon-capture-and-storage-ccs
- **S17 — [PDF] CCS Defined**
  URL: https://www.stemm-ccs.eu/sites/stemm-ccs/files/documents/Glossary%20of%20Terminology%20October%202018.pdf
- **S18 — Carbon Capture, Utilization, and Storage: Do We Have a Choice?**
  URL: https://jpt.spe.org/twa/carbon-capture-utilization-and-storage-do-we-have-choice
- **S19 — IPCC Report Reaffirms Carbon Capture and Storage as a Critical Technology for Mitigating Climate Change | Global CCS Institute**
  URL: https://www.globalccsinstitute.com/ipcc-report-reaffirms-carbon-capture-and-storage-as-a-critical-technology-for-mitigating-climate-change

**Search Duration:** 4.66s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new evidence reinforces that CCS can technically operate at large scale, but demonstrated climate impact remains much smaller than the scale required in modeled pathways.

**Confidence:** High

**Why this confidence level**

The new and prior sources consistently show a large gap between present deployment and modeled requirements, although capacity definitions and the exact required scale vary.

**Evidence**

- The CATF project-track-record report states that meeting climate commitments would require billions of tonnes of CO₂ captured and geologically stored annually by mid-century, many times current levels, while identifying several projects with consistently high technical performance. [S15]
- WRI reports 40 MtCO₂ captured from 26 operating power and industrial facilities in 2020 and describes a need for at least a 100-fold increase by 2050 under cited IPCC scenarios. [S16]
- Prior evidence estimates current operating capacity at roughly 51–64 MtCO₂ per year, only about 0.1–0.16% of global emissions depending on definitions. [S6] [S7]

#### Finding 2

**Claim**

Some CCS projects have demonstrated high technical performance, but these examples do not establish a representative sector-wide capture rate or net climate benefit.

**Confidence:** Medium

**Why this confidence level**

The evidence establishes successful projects alongside weaker aggregate assessments, but the sources use different samples, operating periods, and definitions and do not provide a standardized independently audited global average.

**Evidence**

- CATF identifies Sleipner, the Alberta Carbon Trunk Line, and Quest as projects that consistently achieved high technical performance. [S15]
- CATF also states that many projects were developed for commercial CO₂ sales, technology demonstration, or geological learning rather than to maximize climate impact, and that relatively few were subject to requirements to do so. [S15]
- IEEFA previously reported that none of 16 reviewed projects consistently captured more than 80%, despite claims that 95% capture is achievable. [S13]

#### Finding 3

**Claim**

Reported capture and injection experience includes substantial activity that is not equivalent to permanent climate-oriented storage.

**Confidence:** High

**Why this confidence level**

The limitation is directly stated in the new report and aligns with multiple prior findings.

**Evidence**

- CATF reports that many of the 41 commercial large-scale projects it identifies as operating were not developed or required to minimize atmospheric emissions or maximize stored CO₂; many sold CO₂ for enhanced oil recovery. [S15]
- The report distinguishes dedicated geological storage from CO₂ use and notes that climate-oriented deployment will increasingly involve saline aquifers, which add costs compared with commercially motivated storage or use. [S15]
- Prior evidence likewise finds that reported capacity does not consistently document CO₂ injected, retained, monitored, and permanently stored, and distinguishes point-source CCS from atmospheric carbon removal. [S4] [S6] [S7] [S11]

#### Finding 4

**Claim**

CCS has a stronger prospective case in hard-to-abate industrial sectors and selected removal pathways than as a universal solution for power or the wider energy system.

**Confidence:** High

**Why this confidence level**

Supportive and critical sources converge on a conditional, sector-specific role even though they differ on the breadth and urgency of deployment.

**Evidence**

- CATF identifies cement, steel, and petrochemicals as industries with few decarbonization alternatives and says policies should maximize the climate impact of new projects. [S15]
- WRI describes CCS as a tool for reducing emissions from energy-intensive industries and says it should be one of multiple tools used for net zero. [S16]
- Prior IEA, EU, and critical-review evidence converges on targeted use in hard-to-abate sectors, legacy assets, hydrogen, and removals while warning against substituting CCS for alternatives. [S1] [S2] [S5] [S8]

#### Finding 5

**Claim**

The main barriers remain high and source-dependent costs, additional energy and infrastructure needs, policy dependence, and coordination across capture, transport, and storage systems.

**Confidence:** Medium

**Why this confidence level**

The sources consistently identify the barriers, but the new material does not quantify energy use or provide an apples-to-apples comparison with competing mitigation options.

**Evidence**

- CATF states that applying capture to diverse industrial sources such as cement, steel, and petrochemicals is often more expensive than capturing high-purity CO₂, while transport to distant storage and saline-aquifer storage add costs. [S15]
- Prior evidence reports broad energy requirements of 2.5–8 GJ per tonne and full-chain or near-full-chain cost estimates ranging from approximately €50–300 or $50–600 per tonne, with significant dependence on the source and system design. [S1] [S11] [S12]
- WRI emphasizes the need for major investment, regulatory standards, infrastructure, and financial incentives to overcome high initial capital costs. [S16]

#### Finding 6

**Claim**

The new sources are predominantly supportive or institutionally promotional and therefore strengthen evidence about proponents' arguments more than independent evaluation of costs, lifecycle emissions, permanence, or scalability.

**Confidence:** High

**Why this confidence level**

The framing and institutional affiliations are explicit in the retrieved content; these sources are useful but do not replace independent full-chain assessment.

**Evidence**

- WRI, the Global CCS Institute, and the Society of Petroleum Engineers source describe CCS as critical, indispensable, or a technology for which more projects should be developed. [S16] [S18] [S19]
- CATF provides more substantive project-case-study evidence and explicitly acknowledges underperformance, commercial motives, and the need for transparent reporting, but it remains an advocacy-oriented source. [S15]

### Conflicts Found

- CATF highlights several projects with consistently high technical performance, while IEEFA reports that no project in its sample consistently exceeded 80% capture. The disagreement remains unresolved because the retrieved sources do not align project samples, capture-rate definitions, availability periods, or measurement methods. [S13] [S15]
- Supportive sources characterize CCS as critical or indispensable for net zero, whereas the prior critical evidence emphasizes its very small current contribution, high cost, and risk of delaying alternatives. The sources agree on possible hard-to-abate applications but disagree on aggregate strategic importance and feasibility. [S1] [S16] [S18] [S19]
- The new sources cite different scales and dates for current deployment: WRI reports 40 MtCO₂ captured in 2020, CATF identifies 41 operating commercial projects, and prior sources report approximately 51–64 MtCO₂ per year in 2024–2025. These figures may use different years and inclusion criteria and are not directly comparable. [S6] [S7] [S15] [S16]

### Important Gaps

- What is the independently verified amount of CO₂ currently injected into and retained in dedicated geological storage, excluding temporary capture, utilization, and enhanced-oil-recovery accounting?
- What standardized capture rates, availability, lifecycle emissions, energy penalties, leakage risks, and net climate benefits do major operating projects achieve?
- How do full-chain CCS costs and energy requirements compare with electrification, efficiency, renewable power, alternative fuels, and process substitution in each target sector?
- What technically, legally, politically, and environmentally usable geological-storage capacity and transport infrastructure can be developed globally?
- What additional low-carbon electricity or fuel would deployment at hundreds of millions to billions of tonnes per year require?
- How much modeled future deployment is conventional point-source emissions avoidance versus genuine atmospheric carbon-dioxide removal?

**Analysis Duration:** 20.50s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources corroborate the conditional conclusion and add useful project-track-record context, but they do not resolve the most important quantitative gaps: independently verified net storage, consistent capture performance, comparative full-chain costs, and energy requirements at scale. Because these gaps materially affect whether CCS can make a significant contribution, another focused search is warranted.

**Next Search**

> independent life-cycle assessment CCS full-chain energy penalty net CO2 reduction capture rate permanent geological storage operating projects

---

# Iteration 5

## 1. Search

**Query**

> independent life-cycle assessment CCS full-chain energy penalty net CO2 reduction capture rate permanent geological storage operating projects

**Why this query**

The new sources corroborate the conditional conclusion and add useful project-track-record context, but they do not resolve the most important quantitative gaps: independently verified net storage, consistent capture performance, comparative full-chain costs, and energy requirements at scale. Because these gaps materially affect whether CCS can make a significant contribution, another focused search is warranted.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S20 — Life cycle assessment finds significant emissions savings potential across the onboard carbon capture value chain - GCMD**
  URL: https://www.gcformd.org/life-cycle-assessment-finds-significant-emissions-savings-potential-across-the-onboard-carbon-capture-value-chain
- **S21 — Frontiers | Prospective techno-economic and life cycle assessment: a review across established and emerging carbon capture, storage and utilization (CCS/CCU) technologies**
  URL: https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2024.1412770/full
- **S22 — The CCS+ US guide**
  URL: http://ccsplus.org/wp-content/uploads/2024/08/082724_CCS-Initiative_USguidance-note_final.pdf
- **S23 — SETTING A FOUNDATION FOR CARBON CAPTURE AND ...**
  URL: https://www.cleanenergyministerial.org/resource/setting-a-foundation-for-carbon-capture-and-storage-in-product-life-cycle-assessment

**Search Duration:** 2.97s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

New evidence reinforces that CCS/CCUS could contribute materially in hard-to-abate industry, but current deployment remains far below modeled requirements.

**Confidence:** High

**Why this confidence level**

The new review and prior capacity estimates consistently show a large gap between present or announced deployment and modeled climate-pathway requirements, although announced capacity is not equivalent to operating or permanently stored capacity.

**Evidence**

- A peer-reviewed review reports approximately 400 MtCO₂/year of announced capacity versus about 1 GtCO₂/year required in the IEA Net Zero scenario by 2030, and says deployment remains below pathways compatible with 1.5°C and 2°C goals. [S21]
- The review identifies cement, steel, and chemicals as especially relevant sectors because alternatives are limited, while emphasizing that emissions avoidance and energy efficiency should come first. [S21]
- Earlier evidence places current operating capacity at roughly 51–64 MtCO₂/year, only about 0.1–0.16% of global emissions depending on definitions. [S6] [S7]

#### Finding 2

**Claim**

A real-world onboard carbon-capture pilot demonstrated measurable but limited net emissions savings, illustrating why full-chain accounting matters.

**Confidence:** Medium

**Why this confidence level**

The LCA was verified by DNV and covers the full value chain, but this is a single maritime pilot and cannot establish performance for stationary industrial CCS or the sector as a whole.

**Evidence**

- Project CAPTURED operated at a 10.7% capture rate and reportedly achieved 7.9% greenhouse-gas savings across its entire capture, liquefaction, transport, handling, and utilization chain—0.84 tonnes avoided per tonne captured and offloaded. [S20]
- The pilot’s performance was reduced by the absence of waste-heat recovery, long-distance trucking, and CO₂ venting during handling; an optimized hypothetical scenario increased savings to 17.8%. [S20]

#### Finding 3

**Claim**

Utilization can sometimes produce greater lifecycle emissions savings than storage, but this is pathway-specific and must not be generalized to all CCU.

**Confidence:** Medium

**Why this confidence level**

The source provides quantified LCA scenarios, but the results depend on specific displaced products, transport arrangements, capture rates, and durability assumptions; they do not show that utilization generally outperforms permanent storage.

**Evidence**

- For the Project CAPTURED scenarios at a comparable 40% capture rate, mineralization was estimated to yield 34% emissions savings versus 21% for offshore geological storage; optimized utilization scenarios reached 68–71% savings. [S20]
- The reported advantage depends on durable mineralization and displacement of carbon-intensive products such as conventional precipitated calcium carbonate or steelmaking materials. [S20]
- The CCS+ guide stresses that reductions, removals, short-term utilization, and durable storage must be separately accounted for. [S22]

#### Finding 4

**Claim**

The evidence base still has major accounting and verification weaknesses, especially around net reductions, permanence, leakage, and comparisons between projects.

**Confidence:** High

**Why this confidence level**

Multiple sources explicitly identify accounting and monitoring gaps, and these gaps directly affect whether gross capture figures translate into credible net climate benefits.

**Evidence**

- The CCS+ guide says US policy instruments lack a harmonized accounting infrastructure for quantifying emission reductions and removals across CCS, CCU, and CDR, and calls for monitoring, reporting, verification, permanence, leakage-risk, and embodied-carbon accounting. [S22]
- The Clean Energy Ministerial paper identifies unresolved methodological issues involving system boundaries, long-term liability, reservoir leakage, biogenic carbon, and chain of custody. [S23]
- Prior evidence likewise finds that reported capture capacity does not consistently establish CO₂ injected, retained, monitored, and permanently stored. [S6] [S7] [S11]

#### Finding 5

**Claim**

Costs, energy use, and scalability remain decisive constraints, with improvement possible but not yet demonstrated at global scale.

**Confidence:** Medium

**Why this confidence level**

The evidence consistently identifies high and application-dependent costs, energy penalties, infrastructure needs, and policy dependence, but it lacks a standardized global estimate of additional energy demand and apples-to-apples comparisons with alternatives.

**Evidence**

- The prior review reports energy requirements of 2.5–8 GJ per tonne of CO₂ and costs of roughly $50–600 per tonne, while other evidence gives approximately €50–300 per tonne for capture, transport, and storage. [S1] [S12]
- The new review says prospective techno-economic and lifecycle assessments are necessary because technologies differ substantially in maturity and early-stage estimates contain significant uncertainty. [S21]
- The Clean Energy Ministerial paper states that capture in cement and steel remains nascent, costly, and dependent on substantially expanded pipelines, ports, policy support, and business models. [S23]
- The maritime pilot shows that energy and logistics penalties can materially reduce net savings when waste heat, transport, or handling systems are inefficient. [S20]

#### Finding 6

**Claim**

The strongest defensible argument for CCS is selective deployment in process-emissions-heavy sectors and in genuine carbon-dioxide-removal pathways, not universal use across power and energy.

**Confidence:** High

**Why this confidence level**

Supportive and critical sources agree most strongly on a conditional, sector-specific role, even though they differ over the breadth and urgency of deployment.

**Evidence**

- The review identifies hard-to-abate industrial sectors, especially cement, steel, and chemicals, as applications where alternatives are limited, while warning against locking in outdated fossil infrastructure. [S21]
- The IDDI paper says CCS is particularly relevant to emissions inherent to industrial processes and to removal of biogenic carbon, but that existing abatement, efficiency, and fuel-switching measures remain important. [S23]
- Prior IEA, EU, and critical-review evidence converges on a targeted role while warning that overreliance could delay renewables, efficiency, electrification, and other alternatives. [S1] [S2] [S5] [S8]

### Conflicts Found

- S20 reports that a particular mineralization utilization pathway can outperform offshore storage in lifecycle emissions savings, whereas the broader prior evidence emphasizes that utilization—especially enhanced-oil-recovery use—may not provide durable climate mitigation. These positions concern different utilization pathways and are not directly contradictory. [S20] [S11] [S15]
- The new review reports approximately 400 MtCO₂/year of announced capacity versus a 1 Gt/year 2030 target, while prior sources report only about 51–64 MtCO₂/year of operating capacity. The difference reflects announced versus operating capacity, not necessarily a factual contradiction. [S21] [S6] [S7]
- S20 presents an optimized onboard-capture scenario with 17.8% savings, while some pathway and advocacy sources describe CCS/CCUS as potentially critical or indispensable for net zero. The pilot result demonstrates limited project-level savings and does not resolve the larger question of future system-wide potential. [S20] [S16] [S18] [S19]
- The new sources emphasize the need for robust accounting and prospective assessment, while earlier supportive deployment estimates often present capacity figures without consistently distinguishing capture, utilization, durable storage, and removal. [S21] [S22] [S23] [S6] [S7]

### Important Gaps

- What is the independently verified global volume of CO₂ currently injected into and retained in dedicated geological storage, excluding temporary capture and enhanced-oil-recovery accounting?
- What standardized capture rates, availability, energy penalties, lifecycle emissions, leakage rates, and net climate benefits do major operating projects achieve?
- How do full-chain CCS costs and energy requirements compare with electrification, efficiency, renewable energy, alternative fuels, and process substitution in each target sector?
- What technically, legally, politically, and environmentally usable geological-storage capacity and transport infrastructure can be developed globally?
- How much additional low-carbon electricity or fuel would deployment at hundreds of millions to billions of tonnes per year require?
- How much projected future CCUS deployment represents conventional point-source emissions avoidance versus genuine atmospheric carbon-dioxide removal?
- Whether the reported utilization benefits in S20 remain favorable under alternative assumptions about product displacement, transport, durability, and opportunity costs.

**Analysis Duration:** 19.30s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The overall conclusion is now supportable, but an important empirical gap remains: the research state still lacks an independent, standardized global accounting of operating capture, injection, permanent retention, capture rates, energy penalties, and lifecycle emissions. This gap materially affects the evaluation of demonstrated effectiveness and net climate impact.

**Next Search**

> independent 2024 2025 global CCS operating projects verified CO2 injected permanent storage capture rate energy penalty lifecycle emissions

---

# Iteration 6

## 1. Search

**Query**

> independent 2024 2025 global CCS operating projects verified CO2 injected permanent storage capture rate energy penalty lifecycle emissions

**Why this query**

The overall conclusion is now supportable, but an important empirical gap remains: the research state still lacks an independent, standardized global accounting of operating capture, injection, permanent retention, capture rates, energy penalties, and lifecycle emissions. This gap materially affects the evaluation of demonstrated effectiveness and net climate impact.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S24 — CCUS projects around the world are reaching new milestones – Analysis - IEA**
  URL: https://www.iea.org/commentaries/ccus-projects-around-the-world-are-reaching-new-milestones
- **S25 — Global Status of CCS 2025 report highlights policy advancements and scaling up of CCS projects | Global CCS Institute posted on the topic | LinkedIn**
  URL: https://www.linkedin.com/posts/global-ccs-institute_global-status-of-ccs-activity-7382041437422583808-1cAp
- **S26 — List of carbon capture and storage projects - Wikipedia**
  URL: https://en.wikipedia.org/wiki/List_of_carbon_capture_and_storage_projects
- **S27 — Largest operational CCS projects globally 2025 - Statista**
  URL: https://www.statista.com/statistics/1108355/largest-carbon-capture-and-storage-projects-worldwide-capacity

**Search Duration:** 2.62s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Current operating CCUS capacity remains just over 50 MtCO₂ per year, while the current project pipeline could reach roughly 430 MtCO₂ per year of capture capacity and 670 MtCO₂ per year of storage capacity by 2030.

**Confidence:** High

**Why this confidence level**

These are direct figures from the IEA’s CCUS Projects Database update, although projected capacity is not equivalent to completed, utilized, or permanently verified storage.

**Evidence**

- The IEA reports just over 50 MtCO₂ of operational capture and storage capacity in the first quarter of 2025, with projected 2030 capture capacity of around 430 MtCO₂ per year and storage capacity of around 670 MtCO₂ per year based on the existing pipeline. [S24]

#### Finding 2

**Claim**

The new IEA evidence confirms that CCS is expanding, but current trends remain insufficient for a net-zero pathway.

**Confidence:** High

**Why this confidence level**

The new source directly states the insufficiency of current trends, and it is consistent with the large gap between current operations and pathway requirements.

**Evidence**

- The IEA states that current trends are insufficient for alignment with net zero by mid-century, despite renewed momentum and progress on first-of-a-kind projects. [S24]
- Earlier evidence likewise shows that current operating capacity is only about 0.1–0.16% of global emissions and that modeled pathways require expansion to hundreds of millions or billions of tonnes annually. [S6] [S7] [S11] [S21]

#### Finding 3

**Claim**

Pipeline growth should not be interpreted as demonstrated scalability: many projects remain planned or under construction, and recent additions to operating capacity have been marginal.

**Confidence:** High

**Why this confidence level**

The distinction between pipeline capacity and operating performance is explicit and supported by multiple sources.

**Evidence**

- The IEA reports that advanced-stage and under-construction projects account for 60% of the pipeline, while eight projects began operating in 2024 but were relatively small, leaving only a marginal increase in operational capture capacity. [S24]
- Prior sources similarly distinguish announced or constructed capacity from realized emissions reductions and report that historical deployment has been slow. [S7] [S8] [S9] [S21]

#### Finding 4

**Claim**

More than 60% of current operational capture capacity is located at natural-gas-processing facilities, so present deployment is not yet representative of the harder industrial applications often used to justify CCS’s future role.

**Confidence:** High

**Why this confidence level**

The operational-sector distribution is directly reported by the IEA; the implication for representativeness follows from the contrasting evidence about sectoral difficulty.

**Evidence**

- The IEA states that over 60% of operational capture capacity remains at natural gas processing facilities, while projects in hydrogen, carbon dioxide removal, and industry comprise over half of the pipeline expected to operate by 2030. [S24]
- Earlier evidence identifies cement, steel, chemicals, and removals as more difficult or strategically important applications, while noting that their capture costs and technical maturity are less favorable. [S11] [S15] [S21] [S23]

#### Finding 5

**Claim**

The strongest defensible conclusion remains conditional: CCS could make a significant future contribution, especially in hard-to-abate industrial processes and genuine removals, but its present demonstrated contribution is small and it is not a universal substitute for avoidance, efficiency, electrification, or renewable energy.

**Confidence:** High

**Why this confidence level**

This conclusion is supported by consistent evidence across institutional, critical, and technical sources, even though sources disagree about the eventual breadth and feasibility of deployment.

**Evidence**

- The IEA describes CCUS as potentially important for emissions from existing assets, hard-to-abate sectors, hydrogen, and carbon removal, while acknowledging that current trends are insufficient for net zero. [S8] [S24]
- Critical and supportive sources converge on targeted use in sectors such as cement, steel, chemicals, and selected removal pathways, while warning against overreliance and delay of alternatives. [S1] [S5] [S11] [S15] [S21] [S23]
- Current operating capacity is only roughly 51–64 MtCO₂ per year, and reported capacity does not consistently establish net, permanent geological storage. [S6] [S7] [S22] [S23]

### Conflicts Found

- The IEA projects approximately 430 MtCO₂ per year of capture capacity and 670 MtCO₂ per year of storage capacity by 2030, whereas current operating capacity is just over 50 MtCO₂ per year. These figures are not contradictory, but they highlight the unresolved difference between planned capacity and demonstrated delivery. [S24] [S6] [S7] [S21]
- The Global CCS Institute’s promotional summary reports total capture capacity of 513 Mtpa and a 54% year-on-year increase in operational projects, while the IEA reports just over 50 Mtpa in operation and approximately 430 Mtpa of 2030 capture capacity in its pipeline. The discrepancy likely reflects different definitions, dates, and inclusion criteria; the retrieved material does not reconcile them. [S24] [S25]
- The IEA presents new first-of-a-kind projects and pipeline advancement as signs of progress, while critical sources emphasize that operational capacity has increased only marginally and that current impact remains very small. The disagreement concerns the significance of recent momentum, not the existence of project development. [S1] [S13] [S21] [S24]

### Important Gaps

- What proportion of the IEA’s reported operational and projected capacity represents CO₂ actually injected into and permanently retained in dedicated geological storage, rather than capture capacity, utilization, enhanced oil recovery, or storage that has not yet been independently verified?
- What standardized project-level data would reconcile the differing capture-rate assessments and establish representative full-chain capture rates, availability, energy penalties, lifecycle emissions, leakage risks, and net climate benefits?
- How much additional low-carbon energy would deployment at the IEA’s projected 2030 scale—and at billion-tonne annual pathway scales—require?
- How do full-chain CCS costs compare with electrification, efficiency, renewable energy, alternative fuels, and process substitution in each target sector?
- What technically, legally, politically, and environmentally usable geological-storage capacity and transport infrastructure can be developed globally?
- How much future CCUS deployment represents conventional point-source emissions avoidance versus genuine atmospheric carbon-dioxide removal?

**Analysis Duration:** 14.85s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new IEA source materially strengthens the evidence on current capacity, pipeline scale, sector composition, and delivery momentum, but it does not resolve the most important remaining issue for evaluating demonstrated effectiveness: independently verified net permanent storage and full-chain climate performance. It also does not provide the missing global energy-demand and comparative-cost assessment.

**Next Search**

> independent assessment verified permanent CO2 storage current global CCS capacity lifecycle emissions energy penalty full-chain cost

---

# Iteration 7

## 1. Search

**Query**

> independent assessment verified permanent CO2 storage current global CCS capacity lifecycle emissions energy penalty full-chain cost

**Why this query**

The new IEA source materially strengthens the evidence on current capacity, pipeline scale, sector composition, and delivery momentum, but it does not resolve the most important remaining issue for evaluating demonstrated effectiveness: independently verified net permanent storage and full-chain climate performance. It also does not provide the missing global energy-demand and comparative-cost assessment.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S28 — [PDF] Carbon Capture and Storage Realising the potential?**
  URL: https://ukerc.rl.ac.uk/publications/research_report/Carbon_Capture_and_Storage-Realising_the_potential-Research_report.pdf
- **S29 — The costs of CO₂ capture, transport and storage**
  URL: https://carbonmanagementeurope.org/publication/the-costs-of-co2-capture-transport-and-storage
- **S30 — CCS deployment**
  URL: https://ieaghg.org/publications/ccs-deployment
- **S31 — Global CCS Institute | Carbon Management at Scale**
  URL: https://www.globalccsinstitute.com

**Search Duration:** 2.83s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources reinforce that CCS has plausible future potential but that its large-scale contribution remains conditional on resolving technical, economic, regulatory, and financial uncertainties.

**Confidence:** High

**Why this confidence level**

The sources directly address the question’s feasibility and barriers, and their conclusions align with the accumulated evidence that potential is substantial but not yet demonstrated at the required scale.

**Evidence**

- UKERC identifies unresolved uncertainties concerning full-scale technical proof, costs relative to alternatives, integration, storage safety, finance, policy, regulation, and public acceptance. It concludes that a persistent critical mass of unresolved uncertainties could derail deployment. [S28]
- IEAGHG concludes that CCS is technically feasible at scale and may have costs comparable to other mitigation technologies, but deployment is far behind low-carbon scenarios and faces technical, economic, institutional, regulatory, and cost-effectiveness barriers. [S30]

#### Finding 2

**Claim**

Large-scale CCS requires coordinated transport and storage infrastructure, particularly clustered networks, and cannot be evaluated solely as an individual capture technology.

**Confidence:** High

**Why this confidence level**

Both sources explicitly identify whole-system integration and infrastructure as prerequisites for deployment.

**Evidence**

- The UKERC report treats integration of CCS systems, storage, infrastructure, and speed of deployment as interacting uncertainties rather than isolated technical issues. [S28]
- The ZEP cost study states that large-scale CCS requires transport infrastructure comparable in scale to hydrocarbon infrastructure, and that clustering emitters and storage sites can reduce transport and storage costs. [S29]

#### Finding 3

**Claim**

Some older industry-supported cost assessments projected that CCS could become cost-competitive after demonstration and learning, but this is a forecast rather than demonstrated current performance.

**Confidence:** High

**Why this confidence level**

The sources clearly distinguish prospective cost reductions from current evidence; the newer evidence provides a stronger basis for judging present economics.

**Evidence**

- The ZEP study projected that post-demonstration CCS could become cost-competitive with other low-carbon energy technologies, based on assumed technology improvements, optimized plants, learning, and infrastructure economies of scale. [S29]
- More recent evidence reports high, source-dependent full-chain costs, continuing policy dependence, and uncertain cost reductions; projected future savings have not been demonstrated across the sector. [S1] [S12] [S21]

#### Finding 4

**Claim**

Storage potential may be geographically large, but usable storage capacity is constrained by site quality, injectivity, exploration risk, transport access, regulation, and long-term liability.

**Confidence:** Medium

**Why this confidence level**

The sources establish important constraints and broad potential, but they do not provide a current, independently verified global estimate of technically and politically usable capacity.

**Evidence**

- The ZEP study reports large variation in storage costs and identifies reservoir capacity, quality, location, injectivity, and storage type as key determinants. It argues that saline aquifer development requires risk-sharing mechanisms because sites may prove unsuitable after exploration. [S29]
- IEAGHG reports potentially sufficient storage for several decades in many countries but also identifies storage availability and institutional barriers as conditions affecting deployment. [S30]

#### Finding 5

**Claim**

The new material does not materially change the central conclusion: CCS could make a significant future contribution in selected sectors, but current demonstrated emissions reduction is small and does not justify universal deployment.

**Confidence:** High

**Why this confidence level**

The new and prior sources converge on a conditional, targeted role and a large gap between current impact and modeled requirements.

**Evidence**

- IEAGHG presents CCS as potentially important for deep emissions reductions while explicitly stating that deployment is far behind the levels envisaged by low-carbon scenarios. [S30]
- UKERC describes CCS as potentially crucial but emphasizes that its technical and commercial status remained uncertain and dependent on policy support and successful demonstrations. [S28]
- Accumulated evidence shows current operating capacity of roughly 51–64 MtCO₂ per year, only about 0.1–0.16% of global emissions, with uncertain distinction between captured, utilized, injected, and permanently stored CO₂. [S6] [S7] [S22] [S23]

### Conflicts Found

- The 2011 ZEP study projected that post-demonstration CCS would be cost-competitive with other low-carbon technologies, whereas newer evidence finds current full-chain costs high, application-dependent, and generally reliant on subsidies or other policy support. The difference reflects optimistic prospective assumptions versus later demonstrated market and project experience. [S29] [S1] [S12] [S21]
- IEAGHG and ZEP emphasize technical feasibility, storage potential, and the possibility of comparable costs, while UKERC stresses unresolved uncertainties and the risk that policy, finance, integration, and public acceptance could prevent deployment. These are conditional differences in emphasis rather than direct contradictions. [S28] [S29] [S30]
- The new sources are predominantly institutional or industry-linked and therefore provide stronger evidence about the arguments for deployment and expected enabling conditions than about independently verified net climate benefits, lifecycle emissions, or representative project performance. [S28] [S29] [S30] [S31]

### Important Gaps

- What proportion of current reported CCS capacity is actually injected into and permanently retained in dedicated geological storage, excluding enhanced-oil-recovery use and other utilization?
- What standardized project-level measurements would establish representative capture rates, availability, energy penalties, lifecycle emissions, leakage risks, and net climate benefits?
- How do full-chain CCS costs compare with electrification, efficiency, renewable energy, alternative fuels, and process substitution in each target sector?
- How much additional low-carbon energy and infrastructure would deployment at hundreds of millions to billions of tonnes per year require?
- What geological storage capacity is technically, legally, politically, and environmentally usable, and how rapidly can monitoring and long-term liability systems scale?
- How much future deployment represents conventional point-source emissions avoidance versus genuine atmospheric carbon-dioxide removal?

**Analysis Duration:** 13.88s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The accumulated evidence is sufficient to answer the original evaluative question responsibly: CCS has technically demonstrated operation and a plausible targeted role, but its current global impact is very small, costs and energy requirements are substantial and application-dependent, and large-scale permanent climate mitigation remains unproven. The remaining gaps concern desirable quantification rather than an unresolved central conclusion.

**Stop Reason:** sufficient_evidence

---

# Final Research Decision

**Research Stopped Because**

The analyzer determined that the important parts of the question could be answered responsibly.

**Stop Reason:** sufficient_evidence

**Searches Performed:** 7

**Unique Sources:** 31

**Remaining Uncertainty**

- An independently verified global inventory separating captured, transported, utilized, injected, retained, and permanently stored CO₂.
- Standardized project-level measurements of capture rates, availability, energy penalties, lifecycle emissions, leakage risk, and net climate benefit.
- Apples-to-apples comparisons between full-chain CCS and electrification, efficiency, renewable energy, alternative fuels, and process substitution in each target sector.
- A robust estimate of additional low-carbon electricity or fuel requirements at projected 2030 and billion-tonne-per-year deployment levels.
- A current assessment of geological storage that is technically, legally, politically, and environmentally usable, together with the infrastructure and long-term liability needed to access it.
- A clear separation in future scenarios between conventional point-source emissions avoidance and genuine atmospheric carbon-dioxide removal.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 7 | 21.49s |
| OpenAI Analysis | 7 | 126.14s |
| Report Generation | 1 | 22.57s |
| Total Run | — | 170.21s |
