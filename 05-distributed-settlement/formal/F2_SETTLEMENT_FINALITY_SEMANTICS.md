# FIN-F2-06 — Settlement Finality Semantics

## 1. Purpose

Settlement finality classifies whether a distributed financial
settlement has satisfied the complete set of profile-defined conditions
required for the settlement state to be treated as final within an
identified domain and evaluation context.

Finality is not:

agreement
consensus
authority
admissibility
execution
atomic completion
technical terminality
irreversibility
historical continuity

Finality is profile-relative and domain-relative.

---

## 2. Finality Profile

For distributed settlement q_d, define:

FP(q_d)

as the active finality profile.

FP SHALL identify at minimum:

- finality domain
- required execution conditions
- required effect conditions
- evidence requirements
- temporal requirements
- dependency requirements
- reconciliation requirements
- conflict exclusions
- jurisdictional or institutional applicability where relevant
- revocation / reversal treatment
- terminality requirements
- any cross-domain recognition requirements

A statement that a settlement is "final" without identifying the
applicable finality profile or domain is incomplete.

---

## 3. Finality Domain

Define:

D_f

as a finality domain.

Examples of domain classes may include:

- protocol
- ledger
- clearing
- settlement system
- custodian
- institutional
- contractual
- legal
- jurisdictional
- cross-system

F2-06 does not claim that any one domain dominates all others.

---

## 4. Finality Predicate

Define:

SettlementFinal(q_d,t | FP,D_f)

iff every applicable finality requirement defined by FP for domain D_f
is determinately satisfied at time t.

SettlementFinal is therefore both profile-relative and domain-relative.

---

## 5. Finality Requirement Set

Define:

FR(q_d,FP,D_f,t)

as the set of applicable finality requirements.

For each requirement rho_f:

FinalitySatisfied(rho_f,q_d,t)

must be evaluated independently.

SettlementFinal requires every applicable required finality obligation
to resolve to SATISFIED.

---

## 6. Finality Requirement States

A finality requirement may classify as:

SATISFIED

UNSATISFIED

PENDING

CONFLICTED

STALE

OUT-OF-SCOPE

INAPPLICABLE

INDETERMINATE

No requirement in:

PENDING
CONFLICTED
STALE
OUT-OF-SCOPE
INDETERMINATE

may be silently treated as SATISFIED.

---

## 7. Settlement Finality Classification

Define:

FinalityResult(q_d,t | FP,D_f)

in:

FINAL

NOT-FINAL

FINALITY-PENDING

FINALITY-CONFLICTED

FINALITY-INDETERMINATE

FINALITY-REVALIDATION-REQUIRED

FINALITY-RECONSTRUCTION-REQUIRED

---

## 8. FINAL

FINAL means every applicable required finality condition for FP and D_f
is determinately satisfied.

FINAL does not imply irreversible.

FINAL does not imply historically uninterrupted.

FINAL does not imply continuity preserved.

FINAL does not imply final in another domain.

---

## 9. NOT-FINAL

NOT-FINAL means at least one applicable required finality condition is
determinately unsatisfied and no classification requiring pending,
conflict, reconstruction, or revalidation supersedes it.

---

## 10. FINALITY-PENDING

FINALITY-PENDING means one or more applicable finality requirements
remain legitimately unresolved because required events, windows,
confirmations, dependencies, or external recognitions have not yet
completed.

Pending != Final.

Pending != Failed.

---

## 11. FINALITY-CONFLICTED

FINALITY-CONFLICTED applies where recognized evidence contains mutually
incompatible finality-relevant claims or observations that prevent one
determinate finality classification.

Conflict shall not be resolved by simply choosing:

majority
latest timestamp
fastest system
largest validator set
first terminal state
last terminal state

unless an explicit governing rule defines that precedence.

---

## 12. FINALITY-INDETERMINATE

FINALITY-INDETERMINATE applies where evidence is insufficient to
determine finality.

Unknown != Not-Final.

Unknown != Final.

---

## 13. FINALITY-REVALIDATION-REQUIRED

This class applies where a prior finality determination cannot be safely
reused because:

- authority changed
- scope changed
- temporal validity changed
- profile changed
- dependency state changed
- external recognition changed
- required evidence aged or became stale

Historical finality evidence may persist while current finality requires
reevaluation.

---

## 14. FINALITY-RECONSTRUCTION-REQUIRED

This class applies where sufficient current finality classification
cannot be made without reconstructing prior execution, evidence,
effects, dependencies, or recognized state.

Reconstruction is not finality.

Reconstruction may enable later finality evaluation.

---

## 15. Consensus and Finality

Consensus(q_d,phi,t|CP) !=> SettlementFinal(q_d,t|FP,D_f)

Consensus establishes only the profile-defined collective-recognition
condition.

A consensus result may exist while finality remains:

PENDING
CONFLICTED
INDETERMINATE
NOT-FINAL

---

## 16. Authority and Finality

AuthorityComplete(q_d,t) !=> SettlementFinal(q_d,t|FP,D_f)

Valid authority does not establish occurrence, effect completion, or
finality.

---

## 17. Admissibility and Finality

Admissible_d(q_d,t) !=> SettlementFinal(q_d,t|FP,D_f)

Admission permits execution.

It does not prove execution or finality.

---

## 18. Execution and Finality

Executed(q_d,t) !=> SettlementFinal(q_d,t|FP,D_f)

Execution occurrence does not establish that all finality conditions
have been satisfied.

---

## 19. Atomic Completion and Finality

AtomicComplete(q_d,t|AP) !=> SettlementFinal(q_d,t|FP,D_f)

Atomic completion establishes required effect composition under AP.

Finality may require additional:

- evidence
- time
- external recognition
- institutional acceptance
- legal conditions
- conflict resolution
- reconciliation
- cross-domain completion

---

## 20. Local Finality

Define:

LocalFinal(q_d,t,D_1)

as finality within one domain D_1.

LocalFinal(q_d,t,D_1) !=> LocalFinal(q_d,t,D_2)

for D_1 != D_2.

Therefore:

local finality != universal finality

---

## 21. Cross-Domain Finality

Define:

CrossDomainFinal(q_d,t,D*)

only where a profile explicitly identifies a required domain set:

D* = {D_1,...,D_n}

and every required domain-level finality condition has been
determinately satisfied together with any cross-domain consistency
requirements.

Cross-domain finality is not inferred merely because one domain is final.

---

## 22. Finality and Irreversibility

SettlementFinal(q_d,t|FP,D_f) !=> Irreversible(q_d)

Finality may coexist with mechanisms for:

reversal
correction
legal remedy
administrative intervention
constitutional override
authorized counter-transition

Finality describes status under the applicable profile.

Irreversibility describes whether a state can ever be changed.

These are distinct.

---

## 23. Technical Finality and Legal Finality

TechnicalFinal(q_d,t) !=> LegalFinal(q_d,t)

LegalFinal(q_d,t) !=> TechnicalFinal(q_d,t)

A technical system and a legal or institutional system may evaluate
different properties.

Neither is automatically substituted for the other.

---

## 24. Ledger Inclusion and Finality

LedgerIncluded(q_d,t) !=> SettlementFinal(q_d,t|FP,D_f)

Inclusion is evidence of a ledger event.

It is not universal evidence of settlement finality.

---

## 25. Confirmation Count and Finality

ConfirmationThresholdSatisfied(q_d,t) !=> SettlementFinal(q_d,t|FP,D_f)

unless the active finality profile explicitly defines confirmation
threshold satisfaction as sufficient for that identified domain.

Even then, the result remains domain-relative.

---

## 26. Finality and Reversal

A settlement that was final under a profile may later be subject to a
new authorized reversal or counter-transition where the governing
architecture permits one.

Such later reversal does not prove the earlier finality determination
never existed.

Historical finality and later state change may both be true.

---

## 27. Finality and Compensation

Successful compensation does not prove the original settlement was
final.

Successful compensation does not erase earlier non-final or partial
execution history.

---

## 28. Finality and Continuity

SettlementFinal(q_d,t|FP,D_f) !=> ContinuityPreserved(q_d)

A path may reach a final state after:

- partial execution
- interruption
- conflict
- repair
- reversal
- reconstruction

Final endpoint classification does not establish uninterrupted
continuity.

---

## 29. Finality Principle

The full separation remains:

agreement
!= consensus
!= authority
!= admissibility
!= execution
!= effect completion
!= atomic completion
!= settlement finality
!= irreversibility
!= continuity preservation

No one property shall be silently promoted into another.
