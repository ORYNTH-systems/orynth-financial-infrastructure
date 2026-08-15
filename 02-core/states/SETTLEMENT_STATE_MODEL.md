# Settlement State Model

## Purpose

Settlement state is a specialized state plane and SHALL NOT be collapsed into the general execution lifecycle.

Let:

S_S = {
    NONE,
    PENDING,
    IN_PROGRESS,
    PARTIAL,
    PROVISIONAL,
    SETTLED,
    INTERRUPTED,
    COMPENSATION_PENDING,
    COMPENSATED,
    REVERSAL_PENDING,
    REVERSED,
    RECONCILIATION_PENDING,
    RECONCILED,
    FINALITY_PENDING,
    FINALIZED,
    INDETERMINATE
}

---

## Core Separation

Execution completion and settlement completion are distinct.

Execution may be COMPLETED while settlement is:

- PENDING,
- PARTIAL,
- PROVISIONAL,
- INDETERMINATE.

Settlement may be RECONCILED without continuity being restored.

Settlement may be FINALIZED without establishing that the originating execution was governance-valid.

---

## Required Settlement Observation

A SettlementState observation must bind:

- settlement_id,
- execution_event_id,
- current settlement state,
- participating actors,
- affected resources,
- observed effects,
- evidence,
- observation time,
- finality status,
- continuity status if already classified.
