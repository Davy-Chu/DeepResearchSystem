# Research Log

**System:** llm-only-baseline-v0

**Question:** What caused the Late Bronze Age collapse? Compare the evidence for climate change, warfare, migration, trade disruption, political instability, and systemic collapse, and distinguish well-supported explanations from speculation.

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

- Model: gpt-4o-mini
- OpenAI calls: 1
- Tavily calls: 0
- Research iterations: 0
- Input tokens: 381
- Output tokens: 961
- Duration: 10.272 seconds
- Stop reason: single_llm_call_complete
