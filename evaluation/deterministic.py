"""Pure-Python structural and reference checks."""

from __future__ import annotations

from research.models import Confidence

from evaluation.models import (
    DeterministicCheck,
    DeterministicResult,
    EvaluationInput,
)


def _present(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


class DeterministicEvaluator:
    def evaluate(self, evaluation_input: EvaluationInput) -> DeterministicResult:
        checks: list[DeterministicCheck] = []

        def add(name: str, passed: bool, details: str | None = None) -> None:
            checks.append(
                DeterministicCheck(
                    check_name=name,
                    passed=passed,
                    details=None if passed else details,
                )
            )

        add("question_exists", _present(evaluation_input.question), "Research question is missing.")
        report = evaluation_input.report
        add("report_exists", report is not None, "Structured final report is missing.")
        add(
            "at_least_one_finding",
            bool(report and report.findings),
            "The report contains no findings.",
        )
        add("at_least_one_source", bool(evaluation_input.sources), "The run contains no sources.")

        if report is not None:
            add("report_summary_exists", _present(report.summary), "Report summary is empty.")
            add("report_conclusion_exists", _present(report.conclusion), "Report conclusion is empty.")
            add(
                "report_question_matches",
                report.question.strip() == evaluation_input.question.strip(),
                "The report question differs from the saved research question.",
            )

        source_ids = [source.id for source in evaluation_input.sources]
        duplicate_ids = sorted({item for item in source_ids if source_ids.count(item) > 1})
        add(
            "source_ids_unique",
            not duplicate_ids,
            "Duplicate source ID(s): " + ", ".join(duplicate_ids),
        )
        valid_ids = {source.id for source in evaluation_input.sources if _present(source.id)}

        for index, source in enumerate(evaluation_input.sources, start=1):
            label = source.id.strip() if _present(source.id) else str(index)
            add(
                f"source_{label}_id_exists",
                _present(source.id),
                f"Source {index} has no ID.",
            )
            add(
                f"source_{label}_url_exists",
                _present(source.url),
                f"Source {label} has no URL.",
            )
            add(
                f"source_{label}_content_exists",
                _present(source.content),
                f"Source {label} has no saved source content.",
            )

        if report is not None:
            allowed_confidence = {item.value for item in Confidence}
            for finding_number, finding in enumerate(report.findings, start=1):
                finding_id = f"F{finding_number}"
                add(
                    f"{finding_id}_claim_exists",
                    _present(finding.claim),
                    f"Finding {finding_id} has an empty claim.",
                )
                add(
                    f"{finding_id}_evidence_exists",
                    bool(finding.evidence),
                    f"Finding {finding_id} has no evidence.",
                )
                confidence = finding.confidence
                confidence_value = getattr(confidence, "value", confidence)
                add(
                    f"{finding_id}_confidence_exists",
                    confidence is not None and _present(str(confidence_value)),
                    f"Finding {finding_id} has no confidence.",
                )
                add(
                    f"{finding_id}_confidence_valid",
                    confidence_value in allowed_confidence,
                    f"Finding {finding_id} has invalid confidence: {confidence_value!r}.",
                )
                for evidence_number, evidence in enumerate(finding.evidence, start=1):
                    prefix = f"{finding_id}_evidence_{evidence_number}"
                    add(
                        f"{prefix}_summary_exists",
                        _present(evidence.summary),
                        f"Evidence {evidence_number} for {finding_id} has an empty summary.",
                    )
                    add(
                        f"{prefix}_source_ids_exist",
                        bool(evidence.source_ids),
                        f"Evidence {evidence_number} for {finding_id} has no source IDs.",
                    )
                    unknown = sorted(set(evidence.source_ids) - valid_ids)
                    add(
                        f"{prefix}_source_ids_valid",
                        not unknown,
                        f"Evidence {evidence_number} for {finding_id} references unknown "
                        f"source ID(s): {', '.join(unknown)}.",
                    )

        passed_count = sum(check.passed for check in checks)
        failed_count = len(checks) - passed_count
        return DeterministicResult(
            checks=checks,
            passed_count=passed_count,
            failed_count=failed_count,
            all_passed=failed_count == 0,
        )
