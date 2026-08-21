# FIN-F8-04 — Relation / Predicate Freeze

Status: COMPLETE — PASS

## Canonical family

Autonomous Economic Agency and Machine Financial Authority

## Frozen canonical predicate registry

### F8-R-001 — AutonomousCapabilityAvailable

Autonomous financial action capability is currently available.

### F8-R-002 — EconomicPrincipalValid

A valid economic principal has been resolved for the requested consequential financial action.

### F8-R-003 — PrincipalIdentityBound

The resolved economic principal is bound to a current and valid principal identity.

### F8-R-004 — AutonomousAgentIdentityValid

The acting autonomous agent identity is current, identified, and valid.

### F8-R-005 — MachineFinancialAuthorityActive

Machine financial authority is active for the requested action.

### F8-R-006 — MachineAuthoritySourceSupported

The machine authority derives from a supported valid authority source.

### F8-R-007 — MachineAuthorityScopeValid

The requested action is inside the explicit scope of machine authority.

### F8-R-008 — MachineAuthorityTemporallyValid

Machine authority is current and temporally valid.

### F8-R-009 — MachineAuthorityNotRevoked

Machine authority is not revoked, expired, superseded, or otherwise invalid.

### F8-R-010 — DelegationSourceValid

Delegated machine authority derives from a valid parent authority.

### F8-R-011 — DelegationAttenuated

Delegated machine authority does not exceed the scope, duration, or authority of its parent.

### F8-R-012 — SubdelegationSourceValid

Autonomous subdelegation derives from a valid delegated authority chain.

### F8-R-013 — SubdelegationAttenuated

Autonomous subdelegation does not amplify authority beyond its parent delegation.

### F8-R-014 — TechnicalControlAvailable

Account, wallet, key, credential, or execution-surface control is technically available.

### F8-R-015 — MachineAuthorityEvidenceSufficient

Evidence supporting machine authority and principal attribution is sufficient and current.

### F8-R-016 — MachineActionEvidenceExists

Evidence exists that the autonomous system proposed, initiated, attempted, or completed the financial action.

### F8-R-017 — PrincipalContinuityPreserved

The economic principal relation remains continuous across relevant system or identity changes.

### F8-R-018 — AgentReplacementDetected

An autonomous agent, model, runtime, identity, credential, or implementation replacement has been detected.

### F8-R-019 — AuthorityRevalidationRequired

Existing machine authority requires revalidation before ordinary admission.

### F8-R-020 — AuthorityReauthorizationRequired

Machine authority must be independently re-established before ordinary admission.

### F8-R-021 — MachineAuthorityConflictExists

A conflict exists among principal attribution, identity binding, authority source, scope, temporal validity, delegation, revocation, or observed execution.

### F8-R-022 — GovernanceAuthorizationSupported

The requested autonomous financial action is supported by governance authorization.

### F8-R-023 — AutonomousAuthorityAligned

Capability, principal attribution, identity binding, authority, scope, temporal validity, delegation, revocation state, and evidence are aligned.

### F8-R-024 — CapabilityWithoutAuthorityExists

Autonomous financial capability is available while valid machine financial authority is absent or unusable.

### F8-R-025 — AuthorityWithoutCapabilityExists

Valid machine financial authority exists while autonomous execution capability is unavailable.

### F8-R-026 — PrincipalUnresolved

No valid economic principal has yet been resolved for the requested consequential action.

### F8-R-027 — IdentityMisbound

The autonomous agent identity, principal identity, or authority identity is incorrectly or ambiguously bound.

### F8-R-028 — PersistentOperationAuthorized

Persistent autonomous operation remains within current, scoped, temporally valid, non-revoked authority.

### F8-R-029 — ReplacementAuthorityInherited

Authority inheritance across agent or runtime replacement has been independently established rather than presumed.

### F8-R-030 — ConsequentialExecutionAdmissible

The requested autonomous financial action is governance-admissible under all frozen F8 authority conditions.

## Frozen predicate semantics

- AutonomousCapabilityAvailable does not imply MachineFinancialAuthorityActive.
- TechnicalControlAvailable does not imply EconomicPrincipalValid.
- TechnicalControlAvailable does not imply MachineFinancialAuthorityActive.
- AutonomousAgentIdentityValid does not imply EconomicPrincipalValid.
- PrincipalIdentityBound does not itself constitute machine financial authority.
- MachineActionEvidenceExists does not imply GovernanceAuthorizationSupported.
- MachineAuthorityEvidenceSufficient supports evaluation but does not self-create authority.
- MachineFinancialAuthorityActive without MachineAuthoritySourceSupported is insufficient for ordinary admission.
- MachineFinancialAuthorityActive without MachineAuthorityScopeValid is insufficient for ordinary admission.
- MachineFinancialAuthorityActive without MachineAuthorityTemporallyValid is insufficient for ordinary admission.
- revoked, expired, superseded, or invalid authority cannot satisfy MachineAuthorityNotRevoked.
- DelegationSourceValid without DelegationAttenuated is insufficient for ordinary admission.
- SubdelegationSourceValid without SubdelegationAttenuated is insufficient for ordinary admission.
- AgentReplacementDetected does not imply ReplacementAuthorityInherited.
- PrincipalContinuityPreserved does not imply unchanged machine authority scope.
- PersistentOperationAuthorized must be re-evaluable against current authority state.
- CapabilityWithoutAuthorityExists must remain distinguishable from AuthorityWithoutCapabilityExists.
- AutonomousAuthorityAligned is a classification and does not constitute an authority source.
- ConsequentialExecutionAdmissible requires authority support and cannot derive from execution success alone.

## Frozen admission predicate

ConsequentialExecutionAdmissible(q) requires, where applicable:

- EconomicPrincipalValid
- PrincipalIdentityBound
- AutonomousAgentIdentityValid
- MachineFinancialAuthorityActive
- MachineAuthoritySourceSupported
- MachineAuthorityScopeValid
- MachineAuthorityTemporallyValid
- MachineAuthorityNotRevoked
- DelegationSourceValid and DelegationAttenuated when delegation is used
- SubdelegationSourceValid and SubdelegationAttenuated when subdelegation is used
- MachineAuthorityEvidenceSufficient
- no unresolved MachineAuthorityConflictExists
- no unresolved AuthorityRevalidationRequired
- no unresolved AuthorityReauthorizationRequired
- GovernanceAuthorizationSupported

Autonomous capability, tool access, account control, wallet control, key possession, model output, prior execution, or persistent operation cannot substitute for these authority predicates.

## Replacement rule

ReplacementAuthorityInherited SHALL be false by default when AgentReplacementDetected is true unless authority continuity is independently established.

Agent replacement, model replacement, runtime migration, credential rotation, or wallet replacement SHALL NOT bootstrap authority continuity.

## Persistence rule

PersistentOperationAuthorized SHALL require current authority evaluation and SHALL NOT be inferred from prior successful or authorized execution.

## Freeze control

The F8 relation / predicate vocabulary is frozen.

Decisions, transitions, invariants, proof obligations, runtime components, tests, and publication surfaces remain unfrozen.

## Next

FIN-F8-05 — DECISION / TRANSITION SEMANTICS FREEZE
