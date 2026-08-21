# FIN-F7-02 — Canonical Object / Type Freeze

Status: COMPLETE — PASS

## Canonical family

Cross-Jurisdiction Financial Execution

## Frozen canonical object registry

### F7-O-001 — Jurisdictional Execution Request

A typed request for consequential financial execution that may implicate one or more jurisdictional authority boundaries.

### F7-O-002 — Jurisdictional Authority

A source-bound, scoped, temporally valid authority grant applicable within a defined jurisdictional domain.

### F7-O-003 — Jurisdictional Authority Source

The external or previously admitted basis from which jurisdictional financial authority is derived.

### F7-O-004 — Jurisdiction Domain

A typed jurisdictional domain relevant to the requested operation without treating physical or technical location as constitutive authority.

### F7-O-005 — Principal Jurisdiction

A typed jurisdictional association relevant to the economic principal involved in the requested financial action.

### F7-O-006 — Counterparty Jurisdiction

A typed jurisdictional association relevant to a counterparty without treating presence as consent or authority.

### F7-O-007 — Asset / Custody Jurisdiction

A typed jurisdictional association arising from asset location, situs, custody, or custody infrastructure without treating that association as authority.

### F7-O-008 — Settlement Venue Jurisdiction

A typed jurisdictional association arising from a settlement venue or execution venue without treating venue availability as permission.

### F7-O-009 — Cross-Jurisdiction Delegation

A source-bound, scoped, temporally valid, attenuated delegation whose applicability may span explicitly identified jurisdictional domains.

### F7-O-010 — Jurisdictional Applicability Record

A typed record describing whether an authority source is applicable to a specific jurisdictional boundary and requested financial action.

### F7-O-011 — Jurisdictional Restriction

A typed prohibition, limitation, condition, or regulatory boundary that constrains consequential financial execution.

### F7-O-012 — Jurisdictional Conflict

A typed conflict between jurisdictional authorities, restrictions, applicability claims, or execution requirements.

### F7-O-013 — Jurisdictional Evidence

Evidence relevant to jurisdictional applicability, authority, restriction, or conflict without constituting authority by itself.

### F7-O-014 — Cross-Jurisdiction Execution Evidence

Evidence that a financial operation crossed or implicated jurisdictional boundaries without establishing that those boundaries were authorized.

### F7-O-015 — Jurisdictional Revalidation Requirement

A typed requirement to re-evaluate applicability, authority, evidence, or restriction before consequential financial execution may continue.

### F7-O-016 — Jurisdictional Reauthorization Requirement

A typed requirement to independently re-establish authority for a requested action where existing authority is absent, expired, revoked, superseded, insufficient, or jurisdictionally inapplicable.

## Frozen type distinctions

- technical reach != jurisdictional authority
- cross-border executability != cross-border authorization
- jurisdiction domain != jurisdictional authority
- physical location != authority
- principal jurisdiction != principal authority
- counterparty presence != jurisdictional consent
- asset location != execution authority
- custody jurisdiction != custody authority
- settlement venue != jurisdictional permission
- jurisdictional applicability record != authority source
- jurisdictional restriction != authority
- jurisdictional evidence != jurisdictional authority
- execution evidence != jurisdictional authorization evidence
- one jurisdiction's authority != universal authority
- cross-jurisdiction delegation != unconstrained delegation
- conflict detection != conflict resolution
- regulatory applicability != self-executing authority
- compliance capability != authority to execute
- jurisdictional revalidation != reauthorization
- technical accessibility != legal jurisdiction

## Canonical type boundary

F7 separates technical or operational cross-jurisdiction reach from the jurisdictional authority required to admit consequential financial execution.

No F7 object may self-create, self-expand, or universalize jurisdictional authority merely because an actor, asset, counterparty, custodian, settlement venue, network, contract, or technical system is present or reachable in a jurisdiction.

Each consequentially implicated jurisdiction MUST remain independently representable as an authority domain.

## Cross-family inheritance

F7 inherits:

- F2 consensus and multiparty-authority distinctions;
- F4 ledger-state and record-truth distinctions;
- F5 cryptographic possession and custody-authority distinctions;
- F6 programmable-finance authority distinctions;
- architecture-wide capability / authority separation;
- source-bound delegation and attenuation requirements.

F7 does not redefine settlement semantics, obligation finality, custody authority, programmable authority, or autonomous economic principal status.

## Freeze control

The F7 canonical object and type vocabulary is frozen.

State domains, predicates, decisions, transitions, invariants, proof obligations, runtime components, tests, and publication surfaces remain unfrozen.

## Next

FIN-F7-03 — STATE / CLASSIFICATION ALGEBRA FREEZE
