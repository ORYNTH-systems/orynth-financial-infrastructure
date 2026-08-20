# FIN-F5-03 — State / Classification Algebra Freeze

Status: COMPLETE — PASS

## Working family

Digital-Asset Custody and Delegated Cryptographic Authority

## Frozen state / classification domains

### F5-SD-001 — Cryptographic Capability Status

- ABSENT
- AVAILABLE
- RESTRICTED
- UNAVAILABLE
- COMPROMISED

### F5-SD-002 — Key Possession Status

- NOT_HELD
- HELD
- SHARED
- LOST
- COMPROMISED
- UNKNOWN

### F5-SD-003 — Custody State

- UNESTABLISHED
- HELD
- DELEGATED
- TRANSFER_PENDING
- TRANSFERRED
- CONFLICTED
- UNKNOWN

### F5-SD-004 — Delegated Cryptographic Authority Status

- ABSENT
- PENDING
- ACTIVE
- RESTRICTED
- EXPIRED
- REVOKED
- SUPERSEDED
- INVALID

### F5-SD-005 — Authority Source Status

- UNRESOLVED
- SUPPORTED
- CONFLICTED
- REVOKED
- EXPIRED
- INVALID

### F5-SD-006 — Key Lifecycle Status

- UNISSUED
- ISSUED
- ACTIVE
- ROTATED
- REVOKED
- EXPIRED
- COMPROMISED
- LOST
- RECOVERED
- SUPERSEDED

### F5-SD-007 — Signature / Cryptographic Act Status

- NOT_ATTEMPTED
- PENDING
- TECHNICALLY_VALID
- TECHNICALLY_INVALID
- UNVERIFIED

### F5-SD-008 — Governance Authorization Status

- UNDETERMINED
- SUPPORTED
- DENIED
- DEFERRED
- REVALIDATION_REQUIRED
- CONFLICTED

### F5-SD-009 — Threshold Control Status

- NOT_APPLICABLE
- UNSATISFIED
- PARTIALLY_SATISFIED
- SATISFIED
- CONFLICTED
- INVALID

### F5-SD-010 — Custody Authority Conflict Status

- NONE
- DETECTED
- UNRESOLVED
- BLOCKING
- RESOLVED

### F5-SD-011 — Authority Continuity Classification

- UNCLASSIFIED
- PRESERVED
- DISRUPTED
- REESTABLISHED
- NOT_ESTABLISHED

### F5-SD-012 — Cryptographic / Governance Alignment

- UNDETERMINED
- ALIGNED
- CAPABILITY_WITHOUT_AUTHORITY
- AUTHORITY_WITHOUT_CAPABILITY
- CONFLICTED

## Frozen composite state

Psi5_t = (C_t, K_t, U_t, A_t, S_t, L_t, X_t, G_t, T_t, F_t, N_t, M_t, E_t, sigma_t, tau_t)

where:

- C_t = cryptographic capability status
- K_t = key possession status
- U_t = digital-asset custody state
- A_t = delegated cryptographic authority status
- S_t = authority source status
- L_t = key lifecycle status
- X_t = signature / cryptographic act status
- G_t = governance authorization status
- T_t = threshold control status
- F_t = custody authority conflict status
- N_t = authority continuity classification
- M_t = cryptographic / governance alignment
- E_t = evidence context
- sigma_t = scope context
- tau_t = temporal context

## Frozen algebraic separations

- K_t = HELD does not imply A_t = ACTIVE
- X_t = TECHNICALLY_VALID does not imply G_t = SUPPORTED
- T_t = SATISFIED does not imply G_t = SUPPORTED
- U_t = HELD does not imply A_t = ACTIVE
- L_t = RECOVERED does not imply N_t = PRESERVED
- L_t = ROTATED does not imply N_t = PRESERVED
- M_t = ALIGNED is a classification, not an authority source
- F_t = DETECTED does not resolve S_t or A_t

## State non-collapse requirements

The F5 state algebra MUST preserve independent representation of:

1. capability;
2. possession;
3. custody;
4. authority;
5. authority source;
6. key lifecycle;
7. technical cryptographic validity;
8. governance authorization;
9. threshold satisfaction;
10. custody-authority conflict;
11. authority continuity;
12. cryptographic/governance alignment.

No state value in one domain may be treated as constitutively establishing a value in another domain unless a later frozen predicate or decision rule explicitly permits that relationship.

## Freeze control

The F5 state / classification algebra is frozen.

Predicates, relations, decisions, transitions, invariants, proof obligations, runtime components, and tests remain unfrozen.

## Next

FIN-F5-04 — RELATION / PREDICATE FREEZE
