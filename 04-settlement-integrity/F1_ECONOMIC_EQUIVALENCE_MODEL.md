# F1 — Economic Equivalence Model

## Purpose

Economic equivalence is always defined relative to an explicit projection.

Let:

pi_D

be a projection over selected economic dimensions D.

Two states X_a and X_b are equivalent under projection pi_D when:

pi_D(X_a) = pi_D(X_b)

This does not imply:

X_a = X_b.

---

## Examples

Cash equivalence:

cash(X_a) = cash(X_b)

does not imply:

ownership(X_a) = ownership(X_b).

Balance equivalence does not imply:

obligation equivalence.

Asset-value equivalence does not imply:

custody equivalence.

---

## Projected Economic Equivalence

Define:

EconEq_pi(X_a,X_b)

iff:

pi(X_a) = pi(X_b).

Every claim of economic equivalence must identify pi.

There is no unqualified universal economic-equivalence operator in F1.

---

## Full Current-State Equivalence

FullStateEq(X_a,X_b)

requires equality across all required current-state dimensions.

Even then:

FullStateEq
does not imply
HistoricalEq.

---

## Historical Equivalence

Historical equivalence would require equivalent relevant histories.

A state reached through:

partial execution
-> compensation
-> reconciliation

is not historically equivalent to a state in which the original execution never occurred.

---

## Rule

ProjectedEconomicEquivalence
!= FullStateEquivalence

FullStateEquivalence
!= HistoricalEquivalence

Economic equivalence is descriptive.

It does not establish continuity or authority.
