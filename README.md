# ORYNTH Financial Infrastructure

Formal research and reference architecture for deterministic execution integrity across financially consequential computational systems.

This repository develops a layered financial execution-governance architecture concerned with the conditions under which financial effects may be authorized, admitted, executed, settled, finalized, represented, reopened, reconstructed, preserved, delegated, routed across jurisdictions, and initiated by autonomous systems without collapsing capability, possession, consensus, execution, evidence, record state, or technical reach into authority.

## Core Principle

**Capability does not imply authority.**

The architecture preserves additional separations including:

- prior authorization != current admissibility
- key possession != authority
- consensus != authority
- execution != finality
- obligation satisfaction != custody validity
- custody possession != custody authority
- atomic completion != finality
- reconciliation != finality
- finality != irreversibility
- finality != consequential closure
- ledger representation != underlying financial truth
- record equality != historical identity
- record reconstruction != continuity preservation
- executable code != governance authority
- technical reach != jurisdictional authority
- autonomous capability != economic principal authority
- functional recovery != continuity preservation

## Repository Status

The F1-F8 financial technical suite is canonically closed.

The repository also contains a source-bound F1-F8 manuscript release-candidate suite. These manuscript artifacts are repository-controlled research drafts and publication surfaces; they are **not yet externally published papers**.

Current suite-level technical closure:

- Technical suite tag: `financial-suite-v1.0.0`

Current publication-suite repository closure:

- Publication suite tag: `financial-publication-suite-v0.1.0`
- F1-F8 publication release candidates: 8 verified
- Publication release chain: closed and remote verified
- External publication: not yet claimed

### Family Status

| Family | Research domain | Technical release | Repository manuscript release candidate | External paper |
| --- | --- | --- | --- | --- |
| F1 | Partial settlement, compensation, reconciliation, continuity | `financial-f1-reconciled-v1.0.0` | `financial-f1-publication-v0.1.0` | Not yet published |
| F2 | Distributed settlement, multiparty authority, consensus | `financial-f2-v1.0.0` | `financial-f2-publication-v0.1.0` | Not yet published |
| F3 | Obligation finality, custody-state integrity, consequential closure | `financial-f3-v1.0.0` | `financial-f3-publication-v0.1.0` | Not yet published |
| F4 | Ledger-state finality, record integrity, reopenable state | `financial-f4-v1.0.0` | `financial-f4-publication-v0.1.0` | Not yet published |
| F5 | Digital-asset custody and delegated cryptographic authority | `financial-f5-v1.0.0` | `financial-f5-publication-v0.1.0` | Not yet published |
| F6 | Smart contracts and programmable financial authority | `financial-f6-v1.0.0` | `financial-f6-publication-v0.1.0` | Not yet published |
| F7 | Cross-jurisdiction financial execution | `financial-f7-v1.0.0` | `financial-f7-publication-v0.1.0` | Not yet published |
| F8 | Autonomous economic agency and machine financial authority | `financial-f8-v1.0.0` | `financial-f8-publication-v0.1.0` | Not yet published |

## Financial Research Families

### F1 — Partial Settlement, Compensating Execution, and Economic-State Continuity

Studies partial financial effectuation, compensation, reversal, reconciliation, evidence, historical identity, and continuity.

### F2 — Distributed Settlement, Multiparty Authority, and the Consensus Boundary

`agreement != consensus != authority != admissibility != execution != settlement finality`

### F3 — Obligation Finality, Custody-State Integrity, and Consequential Financial Closure

`execution != effect occurrence != obligation satisfaction != custody validity != settlement completion != finality != consequential closure`

### F4 — Ledger-State Finality, Record Integrity, and Reopenable Financial State

`ledger representation != underlying financial truth`

### F5 — Digital-Asset Custody and Delegated Cryptographic Authority

`key possession != authority`

### F6 — Smart Contracts and Programmable Financial Authority

`executable code != governance authority`

### F7 — Cross-Jurisdiction Financial Execution and the Boundary of Technical Reach

`technical reach != jurisdictional authority`

### F8 — Autonomous Economic Agency and Machine Financial Authority

`autonomous capability != economic principal authority`

## Architecture Layers

- `00-governance/` — repository governance, release doctrine, and architectural control
- `01-inherited/` — inherited architectural dependencies
- `02-core/` — shared financial execution-governance primitives
- `03-registries/` — canonical object, state, invariant, proof, and claim registries
- `04-settlement-integrity/` — F1 settlement-integrity architecture
- `05-distributed-settlement/` — F2 distributed settlement and multiparty authority
- `06-f3-discovery/` — preserved F3 discovery and development surface
- `06-finality/` — finality-related family and cross-family surfaces
- `07-ledger/` — F4 ledger-state and record-integrity architecture
- `08-digital-asset-custody/` — F5 canonical digital-asset custody architecture
- `08-digital-assets/` — preserved digital-asset development surface
- `09-programmable-finance/` — F6 programmable-finance architecture
- `10-cross-jurisdiction/` — F7 cross-jurisdiction architecture
- `11-autonomous-economic-agency/` — F8 autonomous-economic-agency architecture
- `12-reference-runtime/` — shared reference-runtime surfaces
- `13-verification/` — verification infrastructure
- `14-case-corpus/` — case and adversarial corpus
- `15-publications/` — source-bound manuscript drafts, claim bindings, audits, and repository publication-release surfaces
- `16-standard/` — standards-oriented surfaces
- `formal-proofs/` — cross-family formal proof material
- `reference-runtime/` — runtime reference implementations
- `schemas/` — machine-readable schemas
- `tests/` — baseline and adversarial verification
- `tools/` — repository tooling
- `verification/` — verification outputs and supporting controls

Historical or parallel directories are preserved where they form part of the repository's development lineage. Their presence does not imply that multiple directories are independently canonical owners of the same family.

## Verification & Evidence

The repository includes distinct formal-proof, counterexample, reference-runtime, test, and conformance surfaces. These evidence classes are intentionally separated and should not be treated as interchangeable.

For F3 — **Obligation Finality, Custody-State Integrity, and Consequential Financial Closure** — the public verification chain is directly inspectable:

### Formal proof and counterexample discharge

- [`06-f3-discovery/proofs/F3_POSITIVE_PROOF_DISCHARGE.md`](06-f3-discovery/proofs/F3_POSITIVE_PROOF_DISCHARGE.md) — positive proof discharge for admitted F3 proof obligations
- [`06-f3-discovery/proofs/F3_COUNTEREXAMPLE_DISCHARGE.md`](06-f3-discovery/proofs/F3_COUNTEREXAMPLE_DISCHARGE.md) — counterexample discharge for invalid implications and non-equivalences
- [`03-registries/F3_PROOF_DISCHARGE_REGISTRY.csv`](03-registries/F3_PROOF_DISCHARGE_REGISTRY.csv) — obligation-level disposition registry linking F3 proof obligations to their evidence surfaces

The F3 proof registry contains 40 discharged obligations across distinct claim classes, including formally proved, counterexample-discharged, and reference-runtime-conformant obligations.

### Reference runtime

- [`06-f3-discovery/runtime/f3_runtime/`](06-f3-discovery/runtime/f3_runtime/) — F3 reference-runtime package
- [`06-f3-discovery/runtime/f3_runtime/engine.py`](06-f3-discovery/runtime/f3_runtime/engine.py) — deterministic F3 runtime evaluation logic
- [`06-f3-discovery/runtime/f3_runtime/models.py`](06-f3-discovery/runtime/f3_runtime/models.py) — runtime data and state models

The reference runtime is a bounded technical implementation for exercised F3 semantics. It is not represented as production financial infrastructure.

### Runtime tests and conformance

- [`tests/f3/test_f3_runtime.py`](tests/f3/test_f3_runtime.py) — F3 runtime test suite
- [`03-registries/F3_RUNTIME_CONFORMANCE_MATRIX.csv`](03-registries/F3_RUNTIME_CONFORMANCE_MATRIX.csv) — direct mapping from runtime proof obligations to named test surfaces and dispositions

The current F3 runtime-conformance matrix records six `REFERENCE-RUNTIME-CONFORMANT` obligations covering:

1. execution-only finality rejection;
2. consensus-only finality rejection;
3. custody-possession-only authority rejection;
4. unresolved-finality-conflict blocking;
5. historical-finality preservation after reopening;
6. explicit post-finality contradiction.

### Evidence interpretation

The repository preserves the following distinctions:

`formal proof != counterexample discharge != runtime conformance != adversarial evidence != production validation`

A formal derivation establishes a result within the locked model.

A counterexample discharge defeats a specified implication or equivalence; it does not automatically prove a different positive theorem.

Reference-runtime conformance establishes behavior of the specific implementation under the exercised test conditions.

None of these evidence classes, individually or together, establish production deployment, regulatory approval, institutional adoption, legal sufficiency, or universal correctness.

## Publication Surface

`15-publications/` contains the repository-controlled research publication surface for F1-F8.

For each family, that surface includes source/claim binding, a working manuscript draft, a claim/source audit, a publication-surface freeze, and a tagged repository release candidate.

These artifacts establish traceability and bounded manuscript state.

They do **not** establish external publication, peer review, DOI assignment, journal acceptance, regulatory approval, institutional adoption, customer validation, external certification, or legal sufficiency.

The next publication phase is full paper development and external publication packaging.

## Claim Discipline

A claim may be:

- formally proved
- discharged through counterexample analysis
- reference-runtime conformant
- supported by bounded adversarial verification
- historically registered but not currently open
- unresolved

These statuses are not interchangeable.

**evidence != authority**

**successful execution != legitimate execution**

## Inherited ORYNTH Architecture

This repository binds to, rather than silently redefining, broader ORYNTH architecture including relevant concepts from:

- Unified Agency Architecture (UAA)
- Execution Integrity Protocol (EIP)
- AOMS
- Proof of Block
- Integrity Preservation Theory (IPT)
- Morning Star
- other formally registered ORYNTH execution-governance surfaces where explicitly inherited

Inheritance does not imply equivalence or ownership of every upstream concept.

## Release Discipline

Current canonical technical tags:

- `financial-f1-reconciled-v1.0.0`
- `financial-f2-v1.0.0`
- `financial-f3-v1.0.0`
- `financial-f4-v1.0.0`
- `financial-f5-v1.0.0`
- `financial-f6-v1.0.0`
- `financial-f7-v1.0.0`
- `financial-f8-v1.0.0`
- `financial-suite-v1.0.0`

Repository manuscript release-candidate tags:

- `financial-f1-publication-v0.1.0`
- `financial-f2-publication-v0.1.0`
- `financial-f3-publication-v0.1.0`
- `financial-f4-publication-v0.1.0`
- `financial-f5-publication-v0.1.0`
- `financial-f6-publication-v0.1.0`
- `financial-f7-publication-v0.1.0`
- `financial-f8-publication-v0.1.0`
- `financial-publication-suite-v0.1.0`

A release tag identifies a specific frozen repository state. Later development does not rewrite the historical meaning of that release.

## Public Reference Scope

This repository is a public technical research and reference architecture surface.

It does not claim that:

- the repository manuscript drafts are already externally published papers
- every formal obligation is externally verified
- every runtime is production-deployed
- consensus establishes authority
- possession establishes authority
- executable code establishes governance authority
- technical reach establishes jurisdictional authority
- autonomous capability establishes economic-principal authority
- technical success establishes legitimate financial effectuation
- restoration of function automatically restores integrity or continuity

## Related Public Surface

A separate public demonstration repository is maintained at:

`ORYNTH-systems/settlement-demo`

That repository provides a bounded financial execution-governance demonstration surface and should not be treated as the complete formal architecture represented here.

## Development Rule

New work proceeds through explicit discovery, boundary freeze, formal object/state definition, invariants, proof obligations, runtime conformance, adversarial verification, manuscript assembly, controlled repository release, and—where separately authorized—external publication.

No family, manuscript, or paper is treated as externally published merely because files exist in the working tree or a repository release candidate has been tagged.
