# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** social-media-polarization

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 79.5 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.70
- Coverage: 0.76
- Depth: 0.57
- Citation quality: 0.91
- Citation validity: 1.00
- Citation support: 0.83
- Citation completeness: 1.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report recognizes that exposure and engagement are not identical to polarization and names several relevant outcomes, but it lacks an explicit conceptual definition and a systematic taxonomy of related outcomes.
- Candidate evidence:
  - The report distinguishes exposure from attitudes and behavior, stating that “algorithms should not be treated as the sole or universal cause of polarization.”
  - It separately discusses “affective polarization,” “self-reported partisanship,” issue opinions, political knowledge, engagement, and following behavior.
  - It notes that “like-minded content itself may matter more than algorithmic selection.”
- Missing:
  - It never directly defines political polarization or clearly distinguishes ideological extremity, partisan identity, affective polarization, and behavioral polarization as separate constructs.
  - The distinction from related outcomes such as media diversity, ideological exposure, and general political activity is incomplete.
  - It sometimes uses “polarization” broadly while reporting issue-attitude and following effects, without specifying which outcomes count as polarization.

### R2

- Coverage: 1.00
- Depth: 0.75
- Rationale: This requirement is substantially and directly addressed with evidence on ranking, amplification, exposure, and visibility, plus an important distinction between algorithmic selection and user/network processes. Minor omissions concern the full range of non-algorithmic exposure mechanisms and evidence types.
- Candidate evidence:
  - It states that “recommendation algorithms clearly change what users see and whose political content receives visibility.”
  - It reports the randomized Twitter/X finding that algorithmic personalization amplified mainstream right-wing political content more than mainstream left-wing content in six of seven countries.
  - It reports that replacing personalized Facebook/Instagram ranking with chronological feeds changed exposure to political, untrustworthy, uncivil, slur-containing, moderate, and ideologically mixed content.
  - It explicitly distinguishes ranking from “users’ prior preferences, network composition, and exposure to like-minded content.”
- Missing:
  - The report gives limited discussion of content supply and the distinction between recommendation effects and users’ follows, clicks, searches, or subscriptions beyond general references to user choice and following.
  - It does not discuss audits or observational evidence in detail, focusing mainly on randomized platform experiments.

### R3

- Coverage: 1.00
- Depth: 0.75
- Rationale: The report clearly evaluates beliefs and attitudes separately, gives direction and one concrete effect size, and reports null findings. It falls short of full depth because statistical precision and substantive interpretation are incomplete.
- Candidate evidence:
  - It separates feed composition from downstream outcomes and concludes that effects on beliefs are “real but mixed and outcome-specific.”
  - It reports that a seven-week randomized X experiment shifted conservative policy priorities and several issue opinions but produced no significant change in affective polarization or self-reported partisanship.
  - It reports a reranking effect of 2.11 points of increased opposing-party warmth and a 2.48-point reduction when partisan-animosity exposure increased, on a 100-point scale.
  - It reports that the Facebook/Instagram experiment found no significant change in issue polarization, affective polarization, political knowledge, or other key attitudes despite substantial exposure changes.
- Missing:
  - Most reported effects lack confidence intervals, standard errors, or fuller statistical uncertainty information.
  - The report does not consistently assess substantive importance beyond the one 100-point warmth estimate.
  - It does not establish whether the issue-attitude changes reflect persuasion, salience, or selective following, although it identifies this as an unresolved gap.

### R4

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report appropriately covers online behavior and is explicit that offline political effects remain unestablished. It does not fully evaluate the broader behavioral domain or characterize behavioral effect sizes and uncertainty in depth.
- Candidate evidence:
  - It distinguishes on-platform behavior from consequential political behavior, stating that algorithms changed “engagement, time spent, and following.”
  - It reports reduced time and activity after moving users to chronological Facebook/Instagram feeds and increased engagement and conservative-account following under the X algorithmic feed.
  - It explicitly states that the evidence does not establish effects on voting, turnout, donations, offline activism, or offline hostility.
- Missing:
  - Sharing, political participation, and other politically relevant behaviors are mentioned mainly as gaps rather than evaluated.
  - The report does not provide a detailed causal assessment of the behavioral findings or quantify their magnitude except indirectly through the cited studies.
  - The targeted-advertising turnout example is carefully excluded from recommendation effects, but it does not add direct evidence about recommendation-driven offline behavior.

### R5

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes randomization and several major confounds, but its treatment of research designs and causal threats is incomplete and not systematic enough for full coverage.
- Candidate evidence:
  - It identifies the evidence as including “randomized platform experiments with direct measures of feed content.”
  - It distinguishes randomized feed assignment, reranking, and chronological-feed substitutions across the X and Facebook/Instagram studies.
  - It notes confounding or alternative mechanisms involving “users’ prior preferences, network composition,” self-selection, resharing, and user choice.
  - It describes the targeted-advertising study as mechanistically distinct from feed recommendation and notes that its source is a university news report rather than the primary study.
- Missing:
  - It does not systematically distinguish randomized interventions from audits, observational studies, surveys, or simulations.
  - Important threats such as noncompliance, treatment contamination, measurement error, attrition, and interference through networks are not examined in detail.
  - The causal estimands and limitations of each design are only partially articulated.

### R6

- Coverage: 0.75
- Depth: 0.50
- Rationale: There is a meaningful cross-platform and cross-intervention comparison, but the scope analysis is incomplete, especially for country/language variation, simulations, audits, and detailed population comparisons.
- Candidate evidence:
  - It compares X with Facebook/Instagram and contrasts algorithmic-feed assignment, reranking, and replacement of personalized ranking with chronological feeds.
  - It explains that X studies promoted particular conservative, partisan, or antidemocratic content, whereas the Facebook/Instagram intervention did not target a specific political-content category.
  - It identifies differences in platforms, algorithms, content environments, durations, user populations, and outcomes.
  - It acknowledges limited generalizability beyond active U.S. X users and the specific 2023 political context.
- Missing:
  - Country, language, election timing, and platform-design differences are not actually compared in detail, despite being listed as possible explanations.
  - The report does not discuss simulated environments or audits in substantive detail.
  - Population differences and election-context differences remain mostly in the Remaining Gaps section rather than being tied to specific results.

### R7

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report acknowledges heterogeneity and time horizons and appropriately flags uncertainty, but it does not assess these dimensions in much empirical detail.
- Candidate evidence:
  - It reports persistence in some on-platform effects after users returned to chronological feeds.
  - It says the evidence does not determine whether short-term attitude changes accumulate into durable ideological polarization or electoral effects.
  - It identifies possible concentration of effects among highly engaged, initially conservative, or already polarized users as an unresolved question.
  - It mentions feedback loops, changing algorithms, user preferences, and broader social dynamics.
- Missing:
  - The report provides little evidence-supported analysis of actual subgroup, content, or exposure-intensity heterogeneity.
  - Long-term accumulation and feedback mechanisms are mostly presented as possibilities or gaps, not evaluated evidence.
  - It does not distinguish clearly between demonstrated persistence of following behavior and speculative persistence of polarization or belief change.

### R8

- Coverage: 1.00
- Depth: 0.75
- Rationale: The report provides a well-calibrated overall synthesis and directly answers the central comparison between exposure effects and downstream belief or behavior effects. Some methodological explanations and effect-size interpretation remain underdeveloped.
- Candidate evidence:
  - It explains disagreement through different platforms, algorithms, content environments, durations, populations, and outcomes rather than treating the literature as simply contradictory.
  - It separately concludes that evidence is strongest for changes in visibility and exposure, mixed for beliefs, and insufficient for consequential political behavior.
  - It preserves important scope conditions: X produced selected issue-attitude and following effects, Facebook/Instagram produced substantial exposure changes but null polarization-attitude effects, and like-minded content may matter more than algorithmic selection.
  - It explicitly states that ordinary recommendation algorithms are not established as consistently changing voting or turnout.
- Missing:
  - The synthesis does not discuss statistical power, detectable effect thresholds, or measurement differences in much detail.
  - The phrase “meaningful but conditional extent” is somewhat under-justified and could more explicitly distinguish the contribution to polarization from the broader contribution to exposure and political visibility.
  - The explanation of disagreement could more clearly separate causal estimands and treatment compliance across studies.

### Novel Value

- The report offers a useful conditional synthesis rather than equating algorithmic exposure changes with polarization itself.
- It highlights the asymmetry in the X evidence: turning the algorithm on produced some attitude and following effects, while turning it off did not produce comparable reversals, plausibly because promoted accounts had already been followed.
- It separates ordinary feed recommendation from targeted political advertising and avoids using the latter as direct evidence of recommendation-driven turnout effects.
- It identifies a coherent cross-platform explanation for disagreement: directional content and algorithmic assignment on X versus chronological substitution on Facebook/Instagram, combined with different outcomes and time horizons.

## Citations

### Support

#### F1: SUPPORTED

- Claim: Recommendation algorithms clearly change what users see and whose political content receives visibility.
- Sources: S6, S8, S9, S10, S11, S16, S19
- Rationale: The saved sources directly support both parts of the claim. They report that algorithmic feeds rank and order content, that replacing them with chronological feeds changes users’ exposure, and that algorithmic amplification differs across political sources. The evidence is especially direct for Twitter/X and Meta feed-ranking systems, so the claim is best understood in that platform-specific context.
- Supporting text: S6/S8/S9/S10: Twitter’s personalized algorithms rank some political content higher and provide higher amplification to mainstream right-wing political and news sources. S11: moving Facebook and Instagram users to chronological feeds substantially changed the political, ideological, and other content they saw. S16/S19: on X, the algorithm was reported to promote conservative content and demote posts by traditional media.

#### F2: SUPPORTED

- Claim: Algorithms can change some political beliefs or issue attitudes, but the effect is selective and context-dependent rather than a general increase in polarization.
- Sources: S16, S19, S1, S4, S11
- Rationale: The saved sources support both components of the claim. S16/S19 report that switching to X’s algorithmic feed shifted some political opinions—especially policy priorities, views of Trump-related investigations, and the war in Ukraine—but did not significantly affect affective polarization or self-reported partisanship. S4 likewise finds small, topic-specific effects on attitude polarization, while algorithmic curation did not generally amplify polarization. S11 finds that changing Facebook and Instagram feeds substantially altered exposure and behavior but did not significantly change issue or affective polarization or other key attitudes over three months. S1 reports causal effects on partisan hostility, but its commentary framing is broader and less directly necessary than the experimental findings in the other sources.
- Supporting text: S16: “shifted political opinion towards more conservative positions, particularly regarding policy priorities… [and] views on the war in Ukraine,” while “neither switching the algorithm on nor switching it off significantly affected affective polarization.” S4: algorithmic curation “did not amplify” polarization effects and produced only “small direct effects on attitude polarization.” S11: the chronological feed “did not significantly alter levels of issue polarization, affective polarization… or other key attitudes.”

#### F3: PARTIALLY_SUPPORTED

- Claim: Algorithms change on-platform behavior, but evidence that ordinary recommendation feeds change consequential political behavior is limited.
- Sources: S11, S16, S19, S20, S6, S8, S9, S10
- Rationale: The sources strongly support that recommendation algorithms alter on-platform behavior and exposure: S11 reports substantial changes in time spent, activity, and content exposure after replacing algorithmic feeds, while S16/S19/S20 report increased engagement and changes in account-following behavior on X. They also support limited effects in some ordinary-feed experiments: S11 found no significant changes in several political attitudes over three months, and S16/S19 describe no comparable effects when switching from algorithmic to chronological feeds. However, the broad claim that evidence of consequential political-behavior effects is limited is too general: S16/S19/S20 report that switching on X’s algorithm shifted political opinions and policy priorities and increased following of conservative activist accounts. The saved text concerns attitudes, policy priorities, and online following rather than clearly consequential offline political behavior, so it supports only a narrower version.
- Supporting text: S11: replacing the default feed “substantially decreased the time they spent on the platforms and their activity,” but “did not significantly alter” key political attitudes. S16/S19: switching to an algorithmic X feed “increased engagement and shifted political opinion,” while switching it off had no comparable effects.

#### F4: PARTIALLY_SUPPORTED

- Claim: Evidence of effects on voting behavior exists for targeted political advertising, but it should not be conflated with recommendation-algorithm effects.
- Sources: S14
- Rationale: S14 directly supports evidence that targeted political advertising affected voting behavior, reporting that participants exposed to vote-suppressing Facebook ads were 1.9% less likely to vote. However, the source does not explicitly establish or discuss a distinction between targeted advertising effects and recommendation-algorithm effects, so the non-conflation qualification is not supported by this citation.
- Supporting text: The study found that participants who saw vote-suppressing Facebook ads were 1.9% less likely to vote than those who did not; the ads used Facebook’s microtargeting advertising features.

#### F5: SUPPORTED

- Claim: Like-minded exposure and preexisting social dynamics may be more important than algorithmic selection alone in producing polarization.
- Sources: S4, S15, S11
- Rationale: The sources collectively support the claim as a qualified comparative conclusion. S4 reports that like-minded exposure increased attitude and affective polarization more strongly than opposing exposure, while algorithmic selection did not amplify those effects and had only small direct effects. S15 states that algorithms mostly reinforce existing social drivers. S11 reports that substantially changing feed algorithms did not significantly alter polarization, and identifies user choice and network composition as potentially relevant determinants beyond algorithmic ranking.
- Supporting text: S4: “Exposure to like-minded arguments increased participants’ attitude polarization and affective polarization more intensely than exposure to opposing arguments,” but these effects “were not amplified by algorithmic selection.” S15: “Existing evidence suggests that algorithms mostly reinforce existing social drivers.” S11: The chronological feed “did not significantly alter levels of issue polarization [or] affective polarization,” while “user choice or the composition of one’s network” could also matter.

#### F6: SUPPORTED

- Claim: The apparent disagreement in the literature reflects different estimands and experimental environments rather than one settled universal effect.
- Sources: S1, S11, S16, S4, S19, S20
- Rationale: The saved sources document divergent findings across platforms, interventions, outcomes, and study periods: S11 reports no significant changes in several political attitudes when users moved from algorithmic to chronological feeds on Facebook and Instagram, while S16/S19/S20 report conservative opinion shifts when users were moved from chronological to algorithmic feeds on X, with no comparable effect on affective polarization or partisanship. S4 likewise finds that like-minded exposure increased polarization but algorithmic selection did not generally amplify it. Together, these differences support the claim that results vary with the estimand and experimental environment, rather than establishing one universal effect.
- Supporting text: S11: the chronological feed changed exposure and on-platform behavior but “did not significantly alter levels of issue polarization, affective polarization, political knowledge, or other key attitudes.” S16/S19: switching from chronological to algorithmic feeds on X shifted political opinion toward more conservative positions, while the reverse switch had no comparable effects and did not significantly affect affective polarization or self-reported partisanship. S4: empirical evidence was “inconsistent at best”; like-minded exposure increased polarization, but algorithmic selection generally did not amplify those effects.

### Missing Citations

- None identified.

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

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `0a6b1b066d5fe11922b29a875e67b54f06d262533b8526272d8d350999e2c54e`
- Candidate report hash: `c21b9e23b1df549b201f36f672354d6666ecf405292beb3c8ad2778c23a9801b`
- LLM calls: 8
- Evaluated at: 2026-09-01T09:26:33.541717+00:00
