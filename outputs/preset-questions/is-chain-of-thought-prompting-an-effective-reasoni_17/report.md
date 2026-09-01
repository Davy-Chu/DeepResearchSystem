# Research Report

## Research Question

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

## Summary

The evidence evaluated provides a nuanced view of chain-of-thought (CoT) prompting in large language models (LLMs). Although some studies endorse the effectiveness of CoT prompting for enhancing reasoning, others suggest its primary role is in aligning output formats with human expectations. There is significant support for various prompting strategies, yet clear divisions persist regarding the effectiveness of CoT compared to zero-shot and enhanced methods.

## Findings

### Finding 1

**Claim**

Chain-of-thought (CoT) prompting primarily serves to align the output format with human expectations rather than significantly enhancing reasoning performance in recent advanced LLMs.

**Confidence:** High

**Why this confidence level**

The additional evidence reaffirms that while CoT prompting can improve formatting and clarify thought processes, its contribution to reasoning enhancement remains questionable. Subsequent studies align with this view.

**Evidence**

- CoT exemplars do not improve reasoning performance in strong models; instead, they align output with human expectations. [S1]
- The primary function of CoT exemplars is formatting alignment without enhancing reasoning in strong models. [S2]
- CoT prompting improves accuracy for complex reasoning tasks, showing benefits mainly in clarifying the reasoning process, rather than enhancing reasoning ability itself. [S3]

### Finding 2

**Claim**

Enhanced chain-of-thought (CoT) exemplars constructed from answers of advanced LLM models do not yield improved reasoning capabilities in recent models as they tend to ignore exemplar content.

**Confidence:** High

**Why this confidence level**

The addition of robust evidence confirms that even enhanced CoT exemplars fail to improve reasoning in advanced models.

**Evidence**

- Even enhanced CoT exemplars fail to improve reasoning as models focus more on instructions than exemplars. [S1]

### Finding 3

**Claim**

Zero-shot chain-of-thought (CoT) prompting can trigger multi-step reasoning in LLMs, which can be effective for tasks without specific exemplars.

**Confidence:** High

**Why this confidence level**

The new evidence supports and enhances the claim regarding the effectiveness of zero-shot Chain-of-Thought prompting.

**Evidence**

- Zero-shot CoT can elicit reasoning without any exemplars by appending a specific instruction. [S1]

### Finding 4

**Claim**

Pedagogical Chain-of-Thought (PedCoT) prompting significantly enhances LLM's performance in identifying mathematical reasoning mistakes over baseline zero-shot methods.

**Confidence:** High

**Why this confidence level**

Continued evidence supports the effectiveness of PedCoT as a strong technique for identifying reasoning errors.

**Evidence**

- PedCoT outperforms traditional zero-shot prompting methods, showing superior accuracy in identifying reasoning errors. [S5]

### Finding 5

**Claim**

Instance-adaptive Zero-Shot Chain-of-Thought Prompting (IAP) significantly enhances reasoning performance in large language models by dynamically tailoring prompts.

**Confidence:** High

**Why this confidence level**

The findings bolster the effectiveness of IAP in tailoring responses for complex reasoning tasks, aligning with prior claims of its utility.

**Evidence**

- IAP improves reasoning performance by selecting prompts based on saliency scores for individual questions. [S10]

### Finding 6

**Claim**

Plan-and-Solve Prompting (PS) significantly improves the accuracy and reliability of reasoning in LLMs by guiding them to devise a step-by-step plan before solving problems.

**Confidence:** High

**Why this confidence level**

Evidence demonstrates that PS+ prompting effectively mitigates common reasoning errors.

**Evidence**

- The PS prompting approach allows LLMs to generate detailed reasoning steps more accurately, reducing calculation and missing-step errors. [S13]

### Finding 7

**Claim**

Hint of Thought (HoT) prompting significantly improves LLM performance in zero-shot reasoning tasks by deconstructing complex problems into explainable sub-questions.

**Confidence:** High

**Why this confidence level**

The evidence strongly supports the claim of HoT prompting's effectiveness in enhancing zero-shot reasoning capabilities of LLMs.

**Evidence**

- HoT prompting decomposes tasks into three sequential steps, demonstrating improved accuracy in zero-shot reasoning tasks significantly compared to zero-shot CoT. [S24]

## Conflicts and Uncertainty

- No material conflict was identified in the retrieved evidence.

## Remaining Gaps

- No major remaining gap was identified within the research scope.

## Conclusion

While there is strong evidence supporting the benefits of various prompting techniques like zero-shot, PedCoT, and instance-adaptive IAP, the debate surrounding chain-of-thought prompting's role continues, particularly with an emphasis on its formatting utility versus reasoning enhancements.

## Sources

- [S1] Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot — https://arxiv.org/html/2506.14641v2
- [S2] Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot — https://arxiv.org/html/2506.14641v3
- [S3] Chain of Thought Prompting: Step-by-Step Reasoning - AI Prompt Theory — https://aiprompttheory.com/chain-of-thought-prompting-step-by-step-reasoning
- [S4] Few-Shot Prompting: Guiding LLMs with Examples Chain of Thought Prompting: Step-by-Step Reasoning with CoT - AI Prompt Theory — https://aiprompttheory.com/few-shot-prompting-guiding-llms-with-exampleschain-of-thought-prompting-step-by-step-reasoning-with-cot
- [S5] LLMs can Find Mathematical Reasoning Mistakes by Pedagogical Chain-of-Thought [Quick Review] — https://liner.com/review/llms-can-find-mathematical-reasoning-mistakes-by-pedagogical-chainofthought
- [S6] An Empirical Evaluation of Prompting Strategies for Large Language Models in Zero-Shot Clinical Natural Language Processing: Algorithm Development and Validation Study — https://pmc.ncbi.nlm.nih.gov/articles/PMC11036183
- [S7] Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot | alphaXiv — https://www.alphaxiv.org/abs/2506.14641
- [S8] Zero-Shot vs Few-Shot vs Chain-of-Thought Prompting: Complete Guide 2026 | explainx.ai Blog | explainx.ai — https://explainx.ai/blog/zero-shot-few-shot-chain-of-thought-prompting-guide-2026
- [S9] From Zero-Shot to BoT: A Practical Overview of LLM Reasoning Frameworks — https://pub.towardsai.net/from-zero-shot-to-bot-a-practical-overview-of-llm-reasoning-frameworks-da9f7dafd80a
- [S10] Instance-adaptive Zero-Shot Chain-of-Thought Prompting (IAP) — https://learnprompting.org/docs/new_techniques/instance_adaptive_zero_shot_chain_of_thought
- [S11] Medium — https://medium.com/@gangelin/lets-think-step-by-step-zero-shot-chain-of-thought-zero-shot-cot-reasoning-in-large-language-2dfd21315d19
- [S12] Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot — https://emergentmind.com/papers/2506.14641
- [S13] Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models [Quick Review] — https://liner.com/review/planandsolve-prompting-improving-zeroshot-chainofthought-reasoning-by-large-language-models
- [S14] Zero-Shot Chain-of-Thought Prompting - GeeksforGeeks — https://www.geeksforgeeks.org/artificial-intelligence/zero-shot-chain-of-thought-prompting
- [S15] Zero-Shot Chain-of-Thought Prompting — https://www.emergentmind.com/topics/zero-shot-chain-of-thought-cot-prompting
- [S16] Few-Shot & Chain-of-Thought Prompting — https://www.emergentmind.com/topics/few-shot-and-chain-of-thought-prompting
- [S17] Zero-Shot Chain-of-Thought Prompting — https://www.emergentmind.com/topics/zero-shot-cot
- [S18] [PDF] Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models | Semantic Scholar — https://www.semanticscholar.org/paper/Plan-and-Solve-Prompting%3A-Improving-Zero-Shot-by-Wang-Xu/62176de125738e3b95850d1227bac81fd646b78e
- [S19] Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models - East China Normal University — https://pure.ecnu.edu.cn/en/publications/plan-and-solve-prompting-improving-zero-shot-chain-of-thought-rea
- [S20] How Chain of Thought (CoT) Prompting Helps LLMs ... — https://www.splunk.com/en_us/blog/learn/chain-of-thought-cot-prompting.html
- [S21] Types of Prompt Engineering: Zero-Shot, Few-Shot, Chain-of-Thought & More — https://www.scaler.com/topics/types-of-prompt-engineering-zero-shot-few-shot-chain-of-thought-and-more
- [S22] Zero-Shot CoT Prompting: Improving AI with Step-by-Step Reasoning — https://learnprompting.org/docs/intermediate/zero_shot_cot
- [S23] [PDF] Zero-Shot Chain-of-Thought Reasoning Guided by Evolutionary Algorithms in Large Language Models | Semantic Scholar — https://www.semanticscholar.org/paper/Zero-Shot-Chain-of-Thought-Reasoning-Guided-by-in-Jin-Liu/f859b66e55aebdd4d460e2bc1e74640eafead5ad
- [S24] Hint of Thought prompting: an explainable and zero-shot approach to reasoning tasks with LLMs — https://arxiv.org/html/2305.11461v7
- [S25] Medium — https://medium.com/@hetzer2807/zero-shot-reasoning-unleashed-the-magic-of-large-language-models-4e877dfe470e
