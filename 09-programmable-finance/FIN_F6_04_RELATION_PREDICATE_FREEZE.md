# FIN-F6-04 — Relation / Predicate Freeze

Status: COMPLETE — PASS

## Canonical family

Smart-Contract and Programmable Financial Authority

## Frozen canonical relations / predicates

### F6-R-001 — ProgrammableExecutionCapabilityAvailable

Determines whether the subject or system currently possesses the technical capability required to perform the requested programmable financial operation.

### F6-R-002 — ContractOperational

Determines whether the relevant smart contract or programmable-finance program is deployed and operational for the requested action.

### F6-R-003 — ProgrammableAuthorityActive

Determines whether applicable programmable financial authority exists, is active, scoped, temporally valid, non-revoked, and non-superseded.

### F6-R-004 — AuthoritySourceSupported

Determines whether the claimed programmable financial authority is traceable to a supported external or previously admitted authority source.

### F6-R-005 — AuthorityScopeValid

Determines whether the requested programmable financial action falls within the scope of the applicable authority.

### F6-R-006 — AuthorityTemporallyValid

Determines whether the applicable programmable authority is current for the requested operation and temporal context.

### F6-R-007 — DelegationAttenuated

Determines whether delegated programmable authority remains no broader than its parent authority in scope, duration, conditions, and consequence.

### F6-R-008 — InvocationTechnicallyValid

Determines whether the contract invocation, function call, trigger, or programmable request is technically valid.

### F6-R-009 — ProgrammableConditionSatisfied

Determines whether the relevant programmable condition, trigger, predicate, event, threshold, or schedule is technically satisfied.

### F6-R-010 — OracleInputUsable

Determines whether required oracle input is present, current, valid, and usable as data without treating it as authority.

### F6-R-011 — PrivilegedControlAvailable

Determines whether an administrator, owner, pause, resume, emergency, upgrade, or equivalent privileged control capability exists.

### F6-R-012 — PrivilegedControlAuthorized

Determines whether use of a privileged contract control is independently supported by applicable governance authority.

### F6-R-013 — UpgradeMutationAuthorized

Determines whether a proposed contract upgrade, mutation, implementation change, or authority-relevant configuration change is independently authorized.

### F6-R-014 — GovernanceAuthorizationSupported

Determines whether the requested programmable financial action is supported by current applicable governance authority.

### F6-R-015 — ContractStateCorroborated

Determines whether observed contract state is corroborated by applicable evidence without treating contract state as constitutive financial truth.

### F6-R-016 — ProgrammableAuthorityConflictExists

Determines whether observed code capability, execution, invocation, oracle input, privileged control, contract state, or mutation conflicts with applicable governance authority.

### F6-R-017 — ProgrammableGovernanceAligned

Determines whether observed programmable-finance capability and action are aligned with current governance authority.

### F6-R-018 — ExecutionEvidenceExists

Determines whether evidence exists that programmable execution technically occurred.

### F6-R-019 — AuthorityEvidenceExists

Determines whether evidence exists supporting programmable governance authority independently of execution evidence.

### F6-R-020 — ConsequentialExecutionAdmissible

Determines whether a technically possible or completed programmable action is admissible as consequential financial execution.

## Frozen predicate separations

- ProgrammableExecutionCapabilityAvailable does not imply ProgrammableAuthorityActive
- ContractOperational does not imply GovernanceAuthorizationSupported
- InvocationTechnicallyValid does not imply ConsequentialExecutionAdmissible
- ProgrammableConditionSatisfied does not imply GovernanceAuthorizationSupported
- OracleInputUsable does not imply GovernanceAuthorizationSupported
- PrivilegedControlAvailable does not imply PrivilegedControlAuthorized
- UpgradeMutationAuthorized MUST be established independently of upgrade capability
- ContractStateCorroborated does not constitute authority
- ExecutionEvidenceExists does not imply AuthorityEvidenceExists
- ProgrammableGovernanceAligned is a classification predicate, not an authority source

## Predicate authority boundary

No F6 predicate may convert technical execution capability, deployment, invocation validity, condition satisfaction, oracle input, privileged control, ledger acceptance, or contract state into governance authority by implication.

GovernanceAuthorizationSupported and ConsequentialExecutionAdmissible MUST remain independently evaluable from technical execution predicates.

## Cross-family inheritance

F6 predicates inherit F5 cryptographic authority requirements, F4 ledger-state distinctions, and F2 consensus distinctions without collapsing those inherited technical facts into programmable financial authority.

## Freeze control

The F6 relation / predicate vocabulary is frozen.

Decision functions, transition functions, invariants, proof obligations, runtime components, tests, and publication surfaces remain unfrozen.

## Next

FIN-F6-05 — DECISION / TRANSITION SEMANTICS FREEZE
