# Evaluator v1 Fixture Authoring

Each fixture directory starts with:

- `question.md`: the exact benchmark question;
- `reference_report.md`: a user-supplied high-quality reference report.

Running the fixture builder adds and freezes:

- `rubric.json`: 5–10 atomic, conclusion-neutral research requirements;
- `fixture.json`: versions and SHA-256 hashes for the question, reference, and rubric.

Reference reports are used only while authoring rubrics. Normal candidate evaluation sends the
question, frozen rubric, and candidate report to the judge; it never sends the reference report.
The references define benchmark scope, not mandatory conclusions or wording.

All five initial benchmark questions now have user-supplied reference reports. Keep these reports
unchanged after freezing so their recorded hashes remain valid. Do not substitute a newly
researched report if benchmark continuity matters.

Build one fixture from the repository root:

```powershell
python main.py evaluator build-fixture evaluation/fixtures/remote-work-productivity
```

Fixture building uses two OpenAI structured-output calls (builder and critic), may retry malformed
outputs once, and can incur API charges. A frozen fixture is never regenerated automatically.
