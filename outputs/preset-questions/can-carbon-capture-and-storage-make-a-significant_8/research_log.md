# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

Can carbon capture and storage make a significant contribution to reducing global CO₂ emissions? Evaluate its demonstrated effectiveness, costs, scalability, energy requirements, and major arguments for and against large-scale deployment.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 10 / 10

**Unique Sources:** 26

**OpenAI Calls:** 11

**Tavily Calls:** 10

**Started:** 2026-09-01T03:49:15-04:00

**Ended:** 2026-09-01T03:52:45-04:00

**Total Runtime:** 209.44s

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
- **S2 — CCUS in the transition to net-zero emissions – CCUS in Clean Energy Transitions – Analysis - IEA**
  URL: https://www.iea.org/reports/ccus-in-clean-energy-transitions/ccus-in-the-transition-to-net-zero-emissions
- **S3 — Anticipating a potential deficit in global carbon capture demand in 2030 despite benchmarking strategies**
  URL: https://www.nature.com/articles/s44432-025-00002-0
- **S4 — What is carbon dioxide removal and capture in the context of climate change? | Brookings**
  URL: https://www.brookings.edu/articles/what-is-carbon-dioxide-removal-and-capture-in-the-context-of-climate-change
- **S5 — A Vision for Carbon Capture, Utilisation, and Storage in the EU – Clean Air Task Force**
  URL: https://www.catf.us/resource/a-vision-carbon-capture-utilisation-and-storage-eu

**Search Duration:** 2.60s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

CCS could make a significant contribution, but the evidence supports a selective rather than universal role, especially in hard-to-abate industries and for durable carbon removal.

**Confidence:** Medium

**Why this confidence level**

The sources agree on potential niche applications, but the retrieved material does not independently establish how large the resulting contribution would be globally.

**Evidence**

- The IEA identifies four potential roles for CCUS: addressing emissions from existing energy assets, reducing emissions in hard-to-abate sectors, producing low-carbon hydrogen, and removing CO₂ from the atmosphere to balance residual emissions. [S2]
- The EU CCUS Vision Working Group identifies cement, steel, chemicals, and waste incineration as important potential applications, particularly where process emissions cannot readily be eliminated by electrification or alternative fuels. [S5]
- The critical review does not reject CCS outright, but recommends strategic deployment in sectors such as cement and legacy industrial retrofits where alternatives are limited. [S1]

#### Finding 2

**Claim**

CCS’s demonstrated present-day climate impact is small relative to global emissions, and the technology has not yet delivered the scale anticipated in many scenarios.

**Confidence:** Medium

**Why this confidence level**

The quantitative present-scale claim comes primarily from one review, while the second source provides corroborating direction but not a directly comparable global operating total in the retrieved excerpt.

**Evidence**

- The review states that, despite more than $40 billion in global investment, CCS captures and stores less than 0.1% of annual global CO₂ emissions. [S1]
- The Nature study reports that CCUS deployment is lagging behind expectations and projects a persistent deficit relative to climate-target requirements, even under an optimized strategy that could double capture scale by 2030. [S3]

#### Finding 3

**Claim**

The principal economic barriers are high and uncertain costs, project cost overruns, and difficulty achieving economies of scale.

**Confidence:** Medium

**Why this confidence level**

The sources provide useful ranges and identify consistent barriers, but the retrieved material does not specify boundaries such as capture source, capture rate, transport, storage, financing assumptions, or whether costs are real or modeled.

**Evidence**

- The review gives an indicative energy-demand range of 2.5–8 GJ per tonne of CO₂ and a cost range of $50–600 per tonne of CO₂, while citing cost overruns among recurring problems in projects such as Petra Nova, Gorgon, Sleipner, and In Salah. [S1]
- The Nature study finds that cost barriers significantly impede economies of scale and that CCUS development remains highly unequal across countries and regions. [S3]

#### Finding 4

**Claim**

CCS has substantial energy requirements that can reduce its net emissions benefit and increase infrastructure needs.

**Confidence:** Medium

**Why this confidence level**

The energy range is directly reported, but the sources do not provide a full lifecycle comparison with efficiency penalties, additional fuel use, upstream methane, or alternative technologies.

**Evidence**

- The review identifies energy demand of approximately 2.5–8 GJ per tonne of CO₂ as a key evaluation criterion. [S1]
- The EU report describes the need for extensive capture, transport, utilization, and storage infrastructure and emphasizes that deployment must occur across borders and at very large annual volumes. [S5]

#### Finding 5

**Claim**

Large-scale deployment faces technical and governance risks, including suboptimal capture performance, geological uncertainty, long-term liability, and infrastructure coordination challenges.

**Confidence:** Medium

**Why this confidence level**

These are clearly identified risks, but the retrieved excerpts do not quantify failure rates, leakage rates, liability durations, or the frequency of capture underperformance.

**Evidence**

- The review reports recurring suboptimal capture rates, geological uncertainties, and transfer of public liability, and argues that projects described as successful may fall short on durability, scale, and claimed emissions offsets. [S1]
- The EU strategy paper says cross-border coordination and Commission leadership are necessary because capture, transport, utilization, and storage networks are unlikely to develop quickly enough without coordinated action. [S5]

#### Finding 6

**Claim**

Arguments in favor of CCS include addressing unavoidable process emissions, preserving some existing industrial assets, enabling low-carbon hydrogen, and providing durable storage for BECCS or direct-air-capture removals.

**Confidence:** Medium

**Why this confidence level**

These are scenario-based and strategic arguments rather than demonstrations of achieved global performance.

**Evidence**

- The IEA presents CCUS as essential in its Sustainable Development Scenario and describes roles in existing assets, hard-to-abate sectors, hydrogen, and atmospheric carbon removal. [S2]
- The EU report argues that process emissions from cement and lime are intrinsically difficult to eliminate and that geological storage of biogenic or direct-air-captured CO₂ can provide permanent removals. [S5]

#### Finding 7

**Claim**

Arguments against indiscriminate CCS deployment include high costs, energy use, limited current scale, project underperformance, geological and permanence uncertainty, and the risk that investment in CCS delays more scalable or lower-cost mitigation options.

**Confidence:** Medium

**Why this confidence level**

The concerns are supported by the retrieved sources, but comparative claims about alternatives are not accompanied by consistent lifecycle, cost, or scalability metrics.

**Evidence**

- The review characterizes continued broad reliance on CCS as a high-cost gamble, highlights project shortcomings, and identifies renewables, bio-based removals, and mineralization as potentially more scalable or permanent alternatives in some contexts. [S1]
- The Nature study finds persistent cost barriers and a projected shortfall against climate targets, challenging assumptions that policy support alone will produce sufficient scale. [S3]

### Conflicts Found

- The IEA and EU CCUS Vision present CCUS as important or essential for net-zero pathways, whereas the critical review argues that empirical performance is far below modeled expectations and that broad reliance on CCS may delay more effective options. This is partly a conditional disagreement: CCS may be necessary in hard-to-abate sectors and for some removals, but not necessarily a generally effective strategy across the energy system. [S1] [S2] [S5]
- The EU report cites modeled global and EU requirements of very large future capture and storage volumes, while the Nature study indicates that even optimized development may leave a substantial deficit by 2030. These sources differ more in outlook and feasibility than in their recognition that current deployment is insufficient. [S3] [S5]

### Important Gaps

- What is the current verified global capture and permanent-storage capacity, measured by actual tonnes stored rather than nameplate capacity?
- What are the demonstrated capture rates, availability, lifecycle emissions, and net-abatement results of major operating projects across power, hydrogen, cement, and other industries?
- How do CCS costs and energy penalties compare, on a consistent lifecycle basis, with electrification, renewable hydrogen, efficiency, and other decarbonization options?
- How much suitable geological storage is available in practice, considering site characterization, transport networks, monitoring, leakage risk, public acceptance, and long-term liability?
- What proportion of projected future CCS deployment is fossil-fuel abatement, utilization, BECCS, or direct-air capture, and how much would constitute durable net removal?
- Are the cost and energy ranges in the review based on comparable sources and system boundaries, and how sensitive are they to CO₂ concentration and project scale?

**Analysis Duration:** 20.52s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

Another search would materially improve the answer because the current sources do not provide a reliable, independently verified account of operating global capacity, project-level demonstrated effectiveness, or comparable lifecycle costs and energy penalties. Those metrics are central to evaluating whether CCS can make a significant contribution rather than merely having a modeled role.

**Next Search**

> IEA Global CCS Institute 2024 2025 operating carbon capture capacity tonnes stored project performance capture rates cost energy penalty

---

# Iteration 2

## 1. Search

**Query**

> IEA Global CCS Institute 2024 2025 operating carbon capture capacity tonnes stored project performance capture rates cost energy penalty

**Why this query**

Another search would materially improve the answer because the current sources do not provide a reliable, independently verified account of operating global capacity, project-level demonstrated effectiveness, or comparable lifecycle costs and energy penalties. Those metrics are central to evaluating whether CCS can make a significant contribution rather than merely having a modeled role.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S6 — Global Status of CCS | Global CCS Institute**
  URL: https://www.globalccsinstitute.com/global-status-of-ccs
- **S7 — Minimal role for carbon capture, utilization, and storage (CCUS) in IEA's World Energy Outlook 2025 | IEEFA**
  URL: https://ieefa.org/resources/minimal-role-carbon-capture-utilization-and-storage-ccus-ieas-world-energy-outlook-2025
- **S8 — Publications Archive | Global CCS Institute**
  URL: https://www.globalccsinstitute.com/publications
- **S9 — Carbon Capture and Storage Capacity Worldwide**
  URL: https://incorrys.com/environmental-data/carbon-capture-and-storage/carbon-capture-and-storage-capacity-worldwide
- **S10 — Announced and operational carbon capture, utilisation and storage capacity in 2030 across editions of IEA CCUS Projects Database – Charts – Data & Statistics - IEA**
  URL: https://www.iea.org/data-and-statistics/charts/announced-and-operational-carbon-capture-utilisation-and-storage-capacity-in-2030-across-editions-of-iea-ccus-projects-database

**Search Duration:** 3.50s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Current operational CCS capacity remains a very small fraction of global CO₂ emissions, even though the project pipeline is expanding.

**Confidence:** Medium

**Why this confidence level**

The operational-capacity estimate is directly quantified by S9, while S6 corroborates rapid pipeline growth. However, the sources differ in definitions and do not establish how much captured CO₂ is actually permanently stored or how consistently facilities operate.

**Evidence**

- Incorrys reports approximately 51 MtCO₂ per year of operational global CCS capacity at the end of 2024, compared with 37,600 MtCO₂ per year of energy and industrial-process emissions—about 0.16%. It also reports more than 50 MtCO₂ per year under construction, implying potential near-term doubling if projects are completed. [S9]
- The Global CCS Institute reports 77 operating projects and 47 projects under construction in 2025, and says planned capacity has grown at more than 30% annually since 2017. [S6]

#### Finding 2

**Claim**

The new evidence strengthens the conclusion that CCS could contribute materially in selected applications, but does not support treating it as a dominant economy-wide emissions-reduction strategy.

**Confidence:** Medium

**Why this confidence level**

The finding is consistent with the prior selective-role conclusion, but S7 is an advocacy organization’s interpretation of a cited IEA report rather than the primary report excerpt itself.

**Evidence**

- An analysis citing the IEA World Energy Outlook 2025 says CCUS contributes at most 4.9% of total emissions reductions in the IEA Net Zero Emissions scenario by 2050—1.2% from power and 3.7% from industry—while renewables, electrification, fuel switching, and efficiency provide more than 82%. [S7]
- The earlier evidence identifies hard-to-abate industrial process emissions, existing assets, hydrogen, and durable removals as the main strategic roles for CCUS. [S2] [S5]

#### Finding 3

**Claim**

End-to-end CCS costs can be high enough to require substantial policy support or carbon prices, particularly in Europe.

**Confidence:** Medium

**Why this confidence level**

The new source adds an end-to-end regional estimate and supports the conclusion that economics are a major barrier. Direct comparison is limited because the ranges may use different technologies, CO₂ sources, system boundaries, currencies, and assumptions.

**Evidence**

- S7 cites an estimate of EUR105–280 per tonne of CO₂ for end-to-end disposal in the EU, including capture, transport, and permanent storage, and notes that the lower end exceeded the average 2025 EU ETS price of EUR75 per tonne. [S7]
- The prior review reported a much broader indicative CCS cost range of $50–600 per tonne and recurring project cost overruns. [S1]

#### Finding 4

**Claim**

The technology’s scalability is demonstrated more clearly by project growth and storage infrastructure development than by achieved global climate impact.

**Confidence:** Medium

**Why this confidence level**

There is evidence of expanding deployment plans, but planned or announced capacity is not equivalent to delivered, available, or permanently stored CO₂.

**Evidence**

- The Global CCS Institute reports continued movement of projects into operation and construction and links project growth to policy, legal, and regulatory frameworks. [S6]
- The IEA maintains a database covering operational, under-construction, and planned capture facilities, with thresholds for point-source projects and direct-air-capture facilities, indicating an increasingly organized project pipeline. [S10]
- Despite this pipeline, the reported operating capacity remains roughly 0.16% of global energy and industrial-process emissions. [S9]

#### Finding 5

**Claim**

The energy penalty and opportunity-cost arguments against broad CCS deployment remain unresolved and important.

**Confidence:** Medium

**Why this confidence level**

The sources support a substantial energy and opportunity-cost concern, but no new source provides a consistent lifecycle comparison across sectors or verifies net-abatement performance for representative operating projects.

**Evidence**

- The prior review estimates CCS energy demand at approximately 2.5–8 GJ per tonne of CO₂ and warns that this can reduce net emissions benefits and increase infrastructure requirements. [S1]
- S7 argues that high investment and operating costs make CCUS less competitive than renewables, storage, electrification, and efficiency in many applications, while the IEA scenario it discusses assigns those alternatives most emissions reductions. [S7]

### Conflicts Found

- S6 presents CCS as remaining on track toward gigatonne-scale deployment and emphasizes policy-supported expansion, whereas S7 interprets the IEA’s 2025 net-zero scenario as assigning CCUS a minimal role—under 5% of emissions reductions. This is partly a disagreement about future significance and partly about the benchmark: a rapidly growing pipeline can coexist with a relatively small contribution to total global reductions. [S6] [S7]
- The earlier IEA and EU strategy sources characterize CCUS as important or potentially essential for hard-to-abate sectors and removals, while S7 argues that CCUS is not essential to achieving decarbonization in the IEA’s 2025 scenario. The disagreement is conditional on sector, scenario, and whether the question concerns economy-wide mitigation or residual/process emissions. [S2] [S5] [S7]
- S9 reports 51 MtCO₂ per year of operational capacity, while S6 reports 77 operating projects but does not provide a comparable operating-tonnage figure. These figures are not necessarily inconsistent because project counts and capacity totals may use different inclusion criteria and facility definitions. [S6] [S9]

### Important Gaps

- What fraction of the reported 51 MtCO₂ per year operational capacity is actually captured and permanently stored, rather than nameplate, utilized, or associated with enhanced oil recovery?
- What are the measured capture rates, operating availability, energy penalties, lifecycle emissions, and net CO₂ reductions of major operating projects?
- Does the IEA World Energy Outlook 2025 primary text actually support S7’s precise 4.9% figure, and how is that percentage defined?
- How much of the expanding project pipeline will reach operation, and what are the regional and sectoral constraints on transport, storage characterization, permitting, public acceptance, and long-term liability?
- How do CCS costs and energy requirements compare on a consistent lifecycle basis with electrification, efficiency, renewable hydrogen, and other alternatives in cement, steel, chemicals, power, and hydrogen?
- How much future CCS deployment represents durable atmospheric removal through BECCS or direct air capture rather than fossil-fuel or industrial point-source abatement?

**Analysis Duration:** 17.57s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources improve the evidence on current capacity, project pipelines, and scenario-based contribution, but the central evaluation still lacks independently verified operating performance and a primary-source validation of the precise IEA 2025 contribution estimate. Those gaps materially affect judgments about demonstrated effectiveness, net emissions benefit, and scalability.

**Next Search**

> IEA World Energy Outlook 2025 CCUS 4.9% emissions reductions 2050 capture storage operating capacity capture rates

---

# Iteration 3

## 1. Search

**Query**

> IEA World Energy Outlook 2025 CCUS 4.9% emissions reductions 2050 capture storage operating capacity capture rates

**Why this query**

The new sources improve the evidence on current capacity, project pipelines, and scenario-based contribution, but the central evaluation still lacks independently verified operating performance and a primary-source validation of the precise IEA 2025 contribution estimate. Those gaps materially affect judgments about demonstrated effectiveness, net emissions benefit, and scalability.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S11 — Evolution of capture capacity either operational or under construction by sector between 2025 and 2026 editions of IEA CCUS Projects Database – Charts – Data & Statistics - IEA**
  URL: https://www.iea.org/data-and-statistics/charts/evolution-of-capture-capacity-either-operational-or-under-construction-by-sector-between-2025-and-2026-editions-of-iea-ccus-projects-database
- **S12 — World Energy Outlook 2025 – Analysis**
  URL: https://www.iea.org/reports/world-energy-outlook-2025
- **S13 — CCUS Projects Explorer – Data Tools**
  URL: https://www.iea.org/data-and-statistics/data-tools/ccus-projects-explorer

**Search Duration:** 2.71s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The IEA’s CCUS project database is a structured global inventory of large-scale projects, but it tracks announced project capacity and project status rather than directly demonstrating actual captured or permanently stored CO₂.

**Confidence:** High

**Why this confidence level**

This follows directly from the database’s stated scope and inclusion criteria, although the retrieved material does not show the underlying project-level data.

**Evidence**

- The database covers worldwide capture, transport, storage and utilisation projects commissioned since the 1970s, with announced-capacity thresholds above 100,000 tonnes per year for most projects and 1,000 tonnes per year for direct-air-capture facilities. [S13]
- The database includes projects that have been commissioned or are in planning, so its coverage supports assessment of the project pipeline but does not by itself establish operating performance or tonnes permanently stored. [S13]

#### Finding 2

**Claim**

The new IEA material confirms that operational and under-construction capture capacity is being tracked by sector, but the retrieved chart excerpt provides no numerical values or sector-specific results that would materially change the assessment of current scale or costs.

**Confidence:** High

**Why this confidence level**

The source’s existence and stated comparison are clear, while the absence of numerical findings limits what can responsibly be inferred.

**Evidence**

- The IEA publishes a chart comparing capture capacity that is operational or under construction across sectors between the 2025 and 2026 editions of its CCUS Projects Database. [S11]
- The chart page identifies the database as its source but the retrieved content does not include the chart values, capacity totals, capture rates, costs, energy requirements, or storage outcomes. [S11]

#### Finding 3

**Claim**

The retrieved World Energy Outlook 2025 page provides general information about the IEA’s scenario-based energy analysis but does not verify the precise claim that CCUS accounts for 4.9% of emissions reductions in the 2050 net-zero scenario.

**Confidence:** High

**Why this confidence level**

The relevant numerical passage is absent from the retrieved source, so S12 cannot independently support or refute the 4.9% figure.

**Evidence**

- The WEO page describes the report as a multi-scenario analysis of possible energy futures, policies, technology, markets and emissions, but the retrieved excerpt does not contain the CCUS contribution figure or its definition. [S12]

### Conflicts Found

- No substantive new conflict is established. The IEA database’s inclusion of operational, under-construction and planned projects is compatible with both rapid pipeline growth and the prior finding that delivered global climate impact remains small; project counts or announced capacity do not resolve that distinction. [S6] [S9] [S13]

### Important Gaps

- What numerical operational and under-construction capacities are shown in the IEA’s 2025–2026 sector comparison?
- What tonnes of CO₂ are actually captured and permanently stored annually, as opposed to announced or nameplate capacity?
- What are the measured capture rates, availability, energy penalties, lifecycle emissions and net-abatement results of major operating projects?
- Does the primary WEO 2025 text define and substantiate the cited 4.9% CCUS share of emissions reductions?
- How much planned capacity will reach operation, and what share concerns durable removals versus point-source abatement or utilisation?

**Analysis Duration:** 11.29s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources improve confidence about the IEA’s project-tracking scope but do not fill the most important evidence gap: verified real-world capture and permanent-storage performance. They also do not validate the precise WEO-based percentage used in the accumulated findings.

**Next Search**

> global CCS projects actual CO2 captured permanently stored 2024 2025 operating capture rates availability energy penalty

---

# Iteration 4

## 1. Search

**Query**

> global CCS projects actual CO2 captured permanently stored 2024 2025 operating capture rates availability energy penalty

**Why this query**

The new sources improve confidence about the IEA’s project-tracking scope but do not fill the most important evidence gap: verified real-world capture and permanent-storage performance. They also do not validate the precise WEO-based percentage used in the accumulated findings.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S14 — CCUS In 2025: An End-Of-Year Review**
  URL: https://carbonherald.com/ccus-in-2025-an-end-of-year-review
- **S15 — Carbon Capture, Utilization, and Storage Industry**
  URL: https://www.persistencemarketresearch.com/market-research/carbon-capture-utilization-storage-market.asp
- **S16 — Commercial Carbon Capture Plants: International Operating CCS Projects | CCS Knowledge Centre**
  URL: https://ccsknowledge.com/carbon-management-101/international-ccs-projects
- **S17 — List of carbon capture and storage projects - Wikipedia**
  URL: https://en.wikipedia.org/wiki/List_of_carbon_capture_and_storage_projects

**Search Duration:** 2.59s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

New evidence reinforces that CCS has expanded substantially in project count and reported capture capacity, but its demonstrated global climate contribution remains small relative to total emissions.

**Confidence:** Medium

**Why this confidence level**

The new source adds a higher operating-capacity estimate and the secondary review provides a cumulative-storage figure, but the sources use different dates, inclusion criteria, and definitions. None establishes a single independently verified total of tonnes actually and permanently stored annually.

**Evidence**

- The CCS Knowledge Centre, using data from the Global Status of CCS 2025 report, lists 63.9 MtCO₂ per year of capture capacity across operating commercial facilities: 30.19 Mtpa in North America, 14.20 in South America, 11.05 in Asia, 5.80 in Oceania, and 2.66 in Europe. [S16]
- The accumulated evidence estimates approximately 51 MtCO₂ per year of operational capacity at the end of 2024, about 0.16% of energy and industrial-process emissions, while the Global CCS Institute reports 77 operating projects in 2025. [S9] [S6]
- Carbon Herald reports 77 operating projects and 47 under construction in 2025 and cites more than 380 Mt of industrial CO₂ captured and permanently stored since 1996. [S14]

#### Finding 2

**Claim**

The apparent growth in CCS is more firmly demonstrated by deployment pipelines and facility counts than by consistent evidence of operating performance or net emissions reduction.

**Confidence:** Medium

**Why this confidence level**

Multiple sources document expansion, but the evidence does not provide standardized availability, capture-rate, lifecycle-emissions, or permanent-storage data.

**Evidence**

- The 2025 operating-facility list is limited to projects above 100,000 tonnes per year and reports 51 pre-combustion, 11 post-combustion, and one oxy-fuel facility, with DAC facilities too small to appear in the map. [S16]
- Carbon Herald describes sharply growing commercial-facility numbers, investment, policy support, and project starts, but also reports that public support was uneven and that some US projects were delayed, re-scoped, or cancelled. [S14]
- The IEA database’s inclusion of commissioned, under-construction, and planned facilities demonstrates pipeline tracking rather than actual captured or permanently stored volumes. [S13]

#### Finding 3

**Claim**

CCS remains technically relevant for concentrated industrial sources and some removal pathways, especially where process emissions are difficult to eliminate, but the new evidence does not justify broad deployment across all sectors.

**Confidence:** Medium

**Why this confidence level**

The sectoral rationale is consistent with prior evidence, but the new source is a commercial market forecast and does not independently quantify the net global contribution or compare alternatives on a common basis.

**Evidence**

- The accumulated evidence identifies cement, steel, chemicals, existing energy assets, hydrogen, BECCS, and direct-air-capture storage as potential applications where CCS may address residual or process emissions. [S2] [S5]
- The market report states that cement process emissions cannot readily be eliminated through fuel switching or electrification and cites operating or emerging cement-capture projects in China and Norway. [S15]
- The same report describes oil and gas as the largest end-use segment and highlights CO₂-EOR as a revenue source, illustrating that much current and projected deployment is associated with fossil-fuel and industrial systems rather than atmospheric removal. [S15]

#### Finding 4

**Claim**

Economic viability depends heavily on policy support, project scale, and revenue mechanisms; market growth forecasts should not be interpreted as evidence that CCS is already cost-competitive or scalable at climate-relevant levels.

**Confidence:** Medium

**Why this confidence level**

The sources consistently identify policy dependence and high costs, but S15 is a commissioned market forecast whose projections are not equivalent to demonstrated project economics.

**Evidence**

- Carbon Herald says the business case remains the core challenge to broader deployment and reports that rising costs and changes to government grants delayed or reshaped projects. [S14]
- The market report attributes deployment momentum to US tax incentives, including credits of up to $85 per tonne for permanent storage and $60 per tonne for utilization, and forecasts market growth from $3.5 billion in 2026 to $22 billion in 2033. [S15]
- Prior evidence reports indicative CCS costs of $50–600 per tonne and EU end-to-end disposal costs of €105–280 per tonne, with recurring cost overruns. [S1] [S7]

#### Finding 5

**Claim**

Long-term storage is demonstrated at some projects, but the retrieved evidence still shows important risks concerning site integrity, monitoring, and liability.

**Confidence:** Medium

**Why this confidence level**

In Salah provides a concrete example of storage-integrity concerns without reported leakage, but one project cannot establish general storage failure rates or long-term permanence.

**Evidence**

- The project list reports approximately 3.8 Mt stored at In Salah, where injection was suspended after concerns about seal integrity, fracture risk, and CO₂ movement outside the lease; no leakage was reported during the project’s operation. [S17]
- Prior evidence identifies geological uncertainty, long-term liability, and suboptimal capture performance as recurring CCS risks. [S1]

### Conflicts Found

- S16 reports 63.9 Mtpa of operating capture capacity, while S9 reports approximately 51 Mtpa at the end of 2024. This is not necessarily a substantive contradiction because the figures differ in date, project thresholds, and whether they count commercial facilities, capture capacity, or broader CCS capacity; however, the discrepancy prevents treating either as a definitive current global total. [S9] [S16]
- S14 cites more than 380 Mt of industrial CO₂ captured and permanently stored since 1996, whereas the other sources primarily report annual nameplate capacity or project counts. These measures are not directly comparable, and the secondary source does not provide the underlying project-by-project verification in the retrieved excerpt. [S14] [S6] [S9] [S16]
- S15 presents rapid projected market and capacity growth, including 812 Mtpa across announced projects by 2030, while prior evidence finds that current deployment is far below scenario requirements and that pipeline capacity does not ensure completed or operating projects. The disagreement is about forecast realization, not current scale. [S15] [S3] [S6] [S9]

### Important Gaps

- What is the independently verified current annual quantity of CO₂ actually captured and permanently stored, rather than nameplate capacity or cumulative industry claims?
- What are measured capture rates, availability, energy penalties, lifecycle emissions, and net-abatement results for representative operating projects in power, cement, hydrogen, and gas processing?
- How much of operating and planned capacity is associated with CO₂-EOR or fossil-fuel production versus dedicated permanent storage, BECCS, or direct-air capture?
- What fraction of announced capacity will reach final investment decision and operation, given reported cost pressures, grant cancellations, permitting, transport coordination, and storage-site constraints?
- How do CCS costs and energy requirements compare with electrification, efficiency, renewable hydrogen, and other alternatives using consistent sector-specific system boundaries?
- Does the cumulative claim of more than 380 Mt permanently stored withstand independent primary-source verification, and how is permanence defined?

**Analysis Duration:** 18.17s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new sources strengthen evidence for project growth and provide a concrete storage-integrity example, but they do not resolve the most important gap for evaluating demonstrated effectiveness: actual tonnes permanently stored, operating capture performance, energy penalties, and net lifecycle abatement. The capacity discrepancy also warrants verification from a primary tracker.

**Next Search**

> Global CCS Institute 2025 operating projects actual CO2 captured permanently stored capture rates availability energy penalty project performance

---

# Iteration 5

## 1. Search

**Query**

> Global CCS Institute 2025 operating projects actual CO2 captured permanently stored capture rates availability energy penalty project performance

**Why this query**

The new sources strengthen evidence for project growth and provide a concrete storage-integrity example, but they do not resolve the most important gap for evaluating demonstrated effectiveness: actual tonnes permanently stored, operating capture performance, energy penalties, and net lifecycle abatement. The capacity discrepancy also warrants verification from a primary tracker.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S18 — Global Status of CCS 2025 report highlights policy advancements and scaling up of CCS projects | Global CCS Institute posted on the topic | LinkedIn**
  URL: https://www.linkedin.com/posts/global-ccs-institute_global-status-of-ccs-activity-7382041437422583808-1cAp
- **S19 — Global CCS Institute | Carbon Management at Scale**
  URL: https://www.globalccsinstitute.com
- **S20 — Carbon Capture Stays the Course Despite Global Headwinds, with 54% Rise in Operational Projects | Global CCS Institute**
  URL: https://www.globalccsinstitute.com/carbon-capture-stays-the-course-despite-global-headwinds-with-54-rise-in-operational-projects

**Search Duration:** 2.60s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

CCS deployment is growing rapidly in project count and planned capture capacity, but this does not demonstrate equivalent growth in actual emissions reductions.

**Confidence:** High

**Why this confidence level**

The new source directly documents project and pipeline growth, while multiple prior sources establish that delivered operating capacity remains very small. The distinction between announced capacity and actual performance is clear.

**Evidence**

- The Global CCS Institute reports operational projects increasing from 50 to 77, 47 projects under construction with 44 Mtpa cumulative capture capacity, and 610 projects at various development stages. Total operating and developmental capture capacity reached 513 Mtpa, up 23%. [S20]
- The accumulated evidence estimates current operating capacity at only about 51 MtCO₂ per year, approximately 0.16% of global energy and industrial-process emissions; other sources report 63.9 Mtpa under different definitions. [S9] [S16]
- The IEA database includes commissioned, under-construction, and planned projects, so pipeline capacity is not equivalent to captured or permanently stored CO₂. [S13]

#### Finding 2

**Claim**

The new evidence strengthens the case that CCS is technically and commercially expanding, particularly in industrial sectors, but it does not establish that CCS is already scalable at climate-relevant global levels.

**Confidence:** Medium

**Why this confidence level**

Sectoral deployment and project growth are directly reported, but future capacity depends on projects reaching construction and operation, and the source provides no standardized evidence on utilization, availability, net abatement, or storage permanence.

**Evidence**

- The Institute says CCS is expanding in cement, chemicals, and energy and identifies policy, finance, infrastructure, and international collaboration as conditions for further deployment. [S20]
- Earlier evidence identifies cement, chemicals, steel, existing energy assets, hydrogen, BECCS, and direct-air capture as possible applications, especially where process emissions or residual emissions are difficult to eliminate. [S2] [S5] [S15]
- The Institute’s reported 513 Mtpa includes projects in development, whereas operating capacity is roughly 51–63.9 Mtpa in other sources. [S20] [S9] [S16]

#### Finding 3

**Claim**

The new source is supportive evidence for CCS’s potential but should be treated as advocacy or industry-source evidence rather than an independent evaluation of effectiveness or cost.

**Confidence:** High

**Why this confidence level**

The source’s institutional position is explicit, and its numerical project claims are useful for deployment trends but do not independently resolve effectiveness, economics, or lifecycle impacts.

**Evidence**

- The Global CCS Institute describes itself as advocating for CCS as a critical climate solution, and its CEO characterizes CCS as essential to climate goals. [S19] [S20]
- The release acknowledges inflationary pressures and says durable policies, investable business models, and infrastructure are needed to sustain deployment, indicating that growth remains policy- and finance-dependent. [S20]
- Prior evidence reports high and uncertain costs, energy requirements of approximately 2.5–8 GJ per tonne, project overruns, and current capacity below 0.1–0.2% of global emissions. [S1] [S9]

#### Finding 4

**Claim**

The overall answer remains conditional: CCS can make a significant contribution in selected hard-to-abate industries and durable-removal pathways, but current evidence does not support relying on it as the dominant economy-wide mitigation strategy.

**Confidence:** Medium

**Why this confidence level**

The selective-role conclusion is consistent across the evidence. The exact future global share remains less certain because the 4.9% figure is not independently verified from the primary WEO text.

**Evidence**

- The IEA and EU sources identify roles for CCUS in process emissions, existing assets, low-carbon hydrogen, BECCS, and direct-air-capture storage. [S2] [S5]
- Current operating capacity is a tiny fraction of global emissions, while the project pipeline is much larger than delivered capacity. [S9] [S13] [S20]
- The retrieved interpretation of the IEA net-zero scenario assigns CCUS no more than 4.9% of total emissions reductions by 2050, although the primary WEO excerpt does not verify that precise figure. [S7] [S12]

### Conflicts Found

- The Global CCS Institute calls CCS essential and presents rapid expansion as evidence of a clear trajectory toward scale, while prior critical evidence emphasizes that actual operating capacity remains tiny, costs are high, and projects have often underperformed. This is partly a difference between deployment momentum and demonstrated climate effectiveness, and partly an institutional disagreement about how indispensable CCS is. [S1] [S20]
- The Institute reports 513 Mtpa of total capture capacity, but that figure combines operating and developmental projects. It therefore appears much larger than estimates of approximately 51–63.9 Mtpa of operating capacity; the measures are not directly contradictory but could mislead if treated as equivalent. [S9] [S16] [S20]

### Important Gaps

- What proportion of the 77 operating projects’ nameplate capacity is actually captured and permanently stored annually?
- What are standardized measured capture rates, availability, energy penalties, lifecycle emissions, and net-abatement results for representative projects?
- How much of the 513 Mtpa total is likely to reach operation, and what proportion involves dedicated permanent storage, CO₂-EOR or other utilization, fossil-fuel processing, BECCS, or direct-air capture?
- Does the primary IEA World Energy Outlook 2025 text substantiate and define the cited 4.9% contribution of CCUS to total emissions reductions?
- How do CCS costs and energy requirements compare with electrification, efficiency, renewable hydrogen, and other alternatives on consistent sector-specific boundaries?

**Analysis Duration:** 14.57s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The accumulated evidence is sufficient to answer the original question responsibly: CCS has demonstrated feasibility and is expanding, but current delivered impact is small, costs and energy requirements are substantial and uncertain, and its strongest rationale is selective deployment for hard-to-abate process emissions and durable removals. Another search could improve project-level performance metrics, but it is not necessary to support the central evaluation; those gaps should be stated explicitly rather than delaying the conclusion.

**Next Search**

> Can carbon capture and storage make a significant contribution to reducing global CO₂ emissions? Evaluate its demonstrated effectiveness, costs, scalability, energy requirements, and major arguments for and against large-scale deployment. additional evidence search 6

---

# Iteration 6

## 1. Search

**Query**

> Can carbon capture and storage make a significant contribution to reducing global CO₂ emissions? Evaluate its demonstrated effectiveness, costs, scalability, energy requirements, and major arguments for and against large-scale deployment. additional evidence search 6

**Why this query**

The accumulated evidence is sufficient to answer the original question responsibly: CCS has demonstrated feasibility and is expanding, but current delivered impact is small, costs and energy requirements are substantial and uncertain, and its strongest rationale is selective deployment for hard-to-abate process emissions and durable removals. Another search could improve project-level performance metrics, but it is not necessary to support the central evaluation; those gaps should be stated explicitly rather than delaying the conclusion.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S21 — A Comprehensive Review of Carbon Capture, Storage, and Reduction Strategies Within the Built Environment**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12735339
- **S22 — Carbon capture, utilisation and storage**
  URL: https://www.iea.org/energy-system/renewables-and-low-emissions/carbon-capture-utilisation-and-storage
- **S23 — Carbon Capture and Storage (CCS): The Future of Climate ...**
  URL: https://blog.verde.ag/en/carbon-capture-and-storage-ccs
- **S24 — Carbon Capture**
  URL: https://www.c2es.org/content/carbon-capture

**Search Duration:** 2.87s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources do not materially change the central conclusion: CCS may contribute significantly in selected sectors, but current evidence does not support relying on it as the dominant global emissions-reduction strategy.

**Confidence:** High

**Why this confidence level**

The new IEA page is consistent with the existing distinction between deployment tracking and demonstrated climate impact, but it adds no performance data.

**Evidence**

- The IEA source presents CCUS as an actively tracked mitigation technology and provides an installed-capture-capacity time series, but the retrieved page contains no numerical values or evidence of actual tonnes permanently stored. [S22]
- The accumulated evidence shows that operating capacity is only a small fraction of global emissions, while most reported growth concerns projects under construction or in development. [S9] [S13] [S20]

#### Finding 2

**Claim**

CCS remains particularly relevant to industrial and built-environment emissions that may be difficult to eliminate through electrification or fuel switching, although the new built-environment review mainly concerns broader carbon-management strategies rather than demonstrated conventional CCS.

**Confidence:** Medium

**Why this confidence level**

S21 is a recent peer-reviewed review and supports the importance of construction-related emissions, but its abstract does not establish the effectiveness, cost, or scalability of conventional CCS in those sectors.

**Evidence**

- The review identifies the built environment as responsible for approximately 40% of global energy and CO₂ emissions and discusses capture, storage, mineral carbonation, alternative binders, and carbon-absorbing construction materials. [S21]
- Existing evidence specifically identifies cement and other process-emission sectors as important potential applications for geological CCS. [S2] [S5] [S15]

#### Finding 3

**Claim**

Claims that CCS can capture more than 90% of emissions at facilities are technically plausible as capture-performance claims, but they do not demonstrate equivalent net or lifecycle emissions reductions and should not be treated as evidence of global effectiveness.

**Confidence:** Medium

**Why this confidence level**

S24 is an advocacy source and does not provide a standardized lifecycle boundary, measured fleet-wide capture rate, availability, or permanent-storage result.

**Evidence**

- C2ES states that carbon-capture technologies can capture more than 90% of CO₂ emissions from power and industrial facilities and lists commercial applications in several industrial processes. [S24]
- The accumulated evidence reports energy requirements, project underperformance, uncertain lifecycle benefits, and a large gap between nameplate capacity and actual global impact. [S1] [S9] [S13]

#### Finding 4

**Claim**

CCS deployment has a long operating history in certain concentrated sources, but the new sources do not resolve the key question of how much CO₂ is currently captured and permanently stored in practice.

**Confidence:** Medium

**Why this confidence level**

The historical examples establish operational experience, but the figures are dated and do not provide a standardized current global performance total.

**Evidence**

- C2ES describes historical projects including natural-gas processing, fertilizer, coal gasification, ethanol, refinery hydrogen, and power applications, and reports more than 16.5 million tonnes injected at Sleipner by January 2017. [S24]
- The existing evidence contains conflicting current operating-capacity estimates and emphasizes that project counts and nameplate capacity are not equivalent to actual annual permanent storage. [S9] [S14] [S16] [S20]

#### Finding 5

**Claim**

Economic viability remains policy-dependent; the new source’s incentives illustrate support mechanisms rather than proof of cost competitiveness.

**Confidence:** High

**Why this confidence level**

The incentive figures are directly reported, and they reinforce rather than contradict the established conclusion that policy support is important; they do not establish unsubsidized economics.

**Evidence**

- C2ES reports US 45Q incentives of up to $85 per tonne for industrial and power-facility saline storage and $180 per tonne for direct-air-capture saline storage, alongside reduced eligibility thresholds and direct-pay provisions. [S24]
- Existing sources report broad and high cost ranges, end-to-end European costs above some carbon prices, and recurring project cost overruns. [S1] [S7] [S14] [S15]

### Conflicts Found

- C2ES presents CCS as capable of more than 90% capture and as essential or nearly indispensable for deep industrial decarbonization, while the accumulated evidence supports a narrower, conditional role and highlights limited current scale, energy penalties, cost uncertainty, and underperformance. This is primarily a disagreement about system-wide indispensability, not necessarily about whether high facility-level capture rates are technically achievable. [S24] [S1] [S2] [S5]
- C2ES reports 30 operating commercial-scale projects and 11 under construction, whereas newer industry sources report 77 operating projects and 47 under construction. The discrepancy likely reflects different dates and inclusion criteria; the older source should not be used for current project counts. [S24] [S6] [S20]
- S21 emphasizes carbon uptake and storage in construction materials and broader built-environment strategies, whereas the original question concerns CCS as a global emissions-reduction technology. These approaches are related but not equivalent, so S21 cannot be used to infer conventional CCS performance. [S21]

### Important Gaps

- What is the independently verified current annual quantity of CO₂ actually captured and permanently stored, rather than nameplate capacity or cumulative industry claims?
- What are standardized measured capture rates, availability, energy penalties, lifecycle emissions, and net-abatement results for representative operating projects?
- How much operating and planned capacity involves dedicated permanent storage, CO₂-EOR or other utilization, fossil-fuel processing, BECCS, or direct-air capture?
- How much announced capacity will reach operation, and what practical limits arise from storage characterization, transport, permitting, public acceptance, monitoring, and liability?
- How do CCS costs and energy requirements compare with electrification, efficiency, renewable hydrogen, and other alternatives using consistent sector-specific system boundaries?

**Analysis Duration:** 14.63s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The overall conclusion is already responsible, but the most important empirical part of the question—demonstrated effectiveness—still lacks standardized primary data on actual stored tonnes, availability, capture rates, energy penalties, and net lifecycle abatement. The new sources mostly add advocacy, historical, or broad review material rather than resolving that gap.

**Next Search**

> primary data operating CCS projects actual CO2 captured permanently stored annual capture rate availability energy penalty lifecycle emissions cement power gas processing 2024 2025

---

# Iteration 7

## 1. Search

**Query**

> primary data operating CCS projects actual CO2 captured permanently stored annual capture rate availability energy penalty lifecycle emissions cement power gas processing 2024 2025

**Why this query**

The overall conclusion is already responsible, but the most important empirical part of the question—demonstrated effectiveness—still lacks standardized primary data on actual stored tonnes, availability, capture rates, energy penalties, and net lifecycle abatement. The new sources mostly add advocacy, historical, or broad review material rather than resolving that gap.

**Results**

5 results retrieved.

2 new unique sources added.

### Sources

- **S25 — Carbon Capture and Sequestration (CCS) in the United ...**
  URL: https://www.everycrsreport.com/reports/R44902.html
- **S26 — Carbon capture and storage: What can we learn from the project track record? – Clean Air Task Force**
  URL: https://www.catf.us/resource/carbon-capture-storage-what-can-learn-from-project-track-record

**Search Duration:** 2.47s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

CCS has demonstrated that capture, transport, and geological storage can operate at large scale in selected projects, but its record is uneven and does not yet establish reliable, climate-relevant performance across the global project fleet.

**Confidence:** High

**Why this confidence level**

The new source adds concrete project-level evidence of both successful operation and limitations, consistent with the broader evidence that current global impact remains small.

**Evidence**

- A review of 13 significant projects reports that Sleipner, the Alberta Carbon Trunk Line, and Quest consistently achieved high technical performance, while also documenting operational challenges and varying project motivations. [S26]
- The same review says many large-scale projects were developed primarily for commercial purposes, technology demonstration, or experience-building rather than to maximize climate benefits, and calls for more transparent performance reporting. [S26]
- The accumulated evidence finds current operating capacity to be only about 51–63.9 MtCO₂ per year, roughly 0.16% of global energy and industrial-process emissions under one estimate. [S9] [S16]

#### Finding 2

**Claim**

CCS is most defensible in concentrated, hard-to-abate industrial sources and some durable-removal pathways, rather than as a universal substitute for electrification, efficiency, or renewable energy.

**Confidence:** Medium

**Why this confidence level**

The sectoral rationale is consistent across sources, but the evidence does not quantify the maximum global contribution achievable specifically in these sectors.

**Evidence**

- The project-track-record review identifies cement, steel, petrochemicals, and other diverse industrial applications as increasingly important but generally more costly than historically dominant high-purity CO₂ sources. [S26]
- IEA and EU sources identify process emissions, existing assets, low-carbon hydrogen, BECCS, and direct-air-capture storage as potential roles for CCUS. [S2] [S5]
- The accumulated scenario evidence indicates that CCUS contributes a relatively small share of total modeled emissions reductions compared with renewables, electrification, fuel switching, and efficiency, although the precise 4.9% figure is not independently verified from the primary WEO excerpt. [S7] [S12]

#### Finding 3

**Claim**

Large-scale deployment remains economically and institutionally difficult, especially when CCS is used for dedicated permanent storage rather than revenue-generating CO₂ utilization.

**Confidence:** High

**Why this confidence level**

Multiple sources, including a government research service and project review, consistently identify cost and policy dependence as central constraints.

**Evidence**

- The review explains that climate-oriented storage in saline aquifers is effectively a waste-disposal activity that adds cost, while transport becomes more complex when sources are distant from storage sites. [S26]
- The Congressional Research Service reports broad agreement that construction and operating costs would need to decline before widespread deployment, and describes substantial U.S. public funding and tax incentives supporting CCS and DAC. [S25]
- Existing evidence reports indicative costs of $50–600 per tonne, European end-to-end costs of €105–280 per tonne, and recurring project cost overruns. [S1] [S7] [S14]

#### Finding 4

**Claim**

CCS requires substantial infrastructure and energy inputs, and its net climate benefit depends on capture performance, energy sources, transport, storage permanence, and whether captured CO₂ is utilized for enhanced oil recovery.

**Confidence:** Medium

**Why this confidence level**

The direction of the energy, infrastructure, and utilization concerns is well supported, but the retrieved sources do not provide standardized lifecycle energy or net-abatement measurements across projects.

**Evidence**

- The prior review estimates energy demand of approximately 2.5–8 GJ per tonne of CO₂ and identifies infrastructure requirements and possible reductions in net emissions benefits. [S1]
- The project review states that climate-oriented deployment will increasingly involve saline-aquifer storage and more complex transport networks, unlike historical CO₂ use associated with oil production. [S26]
- The CRS reports that most U.S. projects historically used CO₂ for EOR, while others aimed at dedicated geological sequestration, showing that capture does not by itself establish permanent atmospheric removal. [S25]

#### Finding 5

**Claim**

The main arguments against broad CCS deployment are high cost, energy use, uncertain or inconsistent project performance, storage and liability concerns, and the risk of delaying alternative mitigation options; the main arguments in favor are industrial residual emissions, existing-asset emissions, and durable removals.

**Confidence:** High

**Why this confidence level**

The new CRS and project-track-record evidence provide a balanced account of the central pro and con arguments, while the accumulated review supplies the broader systemic criticisms.

**Evidence**

- The CRS describes proponents’ view that CCS is important for mitigation and opponents’ concerns about continued fossil-fuel combustion and long-term underground-storage uncertainty. [S25]
- The critical review highlights cost, energy demand, project underperformance, geological uncertainty, liability, and opportunity costs. [S1]
- The CATF review argues that high-performing projects demonstrate an achievable standard, but that performance should be improved and transparently reported as deployment expands. [S26]

### Conflicts Found

- CATF emphasizes that several projects have consistently achieved high technical performance and that learning and policy can improve future projects, whereas the critical review emphasizes recurring underperformance, high costs, and the gap between modeled expectations and delivered scale. These positions are not wholly incompatible: technically successful projects exist, but they do not demonstrate fleet-wide or economy-wide effectiveness. [S1] [S26]
- The CRS notes that most U.S. projects use captured CO₂ for EOR, while climate-focused assessments emphasize dedicated geological storage and durable removals. This creates a conditional disagreement over whether historical CCS experience should count as climate mitigation, since utilization and oil-production effects may differ from permanent dedicated storage. [S25] [S26] [S5]
- The new CATF source identifies 41 large-scale operating commercial projects, while newer sources report 77 operating projects. The discrepancy likely reflects different dates and inclusion criteria; it does not establish a substantive disagreement about the existence of a growing but still small deployment base. [S6] [S20] [S26]

### Important Gaps

- What proportion of current nameplate capacity is actually captured and permanently stored annually, rather than merely available, utilized, or associated with EOR?
- What are standardized measured capture rates, availability, energy penalties, lifecycle emissions, and net-abatement outcomes for representative operating projects?
- How much projected capacity will reach operation, and what share will involve dedicated storage, EOR, BECCS, or direct-air capture?
- How do CCS costs and energy requirements compare with electrification, efficiency, and renewable hydrogen on consistent sector-specific lifecycle boundaries?
- How much practical geological storage is available after site characterization, transport, permitting, monitoring, public acceptance, and liability constraints?
- Does the primary IEA World Energy Outlook 2025 text substantiate and define the cited 4.9% CCUS contribution to emissions reductions?

**Analysis Duration:** 16.47s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new source materially improves the assessment of demonstrated project performance and supports a balanced conclusion: CCS works in some projects and applications but remains small, costly, policy-dependent, and insufficiently documented at fleet scale. The remaining gaps concern detailed benchmarking rather than information necessary to answer the original question responsibly.

**Next Search**

> Can carbon capture and storage make a significant contribution to reducing global CO₂ emissions? Evaluate its demonstrated effectiveness, costs, scalability, energy requirements, and major arguments for and against large-scale deployment. additional evidence search 8

---

# Iteration 8

## 1. Search

**Query**

> Can carbon capture and storage make a significant contribution to reducing global CO₂ emissions? Evaluate its demonstrated effectiveness, costs, scalability, energy requirements, and major arguments for and against large-scale deployment. additional evidence search 8

**Why this query**

The new source materially improves the assessment of demonstrated project performance and supports a balanced conclusion: CCS works in some projects and applications but remains small, costly, policy-dependent, and insufficiently documented at fleet scale. The remaining gaps concern detailed benchmarking rather than information necessary to answer the original question responsibly.

**Results**

5 results retrieved.

0 new unique sources added.

### Sources

No new unique sources were added.

**Search Duration:** 3.01s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

CCS can make a significant contribution in selected applications, but current evidence does not support it as the dominant economy-wide emissions-reduction strategy.

**Confidence:** High

**Why this confidence level**

The selective-role conclusion is consistent across strategic, project-tracking, and critical sources. The precise maximum global contribution remains uncertain.

**Evidence**

- IEA and EU sources identify hard-to-abate industrial process emissions, existing assets, low-carbon hydrogen, BECCS, and direct-air-capture storage as key potential roles. [S2] [S5]
- Current operating capacity is only a small fraction of global emissions, while most reported growth concerns projects under construction or development. [S9] [S13] [S20]
- The available interpretation of the IEA net-zero scenario assigns CCUS a relatively small share of total modeled reductions, although the precise 4.9% figure is not verified in the retrieved primary WEO excerpt. [S7] [S12]

#### Finding 2

**Claim**

CCS has demonstrated technical feasibility at individual projects, but not consistently reliable, climate-relevant performance across the global fleet.

**Confidence:** High

**Why this confidence level**

The evidence directly supports both successful project operation and uneven performance, while the absence of standardized fleet-wide data is explicit.

**Evidence**

- Sleipner, Quest, and the Alberta Carbon Trunk Line are reported to have achieved high technical performance, demonstrating that capture, transport, and geological storage can work at substantial scale. [S26]
- Other projects have experienced suboptimal capture, cost overruns, operational problems, or storage-integrity concerns; In Salah suspended injection after concerns about seal integrity and CO₂ movement, although no leakage was reported during operation. [S1] [S17] [S26]
- Available sources do not provide a standardized, independently verified global total for actual annual capture and permanent storage, fleet-wide availability, or lifecycle net abatement. [S9] [S13] [S16] [S20]

#### Finding 3

**Claim**

The present global climate contribution of CCS is very small relative to total emissions, despite substantial growth in projects and planned capacity.

**Confidence:** High

**Why this confidence level**

Although current-capacity estimates differ because of definitions and dates, all support the same conclusion: delivered capacity is small and far below pipeline capacity.

**Evidence**

- One estimate places operational capacity at approximately 51 MtCO₂ per year compared with 37,600 MtCO₂ per year of energy and industrial-process emissions, or roughly 0.16%. [S9]
- Other sources report approximately 63.9 Mtpa of operating commercial capture capacity, while the Global CCS Institute reports 513 Mtpa across operating and developmental projects. [S16] [S20]
- The IEA project database includes commissioned, under-construction, and planned projects, so pipeline capacity cannot be equated with actual captured or permanently stored CO₂. [S13]

#### Finding 4

**Claim**

CCS costs are high, uncertain, and strongly dependent on the CO₂ source, system boundary, infrastructure, financing, and policy support.

**Confidence:** High

**Why this confidence level**

Multiple sources, including a government research service, consistently identify cost and policy dependence as central constraints. Exact figures are not directly comparable across technologies and system boundaries.

**Evidence**

- The retrieved review gives an indicative cost range of $50–600 per tonne of CO₂ and cites recurring cost overruns. [S1]
- An EU estimate gives end-to-end disposal costs of approximately €105–280 per tonne, with the lower bound exceeding the cited average 2025 EU ETS price. [S7]
- US tax incentives of up to $85 per tonne for some permanent-storage projects and $180 per tonne for DAC storage illustrate the importance of public support rather than unsubsidized cost competitiveness. [S24]
- A government research service reports that construction and operating costs would need to fall for widespread deployment and describes substantial public funding and tax incentives. [S25]

#### Finding 5

**Claim**

CCS has substantial energy and infrastructure requirements that can reduce its net emissions benefit.

**Confidence:** Medium

**Why this confidence level**

The direction and approximate energy burden are supported, but standardized lifecycle measurements across sectors and projects are unavailable in the retrieved material.

**Evidence**

- The review estimates energy demand of approximately 2.5–8 GJ per tonne of CO₂ and warns that this can reduce net emissions benefits. [S1]
- Large-scale deployment requires coordinated capture, transport, storage, monitoring, and cross-border infrastructure, particularly when sources are distant from storage sites. [S5] [S26]
- Net climate performance depends on the energy source, capture rate, transport, storage permanence, and whether CO₂ is used for enhanced oil recovery or dedicated storage. [S1] [S25] [S26]

#### Finding 6

**Claim**

The strongest arguments for CCS concern emissions that are difficult to eliminate by electrification or fuel switching and the need for durable carbon removals.

**Confidence:** High

**Why this confidence level**

The sectoral rationale and specific technical roles are consistently identified by strategic and project-focused sources, though their aggregate potential is not quantified here.

**Evidence**

- Cement and lime process emissions are identified as intrinsically difficult to eliminate through conventional fuel switching or electrification. [S2] [S5] [S15]
- CCUS can potentially address residual emissions from existing industrial assets, support low-carbon hydrogen, and provide geological storage for BECCS or direct-air-capture removals. [S2] [S5]
- High-performing projects demonstrate that the underlying technologies are technically achievable, with scope for learning and improved reporting. [S26]

#### Finding 7

**Claim**

The strongest arguments against broad CCS deployment are its cost, energy use, uneven record, storage and liability uncertainties, and possible diversion of investment from more effective alternatives.

**Confidence:** High

**Why this confidence level**

The principal arguments are supported by multiple sources and are compatible with the observed gap between project pipelines and delivered climate impact.

**Evidence**

- Critical reviews identify high cost, energy demand, project underperformance, geological uncertainty, long-term liability, and opportunity costs. [S1]
- The CRS records concerns that CCS can prolong fossil-fuel combustion and that long-term underground storage remains uncertain, while noting proponents’ claims about its mitigation value. [S25]
- Scenario evidence assigns most modeled emissions reductions to renewables, electrification, fuel switching, and efficiency rather than CCUS, though the exact cited share is not independently verified. [S7] [S12]

### Conflicts Found

- Industry and strategic sources describe CCS as essential or on a path toward very large-scale deployment, while critical and scenario-based sources view it as a limited, conditional contributor. This is partly a disagreement about whether the benchmark is economy-wide mitigation or hard-to-abate residual emissions. [S1] [S2] [S5] [S7] [S20]
- Reported current operating capacity ranges from approximately 51 to 63.9 Mtpa, and project counts vary substantially. The differences likely reflect dates, thresholds, and whether sources report capture capacity, storage capacity, commercial facilities, or broader project categories. [S6] [S9] [S16] [S20] [S24]
- Historical CCS experience includes CO₂ utilization for enhanced oil recovery, whereas climate assessments emphasize dedicated permanent storage and durable removals. These applications are not equivalent in terms of net atmospheric removal. [S25] [S26]
- Several projects have achieved high technical performance, but this does not resolve the broader evidence of cost overruns, uneven operation, and limited delivered global capacity. [S1] [S26]

### Important Gaps

- What is the independently verified current annual quantity of CO₂ actually captured and permanently stored, rather than nameplate capacity?
- What are standardized measured capture rates, availability, energy penalties, lifecycle emissions, and net-abatement results for representative projects?
- How much of current and planned capacity involves dedicated permanent storage, CO₂-EOR, fossil-fuel processing, BECCS, or direct-air capture?
- What proportion of announced capacity will reach operation, given cost, permitting, infrastructure, storage characterization, public-acceptance, and liability constraints?
- How do CCS costs and energy requirements compare with electrification, efficiency, and renewable hydrogen using consistent sector-specific lifecycle boundaries?
- Does the primary IEA World Energy Outlook 2025 text substantiate and define the cited 4.9% CCUS contribution to emissions reductions?

**Analysis Duration:** 18.19s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The evidence is sufficient for a responsible conditional answer: CCS is technically demonstrated and potentially important in hard-to-abate sectors and durable-removal pathways, but current delivered scale is small, costs and energy requirements are substantial, and fleet-wide net-abatement performance is insufficiently standardized. Further searching would be useful for quantitative project-performance details, but no usable new sources were retrieved and those gaps do not overturn the central conclusion.

**Next Search**

> Can carbon capture and storage make a significant contribution to reducing global CO₂ emissions? Evaluate its demonstrated effectiveness, costs, scalability, energy requirements, and major arguments for and against large-scale deployment. additional evidence search 9

---

# Iteration 9

## 1. Search

**Query**

> Can carbon capture and storage make a significant contribution to reducing global CO₂ emissions? Evaluate its demonstrated effectiveness, costs, scalability, energy requirements, and major arguments for and against large-scale deployment. additional evidence search 9

**Why this query**

The evidence is sufficient for a responsible conditional answer: CCS is technically demonstrated and potentially important in hard-to-abate sectors and durable-removal pathways, but current delivered scale is small, costs and energy requirements are substantial, and fleet-wide net-abatement performance is insufficiently standardized. Further searching would be useful for quantitative project-performance details, but no usable new sources were retrieved and those gaps do not overturn the central conclusion.

**Results**

5 results retrieved.

0 new unique sources added.

### Sources

No new unique sources were added.

**Search Duration:** 2.85s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

CCS can make a significant contribution to global emissions reduction, but primarily as a selective technology for hard-to-abate industrial process emissions and durable carbon removals, not as the dominant economy-wide mitigation strategy.

**Confidence:** High

**Why this confidence level**

The selective-role conclusion is consistent across strategic, critical, project-focused, and scenario-related sources, even though the maximum achievable contribution is not quantified.

**Evidence**

- IEA and EU sources identify cement and other process emissions, existing industrial assets, low-carbon hydrogen, BECCS, and direct-air-capture storage as potential roles for CCUS. [S2] [S5]
- Scenario evidence indicates that most modeled emissions reductions come from renewables, electrification, fuel switching, and efficiency rather than CCUS, although the precise 4.9% figure attributed to CCUS is not verified by the retrieved primary WEO excerpt. [S7] [S12]

#### Finding 2

**Claim**

CCS is technically feasible at individual facilities, but demonstrated fleet-wide effectiveness and net climate impact remain uncertain.

**Confidence:** High

**Why this confidence level**

The evidence directly establishes both successful projects and important limitations, while the absence of standardized global performance data is explicit.

**Evidence**

- Sleipner, Quest, and the Alberta Carbon Trunk Line are reported to have achieved high technical performance, demonstrating that capture, transport, and geological storage can work at substantial scale. [S26]
- Other projects experienced suboptimal capture, cost overruns, operational problems, or storage-integrity concerns; In Salah suspended injection over seal-integrity and CO₂-movement concerns, although no leakage was reported during operation. [S1] [S17] [S26]
- The retrieved sources do not provide a standardized, independently verified global total for actual annual capture and permanent storage, fleet-wide availability, lifecycle emissions, or net abatement. [S9] [S13] [S16] [S20]

#### Finding 3

**Claim**

The current global climate contribution of CCS is very small compared with total emissions, despite rapid growth in project counts and planned capacity.

**Confidence:** High

**Why this confidence level**

Reported operating totals differ because of dates and definitions, but all support the same conclusion that delivered capacity is small and far below the development pipeline.

**Evidence**

- One estimate places operational capacity at approximately 51 MtCO₂ per year against 37,600 MtCO₂ per year of energy and industrial-process emissions, or about 0.16%. [S9]
- Other sources report approximately 63.9 Mtpa of operating commercial capture capacity, while the Global CCS Institute reports 513 Mtpa across operating and developmental projects. [S16] [S20]
- The IEA database includes commissioned, under-construction, and planned projects, so pipeline capacity cannot be equated with captured or permanently stored CO₂. [S13]

#### Finding 4

**Claim**

CCS costs are high, uncertain, and strongly dependent on the source of CO₂, system boundaries, infrastructure, financing, and policy support.

**Confidence:** High

**Why this confidence level**

Multiple sources, including a government research service, consistently identify cost and policy dependence as central constraints; exact figures are not directly comparable.

**Evidence**

- The retrieved review gives an indicative cost range of $50–600 per tonne of CO₂ and cites recurring project cost overruns. [S1]
- An EU estimate gives end-to-end disposal costs of approximately €105–280 per tonne, with the lower bound exceeding the cited average 2025 EU ETS price. [S7]
- US incentives of up to $85 per tonne for some permanent-storage projects and $180 per tonne for DAC storage illustrate the importance of public support rather than unsubsidized cost competitiveness. [S24]
- The Congressional Research Service reports that construction and operating costs would need to decline for widespread deployment and describes substantial public funding and tax incentives. [S25]

#### Finding 5

**Claim**

CCS imposes substantial energy and infrastructure requirements, so its net benefit depends on capture performance, the energy source, transport, storage permanence, and utilization pathway.

**Confidence:** Medium

**Why this confidence level**

The energy burden and infrastructure needs are supported, but standardized lifecycle comparisons across sectors and projects are unavailable.

**Evidence**

- The review estimates energy demand of approximately 2.5–8 GJ per tonne of CO₂ and warns that this can reduce net emissions benefits. [S1]
- Large-scale deployment requires coordinated capture, transport, storage, monitoring, and often cross-border infrastructure, especially when sources are distant from storage sites. [S5] [S26]
- Historical CO₂ use for enhanced oil recovery is not equivalent to dedicated permanent storage or durable atmospheric removal. [S25] [S26]

#### Finding 6

**Claim**

The strongest arguments for large-scale CCS concern emissions that are difficult to eliminate through electrification or fuel switching and the need to store carbon removed from the atmosphere.

**Confidence:** High

**Why this confidence level**

The sectoral rationale and technical roles are consistently identified across strategic and project-focused sources.

**Evidence**

- Cement and lime process emissions are identified as intrinsically difficult to eliminate through conventional fuel switching or electrification. [S2] [S5] [S15]
- CCUS may address residual emissions from existing assets, support low-carbon hydrogen, and provide geological storage for BECCS or direct-air-capture removals. [S2] [S5]
- High-performing projects show that the underlying capture, transport, and storage technologies are achievable. [S26]

#### Finding 7

**Claim**

The strongest arguments against indiscriminate deployment are high cost, energy use, uneven operating performance, storage and liability uncertainties, and the risk of diverting investment from alternatives such as efficiency, electrification, and renewable energy.

**Confidence:** High

**Why this confidence level**

The principal objections are supported by multiple sources and align with the observed gap between project pipelines and delivered climate impact.

**Evidence**

- Critical reviews identify cost, energy demand, project underperformance, geological uncertainty, long-term liability, and opportunity costs. [S1]
- The CRS records concerns that CCS may prolong fossil-fuel combustion and that long-term underground storage remains uncertain, while also presenting proponents’ mitigation arguments. [S25]
- Scenario evidence assigns most modeled reductions to alternatives rather than CCUS, although the exact percentage attributed to CCUS is not independently verified. [S7] [S12]

### Conflicts Found

- Strategic and industry sources describe CCS as important, essential, or capable of reaching very large scale, while critical and scenario-based sources view it as a limited and conditional contributor. The disagreement largely concerns the benchmark: economy-wide mitigation versus hard-to-abate residual emissions. [S1] [S2] [S5] [S7] [S20]
- Several high-performing projects demonstrate technical feasibility, but this does not resolve evidence of cost overruns, uneven operation, and limited delivered global capacity. The positions are therefore conditional rather than mutually exclusive. [S1] [S26]
- Reported operating capacity ranges from approximately 51 to 63.9 Mtpa, and project counts also vary. These differences likely reflect dates, thresholds, and whether sources count capture capacity, storage capacity, commercial facilities, or broader project categories. [S6] [S9] [S16] [S20] [S24]
- Historical CCS experience includes CO₂ utilization for enhanced oil recovery, whereas climate-focused assessments emphasize dedicated permanent storage and durable removals. These pathways are not equivalent in terms of net atmospheric removal. [S25] [S26]
- The 4.9% CCUS contribution attributed to the IEA net-zero scenario is reported by a secondary interpretation, but the retrieved primary WEO page does not contain or define that figure. [S7] [S12]

### Important Gaps

- What is the independently verified current annual quantity of CO₂ actually captured and permanently stored, rather than nameplate capacity?
- What are standardized measured capture rates, availability, energy penalties, lifecycle emissions, and net-abatement results for representative operating projects?
- How much current and planned capacity involves dedicated permanent storage, CO₂-EOR or other utilization, fossil-fuel processing, BECCS, or direct-air capture?
- What proportion of announced capacity will reach operation given cost, permitting, transport, storage characterization, public acceptance, and liability constraints?
- How do CCS costs and energy requirements compare with electrification, efficiency, and renewable hydrogen using consistent sector-specific lifecycle boundaries?
- Does the primary IEA World Energy Outlook 2025 text substantiate and define the cited 4.9% contribution of CCUS to emissions reductions?

**Analysis Duration:** 16.67s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The accumulated evidence is sufficient for a responsible conditional answer, but an important part of the question—demonstrated effectiveness—still lacks independently verified, standardized operating data on actual permanent storage, availability, lifecycle emissions, and net abatement. A focused search could materially improve the assessment, provided it finds primary project-level or audited fleet-level data rather than additional project-pipeline claims.

**Next Search**

> site:iea.org OR site:globalccsinstitute.com measured CCS project capture rate availability actual CO2 stored lifecycle emissions Quest Sleipner Boundary Dam Gorgon 2024 2025

---

# Iteration 10

## 1. Search

**Query**

> site:iea.org OR site:globalccsinstitute.com measured CCS project capture rate availability actual CO2 stored lifecycle emissions Quest Sleipner Boundary Dam Gorgon 2024 2025

**Why this query**

The accumulated evidence is sufficient for a responsible conditional answer, but an important part of the question—demonstrated effectiveness—still lacks independently verified, standardized operating data on actual permanent storage, availability, lifecycle emissions, and net abatement. A focused search could materially improve the assessment, provided it finds primary project-level or audited fleet-level data rather than additional project-pipeline claims.

**Results**

0 results retrieved.

0 new unique sources added.

### Sources

No new unique sources were added.

**Search Duration:** 2.74s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

CCS can make a significant contribution, but mainly in hard-to-abate sectors and durable carbon-removal pathways rather than as the dominant economy-wide mitigation strategy.

**Confidence:** High

**Why this confidence level**

The selective-role conclusion is consistent across strategic, critical, project-focused, and scenario-related sources, even though the maximum achievable contribution is not quantified.

**Evidence**

- IEA and EU sources identify process emissions, existing industrial assets, low-carbon hydrogen, BECCS, and direct-air-capture storage as the main potential roles for CCUS. [S2] [S5]
- Scenario-related evidence indicates that renewables, electrification, fuel switching, and efficiency provide most modeled emissions reductions, although the precise 4.9% CCUS figure is not verified in the retrieved primary WEO material. [S7] [S12]

#### Finding 2

**Claim**

CCS is technically feasible at individual facilities, but demonstrated fleet-wide effectiveness and net climate impact remain uncertain.

**Confidence:** High

**Why this confidence level**

The sources directly establish both successful projects and significant limitations, while the absence of standardized fleet-wide performance data is explicit.

**Evidence**

- Sleipner, Quest, and the Alberta Carbon Trunk Line reportedly achieved high technical performance, demonstrating that capture, transport, and geological storage can operate at substantial scale. [S26]
- Other projects experienced suboptimal capture, cost overruns, operational difficulties, or storage-integrity concerns; In Salah suspended injection because of concerns about seal integrity and CO₂ movement, although no leakage was reported during operation. [S1] [S17] [S26]
- The retrieved evidence does not provide a standardized, independently verified global measure of actual annual capture, permanent storage, availability, lifecycle emissions, or net abatement. [S9] [S13] [S16] [S20]

#### Finding 3

**Claim**

Current delivered CCS capacity is very small relative to global emissions, despite rapid growth in project pipelines.

**Confidence:** High

**Why this confidence level**

Reported operating totals differ by date and definition, but all show that delivered capacity is small and far below announced or developmental capacity.

**Evidence**

- One estimate places operational capacity at approximately 51 MtCO₂ per year against 37,600 MtCO₂ per year of energy and industrial-process emissions, or about 0.16%. [S9]
- Other sources report approximately 63.9 Mtpa of operating commercial capture capacity and 513 Mtpa across operating and developmental projects. [S16] [S20]
- The IEA database includes commissioned, under-construction, and planned projects, so pipeline capacity is not equivalent to captured or permanently stored CO₂. [S13]

#### Finding 4

**Claim**

CCS costs are high, uncertain, and strongly dependent on the CO₂ source, system boundary, infrastructure, financing, and policy support.

**Confidence:** High

**Why this confidence level**

Multiple sources, including a government research service, consistently identify cost and policy dependence as central constraints; exact figures are not directly comparable.

**Evidence**

- The retrieved review gives an indicative cost range of $50–600 per tonne of CO₂ and cites recurring project cost overruns. [S1]
- An EU estimate gives end-to-end disposal costs of approximately €105–280 per tonne. [S7]
- US incentives of up to $85 per tonne for some permanent-storage projects and $180 per tonne for DAC storage, together with CRS evidence of substantial public support, indicate strong policy dependence rather than demonstrated unsubsidized competitiveness. [S24] [S25]

#### Finding 5

**Claim**

CCS requires substantial energy and infrastructure inputs, which can reduce its net emissions benefit.

**Confidence:** Medium

**Why this confidence level**

The energy burden and infrastructure requirements are supported, but standardized lifecycle comparisons across sectors and projects are unavailable.

**Evidence**

- The review estimates energy demand of approximately 2.5–8 GJ per tonne of CO₂ and warns that this can reduce net emissions benefits. [S1]
- Large-scale deployment requires coordinated capture, transport, storage, monitoring, and sometimes cross-border infrastructure, especially where sources are distant from storage sites. [S5] [S26]
- Net climate performance depends on the energy source, capture rate, transport, storage permanence, and whether CO₂ is used for enhanced oil recovery or dedicated storage. [S1] [S25] [S26]

#### Finding 6

**Claim**

The main case for CCS is that it can address unavoidable industrial process emissions and provide storage for durable removals; the main case against broad deployment is cost, energy use, uneven performance, storage and liability uncertainty, and possible diversion from alternatives.

**Confidence:** High

**Why this confidence level**

The principal pro and con arguments are supported by multiple strategic, project-focused, critical, and government sources.

**Evidence**

- Cement and lime process emissions are identified as difficult to eliminate through fuel switching or electrification, while BECCS and DAC require durable geological storage. [S2] [S5] [S15]
- Critical and government sources identify high cost, energy demand, underperformance, geological uncertainty, long-term liability, possible fossil-fuel lock-in, and opportunity costs. [S1] [S25]
- Scenario evidence assigns most modeled reductions to alternatives such as renewables, electrification, fuel switching, and efficiency, though the exact CCUS share is not independently verified. [S7] [S12]

### Conflicts Found

- Strategic and industry sources describe CCS as important, essential, or capable of reaching very large scale, while critical and scenario-based sources view it as a limited and conditional contributor. The disagreement largely concerns the benchmark: hard-to-abate residual emissions versus economy-wide mitigation. [S1] [S2] [S5] [S7] [S20]
- Reported operating capacity ranges from approximately 51 to 63.9 Mtpa, while broader figures such as 513 Mtpa include developmental projects. These differences reflect dates, thresholds, and whether sources count capture capacity, storage capacity, commercial facilities, or planned projects. [S9] [S16] [S20]
- Historical CCS experience includes enhanced-oil-recovery utilization, whereas climate-focused assessments emphasize dedicated permanent storage and durable removals. These pathways are not equivalent in terms of net atmospheric removal. [S25] [S26]
- The cited 4.9% CCUS contribution to emissions reductions is reported by a secondary interpretation, but the retrieved primary WEO page does not contain or define the figure. [S7] [S12]

### Important Gaps

- What is the independently verified current annual quantity of CO₂ actually captured and permanently stored, rather than nameplate capacity?
- What are standardized measured capture rates, availability, energy penalties, lifecycle emissions, and net-abatement results for representative operating projects?
- How much of current and planned capacity involves dedicated permanent storage, CO₂-EOR, fossil-fuel processing, BECCS, or direct-air capture?
- What proportion of announced capacity will reach operation given cost, permitting, transport, storage-characterization, public-acceptance, and liability constraints?
- How do CCS costs and energy requirements compare with electrification, efficiency, and renewable hydrogen using consistent sector-specific lifecycle boundaries?
- Does the primary IEA World Energy Outlook 2025 text substantiate and define the cited 4.9% contribution of CCUS to emissions reductions?

**Analysis Duration:** 15.35s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The runner reached the maximum research iteration budget. Analyzer assessment: The retrieved evidence is sufficient to answer the original question responsibly: CCS is technically feasible and potentially important in selected applications, but current delivered scale is small, costs and energy requirements are substantial, and fleet-wide net-abatement performance is not adequately demonstrated. Further searches would mainly refine unresolved numerical details, and repeated searches have not produced usable primary evidence. Those evidence gaps should be stated explicitly rather than filled with unsupported precision.

**Stop Reason:** max_iterations

---

# Final Research Decision

**Research Stopped Because**

The runner reached the maximum research iteration budget.

**Stop Reason:** max_iterations

**Searches Performed:** 10

**Unique Sources:** 26

**Remaining Uncertainty**

- The independently verified current annual quantity of CO₂ actually captured and permanently stored, rather than nameplate capacity, remains unresolved.
- Standardized measured capture rates, availability, energy penalties, lifecycle emissions, and net-abatement results for representative operating projects were not retrieved.
- The share of current and planned capacity involving dedicated permanent storage, CO₂-EOR, fossil-fuel processing, BECCS, or direct-air capture remains unclear.
- The proportion of announced capacity that will reach operation given cost, permitting, transport, storage-characterization, public-acceptance, and liability constraints remains uncertain.
- The evidence does not provide a consistent sector-specific lifecycle comparison between CCS and electrification, efficiency, renewable hydrogen, or other alternatives.
- The primary IEA World Energy Outlook 2025 text retrieved here does not substantiate or define the cited 4.9% contribution figure.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 10 | 27.94s |
| OpenAI Analysis | 10 | 163.42s |
| Report Generation | 1 | 18.07s |
| Total Run | — | 209.44s |
