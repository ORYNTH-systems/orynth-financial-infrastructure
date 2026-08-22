from f1_runtime.evidence import EvidenceLedger


def populated():
    ledger = EvidenceLedger()

    ledger.append(
        "ORIGIN_EFFECT",
        "e0",
        None,
        {"classification": "PARTIAL"},
    )

    ledger.append(
        "COMPENSATION",
        "ec",
        "e0",
        {"classification": "COMPLETED"},
    )

    ledger.append(
        "RECONCILIATION",
        None,
        None,
        {
            "history": ["e0", "ec"],
            "classification": "RECONCILED",
        },
    )

    return ledger


def test_mutating_records_result_does_not_overwrite_ledger():
    ledger = populated()

    copy = ledger.records()

    copy[0].event_id = "ERASED"
    copy[0].payload["classification"] = "ERASED"

    fresh = ledger.records()

    assert fresh[0].event_id == "e0"
    assert fresh[0].payload["classification"] == "PARTIAL"


def test_clearing_returned_list_does_not_clear_ledger():
    ledger = populated()

    copy = ledger.records()
    copy.clear()

    assert len(ledger.records()) == 3


def test_compensation_does_not_remove_origin_record():
    ledger = populated()

    ids = [
        record.event_id
        for record in ledger.records()
    ]

    assert "e0" in ids
    assert "ec" in ids


def test_parent_lineage_remains_after_compensation():
    ledger = populated()

    comp = [
        record
        for record in ledger.records()
        if record.event_id == "ec"
    ][0]

    assert comp.parent_event_id == "e0"


def test_history_for_origin_contains_repair():
    ledger = populated()

    lineage = ledger.history_for("e0")

    assert any(
        record.event_id == "e0"
        for record in lineage
    )

    assert any(
        record.event_id == "ec"
        for record in lineage
    )
