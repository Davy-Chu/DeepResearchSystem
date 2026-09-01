# Research Run Log

## Run Summary

**System Version:** evidence-ledger-decomposer-verifier-v1

**Research Question**

Can carbon capture and storage make a significant contribution to reducing global CO₂ emissions? Evaluate its demonstrated effectiveness, costs, scalability, energy requirements, and major arguments for and against large-scale deployment.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 14

**OpenAI Calls:** 10

**Tavily Calls:** 3

**Verifier Model:** gpt-5.6-luna

**Started:** 2026-08-31T18:59:14-04:00

**Ended:** 2026-08-31T19:01:31-04:00

**Total Runtime:** 137.03s

---

# Research Plan

## Subquestions

### SQ1 [CORE]

**Question:**

What evidence demonstrates the effectiveness of carbon capture and storage (CCS) in reducing CO₂ emissions, including capture performance, transport and storage integrity, permanence, and emissions across the full system lifecycle?

**Success criteria:**

Assess empirical evidence from operating and completed CCS projects, distinguishing captured CO₂ from CO₂ permanently stored and from net lifecycle emissions; identify demonstrated performance, leakage or monitoring findings, and important limitations or uncertainty.

**Initial status:** UNRESEARCHED

### SQ2 [CORE]

**Question:**

What are the current and projected costs of CCS, and how do they vary by application, technology, region, and project stage compared with relevant alternatives?

**Success criteria:**

Provide comparable cost measures and assumptions where possible, distinguish capture, transport, storage, and total system costs, and address uncertainty, cost reductions, financing, and applications in which CCS is especially costly or potentially competitive.

**Initial status:** UNRESEARCHED

### SQ3 [CORE]

**Question:**

How scalable is CCS as a global emissions-reduction strategy, considering deployment rates, storage-resource capacity, infrastructure, energy and material requirements, workforce and supply chains, and the timeframe needed for meaningful contribution?

**Success criteria:**

Compare current deployment with modeled or stated future requirements, quantify or characterize geological storage and infrastructure constraints, assess build-out feasibility over relevant timeframes, and identify regional or sectoral limitations.

**Initial status:** UNRESEARCHED

### SQ4 [CORE]

**Question:**

What additional energy requirements and associated emissions does CCS impose, and how do they affect its net climate benefit and broader energy-system implications?

**Success criteria:**

Explain energy-penalty mechanisms and quantify ranges where evidence permits for major applications, including implications for fuel or electricity demand, water or other resource use, and net emissions under different energy sources and operating conditions.

**Initial status:** UNRESEARCHED

### SQ5 [CORE]

**Question:**

What are the strongest arguments for and against large-scale deployment of CCS, including its role in hard-to-abate sectors and carbon removal, environmental and public-health risks, economic and policy concerns, infrastructure lock-in, and opportunity costs relative to other mitigation options?

**Success criteria:**

Present the principal evidence-based arguments on both sides, distinguish point-source capture from carbon removal and fossil-fuel applications, evaluate risks and trade-offs, and identify where claims depend on assumptions, context, or unresolved uncertainty.

**Initial status:** UNRESEARCHED

## Synthesis Requirements

- Synthesize the evidence across effectiveness, costs, scalability, energy requirements, and deployment arguments to judge whether CCS can make a significant contribution globally, rather than treating each criterion independently.
- Distinguish technically demonstrated performance from projected future performance and distinguish gross captured CO₂ from net, durable emissions reductions.
- Compare CCS with relevant alternative mitigation options where needed to evaluate opportunity costs and significance, while preserving differences among industrial applications, power generation, and carbon removal.
- State the timeframe, geographic scope, assumptions, and major uncertainties behind the overall assessment.

## Output Requirements

- Provide an evaluative conclusion about whether CCS can make a significant contribution to reducing global CO₂ emissions.
- Cover demonstrated effectiveness, costs, scalability, energy requirements, and major arguments for and against large-scale deployment.
- Present both supporting and opposing arguments and clearly communicate uncertainty and context dependence.

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
- **S3 — Near-term carbon dioxide removal deployment can ...**
  URL: https://www.nature.com/articles/s43247-024-01916-4
- **S4 — Carbon Capture**
  URL: https://www.c2es.org/content/carbon-capture
- **S5 — A Vision for Carbon Capture, Utilisation, and Storage in the ...**
  URL: https://www.catf.us/resource/a-vision-carbon-capture-utilisation-and-storage-eu

**Search Duration:** 2.62s

---

## 2. Evidence Processing

- New claim proposals: 6
- Existing claim updates: 0
- New gaps: 5
- Resolved gaps: 0

**Processing Duration:** 18.87s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

CCS has demonstrated operation in several commercial applications and storage projects, but the supplied evidence does not establish that the global CCS fleet currently delivers a large share of total emissions reductions.

- S4 supports (direct): Reports commercial-scale capture operation in natural-gas processing, coal gasification, ethanol, fertilizer, refinery hydrogen, and coal-fired power, and identifies Sleipner as operating since 1996 with more than 16.5 million tonnes injected by January 2017.
- S1 supports (direct): States that CCS captures and stores less than 0.1% of annual global CO₂ emissions despite more than $40 billion invested, and reviews projects including Sleipner, Gorgon, In Salah, and Petra Nova.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C2

**Claim**

Reported capture performance can exceed 90% at some power and industrial facilities, but captured CO₂ is not equivalent to permanently stored CO₂ or to net lifecycle emissions reductions.

- S4 supports (direct): States that carbon-capture technologies can capture more than 90% of CO₂ emissions from power plants and industrial facilities.
- S1 supports (direct): Highlights suboptimal capture rates, geological uncertainties, durability concerns, and the distinction between projects described as successful and their actual scale, permanence, and emissions-offset claims.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C3

**Claim**

CCS may be particularly relevant to unavoidable process emissions in sectors such as cement, lime, some chemicals, and waste incineration, as well as to certain other hard-to-abate industrial applications including steel, where alternatives to fossil fuels or process-based emissions reductions may be limited or costly.

- S5 supports (direct): Identifies cement, steel, chemical production, and waste incineration as hard-to-abate sectors and states that cement and lime process emissions are unavoidable within the described processes.
- S1 supports (direct): Concludes that CCS may warrant strategic deployment in sectors such as cement production and legacy infrastructure retrofits where alternatives are limited.
- S2 supports (indirect): States that CCS can be applied to cement, steel, and chemical production.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C4

**Claim**

The supplied sources characterize CCS as energy-intensive and costly, with a broad indicative range of 2.5–8 GJ per tonne of CO₂ and $50–600 per tonne of CO₂, while costs vary by application and project conditions.

- S1 supports (direct): Provides an evaluation range of 2.5–8 GJ/tCO₂ for energy demand and $50–600/tCO₂ for cost, and describes CCS as a high-cost technology with recurring cost overruns in reviewed cases.
- S2 supports (direct): Identifies high large-scale implementation costs as a major deployment challenge.
- S4 contradicts (indirect): Describes natural-gas reforming with CCS as potentially the lowest-cost option for producing low-carbon hydrogen and states that capture can become nearly emissions-free when clean electricity powers the capture facility; this is conditional and does not refute the broad cost range.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C5

**Claim**

Large-scale CCS deployment would require substantial expansion of capture, transport, storage, and associated coordination infrastructure; modeled requirements are far above current deployment.

- S4 supports (direct): Reports 30 operating commercial-scale projects, 11 under construction, and 153 at different development stages, while citing a potential 14% contribution to global reductions needed by 2050.
- S5 supports (direct): Estimates that the EU may need to capture and use or store 300–640 MtCO₂ per year by 2050, including at least 150 Mt/year of atmospheric or biogenic CO₂, and describes the required scale as significant.
- S1 supports (direct): Reports that current CCS captures and stores less than 0.1% of annual global CO₂ emissions and discusses the disconnect between modeled expectations and empirical outcomes.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C6

**Claim**

The supplied sources present carbon removal using geological storage, including direct-air-capture storage and bioenergy with capture and storage, as potentially important for residual or legacy emissions, but they do not establish that these approaches are already scalable or cost-effective.

- S5 supports (direct): States that permanent atmospheric removal will be needed for residual and historic emissions and gives an EU modeled requirement of at least 150 Mt/year of atmospheric or biogenic CO₂ captured and stored by 2050.
- S3 supports (direct): Finds in a United States net-zero modeling study that near-term co-deployment of carbon-removal methods can reduce transition risks and that delaying deployment raises modeled carbon prices by 59–79%.
- S1 contradicts (indirect): Emphasizes that CCS projects often fall short when assessed for durability, scale, and emissions-offset claims, and characterizes continued broad reliance on CCS as a high-cost gamble.

**Confidence:** MEDIUM

**Status:** CONFLICTING

### New Gap G1

No source provides a consistent, independently verified lifecycle accounting across capture, compression, transport, injection, monitoring, leakage, and post-closure stewardship for operating CCS projects.

### New Gap G2

Application-, region-, and project-stage-specific CCS costs are not supplied in comparable form, and no robust comparison with electrification, renewables, efficiency, or other alternatives is available.

### New Gap G3

The evidence does not quantify global geological storage capacity, feasible annual injection rates, transport-network requirements, material and workforce needs, or realistic deployment rates through 2050.

### New Gap G4

Energy-penalty evidence is limited to one broad range; the sources do not give technology- and sector-specific fuel, electricity, water, or induced-emissions estimates or net-emissions results under different energy supplies.

### New Gap G5

The sources do not adequately assess environmental, public-health, leakage, monitoring-liability, infrastructure-lock-in, or opportunity-cost arguments using empirical evidence across jurisdictions.

---

## 4. Current Research State

- Claims: 6
- Supported: 5
- Weak: 0
- Conflicting: 1
- Insufficient Evidence: 0
- Open Gaps: 5
- Remaining Searches: 2

### Subquestion Progress

**SQ1:** UNRESEARCHED → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ2:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ3:** UNRESEARCHED → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ4:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ5:** UNRESEARCHED → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

### Research Plan Status

**CORE:**

- SQ1 → CONFLICTING (targeted searches: 0)
- SQ2 → PARTIAL (targeted searches: 0)
- SQ3 → CONFLICTING (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)
- SQ5 → CONFLICTING (targeted searches: 0)

**SECONDARY:**

- None

**Remaining targeted searches:** 2

---

## 5. Independent Verification

### V1 — Claim C3

**Phase:** INITIAL

**Evidence source IDs:** S5, S1, S2

**Verdict:** NEEDS_QUALIFICATION

**Reason**

The evidence supports CCS as relevant to hard-to-abate industries, especially cement, chemicals, and waste incineration, where process emissions can be intrinsic to production. It also identifies steel as a hard-to-abate sector, but does not establish that steel emissions are necessarily process emissions or cannot be eliminated by changing energy sources. The claim should distinguish unavoidable process emissions from energy-related emissions and avoid implying CCS is uniformly required across all listed sectors.

**Missing assumptions**

- The specific industrial process and emission source determine whether emissions are unavoidable process emissions or energy-related emissions.
- Alternative technologies such as electrification, hydrogen, material substitution, or efficiency improvements may reduce some emissions in these sectors.
- CCS is relevant to some applications within each sector, not necessarily to the sector as a whole.

**Source concerns**

- S5 is an advocacy-oriented stakeholder report prepared for the EU CCUS Forum and strongly promotes CCS; its conclusions may not be neutral.
- S1 is a review article whose supplied publication details indicate a 2026 issue, limiting its usefulness for establishing current demonstrated practice; the excerpt nonetheless supports a targeted role in hard-to-abate sectors.

**Counter-search status:** NOT_REQUESTED

**Reconciliation**

Claim:

"CCS can be particularly relevant to process emissions and other hard-to-abate industrial sectors, including cement, steel, chemicals, and waste incineration, where some emissions are not eliminated simply by changing the energy source."
→
"CCS may be particularly relevant to unavoidable process emissions in sectors such as cement, lime, some chemicals, and waste incineration, as well as to certain other hard-to-abate industrial applications including steel, where alternatives to fossil fuels or process-based emissions reductions may be limited or costly."

Confidence: MEDIUM → HIGH

Status: SUPPORTED → SUPPORTED

---

## 6. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ1

**Why**

SQ1 is a conflicting CORE subquestion, and the high-importance gap on independently verified full-system lifecycle performance remains unresolved. Evidence on capture rates alone does not establish net, durable emissions reductions; one focused search could materially improve the evaluation of demonstrated effectiveness and permanence.

**Next Search**

> independent lifecycle assessments of operating CCS projects: capture rate, energy penalty, compression and transport emissions, injection and monitoring, leakage, permanence, and net CO2 reductions; empirical evidence from Sleipner, Quest, Gorgon, In Salah, and other projects


---

# Iteration 2

## 1. Search

**Query**

> independent lifecycle assessments of operating CCS projects: capture rate, energy penalty, compression and transport emissions, injection and monitoring, leakage, permanence, and net CO2 reductions; empirical evidence from Sleipner, Quest, Gorgon, In Salah, and other projects

**Target:** SQ1

**Purpose:** SUBQUESTION

**Why this query**

SQ1 is a conflicting CORE subquestion, and the high-importance gap on independently verified full-system lifecycle performance remains unresolved. Evidence on capture rates alone does not establish net, durable emissions reductions; one focused search could materially improve the evaluation of demonstrated effectiveness and permanence.

5 result(s) retrieved; 4 new unique source(s) added.

- **S6 — Microsoft Word - CO2_storage_Rep_Final.doc**
  URL: https://bellona.org/assets/sites/3/Case_Study_on_the_Sleipner_Gas_Field_in_Norway.pdf
- **S7 — SEPTEMBER 2025 PERSPECTIVE THE SAFETY AND PERMANENCE OF CO2 GEOLOGICAL STORAGE**
  URL: https://www.globalccsinstitute.com/wp-content/uploads/2025/09/The-Safety-and-Permanence-of-CO2-Geological-Storage-Global-CCS-Institute.pdf
- **S8 — Carbon capture and storage: What can we learn from the ...**
  URL: https://www.catf.us/resource/carbon-capture-storage-what-can-learn-from-project-track-record
- **S9 — List of carbon capture and storage projects - Wikipedia**
  URL: https://en.wikipedia.org/wiki/List_of_carbon_capture_and_storage_projects

**Search Duration:** 3.00s

---

## 2. Evidence Processing

- New claim proposals: 2
- Existing claim updates: 6
- New gaps: 1
- Resolved gaps: 0

**Processing Duration:** 24.60s

---

## 3. Ledger Updates

### New Claim C7

**Claim**

As of 2025, dedicated geological-storage projects provide substantial operational experience, but the reported number of projects and stored quantities depend on project definitions: one industry source reports 18 dedicated projects storing over 80 million tonnes, while other project inventories include EOR and broader capture-and-storage facilities.

- S7 supports (direct): Reports 18 operating dedicated geological-storage projects storing over 80 million tonnes of CO₂ as of June 2025, while explicitly excluding EOR projects.
- S8 supports (direct): Reports 41 commercial CCS projects operating under a broader definition that includes facilities capturing and storing CO₂ from industrial facilities or fossil power plants, and notes that many were not developed primarily for climate purposes.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C8

**Claim**

Available project-track-record evidence indicates that some large-scale CCS projects have consistently achieved high technical performance, while operational challenges, incomplete transparency, and project-specific interruptions show that performance is not uniform across the fleet.

- S8 supports (direct): Identifies Sleipner, Alberta Carbon Trunk Line, and Quest as projects that consistently met high technical-performance levels, while also reporting operational challenges and calling for more transparent performance data.
- S9 supports (direct): Reports that In Salah injected about 3.8 million tonnes but suspended injection in 2011 because of concerns about seal integrity, fracture, and CO₂ movement outside the lease; injection did not restart.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

CCS has demonstrated operation in several commercial applications and storage projects, but the supplied evidence does not establish that the global CCS fleet currently delivers a large share of total emissions reductions.

- S7 supports (direct): Reports 18 dedicated geological-storage projects operating globally and over 80 million tonnes stored as of June 2025, documenting a larger operational base while still representing only a small fraction of global emissions.
- S8 supports (direct): Reports 41 commercial CCS projects operating under a broader definition and states that climate-oriented CCS deployment remains relatively new; many projects were motivated by commercial EOR or other purposes rather than maximizing climate benefit.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

Reported capture performance can exceed 90% at some power and industrial facilities, but captured CO₂ is not equivalent to permanently stored CO₂ or to net lifecycle emissions reductions.

- S7 supports (direct): Reports more than three decades of dedicated storage experience, over 80 million tonnes stored in 18 projects, and no reported cases across those projects of CO₂ leakage to the surface causing environmental harm.
- S8 supports (direct): Finds that Sleipner, Alberta Carbon Trunk Line, and Quest consistently met high technical-performance levels, while emphasizing that capture, transport, and storage performance must be reported transparently and is not uniform.
- S9 supports (direct): Reports no CO₂ leakage during In Salah's operating lifetime, but also documents suspension over concerns about seal integrity, fracture, and migration outside the lease.
- S6 contradicts (direct): Documents potential release pathways, groundwater and ecosystem hazards, induced seismicity, and the need for monitoring, verification, risk assessment, and remediation; this does not establish actual leakage but limits claims of demonstrated universal permanence.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C3

**Claim**

CCS may be particularly relevant to unavoidable process emissions in sectors such as cement, lime, some chemicals, and waste incineration, as well as to certain other hard-to-abate industrial applications including steel, where alternatives to fossil fuels or process-based emissions reductions may be limited or costly.

- S8 supports (direct): States that climate-oriented capture is increasingly needed in cement, steel, and petrochemical industries where alternatives may be limited, and that capture costs are often higher in these diverse applications.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

The supplied sources characterize CCS as energy-intensive and costly, with a broad indicative range of 2.5–8 GJ per tonne of CO₂ and $50–600 per tonne of CO₂, while costs vary by application and project conditions.

- S8 supports (direct): States that applying CCS to cement, steel, and petrochemicals is often more costly than historical high-purity CO₂ applications, and that transport to distant saline storage can add cost and complexity.
- S8 contradicts (indirect): Notes that some component technologies are mature and that historical CO₂ capture and transport have operated commercially for decades; this qualifies, rather than eliminates, the broad cost and energy burden for climate-oriented applications.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

Large-scale CCS deployment would require substantial expansion of capture, transport, storage, and associated coordination infrastructure; modeled requirements are far above current deployment.

- S7 supports (direct): Reports 18 dedicated commercial storage projects and more than 50 pilot and demonstration projects, but presents this operational base as experience preceding deployment at the scale required for deep global emissions reductions.
- S8 supports (direct): States that meeting international climate commitments requires several billion tonnes of storage annually by 2050 and that this is many times greater than current deployment; it also identifies transport to storage as increasingly complex when sources and sites are distant.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C6

**Claim**

The supplied sources present carbon removal using geological storage, including direct-air-capture storage and bioenergy with capture and storage, as potentially important for residual or legacy emissions, but they do not establish that these approaches are already scalable or cost-effective.

- S8 supports (direct): Explicitly states that CCS can also remove historic CO₂ emissions directly from the air, while noting that climate commitments require storage at a scale many times current deployment.
- S8 contradicts (direct): States that combining capture, transport, and storage for climate mitigation is relatively new and can be more costly, and that applying capture to diverse industrial sources is often substantially more expensive than historical applications.

**Confidence:** MEDIUM → MEDIUM

**Status:** CONFLICTING → CONFLICTING

### New Gap G6

Reported CCS project counts, stored quantities, and performance records use materially different boundaries, especially regarding dedicated storage, EOR, capture-only facilities, and projects not primarily operated for climate mitigation; a harmonized independent inventory is unavailable.

---

## 4. Current Research State

- Claims: 8
- Supported: 7
- Weak: 0
- Conflicting: 1
- Insufficient Evidence: 0
- Open Gaps: 6
- Remaining Searches: 1

### Subquestion Progress

**SQ1:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ2:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ3:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ4:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ5:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

### Research Plan Status

**CORE:**

- SQ1 → CONFLICTING (targeted searches: 1)
- SQ2 → PARTIAL (targeted searches: 0)
- SQ3 → CONFLICTING (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)
- SQ5 → CONFLICTING (targeted searches: 0)

**SECONDARY:**

- None

**Remaining targeted searches:** 1

---

## 5. Independent Verification

### V2 — Claim C3

**Phase:** RECHECK

**Evidence source IDs:** S5, S1, S2, S8

**Verdict:** VERIFIED

**Reason**

The supplied evidence directly supports CCS as especially relevant for process emissions in cement, lime, some chemicals, and waste incineration, and identifies steel as a hard-to-abate sector where alternatives may be limited or more costly. The wording appropriately uses conditional terms such as “may,” “certain,” and “where.”

**Missing assumptions**

- The relevance and cost-effectiveness of CCS vary by facility, region, technology, carbon price, infrastructure availability, and the development of alternatives.
- “Unavoidable” process emissions should not be interpreted as implying that all emissions from these sectors are unavoidable or that CCS is the only mitigation option.

**Source concerns**

- S5 and S8 are produced by Clean Air Task Force, an advocacy organization, and present a strongly favorable view of CCS.
- S2 is a non-peer-reviewed blog and is not needed to support this claim.
- The supplied excerpts provide limited comparative evidence on the costs and performance of CCS versus sector-specific alternatives, particularly in steel.

**Counter-search status:** NOT_REQUESTED

**Reconciliation**

Confidence: HIGH → HIGH

Status: SUPPORTED → SUPPORTED

---

## 6. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ2

**Why**

A final search is likely to materially improve the answer because the core cost question remains largely unresolved: the evidence lacks comparable application-specific costs, assumptions, regional variation, project-stage uncertainty, and comparisons with alternatives. This is a more consequential gap than further refining already partially documented effectiveness or deployment evidence.

**Next Search**

> Recent authoritative comparative assessment of CCS costs by sector and stage (capture, transport, storage, total system), including cement, steel, power, hydrogen and DAC, regional variation, financing/overruns, learning projections, and comparison with electrification, renewables, efficiency, and alternative mitigation options


---

# Iteration 3

## 1. Search

**Query**

> Recent authoritative comparative assessment of CCS costs by sector and stage (capture, transport, storage, total system), including cement, steel, power, hydrogen and DAC, regional variation, financing/overruns, learning projections, and comparison with electrification, renewables, efficiency, and alternative mitigation options

**Target:** SQ2

**Purpose:** SUBQUESTION

**Why this query**

A final search is likely to materially improve the answer because the core cost question remains largely unresolved: the evidence lacks comparable application-specific costs, assumptions, regional variation, project-stage uncertainty, and comparisons with alternatives. This is a more consequential gap than further refining already partially documented effectiveness or deployment evidence.

5 result(s) retrieved; 5 new unique source(s) added.

- **S10 — Why the Cost of Carbon Capture and Storage Remains Persistently High | International Institute for Sustainable Development**
  URL: https://www.iisd.org/articles/deep-dive/why-carbon-capture-storage-cost-remains-high
- **S11 — A new era for CCUS – CCUS in Clean Energy Transitions**
  URL: https://www.iea.org/reports/ccus-in-clean-energy-transitions/a-new-era-for-ccus
- **S12 — Scaling carbon capture and storage (CCS) to gigaton ...**
  URL: https://www.sciencedirect.com/science/article/pii/S1750583625002294
- **S13 — [PDF] ADVANCEMENTS IN CCS TECHNOLOGIES AND COSTS**
  URL: https://www.globalccsinstitute.com/wp-content/uploads/2025/10/Advancements-in-CCS-Technologies-and-Costs-Report-2.pdf
- **S14 — Carbon Capture, Utilization, and Storage: Technologies and Costs in the U.S. Context | The Belfer Center for Science and International Affairs**
  URL: https://www.belfercenter.org/publication/carbon-capture-utilization-and-storage-technologies-and-costs-us-context

**Search Duration:** 3.44s

---

## 2. Evidence Processing

- New claim proposals: 2
- Existing claim updates: 6
- New gaps: 3
- Resolved gaps: 0

**Processing Duration:** 23.80s

---

## 3. Ledger Updates

### New Claim C9

**Claim**

CCS cost estimates differ substantially by CO₂-stream concentration and application: the supplied evidence reports approximately CAD 27–48 per tonne captured for concentrated streams and CAD 50–150 per tonne captured for diluted streams, with transport and storage costs additional; reported estimates are often pre-project or engineering-level estimates rather than validated final costs.

- S10 supports (direct): Reports CAD 27–48/tCO₂ captured for concentrated streams and CAD 50–150/tCO₂ captured for diluted streams, states that transport and storage are additional, and cautions that available estimates are predominantly projections or FEED-level estimates.
- S13 supports (direct): States that capture is typically the largest CCS cost component, that transport costs depend on flow rate, distance, and method, and that many reported costs are FEED-level estimates with limited publicly available post-2023 data.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C10

**Claim**

The supplied sources identify slow deployment, high costs, project complexity, and dependence on public support as major barriers to widespread CCS deployment, while presenting CCS as potentially valuable in hard-to-decarbonize sectors and as a complement to electrification and renewable energy.

- S10 supports (direct): Attributes persistent high costs to design complexity and customization, reports slow cost reductions relative to solar and wind, and states that oil-and-gas-sector viability relies heavily on government financial support; it nevertheless identifies cement and steel as possible applications.
- S11 supports (direct): States that CCUS deployment has been slow and investment has remained below 0.5% of global clean-energy and efficiency investment, while identifying strategic roles in cement, steel, chemicals, hydrogen, retrofits, and carbon removal.
- S12 supports (direct): Concludes that CCS can offer cost-effective mitigation in hard-to-abate applications and complement renewable energy and electrification, while calling for rapid scale-up and policy action.
- S14 supports (direct): States that CCUS is not economically competitive today in most US applications without stronger incentives or legal requirements, but identifies potential roles in hard-to-electrify industry, firm power, backup generation, and synthetic fuels.

**Confidence:** HIGH

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

CCS has demonstrated operation in several commercial applications and storage projects, but the supplied evidence does not establish that the global CCS fleet currently delivers a large share of total emissions reductions.

- S11 supports (direct): Describes CCUS deployment as slow with limited historical impact on global CO₂ emissions, despite its recognized potential.
- S13 supports (direct): Reports more than 620 identified projects, including more than 50 operational facilities, indicating growth but still a limited operational base relative to global mitigation needs.
- S14 supports (direct): Reports only 27 operating commercial CCUS facilities worldwide in its 2022 inventory and approximately 20 MtCO₂ captured annually in the United States, underscoring the small current contribution.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

Reported capture performance can exceed 90% at some power and industrial facilities, but captured CO₂ is not equivalent to permanently stored CO₂ or to net lifecycle emissions reductions.

- S10 supports (direct): Directly distinguishes CO₂ captured from CO₂ avoided, with the latter subtracting emissions from the energy required to operate CCS; it also notes that fossil-fuel energy supply can generate additional emissions.
- S13 supports (indirect): Describes capture, transport, and storage as separate segments with distinct technical and cost considerations, supporting the need to distinguish capture performance from whole-system outcomes.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

The supplied sources characterize CCS as energy-intensive and costly, with a broad indicative range of 2.5–8 GJ per tonne of CO₂ and $50–600 per tonne of CO₂, while costs vary by application and project conditions.

- S10 supports (direct): Provides application-specific capture-cost estimates of CAD 27–48/tCO₂ for concentrated streams and CAD 50–150/tCO₂ for diluted streams, identifies design complexity and customization as persistent cost drivers, and notes that transport and storage are additional.
- S13 supports (direct): States that capture commonly represents the largest cost component, analyzes transport cost dependence on distance, flow rate, and transport mode, and cautions that many cost figures are engineering estimates rather than final project costs.
- S14 supports (direct): States that CCUS is not economically competitive in most US applications under prevailing incentives and reports reliance on tax credits and other policy support for project economics.
- S12 contradicts (direct): The review concludes that CCS can offer cost-effective mitigation in hard-to-abate applications and complement electrification and renewables; this is application-specific and does not negate high costs elsewhere.
- S11 contradicts (direct): Identifies strategic and potentially least-cost roles for CCUS in hard-to-abate sectors and low-carbon hydrogen, although it also records slow historical deployment.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

Large-scale CCS deployment would require substantial expansion of capture, transport, storage, and associated coordination infrastructure; modeled requirements are far above current deployment.

- S11 supports (direct): States that more than 30 new integrated facilities had been announced since 2017, but describes historical deployment as slow and says the coming decade is critical for scale-up.
- S12 supports (direct): Cites an IEA pathway requiring CCS deployment of 1 GtCO₂ annually by 2030, demonstrating the scale of modeled requirements.
- S13 supports (direct): Reports more than 620 identified projects, including over 50 operational facilities, while emphasizing the need for further deployment and appropriately sized transport infrastructure.
- S14 supports (direct): Reports roughly 20 MtCO₂ captured annually by US facilities versus modeled requirements as high as 1.8 Gt annually across more than 1,000 facilities.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C3

**Claim**

CCS may be particularly relevant to unavoidable process emissions in sectors such as cement, lime, some chemicals, and waste incineration, as well as to certain other hard-to-abate industrial applications including steel, where alternatives to fossil fuels or process-based emissions reductions may be limited or costly.

- S10 supports (direct): Identifies cement and steel as sectors where substitute materials or fully mature decarbonization technologies are not yet available or developed, while distinguishing point-source CCS from direct-air capture.
- S11 supports (direct): Identifies cement, iron and steel, chemicals, and synthetic fuels for long-distance transport as sectors or applications where other options may be limited.
- S12 supports (direct): Characterizes CCS as potentially cost-effective in hard-to-abate applications and complementary to electrification and renewable energy.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C6

**Claim**

The supplied sources present carbon removal using geological storage, including direct-air-capture storage and bioenergy with capture and storage, as potentially important for residual or legacy emissions, but they do not establish that these approaches are already scalable or cost-effective.

- S11 supports (direct): Identifies bioenergy with CCS and direct air capture with storage as ways to remove atmospheric CO₂ and balance unavoidable or technically difficult emissions.
- S12 supports (indirect): Includes carbon removal among the technologies assessed for net-zero pathways but sets a demanding 1 GtCO₂ annual CCS scale target by 2030.
- S10 contradicts (direct): Emphasizes that direct-air capture and storage is distinct from point-source CCS and that the available evidence does not establish broad scalability or cost-effectiveness of climate-oriented applications.

**Confidence:** MEDIUM → HIGH

**Status:** CONFLICTING → CONFLICTING

### New Gap G7

The supplied sources provide improved indicative and application-specific costs but still do not supply a consistent, independently comparable total-system cost dataset—including capture, transport, storage, financing, and avoided-emissions accounting—across regions and against major alternatives.

### New Gap G8

The new deployment targets and project inventories do not establish feasible global build rates, geological storage capacity, annual injection limits, or the infrastructure, materials, workforce, and permitting requirements needed to reach modeled gigatonne-scale deployment.

### New Gap G9

The sources distinguish captured from avoided CO₂ and identify energy-related emissions, but do not provide sector-specific energy, water, fuel, or lifecycle-emissions results under alternative energy supplies.

---

## 4. Current Research State

- Claims: 10
- Supported: 9
- Weak: 0
- Conflicting: 1
- Insufficient Evidence: 0
- Open Gaps: 9
- Remaining Searches: 0

### Subquestion Progress

**SQ1:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ2:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ3:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ4:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ5:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

### Research Plan Status

**CORE:**

- SQ1 → CONFLICTING (targeted searches: 1)
- SQ2 → PARTIAL (targeted searches: 1)
- SQ3 → CONFLICTING (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)
- SQ5 → CONFLICTING (targeted searches: 0)

**SECONDARY:**

- None

**Remaining targeted searches:** 0

---

## 5. Independent Verification

### V3 — Claim C3

**Phase:** RECHECK

**Evidence source IDs:** S5, S1, S2, S8, S10, S11, S12

**Verdict:** VERIFIED

**Reason**

The supplied evidence directly identifies cement, lime, some chemical production, and waste incineration as sectors with unavoidable or process-related emissions, and identifies cement, steel, and other heavy industries as hard to decarbonize because alternatives may be limited, costly, or not fully mature. The claim is appropriately qualified with “may” and “certain.”

**Source concerns**

- Some supporting sources are advocacy or policy-oriented organizations (CATF and IISD), so claims about CCS being part of a lowest-cost pathway should not be generalized without additional comparative studies.
- The evidence supports sectoral relevance but does not establish that CCS is always the best option in each named application or region.

**Counter-search status:** NOT_REQUESTED

**Reconciliation**

Confidence: HIGH → HIGH

Status: SUPPORTED → SUPPORTED

---

## 6. Research Decision

**Decision:** Stop researching.

**Origin:** BUDGET_STOP

**Why**

The maximum research iteration budget was reached.

**Stop Reason:** max_iterations


---

# Final Research Decision

**Stop Reason:** max_iterations

**Remaining Uncertainty**

- G1: No consistent, independently verified full-lifecycle accounting is supplied for operating projects, including capture, compression, transport, injection, monitoring, leakage, and post-closure stewardship.
- G2 and G7: Comparable regional, application-specific total-system costs—including financing, transport, storage, and avoided-emissions accounting—are unavailable, as is a robust comparison with electrification, renewables, efficiency, and other alternatives.
- G3 and G8: The ledger does not quantify global storage capacity, feasible annual injection rates, infrastructure, materials, workforce, permitting, or realistic build rates through 2050.
- G4 and G9: Sector-specific energy, electricity, fuel, water, induced-emissions, and net-emissions results under different energy supplies are not provided.
- G5: Empirical cross-jurisdiction evidence on environmental and public-health effects, leakage liability, monitoring, infrastructure lock-in, and opportunity costs is insufficient.
- G6: No harmonized independent inventory reconciles project counts, stored quantities, performance, EOR, and climate-purpose boundaries.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Question Decomposition | 1 | 9.44s |
| Tavily Search | 3 | 9.06s |
| Evidence Processing | 3 | 67.28s |
| Independent Verification | 3 | 19.80s |
| Research Decision | 2 | 9.06s |
| Report Generation | 1 | 22.37s |
| Total Run | — | 137.03s |

# Verifier Diagnostics

- Verification calls: 3
- Claims verified: 1
- VERIFIED verdicts: 2
- NEEDS_QUALIFICATION verdicts: 1
- CONTRADICTED verdicts: 0
- INSUFFICIENT_EVIDENCE verdicts: 0
- Counter-searches requested: 0
- Counter-searches executed: 0
- Counter-searches blocked by budget: 0
- Counter-searches blocked as duplicates: 0
- Claims whose wording changed: 1
- Claims whose confidence decreased: 0
- Claims whose status changed: 0
- Searches allocated to general research: 1
- Searches allocated to subquestions: 2
- Searches allocated to counter-search: 0
