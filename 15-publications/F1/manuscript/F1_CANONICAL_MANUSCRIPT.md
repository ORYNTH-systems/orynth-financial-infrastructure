# Partial Settlement, Compensating Execution, and Economic-State Continuity

## A Formal Architecture for Financial State After Consequential Execution Has Begun

**Ashley S. Harris**

ORYNTH Systems

---

## Abstract

Financial execution governance is commonly strongest before consequential state
change occurs: an action may be authorized, rejected, admitted, blocked, or
prevented before settlement effectuation begins. A different problem arises once
financially consequential mutation has already occurred, has only partially
occurred, or cannot be established to have not occurred.

This paper develops a formal post-effect architecture for that problem. It
separates intended, observed, committed, economically recognized, and unresolved
financial effects; defines determinate classifications for no effect, partial
effect, completed effect, and indeterminate effect; models compensation and
reversal as distinct independently governed consequential executions; defines
financial reconciliation as a partial epistemic operator rather than a repair
operation; and classifies economic-state continuity as preserved, degraded,
broken, reconstructed, or indeterminate.

A central result is that recovery of economic equivalence does not erase
execution history. Compensation, reversal, reconciliation, and reconstructed
continuity therefore remain distinct from restoration of an uninterrupted prior
state.

The formal model is accompanied by a deterministic reference runtime and an
adversarial verification surface. Formal proof results, constructive
counterexamples, and reference-runtime conformance results are reported
separately so that implementation evidence is not represented as mathematical
proof and mathematical results are not represented as production certification.

---

# 1. Introduction

Financial systems routinely distinguish whether a proposed transaction is
authorized, admissible, executable, settled, or rejected. Those distinctions are
essential before consequential financial state mutation begins.

They do not completely answer the post-effect problem.

Once an execution changes financial state, changes only part of the intended
state, reaches an external system whose state is not yet observable, or leaves
uncertain whether a consequential mutation occurred, the relevant governance
question changes.

The question is no longer only:

> May this execution occur?

It becomes:

> What occurred, what remains unresolved, what repair may now be proposed, what
> authority governs that repair, what current state can be established, and what
> continuity survived the execution history?

This paper addresses that second problem.

The architecture is intentionally post-effect. It does not redefine the upstream
authority, admissibility, execution-prevention, or generic execution-integrity
mechanisms on which it depends.

Its principal claim is structural:

> A financially repaired endpoint does not imply an uninterrupted execution
> history.

Accordingly, the architecture refuses several collapses that are convenient in
implementation but unsafe in formal reasoning:

- observed effect is not necessarily committed effect;
- committed effect is not necessarily final effect;
- failure does not create authority to compensate;
- reversal eligibility does not create reversal authority;
- compensation is not reversal;
- local rollback is not necessarily economic reversal;
- reconciliation is not repair;
- reconciliation is not restoration;
- economic equivalence is not historical identity;
- reconstructed continuity is not preserved continuity.

The purpose of the model is not to prescribe one banking, blockchain, custody,
clearing, or payment system. It establishes a common post-effect reasoning layer
that those domains may later specialize.

---

# 2. Problem Boundary and Architectural Lineage

## 2.1 Pre-Effect and Post-Effect Governance

Let e be a financial execution event.

The F1 domain begins once consequential economic mutation is evidenced, or once
the system has crossed the relevant effectuation boundary and can no longer
establish that no consequential mutation occurred.

The boundary can be represented by an applicability predicate:

B_F1(e,t).

B_F1(e,t) = 0 denotes execution remaining outside the novel post-effect domain.

B_F1(e,t) = 1 denotes execution requiring post-effect financial reasoning.

Software process execution alone is insufficient to establish this condition.

Thus:

software execution begun

is not equivalent to:

economic mutation begun.

This distinction is necessary for asynchronous, multi-party, externally committed,
and partially observable settlement systems.

## 2.2 Inherited Architecture

F1 inherits rather than redefines upstream mechanisms governing:

- authority;
- current admissibility;
- execution authorization;
- consequential-boundary control;
- execution-prevention;
- generic execution integrity;
- generic reconstruction;
- governed refusal evidence.

The post-effect model therefore begins from an already governed execution
environment.

## 2.3 Research Question

The central research question is:

> When a financially consequential execution has already caused, may have caused,
> or cannot be proved not to have caused economic mutation, what formal conditions
> govern containment, compensation, reversal, reconciliation, and continuity
> classification without falsely treating later recovery as erasure of the
> original execution history?

---

# 3. Post-Effect Financial State Algebra

## 3.1 Intended Effect

For a financial execution e define:

M*(e)

as the finite set of intended economically consequential mutations.

Membership in M*(e) denotes intended effect, not established occurrence.

## 3.2 Observed Mutation

Define:

M_obs(e,t)

as the intended mutations reported as having occurred by a conformant observation
mechanism at time t.

Observation is epistemic and may lag or precede other system boundaries.

## 3.3 Committed Mutation

Define:

M_com(e,t)

as intended mutations established to have crossed their applicable commitment
boundary.

Commitment does not by itself establish authority, legitimacy, or finality.

## 3.4 Economically Recognized Effect

Define:

M_econ(e,t)

as the intended mutations currently recognized as economically consequential
effects attributable to e.

The model does not generally assume:

M_obs(e,t) = M_com(e,t) = M_econ(e,t).

## 3.5 Knowledge State

Define:

K_pos(e,t)

as mutations whose occurrence is established.

Define:

K_neg(e,t)

as mutations whose non-occurrence is established.

Then:

K(e,t) = K_pos(e,t) union K_neg(e,t).

The unresolved set is:

M_unr(e,t) = M*(e) \ K(e,t).

## 3.6 Effect Classifier

The canonical immediate effect classifier is:

C_F1(e,t) in {
    NO-EFFECT,
    PARTIAL,
    COMPLETED,
    INDETERMINATE
}.

NO-EFFECT requires complete material knowledge and no recognized economic effect.

PARTIAL requires complete material knowledge and a strict non-empty proper subset
of the intended effect.

COMPLETED requires complete material knowledge and recognized economic effect equal
to the intended effect set.

INDETERMINATE preserves unresolved material occurrence state rather than silently
classifying it as zero effect.

---

# 4. Partial Settlement

Partial effect is not merely failure.

For complete relevant knowledge:

K(e,t) = M*(e)

and:

empty proper-subset M_econ(e,t) proper-subset M*(e)

the execution is classified:

C_F1(e,t) = PARTIAL.

Partiality is therefore set-structural rather than merely percentage-based.

For multi-leg settlement:

M*(e) = {m_1,...,m_n}

a strict subset may have crossed economically consequential boundaries while the
remaining intended mutations did not.

The architecture additionally permits profile-specific weighting and dependency
relations, but effect-set identity remains primary. Equal percentages do not imply
equivalent financial states.

A locally rolled-back system may therefore remain globally partial where an
external mutation survives.

---

# 5. Compensating Execution

## 5.1 Compensation as a New Execution

Let e_0 denote the originating execution.

A compensation proposal is separately instantiated:

e_c = CompensationProposal(e_0,S_t,g_c).

Require:

e_c != e_0.

Compensation does not mutate the identity of the originating execution.

## 5.2 Repair Need and Repair Authority

The requirement for repair is separate from authority to repair.

Therefore:

Failure(e_0)

does not imply:

Authority(e_c).

Likewise:

NeedCompensation(e_0,S_t)

does not imply:

Authority(e_c).

A compensation event must independently satisfy the governing authority,
scope, admissibility, and consequential-boundary requirements before execution.

## 5.3 Compensation Is Consequential

A compensation execution is itself financially consequential.

It therefore has its own intended effect set and may itself result in:

NO-EFFECT,

PARTIAL,

COMPLETED,

or:

INDETERMINATE.

A failed repair does not create unlimited recursive repair authority.

Every later repair remains independently instantiated and governed.

## 5.4 Economic Restoration Without Historical Erasure

Suppose:

S_0 --e_0--> S_1 --e_c--> S_2

and:

S_2 equivalent_E S_0.

This establishes at most the declared economic-equivalence relation.

It does not establish historical identity because the history of S_2 includes the
originating and compensating events.

Therefore:

S_2 equivalent_E S_0

does not imply:

S_2 =_H S_0.

---

# 6. Reversal

## 6.1 Counter-Transition

A reversal is a separately governed counter-transition associated with an existing
financial effect.

Let:

S_0 --e_0--> S_1.

A reversal candidate is:

e_r = ReversalProposal(e_0,S_1,g_r).

Require:

e_r != e_0.

If independently admitted:

S_1 --e_r--> S_2.

The original edge remains part of history.

## 6.2 Four Independent Propositions

The architecture distinguishes:

1. reversal eligibility;
2. reversibility;
3. reversal authority;
4. successful reversal.

These propositions are not synonyms.

A reversal mechanism may exist while current state is no longer reversible.

A state may be reversible while no actor has authority to reverse it.

An actor may hold authority while current scope or admissibility prevents
execution.

An admitted reversal may itself partially effect or become indeterminate.

## 6.3 Reversal Is Not Compensation

Compensation introduces a new economic effect intended to offset or repair prior
consequences.

Reversal specifically counter-transitions a prior effect under a recognized
reversal mechanism.

Therefore:

Reversal != Compensation.

## 6.4 Reversal Is Not Rollback

Local software rollback does not establish economic reversal when a consequential
external effect remains.

Therefore:

LocalRollback != FinancialReversal.

---

# 7. Financial Reconciliation

## 7.1 Purpose

Reconciliation answers:

> What current financial state can be established?

It does not answer:

> How can prior history be made to disappear?

## 7.2 Reconciliation Input

Define:

X_t = (H_t,E_t,O_t,R_t,D_t)

where:

H_t = execution history,

E_t = evidence state,

O_t = obligation state,

R_t = resource state,

D_t = dependency state.

## 7.3 Partial Reconciliation Operator

Define:

R_F1 :
H x E x O x R x D
partial-arrow
S.

The operator is intentionally partial.

Not every post-effect condition permits a unique acceptable reconstructed current
state.

## 7.4 Result Classes

The reconciliation surface distinguishes:

RECONCILED,

RECONCILIATION-INDETERMINATE,

RECONCILIATION-FAILED.

INDETERMINATE represents unresolved evidence, dependencies, or candidate-state
ambiguity.

FAILED represents contradiction or failure of required acceptance conditions.

## 7.5 Reconciled Is Not Restored

A current state may be determinately established while differing materially from
the pre-origin state.

Thus:

Reconciled != Restored.

Likewise:

Reconciled != ContinuityPreserved.

---

# 8. Economic-State Continuity

## 8.1 Continuity as a Path Property

Continuity is evaluated over history, not merely over the terminal financial
state.

Let:

H_t = <e_0,e_1,...,e_n>.

Let:

Gamma = {gamma_1,...,gamma_k}

denote the declared continuity requirements of a financial profile.

Define:

C_F1(H_t,S_R,Gamma)

with range:

{
    PRESERVED,
    DEGRADED,
    BROKEN,
    RECONSTRUCTED,
    INDETERMINATE
}.

## 8.2 Preserved

PRESERVED requires relevant continuity relations to remain satisfied throughout
the complete required interval.

No qualifying break may have occurred.

## 8.3 Degraded

DEGRADED represents a bounded profile-defined impairment that does not meet the
threshold for a qualifying break.

## 8.4 Broken

BROKEN requires evidence of a qualifying violation of at least one required
continuity relation without an accepted reconstruction describing the current
continuity state.

## 8.5 Reconstructed

RECONSTRUCTED requires:

break

followed by:

accepted reconstruction.

Therefore reconstructed continuity contains a historical discontinuity.

It is not equivalent to preserved continuity.

## 8.6 Indeterminate

If material continuity evidence remains unresolved:

C_F1 = INDETERMINATE.

The system may not infer PRESERVED from absence of known break evidence.

## 8.7 Endpoint Non-Sufficiency

Two histories may terminate in economically equivalent states while possessing
different continuity classifications.

Therefore:

S_final equivalent_E S_initial

does not imply:

ContinuityPreserved.

---

# 9. Formal Results

The F1 proof corpus distinguishes positive formal results from constructive
non-equivalence results.

## 9.1 Effect Classification

Under the F1 definitions:

[K = M* AND empty proper-subset M_econ proper-subset M*]

implies:

C_F1 = PARTIAL.

This result is formally established through definitional derivation.

Similarly:

[K = M* AND M_econ = empty]

implies:

NO-EFFECT,

and:

[K = M* AND M_econ = M*]

implies:

COMPLETED.

Materially incomplete knowledge excludes these determinate classifications and
therefore yields INDETERMINATE under the F1 classifier.

## 9.2 Compensation Authority Non-Implication

The implication:

Failure(e_0) => Authority(e_c)

does not hold.

A constructive model exists in which the originating execution fails while no
current authority exists for compensation.

This result is counterexample-discharged.

## 9.3 Reversal Authority Non-Implication

Likewise:

EligibleReverse(e_0) => Authority(e_r)

does not hold.

Structural availability of a reversal mechanism does not create an authorized
principal.

This result is counterexample-discharged.

## 9.4 Economic Equivalence and Historical Identity

The implication:

S_after equivalent_E S_before

=>

S_after =_H S_before

does not hold.

A compensation or reversal history provides a constructive witness with equal
selected economic observables but different execution histories.

## 9.5 Reconciliation and Continuity

The implication:

Reconciled(S_R)

=>

ContinuityPreserved

does not hold.

A financial state can be determinately reconciled while evidence establishes that
continuity was previously broken.

## 9.6 Preserved and Reconstructed Continuity

For the same complete continuity interval:

PRESERVED

requires absence of a qualifying break.

RECONSTRUCTED

requires existence of a qualifying prior break.

Therefore the two classifications are mutually exclusive for that interval.

This result is formally proved.

---

# 10. Executable Reference Runtime

The formal architecture is accompanied by a deterministic Python reference
implementation.

The runtime implements:

FinancialExecutionEvent

-> EffectClassifier

-> Compensation/Reversal Admission

-> Consequential Boundary Permit

-> Reconciliation

-> Continuity Classification

-> Evidence Recording.

## 10.1 Consequential Boundary

Compensation and reversal do not independently create successful execution permits.

They invoke an authority/admission evaluator and the consequential boundary
controller.

Within the reference implementation, successful BoundaryPermit construction is
confined to the boundary-controller module.

## 10.2 Evidence

The reference ledger preserves separately represented originating, repair,
reconciliation, and continuity records through its public interface.

Returned records are copies and therefore cannot be used to mutate the retained
in-memory records indirectly.

This is an in-memory reference property.

It is not a claim of cryptographic immutability or durable persistence.

---

# 11. Adversarial Runtime Verification

FIN-F1-09 subjected the reference implementation to explicit attempts to violate
the F1 architecture.

The tested attack surface included attempts to:

- derive compensation permission from originating failure;
- derive reversal permission from eligibility or reversibility;
- reuse originating event identities for repair;
- use stale authority;
- execute under invalid scope;
- bypass the consequential boundary controller;
- introduce mutations outside the intended mutation universe;
- collapse unresolved effects into NO-EFFECT;
- classify contradictory occurrence evidence determinately;
- force reconciliation to choose arbitrarily among multiple candidate states;
- reconcile with missing provenance;
- mutate returned evidence objects to erase retained history;
- remove the originating event after repair;
- classify reconstructed continuity as preserved;
- claim reconstruction without a represented prior break.

The tested runtime-dependent proof burdens satisfied the reference-runtime
conformance gate.

This result is intentionally narrower than formal proof.

It establishes conformance of the tested reference runtime under the documented
attack surface.

---

# 12. Discussion

The principal structural implication of the architecture is that financial
recovery must be represented as history-preserving execution rather than
state erasure.

A system that returns to the same observable balances may nevertheless have passed
through:

- unauthorized effect,
- partial settlement,
- compensation,
- reversal,
- unresolved obligation,
- continuity break,
- reconstruction.

Those differences matter because terminal-state equivalence cannot establish how
the state was reached.

The architecture therefore treats recovery as additive to history.

Compensation adds an execution.

Reversal adds a counter-transition.

Reconciliation adds a determination.

Reconstruction adds a continuity classification.

None subtracts the originating history.

This creates a consistent foundation for later specialization into multi-party
clearing, settlement finality, distributed ledgers, custody, programmable finance,
cross-jurisdiction execution, and autonomous economic agency.

---

# 13. Limitations and Non-Claims

This work does not claim:

- that every financial system has identical settlement semantics;
- that every economic effect is reversible;
- that every partial effect can be compensated;
- that compensation restores historical identity;
- that reversal erases execution history;
- that reconciliation establishes legitimacy;
- that reconciliation establishes continuity preservation;
- that finality and irreversibility are equivalent;
- that distributed consensus establishes execution authority;
- that possession of a cryptographic key establishes execution authority;
- that the reference runtime is production infrastructure;
- that the reference ledger is cryptographically immutable;
- that runtime conformance constitutes universal formal proof;
- that the model itself constitutes regulatory certification.

Distributed settlement, custody, programmable finance, jurisdiction, and
autonomous economic agency require later specialization.

---

# 14. Conclusion

Pre-effect financial governance asks whether an execution may proceed.

Post-effect financial governance must answer a harder question: what happened
after consequential state change began, and what can legitimately happen next?

The F1 architecture formalizes that boundary.

It distinguishes intended, known, economically recognized, and unresolved effects;
defines partial settlement; treats compensation and reversal as separately governed
consequential executions; defines reconciliation as a partial determination
operator; and classifies continuity over historical execution paths rather than
terminal balances.

The resulting principle is simple but structurally consequential:

> Repair can restore economic relations without restoring an uninterrupted
> history.

A financial system can therefore recover function, reconcile state, reverse an
effect, compensate an obligation, or reconstruct continuity while still preserving
evidence that a consequential disruption occurred.

That distinction provides the foundation for the remaining ORYNTH financial
infrastructure family.

---

# Appendix A — Canonical F1 Definitions

## A.1 Intended Mutation Set

M*(e)

Complete intended economically consequential mutation set.

## A.2 Economically Recognized Effect

M_econ(e,t)

Economically consequential mutations currently attributed to execution e.

## A.3 Knowledge Set

K(e,t) = K_pos(e,t) union K_neg(e,t).

## A.4 Unresolved Set

M_unr(e,t) = M*(e) \ K(e,t).

## A.5 Effect Classifier

C_F1(e,t) in {
NO-EFFECT,
PARTIAL,
COMPLETED,
INDETERMINATE
}.

## A.6 Reconciliation

R_F1 :
H x E x O x R x D
partial-arrow
S.

## A.7 Continuity

C_F1(H,S,Gamma) in {
PRESERVED,
DEGRADED,
BROKEN,
RECONSTRUCTED,
INDETERMINATE
}.

---

# Appendix B — Proof-Status Doctrine

The manuscript uses three distinct result categories:

1. FORMALLY PROVED
2. COUNTEREXAMPLE-DISCHARGED
3. REFERENCE-RUNTIME CONFORMANT

These categories are intentionally non-interchangeable.

The complete machine-readable proof disposition is maintained in:

03-registries/F1_PROOF_DISCHARGE_REGISTRY.csv

and runtime closure in:

03-registries/F1_RUNTIME_PROOF_CLOSURE.csv.

---

# Appendix C — Constructive Non-Equivalence Results

The F1 corpus includes constructive witnesses establishing that:

Failure(e_0)
does not imply
Authority(e_c).

EligibleReverse(e_0)
does not imply
Authority(e_r).

Economic equivalence
does not imply
historical identity.

Reconciled state
does not imply
continuity preservation.

Functional recovery
does not imply
continuity preservation.

---

# Appendix D — Reference Runtime Conformance

The runtime-dependent proof burdens are separately recorded in:

03-registries/F1_RUNTIME_PROOF_CLOSURE.csv.

RUNTIME-CONFORMANT means the tested reference implementation behaved consistently
with the specified property under the FIN-F1-09 attack surface.

It does not convert the underlying proposition into a universal implementation
theorem.

---

# Appendix E — Adversarial Verification

The complete adversarial matrix is maintained in:

03-registries/F1_ADVERSARIAL_VERIFICATION_MATRIX.csv.

Each attack records:

Proof Burden
-> Attack
-> Expected Result
-> Observed Result
-> Verdict.

---

# Appendix F — Traceability

The F1 manuscript is derived from:

FIN-F1-01 — exact problem boundary

FIN-F1-02 — post-effect state algebra

FIN-F1-03 — compensation semantics

FIN-F1-04 — reversal semantics

FIN-F1-05 — reconciliation semantics

FIN-F1-06 — economic-state continuity

FIN-F1-07 — formal proof discharge

FIN-F1-08 — reference implementation

FIN-F1-09 — adversarial runtime verification.

The manuscript introduces no new canonical F1 semantic layer.
