# FIN-F7-03 — State / Classification Algebra Freeze

Status: COMPLETE — PASS

## Canonical family

Cross-Jurisdiction Financial Execution

## Frozen state / classification domains

### F7-SD-001 — Technical Reach Status

- ABSENT
- AVAILABLE
- RESTRICTED
- UNAVAILABLE
- FAILED

### F7-SD-002 — Jurisdictional Authority Status

- ABSENT
- PENDING
- ACTIVE
- RESTRICTED
- EXPIRED
- REVOKED
- SUPERSEDED
- INVALID

### F7-SD-003 — Authority Source Status

- UNRESOLVED
- SUPPORTED
- CONFLICTED
- EXPIRED
- REVOKED
- INVALID

### F7-SD-004 — Jurisdictional Applicability Status

- UNDETERMINED
- APPLICABLE
- PARTIALLY_APPLICABLE
- INAPPLICABLE
- CONFLICTED
- REVALIDATION_REQUIRED

### F7-SD-005 — Principal Jurisdiction Status

- UNRESOLVED
- IDENTIFIED
- MULTIPLE
- CONFLICTED
- INSUFFICIENT

### F7-SD-006 — Counterparty Jurisdiction Status

- UNRESOLVED
- IDENTIFIED
- MULTIPLE
- CONFLICTED
- INSUFFICIENT

### F7-SD-007 — Asset / Custody Jurisdiction Status

- UNRESOLVED
- IDENTIFIED
- MULTIPLE
- CONFLICTED
- INSUFFICIENT

### F7-SD-008 — Settlement Venue Jurisdiction Status

- UNRESOLVED
- IDENTIFIED
- MULTIPLE
- CONFLICTED
- INSUFFICIENT

### F7-SD-009 — Cross-Jurisdiction Delegation Status

- ABSENT
- PENDING
- ACTIVE
- RESTRICTED
- EXPIRED
- REVOKED
- INVALID
- NONATTENUATED

### F7-SD-010 — Jurisdictional Restriction Status

- NONE
- PRESENT
- BLOCKING
- CONDITIONAL
- CONFLICTED
- RESOLVED

### F7-SD-011 — Jurisdictional Conflict Status

- NONE
- DETECTED
- UNRESOLVED
- BLOCKING
- RESOLVED

### F7-SD-012 — Jurisdictional Evidence Status

- ABSENT
- PRESENT
- CORROBORATED
- CONFLICTED
- STALE
- INSUFFICIENT

### F7-SD-013 — Cross-Jurisdiction Execution Status

- NOT_REQUESTED
- REQUESTED
- PENDING
- EXECUTED
- BLOCKED
- FAILED

### F7-SD-014 — Governance Authorization Status

- UNDETERMINED
- SUPPORTED
- DENIED
- DEFERRED
- REVALIDATION_REQUIRED
- REAUTHORIZATION_REQUIRED
- CONFLICTED

### F7-SD-015 — Jurisdictional Alignment Status

- UNDETERMINED
- ALIGNED
- TECHNICAL_REACH_WITHOUT_AUTHORITY
- AUTHORITY_WITHOUT_TECHNICAL_REACH
- PARTIAL_JURISDICTIONAL_COVERAGE
- CONFLICTED

### F7-SD-016 — Execution Consequence Classification

- NONE
- TECHNICAL_ONLY
- FINANCIALLY_CONSEQUENTIAL
- GOVERNANCE_ADMITTED
- GOVERNANCE_REJECTED
- CONFLICTED

## Frozen composite state

Psi7_t = (R_t, A_t, S_t, J_t, P_t, C_t, K_t, V_t, D_t, X_t, F_t, E_t, I_t, G_t, M_t, Q_t, sigma_t, tau_t)

where:

- R_t = technical reach status
- A_t = jurisdictional authority status
- S_t = authority source status
- J_t = jurisdictional applicability status
- P_t = principal jurisdiction status
- C_t = counterparty jurisdiction status
- K_t = asset / custody jurisdiction status
- V_t = settlement venue jurisdiction status
- D_t = cross-jurisdiction delegation status
- X_t = jurisdictional restriction status
- F_t = jurisdictional conflict status
- E_t = jurisdictional evidence status
- I_t = cross-jurisdiction execution status
- G_t = governance authorization status
- M_t = jurisdictional alignment status
- Q_t = execution consequence classification
- sigma_t = scope context
- tau_t = temporal context

## Frozen algebraic separations

- R_t = AVAILABLE does not imply A_t = ACTIVE
- J_t = APPLICABLE does not imply A_t = ACTIVE
- P_t = IDENTIFIED does not constitute jurisdictional authority
- C_t = IDENTIFIED does not constitute jurisdictional consent
- K_t = IDENTIFIED does not constitute execution authority
- V_t = IDENTIFIED does not constitute jurisdictional permission
- D_t = ACTIVE does not imply unconstrained or universal authority
- E_t = CORROBORATED does not constitute authority
- I_t = EXECUTED does not imply G_t = SUPPORTED
- F_t = DETECTED does not resolve jurisdictional conflict
- X_t = PRESENT does not itself identify the correct authority source
- M_t = ALIGNED is a classification, not an authority source
- Q_t = FINANCIALLY_CONSEQUENTIAL does not imply Q_t = GOVERNANCE_ADMITTED
- authorization in one jurisdiction does not imply authorization in another jurisdiction

## Multi-jurisdiction state rule

Each consequentially implicated jurisdiction MUST remain independently representable within the state context.

A multi-jurisdiction request MUST NOT collapse distinct jurisdictional authority, applicability, restriction, evidence, or conflict states into a single aggregate authorization state.

Partial jurisdictional coverage MUST remain distinguishable from complete jurisdictional coverage.

## State non-collapse requirements

The F7 state algebra MUST preserve independent representation of:

1. technical reach;
2. jurisdictional authority;
3. authority source;
4. jurisdictional applicability;
5. principal jurisdiction;
6. counterparty jurisdiction;
7. asset / custody jurisdiction;
8. settlement venue jurisdiction;
9. cross-jurisdiction delegation;
10. jurisdictional restrictions;
11. jurisdictional conflict;
12. jurisdictional evidence;
13. execution status;
14. governance authorization;
15. jurisdictional alignment;
16. execution consequence classification.

No state value in one domain may be treated as constitutively establishing jurisdictional authority, applicability, admissibility, consent, or consequential validity in another domain unless a later frozen predicate or decision rule explicitly permits that relationship.

## Freeze control

The F7 state / classification algebra is frozen.

Predicates, relations, decision functions, transition functions, invariants, proof obligations, runtime components, tests, and publication surfaces remain unfrozen.

## Next

FIN-F7-04 — RELATION / PREDICATE FREEZE
