# F1 Reconciliation Proofs

## F1-NEQ-REC-001 — Reconciled Does Not Imply Restored

A reconciliation operator determines a current accepted state.

No definition requires that accepted state to equal the pre-origin state or desired
state.

Construct a case where the current custody/resource state is determinately known
but differs from the pre-origin configuration.

Then:

Reconciled(S_R) = true

while:

Restored(S_R) = false.

RESULT: COUNTEREXAMPLE-DISCHARGED
EVIDENCE: CONSTRUCTIVE-COUNTEREXAMPLE

---

## F1-NEQ-REC-002 — Reconciled Does Not Imply Continuity Preserved

Consider a fully evidenced history containing a qualifying continuity break.

The terminal state is determinately reconciled.

Thus:

Reconciled(S_R) = true

while:

ContinuityPreserved(H_t,S_R,Gamma) = false.

RESULT: COUNTEREXAMPLE-DISCHARGED
EVIDENCE: CONSTRUCTIVE-COUNTEREXAMPLE

---

## F1-SAFE-REC-003 — Insufficient Evidence Cannot Establish Clean Reconciliation

The reconciliation acceptance predicate requires sufficient evidence and a unique
accepted state.

Where those requirements fail, successful reconciliation is undefined.

Therefore a clean reconciled state does not follow from insufficient evidence.

RESULT: PROVED
EVIDENCE: FORMAL-DERIVATION

---

## F1-THM-REC-004 — Unique Accepted State

Assume exactly one candidate state S_R satisfies the complete reconciliation
acceptance predicate A_R(X_t,S_R).

By definition of R_F1:

R_F1(X_t) = S_R.

RESULT: PROVED
EVIDENCE: DEFINITIONAL-DERIVATION

---

## F1-NEQ-REC-005 — Failure and Indeterminacy Are Distinct

The model defines:

INDETERMINATE

for unresolved/pending evidence or multiple unresolved candidate states.

It defines:

FAILED

for contradiction or absence of any accepted state under completed reconciliation
criteria.

Since a model can exhibit pending evidence without contradiction, the two outcomes
are not equivalent.

RESULT: COUNTEREXAMPLE-DISCHARGED
EVIDENCE: CONSTRUCTIVE-COUNTEREXAMPLE

---

## F1-TRACE-REC-006 — Historical Event Preservation

The semantics require reconciliation to consume complete surviving lineage rather
than overwrite it.

The formal representation preserves the path.

Persistence/conformance in the future runtime remains open.

RESULT: PARTIAL
EVIDENCE: TRACEABILITY-ARGUMENT + RUNTIME-EVIDENCE-REQUIRED
