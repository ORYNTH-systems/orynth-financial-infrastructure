# Financial Finality Classification Model

## Purpose

Finality is a classification plane over observed financial state.

It is not identical to lifecycle completion.

Let:

F = {
    NOT_APPLICABLE,
    UNASSESSED,
    PENDING,
    PROVISIONAL,
    REVERSIBLE,
    CONDITIONALLY_FINAL,
    FINAL,
    DISPUTED,
    REOPENED,
    INDETERMINATE
}

---

## Classification Semantics

### UNASSESSED
No finality determination has yet been made.

### PENDING
Finality determination cannot yet be completed.

### PROVISIONAL
Current state is provisionally recognized but remains subject to defined later transition.

### REVERSIBLE
A valid reversal path remains available.

### CONDITIONALLY_FINAL
Finality holds only while specified conditions remain true.

### FINAL
The architecture recognizes the relevant settlement state as final under the applicable finality model.

### DISPUTED
Competing finality claims or unresolved authoritative conflicts exist.

### REOPENED
A previously final or conditionally final state has re-entered an active resolution path under an explicitly authorized mechanism.

### INDETERMINATE
Available evidence cannot support a valid finality classification.

---

## Critical Rule

FINAL does not by itself imply:

- lawful authorization,
- historical integrity,
- continuity,
- absence of compromise,
- absence of invalid prior state.

Technical finality and governance validity remain distinct.
