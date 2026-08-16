# F1 — Effect Dimension Type Model

## Purpose

Every effect dimension must declare how intended and observed effects may be compared.

---

## Dimension Types

### QUANTITATIVE

Examples:

- monetary amount,
- quantity,
- collateral amount.

Supported relations may include:

=,
<,
>,
difference,
ratio.

---

### RELATIONAL

Examples:

- ownership,
- custody,
- beneficiary,
- counterparty assignment.

Comparison is based on relation identity and direction.

---

### DISCRETE_STATE

Examples:

- obligation OPEN -> DISCHARGED,
- settlement PENDING -> SETTLED,
- lock state UNLOCKED -> LOCKED.

Comparison is state-transition based.

---

### SET_VALUED

Examples:

- affected parties,
- affected accounts,
- obligation sets,
- validator sets.

Comparison may use:

subset,
proper subset,
equality,
unexpected additional members.

---

### GRAPH_STATE

Examples:

- propagated settlement state,
- dependency execution,
- cross-system settlement path.

Comparison is graph-structural.

---

### ORDERED_SEQUENCE

Examples:

- ledger sequence,
- settlement sequence,
- event chronology.

Comparison is sequence-aware.

---

### OPAQUE_TYPED

Used where equality or domain-specific validation exists but no meaningful ordering can be assumed.

---

## Rule

A dimension type must not expose arithmetic operations that are not meaningful for that domain.

For example:

ownership + custody

has no generic scalar meaning.

Therefore no universal weighted sum is assumed by F1.
