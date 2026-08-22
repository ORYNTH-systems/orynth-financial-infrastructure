from .model import (
    ReconciliationClass,
    ReconciliationInput,
    ReconciliationResult,
)


def reconcile(
    data: ReconciliationInput,
) -> ReconciliationResult:

    if data.evidence_conflict:
        return ReconciliationResult(
            ReconciliationClass.FAILED,
            None,
        )

    if not data.provenance_sufficient:
        return ReconciliationResult(
            ReconciliationClass.FAILED,
            None,
        )

    if not data.obligations_consistent:
        return ReconciliationResult(
            ReconciliationClass.FAILED,
            None,
        )

    if not data.resources_consistent:
        return ReconciliationResult(
            ReconciliationClass.FAILED,
            None,
        )

    if not data.evidence_sufficient:
        return ReconciliationResult(
            ReconciliationClass.INDETERMINATE,
            None,
        )

    if not data.dependencies_resolved:
        return ReconciliationResult(
            ReconciliationClass.INDETERMINATE,
            None,
        )

    unique_states = list(
        dict.fromkeys(data.candidate_states)
    )

    if len(unique_states) == 0:
        return ReconciliationResult(
            ReconciliationClass.FAILED,
            None,
        )

    if len(unique_states) > 1:
        return ReconciliationResult(
            ReconciliationClass.INDETERMINATE,
            None,
        )

    return ReconciliationResult(
        ReconciliationClass.RECONCILED,
        unique_states[0],
    )
