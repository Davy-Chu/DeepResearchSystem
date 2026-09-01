# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** social-media-polarization

**System Version:** llm-only-baseline-v0

**Model:** gpt-5.6-luna

## Summary

- Overall: Unavailable
- Evaluation completeness: 80%
- Comprehensiveness: Unavailable
- Coverage: Unavailable
- Depth: Unavailable
- Citation quality: 0.00
- Citation validity: 0.00
- Citation support: 0.00
- Citation completeness: 0.00
- Deterministic integrity: 1.00

## Comprehensiveness

**NOT EVALUABLE:** ValidationError: 1 validation error for ComprehensivenessJudgment
requirements.1
  Value error, Every score below 1 requires a missing-item explanation [type=value_error, input_value={'requirement_id': 'R2', ... substantive coverage.'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.13/v/value_error

## Citations

### Support

#### F1: NOT_EVALUABLE

- Claim: Recommendation systems substantially change what political content users see.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F2: NOT_EVALUABLE

- Claim: Algorithms are not the only, and often not the largest, source of selective exposure; users actively choose whom to follow, click, read, and share.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F3: NOT_EVALUABLE

- Claim: Changing exposure does not reliably produce immediate changes in political beliefs, affective polarization, or political behavior.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F4: NOT_EVALUABLE

- Claim: There is credible evidence that some forms of algorithmically mediated exposure can increase polarization, especially when users are deliberately exposed to opposing political content or when content is emotionally provocative.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F5: NOT_EVALUABLE

- Claim: Algorithms can affect political behavior even when they do not measurably change general political beliefs, but the behavioral evidence is narrower and less consistent than the exposure evidence.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F6: NOT_EVALUABLE

- Claim: The literature reaches different conclusions because studies examine different platforms, algorithms, populations, interventions, and definitions of polarization.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

#### F7: NOT_EVALUABLE

- Claim: The strongest overall interpretation is that algorithms are an amplifier and gatekeeper of polarization, not a sufficient explanation for it.
- Sources: None
- Rationale: No complete saved source snapshot is available for every citation.
- Supporting text: Unavailable

### Missing Citations

- Q1: Recommendation systems rank, filter, and amplify some political content, thereby substantially changing the political content users encounter.
- Q2: In a 2015 Facebook observational study, algorithmic ranking reduced exposure to cross-cutting political content, while users’ own choices accounted for a larger share of the reduction.
- Q3: A large-scale Facebook experiment comparing a personalized feed with a reverse-chronological feed changed the political content users encountered, including the prevalence of like-minded and cross-cutting sources.
- Q4: An Instagram experiment comparing algorithmically ranked and chronological feeds altered exposure to political content and the types of posts users engaged with.
- Q5: Research on Twitter/X found that an engagement-based home timeline can amplify messages from political actors and sources that are more emotionally charged or ideologically distinct than those seen in a chronological timeline.
- Q6: Individual user choices produced more ideological segregation in Facebook news exposure than algorithmic ranking, although ranking had a measurable additional effect.
- Q7: People frequently use ideologically congenial news sources, while social networks, search behavior, and broader media markets also shape exposure.
- Q8: Large randomized interventions on Facebook and Instagram changed political exposure and engagement but generally found little or no short-run change in political knowledge, polarization, political attitudes, or well-being.
- Q9: A Facebook intervention reducing reshared political content changed feed composition and reduced political-content consumption without producing clear changes in key political attitudes during the study period.
- Q10: A large Facebook deactivation experiment during the 2020 election reduced exposure to political news and altered some reported political experiences but found limited evidence of effects on political knowledge, polarization, or participation over several weeks.
- Q11: In a randomized Twitter study, exposure to opposing political views made Republican participants more conservative and produced mixed but sometimes polarizing effects among Democrats.
- Q12: Moral-emotional language and identity-congruent content receive greater diffusion on social media, potentially increasing out-group hostility and the visibility of polarizing material.
- Q13: Research on YouTube and other recommendation systems reports pathways by which repeated recommendations may lead users toward more ideologically extreme or conspiratorial material, although the magnitude and generality of the effect are contested.
- Q14: Observational studies associate ideologically homogeneous networks and exposure to partisan or hostile content with stronger affective polarization.
- Q15: Feed-ranking interventions changed likes, comments, resharing, time spent, and the amount of political material consumed.
- Q16: Studies of social influence and political mobilization indicate that platform design can affect whether users encounter calls to action, civic information, and mobilizing messages.
- Q17: Large-scale deactivation and feed interventions have generally found small or uncertain effects on turnout-related outcomes, political knowledge, and vote choice compared with their effects on platform use and content exposure.
- Q18: A feed-ranking experiment tests the marginal effect of ordering posts from an existing network rather than the effects of joining a platform, acquiring a new partisan network, or being recommended into a new community.
- Q19: Political polarization can refer to ideological extremity, partisan issue attitudes, out-party dislike, perceived disagreement, ideological segregation, hostility, or partisan behavior.
- Q20: Effects of algorithmic exposure are heterogeneous: users with strong prior identities may respond differently, opposing content may moderate some users while provoking backlash in others, and partisan asymmetries have been reported in exposure and response.
- Q21: Short randomized interventions offer stronger causal identification but limited duration, whereas long-term observational studies capture cumulative exposure but cannot cleanly separate algorithmic effects from self-selection and confounding.
- Q22: Platforms continuously modify ranking objectives, recommendation systems, moderation, and available content, so results from Facebook’s 2020 feed or an earlier Twitter ranking system cannot automatically be generalized to current systems or other platforms.
- Q23: Political polarization predates social media and is also driven by party sorting, elite rhetoric, traditional media, geography, institutions, and offline social identities.
- Q24: Observational studies often report links between recommendation systems, extreme content, and polarization, while randomized platform experiments often find little attitude change.
- Q25: Public evidence about proprietary recommendation systems is incomplete because researchers often lack full ranking logs, user-level exposure histories, recommendation candidates, and information about model updates.
- Q26: The literature provides more evidence for effects on engagement, content consumption, and ideological segregation than for effects on vote choice, turnout, or durable political-belief change.
- Q27: Most causal evidence comes from the United States and a limited number of platforms, so effects may differ in other countries, languages, media systems, and political environments.
- Q28: Recommendation algorithms contribute meaningfully to polarization by amplifying and organizing polarizing material, but they are not demonstrated to be a dominant, general-purpose cause of polarization.
- Q29: The strongest causal evidence indicates that altering feed ranking or reducing political content can change consumption and on-platform behavior without producing large immediate changes in political beliefs, affective polarization, or voting-related behavior.
- Q30: Differences in platform design, user selection, outcome definitions, time horizon, and research method explain why the literature appears divided.

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

1. 30 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `0a6b1b066d5fe11922b29a875e67b54f06d262533b8526272d8d350999e2c54e`
- Candidate report hash: `0583ddfa87a95f6416701e0a79a415627758eae82adecfb527710f274e28d9ef`
- LLM calls: 3
- Evaluated at: 2026-09-01T06:01:47.805953+00:00
