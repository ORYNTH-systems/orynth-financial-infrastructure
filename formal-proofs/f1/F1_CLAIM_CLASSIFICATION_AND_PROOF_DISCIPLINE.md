# F1 — Claim Classification and Proof Discipline

## Definitions

Definitions fix the meaning of terms.

A definition is not an empirical discovery and does not require theorem proof in the same sense as derived universal claims.

Definitions must still be internally coherent.

---

## Lemmas

Lemmas are intermediate propositions used to support later theorem construction.

They require explicit derivation.

---

## Theorems

Theorems are propositions claimed to follow from the F1 formal model under stated premises.

They require a valid proof before status may become PROVED.

---

## Non-Implication Theorems

A statement:

A does not imply B

is established by a valid countermodel satisfying:

A

and:

not B.

One valid counterexample is sufficient to defeat the universal implication:

A -> B.

---

## Safety Properties

Safety properties specify states or transitions that must not be silently collapsed.

They may be established from definitions, invariants, or transition structure.

---

## Runtime Evidence

Runtime tests can instantiate and stress formal claims.

Passing tests do not automatically prove universal theorems.

---

## Proof Lifecycle

OPEN

-> FORMALIZED

-> PROOF_CONSTRUCTED or COUNTEREXAMPLE_SUPPLIED

-> REVIEWED

-> PROVED

-> DISCHARGED

Implementation verification may occur in parallel.

---

## FIN-F1-07 Status

FIN-F1-07 formalizes the claim family and specializes proof debt.

It does not mark any theorem PROVED or DISCHARGED.
