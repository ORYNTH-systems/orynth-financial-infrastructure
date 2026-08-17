# FIN-F2-03 — Consensus Semantics

## 1. Purpose

Consensus is a collective state-recognition result produced according
to an explicit consensus profile.

Consensus is not authority.

Consensus is not admissibility.

Consensus is not execution.

Consensus is not settlement finality.

Consensus semantics are defined here independently of any specific
algorithm.

---

## 2. Consensus Profile

Define:

CP(q)

as the active consensus profile for proposal q.

A consensus profile SHALL identify at minimum:

- eligible participants
- observation domain
- proposition or state under evaluation
- counting / weighting rule
- threshold or acceptance condition
- temporal window
- conflict treatment
- abstention treatment
- evidence requirements

No particular Byzantine, chain, voting, staking, or validator algorithm
is assumed.

---

## 3. Consensus Observation

Define:

ConsensusObservation(a,q,phi,v,t)

as a recorded observation from actor a concerning proposition phi with
value v at time t.

Observation does not imply authority.

Observation does not imply agreement provenance beyond the defined
observation semantics.

---

## 4. Consensus Predicate

Define:

Consensus(q,phi,t | CP)

iff the observations recognized under CP satisfy the profile's
consensus condition.

Consensus is therefore profile-relative.

A consensus statement without a profile is incomplete.

---

## 5. Consensus Result

Define:

ConsensusResult(q,phi,t)

in:

CONSENSUS-ACHIEVED
CONSENSUS-NOT-ACHIEVED
CONSENSUS-CONFLICTED
CONSENSUS-INDETERMINATE

---

## 6. Consensus Achieved

CONSENSUS-ACHIEVED means only that the active consensus profile's
collective-recognition condition has been satisfied.

It does not establish:

AuthorityComplete
Admissible
Executed
EconomicEffectComplete
SettlementFinal

---

## 7. Consensus Not Achieved

CONSENSUS-NOT-ACHIEVED means the profile determinately failed to satisfy
its consensus condition.

This is distinct from indeterminate consensus.

---

## 8. Consensus Conflicted

CONSENSUS-CONFLICTED applies where recognized evidence contains mutually
incompatible consensus-relevant results that cannot be reduced to a
single profile-valid outcome.

Conflict shall not be silently mapped to achieved or not-achieved.

---

## 9. Consensus Indeterminate

CONSENSUS-INDETERMINATE applies where evidence, membership, weighting,
ordering, timing, applicability, or state recognition is insufficient
for a determinate result.

Unknown != Negative.

Indeterminate != Not Achieved.

---

## 10. Consensus Cannot Manufacture Authority

Consensus(q,phi,t | CP) !=> AuthorityComplete(q,t)

Even unanimous consensus cannot create authority absent an independent
authority source.

---

## 11. Authority Cannot Manufacture Consensus

AuthorityComplete(q,t) !=> Consensus(q,phi,t | CP)

Every required authority may be valid while the consensus profile fails.

---

## 12. Consensus Cannot Manufacture Admissibility

Consensus(q,phi,t | CP) !=> Admissible(q,t)

Admissibility remains a later execution-boundary property.

---

## 13. Consensus Cannot Manufacture Execution

Consensus(q,phi,t | CP) !=> Executed(q,t)

A consensus result is not an execution event.

---

## 14. Consensus Cannot Manufacture Finality

Consensus(q,phi,t | CP) !=> SettlementFinal(q,t)

A system may reach consensus and later:

- fail execution
- execute partially
- reconcile
- reverse
- lose continuity
- remain non-final under another required domain

Therefore consensus and settlement finality remain distinct formal
properties.

---

## 15. Consensus Evidence Principle

Consensus is evidence about collective recognition under CP.

It is not automatically evidence of:

authority provenance
legal validity
jurisdictional validity
economic completion
historical continuity
settlement finality
