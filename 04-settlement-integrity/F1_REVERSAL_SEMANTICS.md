# F1 — Canonical Reversal Semantics

## Purpose

Reversal is a new financially consequential execution intended to move current economic state toward an explicitly identified prior-state target or reversal relation.

Reversal is not:

- automatic rollback,
- compensation,
- deletion of the original execution,
- guaranteed restoration,
- inherited authority,
- universally possible.

---

## 1. Prior-State Reference

Let:

X_p

be a prior economic state reference relevant to an originating execution e_0.

Let:

X_t

be current observed economic state when reversal is considered.

A reversal target is derived relative to both:

X_p

and:

X_t.

The existence of X_p does not establish that X_p is still reachable, admissible, or desirable.

---

## 2. Reversal Target

Define:

T_R

as an explicitly governed reversal target.

T_R may contain:

- prior-state references,
- dimensions to be reversed,
- dimensions excluded from reversal,
- intervening-state constraints,
- permissible residual divergence,
- authority requirements,
- admissibility constraints,
- evidence requirements.

Reversal is target-relative.

---

## 3. Reversal Execution

A reversal execution r is a new FinancialExecutionEvent:

r : X_t -> X_(t+1)

It requires:

- unique execution identity,
- current authority,
- independent admission,
- current state,
- scope,
- affected-resource references,
- originating-event reference,
- prior-state target reference,
- intervening-history reference,
- evidence lineage.

---

## 4. Reversal Is Not Rollback

Rollback commonly implies restoration of a prior technical state by undoing an operation.

F1 reversal does not assume that such an inverse exists.

Therefore:

Reversal != Rollback

A reversal may require new economic actions rather than inverse machine operations.

---

## 5. Reversal Is Not Compensation

Compensation attempts to satisfy a remediation target.

Reversal specifically attempts to restore selected prior-state relations or values.

Therefore:

Compensation != Reversal

A compensation target may be valid where reversal is impossible.

---

## 6. Reversal Is Not Historical Restoration

Even if:

X_(t+1) = X_p

under some state comparison,

the historical record is:

H_(t+1)
=
H_p
appended with
originating execution
intervening events
reversal execution

not:

H_(t+1) = H_p.

---

## 7. Dimension-Level Reversibility

For each dimension d_i define:

Rev_i(X_p_i,X_t_i)

with classification:

REVERSIBLE

CONDITIONALLY_REVERSIBLE

NON_REVERSIBLE

STALE_TARGET

CONFLICTED_BY_INTERVENING_STATE

INDETERMINATE

Reversibility is typed.

No universal inverse operator is assumed.

---

## 8. Quantitative Reversal

A quantitative dimension may support an inverse delta where:

- the unit is unchanged,
- resources remain available,
- no intervening constraint prevents the inverse,
- the inverse itself is admissible.

Arithmetic invertibility does not establish execution authority.

---

## 9. Relational Reversal

For ownership or custody, reversal requires restoration of a relation.

Example:

A -> B

followed by reversal target:

B -> A.

This may be impossible if B no longer controls the asset.

Thus relational reversal is not equivalent to arithmetic negation.

---

## 10. Discrete-State Reversal

A prior discrete state may not be reachable.

Example:

OBLIGATION_DISCHARGED

may not validly transition back to:

OBLIGATION_OPEN

under the applicable model.

Such a dimension is NON_REVERSIBLE unless an explicit valid transition exists.

---

## 11. Set-Valued Reversal

Reversal of affected-party or resource sets must account for:

- members added by the originating execution,
- members removed,
- members changed by intervening legitimate events.

Blind restoration of the old set is prohibited.

---

## 12. Graph-State Reversal

A propagated state graph may not admit exact inversion.

Intervening downstream state may have produced new dependencies.

Reversal must preserve explicitly valid intervening graph mutations.

---

## 13. Intervening Legitimate Mutation

Let:

M = {m_1,...,m_k}

be legitimate state mutations occurring after e_0 but before reversal r.

Reversal SHALL NOT silently erase M.

The reversal target must distinguish:

originating-effect state

from:

valid intervening state.

---

## 14. Stale Prior State

A prior state X_p is stale when current conditions make restoration inappropriate or invalid.

Examples:

- resource no longer exists,
- counterparty changed,
- obligation lawfully discharged,
- ownership validly transferred again,
- current policy prohibits restoration,
- jurisdiction changed.

STALE_TARGET prevents classification as exact reversal.

---

## 15. Non-Reversible Dimensions

A dimension may be intrinsically or contextually non-reversible.

Examples may include:

- historical record,
- consumed resource,
- externally finalized state,
- expired entitlement,
- irreversible disclosure,
- certain completed third-party effects.

F1 does not assume all financial dimensions are reversible.

---

## 16. Exact Reversal

Exact reversal occurs only when every required reversible target dimension reaches its valid T_R state and:

- no prohibited new divergence exists,
- no legitimate intervening mutation is erased,
- no required dimension remains unresolved.

Exact reversal is target-relative.

It is not historical restoration.

---

## 17. Partial Reversal

Partial reversal occurs when:

- at least one required reversal dimension reaches or moves toward T_R,
- at least one required reversal dimension remains unresolved.

Partial reversal may require further remediation.

---

## 18. Over-Reversal

Over-reversal occurs when reversal exceeds the valid target.

Examples:

- excessive value transferred back,
- additional assets reversed,
- too many obligations reopened,
- unrelated counterparties affected.

---

## 19. Wrong-Object Reversal

Wrong-object reversal occurs when reversal affects a resource, account, obligation, asset, or relation other than the authorized reversal target.

This is not exact or partial success.

---

## 20. Conflicted Reversal

A reversal is conflicted when satisfying T_R would invalidate or erase a legitimate intervening mutation.

Such conflict must remain explicit.

---

## 21. Impossible Reversal

Define:

ReversalImpossible(T_R,X_t)

when one or more required dimensions are NON_REVERSIBLE and no valid reversal target remains.

In this case:

ReversalImpossible
does not imply
CompensationImpossible.

Compensation may remain an available remediation class.

---

## 22. Recursive Reversal

If reversal r_n itself becomes partial:

Effect(r_n) = E_REVERSAL_PARTIAL

then a new remediation event r_(n+1) or compensation event c_(n+1) may be considered.

Every new consequential execution requires independent authority and admission.

---

## 23. Reversal Success

RevSuccess(r,T_R)

requires:

1. independent authorization/admission,
2. execution evidence,
3. observed resulting state,
4. all required reversal predicates satisfied,
5. no prohibited intervening-state destruction,
6. no prohibited new divergence,
7. no unresolved required dimensions.

RevSuccess does not imply continuity preserved.

---

## 24. Historical Preservation

A reversal adds a new historical event.

It does not remove the event it reverses.

Therefore:

Reversed
!=
NeverOccurred.
