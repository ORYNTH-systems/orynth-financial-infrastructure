# Financial Proof-Class Definitions

## THEOREM

A formal proposition intended to be established deductively from explicit
definitions, axioms, inherited results, and previously discharged obligations.

## LEMMA

A supporting formal result required to prove a larger theorem or safety property.

## SAFETY

Establishes that a forbidden financial execution state or transition cannot occur
under the stated assumptions.

Canonical form:

    bad_state is unreachable

or:

    forbidden_transition cannot occur

## LIVENESS

Establishes that a required permitted progression remains reachable and that the
architecture does not permanently block a valid financial execution solely because
of its governance machinery.

Canonical form:

    valid_state eventually permits required progression

subject to explicit assumptions.

## NON-EQUIVALENCE

Establishes that two concepts, states, relations, or outcomes must remain
distinguishable.

Examples:

    control != authority

    compensation != reversal

    economic equivalence != historical equivalence

## TRACEABILITY

Establishes an unbroken mapping among:

    source authority
    -> object
    -> state
    -> transition
    -> decision
    -> effect
    -> evidence
    -> reconstruction

## COUNTEREXAMPLE

Provides a mechanically or formally valid witness demonstrating that an apparently
reasonable equivalence, implication, or shortcut is false.

## RUNTIME-CONFORMANCE

Establishes that the executable reference mechanism preserves the corresponding
formal invariant under the defined runtime model.

---

## Governing Rule

No proof obligation is discharged merely because:

- code exists,
- a unit test passes,
- a scenario appears correct,
- a paper states the proposition,
- an implementation refuses execution,
- a final balance looks correct.

Each obligation must later identify its accepted evidence standard.

---

## Status Vocabulary

OPEN
PARTIAL
PROVED
REFUTED
NOT-APPLICABLE

At FIN-ARCH-06 initialization all obligations SHALL remain OPEN.
