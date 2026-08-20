import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "09-programmable-finance" / "runtime"))

from f6_reference_runtime import (
    Decision,
    F6Request,
    decide,
    transition_exists,
    execution_evidence_implies_authority_evidence,
    contract_state_is_authoritative_truth,
)

def test_executable_code_without_authority_reauthorizes():
    assert decide(F6Request(capability_available=True, authority_active=False)) == Decision.REAUTHORIZE

def test_deployed_operational_contract_without_authority_reauthorizes():
    assert decide(F6Request(contract_operational=True, authority_active=False)) == Decision.REAUTHORIZE

def test_valid_invocation_without_governance_support_blocks():
    assert decide(F6Request(invocation_valid=True, governance_supported=False)) == Decision.BLOCK

def test_satisfied_condition_cannot_override_revoked_authority():
    assert decide(F6Request(authority_active=False, condition_required=True, condition_satisfied=True)) == Decision.REAUTHORIZE

def test_verified_oracle_cannot_override_absent_authority():
    assert decide(F6Request(authority_active=False, oracle_required=True, oracle_usable=True)) == Decision.REAUTHORIZE

def test_privileged_capability_without_privileged_authorization_blocks():
    assert decide(F6Request(privileged_control=True, privileged_authorized=False)) == Decision.BLOCK

def test_upgrade_capability_without_upgrade_authorization_blocks():
    assert decide(F6Request(upgrade_or_mutation=True, upgrade_authorized=False)) == Decision.BLOCK

def test_out_of_scope_authority_blocks():
    assert decide(F6Request(scope_valid=False)) == Decision.BLOCK

def test_expired_temporal_authority_blocks():
    assert decide(F6Request(temporal_valid=False)) == Decision.BLOCK

def test_nonattenuated_delegation_blocks():
    assert decide(F6Request(delegation_attenuated=False)) == Decision.BLOCK

def test_blocking_conflict_blocks_even_when_everything_else_valid():
    assert decide(F6Request(blocking_conflict=True)) == Decision.BLOCK

def test_unresolved_evidence_defers():
    assert decide(F6Request(evidence_resolved=False)) == Decision.DEFER

def test_revalidation_precedes_ordinary_execution():
    assert decide(F6Request(revalidation_required=True)) == Decision.REVALIDATE

def test_missing_capability_defers_even_with_authority():
    assert decide(F6Request(capability_available=False)) == Decision.DEFER

def test_nonoperational_contract_defers_even_with_authority():
    assert decide(F6Request(contract_operational=False)) == Decision.DEFER

def test_invalid_invocation_blocks():
    assert decide(F6Request(invocation_valid=False)) == Decision.BLOCK

def test_unsatisfied_required_condition_blocks():
    assert decide(F6Request(condition_required=True, condition_satisfied=False)) == Decision.BLOCK

def test_unusable_required_oracle_blocks():
    assert decide(F6Request(oracle_required=True, oracle_usable=False)) == Decision.BLOCK

def test_admit_without_operation_preconditions_has_no_transition():
    req = F6Request(operation_preconditions_satisfied=False)
    assert decide(req) == Decision.ADMIT
    assert transition_exists(req) is False

def test_execution_and_contract_state_do_not_self_certify_authority_or_truth():
    assert execution_evidence_implies_authority_evidence() is False
    assert contract_state_is_authoritative_truth() is False
