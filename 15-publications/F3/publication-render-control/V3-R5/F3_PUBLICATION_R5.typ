#set page(
  paper: "us-letter",
  margin: (
    top: 0.62in,
    bottom: 0.60in,
    left: 0.67in,
    right: 0.67in
  ),
  numbering: "1",
  header: context {
    if counter(page).get().first() > 1 {
      set text(
        font: "Arial",
        size: 7.2pt
      )
      grid(
        columns: (1fr, auto),
        gutter: 0.20in,
        [ORYNTH FINANCIAL SYSTEMS SERIES],
        [OBLIGATION FINALITY — F3]
      )
      v(2pt)
      line(
        length: 100%,
        stroke: 0.4pt
      )
    }
  }
)

#set text(
  font: "Times New Roman",
  size: 9.7pt,
  hyphenate: false
)

#set par(
  justify: true,
  leading: 0.64em,
  first-line-indent: 0pt
)

#set heading(numbering: none)

#show heading.where(level: 1): it => block(
  above: 7pt,
  below: 4pt,
  breakable: false,
  text(
    font: "Arial",
    weight: "bold",
    size: 10pt,
    it.body
  )
)

#show heading.where(level: 2): it => block(
  above: 7pt,
  below: 3pt,
  breakable: false,
  text(
    font: "Arial",
    weight: "bold",
    size: 9pt,
    it.body
  )
)

#show heading.where(level: 3): it => block(
  above: 6pt,
  below: 2pt,
  breakable: false,
  text(
    font: "Arial",
    weight: "bold",
    size: 8pt,
    it.body
  )
)

#show strong: it => [#it.body]

#set table(
  stroke: 0.45pt,
  inset: 3pt
)

#align(center)[
  #text(
    font: "Arial",
    size: 7.5pt,
    weight: "bold",
    tracking: 0.08em
  )[ORYNTH FINANCIAL SYSTEMS SERIES]

  #v(10pt)

  #text(
    font: "Arial",
    size: 17pt,
    weight: "bold"
  )[
    Obligation Finality, Custody-State Integrity, \
    and Consequential Financial Closure
  ]

  #v(6pt)

  #text(
    font: "Times New Roman",
    size: 10pt,
    style: "italic"
  )[Finality ≠ consequential closure.]

  #v(8pt)

  #text(
    font: "Arial",
    size: 9pt,
    weight: "bold"
  )[Ashley S. Harris]

  #v(1.5pt)

  #text(
    font: "Arial",
    size: 8pt
  )[ORYNTH Systems]

  #v(1.5pt)

  #text(
    font: "Arial",
    size: 7.5pt
  )[F3]
]

#v(12pt)

#let house-body(body) = columns(
  2,
  gutter: 0.31in,
  body
)

#house-body[


== Abstract
<abstract>
Financial systems frequently treat completion, finality, custody, and
closure as interchangeable terminal concepts. F3 rejects that collapse.

This paper formalizes obligation finality, custody-state integrity, and
consequential financial closure as distinct governed conditions. Its
controlling separation is finality ≠ consequential closure.

The architecture further preserves settlement completion, execution
completion, atomic completion, reconciliation, custody possession,
custody authority, evidence, reversibility, and closure validity as
independently evaluable relations.

== 1. Problem
<problem>
An economic obligation may appear complete while one or more governance
conditions necessary for valid closure remain unresolved.

Likewise, a system may possess assets, complete execution, reconcile
records, or atomically complete a transaction without establishing valid
obligation finality.

F3 therefore separates observable completion states from
governance-valid consequential closure.

== 2. Canonical Boundary
<canonical-boundary>
F3 governs obligation finality, custody-state integrity, consequential
financial closure, finality evidence, custody authority, reversibility,
and closure-state classification.

F3 does not permit execution success, settlement completion, atomicity,
reconciliation, custody possession, or apparent closure to self-prove
finality or valid closure.

== 3. Obligation Finality
<obligation-finality>
Obligation finality describes a governed state in which the applicable
finality requirements for an obligation are satisfied.

It is not reducible to successful execution or visible settlement
completion.

Settlement completion ≠ obligation finality.

Execution completion ≠ finality.

Atomic completion ≠ finality.

== 4. Consequential Financial Closure
<consequential-financial-closure>
Consequential financial closure concerns whether the governed financial
consequence is validly closed under the applicable authority, state,
evidence, and finality conditions.

Finality ≠ consequential closure.

A state may be final under one domain while remaining open, defective,
or unresolved under another closure requirement.

== 5. Custody-State Integrity
<custody-state-integrity>
Custody-state integrity requires preserving the distinction between
possession, control capability, legal or governance authority, delegated
authority, and the actual custody state represented by the system.

Custody possession ≠ custody authority.

Possession of an asset, credential, key, account, or technical control
surface does not by itself establish authority to exercise consequential
custody actions.

== 6. Reconciliation and Finality
<reconciliation-and-finality>
Reconciliation may establish that records or represented states align
under a defined comparison process.

It does not independently establish finality.

Reconciliation ≠ finality.

A reconciled obligation may still fail authority, custody, closure,
temporal, or other finality requirements.

== 7. Finality and Irreversibility
<finality-and-irreversibility>
Finality is also distinct from irreversibility.

Finality ≠ irreversibility.

A financial state may be final under a governed regime while remaining
reopenable, reversible, revocable, supersedable, or otherwise mutable
through separately authorized processes.

== 8. Evidence and Apparent Closure
<evidence-and-apparent-closure>
Evidence that a system reports completion or closure is evidence of
system state or process behavior.

It is not sufficient by itself to establish valid consequential closure.

Apparent closure ≠ valid consequential closure.

Closure validity must remain traceable to the applicable canonical
authority, state, custody, and finality requirements.

== 9. Core Non-Equivalence Results
<core-non-equivalence-results>
+ Obligation finality ≠ consequential financial closure.
+ Settlement completion ≠ obligation finality.
+ Custody possession ≠ custody authority.
+ Possession alone ≠ custody-state integrity.
+ Execution completion ≠ finality.
+ Atomic completion ≠ finality.
+ Reconciliation ≠ finality.
+ Finality ≠ irreversibility.
+ Apparent closure ≠ valid consequential closure.
+ Successful financial execution ≠ retroactive obligation closure.

== 10. Runtime and Adversarial Verification
<runtime-and-adversarial-verification>
The F3 canonical technical surface tests obligation-finality conditions,
custody-state distinctions, closure-state evaluation, authority
non-implication, execution / finality separation, and adversarial
attempts to infer closure from incomplete evidence.

These results are bounded verification evidence for the implemented
canonical F3 surface. They are not universal empirical guarantees.

== 11. Cross-Family Interfaces
<cross-family-interfaces>
F3 inherits F1 distinctions between settlement, reconciliation, history,
repair, and continuity and F2 distinctions between distributed agreement
and authority.

Later financial families may depend on F3 finality and #box[custody-state]
semantics without collapsing them into ledger representation,
cryptographic possession, programmable execution, jurisdictional reach,
or autonomous economic capability.

== 12. Limits and Non-Claims
<limits-and-non-claims>
This paper does not claim production deployment, regulatory approval,
institutional adoption, external certification, customer validation,
legal sufficiency, or universal prevention of financial closure failure.

The claims are limited to the canonical F3 technical architecture,
formal distinctions, runtime behavior, proof surfaces, and adversarial
evidence bound in FIN-PUB-12.

== 13. Conclusion
<conclusion>
Financial closure cannot be inferred merely because execution completed,
records reconciled, custody exists, or a system reports a terminal
state.

F3 formalizes the distinction between obligation finality, #box[custody-state]
integrity, and consequential closure so that each remains independently
inspectable and governed.

The resulting architecture prevents terminal-state appearance from
substituting for valid authority, valid custody, or valid financial
closure.
]