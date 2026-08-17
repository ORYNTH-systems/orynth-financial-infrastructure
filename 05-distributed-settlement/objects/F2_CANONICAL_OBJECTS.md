# F2 Canonical Distributed Settlement Objects

## Actor Classes

Participant

AuthorityHolder

ExecutionParticipant

Validator

Attestor

Observer

Coordinator

SettlementAgent

ClearingParticipant

Custodian

Operator

ExternalAuthority

JurisdictionalAuthority

These actor classes are roles, not automatic authority grants.

Role != Authority.

## Core Objects

DistributedSettlementProposal

ParticipantSet

RequiredParticipantSet

AuthoritySet

AuthorityRequirement

AgreementRecord

ConsensusObservation

ConsensusCertificate

Commitment

CommitmentSet

ExecutionLeg

ExecutionLegSet

DependencyEdge

AtomicityRequirement

OrderingConstraint

OccurrenceObservation

DistributedExecutionTrace

DistributedEvidenceSet

FinalityClaim

FinalityProfile

FinalityClassification

ConflictRecord

ReconciliationRequirement

## F2 Ownership

F2 owns the distributed structure and relationship among these objects.

It does not automatically own the underlying authority semantics,
economic-effect semantics, or continuity semantics inherited from prior
architecture.
