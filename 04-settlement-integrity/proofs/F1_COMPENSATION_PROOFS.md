# F1 Compensation Proofs

## F1-THM-CMP-001 — Compensation Event Distinctness

By definition:

e_c = CompensationProposal(e_0,S_t,g_c)

with:

ID(e_c) != ID(e_0).

Therefore:

e_c != e_0.

RESULT: PROVED
EVIDENCE: DEFINITIONAL-DERIVATION

---

## F1-NEQ-CMP-002 — Failure Does Not Imply Compensation Authority

Claim rejected:

Failure(e_0) => Authority(e_c)

Constructive witness:

- originating event e_0 enters a failed/partial post-effect state;
- compensation is structurally required;
- no valid current authority exists for candidate e_c.

This model satisfies:

Failure(e_0) = true

while:

Authority(e_c) = false.

Therefore the implication is false.

Hence:

Failure(e_0) does not imply Authority(e_c).

RESULT: COUNTEREXAMPLE-DISCHARGED
EVIDENCE: CONSTRUCTIVE-COUNTEREXAMPLE

---

## F1-SAFE-CMP-003 — Independent Admission Requirement

The formal architecture requires compensation to satisfy:

Authority(e_c,t)
AND
ScopeValid(e_c,t)
AND
Admissible(e_c,t)
AND
BoundaryPermit(e_c,t)

before Execute(e_c).

This establishes the formal safety condition.

Executable enforcement remains to be demonstrated by FIN-F1-08 and FIN-F1-09.

RESULT: PARTIAL
EVIDENCE: RUNTIME-EVIDENCE-REQUIRED

---

## F1-NEQ-CMP-004 — Economic Restoration Does Not Erase Origin

Consider:

S_0 --e_0--> S_1 --e_c--> S_2

with:

S_2 equivalent_E S_0.

The established execution history of S_2 includes e_0 and e_c, while the history
of S_0 does not.

Therefore equality of selected economic observables is insufficient for historical
identity.

RESULT: COUNTEREXAMPLE-DISCHARGED
EVIDENCE: CONSTRUCTIVE-COUNTEREXAMPLE

---

## F1-SAFE-CMP-005 — Recursive Repair Authority

The semantics require every later repair e_c2 to be independently instantiated and
admitted.

The normative/formal condition is established.

General runtime enforcement remains open.

RESULT: PARTIAL
EVIDENCE: RUNTIME-EVIDENCE-REQUIRED
