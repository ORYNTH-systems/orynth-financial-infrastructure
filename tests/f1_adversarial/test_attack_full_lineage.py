from f1_runtime.compensation import propose_compensation
from f1_runtime.engine import F1Engine
from f1_runtime.model import (
    AuthorityContext,
    ContinuityInput,
    FinancialExecutionEvent,
    ReconciliationInput,
)


def test_full_origin_repair_reconcile_continuity_path_survives():
    engine = F1Engine()

    origin = FinancialExecutionEvent(
        event_id="e0",
        intended_mutations={"A", "B"},
        known_positive={"A"},
        known_negative={"B"},
        economically_recognized={"A"},
    )

    engine.classify(origin)

    compensation = propose_compensation(
        origin,
        "ec",
        {"C"},
        AuthorityContext(
            authorized=True,
            scope_valid=True,
            current=True,
        ),
    )

    engine.admit_compensation(compensation)

    engine.reconcile(
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

    engine.classify_continuity(
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

    records = engine.evidence.records()

    assert len(records) == 4

    assert records[0].event_id == "e0"
    assert records[1].event_id == "ec"
    assert records[1].parent_event_id == "e0"

    assert records[2].record_type == "RECONCILIATION"
    assert records[2].payload["history"] == ["e0", "ec"]

    assert records[3].record_type == "CONTINUITY_CLASSIFICATION"
    assert records[3].payload["history"] == ["e0", "ec"]
    assert records[3].payload["classification"] == "RECONSTRUCTED"
