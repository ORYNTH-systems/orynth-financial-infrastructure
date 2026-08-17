# Obligation Finality, Custody-State Integrity, and Consequential Financial Closure

## F3 — ORYNTH Financial Infrastructure

Status: CANONICAL RELEASE CANDIDATE

---

## 1. Problem Boundary

# FIN-F3-01B — Exact F3 Problem Boundary

Status: FROZEN

## Canonical F3 Working Title

**Obligation Finality, Custody-State Integrity, and Consequential Financial Closure**

## Position in Suite

F3 follows:

- F1 — Partial Settlement, Compensating Execution, and Economic-State Continuity
- F2 — Distributed Settlement, Multiparty Authority, and Consensus Boundary

F3 owns the next unresolved layer after distributed execution:

**When an obligation has been executed across one or more actors or systems, under what conditions may the resulting financial state be treated as final, closed, custody-valid, and no longer subject to ordinary consequential continuation?**

F3 does not treat finality as a synonym for:

- execution;
- effect occurrence;
- atomic completion;
- consensus;
- reconciliation;
- custody possession;
- local ledger closure;
- irreversible history;
- continuity preservation.

## Central Separation

execution
!= effect occurrence
!= obligation satisfaction
!= custody validity
!= settlement completion
!= finality
!= irreversibility
!= historical identity
!= continuity preservation

## F3 Core Problem

F2 establishes that agreement, consensus, authority, admissibility, execution, effect occurrence, atomic completion, finality, reconciliation, and continuity are distinct.

F3 now formalizes the **financial closure boundary** itself.

The core question is not merely whether execution occurred.

The core question is:

**What conditions must hold before an obligation-bearing financial state can be classified as final across authority, custody, settlement, evidentiary, and consequential dimensions?**

## F3-Owned Objects

F3 uniquely owns formalization of:

1. obligation state;
2. obligation satisfaction state;
3. obligation residual state;
4. closure eligibility;
5. finality requirement state;
6. finality classification;
7. custody-state validity;
8. custody continuity;
9. custody transfer completion;
10. consequential closure;
11. reopenability;
12. post-finality contradiction;
13. finality evidence sufficiency;
14. finality conflict state;
15. finality revocation or invalidation conditions.

## F3 Inherits from F1

F3 inherits without redefining:

- partial effect;
- residual consequence;
- compensation;
- reversal;
- reconciliation;
- economic-state continuity;
- reconstructed continuity;
- historical identity distinctions.

F3 SHALL NOT collapse:

reconciled == final

or

reconstructed == preserved

or

economic equivalence == historical identity

## F3 Inherits from F2

F3 inherits without redefining:

- participant state;
- multiparty authority;
- agreement;
- commitment;
- consensus;
- distributed admissibility;
- execution-leg composition;
- atomicity;
- distributed partial settlement;
- local finality;
- cross-domain finality;
- distributed reconciliation;
- distributed continuity.

F3 SHALL NOT collapse:

AtomicComplete == Final

or

LocalFinal == CrossDomainFinal

or

Consensus == Authority

or

Consensus == Finality

## F3 Primary Invariant Family

FIN-FIN — Finality

Existing repository ownership signal:

F3-F4

F3 therefore owns the **first exact finality / closure architecture**, while F4 may extend finality into later specialized or systemic closure domains.

## F3 Formalization Boundary

F3 SHALL formalize:

- obligation lifecycle;
- obligation satisfaction predicate;
- obligation residual predicate;
- custody validity predicate;
- custody transfer completion predicate;
- finality eligibility predicate;
- finality classification function;
- finality conflict predicate;
- reopenability predicate;
- closure transition relation;
- evidence sufficiency for finality;
- post-finality invalidation conditions.

## F3 Required Non-Implications

At minimum:

execution != finality

effect occurrence != finality

atomic completion != finality

consensus != finality

custody possession != custody authority

custody possession != finality

reconciliation != finality

finality != irreversibility

finality != historical identity

finality != continuity preservation

obligation balance equality != obligation-history identity

closed obligation != impossible future contradiction

## F3 Runtime Boundary

F3 runtime may later implement reference classifiers for:

- obligation state;
- custody state;
- finality eligibility;
- finality classification;
- reopenability;
- contradictory post-finality evidence.

Reference-runtime conformance SHALL remain distinct from formal proof.

## F3 Proof Boundary

F3 SHALL require proof obligations covering:

- finality cannot self-create from execution alone;
- finality cannot self-create from consensus alone;
- custody possession is insufficient for custody authority;
- atomic completion is insufficient for finality;
- reconciliation is insufficient for finality;
- finality is insufficient for irreversibility;
- finality is insufficient for continuity preservation;
- reopened state invalidates prior current-final classification without erasing historical classification;
- post-finality contradiction requires explicit treatment rather than silent state overwrite.

## F3 Adversarial Boundary

F3 SHALL test attempts to manufacture finality from:

- execution completion;
- consensus;
- ledger closure;
- custody possession;
- balance equality;
- reconciliation;
- atomic completion;
- stale evidence;
- conflicting custody records;
- inconsistent obligation records;
- later contradictory consequential effects.

## Explicitly Deferred Beyond F3

F3 does NOT yet own full formalization of:

- liquidity architecture;
- netting architecture;
- collateral architecture;
- default waterfall architecture;
- clearing-house architecture;
- systemic-risk propagation;
- cross-jurisdiction legal finality;
- autonomous treasury authority;
- programmable-finance execution policy;
- digital-asset-specific custody semantics.

Those remain candidates for F4-F8 according to later suite boundary passes.

## Freeze Rule

The F3 problem boundary is frozen as:

**obligation finality + custody-state integrity + consequential financial closure**

subject to inherited F1/F2 semantics and without collapsing finality into execution, consensus, atomic completion, reconciliation, irreversibility, or continuity preservation.

No F3 runtime is frozen here.

No F3 proof is discharged here.

No F3 manuscript is created here.

No F3 release exists here.


---

## 2. Canonical Objects

# F3 Canonical Objects

Status: FORMALIZED

## Core Objects

### F3-O-001 — Financial Obligation

A typed consequential requirement binding one or more parties to a financial performance condition.

An obligation is not equivalent to:

- an instruction;
- an execution;
- a transaction record;
- a ledger entry;
- a payment attempt;
- a settlement result.

---

### F3-O-002 — Obligation Performance

Observed consequential performance against a Financial Obligation.

Performance may be:

- NONE
- PARTIAL
- COMPLETE
- EXCESS
- CONFLICTING
- UNDETERMINED

---

### F3-O-003 — Obligation Residual

The portion or dimension of an obligation not discharged by observed valid performance.

Residual existence does not imply authority to repair, compensate, reverse, or continue execution.

---

### F3-O-004 — Custody State

The currently evidenced state of control, possession, entitlement, or holding with respect to a financial asset or obligation-bearing object.

Custody state is not equivalent to custody authority.

---

### F3-O-005 — Custody Authority

The authority under which a custody state, transfer, mutation, release, or disposition may be treated as admissible.

Possession does not create Custody Authority.

---

### F3-O-006 — Custody Transfer

A transition between custody states involving an asset, entitlement, position, obligation, or governed financial object.

Transfer occurrence is not equivalent to valid transfer completion.

---

### F3-O-007 — Finality Requirement Set

The typed set of conditions required before a specific financial state may be classified as final.

---

### F3-O-008 — Finality Evidence Set

Evidence supporting or contradicting satisfaction of a Finality Requirement Set.

Evidence does not itself create finality.

---

### F3-O-009 — Finality Classification

A classification assigned to a financial state after evaluation against current Finality Requirements and admissible evidence.

---

### F3-O-010 — Consequential Closure

A state in which the governed financial consequence is treated as closed for the relevant request, scope, authority, obligation, and finality domain.

Closure is request-relative and scope-relative.

---

### F3-O-011 — Reopenability State

The current classification of whether a previously closed or final state may validly be reopened under governing rules.

---

### F3-O-012 — Finality Conflict

A conflict in which two or more admissible or purportedly admissible states, records, authorities, or evidence sets yield incompatible finality conclusions.

---

### F3-O-013 — Post-Finality Contradiction

Evidence or state appearing after a finality classification that contradicts one or more conditions required for current finality.

Historical final classification is preserved as historical evidence even when current classification changes.

---

### F3-O-014 — Closure Witness

The reconstructable evidence bundle sufficient to demonstrate why a Consequential Closure classification was reached.

A Closure Witness is evidence of classification, not authority to create classification.


---

## 3. State Algebra

# F3 State Algebra

Status: FORMALIZED

## Obligation State

Let:

O_t ∈ {
    OBLIGATION_ABSENT,
    OBLIGATION_OPEN,
    OBLIGATION_PARTIAL,
    OBLIGATION_SATISFIED,
    OBLIGATION_OVERPERFORMED,
    OBLIGATION_CONFLICTED,
    OBLIGATION_REOPENED,
    OBLIGATION_UNDETERMINED
}

## Custody State

Let:

C_t ∈ {
    CUSTODY_UNESTABLISHED,
    CUSTODY_HELD,
    CUSTODY_TRANSFER_PENDING,
    CUSTODY_TRANSFER_PARTIAL,
    CUSTODY_TRANSFER_COMPLETE,
    CUSTODY_CONFLICTED,
    CUSTODY_INVALID,
    CUSTODY_RECONSTRUCTED
}

## Finality State

Let:

F_t ∈ {
    FINALITY_NOT_EVALUATED,
    FINALITY_INELIGIBLE,
    FINALITY_PENDING,
    FINALITY_LOCAL,
    FINALITY_DOMAIN_COMPLETE,
    FINALITY_CONFLICTED,
    FINALITY_REOPENED,
    FINALITY_INVALIDATED,
    FINALITY_HISTORICAL
}

## Closure State

Let:

K_t ∈ {
    CLOSURE_OPEN,
    CLOSURE_PENDING,
    CLOSURE_ELIGIBLE,
    CLOSURE_COMPLETE,
    CLOSURE_REOPENED,
    CLOSURE_CONFLICTED,
    CLOSURE_INVALIDATED
}

## Composite F3 State

Ψ_t = (
    O_t,
    C_t,
    F_t,
    K_t,
    R_t,
    E_t,
    A_t,
    σ_t,
    τ_t
)

where:

- O_t = obligation state
- C_t = custody state
- F_t = finality state
- K_t = consequential closure state
- R_t = remaining obligation residual
- E_t = admissible evidence state
- A_t = applicable authority state
- σ_t = applicable scope
- τ_t = temporal validity context


---

## 4. Relation Algebra

# F3 Relation Algebra

Status: FORMALIZED

## Core Relations

### ObligationSatisfied

ObligationSatisfied(o, e, σ, τ)

True only when admissible evidence establishes satisfaction of the applicable obligation under current scope and temporal validity.

---

### ResidualExists

ResidualExists(o, e)

True when an obligation remains unsatisfied in at least one applicable dimension.

---

### CustodyValid

CustodyValid(c, a, σ, τ)

True only when current custody state is supported by valid authority, scope, and temporal conditions.

---

### CustodyTransferComplete

CustodyTransferComplete(c0, c1, e)

Transfer occurrence alone is insufficient.

Completion requires all applicable custody transition requirements to be discharged.

---

### FinalityEligible

FinalityEligible(Ψ_t)

True only if every applicable finality requirement is currently satisfied.

---

### Final

Final(Ψ_t)

Final(Ψ_t) iff:

1. FinalityEligible(Ψ_t);
2. no unresolved applicable Finality Conflict exists;
3. evidence sufficiency is satisfied;
4. required custody predicates are satisfied;
5. required obligation predicates are satisfied;
6. applicable authority remains current;
7. applicable scope remains valid;
8. no blocking contradiction exists.

---

### ConsequentiallyClosed

ConsequentiallyClosed(Ψ_t)

True only when the request-relative financial consequence may validly transition from active consequential processing into closure.

---

### Reopenable

Reopenable(Ψ_t, q)

Determines whether a previously closed or final state may validly re-enter an active consequential state for request q.

---

### FinalityConflictExists

FinalityConflictExists(Ψ_t)

True when admissible current evidence or authority states imply mutually incompatible finality classifications.

---

### PostFinalityContradiction

PostFinalityContradiction(Ψ_t, e_new)

True when newly admitted evidence contradicts a predicate required by the current finality classification.


---

## 5. Non-Equivalence Algebra

# F3 Non-Equivalence Algebra

Status: FORMALIZED

The following are mandatory semantic separations.

execution != finality

effect occurrence != obligation satisfaction

obligation satisfaction != custody validity

custody possession != custody authority

custody possession != finality

custody transfer occurrence != custody transfer completion

atomic completion != finality

consensus != finality

reconciliation != finality

balance equality != historical identity

finality != irreversibility

finality != continuity preservation

finality != historical identity

finality != consequential closure

consequential closure != impossibility of reopening

reopening != erasure of historical finality

post-finality contradiction != historical non-occurrence

evidence of finality != authority to declare finality


---

## 6. Transition System

# F3 Transition System

Status: FORMALIZED

## Principle

Finality classification and state transition are distinct.

A decision that a state is eligible for finality does not itself perform a finality transition.

Likewise:

finality decision != transition existence != resulting state

## Composite State

Ψ_t = (
    O_t,
    C_t,
    F_t,
    K_t,
    R_t,
    E_t,
    A_t,
    σ_t,
    τ_t
)

## Decision Function

Let:

D_F : Ψ × Q -> {
    F3-ADMIT,
    F3-BLOCK,
    F3-DEFER,
    F3-REVALIDATE,
    F3-REOPEN
}

D_F is total over admissible decision requests.

## Transition Relation

Let:

Δ_F : Ψ × Q ⇀ Ψ

Δ_F is partial.

Δ_F(Ψ,q) is defined only when the applicable decision authorizes a transition.

## Core Transition Classes

F3-T-001
OBLIGATION_OPEN -> OBLIGATION_PARTIAL

F3-T-002
OBLIGATION_PARTIAL -> OBLIGATION_SATISFIED

F3-T-003
OBLIGATION_SATISFIED -> OBLIGATION_REOPENED

F3-T-004
CUSTODY_UNESTABLISHED -> CUSTODY_HELD

F3-T-005
CUSTODY_HELD -> CUSTODY_TRANSFER_PENDING

F3-T-006
CUSTODY_TRANSFER_PENDING -> CUSTODY_TRANSFER_PARTIAL

F3-T-007
CUSTODY_TRANSFER_PENDING -> CUSTODY_TRANSFER_COMPLETE

F3-T-008
CUSTODY_TRANSFER_PARTIAL -> CUSTODY_TRANSFER_COMPLETE

F3-T-009
CUSTODY_TRANSFER_COMPLETE -> CUSTODY_CONFLICTED

F3-T-010
FINALITY_NOT_EVALUATED -> FINALITY_INELIGIBLE

F3-T-011
FINALITY_NOT_EVALUATED -> FINALITY_PENDING

F3-T-012
FINALITY_PENDING -> FINALITY_LOCAL

F3-T-013
FINALITY_LOCAL -> FINALITY_DOMAIN_COMPLETE

F3-T-014
FINALITY_PENDING -> FINALITY_CONFLICTED

F3-T-015
FINALITY_LOCAL -> FINALITY_CONFLICTED

F3-T-016
FINALITY_DOMAIN_COMPLETE -> FINALITY_REOPENED

F3-T-017
FINALITY_DOMAIN_COMPLETE -> FINALITY_INVALIDATED

F3-T-018
FINALITY_REOPENED -> FINALITY_PENDING

F3-T-019
FINALITY_INVALIDATED -> FINALITY_HISTORICAL

F3-T-020
CLOSURE_OPEN -> CLOSURE_PENDING

F3-T-021
CLOSURE_PENDING -> CLOSURE_ELIGIBLE

F3-T-022
CLOSURE_ELIGIBLE -> CLOSURE_COMPLETE

F3-T-023
CLOSURE_COMPLETE -> CLOSURE_REOPENED

F3-T-024
CLOSURE_COMPLETE -> CLOSURE_CONFLICTED

F3-T-025
CLOSURE_COMPLETE -> CLOSURE_INVALIDATED

## Transition Constraints

No transition to FINALITY_LOCAL or FINALITY_DOMAIN_COMPLETE may occur solely because:

- execution completed;
- effects occurred;
- consensus formed;
- reconciliation completed;
- balances became equal;
- custody is physically possessed;
- an atomic transaction completed.

No transition to CLOSURE_COMPLETE may occur merely because FINALITY_DOMAIN_COMPLETE is observed.

Closure requires its own eligibility and transition decision.

## Historical Preservation

Reopening or invalidation does not erase the earlier classification event.

Historical finality must remain reconstructable.

## Failure Semantics

A blocked finality decision produces no finality transition.

A deferred finality decision produces no finality transition.

An undefined transition must not be represented as successful execution.


---

## 7. Finality Eligibility Semantics

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


---

## 8. Positive Proof Discharge

# F3 Positive Proof Discharge

Status: DISCHARGED

## Proof Doctrine

These arguments discharge only the stated formal or structural obligations.

They do not establish runtime conformance.

---

## F3-PO-014 — Unresolved Finality Conflict Blocks Current Finality

Given:

FinalityEligible requires FE-07.

FE-07 requires no unresolved applicable Finality Conflict.

Therefore:

FinalityConflictExists = true
=> FE-07 = false
=> FinalityEligible = false.

Thus an unresolved applicable finality conflict blocks current finality.

DISCHARGED.

---

## F3-PO-015 — Invalid Required Custody State Blocks Current Finality

Given:

FinalityEligible requires FE-02.

FE-02 requires CustodyValid.

Therefore:

CustodyValid = false
=> FE-02 = false
=> FinalityEligible = false.

DISCHARGED.

---

## F3-PO-016 — Required Obligation Residual Blocks Current Finality

Where full obligation satisfaction is required:

ResidualExists = true
=> FE-01 = false
=> FinalityEligible = false.

DISCHARGED.

---

## F3-PO-017 — Invalid Authority Blocks Current Finality

FE-03 requires applicable authority to be valid and current.

Therefore:

AuthorityValid = false
OR AuthorityCurrent = false
=> FE-03 = false
=> FinalityEligible = false.

DISCHARGED.

---

## F3-PO-018 — Invalid Scope Blocks Current Finality

FE-04 requires valid applicable scope.

Therefore:

ScopeValid = false
=> FE-04 = false
=> FinalityEligible = false.

DISCHARGED.

---

## F3-PO-019 — Current Finality Requires Reconstructable Closure Witness

Finality classification requires sufficient admissible evidence.

The closure witness records the evidence and governing predicates supporting that classification.

Therefore every supported final classification must be reconstructable through a closure witness.

DISCHARGED as traceability obligation.

---

## F3-PO-020 — Closure Witness Cannot Create Authority

Closure Witness is defined as evidence of classification.

Custody Authority and applicable finality authority are separate objects.

Therefore existence of a Closure Witness does not entail authority.

DISCHARGED.

---

## F3-PO-021 — Reopening Preserves Historical Finality Evidence

The transition model explicitly separates:

FINALITY_DOMAIN_COMPLETE
-> FINALITY_REOPENED

from historical record destruction.

Historical finality remains reconstructable.

Therefore reopening changes current classification without erasing the historical classification event.

DISCHARGED.

---

## F3-PO-022 — Invalidation Preserves Prior Classification History

The transition:

FINALITY_DOMAIN_COMPLETE
-> FINALITY_INVALIDATED
-> FINALITY_HISTORICAL

preserves prior classification as historical state.

Therefore invalidation does not rewrite historical occurrence.

DISCHARGED.

---

## F3-PO-023 — Post-Finality Contradiction Does Not Erase Historical Occurrence

A contradiction discovered at t+1 changes the current evidentiary or finality state.

It does not imply that the earlier classification event at t did not occur.

Therefore:

PostFinalityContradiction
!= historical non-occurrence.

DISCHARGED.

---

## F3-PO-024 — Closure Requires Eligibility Rather Than Endpoint Equality

The transition system separates:

decision
!= transition
!= resulting state.

CLOSURE_COMPLETE is reachable only through an admitted closure transition.

Observing an endpoint-equivalent financial state does not establish the existence of a valid closure transition.

DISCHARGED.

---

## F3-PO-025 — Reopening Requires Explicit Admissible Transition

CLOSURE_COMPLETE
-> CLOSURE_REOPENED

and

FINALITY_DOMAIN_COMPLETE
-> FINALITY_REOPENED

are explicit governed transitions.

Reopening is not inferred solely from new activity.

DISCHARGED.


---

## 9. Counterexample Discharge

# F3 Counterexample Discharge

Status: DISCHARGED

## Counterexample Doctrine

A counterexample discharges only the corresponding non-implication.

It does not prove a stronger positive implication.

---

## CE-01 — Execution Complete But Non-Final

State:

execution = complete
authority = expired
finality = blocked

Therefore:

execution != finality

Discharges F3-PO-001 and supports F3-PO-026.

---

## CE-02 — Effect Occurred But Obligation Unsatisfied

State:

required obligation = 100
valid observed effect = 60
residual = 40

Therefore:

effect occurrence != obligation satisfaction

Discharges F3-PO-002.

---

## CE-03 — Obligation Satisfied But Custody Invalid

State:

obligation satisfaction = true
custody transfer record = present
custody authority = invalid

Therefore:

obligation satisfaction != custody validity

Discharges F3-PO-003.

---

## CE-04 — Possession Without Custody Authority

State:

party physically or cryptographically controls asset
applicable custody authority = absent

Therefore:

custody possession != custody authority

Discharges F3-PO-004 and F3-PO-030.

---

## CE-05 — Possession Without Finality

State:

custody possession = true
finality conflict = unresolved

Therefore:

custody possession != finality

Discharges F3-PO-005.

---

## CE-06 — Transfer Occurred But Transfer Not Complete

State:

one custody leg executed
required receiving acknowledgement absent

Therefore:

custody transfer occurrence != custody transfer completion

Discharges F3-PO-006.

---

## CE-07 — Atomic Completion But Non-Final

State:

all execution legs complete atomically
applicable finality authority = stale

Therefore:

atomic completion != finality

Discharges F3-PO-007 and F3-PO-028.

---

## CE-08 — Consensus But Non-Final

State:

all participating nodes agree
required external authority = absent

Therefore:

consensus != finality

Discharges F3-PO-008 and F3-PO-027.

---

## CE-09 — Reconciled But Non-Final

State:

records reconcile numerically
custody evidence remains conflicted

Therefore:

reconciliation != finality

Discharges F3-PO-009 and F3-PO-029.

---

## CE-10 — Final But Reversible

State:

current finality requirements satisfied
governing framework permits later authorized reversal

Therefore:

finality != irreversibility

Discharges F3-PO-010 and F3-PO-031.

---

## CE-11 — Final But Continuity Not Preserved

State:

current finality classification valid
historical chain reconstructed after discontinuity

Therefore:

finality != continuity preservation

Discharges F3-PO-011 and F3-PO-032.

---

## CE-12 — Final But Historical Identity Different

State:

economic endpoint matches prior amount
intervening compensated path differs historically

Therefore:

finality != historical identity

Discharges F3-PO-012.

---

## CE-13 — Final But Not Consequentially Closed

State:

settlement state satisfies finality requirements
separate consequential obligation remains open

Therefore:

finality != consequential closure

Discharges F3-PO-013.

---

## CE-14 — Closed But Reopenable

State:

closure = complete
new admissible contradiction activates explicit reopen transition

Therefore:

consequential closure != impossibility of reopening

Discharges F3-PO-033.

---

## CE-15 — Historically Final Then Invalidated

State at t:

FINALITY_DOMAIN_COMPLETE

New admissible evidence at t+1 contradicts a required finality predicate.

Current state becomes FINALITY_INVALIDATED while historical finality remains recorded.

Therefore:

post-finality contradiction != historical non-occurrence

Discharges F3-PO-034.


---

## 10. Claim-Class Doctrine

Current F3 claim state:

- FORMALLY-PROVED: 12
- COUNTEREXAMPLE-DISCHARGED: 22
- REFERENCE-RUNTIME-CONFORMANT: 6
- OPEN: 0

The following distinctions are mandatory:

formal proof != counterexample discharge

formal proof != runtime conformance

counterexample discharge != runtime conformance

evidence != authority

finality != irreversibility

finality != continuity preservation

finality != historical identity

finality != consequential closure

---

## 11. Registry Status Doctrine

# F3 Registry Status Doctrine

Status: FROZEN

## Purpose

This doctrine distinguishes registration-time state from current discharge state.

## Originating Registries

The following registries preserve the status assigned when the invariant or proof obligation was created:

- 03-registries/F3_INVARIANT_REGISTER.csv
- 03-registries/F3_PROOF_OBLIGATION_REGISTRY.csv

Their OPEN value means:

**OPEN AT REGISTRATION**

It does not represent the current discharge state.

These registries are historical definition ledgers and SHALL NOT be rewritten to collapse initial registration state into later disposition.

## Current Disposition Authority

Current proof / claim disposition is owned by:

- 03-registries/F3_PROOF_DISCHARGE_REGISTRY.csv

Current closure summary is owned by:

- 03-registries/F3_RUNTIME_PROOF_CLOSURE.csv

Current F3 disposition:

- FORMALLY-PROVED: 12
- COUNTEREXAMPLE-DISCHARGED: 22
- REFERENCE-RUNTIME-CONFORMANT: 6
- OPEN: 0
- TOTAL: 40

## Status Separation

registration-time OPEN
!= current OPEN

proof obligation definition
!= proof disposition

formal proof
!= counterexample discharge

formal proof
!= runtime conformance

counterexample discharge
!= runtime conformance

## Release Rule

F3 release eligibility SHALL be determined from the current discharge and closure registries, not from the originating registration-time OPEN field.

The originating registries remain unchanged for historical traceability.


---

## 12. Release-Candidate Statement

This manuscript assembles the currently verified F3 technical corpus.

It does not expand claim scope beyond the source registries.

It does not convert runtime conformance into formal proof.

It does not convert counterexample discharge into positive theorem proof.

It does not alter historical registration-time status.

Release eligibility remains subject to final repository closure, exact staging, commit, tag, and remote verification.
