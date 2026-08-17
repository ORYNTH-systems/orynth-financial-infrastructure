# F3 Canonical Objects

Status: FORMALIZED

## Core Objects

### F3-O-001 — Financial Obligation

A typed consequential requirement binding one or more parties to a financial performance condition.

An obligation is not equivalent to:

- an instruction;
- an execution;
- a transaction record;
- a ledger entry;
- a payment attempt;
- a settlement result.

---

### F3-O-002 — Obligation Performance

Observed consequential performance against a Financial Obligation.

Performance may be:

- NONE
- PARTIAL
- COMPLETE
- EXCESS
- CONFLICTING
- UNDETERMINED

---

### F3-O-003 — Obligation Residual

The portion or dimension of an obligation not discharged by observed valid performance.

Residual existence does not imply authority to repair, compensate, reverse, or continue execution.

---

### F3-O-004 — Custody State

The currently evidenced state of control, possession, entitlement, or holding with respect to a financial asset or obligation-bearing object.

Custody state is not equivalent to custody authority.

---

### F3-O-005 — Custody Authority

The authority under which a custody state, transfer, mutation, release, or disposition may be treated as admissible.

Possession does not create Custody Authority.

---

### F3-O-006 — Custody Transfer

A transition between custody states involving an asset, entitlement, position, obligation, or governed financial object.

Transfer occurrence is not equivalent to valid transfer completion.

---

### F3-O-007 — Finality Requirement Set

The typed set of conditions required before a specific financial state may be classified as final.

---

### F3-O-008 — Finality Evidence Set

Evidence supporting or contradicting satisfaction of a Finality Requirement Set.

Evidence does not itself create finality.

---

### F3-O-009 — Finality Classification

A classification assigned to a financial state after evaluation against current Finality Requirements and admissible evidence.

---

### F3-O-010 — Consequential Closure

A state in which the governed financial consequence is treated as closed for the relevant request, scope, authority, obligation, and finality domain.

Closure is request-relative and scope-relative.

---

### F3-O-011 — Reopenability State

The current classification of whether a previously closed or final state may validly be reopened under governing rules.

---

### F3-O-012 — Finality Conflict

A conflict in which two or more admissible or purportedly admissible states, records, authorities, or evidence sets yield incompatible finality conclusions.

---

### F3-O-013 — Post-Finality Contradiction

Evidence or state appearing after a finality classification that contradicts one or more conditions required for current finality.

Historical final classification is preserved as historical evidence even when current classification changes.

---

### F3-O-014 — Closure Witness

The reconstructable evidence bundle sufficient to demonstrate why a Consequential Closure classification was reached.

A Closure Witness is evidence of classification, not authority to create classification.
