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

def test_absent_authority_reauthorizes_even_when_executable():
    assert decide(F6Request(authority_active=False)) == Decision.REAUTHORIZE

def test_condition_satisfaction_does_not_create_authority():
    assert decide(F6Request(authority_active=False, condition_required=True, condition_satisfied=True)) == Decision.REAUTHORIZE

def test_oracle_validity_does_not_create_authority():
    assert decide(F6Request(authority_active=False, oracle_required=True, oracle_usable=True)) == Decision.REAUTHORIZE

def test_privileged_control_requires_independent_authority():
    assert decide(F6Request(privileged_control=True, privileged_authorized=False)) == Decision.BLOCK

def test_upgrade_requires_independent_authority():
    assert decide(F6Request(upgrade_or_mutation=True, upgrade_authorized=False)) == Decision.BLOCK

def test_blocking_conflict_blocks_execution():
    assert decide(F6Request(blocking_conflict=True)) == Decision.BLOCK

def test_defer_keeps_transition_undefined():
    req = F6Request(evidence_resolved=False)
    assert decide(req) == Decision.DEFER
    assert transition_exists(req) is False

def test_admit_requires_operation_preconditions_for_transition():
    req = F6Request(operation_preconditions_satisfied=False)
    assert decide(req) == Decision.ADMIT
    assert transition_exists(req) is False

def test_execution_evidence_is_not_authority_evidence():
    assert execution_evidence_implies_authority_evidence() is False

def test_contract_state_is_not_authoritative_truth_by_default():
    assert contract_state_is_authoritative_truth() is False
