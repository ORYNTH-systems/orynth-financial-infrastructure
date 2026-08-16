# Canonical Financial Component Architecture

## Purpose

Components assign executable architectural responsibility.

A component:

- consumes canonical typed objects,
- reads defined state,
- evaluates or executes defined transitions,
- preserves applicable invariants,
- emits defined outputs,
- exposes one or more canonical interfaces.

A component does not automatically prove the invariant it enforces.

---

## Ownership Rule

Every canonical financial component SHALL have exactly one primary responsibility.

Multiple components may cooperate on one transition, but responsibility SHALL NOT
be silently duplicated.

---

## Upstream Rule

Financial components may consume inherited semantics from:

- UAA
- EIP
- AOMS
- Proof-of-Block
- UES
- Banking Reasoning Lab
- Morning Star Finance
- DEI

They SHALL NOT silently redefine those upstream semantics.

---

## Fail-Closed Rule

Where a component is responsible for authority, admissibility, or effectuation
gating, indeterminate required state SHALL NOT be converted into permissive
execution.

---

## Evidence Rule

Every consequential decision or state-changing component SHALL expose enough
information for independent evidence generation and later reconstruction.

---

## Classification Rule

Classification components SHALL distinguish classification from mutation.

Examples:

Finality Classifier does not itself make settlement final.

Continuity Classifier does not itself restore continuity.

Partial-Effect Detector does not itself repair financial state.

Jurisdiction State Resolver does not itself grant authority.

---

## No Self-Authorization

No component responsible for:

- compensation,
- reversal,
- settlement,
- autonomous execution,
- smart-contract execution,
- distributed settlement

may derive execution authority solely from the state it is attempting to repair,
complete, reverse, or execute.

---

## Component Families

FI-CORE-*   Cross-family core

FI-EFF-*    Effectuation

FI-SET-*    Settlement

FI-CMP-*    Compensation

FI-REV-*    Reversal

FI-REC-*    Reconciliation / reconstruction

FI-FIN-*    Finality

FI-CNT-*    Continuity

FI-EVD-*    Evidence

FI-DST-*    Distributed / multiparty

FI-LED-*    Ledger

FI-AST-*    Digital asset / custody

FI-PRG-*    Programmable finance

FI-JUR-*    Jurisdiction

FI-AGT-*    Autonomous economic agency
