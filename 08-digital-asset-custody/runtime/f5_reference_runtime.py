from dataclasses import dataclass
from enum import Enum

class Decision(str, Enum):
    ADMIT = "F5-ADMIT"
    BLOCK = "F5-BLOCK"
    DEFER = "F5-DEFER"
    REVALIDATE = "F5-REVALIDATE"
    REAUTHORIZE = "F5-REAUTHORIZE"

@dataclass(frozen=True)
class F5Context:
    authority_source_supported: bool
    delegated_authority_active: bool
    scope_valid: bool
    temporal_valid: bool
    delegation_attenuated: bool
    key_lifecycle_permits_use: bool
    custody_required: bool
    custody_established: bool
    blocking_custody_conflict: bool
    threshold_required: bool
    threshold_satisfied: bool
    evidence_sufficient: bool
    capability_available: bool
    key_possessed: bool
    signature_valid: bool
    authority_revalidation_required: bool = False
    authority_reauthorization_required: bool = False

def decide(ctx: F5Context) -> Decision:
    if ctx.authority_reauthorization_required:
        return Decision.REAUTHORIZE

    if ctx.authority_revalidation_required:
        return Decision.REVALIDATE

    if ctx.blocking_custody_conflict:
        return Decision.BLOCK

    required_authority = (
        ctx.authority_source_supported
        and ctx.delegated_authority_active
        and ctx.scope_valid
        and ctx.temporal_valid
        and ctx.delegation_attenuated
    )

    if not required_authority:
        return Decision.BLOCK

    if not ctx.key_lifecycle_permits_use:
        return Decision.BLOCK

    if ctx.custody_required and not ctx.custody_established:
        return Decision.DEFER

    if ctx.threshold_required and not ctx.threshold_satisfied:
        return Decision.DEFER

    if not ctx.evidence_sufficient:
        return Decision.DEFER

    return Decision.ADMIT

def transition_allowed(ctx: F5Context) -> bool:
    return decide(ctx) == Decision.ADMIT

def governance_authority_created_by_capability(ctx: F5Context) -> bool:
    _ = (ctx.capability_available, ctx.key_possessed, ctx.signature_valid)
    return False

def authority_continuity_after_key_rotation(
    *,
    continuity_independently_established: bool
) -> bool:
    return continuity_independently_established

def authority_restored_after_key_recovery(
    *,
    authority_independently_reestablished: bool
) -> bool:
    return authority_independently_reestablished
