from .model import EffectClass, EffectResult, FinancialExecutionEvent


def classify_effect(event: FinancialExecutionEvent) -> EffectResult:
    intended = set(event.intended_mutations)

    if not intended:
        return EffectResult(
            EffectClass.INDETERMINATE,
            set(),
        )

    if event.known_positive - intended:
        return EffectResult(
            EffectClass.INDETERMINATE,
            set(),
        )

    if event.known_negative - intended:
        return EffectResult(
            EffectClass.INDETERMINATE,
            set(),
        )

    if event.economically_recognized - intended:
        return EffectResult(
            EffectClass.INDETERMINATE,
            set(),
        )

    if event.known_positive & event.known_negative:
        return EffectResult(
            EffectClass.INDETERMINATE,
            intended - (event.known_positive | event.known_negative),
        )

    known = event.known_positive | event.known_negative
    unresolved = intended - known

    if unresolved:
        return EffectResult(
            EffectClass.INDETERMINATE,
            unresolved,
        )

    economic = set(event.economically_recognized)

    # Economically recognized occurrence must be supported as occurred.
    if not economic.issubset(event.known_positive):
        return EffectResult(
            EffectClass.INDETERMINATE,
            set(),
        )

    if not economic:
        return EffectResult(
            EffectClass.NO_EFFECT,
            set(),
        )

    if economic == intended:
        return EffectResult(
            EffectClass.COMPLETED,
            set(),
        )

    return EffectResult(
        EffectClass.PARTIAL,
        set(),
    )
