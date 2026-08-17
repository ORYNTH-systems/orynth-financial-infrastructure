# F2 Authority Requirement Schema

Each distributed authority requirement SHALL be representable as:

AuthorityRequirement = {
    requirement_id,
    proposal_id,
    action,
    scope,
    authority_source,
    required_actor_class,
    independence_class,
    temporal_requirement,
    delegation_policy,
    applicability_rule,
    jurisdictional_rule,
    evidence_requirement
}

## Minimum Evaluation

A requirement may be classified as:

SATISFIED

UNSATISFIED

CONFLICTED

STALE

OUT-OF-SCOPE

INAPPLICABLE

INDETERMINATE

No requirement with state:

CONFLICTED
STALE
OUT-OF-SCOPE
INDETERMINATE

may be silently treated as SATISFIED.

## Requirement Completeness

AuthorityComplete(q,t)

requires all applicable required authority requirements to resolve to
SATISFIED.

INAPPLICABLE requirements are excluded only when their applicability
rule is itself determinately false.

Unknown applicability does not equal inapplicable.
