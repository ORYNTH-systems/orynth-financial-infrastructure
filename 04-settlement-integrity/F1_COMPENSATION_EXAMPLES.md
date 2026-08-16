# F1 — Compensation Examples

## Example 1 — Exact Quantitative Compensation

Original intent:

B receives 100.

Observed:

B receives 60.

Residual:

40.

Explicit compensation target:

B receives additional 40.

Observed compensation:

40.

If all required dimensions now satisfy target predicates and no new divergence exists:

COMP_EXACT.

Historical record still contains:

original partial execution,
compensation execution.

---

## Example 2 — Partial Compensation

Residual:

40 cash units.

Compensation intended:

40.

Observed compensation:

25.

Residual after compensation:

15.

Classification:

COMP_PARTIAL.

A new remediation decision may be required.

---

## Example 3 — Over-Compensation

Residual:

40.

Observed compensation:

50.

The original deficit is eliminated, but 10 excess units now exist.

Classification:

COMP_OVER.

Not:

COMP_EXACT.

---

## Example 4 — Wrong Dimension

Divergence:

asset ownership should be B but remains C.

Compensation:

10 cash units sent to B.

Unless the authorized compensation target explicitly permits cash substitution:

COMP_WRONG_DIMENSION.

---

## Example 5 — Substitute Remedy

Asset cannot be returned.

An explicitly authorized target permits:

cash equivalent + obligation release.

If the substitute target is independently authorized and fully satisfied:

COMP_EXACT relative to the substitute target.

This does not mean original asset history was restored.

---

## Example 6 — New Divergence

Original cash deficit corrected.

Compensation also causes an unauthorized custody transfer.

Result:

COMP_NEW_DIVERGENCE.

---

## Example 7 — Recursive Compensation

Original execution e0 is partial.

Compensation c1 is admitted.

c1 itself executes partially.

A new residual Rho_1 exists.

A second compensation c2 may be proposed.

c2 requires independent admission.

Authority(c1) does not automatically imply Authority(c2).
