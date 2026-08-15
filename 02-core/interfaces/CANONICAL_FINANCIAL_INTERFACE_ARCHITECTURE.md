# Canonical Financial Interface Architecture

## Governing Rule

Interfaces transfer typed information, decisions, evidence, or execution-control outputs.

An interface does not transfer more authority than the underlying authority model permits.

---

## Interface Classes

### Evaluative Interfaces

Examples:

- authority resolution,
- admission,
- effect classification,
- finality,
- continuity,
- jurisdiction,
- intent continuity.

These do not directly produce economic mutation.

---

### Consequential Interfaces

Examples:

- execution control,
- settlement transition,
- containment,
- compensation execution,
- reversal execution,
- distributed settlement,
- machine-originated execution.

These interfaces may participate in consequential state mutation and therefore require explicit upstream admission or enforcement dependencies.

---

## Non-Authority Rule

The following interface outputs SHALL NOT themselves constitute new authority:

- ResolvedAuthorityState
- AdmissionDecision outside its bound attempt
- EconomicEffectClassification
- SettlementStateTransition
- CompensationRequirement
- ReversalRequirement
- ReconciliationResult
- EvidenceObject
- FinalityClassification
- ContinuityClassification
- ConsensusAuthorityAssessment
- OracleIntegrityAssessment
- ResolvedJurisdictionState
- PrincipalResolution
- IntentContinuityAssessment

---

## Attempt Binding

Admission and execution-control interfaces SHALL remain bound to the specific execution attempt for which they were produced.

No output may be replayed to authorize a new attempt unless the upstream authority architecture explicitly permits it.
