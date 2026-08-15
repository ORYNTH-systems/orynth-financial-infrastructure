# FIN-SET — Canonical Proof Obligations

## Status

All obligations in this file begin OPEN.

No obligation is proved or discharged by FIN-ARCH-06.

---

## PO-FIN-SET-001 — Execution Is Not Settlement

**Invariant:** FIN-SET-001

**Formal target:** Show that settlement progression remains separately represented from execution completion and that each consequential settlement mutation preserves explicit lineage.

**Required premises:** Settlement object; originating execution event; prior settlement state; resulting settlement state; mutation evidence.

**Counterexample condition:** Settlement mutates without explicit transition/evidence lineage or execution completion is treated as settlement finality.

**Evidence requirement:** Settlement-state transition trace; originating event binding; evidence lineage; finality status.

**Implementation requirement:** Reference runtime must maintain explicit settlement lifecycle and transition lineage.

**Verification requirement:** Settlement-state mutation, partial settlement, and lineage tests.

**Dependencies:** UES/Financial specialization

**First major paper:** F1

**Discharge state:** OPEN

---

## PO-FIN-SET-002 — Partial Settlement Must Remain Explicit

**Invariant:** FIN-SET-002

**Formal target:** Show that settlement progression remains separately represented from execution completion and that each consequential settlement mutation preserves explicit lineage.

**Required premises:** Settlement object; originating execution event; prior settlement state; resulting settlement state; mutation evidence.

**Counterexample condition:** Settlement mutates without explicit transition/evidence lineage or execution completion is treated as settlement finality.

**Evidence requirement:** Settlement-state transition trace; originating event binding; evidence lineage; finality status.

**Implementation requirement:** Reference runtime must maintain explicit settlement lifecycle and transition lineage.

**Verification requirement:** Settlement-state mutation, partial settlement, and lineage tests.

**Dependencies:** Financial specialization

**First major paper:** F1

**Discharge state:** OPEN

---

## PO-FIN-SET-003 — Settlement State Must Preserve Lineage

**Invariant:** FIN-SET-003

**Formal target:** Show that settlement progression remains separately represented from execution completion and that each consequential settlement mutation preserves explicit lineage.

**Required premises:** Settlement object; originating execution event; prior settlement state; resulting settlement state; mutation evidence.

**Counterexample condition:** Settlement mutates without explicit transition/evidence lineage or execution completion is treated as settlement finality.

**Evidence requirement:** Settlement-state transition trace; originating event binding; evidence lineage; finality status.

**Implementation requirement:** Reference runtime must maintain explicit settlement lifecycle and transition lineage.

**Verification requirement:** Settlement-state mutation, partial settlement, and lineage tests.

**Dependencies:** UES/POB

**First major paper:** F1

**Discharge state:** OPEN

---

## PO-FIN-SET-004 — Settlement Completion Is Not Governance Validity

**Invariant:** FIN-SET-004

**Formal target:** Show that settlement progression remains separately represented from execution completion and that each consequential settlement mutation preserves explicit lineage.

**Required premises:** Settlement object; originating execution event; prior settlement state; resulting settlement state; mutation evidence.

**Counterexample condition:** Settlement mutates without explicit transition/evidence lineage or execution completion is treated as settlement finality.

**Evidence requirement:** Settlement-state transition trace; originating event binding; evidence lineage; finality status.

**Implementation requirement:** Reference runtime must maintain explicit settlement lifecycle and transition lineage.

**Verification requirement:** Settlement-state mutation, partial settlement, and lineage tests.

**Dependencies:** Financial specialization

**First major paper:** F3

**Discharge state:** OPEN

---

## PO-FIN-SET-005 — No Silent Settlement Mutation

**Invariant:** FIN-SET-005

**Formal target:** Show that settlement progression remains separately represented from execution completion and that each consequential settlement mutation preserves explicit lineage.

**Required premises:** Settlement object; originating execution event; prior settlement state; resulting settlement state; mutation evidence.

**Counterexample condition:** Settlement mutates without explicit transition/evidence lineage or execution completion is treated as settlement finality.

**Evidence requirement:** Settlement-state transition trace; originating event binding; evidence lineage; finality status.

**Implementation requirement:** Reference runtime must maintain explicit settlement lifecycle and transition lineage.

**Verification requirement:** Settlement-state mutation, partial settlement, and lineage tests.

**Dependencies:** UES/Financial specialization

**First major paper:** F1

**Discharge state:** OPEN

---

