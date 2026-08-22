# F1 Reversal Evidence Requirements

Every reversal chain must preserve:

originating execution
-> originating effect
-> reversal eligibility determination
-> reversibility determination
-> reversal proposal
-> reversal authority
-> reversal admission
-> reversal execution
-> reversal effect classification
-> resulting state
-> later reconciliation where applicable.

Required evidence properties:

1. Originating and reversal execution IDs remain distinct.

2. Eligibility determination is separately recorded from authority.

3. Reversibility determination is separately recorded from authority.

4. Reversal authority is independently attributable.

5. Reuse of an originating authorization artifact is detectable.

6. Local rollback is distinguishable from economic reversal.

7. Reversal effect uses the F1 effect-state classifier.

8. Original execution evidence is never overwritten by reversal evidence.

9. Resulting economic equivalence does not replace historical lineage.

10. Reversal chains remain reconstructable even after later compensation or
    reconciliation.

Canonical historical form:

S_0 --e_0--> S_1 --e_r--> S_2

not:

S_0 = S_2.
