from __future__ import annotations

from .types import ContinuityClass, ReconciliationClass, Residual


def classify_reconciliation(
    *,
    history_explainable: bool,
    evidence_sufficient: bool,
    residuals: list[Residual],
) -> ReconciliationClass:

    if not evidence_sufficient or not history_explainable:
        return ReconciliationClass.INDETERMINATE

    if any(not r.resolved for r in residuals):
        return ReconciliationClass.DIVERGENT

    return ReconciliationClass.RECONCILED


def classify_continuity(
    *,
    continuity_break_demonstrated: bool,
    history_reconstructable: bool,
    function_available: bool,
    evidence_sufficient: bool,
    no_required_break: bool = False,
) -> ContinuityClass:

    if not evidence_sufficient:
        return ContinuityClass.INDETERMINATE

    if continuity_break_demonstrated:
        if history_reconstructable and function_available:
            return ContinuityClass.RECONSTRUCTED

        if function_available:
            return ContinuityClass.FUNCTION_RESTORED_ONLY

        return ContinuityClass.BROKEN

    if no_required_break:
        return ContinuityClass.PRESERVED

    if history_reconstructable:
        return ContinuityClass.HISTORICALLY_RECONCILED

    return ContinuityClass.DEGRADED


def projected_equivalent(
    state_a: dict,
    state_b: dict,
    projection: list[str],
) -> bool:
    return all(state_a.get(k) == state_b.get(k) for k in projection)


def full_current_state_equivalent(state_a: dict, state_b: dict) -> bool:
    return state_a == state_b


def historical_equivalent(history_a: list[str], history_b: list[str]) -> bool:
    return history_a == history_b
