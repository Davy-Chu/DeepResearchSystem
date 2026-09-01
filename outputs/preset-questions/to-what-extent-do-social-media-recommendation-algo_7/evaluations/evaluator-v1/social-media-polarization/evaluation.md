# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** social-media-polarization

**System Version:** evidence-ledger-decomposer-v1

**Model:** gpt-5.6-luna

## Summary

- Overall: 70.2 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.61
- Coverage: 0.63
- Depth: 0.57
- Citation quality: 0.78
- Citation validity: 1.00
- Citation support: 0.60
- Citation completeness: 1.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.50
- Depth: 0.25
- Rationale: The report correctly avoids treating exposure changes as polarization and separates several outcomes, but it largely assumes rather than defines the relevant constructs.
- Candidate evidence:
  - The report states that “changes in exposure do not reliably produce changes in political beliefs, polarization, or behavior.”
  - It separately discusses “issue polarization,” “affective polarization,” “political knowledge,” “partisanship,” “engagement,” and exposure.
- Missing:
  - It does not explicitly define political polarization.
  - It does not clearly distinguish polarization from ideological exposure, media diversity, partisan following, or general political activity in conceptual terms.
  - Ideological extremity and behavioral polarization are mentioned only indirectly, if at all.

### R2

- Coverage: 0.75
- Depth: 0.75
- Rationale: This is well-supported exposure analysis with direct randomized evidence and attention to selection, but some important components of the requested exposure-versus-user-choice distinction remain abbreviated.
- Candidate evidence:
  - The report cites randomized Facebook/Instagram feed replacement evidence showing changes in political and untrustworthy content, source visibility, moderate friends, ideologically mixed sources, and engagement.
  - It cites a randomized X experiment finding increased conservative activist content and reduced visibility of traditional news sources.
  - Finding 4 explicitly identifies user choices, preferences, networks, and content alignment as distinct contributors from algorithmic ranking.
- Missing:
  - The distinction between algorithmic ranking and follows, clicks, searches, subscriptions, and network composition is not developed systematically.
  - The report gives little detail on content supply, amplification mechanisms, or the size of ideological-diversity changes.
  - Comparable numerical effect sizes are acknowledged as unavailable but not supplied.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report effectively separates exposure from attitudes and presents contrasting causal findings with direction and some uncertainty, but it lacks the quantitative and substantive-effect characterization required for full depth.
- Candidate evidence:
  - The report separately evaluates downstream attitudes and states that Facebook/Instagram exposure changes produced no statistically significant change in issue polarization, affective polarization, political knowledge, or other key attitudes over three months.
  - It reports that the X experiment shifted political opinions toward more conservative positions without major change in partisanship or polarization.
  - It reports German evidence that like-minded exposure increased attitude and affective polarization and that algorithmic selection produced a small topic-specific attitude-polarization effect.
  - It explicitly notes that some positive findings are selective and do not consistently amount to greater polarization.
- Missing:
  - No numerical effect sizes or confidence intervals are reported.
  - The substantive importance of the reported opinion and polarization effects is not assessed beyond labels such as “small,” “substantial,” or “no major change.”
  - The report does not consistently distinguish statistical non-significance from evidence of practical equivalence or adequately powered null results.

### R4

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report appropriately refuses to infer voting or offline behavior from exposure and acknowledges the evidence gap, but its behavioral evaluation is limited mainly to engagement and a statement that direct political-behavior evidence is absent.
- Candidate evidence:
  - The report discusses causal changes in “engagement,” “time spent,” and “activity” in the Facebook/Instagram experiment.
  - It states that the supplied evidence does not establish effects on voting, political participation, or other offline political behavior.
  - The conclusion says that a durable effect or effect on political behavior cannot be drawn.
- Missing:
  - Online behavioral effects are not evaluated in detail, including sharing, following, political posting, or other forms of participation.
  - The report does not clearly distinguish behavior measured as an outcome from engagement changes caused by the feed intervention.
  - It does not characterize the magnitude or uncertainty of the reported engagement and activity effects.

### R5

- Coverage: 0.50
- Depth: 0.50
- Rationale: It recognizes randomized versus non-randomized evidence and several confounding concerns, but does not provide the requested systematic treatment of study designs and threats to causal inference.
- Candidate evidence:
  - The report contrasts randomized feed interventions on Facebook/Instagram and X with German experimental panel studies, a review, survey evidence around a Facebook update, and a theoretical model.
  - It notes that the Facebook-update evidence lacks causal identification, comparison conditions, and effect sizes.
  - It identifies user selection, network structure, content alignment, and pre-existing preferences as complications.
- Missing:
  - The causal strengths of audits, observational studies, surveys, and simulations are not explicitly differentiated as evidence types.
  - Material threats such as noncompliance, treatment contamination, measurement error, and treatment spillovers are not discussed.
  - The report does not explain how the interventions isolate ranking from follows, network composition, or user behavior in sufficient methodological detail.

### R6

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report makes a useful cross-platform and cross-study comparison, but the explanation of why particular settings and intervention designs yield different results remains relatively general.
- Candidate evidence:
  - The report compares a three-month Facebook/Instagram intervention, a seven-week X intervention among active US users, and German panel experiments.
  - It explains that these studies differ in platforms, ranking systems, populations, political contexts, timeframes, interventions, exposure conditions, and polarization definitions.
  - It states that real differences across intervention types and short- versus long-term effects remain unresolved.
- Missing:
  - Country and user-composition differences are noted but not analyzed in detail.
  - Election timing, language, and platform-design differences are not specifically explained.
  - Simulated environments, audits, and chronological substitutions are not separately compared as requested.

### R7

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes the relevant dimensions and is appropriately cautious about long-term claims, but mostly lists unresolved possibilities rather than assessing observed heterogeneity.
- Candidate evidence:
  - The report identifies unresolved heterogeneity by platform, algorithm design, population, political context, exposure intensity, intervention type, and outcome definition.
  - It discusses three-month and seven-week interventions and explicitly states that persistence, accumulation, and long-term effects are unestablished.
  - It mentions feedback loops between engagement and ranking.
- Missing:
  - There is little actual assessment of evidence for differences across user subgroups, content types, or exposure intensity.
  - Feedback loops are presented mainly as a model or possible mechanism rather than evaluated empirical evidence.
  - The report does not distinguish clearly between evidence-supported heterogeneity and speculation about cumulative or persistent effects.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report offers a strong, appropriately qualified synthesis and directly answers the central separation requested. Full credit is withheld because methodological and statistical explanations for divergent findings are not developed with sufficient specificity.
- Candidate evidence:
  - The conclusion separately states that algorithms demonstrably affect political-information exposure while evidence for beliefs or polarization is weaker and heterogeneous.
  - It explains disagreement through platform, user, network, content, intervention, outcome, context, and duration differences.
  - It gives a calibrated conclusion that algorithms are “plausible and sometimes consequential contributors within a broader user-and-network system,” not a consistently demonstrated primary cause.
  - It explicitly states that reliable average magnitude, durable effects, and effects on political behavior cannot be drawn.
- Missing:
  - The explanation does not explicitly address statistical power, non-equivalent null findings, or differing thresholds for what counts as a substantively important effect.
  - The synthesis could more clearly distinguish evidence for algorithm-specific causal effects from effects of exposure to like-minded content generally.
  - Some claims about why studies disagree remain broad because study-level methodological details and effect sizes are not provided.

### Novel Value

- The report provides a useful synthesis separating demonstrable feed-composition and engagement effects from weaker, heterogeneous evidence on political attitudes and behavior.
- It emphasizes that algorithmic ranking interacts with user selection, homophily, network structure, and content alignment rather than operating as an isolated cause.
- Its conclusion preserves uncertainty about average magnitude, persistence, voting, participation, and offline effects instead of extrapolating from exposure changes.

## Citations

### Support

#### F1: SUPPORTED

- Claim: Recommendation algorithms can change the political content, source mix, ideological visibility, and engagement that users encounter, but the direction and magnitude of exposure effects are platform- and intervention-dependent rather than uniformly producing less viewpoint diversity.
- Sources: S10, S8, S6, S12
- Rationale: The saved sources support the claim’s main points. S10 reports that replacing Facebook and Instagram’s default feeds with chronological feeds changed political and untrustworthy content exposure, increased exposure to moderate friends and ideologically mixed sources on Facebook, and reduced time spent and activity. S8 reports that switching from a chronological to an algorithmic feed on X increased engagement and shifted political opinion, demonstrating platform-dependent effects. S6 finds that algorithmic curation had small direct effects on polarization but did not amplify the effects of like-minded exposure. S12 describes evidence that diverse exposure can be higher than through other media and that ranking algorithms did not greatly affect ideological balance, supporting the non-uniform viewpoint-diversity qualification.
- Supporting text: S10: The chronological feed changed exposure to political, untrustworthy, uncivil, moderate-source, and ideologically mixed content, while also decreasing time spent and activity. S8: On X, switching to an algorithmic feed increased engagement and shifted political opinion. S6: Algorithmic curation did not amplify polarization effects, with only small direct effects. S12: Empirical studies offer a nuanced view; diverse exposure may be higher on social media and ranking algorithms may have little effect on ideological balance.

#### F2: CONTRADICTED

- Claim: Changes in what users see should not be treated as evidence that recommendation algorithms changed political beliefs, polarization, or behavior.
- Sources: S10, S12, S6, S8
- Rationale: S10 supports caution: substantial changes in exposure and on-platform experience did not significantly change several political attitudes during its three-month study. S12 and S6 likewise describe mixed or nuanced evidence. However, the claim is categorical, and S8 reports a randomized field experiment in which switching feeds increased engagement and shifted political opinion toward more conservative positions. Thus, the sources do not support rejecting changes in what users see as evidence in all cases; they support treating them as insufficient on their own and requiring causal evidence.
- Supporting text: S10: “Despite these substantial changes in users’ on-platform experience, the chronological feed did not significantly alter levels of issue polarization, affective polarization, political knowledge, or other key attitudes.” Counterevidence in S8: switching from a chronological to an algorithmic feed “increased engagement and shifted political opinion towards more conservative positions.”

#### F3: SUPPORTED

- Claim: Some experiments provide causal or comparatively well-supported evidence that algorithmic systems can affect political attitudes, but the effects are selective and do not consistently amount to greater polarization.
- Sources: S6, S8, S11, S10
- Rationale: The cited snapshots collectively support the claim. S6 reports two quasi-experiments in which algorithmic selection produced a small, topic-specific increase in attitude polarization, while like-minded exposure—not algorithmic curation—was the stronger source of polarization and algorithmic curation did not amplify the effects. S8 reports a randomized seven-week field experiment finding that an algorithmic X feed shifted political opinion toward more conservative positions. S10 reports randomized Facebook and Instagram experiments in which replacing algorithmic feeds substantially changed users’ experiences but did not significantly change issue polarization, affective polarization, political knowledge, or other key attitudes. Thus, the evidence includes causal or comparatively strong designs, effects on political attitudes are selective, and polarization effects are not consistent. S11 is supportive of algorithmic effects on polarization in its model and associated survey evidence, though it is less directly experimental.
- Supporting text: S6: “exposure to algorithmically selected arguments led to slightly stronger attitude polarization than randomly selected arguments” for one topic, but algorithmic selection “did not amplify” the broader effects. S8: randomly assigning users to algorithmic versus chronological feeds for seven weeks “shifted political opinion towards more conservative positions.” S10: the chronological-feed intervention “did not significantly alter levels of issue polarization, affective polarization, political knowledge, or other key attitudes.”

#### F4: PARTIALLY_SUPPORTED

- Claim: Users’ own choices, pre-existing preferences, confirmation bias, social networks, and content alignment are complementary contributors to politically homogeneous exposure and polarization; recommendation algorithms are not established as the sole cause.
- Sources: S1, S2, S6, S10, S11, S12
- Rationale: The sources support a narrower claim that user behavior or choice, pre-existing preferences, content alignment, and network composition contribute alongside algorithms, and that algorithmic ranking is not consistently shown to be the sole or dominant cause. S6 directly reports that like-minded exposure increased polarization more strongly than opposing exposure and that algorithmic selection did not amplify those effects. S10 identifies user choice and network composition as relevant determinants and finds that changing feed algorithms did not significantly alter polarization during the study. However, the supplied text does not specifically establish confirmation bias as a distinct contributor, and the evidence for all listed factors jointly causing politically homogeneous exposure is incomplete.
- Supporting text: S6: “Exposure to like-minded arguments increased participants’ attitude polarization ... Yet ... these effects were not amplified by algorithmic selection.” S10: “other determinants ... such as user choice or the composition of one’s network—could be relevant as well”; changing to a chronological feed “did not significantly alter levels of issue polarization [or] affective polarization.”

#### F5: PARTIALLY_SUPPORTED

- Claim: The literature reaches different conclusions because studies examine different platforms and ranking systems, populations, political contexts, timeframes, interventions, exposure conditions, and definitions of polarization; these differences remain insufficiently resolved in the supplied evidence.
- Sources: S10, S8, S6, S12
- Rationale: The sources support that findings differ and that studies vary in platform, feed/ranking system, political context, timeframe, intervention, and exposure conditions. They also indicate that empirical evidence is inconsistent or nuanced and that open questions remain. However, the supplied text does not establish the full list of claimed sources of disagreement—especially different populations and definitions of polarization—or demonstrate that all these differences are insufficiently resolved.
- Supporting text: S10 compares Facebook and Instagram during the 2020 US election and reports no significant polarization effects after switching to chronological feeds. S8 describes a 2023 US-based, seven-week experiment on X with a different feed comparison and reports a political shift. S6 reports German panel experiments in which like-minded exposure increased polarization, but algorithmic selection generally did not amplify it. S12 says empirical studies offer a “much more nuanced view” and identifies questions that remain open.

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
- `structured_claim_evidence_available`: PASS
- `ledger_claim_ids_unique`: PASS
- `ledger_evidence_relationships_resolve`: PASS
- `ledger_confidence_values_valid`: PASS
- `ledger_evidence_ids_unique`: NOT_EVALUABLE — Current ledger relations have no independent evidence-ID field.

## Main Weaknesses

1. R1: Define political polarization and distinguish it from related outcomes such as ideological exposure, engagement, media diversity, political knowledge, partisan following, or general political activity.
2. R5: Distinguish the causal strength and limitations of the main types of evidence.
3. R4: Evaluate whether recommendation algorithms cause politically relevant behavioral changes.
4. 3 cited finding(s) were not fully supported by saved evidence.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `0a6b1b066d5fe11922b29a875e67b54f06d262533b8526272d8d350999e2c54e`
- Candidate report hash: `be5bd75e7567efbf9dcdc60bb2c26715faff61d7d82bdc6ca53575cdead751bc`
- LLM calls: 7
- Evaluated at: 2026-09-01T01:16:20.233417+00:00
