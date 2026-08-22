from .model import (
    AdmissionResult,
    BoundaryPermit,
    Decision,
    FinancialExecutionEvent,
)


def issue_boundary_permit(
    event: FinancialExecutionEvent,
    admission: AdmissionResult,
) -> BoundaryPermit:

    if admission.decision is not Decision.ADMIT:
        return BoundaryPermit(
            permitted=False,
            event_id=event.event_id,
            reason=f"BLOCKED:{admission.reason}",
        )

    return BoundaryPermit(
        permitted=True,
        event_id=event.event_id,
        reason="ADMISSION_VERIFIED",
    )
