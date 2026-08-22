import pytest

from f1_runtime.model import (
    AuthorityContext,
    FinancialExecutionEvent,
)
from f1_runtime.reversal import (
    admit_reversal,
    propose_reversal,
)


def origin():
    return FinancialExecutionEvent(
        event_id="e0",
        intended_mutations={"A"},
    )


def test_eligibility_alone_cannot_create_reversal_permit():
    reversal = propose_reversal(
        origin(),
        "er",
        {"R"},
        None,
        eligible=True,
        reversible=True,
    )

    assert admit_reversal(reversal).permitted is False


def test_reversibility_alone_cannot_create_reversal_permit():
    reversal = propose_reversal(
        origin(),
        "er",
        {"R"},
        AuthorityContext(
            authorized=False,
            scope_valid=True,
            current=True,
        ),
        eligible=True,
        reversible=True,
    )

    assert admit_reversal(reversal).permitted is False


def test_stale_reversal_authority_is_blocked():
    reversal = propose_reversal(
        origin(),
        "er",
        {"R"},
        AuthorityContext(
            authorized=True,
            scope_valid=True,
            current=False,
        ),
        eligible=True,
        reversible=True,
    )

    permit = admit_reversal(reversal)

    assert permit.permitted is False
    assert "AUTHORITY_NOT_CURRENT" in permit.reason


def test_invalid_reversal_scope_is_blocked():
    reversal = propose_reversal(
        origin(),
        "er",
        {"R"},
        AuthorityContext(
            authorized=True,
            scope_valid=False,
            current=True,
        ),
        eligible=True,
        reversible=True,
    )

    permit = admit_reversal(reversal)

    assert permit.permitted is False
    assert "SCOPE_INVALID" in permit.reason


def test_origin_id_reuse_for_reversal_is_rejected():
    with pytest.raises(
        ValueError,
        match="REVERSAL_EVENT_ID_MUST_DIFFER_FROM_ORIGIN",
    ):
        propose_reversal(
            origin(),
            "e0",
            {"R"},
            AuthorityContext(True, True, True),
            eligible=True,
            reversible=True,
        )
