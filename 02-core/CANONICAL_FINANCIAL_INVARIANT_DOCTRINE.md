# Canonical Financial Invariant Doctrine

## Purpose

Financial Infrastructure invariants define properties that SHALL remain true across all conformant financial execution paths.

An invariant is not a proof.

An invariant defines a required property.

Proof obligations, verification mechanisms, and runtime enforcement will be assigned in later architecture passes.

---

## General Rule

For every governed financial execution event e and every consequential transition tau:

If an invariant applicable to e or tau is not established, execution SHALL NOT be treated as conformant.

---

## Invariant Families

FIN-OBJ-*  Object / semantic separation

FIN-AUTH-* Authority

FIN-ADM-*  Admissibility

FIN-EFF-*  Effectuation

FIN-SET-*  Settlement

FIN-CMP-*  Compensation

FIN-REV-*  Reversal

FIN-REC-*  Reconciliation / reconstruction

FIN-FIN-*  Finality

FIN-CNT-*  Continuity

FIN-EVD-*  Evidence

FIN-DST-*  Distributed / multiparty

FIN-JUR-*  Jurisdiction

FIN-AGT-*  Autonomous agency

---

## Governing Architectural Principles

Capability does not imply authority.

Possession does not imply authority.

Prior authorization does not imply current admissibility.

Execution completion does not imply settlement finality.

Settlement finality does not imply continuity preservation.

Compensation does not erase original execution history.

Reversal does not establish historical non-occurrence.

Economic equivalence does not imply historical-state equivalence.

Consensus does not imply authority.

Cryptographic control does not imply authority.

Programmable validity does not imply execution admissibility.

Evidence does not create authority.

Recovery does not imply restoration.

Reconstruction does not imply uninterrupted continuity.

---

## Failure Semantics

Violation of a mandatory invariant produces one of:

- execution denial,
- effectuation denial,
- containment,
- reconciliation requirement,
- indeterminate classification,
- continuity failure classification,
- non-conformance.

The exact enforcement mapping will be assigned in FIN-ARCH-07.
