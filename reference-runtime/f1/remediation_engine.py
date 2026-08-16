from __future__ import annotations

from .types import (
    CompensationOutcome,
    History,
    RemediationEvent,
    ReversalOutcome,
)


def executable(event: RemediationEvent) -> bool:
    if not event.consequential:
        return True
    return event.admitted


def append_remediation(history: History, event: RemediationEvent) -> History:
    if event.depth < 1:
        raise ValueError("remediation event depth must be >= 1")

    if history.events:
        parent_candidates = {
            e.event_id for e in history.events
        }

        if event.parent_event_id not in parent_candidates:
            raise ValueError("remediation parent does not exist in history")

        parent = next(
            e for e in history.events
            if e.event_id == event.parent_event_id
        )

        if event.depth != parent.depth + 1:
            raise ValueError("remediation depth must be parent depth + 1")

    return history.append(event)


def classify_compensation(
    *,
    target_resolved: bool,
    partial_progress: bool,
    over: bool = False,
    wrong_dimension: bool = False,
    new_divergence: bool = False,
    contradictory: bool = False,
    zero_effect: bool = False,
    indeterminate: bool = False,
) -> CompensationOutcome:

    if indeterminate:
        return CompensationOutcome.COMP_INDETERMINATE

    if contradictory:
        return CompensationOutcome.COMP_CONTRADICTORY

    if new_divergence:
        return CompensationOutcome.COMP_NEW_DIVERGENCE

    if wrong_dimension:
        return CompensationOutcome.COMP_WRONG_DIMENSION

    if over:
        return CompensationOutcome.COMP_OVER

    if zero_effect:
        return CompensationOutcome.COMP_ZERO_EFFECT

    if target_resolved:
        return CompensationOutcome.COMP_EXACT

    if partial_progress:
        return CompensationOutcome.COMP_PARTIAL

    return CompensationOutcome.COMP_ZERO_EFFECT


def classify_reversal(
    *,
    target_resolved: bool,
    partial_progress: bool,
    over: bool = False,
    wrong_object: bool = False,
    stale_target: bool = False,
    non_reversible: bool = False,
    intervening_conflict: bool = False,
    new_divergence: bool = False,
    contradictory: bool = False,
    zero_effect: bool = False,
    indeterminate: bool = False,
) -> ReversalOutcome:

    if indeterminate:
        return ReversalOutcome.REV_INDETERMINATE

    if stale_target:
        return ReversalOutcome.REV_STALE_TARGET

    if non_reversible:
        return ReversalOutcome.REV_NON_REVERSIBLE

    if intervening_conflict:
        return ReversalOutcome.REV_INTERVENING_CONFLICT

    if contradictory:
        return ReversalOutcome.REV_CONTRADICTORY

    if new_divergence:
        return ReversalOutcome.REV_NEW_DIVERGENCE

    if wrong_object:
        return ReversalOutcome.REV_WRONG_OBJECT

    if over:
        return ReversalOutcome.REV_OVER

    if zero_effect:
        return ReversalOutcome.REV_ZERO_EFFECT

    if target_resolved:
        return ReversalOutcome.REV_EXACT

    if partial_progress:
        return ReversalOutcome.REV_PARTIAL

    return ReversalOutcome.REV_ZERO_EFFECT
