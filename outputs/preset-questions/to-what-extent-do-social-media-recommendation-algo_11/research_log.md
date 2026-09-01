# Research Run Log

## Run Summary

**System Version:** baseline-zero

**Research Question**

To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions.

**Status:** Completed

**Stop Reason:** sufficient_evidence

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 4 / 10

**Unique Sources:** 20

**OpenAI Calls:** 5

**Tavily Calls:** 4

**Started:** 2026-09-01T05:11:32-04:00

**Ended:** 2026-09-01T05:13:27-04:00

**Total Runtime:** 114.15s

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

- **S1 — Algorithms Shift Polarization. Why Does Policy Still Miss the Real ...**
  URL: https://www.techpolicy.press/algorithms-shift-polarization-why-does-policy-still-miss-the-real-problem
- **S2 — How Social Media and Embedded Recommender Algorithm ...**
  URL: https://commons.clarku.edu/cgi/viewcontent.cgi?article=1086&context=sps_masters_papers
- **S3 — How do beliefs and attitudes influence consumer behavior?**
  URL: https://findanyanswer.com/how-do-beliefs-and-attitudes-influence-consumer-behavior
- **S4 — How algorithmically curated online environments influence users’ political polarization: Results from two experiments with panel data**
  URL: https://www.sciencedirect.com/science/article/pii/S2451958823000763
- **S5 — The Influence of Social Media on Political Polarization – notesfromthehouse.co.za**
  URL: https://notesfromthehouse.co.za/the-influence-of-social-media-on-political-polarization

**Search Duration:** 5.35s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Algorithmic curation can change the political content users see, but exposure effects are not equivalent to algorithm effects.

**Confidence:** High

**Why this confidence level**

S4 directly describes two quasi-experiments designed to distinguish content exposure from algorithmic selection, although the evidence concerns constructed online environments and German participants rather than all platforms.

**Evidence**

- The 2023 panel experiments separately varied whether participants received like-minded or opposing arguments and whether selection was algorithmic or random. Like-minded exposure increased attitude and affective polarization, but algorithmic selection generally did not amplify that effect; it produced a small direct increase in attitude polarization for one topic. [S4]

#### Finding 2

**Claim**

There is evidence from a recent field experiment that changing the ranking of the same X-feed content can change affective political attitudes.

**Confidence:** Medium

**Why this confidence level**

The reported design and estimates are highly relevant causal evidence, but the retrieved material is a 2025 commentary summarizing the study rather than the primary Science article. The size, durability, generalizability, and exact outcome measures therefore remain unverified here.

**Evidence**

- According to S1’s account of a Science study, researchers reranked X feeds for 1,256 U.S. participants for one week during the 2024 campaign. Reducing exposure to content expressing partisan animosity and antidemocratic attitudes reportedly increased warmth toward the opposing party by 2.11 points on a 100-point scale, while increasing exposure reduced warmth by 2.48 points. [S1]
- S1 reports that the intervention changed ranking rather than the underlying users or available content, and that 74% of participants noticed no effect on their experience. [S1]

#### Finding 3

**Claim**

The strongest available evidence in this set concerns political attitudes—especially affective polarization—not political behavior such as voting, sharing, participation, or extremist action.

**Confidence:** High

**Why this confidence level**

None of the retrieved sources supplies convincing causal evidence about real-world political behavior.

**Evidence**

- S4 measures attitude polarization and affective polarization, not downstream political behavior. [S4]
- S1 describes changes in party warmth and political attitudes, but does not report voting, posting, sharing, turnout, or other behavioral outcomes. [S1]
- S2 frames polarization, manipulation, and populism as political concerns but presents a literature-oriented capstone overview rather than a clearly identified causal behavioral test. [S2]

#### Finding 4

**Claim**

Like-minded content exposure appears more consistently associated with polarization than the additional effect of algorithmic ranking itself.

**Confidence:** Medium

**Why this confidence level**

The sources use different designs, populations, platforms, interventions, and outcomes, so the apparent disagreement may be conditional rather than a direct replication conflict.

**Evidence**

- In S4, exposure to arguments consistent with participants’ prior attitudes produced stronger attitude and affective polarization than exposure to opposing arguments, while algorithmic selection did not generally amplify those effects. [S4]
- S1 presents a contrasting result in which changing ranking alone altered affective attitudes, suggesting that algorithmic effects may depend on the type of content amplified and the platform context. [S1] [S4]

#### Finding 5

**Claim**

The literature reaches different conclusions partly because studies conflate several mechanisms: users’ prior preferences, the content they encounter, ranking and recommendation rules, and broader social-media interaction dynamics.

**Confidence:** High

**Why this confidence level**

S4 provides a direct methodological explanation, while S1 and S2 support the broader distinction among mechanisms. The latter two are less rigorous as causal evidence.

**Evidence**

- S4 explicitly identifies failure to separate exposure to like-minded content from effects caused by algorithms as a reason for inconsistent prior findings. [S4]
- S2 describes recommender systems as grouping users by interests and facilitating political communication, but does not isolate recommendation effects from self-selection or social interaction. [S2]
- S1 distinguishes algorithmic amplification from malicious actors and communication conditions, and attributes polarization to their interaction rather than to ranking alone. [S1]

#### Finding 6

**Claim**

The retrieved evidence does not justify the broad claim that recommendation algorithms are the primary cause of political polarization; it supports a context-dependent, probably modest-to-meaningful contribution to attitudes under some ranking conditions.

**Confidence:** Medium

**Why this confidence level**

The direction and scale of effects are not fully comparable across the two sources, and the evidence base here is too narrow to estimate an overall contribution.

**Evidence**

- S4 finds mostly small or absent incremental algorithmic effects despite clear effects of like-minded exposure. [S4]
- S1 reports attitude changes of roughly 2 points on a 100-point scale after a one-week ranking intervention, while also arguing that repeated exposure at population scale could matter. [S1]

### Conflicts Found

- S1 portrays algorithmic ranking as directly causing meaningful movement in political attitudes, whereas S4 finds that algorithmic selection generally did not amplify polarization caused by like-minded content and had only a small direct effect for one topic. [S1] [S4]
- S5 makes broad claims that algorithms create echo chambers and that 55% of users became more extreme, but the retrieved text does not provide verifiable study details and these claims are not corroborated by the stronger experimental evidence in S4. [S5] [S4]
- S2 and S5 treat social-media recommender algorithms as broadly responsible for polarization, while S4 indicates that user-aligned exposure—not necessarily the algorithmic selection mechanism—may be the more important causal component. [S2] [S4] [S5]

### Important Gaps

- What are the exact methods, preregistration, sample composition, effect sizes, and durability of the Science study summarized by S1?
- Do algorithmic ranking changes affect political behavior—voting, turnout, political participation, sharing, following, or offline hostility—or mainly short-term attitudes?
- How representative are the findings across platforms, countries, political systems, topics, and recommendation systems?
- Are effects concentrated among particular users, such as highly engaged or already polarized users?
- How much of observed polarization reflects algorithmic amplification versus user self-selection, peer networks, partisan media, and offline political trends?
- Does repeated exposure over months or years produce cumulative effects, or do short-term attitude changes fade?

**Analysis Duration:** 17.78s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The central distinction can be answered provisionally: algorithms clearly affect what is ranked and can sometimes shift attitudes, but evidence that they change durable beliefs or political behavior is sparse in the retrieved material. A further search is needed for primary causal studies and behavioral outcomes, especially to verify S1 and determine whether effects persist.

**Next Search**

> primary causal studies algorithmic feed ranking political polarization beliefs behavior randomized experiment X Twitter Facebook recommendation

---

# Iteration 2

## 1. Search

**Query**

> primary causal studies algorithmic feed ranking political polarization beliefs behavior randomized experiment X Twitter Facebook recommendation

**Why this query**

The central distinction can be answered provisionally: algorithms clearly affect what is ranked and can sometimes shift attitudes, but evidence that they change durable beliefs or political behavior is sparse in the retrieved material. A further search is needed for primary causal studies and behavioral outcomes, especially to verify S1 and determine whether effects persist.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S6 — Algorithmic Amplification of Politics on...**
  URL: https://axi.lims.ac.uk/paper/2110.11010
- **S7 — How do social media feed algorithms affect attitudes and behavior in an election campaign? | Semantic Scholar**
  URL: https://www.semanticscholar.org/paper/How-do-social-media-feed-algorithms-affect-and-in-Guess-Malhotra/f48409576a7b05ec99dcc44429e655bcc6992bdb
- **S8 — Algorithmic amplification of politics on Twitter | PNAS**
  URL: https://www.pnas.org/doi/abs/10.1073/pnas.2025334119?af=R
- **S9 — Algorithmic amplification of politics on Twitter | PNAS**
  URL: https://www.pnas.org/doi/abs/10.1073/pnas.2025334119?cookieSet=1+
- **S10 — Algorithmic amplification of politics on Twitter | PNAS**
  URL: https://www.pnas.org/doi/abs/10.1073/pnas.2025334119?url_ver=Z39.88-2003

**Search Duration:** 5.54s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Twitter’s ranking algorithm changes the political content users see, including whose political messages receive greater visibility.

**Confidence:** High

**Why this confidence level**

The finding is based on a very large randomized platform experiment and is consistently reported across the primary-source versions, although the retrieved summary does not provide all methodological details.

**Evidence**

- A massive randomized experiment assigning nearly 2 million daily active accounts to a reverse-chronological, nonpersonalized feed found higher algorithmic amplification of mainstream right-wing political content than mainstream left-wing content in six of seven countries; U.S. right-leaning news sources were likewise favored. [S6] [S8] [S9] [S10]

#### Finding 2

**Claim**

Evidence that algorithms alter exposure does not by itself establish that they change political beliefs or behavior.

**Confidence:** High

**Why this confidence level**

The distinction follows directly from the outcomes described: amplification and exposure are measured separately from attitudinal or behavioral change.

**Evidence**

- The Twitter amplification study measures differential visibility of political parties and news sources, but the retrieved description does not report causal effects on users’ ideology, polarization, participation, or other political behavior. [S6] [S8] [S9] [S10]
- The earlier evidence in S4 found that like-minded content exposure increased polarization, while algorithmic selection generally did not add much beyond the content exposure itself. [S4]

#### Finding 3

**Claim**

A longer-term randomized comparison of algorithmic and chronological feeds found substantial effects on platform use but not detectable changes in several political attitudes over three months.

**Confidence:** Medium

**Why this confidence level**

This is highly relevant evidence about both behavior and attitudes, but the retrieved material is a Semantic Scholar summary rather than the study’s full primary text, and the exact sample, design, and statistical estimates are unavailable.

**Evidence**

- S7 reports that moving users out of algorithmic feeds substantially reduced time spent on the platforms and user activity, while the chronological feed did not significantly change issue polarization, affective polarization, political knowledge, or other key attitudes during the three-month study. [S7]

#### Finding 4

**Claim**

The new evidence strengthens the conclusion that algorithmic effects on political attitudes are context-dependent rather than uniformly large.

**Confidence:** Medium

**Why this confidence level**

The studies point in different directions, but they vary in platform intervention, content composition, duration, sample, and outcomes. They therefore support conditional effects more clearly than a single universal estimate.

**Evidence**

- S1 reports that reranking X content expressing partisan animosity and antidemocratic attitudes changed opposing-party warmth by roughly two points on a 100-point scale after a short field intervention. [S1]
- S7 reports no significant change in issue or affective polarization when users were moved to chronological feeds for three months. [S7]
- S4 found that like-minded exposure increased polarization, but algorithmic selection generally did not amplify that effect, aside from a small direct effect for one topic. [S4]

#### Finding 5

**Claim**

Algorithmic ranking may systematically advantage some political actors in visibility without necessarily driving users toward more extreme beliefs.

**Confidence:** Medium

**Why this confidence level**

The visibility result is strong, but the connection between partisan amplification and individual-level ideological change remains unestablished in the retrieved sources.

**Evidence**

- The Twitter experiment found greater amplification of mainstream right-wing content but explicitly found no evidence, in the retrieved summary, that far-left and far-right groups were amplified more than moderate groups. [S6]
- S7 reports no significant changes in issue or affective polarization from replacing algorithmic feeds with chronological feeds over three months. [S7]

#### Finding 6

**Claim**

The literature reaches different conclusions because studies manipulate or observe different causal components: the content shown, the ranking mechanism, users’ self-selection, and the broader interaction environment.

**Confidence:** High

**Why this confidence level**

The studies clearly differ in estimand, intervention, duration, platform context, and outcome, providing a direct methodological explanation for apparently inconsistent results.

**Evidence**

- S4 directly distinguishes exposure to like-minded or opposing arguments from whether selection was algorithmic or random, finding stronger effects for content alignment than for algorithmic selection itself. [S4]
- S1 reranked a feed specifically to alter exposure to partisan animosity and antidemocratic attitudes, whereas S7 compared algorithmic and chronological feeds without the same targeted content manipulation. [S1] [S7]
- S6 measures platform-wide amplification differences across political groups and countries rather than individual changes in beliefs or behavior. [S6] [S8] [S9] [S10]

### Conflicts Found

- S1 reports that changing the ranking of the same X-feed environment altered affective political attitudes, whereas S7 reports that replacing algorithmic feeds with chronological feeds did not significantly alter issue or affective polarization over three months. [S1] [S7]
- S4 finds that like-minded exposure was more consequential than the algorithmic selection mechanism itself, while S1 finds a direct attitude effect from targeted reranking. This is a conditional disagreement rather than a clean contradiction because the interventions and content differed. [S1] [S4]
- S6 shows systematic partisan differences in content amplification, but the retrieved evidence does not show that this visibility asymmetry produced corresponding changes in users’ beliefs or political behavior. [S6] [S8] [S9] [S10]

### Important Gaps

- Does algorithmic ranking affect concrete political behavior such as voting, turnout, political donations, political participation, sharing, following, or offline hostility?
- Are the attitude effects reported by S1 durable beyond the short intervention, and how do they compare with the null attitude effects in S7?
- What exact outcomes, sample characteristics, and statistical estimates underlie the S7 three-month study?
- Do the amplification asymmetries identified in S6 translate into population-level changes in political attitudes or electoral outcomes?
- How much do effects vary by platform, country, political topic, user engagement, and preexisting polarization?
- Do algorithmic effects accumulate over months or years, or do short-term changes fade?

**Analysis Duration:** 17.08s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The central exposure question is now supported by strong evidence that ranking changes political visibility. There is also meaningful but conflicting evidence on attitudes. However, the original question explicitly asks about political behavior, and the retrieved sources provide no convincing causal evidence for downstream real-world behavior. A focused search for randomized studies measuring behavioral outcomes would materially improve the answer.

**Next Search**

> randomized field experiment social media feed algorithm political behavior voting participation sharing turnout

---

# Iteration 3

## 1. Search

**Query**

> randomized field experiment social media feed algorithm political behavior voting participation sharing turnout

**Why this query**

The central exposure question is now supported by strong evidence that ranking changes political visibility. There is also meaningful but conflicting evidence on attitudes. However, the original question explicitly asks about political behavior, and the retrieved sources provide no convincing causal evidence for downstream real-world behavior. A focused search for randomized studies measuring behavioral outcomes would materially improve the answer.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S11 — How do social media feed algorithms affect attitudes and ...**
  URL: https://cdr.lib.unc.edu/downloads/wp9891401
- **S12 — Null effects of social media ads on voter registration**
  URL: https://journals.sagepub.com/doi/abs/10.1177/20531680231225316
- **S13 — The political effects of X’s feed algorithm**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC13061628
- **S14 — Research shows social media advertising suppresses voting in targeted communities – UW–Madison News**
  URL: https://news.wisc.edu/research-shows-social-media-advertising-suppresses-voting-in-targeted-communities
- **S15 — Social Drivers and Algorithmic Mechanisms on Digital Media**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11373151

**Search Duration:** 3.57s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The strongest direct evidence that feed algorithms change what users see comes from randomized comparisons of algorithmic and chronological feeds.

**Confidence:** High

**Why this confidence level**

S11 reports a randomized platform experiment with direct exposure measures, and the X result is based on a very large randomized experiment. These establish changes in visibility and content composition, not by themselves changes in beliefs.

**Evidence**

- In a randomized 2020 election experiment on Facebook and Instagram, replacing machine-learning ranking with reverse chronology substantially changed exposure: political and untrustworthy content increased on both platforms, while Facebook users saw less uncivil/slur content and more content from moderate friends and ideologically mixed sources. [S11]
- The large X amplification experiment found that algorithmic ranking gave greater visibility to mainstream right-wing political content than mainstream left-wing content in six of seven countries, including greater amplification of right-leaning U.S. news sources. [S6] [S8] [S9] [S10]

#### Finding 2

**Claim**

Changing algorithmic ranking can affect political attitudes, but the evidence is inconsistent across platforms and interventions.

**Confidence:** Medium

**Why this confidence level**

The new S13 evidence is highly relevant but only an abstract is available here, while the S1 account is secondary. S11 and S4 provide comparatively detailed null or limited-effect findings. Together they support conditional rather than uniform effects.

**Evidence**

- A 2023 X field experiment randomly assigned U.S. users to algorithmic or chronological feeds for seven weeks and reports that switching to the algorithmic feed increased engagement and shifted political opinion toward more conservative positions. [S13]
- A separate X reranking experiment reported that reducing exposure to partisan animosity and antidemocratic content increased warmth toward the opposing party by 2.11 points on a 100-point scale, while increasing such exposure reduced warmth by 2.48 points after one week. [S1]
- In contrast, the Facebook and Instagram experiment found no significant change in issue polarization, affective polarization, political knowledge, or other key attitudes over three months, despite substantial changes in exposure and platform activity. [S11]
- Quasi-experiments separating content alignment from algorithmic selection found that like-minded exposure increased attitude and affective polarization, whereas algorithmic selection generally did not add much; one small direct effect appeared for one topic. [S4]

#### Finding 3

**Claim**

Algorithmic ranking has been shown to change on-platform behavior, especially engagement and time spent, but evidence for broader political behavior remains limited.

**Confidence:** High

**Why this confidence level**

The experiments directly measure platform use or engagement, while the absence of reported downstream political outcomes is clear in the retrieved material. It would be inappropriate to equate engagement changes with political behavior change.

**Evidence**

- Moving users from algorithmic to chronological feeds on Facebook and Instagram substantially reduced time spent on the platforms and user activity. [S11]
- The X study reports that algorithmic feeds increased engagement relative to chronological feeds. [S13]
- The retrieved evidence from these feed experiments does not establish effects on voting, turnout, donations, sharing, following, offline hostility, or other consequential political behavior. [S11] [S13] [S6] [S8] [S9] [S10]

#### Finding 4

**Claim**

Evidence of political behavior effects exists for targeted social-media advertising, but it should not be attributed directly to recommendation algorithms.

**Confidence:** Medium

**Why this confidence level**

The reported outcome is concrete political behavior, but this is a different mechanism from recommendation ranking and the retrieved item is a university news account rather than the primary study.

**Evidence**

- A report on a study of more than 10,000 U.S. participants states that exposure to Facebook vote-suppressing advertisements was associated with a 1.9-percentage-point reduction in actual turnout, using voter records; the messages were microtargeted to particular communities. [S14]
- The intervention concerned targeted political advertisements and their delivery, not the ranking of users’ ordinary social-media feeds. The source also describes exposure-turnout matching rather than a randomized feed-ranking experiment. [S14]

#### Finding 5

**Claim**

The overall contribution of recommendation algorithms to polarization appears real in some settings but is not established as the primary or universal cause of polarization.

**Confidence:** Medium

**Why this confidence level**

The evidence is experimentally informative but heterogeneous in platform, country, duration, content, outcome, and algorithmic manipulation. It supports a context-dependent contribution, not a single aggregate effect size.

**Evidence**

- S11 found large exposure and activity changes without detectable changes in polarization-related attitudes over three months. [S11]
- S4 found that like-minded content exposure was more consistently polarizing than the additional algorithmic-selection mechanism. [S4]
- S1 and S13 report attitude shifts from algorithmic changes on X, indicating that ranking can matter when it changes exposure to particular political or antagonistic content. [S1] [S13]
- A review argues that algorithms and social drivers operate in a feedback loop and that existing evidence suggests algorithms mostly reinforce preexisting social drivers rather than acting independently. [S15]

#### Finding 6

**Claim**

Different conclusions in the literature arise because studies estimate different causal quantities and manipulate different parts of the media environment.

**Confidence:** High

**Why this confidence level**

The sources directly document differences in intervention, estimand, duration, platform, content, and outcome, providing a strong explanation for apparently conflicting results.

**Evidence**

- S11 distinguishes feed-ranking effects from users’ network composition, user choice, resharing, and other features bundled into ‘social media’ studies. [S11]
- S4 separately varies like-minded versus opposing content and algorithmic versus random selection, finding stronger effects for content alignment than for algorithmic selection itself. [S4]
- S1 targets ranking of content expressing partisan animosity and antidemocratic attitudes, whereas S11 replaces personalized ranking with chronology without targeting a specific type of political content. [S1] [S11]
- S6 measures population-level visibility asymmetries across political actors and countries, not individual-level belief or behavioral change. [S6] [S8] [S9] [S10]
- S15 describes algorithms as embedded in feedback loops with existing social drivers, making self-selection and prior attitudes difficult to separate from algorithmic effects. [S15]

### Conflicts Found

- S13 reports that algorithmic X feeds shifted political opinion toward more conservative positions, whereas S11 found no detectable change in polarization-related attitudes after replacing Facebook and Instagram algorithms with chronological feeds for three months. [S13] [S11]
- S1 reports an affective-attitude effect from targeted reranking on X, while S4 finds that algorithmic selection generally added little beyond exposure to like-minded content. [S1] [S4]
- S6 documents partisan asymmetry in visibility, but the retrieved evidence does not show that this asymmetry caused corresponding changes in individual beliefs or political behavior. [S6] [S8] [S9] [S10]
- S14 reports a turnout effect from targeted vote-suppressing advertisements, but this does not directly conflict with null feed-ranking studies because advertising microtargeting and recommendation ranking are different interventions. [S14] [S11] [S13]

### Important Gaps

- What are the full methods, effect sizes, sample characteristics, and behavioral outcomes in the seven-week X experiment reported by S13?
- Are the X attitude shifts durable, and do they reflect general ideological movement, affective polarization, or particular issue opinions?
- Do ranking-induced changes in exposure translate into voting, turnout, sharing, following, donations, or offline political hostility?
- Why do X experiments report attitude effects while the Facebook/Instagram experiment reports null effects: platform design, content mix, baseline feed, user population, timing, or outcome measurement?
- Are effects concentrated among highly engaged or already polarized users?
- Do repeated ranking effects accumulate over months or years, or do short-term changes fade?
- How generalizable are these findings across countries, election periods, platforms, and recommendation systems?

**Analysis Duration:** 19.01s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The new evidence materially improves the exposure-versus-attitude distinction, and S11 provides a primary-source account of the major Meta null result. However, S13 is only represented by an abstract excerpt and may substantially change the synthesis because it reports a direct X attitude effect. Full results are needed to compare its estimand and magnitude with S11, S4, and S1.

**Next Search**

> Gauthier Hodler Widmer Zhuravskaya political effects X feed algorithm 2023 field experiment full results conservative attitudes chronological feed

---

# Iteration 4

## 1. Search

**Query**

> Gauthier Hodler Widmer Zhuravskaya political effects X feed algorithm 2023 field experiment full results conservative attitudes chronological feed

**Why this query**

The new evidence materially improves the exposure-versus-attitude distinction, and S11 provides a primary-source account of the major Meta null result. However, S13 is only represented by an abstract excerpt and may substantially change the synthesis because it reports a direct X attitude effect. Full results are needed to compare its estimand and magnitude with S11, S4, and S1.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S16 — The political effects of X's feed algorithm. - Abstract**
  URL: https://pubmed.ncbi.nlm.nih.gov/41708846
- **S17 — Ekaterina Zhuravskaya and Philine Widmer published in ...**
  URL: https://www.parisschoolofeconomics.eu/en/news/ekaterina-zhuravskaya-and-philine-widmer-published-in-nature-a-study-on-the-influence-of-xs-algorithm
- **S18 — How X's algorithm shifts political attitudes**
  URL: https://cepr.org/voxeu/columns/how-xs-algorithm-shifts-political-attitudes
- **S19 — The political effects of X's feed algorithm**
  URL: https://www.nature.com/articles/s41586-026-10098-2
- **S20 — Social sciences: X’s algorithm may influence political attitudes (Nature) | Nature Portfolio**
  URL: https://www.natureasia.com/en/info/press-releases/detail/9242

**Search Duration:** 5.59s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The strongest new evidence indicates that X’s feed algorithm can change both users’ exposure and some political attitudes, but not all forms of polarization.

**Confidence:** High

**Why this confidence level**

S16 is a primary-source abstract indexed by PubMed/Europe PMC, and S19 provides the corresponding Nature article. The design directly randomizes feed type and measures political attitudes, though the retrieved full text is only partially available.

**Evidence**

- A randomized 2023 field experiment assigned active U.S. X users to algorithmic or chronological feeds for approximately seven weeks. Turning on the algorithm increased engagement and shifted opinions toward more conservative policy priorities, views about criminal investigations into Donald Trump, and views on the war in Ukraine. [S16] [S19]
- The same study found no significant effect on affective polarization or self-reported partisanship, distinguishing issue-attitude change from broader partisan identity or interparty affect. [S16]

#### Finding 2

**Claim**

X’s algorithm changes the political content users encounter in a politically directional way.

**Confidence:** High

**Why this confidence level**

The new X field experiment combines randomized feed assignment with observed feed-content data, while the prior amplification study used a very large randomized platform experiment.

**Evidence**

- Feed-content analysis found that the algorithm promoted conservative content and demoted posts from traditional media outlets. [S16] [S19]
- The large X amplification experiment independently found greater visibility for mainstream right-wing political content than mainstream left-wing content in six of seven countries, including the United States. [S6] [S8] [S9] [S10]

#### Finding 3

**Claim**

The X study supplies direct causal evidence that altered exposure can affect political beliefs or preferences, not merely what appears in the feed.

**Confidence:** High

**Why this confidence level**

Political-attitude outcomes were measured under randomized feed assignment. The evidence supports effects on selected opinions, but not a blanket claim that the algorithm increases all dimensions of polarization.

**Evidence**

- Users assigned from chronological to algorithmic feeds moved toward more conservative policy priorities and changed views on several political issues; the abstract attributes these effects to exposure to algorithmically promoted content. [S16]
- The effects were not equivalent to a generalized change in partisanship or affective polarization: neither outcome changed significantly. [S16]

#### Finding 4

**Claim**

Algorithmic exposure can also alter online political behavior, especially engagement and following, with some persistence after the algorithm is removed.

**Confidence:** High

**Why this confidence level**

These outcomes were directly measured in the randomized field experiment. However, following accounts and engagement are on-platform behaviors, not evidence of effects on voting, turnout, offline activism, or other consequential political behavior.

**Evidence**

- Algorithmic-feed assignment increased platform engagement and led users to follow more conservative political activist accounts. [S16] [S19] [S20]
- Users who later switched from algorithmic to chronological feeds did not show comparable reversals in views or following behavior, suggesting that at least some effects persisted after the intervention ended. [S16] [S20]

#### Finding 5

**Claim**

The new study helps explain why switching off an algorithm may produce null results even if turning it on can have effects.

**Confidence:** High

**Why this confidence level**

The asymmetry and proposed mechanism are explicitly reported in the primary-source abstract and Nature-related materials.

**Evidence**

- The study found an asymmetry: switching from chronological to algorithmic feeds changed opinions and behavior, whereas switching from algorithmic to chronological feeds produced no comparable effects. [S16] [S19] [S20]
- The authors’ mechanism analysis indicates that initial algorithmic exposure promoted conservative activist accounts that users continued to follow after returning to a chronological feed, so the later control condition may not restore the original information environment. [S16] [S19]

#### Finding 6

**Claim**

The literature’s apparent disagreement is substantially conditional rather than a simple contradiction.

**Confidence:** High

**Why this confidence level**

The interventions, platforms, durations, content environments, populations, and outcome measures differ clearly across the studies.

**Evidence**

- The X experiment targeted an existing platform algorithm that promoted particular political content and found issue-attitude and following effects, while the Facebook/Instagram experiment found large exposure and activity changes but no detectable changes in issue or affective polarization over three months. [S16] [S11]
- Other experiments found that exposure to like-minded arguments was more consistently polarizing than whether selection was algorithmic rather than random, with only a small direct algorithmic effect for one topic. [S4]
- The studies therefore estimate different quantities: directional content amplification, the effect of switching feed systems, the effect of like-minded content itself, and different outcomes such as issue opinions, affective polarization, partisanship, engagement, and following. [S4] [S11] [S16]

#### Finding 7

**Claim**

Recommendation algorithms are best characterized as contributors to polarization under particular content and platform conditions, not as the universal or primary cause of political polarization.

**Confidence:** High

**Why this confidence level**

The conclusion is supported by multiple experimental patterns and is appropriately narrower than the claim that algorithms generally create polarization.

**Evidence**

- X evidence now shows that algorithmic ranking can produce conservative shifts in selected political opinions and changes in following behavior, while leaving affective polarization and self-reported partisanship unchanged. [S16]
- Facebook/Instagram and other studies found substantial exposure changes with null or limited effects on polarization-related attitudes, and like-minded content often appeared more consequential than the algorithmic selection mechanism alone. [S11] [S4]
- A review describes algorithms as operating in feedback loops with preexisting social drivers rather than independently generating polarization. [S15]

### Conflicts Found

- The new primary X study reports shifts toward conservative policy opinions, whereas the Facebook/Instagram feed experiment found no detectable changes in issue or affective polarization. This is a cross-platform and intervention disagreement, not necessarily a direct replication failure. [S16] [S11]
- The X study finds direct effects from feed assignment, while S4 finds that like-minded exposure generally matters more than the additional algorithmic-selection mechanism. The difference may reflect X’s specific content ranking and activist-account dynamics versus S4’s constructed exposure experiment. [S16] [S4]
- The new source reports no significant effect on affective polarization or self-reported partisanship despite shifts in policy opinions. Thus evidence for belief change is stronger for selected issue attitudes than for generalized partisan polarization. [S16]
- Prior material described the X study through secondary accounts and gave a sample of 1,256 participants, while the primary-source materials report nearly 5,000 users (4,965 in S20). The participant count and exact study reporting should therefore be treated according to S16/S19/S20, with the earlier figure considered unresolved or potentially referring to a subgroup. [S1] [S16] [S19] [S20]

### Important Gaps

- Whether the X-induced opinion shifts persist over substantially longer periods and whether they affect voting, turnout, donations, political participation, sharing, or offline hostility.
- Why X produces detectable issue-attitude effects while Meta studies produce mostly null polarization effects: possible explanations include platform design, content mix, baseline feeds, user populations, timing, or outcome measurement.
- Whether the findings generalize beyond active U.S. X users, the 2023 political context, and the specific algorithmic ranking system studied.
- Whether effects are concentrated among highly engaged, initially conservative, or already polarized users.
- Whether the observed conservative shift represents ideological persuasion, changes in issue salience, selective following, or some combination of these processes.

**Analysis Duration:** 18.49s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The new primary Nature study materially resolves the most important earlier gap: it verifies the X experiment’s randomized design, sample scale, attitude outcomes, behavioral outcomes, content mechanism, and asymmetry between turning the algorithm on and off. Together with S4, S11, and the amplification experiments, the evidence supports a responsible answer: algorithms clearly alter exposure; they can alter selected political opinions and on-platform following or engagement in some settings; but effects on generalized polarization and consequential political behavior remain limited or unestablished. Further research would improve generalizability, but is not necessary to answer the original question responsibly.

**Stop Reason:** sufficient_evidence

---

# Final Research Decision

**Research Stopped Because**

The analyzer determined that the important parts of the question could be answered responsibly.

**Stop Reason:** sufficient_evidence

**Searches Performed:** 4

**Unique Sources:** 20

**Remaining Uncertainty**

- Whether recommendation-induced changes affect voting, turnout, donations, political participation, sharing, or offline hostility.
- Why X produces detectable issue-attitude effects while Facebook/Instagram studies produce mostly null polarization effects; possible explanations include platform design, content mix, baseline feeds, user populations, timing, and outcome measurement.
- Whether the X-induced opinion and following changes persist over substantially longer periods.
- Whether effects are concentrated among highly engaged, initially conservative, or already polarized users.
- How generalizable the findings are beyond active U.S. X users, the specific 2023 political context, and the particular recommendation systems studied.
- Whether observed conservative shifts reflect persuasion, changes in issue salience, selective following, or a combination of mechanisms.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 4 | 20.05s |
| OpenAI Analysis | 4 | 72.36s |
| Report Generation | 1 | 21.73s |
| Total Run | — | 114.15s |
