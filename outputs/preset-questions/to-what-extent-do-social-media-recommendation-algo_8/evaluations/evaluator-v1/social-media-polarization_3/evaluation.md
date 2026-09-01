# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** social-media-polarization

**System Version:** llm-only-baseline-v0

**Model:** gpt-5.6-luna

## Summary

- Overall: 58.0 / 100
- Evaluation completeness: 100%
- Comprehensiveness: 0.80
- Coverage: 0.82
- Depth: 0.75
- Citation quality: 0.00
- Citation validity: 0.00
- Citation support: 0.00
- Citation completeness: 0.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report correctly avoids equating changed exposure with polarization and recognizes affective, ideological, behavioral, and segregation-related dimensions. However, its conceptual treatment is mostly classificatory rather than a clear definition and systematic differentiation of all requested related outcomes.
- Candidate evidence:
  - The report distinguishes “political exposure” from downstream outcomes, stating that “exposure is not equivalent to persuasion.”
  - It identifies multiple polarization dimensions: “ideological extremity, partisan issue attitudes, dislike of the opposing party, perceived disagreement, ideological segregation, hostility, or partisan behavior.”
  - It explicitly notes that algorithms may increase “hostile content exposure” without changing “vote choice.”
- Missing:
  - It does not give a concise, affirmative definition of political polarization itself; instead, it mainly lists possible dimensions and related outcomes.
  - The distinctions among polarization, ideological exposure, engagement, media diversity, political knowledge, and general political activity are present but not systematically developed.

### R2

- Coverage: 1.00
- Depth: 0.75
- Rationale: This requirement is substantively addressed: the report clearly separates algorithmic ordering from user choice and network composition and cites several forms of exposure evidence. Depth is reduced by the absence of quantitative estimates and fuller treatment of content-supply effects.
- Candidate evidence:
  - It states that recommendation systems “rank, filter, and amplify some political content.”
  - It reports that Facebook ranking reduced cross-cutting exposure, while “users' choices accounted for a larger share of the reduction.”
  - It describes a Facebook experiment comparing personalized and reverse-chronological feeds and an Instagram experiment comparing ranked and chronological feeds.
  - It separately discusses follows, clicks, reading, sharing, networks, subscriptions, search behavior, and broader media markets as sources of exposure beyond ranking.
  - It reports Twitter/X evidence that engagement-based timelines can amplify emotionally charged or ideologically distinct messages.
- Missing:
  - The report gives few quantitative effect sizes or precise estimates for how large the exposure changes were.
  - Evidence on content supply, candidate pools, and recommendation versus ranking is discussed only briefly, rather than analyzed in detail.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report clearly separates feed composition from attitudes and gives a balanced account of null, mixed, and backlash findings. It falls short of full depth because the requested magnitude and statistical uncertainty are described qualitatively rather than with study-level estimates.
- Candidate evidence:
  - It separately concludes that changing exposure “does not reliably produce immediate changes in political beliefs, affective polarization, or political behavior.”
  - It reports that the Facebook and Instagram experiments produced substantial exposure changes but “little evidence of short-run changes in ideological attitudes or political evaluations.”
  - It discusses a randomized Twitter study in which opposing views made Republican participants “more conservative” and produced mixed effects among Democrats.
  - It distinguishes observational associations between homogeneous networks or hostile content and affective polarization from causal evidence, noting possible reverse causality.
  - It repeatedly characterizes effects as “limited,” “small,” “uncertain,” “mixed,” or “not meaningful” over short study periods.
- Missing:
  - The report does not provide concrete effect sizes, confidence intervals, p-values, or clearly specified statistical uncertainty for the attitude outcomes.
  - It does not consistently distinguish null findings from equivalence or low statistical power, although it mentions that some studies may be underpowered for small effects.
  - Evidence for durable belief change and partisan identity change is largely discussed as a gap rather than evaluated with specific studies.

### R4

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report appropriately covers online behavior and explicitly avoids inferring voting or participation from exposure. It gives a calibrated assessment of limited downstream behavioral evidence, but the treatment of direct political behavior is not as evidence-specific as the treatment of exposure.
- Candidate evidence:
  - It identifies changes in “likes, comments, resharing, time spent, and the amount of political material consumed” as genuine on-platform behavioral effects.
  - It explicitly warns that these effects “do not necessarily imply changes in voting, persuasion, or democratic participation.”
  - It states that evidence for turnout and downstream electoral behavior is “sparse, difficult to measure, and often underpowered for small effects.”
  - It reports that deactivation and feed interventions generally found “small or uncertain effects on turnout-related outcomes” and political participation.
- Missing:
  - The report provides limited direct evidence on voting, turnout, following, or offline participation beyond general claims about sparsity and uncertainty.
  - It does not clearly identify which specific behavioral findings are randomized, observational, or campaign-specific.

### R5

- Coverage: 0.75
- Depth: 0.75
- Rationale: The core causal hierarchy and major threats are well covered, especially randomized versus observational evidence. Full treatment would require explicit discussion of audits and simulations and more technical threats to randomized feed interventions.
- Candidate evidence:
  - It differentiates “large randomized interventions conducted on real platforms” from “long-term observational studies.”
  - It also refers to randomized Twitter studies, laboratory and field studies, observational studies, deactivation experiments, and feed-ranking interventions.
  - It identifies self-selection, reverse causality, preexisting polarization, network composition, media supply, and proprietary-system limitations as threats.
  - It notes that short randomized interventions have stronger causal identification but limited duration, while observational studies capture cumulative exposure but cannot cleanly separate algorithmic effects from confounding.
- Missing:
  - Audits and simulations are not separately evaluated, despite being relevant evidence types in the rubric.
  - Treatment noncompliance, contamination between treatment conditions, measurement error, and imperfect exposure manipulation are not substantially discussed.
  - The report does not explain in detail how laboratory, field, audit, and simulation designs differ in causal interpretation.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report explains why platform and intervention differences can generate divergent findings and recognizes limited U.S. generalizability. Its comparative analysis remains broad and does not concretely evaluate simulations or cross-national evidence.
- Candidate evidence:
  - It compares Facebook, Instagram, Twitter/X, YouTube, and other recommendation systems.
  - It contrasts ranked feeds with reverse-chronological or chronological feeds, reduced reshared political content, deactivation, and deliberate exposure to opposing views.
  - It states that findings may vary across “other countries, languages, media systems, and political environments.”
  - It notes differences in platform design, changing ranking objectives, moderation, available content, and user populations.
- Missing:
  - Country, language, election-timing, and user-composition differences are mostly mentioned as general limitations rather than compared with concrete findings.
  - Simulated environments are not actually compared with real-world feeds.
  - The report does not give detailed platform-by-platform or intervention-by-intervention estimates.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report covers heterogeneity, duration, algorithm change, and external validity and appropriately flags uncertainty. It lacks detailed evidence on cumulative persistence and feedback loops, so the treatment is strong but not complete.
- Candidate evidence:
  - It states that effects are heterogeneous by prior identity, partisan group, intervention, and outcome, including possible backlash among some users and partisan asymmetries.
  - It contrasts short-run randomized evidence with possible cumulative effects in longer-term observational studies.
  - It notes that platforms continuously modify ranking objectives and that results may not generalize to current systems.
  - It identifies “small susceptible subgroup[s]” as a topic requiring further research even when average effects are near zero.
  - It discusses repetition, social reinforcement, and diffusion as possible mechanisms while labeling recommendation-to-extremity effects contested and difficult to identify causally.
- Missing:
  - Evidence for long-term accumulation, feedback loops, and persistence is not directly established; these mechanisms are mostly presented as possibilities or research gaps.
  - The report does not systematically distinguish observed heterogeneity from hypothesized heterogeneity across exposure intensity and content types.
  - There is little concrete evidence on adolescents, low-information users, or other specific subgroups.

### R8

- Coverage: 1.00
- Depth: 0.75
- Rationale: The report provides the requested overall explanation and a well-calibrated conclusion, clearly separating exposure from attitudes and behavior. Its depth is slightly limited because some reasons for disagreement, especially power and substantive effect-size standards, are stated only generally.
- Candidate evidence:
  - The conclusion separately states that algorithms “demonstrably change political exposure” while the strongest causal evidence does not show “large immediate changes in political beliefs, affective polarization, or voting-related behavior.”
  - It gives a calibrated synthesis: algorithms are “an amplifier and gatekeeper of polarization, not a sufficient explanation for it.”
  - It explains disagreement through platform design, user selection, outcome definitions, time horizon, research method, causal identification, sample differences, and changing systems.
  - It preserves uncertainty by stating that algorithms can intensify polarization in particular environments but are not shown to be a general-purpose or dominant cause of mass belief change.
  - It notes that political polarization also reflects party sorting, elite rhetoric, traditional media, geography, institutions, and offline identities.
- Missing:
  - The synthesis does not discuss statistical power and effect-size thresholds in much detail, apart from a brief reference to studies being underpowered for small effects.
  - The conclusion could more explicitly separate evidence for different forms of online behavior from evidence for offline voting and participation.

### Novel Value

- No material benchmark-external value identified.

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

- Q1: Recommendation systems substantially change what political content users see by ranking, filtering, and amplifying some content.
- Q2: On Facebook, users’ ideological choices and algorithmic ranking both affect the diversity of political news in feeds, with user choices accounting for a larger share of the reduction in cross-cutting exposure in the cited 2015 study.
- Q3: Randomized changes from personalized to reverse-chronological Facebook feeds altered users’ exposure to like-minded and cross-cutting political sources.
- Q4: Changing Instagram from an algorithmically ranked feed to a chronological feed altered political-content exposure and the kinds of posts users engaged with.
- Q5: The engagement-based Twitter/X home timeline can amplify messages from political actors and sources that are more emotionally charged or ideologically distinct than those shown in a chronological timeline.
- Q6: Individual user choices account for more ideological segregation in Facebook news exposure than algorithmic ranking, although ranking has a measurable incremental effect.
- Q7: People frequently use ideologically congenial sources, while social networks, search behavior, and broader media markets also shape exposure alongside recommendation systems.
- Q8: Large randomized Facebook and Instagram feed experiments found substantial changes in political-content exposure and engagement but little or no short-run change in measured political knowledge, polarization, attitudes, or well-being.
- Q9: A Facebook intervention reducing reshared political content changed feed composition and reduced political-content consumption without clear changes in key political attitudes during the study period.
- Q10: A large Facebook deactivation experiment during the 2020 election reduced exposure to political news and altered some reported political experiences but found limited effects on measured political knowledge, polarization, or political participation over several weeks.
- Q11: Exposure to opposing political views can increase polarization in some contexts rather than moderate attitudes.
- Q12: In a randomized Twitter study, exposure to opposing views made Republican participants more conservative and produced mixed but sometimes polarizing effects among Democrats.
- Q13: Moral-emotional language and identity-congruent content receive greater diffusion on social media, potentially increasing out-group hostility and the visibility of polarizing material.
- Q14: Research on YouTube and other recommendation systems reports pathways by which repeated recommendations may lead users toward more ideologically extreme or conspiratorial material, although the magnitude and generality are contested.
- Q15: Observational studies associate ideologically homogeneous networks and partisan or hostile content with stronger affective polarization, but the associations may reflect reverse causality.
- Q16: Feed-ranking interventions changed likes, comments, resharing, time spent, and political-material consumption without necessarily changing voting, persuasion, or democratic participation.
- Q17: Platform design can affect whether users encounter calls to action, civic information, and mobilizing messages, making effects on turnout or participation plausible in specific campaigns.
- Q18: Large-scale deactivation and feed interventions generally find small or uncertain effects on turnout-related outcomes, political knowledge, and vote choice compared with their effects on platform use and content exposure.
- Q19: The literature reaches different conclusions because studies differ in platforms, algorithms, populations, interventions, and definitions of polarization.
- Q20: Feed-ranking experiments estimate the marginal effect of ordering posts from an existing network rather than the effects of joining a platform, acquiring a new partisan network, or being recommended into a new community.
- Q21: Political polarization can refer to ideological extremity, partisan issue attitudes, dislike of the opposing party, perceived disagreement, ideological segregation, hostility, or partisan behavior, and algorithms may affect these dimensions differently.
- Q22: Effects of algorithmically mediated exposure are heterogeneous: prior identities, responses to opposing content, and partisan asymmetries can affect exposure and response.
- Q23: Short randomized interventions provide stronger causal identification but limited duration, whereas long-term observational studies capture cumulative exposure but cannot cleanly separate algorithmic effects from self-selection and confounding.
- Q24: Results from Facebook’s 2020 feed or Twitter’s prior ranking system cannot automatically be generalized to current systems or to TikTok, YouTube, or Instagram because platforms change ranking objectives, recommendation systems, moderation, and available content.
- Q25: Algorithms influence visibility, repetition, social reinforcement, and diffusion speed, creating mechanisms through which partisan and inflammatory content can spread.
- Q26: User choice and preexisting partisan networks often explain more segregation than ranking alone.
- Q27: Political polarization predates social media and is also driven by party sorting, elite rhetoric, traditional media, geography, institutions, and offline social identities.
- Q28: Observational studies often report links between recommendation systems, extreme content, and polarization, whereas randomized platform experiments often find little attitude change.
- Q29: Public evidence about proprietary recommendation systems is incomplete because researchers often lack full ranking logs, user-level exposure histories, recommendation candidates, and information about model updates.
- Q30: There is more evidence for effects on engagement, content consumption, and ideological segregation than for effects on vote choice, turnout, or durable political-belief change.
- Q31: Most causal evidence comes from the United States and a limited number of platforms, so effects may differ in other countries, languages, media systems, and political environments.
- Q32: Social-media recommendation algorithms demonstrably change political exposure, but exposure is not equivalent to persuasion.
- Q33: The strongest causal evidence indicates that altering feed ranking or reducing political content can change consumption and on-platform behavior without producing large immediate changes in political beliefs, affective polarization, or voting-related behavior.
- Q34: Particular recommendation environments can intensify polarization through backlash to opposing views, emotional and identity-based amplification, repeated exposure, and reinforcement of homogeneous networks.
- Q35: Differences in platform design, user selection, outcome definitions, time horizon, and research method help explain why the literature appears divided.

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

1. 35 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `0a6b1b066d5fe11922b29a875e67b54f06d262533b8526272d8d350999e2c54e`
- Candidate report hash: `0583ddfa87a95f6416701e0a79a415627758eae82adecfb527710f274e28d9ef`
- LLM calls: 2
- Evaluated at: 2026-09-01T06:03:40.237251+00:00
