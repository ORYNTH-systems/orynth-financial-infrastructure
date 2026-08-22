from typing import Optional, Set

from .authority import evaluate_admission
from .boundary import issue_boundary_permit
from .model import (
    AuthorityContext,
    BoundaryPermit,
    FinancialExecutionEvent,
)


def propose_reversal(
    origin: FinancialExecutionEvent,
    event_id: str,
    intended_mutations: Set[str],
    authority: Optional[AuthorityContext],
    eligible: bool,
    reversible: bool,
) -> FinancialExecutionEvent:

    if not eligible:
        raise ValueError("REVERSAL_NOT_ELIGIBLE")

    if not reversible:
        raise ValueError("REVERSAL_NOT_REVERSIBLE")

    if event_id == origin.event_id:
        raise ValueError(
            "REVERSAL_EVENT_ID_MUST_DIFFER_FROM_ORIGIN"
        )

    return FinancialExecutionEvent(
        event_id=event_id,
        intended_mutations=set(intended_mutations),
        authority=authority,
        parent_event_id=origin.event_id,
        event_kind="REVERSAL",
    )


def admit_reversal(
    event: FinancialExecutionEvent,
) -> BoundaryPermit:

    if event.event_kind != "REVERSAL":
        raise ValueError("NOT_A_REVERSAL_EVENT")

    admission = evaluate_admission(event)

    return issue_boundary_permit(
        event,
        admission,
    )
