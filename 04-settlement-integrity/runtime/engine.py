from .compensation import admit_compensation
from .continuity import classify_continuity
from .effect_classifier import classify_effect
from .evidence import EvidenceLedger
from .model import (
    ContinuityInput,
    FinancialExecutionEvent,
    ReconciliationInput,
)
from .reconciliation import reconcile
from .reversal import admit_reversal


class F1Engine:
    def __init__(self):
        self.evidence = EvidenceLedger()

    def classify(self, event: FinancialExecutionEvent):
        result = classify_effect(event)

        self.evidence.append(
            record_type="EFFECT_CLASSIFICATION",
            event_id=event.event_id,
            parent_event_id=event.parent_event_id,
            payload={
                "event_kind": event.event_kind,
                "classification": result.classification.value,
                "unresolved": sorted(result.unresolved),
            },
        )

        return result

    def authorize_compensation(self, event: FinancialExecutionEvent):
        permit = admit_compensation(event)

        self.evidence.append(
            record_type="COMPENSATION_ADMISSION",
            event_id=event.event_id,
            parent_event_id=event.parent_event_id,
            payload={
                "permitted": permit.permitted,
                "reason": permit.reason,
            },
        )

        return permit

    def authorize_reversal(self, event: FinancialExecutionEvent):
        permit = admit_reversal(event)

        self.evidence.append(
            record_type="REVERSAL_ADMISSION",
            event_id=event.event_id,
            parent_event_id=event.parent_event_id,
            payload={
                "permitted": permit.permitted,
                "reason": permit.reason,
            },
        )

        return permit

    def reconcile(self, data: ReconciliationInput):
        result = reconcile(data)

        self.evidence.append(
            record_type="RECONCILIATION",
            event_id=None,
            parent_event_id=None,
            payload={
                "classification": result.classification.value,
                "state": result.state,
                "history": list(data.history),
            },
        )

        return result

    def continuity(self, data: ContinuityInput):
        result = classify_continuity(data)

        self.evidence.append(
            record_type="CONTINUITY_CLASSIFICATION",
            event_id=None,
            parent_event_id=None,
            payload={
                "classification": result.value,
                "history": list(data.history),
            },
        )

        return result
