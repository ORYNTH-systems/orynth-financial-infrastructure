# F1 — Canonical Compensation Semantics

## Purpose

Compensation is a new financially consequential execution intended to address an identified residual divergence.

Compensation is not:

- automatic rollback,
- arithmetic negation of the original execution,
- historical erasure,
- implicit authority,
- necessarily exact restoration.

---

## 1. Original Execution

Let e_0 be an originating financial execution.

Let:

I(e_0)

be its intended effect vector.

Let:

O(e_0,t)

be its observed effect vector at time t.

---

## 2. Typed Residual Divergence

For each effect dimension d_i define:

rho_i(I_i,O_i)

as the typed residual relation between intended and observed effect.

The residual operator is dimension-specific.

### Quantitative dimensions

Where subtraction is semantically valid:

rho_i(I_i,O_i) = I_i - O_i

Example:

intended = 100
observed = 60

residual = 40

### Relational dimensions

For ownership or custody:

rho_i(I_i,O_i)

is a relation mismatch description.

Example:

intended owner = B
observed owner = C

Residual is not:

B - C

It is:

OWNER_MISMATCH(expected=B, observed=C)

### Discrete state dimensions

For obligations:

rho_i(I_i,O_i)

records the unresolved state transition.

Example:

intended = DISCHARGED
observed = OPEN

Residual:

STATE_DIVERGENCE(OPEN -> DISCHARGED)

### Set-valued dimensions

Residual may include:

missing intended members

and:

unexpected observed members.

### Graph dimensions

Residual may include:

missing nodes,
missing edges,
unexpected nodes,
unexpected edges,
incorrect propagation paths.

---

## 3. Residual Divergence Vector

Define:

Rho(e_0,t)
=
(
    rho_1(I_1,O_1),
    ...,
    rho_n(I_n,O_n)
)

This is a typed residual vector.

It is not necessarily numeric.

---

## 4. Current-State Principle

Compensation is computed against current observed state, not merely against original intent.

Let:

X_t

be current economic state.

Let:

T_C

be an admissible compensation target.

A compensation execution c proposes:

c : X_t -> X_(t+1)

The purpose of c is to reduce or resolve an identified divergence with respect to T_C.

---

## 5. Compensation Is Not Negation

In general:

c != -e_0

and:

Effect(c) != -Effect(e_0)

because:

- intervening state may have changed,
- relational state may not support negation,
- obligations may require distinct discharge actions,
- assets may no longer be available,
- custody may differ,
- third parties may now be affected,
- legal/technical constraints may prohibit restoration,
- the target may be compensation rather than restoration.

---

## 6. Compensation Target

A compensation target T_C must explicitly identify:

- affected dimensions,
- target values or relations,
- allowed residual state,
- authority requirements,
- admissibility constraints,
- preservation requirements,
- evidence requirements.

No implicit "restore everything" target is assumed.

---

## 7. Compensation Execution

A compensation execution c is a new FinancialExecutionEvent.

It requires:

- unique execution identity,
- initiating actor,
- authority reference,
- current admission,
- current state,
- scope,
- execution boundary,
- evidence lineage,
- originating-event reference.

The fact that e_0 requires remediation does not grant authority for c.

---

## 8. Exact Compensation

Exact compensation occurs when:

for every required compensation dimension d_i,

rho_i(T_C_i,O_after_i) = RESOLVED

and no new prohibited divergence is created.

Exact compensation is target-relative.

It does not mean historical restoration.

---

## 9. Partial Compensation

Partial compensation occurs when:

at least one required compensation dimension improves toward T_C

while at least one required dimension remains unresolved.

Partial compensation may itself require further remediation.

---

## 10. Over-Compensation

Over-compensation occurs when compensation exceeds its target on any dimension supporting meaningful excess.

Examples:

- excessive monetary credit,
- excess asset quantity,
- discharge of additional obligations,
- unintended expansion of affected-party set.

Over-compensation is not exact compensation.

---

## 11. Wrong-Dimension Compensation

Wrong-dimension compensation occurs when compensation changes a dimension that does not resolve the relevant divergence.

Example:

Original divergence:
asset ownership incorrect.

Compensation:
cash payment only.

A cash payment may constitute a valid negotiated remedy under a defined target.

It does not automatically resolve ownership divergence.

The target must specify whether substitution is admissible.

---

## 12. New-Divergence Compensation

Compensation creates new divergence when the compensating execution introduces additional inconsistency.

Example:

Compensation corrects cash balance

but transfers custody to an unauthorized party.

The resulting state is not classified as exact compensation.

---

## 13. Projection-Equivalent Compensation

Let pi be a projection over selected economic dimensions.

It may be true that:

pi(X_after) = pi(T_C)

while:

X_after != T_C

and:

History_after != History_before.

Thus compensation can restore projected economic equivalence without restoring complete state or history.

---

## 14. Recursive Compensation

If compensation c_n becomes partial:

Effect(c_n) = E_COMPENSATING_PARTIAL

then a new remediation execution c_(n+1) may be proposed.

The new execution has:

depth(c_(n+1)) = depth(c_n) + 1

and requires independent authority and admission.

No inherited authorization from c_n is assumed.

---

## 15. Compensation Success

Compensation success is target-relative.

Define:

CompSuccess(c,T_C)

only when:

1. c was independently authorized/admitted,
2. execution evidence exists,
3. resulting state is observable,
4. all required target dimensions satisfy their residual-resolution predicates,
5. prohibited new divergence is absent,
6. unresolved required dimensions are absent.

This does not establish preserved continuity.

---

## 16. Compensation Failure

Compensation may fail through:

- zero compensating effect,
- partial compensating effect,
- over-compensation,
- wrong-dimension compensation,
- contradictory compensation,
- new divergence,
- admission failure,
- execution interruption,
- indeterminate effect.

---

## 17. Historical Preservation

Let H(e_0) be historical execution lineage.

After compensation c:

H' = H(e_0) appended with c

not:

H' = history in which e_0 is erased.

Compensation modifies current state.

It does not rewrite historical fact.
