from f1_runtime.evidence import EvidenceLedger


def test_origin_and_compensation_remain_separate():
    ledger = EvidenceLedger()

    ledger.append(
        "ORIGIN_EFFECT",
        "e0",
        None,
        {"classification": "PARTIAL"},
    )

    ledger.append(
        "COMPENSATION_EFFECT",
        "ec",
        "e0",
        {"classification": "COMPLETED"},
    )

    records = ledger.records()

    assert records[0].event_id == "e0"
    assert records[1].event_id == "ec"
    assert records[1].parent_event_id == "e0"


def test_origin_and_reversal_remain_separate():
    ledger = EvidenceLedger()

    ledger.append(
        "ORIGIN_EFFECT",
        "e0",
        None,
        {"classification": "COMPLETED"},
    )

    ledger.append(
        "REVERSAL_EFFECT",
        "er",
        "e0",
        {"classification": "COMPLETED"},
    )

    records = ledger.records()

    assert [r.event_id for r in records] == ["e0", "er"]


def test_sequence_is_append_ordered():
    ledger = EvidenceLedger()

    for event_id in ["e0", "ec", "er"]:
        ledger.append(
            "EVENT",
            event_id,
            None,
            {},
        )

    records = ledger.records()

    assert [r.sequence for r in records] == [1, 2, 3]


def test_returned_record_cannot_mutate_internal_history():
    ledger = EvidenceLedger()

    ledger.append(
        "ORIGIN_EFFECT",
        "e0",
        None,
        {"classification": "PARTIAL"},
    )

    records = ledger.records()
    records[0].payload["classification"] = "ERASED"

    fresh = ledger.records()

    assert fresh[0].payload["classification"] == "PARTIAL"


def test_history_for_preserves_parent_relationship():
    ledger = EvidenceLedger()

    ledger.append(
        "ORIGIN",
        "e0",
        None,
        {},
    )

    ledger.append(
        "COMPENSATION",
        "ec",
        "e0",
        {},
    )

    history = ledger.history_for("e0")

    assert len(history) == 2
    assert history[0].event_id == "e0"
    assert history[1].parent_event_id == "e0"
