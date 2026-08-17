# FIN-F2-09 — Positive Formal Proof Discharge

The proofs below are limited to consequences of the locked F2
definitions. They do not claim protocol universality beyond those
definitions.

---

## F2-THM-001 — Authority Completeness Does Not Collapse Participant Roles

### Claim

AuthorityComplete(q,t) is a collective satisfaction property over
applicable authority requirements and does not require a single actor
to instantiate all required authority roles.

### Basis

AuthorityComplete(q,t) holds iff every applicable rho in AR(q,t) is
satisfied.

Satisfied(rho,q,t) requires existence of an actor holding the authority
required by rho.

The definition quantifies independently over requirements.

### Discharge

No clause requires the same actor to satisfy every rho.

Therefore multiple actors may jointly satisfy AR(q,t).

Status: PROVED

---

## F2-THM-002 — Consensus Cannot Establish Authority Completeness

### Claim

Consensus(q,phi,t|CP) does not imply AuthorityComplete(q,t).

### Basis

Consensus is defined only by the active consensus profile's collective
recognition condition.

AuthorityComplete is defined independently by satisfaction of every
applicable authority requirement in AR(q,t).

### Discharge

A model may satisfy CP while at least one required authority predicate
is false.

Therefore the implication is not valid.

Positive universal implication status: REFUTED

Semantic non-implication status: COUNTEREXAMPLE-DISCHARGED

---

## F2-THM-003 — Distributed Admission Is Distinct From Execution

### Claim

Admissible_d(q_d,t) does not establish Executed(q_d,t).

### Basis

Admissibility is defined as satisfaction of applicable pre-execution
conditions.

Execution is a later attempted transition.

### Discharge

An admitted proposal may have no execution attempt.

Thus admission and execution are formally distinct.

Status: PROVED

---

## F2-THM-004 — Atomic Partiality Maps to F1 PARTIAL

### Claim

Under sufficient evidence, if the recognized distributed economic
mutation set is a strict non-empty subset of the intended distributed
mutation set, the F1 PARTIAL classification applies.

### Basis

F2 defines:

empty proper subset:

M_d,econ(q_d,t) proper-subset M*_d(q_d)

with non-empty recognized effect.

F1 owns the PARTIAL meaning.

### Discharge

F2 specializes only the distributed cause and binds the strict-subset
condition to the inherited F1 classifier.

Status: PROVED

---

## F2-THM-005 — Atomic Completion Does Not Establish Settlement Finality

### Claim

AtomicComplete(q_d,t|AP) does not imply
SettlementFinal(q_d,t|FP,D_f).

### Basis

AtomicComplete requires all AP-required leg effects.

SettlementFinal requires all FP-required finality obligations for D_f.

FP may contain obligations not present in AP.

### Discharge

Construct a profile where all AP leg effects are satisfied while an
external finality recognition remains pending.

AtomicComplete is true while SettlementFinal is false.

Status: COUNTEREXAMPLE-DISCHARGED

---

## F2-THM-006 — Local Finality Does Not Propagate Automatically

### Claim

LocalFinal(q_d,t,D_1) does not imply LocalFinal(q_d,t,D_2).

### Basis

Finality is domain-relative.

Each domain may possess a distinct requirement set.

### Discharge

D_1 requirements may all be satisfied while at least one D_2 requirement
is pending or unsatisfied.

Status: COUNTEREXAMPLE-DISCHARGED

---

## F2-THM-007 — Settlement Finality Does Not Imply Irreversibility

### Claim

SettlementFinal(q_d,t|FP,D_f) does not imply Irreversible(q_d).

### Basis

Finality is status under a profile.

The architecture separately permits new authorized reversal or
counter-transition where governing rules allow one.

### Discharge

A settlement may satisfy all finality conditions and later undergo a new
authorized reversal.

Therefore finality and irreversibility are distinct.

Status: COUNTEREXAMPLE-DISCHARGED

---

## F2-THM-008 — Reconciliation Does Not Mutate Financial State

### Claim

R_d(q_d,t|GR) alone does not perform a consequential financial mutation.

### Basis

R_d is defined as an evidence/classification operator.

All consequential repair actions require separate authority and
admissibility.

### Discharge

No transition rule in R_d authorizes or instantiates compensation,
reversal, re-execution, or state overwrite.

Status: PROVED

---

## F2-THM-009 — Canonical Branch Selection Does Not Erase History

### Claim

Selection of CanonicalBranch(q_d,t|GR) does not imply that other
historically evidenced branches never existed.

### Basis

Canonicality is a current governing selection over evidenced branches.

Historical branch evidence persists by invariant.

### Discharge

Current canonical selection and historical existence are not mutually
exclusive.

Status: PROVED

---

## F2-THM-010 — Reconstructed Continuity Is Not Preserved Continuity

### Claim

RECONSTRUCTED != PRESERVED.

### Basis

RECONSTRUCTED requires a prior interval whose lineage had to be rebuilt.

PRESERVED requires no continuity-breaking gap and no reconstruction for
the classified interval.

### Discharge

The predicates have incompatible defining conditions for the same
historical interval.

Status: PROVED

---

## F2-THM-011 — Current Preservation Does Not Erase Historical Break

### Claim

CurrentContinuity(q_d,t_now)=PRESERVED does not imply every prior
interval was PRESERVED.

### Basis

CurrentContinuity and HistoricalContinuity are explicitly separate
evaluations.

### Discharge

A prior BROKEN interval may be followed by reconstruction and a new
clean preserved interval.

Status: COUNTEREXAMPLE-DISCHARGED

---

## F2-THM-012 — Full Semantic Chain Is Non-Collapsible

### Claim

The architecture preserves the distinctions:

agreement
!= consensus
!= authority
!= admissibility
!= execution
!= effect occurrence
!= atomic completion
!= settlement finality
!= reconciliation
!= continuity preservation

### Basis

Each object has an independently defined predicate, requirement set,
classification surface, or operator.

### Discharge

The locked definitions contain no identity rule collapsing adjacent
layers, and the non-implication obligations supply explicit models where
one property can hold without the next.

Status: PROVED for definitional distinctness.

Universal non-implication coverage remains represented separately in the
counterexample register.
