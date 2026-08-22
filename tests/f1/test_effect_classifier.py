from f1_runtime.effect_classifier import classify_effect
from f1_runtime.model import EffectClass, FinancialExecutionEvent


def test_no_effect():
    event = FinancialExecutionEvent(
        event_id="e0",
        intended_mutations={"A", "B"},
        known_negative={"A", "B"},
        economically_recognized=set(),
    )

    assert classify_effect(event).classification == EffectClass.NO_EFFECT


def test_partial():
    event = FinancialExecutionEvent(
        event_id="e0",
        intended_mutations={"A", "B"},
        known_positive={"A"},
        known_negative={"B"},
        economically_recognized={"A"},
    )

    assert classify_effect(event).classification == EffectClass.PARTIAL


def test_completed():
    event = FinancialExecutionEvent(
        event_id="e0",
        intended_mutations={"A", "B"},
        known_positive={"A", "B"},
        economically_recognized={"A", "B"},
    )

    assert classify_effect(event).classification == EffectClass.COMPLETED


def test_unresolved_is_indeterminate():
    event = FinancialExecutionEvent(
        event_id="e0",
        intended_mutations={"A", "B"},
        known_positive={"A"},
        economically_recognized={"A"},
    )

    result = classify_effect(event)

    assert result.classification == EffectClass.INDETERMINATE
    assert result.unresolved == {"B"}


def test_conflicting_knowledge_is_indeterminate():
    event = FinancialExecutionEvent(
        event_id="e0",
        intended_mutations={"A"},
        known_positive={"A"},
        known_negative={"A"},
        economically_recognized={"A"},
    )

    assert classify_effect(event).classification == EffectClass.INDETERMINATE


def test_unknown_mutation_is_indeterminate():
    event = FinancialExecutionEvent(
        event_id="e0",
        intended_mutations={"A"},
        known_positive={"A"},
        economically_recognized={"A", "X"},
    )

    assert classify_effect(event).classification == EffectClass.INDETERMINATE
