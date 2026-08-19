# FIN-F4-08 — Formal Proof / Counterexample Discharge

Status: COMPLETE — PASS

## Verified base

- branch: master
- HEAD: 5866e0551e15fd2ebd12a04183db3be8ae032764
- origin/master: 5866e0551e15fd2ebd12a04183db3be8ae032764
- inherited proof-obligation registry: FIN-F4-07-R1
- inherited registration state: 40 OPEN

## Claim discipline

Formal proof != counterexample discharge != runtime conformance.

Runtime-conformance obligations remain OPEN until a reference runtime exists and is mechanically tested.

## FORMALLY-PROVED obligations

### F4-PO-001

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

Representation is typed separately from underlying financial state; F4-O-001 and F4-SD-001 do not confer financial-state truth.

### F4-PO-002

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

Authority is external to record inclusion, persistence, and commitment; none of those relations are authority-creating relations.

### F4-PO-003

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

RecordCommitted and RepresentsFinality are separate predicates, preserving commitment != finality.

### F4-PO-004

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

F4 finality representation records an F3 finality classification but does not constitute that classification.

### F4-PO-005

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

HistoricalRecordExists is independent of current reopening, supersession, and contradiction classifications.

### F4-PO-006

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

F4-REOPEN changes reopening semantics while historical record existence remains separately represented.

### F4-PO-007

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

LedgerContradictionExists is evidentiary; RecordAuthoritySupported remains a separate relation.

### F4-PO-008

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

RecordReconstructed and HistoricalIdentityPreserved are separately typed predicates.

### F4-PO-009

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

Reconstruction status and continuity classification are separate frozen state domains.

### F4-PO-010

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

RepresentsCustody is explicitly distinct from custody authority.

### F4-PO-011

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

Predicates feed decision semantics but are not themselves transition-authorizing outcomes.

### F4-PO-012

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

D_4 is total while Delta_4 is partial; therefore decision outcome and transition existence are non-equivalent.

### F4-PO-013

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

A defined Delta_4 produces a state that requires independent classification.

### F4-PO-014

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

F4-BLOCK semantics explicitly require the corresponding target transition to be undefined.

### F4-PO-015

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

F4-DEFER preserves unresolved status and explicitly withholds target transition authorization.

### F4-PO-016

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

F4-REVALIDATE and F4-REOPEN are distinct decision outcomes with distinct semantics.

### F4-PO-017

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

Reopening changes operative review state but does not remove HistoricalRecordExists.

### F4-PO-018

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

F4-ADMIT makes a transition eligible but does not prove Delta_4 is defined or executed.

### F4-PO-019

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

RecordStateMatchesUnderlyingState is separate from authority, admissibility, and HistoricalIdentityPreserved.

### F4-PO-020

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

The F3/F4 type boundary explicitly separates final financial state from ledger representation.

### F4-PO-029

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

The frozen chain predicate -> D_4 outcome -> Delta_4 eligibility preserves traceability without semantic collapse.

### F4-PO-030

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

Transition attempts are governed by D_4 and therefore traceable to an explicit decision outcome.

### F4-PO-031

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

HistoricalRecordExists persists independently of reopening classification, preserving traceable history.

### F4-PO-032

- status: FORMALLY-PROVED
- discharge basis: frozen F4 type, state, relation, decision, and transition semantics

Contradiction evidence and authority-resolution predicates are separately typed and independently evaluable.

## COUNTEREXAMPLE-DISCHARGED obligations

### F4-PO-021

- status: COUNTEREXAMPLE-DISCHARGED
- discharge basis: explicit separating witness

A ledger records balance=100 while admissible external evidence establishes balance=80; representation exists but underlying state differs.

### F4-PO-022

- status: COUNTEREXAMPLE-DISCHARGED
- discharge basis: explicit separating witness

A record is durably committed by a process lacking current delegated authority; commitment exists without authority.

### F4-PO-023

- status: COUNTEREXAMPLE-DISCHARGED
- discharge basis: explicit separating witness

A record remains committed after the underlying F3 state is reopened; commitment persists while current finality does not.

### F4-PO-024

- status: COUNTEREXAMPLE-DISCHARGED
- discharge basis: explicit separating witness

A record is reconstructed from incomplete evidence to the same visible fields while provenance differs; content restoration does not establish historical identity.

### F4-PO-025

- status: COUNTEREXAMPLE-DISCHARGED
- discharge basis: explicit separating witness

A ledger records Party A as custodian although the applicable authority grant has expired; custody representation exists without custody authority.

### F4-PO-026

- status: COUNTEREXAMPLE-DISCHARGED
- discharge basis: explicit separating witness

D_4 returns F4-ADMIT, but a required transition precondition fails before Delta_4 is defined; admission occurs without transition.

### F4-PO-027

- status: COUNTEREXAMPLE-DISCHARGED
- discharge basis: explicit separating witness

A record exactly matches underlying financial data but was produced outside valid scope; equality holds while governance admissibility fails.

### F4-PO-028

- status: COUNTEREXAMPLE-DISCHARGED
- discharge basis: explicit separating witness

Underlying F3 financial state is reopened while a ledger still displays the historical final representation; ledger and current financial state diverge.

## OPEN runtime-conformance obligations

### F4-PO-033

- status: OPEN
- required future discharge class: REFERENCE-RUNTIME-CONFORMANT

### F4-PO-034

- status: OPEN
- required future discharge class: REFERENCE-RUNTIME-CONFORMANT

### F4-PO-035

- status: OPEN
- required future discharge class: REFERENCE-RUNTIME-CONFORMANT

### F4-PO-036

- status: OPEN
- required future discharge class: REFERENCE-RUNTIME-CONFORMANT

### F4-PO-037

- status: OPEN
- required future discharge class: REFERENCE-RUNTIME-CONFORMANT

### F4-PO-038

- status: OPEN
- required future discharge class: REFERENCE-RUNTIME-CONFORMANT

### F4-PO-039

- status: OPEN
- required future discharge class: REFERENCE-RUNTIME-CONFORMANT

### F4-PO-040

- status: OPEN
- required future discharge class: REFERENCE-RUNTIME-CONFORMANT

## Frozen architecture boundaries

semantic fact / predicate != decision outcome != transition existence != resulting record-state

final financial state != ledger representation of final financial state

record commitment != financial finality

record reconstruction != historical identity

record reconstruction != continuity preservation

recorded custody != custody authority

## Release controls

Formal discharge performed for 24 obligations.
Counterexample discharge performed for 8 obligations.
Runtime-conformance obligations remaining OPEN: 8.
No runtime conformance claimed.
No runtime created.
No staging performed.
No commit performed.
No tag created.
No push performed.

## Next

FIN-F4-09 — REFERENCE RUNTIME CONSTRUCTION AND CONFORMANCE
