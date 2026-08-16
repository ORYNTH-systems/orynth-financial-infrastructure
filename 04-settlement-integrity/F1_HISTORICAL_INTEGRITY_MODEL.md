# F1 — Historical Integrity Model

## Purpose

Historical integrity concerns whether the relevant execution/remediation history remains complete enough, ordered enough, and evidence-backed enough to support reconstruction.

---

## Historical Record

Let:

H_t = (e_0,...,e_n)

with evidence mapping:

eta : e_i -> EvidenceSet_i.

---

## F1 Historical Integrity Predicate

HistInt_F1(H_t,E_t)

requires at minimum:

1. root execution remains represented,
2. remediation events remain represented,
3. ordering remains reconstructable,
4. causal/remediation edges remain represented,
5. no prior event is silently deleted,
6. surviving evidence is sufficient to distinguish known from indeterminate history.

---

## Historical Integrity Is Not Continuity

A perfectly preserved record may prove that continuity broke.

Therefore:

HistoricalIntegrity
does not imply
ContinuityPreserved.

Historical integrity means the history is faithfully represented.

It does not mean the history contains no failures.
