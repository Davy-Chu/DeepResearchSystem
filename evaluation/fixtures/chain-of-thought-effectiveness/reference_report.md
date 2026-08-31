# Chain-of-Thought Prompting: Reasoning vs. Output Formatting

**Executive Summary:** Chain-of-thought (CoT) prompting can substantially boost LLM accuracy on multi-step reasoning benchmarks, but its gains are highly conditional.  Early work (e.g. Wei *et al.* 2022) showed *huge* improvements on arithmetic and symbolic tasks with few-shot CoT (e.g. PaLM-540B accuracy on GSM8K jumped from ~10% to 58%).  Similarly, Kojima *et al.* (2023) found that simply adding “*Let’s think step by step*” in zero-shot prompts raised accuracy dramatically on puzzles (e.g. GSM8K 10.4→40.7%, MultiArith 17.7→78.7%).  Follow-on work (Wang *et al.* 2022) introduced *self-consistency* (sampling multiple chains and voting), yielding further gains (e.g. GSM8K +17.9%, SVAMP +11.0% accuracy).  However, these benefits mainly arise in *very large models* (>100B) on tasks similar to their training data.  For smaller models or out-of-distribution tasks, CoT often produces little or no lift (even harming accuracy on simple questions in some cases).  Critically, recent analyses (e.g. Zhao *et al.* 2026) suggest CoT may exploit *training data patterns* rather than true logical inference; CoT “reasoning” becomes a mirage when tasks deviate from the model’s learned distribution.  In practice, CoT prompts consume many extra tokens and increase latency, so they should be used judiciously (especially since many LLMs perform CoT-like reasoning even under a default prompt).  

## Key Experiments and Findings

- **Wei *et al.* (2022)** performed few-shot CoT on arithmetic/commonsense tasks using very large models.  They found that with *8 CoT exemplars*, a 540B-parameter model solved GSM8K (math word problems) at **58% accuracy**, far above the ~10% baseline and past the previous 55% SOTA.  Even smaller models showed **flat scaling** without CoT (poor accuracy), but *with* CoT their performance *improved steeply* with scale.  On commonsense QA (CommonsenseQA, StrategyQA), CoT gave modest gains as model scale increased.  Wei *et al.* also noted they used an *external calculator* to do basic arithmetic in these experiments (so the model’s chain-of-thought primarily orchestrated operations rather than computing by itself).  

- **Kojima *et al.* (2023)** introduced *zero-shot CoT*: appending a fixed phrase (“*Let’s think step by step*”) to each query.  With this single prompt and *no examples*, models like GPT-3.5/InstructGPT and PaLM-540B showed similarly large gains.  For instance, on arithmetic and symbolic benchmarks (MultiArith, SVAMP, GSM8K, etc.), accuracy jumped by dozens of points (e.g. MultiArith from 17.7%→78.7%, GSM8K 10.4%→40.7%).  This indicates that even a short CoT cue can unlock latent reasoning in very large models, without handcrafted exemplars.  

- **Wang *et al.* (2022, ICLR)** proposed *Self-Consistency*: instead of one deterministic CoT decode, sample many reasoning paths and take a majority vote on the answer.  Across arithmetic and commonsense tasks (GSM8K, SVAMP, AQuA, StrategyQA, ARC), self-consistency **consistently improved** on basic CoT decoding.  For example, self-consistency on GSM8K raised accuracy by +17.9% absolute over greedy CoT.  This suggests that many valid reasoning chains exist and aggregating them boosts robustness.  

- **Other analyses:**  Independent evaluations reinforce these patterns.  A technical report from Wharton (2024) tested CoT on a 1000+ question QA benchmark across various LLMs.  They found CoT *helped “non-reasoning” models* (like GPT-4o-mini, older Gemini) by ~5–13% on average, but often *hurt* the top-tier “reasoning” models (e.g. Gemini Pro accuracy dropped 17.2% with CoT).  Crucially, many high-end models already produced CoT-like answers under default prompts, so forcing CoT often just added noise.  

The table below compares key results from these studies:

| Study                      | Model(s) & Size                   | Tasks                         | Prompt / Method              | Baseline       | Key Results & Effects  |
|----------------------------|-----------------------------------|-------------------------------|------------------------------|----------------|-------------------------------|
| Wei *et al.* 2022   | PaLM (8B, 62B, 540B)               | GSM8K, MultiArith, others     | 8-shot CoT (few-shot)       | Standard few-shot Q&A | PaLM-540B: GSM8K 10%→58% (new SOTA); similar strides on arithmetic/symbolic tasks  |
| Kojima *et al.* 2023| InstructGPT (175B), PaLM (540B)   | MultiArith, GSM8K, SVAMP, AQuA, StrategyQA | Zero-shot CoT (“think step by step”)  | Standard zero-shot        | MultiArith 17.7%→78.7%; GSM8K 10.4%→40.7%; other logic tasks similarly large gains (only in >100B models). |
| Wang *et al.* 2022   | PaLM (540B), UL2 (? size)         | GSM8K, SVAMP, AQuA, StrategyQA, ARC Challenge | Greedy CoT vs. CoT+Self-Consistency (100 samples) | Greedy CoT decoding   | Self-consistency boosts accuracy: GSM8K +17.9%, SVAMP +11.0%, AQuA +12.2%, StrQA +6.4%, ARC +3.9%.      |
| Zhao *et al.* 2026  | Synthetic LLMs (trained from scratch; 62K–14B) | Controlled “DataAlchemy” logic tasks (varied dist.) | CoT vs. Direct (in/out-of-dist)  | Direct prompt (or in-dist CoT) | *In-distribution:* CoT yields structured reasoning. *Shifted tasks:* CoT yields fluent but **inconsistent** outputs; accuracy drops sharply. CoT success is fragile under moderate distribution shift. |
| Wharton 2024    | Various (Gemini 2.0/3.5, GPT-4o, “Sonnet” 3.5) | GPQA (general QA set)         | 1-shot CoT vs. direct answer | Direct answer            | *Non-reasoning models:* +11–13% accuracy (Gemini Flash +13.5%, Sonnet +11.7%). *Reasoning models:* CoT gave near-zero or negative effects (Gemini Pro –17.2%). CoT increased latency 20–80%. |

## Methodological Differences and Confounds

Multiple design choices vary across studies, explaining some conflicting outcomes:

- **Model scale:** Virtually all gains appear *only in the largest models*.  Wei and colleagues saw emergent CoT performance at ~100B+ parameters.  Kojima likewise reported negligible improvement on smaller models.  In Zhao *et al.*’s experiments, tiny models (millions of params) showed *no real CoT benefit* even in-distribution, whereas larger ones did.  

- **Task selection:** Most CoT gains are reported on arithmetic, symbolic or logical reasoning benchmarks (GSM8K, MultiArith, SVAMP, etc.), which often resemble content seen during pretraining.  Commonsense or open-ended tasks (CommonsenseQA, StrategyQA) show only *mild or inconsistent* improvements.  If a task requires knowledge or skills poorly covered in training, CoT yields little gain (Zhao *et al.* find CoT “fails” on sufficiently novel tasks).  

- **Prompt engineering:** Studies use different CoT styles.  Wei used *exemplar-based few-shot CoTs*, Kojima used a fixed zero-shot prompt, while others tried variations of the “*explanation style*” (e.g. keywords like “explain step by step”).  This affects performance; e.g., some models may respond better to explicit exemplars than to a plain instruction.  Also, exact wording matters (“*step by step*” was a key phrase in zero-shot CoT).  

- **Decoding & randomness:** Most original CoT used *greedy decoding*, but self-consistency shows random sampling & majority vote can **substantially amplify** CoT’s success.  Higher temperature and more samples can increase consistency of correct answers.  Conversely, deterministic or low-temperature decoding can hide alternate chains.  We also note *answer extraction*: some CoT methods split reasoning and answer stages (Kojima’s two-stage pipeline), which can improve answer formatting.  

- **Evaluation metrics:** Studies often report *accuracy* on benchmarks, but definitions vary.  Some measure strict final-answer match, others allow partial credit.  Wharton’s report additionally used “90% correct” or “perfect accuracy” to show CoT sometimes *reduced* top-end correctness.  Few works report statistical significance, making small gains (<5%) uncertain.  In general, the reported effect sizes (often tens of points) are large enough to be unambiguous in major studies.  

- **Use of tools:** Some CoT pipelines embed external tools.  Wei *et al.* explicitly used a calculator for arithmetic tasks; thus the chain-of-thought only had to parse and output calculations, not perform them.  In real applications, permitting LLMs to call tools (e.g. Python interpreter) can mimic this effect.  Without tools, even large LMs may make numeric errors, so part of the “CoT gain” may come from structured context that simplifies calculation.  

- **Training data distribution:** Zhao *et al.* emphasize that CoT’s effectiveness depends on how similar test problems are to the model’s training data.  If problems are “within distribution”, models can *interpolate* known solution patterns with CoT.  When problems deviate (novel logic, different length), CoT often breaks down.  This suggests a major confound: CoT might be retrieving or recombining memorized fragments rather than performing genuine novel reasoning.  

## Fault Lines: Reasoning vs. Formatting Effects

The literature reveals clear fault lines:

- **Genuine reasoning gains:**  Large LMs *do* appear to solve multi-step problems with CoT prompts where they otherwise fail.  This is most evident in tasks with clear step-by-step solutions (e.g. math word problems).  The pattern (scale-dependent emergence, self-consistency gains) implies some *reasoning-like* capability is at play.  When CoT helps, the model often spells out a plausible chain that a human would recognize.

- **Formatting/context artifacts:**  Several observations suggest CoT benefits can be superficial.  First, the massive token overhead means CoT mainly adds context, which an LLM can exploit.  Essentially, the model has more “room” to think or retrieve related facts.  Indeed, Wharton et al. note that many models already produce reasoning-like outputs by default – so explicitly prompting chain-of-thought is sometimes just *reformatting* what the model would do anyway.  Second, Zhao *et al.* find that CoT chains can be *fluent but logically inconsistent* when tasks go OOD (e.g. the model might assert contradictory premises while still guessing a correct answer).  Third, faithfulness studies show models often “fake” reasoning: they can arrive at the correct answer even if their chain is disrupted or nonsensical (e.g. Shumskii 2023, Bansal 2025, etc., though not detailed here).  These patterns imply that the **final answer may not truly depend on the articulated steps** – the chain is partially post-hoc rationalization.  

- **Error introduction:** CoT can sometimes *hurt* performance on questions the model would otherwise solve easily.  As Wharton observed, non-reasoning models gained on hard questions but lost accuracy on easy ones (e.g. confidence thresholds dropped).  This suggests CoT can introduce confusion or longer reasoning paths that muddle simple answers.  

In summary, CoT tends to yield true performance improvements **only when** (a) model capacity is very high and (b) the task strongly parallels training experiences.  Outside those conditions, apparent gains often reflect better formatting and more exploitable context rather than deep reasoning.  

## Causal Hypotheses

Combining these findings leads to several explanatory hypotheses:

- **Emergent pattern matching:** Large LLMs may have implicitly memorized chains of reasoning from training data.  CoT prompts cue retrieval or interpolation of these chains.  For in-distribution tasks, this works well; for out-of-distribution ones, the cues fail, producing incoherence.  

- **Contextual search:** Asking for a reasoning chain effectively *widened the model’s context window* (by generating intermediate tokens) and guided its attention through sub-steps.  This can help the model focus, analogous to chaining clauses in retrieval.  The success of self-consistency supports the idea that exploring multiple chains finds the right latent reasoning path.  

- **Calibration and token usage:** CoT changes the probability landscape.  In many LMs, answers are more likely when preceded by a confident chain of reasoning.  Without CoT, the model may under-express uncertainty or skip steps.  CoT could simply *remix* existing knowledge in a more structured way, improving answer confidence.  

- **Shortcut vs. actual computation:** In math tasks, CoT often offloads computation (especially with an external tool).  Without tools, CoT sometimes still succeeds by breaking the problem into sub-queries the model can handle.  But when asked about unfamiliar logic, the model may use statistical heuristics rather than symbolic reasoning.  

These hypotheses are not mutually exclusive and can be tested further.

## Recommendations for Future Experiments

To resolve open questions, we suggest: 

- **Out-of-distribution testing:** Create or identify benchmarks that differ from pretraining data (e.g. novel logic puzzles, synthetic tasks).  Compare CoT vs. direct prompting; check whether CoT still helps or degrades.  Zhao *et al.*’s *DataAlchemy* framework is one approach.  

- **Control chains:** Test CoT against *random or irrelevant chains*. For example, give correct answers but with scrambled reasoning steps; or use templated nonsense as chain prompts.  If performance remains high, it indicates the final answer is not depending on true reasoning content.  

- **Chain length and density:** Vary how many reasoning steps are required.  If the model saturates (no extra benefit beyond a certain chain length), it suggests limits to useful computation.  Similarly, measure at what point additional detail (or verbosity) stops improving accuracy.  

- **Generalization and systematicity:** Compare CoT performance on systematically altered problems (e.g. numeric perturbations, negations, adversarial distractors).  This probes whether CoT fosters robust reasoning or just pattern exploitation.  

- **Statistical rigor:** Run ablations with multiple seeds and statistical tests, especially for smaller gains.  Report effect sizes with confidence intervals as Wharton did.  

- **Interactive tools:** Experiment with tool-augmented CoT vs. raw CoT to quantify how much computation is offloaded.  Also test if CoT benefits persist when forbidding additional facts (e.g. using a minimal vocabulary).  

## Practical Guidance

Based on current evidence, we advise:

- **Use CoT for hard reasoning tasks in large models:** If you have a very capable LLM struggling with multi-step problems, try CoT prompts.  Even a simple phrase like “*step by step*” can unlock latent performance. 

- **Check baseline performance:** Since many LLMs already “think” under the hood, always compare against a no-CoT baseline.  If the model already yields a long justification on default prompts, forcing CoT may not help (and may hurt). 

- **Be mindful of trade-offs:** CoT *greatly increases tokens and latency*.  Our cited analyses note up to ~80% slower response times.  Evaluate whether accuracy gain justifies the cost. In some applications, a slightly lower accuracy with  shorter answers may be preferable.

- **Use self-consistency or ensembling:** If using CoT, consider sampling multiple chains and aggregating answers (self-consistency).  This often boosts reliability at the expense of more queries.  

- **Plan for calibration:** Because CoT changes how probabilities flow, output answers may become overconfident.  Validate on held-out data and possibly calibrate confidence thresholds.  

- **Monitor for spurious chains:** Inspect some chains qualitatively.  If reasoning steps look off-topic or contradictory, be cautious – the model may still be right by luck or bias.  

## Timeline of Key Developments (Flowchart of Factors)

```mermaid
flowchart TD
    A[Large Model Scale] -->|Enables| B[Strong CoT Gains]
    C[Small Model] -->|Limited| D[No CoT Benefit]
    E[In-Distribution Task] -->|Supports| B
    F[Out-of-Distribution Task] -->|Hinders| D
    G[Self-Consistency (Sampling)] -->|Amplifies| B
    H[Greedy Decoding] -->|Baseline| B
    I[Few-shot or Zero-shot CoT] -->|Method Choice| B
    J[Use of External Tools] -->|Augments| B
```

*Figure: Factors influencing CoT effectiveness. Large model size and task alignment tend to produce true reasoning gains (green), whereas small models or distribution shifts yield only minimal or spurious improvements (red arrows).  Self-consistency and additional tools further enhance accuracy.*

## Conclusion (Claims and Confidence)

1. **CoT improves performance on complex reasoning tasks *in large models*.**  **Confidence: High.**  Multiple studies (Wei 2022, Kojima 2023, Google blog) consistently report *dramatic* accuracy jumps in tasks like math word problems when using CoT with LMs ≥100B parameters.  This is supported by both peer-reviewed papers and internal Google research.

2. **CoT gains are highly *scale-dependent* and task-dependent.**  **Confidence: High.**  Empirical results show negligible CoT benefit in small models and on open-ended tasks.  The improvements emerge near the high end of scale and on benchmarks similar to pretraining data.  This consistency across studies gives high confidence.

3. **Many CoT “reasoning” gains reflect formatting/context effects rather than robust logic.**  **Confidence: Medium.**  Evidence (e.g. Zhao 2026) indicates CoT works well only in-distribution, and Wharton’s analysis shows trivial errors induced by CoT in easy cases.  Faithfulness studies (external) also suggest chains can be post-hoc.  However, these are mostly recent analyses; while suggestive, more work is needed to fully prove how much CoT is “mirage vs real”.  

4. **Self-consistency reliably boosts CoT performance.**  **Confidence: High.**  The original CoT papers and follow-ups (e.g. Wang 2022) uniformly find that sampling multiple chains improves accuracy significantly, a result echoed in practice.  This is a robust finding with clear effect sizes.

5. **CoT has diminishing or negative returns on already-competent models.**  **Confidence: Medium.**  The Wharton report and anecdotal evidence from GPT-4/Gemini suggest that as LMs become intrinsically good at reasoning, explicit CoT offers little benefit and can even confuse them.  This claim fits practical experience but is supported by a smaller set of evaluations, so we assign medium confidence.

6. **CoT’s reliability drops sharply under distribution shift.**  **Confidence: Medium.**  The Zhao *et al.* study (2026) clearly shows CoT fails on moderately out-of-distribution tasks.  While this controlled experiment is convincing, it is a single rigorous study; confirmatory experiments on other tasks would strengthen this claim.

*Criteria for confidence:* We base “High” on consistent, large-effect results from multiple independent sources (e.g. Wei, Kojima, Wang). “Medium” indicates some evidence or partial consensus but also open questions or contradictions (e.g. CoT faithfulness). Claims without direct experimental backing (e.g. theoretical explanations) are given lower confidence. All claims above are supported by citations as noted. 

**Sources:** Peer-reviewed and preprint papers (Wei *et al.* 2022; Kojima *et al.* 2023; Wang *et al.* 2022; Zhao *et al.* 2026), industry technical reports (Wharton 2024), and major blog posts. These cover original experiments, ablations, and analyses of CoT prompting from 2020–2026.