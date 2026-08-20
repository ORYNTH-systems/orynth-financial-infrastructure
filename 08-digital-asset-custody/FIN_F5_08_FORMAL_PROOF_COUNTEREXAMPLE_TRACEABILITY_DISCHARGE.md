# FIN-F5-08 — Formal Proof / Counterexample / Traceability Discharge

Status: COMPLETE — PASS

## Formal / non-equivalence / safety discharge

### F5-PO-001

- status: FORMALLY-PROVED
- witness: Capability and governance authority are independently typed.

### F5-PO-002

- status: FORMALLY-PROVED
- witness: Key possession is represented independently from delegated authority.

### F5-PO-003

- status: FORMALLY-PROVED
- witness: Technical signature validity is independent from governance authorization.

### F5-PO-004

- status: FORMALLY-PROVED
- witness: Threshold satisfaction is independent from governance authorization.

### F5-PO-005

- status: FORMALLY-PROVED
- witness: Custody possession and custody authority are separately represented.

### F5-PO-006

- status: FORMALLY-PROVED
- witness: Wallet/address control is representational capability, not financial authority.

### F5-PO-007

- status: FORMALLY-PROVED
- witness: Delegated authority requires an applicable source authority.

### F5-PO-008

- status: FORMALLY-PROVED
- witness: Delegation is constrained by attenuation relative to source authority.

### F5-PO-009

- status: FORMALLY-PROVED
- witness: Admission conditions require applicable scope.

### F5-PO-010

- status: FORMALLY-PROVED
- witness: Admission conditions require current temporal validity.

### F5-PO-011

- status: FORMALLY-PROVED
- witness: Key lifecycle permission and governance authority validity are distinct domains.

### F5-PO-012

- status: FORMALLY-PROVED
- witness: Recovered cryptographic capability does not establish restored authority.

### F5-PO-013

- status: FORMALLY-PROVED
- witness: Rotated key material does not establish authority continuity.

### F5-PO-014

- status: FORMALLY-PROVED
- witness: Revocation changes current validity without erasing historical evidence.

### F5-PO-015

- status: FORMALLY-PROVED
- witness: Execution evidence and authority evidence are separately typed.

### F5-PO-016

- status: FORMALLY-PROVED
- witness: Conflict detection is evidentiary and does not select valid authority.

### F5-PO-017

- status: FORMALLY-PROVED
- witness: Alignment is derived classification, not authority source.

### F5-PO-018

- status: FORMALLY-PROVED
- witness: Predicate truth precedes decision and cannot itself authorize transition.

### F5-PO-019

- status: FORMALLY-PROVED
- witness: D_5 decision outcome is distinct from Delta_5 transition existence.

### F5-PO-020

- status: FORMALLY-PROVED
- witness: Defined transition remains distinct from resulting state classification.

### F5-PO-021

- status: FORMALLY-PROVED
- witness: F5-BLOCK requires target transition to remain undefined.

### F5-PO-022

- status: FORMALLY-PROVED
- witness: F5-DEFER preserves unresolved state and does not authorize target transition.

### F5-PO-023

- status: FORMALLY-PROVED
- witness: F5-REVALIDATE does not create, restore, or extend authority.

### F5-PO-024

- status: FORMALLY-PROVED
- witness: F5-REAUTHORIZE requires authority re-establishment independent of capability restoration.

### F5-PO-025

- status: FORMALLY-PROVED
- witness: F5-ADMIT denotes eligibility, not proof of execution.

### F5-PO-026

- status: FORMALLY-PROVED
- witness: Admission requires authority support beyond key/signature/threshold/custody evidence.

### F5-PO-027

- status: FORMALLY-PROVED
- witness: Capability restoration and authority continuity are independently classified.

### F5-PO-028

- status: FORMALLY-PROVED
- witness: F5 inherits F3 custody/finality determinations rather than redefining them.

### F5-PO-029

- status: FORMALLY-PROVED
- witness: F5 inherits F4 ledger representation without treating record control as authority.

### F5-PO-030

- status: FORMALLY-PROVED
- witness: Core F5 typing prevents cryptographic or ledger control from self-creating authority.

## Counterexample discharge

### F5-PO-031

- status: COUNTEREXAMPLE-DISCHARGED
- witness: Actor possesses signing hardware and key access but no current authority grant.

### F5-PO-032

- status: COUNTEREXAMPLE-DISCHARGED
- witness: Private key is held after the associated delegation expired.

### F5-PO-033

- status: COUNTEREXAMPLE-DISCHARGED
- witness: Signature verifies cryptographically while the requested operation lies outside delegated scope.

### F5-PO-034

- status: COUNTEREXAMPLE-DISCHARGED
- witness: Threshold quorum is technically satisfied using shares whose governing authority has been revoked.

### F5-PO-035

- status: COUNTEREXAMPLE-DISCHARGED
- witness: Lost key is recovered while the original authority grant remains expired or revoked.

### F5-PO-036

- status: COUNTEREXAMPLE-DISCHARGED
- witness: Key rotation completes but authority source continuity is unresolved.

### F5-PO-037

- status: COUNTEREXAMPLE-DISCHARGED
- witness: Signature, key possession, and threshold checks all succeed while authority-source evidence is absent.

### F5-PO-038

- status: COUNTEREXAMPLE-DISCHARGED
- witness: Ledger identifies wallet control while governance authority belongs elsewhere or is revoked.

### F5-PO-039

- status: COUNTEREXAMPLE-DISCHARGED
- witness: Custodian physically or technically controls the asset without current custody authority.

### F5-PO-040

- status: COUNTEREXAMPLE-DISCHARGED
- witness: Cryptographic access is restored after compromise while governance continuity remains NOT_ESTABLISHED.

## Traceability discharge

### F5-PO-041

- status: TRACEABILITY-DISCHARGED
- witness: Frozen chain: F5 predicate facts -> D_5 decision -> Delta_5 eligibility -> resulting-state classification.

### F5-PO-042

- status: TRACEABILITY-DISCHARGED
- witness: Delta_5 is partial and governed by an explicit total D_5 decision on admissible requests.

### F5-PO-043

- status: TRACEABILITY-DISCHARGED
- witness: DelegatedAuthorityActive and AuthoritySourceSupported preserve source-bound authority traceability.

### F5-PO-044

- status: TRACEABILITY-DISCHARGED
- witness: Revocation modifies current lifecycle/authority validity while historical execution and authority evidence remain independently representable.

## Runtime-conformance obligations preserved OPEN

### F5-PO-045

- status: OPEN
- class: RUNTIME-CONFORMANCE

### F5-PO-046

- status: OPEN
- class: RUNTIME-CONFORMANCE

### F5-PO-047

- status: OPEN
- class: RUNTIME-CONFORMANCE

### F5-PO-048

- status: OPEN
- class: RUNTIME-CONFORMANCE

### F5-PO-049

- status: OPEN
- class: RUNTIME-CONFORMANCE

### F5-PO-050

- status: OPEN
- class: RUNTIME-CONFORMANCE

### F5-PO-051

- status: OPEN
- class: RUNTIME-CONFORMANCE

### F5-PO-052

- status: OPEN
- class: RUNTIME-CONFORMANCE

## Disposition

- FORMALLY-PROVED: 30
- COUNTEREXAMPLE-DISCHARGED: 10
- TRACEABILITY-DISCHARGED: 4
- RUNTIME-CONFORMANCE OPEN: 8
- TOTAL: 52

## Control

No runtime-conformance claim is made by this pass.
No runtime is created by this pass.
No staging, commit, tag, or push is performed.

## Next

FIN-F5-09 — REFERENCE RUNTIME CONSTRUCTION AND CONFORMANCE
