# FIN-F2-03 — Commitment Semantics

## 1. Purpose

A commitment is a recorded binding or protocol-recognized undertaking
concerning a future or pending action, state, resource, or execution leg.

Commitment is distinct from:

agreement
authority
admissibility
execution
economic effect
finality

---

## 2. Commitment Object

Define:

Commitment c = {
    commitment_id,
    actor,
    proposal,
    obligation,
    scope,
    time_created,
    validity_interval,
    conditions,
    provenance,
    evidence
}

---

## 3. Commitment Predicate

Committed(a,q,o,t)

means that actor a has a recognized commitment concerning obligation o
under proposal q at time t.

Committed does not imply:

Authority(a,q,o,t)

Admissible(q,t)

Executed(q,t)

EffectOccurred(q,t)

Final(q,t)

---

## 4. Commitment Validity

Define:

CommitmentValid(c,t)

iff the commitment:

- exists
- is current
- is applicable
- satisfies its required form
- has valid provenance
- is not revoked or expired according to the active profile

Commitment validity is not authority validity.

---

## 5. Commitment Set

Define:

K(q,t)

as the set of recognized commitments for q at t.

K_req(q,t)

denotes the required commitment set under the active profile.

---

## 6. Commitment Completeness

Define:

CommitmentComplete(q,t)

iff every required commitment obligation has a corresponding valid
commitment.

CommitmentComplete != AuthorityComplete

CommitmentComplete != AgreementComplete

CommitmentComplete != Consensus

CommitmentComplete != Admissible

CommitmentComplete != Executed

CommitmentComplete != Final

---

## 7. Conditional Commitment

A commitment may be conditional.

ConditionalCommitment(c,psi)

means c becomes actionable only if condition psi is satisfied.

Satisfaction of psi does not automatically execute c.

---

## 8. Revocation

A revocable commitment may transition to:

REVOKED

before execution, subject to profile rules.

Revocation is not reversal.

Revocation concerns a commitment state.

Reversal concerns a consequential execution already performed.

---

## 9. Failure of Commitment

A commitment may fail to produce execution.

Therefore:

Committed(a,q,o,t) !=> Executed(q,t)

and:

CommitmentComplete(q,t) !=> EffectOccurred(q,t)

---

## 10. Historical Persistence

If a commitment was validly issued and later revoked, expired, consumed,
or superseded, its historical existence remains part of the evidence
record.

Current invalidity does not erase historical existence.
