from dataclasses import dataclass, asdict
from typing import Any


@dataclass(frozen=True)
class TraceEvent:
    sequence: int
    event_type: str
    object_id: str
    payload: dict[str, Any]


class EvidenceLedger:
    """
    Append-oriented in-memory reference ledger.

    This is NOT claimed to be cryptographically immutable,
    persistent, tamper-proof, or production-grade.
    """

    def __init__(self):
        self._events: list[TraceEvent] = []

    def append(
        self,
        *,
        event_type: str,
        object_id: str,
        payload: dict[str, Any] | None = None,
    ) -> TraceEvent:

        event = TraceEvent(
            sequence=len(self._events) + 1,
            event_type=event_type,
            object_id=object_id,
            payload={} if payload is None else dict(payload),
        )

        self._events.append(event)
        return event

    def events(self) -> tuple[TraceEvent, ...]:
        return tuple(self._events)

    def export(self) -> list[dict[str, Any]]:
        return [asdict(event) for event in self._events]
