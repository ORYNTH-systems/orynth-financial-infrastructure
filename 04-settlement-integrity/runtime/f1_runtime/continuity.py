from .model import ContinuityClass, ContinuityInput


_ALLOWED = {
    "SATISFIED",
    "DEGRADED",
    "VIOLATED",
    "UNKNOWN",
}


def classify_continuity(
    data: ContinuityInput,
) -> ContinuityClass:

    flattened = []

    for trace in data.requirement_traces.values():
        for state in trace:

            if state not in _ALLOWED:
                return ContinuityClass.INDETERMINATE

            flattened.append(state)

    if not flattened:
        return ContinuityClass.INDETERMINATE

    if "UNKNOWN" in flattened:
        return ContinuityClass.INDETERMINATE

    if "VIOLATED" in flattened:

        if data.reconstructed:
            return ContinuityClass.RECONSTRUCTED

        return ContinuityClass.BROKEN

    if data.reconstructed:
        # Reconstruction without a represented prior break is invalid.
        return ContinuityClass.INDETERMINATE

    if "DEGRADED" in flattened:
        return ContinuityClass.DEGRADED

    return ContinuityClass.PRESERVED
