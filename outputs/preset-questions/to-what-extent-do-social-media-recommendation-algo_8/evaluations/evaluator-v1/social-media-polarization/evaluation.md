# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** social-media-polarization

**System Version:** llm-only-baseline-v0

**Model:** gpt-5.6-luna

## Summary

- Overall: 56.1 / 100
- Evaluation completeness: 80%
- Comprehensiveness: 0.77
- Coverage: 0.79
- Depth: 0.73
- Citation quality: 0.00
- Citation validity: 0.00
- Citation support: 0.00
- Citation completeness: 0.00
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report clearly recognizes that exposure, engagement, and segregation are not identical to polarization and names relevant attitudinal and behavioral forms. Its conceptual treatment is substantial but somewhat embedded in the discussion rather than sharply defined.
- Candidate evidence:
  - The report distinguishes exposure from polarization: “exposure is not equivalent to persuasion.”
  - It identifies multiple polarization dimensions, including “ideological extremity, partisan issue attitudes, dislike of the opposing party, perceived disagreement, ideological segregation, hostility, or partisan behavior.”
  - It separately discusses engagement, political knowledge, content consumption, and ideological segregation rather than treating all of them as polarization.
- Missing:
  - The report does not provide a concise, explicit definition of political polarization as a concept before listing its dimensions.
  - The relationship among affective polarization, ideological polarization, behavioral polarization, and exposure outcomes could be more systematically specified.

### R2

- Coverage: 1.00
- Depth: 0.75
- Rationale: This requirement is fully addressed substantively: the report separates algorithmic ranking from user choice and network composition and presents evidence on cross-cutting exposure, amplification, and political-content consumption. Quantitative detail would improve depth.
- Candidate evidence:
  - It states that recommendation systems “rank, filter, and amplify some political content.”
  - It reports that Facebook ranking reduced cross-cutting exposure, while “users’ choices accounted for a larger share of the reduction.”
  - It describes randomized Facebook and Instagram experiments comparing personalized/ranked feeds with chronological feeds and says these changed political content exposure.
  - It discusses Twitter/X evidence that engagement-based ranking can amplify emotionally charged or ideologically distinct messages.
  - It explicitly distinguishes ranking from follows, clicks, reading, sharing, network composition, and content supply.
- Missing:
  - The report gives few quantitative effect sizes or precise estimates of how large the exposure changes were.
  - The evidence on content-supply effects and recommendation candidate generation is mentioned more as a limitation than evaluated in detail.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report strongly separates exposure from beliefs and attitudes and gives both null and positive causal evidence. It is not fully deep because it lacks quantitative estimates and more explicit treatment of precision and substantive magnitude.
- Candidate evidence:
  - It separately evaluates downstream outcomes and states that exposure changes “do not reliably produce immediate changes in political beliefs, affective polarization, or political behavior.”
  - It reports that the Facebook and Instagram experiments changed exposure but found “little evidence of short-run changes in ideological attitudes or political evaluations.”
  - It identifies a randomized Twitter study in which opposing views made Republican participants “more conservative” and produced mixed effects among Democrats.
  - It distinguishes observational associations from causal evidence and notes that already-polarized users may seek partisan or hostile content.
  - It repeatedly qualifies the findings as short-run, mixed, and context-dependent.
- Missing:
  - The report provides little numerical information about effect sizes, confidence intervals, or statistical uncertainty beyond qualitative terms such as “little,” “mixed,” and “uncertain.”
  - The evidence for changes in partisan identity and durable policy attitudes is less directly developed than the evidence for general attitudes or affective polarization.
  - The report does not clearly distinguish null results from evidence that effects are substantively negligible versus statistically imprecise.

### R4

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report correctly treats on-platform behavioral changes separately from downstream political behavior and does not infer voting effects from engagement. Coverage is good, but the behavioral evidence review remains relatively brief and largely qualitative.
- Candidate evidence:
  - It reports changes in “likes, comments, resharing, time spent, and the amount of political material consumed.”
  - It explicitly warns that these “do not necessarily imply changes in voting, persuasion, or democratic participation.”
  - It states that evidence for downstream electoral behavior is “sparse, difficult to measure, and often underpowered for small effects.”
  - It notes that deactivation and feed interventions generally found “small or uncertain effects on turnout-related outcomes” and political participation.
- Missing:
  - Direct causal evidence concerning voting, turnout, offline participation, or vote choice is not presented in much detail.
  - The report mentions mobilization and calls to action as plausible pathways but does not provide a clearly identified causal estimate of such effects.
  - The distinction among different forms of online behavior, political participation, and electoral behavior could be more systematically evaluated.

### R5

- Coverage: 0.75
- Depth: 0.75
- Rationale: The major evidence designs and important confounding threats are covered well. It falls short of full depth because several specific threats and design classes in the rubric are omitted.
- Candidate evidence:
  - It distinguishes “large randomized platform experiments,” randomized Twitter exposure, observational studies, laboratory and field studies, and deactivation interventions.
  - It explains that randomized interventions have stronger causal identification but usually short duration, while observational studies capture cumulative exposure but cannot separate algorithmic effects from self-selection and confounding.
  - It identifies self-selection, preexisting polarization, user networks, content supply, reverse causality, proprietary-system opacity, and limited exposure histories as threats.
  - It notes that a feed-ranking experiment tests the marginal effect of ordering posts in an existing network rather than joining a platform or entering a new community.
- Missing:
  - Audits and simulations are not explicitly characterized as distinct evidence types, despite the rubric requesting them.
  - Noncompliance, treatment contamination, and measurement error are not discussed explicitly.
  - The report could say more about how deactivation, reranking, and chronological-feed treatments differ in causal estimand and implementation.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report gives a meaningful cross-platform and cross-design comparison and identifies important scope limits. It would need more concrete country, election-period, population, and simulation comparisons for full coverage.
- Candidate evidence:
  - It compares Facebook, Instagram, Twitter/X, YouTube, and other recommendation environments.
  - It distinguishes ranked-feed interventions, chronological substitutions, deactivation, reduced reshared political content, deliberate exposure to opposing views, and observational studies.
  - It states that findings vary by “platform, political group, intervention, and outcome.”
  - It notes that most causal evidence is from the United States and that effects may differ across “countries, languages, media systems, and political environments.”
  - It explains that platform design, moderation, ranking objectives, and algorithm updates limit generalization.
- Missing:
  - Election timing is not analyzed in detail, even though the report refers generally to the 2020 election.
  - Differences in user composition and political context are noted but not developed with concrete comparative examples across countries or populations.
  - Simulated environments are not directly compared with real-world feeds.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report addresses subgroup variation, outcomes, time horizon, algorithm change, and possible feedback mechanisms. Its treatment is appropriately cautious but could more sharply distinguish established heterogeneity from plausible but unverified long-term mechanisms.
- Candidate evidence:
  - It reports heterogeneity by political group: opposing exposure made Republicans more conservative and had mixed effects among Democrats.
  - It states that effects vary across users with strong prior identities and that some users may resist while others assimilate or experience backlash.
  - It discusses short-run randomized studies versus longer-term observational evidence and identifies cumulative exposure as a possible distinction.
  - It notes changing algorithms, feedback through visibility and social reinforcement, and the possibility that a small susceptible subgroup experiences large effects despite near-zero average effects.
  - It explicitly identifies longer-term tracking and heterogeneous-effects research as gaps.
- Missing:
  - The report does not clearly separate evidence-supported heterogeneity from speculative mechanisms such as cumulative feedback loops and long-term accumulation.
  - Persistent or multi-election effects are mostly identified as unknown rather than evaluated using existing evidence.
  - Exposure intensity and dose-response relationships receive limited direct treatment.

### R8

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report provides a well-calibrated overall conclusion and explains most major sources of disagreement. It is not fully comprehensive because statistical power, substantive-effect thresholds, and construct-specific conclusions are not developed equally.
- Candidate evidence:
  - The conclusion separately states that algorithms “demonstrably change political exposure” while the strongest causal evidence does not show large immediate changes in beliefs, affective polarization, or voting-related behavior.
  - It explains disagreement through differences in platforms, algorithms, interventions, populations, definitions of polarization, user selection, causal design, and time horizon.
  - It gives a calibrated synthesis: algorithms are “an amplifier and gatekeeper of polarization, not a sufficient explanation for it.”
  - It preserves uncertainty by noting backlash, heterogeneous responses, proprietary-system limits, and limited evidence for durable belief or electoral change.
- Missing:
  - Statistical power and effect-size thresholds are mentioned only briefly through “underpowered for small effects” and are not integrated fully into the synthesis.
  - The report does not explicitly discuss how researchers’ thresholds for calling an effect politically important contribute to disagreement.
  - The overall assessment could more clearly distinguish the extent of contribution to affective polarization, ideological extremity, and political behavior rather than summarizing them together.

### Novel Value

- The report offers a useful two-stage synthesis: algorithms have strong evidence of changing exposure and engagement, but much weaker evidence of changing durable beliefs or electoral behavior.
- It emphasizes that user choice and network composition may account for more ideological segregation than ranking alone, preventing an overly algorithm-centric explanation.
- It reconciles apparently conflicting findings by distinguishing marginal feed-ranking interventions from broader processes such as network formation, cumulative exposure, and platform participation.
- It identifies a potentially important but unresolved possibility of large effects among susceptible subgroups despite small population-average effects.

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

- Q1: Recommendation systems substantially change which political content users see, including the prevalence of like-minded and cross-cutting sources.
- Q2: On Facebook, both users’ ideological choices and algorithmic ranking affect the diversity of political news in feeds, with user choices accounting for a larger share of reduced cross-cutting exposure in the cited 2015 study.
- Q3: Changing Facebook from a personalized ranked feed to a reverse-chronological feed altered the political content users encountered.
- Q4: Changing Instagram from an algorithmically ranked feed to a chronological feed altered political-content exposure and the kinds of posts users engaged with.
- Q5: Engagement-based ranking on Twitter/X can amplify messages from political actors and sources that are more emotionally charged or ideologically distinct than those seen in a chronological timeline.
- Q6: Users’ choices about whom to follow, click, read, and share are an important source of selective exposure and can account for more ideological segregation than algorithmic ranking.
- Q7: Large randomized Facebook and Instagram feed experiments found substantial changes in political exposure and engagement but little or no short-run change in political knowledge, polarization, political attitudes, ideological attitudes, political evaluations, or well-being across their main outcomes.
- Q8: A Facebook intervention reducing reshared political content changed feed composition and reduced political-content consumption without producing clear changes in key political attitudes during the study period.
- Q9: A large Facebook deactivation experiment during the 2020 election reduced exposure to political news and altered some reported political experiences, while finding limited evidence of effects on political knowledge, polarization, or political participation over several weeks.
- Q10: In a randomized Twitter study, exposure to opposing political views made Republican participants more conservative and produced mixed but sometimes polarizing effects among Democrats.
- Q11: Moral-emotional language and identity-congruent content receive greater diffusion in social-media sharing, potentially increasing out-group hostility and the visibility of polarizing material.
- Q12: Research on YouTube and other recommendation systems reports pathways through which repeated recommendations may lead users toward more ideologically extreme or conspiratorial material, although the magnitude and generality of the effect are contested.
- Q13: Observational studies associate ideologically homogeneous networks and exposure to partisan or hostile content with stronger affective polarization, although reverse causality is also compatible with those associations.
- Q14: Feed-ranking interventions changed likes, comments, resharing, time spent, and the amount of political material consumed.
- Q15: Platform design can affect whether users encounter calls to action, civic information, and mobilizing messages, making effects on turnout or participation plausible in specific campaigns.
- Q16: Large-scale deactivation and feed interventions have generally found small or uncertain effects on turnout-related outcomes, political knowledge, and vote choice compared with their effects on platform use and content exposure.
- Q17: The literature reaches different conclusions in part because studies examine different platforms, algorithms, populations, interventions, time horizons, and definitions of polarization.
- Q18: Polarization has been operationalized as ideological extremity, partisan issue attitudes, dislike of the opposing party, perceived disagreement, ideological segregation, hostility, or partisan behavior, and an algorithm may affect one dimension without affecting another.
- Q19: Short randomized interventions provide stronger causal identification but usually have limited duration, whereas long-term observational studies capture cumulative exposure but cannot cleanly separate algorithmic effects from self-selection and confounding.
- Q20: Platforms continuously modify ranking objectives, recommendation systems, moderation, and available content, limiting the generalizability of findings from Facebook’s 2020 feed or earlier Twitter ranking systems to current systems and other platforms.
- Q21: Political polarization predates social media and is also driven by party sorting, elite rhetoric, traditional media, geography, institutions, and offline social identities.
- Q22: The evidence is stronger for effects on engagement, content consumption, and ideological segregation than for effects on vote choice, turnout, or durable political-belief change.
- Q23: Most causal evidence comes from the United States and a limited number of platforms, so effects may differ in other countries, languages, media systems, and political environments.
- Q24: Recommendation algorithms demonstrably affect visibility, repetition, social reinforcement, and the speed of diffusion of political content.
- Q25: The strongest overall interpretation is that recommendation algorithms are amplifiers and gatekeepers within a broader polarization ecosystem, rather than a sufficient or general-purpose explanation for polarization.

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

1. R4: Evaluate whether recommendation algorithms cause politically relevant behavioral changes.
2. 25 citation-required claim(s) lacked an appropriate citation.

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `0a6b1b066d5fe11922b29a875e67b54f06d262533b8526272d8d350999e2c54e`
- Candidate report hash: `0583ddfa87a95f6416701e0a79a415627758eae82adecfb527710f274e28d9ef`
- LLM calls: 2
- Evaluated at: 2026-09-01T05:51:15.712414+00:00
