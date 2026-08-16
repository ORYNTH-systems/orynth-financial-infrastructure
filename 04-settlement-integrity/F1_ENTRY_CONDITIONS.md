# F1 — Entry Conditions

F1 is entered when at least one of the following conditions holds.

## EC-1 — Confirmed Partial Effect

A subset of intended economic mutation is observed.

Result:

Enter post-effect governance.

---

## EC-2 — Confirmed Completed Effect With Later Invalidity

Execution-level effect completed, but later state invalidates the assumption that completion resolved the governance problem.

Result:

Enter post-effect resolution.

---

## EC-3 — Interrupted Execution With Non-Zero Effect

Execution was interrupted after some economic mutation occurred.

Result:

Containment and effect classification required.

---

## EC-4 — Effect Indeterminate

Evidence cannot establish whether consequential mutation occurred.

Result:

Do not classify as NO_EFFECT.

Enter evidence-preserving post-effect analysis.

---

## EC-5 — Settlement Divergence

Execution outcome and settlement state diverge.

Examples:

- execution completed, settlement partial,
- settlement progressed, execution lineage incomplete,
- resource mutation exists without complete settlement classification.

Result:

Enter reconciliation path.

---

## EC-6 — Post-Execution Authority Invalidity

Authority/admissibility failure is discovered after economic effect occurred.

Result:

Prior effect remains historically real.

Separate remediation authority is required.

---

## Exclusion Condition

If the architecture can establish:

NO_EFFECT

and invalidity occurred before consequential mutation,

the case remains within inherited pre-effect block/no-effect machinery and is outside F1's primary novelty boundary.
