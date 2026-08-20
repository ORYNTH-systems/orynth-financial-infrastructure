# FIN-F5-04 — Relation / Predicate Freeze

Status: COMPLETE — PASS

## Working family

Digital-Asset Custody and Delegated Cryptographic Authority

## Frozen canonical relations / predicates

### F5-R-001 — HasCryptographicCapability

Determines whether the subject currently possesses the technical capability required to perform the requested cryptographic act.

### F5-R-002 — PossessesKeyMaterial

Determines whether the subject possesses or controls the relevant cryptographic key material or equivalent cryptographic credential.

### F5-R-003 — CustodyStateEstablished

Determines whether the applicable digital-asset custody state is established under the current evidence context.

### F5-R-004 — DelegatedAuthorityActive

Determines whether delegated cryptographic authority exists, is active, scoped, temporally valid, and not revoked or superseded.

### F5-R-005 — AuthoritySourceSupported

Determines whether the claimed cryptographic authority is traceable to a supported external or previously admitted authority source.

### F5-R-006 — AuthorityScopeValid

Determines whether the requested cryptographic operation falls within the scope of the applicable delegated authority.

### F5-R-007 — AuthorityTemporallyValid

Determines whether the authority is current for the requested operation and applicable temporal context.

### F5-R-008 — DelegationAttenuated

Determines whether delegated authority does not exceed the scope, capability, duration, or conditions of its source authority.

### F5-R-009 — CryptographicActTechnicallyValid

Determines whether the signature or cryptographic act is technically valid under the applicable cryptographic mechanism.

### F5-R-010 — ThresholdControlSatisfied

Determines whether applicable multisignature or threshold-control requirements have been technically satisfied.

### F5-R-011 — GovernanceAuthorizationSupported

Determines whether the requested cryptographic act is supported by applicable governance authority.

### F5-R-012 — CustodyAuthorityConflictExists

Determines whether observed custody or cryptographic control conflicts with applicable custody or governance authority.

### F5-R-013 — KeyLifecyclePermitsUse

Determines whether the applicable key lifecycle state permits current use of the key or cryptographic capability.

### F5-R-014 — AuthorityContinuityPreserved

Determines whether governance authority continuity is preserved across key rotation, recovery, replacement, or related cryptographic lifecycle change.

### F5-R-015 — CryptographicGovernanceAligned

Determines whether observed cryptographic capability and action are aligned with current applicable governance authority.

### F5-R-016 — ExecutionEvidenceExists

Determines whether evidence exists that the cryptographic act or signing operation occurred.

### F5-R-017 — AuthorityEvidenceExists

Determines whether evidence exists supporting the claimed governance authority independently of cryptographic execution evidence.

### F5-R-018 — KeyRecoveryRestoresAuthority

Determines whether governance authority has been independently re-established after key recovery rather than inferred from restored cryptographic capability.

## Frozen predicate separations

- HasCryptographicCapability does not imply DelegatedAuthorityActive
- PossessesKeyMaterial does not imply GovernanceAuthorizationSupported
- CryptographicActTechnicallyValid does not imply GovernanceAuthorizationSupported
- ThresholdControlSatisfied does not imply GovernanceAuthorizationSupported
- CustodyStateEstablished does not imply DelegatedAuthorityActive
- ExecutionEvidenceExists does not imply AuthorityEvidenceExists
- KeyLifecyclePermitsUse does not imply AuthorityContinuityPreserved
- KeyRecoveryRestoresAuthority MUST be independently established
- CustodyAuthorityConflictExists does not resolve authority
- CryptographicGovernanceAligned is a classification result, not an authority source

## Object bindings

- F5-O-001 -> F5-R-001
- F5-O-002 -> F5-R-002
- F5-O-003 -> F5-R-003, F5-R-012
- F5-O-004 -> F5-R-004, F5-R-006, F5-R-007, F5-R-008
- F5-O-005 -> F5-R-005
- F5-O-006 -> F5-R-006, F5-R-007, F5-R-011
- F5-O-007 -> F5-R-009, F5-R-016
- F5-O-008 -> F5-R-005, F5-R-011, F5-R-017
- F5-O-009 -> F5-R-013, F5-R-014, F5-R-018
- F5-O-010 -> F5-R-012
- F5-O-011 -> F5-R-010
- F5-O-012 -> F5-R-001, F5-R-015

## State-domain bindings

- F5-SD-001 -> F5-R-001
- F5-SD-002 -> F5-R-002
- F5-SD-003 -> F5-R-003, F5-R-012
- F5-SD-004 -> F5-R-004, F5-R-006, F5-R-007, F5-R-008
- F5-SD-005 -> F5-R-005
- F5-SD-006 -> F5-R-013, F5-R-014, F5-R-018
- F5-SD-007 -> F5-R-009, F5-R-016
- F5-SD-008 -> F5-R-011
- F5-SD-009 -> F5-R-010
- F5-SD-010 -> F5-R-012
- F5-SD-011 -> F5-R-014, F5-R-018
- F5-SD-012 -> F5-R-015

## Predicate control

Predicates describe facts or classifications only.

No predicate in this freeze authorizes execution or implies that a transition exists.

Authority remains external to mere possession, capability, signature validity, threshold satisfaction, ledger recognition, custody evidence, or key lifecycle state.

## Freeze control

The F5 canonical relation / predicate vocabulary is frozen.

Decision functions, transition functions, invariants, proof obligations, runtime components, and tests remain unfrozen.

## Next

FIN-F5-05 — DECISION / TRANSITION SEMANTICS FREEZE
