# FIN-F8-05 — Decision / Transition Semantics Freeze

Status: COMPLETE — PASS

## Canonical family

Autonomous Economic Agency and Machine Financial Authority

## Frozen decision outcomes

- F8-ADMIT
- F8-BLOCK
- F8-DEFER
- F8-REVALIDATE
- F8-REAUTHORIZE
- F8-REIDENTIFY

## Frozen decision function

D_8 : Psi8 x Q8 -> {F8-ADMIT, F8-BLOCK, F8-DEFER, F8-REVALIDATE, F8-REAUTHORIZE, F8-REIDENTIFY}

## F8-ADMIT

F8-ADMIT requires all applicable authority predicates to be satisfied, including:

- a valid economic principal;
- valid principal identity binding;
- valid autonomous agent identity;
- active machine financial authority;
- supported authority source;
- valid authority scope;
- current temporal validity;
- no revocation, expiry, supersession, or invalidation;
- valid and attenuated delegation when delegation is used;
- valid and attenuated subdelegation when subdelegation is used;
- sufficient authority evidence;
- no unresolved machine authority conflict;
- no unresolved revalidation requirement;
- no unresolved reauthorization requirement;
- no unresolved identity misbinding;
- supported governance authorization.

Autonomous capability alone cannot produce F8-ADMIT.

## F8-BLOCK

F8-BLOCK applies where a blocking authority defect is established, including:

- invalid authority source;
- out-of-scope action;
- revoked, expired, superseded, or invalid machine authority;
- nonattenuated delegation;
- nonattenuated subdelegation;
- unauthorized authority inheritance across agent or runtime replacement;
- conflict that prevents ordinary admission;
- attempted self-authorization;
- attempted authority amplification;
- substitution of account, wallet, key, credential, model output, or execution success for authority.

## F8-DEFER

F8-DEFER applies where required facts, evidence, or authority inputs remain unresolved but no established blocking defect yet determines the request.

F8-DEFER does not authorize execution.

## F8-REVALIDATE

F8-REVALIDATE applies where previously valid authority, principal continuity, identity binding, scope, temporal state, delegation, evidence, or replacement continuity must be re-evaluated before ordinary admission.

Revalidation evaluates existing authority and SHALL NOT create new authority.

## F8-REAUTHORIZE

F8-REAUTHORIZE applies where authority is absent, expired, revoked, superseded, invalid, insufficient, or cannot validly continue after replacement or continuity disruption.

Reauthorization MUST derive from a valid external or previously admitted economic principal or authority source.

Prior execution, account control, wallet control, key possession, persistent operation, or prior authorization cannot self-create reauthorization.

## F8-REIDENTIFY

F8-REIDENTIFY applies where the economic principal, principal identity, autonomous agent identity, or their binding is unresolved, stale, conflicted, replaced, or invalid.

F8-REIDENTIFY SHALL resolve identity and attribution before ordinary admission and SHALL NOT itself create financial authority.

## Frozen partial transition function

Delta_8 : Psi8 x Q8 ->partial Psi8

A consequential F8 transition may exist only if:

- D_8(Psi8,q) = F8-ADMIT;
- operation-specific preconditions are satisfied;
- no blocking invariant is violated;
- execution remains inside admitted scope;
- execution remains inside admitted temporal authority;
- principal and agent identity bindings remain valid at transition time;
- any replacement or continuity condition has been independently resolved;
- evidence required by the transition is preserved.

F8-ADMIT is necessary but not sufficient for transition existence.

## Frozen undefined-transition rules

- F8-BLOCK => Delta_8 undefined
- F8-DEFER => Delta_8 undefined
- F8-REVALIDATE => Delta_8 undefined
- F8-REAUTHORIZE => Delta_8 undefined
- F8-REIDENTIFY => Delta_8 undefined

These outcomes are governance states and SHALL NOT be collapsed into technical execution failure.

## Frozen principal / agent rule

An autonomous system that can independently choose or perform an action SHALL NOT thereby become the economic principal authorized to bind that action.

Economic principal status and autonomous execution capability remain independent.

## Frozen replacement rule

Agent replacement, model replacement, runtime migration, identity rotation, credential rotation, wallet replacement, or infrastructure change SHALL NOT automatically preserve machine authority.

Where replacement affects identity or authority continuity, the request MUST enter F8-REIDENTIFY, F8-REVALIDATE, or F8-REAUTHORIZE as applicable before ordinary admission.

## Frozen persistence rule

Persistent technical operation SHALL NOT imply persistent machine authority.

Every consequential transition remains subject to current principal attribution, authority scope, temporal validity, revocation state, and applicable continuity conditions.

## Frozen no-retroactivity rule

Successful autonomous execution SHALL NOT retroactively establish principal status, authority, admissibility, valid delegation, identity continuity, or authority continuity.

Settlement, ledger inclusion, account mutation, wallet mutation, contract completion, or external acceptance SHALL NOT retroactively create machine financial authority.

## Freeze control

The F8 decision / transition semantics are frozen.

Invariants, proof obligations, runtime components, tests, adversarial verification, release surfaces, commit, tag, and push remain unfrozen.

## Next

FIN-F8-06 — INVARIANT DISCOVERY / FREEZE
