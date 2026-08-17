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
