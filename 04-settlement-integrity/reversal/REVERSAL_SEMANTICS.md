# F1 Reversal Semantics

## 1. Originating Transition

Let:

S_0 --e_0--> S_1

represent an originating financially consequential execution.

The originating event e_0 and its effect remain historically persistent.

---

## 2. Reversal Proposal

Define a distinct candidate event:

e_r = ReversalProposal(e_0,S_1,g_r)

where:

e_0 = originating execution,
S_1 = current post-origin state,
g_r = intended reversal goal.

Require:

e_r != e_0

and:

ExecutionEventId(e_r) != ExecutionEventId(e_0).

A reversal is therefore not deletion or mutation of the original execution record.

---

## 3. Reversal Eligibility

Define:

EligibleReverse(e_0,S_t)

as the proposition that a structurally recognized reversal mechanism exists for
the relevant originating effect under the current domain profile.

Eligibility answers:

Can this type of effect potentially be counter-transitioned?

It does not answer:

Is reversal currently authorized?

Therefore:

EligibleReverse(e_0,S_t)
does not imply
Authority(e_r,t).

---

## 4. Reversibility

Define:

Reversible(e_0,S_t)

as the proposition that the current effect/state remains technically or
institutionally capable of being counter-transitioned under the relevant model.

Reversibility is state-dependent.

It may cease to hold because of:

- finality rules,
- irreversible external commitment,
- downstream dependencies,
- asset transfer,
- timing,
- institutional state,
- jurisdictional constraints,
- destruction or transformation of the target resource.

Reversibility does not imply reversal authority.

Thus:

Reversible(e_0,S_t)
does not imply
Authority(e_r,t).

---

## 5. Reversal Authority

A reversal execution must possess its own current authority.

Require:

Authority(e_r,t).

Authority over the originating execution does not automatically transfer.

Therefore:

Authority(e_0,t_0)
does not imply
Authority(e_r,t).

Likewise:

EligibleReverse(e_0,S_t)
does not imply
Authority(e_r,t).

Reversible(e_0,S_t)
does not imply
Authority(e_r,t).

---

## 6. Reversal Scope

Require:

ScopeValid(e_r,t).

The scope required for reversal may differ from the scope of the original action.

A reversal may implicate:

- different resources,
- different accounts,
- different counterparties,
- different institutions,
- different settlement systems,
- different governing policies.

Therefore:

Scope(e_0)
need not equal
Scope(e_r).

---

## 7. Independent Admissibility

A reversal event must independently satisfy:

Authority(e_r,t)

AND

ScopeValid(e_r,t)

AND

Admissible(e_r,t)

AND

BoundaryPermit(e_r,t)

before:

Execute(e_r).

Reversal need does not bypass current-state governance.

---

## 8. Reversal Counter-Transition

If admitted, the reversal executes as:

S_1 --e_r--> S_2.

The reversal event creates a new consequential state transition.

It does not delete:

S_0 --e_0--> S_1.

---

## 9. Successful Reversal

Define:

ReversalSuccess(e_r,S_2,g_r)

iff:

1. e_r completed under the F1 effect classifier;
2. the defined reversal goal g_r is satisfied;
3. required evidence exists;
4. historical lineage remains preserved.

Successful reversal is an execution result.

It is not equivalent to reversal eligibility, reversibility, or reversal authority.

---

## 10. Four-Way Distinction

The following propositions are independent:

EligibleReverse(e_0,S_t)

Reversible(e_0,S_t)

Authority(e_r,t)

ReversalSuccess(e_r,S_2,g_r)

No pair is treated as synonymous.

Examples:

A reversal may be eligible but no longer technically reversible.

A reversal may be technically reversible but lack authority.

A reversal may be authorized but inadmissible under current state.

A reversal may execute with authority but itself become PARTIAL or INDETERMINATE.

---

## 11. Reversal Effect Classification

The reversal event is itself subject to:

C_F1(e_r,t) ∈ {
    NO-EFFECT,
    PARTIAL,
    COMPLETED,
    INDETERMINATE
}

A reversal is not presumed successful merely because its direction is opposite
the originating transition.

---

## 12. Reversal Is Not Compensation

A reversal is associated with counter-transitioning an originating effect.

Compensation introduces a separate effect intended to offset or repair economic
consequences.

Therefore:

Reversal != Compensation.

A system may permit compensation where reversal is impossible.

A system may permit reversal where compensation would be unnecessary.

A domain may support both.

---

## 13. Reversal Is Not Rollback

Local software rollback does not necessarily constitute financial reversal.

A local runtime may restore its own internal state while an external economic
effect remains committed.

Therefore:

LocalRollback != Reversal.

Reversal requires an economically meaningful counter-transition in the relevant
financial state domain.

---

## 14. Reversal Is Not Erasure

If:

Occurred(e_0,t_0)

then after reversal:

Occurred(e_0,t_0)

remains true.

If:

Occurred(e_r,t_r)

then:

Occurred(e_r,t_r)

also remains true.

The historical path remains:

S_0 --e_0--> S_1 --e_r--> S_2.

It SHALL NOT collapse into:

S_0 =_H S_2

merely because:

S_2 ≡_E S_0.

---

## 15. Economic Equivalence After Reversal

A successful reversal may produce:

S_2 ≡_E S_0

under a domain-specific economic-equivalence relation.

This does not imply:

S_2 =_H S_0.

The states may be economically equivalent while carrying different:

- execution histories,
- timestamps,
- evidence,
- provenance,
- counterparty states,
- obligations,
- fees,
- external side effects.

---

## 16. Reversal Failure

If a reversal itself fails or partially effects state, that failure does not
automatically authorize another reversal.

Any subsequent repair event must be independently instantiated and admitted.

---

## 17. Reversal and Finality

Reversal eligibility and reversibility do not define financial finality.

F3 owns finality specialization.

FIN-F1-04 only preserves the distinction:

Reversible != Final

and:

Final does not automatically imply Irreversible.

---

## 18. Historical Monotonicity

The set of established historical execution events is append-preserving.

If:

e_0 ∈ H_t

then for later t':

e_0 ∈ H_t'

unless evidence is explicitly reclassified as invalid provenance rather than
silently deleted.

Reversal appends e_r to history.

It does not subtract e_0.

---

## 19. Governance Rule

The system may determine:

- reversal eligibility,
- reversibility,
- candidate reversal structure.

Those determinations may not generate the authority required to execute reversal.

Thus:

Counter-transition capability != Counter-transition authority.

---

## 20. F1 Ownership

F1 owns reversal as a financially specialized, independently governed,
historically persistent counter-transition.

Generic authority, admissibility, execution-boundary, and generic continuity
semantics remain inherited.
