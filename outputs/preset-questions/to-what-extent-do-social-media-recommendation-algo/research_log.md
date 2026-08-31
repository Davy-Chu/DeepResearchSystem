# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 10

**OpenAI Calls:** 4

**Tavily Calls:** 3

**Started:** 2026-08-31T17:05:10-04:00

**Ended:** 2026-08-31T17:06:30-04:00

**Total Runtime:** 79.79s

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

- **S1 — How algorithmically curated online environments influence users’ political polarization: Results from two experiments with panel data - ScienceDirect**
  URL: https://www.sciencedirect.com/science/article/pii/S2451958823000763
- **S2 — The Role of Social Media Algorithms in Shaping Political Polarisation in the United States**
  URL: https://www.humanrightsresearch.org/post/the-role-of-social-media-algorithms-in-shaping-political-polarisation-in-the-united-states
- **S3 — Social Drivers and Algorithmic Mechanisms on Digital Media**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11373151
- **S4 — Algorithms Shift Polarization. Why Does Policy Still Miss the Real Problem? | TechPolicy.Press**
  URL: https://techpolicy.press/algorithms-shift-polarization-why-does-policy-still-miss-the-real-problem
- **S5 — How Does Social Media Impact Political Polarization?**
  URL: https://news.northeastern.edu/2025/11/27/social-media-political-polarization-research

**Search Duration:** 3.15s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Algorithmic curation clearly changes the composition and ordering of political content users encounter, but this exposure effect is not equivalent to changing political beliefs or behavior.

**Confidence:** Medium

**Why this confidence level**

The mechanism is directly described, but S2 is a secondary commentary and S4–S5 are journalistic or advocacy-oriented accounts rather than the underlying full research papers.

**Evidence**

- Recommendation systems rank, filter, and suggest content using behavioral signals such as likes, shares, comments, watch time, follows, searches, and prior engagement; algorithmic feeds therefore determine visibility and ordering rather than presenting a neutral pool. [S2]
- The strongest experimental designs described here manipulate which posts appear higher in users’ feeds while leaving the underlying set of posts and followed accounts unchanged. [S4] [S5]

#### Finding 2

**Claim**

Exposure to like-minded political content can increase both attitude polarization and affective polarization, whereas exposure to opposing content produces weaker polarization in the reported experiment.

**Confidence:** High

**Why this confidence level**

S1 reports a panel-based experimental design and directly distinguishes content exposure from algorithmic selection.

**Evidence**

- In two quasi-experiments with three-wave panel data, participants exposed to arguments aligned with their prior attitudes became more attitude- and affectively polarized than participants exposed to opposing arguments. [S1]

#### Finding 3

**Claim**

Algorithmic selection did not generally amplify the polarizing effect of like-minded exposure, although it produced a small direct increase in attitude polarization for one topic.

**Confidence:** High

**Why this confidence level**

This is the study’s explicit causal comparison and directly addresses whether the algorithm adds an effect beyond the content users receive.

**Evidence**

- S1 compared algorithmically selected with randomly selected arguments, holding the direction of the content relative to participants’ attitudes constant. Like-minded exposure was more polarizing, but algorithmic selection did not amplify that effect overall; a small direct effect appeared for one topic. [S1]

#### Finding 4

**Claim**

There is some experimental evidence that changing feed ranking alone can change political attitudes, particularly affective evaluations of the opposing party.

**Confidence:** Medium

**Why this confidence level**

Both sources describe the same underlying study and report causal effects, but the retrieved material consists of secondary summaries, not the full Science article. The evidence concerns affective polarization, not all political beliefs or behavior.

**Evidence**

- The reported 2025 X browser-extension experiment reranked existing posts to increase or decrease exposure to content classified as expressing antidemocratic attitudes and partisan animosity. Secondary accounts report that increased exposure made evaluations of the opposing party about two points colder, while decreased exposure made them about two points warmer after one week. [S4] [S5]
- The manipulation reportedly changed the order and prominence of posts without removing them, isolating ranking as the intervention more closely than ordinary observational studies do. [S5]

#### Finding 5

**Claim**

The available evidence does not establish that recommendation algorithms broadly change political behavior, such as voting, political participation, or offline conduct.

**Confidence:** High

**Why this confidence level**

The outcomes explicitly reported in the sources are attitudinal; behavioral effects are an important evidence gap rather than a demonstrated result.

**Evidence**

- S1 measures attitude and affective polarization, not political behavior. The reported X experiment also measures feelings toward the opposing party and related attitudes, with no behavioral outcomes presented in the retrieved content. [S1] [S4] [S5]

#### Finding 6

**Claim**

The literature reaches different conclusions partly because studies vary in what they identify: exposure to congenial or hostile content, the ranking algorithm’s incremental effect, and downstream attitude or behavioral change are distinct causal questions.

**Confidence:** High

**Why this confidence level**

The sources converge on identification and feedback-loop problems, although the retrieved material does not provide a systematic review of all competing studies.

**Evidence**

- S1 argues that previous studies often could not separate the effects of exposure to like-minded content from effects caused by algorithmic selection itself, and reports inconsistent evidence for the broader causal relationship. [S1]
- The review by Metzler and Garcia characterizes algorithmic effects on polarization as far from straightforward and says existing evidence suggests algorithms mostly reinforce pre-existing social drivers. [S3]
- S2 describes a feedback loop in which users’ follows and engagement shape algorithmic recommendations, while recommendations in turn structure future exposure; this makes user self-selection and algorithmic influence difficult to disentangle. [S2]

#### Finding 7

**Claim**

Algorithmic effects are likely heterogeneous and context-dependent rather than uniformly polarizing.

**Confidence:** Medium

**Why this confidence level**

The evidence supports conditional effects, but the available sources do not establish how effects vary across platforms, countries, political groups, or recommendation objectives.

**Evidence**

- S1 finds that like-minded exposure has stronger polarizing effects than opposing exposure, while the incremental effect of algorithmic selection differs by topic and is small in the reported case. [S1]
- S3 states that algorithms are embedded in broader social drivers and generally reinforce existing social phenomena rather than operating as an independent cause. [S3]

### Conflicts Found

- S1 finds no general amplification by algorithmic selection beyond the effect of like-minded content, whereas S4 and S5 describe a feed-reranking experiment as showing that ranking changes directly shifted affective polarization. These findings are not necessarily incompatible: S1 tests whether algorithmic selection magnifies exposure effects in a constructed environment, while the X study tests whether changing the prominence of hostile content changes partisan feelings. [S1] [S4] [S5]
- S3’s synthesis says algorithms mostly reinforce existing social drivers, while S4 and S5 present ranking as producing direct causal attitude changes. The disagreement may reflect different meanings of 'direct': algorithms can have an incremental causal effect while still depending on users’ prior networks, preferences, and the platform’s available content. [S3] [S4] [S5]
- S2, S4, and S5 make broad claims about algorithmic amplification and polarization, but the retrieved passages rely heavily on secondary citations and, in S2’s case, include claims about studies dated after the apparent publication context. These claims are weaker evidence than the directly reported experiment in S1. [S2] [S4] [S5]

### Important Gaps

- How large and durable are algorithmic effects on political beliefs beyond short-term affective evaluations?
- Do recommendation algorithms change concrete political behavior, including voting, political participation, political discussion, or offline hostility?
- How representative are the reported experimental participants and platforms, especially beyond X and beyond the United States or Germany?
- What aspects of ranking matter most: ideological similarity, emotional intensity, partisan animosity, engagement optimization, or repeated exposure?
- Do effects differ for users with strong prior partisan identities, politically disengaged users, and users who actively seek cross-cutting information?

**Analysis Duration:** 19.30s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The current evidence supports a responsible distinction between changed exposure and changed attitudes, but it leaves the behavior question largely unanswered and relies on secondary reports for the strongest claimed feed-ranking experiment. A focused search for causal studies measuring political behavior and durable belief change would materially improve the answer.

**Next Search**

> causal experiment social media recommendation algorithm political behavior voting participation political beliefs longitudinal

---

# Iteration 2

## 1. Search

**Query**

> causal experiment social media recommendation algorithm political behavior voting participation political beliefs longitudinal

**Why this query**

The current evidence supports a responsible distinction between changed exposure and changed attitudes, but it leaves the behavior question largely unanswered and relies on secondary reports for the strongest claimed feed-ranking experiment. A focused search for causal studies measuring political behavior and durable belief change would materially improve the answer.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S6 — How X's algorithm shifts political attitudes**
  URL: https://cepr.org/voxeu/columns/how-xs-algorithm-shifts-political-attitudes
- **S7 — Alternative social media algorithms can help users form more accurate and less polarized beliefs | EurekAlert!**
  URL: https://www.eurekalert.org/news-releases/1128531
- **S8 — A systematic review of worldwide causal and correlational evidence on digital media and democracy**
  URL: https://www.nature.com/articles/s41562-022-01460-1

**Search Duration:** 3.24s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

A controlled experiment indicates that the design of content-ranking algorithms can affect political beliefs, not merely exposure, although the evidence concerns short-term belief updating rather than durable real-world behavior.

**Confidence:** Medium

**Why this confidence level**

The study uses experimental manipulation and directly measures belief updating, but the retrieved evidence is a university press release rather than the full paper, and the task involves brief exposure to selected posts rather than ordinary long-term platform use.

**Evidence**

- In a two-stage experiment with 500 participants generating a content inventory and a separate sample of 1,000 US residents, participants viewed feeds selected and ranked by one of five algorithms and then revised beliefs on six topics. [S7]
- The engagement-based ranking algorithm produced more polarized and less accurate beliefs than the other tested algorithms, while alternative bridging- and intelligence-based rankings increased consensus or factual accuracy in some comparisons. [S7]

#### Finding 2

**Claim**

The new experiment strengthens the case that ranking itself can influence political attitudes, while also suggesting that the direction of the effect depends on the ranking objective.

**Confidence:** Medium

**Why this confidence level**

The source reports a direct experimental comparison, but details about implementation, effect sizes, statistical uncertainty, and the exact construction of the algorithms are unavailable in the retrieved passage.

**Evidence**

- The reported experiment compared engagement-based ranking with bridging-based, intelligence-based, and other algorithms while holding the underlying content inventory within the experimental design; outcomes differed across algorithms in polarization, consensus, and accuracy. [S7]
- The engagement-based feed was perceived as more insightful and received more positive feedback even though it generated more polarized and less accurate beliefs, indicating that user satisfaction is not a reliable proxy for democratic or epistemic outcomes. [S7]

#### Finding 3

**Claim**

A broad systematic review supports the conclusion that effects of digital media on polarization are variable across political systems and outcomes, rather than uniformly harmful or beneficial; it does not isolate recommendation algorithms specifically.

**Confidence:** High

**Why this confidence level**

S8 is a systematic review in Nature Human Behaviour with a large evidence base, but its scope is digital media use broadly and therefore cannot by itself establish the causal effect of recommendation algorithms.

**Evidence**

- A systematic review of 496 articles reports that associations between digital media and political outcomes vary by the outcome and political system; growing polarization was among the potentially detrimental associations and was more pronounced in established democracies. [S8]

#### Finding 4

**Claim**

The accumulated evidence now supports a two-stage conclusion: algorithms reliably alter what users encounter, and some controlled experiments show that ranking can alter attitudes or belief updating, but evidence of effects on concrete political behavior remains absent from the retrieved material.

**Confidence:** High

**Why this confidence level**

The distinction between exposure, attitudes, and behavior is consistently supported across the available sources; the behavioral conclusion is appropriately limited to what these sources measured.

**Evidence**

- Prior evidence shows that recommendation systems rank, filter, and suggest content using behavioral signals, thereby changing content visibility and ordering. [S2]
- The like-mindedness experiment found that exposure to congenial arguments increased attitude and affective polarization, but algorithmic selection did not generally amplify that exposure effect beyond the content direction itself. [S1]
- The X reranking experiment reportedly found short-term changes in evaluations of the opposing party, and the new experiment reports changes in polarization and belief accuracy under different ranking algorithms. [S4] [S5] [S7]
- The retrieved experiments report attitudinal or belief outcomes, not voting, participation, political discussion, or offline conduct. [S1] [S4] [S5] [S7]

#### Finding 5

**Claim**

The literature reaches different conclusions because studies manipulate or observe different links in the causal chain and use different comparison conditions.

**Confidence:** High

**Why this confidence level**

The sources provide convergent methodological reasons for divergent findings, though they do not constitute a complete meta-analysis of recommendation-algorithm studies.

**Evidence**

- S1 separates exposure to like-minded content from the incremental effect of algorithmic selection and finds strong effects of content alignment but little general additional amplification by selection. [S1]
- S4 and S5 examine feed reranking and report direct changes in affective evaluations, while S7 compares alternative ranking objectives and reports changes in belief updating, polarization, and accuracy. [S4] [S5] [S7]
- S2 describes reciprocal feedback between users’ preferences and recommendations, creating confounding between self-selection and algorithmic influence. [S2]
- S8 shows that broader digital-media effects differ by outcome and political system, limiting generalization from any one platform or experiment. [S8]

### Conflicts Found

- S1 finds that algorithmic selection did not generally amplify the polarizing effect of like-minded content, whereas S7 reports that an engagement-based ranking algorithm produced more polarized and less accurate beliefs than alternative rankings. These are conditional rather than necessarily contradictory: S1 estimates an algorithm's incremental amplification of content alignment, while S7 compares different ranking objectives in a belief-updating task. [S1] [S7]
- S3 characterizes algorithms as mainly reinforcing pre-existing social drivers, whereas S4, S5, and S7 report direct attitude or belief effects from ranking. These positions can coexist if algorithms have modest causal effects that operate through users' prior preferences, available content, and repeated exposure. [S3] [S4] [S5] [S7]
- S8 reports polarization associations in the broader digital-media literature, but its scope does not establish that recommendation algorithms caused those associations. Applying its conclusion directly to algorithmic ranking would overstate the evidence. [S8]

### Important Gaps

- Do ranking-induced attitude changes persist beyond the brief experimental periods, and do they generalize to ordinary multi-platform use?
- Do recommendation algorithms affect concrete political behavior, including voting, participation, political discussion, or offline hostility?
- What are the effect sizes and statistical uncertainties in the S7 experiment, and how were its five algorithms operationalized?
- How representative are the experimental samples and contexts, particularly outside the United States and beyond X-like platforms?
- Which algorithmic features matter most: ideological similarity, emotionality, partisan hostility, engagement optimization, personalization, or repeated exposure?

**Analysis Duration:** 15.62s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The central exposure-versus-attitudes distinction is now better supported, but the question explicitly includes political behavior, for which the retrieved evidence remains a major gap. A targeted search for causal behavioral studies would materially improve the answer.

**Next Search**

> causal experiment social media recommendation algorithm political behavior voting participation polarization

---

# Iteration 3

## 1. Search

**Query**

> causal experiment social media recommendation algorithm political behavior voting participation polarization

**Why this query**

The central exposure-versus-attitudes distinction is now better supported, but the question explicitly includes political behavior, for which the retrieved evidence remains a major gap. A targeted search for causal behavioral studies would materially improve the answer.

**Results**

5 results retrieved.

2 new unique sources added.

### Sources

- **S9 — Independent research shows that X's (Twitter's) algorithm can influence political polarisation**
  URL: https://sciencemediacentre.es/en/independent-research-shows-xs-twitters-algorithm-can-influence-political-polarisation
- **S10 — How do social media feed algorithms affect attitudes and ...**
  URL: https://cdr.lib.unc.edu/downloads/wp9891401

**Search Duration:** 2.48s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Recommendation algorithms substantially change users’ exposure and on-platform activity, but exposure changes do not necessarily translate into changes in political attitudes.

**Confidence:** High

**Why this confidence level**

S10 reports a randomized controlled experiment with direct measures of exposure, activity, and political attitudes.

**Evidence**

- In a randomized 2020 Facebook and Instagram experiment, replacing algorithmic feeds with chronological feeds changed the amount and type of political, untrustworthy, uncivil, moderate, and ideologically mixed content users encountered. It also substantially reduced time spent on the platforms and user activity. [S10]
- Despite these changes in exposure and activity over three months, the chronological feed did not significantly change issue polarization, affective polarization, political knowledge, or other key attitudes. [S10]

#### Finding 2

**Claim**

The evidence that algorithms change what users see is stronger and more consistent than the evidence that they broadly change political beliefs or polarization.

**Confidence:** High

**Why this confidence level**

The distinction is supported by both a large randomized platform experiment and a separate exposure experiment, although the studies use different platforms and interventions.

**Evidence**

- S10 directly finds substantial changes in content exposure when algorithmic ranking is replaced, while finding no significant effects on several political attitudes. [S10]
- S1 similarly finds that exposure to like-minded arguments increases attitude and affective polarization, but algorithmic selection does not generally amplify that effect beyond the direction of the content itself. [S1]
- S2 describes recommendation systems as ranking, filtering, and suggesting content using behavioral signals, thereby determining content visibility and ordering. [S2]

#### Finding 3

**Claim**

Some newer field and laboratory-style experiments indicate that ranking can causally affect political attitudes or belief updating under particular conditions.

**Confidence:** Medium

**Why this confidence level**

Both studies directly manipulate ranking or feed exposure, but the retrieved evidence for S7 is a press release and S9 is a secondary account of the X study; both mainly measure short-term attitudes or beliefs.

**Evidence**

- The X browser-extension experiment varied exposure to anti-democratic and partisan-hostile content during the 2024 US election campaign. The reported result was that increasing such exposure made evaluations of the opposing party colder, while reducing it made them warmer. [S9]
- S7 reports that an engagement-based ranking algorithm generated more polarized and less accurate beliefs than alternative ranking objectives in a controlled belief-updating experiment. [S7]

#### Finding 4

**Claim**

The best-supported conclusion is that algorithms have a conditional, generally modest-to-substantial potential effect on polarization, rather than being a universal or dominant cause of polarization.

**Confidence:** High

**Why this confidence level**

The sources support a qualified synthesis: algorithmic effects exist in some settings, but their magnitude and even detectability depend on the content targeted, platform, period, and outcome measured.

**Evidence**

- S10 found large exposure and activity effects but no detectable attitude effects from switching between algorithmic and chronological feeds on Facebook and Instagram. [S10]
- S1 found strong polarization effects from like-minded content exposure but little general additional amplification attributable to algorithmic selection. [S1]
- S9 reports an attitude effect when the manipulated content specifically involved anti-democratic attitudes and partisan hostility during a highly polarized election period. [S9]
- S3 characterizes algorithms as generally reinforcing pre-existing social drivers rather than acting as independent causes. [S3]

#### Finding 5

**Claim**

The retrieved evidence does not establish that recommendation algorithms change concrete political behavior such as voting, turnout, participation, or offline hostility.

**Confidence:** High

**Why this confidence level**

The sources clearly identify behavioral effects as unmeasured or unresolved, though S10 does demonstrate effects on platform use and activity.

**Evidence**

- S10 measures on-platform activity and political attitudes, but the retrieved passage does not report effects on voting or other offline political behavior. [S10]
- S9 explicitly states that the duration of the observed effects and their impact on voting or other citizen participation remain unclear. [S9]
- S1, S4, S5, and S7 primarily report attitude, affective polarization, or belief outcomes rather than behavioral outcomes. [S1] [S4] [S5] [S7]

#### Finding 6

**Claim**

The literature reaches different conclusions because studies compare different counterfactuals and identify different links in the causal chain.

**Confidence:** High

**Why this confidence level**

The sources directly show that apparently conflicting results arise from different interventions, content categories, platforms, time periods, and outcome measures.

**Evidence**

- S10 compares default personalized ranking with reverse-chronological ordering and finds changed exposure without changed political attitudes. [S10]
- S1 holds the direction of content relative to users’ prior attitudes constant and asks whether algorithmic selection adds to the effect of like-minded exposure; it finds little general additional amplification. [S1]
- S9 targets the ranking of a specific category—anti-democratic and partisan-hostile content—and reports an affective-polarization effect during an election campaign. [S9]
- S7 compares different ranking objectives, including engagement-based and bridging-oriented algorithms, and reports different effects on polarization, consensus, and accuracy. [S7]

#### Finding 7

**Claim**

A major methodological reason for divergent findings is that algorithms and user preferences operate in a feedback loop, making observational evidence difficult to interpret.

**Confidence:** High

**Why this confidence level**

Both sources explicitly describe personalization, user choice, and network composition as important parts of the causal process.

**Evidence**

- Recommendations are shaped by users’ prior behavior, networks, and engagement, while recommendations then influence subsequent exposure and behavior. [S2] [S10]
- S10 notes that algorithmic ranking is only one component of the platform bundle; user choice and network composition also determine the content inventory available for ranking. [S10]

### Conflicts Found

- S10 found no significant change in polarization or political attitudes after replacing Facebook and Instagram’s algorithmic feeds with chronological feeds, whereas S9 reports that reranking hostile and anti-democratic content on X changed affective polarization. The results are conditional rather than necessarily incompatible: the interventions targeted different content, platforms, periods, and user experiences. [S9] [S10]
- S1 finds that algorithmic selection did not generally amplify the polarizing effect of like-minded content, while S7 reports more polarized and less accurate beliefs under engagement-based ranking and S9 reports changed partisan feelings under targeted hostile-content reranking. These studies estimate different effects of ranking objectives and content categories. [S1] [S7] [S9]
- S9 describes the X study as contradicting the Facebook/Instagram findings in S10, but the retrieved S9 material is partly expert commentary and emphasizes that the X result occurred during a highly polarized election period and over a short interval. The contradiction should therefore not be generalized to all recommendation systems. [S9] [S10]

### Important Gaps

- Do ranking-induced attitude changes persist beyond the short experimental periods?
- Do recommendation algorithms affect voting, turnout, political participation, political discussion, or offline hostility?
- How representative are browser-extension volunteers, platform users, and experimental samples?
- Which ranking features matter most: engagement optimization, partisan hostility, emotional intensity, ideological similarity, or repeated exposure?
- Do effects differ across platforms, countries, election periods, and users with different levels of prior partisan commitment?
- How do short-term attitude effects accumulate, dissipate, or interact with longer-term network and media use?

**Analysis Duration:** 18.72s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The runner reached the maximum research iteration budget. Analyzer assessment: The central distinction can now be answered well: algorithms clearly alter exposure and activity, while evidence for attitude effects is mixed and context-dependent. However, an important part of the original question—whether algorithms change concrete political behavior—remains unresolved. A focused search for randomized or quasi-experimental studies measuring voting, turnout, participation, or political discussion could materially improve the answer.

**Stop Reason:** max_iterations

---

# Final Research Decision

**Research Stopped Because**

The runner reached the maximum research iteration budget.

**Stop Reason:** max_iterations

**Searches Performed:** 3

**Unique Sources:** 10

**Remaining Uncertainty**

- Whether ranking-induced attitude changes persist beyond the short experimental periods.
- Whether recommendation algorithms affect voting, turnout, political participation, political discussion, or offline hostility.
- How representative browser-extension volunteers, platform users, and experimental samples are.
- Which features matter most: engagement optimization, partisan hostility, emotional intensity, ideological similarity, personalization, or repeated exposure.
- Whether effects differ across platforms, countries, election periods, and users with different levels of prior partisan commitment.
- How short-term effects accumulate, dissipate, or interact with longer-term network and media use.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 8.86s |
| OpenAI Analysis | 3 | 53.64s |
| Report Generation | 1 | 17.28s |
| Total Run | — | 79.79s |
