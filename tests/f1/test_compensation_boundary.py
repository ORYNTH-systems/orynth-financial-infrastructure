import pytest

from f1_runtime.compensation import (
    admit_compensation,
    propose_compensation,
)
from f1_runtime.model import AuthorityContext, FinancialExecutionEvent


def origin():
    return FinancialExecutionEvent(
        event_id="e0",
        intended_mutations={"A"},
    )


def test_need_does_not_create_compensation_authority():
    event = propose_compensation(
        origin(),
        "ec",
        {"C"},
        None,
    )

    assert admit_compensation(event).permitted is False


def test_false_authority_blocks_compensation():
    event = propose_compensation(
        origin(),
        "ec",
        {"C"},
        AuthorityContext(
            authorized=False,
            scope_valid=True,
        ),
    )

    assert admit_compensation(event).permitted is False


def test_invalid_scope_blocks_compensation():
    event = propose_compensation(
        origin(),
        "ec",
        {"C"},
        AuthorityContext(
            authorized=True,
            scope_valid=False,
        ),
    )

    assert admit_compensation(event).permitted is False


def test_stale_authority_blocks_compensation():
    event = propose_compensation(
        origin(),
        "ec",
        {"C"},
        AuthorityContext(
            authorized=True,
            scope_valid=True,
            current=False,
        ),
    )

    assert admit_compensation(event).permitted is False


def test_valid_compensation_receives_boundary_permit():
    event = propose_compensation(
        origin(),
        "ec",
        {"C"},
        AuthorityContext(
            authorized=True,
            scope_valid=True,
            current=True,
        ),
    )

    permit = admit_compensation(event)

    assert permit.permitted is True
    assert permit.event_id == "ec"


def test_origin_identity_cannot_be_reused_for_compensation():
    with pytest.raises(
        ValueError,
        match="COMPENSATION_EVENT_ID_MUST_DIFFER_FROM_ORIGIN",
    ):
        propose_compensation(
            origin(),
            "e0",
            {"C"},
            None,
        )
