# Research Run Log

## Run Summary

**System Version:** evidence-ledger-decomposer-v1

**Research Question**

To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions.

**Status:** Failed

**Failure Stage:** OpenAI Evidence Processing — Iteration 3

**Error**

Update C4 contains CONTRADICTS evidence in the SUPPORTS collection

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 13

**OpenAI Calls:** 6

**Tavily Calls:** 3

**Started:** 2026-08-31T18:51:47-04:00

**Ended:** 2026-08-31T18:53:01-04:00

**Total Runtime:** 73.53s

---

# Research Plan

## Subquestions

### SQ1 [CORE]

**Question:**

What evidence shows that social-media recommendation algorithms change the political content, sources, viewpoints, or ideological diversity that users see or engage with?

**Success criteria:**

Identify and characterize relevant empirical studies, distinguishing algorithmic recommendations from other platform features and from user self-selection; report the direction, magnitude, and conditions of observed changes in exposure or engagement, including uncertainty and methodological limitations.

**Initial status:** UNRESEARCHED

### SQ2 [CORE]

**Question:**

What evidence shows that social-media recommendation algorithms change users’ political beliefs, attitudes, polarization, or political behavior?

**Success criteria:**

Identify empirical evidence on downstream effects beyond exposure, distinguishing changes in beliefs or affective/ideological polarization from changes in political participation or other behavior; report causal identification, effect size or direction, duration, heterogeneity, uncertainty, and limitations.

**Initial status:** UNRESEARCHED

### SQ3 [CORE]

**Question:**

Why does the literature reach different conclusions about the political effects of recommendation algorithms?

**Success criteria:**

Synthesize explanations involving differences in outcome definitions, exposure versus persuasion measures, research designs and causal identification, platforms and recommendation systems, populations and political contexts, time periods, content and user behavior, and measurement or data limitations; connect each explanation to the divergent findings.

**Initial status:** UNRESEARCHED

### SQ4 [CORE]

**Question:**

How should the overall contribution of recommendation algorithms to political polarization be characterized, given the distinction between changing exposure and changing beliefs or behavior?

**Success criteria:**

Integrate the evidence without conflating exposure effects with downstream political effects; state what can and cannot be concluded about the extent of contribution, including whether effects appear large, small, conditional, indirect, or uncertain.

**Initial status:** UNRESEARCHED

## Synthesis Requirements

- Maintain a clear distinction between algorithms changing what users see and algorithms changing political beliefs or behavior.
- Explain divergent findings rather than merely listing studies, including differences in causal inference, outcomes, platforms, populations, contexts, and timeframes where relevant.
- Assess contribution to political polarization specifically, while distinguishing ideological, affective, and behavioral outcomes when the evidence permits.
- Represent uncertainty, conflicting evidence, and limitations explicitly.

## Output Requirements

- Provide an evidence-based assessment of the extent to which recommendation algorithms contribute to political polarization.
- Present exposure effects separately from effects on political beliefs or behavior.
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

- **S1 — How algorithmically curated online environments influence users’ political polarization: Results from two experiments with panel data - ScienceDirect**
  URL: https://www.sciencedirect.com/science/article/pii/S2451958823000763
- **S2 — The Role of Social Media Algorithms in Shaping Political Polarisation in the United States**
  URL: https://www.humanrightsresearch.org/post/the-role-of-social-media-algorithms-in-shaping-political-polarisation-in-the-united-states
- **S3 — Social Drivers and Algorithmic Mechanisms on Digital Media**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11373151
- **S4 — Algorithms Shift Polarization. Why Does Policy Still Miss ...**
  URL: https://techpolicy.press/algorithms-shift-polarization-why-does-policy-still-miss-the-real-problem
- **S5 — How Does Social Media Impact Political Polarization?**
  URL: https://news.northeastern.edu/2025/11/27/social-media-political-polarization-research

**Search Duration:** 2.81s

---

## 2. Evidence Processing

- New claim proposals: 5
- Existing claim updates: 0
- New gaps: 4
- Resolved gaps: 0

**Processing Duration:** 14.82s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

In two panel quasi-experiments, exposure to like-minded political arguments increased attitude and affective polarization more than exposure to opposing arguments; algorithmic selection did not generally amplify these exposure effects, although it produced a small additional attitude-polarization effect for one topic.

- S1 supports (direct): The study compared algorithmically selected with randomly selected arguments that were either attitude-congruent or attitude-incongruent. Like-minded exposure increased attitude and affective polarization more strongly than opposing exposure, while algorithmic selection generally did not amplify the effects and had a small direct effect for one topic.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C2

**Claim**

A browser-extension experiment on X that reranked, rather than removed, posts to increase or decrease exposure to antidemocratic attitudes and partisan animosity changed affective polarization after one week: reduced exposure made participants feel about 2.11 points warmer toward the opposing party, while increased exposure made them about 2.48 points cooler on a 100-point scale.

- S4 supports (direct): A report on the Science study states that 1,256 U.S. participants were assigned to increased or decreased exposure to antidemocratic and partisan-animosity content for one week, producing opposing-party feeling changes of 2.11 and 2.48 points.
- S5 supports (direct): The institutional news report describes the browser-extension reranking experiment, its more-than-1,200 participants, the one-week intervention, and approximately two-point shifts in feelings toward the opposing party.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C3

**Claim**

The X reranking experiment altered political attitudes without changing the underlying set of followed posts: it changed the order and prominence of content, and the reported effects were not necessarily consciously perceived by users.

- S5 supports (direct): The experiment is described as reranking posts within users' existing feeds without removing content; participants reportedly could not notice the reranking, while exposure to partisan-animosity content was increased or decreased.
- S4 supports (direct): The report states that the content and users remained the same and only ranking changed, and that 74% of participants reported noticing no impact on their experience.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C4

**Claim**

The available overview characterizes algorithmic effects on polarization as non-straightforward and argues that algorithms often reinforce pre-existing social drivers rather than independently determining polarization; feedback between user behavior and algorithmic curation makes causal attribution difficult.

- S3 supports (direct): The review states that algorithms create feedback loops with social drivers, that evidence concerning polarization is far from straightforward, and that existing evidence suggests algorithms mostly reinforce existing social drivers.
- S1 supports (indirect): The study notes that prior research often could not separate effects of exposure to like-minded content from effects caused by algorithms themselves, and finds stronger effects for like-minded exposure than for algorithmic selection.
- S4 contradicts (direct): The report presents the X reranking experiment as causal evidence that changing algorithmic ranking directly changed affective polarization, indicating that algorithms can have effects beyond merely reflecting user preferences.
- S5 contradicts (direct): The report describes a controlled reranking intervention in which changing ranking changed partisan feelings despite retaining the same posts and users.

**Confidence:** MEDIUM

**Status:** CONFLICTING

### New Claim C5

**Claim**

The supplied evidence does not establish that recommendation algorithms change political participation, voting, or other political behavior; the reported downstream outcomes concern attitudes, affective polarization, and partisan feelings.

- No new evidence relationship was added.

**Confidence:** HIGH

**Status:** INSUFFICIENT_EVIDENCE

### New Gap G1

Evidence is insufficient to determine whether recommendation algorithms change political behavior, including participation, voting, sharing, or other offline and online political actions.

### New Gap G2

The evidence base does not permit a reliable estimate of the average magnitude, duration, persistence, or cumulative population-level contribution of recommendation algorithms to polarization across platforms and political contexts.

### New Gap G3

The supplied sources do not adequately compare platforms, recommendation objectives, user populations, political systems, or time periods, limiting explanation of when algorithmic exposure effects generalize.

### New Gap G4

The materials do not provide enough methodological detail to assess uncertainty, attrition, sample representativeness, intervention compliance, or the full causal identification strategy of the reported X experiment.

---

## 4. Current Research State

- Claims: 5
- Supported: 3
- Weak: 0
- Conflicting: 1
- Insufficient Evidence: 1
- Open Gaps: 4
- Remaining Searches: 2

### Subquestion Progress

**SQ1:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** UNRESEARCHED → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ3:** UNRESEARCHED → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ4:** UNRESEARCHED → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → CONFLICTING (targeted searches: 0)
- SQ3 → CONFLICTING (targeted searches: 0)
- SQ4 → CONFLICTING (targeted searches: 0)

**SECONDARY:**

- None

**Remaining targeted searches:** 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ2

**Why**

SQ2 remains unresolved, with a high-importance gap concerning whether recommendation algorithms affect political participation, voting, sharing, or other political behavior. The current evidence only establishes attitude and affective-polarization outcomes, so targeted behavioral evidence would materially improve the answer.

**Next Search**

> Empirical causal studies testing whether social-media recommendation algorithms affect political behavior: voting, turnout, political participation, sharing, protest, or offline action; distinguish recommendation/ranking interventions from general social-media use and report effect sizes, duration, heterogeneity, and limitations.


---

# Iteration 2

## 1. Search

**Query**

> Empirical causal studies testing whether social-media recommendation algorithms affect political behavior: voting, turnout, political participation, sharing, protest, or offline action; distinguish recommendation/ranking interventions from general social-media use and report effect sizes, duration, heterogeneity, and limitations.

**Target:** SQ2

**Purpose:** SUBQUESTION

**Why this query**

SQ2 remains unresolved, with a high-importance gap concerning whether recommendation algorithms affect political participation, voting, sharing, or other political behavior. The current evidence only establishes attitude and affective-polarization outcomes, so targeted behavioral evidence would materially improve the answer.

5 result(s) retrieved; 5 new unique source(s) added.

- **S6 — How do social media feed algorithms affect attitudes and ...**
  URL: https://cdr.lib.unc.edu/downloads/wp9891401
- **S7 — A systematic review of worldwide causal and correlational ...**
  URL: https://www.nature.com/articles/s41562-022-01460-1
- **S8 — First Findings Shed Light on Role of Social Media Algorithms in 2020 ...**
  URL: https://news.utexas.edu/2023/07/27/first-findings-shed-light-on-role-of-social-media-algorithms-in-2020-election
- **S9 — How Social Media and Embedded Recommender Algorithm ...**
  URL: https://commons.clarku.edu/cgi/viewcontent.cgi?article=1086&context=sps_masters_papers
- **S10 — Op-ed: Social media algorithms & their effects on American ...**
  URL: https://funginstitute.berkeley.edu/news/op-ed-social-media-algorithms-their-effects-on-american-politics

**Search Duration:** 3.74s

---

## 2. Evidence Processing

- New claim proposals: 4
- Existing claim updates: 2
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 16.93s

---

## 3. Ledger Updates

### New Claim C6

**Claim**

In a randomized 2020 U.S. election experiment on Facebook and Instagram, replacing personalized algorithmic feeds with reverse-chronological feeds substantially changed users’ on-platform experience and exposure: it reduced time spent and activity, increased political and untrustworthy content on both platforms, increased exposure to moderate friends and ideologically mixed sources on Facebook, and decreased uncivil or slur-containing content on Facebook. Despite these exposure and engagement changes over three months, it did not significantly change issue polarization, affective polarization, political knowledge, or other key political attitudes.

- S6 supports (direct): The study directly reports random assignment to chronological versus default algorithmic feeds, substantial changes in exposure and activity, and null effects on several political-attitude and polarization outcomes during the three-month intervention.
- S8 supports (direct): The university summary reports that changing fundamental parts of Facebook and Instagram’s algorithms substantially changed content exposure but did not significantly affect political attitudes, polarization, ideological extremity, or candidate evaluations.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C7

**Claim**

The Meta 2020 election experiments provide evidence that algorithmic feed ranking can substantially alter exposure and on-platform engagement without producing detectable short-run changes in measured political attitudes or polarization, illustrating that exposure effects do not automatically translate into downstream belief effects.

- S6 supports (direct): The randomized replacement of algorithmic ranking changed content exposure and time/activity while leaving issue polarization, affective polarization, political knowledge, and other key attitudes statistically unchanged over three months.
- S8 supports (direct): The project summary explicitly contrasts the algorithm’s large effect on what people see with the absence of significant effects on political attitudes and polarization.
- S4 contradicts (direct): The X reranking experiment reported short-run causal changes in opposing-party feelings after one week, indicating that at least some ranking interventions can affect affective polarization.
- S5 contradicts (direct): The reported X experiment found approximately two-point changes in opposing-party feelings following increased or decreased exposure to partisan-animosity content.

**Confidence:** HIGH

**Status:** CONFLICTING

### New Claim C8

**Claim**

Differences in conclusions may reflect differences in the intervention and counterfactual: the Meta experiments replaced the entire default feed-ranking system with chronological ordering for three months, whereas the X experiment reranked particular types of content for one week; these designs alter different aspects of users’ information environments and may produce different downstream effects.

- S6 supports (direct): The Meta study identifies chronological feeds as the counterfactual to personalized ranking and emphasizes that total feed-system effects require a well-understood alternative; its intervention lasted three months.
- S4 supports (direct): The X study report describes a one-week intervention that increased or decreased exposure to antidemocratic and partisan-animosity content through reranking.
- S5 supports (direct): The institutional report likewise distinguishes reranking within existing feeds from broader feed replacement and reports the one-week duration.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C9

**Claim**

Evidence from the broader digital-media literature suggests that political effects vary by outcome and political system: participation and information consumption can be beneficial associations, while declining trust, populism, and polarization are more pronounced in established democracies; this broader pattern is relevant context but does not isolate recommendation algorithms.

- S7 supports (direct): A systematic review of 496 causal and correlational articles reports outcome- and system-dependent associations, with polarization-related associations more pronounced in established democracies.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C4

**Claim**

The available overview characterizes algorithmic effects on polarization as non-straightforward and argues that algorithms often reinforce pre-existing social drivers rather than independently determining polarization; feedback between user behavior and algorithmic curation makes causal attribution difficult.

- S6 supports (direct): The randomized Meta experiments found large changes in exposure and activity but no significant changes in polarization or key attitudes, supporting a non-straightforward and conditional account of algorithmic political effects.
- S8 supports (direct): The project summary states that algorithms strongly shaped on-platform experiences while changing them did not alter political attitudes, reinforcing the distinction between algorithmic exposure and downstream polarization.

**Confidence:** MEDIUM → HIGH

**Status:** CONFLICTING → CONFLICTING

### Updated Claim C5

**Claim**

The supplied evidence does not establish that recommendation algorithms change political participation, voting, or other political behavior; the reported downstream outcomes concern attitudes, affective polarization, and partisan feelings.

- S6 supports (direct): The Meta experiment changed time spent and on-platform activity, but the reported downstream political outcomes were attitudes, knowledge, and polarization; it provides no evidence about voting, participation, or other political behavior.
- S8 supports (indirect): The summary lists null effects on political attitudes and polarization and does not report effects on voting or political participation.

**Confidence:** HIGH → HIGH

**Status:** INSUFFICIENT_EVIDENCE → INSUFFICIENT_EVIDENCE

---

## 4. Current Research State

- Claims: 9
- Supported: 6
- Weak: 0
- Conflicting: 2
- Insufficient Evidence: 1
- Open Gaps: 4
- Remaining Searches: 1

### Subquestion Progress

**SQ1:** PARTIAL → CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ2:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ3:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

**SQ4:** CONFLICTING

Reason: At least one linked ledger claim contains conflicting evidence.

### Research Plan Status

**CORE:**

- SQ1 → CONFLICTING (targeted searches: 0)
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

A final focused search could materially improve the explanation of conflicting findings, especially by directly comparing the Meta feed-replacement experiments with the X reranking experiment and identifying how intervention type, outcome measurement, duration, platform, and causal design account for divergent results. SQ3 is a CORE subquestion with no prior targeted search.

**Next Search**

> Compare causal studies of social-media recommendation algorithms and political polarization, especially Meta/Facebook-Instagram chronological-feed experiments versus X/Twitter reranking experiments: how do intervention, counterfactual, exposure measure, polarization outcome, duration, platform, sample, and causal design explain divergent findings?


---

# Iteration 3

## 1. Search

**Query**

> Compare causal studies of social-media recommendation algorithms and political polarization, especially Meta/Facebook-Instagram chronological-feed experiments versus X/Twitter reranking experiments: how do intervention, counterfactual, exposure measure, polarization outcome, duration, platform, sample, and causal design explain divergent findings?

**Target:** SQ3

**Purpose:** SUBQUESTION

**Why this query**

A final focused search could materially improve the explanation of conflicting findings, especially by directly comparing the Meta feed-replacement experiments with the X reranking experiment and identifying how intervention type, outcome measurement, duration, platform, and causal design account for divergent results. SQ3 is a CORE subquestion with no prior targeted search.

5 result(s) retrieved; 3 new unique source(s) added.

- **S11 — X's (Twitter's) algorithm can influence political polarisation**
  URL: https://sciencemediacentre.es/en/independent-research-shows-xs-twitters-algorithm-can-influence-political-polarisation
- **S12 — The political effects of X's feed algorithm**
  URL: https://www.nature.com/articles/s41586-026-10098-2
- **S13 — How Much has Social Media affected Polarization? | Tom Cunningham – Tom Cunningham**
  URL: https://tecunningham.github.io/posts/2023-07-27-meta-2020-elections-experiments.html

**Search Duration:** 2.90s

---

## 2. Evidence Processing

Evidence processing did not complete.

---

## 3. Ledger Updates

No ledger update was completed.

---

## 4. Current Research State

- Claims: 0
- Supported: 0
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 0

---

## 5. Research Decision

No research decision was completed for this iteration.

---

# Final Research Decision

**Research did not complete.**

**Failure Stage:** OpenAI Evidence Processing — Iteration 3

**Remaining Uncertainty**

- Evidence is insufficient to determine whether recommendation algorithms change political behavior, including participation, voting, sharing, or other offline and online political actions.
- The evidence base does not permit a reliable estimate of the average magnitude, duration, persistence, or cumulative population-level contribution of recommendation algorithms to polarization across platforms and political contexts.
- The supplied sources do not adequately compare platforms, recommendation objectives, user populations, political systems, or time periods, limiting explanation of when algorithmic exposure effects generalize.
- The materials do not provide enough methodological detail to assess uncertainty, attrition, sample representativeness, intervention compliance, or the full causal identification strategy of the reported X experiment.
- SQ1: What evidence shows that social-media recommendation algorithms change the political content, sources, viewpoints, or ideological diversity that users see or engage with? (CONFLICTING: At least one linked ledger claim contains conflicting evidence.)
- SQ2: What evidence shows that social-media recommendation algorithms change users’ political beliefs, attitudes, polarization, or political behavior? (CONFLICTING: At least one linked ledger claim contains conflicting evidence.)
- SQ3: Why does the literature reach different conclusions about the political effects of recommendation algorithms? (CONFLICTING: At least one linked ledger claim contains conflicting evidence.)
- SQ4: How should the overall contribution of recommendation algorithms to political polarization be characterized, given the distinction between changing exposure and changing beliefs or behavior? (CONFLICTING: At least one linked ledger claim contains conflicting evidence.)

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Question Decomposition | 1 | 7.74s |
| Tavily Search | 3 | 9.46s |
| Evidence Processing | 3 | 31.75s |
| Research Decision | 2 | 8.33s |
| Report Generation | 0 | 0.00s |
| Total Run | — | 73.53s |
