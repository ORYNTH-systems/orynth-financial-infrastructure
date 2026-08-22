# F1 Manuscript Claim Doctrine

## Purpose

This document governs every technical claim made in the F1 manuscript.

The manuscript SHALL distinguish three independent evidentiary categories.

### FORMALLY PROVED

A proposition discharged through a definitional or formal derivation under the
declared F1 model.

The manuscript may describe such a proposition as:

- proved under the declared model,
- formally established,
- a theorem of the F1 formalization.

It SHALL NOT automatically generalize the proposition beyond the assumptions of
the F1 model.

### COUNTEREXAMPLE-DISCHARGED

A non-implication or non-equivalence closed through a constructive witness.

The manuscript may state that the universal implication or equivalence does not
hold under the F1 model.

It SHALL NOT call such a result a positive universal theorem unless a separate
positive proof exists.

### REFERENCE-RUNTIME CONFORMANT

A runtime-dependent requirement successfully tested against the ORYNTH F1
reference implementation under the defined FIN-F1-09 adversarial test surface.

The manuscript SHALL describe this as:

reference-runtime conformance

or:

observed conformance of the reference implementation.

It SHALL NOT describe this status as:

- universal implementation proof,
- production certification,
- cryptographic proof,
- institutional certification,
- regulatory certification.

## Forbidden Claim Collapse

The following claim transformations are prohibited:

REFERENCE-RUNTIME CONFORMANT -> FORMALLY PROVED

COUNTEREXAMPLE-DISCHARGED -> POSITIVE UNIVERSAL THEOREM

FORMALLY PROVED -> UNIVERSALLY TRUE OUTSIDE DECLARED ASSUMPTIONS

TEST PASS -> PRODUCTION READY

REFERENCE IMPLEMENTATION -> INSTITUTIONAL IMPLEMENTATION

RECONCILED -> RESTORED

RECONSTRUCTED -> PRESERVED

ECONOMIC EQUIVALENCE -> HISTORICAL IDENTITY
