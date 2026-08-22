# Smart Contracts and Programmable Financial Authority

Draft status: WORKING MANUSCRIPT v0.1

Canonical source baseline: financial-suite-v1.0.0

## Abstract

Programmable financial systems often treat executable logic as though successful execution were sufficient to establish authority. F6 rejects that collapse.

This paper formalizes smart-contract execution, programmed conditions, delegated programmable authority, deterministic execution, external inputs, immutability, and governance admissibility. Its controlling separation is executable code != governance authority.

The architecture preserves execution capability, authority source, delegated scope, trigger satisfaction, admissibility, evidence, and consequential authority as distinct governed relations.

## 1. Problem

A smart contract may execute exactly as programmed while the consequential financial action lacks valid governance authority.

Likewise, satisfied code conditions may establish that a programmed branch is executable without establishing that the resulting action is authorized.

F6 therefore separates executable logic from governance authority.

## 2. Canonical Boundary

F6 governs programmable financial execution, smart-contract conditions, delegated authority, deterministic execution, initiation authority, external inputs, immutability, evidence, and governance admissibility.

F6 does not permit executable code, successful execution, programmed conditions, oracle satisfaction, automation, or immutability to self-create governance authority.

## 3. Executable Code and Governance Authority

Executable code defines technical behavior under specified computational conditions.

Governance authority determines whether a consequential financial action is validly authorized under the applicable authority source and scope.

Executable code != governance authority.

## 4. Successful Execution and Authorization

Successful smart-contract execution establishes that the implemented computational path completed under its technical conditions.

It does not by itself establish valid authorization.

Successful smart-contract execution != valid authorization.

## 5. Programmed Conditions and Authority Conditions

Programmed conditions define technical predicates for execution.

Authority-source conditions determine whether the actor, mechanism, or delegated process possesses valid authority for the consequential action.

Programmed conditions != valid authority-source conditions.

## 6. Deployment and Delegated Programmable Authority

Deployment of executable financial code creates a technical mechanism, not an independent authority source.

Code deployment != creation of unbounded authority.

Any programmable authority remains bounded by the valid source and scope delegated to the mechanism.

## 7. Determinism and Governance Admissibility

A deterministic system may produce the same technical output from the same defined inputs.

Technical determinism != governance admissibility.

Predictable or inevitable execution under code does not establish that the resulting financial action is authorized.

## 8. Automated Capability and Initiation Authority

Automation can permit a mechanism to initiate or complete financial actions without contemporaneous human intervention.

Automated execution capability != authority to initiate consequential financial action.

Initiation authority must remain traceable to a valid governance basis rather than inferred from automation capability.

## 9. Oracles and External Inputs

An oracle or other external input may satisfy a programmed condition and thereby make a contract path technically executable.

Oracle or external-input satisfaction != authority.

External input validity and authority validity remain separate questions.

## 10. Immutability and Financial Legitimacy

Immutability may constrain whether deployed code can be modified through the technical mechanism.

Contract immutability != valid governance authority.

Contract immutability != irreversible financial legitimacy.

Technical resistance to change does not convert an unauthorized action into an authorized one.

## 11. Execution Evidence and Admissibility

Evidence that code executed as programmed is evidence of technical runtime behavior.

Execution evidence != governance admissibility.

Successful execution cannot retroactively establish valid authority.

## 12. Core Non-Equivalence Results

1. Executable code != governance authority.
2. Successful smart-contract execution != valid authorization.
3. Programmed conditions != valid authority-source conditions.
4. Code deployment != creation of unbounded authority.
5. Technical determinism != governance admissibility.
6. Automated execution capability != initiation authority.
7. Oracle or external-input satisfaction != authority.
8. Contract immutability != valid governance authority or irreversible financial legitimacy.
9. Execution evidence != governance admissibility.
10. Successful programmable financial execution != retroactive governance authorization.

## 13. Runtime and Adversarial Verification

The F6 canonical technical surface tests programmable execution boundaries, authority-source separation, delegated scope, deterministic behavior, external-input handling, and adversarial attempts to infer authority from code execution.

These results are bounded verification evidence for the implemented canonical F6 surface. They are not universal empirical guarantees.

## 14. Cross-Family Interfaces

F6 inherits F5 capability / authority and delegation boundaries while preserving F3 and F4 distinctions concerning finality, evidence, and represented financial state.

Later financial families may rely on F6 programmable-authority semantics without collapsing technical reach, jurisdiction, or autonomous capability into governance authority.

## 15. Limits and Non-Claims

This paper does not claim production deployment, regulatory approval, institutional adoption, external certification, customer validation, legal sufficiency, or universal prevention of programmable-finance failure.

The claims are limited to the canonical F6 technical architecture, formal distinctions, runtime behavior, proof surfaces, and adversarial evidence bound in FIN-PUB-27.

## 16. Conclusion

Smart contracts can execute correctly without establishing valid governance authority for the financial consequence they produce.

F6 formalizes the separation among executable code, programmed conditions, delegation, automation, external inputs, immutability, evidence, admissibility, and authority.

The resulting architecture prevents computational success from substituting for valid programmable financial authority.

## Manuscript control

This is a working manuscript derived from the ten bound FIN-PUB-27 claims.

No claim expansion is admitted in this pass.

The manuscript is not yet publication-frozen.

## Next

FIN-PUB-29 — F6 MANUSCRIPT CLAIM / SOURCE AUDIT
