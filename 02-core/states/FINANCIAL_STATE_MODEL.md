# Canonical Financial State Model

## Purpose

This document defines the shared lifecycle-state vocabulary for ORYNTH Financial Infrastructure.

State identity, transition existence, transition admissibility, transition execution, finality, and continuity classification are separate concepts.

---

## Canonical Financial Lifecycle

Let:

S_F = {
    PROPOSED,
    AUTHORIZED,
    ADMITTED,
    EXECUTING,
    PARTIAL,
    COMPLETED,
    INTERRUPTED,
    CONTAINED,
    COMPENSATION_REQUIRED,
    COMPENSATING,
    COMPENSATED,
    REVERSAL_REQUIRED,
    REVERSING,
    REVERSED,
    RECONCILIATION_REQUIRED,
    RECONCILING,
    RECONCILED,
    FINALITY_PENDING,
    CLASSIFIED,
    INDETERMINATE
}

---

## State Semantics

### PROPOSED

A financially consequential execution has been represented but has not yet received execution authority.

PROPOSED does not imply AUTHORIZED.

---

### AUTHORIZED

An upstream authority mechanism has produced an authorization applicable to the proposed execution.

AUTHORIZED does not imply current admissibility.

---

### ADMITTED

Current execution-time evaluation has determined the execution is admissible at the relevant boundary.

ADMITTED does not imply that economic effect has occurred.

---

### EXECUTING

The governed execution process has begun.

EXECUTING does not imply completion.

---

### PARTIAL

At least one intended consequential economic effect has occurred, while the complete intended effect has not been established.

PARTIAL is distinct from failure with zero effect.

---

### COMPLETED

The intended execution sequence has produced its expected execution-level effect.

COMPLETED does not imply settlement finality, legal finality, continuity, or absence of later invalidity.

---

### INTERRUPTED

Execution ceased before ordinary completion.

INTERRUPTED does not itself determine whether economic effect exists.

---

### CONTAINED

Further consequential execution has been prevented following interruption, partial effect, or newly detected invalidity.

CONTAINED is a control state, not a restored-state classification.

---

### COMPENSATION_REQUIRED

The architecture has determined that a new compensating execution may be required to address prior effect.

This state does not authorize compensation.

---

### COMPENSATING

A separately authorized and admitted compensating execution is in progress.

---

### COMPENSATED

A compensating execution has completed.

COMPENSATED does not mean the original execution never occurred.

---

### REVERSAL_REQUIRED

A reversal action has been identified as potentially required.

This state does not itself authorize reversal.

---

### REVERSING

A separately authorized and admitted reversal execution is in progress.

---

### REVERSED

A reversal execution has completed.

REVERSED does not erase historical state or evidence.

---

### RECONCILIATION_REQUIRED

Observed financial state requires reconciliation before the architecture can classify the resulting condition.

---

### RECONCILING

Reconciliation is in progress.

---

### RECONCILED

Relevant observed economic state has been reconciled sufficiently for subsequent classification.

RECONCILED does not imply restoration of continuity.

---

### FINALITY_PENDING

Execution and settlement observations exist, but finality classification remains unresolved.

---

### CLASSIFIED

The resulting execution has received explicit finality and continuity classifications.

---

### INDETERMINATE

The architecture cannot currently establish a valid lifecycle classification.

INDETERMINATE is not equivalent to denial, failure, completion, or finality.

---

## Non-Equivalence Rules

AUTHORIZED != ADMITTED

ADMITTED != EXECUTED

EXECUTING != PARTIAL

PARTIAL != COMPLETED

COMPLETED != FINAL

COMPENSATED != REVERSED

REVERSED != RESTORED

RECONCILED != CONTINUOUS

FINALITY != CONTINUITY

BALANCE_EQUIVALENCE != STATE_EQUIVALENCE

FUNCTIONAL_RECOVERY != HISTORICAL_RESTORATION

---

## State Observation Rule

Every lifecycle observation must identify:

- execution event,
- state,
- observation time,
- affected resource references,
- evidence references,
- applicable authority reference,
- applicable jurisdiction state,
- settlement reference where applicable.

No state may be inferred solely from absence of another state.
