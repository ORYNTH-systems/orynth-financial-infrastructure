# FIN-AUTH — Authority Invariants

## Purpose

Preserve separation between capability, possession, delegation, and current execution authority.

## Canonical Status

These invariants are architecturally asserted by FIN-ARCH-05.

Assertion does not constitute proof.

FIN-ARCH-06 SHALL assign explicit proof obligations.

---

## FIN-AUTH-001 — Capability Is Not Authority

**Normative rule:** Technical capability to execute SHALL NOT establish execution authority.

**Applies to:** All financially consequential execution

**Inherited / derived from:** UAA

**First major paper:** FOUNDATION

**Status:** ASSERTED

---

## FIN-AUTH-002 — Prior Authorization Is Not Current Authority

**Normative rule:** A prior authorization SHALL NOT establish current authority without execution-time validity.

**Applies to:** All execution attempts

**Inherited / derived from:** UAA/AOMS

**First major paper:** FOUNDATION

**Status:** ASSERTED

---

## FIN-AUTH-003 — Authority Cannot Self-Expand

**Normative rule:** An actor or agent SHALL NOT enlarge its own financial authority through execution, possession, inference, or delegation.

**Applies to:** Human institutional and autonomous actors

**Inherited / derived from:** UAA

**First major paper:** FOUNDATION/F8

**Status:** ASSERTED

---

## FIN-AUTH-004 — Control Is Not Authority

**Normative rule:** Ownership control custody wallet access or key possession SHALL NOT be treated as equivalent to execution authority.

**Applies to:** Financial and digital resources

**Inherited / derived from:** Financial specialization

**First major paper:** F5

**Status:** ASSERTED

---

## FIN-AUTH-005 — Delegation Must Remain Bound

**Normative rule:** Delegated financial authority SHALL remain bound to principal scope action time and governing constraints.

**Applies to:** Delegated actors and autonomous agents

**Inherited / derived from:** UAA/EIP

**First major paper:** F8

**Status:** ASSERTED

---

