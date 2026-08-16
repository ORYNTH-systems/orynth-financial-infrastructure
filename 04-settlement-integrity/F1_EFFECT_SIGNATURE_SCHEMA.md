# F1 — Effect Signature Schema

Every F1 effect classification must retain a dimension-level signature.

Required structure:

effect_event_id

observation_time

intended_effect_reference

observed_effect_reference

dimensions[]

For each dimension:

- dimension_id
- dimension_type
- intended_value_reference
- observed_value_reference
- comparison_result
- evidence_reference
- confidence_or_determinacy_state
- required_for_full_effect

Global fields:

- effect_signature
- global_effect_class
- classification_policy_version
- unresolved_dimensions
- contradictory_dimensions
- over_effect_dimensions
- evidence_references

---

## Rule

The global effect class must remain reconstructable from the retained dimension-level signature.

The system must not store only:

PARTIAL

while discarding why the effect was partial.
