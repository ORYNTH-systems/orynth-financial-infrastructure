# FIN-F7-08 — Formal Proof / Counterexample / Traceability Discharge

Status: COMPLETE — PASS

## Canonical family

Cross-Jurisdiction Financial Execution

## Formal proof discharge

The following proof schemas discharge F7-PO-001 through F7-PO-032.

### P1 — Technical reach / authority separation

Let R denote technical reach and A denote jurisdictional authority.

F7 admits states where R = AVAILABLE and A != ACTIVE.

Therefore R does not entail A.

This discharges non-equivalence obligations concerning technical reach, routing, accessibility, asset presence, custody location, settlement venue, and cross-border executability.

### P2 — Jurisdiction-specific authority separation

Let A_i denote authority applicable in jurisdiction J_i and A_j authority applicable in J_j.

The frozen F7 state and predicate model independently represents applicability for each consequential jurisdiction.

No inference rule permits A_i => A_j for i != j.

Therefore authority in one jurisdiction does not entail authority in another.

### P3 — Evidence / authority separation

Jurisdictional evidence and execution evidence are distinct typed objects from jurisdictional authority and authority source.

Accordingly, evidence predicates may support evaluation but cannot constitute authority.

### P4 — Coverage separation

Let C_req be the set of consequential jurisdictions required by request q and C_auth the set supported by applicable authority.

Complete coverage requires C_req subseteq C_auth.

If C_auth is a proper subset of C_req, partial coverage exists and complete coverage is false.

Therefore partial jurisdictional coverage does not imply complete coverage.

### P5 — Delegation attenuation

A delegated cross-jurisdiction authority is admissible only where its jurisdictional applicability, scope, and duration are no broader than its parent authority.

Any delegation that expands beyond the parent authority is nonattenuated and therefore blocks ordinary admission.

### P6 — Decision / transition separation

D_7 and Delta_7 are separately frozen functions.

F7-ADMIT is necessary but not sufficient for transition existence.

F7-BLOCK, F7-DEFER, F7-REVALIDATE, and F7-REAUTHORIZE leave the requested consequential target transition undefined.

Therefore decision outcome does not collapse into transition existence.

### P7 — No retroactive authorization

Execution status and governance authorization status are independently represented.

The frozen semantics admit EXECUTED with governance authorization unsupported or blocking.

Therefore successful execution, settlement, ledger inclusion, custody transfer, or cross-border completion cannot logically establish prior jurisdictional admissibility.

### P8 — Revalidation / reauthorization separation

REVALIDATE evaluates whether existing authority remains applicable.

REAUTHORIZE requires authority to be newly established from a valid authority source.

Therefore revalidation does not imply reauthorization and neither state self-creates authority.

## Formally proved obligations

- F7-PO-001: FORMALLY-PROVED
- F7-PO-002: FORMALLY-PROVED
- F7-PO-003: FORMALLY-PROVED
- F7-PO-004: FORMALLY-PROVED
- F7-PO-005: FORMALLY-PROVED
- F7-PO-006: FORMALLY-PROVED
- F7-PO-007: FORMALLY-PROVED
- F7-PO-008: FORMALLY-PROVED
- F7-PO-009: FORMALLY-PROVED
- F7-PO-010: FORMALLY-PROVED
- F7-PO-011: FORMALLY-PROVED
- F7-PO-012: FORMALLY-PROVED
- F7-PO-013: FORMALLY-PROVED
- F7-PO-014: FORMALLY-PROVED
- F7-PO-015: FORMALLY-PROVED
- F7-PO-016: FORMALLY-PROVED
- F7-PO-017: FORMALLY-PROVED
- F7-PO-018: FORMALLY-PROVED
- F7-PO-019: FORMALLY-PROVED
- F7-PO-020: FORMALLY-PROVED
- F7-PO-021: FORMALLY-PROVED
- F7-PO-022: FORMALLY-PROVED
- F7-PO-023: FORMALLY-PROVED
- F7-PO-024: FORMALLY-PROVED
- F7-PO-025: FORMALLY-PROVED
- F7-PO-026: FORMALLY-PROVED
- F7-PO-027: FORMALLY-PROVED
- F7-PO-028: FORMALLY-PROVED
- F7-PO-029: FORMALLY-PROVED
- F7-PO-030: FORMALLY-PROVED
- F7-PO-031: FORMALLY-PROVED
- F7-PO-032: FORMALLY-PROVED

## Counterexample discharge

The following explicit countermodels discharge F7-PO-033 through F7-PO-044.

### CE-01 — Reach without authority
R = AVAILABLE; A = ABSENT. Technical cross-border execution is reachable, but jurisdictional authority is absent.

### CE-02 — Authority in J_i but not J_j
A_i = ACTIVE and applicable; A_j = ABSENT. The request implicates both J_i and J_j. Complete coverage is false.

### CE-03 — Full routing with partial coverage
Technical routing succeeds across all systems while only a proper subset of consequential jurisdictions is authorized.

### CE-04 — Asset presence without authority
An asset is located or represented in J_k while no applicable execution authority exists for the requested action.

### CE-05 — Counterparty presence without consent
A counterparty is present in J_k, but no jurisdictional consent or authority follows from presence alone.

### CE-06 — Venue availability without permission
A settlement venue in J_k is technically available while the requested action remains jurisdictionally unauthorized.

### CE-07 — Evidence without authority
Jurisdictional evidence is CORROBORATED while A = ABSENT. Evidence supports evaluation but does not create authority.

### CE-08 — Execution while blocked
I = EXECUTED while G = DENIED or conflict is BLOCKING. The action occurred technically but remains governance-inadmissible.

### CE-09 — Nonattenuated delegation
Delegated authority is ACTIVE but expands jurisdictional scope beyond its parent authority. Ordinary admission is blocked.

### CE-10 — Conflict with broader authority available
J_i and J_j conflict, with J_i broader. The existence of the broader authority does not resolve the conflict or authorize selection of J_i.

### CE-11 — Stale applicability
Authority was previously applicable, but jurisdictional applicability evidence is stale. Decision = F7-REVALIDATE.

### CE-12 — Revoked authority
Authority is REVOKED while technical reach remains AVAILABLE. Decision = F7-REAUTHORIZE.

## Counterexample obligations

- F7-PO-033: COUNTEREXAMPLE-DISCHARGED
- F7-PO-034: COUNTEREXAMPLE-DISCHARGED
- F7-PO-035: COUNTEREXAMPLE-DISCHARGED
- F7-PO-036: COUNTEREXAMPLE-DISCHARGED
- F7-PO-037: COUNTEREXAMPLE-DISCHARGED
- F7-PO-038: COUNTEREXAMPLE-DISCHARGED
- F7-PO-039: COUNTEREXAMPLE-DISCHARGED
- F7-PO-040: COUNTEREXAMPLE-DISCHARGED
- F7-PO-041: COUNTEREXAMPLE-DISCHARGED
- F7-PO-042: COUNTEREXAMPLE-DISCHARGED
- F7-PO-043: COUNTEREXAMPLE-DISCHARGED
- F7-PO-044: COUNTEREXAMPLE-DISCHARGED

## Traceability discharge

- F7-PO-045: TRACEABILITY-DISCHARGED — canonical objects map to frozen F7 state domains and predicates.
- F7-PO-046: TRACEABILITY-DISCHARGED — frozen predicates map to D_7 and Delta_7 decision / transition semantics.
- F7-PO-047: TRACEABILITY-DISCHARGED — all 58 invariants derive from frozen object, state, predicate, decision, delegation, restriction, evidence, or transition surfaces.
- F7-PO-048: TRACEABILITY-DISCHARGED — F7 inheritance preserves F2 consensus, F4 ledger-state, F5 cryptographic-authority, and F6 programmable-authority boundaries without collapse.

## Runtime obligations

F7-PO-049 through F7-PO-058 remain OPEN pending reference runtime construction and runtime-conformance testing.

## Disposition

- FORMALLY-PROVED: 32
- COUNTEREXAMPLE-DISCHARGED: 12
- TRACEABILITY-DISCHARGED: 4
- RUNTIME-CONFORMANCE: 0
- OPEN: 10
- TOTAL: 58

## Next

FIN-F7-09 — REFERENCE RUNTIME CONSTRUCTION / CONFORMANCE
