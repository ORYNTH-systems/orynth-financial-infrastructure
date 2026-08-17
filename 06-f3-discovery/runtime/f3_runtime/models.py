from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class FinalityRequest:
    execution_complete: bool = False
    effect_occurred: bool = False
    obligation_satisfied: bool = False
    residual_exists: bool = False

    custody_possession: bool = False
    custody_authority_valid: bool = False
    custody_state_valid: bool = False

    atomic_complete: bool = False
    consensus_complete: bool = False
    reconciliation_complete: bool = False

    authority_valid: bool = False
    scope_valid: bool = False
    temporal_valid: bool = False
    evidence_sufficient: bool = False
    finality_conflict: bool = False
    blocking_contradiction: bool = False
    transition_valid: bool = False
    requirement_set_non_vacuous: bool = False


@dataclass
class FinalityResult:
    eligible: bool
    classification: str
    blockers: List[str] = field(default_factory=list)
    historical_finality_preserved: bool = False
    post_finality_contradiction: bool = False
