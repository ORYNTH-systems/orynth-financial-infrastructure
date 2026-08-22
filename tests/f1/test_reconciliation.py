from f1_runtime.model import (
    ReconciliationClass,
    ReconciliationInput,
)
from f1_runtime.reconciliation import reconcile


def make_input(**overrides):
    values = dict(
        history=["e0"],
        evidence_sufficient=True,
        evidence_conflict=False,
        obligations_consistent=True,
        resources_consistent=True,
        dependencies_resolved=True,
        provenance_sufficient=True,
        candidate_states=["S1"],
    )

    values.update(overrides)

    return ReconciliationInput(**values)


def test_unique_state_reconciles():
    result = reconcile(make_input())

    assert result.classification == ReconciliationClass.RECONCILED
    assert result.state == "S1"


def test_two_candidate_states_are_indeterminate():
    result = reconcile(
        make_input(candidate_states=["S1", "S2"])
    )

    assert result.classification == ReconciliationClass.INDETERMINATE


def test_missing_evidence_is_indeterminate():
    result = reconcile(
        make_input(evidence_sufficient=False)
    )

    assert result.classification == ReconciliationClass.INDETERMINATE


def test_pending_dependency_is_indeterminate():
    result = reconcile(
        make_input(dependencies_resolved=False)
    )

    assert result.classification == ReconciliationClass.INDETERMINATE


def test_conflicting_evidence_fails():
    result = reconcile(
        make_input(evidence_conflict=True)
    )

    assert result.classification == ReconciliationClass.FAILED


def test_missing_provenance_fails():
    result = reconcile(
        make_input(provenance_sufficient=False)
    )

    assert result.classification == ReconciliationClass.FAILED


def test_inconsistent_obligation_fails():
    result = reconcile(
        make_input(obligations_consistent=False)
    )

    assert result.classification == ReconciliationClass.FAILED
