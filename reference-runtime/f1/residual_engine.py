from __future__ import annotations

from .types import DimensionType, EffectDimension, Residual


def compute_residual(d: EffectDimension) -> Residual:
    """
    Compute a typed residual between intended and observed effect.

    Residual computation is dimension-specific. No universal subtraction
    operation is assumed outside quantitative dimensions.
    """

    if not d.evidence_present:
        return Residual(
            dimension_id=d.dimension_id,
            resolved=False,
            detail={
                "class": "INDETERMINATE",
            },
        )

    if d.dimension_type == DimensionType.QUANTITATIVE:
        delta = d.intended - d.observed

        return Residual(
            dimension_id=d.dimension_id,
            resolved=(delta == 0),
            detail={
                "class": "QUANTITATIVE",
                "delta": delta,
            },
        )

    if d.dimension_type in {
        DimensionType.RELATIONAL,
        DimensionType.DISCRETE_STATE,
        DimensionType.ORDERED_SEQUENCE,
        DimensionType.OPAQUE_TYPED,
    }:
        resolved = d.intended == d.observed

        return Residual(
            dimension_id=d.dimension_id,
            resolved=resolved,
            detail={
                "class": d.dimension_type.value,
                "expected": d.intended,
                "observed": d.observed,
            },
        )

    if d.dimension_type == DimensionType.SET_VALUED:
        intended = set(d.intended)
        observed = set(d.observed)

        missing = intended - observed
        unexpected = observed - intended

        return Residual(
            dimension_id=d.dimension_id,
            resolved=(not missing and not unexpected),
            detail={
                "class": "SET_VALUED",
                "missing": sorted(missing),
                "unexpected": sorted(unexpected),
            },
        )

    if d.dimension_type == DimensionType.GRAPH_STATE:
        intended_nodes = set(d.intended.get("nodes", []))
        intended_edges = {
            tuple(edge)
            for edge in d.intended.get("edges", [])
        }

        observed_nodes = set(d.observed.get("nodes", []))
        observed_edges = {
            tuple(edge)
            for edge in d.observed.get("edges", [])
        }

        missing_nodes = intended_nodes - observed_nodes
        unexpected_nodes = observed_nodes - intended_nodes
        missing_edges = intended_edges - observed_edges
        unexpected_edges = observed_edges - intended_edges

        resolved = (
            not missing_nodes
            and not unexpected_nodes
            and not missing_edges
            and not unexpected_edges
        )

        return Residual(
            dimension_id=d.dimension_id,
            resolved=resolved,
            detail={
                "class": "GRAPH_STATE",
                "missing_nodes": sorted(missing_nodes),
                "unexpected_nodes": sorted(unexpected_nodes),
                "missing_edges": sorted(missing_edges),
                "unexpected_edges": sorted(unexpected_edges),
            },
        )

    raise ValueError(
        f"Unsupported dimension type: {d.dimension_type}"
    )


def compute_residual_vector(
    dimensions: list[EffectDimension],
) -> list[Residual]:
    """
    Compute residuals for required effect dimensions.
    """

    return [
        compute_residual(d)
        for d in dimensions
        if d.required
    ]
