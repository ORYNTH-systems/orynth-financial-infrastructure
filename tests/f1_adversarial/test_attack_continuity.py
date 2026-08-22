from f1_runtime.continuity import classify_continuity
from f1_runtime.model import (
    ContinuityClass,
    ContinuityInput,
)


def test_reconstructed_path_cannot_be_preserved():
    data = ContinuityInput(
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

    result = classify_continuity(data)

    assert result == ContinuityClass.RECONSTRUCTED
    assert result != ContinuityClass.PRESERVED


def test_reconstruction_without_recorded_break_is_not_accepted():
    data = ContinuityInput(
        history=["e0", "ec"],
        requirement_traces={
            "g1": [
                "SATISFIED",
                "SATISFIED",
            ],
        },
        reconstructed=True,
    )

    assert classify_continuity(data) == ContinuityClass.INDETERMINATE


def test_unknown_break_state_cannot_be_preserved():
    data = ContinuityInput(
        history=["e0"],
        requirement_traces={
            "g1": [
                "SATISFIED",
                "UNKNOWN",
            ],
        },
    )

    assert classify_continuity(data) == ContinuityClass.INDETERMINATE


def test_break_without_reconstruction_remains_broken():
    data = ContinuityInput(
        history=["e0"],
        requirement_traces={
            "g1": [
                "SATISFIED",
                "VIOLATED",
            ],
        },
        reconstructed=False,
    )

    assert classify_continuity(data) == ContinuityClass.BROKEN
