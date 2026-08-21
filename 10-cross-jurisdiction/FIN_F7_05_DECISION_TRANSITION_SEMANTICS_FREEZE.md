# FIN-F7-05 — Decision / Transition Semantics Freeze

Status: COMPLETE — PASS

## Canonical family

Cross-Jurisdiction Financial Execution

## Frozen decision outcomes

- F7-ADMIT
- F7-BLOCK
- F7-DEFER
- F7-REVALIDATE
- F7-REAUTHORIZE

## Frozen decision function

D_7 : Psi7 x Q7 -> {F7-ADMIT, F7-BLOCK, F7-DEFER, F7-REVALIDATE, F7-REAUTHORIZE}

## Frozen transition function

Delta_7 : Psi7 x Q7 ->partial Psi7

## Frozen semantic separation

predicate / jurisdictional fact != decision outcome != transition existence != resulting F7 state

A predicate may establish a jurisdictional fact relevant to decision-making without itself constituting an admission decision or causing a consequential state transition.

## F7-ADMIT rule

D_7(Psi7,q) MAY equal F7-ADMIT only if all of the following hold for the requested consequential target:

1. required jurisdictional authority sources are supported;
2. authority is active, scoped, temporally valid, non-revoked, and jurisdictionally applicable;
3. every consequentially implicated jurisdiction is independently covered;
4. delegated authority, where used, is source-valid and attenuated;
5. no blocking jurisdictional restriction applies;
6. no unresolved blocking jurisdictional conflict exists;
7. required jurisdictional evidence is sufficient for the decision;
8. no revalidation requirement remains unresolved;
9. no reauthorization requirement remains unresolved;
10. operation-specific admission predicates are satisfied.

Technical reach MAY be present or absent independently of authority. Technical reach alone SHALL NOT produce F7-ADMIT.

## F7-BLOCK rule

D_7(Psi7,q) MUST equal F7-BLOCK where any blocking condition applies, including:

- an applicable jurisdictional authority source is invalid, revoked, expired, or unsupported;
- requested execution exceeds authority scope;
- required jurisdictional applicability is false;
- partial jurisdictional coverage exists where complete coverage is required;
- a blocking jurisdictional restriction applies;
- an unresolved blocking jurisdictional conflict exists;
- delegation is nonattenuated or unsupported;
- the request attempts to universalize authority from one jurisdiction into another;
- technical location, network reach, custody location, settlement venue, or counterparty presence is offered as a substitute for authority.

## F7-DEFER rule

D_7(Psi7,q) MAY equal F7-DEFER where required jurisdictional facts or evidence remain unresolved but no presently established blocking condition independently requires F7-BLOCK.

F7-DEFER SHALL NOT be treated as admission.

## F7-REVALIDATE rule

D_7(Psi7,q) MUST equal F7-REVALIDATE where previously established jurisdictional applicability, evidence, scope, restriction, or conflict state is stale, changed, incomplete, or requires renewed evaluation before execution.

Revalidation evaluates whether existing authority remains applicable; it does not create new authority.

## F7-REAUTHORIZE rule

D_7(Psi7,q) MUST equal F7-REAUTHORIZE where applicable authority is absent, expired, revoked, superseded, insufficient, or jurisdictionally inapplicable and the requested action requires newly established authority.

Reauthorization MUST derive from a valid external or previously admitted authority source and MUST NOT be self-created by technical reach or prior execution.

## Frozen transition existence rule

Delta_7(Psi7,q) is defined for the requested consequential target only if:

1. D_7(Psi7,q) = F7-ADMIT;
2. all operation-specific transition preconditions are satisfied;
3. no blocking invariant applies at transition time;
4. the resulting transition remains inside every admitted jurisdictional scope and temporal boundary;
5. required jurisdictional authority and execution evidence is preserved.

F7-ADMIT is necessary but not sufficient for transition existence.

## Undefined transition rule

For the requested consequential target:

- F7-BLOCK => Delta_7 undefined
- F7-DEFER => Delta_7 undefined
- F7-REVALIDATE => Delta_7 undefined
- F7-REAUTHORIZE => Delta_7 undefined

These outcomes MUST NOT be collapsed into execution failure. They are governance decision states with distinct semantics.

## Frozen multi-jurisdiction transition rule

A single technically executable operation that crosses multiple jurisdictional boundaries MUST NOT create one aggregate transition authorization.

Each consequentially implicated jurisdiction MUST remain independently satisfied at decision time and transition time.

Authority established for J_i SHALL NOT be inferred for J_j where i != j.

Partial jurisdictional coverage MUST NOT permit a consequential transition requiring complete coverage.

## No retroactive authorization

Successful technical execution, settlement, ledger inclusion, custody transfer, or cross-border completion MUST NOT retroactively establish jurisdictional admissibility.

Execution evidence MAY establish that an action occurred while the corresponding governance decision remains F7-BLOCK, F7-DEFER, F7-REVALIDATE, or F7-REAUTHORIZE.

## Freeze control

The F7 decision / transition semantics are frozen.

Invariants, proof obligations, formal discharge, runtime components, adversarial tests, and publication surfaces remain unfrozen.

## Next

FIN-F7-06 — INVARIANT DISCOVERY / FREEZE
