import pytest

from f1_runtime.compensation import (
    admit_compensation,
    propose_compensation,
)
from f1_runtime.model import (
    AuthorityContext,
    FinancialExecutionEvent,
)


def origin():
    return FinancialExecutionEvent(
        event_id="e0",
        intended_mutations={"A"},
    )


def test_failure_cannot_create_compensation_authority():
    compensation = propose_compensation(
        origin(),
        "ec",
        {"C"},
        None,
    )

    permit = admit_compensation(compensation)

    assert permit.permitted is False


def test_original_failure_cannot_be_used_as_authority_object():
    compensation = propose_compensation(
        origin(),
        "ec",
        {"C"},
        AuthorityContext(
            authorized=False,
            scope_valid=True,
            current=True,
        ),
    )

    assert admit_compensation(compensation).permitted is False


def test_stale_compensation_authority_is_blocked():
    compensation = propose_compensation(
        origin(),
        "ec",
        {"C"},
        AuthorityContext(
            authorized=True,
            scope_valid=True,
            current=False,
        ),
    )

    permit = admit_compensation(compensation)

    assert permit.permitted is False
    assert "AUTHORITY_NOT_CURRENT" in permit.reason


def test_invalid_compensation_scope_is_blocked():
    compensation = propose_compensation(
        origin(),
        "ec",
        {"C"},
        AuthorityContext(
            authorized=True,
            scope_valid=False,
            current=True,
        ),
    )

    permit = admit_compensation(compensation)

    assert permit.permitted is False
    assert "SCOPE_INVALID" in permit.reason


def test_origin_id_reuse_for_compensation_is_rejected():
    with pytest.raises(
        ValueError,
        match="COMPENSATION_EVENT_ID_MUST_DIFFER_FROM_ORIGIN",
    ):
        propose_compensation(
            origin(),
            "e0",
            {"C"},
            AuthorityContext(True, True, True),
        )
