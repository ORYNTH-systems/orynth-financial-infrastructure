# Digital-Asset Custody and Delegated Cryptographic Authority

Draft status: WORKING MANUSCRIPT v0.1

Canonical source baseline: financial-suite-v1.0.0

## Abstract

Digital-asset systems often treat possession of a key, production of a valid signature, or technical control of an asset as though those conditions were sufficient to establish authority. F5 rejects that collapse.

This paper formalizes digital-asset custody, delegated cryptographic authority, revocation, signature validity, technical control, and governance admissibility. Its controlling separation is key possession != authority.

The architecture preserves cryptographic capability, custody capability, authority source, delegated scope, principal authority, revocation, evidence, execution validity, and governance admissibility as distinct governed relations.

## 1. Problem

A system may possess a valid key and successfully execute a cryptographic action while lacking governance authority for the represented financial consequence.

Likewise, a signature may be technically valid while the signer is unauthorized, outside scope, revoked, or otherwise inadmissible.

F5 therefore separates cryptographic capability from governance authority.

## 2. Canonical Boundary

F5 governs digital-asset custody, key possession, signature validity, delegated cryptographic authority, custody capability, principal authority, revocation, and custody-action admissibility.

F5 does not permit key possession, signature validity, technical control, delegated capability, or successful execution to self-prove governance authority.

## 3. Key Possession and Authority

Possession of a cryptographic key establishes a technical capability to perform operations supported by that key.

It does not by itself establish governance authority to perform those operations.

Key possession != authority.

## 4. Signature Validity and Authorization

A cryptographic signature may validly prove that a particular key produced or approved a signed payload under the applicable cryptographic mechanism.

That proof does not independently establish that the represented financial action was governance-authorized.

Valid cryptographic signature != valid governance authorization.

## 5. Custody Capability and Custody Authority

Technical ability to move, sign for, lock, unlock, delegate, or otherwise control a digital asset is a custody capability.

Custody capability != custody authority.

A system must preserve the difference between what an actor can technically do and what that actor is authorized to do.

## 6. Delegated Cryptographic Authority

Delegated cryptographic authority derives from an existing authority source and remains bounded by the admitted scope of that delegation.

Delegated authority cannot exceed the authority available to the delegating principal.

Delegation therefore attenuates authority rather than creating an unbounded new source.

## 7. Technical Control and Economic-Principal Authority

Technical control of a digital asset may arise through key possession, infrastructure access, account control, delegated execution capability, or other mechanisms.

Technical control != economic-principal authority.

Control of the execution mechanism does not itself establish authority to determine the governed economic consequence.

## 8. Key Transfer and Authority Transfer

Transfer of a cryptographic key changes technical possession.

It does not necessarily transfer governance authority.

Key transfer != authority transfer.

Authority transfer requires its own valid source, scope, delegation, and admission conditions.

## 9. Revocation and Residual Capability

Governance authority may be revoked while an actor retains a previously issued key or other cryptographic capability.

Revoked authority != absence of technical capability.

Continued technical possession after revocation therefore cannot be interpreted as continuing authority.

## 10. Cryptographic Evidence and Admissibility

Cryptographic evidence may show that a key signed, approved, transmitted, or executed a digital-asset action.

Cryptographic evidence != authority.

A custody action may be technically valid while remaining governance-inadmissible.

## 11. Core Non-Equivalence Results

1. Key possession != authority.
2. Valid cryptographic signature != valid governance authorization.
3. Custody capability != custody authority.
4. Delegated cryptographic authority != unbounded authority.
5. Technical control != economic-principal authority.
6. Key transfer != authority transfer.
7. Revoked authority != absence of technical capability.
8. Cryptographic evidence != authority.
9. Technically valid custody action != governance admission.
10. Successful digital-asset execution != retroactive custody authorization.

## 12. Runtime and Adversarial Verification

The F5 canonical technical surface tests key-possession boundaries, signature / authority separation, delegation attenuation, revocation behavior, custody-state admissibility, and adversarial attempts to infer authority from cryptographic success.

These results are bounded verification evidence for the implemented canonical F5 surface. They are not universal empirical guarantees.

## 13. Cross-Family Interfaces

F5 inherits F3 custody-state distinctions and F4 evidence and record-integrity boundaries while preserving the architecture-wide capability / authority separation.

Later financial families may rely on F5 cryptographic-authority semantics without collapsing executable code, jurisdictional reach, autonomous capability, or successful execution into governance authority.

## 14. Limits and Non-Claims

This paper does not claim production deployment, regulatory approval, institutional adoption, external certification, customer validation, legal sufficiency, or universal prevention of digital-asset custody failure.

The claims are limited to the canonical F5 technical architecture, formal distinctions, runtime behavior, proof surfaces, and adversarial evidence bound in FIN-PUB-22.

## 15. Conclusion

Cryptographic systems can establish possession, signature validity, and technical execution without establishing governance authority.

F5 formalizes the separation among keys, signatures, custody capability, delegated scope, principal authority, revocation, evidence, admissibility, and execution.

The resulting architecture prevents technical possession or cryptographic success from substituting for valid digital-asset authority.

## Manuscript control

This is a working manuscript derived from the ten bound FIN-PUB-22 claims.

No claim expansion is admitted in this pass.

The manuscript is not yet publication-frozen.

## Next

FIN-PUB-24 — F5 MANUSCRIPT CLAIM / SOURCE AUDIT
