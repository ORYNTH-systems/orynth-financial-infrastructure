# F1 Reconciliation Evidence Requirements

A conformant reconciliation record must preserve enough information to establish
why a particular current state was or was not accepted.

Minimum evidence surfaces:

1. complete known execution lineage;
2. originating event identifiers;
3. compensation event identifiers;
4. reversal event identifiers;
5. effect classifications;
6. resource-state observations;
7. obligation state;
8. counterparty/dependency state;
9. provenance of state observations;
10. conflict records;
11. unresolved-state records;
12. reconciliation decision;
13. candidate-state set where multiple states were considered;
14. reason for RECONCILED, INDETERMINATE, or FAILED classification.

Reconciliation evidence must not overwrite the evidence of the transactions that
created the current state.

A later RECONCILED result therefore appends:

reconciliation evidence

to:

execution evidence

rather than replacing it.

A current state that cannot be proven must remain unresolved.

Absence of contradiction is not sufficient proof of correctness.
