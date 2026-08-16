# Canonical Financial Proof-Obligation Doctrine

## Purpose

This architecture distinguishes normative invariants from the burden required to
establish them.

Each invariant SHALL map to one or more explicit proof obligations.

No invariant is considered discharged until its assigned proof obligations satisfy
their required evidence standard.

---

## Canonical Mapping

Invariant
    -> Proof Obligation
        -> Formal Result
        -> Counterexample / Safety Witness where applicable
        -> Runtime Mechanism
        -> Verification Artifact
        -> Publication Claim

---

## Proof Status

OPEN

The obligation has been identified but not discharged.

PARTIAL

Some required evidence exists, but the complete burden is not satisfied.

PROVED

The complete accepted burden has been satisfied.

REFUTED

A valid counterexample or contradiction defeats the proposed result.

NOT-APPLICABLE

The obligation has been formally determined not to apply to a particular profile.
The obligation itself remains in the canonical registry.

---

## Prohibition Against Test Substitution

Passing tests may support a proof obligation but SHALL NOT automatically discharge
a theorem, lemma, non-equivalence, or general safety property.

Runtime tests establish implementation behavior only over the tested domain unless
a separate argument establishes broader completeness.

---

## Proof Independence

Where feasible:

- the mechanism enforcing an invariant,
- the mechanism verifying the invariant,
- and the evidence establishing the verification

SHALL remain separable.

Self-reported success by an executing component is insufficient proof of conformance.

---

## Future Paper Rule

Every F1-F8 manuscript SHALL identify:

1. inherited invariants,
2. newly specialized invariants,
3. relevant proof obligations,
4. discharged proof obligations,
5. still-open proof obligations,
6. runtime evidence,
7. counterexamples and limitations.

No manuscript may represent an OPEN obligation as proven.
