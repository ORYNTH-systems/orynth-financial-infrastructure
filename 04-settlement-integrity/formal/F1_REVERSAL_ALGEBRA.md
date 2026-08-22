# F1 Reversal Algebra

## State Path

Let:

S_0 --e_0--> S_1

be an originating transition.

Define:

RP(e_0,S_1,g_r) = e_r

where RP is the ReversalProposal constructor.

Then:

e_r != e_0

and:

ID(e_r) != ID(e_0).

---

## Eligibility Predicate

R_elig(e_0,S_t)

iff the applicable financial profile exposes a recognized reversal mechanism for
the originating effect under the current structural conditions.

R_elig does not imply authority.

---

## Reversibility Predicate

R_rev(e_0,S_t)

iff the current financial state remains capable of supporting an economically
meaningful counter-transition associated with e_0.

R_rev does not imply authority.

---

## Reversal Admission Predicate

Define:

A_r(e_r,t)

iff:

Authority(e_r,t)
AND
ScopeValid(e_r,t)
AND
Admissible(e_r,t)
AND
BoundaryPermit(e_r,t).

Then:

Execute(e_r,t)

is permitted only if:

A_r(e_r,t) = true.

---

## Non-Implication Set

The following implications are prohibited:

R_elig(e_0,S_t)
=> Authority(e_r,t)

R_rev(e_0,S_t)
=> Authority(e_r,t)

Authority(e_0,t_0)
=> Authority(e_r,t)

Failure(e_0)
=> Authority(e_r,t)

NeedReverse(e_0,S_t)
=> Authority(e_r,t)

---

## Counter-Transition

If A_r(e_r,t) holds and reversal executes:

S_1 --e_r--> S_2.

The counter-transition does not remove the originating edge:

S_0 --e_0--> S_1.

Historical transition graph:

S_0
  |
 e_0
  v
S_1
  |
 e_r
  v
S_2

remains the canonical history.

---

## Economic Equivalence

A reversal goal may satisfy:

S_2 ≡_E S_0.

However:

S_2 ≡_E S_0
does not imply
S_2 =_H S_0.

---

## Historical Identity

Historical identity requires equivalence of relevant execution lineage, not merely
economic observables.

Because e_0 and e_r are present in the later history:

History(S_2) != History(S_0)

for any reversal that actually executed after e_0.

---

## Successful Reversal Predicate

Define:

R_success(e_r,S_2,g_r)

iff:

C_F1(e_r,t) = COMPLETED

AND

GoalSatisfied(g_r,S_2)

AND

EvidenceComplete(e_r)

subject to the profile-defined reversal goal.

Successful reversal does not imply historical erasure.

---

## Partial Reversal

If:

C_F1(e_r,t) = PARTIAL

then the reversal itself produces a new post-effect problem state.

The architecture does not recursively assume authority for additional repair.

---

## Indeterminate Reversal

If:

C_F1(e_r,t) = INDETERMINATE

the resulting financial state remains unresolved and must not be represented as
successfully reversed solely because reversal execution was attempted.

---

## Reversal / Compensation Separation

Let:

e_c = compensating execution.

Then:

e_r != e_c

as semantic execution classes unless a domain profile explicitly demonstrates that
a single event satisfies both roles while preserving both labels.

No default equivalence is permitted.
