# F1 — Economic-State Continuity Predicates

## Purpose

F1 defines only the continuity predicates required to distinguish post-effect recovery states.

Complete financial continuity and finality theory remains owned primarily by F3.

---

## F1 Continuity Classes

C_F1 = {
    F1_CONTINUITY_UNASSESSED,
    F1_CONTINUITY_PRESERVED,
    F1_CONTINUITY_DEGRADED,
    F1_CONTINUITY_BROKEN,
    F1_CONTINUITY_RECONSTRUCTED,
    F1_FUNCTION_RESTORED_ONLY,
    F1_HISTORICALLY_RECONCILED,
    F1_CONTINUITY_INDETERMINATE
}

---

## CONTINUITY_PRESERVED

May be assigned only where no required continuity property was broken across the relevant post-effect path.

This class must not be inferred merely because remediation succeeded.

---

## CONTINUITY_DEGRADED

Used where continuity assurance weakened but a definitive break is not established.

---

## CONTINUITY_BROKEN

Used where a required continuity property demonstrably failed.

Examples may include:

- unauthorized or invalid effect,
- unresolved execution/effect discontinuity,
- state lineage break,
- required binding loss.

Later remediation does not erase the fact that continuity broke.

---

## CONTINUITY_RECONSTRUCTED

Used where historical state becomes reconstructable after a continuity break.

RECONSTRUCTED
!=
PRESERVED.

---

## FUNCTION_RESTORED_ONLY

Used where relevant function is restored without evidence supporting preserved continuity.

---

## HISTORICALLY_RECONCILED

Used where execution/remediation history is sufficiently reconciled but continuity was not necessarily preserved.

---

## CONTINUITY_INDETERMINATE

Used where available evidence cannot support a valid continuity classification.

---

## Core Rule

Once a continuity break is demonstrated:

later current-state equivalence

does not retroactively transform:

BROKEN

into:

PRESERVED.

The historical classification remains true.
