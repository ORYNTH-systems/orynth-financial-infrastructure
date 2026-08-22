# F1 Economic Continuity Proofs

## F1-NEQ-CNT-001 — Economic Endpoint Equivalence Does Not Imply Preservation

Construct two histories with economically equivalent endpoints.

History A:

S_0 --valid uninterrupted path--> S_A

with:

C_F1(H_A,S_A,Gamma) = PRESERVED.

History B:

S_0 --e_0--> S_1 --e_c--> S_B

where e_0 causes a qualifying continuity break and e_c later restores economic
equivalence.

Let:

S_A equivalent_E S_B.

But:

C_F1(H_A,S_A,Gamma) = PRESERVED

and:

C_F1(H_B,S_B,Gamma) = RECONSTRUCTED.

Hence endpoint economic equivalence does not determine continuity classification.

RESULT: COUNTEREXAMPLE-DISCHARGED
EVIDENCE: CONSTRUCTIVE-COUNTEREXAMPLE

---

## F1-NEQ-CNT-002 — Reconciled State Does Not Imply Preservation

A history may be fully reconciled while preserving evidence that a continuity break
occurred.

Therefore:

Reconciled(S_R)
does not imply
ContinuityPreserved.

RESULT: COUNTEREXAMPLE-DISCHARGED
EVIDENCE: CONSTRUCTIVE-COUNTEREXAMPLE

---

## F1-THM-CNT-003 — PRESERVED and RECONSTRUCTED Are Mutually Exclusive

For the same complete historical interval:

PRESERVED requires no qualifying break.

RECONSTRUCTED requires at least one qualifying prior break followed by accepted
reconstruction.

Assume both hold.

Then the same interval must simultaneously satisfy:

there exists no qualifying break

and:

there exists at least one qualifying break.

Contradiction.

Therefore:

PRESERVED ∩ RECONSTRUCTED = empty

for the same complete continuity interval.

RESULT: PROVED
EVIDENCE: FORMAL-DERIVATION

---

## F1-SAFE-CNT-004 — A Known Qualifying Break Excludes PRESERVED

By definition PRESERVED requires every gamma in Gamma to remain satisfied
throughout the relevant interval.

A qualifying break establishes at least one violated continuity requirement.

Therefore PRESERVED is false for that complete interval.

RESULT: PROVED
EVIDENCE: FORMAL-DERIVATION

---

## F1-NEQ-CNT-005 — Functional Recovery Does Not Imply Preservation

Construct a history where system operation resumes after a qualifying obligation
continuity break.

FunctionalRecovery = true.

ContinuityPreserved = false.

Therefore the implication fails.

RESULT: COUNTEREXAMPLE-DISCHARGED
EVIDENCE: CONSTRUCTIVE-COUNTEREXAMPLE

---

## F1-SAFE-CNT-006 — Unknown Break State Cannot Establish PRESERVED

PRESERVED requires evidence sufficient to establish satisfaction of all required
relations over the complete interval.

If a material continuity state is UNKNOWN, that requirement is unmet.

Therefore the canonical result cannot be PRESERVED.

Under F1 semantics the proper classification is INDETERMINATE unless another
classification is positively established.

RESULT: PROVED
EVIDENCE: FORMAL-DERIVATION

---

## F1-TRACE-CNT-007 — Reconstruction Preserves Break Evidence

The semantics require RECONSTRUCTED to contain:

break
-> reconstruction
-> re-established accepted relation.

Therefore break evidence is structurally required by the formal classification.

Executable preservation remains to be validated in FIN-F1-08/09.

RESULT: PARTIAL
EVIDENCE: TRACEABILITY-ARGUMENT + RUNTIME-EVIDENCE-REQUIRED
