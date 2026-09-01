# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** social-media-polarization

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 70.3 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.60
- Coverage: 0.62
- Depth: 0.55
- Citation quality: 0.82
- Citation validity: 1.00
- Citation support: 0.83
- Citation completeness: 0.69
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.25
- Depth: 0.25
- Rationale: The report recognizes that exposure changes are not identical to polarization, but it does not provide the requested conceptual definition or systematic distinctions among related outcomes.
- Candidate evidence:
  - The report distinguishes exposure from downstream outcomes, stating that algorithms change users’ “political-information environments” while belief and polarization effects are “more conditional.”
  - It separately lists affective polarization, issue polarization, policy attitudes, knowledge, partisanship, and engagement as outcomes.
- Missing:
  - It never defines political polarization or clearly distinguishes affective polarization, ideological extremity, partisan identity, and behavioral polarization.
  - It does not explicitly distinguish polarization from ideological exposure, media diversity, political knowledge, partisan following, engagement, or general political activity.
  - The conceptual distinction is implied rather than developed, and some listed outcomes are not polarization measures.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is one of the report’s strongest sections: it provides concrete experimental evidence and acknowledges that exposure effects can run in different ideological directions, but it does not fully disentangle algorithmic ranking from user and network processes.
- Candidate evidence:
  - It states that recommendation systems alter “ranking, prominence, sequencing, content mix, engagement, and sometimes which accounts users follow.”
  - It reports randomized Meta and X interventions changing exposure to ideological, uncivil, untrustworthy, moderate, mixed, and traditional-media content.
  - It reports that on X, algorithmic exposure promoted conservative content, demoted traditional-media posts, increased engagement, and increased following of conservative activist accounts.
  - It contrasts personalized and chronological feeds and notes that ranking changes can increase exposure to moderate and ideologically mixed sources as well as political or untrustworthy content.
- Missing:
  - The distinction between algorithmic effects and user follows, clicks, searches, subscriptions, and network composition is only partial; these user-driven inputs are mentioned mainly as feedback signals.
  - There is little direct discussion of observational audits, content supply, or the size and uncertainty of exposure effects.
  - The report does not consistently separate changes caused by ranking from changes caused by recommendation, account networks, or users’ own choices.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report clearly separates feed composition from attitudes and presents both positive and null findings with some magnitude information. Its treatment is substantial but not fully quantitative or methodologically detailed.
- Candidate evidence:
  - It reports an X experiment producing shifts toward more conservative policy priorities and selected political perceptions but no significant change in affective polarization or self-reported partisanship.
  - It reports a reranking experiment changing feelings toward the opposing party by roughly two points on a 100-point scale after one week.
  - It reports that like-minded exposure increased attitude and affective polarization, while algorithmic selection generally did not amplify that effect, apart from a small topic-specific attitude-polarization effect.
  - It reports that the three-month Meta/Facebook and Instagram intervention changed exposure without significant changes in issue polarization, affective polarization, political knowledge, or related attitudes.
- Missing:
  - Statistical uncertainty is described mostly through significance/no-significance; confidence intervals, precision, power, and uncertainty around the reported effect sizes are not supplied.
  - The report gives only one approximate magnitude and does not consistently characterize substantive importance across outcomes.
  - It does not fully clarify whether the X reranking result was an effect on polarization itself, a specific affect measure, or a broader attitudinal outcome.

### R4

- Coverage: 0.75
- Depth: 0.50
- Rationale: It correctly avoids inferring voting or participation effects from exposure and identifies some online behavioral results. However, behavioral evidence is treated mainly as an evidentiary gap rather than evaluated in depth.
- Candidate evidence:
  - It states that the supplied evidence does not establish effects on voting, turnout, protest, donations, or offline participation.
  - It distinguishes measured platform engagement and account-following behavior from consequential political action.
  - It reports increased engagement and following of conservative activist accounts in the X experiment, and reduced time spent and activity in the Meta chronological-feed intervention.
- Missing:
  - The report does not systematically evaluate online political behaviors such as sharing, posting, following, or participation beyond a few examples.
  - It provides little detail about whether observed engagement or following changes are politically consequential, their magnitudes, or their uncertainty.
  - It appropriately notes that offline behavioral evidence is limited, but does not distinguish causal evidence for each behavioral outcome.

### R5

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes experimental versus observational reasoning and mentions several confounders, but it does not provide the requested systematic methodological comparison or detailed threat assessment.
- Candidate evidence:
  - It identifies randomized feed interventions, X reranking experiments, comparisons of algorithmically selected and randomly selected material, and observational or review-style evidence.
  - It notes self-selection, social networks, content choices, other media, nonuniform platform environments, and difficulty attributing long-term effects.
  - It distinguishes direct feed interventions from broader claims that personalization or engagement optimization causes polarization.
- Missing:
  - Audits, surveys, and simulations are not clearly differentiated or evaluated.
  - Important threats such as noncompliance, treatment contamination, attrition, network spillovers, content-supply changes, and measurement error are not developed; attrition and compliance are only listed as unavailable details in the gaps section.
  - The relative causal strength of each design is not explicitly ranked or explained.
  - The report does not explain whether chronological substitutions, reranking, and algorithm-versus-random-selection treatments identify different causal estimands.

### R6

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report covers the main dimensions of variation and gives useful platform/intervention contrasts, but the comparative explanation is more enumerative than analytical.
- Candidate evidence:
  - It states that results vary by platform, election context, country, duration, participant population, algorithm version, and whether ranking alone or the broader social-media environment is changed.
  - It contrasts Meta/Facebook and Instagram chronological-feed interventions with X feed and reranking experiments and with algorithmic-selection versus like-minded-exposure experiments.
  - It notes that ranking can produce moderate or mixed exposure in some settings and conservative or antagonistic exposure in others.
- Missing:
  - The report largely lists contextual differences without explaining how particular differences in country, language, election timing, user composition, or platform design generate different results.
  - It does not provide concrete comparative findings across multiple countries or language settings.
  - Simulated environments and audits are not substantively compared with real-world feed interventions.
  - The account of platform and intervention differences remains somewhat generic.

### R7

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report acknowledges heterogeneity and temporal uncertainty, but offers little actual assessment of who is affected, under what exposure conditions, or whether effects persist.
- Candidate evidence:
  - It describes effects as “narrow and heterogeneous” and says results differ by platform, content, intervention, duration, and outcome.
  - It identifies unresolved questions about persistence over months or years, generalization to less politically engaged users, and subgroup effects.
  - It notes feedback between user preferences, networks, interactions, and algorithmic curation.
- Missing:
  - There is no concrete evidence about subgroup differences across users, content types, exposure intensity, or political predispositions.
  - Cumulative effects, persistence, and feedback loops are raised mostly as possibilities or unresolved questions rather than assessed with evidence.
  - The report does not distinguish evidence-supported heterogeneity from speculative long-term accumulation mechanisms.
  - Changing algorithms and external validity are mentioned but not analyzed in relation to time horizons.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report provides a nuanced and generally well-calibrated synthesis, explains several major sources of divergent findings, and avoids a sweeping causal conclusion. It falls short of a fully comprehensive synthesis because conceptualization, statistical precision, relative contribution, and effect-size interpretation remain underdeveloped.
- Candidate evidence:
  - It concludes that exposure effects are strongly supported while downstream effects are conditional and not uniform.
  - It explains disagreement through different interventions, platforms, endpoints, time horizons, samples, election contexts, and algorithm versions.
  - It explicitly contrasts short-term X effects with null or outcome-specific Meta and other experimental results.
  - It concludes that algorithms are “socio-technical amplifiers and organizers of political exposure” rather than uniformly or primarily causing polarization, and states that consequential political behavior remains unestablished.
- Missing:
  - The explanation does not explicitly discuss differences in statistical power, precision, or effect-size thresholds as sources of disagreement.
  - It does not fully quantify the overall extent of contribution or compare algorithmic effects with other causes of polarization.
  - Some causal claims, such as algorithms “meaningfully” contributing to polarization risk, are broader than the presented outcome-specific evidence and are not tied to a clearly defined polarization construct.
  - The synthesis could more sharply separate exposure, attitudes, online behavior, and offline behavior in the final calibrated assessment.

### Novel Value

- The report’s most useful synthesis is its consistent separation of large, experimentally demonstrated changes in feed exposure from smaller, conditional, and sometimes null downstream attitude effects.
- It usefully combines positive, null, and outcome-specific findings across Meta and X rather than treating algorithmic influence as uniformly polarizing.
- It appropriately identifies consequential political behavior as an unresolved evidentiary boundary instead of inferring it from engagement or exposure changes.

## Citations

### Support

#### F1: SUPPORTED

- Claim: Recommendation algorithms clearly change what users see, even when content is not removed.
- Sources: S4, S7, S11
- Rationale: The saved sources directly support that recommendation or feed-ranking algorithms alter content visibility and exposure without stating that the content is removed. S4 explains that algorithms rank, filter, and recommend content, determining what emerges and receives visibility. S7 reports an experiment in which replacing default algorithmic feeds with chronological feeds substantially changed participants’ exposure to political, untrustworthy, uncivil, and moderate content. S11 likewise finds that X’s algorithm promotes conservative content and demotes traditional-media posts. Together, these findings clearly support the claim’s important factual content.
- Supporting text: S4: Algorithms “categorise, rank, filter, and recommend content,” influencing what receives visibility. S7: Changing to chronological feeds “affected exposure to content,” including increases or decreases in several content categories. S11: The X algorithm “promotes conservative content and demotes posts by traditional media.”

#### F2: SUPPORTED

- Claim: Changes in exposure can produce measurable changes in political attitudes or affect, but the effects are narrow and heterogeneous rather than a uniform increase in polarization.
- Sources: S11, S5, S20, S12
- Rationale: The sources support both parts of the claim. S11 reports that changing exposure to X’s algorithm shifted political opinions on particular issues, while not significantly affecting affective polarization or self-reported partisanship, and describes asymmetric effects depending on the direction of the feed change. S12 similarly finds that like-minded exposure increased attitude and affective polarization more than opposing exposure, but algorithmic selection did not generally amplify those effects and produced only a small direct effect for one topic. S5 and S20 report measurable but modest changes in affective polarization from increased versus decreased exposure. Together, these findings indicate measurable effects that vary by exposure type, outcome, and topic rather than a uniform increase in polarization.
- Supporting text: S11: “Switching from a chronological to an algorithmic feed increased engagement and shifted political opinion towards more conservative positions” but “neither switching the algorithm on nor switching it off significantly affected affective polarization.” S12: “Exposure to like-minded arguments increased participants’ attitude polarization and affective polarization,” while algorithmic curation “did not amplify these effects” and had only “small direct effects on attitude polarization.”

#### F3: SUPPORTED

- Claim: Large changes in users’ on-platform experience do not necessarily change polarization or political knowledge.
- Sources: S7
- Rationale: S7 directly reports substantial changes in users’ on-platform experience after switching to chronological feeds, while finding no significant changes in issue polarization, affective polarization, or political knowledge during the three-month study.
- Supporting text: “Despite these substantial changes in users’ on-platform experience, the chronological feed did not significantly alter levels of issue polarization, affective polarization, political knowledge, or other key attitudes.”

#### F4: SUPPORTED

- Claim: Algorithms are better characterized as structuring and sometimes amplifying existing political tendencies than as independently creating polarization from nothing.
- Sources: S1, S4, S7, S13, S17, S11, S12, S21
- Rationale: The saved sources collectively support the claim. S1 explicitly says algorithms mostly reinforce existing social drivers. S13 describes polarization-related effects as emergent from human–algorithm interactions rather than attributable solely to either users or algorithms. S7 and S17 report that changing Meta’s feed algorithms substantially altered exposure and on-platform experiences but did not significantly change polarization or key political attitudes, while S17 says algorithms make it easier for users to pursue what they are already inclined to do. S12 similarly finds that like-minded exposure increased polarization, but algorithmic selection generally did not amplify that effect, aside from a small direct effect for one topic. S11 provides a qualification: X’s algorithm shifted some political opinions, although it did not significantly affect affective polarization or partisanship. Thus, the evidence supports a nuanced characterization of algorithms as structuring exposure and sometimes amplifying or influencing existing tendencies, not as independently generating polarization from nothing.
- Supporting text: S1: “Existing evidence suggests that algorithms mostly reinforce existing social drivers.” S13: “Many pathologies of social media are attributed either to human behavior or to the algorithms ... when they are in fact the result of both”; these are “emergent effects of human-algorithm interactions.” S17: algorithms help users by “making it easier for people to do what they’re inclined to do.” S7: changing to chronological feeds did not significantly alter issue or affective polarization. S12: like-minded arguments increased polarization, but these effects “were not amplified by algorithmic selection,” with only a slight topic-specific direct effect.

#### F5: PARTIALLY_SUPPORTED

- Claim: The supplied evidence does not establish that recommendation algorithms change consequential political behavior.
- Sources: S7, S11, S12, S17, S20
- Rationale: S7 and S17 support the narrower conclusion that changing Meta’s feed algorithms did not significantly alter several measured political attitudes during a short 2020-election study, while S12 reports only small or limited polarization effects. However, S11 directly reports that switching on X’s algorithm shifted political opinion and account-following behavior, and S20 describes causal changes in political attitudes from reranking X feeds. The sources therefore do not support the broad claim that the evidence does not establish algorithmic effects on consequential political behavior.
- Supporting text: S7: the chronological feed “did not significantly alter levels of issue polarization, affective polarization, political knowledge, or other key attitudes” over three months. S17: changing Facebook’s algorithms produced “little impact on polarization,” with limitations including the short study period.

#### F6: PARTIALLY_SUPPORTED

- Claim: The literature reaches different conclusions because studies estimate different causal effects rather than one common phenomenon called algorithmic polarization.
- Sources: S5, S7, S11, S12, S6, S17, S13
- Rationale: The sources support the narrower point that studies examine different interventions, platforms, outcomes, and mechanisms, producing differing findings. S7 compares algorithmic versus chronological feeds and finds no significant change in several polarization measures; S11/S6 reports that X’s algorithm shifted some political opinions but not affective polarization or partisanship; and S12 distinguishes exposure to like-minded content from the effects of algorithmic selection. However, the sources do not explicitly establish the broader causal explanation that the literature reaches different conclusions because of these differences, nor do they directly reject a single common phenomenon called “algorithmic polarization.”
- Supporting text: S7: the study changed feed ranking and found no significant effects on issue or affective polarization. S11/S6: switching to an algorithmic X feed shifted political opinion but did not significantly affect affective polarization or partisanship. S12: like-minded exposure increased polarization, while algorithmic selection generally did not amplify that effect. S13: observed effects can emerge from interactions between platform design and user behavior, and there are many different social-media algorithms.

### Missing Citations

- Q1: Recommendation systems change users’ political-information environments by altering ranking, prominence, sequencing, content mix, engagement, and sometimes which accounts users follow.
- Q2: Evidence that recommendation systems change political beliefs or polarization is more conditional than evidence that they change exposure.
- Q3: Some experiments find short-term changes in affective polarization or selected policy attitudes, while others find no significant change in issue polarization, affective polarization, knowledge, or partisanship despite substantial exposure changes.
- Q4: The supplied studies do not establish effects on consequential political behavior such as voting, turnout, protest, donations, or offline participation.
- Q23: Recommendation algorithms make a meaningful contribution to polarization risk by determining which political content becomes prominent and by sometimes reinforcing or redirecting users’ existing tendencies.
- Q24: Some interventions change affective polarization or selected policy attitudes, while others produce no detectable change in polarization despite large exposure effects.
- Q25: The supplied evidence supports viewing algorithms as socio-technical amplifiers and organizers of political exposure that interact with user preferences, networks, content supply, and broader media environments.
- Q26: Effects of recommendation algorithms on consequential political behavior remain unestablished on the supplied evidence.

## Deterministic Checks

- `run_metadata_loads`: PASS
- `report_exists`: PASS
- `sources_present`: PASS
- `structured_report_parses`: PASS
- `report_question_matches`: PASS
- `source_ids_unique`: PASS
- `source_ids_syntactically_valid`: PASS
- `source_urls_present`: PASS
- `evidence_objects_valid`: PASS
- `confidence_values_valid`: PASS
- `citation_ids_syntactically_valid`: PASS
- `citation_ids_resolve`: PASS
- `structured_claim_evidence_available`: NOT_EVALUABLE — This run predates or does not use an evidence ledger.
- `ledger_claim_ids_unique`: NOT_EVALUABLE — Evidence ledger unavailable.
- `ledger_evidence_relationships_resolve`: NOT_EVALUABLE — Evidence ledger unavailable.
- `ledger_confidence_values_valid`: NOT_EVALUABLE — Evidence ledger unavailable.
- `ledger_evidence_ids_unique`: NOT_EVALUABLE — Evidence ledger unavailable.

## Main Weaknesses

1. R1: Define political polarization and distinguish it from related outcomes such as ideological exposure, engagement, media diversity, political knowledge, partisan following, or general political activity.
2. R5: Distinguish the causal strength and limitations of the main types of evidence.
3. R7: Assess whether effects vary across users, content, outcomes, exposure intensity, and time horizons.
4. 2 cited finding(s) were not fully supported by saved evidence.
5. 8 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `0a6b1b066d5fe11922b29a875e67b54f06d262533b8526272d8d350999e2c54e`
- Candidate report hash: `412fd95c37a3e422f9e59c39452ca995071fbe6f2637e221b6890487917f38aa`
- LLM calls: 8
- Evaluated at: 2026-09-01T08:31:33.608947+00:00
