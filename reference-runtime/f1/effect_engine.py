from __future__ import annotations

from .types import (
    DimensionComparison,
    DimensionOutcome,
    DimensionType,
    EffectDimension,
    EffectSignature,
    GlobalEffectClass,
)


def compare_dimension(d: EffectDimension) -> DimensionComparison:
    if not d.evidence_present:
        return DimensionComparison(
            d.dimension_id,
            DimensionOutcome.INDETERMINATE,
            {"reason": "required evidence unavailable"},
        )

    if d.dimension_type == DimensionType.QUANTITATIVE:
        i = d.intended
        o = d.observed

        if o == 0:
            outcome = DimensionOutcome.NO_EFFECT
        elif o == i:
            outcome = DimensionOutcome.FULL_MATCH
        elif i > 0 and 0 < o < i:
            outcome = DimensionOutcome.PARTIAL_MATCH
        elif i < 0 and i < o < 0:
            outcome = DimensionOutcome.PARTIAL_MATCH
        elif abs(o) > abs(i) and (o == 0 or i == 0 or (o > 0) == (i > 0)):
            outcome = DimensionOutcome.OVER_EFFECT
        else:
            outcome = DimensionOutcome.CONTRADICTORY_EFFECT

        return DimensionComparison(
            d.dimension_id,
            outcome,
            {"intended": i, "observed": o},
        )

    if d.dimension_type in {
        DimensionType.RELATIONAL,
        DimensionType.DISCRETE_STATE,
        DimensionType.ORDERED_SEQUENCE,
        DimensionType.OPAQUE_TYPED,
    }:
        if d.observed is None:
            return DimensionComparison(
                d.dimension_id,
                DimensionOutcome.NO_EFFECT,
                {"intended": d.intended, "observed": d.observed},
            )

        if d.observed == d.intended:
            return DimensionComparison(
                d.dimension_id,
                DimensionOutcome.FULL_MATCH,
                {"intended": d.intended, "observed": d.observed},
            )

        return DimensionComparison(
            d.dimension_id,
            DimensionOutcome.CONTRADICTORY_EFFECT,
            {"intended": d.intended, "observed": d.observed},
        )

    if d.dimension_type == DimensionType.SET_VALUED:
        intended = set(d.intended)
        observed = set(d.observed)

        if not observed:
            outcome = DimensionOutcome.NO_EFFECT
        elif observed == intended:
            outcome = DimensionOutcome.FULL_MATCH
        elif observed < intended:
            outcome = DimensionOutcome.PARTIAL_MATCH
        elif intended < observed:
            outcome = DimensionOutcome.OVER_EFFECT
        else:
            outcome = DimensionOutcome.CONTRADICTORY_EFFECT

        return DimensionComparison(
            d.dimension_id,
            outcome,
            {
                "missing": sorted(intended - observed),
                "unexpected": sorted(observed - intended),
            },
        )

    if d.dimension_type == DimensionType.GRAPH_STATE:
        intended_nodes = set(d.intended.get("nodes", []))
        intended_edges = {tuple(x) for x in d.intended.get("edges", [])}
        observed_nodes = set(d.observed.get("nodes", []))
        observed_edges = {tuple(x) for x in d.observed.get("edges", [])}

        if not observed_nodes and not observed_edges:
            outcome = DimensionOutcome.NO_EFFECT
        elif observed_nodes == intended_nodes and observed_edges == intended_edges:
            outcome = DimensionOutcome.FULL_MATCH
        elif observed_nodes <= intended_nodes and observed_edges <= intended_edges:
            outcome = DimensionOutcome.PARTIAL_MATCH
        elif intended_nodes <= observed_nodes and intended_edges <= observed_edges:
            outcome = DimensionOutcome.OVER_EFFECT
        else:
            outcome = DimensionOutcome.CONTRADICTORY_EFFECT

        return DimensionComparison(
            d.dimension_id,
            outcome,
            {
                "missing_nodes": sorted(intended_nodes - observed_nodes),
                "unexpected_nodes": sorted(observed_nodes - intended_nodes),
                "missing_edges": sorted(intended_edges - observed_edges),
                "unexpected_edges": sorted(observed_edges - intended_edges),
            },
        )

    raise ValueError(f"Unsupported dimension type: {d.dimension_type}")


def classify_effect(dimensions: list[EffectDimension]) -> EffectSignature:
    comparisons = [compare_dimension(d) for d in dimensions if d.required]

    outcomes = [c.outcome for c in comparisons]

    if any(x == DimensionOutcome.INDETERMINATE for x in outcomes):
        global_class = GlobalEffectClass.E_INDETERMINATE

    elif any(
        x in {
            DimensionOutcome.CONTRADICTORY_EFFECT,
            DimensionOutcome.OVER_EFFECT,
        }
        for x in outcomes
    ):
        global_class = GlobalEffectClass.E_MIXED

    elif outcomes and all(x == DimensionOutcome.FULL_MATCH for x in outcomes):
        global_class = GlobalEffectClass.E_COMPLETED

    elif outcomes and all(x == DimensionOutcome.NO_EFFECT for x in outcomes):
        global_class = GlobalEffectClass.E_NO_EFFECT

    elif any(
        x in {
            DimensionOutcome.PARTIAL_MATCH,
            DimensionOutcome.FULL_MATCH,
        }
        for x in outcomes
    ):
        global_class = GlobalEffectClass.E_PARTIAL

    else:
        global_class = GlobalEffectClass.E_INDETERMINATE

    return EffectSignature(
        comparisons=comparisons,
        global_class=global_class,
    )
