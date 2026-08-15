# FIN-COMP-029 — Jurisdiction State Resolver

## Category

jurisdiction

## Responsibility

Resolve execution-relevant current jurisdiction state and applicable constraints.

## Inputs

ActorState; ResourceState; ExecutionEvent; JurisdictionReferences

## Outputs

ResolvedJurisdictionState

## Canonical State Ownership

Jurisdiction observation state

## Upstream Dependencies

Financial Infrastructure

## May Mutate State

YES

## May Create Authority

NO

## First Major Paper

F7

## Architectural Rule

This component may perform only the responsibility assigned above.

Responsibility does not imply generic financial authority.

Where consequential execution depends on current authority or admission, those upstream requirements remain independently binding.

## Implementation Status

NOT IMPLEMENTED BY FIN-ARCH-07.

Architecture definition only.
