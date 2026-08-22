from f1_runtime.effect_classifier import classify_effect
from f1_runtime.model import (
    EffectClass,
    FinancialExecutionEvent,
)


def test_external_mutation_injection_is_not_determinate():
    event = FinancialExecutionEvent(
        event_id="e0",
        intended_mutations={"A"},
        known_positive={"A"},
        economically_recognized={"A", "X"},
    )

    assert classify_effect(event).classification == EffectClass.INDETERMINATE


def test_unknown_known_positive_is_not_accepted():
    event = FinancialExecutionEvent(
        event_id="e0",
        intended_mutations={"A"},
        known_positive={"A", "X"},
        economically_recognized={"A"},
    )

    assert classify_effect(event).classification == EffectClass.INDETERMINATE


def test_unknown_known_negative_is_not_accepted():
    event = FinancialExecutionEvent(
        event_id="e0",
        intended_mutations={"A"},
        known_negative={"A", "X"},
        economically_recognized=set(),
    )

    assert classify_effect(event).classification == EffectClass.INDETERMINATE


def test_unresolved_effect_cannot_be_forced_to_no_effect():
    event = FinancialExecutionEvent(
        event_id="e0",
        intended_mutations={"A", "B"},
        known_negative={"A"},
        economically_recognized=set(),
    )

    assert classify_effect(event).classification == EffectClass.INDETERMINATE


def test_conflicting_occurrence_cannot_be_determinate():
    event = FinancialExecutionEvent(
        event_id="e0",
        intended_mutations={"A"},
        known_positive={"A"},
        known_negative={"A"},
        economically_recognized={"A"},
    )

    assert classify_effect(event).classification == EffectClass.INDETERMINATE


def test_economic_effect_without_positive_occurrence_is_indeterminate():
    event = FinancialExecutionEvent(
        event_id="e0",
        intended_mutations={"A"},
        known_negative={"A"},
        economically_recognized={"A"},
    )

    assert classify_effect(event).classification == EffectClass.INDETERMINATE
