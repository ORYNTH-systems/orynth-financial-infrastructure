# FIN-CMP — Compensation Invariants

## Purpose

Govern compensation as a new financially consequential execution rather than implicit rollback.

## Canonical Status

These invariants are architecturally asserted by FIN-ARCH-05.

Assertion does not constitute proof.

FIN-ARCH-06 SHALL assign explicit proof obligations.

---

## FIN-CMP-001 — Compensation Is New Execution

**Normative rule:** A compensating transaction SHALL be represented as a new financially consequential execution event.

**Applies to:** Compensation

**Inherited / derived from:** Financial specialization

**First major paper:** F1

**Status:** ASSERTED

---

## FIN-CMP-002 — Compensation Requirement Is Not Compensation Authority

**Normative rule:** COMPENSATION_REQUIRED SHALL NOT imply authority or admission to enter COMPENSATING.

**Applies to:** Compensation lifecycle

**Inherited / derived from:** Financial specialization/UAA

**First major paper:** F1

**Status:** ASSERTED

---

## FIN-CMP-003 — Compensation Must Be Independently Admitted

**Normative rule:** Compensation SHALL pass an execution admission boundary independently of the originating execution.

**Applies to:** Compensation

**Inherited / derived from:** UAA/Financial specialization

**First major paper:** F1

**Status:** ASSERTED

---

## FIN-CMP-004 — Compensation Preserves Originating History

**Normative rule:** COMPENSATED state SHALL preserve evidence and lineage of the originating execution and effect.

**Applies to:** Compensation

**Inherited / derived from:** POB/Financial specialization

**First major paper:** F1

**Status:** ASSERTED

---

## FIN-CMP-005 — Compensation Is Not Reversal

**Normative rule:** A compensating effect SHALL NOT be classified as reversal unless the reversal requirements are independently satisfied.

**Applies to:** Post-effect classification

**Inherited / derived from:** Financial specialization

**First major paper:** F1

**Status:** ASSERTED

---

