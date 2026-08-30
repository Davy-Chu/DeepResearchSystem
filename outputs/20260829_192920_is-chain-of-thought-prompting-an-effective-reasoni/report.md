# Research Report

## Research Question

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees-find the real fault lines and explain what accounts for the conflicting results.

## Summary

The accumulated evidence supports neither a universal “CoT improves reasoning” conclusion nor a universal “CoT is only formatting” conclusion. CoT appears most useful when a task genuinely requires sequential intermediate computation and the model does not already have a native reasoning mechanism. Its effects become small, inconsistent, or negative for models that already reason internally, for easy tasks, and under metrics sensitive to occasional errors or variability. Some reported gains may reflect output-format imitation, additional computation, extra tokens, or structured decomposition rather than a distinct improvement in latent reasoning. The central causal question remains unresolved because the retrieved material lacks strong comparisons matched for token budget, computation, format, and model regime.

## Findings

### Finding 1

**Claim**

CoT is conditionally effective: benefits depend on model type, task difficulty, and evaluation metric.

**Confidence:** Medium

**Why this confidence level**

The pattern is reported across a systematic evaluation and a corroborating secondary source, but the retrieved material does not include the full primary study or complete statistical tables.

**Evidence**

- A repeated-trial GPQA Diamond evaluation found modest average gains for some non-reasoning models, minimal gains for reasoning models, declines for some models, and different results under average-, majority-, and perfect-accuracy metrics. [S2]
- A secondary synthesis similarly describes larger gains on difficult sequential tasks and weak or negative effects elsewhere. [S8]

### Finding 2

**Claim**

For non-reasoning models and genuinely multistep tasks, explicit intermediate reasoning can improve accuracy, but it can also increase variability and cause errors on cases that direct prompting would have solved.

**Confidence:** Medium

**Why this confidence level**

Two sources converge on conditional gains and occasional degradation, although the underlying trial-level analysis is not available here.

**Evidence**

- On GPQA Diamond, reported average gains for non-reasoning models ranged from 4.4% to 13.5%, while perfect-accuracy outcomes were mixed; Gemini Pro 1.5 reportedly declined by 17.2%. [S2]
- The same model-specific decline and an overthinking/second-guessing explanation are reported in the secondary discussion. [S8]

### Finding 3

**Claim**

For models with native reasoning mechanisms, a generic “think step by step” instruction usually adds little measured accuracy and can impose substantial latency or token costs.

**Confidence:** Medium

**Why this confidence level**

The numerical performance pattern is supported by the reported evaluation; the claim that the extra tokens amount to duplicative reasoning is interpretive and not directly demonstrated.

**Evidence**

- The GPQA evaluation reported only 2.9% and 3.1% average gains for o3-mini and o4-mini, a 3.3% decline for Gemini Flash 2.5, and 20–80% longer response times for reasoning models. [S2]
- A secondary account characterizes explicit CoT as often redundant for native reasoning models and reports increased token usage and latency relative to modest gains. [S8]

### Finding 4

**Claim**

The apparent conflict partly arises because “CoT” names different interventions: zero-shot instructions, few-shot rationale demonstrations, automated demonstrations, self-consistency, and structured variants are not equivalent.

**Confidence:** High

**Why this confidence level**

The definitional distinction is explicit in both sources, though the sources do not isolate the causal contribution of each component.

**Evidence**

- The tutorial sources explicitly distinguish zero-shot CoT (“Let’s think step by step”) from few-shot CoT containing worked reasoning examples, and describe additional variants such as Auto-CoT and self-consistency. [S6] [S7]
- Auto-CoT is described as selecting diverse demonstrations and generating rationale chains, with possible errors in the generated demonstrations. [S7]

### Finding 5

**Claim**

Some CoT gains may be due to formatting, behavioral elicitation, or extra computational workspace rather than a new reasoning capability.

**Confidence:** Low

**Why this confidence level**

This is the key causal fault line, but the strongest formatting claim is reported only indirectly, and none of the retrieved sources provides a controlled format-matched test.

**Evidence**

- The Hi-CoT paper reports that cited recent work finds CoT exemplars primarily enforce output format for modern LLMs, while the Wharton study notes that many models produce CoT-like outputs by default without an explicit instruction. [S1] [S2]
- The tutorial material treats visible intermediate steps as evidence of improved reasoning but also acknowledges that reasoning chains may be incorrect or unfaithful. [S6] [S7]

### Finding 6

**Claim**

Structure may matter more than verbosity: adaptive planning, concise intermediate states, and compression can outperform or match flat verbose CoT while reducing output length.

**Confidence:** Low

**Why this confidence level**

The sources support the hypothesis that useful computation need not be verbose, but the claims come from a recent preprint and a secondary blog without the equal-token, equal-computation, or independent replication controls needed to identify the mechanism.

**Evidence**

- Hi-CoT reports a 6.2% average accuracy improvement and a 13.9% shorter reasoning trace than ordinary CoT across 13 model configurations and five mathematical benchmarks, attributing the effect to adaptive planning and compression bottlenecks. [S1]
- A secondary source reports favorable results for concise CoT, Chain-of-Draft, and token-budgeted reasoning methods, including substantial reductions in token use. [S8]

### Finding 7

**Claim**

Broad positive claims in tutorials and explanatory material overstate what can be inferred from the controlled evidence.

**Confidence:** High

**Why this confidence level**

The genre difference is clear from the retrieved content: the tutorial and explanatory sources present definitions and examples, whereas S2 reports repeated trials across models and metrics.

**Evidence**

- PromptHub, Prompting Guide, IBM, and an instructional video describe CoT as improving reasoning, accuracy, transparency, or reliability, often using illustrative arithmetic examples rather than systematic comparisons. [S4] [S6] [S7] [S9] [S10]
- The more systematic GPQA summary instead reports model-sensitive, metric-sensitive, and sometimes negative effects. [S2]

## Conflicts and Uncertainty

- S1 presents CoT and Hi-CoT as strong reasoning improvements, whereas S2 finds generic CoT marginal or harmful for several native reasoning models. These results may concern different model generations, tasks, and prompt structures rather than a direct contradiction. [S1] [S2]
- S4, S6, S7, S9, and S10 describe visible intermediate reasoning as evidence of improved reasoning, while S1 and S2 raise the possibility that modern models already reason by default or that CoT mainly enforces a format. The retrieved material does not settle this causal distinction. [S1] [S2] [S4] [S6] [S7] [S9] [S10]
- CoT can improve average accuracy while reducing perfect accuracy for some models. Whether it is beneficial therefore depends on whether the evaluation rewards mean performance, majority correctness, worst-case reliability, or error-free performance. [S2]
- S8 explains weak gains on reasoning models as duplicated or redundant reasoning, but S2 reports the numerical pattern without proving that redundancy is the mechanism. [S2] [S8]
- Claims that concise or hierarchical reasoning preserves accuracy at lower cost are compatible with one another, but the sources do not determine whether the benefit comes from shorter traces, better planning, altered formatting, or different amounts of computation. [S1] [S8]

## Remaining Gaps

- A controlled comparison matching direct prompting and CoT for output-token budget, total computation, latency, and response format.
- A causal test separating rationale demonstrations from the mere instruction to produce intermediate steps.
- Evidence testing whether visible natural-language traces are faithful to the process that produced the answer.
- Independent replication of the reported Hi-CoT, Chain-of-Draft, early-stopping, and token-budget results.
- Broader evaluation across difficult reasoning tasks and realistic task mixtures, rather than selected examples or a single benchmark.
- A direct comparison of explicit CoT with models’ native internal reasoning modes under matched resource budgets.

## Conclusion

The best-supported synthesis is that CoT is a conditional reasoning aid, not a universal reasoning switch and not demonstrably mere formatting. It can provide a useful intermediate workspace or decomposition for difficult sequential problems, particularly in models without strong native reasoning behavior. However, explicit CoT often adds little to models that already reason internally, can cause overthinking and variability, and carries meaningful token and latency costs. The literature conflicts because studies compare different model regimes, task difficulties, CoT variants, correctness metrics, and evidentiary standards; many positive accounts rely on illustrative examples, while the stronger comparative evidence finds heterogeneous effects. The formatting-versus-reasoning question remains open: the accumulated sources suggest that format, extra computation, and structured intermediate state may all contribute, but do not identify their separate causal effects.

## Sources

- [S1] Hierarchical Chain-of-Thought Prompting: Enhancing LLM Reasoning Performance and Efficiency — https://arxiv.org/html/2604.00130v1
- [S2] The Decreasing Value of Chain of Thought in Prompting — https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought
- [S3] Contrastive Chain-Of-Thought Prompting — https://www.kore.ai/blog/contrastive-chain-of-thought-prompting
- [S4] What is chain of thought (CoT) prompting? — https://www.ibm.com/think/topics/chain-of-thoughts
- [S5] Medium — https://cobusgreyling.medium.com/chain-of-thought-prompting-in-llms-1077164edf97
- [S6] PromptHub Blog: Chain of Thought Prompting Guide — https://www.prompthub.us/blog/chain-of-thought-prompting-guide
- [S7] Chain-of-Thought (CoT) Prompting — https://www.promptingguide.ai/techniques/cot
- [S8] The Token Economics of Chain-of-Thought: When Thinking Out Loud Costs More Than It's Worth — https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more
- [S9] Chain of Thought Prompting in AI: A Comprehensive Guide [2026] — https://orq.ai/blog/what-is-chain-of-thought-prompting
- [S10] What is Chain of Thought Prompting? (2026) — https://www.youtube.com/watch?v=Qe7DxM5PxPs&vl=en
