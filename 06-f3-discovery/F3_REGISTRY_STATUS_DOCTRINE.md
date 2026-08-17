# F3 Registry Status Doctrine

Status: FROZEN

## Purpose

This doctrine distinguishes registration-time state from current discharge state.

## Originating Registries

The following registries preserve the status assigned when the invariant or proof obligation was created:

- 03-registries/F3_INVARIANT_REGISTER.csv
- 03-registries/F3_PROOF_OBLIGATION_REGISTRY.csv

Their OPEN value means:

**OPEN AT REGISTRATION**

It does not represent the current discharge state.

These registries are historical definition ledgers and SHALL NOT be rewritten to collapse initial registration state into later disposition.

## Current Disposition Authority

Current proof / claim disposition is owned by:

- 03-registries/F3_PROOF_DISCHARGE_REGISTRY.csv

Current closure summary is owned by:

- 03-registries/F3_RUNTIME_PROOF_CLOSURE.csv

Current F3 disposition:

- FORMALLY-PROVED: 12
- COUNTEREXAMPLE-DISCHARGED: 22
- REFERENCE-RUNTIME-CONFORMANT: 6
- OPEN: 0
- TOTAL: 40

## Status Separation

registration-time OPEN
!= current OPEN

proof obligation definition
!= proof disposition

formal proof
!= counterexample discharge

formal proof
!= runtime conformance

counterexample discharge
!= runtime conformance

## Release Rule

F3 release eligibility SHALL be determined from the current discharge and closure registries, not from the originating registration-time OPEN field.

The originating registries remain unchanged for historical traceability.
