import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME = ROOT / "11-autonomous-economic-agency" / "runtime" / "f8_reference_runtime.py"

spec = importlib.util.spec_from_file_location("f8_reference_runtime", RUNTIME)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

Decision = module.Decision
F8Request = module.F8Request
evaluate = module.evaluate


def test_adversarial_001_capability_cannot_self_authorize():
    r = evaluate(F8Request(
        capability_available=True,
        principal_valid=False,
        authority_active=False,
    ))
    assert r.decision != Decision.ADMIT
    assert r.transition_defined is False


def test_adversarial_002_model_output_cannot_authorize():
    r = evaluate(F8Request(
        principal_valid=False,
        authority_active=False,
        model_output_present=True,
    ))
    assert r.decision != Decision.ADMIT


def test_adversarial_003_tool_control_cannot_authorize():
    r = evaluate(F8Request(
        principal_valid=False,
        authority_active=False,
        technical_control_available=True,
    ))
    assert r.decision != Decision.ADMIT


def test_adversarial_004_prior_success_cannot_bootstrap_authority():
    r = evaluate(F8Request(
        principal_valid=False,
        authority_active=False,
        prior_execution_success=True,
    ))
    assert r.decision != Decision.ADMIT


def test_adversarial_005_revoked_authority_blocks_with_capability_available():
    r = evaluate(F8Request(
        capability_available=True,
        authority_revoked=True,
    ))
    assert r.decision == Decision.BLOCK
    assert r.transition_defined is False


def test_adversarial_006_expired_authority_blocks_persistent_operation():
    r = evaluate(F8Request(
        capability_available=True,
        prior_execution_success=True,
        authority_expired=True,
    ))
    assert r.decision == Decision.BLOCK


def test_adversarial_007_superseded_authority_blocks():
    r = evaluate(F8Request(authority_superseded=True))
    assert r.decision == Decision.BLOCK


def test_adversarial_008_invalid_authority_blocks():
    r = evaluate(F8Request(authority_invalid=True))
    assert r.decision == Decision.BLOCK


def test_adversarial_009_nonattenuated_delegation_blocks():
    r = evaluate(F8Request(
        delegation_used=True,
        delegation_attenuated=False,
    ))
    assert r.decision == Decision.BLOCK


def test_adversarial_010_invalid_delegation_source_blocks():
    r = evaluate(F8Request(
        delegation_used=True,
        delegation_source_valid=False,
    ))
    assert r.decision == Decision.BLOCK


def test_adversarial_011_nonattenuated_subdelegation_blocks():
    r = evaluate(F8Request(
        subdelegation_used=True,
        subdelegation_attenuated=False,
    ))
    assert r.decision == Decision.BLOCK


def test_adversarial_012_invalid_subdelegation_source_blocks():
    r = evaluate(F8Request(
        subdelegation_used=True,
        subdelegation_source_valid=False,
    ))
    assert r.decision == Decision.BLOCK


def test_adversarial_013_identity_misbinding_reidentifies():
    r = evaluate(F8Request(identity_misbound=True))
    assert r.decision == Decision.REIDENTIFY
    assert r.transition_defined is False


def test_adversarial_014_identity_unresolved_reidentifies():
    r = evaluate(F8Request(identity_unresolved=True))
    assert r.decision == Decision.REIDENTIFY


def test_adversarial_015_replacement_without_inheritance_reauthorizes():
    r = evaluate(F8Request(
        replacement_detected=True,
        replacement_authority_inherited=False,
    ))
    assert r.decision == Decision.REAUTHORIZE
    assert r.transition_defined is False


def test_adversarial_016_authority_conflict_blocks():
    r = evaluate(F8Request(authority_conflict=True))
    assert r.decision == Decision.BLOCK


def test_adversarial_017_revalidation_is_nonexecuting():
    r = evaluate(F8Request(revalidation_required=True))
    assert r.decision == Decision.REVALIDATE
    assert r.transition_defined is False


def test_adversarial_018_reauthorization_is_nonexecuting():
    r = evaluate(F8Request(reauthorization_required=True))
    assert r.decision == Decision.REAUTHORIZE
    assert r.transition_defined is False


def test_adversarial_019_missing_scope_does_not_admit():
    r = evaluate(F8Request(authority_scope_valid=False))
    assert r.decision != Decision.ADMIT
    assert r.transition_defined is False


def test_adversarial_020_missing_temporal_validity_does_not_admit():
    r = evaluate(F8Request(authority_temporally_valid=False))
    assert r.decision != Decision.ADMIT


def test_adversarial_021_missing_authority_source_does_not_admit():
    r = evaluate(F8Request(authority_source_supported=False))
    assert r.decision != Decision.ADMIT


def test_adversarial_022_missing_authority_evidence_does_not_admit():
    r = evaluate(F8Request(authority_evidence_sufficient=False))
    assert r.decision != Decision.ADMIT


def test_adversarial_023_missing_governance_authorization_does_not_admit():
    r = evaluate(F8Request(governance_authorization_supported=False))
    assert r.decision != Decision.ADMIT


def test_adversarial_024_admit_without_transition_preconditions_stays_nontransitioning():
    r = evaluate(F8Request(operation_preconditions_satisfied=False))
    assert r.decision == Decision.ADMIT
    assert r.transition_defined is False


def test_adversarial_025_full_valid_case_admits_and_transitions():
    r = evaluate(F8Request())
    assert r.decision == Decision.ADMIT
    assert r.transition_defined is True


def test_adversarial_026_technical_control_plus_action_evidence_cannot_replace_authority():
    r = evaluate(F8Request(
        principal_valid=False,
        authority_active=False,
        technical_control_available=True,
        action_evidence_present=True,
    ))
    assert r.decision != Decision.ADMIT


def test_adversarial_027_model_output_plus_prior_success_cannot_replace_authority():
    r = evaluate(F8Request(
        principal_valid=False,
        authority_active=False,
        model_output_present=True,
        prior_execution_success=True,
    ))
    assert r.decision != Decision.ADMIT


def test_adversarial_028_agent_identity_without_principal_does_not_admit():
    r = evaluate(F8Request(
        agent_identity_valid=True,
        principal_valid=False,
    ))
    assert r.decision != Decision.ADMIT


def test_adversarial_029_principal_without_agent_identity_does_not_admit():
    r = evaluate(F8Request(
        principal_valid=True,
        agent_identity_valid=False,
    ))
    assert r.decision != Decision.ADMIT


def test_adversarial_030_principal_binding_without_authority_does_not_admit():
    r = evaluate(F8Request(
        principal_identity_bound=True,
        authority_active=False,
    ))
    assert r.decision != Decision.ADMIT
