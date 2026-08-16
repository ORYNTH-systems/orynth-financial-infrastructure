# F1 — Multidimensional Partial-Effect Formalization

## Purpose

This model defines what constitutes partial financial effect without reducing all financial mutation to a single scalar quantity.

Financial execution can mutate multiple heterogeneous state dimensions simultaneously.

---

## 1. Effect Domain

Let D be the finite set of execution-relevant effect dimensions.

For a financially consequential execution e:

D(e) = {
    d_1,
    d_2,
    ...,
    d_n
}

Possible dimensions include:

- cash balance,
- asset ownership,
- obligation state,
- settlement obligation,
- ledger state,
- custody state,
- counterparty state,
- reservation/lock state,
- collateral state,
- entitlement state,
- account state.

The domain is typed.

No assumption is made that all dimensions are numerically commensurable.

---

## 2. Intended Effect Vector

Define the intended effect vector:

I(e) = (I_1, I_2, ..., I_n)

where each I_i belongs to its own typed effect domain T_i.

Therefore:

I(e) in T_1 x T_2 x ... x T_n

Examples:

I_cash may be a monetary delta.

I_ownership may be a transfer relation.

I_obligation may be a state transition from OPEN to DISCHARGED.

I_custody may be a custody-control relation.

I_ledger may be a ledger-state mutation.

---

## 3. Observed Effect Vector

Define the observed effect vector:

O(e,t) = (O_1, O_2, ..., O_n)

at observation time t.

Each O_i must be evaluated against the corresponding intended dimension I_i.

Observed effect is evidence-relative.

An unavailable observation must not be silently treated as zero.

---

## 4. Dimension Comparison Relation

For each dimension d_i define a typed comparison relation:

C_i(O_i, I_i)

with possible results:

NO_EFFECT

PARTIAL_MATCH

FULL_MATCH

OVER_EFFECT

CONTRADICTORY_EFFECT

INDETERMINATE

The comparison relation is dimension-specific.

A monetary amount may use quantitative comparison.

An ownership relation may use relational equality.

An obligation state may use state-transition comparison.

A ledger-state dimension may use sequence/state comparison.

---

## 5. Zero Effect

Define:

ZeroEffect(e)

iff for every relevant dimension d_i:

C_i(O_i,I_i) = NO_EFFECT

and sufficient evidence exists to support that conclusion.

Therefore:

absence of evidence
does not imply
ZeroEffect.

---

## 6. Full Intended Effect

Define:

FullEffect(e)

iff for every required dimension d_i:

C_i(O_i,I_i) = FULL_MATCH

and no dimension is:

OVER_EFFECT,
CONTRADICTORY_EFFECT,
or INDETERMINATE.

---

## 7. Partial Effect

Define:

PartialEffect(e)

when:

1. at least one relevant dimension has non-zero intended-corresponding effect,

AND

2. FullEffect(e) is false,

AND

3. the observed state is not more accurately classified as purely contradictory or indeterminate.

Formally:

exists i:
C_i(O_i,I_i) in {PARTIAL_MATCH, FULL_MATCH}

AND

not FullEffect(e)

AND

exists j:
C_j(O_j,I_j) in {
    NO_EFFECT,
    PARTIAL_MATCH
}

subject to absence of dominant contradictory/indeterminate conditions.

---

## 8. Mixed Effect

Define:

MixedEffect(e)

when the observed effect includes combinations such as:

- intended effect on one dimension,
- contradictory effect on another,
- over-effect on another,
- unresolved effect on another.

Mixed effect is not reducible to ordinary partial effect without losing information.

---

## 9. Indeterminate Effect

Define:

IndeterminateEffect(e)

when required observations are insufficient to classify the effect vector safely.

Indeterminate effect must remain distinct from zero effect.

---

## 10. Componentwise Ordering

Where a dimension supports an ordering <=_i:

0_i <=_i O_i <=_i I_i

may be meaningful.

For the complete vector define a product partial order only where all participating dimensions expose valid typed orderings.

Thus:

O <= I

means:

for every ordered dimension i:

O_i <=_i I_i

This is a partial order, not a universal scalar metric.

---

## 11. Partial Quantity

Partial quantity occurs when a quantitative dimension satisfies:

0_i <_i O_i <_i I_i

Example:

intended cash transfer = 100

observed cash transfer = 60

This establishes partiality in that dimension only.

It does not alone classify all other dimensions.

---

## 12. Partial Party Coverage

Let P_I be the intended affected-party set.

Let P_O be the observed affected-party set.

Partial party coverage occurs when:

empty != P_O

and

P_O proper-subset P_I

subject to correct direction and effect semantics.

---

## 13. Partial Obligation Discharge

Let obligations be:

B = {b_1,...,b_m}

with intended terminal states I_B.

Partial obligation discharge occurs when:

at least one required obligation reaches intended state

and

at least one required obligation does not.

---

## 14. Partial State Propagation

Let G be an intended propagation graph of dependent state changes.

Partial propagation occurs when the observed mutation subgraph G_O is a proper subgraph of the required intended propagation graph G_I:

G_O proper-subgraph G_I

with at least one consequential intended mutation present.

---

## 15. Contradictory Effect

A contradictory effect exists when observed state is not merely incomplete but conflicts with the intended effect.

Examples:

- wrong counterparty receives the asset,
- obligation increases instead of decreases,
- custody moves to an unauthorized holder,
- ledger mutation records the opposite direction,
- collateral is released when intended effect required locking.

Contradictory effect must not be classified as simple partiality.

---

## 16. Over-Effect

Over-effect occurs where effect magnitude, coverage, scope, or propagation exceeds the intended execution.

Examples:

- 110 transferred when 100 was intended,
- additional accounts mutated,
- excess asset quantity transferred,
- unintended obligations discharged.

Over-effect is not equivalent to completed effect.

---

## 17. Effect Signature

Define the effect signature:

Sigma_E(e,t)
=
(
    C_1(O_1,I_1),
    ...,
    C_n(O_n,I_n)
)

The signature preserves dimension-level outcomes.

The global effect class is derived from Sigma_E but must not erase it.

---

## 18. Global Classification Function

Define:

Gamma_E : Sigma_E -> {
    E_NO_EFFECT,
    E_PARTIAL,
    E_COMPLETED,
    E_MIXED,
    E_INDETERMINATE
}

with remediation-specific extensions handled separately.

Gamma_E must be deterministic for a fixed effect signature and classification policy.

---

## 19. Projection Principle

A projection pi onto one subset of dimensions may show equivalence:

pi(O_a) = pi(O_b)

while complete effect states differ:

O_a != O_b

Therefore financial equivalence under one projection must not be generalized to full state equivalence.

---

## 20. Historical Principle

Effect comparison evaluates what occurred.

It does not authorize remediation.

No result of Gamma_E creates authority.
