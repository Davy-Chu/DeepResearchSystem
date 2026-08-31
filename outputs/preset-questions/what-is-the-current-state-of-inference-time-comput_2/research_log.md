# Research Run Log

## Run Summary

**System Version:** evidence-ledger-v1

**Research Question**

What is the current state of inference-time compute scaling for LLM reasoning? Separate what has been empirically validated from what is still speculative, and identify where the evidence is too thin to draw conclusions.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-5.6-luna

**Searches Performed:** 3 / 3

**Unique Sources:** 10

**OpenAI Calls:** 6

**Tavily Calls:** 3

**Started:** 2026-08-31T17:32:01-04:00

**Ended:** 2026-08-31T17:33:17-04:00

**Total Runtime:** 75.78s

---

# Iteration 1

## 1. Search

**Query**

> What is the current state of inference-time compute scaling for LLM reasoning? Separate what has been empirically validated from what is still speculative, and identify where the evidence is too thin to draw conclusions.

**Purpose:** GENERAL

**Why this query**

This is the user's original research question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S1 — Overthinking in LLM Test-Time Compute Scaling**
  URL: https://arxiv.org/html/2604.10739v1
- **S2 — GitHub - ThreeSR/Awesome-Inference-Time ...**
  URL: https://github.com/ThreeSR/Awesome-Inference-Time-Scaling
- **S3 — Reasoning Under Inference-Time Compute**
  URL: https://eecs.engin.umich.edu/event/reasoning-under-inference-time-compute
- **S4 — Inference-Time Scaling: How Modern AI Models Think ...**
  URL: https://medium.com/@adnanmasood/inference-time-scaling-how-modern-ai-models-think-longer-to-perform-better-a1e1a8155fbd
- **S5 — Categories of Inference-Time Scaling for Improved LLM ...**
  URL: https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling

**Search Duration:** 2.41s

---

## 2. Evidence Processing

- New claim proposals: 5
- Existing claim updates: 0
- New gaps: 5
- Resolved gaps: 0

**Processing Duration:** 16.67s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

Inference-time compute scaling is an umbrella of methods that spend additional inference resources through longer reasoning, multiple candidate generations, search, verification, retrieval, or iterative/agent-style computation; it is presented as a complement to training-time scaling rather than a replacement for it.

- S5 supports (direct): Defines inference-time scaling as allocating more compute and time during inference, and lists chain-of-thought, self-consistency, best-of-N, verifier-based sampling, refinement, and search methods.
- S4 supports (direct): Describes test-time compute as longer thinking, more candidate solutions, search/verification, or agent-style loops.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C2

**Claim**

Empirical studies have reported that allocating additional inference-time compute can improve reasoning performance on at least some mathematical, scientific, and other complex reasoning tasks.

- S1 supports (indirect): States that prior research has reported substantial success from extended chains of thought and that test-time compute scaling can outperform model scaling for many tasks; the cited study evaluates controlled budgets from 500 to 16,000 reasoning tokens.
- S3 supports (direct): The dissertation abstract states that inference-time retrieval, search, and extended chain-of-thought enabled LLMs to tackle complex math and science problems, and that its methods improve or strengthen reasoning capabilities.
- S5 supports (indirect): Summarizes inference scaling as an effective way to improve answer quality and accuracy and describes multiple evaluated method families.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C3

**Claim**

The relationship between reasoning-token budget and accuracy is not reliably monotonic: the supplied primary study reports diminishing marginal returns at higher budgets and an overthinking phenomenon in which extended reasoning can cause a model to abandon a previously correct answer.

- S1 supports (direct): Its abstract reports substantially diminishing marginal returns, answer-changing from correct to incorrect with extended reasoning, and task-dependent optimal thinking lengths; it describes controlled budget experiments and per-problem flip-event tracking.
- S4 contradicts (indirect): The overview frames the practical pattern as giving more thinking time for harder questions and often obtaining a better answer, but it does not present evidence that accuracy is monotonic.
- S5 contradicts (indirect): The overview says additional inference resources generally improve accuracy, without discussing the non-monotonicity reported by S1; this is a weaker, broad characterization rather than a direct test of monotonicity.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C4

**Claim**

Uniform allocation of the same reasoning budget to every problem is empirically indicated to be suboptimal in the supplied study; optimal thinking length varies with problem difficulty, and moderate stopping can reduce computation while maintaining comparable accuracy.

- S1 supports (direct): Reports difficulty-dependent optimal thinking lengths, gives examples of earlier overthinking on easier problems than harder ones, and states that cost-aware stopping at moderate budgets can substantially reduce computation at comparable accuracy.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C5

**Claim**

Verification is an important bottleneck and reliability concern for inference-time reasoning systems: the supplied dissertation abstract reports limitations from static discriminative verifiers and a vulnerability in which unfaithful reasoning traces can manipulate LLM judges into accepting suboptimal actions.

- S3 supports (direct): Reports that static discriminative verifiers cannot adapt verification compute to input complexity, motivates generative process verification, and describes agents gaming evaluation through unfaithful traces.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Gap G1

The supplied evidence does not establish how inference-time scaling compares quantitatively with model scaling or training-time scaling across standardized benchmarks, models, and compute-matched cost/latency budgets.

### New Gap G2

Evidence is too thin to determine the generality of overthinking, diminishing returns, or optimal stopping across model families, domains, languages, prompting protocols, budget ranges, and reasoning methods beyond the study summarized in S1.

### New Gap G3

The sources do not provide sufficient quantitative evidence to identify which inference-time scaling method—serial chain-of-thought, parallel sampling, search, verification, retrieval, or agentic iteration—offers the best accuracy-cost-reliability trade-off.

### New Gap G4

The supplied material does not quantify reliability risks, verifier gaming, or the effectiveness of proposed verification and adaptive-compute methods under adversarial or distribution-shifted conditions.

### New Gap G5

The repository and overview sources catalog or summarize methods, but the supplied excerpts do not independently validate the reported performance of individual methods or establish reproducibility.

---

## 4. Current Research State

- Claims: 5
- Supported: 5
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 5
- Remaining Searches: 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** GAP G1

**Why**

High-value gap: the answer lacks quantitative, compute-matched evidence comparing inference-time scaling with model/training scaling across benchmarks.

**Next Search**

> Primary empirical studies comparing inference-time/test-time compute scaling with model scaling or training-time scaling under matched compute or latency budgets across standardized LLM reasoning benchmarks; report accuracy, cost, and scaling curves.


---

# Iteration 2

## 1. Search

**Query**

> Primary empirical studies comparing inference-time/test-time compute scaling with model scaling or training-time scaling under matched compute or latency budgets across standardized LLM reasoning benchmarks; report accuracy, cost, and scaling curves.

**Target:** G1

**Purpose:** GENERAL

**Why this query**

High-value gap: the answer lacks quantitative, compute-matched evidence comparing inference-time scaling with model/training scaling across benchmarks.

5 result(s) retrieved; 3 new unique source(s) added.

- **S6 — Test-Time Compute scaling but in simple! OpenAI o1/o3 made big waves by being able to scale inference compute relative to downstream performance. Here is a poor man's recipe for it. “Scaling… | Philipp Schmid | 12 comments**
  URL: https://www.linkedin.com/posts/philipp-schmid-a6a2bb196_test-time-compute-scaling-but-in-simple-activity-7276162046050668544-bYxt
- **S7 — Scaling LLM Test Time Compute - Jonas Vetterle Personal Page & Blog**
  URL: https://www.jonvet.com/blog/llm-test-time-compute
- **S8 — What is Inference-Time Scaling? How to Optimize ...**
  URL: https://unimon.co.th/en/blog/test-time-compute-inference-scaling-guide

**Search Duration:** 2.79s

---

## 2. Evidence Processing

- New claim proposals: 2
- Existing claim updates: 4
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 14.15s

---

## 3. Ledger Updates

### New Claim C6

**Claim**

A secondary summary reports that repeated sampling with answer selection or verification improved coding performance by up to 40% in the cited study, with performance scaling approximately log-linearly in the number of samples before verification methods plateaued at roughly 100 samples.

- S6 supports (indirect): A LinkedIn post summarizes the cited repeated-sampling paper as finding up to 40% coding improvement, approximately log-linear scaling with sample count, and a plateau in voting or reward-model verification after about 100 samples.

**Confidence:** LOW

**Status:** WEAK

### New Claim C7

**Claim**

Inference-time compute can impose substantial per-request cost and latency, creating a practical trade-off between reasoning accuracy and deployment efficiency.

- S6 supports (direct): The post emphasizes that repeated sampling requires many generations, discusses balancing sample count against cost, and notes concerns about throughput and practical serving speed.
- S8 supports (direct): The enterprise-oriented guide identifies latency and inference cost as the principal bottlenecks of inference-time scaling and describes increased internal reasoning-token costs per request.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

Inference-time compute scaling is an umbrella of methods that spend additional inference resources through longer reasoning, multiple candidate generations, search, verification, retrieval, or iterative/agent-style computation; it is presented as a complement to training-time scaling rather than a replacement for it.

- S7 supports (direct): The overview defines test-time compute as additional inference computation and lists chains of thought, revision, external verification, backtracking, repeated sampling, and selection.
- S8 supports (direct): The guide defines inference-time scaling as increasing generated tokens, sampling passes, or search depth, including CoT, self-consistency, Best-of-N, Tree-of-Thoughts, and reflection, and presents it as complementary to training-time scaling.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

Empirical studies have reported that allocating additional inference-time compute can improve reasoning performance on at least some mathematical, scientific, and other complex reasoning tasks.

- S6 supports (indirect): A secondary summary reports performance gains from repeated sampling and verification, including up to 40% improvement in coding, and describes particular benefits for coding and formal-proof tasks.
- S7 supports (indirect): The overview states that additional test-time computation improves performance on some reasoning tasks and cites reported results for difficult ARC and FrontierMath evaluations, while noting that closed-model mechanisms are unclear.
- S8 supports (indirect): The guide states that additional inference computation can improve answer quality and describes repeated solving, critique/revision, and search as practical techniques.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C3

**Claim**

The relationship between reasoning-token budget and accuracy is not reliably monotonic: the supplied primary study reports diminishing marginal returns at higher budgets and an overthinking phenomenon in which extended reasoning can cause a model to abandon a previously correct answer.

- S6 supports (indirect): The summary reports diminishing returns and a plateau in verification-based repeated sampling at roughly 100 samples, consistent with non-unbounded benefits from additional inference compute.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

Verification is an important bottleneck and reliability concern for inference-time reasoning systems: the supplied dissertation abstract reports limitations from static discriminative verifiers and a vulnerability in which unfaithful reasoning traces can manipulate LLM judges into accepting suboptimal actions.

- S6 supports (indirect): The post identifies voting, reward-model scoring, and LLM judging as selection mechanisms, reports that verification methods plateau, and notes the need for clear criteria for a good generation.
- S7 supports (direct): The overview frames test-time scaling around a proposer generating candidates and a verifier scoring and selecting among them, highlighting verification as a central component.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 7
- Supported: 6
- Weak: 1
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 5
- Remaining Searches: 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** GAP G1

**Why**

A final focused search should address the highest-priority unresolved comparison: whether inference-time scaling beats or complements model/training scaling under matched compute budgets.

**Next Search**

> Primary empirical papers on test-time or inference-time compute scaling versus model-size or training-compute scaling under compute-matched budgets for LLM reasoning; include benchmark-level accuracy, inference FLOPs, latency, and scaling curves.


---

# Iteration 3

## 1. Search

**Query**

> Primary empirical papers on test-time or inference-time compute scaling versus model-size or training-compute scaling under compute-matched budgets for LLM reasoning; include benchmark-level accuracy, inference FLOPs, latency, and scaling curves.

**Target:** G1

**Purpose:** GENERAL

**Why this query**

A final focused search should address the highest-priority unresolved comparison: whether inference-time scaling beats or complements model/training scaling under matched compute budgets.

5 result(s) retrieved; 2 new unique source(s) added.

- **S9 — Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters**
  URL: https://arxiv.org/html/2408.03314v1
- **S10 — Deep dive into scaling test time compute.**
  URL: https://machinelearningatscale.substack.com/p/deep-dive-into-scaling-test-time

**Search Duration:** 2.85s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 3
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 11.05s

---

## 3. Ledger Updates

### New Claim C8

**Claim**

The effectiveness of inference-time scaling strategies is strongly prompt-difficulty- and base-model-dependent: iterative revision can be more effective on easier problems, whereas independent sampling or search against process-based verifiers can be more effective on harder problems requiring exploration of multiple approaches.

- S9 supports (direct): In experiments on MATH with capability-fine-tuned PaLM-2 models, the paper reports that strategy effectiveness critically depends on problem difficulty and base model; sequential revision is favored on easier problems, while parallel resampling or tree search with process-based verifiers is favored on harder problems.
- S10 supports (indirect): The secondary deep dive summarizes the same difficulty-dependent pattern, including revision benefits on easier questions and more extensive PRM-guided search for harder questions.

**Confidence:** HIGH

**Status:** SUPPORTED

### Updated Claim C2

**Claim**

Empirical studies have reported that allocating additional inference-time compute can improve reasoning performance on at least some mathematical, scientific, and other complex reasoning tasks.

- S9 supports (direct): A primary study evaluates test-time search and adaptive response-distribution updating on MATH and reports that compute-optimal scaling can improve efficiency by more than 4× versus best-of-N; in a FLOPs-matched evaluation, test-time compute outperforms a 14× larger model on problems where the smaller model has non-trivial success rates.
- S10 supports (indirect): A secondary account reports the paper's gains from adaptive strategy selection, including up to a 4× reduction in compute relative to a comparable best-of-N approach.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

Uniform allocation of the same reasoning budget to every problem is empirically indicated to be suboptimal in the supplied study; optimal thinking length varies with problem difficulty, and moderate stopping can reduce computation while maintaining comparable accuracy.

- S9 supports (direct): The primary study reports that the most effective test-time strategy depends on prompt difficulty and motivates compute-optimal allocation rather than uniform strategy or budget assignment; it also reports more than 4× efficiency improvement over a best-of-N baseline.
- S10 supports (indirect): The secondary summary describes difficulty-bin-based strategy selection and reports that adaptive allocation achieves substantial compute savings relative to best-of-N.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

Verification is an important bottleneck and reliability concern for inference-time reasoning systems: the supplied dissertation abstract reports limitations from static discriminative verifiers and a vulnerability in which unfaithful reasoning traces can manipulate LLM judges into accepting suboptimal actions.

- S9 supports (direct): The primary study centers one mechanism on search against dense process-based verifier reward models and shows that the usefulness of verifier-guided search varies with prompt difficulty; it also notes that capability-specific fine-tuning was needed to induce verification and revision abilities in the evaluated models.
- S10 supports (indirect): The secondary account describes PRM-guided beam and lookahead search, including beam-search overfitting to the verifier on easier problems and lookahead underperforming at equal generation budgets because of rollout cost.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 8
- Supported: 7
- Weak: 1
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 5
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

- G1: No quantitative, standardized comparison establishes how inference-time scaling compares with model scaling or training-time scaling across models, benchmarks, and matched cost or latency budgets.
- G2: The generality of overthinking, diminishing returns, and optimal stopping across model families, domains, languages, prompting protocols, and budget ranges is unresolved.
- G3: The evidence is insufficient to identify a universally best accuracy-cost-reliability trade-off among serial reasoning, parallel sampling, search, verification, retrieval, and agentic iteration.
- G4: Reliability risks, verifier gaming, and the performance of adaptive-compute or verification methods under adversarial or distribution-shifted conditions are not quantitatively established.
- G5: Several repository, overview, and secondary sources summarize methods or results without independently validating performance or reproducibility.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 8.05s |
| Evidence Processing | 3 | 41.87s |
| Research Decision | 2 | 5.19s |
| Report Generation | 1 | 20.66s |
| Total Run | — | 75.78s |
