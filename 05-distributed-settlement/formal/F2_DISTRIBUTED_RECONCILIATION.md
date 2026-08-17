# FIN-F2-07 — Distributed Reconciliation

## 1. Purpose

Distributed reconciliation determines what can be established from
conflicting, forked, incomplete, stale, or inconsistent evidence.

Reconciliation is epistemic and classificatory unless a separate
authorized consequential execution is invoked.

Reconciliation itself does not mutate financial state.

---

## 2. Reconciliation Input

Define:

R_in(q_d,t)

as the evidence-preserving input set containing relevant:

- authority records
- agreement records
- commitment records
- consensus observations
- admission decisions
- execution traces
- leg effects
- branch histories
- finality claims
- domain observations
- timestamps
- scope records
- provenance

---

## 3. Reconciliation Operator

Define:

R_d(q_d,t | GR)

as the distributed reconciliation operator under governing rule set GR.

R_d evaluates evidence.

R_d SHALL NOT fabricate missing evidence.

---

## 4. Reconciliation Result

Define:

ReconciliationResult(q_d,t)

in:

RECONCILED

RECONCILED-WITH-RESIDUAL-CONFLICT

REVALIDATION-REQUIRED

RECONSTRUCTION-REQUIRED

UNRESOLVED

INDETERMINATE

---

## 5. RECONCILED

RECONCILED means the material conflict set has been determinately
classified or resolved for the required evaluation context.

RECONCILED != RESTORED

RECONCILED != CONTINUITY-PRESERVED

RECONCILED != FINAL

RECONCILED != HISTORICALLY-UNCONFLICTED

---

## 6. RECONCILED-WITH-RESIDUAL-CONFLICT

This class applies where sufficient reconciliation has occurred for a
specific decision context while non-blocking or out-of-scope conflicts
remain historically or operationally present.

Residual conflict SHALL remain evidenced.

---

## 7. REVALIDATION-REQUIRED

Applies where previously valid authority, scope, commitment, consensus,
admission, or finality determinations must be reevaluated against current
state.

Revalidation != Reconstruction.

---

## 8. RECONSTRUCTION-REQUIRED

Applies where the relevant execution or state history cannot be
sufficiently classified without rebuilding a prior evidence/state chain.

Reconstruction may use:

execution traces
receipts
effects
branch records
external observations
historical authority state
prior finality classifications

Reconstruction does not recreate continuity automatically.

---

## 9. UNRESOLVED

UNRESOLVED means a recognized material conflict remains and no governing
rule or evidence set currently permits deterministic resolution.

UNRESOLVED shall not be promoted to clean state.

---

## 10. INDETERMINATE

INDETERMINATE means available evidence is insufficient to determine a
reconciliation outcome.

INDETERMINATE != UNRESOLVED.

UNRESOLVED may be well-evidenced conflict with no governing resolution.

INDETERMINATE is evidentiary insufficiency.

---

## 11. Reconciliation Precedence

Where competing evidence exists, precedence SHALL come from explicit
governing rules concerning:

authority
scope
time
provenance
domain
dependency
historical ordering
evidence integrity

Reconciliation SHALL NOT invent precedence from convenience.

---

## 12. No Majority Manufacture

MajorityObservation(q_d,t) !=> Reconciled(q_d,t)

A majority may be wrong, stale, unauthorized, or out-of-scope.

---

## 13. No Consensus Manufacture

Consensus(q_d,phi,t) !=> Reconciled(q_d,t)

Consensus is one possible evidence input.

It is not reconciliation itself.

---

## 14. No Canonicality Manufacture

LargestBranch(q_d,t) !=> CanonicalBranch(q_d,t)

LongestBranch(q_d,t) !=> CanonicalBranch(q_d,t)

NewestBranch(q_d,t) !=> CanonicalBranch(q_d,t)

Canonicality requires an explicit governing rule.

---

## 15. No State Mutation by Reconciliation

R_d(q_d,t) does not itself authorize:

compensation
reversal
re-execution
alternate settlement
state overwrite

Any consequential repair remains a new execution subject to independent
authority and admissibility.

---

## 16. Historical Persistence

A resolved conflict remains part of the historical execution record.

Reconciliation cannot erase:

prior forks
prior partial effect
prior inconsistent observations
prior finality conflict
prior reconstruction

---

## 17. Finality After Reconciliation

ReconciliationResult = RECONCILED

does not imply:

SettlementFinal

A later finality evaluation may consume the reconciled evidence and
produce a separate finality classification.

---

## 18. Continuity After Reconciliation

ReconciliationResult = RECONCILED

does not imply:

ContinuityPreserved

Distributed continuity classification remains FIN-F2-08.
