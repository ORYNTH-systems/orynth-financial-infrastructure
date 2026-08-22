from .model import EffectClass, EffectResult, FinancialExecutionEvent


def classify_effect(event: FinancialExecutionEvent) -> EffectResult:
    intended = set(event.intended_mutations)

    if event.known_positive & event.known_negative:
        unresolved = intended - (event.known_positive | event.known_negative)
        return EffectResult(EffectClass.INDETERMINATE, unresolved)

    known = event.known_positive | event.known_negative
    unresolved = intended - known

    if unresolved:
        return EffectResult(EffectClass.INDETERMINATE, unresolved)

    economic = set(event.economically_recognized)

    if not economic:
        return EffectResult(EffectClass.NO_EFFECT, set())

    if economic == intended:
        return EffectResult(EffectClass.COMPLETED, set())

    if economic < intended:
        return EffectResult(EffectClass.PARTIAL, set())

    # Economic effect outside intended universe is not silently accepted.
    return EffectResult(EffectClass.INDETERMINATE, set())
