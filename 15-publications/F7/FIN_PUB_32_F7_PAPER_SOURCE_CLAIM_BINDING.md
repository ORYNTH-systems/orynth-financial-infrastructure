# FIN-PUB-32 — F7 Paper Source / Claim Binding

Status: COMPLETE — PASS

## Paper

F7 — Cross-Jurisdiction Financial Execution and the Boundary of Technical Reach

## Canonical baseline

- suite closure tag: financial-suite-v1.0.0
- F7 release tag: financial-f7-v1.0.0
- controlling separation: technical reach != jurisdictional authority

## Bound publication claims

### F7-PUB-C001

Claim: Technical reach is distinct from jurisdictional authority.

Canonical basis: F7 jurisdictional-boundary semantics; canonical non-equivalence results

### F7-PUB-C002

Claim: Ability to execute across a network or territory does not by itself establish authority to act within that jurisdiction.

Canonical basis: technical reach / jurisdiction authority separation

### F7-PUB-C003

Claim: Cross-border execution capability does not create or expand jurisdictional authority.

Canonical basis: cross-jurisdiction capability / authority non-implication

### F7-PUB-C004

Claim: Authority valid in one jurisdiction does not automatically remain valid in another jurisdiction.

Canonical basis: jurisdiction-scoped authority semantics; scope preservation

### F7-PUB-C005

Claim: Technical routing through a jurisdiction does not itself establish governance authority from that jurisdiction.

Canonical basis: routing / jurisdiction-source separation

### F7-PUB-C006

Claim: Jurisdictional conflict must remain representable rather than collapsed into a single technical execution result.

Canonical basis: multi-jurisdiction conflict model; authority collision semantics

### F7-PUB-C007

Claim: Successful execution under one jurisdictional basis does not resolve incompatible authority conditions in another.

Canonical basis: cross-jurisdiction authority conflict; execution / authority separation

### F7-PUB-C008

Claim: Evidence of geographic or network location does not itself establish applicable jurisdictional authority.

Canonical basis: location evidence / jurisdiction authority separation

### F7-PUB-C009

Claim: A technically valid cross-jurisdiction transaction may remain governance-inadmissible.

Canonical basis: technical validity / jurisdictional admissibility separation; adversarial verification

### F7-PUB-C010

Claim: Successful cross-jurisdiction financial execution does not retroactively establish valid jurisdictional authority.

Canonical basis: execution / jurisdiction authority non-implication; adversarial verification

## Canonical source surfaces

- 10-cross-jurisdiction/FIN_F7_01B_BOUNDARY_FREEZE.md
- 10-cross-jurisdiction/FIN_F7_02_CANONICAL_OBJECT_TYPE_FREEZE.md
- 10-cross-jurisdiction/FIN_F7_03_STATE_CLASSIFICATION_ALGEBRA_FREEZE.md
- 10-cross-jurisdiction/FIN_F7_04_RELATION_PREDICATE_FREEZE.md
- 10-cross-jurisdiction/FIN_F7_05_DECISION_TRANSITION_SEMANTICS_FREEZE.md
- 10-cross-jurisdiction/FIN_F7_06_INVARIANT_DISCOVERY_FREEZE.md
- 10-cross-jurisdiction/FIN_F7_07_PROOF_OBLIGATION_REGISTRY_FREEZE.md
- 10-cross-jurisdiction/FIN_F7_08_FORMAL_PROOF_COUNTEREXAMPLE_TRACEABILITY_DISCHARGE.md
- 10-cross-jurisdiction/FIN_F7_09_REFERENCE_RUNTIME_CONSTRUCTION_CONFORMANCE.md
- 10-cross-jurisdiction/FIN_F7_10_ADVERSARIAL_VERIFICATION_RELEASE_READINESS.md
- 10-cross-jurisdiction/FIN_F7_11_CANONICAL_SURFACE_RELEASE_FREEZE.md
- 10-cross-jurisdiction/runtime/f7_reference_runtime.py
- 15-publications/F7/.gitkeep
- tests/f7/test_f7_reference_runtime.py
- tests/f7_adversarial/test_f7_adversarial.py

## Claim-control rules

- technical reach SHALL NOT be represented as jurisdictional authority
- cross-border capability SHALL NOT create or expand jurisdictional authority
- authority SHALL remain scoped to its valid jurisdictional basis
- technical routing SHALL NOT be represented as jurisdiction-source authority
- jurisdictional conflicts SHALL remain representable rather than collapsed into execution success
- location evidence SHALL NOT by itself establish applicable jurisdictional authority
- successful execution SHALL NOT be used as retroactive jurisdiction-authority evidence
- adversarial results SHALL remain bounded verification evidence
- no production, regulatory, institutional, customer, legal, or external-certification claim is admitted

## Binding status

F7 publication claims are source-bound to the canonical F7 technical and verification surfaces.

The F7 manuscript itself remains unwritten / unfrozen.

## Next

FIN-PUB-33 — F7 MANUSCRIPT CONSTRUCTION
