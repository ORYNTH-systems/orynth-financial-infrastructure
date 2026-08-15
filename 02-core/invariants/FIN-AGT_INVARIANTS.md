# FIN-AGT — Autonomous Agency Invariants

## Purpose

Bind autonomous financial execution to a valid principal, delegation, scope, and current authority.

## Canonical Status

These invariants are architecturally asserted by FIN-ARCH-05.

Assertion does not constitute proof.

FIN-ARCH-06 SHALL assign explicit proof obligations.

---

## FIN-AGT-001 — Agent Capability Is Not Economic Authority

**Normative rule:** An autonomous agent's ability to construct sign transmit or execute a financial action SHALL NOT establish authority to do so.

**Applies to:** Autonomous economic agents

**Inherited / derived from:** UAA

**First major paper:** F8

**Status:** ASSERTED

---

## FIN-AGT-002 — Agent Must Resolve To Principal

**Normative rule:** Autonomous financial authority SHALL resolve to a valid principal or other explicitly recognized authority origin.

**Applies to:** Autonomous agents

**Inherited / derived from:** UAA/Financial specialization

**First major paper:** F8

**Status:** ASSERTED

---

## FIN-AGT-003 — Delegation Attenuates

**Normative rule:** A delegated autonomous agent SHALL NOT possess authority broader than the authority validly delegated to it.

**Applies to:** Delegated agents

**Inherited / derived from:** UAA/EIP

**First major paper:** F8

**Status:** ASSERTED

---

## FIN-AGT-004 — Agent Cannot Self-Authorize

**Normative rule:** An autonomous agent SHALL NOT create or validate the authority required for its own consequential financial execution unless explicitly authorized by a distinct upstream mechanism.

**Applies to:** Autonomous execution

**Inherited / derived from:** UAA

**First major paper:** F8

**Status:** ASSERTED

---

## FIN-AGT-005 — Agent Intent Drift Invalidates Admission

**Normative rule:** Material divergence between authorized economic intent and current agent action SHALL invalidate the inherited admission basis.

**Applies to:** Autonomous agents

**Inherited / derived from:** AOMS/EIP

**First major paper:** F8

**Status:** ASSERTED

---

