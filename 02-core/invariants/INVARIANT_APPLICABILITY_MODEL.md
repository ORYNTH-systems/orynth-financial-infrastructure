# Financial Invariant Applicability Model

## Governing Rule

Applicability and satisfaction are separate.

For invariant I and execution history H:

Applicable(I,H) != Satisfied(I,H)

An invariant that is not applicable SHALL NOT be recorded as PASS merely because no violation was observed.

---

## Applicability States

Every invariant assessment SHALL resolve to one of:

- APPLICABLE_PASS
- APPLICABLE_FAIL
- NOT_APPLICABLE
- INDETERMINATE
- NOT_ASSESSED

---

## Required Assessment Record

Every invariant assessment SHALL identify:

- invariant_id
- subject execution / state / artifact
- applicability result
- evidence references
- observed result
- assessment time
- verifier reference
- reason

---

## Fail-Closed Relationship

Where a required pre-effect invariant is APPLICABLE_FAIL or INDETERMINATE, the dependent consequential transition SHALL NOT be admitted.

Post-effect invariant failure SHALL NOT be represented as NO_EFFECT when economic mutation may already have occurred.
