from f1_runtime.continuity import classify_continuity
from f1_runtime.model import ContinuityClass, ContinuityInput


def test_preserved():
    data = ContinuityInput(
        history=["e0"],
        requirement_traces={
            "g1": ["SATISFIED", "SATISFIED"],
        },
    )

    assert classify_continuity(data) == ContinuityClass.PRESERVED


def test_degraded():
    data = ContinuityInput(
        history=["e0"],
        requirement_traces={
            "g1": ["SATISFIED", "DEGRADED", "SATISFIED"],
        },
    )

    assert classify_continuity(data) == ContinuityClass.DEGRADED


def test_broken():
    data = ContinuityInput(
        history=["e0"],
        requirement_traces={
            "g1": ["SATISFIED", "VIOLATED"],
        },
    )

    assert classify_continuity(data) == ContinuityClass.BROKEN


def test_reconstructed_is_not_preserved():
    data = ContinuityInput(
        history=["e0", "ec"],
        requirement_traces={
            "g1": ["SATISFIED", "VIOLATED", "SATISFIED"],
        },
        reconstructed=True,
    )

    result = classify_continuity(data)

    assert result == ContinuityClass.RECONSTRUCTED
    assert result != ContinuityClass.PRESERVED


def test_unknown_is_indeterminate():
    data = ContinuityInput(
        history=["e0"],
        requirement_traces={
            "g1": ["SATISFIED", "UNKNOWN"],
        },
    )

    assert classify_continuity(data) == ContinuityClass.INDETERMINATE


def test_reconstruction_without_break_is_indeterminate():
    data = ContinuityInput(
        history=["e0"],
        requirement_traces={
            "g1": ["SATISFIED", "SATISFIED"],
        },
        reconstructed=True,
    )

    assert classify_continuity(data) == ContinuityClass.INDETERMINATE
