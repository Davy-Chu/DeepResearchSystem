# Research Run Log

## Run Summary

**System Version:** evidence-ledger-decomposer-v1

**Research Question**

To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 13

**OpenAI Calls:** 7

**Tavily Calls:** 3

**Started:** 2026-08-31T21:09:58-04:00

**Ended:** 2026-08-31T21:11:33-04:00

**Total Runtime:** 94.70s

---

# Research Plan

## Subquestions

### SQ1 [CORE]

**Question:**

What evidence shows that social-media recommendation algorithms change the political content, sources, viewpoints, or ideological diversity that users see or engage with?

**Success criteria:**

Identify and characterize empirical studies that measure algorithmic effects on users’ exposure or engagement, distinguishing recommendation-driven changes from users’ own selection, following, and network effects; report the platforms, populations, timeframes, methods, and magnitude and direction of findings where available.

**Initial status:** UNRESEARCHED

### SQ2 [CORE]

**Question:**

What evidence shows that social-media recommendation algorithms change users’ political beliefs, attitudes, polarization, or political behavior?

**Success criteria:**

Identify and characterize causal or otherwise well-supported evidence linking algorithmic recommendations to changes in political beliefs, affective or ideological polarization, political participation, voting-related behavior, or other political conduct; distinguish measured outcomes from exposure outcomes and state the strength and limits of causal identification.

**Initial status:** UNRESEARCHED

### SQ3 [CORE]

**Question:**

Why does the literature reach different conclusions about the political effects of recommendation algorithms?

**Success criteria:**

Synthesize explanations involving differences in definitions of polarization, platforms and algorithm designs, user populations and political contexts, study periods, exposure intensity, content and network environments, research designs and interventions, outcome measures, and possible heterogeneous or short- versus long-term effects.

**Initial status:** UNRESEARCHED

### SQ4 [CORE]

**Question:**

To what extent can the evidence support an overall conclusion about algorithms’ contribution to political polarization, given the distinction between changing exposure and changing beliefs or behavior?

**Success criteria:**

Integrate the exposure and outcome evidence without treating changes in what users see as proof of changed beliefs or behavior; assess the relative strength, consistency, causal credibility, and uncertainty of the evidence and formulate a qualified overall judgment.

**Initial status:** UNRESEARCHED

## Synthesis Requirements

- Keep evidence about changes in users’ information exposure analytically separate from evidence about changes in political beliefs, polarization, or behavior.
- Distinguish correlation, selection, and mediation from causal effects attributable specifically to recommendation algorithms.
- Explain conflicting findings rather than merely listing them, including differences in platforms, populations, contexts, timeframes, methods, and outcome definitions.
- Preserve uncertainty and avoid inferring belief or behavioral change solely from exposure or engagement changes.

## Output Requirements

- Answer the extent question with a qualified synthesis rather than a binary conclusion.
- Present separate treatment of exposure effects and effects on political beliefs or behavior.
- Explain why the literature reaches different conclusions.

---

# Iteration 1

## 1. Search

**Query**

> To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions.

**Purpose:** GENERAL

**Why this query**

This is the user's original research question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S1 — The Impact Of Social Media Algorithms On Information Bubbles And Political Polarization. - Consensus Academic Search Engine**
  URL: https://consensus.app/questions/impact-social-media-algorithms-information-bubbles
- **S2 — The Impact of Social Media Algorithms on Political Polarization » boslabour.org.uk**
  URL: https://boslabour.org.uk/the-impact-of-social-media-algorithms-on-political-polarization
- **S3 — Impact of Social Media Algorithms on Polarization | PDF | Social Media | Popular Culture & Media Studies**
  URL: https://www.scribd.com/document/870029496/Social-Media-Algorithms-and-Political-Polarization
- **S4 — Social Algorithms and Political Polarization: A Teenager’s Perspective on Social Media and American Divisiveness [Opinion] - VOX ATL**
  URL: https://voxatl.org/social-algorithms-political-polarization-teen-perspective
- **S5 — The Political and Psychological Costs of Social Media Algorithms: Evidence-Based Strategies to Mitigate Algorithm-Driven Addiction, Echo Chambers, Polarization, and Misinformation - Gilmore Health News**
  URL: https://www.gilmorehealth.com/the-political-and-psychological-costs-of-social-media-algorithms-evidence-based-strategies-to-mitigate-algorithm-driven-addiction-echo-chambers-polarization-and-misinformation

**Search Duration:** 4.86s

---

## 2. Evidence Processing

- New claim proposals: 3
- Existing claim updates: 0
- New gaps: 4
- Resolved gaps: 0

**Processing Duration:** 12.41s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

The supplied sources describe recommendation algorithms as changing users’ political exposure by prioritizing personalized, engagement-relevant content and potentially reducing exposure to diverse or counter-attitudinal viewpoints.

- S1 supports (indirect): Reports that personalization and algorithmic filtering can limit exposure to diverse perspectives and counter-attitudinal news; it also mentions experiments in which small changes in filtering affected polarization.
- S2 supports (indirect): States that platforms curate feeds according to user interactions and preferences, prioritizing partisan or belief-consistent information and excluding some diverse perspectives.
- S5 supports (indirect): Describes algorithms as delivering customized content based on user data and argues that repeated presentation of belief-consistent content can form echo chambers.

**Confidence:** LOW

**Status:** WEAK

### New Claim C2

**Claim**

The supplied sources allege that algorithmically curated, belief-consistent content can reinforce existing political beliefs and contribute to polarization, but they do not provide sufficiently detailed evidence to establish the size or causal consistency of effects on beliefs, attitudes, or behavior.

- S1 supports (indirect): Claims that algorithmic filtering and uniform, politically aligned news can reinforce beliefs and increase polarization, citing unspecified experiments and studies.
- S2 supports (indirect): Attributes intensified ideological divisions and effects on political attitudes and behaviors to algorithm-driven partisan curation, but does not report the underlying study designs or results.
- S5 supports (indirect): Claims that repeated belief-consistent content deepens polarization and that engagement optimization can amplify highly reactive content.

**Confidence:** LOW

**Status:** INSUFFICIENT_EVIDENCE

### New Claim C3

**Claim**

The supplied sources identify user behavior and pre-existing preferences as complementary contributors to politically homogeneous exposure, rather than presenting recommendation algorithms as the sole cause of polarization.

- S1 supports (direct): Explicitly states that user behavior also contributes to polarization alongside algorithms’ role in creating filter bubbles.
- S2 supports (indirect): Describes curation based on user interactions and preferences, implying that user selection and engagement feed into recommendation outcomes.
- S4 supports (indirect): Frames algorithms as operating in a relationship with confirmation bias and gives anecdotal examples of partisan media environments, though it is an opinion piece rather than a systematic study.

**Confidence:** MEDIUM

**Status:** WEAK

### New Gap G1

No supplied source gives identifiable primary-study details—platform, population, timeframe, design, exposure measure, comparison condition, or effect size—needed to assess how much recommendation algorithms change political content exposure or ideological diversity independently of users’ following and selection.

### New Gap G2

The supplied material does not provide well-documented causal evidence that recommendation algorithms change political beliefs, affective or ideological polarization, voting-related behavior, or political participation. Claims about these outcomes are mostly generalized summaries or anecdotes.

### New Gap G3

The sources do not adequately explain conflicting findings across platforms, algorithm designs, populations, political contexts, periods, exposure intensity, intervention types, or definitions of polarization; consequently, heterogeneity and short- versus long-term effects remain unresolved.

### New Gap G4

The supplied sources do not clearly separate recommendation effects from selection, confirmation bias, homophily, network effects, and general social-media use, preventing a confident estimate of the algorithms’ independent contribution.

---

## 4. Current Research State

- Claims: 3
- Supported: 0
- Weak: 2
- Conflicting: 0
- Insufficient Evidence: 1
- Open Gaps: 4
- Remaining Searches: 2

### Subquestion Progress

**SQ1:** UNRESEARCHED → PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ2:** UNRESEARCHED → PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ3:** UNRESEARCHED → PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ4:** UNRESEARCHED → PARTIAL

Reason: At least one linked ledger claim is not yet supported.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → PARTIAL (targeted searches: 0)
- SQ3 → PARTIAL (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- None

**Remaining targeted searches:** 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ2

**Why**

SQ2 is a high-priority CORE subquestion with only indirect claims and an open gap concerning causal effects on political beliefs, polarization, or behavior. A focused search for randomized or quasi-experimental platform interventions would materially improve the answer.

**Next Search**

> Causal empirical studies randomized experiments social-media recommendation algorithms political beliefs affective polarization voting behavior Facebook feed ranking YouTube recommendations algorithmic curation


---

# Iteration 2

## 1. Search

**Query**

> Causal empirical studies randomized experiments social-media recommendation algorithms political beliefs affective polarization voting behavior Facebook feed ranking YouTube recommendations algorithmic curation

**Target:** SQ2

**Purpose:** SUBQUESTION

**Why this query**

SQ2 is a high-priority CORE subquestion with only indirect claims and an open gap concerning causal effects on political beliefs, polarization, or behavior. A focused search for randomized or quasi-experimental platform interventions would materially improve the answer.

5 result(s) retrieved; 5 new unique source(s) added.

- **S6 — How algorithmically curated online environments influence users’ political polarization: Results from two experiments with panel data**
  URL: https://www.sciencedirect.com/science/article/pii/S2451958823000763
- **S7 — The Role of Social Media Algorithms in Shaping Political Polarisation in the United States**
  URL: https://www.humanrightsresearch.org/post/the-role-of-social-media-algorithms-in-shaping-political-polarisation-in-the-united-states
- **S8 — The political effects of X’s feed algorithm**
  URL: https://www.nature.com/articles/s41586-026-10098-2
- **S9 — How X’s algorithm shifts political attitudes**
  URL: https://cepr.org/voxeu/columns/how-xs-algorithm-shifts-political-attitudes
- **S10 — How do social media feed algorithms affect attitudes and ...**
  URL: https://cdr.lib.unc.edu/downloads/wp9891401

**Search Duration:** 2.69s

---

## 2. Evidence Processing

- New claim proposals: 4
- Existing claim updates: 3
- New gaps: 2
- Resolved gaps: 1

**Processing Duration:** 22.03s

---

## 3. Ledger Updates

### New Claim C4

**Claim**

In a randomized 2020 US-election experiment on Facebook and Instagram, replacing default algorithmic feeds with reverse-chronological feeds substantially changed users’ on-platform experience and political exposure: users spent less time and were less active, saw more political and untrustworthy content on both platforms, and on Facebook saw less uncivil/slur content and more content from moderate friends and ideologically mixed sources.

- S10 supports (direct): Reports randomized assignment of consenting Facebook and Instagram users to chronological rather than default algorithmic feeds during the 2020 US election; documents changes in time, activity, political and untrustworthy content, uncivil/slur content, and moderate or ideologically mixed sources.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C5

**Claim**

The Facebook and Instagram feed experiment found no statistically significant change in issue polarization, affective polarization, political knowledge, or other key political attitudes during its three-month study period, despite substantial changes in exposure and on-platform activity.

- S10 supports (direct): States that the chronological-feed treatment substantially changed users’ experience and exposure but did not significantly alter issue polarization, affective polarization, political knowledge, or other key attitudes over three months.
- S6 contradicts (direct): In two experimental panel studies, like-minded exposure increased attitude and affective polarization, and algorithmically selected arguments produced a small additional attitude-polarization effect for one topic.
- S8 contradicts (direct): Reports a seven-week randomized X field experiment in which switching from chronological to algorithmic feeds shifted political opinion toward more conservative positions, although it did not substantially change partisanship or polarization.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C6

**Claim**

Two experiments with panel data in Germany found that exposure to like-minded political arguments increased attitude and affective polarization more than exposure to opposing arguments, but algorithmic selection generally did not amplify those exposure effects; it produced only a small direct attitude-polarization effect for one topic relative to random selection.

- S6 supports (direct): Describes two quasi-experiments with a three-wave panel survey in which participants received algorithmically or randomly selected arguments that were attitude-consistent or attitude-inconsistent; like-minded exposure increased attitude and affective polarization, while algorithmic selection did not generally amplify the effect and had a small direct effect for one topic.
- S10 contradicts (direct): A randomized Facebook and Instagram experiment found no significant changes in issue or affective polarization after changing feed ranking, despite substantial exposure changes.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C7

**Claim**

A randomized seven-week 2023 field experiment among active US-based X users found that switching from a chronological feed to X’s algorithmic feed increased engagement and shifted political opinions toward more conservative positions, while not producing a major change in partisanship or polarization; the algorithm also increased conservative activist content and reduced the visibility of traditional news sources.

- S8 supports (direct): Reports random assignment of active US-based X users to algorithmic or chronological feeds for seven weeks, with increased engagement, more conservative political opinions, increased conservative activist content, and reduced traditional-news visibility, but no major effect on partisanship or polarization.
- S7 supports (indirect): Summarizes the same X field experiment and its reported seven-week attitude, engagement, and content-visibility findings.
- S10 contradicts (direct): The Facebook and Instagram randomized feed experiment found no significant political-attitude or polarization effects during three months, despite exposure changes.

**Confidence:** HIGH

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

The supplied sources describe recommendation algorithms as changing users’ political exposure by prioritizing personalized, engagement-relevant content and potentially reducing exposure to diverse or counter-attitudinal viewpoints.

- S10 supports (direct): A randomized Facebook and Instagram intervention directly shows that replacing algorithmic ranking changed political exposure, source mix, content characteristics, engagement, and time spent.
- S6 supports (direct): Experimental environments varied algorithmic versus random selection and attitude-consistent versus opposing arguments, directly separating exposure alignment from algorithmic selection.
- S8 supports (direct): A randomized X field experiment reports that feed type changed engagement and the visibility of conservative activist content and traditional news sources.

**Confidence:** LOW → HIGH

**Status:** WEAK → SUPPORTED

### Updated Claim C2

**Claim**

The supplied sources allege that algorithmically curated, belief-consistent content can reinforce existing political beliefs and contribute to polarization, but they do not provide sufficiently detailed evidence to establish the size or causal consistency of effects on beliefs, attitudes, or behavior.

- S6 supports (direct): A three-wave experimental panel found that like-minded exposure increased attitude and affective polarization, while algorithmic selection itself generally did not amplify the exposure effect and had a small direct attitude effect for one topic.
- S8 supports (direct): A randomized X field experiment found a shift toward more conservative political opinions under the algorithmic feed, without a major change in partisanship or polarization.
- S10 contradicts (direct): A randomized Facebook and Instagram experiment found no significant change in issue polarization, affective polarization, political knowledge, or other key attitudes after a substantial feed-ranking intervention.

**Confidence:** LOW → HIGH

**Status:** INSUFFICIENT_EVIDENCE → CONFLICTING

### Updated Claim C3

**Claim**

The supplied sources identify user behavior and pre-existing preferences as complementary contributors to politically homogeneous exposure, rather than presenting recommendation algorithms as the sole cause of polarization.

- S6 supports (direct): The design explicitly distinguishes exposure to like-minded or opposing arguments from algorithmic versus random selection, showing that content alignment had stronger polarization effects than algorithmic selection in general.
- S10 supports (direct): The study isolates feed-ranking algorithms from users’ existing networks and other platform affordances through randomized replacement of default ranking, while noting that user choice and network composition also shape content.
- S8 supports (indirect): The X experiment compares feed systems, but its reported effects occur within users’ existing platform and network environments, supporting an interaction-based rather than sole-cause interpretation.

**Confidence:** MEDIUM → HIGH

**Status:** WEAK → SUPPORTED

### New Gap G5

The new experiments establish context-specific causal effects but do not provide enough comparable numerical effect sizes, full sample details, or cross-platform evidence to estimate the average magnitude of recommendation algorithms’ independent contribution to exposure change or polarization.

### New Gap G6

The supplied experiments primarily measure short-term or medium-term attitudes, polarization, engagement, and exposure; they do not establish whether the observed effects persist, accumulate, or translate into voting, participation, or other offline political behavior.

### Resolved Gap G2

The supplied material does not provide well-documented causal evidence that recommendation algorithms change political beliefs, affective or ideological polarization, voting-related behavior, or political participation. Claims about these outcomes are mostly generalized summaries or anecdotes.

---

## 4. Current Research State

- Claims: 7
- Supported: 6
- Weak: 0
- Conflicting: 1
- Insufficient Evidence: 0
- Open Gaps: 5
- Remaining Searches: 1

### Subquestion Progress

**SQ1:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** PARTIAL → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ3:** PARTIAL → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ4:** PARTIAL → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → CONFLICTING (targeted searches: 1)
- SQ3 → CONFLICTING (targeted searches: 0)
- SQ4 → CONFLICTING (targeted searches: 0)

**SECONDARY:**

- None

**Remaining targeted searches:** 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ3

**Why**

A final focused search could materially improve the answer by addressing the unresolved core question of why causal findings differ across platforms, interventions, populations, timeframes, and polarization measures. This is necessary to synthesize the conflicting Facebook/Instagram, X, and German experimental results responsibly.

**Next Search**

> Comparative review or meta-analysis explaining conflicting causal findings on social-media recommendation algorithms and political polarization: platform design, user selection, exposure intensity, intervention duration, US versus Europe, polarization measures, and short- versus long-term effects


---

# Iteration 3

## 1. Search

**Query**

> Comparative review or meta-analysis explaining conflicting causal findings on social-media recommendation algorithms and political polarization: platform design, user selection, exposure intensity, intervention duration, US versus Europe, polarization measures, and short- versus long-term effects

**Target:** SQ3

**Purpose:** SUBQUESTION

**Why this query**

A final focused search could materially improve the answer by addressing the unresolved core question of why causal findings differ across platforms, interventions, populations, timeframes, and polarization measures. This is necessary to synthesize the conflicting Facebook/Instagram, X, and German experimental results responsibly.

5 result(s) retrieved; 3 new unique source(s) added.

- **S11 — Ranking for engagement: How social media algorithms fuel misinformation and polarization**
  URL: https://www.sciencedirect.com/science/article/pii/S0047272726000253
- **S12 — Social Media, Echo Chambers, and Political Polarization (Chapter 3) - Social Media and Democracy**
  URL: https://www.cambridge.org/core/books/social-media-and-democracy/social-media-echo-chambers-and-political-polarization/333A5B4DE1B67EFF7876261118CCFE19
- **S13 — The Algorithmic Management of Polarization and Violence on Social Media | Knight First Amendment Institute**
  URL: https://knightcolumbia.org/content/the-algorithmic-management-of-polarization-and-violence-on-social-media

**Search Duration:** 2.47s

---

## 2. Evidence Processing

- New claim proposals: 2
- Existing claim updates: 4
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 17.96s

---

## 3. Ledger Updates

### New Claim C8

**Claim**

A 2020 review reports that empirical studies often find limited effects of ranking algorithms on the ideological balance of news consumption on Facebook or Google, while weak-tie connections can expose users to ideologically diverse information; therefore, politically homogeneous interaction does not by itself establish a widespread algorithmic filter bubble.

- S12 supports (direct): The review states that ranking algorithms do not have a large impact on the ideological balance of news consumption on Facebook or Google and that weak ties can increase exposure to novel and ideologically diverse news. It presents the empirical literature as more nuanced than the conventional filter-bubble account.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C9

**Claim**

A theoretical model argues that engagement-weighted and personalized ranking can create a feedback loop in which extreme users engage disproportionately, increasing the visibility of misinformation and ideologically polarizing content; survey evidence from the United States and Italy around Facebook’s 2018 Meaningful Social Interactions update is reported as consistent with increased ideological extremism and affective polarization, but the supplied material does not establish the strength of the causal identification.

- S11 supports (direct): The paper develops a dynamic model linking engagement-based ranking, user behavior, misinformation, and polarization, and reports that survey evidence around Facebook’s 2018 algorithmic update is consistent with increased ideological extremism and affective polarization.

**Confidence:** MEDIUM

**Status:** WEAK

### Updated Claim C1

**Claim**

The supplied sources describe recommendation algorithms as changing users’ political exposure by prioritizing personalized, engagement-relevant content and potentially reducing exposure to diverse or counter-attitudinal viewpoints.

- S11 supports (direct): The model identifies engagement-weighted and personalized ranking as mechanisms that can amplify misinformation and ideological polarization through a feedback loop.
- S13 supports (indirect): The essay argues that prioritizing distribution based on engagement can incentivize divisive content and recommends monitoring or changing ranking signals in conflict-sensitive contexts.
- S12 contradicts (direct): The review reports that empirical studies found ranking algorithms had little impact on the ideological balance of news consumption on Facebook or Google, qualifying any general claim that recommendation systems uniformly reduce viewpoint diversity.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

The supplied sources allege that algorithmically curated, belief-consistent content can reinforce existing political beliefs and contribute to polarization, but they do not provide sufficiently detailed evidence to establish the size or causal consistency of effects on beliefs, attitudes, or behavior.

- S11 supports (direct): A theoretical model predicts that engagement-based and personalized ranking can increase misinformation and polarization, and reports survey evidence around Facebook’s 2018 update consistent with increased ideological extremism and affective polarization.
- S13 supports (indirect): The essay synthesizes platform experiments, creator reports, and conflict-setting experiences to argue that engagement-oriented design can incentivize divisive speech, harassment, and manipulation, with possible implications for destructive conflict.
- S12 contradicts (direct): The review emphasizes that empirical findings are nuanced and reports limited effects of ranking algorithms on ideological news balance, while also noting exposure to diverse information through weak ties; this qualifies broad claims that algorithmic curation reliably increases polarization.

**Confidence:** HIGH → HIGH

**Status:** CONFLICTING → CONFLICTING

### Updated Claim C3

**Claim**

The supplied sources identify user behavior and pre-existing preferences as complementary contributors to politically homogeneous exposure, rather than presenting recommendation algorithms as the sole cause of polarization.

- S11 supports (direct): The model explicitly describes a dynamic feedback loop between user behavior and algorithmic ranking, with extreme users’ disproportionate engagement contributing to amplification.
- S12 supports (direct): The review attributes diverse exposure in part to weak ties and presents algorithmic ranking as only one factor among social-network processes affecting ideological exposure.
- S13 supports (indirect): The essay focuses on interactions between platform design, conflict actors, divisive content production, harassment, and manipulation rather than treating ranking as a sole cause.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

The Facebook and Instagram feed experiment found no statistically significant change in issue polarization, affective polarization, political knowledge, or other key political attitudes during its three-month study period, despite substantial changes in exposure and on-platform activity.

- S12 supports (indirect): The review characterizes the empirical literature as nuanced and reports that ranking algorithms did not have a large impact on ideological news balance in some platform settings, consistent with the possibility that substantial exposure changes need not produce uniform polarization effects.
- S11 contradicts (indirect): The paper reports survey evidence around Facebook’s 2018 Meaningful Social Interactions update consistent with increased ideological extremism and affective polarization, though the supplied excerpt does not establish causal identification.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 9
- Supported: 7
- Weak: 1
- Conflicting: 1
- Insufficient Evidence: 0
- Open Gaps: 5
- Remaining Searches: 0

### Subquestion Progress

**SQ1:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ3:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ4:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → CONFLICTING (targeted searches: 1)
- SQ3 → CONFLICTING (targeted searches: 1)
- SQ4 → CONFLICTING (targeted searches: 0)

**SECONDARY:**

- None

**Remaining targeted searches:** 0

---

## 5. Research Decision

**Decision:** Stop researching.

**Origin:** BUDGET_STOP

**Why**

The maximum research iteration budget was reached.

**Stop Reason:** max_iterations


---

# Final Research Decision

**Stop Reason:** max_iterations

**Remaining Uncertainty**

- Primary-study details and comparable effect sizes are insufficient to estimate how much recommendation ranking independently changes political exposure or ideological diversity.
- The independent effects of recommendation ranking cannot be cleanly separated from user selection, confirmation bias, homophily, network effects, and general social-media use across the supplied sources.
- The evidence does not adequately resolve heterogeneity by platform, algorithm design, population, political context, study period, exposure intensity, intervention type, or outcome definition.
- The supplied experiments do not establish persistence, cumulative effects, voting effects, participation effects, or other offline behavioral consequences.
- The verification process stopped because the maximum number of iterations was reached; no additional verification records were supplied.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Question Decomposition | 1 | 8.08s |
| Tavily Search | 3 | 10.01s |
| Evidence Processing | 3 | 52.40s |
| Research Decision | 2 | 7.46s |
| Report Generation | 1 | 16.73s |
| Total Run | — | 94.70s |
