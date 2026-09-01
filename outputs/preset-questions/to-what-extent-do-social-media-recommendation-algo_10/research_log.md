# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 10 / 10

**Unique Sources:** 21

**OpenAI Calls:** 11

**Tavily Calls:** 10

**Started:** 2026-09-01T04:15:30-04:00

**Ended:** 2026-09-01T04:18:44-04:00

**Total Runtime:** 194.10s

---

# Iteration 1

## 1. Search

**Query**

> To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions.

**Why this query**

This is the user's original research question.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S1 — Social Drivers and Algorithmic Mechanisms on Digital Media**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11373151
- **S2 — Effects of news media bias and social media algorithms on ...**
  URL: https://dr.lib.iastate.edu/server/api/core/bitstreams/679463ea-22c2-4102-8ebf-cc15b04f76c9/content
- **S3 — Algorithms may be making political polarization worse than we think**
  URL: https://dobetter.esade.edu/en/algorithms-political-decisions
- **S4 — The Role of Social Media Algorithms in Shaping Political Polarisation in the United States**
  URL: https://www.humanrightsresearch.org/post/the-role-of-social-media-algorithms-in-shaping-political-polarisation-in-the-united-states
- **S5 — How Does Social Media Impact Political Polarization?**
  URL: https://news.northeastern.edu/2025/11/27/social-media-political-polarization-research

**Search Duration:** 2.65s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The available evidence supports a distinction between algorithmic effects on exposure and effects on political beliefs or behavior: algorithms clearly rank, filter, and recommend political content, but the causal effect of that curation on polarization is less settled.

**Confidence:** High

**Why this confidence level**

Two sources directly distinguish the observable curation mechanism from the more difficult question of downstream political effects.

**Evidence**

- The review describes algorithms as highlighting and recommending posts, news, people, and groups, while concluding that their effects on polarization are not straightforward and require further empirical research. [S1]
- The thesis reports that the literature on whether social-media algorithms affect polarization produced an unclear picture and did not support a firm conclusion. [S2]

#### Finding 2

**Claim**

Algorithms change what users see by ranking content according to behavioral signals and predicted relevance, thereby altering visibility and sequencing even when content is not removed.

**Confidence:** Medium

**Why this confidence level**

The mechanism is consistently described, and S5 and S3 report empirical platform analyses, but the supplied material is largely secondary or summary-level rather than the full primary studies.

**Evidence**

- The described systems use likes, shares, comments, watch time, follows, searches, and prior engagement to rank, filter, and recommend content; algorithmic feeds differ from chronological feeds by organizing content according to predicted relevance. [S4]
- An experiment reported in the source reranked posts within users’ existing X feeds without removing posts, changing only their order and exposure prominence. [S5]
- A YouTube recommendation-network analysis reportedly found pathways from center-right material toward more extreme right material and disproportionate exposure to extreme opposing-view content. [S3]

#### Finding 3

**Claim**

There is some experimental evidence that changing algorithmic exposure can change affective political attitudes, but the evidence supplied does not establish broad effects on ideology, partisanship, voting, or other political behavior.

**Confidence:** Medium

**Why this confidence level**

The sources report randomized or quasi-experimental interventions, which are more informative about causality than observational correlations, but the underlying studies are not provided in full and the reported outcomes are narrow and partly inconsistent.

**Evidence**

- The reported browser-extension experiment with more than 1,200 participants changed the ranking of posts containing partisan animosity and antidemocratic attitudes; after one week, increased exposure reportedly made feelings toward the opposing party about two points colder, while decreased exposure made them about two points warmer. [S5]
- The source characterizes the outcome as a change in affective polarization, not as a demonstrated change in voting, political participation, policy preferences generally, or partisan identity. [S5]
- A separate reported X experiment comparing algorithmic and chronological feeds allegedly shifted policy and current-affairs attitudes toward more conservative positions, but did not substantially change partisanship or polarization. [S4]

#### Finding 4

**Claim**

The strongest supported interpretation is that algorithms may amplify or structure pre-existing political tendencies rather than independently creating polarization from nothing.

**Confidence:** Medium

**Why this confidence level**

This explanation is consistent across the review and mechanism-focused accounts, but the supplied evidence does not quantify how much polarization is attributable to algorithms versus users, political elites, media systems, or broader social conditions.

**Evidence**

- The review concludes that algorithms mostly reinforce existing social drivers and emphasizes a feedback loop between algorithmic mechanisms and social phenomena. [S1]
- The account of algorithmic feedback describes users selecting and engaging with ideologically congenial material while algorithms learn from those behaviors, making technological and psychological causes difficult to separate. [S4]
- The YouTube analysis is presented as evidence that recommender systems can intensify both in-group extremity and antagonistic exposure to the opposing group. [S3]

#### Finding 5

**Claim**

The literature reaches different conclusions partly because studies measure different outcomes and manipulate different parts of the media environment.

**Confidence:** High

**Why this confidence level**

The sources directly document differences in outcomes, designs, and the algorithm-user feedback problem, providing a well-supported explanation for divergent findings.

**Evidence**

- The supplied studies concern distinct outcomes: visibility and recommendation pathways, policy/current-affairs attitudes, affect toward the opposing party, partisanship, and polarization; effects appear for some outcomes but not others. [S3] [S4] [S5]
- The review explicitly says that algorithmic mechanisms are powered by social drivers, creating a feedback loop that complicates attempts to disentangle algorithmic effects from already-existing social phenomena. [S1]
- The reported reranking experiment changed the order of already-followed content, whereas other analyses examine naturally occurring recommendation networks or platform-level feed systems; these interventions do not test the same causal question. [S3] [S4] [S5]

### Conflicts Found

- The sources disagree about whether algorithmic curation produces measurable political change. S1 and S2 characterize the overall evidence as unclear or far from straightforward, while S5 reports a causal shift in affective polarization and S4 reports a shift in policy and current-affairs attitudes without a major change in polarization. [S1] [S2] [S4] [S5]
- S3 and S4 emphasize algorithms’ tendency to amplify extremity and antagonism, whereas S1 argues that algorithms mostly reinforce pre-existing social drivers. These positions are not necessarily mutually exclusive: amplification may occur while the principal source of polarization remains users’ prior preferences and social identities. [S1] [S3] [S4]
- The reported X findings differ in direction and scope: S4 describes movement toward more conservative attitudes under an algorithmic feed, while S5 describes warmer or colder feelings toward the opposing party depending on reranked exposure. The interventions and outcomes differ, so they cannot be treated as direct replications. [S4] [S5]

### Important Gaps

- How large are algorithmic effects relative to user self-selection, partisan identity, political elites, and legacy news media?
- Do short-term changes in affective feeling or policy attitudes persist over months or years?
- Is there reliable evidence that recommendation algorithms change political behavior, such as voting, protest, political participation, sharing, or willingness to engage across party lines?
- How representative are the reported platform experiments, given that they concern particular X users, a short duration, and platform-specific interventions?
- Do recommendation systems systematically increase ideological extremity, or do they sometimes expose users to opposing content in ways that reduce polarization?
- The supplied material does not provide the full methods, effect sizes, preregistration, attrition, or statistical uncertainty for the reported experiments.

**Analysis Duration:** 18.98s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The original question specifically asks for evidence about beliefs and behavior, but the supplied sources provide only limited, secondary reports of short-term attitude and affective changes and no strong evidence about behavior. A focused search for primary experimental and quasi-experimental studies would materially improve the answer and help resolve the apparent disagreement.

**Next Search**

> primary experimental evidence social media feed algorithms political polarization beliefs behavior chronological feed recommendation algorithm randomized study

---

# Iteration 2

## 1. Search

**Query**

> primary experimental evidence social media feed algorithms political polarization beliefs behavior chronological feed recommendation algorithm randomized study

**Why this query**

The original question specifically asks for evidence about beliefs and behavior, but the supplied sources provide only limited, secondary reports of short-term attitude and affective changes and no strong evidence about behavior. A focused search for primary experimental and quasi-experimental studies would materially improve the answer and help resolve the apparent disagreement.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S6 — The political effects of X’s feed algorithm**
  URL: https://www.nature.com/articles/s41586-026-10098-2
- **S7 — How do social media feed algorithms affect attitudes and ...**
  URL: https://cdr.lib.unc.edu/downloads/wp9891401
- **S8 — How X’s algorithm shifts political attitudes**
  URL: https://cepr.org/voxeu/columns/how-xs-algorithm-shifts-political-attitudes

**Search Duration:** 2.63s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new evidence strengthens the distinction between exposure effects and downstream political effects: feed algorithms substantially alter what users encounter and how they engage, but exposure changes do not consistently translate into polarization or broader political attitude change.

**Confidence:** High

**Why this confidence level**

S7 provides direct randomized evidence of large exposure changes without detectable polarization effects. S6 is a peer-reviewed Nature article reporting another randomized field experiment, but the supplied abstract is incomplete.

**Evidence**

- In a randomized 2020 Facebook and Instagram experiment, replacing algorithmic feeds with chronological feeds substantially changed users’ exposure to political, untrustworthy, uncivil, and ideologically mixed content, and reduced time spent and activity on the platforms. Yet it did not significantly change issue polarization, affective polarization, political knowledge, or other key attitudes during three months. [S7]
- The source explains that feed-ranking algorithms personalize the order of content using users’ past behavior and predictions based on similar users, making them capable of changing the content mix and sequencing without necessarily changing the underlying network of connections. [S7]
- The X field experiment randomly assigned users to algorithmic or chronological feeds for seven weeks and measured both political attitudes and online behavior; the abstract reports increased engagement and movement toward more conservative political opinions under the algorithmic feed, though the retrieved text is truncated before giving the full results. [S6]

#### Finding 2

**Claim**

The strongest direct evidence in the supplied material does not establish that recommendation algorithms change voting or other consequential political behavior.

**Confidence:** Medium

**Why this confidence level**

The experiments provide useful outcome boundaries, but the available extracts do not comprehensively assess all forms of political behavior.

**Evidence**

- The Facebook and Instagram experiment measured on-platform activity and political attitudes, but found no significant effects on polarization, knowledge, or related attitudes; it does not report a demonstrated effect on voting, turnout, protest, or political participation. [S7]
- The prior X evidence concerned affective polarization and policy/current-affairs attitudes, not demonstrated changes in voting, participation, or partisan identity. [S4] [S5]
- The new X source says it measured online behavior, but the retrieved passage does not specify whether behavior means engagement only or includes consequential political actions. [S6]

#### Finding 3

**Claim**

The Facebook and Instagram findings qualify claims that algorithms generally create filter bubbles or polarization: algorithmic ranking changed exposure in several directions, including both more political and untrustworthy content and, on Facebook, more moderate and ideologically mixed sources under chronological ordering, without changing polarization over the study period.

**Confidence:** High

**Why this confidence level**

The source reports a randomized platform intervention and directly compares exposure outcomes with political-attitude outcomes.

**Evidence**

- Compared with the default algorithmic feed, chronological feeds increased exposure to political and untrustworthy content on both platforms, decreased exposure to uncivil or slur-containing content on Facebook, and increased exposure to moderate friends and ideologically mixed sources on Facebook. [S7]
- Despite these substantial changes in users’ on-platform experience, no significant changes occurred in issue polarization or affective polarization during the three-month election-period study. [S7]

#### Finding 4

**Claim**

Differences across studies are plausibly explained by platform, intervention, duration, baseline feed, and outcome differences rather than by a single contradiction about whether algorithms matter.

**Confidence:** High

**Why this confidence level**

The sources directly document materially different experimental designs, platforms, exposure manipulations, time horizons, and dependent variables.

**Evidence**

- S7 switched Facebook and Instagram users from personalized ranking to reverse chronology for three months, whereas S5 reranked partisan content within existing X feeds for one week and S6 compared algorithmic and chronological X feeds for seven weeks. [S5] [S6] [S7]
- The studies examine different outcomes: content exposure and engagement, affective polarization, policy attitudes, partisanship, political knowledge, and online behavior. Effects reported for one outcome therefore do not imply effects for all others. [S4] [S5] [S6] [S7]
- S7 emphasizes that algorithmic feeds operate together with users’ networks, choices, reshares, and interactions; changing ranking alone may therefore have smaller effects than changing the broader social-media environment. [S7]
- The prior review describes a feedback loop in which users’ political preferences shape engagement and algorithms learn from that engagement, making selection and algorithmic influence difficult to disentangle. [S1] [S4]

#### Finding 5

**Claim**

A responsible overall conclusion is that algorithms contribute to polarization mainly by structuring and potentially amplifying political exposure, while the magnitude and persistence of their independent effect on beliefs and behavior remain uncertain.

**Confidence:** High

**Why this confidence level**

This synthesis accommodates both positive and null causal findings and is supported by direct experiments plus the broader mechanism evidence.

**Evidence**

- The supplied evidence consistently shows that ranking systems alter visibility, sequencing, engagement, and recommendation pathways. [S3] [S4] [S5] [S7]
- Some interventions report short-term shifts in affective polarization or policy attitudes, while the large Facebook and Instagram experiment found no significant changes in polarization or political knowledge. [S4] [S5] [S7]
- The review and mechanism-focused sources characterize algorithms as interacting with or reinforcing pre-existing preferences and social drivers rather than acting as an isolated cause. [S1] [S4]

### Conflicts Found

- S7 reports substantial exposure and engagement changes but no significant effects on issue or affective polarization, whereas S5 reports a short-term causal change in affective polarization and S4 reports movement in policy/current-affairs attitudes under an X algorithmic feed. [S4] [S5] [S7]
- S6 appears to report that switching to an algorithmic X feed increased engagement and shifted political opinion toward more conservative positions, while S7 found no significant attitude effects from removing algorithmic ranking on Facebook and Instagram. These are conditional differences across platforms, periods, interventions, and samples, not direct replications. [S6] [S7]
- S3 and S4 emphasize amplification of extremity or antagonistic content, while S7 shows that replacing algorithmic ranking can increase some forms of political or untrustworthy exposure and moderate or ideologically mixed exposure can also change. Exposure direction is therefore not uniformly toward greater extremity. [S3] [S4] [S7]

### Important Gaps

- What are the complete results and effect sizes in S6, including whether the X experiment changed polarization, partisanship, sharing, political participation, or other behavior?
- Do the short-term attitude effects reported in some X experiments persist beyond one to three months?
- How representative are the users who consent to platform experiments, and do results generalize across countries, elections, platforms, and algorithm versions?
- How large are algorithmic effects relative to self-selection, network composition, partisan identity, political elites, and other platform features?
- Does algorithmic ranking affect consequential political behavior such as voting, turnout, protest, persuasion, or cross-party engagement?
- The supplied extracts do not provide complete methodological details such as attrition, compliance, statistical uncertainty, subgroup effects, or preregistration for all experiments.

**Analysis Duration:** 17.34s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The evidence now answers the exposure-versus-belief distinction more clearly, especially through S7, but an important part of the original question—effects on political behavior—and the complete findings of the newer X experiment remain unresolved. A focused search for the full S6 results would materially improve the answer.

**Next Search**

> Gauthier Hodler Widmer Zhuravskaya 2026 Nature X feed algorithm political effects full results behavior polarization

---

# Iteration 3

## 1. Search

**Query**

> Gauthier Hodler Widmer Zhuravskaya 2026 Nature X feed algorithm political effects full results behavior polarization

**Why this query**

The evidence now answers the exposure-versus-belief distinction more clearly, especially through S7, but an important part of the original question—effects on political behavior—and the complete findings of the newer X experiment remain unresolved. A focused search for the full S6 results would materially improve the answer.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S9 — NEWS: Algorithm on X effects political views in the USA | unisg.ch**
  URL: https://www.unisg.ch/en/newsroom/algorithm-on-x-effects-political-views-in-the-usa
- **S10 — Social sciences: X’s algorithm may influence political attitudes (Nature) | Nature Portfolio**
  URL: https://www.natureasia.com/en/info/press-releases/detail/9242
- **S11 — The political effects of X's feed algorithm. - Abstract**
  URL: https://pubmed.ncbi.nlm.nih.gov/41708846

**Search Duration:** 2.72s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new primary evidence strengthens the conclusion that recommendation algorithms can change users’ political attitudes, but mainly in platform- and outcome-specific ways rather than by uniformly increasing polarization.

**Confidence:** High

**Why this confidence level**

S11 is a primary peer-reviewed field experiment with a large randomized sample and explicitly distinguishes policy-attitude effects from null effects on polarization and partisanship.

**Evidence**

- A 2023 randomized seven-week field experiment with 4,965 US X users found that switching from a chronological to an algorithmic feed shifted opinions toward more conservative positions, especially on policy priorities, perceptions of investigations into Donald Trump, and views on the war in Ukraine. [S11]
- The same experiment found no significant effect on affective polarization or self-reported partisanship. [S11]

#### Finding 2

**Claim**

The X algorithm changed political exposure in a directional way, promoting conservative content and demoting posts from traditional media; this exposure also altered users’ subsequent account-following behavior.

**Confidence:** High

**Why this confidence level**

The source reports both the randomized intervention and mechanism analyses based on observed feed content and user behavior.

**Evidence**

- The experiment’s feed-content analysis found that the algorithm promoted conservative content and demoted posts by traditional news outlets. [S11]
- Exposure to algorithmic content made users more likely to follow conservative political activist accounts, and those follows persisted after users returned to a chronological feed. [S11]

#### Finding 3

**Claim**

The X experiment provides evidence of persistence and asymmetry: turning on the algorithm affected attitudes and following behavior, whereas turning it off produced no comparable reversal.

**Confidence:** High

**Why this confidence level**

The randomized two-direction design directly supports an asymmetric treatment effect, although the persistence evidence concerns current attitudes and follows over the study’s observed period.

**Evidence**

- Users switched from chronological to algorithmic feeds changed political opinions and engagement, while users switched from algorithmic to chronological feeds showed little comparable change. [S11]
- Conservative activist accounts followed during algorithmic exposure remained followed after algorithmic curation was removed, offering a mechanism for persistent effects. [S11]

#### Finding 4

**Claim**

The new evidence resolves an important incompleteness in the earlier research state: the X experiment did not show a broad increase in polarization or partisanship, despite shifting some policy-related attitudes and online behavior.

**Confidence:** High

**Why this confidence level**

The new primary source supplies the previously missing full result and can be compared directly with the earlier experiments.

**Evidence**

- S11 reports significant effects on conservative policy priorities and selected political perceptions, but no significant effects on affective polarization or self-reported partisanship. [S11]
- This is consistent with earlier evidence that algorithmic exposure can affect affective attitudes in some interventions, while the Meta feed experiment found large exposure changes without significant changes in issue or affective polarization. [S5] [S7]

#### Finding 5

**Claim**

The literature reaches different conclusions because ‘political effects’ are not a single outcome: algorithms may change exposure, engagement, policy priorities, perceptions, or following behavior without changing affective polarization, ideological identity, or partisanship.

**Confidence:** High

**Why this confidence level**

The sources directly show divergent results across dependent variables, not merely disagreement in interpretation.

**Evidence**

- S11 reports effects on policy priorities, selected political perceptions, engagement, and conservative account-following, but not affective polarization or self-reported partisanship. [S11]
- S5 reports a short-term change in affective polarization under partisan-content reranking, while S7 reports substantial exposure changes but no significant changes in polarization or political knowledge. [S5] [S7]

#### Finding 6

**Claim**

A defensible overall assessment is that algorithms make a meaningful contribution to political polarization risk by structuring exposure and potentially reinforcing or intensifying existing political tendencies, but the supplied evidence does not justify attributing polarization broadly or primarily to algorithms.

**Confidence:** High

**Why this confidence level**

This synthesis accommodates the strongest positive and null experimental findings and does not overstate evidence for voting or large-scale behavioral effects.

**Evidence**

- Across studies, ranking systems alter content visibility, sequencing, engagement, recommendation pathways, and sometimes subsequent follows. [S3] [S4] [S5] [S7] [S11]
- Causal experiments produce mixed downstream results: some find attitude or affective-polarization effects, while others find no polarization effect; S11 specifically finds conservative attitude shifts without increased affective polarization or partisanship. [S5] [S7] [S11]
- The broader literature describes feedback between user preferences, social networks, and algorithmic ranking, making algorithms more plausibly an amplifier or structuring force than an independent creator of polarization. [S1] [S4] [S7]

### Conflicts Found

- S11 reports that activating X’s algorithm shifted policy-related attitudes toward more conservative positions, whereas S7 found no significant political-attitude or polarization effects when algorithmic ranking was removed on Facebook and Instagram. The disagreement is conditional on platform, algorithm, intervention direction, study period, and user environment rather than a direct replication conflict. [S7] [S11]
- S11 finds attitude and following effects without a significant change in affective polarization or partisanship; S5 reports a short-term causal change in affective polarization. These findings concern different X interventions and outcomes, so they indicate heterogeneous effects rather than a settled uniform direction. [S5] [S11]
- S3 and S4 emphasize amplification of extreme or antagonistic content, while S7 shows that changing ranking can alter exposure in multiple directions, including toward moderate or ideologically mixed sources. The evidence does not establish that algorithmic ranking always increases extremity. [S3] [S4] [S7]

### Important Gaps

- How large are these algorithmic effects relative to user self-selection, partisan identity, political elites, network composition, and other platform features?
- Do the attitude and account-following effects in S11 persist over longer periods, across election cycles, or outside the United States?
- Does algorithmic curation affect consequential political behavior such as voting, turnout, protest, donations, or political participation?
- Why did algorithmic exposure shift policy priorities and selected perceptions in S11 without significantly changing partisanship or affective polarization?
- How generalizable are results from X, Facebook, and Instagram to other platforms, countries, algorithm versions, and less politically engaged users?

**Analysis Duration:** 15.15s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new primary study fills the most important prior gap by providing the complete X results and confirms the central distinction: algorithms clearly alter exposure and can causally shift some political attitudes and online behavior, but effects on polarization are inconsistent and effects on consequential political behavior remain unestablished. Further research would improve precision but is not necessary to answer the original question responsibly.

**Next Search**

> To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions. additional evidence search 4

---

# Iteration 4

## 1. Search

**Query**

> To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions. additional evidence search 4

**Why this query**

The new primary study fills the most important prior gap by providing the complete X results and confirms the central distinction: algorithms clearly alter exposure and can causally shift some political attitudes and online behavior, but effects on polarization are inconsistent and effects on consequential political behavior remain unestablished. Further research would improve precision but is not necessary to answer the original question responsibly.

**Results**

5 results retrieved.

2 new unique sources added.

### Sources

- **S12 — How algorithmically curated online environments influence users’ political polarization: Results from two experiments with panel data**
  URL: https://www.sciencedirect.com/science/article/pii/S2451958823000763
- **S13 — Understanding Social Media Recommendation Algorithms**
  URL: https://knightcolumbia.org/content/understanding-social-media-recommendation-algorithms

**Search Duration:** 2.98s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

S12 provides experimental evidence that exposure to like-minded political arguments increases both attitude polarization and affective polarization, but algorithmic selection does not generally amplify those exposure effects.

**Confidence:** High

**Why this confidence level**

S12 is a peer-reviewed study reporting two experiments with panel data and directly separates the effect of ideological exposure from the effect of algorithmic selection.

**Evidence**

- Across two quasi-experiments with a three-wave panel design, participants exposed to arguments consistent with their attitudes became more polarized than participants exposed to opposing arguments; the effect was observed for both attitude and affective polarization. [S12]
- Comparing algorithmically selected arguments with randomly selected arguments, S12 found no general amplification of polarization by algorithmic selection. For one topic, algorithmic selection produced a small additional increase in attitude polarization. [S12]

#### Finding 2

**Claim**

The new evidence strengthens the conclusion that the content users encounter can affect political polarization, while the independent contribution of recommendation algorithms may be modest and outcome-specific.

**Confidence:** High

**Why this confidence level**

Multiple experimental studies converge on heterogeneous downstream effects and distinguish exposure content from ranking or curation effects.

**Evidence**

- S12 identifies a strong difference between like-minded and opposing exposure, but finds little evidence that algorithmic curation itself magnifies the difference; only one topic showed a slight additional attitude-polarization effect. [S12]
- This pattern complements S7, where replacing personalized ranking with chronological feeds substantially changed exposure but did not significantly change issue or affective polarization, and S11, where algorithmic X exposure shifted some policy attitudes without changing affective polarization or partisanship. [S7] [S11]

#### Finding 3

**Claim**

Algorithmic recommendation systems change what users see by controlling content propagation, feed composition, and sequencing, but their effects emerge through interaction with user behavior rather than through algorithms alone.

**Confidence:** High

**Why this confidence level**

S13 provides a clear mechanism account, while S12 supplies an experimental design directly isolating algorithmic selection from the political slant of exposure.

**Evidence**

- S13 distinguishes algorithms that process content from algorithms that propagate it, emphasizing that recommendation algorithms generate feeds and determine much of what users encounter. [S13]
- S13 characterizes social-media platforms as complex systems in which platform design, user behavior, and content-creator adaptation produce feedback loops; it argues that many observed effects cannot be attributed exclusively either to users or to algorithms. [S13]
- S12 operationalizes this distinction by comparing algorithmically selected arguments with randomly selected arguments while holding the broad ideological direction of exposure in view. [S12]

#### Finding 4

**Claim**

The literature's divergent conclusions are substantially explained by confusing or combining different causal treatments: ideological exposure, algorithmic selection, feed ranking, platform environment, and user interaction.

**Confidence:** High

**Why this confidence level**

The studies directly use different interventions, platforms, durations, exposure materials, and dependent variables, providing a strong explanation for heterogeneous results.

**Evidence**

- S12 finds strong polarization effects from like-minded exposure but little general amplification from algorithmic selection. [S12]
- S5 reranked partisan-animosity and antidemocratic content within existing X feeds and reported a short-term change in affective polarization, whereas S7 removed personalized ranking on Facebook and Instagram and found no significant polarization effect. [S5] [S7]
- S11 found shifts in selected policy attitudes and conservative-account following under algorithmic X exposure, but no significant change in affective polarization or partisanship. [S11]
- S13 argues that emergent human-algorithm feedback loops and limited platform access make it difficult to observe and explain the full causal process. [S13]

#### Finding 5

**Claim**

The strongest supported synthesis is that recommendation algorithms contribute to polarization risk primarily by structuring exposure and potentially reinforcing users' existing preferences, not by uniformly causing polarization or independently creating partisan hostility.

**Confidence:** High

**Why this confidence level**

The conclusion accommodates positive exposure and attitude findings as well as null polarization findings and is supported by both experimental and mechanism-focused evidence.

**Evidence**

- S12 shows that like-minded exposure can polarize users, but algorithmic selection usually did not intensify that effect. [S12]
- S7 found major exposure changes without significant changes in issue or affective polarization, while S11 found policy-attitude and following effects without increased affective polarization or partisanship. [S7] [S11]
- S13 describes recommendation effects as emergent outcomes of interaction between platform design and human behavior rather than as effects attributable to algorithms in isolation. [S13]

#### Finding 6

**Claim**

The supplied evidence remains insufficient to establish that recommendation algorithms change consequential political behavior such as voting, turnout, protest, or participation.

**Confidence:** Medium

**Why this confidence level**

The studies establish boundaries around measured outcomes, but the available sources do not comprehensively test consequential political behavior.

**Evidence**

- S12 measures attitude and affective polarization rather than consequential political actions. [S12]
- S7 and S11 report platform activity, following behavior, and political attitudes, but do not demonstrate effects on voting, turnout, protest, or comparable offline political behavior. [S7] [S11]

### Conflicts Found

- S12 reports that like-minded exposure increases polarization, but finds that algorithmic selection generally does not amplify that effect. This qualifies stronger claims in S3, S4, and S5 that algorithmic curation or recommendation tends to intensify extremity or affective polarization. [S3] [S4] [S5] [S12]
- S12's small topic-specific attitude effect from algorithmic selection contrasts with S7's null effects on issue and affective polarization after removing algorithmic ranking, and with S11's null effects on affective polarization and partisanship. The studies differ in platform, exposure material, intervention, and outcomes, so the disagreement is conditional rather than a direct replication conflict. [S7] [S11] [S12]
- S13 emphasizes that human behavior and algorithmic design jointly produce emergent effects, while some accounts frame recommendation algorithms as independent amplifiers. These views can be reconciled if algorithms are treated as mechanisms that reinforce or redirect user-driven dynamics rather than as sole causes. [S3] [S4] [S13]

### Important Gaps

- How large are algorithmic effects relative to users' prior preferences, social networks, partisan identity, political elites, and other platform features?
- Why does like-minded exposure reliably affect polarization in S12, while algorithmic selection adds little additional effect?
- Do the short-term attitude, affective-polarization, and following effects persist over months or years?
- Do recommendation algorithms affect consequential political behavior such as voting, turnout, protest, donations, or political participation?
- How generalizable are findings from the German S12 experiments and the US X, Facebook, and Instagram experiments across platforms, countries, elections, and algorithm versions?
- The supplied S12 and S13 material does not provide full effect sizes, attrition, compliance, subgroup analyses, or statistical uncertainty for all reported comparisons.

**Analysis Duration:** 16.85s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new S12 evidence materially improves the answer by directly separating ideological exposure from algorithmic selection, and S13 clarifies the human-algorithm feedback mechanism. Together with S7 and S11, the important question can be answered responsibly: algorithms clearly change exposure, but downstream polarization effects are heterogeneous, generally modest or absent in several experiments, and not established for consequential political behavior. Further research would be useful but is not necessary to answer the original question at this stage.

**Next Search**

> To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions. additional evidence search 5

---

# Iteration 5

## 1. Search

**Query**

> To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions. additional evidence search 5

**Why this query**

The new S12 evidence materially improves the answer by directly separating ideological exposure from algorithmic selection, and S13 clarifies the human-algorithm feedback mechanism. Together with S7 and S11, the important question can be answered responsibly: algorithms clearly change exposure, but downstream polarization effects are heterogeneous, generally modest or absent in several experiments, and not established for consequential political behavior. Further research would be useful but is not necessary to answer the original question at this stage.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S14 — The Impact of Social Media Algorithms on Political Polarization » boslabour.org.uk**
  URL: https://boslabour.org.uk/the-impact-of-social-media-algorithms-on-political-polarization
- **S15 — The Political and Psychological Costs of Social Media Algorithms: Evidence-Based Strategies to Mitigate Algorithm-Driven Addiction, Echo Chambers, Polarization, and Misinformation - Gilmore Health News**
  URL: https://www.gilmorehealth.com/the-political-and-psychological-costs-of-social-media-algorithms-evidence-based-strategies-to-mitigate-algorithm-driven-addiction-echo-chambers-polarization-and-misinformation
- **S16 — The Impact Of Social Media Algorithms On Information Bubbles And Political Polarization. - Consensus Academic Search Engine**
  URL: https://consensus.app/questions/impact-social-media-algorithms-information-bubbles
- **S17 — Deep dive into Meta’s algorithms shows that America’s political polarization has no easy fix | The Seattle Times**
  URL: https://www.seattletimes.com/business/deep-dive-into-metas-algorithms-shows-that-americas-political-polarization-has-no-easy-fix
- **S18 — Social Algorithms and Political Polarization: A Teenager’s Perspective on Social Media and American Divisiveness [Opinion] - VOX ATL**
  URL: https://voxatl.org/social-algorithms-political-polarization-teen-perspective

**Search Duration:** 4.84s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new sources provide little strong new evidence beyond the existing experimental literature: they mostly restate the filter-bubble hypothesis, while S17 offers secondary reporting that broadly corroborates the null polarization findings from the Meta experiments.

**Confidence:** High

**Why this confidence level**

S17 is consistent with the stronger primary evidence already in the research state; the other sources add mechanisms and claims but not comparably reliable new causal results.

**Evidence**

- S17 reports that replacing Facebook’s algorithmic feed with chronological ordering, reducing resharing, and reducing ideologically aligned content changed users’ exposure and platform behavior but produced little measurable change in polarization or political attitudes during the 2020 election study. [S17]
- S17 also reports that the researchers observed substantial ideological segregation and divergent information environments, showing that exposure structure and downstream attitude change are distinct outcomes. [S17]
- S14, S15, and S16 describe algorithms as creating echo chambers and intensifying polarization, but primarily present summaries, commentary, or aggregated claims rather than new causal evidence. [S14] [S15] [S16]

#### Finding 2

**Claim**

The new evidence reinforces that algorithms substantially change what users see and how they use platforms, but does not show that they uniformly increase political polarization.

**Confidence:** High

**Why this confidence level**

Exposure and platform-use effects are supported by the reported Meta experiments and align with the prior evidence; the broader claims about polarization from S14 and S16 are less methodologically informative.

**Evidence**

- S17 states that algorithmic systems determine content visibility based on past clicks, groups, friends, topics, and headlines, and reports significant ideological segregation in political-news exposure. [S17]
- The same report says that removing algorithmic ranking reduced time spent on Facebook and Instagram, while other interventions changed exposure to political, untrustworthy, or ideologically aligned content without significantly changing political attitudes. [S17]
- S14 and S16 assert that personalization narrows exposure and can create echo chambers, but their claims are not sufficient to establish the size or consistency of downstream effects. [S14] [S16]

#### Finding 3

**Claim**

S17 gives a useful explanation for why the literature reaches different conclusions: users’ own preferences and networks may drive much of the observed ideological segregation, while algorithms make it easier to follow those preferences rather than independently creating them.

**Confidence:** High

**Why this confidence level**

The source directly identifies duration, cumulative exposure, cross-media effects, and user self-selection as limitations, matching the design-based explanation already supported by the primary studies.

**Evidence**

- S17 quotes researchers arguing that users seek content aligned with their views and that algorithms primarily make this behavior easier, implying a feedback relationship between self-selection and ranking. [S17]
- S17 notes that the studies covered only a few months during the 2020 election and did not measure the cumulative effects of years of social-media misinformation or users’ exposure to television, radio, other websites, and interpersonal communication. [S17]
- This complements the prior evidence that algorithmic selection, ideological exposure, feed ranking, and user interaction are different causal treatments. [S7] [S11] [S12] [S13]

#### Finding 4

**Claim**

The new sources do not materially improve the evidence concerning consequential political behavior such as voting, turnout, protest, or participation.

**Confidence:** Medium

**Why this confidence level**

The sources establish an evidence gap rather than resolving it; the available extracts do not comprehensively test offline or consequential political behavior.

**Evidence**

- S17 discusses platform time, exposure, misinformation, and political attitudes, but does not report demonstrated effects on voting, turnout, protest, or other consequential political actions. [S17]
- S14, S15, and S16 make broad claims about public opinion, democracy, and behavior without presenting a clearly identified causal experiment measuring consequential political behavior. [S14] [S15] [S16]

### Conflicts Found

- S14 and S16 present algorithmic personalization and echo chambers as significant causes of polarization, whereas S17 reports that major changes to Meta’s ranking and sharing systems did not measurably alter polarization or key political attitudes. The disagreement is largely one of evidentiary strength: S14 and S16 summarize a causal narrative, while S17 reports experimental null results. [S14] [S16] [S17]
- S16 claims that experiments show even small changes in algorithmic filtering can significantly increase polarization, but the supplied source does not identify the experiments or provide effect sizes. This is difficult to reconcile with S7 and S17, which report substantial exposure changes without significant polarization effects. [S7] [S16] [S17]
- S15 argues broadly that engagement-optimized algorithms deepen echo chambers and polarization, but its supplied discussion combines political claims with commentary about addiction, profit incentives, and misinformation rather than isolating the causal effect of recommendation ranking. Its conclusions therefore exceed what can be compared directly with the platform experiments. [S15] [S7] [S11] [S12]

### Important Gaps

- What are the long-term cumulative effects of algorithmic exposure over years rather than weeks or a few months?
- How large are algorithmic effects relative to user self-selection, partisan identity, network composition, political elites, and other media?
- Do recommendation algorithms affect voting, turnout, protest, donations, or other consequential political behavior?
- How generalizable are the experimental findings across platforms, countries, elections, algorithm versions, and less politically engaged users?
- Why do some X interventions produce policy-attitude or affective-polarization effects while Meta and other interventions produce null polarization results?
- The new secondary sources do not provide complete methods, effect sizes, attrition, compliance, or uncertainty estimates that would resolve these questions.

**Analysis Duration:** 15.08s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The important parts of the question can now be answered responsibly. The accumulated evidence clearly supports a distinction between substantial exposure effects and heterogeneous, generally modest or outcome-specific downstream political effects. The new sources are mostly low-value summaries or commentary and do not justify another search; the remaining gaps concern broad generalizability and long-term or consequential behavior, not an unresolved core conclusion.

**Next Search**

> To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions. additional evidence search 6

---

# Iteration 6

## 1. Search

**Query**

> To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions. additional evidence search 6

**Why this query**

The important parts of the question can now be answered responsibly. The accumulated evidence clearly supports a distinction between substantial exposure effects and heterogeneous, generally modest or outcome-specific downstream political effects. The new sources are mostly low-value summaries or commentary and do not justify another search; the remaining gaps concern broad generalizability and long-term or consequential behavior, not an unresolved core conclusion.

**Results**

5 results retrieved.

2 new unique sources added.

### Sources

- **S19 — #1 Social Media, Algorithms and Politics: Lessons from Research and Challenges for Policy - with ...**
  URL: https://www.youtube.com/watch?v=xazNwH_g8cA
- **S20 — Algorithms Shift Polarization. Why Does Policy Still Miss the Real Problem? | TechPolicy.Press**
  URL: https://www.techpolicy.press/algorithms-shift-polarization-why-does-policy-still-miss-the-real-problem

**Search Duration:** 2.63s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

S20 independently corroborates the earlier finding that reranking content within users’ existing X feeds can causally affect affective polarization, while leaving the content and users unchanged.

**Confidence:** Medium

**Why this confidence level**

The result is consistent with S5 and S20 gives specific sample and effect-size details, but S20 is a commentary rather than the primary study, so it should not be treated as independent primary confirmation.

**Evidence**

- S20 reports a browser-extension experiment with 1,256 US participants during the 2024 campaign. Increasing exposure to content expressing antidemocratic attitudes and partisan animosity reportedly cooled feelings toward the opposing party by 2.48 points on a 100-point scale; reducing exposure warmed them by 2.11 points. [S20]
- The intervention changed the ranking of existing feed content rather than removing content, isolating feed prominence as the treatment. [S20]

#### Finding 2

**Claim**

The reported X reranking effect is modest for an individual but relevant as evidence that algorithmic exposure can produce measurable short-term changes in political affect.

**Confidence:** Medium

**Why this confidence level**

The immediate individual-level effect is reported consistently, but the claim about cumulative population-scale consequences is extrapolative and not directly demonstrated by the supplied evidence.

**Evidence**

- S20 characterizes the approximately two-point changes as small for an individual while arguing that repeated exposure across large populations could accumulate into broader hostility differences. [S20]
- S5 likewise reports a short-term affective-polarization effect from increasing or decreasing exposure to partisan-animosity and antidemocratic content. [S5]

#### Finding 3

**Claim**

S19 reinforces the view that the central research problem concerns algorithmic curation, segregation, polarization, and the difficulty of measuring causal effects, but it adds little concrete causal evidence.

**Confidence:** Low

**Why this confidence level**

S19 is a general interview description of a research agenda and does not report a clearly identified experiment, effect size, or behavioral outcome relevant to the question.

**Evidence**

- The interview describes research focused on how algorithms curate and select what users see, and on measuring consequences for segregation, polarization, and political opinion. [S19]
- It emphasizes the use of large-scale social-media data, explainability methods, and opinion-dynamics models to connect algorithmic mechanisms with political outcomes. [S19]

#### Finding 4

**Claim**

The new sources do not change the overall conclusion: recommendation algorithms clearly affect exposure and can sometimes shift political attitudes or affect, but the evidence does not show a uniform or broad effect on polarization, partisanship, or consequential political behavior.

**Confidence:** High

**Why this confidence level**

The new material is consistent with the accumulated experimental pattern of heterogeneous, outcome-specific effects and does not resolve the behavioral evidence gap.

**Evidence**

- S20 supports a short-term affective-polarization effect from targeted reranking, consistent with S5. [S20] [S5]
- Other experiments in the research state found substantial exposure changes without significant polarization effects (S7), or policy-attitude and following effects without significant changes in affective polarization or partisanship (S11). [S7] [S11]
- Neither S19 nor S20 supplies evidence of changes in voting, turnout, protest, donations, or comparable consequential political behavior. [S19] [S20]

### Conflicts Found

- S20 presents the 2024 X reranking study as strong evidence that algorithmic ranking directly changes polarization, whereas S7 and S11 found no significant changes in affective polarization under different interventions. This remains a conditional disagreement because the studies differ in platform treatment, content targeted, duration, timing, and outcome measurement; S20 is also secondary reporting. [S20] [S7] [S11]
- S20 argues that algorithmic amplification of emotionally intense content is a major causal driver, while S12 found that like-minded exposure increased polarization but algorithmic selection generally added little amplification. The findings can coexist if algorithmic effects depend on the particular content category and ranking manipulation. [S20] [S12]

### Important Gaps

- Do the approximately two-point affective-polarization effects reported for the X reranking intervention persist beyond one week or translate into behavior outside the platform?
- How representative are participants in the X experiments, and do effects generalize across platforms, countries, election periods, and algorithm versions?
- What is the relative contribution of algorithmic ranking compared with user self-selection, network composition, political elites, and content supply?
- Does recommendation curation affect consequential political behavior such as voting, turnout, protest, donations, or political participation?

**Analysis Duration:** 11.63s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The accumulated evidence now responsibly answers the central question: algorithms substantially alter political exposure, with some causal effects on narrow attitude or affective outcomes, but no consistent evidence that they broadly increase polarization or consequential political behavior. S20 mainly corroborates S5, and S19 is too general to resolve the remaining gaps. Further searching could add detail but is unlikely to materially improve the core answer without specifically targeted evidence on long-term or consequential behavior.

**Next Search**

> To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions. additional evidence search 7

---

# Iteration 7

## 1. Search

**Query**

> To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions. additional evidence search 7

**Why this query**

The accumulated evidence now responsibly answers the central question: algorithms substantially alter political exposure, with some causal effects on narrow attitude or affective outcomes, but no consistent evidence that they broadly increase polarization or consequential political behavior. S20 mainly corroborates S5, and S19 is too general to resolve the remaining gaps. Further searching could add detail but is unlikely to materially improve the core answer without specifically targeted evidence on long-term or consequential behavior.

**Results**

5 results retrieved.

0 new unique sources added.

### Sources

No new unique sources were added.

**Search Duration:** 5.15s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The accumulated evidence supports a clear distinction between effects on exposure and effects on political beliefs or behavior: recommendation algorithms substantially alter what users encounter, but their downstream effects are heterogeneous and do not establish that algorithms broadly or uniformly cause polarization.

**Confidence:** High

**Why this confidence level**

Multiple experimental and mechanism-focused sources consistently establish exposure effects while showing heterogeneous downstream outcomes.

**Evidence**

- Across the studies, ranking systems changed content visibility, sequencing, exposure composition, engagement, recommendation pathways, and—in one X experiment—subsequent account-following behavior. [S3] [S4] [S5] [S7] [S11]
- Causal studies produced mixed downstream results: some found shifts in affective polarization or selected policy attitudes, while others found no significant change in issue polarization, affective polarization, knowledge, or partisanship. [S5] [S7] [S11] [S12]

#### Finding 2

**Claim**

There is strong evidence that algorithmic ranking changes what users see, even without deleting content.

**Confidence:** High

**Why this confidence level**

The evidence includes randomized feed interventions and direct analyses of resulting feed content and behavior.

**Evidence**

- Algorithms use engagement and behavioral signals to rank and recommend content, changing its prominence and order relative to chronological feeds. [S4] [S7]
- Experiments on X and Meta changed feed ranking or replaced personalized ranking with chronological ordering, producing substantial changes in political, ideological, uncivil, untrustworthy, and mixed-content exposure. [S5] [S7] [S11]
- On X, algorithmic exposure promoted conservative content, demoted traditional-media posts, increased engagement, and increased following of conservative activist accounts. [S11]

#### Finding 3

**Claim**

Exposure to congenial or emotionally antagonistic political content can change political attitudes, but the independent contribution of algorithmic selection is generally modest, conditional, or outcome-specific.

**Confidence:** High

**Why this confidence level**

Several experiments directly manipulate exposure or ranking, and their results converge on measurable but narrow and non-uniform effects.

**Evidence**

- Like-minded exposure increased both attitude polarization and affective polarization, but algorithmic selection generally did not amplify that exposure effect; only one topic showed a small additional attitude-polarization effect. [S12]
- Reranking partisan-animosity and antidemocratic content on X reportedly changed feelings toward the opposing party by roughly two points on a 100-point scale after one week. [S5] [S20]
- Switching to X's algorithmic feed shifted selected policy priorities and political perceptions toward more conservative positions and altered following behavior, but did not significantly change affective polarization or self-reported partisanship. [S11]

#### Finding 4

**Claim**

The strongest evidence does not establish effects on consequential political behavior such as voting, turnout, protest, donations, or offline participation.

**Confidence:** Medium

**Why this confidence level**

The evidence establishes what outcomes were and were not measured in the supplied material, but it does not constitute a comprehensive review of all behavioral research.

**Evidence**

- The available experiments measured attitudes, affect, knowledge, platform engagement, and account-following behavior, but did not demonstrate changes in voting, turnout, protest, or comparable consequential political action. [S7] [S11] [S12] [S17] [S20]

#### Finding 5

**Claim**

Algorithms are better characterized as structuring and sometimes amplifying existing political tendencies than as independently creating polarization from nothing.

**Confidence:** High

**Why this confidence level**

This synthesis accommodates both the evidence of algorithm-mediated influence and the evidence that user-driven selection and broader platform dynamics are important causes.

**Evidence**

- Users' preferences, networks, interactions, and content choices feed the ranking systems, producing a feedback loop that makes algorithmic influence difficult to separate from self-selection and social identity. [S1] [S4] [S7] [S13] [S17]
- The finding that like-minded exposure polarizes users while algorithmic selection usually adds little amplification suggests that content alignment and user selection may matter more than ranking alone in some settings. [S12]
- Other findings—such as conservative attitude shifts and persistent follows under X's algorithm—show that algorithms can nevertheless redirect or reinforce political trajectories in particular environments. [S11]

#### Finding 6

**Claim**

The literature reaches different conclusions because studies test different causal treatments, platforms, time periods, users, and outcomes rather than one common intervention.

**Confidence:** High

**Why this confidence level**

The accumulated sources explicitly document these design differences and show that apparently conflicting results often concern different estimands.

**Evidence**

- Studies differ between changing ideological exposure, reranking existing content, replacing personalized feeds with chronological feeds, and comparing algorithmically selected material with randomly selected material. [S5] [S7] [S11] [S12]
- They measure different endpoints, including exposure, engagement, policy attitudes, selected political perceptions, affective polarization, issue polarization, partisanship, knowledge, and following behavior. [S5] [S7] [S11] [S12]
- The studies also differ in platform, duration, election context, country, and whether they alter ranking alone or the broader social-media environment. [S5] [S6] [S7] [S11] [S12] [S17]
- Short interventions may detect immediate exposure or attitude changes but not cumulative effects, while longer-term effects are difficult to identify because users' other media and social environments remain active. [S7] [S17]

### Conflicts Found

- S5 and S20 report a short-term affective-polarization effect from targeted X reranking, while S7 found large exposure changes without significant polarization effects and S11 found policy-attitude and following effects without significant affective-polarization or partisanship effects. [S5] [S7] [S11] [S20]
- S3 and S4 emphasize amplification of extremity or antagonism, whereas S7 shows that changing ranking can alter exposure in multiple directions, including toward moderate or ideologically mixed sources; S12 finds little general amplification from algorithmic selection. [S3] [S4] [S7] [S12]
- S14-S16 present broad claims that personalization or engagement optimization causes polarization, but the supplied evidence is less methodologically specific than the randomized experiments reporting null or outcome-specific results. [S14] [S15] [S16] [S7] [S11] [S12]

### Important Gaps

- How large are algorithmic effects relative to user self-selection, partisan identity, network composition, political elites, and other media?
- Do the short-term attitude, affective-polarization, and following effects persist over months or years?
- Do recommendation algorithms affect consequential political behavior such as voting, turnout, protest, donations, or participation?
- How representative and generalizable are the findings across platforms, countries, elections, algorithm versions, and less politically engaged users?
- Why do particular X interventions produce effects that are absent in Meta experiments or in studies separating ideological exposure from algorithmic selection?
- The supplied material does not provide complete methods, attrition, compliance, subgroup analyses, or statistical uncertainty for every reported study.

**Analysis Duration:** 15.35s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

No usable new sources were retrieved, and the accumulated evidence is sufficient to answer the original question responsibly. It supports strong conclusions about exposure effects, qualified conclusions about beliefs and platform behavior, and an explicit evidence gap concerning consequential political behavior. Another search could add detail but is not necessary to resolve the main question.

**Next Search**

> To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions. additional evidence search 8

---

# Iteration 8

## 1. Search

**Query**

> To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions. additional evidence search 8

**Why this query**

No usable new sources were retrieved, and the accumulated evidence is sufficient to answer the original question responsibly. It supports strong conclusions about exposure effects, qualified conclusions about beliefs and platform behavior, and an explicit evidence gap concerning consequential political behavior. Another search could add detail but is not necessary to resolve the main question.

**Results**

5 results retrieved.

0 new unique sources added.

### Sources

No new unique sources were added.

**Search Duration:** 6.54s

---

## 2. Evidence Analysis

### What We Learned

No evidence-backed findings were established.

### Conflicts Found

No meaningful conflicts were identified in this iteration.

### Important Gaps

- The evidence gap concerning consequential political behavior remains unresolved: the supplied studies do not establish effects on voting, turnout, protest, donations, or offline participation.
- The long-term persistence and cumulative effects of short-term changes in exposure, affect, policy attitudes, or account-following remain unknown.
- The relative contribution of algorithmic ranking compared with user self-selection, partisan identity, networks, political elites, and other media remains unquantified.
- Generalizability across platforms, countries, elections, algorithm versions, and less politically engaged users remains uncertain.
- Complete methodological details and uncertainty estimates are not available for every reported study.

**Analysis Duration:** 3.71s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

No usable new sources were retrieved, and the accumulated evidence already supports a responsible answer: recommendation algorithms clearly alter exposure and sometimes produce narrow, short-term changes in affect or selected political attitudes, but they do not consistently increase polarization and have not been shown in the supplied evidence to change consequential political behavior. Further searching could fill gaps, especially on long-term and offline behavior, but it is not necessary to answer the original question responsibly.

**Next Search**

> To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions. additional evidence search 9

---

# Iteration 9

## 1. Search

**Query**

> To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions. additional evidence search 9

**Why this query**

No usable new sources were retrieved, and the accumulated evidence already supports a responsible answer: recommendation algorithms clearly alter exposure and sometimes produce narrow, short-term changes in affect or selected political attitudes, but they do not consistently increase polarization and have not been shown in the supplied evidence to change consequential political behavior. Further searching could fill gaps, especially on long-term and offline behavior, but it is not necessary to answer the original question responsibly.

**Results**

5 results retrieved.

0 new unique sources added.

### Sources

No new unique sources were added.

**Search Duration:** 4.86s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Recommendation algorithms clearly change users’ political-information exposure, even when they do not remove content.

**Confidence:** High

**Why this confidence level**

Multiple randomized feed interventions directly measured changes in what users encountered and, on X, subsequent account-following behavior.

**Evidence**

- Ranking systems use behavioral and predicted-relevance signals to determine content visibility and sequence, distinguishing personalized feeds from chronological feeds. [S4] [S7]
- Randomized interventions on Meta and X substantially changed exposure to political, ideological, uncivil, untrustworthy, moderate, mixed, and traditional-media content; the X intervention also increased exposure to conservative content and subsequent following of conservative activist accounts. [S7] [S11]

#### Finding 2

**Claim**

Algorithms can affect political beliefs and affect, but effects are heterogeneous, generally narrow, and not equivalent to a broad increase in polarization.

**Confidence:** High

**Why this confidence level**

Several experimental studies directly manipulate feeds or exposure, but their results differ by platform, content, intervention, duration, and outcome.

**Evidence**

- The X field experiment shifted selected policy priorities and political perceptions toward more conservative positions and altered following behavior, but did not significantly change affective polarization or self-reported partisanship. [S11]
- Targeted reranking of partisan-animosity and antidemocratic content reportedly changed feelings toward the opposing party by roughly two points on a 100-point scale after one week. [S5] [S20]
- The Meta experiment produced major exposure changes but no significant changes in issue polarization, affective polarization, political knowledge, or related attitudes over three months. [S7]
- Like-minded exposure increased attitude and affective polarization, but algorithmic selection generally did not amplify that effect, aside from a small topic-specific attitude effect. [S12]

#### Finding 3

**Claim**

The evidence does not establish that recommendation algorithms change consequential political behavior such as voting, turnout, protest, donations, or offline participation.

**Confidence:** Medium

**Why this confidence level**

The available studies define a clear boundary around measured outcomes, but they are not a comprehensive review of all behavioral research.

**Evidence**

- The supplied studies measured attitudes, affect, knowledge, platform engagement, and account-following, but did not demonstrate effects on voting, turnout, protest, donations, or comparable political action. [S7] [S11] [S12] [S17] [S20]

#### Finding 4

**Claim**

The best-supported interpretation is that algorithms are structuring and sometimes amplifying political tendencies, rather than independently creating polarization from nothing.

**Confidence:** High

**Why this confidence level**

The evidence supports both algorithm-mediated influence and the importance of prior preferences, social networks, and broader platform dynamics.

**Evidence**

- Users’ preferences, networks, interactions, and content choices supply signals to ranking systems, creating feedback between self-selection and algorithmic curation. [S1] [S4] [S7] [S13] [S17]
- Like-minded exposure can polarize users even when algorithmic selection adds little additional effect, while the X findings show that algorithmic exposure can nevertheless redirect selected attitudes and following behavior. [S11] [S12]

#### Finding 5

**Claim**

The literature reaches different conclusions because studies estimate different causal effects rather than testing one common phenomenon called ‘algorithmic polarization.’

**Confidence:** High

**Why this confidence level**

The sources directly document differences in interventions, platforms, time horizons, samples, and dependent variables, explaining much of the apparent disagreement.

**Evidence**

- Studies manipulate different treatments: ideological exposure, reranking existing posts, replacing personalized feeds with chronological feeds, or comparing algorithmically selected with randomly selected material. [S5] [S7] [S11] [S12]
- They measure different endpoints, including exposure, engagement, policy attitudes, political perceptions, affective polarization, issue polarization, partisanship, knowledge, and following behavior. [S5] [S7] [S11] [S12]
- Results also vary by platform, election context, country, duration, participant population, and whether ranking alone or the broader social-media environment is changed. [S5] [S7] [S11] [S12] [S17]
- Short experiments may detect immediate exposure or attitude changes but not cumulative effects, while user self-selection and other media make long-term causal attribution difficult. [S7] [S13] [S17]

### Conflicts Found

- S5 and S20 report a short-term affective-polarization effect from targeted X reranking, while S7 finds substantial exposure changes without significant polarization effects and S11 finds policy-attitude and following effects without significant changes in affective polarization or partisanship. [S5] [S7] [S11] [S20]
- S3 and S4 emphasize amplification of extremity or antagonism, whereas S7 shows that ranking changes can increase exposure in multiple directions, including toward moderate or ideologically mixed sources; S12 finds little general amplification from algorithmic selection. [S3] [S4] [S7] [S12]
- S11 reports conservative shifts in selected attitudes under X’s algorithmic feed, whereas S7 reports null polarization and attitude effects after removing personalized ranking on Meta. This is a conditional disagreement across platforms, algorithms, interventions, and periods, not a direct replication conflict. [S7] [S11]
- S14-S16 make broad causal claims about personalization, echo chambers, and polarization, but their supplied evidence is less methodologically specific than the randomized studies reporting null or outcome-specific effects. [S14] [S15] [S16] [S7] [S11] [S12]

### Important Gaps

- Do short-term changes in affect, policy attitudes, or account-following persist over months or years?
- Do recommendation algorithms affect consequential political behavior such as voting, turnout, protest, donations, or participation?
- How large are algorithmic effects relative to user self-selection, partisan identity, networks, political elites, and other media?
- How generalizable are the findings across platforms, countries, elections, algorithm versions, and less politically engaged users?
- Why do particular X interventions produce effects that are absent in Meta experiments or in studies separating ideological exposure from algorithmic selection?
- Complete methodological details, attrition, compliance, subgroup effects, and uncertainty estimates are not available for every reported study.

**Analysis Duration:** 14.33s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

No usable new sources were retrieved, and the accumulated evidence is sufficient to answer the central question responsibly: exposure effects are strong and well established, downstream effects are causal but heterogeneous, and evidence for broad polarization or consequential political behavior remains insufficient. Further searching could refine effect sizes or long-term behavior evidence, but is not necessary for the core conclusion.

**Next Search**

> To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions. additional evidence search 10

---

# Iteration 10

## 1. Search

**Query**

> To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions. additional evidence search 10

**Why this query**

No usable new sources were retrieved, and the accumulated evidence is sufficient to answer the central question responsibly: exposure effects are strong and well established, downstream effects are causal but heterogeneous, and evidence for broad polarization or consequential political behavior remains insufficient. Further searching could refine effect sizes or long-term behavior evidence, but is not necessary for the core conclusion.

**Results**

5 results retrieved.

1 new unique source added.

### Sources

- **S21 — Social Media, Echo Chambers, and Political Polarization (Chapter 3) - Social Media and Democracy**
  URL: https://www.cambridge.org/core/books/social-media-and-democracy/social-media-echo-chambers-and-political-polarization/333A5B4DE1B67EFF7876261118CCFE19

**Search Duration:** 2.64s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

S21 adds an important qualification to the filter-bubble account: empirical research has found that social-media users may encounter more diverse political news and cross-cutting interactions than the conventional echo-chamber narrative implies.

**Confidence:** Medium

**Why this confidence level**

S21 is a scholarly literature review, but the retrieved passage provides a summary rather than the underlying studies’ full methods or results.

**Evidence**

- The chapter states that cross-cutting interactions are more frequent than commonly believed and that exposure to diverse news can be higher through social media than through some other media forms. [S21]
- It suggests that weak ties—including coworkers, relatives, and acquaintances—can transmit novel and ideologically diverse information. [S21]

#### Finding 2

**Claim**

The available evidence does not support the claim that ranking algorithms uniformly create ideologically segregated news consumption, at least in the Facebook and Google studies cited by S21.

**Confidence:** Medium

**Why this confidence level**

The sources support a qualification of strong filter-bubble claims, but S21 reports findings from cited studies rather than presenting new primary evidence.

**Evidence**

- S21 reports that ranking algorithms did not have a large impact on the ideological balance of news consumption on Facebook or Google. [S21]
- This is consistent with the Meta experiment in which replacing personalized ranking with chronological feeds substantially changed exposure but did not significantly change issue or affective polarization. [S7]

#### Finding 3

**Claim**

S21 reinforces the distinction between exposure diversity and downstream political effects: encountering cross-cutting or diverse information does not by itself establish that social media reduces or increases polarization.

**Confidence:** High

**Why this confidence level**

The distinction is explicit in S21 and is strongly supported by the accumulated experimental evidence.

**Evidence**

- The chapter explicitly notes that increased exposure to diverse political ideas does not necessarily mean social media has no effect on political polarization. [S21]
- The broader evidence shows that like-minded exposure can increase attitude and affective polarization, while algorithmic selection generally adds little amplification and some feed interventions produce null polarization effects. [S12] [S7]

#### Finding 4

**Claim**

The new source strengthens the interpretation that algorithms operate within user-driven and network-driven processes rather than acting as isolated causes of polarization.

**Confidence:** High

**Why this confidence level**

The mechanism is supported by both the new review and multiple accumulated sources.

**Evidence**

- S21 attributes some exposure to diverse information to weak ties and emphasizes that social-media interaction patterns complicate the simple echo-chamber account. [S21]
- Other studies likewise describe feedback between users’ preferences, networks, interactions, and algorithmic ranking. [S1] [S7] [S13] [S17]

#### Finding 5

**Claim**

S21 does not materially change the overall conclusion: recommendation algorithms clearly structure exposure, but their contribution to political polarization is conditional, heterogeneous, and not established as the primary cause of broad polarization.

**Confidence:** High

**Why this confidence level**

The new review is consistent with the strongest accumulated experimental evidence and mainly adds a useful counterweight to stronger echo-chamber claims.

**Evidence**

- S21 presents the literature as nuanced and reports limited effects of ranking algorithms on ideological news balance, while also cautioning that exposure patterns alone do not settle the polarization question. [S21]
- Randomized studies find substantial exposure changes but mixed downstream effects: selected attitude or affective-polarization changes in some X interventions, null polarization effects in the Meta experiment, and little general amplification from algorithmic selection in S12. [S5] [S7] [S11] [S12]

### Conflicts Found

- S21 reports that ranking algorithms did not have a large effect on the ideological balance of news consumption on Facebook or Google, whereas S3 and S4 emphasize recommender pathways toward extreme or antagonistic content. The findings may concern different platforms, content types, measures, and periods; they do not establish that algorithms always have the same exposure effect. [S21] [S3] [S4]
- S21 highlights cross-cutting exposure and weak-tie diversity, while the conventional filter-bubble account summarized in S21 and echoed by S14-S16 treats personalization as a major driver of ideological isolation. The new source presents the latter as an overgeneralization rather than directly resolving every platform-specific case. [S21] [S14] [S15] [S16]
- S21's review-level claim that algorithmic ranking has limited effects on ideological news balance complements, but does not directly replicate, S11's finding that X's algorithm promoted conservative content and affected selected attitudes and follows. These results may differ because ideological balance and directional content promotion are distinct measures. [S21] [S11]

### Important Gaps

- What were the exact samples, periods, measures, and effect sizes in the Facebook and Google studies cited by S21?
- Under what conditions do weak-tie and cross-cutting exposures outweigh personalization, partisan self-selection, or emotionally engaging content?
- Do diverse or cross-cutting exposures produce durable moderation, and do any such effects translate into consequential political behavior?
- How should ideological balance be distinguished from exposure to extreme, uncivil, misleading, or antagonistic content when evaluating algorithmic effects?

**Analysis Duration:** 12.75s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The runner reached the maximum research iteration budget. Analyzer assessment: The central question can now be answered responsibly: algorithms clearly change exposure, while causal effects on beliefs are heterogeneous and effects on consequential political behavior remain unsupported in the supplied material. S21 adds useful review-level evidence against a universal filter-bubble account but does not create a critical unresolved gap requiring another search.

**Stop Reason:** max_iterations

---

# Final Research Decision

**Research Stopped Because**

The runner reached the maximum research iteration budget.

**Stop Reason:** max_iterations

**Searches Performed:** 10

**Unique Sources:** 21

**Remaining Uncertainty**

- Whether short-term changes in affect, policy attitudes, or account-following persist over months or years.
- Whether recommendation algorithms affect voting, turnout, protest, donations, or other consequential political participation.
- The relative contribution of algorithmic ranking compared with user self-selection, partisan identity, network composition, political elites, and other media.
- How findings generalize across platforms, countries, elections, algorithm versions, and less politically engaged users.
- Why particular X interventions produce effects absent in Meta experiments or in studies separating ideological exposure from algorithmic selection.
- Complete methodological details, attrition, compliance, subgroup effects, and uncertainty estimates are not available for every reported study.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 10 | 37.62s |
| OpenAI Analysis | 10 | 141.16s |
| Report Generation | 1 | 15.31s |
| Total Run | — | 194.10s |
