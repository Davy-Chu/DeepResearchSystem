# Research Run Log

## Run Summary

**System Version:** evidence-ledger-decomposer-v1

**Research Question**

Can carbon capture and storage make a significant contribution to reducing global CO₂ emissions? Evaluate its demonstrated effectiveness, costs, scalability, energy requirements, and major arguments for and against large-scale deployment.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 14

**OpenAI Calls:** 7

**Tavily Calls:** 3

**Started:** 2026-08-31T18:10:16-04:00

**Ended:** 2026-08-31T18:11:53-04:00

**Total Runtime:** 96.99s

---

# Research Plan

## Subquestions

### SQ1 [CORE]

**Question:**

What reduction in CO₂ emissions has carbon capture and storage (CCS) actually demonstrated to date, across operating and historically completed projects, and how does this compare with the scale required for meaningful global emissions reductions?

**Success criteria:**

Use documented project-level and aggregate evidence on captured, transported, injected, and durably stored CO₂; distinguish nameplate capacity from actual performance, availability, capture rates, and permanence; compare demonstrated deployment with relevant global emissions and mitigation scales.

**Initial status:** UNRESEARCHED

### SQ2 [CORE]

**Question:**

What are the costs of CCS across major applications and how do they compare with alternative emissions-reduction options?

**Success criteria:**

Report cost ranges using clearly identified measures and system boundaries, distinguishing capture, transport, storage, and whole-system costs where possible; cover relevant sectors and explain major drivers, uncertainty, and comparisons with alternatives without implying a single universal cost.

**Initial status:** UNRESEARCHED

### SQ3 [CORE]

**Question:**

How scalable is CCS globally, considering geological storage availability, infrastructure, supply chains, project development, regulation, public acceptance, and deployment rates?

**Success criteria:**

Assess theoretical versus practically accessible storage, required build-out of capture, transport, and injection infrastructure, geographic and sectoral constraints, historical deployment rates, permitting and policy conditions, and bottlenecks that could limit or enable large-scale expansion.

**Initial status:** UNRESEARCHED

### SQ4 [CORE]

**Question:**

What energy requirements and associated emissions arise from CCS, and under what conditions could they materially reduce its net climate benefit?

**Success criteria:**

Explain energy penalties for capture, compression, transport, and storage; identify how energy sources affect additional fuel use and residual emissions; evaluate net lifecycle climate effects and conditions under which CCS delivers substantial versus limited or negative benefits.

**Initial status:** UNRESEARCHED

### SQ5 [CORE]

**Question:**

What are the strongest arguments for and against large-scale CCS deployment, including its potential roles in hard-to-abate sectors and carbon dioxide removal?

**Success criteria:**

Present evidence-based arguments on industrial process emissions, fossil-fuel power or hydrogen, bioenergy with CCS, direct air capture, residual emissions, mitigation timing, and energy-system integration; address counterarguments involving cost, lock-in, leakage, delayed decarbonization, environmental impacts, and opportunity costs.

**Initial status:** UNRESEARCHED

## Synthesis Requirements

- Integrate demonstrated effectiveness, costs, scalability, energy requirements, and deployment arguments into an overall judgment about whether CCS can make a significant contribution to reducing global CO₂ emissions.
- Distinguish potential contribution from demonstrated contribution, and distinguish gross captured CO₂ from net, additional, and durably stored emissions reductions.
- Compare CCS across applications rather than treating it as a single uniform technology, and identify where conclusions depend on sector, energy source, project design, and policy assumptions.
- Make uncertainty and the timeframe of evidence explicit, especially when extrapolating from current projects to future global deployment.

## Output Requirements

- Provide an evaluative answer to whether CCS can make a significant contribution to global CO₂ reductions.
- Cover demonstrated effectiveness, costs, scalability, energy requirements, and major arguments for and against large-scale deployment.
- Present a balanced assessment rather than a purely descriptive account, with conclusions qualified by evidence strength and relevant conditions.

---

# Iteration 1

## 1. Search

**Query**

> Can carbon capture and storage make a significant contribution to reducing global CO₂ emissions? Evaluate its demonstrated effectiveness, costs, scalability, energy requirements, and major arguments for and against large-scale deployment.

**Purpose:** GENERAL

**Why this query**

This is the user's original research question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S1 — Carbon capture and storage: An evidence-based review of ...**
  URL: https://www.sciencedirect.com/science/article/pii/S2096249525000973
- **S2 — Carbon Capture and Storage (CCS): The Future of Climate ...**
  URL: https://blog.verde.ag/en/carbon-capture-and-storage-ccs
- **S3 — Anticipating a potential deficit in global carbon capture ...**
  URL: https://www.nature.com/articles/s44432-025-00002-0
- **S4 — Carbon Capture**
  URL: https://www.c2es.org/content/carbon-capture
- **S5 — A Vision for Carbon Capture, Utilisation, and Storage in the ...**
  URL: https://www.catf.us/resource/a-vision-carbon-capture-utilisation-and-storage-eu

**Search Duration:** 2.86s

---

## 2. Evidence Processing

- New claim proposals: 7
- Existing claim updates: 0
- New gaps: 5
- Resolved gaps: 0

**Processing Duration:** 17.24s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

A 2025 review reports that CCS captures and stores less than 0.1% of annual global CO₂ emissions despite more than $40 billion in global investment, indicating that demonstrated aggregate deployment remains very small relative to global emissions.

- S1 supports (direct): The review abstract explicitly reports investment exceeding $40 billion and captured-and-stored emissions below 0.1% of annual global CO₂ emissions.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C2

**Claim**

Commercial-scale CCS has been demonstrated in several industrial applications, including natural-gas processing, fertilizer and ethanol production, coal gasification, refinery hydrogen, and at least one coal-power project; the supplied evidence also documents Sleipner injecting roughly 0.85 million tonnes of CO₂ annually and more than 16.5 million tonnes cumulatively by January 2017.

- S4 supports (direct): C2ES lists commercial operation across multiple industrial applications and reports Sleipner's annual and cumulative injection figures.
- S2 supports (indirect): The article identifies Sleipner and Petra Nova as large-scale projects and characterizes them as demonstrations of technical viability.
- S1 contradicts (indirect): The review argues that projects described as successful may fall short when assessed for durability, scale, and emissions-offset claims, and identifies suboptimal capture rates and geological uncertainties.

**Confidence:** MEDIUM

**Status:** CONFLICTING

### New Claim C3

**Claim**

CCS capture and storage costs vary substantially by application and system design; the supplied review gives a broad indicative range of $50–$600 per tonne of CO₂ and an energy-demand range of 2.5–8 GJ per tonne of CO₂.

- S1 supports (direct): The review's abstract specifies cost parameters of $50–$600/tCO₂ and energy demand of 2.5–8 GJ/tCO₂.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C4

**Claim**

CCS proponents identify hard-to-abate industrial process emissions, including cement, lime, chemicals, steel, and waste incineration, as important potential applications because some emissions arise intrinsically from industrial processes rather than only from fuel combustion.

- S5 supports (direct): The EU CCUS vision identifies cement, steel, chemical production, and waste incineration as hard-to-abate sectors and distinguishes unavoidable process emissions in cement, lime, and some chemicals.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C5

**Claim**

CCS is also proposed for carbon-dioxide removal through direct-air capture with storage and bioenergy with CCS; the supplied EU assessment states that its modelling indicates a need for at least 150 MtCO₂ per year of atmospheric or biogenic CO₂ capture and storage in the EU by 2050.

- S5 supports (direct): The report identifies DACS and BECCS as routes to permanent atmospheric carbon removal and gives the EU 2050 figure of at least 150 Mt/year.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C6

**Claim**

Large-scale CCS deployment faces substantial economic, infrastructure, policy, and coordination barriers; the supplied sources describe high implementation costs, cost barriers to economies of scale, dependence on policy support, and the need for cross-border capture, transport, utilization, and storage infrastructure.

- S1 supports (indirect): The review reports recurring cost overruns and characterizes CCS as high-cost, while noting scalability concerns.
- S3 supports (direct): The study reports that cost barriers significantly impede economies of scale and that CCUS development is strongly policy-driven, with a persistent projected deficit relative to climate targets.
- S5 supports (direct): The EU vision states that coordinated European action and cross-border infrastructure are needed to develop CCUS quickly and at the required scale.
- S2 supports (direct): The article identifies high implementation costs, storage-site availability, safety, and environmental impacts as challenges.
- S4 contradicts (indirect): C2ES presents policy incentives, multiple operating projects, and claimed potential for substantial global emissions reductions, implying that supportive policy could enable broader deployment.

**Confidence:** HIGH

**Status:** CONFLICTING

### New Claim C7

**Claim**

Supporters argue that CCS could contribute materially to decarbonization, with supplied sources citing modelled contributions of approximately 13% of required emissions reductions by 2060 or 14% of reductions needed by 2050, while opponents argue that reliance on CCS can delay more scalable alternatives and prolong fossil-fuel dependence.

- S2 supports (direct): The article cites an IEA-attributed estimate of up to 13% of required reductions by 2060 and presents CCS as enabling continued fossil-fuel use with lower emissions.
- S4 supports (direct): C2ES claims CCS could provide 14% of global greenhouse-gas reductions needed by 2050 and describes it as important for industrial deep decarbonization.
- S1 supports (direct): The review argues that continued reliance on CCS risks delaying alternatives and characterizes renewables, bio-based removals, and mineralization as potentially more scalable or permanent in some contexts.

**Confidence:** MEDIUM

**Status:** CONFLICTING

### New Gap G1

The evidence does not establish a consistent, independently verified global inventory of actual captured, transported, injected, and durably stored CO₂, nor does it systematically distinguish nameplate capacity, capture rate, availability, utilization, leakage, and net emissions reductions across operating and failed projects.

### New Gap G2

The supplied cost range lacks defined system boundaries and sector-specific breakdowns, and no directly comparable evidence is provided on CCS costs versus alternatives such as renewables, electrification, efficiency, or non-CCS industrial pathways.

### New Gap G3

The evidence does not quantify global geological storage capacity by theoretical, technically accessible, permitted, and practically developable categories, or specify the transport, injection, supply-chain, permitting, and public-acceptance requirements for a global build-out.

### New Gap G4

The supplied material gives an aggregate energy-demand range but does not separate capture, compression, transport, and storage penalties, identify fuel or electricity sources, or quantify lifecycle residual emissions and conditions under which net climate benefits become limited or negative.

### New Gap G5

The evidence does not adequately compare CCS applications, including fossil power, blue hydrogen, cement, BECCS, and direct-air capture, in terms of net emissions, permanence, environmental impacts, lock-in, opportunity costs, and demonstrated scalability.

---

## 4. Current Research State

- Claims: 7
- Supported: 4
- Weak: 0
- Conflicting: 3
- Insufficient Evidence: 0
- Open Gaps: 5
- Remaining Searches: 2

### Subquestion Progress

**SQ1:** UNRESEARCHED → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ2:** UNRESEARCHED → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ3:** UNRESEARCHED → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ4:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ5:** UNRESEARCHED → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

### Research Plan Status

**CORE:**

- SQ1 → CONFLICTING (targeted searches: 0)
- SQ2 → CONFLICTING (targeted searches: 0)
- SQ3 → CONFLICTING (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)
- SQ5 → CONFLICTING (targeted searches: 0)

**SECONDARY:**

- None

**Remaining targeted searches:** 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ1

**Why**

SQ1 is a CORE subquestion with conflicting evidence and the highest-value unresolved gap: the current record lacks an independently verified inventory distinguishing nameplate capacity from CO₂ actually captured, transported, injected, and durably stored. Resolving demonstrated performance is central to judging whether CCS can contribute significantly, and two searches remain.

**Next Search**

> Global CCS Institute 2024 status report: operating CCS projects actual captured CO2, annual injection, utilization, capture rates, project failures/cancellations, and comparison with global CO2 emissions; distinguish nameplate capacity from verified captured and permanently stored amounts.


---

# Iteration 2

## 1. Search

**Query**

> Global CCS Institute 2024 status report: operating CCS projects actual captured CO2, annual injection, utilization, capture rates, project failures/cancellations, and comparison with global CO2 emissions; distinguish nameplate capacity from verified captured and permanently stored amounts.

**Target:** SQ1

**Purpose:** SUBQUESTION

**Why this query**

SQ1 is a CORE subquestion with conflicting evidence and the highest-value unresolved gap: the current record lacks an independently verified inventory distinguishing nameplate capacity from CO₂ actually captured, transported, injected, and durably stored. Resolving demonstrated performance is central to judging whether CCS can contribute significantly, and two searches remain.

5 result(s) retrieved; 5 new unique source(s) added.

- **S6 — Previous Global Status of CCS Reports**
  URL: https://www.globalccsinstitute.com/previous-reports
- **S7 — Global Status Report**
  URL: https://www.globalccsinstitute.com/resources/global-status-report
- **S8 — Carbon Capture and Storage Capacity Worldwide**
  URL: https://incorrys.com/environmental-data/carbon-capture-and-storage/carbon-capture-and-storage-capacity-worldwide
- **S9 — Carbon capture and storage (CCS) - statistics & facts | Statista**
  URL: https://www.statista.com/topics/4101/carbon-capture-and-storage
- **S10 — Commercial Carbon Capture Plants: International Operating CCS Projects | CCS Knowledge Centre**
  URL: https://ccsknowledge.com/carbon-management-101/international-ccs-projects

**Search Duration:** 2.35s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 4
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 14.26s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

A 2025 review reports that CCS captures and stores less than 0.1% of annual global CO₂ emissions despite more than $40 billion in global investment, indicating that demonstrated aggregate deployment remains very small relative to global emissions.

- S9 supports (indirect): Statista reports that operational CCS captured well under 1% of global CO₂ emissions per year, consistent with the claim that demonstrated aggregate deployment remains very small.
- S8 supports (indirect): Incorrys estimates 51 MtCO₂/year of operational CCS capacity at the end of 2024 against 37,600 MtCO₂/year of energy and industrial emissions, or about 0.16% of emissions; this is capacity rather than verified actual storage and therefore provides scale context rather than a direct measure of realized reductions.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

Commercial-scale CCS has been demonstrated in several industrial applications, including natural-gas processing, fertilizer and ethanol production, coal gasification, refinery hydrogen, and at least one coal-power project; the supplied evidence also documents Sleipner injecting roughly 0.85 million tonnes of CO₂ annually and more than 16.5 million tonnes cumulatively by January 2017.

- S10 supports (direct): The CCS Knowledge Centre, using data recorded through July 2025, lists 46 operating commercial facilities above 100,000 tonnes per year across North and South America, Asia, Oceania, and Europe, with reported capture capacity totaling about 64.2 Mtpa; it identifies pre-combustion, post-combustion, and oxy-fuel facilities.
- S9 supports (direct): Statista reports operational capture capacity of around 64 MtCO₂/year in mid-2025, up from 28 MtCO₂/year in 2014, and states that natural-gas processing accounts for roughly 60% of operating capture capacity.
- S8 supports (direct): Incorrys reports 51 MtCO₂/year of global operational CCS capacity at the end of 2024 and describes growth from 33 MtCO₂/year in 2014 to just over 50 MtCO₂/year in 2023.

**Confidence:** MEDIUM → HIGH

**Status:** CONFLICTING → CONFLICTING

### Updated Claim C6

**Claim**

Large-scale CCS deployment faces substantial economic, infrastructure, policy, and coordination barriers; the supplied sources describe high implementation costs, cost barriers to economies of scale, dependence on policy support, and the need for cross-border capture, transport, utilization, and storage infrastructure.

- S9 supports (direct): Statista identifies high implementation cost as a major scaling barrier and reports an estimated need for roughly $500 billion per year of global CCS investment through 2030, compared with about $11 billion invested in 2023.
- S6 supports (direct): The Global CCS Institute states that CCS capture capacity is on track to exceed 100 Mtpa when facilities under construction operate, but emphasizes that substantially more work is urgently needed for gigatonne-scale deployment.
- S8 supports (indirect): Incorrys reports more than 50 MtCO₂/year under construction for 2025–2027, indicating a growing pipeline while also showing that near-term capacity remains far below gigatonne scale.
- S10 contradicts (indirect): The operating-project inventory documents a broader and larger commercial footprint than the earlier evidence, including about 64.2 Mtpa of capture capacity across 46 facilities, indicating that deployment momentum and existing infrastructure may be stronger than implied by a purely barrier-focused characterization.
- S9 contradicts (indirect): Statista reports more than 700 projects in the global pipeline and over 500 MtCO₂/year of capacity in development, suggesting significant expansion potential if projects proceed, although this is planned capacity rather than delivered deployment.

**Confidence:** HIGH → HIGH

**Status:** CONFLICTING → CONFLICTING

### Updated Claim C7

**Claim**

Supporters argue that CCS could contribute materially to decarbonization, with supplied sources citing modelled contributions of approximately 13% of required emissions reductions by 2060 or 14% of reductions needed by 2050, while opponents argue that reliance on CCS can delay more scalable alternatives and prolong fossil-fuel dependence.

- S6 supports (indirect): The Global CCS Institute describes year-on-year momentum and argues that CCS is beginning to scale, while explicitly noting that gigatonne-scale deployment has not yet been achieved.
- S9 supports (indirect): Statista identifies hard-to-abate sectors such as oil and gas, iron and steel, cement, and refining as potential applications, and reports a development pipeline exceeding 500 MtCO₂/year that could support larger future contributions.
- S8 contradicts (indirect): Even using the reported 2024 operational capacity of 51 MtCO₂/year, CCS represents only about 0.16% of global energy and industrial CO₂ emissions, underscoring the large gap between projected contribution and demonstrated deployment.
- S9 contradicts (direct): Statista characterizes CCS as still in its infancy and states that current capture remains well under 1% of global CO₂ emissions, limiting the evidentiary basis for treating modelled future contributions as demonstrated outcomes.

**Confidence:** MEDIUM → MEDIUM

**Status:** CONFLICTING → CONFLICTING

---

## 4. Current Research State

- Claims: 7
- Supported: 4
- Weak: 0
- Conflicting: 3
- Insufficient Evidence: 0
- Open Gaps: 5
- Remaining Searches: 1

### Subquestion Progress

**SQ1:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ2:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ3:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ4:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ5:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

### Research Plan Status

**CORE:**

- SQ1 → CONFLICTING (targeted searches: 1)
- SQ2 → CONFLICTING (targeted searches: 0)
- SQ3 → CONFLICTING (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)
- SQ5 → CONFLICTING (targeted searches: 0)

**SECONDARY:**

- None

**Remaining targeted searches:** 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ2

**Why**

SQ2 is a CORE subquestion with no targeted research yet, and its high-importance gap prevents a responsible evaluation of CCS economics: the current broad cost range lacks system boundaries, sector-specific detail, and comparisons with alternatives. One focused search could materially improve the answer.

**Next Search**

> Authoritative 2024–2025 sources on CCS costs by sector and component: capture, transport, storage, and whole-system costs for power, cement, steel, hydrogen, and DAC; include assumptions, cost per tonne, regional variation, and comparisons with renewables, electrification, efficiency, and non-CCS pathways.


---

# Iteration 3

## 1. Search

**Query**

> Authoritative 2024–2025 sources on CCS costs by sector and component: capture, transport, storage, and whole-system costs for power, cement, steel, hydrogen, and DAC; include assumptions, cost per tonne, regional variation, and comparisons with renewables, electrification, efficiency, and non-CCS pathways.

**Target:** SQ2

**Purpose:** SUBQUESTION

**Why this query**

SQ2 is a CORE subquestion with no targeted research yet, and its high-importance gap prevents a responsible evaluation of CCS economics: the current broad cost range lacks system boundaries, sector-specific detail, and comparisons with alternatives. One focused search could materially improve the answer.

5 result(s) retrieved; 4 new unique source(s) added.

- **S11 — [PDF] ADVANCEMENTS IN CCS TECHNOLOGIES AND COSTS**
  URL: https://www.globalccsinstitute.com/wp-content/uploads/2025/10/Advancements-in-CCS-Technologies-and-Costs-Report-2.pdf
- **S12 — Why CCUS Adoption Remains Slow Despite Massive Global Investment | Green Fuel Journal**
  URL: https://www.greenfueljournal.com/post/why-ccus-adoption-remains-slow-despite-massive-global-investment
- **S13 — Global CCS Status Report 2024 | PDF | Carbon Capture And Storage | Climate Change**
  URL: https://www.scribd.com/document/916596935/CCS-Global-Status-Report-2024
- **S14 — [PDF] ORCHESTRATING CARBON REMOVAL: HOW SCIENCE ...**
  URL: https://www.oxfordenergy.org/wpcms/wp-content/uploads/2025/11/OEF-146-Carbon-Removal.pdf

**Search Duration:** 3.74s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 5
- New gaps: 4
- Resolved gaps: 0

**Processing Duration:** 18.42s

---

## 3. Ledger Updates

### New Claim C8

**Claim**

Authoritative assessments cited by the Oxford Energy Forum indicate that meeting climate goals may require approximately 7–9 billion tonnes of CO₂ removal annually by 2050, whereas current carbon-removal activities collectively remove only tens of millions of tonnes per year; the resulting gap is especially relevant to DACCS and BECCS claims about future contribution rather than demonstrated performance.

- S14 supports (direct): The Oxford Energy Forum introduction reports a requirement of roughly 7–9 GtCO₂ of annual removal by 2050 while current removal activities combined remove only tens of millions of tonnes annually.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C2

**Claim**

Commercial-scale CCS has been demonstrated in several industrial applications, including natural-gas processing, fertilizer and ethanol production, coal gasification, refinery hydrogen, and at least one coal-power project; the supplied evidence also documents Sleipner injecting roughly 0.85 million tonnes of CO₂ annually and more than 16.5 million tonnes cumulatively by January 2017.

- S11 supports (direct): The Global CCS Institute report states that more than 620 CCS projects have been identified globally, including more than 50 operational facilities, corroborating a substantial operating and developing project base.
- S12 supports (direct): The article describes Northern Lights as operational since 2024, with Phase 1 capacity of 1.5 MtCO₂/year and a Phase 2 target of 5 Mt/year by 2028, providing an example of cross-border transport and storage infrastructure.

**Confidence:** HIGH → HIGH

**Status:** CONFLICTING → CONFLICTING

### Updated Claim C3

**Claim**

CCS capture and storage costs vary substantially by application and system design; the supplied review gives a broad indicative range of $50–$600 per tonne of CO₂ and an energy-demand range of 2.5–8 GJ per tonne of CO₂.

- S11 supports (direct): The report explains that capture typically represents the largest portion of overall CCS costs and analyzes capture, compression, pumping, pipelines, and shipping separately, while emphasizing that estimates are general, uncertain, and intended primarily for relative rather than project-specific cost comparison.
- S12 supports (direct): The article reports capture costs of approximately $60–$120 per tonne for an industrial emitter and states that pipeline transport may represent 21–25% of total CCUS project costs, with costs varying by distance, terrain, and throughput.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C6

**Claim**

Large-scale CCS deployment faces substantial economic, infrastructure, policy, and coordination barriers; the supplied sources describe high implementation costs, cost barriers to economies of scale, dependence on policy support, and the need for cross-border capture, transport, utilization, and storage infrastructure.

- S11 supports (direct): The report identifies coordinated capture, transport, and storage infrastructure, adequate transport sizing, cost inflation, limited post-2023 benchmarking data, and reliance on FEED-level rather than final project costs as important deployment and economic uncertainties.
- S12 supports (direct): The article describes a coordination or 'chicken-and-egg' problem between capture developers and transport/storage providers, permitting delays for Class VI wells, right-of-way challenges, and the need for shared cross-border infrastructure.
- S12 contradicts (indirect): Northern Lights is presented as an operating cross-border system with planned expansion from 1.5 to 5 MtCO₂/year, showing that shared infrastructure and coordinated business models can overcome some deployment barriers.

**Confidence:** HIGH → HIGH

**Status:** CONFLICTING → CONFLICTING

### Updated Claim C5

**Claim**

CCS is also proposed for carbon-dioxide removal through direct-air capture with storage and bioenergy with CCS; the supplied EU assessment states that its modelling indicates a need for at least 150 MtCO₂ per year of atmospheric or biogenic CO₂ capture and storage in the EU by 2050.

- S14 supports (direct): The Oxford Energy Forum describes atmospheric removal as necessary alongside emissions reductions and identifies DACCS and other engineered removal pathways as promising but constrained by cost, energy needs, measurement, and permanence questions.
- S14 contradicts (direct): The source emphasizes that current removal activities are only in the tens of millions of tonnes per year against a 7–9 GtCO₂/year 2050 requirement, indicating that proposed large-scale CDR roles remain far beyond demonstrated deployment.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → CONFLICTING

### Updated Claim C7

**Claim**

Supporters argue that CCS could contribute materially to decarbonization, with supplied sources citing modelled contributions of approximately 13% of required emissions reductions by 2060 or 14% of reductions needed by 2050, while opponents argue that reliance on CCS can delay more scalable alternatives and prolong fossil-fuel dependence.

- S11 supports (direct): The Global CCS Institute argues that CCS is important for net-zero transition, particularly in hard-to-abate sectors such as cement, steel, chemicals, ethanol fermentation, and ethylene oxide, and reports more than 620 identified projects.
- S12 supports (direct): The article argues that shared, cross-border transport and storage infrastructure can reduce costs for individual emitters and describes Northern Lights as an example of this deployment model.
- S14 contradicts (direct): The source indicates that current carbon removal is only tens of millions of tonnes annually compared with a 7–9 GtCO₂/year 2050 requirement and highlights unresolved cost, energy, measurement, and permanence constraints for engineered removals.

**Confidence:** MEDIUM → MEDIUM

**Status:** CONFLICTING → CONFLICTING

### New Gap G6

The new sources provide indicative capture and transport cost figures and discuss cost components, but they do not supply consistently defined, independently comparable whole-system costs by sector or credible comparisons with renewables, electrification, efficiency, or non-CCS industrial pathways.

### New Gap G7

The sources describe infrastructure coordination, permitting, pipelines, and a Northern Lights example but do not quantify global geological storage availability or distinguish theoretical, technically accessible, permitted, and practically developable storage, nor do they establish global public-acceptance and supply-chain limits.

### New Gap G8

The new evidence identifies energy needs as a constraint for engineered carbon removal but still does not quantify component-level CCS energy penalties or lifecycle residual emissions under different electricity and fuel sources, leaving conditions for limited or negative net climate benefit unresolved.

### New Gap G9

The evidence still lacks a systematic application-by-application comparison of fossil-power CCS, blue hydrogen, cement CCS, BECCS, and DACCS covering net emissions, permanence, environmental impacts, lock-in, opportunity costs, and demonstrated scalability.

---

## 4. Current Research State

- Claims: 8
- Supported: 4
- Weak: 0
- Conflicting: 4
- Insufficient Evidence: 0
- Open Gaps: 9
- Remaining Searches: 0

### Subquestion Progress

**SQ1:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ2:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ3:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ4:** PARTIAL → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ5:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

### Research Plan Status

**CORE:**

- SQ1 → CONFLICTING (targeted searches: 1)
- SQ2 → CONFLICTING (targeted searches: 1)
- SQ3 → CONFLICTING (targeted searches: 0)
- SQ4 → CONFLICTING (targeted searches: 0)
- SQ5 → CONFLICTING (targeted searches: 0)

**SECONDARY:**

- None

**Remaining targeted searches:** 0

---

## 5. Research Decision

**Decision:** Stop researching.

**Origin:** BUDGET_STOP

**Why**

The maximum research iteration budget was reached.

**Stop Reason:** max_iterations


---

# Final Research Decision

**Stop Reason:** max_iterations

**Remaining Uncertainty**

- G1: No consistent, independently verified global inventory distinguishes nameplate capacity from actual captured, transported, injected, durably stored, and net-reduced CO₂.
- G2/G6: Cost system boundaries, sector-specific whole-system costs, and comparable costs for alternative mitigation options remain unresolved.
- G3/G7: Geological storage availability and practical global infrastructure, permitting, supply-chain, and public-acceptance limits are not quantified.
- G4/G8: Component-level energy penalties and lifecycle residual emissions under different fuel and electricity sources are not established.
- G5/G9: CCS applications are not systematically compared for net emissions, permanence, environmental impacts, lock-in, opportunity costs, and demonstrated scalability.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Question Decomposition | 1 | 10.46s |
| Tavily Search | 3 | 8.95s |
| Evidence Processing | 3 | 49.92s |
| Research Decision | 2 | 7.50s |
| Report Generation | 1 | 20.15s |
| Total Run | — | 96.99s |
