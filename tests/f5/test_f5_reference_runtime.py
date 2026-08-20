import importlib.util
from pathlib import Path

RUNTIME_PATH = Path(__file__).parents[2] / "08-digital-asset-custody" / "runtime" / "f5_reference_runtime.py"

spec = importlib.util.spec_from_file_location("f5_reference_runtime", RUNTIME_PATH)
runtime = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runtime)

F5Context = runtime.F5Context
Decision = runtime.Decision
decide = runtime.decide
transition_allowed = runtime.transition_allowed
governance_authority_created_by_capability = runtime.governance_authority_created_by_capability
authority_continuity_after_key_rotation = runtime.authority_continuity_after_key_rotation
authority_restored_after_key_recovery = runtime.authority_restored_after_key_recovery

def base_context(**overrides):
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

def test_f5_po_045_block_prevents_transition():
    ctx = base_context(authority_source_supported=False)
    assert decide(ctx) == Decision.BLOCK
    assert transition_allowed(ctx) is False

def test_f5_po_046_defer_prevents_transition():
    ctx = base_context(threshold_required=True, threshold_satisfied=False)
    assert decide(ctx) == Decision.DEFER
    assert transition_allowed(ctx) is False

def test_f5_po_047_revalidate_does_not_restore_authority():
    ctx = base_context(authority_revalidation_required=True)
    assert decide(ctx) == Decision.REVALIDATE
    assert transition_allowed(ctx) is False

def test_f5_po_048_reauthorize_requires_independent_authority():
    ctx = base_context(authority_reauthorization_required=True)
    assert decide(ctx) == Decision.REAUTHORIZE
    assert transition_allowed(ctx) is False

def test_f5_po_049_key_recovery_does_not_auto_restore_authority():
    assert authority_restored_after_key_recovery(
        authority_independently_reestablished=False
    ) is False

def test_f5_po_050_key_rotation_does_not_auto_preserve_continuity():
    assert authority_continuity_after_key_rotation(
        continuity_independently_established=False
    ) is False

def test_f5_po_051_valid_signature_does_not_override_authority():
    ctx = base_context(
        signature_valid=True,
        authority_source_supported=False
    )
    assert decide(ctx) == Decision.BLOCK
    assert transition_allowed(ctx) is False

def test_f5_po_052_capability_cannot_self_create_authority():
    ctx = base_context(
        capability_available=True,
        key_possessed=True,
        signature_valid=True,
        authority_source_supported=False
    )
    assert governance_authority_created_by_capability(ctx) is False
    assert decide(ctx) == Decision.BLOCK

def test_valid_authority_path_can_be_admitted():
    ctx = base_context()
    assert decide(ctx) == Decision.ADMIT
    assert transition_allowed(ctx) is True

def test_custody_requirement_can_defer_without_denial():
    ctx = base_context(custody_required=True, custody_established=False)
    assert decide(ctx) == Decision.DEFER
    assert transition_allowed(ctx) is False
