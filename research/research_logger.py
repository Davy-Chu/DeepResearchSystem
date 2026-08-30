"""Human-readable, passive observability for a research run."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from time import perf_counter

from research.models import FinalReport, IterationAnalysis, ResearchState, Source


@dataclass
class IterationLog:
    iteration_number: int
    search_query: str
    query_reason: str
    results_returned: int
    new_sources: list[Source]
    search_duration: float
    analysis: IterationAnalysis | None = None
    analysis_duration: float | None = None
    continue_research: bool | None = None
    decision_reason: str | None = None
    next_search_query: str | None = None
    stop_reason: str | None = None


@dataclass
class ResearchLogger:
    question: str
    model: str
    max_iterations: int
    search_provider: str = "Tavily"
    system_version: str = "baseline-zero"
    iterations: list[IterationLog] = field(default_factory=list)
    start_time: datetime | None = None
    end_time: datetime | None = None
    total_runtime: float | None = None
    report_duration: float | None = None
    final_stop_reason: str | None = None
    remaining_gaps: list[str] = field(default_factory=list)
    status: str = "Not started"
    failure_stage: str | None = None
    error_message: str | None = None
    _start_counter: float | None = field(default=None, repr=False)

    def start_run(self) -> None:
        self.start_time = datetime.now().astimezone()
        self._start_counter = perf_counter()
        self.status = "Running"

    def record_search(
        self,
        iteration_number: int,
        search_query: str,
        query_reason: str,
        results_returned: int,
        new_sources: list[Source],
        duration: float,
    ) -> None:
        self.iterations.append(
            IterationLog(
                iteration_number=iteration_number,
                search_query=search_query,
                query_reason=query_reason,
                results_returned=results_returned,
                new_sources=list(new_sources),
                search_duration=duration,
            )
        )

    def record_analysis(
        self, iteration_number: int, analysis: IterationAnalysis, duration: float
    ) -> None:
        item = self._iteration(iteration_number)
        item.analysis = analysis
        item.analysis_duration = duration

    def record_decision(
        self,
        iteration_number: int,
        continue_research: bool,
        reason: str,
        next_search_query: str | None = None,
        stop_reason: str | None = None,
    ) -> None:
        item = self._iteration(iteration_number)
        item.continue_research = continue_research
        item.decision_reason = reason
        item.next_search_query = next_search_query
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
        self.total_runtime = (
            total_runtime
            if total_runtime is not None
            else self.current_runtime()
        )
        self.status = "Failed"
        self.failure_stage = stage
        self.error_message = self._sanitize_error(error)

    def record_recovered_state(
        self, state: ResearchState, report: FinalReport
    ) -> None:
        """Add final state metadata while preserving the failed status and stage."""
        self.final_stop_reason = state.stop_reason
        self.remaining_gaps = list(report.remaining_gaps)

    def current_runtime(self) -> float:
        if self._start_counter is None:
            return 0.0
        return perf_counter() - self._start_counter

    def render_markdown(self) -> str:
        lines = self._render_summary()
        for iteration in self.iterations:
            lines.extend(self._render_iteration(iteration))
        lines.extend(self._render_final_decision())
        lines.extend(self._render_performance())
        return "\n".join(lines).rstrip() + "\n"

    def save(self, output_dir: Path) -> Path:
        output_dir.mkdir(parents=True, exist_ok=True)
        path = output_dir / "research_log.md"
        path.write_text(self.render_markdown(), encoding="utf-8")
        return path

    def _iteration(self, iteration_number: int) -> IterationLog:
        for item in self.iterations:
            if item.iteration_number == iteration_number:
                return item
        raise ValueError(f"No search record exists for iteration {iteration_number}")

    def _render_summary(self) -> list[str]:
        unique_source_ids = {
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
                f"**Unique Sources:** {len(unique_source_ids)}",
                "",
                f"**OpenAI Calls:** {self._analysis_calls() + self._report_calls()}",
                "",
                f"**Tavily Calls:** {len(self.iterations)}",
                "",
            ]
        )
        if self.start_time:
            lines.extend([f"**Started:** {self.start_time.isoformat(timespec='seconds')}", ""])
        if self.end_time:
            lines.extend([f"**Ended:** {self.end_time.isoformat(timespec='seconds')}", ""])
        if self.total_runtime is not None:
            lines.extend([f"**Total Runtime:** {self._duration(self.total_runtime)}", ""])
        lines.extend(["---", ""])
        return lines

    def _render_iteration(self, item: IterationLog) -> list[str]:
        lines = [
            f"# Iteration {item.iteration_number}",
            "",
            "## 1. Search",
            "",
            "**Query**",
            "",
            f"> {item.search_query}",
            "",
            "**Why this query**",
            "",
            item.query_reason,
            "",
            "**Results**",
            "",
            f"{item.results_returned} result{'s' if item.results_returned != 1 else ''} retrieved.",
            "",
            f"{len(item.new_sources)} new unique source{'s' if len(item.new_sources) != 1 else ''} added.",
            "",
            "### Sources",
            "",
        ]
        if item.new_sources:
            for source in item.new_sources:
                lines.extend(
                    [f"- **{source.id} — {source.title}**", f"  URL: {source.url}"]
                )
        else:
            lines.append("No new unique sources were added.")
        lines.extend(
            [
                "",
                f"**Search Duration:** {self._duration(item.search_duration)}",
                "",
                "---",
                "",
                "## 2. Evidence Analysis",
                "",
            ]
        )
        if item.analysis is None:
            lines.extend(["Analysis did not complete for this iteration.", ""])
        else:
            lines.extend(self._render_analysis(item.analysis))
            if item.analysis_duration is not None:
                lines.extend(
                    [f"**Analysis Duration:** {self._duration(item.analysis_duration)}", ""]
                )
        lines.extend(["---", "", "## 3. Research Decision", ""])
        if item.continue_research is None:
            lines.append("No research decision was completed for this iteration.")
        elif item.continue_research:
            lines.extend(
                [
                    "**Decision:** Continue researching",
                    "",
                    "**Why**",
                    "",
                    item.decision_reason or "No decision reason was recorded.",
                    "",
                    "**Next Search**",
                    "",
                    f"> {item.next_search_query}",
                ]
            )
        else:
            lines.extend(
                [
                    "**Decision:** Stop researching",
                    "",
                    "**Why**",
                    "",
                    self._decision_explanation(item),
                ]
            )
            if item.stop_reason:
                lines.extend(["", f"**Stop Reason:** {item.stop_reason}"])
        lines.extend(["", "---", ""])
        return lines

    def _render_analysis(self, analysis: IterationAnalysis) -> list[str]:
        lines = ["### What We Learned", ""]
        if analysis.findings:
            for number, finding in enumerate(analysis.findings, start=1):
                lines.extend(
                    [
                        f"#### Finding {number}",
                        "",
                        "**Claim**",
                        "",
                        finding.claim,
                        "",
                        f"**Confidence:** {finding.confidence.value.title()}",
                        "",
                        "**Why this confidence level**",
                        "",
                        finding.confidence_reason,
                        "",
                        "**Evidence**",
                        "",
                    ]
                )
                if finding.evidence:
                    for evidence in finding.evidence:
                        citations = " ".join(f"[{source_id}]" for source_id in evidence.source_ids)
                        lines.append(f"- {evidence.summary} {citations}".rstrip())
                else:
                    lines.append("- No supporting evidence was established.")
                lines.append("")
        else:
            lines.extend(["No evidence-backed findings were established.", ""])

        lines.extend(["### Conflicts Found", ""])
        if analysis.conflicts:
            for conflict in analysis.conflicts:
                citations = " ".join(f"[{source_id}]" for source_id in conflict.source_ids)
                lines.append(f"- {conflict.description} {citations}".rstrip())
        else:
            lines.append("No meaningful conflicts were identified in this iteration.")

        lines.extend(["", "### Important Gaps", ""])
        if analysis.unresolved_questions:
            lines.extend(f"- {gap}" for gap in analysis.unresolved_questions)
        else:
            lines.append("No major unanswered gaps were identified.")
        lines.append("")
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
                    f"**Completed Iterations:** {self._completed_iterations()}",
                    "",
                ]
            )
            if self.remaining_gaps:
                lines.extend(["**Remaining Uncertainty**", ""])
                lines.extend(f"- {gap}" for gap in self.remaining_gaps)
                lines.append("")
        else:
            lines.extend(
                [
                    "**Research Stopped Because**",
                    "",
                    self._final_stop_explanation(),
                    "",
                    f"**Stop Reason:** {self.final_stop_reason or 'not_recorded'}",
                    "",
                    f"**Searches Performed:** {len(self.iterations)}",
                    "",
                    f"**Unique Sources:** {self._unique_sources()}",
                    "",
                    "**Remaining Uncertainty**",
                    "",
                ]
            )
            if self.remaining_gaps:
                lines.extend(f"- {gap}" for gap in self.remaining_gaps)
            else:
                lines.append("- No major remaining uncertainty was identified.")
            lines.append("")
        lines.extend(["---", ""])
        return lines

    def _render_performance(self) -> list[str]:
        search_total = sum(item.search_duration for item in self.iterations)
        analysis_durations = [
            item.analysis_duration
            for item in self.iterations
            if item.analysis_duration is not None
        ]
        report_time = self.report_duration or 0.0
        total_time = self.total_runtime or 0.0
        return [
            "# Performance Summary",
            "",
            "| Component | Calls | Total Time |",
            "|---|---:|---:|",
            f"| Tavily Search | {len(self.iterations)} | {self._duration(search_total)} |",
            f"| OpenAI Analysis | {len(analysis_durations)} | {self._duration(sum(analysis_durations))} |",
            f"| Report Generation | {self._report_calls()} | {self._duration(report_time)} |",
            f"| Total Run | — | {self._duration(total_time)} |",
            "",
        ]

    def _decision_explanation(self, item: IterationLog) -> str:
        explanations = {
            "max_iterations": "The runner reached the maximum research iteration budget.",
            "duplicate_query": "The proposed next query duplicated a query already executed.",
            "no_search_results": "No usable new sources were retrieved and no further query was selected.",
        }
        if item.stop_reason in explanations:
            analyzer_reason = item.decision_reason or "No analyzer reason was recorded."
            return f"{explanations[item.stop_reason]} Analyzer assessment: {analyzer_reason}"
        return item.decision_reason or "No decision reason was recorded."

    def _final_stop_explanation(self) -> str:
        explanations = {
            "sufficient_evidence": "The analyzer determined that the important parts of the question could be answered responsibly.",
            "max_iterations": "The runner reached the maximum research iteration budget.",
            "duplicate_query": "The proposed next query duplicated a query already executed, so the runner prevented a loop.",
            "no_search_results": "No usable new sources were retrieved and no further meaningful query was selected.",
        }
        return explanations.get(
            self.final_stop_reason or "", "The run ended without a recorded stop explanation."
        )

    def _analysis_calls(self) -> int:
        return sum(item.analysis is not None for item in self.iterations)

    def _report_calls(self) -> int:
        return 1 if self.report_duration is not None else 0

    def _completed_iterations(self) -> int:
        return sum(item.continue_research is not None for item in self.iterations)

    def _unique_sources(self) -> int:
        return len(
            {source.id for iteration in self.iterations for source in iteration.new_sources}
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
        message = re.sub(r"\b(?:sk|tvly)-[A-Za-z0-9_-]+", "[REDACTED]", message)
        return message
