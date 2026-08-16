# F1 — Recursive Remediation Model

## Purpose

Financial remediation can itself produce consequential failure.

F1 therefore models remediation as a graph rather than a guaranteed linear rollback chain.

---

## Execution Nodes

Let:

G_R = (V_R,E_R)

where each vertex v in V_R is a financially consequential execution event.

The originating event has depth 0.

A compensation or reversal created to address prior event v_i creates child v_j.

---

## Remediation Edge Types

E_R contains:

COMPENSATES

REVERSES

RECONCILES_EFFECT_OF

CONTAINS_AFTER

REMEDIATES

---

## Lineage Rule

Every remediation edge must identify:

- source execution,
- remediation execution,
- remediation type,
- authority reference,
- admission reference,
- resulting effect,
- evidence reference.

---

## Partial Compensation

If compensation execution c_1 is partial:

origin e_0
-> compensation c_1
-> PARTIAL compensation effect

the architecture SHALL preserve both:

effect(e_0)

and:

effect(c_1)

A second remediation c_2 may be considered.

c_2 is not a continuation of c_1 authority.

It is a new execution event.

---

## Partial Reversal

The same rule applies to reversal.

A partial reversal does not restore the original state by definition.

It creates a new state requiring observation, possible containment, and possible reconciliation.

---

## Cycle Detection

The remediation graph may not silently permit cycles such as:

e_0 compensates e_1

while:

e_1 compensates e_0

unless the cycle is explicitly represented and evaluated.

Cycles are not automatically forbidden by FIN-F1-02, but they are marked as a proof/verification concern.

---

## Termination Classification

Possible remediation-chain outcomes include:

TERMINATED_RECONCILED

TERMINATED_DIVERGENT

TERMINATED_UNRECOVERABLE

CONTAINED_PENDING_DECISION

ACTIVE_REMEDIATION

CYCLIC

INDETERMINATE

No universal termination claim is asserted at this stage.
