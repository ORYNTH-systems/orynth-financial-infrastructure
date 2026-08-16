# F1 — Compensation Classification Model

After a compensating execution, classify the outcome against the explicit compensation target.

Possible classifications:

COMP_EXACT

COMP_PARTIAL

COMP_OVER

COMP_WRONG_DIMENSION

COMP_NEW_DIVERGENCE

COMP_CONTRADICTORY

COMP_ZERO_EFFECT

COMP_INDETERMINATE

---

## COMP_EXACT

All required target residuals resolved.

No prohibited new divergence.

---

## COMP_PARTIAL

At least one required residual improved or resolved.

At least one required residual remains unresolved.

---

## COMP_OVER

One or more ordered dimensions exceed the authorized compensation target.

---

## COMP_WRONG_DIMENSION

Observed compensation effect does not address the target divergence on required dimensions.

---

## COMP_NEW_DIVERGENCE

Compensation resolves some prior divergence but introduces new prohibited divergence.

---

## COMP_CONTRADICTORY

Compensation moves one or more required dimensions away from the authorized target or into an incompatible state.

---

## COMP_ZERO_EFFECT

No compensating economic effect occurred with sufficient evidence to establish that result.

---

## COMP_INDETERMINATE

Available evidence cannot support safe compensation classification.

---

## Precedence

Indeterminate evidence must not be converted into exact compensation.

Contradictory or new-divergence outcomes must not be collapsed into partial success.

Over-compensation must not be classified exact merely because all original residuals were eliminated.
