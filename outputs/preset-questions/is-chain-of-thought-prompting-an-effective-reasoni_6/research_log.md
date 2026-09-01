# Research Log

**System:** llm-only-baseline-v0

**Question:** Is chain-of-thought prompting an effective reasoning strategy for LLMs, or does it primarily improve output formatting? The literature disagrees—find the real fault lines and explain what accounts for the conflicting results.

## Architecture

Question → one OpenAI call → raw report

## Execution

1. Sent the user question to the configured OpenAI model with the minimal deep-research instruction.
2. No external retrieval or tools were used.
3. No Tavily calls occurred.
4. No decomposition occurred.
5. No Evidence Ledger or Research State was created.
6. No verification or counter-search occurred.
7. The model response was saved unchanged as `report.md`.

## Performance

- Model: gpt-5.6-luna
- OpenAI calls: 1
- Tavily calls: 0
- Research iterations: 0
- Input tokens: 60
- Output tokens: 5582
- Duration: 48.563 seconds
- Stop reason: single_llm_call_complete
