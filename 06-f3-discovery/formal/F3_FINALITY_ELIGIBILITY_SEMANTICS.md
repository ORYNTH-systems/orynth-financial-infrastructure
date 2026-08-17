# F3 Finality Eligibility Semantics

Status: FORMALIZED

## Eligibility Predicate

Let:

FinalityEligible(Ψ_t, q)

be true iff every applicable requirement below is satisfied.

## Required Conjuncts

FE-01 — Obligation Condition

Applicable obligation requirements are satisfied.

Where full satisfaction is required:

ResidualExists = false

---

FE-02 — Custody Condition

Required custody state is valid.

Custody possession alone is insufficient.

CustodyValid must hold.

---

FE-03 — Authority Condition

Applicable authority is valid and current.

Authority cannot be inferred from:

- execution;
- consensus;
- possession;
- evidence;
- ledger state;
- historical authority.

---

FE-04 — Scope Condition

The requested finality classification lies within current applicable scope.

Scope validity is request-relative.

---

FE-05 — Temporal Condition

Applicable authority, evidence, and scope remain temporally current for the decision.

Historical validity alone is insufficient for current finality.

---

FE-06 — Evidence Condition

The evidence required by the Finality Requirement Set is admissible and sufficient.

Evidence sufficiency does not create authority.

---

FE-07 — Conflict Condition

No unresolved applicable Finality Conflict exists.

If an unresolved conflict exists:

FinalityEligible = false

---

FE-08 — Contradiction Condition

No current blocking contradiction exists.

Post-finality contradiction must be explicitly processed if discovered after classification.

---

FE-09 — Transition Condition

The requested transition must be valid from the current state.

Endpoint desirability does not create transition validity.

---

FE-10 — Non-Vacuity Condition

Finality eligibility must have at least one applicable requirement.

An empty requirement set cannot produce finality.

## Conjunctive Rule

FinalityEligible(Ψ_t,q) iff

FE-01
AND FE-02
AND FE-03
AND FE-04
AND FE-05
AND FE-06
AND FE-07
AND FE-08
AND FE-09
AND FE-10

No requirement may compensate for the failure of another.

## Blocking Conditions

FinalityBlocked(Ψ_t,q) is true if any applicable blocking condition holds.

Blocking conditions include:

FB-01 unresolved obligation residual

FB-02 invalid custody state

FB-03 absent or invalid custody authority

FB-04 stale authority

FB-05 invalid scope

FB-06 insufficient evidence

FB-07 unresolved finality conflict

FB-08 post-finality contradiction requiring revalidation

FB-09 invalid requested transition

FB-10 vacuous finality requirement set

## Decision Semantics

If FinalityEligible = true:
    D_F may return F3-ADMIT

If any blocking condition holds:
    D_F returns F3-BLOCK

If evidence or authority cannot yet be resolved:
    D_F may return F3-DEFER

If current classification must be reconsidered:
    D_F may return F3-REVALIDATE

If a previously closed state is validly reopened:
    D_F may return F3-REOPEN

## Non-Compensation Rule

No valid factor compensates for an invalid required factor.

Examples:

valid consensus + invalid authority != finality

valid custody possession + invalid custody authority != finality

complete execution + unresolved obligation residual != finality

sufficient evidence + invalid scope != finality

historical authority + expired current authority != current finality

## Finality / Closure Separation

FinalityEligible != ConsequentiallyClosed

Finality classification is not equivalent to consequential closure.

A separate closure eligibility determination and transition is required.
