# FIN-F2-05 — Partial Distributed Settlement

## 1. Purpose

Partial distributed settlement occurs when recognized consequential
effects exist across a distributed settlement structure but the
required distributed effect set has not been completely satisfied.

F2 does not create a competing definition of PARTIAL.

F2 identifies distributed conditions under which the inherited F1
partial-effect semantics apply.

---

## 2. Distributed Intended Mutation Set

For distributed proposal q_d, define:

M*_d(q_d)

as the union of intended consequential economic mutations associated
with the required distributed execution legs.

M*_d(q_d) =
Union over required consequential legs l_i of M*(l_i)

The underlying per-event intended mutation semantics are inherited
from F1.

---

## 3. Distributed Recognized Economic Effects

Define:

M_d,econ(q_d,t)

as the recognized consequential economic mutations attributable to the
distributed execution trace at time t.

Recognition is evidence-based.

Occurrence uncertainty remains INDETERMINATE.

---

## 4. Distributed Partial Classification

Under sufficient evidence:

empty proper subset condition:

∅ ⊂ M_d,econ(q_d,t) ⊂ M*_d(q_d)

implies the distributed settlement is in a partial-effect state.

This maps to inherited F1:

PARTIAL

It does not create a new competing effect classifier.

---

## 5. Leg-Level Partiality

Partiality may arise through:

- one leg complete while another remains no-effect
- one leg itself partially effected
- multiple legs partially effected
- required dependency execution interrupted
- recognized effects across only a strict subset of required legs

All such cases must preserve trace evidence.

---

## 6. No Endpoint Collapse

If later repair produces:

EconomicState_after ≡E EconomicState_intended

this does not imply that the original distributed settlement was
historically atomic.

Endpoint equivalence != atomic execution history.

---

## 7. Compensation

A compensating execution following partial distributed settlement is a
new consequential execution.

Compensation != completion of the original execution unless the active
formal profile explicitly defines a distinct continuation mechanism and
all identity/history rules are preserved.

Inherited F1 compensation semantics control repair authority.

---

## 8. Reversal

A reversal following partial distributed settlement is a new
counter-transition.

Reversal does not erase the earlier distributed partial state.

---

## 9. Reconciliation

A partially executed distributed settlement may require reconciliation
to determine:

- which legs executed
- which economic effects occurred
- which commitments remain live
- which dependencies remain unresolved
- which parties recognize which state
- which evidence is authoritative

Reconciliation does not itself mutate financial state.

---

## 10. Conflict

Partiality and conflict are distinct.

A settlement may be:

partial without conflict

conflicted without determinable partiality

both partial and conflicted

indeterminate as to one or both.

Conflict semantics are formalized later in FIN-F2-07.

---

## 11. Finality

PARTIAL != FINAL

ATOMIC-PARTIAL != FINAL

A partial distributed settlement cannot be promoted to completed
settlement finality merely because one technical subsystem reports a
terminal state.

---

## 12. Continuity

Partial distributed settlement may affect continuity, but the continuity
classification itself remains deferred to FIN-F2-08.

No continuity conclusion is automatically created by partiality alone.
