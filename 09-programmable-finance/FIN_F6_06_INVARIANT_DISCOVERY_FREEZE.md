# FIN-F6-06 — Invariant Discovery / Freeze

Status: COMPLETE — PASS

## Canonical family

Smart-Contract and Programmable Financial Authority

## Frozen canonical invariant registry

### F6-INV-001 — AUTHORITY

Executable code SHALL NOT constitute governance authority.

### F6-INV-002 — AUTHORITY

Deployed code SHALL NOT self-create programmable financial authority.

### F6-INV-003 — AUTHORITY

Contract ownership or administrator capability SHALL NOT by itself constitute governance authority.

### F6-INV-004 — AUTHORITY

Upgrade capability SHALL NOT by itself authorize alteration of a governance boundary.

### F6-INV-005 — AUTHORITY

Oracle input SHALL NOT constitute governance authority.

### F6-INV-006 — AUTHORITY

Condition satisfaction SHALL NOT constitute financial authorization.

### F6-INV-007 — AUTHORITY

Automation SHALL NOT constitute principal authority.

### F6-INV-008 — AUTHORITY

Ledger or on-chain acceptance SHALL NOT constitute governance authority.

### F6-INV-009 — ADMISSION

A technically valid invocation SHALL NOT imply F6-ADMIT.

### F6-INV-010 — ADMISSION

Deterministic execution SHALL NOT imply governance admissibility.

### F6-INV-011 — ADMISSION

Successful contract execution SHALL NOT retroactively establish admissibility.

### F6-INV-012 — ADMISSION

A satisfied programmable condition SHALL NOT override absent or invalid authority.

### F6-INV-013 — ADMISSION

Verified oracle data SHALL NOT override absent or invalid authority.

### F6-INV-014 — ADMISSION

Privileged control availability SHALL NOT override absent or invalid authority.

### F6-INV-015 — ADMISSION

F6-BLOCK SHALL keep the blocked target transition undefined.

### F6-INV-016 — ADMISSION

F6-DEFER SHALL keep the requested target transition undefined.

### F6-INV-017 — ADMISSION

F6-REVALIDATE SHALL keep the ordinary target transition undefined until renewed validation and a new decision.

### F6-INV-018 — ADMISSION

F6-REAUTHORIZE SHALL keep the ordinary target transition undefined until authority is independently re-established.

### F6-INV-019 — DELEGATION

Delegated programmable authority SHALL remain source-bound.

### F6-INV-020 — DELEGATION

Delegated programmable authority SHALL remain scoped.

### F6-INV-021 — DELEGATION

Delegated programmable authority SHALL remain temporally valid.

### F6-INV-022 — DELEGATION

Delegated programmable authority SHALL remain attenuated relative to its parent authority.

### F6-INV-023 — DELEGATION

A delegate SHALL NOT amplify authority beyond its admitted source.

### F6-INV-024 — STATE

Contract state SHALL NOT be treated as constitutive authoritative economic truth.

### F6-INV-025 — STATE

Contract-state corroboration SHALL NOT constitute authority.

### F6-INV-026 — STATE

Execution evidence SHALL remain distinct from authority evidence.

### F6-INV-027 — STATE

Technical execution success SHALL remain distinct from authorized consequential effect.

### F6-INV-028 — UPGRADE

Contract mutation SHALL NOT imply authority renewal.

### F6-INV-029 — UPGRADE

Upgrade execution SHALL NOT prove that upgrade authority was valid.

### F6-INV-030 — UPGRADE

Immutability SHALL NOT eliminate governance revalidation or reauthorization requirements.

### F6-INV-031 — ORACLE

Oracle truth assertions SHALL remain data claims rather than authority grants.

### F6-INV-032 — ORACLE

Stale, conflicted, absent, or invalid oracle inputs SHALL NOT support ordinary admitted execution when the oracle is required.

### F6-INV-033 — PRIVILEGED-CONTROL

Pause, resume, kill, emergency, administrator, or owner capabilities SHALL require independent authority when consequential.

### F6-INV-034 — PRIVILEGED-CONTROL

Possession of privileged credentials SHALL NOT self-bootstrap programmable authority.

### F6-INV-035 — TRANSITION

F6-ADMIT SHALL NOT alone guarantee transition existence.

### F6-INV-036 — TRANSITION

A consequential transition SHALL require operation-specific preconditions in addition to F6-ADMIT.

### F6-INV-037 — TRANSITION

A consequential transition SHALL remain within admitted scope and temporal boundaries.

### F6-INV-038 — TRANSITION

A consequential transition SHALL preserve required execution and authority evidence.

### F6-INV-039 — CONFLICT

A blocking programmable-authority conflict SHALL prohibit ordinary admitted consequential execution.

### F6-INV-040 — CONFLICT

Conflict detection SHALL NOT by itself resolve authority source, authority status, or governance authorization.

## Frozen invariant summary

- total canonical invariants: 40
- core separation: executable code != governance authority
- technical execution != governance admissibility
- oracle data != authority
- privileged capability != authority
- upgrade capability != authority
- contract state != authoritative economic truth
- execution evidence != authority evidence
- delegation attenuates; it does not amplify

## Invariant status

All 40 canonical F6 invariants are frozen as requirements.

Formal proof, counterexample discharge, traceability discharge, and runtime conformance have not yet been asserted.

Each invariant remains subject to proof-obligation binding in FIN-F6-07.

## Freeze control

The F6 invariant registry is frozen.

Proof obligations, proof dispositions, runtime components, tests, adversarial surfaces, and release surfaces remain unfrozen.

## Next

FIN-F6-07 — PROOF OBLIGATION REGISTRY FREEZE
