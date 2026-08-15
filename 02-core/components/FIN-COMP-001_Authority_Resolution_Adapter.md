# FIN-COMP-001 — Authority Resolution Adapter

## Category

authority

## Responsibility

Resolve upstream authority references into finance-consumable authority state without creating authority.

## Inputs

AuthorityReference; DelegationReference; PrincipalId; ScopeReference

## Outputs

ResolvedAuthorityState

## Canonical State Ownership

NONE

## Upstream Dependencies

UAA

## May Mutate State

NO

## May Create Authority

NO

## First Major Paper

FOUNDATION

## Architectural Rule

This component may perform only the responsibility assigned above.

Responsibility does not imply generic financial authority.

Where consequential execution depends on current authority or admission, those upstream requirements remain independently binding.

## Implementation Status

NOT IMPLEMENTED BY FIN-ARCH-07.

Architecture definition only.
