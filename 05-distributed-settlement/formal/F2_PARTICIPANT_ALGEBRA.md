# FIN-F2-02 — Participant Algebra

## 1. Purpose

This artifact defines the formal participant structure required before
agreement, consensus, distributed admissibility, execution composition,
or settlement finality can be defined.

Participant membership does not itself create authority.

Participant != AuthorityHolder.

Participation != Authorization.

Observation != Authority.

Validation != Authority.

Execution capability != Authority.

---

## 2. Universe of Actors

Let:

A

denote the universe of identifiable actors relevant to a distributed
settlement process.

An actor may occupy zero or more roles.

Define a role-assignment relation:

Role(a,r,t)

where:

a ∈ A

r is a system-defined role

t is the relevant evaluation time.

Role assignment is not authority assignment.

Role(a,r,t) does not imply Authority(a,q,t).

---

## 3. Participant Set

For a distributed settlement proposal q, define:

P(q,t) ⊆ A

as the set of actors recognized as participants in q at time t.

Membership means only that an actor participates in the distributed
settlement structure.

a ∈ P(q,t)

does not imply:

Authority(a,q,t)

Admissible(a,q,t)

Required(a,q,t)

ExecutionEligible(a,q,t)

ConsensusWeight(a,q,t) > 0

---

## 4. Required Participant Set

Define:

P_req(q,t) ⊆ P(q,t)

as the actors whose participation is required by the applicable
settlement profile.

P_req is profile-dependent.

A participant may be optional.

A required participant may lack authority.

Therefore:

a ∈ P_req(q,t)

does not imply:

Authority(a,q,t)

---

## 5. Participant Identity

Participant identity SHALL be explicit and stable within an evaluation
context.

Define:

IdentityValid(a,t)

as the predicate that actor a possesses a valid identity representation
for the relevant distributed execution context at time t.

Participation requires:

a ∈ P(q,t) => IdentityValid(a,t)

where the profile requires identity-bound participation.

IdentityValid does not establish authority.

---

## 6. Actor Role Separation

The following roles SHALL remain semantically separable:

Participant

AuthorityHolder

Validator

Attestor

Observer

Coordinator

ExecutionParticipant

SettlementAgent

Custodian

Operator

ExternalAuthority

JurisdictionalAuthority

One actor may instantiate multiple roles.

Multiple actors may instantiate the same role.

Role overlap does not collapse role semantics.

---

## 7. Required Participation Completeness

Define:

ParticipationComplete(q,t)

iff every actor required by the active profile is represented in the
recognized participant set.

ParticipationComplete(q,t)

iff:

P_req(q,t) ⊆ P(q,t)

This establishes participation completeness only.

It does not establish:

authority completeness

agreement

consensus

admissibility

execution readiness

finality.

---

## 8. Participant-State Principle

Distributed financial execution SHALL NOT infer authority from mere
presence in a participant set.

Formally:

a ∈ P(q,t) !=> Authority(a,q,t)

and:

a ∈ P_req(q,t) !=> Authority(a,q,t)

Participant structure and authority structure are separate formal
objects.
