# F1 — Effect Classification Precedence

## Purpose

This document prevents contradictory or indeterminate effects from being incorrectly collapsed into simple partial effect.

---

## Dimension-Level Outcomes

Each required effect dimension resolves to:

NO_EFFECT

PARTIAL_MATCH

FULL_MATCH

OVER_EFFECT

CONTRADICTORY_EFFECT

INDETERMINATE

---

## Global Classification Precedence

### Rule 1 — Indeterminacy

If evidence required for safe classification is materially insufficient:

E_INDETERMINATE

unless a stronger known contradictory classification remains valid over observed dimensions and the architecture explicitly supports mixed classification.

---

### Rule 2 — Contradiction / Over-Effect

If any required dimension contains:

CONTRADICTORY_EFFECT

or:

OVER_EFFECT

then the global state must not be E_COMPLETED.

Ordinarily classify:

E_MIXED

unless a more specific later subtype is introduced.

---

### Rule 3 — Full Effect

E_COMPLETED requires every required dimension to resolve FULL_MATCH.

---

### Rule 4 — Zero Effect

E_NO_EFFECT requires every required dimension to resolve NO_EFFECT with sufficient evidence.

---

### Rule 5 — Partial Effect

E_PARTIAL applies where:

- at least one intended-corresponding effect exists,
- full effect is not established,
- no higher-priority contradictory or indeterminate classification dominates.

---

## Safety Principle

Classification must preserve the highest-information state supported by evidence.

Simplification must not erase:

contradiction,
over-effect,
unknown state,
or dimension-level divergence.
