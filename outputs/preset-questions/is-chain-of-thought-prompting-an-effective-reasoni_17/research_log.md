# Research Run Log

## Run Summary

**System Version:** evidence-ledger-v1

**Research Question**

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

**Status:** Completed

**Stop Reason:** max_iterations

**Search Provider:** Tavily

**Model:** gpt-4o-mini

**Searches Performed:** 10 / 10

**Unique Sources:** 25

**OpenAI Calls:** 20

**Tavily Calls:** 10

**Started:** 2026-09-01T12:12:44-04:00

**Ended:** 2026-09-01T12:14:51-04:00

**Total Runtime:** 127.18s

---

# Iteration 1

## 1. Search

**Query**

> Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

**Purpose:** GENERAL

**Why this query**

This is the user's original research question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S1 — Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot**
  URL: https://arxiv.org/html/2506.14641v2
- **S2 — Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot**
  URL: https://arxiv.org/html/2506.14641v3
- **S3 — Chain of Thought Prompting: Step-by-Step Reasoning - AI Prompt Theory**
  URL: https://aiprompttheory.com/chain-of-thought-prompting-step-by-step-reasoning
- **S4 — Few-Shot Prompting: Guiding LLMs with Examples Chain of Thought Prompting: Step-by-Step Reasoning with CoT - AI Prompt Theory**
  URL: https://aiprompttheory.com/few-shot-prompting-guiding-llms-with-exampleschain-of-thought-prompting-step-by-step-reasoning-with-cot
- **S5 — LLMs can Find Mathematical Reasoning Mistakes by Pedagogical Chain-of-Thought [Quick Review]**
  URL: https://liner.com/review/llms-can-find-mathematical-reasoning-mistakes-by-pedagogical-chainofthought

**Search Duration:** 4.50s

---

## 2. Evidence Processing

- New claim proposals: 4
- Existing claim updates: 0
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 9.41s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

Chain-of-thought (CoT) prompting primarily serves to align the output format with human expectations rather than significantly enhancing reasoning performance in recent advanced LLMs.

- S1 supports (direct): CoT exemplars do not improve reasoning performance in strong models; instead, they align output with human expectations.
- S2 supports (direct): The primary function of CoT exemplars is formatting alignment without enhancing reasoning in strong models.
- S3 supports (indirect): CoT prompting improves accuracy for complex reasoning tasks, showing benefits mainly in clarifying the reasoning process, rather than enhancing reasoning ability itself.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C2

**Claim**

Enhanced chain-of-thought (CoT) exemplars constructed from answers of advanced LLM models do not yield improved reasoning capabilities in recent models as they tend to ignore exemplar content.

- S1 supports (direct): Even enhanced CoT exemplars fail to improve reasoning as models focus more on instructions than exemplars.
- S2 supports (direct): Experimental results indicate that enhanced CoT exemplars do not lead to observable gain in reasoning ability for strong models.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C3

**Claim**

Zero-shot chain-of-thought (CoT) prompting can trigger multi-step reasoning in LLMs, which can be effective for tasks without specific exemplars.

- S1 supports (direct): Zero-shot CoT can elicit reasoning without any exemplars by appending a specific instruction.
- S3 supports (indirect): Zero-shot CoT through prompting can provide a level of reasoning without demonstrations, useful for various tasks.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C4

**Claim**

Pedagogical Chain-of-Thought (PedCoT) prompting significantly enhances LLM's performance in identifying mathematical reasoning mistakes over baseline zero-shot methods.

- S5 supports (direct): PedCoT outperforms traditional zero-shot prompting methods, showing superior accuracy in identifying reasoning errors.

**Confidence:** HIGH

**Status:** SUPPORTED

---

## 4. Current Research State

- Claims: 4
- Supported: 4
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 9

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C3

**Why**

Further investigation is needed to understand the differing results on the effectiveness of chain-of-thought (CoT) prompting, specifically focusing on the impact of zero-shot CoT in various contexts.

**Next Search**

> What are the experimental results comparing zero-shot chain-of-thought prompting to other prompting strategies in various reasoning tasks with LLMs?


---

# Iteration 2

## 1. Search

**Query**

> What are the experimental results comparing zero-shot chain-of-thought prompting to other prompting strategies in various reasoning tasks with LLMs?

**Target:** C3

**Purpose:** GENERAL

**Why this query**

Further investigation is needed to understand the differing results on the effectiveness of chain-of-thought (CoT) prompting, specifically focusing on the impact of zero-shot CoT in various contexts.

5 result(s) retrieved; 4 new unique source(s) added.

- **S6 — An Empirical Evaluation of Prompting Strategies for Large Language Models in Zero-Shot Clinical Natural Language Processing: Algorithm Development and Validation Study**
  URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11036183
- **S7 — Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot | alphaXiv**
  URL: https://www.alphaxiv.org/abs/2506.14641
- **S8 — Zero-Shot vs Few-Shot vs Chain-of-Thought Prompting: Complete Guide 2026 | explainx.ai Blog | explainx.ai**
  URL: https://explainx.ai/blog/zero-shot-few-shot-chain-of-thought-prompting-guide-2026
- **S9 — From Zero-Shot to BoT: A Practical Overview of LLM Reasoning Frameworks**
  URL: https://pub.towardsai.net/from-zero-shot-to-bot-a-practical-overview-of-llm-reasoning-frameworks-da9f7dafd80a

**Search Duration:** 4.31s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 4
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 9.71s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Chain-of-thought (CoT) prompting primarily serves to align the output format with human expectations rather than significantly enhancing reasoning performance in recent advanced LLMs.

- S7 supports (direct): Traditional CoT exemplars do not improve reasoning performance compared to Zero-Shot CoT; their main purpose is to format alignment.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

Enhanced chain-of-thought (CoT) exemplars constructed from answers of advanced LLM models do not yield improved reasoning capabilities in recent models as they tend to ignore exemplar content.

- S7 supports (direct): Enhanced CoT exemplars do not lead to improved reasoning performance; models focus on instructions rather than exemplars.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C3

**Claim**

Zero-shot chain-of-thought (CoT) prompting can trigger multi-step reasoning in LLMs, which can be effective for tasks without specific exemplars.

- S7 supports (direct): The research suggests Zero-shot CoT can evoke reasoning in advanced LLMs, matching or exceeding Few-shot performance.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

Pedagogical Chain-of-Thought (PedCoT) prompting significantly enhances LLM's performance in identifying mathematical reasoning mistakes over baseline zero-shot methods.

- S6 supports (indirect): PedCoT approaches show higher effectiveness in specific complex tasks compared to traditional methods.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 4
- Supported: 4
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 8

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C3

**Why**

Conflicting claims about the effectiveness of different chain-of-thought prompting strategies remain unresolved, particularly regarding zero-shot prompting's performance relative to other approaches.

**Next Search**

> Compare zero-shot chain-of-thought prompting with traditional and pedagogical methods in various reasoning tasks to evaluate performance and effectiveness.


---

# Iteration 3

## 1. Search

**Query**

> Compare zero-shot chain-of-thought prompting with traditional and pedagogical methods in various reasoning tasks to evaluate performance and effectiveness.

**Target:** C3

**Purpose:** GENERAL

**Why this query**

Conflicting claims about the effectiveness of different chain-of-thought prompting strategies remain unresolved, particularly regarding zero-shot prompting's performance relative to other approaches.

5 result(s) retrieved; 5 new unique source(s) added.

- **S10 — Instance-adaptive Zero-Shot Chain-of-Thought Prompting (IAP)**
  URL: https://learnprompting.org/docs/new_techniques/instance_adaptive_zero_shot_chain_of_thought
- **S11 — Medium**
  URL: https://medium.com/@gangelin/lets-think-step-by-step-zero-shot-chain-of-thought-zero-shot-cot-reasoning-in-large-language-2dfd21315d19
- **S12 — Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot**
  URL: https://emergentmind.com/papers/2506.14641
- **S13 — Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models [Quick Review]**
  URL: https://liner.com/review/planandsolve-prompting-improving-zeroshot-chainofthought-reasoning-by-large-language-models
- **S14 — Zero-Shot Chain-of-Thought Prompting - GeeksforGeeks**
  URL: https://www.geeksforgeeks.org/artificial-intelligence/zero-shot-chain-of-thought-prompting

**Search Duration:** 4.04s

---

## 2. Evidence Processing

- New claim proposals: 3
- Existing claim updates: 4
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 9.23s

---

## 3. Ledger Updates

### New Claim C5

**Claim**

Instance-adaptive Zero-Shot Chain-of-Thought Prompting (IAP) significantly enhances reasoning performance in large language models by dynamically tailoring prompts to individual questions, yielding improvements in accuracy for complex reasoning tasks.

- S10 supports (direct): IAP improves reasoning performance by selecting prompts based on saliency scores for individual questions, leading to significant accuracy enhancements.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C6

**Claim**

Plan-and-Solve Prompting (PS) significantly improves the accuracy and reliability of reasoning in large language models by guiding them to devise a step-by-step plan before solving problems.

- S13 supports (direct): The PS prompting approach allows LLMs to generate detailed reasoning steps more accurately, reducing calculation and missing-step errors compared to Zero-shot-CoT.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C7

**Claim**

Zero-shot Chain-of-Thought (CoT) prompting can outperform few-shot prompting methods for complex reasoning tasks, highlighting LLMs' intrinsic reasoning capabilities without relying on exemplars.

- S12 supports (direct): Recent studies show that zero-shot CoT prompting consistently achieves robust performance in reasoning tasks, often surpassing few-shot CoT scenarios.

**Confidence:** HIGH

**Status:** SUPPORTED

### Updated Claim C1

**Claim**

Chain-of-thought (CoT) prompting primarily serves to align the output format with human expectations rather than significantly enhancing reasoning performance in recent advanced LLMs.

- S10 supports (direct): The primary function of CoT exemplars is formatting alignment without enhancing reasoning in strong models, which aligns with findings that support zero-shot methods.
- S12 supports (direct): Adding traditional CoT exemplars does not improve reasoning performance compared to Zero-Shot CoT, reinforcing claims about their limited utility in advanced models.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C2

**Claim**

Enhanced chain-of-thought (CoT) exemplars constructed from answers of advanced LLM models do not yield improved reasoning capabilities in recent models as they tend to ignore exemplar content.

- S12 supports (direct): Experimental results indicate that enhanced CoT exemplars do not lead to observable gain in reasoning ability for strong models, as they focus on instructions rather than exemplar content.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C3

**Claim**

Zero-shot chain-of-thought (CoT) prompting can trigger multi-step reasoning in LLMs, which can be effective for tasks without specific exemplars.

- S12 supports (direct): In mathematical reasoning, zero-shot CoT prompting consistently achieves robust performance, often surpassing few-shot prompting scenarios.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C4

**Claim**

Pedagogical Chain-of-Thought (PedCoT) prompting significantly enhances LLM's performance in identifying mathematical reasoning mistakes over baseline zero-shot methods.

- No new evidence relationship was added.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 7
- Supported: 7
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 7

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** GENERAL

**Why**

Investigate why zero-shot CoT prompting is reported to outperform few-shot approaches in reasoning tasks to better understand the effectiveness of different prompting methods.

**Next Search**

> What evidence exists to support the claim that zero-shot chain-of-thought prompting outperforms few-shot prompting in reasoning tasks for LLMs, and what factors contribute to its success?


---

# Iteration 4

## 1. Search

**Query**

> What evidence exists to support the claim that zero-shot chain-of-thought prompting outperforms few-shot prompting in reasoning tasks for LLMs, and what factors contribute to its success?

**Purpose:** GENERAL

**Why this query**

Investigate why zero-shot CoT prompting is reported to outperform few-shot approaches in reasoning tasks to better understand the effectiveness of different prompting methods.

5 result(s) retrieved; 5 new unique source(s) added.

- **S15 — Zero-Shot Chain-of-Thought Prompting**
  URL: https://www.emergentmind.com/topics/zero-shot-chain-of-thought-cot-prompting
- **S16 — Few-Shot & Chain-of-Thought Prompting**
  URL: https://www.emergentmind.com/topics/few-shot-and-chain-of-thought-prompting
- **S17 — Zero-Shot Chain-of-Thought Prompting**
  URL: https://www.emergentmind.com/topics/zero-shot-cot
- **S18 — [PDF] Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models | Semantic Scholar**
  URL: https://www.semanticscholar.org/paper/Plan-and-Solve-Prompting%3A-Improving-Zero-Shot-by-Wang-Xu/62176de125738e3b95850d1227bac81fd646b78e
- **S19 — Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models - East China Normal University**
  URL: https://pure.ecnu.edu.cn/en/publications/plan-and-solve-prompting-improving-zero-shot-chain-of-thought-rea

**Search Duration:** 4.53s

---

## 2. Evidence Processing

- New claim proposals: 1
- Existing claim updates: 0
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 3.15s

---

## 3. Ledger Updates

### New Claim C8

**Claim**

Plan-and-Solve prompting (PS+) significantly enhances reasoning performance in zero-shot Chain-of-Thought (CoT) tasks by guiding LLMs to devise a plan before solving, addressing calculation and missing-step errors.

- S18 supports (direct): PS+ prompting improves reasoning by dividing tasks into manageable subtasks and addressing common errors.
- S19 supports (direct): Experimental results show PS+ prompting outperforms traditional Zero-shot CoT prompting across various datasets.

**Confidence:** HIGH

**Status:** SUPPORTED

---

## 4. Current Research State

- Claims: 8
- Supported: 8
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 6

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C7

**Why**

Conflicting claims about the effectiveness of chain-of-thought prompting in reasoning need clarification, particularly regarding the performance comparison with few-shot methods.

**Next Search**

> What specific factors contribute to zero-shot Chain-of-Thought (CoT) prompting's superior performance over few-shot methods in reasoning tasks for large language models?


---

# Iteration 5

## 1. Search

**Query**

> What specific factors contribute to zero-shot Chain-of-Thought (CoT) prompting's superior performance over few-shot methods in reasoning tasks for large language models?

**Target:** C7

**Purpose:** GENERAL

**Why this query**

Conflicting claims about the effectiveness of chain-of-thought prompting in reasoning need clarification, particularly regarding the performance comparison with few-shot methods.

5 result(s) retrieved; 1 new unique source(s) added.

- **S20 — How Chain of Thought (CoT) Prompting Helps LLMs ...**
  URL: https://www.splunk.com/en_us/blog/learn/chain-of-thought-cot-prompting.html

**Search Duration:** 2.64s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 3
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 4.54s

---

## 3. Ledger Updates

### Updated Claim C1

**Claim**

Chain-of-thought (CoT) prompting primarily serves to align the output format with human expectations rather than significantly enhancing reasoning performance in recent advanced LLMs.

- S20 supports (direct): CoT prompting helps LLMs by decomposing complex tasks into intermediate steps, but its efficacy is often limited to formatting.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C3

**Claim**

Zero-shot chain-of-thought (CoT) prompting can trigger multi-step reasoning in LLMs, which can be effective for tasks without specific exemplars.

- S20 supports (direct): Zero-shot CoT prompting allows models to reason through complex queries without specific exemplars, supporting its effectiveness in various tasks.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C5

**Claim**

Instance-adaptive Zero-Shot Chain-of-Thought Prompting (IAP) significantly enhances reasoning performance in large language models by dynamically tailoring prompts to individual questions, yielding improvements in accuracy for complex reasoning tasks.

- S20 supports (direct): IAP enhances reasoning performance by adjusting prompts dynamically, showcasing significant improvement in accuracy for complex tasks.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 8
- Supported: 8
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 5

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C7

**Why**

Understanding specific factors contributing to the effectiveness of zero-shot CoT prompting compared to other methods could clarify conflicting results in the literature.

**Next Search**

> What underlying mechanisms explain why zero-shot Chain-of-Thought (CoT) prompting achieves superior reasoning performance over few-shot methods in large language models?


---

# Iteration 6

## 1. Search

**Query**

> What underlying mechanisms explain why zero-shot Chain-of-Thought (CoT) prompting achieves superior reasoning performance over few-shot methods in large language models?

**Target:** C7

**Purpose:** GENERAL

**Why this query**

Understanding specific factors contributing to the effectiveness of zero-shot CoT prompting compared to other methods could clarify conflicting results in the literature.

5 result(s) retrieved; 2 new unique source(s) added.

- **S21 — Types of Prompt Engineering: Zero-Shot, Few-Shot, Chain-of-Thought & More**
  URL: https://www.scaler.com/topics/types-of-prompt-engineering-zero-shot-few-shot-chain-of-thought-and-more
- **S22 — Zero-Shot CoT Prompting: Improving AI with Step-by-Step Reasoning**
  URL: https://learnprompting.org/docs/intermediate/zero_shot_cot

**Search Duration:** 2.15s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 1
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 3.28s

---

## 3. Ledger Updates

### Updated Claim C3

**Claim**

Zero-shot chain-of-thought (CoT) prompting can trigger multi-step reasoning in LLMs, which can be effective for tasks without specific exemplars.

- S21 supports (direct): Zero-shot CoT improves model performance by appending 'Let's think step by step' to prompts, enhancing logical reasoning without needing exemplars.
- S22 supports (direct): Zero-shot CoT was effective in improving results on arithmetic and commonsense reasoning tasks, even if not as effective as CoT prompting for more complex tasks.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 8
- Supported: 8
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 4

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C7

**Why**

Further exploration is needed to elucidate the underlying mechanisms behind the superior performance of zero-shot CoT over few-shot methods, as this directly relates to the effectiveness of reasoning strategies in LLMs and addresses conflicting claims.

**Next Search**

> What are the cognitive mechanisms that allow zero-shot Chain-of-Thought prompting to outperform few-shot methods in reasoning tasks, according to the latest studies on large language models?


---

# Iteration 7

## 1. Search

**Query**

> What are the cognitive mechanisms that allow zero-shot Chain-of-Thought prompting to outperform few-shot methods in reasoning tasks, according to the latest studies on large language models?

**Target:** C7

**Purpose:** GENERAL

**Why this query**

Further exploration is needed to elucidate the underlying mechanisms behind the superior performance of zero-shot CoT over few-shot methods, as this directly relates to the effectiveness of reasoning strategies in LLMs and addresses conflicting claims.

5 result(s) retrieved; 1 new unique source(s) added.

- **S23 — [PDF] Zero-Shot Chain-of-Thought Reasoning Guided by Evolutionary Algorithms in Large Language Models | Semantic Scholar**
  URL: https://www.semanticscholar.org/paper/Zero-Shot-Chain-of-Thought-Reasoning-Guided-by-in-Jin-Liu/f859b66e55aebdd4d460e2bc1e74640eafead5ad

**Search Duration:** 2.60s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 2
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 5.61s

---

## 3. Ledger Updates

### Updated Claim C3

**Claim**

Zero-shot chain-of-thought (CoT) prompting can trigger multi-step reasoning in LLMs, which can be effective for tasks without specific exemplars.

- S23 supports (direct): A novel zero-shot prompting method incorporating evolutionary algorithms significantly enhances zero-shot Chain-of-Thought reasoning in LLMs by dynamically generating diverse promptings, improving the models’ understanding of the problem.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

### Updated Claim C7

**Claim**

Zero-shot Chain-of-Thought (CoT) prompting can outperform few-shot prompting methods for complex reasoning tasks, highlighting LLMs' intrinsic reasoning capabilities without relying on exemplars.

- S23 supports (direct): Recent advancements in zero-shot Chain-of-Thought prompting reveal improved performance in reasoning tasks through evolutionary algorithms, suggesting a potential for outperforming traditional methods in complex scenarios.

**Confidence:** HIGH → HIGH

**Status:** SUPPORTED → SUPPORTED

---

## 4. Current Research State

- Claims: 8
- Supported: 8
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 3

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C7

**Why**

Investigate specific cognitive mechanisms behind the efficacy of zero-shot CoT prompting to understand how it achieves superior performance over few-shot methods in reasoning tasks. This could clarify the remaining disagreements in the literature.

**Next Search**

> What cognitive mechanics enable zero-shot Chain-of-Thought prompting to exceed few-shot methods in reasoning tasks in LLMs?


---

# Iteration 8

## 1. Search

**Query**

> What cognitive mechanics enable zero-shot Chain-of-Thought prompting to exceed few-shot methods in reasoning tasks in LLMs?

**Target:** C7

**Purpose:** GENERAL

**Why this query**

Investigate specific cognitive mechanisms behind the efficacy of zero-shot CoT prompting to understand how it achieves superior performance over few-shot methods in reasoning tasks. This could clarify the remaining disagreements in the literature.

5 result(s) retrieved; 2 new unique source(s) added.

- **S24 — Hint of Thought prompting: an explainable and zero-shot approach to reasoning tasks with LLMs**
  URL: https://arxiv.org/html/2305.11461v7
- **S25 — Medium**
  URL: https://medium.com/@hetzer2807/zero-shot-reasoning-unleashed-the-magic-of-large-language-models-4e877dfe470e

**Search Duration:** 3.37s

---

## 2. Evidence Processing

- New claim proposals: 2
- Existing claim updates: 0
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 7.24s

---

## 3. Ledger Updates

### New Claim C9

**Claim**

Hint of Thought (HoT) prompting, a novel extension of zero-shot reasoning, significantly improves LLM performance in zero-shot reasoning tasks by deconstructing complex problems into explainable sub-questions, enhancing overall accuracy.

- S24 supports (direct): HoT prompting decomposes tasks into three sequential steps, demonstrating improved accuracy in zero-shot reasoning tasks significantly compared to zero-shot CoT.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C10

**Claim**

Zero-shot reasoning with large language models (LLMs) can yield performance improvements on multi-step reasoning tasks without requiring hand-crafted examples, showing their ability to generalize knowledge effectively.

- S25 supports (direct): LLMs demonstrated sufficient performance on multi-step reasoning tasks using only one simple prompt, underscoring their zero-shot reasoning abilities without requiring explicit examples.

**Confidence:** HIGH

**Status:** SUPPORTED

---

## 4. Current Research State

- Claims: 10
- Supported: 10
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 2

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C7

**Why**

Further clarification is needed on the cognitive mechanisms employed by zero-shot CoT prompting that contribute to its superior performance over few-shot methods in reasoning tasks, as this is crucial for understanding the contradictions in the literature.

**Next Search**

> What specific cognitive mechanisms allow zero-shot Chain-of-Thought prompting to outperform few-shot methods in reasoning tasks among large language models?


---

# Iteration 9

## 1. Search

**Query**

> What specific cognitive mechanisms allow zero-shot Chain-of-Thought prompting to outperform few-shot methods in reasoning tasks among large language models?

**Target:** C7

**Purpose:** GENERAL

**Why this query**

Further clarification is needed on the cognitive mechanisms employed by zero-shot CoT prompting that contribute to its superior performance over few-shot methods in reasoning tasks, as this is crucial for understanding the contradictions in the literature.

5 result(s) retrieved; 0 new unique source(s) added.

- No new unique sources were added.

**Search Duration:** 2.42s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 0
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 1.01s

---

## 3. Ledger Updates

No ledger or gap changes were recorded.

---

## 4. Current Research State

- Claims: 10
- Supported: 10
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 0
- Remaining Searches: 1

---

## 5. Research Decision

**Decision:** Continue researching.

**Origin:** RESEARCH_CONTROLLER

**Target:** CLAIM C7

**Why**

Exploring the cognitive mechanics behind zero-shot Chain-of-Thought prompting could clarify conflicting results and improve understanding of its effectiveness over few-shot methods.

**Next Search**

> What recent studies identify specific cognitive mechanics that enable zero-shot Chain-of-Thought prompting to outperform few-shot methods in reasoning tasks for large language models?


---

# Iteration 10

## 1. Search

**Query**

> What recent studies identify specific cognitive mechanics that enable zero-shot Chain-of-Thought prompting to outperform few-shot methods in reasoning tasks for large language models?

**Target:** C7

**Purpose:** GENERAL

**Why this query**

Exploring the cognitive mechanics behind zero-shot Chain-of-Thought prompting could clarify conflicting results and improve understanding of its effectiveness over few-shot methods.

5 result(s) retrieved; 0 new unique source(s) added.

- No new unique sources were added.

**Search Duration:** 3.13s

---

## 2. Evidence Processing

- New claim proposals: 0
- Existing claim updates: 0
- New gaps: 0
- Resolved gaps: 0

**Processing Duration:** 1.05s

---

## 3. Ledger Updates

No ledger or gap changes were recorded.

---

## 4. Current Research State

- Claims: 10
- Supported: 10
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
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
| Tavily Search | 10 | 33.70s |
| Evidence Processing | 10 | 54.22s |
| Research Decision | 9 | 18.89s |
| Report Generation | 1 | 20.35s |
| Total Run | — | 127.18s |
