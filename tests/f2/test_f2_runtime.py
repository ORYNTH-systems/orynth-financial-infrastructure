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


def test_authority_complete_true():
    assert authority_complete([
        RequirementState.SATISFIED,
        RequirementState.SATISFIED,
    ]) is True


def test_authority_complete_false():
    assert authority_complete([
        RequirementState.SATISFIED,
        RequirementState.UNSATISFIED,
    ]) is False


def test_inapplicable_does_not_block_authority():
    assert authority_complete([
        RequirementState.SATISFIED,
        RequirementState.INAPPLICABLE,
    ]) is True


def test_consensus_achieved():
    assert classify_consensus(
        threshold_met=True
    ) == ConsensusState.ACHIEVED


def test_consensus_conflicted():
    assert classify_consensus(
        threshold_met=True,
        conflicted=True
    ) == ConsensusState.CONFLICTED


def test_consensus_indeterminate():
    assert classify_consensus(
        threshold_met=False,
        determinate=False
    ) == ConsensusState.INDETERMINATE


def test_admit_only_when_all_requirements_satisfied():
    assert classify_admissibility([
        RequirementState.SATISFIED,
        RequirementState.SATISFIED,
    ]) == AdmissibilityState.ADMIT


def test_unsatisfied_blocks_admission():
    assert classify_admissibility([
        RequirementState.SATISFIED,
        RequirementState.UNSATISFIED,
    ]) == AdmissibilityState.BLOCK


def test_indeterminate_defers_admission():
    assert classify_admissibility([
        RequirementState.SATISFIED,
        RequirementState.INDETERMINATE,
    ]) == AdmissibilityState.DEFER


def test_stale_requires_revalidation():
    assert classify_admissibility([
        RequirementState.SATISFIED,
        RequirementState.STALE,
    ]) == AdmissibilityState.REVALIDATE


def test_reconstruction_precedes_admission():
    assert classify_admissibility(
        [RequirementState.SATISFIED],
        reconstruction_required=True
    ) == AdmissibilityState.RECONSTRUCT


def test_atomic_no_effect():
    assert classify_atomicity(
        [False, False]
    ) == AtomicityState.NO_EFFECT


def test_atomic_partial():
    assert classify_atomicity(
        [True, False]
    ) == AtomicityState.PARTIAL


def test_atomic_complete():
    assert classify_atomicity(
        [True, True]
    ) == AtomicityState.COMPLETE


def test_atomic_indeterminate():
    assert classify_atomicity(
        [True, None]
    ) == AtomicityState.INDETERMINATE


def test_finality_final():
    assert classify_finality([
        RequirementState.SATISFIED,
        RequirementState.SATISFIED,
    ]) == FinalityState.FINAL


def test_finality_pending():
    assert classify_finality([
        RequirementState.SATISFIED,
        RequirementState.PENDING,
    ]) == FinalityState.PENDING


def test_finality_conflicted():
    assert classify_finality([
        RequirementState.SATISFIED,
        RequirementState.CONFLICTED,
    ]) == FinalityState.CONFLICTED


def test_finality_indeterminate():
    assert classify_finality([
        RequirementState.SATISFIED,
        RequirementState.INDETERMINATE,
    ]) == FinalityState.INDETERMINATE


def test_finality_stale_requires_revalidation():
    assert classify_finality([
        RequirementState.SATISFIED,
        RequirementState.STALE,
    ]) == FinalityState.REVALIDATION_REQUIRED


def test_reconciliation_clean():
    assert classify_reconciliation(
        material_conflict=False
    ) == ReconciliationState.RECONCILED


def test_reconciliation_unresolved_conflict():
    assert classify_reconciliation(
        material_conflict=True,
        governing_rule_available=False,
    ) == ReconciliationState.UNRESOLVED


def test_reconciliation_indeterminate():
    assert classify_reconciliation(
        material_conflict=True,
        evidence_sufficient=False,
    ) == ReconciliationState.INDETERMINATE


def test_reconciliation_with_residual_conflict():
    assert classify_reconciliation(
        material_conflict=True,
        residual_nonblocking_conflict=True,
    ) == ReconciliationState.RECONCILED_WITH_RESIDUAL_CONFLICT


def test_continuity_preserved():
    assert classify_continuity() == ContinuityState.PRESERVED


def test_continuity_degraded():
    assert classify_continuity(
        degraded_condition=True
    ) == ContinuityState.DEGRADED


def test_continuity_broken():
    assert classify_continuity(
        break_event=True
    ) == ContinuityState.BROKEN


def test_continuity_reconstructed():
    assert classify_continuity(
        break_event=True,
        reconstruction_occurred=True,
    ) == ContinuityState.RECONSTRUCTED


def test_continuity_indeterminate():
    assert classify_continuity(
        evidence_sufficient=False
    ) == ContinuityState.INDETERMINATE


def test_evidence_ledger_append_order():
    ledger = EvidenceLedger()

    e1 = ledger.append(
        event_type="ADMISSION",
        object_id="Q-001",
        payload={"state": "ADMIT"},
    )

    e2 = ledger.append(
        event_type="EXECUTION",
        object_id="LEG-001",
        payload={"effect": "COMPLETED"},
    )

    assert e1.sequence == 1
    assert e2.sequence == 2
    assert len(ledger.events()) == 2


def test_evidence_ledger_returns_immutable_tuple():
    ledger = EvidenceLedger()

    ledger.append(
        event_type="OBSERVATION",
        object_id="O-001",
    )

    assert isinstance(ledger.events(), tuple)
