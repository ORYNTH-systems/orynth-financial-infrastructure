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
