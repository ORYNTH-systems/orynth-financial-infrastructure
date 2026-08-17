import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
RUNTIME_PARENT = ROOT / "05-distributed-settlement" / "runtime"

if str(RUNTIME_PARENT) not in sys.path:
    sys.path.insert(0, str(RUNTIME_PARENT))

from f2_runtime.engine import (
    authority_complete,
    classify_consensus,
    classify_admissibility,
    classify_atomicity,
    classify_finality,
    classify_reconciliation,
    classify_continuity,
)

from f2_runtime.models import (
    RequirementState,
    ConsensusState,
    AdmissibilityState,
    AtomicityState,
    FinalityState,
    ReconciliationState,
    ContinuityState,
)

from f2_runtime.trace import EvidenceLedger


# ============================================================
# AUTHORITY / CONSENSUS ATTACKS
# ============================================================

def test_consensus_does_not_manufacture_authority():
    consensus = classify_consensus(threshold_met=True)

    authority = authority_complete([
        RequirementState.SATISFIED,
        RequirementState.UNSATISFIED,
    ])

    assert consensus == ConsensusState.ACHIEVED
    assert authority is False


def test_unanimity_does_not_override_missing_authority():
    consensus = classify_consensus(threshold_met=True)

    admission = classify_admissibility([
        RequirementState.UNSATISFIED,
        RequirementState.SATISFIED,
    ])

    assert consensus == ConsensusState.ACHIEVED
    assert admission == AdmissibilityState.BLOCK


def test_conflicted_consensus_never_becomes_achieved():
    assert classify_consensus(
        threshold_met=True,
        conflicted=True,
    ) == ConsensusState.CONFLICTED


def test_indeterminate_consensus_never_becomes_not_achieved():
    assert classify_consensus(
        threshold_met=False,
        determinate=False,
    ) == ConsensusState.INDETERMINATE


# ============================================================
# ADMISSION FAIL-CLOSED ATTACKS
# ============================================================

def test_unknown_admission_requirement_never_admits():
    result = classify_admissibility([
        RequirementState.SATISFIED,
        RequirementState.INDETERMINATE,
    ])

    assert result != AdmissibilityState.ADMIT
    assert result == AdmissibilityState.DEFER


def test_stale_authority_never_admits():
    result = classify_admissibility([
        RequirementState.SATISFIED,
        RequirementState.STALE,
    ])

    assert result == AdmissibilityState.REVALIDATE


def test_out_of_scope_authority_blocks():
    result = classify_admissibility([
        RequirementState.SATISFIED,
        RequirementState.OUT_OF_SCOPE,
    ])

    assert result == AdmissibilityState.BLOCK


def test_reconstruction_requirement_overrides_apparent_satisfaction():
    result = classify_admissibility(
        [
            RequirementState.SATISFIED,
            RequirementState.SATISFIED,
        ],
        reconstruction_required=True,
    )

    assert result == AdmissibilityState.RECONSTRUCT


# ============================================================
# ATOMICITY ATTACKS
# ============================================================

def test_one_completed_leg_cannot_manufacture_atomic_completion():
    assert classify_atomicity(
        [True, False]
    ) == AtomicityState.PARTIAL


def test_unknown_leg_effect_cannot_be_promoted_to_partial_or_complete():
    assert classify_atomicity(
        [True, None]
    ) == AtomicityState.INDETERMINATE


def test_all_false_is_no_effect_not_partial():
    assert classify_atomicity(
        [False, False, False]
    ) == AtomicityState.NO_EFFECT


def test_all_true_is_atomic_complete_only():
    assert classify_atomicity(
        [True, True, True]
    ) == AtomicityState.COMPLETE


# ============================================================
# FINALITY ATTACKS
# ============================================================

def test_atomic_completion_does_not_bypass_pending_finality():
    atomicity = classify_atomicity([True, True])

    finality = classify_finality([
        RequirementState.SATISFIED,
        RequirementState.PENDING,
    ])

    assert atomicity == AtomicityState.COMPLETE
    assert finality == FinalityState.PENDING


def test_conflicted_finality_cannot_be_final():
    assert classify_finality([
        RequirementState.SATISFIED,
        RequirementState.CONFLICTED,
    ]) == FinalityState.CONFLICTED


def test_indeterminate_finality_cannot_be_final():
    assert classify_finality([
        RequirementState.SATISFIED,
        RequirementState.INDETERMINATE,
    ]) == FinalityState.INDETERMINATE


def test_stale_finality_requires_revalidation():
    assert classify_finality([
        RequirementState.SATISFIED,
        RequirementState.STALE,
    ]) == FinalityState.REVALIDATION_REQUIRED


def test_out_of_scope_finality_requirement_is_not_final():
    assert classify_finality([
        RequirementState.SATISFIED,
        RequirementState.OUT_OF_SCOPE,
    ]) == FinalityState.NOT_FINAL


def test_reconstruction_requirement_prevents_finality():
    assert classify_finality(
        [RequirementState.SATISFIED],
        reconstruction_required=True,
    ) == FinalityState.RECONSTRUCTION_REQUIRED


# ============================================================
# RECONCILIATION ATTACKS
# ============================================================

def test_material_conflict_without_rule_remains_unresolved():
    assert classify_reconciliation(
        material_conflict=True,
        governing_rule_available=False,
    ) == ReconciliationState.UNRESOLVED


def test_missing_evidence_is_indeterminate_not_reconciled():
    assert classify_reconciliation(
        material_conflict=True,
        evidence_sufficient=False,
    ) == ReconciliationState.INDETERMINATE


def test_reconstruction_requirement_not_promoted_to_reconciled():
    assert classify_reconciliation(
        material_conflict=True,
        reconstruction_required=True,
    ) == ReconciliationState.RECONSTRUCTION_REQUIRED


def test_revalidation_requirement_not_promoted_to_reconciled():
    assert classify_reconciliation(
        material_conflict=True,
        revalidation_required=True,
    ) == ReconciliationState.REVALIDATION_REQUIRED


def test_residual_conflict_is_preserved_in_result():
    assert classify_reconciliation(
        material_conflict=True,
        residual_nonblocking_conflict=True,
        governing_rule_available=True,
    ) == ReconciliationState.RECONCILED_WITH_RESIDUAL_CONFLICT


# ============================================================
# CONTINUITY ATTACKS
# ============================================================

def test_break_event_cannot_be_reported_preserved():
    assert classify_continuity(
        break_event=True
    ) == ContinuityState.BROKEN


def test_reconstruction_cannot_be_reported_preserved():
    assert classify_continuity(
        break_event=True,
        reconstruction_occurred=True,
    ) == ContinuityState.RECONSTRUCTED


def test_missing_continuity_evidence_cannot_be_preserved():
    assert classify_continuity(
        evidence_sufficient=False,
    ) == ContinuityState.INDETERMINATE


def test_degraded_condition_cannot_be_silently_cleaned():
    assert classify_continuity(
        degraded_condition=True,
    ) == ContinuityState.DEGRADED


def test_reconstruction_precedence_over_break_classification():
    assert classify_continuity(
        break_event=True,
        reconstruction_occurred=True,
        evidence_sufficient=True,
    ) == ContinuityState.RECONSTRUCTED


# ============================================================
# EVIDENCE-TRACE ATTACKS
# ============================================================

def test_exported_trace_is_copy_not_internal_list():
    ledger = EvidenceLedger()

    ledger.append(
        event_type="EXECUTION",
        object_id="LEG-001",
        payload={"effect": "PARTIAL"},
    )

    exported = ledger.export()
    exported.append({
        "sequence": 999,
        "event_type": "FORGED",
        "object_id": "X",
        "payload": {},
    })

    assert len(ledger.events()) == 1


def test_payload_input_is_copied_on_append():
    ledger = EvidenceLedger()

    payload = {"state": "ADMIT"}

    ledger.append(
        event_type="ADMISSION",
        object_id="Q-001",
        payload=payload,
    )

    payload["state"] = "BLOCK"

    assert ledger.events()[0].payload["state"] == "ADMIT"


def test_sequence_monotonicity():
    ledger = EvidenceLedger()

    for i in range(25):
        event = ledger.append(
            event_type="TRACE",
            object_id=f"E-{i:03d}",
        )

        assert event.sequence == i + 1


def test_events_view_cannot_be_appended_to():
    ledger = EvidenceLedger()

    ledger.append(
        event_type="TRACE",
        object_id="E-001",
    )

    view = ledger.events()

    assert isinstance(view, tuple)
    assert not hasattr(view, "append")


# ============================================================
# CROSS-LAYER COLLAPSE ATTACKS
# ============================================================

def test_consensus_plus_authority_still_does_not_force_atomic_completion():
    consensus = classify_consensus(threshold_met=True)

    authority = authority_complete([
        RequirementState.SATISFIED,
        RequirementState.SATISFIED,
    ])

    atomicity = classify_atomicity([True, False])

    assert consensus == ConsensusState.ACHIEVED
    assert authority is True
    assert atomicity == AtomicityState.PARTIAL


def test_admit_plus_atomic_complete_still_does_not_force_finality():
    admission = classify_admissibility([
        RequirementState.SATISFIED,
    ])

    atomicity = classify_atomicity([True, True])

    finality = classify_finality([
        RequirementState.PENDING,
    ])

    assert admission == AdmissibilityState.ADMIT
    assert atomicity == AtomicityState.COMPLETE
    assert finality == FinalityState.PENDING


def test_finality_does_not_force_continuity_preservation():
    finality = classify_finality([
        RequirementState.SATISFIED,
    ])

    continuity = classify_continuity(
        reconstruction_occurred=True,
    )

    assert finality == FinalityState.FINAL
    assert continuity == ContinuityState.RECONSTRUCTED


def test_reconciled_result_does_not_force_continuity_preservation():
    reconciliation = classify_reconciliation(
        material_conflict=False,
    )

    continuity = classify_continuity(
        break_event=True,
    )

    assert reconciliation == ReconciliationState.RECONCILED
    assert continuity == ContinuityState.BROKEN
