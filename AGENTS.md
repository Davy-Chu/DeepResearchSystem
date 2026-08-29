# Mandatory Live Research Approval Policy

Codex must never initiate a live research run on its own.

Before every live research run, Codex must:

1. clearly state that the run will contact Tavily and OpenAI and may incur API usage or charges;
2. ask the user for explicit permission to perform that specific run; and
3. wait until the user grants permission before executing it.

Without that explicit permission, Codex must not run `python main.py`, invoke the
application's live research workflow through another command, or directly make Tavily
or OpenAI requests on the application's behalf.

The following do not count as permission:

- API credentials being available in `.env`;
- permission granted for an earlier research run;
- a request to implement, debug, test, review, or verify code;
- a specification that mentions a smoke test;
- an assumption that a live run would be useful.

Permission applies to one specifically described live run only. A subsequent run
requires a new approval request.

Codex may edit files, inspect code, compile the project, and run mocked or unit tests
that make no external research/API calls without requesting live-run permission.

This policy applies to smoke tests, demonstrations, debugging, acceptance testing,
and all other live research executions.
