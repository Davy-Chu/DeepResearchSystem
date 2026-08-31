"""Pure-Python integrity checks for historical baseline and ledger runs."""

from __future__ import annotations

import re

from evaluation.v1.models import (
    CheckStatus,
    DeterministicCheck,
    DeterministicIntegrityResult,
    EvaluationInput,
)
from research.models import Confidence


SOURCE_ID = re.compile(r"^S[1-9][0-9]*$")
CLAIM_ID = re.compile(r"^C[1-9][0-9]*$")


def _present(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


class DeterministicEvaluator:
    def evaluate(self, item: EvaluationInput) -> DeterministicIntegrityResult:
        checks: list[DeterministicCheck] = []

        def add(name: str, status: CheckStatus, details: str | None = None) -> None:
            checks.append(DeterministicCheck(check_name=name, status=status, details=details))

        def binary(name: str, passed: bool, details: str) -> None:
            add(name, CheckStatus.PASS if passed else CheckStatus.FAIL, None if passed else details)

        binary("run_metadata_loads", bool(item.question), "Saved question is missing.")
        binary("report_exists", bool(item.report_markdown.strip()), "Report is empty.")
        binary("sources_present", bool(item.sources), "No saved sources are available.")

        if item.report is None:
            add(
                "structured_report_parses",
                CheckStatus.NOT_EVALUABLE,
                item.trace_metadata.get("report_validation_error")
                or "This historical run has no structured final report.",
            )
        else:
            add("structured_report_parses", CheckStatus.PASS)
            binary(
                "report_question_matches",
                item.report.question.strip() == item.question.strip(),
                "Structured report question differs from saved question.",
            )

        source_ids = [source.id for source in item.sources]
        binary(
            "source_ids_unique",
            len(source_ids) == len(set(source_ids)),
            "Saved source IDs are not unique.",
        )
        binary(
            "source_ids_syntactically_valid",
            all(SOURCE_ID.fullmatch(source_id) for source_id in source_ids),
            "One or more saved source IDs do not match S<number>.",
        )
        binary(
            "source_urls_present",
            all(_present(source.url) for source in item.sources),
            "One or more saved sources have no URL.",
        )
        valid_sources = set(source_ids)

        citation_ids: list[str] = []
        evidence_valid = True
        confidence_valid = True
        if item.report is not None:
            for finding in item.report.findings:
                evidence_valid = evidence_valid and bool(finding.evidence)
                confidence_valid = confidence_valid and finding.confidence in set(Confidence)
                for evidence in finding.evidence:
                    evidence_valid = evidence_valid and bool(evidence.summary.strip())
                    citation_ids.extend(evidence.source_ids)
            binary(
                "evidence_objects_valid",
                evidence_valid,
                "One or more findings have missing or malformed evidence.",
            )
            binary(
                "confidence_values_valid",
                confidence_valid,
                "One or more finding confidence values are invalid.",
            )
            binary(
                "citation_ids_syntactically_valid",
                all(SOURCE_ID.fullmatch(source_id) for source_id in citation_ids),
                "One or more citation IDs do not match S<number>.",
            )
            binary(
                "citation_ids_resolve",
                set(citation_ids).issubset(valid_sources),
                "One or more citation IDs do not resolve to saved sources.",
            )
        else:
            for name in ("evidence_objects_valid", "confidence_values_valid"):
                add(name, CheckStatus.NOT_EVALUABLE, "Structured report unavailable.")
            markdown_citations = re.findall(r"\[(S[1-9][0-9]*)\]", item.report_markdown)
            if markdown_citations:
                add("citation_ids_syntactically_valid", CheckStatus.PASS)
                binary(
                    "citation_ids_resolve",
                    set(markdown_citations).issubset(valid_sources),
                    "One or more Markdown citation IDs do not resolve to saved sources.",
                )
            else:
                add(
                    "citation_ids_syntactically_valid",
                    CheckStatus.NOT_EVALUABLE,
                    "No parseable structured or Markdown citations are available.",
                )
                add(
                    "citation_ids_resolve",
                    CheckStatus.NOT_EVALUABLE,
                    "No parseable structured or Markdown citations are available.",
                )

        ledger = item.evidence_ledger
        if not item.structured_claim_evidence_available or ledger is None:
            add(
                "structured_claim_evidence_available",
                CheckStatus.NOT_EVALUABLE,
                "This run predates or does not use an evidence ledger.",
            )
            for name in (
                "ledger_claim_ids_unique",
                "ledger_evidence_relationships_resolve",
                "ledger_confidence_values_valid",
                "ledger_evidence_ids_unique",
            ):
                add(name, CheckStatus.NOT_EVALUABLE, "Evidence ledger unavailable.")
        else:
            add("structured_claim_evidence_available", CheckStatus.PASS)
            claims = ledger.get("claims") if isinstance(ledger.get("claims"), list) else []
            claim_ids = [str(claim.get("id") or "") for claim in claims if isinstance(claim, dict)]
            binary(
                "ledger_claim_ids_unique",
                len(claim_ids) == len(set(claim_ids))
                and all(CLAIM_ID.fullmatch(claim_id) for claim_id in claim_ids),
                "Ledger claim IDs are duplicate or malformed.",
            )
            relation_ids: list[str] = []
            ledger_confidences: list[str] = []
            for claim in claims:
                if not isinstance(claim, dict):
                    continue
                ledger_confidences.append(str(claim.get("confidence") or ""))
                for key in ("supporting_evidence", "contradicting_evidence"):
                    for relation in claim.get(key) or []:
                        if isinstance(relation, dict):
                            relation_ids.append(str(relation.get("source_id") or ""))
            binary(
                "ledger_evidence_relationships_resolve",
                set(relation_ids).issubset(valid_sources),
                "One or more ledger evidence relationships are dangling.",
            )
            binary(
                "ledger_confidence_values_valid",
                all(value in {member.value for member in Confidence} for value in ledger_confidences),
                "One or more ledger confidence values are invalid.",
            )
            add(
                "ledger_evidence_ids_unique",
                CheckStatus.NOT_EVALUABLE,
                "Current ledger relations have no independent evidence-ID field.",
            )

        passed = sum(check.status == CheckStatus.PASS for check in checks)
        failed = sum(check.status == CheckStatus.FAIL for check in checks)
        unavailable = sum(check.status == CheckStatus.NOT_EVALUABLE for check in checks)
        score = passed / (passed + failed) if passed + failed else None
        return DeterministicIntegrityResult(
            score=score,
            checks=checks,
            passed_count=passed,
            failed_count=failed,
            not_evaluable_count=unavailable,
            structured_claim_evidence_available=item.structured_claim_evidence_available,
        )
