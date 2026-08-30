# Deep Research Agent — Baseline Zero and Evidence Ledger

## What this is

This repository contains two selectable, comparable architectures for iterative web
research. Both retrieve pages with Tavily, use OpenAI structured outputs, and produce a
final report, human-readable log, reproducible machine trace, and Evaluator v0-compatible
artifacts.

The system favors an honest incomplete answer over unsupported completeness. It performs at most three searches.

`baseline-zero` preserves the original combined analysis/decision loop.
`evidence-ledger-v1` persists claims, evidence relationships, confidence, conflicts, and
research gaps across iterations before making a separate research decision.

## Architecture

```text
Question
   ↓
Tavily Search
   ↓
OpenAI Evidence Analysis
   ↓
Need more research?
   ├── yes → targeted Tavily search ──┐
   │                                 │
   └── no  → structured final report │
                                     │
                   (at most 3 searches)
```

The Baseline Zero loop remains ordinary Python in `research/runner.py`.

Evidence Ledger v1 uses this explicit flow:

```text
Question
  → Tavily Search
  → Evidence Processor
  → Evidence Ledger and Research Gaps
  → Research Decision
      ├→ targeted search and repeat
      └→ ledger-backed final report
```

Its orchestration lives in `research/ledger_runner.py`. The Evidence Processor updates
knowledge but never chooses the next search. The separate decision component reads the
structured ledger, open gaps, search history, and remaining budget without raw source
content. Python assigns stable `C1...` claim IDs and `G1...` gap IDs, validates every
state update, deduplicates evidence relationships, and renders artifacts.

## Requirements

- Python 3.11 or newer
- An OpenAI API key with access to the configured model
- A Tavily API key

## Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on macOS/Linux:

```bash
source .venv/bin/activate
```

Install the pinned dependencies:

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and populate both keys:

```text
OPENAI_API_KEY=your-key
TAVILY_API_KEY=your-key
OPENAI_MODEL=gpt-5.6-terra
EVALUATOR_MODEL=gpt-5.6-terra
OPENAI_TIMEOUT_SECONDS=120
OPENAI_MAX_RETRIES=1
```

`EVALUATOR_MODEL` is optional and falls back to `OPENAI_MODEL`. Both model choices can
be changed without editing code. `.env` is ignored by Git, and keys are never logged.
`OPENAI_TIMEOUT_SECONDS` applies to every OpenAI request attempt and defaults to 120
seconds. The OpenAI SDK may retry a timed-out request, so total elapsed time can exceed
this value.
`OPENAI_MAX_RETRIES` defaults to 1, allowing one retry after a transient OpenAI
connection, timeout, rate-limit, or server error.

## Running

Baseline Zero remains the default, preserving existing commands:

```bash
python main.py "your research question"
```

Run Evidence Ledger v1 explicitly:

```bash
python main.py "your research question" --mode ledger
```

For example:

```bash
python main.py "What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation."
```

Progress, the stop reason, and artifact paths are printed to the terminal. Missing keys, retrieval failures, OpenAI failures, and malformed structured output cause a clear error and a non-zero exit.

Run the command from the project root, where `main.py` and `.env` are located. A
Baseline Zero may perform up to three Tavily searches and four OpenAI requests. Evidence
Ledger v1 may perform up to three Tavily searches, three evidence-processing requests,
two model-based research decisions, and one final-report request. Either mode can incur
API usage or charges.

## Evaluating a Saved Run

Evaluator v0 measures coverage, citation support, and deterministic validity for an
already-saved research run:

```bash
python main.py evaluate outputs/<run-directory>
```

For example:

```bash
python main.py evaluate outputs/what-are-the-benefits-of-solar-energy
```

Evaluation does not call Tavily, search the web, rerun research, or change the saved
report. It does make OpenAI structured-output calls using `EVALUATOR_MODEL` (or
`OPENAI_MODEL` as a fallback), so evaluating a run may incur OpenAI API usage or
charges. Coverage and citation stages use low reasoning effort. All numerical rates
are calculated deterministically in Python from the returned categorical judgments.

## Testing

Tests use fakes and make no real API calls:

```bash
pytest
```

## Output

Each run creates a directory named from the sanitized research question below
`outputs/`. If that question has already been run, the new directory receives a numeric
suffix such as `_2` or `_3` instead of overwriting the earlier run:

```text
outputs/
├── what-are-the-benefits-of-solar-energy/
└── what-are-the-benefits-of-solar-energy_2/
```

Each run directory contains:

- `report.md`: the final research findings, rendered deterministically from the structured report with claims and evidence visually separated.
- `research_log.md`: a chronological explanation of searches, state updates, decisions, and timings. Ledger-mode logs explicitly show new and updated claims, confidence/status transitions, gap changes, and a state summary after every iteration.
- `trace.json`: the machine-readable trace. It records `system_version`, decisions, stop reason, model, structured final report, and exact source snapshots. Ledger mode additionally preserves the full evidence ledger, evidence relationships, gap creation/resolution, and decision targets.

The Evidence Ledger research log is organized for quick review:

```text
Run Summary
Iteration 1
  Search and query reason
  Evidence processing
  Ledger updates
  Current research state
  Research decision
Iteration 2 (when needed)
  ...
Final Research Decision
Performance Summary
```

`research_log.md` does not store raw retrieved webpage content. `trace.json` does store
the exact source snapshot used by the research agent so citation evaluation remains
reproducible if a live webpage changes. Treat traces as potentially sensitive artifacts.

Each evaluation is saved without overwriting earlier evaluations:

```text
outputs/<run>/evaluations/
├── evaluator-v0/
│   ├── evaluation.json
│   └── evaluation.md
└── evaluator-v0_2/        # created when evaluator-v0 already exists
```

Runs created before evaluator-v0 do not contain the structured report and saved source
content required for reproducible evaluation. The evaluator rejects those legacy runs
with a clear error instead of downloading replacement evidence.

If research or final synthesis fails after a run has accumulated state, the application
still attempts to save all three artifacts. In that case, `report.md` is clearly labeled
as an automatically generated incomplete report and preserves the citation-backed
findings collected so far. The research log records the failure stage and remaining
gaps, while the process exits with a non-zero status. If no validated finding exists,
the report says that the available evidence is insufficient instead of inventing an
answer.

Source IDs (`S1`, `S2`, and so on) remain stable for a run. Final report generation fails if the model cites an ID that does not map to a retrieved URL.

Research stops with one of four recorded reasons: `sufficient_evidence`, `max_iterations`, `duplicate_query`, or `no_search_results`.

## Current limitations

Both current architectures:

- relies on a general web search provider;
- does not independently score source credibility;
- does not guarantee retrieved pages are authoritative;
- uses LLM judgment for evidence interpretation;
- uses coarse Low/Medium/High confidence;
- has a fixed search budget;
- does not yet perform parallel subquestion research;
- evaluates citation support with an LLM against saved source text, but does not perform
  independent internet fact-checking;
- rely on model judgment to interpret evidence and identify semantic claim updates;
- do not use embeddings or an independent verifier;
- may still miss contradictions or create semantically overlapping claims;
- may be vulnerable to imperfect retrieval;
- uses prompt-level protection against instructions embedded in webpages rather than a complete prompt-injection defense.

Retrieved web content is treated as untrusted data in every model prompt that receives it, but prompt instructions alone are not a complete security boundary.
