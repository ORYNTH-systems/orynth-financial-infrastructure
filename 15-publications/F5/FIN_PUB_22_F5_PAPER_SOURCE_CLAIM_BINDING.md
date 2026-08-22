# FIN-PUB-22 — F5 Paper Source / Claim Binding

Status: COMPLETE — PASS

## Paper

F5 — Digital-Asset Custody and Delegated Cryptographic Authority

## Canonical baseline

- suite closure tag: financial-suite-v1.0.0
- F5 release tag: financial-f5-v1.0.0
- controlling separation: key possession != authority

## Bound publication claims

### F5-PUB-C001

Claim: Cryptographic key possession is distinct from governance authority.

Canonical basis: F5 custody and authority semantics; canonical non-implication results

### F5-PUB-C002

Claim: A valid cryptographic signature does not by itself establish valid governance authorization.

Canonical basis: signature / authority separation; verification and adversarial surfaces

### F5-PUB-C003

Claim: Custody capability is distinct from authority to exercise custody.

Canonical basis: custody-state model; capability / authority boundary

### F5-PUB-C004

Claim: Delegated cryptographic authority cannot exceed the scope of the delegating authority.

Canonical basis: delegation attenuation; delegated custody authority model

### F5-PUB-C005

Claim: Technical control of an asset does not itself establish valid economic-principal authority.

Canonical basis: principal / technical-control separation; custody proofs

### F5-PUB-C006

Claim: Transfer of a key does not necessarily transfer governance authority.

Canonical basis: key-transfer / authority-transfer non-equivalence

### F5-PUB-C007

Claim: Revocation of authority is distinct from continued technical possession of cryptographic capability.

Canonical basis: revocation-state semantics; authority / capability separation

### F5-PUB-C008

Claim: Cryptographic evidence does not itself create authority for the represented financial action.

Canonical basis: evidence / authority separation; inherited governance boundary

### F5-PUB-C009

Claim: A custody action may be technically valid while remaining governance-inadmissible.

Canonical basis: custody execution / admissibility separation; adversarial verification

### F5-PUB-C010

Claim: Successful digital-asset execution does not retroactively establish valid custody authority.

Canonical basis: execution / authority non-implication; adversarial verification

## Canonical source surfaces

- 08-digital-asset-custody/FIN_F5_01B_BOUNDARY_FREEZE.md
- 08-digital-asset-custody/FIN_F5_02_CANONICAL_OBJECT_TYPE_FREEZE.md
- 08-digital-asset-custody/FIN_F5_03_STATE_CLASSIFICATION_ALGEBRA_FREEZE.md
- 08-digital-asset-custody/FIN_F5_04_RELATION_PREDICATE_FREEZE.md
- 08-digital-asset-custody/FIN_F5_05_DECISION_TRANSITION_SEMANTICS_FREEZE.md
- 08-digital-asset-custody/FIN_F5_06_INVARIANT_DISCOVERY_FREEZE.md
- 08-digital-asset-custody/FIN_F5_07_PROOF_OBLIGATION_REGISTRY_FREEZE.md
- 08-digital-asset-custody/FIN_F5_08_FORMAL_PROOF_COUNTEREXAMPLE_TRACEABILITY_DISCHARGE.md
- 08-digital-asset-custody/FIN_F5_09_REFERENCE_RUNTIME_CONSTRUCTION_CONFORMANCE.md
- 08-digital-asset-custody/FIN_F5_10_ADVERSARIAL_VERIFICATION_RELEASE_READINESS.md
- 08-digital-asset-custody/FIN_F5_11_CANONICAL_SURFACE_RELEASE_FREEZE.md
- 08-digital-asset-custody/runtime/f5_reference_runtime.py
- 15-publications/F5/.gitkeep
- tests/f5/test_f5_reference_runtime.py
- tests/f5_adversarial/test_f5_adversarial.py

## Claim-control rules

- key possession SHALL NOT be represented as governance authority
- valid cryptographic signature SHALL NOT be represented as self-proving authorization
- custody capability SHALL NOT be represented as custody authority
- delegation SHALL remain attenuated to the delegating authority and admitted scope
- technical control SHALL NOT be represented as economic-principal authority
- execution evidence SHALL NOT be used as retroactive custody-authority evidence
- adversarial results SHALL remain bounded verification evidence
- no production, regulatory, institutional, customer, legal, or external-certification claim is admitted

## Binding status

F5 publication claims are source-bound to the canonical F5 technical and verification surfaces.

The F5 manuscript itself remains unwritten / unfrozen.

## Next

FIN-PUB-23 — F5 MANUSCRIPT CONSTRUCTION
