# FIN-F8-02 — Canonical Object / Type Freeze

Status: COMPLETE — PASS

## Canonical family

Autonomous Economic Agency and Machine Financial Authority

## Frozen canonical object registry

### F8-O-001 — Autonomous Financial Action Capability

A typed technical capability of an autonomous or machine system to select, initiate, invoke, route, sign, transfer, trade, purchase, settle, or otherwise perform a financial action without that capability itself constituting principal authority.

### F8-O-002 — Machine-Originated Financial Request

A typed consequential financial request produced or initiated by an autonomous or machine system that remains independently evaluable from the authority required to admit it.

### F8-O-003 — Economic Principal

The external or previously admitted person, organization, institution, governed entity, or other valid principal to whom consequential economic authority is attributable.

### F8-O-004 — Economic Principal Identity

A typed identity binding used to distinguish the valid economic principal from machine, agent, account, wallet, key, or runtime identities.

### F8-O-005 — Autonomous Agent Identity

A typed machine or agent identity representing the acting autonomous system without constituting economic principal status.

### F8-O-006 — Machine Financial Authority

A source-bound, scoped, temporally valid, non-revoked authority grant permitting an autonomous system to perform specified consequential financial actions on behalf of a valid economic principal.

### F8-O-007 — Machine Authority Source

The valid external or previously admitted authority basis from which machine financial authority is derived.

### F8-O-008 — Machine Authority Scope

The explicit set of financial actions, assets, limits, counterparties, venues, jurisdictions, conditions, or other consequential boundaries within which machine authority may operate.

### F8-O-009 — Machine Authority Temporal Window

The validity interval within which machine financial authority is current and usable.

### F8-O-010 — Delegated Machine Authority

A source-bound, scoped, temporally valid, non-revoked, attenuated delegation of financial authority to an autonomous system.

### F8-O-011 — Autonomous Subdelegation

A typed delegation issued through an already delegated machine-authority chain that SHALL NOT exceed the authority of the delegating parent.

### F8-O-012 — Machine Financial Action Evidence

Evidence that an autonomous system proposed, initiated, attempted, or completed a financial action without treating execution evidence as authority.

### F8-O-013 — Machine Authority Evidence

Evidence relevant to whether machine financial authority exists, is attributable to a valid principal, and remains scoped, current, and non-revoked.

### F8-O-014 — Autonomous Account / Wallet Control

A typed technical control relation over an account, wallet, key, credential, or financial execution surface without constituting economic principal authority.

### F8-O-015 — Machine Authority Revocation

A typed event or state terminating previously valid machine financial authority.

### F8-O-016 — Machine Authority Supersession

A typed event or state replacing previously valid machine financial authority with another authority record or principal relation.

### F8-O-017 — Principal Continuity Record

A typed record determining whether the economic principal relation remains continuous across agent replacement, model replacement, runtime migration, identity rotation, or infrastructure change.

### F8-O-018 — Agent Replacement Event

A typed substitution of one autonomous agent, model, runtime, identity, or implementation for another without presuming inherited authority.

### F8-O-019 — Machine Authority Conflict

A typed conflict between autonomous capability, identity, principal attribution, delegated authority, scope, temporal validity, revocation state, or observed financial execution.

### F8-O-020 — Autonomous Financial Admission Record

A typed decision record separating whether a machine-originated financial request is governance-admissible from whether the autonomous system can technically execute it.

## Frozen type distinctions

- autonomous financial action capability != machine financial authority
- machine-originated financial request != economic principal instruction
- economic principal != autonomous agent
- economic principal identity != autonomous agent identity
- agent identity != principal identity
- machine identity != economic principal status
- machine financial authority != machine authority source
- machine authority scope != technical capability envelope
- machine authority temporal window != persistent runtime availability
- delegated machine authority != self-authorization
- autonomous subdelegation != authority amplification
- machine financial action evidence != machine authority evidence
- account control != financial authority
- wallet control != principal authority
- key possession != authority
- agent replacement != authority inheritance
- runtime migration != principal continuity
- successful autonomous execution != governance admission
- persistent operation != continuing authority
- model output != financial authorization

## Canonical type boundary

F8 separates autonomous financial capability from economic principal status and from the machine financial authority required to bind consequential action.

No F8 object may self-create, self-renew, self-expand, self-transfer, or self-inherit economic principal authority merely because an autonomous system can act, persist, retain state, control credentials, access tools, or complete financial execution.

Machine financial authority MUST remain attributable to a valid economic principal and distinguishable from the technical identity or implementation of the acting autonomous system.

## Identity non-collapse rule

Economic principal identity, autonomous agent identity, account identity, wallet identity, key identity, and runtime identity MUST remain independently representable.

Technical control over an identity-bearing object SHALL NOT constitute economic principal status.

## Replacement / continuity rule

Replacement of an autonomous agent, model, runtime, account credential, wallet, or implementation SHALL NOT automatically transfer or recreate machine financial authority.

Principal continuity and authority continuity MUST be separately established.

## Cross-family inheritance

F8 inherits:

- F2 consensus and multiparty-authority distinctions;
- F4 ledger-state and record-truth distinctions;
- F5 key-possession, signature-validity, and custody-authority distinctions;
- F6 programmable-finance authority distinctions;
- F7 jurisdictional authority distinctions;
- architecture-wide capability / authority separation;
- source-bound delegation and attenuation requirements.

F8 does not redefine settlement semantics, obligation finality, ledger truth, cryptographic custody authority, programmable-finance authority, or jurisdictional authority as primary subjects.

## Freeze control

The F8 canonical object and type vocabulary is frozen.

State domains, predicates, decisions, transitions, invariants, proof obligations, runtime components, tests, and publication surfaces remain unfrozen.

## Next

FIN-F8-03 — STATE / CLASSIFICATION ALGEBRA FREEZE
