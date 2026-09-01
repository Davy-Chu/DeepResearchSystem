# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** social-media-polarization

**System Version:** llm-only-baseline-v0

**Model:** gpt-5.6-luna

## Summary

- Overall: 59.3 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.82
- Coverage: 0.82
- Depth: 0.82
- Citation quality: 0.00
- Citation validity: 0.00
- Citation support: 0.00
- Citation completeness: 0.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report clearly conceptualizes multiple forms of polarization and separates exposure and engagement from attitudinal and behavioral polarization. It also explains that the same intervention can affect expressive hostility without changing policy preferences.
- Candidate evidence:
  - The report defines ideological, affective, perceptual, epistemic, and behavioral polarization in Section 1.
  - It explicitly states that “Evidence is strongest for the first link” in the exposure chain and warns: “It is therefore important not to treat evidence that algorithms change exposure as evidence that they change political beliefs.”
  - It distinguishes exposure, attention, engagement, internalization, and behavioral consequence in Section 5.5, and discusses engagement, media diversity, knowledge, partisan following, and political activity separately.
- Missing:

### R2

- Coverage: 1.00
- Depth: 1.00
- Rationale: This requirement is thoroughly addressed with platform-specific evidence, distinctions between ranking and user selection, and discussion of ideological slant, emotional content, engagement optimization, and segregation.
- Candidate evidence:
  - The report states that ranking systems “substantially alter exposure” and discusses algorithmic versus chronological feeds on Facebook/Instagram and Twitter/X.
  - It reports that Meta feed experiments changed exposure, political-material volume, engagement, and information-flow composition.
  - It describes Huszár and colleagues’ finding that Twitter’s ranking algorithm amplified right-leaning political content relative to reverse chronology.
  - It explicitly contrasts algorithmic selection with user choices: whom users “follow, friend, click, and engage with,” citing Bakshy, Messing, and Adamic’s finding that user choice could contribute more to segregation than ranking.
- Missing:

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report makes the crucial exposure-versus-belief distinction and gives a reasonably nuanced causal synthesis, but its characterization of magnitude and statistical uncertainty is mostly qualitative and some positive findings remain nonspecific.
- Candidate evidence:
  - The report separately evaluates political beliefs and states that large randomized Meta studies generally found “little or no effect” on political knowledge, issue positions, affective polarization, and related attitudes.
  - It discusses Bail et al.’s opposing-content experiment, reporting increased polarization among some participants, particularly Republicans.
  - It distinguishes intermediate outcomes such as anger, moral outrage, perceived threat, and group identification from durable changes in policy preferences or voting.
  - It notes that the strongest causal studies often find little short-term attitude change, while effects may be conditional on subgroup, exposure type, or duration.
- Missing:
  - The report rarely supplies numerical effect sizes, confidence intervals, or precise statistical uncertainty beyond phrases such as “little or no effect,” “some participants,” and “more limited.”
  - Several claims about experiments producing increased ideological extremity or attitude effects are not tied to specific studies or estimates.
  - The report does not consistently distinguish which findings concern ideological extremity, affective polarization, perceptual polarization, or policy attitudes in the cited evidence.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: It correctly covers online and offline behavioral outcomes and appropriately states that direct evidence for voting and durable participation effects is limited. Depth is reduced by the lack of specific causal estimates and by limited separation of ranking effects from downstream user adaptation.
- Candidate evidence:
  - The report separately discusses sharing, clicking, commenting, account reach, misinformation spread, and expressive behavior as outcomes influenced by ranking.
  - It states that evidence for turnout or vote choice is much weaker and reports that the 2020 Meta experiments found little evidence of broad participation or voting-related effects.
  - It distinguishes Facebook’s “I Voted” mobilization message from an ordinary recommendation algorithm.
  - For extremist and anti-democratic behavior, it describes plausible recommendation pathways but explicitly says that independent causal effects are difficult to establish because of active seeking, cross-platform movement, and offline organizations.
- Missing:
  - The report does not provide much direct causal evidence or quantitative estimates for sharing, engagement, participation, turnout, voting, or extremist behavior.
  - It sometimes moves from evidence that ranking affects clicks or shares to broad claims about recommendation systems without clearly separating algorithmic effects from user and creator responses.
  - Offline behavioral outcomes are mainly addressed through general conclusions rather than specific studies or experimental results.

### R5

- Coverage: 0.50
- Depth: 0.50
- Rationale: The report recognizes the core causal hierarchy and several major threats, especially self-selection and incomplete exposure manipulation, but it does not provide the systematic design-by-design causal assessment required for full coverage.
- Candidate evidence:
  - The report identifies large randomized feed interventions as the strongest recent evidence and contrasts them with observational studies of user choice and exposure.
  - It notes that Bail et al.’s experiment tested selected opposing content rather than a complete platform recommendation algorithm.
  - It discusses selection effects, reverse causation, user preferences, network formation, and the distinction between potential exposure, actual exposure, engagement, and internalization.
  - It mentions that observational studies cannot easily separate algorithms from self-selection and broader political trends.
- Missing:
  - Audits, simulations, surveys, and observational designs are not systematically differentiated or evaluated as separate evidence types.
  - Important experimental threats such as noncompliance, treatment contamination, attrition, treatment spillovers, and incomplete manipulation of personalization are only partly addressed; incomplete personalization is mentioned, but the others are not developed.
  - The report does not explain the causal limits of platform audits or simulations, nor how measurement error affects inference in a systematic way.
  - It does not identify the particular estimands or statistical-power limitations of the major randomized studies beyond general discussion.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: There is strong comparative framing across platforms, interventions, and political contexts, but the empirical comparison across countries, languages, populations, and study settings remains incomplete.
- Candidate evidence:
  - The report compares Facebook/Instagram, Twitter/X, YouTube, TikTok, Instagram, and encrypted messaging platforms, noting differences in user base, content format, ranking objective, and social context.
  - It contrasts chronological substitutions, reranking, opposing-content exposure, reduced political content, and ordinary recommendation systems.
  - It explains that effects may differ during elections, crises, protests, wars, and periods of institutional distrust.
  - It notes specific geographic variation in Twitter amplification, including greater right-leaning amplification in the United States and several examined countries.
- Missing:
  - Country, language, election-timing, and population differences are mostly listed as possible sources of variation rather than demonstrated with specific comparative evidence.
  - The report gives little discussion of non-U.S. findings beyond the Twitter example and does not analyze how platform design differs in concrete intervention results.
  - Simulated environments and audits are mentioned only indirectly and are not substantively compared with real-world feed experiments.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report addresses users, content, outcomes, intensity, cumulative exposure, and time horizon, and it acknowledges external-validity limits. However, it supplies little direct evidence establishing the size or robustness of these heterogeneous and long-term effects.
- Candidate evidence:
  - The report identifies possible subgroup differences involving highly partisan, politically attentive, younger, highly engaged, politically inattentive, weakly opinionated, and isolated users.
  - It distinguishes conditional effects on affective hostility from effects on policy positions and notes that average treatment effects can conceal subgroup effects.
  - It discusses short experiments versus cumulative exposure over months or years, along with identity reinforcement, norm changes, migration into isolated communities, and elite adaptation.
  - It acknowledges that long-term accumulation is a plausible mechanism but that short experiments may underestimate it and observational studies cannot easily identify it.
- Missing:
  - Most subgroup and long-term claims are presented as hypotheses or plausible mechanisms rather than evidence-supported heterogeneity with study-specific estimates.
  - Feedback loops and changing algorithms are mentioned only briefly; persistent effects, decay, and repeated exposure are not empirically assessed.
  - The report does not clearly distinguish which proposed heterogeneity findings have been demonstrated from which remain speculative, aside from general caveats.

### R8

- Coverage: 1.00
- Depth: 1.00
- Rationale: The report provides a calibrated overall assessment, directly explains why studies reach different conclusions, and preserves the distinction between exposure effects and downstream belief or behavioral effects.
- Candidate evidence:
  - The report’s central synthesis distinguishes strong evidence that algorithms change exposure from weaker and mixed evidence that they change beliefs or behavior.
  - Section 5 identifies different causal estimands, interventions, time horizons, selection processes, attention versus exposure, users, platforms, political contexts, and polarization measures as reasons for disagreement.
  - The conclusion describes algorithms as “conditional amplification,” says they are not a “dominant, general-purpose cause” of mass polarization, and states that effects are “smaller, more conditional, and less uniform” than often claimed.
  - The confidence summary separately rates exposure and engagement effects as high confidence, affective and identity effects as moderate confidence, and broad ideological, voting, turnout, and national-level effects as low or mixed confidence.
- Missing:

### Novel Value

- The report offers a useful synthesis that frames recommendation systems as “conditional amplification” and as a multiplier or accelerator interacting with user choice rather than as a sole origin of polarization.
- Its staged causal model—ranking to exposure to attention and engagement to beliefs and emotions to behavior—organizes the evidence around the precise distinction in the question.
- It adds a nuanced distinction between changing policy beliefs and changing emotional reactions, expression, perceived norms, and polarized subcommunities.

## Citations

### Support

### Missing Citations

- Q1: Recommendation algorithms rank, filter, and repeatedly expose users to some political content while reducing exposure to other material.
- Q2: Recent randomized interventions conducted with Meta and Twitter/X often found that changing users’ feeds changed exposure and engagement but produced little or no measurable short-term change in political attitudes, polarization, or voting-related outcomes.
- Q3: The Facebook and Instagram 2020 election feed experiments found that algorithmic and chronological feeds produced substantially different patterns of exposure and that changing the feed affected engagement and information-flow composition without generally producing detectable changes in several political-attitude measures.
- Q4: Facebook users tend to see more content from politically like-minded sources than from opposing sources, while segregation attributable specifically to Facebook’s ranking algorithm was often smaller than segregation produced by users’ own choices.
- Q5: Twitter’s ranking algorithm amplified right-leaning political content relative to a reverse-chronological alternative in the countries examined, particularly in the United States.
- Q6: The Facebook emotional-contagion experiment found that reducing emotionally positive or negative posts affected the emotional tone of users’ own posts.
- Q7: Bakshy, Messing, and Adamic’s Facebook study found substantial ideological segregation in cross-cutting news exposure and estimated that individual choices contributed more to observed segregation than algorithmic ranking, although ranking still had a measurable effect.
- Q8: Brady and colleagues found that moral-emotional language increased the diffusion of political messages, especially within users’ own ideological communities.
- Q9: The 2023 randomized Facebook and Instagram interventions generally found little or no effect on political knowledge, issue positions, affective polarization, or reported political participation and voting-related outcomes over the study period.
- Q10: Bail and colleagues’ experiment exposing Twitter users to automated accounts posting opposing-party content increased political polarization among some participants, particularly Republicans in the study.
- Q11: The 2010 Facebook “I Voted” message was associated with increased turnout among some users.
- Q12: The 2020 Meta feed experiments found little evidence that short-term changes in algorithmic ranking significantly changed broad political participation outcomes.
- Q13: Engagement-based ranking tends to elevate moral-emotional language, anger, outrage, identity-based political content, sensational or misleading claims, and posts that provoke rapid reactions.
- Q14: Recommendation systems optimized for clicks, watch time, comments, or shares may favor content that provokes arousal, including anger and moral outrage.
- Q15: Platforms may contribute to radicalization by facilitating repeated exposure to conspiratorial narratives, extremist recruitment, social reinforcement, normalization of dehumanizing language, and coordination or mobilization.
- Q17: Most randomized experiments on recommendation algorithms last days or weeks, whereas polarization may develop through cumulative exposure over months or years.
- Q18: People with strong political views are more likely to seek partisan content, follow ideologically similar accounts, engage with outrage, join political groups, and believe identity-consistent misinformation.
- Q19: Recommendation systems may have stronger effects on politically inattentive users, younger users, highly engaged users, people with weak prior opinions, users isolated from alternative news, and people susceptible to social-identity or threat cues.
- Q20: Recommendation algorithms change the ordering and visibility of political content, create different information environments for different users, interact with user choices to produce ideological segregation, and affect engagement, sharing, and expressive behavior.
- Q21: There is limited and inconsistent evidence that ordinary recommendation systems generally cause large shifts in policy ideology, substantially increase the average user’s political extremity, determine vote choice, produce broad turnout changes, or constitute the primary cause of national-level polarization.
- Q22: Political polarization is also driven by partisan realignment, elite rhetoric, economic and racial conflict, institutional distrust, partisan media, geographic and social sorting, offline organizations, and major political events.

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

1. R5: Distinguish the causal strength and limitations of the main types of evidence.
2. 21 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `0a6b1b066d5fe11922b29a875e67b54f06d262533b8526272d8d350999e2c54e`
- Candidate report hash: `033679f9ad04c469b61970d91f852f052d665629fcff269a740eff26347db0ab`
- LLM calls: 2
- Evaluated at: 2026-09-01T01:03:11.472363+00:00
