# FIN-F5-01B — Digital-Asset Custody / Delegated Cryptographic Authority Boundary Freeze

Status: COMPLETE — PASS

## Working family

Digital-Asset Custody and Delegated Cryptographic Authority

## Frozen problem boundary

F5 governs the distinction between cryptographic or custody capability and the governance authority required to use that capability for consequential financial action.

The central F5 problem is not whether an actor, process, wallet, device, key-holder, custodian, contract surface, or signing mechanism can produce a technically valid cryptographic act.

The central problem is whether that cryptographic act is supported by current, applicable, scoped, non-revoked financial authority.

## Frozen core separation

key possession != authority

A private key, signing key, multisignature share, threshold-signature share, wallet credential, custody credential, device control, or equivalent cryptographic capability SHALL NOT by itself constitute governance authority.

## Frozen inclusion boundary

- digital-asset custody state
- cryptographic key possession
- cryptographic control capability
- signing capability
- delegated cryptographic authority
- source-bound delegation
- delegation attenuation
- key rotation
- key revocation
- key compromise
- key recovery
- multisignature control
- threshold-signature control
- wallet control
- address control
- custody transfer representation
- cryptographic custody evidence
- custody authority conflict
- cryptographic authority conflict
- ledger-recognized control versus governance authority
- technically valid signature versus admissible financial authorization
- delegated key capability versus delegated financial authority
- loss, compromise, revocation, expiry, or supersession of cryptographic authority
- separation of cryptographic execution evidence from authority evidence

## Frozen exclusion boundary

- F1 partial settlement, compensation, reversal, and reconciliation semantics as primary subject
- F2 distributed consensus and multiparty authority semantics as primary subject
- F3 obligation finality, custody-validity determination, and consequential closure as primary subject
- F4 ledger-state representation, record reopening, and record-state reconstruction as primary subject
- F6 smart-contract and programmable-finance authority as primary subject
- F7 cross-jurisdiction financial execution as primary subject
- F8 autonomous economic principal authority as primary subject
- blockchain consensus protocol correctness
- cryptographic primitive design or cryptanalytic security
- wallet user-interface design
- token economics

## Frozen inherited separations

- capability != authority
- key possession != authority
- signing capability != authority
- valid cryptographic signature != valid governance authorization
- wallet control != financial authority
- address control != beneficial or governance authority
- custody possession != custody authority
- recorded custody != custody authority
- evidence != authority
- consensus != authority
- ledger inclusion != authority
- ledger representation != underlying financial truth
- delegated capability != delegated authority
- key recovery != authority recovery
- key rotation != authority continuity
- key revocation != historical erasure
- cryptographic success != admissible financial execution

## Cross-family inheritance

F5 inherits F3 custody semantics without redefining custody validity itself.

F5 inherits F4 record and ledger distinctions without treating ledger-recognized possession or control as constitutive authority.

F5 inherits the architecture-wide rule that capability cannot self-create authority.

## Frozen authority boundary

Cryptographic authority MUST be attributable to an external or previously admitted authority source.

Cryptographic possession or control MUST NOT self-bootstrap that authority.

Delegated cryptographic authority MUST remain source-bound, scoped, temporally valid, and attenuated relative to its parent authority.

Revocation, expiry, compromise, supersession, or loss of authority MUST remain distinguishable from mere loss or replacement of key material.

## Frozen non-collapse conditions

F5 SHALL reject any architecture that collapses:

1. possession into authority;
2. signature validity into governance authorization;
3. wallet control into financial ownership or authority;
4. ledger recognition into authority;
5. key replacement into authority continuity;
6. recovery of cryptographic capability into recovery of governance authority;
7. delegated execution capability into unconstrained delegation;
8. custody evidence into custody authority.

## Boundary status

The F5 problem boundary is frozen.

Canonical objects, state domains, predicates, transitions, invariants, proof obligations, and runtime surfaces remain unfrozen.

## Next

FIN-F5-02 — CANONICAL OBJECT / TYPE FREEZE
