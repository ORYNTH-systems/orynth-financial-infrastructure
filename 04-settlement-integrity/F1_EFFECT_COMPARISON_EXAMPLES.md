# F1 — Effect Comparison Examples

## Example 1 — Pure Quantitative Partiality

Intended:

cash = -100 from A
cash = +100 to B

Observed:

cash = -100 from A
cash = +60 to B

Classification:

not NO_EFFECT

not FULL_EFFECT

PARTIAL_EFFECT

subject to accounting for the unresolved 40-unit divergence.

---

## Example 2 — Party Coverage Partiality

Intended affected parties:

{A,B,C}

Observed affected parties:

{A,B}

Result:

PARTIAL_PARTY_COVERAGE

provided observed mutations otherwise correspond to intended effects.

---

## Example 3 — Partial Obligation Discharge

Intended:

obligation_1 -> DISCHARGED
obligation_2 -> DISCHARGED
obligation_3 -> DISCHARGED

Observed:

obligation_1 -> DISCHARGED
obligation_2 -> DISCHARGED
obligation_3 -> OPEN

Result:

PARTIAL_OBLIGATION_DISCHARGE

---

## Example 4 — Partial State Propagation

Intended graph:

instruction
-> internal account mutation
-> settlement ledger mutation
-> custody update
-> downstream confirmation

Observed:

instruction
-> internal account mutation
-> settlement ledger mutation

Result:

PARTIAL_STATE_PROPAGATION

---

## Example 5 — Contradictory Effect

Intended:

asset X ownership:
A -> B

Observed:

asset X ownership:
A -> C

This is not merely partial ownership transfer.

It is contradictory effect.

Global classification should ordinarily become E_MIXED or another explicit contradictory class.

---

## Example 6 — Over-Effect

Intended:

100 units transferred.

Observed:

110 units transferred.

This is not full completion.

It is OVER_EFFECT.

---

## Example 7 — Indeterminate Effect

Originating system reports execution attempt.

Remote settlement evidence is missing.

No reliable before/after resource observation exists.

Result:

E_INDETERMINATE

not:

E_NO_EFFECT.
