# F1 — Typed Residual Divergence Model

## Residual Function

For each effect dimension d_i:

rho_i : T_i x T_i -> R_i

where:

T_i = dimension value domain

R_i = residual-description domain.

R_i need not equal T_i.

---

## Quantitative Residual

Where valid:

rho_q(I,O) = I - O

Residual states include:

ZERO_RESIDUAL

POSITIVE_RESIDUAL

NEGATIVE_RESIDUAL

INDETERMINATE_RESIDUAL

---

## Relational Residual

Possible values include:

RELATION_MATCH

EXPECTED_RELATION_MISSING

UNEXPECTED_RELATION

RELATION_CONFLICT

RELATION_INDETERMINATE

---

## Discrete-State Residual

Possible values include:

STATE_MATCH

TARGET_NOT_REACHED

UNEXPECTED_STATE

INVALID_TRANSITION_RESULT

STATE_INDETERMINATE

---

## Set Residual

For intended set I and observed set O:

Missing = I \ O

Unexpected = O \ I

Residual:

rho_set(I,O) = (Missing,Unexpected)

---

## Graph Residual

For intended graph G_I and observed graph G_O:

rho_graph(G_I,G_O)
=
(
    missing_vertices,
    missing_edges,
    unexpected_vertices,
    unexpected_edges,
    conflicting_paths
)

---

## Residual Resolution

A residual is resolved only under its own typed resolution predicate.

There is no universal:

rho = 0

operator for all domains.

---

## Global Residual

Rho(I,O)
=
(rho_1,...,rho_n)

The global residual is resolved when every required dimension satisfies its domain-specific resolution predicate.

Optional dimensions may remain explicitly non-required.

---

## Information Preservation

Residual reduction must not destroy evidence of prior divergence.

The architecture records:

previous residual,
compensation event,
new residual.

It does not retain only the newest residual.
