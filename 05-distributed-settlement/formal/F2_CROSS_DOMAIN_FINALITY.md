# FIN-F2-06 — Cross-Domain Finality

## 1. Purpose

Distributed financial settlement may involve more than one finality
domain.

A settlement may be final in one domain while unresolved in another.

F2 therefore prohibits universalizing a local finality result.

---

## 2. Domain Finality Vector

For required domain set:

D* = {D_1,...,D_n}

define the finality vector:

V_f(q_d,t) =
[
F_1,
F_2,
...,
F_n
]

where each F_i is the domain-level FinalityResult for D_i.

---

## 3. Cross-Domain Completeness

CrossDomainFinal(q_d,t,D*)

requires:

for every required D_i ∈ D*:

FinalityResult(q_d,t|FP,D_i) = FINAL

and any profile-defined cross-domain consistency obligations are
satisfied.

---

## 4. Mixed Finality State

A distributed settlement may occupy a mixed state such as:

D_1 = FINAL

D_2 = FINALITY-PENDING

D_3 = FINALITY-CONFLICTED

Such a state SHALL NOT be collapsed to FINAL for D*.

---

## 5. Finality Propagation Prohibition

Final(D_1) !=> Final(D_2)

Final(D_1) !=> CrossDomainFinal(D*)

No finality result propagates across domains without an explicit
profile-defined rule.

---

## 6. External Recognition

Where a domain requires recognition from an external system, authority,
institution, or jurisdiction, absence of that recognition cannot be
replaced by internal consensus.

InternalConsensus != ExternalFinalityRecognition

---

## 7. Cross-Domain Indeterminacy

If any required domain result is indeterminate, and the active profile
requires that domain, cross-domain finality cannot be established.

Unknown domain state != satisfied domain state.

---

## 8. Cross-Domain Conflict

Where two required domains assert mutually incompatible settlement
states, cross-domain finality remains unavailable until the conflict is
resolved under an explicit governing rule.

Conflict reconciliation is deferred to FIN-F2-07.
