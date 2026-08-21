# FIN-F7-06 — Invariant Discovery / Freeze

Status: COMPLETE — PASS

## Canonical family

Cross-Jurisdiction Financial Execution

## Frozen invariant registry

### F7-INV-001 — AUTHORITY

Technical reach SHALL NOT constitute jurisdictional authority.

### F7-INV-002 — AUTHORITY

Cross-border executability SHALL NOT constitute cross-border authorization.

### F7-INV-003 — AUTHORITY

Location SHALL NOT constitute authority.

### F7-INV-004 — AUTHORITY

Network accessibility SHALL NOT constitute legal jurisdiction.

### F7-INV-005 — AUTHORITY

Asset presence SHALL NOT constitute execution authority.

### F7-INV-006 — AUTHORITY

Counterparty presence SHALL NOT constitute jurisdictional consent.

### F7-INV-007 — AUTHORITY

Custody location SHALL NOT constitute governance authority.

### F7-INV-008 — AUTHORITY

Settlement venue SHALL NOT constitute jurisdictional permission.

### F7-INV-009 — AUTHORITY

Regulatory applicability SHALL NOT constitute self-executing authority.

### F7-INV-010 — AUTHORITY

Authority valid in one jurisdiction SHALL NOT be presumed universally valid.

### F7-INV-011 — ADMISSION

F7-ADMIT SHALL require supported jurisdictional authority.

### F7-INV-012 — ADMISSION

F7-ADMIT SHALL require jurisdictional applicability.

### F7-INV-013 — ADMISSION

F7-ADMIT SHALL require valid scope.

### F7-INV-014 — ADMISSION

F7-ADMIT SHALL require temporal validity.

### F7-INV-015 — ADMISSION

F7-ADMIT SHALL require complete consequential jurisdictional coverage.

### F7-INV-016 — ADMISSION

Partial jurisdictional coverage SHALL NOT satisfy complete coverage.

### F7-INV-017 — ADMISSION

A blocking jurisdictional restriction SHALL prohibit ordinary admission.

### F7-INV-018 — ADMISSION

An unresolved blocking jurisdictional conflict SHALL prohibit ordinary admission.

### F7-INV-019 — ADMISSION

Technical reach alone SHALL NOT produce F7-ADMIT.

### F7-INV-020 — ADMISSION

Execution evidence alone SHALL NOT produce F7-ADMIT.

### F7-INV-021 — DELEGATION

Cross-jurisdiction delegation SHALL be source-bound.

### F7-INV-022 — DELEGATION

Cross-jurisdiction delegation SHALL remain scoped.

### F7-INV-023 — DELEGATION

Cross-jurisdiction delegation SHALL remain temporally valid.

### F7-INV-024 — DELEGATION

Cross-jurisdiction delegation SHALL remain jurisdictionally applicable.

### F7-INV-025 — DELEGATION

Cross-jurisdiction delegation SHALL attenuate and SHALL NOT amplify parent authority.

### F7-INV-026 — DELEGATION

Nonattenuated delegation SHALL block ordinary admission.

### F7-INV-027 — MULTI-JURISDICTION

Each consequentially implicated jurisdiction SHALL remain independently representable.

### F7-INV-028 — MULTI-JURISDICTION

Authority established for J_i SHALL NOT be inferred for J_j where i != j.

### F7-INV-029 — MULTI-JURISDICTION

A multi-jurisdiction request SHALL NOT collapse distinct authority domains into one aggregate authorization.

### F7-INV-030 — MULTI-JURISDICTION

Complete coverage SHALL require every consequential jurisdictional boundary to be satisfied.

### F7-INV-031 — MULTI-JURISDICTION

Conflict among jurisdictions SHALL remain explicit until resolved.

### F7-INV-032 — MULTI-JURISDICTION

Jurisdictional conflict SHALL NOT be resolved by selecting the broadest or most permissive authority.

### F7-INV-033 — EVIDENCE

Jurisdictional evidence SHALL NOT constitute authority.

### F7-INV-034 — EVIDENCE

Cross-jurisdiction execution evidence SHALL NOT constitute authorization evidence.

### F7-INV-035 — EVIDENCE

Corroborated evidence SHALL remain distinct from applicable authority.

### F7-INV-036 — EVIDENCE

Stale or insufficient jurisdictional evidence SHALL require deferment or revalidation rather than self-certification.

### F7-INV-037 — RESTRICTION

A jurisdictional restriction SHALL remain distinguishable from an authority source.

### F7-INV-038 — RESTRICTION

Compliance capability SHALL NOT constitute authority to execute.

### F7-INV-039 — RESTRICTION

Applicable blocking restrictions SHALL remain effective despite technical executability.

### F7-INV-040 — RESTRICTION

Restriction resolution SHALL NOT by itself create positive authority.

### F7-INV-041 — DECISION

F7-BLOCK SHALL keep the requested consequential target transition undefined.

### F7-INV-042 — DECISION

F7-DEFER SHALL keep the requested consequential target transition undefined.

### F7-INV-043 — DECISION

F7-REVALIDATE SHALL keep the requested consequential target transition undefined.

### F7-INV-044 — DECISION

F7-REAUTHORIZE SHALL keep the requested consequential target transition undefined.

### F7-INV-045 — DECISION

F7-ADMIT SHALL be necessary but not sufficient for transition existence.

### F7-INV-046 — TRANSITION

A consequential transition SHALL require operation-specific preconditions.

### F7-INV-047 — TRANSITION

A consequential transition SHALL remain within every admitted jurisdictional scope.

### F7-INV-048 — TRANSITION

A consequential transition SHALL remain within every admitted temporal boundary.

### F7-INV-049 — TRANSITION

Successful execution SHALL NOT retroactively establish jurisdictional admissibility.

### F7-INV-050 — TRANSITION

Settlement, ledger inclusion, custody transfer, or cross-border completion SHALL NOT retroactively create authority.

### F7-INV-051 — REVALIDATION

Revalidation SHALL evaluate existing authority applicability and SHALL NOT create new authority.

### F7-INV-052 — REVALIDATION

Changed or stale jurisdictional applicability SHALL require revalidation before ordinary admission.

### F7-INV-053 — REAUTHORIZATION

Reauthorization SHALL derive from a valid external or previously admitted authority source.

### F7-INV-054 — REAUTHORIZATION

Absent, expired, revoked, superseded, insufficient, or inapplicable authority SHALL NOT self-repair through prior execution.

### F7-INV-055 — ALIGNMENT

Jurisdictional alignment SHALL be a classification and SHALL NOT constitute an authority source.

### F7-INV-056 — ALIGNMENT

Technical reach with absent authority SHALL remain representable as misalignment.

### F7-INV-057 — ALIGNMENT

Authority without technical reach SHALL remain distinguishable from technical failure.

### F7-INV-058 — ALIGNMENT

Partial jurisdictional coverage SHALL remain distinguishable from full alignment.

## Frozen invariant families

- AUTHORITY: 10
- ADMISSION: 10
- DELEGATION: 6
- MULTI-JURISDICTION: 6
- EVIDENCE: 4
- RESTRICTION: 4
- DECISION: 5
- TRANSITION: 5
- REVALIDATION: 2
- REAUTHORIZATION: 2
- ALIGNMENT: 4
- TOTAL: 58

## Proof-status control

FIN-F7-06 freezes the invariant registry only.

No invariant is marked formally proved, counterexample-discharged, traceability-discharged, runtime-conformant, or closed by this pass.

Proof status remains unasserted until later proof-obligation and discharge passes.

## Core preserved separations

- technical reach != jurisdictional authority
- one jurisdiction's authority != universal authority
- partial jurisdictional coverage != complete coverage
- evidence != authority
- execution != admissibility
- revalidation != reauthorization
- admission != transition existence

## Freeze control

The F7 invariant registry is frozen.

Proof obligations, formal discharge, runtime components, adversarial tests, and publication surfaces remain unfrozen.

## Next

FIN-F7-07 — PROOF OBLIGATION REGISTRY FREEZE
