# Research Run Log

## Run Summary

**System Version:** evidence-ledger-v1

**Research Question**

To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions.

**Status:** Failed

**Failure Stage:** OpenAI Research Decision — Iteration 5

**Error**

1 validation error for ResearchDecision
  Value error, target_id must be provided for a claim or gap research target [type=value_error, input_value={'needs_more_research': T...: 'RESEARCH_CONTROLLER'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.13/v/value_error

**Search Provider:** Tavily

**Model:** gpt-4o-mini

**Searches Performed:** 5 / 10

**Unique Sources:** 15

**OpenAI Calls:** 10

**Tavily Calls:** 5

**Started:** 2026-09-01T11:35:08-04:00

**Ended:** 2026-09-01T11:35:53-04:00

**Total Runtime:** 44.60s

---

# Iteration 1

## 1. Search

**Query**

> To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions.

**Purpose:** GENERAL

**Why this query**

This is the user's original research question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S1 — The Role of Social Media Algorithms in Shaping Political Polarisation in the United States**
  URL: https://www.humanrightsresearch.org/post/the-role-of-social-media-algorithms-in-shaping-political-polarisation-in-the-united-states
- **S2 — How algorithmically curated online environments influence users’ political polarization: Results from two experiments with panel data**
  URL: https://www.sciencedirect.com/science/article/pii/S2451958823000763
- **S3 — Algorithms Shift Polarization. Why Does Policy Still Miss the Real Problem? | TechPolicy.Press**
  URL: https://techpolicy.press/algorithms-shift-polarization-why-does-policy-still-miss-the-real-problem
- **S4 — Op-ed: Social media algorithms & their effects on American politics - Fung Institute for Engineering Leadership**
  URL: https://funginstitute.berkeley.edu/news/op-ed-social-media-algorithms-their-effects-on-american-politics
- **S5 — Social Drivers and Algorithmic Mechanisms on Digital Media**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11373151

**Search Duration:** 0.56s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 0
- New gaps: 1
- Resolved gaps: 0

**Processing Duration:** 6.49s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

Social media algorithms contribute to political polarization by influencing the visibility of content and the formation of echo chambers.

- S1 supports (direct): The article discusses how algorithms control what users see, leading to polarization by reinforcing existing political beliefs.
- S2 supports (direct): Experiments show that exposure to like-minded political arguments leads to increased polarization, indicating algorithms influence user attitudes.
- S3 supports (direct): A study demonstrated that algorithmic ranking decisions can directly shape political attitudes and contribute to hostility.
- S4 supports (direct): Discussing the effects of social media algorithms, the op-ed highlights their role in creating echo chambers and political divides.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Gap G1

The extent to which algorithmic manipulation can be regulated effectively remains unknown.

---

## 4. Current Research State

- Claims: 1
- Supported: 1
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 1
- Remaining Searches: 9

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** GAP G1

**Why**

Need to explore the regulation of algorithmic manipulation, which is crucial for understanding the full impact on political polarization.

**Next Search**

> What regulatory measures have been proposed or implemented to mitigate the effects of social media algorithms on political polarization?


---

# Iteration 2

## 1. Search

**Query**

> What regulatory measures have been proposed or implemented to mitigate the effects of social media algorithms on political polarization?

**Target:** G1

**Purpose:** GENERAL

**Why this query**

Need to explore the regulation of algorithmic manipulation, which is crucial for understanding the full impact on political polarization.

5 result(s) retrieved; 4 new unique source(s) added.

- **S6 — Post-seminar reflection: The Role of Algorithms in Political Polarisation | Centre on Law and Social Transformation**
  URL: https://www.lawtransform.no/publication/post-seminar-reflection-the-role-of-algorithms-in-political-polarisation
- **S7 — How tech platforms fuel U.S. political polarization and what ...**
  URL: https://www.brookings.edu/articles/how-tech-platforms-fuel-u-s-political-polarization-and-what-government-can-do-about-it
- **S8 — Regulating Algorithmic Content Distribution and Moderation by Online Platforms - R Street Institute**
  URL: https://www.rstreet.org?post_type=research&p=95059
- **S9 — Social media research tool can reduce polarization**
  URL: https://www.washington.edu/news/2025/12/03/social-media-research-tool-can-reduce-polarization-it-could-also-lead-to-more-user-control-over-algorithms

**Search Duration:** 2.77s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 1
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 4.04s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Social media algorithms contribute to political polarization by influencing the visibility of content and the formation of echo chambers.

- S6 supports (direct): The article discusses how social media algorithms create echo chambers and filter bubbles that contribute to political polarization.
- S7 supports (direct): Research indicates that algorithms amplify content that drives political divides, fostering negative sentiments across opposing political views.
- S8 supports (direct): A study discusses the complexities of regulating algorithms that influence political discourse and how they contribute to polarization.
- S9 supports (direct): A new tool shows how reordering content can reduce polarization, demonstrating the influence of algorithms on user attitudes towards different political perspectives.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 1
- Supported: 1
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 1
- Remaining Searches: 8

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** GAP G1

**Why**

G1 addresses a significant gap regarding the regulation of algorithmic manipulation.

**Next Search**

> What are the most effective regulatory strategies proposed or implemented to manage the impact of social media algorithms on political polarization?


---

# Iteration 3

## 1. Search

**Query**

> What are the most effective regulatory strategies proposed or implemented to manage the impact of social media algorithms on political polarization?

**Target:** G1

**Purpose:** GENERAL

**Why this query**

G1 addresses a significant gap regarding the regulation of algorithmic manipulation.

5 result(s) retrieved; 1 new unique source(s) added.

- **S10 — The political effects of X's feed algorithm**
  URL: https://www.nature.com/articles/s41586-026-10098-2

**Search Duration:** 3.20s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 1
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 3.74s

---

## 3. Ledger Updates

### New Claim C2

**Claim**

Switching from a chronological to an algorithmic feed increases user engagement and shifts political opinion towards more conservative positions.

- S10 supports (direct): A field experiment found that users exposed to an algorithmic feed had increased engagement and more conservative political opinions compared to the chronological feed.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

Social media algorithms contribute to political polarization by influencing the visibility of content and the formation of echo chambers.

- S10 supports (direct): The article discusses the algorithm's influence on user engagement and political opinions, adding to the existing claim about algorithms contributing to polarization.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 2
- Supported: 2
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 1
- Remaining Searches: 7

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** GAP G1

**Why**

Regulating algorithmic manipulation is crucial to addressing political polarization, and no existing evidence clarifies effective strategies.

**Next Search**

> What recent studies or frameworks analyze effective regulatory strategies for managing the influence of social media algorithms on political polarization?


---

# Iteration 4

## 1. Search

**Query**

> What recent studies or frameworks analyze effective regulatory strategies for managing the influence of social media algorithms on political polarization?

**Target:** G1

**Purpose:** GENERAL

**Why this query**

Regulating algorithmic manipulation is crucial to addressing political polarization, and no existing evidence clarifies effective strategies.

5 result(s) retrieved; 2 new unique source(s) added.

- **S11 — Ranking for engagement: How social media algorithms fuel ...**
  URL: https://www.sciencedirect.com/science/article/pii/S0047272726000253
- **S12 — New research reveals algorithms' hidden political power**
  URL: https://news.northeastern.edu/2025/11/27/social-media-political-polarization-research

**Search Duration:** 2.57s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 2
- New gaps: 0
- Resolved gaps: 1

**Processing Duration:** 5.09s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Social media algorithms contribute to political polarization by influencing the visibility of content and the formation of echo chambers.

- S11 supports (direct): The study finds that social media algorithms amplify misinformation and polarization through engagement-driven ranking, indicating algorithmic influence on political content visibility.
- S12 supports (direct): Research shows that social media algorithms can shift partisan political feelings in a short time, demonstrating their significant impact on polarization.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

Switching from a chronological to an algorithmic feed increases user engagement and shifts political opinion towards more conservative positions.

- S12 supports (direct): The research found algorithmic alterations in users' feeds can shift political perceptions significantly in a week, which may suggest engagement changes lead to a shift towards conservatism.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Resolved Gap G1

The extent to which algorithmic manipulation can be regulated effectively remains unknown.

---

## 4. Current Research State

- Claims: 2
- Supported: 2
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 6

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C2

**Why**

The evidence supports claims about algorithms contributing to polarization but lacks exploration of how they impact political beliefs specifically. Investigating the influence of algorithmic feeds on belief shifts is crucial.

**Next Search**

> What recent studies explore the impact of social media algorithmic feeds on changing political beliefs or opinions among users, focusing on shifts towards conservatism?


---

# Iteration 5

## 1. Search

**Query**

> What recent studies explore the impact of social media algorithmic feeds on changing political beliefs or opinions among users, focusing on shifts towards conservatism?

**Target:** C2

**Purpose:** GENERAL

**Why this query**

The evidence supports claims about algorithms contributing to polarization but lacks exploration of how they impact political beliefs specifically. Investigating the influence of algorithmic feeds on belief shifts is crucial.

5 result(s) retrieved; 3 new unique source(s) added.

- **S13 — The algorithmic feed on X could be shifting political views toward conservatism**
  URL: https://www.scimex.org/newsfeed/the-algorithmic-feed-on-x-could-be-shifting-political-views-toward-conservatism
- **S14 — NEWS: Algorithm on X effects political views in the USA | unisg.ch**
  URL: https://www.unisg.ch/en/newsroom/algorithm-on-x-effects-political-views-in-the-usa
- **S15 — The political effects of X's feed algorithm. - Abstract**
  URL: https://pubmed.ncbi.nlm.nih.gov/41708846

**Search Duration:** 2.61s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 1
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 5.52s

---

## 3. Ledger Updates

### Updated Claim C2

**Claim**

Switching from a chronological to an algorithmic feed increases user engagement and shifts political opinion towards more conservative positions.

- S13 supports (direct): A recent experiment found that switching to the algorithmic feed led users to engage more and shift towards conservative political views, indicating an influence of algorithm on political opinion.
- S14 supports (direct): The study shows that users on the algorithmic feed adopted more conservative views related to political priorities and followed conservative activists, demonstrating the feed's impact on their opinions.
- S15 supports (direct): Research confirms that exposure to algorithmic content promotes conservative views and shifts political attitudes, even persisting after users switch to a chronological feed.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 2
- Supported: 2
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 5

---

## 5. Research Decision

No research decision was completed for this iteration.

---

# Final Research Decision

**Research did not complete.**

**Failure Stage:** OpenAI Research Decision — Iteration 5

**Remaining Uncertainty**

- Normal final synthesis did not complete, so the completeness of the evidence could not be confirmed.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 5 | 11.71s |
| Evidence Processing | 5 | 24.89s |
| Research Decision | 5 | 6.64s |
| Report Generation | 0 | 0.00s |
| Total Run | — | 44.60s |
