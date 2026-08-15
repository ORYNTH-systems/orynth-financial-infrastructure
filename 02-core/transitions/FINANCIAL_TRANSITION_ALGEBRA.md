# Financial Transition Algebra

## Formal Domain

Let S_F be the canonical financial lifecycle-state set.

Let Q_F be the canonical transition-operation set.

Define:

Delta_F : S_F x Q_F -> S_F

as a partial transition function.

The function is intentionally partial.

A transition that is not defined by the architecture SHALL NOT be inferred merely because software is technically capable of producing the destination state.

---

## Important Separation

TransitionDefined(s,q)
does not imply
TransitionAdmissible(s,q)

TransitionAdmissible(s,q)
does not imply
TransitionExecuted(s,q)

TransitionExecuted(s,q)
does not imply
Finality

Finality
does not imply
Continuity

---

## Canonical Transition Families

### Proposal Family

PROPOSED -> AUTHORIZED

PROPOSED may also terminate without authorization.

---

### Admission Family

AUTHORIZED -> ADMITTED

Authorization alone does not force admission.

---

### Execution Family

ADMITTED -> EXECUTING

EXECUTING may produce:

- COMPLETED
- PARTIAL
- INTERRUPTED
- INDETERMINATE

---

### Partial-Effect Family

PARTIAL may transition toward:

- CONTAINED
- COMPENSATION_REQUIRED
- REVERSAL_REQUIRED
- RECONCILIATION_REQUIRED
- INDETERMINATE

No automatic rollback is assumed.

---

### Completion Family

COMPLETED may transition toward:

- FINALITY_PENDING
- RECONCILIATION_REQUIRED
- COMPENSATION_REQUIRED
- REVERSAL_REQUIRED

Completion is not a terminal guarantee.

---

### Compensation Family

COMPENSATION_REQUIRED -> COMPENSATING

COMPENSATING may transition toward:

- COMPENSATED
- PARTIAL
- INTERRUPTED
- INDETERMINATE

Compensation itself is financially consequential execution.

---

### Reversal Family

REVERSAL_REQUIRED -> REVERSING

REVERSING may transition toward:

- REVERSED
- PARTIAL
- INTERRUPTED
- INDETERMINATE

Reversal is not historical erasure.

---

### Reconciliation Family

RECONCILIATION_REQUIRED -> RECONCILING

RECONCILING may transition toward:

- RECONCILED
- INDETERMINATE

---

### Classification Family

RECONCILED -> FINALITY_PENDING

FINALITY_PENDING -> CLASSIFIED

Classification requires separate finality and continuity outputs.

---

## No Implicit Terminal State

CLASSIFIED is terminal only for the specific assessed lifecycle instance.

New evidence, newly authorized remediation, legal reopening, or externally authoritative transition may create a new execution event.

Historical states SHALL NOT be overwritten merely because a later lifecycle exists.
