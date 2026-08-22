# F1 Compensation Semantics

## 1. Originating Execution

Let:

e_0 ∈ E_F

be a financially consequential originating execution.

Let:

S_pre(e_0)

denote the relevant economic state before e_0.

Let:

S_post(e_0,t)

denote the observed post-effect economic state at time t.

The originating event and its resulting history remain independently identifiable.

---

## 2. Compensation Requirement

Define:

NeedComp(e_0,S_t)

as a determination that the post-effect state may require a compensating action.

NeedComp is a control determination.

It is not execution authority.

Therefore:

NeedComp(e_0,S_t)
does not imply
Authority(e_c)

for any candidate compensating event e_c.

---

## 3. Compensation Proposal

A compensation proposal is a separately instantiated financial execution event:

e_c = CompensationProposal(e_0,S_t,g_c)

where:

e_0 = originating execution,
S_t = current post-effect state,
g_c = proposed compensating economic goal.

Require:

e_c != e_0

and:

ExecutionEventId(e_c) != ExecutionEventId(e_0)

The compensation event must remain independently addressable in evidence,
authority, execution, and historical lineage.

---

## 4. Compensation Goal

A compensation goal g_c describes a desired economic result.

Examples may include:

- restoration of an economic balance relation,
- satisfaction of an outstanding obligation,
- neutralization of an unintended transfer,
- restoration of a resource allocation condition,
- creation of an economically equivalent position.

A goal does not imply that the proposed means are authorized.

Therefore:

GoalValid(g_c)
does not imply
Authority(e_c).

---

## 5. Compensation Eligibility

Define:

EligibleComp(e_c,S_t)

as the structural proposition that e_c is a candidate capable of pursuing the
specified compensating goal within the current domain model.

Eligibility is not authority.

Thus:

EligibleComp(e_c,S_t)
does not imply
Authority(e_c,t)

and:

EligibleComp(e_c,S_t)
does not imply
Admissible(e_c,t).

---

## 6. Independent Authority

A compensation event must obtain or reference its own current authority.

Require:

Authority(e_c,t)

under inherited authority semantics.

Authority over e_0 does not automatically transfer to e_c.

Therefore:

Authority(e_0,t_0)
does not imply
Authority(e_c,t_c).

Likewise:

Failure(e_0)
does not imply
Authority(e_c).

PartialEffect(e_0)
does not imply
Authority(e_c).

Invalid(e_0)
does not imply
Authority(e_c).

---

## 7. Scope

Require:

ScopeValid(e_c,t)

for the compensating action.

The scope of the originating execution is not presumed to authorize repair.

A compensation proposal may require:

- different resources,
- different counterparties,
- different transaction types,
- different settlement rails,
- different jurisdictional permissions,
- different institutional authority.

Therefore:

Scope(e_0)
need not equal
Scope(e_c).

---

## 8. Independent Admissibility

Before consequential compensation effectuation:

Admissible(e_c,t)

must be established independently.

The compensation event must traverse the canonical financial admission and
consequential-boundary architecture.

Require:

Authority(e_c,t)
AND
ScopeValid(e_c,t)
AND
Admissible(e_c,t)
AND
BoundaryPermit(e_c,t)

before:

Execute(e_c).

---

## 9. No Self-Authorization From Failure

The originating problematic state cannot manufacture compensation authority.

Formally:

Failure(e_0)
does not imply
Authority(e_c).

More generally:

ProblemState(e_0,S_t)
does not imply
Authority(e_c).

The need for repair and authority to repair are orthogonal propositions.

---

## 10. Compensation Effect

Let:

M*(e_c)

be the intended consequential mutation set of the compensation event.

Let:

M_econ(e_c,t)

be its recognized economic effect set.

The compensation event is classified using the same post-effect effect algebra
as any other consequential financial execution.

Thus compensation itself may result in:

- NO-EFFECT,
- PARTIAL,
- COMPLETED,
- INDETERMINATE.

A compensation event is not assumed successful merely because its purpose is
corrective.

---

## 11. Recursive Repair

If a compensation event itself partially effects economic state:

PARTIAL(e_c,t)

then any later proposed repair e_c2 must itself be instantiated as a new event.

Require:

e_c2 != e_c

and:

e_c2 != e_0.

No repair event creates an unlimited chain of inherited repair authority.

Each consequential repair remains independently governed.

---

## 12. Economic Equivalence

Define an economic-equivalence relation:

S_a ≡_E S_b

iff the domain-specific economically relevant observables selected by the profile
are equivalent under an explicitly defined comparison relation.

This relation may consider:

- balances,
- obligations,
- asset positions,
- economic exposure,
- settlement liabilities,
- other profile-defined economic quantities.

Economic equivalence is domain-specific and must not be assumed from raw object
identity.

---

## 13. Compensation Success

A compensation operation may be considered economically successful relative to
goal g_c if:

GoalSatisfied(g_c,S_after)

holds.

This may include a case where:

S_after ≡_E S_pre(e_0).

However:

S_after ≡_E S_pre(e_0)

does not imply:

S_after =_H S_pre(e_0)

where =_H denotes historical-state identity.

---

## 14. Historical Persistence

If the originating execution produced economic effect:

Occurred(e_0)

then after compensation:

Occurred(e_0)

remains true.

Likewise, if the compensation execution produced effect:

Occurred(e_c)

remains true.

Thus:

History(S_after)
contains
History(e_0)

and, where executed:

History(e_c).

Compensation adds history.

It does not rewrite history.

---

## 15. Economic Restoration Is Not Historical Restoration

Even if:

S_after ≡_E S_pre(e_0)

we do not infer:

S_after =_H S_pre(e_0).

The execution path remains:

S_pre
--e_0-->
S_problem
--e_c-->
S_after

rather than collapsing into:

S_pre
=
S_after

for historical purposes.

---

## 16. Compensation Is Not Reversal

Compensation and reversal remain distinct.

Compensation creates a separate effect intended to offset, satisfy, neutralize,
or economically repair consequences of prior execution.

Reversal will be separately formalized in FIN-F1-04.

No statement in FIN-F1-03 permits:

Compensation = Reversal.

---

## 17. Compensation Is Not Reconstruction

Compensation changes economic state.

Reconstruction determines or reconstructs state/history from evidence.

Therefore:

Compensation != Reconstruction.

---

## 18. Compensation Is Not Reconciliation

Compensation may be one input to later reconciliation.

But:

Compensation != Reconciliation.

A system may compensate successfully and still require reconciliation.

---

## 19. Governance Independence

The compensation machinery may determine:

- need,
- candidate form,
- target economic goal.

It may not create the authority it requires.

This preserves the inherited principle:

Capability != Authority.

Within F1:

Repair Need != Repair Authority.

---

## 20. F1 Ownership

F1 owns the financial specialization of compensation as an independently governed
post-effect consequential execution.

Generic authority, admissibility, and execution-boundary semantics remain inherited.
