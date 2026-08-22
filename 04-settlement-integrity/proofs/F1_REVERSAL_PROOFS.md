# F1 Reversal Proofs

## F1-THM-REV-001 — Reversal Event Distinctness

By canonical construction:

e_r = ReversalProposal(e_0,S_1,g_r)

and:

ID(e_r) != ID(e_0).

Therefore:

e_r != e_0.

RESULT: PROVED
EVIDENCE: DEFINITIONAL-DERIVATION

---

## F1-NEQ-REV-002 — Eligibility Does Not Imply Authority

Claim rejected:

EligibleReverse(e_0,S_t) => Authority(e_r,t).

Construct a state where:

- a recognized reversal mechanism exists;
- the state is technically reversible;
- the actor possesses no current reversal authority.

Then:

EligibleReverse = true

and:

Authority(e_r,t) = false.

The implication is therefore invalid.

RESULT: COUNTEREXAMPLE-DISCHARGED
EVIDENCE: CONSTRUCTIVE-COUNTEREXAMPLE

---

## F1-NEQ-REV-003 — Reversibility Does Not Imply Authority

A counter-transition may remain technically possible even when no actor currently
possesses governing authority to perform it.

Therefore:

Reversible(e_0,S_t)
does not imply
Authority(e_r,t).

RESULT: COUNTEREXAMPLE-DISCHARGED
EVIDENCE: CONSTRUCTIVE-COUNTEREXAMPLE

---

## F1-SAFE-REV-004 — Independent Reversal Admission

The formal model requires:

Authority(e_r,t)
AND
ScopeValid(e_r,t)
AND
Admissible(e_r,t)
AND
BoundaryPermit(e_r,t)

before effectuation.

Formal safety requirement is established.

Runtime conformance remains open.

RESULT: PARTIAL
EVIDENCE: RUNTIME-EVIDENCE-REQUIRED

---

## F1-NEQ-REV-005 — Reversal Does Not Erase Historical Occurrence

Consider:

S_0 --e_0--> S_1 --e_r--> S_2

with:

S_2 equivalent_E S_0.

The history of S_2 still contains both e_0 and e_r.

Therefore:

S_2 equivalent_E S_0

does not imply:

S_2 =_H S_0.

RESULT: COUNTEREXAMPLE-DISCHARGED
EVIDENCE: CONSTRUCTIVE-COUNTEREXAMPLE

---

## F1-TRACE-REV-006 — Origin and Reversal Remain Separately Traceable

The canonical identity constraints require distinct event identifiers for e_0 and
e_r and preserve both edges in the historical path.

Under those representation assumptions, separate reconstruction is derivable.

Runtime persistence of those records remains to be verified.

RESULT: PARTIAL
EVIDENCE: TRACEABILITY-ARGUMENT + RUNTIME-EVIDENCE-REQUIRED
