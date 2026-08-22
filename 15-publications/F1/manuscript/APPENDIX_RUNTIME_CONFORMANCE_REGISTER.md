# F1 Reference-Runtime Conformance Register

Generated from F1_RUNTIME_PROOF_CLOSURE.csv.

These results describe the tested F1 reference runtime only.

## F1-SAFE-CMP-003

**Prior formal result:** PARTIAL

**Runtime result:** RUNTIME-CONFORMANT

**Generality:** REFERENCE-RUNTIME

**Basis:** Authority absence, stale authority, invalid scope, and permit-boundary attacks blocked

## F1-SAFE-CMP-005

**Prior formal result:** PARTIAL

**Runtime result:** RUNTIME-CONFORMANT

**Generality:** REFERENCE-RUNTIME

**Basis:** Origin event identity cannot be reused for compensation; distinct repair-event construction enforced

## F1-SAFE-REV-004

**Prior formal result:** PARTIAL

**Runtime result:** RUNTIME-CONFORMANT

**Generality:** REFERENCE-RUNTIME

**Basis:** Eligibility/reversibility do not create authority; stale and invalid-scope reversal attacks blocked

## F1-TRACE-REV-006

**Prior formal result:** PARTIAL

**Runtime result:** RUNTIME-CONFORMANT

**Generality:** REFERENCE-RUNTIME-IN-MEMORY

**Basis:** Origin and reversal/repair identities remain independently represented; returned ledger values cannot mutate retained records

## F1-TRACE-REC-006

**Prior formal result:** PARTIAL

**Runtime result:** RUNTIME-CONFORMANT

**Generality:** REFERENCE-RUNTIME-IN-MEMORY

**Basis:** Reconciliation preserves supplied execution lineage and does not overwrite prior evidence records

## F1-TRACE-CNT-007

**Prior formal result:** PARTIAL

**Runtime result:** RUNTIME-CONFORMANT

**Generality:** REFERENCE-RUNTIME

**Basis:** Reconstructed continuity requires represented violation and remains distinct from PRESERVED
