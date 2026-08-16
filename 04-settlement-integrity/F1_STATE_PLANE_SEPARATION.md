# F1 — State Plane Separation

The F1 architecture contains distinct state planes.

## Effect Plane

Answers:

What economic mutation occurred?

## Settlement Plane

Answers:

What is the settlement status of the relevant financial obligation or transfer?

## Resolution Plane

Answers:

What containment, compensation, reversal, or remediation state exists?

## Reconciliation Plane

Answers:

Has the observed execution/effect/settlement history been reconciled?

## Finality Plane

Answers:

What finality classification currently applies?

## Continuity Plane

Answers:

Was integrity preserved, broken, reconstructed, restored-function-only, or indeterminate?

---

## Prohibited Collapse

Effect state must not determine settlement state by implication.

Settlement state must not determine resolution state by implication.

Resolution state must not determine reconciliation by implication.

Reconciliation must not determine finality by implication.

Finality must not determine continuity by implication.

No plane may overwrite another plane.
