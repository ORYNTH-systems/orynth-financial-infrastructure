# FIN-F2-05 — Atomicity Semantics

## 1. Purpose

Atomicity classifies whether a defined set of required consequential
execution legs is observed as a single all-required-effects condition
under an explicit atomicity profile.

Atomicity is not:

authority
admissibility
consensus
execution occurrence
settlement finality
historical continuity
irreversibility

Atomicity concerns required effect composition.

---

## 2. Atomicity Profile

For distributed settlement proposal q_d, define:

AP(q_d)

as the active atomicity profile.

AP SHALL identify at minimum:

- atomic leg set
- required effect condition for each leg
- dependency conditions
- temporal evaluation window
- observation requirements
- evidence sufficiency rules
- conflict treatment
- indeterminacy treatment

No atomicity claim is meaningful without an identified profile.

---

## 3. Atomic Leg Set

Define:

L_A(q_d) ⊆ L(q_d)

as the set of execution legs whose required effects participate in the
atomicity condition.

Not every leg in a distributed transaction must necessarily belong to
L_A.

The profile determines inclusion.

---

## 4. Leg Effect Satisfaction

For each l_i ∈ L_A(q_d), define:

EffectSatisfied(l_i,t | AP)

iff the recognized effect of l_i satisfies the effect requirement
assigned by AP.

EffectSatisfied is evaluated from recognized evidence.

Attempted(l_i,t) !=> EffectSatisfied(l_i,t | AP)

Admitted(l_i,t) !=> EffectSatisfied(l_i,t | AP)

---

## 5. Atomic Completion

Define:

AtomicComplete(q_d,t | AP)

iff:

for every l_i ∈ L_A(q_d),
EffectSatisfied(l_i,t | AP)

and all AP dependency and evidence conditions are satisfied.

AtomicComplete concerns the required leg-effect set.

AtomicComplete does not imply SettlementFinal.

---

## 6. Atomic Non-Occurrence

Define:

AtomicNoEffect(q_d,t | AP)

iff no consequential leg in L_A(q_d) has recognized economic effect.

Where appropriate, the inherited F1 NO-EFFECT classification applies
to the distributed consequential mutation set.

---

## 7. Atomic Partial Condition

Define:

AtomicPartial(q_d,t | AP)

iff:

there exists l_i ∈ L_A(q_d) with recognized required economic effect

and

there exists l_j ∈ L_A(q_d) whose required effect is not satisfied.

This establishes a distributed partial-effect condition.

It does not redefine F1 PARTIAL.

F2 maps the multi-leg condition into the inherited F1 post-effect
classification.

---

## 8. Atomic Indeterminacy

Define:

AtomicIndeterminate(q_d,t | AP)

where available evidence is insufficient to determine whether the
atomic leg-effect condition is complete, partial, or no-effect.

Indeterminate != Partial

Indeterminate != No-Effect

Indeterminate != Complete

---

## 9. Atomicity Classification

Define:

AtomicityResult(q_d,t | AP)

in:

ATOMIC-NO-EFFECT
ATOMIC-PARTIAL
ATOMIC-COMPLETE
ATOMIC-INDETERMINATE

These classes describe distributed required-effect composition.

They do not establish settlement finality.

---

## 10. Strong Partial Condition

If:

L_A(q_d) != empty

and:

there exists l_i ∈ L_A with EffectSatisfied(l_i,t|AP)

and:

there exists l_j ∈ L_A with not EffectSatisfied(l_j,t|AP)

under sufficient evidence,

then:

AtomicityResult(q_d,t|AP) = ATOMIC-PARTIAL

This is a definitionally grounded classification result.

Formal proof discharge remains FIN-F2-09.

---

## 11. Atomicity and Consensus

Consensus(q_d,phi,t|CP) !=> AtomicComplete(q_d,t|AP)

Consensus may concern intention, ordering, recognition, or another
proposition.

Consensus cannot establish economic occurrence by itself.

---

## 12. Atomicity and Admissibility

Admissible_d(q_d,t) !=> AtomicComplete(q_d,t|AP)

Admission precedes effect.

Atomicity is evaluated from resulting leg effects.

---

## 13. Atomicity and Finality

AtomicComplete(q_d,t|AP) !=> SettlementFinal(q_d,t)

A settlement may satisfy all AP leg-effect requirements yet remain
non-final because:

- another required finality domain is unresolved
- legal or institutional finality is pending
- cross-system recognition is incomplete
- evidence remains disputed
- a profile-defined finality condition has not been met

---

## 14. Atomicity and Continuity

AtomicComplete(q_d,t|AP) !=> ContinuityPreserved(q_d)

Atomic completion cannot erase:

prior interruptions
temporary inconsistent states
repair events
reversals
reconstruction
historical discontinuities

---

## 15. Atomic Intent

AtomicIntent(q_d) means the proposal requires an atomicity condition.

AtomicIntent(q_d) !=> AtomicComplete(q_d,t|AP)

Intent is not effect.

---

## 16. Atomic Failure

Failure to achieve AtomicComplete does not create:

repair authority
compensation authority
reversal authority
dependency-bypass authority
alternate execution authority

Repair remains independently authorized under inherited F1 doctrine.

---

## 17. Historical Persistence

If a settlement enters ATOMIC-PARTIAL and later reaches an economically
equivalent repaired state, the prior partial execution remains part of
history.

Repair cannot rewrite the atomic execution path.

---

## 18. Boundary

FIN-F2-05 formalizes:

atomic leg sets
atomicity profiles
atomic required-effect satisfaction
atomic no-effect
atomic partial effect
atomic completion
atomic indeterminacy

It does not yet formalize:

settlement finality
cross-domain finality
conflict reconciliation
distributed continuity classification
