# F1 — Post-Effect State Algebra

## Purpose

F1 models post-effect financial execution as a typed product state rather than one flattened lifecycle variable.

The architecture must preserve independent distinctions among:

- economic effect,
- settlement,
- remediation/resolution,
- reconciliation,
- finality,
- continuity.

---

## 1. Product State

Define the F1 state:

X_F1 = E x S x R x Q x F x C

where:

E = economic-effect state
S = settlement state
R = resolution/remediation state
Q = reconciliation state
F = finality classification
C = continuity classification

A concrete post-effect state is:

x = (e,s,r,q,f,c)

---

## 2. Effect State

Let:

E = {
    E_NO_EFFECT,
    E_PARTIAL,
    E_COMPLETED,
    E_COMPENSATING_PARTIAL,
    E_COMPENSATING_COMPLETED,
    E_REVERSAL_PARTIAL,
    E_REVERSAL_COMPLETED,
    E_MIXED,
    E_INDETERMINATE
}

### E_NO_EFFECT

No governed consequential economic mutation is established.

This state ordinarily remains outside F1 primary novelty unless effect uncertainty persists.

### E_PARTIAL

Some but not all intended originating economic effect occurred.

### E_COMPLETED

The intended originating execution-level effect completed.

This does not imply valid finality or preserved continuity.

### E_COMPENSATING_PARTIAL

A compensating execution itself produced only partial effect.

### E_COMPENSATING_COMPLETED

The compensating execution produced its intended execution-level effect.

### E_REVERSAL_PARTIAL

A reversal execution itself produced only partial effect.

### E_REVERSAL_COMPLETED

The reversal execution produced its intended execution-level effect.

### E_MIXED

Multiple economically consequential effects coexist and cannot be reduced without information loss.

### E_INDETERMINATE

Available evidence cannot establish a valid effect class.

---

## 3. Settlement State

Let:

S = {
    S_NONE,
    S_PENDING,
    S_IN_PROGRESS,
    S_PARTIAL,
    S_PROVISIONAL,
    S_SETTLED,
    S_INTERRUPTED,
    S_REMEDIATION_PENDING,
    S_RECONCILIATION_PENDING,
    S_RECONCILED,
    S_FINALITY_PENDING,
    S_FINALIZED,
    S_INDETERMINATE
}

Effect state and settlement state remain independent.

Example:

E_COMPLETED
with
S_PARTIAL

is valid.

Likewise:

E_PARTIAL
with
S_PROVISIONAL

may be valid.

---

## 4. Resolution / Remediation State

Let:

R = {
    R_NONE,
    R_CONTAINMENT_REQUIRED,
    R_CONTAINED,
    R_COMPENSATION_REQUIRED,
    R_COMPENSATION_ADMISSION_PENDING,
    R_COMPENSATING,
    R_COMPENSATED,
    R_REVERSAL_REQUIRED,
    R_REVERSAL_ADMISSION_PENDING,
    R_REVERSING,
    R_REVERSED,
    R_REMEDIATION_PARTIAL,
    R_REMEDIATION_FAILED,
    R_REMEDIATION_INDETERMINATE
}

Important:

R_COMPENSATION_REQUIRED
!=
R_COMPENSATING

R_REVERSAL_REQUIRED
!=
R_REVERSING

Requirement does not create authority.

---

## 5. Reconciliation State

Let:

Q = {
    Q_NOT_REQUIRED,
    Q_REQUIRED,
    Q_PENDING,
    Q_IN_PROGRESS,
    Q_RECONCILED,
    Q_DIVERGENT,
    Q_INDETERMINATE
}

Q_RECONCILED does not imply preserved continuity.

Q_DIVERGENT is explicit and may survive remediation.

---

## 6. Finality State

Let:

F = {
    F_UNASSESSED,
    F_PENDING,
    F_PROVISIONAL,
    F_REVERSIBLE,
    F_CONDITIONALLY_FINAL,
    F_FINAL,
    F_DISPUTED,
    F_REOPENED,
    F_INDETERMINATE
}

F1 may enter and preserve F_PENDING or related preliminary finality states.

Full finality theory is primarily owned by F3.

---

## 7. Continuity State

Let:

C = {
    C_UNASSESSED,
    C_PRESERVED,
    C_DEGRADED,
    C_BROKEN,
    C_RECONSTRUCTED,
    C_FUNCTIONALLY_RESTORED,
    C_HISTORICALLY_RECONCILED,
    C_INDETERMINATE
}

F1 may identify continuity implications.

Full continuity-classification theory is primarily owned by F3.

---

## 8. State Non-Equivalence

For x=(e,s,r,q,f,c):

e does not determine s.

s does not determine r.

r does not determine q.

q does not determine f.

f does not determine c.

Therefore:

EffectState
!= SettlementState
!= ResolutionState
!= ReconciliationState
!= FinalityState
!= ContinuityState

No plane may be inferred solely from another plane.

---

## 9. Post-Effect Entry Set

Define:

Entry_F1(x)

when:

e in {
    E_PARTIAL,
    E_COMPLETED,
    E_COMPENSATING_PARTIAL,
    E_COMPENSATING_COMPLETED,
    E_REVERSAL_PARTIAL,
    E_REVERSAL_COMPLETED,
    E_MIXED,
    E_INDETERMINATE
}

or when NO_EFFECT cannot be established.

---

## 10. Recursive Remediation

A critical property of F1 is that remediation is itself execution.

Therefore compensation can itself become partial:

R_COMPENSATING
-> E_COMPENSATING_PARTIAL

and reversal can itself become partial:

R_REVERSING
-> E_REVERSAL_PARTIAL

Such states SHALL NOT be collapsed back into the original originating partial effect.

They are new effect-bearing execution events with their own:

- event identity,
- authority,
- admission,
- effect history,
- evidence,
- settlement implications.

---

## 11. Remediation Depth

Define remediation depth:

d(e_0) = 0

for the originating execution.

If execution e_(n+1) exists to compensate, reverse, or remediate effect from e_n, then:

d(e_(n+1)) = d(e_n) + 1

Remediation depth records causal/remedial lineage.

Depth does not itself imply validity.

---

## 12. Recursive Partiality

If a compensation execution at depth n becomes partial:

e_n -> E_COMPENSATING_PARTIAL

then the architecture may require a new remediation decision:

e_(n+1)

with:

d(e_(n+1)) = d(e_n) + 1

The new execution must independently satisfy authority and admission.

No recursive remediation execution inherits authority merely from the existence of earlier failure.

---

## 13. Termination Concern

The architecture must not assume remediation recursion always terminates.

F1 later proof obligations must distinguish:

- finite successful remediation,
- finite failed remediation,
- repeated partial remediation,
- bounded containment,
- indeterminate termination,
- structurally prohibited further remediation.

No theorem of guaranteed termination is asserted in FIN-F1-02.

---

## 14. Historical Preservation

Every remediation execution adds history.

Let H_n be the execution history through remediation depth n.

Then:

H_(n+1) = H_n appended with e_(n+1)

not:

H_(n+1) = replace(H_n,e_(n+1))

History is append-preserving.

---

## 15. Economic Equivalence

A later state may be economically equivalent under some projection P:

P(x_i) = P(x_j)

while the complete historical states remain unequal:

H_i != H_j

Therefore:

EconomicEquivalence
does not imply
HistoricalEquivalence.
