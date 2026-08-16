# F1 — Compensation Lineage Model

## Purpose

Every compensating execution must remain causally linked to the divergence it addresses.

---

## Compensation Record

Each compensation event must identify:

- compensation_event_id
- originating_execution_id
- immediate_parent_remediation_id if recursive
- remediation_depth
- residual_before_reference
- compensation_target_reference
- authority_reference
- admission_reference
- execution_attempt_reference
- effect_signature_reference
- residual_after_reference
- evidence_references
- classification

---

## Parent Rule

For initial compensation:

parent = originating execution.

For recursive compensation:

parent = immediately preceding remediation execution that produced the unresolved divergence.

---

## Root Rule

Every recursive compensation chain must resolve to one originating root event.

---

## No Lineage Rewriting

Later compensation may not replace the parent reference of earlier remediation records.

The graph is append-only at the logical-history level.

---

## Depth Rule

If parent depth = n:

child depth = n + 1.

Depth alone does not establish success or authority.
