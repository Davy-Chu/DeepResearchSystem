"""Human-readable observability for evidence-ledger-v1 research runs."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from time import perf_counter

from research.models import (
    ClaimStatus,
    ClaimVerificationRecord,
    EvidenceLedger,
    EvidenceProcessingResult,
    FinalReport,
    GapStatus,
    LedgerChangeType,
    LedgerUpdateSummary,
    ResearchDecision,
    ResearchGap,
    ResearchPlan,
    ResearchState,
    SearchPurpose,
    Source,
    SubQuestionStatusChange,
)


@dataclass
class LedgerIterationLog:
    iteration_number: int
    search_query: str
    query_reason: str
    results_returned: int
    new_sources: list[Source]
    search_duration: float
    search_purpose: SearchPurpose = SearchPurpose.GENERAL
    search_target_id: str | None = None
    processing_attempted: bool = False
    processing_result: EvidenceProcessingResult | None = None
    ledger_updates: LedgerUpdateSummary | None = None
    ledger_snapshot: EvidenceLedger | None = None
    gaps_snapshot: list[ResearchGap] = field(default_factory=list)
    processing_duration: float | None = None
    decision: ResearchDecision | None = None
    decision_duration: float | None = None
    decision_model_call: bool = False
    decision_attempted: bool = False
    stop_reason: str | None = None
    subquestion_status_changes: list[SubQuestionStatusChange] = field(
        default_factory=list
    )
    research_plan_snapshot: ResearchPlan | None = None
    verification_attempts: int = 0
    verifications: list[ClaimVerificationRecord] = field(default_factory=list)
    verification_duration: float = 0.0


@dataclass
class LedgerResearchLogger:
    question: str
    model: str
    max_iterations: int
    system_version: str = "evidence-ledger-v1"
    search_provider: str = "Tavily"
    verifier_model: str | None = None
    iterations: list[LedgerIterationLog] = field(default_factory=list)
    start_time: datetime | None = None
    end_time: datetime | None = None
    total_runtime: float | None = None
    report_duration: float | None = None
    final_stop_reason: str | None = None
    remaining_gaps: list[str] = field(default_factory=list)
    status: str = "Not started"
    failure_stage: str | None = None
    error_message: str | None = None
    research_plan: ResearchPlan | None = None
    decomposition_attempted: bool = False
    decomposition_duration: float | None = None
    report_attempted: bool = False
    _start_counter: float | None = field(default=None, repr=False)

    def start_run(self) -> None:
        self.start_time = datetime.now().astimezone()
        self._start_counter = perf_counter()
        self.status = "Running"

    def record_research_plan(self, plan: ResearchPlan, duration: float) -> None:
        self.research_plan = plan.model_copy(deep=True)
        self.decomposition_duration = duration

    def record_decomposition_attempt(self) -> None:
        self.decomposition_attempted = True

    def record_search(
        self,
        iteration_number: int,
        search_query: str,
        query_reason: str,
        results_returned: int,
        new_sources: list[Source],
        duration: float,
        search_purpose: SearchPurpose = SearchPurpose.GENERAL,
        search_target_id: str | None = None,
    ) -> None:
        self.iterations.append(
            LedgerIterationLog(
                iteration_number=iteration_number,
                search_query=search_query,
                query_reason=query_reason,
                results_returned=results_returned,
                new_sources=list(new_sources),
                search_duration=duration,
                search_purpose=search_purpose,
                search_target_id=search_target_id,
            )
        )

    def record_processing(
        self,
        iteration_number: int,
        result: EvidenceProcessingResult,
        updates: LedgerUpdateSummary,
        state: ResearchState,
        duration: float,
        status_changes: list[SubQuestionStatusChange] | None = None,
    ) -> None:
        item = self._iteration(iteration_number)
        item.processing_attempted = True
        item.processing_result = result.model_copy(deep=True)
        item.ledger_updates = updates.model_copy(deep=True)
        item.ledger_snapshot = state.evidence_ledger.model_copy(deep=True)
        item.gaps_snapshot = [gap.model_copy(deep=True) for gap in state.research_gaps]
        item.processing_duration = duration
        item.subquestion_status_changes = [
            change.model_copy(deep=True) for change in (status_changes or [])
        ]
        item.research_plan_snapshot = (
            state.research_plan.model_copy(deep=True)
            if state.research_plan is not None
            else None
        )

    def record_processing_attempt(self, iteration_number: int) -> None:
        self._iteration(iteration_number).processing_attempted = True

    def record_decision_attempt(self, iteration_number: int) -> None:
        self._iteration(iteration_number).decision_attempted = True

    def record_report_attempt(self) -> None:
        self.report_attempted = True

    def record_verification_attempt(self, iteration_number: int) -> None:
        self._iteration(iteration_number).verification_attempts += 1

    def record_verification(
        self,
        iteration_number: int,
        record: ClaimVerificationRecord,
        duration: float,
        state: ResearchState,
        status_changes: list[SubQuestionStatusChange] | None = None,
    ) -> None:
        item = self._iteration(iteration_number)
        item.verifications.append(record.model_copy(deep=True))
        item.verification_duration += duration
        item.ledger_snapshot = state.evidence_ledger.model_copy(deep=True)
        item.research_plan_snapshot = (
            state.research_plan.model_copy(deep=True)
            if state.research_plan is not None
            else None
        )
        item.subquestion_status_changes = [
            change.model_copy(deep=True) for change in (status_changes or [])
        ]

    def synchronize_verification(self, record: ClaimVerificationRecord) -> None:
        """Refresh an earlier log snapshot after its counter-search executes."""
        for iteration in self.iterations:
            for index, logged in enumerate(iteration.verifications):
                if logged.id == record.id:
                    iteration.verifications[index] = record.model_copy(deep=True)

    def record_decision(
        self,
        iteration_number: int,
        decision: ResearchDecision,
        duration: float,
        model_call: bool,
        stop_reason: str | None = None,
    ) -> None:
        item = self._iteration(iteration_number)
        item.decision = decision.model_copy(deep=True)
        item.decision_duration = duration
        item.decision_model_call = model_call
        if model_call:
            item.decision_attempted = True
        item.stop_reason = stop_reason

    def finish_run(
        self,
        state: ResearchState,
        report: FinalReport,
        report_duration: float,
        total_runtime: float,
    ) -> None:
        self.end_time = datetime.now().astimezone()
        self.total_runtime = total_runtime
        self.report_duration = report_duration
        self.report_attempted = True
        self.final_stop_reason = state.stop_reason
        self.remaining_gaps = list(report.remaining_gaps)
        self.status = "Completed"

    def record_failure(
        self,
        stage: str,
        error: BaseException,
        total_runtime: float | None = None,
    ) -> None:
        self.end_time = datetime.now().astimezone()
        self.total_runtime = total_runtime if total_runtime is not None else self.current_runtime()
        self.status = "Failed"
        self.failure_stage = stage
        self.error_message = self._sanitize_error(error)

    def record_recovered_state(
        self, state: ResearchState, report: FinalReport
    ) -> None:
        self.final_stop_reason = state.stop_reason
        self.remaining_gaps = list(report.remaining_gaps)

    def current_runtime(self) -> float:
        if self._start_counter is None:
            return 0.0
        return perf_counter() - self._start_counter

    def save(self, output_dir: Path) -> Path:
        output_dir.mkdir(parents=True, exist_ok=True)
        path = output_dir / "research_log.md"
        path.write_text(self.render_markdown(), encoding="utf-8")
        return path

    def render_markdown(self) -> str:
        lines = self._render_summary()
        lines.extend(self._render_research_plan())
        for iteration in self.iterations:
            lines.extend(self._render_iteration(iteration))
        lines.extend(self._render_final_decision())
        lines.extend(self._render_performance())
        lines.extend(self._render_verifier_diagnostics())
        return "\n".join(lines).rstrip() + "\n"

    def _render_summary(self) -> list[str]:
        unique_sources = {
            source.id for iteration in self.iterations for source in iteration.new_sources
        }
        lines = [
            "# Research Run Log",
            "",
            "## Run Summary",
            "",
            f"**System Version:** {self.system_version}",
            "",
            "**Research Question**",
            "",
            self.question,
            "",
            f"**Status:** {self.status}",
            "",
        ]
        if self.final_stop_reason:
            lines.extend([f"**Stop Reason:** {self.final_stop_reason}", ""])
        if self.failure_stage:
            lines.extend([f"**Failure Stage:** {self.failure_stage}", ""])
        if self.error_message:
            lines.extend(["**Error**", "", self.error_message, ""])
        lines.extend(
            [
                f"**Search Provider:** {self.search_provider}",
                "",
                f"**Model:** {self.model}",
                "",
                f"**Searches Performed:** {len(self.iterations)} / {self.max_iterations}",
                "",
                f"**Unique Sources:** {len(unique_sources)}",
                "",
                f"**OpenAI Calls:** {self._openai_calls()}",
                "",
                f"**Tavily Calls:** {len(self.iterations)}",
                "",
            ]
        )
        if self.verifier_model:
            lines.extend([f"**Verifier Model:** {self.verifier_model}", ""])
        if self.start_time:
            lines.extend([f"**Started:** {self.start_time.isoformat(timespec='seconds')}", ""])
        if self.end_time:
            lines.extend([f"**Ended:** {self.end_time.isoformat(timespec='seconds')}", ""])
        if self.total_runtime is not None:
            lines.extend([f"**Total Runtime:** {self._duration(self.total_runtime)}", ""])
        lines.extend(["---", ""])
        return lines

    def _render_research_plan(self) -> list[str]:
        if self.research_plan is None:
            return []
        lines = ["# Research Plan", "", "## Subquestions", ""]
        for item in self.research_plan.subquestions:
            lines.extend(
                [
                    f"### {item.id} [{item.importance.value}]",
                    "",
                    "**Question:**",
                    "",
                    item.question,
                    "",
                    "**Success criteria:**",
                    "",
                    item.success_criteria,
                    "",
                    f"**Initial status:** {item.status.value}",
                    "",
                ]
            )
        if self.research_plan.synthesis_requirements:
            lines.extend(
                [
                    "## Synthesis Requirements",
                    "",
                    *[
                        f"- {requirement}"
                        for requirement in self.research_plan.synthesis_requirements
                    ],
                    "",
                ]
            )
        if self.research_plan.output_requirements:
            lines.extend(
                [
                    "## Output Requirements",
                    "",
                    *[
                        f"- {requirement}"
                        for requirement in self.research_plan.output_requirements
                    ],
                    "",
                ]
            )
        lines.extend(["---", ""])
        return lines

    def _render_iteration(self, item: LedgerIterationLog) -> list[str]:
        lines = [
            f"# Iteration {item.iteration_number}",
            "",
            "## 1. Search",
            "",
            "**Query**",
            "",
            f"> {item.search_query}",
            "",
            f"**Purpose:** {item.search_purpose.value}",
            "",
            "**Why this query**",
            "",
            item.query_reason,
            "",
            f"{item.results_returned} result(s) retrieved; "
            f"{len(item.new_sources)} new unique source(s) added.",
            "",
        ]
        if item.search_target_id:
            lines[8:8] = [f"**Target:** {item.search_target_id}", ""]
        for source in item.new_sources:
            lines.extend([f"- **{source.id} — {source.title}**", f"  URL: {source.url}"])
        if not item.new_sources:
            lines.append("- No new unique sources were added.")
        lines.extend(
            [
                "",
                f"**Search Duration:** {self._duration(item.search_duration)}",
                "",
                "---",
                "",
                "## 2. Evidence Processing",
                "",
            ]
        )
        if item.processing_result is None:
            lines.extend(["Evidence processing did not complete.", ""])
        else:
            result = item.processing_result
            lines.extend(
                [
                    f"- New claim proposals: {len(result.new_claims)}",
                    f"- Existing claim updates: {len(result.claim_updates)}",
                    f"- New gaps: {len(result.new_gaps)}",
                    f"- Resolved gaps: {len(result.resolved_gap_ids)}",
                    "",
                    f"**Processing Duration:** {self._duration(item.processing_duration or 0.0)}",
                    "",
                ]
            )
        lines.extend(["---", "", "## 3. Ledger Updates", ""])
        lines.extend(self._render_ledger_updates(item))
        lines.extend(["---", "", "## 4. Current Research State", ""])
        lines.extend(self._render_state_summary(item))
        if self._verifier_enabled():
            lines.extend(["---", "", "## 5. Independent Verification", ""])
            lines.extend(self._render_verifications(item))
            decision_section = "## 6. Research Decision"
        else:
            decision_section = "## 5. Research Decision"
        lines.extend(["---", "", decision_section, ""])
        lines.extend(self._render_decision(item))
        lines.extend(["", "---", ""])
        return lines

    def _render_verifications(self, item: LedgerIterationLog) -> list[str]:
        if not item.verifications:
            return ["No eligible claim was independently verified.", ""]
        lines: list[str] = []
        for record in item.verifications:
            result = record.result
            lines.extend(
                [
                    f"### {record.id} — Claim {record.claim_id}",
                    "",
                    f"**Phase:** {record.phase.value}",
                    "",
                    f"**Evidence source IDs:** "
                    f"{', '.join(record.evidence_source_ids) or 'None'}",
                    "",
                    f"**Verdict:** {result.verdict.value}",
                    "",
                    "**Reason**",
                    "",
                    result.reason,
                    "",
                ]
            )
            if result.missing_assumptions:
                lines.extend(["**Missing assumptions**", ""])
                lines.extend(f"- {value}" for value in result.missing_assumptions)
                lines.append("")
            if result.source_quality_concerns:
                lines.extend(["**Source concerns**", ""])
                lines.extend(
                    f"- {value}" for value in result.source_quality_concerns
                )
                lines.append("")
            lines.extend(
                [
                    f"**Counter-search status:** "
                    f"{record.counter_search_status.value}",
                    "",
                ]
            )
            if result.counter_search_query:
                lines.extend(
                    ["**Counter-search query:**", "", f"> {result.counter_search_query}", ""]
                )
            if record.counter_search_source_ids:
                lines.extend(
                    [
                        f"**Counter-search evidence:** "
                        f"{', '.join(record.counter_search_source_ids)}",
                        "",
                    ]
                )
            if record.reconciliation_applied:
                lines.extend(["**Reconciliation**", ""])
                if record.previous_claim_text != record.current_claim_text:
                    lines.extend(
                        [
                            "Claim:",
                            "",
                            f'"{record.previous_claim_text}"',
                            "→",
                            f'"{record.current_claim_text}"',
                            "",
                        ]
                    )
                lines.extend(
                    [
                        f"Confidence: {record.previous_confidence.value} → "
                        f"{record.current_confidence.value}",
                        "",
                        f"Status: {record.previous_status.value} → "
                        f"{record.current_status.value}",
                        "",
                    ]
                )
        return lines

    def _render_ledger_updates(self, item: LedgerIterationLog) -> list[str]:
        if item.ledger_updates is None or item.ledger_snapshot is None:
            return ["No ledger update was completed.", ""]
        lines: list[str] = []
        claim_map = {claim.id: claim for claim in item.ledger_snapshot.claims}
        for change in item.ledger_updates.claim_changes:
            claim = claim_map[change.claim_id]
            heading = "New Claim" if change.change_type == LedgerChangeType.NEW else "Updated Claim"
            lines.extend(
                [
                    f"### {heading} {claim.id}",
                    "",
                    "**Claim**",
                    "",
                    claim.claim,
                    "",
                ]
            )
            for relation in change.added_supporting_evidence:
                lines.append(
                    f"- {relation.source_id} supports ({relation.strength.value.lower()}): "
                    f"{relation.summary}"
                )
            for relation in change.added_contradicting_evidence:
                lines.append(
                    f"- {relation.source_id} contradicts ({relation.strength.value.lower()}): "
                    f"{relation.summary}"
                )
            if not change.added_supporting_evidence and not change.added_contradicting_evidence:
                lines.append("- No new evidence relationship was added.")
            lines.extend([""])
            if change.previous_confidence is not None:
                lines.append(
                    f"**Confidence:** {change.previous_confidence.value} → "
                    f"{change.current_confidence.value}"
                )
                lines.append("")
            else:
                lines.extend([f"**Confidence:** {change.current_confidence.value}", ""])
            if change.previous_status is not None:
                lines.append(
                    f"**Status:** {change.previous_status.value} → {change.current_status.value}"
                )
                lines.append("")
            else:
                lines.extend([f"**Status:** {change.current_status.value}", ""])
        for change in item.ledger_updates.gap_changes:
            action = "New Gap" if change.change_type.value == "NEW" else "Resolved Gap"
            lines.extend([f"### {action} {change.gap_id}", "", change.description, ""])
        if not item.ledger_updates.claim_changes and not item.ledger_updates.gap_changes:
            lines.extend(["No ledger or gap changes were recorded.", ""])
        return lines

    def _render_state_summary(self, item: LedgerIterationLog) -> list[str]:
        ledger = item.ledger_snapshot or EvidenceLedger()
        counts = {status: 0 for status in ClaimStatus}
        for claim in ledger.claims:
            counts[claim.status] += 1
        open_gaps = sum(gap.status == GapStatus.OPEN for gap in item.gaps_snapshot)
        remaining = max(self.max_iterations - item.iteration_number, 0)
        lines = [
            f"- Claims: {len(ledger.claims)}",
            f"- Supported: {counts[ClaimStatus.SUPPORTED]}",
            f"- Weak: {counts[ClaimStatus.WEAK]}",
            f"- Conflicting: {counts[ClaimStatus.CONFLICTING]}",
            f"- Insufficient Evidence: {counts[ClaimStatus.INSUFFICIENT_EVIDENCE]}",
            f"- Open Gaps: {open_gaps}",
            f"- Remaining Searches: {remaining}",
            "",
        ]
        if item.research_plan_snapshot is not None:
            lines.extend(["### Subquestion Progress", ""])
            changes = {
                change.subquestion_id: change
                for change in item.subquestion_status_changes
            }
            for subquestion in item.research_plan_snapshot.subquestions:
                transition = changes.get(subquestion.id)
                status = subquestion.status.value
                if transition is not None:
                    status = (
                        f"{transition.previous_status.value} → "
                        f"{transition.current_status.value}"
                    )
                lines.extend(
                    [
                        f"**{subquestion.id}:** {status}",
                        "",
                        f"Reason: {subquestion.status_reason}",
                        "",
                    ]
                )
            lines.extend(["### Research Plan Status", ""])
            for importance in ("CORE", "SECONDARY"):
                lines.extend([f"**{importance}:**", ""])
                matching = [
                    subquestion
                    for subquestion in item.research_plan_snapshot.subquestions
                    if subquestion.importance.value == importance
                ]
                if matching:
                    lines.extend(
                        f"- {subquestion.id} → {subquestion.status.value} "
                        f"(targeted searches: {subquestion.search_attempts})"
                        for subquestion in matching
                    )
                else:
                    lines.append("- None")
                lines.append("")
            lines.extend([f"**Remaining targeted searches:** {remaining}", ""])
        return lines

    def _render_decision(self, item: LedgerIterationLog) -> list[str]:
        if item.decision is None:
            return ["No research decision was completed for this iteration."]
        decision = item.decision
        lines = [
            "**Decision:** "
            + ("Continue researching." if decision.needs_more_research else "Stop researching."),
            "",
            f"**Origin:** {decision.decision_origin.value}",
            "",
        ]
        if decision.target_type is not None:
            target = decision.target_type.value
            if decision.target_id:
                target += f" {decision.target_id}"
            lines.extend([f"**Target:** {target}", ""])
        lines.extend(["**Why**", "", decision.reason, ""])
        if decision.next_search_query:
            lines.extend(["**Next Search**", "", f"> {decision.next_search_query}", ""])
        if item.stop_reason:
            lines.extend([f"**Stop Reason:** {item.stop_reason}", ""])
        return lines

    def _render_final_decision(self) -> list[str]:
        lines = ["# Final Research Decision", ""]
        if self.status == "Failed":
            lines.extend(
                [
                    "**Research did not complete.**",
                    "",
                    f"**Failure Stage:** {self.failure_stage or 'Unknown'}",
                    "",
                ]
            )
        else:
            lines.extend(
                [
                    f"**Stop Reason:** {self.final_stop_reason or 'not_recorded'}",
                    "",
                ]
            )
        lines.extend(["**Remaining Uncertainty**", ""])
        if self.remaining_gaps:
            lines.extend(f"- {gap}" for gap in self.remaining_gaps)
        else:
            lines.append("- No major remaining uncertainty was identified.")
        lines.extend(["", "---", ""])
        return lines

    def _render_performance(self) -> list[str]:
        search_total = sum(item.search_duration for item in self.iterations)
        processing_total = sum(item.processing_duration or 0.0 for item in self.iterations)
        decision_total = sum(item.decision_duration or 0.0 for item in self.iterations)
        verification_total = sum(item.verification_duration for item in self.iterations)
        lines = [
            "# Performance Summary",
            "",
            "| Component | Calls | Total Time |",
            "|---|---:|---:|",
        ]
        if self.decomposition_attempted:
            lines.append(
                f"| Question Decomposition | 1 | "
                f"{self._duration(self.decomposition_duration or 0.0)} |"
            )
        lines.extend([
            f"| Tavily Search | {len(self.iterations)} | {self._duration(search_total)} |",
            f"| Evidence Processing | {self._processing_calls()} | {self._duration(processing_total)} |",
        ])
        if self._verifier_enabled():
            lines.append(
                f"| Independent Verification | {self._verification_calls()} | "
                f"{self._duration(verification_total)} |"
            )
        lines.extend(
            [
                f"| Research Decision | {self._decision_calls()} | {self._duration(decision_total)} |",
                f"| Report Generation | {self._report_calls()} | {self._duration(self.report_duration or 0.0)} |",
                f"| Total Run | — | {self._duration(self.total_runtime or 0.0)} |",
                "",
            ]
        )
        return lines

    def _render_verifier_diagnostics(self) -> list[str]:
        if not self._verifier_enabled():
            return []
        records = self._verification_records()
        verdicts = {
            verdict: sum(record.result.verdict.value == verdict for record in records)
            for verdict in (
                "VERIFIED",
                "NEEDS_QUALIFICATION",
                "CONTRADICTED",
                "INSUFFICIENT_EVIDENCE",
            )
        }
        statuses = {
            status: sum(record.counter_search_status.value == status for record in records)
            for status in (
                "EXECUTED",
                "BLOCKED_BUDGET",
                "BLOCKED_DUPLICATE",
            )
        }
        confidence_rank = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}
        confidence_decreases = sum(
            record.reconciliation_applied
            and record.previous_confidence is not None
            and record.current_confidence is not None
            and confidence_rank[record.current_confidence.value]
            < confidence_rank[record.previous_confidence.value]
            for record in records
        )
        wording_changes = sum(
            record.reconciliation_applied
            and record.previous_claim_text != record.current_claim_text
            for record in records
        )
        status_changes = sum(
            record.reconciliation_applied
            and record.previous_status != record.current_status
            for record in records
        )
        search_counts = {
            purpose: sum(item.search_purpose.value == purpose for item in self.iterations)
            for purpose in ("GENERAL", "SUBQUESTION", "COUNTERSEARCH")
        }
        requested = sum(record.result.counter_search_needed for record in records)
        lines = [
            "# Verifier Diagnostics",
            "",
            f"- Verification calls: {self._verification_calls()}",
            f"- Claims verified: {len({record.claim_id for record in records})}",
            f"- VERIFIED verdicts: {verdicts['VERIFIED']}",
            f"- NEEDS_QUALIFICATION verdicts: {verdicts['NEEDS_QUALIFICATION']}",
            f"- CONTRADICTED verdicts: {verdicts['CONTRADICTED']}",
            f"- INSUFFICIENT_EVIDENCE verdicts: {verdicts['INSUFFICIENT_EVIDENCE']}",
            f"- Counter-searches requested: {requested}",
            f"- Counter-searches executed: {statuses['EXECUTED']}",
            f"- Counter-searches blocked by budget: {statuses['BLOCKED_BUDGET']}",
            f"- Counter-searches blocked as duplicates: {statuses['BLOCKED_DUPLICATE']}",
            f"- Claims whose wording changed: {wording_changes}",
            f"- Claims whose confidence decreased: {confidence_decreases}",
            f"- Claims whose status changed: {status_changes}",
            f"- Searches allocated to general research: {search_counts['GENERAL']}",
            f"- Searches allocated to subquestions: {search_counts['SUBQUESTION']}",
            f"- Searches allocated to counter-search: {search_counts['COUNTERSEARCH']}",
            "",
        ]
        return lines

    def _verification_records(self) -> list[ClaimVerificationRecord]:
        by_id: dict[str, ClaimVerificationRecord] = {}
        for iteration in self.iterations:
            for record in iteration.verifications:
                by_id[record.id] = record
        return list(by_id.values())

    def _verifier_enabled(self) -> bool:
        return (
            self.verifier_model is not None
            or self.system_version == "evidence-ledger-decomposer-verifier-v1"
        )

    def _iteration(self, iteration_number: int) -> LedgerIterationLog:
        for item in self.iterations:
            if item.iteration_number == iteration_number:
                return item
        raise ValueError(f"No search record exists for iteration {iteration_number}")

    def _processing_calls(self) -> int:
        return sum(item.processing_attempted for item in self.iterations)

    def _decision_calls(self) -> int:
        return sum(item.decision_attempted for item in self.iterations)

    def _report_calls(self) -> int:
        return 1 if self.report_attempted else 0

    def _verification_calls(self) -> int:
        return sum(item.verification_attempts for item in self.iterations)

    def _openai_calls(self) -> int:
        return (
            (1 if self.decomposition_attempted else 0)
            + self._processing_calls()
            + self._verification_calls()
            + self._decision_calls()
            + self._report_calls()
        )

    @staticmethod
    def _duration(seconds: float) -> str:
        return f"{seconds:.2f}s"

    @staticmethod
    def _sanitize_error(error: BaseException) -> str:
        message = str(error).strip() or error.__class__.__name__
        message = re.sub(
            r"(?i)(authorization|api[_ -]?key)(\s*[:=]\s*)\S+",
            r"\1\2[REDACTED]",
            message,
        )
        return re.sub(r"\b(?:sk|tvly)-[A-Za-z0-9_-]+", "[REDACTED]", message)
