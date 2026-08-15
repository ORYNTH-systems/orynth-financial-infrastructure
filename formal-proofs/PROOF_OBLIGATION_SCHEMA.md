# Canonical Financial Proof-Obligation Schema

Every proof obligation SHALL contain:

- proof_obligation_id
- invariant_id
- invariant_family
- obligation_name
- formal_target
- required_premises
- counterexample_condition
- evidence_requirement
- implementation_requirement
- verification_requirement
- first_major_paper
- dependency_references
- discharge_state

---

## Formal Shape

For an invariant I and applicable subject X:

Premises(X)
AND
Applicable(I,X)
=>
InvariantSatisfied(I,X)

A valid counterexample exists when:

Premises(X)
AND
Applicable(I,X)
AND
NOT InvariantSatisfied(I,X)

---

## Discharge Rule

An obligation SHALL NOT be DISCHARGED merely because:

- a document states the invariant,
- a runtime demo succeeds,
- no counterexample has yet been observed,
- a test suite passes,
- an implementation appears conformant,
- a publication claims the property.

Discharge requires the specific evidence and verification conditions assigned to the obligation.
