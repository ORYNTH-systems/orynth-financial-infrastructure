# Canonical Financial State Model

## Governing Rule

Financial execution state is not represented as a single linear lifecycle.

Execution may branch according to whether effect occurred, whether effect completed,
whether containment is required, whether compensation or reversal is admissible,
and whether finality or continuity can be established.

State identity does not itself imply admissibility.

---

## Primary Pre-Execution States

### FIN-S-PROPOSED
A financially consequential execution event has been proposed.

No authority or admissibility is implied.

### FIN-S-AUTHORIZED
An upstream authorization artifact or authority determination exists.

Prior authorization does not imply current execution admissibility.

### FIN-S-ADMITTED
Current admissibility has been established at the required execution boundary.

Admission is attempt-specific and temporally current.

### FIN-S-EXECUTING
Execution has crossed the effectuation boundary and consequential mutation may occur.

This state marks the beginning of the post-effect problem domain.

---

## Effect Outcome States

### FIN-S-NO-EFFECT
Execution produced no governed economic effect.

This includes governed pre-effect refusal and other classified zero-effect outcomes.

### FIN-S-PARTIAL
Some intended economic effect occurred, but the complete intended effect did not.

Partial effect is distinct from failure with zero effect.

### FIN-S-COMPLETED
The intended execution effect completed.

Completed does not imply final, legitimate, irreversible, or continuous.

### FIN-S-INDETERMINATE
The system cannot currently prove whether consequential effect occurred or completed.

Indeterminate is not equivalent to NO-EFFECT or PARTIAL.

---

## Post-Effect Control States

### FIN-S-CONTAINMENT-REQUIRED
Further uncontrolled effect must be prevented while state is assessed.

### FIN-S-CONTAINED
Additional uncontrolled financial mutation has been prevented or bounded.

Containment does not repair prior effect.

### FIN-S-COMPENSATION-REQUIRED
A determination exists that compensating execution may be required.

This state does not authorize compensation.

### FIN-S-COMPENSATION-PROPOSED
A distinct CompensationInstruction exists.

### FIN-S-COMPENSATION-AUTHORIZED
Compensation has upstream authority.

### FIN-S-COMPENSATION-ADMITTED
Compensation is currently admissible.

### FIN-S-COMPENSATING
A compensating execution is in progress.

### FIN-S-COMPENSATED
A compensating effect has completed.

Compensated does not mean original history has been erased or reversed.

---

## Reversal States

### FIN-S-REVERSAL-ELIGIBLE
A reversal operation is structurally possible under the applicable execution model.

Eligibility does not imply authority.

### FIN-S-REVERSAL-PROPOSED
A distinct ReversalInstruction exists.

### FIN-S-REVERSAL-AUTHORIZED
Reversal has upstream authority.

### FIN-S-REVERSAL-ADMITTED
Reversal is currently admissible.

### FIN-S-REVERSING
A reversal execution is in progress.

### FIN-S-REVERSED
A reversal effect completed.

Reversed does not mean original execution did not occur.

---

## Reconciliation States

### FIN-S-RECONCILIATION-REQUIRED
Current economic state cannot be accepted without reconciliation.

### FIN-S-RECONCILING
State, evidence, obligations, and resulting effects are being reconciled.

### FIN-S-RECONCILED
A determinate reconciled state has been established.

Reconciled does not itself establish finality or continuity.

### FIN-S-RECONCILIATION-FAILED
Reconciliation could not establish a determinate acceptable state.

---

## Finality States

### FIN-S-FINALITY-UNCLASSIFIED
Finality has not yet been determined.

### FIN-S-PROVISIONAL
The effect is recognized but remains subject to permitted later state change.

### FIN-S-FINAL
The relevant execution model classifies the state as final.

### FIN-S-REVERSIBLE
The state remains reversibly mutable under an admissible mechanism.

### FIN-S-IRREVERSIBLE
No admissible reversal mechanism exists within the modeled domain.

Important:
Final and irreversible are not automatically equivalent.

---

## Continuity States

### FIN-S-CONTINUITY-UNCLASSIFIED
Continuity has not been determined.

### FIN-S-CONTINUITY-PRESERVED
Required financial execution continuity remained intact.

### FIN-S-CONTINUITY-DEGRADED
Continuity was impaired but not wholly lost.

### FIN-S-CONTINUITY-BROKEN
Required continuity was not preserved.

### FIN-S-CONTINUITY-RECONSTRUCTED
A later state has been reconstructed under explicit reconstruction semantics.

Reconstructed continuity is not identical to uninterrupted preserved continuity.

### FIN-S-CONTINUITY-INDETERMINATE
Evidence is insufficient to classify continuity.

---

## Historical Rule

Returning balances or resources to an economically equivalent configuration does not erase prior transitions.

Economic equivalence does not imply historical-state equivalence.

---

## Separation Rules

NO-EFFECT != PARTIAL

PARTIAL != COMPLETED

COMPLETED != FINAL

FINAL != IRREVERSIBLE

COMPENSATED != REVERSED

REVERSED != ERASED

RECONCILED != RESTORED

RECONSTRUCTED != PRESERVED

FUNCTIONAL RECOVERY != CONTINUITY PRESERVATION
