# F1 Adversarial Verification Register

Generated from F1_ADVERSARIAL_VERIFICATION_MATRIX.csv.

## F1-ADV-001

**Proof burden:** F1-SAFE-CMP-003

**Attack:** Create compensation from original failure with no independent authority

**Expected:** BLOCK

**Observed:** BLOCK

**Verdict:** PASS

## F1-ADV-002

**Proof burden:** F1-SAFE-CMP-003

**Attack:** Use stale compensation authority

**Expected:** BLOCK

**Observed:** BLOCK

**Verdict:** PASS

## F1-ADV-003

**Proof burden:** F1-SAFE-CMP-003

**Attack:** Use invalid compensation scope

**Expected:** BLOCK

**Observed:** BLOCK

**Verdict:** PASS

## F1-ADV-004

**Proof burden:** F1-SAFE-CMP-005

**Attack:** Reuse e0 as compensation event identity

**Expected:** REJECT

**Observed:** REJECT

**Verdict:** PASS

## F1-ADV-005

**Proof burden:** F1-SAFE-REV-004

**Attack:** Create reversal permit from eligibility without authority

**Expected:** BLOCK

**Observed:** BLOCK

**Verdict:** PASS

## F1-ADV-006

**Proof burden:** F1-SAFE-REV-004

**Attack:** Use stale reversal authority

**Expected:** BLOCK

**Observed:** BLOCK

**Verdict:** PASS

## F1-ADV-007

**Proof burden:** F1-SAFE-REV-004

**Attack:** Use invalid reversal scope

**Expected:** BLOCK

**Observed:** BLOCK

**Verdict:** PASS

## F1-ADV-008

**Proof burden:** F1-SAFE-REV-004

**Attack:** Reuse e0 as reversal event identity

**Expected:** REJECT

**Observed:** REJECT

**Verdict:** PASS

## F1-ADV-009

**Proof burden:** CONSEQUENTIAL-BOUNDARY

**Attack:** Instantiate successful BoundaryPermit outside boundary.py

**Expected:** NO-BYPASS

**Observed:** NO-BYPASS

**Verdict:** PASS

## F1-ADV-010

**Proof burden:** EFFECT-CLASSIFIER

**Attack:** Inject economic mutation outside intended set M*

**Expected:** INDETERMINATE

**Observed:** INDETERMINATE

**Verdict:** PASS

## F1-ADV-011

**Proof burden:** EFFECT-CLASSIFIER

**Attack:** Force unresolved mutation state into NO-EFFECT

**Expected:** INDETERMINATE

**Observed:** INDETERMINATE

**Verdict:** PASS

## F1-ADV-012

**Proof burden:** EFFECT-CLASSIFIER

**Attack:** Supply conflicting occurrence and non-occurrence evidence

**Expected:** INDETERMINATE

**Observed:** INDETERMINATE

**Verdict:** PASS

## F1-ADV-013

**Proof burden:** F1-TRACE-REC-006

**Attack:** Force reconciliation to choose arbitrarily between two candidate states

**Expected:** INDETERMINATE

**Observed:** INDETERMINATE

**Verdict:** PASS

## F1-ADV-014

**Proof burden:** F1-TRACE-REC-006

**Attack:** Reconcile with missing provenance

**Expected:** FAILED

**Observed:** FAILED

**Verdict:** PASS

## F1-ADV-015

**Proof burden:** F1-TRACE-REV-006

**Attack:** Mutate returned evidence object to erase originating history

**Expected:** RETAINED-HISTORY-UNCHANGED

**Observed:** RETAINED-HISTORY-UNCHANGED

**Verdict:** PASS

## F1-ADV-016

**Proof burden:** F1-TRACE-REV-006

**Attack:** Compensation/reversal lineage removes original event e0

**Expected:** E0-PRESERVED

**Observed:** E0-PRESERVED

**Verdict:** PASS

## F1-ADV-017

**Proof burden:** F1-TRACE-CNT-007

**Attack:** Classify reconstructed history as PRESERVED

**Expected:** RECONSTRUCTED

**Observed:** RECONSTRUCTED

**Verdict:** PASS

## F1-ADV-018

**Proof burden:** F1-TRACE-CNT-007

**Attack:** Claim reconstruction without represented prior break

**Expected:** INDETERMINATE

**Observed:** INDETERMINATE

**Verdict:** PASS

## F1-ADV-019

**Proof burden:** F1-TRACE-REC-006

**Attack:** Collapse full e0 -> ec -> reconciliation -> continuity path to terminal state

**Expected:** FULL-LINEAGE-PRESERVED

**Observed:** FULL-LINEAGE-PRESERVED

**Verdict:** PASS
