# F1 Partial-Effect Formalization

## Definition

For a financial execution event e with intended effect set M*(e):

PARTIAL(e,t)

iff:

1. F1 applicability holds;
2. every material intended mutation has determinate occurrence status;
3. at least one intended economically consequential mutation occurred;
4. at least one intended economically consequential mutation did not occur.

Formally:

PARTIAL(e,t)

iff:

B_F1(e,t) = 1

∧ K(e,t) = M*(e)

∧ M_econ(e,t) != ∅

∧ M_econ(e,t) != M*(e)

equivalently:

∅ ⊂ M_econ(e,t) ⊂ M*(e)

under complete material knowledge.

---

## Partial Is Not Failed

PARTIAL is not synonymous with FAILED.

A financial execution may produce a validly observed consequential subset of its
intended effects even though the overall intended execution did not complete.

Therefore:

PARTIAL != NO-EFFECT

PARTIAL != COMPLETED

PARTIAL != INDETERMINATE

---

## Partial Is Not Necessarily Invalid

Partial effect classification is descriptive of effect state.

It does not itself determine:

- authority validity,
- admissibility,
- legal validity,
- contractual validity,
- fault,
- culpability,
- finality.

---

## Partial Effect Vector

For:

M*(e) = {m_1, ..., m_n}

define the occurrence vector:

v_e(t) = (x_1, ..., x_n)

where:

x_i = 1
if occurrence of m_i is established,

x_i = 0
if non-occurrence of m_i is established,

x_i = ?
if occurrence status remains unresolved.

Then:

NO-EFFECT:
v_e(t) = (0,...,0)

COMPLETED:
v_e(t) = (1,...,1)

PARTIAL:
v_e(t) ∈ {0,1}^n
with:
v_e(t) != (0,...,0)
and:
v_e(t) != (1,...,1)

INDETERMINATE:
at least one material component x_i = ?

This representation avoids collapsing uncertainty into a binary result.

---

## Weighted Economic Effect

Not all mutations necessarily carry equal economic magnitude.

Define:

w_i >= 0

as an optional domain-specific economic weight for mutation m_i.

Then:

E_total(e) = Σ_i w_i

and:

E_observed(e,t) = Σ_{i : m_i ∈ M_econ(e,t)} w_i

A normalized effect ratio may be defined:

rho(e,t) = E_observed(e,t) / E_total(e)

when:

E_total(e) > 0

However:

rho alone SHALL NOT determine PARTIAL / COMPLETED / NO-EFFECT where mutation
identity matters.

Two executions may have equal rho while affecting materially different obligations
or resources.

Therefore effect-set identity remains primary.

---

## Dependency-Aware Partial Effect

Let:

D ⊆ M* × M*

represent mutation dependencies.

If:

(m_i, m_j) ∈ D

then m_j may depend on prior occurrence or recognition of m_i.

Partiality SHALL preserve dependency structure.

A subset of effects cannot be treated as merely numerical completion percentage
where the resulting subset violates required ordering or atomic relationships.

---

## Atomic Subsets

A domain profile MAY define:

A_1, A_2, ..., A_k ⊆ M*

as atomic mutation groups.

For an atomic group A_j:

partial occurrence inside A_j

may itself constitute an integrity violation even if the entire execution is
already classified PARTIAL.

This supports later settlement-specific invariants without changing the generic
effect classification.

---

## Externally Committed Partial Effect

If:

m_1 ∈ M_com(e,t)

and:

m_1 ∈ M_econ(e,t)

while another required mutation m_2 is established not to have occurred,

then the execution is PARTIAL even if the originating local system attempted to
roll back its own local state.

External economic effect cannot be erased by local process rollback.

---

## Indeterminate Partial Candidate

If at least one intended mutation is known to have occurred but another material
mutation remains unresolved, the correct canonical classification remains:

INDETERMINATE

until the knowledge set is complete enough to distinguish:

PARTIAL

from:

COMPLETED

unless a later F1 specialization introduces a formally separate
PARTIAL-INDETERMINATE substate.

No such new canonical state is introduced in FIN-F1-02.
