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

**Unique Sources:** 11

**OpenAI Calls:** 6

**Tavily Calls:** 3

**Started:** 2026-08-30T18:26:59-04:00

**Ended:** 2026-08-30T18:28:09-04:00

**Total Runtime:** 70.60s

---

# Iteration 1

## 1. Search

**Query**

> What is the current state of inference-time compute scaling for LLM reasoning? Separate what has been empirically validated from what is still speculative, and identify where the evidence is too thin to draw conclusions.

**Why this query**

This is the user's original research question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S1 — Overthinking in LLM Test-Time Compute Scaling**
  URL: https://arxiv.org/html/2604.10739v1
- **S2 — GitHub - ThreeSR/Awesome-Inference-Time ...**
  URL: https://github.com/ThreeSR/Awesome-Inference-Time-Scaling
- **S3 — Medium**
  URL: https://medium.com/@adnanmasood/inference-time-scaling-how-modern-ai-models-think-longer-to-perform-better-a1e1a8155fbd
- **S4 — Categories of Inference-Time Scaling for Improved LLM ...**
  URL: https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling
- **S5 — LLM Training vs Inference Scaling: A Cost-Benefit Analysis | Sebastian Raschka, PhD posted on the topic | LinkedIn**
  URL: https://www.linkedin.com/posts/sebastianraschka_what-should-we-focus-on-more-llm-training-activity-7396584322155257856-XoR8

**Search Duration:** 2.34s

---

## 2. Evidence Processing

- New claim proposals: 6
- Existing claim updates: 0
- New gaps: 5
- Resolved gaps: 0

**Processing Duration:** 15.67s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

Inference-time compute scaling can improve LLM reasoning performance by allocating additional inference resources, including longer reasoning traces, multiple candidate generations, search, verification, or iterative loops.

- S1 supports (direct): The paper describes test-time compute scaling through extended chains of thought and states that prior research reports accuracy improvements as compute budgets increase.
- S4 supports (direct): The overview defines inference-time scaling as allocating more compute and time during inference and lists chain-of-thought, self-consistency, best-of-N, verification, refinement, and search methods.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C2

**Claim**

The benefit of additional reasoning compute is not reliably monotonic: marginal returns diminish at higher budgets, and extended reasoning can cause some models to replace a previously correct answer with an incorrect one.

- S1 supports (direct): The study reports substantially diminishing marginal returns at higher budgets and identifies overthinking in which extended reasoning is associated with abandoning correct answers; it also describes tracking correct-to-incorrect answer flips.
- S4 contradicts (indirect): The overview says additional inference resources generally improve accuracy, but it does not examine or document non-monotonicity; this is a broad secondary characterization rather than a direct controlled contradiction.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C3

**Claim**

Optimal reasoning length varies with problem difficulty, making uniform compute allocation potentially inefficient.

- S1 supports (direct): The paper reports that optimal thinking length varies by difficulty and gives an example in which easy problems overthink at about 2K tokens whereas hard problems do so at about 8K tokens.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C4

**Claim**

Cost-aware stopping at moderate reasoning budgets can substantially reduce computation while maintaining comparable accuracy in the evaluated settings.

- S1 supports (direct): The abstract states that stopping at moderate budgets can reduce computation significantly while maintaining comparable accuracy, and the paper introduces cost-aware evaluation metrics and efficiency frontiers.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C5

**Claim**

Adaptive stopping and other adaptive test-time compute methods are promising approaches, but their general superiority over fixed-budget scaling is not established by the supplied evidence.

- S1 supports (direct): The paper explores early-stopping strategies and argues that adaptive reasoning length may reduce cost and improve accuracy when overthinking occurs.
- S4 supports (indirect): The overview identifies adaptive and varied inference-time methods as part of the current research landscape.

**Confidence:** LOW

**Status:** INSUFFICIENT_EVIDENCE

### New Claim C6

**Claim**

The evidence supplied is insufficient to determine a general compute-versus-training cost optimum or a universal break-even point for inference-time scaling.

- S5 supports (direct): The cost comparison is explicitly presented as a hypothetical thought experiment whose break-even point depends on assumed training cost, per-query inference cost, query volume, and model lifetime.

**Confidence:** HIGH

**Status:** INSUFFICIENT_EVIDENCE

### New Gap G1

The supplied evidence does not report the full experimental details, quantitative accuracy curves, sample sizes, statistical uncertainty, model identities, or benchmark coverage needed to assess how robust S1's overthinking and early-stopping findings are.

### New Gap G2

There is no direct comparative evidence in the supplied sources establishing which inference-time scaling strategy—longer chains, parallel sampling, self-consistency, search, verification, refinement, or agent-style looping—works best under matched compute and latency budgets.

### New Gap G3

The evidence is too thin to determine how inference-time scaling transfers beyond the mathematical and reasoning benchmarks mentioned, including factuality, coding, planning, tool use, long-context tasks, and real-world workloads.

### New Gap G4

The supplied sources do not establish whether observed scaling behavior depends on model family, training method, verifier quality, prompting, budget-forcing procedure, or evaluator design.

### New Gap G5

No evidence is supplied for the reliability of model confidence or convergence signals as adaptive stopping criteria, nor for their calibration under compute-cost constraints.

---

## 4. Current Research State

- Claims: 6
- Supported: 4
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 2
- Open Gaps: 5
- Remaining Searches: 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Target:** GAP G2

**Why**

Direct matched-budget comparisons are needed to determine which inference-time scaling strategies are empirically strongest; this is central to assessing the field’s current state.

**Next Search**

> LLM inference-time test-time compute scaling comparison matched compute budget chain-of-thought self-consistency best-of-N search verification refinement empirical benchmark


---

# Iteration 2

## 1. Search

**Query**

> LLM inference-time test-time compute scaling comparison matched compute budget chain-of-thought self-consistency best-of-N search verification refinement empirical benchmark

**Why this query**

Direct matched-budget comparisons are needed to determine which inference-time scaling strategies are empirically strongest; this is central to assessing the field’s current state.

5 result(s) retrieved; 3 new unique source(s) added.

- **S6 — Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters**
  URL: https://arxiv.org/html/2408.03314v1
- **S7 — Scaling Test-Time Compute: A New Paradigm in LLM Performance**
  URL: https://neurohive.io/en/state-of-the-art/scaling-test-time-compute-a-new-paradigm-in-llm-performance
- **S8 — Deep dive into scaling test time compute.**
  URL: https://machinelearningatscale.substack.com/p/deep-dive-into-scaling-test-time

**Search Duration:** 2.93s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 3
- New gaps: 2
- Resolved gaps: 0

**Processing Duration:** 15.26s

---

## 3. Ledger Updates

### New Claim C7

**Claim**

In experiments on PaLM-2 models fine-tuned for revision and verification on the MATH benchmark, a difficulty-aware compute-optimal strategy that selects among iterative revision, parallel sampling, and verifier-guided search improved test-time compute efficiency by more than 4× relative to a best-of-N baseline; under FLOPs-matched evaluation, a smaller model using test-time compute outperformed a 14× larger model on problems where the smaller model already had non-trivial success rates.

- S6 supports (direct): The paper's abstract directly reports more than 4× efficiency improvement over best-of-N and that test-time compute enabled a smaller base model to outperform a 14× larger model in FLOPs-matched evaluation. The reported experiments used PaLM-2 models fine-tuned for revision or verification on MATH.
- S7 supports (indirect): A secondary account repeats the more-than-4× efficiency and 14× larger-model comparisons and describes the PaLM-2/MATH evaluation.
- S8 supports (indirect): A secondary technical discussion reports that difficulty-based strategy selection can outperform best-of-N with up to a 4× compute reduction and describes the relevant revision and verifier-search mechanisms.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

Inference-time compute scaling can improve LLM reasoning performance by allocating additional inference resources, including longer reasoning traces, multiple candidate generations, search, verification, or iterative loops.

- S6 supports (direct): The study directly evaluates additional test-time computation through verifier-guided search and adaptive revision of the response distribution, showing measurable performance and efficiency gains.
- S7 supports (indirect): The secondary report describes test-time compute gains over best-of-N and parameter scaling in PaLM-2 experiments on MATH.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C3

**Claim**

Optimal reasoning length varies with problem difficulty, making uniform compute allocation potentially inefficient.

- S6 supports (direct): The study finds that the most effective test-time strategy depends critically on prompt difficulty: sequential refinement is favored on easier problems, while independent resampling or verifier-guided search is more useful on harder problems.
- S8 supports (indirect): The secondary discussion likewise reports difficulty-dependent differences between revision, parallel sampling, and search methods.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

Adaptive stopping and other adaptive test-time compute methods are promising approaches, but their general superiority over fixed-budget scaling is not established by the supplied evidence.

- S6 supports (direct): The paper directly motivates and evaluates a difficulty-aware compute-optimal policy that adaptively selects among revision, parallel sampling, and verifier-guided search; its reported efficiency advantage is specific to the evaluated setup.
- S8 supports (indirect): The secondary analysis describes practical difficulty estimation and adaptive strategy selection, including reported gains over best-of-N.

**Confidence:** LOW → MEDIUM

**Status:** INSUFFICIENT_EVIDENCE → INSUFFICIENT_EVIDENCE

### New Gap G6

The reported more-than-4× efficiency gain and 14× larger-model comparison are based on a specific PaLM-2/MATH setup with capability-specific fine-tuning; the supplied evidence does not establish how these quantitative advantages change across model families, untuned models, tasks, or independently replicated evaluations.

### New Gap G7

The supplied evidence does not fully specify the matched compute accounting, latency assumptions, verifier-training and selection costs, or uncertainty estimates needed to interpret the magnitude of the reported compute-optimal advantages.

---

## 4. Current Research State

- Claims: 7
- Supported: 5
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 2
- Open Gaps: 7
- Remaining Searches: 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Target:** GAP G2

**Why**

A direct matched-budget comparison of inference-time strategies is the highest-value unresolved issue for distinguishing validated methods from speculative superiority claims.

**Next Search**

> empirical comparison LLM test-time compute scaling chain-of-thought self-consistency best-of-N search verification refinement matched FLOPs latency benchmark


---

# Iteration 3

## 1. Search

**Query**

> empirical comparison LLM test-time compute scaling chain-of-thought self-consistency best-of-N search verification refinement matched FLOPs latency benchmark

**Why this query**

A direct matched-budget comparison of inference-time strategies is the highest-value unresolved issue for distinguishing validated methods from speculative superiority claims.

5 result(s) retrieved; 3 new unique source(s) added.

- **S9 — Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (Paper)**
  URL: https://www.youtube.com/watch?v=AfAmwIP2ntY
- **S10 — [PDF] Towards Thinking-Optimal Scaling of Test-Time Compute for LLM ... - NIPS**
  URL: https://proceedings.neurips.cc/paper_files/paper/2025/file/3e22bea3b170f4c2aebb9c48d98ae64d-Paper-Conference.pdf
- **S11 — CMU Advanced NLP Spring 2026 (23): Test-Time Scaling**
  URL: https://www.youtube.com/watch?v=ZRA00pilC6k

**Search Duration:** 2.52s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 5
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 13.99s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Inference-time compute scaling can improve LLM reasoning performance by allocating additional inference resources, including longer reasoning traces, multiple candidate generations, search, verification, or iterative loops.

- S9 supports (indirect): The paper presentation summarizes systematic experiments on verifier-guided search and adaptive response-distribution updates, reporting improved test-time performance and efficiency under fixed compute.
- S10 supports (direct): The paper reports that longer chain-of-thought reasoning, sampling-based scaling, and related test-time methods can improve reasoning performance, while framing test-time compute as an additional scaling dimension.
- S11 supports (indirect): The lecture describes empirical scaling plots in which additional test-time samples or generated reasoning tokens improve benchmark solve rates, and presents reranking, refinement, and long-CoT methods as inference-time scaling strategies.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

The benefit of additional reasoning compute is not reliably monotonic: marginal returns diminish at higher budgets, and extended reasoning can cause some models to replace a previously correct answer with an incorrect one.

- S10 supports (direct): Controlled experiments on LLaMA3.1-8B-Instruct and Qwen2.5-32B-Instruct report that excessively long reasoning paths can impair performance, especially on easier tasks, and that longer chains may contain more erroneous steps.
- S9 supports (indirect): The presentation of the compute-scaling paper reports that the effectiveness of scaling methods varies with prompt difficulty and that excessive computation can be inefficient.

**Confidence:** MEDIUM → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C3

**Claim**

Optimal reasoning length varies with problem difficulty, making uniform compute allocation potentially inefficient.

- S10 supports (direct): Experiments report an optimal reasoning-effort or scaled-length distribution that varies by task difficulty and domain; longer reasoning is more useful for challenging problems than for easier ones.
- S9 supports (indirect): The paper presentation states that the best test-time strategy critically varies with prompt difficulty, motivating adaptive allocation per prompt.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

Adaptive stopping and other adaptive test-time compute methods are promising approaches, but their general superiority over fixed-budget scaling is not established by the supplied evidence.

- S10 supports (direct): The paper proposes Thinking-Optimal Scaling, in which models select among different reasoning efforts and use the shortest correct response, and reports improvements across GSM8K, MATH500, and AIME2024 for Qwen2.5-based models.
- S11 supports (indirect): The lecture presents strategy choice, reranking, and variable reasoning length as active approaches to inference-time scaling, including cases where strategy affects performance.

**Confidence:** MEDIUM → MEDIUM

**Status:** INSUFFICIENT_EVIDENCE → INSUFFICIENT_EVIDENCE

### Updated Claim C7

**Claim**

In experiments on PaLM-2 models fine-tuned for revision and verification on the MATH benchmark, a difficulty-aware compute-optimal strategy that selects among iterative revision, parallel sampling, and verifier-guided search improved test-time compute efficiency by more than 4× relative to a best-of-N baseline; under FLOPs-matched evaluation, a smaller model using test-time compute outperformed a 14× larger model on problems where the smaller model already had non-trivial success rates.

- S9 supports (indirect): The presentation reproduces the paper's reported more-than-4× efficiency improvement over best-of-N and the FLOPs-matched result in which test-time compute lets a smaller model outperform a 14× larger model on a subset of MATH problems.

**Confidence:** MEDIUM → MEDIUM

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 7
- Supported: 5
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 2
- Open Gaps: 7
- Remaining Searches: 0

---

## 5. Research Decision

**Decision:** Stop researching.

**Why**

The maximum research iteration budget was reached.

**Stop Reason:** max_iterations


---

# Final Research Decision

**Stop Reason:** max_iterations

**Remaining Uncertainty**

- The full experimental details, quantitative accuracy curves, sample sizes, statistical uncertainty, model identities, and benchmark coverage needed to assess the robustness of overthinking and early-stopping findings are not supplied.
- There is no direct comparative evidence establishing which strategy—longer chains, parallel sampling, self-consistency, search, verification, refinement, or agent-style looping—works best under matched compute and latency budgets.
- The evidence is too thin to determine whether inference-time scaling transfers beyond mathematical and reasoning benchmarks to factuality, coding, planning, tool use, long-context tasks, or real-world workloads.
- The supplied sources do not establish how scaling behavior depends on model family, training method, verifier quality, prompting, budget-forcing procedure, or evaluator design.
- No evidence is supplied on the reliability or calibration of model confidence and convergence signals as adaptive stopping criteria under compute-cost constraints.
- The more-than-4x efficiency and 14x larger-model comparisons come from a specific PaLM-2/MATH setup, and their behavior across model families, untuned models, tasks, and independent replications remains unresolved.
- The supplied evidence does not fully specify matched compute accounting, latency assumptions, verifier-training and selection costs, or uncertainty estimates needed to interpret the magnitude of reported compute-optimal advantages.

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Tavily Search | 3 | 7.78s |
| Evidence Processing | 3 | 44.93s |
| Research Decision | 2 | 4.52s |
| Report Generation | 1 | 13.35s |
| Total Run | — | 70.60s |
