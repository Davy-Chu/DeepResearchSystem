# Deep Research Agent — Baseline Zero and Evidence Ledger

## What this is

This repository contains three selectable, comparable architectures for iterative web
research. Both retrieve pages with Tavily, use OpenAI structured outputs, and produce a
final report, human-readable log, reproducible machine trace, and Evaluator v0-compatible
artifacts.

The system favors an honest incomplete answer over unsupported completeness. It performs at most three searches.

`baseline-zero` preserves the original combined analysis/decision loop.
`evidence-ledger-v1` persists claims, evidence relationships, confidence, conflicts, and
research gaps across iterations before making a separate research decision.
`evidence-ledger-decomposer-v1` first creates a stable two-to-six-subquestion research
plan, then uses the ledger to target unresolved subquestions explicitly.

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

Decomposed mode adds one OpenAI structured-output decomposition before any search. Python
assigns stable `SQ1...SQ6` IDs. The first search remains the user's exact original
question; later searches target one unresolved subquestion at a time. Subquestion status
(`UNRESEARCHED`, `PARTIAL`, `SUFFICIENT`, or `CONFLICTING`) is recomputed deterministically
from linked claims and gaps after each evidence update. The plan is not expanded or
rewritten during a run.

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
OPENAI_EVALUATOR_MODEL=gpt-5.6-terra
OPENAI_TIMEOUT_SECONDS=120
OPENAI_MAX_RETRIES=1
```

`EVALUATOR_MODEL` configures evaluator-v0 and falls back to `OPENAI_MODEL`.
`OPENAI_EVALUATOR_MODEL` configures evaluator-v1 and falls back through
`EVALUATOR_MODEL` to `OPENAI_MODEL`. All model choices can be changed without editing
code. `.env` is ignored by Git, and keys are never logged.
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

Run the subquestion-aware Evidence Ledger Decomposer v1:

```bash
python main.py "your research question" --mode decomposed
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
API usage or charges. Decomposed mode has the same search and ledger limits plus one
question-decomposition request, for a maximum of three Tavily requests and seven OpenAI
requests (one decomposition, three evidence updates, two decisions, and one report).

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

### Evaluator v1: Frozen Reference Benchmark

Evaluator v0 asks whether a report appears to address the prompt. That is useful as a
basic check, but it can give a short, plausible report unrealistically high coverage
because it has no independent estimate of the important research space.

Evaluator v1 derives 5–10 atomic, weighted research requirements from a high-quality
reference report and freezes them with SHA-256 hashes. Candidate reports are judged
against the frozen rubric—not against reference wording, organization, sources, or
conclusions. Freezing prevents the benchmark definition from changing between
baseline and ablation evaluations. Reference reports establish benchmark scope; they
are not absolute truth.

The initial five-fixture benchmark is frozen under `evaluation/fixtures/`: remote
work, the Late Bronze Age collapse, quantum commercial advantage, carbon capture, and
social-media polarization. Each directory contains the exact supplied question and
reference report plus the generated atomic rubric and hash metadata.

Build and freeze an authored fixture:

```powershell
python main.py evaluator build-fixture evaluation/fixtures/remote-work-productivity
```

This performs one rubric-builder and one rubric-critic OpenAI call. Invalid structured
output receives one repair attempt. Once `fixture.json` exists, the builder refuses to
regenerate the frozen fixture automatically.

Evaluate an existing saved run. Exact normalized question matching selects the fixture:

```powershell
python main.py evaluator evaluate outputs/<run-directory>
```

Or select it explicitly:

```powershell
python main.py evaluator evaluate outputs/<run-directory> --fixture remote-work-productivity
```

Evaluator v1 never calls Tavily, performs web research, or changes the original report
or trace. It does use OpenAI structured-output calls for frozen-rubric
comprehensiveness, saved-snapshot citation support, and citation completeness. Missing
fixtures, historical ledgers, or saved source content become visible `NOT_EVALUABLE`
components rather than silently receiving zero or full credit.

Evaluate several saved experiments and write JSON, CSV, and Markdown tables:

```powershell
python main.py evaluator benchmark outputs/<baseline-run> outputs/<ledger-run>
```

Compare two already-saved evaluator-v1 results without making API calls:

```powershell
python main.py evaluator compare outputs/<baseline-run> outputs/<ledger-run>
```

Evaluator-v1 results are stored without overwriting earlier results:

```text
outputs/<run>/evaluations/evaluator-v1/<fixture-id>/
├── evaluation.json
└── evaluation.md
```

Benchmark and comparison summaries are written below `evaluation/results/`. Every
evaluation records fixture and rubric hashes, prompt versions, candidate-report hash,
model, scoring weights, timestamp, evaluation completeness, and available token usage.

## Testing

Tests use fakes and make no real API calls:

```bash
pytest
```

In a restricted Windows environment where pytest cannot access the user temp folder:

```powershell
pytest --basetemp .pytest-temp
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
- `research_log.md`: a chronological explanation of searches, state updates, decisions, and timings. Ledger-mode logs explicitly show new and updated claims, confidence/status transitions, gap changes, and a state summary after every iteration. Decomposed-mode logs also show the initial plan, per-iteration subquestion progress, transitions, and targeted search counts.
- `trace.json`: the machine-readable trace. It records `system_version`, decisions, stop reason, model, structured final report, and exact source snapshots. Ledger mode additionally preserves the full evidence ledger, evidence relationships, gap creation/resolution, and decision targets; decomposed mode also preserves the full research plan and status transitions.

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

All current architectures:

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
