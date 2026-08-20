# FIN-F6-01B — Programmable-Finance / Smart-Contract Authority Boundary Freeze

Status: COMPLETE — PASS

## Canonical family

Smart-Contract and Programmable Financial Authority

## Frozen problem boundary

F6 governs the distinction between programmable or smart-contract execution capability and the governance authority required to admit consequential financial execution.

The primary F6 question is not whether deployed code can execute, whether a contract invocation is technically valid, whether a trigger condition is satisfied, or whether a blockchain or ledger accepts the resulting state transition.

The primary question is whether the requested programmable financial action is supported by current, applicable, scoped, non-revoked governance authority.

## Frozen core separation

executable code != governance authority

Executable smart-contract logic, deployed code, automation logic, contract ownership, administrator capability, upgrade capability, oracle input, condition satisfaction, or ledger acceptance SHALL NOT by itself constitute governance authority.

## Frozen inherited separations

- capability != authority
- execution capability != governance authority
- evidence != authority
- consensus != authority
- key possession != authority
- valid cryptographic signature != valid governance authorization
- ledger inclusion != authority
- ledger representation != underlying financial truth
- delegation attenuates; it does not amplify

## Frozen F6 non-collapse conditions

- deployed code != authority
- deterministic execution != admissibility
- contract invocation != authorized financial action
- programmable condition satisfaction != financial authorization
- oracle input != authority
- oracle truth assertion != governance authorization
- on-chain acceptance != governance admissibility
- upgrade capability != authority to alter governance boundaries
- administrator capability != governance authority
- immutable code != irrevocable governance mandate
- smart-contract state != authoritative economic truth
- technical correctness != authority validity
- automation != principal authority

## Frozen inclusion boundary

- smart-contract execution authority
- programmable financial execution
- deployment and activation authority
- contract invocation authority
- automated trigger execution
- condition-bound financial execution
- oracle-mediated execution
- upgrade and mutation authority
- administrator and privileged contract controls
- programmable delegation
- pause, resume, kill, and emergency-control authority
- mutable versus immutable contract authority boundaries
- on-chain execution versus governance admissibility
- contract-state representation versus authoritative financial state
- technical execution success versus authorized consequential effect

## Frozen exclusion boundary

- F1 partial settlement, compensation, reversal, and reconciliation semantics as primary subject
- F2 distributed consensus and multiparty authority semantics as primary subject
- F3 obligation finality, custody validity, and consequential closure as primary subject
- F4 ledger-state finality, record integrity, and reconstruction as primary subject
- F5 cryptographic key possession and delegated cryptographic authority as primary subject
- F7 cross-jurisdiction financial execution as primary subject
- F8 autonomous economic principal authority as primary subject
- general smart-contract software security except where it changes authority semantics
- reentrancy as a standalone software-security subject
- gas optimization
- token economics
- consensus protocol correctness

## Frozen authority boundary

Programmable financial authority MUST be attributable to an external or previously admitted authority source.

A contract, program, automation mechanism, oracle, administrator role, deployment action, invocation surface, or upgrade capability MUST NOT self-bootstrap governance authority.

Any delegated programmable authority MUST remain source-bound, scoped, temporally valid, non-revoked, and attenuated relative to its parent authority.

Successful technical execution MUST remain distinguishable from governance authorization and consequential financial admissibility.

## Cross-family inheritance

F6 inherits F5 cryptographic-authority distinctions without redefining key possession, signature validity, or custody authority as primary F6 subjects.

F6 inherits F4 ledger-state distinctions without treating contract or ledger state as constitutive financial truth.

F6 inherits F2 consensus distinctions without treating network acceptance as authority.

F6 leaves cross-jurisdiction authority to F7 and autonomous economic principal status to F8.

## Freeze control

The F6 problem boundary is frozen.

Canonical objects, state domains, predicates, decisions, transitions, invariants, proof obligations, runtime components, tests, and publication surfaces remain unfrozen.

## Next

FIN-F6-02 — CANONICAL OBJECT / TYPE FREEZE
