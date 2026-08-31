# Research Run Log

## Run Summary

**System Version:** evidence-ledger-v1

**Research Question**

To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 11

**OpenAI Calls:** 6

**Tavily Calls:** 3

**Started:** 2026-08-31T17:42:57-04:00

**Ended:** 2026-08-31T17:44:10-04:00

**Total Runtime:** 72.78s

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

**Search Duration:** 3.45s

---

## 2. Evidence Processing

- New claim proposals: 5
- Existing claim updates: 0
- New gaps: 3
- Resolved gaps: 0

**Processing Duration:** 18.89s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

Recommendation and ranking algorithms can change the political content users see or encounter first, including by selecting among posts or changing their ordering while leaving the underlying pool of followed accounts and available posts unchanged.

- S1 supports (direct): The experiments compared algorithmically selected with randomly selected political arguments, directly manipulating curation and exposure.
- S5 supports (direct): The browser-extension experiment reranked posts in users’ X feeds in real time; the same posts remained available, but their order was controlled by the intervention.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C2

**Claim**

Evidence that algorithmic curation changes political attitudes or polarization is positive but modest and context-dependent: like-minded exposure increases attitude and affective polarization, while algorithmic selection does not necessarily amplify the effect of that exposure and produced only a slight additional attitude-polarization effect for one topic.

- S1 supports (direct): Across two quasi-experiments, like-minded arguments increased attitude and affective polarization more than opposing arguments; algorithmic selection did not amplify these exposure effects, though it produced a slightly stronger attitude-polarization effect for one topic.
- S4 supports (indirect): A reported browser-extension experiment on X found that increasing exposure to antidemocratic and partisan-animosity content cooled feelings toward the opposing party by 2.48 points, while reducing exposure warmed them by 2.11 points after one week.
- S5 supports (indirect): A university report on the same X reranking experiment describes approximately two-point shifts in feelings toward the opposing party after one week.
- S1 contradicts (direct): The study found no amplification of like-minded-content effects by algorithmic selection and only a small direct effect for one topic, qualifying stronger general claims about algorithmic polarization.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C3

**Claim**

The literature reaches different conclusions partly because algorithms and user-driven selective exposure are difficult to disentangle: users’ preferences and engagement shape what algorithms recommend, while algorithmic curation can in turn reinforce those existing social drivers.

- S1 supports (direct): The study explicitly identifies failure to separate individual exposure to like-minded content from effects caused by algorithms as a reason prior causal evidence was inconsistent.
- S3 supports (direct): The review describes a feedback loop between social drivers and algorithmic mechanisms and concludes that algorithms mostly reinforce existing social drivers; it characterizes effects on polarization as far from straightforward.
- S2 supports (indirect): The article describes recommendations as based on likes, shares, comments, watch time, follows, searches, and prior engagement, and emphasizes interaction between platform architecture and user behavior.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C4

**Claim**

Some experimental evidence indicates that algorithmic ranking can shift affective political feelings without users consciously noticing the intervention.

- S4 supports (indirect): The reported X experiment found that 74% of participants noticed no impact on their experience despite changes in exposure and measurable shifts in partisan feelings.
- S5 supports (indirect): The report states that participants generally could not notice the reranking and that the intervention changed only the order in which existing posts appeared.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C5

**Claim**

The supplied evidence does not establish whether recommendation algorithms produce durable changes in political behavior, such as voting, participation, sharing, following, or offline political action.

- No new evidence relationship was added.

**Confidence:** HIGH

**Status:** INSUFFICIENT_EVIDENCE

### New Gap G1

Evidence is insufficient on whether algorithm-induced changes in exposure or affective attitudes translate into political behavior, including voting, participation, political sharing, or offline action.

### New Gap G2

The durability and real-world scale of the observed attitude and affective-polarization effects remain unresolved: the supplied experiments examine short interventions and specific topics or X-feed manipulations, not long-term population-level outcomes.

### New Gap G3

The supplied sources do not permit a systematic comparison across platforms, countries, demographic groups, or recommendation designs, so the extent to which the findings generalize beyond the studied settings is unresolved.

---

## 4. Current Research State

- Claims: 5
- Supported: 4
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 1
- Open Gaps: 3
- Remaining Searches: 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** GAP G1

**Why**

High-value gap: the evidence does not show whether algorithmic exposure changes political behavior beyond short-term attitudes and affect.

**Next Search**

> Do social-media recommendation algorithms causally change political behavior? Find experimental or quasi-experimental evidence on voting, political participation, sharing, following, or offline political action, distinguishing exposure effects from attitude effects.


---

# Iteration 2

## 1. Search

**Query**

> Do social-media recommendation algorithms causally change political behavior? Find experimental or quasi-experimental evidence on voting, political participation, sharing, following, or offline political action, distinguishing exposure effects from attitude effects.

**Target:** G1

**Purpose:** GENERAL

**Why this query**

High-value gap: the evidence does not show whether algorithmic exposure changes political behavior beyond short-term attitudes and affect.

5 result(s) retrieved; 4 new unique source(s) added.

- **S6 — How do social media feed algorithms affect attitudes and ...**
  URL: https://cdr.lib.unc.edu/downloads/wp9891401
- **S7 — How Social Media Algorithms Shape Offline Civic Participation: A Framework of Social Psychological Processes**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12421319
- **S8 — First Findings Shed Light on Role of Social Media Algorithms ...**
  URL: https://moody.utexas.edu/news/socialmediainelections
- **S9 — How do social media feed algorithms affect attitudes and behavior in an election campaign? | Institute for Data, Democracy & Politics (IDDP) | Columbian College of Arts & Sciences | The George Washington University**
  URL: https://iddp.gwu.edu/how-do-social-media-feed-algorithms-affect-attitudes-and-behavior-election-campaign

**Search Duration:** 3.31s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 4
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 14.33s

---

## 3. Ledger Updates

### New Claim C6

**Claim**

In a randomized 2020 U.S. election experiment on Facebook and Instagram, replacing default feed-ranking algorithms with reverse-chronological feeds substantially changed users’ on-platform exposure, time spent, and activity, but did not significantly change measured political attitudes during the three-month study period.

- S6 supports (direct): The randomized experiment reports substantial changes in time spent, activity, and exposure to political, untrustworthy, uncivil, slur-containing, moderate, and ideologically mixed content, but no significant changes in issue polarization, affective polarization, political knowledge, or other key attitudes over three months.
- S9 supports (indirect): The institutional summary reports the same experiment’s changes in on-platform experience and its null effects on issue polarization, affective polarization, political knowledge, and other key attitudes.
- S8 supports (indirect): The university summary states that algorithm adjustments significantly changed what participants saw and their platform engagement but did not notably affect attitudes or off-platform behaviors during the three-month intervention.

**Confidence:** HIGH

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

Recommendation and ranking algorithms can change the political content users see or encounter first, including by selecting among posts or changing their ordering while leaving the underlying pool of followed accounts and available posts unchanged.

- S6 supports (direct): The Facebook/Instagram randomized experiment changed the amount and type of political content users encountered, including political, untrustworthy, uncivil, slur-containing, moderate, and ideologically mixed content, by replacing algorithmic ranking with chronological ordering.
- S9 supports (indirect): The summary reports substantial exposure changes after users were moved from default algorithmic feeds to reverse-chronological feeds.
- S8 supports (indirect): The university summary characterizes the algorithms as highly influential in shaping what users saw and their on-platform experiences.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

Evidence that algorithmic curation changes political attitudes or polarization is positive but modest and context-dependent: like-minded exposure increases attitude and affective polarization, while algorithmic selection does not necessarily amplify the effect of that exposure and produced only a slight additional attitude-polarization effect for one topic.

- S6 contradicts (direct): In the randomized Facebook/Instagram experiment, substantial algorithm-induced changes in exposure did not significantly alter issue polarization, affective polarization, political knowledge, or other key attitudes over three months.
- S8 contradicts (indirect): The summary reports that three-month algorithm modifications changed exposure and engagement but did not notably affect attitudes or off-platform behaviors.
- S9 contradicts (indirect): The institutional summary reports substantial on-platform changes but no significant changes in issue polarization, affective polarization, political knowledge, or other key attitudes during the three-month study.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C3

**Claim**

The literature reaches different conclusions partly because algorithms and user-driven selective exposure are difficult to disentangle: users’ preferences and engagement shape what algorithms recommend, while algorithmic curation can in turn reinforce those existing social drivers.

- S6 supports (direct): The study notes that ranking effects are personalized using past behavior and predictions from similar users, and that users’ choices and network composition are alternative determinants of what they see, complicating attribution to the ranking algorithm alone.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

The supplied evidence does not establish whether recommendation algorithms produce durable changes in political behavior, such as voting, participation, sharing, following, or offline political action.

- S8 supports (indirect): The summary reports that three-month algorithm modifications did not notably affect participants’ off-platform behaviors, although it does not establish effects for all forms of political behavior or longer periods.

**Confidence:** HIGH → HIGH

**Status:** INSUFFICIENT_EVIDENCE → INSUFFICIENT_EVIDENCE

---

## 4. Current Research State

- Claims: 6
- Supported: 5
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 1
- Open Gaps: 3
- Remaining Searches: 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** GAP G1

**Why**

Durable political behavior is a high-importance unresolved gap central to the question; one focused search remains.

**Next Search**

> social media recommendation algorithm randomized experiment political behavior voting participation sharing following offline action causal evidence


---

# Iteration 3

## 1. Search

**Query**

> social media recommendation algorithm randomized experiment political behavior voting participation sharing following offline action causal evidence

**Target:** G1

**Purpose:** GENERAL

**Why this query**

Durable political behavior is a high-importance unresolved gap central to the question; one focused search remains.

5 result(s) retrieved; 2 new unique source(s) added.

- **S10 — [PDF] How Social Media Algorithms Shape Offline Civic Participation**
  URL: https://socialactionlab.org/wp-content/uploads/2024/01/Jung-Dai-and-Albarracin-2023.pdf
- **S11 — Frontiers | Social media and the democratization of political participation: a global perspective**
  URL: https://www.frontiersin.org/journals/political-science/articles/10.3389/fpos.2026.1719957/full

**Search Duration:** 2.64s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 1
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 8.74s

---

## 3. Ledger Updates

### Updated Claim C5

**Claim**

The supplied evidence does not establish whether recommendation algorithms produce durable changes in political behavior, such as voting, participation, sharing, following, or offline political action.

- S10 supports (direct): The review states that most evidence linking social-media use to offline civic participation is correlational, preventing causal inference, and presents algorithmic pathways to offline participation as theoretical mechanisms and questions for future research rather than established causal findings.
- S11 supports (indirect): The cross-national study reports associations between social-media use and online political participation, but its survey design does not isolate recommendation algorithms or establish that algorithms cause political behavior.

**Confidence:** HIGH → HIGH

**Status:** INSUFFICIENT_EVIDENCE → INSUFFICIENT_EVIDENCE

---

## 4. Current Research State

- Claims: 6
- Supported: 5
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 1
- Open Gaps: 3
- Remaining Searches: 0

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

- Whether algorithm-induced exposure changes or affective-attitude shifts translate into voting, political participation, sharing, following, or offline political action remains unresolved.
- The durability and population-level scale of observed attitude and affective-polarization effects remain unresolved because the supplied experiments examine short interventions or bounded study periods rather than long-term outcomes.
- The supplied evidence does not permit systematic comparison across platforms, countries, demographic groups, or recommendation designs, so generalizability beyond the studied settings remains unresolved.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 9.40s |
| Evidence Processing | 3 | 41.95s |
| Research Decision | 2 | 4.47s |
| Report Generation | 1 | 16.95s |
| Total Run | — | 72.78s |
