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


def test_f8_po_063_capability_does_not_create_authority():
    r = evaluate(F8Request(capability_available=True, principal_valid=False, authority_active=False))
    assert r.decision != Decision.ADMIT
    assert r.transition_defined is False


def test_f8_po_064_requires_principal_and_binding():
    assert evaluate(F8Request(principal_valid=False)).decision != Decision.ADMIT
    assert evaluate(F8Request(principal_identity_bound=False)).decision != Decision.ADMIT


def test_f8_po_065_validates_agent_identity_separately():
    r = evaluate(F8Request(agent_identity_valid=False))
    assert r.decision != Decision.ADMIT


def test_f8_po_066_validates_source_scope_time_and_revocation():
    cases = [
        F8Request(authority_source_supported=False),
        F8Request(authority_scope_valid=False),
        F8Request(authority_temporally_valid=False),
        F8Request(authority_revoked=True),
    ]
    for case in cases:
        assert evaluate(case).decision != Decision.ADMIT


def test_f8_po_067_validates_delegation_and_subdelegation_attenuation():
    assert evaluate(F8Request(delegation_used=True, delegation_attenuated=False)).decision == Decision.BLOCK
    assert evaluate(F8Request(subdelegation_used=True, subdelegation_attenuated=False)).decision == Decision.BLOCK


def test_f8_po_068_detects_identity_and_replacement_defects():
    assert evaluate(F8Request(identity_misbound=True)).decision == Decision.REIDENTIFY
    assert evaluate(
        F8Request(replacement_detected=True, replacement_authority_inherited=False)
    ).decision == Decision.REAUTHORIZE


def test_f8_po_069_exposes_all_six_decision_outcomes():
    outcomes = {
        evaluate(F8Request()).decision,
        evaluate(F8Request(authority_revoked=True)).decision,
        evaluate(F8Request(principal_valid=False)).decision,
        evaluate(F8Request(revalidation_required=True)).decision,
        evaluate(F8Request(reauthorization_required=True)).decision,
        evaluate(F8Request(identity_unresolved=True)).decision,
    }

    assert outcomes == {
        Decision.ADMIT,
        Decision.BLOCK,
        Decision.DEFER,
        Decision.REVALIDATE,
        Decision.REAUTHORIZE,
        Decision.REIDENTIFY,
    }


def test_f8_po_070_transition_only_after_admit_and_preconditions():
    r1 = evaluate(F8Request())
    r2 = evaluate(F8Request(operation_preconditions_satisfied=False))
    r3 = evaluate(F8Request(authority_revoked=True))

    assert r1.decision == Decision.ADMIT and r1.transition_defined is True
    assert r2.decision == Decision.ADMIT and r2.transition_defined is False
    assert r3.decision != Decision.ADMIT and r3.transition_defined is False


def test_f8_po_071_no_authority_inference_from_technical_surfaces():
    r = evaluate(
        F8Request(
            principal_valid=False,
            authority_active=False,
            technical_control_available=True,
            model_output_present=True,
            action_evidence_present=True,
            prior_execution_success=True,
        )
    )
    assert r.decision != Decision.ADMIT
    assert r.transition_defined is False


def test_f8_po_072_persistent_operation_rechecks_current_authority():
    r = evaluate(
        F8Request(
            capability_available=True,
            prior_execution_success=True,
            authority_expired=True,
        )
    )
    assert r.decision == Decision.BLOCK
    assert r.transition_defined is False
