# F3 Counterexample Discharge

Status: DISCHARGED

## Counterexample Doctrine

A counterexample discharges only the corresponding non-implication.

It does not prove a stronger positive implication.

---

## CE-01 — Execution Complete But Non-Final

State:

execution = complete
authority = expired
finality = blocked

Therefore:

execution != finality

Discharges F3-PO-001 and supports F3-PO-026.

---

## CE-02 — Effect Occurred But Obligation Unsatisfied

State:

required obligation = 100
valid observed effect = 60
residual = 40

Therefore:

effect occurrence != obligation satisfaction

Discharges F3-PO-002.

---

## CE-03 — Obligation Satisfied But Custody Invalid

State:

obligation satisfaction = true
custody transfer record = present
custody authority = invalid

Therefore:

obligation satisfaction != custody validity

Discharges F3-PO-003.

---

## CE-04 — Possession Without Custody Authority

State:

party physically or cryptographically controls asset
applicable custody authority = absent

Therefore:

custody possession != custody authority

Discharges F3-PO-004 and F3-PO-030.

---

## CE-05 — Possession Without Finality

State:

custody possession = true
finality conflict = unresolved

Therefore:

custody possession != finality

Discharges F3-PO-005.

---

## CE-06 — Transfer Occurred But Transfer Not Complete

State:

one custody leg executed
required receiving acknowledgement absent

Therefore:

custody transfer occurrence != custody transfer completion

Discharges F3-PO-006.

---

## CE-07 — Atomic Completion But Non-Final

State:

all execution legs complete atomically
applicable finality authority = stale

Therefore:

atomic completion != finality

Discharges F3-PO-007 and F3-PO-028.

---

## CE-08 — Consensus But Non-Final

State:

all participating nodes agree
required external authority = absent

Therefore:

consensus != finality

Discharges F3-PO-008 and F3-PO-027.

---

## CE-09 — Reconciled But Non-Final

State:

records reconcile numerically
custody evidence remains conflicted

Therefore:

reconciliation != finality

Discharges F3-PO-009 and F3-PO-029.

---

## CE-10 — Final But Reversible

State:

current finality requirements satisfied
governing framework permits later authorized reversal

Therefore:

finality != irreversibility

Discharges F3-PO-010 and F3-PO-031.

---

## CE-11 — Final But Continuity Not Preserved

State:

current finality classification valid
historical chain reconstructed after discontinuity

Therefore:

finality != continuity preservation

Discharges F3-PO-011 and F3-PO-032.

---

## CE-12 — Final But Historical Identity Different

State:

economic endpoint matches prior amount
intervening compensated path differs historically

Therefore:

finality != historical identity

Discharges F3-PO-012.

---

## CE-13 — Final But Not Consequentially Closed

State:

settlement state satisfies finality requirements
separate consequential obligation remains open

Therefore:

finality != consequential closure

Discharges F3-PO-013.

---

## CE-14 — Closed But Reopenable

State:

closure = complete
new admissible contradiction activates explicit reopen transition

Therefore:

consequential closure != impossibility of reopening

Discharges F3-PO-033.

---

## CE-15 — Historically Final Then Invalidated

State at t:

FINALITY_DOMAIN_COMPLETE

New admissible evidence at t+1 contradicts a required finality predicate.

Current state becomes FINALITY_INVALIDATED while historical finality remains recorded.

Therefore:

post-finality contradiction != historical non-occurrence

Discharges F3-PO-034.
