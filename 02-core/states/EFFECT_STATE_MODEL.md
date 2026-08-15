# Economic Effect State Model

## Effect Domain

Let:

E_F = {
    NO_EFFECT,
    PARTIAL_EFFECT,
    COMPLETED_EFFECT,
    COMPENSATING_EFFECT,
    REVERSAL_EFFECT,
    MIXED_EFFECT,
    INDETERMINATE_EFFECT
}

---

## NO_EFFECT

No governed economic state mutation has occurred.

---

## PARTIAL_EFFECT

At least one economically consequential state mutation occurred, but the full intended execution effect was not established.

---

## COMPLETED_EFFECT

The intended execution-level economic effect occurred.

This does not establish finality.

---

## COMPENSATING_EFFECT

A new economic effect created by a separately governed compensation execution.

Compensation does not erase the originating effect.

---

## REVERSAL_EFFECT

A new economic effect created by a separately governed reversal execution.

Reversal does not erase historical execution.

---

## MIXED_EFFECT

Multiple heterogeneous or conflicting effects exist and cannot be represented honestly as a single simpler effect class.

---

## INDETERMINATE_EFFECT

Available evidence is insufficient to classify observed economic effect.

---

## Core Non-Equivalence

NO_EFFECT != PARTIAL_EFFECT

PARTIAL_EFFECT != COMPLETED_EFFECT

COMPENSATING_EFFECT != REVERSAL_EFFECT

REVERSAL_EFFECT != HISTORICAL_ERASURE

STATE_EQUIVALENCE_AFTER_REVERSAL != HISTORY_EQUIVALENCE
