# Research Log

**System:** llm-only-baseline-v0

**Question:** How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

## Architecture

Question -> one structured OpenAI call -> canonical report renderer

## Execution

1. Sent the user question to the configured OpenAI model with the minimal deep-research instruction.
2. No external retrieval or tools were used.
3. No Tavily calls occurred.
4. No decomposition occurred.
5. No Evidence Ledger or Research State was created.
6. No verification or counter-search occurred.
7. The parsed `FinalReport` was rendered with the same Markdown format as V0+.
8. Unverified model-produced source IDs were removed because no retrieval occurred.

## Performance

- Model: gpt-5.6-luna
- OpenAI calls: 1
- Tavily calls: 0
- Research iterations: 0
- Input tokens: 374
- Output tokens: 3568
- Duration: 47.818 seconds
- Stop reason: single_llm_call_complete
