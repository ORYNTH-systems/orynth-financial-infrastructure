# Canonical Financial Invariant Architecture

## Purpose

The Financial Invariant Architecture defines normative conditions that SHALL remain true across the ORYNTH Financial Infrastructure architecture and its F1-F8 research families.

These invariants constrain:

- objects,
- actors,
- authority,
- admission,
- transitions,
- execution,
- economic effects,
- settlement,
- remediation,
- evidence,
- finality,
- continuity,
- distributed execution,
- jurisdiction,
- autonomous agency.

---

## Formal Interpretation

Let:

I_F = { I_1, I_2, ..., I_n }

be the canonical invariant set.

For any conformant financial execution history H:

Conformant(H) => forall I in I_F_applicable(H), I(H) = true

Applicability is explicit.

An invariant that is not applicable is not equivalent to a passed invariant.

---

## Critical Architectural Separations

Capability != Authority

Authorization != Admission

TransitionDefined != TransitionAdmissible

Admission != Execution

Execution != EconomicEffect

ExecutionCompletion != SettlementFinality

PartialEffect != NoEffect

Compensation != Reversal

Reversal != HistoricalErasure

Reconciliation != Continuity

Reconstruction != Restoration

EconomicEquivalence != HistoricalEquivalence

Consensus != Authority

LedgerValidity != GovernanceAdmission

Finality != Continuity

Evidence != Authority

AgentCapability != AgentAuthority

---

## Fail-Closed Principle

Where an invariant requires a positive determination before consequential execution and the required determination cannot be established, execution SHALL NOT proceed.

This rule does not mean every indeterminate post-effect state can be converted into NO_EFFECT.

Once economic effect may have occurred, uncertainty must remain explicitly represented.

---

## Post-Effect Principle

The pre-effect fail-closed model and post-effect resolution model are distinct.

Before effect:

invalid / inadmissible execution
-> block
-> no governed effect

After effect:

newly detected invalidity or incomplete execution
-> containment
-> evidence preservation
-> explicit remediation determination
-> independently governed compensation / reversal / reconciliation
-> finality and continuity classification

No automatic rollback is assumed.

---

## Historical Preservation Principle

No later remediation operation may erase the historical fact that an earlier execution or effect occurred.

Compensation, reversal, reconciliation, and reconstruction produce new state and new evidence.

They do not rewrite the past.

---

## Proof Status

FIN-ARCH-05 establishes the invariant specification.

FIN-ARCH-06 SHALL establish the proof-obligation architecture.

No invariant is considered mechanically discharged solely because it appears in this document or registry.
