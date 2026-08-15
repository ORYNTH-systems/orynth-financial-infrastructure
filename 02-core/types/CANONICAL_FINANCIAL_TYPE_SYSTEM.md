# Canonical Financial Type System

## Governing Rule

Type identity does not imply execution authority.

Membership in any financial type establishes only structural classification.

No actor, artifact, key, instruction, contract, ledger entry, settlement object, or other typed object is execution-admissible solely because it is well-formed or validly typed.

---

## Primitive Identifier Types

### FinancialObjectId
Globally unique identifier for a canonical financial object.

### ActorId
Identifier for an economic actor.

### PrincipalId
Identifier for a principal capable of originating or delegating authority.

### AgentId
Identifier for an autonomous or delegated computational actor.

### AuthorityId
Identifier for an authority reference.

### AuthorizationArtifactId
Identifier for an upstream authorization artifact.

### ExecutionEventId
Identifier for a financially consequential execution event.

### TransitionId
Identifier for a state transition.

### SettlementId
Identifier for a settlement object.

### EvidenceId
Identifier for an evidence object.

### ResourceId
Identifier for a financial resource.

### JurisdictionId
Identifier for a jurisdiction state.

### LedgerId
Identifier for a ledger state domain.

### ContractId
Identifier for a programmable financial contract.

### OracleId
Identifier for an external data authority or oracle state source.

---

## Scalar / Temporal Types

### Timestamp
Execution-relevant time.

### MonetaryAmount
A typed numeric amount associated with a CurrencyUnit.

### CurrencyUnit
Canonical currency or unit denomination.

### Quantity
Typed quantity of a financial or tokenized resource.

### Version
Version identifier for rules, policies, contracts, schemas, or artifacts.

### HashDigest
Cryptographic digest used for identity or integrity comparison.

### Nonce
Single-use replay-resistance value.

---

## Actor Types

### EconomicActor
Any actor capable of participating in a financially consequential state transition.

### Principal
EconomicActor from which authority may originate or be delegated.

### HumanPrincipal
Principal represented by a human operator.

### InstitutionalPrincipal
Principal represented by an institution.

### AutonomousAgent
EconomicActor executing under delegated or derived machine authority.

### Counterparty
EconomicActor occupying an opposing or complementary role in a financial execution.

### ClearingEntity
EconomicActor coordinating or resolving obligations among multiple parties.

### Custodian
EconomicActor controlling or safeguarding a financial resource without automatically owning execution authority over that resource.

### Validator
EconomicActor participating in distributed-ledger validation.

---

## Authority Types

### AuthorityReference
Reference to upstream authority semantics.

### DelegationReference
Reference to a delegation chain.

### AuthorizationArtifactReference
Reference to an upstream authorization artifact.

### ScopeReference
Typed scope limiting permissible execution.

### PolicyReference
Reference to current governing policy.

### GovernanceConstraintReference
Reference to a constraint evaluated during admissibility.

Important:
Possession of an AuthorityReference or AuthorizationArtifactReference does not by itself establish current admissibility.

---

## Financial Resource Types

### FinancialResource
Canonical superclass for economically consequential resources.

### Account
Resource representing an account-state domain.

### CurrencyBalance
Resource representing denominated value.

### Asset
Resource representing an economically transferable asset.

### DigitalAsset
Asset represented through digital or cryptographic state.

### Security
Asset representing a security interest.

### TokenizedAsset
Asset represented through tokenized state.

### Collateral
Resource pledged or bound to an obligation.

### Obligation
Economic duty, debt, claim, or settlement requirement.

---

## Execution Types

### FinancialExecutionEvent
Canonical object representing a proposed financially consequential execution.

### ExecutionBoundary
A consequential boundary at which current admissibility must be evaluated.

### ExecutionAttempt
A specific attempt to cause financial effect.

### SettlementInstruction
Instruction proposing settlement-related state mutation.

### TransferInstruction
Instruction proposing movement of a resource.

### AllocationInstruction
Instruction proposing allocation or reallocation.

### CompensationInstruction
Instruction proposing a new consequential execution intended to compensate for prior effect.

### ReversalInstruction
Instruction proposing a distinct reversal operation.

### ClearingInstruction
Instruction governing clearing-related state resolution.

### ContractExecutionRequest
Request to execute programmable financial logic.

---

## State Types

### EconomicState
Canonical representation of financially relevant current state.

### FinancialResourceState
State of a FinancialResource.

### SettlementState
State associated with a settlement lifecycle.

### LedgerState
State associated with a distributed or replicated ledger.

### JurisdictionState
Current jurisdictionally relevant execution state.

### PolicyState
Current governing policy state.

### CounterpartyState
Current execution-relevant state of a counterparty.

### CustodyState
Current custody/control state.

### ContractState
Current programmable-contract state.

### OracleState
Current external-data state relevant to programmable execution.

### ContinuityState
Reference to continuity classification inherited from upstream architectures.

---

## Effect Types

### EconomicEffect
Observable mutation of economically consequential state.

### NoEffect
No governed economic mutation occurred.

### PartialEffect
Some but not all intended consequential mutation occurred.

### CompletedEffect
The intended consequential mutation completed.

### CompensatingEffect
Effect produced by a separate compensation execution.

### ReversalEffect
Effect produced by a separate reversal execution.

Important:
CompensatingEffect and ReversalEffect are not aliases for erasure of historical execution.

---

## Evidence Types

### EvidenceObject
Canonical evidence associated with execution, refusal, transition, or reconstruction.

### ExecutionEvidence
Evidence that an execution occurred.

### RefusalEvidence
Evidence that execution was governed and refused.

### SettlementEvidence
Evidence associated with settlement state.

### ReconstructionEvidence
Evidence used to reconstruct historical financial state.

### ProvenanceEvidence
Evidence establishing lineage and source relationships.

### ProofOfBlockReference
Reference to canonical POB evidence.

---

## Distributed / Programmable Types

### LedgerTransaction
Canonical transaction representation submitted to a ledger.

### ConsensusState
State describing replicated agreement.

### SmartContractReference
Reference to executable programmable financial logic.

### SmartContractState
Current state associated with a smart contract.

### OracleReference
Reference to an external data source.

### WalletReference
Reference to a digital-asset control container.

### KeyReference
Reference to cryptographic signing capability.

Important:
KeyReference or WalletReference possession does not imply execution authority.

---

## Relationship Types

### Owns
Economic ownership relation.

### Controls
Technical or operational control relation.

### Custodies
Custodial relation.

### DelegatesTo
Authority delegation relation.

### ActsFor
Agency relation.

### SettlesWith
Settlement relation.

### ClearsThrough
Clearing relation.

### DependsOn
Execution dependency relation.

### GovernedBy
Governance relation.

### EvidencedBy
Evidence relation.

### Reconstructs
Historical reconstruction relation.

### TransitionsTo
State-transition relation.

Important:
Owns, Controls, Custodies, PossessesKey, and DelegatesTo are distinct relations.

No relationship shall be treated as semantically equivalent unless explicitly proved.
