# FIN-F5-06 — Invariant Discovery and Freeze

Status: COMPLETE — PASS

## Canonical invariant registry

### F5-INV-001 — CAPABILITY

Cryptographic capability SHALL NOT by itself establish governance authority.

- registration status: OPEN

### F5-INV-002 — POSSESSION

Possession or control of key material SHALL NOT by itself establish governance authority.

- registration status: OPEN

### F5-INV-003 — SIGNATURE

A technically valid cryptographic signature SHALL NOT by itself establish governance authorization.

- registration status: OPEN

### F5-INV-004 — THRESHOLD

Threshold or multisignature satisfaction SHALL NOT by itself establish governance authorization.

- registration status: OPEN

### F5-INV-005 — CUSTODY

Digital-asset custody possession SHALL remain distinct from custody authority.

- registration status: OPEN

### F5-INV-006 — WALLET

Wallet or address control SHALL NOT by itself establish financial authority.

- registration status: OPEN

### F5-INV-007 — SOURCE

Delegated cryptographic authority SHALL be traceable to an applicable authority source.

- registration status: OPEN

### F5-INV-008 — DELEGATION

Delegated cryptographic authority SHALL NOT exceed its source authority in scope, duration, capability, or conditions.

- registration status: OPEN

### F5-INV-009 — SCOPE

A cryptographic operation SHALL NOT be admitted outside the applicable authority scope.

- registration status: OPEN

### F5-INV-010 — TEMPORAL

Expired, revoked, superseded, or otherwise temporally invalid authority SHALL NOT authorize a current cryptographic operation.

- registration status: OPEN

### F5-INV-011 — LIFECYCLE

Key lifecycle permission SHALL remain distinct from governance authority validity.

- registration status: OPEN

### F5-INV-012 — RECOVERY

Key recovery SHALL NOT by itself restore governance authority.

- registration status: OPEN

### F5-INV-013 — ROTATION

Key rotation SHALL NOT by itself establish authority continuity.

- registration status: OPEN

### F5-INV-014 — REVOCATION

Key revocation or authority revocation SHALL NOT erase historical cryptographic or authority evidence.

- registration status: OPEN

### F5-INV-015 — EVIDENCE

Cryptographic execution evidence SHALL remain distinct from governance authority evidence.

- registration status: OPEN

### F5-INV-016 — CONFLICT

Detection of a custody-authority conflict SHALL NOT itself resolve which authority state is valid.

- registration status: OPEN

### F5-INV-017 — ALIGNMENT

Cryptographic-governance alignment SHALL be a derived classification and SHALL NOT constitute an authority source.

- registration status: OPEN

### F5-INV-018 — PREDICATE

Truth of an F5 predicate SHALL NOT by itself authorize a state transition.

- registration status: OPEN

### F5-INV-019 — DECISION

F5 decision outcome SHALL remain distinct from transition existence.

- registration status: OPEN

### F5-INV-020 — TRANSITION

Transition existence SHALL remain distinct from resulting F5 state classification.

- registration status: OPEN

### F5-INV-021 — BLOCK

F5-BLOCK SHALL imply that the blocked target transition is undefined.

- registration status: OPEN

### F5-INV-022 — DEFER

F5-DEFER SHALL NOT authorize the deferred target transition and SHALL remain distinct from denial.

- registration status: OPEN

### F5-INV-023 — REVALIDATION

F5-REVALIDATE SHALL NOT create, restore, or extend governance authority.

- registration status: OPEN

### F5-INV-024 — REAUTHORIZATION

F5-REAUTHORIZE SHALL require independent re-establishment of authority and SHALL NOT be satisfied solely by restored cryptographic capability.

- registration status: OPEN

### F5-INV-025 — ADMISSION

F5-ADMIT SHALL NOT prove that a cryptographic act or custody transition occurred.

- registration status: OPEN

### F5-INV-026 — ADMISSION

F5-ADMIT SHALL require applicable authority support and SHALL NOT be inferred solely from signature validity, key possession, threshold satisfaction, wallet control, or custody evidence.

- registration status: OPEN

### F5-INV-027 — CONTINUITY

Restoration of cryptographic capability SHALL NOT by itself establish preservation of governance authority continuity.

- registration status: OPEN

### F5-INV-028 — F3-BOUNDARY

F5 SHALL NOT redefine underlying F3 custody-validity or finality determinations merely from cryptographic control.

- registration status: OPEN

### F5-INV-029 — F4-BOUNDARY

F5 SHALL NOT infer governance authority from F4 ledger or record representation of cryptographic control.

- registration status: OPEN

### F5-INV-030 — CORE

Key possession, cryptographic success, and ledger-recognized control SHALL remain insufficient to self-create financial authority.

- registration status: OPEN

## Invariant-family inventory

- ADMISSION: 2
- ALIGNMENT: 1
- BLOCK: 1
- CAPABILITY: 1
- CONFLICT: 1
- CONTINUITY: 1
- CORE: 1
- CUSTODY: 1
- DECISION: 1
- DEFER: 1
- DELEGATION: 1
- EVIDENCE: 1
- F3-BOUNDARY: 1
- F4-BOUNDARY: 1
- LIFECYCLE: 1
- POSSESSION: 1
- PREDICATE: 1
- REAUTHORIZATION: 1
- RECOVERY: 1
- REVALIDATION: 1
- REVOCATION: 1
- ROTATION: 1
- SCOPE: 1
- SIGNATURE: 1
- SOURCE: 1
- TEMPORAL: 1
- THRESHOLD: 1
- TRANSITION: 1
- WALLET: 1

## Frozen control

All 30 F5 invariants are registered OPEN.

No invariant is formally proved, counterexample-discharged, runtime-conformant, or otherwise closed by this pass.

## Next

FIN-F5-07 — PROOF OBLIGATION REGISTRY FREEZE
