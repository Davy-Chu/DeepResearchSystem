# Research Run Log

## Run Summary

**System Version:** evidence-ledger-decomposer-verifier-v1

**Research Question**

To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 8

**OpenAI Calls:** 9

**Tavily Calls:** 3

**Verifier Model:** gpt-5.6-luna

**Started:** 2026-08-31T19:12:34-04:00

**Ended:** 2026-08-31T19:14:06-04:00

**Total Runtime:** 92.58s

---

# Research Plan

## Subquestions

### SQ1 [CORE]

**Question:**

What evidence shows that social-media recommendation algorithms change users’ exposure to political content, including the quantity, diversity, ideological slant, or source of what they see?

**Success criteria:**

Summarize credible empirical evidence identifying algorithmic recommendations as a cause of changes in political content exposure, distinguishing algorithmic effects from users’ own follows, searches, clicks, and choices where possible; report relevant populations, platforms, timeframes, and uncertainty.

**Initial status:** UNRESEARCHED

### SQ2 [CORE]

**Question:**

What evidence shows that algorithm-driven changes in political-content exposure alter users’ political beliefs, attitudes, affective polarization, or political behavior?

**Success criteria:**

Assess causal evidence linking recommendation algorithms—not merely social-media use or exposure in general—to changes in political beliefs or behavior, distinguishing null, positive, and negative effects and identifying the outcomes and time horizons studied.

**Initial status:** UNRESEARCHED

### SQ3 [CORE]

**Question:**

Why do studies reach different conclusions about the relationship between recommendation algorithms and political polarization?

**Success criteria:**

Compare explanations involving differing definitions and measures of polarization, platform and algorithm differences, user selection and behavior, experimental versus observational designs, intervention intensity, population and country context, study duration, and other methodological or contextual factors supported by the literature.

**Initial status:** UNRESEARCHED

### SQ4 [CORE]

**Question:**

How should the evidence be synthesized to characterize the extent of algorithms’ contribution to political polarization while preserving the distinction between exposure effects and belief or behavior effects?

**Success criteria:**

Develop a calibrated overall assessment that separates direct evidence of changed exposure from evidence of downstream attitude or behavior change, states the strength and limits of causal inference, and identifies where conclusions are robust, mixed, or unresolved.

**Initial status:** UNRESEARCHED

## Synthesis Requirements

- Maintain a clear causal chain distinction: recommendation algorithms changing what users see versus those exposure changes causing changes in political beliefs or behavior.
- Explain conflicting findings rather than treating them as interchangeable, accounting for differences in measures, methods, platforms, users, contexts, and timeframes.
- Assess the extent of contribution rather than making an all-or-nothing judgment, and communicate relevant uncertainty.

## Output Requirements

- Answer the question about social-media recommendation algorithms and political polarization.
- Present separate treatment of evidence on changes in users’ exposure and evidence on changes in political beliefs or behavior.
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

**Search Duration:** 0.72s

---

## 2. Evidence Processing

- New claim proposals: 5
- Existing claim updates: 0
- New gaps: 4
- Resolved gaps: 0

**Processing Duration:** 12.91s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

In two German quasi-experiments using a three-wave panel design, exposure to like-minded political arguments increased attitude and affective polarization more than exposure to opposing arguments; algorithmic selection did not generally amplify these exposure effects, although it produced a small additional attitude-polarization effect for one topic.

- S1 supports (direct): The study experimentally compared algorithmically selected with randomly selected like-minded or opposing arguments and reported stronger polarization after like-minded exposure, no general amplification by algorithmic selection, and a small direct effect for one topic.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C2

**Claim**

A browser-extension experiment on more than 1,200 U.S. X users during the 2024 presidential campaign found that reranking users’ existing feeds to increase or decrease exposure to antidemocratic attitudes and partisan animosity changed affective polarization after one week: increased exposure made evaluations of the opposing party approximately 2.48 points cooler and reduced exposure made them approximately 2.11 points warmer on a 100-point scale.

- S4 supports (direct): The article reports a randomized browser-extension intervention with 1,256 U.S. participants and opposing-party feeling changes of 2.48 degrees cooler under increased exposure and 2.11 degrees warmer under reduced exposure.
- S5 supports (indirect): The university report describes the same reranking experiment, its one-week duration, sample exceeding 1,200, and approximately two-point shifts in feelings toward the opposing party.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C3

**Claim**

The X reranking experiment changed the ordering and prominence of posts while leaving the followed accounts, the set of available posts, and the underlying content unchanged; thus it provides causal evidence that algorithmic ranking can alter political exposure without changing users’ networks or removing content.

- S5 supports (direct): The report states that the extension reranked posts in real time, did not remove content, and preserved the people users followed and the same available posts.
- S4 supports (indirect): The commentary says the intervention changed ranking while keeping content and users constant and reports different exposure to antidemocratic and partisan-animosity content.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C4

**Claim**

The supplied review characterizes algorithmic effects on polarization as non-straightforward and suggests that algorithms often reinforce pre-existing social drivers rather than operating independently of users’ preferences and broader social dynamics.

- S3 supports (direct): The review describes a feedback loop between algorithmic mechanisms and social drivers, states that the role of algorithms in polarization is far from straightforward, and says existing evidence suggests algorithms mostly reinforce existing social drivers.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C5

**Claim**

The available evidence supports a distinction between algorithm-caused changes in exposure or ranking and downstream polarization: direct experimental evidence in the supplied sources demonstrates both ranking changes and some affective or attitudinal changes, but does not establish effects on political behavior or durable belief change.

- S1 supports (direct): The panel experiments separate exposure to like-minded or opposing arguments from algorithmic versus random selection and measure attitude and affective polarization, finding limited direct algorithmic amplification.
- S5 supports (indirect): The X intervention manipulated feed ranking and measured short-term partisan feelings, not political behavior or long-term beliefs.
- S3 supports (indirect): The review emphasizes that the algorithm-polarization relationship is complex and requires further empirical research.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Gap G1

The supplied evidence does not adequately quantify how recommendation algorithms change the quantity, ideological diversity, source mix, or slant of ordinary users’ political exposure across major platforms, while separating algorithmic ranking from users’ follows, searches, clicks, and engagement.

### New Gap G2

No supplied source provides direct evidence about algorithm-driven changes in political behavior, such as voting, participation, sharing, contacting politicians, or offline political activity; durable belief change is also unresolved.

### New Gap G3

The causal attitude evidence is limited in the supplied material to short interventions and specific contexts: a German panel experiment and a one-week U.S. X reranking experiment during the 2024 campaign. Generalizability across platforms, countries, populations, political issues, and longer time horizons remains unresolved.

### New Gap G4

The supplied sources do not permit a systematic comparison of why observational, experimental, and quasi-experimental studies reach different conclusions, including differences in polarization definitions, outcome measures, intervention intensity, sample selection, and platform algorithms.

---

## 4. Current Research State

- Claims: 5
- Supported: 5
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 4
- Remaining Searches: 2

### Subquestion Progress

**SQ1:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ3:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ4:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

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

## 5. Independent Verification

### V1 — Claim C1

**Phase:** INITIAL

**Evidence source IDs:** S1

**Verdict:** VERIFIED

**Reason**

The supplied article abstract explicitly reports two quasi-experiments using a three-wave experimental panel survey, stronger attitude and affective-polarization effects from like-minded than opposing arguments, no general amplification by algorithmic selection, and a small direct attitude-polarization effect for one topic. The article metadata also identifies Germany. This supports the claim within the study’s limited two-topic experimental setting.

**Missing assumptions**

- The claim applies to the studied German sample, topics, simulated online environments, and study duration rather than to recommendation algorithms generally.
- The evidence concerns polarization outcomes, not political behavior or longer-term belief change beyond the measured panel period.

**Source concerns**

- Only the publisher page and abstract are supplied, so detailed sample, design, statistical uncertainty, and implementation limitations cannot be independently assessed from the saved evidence.
- No independent corroborating source is provided.

**Counter-search status:** NOT_REQUESTED

**Reconciliation**

Confidence: HIGH → HIGH

Status: SUPPORTED → SUPPORTED

---

## 6. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** SUBQUESTION SQ2

**Why**

A high-importance gap remains: the supplied evidence does not establish whether recommendation-driven exposure changes durable political beliefs or political behavior. Filling this gap would materially improve the required distinction between exposure effects and downstream consequences.

**Next Search**

> Causal empirical studies of social-media recommendation or feed-ranking algorithms changing political beliefs, affective polarization, voting, political participation, sharing, or offline behavior; prioritize randomized or quasi-experimental designs, long-term outcomes, and evidence from Facebook, YouTube, TikTok, and X.


---

# Iteration 2

## 1. Search

**Query**

> Causal empirical studies of social-media recommendation or feed-ranking algorithms changing political beliefs, affective polarization, voting, political participation, sharing, or offline behavior; prioritize randomized or quasi-experimental designs, long-term outcomes, and evidence from Facebook, YouTube, TikTok, and X.

**Target:** SQ2

**Purpose:** SUBQUESTION

**Why this query**

A high-importance gap remains: the supplied evidence does not establish whether recommendation-driven exposure changes durable political beliefs or political behavior. Filling this gap would materially improve the required distinction between exposure effects and downstream consequences.

5 result(s) retrieved; 2 new unique source(s) added.

- **S6 — How do social media feed algorithms affect attitudes and ...**
  URL: https://cdr.lib.unc.edu/downloads/wp9891401
- **S7 — Social media research tool can reduce polarization**
  URL: https://www.washington.edu/news/2025/12/03/social-media-research-tool-can-reduce-polarization-it-could-also-lead-to-more-user-control-over-algorithms

**Search Duration:** 2.71s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 4
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 12.18s

---

## 3. Ledger Updates

### New Claim C6

**Claim**

In a randomized 2020 U.S. election experiment on Facebook and Instagram, replacing default machine-learning feed ranking with reverse-chronological ordering substantially changed users’ on-platform experience and political-content exposure: it increased political and untrustworthy content on both platforms, decreased uncivil or slur-containing content on Facebook, and increased exposure to moderate friends and ideologically mixed sources on Facebook. Despite these exposure changes, it did not significantly change issue polarization, affective polarization, political knowledge, or other key attitudes during the three-month study.

- S6 supports (direct): The randomized experiment directly compared default algorithmic feeds with chronological feeds during the 2020 U.S. election and reported substantial changes in content exposure but null effects on polarization, political knowledge, and other key attitudes over three months.

**Confidence:** HIGH

**Status:** SUPPORTED

### Updated Claim C2

**Claim**

A browser-extension experiment on more than 1,200 U.S. X users during the 2024 presidential campaign found that reranking users’ existing feeds to increase or decrease exposure to antidemocratic attitudes and partisan animosity changed affective polarization after one week: increased exposure made evaluations of the opposing party approximately 2.48 points cooler and reduced exposure made them approximately 2.11 points warmer on a 100-point scale.

- S7 supports (indirect): The institutional report describes the same X feed-reranking intervention, involving about 1,200 volunteers during the 2024 election and seven-day upranking or downranking of antidemocratic and partisan-animosity content; downranking produced warmer views of the opposing party and upranking produced colder views.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C3

**Claim**

The X reranking experiment changed the ordering and prominence of posts while leaving the followed accounts, the set of available posts, and the underlying content unchanged; thus it provides causal evidence that algorithmic ranking can alter political exposure without changing users’ networks or removing content.

- S7 supports (indirect): The report states that the external web tool reordered X posts without removing them, placing posts containing antidemocratic attitudes and partisan animosity lower or higher in users’ feeds.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

The supplied review characterizes algorithmic effects on polarization as non-straightforward and suggests that algorithms often reinforce pre-existing social drivers rather than operating independently of users’ preferences and broader social dynamics.

- S6 supports (direct): The randomized Facebook and Instagram study found that substantially changing algorithmic ranking and political-content exposure did not significantly change polarization or other key attitudes over three months, illustrating that exposure effects need not translate into average attitude effects.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

The available evidence supports a distinction between algorithm-caused changes in exposure or ranking and downstream polarization: direct experimental evidence in the supplied sources demonstrates both ranking changes and some affective or attitudinal changes, but does not establish effects on political behavior or durable belief change.

- S6 supports (direct): The Facebook and Instagram experiment directly separated algorithmic ranking from users’ existing networks and measured both exposure and downstream political outcomes: ranking changed what users saw, but issue polarization, affective polarization, political knowledge, and other key attitudes did not significantly change during three months.
- S7 supports (indirect): The X reranking report describes a contrasting short-term result in which changing the prominence of antidemocratic and partisan-animosity content changed opposing-party evaluations, reinforcing that downstream effects vary by intervention and context.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 6
- Supported: 6
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 4
- Remaining Searches: 1

### Subquestion Progress

**SQ1:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ2:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ3:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

**SQ4:** PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → PARTIAL (targeted searches: 1)
- SQ3 → PARTIAL (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- None

**Remaining targeted searches:** 1

---

## 5. Independent Verification

### V2 — Claim C5

**Phase:** INITIAL

**Evidence source IDs:** S1, S5, S3, S6, S7

**Verdict:** NEEDS_QUALIFICATION

**Reason**

The supplied experiments support a causal distinction: changing feed ranking or selection changed users’ exposure, while some interventions also changed affective or attitudinal polarization. However, the evidence is short-term and platform- and outcome-specific; it does not establish durable belief change or political behavior effects. The wording should also acknowledge that one experiment changed on-platform activity, although not demonstrated political behavior.

**Missing assumptions**

- That the supplied sources are sufficient to characterize the broader available literature.
- That short experimental follow-ups can support a conclusion about the absence of durable effects; they primarily show that such effects were not established in these studies.
- That changes in on-platform activity do not count as political behavior.

**Source concerns**

- S5 and S7 are institutional news reports rather than the underlying peer-reviewed article, so their methodological detail is limited.
- The evidence covers a small set of interventions, mainly Facebook/Instagram and X, in the United States and Germany, over periods ranging from about one week to three months.
- The experiments manipulate ranking or selection, which establishes effects of those interventions but not necessarily the effects of every platform’s production recommendation system.

**Counter-search status:** EXECUTED

**Counter-search query:**

> Are there randomized or quasi-experimental studies showing that social-media recommendation or feed-ranking algorithms produce durable changes in political beliefs, voting, political participation, or other political behavior, including null findings and long-term follow-ups?

**Counter-search evidence:** S8

---

## 6. Research Decision

**Decision:** Continue researching.

**Origin:** VERIFIER_COUNTERSEARCH

**Target:** CLAIM C5

**Why**

Independent verification of C5 identified a high-value falsification search: The supplied experiments support a causal distinction: changing feed ranking or selection changed users’ exposure, while some interventions also changed affective or attitudinal polarization. However, the evidence is short-term and platform- and outcome-specific; it does not establish durable belief change or political behavior effects. The wording should also acknowledge that one experiment changed on-platform activity, although not demonstrated political behavior.

**Next Search**

> Are there randomized or quasi-experimental studies showing that social-media recommendation or feed-ranking algorithms produce durable changes in political beliefs, voting, political participation, or other political behavior, including null findings and long-term follow-ups?


---

# Iteration 3

## 1. Search

**Query**

> Are there randomized or quasi-experimental studies showing that social-media recommendation or feed-ranking algorithms produce durable changes in political beliefs, voting, political participation, or other political behavior, including null findings and long-term follow-ups?

**Target:** C5

**Purpose:** COUNTERSEARCH

**Why this query**

Independent verification of C5 identified a high-value falsification search: The supplied experiments support a causal distinction: changing feed ranking or selection changed users’ exposure, while some interventions also changed affective or attitudinal polarization. However, the evidence is short-term and platform- and outcome-specific; it does not establish durable belief change or political behavior effects. The wording should also acknowledge that one experiment changed on-platform activity, although not demonstrated political behavior.

5 result(s) retrieved; 1 new unique source(s) added.

- **S8 — New study shows just how Facebook's algorithm shapes politics : NPR**
  URL: https://www.npr.org/2023/07/27/1190383104/new-study-shows-just-how-facebooks-algorithm-shapes-conservative-and-liberal-bub

**Search Duration:** 2.68s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 2
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 9.40s

---

## 3. Ledger Updates

### New Claim C7

**Claim**

An observational analysis of approximately 208 million U.S. Facebook adults during September 2020–February 2021 found that liberals and conservatives consumed political news with limited overlap, and that ideological segregation increased across the stages from algorithmic selection to user exposure and then interaction. The analysis also found asymmetric engagement, with conservatives interacting with political news more often than liberals. These findings document differences in exposure and on-platform behavior but do not by themselves identify the causal effect of algorithmic ranking apart from users’ choices.

- S8 supports (direct): NPR reports that the study analyzed political-news links among 208 million U.S. Facebook adults, found little overlap between liberal and conservative news consumption, and observed increasing segregation from algorithm-selected content to content seen and interacted with by users. It also reports higher political-news engagement among conservatives.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C6

**Claim**

In a randomized 2020 U.S. election experiment on Facebook and Instagram, replacing default machine-learning feed ranking with reverse-chronological ordering substantially changed users’ on-platform experience and political-content exposure: it increased political and untrustworthy content on both platforms, decreased uncivil or slur-containing content on Facebook, and increased exposure to moderate friends and ideologically mixed sources on Facebook. Despite these exposure changes, it did not significantly change issue polarization, affective polarization, political knowledge, or other key attitudes during the three-month study.

- S8 supports (indirect): The NPR account independently describes the Facebook/Instagram research as showing that changing algorithmic systems substantially changes what users see, while also reporting observational evidence that political-news segregation increases between algorithmic selection, user exposure, and interaction. This adds evidence about ideological source separation but does not alter C6’s randomized findings on exposure and measured attitudes.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

The supplied evidence supports distinguishing algorithmic changes in feed ranking or content exposure from downstream political effects. Experiments show that altering ranking can substantially change what users see and how active they are on-platform, while some short-term interventions produced small changes in affective or attitudinal polarization. Other evidence, including the three-month Facebook/Instagram experiment, found no significant changes in key political attitudes. The supplied studies do not establish durable belief change or offline political behavior.

- S8 supports (indirect): The source distinguishes changes in what users see from downstream interaction: ideological segregation increased from algorithmic selection to exposure and interaction, but the report does not show that algorithmic ranking caused the later behavioral differences. This reinforces the need to separate exposure evidence from behavior effects.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 7
- Supported: 6
- Weak: 1
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 4
- Remaining Searches: 0

### Subquestion Progress

**SQ1:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ2:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ3:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

**SQ4:** PARTIAL

Reason: At least one linked ledger claim is not yet supported.

### Research Plan Status

**CORE:**

- SQ1 → PARTIAL (targeted searches: 0)
- SQ2 → PARTIAL (targeted searches: 1)
- SQ3 → PARTIAL (targeted searches: 0)
- SQ4 → PARTIAL (targeted searches: 0)

**SECONDARY:**

- None

**Remaining targeted searches:** 0

---

## 5. Independent Verification

### V3 — Claim C5

**Phase:** POST_COUNTERSEARCH

**Evidence source IDs:** S1, S5, S3, S6, S7, S8

**Verdict:** NEEDS_QUALIFICATION

**Reason**

The supplied evidence supports the exposure–outcome distinction. Randomized or quasi-experimental studies show that changing feed-ranking or selection changes users’ content exposure and on-platform activity, while S1 and the reported X-feed experiment find some short-term changes in affective or attitudinal polarization. However, the evidence is platform-, intervention-, topic-, and time-specific, and S6 found no significant changes in issue or affective polarization, knowledge, or other key attitudes over three months. The evidence therefore does not establish durable belief change or offline political behavior, but the claim should explicitly describe the downstream findings as limited and mixed rather than implying a general experimental demonstration.

**Missing assumptions**

- The short-term attitude effects reported in S1 and the X-feed reranking study generalize beyond the studied topics, recruited samples, platforms, and election contexts.
- Changes in feed ranking are being treated as evidence about recommendation algorithms, although some interventions replaced the platform ranking system or used researcher-designed reranking rules rather than testing naturally occurring platform changes.
- The absence of measured effects over three months in S6 is not evidence that longer-term effects or unmeasured political behaviors do not occur.

**Source concerns**

- The strongest positive X-feed evidence is supplied through university news coverage rather than the primary Science article, so details about design, estimation, attrition, and outcome measurement cannot be independently assessed from the supplied text.
- S1 describes two quasi-experiments and reports a small direct attitude effect for only one topic, limiting broad generalization.
- The evidence set contains relatively few studies and is concentrated in U.S. 2020/2024 election settings and one German study.

**Counter-search status:** NOT_REQUESTED

**Reconciliation**

Claim:

"The available evidence supports a distinction between algorithm-caused changes in exposure or ranking and downstream polarization: direct experimental evidence in the supplied sources demonstrates both ranking changes and some affective or attitudinal changes, but does not establish effects on political behavior or durable belief change."
→
"The supplied evidence supports distinguishing algorithmic changes in feed ranking or content exposure from downstream political effects. Experiments show that altering ranking can substantially change what users see and how active they are on-platform, while some short-term interventions produced small changes in affective or attitudinal polarization. Other evidence, including the three-month Facebook/Instagram experiment, found no significant changes in key political attitudes. The supplied studies do not establish durable belief change or offline political behavior."

Confidence: HIGH → HIGH

Status: SUPPORTED → WEAK

---

## 6. Research Decision

**Decision:** Stop researching.

**Origin:** BUDGET_STOP

**Why**

The maximum research iteration budget was reached.

**Stop Reason:** max_iterations


---

# Final Research Decision

**Stop Reason:** max_iterations

**Remaining Uncertainty**

- The supplied evidence does not adequately quantify changes in the quantity, ideological diversity, source mix, or slant of ordinary users’ political exposure across major platforms while separating algorithmic ranking from users’ own choices.
- No supplied source directly examines algorithm-driven effects on voting, political participation, contacting politicians, or other offline political behavior; durable belief change remains unresolved.
- Causal attitude evidence is limited to short interventions and specific contexts, especially a German panel study and a one-week U.S. X experiment; generalizability across platforms, countries, populations, issues, and longer time horizons is unresolved.
- The supplied sources do not permit a systematic comparison of polarization definitions, outcome measures, intervention intensity, sample selection, and platform algorithms across observational, experimental, and quasi-experimental studies.
- The research process stopped because of the maximum-iteration limit. The counter-search for durable beliefs and political behavior produced S8, but that source added observational exposure and engagement evidence rather than resolving the behavioral gap.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Question Decomposition | 1 | 6.54s |
| Tavily Search | 3 | 6.11s |
| Evidence Processing | 3 | 34.50s |
| Independent Verification | 3 | 26.16s |
| Research Decision | 1 | 2.63s |
| Report Generation | 1 | 16.62s |
| Total Run | — | 92.58s |

# Verifier Diagnostics

- Verification calls: 3
- Claims verified: 2
- VERIFIED verdicts: 1
- NEEDS_QUALIFICATION verdicts: 2
- CONTRADICTED verdicts: 0
- INSUFFICIENT_EVIDENCE verdicts: 0
- Counter-searches requested: 1
- Counter-searches executed: 1
- Counter-searches blocked by budget: 0
- Counter-searches blocked as duplicates: 0
- Claims whose wording changed: 1
- Claims whose confidence decreased: 0
- Claims whose status changed: 1
- Searches allocated to general research: 1
- Searches allocated to subquestions: 1
- Searches allocated to counter-search: 1
