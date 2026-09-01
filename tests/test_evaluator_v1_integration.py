from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

import pytest

from evaluation.v1.adapters import load_evaluation_input
from evaluation.v1.benchmark import (
    BenchmarkEntry,
    save_benchmark,
    save_comparison,
    save_model_family_comparison,
)
from evaluation.v1.comprehensiveness import ComprehensivenessEvaluator
from evaluation.v1.fixtures import load_frozen_fixture, sha256_file
from evaluation.v1.models import (
    ComprehensivenessJudgment,
    FixtureMetadata,
    NovelValue,
    RequirementEvaluation,
    Rubric,
    RubricRequirement,
)
from evaluation.v1.renderer import save_evaluation
from evaluation.v1.runner import EvaluatorRunner
from research.models import (
    ClaimStatus,
    Confidence,
    EvidenceItem,
    EvidenceLedger,
    EvidenceRelation,
    EvidenceRelationType,
    EvidenceStrength,
    FinalReport,
    Finding,
    LedgerClaim,
    ResearchState,
    Source,
)
from research.llm_only_runner import LLMOnlyRunResult, save_llm_only_artifacts
from research.report import save_research_outputs
from research.versions import CANONICAL_SYSTEM_VERSIONS


class FakeResponses:
    def __init__(self, outputs: list[object]) -> None:
        self.outputs = list(outputs)
        self.calls: list[dict[str, object]] = []

    def parse(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(output_parsed=self.outputs.pop(0), usage=None)


def saved_run(root: Path, ledger: bool = False) -> Path:
    question = "Exact benchmark question"
    source = Source(id="S1", title="Study", url="https://example.com", content="Direct support")
    report = FinalReport(
        question=question,
        summary="A substantive summary.",
        findings=[
            Finding(
                claim="A substantive claim.",
                evidence=[EvidenceItem(summary="Evidence", source_ids=["S1"])],
                confidence=Confidence.HIGH,
                confidence_reason="Direct evidence.",
            )
        ],
        conclusion="A bounded conclusion.",
    )
    evidence_ledger = EvidenceLedger()
    if ledger:
        evidence_ledger = EvidenceLedger(
            claims=[
                LedgerClaim(
                    id="C1",
                    claim="A substantive claim.",
                    supporting_evidence=[
                        EvidenceRelation(
                            source_id="S1",
                            relation=EvidenceRelationType.SUPPORTS,
                            summary="Direct support.",
                            strength=EvidenceStrength.DIRECT,
                        )
                    ],
                    confidence=Confidence.HIGH,
                    confidence_reason="Direct evidence.",
                    status=ClaimStatus.SUPPORTED,
                    first_seen_iteration=1,
                    last_updated_iteration=1,
                )
            ]
        )
    state = ResearchState(
        question=question,
        sources=[source],
        stop_reason="sufficient_evidence",
        system_version="evidence-ledger-v1" if ledger else "baseline-zero",
        evidence_ledger=evidence_ledger,
    )
    report_path, _ = save_research_outputs(state, report, "research-model", root)
    return report_path.parent


def fixture(root: Path):
    root.mkdir()
    question_path = root / "question.md"
    reference_path = root / "reference_report.md"
    rubric_path = root / "rubric.json"
    question_path.write_text("Exact benchmark question", encoding="utf-8")
    reference_path.write_text("Frozen reference", encoding="utf-8")
    requirement = RubricRequirement(
        id="R1",
        category="scope",
        requirement="Address the central evidence.",
        description="Central evidence requirement.",
        importance=3,
        evidence_expected=True,
    )
    rubric = Rubric(rubric_version="1.0", fixture_id=root.name, requirements=[requirement])
    rubric_path.write_text(json.dumps(rubric.model_dump(mode="json")), encoding="utf-8")
    metadata = FixtureMetadata(
        fixture_id=root.name,
        fixture_version="1.0",
        question_sha256=sha256_file(question_path),
        reference_report_sha256=sha256_file(reference_path),
        rubric_sha256=sha256_file(rubric_path),
        created_at=datetime.now(timezone.utc).isoformat(),
        status="frozen",
        builder_model="builder-model",
        prompt_versions={"rubric_builder": "1.0", "rubric_critic": "1.0"},
    )
    (root / "fixture.json").write_text(json.dumps(metadata.model_dump(mode="json")), encoding="utf-8")
    return load_frozen_fixture(root)


def test_old_run_loads_without_ledger_and_evaluation_does_not_mutate_it(tmp_path: Path) -> None:
    run = saved_run(tmp_path / "run")
    trace_path = run / "trace.json"
    legacy_trace = json.loads(trace_path.read_text(encoding="utf-8"))
    legacy_trace.pop("research_model", None)
    trace_path.write_text(json.dumps(legacy_trace), encoding="utf-8")
    before = {path.name: path.read_bytes() for path in run.iterdir() if path.is_file()}
    item = load_evaluation_input(run)
    assert item.structured_claim_evidence_available is False
    assert item.system_version == "baseline-zero"
    assert item.research_model == "unknown"
    after = {path.name: path.read_bytes() for path in run.iterdir() if path.is_file()}
    assert before == after


def test_new_ledger_run_loads_structured_claim_evidence(tmp_path: Path) -> None:
    item = load_evaluation_input(saved_run(tmp_path / "ledger-run", ledger=True))
    assert item.system_version == "evidence-ledger-v1"
    assert item.structured_claim_evidence_available is True
    assert item.evidence_ledger["claims"][0]["id"] == "C1"


def test_evaluator_v1_scores_llm_only_report_with_same_frozen_fixture(
    tmp_path: Path,
) -> None:
    run = tmp_path / "llm-only-run"
    save_llm_only_artifacts(
        LLMOnlyRunResult(
            question="Exact benchmark question",
            system_version="llm-only-baseline-v0",
            model="research-model",
            report=FinalReport(
                question="Exact benchmark question",
                summary="A substantive claim without a verified citation.",
                findings=[
                    Finding(
                        claim="A substantive claim.",
                        evidence=[EvidenceItem(summary="Unverified model knowledge.")],
                        confidence=Confidence.LOW,
                        confidence_reason="No retrieved evidence is available.",
                    )
                ],
                conflicts_and_uncertainties=[],
                remaining_gaps=[],
                conclusion="A substantive claim.",
            ),
            duration_seconds=0.1,
            input_tokens=10,
            output_tokens=20,
        ),
        run,
    )
    frozen = fixture(tmp_path / "llm-only-fixture")
    comprehensive = ComprehensivenessJudgment(
        requirements=[
            RequirementEvaluation(
                requirement_id="R1",
                coverage=0.5,
                depth=0.25,
                candidate_evidence=["A substantive claim."],
                missing=["Evidence and qualification are missing."],
                rationale="The requirement is mentioned but not researched deeply.",
            )
        ],
        novel_value=NovelValue(present=False),
    )
    fake = FakeResponses([comprehensive])
    client = SimpleNamespace(responses=fake)
    comp = ComprehensivenessEvaluator("unused", "judge-model", client=client)

    result = EvaluatorRunner("judge-model", comp).evaluate(
        load_evaluation_input(run), frozen
    )

    assert result.system_version == "llm-only-baseline-v0"
    assert result.comprehensiveness.score == pytest.approx(0.375)
    assert result.citations is None
    assert result.deterministic_integrity.score == 1.0
    assert result.evaluation_completeness == 1.0
    assert result.overall_score == pytest.approx(37.5)
    assert result.metadata.research_model == "research-model"
    assert result.metadata.scoring_weights == {"coverage": 0.5, "depth": 0.5}
    assert len(fake.calls) == 1
    assert all(call["model"] == "judge-model" for call in fake.calls)
    assert all(call["model"] != "research-model" for call in fake.calls)


def test_full_v1_result_saves_metadata_and_comparison_outputs(tmp_path: Path) -> None:
    run = saved_run(tmp_path / "run")
    frozen = fixture(tmp_path / "fixture")
    comprehensive = ComprehensivenessJudgment(
        requirements=[
            RequirementEvaluation(
                requirement_id="R1",
                coverage=1.0,
                depth=0.75,
                candidate_evidence=["A substantive claim."],
                missing=["More counterevidence."],
                rationale="Substantial treatment.",
            )
        ],
        novel_value=NovelValue(present=False),
    )
    fake = FakeResponses([comprehensive])
    client = SimpleNamespace(responses=fake)
    comp = ComprehensivenessEvaluator("unused", "judge-model", client=client)
    result = EvaluatorRunner("judge-model", comp).evaluate(
        load_evaluation_input(run), frozen
    )
    first_json, first_md = save_evaluation(run, result)
    second_json, _ = save_evaluation(run, result)
    assert result.overall_score is not None
    assert result.metadata.rubric_hash == frozen.metadata.rubric_sha256
    assert first_json.parent.parent.name == "evaluator-v1"
    assert second_json.parent.name.endswith("_2")
    rendered = first_md.read_text(encoding="utf-8")
    assert "## Coverage and Depth" in rendered
    assert "Citation quality" not in rendered
    saved_result = json.loads(first_json.read_text(encoding="utf-8"))
    assert saved_result["overall_score"] == pytest.approx(87.5)
    assert saved_result["comprehensiveness"]["score"] == pytest.approx(0.875)
    assert "citations" not in saved_result

    benchmark_json, benchmark_csv, _ = save_benchmark(
        [BenchmarkEntry(run="run", result=result)], tmp_path / "results"
    )
    assert benchmark_json.is_file() and benchmark_csv.is_file()
    benchmark_row = json.loads(benchmark_json.read_text(encoding="utf-8"))[0]
    assert benchmark_row["research_model"] == "research-model"
    assert benchmark_row["evaluator_model"] == "judge-model"
    assert "citation_support" not in benchmark_row
    reversed_entries = [
        BenchmarkEntry(
            run=system_version,
            result=result.model_copy(update={"system_version": system_version}),
        )
        for system_version in reversed(CANONICAL_SYSTEM_VERSIONS)
    ]
    ordered_json, _, _ = save_benchmark(reversed_entries, tmp_path / "results")
    ordered_rows = json.loads(ordered_json.read_text(encoding="utf-8"))
    assert [row["system_version"] for row in ordered_rows] == list(
        CANONICAL_SYSTEM_VERSIONS
    )
    comparison_json, comparison_md = save_comparison(run, run, tmp_path / "results")
    assert json.loads(comparison_json.read_text(encoding="utf-8"))["metrics"]["overall"][
        "delta"
    ] == pytest.approx(0.0)
    assert "Ablation Comparison" in comparison_md.read_text(encoding="utf-8")


def test_cross_model_comparison_reports_architecture_deltas(tmp_path: Path) -> None:
    luna_path = tmp_path / "luna.json"
    mini_path = tmp_path / "mini.json"
    versions = list(CANONICAL_SYSTEM_VERSIONS)
    luna_rows = [
        {
            "system_version": version,
            "coverage": 0.50 + index * 0.05,
            "depth": 0.40 + index * 0.04,
            "research_model": "gpt-5.6-luna",
            "evaluator_model": "gpt-5.6-luna",
        }
        for index, version in enumerate(versions)
    ]
    mini_rows = [
        {
            "system_version": version,
            "coverage": 0.30 + index * 0.10,
            "depth": 0.20 + index * 0.08,
            "research_model": "gpt-4o-mini",
            "evaluator_model": "gpt-5.6-luna",
        }
        for index, version in enumerate(versions)
    ]
    luna_path.write_text(json.dumps(luna_rows), encoding="utf-8")
    mini_path.write_text(json.dumps(mini_rows), encoding="utf-8")

    comparison_json, comparison_md = save_model_family_comparison(
        [luna_path], [mini_path], tmp_path / "results"
    )

    payload = json.loads(comparison_json.read_text(encoding="utf-8"))
    first_delta = payload["architecture_deltas"][0]["families"]
    assert first_delta["Luna"]["coverage"] == pytest.approx(0.05)
    assert first_delta["GPT-4o-mini"]["coverage"] == pytest.approx(0.10)
    rendered = comparison_md.read_text(encoding="utf-8")
    assert "Marginal Architecture Deltas" in rendered
    assert "GPT-4o-mini Coverage" in rendered
