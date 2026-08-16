# F1 — Reversal Examples

## Example 1 — Exact Quantitative Reversal

Original execution:

A -> B : 100 units.

Current state still permits valid return of exactly 100 units.

No legitimate intervening mutation conflicts.

Independently authorized reversal executes successfully.

Classification:

REV_EXACT.

History still contains both transfers.

---

## Example 2 — Partial Reversal

Original:

100 units transferred.

Only 70 units remain reversibly available.

Authorized reversal returns 70.

Classification:

REV_PARTIAL.

Residual divergence remains.

---

## Example 3 — Over-Reversal

Target:

return 100.

Observed:

return 110.

Classification:

REV_OVER.

---

## Example 4 — Wrong Object

Target:

reverse transfer of Asset X.

Execution instead transfers Asset Y.

Classification:

REV_WRONG_OBJECT.

---

## Example 5 — Stale Prior State

Asset moved A -> B.

B later legitimately transferred asset to C.

A reversal target attempting blind restoration B -> A is stale.

The legitimate B -> C mutation must not be erased.

Classification:

REV_STALE_TARGET or REV_INTERVENING_CONFLICT depending on target semantics.

---

## Example 6 — Non-Reversible Dimension

A legally completed disclosure or consumed resource cannot be returned to its pre-effect state.

Classification:

REV_NON_REVERSIBLE.

Compensation may still be possible.

---

## Example 7 — Recursive Reversal

r1 is independently admitted.

r1 itself becomes partial.

A new remediation decision may:

- require r2,
- switch to compensation,
- contain and reconcile.

r2 does not inherit authority from r1.

---

## Example 8 — Exact State Projection Without Historical Restoration

After reversal:

cash balances match the pre-originating state.

But history contains:

originating execution,
intervening observations,
reversal.

Thus:

projected current-state equality

does not imply:

historical equality.
