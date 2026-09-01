# Research Report

## Research Question

Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

## Summary

The accumulated literature rejects both simple extremes. Chain-of-thought (CoT) can improve accuracy on difficult, decomposable tasks, and causal studies find that some models use some intermediate steps in solving arithmetic problems. But the visible natural-language chain is not reliably the model’s actual reasoning process: chains may be unnecessary, redundant, post-hoc, distribution-sensitive, or overridden by an explicit final answer. Many results also conflate semantic intermediate computation with extra serial inference, task-specific schemas, demonstrations, delimiters, answer placement, and output-format effects. The best-supported account is therefore conditional and three-way: useful intermediate computation can occur; generic additional computation can help; and surface format/readout conventions can independently alter performance. Verbal CoT is neither merely cosmetic nor universally faithful or necessary.

## Findings

### Finding 1

**Claim**

CoT is an effective accuracy intervention in some regimes, especially difficult tasks requiring sequential or compositional reasoning, but not a universal improvement.

**Confidence:** High

**Why this confidence level**

The task-dependent pattern is supported across multiple research-oriented sources, though the sources do not form a formal meta-analysis.

**Evidence**

- Classic CoT accounts report gains over direct or standard few-shot prompting on arithmetic, symbolic, and some commonsense tasks; other evidence finds that gains are concentrated on difficult, decomposable questions and can be neutral or negative on simpler tasks. [S4] [S9] [S13] [S18]
- In code generation, generic CoT reportedly produced only slight gains in one cited real-world benchmark, motivating structured alternatives. [S1]

### Finding 2

**Claim**

The visible chain is not a reliable proxy for the computation that produced the answer. Accuracy and faithfulness are separate properties.

**Confidence:** High

**Why this confidence level**

Several independent methods converge on heterogeneous causal use: some chains matter, but correctness of the final answer does not establish that the visible chain was followed.

**Evidence**

- Causal mediation work reports weak or inconsistent use of generated chains by vanilla LMs, despite their sometimes improved final accuracy; instruction tuning or CoT-related training can improve mediation but does not make it uniform. [S23]
- A causal-abstraction study finds that some models partially realize the causal structure described by their chains in arithmetic tasks, while also finding that other internal processes may contribute. [S33]
- Other studies report early answering, reasoning errors in correct-answer chains, and cases where models retain an answer after chain truncation or corruption. [S6] [S13]

### Finding 3

**Claim**

Answer placement and output format are major confounds, particularly in studies that infer reasoning from chain corruption.

**Confidence:** High

**Why this confidence level**

S6 provides detailed within-dataset and conflicting-answer controls; S3 and S5 reinforce the broader format-sensitivity point but are weaker sources.

**Evidence**

- A format-ablation study reports that models often follow an explicit terminal answer even when intermediate reasoning supports another answer. Removing only the terminal answer statement sharply reduces positional sensitivity, and the effect replicates across model families and datasets. [S6]
- Separate formatting research reports very large changes from semantically equivalent changes in separators, spacing, connectors, and layout, although that evidence is partly secondary. [S3] [S5]

### Finding 4

**Claim**

Many apparent CoT gains reflect a mixture of intermediate computation, additional serial compute, and learned schemas rather than natural-language wording alone.

**Confidence:** High

**Why this confidence level**

The three-way account is supported by converging representation, latent-reasoning, and budget evidence, although no supplied study fully isolates all three factors in one ordinary-prompting experiment.

**Evidence**

- A framework explicitly separates surface CoT, latent-state trajectories, and generic serial compute, noting that ordinary CoT changes several of these variables simultaneously. [S19] [S20]
- Latent and abstract reasoning studies show that non-verbal intermediate representations can preserve or improve performance, demonstrating that human-readable verbalization is not necessary in at least some trained systems. [S16] [S18]
- Budget studies show that large portions of generated chains can be compressed while retaining most accuracy, indicating that raw verbosity is not itself essential. [S34] [S38] [S41]

### Finding 5

**Claim**

Representation quality matters: structured, strategic, executable, or causally selected intermediate steps can outperform generic verbal CoT.

**Confidence:** Medium

**Why this confidence level**

The sources report promising direct comparisons, but the retrieved material does not establish whether improvements reflect general reasoning, better task schemas, verification, or benchmark-specific structure.

**Evidence**

- Structured CoT for code explicitly represents input/output, sequence, branching, and loops and reports improvements over generic CoT. [S1]
- Strategic CoT elicits a problem-solving strategy before generating the chain and reports gains across several reasoning datasets. [S2]
- Faithful CoT uses symbolic representations and deterministic execution to align the derived answer with the intermediate reasoning, while causal sufficiency/necessity methods seek to remove redundant steps. [S10] [S37]

### Finding 6

**Claim**

Task distribution and model regime explain much of the disagreement. Ordinary prompted CoT, trained reasoning models, and latent-reasoning systems are different interventions.

**Confidence:** High

**Why this confidence level**

Model-regime and task-dependence recur across the accumulated evidence, though generalization across all frontier models and domains remains untested.

**Evidence**

- Controlled distribution-shift work reports that CoT performs better near the training distribution but becomes fragile under changes in task structure, chain length, and surface format. [S11]
- Studies of built-in reasoning models find little incremental benefit from a generic step-by-step instruction, while trained reasoning models use extended inference-time computation and distinct training procedures. [S8] [S14] [S27]
- A latent-CoT model improves arithmetic performance over a shared-weight direct-answer mode but slightly worsens CommonsenseQA, reinforcing task dependence. [S18]

### Finding 7

**Claim**

Additional computation can help, but more tokens or verbosity are not automatically better.

**Confidence:** High

**Why this confidence level**

The sources consistently show budget sensitivity and redundancy, but do not identify the exact share attributable to semantic content versus generic serial processing.

**Evidence**

- Budget-control and concise-reasoning studies report substantial token reductions with limited average accuracy loss, while other work finds that carefully allocated thinking and solution budgets improve robustness under constraints. [S15] [S34] [S38] [S41]
- The evidence distinguishes redundant exposition from useful computation and structured solution segments; simply truncating or overconstraining a chain can fail. [S15] [S37] [S38]

## Conflicts and Uncertainty

- Classic CoT studies and practical summaries report large reasoning gains, whereas faithfulness and distribution-shift studies find unfaithful or brittle chains. These results are compatible if CoT improves benchmark performance in familiar, decomposable settings without guaranteeing faithful or generalizable reasoning. [S4] [S9] [S11] [S23]
- Causal-abstraction evidence finds that some models use intermediate CoT tokens, while early-answering and answer-suffix studies find that models often do not depend on the visible chain. The likely resolution is heterogeneity across models, tasks, examples, and interventions rather than a universal yes/no answer. [S33] [S6] [S13] [S23]
- Latent and abstract CoT results show that natural-language chains are not necessary for useful intermediate computation, but they do not prove that verbal CoT is never causally useful. [S16] [S18] [S19] [S20]
- Compression studies find that many tokens are redundant, while extended reasoning and budget-allocation studies find benefits from additional computation. The distinction may be between verbose narration and useful, appropriately allocated computation, but the sources do not quantify the boundary. [S15] [S34] [S38] [S41]
- Some sources describe CoT as broadly effective or even as a reasoning breakthrough, while others characterize it as largely an illusion. The stronger claims are not directly comparable: explanatory sources often discuss intended behavior, whereas intervention studies test causal use, faithfulness, or robustness. [S29] [S39] [S6] [S23]
- The latent-trajectory position paper favors hidden-state dynamics as the default scientific object, but its conclusion is explicitly a working hypothesis rather than a task-independent verdict, and the supplied material does not expose enough detail to independently assess all of its compute-audited examples. [S19] [S20]

## Remaining Gaps

- No supplied study directly compares ordinary verbal CoT with a direct-answer or nonverbal-scratchpad control while simultaneously matching total generated tokens, inference-time compute, demonstrations, delimiters, answer placement, and output format.
- The proportion of classic CoT gains attributable to semantic intermediate content, generic serial computation, learned task schemas, and terminal-answer/readout conventions remains unknown.
- It is unclear whether structured, executable, concise, or latent methods improve out-of-distribution reasoning and calibration, rather than primarily benchmark accuracy and efficiency.
- The generality of causal-abstraction and mediation findings across model scales, free-response tasks, domains, open versus closed models, and frontier systems remains unresolved.
- It remains uncertain whether latent reasoning findings from specialized post-trained models transfer to ordinary pretrained or instruction-tuned models using prompted verbal CoT.
- Because research stopped at the iteration limit, these questions were not resolved by the accumulated search.

## Conclusion

Chain-of-thought prompting is not best understood as either genuine reasoning in every case or mere output formatting. It is a bundle of interventions: it may allocate extra serial computation, provide a useful external scratchpad or task schema, alter answer readout, and induce a particular output format. On difficult, decomposable, in-distribution tasks—and in models capable of using intermediate representations—it can improve problem solving. Yet the visible chain is often redundant or unfaithful, can be unnecessary when the answer is already selected, and can become actively misleading under distribution shift or answer-conditioned generation. The practical and scientific conclusion is to treat verbal CoT as a conditional tool, not a universal reasoning mechanism: evaluate it against format- and compute-matched controls, test causal use rather than merely chain plausibility, and distinguish ordinary prompted CoT from process-trained or latent reasoning systems.

## Sources

- [S1] [PDF] Structured Chain-of-Thought Prompting for Code Generation - Ge Li — https://ligechina.github.io/My%20Papers/2025%20-%20TOSEM%20-%20Structured%20Chain-of-Thought%20Prompting%20for%20Code%20Generation.pdf
- [S2] Strategic Chain-of-Thought: Guiding Accurate Reasoning in LLMs through Strategy Elicitation — https://arxiv.org/html/2409.03271v1
- [S3] LLM Prompt FORMATS make or break your LLM and RAG — https://www.youtube.com/watch?v=M5i3rQfEw_A
- [S4] Master Prompting Concepts: Chain of Thought Prompting — https://promptengineering.org/master-prompting-concepts-chain-of-thought-prompting
- [S5] Medium — https://medium.com/data-science-collective/so-you-think-you-can-prompt-b3384664bafc
- [S6] The Last Word Often Wins: A Format Confound in Chain-of-Thought Corruption Studies — https://arxiv.org/html/2605.10799v1
- [S7] Faithful Chain of Thought Reasoning Guide — https://www.prompthub.us/blog/faithful-chain-of-thought-reasoning-guide
- [S8] The Decreasing Value of Chain of Thought in Prompting — https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought
- [S9] Chain-of-Thought Prompting: A Guide for LLM Apps and Agents — https://www.comet.com/site/blog/chain-of-thought-prompting
- [S10] Faithful Chain-of-Thought Reasoning - DebugML — https://debugml.github.io/fcot
- [S11] Is Chain-of-Thought Reasoning of LLMs a Mirage? A Data Distribution Lens — https://arxiv.org/html/2508.01191v2
- [S12] Testing Explainability of Chain of Thought for Large Language Models — https://www.mdpi.com/2076-3417/16/7/3112
- [S13] [PDF] Chain-of-Probe: Examining the Necessity and Accuracy of CoT Step ... — https://aclanthology.org/2025.findings-naacl.140.pdf
- [S14] Demystifying Reasoning Models - by Cameron R. Wolfe, Ph.D. — https://cameronrwolfe.substack.com/p/demystifying-reasoning-models
- [S15] SCALABLE CHAIN OF THOUGHTS VIA ELASTIC REA — https://proceedings.iclr.cc/paper_files/paper/2026/file/eb0965da1d2cb3fbbbb8dbbad5fa0bfc-Paper-Conference.pdf
- [S16] Thinking Without Words: Efficient Latent Reasoning with Abstract Chain-of-Thought — https://arxiv.org/html/2604.22709v2
- [S17] LLM Reasoning Is Latent, Not the Chain of Thought (Apr 2026) — https://www.youtube.com/watch?v=zAR0Bm6WVWA
- [S18] Can we interpret latent reasoning using current mechanistic interpretability tools? — LessWrong — https://www.lesswrong.com/posts/YGAimivLxycZcqRFR/can-we-interpret-latent-reasoning-using-current-mechanistic
- [S19] LLM Reasoning Is Latent, Not the Chain of Thought — https://arxiv.org/html/2604.15726v1
- [S20] LLM Reasoning Is Latent, Not the Chain of Thought Wenshuo Wang — https://arxiv.org/pdf/2604.15726
- [S21] Brevity is the Soul of Inference Efficiency — https://www.datologyai.com/blog/brevity-is-the-soul-of-inference-efficiency
- [S22] Inference Budget — https://www.aussieai.com/research/inference-budget
- [S23] Making Reasoning Matter — https://debjitpaul.github.io/reasoningmatter
- [S24] Answer-Conditioned Chains of Thought Degrade Verifiable-Reasoning Distillation in Large Language Models — https://arxiv.org/html/2607.14552v1
- [S25] Dynamics Within Latent Chain-of-Thought: An Empirical Study of Causal Structure — https://arxiv.org/html/2602.08783v3
- [S26] The Token Economics of Chain-of-Thought: When Thinking Out Loud Costs More Than It's Worth — https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more
- [S27] Chain of Thought Reasoning, the New LLM Breakthrough – Artificial Intelligence Management — https://blog.iese.edu/artificial-intelligence-management/2024/chain-of-thought-reasoning-the-new-llm-breakthrough
- [S28] Dynamic Micro-Batch and Token-Budget Scheduling for IoT-Scale Pipeline-Parallel LLM Inference — https://pmc.ncbi.nlm.nih.gov/articles/PMC12944026
- [S29] What is chain of thought (CoT) prompting? - IBM — https://www.ibm.com/think/topics/chain-of-thoughts
- [S30] Medium — https://cobusgreyling.medium.com/concise-chain-of-thought-ccot-prompting-6d9119fc0fdf
- [S31] Verbalizable Representations Form a Global Workspace in ... — https://transformer-circuits.pub/2026/workspace
- [S32] Token-budget ablation for 10% of the persetting optimal ... — https://www.researchgate.net/figure/Token-budget-ablation-for-10-of-the-persetting-optimal-token-count-The-x-axis-shows-the_fig2_400856240
- [S33] Causal Abstraction for Chain-of-Thought Reasoning in ... — https://aclanthology.org/2023.blackboxnlp-1.12.pdf
- [S34] Token-Budget-Aware LLM Reasoning — https://arxiv.org/html/2412.18547v4
- [S35] Token-Budget-Aware LLM Reasoning — https://www.alphaxiv.org/abs/2412.18547
- [S36] Chain-of-Thought Prompting — Improve Accuracy by Getting LLMs to Reason | Width.ai — https://www.width.ai/post/chain-of-thought-prompting
- [S37] Causal Sufficiency and Necessity Improves Chain-of- ... — https://haoxuanli-pku.github.io/papers/NeurIPS%2025%20-%20Causal%20Sufficiency%20and%20Necessity%20Improves%20Chain-of-Thought%20Reasoning.pdf
- [S38] Token-Budget-Aware LLM Reasoning — https://arxiv.org/html/2412.18547v3
- [S39] Escaping the chain-of-thought trap: What is next for LLM ... — https://bdtechtalks.substack.com/p/escaping-the-chain-of-thought-trap
- [S40] Quantum combinatorial reasoning for large language models — http://link.aps.org/doi/10.1103/kk5d-tb9b
- [S41] Self-Training Elicits Concise Reasoning in Large ... — https://aclanthology.org/2025.findings-acl.1289.pdf
- [S42] Why LLMs should stop thinking out loud (and what comes ... — https://bdtechtalks.com/2026/06/15/llm-chain-of-thought-limitations
