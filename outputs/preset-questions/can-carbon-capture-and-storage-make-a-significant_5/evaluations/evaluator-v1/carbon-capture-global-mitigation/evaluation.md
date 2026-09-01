# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** carbon-capture-global-mitigation

**System Version:** llm-only-baseline-v0

**Model:** gpt-5.6-luna

## Summary

- Overall: 53.8 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.73
- Coverage: 0.75
- Depth: 0.68
- Citation quality: 0.00
- Citation validity: 0.00
- Citation support: 0.00
- Citation completeness: 0.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report clearly understands the distinction between capture rate, nameplate capacity, operating performance, and lifecycle reduction, and it supplies representative projects. However, it does not substantively quantify actual-versus-designed performance or availability for those projects, which is central to the requirement.
- Candidate evidence:
  - The report distinguishes capture rates from total lifecycle reductions: amine systems may capture “85–95% of the CO₂ in the treated exhaust stream,” while lifecycle reductions may be only “roughly 70–90%.”
  - It reports operating examples and periods, including Sleipner injecting “approximately 1 million tonnes of CO₂ per year” since 1996 and Quest storing roughly 1 Mt annually since 2015.
  - It explicitly warns that “announced capacity is not the same as delivered capacity” and notes downtime, cancellations, and projects operating below nameplate capacity.
- Missing:
  - The report does not provide project-specific measured capture versus design/nameplate quantities, capture availability, cumulative stored volumes, or systematic operating-performance data.
  - Boundary definitions are not consistently specified for the 45–50 Mt/year global figure or the cited project figures.
  - The discussion of actual net emissions reductions remains largely estimated rather than demonstrated with audited project-level lifecycle evidence.

### R2

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report covers the main integrity concepts and governance requirements and correctly separates storage from nonpermanent utilization. It lacks the measured storage-performance and leakage evidence needed for a deep assessment.
- Candidate evidence:
  - It describes injection into saline aquifers and depleted reservoirs and explains structural, residual, dissolution, and mineral trapping.
  - It identifies risks including old-well leakage pathways, migration, inadequate pressure management, incomplete monitoring, and induced seismicity.
  - It calls for site characterization, baseline monitoring, leakage detection, post-closure monitoring, financial assurance, and clear long-term liability rules.
  - It distinguishes permanent geological storage from utilization and notes that enhanced oil recovery may have uncertain net benefits.
- Missing:
  - There is little quantitative evidence on observed leakage rates, retention performance, pressure behavior, or monitoring results from Sleipner, Snøhvit, or other projects.
  - Transport safety and the consequences or frequency of pipeline and shipping incidents receive only brief treatment.
  - Long-term responsibility and liability are identified as issues but not evaluated across jurisdictions.
  - The climate accounting of enhanced oil recovery is described as uncertain without explaining the relevant counterfactual oil production, substitution, or lifecycle accounting.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is a strong broad cost assessment with useful application-specific ranges and alternative comparisons. Its depth is limited by unclear cost definitions and the absence of project-level observed-cost evidence.
- Candidate evidence:
  - It provides application-specific capture-cost ranges from $10–40/tCO₂ for high-purity streams, $50–120+/tCO₂ for cement, $60–150/tCO₂ for coal retrofits, and $250–600+/tCO₂ for DAC.
  - It notes that transport and storage can add approximately $10–30/tCO₂ in favorable clusters but may cost substantially more in difficult settings.
  - It discusses capital and operating costs, financing, fuel prices, utilization, first-of-a-kind premiums, infrastructure, subsidies, and enhanced-oil-recovery revenues.
  - It compares fossil power with CCS against renewables, efficiency, storage, and grid investment, while noting that cement and other industrial applications may have fewer alternatives.
- Missing:
  - The report does not clearly state whether the cost ranges are levelized, capture-only, avoided-emissions costs, or include financing and storage; this limits comparability.
  - Observed costs from named operating projects are not separated systematically from modeled or projected costs.
  - Revenue and policy conditions, including carbon prices, tax credits, contracts for difference, and the economic effect of EOR, are discussed qualitatively rather than evaluated with examples.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report quantifies important power and DAC penalties and addresses carbon intensity and resource constraints. It does not provide comparable quantitative treatment across all major pathways or system-scale resource implications.
- Candidate evidence:
  - For power plants, it estimates a net-output penalty of roughly 10–30%, increased fuel consumption, lower efficiency, and potentially higher cooling-water demand.
  - For DAC, it gives representative requirements of 5–10 GJ of heat and 0.5–1.5 GJ of electricity per tonne of CO₂.
  - It explains that dilute atmospheric CO₂ makes DAC energy-intensive and that fossil-powered DAC could lose much of its climate benefit.
  - It discusses methane leakage, upstream emissions, and energy supply for blue hydrogen, and identifies land, water, biodiversity, fertilizer, and indirect land-use concerns for BECCS.
- Missing:
  - Energy and material requirements for BECCS, cement capture, hydrogen, and other major pathways are not quantified consistently.
  - Water, land, biomass, solvent/sorbent, steel, and drilling requirements are mostly qualitative.
  - The report does not translate the stated energy penalties into aggregate energy demand or opportunity costs at the projected multi-gigatonne scales.

### R5

- Coverage: 0.75
- Depth: 0.75
- Rationale: It provides a well-rounded scalability framework and appropriately rejects treating theoretical storage capacity as deployable capacity. More quantitative evidence on infrastructure buildout and historical delivery is needed for full coverage and depth.
- Candidate evidence:
  - It compares current capture of 45–50 Mt/year with possible hundreds of Mt/year by 2030 and 1–7 Gt/year by 2050.
  - It distinguishes theoretical geological capacity from usable capacity and identifies injectivity, pressure management, permitting, pore-space ownership, distance, transport, monitoring, and acceptance constraints.
  - It discusses pipelines, shipping, terminals, injection wells, hubs, compressors, drilling capacity, specialized materials, workforce, and project finance.
  - It notes that announced project capacity can greatly exceed delivered capacity because of cancellations, delays, permitting, subsidies, and technical problems.
- Missing:
  - The report gives no quantified comparison of historical project growth rates, annual injection capacity, pipeline length, wells, or construction requirements.
  - Geological capacity is described as “many thousands of gigatonnes” without a method for converting it to accessible, permitted, and injectible capacity.
  - Workforce, supply-chain, permitting, regulatory, and public-acceptance constraints are identified but not prioritized or supported with empirical deployment evidence.
  - The 2030 and 2050 ranges are scenario claims rather than a demonstrated feasibility assessment tied to specific build rates.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report offers a clear and useful application map and correctly distinguishes avoided emissions from removals. It would need deeper alternative comparisons and quantitative net-removal analysis for complete treatment.
- Candidate evidence:
  - It identifies cement and lime, high-purity industrial streams, chemicals, hydrogen, industrial clusters, DAC, BECCS, and some waste-to-energy as possible applications.
  - It explains that cement calcination produces process CO₂ that electrification and renewable energy cannot eliminate, making CCS comparatively valuable there.
  - It distinguishes point-source avoidance from removal: fossil and industrial capture prevents emissions, whereas biomass capture and DAC with storage can remove atmospheric CO₂.
  - It treats fossil power, old plant retrofits, high-methane blue hydrogen, and carbon-intensive DAC as weaker applications and calls for comparison with electrification and renewable alternatives.
- Missing:
  - Sectoral necessity claims are not examined in detail against specific alternatives such as alternative cements, material efficiency, electrified hydrogen, direct-reduced iron, or other process changes.
  - Gross capture versus net removal is explained conceptually, but no quantitative net-removal accounting is provided for BECCS or DAC.
  - Waste-to-energy and other variants receive only brief treatment.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report is balanced and covers nearly all major pro and con arguments, with some critical qualification. It falls short of full depth because supporting evidence and distributional analysis are limited.
- Candidate evidence:
  - Supporting arguments include addressing unavoidable cement process emissions, supplying durable removals, preserving industrial competitiveness, retrofitting long-lived assets, and diversifying climate strategies.
  - Opposing arguments include the small and mixed project record, high costs, energy penalties, fossil lock-in, moral hazard, transport and storage risks, non-100% capture, uncertain utilization permanence, and competition from renewables and efficiency.
  - The report repeatedly distinguishes technically successful projects from broad economic scalability and states that subsidies should reward verified permanent storage rather than installed capacity.
- Missing:
  - Most arguments are not tied to specific studies, measured outcomes, or comparative empirical evidence despite the report’s selected-source list.
  - Equity and environmental-justice concerns are mentioned but not critically developed, including who bears risks and who receives benefits.
  - The treatment of public acceptance, health risks, and opportunity costs remains largely qualitative.
  - Scenario assumptions are acknowledged, but the report does not systematically distinguish evidence-based impacts from model-dependent claims.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report reaches a clear, conditional, well-synthesized judgment and separates current evidence from future scenarios. It needs a more explicit definition of significance and a more rigorous evaluation of the feasibility assumptions behind the mid-century estimate.
- Candidate evidence:
  - The executive conclusion states that CCS can contribute significantly but cannot substitute for fossil-fuel reduction and efficiency.
  - The final judgment targets hard-to-abate industry and removals, rejects CCS as a general license to continue emitting, and estimates a possible several-gigatonne annual contribution by mid-century.
  - It synthesizes performance, costs, energy penalties, scalability, permanence, applications, alternatives, and policy conditions including lifecycle accounting, verified storage, and avoiding mitigation delay.
  - It distinguishes what is demonstrated now—capture and storage in selected applications—from future-dependent outcomes such as multi-gigatonne deployment and low-cost DAC.
- Missing:
  - “Significant” is not defined with a clear quantitative threshold or explicit share of global emissions; the report gives several possible scales but does not establish which threshold it adopts.
  - The conclusion relies on projected gigatonne deployment without fully testing whether the necessary infrastructure, energy, finance, and permitting can be delivered within the stated timeframe.
  - Key uncertainties are acknowledged but not ranked or integrated into a conditional probability or confidence judgment.

### Novel Value

- The report’s most useful synthesis is its consistent distinction between smokestack capture rates, lifecycle emissions, gross capture, permanent removal, and nameplate versus delivered capacity.
- It provides a practical application hierarchy: strongest cases in cement, high-purity streams, industrial clusters, and carefully governed removals; weakest cases in unabated fossil-power continuation, old retrofits, and poorly accounted blue hydrogen or DAC.
- It combines technical, economic, infrastructure, governance, and moral-hazard considerations into a conditional rather than purely technological conclusion.

## Citations

### Support

### Missing Citations

- Q1: CCS has technically demonstrated the separation, transport, underground injection, and monitoring of CO₂, including at some industrial facilities operating at large scale.
- Q2: Existing facilities capture approximately 45–50 million tonnes of CO₂ per year, while energy- and industrial-process emissions are approximately 37 billion tonnes per year, making current capture roughly 0.1% of annual emissions.
- Q4: CCU does not necessarily provide permanent storage because some uses of captured CO₂ may later release the carbon back to the atmosphere.
- Q5: CO₂ capture from biomass or directly from air followed by permanent storage can constitute carbon dioxide removal, whereas capture from fossil-fuel or industrial processes generally prevents emissions rather than removing existing atmospheric CO₂.
- Q6: High-purity process streams, including natural-gas processing, hydrogen, ammonia, fertilizer, ethanol, and some chemical processes, are generally easier and less energy-intensive to capture than dilute power-plant exhaust.
- Q7: Amine-based post-combustion systems can commonly capture approximately 85–95% of CO₂ in the treated exhaust stream, depending on design and operation.
- Q8: Lifecycle emissions from fossil-fuel power plants with CCS include residual stack emissions, capture-energy emissions, upstream methane leakage, fuel-production emissions, infrastructure emissions, and possible venting or downtime.
- Q9: Under favorable conditions, fossil-fuel power plants with CCS may achieve roughly 70–90% lifecycle emissions reductions relative to unabated plants, while unfavorable conditions can produce substantially lower reductions.
- Q10: Sleipner has injected approximately 1 million tonnes of CO₂ per year into a saline formation since 1996.
- Q11: Snøhvit stores CO₂ separated from natural gas, and Quest has captured and stored roughly 1 million tonnes annually from hydrogen production since 2015.
- Q12: Boundary Dam 3 demonstrated coal-power capture, while Petra Nova captured CO₂ from a coal plant, ceased operation in 2020 amid adverse economic conditions, and later restarted for a period.
- Q13: Deep geological storage can retain CO₂ for centuries to millennia through structural, residual, dissolution, and mineral trapping mechanisms.
- Q14: Well-designed geological storage can achieve very high retention rates, but site characterization, monitoring, liability rules, and long-term stewardship are important challenges.
- Q15: Global operational CCS capture capacity is approximately 45–50 MtCO₂ per year, while energy and industrial-process emissions are roughly 37 GtCO₂ per year.
- Q16: Announced CCS projects could approach hundreds of millions of tonnes per year by 2030, with some inventories exceeding 400 MtCO₂ annually, but announced capacity substantially exceeds delivered capacity.
- Q17: Major climate scenarios commonly project hundreds of millions of tonnes of annual CCS by 2030 and approximately 1–7 GtCO₂ per year by 2050, depending on the pathway.
- Q18: Indicative CCS capture costs range from approximately $10–40 per tonne for high-purity streams to roughly $250–600 or more per tonne for current or early-commercial DAC, with transport and storage potentially adding approximately $10–30 per tonne in favorable clusters.
- Q19: In many markets, new gas or coal power plants with CCS cost more than new wind or solar generation, while retrofitting old coal plants is particularly difficult.
- Q20: DAC is expensive because atmospheric CO₂ concentration is approximately 0.04% of air and large quantities of air must be processed.
- Q21: Representative DAC energy requirements are roughly 5–10 GJ of heat and 0.5–1.5 GJ of electricity per tonne of CO₂.
- Q22: Power-plant CCS can reduce net electrical output by roughly 10–30%, increase fuel consumption per unit of electricity, and lower plant efficiency.
- Q23: Cement emissions arise substantially from the chemical calcination of limestone, so renewable energy alone does not eliminate cement process CO₂ and CCS is one potential option for addressing it.
- Q24: Blue hydrogen’s lifecycle emissions depend on capture rate, methane leakage, gas extraction and processing emissions, system boundaries, and how the energy penalty is supplied.
- Q25: Global saline aquifers and depleted hydrocarbon reservoirs could theoretically store many thousands of gigatonnes of CO₂, but usable capacity is constrained by characterization, injectivity, pressure, permitting, transport, monitoring, liability, and public acceptance.
- Q27: BECCS has constrained potential because of land, food, water, biodiversity, fertilizer, transport, carbon-accounting, and indirect-land-use-change considerations.
- Q28: CO₂ is nonflammable, but a major pipeline rupture can create an asphyxiation hazard by displacing oxygen; underground injection can also create pressure-related problems or induced seismicity.
- Q29: Some industrial process emissions, especially from cement calcination, are difficult to eliminate through renewable electricity or efficiency alone, making CCS potentially useful in those sectors.
- Q30: CCS can enable carbon removal through DAC with geological storage, BECCS, and potentially some carbon-negative industrial processes.
- Q31: CCS projects have a mixed record, including examples of underperformance, downtime, cost overruns, reliance on enhanced oil recovery, cancellations, and operation below nameplate capacity.
- Q32: In power generation, renewables, efficiency, storage, and grid investment frequently provide lower-cost emissions reductions than CCS on new or existing fossil plants, although this is not universally true for cement and some industrial processes.
- Q33: Captured CO₂ used in fuels, plastics, or enhanced oil recovery may eventually return to the atmosphere, so climate claims must distinguish permanent storage from temporary utilization and other pathways.

## Deterministic Checks

- `run_metadata_loads`: PASS
- `report_exists`: PASS
- `sources_present`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `structured_report_parses`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `report_question_matches`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `source_ids_unique`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `source_ids_syntactically_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `source_urls_present`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `evidence_objects_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `confidence_values_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `citation_ids_syntactically_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `citation_ids_resolve`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `structured_claim_evidence_available`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `ledger_claim_ids_unique`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `ledger_evidence_relationships_resolve`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `ledger_confidence_values_valid`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.
- `ledger_evidence_ids_unique`: NOT_APPLICABLE — Not applicable to the deliberate one-call LLM-only baseline.

## Main Weaknesses

1. R1: Evaluate the demonstrated effectiveness of CCS projects using measured evidence, distinguishing nameplate or design performance from actual captured and stored quantities, capture rates, operating availability, and net emissions reductions.
2. R2: Assess whether captured CO₂ can be transported, injected, monitored, and retained with sufficient safety and permanence to provide genuine climate mitigation.
3. 31 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `4b355a5b699abd7c1c1443375f23687623ff495a7eb9a683c06bcd344b1574b9`
- Candidate report hash: `851254b8c00de7026facc27e6f8261d6c3d1c01beab9940040614c455676fe0e`
- LLM calls: 2
- Evaluated at: 2026-08-31T23:40:42.961618+00:00
