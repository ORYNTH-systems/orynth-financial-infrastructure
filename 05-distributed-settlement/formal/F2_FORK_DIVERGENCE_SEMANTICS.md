# FIN-F2-07 — Fork / Divergence Semantics

## 1. Purpose

A fork is a structured divergence in recognized distributed state or
execution history.

Fork semantics are system-independent.

This pass does not assume blockchain.

---

## 2. Fork Predicate

Define:

Fork(q_d,t)

iff at least two recognized branches:

B_1
B_2

exist for q_d such that:

B_1 != B_2

and both claim relevance to the same distributed settlement history or
state lineage.

---

## 3. Branch

A branch SHALL identify:

- branch identity
- predecessor state
- branch-producing event
- execution/effect trace
- evidence
- recognizing participants/domains
- current status

---

## 4. Fork Classes

ForkClass may include:

STATE-FORK

EXECUTION-FORK

OBSERVATION-FORK

FINALITY-FORK

CROSS-DOMAIN-FORK

EVIDENCE-FORK

---

## 5. Fork != Consensus Failure

Fork(q_d,t) !=> ConsensusNotAchieved(q_d,t)

A system may reach local consensus on multiple incompatible branches
under different scopes, times, profiles, or domains.

---

## 6. Fork != Invalidity

Fork(q_d,t) !=> Invalid(q_d,t)

A fork may contain:

one valid branch and one invalid branch

multiple locally valid but mutually incompatible branches

historical branch evidence after one branch is superseded

insufficient evidence to establish which branch governs.

---

## 7. Canonical Branch

Define:

CanonicalBranch(q_d,t | GR)

only where an explicit governing rule GR determinately selects the
branch authoritative for the relevant evaluation context.

Canonicality is rule-relative.

It is not created by mere popularity.

---

## 8. Canonical != Historical Erasure

If B_1 becomes canonical:

CanonicalBranch(q_d,t) = B_1

then:

B_2 existed historically

may remain true.

Canonical selection does not rewrite history.

---

## 9. Fork Resolution

Fork resolution may yield:

CANONICAL-BRANCH-SELECTED

MULTIPLE-DOMAIN-BRANCHES-RETAINED

RECONSTRUCTION-REQUIRED

REVALIDATION-REQUIRED

UNRESOLVED

INDETERMINATE

---

## 10. Economic Equivalence

If two branches later converge to economically equivalent endpoint
states:

Endpoint(B_1) ≡E Endpoint(B_2)

this does not establish historical identity.

Economic equivalence != branch identity.
