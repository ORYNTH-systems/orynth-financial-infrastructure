# FIN-F2-07 — Distributed Conflict Semantics

## 1. Purpose

Distributed financial execution may produce incompatible observations,
claims, commitments, authority assertions, effect histories, or finality
states.

Conflict is not automatically error.

Conflict is not automatically fraud.

Conflict is not automatically fork.

Conflict is not automatically partial effect.

Conflict is not automatically finality failure.

Conflict is a formal state requiring classification.

---

## 2. Conflict Record

Define:

ConflictRecord k = {
    conflict_id,
    proposal_id,
    conflict_class,
    involved_objects,
    involved_actors,
    involved_domains,
    observed_values,
    evidence_set,
    first_observed_time,
    current_status,
    governing_rule
}

---

## 3. Conflict Predicate

Define:

Conflict(q_d,t)

iff the recognized evidence for q_d contains two or more mutually
incompatible claims or states relevant to the same required decision,
execution, effect, or finality determination.

---

## 4. Conflict Classes

ConflictClass(q_d,t) may include:

AUTHORITY-CONFLICT

AGREEMENT-CONFLICT

COMMITMENT-CONFLICT

CONSENSUS-CONFLICT

EXECUTION-ORDER-CONFLICT

EFFECT-CONFLICT

OBSERVATION-CONFLICT

FINALITY-CONFLICT

CROSS-DOMAIN-CONFLICT

EVIDENCE-CONFLICT

STATE-CONFLICT

MULTI-CLASS-CONFLICT

---

## 5. Conflict != Indeterminacy

Conflict and indeterminacy are distinct.

Conflict means incompatible recognized evidence exists.

Indeterminacy means sufficient evidence for a determinate conclusion is
absent.

A state may be:

conflicted but well-evidenced

indeterminate without conflict

both conflicted and indeterminate

neither.

---

## 6. Conflict != Partial Effect

Conflict(q_d,t) !=> PARTIAL(q_d,t)

A system may contain inconsistent observations concerning a settlement
without sufficient evidence that a strict subset of intended economic
mutations occurred.

Likewise:

PARTIAL(q_d,t) !=> Conflict(q_d,t)

Partial effect may be unanimously observed.

---

## 7. Conflict != Fork

Conflict(q_d,t) !=> Fork(q_d,t)

Fork is a specialized divergence structure defined later in this pass.

Not every disagreement or incompatible claim constitutes a fork.

---

## 8. Conflict and Authority

AuthorityConflict(q_d,t)

shall not be resolved solely by:

majority vote
validator count
latest observation
earliest observation
execution speed
key possession
consensus weight

unless an explicit authority-precedence rule governs that exact conflict.

---

## 9. Conflict and Finality

FinalityConflict(q_d,t)

prevents automatic promotion to FINAL where the conflicting evidence is
material to the active finality profile.

Conflict must be resolved, excluded as inapplicable, or determinately
classified under a governing rule.

---

## 10. Historical Persistence

Once a material conflict has been observed and evidenced, later
resolution does not erase the historical existence of the conflict.

Resolved != Never Conflicted.
