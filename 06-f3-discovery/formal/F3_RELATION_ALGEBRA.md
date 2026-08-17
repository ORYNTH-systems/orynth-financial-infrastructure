# F3 Relation Algebra

Status: FORMALIZED

## Core Relations

### ObligationSatisfied

ObligationSatisfied(o, e, σ, τ)

True only when admissible evidence establishes satisfaction of the applicable obligation under current scope and temporal validity.

---

### ResidualExists

ResidualExists(o, e)

True when an obligation remains unsatisfied in at least one applicable dimension.

---

### CustodyValid

CustodyValid(c, a, σ, τ)

True only when current custody state is supported by valid authority, scope, and temporal conditions.

---

### CustodyTransferComplete

CustodyTransferComplete(c0, c1, e)

Transfer occurrence alone is insufficient.

Completion requires all applicable custody transition requirements to be discharged.

---

### FinalityEligible

FinalityEligible(Ψ_t)

True only if every applicable finality requirement is currently satisfied.

---

### Final

Final(Ψ_t)

Final(Ψ_t) iff:

1. FinalityEligible(Ψ_t);
2. no unresolved applicable Finality Conflict exists;
3. evidence sufficiency is satisfied;
4. required custody predicates are satisfied;
5. required obligation predicates are satisfied;
6. applicable authority remains current;
7. applicable scope remains valid;
8. no blocking contradiction exists.

---

### ConsequentiallyClosed

ConsequentiallyClosed(Ψ_t)

True only when the request-relative financial consequence may validly transition from active consequential processing into closure.

---

### Reopenable

Reopenable(Ψ_t, q)

Determines whether a previously closed or final state may validly re-enter an active consequential state for request q.

---

### FinalityConflictExists

FinalityConflictExists(Ψ_t)

True when admissible current evidence or authority states imply mutually incompatible finality classifications.

---

### PostFinalityContradiction

PostFinalityContradiction(Ψ_t, e_new)

True when newly admitted evidence contradicts a predicate required by the current finality classification.
