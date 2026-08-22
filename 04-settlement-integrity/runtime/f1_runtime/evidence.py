from copy import deepcopy
from typing import List, Optional

from .model import EvidenceRecord


class EvidenceLedger:
    def __init__(self) -> None:
        self._records: List[EvidenceRecord] = []

    def append(
        self,
        record_type: str,
        event_id: Optional[str],
        parent_event_id: Optional[str],
        payload: dict,
    ) -> EvidenceRecord:

        record = EvidenceRecord(
            sequence=len(self._records) + 1,
            record_type=record_type,
            event_id=event_id,
            parent_event_id=parent_event_id,
            payload=deepcopy(payload),
        )

        self._records.append(record)

        return deepcopy(record)

    def records(self) -> List[EvidenceRecord]:
        return deepcopy(self._records)

    def history_for(
        self,
        event_id: str,
    ) -> List[EvidenceRecord]:

        return [
            deepcopy(record)
            for record in self._records
            if (
                record.event_id == event_id
                or record.parent_event_id == event_id
            )
        ]
