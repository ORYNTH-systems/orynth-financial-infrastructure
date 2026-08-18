# ORYNTH Financial Infrastructure

Formal research and reference architecture for deterministic execution integrity across financially consequential computational systems.

This repository develops a layered financial execution-governance architecture concerned with the conditions under which financial effects may be authorized, admitted, executed, settled, finalized, represented, reopened, reconstructed, and preserved without collapsing capability, possession, consensus, execution, evidence, or record state into authority.

## Core Principle

**Capability does not imply authority.**

The architecture maintains additional separations including:

- prior authorization != current admissibility
- key possession != authority
- consensus != authority
- execution != finality
- obligation satisfaction != custody validity
- custody possession != custody authority
- atomic completion != finality
- reconciliation != finality
- finality != irreversibility
- finality != historical identity
- finality != continuity preservation
- functional recovery != continuity preservation

## Repository Status

The repository is under active staged development across eight financial research families.

Released canonical families:

- **F2 — Distributed Settlement / Multiparty Authority and Consensus Boundary**
  - Release tag: `financial-f2-v1.0.0`

- **F3 — Obligation Finality, Custody-State Integrity, and Consequential Financial Closure**
  - Release tag: `financial-f3-v1.0.0`

Active development:

- **F4 — Ledger-State Finality, Record Integrity, and Reopenable Financial State**
  - Boundary frozen
  - Object/type formalization not yet frozen

F1 contains substantial preserved development surfaces but is not represented here as a clean canonical release because its historical release state requires later reconciliation.

F5-F8 remain subsequent research families and are not yet treated as completed canonical releases.

## Financial Research Families

### F1 — Partial Settlement, Compensating Execution, and Economic-State Continuity

Studies partial financial effectuation, compensation, reconciliation, continuity, and the distinction between restored function and restored integrity.

### F2 — Distributed Settlement / Multiparty Authority and Consensus Boundary

Formalizes the separation between:

`agreement != consensus != authority != admissibility != execution != settlement finality`

This family addresses multiparty execution, distributed settlement, authority boundaries, consensus limitations, and adversarial cases where agreement or technical completion must not be treated as sufficient authority.

### F3 — Obligation Finality, Custody-State Integrity, and Consequential Financial Closure

Formalizes the separation between:

`execution != effect occurrence != obligation satisfaction != custody validity != settlement completion != finality != irreversibility != historical identity != continuity preservation`

F3 introduces explicit treatment of obligation satisfaction, custody validity, finality eligibility, consequential closure, reopening, post-finality contradiction, and historical finality.

### F4 — Ledger-State Finality, Record Integrity, and Reopenable Financial State

Current frozen working boundary.

F4 begins where F3 leaves off and addresses the distinction between a valid final financial state and the ledger or record state that represents, persists, commits, reopens, contradicts, or reconstructs that state.

Its inherited constraint is:

`final financial state != ledger representation of final financial state`

Formal object, state, transition, invariant, proof, and runtime surfaces are still under development.

### F5 — Digital-Asset Custody and Delegated Cryptographic Authority

Reserved for digital-asset custody, cryptographic possession, delegated authority, signing capability, and related execution-governance distinctions.

### F6 — Smart-Contract and Programmable Financial Authority

Reserved for programmable financial execution, smart-contract authority, delegated instruction, execution scope, and runtime admissibility.

### F7 — Cross-Jurisdiction Financial Execution

Reserved for jurisdiction-sensitive execution authority, legal scope, temporal validity, conflicting authority domains, and cross-boundary execution.

### F8 — Autonomous Economic Agency and Machine Financial Authority

Reserved for autonomous principals, machine-initiated financial action, bounded economic authority, delegated agency, and execution constraints for autonomous systems.

## Architecture Layers

The repository is organized as a layered research and implementation surface:

- `00-governance/` — repository governance, release doctrine, and architectural control
- `01-inherited/` — inherited architectural dependencies
- `02-core/` — shared financial execution-governance primitives
- `03-registries/` — canonical object, state, invariant, proof, and claim registries
- `04-settlement-integrity/` — F1 settlement-integrity development
- `05-distributed-settlement/` — F2 distributed settlement and multiparty authority
- `06-f3-discovery/` — F3 finality architecture, formalization, proofs, runtime, and release evidence
- `06-finality/` — finality-related inherited and cross-family surfaces
- `07-ledger/` — F4 ledger-state and record-integrity development
- `08-digital-assets/` — subsequent digital-asset family
- `09-programmable-finance/` — subsequent programmable-finance family
- `10-jurisdiction/` — subsequent jurisdiction family
- `11-autonomous-economy/` — subsequent autonomous-economic-agency family
- `12-reference-runtime/` — shared reference-runtime surfaces
- `13-verification/` — verification infrastructure
- `14-case-corpus/` — case and adversarial corpus
- `15-publications/` — technical manuscript and publication source surfaces
- `16-standard/` — standards-oriented surfaces
- `formal-proofs/` — cross-family formal proof material
- `reference-runtime/` — runtime reference implementations
- `schemas/` — machine-readable schemas
- `tests/` — baseline and adversarial verification
- `tools/` — repository tooling
- `verification/` — verification outputs and supporting controls

## Claim Discipline

The repository distinguishes among different forms of support.

A claim may be:

- formally proved
- discharged through counterexample analysis
- reference-runtime conformant
- historically registered but not currently open
- unresolved

These statuses are not interchangeable.

Likewise:

**evidence != authority**

and:

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

Canonical family releases are frozen through explicit commit and annotated-tag boundaries.

Current canonical financial release tags include:

- `financial-f2-v1.0.0`
- `financial-f3-v1.0.0`

A release tag identifies a specific frozen repository state. Later development does not rewrite the historical meaning of that release.

## Public Reference Scope

This repository is a public technical research and reference architecture surface.

It does not claim that:

- every research family is complete
- every formal obligation is externally verified
- every runtime is production-deployed
- consensus establishes authority
- possession establishes authority
- technical success establishes legitimate financial effectuation
- restoration of function automatically restores integrity or continuity

## Related Public Surface

A separate public demonstration repository is maintained at:

`ORYNTH-systems/settlement-demo`

That repository provides a bounded financial execution-governance demonstration surface and should not be treated as the complete formal architecture represented here.

## Development Rule

New family work proceeds through explicit discovery, boundary freeze, formal object/state definition, invariants, proof obligations, runtime conformance, adversarial verification, manuscript assembly, and controlled release.

No family is treated as canonically released merely because files exist in the working tree.
