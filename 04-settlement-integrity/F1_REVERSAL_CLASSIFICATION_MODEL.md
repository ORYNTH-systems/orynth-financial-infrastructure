# F1 — Reversal Classification Model

Possible reversal outcomes:

REV_EXACT

REV_PARTIAL

REV_OVER

REV_WRONG_OBJECT

REV_STALE_TARGET

REV_NON_REVERSIBLE

REV_INTERVENING_CONFLICT

REV_NEW_DIVERGENCE

REV_CONTRADICTORY

REV_ZERO_EFFECT

REV_INDETERMINATE

---

## REV_EXACT

All required reversal predicates satisfied against a current valid reversal target.

---

## REV_PARTIAL

At least one required reversal predicate is satisfied while at least one remains unresolved.

---

## REV_OVER

Reversal exceeds the valid target.

---

## REV_WRONG_OBJECT

The reversal affects an object or relation outside the authorized target.

---

## REV_STALE_TARGET

The target references a prior state that is no longer validly reachable under current conditions.

---

## REV_NON_REVERSIBLE

One or more required dimensions cannot be validly reversed.

---

## REV_INTERVENING_CONFLICT

The reversal would erase or invalidate legitimate intervening state.

---

## REV_NEW_DIVERGENCE

The reversal resolves prior divergence while creating a new prohibited divergence.

---

## REV_CONTRADICTORY

The reversal moves state away from its valid reversal target.

---

## REV_ZERO_EFFECT

No reversal effect occurred and evidence is sufficient to establish no effect.

---

## REV_INDETERMINATE

Available evidence is insufficient for safe classification.
