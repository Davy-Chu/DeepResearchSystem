"""Frozen-reference Evaluator v1.

Reference reports define benchmark scope only. Candidate reports are judged against
frozen atomic rubrics and never against reference wording or conclusions.
"""

from evaluation.v1.models import EVALUATOR_VERSION, EvaluationResult

__all__ = ["EVALUATOR_VERSION", "EvaluationResult"]
