# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** social-media-polarization

**System Version:** evidence-ledger-v1

**Model:** gpt-5.6-luna

## Summary

- Overall: 74.0 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.61
- Coverage: 0.63
- Depth: 0.55
- Citation quality: 0.92
- Citation validity: 1.00
- Citation support: 0.90
- Citation completeness: 0.92
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report recognizes that altered exposure is not equivalent to changed polarization and mentions several relevant outcomes, but it does not provide the requested conceptualization in a systematic or sufficiently developed way.
- Candidate evidence:
  - The report distinguishes exposure changes from polarization, stating that algorithms contribute to polarization only in the “limited sense that they alter the political material users encounter.”
  - It identifies “affective polarization,” “attitude polarization,” political knowledge, and behavior as distinct outcomes.
- Missing:
  - It does not explicitly define political polarization or clearly distinguish ideological extremity, partisan identity, behavioral polarization, ideological exposure, media diversity, engagement, and general political activity.
  - The conceptual distinction between exposure and polarization is asserted but not developed with a clear framework or operational definitions.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report provides substantial evidence that feed ranking changes exposure and acknowledges user-driven and network-based alternatives. It would be stronger with more precise evidence about the content changes and a more explicit decomposition of algorithmic ranking versus user selection and content supply.
- Candidate evidence:
  - Finding 1 states that ranking and recommendation algorithms can change what political content users see or encounter first even when the underlying pool of posts or followed accounts is unchanged.
  - It cites a browser-extension intervention that reranked existing X posts while leaving the same posts available.
  - It describes a randomized Facebook/Instagram intervention replacing algorithmic ranking with chronological ordering and changing the amount and type of political, ideological, uncivil, and other content encountered.
  - Finding 5 notes that personalization, likes, shares, comments, watch time, follows, searches, prior engagement, user choices, and network composition also influence exposure.
- Missing:
  - The report gives limited detail about the direction and magnitude of ideological slant, cross-cutting exposure, amplification, or content-supply effects.
  - It does not systematically distinguish recommendation effects from each of follows, clicks, searches, subscriptions, and network composition, although several of these are mentioned.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is one of the strongest parts of the report: it separates feed composition from downstream attitudes, gives contrasting positive and null findings, and addresses direction, approximate magnitude, and duration. Statistical uncertainty and the range of attitudinal constructs are not treated in comparable detail.
- Candidate evidence:
  - Finding 2 reports that two experiments found like-minded exposure increased attitude and affective polarization, while algorithmic selection generally did not amplify those effects and produced only a slight additional attitude-polarization effect for one topic.
  - It reports approximately two-point shifts in feelings toward the opposing party after one week in the X reranking experiment.
  - It contrasts those results with a large randomized Facebook/Instagram intervention that substantially changed exposure, time spent, and activity but found no significant changes over three months in issue polarization, affective polarization, political knowledge, or other key attitudes.
  - The report explicitly characterizes effects as modest, short-term, context-dependent, and not consistently large or general.
- Missing:
  - It provides little information about confidence intervals, statistical power, effect uncertainty, or the substantive interpretation of the reported two-point shift.
  - It does not consistently separate effects on policy beliefs, ideological extremity, partisan identity, and affective polarization.

### R4

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report appropriately refuses to infer behavioral effects from exposure and clearly states that direct causal evidence is limited. However, its evaluation of the behavioral outcomes themselves is relatively thin.
- Candidate evidence:
  - Finding 4 states that the evidence does not establish durable changes in voting, participation, sharing, following, or offline political action.
  - It reports that the three-month Facebook/Instagram intervention did not notably affect reported off-platform behaviors.
  - It distinguishes a cross-national study associating general social-media use with online political participation from algorithm-specific causal evidence.
- Missing:
  - The report does not provide much direct evidence on algorithm-induced sharing, following, engagement, time spent, voting, or participation beyond the limited off-platform null finding.
  - It mentions changes in time spent and activity in the Facebook/Instagram intervention but does not clarify whether these were politically relevant behavioral outcomes or provide their direction and size.
  - It does not distinguish online behavior, offline behavior, and political behavior measures in a detailed evidence comparison.

### R5

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report makes a useful basic distinction between experiments and correlational studies and identifies several major confounds. Its treatment of the full range of designs and experiment-specific threats is incomplete.
- Candidate evidence:
  - The report identifies two experiments, an X reranking experiment, and a randomized Facebook/Instagram chronological-feed intervention as causal evidence.
  - It characterizes a cross-national study and evidence linking social-media use to offline participation as correlational rather than algorithm-specific causal evidence.
  - It notes threats from self-selection, personalization, users’ choices, network composition, reciprocal algorithm-user influence, and difficulty separating like-minded exposure from algorithm effects.
- Missing:
  - It does not distinguish the causal strengths and limitations of audits, simulations, surveys, or other evidence types, and does not discuss whether such designs were used or absent.
  - Important threats such as noncompliance, treatment contamination, measurement error, attrition, and limited statistical power are not addressed.
  - The report does not explain in detail how chronological substitutions, reranking, and targeted content manipulations differ in causal interpretation.

### R6

- Coverage: 0.50
- Depth: 0.50
- Rationale: It correctly identifies several dimensions of variation and avoids overgeneralization, but the requirement calls for comparative explanation across settings; the report mainly lists those differences and labels them gaps.
- Candidate evidence:
  - The report says positive and null findings are not directly comparable because studies differ in platform, ranking intervention, content increased or reduced, participant setting, outcomes, and duration.
  - The conclusion attributes divergent results to differences in interventions, platforms, content, outcomes, and time horizons.
  - The remaining gaps section states that systematic comparison across platforms, countries, demographic groups, and recommendation designs is not possible from the supplied evidence.
- Missing:
  - It does not actually compare findings across platforms, countries, languages, election timing, user populations, or platform designs in substantive detail.
  - It does not explain specifically why real-world feeds, chronological substitutions, reranking experiments, audits, and simulated environments might produce different results.
  - The report largely treats these scope differences as unresolved rather than analyzing their implications.

### R7

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report recognizes short-versus-longer horizons and flags external-validity and heterogeneity gaps, but it does not substantially assess who is affected, under what exposure conditions, or whether effects persist.
- Candidate evidence:
  - The report states that effects are context-dependent and differ by intervention, content, outcome, and time horizon.
  - It notes that the positive findings come from shorter or more targeted interventions, whereas the null Facebook/Instagram finding covers three months.
  - It identifies unresolved questions about durability, population-level scale, demographic variation, and long-term accumulation.
- Missing:
  - There is little evidence-based analysis of heterogeneity across users, subgroups, content types, exposure intensity, or outcomes.
  - Feedback loops and changing algorithms are mentioned only generally, not evaluated with evidence.
  - The report does not distinguish demonstrated heterogeneity from speculative claims about cumulative or persistent effects.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report delivers a clear and appropriately qualified synthesis, with a useful separation between exposure, attitudes, and behavior. It falls short of full coverage because several methodological and construct-level reasons for disagreement are only implicit or omitted.
- Candidate evidence:
  - The conclusion separately states that exposure changes are clear, attitude and polarization effects are limited and conditional, and durable behavioral effects are not established.
  - It explains divergent findings through differences in platforms, interventions, content, outcomes, time horizons, and the reciprocal relationship between user preferences and algorithmic ranking.
  - The conflicts section explicitly contrasts modest positive findings from targeted or short interventions with a large randomized feed intervention showing major exposure changes but null attitude effects.
  - The report preserves uncertainty by describing the evidence as mixed, insufficient for durable behavioral conclusions, and not reliably generalizable.
- Missing:
  - The explanation does not explicitly address differences in statistical power, measurement error, or thresholds for substantively meaningful effects.
  - It does not fully connect construct differences—such as exposure, engagement, affective polarization, ideological extremity, and behavior—to the literature’s divergent conclusions.
  - The calibrated conclusion is strong overall but could better state the scale of the algorithmic contribution relative to user choice, network composition, and broader political environments.

### Novel Value

- The report offers a useful evidence synthesis that cleanly separates changes in political exposure from downstream attitude and behavioral effects.
- Its central calibrated conclusion—that exposure effects are well supported while durable polarization and behavioral effects remain conditional or unresolved—is a substantive organizing contribution within the supplied material.

## Citations

### Support

#### F1: SUPPORTED

- Claim: Recommendation and ranking algorithms can substantially change what political content users see or encounter first, even when the underlying pool of posts or followed accounts is unchanged.
- Sources: S1, S5, S6, S8, S9
- Rationale: The saved sources directly describe feed-ranking or reranking experiments in which the available posts and followed accounts remained the same while changing the ranking algorithm substantially changed users’ exposure to political and other content. S5 is especially direct: it states that the same posts from the same followed accounts remained available, but their order was controlled by the reranking system. S6, S8, and S9 likewise report substantial exposure changes after replacing default algorithmic feeds with chronological feeds. S1 provides broader evidence that users were exposed to algorithmically selected versus randomly selected political arguments, though it is less directly tied to an unchanged post pool.
- Supporting text: S5: “We didn’t remove anything”; feeds remained constituted by the people users followed and “all the same posts were available,” with only the order changed. S6/S9: replacing algorithmic feeds with chronological feeds changed exposure, including the amount of political content users saw. S8: algorithms were “extremely influential” in what people saw, and algorithm adjustments significantly changed what users saw and their engagement.

#### F2: SUPPORTED

- Claim: Evidence that algorithmic curation changes political attitudes or polarization is positive in some settings but modest and context-dependent, rather than consistently large or general.
- Sources: S1, S4, S5, S6, S8, S9
- Rationale: The saved sources collectively support the claim's main points. S1 reports small direct polarization effects in one topic, no algorithmic amplification of like-minded exposure effects, and inconsistent empirical evidence. S6, S8, and S9 describe substantial changes in exposure and platform experience without significant changes in polarization or other political attitudes during a three-month 2020 election study. S4 and S5 describe a different, one-week X-feed reranking experiment that produced approximately two-point changes in partisan feelings, while S4 explicitly characterizes these as not huge for an individual. Together, these findings indicate positive effects in some settings, null effects in others, and effects that vary by platform, intervention, topic, and study period.
- Supporting text: S1: “Empirical evidence of this causal relationship is inconsistent at best”; algorithmic curation “had small direct effects on attitude polarization,” and for one topic produced “slightly stronger attitude polarization.” S6/S9: despite substantial changes in users’ on-platform experience, chronological feeds “did not significantly alter” issue or affective polarization or other key attitudes over three months. S4/S5: one week of X-feed reranking shifted feelings toward the opposing party by about two points; S4 says these were “not huge shifts for any single individual.”

#### F3: SUPPORTED

- Claim: Some evidence indicates that algorithmic ranking can shift affective political feelings without users consciously noticing the intervention, but this evidence is limited to one reported experiment and does not establish effects on all political beliefs or behaviors.
- Sources: S4, S5
- Rationale: Both sources report the same browser-extension experiment in which reranking X-feed posts changed participants’ feelings toward the opposing political party by roughly two points after one week. S4 reports that 74% noticed no impact, while S5 quotes the researcher saying users could not notice the reranking. The sources describe effects on partisan feelings/affective polarization, not all political beliefs or behaviors, and present this as a single experiment, supporting the claim’s stated limitation.
- Supporting text: S4: “Reducing AAPA exposure led participants to feel warmer toward the opposing party by 2.11 degrees… Increasing exposure caused a symmetrical cooling of 2.48 degrees”; “74% of participants reported noticing no impact.” S5: “after one week, users’ feelings toward the opposing party shifted by about two points,” and users “basically can’t notice anything in terms of the reranking.”

#### F4: PARTIALLY_SUPPORTED

- Claim: The supplied evidence does not establish that recommendation algorithms produce durable changes in political behavior, such as voting, participation, political sharing, following, or offline political action.
- Sources: S8, S10, S11
- Rationale: S8 supports a narrower version of the claim: in three election-period experiments, three-month algorithm modifications changed what participants saw and their platform engagement but did not notably affect attitudes or off-platform behaviors. S10 describes the evidence on algorithms and offline civic participation as a theoretical framework and emphasizes that much existing evidence is correlational, so it does not establish durable causal effects. However, S11 reports a cross-national survey in which social media use was the strongest predictor of online political participation; it does not specifically test recommendation algorithms or durability, but it means the cited set does not uniformly support a broad non-establishment claim about political participation. The sources also do not specifically address following or all listed behaviors.
- Supporting text: S8: “the three-month experimental modifications did not notably affect their attitudes or off-platform behaviors.” S10: the framework proposes mechanisms and future research, while noting that “most evidence is correlational,” limiting causal inference.

#### F5: SUPPORTED

- Claim: The literature reaches different conclusions partly because algorithmic curation and user-driven selective exposure are difficult to disentangle; users’ preferences and engagement influence recommendations, while recommendations may reinforce those existing tendencies.
- Sources: S1, S3, S2, S6
- Rationale: The cited sources collectively support the claim. S1 explicitly states that inconsistent evidence may result from difficulties separating individual exposure to like-minded content from algorithmic effects. S3 describes a feedback loop in which social drivers power algorithmic mechanisms, complicating efforts to disentangle algorithms from existing social phenomena, and says algorithms mostly reinforce existing social drivers. S2 directly describes a feedback loop between users’ selective engagement and platform predictions. S6 explains that personalized algorithms use users’ past behavior and similar users’ actions, while noting that user choice and network composition also affect exposure.
- Supporting text: S1: “many previous studies were unable to separate the effects caused by individual exposure to like-minded content from the effects caused by the algorithms themselves.” S3: algorithms are “powered by social drivers,” creating “a feedback loop that complicates research to disentangle” their roles, and “mostly reinforce existing social drivers.” S2: users reinforce their feeds through repeated engagement, and “algorithms were designed to learn from these behaviours.” S6: algorithms are personalized using “a user’s past behavior,” while “user choice or the composition of one’s network” may also shape content.

### Missing Citations

- Q21: The supplied experiments examine short interventions or bounded study periods rather than long-term outcomes, leaving the durability and population-level scale of observed attitude and affective-polarization effects unresolved.
- Q22: The supplied evidence does not permit systematic comparison across platforms, countries, demographic groups, or recommendation designs, leaving generalizability beyond the studied settings unresolved.

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
- `structured_claim_evidence_available`: PASS
- `ledger_claim_ids_unique`: PASS
- `ledger_evidence_relationships_resolve`: PASS
- `ledger_confidence_values_valid`: PASS
- `ledger_evidence_ids_unique`: NOT_EVALUABLE — Current ledger relations have no independent evidence-ID field.

## Main Weaknesses

1. R1: Define political polarization and distinguish it from related outcomes such as ideological exposure, engagement, media diversity, political knowledge, partisan following, or general political activity.
2. R5: Distinguish the causal strength and limitations of the main types of evidence.
3. R7: Assess whether effects vary across users, content, outcomes, exposure intensity, and time horizons.
4. 1 cited finding(s) were not fully supported by saved evidence.
5. 2 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `0a6b1b066d5fe11922b29a875e67b54f06d262533b8526272d8d350999e2c54e`
- Candidate report hash: `3ea9dba2413dba8f155c4973796755c025ba205da5db0536379d428399c55e36`
- LLM calls: 7
- Evaluated at: 2026-08-31T21:54:24.133067+00:00
