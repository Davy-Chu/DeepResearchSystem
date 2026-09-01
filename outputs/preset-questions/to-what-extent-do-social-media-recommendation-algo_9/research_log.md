# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions.

**Status:** Completed

**Stop Reason:** sufficient_evidence

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 10

**Unique Sources:** 13

**OpenAI Calls:** 4

**Tavily Calls:** 3

**Started:** 2026-09-01T02:57:55-04:00

**Ended:** 2026-09-01T02:59:11-04:00

**Total Runtime:** 76.28s

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

- **S1 — Algorithms Shift Polarization. Why Does Policy Still Miss the Real Problem? | TechPolicy.Press**
  URL: https://techpolicy.press/algorithms-shift-polarization-why-does-policy-still-miss-the-real-problem
- **S2 — Social Drivers and Algorithmic Mechanisms on Digital Media**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11373151
- **S3 — The Role of Social Media Algorithms in Shaping Political Polarisation in the United States**
  URL: https://www.humanrightsresearch.org/post/the-role-of-social-media-algorithms-in-shaping-political-polarisation-in-the-united-states
- **S4 — Meta's algorithms show US political polarization has no easy fix - WDSU**
  URL: https://www.wdsu.com/article/metas-algorithms-show-us-political-polarization-has-no-easy-fix/44679027
- **S5 — How Does Social Media Impact Political Polarization?**
  URL: https://news.northeastern.edu/2025/11/27/social-media-political-polarization-research

**Search Duration:** 3.19s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

There is strong evidence that recommendation and ranking systems change users’ political-media exposure and on-platform experience.

**Confidence:** High

**Why this confidence level**

The evidence includes large platform-based studies and a controlled reranking experiment. The exposure effect is directly measured and consistently described across sources.

**Evidence**

- The Meta/Facebook studies reported substantial ideological segregation in political-news exposure; changing ranking and feed mechanisms altered what users saw. Turning off Facebook resharing reduced exposure to untrustworthy and political news, while reducing same-ideology content also changed exposure. [S4]
- The review characterizes algorithms as systems that highlight and filter posts, news, people, and groups, while emphasizing that their effects are entangled with existing social behavior and social drivers. [S2]
- The X reranking experiment changed the ordering of the same posts users received, without removing content, demonstrating that ranking alone can alter exposure to antidemocratic and partisan-animosity content. [S1] [S5]

#### Finding 2

**Claim**

Evidence that algorithms change political beliefs or affective polarization is mixed, but a recent controlled X experiment reports a causal effect on partisan feelings.

**Confidence:** Medium

**Why this confidence level**

The sources describe a randomized, controlled intervention and consistent numerical results, but they are secondary reports of one short-duration study rather than the primary paper. The measured outcome is affective warmth toward the opposing party, not broad political ideology, voting, or offline behavior.

**Evidence**

- In the reported X experiment, 1,256 U.S. participants were assigned for one week to increased or decreased exposure to content expressing antidemocratic attitudes and partisan animosity. Decreased exposure made participants about 2.11 points warmer toward the opposing party, while increased exposure made them about 2.48 points cooler on a 100-point scale. [S1]
- The study’s university account reports that the effect was approximately two points and comparable to the change normally observed over several years in survey measures, and that it appeared regardless of participants’ partisan identification. [S5]
- The intervention changed only the ranking of posts, not the underlying set of posts, making the result evidence that algorithmic ordering can causally affect affective polarization under the study’s conditions. [S1] [S5]

#### Finding 3

**Claim**

Large Meta experiments found that changing several major feed features did not measurably change political attitudes, polarization, misinformation susceptibility, or extremist views during the 2020 election period.

**Confidence:** High

**Why this confidence level**

The source describes multiple studies based on platform data and interventions during the 2020 election. The findings directly distinguish exposure effects from null effects on measured political attitudes, though the source is a news report rather than the original studies.

**Evidence**

- Replacing Facebook’s algorithmic feed with chronological posts produced no measurable effect on polarization. Turning off resharing reduced exposure to untrustworthy and political news but did not significantly change political attitudes. Reducing same-ideology content likewise had no significant effect on polarization, misinformation susceptibility, or extremist views. [S4]
- The researchers concluded that algorithms were highly influential in users’ on-platform experiences and exposure segregation, while the tested changes did not sway political attitudes. [S4]

#### Finding 4

**Claim**

The literature reaches different conclusions partly because it studies different outcomes: exposure and engagement are more readily affected than durable beliefs, partisan identity, or behavior.

**Confidence:** High

**Why this confidence level**

The distinction is directly supported by the contrast between measured exposure changes and divergent attitude results. The gap concerning long-term and behavioral outcomes is explicit from what the sources do and do not report.

**Evidence**

- The Meta studies found large changes in exposure and time use but little or no change in political attitudes and polarization. [S4]
- The X experiment measured short-term affective warmth after one week, finding a modest shift, but the reported evidence does not establish effects on voting, political participation, policy preferences broadly construed, or long-term belief change. [S1] [S5]
- The review states that evidence on algorithms, misinformation, and polarization is far from straightforward and that existing evidence suggests algorithms often reinforce pre-existing social drivers rather than independently determining outcomes. [S2]

#### Finding 5

**Claim**

User choice and feedback loops are an important explanation for why algorithmic exposure can be politically segregated without producing large average attitude changes when ranking is altered.

**Confidence:** Medium

**Why this confidence level**

The mechanism is consistently described, but the supplied sources provide more conceptual and interpretive evidence than a direct test isolating each component.

**Evidence**

- The Meta researchers argued that users seek content aligned with their existing views and that algorithms make this selection easier, rather than necessarily creating those preferences. [S4]
- The review describes a feedback loop in which social drivers shape algorithmic recommendations and recommendations in turn reinforce those drivers. [S2]
- The discussion of filter bubbles and echo chambers distinguishes algorithmic curation from users’ selective networks and engagement choices, presenting polarization as an interaction between platform architecture and user behavior. [S3]

#### Finding 6

**Claim**

The apparent contradiction between the Meta and X findings may reflect differences in intervention design, platform, content target, duration, and outcome—not necessarily a simple disagreement about whether algorithms matter.

**Confidence:** Medium

**Why this confidence level**

The design differences are clearly documented, but the sources do not provide a formal cross-study comparison proving which design feature caused the divergent results.

**Evidence**

- The Meta interventions changed broad platform features such as chronology, resharing, or same-ideology recommendations during an election period; they altered exposure but produced null effects on the reported political outcomes. [S4]
- The X experiment deliberately increased or decreased exposure to posts classified as antidemocratic or expressing partisan animosity, and measured affective warmth after one week. [S1] [S5]
- The review cautions that algorithmic effects are context-dependent and embedded in wider social and political conditions. [S2]

### Conflicts Found

- The X reranking study is presented as evidence that changing algorithmic ranking causally shifts affective polarization, whereas the Meta experiments found that several algorithmic changes did not significantly alter polarization or political attitudes. [S1] [S4] [S5]
- There is a conditional disagreement over whether algorithms primarily cause polarization or mainly facilitate users’ pre-existing preferences: the X findings support an independent causal effect under targeted reranking, while the Meta interpretation emphasizes user self-selection and limited effects of broad feed changes. [S1] [S2] [S4]

### Important Gaps

- Do algorithmic recommendations change voting, political participation, sharing, offline hostility, or other political behavior?
- Are the X reranking effects durable beyond one week, and do they generalize to other platforms, countries, elections, or less politically engaged users?
- Why did targeted manipulation of partisan-animosity content produce an attitude effect while broad Meta feed interventions did not?
- How large are cumulative effects over months or years compared with the short-term experimental effects?
- Do algorithms amplify polarization mainly by changing exposure, by increasing engagement and repeated attention, or through interactions with user networks and pre-existing partisan identities?

**Analysis Duration:** 19.78s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The supplied evidence supports a careful conclusion about exposure and some short-term affective attitudes, but it does not adequately answer the question’s explicit behavioral component or establish the durability and generalizability of the newer causal finding. One focused search for behavioral and long-term outcomes would materially improve the answer.

**Next Search**

> social media recommendation algorithm randomized experiment political behavior voting participation sharing polarization long-term effects

---

# Iteration 2

## 1. Search

**Query**

> social media recommendation algorithm randomized experiment political behavior voting participation sharing polarization long-term effects

**Why this query**

The supplied evidence supports a careful conclusion about exposure and some short-term affective attitudes, but it does not adequately answer the question’s explicit behavioral component or establish the durability and generalizability of the newer causal finding. One focused search for behavioral and long-term outcomes would materially improve the answer.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S6 — How do social media feed algorithms affect attitudes and ...**
  URL: https://cdr.lib.unc.edu/downloads/wp9891401
- **S7 — Ranking for engagement: How social media algorithms fuel misinformation and polarization**
  URL: https://www.sciencedirect.com/science/article/pii/S0047272726000253
- **S8 — The political effects of X's feed algorithm**
  URL: https://www.nature.com/articles/s41586-026-10098-2
- **S9 — Op-ed: Social media algorithms & their effects on American ...**
  URL: https://funginstitute.berkeley.edu/news/op-ed-social-media-algorithms-their-effects-on-american-politics

**Search Duration:** 3.42s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The strongest evidence concerns changes in political exposure and on-platform behavior, not necessarily changes in political attitudes.

**Confidence:** High

**Why this confidence level**

S6 provides a randomized platform experiment with direct measures of both exposure and attitudes, and it corroborates the accumulated evidence that feed changes substantially affect users’ on-platform experience.

**Evidence**

- The randomized Facebook/Instagram experiment moved users from algorithmic to reverse-chronological feeds. This substantially changed platform time and activity and altered exposure to political, untrustworthy, uncivil, moderate, and ideologically mixed content. [S6]
- The same experiment found no significant change over three months in issue polarization, affective polarization, political knowledge, or other key attitudes. [S6]
- Prior platform studies and the X reranking experiment likewise show that ranking changes what users encounter even when the underlying inventory is not removed. [S1] [S4] [S5]

#### Finding 2

**Claim**

The Meta evidence supports a substantial exposure effect but a limited average effect on measured political beliefs during the study period.

**Confidence:** High

**Why this confidence level**

This is a direct report of the randomized experiment rather than merely an interpretation of observational data.

**Evidence**

- Replacing Facebook and Instagram’s default feed algorithms with chronological feeds changed exposure and reduced time and activity, but did not significantly alter issue polarization, affective polarization, political knowledge, or other key attitudes during the three-month 2020 election study. [S6]
- The source explains that the intervention isolates ranking from other platform features, while user choice and network composition remain other determinants of what content is available to rank. [S6]

#### Finding 3

**Claim**

New evidence indicates that effects may depend strongly on the platform and the design of the algorithmic intervention: an X field experiment found political-attitude and engagement effects where the Meta chronological-feed experiment found null attitude effects.

**Confidence:** Medium

**Why this confidence level**

The X result is reported by the journal source, but the retrieved abstract is truncated and does not provide the effect sizes, detailed outcome measures, sample composition, or full methodological qualifications.

**Evidence**

- Nature reports a seven-week randomized X field experiment assigning active U.S. users to algorithmic or chronological feeds; switching from chronological to algorithmic ranking increased engagement and shifted political opinion in a more conservative direction. [S8]
- The earlier X experiment deliberately increased or decreased exposure to antidemocratic and partisan-animosity content and found corresponding changes in affective warmth toward the opposing party after one week. [S1] [S5]
- The Facebook/Instagram experiment changed the overall ranking system during a three-month election-period intervention but found no significant attitude effects. [S6]

#### Finding 4

**Claim**

A plausible mechanism is a feedback loop in which engagement-oriented ranking amplifies content from politically extreme users, potentially increasing polarization over time.

**Confidence:** Medium

**Why this confidence level**

S7 combines a theoretical model with survey evidence rather than a clean randomized intervention; the mechanism is informative but does not establish the size or generality of causal effects.

**Evidence**

- The theoretical model argues that weighting likes and shares more heavily increases engagement but also misinformation and polarization because ideologically extreme users engage disproportionately; personalization is predicted to amplify the effect further. [S7]
- The model’s authors state that survey evidence from the United States and Italy around Facebook’s 2018 Meaningful Social Interactions update is consistent with increased ideological extremism and affective polarization after greater emphasis on engagement metrics. [S7]
- The broader literature describes algorithmic ranking as interacting with user behavior, pre-existing preferences, and network composition rather than operating as an isolated cause. [S2] [S3] [S6]

#### Finding 5

**Claim**

The literature reaches different conclusions because studies manipulate different parts of the platform and measure different outcomes over different periods.

**Confidence:** High

**Why this confidence level**

The design and outcome differences are explicit in the sources and provide a well-supported explanation for apparently conflicting results, although they do not identify which single design feature accounts for the divergence.

**Evidence**

- S6 replaces personalized ranking with chronology across Facebook and Instagram and measures exposure, activity, knowledge, and polarization over three months. [S6]
- S1 and S5 target exposure to antidemocratic or animosity-related content and measure short-term partisan warmth after one week. [S1] [S5]
- S8 compares algorithmic and chronological feeds on X for seven weeks and reports effects on engagement, political opinion, and online behavior. [S8]
- S7 focuses on engagement-weighting and dynamic feedback, while the review evidence emphasizes interactions between algorithms and users’ existing social behavior. [S2] [S7]

### Conflicts Found

- The Meta experiment found no significant effects on issue or affective polarization after replacing algorithmic feeds with chronological feeds, whereas the X experiments report shifts in partisan feelings or political opinion under algorithmic-ranking interventions. [S1] [S6] [S8]
- The findings conditionally disagree over whether ranking algorithms have independent political effects. Broad feed replacement on Meta produced null average attitude effects, while targeted or platform-specific X interventions and the engagement-feedback account indicate that some ranking rules can affect attitudes under particular conditions. [S1] [S6] [S7] [S8]
- S7’s survey-consistent account attributes increased extremism and affective polarization to Facebook’s 2018 engagement-oriented update, but S6’s randomized 2020 Facebook/Instagram feed experiment found no comparable average attitude effect. The studies concern different updates, platforms/features, periods, and designs, so this is a conditional rather than direct contradiction. [S6] [S7]

### Important Gaps

- What were the precise effect sizes, sample characteristics, and online-behavior outcomes in the full seven-week X study reported in S8?
- Do the observed X attitude effects persist beyond one or several weeks, and do they affect voting, participation, sharing, or offline conduct?
- Why do targeted changes in exposure to partisan animosity appear more consequential than broad chronological-feed replacement?
- How large are cumulative feedback effects over months or years, relative to short-term experimental effects?
- How well do these U.S.- and platform-specific findings generalize to other countries, elections, platforms, and less politically engaged users?

**Analysis Duration:** 16.67s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The central exposure-versus-attitudes distinction can now be answered responsibly, and S6 substantially strengthens the evidence base. However, S8 appears especially important for reconciling Meta and X results, yet the retrieved content is only an abstract excerpt and omits key estimates and behavioral findings. One focused search for the full X study results would materially improve the comparison.

**Next Search**

> Gauthier Hodler Widmer Zhuravskaya 2026 Nature X feed algorithm full text political opinion engagement online behavior effect sizes

---

# Iteration 3

## 1. Search

**Query**

> Gauthier Hodler Widmer Zhuravskaya 2026 Nature X feed algorithm full text political opinion engagement online behavior effect sizes

**Why this query**

The central exposure-versus-attitudes distinction can now be answered responsibly, and S6 substantially strengthens the evidence base. However, S8 appears especially important for reconciling Meta and X results, yet the retrieved content is only an abstract excerpt and omits key estimates and behavioral findings. One focused search for the full X study results would materially improve the comparison.

**Results**

5 results retrieved.

4 new unique sources added.

### Sources

- **S10 — The political effects of X's feed algorithm. - Abstract**
  URL: https://pubmed.ncbi.nlm.nih.gov/41708846
- **S11 — Social sciences: X’s algorithm may influence political attitudes (Nature) | Nature Portfolio**
  URL: https://www.natureasia.com/en/info/press-releases/detail/9242
- **S12 — How X’s algorithm shifts political attitudes**
  URL: https://cepr.org/voxeu/columns/how-xs-algorithm-shifts-political-attitudes
- **S13 — NEWS: Algorithm on X effects political views in the USA | unisg.ch**
  URL: https://www.unisg.ch/en/newsroom/algorithm-on-x-effects-political-views-in-the-usa

**Search Duration:** 2.88s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

New primary-source evidence strengthens the conclusion that recommendation algorithms can change political attitudes, not merely exposure, under some platform-specific conditions.

**Confidence:** High

**Why this confidence level**

S10 is an abstract of the Nature article and directly reports the randomized design, sample, duration, and outcomes; S11 independently summarizes the same study.

**Evidence**

- A 2023 randomized field experiment assigned 4,965 active U.S. X users to algorithmic or chronological feeds for approximately seven weeks. Switching from chronological to algorithmic ranking increased engagement and shifted political opinion toward more conservative positions on policy priorities, views of investigations into Donald Trump, and the war in Ukraine. [S10] [S11]

#### Finding 2

**Claim**

The new X study finds effects on selected policy attitudes and online behavior, but not on affective polarization or self-reported partisanship.

**Confidence:** High

**Why this confidence level**

These are explicit outcomes in the study abstract and institutional summary, though they do not establish changes in offline political behavior.

**Evidence**

- Neither turning the algorithm on nor turning it off significantly affected affective polarization or self-reported partisanship, even though turning it on shifted several political opinions. [S10]
- Users assigned to the algorithmic feed engaged more and were more likely to follow conservative political activist accounts. [S10] [S11]

#### Finding 3

**Claim**

The study provides evidence of a mechanism through which exposure can become behaviorally and politically persistent: algorithmic exposure led users to follow conservative activist accounts, which they continued to follow after returning to a chronological feed.

**Confidence:** Medium

**Why this confidence level**

The evidence is reported directly from the experiment, but the supplied material does not provide detailed estimates, persistence duration beyond the study, or separate tests of every proposed mechanism.

**Evidence**

- Feed-content analysis found that X promoted conservative content and demoted posts by traditional media. Exposure to this content increased following of conservative political activist accounts, and those follows persisted after the algorithm was switched off. [S10] [S11]

#### Finding 4

**Claim**

The asymmetry between switching X’s algorithm on and switching it off helps explain why prior studies that only switched algorithms off could find null effects.

**Confidence:** High

**Why this confidence level**

The asymmetry and the contrast with Meta are explicit in the primary abstract and Nature’s summary. The causal explanation is supported by the observed persistence of follows, though broader long-term interpretation remains limited.

**Evidence**

- On X, switching from chronological to algorithmic feeds produced political and engagement effects, whereas switching from algorithmic to chronological feeds produced no comparable effects. The authors suggest that earlier algorithmic exposure had already shaped users’ attitudes and account-following behavior. [S10] [S11]
- The Nature press summary explicitly contrasts this result with previous Meta experiments in which switching off algorithmic feeds found little political effect. [S11]

#### Finding 5

**Claim**

The accumulated literature now supports a conditional rather than universal account: algorithms clearly alter political exposure; some ranking systems can shift selected political attitudes and online behavior; but effects are not consistently observed for broad affective polarization, partisanship, or all platforms and interventions.

**Confidence:** High

**Why this confidence level**

The cross-study pattern is consistent: exposure effects are robust, while attitudinal effects depend on platform, content, intervention direction, and outcome.

**Evidence**

- Meta experiments changed exposure, time use, and on-platform activity without significant average effects on issue polarization, affective polarization, political knowledge, or other measured attitudes. [S6]
- Earlier X experiments found modest changes in partisan warmth after targeted reranking, while the new seven-week X experiment found shifts in selected policy opinions but no significant change in affective polarization or partisanship. [S1] [S5] [S10]
- The new X experiment also found increased engagement and following of conservative activist accounts, extending the evidence beyond exposure alone. [S10] [S11]

### Conflicts Found

- The new X study reports conservative shifts in selected political opinions when algorithmic ranking is introduced, whereas the Meta chronological-feed experiment found no significant average changes in political attitudes or polarization. This is a genuine empirical contrast, but the studies differ in platform, algorithm, period, treatment direction, and outcomes. [S6] [S10] [S11]
- Within the X evidence, algorithmic exposure shifts policy opinions but does not significantly shift affective polarization or self-reported partisanship. Thus, evidence for ideological or policy-attitude change is stronger than evidence for generalized partisan animosity or identity change. [S1] [S5] [S10]
- The new study reports persistent following behavior after algorithmic exposure, while the broader accumulated evidence still does not show whether such online behavioral changes translate into voting, participation, sharing, or offline conduct. [S10] [S11] [S6]

### Important Gaps

- Do the X-induced opinion and following changes persist for substantially longer than the approximately seven-week experiment?
- Do algorithmic effects on following conservative activist accounts lead to measurable changes in sharing, political participation, voting, or offline behavior?
- Why does X promote conservative content and demote traditional media, and how platform-specific is this content-selection pattern?
- What explains the contrast between policy-attitude effects on X and null average effects in Meta’s broad feed intervention?
- How do effects vary by users’ initial ideology, political engagement, network composition, and exposure to competing information?
- Can the X findings generalize beyond active U.S. users, the 2023 political environment, and X’s particular ranking system?

**Analysis Duration:** 13.30s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The new primary Nature evidence materially improves the answer to the central question: it directly documents causal effects on selected political attitudes and online following behavior, while also showing null effects on affective polarization and partisanship. The remaining gaps concern generalization, durability, and offline behavior, but the core distinction between exposure effects and belief/behavior effects can now be answered responsibly from the accumulated evidence.

**Stop Reason:** sufficient_evidence

---

# Final Research Decision

**Research Stopped Because**

The analyzer determined that the important parts of the question could be answered responsibly.

**Stop Reason:** sufficient_evidence

**Searches Performed:** 3

**Unique Sources:** 13

**Remaining Uncertainty**

- Whether X-induced opinion and following changes persist substantially beyond the approximately seven-week study.
- Whether changes in follows or on-platform engagement lead to changes in sharing, voting, political participation, or offline behavior.
- Why targeted exposure to partisan animosity on X produced affective effects while broad chronological-feed replacement on Meta did not produce comparable average effects.
- How findings generalize beyond active U.S. users, the studied elections and political environments, and the particular ranking systems of X, Facebook, and Instagram.
- How effects vary with users’ prior ideology, political engagement, network composition, and exposure to competing information.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 9.50s |
| OpenAI Analysis | 3 | 49.75s |
| Report Generation | 1 | 17.03s |
| Total Run | — | 76.28s |
