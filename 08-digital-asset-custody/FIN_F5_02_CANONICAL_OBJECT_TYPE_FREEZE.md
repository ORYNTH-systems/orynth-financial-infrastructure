# FIN-F5-02 — Canonical Object / Type Freeze

Status: COMPLETE — PASS

## Working family

Digital-Asset Custody and Delegated Cryptographic Authority

## Frozen canonical object registry

### F5-O-001 — Cryptographic Capability

A typed capability to perform a cryptographic operation such as signing, key use, threshold participation, or equivalent cryptographic act.

### F5-O-002 — Cryptographic Key Possession

A typed condition representing possession or control of cryptographic key material or equivalent signing capability.

### F5-O-003 — Digital-Asset Custody State

A typed representation of custody or control state associated with a digital asset, wallet, address, key set, or custody mechanism.

### F5-O-004 — Delegated Cryptographic Authority

A source-bound, scoped, temporally valid, attenuated authority grant permitting specified cryptographic operations.

### F5-O-005 — Cryptographic Authority Source

The external or previously admitted authority basis from which delegated cryptographic authority is derived.

### F5-O-006 — Cryptographic Authorization Request

A typed request seeking authority to perform a cryptographic or custody-relevant financial operation.

### F5-O-007 — Cryptographic Execution Evidence

Evidence that a cryptographic operation occurred or that a signature, threshold contribution, or key-mediated act was technically produced.

### F5-O-008 — Cryptographic Authority Evidence

Evidence relevant to whether a cryptographic operation was supported by applicable governance authority.

### F5-O-009 — Key Lifecycle Event

A typed event representing key issuance, activation, rotation, revocation, expiry, compromise, loss, supersession, or recovery.

### F5-O-010 — Custody Authority Conflict

A typed conflict between observed custody or cryptographic control and the applicable governance authority.

### F5-O-011 — Threshold Control Structure

A typed structure describing multisignature, threshold-signature, quorum, or shared cryptographic control requirements.

### F5-O-012 — Wallet / Address Control Representation

A typed representation that an actor, process, or device controls a wallet or address without treating that control as constitutive financial authority.

## Frozen type distinctions

- cryptographic capability != authority
- key possession != authority
- cryptographic key possession != delegated cryptographic authority
- digital-asset custody state != custody authority
- wallet control != financial authority
- address control != beneficial or governance authority
- valid cryptographic signature != valid governance authorization
- cryptographic execution evidence != authority evidence
- delegated capability != delegated authority
- authority source != key material
- key lifecycle event != authority lifecycle event
- key recovery != authority recovery
- key rotation != authority continuity
- key revocation != historical erasure
- threshold satisfaction != governance admissibility
- custody evidence != custody authority
- custody conflict != authority resolution
- ledger-recognized control != governance authority

## Canonical type boundary

F5 separates the technical capability to produce a cryptographic act from the governance authority required to admit that act as consequential financial execution.

No F5 object may self-create, self-extend, or self-recover governance authority merely because cryptographic capability exists.

## Cross-family inheritance

F5 inherits:

- F3 custody-validity distinctions;
- F4 ledger and record representation distinctions;
- architecture-wide capability / authority separation;
- source-bound delegation and attenuation requirements.

F5 does not redefine underlying obligation finality, ledger-state truth, programmable-contract authority, jurisdictional authority, or autonomous economic principal status.

## Freeze control

The F5 canonical object and type vocabulary is frozen.

State domains, predicates, decision functions, transition functions, invariants, proof obligations, runtime components, and tests remain unfrozen.

## Next

FIN-F5-03 — STATE / CLASSIFICATION ALGEBRA FREEZE
