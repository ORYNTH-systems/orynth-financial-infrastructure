from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class DimensionType(str, Enum):
    QUANTITATIVE = "QUANTITATIVE"
    RELATIONAL = "RELATIONAL"
    DISCRETE_STATE = "DISCRETE_STATE"
    SET_VALUED = "SET_VALUED"
    GRAPH_STATE = "GRAPH_STATE"
    ORDERED_SEQUENCE = "ORDERED_SEQUENCE"
    OPAQUE_TYPED = "OPAQUE_TYPED"


class DimensionOutcome(str, Enum):
    NO_EFFECT = "NO_EFFECT"
    PARTIAL_MATCH = "PARTIAL_MATCH"
    FULL_MATCH = "FULL_MATCH"
    OVER_EFFECT = "OVER_EFFECT"
    CONTRADICTORY_EFFECT = "CONTRADICTORY_EFFECT"
    INDETERMINATE = "INDETERMINATE"


class GlobalEffectClass(str, Enum):
    E_NO_EFFECT = "E_NO_EFFECT"
    E_PARTIAL = "E_PARTIAL"
    E_COMPLETED = "E_COMPLETED"
    E_MIXED = "E_MIXED"
    E_INDETERMINATE = "E_INDETERMINATE"


class CompensationOutcome(str, Enum):
    COMP_EXACT = "COMP_EXACT"
    COMP_PARTIAL = "COMP_PARTIAL"
    COMP_OVER = "COMP_OVER"
    COMP_WRONG_DIMENSION = "COMP_WRONG_DIMENSION"
    COMP_NEW_DIVERGENCE = "COMP_NEW_DIVERGENCE"
    COMP_CONTRADICTORY = "COMP_CONTRADICTORY"
    COMP_ZERO_EFFECT = "COMP_ZERO_EFFECT"
    COMP_INDETERMINATE = "COMP_INDETERMINATE"


class ReversalOutcome(str, Enum):
    REV_EXACT = "REV_EXACT"
    REV_PARTIAL = "REV_PARTIAL"
    REV_OVER = "REV_OVER"
    REV_WRONG_OBJECT = "REV_WRONG_OBJECT"
    REV_STALE_TARGET = "REV_STALE_TARGET"
    REV_NON_REVERSIBLE = "REV_NON_REVERSIBLE"
    REV_INTERVENING_CONFLICT = "REV_INTERVENING_CONFLICT"
    REV_NEW_DIVERGENCE = "REV_NEW_DIVERGENCE"
    REV_CONTRADICTORY = "REV_CONTRADICTORY"
    REV_ZERO_EFFECT = "REV_ZERO_EFFECT"
    REV_INDETERMINATE = "REV_INDETERMINATE"


class ReconciliationClass(str, Enum):
    RECONCILED = "RECONCILED"
    DIVERGENT = "DIVERGENT"
    INDETERMINATE = "INDETERMINATE"


class ContinuityClass(str, Enum):
    UNASSESSED = "F1_CONTINUITY_UNASSESSED"
    PRESERVED = "F1_CONTINUITY_PRESERVED"
    DEGRADED = "F1_CONTINUITY_DEGRADED"
    BROKEN = "F1_CONTINUITY_BROKEN"
    RECONSTRUCTED = "F1_CONTINUITY_RECONSTRUCTED"
    FUNCTION_RESTORED_ONLY = "F1_FUNCTION_RESTORED_ONLY"
    HISTORICALLY_RECONCILED = "F1_HISTORICALLY_RECONCILED"
    INDETERMINATE = "F1_CONTINUITY_INDETERMINATE"


@dataclass(frozen=True)
class EffectDimension:
    dimension_id: str
    dimension_type: DimensionType
    intended: Any
    observed: Any
    required: bool = True
    evidence_present: bool = True


@dataclass(frozen=True)
class DimensionComparison:
    dimension_id: str
    outcome: DimensionOutcome
    detail: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class EffectSignature:
    comparisons: List[DimensionComparison]
    global_class: GlobalEffectClass


@dataclass(frozen=True)
class Residual:
    dimension_id: str
    resolved: bool
    detail: Any


@dataclass(frozen=True)
class RemediationEvent:
    event_id: str
    event_type: str
    parent_event_id: Optional[str]
    depth: int
    admitted: bool
    consequential: bool
    effect_class: Optional[str] = None


@dataclass
class History:
    events: List[RemediationEvent] = field(default_factory=list)

    def append(self, event: RemediationEvent) -> "History":
        return History(events=[*self.events, event])
