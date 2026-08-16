# F1 — Reconciliation Semantics

## Purpose

Reconciliation determines whether the current financial state, execution history, settlement history, remediation history, residual divergence, and surviving evidence can be placed into a coherent post-effect representation.

Reconciliation does not imply:

- economic equivalence,
- successful remediation,
- restored function,
- historical integrity,
- preserved continuity,
- finality.

---

## 1. Execution / Remediation History

Let:

H_t = (e_0,e_1,...,e_n)

where:

e_0 = originating execution

and:

e_i for i > 0

may be:

- compensation,
- reversal,
- containment-related consequential action,
- other explicit remediation execution.

History is ordered and append-preserving.

---

## 2. Current State

Let:

X_t

be current observed financial state.

Let:

S_t

be current settlement state.

Let:

R_t

be current remediation state.

Let:

Q_t

be current reconciliation state.

---

## 3. Residual Divergence

For every required effect dimension d_i define:

rho_i(T_i,O_i)

against the applicable target T_i.

The aggregate typed residual state is:

Rho_t =
(
    rho_1,
    rho_2,
    ...,
    rho_m
)

Residual state may contain:

RESOLVED

UNRESOLVED

CONTRADICTORY

OVER_EFFECT

INDETERMINATE

or domain-specific values.

---

## 4. Reconciliation Relation

Define:

Recon(H_t,X_t,S_t,R_t,Rho_t,E_t)

where:

E_t

is the available evidence set.

Recon succeeds only when the architecture can produce a coherent account of:

- what was intended,
- what executed,
- what effect occurred,
- what remediation occurred,
- what settlement state exists,
- what residuals remain,
- what evidence supports each conclusion.

---

## 5. Reconciliation Output

Define:

Gamma_Q
:
(H_t,X_t,S_t,R_t,Rho_t,E_t)
->
{
    Q_RECONCILED,
    Q_DIVERGENT,
    Q_INDETERMINATE
}

---

## 6. Q_RECONCILED

Q_RECONCILED means:

the relevant execution/remediation history and present state are sufficiently explained and internally represented.

It does not require zero residual divergence.

A system may be reconciled while still divergent.

Example:

a non-reversible effect is fully understood,
its history is evidenced,
its current divergence is explicit,
and no further valid remediation exists.

The history may be reconciled even though economic restoration did not occur.

---

## 7. Q_DIVERGENT

Q_DIVERGENT means:

a known unresolved state divergence remains.

Examples:

- unresolved quantity deficit,
- unresolved ownership mismatch,
- unresolved obligation,
- persistent settlement divergence,
- failed compensation,
- partial reversal,
- non-reversible effect.

Divergence may be fully evidenced.

Therefore:

DIVERGENT
does not imply
INDETERMINATE.

---

## 8. Q_INDETERMINATE

Q_INDETERMINATE means available evidence does not support a reliable reconciliation classification.

Indeterminate reconciliation must not be converted into successful reconciliation merely because current balances appear plausible.

---

## 9. Reconciliation Completeness

A reconciliation record must identify:

- root execution,
- remediation lineage,
- current state,
- settlement state,
- current residual signature,
- unresolved dimensions,
- contradictory dimensions,
- non-reversible dimensions,
- evidence references,
- final reconciliation class.

---

## 10. No Historical Rewrite

Reconciliation explains history.

It does not rewrite it.

A reconciled result cannot erase:

- partial execution,
- compensation,
- reversal,
- failed remediation,
- intervening events,
- continuity breaks.
