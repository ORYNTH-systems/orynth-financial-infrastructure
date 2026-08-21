# FIN-F7-04 — Relation / Predicate Freeze

Status: COMPLETE — PASS

## Canonical family

Cross-Jurisdiction Financial Execution

## Frozen canonical relations / predicates

### F7-R-001 — TechnicalReachAvailable

Determines whether the requested operation is technically reachable or executable across the implicated infrastructure.

### F7-R-002 — JurisdictionalAuthorityActive

Determines whether applicable jurisdictional financial authority exists, is active, scoped, temporally valid, and non-revoked.

### F7-R-003 — AuthoritySourceSupported

Determines whether claimed jurisdictional authority is traceable to a supported external or previously admitted source.

### F7-R-004 — JurisdictionApplicable

Determines whether a claimed authority source actually applies to the specific jurisdictional boundary and requested operation.

### F7-R-005 — AuthorityScopeValid

Determines whether the requested operation falls within the substantive scope of the applicable jurisdictional authority.

### F7-R-006 — AuthorityTemporallyValid

Determines whether the applicable jurisdictional authority is current for the requested operation and time context.

### F7-R-007 — PrincipalJurisdictionResolved

Determines whether the relevant principal jurisdiction is sufficiently identified for the requested operation.

### F7-R-008 — CounterpartyJurisdictionResolved

Determines whether relevant counterparty jurisdiction is sufficiently identified without treating presence as consent.

### F7-R-009 — AssetCustodyJurisdictionResolved

Determines whether asset or custody jurisdiction is sufficiently identified without treating location as authority.

### F7-R-010 — SettlementVenueJurisdictionResolved

Determines whether settlement venue jurisdiction is sufficiently identified without treating venue availability as permission.

### F7-R-011 — DelegationSourceValid

Determines whether cross-jurisdiction delegated authority derives from a valid parent authority source.

### F7-R-012 — DelegationAttenuated

Determines whether delegated cross-jurisdiction authority remains no broader than its parent authority in scope, duration, and jurisdictional applicability.

### F7-R-013 — JurisdictionalRestrictionPresent

Determines whether a jurisdictional prohibition, limitation, condition, or regulatory boundary applies to the requested operation.

### F7-R-014 — BlockingJurisdictionalRestrictionExists

Determines whether an applicable restriction blocks ordinary consequential execution.

### F7-R-015 — JurisdictionalConflictExists

Determines whether jurisdictional authorities, applicability claims, restrictions, or execution requirements conflict.

### F7-R-016 — JurisdictionalEvidenceSufficient

Determines whether evidence is sufficient to evaluate jurisdictional applicability or authority without treating evidence as authority.

### F7-R-017 — AllConsequentialJurisdictionsCovered

Determines whether every consequentially implicated jurisdiction is supported by applicable authority rather than only a subset.

### F7-R-018 — PartialJurisdictionalCoverageExists

Determines whether some but not all consequentially implicated jurisdictions are supported by applicable authority.

### F7-R-019 — JurisdictionalRevalidationRequired

Determines whether changed, stale, conflicting, or incomplete jurisdictional conditions require revalidation.

### F7-R-020 — JurisdictionalReauthorizationRequired

Determines whether authority must be independently re-established due to absence, expiry, revocation, supersession, insufficiency, or inapplicability.

### F7-R-021 — CrossJurisdictionExecutionEvidenceExists

Determines whether evidence shows that technical execution crossed or implicated jurisdictional boundaries.

### F7-R-022 — GovernanceAuthorizationSupported

Determines whether governance authorization is supported after jurisdiction-specific authority, applicability, scope, temporal, restriction, delegation, and conflict checks.

### F7-R-023 — JurisdictionalAlignmentExists

Determines whether technical reach, jurisdictional authority, applicability, and consequential coverage are aligned.

### F7-R-024 — ConsequentialExecutionAdmissible

Determines whether the requested cross-jurisdiction financial action is admissible under all required jurisdictional authority boundaries.

## Frozen predicate separations

- TechnicalReachAvailable != JurisdictionalAuthorityActive
- JurisdictionApplicable != JurisdictionalAuthorityActive
- PrincipalJurisdictionResolved != GovernanceAuthorizationSupported
- CounterpartyJurisdictionResolved != jurisdictional consent
- AssetCustodyJurisdictionResolved != execution authority
- SettlementVenueJurisdictionResolved != jurisdictional permission
- JurisdictionalEvidenceSufficient != authority
- CrossJurisdictionExecutionEvidenceExists != authorization
- PartialJurisdictionalCoverageExists != AllConsequentialJurisdictionsCovered
- JurisdictionalConflictExists != conflict resolution
- DelegationSourceValid != DelegationAttenuated
- GovernanceAuthorizationSupported != technical executability

## Frozen admission predicate rule

ConsequentialExecutionAdmissible MAY evaluate true only where all consequentially implicated jurisdictional boundaries are covered by applicable, scoped, temporally valid, non-revoked authority; required delegation constraints are satisfied; no blocking jurisdictional restriction applies; and no unresolved blocking jurisdictional conflict exists.

Technical reach, successful routing, settlement availability, asset presence, custody location, counterparty location, or execution evidence SHALL NOT substitute for any missing jurisdictional authority predicate.

Partial jurisdictional coverage SHALL NOT satisfy AllConsequentialJurisdictionsCovered.

## Multi-jurisdiction predicate rule

For a request implicating jurisdictions J_1 ... J_n, authority applicability MUST be evaluated independently for each consequential jurisdictional boundary.

A request SHALL NOT become admissible merely because one jurisdiction authorizes an operation that is consequential in another jurisdiction.

## Freeze control

The F7 relation / predicate vocabulary is frozen.

Decision functions, transition functions, invariants, proof obligations, runtime components, tests, and publication surfaces remain unfrozen.

## Next

FIN-F7-05 — DECISION / TRANSITION SEMANTICS FREEZE
