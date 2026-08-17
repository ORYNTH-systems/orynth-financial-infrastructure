# FIN-F2-03 — Agreement Semantics

## 1. Purpose

Agreement is a participant-relative statement concerning a proposal,
state, value, ordering, commitment, or transition.

Agreement is not consensus.

Agreement is not authority.

Agreement is not admissibility.

Agreement is not execution.

Agreement is not settlement finality.

---

## 2. Agreement Predicate

For actor a, proposal q, proposition phi, and time t, define:

Agree(a,q,phi,t)

to mean actor a is recorded as affirming proposition phi concerning q
at time t according to the applicable agreement protocol.

Agreement is always relative to:

- an identified actor
- an identified proposition
- an identified proposal
- an evaluation time
- an applicable agreement protocol

---

## 3. Agreement Record

Define:

AgreementRecord = {
    actor,
    proposal,
    proposition,
    decision,
    time,
    provenance,
    evidence
}

where decision may include:

AGREE
DISAGREE
ABSTAIN
NOT-OBSERVED
INDETERMINATE

---

## 4. Agreement Set

For proposal q and proposition phi:

G(q,phi,t)

denotes the set of actors whose agreement is recognized at time t.

G(q,phi,t) =
{
a |
Agree(a,q,phi,t)
}

Membership in G does not imply authority.

---

## 5. Agreement Completeness

Define:

AgreementComplete(q,phi,t)

only where an active profile defines which participants must provide
agreement evidence.

AgreementComplete concerns evidence completeness.

It does not imply unanimous agreement.

It does not imply consensus.

It does not imply authority completeness.

---

## 6. Agreement Conflict

Define:

AgreementConflict(q,phi,t)

where recognized participant statements concerning phi are mutually
incompatible.

Agreement conflict is not an authority conflict.

The same execution may contain both independently.

---

## 7. No Authority Manufacture

Agree(a,q,phi,t) !=> Authority(a,q,x,s,t)

An unauthorized actor may agree.

An authorized actor may disagree.

An authorized actor may abstain.

Therefore agreement cannot replace authority evaluation.

---

## 8. No Execution Manufacture

AgreementComplete(q,phi,t) !=> Executed(q,t)

Agreement evidence does not cross the execution boundary.

---

## 9. No Finality Manufacture

AgreementComplete(q,phi,t) !=> Final(q,t)

Agreement cannot itself establish settlement finality.
