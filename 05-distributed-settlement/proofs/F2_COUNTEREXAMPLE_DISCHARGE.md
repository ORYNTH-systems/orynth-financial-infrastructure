# FIN-F2-09 — Counterexample Discharge

Each case below defeats an invalid universal implication.

A counterexample discharge does not prove a positive theorem beyond the
non-implication being tested.

---

## CE-001 — Consensus != Authority

State:

Consensus = ACHIEVED

Authority requirement rho_2 = UNSATISFIED

Result:

Consensus true
AuthorityComplete false

Discharges:

Consensus -> AuthorityComplete

Status: COUNTEREXAMPLE-DISCHARGED

---

## CE-002 — Authority != Admissibility

State:

AuthorityComplete = true

TemporalValid = false

Result:

Admissible_d = false

Discharges:

AuthorityComplete -> Admissible_d

Status: COUNTEREXAMPLE-DISCHARGED

---

## CE-003 — Admission != Execution

State:

AdmissibilityResult = ADMIT

No execution attempt occurs

Result:

Executed = false

Discharges:

Admissible_d -> Executed

Status: COUNTEREXAMPLE-DISCHARGED

---

## CE-004 — Execution != Complete Effect

State:

Leg l1 attempted and effects

Leg l2 required but no effect

Result:

Executed = true
AtomicComplete = false
AtomicPartial = true

Discharges:

Executed -> AtomicComplete

Status: COUNTEREXAMPLE-DISCHARGED

---

## CE-005 — Atomic Complete != Final

State:

All AP-required economic effects satisfied

Required legal-domain recognition pending

Result:

AtomicComplete = true
SettlementFinal = false

Discharges:

AtomicComplete -> SettlementFinal

Status: COUNTEREXAMPLE-DISCHARGED

---

## CE-006 — Local Final != Cross-Domain Final

State:

D1 = FINAL

D2 = FINALITY-PENDING

Result:

CrossDomainFinal = false

Discharges:

LocalFinal -> CrossDomainFinal

Status: COUNTEREXAMPLE-DISCHARGED

---

## CE-007 — Final != Irreversible

State:

Settlement receives FINAL classification

Later valid authority permits new reversal execution

Result:

Earlier finality historically exists
State remains changeable

Discharges:

SettlementFinal -> Irreversible

Status: COUNTEREXAMPLE-DISCHARGED

---

## CE-008 — Reconciled != Final

State:

Conflict resolved

External finality requirement pending

Result:

Reconciled = true
SettlementFinal = false

Discharges:

Reconciled -> SettlementFinal

Status: COUNTEREXAMPLE-DISCHARGED

---

## CE-009 — Reconciled != Continuity Preserved

State:

Fork occurred

Historical state reconstructed

Conflict then reconciled

Result:

Reconciled = true
Continuity = RECONSTRUCTED

Discharges:

Reconciled -> ContinuityPreserved

Status: COUNTEREXAMPLE-DISCHARGED

---

## CE-010 — Functional Recovery != Continuity Preserved

State:

System experiences continuity-breaking partial execution

Repair returns service to functional operation

Result:

Functional = true
Historical continuity = BROKEN or RECONSTRUCTED

Discharges:

FunctionalRecovery -> ContinuityPreserved

Status: COUNTEREXAMPLE-DISCHARGED

---

## CE-011 — Endpoint Equivalence != Historical Identity

State:

Original distributed execution partially effects

Compensation later restores economically equivalent balances

Result:

Final economic endpoint equivalent
Execution histories differ

Discharges:

EconomicEndpointEquivalent -> HistoricalIdentity

Status: COUNTEREXAMPLE-DISCHARGED

---

## CE-012 — Majority != Canonicality

State:

Majority observes branch B2

Explicit governing authority selects B1

Result:

Largest/Majority branch != canonical branch

Discharges:

MajorityObservation -> CanonicalBranch

Status: COUNTEREXAMPLE-DISCHARGED
