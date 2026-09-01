# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** social-media-polarization

**System Version:** baseline-zero

**Model:** gpt-5.6-luna

## Summary

- Overall: 79.3 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.65
- Coverage: 0.69
- Depth: 0.57
- Citation quality: 1.00
- Citation validity: 1.00
- Citation support: 1.00
- Citation completeness: 1.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report makes several useful outcome distinctions, especially between exposure, attitudes, affective polarization, partisanship, and behavior. However, it lacks an explicit conceptual definition and a systematic treatment of the requested related constructs.
- Candidate evidence:
  - The report states that “political attitudes” and “polarization” should not be treated as interchangeable outcomes.
  - It separately discusses “issue polarization,” “affective polarization,” “self-reported partisanship,” political knowledge, exposure, engagement, and following behavior.
  - The conclusion distinguishes changes in exposure from changes in beliefs and behavior.
- Missing:
  - It does not explicitly define political polarization as a concept or clearly distinguish ideological extremity, affective polarization, partisan identity, and behavioral polarization.
  - It mentions related outcomes but does not systematically explain why exposure, engagement, political knowledge, media diversity, or general activity are not themselves polarization.

### R2

- Coverage: 1.00
- Depth: 0.75
- Rationale: This requirement is addressed substantively with multiple controlled experiments and distinctions between feed ranking, exposure, user selection, and network effects. The treatment is strong but not fully comprehensive about all sources of observed content supply and exposure.
- Candidate evidence:
  - The report states that recommendation algorithms have “strong, directly measured effects on what users see and do on platforms.”
  - It describes the Facebook/Instagram chronological-feed experiment as changing “time spent, activity, and exposure to political, untrustworthy, uncivil, moderate, and ideologically mixed content.”
  - It reports that Meta studies found “substantial ideological segregation in political-news exposure” and that ranking, resharing, and same-ideology recommendations altered users’ experiences.
  - It reports that the X reranking experiment changed the order of the same posts and increased or decreased exposure to antidemocratic and partisan-animosity content.
  - It distinguishes algorithmic exposure from user behavior through discussion of follows, user preferences, social networks, and platform architecture.
- Missing:
  - The report does not comprehensively separate ranking effects from follows, clicks, searches, subscriptions, and network composition in the empirical discussion.
  - It provides little detail on the magnitude or uncertainty of the reported exposure effects and does not discuss audit evidence separately from experiments.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report clearly separates feed composition from downstream attitudes and provides direction, approximate magnitude, and significance for important findings. It falls short of full coverage because statistical uncertainty and substantive significance are only partially characterized.
- Candidate evidence:
  - The report separately states that exposure effects do not necessarily imply attitude effects.
  - It reports that Meta interventions changed exposure but produced “no significant average changes” in issue polarization, affective polarization, political knowledge, or other attitudes over three months.
  - It reports that an X experiment shifted selected policy and current-affairs opinions toward more conservative positions.
  - It reports a one-week X experiment producing approximately 2.11-point greater opposing-party warmth when hostile content was reduced and a 2.48-point decline when such exposure was increased, on a 100-point scale.
  - It notes that X produced no significant effect on affective polarization or self-reported partisanship.
- Missing:
  - The report does not consistently provide confidence intervals, standard errors, or precise statistical uncertainty beyond statements of significance.
  - It gives limited discussion of the substantive importance of the reported effect sizes, especially whether the roughly two-point warmth effects are large or durable.
  - It does not fully distinguish policy-attitude changes from ideological extremity and broader belief change.

### R4

- Coverage: 0.75
- Depth: 0.50
- Rationale: It appropriately reports online following and engagement evidence and avoids inferring voting or offline effects. However, behavioral effects receive less detailed evaluation than exposure and attitudes.
- Candidate evidence:
  - The report identifies changes in engagement, time use, activity, and account following as directly measured behavioral outcomes.
  - It reports that algorithmically exposed X users were more likely to follow conservative activist accounts and continued following them after the feed returned to chronological order.
  - It explicitly states that the evidence does not establish effects on voting, political participation, sharing, offline hostility, or offline conduct.
- Missing:
  - The report does not systematically evaluate the causal evidence for engagement, sharing, time spent, political participation, or other online and offline behaviors.
  - It does not clearly separate politically relevant behavior from general on-platform activity or explain the magnitude and uncertainty of the following and engagement effects.

### R5

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes randomized designs and some causal limitations, particularly selection and feedback loops. It does not provide the requested method-by-method appraisal or discuss several important threats to inference.
- Candidate evidence:
  - The report identifies the Facebook/Instagram and X studies as randomized experiments and describes their interventions.
  - It contrasts broad chronological-feed replacement with targeted X reranking and notes that treatment direction, duration, content, platform, and outcomes differed.
  - It acknowledges that feedback-loop evidence combines conceptual, theoretical, survey, and experimental research and does not fully separate user selection from algorithmic influence.
- Missing:
  - It does not systematically distinguish randomized feed interventions, reranking experiments, audits, observational studies, surveys, and simulations.
  - Material threats such as noncompliance, treatment contamination, measurement error, network confounding, and content-supply confounding are largely absent.
  - It does not explain the causal limitations of the cited news reports, theoretical models, and survey evidence in enough detail.

### R6

- Coverage: 0.75
- Depth: 0.50
- Rationale: There is a meaningful comparison across platforms and intervention types, plus an explicit external-validity caveat. The cross-national, language, audit, and simulation dimensions are underdeveloped.
- Candidate evidence:
  - The report compares Meta and X experiments, including broad feed replacement, targeted reranking, and changes in following behavior.
  - It explains that results differ by “platform, algorithmic system, treatment direction, content being amplified, intervention duration, political context, and outcome measures.”
  - It states that generalization is limited beyond active U.S. users, studied elections and political environments, and the ranking systems of X, Facebook, and Instagram.
- Missing:
  - It does not substantially compare countries, languages, or non-U.S. political contexts.
  - It does not discuss audits and simulated environments in the requested cross-setting comparison.
  - It gives limited detail on how election timing, platform design, and user composition concretely alter expected effects.

### R7

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report acknowledges important dimensions of heterogeneity and time horizon and is appropriately cautious about persistence. It provides limited actual evidence about subgroup or cumulative variation.
- Candidate evidence:
  - The report notes that effects depend on users’ existing preferences and identifies possible variation by “prior ideology, political engagement, network composition, and exposure to competing information.”
  - It reports a seven-week X intervention and a three-month Meta intervention, and identifies persistence of follows after the X algorithm was switched off.
  - It lists as an unresolved issue whether X-induced opinion and following changes persist beyond approximately seven weeks.
- Missing:
  - Most subgroup differences are posed as open questions rather than supported findings.
  - There is little evidence-based analysis of heterogeneity by content, exposure intensity, user type, or outcome.
  - Feedback loops, cumulative effects, changing algorithms, and long-term persistence are mentioned but not empirically evaluated; the report does not clearly distinguish established heterogeneity from speculation.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report offers a well-calibrated, nonbinary synthesis and directly explains several major sources of disagreement. It is not fully comprehensive about methodological reasons for divergent results or the full range of polarization constructs.
- Candidate evidence:
  - The conclusion separately characterizes strong evidence for altered exposure and narrower, conditional evidence for changed beliefs or behavior.
  - It explains divergent findings through differences in platform design, content and ranking rules, intervention duration, treatment direction, political context, and outcome measures.
  - It states that Meta found large exposure changes alongside null average attitude effects, whereas X found selected changes in policy opinions, partisan warmth, and following.
  - It concludes that algorithms can influence attitudes and online behavior but that the evidence does not support attributing overall polarization, voting, or offline conduct primarily to algorithms alone.
- Missing:
  - The explanation gives limited attention to statistical power, noncompliance, measurement choices, and differing effect-size thresholds as sources of disagreement.
  - The overall synthesis could more explicitly distinguish evidence for affective polarization, ideological polarization, partisan identity, and behavioral polarization.
  - Some claims about why findings differ, such as persistent follows explaining asymmetric X effects, are presented as plausible explanations without much direct evidence.

### Novel Value

- The report offers a conditional synthesis that separates robust exposure effects from mixed downstream attitude effects and limited evidence for broader political behavior.
- It highlights the contrast between large Meta exposure changes with null average attitude effects and selected X effects on policy opinions, partisan warmth, and account following.
- It identifies persistence of follows and the asymmetry between turning X’s algorithm on and off as a potentially important mechanism, while explicitly noting that long-term persistence remains unresolved.

## Citations

### Support

#### F1: SUPPORTED

- Claim: Recommendation algorithms have strong, directly measured effects on what users see and do on platforms.
- Sources: S6, S4, S1, S5
- Rationale: The cited sources report experiments that changed feed-ranking systems and directly measured effects on users’ exposure, time spent, activity, and—in a separate X-feed experiment—political feelings. S6 provides especially direct support for both what users saw and did: replacing default feeds substantially changed content exposure, time spent, and activity. The claim is supported in the platform-feed context, although the sources do not establish effects on every type of user behavior.
- Supporting text: S6: Users assigned to chronological rather than default algorithmic feeds saw substantial changes in content exposure, while spending less time on the platforms and showing less activity. S5: A browser extension that reranked X posts changed users’ feelings toward the opposing party by about two points after one week.

#### F2: SUPPORTED

- Claim: There is credible causal evidence that some algorithmic interventions change selected political attitudes, but the effects are not uniform across outcomes.
- Sources: S10, S11, S1, S5
- Rationale: S10 reports a randomized seven-week field experiment in which assigning users to an algorithmic rather than chronological feed shifted several political attitudes, while producing no significant effect on affective polarization or self-reported partisanship. S1 and S5 independently describe a randomized reranking intervention that changed partisan feelings, with increased and decreased exposure producing opposite effects. Together, the sources support both causal evidence and variation across outcomes.
- Supporting text: S10: Users were randomly assigned to algorithmic or chronological feeds; the algorithmic feed shifted policy priorities, views concerning Trump investigations, and views on Ukraine, but did not significantly affect affective polarization or self-reported partisanship. S5: After one week of reranking partisan-animosity content, opposing-party feelings shifted by about two points, with increased exposure making feelings colder and decreased exposure making them warmer.

#### F3: SUPPORTED

- Claim: The strongest counterevidence comes from randomized Meta experiments, which found large exposure effects but no significant average changes in measured political attitudes or polarization during the study periods.
- Sources: S6, S4
- Rationale: S6 directly describes randomized controlled experiments on Facebook and Instagram, reports substantial changes in users’ exposure and on-platform experience, and states that the intervention did not significantly alter issue polarization, affective polarization, political knowledge, or other key attitudes during the three-month study. S4 independently summarizes multiple randomized algorithm interventions, reporting little difference in political attitudes or polarization while documenting changes in news exposure and platform use.
- Supporting text: S6: Users were randomly assigned to chronological rather than algorithmic feeds; this substantially changed time spent, activity, and content exposure, but did not significantly alter issue polarization, affective polarization, political knowledge, or other key attitudes during the 3-month study. S4: Researchers changed algorithms for some users and saw little difference; chronological feeds had no measurable impact on polarization, while other interventions changed exposure to untrustworthy and political news without significant changes in political attitudes.

#### F4: SUPPORTED

- Claim: The X evidence suggests one pathway from algorithmic exposure to persistent online political behavior: users exposed to X’s algorithm were more likely to follow conservative political activist accounts, and those follows persisted after returning to a chronological feed.
- Sources: S10, S11
- Rationale: Both saved sources directly support the claim. S10 reports that algorithmic exposure led users to follow conservative political activist accounts and that they continued following them after the algorithm was switched off. S11 independently summarizes that algorithm-assigned users were more likely to follow such accounts and that switching to a chronological feed had little effect on following behavior.
- Supporting text: S10: “Exposure to algorithmic content leads users to follow conservative political activist accounts, which they continue to follow even after switching off the algorithm.” S11: Users assigned to the algorithmic feed “were more likely to follow conservative political activist accounts,” while switching to the chronological feed had “little effect” on following behavior.

#### F5: SUPPORTED

- Claim: User preferences and algorithmic ranking operate in a feedback loop, so algorithms may reinforce polarization without being its sole or initial cause.
- Sources: S4, S2, S3, S6, S7
- Rationale: The saved sources directly support both key elements: users’ preferences and behavior shape algorithmic recommendations, while algorithmic ranking reinforces or amplifies those patterns. They also indicate that polarization predates platforms and that algorithms are not necessarily the sole cause: S2 says algorithms are powered by social drivers in a feedback loop and mostly reinforce existing drivers; S3 describes the interaction between user behavior and platform architecture; and S4 says users seek aligned content while algorithms make it easier, adding that polarization involves more than social media. S6 provides corroborating evidence that ranking substantially changes exposure and experience without significantly changing polarization during the study period.
- Supporting text: S2: “Algorithmic mechanisms on digital media are powered by social drivers, creating a feedback loop” and “algorithms mostly reinforce existing social drivers.” S3: “the process is ... a feedback loop between platform architecture and user behaviour.” S4: users “seek out content that aligns with their views” and algorithms help by “making it easier for people to do what they're inclined to do”; the article says “there’s a lot more that goes into this than social media.”

#### F6: SUPPORTED

- Claim: The literature’s different conclusions are best understood as conditional findings rather than a simple contradiction about whether algorithms matter.
- Sources: S6, S10, S1, S11, S2
- Rationale: The sources describe differing results across platforms, interventions, outcomes, and exposure conditions. S6 reports substantial changes in content exposure and platform behavior but no significant changes in several political attitudes after replacing Meta’s algorithmic feed with a chronological feed. In contrast, S10 and S11 report that switching users onto X’s algorithmic feed shifted some political opinions, while switching it off had no comparable effects, suggesting asymmetric and persistent effects. S2 explicitly states that algorithmic effects are “far from straightforward” and that algorithms mostly reinforce existing social drivers. Together, these sources support interpreting the findings as conditional rather than as a simple contradiction.
- Supporting text: S2: the role of algorithms is “far from straightforward.” S6: changing Meta feeds substantially altered exposure and activity but did not significantly alter key attitudes. S10/S11: turning on X’s algorithm shifted some political opinions, whereas turning it off had no comparable effect.

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

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `0a6b1b066d5fe11922b29a875e67b54f06d262533b8526272d8d350999e2c54e`
- Candidate report hash: `4a21aed77d1b284d2e85650b01a56de3ab2c71c41a1424cc100d614fa5fd8493`
- LLM calls: 8
- Evaluated at: 2026-09-01T07:12:46.841670+00:00
