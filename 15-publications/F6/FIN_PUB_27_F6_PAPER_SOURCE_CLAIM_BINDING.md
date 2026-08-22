# FIN-PUB-27 — F6 Paper Source / Claim Binding

Status: COMPLETE — PASS

## Paper

F6 — Smart Contracts and Programmable Financial Authority

## Canonical baseline

- suite closure tag: financial-suite-v1.0.0
- F6 release tag: financial-f6-v1.0.0
- controlling separation: executable code != governance authority

## Bound publication claims

### F6-PUB-C001

Claim: Executable code is distinct from governance authority.

Canonical basis: F6 programmable-authority semantics; canonical non-implication results

### F6-PUB-C002

Claim: Successful smart-contract execution does not by itself establish valid authorization.

Canonical basis: execution / authorization separation; adversarial verification

### F6-PUB-C003

Claim: Programmed conditions are distinct from valid authority-source conditions.

Canonical basis: contract-condition / authority-source boundary

### F6-PUB-C004

Claim: Code deployment does not create authority beyond the authority validly delegated to the programmable mechanism.

Canonical basis: delegation attenuation; programmable authority scope

### F6-PUB-C005

Claim: Technical determinism does not itself establish governance admissibility.

Canonical basis: deterministic execution / admissibility separation

### F6-PUB-C006

Claim: Automated execution capability is distinct from authority to initiate consequential financial action.

Canonical basis: automation capability / initiation authority boundary

### F6-PUB-C007

Claim: Oracle or external-input satisfaction does not itself establish authority for the resulting execution.

Canonical basis: external input / authority separation; runtime verification

### F6-PUB-C008

Claim: Contract immutability does not imply valid authority or irreversible financial legitimacy.

Canonical basis: immutability / authority / legitimacy non-equivalence

### F6-PUB-C009

Claim: Evidence that code executed as programmed does not itself prove the consequential action was governance-admissible.

Canonical basis: execution evidence / admissibility separation

### F6-PUB-C010

Claim: Successful programmable financial execution does not retroactively establish valid governance authority.

Canonical basis: execution / authority non-implication; adversarial verification

## Canonical source surfaces

- 15-publications/F6/.gitkeep
- tests/f6/test_f6_reference_runtime.py
- tests/f6_adversarial/test_f6_adversarial.py

## Claim-control rules

- executable code SHALL NOT be represented as governance authority
- successful contract execution SHALL NOT be represented as self-proving authorization
- programmed conditions SHALL NOT be represented as authority-source validity
- programmable delegation SHALL remain attenuated to valid source and scope
- deterministic execution SHALL NOT be represented as governance admissibility
- oracle or external-input satisfaction SHALL NOT create authority by itself
- execution evidence SHALL NOT be used as retroactive authority evidence
- adversarial results SHALL remain bounded verification evidence
- no production, regulatory, institutional, customer, legal, or external-certification claim is admitted

## Binding status

F6 publication claims are source-bound to the canonical F6 technical and verification surfaces.

The F6 manuscript itself remains unwritten / unfrozen.

## Next

FIN-PUB-28 — F6 MANUSCRIPT CONSTRUCTION
