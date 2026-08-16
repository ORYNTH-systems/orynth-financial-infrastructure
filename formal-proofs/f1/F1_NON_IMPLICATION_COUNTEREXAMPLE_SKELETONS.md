# F1 — Non-Implication Counterexample Proof Skeletons

## Rule

To establish:

A does not imply B

construct one admissible model M such that:

M satisfies A

and:

M does not satisfy B.

---

## C1 — Compensation Requirement / Authorization

Construct:

R = R_COMPENSATION_REQUIRED

with:

Admission = DENIED.

Then:

CompensationRequired = true

CompensationAuthorized = false.

---

## C2 — Reversal Requirement / Authorization

Construct:

R = R_REVERSAL_REQUIRED

with:

Admission = DENIED.

Then:

ReversalRequired = true

ReversalAuthorized = false.

---

## C3 — Exact Compensation / Historical Equivalence

Construct history:

H_0 = [partial originating execution]

H_1 = [partial originating execution, exact compensation]

with current compensation target satisfied.

Then:

ExactCompensation(H_1) = true

while:

H_1 != H_prior.

---

## C4 — Exact Reversal / Historical Equivalence

Construct:

originating transfer

followed by exact reversal.

Current selected state may equal the prior selected state.

History still contains two consequential executions.

Thus:

HistoricalEquivalence = false.

---

## C5 — Reconciliation / Continuity

Construct a fully evidenced unauthorized partial effect.

Later reconcile every event and residual.

Then:

Reconciled = true

while the demonstrated historical continuity break remains.

---

## C6 — Functional Restoration / Continuity

Construct a failure causing continuity break.

Restore operational function.

Then:

FunctionalRestoration = true

while:

ContinuityPreserved = false.

---

## Status

These are proof skeletons.

They remain OPEN until formally instantiated and checked.
