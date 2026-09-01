"""Human-readable observability for the prior-guided baseline experiment."""

from __future__ import annotations

from dataclasses import dataclass, field

from research.models import (
    PriorKnowledgeResearchPlan,
    ResearchDimension,
    ResearchDimensionStatusChange,
)
from research.research_logger import ResearchLogger
from research.versions import PRIOR_GUIDED_SYSTEM_VERSION


@dataclass
class CoverageSnapshot:
    iteration_number: int
    dimensions: list[ResearchDimension]
    changes: list[ResearchDimensionStatusChange]
    next_target_dimension_id: str | None
    decision_reason: str


@dataclass
class PriorGuidedResearchLogger(ResearchLogger):
    system_version: str = PRIOR_GUIDED_SYSTEM_VERSION
    prior_knowledge_plan: PriorKnowledgeResearchPlan | None = None
    coverage_snapshots: list[CoverageSnapshot] = field(default_factory=list)
    planning_attempts: int = 0
    planning_duration: float | None = None

    def record_planning_attempt(self) -> None:
        self.planning_attempts += 1

    def record_plan(
        self, plan: PriorKnowledgeResearchPlan, duration: float
    ) -> None:
        self.prior_knowledge_plan = plan.model_copy(deep=True)
        self.planning_duration = duration

    def record_coverage_snapshot(
        self,
        iteration_number: int,
        dimensions: list[ResearchDimension],
        changes: list[ResearchDimensionStatusChange],
        next_target_dimension_id: str | None,
        decision_reason: str,
    ) -> None:
        self.coverage_snapshots.append(
            CoverageSnapshot(
                iteration_number=iteration_number,
                dimensions=[item.model_copy(deep=True) for item in dimensions],
                changes=list(changes),
                next_target_dimension_id=next_target_dimension_id,
                decision_reason=decision_reason,
            )
        )

    def render_markdown(self) -> str:
        lines = self._render_summary()
        lines.extend(self._render_coverage_plan())
        snapshots = {
            item.iteration_number: item for item in self.coverage_snapshots
        }
        for iteration in self.iterations:
            lines.extend(self._render_iteration(iteration))
            snapshot = snapshots.get(iteration.iteration_number)
            if snapshot is not None:
                lines.extend(self._render_coverage_snapshot(snapshot))
        lines.extend(self._render_final_decision())
        lines.extend(self._render_performance())
        return "\n".join(lines).rstrip() + "\n"

    def _render_summary(self) -> list[str]:
        lines = super()._render_summary()
        for index, line in enumerate(lines):
            if line.startswith("**OpenAI Calls:**"):
                lines[index] = (
                    "**OpenAI Calls:** "
                    f"{self._analysis_calls() + self._report_calls() + self.planning_attempts}"
                )
                break
        return lines

    def _render_coverage_plan(self) -> list[str]:
        lines = ["## Prior-Knowledge Coverage Plan", ""]
        if self.prior_knowledge_plan is None:
            return lines + ["Coverage planning did not complete.", "", "---", ""]
        for dimension in self.prior_knowledge_plan.dimensions:
            lines.extend(
                [
                    f"### {dimension.id} — {dimension.title}",
                    "",
                    f"**Importance:** {dimension.importance.value}",
                    "",
                    "**Research question**",
                    "",
                    dimension.research_question,
                    "",
                    "**Why it matters**",
                    "",
                    dimension.why_it_matters,
                    "",
                    "**Evidence needed**",
                    "",
                    dimension.evidence_needed,
                    "",
                    f"**Initial status:** {dimension.status.value}",
                    "",
                ]
            )
        if self.prior_knowledge_plan.synthesis_requirements:
            lines.extend(["### Synthesis requirements", ""])
            lines.extend(
                f"- {item}"
                for item in self.prior_knowledge_plan.synthesis_requirements
            )
            lines.append("")
        lines.extend(["Planner output is planning metadata, not evidence.", "", "---", ""])
        return lines

    @staticmethod
    def _render_coverage_snapshot(snapshot: CoverageSnapshot) -> list[str]:
        lines = [
            f"## Coverage Map After Iteration {snapshot.iteration_number}",
            "",
            "| Dimension | Importance | Status | Searches |",
            "|---|---|---|---:|",
        ]
        lines.extend(
            f"| {item.id} — {item.title} | {item.importance.value} | "
            f"{item.status.value} | {item.search_attempts} |"
            for item in snapshot.dimensions
        )
        lines.extend(["", "**Next search target:** " + (snapshot.next_target_dimension_id or "None"), ""])
        lines.extend(["**Reason:**", "", snapshot.decision_reason, "", "---", ""])
        return lines

    def _render_performance(self) -> list[str]:
        lines = super()._render_performance()
        row_index = next(
            index for index, line in enumerate(lines) if line.startswith("| Tavily Search")
        )
        lines.insert(
            row_index,
            f"| Prior-Knowledge Planning | {self.planning_attempts} | "
            f"{self._duration(self.planning_duration or 0.0)} |",
        )
        return lines
