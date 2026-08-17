# FIN-F2-09 — Claim Status Doctrine

## Allowed Status Values

PROVED

COUNTEREXAMPLE-DISCHARGED

PARTIAL

REFUTED

BLOCKED

## Required Separation

PROVED means a positive formal claim has been discharged by a valid
formal argument from the locked definitions and assumptions.

COUNTEREXAMPLE-DISCHARGED means a universal implication or semantic
collapse has been defeated by a valid counterexample.

COUNTEREXAMPLE-DISCHARGED is not equivalent to PROVED.

PARTIAL means only a proper subset of the stated obligation has been
discharged.

REFUTED means the proposed claim is false under the locked model.

BLOCKED means required premises, definitions, evidence, or consistency
conditions are insufficient for responsible discharge.

## Runtime Rule

No runtime test result may be represented as PROVED.

No proof result may be represented as REFERENCE-RUNTIME-CONFORMANT before
FIN-F2-10 / FIN-F2-11.

## Production Rule

No FIN-F2-09 result implies production readiness.
