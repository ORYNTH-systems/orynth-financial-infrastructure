# FIN-F2-04 — Execution-Leg Composition

## 1. Purpose

A distributed settlement may consist of multiple execution legs.

An execution leg is an independently identifiable consequential or
pre-consequential transition component within a distributed settlement
proposal.

Execution-leg composition does not yet define atomicity.

Atomicity is deferred to FIN-F2-05.

---

## 2. Execution Leg

Define:

l_i ∈ L(q_d)

where:

L(q_d)

is the execution-leg set of distributed proposal q_d.

Each leg SHALL identify at minimum:

- leg identity
- actor or execution surface
- source state
- target state or intended mutation
- required authority
- required scope
- temporal validity
- dependencies
- ordering constraints
- intended economic mutation
- evidence requirements

---

## 3. Leg Identity

For all distinct legs:

l_i != l_j

where i != j.

No two distinct execution legs may share the same canonical identity.

---

## 4. Leg Dependency Graph

Define:

D(q_d) = (L,E_D)

where E_D contains directed dependency edges.

An edge:

l_i -> l_j

means l_j depends upon a condition produced or satisfied by l_i.

Dependency does not imply authority inheritance.

Authority(l_i) !=> Authority(l_j)

---

## 5. Ordering Constraint

Define:

l_i <_q l_j

where the active profile requires leg l_i to precede leg l_j.

Ordering is distinct from dependency.

A leg may depend on another leg without requiring a strict execution
ordering if the profile permits equivalent evidence or state.

---

## 6. Leg Admission

Define:

LegAdmissible(l_i,q_d,t)

as the leg-specific admission predicate.

Global distributed admission and leg admission SHALL remain distinct.

Admissible_d(q_d,t) does not automatically mean every leg remains
admissible at every later execution time.

Leg state may require revalidation.

---

## 7. Leg Execution

Define:

Execute(l_i,t)

as an attempted transition of leg l_i at time t.

Execution attempt is distinct from recognized effect.

Attempted(l_i,t) !=> EffectOccurred(l_i,t)

---

## 8. Leg State

Each leg may occupy a state in:

NOT-STARTED
ADMITTED
EXECUTING
EFFECT-PARTIAL
EFFECT-COMPLETED
FAILED
BLOCKED
DEFERRED
INDETERMINATE

The meaning of partial/completed economic effect inherits F1.

F2 does not redefine F1 effect semantics.

---

## 9. Distributed Execution Trace

Define:

T_d(q_d)

as the ordered evidence-preserving trace of execution-leg events.

The trace SHALL preserve:

- admission decisions
- execution attempts
- recognized effects
- failures
- blocks
- deferrals
- revalidations
- dependency state changes
- ordering evidence

---

## 10. Multi-Leg Completion

Define:

LegCompletionSet(q_d,t)

as the set of legs whose required effects are classified COMPLETED at t.

Multi-leg completion is not yet equivalent to:

atomic settlement
settlement finality
continuity preservation

Those remain later formal objects.

---

## 11. Partial Distributed Execution

If at least one intended consequential leg has recognized economic effect
and at least one required consequential leg does not satisfy its intended
effect, the distributed settlement enters a candidate partial-execution
condition.

The final classification is deferred to FIN-F2-05 and SHALL inherit F1
partial-effect semantics.

---

## 12. Leg Failure

Failure(l_i) does not create authority for:

compensation
reversal
alternate leg execution
dependency bypass
reordering

Any repair execution remains independently authorized.

---

## 13. No Dependency Bypass

A dependency failure SHALL NOT be silently ignored merely because:

consensus exists
another leg completed
a quorum exists
the target state appears economically equivalent

Dependency rules remain independently enforceable.

---

## 14. No Consensus-to-Execution Collapse

Consensus(q_d,phi,t|CP) !=> Execute(l_i,t)

Consensus does not instantiate an execution event.

---

## 15. No Admission-to-Effect Collapse

LegAdmissible(l_i,q_d,t) !=> EffectOccurred(l_i,t)

Permission does not establish occurrence.

---

## 16. Composition Boundary

FIN-F2-04 establishes:

distributed proposal admission
leg identity
leg dependencies
leg ordering
leg-specific admission
execution attempts
distributed execution traces

It does not yet establish:

atomicity
distributed partial-settlement theorem
settlement finality
cross-domain finality
continuity classification
