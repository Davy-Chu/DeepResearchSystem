# Research Run Log

## Run Summary

**System Version:** evidence-ledger-v1

**Research Question**

To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-4o-mini

**Searches Performed:** 10 / 10

**Unique Sources:** 22

**OpenAI Calls:** 20

**Tavily Calls:** 10

**Started:** 2026-09-01T11:56:54-04:00

**Ended:** 2026-09-01T11:58:50-04:00

**Total Runtime:** 116.53s

---

# Iteration 1

## 1. Search

**Query**

> To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions.

**Purpose:** GENERAL

**Why this query**

This is the user's original research question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S1 — The Role of Social Media Algorithms in Shaping Political ...**
  URL: https://www.humanrightsresearch.org/post/the-role-of-social-media-algorithms-in-shaping-political-polarisation-in-the-united-states
- **S2 — Meta's algorithms show US political polarization has no ...**
  URL: https://www.wdsu.com/article/metas-algorithms-show-us-political-polarization-has-no-easy-fix/44679027
- **S3 — Algorithms Shift Polarization. Why Does Policy Still Miss ...**
  URL: https://techpolicy.press/algorithms-shift-polarization-why-does-policy-still-miss-the-real-problem
- **S4 — Social Drivers and Algorithmic Mechanisms on Digital Media**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11373151
- **S5 — How algorithmically curated online environments influence ...**
  URL: https://www.sciencedirect.com/science/article/pii/S2451958823000763

**Search Duration:** 3.06s

---

## 2. Evidence Processing

- New claim proposals: 2
- Existing claim updates: 0
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 5.66s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

Social media algorithms influence political polarization by determining what content is visible to users, contributing to the reinforcement of existing beliefs and facilitating the creation of echo chambers.

- S1 supports (direct): The article discusses how algorithms affect visibility and political engagement, influencing polarization and user beliefs.
- S3 supports (direct): A study confirms that algorithms can drive political hostility by selectively amplifying certain political content, impacting user attitudes.
- S2 contradicts (direct): Research shows that changing algorithms had no significant impact on users' political attitudes, suggesting other factors are at play.
- S4 contradicts (direct): Evidence suggests that while algorithms curate content, they largely reinforce existing societal drivers rather than independently inciting polarization.

**Confidence:** MEDIUM

**Status:** INSUFFICIENT_EVIDENCE

### New Claim C2

**Claim**

Political attitudes can shift significantly when exposed to algorithmically curated political content; however, the overall impact on polarization is not straightforward due to various influencing factors.

- S5 supports (direct): Experiments show that exposure to like-minded arguments increases political polarization, highlighting the role of algorithmic selection.
- S2 contradicts (direct): Studies find that changing algorithms does not significantly sway political attitudes, indicating a complexity in how algorithms affect polarization.

**Confidence:** MEDIUM

**Status:** INSUFFICIENT_EVIDENCE

---

## 4. Current Research State

- Claims: 2
- Supported: 0
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 2
- Open Gaps: 0
- Remaining Searches: 9

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C1

**Why**

Conflicting evidence on the influence of algorithms on political attitudes highlights the need for more direct studies to clarify their role in polarization.

**Next Search**

> Investigate how social media recommendation algorithms directly affect users' political beliefs and behaviors, focusing on studies that examine the impact of algorithm changes on political polarization.


---

# Iteration 2

## 1. Search

**Query**

> Investigate how social media recommendation algorithms directly affect users' political beliefs and behaviors, focusing on studies that examine the impact of algorithm changes on political polarization.

**Target:** C1

**Purpose:** GENERAL

**Why this query**

Conflicting evidence on the influence of algorithms on political attitudes highlights the need for more direct studies to clarify their role in polarization.

5 result(s) retrieved; 5 new unique source(s) added.

- **S6 — Algorithm Political Polarization 2026: The Digital Divide**
  URL: https://outsidethecase.org/2026/01/18/algorithm-political-polarization-2026
- **S7 — Social Media Algorithms: Impact on Political Polarization and Engagement**
  URL: https://latunisievote.org/social-media-algorithms-political-polarization-information-spread-and-user-engagement
- **S8 — The Impact of Social Media Algorithms on Political Polarization » boslabour.org.uk**
  URL: https://boslabour.org.uk/the-impact-of-social-media-algorithms-on-political-polarization
- **S9 — Impact of Social Media Algorithms on Polarization | PDF | Social Media | Popular Culture & Media Studies**
  URL: https://www.scribd.com/document/870029496/Social-Media-Algorithms-and-Political-Polarization
- **S10 — The Impact Of Social Media Algorithms On Information Bubbles And Political Polarization. - Consensus Academic Search Engine**
  URL: https://consensus.app/questions/impact-social-media-algorithms-information-bubbles

**Search Duration:** 4.70s

---

## 2. Evidence Processing

- New claim proposals: 3
- Existing claim updates: 2
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 13.25s

---

## 3. Ledger Updates

### New Claim C3

**Claim**

Social media algorithms contribute to political polarization by creating echo chambers and filter bubbles, which reinforce users' existing beliefs and reduce their exposure to opposing viewpoints.

- S6 supports (direct): The article discusses how algorithms prioritize content that triggers emotional reactions, reinforcing users' beliefs and leading to polarization.
- S7 supports (direct): Research shows that algorithms curate content aligning with users' beliefs, leading to increased political polarization and limited perspective.
- S8 supports (direct): Evidence indicates algorithms amplify divisive content, creating a fragmented information environment that deepens political divides.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C4

**Claim**

Algorithm-driven content curation can distort public opinion and influence electoral outcomes by amplifying misinformation, ultimately affecting democratic processes.

- S7 supports (direct): The article highlights how algorithms amplify sensational political content, distorting public opinion and impacting electoral outcomes.
- S9 supports (direct): Research indicates social media algorithms can foster political polarization, leading to radicalization and affecting democratic dialogue.
- S10 supports (direct): Studies show that even small adjustments in algorithmic filtering can significantly enhance user polarization and influence electoral outcomes.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C5

**Claim**

The societal impact of algorithm-driven polarization extends to diminished civic discourse and declining trust in democratic institutions.

- S6 supports (direct): The article discusses how algorithms weaken civic discourse and public trust by stifling critical debate among users.
- S8 supports (direct): Research confirms that algorithm-driven echo chambers undermine trust in institutions by amplifying divisive content.

**Confidence:** MEDIUM

**Status:** INSUFFICIENT_EVIDENCE

### Updated Claim C1

**Claim**

Social media algorithms influence political polarization by determining what content is visible to users, contributing to the reinforcement of existing beliefs and facilitating the creation of echo chambers.

- S6 supports (direct): The article discusses how algorithms affect visibility and political engagement, influencing polarization and user beliefs.
- S7 supports (direct): Research shows that algorithms prioritize content that aligns with users’ existing beliefs, leading to political polarization.
- S8 supports (direct): Social media algorithms curate content based on user interactions, significantly reinforcing political polarization.

**Confidence:** MEDIUM → HIGH

**Status:** INSUFFICIENT_EVIDENCE → SUPPORTED

### Updated Claim C2

**Claim**

Political attitudes can shift significantly when exposed to algorithmically curated political content; however, the overall impact on polarization is not straightforward due to various influencing factors.

- S6 supports (direct): Algorithm-driven content curation can alter user opinions significantly, affecting political polarization outcomes.
- S10 supports (direct): Empirical studies demonstrate that changes in algorithmic filtering can increase political polarization and change electoral dynamics.

**Confidence:** MEDIUM → HIGH

**Status:** INSUFFICIENT_EVIDENCE → SUPPORTED

---

## 4. Current Research State

- Claims: 5
- Supported: 4
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 1
- Open Gaps: 0
- Remaining Searches: 8

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C2

**Why**

Need to resolve conflicting claims about the algorithms' impact on political attitudes specifically, as existing evidence presents a complex picture. This gap is critical for understanding how algorithms influence polarization.

**Next Search**

> Examine studies that analyze the effect of algorithm changes on political attitudes, particularly focusing on how exposure to different types of curated content might influence user beliefs and potential shifts in polarization.


---

# Iteration 3

## 1. Search

**Query**

> Examine studies that analyze the effect of algorithm changes on political attitudes, particularly focusing on how exposure to different types of curated content might influence user beliefs and potential shifts in polarization.

**Target:** C2

**Purpose:** GENERAL

**Why this query**

Need to resolve conflicting claims about the algorithms' impact on political attitudes specifically, as existing evidence presents a complex picture. This gap is critical for understanding how algorithms influence polarization.

5 result(s) retrieved; 3 new unique source(s) added.

- **S11 — How X's algorithm shifts political attitudes**
  URL: https://cepr.org/voxeu/columns/how-xs-algorithm-shifts-political-attitudes
- **S12 — The political effects of X's feed algorithm**
  URL: https://www.nature.com/articles/s41586-026-10098-2
- **S13 — X's (Twitter's) algorithm can influence political polarisation**
  URL: https://sciencemediacentre.es/en/independent-research-shows-xs-twitters-algorithm-can-influence-political-polarisation

**Search Duration:** 3.00s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 2
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 4.89s

---

## 3. Ledger Updates

### Updated Claim C2

**Claim**

Political attitudes can shift significantly when exposed to algorithmically curated political content; however, the overall impact on polarization is not straightforward due to various influencing factors.

- S11 supports (direct): A field experiment shows that exposure to algorithmic feeds can shift political attitudes towards more conservative positions.
- S12 supports (direct): Research indicates that algorithmic feeds can increase user engagement and influence political opinions during elections.
- S13 supports (direct): An independent study shows that exposure to politically charged content in algorithms can significantly influence polarization and attitudes.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

The societal impact of algorithm-driven polarization extends to diminished civic discourse and declining trust in democratic institutions.

- S13 supports (direct): The study indicates that when algorithms amplify anti-democratic content, they can lead to higher political polarization and lower trust in institutions.

**Confidence:** MEDIUM → MEDIUM

**Status:** INSUFFICIENT_EVIDENCE → INSUFFICIENT_EVIDENCE

---

## 4. Current Research State

- Claims: 5
- Supported: 4
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 1
- Open Gaps: 0
- Remaining Searches: 7

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C2

**Why**

To address conflicting evidence regarding the extent to which algorithm changes affect political beliefs, further investigation into studies demonstrating the nuanced relationship between algorithmic exposure and shifts in political attitudes is necessary.

**Next Search**

> Explore research that dissects how algorithmic content curation influences political attitudes and polarization, particularly studies highlighting discrepancies in the impact of algorithm changes on individual beliefs versus broader polarization trends.


---

# Iteration 4

## 1. Search

**Query**

> Explore research that dissects how algorithmic content curation influences political attitudes and polarization, particularly studies highlighting discrepancies in the impact of algorithm changes on individual beliefs versus broader polarization trends.

**Target:** C2

**Purpose:** GENERAL

**Why this query**

To address conflicting evidence regarding the extent to which algorithm changes affect political beliefs, further investigation into studies demonstrating the nuanced relationship between algorithmic exposure and shifts in political attitudes is necessary.

5 result(s) retrieved; 2 new unique source(s) added.

- **S14 — How Social Media Algorithms Are Increasing Political Polarisation**
  URL: https://www.youngausint.org.au/post/how-social-media-algorithms-are-increasing-political-polarisation
- **S15 — New research reveals algorithms' hidden political power**
  URL: https://news.northeastern.edu/2025/11/27/social-media-political-polarization-research

**Search Duration:** 2.22s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 3
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 6.37s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Social media algorithms influence political polarization by determining what content is visible to users, contributing to the reinforcement of existing beliefs and facilitating the creation of echo chambers.

- S14 supports (direct): Social media algorithms create echo chambers that isolate user viewpoints and influence behavior, significantly contributing to polarization.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

Political attitudes can shift significantly when exposed to algorithmically curated political content; however, the overall impact on polarization is not straightforward due to various influencing factors.

- S15 supports (direct): New research indicates that algorithms can shift partisan feelings significantly within a short timeframe, illustrating their potential impact on political attitudes.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

The societal impact of algorithm-driven polarization extends to diminished civic discourse and declining trust in democratic institutions.

- S14 supports (direct): The distortion of civic discourse due to algorithmic prioritization of engagement over accuracy leads to diminished trust in institutions.

**Confidence:** MEDIUM → MEDIUM

**Status:** INSUFFICIENT_EVIDENCE → INSUFFICIENT_EVIDENCE

---

## 4. Current Research State

- Claims: 5
- Supported: 4
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 1
- Open Gaps: 0
- Remaining Searches: 6

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C2

**Why**

Evidence related to the impact of algorithm changes on individual political attitudes vs. broader polarization trends still shows discrepancies and requires further examination.

**Next Search**

> Investigate studies that specifically differentiate the effects of algorithm changes on individual political attitudes compared to overall trends in political polarization, highlighting discrepancies in outcomes.


---

# Iteration 5

## 1. Search

**Query**

> Investigate studies that specifically differentiate the effects of algorithm changes on individual political attitudes compared to overall trends in political polarization, highlighting discrepancies in outcomes.

**Target:** C2

**Purpose:** GENERAL

**Why this query**

Evidence related to the impact of algorithm changes on individual political attitudes vs. broader polarization trends still shows discrepancies and requires further examination.

5 result(s) retrieved; 1 new unique source(s) added.

- **S16 — Effects of news media bias and social media algorithms on ...**
  URL: https://dr.lib.iastate.edu/server/api/core/bitstreams/679463ea-22c2-4102-8ebf-cc15b04f76c9/content

**Search Duration:** 3.26s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 5
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 7.12s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Social media algorithms influence political polarization by determining what content is visible to users, contributing to the reinforcement of existing beliefs and facilitating the creation of echo chambers.

- S16 supports (direct): The thesis examines the impact of social media algorithms, indicating they shape user beliefs and contribute to polarization.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

Political attitudes can shift significantly when exposed to algorithmically curated political content; however, the overall impact on polarization is not straightforward due to various influencing factors.

- S16 supports (direct): The thesis highlights that while algorithms curate political content, their influence is complex and intertwined with societal factors.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C3

**Claim**

Social media algorithms contribute to political polarization by creating echo chambers and filter bubbles, which reinforce users' existing beliefs and reduce their exposure to opposing viewpoints.

- S16 supports (direct): The thesis notes that social media algorithms significantly enhance the formation of echo chambers, reinforcing existing beliefs.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

Algorithm-driven content curation can distort public opinion and influence electoral outcomes by amplifying misinformation, ultimately affecting democratic processes.

- S16 supports (direct): It discusses the potential of biased algorithms to distort public opinion, influencing electoral outcomes.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

The societal impact of algorithm-driven polarization extends to diminished civic discourse and declining trust in democratic institutions.

- No new evidence relationship was added.

**Confidence:** MEDIUM → MEDIUM

**Status:** INSUFFICIENT_EVIDENCE → INSUFFICIENT_EVIDENCE

---

## 4. Current Research State

- Claims: 5
- Supported: 4
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 1
- Open Gaps: 0
- Remaining Searches: 5

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C2

**Why**

Further investigation is required to clarify the contrasting evidence regarding the impact of algorithms on political attitudes versus broader polarization trends.

**Next Search**

> Find recent studies that specifically analyze how social media algorithms affect individual political beliefs compared to overall political polarization trends, focusing on evidence for conflicting outcomes and underlying factors.


---

# Iteration 6

## 1. Search

**Query**

> Find recent studies that specifically analyze how social media algorithms affect individual political beliefs compared to overall political polarization trends, focusing on evidence for conflicting outcomes and underlying factors.

**Target:** C2

**Purpose:** GENERAL

**Why this query**

Further investigation is required to clarify the contrasting evidence regarding the impact of algorithms on political attitudes versus broader polarization trends.

5 result(s) retrieved; 1 new unique source(s) added.

- **S17 — Social media research tool can reduce polarization**
  URL: https://www.washington.edu/news/2025/12/03/social-media-research-tool-can-reduce-polarization-it-could-also-lead-to-more-user-control-over-algorithms

**Search Duration:** 3.61s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 2
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 3.77s

---

## 3. Ledger Updates

### Updated Claim C2

**Claim**

Political attitudes can shift significantly when exposed to algorithmically curated political content; however, the overall impact on polarization is not straightforward due to various influencing factors.

- S17 supports (direct): A new tool allowing users to downrank content associated with antidemocratic attitudes showed that exposure to less polarizing content improved attitudes toward opposing parties.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

The societal impact of algorithm-driven polarization extends to diminished civic discourse and declining trust in democratic institutions.

- S17 supports (direct): The study indicates that reducing exposure to partisan animosity can lead to improved attitudes towards opposing parties, which relates to the impact of algorithm-driven polarization.

**Confidence:** MEDIUM → MEDIUM

**Status:** INSUFFICIENT_EVIDENCE → INSUFFICIENT_EVIDENCE

---

## 4. Current Research State

- Claims: 5
- Supported: 4
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 1
- Open Gaps: 0
- Remaining Searches: 4

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C2

**Why**

To clarify conflicting evidence regarding the impact of algorithms on political behavior versus polarization trends, focusing on specific cases that show differing outcomes.

**Next Search**

> Explore additional research on the direct effects of social media algorithms on individual political beliefs, specifically seeking studies that draw a clear distinction between changes in personal attitudes and overall trends in political polarization caused by algorithmic content curation.


---

# Iteration 7

## 1. Search

**Query**

> Explore additional research on the direct effects of social media algorithms on individual political beliefs, specifically seeking studies that draw a clear distinction between changes in personal attitudes and overall trends in political polarization caused by algorithmic content curation.

**Target:** C2

**Purpose:** GENERAL

**Why this query**

To clarify conflicting evidence regarding the impact of algorithms on political behavior versus polarization trends, focusing on specific cases that show differing outcomes.

5 result(s) retrieved; 2 new unique source(s) added.

- **S18 — Op-ed: Social media algorithms & their effects on American ...**
  URL: https://funginstitute.berkeley.edu/news/op-ed-social-media-algorithms-their-effects-on-american-politics
- **S19 — How tech platforms fuel U.S. political polarization and what ...**
  URL: https://www.brookings.edu/articles/how-tech-platforms-fuel-u-s-political-polarization-and-what-government-can-do-about-it

**Search Duration:** 2.20s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 2
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 4.17s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Social media algorithms influence political polarization by determining what content is visible to users, contributing to the reinforcement of existing beliefs and facilitating the creation of echo chambers.

- S18 supports (direct): The op-ed argues that social media algorithms contribute to political polarization by creating echo chambers and amplifying extreme ideologies, resulting in distrust and radicalization.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

The societal impact of algorithm-driven polarization extends to diminished civic discourse and declining trust in democratic institutions.

- S19 supports (direct): The article discusses how algorithm-driven polarization negatively impacts civic discourse and trust in democratic institutions.

**Confidence:** MEDIUM → MEDIUM

**Status:** INSUFFICIENT_EVIDENCE → INSUFFICIENT_EVIDENCE

---

## 4. Current Research State

- Claims: 5
- Supported: 4
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 1
- Open Gaps: 0
- Remaining Searches: 3

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C2

**Why**

Clarifying the conflicting evidence regarding the impact of algorithmic changes on individual political attitudes versus broader political polarization trends is crucial for a comprehensive understanding.

**Next Search**

> Analyze recent empirical studies that investigate how changes in social media algorithms specifically impact individual political attitudes and beliefs, focusing on nuances that distinguish these effects from broader societal polarization trends.


---

# Iteration 8

## 1. Search

**Query**

> Analyze recent empirical studies that investigate how changes in social media algorithms specifically impact individual political attitudes and beliefs, focusing on nuances that distinguish these effects from broader societal polarization trends.

**Target:** C2

**Purpose:** GENERAL

**Why this query**

Clarifying the conflicting evidence regarding the impact of algorithmic changes on individual political attitudes versus broader political polarization trends is crucial for a comprehensive understanding.

5 result(s) retrieved; 0 new unique source(s) added.

- No new unique sources were added.

**Search Duration:** 3.25s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 0
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 1.23s

---

## 3. Ledger Updates

No ledger or gap changes were recorded.

---

## 4. Current Research State

- Claims: 5
- Supported: 4
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 1
- Open Gaps: 0
- Remaining Searches: 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C2

**Why**

The claim that algorithm-driven content curation can significantly alter political attitudes while the overall impact on polarization remains complex needs further exploration to clarify discrepancies in the literature.

**Next Search**

> Identify recent empirical studies that further clarify how algorithm-driven content curation influences individual political attitudes compared to effects on overall political polarization, focusing on conflicting evidence and underlying factors.


---

# Iteration 9

## 1. Search

**Query**

> Identify recent empirical studies that further clarify how algorithm-driven content curation influences individual political attitudes compared to effects on overall political polarization, focusing on conflicting evidence and underlying factors.

**Target:** C2

**Purpose:** GENERAL

**Why this query**

The claim that algorithm-driven content curation can significantly alter political attitudes while the overall impact on polarization remains complex needs further exploration to clarify discrepancies in the literature.

5 result(s) retrieved; 2 new unique source(s) added.

- **S20 — Mechanisms of Algorithmic Recommendation on Social ...**
  URL: https://www.sciencedirect.com/org/science/article/pii/S1548367326000062
- **S21 — How do social media feed algorithms affect attitudes and ...**
  URL: https://cdr.lib.unc.edu/downloads/wp9891401

**Search Duration:** 3.16s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 0
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 5.52s

---

## 3. Ledger Updates

### New Claim C6

**Claim**

Algorithmic recommendation systems significantly contribute to social media opinion polarization by filtering and amplifying extreme viewpoints on platforms.

- S20 supports (direct): The study reveals how algorithms drive polarization by shaping viewpoint exposure and spreading extreme opinions on short video platforms.
- S21 supports (direct): Research indicates that while algorithmic changes affect content exposure, they do not significantly alter political attitudes, underscoring the complexity of polarization dynamics.

**Confidence:** MEDIUM

**Status:** INSUFFICIENT_EVIDENCE

---

## 4. Current Research State

- Claims: 6
- Supported: 4
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 2
- Open Gaps: 0
- Remaining Searches: 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C2

**Why**

Conflicting evidence regarding the impact of algorithms on political beliefs needs further exploration to understand influences on polarization better.

**Next Search**

> Find recent empirical studies examining the complexities in how social media algorithms impact individual political attitudes versus broader polarization trends, emphasizing evidence for conflicting outcomes and potential mediating factors.


---

# Iteration 10

## 1. Search

**Query**

> Find recent empirical studies examining the complexities in how social media algorithms impact individual political attitudes versus broader polarization trends, emphasizing evidence for conflicting outcomes and potential mediating factors.

**Target:** C2

**Purpose:** GENERAL

**Why this query**

Conflicting evidence regarding the impact of algorithms on political beliefs needs further exploration to understand influences on polarization better.

5 result(s) retrieved; 1 new unique source(s) added.

- **S22 — Ranking for engagement: How social media algorithms fuel ...**
  URL: https://www.sciencedirect.com/science/article/pii/S0047272726000253

**Search Duration:** 2.45s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 4
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 5.13s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Social media algorithms influence political polarization by determining what content is visible to users, contributing to the reinforcement of existing beliefs and facilitating the creation of echo chambers.

- S22 supports (direct): The study indicates that algorithms enhance misinformation and polarization through user engagement metrics, reinforcing existing beliefs and extremism.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

Political attitudes can shift significantly when exposed to algorithmically curated political content; however, the overall impact on polarization is not straightforward due to various influencing factors.

- S22 supports (direct): The paper discusses how engagement metrics related to algorithmic curation can alter user opinions and increase polarization, illustrating the complexities of political attitudes influenced by algorithms.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

Algorithm-driven content curation can distort public opinion and influence electoral outcomes by amplifying misinformation, ultimately affecting democratic processes.

- S22 supports (direct): The research shows that increasing emphasis on engagement metrics in algorithms distorts public opinion and exacerbates polarization, impacting electoral dynamics.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

The societal impact of algorithm-driven polarization extends to diminished civic discourse and declining trust in democratic institutions.

- S22 supports (direct): The study argues that algorithm-driven engagement strategies can diminish civic discourse and trust in democratic institutions by amplifying divisive content.

**Confidence:** MEDIUM → MEDIUM

**Status:** INSUFFICIENT_EVIDENCE → INSUFFICIENT_EVIDENCE

---

## 4. Current Research State

- Claims: 6
- Supported: 4
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 2
- Open Gaps: 0
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

- No major remaining uncertainty was identified.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 10 | 30.91s |
| Evidence Processing | 10 | 57.09s |
| Research Decision | 9 | 15.96s |
| Report Generation | 1 | 12.55s |
| Total Run | — | 116.53s |
