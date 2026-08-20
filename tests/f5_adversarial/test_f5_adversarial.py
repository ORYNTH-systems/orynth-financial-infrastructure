import importlib.util
from pathlib import Path

RUNTIME_PATH = Path(__file__).parents[2] / "08-digital-asset-custody" / "runtime" / "f5_reference_runtime.py"

spec = importlib.util.spec_from_file_location("f5_reference_runtime_adv", RUNTIME_PATH)
runtime = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runtime)

F5Context = runtime.F5Context
Decision = runtime.Decision
decide = runtime.decide
transition_allowed = runtime.transition_allowed
governance_authority_created_by_capability = runtime.governance_authority_created_by_capability
authority_continuity_after_key_rotation = runtime.authority_continuity_after_key_rotation
authority_restored_after_key_recovery = runtime.authority_restored_after_key_recovery

def ctx(**overrides):
    data = dict(
        authority_source_supported=True,
        delegated_authority_active=True,
        scope_valid=True,
        temporal_valid=True,
        delegation_attenuated=True,
        key_lifecycle_permits_use=True,
        custody_required=False,
        custody_established=True,
        blocking_custody_conflict=False,
        threshold_required=False,
        threshold_satisfied=True,
        evidence_sufficient=True,
        capability_available=True,
        key_possessed=True,
        signature_valid=True,
        authority_revalidation_required=False,
        authority_reauthorization_required=False,
    )
    data.update(overrides)
    return F5Context(**data)

def test_adv_01_valid_signature_but_expired_authority_blocks():
    c = ctx(temporal_valid=False, signature_valid=True)
    assert decide(c) == Decision.BLOCK
    assert transition_allowed(c) is False

def test_adv_02_key_possession_without_source_authority_blocks():
    c = ctx(key_possessed=True, authority_source_supported=False)
    assert decide(c) == Decision.BLOCK

def test_adv_03_wallet_capability_cannot_self_authorize():
    c = ctx(capability_available=True, authority_source_supported=False)
    assert governance_authority_created_by_capability(c) is False
    assert transition_allowed(c) is False

def test_adv_04_threshold_satisfied_but_revoked_authority_blocks():
    c = ctx(threshold_required=True, threshold_satisfied=True, delegated_authority_active=False)
    assert decide(c) == Decision.BLOCK

def test_adv_05_scope_violation_blocks_even_with_every_crypto_signal():
    c = ctx(scope_valid=False, key_possessed=True, signature_valid=True, threshold_required=True, threshold_satisfied=True)
    assert decide(c) == Decision.BLOCK

def test_adv_06_unattenuated_delegation_blocks():
    c = ctx(delegation_attenuated=False)
    assert decide(c) == Decision.BLOCK

def test_adv_07_compromised_or_disallowed_key_lifecycle_blocks():
    c = ctx(key_lifecycle_permits_use=False)
    assert decide(c) == Decision.BLOCK

def test_adv_08_blocking_custody_conflict_overrides_other_successes():
    c = ctx(blocking_custody_conflict=True)
    assert decide(c) == Decision.BLOCK
    assert transition_allowed(c) is False

def test_adv_09_missing_required_custody_defers():
    c = ctx(custody_required=True, custody_established=False)
    assert decide(c) == Decision.DEFER

def test_adv_10_unsatisfied_threshold_defers_not_admits():
    c = ctx(threshold_required=True, threshold_satisfied=False)
    assert decide(c) == Decision.DEFER

def test_adv_11_insufficient_evidence_defers():
    c = ctx(evidence_sufficient=False)
    assert decide(c) == Decision.DEFER

def test_adv_12_revalidation_preempts_admission():
    c = ctx(authority_revalidation_required=True)
    assert decide(c) == Decision.REVALIDATE
    assert transition_allowed(c) is False

def test_adv_13_reauthorization_preempts_revalidation():
    c = ctx(authority_revalidation_required=True, authority_reauthorization_required=True)
    assert decide(c) == Decision.REAUTHORIZE
    assert transition_allowed(c) is False

def test_adv_14_recovered_key_without_reestablished_authority_is_false():
    assert authority_restored_after_key_recovery(authority_independently_reestablished=False) is False

def test_adv_15_recovered_key_with_independent_reauthorization_is_true():
    assert authority_restored_after_key_recovery(authority_independently_reestablished=True) is True

def test_adv_16_rotated_key_without_continuity_witness_is_false():
    assert authority_continuity_after_key_rotation(continuity_independently_established=False) is False

def test_adv_17_rotated_key_with_continuity_witness_is_true():
    assert authority_continuity_after_key_rotation(continuity_independently_established=True) is True

def test_adv_18_valid_signature_is_irrelevant_when_authority_invalid():
    c = ctx(signature_valid=True, delegated_authority_active=False)
    assert decide(c) == Decision.BLOCK

def test_adv_19_signature_invalidity_does_not_create_authority():
    c = ctx(signature_valid=False, authority_source_supported=False)
    assert governance_authority_created_by_capability(c) is False

def test_adv_20_only_fully_supported_path_admits():
    c = ctx()
    assert decide(c) == Decision.ADMIT
    assert transition_allowed(c) is True
