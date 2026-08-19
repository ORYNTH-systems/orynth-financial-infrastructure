# FIN-F4-02 — Canonical Object / Type Discovery and Freeze

Status: COMPLETE — PASS

## Verified base

- branch: master
- HEAD: 5866e0551e15fd2ebd12a04183db3be8ae032764
- origin/master: 5866e0551e15fd2ebd12a04183db3be8ae032764
- inherited boundary: FIN-F4-01B
- working family: Ledger-State Finality, Record Integrity, and Reopenable Financial State

## Scope

This pass freezes the minimum canonical F4 object/type vocabulary supported by repository evidence.

It does not freeze:

- state values
- transition functions
- decision functions
- admissibility conditions
- invariant numbering
- proof-obligation numbering
- runtime implementation
- test counts
- manuscript structure
- publication title

## Canonical F4 object registry

### F4-O-001 — Ledger-State Representation

**Ledger-State Representation**

A typed representation of financial state recorded or represented within a ledger or record system.

It is representational rather than constitutive of authority.

A ledger-state representation may accurately, inaccurately, incompletely, historically, or contradictorily represent an underlying financial state.

Evidence hits observed in this pass: 41

### F4-O-002 — Committed Financial Record

**Committed Financial Record**

A record-state object whose representation has crossed the applicable commitment boundary of the record system.

Commitment identifies persistence or accepted record placement under the applicable record semantics.

Commitment does not by itself establish financial finality, authority, irreversibility, or historical identity.

Evidence hits observed in this pass: 2

### F4-O-003 — Finality Representation

**Finality Representation**

A ledger or record representation asserting, recording, or preserving the finality classification of a financial state.

The representation of finality is distinct from the conditions that make the underlying financial state final.

Evidence hits observed in this pass: 1

### F4-O-004 — Historical Record State

**Historical Record State**

A typed historical representation preserving the existence and identity of an earlier record state.

Historical persistence does not imply that the state remains currently operative, admissible, authoritative, or unreopened.

Evidence hits observed in this pass: 115

### F4-O-005 — Record Reopening

**Record Reopening**

A typed reopening object representing that a previously committed or finality-associated record state has entered a permitted or required reconsideration path.

Reopening does not erase the historical existence of the earlier record state.

Evidence hits observed in this pass: 93

### F4-O-006 — Ledger Contradiction

**Ledger Contradiction**

A typed contradiction object identifying incompatible record-state assertions, representations, histories, or commitments.

Contradiction is evidence of unresolved record integrity and does not by itself determine which competing state is authoritative.

Evidence hits observed in this pass: 1

### F4-O-007 — Record-State Reconstruction

**Record-State Reconstruction**

A typed reconstruction object representing the restoration or derivation of record state from admissible evidence after loss, contradiction, corruption, reopening, or incomplete persistence.

Reconstruction does not automatically restore historical identity or continuity.

Evidence hits observed in this pass: 2

### F4-O-008 — Ledger/Finality Conflict

**Ledger/Finality Conflict**

A typed conflict object representing disagreement between ledger or record state and the applicable financial finality classification.

The object preserves the distinction between record representation and underlying financial finality.

Evidence hits observed in this pass: 40

### F4-O-009 — Ledger/Custody Representation

**Ledger/Custody Representation**

A typed record representation of custody state, custody transfer, or custody-related financial position.

Recorded custody is evidence of custody state but is not itself custody authority.

Evidence hits observed in this pass: 5

### F4-O-010 — Record-State Continuity Classification

**Record-State Continuity Classification**

A typed classification of whether a record-state history preserves, disrupts, reconstructs, or fails to establish continuity across relevant transitions.

Continuity classification is distinct from functional restoration and record equality.

Evidence hits observed in this pass: 138


## Frozen type distinctions

- financial state != ledger-state representation
- ledger-state representation != authority
- record commitment != finality
- record persistence != irreversibility
- record equality != historical identity
- recorded custody != custody authority
- record reopening != historical erasure
- record reconstruction != continuity preservation
- record contradiction != historical non-occurrence
- ledger evidence != authority to establish financial truth

These distinctions are semantic constraints only at this stage.

They MUST NOT yet be treated as discharged invariants or proof results.

## Core F4 type boundary

F4 inherits:

**final financial state != ledger representation of final financial state**

The canonical object model therefore separates:

1. underlying financial state;
2. ledger or record representation;
3. commitment of that representation;
4. representation of finality;
5. historical persistence;
6. reopening;
7. contradiction;
8. reconstruction;
9. custody representation;
10. continuity classification.

## Cross-family inheritance

F4 inherits from F3 but does not redefine:

- financial obligation
- obligation performance
- obligation residual
- custody state
- custody authority
- custody transfer
- finality requirement set
- finality evidence set
- finality classification
- consequential closure
- reopenability state
- finality conflict
- post-finality contradiction
- closure witness

F4 objects represent or reason about record-state consequences surrounding those F3 objects.

F4 MUST NOT collapse record representation into the underlying F3 financial-state determination.

## Evidence appendix

- F4-O-001 | 02-core/components/FIN-COMP-022_Remote_State_Monitor.md:9 | term=ledger state | Observe execution-relevant remote counterparty institution or ledger state.
- F4-O-001 | 02-core/invariants/FIN-DST_INVARIANTS.md:61 | term=ledger state | **Normative rule:** Execution-relevant remote counterparty or ledger state SHALL be incorporated where its change can alter admissibility.
- F4-O-001 | 02-core/types/CANONICAL_FINANCIAL_TYPE_SYSTEM.md:52 | term=ledger state | Identifier for a ledger state domain.
- F4-O-001 | 03-registries/INTERFACE_REGISTRY.csv:20 | term=ledger state | "FI-IF-019","MapLedgerAdmission","FI-LED-001","ledger transaction + ledger state","financial governance admission request"
- F4-O-001 | 03-registries/INVARIANT_REGISTRY.csv:34 | term=ledger state | "FIN-FIN-001","FINALITY","Finality Requires Explicit Classification","Financial finality SHALL be explicitly classified rather than inferred from completion.","Settlement and ledger state","FIN-ARCH-04","F3"
- F4-O-001 | 03-registries/PROOF_OBLIGATION_REGISTRY.csv:34 | term=ledger state | "FIN-PO-033","FIN-FIN-001","THEOREM","Finality Requires Explicit Classification","Establish invariant FIN-FIN-001 'Finality Requires Explicit Classification' under its stated applicability conditions and inherited architectural assumptions; demonstrate that the forbidden violating state or semantic collapse cannot be accepted as conformant.","Settlement and ledger state","FIN-ARCH-04","F3","OPEN","","","",""
- F4-O-001 | 05-distributed-settlement/formal/F2_DISTRIBUTED_ECONOMIC_STATE_CONTINUITY.md:56 | term=ledger state | - ledger state
- F4-O-001 | 06-f3-discovery/formal/F3_FINALITY_ELIGIBILITY_SEMANTICS.md:45 | term=ledger state | - ledger state;
- F4-O-001 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:620 | term=ledger state | - 03-registries/INTERFACE_REGISTRY.csv:20 | pattern=ledger | "FI-IF-019","MapLedgerAdmission","FI-LED-001","ledger transaction + ledger state","financial governance admission request"
- F4-O-001 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:621 | term=ledger state | - 03-registries/INTERFACE_REGISTRY.csv:20 | pattern=ledger state | "FI-IF-019","MapLedgerAdmission","FI-LED-001","ledger transaction + ledger state","financial governance admission request"
- F4-O-001 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:636 | term=ledger state | - 03-registries/INVARIANT_REGISTRY.csv:34 | pattern=finality | "FIN-FIN-001","FINALITY","Finality Requires Explicit Classification","Financial finality SHALL be explicitly classified rather than inferred from completion.","Settlement and ledger state","FIN-ARCH-04","F3"
- F4-O-001 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:637 | term=ledger state | - 03-registries/INVARIANT_REGISTRY.csv:34 | pattern=ledger | "FIN-FIN-001","FINALITY","Finality Requires Explicit Classification","Financial finality SHALL be explicitly classified rather than inferred from completion.","Settlement and ledger state","FIN-ARCH-04","F3"
- F4-O-001 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:638 | term=ledger state | - 03-registries/INVARIANT_REGISTRY.csv:34 | pattern=ledger state | "FIN-FIN-001","FINALITY","Finality Requires Explicit Classification","Financial finality SHALL be explicitly classified rather than inferred from completion.","Settlement and ledger state","FIN-ARCH-04","F3"
- F4-O-001 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:670 | term=ledger state | - 03-registries/PROOF_OBLIGATION_REGISTRY.csv:34 | pattern=finality | "FIN-PO-033","FIN-FIN-001","THEOREM","Finality Requires Explicit Classification","Establish invariant FIN-FIN-001 'Finality Requires Explicit Classification' under its stated applicability conditions and inherited architectural assumptions; demonstrate that the forbidden violating state or semantic collapse cannot be accepted as conformant.","Settlement and ledger state","FIN-ARCH-04","F3","OPEN","","","",""
- F4-O-001 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:671 | term=ledger state | - 03-registries/PROOF_OBLIGATION_REGISTRY.csv:34 | pattern=ledger | "FIN-PO-033","FIN-FIN-001","THEOREM","Finality Requires Explicit Classification","Establish invariant FIN-FIN-001 'Finality Requires Explicit Classification' under its stated applicability conditions and inherited architectural assumptions; demonstrate that the forbidden violating state or semantic collapse cannot be accepted as conformant.","Settlement and ledger state","FIN-ARCH-04","F3","OPEN","","","",""
- F4-O-001 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:672 | term=ledger state | - 03-registries/PROOF_OBLIGATION_REGISTRY.csv:34 | pattern=ledger state | "FIN-PO-033","FIN-FIN-001","THEOREM","Finality Requires Explicit Classification","Establish invariant FIN-FIN-001 'Finality Requires Explicit Classification' under its stated applicability conditions and inherited architectural assumptions; demonstrate that the forbidden violating state or semantic collapse cannot be accepted as conformant.","Settlement and ledger state","FIN-ARCH-04","F3","OPEN","","","",""
- F4-O-001 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1204 | term=ledger state | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:858 | pattern=ledger | - ledger state;
- F4-O-001 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1205 | term=ledger state | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:858 | pattern=ledger state | - ledger state;
- F4-O-001 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1452 | term=ledger state | - formal-proofs/FIN-DST_PROOF_OBLIGATIONS.md:17 | pattern=ledger | **Required premises:** Participant identities; authority references; remote state; consensus or ledger state; applicable execution boundaries.
- F4-O-001 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1453 | term=ledger state | - formal-proofs/FIN-DST_PROOF_OBLIGATIONS.md:17 | pattern=ledger state | **Required premises:** Participant identities; authority references; remote state; consensus or ledger state; applicable execution boundaries.
- F4-O-001 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1460 | term=ledger state | - formal-proofs/FIN-DST_PROOF_OBLIGATIONS.md:41 | pattern=ledger | **Required premises:** Participant identities; authority references; remote state; consensus or ledger state; applicable execution boundaries.
- F4-O-001 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1461 | term=ledger state | - formal-proofs/FIN-DST_PROOF_OBLIGATIONS.md:41 | pattern=ledger state | **Required premises:** Participant identities; authority references; remote state; consensus or ledger state; applicable execution boundaries.
- F4-O-001 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1467 | term=ledger state | - formal-proofs/FIN-DST_PROOF_OBLIGATIONS.md:65 | pattern=ledger | **Required premises:** Participant identities; authority references; remote state; consensus or ledger state; applicable execution boundaries.
- F4-O-001 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1468 | term=ledger state | - formal-proofs/FIN-DST_PROOF_OBLIGATIONS.md:65 | pattern=ledger state | **Required premises:** Participant identities; authority references; remote state; consensus or ledger state; applicable execution boundaries.
- F4-O-001 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1473 | term=ledger state | - formal-proofs/FIN-DST_PROOF_OBLIGATIONS.md:89 | pattern=ledger | **Required premises:** Participant identities; authority references; remote state; consensus or ledger state; applicable execution boundaries.
- F4-O-001 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1474 | term=ledger state | - formal-proofs/FIN-DST_PROOF_OBLIGATIONS.md:89 | pattern=ledger state | **Required premises:** Participant identities; authority references; remote state; consensus or ledger state; applicable execution boundaries.
- F4-O-001 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1481 | term=ledger state | - formal-proofs/FIN-DST_PROOF_OBLIGATIONS.md:113 | pattern=ledger | **Required premises:** Participant identities; authority references; remote state; consensus or ledger state; applicable execution boundaries.
- F4-O-001 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1482 | term=ledger state | - formal-proofs/FIN-DST_PROOF_OBLIGATIONS.md:113 | pattern=ledger state | **Required premises:** Participant identities; authority references; remote state; consensus or ledger state; applicable execution boundaries.
- F4-O-001 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:14 | term=ledger-state | **Ledger-State Finality, Record Integrity, and Reopenable Financial State**
- F4-O-001 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:22 | term=ledger-state | The supported problem is not merely whether an obligation is final. It is whether a ledger-state representation may validly encode, preserve, reopen, contradict, or reconstruct a financial state without collapsing record state into authority, historical identity, irreversibility, or continuity preservation.
- F4-O-001 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:22 | term=state representation | The supported problem is not merely whether an obligation is final. It is whether a ledger-state representation may validly encode, preserve, reopen, contradict, or reconstruct a financial state without collapsing record state into authority, historical identity, irreversibility, or continuity preservation.
- F4-O-001 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:41 | term=ledger representation | **final financial state != ledger representation of final financial state**
- F4-O-001 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:51 | term=state representation | - state representation != valid transition
- F4-O-001 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:855 | term=ledger-state | - ledger-state representation
- F4-O-001 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:855 | term=state representation | - ledger-state representation
- F4-O-001 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:858 | term=ledger state | - ledger state;
- F4-O-001 | formal-proofs/FIN-DST_PROOF_OBLIGATIONS.md:17 | term=ledger state | **Required premises:** Participant identities; authority references; remote state; consensus or ledger state; applicable execution boundaries.
- F4-O-001 | formal-proofs/FIN-DST_PROOF_OBLIGATIONS.md:41 | term=ledger state | **Required premises:** Participant identities; authority references; remote state; consensus or ledger state; applicable execution boundaries.
- F4-O-001 | formal-proofs/FIN-DST_PROOF_OBLIGATIONS.md:65 | term=ledger state | **Required premises:** Participant identities; authority references; remote state; consensus or ledger state; applicable execution boundaries.
- F4-O-001 | formal-proofs/FIN-DST_PROOF_OBLIGATIONS.md:89 | term=ledger state | **Required premises:** Participant identities; authority references; remote state; consensus or ledger state; applicable execution boundaries.
- F4-O-001 | formal-proofs/FIN-DST_PROOF_OBLIGATIONS.md:113 | term=ledger state | **Required premises:** Participant identities; authority references; remote state; consensus or ledger state; applicable execution boundaries.
- F4-O-002 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:48 | term=record commitment | - record commitment != irreversibility
- F4-O-002 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:856 | term=committed financial | - committed financial record state
- F4-O-003 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:857 | term=finality representation | - finality representation
- F4-O-004 | 02-core/invariants/FIN-REC_INVARIANTS.md:33 | term=historical state | **Normative rule:** Reconstructed historical state SHALL NOT be classified as restored continuity merely because historical state can be reconstructed.
- F4-O-004 | 02-core/invariants/FIN-REV_INVARIANTS.md:63 | term=historical state | **Applies to:** Historical state
- F4-O-004 | 02-core/OBJECT_NON_EQUIVALENCE_RULES.md:25 | term=historical state | Economic Balance Equivalence != Historical State Equivalence
- F4-O-004 | 02-core/states/CONTINUITY_CLASSIFICATION_MODEL.md:42 | term=historical state | Historical state has been reconstructed from surviving evidence.
- F4-O-004 | 02-core/states/CONTINUITY_CLASSIFICATION_MODEL.md:58 | term=historical record | Observed history has been reconciled sufficiently to establish a coherent historical record.
- F4-O-004 | 02-core/states/FINANCIAL_STATE_MODEL.md:146 | term=historical state | REVERSED does not erase historical state or evidence.
- F4-O-004 | 02-core/transitions/CANONICAL_FINANCIAL_TRANSITION_ALGEBRA.md:153 | term=historical state | BALANCE RESTORED -> HISTORICAL STATE RESTORED
- F4-O-004 | 02-core/transitions/FINANCIAL_TRANSITION_ALGEBRA.md:156 | term=historical state | Historical states SHALL NOT be overwritten merely because a later lifecycle exists.
- F4-O-004 | 03-registries/F1_COMPENSATION_RELATION_REGISTRY.csv:8 | term=historical identity | "F1-CMP-R007","Economic equivalence != historical identity","YES"
- F4-O-004 | 03-registries/F1_CONTINUITY_RELATION_REGISTRY.csv:8 | term=historical identity | "F1-CNT-R007","Continuity Preservation != Historical Identity","YES"
- F4-O-004 | 03-registries/F1_MANUSCRIPT_CLAIM_REGISTRY.csv:7 | term=historical identity | "F1-MC-006","Economic restoration after compensation does not imply historical identity","COUNTEREXAMPLE-DISCHARGED","F1-NEQ-CMP-004","F1_PROOF_DISCHARGE_REGISTRY.csv"
- F4-O-004 | 03-registries/F1_NOVELTY_INHERITANCE_MATRIX.csv:10 | term=historical identity | "Economic equivalence vs historical identity","NEW","F1","FORMALIZE/PROVE"
- F4-O-004 | 03-registries/F1_PROOF_DISCHARGE_REGISTRY.csv:9 | term=historical identity | "F1-NEQ-CMP-004","COMPENSATION","NON-EQUIVALENCE","Economic restoration after compensation does not imply historical identity","COUNTEREXAMPLE-DISCHARGED","CONSTRUCTIVE-COUNTEREXAMPLE","04-settlement-integrity/proofs/F1_COMPENSATION_PROOFS.md","NO"
- F4-O-004 | 03-registries/F1_PROOF_DISCHARGE_REGISTRY.csv:15 | term=historical identity | "F1-NEQ-REV-005","REVERSAL","NON-EQUIVALENCE","Successful reversal does not imply historical identity","COUNTEREXAMPLE-DISCHARGED","CONSTRUCTIVE-COUNTEREXAMPLE","04-settlement-integrity/proofs/F1_REVERSAL_PROOFS.md","NO"
- F4-O-004 | 03-registries/F1_RECONCILIATION_RELATION_REGISTRY.csv:8 | term=historical identity | "F1-REC-R007","Economic Equivalence != Historical Identity","YES"
- F4-O-004 | 03-registries/F1_REVERSAL_RELATION_REGISTRY.csv:8 | term=historical identity | "F1-REV-R007","Successful Reversal != Historical Identity","YES"
- F4-O-004 | 03-registries/F1_REVERSAL_RELATION_REGISTRY.csv:9 | term=historical identity | "F1-REV-R008","Economic Equivalence != Historical Identity","YES"
- F4-O-004 | 03-registries/F2_07_INVARIANT_REGISTER.csv:21 | term=historical identity | "F2-REC-008","RECONCILIATION","Economic branch convergence does not imply historical identity.","LOCKED"
- F4-O-004 | 03-registries/F2_PROOF_DISCHARGE_REGISTRY.csv:15 | term=historical identity | "F2-NI-011","Economic endpoint equivalence does not imply historical identity.","NON-IMPLICATION","COUNTEREXAMPLE-DISCHARGED","CE-011"
- F4-O-004 | 03-registries/F3_INVARIANT_REGISTER.csv:11 | term=historical identity | F3-INV-010,FIN-FIN,Balance equality cannot establish historical identity,OPEN
- F4-O-004 | 03-registries/F3_INVARIANT_REGISTER.csv:14 | term=historical identity | F3-INV-013,FIN-FIN,Finality does not imply historical identity,OPEN
- F4-O-004 | 03-registries/F3_NON_EQUIVALENCE_REGISTRY.csv:11 | term=historical identity | F3-NE-010,balance equality,historical identity,REQUIRED
- F4-O-004 | 03-registries/F3_NON_EQUIVALENCE_REGISTRY.csv:14 | term=historical identity | F3-NE-013,finality,historical identity,REQUIRED
- F4-O-004 | 03-registries/F3_PROOF_OBLIGATION_REGISTRY.csv:13 | term=historical identity | F3-PO-012,NON-EQUIV,Prove finality is insufficient for historical identity,OPEN
- F4-O-004 | 05-distributed-settlement/formal/F2_DISTRIBUTED_ECONOMIC_STATE_CONTINUITY.md:29 | term=historical identity | Economic equivalence != historical identity.
- F4-O-004 | 05-distributed-settlement/formal/F2_DISTRIBUTED_ECONOMIC_STATE_CONTINUITY.md:166 | term=historical identity | - no material historical identity discontinuity occurred
- F4-O-004 | 05-distributed-settlement/formal/F2_DISTRIBUTED_ECONOMIC_STATE_CONTINUITY.md:206 | term=historical identity | - material historical identity break
- F4-O-004 | 05-distributed-settlement/formal/F2_DISTRIBUTED_ECONOMIC_STATE_CONTINUITY.md:218 | term=historical state | historical state and evidence were later rebuilt to establish a usable
- F4-O-004 | 05-distributed-settlement/formal/F2_DISTRIBUTED_ECONOMIC_STATE_CONTINUITY.md:263 | term=historical state | Continuity concerns historical state lineage.
- F4-O-004 | 05-distributed-settlement/formal/F2_FORK_DIVERGENCE_SEMANTICS.md:147 | term=historical identity | this does not establish historical identity.
- F4-O-004 | 05-distributed-settlement/inheritance/F2_INHERITED_OBJECT_MAP.md:33 | term=historical identity | | economic equivalence != historical identity | inherited invariant | F1 |
- F4-O-004 | 05-distributed-settlement/proofs/F2_COUNTEREXAMPLE_DISCHARGE.md:182 | term=historical state | Historical state reconstructed
- F4-O-004 | 05-distributed-settlement/proofs/F2_COUNTEREXAMPLE_DISCHARGE.md:220 | term=historical identity | ## CE-011 — Endpoint Equivalence != Historical Identity
- F4-O-004 | 05-distributed-settlement/proofs/F2_FORMAL_PROOF_SUMMARY.md:50 | term=historical identity | - endpoint economic equivalence does not establish historical identity
- F4-O-004 | 06-f3-discovery/FIN_F3_01B_PROBLEM_BOUNDARY.md:41 | term=historical identity | != historical identity
- F4-O-004 | 06-f3-discovery/FIN_F3_01B_PROBLEM_BOUNDARY.md:87 | term=historical identity | - historical identity distinctions.
- F4-O-004 | 06-f3-discovery/FIN_F3_01B_PROBLEM_BOUNDARY.md:99 | term=historical identity | economic equivalence == historical identity
- F4-O-004 | 06-f3-discovery/FIN_F3_01B_PROBLEM_BOUNDARY.md:182 | term=historical identity | finality != historical identity
- F4-O-004 | 06-f3-discovery/formal/F3_NON_EQUIVALENCE_ALGEBRA.md:25 | term=historical identity | balance equality != historical identity
- F4-O-004 | 06-f3-discovery/formal/F3_NON_EQUIVALENCE_ALGEBRA.md:31 | term=historical identity | finality != historical identity
- F4-O-004 | 06-f3-discovery/proofs/F3_COUNTEREXAMPLE_DISCHARGE.md:181 | term=historical identity | ## CE-12 — Final But Historical Identity Different
- F4-O-004 | 06-f3-discovery/proofs/F3_COUNTEREXAMPLE_DISCHARGE.md:190 | term=historical identity | finality != historical identity
- F4-O-004 | 06-f3-discovery/proofs/F3_POSITIVE_PROOF_DISCHARGE.md:123 | term=historical record | from historical record destruction.
- F4-O-004 | 06-f3-discovery/proofs/F3_POSITIVE_PROOF_DISCHARGE.md:141 | term=historical state | preserves prior classification as historical state.
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:130 | term=historical identity | - 03-registries/F1_COMPENSATION_RELATION_REGISTRY.csv:8 | pattern=historical identity | "F1-CMP-R007","Economic equivalence != historical identity","YES"
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:168 | term=historical identity | - 03-registries/F1_CONTINUITY_RELATION_REGISTRY.csv:8 | pattern=continuity | "F1-CNT-R007","Continuity Preservation != Historical Identity","YES"
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:169 | term=historical identity | - 03-registries/F1_CONTINUITY_RELATION_REGISTRY.csv:8 | pattern=historical identity | "F1-CNT-R007","Continuity Preservation != Historical Identity","YES"
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:191 | term=historical identity | - 03-registries/F1_MANUSCRIPT_CLAIM_REGISTRY.csv:7 | pattern=historical identity | "F1-MC-006","Economic restoration after compensation does not imply historical identity","COUNTEREXAMPLE-DISCHARGED","F1-NEQ-CMP-004","F1_PROOF_DISCHARGE_REGISTRY.csv"
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:201 | term=historical identity | - 03-registries/F1_NOVELTY_INHERITANCE_MATRIX.csv:10 | pattern=historical identity | "Economic equivalence vs historical identity","NEW","F1","FORMALIZE/PROVE"
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:208 | term=historical identity | - 03-registries/F1_PROOF_DISCHARGE_REGISTRY.csv:9 | pattern=historical identity | "F1-NEQ-CMP-004","COMPENSATION","NON-EQUIVALENCE","Economic restoration after compensation does not imply historical identity","COUNTEREXAMPLE-DISCHARGED","CONSTRUCTIVE-COUNTEREXAMPLE","04-settlement-integrity/proofs/F1_COMPENSATION_PROOFS.md","NO"
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:209 | term=historical identity | - 03-registries/F1_PROOF_DISCHARGE_REGISTRY.csv:15 | pattern=historical identity | "F1-NEQ-REV-005","REVERSAL","NON-EQUIVALENCE","Successful reversal does not imply historical identity","COUNTEREXAMPLE-DISCHARGED","CONSTRUCTIVE-COUNTEREXAMPLE","04-settlement-integrity/proofs/F1_REVERSAL_PROOFS.md","NO"
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:228 | term=historical identity | - 03-registries/F1_RECONCILIATION_RELATION_REGISTRY.csv:8 | pattern=historical identity | "F1-REC-R007","Economic Equivalence != Historical Identity","YES"
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:247 | term=historical identity | - 03-registries/F1_REVERSAL_RELATION_REGISTRY.csv:8 | pattern=historical identity | "F1-REV-R007","Successful Reversal != Historical Identity","YES"
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:248 | term=historical identity | - 03-registries/F1_REVERSAL_RELATION_REGISTRY.csv:9 | pattern=historical identity | "F1-REV-R008","Economic Equivalence != Historical Identity","YES"
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:311 | term=historical identity | - 03-registries/F2_07_INVARIANT_REGISTER.csv:21 | pattern=historical identity | "F2-REC-008","RECONCILIATION","Economic branch convergence does not imply historical identity.","LOCKED"
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:402 | term=historical identity | - 03-registries/F2_PROOF_DISCHARGE_REGISTRY.csv:15 | pattern=historical identity | "F2-NI-011","Economic endpoint equivalence does not imply historical identity.","NON-IMPLICATION","COUNTEREXAMPLE-DISCHARGED","CE-011"
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:448 | term=historical identity | - 03-registries/F3_INVARIANT_REGISTER.csv:11 | pattern=historical identity | F3-INV-010,FIN-FIN,Balance equality cannot establish historical identity,OPEN
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:453 | term=historical identity | - 03-registries/F3_INVARIANT_REGISTER.csv:14 | pattern=finality | F3-INV-013,FIN-FIN,Finality does not imply historical identity,OPEN
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:454 | term=historical identity | - 03-registries/F3_INVARIANT_REGISTER.csv:14 | pattern=historical identity | F3-INV-013,FIN-FIN,Finality does not imply historical identity,OPEN
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:488 | term=historical identity | - 03-registries/F3_NON_EQUIVALENCE_REGISTRY.csv:11 | pattern=historical identity | F3-NE-010,balance equality,historical identity,REQUIRED
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:493 | term=historical identity | - 03-registries/F3_NON_EQUIVALENCE_REGISTRY.csv:14 | pattern=finality | F3-NE-013,finality,historical identity,REQUIRED
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:494 | term=historical identity | - 03-registries/F3_NON_EQUIVALENCE_REGISTRY.csv:14 | pattern=historical identity | F3-NE-013,finality,historical identity,REQUIRED
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:533 | term=historical identity | - 03-registries/F3_PROOF_OBLIGATION_REGISTRY.csv:13 | pattern=finality | F3-PO-012,NON-EQUIV,Prove finality is insufficient for historical identity,OPEN
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:534 | term=historical identity | - 03-registries/F3_PROOF_OBLIGATION_REGISTRY.csv:13 | pattern=historical identity | F3-PO-012,NON-EQUIV,Prove finality is insufficient for historical identity,OPEN
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:718 | term=historical identity | - 15-publications/F1/manuscript/APPENDIX_FORMAL_RESULT_REGISTER.md:101 | pattern=historical identity | **Statement:** Economic restoration after compensation does not imply historical identity
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:719 | term=historical identity | - 15-publications/F1/manuscript/APPENDIX_FORMAL_RESULT_REGISTER.md:173 | pattern=historical identity | **Statement:** Successful reversal does not imply historical identity
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:740 | term=historical identity | - 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:86 | pattern=historical identity | - economic equivalence is not historical identity;
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:745 | term=historical identity | - 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:352 | pattern=historical identity | It does not establish historical identity because the history of S_2 includes the
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:760 | term=historical identity | - 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:655 | pattern=historical identity | ## 9.4 Economic Equivalence and Historical Identity
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:776 | term=historical identity | - 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:826 | pattern=historical identity | - that compensation restores historical identity;
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:788 | term=historical identity | - 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:956 | pattern=historical identity | historical identity.
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:793 | term=historical identity | - 15-publications/F1/manuscript/F1_MANUSCRIPT_CLAIM_DOCTRINE.md:72 | pattern=historical identity | ECONOMIC EQUIVALENCE -> HISTORICAL IDENTITY
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:808 | term=historical identity | - 15-publications/F2/manuscript/F2_CANONICAL_MANUSCRIPT.md:108 | pattern=historical identity | - historical identity,
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:814 | term=historical identity | - 15-publications/F2/manuscript/F2_CANONICAL_MANUSCRIPT.md:127 | pattern=historical identity | **economic equivalence != historical identity**
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:888 | term=historical identity | - 15-publications/F2/manuscript/F2_CANONICAL_MANUSCRIPT.md:1133 | pattern=historical identity | Economic Equivalence != Historical Identity
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:914 | term=historical identity | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:51 | pattern=historical identity | != historical identity
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:939 | term=historical identity | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:97 | pattern=historical identity | - historical identity distinctions.
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:940 | term=historical identity | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:109 | pattern=historical identity | economic equivalence == historical identity
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:973 | term=historical identity | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:192 | pattern=finality | finality != historical identity
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:974 | term=historical identity | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:192 | pattern=historical identity | finality != historical identity
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1137 | term=historical identity | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:627 | pattern=historical identity | balance equality != historical identity
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1142 | term=historical identity | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:633 | pattern=finality | finality != historical identity
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1143 | term=historical identity | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:633 | pattern=historical identity | finality != historical identity
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1331 | term=historical identity | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1388 | pattern=historical identity | ## CE-12 — Final But Historical Identity Different
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1332 | term=historical identity | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1397 | pattern=finality | finality != historical identity
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1333 | term=historical identity | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1397 | pattern=historical identity | finality != historical identity
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1351 | term=historical identity | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1475 | pattern=finality | finality != historical identity
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1352 | term=historical identity | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1475 | pattern=historical identity | finality != historical identity
- F4-O-004 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:2032 | term=historical identity | - finality != historical identity
- F4-O-004 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:22 | term=historical identity | The supported problem is not merely whether an obligation is final. It is whether a ledger-state representation may validly encode, preserve, reopen, contradict, or reconstruct a financial state without collapsing record state into authority, historical identity, irreversibility, or continuity preservation.
- F4-O-004 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:35 | term=historical identity | - historical identity
- F4-O-004 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:47 | term=historical identity | - ledger equality != historical identity
- F4-O-004 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:858 | term=historical record | - historical record state
- F4-O-004 | 15-publications/F1/manuscript/APPENDIX_FORMAL_RESULT_REGISTER.md:101 | term=historical identity | **Statement:** Economic restoration after compensation does not imply historical identity
- F4-O-004 | 15-publications/F1/manuscript/APPENDIX_FORMAL_RESULT_REGISTER.md:173 | term=historical identity | **Statement:** Successful reversal does not imply historical identity
- F4-O-004 | 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:86 | term=historical identity | - economic equivalence is not historical identity;
- F4-O-004 | 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:352 | term=historical identity | It does not establish historical identity because the history of S_2 includes the
- F4-O-004 | 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:655 | term=historical identity | ## 9.4 Economic Equivalence and Historical Identity
- F4-O-004 | 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:826 | term=historical identity | - that compensation restores historical identity;
- F4-O-004 | 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:956 | term=historical identity | historical identity.
- F4-O-004 | 15-publications/F1/manuscript/F1_MANUSCRIPT_CLAIM_DOCTRINE.md:72 | term=historical identity | ECONOMIC EQUIVALENCE -> HISTORICAL IDENTITY
- F4-O-004 | 15-publications/F2/manuscript/F2_CANONICAL_MANUSCRIPT.md:108 | term=historical identity | - historical identity,
- F4-O-004 | 15-publications/F2/manuscript/F2_CANONICAL_MANUSCRIPT.md:127 | term=historical identity | **economic equivalence != historical identity**
- F4-O-004 | 15-publications/F2/manuscript/F2_CANONICAL_MANUSCRIPT.md:1133 | term=historical identity | Economic Equivalence != Historical Identity
- F4-O-004 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:51 | term=historical identity | != historical identity
- F4-O-004 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:97 | term=historical identity | - historical identity distinctions.
- F4-O-004 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:109 | term=historical identity | economic equivalence == historical identity
- F4-O-004 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:192 | term=historical identity | finality != historical identity
- F4-O-004 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:627 | term=historical identity | balance equality != historical identity
- F4-O-004 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:633 | term=historical identity | finality != historical identity
- F4-O-004 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1130 | term=historical record | from historical record destruction.
- F4-O-004 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1148 | term=historical state | preserves prior classification as historical state.
- F4-O-004 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1388 | term=historical identity | ## CE-12 — Final But Historical Identity Different
- F4-O-004 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1397 | term=historical identity | finality != historical identity
- F4-O-004 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1475 | term=historical identity | finality != historical identity
- F4-O-005 | 02-core/transitions/FINANCIAL_TRANSITION_ALGEBRA.md:154 | term=reopening | New evidence, newly authorized remediation, legal reopening, or externally authoritative transition may create a new execution event.
- F4-O-005 | 03-registries/F3_ADVERSARIAL_VERIFICATION_MATRIX.csv:14 | term=reopening | F3-ADV-013,History,reopening==historical-erasure,BLOCK,REGISTERED
- F4-O-005 | 03-registries/F3_INVARIANT_REGISTER.csv:16 | term=reopening | F3-INV-015,FIN-FIN,Consequential closure does not imply impossibility of reopening,OPEN
- F4-O-005 | 03-registries/F3_INVARIANT_REGISTER.csv:17 | term=reopening | F3-INV-016,FIN-FIN,Reopening does not erase historical finality evidence,OPEN
- F4-O-005 | 03-registries/F3_NON_EQUIVALENCE_REGISTRY.csv:16 | term=reopening | F3-NE-015,consequential closure,impossibility of reopening,REQUIRED
- F4-O-005 | 03-registries/F3_NON_EQUIVALENCE_REGISTRY.csv:17 | term=reopening | F3-NE-016,reopening,erasure of historical finality,REQUIRED
- F4-O-005 | 03-registries/F3_PROOF_OBLIGATION_REGISTRY.csv:22 | term=reopening | F3-PO-021,HISTORY,Prove reopening preserves historical finality evidence,OPEN
- F4-O-005 | 03-registries/F3_PROOF_OBLIGATION_REGISTRY.csv:40 | term=reopening | F3-PO-039,RUNTIME-CONF,Verify reference classifier preserves historical finality after reopening,OPEN
- F4-O-005 | 03-registries/F3_RUNTIME_CONFORMANCE_MATRIX.csv:6 | term=reopening | F3-PO-039,Preserve historical finality after reopening,tests/f3/test_f3_runtime.py::test_reopening_preserves_historical_finality,REFERENCE-RUNTIME-CONFORMANT
- F4-O-005 | 06-f3-discovery/formal/F3_NON_EQUIVALENCE_ALGEBRA.md:35 | term=reopening | consequential closure != impossibility of reopening
- F4-O-005 | 06-f3-discovery/formal/F3_NON_EQUIVALENCE_ALGEBRA.md:37 | term=reopening | reopening != erasure of historical finality
- F4-O-005 | 06-f3-discovery/formal/F3_TRANSITION_SYSTEM.md:148 | term=reopening | Reopening or invalidation does not erase the earlier classification event.
- F4-O-005 | 06-f3-discovery/proofs/F3_COUNTEREXAMPLE_DISCHARGE.md:220 | term=reopening | consequential closure != impossibility of reopening
- F4-O-005 | 06-f3-discovery/proofs/F3_POSITIVE_PROOF_DISCHARGE.md:116 | term=reopening | ## F3-PO-021 — Reopening Preserves Historical Finality Evidence
- F4-O-005 | 06-f3-discovery/proofs/F3_POSITIVE_PROOF_DISCHARGE.md:127 | term=reopening | Therefore reopening changes current classification without erasing the historical classification event.
- F4-O-005 | 06-f3-discovery/proofs/F3_POSITIVE_PROOF_DISCHARGE.md:180 | term=reopening | ## F3-PO-025 — Reopening Requires Explicit Admissible Transition
- F4-O-005 | 06-f3-discovery/proofs/F3_POSITIVE_PROOF_DISCHARGE.md:192 | term=reopening | Reopening is not inferred solely from new activity.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:431 | term=reopening | - 03-registries/F3_ADVERSARIAL_VERIFICATION_MATRIX.csv:14 | pattern=reopen | F3-ADV-013,History,reopening==historical-erasure,BLOCK,REGISTERED
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:457 | term=reopening | - 03-registries/F3_INVARIANT_REGISTER.csv:16 | pattern=closure | F3-INV-015,FIN-FIN,Consequential closure does not imply impossibility of reopening,OPEN
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:458 | term=reopening | - 03-registries/F3_INVARIANT_REGISTER.csv:16 | pattern=reopen | F3-INV-015,FIN-FIN,Consequential closure does not imply impossibility of reopening,OPEN
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:459 | term=reopening | - 03-registries/F3_INVARIANT_REGISTER.csv:17 | pattern=finality | F3-INV-016,FIN-FIN,Reopening does not erase historical finality evidence,OPEN
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:460 | term=reopening | - 03-registries/F3_INVARIANT_REGISTER.csv:17 | pattern=reopen | F3-INV-016,FIN-FIN,Reopening does not erase historical finality evidence,OPEN
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:497 | term=reopening | - 03-registries/F3_NON_EQUIVALENCE_REGISTRY.csv:16 | pattern=closure | F3-NE-015,consequential closure,impossibility of reopening,REQUIRED
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:498 | term=reopening | - 03-registries/F3_NON_EQUIVALENCE_REGISTRY.csv:16 | pattern=reopen | F3-NE-015,consequential closure,impossibility of reopening,REQUIRED
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:499 | term=reopening | - 03-registries/F3_NON_EQUIVALENCE_REGISTRY.csv:17 | pattern=finality | F3-NE-016,reopening,erasure of historical finality,REQUIRED
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:500 | term=reopening | - 03-registries/F3_NON_EQUIVALENCE_REGISTRY.csv:17 | pattern=reopen | F3-NE-016,reopening,erasure of historical finality,REQUIRED
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:547 | term=reopening | - 03-registries/F3_PROOF_OBLIGATION_REGISTRY.csv:22 | pattern=finality | F3-PO-021,HISTORY,Prove reopening preserves historical finality evidence,OPEN
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:548 | term=reopening | - 03-registries/F3_PROOF_OBLIGATION_REGISTRY.csv:22 | pattern=reopen | F3-PO-021,HISTORY,Prove reopening preserves historical finality evidence,OPEN
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:559 | term=reopening | - 03-registries/F3_PROOF_OBLIGATION_REGISTRY.csv:40 | pattern=finality | F3-PO-039,RUNTIME-CONF,Verify reference classifier preserves historical finality after reopening,OPEN
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:560 | term=reopening | - 03-registries/F3_PROOF_OBLIGATION_REGISTRY.csv:40 | pattern=reopen | F3-PO-039,RUNTIME-CONF,Verify reference classifier preserves historical finality after reopening,OPEN
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:566 | term=reopening | - 03-registries/F3_RUNTIME_CONFORMANCE_MATRIX.csv:6 | pattern=finality | F3-PO-039,Preserve historical finality after reopening,tests/f3/test_f3_runtime.py::test_reopening_preserves_historical_finality,REFERENCE-RUNTIME-CONFORMANT
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:567 | term=reopening | - 03-registries/F3_RUNTIME_CONFORMANCE_MATRIX.csv:6 | pattern=reopen | F3-PO-039,Preserve historical finality after reopening,tests/f3/test_f3_runtime.py::test_reopening_preserves_historical_finality,REFERENCE-RUNTIME-CONFORMANT
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1146 | term=reopening | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:637 | pattern=closure | consequential closure != impossibility of reopening
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1147 | term=reopening | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:637 | pattern=reopen | consequential closure != impossibility of reopening
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1148 | term=reopening | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:639 | pattern=finality | reopening != erasure of historical finality
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1149 | term=reopening | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:639 | pattern=reopen | reopening != erasure of historical finality
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1190 | term=reopening | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:797 | pattern=reopen | Reopening or invalidation does not erase the earlier classification event.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1272 | term=reopening | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1123 | pattern=finality | ## F3-PO-021 — Reopening Preserves Historical Finality Evidence
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1273 | term=reopening | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1123 | pattern=reopen | ## F3-PO-021 — Reopening Preserves Historical Finality Evidence
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1278 | term=reopening | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1134 | pattern=reopen | Therefore reopening changes current classification without erasing the historical classification event.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1288 | term=reopening | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1187 | pattern=reopen | ## F3-PO-025 — Reopening Requires Explicit Admissible Transition
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1295 | term=reopening | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1199 | pattern=reopen | Reopening is not inferred solely from new activity.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1341 | term=reopening | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1427 | pattern=closure | consequential closure != impossibility of reopening
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1342 | term=reopening | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1427 | pattern=reopen | consequential closure != impossibility of reopening
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1508 | term=reopening | - formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:17 | pattern=finality | **Required premises:** Settlement history; finality model; governing conditions; evidence; reopening authority if applicable.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1509 | term=reopening | - formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:17 | pattern=reopen | **Required premises:** Settlement history; finality model; governing conditions; evidence; reopening authority if applicable.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1512 | term=reopening | - formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:21 | pattern=finality | **Evidence requirement:** Finality-classification record; conditions; evidence basis; reopening evidence where applicable.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1513 | term=reopening | - formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:21 | pattern=reopen | **Evidence requirement:** Finality-classification record; conditions; evidence basis; reopening evidence where applicable.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1521 | term=reopening | - formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:41 | pattern=finality | **Required premises:** Settlement history; finality model; governing conditions; evidence; reopening authority if applicable.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1522 | term=reopening | - formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:41 | pattern=reopen | **Required premises:** Settlement history; finality model; governing conditions; evidence; reopening authority if applicable.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1525 | term=reopening | - formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:45 | pattern=finality | **Evidence requirement:** Finality-classification record; conditions; evidence basis; reopening evidence where applicable.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1526 | term=reopening | - formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:45 | pattern=reopen | **Evidence requirement:** Finality-classification record; conditions; evidence basis; reopening evidence where applicable.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1535 | term=reopening | - formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:65 | pattern=finality | **Required premises:** Settlement history; finality model; governing conditions; evidence; reopening authority if applicable.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1536 | term=reopening | - formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:65 | pattern=reopen | **Required premises:** Settlement history; finality model; governing conditions; evidence; reopening authority if applicable.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1539 | term=reopening | - formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:69 | pattern=finality | **Evidence requirement:** Finality-classification record; conditions; evidence basis; reopening evidence where applicable.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1540 | term=reopening | - formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:69 | pattern=reopen | **Evidence requirement:** Finality-classification record; conditions; evidence basis; reopening evidence where applicable.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1549 | term=reopening | - formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:89 | pattern=finality | **Required premises:** Settlement history; finality model; governing conditions; evidence; reopening authority if applicable.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1550 | term=reopening | - formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:89 | pattern=reopen | **Required premises:** Settlement history; finality model; governing conditions; evidence; reopening authority if applicable.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1553 | term=reopening | - formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:93 | pattern=finality | **Evidence requirement:** Finality-classification record; conditions; evidence basis; reopening evidence where applicable.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1554 | term=reopening | - formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:93 | pattern=reopen | **Evidence requirement:** Finality-classification record; conditions; evidence basis; reopening evidence where applicable.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1563 | term=reopening | - formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:113 | pattern=finality | **Required premises:** Settlement history; finality model; governing conditions; evidence; reopening authority if applicable.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1564 | term=reopening | - formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:113 | pattern=reopen | **Required premises:** Settlement history; finality model; governing conditions; evidence; reopening authority if applicable.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1567 | term=reopening | - formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:117 | pattern=finality | **Evidence requirement:** Finality-classification record; conditions; evidence basis; reopening evidence where applicable.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1568 | term=reopening | - formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:117 | pattern=reopen | **Evidence requirement:** Finality-classification record; conditions; evidence basis; reopening evidence where applicable.
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1939 | term=reopening | - tests/f3/test_f3_runtime.py:87 | pattern=finality | def test_reopening_preserves_historical_finality():
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1940 | term=reopening | - tests/f3/test_f3_runtime.py:87 | pattern=reopen | def test_reopening_preserves_historical_finality():
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:2007 | term=reopening | - tests/f3_adversarial/test_f3_adversarial.py:160 | pattern=finality | def test_reopening_does_not_erase_historical_finality():
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:2008 | term=reopening | - tests/f3_adversarial/test_f3_adversarial.py:160 | pattern=reopen | def test_reopening_does_not_erase_historical_finality():
- F4-O-005 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:2035 | term=reopening | - reopening != historical erasure
- F4-O-005 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:50 | term=record reopening | - record reopening != historical erasure
- F4-O-005 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:50 | term=reopening | - record reopening != historical erasure
- F4-O-005 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:859 | term=record reopening | - record reopening
- F4-O-005 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:859 | term=reopening | - record reopening
- F4-O-005 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:637 | term=reopening | consequential closure != impossibility of reopening
- F4-O-005 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:639 | term=reopening | reopening != erasure of historical finality
- F4-O-005 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:797 | term=reopening | Reopening or invalidation does not erase the earlier classification event.
- F4-O-005 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1123 | term=reopening | ## F3-PO-021 — Reopening Preserves Historical Finality Evidence
- F4-O-005 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1134 | term=reopening | Therefore reopening changes current classification without erasing the historical classification event.
- F4-O-005 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1187 | term=reopening | ## F3-PO-025 — Reopening Requires Explicit Admissible Transition
- F4-O-005 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1199 | term=reopening | Reopening is not inferred solely from new activity.
- F4-O-005 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1427 | term=reopening | consequential closure != impossibility of reopening
- F4-O-005 | formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:17 | term=reopening | **Required premises:** Settlement history; finality model; governing conditions; evidence; reopening authority if applicable.
- F4-O-005 | formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:21 | term=reopening | **Evidence requirement:** Finality-classification record; conditions; evidence basis; reopening evidence where applicable.
- F4-O-005 | formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:41 | term=reopening | **Required premises:** Settlement history; finality model; governing conditions; evidence; reopening authority if applicable.
- F4-O-005 | formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:45 | term=reopening | **Evidence requirement:** Finality-classification record; conditions; evidence basis; reopening evidence where applicable.
- F4-O-005 | formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:65 | term=reopening | **Required premises:** Settlement history; finality model; governing conditions; evidence; reopening authority if applicable.
- F4-O-005 | formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:69 | term=reopening | **Evidence requirement:** Finality-classification record; conditions; evidence basis; reopening evidence where applicable.
- F4-O-005 | formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:89 | term=reopening | **Required premises:** Settlement history; finality model; governing conditions; evidence; reopening authority if applicable.
- F4-O-005 | formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:93 | term=reopening | **Evidence requirement:** Finality-classification record; conditions; evidence basis; reopening evidence where applicable.
- F4-O-005 | formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:113 | term=reopening | **Required premises:** Settlement history; finality model; governing conditions; evidence; reopening authority if applicable.
- F4-O-005 | formal-proofs/FIN-FIN_PROOF_OBLIGATIONS.md:117 | term=reopening | **Evidence requirement:** Finality-classification record; conditions; evidence basis; reopening evidence where applicable.
- F4-O-005 | tests/f3/test_f3_runtime.py:87 | term=reopening | def test_reopening_preserves_historical_finality():
- F4-O-005 | tests/f3_adversarial/test_f3_adversarial.py:160 | term=reopening | def test_reopening_does_not_erase_historical_finality():
- F4-O-006 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:860 | term=ledger contradiction | - ledger contradiction
- F4-O-007 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:861 | term=record-state reconstruction | - record-state reconstruction
- F4-O-007 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:861 | term=state reconstruction | - record-state reconstruction
- F4-O-008 | 03-registries/F3_FINALITY_ELIGIBILITY_REGISTER.csv:8 | term=finality conflict | FE-07,No unresolved applicable finality conflict,BLOCK,FORMALIZED
- F4-O-008 | 03-registries/F3_INVARIANT_REGISTER.csv:23 | term=finality conflict | F3-INV-022,FIN-FIN,Current finality is blocked by unresolved applicable finality conflict,OPEN
- F4-O-008 | 03-registries/F3_OBJECT_REGISTRY.csv:13 | term=finality conflict | F3-O-012,Finality Conflict,F3,FORMALIZED
- F4-O-008 | 03-registries/F3_PROOF_OBLIGATION_REGISTRY.csv:15 | term=finality conflict | F3-PO-014,SAFETY,Prove unresolved finality conflict blocks current finality,OPEN
- F4-O-008 | 05-distributed-settlement/formal/F2_DISTRIBUTED_RECONCILIATION.md:223 | term=finality conflict | prior finality conflict
- F4-O-008 | 06-f3-discovery/FIN_F3_01B_PROBLEM_BOUNDARY.md:73 | term=finality conflict | 14. finality conflict state;
- F4-O-008 | 06-f3-discovery/FIN_F3_01B_PROBLEM_BOUNDARY.md:156 | term=finality conflict | - finality conflict predicate;
- F4-O-008 | 06-f3-discovery/formal/F3_CANONICAL_OBJECTS.md:103 | term=finality conflict | ### F3-O-012 — Finality Conflict
- F4-O-008 | 06-f3-discovery/formal/F3_FINALITY_ELIGIBILITY_SEMANTICS.md:76 | term=finality conflict | No unresolved applicable Finality Conflict exists.
- F4-O-008 | 06-f3-discovery/formal/F3_FINALITY_ELIGIBILITY_SEMANTICS.md:141 | term=finality conflict | FB-07 unresolved finality conflict
- F4-O-008 | 06-f3-discovery/formal/F3_RELATION_ALGEBRA.md:56 | term=finality conflict | 2. no unresolved applicable Finality Conflict exists;
- F4-O-008 | 06-f3-discovery/proofs/F3_COUNTEREXAMPLE_DISCHARGE.md:81 | term=finality conflict | finality conflict = unresolved
- F4-O-008 | 06-f3-discovery/proofs/F3_POSITIVE_PROOF_DISCHARGE.md:13 | term=finality conflict | ## F3-PO-014 — Unresolved Finality Conflict Blocks Current Finality
- F4-O-008 | 06-f3-discovery/proofs/F3_POSITIVE_PROOF_DISCHARGE.md:19 | term=finality conflict | FE-07 requires no unresolved applicable Finality Conflict.
- F4-O-008 | 06-f3-discovery/proofs/F3_POSITIVE_PROOF_DISCHARGE.md:27 | term=finality conflict | Thus an unresolved applicable finality conflict blocks current finality.
- F4-O-008 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:436 | term=finality conflict | - 03-registries/F3_FINALITY_ELIGIBILITY_REGISTER.csv:8 | pattern=finality | FE-07,No unresolved applicable finality conflict,BLOCK,FORMALIZED
- F4-O-008 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:466 | term=finality conflict | - 03-registries/F3_INVARIANT_REGISTER.csv:23 | pattern=finality | F3-INV-022,FIN-FIN,Current finality is blocked by unresolved applicable finality conflict,OPEN
- F4-O-008 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:515 | term=finality conflict | - 03-registries/F3_OBJECT_REGISTRY.csv:13 | pattern=finality | F3-O-012,Finality Conflict,F3,FORMALIZED
- F4-O-008 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:537 | term=finality conflict | - 03-registries/F3_PROOF_OBLIGATION_REGISTRY.csv:15 | pattern=finality | F3-PO-014,SAFETY,Prove unresolved finality conflict blocks current finality,OPEN
- F4-O-008 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:935 | term=finality conflict | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:83 | pattern=finality | 14. finality conflict state;
- F4-O-008 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:958 | term=finality conflict | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:166 | pattern=finality | - finality conflict predicate;
- F4-O-008 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1046 | term=finality conflict | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:383 | pattern=finality | ### F3-O-012 — Finality Conflict
- F4-O-008 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1114 | term=finality conflict | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:558 | pattern=finality | 2. no unresolved applicable Finality Conflict exists;
- F4-O-008 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1209 | term=finality conflict | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:889 | pattern=finality | No unresolved applicable Finality Conflict exists.
- F4-O-008 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1220 | term=finality conflict | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:954 | pattern=finality | FB-07 unresolved finality conflict
- F4-O-008 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1240 | term=finality conflict | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1020 | pattern=finality | ## F3-PO-014 — Unresolved Finality Conflict Blocks Current Finality
- F4-O-008 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1242 | term=finality conflict | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1026 | pattern=finality | FE-07 requires no unresolved applicable Finality Conflict.
- F4-O-008 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1245 | term=finality conflict | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1034 | pattern=finality | Thus an unresolved applicable finality conflict blocks current finality.
- F4-O-008 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1313 | term=finality conflict | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1288 | pattern=finality | finality conflict = unresolved
- F4-O-008 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:862 | term=finality conflict | - ledger / finality conflict
- F4-O-008 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:83 | term=finality conflict | 14. finality conflict state;
- F4-O-008 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:166 | term=finality conflict | - finality conflict predicate;
- F4-O-008 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:383 | term=finality conflict | ### F3-O-012 — Finality Conflict
- F4-O-008 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:558 | term=finality conflict | 2. no unresolved applicable Finality Conflict exists;
- F4-O-008 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:889 | term=finality conflict | No unresolved applicable Finality Conflict exists.
- F4-O-008 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:954 | term=finality conflict | FB-07 unresolved finality conflict
- F4-O-008 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1020 | term=finality conflict | ## F3-PO-014 — Unresolved Finality Conflict Blocks Current Finality
- F4-O-008 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1026 | term=finality conflict | FE-07 requires no unresolved applicable Finality Conflict.
- F4-O-008 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1034 | term=finality conflict | Thus an unresolved applicable finality conflict blocks current finality.
- F4-O-008 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:1288 | term=finality conflict | finality conflict = unresolved
- F4-O-009 | 06-f3-discovery/FIN_F3_01B_PROBLEM_BOUNDARY.md:229 | term=custody record | - conflicting custody records;
- F4-O-009 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1002 | term=custody record | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:239 | pattern=custody | - conflicting custody records;
- F4-O-009 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:52 | term=recorded custody | - recorded custody != custody authority
- F4-O-009 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:863 | term=custody representation | - ledger / custody representation
- F4-O-009 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:239 | term=custody record | - conflicting custody records;
- F4-O-010 | 02-core/components/CANONICAL_FINANCIAL_COMPONENT_ARCHITECTURE.md:90 | term=continuity classification | Continuity classification does not repair continuity.
- F4-O-010 | 02-core/components/FIN-COMP-020_Continuity_Classifier.md:21 | term=continuity classification | Continuity classification
- F4-O-010 | 02-core/invariants/CANONICAL_FINANCIAL_INVARIANT_ARCHITECTURE.md:110 | term=continuity classification | -> finality and continuity classification
- F4-O-010 | 02-core/states/CONTINUITY_CLASSIFICATION_MODEL.md:1 | term=continuity classification | # Financial Continuity Classification Model
- F4-O-010 | 02-core/states/CONTINUITY_CLASSIFICATION_MODEL.md:5 | term=continuity classification | Continuity classification determines whether execution-relevant integrity remained continuous across the financial transition history.
- F4-O-010 | 02-core/states/FINANCIAL_STATE_MODEL.md:7 | term=continuity classification | State identity, transition existence, transition admissibility, transition execution, finality, and continuity classification are separate concepts.
- F4-O-010 | 02-core/states/FINANCIAL_STATE_MODEL.md:178 | term=continuity classification | The resulting execution has received explicit finality and continuity classifications.
- F4-O-010 | 02-core/transitions/CANONICAL_FINANCIAL_TRANSITION_ALGEBRA.md:121 | term=continuity classification | ## Continuity Classification
- F4-O-010 | 02-core/transitions/CANONICAL_FINANCIAL_TRANSITION_ALGEBRA.md:131 | term=continuity classification | Continuity classification is separate from financial balance equivalence.
- F4-O-010 | 02-core/transitions/TRANSITION_ADMISSIBILITY_BOUNDARY.md:37 | term=continuity classification | 14. What continuity classification applies?
- F4-O-010 | 02-core/types/CANONICAL_FINANCIAL_TYPE_SYSTEM.md:241 | term=continuity classification | Reference to continuity classification inherited from upstream architectures.
- F4-O-010 | 03-registries/COMPONENT_REGISTRY.csv:16 | term=continuity classification | "FI-CNT-001","Economic Continuity Classifier","CONTINUITY","Classify financial execution continuity independently from completion, balance equivalence, and settlement finality.","Execution history;EvidenceObject;EconomicState","Continuity classification","EIP;POB","F3"
- F4-O-010 | 03-registries/F1_CONTINUITY_CLASS_REGISTRY.csv:6 | term=continuity classification | "F1-CNT-C005","INDETERMINATE","UNKNOWN","UNKNOWN","Evidence is insufficient to establish a unique continuity classification"
- F4-O-010 | 03-registries/F1_CONTINUITY_PROOF_CANDIDATES.csv:6 | term=continuity classification | "F1-CNT-PC005","COUNTEREXAMPLE","Two histories may terminate in economically equivalent states while possessing different continuity classifications.","FIN-CNT-004","OPEN"
- F4-O-010 | 03-registries/F1_CONTINUITY_PROOF_CANDIDATES.csv:9 | term=continuity classification | "F1-CNT-PC008","TRACEABILITY","A reconstructed continuity classification preserves evidence of the preceding continuity break.","FIN-CNT-003;FIN-EVD-001","OPEN"
- F4-O-010 | 03-registries/F1_MANUSCRIPT_SECTION_SOURCE_MATRIX.csv:10 | term=state continuity | "8 Economic-State Continuity","F1_ECONOMIC_CONTINUITY_ALGEBRA.md","NO"
- F4-O-010 | 03-registries/F1_NOVELTY_INHERITANCE_MATRIX.csv:11 | term=continuity classification | "Post-effect financial continuity classification","NEW-SPECIALIZATION","F1/EIP","FORMALIZE WITH EIP BINDING"
- F4-O-010 | 03-registries/F1_RUNTIME_TEST_RESULTS.csv:9 | term=continuity classification | "F1-RT-TEST-008","F1 continuity classification","PASS","NO"
- F4-O-010 | 03-registries/F1_SCOPE_REGISTRY.csv:11 | term=continuity classification | "F1-SCP-010","Post-effect continuity classification","IN-SCOPE","F1"
- F4-O-010 | 03-registries/F1_SEMANTIC_ARCHITECTURE_MATRIX.csv:7 | term=state continuity | "FIN-F1-06","Economic-state continuity","ESTABLISHED"
- F4-O-010 | 03-registries/FORBIDDEN_AUTHORITY_RELATIONSHIPS.csv:7 | term=continuity classification | "FIN-FORBID-006","Continuity Classifier","Create authority from continuity classification","Classification is descriptive/evaluative"
- F4-O-010 | 03-registries/INTERFACE_REGISTRY.csv:16 | term=continuity classification | "FI-IF-015","ClassifyEconomicContinuity","FI-CNT-001","history + evidence + state","continuity classification"
- F4-O-010 | 03-registries/PROOF_OBLIGATION_REGISTRY.csv:41 | term=continuity classification | "FIN-PO-040","FIN-CNT-004","COUNTEREXAMPLE","Continuity Cannot Be Inferred From Balance Equality","Construct a valid financial history in which resulting balances are equal while execution continuity was broken, proving balance equality insufficient for continuity classification.","Settlement recovery","FIN-ARCH-04","F3","OPEN","","","",""
- F4-O-010 | 03-registries/STATE_OWNERSHIP_REGISTRY.csv:12 | term=continuity classification | "Continuity classification","FIN-COMP-020","NO"
- F4-O-010 | 05-distributed-settlement/evidence/FIN_F2_08_RESULT.md:7 | term=state continuity | FIN-F2-08 — Distributed Economic-State Continuity
- F4-O-010 | 05-distributed-settlement/evidence/FIN_F2_08_RESULT.md:27 | term=continuity classification | Distributed continuity classification
- F4-O-010 | 05-distributed-settlement/evidence/FIN_F2_10_RESULT.md:33 | term=continuity classification | - distributed continuity classification
- F4-O-010 | 05-distributed-settlement/evidence/FIN_F2_12_RESULT.md:38 | term=state continuity | - distributed economic-state continuity
- F4-O-010 | 05-distributed-settlement/formal/F2_ATOMICITY_SEMANTICS.md:298 | term=continuity classification | distributed continuity classification
- F4-O-010 | 05-distributed-settlement/formal/F2_DISTRIBUTED_CONTINUITY_TRANSITIONS.md:131 | term=continuity classification | continuity classification.
- F4-O-010 | 05-distributed-settlement/formal/F2_DISTRIBUTED_ECONOMIC_STATE_CONTINUITY.md:1 | term=state continuity | # FIN-F2-08 — Distributed Economic-State Continuity
- F4-O-010 | 05-distributed-settlement/formal/F2_DISTRIBUTED_ECONOMIC_STATE_CONTINUITY.md:5 | term=state continuity | Distributed economic-state continuity classifies whether the economic
- F4-O-010 | 05-distributed-settlement/formal/F2_DISTRIBUTED_ECONOMIC_STATE_CONTINUITY.md:134 | term=continuity classification | ## 7. Continuity Classification
- F4-O-010 | 05-distributed-settlement/formal/F2_DISTRIBUTED_ECONOMIC_STATE_CONTINUITY.md:335 | term=continuity classification | as continuity classification within domain D_i.
- F4-O-010 | 05-distributed-settlement/formal/F2_DISTRIBUTED_ECONOMIC_STATE_CONTINUITY.md:419 | term=continuity classification | Distributed continuity classification SHALL preserve:
- F4-O-010 | 05-distributed-settlement/formal/F2_DISTRIBUTED_RECONCILIATION.md:249 | term=continuity classification | Distributed continuity classification remains FIN-F2-08.
- F4-O-010 | 05-distributed-settlement/formal/F2_EXECUTION_LEG_COMPOSITION.md:256 | term=continuity classification | continuity classification
- F4-O-010 | 05-distributed-settlement/runtime/f2_runtime/README.md:15 | term=continuity classification | - distributed continuity classification
- F4-O-010 | 05-distributed-settlement/scope/F2_PROBLEM_BOUNDARY.md:19 | term=state continuity | - economic-state continuity
- F4-O-010 | 06-f3-discovery/FIN_F3_01_DISCOVERY.md:13 | term=state continuity | - F1 — Partial Settlement, Compensating Execution, and Economic-State Continuity
- F4-O-010 | 06-f3-discovery/FIN_F3_01B_PROBLEM_BOUNDARY.md:13 | term=state continuity | - F1 — Partial Settlement, Compensating Execution, and Economic-State Continuity
- F4-O-010 | 06-f3-discovery/FIN_F3_01B_PROBLEM_BOUNDARY.md:85 | term=state continuity | - economic-state continuity;
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:117 | term=continuity classification | - 03-registries/COMPONENT_REGISTRY.csv:16 | pattern=continuity | "FI-CNT-001","Economic Continuity Classifier","CONTINUITY","Classify financial execution continuity independently from completion, balance equivalence, and settlement finality.","Execution history;EvidenceObject;EconomicState","Continuity classification","EIP;POB","F3"
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:118 | term=continuity classification | - 03-registries/COMPONENT_REGISTRY.csv:16 | pattern=finality | "FI-CNT-001","Economic Continuity Classifier","CONTINUITY","Classify financial execution continuity independently from completion, balance equivalence, and settlement finality.","Execution history;EvidenceObject;EconomicState","Continuity classification","EIP;POB","F3"
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:148 | term=continuity classification | - 03-registries/F1_CONTINUITY_CLASS_REGISTRY.csv:6 | pattern=continuity | "F1-CNT-C005","INDETERMINATE","UNKNOWN","UNKNOWN","Evidence is insufficient to establish a unique continuity classification"
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:157 | term=continuity classification | - 03-registries/F1_CONTINUITY_PROOF_CANDIDATES.csv:6 | pattern=continuity | "F1-CNT-PC005","COUNTEREXAMPLE","Two histories may terminate in economically equivalent states while possessing different continuity classifications.","FIN-CNT-004","OPEN"
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:160 | term=continuity classification | - 03-registries/F1_CONTINUITY_PROOF_CANDIDATES.csv:9 | pattern=continuity | "F1-CNT-PC008","TRACEABILITY","A reconstructed continuity classification preserves evidence of the preceding continuity break.","FIN-CNT-003;FIN-EVD-001","OPEN"
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:200 | term=state continuity | - 03-registries/F1_MANUSCRIPT_SECTION_SOURCE_MATRIX.csv:10 | pattern=continuity | "8 Economic-State Continuity","F1_ECONOMIC_CONTINUITY_ALGEBRA.md","NO"
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:202 | term=continuity classification | - 03-registries/F1_NOVELTY_INHERITANCE_MATRIX.csv:11 | pattern=continuity | "Post-effect financial continuity classification","NEW-SPECIALIZATION","F1/EIP","FORMALIZE WITH EIP BINDING"
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:258 | term=continuity classification | - 03-registries/F1_RUNTIME_TEST_RESULTS.csv:9 | pattern=continuity | "F1-RT-TEST-008","F1 continuity classification","PASS","NO"
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:259 | term=continuity classification | - 03-registries/F1_SCOPE_REGISTRY.csv:11 | pattern=continuity | "F1-SCP-010","Post-effect continuity classification","IN-SCOPE","F1"
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:261 | term=state continuity | - 03-registries/F1_SEMANTIC_ARCHITECTURE_MATRIX.csv:7 | pattern=continuity | "FIN-F1-06","Economic-state continuity","ESTABLISHED"
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:616 | term=continuity classification | - 03-registries/FORBIDDEN_AUTHORITY_RELATIONSHIPS.csv:7 | pattern=continuity | "FIN-FORBID-006","Continuity Classifier","Create authority from continuity classification","Classification is descriptive/evaluative"
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:619 | term=continuity classification | - 03-registries/INTERFACE_REGISTRY.csv:16 | pattern=continuity | "FI-IF-015","ClassifyEconomicContinuity","FI-CNT-001","history + evidence + state","continuity classification"
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:681 | term=continuity classification | - 03-registries/PROOF_OBLIGATION_REGISTRY.csv:41 | pattern=continuity | "FIN-PO-040","FIN-CNT-004","COUNTEREXAMPLE","Continuity Cannot Be Inferred From Balance Equality","Construct a valid financial history in which resulting balances are equal while execution continuity was broken, proving balance equality insufficient for continuity classification.","Settlement recovery","FIN-ARCH-04","F3","OPEN","","","",""
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:689 | term=continuity classification | - 03-registries/STATE_OWNERSHIP_REGISTRY.csv:12 | pattern=continuity | "Continuity classification","FIN-COMP-020","NO"
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:714 | term=state continuity | - 15-publications/F1/F1_OUTLINE.md:5 | pattern=continuity | Partial Settlement, Compensating Execution, and Economic-State Continuity
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:715 | term=state continuity | - 15-publications/F1/F1_OUTLINE.md:56 | pattern=continuity | ## 10. Economic-State Continuity
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:736 | term=state continuity | - 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:1 | pattern=continuity | # Partial Settlement, Compensating Execution, and Economic-State Continuity
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:737 | term=state continuity | - 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:25 | pattern=continuity | operation; and classifies economic-state continuity as preserved, degraded,
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:748 | term=state continuity | - 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:507 | pattern=continuity | # 8. Economic-State Continuity
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:758 | term=continuity classification | - 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:581 | pattern=continuity | different continuity classifications.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:766 | term=continuity classification | - 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:720 | pattern=continuity | -> Continuity Classification
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:772 | term=continuity classification | - 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:809 | pattern=continuity | Reconstruction adds a continuity classification.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:792 | term=state continuity | - 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:1012 | pattern=continuity | FIN-F1-06 — economic-state continuity
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:794 | term=state continuity | - 15-publications/F2/manuscript/F2_CANONICAL_MANUSCRIPT.md:1 | pattern=continuity | # Distributed Settlement, Multiparty Authority, and Economic-State Continuity
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:800 | term=state continuity | - 15-publications/F2/manuscript/F2_CANONICAL_MANUSCRIPT.md:42 | pattern=continuity | economic-state continuity
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:807 | term=state continuity | - 15-publications/F2/manuscript/F2_CANONICAL_MANUSCRIPT.md:85 | pattern=continuity | - and whether economic-state continuity was preserved.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:845 | term=state continuity | - 15-publications/F2/manuscript/F2_CANONICAL_MANUSCRIPT.md:722 | pattern=continuity | # 18. Distributed Economic-State Continuity
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:849 | term=continuity classification | - 15-publications/F2/manuscript/F2_CANONICAL_MANUSCRIPT.md:746 | pattern=continuity | The inherited continuity classifications are:
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:891 | term=state continuity | - 15-publications/F2/manuscript/F2_CANONICAL_MANUSCRIPT.md:1197 | pattern=continuity | FIN-F2-08 — Distributed Economic-State Continuity
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:902 | term=state continuity | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:23 | pattern=continuity | - F1 — Partial Settlement, Compensating Execution, and Economic-State Continuity
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:937 | term=state continuity | - 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:95 | pattern=continuity | - economic-state continuity;
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1409 | term=continuity classification | - formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:15 | pattern=continuity | **Formal target:** Show that continuity classification is independent from reconstruction, restored function, finality, and later economic equivalence.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1410 | term=continuity classification | - formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:15 | pattern=finality | **Formal target:** Show that continuity classification is independent from reconstruction, restored function, finality, and later economic equivalence.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1413 | term=continuity classification | - formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:21 | pattern=continuity | **Evidence requirement:** Continuity classification record; complete relevant execution/remediation history; evidence supporting preserved/broken/indeterminate status.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1414 | term=continuity classification | - formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:23 | pattern=continuity | **Implementation requirement:** Reference runtime must expose explicit continuity classification.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1417 | term=continuity classification | - formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:39 | pattern=continuity | **Formal target:** Show that continuity classification is independent from reconstruction, restored function, finality, and later economic equivalence.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1418 | term=continuity classification | - formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:39 | pattern=finality | **Formal target:** Show that continuity classification is independent from reconstruction, restored function, finality, and later economic equivalence.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1421 | term=continuity classification | - formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:45 | pattern=continuity | **Evidence requirement:** Continuity classification record; complete relevant execution/remediation history; evidence supporting preserved/broken/indeterminate status.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1422 | term=continuity classification | - formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:47 | pattern=continuity | **Implementation requirement:** Reference runtime must expose explicit continuity classification.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1425 | term=continuity classification | - formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:63 | pattern=continuity | **Formal target:** Show that continuity classification is independent from reconstruction, restored function, finality, and later economic equivalence.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1426 | term=continuity classification | - formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:63 | pattern=finality | **Formal target:** Show that continuity classification is independent from reconstruction, restored function, finality, and later economic equivalence.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1429 | term=continuity classification | - formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:69 | pattern=continuity | **Evidence requirement:** Continuity classification record; complete relevant execution/remediation history; evidence supporting preserved/broken/indeterminate status.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1430 | term=continuity classification | - formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:71 | pattern=continuity | **Implementation requirement:** Reference runtime must expose explicit continuity classification.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1433 | term=continuity classification | - formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:87 | pattern=continuity | **Formal target:** Show that continuity classification is independent from reconstruction, restored function, finality, and later economic equivalence.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1434 | term=continuity classification | - formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:87 | pattern=finality | **Formal target:** Show that continuity classification is independent from reconstruction, restored function, finality, and later economic equivalence.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1437 | term=continuity classification | - formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:93 | pattern=continuity | **Evidence requirement:** Continuity classification record; complete relevant execution/remediation history; evidence supporting preserved/broken/indeterminate status.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1438 | term=continuity classification | - formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:95 | pattern=continuity | **Implementation requirement:** Reference runtime must expose explicit continuity classification.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1441 | term=continuity classification | - formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:111 | pattern=continuity | **Formal target:** Show that continuity classification is independent from reconstruction, restored function, finality, and later economic equivalence.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1442 | term=continuity classification | - formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:111 | pattern=finality | **Formal target:** Show that continuity classification is independent from reconstruction, restored function, finality, and later economic equivalence.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1445 | term=continuity classification | - formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:117 | pattern=continuity | **Evidence requirement:** Continuity classification record; complete relevant execution/remediation history; evidence supporting preserved/broken/indeterminate status.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1446 | term=continuity classification | - formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:119 | pattern=continuity | **Implementation requirement:** Reference runtime must expose explicit continuity classification.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1582 | term=continuity classification | - formal-proofs/FIN-REC_PROOF_OBLIGATIONS.md:23 | pattern=continuity | **Implementation requirement:** Reference runtime must keep reconciliation/reconstruction/continuity classifications distinct.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1586 | term=continuity classification | - formal-proofs/FIN-REC_PROOF_OBLIGATIONS.md:47 | pattern=continuity | **Implementation requirement:** Reference runtime must keep reconciliation/reconstruction/continuity classifications distinct.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1590 | term=continuity classification | - formal-proofs/FIN-REC_PROOF_OBLIGATIONS.md:71 | pattern=continuity | **Implementation requirement:** Reference runtime must keep reconciliation/reconstruction/continuity classifications distinct.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1594 | term=continuity classification | - formal-proofs/FIN-REC_PROOF_OBLIGATIONS.md:95 | pattern=continuity | **Implementation requirement:** Reference runtime must keep reconciliation/reconstruction/continuity classifications distinct.
- F4-O-010 | 07-ledger/FIN_F4_01_BOUNDARY_DISCOVERY.md:1598 | term=continuity classification | - formal-proofs/FIN-REC_PROOF_OBLIGATIONS.md:119 | pattern=continuity | **Implementation requirement:** Reference runtime must keep reconciliation/reconstruction/continuity classifications distinct.
- F4-O-010 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:864 | term=continuity classification | - record-state continuity classification
- F4-O-010 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:864 | term=record-state continuity | - record-state continuity classification
- F4-O-010 | 07-ledger/FIN_F4_01B_BOUNDARY_FREEZE.md:864 | term=state continuity | - record-state continuity classification
- F4-O-010 | 15-publications/F1/F1_OUTLINE.md:5 | term=state continuity | Partial Settlement, Compensating Execution, and Economic-State Continuity
- F4-O-010 | 15-publications/F1/F1_OUTLINE.md:56 | term=state continuity | ## 10. Economic-State Continuity
- F4-O-010 | 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:1 | term=state continuity | # Partial Settlement, Compensating Execution, and Economic-State Continuity
- F4-O-010 | 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:25 | term=state continuity | operation; and classifies economic-state continuity as preserved, degraded,
- F4-O-010 | 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:507 | term=state continuity | # 8. Economic-State Continuity
- F4-O-010 | 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:581 | term=continuity classification | different continuity classifications.
- F4-O-010 | 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:720 | term=continuity classification | -> Continuity Classification
- F4-O-010 | 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:809 | term=continuity classification | Reconstruction adds a continuity classification.
- F4-O-010 | 15-publications/F1/manuscript/F1_CANONICAL_MANUSCRIPT.md:1012 | term=state continuity | FIN-F1-06 — economic-state continuity
- F4-O-010 | 15-publications/F2/manuscript/F2_CANONICAL_MANUSCRIPT.md:1 | term=state continuity | # Distributed Settlement, Multiparty Authority, and Economic-State Continuity
- F4-O-010 | 15-publications/F2/manuscript/F2_CANONICAL_MANUSCRIPT.md:42 | term=state continuity | economic-state continuity
- F4-O-010 | 15-publications/F2/manuscript/F2_CANONICAL_MANUSCRIPT.md:85 | term=state continuity | - and whether economic-state continuity was preserved.
- F4-O-010 | 15-publications/F2/manuscript/F2_CANONICAL_MANUSCRIPT.md:722 | term=state continuity | # 18. Distributed Economic-State Continuity
- F4-O-010 | 15-publications/F2/manuscript/F2_CANONICAL_MANUSCRIPT.md:746 | term=continuity classification | The inherited continuity classifications are:
- F4-O-010 | 15-publications/F2/manuscript/F2_CANONICAL_MANUSCRIPT.md:1197 | term=state continuity | FIN-F2-08 — Distributed Economic-State Continuity
- F4-O-010 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:23 | term=state continuity | - F1 — Partial Settlement, Compensating Execution, and Economic-State Continuity
- F4-O-010 | 15-publications/F3/manuscript/F3_CANONICAL_MANUSCRIPT.md:95 | term=state continuity | - economic-state continuity;
- F4-O-010 | formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:15 | term=continuity classification | **Formal target:** Show that continuity classification is independent from reconstruction, restored function, finality, and later economic equivalence.
- F4-O-010 | formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:21 | term=continuity classification | **Evidence requirement:** Continuity classification record; complete relevant execution/remediation history; evidence supporting preserved/broken/indeterminate status.
- F4-O-010 | formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:23 | term=continuity classification | **Implementation requirement:** Reference runtime must expose explicit continuity classification.
- F4-O-010 | formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:39 | term=continuity classification | **Formal target:** Show that continuity classification is independent from reconstruction, restored function, finality, and later economic equivalence.
- F4-O-010 | formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:45 | term=continuity classification | **Evidence requirement:** Continuity classification record; complete relevant execution/remediation history; evidence supporting preserved/broken/indeterminate status.
- F4-O-010 | formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:47 | term=continuity classification | **Implementation requirement:** Reference runtime must expose explicit continuity classification.
- F4-O-010 | formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:63 | term=continuity classification | **Formal target:** Show that continuity classification is independent from reconstruction, restored function, finality, and later economic equivalence.
- F4-O-010 | formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:69 | term=continuity classification | **Evidence requirement:** Continuity classification record; complete relevant execution/remediation history; evidence supporting preserved/broken/indeterminate status.
- F4-O-010 | formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:71 | term=continuity classification | **Implementation requirement:** Reference runtime must expose explicit continuity classification.
- F4-O-010 | formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:87 | term=continuity classification | **Formal target:** Show that continuity classification is independent from reconstruction, restored function, finality, and later economic equivalence.
- F4-O-010 | formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:93 | term=continuity classification | **Evidence requirement:** Continuity classification record; complete relevant execution/remediation history; evidence supporting preserved/broken/indeterminate status.
- F4-O-010 | formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:95 | term=continuity classification | **Implementation requirement:** Reference runtime must expose explicit continuity classification.
- F4-O-010 | formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:111 | term=continuity classification | **Formal target:** Show that continuity classification is independent from reconstruction, restored function, finality, and later economic equivalence.
- F4-O-010 | formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:117 | term=continuity classification | **Evidence requirement:** Continuity classification record; complete relevant execution/remediation history; evidence supporting preserved/broken/indeterminate status.
- F4-O-010 | formal-proofs/FIN-CON_PROOF_OBLIGATIONS.md:119 | term=continuity classification | **Implementation requirement:** Reference runtime must expose explicit continuity classification.
- F4-O-010 | formal-proofs/FIN-REC_PROOF_OBLIGATIONS.md:23 | term=continuity classification | **Implementation requirement:** Reference runtime must keep reconciliation/reconstruction/continuity classifications distinct.
- F4-O-010 | formal-proofs/FIN-REC_PROOF_OBLIGATIONS.md:47 | term=continuity classification | **Implementation requirement:** Reference runtime must keep reconciliation/reconstruction/continuity classifications distinct.
- F4-O-010 | formal-proofs/FIN-REC_PROOF_OBLIGATIONS.md:71 | term=continuity classification | **Implementation requirement:** Reference runtime must keep reconciliation/reconstruction/continuity classifications distinct.
- F4-O-010 | formal-proofs/FIN-REC_PROOF_OBLIGATIONS.md:95 | term=continuity classification | **Implementation requirement:** Reference runtime must keep reconciliation/reconstruction/continuity classifications distinct.
- F4-O-010 | formal-proofs/FIN-REC_PROOF_OBLIGATIONS.md:119 | term=continuity classification | **Implementation requirement:** Reference runtime must keep reconciliation/reconstruction/continuity classifications distinct.

## Release controls

No state algebra frozen.

No transition system frozen.

No invariant registry frozen.

No proof obligations frozen.

No runtime created.

No staging performed.

No commit performed.

No tag created.

No push performed.

## Next

FIN-F4-03 — STATE / CLASSIFICATION ALGEBRA DISCOVERY AND FREEZE
