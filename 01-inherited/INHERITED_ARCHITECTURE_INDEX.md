# Inherited Architecture Index

## Governing Rule

The ORYNTH Financial Infrastructure repository SHALL specialize inherited architecture without silently redefining the canonical properties owned by upstream systems.

Inheritance does not transfer canonical ownership.

A financial specialization MAY:

- introduce domain-specific state,
- introduce financial transition semantics,
- define additional proof obligations,
- define stricter constraints,
- define domain-specific reference implementations.

A financial specialization SHALL NOT:

- redefine an inherited primitive without explicit architectural reconciliation,
- claim inherited mechanisms as novel financial contributions,
- weaken upstream invariants,
- silently fork canonical terminology,
- infer ownership merely from implementation reuse.

---

## Inherited Systems

### UAA

Canonical ownership:
- non-default execution authority,
- admissibility-before-authority,
- control-point verification,
- fail-closed execution,
- authorization artifacts,
- replay resistance,
- no-effect-on-block.

Financial specialization:
- financial action representation,
- financially consequential execution boundaries,
- financial authority constraints.

Non-redefinition boundary:
Financial Infrastructure does not redefine the creation or nature of execution authority.

---

### EIP

Canonical ownership:
- execution-time rule identity continuity,
- rule/version continuity,
- authority binding continuity,
- delegation continuity,
- policy translation continuity,
- verification continuity.

Financial specialization:
- execution continuity over financially consequential rules and settlement instructions.

Non-redefinition boundary:
Financial Infrastructure does not redefine rule identity continuity.

---

### AOMS

Canonical ownership:
- AuthorizedState / CurrentState reconciliation,
- action drift detection,
- policy/resource/environment/dependency state reconciliation,
- current execution admissibility.

Financial specialization:
- financial orchestration state,
- multi-party financial transition state,
- settlement boundary state.

Non-redefinition boundary:
Financial Infrastructure does not redefine generic current-state reconciliation.

---

### Proof-of-Block

Canonical ownership:
- governed refusal evidence,
- reconstruction integrity,
- continuity integrity,
- admissibility integrity,
- provenance integrity,
- compound failure evidence.

Financial specialization:
- financial Proof-of-Block profiles,
- settlement denial evidence,
- post-effect evidence classification where newly required.

Non-redefinition boundary:
Financial Infrastructure does not redefine Proof-of-Block itself.

---

### UES

Canonical ownership:
- exchange-state transition representation,
- exchange authorization,
- execution-time settlement verification,
- effectuation enforcement,
- replay resistance,
- deterministic no-settlement semantics,
- settlement audit lineage,
- continuity-bound exchange authorization.

Financial specialization:
- post-effect settlement integrity,
- partial-effect semantics,
- compensation,
- reversal,
- finality,
- financial reconstruction.

Non-redefinition boundary:
F1 SHALL begin after the pre-effect settlement-governance boundary already established by UES.

---

### Banking Reasoning Lab

Canonical ownership:
- historical banking-domain financial object models,
- financial state and mutation machinery,
- banking reasoning surfaces,
- financial planning / graph / evidence / replay / ledger experimentation.

Financial specialization:
- promote only validated primitives after explicit reconciliation.

Non-redefinition boundary:
Existing banking machinery SHALL NOT be silently copied or relabeled as new F1-F8 work.

---

### Morning Star Finance

Canonical ownership:
- constitutional finance-domain governance specialization,
- financial deployment,
- financial integrity,
- financial assurance.

Financial specialization:
- normative correspondence where relevant.

Non-redefinition boundary:
Financial Infrastructure SHALL distinguish execution-integrity mechanisms from Morning Star constitutional lifecycle machinery.

---

### DEI

Canonical ownership:
- unified financially consequential execution-integrity model,
- contemporaneous financial admissibility,
- execution-chain continuity framing,
- Proof-of-Block application to financial outcomes.

Financial specialization:
- F1-F8 extend beyond DEI's initial boundary.

Non-redefinition boundary:
F1-F8 must explicitly identify which DEI assumptions are preserved, weakened, removed, or extended.

---

## Inheritance Principle

Inherited architecture is dependency, not duplication.

Canonical ownership remains with the upstream authority unless an explicit architecture-reconciliation record changes ownership.
