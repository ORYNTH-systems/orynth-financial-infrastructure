from f1_runtime.model import (
    ReconciliationClass,
    ReconciliationInput,
)
from f1_runtime.reconciliation import reconcile


def base(**overrides):
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


def test_multiple_candidates_cannot_be_arbitrarily_selected():
    result = reconcile(
        base(candidate_states=["S1", "S2"])
    )

    assert result.classification == ReconciliationClass.INDETERMINATE
    assert result.state is None


def test_missing_provenance_cannot_reconcile():
    result = reconcile(
        base(provenance_sufficient=False)
    )

    assert result.classification == ReconciliationClass.FAILED
    assert result.state is None


def test_missing_evidence_cannot_reconcile_cleanly():
    result = reconcile(
        base(evidence_sufficient=False)
    )

    assert result.classification == ReconciliationClass.INDETERMINATE
    assert result.state is None


def test_conflicting_evidence_cannot_reconcile_cleanly():
    result = reconcile(
        base(evidence_conflict=True)
    )

    assert result.classification == ReconciliationClass.FAILED
    assert result.state is None


def test_unresolved_dependency_cannot_reconcile_cleanly():
    result = reconcile(
        base(dependencies_resolved=False)
    )

    assert result.classification == ReconciliationClass.INDETERMINATE
    assert result.state is None


def test_inconsistent_obligation_cannot_reconcile():
    result = reconcile(
        base(obligations_consistent=False)
    )

    assert result.classification == ReconciliationClass.FAILED
