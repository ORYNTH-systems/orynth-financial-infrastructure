# F1 Proof-Discharge Doctrine

## Purpose

FIN-F1-07 converts semantic propositions into explicit proof results.

It does not assume that every semantic requirement is already proven.

---

## Allowed Result States

PROVED

The proposition follows from the formal definitions/axioms under its stated
assumptions, with an explicit derivation.

COUNTEREXAMPLE-DISCHARGED

A universal implication or claimed equivalence is defeated by at least one valid
constructive witness.

PARTIAL

A formal result is established only under narrower assumptions than the complete
candidate claim, or the mathematical part is established while runtime
conformance remains open.

REFUTED

The proposition as written is false under the declared model.

BLOCKED

The proposition cannot currently be resolved because required assumptions,
formalization, profile semantics, or runtime evidence are absent.

---

## Evidence Types

DEFINITIONAL-DERIVATION

The result follows directly from canonical definitions.

FORMAL-DERIVATION

The result follows through an explicit finite chain of formal implications.

CONSTRUCTIVE-COUNTEREXAMPLE

A concrete witness establishes non-implication or non-equivalence.

FINITE-CASE-EXHAUSTION

A bounded finite domain is exhaustively evaluated.

TRACEABILITY-ARGUMENT

The result follows from explicit identity and lineage preservation.

RUNTIME-EVIDENCE-REQUIRED

Formal semantics establish the required behavior but executable conformance has not
yet been demonstrated.

PROFILE-ASSUMPTION-REQUIRED

The result depends on domain/profile assumptions not universally fixed by F1.

---

## Governing Rule

A candidate SHALL NOT be marked PROVED solely because:

- its statement appears in a specification,
- an invariant requires it,
- an adversarial case expects it,
- implementation is planned.

Proof result and normative requirement remain distinct.
