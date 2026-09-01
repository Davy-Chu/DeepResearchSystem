# Deep Research Agent — Canonical Research Ablation Ladder

## What this is

This repository contains five selectable, comparable research architectures spanning
the simplest possible model interaction through retrieval, structured evidence state,
explicit planning, and independent verification. Every architecture produces a report,
human-readable log, machine trace, and Evaluator-v1-compatible artifacts.

The LLM-only architecture is deliberately below the assignment's MVP minimum bar. It is
a lower-bound experimental baseline, not a viable research system or the MVP
implementation. It measures what the configured model produces from pretrained
knowledge and one minimal instruction. The other four architectures use Tavily and may
perform at most ten searches; they favor an honest incomplete answer over unsupported
completeness.

| Version | System | Stable system ID | Search | Ledger | Plan | Verifier |
|---|---|---|---:|---:|---:|---:|
| V-1 | LLM Only | `llm-only-baseline-v0` | No | No | No | No |
| V0 | Search Baseline | `baseline-zero` | Yes | No | No | No |
| V1 | Evidence Ledger | `evidence-ledger-v1` | Yes | Yes | No | No |
| V2 | Decomposer | `evidence-ledger-decomposer-v1` | Yes | Yes | Yes | No |
| V3 | Verifier | `evidence-ledger-decomposer-verifier-v1` | Yes | Yes | Yes | Yes |

This canonical ladder separates:

```text
Raw model capability
  -> + fresh external retrieval
  -> + structured evidence state
  -> + explicit decomposition and planning
  -> + independent adversarial verification
```

Without V-1, comparisons beginning at the search baseline cannot distinguish the value
of fresh information from the value of later research mechanisms. V-1 to V0 is
intentionally a lower-bound comparison rather than a perfectly compute-matched
ablation: it adds both Tavily access and a research loop. The later transitions are
cleaner architectural ablations because they retain the same retrieval environment.

## Architecture and Experimental Questions

### V-1 — LLM Only

System version: `llm-only-baseline-v0`

```text
Question -> one structured OpenAI call -> canonical report renderer
```

The model receives only: `Do deep research and create a report on the following
question:` followed by the question. There is no custom system prompt, tool access,
retrieval, research loop, evidence state, decomposition, verification, self-correction,
or report rewriting. The response uses the same `FinalReport` schema and Markdown
renderer as V0+, while unverified source IDs are removed because no retrieval occurs. Missing fresh evidence and
unverified model-generated citations are intentional limitations.

### V0 — Search Baseline

System version: `baseline-zero`

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

The Search Baseline loop remains ordinary Python in `research/runner.py`. The V-1 to V0
transition asks: **What value does fresh external retrieval add beyond the model's
pretrained knowledge?** It adds Tavily retrieval and the iterative research loop.

### V1 — Evidence Ledger

System version: `evidence-ledger-v1`

Evidence Ledger uses this explicit flow:

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

The V0 to V1 transition asks: **What value does explicit structured research state add
beyond search-and-write behavior?** It adds the Evidence Ledger and explicit
claim/evidence/gap tracking.

### V2 — Decomposer

System version: `evidence-ledger-decomposer-v1`

Decomposed mode adds one OpenAI structured-output decomposition before any search. Python
assigns stable `SQ1...SQ6` IDs. The first search remains the user's exact original
question; later searches target one unresolved subquestion at a time. Subquestion status
(`UNRESEARCHED`, `PARTIAL`, `SUFFICIENT`, or `CONFLICTING`) is recomputed deterministically
from linked claims and gaps after each evidence update. The plan is not expanded or
rewritten during a run.

The V1 to V2 transition asks: **What value does explicit question decomposition and
subquestion-aware search allocation add?** It adds a stable Research Plan, explicit
subquestions, and targeted search prioritization.

### V3 — Verifier

System version: `evidence-ledger-decomposer-verifier-v1`

Verified mode builds on decomposed mode:

```text
Question
  -> Decompose
  -> Search
  -> Evidence Ledger
  -> Independent Verification
       |-> Counter-search -> Evidence Processor -> Ledger Update -> Reverify
       `-> Continue
  -> Subquestion Decision
  -> Report
```

The verifier runs in a fresh OpenAI request context. It receives only the original
question, the selected claim ID and text, related subquestion questions and success
criteria, neutral saved source snapshots, its verification phase, and whether a
counter-search is allowed. It does not receive the claim's status, confidence,
confidence reason, processor evidence labels, other claims, controller reasoning, or a
draft/final report. Verification can revise claim wording, confidence, and status, but
only the Evidence Processor can change supporting or contradicting evidence relations.

The V2 to V3 transition asks: **What value does independently challenging
apparently-supported claims add?** It adds an independent verifier,
falsification-oriented counter-search, and deterministic claim reconciliation.

## Requirements

- Python 3.11 or newer
- An OpenAI API key with access to the configured model
- A Tavily API key for V0–V3 (V-1 does not use or require Tavily)

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
LLM_ONLY_MODEL=
VERIFIER_MODEL=
EVALUATOR_MODEL=gpt-5.6-terra
OPENAI_EVALUATOR_MODEL=gpt-5.6-terra
OPENAI_TIMEOUT_SECONDS=120
OPENAI_MAX_RETRIES=1
```

`EVALUATOR_MODEL` configures evaluator-v0 and falls back to `OPENAI_MODEL`.
`OPENAI_EVALUATOR_MODEL` configures evaluator-v1 and falls back through
`EVALUATOR_MODEL` to `OPENAI_MODEL`. All model choices can be changed without editing
code. `.env` is ignored by Git, and keys are never logged.
`VERIFIER_MODEL` configures the independent claim verifier and falls back to
`OPENAI_MODEL` when blank or missing. It uses the existing OpenAI API key.
`LLM_ONLY_MODEL` optionally overrides the model for V-1 and falls back to `OPENAI_MODEL`.
For controlled comparisons, leave it blank so every research architecture uses the
same underlying research model.
`OPENAI_TIMEOUT_SECONDS` applies to every OpenAI request attempt and defaults to 120
seconds. The OpenAI SDK may retry a timed-out request, so total elapsed time can exceed
this value.
`OPENAI_MAX_RETRIES` defaults to 1, allowing one retry after a transient OpenAI
connection, timeout, rate-limit, or server error.

## Running

Run the deliberately primitive V-1 lower-bound baseline:

```bash
python main.py "your research question" --mode llm-only
```

This makes exactly one logical OpenAI research-generation request, exposes no tools,
does not require a Tavily key, and saves the raw model response unchanged.

V0 Search Baseline remains the default, preserving existing commands:

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

Run the decomposed architecture with independent verification and adversarial
counter-search:

```bash
python main.py "your research question" --mode verified
```

For example:

```bash
python main.py "What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation."
```

Progress, the stop reason, and artifact paths are printed to the terminal. Missing keys, retrieval failures, OpenAI failures, and malformed structured output cause a clear error and a non-zero exit.

Run the command from the project root, where `main.py` and `.env` are located. A
V-1 makes one logical OpenAI research request and zero Tavily requests. Infrastructure
retries may cause another HTTP attempt, but it never performs a semantic retry or second
generation pass. Search Baseline may perform up to ten Tavily searches and eleven OpenAI requests. Evidence
Ledger v1 may perform up to ten Tavily searches, ten evidence-processing requests,
nine model-based research decisions, and one final-report request. Either mode can incur
API usage or charges. Decomposed mode has the same search and ledger limits plus one
question-decomposition request, for a maximum of ten Tavily requests and twenty-one OpenAI
requests (one decomposition, ten evidence updates, nine decisions, and one report).
Verified mode retains the same hard maximum of ten Tavily searches. A verifier-requested
counter-search consumes the next slot in that budget and goes through the same Tavily
client and Evidence Processor; it is not a hidden eleventh search. A claim can receive at
most one adversarial counter-search, after which the same claim is forcibly reverified
without permitting another counter-search. In the worst case, verified mode makes thirty-one
OpenAI requests: one decomposition, ten evidence updates, up to ten verification
calls, up to nine ordinary decisions, and one report request.

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

The current nine-fixture benchmark is frozen under `evaluation/fixtures/`: remote work,
the Late Bronze Age collapse, quantum commercial advantage, carbon capture,
social-media polarization, synthetic data for LLM training, chain-of-thought
effectiveness, inference-time compute scaling, and multi-agent LLM systems. Each
directory contains the exact supplied question and reference report plus the generated
atomic rubric and hash metadata.

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

### Automated Frozen-Fixture Suite

Preview the complete fixture-suite plan without making Tavily or OpenAI calls:

```powershell
python scripts/run_fixture_suite.py --dry-run
```

Run every frozen fixture question sequentially in verified mode, then evaluate all
successful newly saved runs with Evaluator v1 and create an aggregate benchmark:

```powershell
python scripts/run_fixture_suite.py
```

Choose the research architecture by placing its name after the script:

| Command | Research components |
| --- | --- |
| `python scripts/run_fixture_suite.py llm-only` | One structured OpenAI generation using the canonical report format; no retrieval or research components |
| `python scripts/run_fixture_suite.py baseline` | Baseline analyzer; no ledger, decomposition, or verification |
| `python scripts/run_fixture_suite.py ledger` | Evidence ledger only |
| `python scripts/run_fixture_suite.py decomposed` | Evidence ledger and question decomposer |
| `python scripts/run_fixture_suite.py verified` | Ledger, decomposer, independent verifier, and adversarial counter-search |

Omitting the architecture is equivalent to `verified`. Add `--dry-run` to any command
to inspect its plan without calling Tavily or OpenAI, for example
`python scripts/run_fixture_suite.py ledger --dry-run`.

The research phase always finishes before the evaluation phase begins. The script
discovers frozen fixtures in stable fixture-ID order and validates that every saved run
matches its fixture and requested architecture. Fixed-suite reports, traces, logs, and
per-report evaluations are kept separate from ad-hoc research beneath
`outputs/preset-questions/<question>/`. Aggregate benchmark JSON, CSV, Markdown, and the
suite manifest are written beneath
`outputs/preset-questions/evaluation-results/fixture-suite-<timestamp>-<mode>/`.

Choose another architecture or a smaller fixture subset when needed:

```powershell
python scripts/run_fixture_suite.py decomposed
python scripts/run_fixture_suite.py --fixture remote-work-productivity --fixture chain-of-thought-effectiveness
python scripts/run_fixture_suite.py --outputs-root outputs/another-fixed-suite
```

The older `--mode ledger` form remains supported for compatibility.

The script continues to later research questions if one run fails, evaluates every
successful run, records skipped/failed items in the manifest, and exits nonzero unless
the whole selected suite succeeds. With the current nine fixtures, verified mode can
make at most 27 Tavily searches and 90 research OpenAI requests. Evaluator-v1 usage is
additional and report-dependent: it uses one comprehensiveness judgment, one citation
completeness judgment, and one citation-support judgment per final finding, with at
most one semantic repair attempt per structured judgment. OpenAI SDK retries may add
HTTP attempts. Running the non-dry command can therefore incur substantial API charges.
The LLM-only fixture suite uses exactly nine logical research-generation requests and
zero Tavily searches before evaluation.

Evaluator-v1 results are stored without overwriting earlier results:

```text
outputs/<run>/evaluations/evaluator-v1/<fixture-id>/
├── evaluation.json
└── evaluation.md
```

Benchmark and comparison summaries are written below `evaluation/results/`. Mixed
architecture benchmark rows are sorted in canonical V-1, V0, V1, V2, V3 order. Every
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

- `report.md`: for V-1, the exact raw model output; for V0–V3, the final research findings rendered deterministically from the structured report with claims and evidence visually separated.
- `research_log.md`: a chronological explanation of searches, state updates, decisions, and timings. Ledger-mode logs explicitly show new and updated claims, confidence/status transitions, gap changes, and a state summary after every iteration. Decomposed-mode logs also show the initial plan, per-iteration subquestion progress, transitions, and targeted search counts. Verified-mode logs add neutral-evidence verification records, before/after reconciliation, counter-search lifecycle, search-purpose allocation, verifier calls, verdict counts, and change counts.
- `trace.json`: the machine-readable trace. V-1 records one OpenAI call, zero Tavily calls, token usage when available, latency, empty sources/iterations, and `single_llm_call_complete`; it deliberately has no structured final report or research state. V0–V3 record decisions, their stop reason, model, structured final report, and exact source snapshots. Ledger mode additionally preserves the full evidence ledger, evidence relationships, gap creation/resolution, and decision targets; decomposed mode also preserves the full research plan and status transitions. Verified mode adds `claim_verifications`, `search_purpose`, `search_target_id`, `decision_origin`, and counter-search metadata.

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
- do not use embeddings; only verified mode adds an independent verifier;
- may still miss contradictions or create semantically overlapping claims;
- may be vulnerable to imperfect retrieval;
- uses prompt-level protection against instructions embedded in webpages rather than a complete prompt-injection defense.

Retrieved web content is treated as untrusted data in every model prompt that receives it, but prompt instructions alone are not a complete security boundary.
