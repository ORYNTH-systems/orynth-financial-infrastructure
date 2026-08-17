# FIN-F2-08 — Distributed Continuity Transition Model

## 1. Purpose

This artifact defines allowed classification transitions among inherited
continuity states without converting recovery into retroactive preserved
continuity.

---

## 2. State Set

C_d = {
    PRESERVED,
    DEGRADED,
    BROKEN,
    RECONSTRUCTED,
    INDETERMINATE
}

---

## 3. Permitted Classification Evolution

Candidate transitions include:

PRESERVED -> DEGRADED

PRESERVED -> BROKEN

PRESERVED -> INDETERMINATE

DEGRADED -> PRESERVED

DEGRADED -> BROKEN

DEGRADED -> INDETERMINATE

BROKEN -> RECONSTRUCTED

BROKEN -> INDETERMINATE

INDETERMINATE -> PRESERVED

INDETERMINATE -> DEGRADED

INDETERMINATE -> BROKEN

INDETERMINATE -> RECONSTRUCTED

Transitions are evidence-dependent and profile-dependent.

---

## 4. Forbidden Historical Collapse

BROKEN -> PRESERVED

is forbidden as a retroactive description of the same broken interval.

A later current state may be newly preserved after repair, but the prior
interval remains historically BROKEN.

Likewise:

RECONSTRUCTED -> PRESERVED

must not erase reconstruction history.

---

## 5. Current vs Historical Continuity

Define:

CurrentContinuity(q_d,t)

and:

HistoricalContinuity(q_d,[t0,t1])

as separate evaluations.

A system may currently operate with preserved continuity after a later
clean transition while retaining a historical BROKEN or RECONSTRUCTED
interval.

Current state != historical path.

---

## 6. Recovery Transition

Recovery after BROKEN may produce:

BROKEN -> RECONSTRUCTED

where historical lineage must be rebuilt.

A subsequent clean execution interval may separately receive a current
PRESERVED classification.

That does not rewrite the earlier classification.

---

## 7. Degradation Cure

DEGRADED -> PRESERVED

is allowed only where the profile-defined degrading condition is cured
without a continuity-breaking event having occurred.

If a break occurred, the path must not be relabeled preserved.

---

## 8. Indeterminacy Resolution

INDETERMINATE may resolve to any evidence-supported continuity class.

The prior period of indeterminacy remains historically evidenced.

Resolution != retroactive certainty beyond the supporting evidence.

---

## 9. Finality Independence

Changes in finality classification do not automatically change
continuity classification.

Likewise, continuity repair does not automatically establish finality.
