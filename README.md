# Deep Research Agent — Baseline Zero

## What this is

This repository is a small end-to-end baseline for iterative web research. Given a question, it retrieves real web pages with Tavily, asks an OpenAI model to extract evidence-backed findings and identify important gaps, optionally performs a targeted follow-up search, and produces a Markdown report plus a JSON research trace.

The system favors an honest incomplete answer over unsupported completeness. It performs at most three searches.

This repository currently represents the baseline-zero system, not the final take-home architecture.

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

The main loop is ordinary Python in `research/runner.py`. Tavily only retrieves pages; it does not generate answers. OpenAI's Responses API returns Pydantic-validated `IterationAnalysis` and `FinalReport` objects. Python then validates source references and renders Markdown deterministically.

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
```

The model can be changed without editing code. `.env` is ignored by Git, and keys are never logged.

## Running

```bash
python main.py "your research question"
```

For example:

```bash
python main.py "What are the real-world risks and benefits of using synthetic data to train or fine-tune large language models? Focus on data quality, bias, and evaluation."
```

Progress, the stop reason, and artifact paths are printed to the terminal. Missing keys, retrieval failures, OpenAI failures, and malformed structured output cause a clear error and a non-zero exit.

Run the command from the project root, where `main.py` and `.env` are located. A
research run may perform up to three Tavily searches and four OpenAI requests (one
analysis per search plus final report generation), so it may incur API usage or charges.

## Testing

Tests use fakes and make no real API calls:

```bash
pytest
```

## Output

Each run creates a timestamped directory below `outputs/` containing:

- `report.md`: a deterministic Markdown rendering of the structured final report, with claims and evidence visually separated.
- `trace.json`: iteration decisions, queries, findings, conflicts, gaps, stop reason, model, and source metadata. It intentionally excludes full page content.

Source IDs (`S1`, `S2`, and so on) remain stable for a run. Final report generation fails if the model cites an ID that does not map to a retrieved URL.

Research stops with one of four recorded reasons: `sufficient_evidence`, `max_iterations`, `duplicate_query`, or `no_search_results`.

## Current limitations

Baseline zero:

- relies on a general web search provider;
- does not independently score source credibility;
- does not guarantee retrieved pages are authoritative;
- uses LLM judgment for evidence interpretation;
- uses coarse Low/Medium/High confidence;
- has a fixed search budget;
- does not yet perform parallel subquestion research;
- does not yet independently verify citations;
- may miss contradictions;
- may be vulnerable to imperfect retrieval;
- uses prompt-level protection against instructions embedded in webpages rather than a complete prompt-injection defense.

Retrieved web content is treated as untrusted data in every model prompt that receives it, but prompt instructions alone are not a complete security boundary.
