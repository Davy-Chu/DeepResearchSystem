"""Frozen fixture discovery, matching, hashing, and integrity checks."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from pydantic import ValidationError

from evaluation.v1.models import FixtureMetadata, FrozenFixture, Rubric


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def normalize_question(question: str) -> str:
    return " ".join(question.split()).casefold()


def load_frozen_fixture(directory: Path) -> FrozenFixture:
    directory = directory.resolve()
    required = {
        "question.md": directory / "question.md",
        "reference_report.md": directory / "reference_report.md",
        "rubric.json": directory / "rubric.json",
        "fixture.json": directory / "fixture.json",
    }
    missing = [name for name, path in required.items() if not path.is_file()]
    if missing:
        raise ValueError(
            f"Fixture is incomplete ({directory}): missing " + ", ".join(missing)
        )
    try:
        metadata = FixtureMetadata.model_validate_json(
            required["fixture.json"].read_text(encoding="utf-8")
        )
    except (ValidationError, ValueError) as error:
        raise ValueError(f"Fixture metadata is malformed: {error}") from error

    expected_hashes = {
        "question.md": metadata.question_sha256,
        "reference_report.md": metadata.reference_report_sha256,
        "rubric.json": metadata.rubric_sha256,
    }
    mismatches = [
        name
        for name, expected in expected_hashes.items()
        if sha256_file(required[name]) != expected
    ]
    if mismatches:
        raise ValueError(
            "Fixture integrity check failed: "
            + ", ".join(mismatches)
            + " does not match its frozen hash."
        )
    try:
        rubric = Rubric.model_validate_json(required["rubric.json"].read_text(encoding="utf-8"))
    except (ValidationError, ValueError) as error:
        raise ValueError(f"Fixture rubric is malformed: {error}") from error
    if metadata.status != "frozen":
        raise ValueError(f"Fixture is not frozen: {directory}")
    if metadata.fixture_id != rubric.fixture_id or metadata.fixture_id != directory.name:
        raise ValueError("Fixture IDs in directory, fixture.json, and rubric.json must match")
    return FrozenFixture(
        directory=directory,
        question=required["question.md"].read_text(encoding="utf-8").strip(),
        reference_report=required["reference_report.md"].read_text(encoding="utf-8"),
        rubric=rubric,
        metadata=metadata,
    )


def discover_fixtures(root: Path) -> list[FrozenFixture]:
    if not root.is_dir():
        return []
    fixtures: list[FrozenFixture] = []
    for directory in sorted(path for path in root.iterdir() if path.is_dir()):
        if (directory / "fixture.json").is_file():
            fixtures.append(load_frozen_fixture(directory))
    return fixtures


def match_fixture(
    question: str,
    fixtures: list[FrozenFixture],
    benchmark_fixture_id: str | None = None,
) -> FrozenFixture | None:
    if benchmark_fixture_id:
        matches = [item for item in fixtures if item.metadata.fixture_id == benchmark_fixture_id]
        if len(matches) > 1:
            raise ValueError(f"Duplicate fixture ID: {benchmark_fixture_id}")
        return matches[0] if matches else None
    normalized = normalize_question(question)
    matches = [item for item in fixtures if normalize_question(item.question) == normalized]
    if len(matches) > 1:
        raise ValueError("Multiple frozen fixtures exactly match the saved question")
    return matches[0] if matches else None


def resolve_fixture(reference: str | None, fixtures_root: Path) -> FrozenFixture | None:
    if reference is None:
        return None
    candidate = Path(reference)
    if candidate.is_dir():
        return load_frozen_fixture(candidate)
    fixture_path = fixtures_root / reference
    if fixture_path.is_dir():
        return load_frozen_fixture(fixture_path)
    raise ValueError(f"Frozen fixture does not exist: {reference}")
