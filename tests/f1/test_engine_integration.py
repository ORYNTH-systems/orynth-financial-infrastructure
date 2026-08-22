from f1_runtime.compensation import propose_compensation
from f1_runtime.engine import F1Engine
from f1_runtime.model import (
    AuthorityContext,
    ContinuityClass,
    ContinuityInput,
    EffectClass,
    FinancialExecutionEvent,
    ReconciliationClass,
    ReconciliationInput,
)


def test_engine_records_effect_classification():
    engine = F1Engine()

    event = FinancialExecutionEvent(
        event_id="e0",
        intended_mutations={"A", "B"},
        known_positive={"A"},
        known_negative={"B"},
        economically_recognized={"A"},
    )

    result = engine.classify(event)

    assert result.classification == EffectClass.PARTIAL
    assert engine.evidence.records()[0].event_id == "e0"


def test_engine_records_blocked_compensation():
    engine = F1Engine()

    origin = FinancialExecutionEvent(
        event_id="e0",
        intended_mutations={"A"},
    )

    compensation = propose_compensation(
        origin,
        "ec",
        {"C"},
        None,
    )

    permit = engine.admit_compensation(compensation)

    assert permit.permitted is False
    assert engine.evidence.records()[-1].event_id == "ec"


def test_engine_records_reconciliation_history():
    engine = F1Engine()

    result = engine.reconcile(
        ReconciliationInput(
            history=["e0", "ec"],
            evidence_sufficient=True,
            evidence_conflict=False,
            obligations_consistent=True,
            resources_consistent=True,
            dependencies_resolved=True,
            provenance_sufficient=True,
            candidate_states=["S2"],
        )
    )

    assert result.classification == ReconciliationClass.RECONCILED

    record = engine.evidence.records()[-1]

    assert record.payload["history"] == ["e0", "ec"]


def test_engine_records_reconstructed_continuity():
    engine = F1Engine()

    result = engine.classify_continuity(
        ContinuityInput(
            history=["e0", "ec"],
            requirement_traces={
                "g1": [
                    "SATISFIED",
                    "VIOLATED",
                    "SATISFIED",
                ],
            },
            reconstructed=True,
        )
    )

    assert result == ContinuityClass.RECONSTRUCTED

    record = engine.evidence.records()[-1]

    assert record.payload["classification"] == "RECONSTRUCTED"
    assert record.payload["history"] == ["e0", "ec"]
