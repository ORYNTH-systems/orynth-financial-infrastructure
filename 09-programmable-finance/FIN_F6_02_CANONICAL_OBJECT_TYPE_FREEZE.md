# FIN-F6-02 — Canonical Object / Type Freeze

Status: COMPLETE — PASS

## Canonical family

Smart-Contract and Programmable Financial Authority

## Frozen canonical object registry

### F6-O-001 — Programmable Financial Execution Capability

A typed capability of code, a contract, workflow, runtime, or automation mechanism to perform or initiate a financial operation.

### F6-O-002 — Smart-Contract Program

A deployed or deployable executable program whose technical behavior may affect financial state without itself constituting governance authority.

### F6-O-003 — Programmable Financial Authority

A source-bound, scoped, temporally valid, non-revoked authority grant permitting specified programmable financial actions.

### F6-O-004 — Programmable Authority Source

The external or previously admitted authority basis from which programmable financial authority is derived.

### F6-O-005 — Contract Invocation Request

A typed request to invoke, execute, trigger, call, or otherwise activate a programmable financial operation.

### F6-O-006 — Deployment / Activation Action

A typed action that deploys, activates, enables, or places executable programmable-finance logic into an operational state.

### F6-O-007 — Programmable Condition

A typed condition, predicate, threshold, event, schedule, or trigger whose satisfaction may permit technical execution but does not itself establish financial authorization.

### F6-O-008 — Oracle Input

A typed external or internal data input consumed by programmable financial logic without treating data provision or asserted truth as governance authority.

### F6-O-009 — Privileged Contract Control

A typed administrator, owner, pause, resume, kill, mutation, emergency, or equivalent privileged control capability.

### F6-O-010 — Contract Upgrade / Mutation Action

A typed action that changes executable code, parameters, implementation references, authority-relevant configuration, or operational contract behavior.

### F6-O-011 — Programmable Execution Evidence

Evidence that a contract, program, trigger, oracle-mediated action, or automated financial execution technically occurred.

### F6-O-012 — Programmable Authority Evidence

Evidence relevant to whether a programmable financial action was supported by applicable governance authority independently of execution success.

### F6-O-013 — Contract State Representation

A typed representation of contract or programmable-finance state that SHALL NOT be treated as constitutive authoritative economic truth.

### F6-O-014 — Programmable Authority Conflict

A typed conflict between observed executable capability, invocation, contract state, privileged control, or successful execution and the applicable governance authority.

## Frozen type distinctions

- programmable execution capability != governance authority
- smart-contract program != programmable financial authority
- deployed code != authority
- deployment != authorization
- activation != authorization
- contract invocation != authorized financial action
- deterministic execution != admissibility
- programmable condition satisfaction != financial authorization
- oracle input != authority
- oracle assertion != governance authorization
- privileged contract control != governance authority
- upgrade capability != authority to alter governance boundaries
- contract mutation != authority renewal
- programmable execution evidence != programmable authority evidence
- successful execution != authorized consequential effect
- on-chain acceptance != governance admissibility
- immutable code != irrevocable governance mandate
- contract state representation != authoritative economic truth
- technical correctness != authority validity
- automation != principal authority

## Canonical type boundary

F6 separates executable programmable-finance capability from the governance authority required to admit consequential financial execution.

No F6 object may self-create, self-extend, self-recover, or self-expand governance authority merely because code exists, executes deterministically, satisfies a trigger, receives oracle data, holds privileged control, or is accepted by a ledger.

## Cross-family inheritance

F6 inherits:

- F2 consensus and multiparty-authority distinctions;
- F4 ledger-state and record-truth distinctions;
- F5 key-possession, signature-validity, and delegated cryptographic-authority distinctions;
- architecture-wide capability / authority separation;
- source-bound delegation and attenuation requirements.

F6 does not redefine settlement semantics, obligation finality, custody authority, ledger truth, jurisdictional authority, or autonomous economic principal status.

## Freeze control

The F6 canonical object and type vocabulary is frozen.

State domains, predicates, decisions, transitions, invariants, proof obligations, runtime components, tests, and publication surfaces remain unfrozen.

## Next

FIN-F6-03 — STATE / CLASSIFICATION ALGEBRA FREEZE
