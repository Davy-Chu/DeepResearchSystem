from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

import pytest

from evaluation.v1.fixture_builder import FixtureBuilder
from evaluation.v1.fixtures import (
    load_frozen_fixture,
    match_fixture,
    normalize_question,
    sha256_file,
)
from evaluation.v1.models import FixtureMetadata, Rubric, RubricDraft, RubricRequirement


def requirements() -> list[RubricRequirement]:
    return [
        RubricRequirement(
            id=f"R{number}",
            category="scope",
            requirement=f"Address research obligation {number}.",
            description=f"Atomic obligation {number}.",
            importance=3 if number == 1 else 2,
            evidence_expected=True,
        )
        for number in range(1, 6)
    ]


class FakeResponses:
    def __init__(self, parsed: list[object]) -> None:
        self.parsed = list(parsed)
        self.calls = []

    def parse(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(
            output_parsed=self.parsed.pop(0),
            usage=SimpleNamespace(input_tokens=10, output_tokens=5),
        )


def frozen_fixture(root: Path, question: str = "Exact benchmark question") -> Path:
    root.mkdir()
    question_path = root / "question.md"
    reference_path = root / "reference_report.md"
    rubric_path = root / "rubric.json"
    question_path.write_text(question, encoding="utf-8")
    reference_path.write_text("A high-quality frozen report.", encoding="utf-8")
    rubric = Rubric(rubric_version="1.0", fixture_id=root.name, requirements=requirements())
    rubric_path.write_text(json.dumps(rubric.model_dump(mode="json")), encoding="utf-8")
    metadata = FixtureMetadata(
        fixture_id=root.name,
        fixture_version="1.0",
        question_sha256=sha256_file(question_path),
        reference_report_sha256=sha256_file(reference_path),
        rubric_sha256=sha256_file(rubric_path),
        created_at=datetime.now(timezone.utc).isoformat(),
        status="frozen",
        builder_model="test-model",
        prompt_versions={"rubric_builder": "1.0", "rubric_critic": "1.0"},
    )
    (root / "fixture.json").write_text(
        json.dumps(metadata.model_dump(mode="json")), encoding="utf-8"
    )
    return root


def test_fixture_hash_mismatch_is_detected(tmp_path: Path) -> None:
    fixture_path = frozen_fixture(tmp_path / "fixture")
    assert load_frozen_fixture(fixture_path).metadata.fixture_id == "fixture"
    (fixture_path / "rubric.json").write_text("{}", encoding="utf-8")
    with pytest.raises(ValueError, match="integrity check failed"):
        load_frozen_fixture(fixture_path)


def test_fixture_matching_uses_id_then_exact_normalized_question(tmp_path: Path) -> None:
    first = load_frozen_fixture(frozen_fixture(tmp_path / "first", "Question One"))
    second = load_frozen_fixture(frozen_fixture(tmp_path / "second", "Question Two"))
    assert match_fixture(" question   one ", [first, second]) == first
    assert match_fixture("unrelated", [first, second]) is None
    assert match_fixture("unrelated", [first, second], "second") == second
    assert normalize_question(" A\n B ") == "a b"


def test_builder_uses_two_passes_and_refuses_to_regenerate_frozen_fixture(
    tmp_path: Path,
) -> None:
    fixture_path = tmp_path / "new-fixture"
    fixture_path.mkdir()
    (fixture_path / "question.md").write_text("Benchmark question", encoding="utf-8")
    (fixture_path / "reference_report.md").write_text("Reference report", encoding="utf-8")
    draft = RubricDraft(requirements=requirements())
    responses = FakeResponses([draft, draft])
    builder = FixtureBuilder(
        "unused",
        "gpt-5.6-luna",
        client=SimpleNamespace(responses=responses),
    )
    metadata = builder.build(fixture_path)
    assert metadata.status == "frozen"
    assert len(responses.calls) == 2
    assert all(call["model"] == "gpt-5.6-luna" for call in responses.calls)
    assert builder.usage.llm_calls == 2
    assert load_frozen_fixture(fixture_path).rubric.requirements[0].id == "R1"
    with pytest.raises(ValueError, match="will not be regenerated"):
        builder.build(fixture_path)
