# F1 — Partial Transition Function

## Formal Definition

Let X_F1 be the F1 product-state space.

Let O_F1 be the set of F1 post-effect operations.

Define:

Delta_F1 : X_F1 x O_F1 -> X_F1

as a partial function.

The function is partial because not every operation is structurally defined from every state.

---

## Operation Set

O_F1 = {
    OBSERVE_EFFECT,
    CONTAIN,
    REQUIRE_COMPENSATION,
    ADMIT_COMPENSATION,
    EXECUTE_COMPENSATION,
    REQUIRE_REVERSAL,
    ADMIT_REVERSAL,
    EXECUTE_REVERSAL,
    REQUIRE_RECONCILIATION,
    RECONCILE,
    REQUEST_FINALITY_CLASSIFICATION,
    REQUEST_CONTINUITY_CLASSIFICATION,
    MARK_INDETERMINATE
}

---

## Structural Rules

### Effect Observation

OBSERVE_EFFECT may alter E.

It does not create authority.

---

### Containment

CONTAIN may alter R:

R_CONTAINMENT_REQUIRED
-> R_CONTAINED

Containment does not imply reconciliation.

---

### Compensation Requirement

REQUIRE_COMPENSATION may alter R:

R_NONE / R_CONTAINED
-> R_COMPENSATION_REQUIRED

This transition does not authorize compensation.

---

### Compensation Admission

ADMIT_COMPENSATION may alter R only after independent admission:

R_COMPENSATION_REQUIRED
-> R_COMPENSATION_ADMISSION_PENDING
-> R_COMPENSATING

The exact admissibility predicate is inherited and specialized later.

---

### Compensation Execution

EXECUTE_COMPENSATION may produce:

E_COMPENSATING_COMPLETED

or:

E_COMPENSATING_PARTIAL

or:

E_INDETERMINATE

and corresponding remediation state.

---

### Reversal Requirement

REQUIRE_REVERSAL may alter R:

R_NONE / R_CONTAINED
-> R_REVERSAL_REQUIRED

Requirement does not authorize reversal.

---

### Reversal Admission

ADMIT_REVERSAL may alter R only after independent admission:

R_REVERSAL_REQUIRED
-> R_REVERSAL_ADMISSION_PENDING
-> R_REVERSING

---

### Reversal Execution

EXECUTE_REVERSAL may produce:

E_REVERSAL_COMPLETED

or:

E_REVERSAL_PARTIAL

or:

E_INDETERMINATE

---

### Reconciliation

REQUIRE_RECONCILIATION:

Q_NOT_REQUIRED
-> Q_REQUIRED

RECONCILE:

Q_REQUIRED
-> Q_PENDING
-> Q_IN_PROGRESS
-> {
    Q_RECONCILED,
    Q_DIVERGENT,
    Q_INDETERMINATE
}

---

## Undefined Transition Principle

If Delta_F1(x,o) is undefined, the architecture SHALL NOT infer a valid destination state.

Undefined means structurally unavailable.

Undefined is distinct from:

- inadmissible,
- failed,
- blocked,
- indeterminate.

---

## Admission Separation

Defined(x,o)
does not imply
Admitted(x,o)

Admitted(x,o)
does not imply
Executed(x,o)

Executed(x,o)
does not imply
SuccessfulRemediation(x,o)

SuccessfulRemediation(x,o)
does not imply
ContinuityPreserved.
