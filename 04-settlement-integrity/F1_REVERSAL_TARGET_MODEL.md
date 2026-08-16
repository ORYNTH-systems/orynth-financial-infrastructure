# F1 — Reversal Target Model

Define:

T_R =
(
    prior_state_reference,
    target_dimensions,
    target_values_or_relations,
    excluded_dimensions,
    intervening_state_constraints,
    permitted_residuals,
    prohibited_new_effects,
    reversibility_requirements,
    authority_constraints,
    evidence_requirements
)

A reversal target must be current-state-aware.

A prior state reference alone is insufficient.

---

## Target Classes

EXACT_PRIOR_STATE_TARGET

SELECTIVE_DIMENSION_TARGET

RELATIONAL_RESTORATION_TARGET

OBLIGATION_REVERSAL_TARGET

STATE_CORRECTION_TARGET

NO_VALID_REVERSAL_TARGET

---

## Validity

A reversal target may become invalid due to:

- stale state,
- unavailable resources,
- changed counterparties,
- later legitimate transfer,
- changed jurisdiction,
- changed policy,
- irreversible external state,
- finality constraints.

Target validity must therefore be evaluated at execution time.
