# FIN-COMP-012 — Reversal Requirement Classifier

## Category

reversal

## Responsibility

Determine whether reversal may be required without authorizing reversal.

## Inputs

EffectClassification; SettlementState; EvidenceObject

## Outputs

ReversalRequirement

## Canonical State Ownership

Resolution requirement state

## Upstream Dependencies

Financial Infrastructure

## May Mutate State

YES

## May Create Authority

NO

## First Major Paper

F1

## Architectural Rule

This component may perform only the responsibility assigned above.

Responsibility does not imply generic financial authority.

Where consequential execution depends on current authority or admission, those upstream requirements remain independently binding.

## Implementation Status

NOT IMPLEMENTED BY FIN-ARCH-07.

Architecture definition only.
