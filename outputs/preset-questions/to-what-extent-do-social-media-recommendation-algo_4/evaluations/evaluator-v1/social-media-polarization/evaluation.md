# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** social-media-polarization

**System Version:** evidence-ledger-decomposer-verifier-v1

**Model:** gpt-5.6-luna

## Summary

- Overall: 77.4 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.73
- Coverage: 0.80
- Depth: 0.57
- Citation quality: 0.79
- Citation validity: 1.00
- Citation support: 0.75
- Citation completeness: 0.75
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report makes the crucial exposure-versus-downstream distinction and names several relevant outcomes, but it does not provide the requested conceptual definition or a systematic boundary between polarization and related outcomes.
- Candidate evidence:
  - The report distinguishes “feed-ranking and exposure changes from downstream outcomes” and states that exposure effects should not be treated as established durable belief or behavior effects.
  - It identifies affective and attitudinal polarization as outcomes, including “opposing-party evaluations,” “issue polarization,” and “political knowledge.”
- Missing:
  - It does not explicitly define political polarization or clearly distinguish affective polarization, ideological extremity, partisan identity, and behavioral polarization.
  - It does not systematically distinguish polarization from ideological exposure, media diversity, engagement, partisan following, or general political activity.
  - The report mentions exposure and interaction differences but does not explicitly state that ideological separation in exposure is not itself polarization.

### R2

- Coverage: 1.00
- Depth: 0.75
- Rationale: The report directly evaluates whether ranking changes what users see and distinguishes ranking manipulation from user choices and observational network composition.
- Candidate evidence:
  - The report states that controlled ranking interventions changed “the prominence, quantity, ideological mix, and source characteristics” of political content.
  - It explains that the X reranking experiment changed post ordering while preserving followed accounts, available posts, and underlying content.
  - It reports that replacing Facebook/Instagram machine-learning ranking with chronological feeds changed political and untrustworthy content exposure, moderate-friend exposure, and ideologically mixed sources.
  - It separately reports observational ideological segregation and notes that follows, clicks, and interactions prevent attribution of later-stage differences solely to ranking.
- Missing:
  - A fully developed treatment could provide more quantitative estimates of exposure changes and more detail on content supply, but the core requirement is substantially addressed.

### R3

- Coverage: 1.00
- Depth: 0.75
- Rationale: The report clearly separates downstream attitudes from exposure and provides direction, some magnitudes, and mixed/null evidence. Its treatment is strong but not fully comprehensive on uncertainty and the full range of belief and identity outcomes.
- Candidate evidence:
  - It reports German quasi-experiments in which like-minded exposure increased attitude and affective polarization, while algorithmic selection generally did not amplify those effects except for a small additional effect on one topic.
  - It reports a one-week randomized X intervention producing approximately 2.48-point cooler opposing-party evaluations when exposure to antidemocratic attitudes and partisan animosity increased, and approximately 2.11-point warmer evaluations when such exposure was reduced, on a 100-point scale.
  - It contrasts these findings with the three-month Facebook/Instagram experiment, which found no significant changes in issue polarization, affective polarization, political knowledge, or other key attitudes.
  - It qualifies the evidence by platform, topic, sample, intervention, and timeframe and states that durable belief change is not established.
- Missing:
  - The report gives limited statistical uncertainty beyond significance and does not consistently report confidence intervals, standard errors, or detectable-effect bounds.
  - It does not substantially evaluate policy-belief change or partisan-identity change separately from affective and issue polarization.

### R4

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report responsibly identifies the behavioral evidence gap and avoids overclaiming, but it offers little positive evaluation of behavioral outcomes and only limited treatment of engagement and other online actions.
- Candidate evidence:
  - The report explicitly states that no supplied study establishes effects on voting, offline participation, or other political behavior.
  - It says the studies do not provide direct evidence about voting, political participation, contacting politicians, sharing as a political behavior, or other offline activity.
  - It distinguishes these gaps from observed exposure and attitude effects rather than inferring behavior from them.
  - It notes that the Facebook observational analysis found differences in political-news engagement, while cautioning that these do not identify algorithmic ranking as the cause.
- Missing:
  - It does not evaluate causal evidence for online behaviors such as sharing, following, engagement, or time spent beyond noting their absence or observational status.
  - It does not discuss whether the interventions changed online behavioral measures, compliance, or participation within the experiments.
  - The report could more explicitly distinguish evidence that algorithms cause behavioral change from the stronger claim that no such evidence was supplied.

### R5

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report differentiates the principal causal designs and recognizes self-selection and intervention limitations, but the rubric calls for a fuller treatment of design-specific threats and additional evidence types.
- Candidate evidence:
  - It distinguishes randomized or researcher-controlled feed interventions, quasi-experiments, and large observational analyses.
  - It explains that randomized interventions provide stronger causal leverage, while the Facebook observational analysis cannot separate ranking from follows, clicks, searches, and other user choices.
  - It notes that some interventions replace or simulate platform ranking rather than testing every naturally occurring production algorithm.
  - It identifies narrower samples and interventions as limitations of experiments and feedback between algorithms, user preferences, and social dynamics as a causal complication.
- Missing:
  - It does not systematically discuss audits or simulations as distinct evidence types.
  - Important threats are only partly covered: noncompliance, treatment contamination, network/content-supply confounding, and measurement error are not developed explicitly.
  - It does not explain in detail how quasi-experimental identification works or what assumptions its German studies require.

### R6

- Coverage: 0.75
- Depth: 0.50
- Rationale: There is meaningful cross-study comparison and an appropriate external-validity warning, but the contextual mechanisms behind cross-platform and cross-country variation remain mostly listed rather than explained.
- Candidate evidence:
  - It compares a three-month Facebook/Instagram ranking intervention, a one-week X reranking intervention, and two German panel quasi-experiments.
  - It identifies differences in platform, country, campaign context, topics, intervention design, duration, outcomes, and samples as reasons results should not be collapsed.
  - It contrasts observational Facebook evidence with stronger but narrower randomized and quasi-experimental evidence.
  - It notes that generalizability across platforms, countries, populations, issues, and longer time horizons remains unresolved.
- Missing:
  - Country and platform differences are named but not substantively analyzed, including language, election timing beyond the U.S. campaign reference, user composition, and platform-design differences.
  - The report does not discuss chronological substitutions, audits, or simulated environments in enough detail to explain why their results may differ.

### R7

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes heterogeneity and time-horizon issues and appropriately avoids asserting unsupported long-term accumulation, but it does not substantially evaluate variation across users, content, exposure intensity, or time.
- Candidate evidence:
  - The report states that effects depend on “platform, users, content, intervention, outcome, and time horizon.”
  - It notes possible moderation or mediation by user preferences and social dynamics and identifies one-week versus three-month interventions.
  - It says the available evidence does not resolve longer-term effects, subgroup effects, or durable belief change.
- Missing:
  - It provides little evidence-based analysis of subgroup heterogeneity, exposure intensity, user types, content types, or differential effects.
  - Feedback loops are mentioned through the review, but not explained or tested as an empirical mechanism.
  - It does not distinguish demonstrated heterogeneity from speculative possibilities in a detailed way.
  - Cumulative, persistent, and changing-algorithm effects are identified as unresolved rather than assessed.

### R8

- Coverage: 1.00
- Depth: 0.75
- Rationale: The report delivers a calibrated and appropriately separated overall assessment, explains major sources of disagreement, and avoids both dismissal and overstatement. Some rubric-specified explanatory factors are only implicit or absent.
- Candidate evidence:
  - The conclusion separately states that ranking can reliably alter the informational environment while evidence for changes in beliefs or behavior is weaker and mixed.
  - It explains disagreement through differences in platform, users, content, intervention, outcome, duration, country, campaign context, and research design.
  - It preserves uncertainty by stating that algorithms are neither harmless nor a general, sufficient cause of polarization.
  - It explicitly concludes that some short-term interventions changed affective or attitudinal polarization, another three-month intervention found no significant average attitude changes, and durable belief and political-behavior effects are not established.
- Missing:
  - The synthesis could connect disagreements more explicitly to statistical power, construct definitions, intervention intensity, and effect-size thresholds.
  - The overall assessment would be stronger with a clearer distinction between contribution to polarization as a causal component and evidence of large population-level effects.

### Novel Value

- No material benchmark-external value identified.

## Citations

### Support

#### F1: SUPPORTED

- Claim: Recommendation or feed-ranking systems can causally change what users see, even when users’ followed accounts and the available content remain unchanged.
- Sources: S4, S5, S7, S6
- Rationale: The saved sources directly describe randomized or experimental feed reranking that changed the ordering and exposure of posts while leaving the underlying posts and followed accounts unchanged. S5 explicitly states that feeds remained constituted by followed accounts and that all the same posts were available; only their order changed. S7 likewise says no posts were removed and that reranking caused incendiary posts to appear lower or higher. S6 independently reports that replacing default algorithmic feeds with chronological feeds substantially changed users’ content exposure.
- Supporting text: S5: “We didn’t remove anything… Users’ feeds were still constituted by the people they followed and all the same posts were available for viewing, it was simply the order in which they appeared that the LLM controlled.” S7: “No posts were removed, but the more incendiary political posts appeared lower or higher in their content streams.”

#### F2: PARTIALLY_SUPPORTED

- Claim: The supplied evidence documents ideological separation in political-news exposure and interaction, but observational evidence cannot isolate the contribution of algorithmic ranking from users’ own choices.
- Sources: S8
- Rationale: S8 supports the first part: it reports limited overlap in political-news consumption between liberals and conservatives and increasing segregation from algorithmic selection to user exposure and interaction. It also notes researchers had little direct insight into the algorithms’ inner workings, which supports a limitation on attributing effects to ranking. However, the source does not explicitly state that observational evidence cannot separate algorithmic ranking from users’ own choices; it also describes an intervention that changed the algorithm and affected what users saw and how they behaved.
- Supporting text: S8 reports that liberals and conservatives had “not much overlap” in political-news consumption, with segregation increasing from links selected by the algorithm to those seen and interacted with. It also says researchers had “little direct insight about the inner workings” of the algorithms.

#### F3: SUPPORTED

- Claim: Changing algorithmic exposure can sometimes produce short-term changes in affective or attitudinal polarization, but the effects are not uniform or consistently attributable to algorithmic selection itself.
- Sources: S1, S4, S5, S7
- Rationale: The saved sources support both parts of the claim. S1 reports that changing exposure to like-minded versus opposing arguments altered affective and attitude polarization, but says algorithmic selection did not consistently amplify those effects and produced only a slight attitude-polarization effect for one topic. S4, S5, and S7 report short interventions in which reranking partisan-animosity content changed feelings toward the opposing party. S1 directly supports the qualification that effects are not uniform and cannot consistently be attributed to algorithmic selection itself.
- Supporting text: S1: Exposure to like-minded arguments increased attitude and affective polarization, but these effects “were not amplified by algorithmic selection”; algorithmically selected arguments produced slightly stronger attitude polarization than randomly selected arguments for one topic. S5/S7: after about one week, increasing or decreasing exposure to partisan-animosity content shifted feelings toward the opposing party by roughly two points.

#### F4: SUPPORTED

- Claim: Substantial algorithmically induced changes in exposure do not necessarily produce measurable average changes in political attitudes.
- Sources: S6, S3
- Rationale: S6 directly reports that replacing Facebook and Instagram’s default algorithmic feeds caused substantial changes in users’ content exposure but did not significantly alter several average political attitudes over the three-month study. S3 provides broader contextual support that algorithmic effects on polarization are not straightforward, though it is not necessary for the claim.
- Supporting text: S6: Users moved to chronological feeds saw substantial changes in political, untrustworthy, uncivil, and ideologically mixed content exposure, yet the intervention did not significantly change average issue polarization, affective polarization, political knowledge, or other key attitudes during the study period.

#### F5: PARTIALLY_SUPPORTED

- Claim: The overall causal chain is better established for exposure than for durable political beliefs or behavior: the supplied studies show ranking and exposure effects, limited short-term attitude effects in some settings, and no established effects on durable beliefs or offline political behavior.
- Sources: S1, S5, S6, S7, S3
- Rationale: The sources support causal effects on content ranking/exposure and short-term political attitudes or affective polarization. S1 reports that like-minded exposure increased attitude and affective polarization, while algorithmic selection did not generally amplify those effects. S5 and S7 report short interventions changing partisan feelings. S6 reports substantial changes in exposure and on-platform activity but no significant changes in several political attitudes during three months. S3 characterizes the broader evidence as non-straightforward and requiring further research. However, the claim’s categorical statement that there are “no established effects” on durable beliefs or offline political behavior is not directly established by the supplied excerpts: they do not comprehensively assess durable beliefs or offline behavior, and S6 concerns on-platform activity rather than offline behavior.
- Supporting text: S1: exposure to like-minded arguments increased attitude and affective polarization; algorithmic curation did not amplify these effects. S5/S7: about one week of reranking changed feelings toward the opposing party by roughly two points. S6: ranking changes altered exposure and platform activity, but did not significantly alter issue polarization, affective polarization, political knowledge, or other key attitudes over three months. S3: the role of algorithms is “far from straightforward” and substantial further empirical research is needed.

#### F6: PARTIALLY_SUPPORTED

- Claim: The literature reaches different conclusions because the studies manipulate or observe different stages of the causal process and use different platforms, interventions, populations, outcomes, and time horizons.
- Sources: S1, S5, S6, S7, S8, S3
- Rationale: The snapshots support that studies reach different conclusions and differ in several important design features. S1 reports inconsistent evidence and distinguishes exposure to like-minded content from algorithmic selection. S6 and S8 describe Facebook/Instagram experiments using chronological feeds during the 2020 election, measuring content exposure, behavior, and political attitudes over three months; S7 and S5 describe X-feed reranking interventions during the 2024 election, involving about 1,200 participants and measuring affective polarization over roughly one week to ten days. S3 broadly states that algorithmic effects are not straightforward and are entangled with social drivers. However, the supplied text does not systematically establish that all listed differences—especially distinct causal-process stages and populations across the literature—are the reason for the divergent conclusions. Thus, a narrower version is supported.
- Supporting text: S1: “empirical evidence ... is inconsistent at best” and prior studies often could not separate individual exposure effects from algorithm effects. S6: the chronological-feed intervention changed on-platform experience but did not significantly change polarization during the “3-month study period.” S7: an X-feed intervention reranked antidemocratic and partisan-animosity content; about 1,200 participants used it for 10 days and showed changes in views of the opposing party. S3: algorithmic effects are “far from straightforward” and algorithms interact with existing social drivers.

### Missing Citations

- Q19: The supplied evidence does not adequately quantify ordinary users’ political exposure across major platforms while separating algorithmic ranking from users’ own choices.
- Q20: Causal attitude evidence in the supplied materials is limited to short interventions and specific contexts, especially a German panel study and a one-week U.S. X experiment.
- Q21: The supplied sources do not permit a systematic comparison of polarization definitions, outcome measures, intervention intensity, sample selection, and platform algorithms across the full literature.
- Q23: Controlled changes to ranking can alter which political content is prominent, how much users encounter, and in some cases its ideological or source mix.
- Q24: Some short-term interventions changed affective or attitudinal polarization, while another substantial three-month intervention found no significant average changes in key political attitudes.
- Q25: The most defensible synthesis is that recommendation algorithms can shape the informational environment and may amplify polarization under particular conditions, but are not shown to be a general or sufficient cause of polarization.

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
4. 3 cited finding(s) were not fully supported by saved evidence.
5. 6 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `0a6b1b066d5fe11922b29a875e67b54f06d262533b8526272d8d350999e2c54e`
- Candidate report hash: `c2a2fb8cfa640fcd8c4f738bdbe74a4e31c16c81bb4dd5a5cd3d8d5ab085927b`
- LLM calls: 8
- Evaluated at: 2026-08-31T23:23:21.554491+00:00
