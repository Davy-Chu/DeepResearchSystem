# Frozen Reference Research Evaluation

**Evaluator:** evaluator-v1

**Fixture:** social-media-polarization

**System Version:** llm-only-baseline-v0

**Model:** gpt-5.6-luna

## Summary

- Overall: Unavailable
- Evaluation completeness: 80%
- Comprehensiveness: 0.79
- Coverage: 0.82
- Depth: 0.73
- Citation quality: Unavailable
- Citation validity: 0.00
- Citation support: 0.00
- Citation completeness: Unavailable
- Deterministic integrity: 1.00

## Comprehensiveness

### R1

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report clearly identifies several forms of polarization and warns that exposure is not polarization itself. Its conceptual treatment is substantial, but some related outcomes are only mentioned indirectly or not defined.
- Candidate evidence:
  - The report defines ideological, affective, perceived, social/network, behavioral, and epistemic polarization.
  - It explicitly states that “a major source of disagreement” is treating outcomes as interchangeable and distinguishes exposure, attention, beliefs, and behavior.
  - It gives examples such as exposure changing perceived polarization without changing policy preferences, or hostile material increasing affective hostility without changing voting behavior.
- Missing:
  - The report does not systematically distinguish polarization from every listed related outcome, particularly political knowledge, media diversity, and general political activity.
  - The boundary between network polarization and exposure/segregation is discussed but not fully conceptualized.

### R2

- Coverage: 1.00
- Depth: 0.75
- Rationale: This requirement is fully addressed substantively: the report separates ranking from following, clicking, searching, networks, and content supply, and supplies platform-specific evidence. Depth is slightly reduced by limited quantitative detail.
- Candidate evidence:
  - The report states that ranking systems change which news sources users encounter, ideological cross-cutting exposure, emotional and antagonistic content visibility, political-topic salience, and spread of low-quality content.
  - Bakshy, Messing, and Adamic are used to distinguish user choice from ranking effects; the report says user choice explained more of the reduction in cross-cutting exposure while ranking still had a measurable effect.
  - The Twitter discussion cites Huszár et al. and explicitly says the study measured visibility and engagement rather than persuasion.
  - The report compares Facebook, Twitter/X, YouTube, Instagram, and TikTok, including differences between algorithmic and chronological presentation.
- Missing:
  - It generally reports direction and qualitative magnitude rather than concrete effect sizes or confidence intervals.
  - Evidence for Instagram and TikTok is characterized broadly, with few specific studies or quantified findings.

### R3

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report makes the crucial exposure-versus-attitude distinction and presents both null and backlash evidence. It does not fully characterize the magnitude and uncertainty of downstream effects with the precision required for complete coverage.
- Candidate evidence:
  - The report explicitly separates exposure from persuasion and says observational associations do not establish algorithmic effects.
  - It describes randomized 2020 Facebook and Instagram interventions that substantially changed information environments but generally produced little or no measurable short-term change in core political attitudes.
  - It discusses deactivation experiments and notes effects on some beliefs while emphasizing that results were not uniformly large.
  - The Bail et al. opposing-view experiment is used to show that cross-cutting exposure can sometimes increase polarization, especially among strongly identified users.
  - The report identifies possible reinforcement, resistance, fatigue, counter-mobilization, and disengagement rather than assuming a uniform direction.
- Missing:
  - The report rarely gives numerical effect sizes, confidence intervals, or formal statistical uncertainty beyond terms such as “not significant,” “small,” and “mixed.”
  - It gives limited direct evidence about changes in partisan identity, policy attitudes, or durable affective polarization specifically, as opposed to general claims about political attitudes.
  - The causal contribution of recommendation algorithms is not cleanly isolated in several cited deactivation and exposure studies.

### R4

- Coverage: 0.75
- Depth: 0.50
- Rationale: The report addresses the behavioral question and appropriately states that direct offline evidence is limited. However, it provides substantially less concrete evidence than for exposure and attitudes.
- Candidate evidence:
  - The report identifies online and offline behavioral outcomes including sharing, following, joining groups, donations, petitions, contacting politicians, harassment, collective action, abstention, and voting.
  - It states that evidence is strongest for online behaviors such as viewing, sharing, commenting, following, and joining, and weaker for offline actions such as voting.
  - It discusses Facebook deactivation reducing political knowledge and political activity, while finding no strong evidence of large changes in polarization or voting-related outcomes.
  - It argues that algorithms may function more as mobilization and coordination systems than as engines of ideological conversion.
- Missing:
  - Most behavioral claims are conceptual or general rather than supported by specific causal behavioral studies and quantified results.
  - The report does not clearly distinguish recommendation-driven behavior from behavior caused by other platform functions such as posting, social connection, or general news exposure, except for noting this limitation in deactivation studies.
  - Offline participation and voting evidence remains very thin.

### R5

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report gives a strong general account of causal identification and major confounding problems, especially selection and treatment-isolation issues. It falls short of complete coverage because several rubric-specified designs and threats receive little or no treatment.
- Candidate evidence:
  - The report distinguishes observational studies from randomized feed interventions and deactivation experiments, and separately discusses audits and platform-data studies.
  - It identifies self-selection, user preferences, network structure, content-supply confounding, offline polarization, reverse causality, and campaign targeting as threats to observational inference.
  - It explains that randomized feed experiments improve causal identification but are often short-term, platform-specific, expensive, and potentially affected by users obtaining information elsewhere.
  - It notes that deactivation cannot cleanly isolate recommendation effects from social connection, posting, news exposure, and interpersonal interaction.
- Missing:
  - Simulations are not meaningfully discussed.
  - Important experimental threats such as noncompliance, treatment contamination, and measurement error are not developed explicitly.
  - The relative causal strength of audits, surveys, and platform observational studies could be differentiated more systematically.

### R6

- Coverage: 0.75
- Depth: 0.75
- Rationale: There is substantial cross-platform and intervention comparison, with useful scope cautions. Coverage is incomplete for cross-national, linguistic, population-composition, and simulated-setting variation.
- Candidate evidence:
  - The report compares Facebook, Twitter/X, YouTube, Instagram, and TikTok and explains that ranking friends’ posts differs from recommending unfamiliar videos.
  - It contrasts real-world algorithmic feeds with chronological feeds, reranking interventions, deactivation, and YouTube recommendation audits.
  - It warns that Facebook findings from the 2020 U.S. election should not automatically generalize to YouTube or TikTok.
  - It notes variation by platform, user, topic, and definition of polarization, and discusses exposure during elections, crises, and political violence as potentially different settings.
- Missing:
  - Country and language differences are only lightly addressed; the report mentions Twitter findings in several countries but does not analyze how political contexts differ.
  - Differences in election timing, user composition, and platform penetration are not developed in detail.
  - Simulated environments are not compared because they are not discussed.

### R7

- Coverage: 0.75
- Depth: 0.75
- Rationale: The report directly addresses subgroup variation and time horizon and appropriately flags uncertainty about cumulative mechanisms. It would need more empirical support and clearer separation of demonstrated versus speculative heterogeneity for full credit.
- Candidate evidence:
  - The report discusses heterogeneity by partisan engagement, age, prior beliefs, local versus national content, video versus text, and offline-network isolation.
  - It explains that average treatment effects can conceal effects on small but consequential subgroups.
  - It addresses repeated exposure, migration into extreme communities, network changes, normalization, online/offline feedback, and changing algorithms as possible long-term processes.
  - It explicitly says evidence for large subgroup effects is plausible but insufficiently measured and that short experiments cannot establish cumulative effects.
- Missing:
  - Evidence-supported heterogeneity is not consistently separated from proposed mechanisms; many subgroup claims are presented as possibilities rather than findings.
  - Persistent effects, feedback loops, and long-term accumulation are discussed mainly as hypotheses, with few empirical results.
  - Changing algorithms and external validity are noted but not examined with concrete comparative evidence.

### R8

- Coverage: 1.00
- Depth: 0.75
- Rationale: The report provides a nuanced and well-calibrated synthesis that directly answers why the literature differs and separates exposure from downstream effects. Its main limitation is that statistical uncertainty and outcome-specific effect sizes are discussed qualitatively rather than rigorously.
- Candidate evidence:
  - The conclusion separately characterizes strong evidence for altered visibility and weaker evidence for altered beliefs or behavior.
  - The report explains divergent findings through differences in platforms, outcomes, periods, populations, user selection, algorithmic ranking, time horizon, measurement, intervention type, and network context.
  - It gives a calibrated overall assessment: algorithms are “significant contributors to polarized political information environments” but are not shown to be the main cause of mass polarization or to routinely transform beliefs.
  - It preserves uncertainty by distinguishing immediate experimental null results from possible cumulative and subgroup effects.
  - The report presents a conditional model in which exposure may produce reinforcement, mobilization, backfire, disengagement, or little durable change.
- Missing:
  - Statistical power and explicit effect-size thresholds are not directly discussed as reasons for disagreement.
  - The synthesis could more explicitly distinguish whether evidence supports contributions to affective, ideological, epistemic, and behavioral polarization separately rather than primarily discussing them in aggregate.

### Novel Value

- No material benchmark-external value identified.

## Citations

### Support

### Missing Citations

- None identified.

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

## Audit Metadata

- Fixture version: 1.0
- Rubric hash: `0a6b1b066d5fe11922b29a875e67b54f06d262533b8526272d8d350999e2c54e`
- Candidate report hash: `d428098f264ff5209c67590d2bfc3026970bb1fb6e988223953d5e387e4b30e4`
- LLM calls: 3
- Evaluated at: 2026-08-31T23:47:50.596779+00:00
