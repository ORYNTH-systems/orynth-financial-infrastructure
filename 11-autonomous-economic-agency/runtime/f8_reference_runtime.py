from dataclasses import dataclass
from enum import Enum


class Decision(str, Enum):
    ADMIT = "F8-ADMIT"
    BLOCK = "F8-BLOCK"
    DEFER = "F8-DEFER"
    REVALIDATE = "F8-REVALIDATE"
    REAUTHORIZE = "F8-REAUTHORIZE"
    REIDENTIFY = "F8-REIDENTIFY"


@dataclass(frozen=True)
class F8Request:
    capability_available: bool = True
    principal_valid: bool = True
    principal_identity_bound: bool = True
    agent_identity_valid: bool = True
    authority_active: bool = True
    authority_source_supported: bool = True
    authority_scope_valid: bool = True
    authority_temporally_valid: bool = True
    authority_revoked: bool = False
    authority_expired: bool = False
    authority_superseded: bool = False
    authority_invalid: bool = False
    delegation_used: bool = False
    delegation_source_valid: bool = True
    delegation_attenuated: bool = True
    subdelegation_used: bool = False
    subdelegation_source_valid: bool = True
    subdelegation_attenuated: bool = True
    authority_evidence_sufficient: bool = True
    authority_conflict: bool = False
    revalidation_required: bool = False
    reauthorization_required: bool = False
    identity_misbound: bool = False
    identity_unresolved: bool = False
    replacement_detected: bool = False
    replacement_authority_inherited: bool = True
    governance_authorization_supported: bool = True
    technical_control_available: bool = False
    model_output_present: bool = False
    action_evidence_present: bool = False
    prior_execution_success: bool = False
    operation_preconditions_satisfied: bool = True


@dataclass(frozen=True)
class F8Evaluation:
    decision: Decision
    transition_defined: bool
    reason: str


def evaluate(request: F8Request) -> F8Evaluation:
    if request.identity_unresolved or request.identity_misbound:
        return F8Evaluation(Decision.REIDENTIFY, False, "identity resolution required")

    if request.reauthorization_required:
        return F8Evaluation(Decision.REAUTHORIZE, False, "reauthorization required")

    if request.revalidation_required:
        return F8Evaluation(Decision.REVALIDATE, False, "revalidation required")

    if request.authority_conflict:
        return F8Evaluation(Decision.BLOCK, False, "authority conflict")

    if request.authority_revoked:
        return F8Evaluation(Decision.BLOCK, False, "authority revoked")

    if request.authority_expired:
        return F8Evaluation(Decision.BLOCK, False, "authority expired")

    if request.authority_superseded:
        return F8Evaluation(Decision.BLOCK, False, "authority superseded")

    if request.authority_invalid:
        return F8Evaluation(Decision.BLOCK, False, "authority invalid")

    if request.delegation_used:
        if not request.delegation_source_valid:
            return F8Evaluation(Decision.BLOCK, False, "delegation source invalid")
        if not request.delegation_attenuated:
            return F8Evaluation(Decision.BLOCK, False, "delegation nonattenuated")

    if request.subdelegation_used:
        if not request.subdelegation_source_valid:
            return F8Evaluation(Decision.BLOCK, False, "subdelegation source invalid")
        if not request.subdelegation_attenuated:
            return F8Evaluation(Decision.BLOCK, False, "subdelegation nonattenuated")

    if request.replacement_detected and not request.replacement_authority_inherited:
        return F8Evaluation(
            Decision.REAUTHORIZE,
            False,
            "replacement authority inheritance not established",
        )

    required = (
        request.principal_valid,
        request.principal_identity_bound,
        request.agent_identity_valid,
        request.authority_active,
        request.authority_source_supported,
        request.authority_scope_valid,
        request.authority_temporally_valid,
        request.authority_evidence_sufficient,
        request.governance_authorization_supported,
    )

    if not all(required):
        return F8Evaluation(
            Decision.DEFER,
            False,
            "required authority or attribution input unresolved",
        )

    if not request.operation_preconditions_satisfied:
        return F8Evaluation(
            Decision.ADMIT,
            False,
            "admitted but transition preconditions unsatisfied",
        )

    return F8Evaluation(
        Decision.ADMIT,
        True,
        "admitted and transition preconditions satisfied",
    )
