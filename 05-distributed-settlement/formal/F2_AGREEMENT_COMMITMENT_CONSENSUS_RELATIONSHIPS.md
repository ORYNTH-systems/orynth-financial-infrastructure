# F2 Agreement / Commitment / Consensus Relationship Map

The following objects are independent unless an explicit profile binds
them.

Agreement != Commitment

Agreement != Consensus

Commitment != Consensus

Agreement != Authority

Commitment != Authority

Consensus != Authority

Agreement != Admissibility

Commitment != Admissibility

Consensus != Admissibility

Agreement != Execution

Commitment != Execution

Consensus != Execution

Agreement != Finality

Commitment != Finality

Consensus != Finality

## Possible Relationships

A profile MAY require agreement before commitment.

A profile MAY require commitment before consensus.

A profile MAY derive a consensus observation from agreement records.

A profile MAY require commitments from a consensus-defined set.

None of those profile relationships erase the semantic distinction among
the objects.

## Fail-Closed Rule

Where the active profile does not explicitly define a relationship,
the system SHALL NOT infer one.
