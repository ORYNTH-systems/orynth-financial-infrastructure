# F1 Formal Boundary

Let:

e ∈ E_F

be a canonical FinancialExecutionEvent.

Let:

t_b

denote the consequential economic-effect boundary.

Let:

M(e,t)

denote the set of economically consequential mutations attributable to e and
observable by time t.

Define the F1 applicability predicate:

B_F1(e,t) = 1

iff:

|M(e,t)| > 0

or the system cannot establish:

|M(e,t)| = 0

after the consequential effectuation boundary has been crossed.

Otherwise:

B_F1(e,t) = 0.

This intentionally separates:

execution process activity

from:

economically consequential mutation.

---

## Zero-Effect Domain

If:

|M(e,t)| = 0

is established before or at the relevant effectuation boundary, then F1's novel
post-effect machinery is not required.

---

## Partial-Effect Domain

Let:

M*(e)

be the complete intended mutation set.

A preliminary partial-effect condition is:

∅ ⊂ M(e,t) ⊂ M*(e)

subject to later refinement in FIN-F1-02.

This definition is intentionally provisional.

FIN-F1-02 owns the complete state algebra and edge cases.

---

## Indeterminate Domain

If the system cannot prove either:

M(e,t) = ∅

or:

M(e,t) != ∅

after entry into the consequential effectuation domain, F1 treats the result as
post-effect indeterminate rather than silently assigning NO-EFFECT.

---

## Historical Persistence

If:

m ∈ M(e,t)

occurred at any prior time, later compensating or reversing mutations do not imply:

m never occurred.

This is a required F1 semantic boundary and will be formalized/proved in later passes.
