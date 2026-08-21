from dataclasses import dataclass
from enum import Enum
from typing import Tuple

class Decision(str, Enum):
    ADMIT = "F7-ADMIT"
    BLOCK = "F7-BLOCK"
    DEFER = "F7-DEFER"
    REVALIDATE = "F7-REVALIDATE"
    REAUTHORIZE = "F7-REAUTHORIZE"

@dataclass(frozen=True)
class JurisdictionBoundary:
    authority_active: bool = True
    authority_source_supported: bool = True
    applicable: bool = True
    scope_valid: bool = True
    temporal_valid: bool = True
    blocking_restriction: bool = False
    blocking_conflict: bool = False
    evidence_sufficient: bool = True

@dataclass(frozen=True)
class F7Request:
    technical_reach: bool = True
    jurisdictions: Tuple[JurisdictionBoundary, ...] = (JurisdictionBoundary(),)
    delegation_used: bool = False
    delegation_source_valid: bool = True
    delegation_attenuated: bool = True
    evidence_resolved: bool = True
    revalidation_required: bool = False
    operation_preconditions_satisfied: bool = True

def complete_coverage(req: F7Request) -> bool:
    return bool(req.jurisdictions) and all(
        j.authority_active
        and j.authority_source_supported
        and j.applicable
        and j.scope_valid
        and j.temporal_valid
        for j in req.jurisdictions
    )

def partial_coverage(req: F7Request) -> bool:
    if not req.jurisdictions:
        return False
    supported = [
        j.authority_active
        and j.authority_source_supported
        and j.applicable
        and j.scope_valid
        and j.temporal_valid
        for j in req.jurisdictions
    ]
    return any(supported) and not all(supported)

def decide(req: F7Request) -> Decision:
    if req.revalidation_required:
        return Decision.REVALIDATE
    if not req.evidence_resolved:
        return Decision.DEFER
    if not req.jurisdictions:
        return Decision.DEFER
    if any(not j.authority_active for j in req.jurisdictions):
        return Decision.REAUTHORIZE
    if any(not j.authority_source_supported for j in req.jurisdictions):
        return Decision.BLOCK
    if any(not j.applicable for j in req.jurisdictions):
        return Decision.BLOCK
    if any(not j.scope_valid for j in req.jurisdictions):
        return Decision.BLOCK
    if any(not j.temporal_valid for j in req.jurisdictions):
        return Decision.BLOCK
    if req.delegation_used and not req.delegation_source_valid:
        return Decision.BLOCK
    if req.delegation_used and not req.delegation_attenuated:
        return Decision.BLOCK
    if any(j.blocking_restriction for j in req.jurisdictions):
        return Decision.BLOCK
    if any(j.blocking_conflict for j in req.jurisdictions):
        return Decision.BLOCK
    if any(not j.evidence_sufficient for j in req.jurisdictions):
        return Decision.DEFER
    if not complete_coverage(req):
        return Decision.BLOCK
    return Decision.ADMIT

def transition_exists(req: F7Request) -> bool:
    return decide(req) == Decision.ADMIT and req.operation_preconditions_satisfied

def evidence_implies_authority() -> bool:
    return False

def technical_reach_implies_authority() -> bool:
    return False
