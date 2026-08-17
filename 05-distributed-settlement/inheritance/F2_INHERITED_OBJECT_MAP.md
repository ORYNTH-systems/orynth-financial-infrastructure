# F2 Inherited Object Map

## Frozen F1 Inheritance

F2 inherits the following F1 concepts without semantic modification.

| F1 Object / Concept | F2 Treatment | Ownership |
|---|---|---|
| execution event | inherited | F1 |
| intended mutation set M*(e) | inherited | F1 |
| recognized economic effects M_econ(e,t) | inherited | F1 |
| effect classification | inherited | F1 |
| NO-EFFECT | inherited | F1 |
| PARTIAL | inherited | F1 |
| COMPLETED | inherited | F1 |
| INDETERMINATE | inherited | F1 |
| CompensationProposal | inherited | F1 |
| compensation authority rule | inherited | F1 |
| ReversalProposal | inherited | F1 |
| reversal authority rule | inherited | F1 |
| reconciliation operator | inherited | F1 |
| RECONCILED | inherited | F1 |
| RECONCILIATION-INDETERMINATE | inherited | F1 |
| RECONCILIATION-FAILED | inherited | F1 |
| continuity classifier | inherited | F1 |
| PRESERVED | inherited | F1 |
| DEGRADED | inherited | F1 |
| BROKEN | inherited | F1 |
| RECONSTRUCTED | inherited | F1 |
| continuity INDETERMINATE | inherited | F1 |
| evidence preservation | inherited | F1 |
| historical persistence | inherited | F1 |
| economic equivalence != historical identity | inherited invariant | F1 |
| repair authority independent of failure | inherited invariant | F1 |

## F2 Specialization Rule

F2 MAY introduce distributed structures around these objects.

Examples:

- distributed execution events
- participant-specific observations
- multiparty authority sets
- consensus evidence
- commitment sets
- distributed occurrence evidence
- finality classifications

F2 SHALL NOT redefine the F1 objects themselves.

## Dependency Direction

F2 -> F1

F1 -/-> F2

F1 remains independently meaningful without distributed settlement.

F2 depends on F1 whenever distributed execution produces consequential
financial effects.
