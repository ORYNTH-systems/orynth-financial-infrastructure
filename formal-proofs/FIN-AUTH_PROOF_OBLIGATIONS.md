# FIN-AUTH — Canonical Proof Obligations

## Status

All obligations in this file begin OPEN.

No obligation is proved or discharged by FIN-ARCH-06.

---

## PO-FIN-AUTH-001 — Capability Is Not Authority

**Invariant:** FIN-AUTH-001

**Formal target:** Show that the relevant execution authority property cannot be derived solely from capability, possession, prior authorization, self-expansion, or unbounded delegation.

**Required premises:** Canonical actor identity; authority reference; scope; delegation chain where applicable; current execution context.

**Counterexample condition:** A consequential action executes even though authority is absent, stale, self-expanded, or inferred from capability/control.

**Evidence requirement:** Authority/delegation artifacts; current-state validation; scope evidence; negative case demonstrating capability without authority.

**Implementation requirement:** Reference runtime must prevent authority derivation from capability/control alone.

**Verification requirement:** Positive and negative authority cases; privilege-escalation counterexample attempts.

**Dependencies:** UAA

**First major paper:** FOUNDATION

**Discharge state:** OPEN

---

## PO-FIN-AUTH-002 — Prior Authorization Is Not Current Authority

**Invariant:** FIN-AUTH-002

**Formal target:** Show that the relevant execution authority property cannot be derived solely from capability, possession, prior authorization, self-expansion, or unbounded delegation.

**Required premises:** Canonical actor identity; authority reference; scope; delegation chain where applicable; current execution context.

**Counterexample condition:** A consequential action executes even though authority is absent, stale, self-expanded, or inferred from capability/control.

**Evidence requirement:** Authority/delegation artifacts; current-state validation; scope evidence; negative case demonstrating capability without authority.

**Implementation requirement:** Reference runtime must prevent authority derivation from capability/control alone.

**Verification requirement:** Positive and negative authority cases; privilege-escalation counterexample attempts.

**Dependencies:** UAA/AOMS

**First major paper:** FOUNDATION

**Discharge state:** OPEN

---

## PO-FIN-AUTH-003 — Authority Cannot Self-Expand

**Invariant:** FIN-AUTH-003

**Formal target:** Show that the relevant execution authority property cannot be derived solely from capability, possession, prior authorization, self-expansion, or unbounded delegation.

**Required premises:** Canonical actor identity; authority reference; scope; delegation chain where applicable; current execution context.

**Counterexample condition:** A consequential action executes even though authority is absent, stale, self-expanded, or inferred from capability/control.

**Evidence requirement:** Authority/delegation artifacts; current-state validation; scope evidence; negative case demonstrating capability without authority.

**Implementation requirement:** Reference runtime must prevent authority derivation from capability/control alone.

**Verification requirement:** Positive and negative authority cases; privilege-escalation counterexample attempts.

**Dependencies:** UAA

**First major paper:** FOUNDATION/F8

**Discharge state:** OPEN

---

## PO-FIN-AUTH-004 — Control Is Not Authority

**Invariant:** FIN-AUTH-004

**Formal target:** Show that the relevant execution authority property cannot be derived solely from capability, possession, prior authorization, self-expansion, or unbounded delegation.

**Required premises:** Canonical actor identity; authority reference; scope; delegation chain where applicable; current execution context.

**Counterexample condition:** A consequential action executes even though authority is absent, stale, self-expanded, or inferred from capability/control.

**Evidence requirement:** Authority/delegation artifacts; current-state validation; scope evidence; negative case demonstrating capability without authority.

**Implementation requirement:** Reference runtime must prevent authority derivation from capability/control alone.

**Verification requirement:** Positive and negative authority cases; privilege-escalation counterexample attempts.

**Dependencies:** Financial specialization

**First major paper:** F5

**Discharge state:** OPEN

---

## PO-FIN-AUTH-005 — Delegation Must Remain Bound

**Invariant:** FIN-AUTH-005

**Formal target:** Show that the relevant execution authority property cannot be derived solely from capability, possession, prior authorization, self-expansion, or unbounded delegation.

**Required premises:** Canonical actor identity; authority reference; scope; delegation chain where applicable; current execution context.

**Counterexample condition:** A consequential action executes even though authority is absent, stale, self-expanded, or inferred from capability/control.

**Evidence requirement:** Authority/delegation artifacts; current-state validation; scope evidence; negative case demonstrating capability without authority.

**Implementation requirement:** Reference runtime must prevent authority derivation from capability/control alone.

**Verification requirement:** Positive and negative authority cases; privilege-escalation counterexample attempts.

**Dependencies:** UAA/EIP

**First major paper:** F8

**Discharge state:** OPEN

---

