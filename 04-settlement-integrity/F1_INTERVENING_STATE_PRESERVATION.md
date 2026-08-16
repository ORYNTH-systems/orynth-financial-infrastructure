# F1 — Intervening-State Preservation Model

## Purpose

Reversal must distinguish the originating execution from legitimate state changes that occurred afterward.

Let:

H =
(e_0,m_1,...,m_k,r)

where:

e_0 = originating execution

m_i = intervening event

r = proposed reversal.

---

## Intervening Event Classification

Each m_i must be classifiable as:

LEGITIMATE_AND_PRESERVE

INVALID_AND_REMEDIATION_RELEVANT

DEPENDENT_ON_ORIGINATING_EFFECT

INDEPENDENT_OF_ORIGINATING_EFFECT

INDETERMINATE

---

## Preservation Rule

A reversal SHALL NOT restore a prior snapshot by blindly overwriting:

m_1,...,m_k.

Instead it must compute a target that preserves valid intervening mutations while addressing the originating divergence.

---

## Conflict

Define:

Conflict(T_R,M)

when satisfying the reversal target would invalidate a required legitimate intervening state.

Such a target is not EXACTLY_REVERSIBLE without further authoritative resolution.

---

## Historical Rule

Intervening events remain part of history regardless of whether their state consequences survive reversal.
