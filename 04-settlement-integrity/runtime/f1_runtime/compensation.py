from typing import Optional, Set

from .authority import evaluate_admission
from .boundary import issue_boundary_permit
from .model import (
    AuthorityContext,
    BoundaryPermit,
    FinancialExecutionEvent,
)


def propose_compensation(
    origin: FinancialExecutionEvent,
    event_id: str,
    intended_mutations: Set[str],
    authority: Optional[AuthorityContext],
) -> FinancialExecutionEvent:

    if event_id == origin.event_id:
        raise ValueError(
            "COMPENSATION_EVENT_ID_MUST_DIFFER_FROM_ORIGIN"
        )

    return FinancialExecutionEvent(
        event_id=event_id,
        intended_mutations=set(intended_mutations),
        authority=authority,
        parent_event_id=origin.event_id,
        event_kind="COMPENSATION",
    )


def admit_compensation(
    event: FinancialExecutionEvent,
) -> BoundaryPermit:

    if event.event_kind != "COMPENSATION":
        raise ValueError("NOT_A_COMPENSATION_EVENT")

    admission = evaluate_admission(event)

    return issue_boundary_permit(
        event,
        admission,
    )
