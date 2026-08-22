import pytest

from f1_runtime.model import AuthorityContext, FinancialExecutionEvent
from f1_runtime.reversal import admit_reversal, propose_reversal


def origin():
    return FinancialExecutionEvent(
        event_id="e0",
        intended_mutations={"A"},
    )


def test_eligibility_does_not_create_authority():
    event = propose_reversal(
        origin(),
        "er",
        {"R"},
        None,
        eligible=True,
        reversible=True,
    )

    assert admit_reversal(event).permitted is False


def test_ineligible_reversal_cannot_be_proposed():
    with pytest.raises(ValueError, match="REVERSAL_NOT_ELIGIBLE"):
        propose_reversal(
            origin(),
            "er",
            {"R"},
            AuthorityContext(True, True),
            eligible=False,
            reversible=True,
        )


def test_nonreversible_reversal_cannot_be_proposed():
    with pytest.raises(ValueError, match="REVERSAL_NOT_REVERSIBLE"):
        propose_reversal(
            origin(),
            "er",
            {"R"},
            AuthorityContext(True, True),
            eligible=True,
            reversible=False,
        )


def test_invalid_scope_blocks_reversal():
    event = propose_reversal(
        origin(),
        "er",
        {"R"},
        AuthorityContext(True, False),
        eligible=True,
        reversible=True,
    )

    assert admit_reversal(event).permitted is False


def test_stale_authority_blocks_reversal():
    event = propose_reversal(
        origin(),
        "er",
        {"R"},
        AuthorityContext(True, True, False),
        eligible=True,
        reversible=True,
    )

    assert admit_reversal(event).permitted is False


def test_valid_reversal_receives_boundary_permit():
    event = propose_reversal(
        origin(),
        "er",
        {"R"},
        AuthorityContext(True, True, True),
        eligible=True,
        reversible=True,
    )

    assert admit_reversal(event).permitted is True


def test_origin_identity_cannot_be_reused_for_reversal():
    with pytest.raises(
        ValueError,
        match="REVERSAL_EVENT_ID_MUST_DIFFER_FROM_ORIGIN",
    ):
        propose_reversal(
            origin(),
            "e0",
            {"R"},
            AuthorityContext(True, True),
            eligible=True,
            reversible=True,
        )
