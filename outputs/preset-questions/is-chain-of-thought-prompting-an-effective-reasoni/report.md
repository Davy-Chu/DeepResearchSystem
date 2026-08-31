# Research Report

## Research Question

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

## Summary

The evidence supports neither a universal “CoT works” nor a universal “CoT is only formatting” conclusion. Chain-of-thought prompting can improve accuracy for some weaker or non-reasoning models on difficult multi-step tasks. For stronger contemporary models—especially those with built-in reasoning—generic CoT instructions and few-shot rationales often add little reasoning capability, may mainly align output format, and can impose latency and token costs. The main fault lines are model capability, the exact prompting intervention, task structure, evaluation methodology, and whether cost, consistency, or only average accuracy is measured.

## Findings

### Finding 1

**Claim**

CoT is conditionally effective, rather than a universally effective reasoning strategy.

**Confidence:** Medium

**Why this confidence level**

The conditional pattern is directly supported by an empirical comparison, but much of the retrieved material consists of secondary explainers.

**Evidence**

- A controlled GPQA Diamond study found modest average gains for several non-reasoning models, but marginal or negative effects for some built-in reasoning models. [S3]
- Instructional sources describe benefits on multi-step arithmetic, mathematical, symbolic, commonsense, and planning tasks, though they do not provide controlled causal evidence. [S4] [S5]

### Finding 2

**Claim**

For strong or reasoning-oriented models, generic CoT prompting and few-shot CoT exemplars may be redundant and may primarily affect response format rather than reasoning ability.

**Confidence:** Medium

**Why this confidence level**

The formatting interpretation is directly reported for recent mathematical-reasoning experiments and is consistent with the GPQA results, but the evidence comes from limited model and task samples and does not establish that all forms of CoT are formatting-only.

**Evidence**

- Experiments on GSM8K and MATH report that recent strong models gained no reasoning improvement from traditional CoT exemplars over zero-shot CoT; the reported primary effect was alignment with human-expected output format. [S6]
- The same study reports that even enhanced exemplars were often ignored by strong models, which focused more on the instructions than on the exemplar content. [S6]
- The GPQA study reports that many contemporary models already produce CoT-like reasoning by default and that generic CoT yielded only small gains for tested reasoning models. [S3]

### Finding 3

**Claim**

CoT can help non-reasoning models, but its benefits may trade off against consistency, latency, and token cost.

**Confidence:** Medium

**Why this confidence level**

The source directly measures accuracy, variability, and timing, but the retrieved material does not include the complete results tables or independent replication.

**Evidence**

- The GPQA study reports average gains for several non-reasoning models, including reported gains of 13.5% for Gemini Flash 2.0 and 11.7% for Sonnet 3.5, while also finding mixed or negative effects under a perfect-accuracy criterion. [S3]
- The study reports increased answer variability and response-time increases of 35–600% for non-reasoning models. [S3]

### Finding 4

**Claim**

The useful ingredient may be structured intermediate representations and planning, not simply longer verbal reasoning traces.

**Confidence:** Medium

**Why this confidence level**

Two task-specific studies point toward benefits from structure rather than verbosity, but both are individual studies and do not establish generalization across tasks or isolate planning from other prompt changes.

**Evidence**

- Hi-CoT reports higher average accuracy and shorter traces than flat CoT, attributing the result to adaptive planning, execution grounding, and compression bottlenecks. [S1]
- Structured CoT for code generation, using sequential, branch, and loop structures, reportedly outperformed ordinary CoT by up to 13.79% Pass@1 across code-generation benchmarks and models. [S8]

### Finding 5

**Claim**

The apparent contradiction in the literature is largely explained by differences in model capability, intervention type, task, evaluation procedure, and success criteria.

**Confidence:** High

**Why this confidence level**

Multiple sources independently identify model family, evaluation, task representation, and cost as moderators, providing a coherent explanation for divergent headline results.

**Evidence**

- The GPQA study reports different effects for non-reasoning and built-in reasoning models, as well as different conclusions under average-performance versus perfect-accuracy thresholds. [S3]
- The GSM8K/MATH study identifies an evaluation bias that underestimated zero-shot CoT, which could make few-shot CoT appear more beneficial than it is. [S6]
- Code-generation and mathematical studies report larger gains from task-aligned structured variants than from ordinary generic CoT. [S8] [S1]
- The instructional examples change both the requested reasoning process and the output format, so they cannot determine whether improved answers result from latent reasoning, decomposition, or compliance with a format. [S9] [S10]

### Finding 6

**Claim**

Canonical demonstrations showing that “think step by step” can produce a correct answer do not by themselves establish genuine reasoning improvement.

**Confidence:** High

**Why this confidence level**

The limitation follows directly from the design of the cited examples and is consistent with the controlled studies, although the exact causal contribution of formatting remains unresolved.

**Evidence**

- Secondary guides present arithmetic examples where direct prompting fails and step-by-step prompting succeeds, but they do not hold output format, trace visibility, length, or decoding constant. [S9] [S10]
- The broader empirical evidence reports both formatting-only effects for exemplars and genuine accuracy changes for some non-reasoning models, leaving the causal mechanism conditional. [S6] [S3]

## Conflicts and Uncertainty

- Some sources characterize CoT as genuine stepwise reasoning that improves decomposition, error detection, and accuracy, while recent studies report that CoT exemplars primarily align output format in strong models. These claims need not be mutually exclusive: formatting or instruction-following may unlock useful behavior in weaker models, while adding exemplars may be stylistic or redundant for stronger models. [S4] [S5] [S6] [S3]
- Structured and hierarchical CoT studies report meaningful gains and shorter traces, whereas generic CoT is reported to be marginal and costly for some reasoning models. The interventions are not equivalent: structured methods alter the representation and control of reasoning rather than merely adding a step-by-step instruction. [S1] [S8] [S3]
- The retrieved evidence does not directly test whether CoT improves hidden problem-solving ability when answer format, output length, trace visibility, and decoding procedure are held constant. [S3] [S6] [S9] [S10]
- The strongest empirical findings are concentrated in mathematical, scientific multiple-choice, and code-generation settings; the evidence does not establish comparable effects for open-ended, adversarial, or out-of-distribution tasks. [S1] [S3] [S6] [S8]

## Remaining Gaps

- A controlled causal comparison holding output format, response length, trace visibility, and decoding conditions constant.
- Independent replication of the reported formatting-only effect of CoT exemplars.
- Systematic separation of zero-shot instructions, few-shot rationales, structured representations, and built-in model reasoning.
- Evaluation across non-mathematical, open-ended, adversarial, and out-of-distribution tasks.
- A common evaluation framework that jointly reports accuracy, consistency, latency, token usage, and cost.

## Conclusion

Chain-of-thought prompting is best understood as an elicitation and control technique whose value depends on the model and task—not as a universally reliable reasoning upgrade. It can materially help some non-reasoning models on difficult multi-step problems, but for strong modern models, especially those with native reasoning, generic CoT or few-shot rationales may be redundant and may chiefly impose a response format. The most promising evidence concerns structured, task-aligned intermediate representations, which can outperform flat verbal chains while using fewer tokens. Thus, the real fault line is not “reasoning versus formatting” in the abstract: it is whether a particular prompt supplies a missing computational scaffold, merely changes presentation, or redundantly requests behavior the model already performs. The retrieved literature supports this conditional account, but does not yet settle the underlying causal question under fully controlled formatting and visibility conditions.

## Sources

- [S1] Hierarchical Chain-of-Thought Prompting: Enhancing LLM Reasoning Performance and Efficiency — https://arxiv.org/html/2604.00130v1
- [S2] Medium — https://medium.com/@tahirbalarabe2/what-is-llm-chain-of-thought-prompting-1d4b57a4dd22
- [S3] Technical Report: The Decreasing Value of Chain of Thought in Prompting - Wharton Generative AI Labs — https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought
- [S4] What is chain of thought (CoT) prompting? - IBM — https://www.ibm.com/think/topics/chain-of-thoughts
- [S5] What is Chain of Thought (CoT) Prompting? | NVIDIA Glossary — https://www.nvidia.com/en-us/glossary/cot-prompting
- [S6] Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot — https://arxiv.org/html/2506.14641v3
- [S7] Chain of Thought Prompting Guide - PromptHub — https://www.prompthub.us/blog/chain-of-thought-prompting-guide
- [S8] [PDF] Structured Chain-of-Thought Prompting for Code Generation — https://ligechina.github.io/My%20Papers/2025%20-%20TOSEM%20-%20Structured%20Chain-of-Thought%20Prompting%20for%20Code%20Generation.pdf
- [S9] Chain-of-Thought (CoT) Prompting — https://www.promptingguide.ai/techniques/cot
- [S10] Master Prompting Concepts: Chain of Thought Prompting — https://promptengineering.org/master-prompting-concepts-chain-of-thought-prompting
