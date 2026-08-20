# FIN-F6-08 — Formal Proof / Counterexample / Traceability Discharge

Status: COMPLETE — PASS

## Canonical family

Smart-Contract and Programmable Financial Authority

## Disposition summary

- FORMALLY-PROVED: 32
- COUNTEREXAMPLE-DISCHARGED: 12
- TRACEABILITY-DISCHARGED: 4
- RUNTIME-CONFORMANCE: 0
- OPEN: 10
- TOTAL: 58

The ten runtime-conformance obligations remain OPEN for FIN-F6-09.

## Formal proof discharge

F6-PO-001 through F6-PO-032 are discharged as formal non-equivalence and safety obligations.

### Proof schema P1 — capability / authority separation

Given executable or programmable capability C and governance authority A, no frozen F6 rule defines C -> A. Therefore capability facts cannot constitute authority without an independently supported authority source.

This discharges obligations covering deployed code, invocation validity, deterministic execution, privileged capability, administrator possession, contract ownership, automation, and upgrade capability.

### Proof schema P2 — data / authority separation

Oracle input, condition satisfaction, execution evidence, contract state, and ledger acceptance are typed facts or evidence. None is typed as an authority source. Therefore data or evidence validity cannot establish governance authorization.

### Proof schema P3 — decision / transition separation

D_6 is total on admissible requests while Delta_6 is partial. Therefore a decision outcome is not equivalent to transition existence.

F6-BLOCK, F6-DEFER, F6-REVALIDATE, and F6-REAUTHORIZE each keep the ordinary target transition undefined under their frozen semantics.

F6-ADMIT is necessary but not sufficient for consequential target transition existence because operation-specific preconditions remain independently required.

### Proof schema P4 — delegation attenuation

Programmable delegated authority is source-bound, scoped, temporally valid, and attenuated. Therefore no delegate may produce authority broader than its admitted parent authority.

### Proof schema P5 — representational state separation

Contract state and on-chain state are representational surfaces. Because F6 preserves contract-state truth classification independently from authority and admissibility, state representation cannot constitute authoritative economic truth or governance authority.

## Counterexample discharge

F6-PO-033 through F6-PO-044 are discharged by explicit counterexample construction.

- F6-PO-033 — A deployed contract can execute successfully while A_t = ABSENT; therefore successful execution does not imply governance authority.
- F6-PO-034 — A technically valid invocation can occur while authority status is REVOKED; therefore invocation validity does not imply admissibility.
- F6-PO-035 — P_t = SATISFIED can coexist with an out-of-scope request; therefore condition satisfaction does not imply authorization.
- F6-PO-036 — O_t = VERIFIED can coexist with A_t = ABSENT; therefore verified oracle input does not imply financial authority.
- F6-PO-037 — R_t = ACTIVE can coexist with G_t = DENIED; therefore privileged control capability does not imply authorization.
- F6-PO-038 — An upgrade credential can remain technically usable after authority revocation; therefore upgrade capability does not imply valid upgrade authority.
- F6-PO-039 — A ledger can accept a technically valid state transition while governance authorization is denied; therefore on-chain acceptance does not imply admissibility.
- F6-PO-040 — Immutable code may remain executable after authority expiry; therefore immutability does not imply continuing governance mandate.
- F6-PO-041 — Contract state may report a value inconsistent with corroborating authoritative evidence; therefore contract state does not constitute economic truth.
- F6-PO-042 — Automated execution can occur without an admitted economic principal; therefore automation does not imply principal authority.
- F6-PO-043 — Execution evidence may exist while authority evidence is absent; therefore execution evidence does not imply authority evidence.
- F6-PO-044 — F6-ADMIT may be produced while an operation-specific transition precondition remains false; therefore ADMIT does not guarantee transition existence.

## Traceability discharge

F6-PO-045 through F6-PO-048 are discharged.

- F6-PO-045: all 40 canonical F6 invariants map into the frozen proof obligation registry.
- F6-PO-046: each proof obligation derives from a frozen invariant, non-collapse condition, decision rule, transition rule, or authority boundary.
- F6-PO-047: all runtime-conformance obligations map to frozen F6 decision, transition, authority, evidence, or state-separation semantics.
- F6-PO-048: all counterexample obligations map to explicit F6 non-equivalence or non-collapse requirements.

## Runtime obligations remaining OPEN

- F6-PO-049: OPEN — requires reference runtime conformance.
- F6-PO-050: OPEN — requires reference runtime conformance.
- F6-PO-051: OPEN — requires reference runtime conformance.
- F6-PO-052: OPEN — requires reference runtime conformance.
- F6-PO-053: OPEN — requires reference runtime conformance.
- F6-PO-054: OPEN — requires reference runtime conformance.
- F6-PO-055: OPEN — requires reference runtime conformance.
- F6-PO-056: OPEN — requires reference runtime conformance.
- F6-PO-057: OPEN — requires reference runtime conformance.
- F6-PO-058: OPEN — requires reference runtime conformance.

## Discharge control

No runtime-conformance obligation is discharged by this pass.

No claim of full F6 technical closure is made by FIN-F6-08.

## Next

FIN-F6-09 — REFERENCE RUNTIME CONSTRUCTION / CONFORMANCE
