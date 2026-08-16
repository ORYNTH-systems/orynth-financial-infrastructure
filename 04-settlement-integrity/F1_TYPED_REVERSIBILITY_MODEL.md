# F1 — Typed Reversibility Model

For each effect dimension d_i define:

Rev_i(X_p_i,X_t_i)

returning one of:

REVERSIBLE

CONDITIONALLY_REVERSIBLE

NON_REVERSIBLE

STALE_TARGET

CONFLICTED_BY_INTERVENING_STATE

INDETERMINATE

---

## Quantitative

Potentially reversible through a typed inverse or target delta where the current state supports it.

---

## Relational

Potentially reversible only where the prior relation can validly be re-established.

---

## Discrete State

Reversible only if a defined valid transition exists from current state toward the prior target state.

---

## Set-Valued

Reversible only after separating originating changes from legitimate later membership changes.

---

## Graph State

Reversible only where the relevant subgraph can be transformed without invalidating legitimate dependent state.

---

## Ordered Sequence

A sequence index is not generally reversible merely because a prior index existed.

A compensating or corrective later entry may be possible while historical sequence remains append-only.

---

## Opaque Typed

Reversibility is determined by a domain-specific validator.

No generic inverse is assumed.

---

## Global Reversibility

A reversal target is globally EXACTLY_REVERSIBLE only if all required target dimensions are REVERSIBLE under current conditions.

If at least one required dimension is NON_REVERSIBLE:

exact reversal is unavailable.

If some dimensions remain reversible:

partial or alternative remediation may remain possible.
