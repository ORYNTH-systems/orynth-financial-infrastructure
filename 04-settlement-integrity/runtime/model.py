from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Set


class EffectClass(str, Enum):
    NO_EFFECT = "NO-EFFECT"
    PARTIAL = "PARTIAL"
    COMPLETED = "COMPLETED"
    INDETERMINATE = "INDETERMINATE"


class Decision(str, Enum):
    ADMIT = "ADMIT"
    BLOCK = "BLOCK"
    INDETERMINATE = "INDETERMINATE"


class ReconciliationClass(str, Enum):
    RECONCILED = "RECONCILED"
    INDETERMINATE = "RECONCILIATION-INDETERMINATE"
    FAILED = "RECONCILIATION-FAILED"


class ContinuityClass(str, Enum):
    PRESERVED = "PRESERVED"
    DEGRADED = "DEGRADED"
    BROKEN = "BROKEN"
    RECONSTRUCTED = "RECONSTRUCTED"
    INDETERMINATE = "INDETERMINATE"


@dataclass(frozen=True)
class AuthorityContext:
    authorized: bool
    scope_valid: bool
    current: bool = True


@dataclass
class FinancialExecutionEvent:
    event_id: str
    intended_mutations: Set[str]
    known_positive: Set[str] = field(default_factory=set)
    known_negative: Set[str] = field(default_factory=set)
    economically_recognized: Set[str] = field(default_factory=set)
    authority: Optional[AuthorityContext] = None
    parent_event_id: Optional[str] = None
    event_kind: str = "ORIGIN"


@dataclass(frozen=True)
class EffectResult:
    classification: EffectClass
    unresolved: Set[str]


@dataclass(frozen=True)
class AdmissionResult:
    decision: Decision
    reason: str


@dataclass
class EvidenceRecord:
    sequence: int
    record_type: str
    event_id: Optional[str]
    parent_event_id: Optional[str]
    payload: Dict[str, object]


@dataclass
class ReconciliationInput:
    history: List[str]
    evidence_sufficient: bool
    evidence_conflict: bool
    obligations_consistent: bool
    resources_consistent: bool
    dependencies_resolved: bool
    provenance_sufficient: bool
    candidate_states: List[str]


@dataclass(frozen=True)
class ReconciliationResult:
    classification: ReconciliationClass
    state: Optional[str]


@dataclass
class ContinuityInput:
    history: List[str]
    requirement_traces: Dict[str, List[str]]
    reconstructed: bool = False
