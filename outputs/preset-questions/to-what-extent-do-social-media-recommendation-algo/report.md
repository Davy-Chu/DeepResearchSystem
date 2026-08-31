# Research Report

## Research Question

To what extent do social-media recommendation algorithms contribute to political polarization? Separate evidence that algorithms change what users see from evidence that they actually change political beliefs or behavior, and explain why the literature reaches different conclusions.

## Summary

The evidence most clearly shows that recommendation algorithms change the visibility, ordering, and composition of content users encounter. Evidence that these changes alter political beliefs or polarization is mixed: some experiments find short-term effects on affective polarization or belief updating, while other large randomized experiments find substantial exposure changes but no measurable change in political attitudes. The literature therefore supports a conditional contribution rather than the claim that algorithms universally or independently drive polarization. The retrieved evidence does not establish effects on concrete political behavior such as voting, turnout, or participation.

## Findings

### Finding 1

**Claim**

Recommendation algorithms reliably change what users see and how they engage with platforms.

**Confidence:** High

**Why this confidence level**

S10 directly reports a randomized experiment measuring both exposure and on-platform activity; S2 provides a consistent description of recommendation mechanisms, though it is a secondary source.

**Evidence**

- Recommendation systems rank, filter, and suggest content using behavioral signals such as likes, shares, comments, watch time, follows, searches, and prior engagement, thereby changing content visibility and ordering. [S2]
- In a randomized Facebook and Instagram experiment, replacing personalized algorithmic feeds with chronological feeds substantially changed the amount and type of political, untrustworthy, uncivil, moderate, and ideologically mixed content users encountered. It also reduced time spent on the platforms and user activity. [S10]

### Finding 2

**Claim**

Changes in exposure should not be treated as evidence that algorithms necessarily change political beliefs or polarization.

**Confidence:** High

**Why this confidence level**

Both sources distinguish changes in content exposure from downstream attitudinal outcomes, using experimental comparisons.

**Evidence**

- Despite substantial changes in exposure and platform activity, the Facebook and Instagram experiment found no significant change over three months in issue polarization, affective polarization, political knowledge, or other key attitudes. [S10]
- A separate experiment found that exposure to like-minded arguments increased attitude and affective polarization, but algorithmic selection did not generally amplify that effect beyond the effect of receiving like-minded content. [S1]

### Finding 3

**Claim**

Some experiments do find that ranking or curation can change political attitudes and belief updating under particular conditions.

**Confidence:** Medium

**Why this confidence level**

These studies directly manipulate ranking or feed exposure, but the retrieved evidence for them is a secondary account or press release rather than the complete underlying paper. The outcomes are also short-term attitudes or beliefs rather than durable behavior.

**Evidence**

- An X browser-extension experiment varied exposure to content classified as expressing antidemocratic attitudes and partisan hostility. The reported result was that increased exposure made evaluations of the opposing party colder, while reduced exposure made them warmer after a short experimental period. [S9]
- A controlled belief-updating experiment reported that engagement-based ranking produced more polarized and less accurate beliefs than alternative ranking objectives; bridging-oriented and intelligence-oriented rankings increased consensus or factual accuracy in some comparisons. [S7]

### Finding 4

**Claim**

The best-supported synthesis is that algorithms can contribute to polarization conditionally, but they are not shown here to be a universal or dominant cause.

**Confidence:** High

**Why this confidence level**

The sources converge on a qualified conclusion: effects depend on the content being ranked, the platform, the period, the comparison condition, and the outcome measured.

**Evidence**

- The Facebook and Instagram experiment found changed exposure without changed political attitudes, while the X experiment found an affective-polarization effect when specifically targeting hostile and antidemocratic content during a highly polarized election period. [S9] [S10]
- The German panel experiments found that like-minded content exposure was more polarizing than opposing exposure, but found little general additional amplification attributable to algorithmic selection itself. [S1]
- A review of digital-media research characterizes effects on political outcomes as variable by outcome and political system, while a review focused on algorithmic mechanisms says algorithms often reinforce pre-existing social drivers. [S3] [S8]

### Finding 5

**Claim**

The retrieved evidence does not establish that recommendation algorithms change concrete political behavior such as voting, turnout, political participation, or offline hostility.

**Confidence:** High

**Why this confidence level**

The sources identify attitudinal outcomes but do not report demonstrated effects on the concrete political behaviors specified in the question.

**Evidence**

- The reported experiments primarily measure attitude polarization, affective evaluations, belief updating, knowledge, platform activity, or content exposure rather than voting or other offline political behavior. [S1] [S4] [S5] [S7] [S9] [S10]
- The account of the X experiment explicitly states that the duration of the observed effects and their impact on voting or other forms of citizen participation remain unclear. [S9]

### Finding 6

**Claim**

Different conclusions arise because studies test different links in the causal chain and use different counterfactuals.

**Confidence:** High

**Why this confidence level**

The sources directly document differences in interventions, content categories, platforms, time periods, user behavior, and outcomes, all of which can produce different findings.

**Evidence**

- The Facebook and Instagram study compared default personalized ranking with reverse-chronological ordering, whereas the X study targeted the prominence of hostile and antidemocratic content. [S9] [S10]
- The German experiments held the direction of content relative to users’ prior attitudes constant and tested whether algorithmic selection added to the effect of like-minded exposure; the belief-updating study instead compared different ranking objectives, including engagement-based and bridging-oriented approaches. [S1] [S7]
- Algorithms operate in a feedback loop with users’ prior preferences, networks, and engagement, so observational associations can conflate user self-selection with algorithmic influence. [S2] [S10]
- The broader digital-media review shows that effects vary across political outcomes and political systems, limiting generalization from any single platform or experiment. [S8]

## Conflicts and Uncertainty

- S10 found no significant change in political attitudes after replacing Facebook and Instagram’s algorithmic feeds with chronological feeds, whereas S9 reports that reranking hostile and antidemocratic content on X changed affective polarization. These results may be conditional rather than contradictory because the studies used different platforms, content interventions, periods, and outcome measures. [S9] [S10]
- S1 found little general incremental amplification from algorithmic selection, while S7 and S9 report attitude or belief effects from particular ranking objectives or targeted content categories. The studies therefore estimate different forms of algorithmic influence rather than one identical treatment effect. [S1] [S7] [S9]
- S3 emphasizes that algorithms mostly reinforce pre-existing social drivers, while S9 and S7 report direct effects of ranking on attitudes or beliefs. These claims can coexist if algorithms exert causal effects that depend on users’ prior preferences, networks, and the available content environment. [S3] [S7] [S9]
- The strongest reported evidence for the X and alternative-ranking experiments is available here through secondary reporting rather than the complete research papers, limiting assessment of their methods, effect sizes, and statistical uncertainty. [S7] [S9]

## Remaining Gaps

- Whether ranking-induced attitude changes persist beyond the short experimental periods.
- Whether recommendation algorithms affect voting, turnout, political participation, political discussion, or offline hostility.
- How representative browser-extension volunteers, platform users, and experimental samples are.
- Which features matter most: engagement optimization, partisan hostility, emotional intensity, ideological similarity, personalization, or repeated exposure.
- Whether effects differ across platforms, countries, election periods, and users with different levels of prior partisan commitment.
- How short-term effects accumulate, dissipate, or interact with longer-term network and media use.

## Conclusion

Recommendation algorithms clearly contribute to political information exposure: they alter which content is prominent and how users engage with platforms. Their effect on political beliefs is real in some controlled settings, particularly when ranking increases exposure to hostile or antidemocratic material or when engagement-based curation is compared with alternative objectives. However, other large experiments found no change in polarization or related attitudes despite major exposure changes. The most defensible conclusion is therefore conditional: algorithms can shape polarization, but their effects depend on the content, ranking objective, platform, users, and political context, and they often operate by reinforcing existing social and partisan dynamics. The accumulated research does not yet demonstrate that recommendation algorithms change concrete political behavior. Research stopped at the iteration limit, so these behavioral and durability questions remain unresolved.

## Sources

- [S1] How algorithmically curated online environments influence users’ political polarization: Results from two experiments with panel data - ScienceDirect — https://www.sciencedirect.com/science/article/pii/S2451958823000763
- [S2] The Role of Social Media Algorithms in Shaping Political Polarisation in the United States — https://www.humanrightsresearch.org/post/the-role-of-social-media-algorithms-in-shaping-political-polarisation-in-the-united-states
- [S3] Social Drivers and Algorithmic Mechanisms on Digital Media — https://pmc.ncbi.nlm.nih.gov/articles/PMC11373151
- [S4] Algorithms Shift Polarization. Why Does Policy Still Miss the Real Problem? | TechPolicy.Press — https://techpolicy.press/algorithms-shift-polarization-why-does-policy-still-miss-the-real-problem
- [S5] How Does Social Media Impact Political Polarization? — https://news.northeastern.edu/2025/11/27/social-media-political-polarization-research
- [S6] How X's algorithm shifts political attitudes — https://cepr.org/voxeu/columns/how-xs-algorithm-shifts-political-attitudes
- [S7] Alternative social media algorithms can help users form more accurate and less polarized beliefs | EurekAlert! — https://www.eurekalert.org/news-releases/1128531
- [S8] A systematic review of worldwide causal and correlational evidence on digital media and democracy — https://www.nature.com/articles/s41562-022-01460-1
- [S9] Independent research shows that X's (Twitter's) algorithm can influence political polarisation — https://sciencemediacentre.es/en/independent-research-shows-xs-twitters-algorithm-can-influence-political-polarisation
- [S10] How do social media feed algorithms affect attitudes and ... — https://cdr.lib.unc.edu/downloads/wp9891401
