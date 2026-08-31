# Research Run Log

## Run Summary

**System Version:** evidence-ledger-v1

**Research Question**

Can carbon capture and storage make a significant contribution to reducing global CO₂ emissions? Evaluate its demonstrated effectiveness, costs, scalability, energy requirements, and major arguments for and against large-scale deployment.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 15

**OpenAI Calls:** 6

**Tavily Calls:** 3

**Started:** 2026-08-31T17:29:21-04:00

**Ended:** 2026-08-31T17:30:37-04:00

**Total Runtime:** 75.67s

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
- **S3 — Carbon Capture**
  URL: https://www.c2es.org/content/carbon-capture
- **S4 — A Vision for Carbon Capture, Utilisation, and Storage in the ...**
  URL: https://www.catf.us/resource/a-vision-carbon-capture-utilisation-and-storage-eu
- **S5 — Anticipating a potential deficit in global carbon capture demand in 2030 despite benchmarking strategies**
  URL: https://www.nature.com/articles/s44432-025-00002-0

**Search Duration:** 3.30s

---

## 2. Evidence Processing

- New claim proposals: 5
- Existing claim updates: 0
- New gaps: 4
- Resolved gaps: 0

**Processing Duration:** 17.07s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

CCS has demonstrated commercial operation in several industrial applications, including natural-gas processing, fertilizer production, coal gasification, refinery hydrogen production, and at least one coal-fired power-generation project; however, demonstrated operation does not by itself establish that deployment has achieved large global emissions reductions.

- S3 supports (direct): Reports commercial-scale operation in multiple industrial processes and identifies projects including Sleipner and Petra Nova.
- S1 contradicts (direct): Argues that reviewed projects, including Petra Nova, Gorgon, Sleipner, and In Salah, often fall short when assessed for capture rates, durability, scale, and claimed emissions offsets.

**Confidence:** MEDIUM

**Status:** CONFLICTING

### New Claim C2

**Claim**

The retrieved evidence presents CCS as potentially important for hard-to-abate industrial process emissions, particularly cement, lime, chemicals, steel, and waste incineration, where emissions may be intrinsic to the process or difficult to eliminate through electrification alone.

- S1 supports (direct): Identifies cement and other hard-to-abate sectors as strategic applications where alternatives are limited.
- S4 supports (direct): States that CCUS can mitigate unavoidable process emissions and may be part of the lowest-cost decarbonization pathway for several heavy industries.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C3

**Claim**

CCS requires substantial energy and can be expensive: the review source gives an energy-demand range of 2.5–8 GJ per tonne of CO2 and a cost range of $50–600 per tonne of CO2.

- S1 supports (direct): Explicitly specifies energy demand of 2.5–8 GJ/tCO2 and cost of $50–600/tCO2 in its evaluation framework.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C4

**Claim**

The evidence supports a potentially large future role for CCS/CCUS in climate scenarios, but the scale required is far beyond current deployment and depends heavily on policy coordination, cost reductions, infrastructure, and governance.

- S2 supports (indirect): Cites projections that CCS could contribute up to 13% of required emissions reductions by 2060 and describes policy and storage-site challenges.
- S3 supports (indirect): States that carbon capture could provide 14% of global emissions reductions needed by 2050 and lists projects at operating, construction, and development stages.
- S4 supports (indirect): Reports EU modelling requirements of 300–640 MtCO2 captured and used or stored annually by 2050, and a global IPCC median of 665 Gt captured and stored by 2100 in a 1.5°C-compatible scenario.
- S5 supports (direct): Finds that an optimized strategy could double capture scale by 2030, while still leaving a persistent one-third deficit relative to climate targets; cost barriers impede economies of scale.
- S1 contradicts (direct): States that CCS currently captures and stores less than 0.1% of annual global CO2 emissions despite more than $40 billion invested, and characterizes continued reliance on CCS as high-cost and at risk of delaying other solutions.

**Confidence:** HIGH

**Status:** CONFLICTING

### New Claim C5

**Claim**

Major arguments against large-scale CCS deployment in the retrieved evidence include high costs, energy requirements, uncertain or limited storage availability, geological and leakage/permanence concerns, cost overruns, suboptimal capture performance, public-liability concerns, and the risk of delaying alternative mitigation options.

- S1 supports (direct): Identifies cost overruns, suboptimal capture rates, geological uncertainties, public-liability transfer, energy demand, and risk of delaying more effective solutions.
- S2 supports (direct): Identifies high implementation costs, storage-site availability, and safety and environmental concerns as challenges.
- S5 supports (direct): Reports that cost barriers significantly impede economies of scale and that deployment lags behind expectations.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Gap G1

The retrieved material does not provide a consistent, independently verified accounting of current global CCS capture and permanent-storage capacity, actual capture rates, project reliability, or lifecycle net CO2 reductions.

### New Gap G2

The evidence does not establish comparable, sector-specific costs—including transport, storage, monitoring, liability, financing, and energy-system effects—against major alternatives such as renewables, electrification, efficiency, or process substitution.

### New Gap G3

The sources do not quantitatively resolve how much geological storage capacity is technically, economically, environmentally, and politically usable at global scale, or how durable stored CO2 will be over the relevant climate timescale.

### New Gap G4

The retrieved sources do not provide sufficient evidence to determine whether CCS can make a significant contribution globally in practice, as opposed to being valuable mainly in selected hard-to-abate sectors and for carbon-dioxide-removal pathways.

---

## 4. Current Research State

- Claims: 5
- Supported: 3
- Weak: 0
- Conflicting: 2
- Insufficient Evidence: 0
- Open Gaps: 4
- Remaining Searches: 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** GAP G1

**Why**

Current deployment and real-world net reductions are central to judging whether CCS can make a significant global contribution, but remain unresolved and conflicting.

**Next Search**

> Global CCS Institute, IEA, or peer-reviewed review: current CCS facilities, annual CO₂ captured and permanently stored, capture rates, uptime, and verified net lifecycle emissions reductions in 2023–2024


---

# Iteration 2

## 1. Search

**Query**

> Global CCS Institute, IEA, or peer-reviewed review: current CCS facilities, annual CO₂ captured and permanently stored, capture rates, uptime, and verified net lifecycle emissions reductions in 2023–2024

**Target:** G1

**Purpose:** GENERAL

**Why this query**

Current deployment and real-world net reductions are central to judging whether CCS can make a significant global contribution, but remain unresolved and conflicting.

5 result(s) retrieved; 5 new unique source(s) added.

- **S6 — Previous Global Status of CCS Reports | Global CCS Institute**
  URL: https://www.globalccsinstitute.com/previous-reports
- **S7 — GLOBAL CCS INSTITUTE**
  URL: https://www.aph.gov.au/DocumentStore.ashx?id=7b6f9516-f3ca-461e-b688-8251f095cd7b&subId=755829
- **S8 — Carbon capture and storage: What can we learn from the ...**
  URL: https://www.catf.us/resource/carbon-capture-storage-what-can-learn-from-project-track-record
- **S9 — CCUS in the transition to net-zero emissions**
  URL: https://www.iea.org/reports/ccus-in-clean-energy-transitions/ccus-in-the-transition-to-net-zero-emissions
- **S10 — Global CCS Institute | Carbon Management at Scale**
  URL: https://www.globalccsinstitute.com

**Search Duration:** 2.35s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 4
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 11.66s

---

## 3. Ledger Updates

### New Claim C6

**Claim**

CCS components have substantial prior commercial and operational experience, but integrating capture, transport, and dedicated geological storage specifically for climate mitigation remains comparatively new and can be more costly, especially for dilute or harder-to-abate industrial emissions and storage in saline aquifers.

- S8 supports (direct): Describes decades of experience with capture, CO2 transport, and geological injection, while stating that combining them for climate mitigation is relatively new and generally more costly for sectors such as cement, steel, and petrochemicals.

**Confidence:** HIGH

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

CCS has demonstrated commercial operation in several industrial applications, including natural-gas processing, fertilizer production, coal gasification, refinery hydrogen production, and at least one coal-fired power-generation project; however, demonstrated operation does not by itself establish that deployment has achieved large global emissions reductions.

- S7 supports (direct): Reports 43 operational CCS facilities as of March 2024, with cumulative capture capacity of 50 MtCO2 per year, and describes CCS as proven and safe in its submission.
- S8 supports (direct): Identifies 41 commercial CCS projects operating at the time of its report and documents consistently high technical performance at several projects, including Sleipner, Alberta Carbon Trunk Line, and Quest.
- S8 contradicts (direct): Notes that most operating projects were not developed primarily for climate purposes and often were not required to maximize stored CO2 or minimize atmospheric emissions; it also reports operational challenges across the 13 projects examined.

**Confidence:** MEDIUM → HIGH

**Status:** CONFLICTING → CONFLICTING

### Updated Claim C4

**Claim**

The evidence supports a potentially large future role for CCS/CCUS in climate scenarios, but the scale required is far beyond current deployment and depends heavily on policy coordination, cost reductions, infrastructure, and governance.

- S6 supports (direct): Reports global capture capacity on track to exceed 100 MtCO2 per year once facilities under construction operate, while explicitly stating that gigatonne-scale deployment remains necessary.
- S7 supports (direct): Reports 50 MtCO2 per year of operational capture capacity as of March 2024 and a further 386.8 MtCO2 per year of potential capacity in 521 facilities under development or construction.
- S8 supports (indirect): States that climate pathways require billions of tonnes of annual capture and geological storage by mid-century, many times current deployment, and identifies policy and learning needs for scale-up.
- S9 supports (direct): Identifies four potential roles for CCUS in net-zero transitions: addressing existing energy assets, hard-to-abate sectors, clean hydrogen production, and carbon removal; its scenario analysis projects increasing contribution as costs fall and cheaper options are exhausted.

**Confidence:** HIGH → HIGH

**Status:** CONFLICTING → CONFLICTING

### Updated Claim C3

**Claim**

CCS requires substantial energy and can be expensive: the review source gives an energy-demand range of 2.5–8 GJ per tonne of CO2 and a cost range of $50–600 per tonne of CO2.

- S8 supports (direct): States that integrated climate-oriented CCS can be more costly than established commercial CO2 applications, with higher capture costs in cement, steel, and petrochemicals and added costs for saline-aquifer storage and longer-distance transport.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

Major arguments against large-scale CCS deployment in the retrieved evidence include high costs, energy requirements, uncertain or limited storage availability, geological and leakage/permanence concerns, cost overruns, suboptimal capture performance, public-liability concerns, and the risk of delaying alternative mitigation options.

- S8 supports (direct): Documents technical and operational challenges, the higher cost of applying CCS to diverse industrial sources, added complexity of transport to distant storage, and the need for transparent performance reporting and appropriate regulation.
- S9 supports (indirect): Frames CCS as increasingly valuable after cheaper abatement options are exhausted, implying that its large-scale rationale depends on the availability and relative cost of alternatives.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 6
- Supported: 4
- Weak: 0
- Conflicting: 2
- Insufficient Evidence: 0
- Open Gaps: 4
- Remaining Searches: 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** GAP G1

**Why**

Current evidence shows capacity estimates but does not independently verify actual capture, permanent storage, reliability, or lifecycle net reductions—the key basis for judging demonstrated effectiveness.

**Next Search**

> Independent 2023–2024 assessment of operational CCS: CO₂ actually captured and permanently stored, verified capture rates, uptime, leakage, and lifecycle net emissions reductions, distinguishing climate-mitigation storage from enhanced oil recovery


---

# Iteration 3

## 1. Search

**Query**

> Independent 2023–2024 assessment of operational CCS: CO₂ actually captured and permanently stored, verified capture rates, uptime, leakage, and lifecycle net emissions reductions, distinguishing climate-mitigation storage from enhanced oil recovery

**Target:** G1

**Purpose:** GENERAL

**Why this query**

Current evidence shows capacity estimates but does not independently verify actual capture, permanent storage, reliability, or lifecycle net reductions—the key basis for judging demonstrated effectiveness.

5 result(s) retrieved; 5 new unique source(s) added.

- **S11 — A closer look at CCS: Problems and potential - Zero Carbon Analytics**
  URL: https://zerocarbon-analytics.org/insights/briefings/a-closer-look-at-ccs-problems-and-potential
- **S12 — Carbon Capture and Storage Projects**
  URL: https://acrcarbon.org/wp-content/uploads/2023/03/ACR-CCS-v1.1-2024-08-13.pdf
- **S13 — Carbon capture, utilisation and storage**
  URL: https://www.iea.org/energy-system/renewables-and-low-emissions/carbon-capture-utilisation-and-storage
- **S14 — Carbon Capture's Publicly Funded Failure - Oil Change International**
  URL: https://oilchange.org/publications/ccs-data
- **S15 — Publications Archive | Global CCS Institute**
  URL: https://www.globalccsinstitute.com/publications

**Search Duration:** 2.71s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 3
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 12.63s

---

## 3. Ledger Updates

### New Claim C7

**Claim**

Most operating CCS capacity described in the newly retrieved evidence is associated with enhanced oil recovery (EOR) or oil-and-gas production rather than dedicated permanent climate-mitigation storage: estimates range from 79% to 82.5%.

- S11 supports (direct): Reports that 82.5% of existing CCS capacity uses captured CO2 in EOR and that almost all of the 41 operational projects are connected to oil and gas.
- S14 supports (direct): Reports that 79% of operating global carbon-capture capacity sends captured CO2 to EOR and argues that increased oil production remains the primary use.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

CCS has demonstrated commercial operation in several industrial applications, including natural-gas processing, fertilizer production, coal gasification, refinery hydrogen production, and at least one coal-fired power-generation project; however, demonstrated operation does not by itself establish that deployment has achieved large global emissions reductions.

- S11 supports (direct): Adds evidence that almost all of the 41 operational projects are connected to oil and gas and that 82.5% of existing CCS capacity uses CO2 in EOR, qualifying the climate relevance of demonstrated operation.
- S12 supports (indirect): Provides a formal methodology covering capture, transport, storage, leakage accounting, emissions reductions, and monitoring, reporting, and verification, illustrating the components needed to assess demonstrated climate performance.
- S14 contradicts (direct): Reports that 79% of operating capture capacity is used for EOR and that major projects have overpromised and underdelivered, reinforcing that operational status does not necessarily demonstrate dedicated permanent emissions reduction.

**Confidence:** HIGH → HIGH

**Status:** CONFLICTING → CONFLICTING

### Updated Claim C4

**Claim**

The evidence supports a potentially large future role for CCS/CCUS in climate scenarios, but the scale required is far beyond current deployment and depends heavily on policy coordination, cost reductions, infrastructure, and governance.

- S13 supports (indirect): The IEA page presents installed CO2 capture capacity as a tracked global deployment metric, although the supplied extract does not provide the underlying values.
- S11 contradicts (direct): Reports slow deployment and unmet expectations, and states that nearly all operational projects are linked to oil and gas, challenging the inference that projected CCS potential is already translating into climate-relevant global reductions.
- S14 contradicts (direct): Reports a history of underperformance, substantial public support, and predominant EOR use, weighing against the claim that large-scale deployment will necessarily deliver the modeled climate contribution.

**Confidence:** HIGH → HIGH

**Status:** CONFLICTING → CONFLICTING

### Updated Claim C5

**Claim**

Major arguments against large-scale CCS deployment in the retrieved evidence include high costs, energy requirements, uncertain or limited storage availability, geological and leakage/permanence concerns, cost overruns, suboptimal capture performance, public-liability concerns, and the risk of delaying alternative mitigation options.

- S11 supports (direct): Identifies slow deployment, unmet expectations, costly and uncertain carbon removal, extensive EOR use, and dependence on government support as arguments against indiscriminate large-scale CCS deployment.
- S12 supports (direct): Requires accounting for capture, transport, storage, atmospheric leakage, project emissions, and ongoing MRV, supporting the concern that lifecycle accounting and permanence oversight add material complexity.
- S14 supports (direct): Reports over $20 billion in public spending, potentially much larger future subsidies, predominant EOR use, and examples of projects that underdeliver or lack publicly available capture data.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 7
- Supported: 5
- Weak: 0
- Conflicting: 2
- Insufficient Evidence: 0
- Open Gaps: 4
- Remaining Searches: 0

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

- No consistent, independently verified global accounting of current capture capacity, permanent-storage capacity, actual capture rates, reliability, or lifecycle net CO₂ reductions is provided.
- Comparable sector-specific costs—including transport, storage, monitoring, liability, financing, and energy-system effects—are not established against alternatives such as electrification, renewables, efficiency, or process substitution.
- The technically, economically, environmentally, and politically usable quantity of geological storage, and the long-term durability of storage, remain quantitatively unresolved.
- The evidence does not determine whether CCS can make a significant global contribution in practice or whether its principal value will remain concentrated in selected hard-to-abate sectors and carbon-removal pathways.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 8.36s |
| Evidence Processing | 3 | 41.36s |
| Research Decision | 2 | 5.69s |
| Report Generation | 1 | 20.26s |
| Total Run | — | 75.67s |
