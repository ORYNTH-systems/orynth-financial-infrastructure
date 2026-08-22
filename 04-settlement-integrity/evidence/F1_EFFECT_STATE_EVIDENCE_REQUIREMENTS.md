# F1 Effect-State Evidence Requirements

## Classification Evidence

The classifier must be capable of distinguishing:

- established occurrence,
- established non-occurrence,
- unresolved occurrence,
- conflicting evidence.

Absence of an observation record does not satisfy established non-occurrence.

---

## Minimum Evidence Dimensions

For each intended mutation m_i, a conformant future runtime profile should be able
to represent:

1. mutation identity;
2. intended resource/state target;
3. observation status;
4. commitment status;
5. economic-recognition status;
6. occurrence evidence;
7. non-occurrence evidence where applicable;
8. provenance;
9. observation time;
10. commitment time where applicable;
11. confidence or determinacy status where required by the profile.

---

## Classification Integrity

NO-EFFECT requires evidence sufficient to establish non-occurrence for every
material intended mutation.

PARTIAL requires evidence sufficient to establish both:

- occurrence of at least one material intended mutation;
- non-occurrence of at least one other material intended mutation.

COMPLETED requires evidence sufficient to establish occurrence of every intended
material economic mutation.

INDETERMINATE is required whenever material occurrence state remains unresolved.

---

## External Effects

Evidence may originate outside the local runtime.

A local runtime cannot classify NO-EFFECT solely because its own state was rolled
back when external or counterparty systems may have committed economic mutation.

---

## Preservation Rule

Later compensation, reversal, or reconciliation evidence must reference the
original effect history rather than replace it.
