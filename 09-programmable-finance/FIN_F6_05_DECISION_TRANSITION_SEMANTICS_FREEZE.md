# FIN-F6-05 — Decision / Transition Semantics Freeze

Status: COMPLETE — PASS

## Canonical family

Smart-Contract and Programmable Financial Authority

## Frozen decision outcomes

- F6-ADMIT
- F6-BLOCK
- F6-DEFER
- F6-REVALIDATE
- F6-REAUTHORIZE

## Frozen decision function

D_6 : Psi6 x Q6 -> {F6-ADMIT, F6-BLOCK, F6-DEFER, F6-REVALIDATE, F6-REAUTHORIZE}

D_6 is total on admissible F6 requests.

## Frozen transition function

Delta_6 : Psi6 x Q6 ->partial Psi6

Delta_6 is partial.

## Frozen semantic separation

predicate / semantic fact != decision outcome != transition existence != resulting F6 state

Technical programmability, contract deployment, invocation validity, condition satisfaction, oracle usability, privileged control, successful execution, or ledger acceptance do not independently establish an F6 decision outcome.

## F6-ADMIT

F6-ADMIT means the requested programmable financial operation is governance-admissible under the current F6 state and request.

F6-ADMIT requires, as applicable:

- programmable execution capability available;
- relevant contract operational;
- programmable authority active;
- authority source supported;
- authority scope valid;
- authority temporally valid;
- delegation attenuated;
- invocation technically valid;
- required programmable condition satisfied;
- required oracle input usable;
- privileged control independently authorized when applicable;
- upgrade or mutation independently authorized when applicable;
- no blocking programmable-authority conflict;
- governance authorization supported;
- consequential execution admissible.

F6-ADMIT does not mean that the target transition must exist. Operation-specific transition preconditions remain independently necessary.

## F6-BLOCK

F6-BLOCK means the requested consequential programmable financial operation is prohibited under the current F6 state.

If D_6(Psi6,q) = F6-BLOCK, the blocked target transition is undefined.

Technical executability MUST NOT override F6-BLOCK.

## F6-DEFER

F6-DEFER means the request cannot yet be decided because required evidence, state, or dependency is unresolved without establishing a definitive authorization failure.

If D_6(Psi6,q) = F6-DEFER, the requested target transition is undefined.

## F6-REVALIDATE

F6-REVALIDATE means previously usable evidence, authority, contract state, oracle input, scope, or temporal applicability requires renewed validation before the ordinary target transition may proceed.

If D_6(Psi6,q) = F6-REVALIDATE, the ordinary target transition is undefined until revalidation succeeds and a new decision is produced.

## F6-REAUTHORIZE

F6-REAUTHORIZE means valid authority for the requested programmable financial operation is absent, expired, revoked, superseded, insufficient, or otherwise not currently established.

If D_6(Psi6,q) = F6-REAUTHORIZE, the ordinary target transition is undefined until authority is independently re-established from a valid authority source.

Execution capability, administrator capability, upgrade capability, contract ownership, key possession, oracle input, condition satisfaction, or successful code execution MUST NOT satisfy reauthorization by themselves.

## Frozen transition existence rule

Delta_6(Psi6,q) is defined for a requested consequential target operation only if:

1. D_6(Psi6,q) = F6-ADMIT;
2. operation-specific transition preconditions are satisfied;
3. no blocking invariant is violated;
4. the transition remains inside the admitted scope and temporal boundary;
5. required execution and authority evidence can be preserved.

## Frozen programmable-finance authority rules

- deployed code cannot self-authorize execution;
- deterministic execution cannot convert BLOCK into ADMIT;
- condition satisfaction cannot convert absent authority into ADMIT;
- oracle verification cannot convert data validity into authority;
- privileged control cannot convert capability into governance authority;
- successful contract execution cannot retroactively establish admissibility;
- ledger acceptance cannot retroactively establish authority;
- contract immutability cannot eliminate revalidation or reauthorization requirements imposed by governance state;

## Decision / execution separation

A technically executed smart-contract action may exist as execution evidence while remaining governance-inadmissible.

Execution evidence MUST NOT be interpreted as proof that F6-ADMIT was validly produced.

## Cross-family inheritance

F6 decision semantics inherit F5 cryptographic-authority constraints, F4 ledger-state distinctions, F3 consequential closure distinctions, and F2 consensus boundaries without allowing any inherited technical fact to substitute for F6 governance authorization.

## Freeze control

The F6 decision / transition semantics are frozen.

Invariants, proof obligations, runtime components, tests, adversarial surfaces, and publication surfaces remain unfrozen.

## Next

FIN-F6-06 — INVARIANT DISCOVERY / FREEZE
