# F1 Reference Runtime

## Purpose

This package implements the already-established F1 post-effect financial model.

It introduces no new financial semantics.

## Pipeline

FinancialExecutionEvent
-> Effect Classification
-> independent Compensation/Reversal Admission
-> Consequential Boundary Permit
-> Reconciliation
-> Continuity Classification
-> Evidence Recording

## Boundary Rule

Compensation and reversal do not construct permits.

They invoke:

evaluate_admission()

and then:

issue_boundary_permit().

boundary.py is the sole implementation surface authorized to instantiate
BoundaryPermit.

## Evidence Rule

The public EvidenceLedger API is append-oriented.

records() and history_for() return deep copies so callers cannot mutate retained
records through returned object references.

This is NOT represented as cryptographic immutability or durable persistence.

## Non-Claims

FIN-F1-08 does not establish:

- production readiness;
- institutional settlement correctness;
- bank-specific correctness;
- cryptographic immutability;
- distributed consensus;
- jurisdictional correctness;
- external certification;
- universal formal verification of Python behavior.
