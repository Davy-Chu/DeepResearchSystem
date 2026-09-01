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

**Unique Sources:** 16

**OpenAI Calls:** 5

**Tavily Calls:** 4

**Started:** 2026-09-01T06:33:01-04:00

**Ended:** 2026-09-01T06:34:33-04:00

**Total Runtime:** 92.03s

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

- **S1 — Social Media Algorithms: Impact on Political Polarization and Engagement**
  URL: https://latunisievote.org/social-media-algorithms-political-polarization-information-spread-and-user-engagement
- **S2 — The Impact of Social Media Algorithms on Political Polarization » boslabour.org.uk**
  URL: https://boslabour.org.uk/the-impact-of-social-media-algorithms-on-political-polarization
- **S3 — The Impact Of Social Media Algorithms On Information Bubbles And Political Polarization. - Consensus Academic Search Engine**
  URL: https://consensus.app/questions/impact-social-media-algorithms-information-bubbles
- **S4 — Deep dive into Meta’s algorithms shows that America’s political polarization has no easy fix – The Denver Post**
  URL: https://www.denverpost.com/2023/07/27/deep-dive-into-metas-algorithms-shows-that-americas-political-polarization-has-no-easy-fix
- **S5 — Polarization And Meta's Algorithms: New Research**
  URL: https://www.genocidewatch.com/single-post/research-on-facebook-s-algorithms-and-polarization-published

**Search Duration:** 4.17s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Recommendation algorithms clearly change users’ on-platform information environments, including the amount and ideological composition of political content they encounter.

**Confidence:** High

**Why this confidence level**

S4 and S5 independently reproduce reporting on large-scale studies using millions of users and experimental algorithm changes. The precise causal effects on exposure are directly described, although the material is secondary reporting rather than the primary papers.

**Evidence**

- A large set of Facebook and Instagram studies found that algorithms were highly influential in users’ on-platform experiences and that political news exposure was substantially ideologically segregated. [S4] [S5]
- The reported studies found that disabling Facebook’s reshare feature reduced exposure to political news and untrustworthy sources, while eliminating algorithmic ranking substantially reduced time spent on Facebook and Instagram. [S4] [S5]
- The sources describe personalization and engagement-based ranking as mechanisms that prioritize content related to users’ past interactions and preferences, potentially narrowing exposure to opposing views. [S1] [S2] [S3]

#### Finding 2

**Claim**

Evidence that algorithmic changes directly alter political beliefs, affective polarization, extremist views, or related behavior is substantially weaker and, in the reported 2020 Facebook experiments, largely null.

**Confidence:** High

**Why this confidence level**

The same reported experimental evidence consistently distinguishes strong effects on exposure from weak or absent effects on measured attitudes and polarization.

**Evidence**

- Replacing Facebook’s ranked feed with a chronological feed produced no measurable change in polarization. [S4] [S5]
- Reducing content from ideologically aligned accounts had no significant effect on polarization, susceptibility to misinformation, or extremist views. [S4] [S5]
- Turning off resharing changed what users saw but did not significantly change their political attitudes. [S4] [S5]
- The reported studies concluded that popular proposals to modify Facebook’s algorithms did not sway political attitudes, despite substantially changing users’ platform experiences. [S4] [S5]

#### Finding 3

**Claim**

Algorithms may contribute to polarization indirectly by making it easier for users to pursue politically congenial information, but the available sources do not establish that algorithms are a primary cause of broad political polarization.

**Confidence:** Medium

**Why this confidence level**

The mechanism is plausible and supported by descriptive evidence, but the retrieved material does not isolate algorithms from user selection, partisan media ecosystems, offline networks, or prior beliefs.

**Evidence**

- The researchers’ interpretation was that users seek content aligned with their views and algorithms facilitate that behavior rather than necessarily creating the underlying preferences. [S4] [S5]
- The sources report ideological echo chambers and divergent information sources among conservatives and liberals, but these patterns coexist with evidence that algorithmic interventions did not shift attitudes. [S4] [S5]
- Several sources emphasize reciprocal reinforcement between personalization, engagement, selective exposure, and users’ own choices. [S1] [S2] [S3]

#### Finding 4

**Claim**

The literature reaches different conclusions partly because it asks different causal questions and uses different designs: exposure studies often measure what appears in feeds, whereas belief studies require observing changes in attitudes or behavior after an intervention.

**Confidence:** High

**Why this confidence level**

This methodological distinction is explicit in the experimental findings and is consistent with the contrast between descriptive/mechanistic claims in S1–S3 and intervention results in S4–S5.

**Evidence**

- The reported Meta studies found strong effects on on-platform experience and ideological segregation but no meaningful effects on political attitudes, directly illustrating the distinction between exposure and persuasion. [S4] [S5]
- The review-like sources infer polarization from echo chambers, selective exposure, and ideological clustering, while the experimental evidence tests whether changing ranking or sharing features changes attitudes. [S1] [S2] [S3] [S4] [S5]
- The sources indicate that users’ pre-existing beliefs and selective exposure may confound observational associations between algorithmic feeds and polarization. [S3] [S4] [S5]

#### Finding 5

**Claim**

The strongest current conclusion is that algorithms have a substantial role in shaping political visibility and information flows, but their incremental causal effect on political beliefs or behavior appears limited in the short-run interventions studied; long-run and cross-platform effects remain uncertain.

**Confidence:** Medium

**Why this confidence level**

The short-run null results are well supported in the retrieved reporting, but the evidence gap concerning cumulative, cross-platform, and non-election effects is explicitly unresolved.

**Evidence**

- The studies covered only several months around the 2020 election and therefore could not assess cumulative effects from years of algorithmic exposure. [S4] [S5]
- The reported studies focused on Facebook and Instagram, while users also obtain information from television, radio, other websites, word of mouth, TikTok, and YouTube. [S4] [S5]
- Critics cited in the reporting argued that the studies were a snapshot and did not capture possible effects of years of misinformation or broader platform dynamics. [S4] [S5]

### Conflicts Found

- S1–S3 present algorithmic personalization, echo chambers, and engagement optimization as contributing to increased polarization, sometimes implying that algorithmic filtering itself increases ideological division. S4–S5 report large-scale experiments in which changing ranking, resharing, or ideological alignment had little or no effect on measured polarization or attitudes. [S1] [S2] [S3] [S4] [S5]
- The disagreement is partly conditional rather than strictly contradictory: algorithms may strongly alter exposure and facilitate selective exposure, while producing little detectable short-term change in beliefs when users already hold strong preferences and can obtain political information through other channels. [S3] [S4] [S5]
- S1–S3 rely heavily on broad summaries and secondary or aggregator material, whereas S4–S5 report findings from large studies published in Science and Nature but still provide those findings through news coverage rather than the primary articles. [S1] [S2] [S3] [S4] [S5]

### Important Gaps

- Do algorithmic effects accumulate over years, rather than appearing in short intervention windows around one election?
- Do recommendation systems affect political participation, voting, sharing, donations, protest, or hostility differently from ideological attitudes?
- How much of observed polarization is caused by ranking algorithms versus users’ intentional choices, partisan media supply, social networks, and offline political conditions?
- Do results from Facebook and Instagram generalize to TikTok, YouTube, X, or recommendation systems outside the United States?
- What were the exact outcomes, treatment designs, effect sizes, and statistical limitations in the underlying Science and Nature papers?

**Analysis Duration:** 17.87s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

A further search would materially improve the answer by retrieving the primary Science and Nature studies behind S4–S5. The current evidence supports a strong exposure-versus-belief distinction, but precise effect sizes, behavioral outcomes, study limitations, and whether the null results extend beyond the 2020 Facebook/Instagram interventions remain unclear.

**Next Search**

> 2023 Science Nature Facebook Instagram algorithm ranking experiment political polarization attitudes chronological feed resharing primary studies

---

# Iteration 2

## 1. Search

**Query**

> 2023 Science Nature Facebook Instagram algorithm ranking experiment political polarization attitudes chronological feed resharing primary studies

**Why this query**

A further search would materially improve the answer by retrieving the primary Science and Nature studies behind S4–S5. The current evidence supports a strong exposure-versus-belief distinction, but precise effect sizes, behavioral outcomes, study limitations, and whether the null results extend beyond the 2020 Facebook/Instagram interventions remain unclear.

**Results**

5 results retrieved.

5 new unique sources added.

### Sources

- **S6 — Science and Nature studies on Facebook show algorithm not only problem**
  URL: https://www.cnbc.com/2023/07/27/science-and-nature-studies-on-facebook-show-algorithm-not-only-problem.html
- **S7 — The Role of Social Media Algorithms in Shaping Political ...**
  URL: https://www.humanrightsresearch.org/post/the-role-of-social-media-algorithms-in-shaping-political-polarisation-in-the-united-states
- **S8 — The political effects of X’s feed algorithm**
  URL: https://www.nature.com/articles/s41586-026-10098-2
- **S9 — How do social media feed algorithms affect attitudes and ...**
  URL: https://cdr.lib.unc.edu/downloads/wp9891401
- **S10 — New study shows just how Facebook's algorithm shapes politics : NPR**
  URL: https://www.npr.org/2023/07/27/1190383104/new-study-shows-just-how-facebooks-algorithm-shapes-conservative-and-liberal-bub

**Search Duration:** 2.14s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new evidence strengthens the distinction between changing exposure and changing political beliefs: Facebook’s algorithm substantially changed users’ feeds and on-platform activity, but a three-month randomized intervention did not measurably change polarization or political attitudes.

**Confidence:** High

**Why this confidence level**

S9 is the underlying study text and directly describes both exposure and outcome measures; S10 independently summarizes the same distinction.

**Evidence**

- The primary study reports that replacing Facebook and Instagram’s algorithmic feeds with reverse-chronological feeds changed time spent, activity, political and untrustworthy-content exposure, exposure to moderate and ideologically mixed sources, and some uncivil content; nevertheless, it did not significantly change issue polarization, affective polarization, political knowledge, or other key attitudes during the three-month study. [S9]
- NPR reports that the Facebook/Instagram studies found substantial changes in what users saw and how they behaved on the platforms without detectable belief changes during the study period. [S10]

#### Finding 2

**Claim**

The Facebook evidence indicates substantial ideological segregation in political-news exposure, but segregation alone does not demonstrate that the ranking algorithm caused users’ political beliefs to become more polarized.

**Confidence:** Medium

**Why this confidence level**

The exposure patterns are large-scale and directly reported, but the retrieved material does not isolate algorithmic ranking from users’ networks, follows, clicks, and selective engagement.

**Evidence**

- A study of 208 million U.S. Facebook adults found limited overlap in political-news consumption between liberals and conservatives, with segregation increasing from algorithmic selection to user exposure to user interaction. [S10]
- The Nature study reported that the average Facebook user received about half of visible content from people, pages, or groups sharing the user’s beliefs. [S6]

#### Finding 3

**Claim**

The literature’s apparently conflicting conclusions are partly platform- and intervention-dependent: Facebook’s 2020 feed-ranking intervention produced null short-run attitude effects, whereas a later randomized X experiment reportedly found that enabling X’s algorithmic feed shifted political opinions in a more conservative direction while not substantially changing partisanship or polarization.

**Confidence:** Medium

**Why this confidence level**

The X result is supported by the primary article’s abstract and secondary reporting, but the retrieved primary text is truncated before the full results and does not provide effect sizes, outcome construction, or all design details.

**Evidence**

- The 2026 Nature abstract states that randomly assigning active U.S.-based X users to algorithmic or chronological feeds for seven weeks measured political attitudes and online behavior, and that switching to the algorithmic feed increased engagement and shifted political opinion toward more conservative positions. [S8]
- A secondary account of the X study says the shift affected policy and current-affairs opinions but did not majorly affect partisanship or polarization; it also reports increased promotion of conservative activist content and reduced visibility of traditional news sources. [S7]
- The Facebook/Instagram primary study found no significant change in issue polarization, affective polarization, political knowledge, or other key attitudes after three months with chronological feeds. [S9]

#### Finding 4

**Claim**

Algorithms should not be treated either as the sole cause of polarization or as merely passive mirrors of user preference; the evidence supports an interaction between platform ranking, the content inventory generated by users’ networks, and users’ own choices.

**Confidence:** High

**Why this confidence level**

The interaction is directly articulated in the primary Facebook study and is consistent with the reporting and descriptive synthesis, though its contribution to long-run societal polarization remains unmeasured.

**Evidence**

- The Facebook study describes algorithmic ranking as operating on content generated by users’ social connections and notes that user choice and network composition may matter independently of the ranking algorithm. [S9]
- The Facebook/Instagram reporting says users often seek information consistent with existing beliefs, making echo chambers easier to inhabit, while changing algorithmic ranking still changes the content and activity users experience. [S6] [S10]
- The review-style source describes a feedback loop in which users select congenial accounts and engagement, and algorithms learn from those behaviors and rank accordingly. [S7]

#### Finding 5

**Claim**

The overall answer is now more qualified: recommendation algorithms clearly contribute to political visibility, segregation, and engagement patterns, but their causal contribution to beliefs or political behavior is heterogeneous and cannot be summarized as uniformly polarization-increasing.

**Confidence:** High

**Why this confidence level**

The conclusion follows from convergent evidence that exposure effects are robust while downstream effects vary by platform and outcome; important long-term and behavioral outcomes remain absent.

**Evidence**

- Facebook/Instagram experiments show large exposure and activity effects but null short-run attitude effects. [S9]
- The X experiment reports a directional shift in political opinions without a major change in polarization or partisanship. [S8] [S7]
- The retrieved sources do not establish effects on voting, participation, donations, protest, offline relationships, or long-term cumulative polarization. [S7] [S8] [S9] [S10]

### Conflicts Found

- The Facebook/Instagram experiments found no significant short-run changes in polarization or attitudes after replacing algorithmic feeds, while the X experiment reports a conservative shift in political opinions after enabling an algorithmic feed. These are not necessarily direct contradictions because they involve different platforms, algorithms, periods, treatment directions, and outcomes; the X result reportedly did not substantially change polarization itself. [S8] [S9]
- Descriptive accounts characterize ideological segregation and algorithmic prioritization as mechanisms that may intensify polarization, whereas randomized Facebook evidence shows that changing ranking can alter exposure without changing measured attitudes. The disagreement is between a mechanism or opportunity claim and a demonstrated persuasion claim. [S6] [S7] [S9] [S10]
- S7 makes broad claims about algorithmically amplified antagonistic content and belief reinforcement, but much of its supporting material is cited secondhand and the page is dated August 2026; these claims are weaker than the directly retrieved primary-study evidence. [S7] [S8] [S9]

### Important Gaps

- What are the complete effect sizes, confidence intervals, treatment compliance rates, and subgroup effects in the X experiment?
- Why did X’s algorithmic feed shift policy opinions while apparently not changing overall partisanship or polarization?
- Are the Facebook and X results driven by differences in recommendation objectives, network structure, content supply, user populations, or political context?
- Do recommendation algorithms affect concrete political behavior—voting, participation, sharing, donations, protest, or hostility—even when standard polarization measures do not change?
- Do exposure effects accumulate over years or generalize across TikTok, YouTube, Instagram Reels, and other recommendation systems?
- How much of ideological segregation is produced by ranking versus prior beliefs, follows, social networks, and active user choice?

**Analysis Duration:** 16.36s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The X experiment materially changes the synthesis by providing evidence of a downstream opinion effect, but the retrieved primary source is truncated and the key comparative question—why X differs from Facebook—remains unanswered. A focused search for the complete X study results and design would materially improve the answer.

**Next Search**

> "The political effects of X’s feed algorithm" full results effect sizes polarization chronological feed

---

# Iteration 3

## 1. Search

**Query**

> "The political effects of X’s feed algorithm" full results effect sizes polarization chronological feed

**Why this query**

The X experiment materially changes the synthesis by providing evidence of a downstream opinion effect, but the retrieved primary source is truncated and the key comparative question—why X differs from Facebook—remains unanswered. A focused search for the complete X study results and design would materially improve the answer.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S11 — The political effects of X's feed algorithm. - Abstract**
  URL: https://pubmed.ncbi.nlm.nih.gov/41708846
- **S12 — NEWS: Algorithm on X effects political views in the USA | unisg.ch**
  URL: https://www.unisg.ch/en/newsroom/algorithm-on-x-effects-political-views-in-the-usa
- **S13 — Ekaterina Zhuravskaya: The Political Eﬀects of X’s Recommender Algorithm | Department of Economics**
  URL: https://economics.unibocconi.eu/events/ekaterina-zhuravskaya-political-effects-xs-recommender-algorithm

**Search Duration:** 2.11s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

The new evidence strengthens the conclusion that X’s recommendation algorithm can change political opinions, not merely users’ exposure, but the effect is selective rather than a general increase in polarization.

**Confidence:** High

**Why this confidence level**

S11 provides the primary study abstract and S13 independently summarizes the same experiment. The treatment was randomized, though the evidence concerns a specific platform, population, and seven-week period.

**Evidence**

- A randomized seven-week field experiment assigned active U.S.-based X users to algorithmic or chronological feeds. Switching from chronological to algorithmic increased engagement and shifted opinions in a more conservative direction, especially on policy priorities, views of investigations into Donald Trump, and the war in Ukraine. [S11] [S13]
- The same experiment found no significant effect on affective polarization or self-reported partisanship. [S11]

#### Finding 2

**Claim**

The X study offers evidence for a behavioral mechanism: algorithmic exposure can change whom users follow, creating effects that persist after the feed is changed back.

**Confidence:** High

**Why this confidence level**

The mechanism is stated in the primary abstract and repeated in the institutional research summary. However, the retrieved material does not provide effect sizes or detailed compliance information.

**Evidence**

- Users exposed to X’s algorithmic feed were more likely to follow conservative political activist accounts and continued following them after switching to a chronological feed. [S11] [S13]
- The study reports that X’s algorithm promoted conservative content and demoted posts from traditional media, linking feed composition to subsequent account-following behavior. [S11]

#### Finding 3

**Claim**

The contrast between Facebook/Instagram and X is now more clearly platform-dependent rather than a simple contradiction in the literature.

**Confidence:** High

**Why this confidence level**

The results are directly comparable at the broad level and consistently show different downstream effects, while the sources also identify important differences in platform and treatment context.

**Evidence**

- Facebook/Instagram’s three-month chronological-feed intervention substantially changed exposure and platform activity but did not significantly change issue polarization, affective polarization, political knowledge, or other key attitudes. [S9]
- In contrast, X’s seven-week intervention shifted some political opinions when users moved from chronological to algorithmic feeds, while leaving partisanship and affective polarization unchanged. [S11] [S13]

#### Finding 4

**Claim**

The new evidence supports a more precise answer to the original question: algorithms have a robust and substantial effect on political visibility and engagement, and they can sometimes change political beliefs, but their effect on polarization itself is heterogeneous and not uniformly polarization-increasing.

**Confidence:** High

**Why this confidence level**

The conclusion integrates randomized evidence across two platforms and preserves the distinction between exposure, beliefs, polarization, and concrete behavior.

**Evidence**

- Facebook/Instagram evidence shows strong changes in what users see without detectable short-run changes in polarization or attitudes. [S9]
- X evidence shows a conservative shift in selected political opinions without a significant change in affective polarization or partisanship. [S11]
- Across the evidence reviewed, no source establishes effects on voting, donations, protest, or other concrete offline political behavior. [S7] [S8] [S9] [S10] [S11]

#### Finding 5

**Claim**

Differences in algorithmic objectives, content supply, user networks, treatment direction, and persistence may explain why studies reach different conclusions.

**Confidence:** Medium

**Why this confidence level**

The sources directly document these mechanisms, but they do not experimentally decompose the relative contribution of ranking, content supply, network structure, and user choice.

**Evidence**

- The X study reports that the algorithm promoted conservative content, reduced traditional-media visibility, and induced users to follow accounts they retained after treatment ended. [S11] [S13]
- The Facebook study emphasizes that ranking operates on content generated by users’ existing connections and that user choice and network composition may independently shape exposure. [S9]
- The asymmetric X result—effects when switching algorithmic ranking on but not comparable effects when switching it off—suggests that cumulative feed exposure and subsequent user choices matter. [S11] [S13]

### Conflicts Found

- The prior Facebook/Instagram experiments found large exposure effects but null short-run attitude effects, whereas the new X experiment found a directional shift in selected political opinions. This is a conditional disagreement across platforms and interventions, not evidence that one result necessarily invalidates the other. [S9] [S11] [S13]
- Descriptive claims that recommendation systems create echo chambers or intensify polarization remain stronger for exposure and opportunity effects than for broad changes in political beliefs. The X evidence strengthens the belief-change case but does not show increased affective polarization or partisanship. [S6] [S7] [S9] [S11]

### Important Gaps

- Whether the X opinion shifts persist over longer periods and translate into concrete political behavior such as voting, sharing, donations, or protest.
- Whether X’s results generalize to other platforms, countries, user populations, or algorithmic systems with different content and engagement objectives.
- How much of the X effect reflects ranking itself versus the conservative content supply, demotion of traditional media, and users’ subsequent decisions to follow new accounts.
- Whether Facebook/Instagram would produce effects under longer exposure, different political periods, or outcomes other than standard polarization and attitude measures.
- The effect sizes, subgroup differences, treatment compliance, and statistical precision for the X experiment are not included in the retrieved material.

**Analysis Duration:** 13.37s

---

## 3. Research Decision

**Decision:** Continue researching

**Why**

The main exposure-versus-belief question can now be answered responsibly, but an important part remains unresolved: whether algorithmically induced opinion changes affect concrete political behavior and whether the platform-specific results generalize. Evidence on those outcomes would materially improve the answer.

**Next Search**

> randomized social media recommendation algorithm experiment political behavior voting sharing donations participation outcomes

---

# Iteration 4

## 1. Search

**Query**

> randomized social media recommendation algorithm experiment political behavior voting sharing donations participation outcomes

**Why this query**

The main exposure-versus-belief question can now be answered responsibly, but an important part remains unresolved: whether algorithmically induced opinion changes affect concrete political behavior and whether the platform-specific results generalize. Evidence on those outcomes would materially improve the answer.

**Results**

5 results retrieved.

3 new unique sources added.

### Sources

- **S14 — How algorithmically curated online environments influence users’ political polarization: Results from two experiments with panel data**
  URL: https://www.sciencedirect.com/science/article/pii/S2451958823000763
- **S15 — How X's algorithm shifts political attitudes**
  URL: https://cepr.org/voxeu/columns/how-xs-algorithm-shifts-political-attitudes
- **S16 — How Social Media and Embedded Recommender Algorithm ...**
  URL: https://commons.clarku.edu/cgi/viewcontent.cgi?article=1086&context=sps_masters_papers

**Search Duration:** 2.51s

---

## 2. Evidence Analysis

### What We Learned

#### Finding 1

**Claim**

Exposure to politically like-minded arguments can itself increase both attitude polarization and affective polarization, but algorithmic selection does not necessarily intensify that exposure effect.

**Confidence:** High

**Why this confidence level**

S14 reports the design and central results of two experiments with panel data, directly separating content congruence from algorithmic versus random selection.

**Evidence**

- Two panel-based quasi-experiments exposed participants to arguments selected either algorithmically or randomly, while varying whether arguments matched or contradicted participants’ prior attitudes. Like-minded exposure increased attitude and affective polarization more than opposing exposure, but algorithmic selection did not amplify those effects overall. [S14]

#### Finding 2

**Claim**

Algorithmic curation may have a small direct effect on polarization in particular contexts, even when it does not amplify the broader effect of like-minded exposure.

**Confidence:** Medium

**Why this confidence level**

The result is reported in the article abstract, but the retrieved material does not give effect sizes, confidence intervals, or enough detail to assess its magnitude and robustness across topics.

**Evidence**

- For one of the two topics, algorithmically selected arguments produced slightly stronger attitude polarization than randomly selected arguments; the overall conclusion was that algorithmic curation did not amplify the effects consistently. [S14]

#### Finding 3

**Claim**

The new evidence reinforces the distinction between content exposure and algorithmic mediation: users’ exposure to congenial political arguments can change polarization, but this does not imply that recommendation algorithms are the source of the underlying persuasion effect.

**Confidence:** High

**Why this confidence level**

The evidence converges on a conditional conclusion: exposure congruence can matter, while the incremental effect of ranking varies by platform, context, and outcome.

**Evidence**

- S14 explicitly separates exposure to like-minded versus opposing arguments from algorithmically versus randomly selected arguments. Congenial exposure had a stronger polarization effect, whereas algorithmic selection generally did not magnify it. [S14]
- This complements the Facebook/Instagram evidence, where changing feed ranking substantially altered users’ information environments without changing short-run polarization, and the X evidence, where algorithmic ranking shifted selected political opinions but not affective polarization or partisanship. [S9] [S11]

#### Finding 4

**Claim**

The literature’s differing conclusions are partly explained by whether studies manipulate the content users receive or only the system’s method of selecting and ranking that content.

**Confidence:** High

**Why this confidence level**

These studies use different interventions and outcomes, and their reported results directly demonstrate why broad claims about 'algorithmic polarization' can conflate distinct causal pathways.

**Evidence**

- S14 manipulates both attitude-congruent versus attitude-incongruent arguments and algorithmic versus random selection, finding a stronger effect for congruent content than for algorithmic selection itself. [S14]
- S9 primarily changes ranking order and feed structure, finding major exposure and activity effects but no significant short-run changes in measured attitudes or polarization. [S9]
- S11 finds that enabling X’s algorithmic feed shifted selected policy opinions, while leaving affective polarization and partisanship unchanged. [S11]

#### Finding 5

**Claim**

The geographical and platform scope of the evidence is broader than the Facebook/X studies alone, but the new evidence still does not establish effects on concrete political behavior or long-term societal polarization.

**Confidence:** High

**Why this confidence level**

The retrieved sources clearly identify the measured outcomes and the continuing evidence gap.

**Evidence**

- S14 studies participants in Germany and examines experimental changes in attitudes and affective polarization rather than voting, participation, donations, protest, or offline hostility. [S14]
- The accumulated Facebook and X experiments likewise report short-run effects on exposure, activity, and selected opinions, but do not establish effects on concrete offline political behavior or years-long cumulative polarization. [S9] [S11]

### Conflicts Found

- S14 finds that like-minded exposure increases attitude and affective polarization, while algorithmic selection generally does not amplify that effect. This qualifies, rather than directly contradicts, descriptive claims that recommender systems create echo chambers or fuel polarization: the content users receive may matter more than the selection mechanism under the tested conditions. [S1] [S2] [S3] [S14]
- S14 reports largely null or small algorithmic effects in two German experiments, S9 reports null short-run attitude effects for Facebook/Instagram ranking changes, and S11 reports a conservative shift in selected opinions on X. The results are conditional across platform, population, content supply, treatment, and outcome; none shows a uniform increase in polarization. [S9] [S11] [S14]
- S14 describes a small direct algorithmic effect for one topic, whereas the broader summary of Facebook/Instagram experiments found no measurable short-run polarization effects. This is a difference in context and estimated scope, not necessarily a contradiction, but it indicates that algorithmic effects may be topic-specific. [S9] [S14]

### Important Gaps

- How large were the effects in S14, and how durable were they after the experimental exposure ended?
- Why did algorithmic selection produce a small additional attitude-polarization effect for one topic but not the other?
- Do the German findings generalize to other countries, platforms, recommender objectives, and political populations?
- How much of the effect attributed to algorithmic curation reflects the content pool, users’ prior attitudes, or their subsequent choices?
- Do recommendation algorithms affect concrete political behavior—such as voting, sharing, donations, protest, or hostility—even when standard polarization measures do not change?
- Do effects accumulate over years or through repeated cross-platform exposure?

**Analysis Duration:** 14.73s

---

## 3. Research Decision

**Decision:** Stop researching

**Why**

The new S14 evidence materially improves the answer by directly separating congenial content exposure from algorithmic selection. Together with the Facebook and X randomized evidence, the important question can now be answered responsibly: algorithms robustly shape visibility and can sometimes shift opinions, but their contribution to polarization is heterogeneous, generally smaller and less consistent than the effect of congenial exposure, and unproven for long-term or concrete political behavior. Further research would be valuable for effect sizes, persistence, and offline behavior, but it is not necessary to resolve the original question at the current level.

**Stop Reason:** sufficient_evidence

---

# Final Research Decision

**Research Stopped Because**

The analyzer determined that the important parts of the question could be answered responsibly.

**Stop Reason:** sufficient_evidence

**Searches Performed:** 4

**Unique Sources:** 16

**Remaining Uncertainty**

- The full effect sizes, confidence intervals, treatment compliance, and subgroup results for the X experiment are not included in the accumulated material.
- The persistence of Facebook, Instagram, X, and German experimental effects beyond the study windows remains unresolved.
- It is unclear why the X algorithm shifted selected opinions while not significantly changing affective polarization or partisanship.
- The generalizability of these results to TikTok, YouTube, Instagram Reels, other countries, and other recommender objectives is not established.
- No retrieved study establishes a causal effect on concrete political behavior such as voting, donations, protest, or offline political hostility.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 4 | 10.94s |
| OpenAI Analysis | 4 | 62.33s |
| Report Generation | 1 | 18.76s |
| Total Run | — | 92.03s |
