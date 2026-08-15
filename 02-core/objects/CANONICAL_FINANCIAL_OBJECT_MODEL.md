# Canonical Financial Object Model

## FinancialExecutionEvent

Required fields:

- event_id
- event_type
- initiating_actor_id
- principal_id
- authority_reference
- authorization_artifact_reference
- requested_action
- affected_resources
- counterparties
- requested_at
- execution_boundary
- jurisdiction_state_reference
- policy_state_reference
- dependency_references
- evidence_requirements
- expected_effect
- current_state_reference

FinancialExecutionEvent represents a proposal for consequential execution.

It does not imply permission.

---

## EconomicActor

Required fields:

- actor_id
- actor_type
- identity_reference
- authority_reference
- delegation_reference
- current_status

Actor capability and actor authority remain separate.

---

## FinancialResource

Required fields:

- resource_id
- resource_type
- ownership_reference
- control_reference
- custody_reference
- current_state_reference
- jurisdiction_reference

Ownership, control, and custody MUST remain separately representable.

---

## SettlementObject

Required fields:

- settlement_id
- execution_event_id
- participating_actor_ids
- obligation_references
- resource_references
- settlement_state
- initiated_at
- updated_at
- finality_reference
- evidence_references

SettlementObject is the canonical state-bearing object for settlement progression.

---

## EconomicState

Required fields:

- state_id
- effective_at
- resource_states
- actor_states
- policy_state
- jurisdiction_state
- dependency_state
- evidence_state

EconomicState represents execution-relevant state at a defined observation time.

---

## EconomicEffect

Required fields:

- effect_id
- execution_event_id
- effect_type
- affected_resources
- before_state_reference
- after_state_reference
- occurred_at
- evidence_references

EffectType must not collapse PartialEffect, CompletedEffect, CompensatingEffect, and ReversalEffect.

---

## CompensationInstruction

Required fields:

- compensation_id
- originating_event_id
- initiating_actor_id
- authority_reference
- requested_effect
- target_state_reference
- requested_at

A CompensationInstruction is a new execution instruction.

The failure or invalidity of an earlier execution does not automatically authorize compensation.

---

## ReversalInstruction

Required fields:

- reversal_id
- originating_event_id
- initiating_actor_id
- authority_reference
- requested_effect
- requested_at

Reversal is a new consequential execution.

It does not erase historical occurrence of the original execution.

---

## EvidenceObject

Required fields:

- evidence_id
- evidence_type
- subject_reference
- generated_at
- provenance_reference
- integrity_reference
- content_reference

Evidence does not create authority.

---

## JurisdictionState

Required fields:

- jurisdiction_state_id
- jurisdiction_id
- effective_at
- governing_authority_reference
- constraint_references
- currentness_reference

Jurisdiction state is execution-relevant state, not descriptive metadata.

---

## LedgerState

Required fields:

- ledger_state_id
- ledger_id
- height_or_sequence
- state_reference
- consensus_state_reference
- finality_reference
- observed_at

Consensus and governance authority remain distinct.

---

## SmartContractReference

Required fields:

- contract_id
- code_hash
- version
- deployed_state_reference
- authority_reference
- governing_policy_reference

Valid code identity does not establish current execution admissibility.

---

## OracleState

Required fields:

- oracle_id
- observed_value_reference
- observed_at
- provenance_reference
- integrity_reference
- currentness_reference

Oracle data is evidence/input.

It is not execution authority.
