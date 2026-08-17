from typing import Iterable

from .models import (
    RequirementState,
    ConsensusState,
    AdmissibilityState,
    AtomicityState,
    FinalityState,
    ReconciliationState,
    ContinuityState,
)


BLOCKING_REQUIREMENT_STATES = {
    RequirementState.UNSATISFIED,
    RequirementState.CONFLICTED,
    RequirementState.OUT_OF_SCOPE,
}

DEFER_REQUIREMENT_STATES = {
    RequirementState.PENDING,
    RequirementState.INDETERMINATE,
}

REVALIDATE_REQUIREMENT_STATES = {
    RequirementState.STALE,
}


def _applicable(states: Iterable[RequirementState]):
    return [state for state in states if state != RequirementState.INAPPLICABLE]


def authority_complete(states: Iterable[RequirementState]) -> bool:
    applicable = _applicable(states)

    if not applicable:
        return True

    return all(state == RequirementState.SATISFIED for state in applicable)


def classify_consensus(
    *,
    threshold_met: bool,
    conflicted: bool = False,
    determinate: bool = True,
) -> ConsensusState:

    if conflicted:
        return ConsensusState.CONFLICTED

    if not determinate:
        return ConsensusState.INDETERMINATE

    if threshold_met:
        return ConsensusState.ACHIEVED

    return ConsensusState.NOT_ACHIEVED


def classify_admissibility(
    requirement_states: Iterable[RequirementState],
    *,
    reconstruction_required: bool = False,
) -> AdmissibilityState:

    states = _applicable(requirement_states)

    if reconstruction_required:
        return AdmissibilityState.RECONSTRUCT

    if any(state in BLOCKING_REQUIREMENT_STATES for state in states):
        return AdmissibilityState.BLOCK

    if any(state in REVALIDATE_REQUIREMENT_STATES for state in states):
        return AdmissibilityState.REVALIDATE

    if any(state in DEFER_REQUIREMENT_STATES for state in states):
        return AdmissibilityState.DEFER

    if all(state == RequirementState.SATISFIED for state in states):
        return AdmissibilityState.ADMIT

    return AdmissibilityState.DEFER


def classify_atomicity(
    required_leg_effects: Iterable[bool | None],
) -> AtomicityState:

    effects = list(required_leg_effects)

    if any(effect is None for effect in effects):
        return AtomicityState.INDETERMINATE

    if not effects:
        return AtomicityState.NO_EFFECT

    satisfied = sum(effect is True for effect in effects)

    if satisfied == 0:
        return AtomicityState.NO_EFFECT

    if satisfied == len(effects):
        return AtomicityState.COMPLETE

    return AtomicityState.PARTIAL


def classify_finality(
    requirement_states: Iterable[RequirementState],
    *,
    reconstruction_required: bool = False,
) -> FinalityState:

    states = _applicable(requirement_states)

    if reconstruction_required:
        return FinalityState.RECONSTRUCTION_REQUIRED

    if any(state == RequirementState.CONFLICTED for state in states):
        return FinalityState.CONFLICTED

    if any(state == RequirementState.STALE for state in states):
        return FinalityState.REVALIDATION_REQUIRED

    if any(state == RequirementState.INDETERMINATE for state in states):
        return FinalityState.INDETERMINATE

    if any(state == RequirementState.PENDING for state in states):
        return FinalityState.PENDING

    if any(
        state in {
            RequirementState.UNSATISFIED,
            RequirementState.OUT_OF_SCOPE,
        }
        for state in states
    ):
        return FinalityState.NOT_FINAL

    if all(state == RequirementState.SATISFIED for state in states):
        return FinalityState.FINAL

    return FinalityState.INDETERMINATE


def classify_reconciliation(
    *,
    material_conflict: bool,
    residual_nonblocking_conflict: bool = False,
    reconstruction_required: bool = False,
    revalidation_required: bool = False,
    evidence_sufficient: bool = True,
    governing_rule_available: bool = True,
) -> ReconciliationState:

    if reconstruction_required:
        return ReconciliationState.RECONSTRUCTION_REQUIRED

    if revalidation_required:
        return ReconciliationState.REVALIDATION_REQUIRED

    if not evidence_sufficient:
        return ReconciliationState.INDETERMINATE

    if material_conflict and not governing_rule_available:
        return ReconciliationState.UNRESOLVED

    if residual_nonblocking_conflict:
        return ReconciliationState.RECONCILED_WITH_RESIDUAL_CONFLICT

    return ReconciliationState.RECONCILED


def classify_continuity(
    *,
    break_event: bool = False,
    reconstruction_occurred: bool = False,
    evidence_sufficient: bool = True,
    degraded_condition: bool = False,
) -> ContinuityState:

    if not evidence_sufficient:
        return ContinuityState.INDETERMINATE

    if reconstruction_occurred:
        return ContinuityState.RECONSTRUCTED

    if break_event:
        return ContinuityState.BROKEN

    if degraded_condition:
        return ContinuityState.DEGRADED

    return ContinuityState.PRESERVED
