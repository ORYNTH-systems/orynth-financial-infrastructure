# F1 Formal Result Register

Generated from F1_PROOF_DISCHARGE_REGISTRY.csv.

This register is authoritative for manuscript proof-status language.

## F1-THM-EFF-001

**Family:** EFFECT

**Class:** THEOREM

**Result:** PROVED

**Evidence type:** DEFINITIONAL-DERIVATION

**Statement:** [K=M* AND empty proper-subset M_econ proper-subset M*] implies C_F1=PARTIAL

## F1-THM-EFF-002

**Family:** EFFECT

**Class:** THEOREM

**Result:** PROVED

**Evidence type:** DEFINITIONAL-DERIVATION

**Statement:** [K=M* AND M_econ=empty] implies C_F1=NO-EFFECT

## F1-THM-EFF-003

**Family:** EFFECT

**Class:** THEOREM

**Result:** PROVED

**Evidence type:** DEFINITIONAL-DERIVATION

**Statement:** [K=M* AND M_econ=M*] implies C_F1=COMPLETED

## F1-THM-EFF-004

**Family:** EFFECT

**Class:** SAFETY

**Result:** PROVED

**Evidence type:** FORMAL-DERIVATION

**Statement:** Material incomplete knowledge prevents determinate NO-EFFECT/PARTIAL/COMPLETED classification

## F1-THM-CMP-001

**Family:** COMPENSATION

**Class:** THEOREM

**Result:** PROVED

**Evidence type:** DEFINITIONAL-DERIVATION

**Statement:** Compensation execution is distinct from originating execution

## F1-NEQ-CMP-002

**Family:** COMPENSATION

**Class:** NON-EQUIVALENCE

**Result:** COUNTEREXAMPLE-DISCHARGED

**Evidence type:** CONSTRUCTIVE-COUNTEREXAMPLE

**Statement:** Failure(e_0) does not imply Authority(e_c)

## F1-SAFE-CMP-003

**Family:** COMPENSATION

**Class:** SAFETY

**Result:** PARTIAL

**Evidence type:** RUNTIME-EVIDENCE-REQUIRED

**Statement:** Compensation cannot cross consequential boundary without independent authority/admission

## F1-NEQ-CMP-004

**Family:** COMPENSATION

**Class:** NON-EQUIVALENCE

**Result:** COUNTEREXAMPLE-DISCHARGED

**Evidence type:** CONSTRUCTIVE-COUNTEREXAMPLE

**Statement:** Economic restoration after compensation does not imply historical identity

## F1-SAFE-CMP-005

**Family:** COMPENSATION

**Class:** SAFETY

**Result:** PARTIAL

**Evidence type:** RUNTIME-EVIDENCE-REQUIRED

**Statement:** Recursive compensation requires independent admission

## F1-THM-REV-001

**Family:** REVERSAL

**Class:** THEOREM

**Result:** PROVED

**Evidence type:** DEFINITIONAL-DERIVATION

**Statement:** Reversal execution is distinct from originating execution

## F1-NEQ-REV-002

**Family:** REVERSAL

**Class:** NON-EQUIVALENCE

**Result:** COUNTEREXAMPLE-DISCHARGED

**Evidence type:** CONSTRUCTIVE-COUNTEREXAMPLE

**Statement:** Reversal eligibility does not imply reversal authority

## F1-NEQ-REV-003

**Family:** REVERSAL

**Class:** NON-EQUIVALENCE

**Result:** COUNTEREXAMPLE-DISCHARGED

**Evidence type:** CONSTRUCTIVE-COUNTEREXAMPLE

**Statement:** Technical reversibility does not imply reversal authority

## F1-SAFE-REV-004

**Family:** REVERSAL

**Class:** SAFETY

**Result:** PARTIAL

**Evidence type:** RUNTIME-EVIDENCE-REQUIRED

**Statement:** Reversal cannot cross consequential boundary without independent authority/admission

## F1-NEQ-REV-005

**Family:** REVERSAL

**Class:** NON-EQUIVALENCE

**Result:** COUNTEREXAMPLE-DISCHARGED

**Evidence type:** CONSTRUCTIVE-COUNTEREXAMPLE

**Statement:** Successful reversal does not imply historical identity

## F1-TRACE-REV-006

**Family:** REVERSAL

**Class:** TRACEABILITY

**Result:** PARTIAL

**Evidence type:** TRACEABILITY-ARGUMENT

**Statement:** Origin and reversal remain independently reconstructable

## F1-NEQ-REC-001

**Family:** RECONCILIATION

**Class:** NON-EQUIVALENCE

**Result:** COUNTEREXAMPLE-DISCHARGED

**Evidence type:** CONSTRUCTIVE-COUNTEREXAMPLE

**Statement:** Reconciled does not imply restored

## F1-NEQ-REC-002

**Family:** RECONCILIATION

**Class:** NON-EQUIVALENCE

**Result:** COUNTEREXAMPLE-DISCHARGED

**Evidence type:** CONSTRUCTIVE-COUNTEREXAMPLE

**Statement:** Reconciled does not imply continuity preserved

## F1-SAFE-REC-003

**Family:** RECONCILIATION

**Class:** SAFETY

**Result:** PROVED

**Evidence type:** FORMAL-DERIVATION

**Statement:** Insufficient evidence cannot establish a clean reconciled state

## F1-THM-REC-004

**Family:** RECONCILIATION

**Class:** THEOREM

**Result:** PROVED

**Evidence type:** DEFINITIONAL-DERIVATION

**Statement:** Unique state satisfying the reconciliation acceptance predicate is the determinate reconciled result

## F1-NEQ-REC-005

**Family:** RECONCILIATION

**Class:** NON-EQUIVALENCE

**Result:** COUNTEREXAMPLE-DISCHARGED

**Evidence type:** CONSTRUCTIVE-COUNTEREXAMPLE

**Statement:** Reconciliation failure and indeterminacy are distinct

## F1-TRACE-REC-006

**Family:** RECONCILIATION

**Class:** TRACEABILITY

**Result:** PARTIAL

**Evidence type:** TRACEABILITY-ARGUMENT

**Statement:** Reconciliation preserves complete execution lineage

## F1-NEQ-CNT-001

**Family:** CONTINUITY

**Class:** NON-EQUIVALENCE

**Result:** COUNTEREXAMPLE-DISCHARGED

**Evidence type:** CONSTRUCTIVE-COUNTEREXAMPLE

**Statement:** Economic endpoint equivalence does not imply continuity preservation

## F1-NEQ-CNT-002

**Family:** CONTINUITY

**Class:** NON-EQUIVALENCE

**Result:** COUNTEREXAMPLE-DISCHARGED

**Evidence type:** CONSTRUCTIVE-COUNTEREXAMPLE

**Statement:** Reconciled state does not imply continuity preservation

## F1-THM-CNT-003

**Family:** CONTINUITY

**Class:** THEOREM

**Result:** PROVED

**Evidence type:** FORMAL-DERIVATION

**Statement:** PRESERVED and RECONSTRUCTED are mutually exclusive for the same complete interval

## F1-SAFE-CNT-004

**Family:** CONTINUITY

**Class:** SAFETY

**Result:** PROVED

**Evidence type:** FORMAL-DERIVATION

**Statement:** A qualifying break excludes PRESERVED for the complete interval

## F1-NEQ-CNT-005

**Family:** CONTINUITY

**Class:** NON-EQUIVALENCE

**Result:** COUNTEREXAMPLE-DISCHARGED

**Evidence type:** CONSTRUCTIVE-COUNTEREXAMPLE

**Statement:** Functional recovery does not imply continuity preservation

## F1-SAFE-CNT-006

**Family:** CONTINUITY

**Class:** SAFETY

**Result:** PROVED

**Evidence type:** FORMAL-DERIVATION

**Statement:** Unknown material continuity state cannot establish PRESERVED

## F1-TRACE-CNT-007

**Family:** CONTINUITY

**Class:** TRACEABILITY

**Result:** PARTIAL

**Evidence type:** TRACEABILITY-ARGUMENT

**Statement:** RECONSTRUCTED preserves evidence of the prior continuity break
