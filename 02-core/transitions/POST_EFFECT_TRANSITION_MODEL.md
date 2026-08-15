# Post-Effect Transition Model

## Purpose

This model defines the architectural region beginning after economic mutation is observable.

This is the primary new territory opened for F1-F3.

---

## Entry Conditions

Post-effect governance is entered when:

EffectType != NO_EFFECT

or when evidence cannot establish NO_EFFECT.

---

## Primary Branches

### Partial Effect

EXECUTING
-> PARTIAL

Possible subsequent resolution classes:

PARTIAL
-> CONTAINED

PARTIAL
-> COMPENSATION_REQUIRED

PARTIAL
-> REVERSAL_REQUIRED

PARTIAL
-> RECONCILIATION_REQUIRED

PARTIAL
-> INDETERMINATE

---

### Completed Effect With Later Invalidity

COMPLETED
-> COMPENSATION_REQUIRED

or

COMPLETED
-> REVERSAL_REQUIRED

or

COMPLETED
-> RECONCILIATION_REQUIRED

No assumption is made that completion guarantees legitimacy.

---

### Compensation

COMPENSATION_REQUIRED
-> COMPENSATING
-> COMPENSATED
-> RECONCILIATION_REQUIRED

---

### Reversal

REVERSAL_REQUIRED
-> REVERSING
-> REVERSED
-> RECONCILIATION_REQUIRED

---

### Reconciliation

RECONCILIATION_REQUIRED
-> RECONCILING
-> RECONCILED
-> FINALITY_PENDING
-> CLASSIFIED

---

## Historical Preservation Rule

Original execution history remains evidence-bearing after compensation, reversal, or reconciliation.

Later economically equivalent state does not overwrite historical transition lineage.
