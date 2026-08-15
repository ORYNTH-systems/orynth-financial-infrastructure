# FIN-IF-021 — DistributedSettlementInterface

## Producer

FIN-COMP-023

## Consumer

Settlement execution plane

## Input Type

Composite authority + settlement + remote state

## Output Type

CoordinatedSettlementAction

## Consequential

YES

## Interface Rule

This interface transmits only the output type assigned above.

It does not implicitly create authority, broaden scope, bypass admission, or establish finality or continuity beyond the semantics of the output object.

## Implementation Status

NOT IMPLEMENTED BY FIN-ARCH-07.

Interface architecture only.
