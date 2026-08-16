# F1 — Reconciliation and Continuity Examples

## Example 1 — Reconciled and Restored Economically, But Continuity Broken

Originating execution partially transfers 100-unit obligation.

Compensation later restores the target balance.

Current projected balance equals intended balance.

History is fully evidenced.

Classification may be:

RECONCILED

PROJECTED_ECONOMIC_EQUIVALENCE

FUNCTION_RESTORED

CONTINUITY_BROKEN

because later compensation does not make the original discontinuity disappear.

---

## Example 2 — Reconciled but Divergent

Asset cannot be reversed.

All history is known.

Current ownership divergence is explicit.

No further valid remediation exists.

The architecture may classify history as reconciled while retaining known divergence.

---

## Example 3 — Function Restored Only

Settlement functionality resumes after reconstruction.

Historical continuity cannot be established.

Classification:

FUNCTION_RESTORED_ONLY

not:

CONTINUITY_PRESERVED.

---

## Example 4 — Historical Integrity With Broken Continuity

Every execution and remediation event is perfectly evidenced.

Evidence proves an unauthorized partial effect occurred.

Historical integrity is strong.

Continuity is broken.

Thus:

HistoricalIntegrity != ContinuityPreserved.

---

## Example 5 — Current State Equality

Reversal returns all selected current-state dimensions to their prior values.

History still contains:

originating execution,
intervening events,
reversal.

Therefore:

FullCurrentStateEquivalence

does not imply:

HistoricalEquivalence.

---

## Example 6 — Indeterminate Reconciliation

Current balances appear correct.

Required settlement evidence is missing.

Remediation lineage cannot be reconstructed.

Classification:

Q_INDETERMINATE

and potentially:

F1_CONTINUITY_INDETERMINATE.

Current balance plausibility is insufficient.
