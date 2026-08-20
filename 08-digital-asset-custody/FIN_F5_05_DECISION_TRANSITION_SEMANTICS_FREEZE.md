# FIN-F5-05 — Decision / Transition Semantics Freeze

Status: COMPLETE — PASS

## Working family

Digital-Asset Custody and Delegated Cryptographic Authority

## Frozen four-layer separation

predicate / semantic fact != decision outcome != transition existence != resulting F5 state

No F5 predicate directly authorizes or performs a transition.

## Frozen decision function

D_5 : Psi5 x Q5 -> {F5-ADMIT, F5-BLOCK, F5-DEFER, F5-REVALIDATE, F5-REAUTHORIZE}

D_5 is total on admissible F5 decision requests.

### Decision outcomes

- F5-ADMIT
- F5-BLOCK
- F5-DEFER
- F5-REVALIDATE
- F5-REAUTHORIZE

### F5-ADMIT

The requested cryptographic or custody-relevant operation is governance-admissible under the current authority, scope, temporal, evidence, and lifecycle context.

F5-ADMIT does not prove that the requested transition occurred.

### F5-BLOCK

The requested operation is governance-inadmissible under the current F5 context.

For the blocked target operation, the transition MUST be undefined.

### F5-DEFER

The request cannot yet be admitted because required authority, evidence, scope, lifecycle, custody, or conflict conditions remain unresolved.

F5-DEFER is not equivalent to denial.

The requested target transition MUST remain undefined while deferred.

### F5-REVALIDATE

Previously established authority, custody, key-lifecycle, threshold, or execution evidence requires current revalidation before the target operation can be admitted.

F5-REVALIDATE does not itself restore or create authority.

### F5-REAUTHORIZE

The prior cryptographic capability may exist or have been restored, but current governance authority must be independently re-established from an applicable authority source.

F5-REAUTHORIZE MUST NOT be inferred solely from key recovery, key rotation, wallet recovery, credential replacement, or restored signing capability.

## Frozen transition function

Delta_5 : Psi5 x Q5 ->partial Psi5

Delta_5 is partial.

A decision outcome and a transition are distinct objects.

## Frozen transition eligibility

- D_5(Psi5,q) = F5-BLOCK => Delta_5(Psi5,q) is undefined for the blocked target operation.
- D_5(Psi5,q) = F5-DEFER => Delta_5(Psi5,q) is undefined for the deferred target operation.
- D_5(Psi5,q) = F5-REVALIDATE => ordinary target transition remains undefined until revalidation succeeds.
- D_5(Psi5,q) = F5-REAUTHORIZE => ordinary target transition remains undefined until authority is independently re-established.
- D_5(Psi5,q) = F5-ADMIT => a target transition MAY exist only if all operation-specific transition preconditions are satisfied.

## Frozen minimum decision request Q5

Every admissible F5 decision request MUST identify at minimum:

- request_id
- requested_cryptographic_or_custody_operation
- subject_or_actor
- target_asset_wallet_address_or_control_surface
- claimed_authority_source
- delegated_authority_context
- key_or_capability_context
- custody_context
- evidence_context
- scope_context
- temporal_context
- lifecycle_context

## Frozen admission conditions

F5-ADMIT requires the decision process to establish, where applicable:

1. authority source support;
2. active delegated authority;
3. valid authority scope;
4. temporal validity;
5. delegation attenuation;
6. key lifecycle permission;
7. required custody state;
8. absence of unresolved blocking custody-authority conflict;
9. required threshold-control satisfaction where applicable;
10. operation-specific evidence sufficiency.

Cryptographic capability or technically valid execution evidence alone is insufficient.

## Frozen non-collapse rules

- F5-ADMIT != cryptographic act occurred
- F5-ADMIT != resulting custody state
- F5-BLOCK != absence of cryptographic capability
- F5-DEFER != F5-BLOCK
- F5-REVALIDATE != F5-REAUTHORIZE
- key recovery != F5-REAUTHORIZE success
- valid signature != F5-ADMIT
- threshold satisfaction != F5-ADMIT
- predicate truth != transition authority
- transition existence != resulting-state classification

## Freeze control

The F5 decision / transition semantics are frozen.

Invariants, proof obligations, formal discharge, runtime components, and tests remain unfrozen.

## Next

FIN-F5-06 — INVARIANT DISCOVERY AND FREEZE
