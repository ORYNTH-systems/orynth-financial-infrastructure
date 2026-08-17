# FIN-F2-02 — Distributed Authority Algebra

## 1. Purpose

This artifact defines how authority is represented across multiple
actors without allowing participation, quorum, agreement, signature,
key possession, validator recognition, or consensus to manufacture
authority.

F2 inherits the prior ORYNTH authority doctrine:

Capability != Authority.

Failure != Repair Authority.

Possession != Authorization.

Consensus != Authority.

---

## 2. Authority Predicate

For actor a, proposal q, action x, scope s, and time t, define:

Authority(a,q,x,s,t)

as the predicate that actor a holds valid authority to perform or
authorize action x concerning proposal q within scope s at time t.

Authority is relational.

Authority is not an intrinsic property of the actor.

---

## 3. Authority Requirement Set

For proposal q, define:

AR(q,t)

as the set of authority requirements that must be satisfied before a
specified distributed settlement decision or execution boundary may be
crossed.

Each authority requirement rho ∈ AR(q,t) SHALL identify at minimum:

- required action
- required scope
- temporal validity
- authority source or provenance
- any delegation chain
- any actor-class constraint
- any jurisdictional applicability constraint where relevant.

---

## 4. Authority Satisfaction

For requirement rho, define:

Satisfied(rho,q,t)

iff there exists at least one actor a such that:

Authority(a,q,Action(rho),Scope(rho),t)

and all applicability requirements of rho are satisfied.

No authority requirement may be satisfied solely by:

- participation
- signature
- possession of a key
- vote
- quorum membership
- validator status
- attestation
- consensus membership
- ledger inclusion.

---

## 5. Distributed Authority Set

Define:

A_valid(q,t)

as the set of actor-authority tuples valid for proposal q at time t.

A_valid(q,t) =
{
(a,x,s) |
Authority(a,q,x,s,t)
}

This set is distinct from:

P(q,t)

and from any later consensus or quorum set.

---

## 6. Authority Completeness

Define:

AuthorityComplete(q,t)

iff:

for every rho ∈ AR(q,t),
Satisfied(rho,q,t)

AuthorityComplete is a collective property of the requirement set.

It does not require one actor to hold every required authority.

It does not imply consensus.

It does not imply admissibility.

It does not imply execution.

---

## 7. Multiparty Authority Composition

Where a settlement profile requires multiple independent authorities,
define:

CompositeAuthority(q,t)

iff all required authority obligations are independently satisfied.

CompositeAuthority does not collapse the authorities into a single
synthetic authority source.

The individual provenance of each authority SHALL remain recoverable.

---

## 8. Independence Constraint

If two authority requirements rho1 and rho2 are marked independent:

Independent(rho1,rho2)

then a single authority claim SHALL NOT satisfy both unless the active
profile explicitly permits common satisfaction.

This prevents accidental collapse of multiparty authority into one
actor merely because that actor possesses broad capability.

---

## 9. Delegation

Where authority is delegated:

Delegate(a0,a1,x,s,t)

the delegated authority SHALL be no broader than the delegating
authority.

DelegatedScope(a1) ⊆ DelegatorScope(a0)

Delegation does not create authority ex nihilo.

Invalid or expired upstream authority cannot generate valid downstream
authority.

---

## 10. Temporal Validity

AuthorityComplete(q,t1)

does not imply:

AuthorityComplete(q,t2)

for t1 != t2.

Distributed authority SHALL be evaluated at the relevant decision or
execution time.

Stale authority cannot satisfy a current authority requirement.

---

## 11. Authority Conflict

Define:

AuthorityConflict(q,t)

where two or more apparently valid authority claims produce mutually
incompatible permissions, prohibitions, or scope assignments.

Authority conflict SHALL NOT be resolved by:

majority vote

consensus

validator count

execution speed

key possession

first execution

last execution.

Conflict resolution requires an independently defined precedence or
reconciliation rule.

---

## 12. No Consensus Manufacture Rule

For any consensus predicate Consensus(q,t):

Consensus(q,t) !=> AuthorityComplete(q,t)

Likewise:

AuthorityComplete(q,t) !=> Consensus(q,t)

The two predicates represent different properties of the system.

---

## 13. No Quorum Manufacture Rule

For any quorum predicate Quorum(q,t):

Quorum(q,t) !=> AuthorityComplete(q,t)

A quorum may satisfy a coordination requirement.

It SHALL NOT manufacture authority absent a separate rule making quorum
participation itself part of the valid authority source.

---

## 14. No Signature Manufacture Rule

SignatureValid(a,q,t) !=> Authority(a,q,x,s,t)

A valid signature establishes a cryptographic or identity-linked fact
according to the applicable signature system.

It does not by itself establish legal, institutional, constitutional,
financial, or execution authority.

---

## 15. No Key-Possession Manufacture Rule

KeyPossession(a,k,t) !=> Authority(a,q,x,s,t)

Control of execution capability cannot replace authority provenance.

---

## 16. Authority Boundary Rule

Before F2 may later define distributed admissibility, it SHALL preserve:

ParticipantComplete
!= AuthorityComplete
!= Agreement
!= Consensus
!= Admissible
!= Executed
!= Final

FIN-F2-02 defines only the first two authority-bearing layers.

Agreement and consensus remain deferred to FIN-F2-03.
