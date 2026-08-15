# Financial Proof Status Model

## Purpose

This model prevents proof-status inflation.

The following states are distinct and SHALL NOT be used interchangeably:

OPEN
FORMALIZED
TESTED
PROVED
DISCHARGED
FAILED
BLOCKED
NOT_APPLICABLE

---

## OPEN

The obligation exists but has not yet been formally discharged.

---

## FORMALIZED

The obligation has an explicit mathematical or logical statement with identified premises and conclusion.

FORMALIZED does not imply tested or proved.

---

## TESTED

One or more executable tests or adversarial cases exercise the obligation.

TESTED does not imply universal proof.

---

## PROVED

A valid proof has been supplied under explicit premises.

PROVED does not automatically imply repository discharge unless required evidence, correspondence, and verification gates also pass.

---

## DISCHARGED

The proof obligation has satisfied all required discharge criteria, including:

- formal statement,
- premises,
- proof or accepted verification method,
- evidence,
- implementation correspondence where required,
- adversarial or counterexample treatment where required,
- traceability,
- independent review requirement where applicable.

---

## FAILED

A counterexample or contradiction demonstrates the obligation does not currently hold.

---

## BLOCKED

The obligation cannot be evaluated because prerequisite work is unresolved.

---

## NOT_APPLICABLE

The obligation is explicitly non-applicable to the assessed subject.

NOT_APPLICABLE is not PASS.

---

## Mandatory Separation

ASSERTED != FORMALIZED

FORMALIZED != TESTED

TESTED != PROVED

PROVED != DISCHARGED

NO_OBSERVED_FAILURE != PROVED

NOT_APPLICABLE != PASSED
