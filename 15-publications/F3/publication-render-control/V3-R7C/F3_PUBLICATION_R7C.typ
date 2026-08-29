#set page(
  paper: "a4",
  margin: (
    left: 16mm,
    right: 16mm,
    top: 16mm,
    bottom: 17mm,
  ),
  header-ascent: 6mm,
  footer-descent: 7mm,

  header: context {
    if counter(page).get().first() > 1 {
      set text(
        font: "Nimbus Sans",
        size: 7.1pt,
        fill: rgb("#4B4F54"),
        tracking: 0.45pt,
      )

      block(width: 100%)[
        #grid(
          columns: (1fr, 1fr),
          [ORYNTH FINANCIAL SYSTEMS SERIES],
          align(right)[OBLIGATION FINALITY · F3],
        )
      ]
    }
  },

  footer: context {
    set text(
      font: "Nimbus Sans",
      size: 7.3pt,
      fill: rgb("#55595E"),
    )

    align(center)[
      #counter(page).display()
    ]
  },
)

#set text(
  font: "Libertinus Serif",
  size: 9pt,
  fill: black,
  hyphenate: false,
)

#set par(
  justify: true,
  linebreaks: "optimized",
  leading: 0.56em,
  spacing: 0.62em,
  first-line-indent: 0pt,
)

#set heading(numbering: none)

#show heading.where(level: 2): it => {
  block(
    above: 12pt,
    below: 5.5pt,
    breakable: false,
  )[
    #set text(
      font: "Libertinus Serif",
      size: 10.2pt,
      weight: "semibold",
      tracking: 0.18pt,
    )

    #it.body

    #v(2.5pt)

    #line(
      length: 100%,
      stroke: 0.45pt + rgb("#73777C"),
    )
  ]
}

#let body-columns(body) = {
  columns(
    2,
    gutter: 5.5mm,
    body,
  )
}

#align(center)[

  #v(4mm)

  #text(
    font: "Nimbus Sans",
    size: 7.4pt,
    weight: "semibold",
    tracking: 1.15pt,
    fill: rgb("#565B60"),
  )[
    ORYNTH FINANCIAL SYSTEMS SERIES
  ]

  #v(5mm)

  #block(
    width: 165mm,
  )[
    #set text(
      font: "Libertinus Serif",
      size: 21pt,
      weight: "semibold",
    )

    #set par(
      justify: false,
      leading: 0.18em,
    )

    #align(center)[
      Obligation Finality, Custody-State Integrity, \
      and Consequential Financial Closure
    ]
  ]

  #v(2.5mm)

  #block(
    width: 150mm,
  )[
    #set text(
      font: "Libertinus Serif",
      size: 9.4pt,
      style: "italic",
      fill: rgb("#3F4449"),
    )

    #align(center)[
      Finality ≠ consequential closure.
    ]
  ]

  #v(4mm)

  #line(
    length: 34mm,
    stroke: 0.65pt + rgb("#5E6368"),
  )

  #v(4mm)

  #text(
    font: "Libertinus Serif",
    size: 10pt,
    weight: "semibold",
  )[
    Ashley S. Harris
  ]

  #v(1.5pt)

  #text(
    font: "Nimbus Sans",
    size: 8.2pt,
    style: "italic",
    fill: rgb("#50555A"),
  )[
    ORYNTH Systems
  ]
]

#v(5mm)

#heading(level: 2)[Abstract]

Financial systems frequently treat completion, finality, custody, and closure as interchangeable terminal concepts. F3 rejects that collapse.

This paper formalizes obligation finality, custody-state integrity, and consequential financial closure as distinct governed states and relations. Its controlling separation is:

#align(center)[
  #emph[Finality ≠ consequential closure.]
]

The architecture preserves settlement completion, execution completion, atomic completion, reconciliation, custody possession, custody authority, evidence, reversibility, finality, and closure validity as independently evaluable conditions. No one terminal appearance is permitted to stand in for another.

#v(2mm)

#line(
  length: 100%,
  stroke: 0.45pt + rgb("#777B80"),
)

#v(2mm)

#body-columns[

== 1. Problem

An economic obligation may present as complete while one or more governance conditions required for valid closure remain unresolved.

A system may possess assets, complete execution, reconcile records, or atomically complete a transaction without thereby establishing valid obligation finality.

F3 therefore separates observable completion states from governance-valid consequential closure.

== 2. Canonical Boundary

F3 governs obligation finality, custody-state integrity, consequential financial closure, finality evidence, custody authority, reversibility, and closure-state classification.

It does not permit execution success, settlement completion, atomicity, reconciliation, custody possession, or apparent closure to self-prove either finality or valid consequential closure.

== 3. Obligation Finality

Obligation finality is a governed state in which the applicable finality requirements for an obligation have been satisfied.

It is not reducible to successful execution or visible settlement completion.

*Settlement completion ≠ obligation finality.*

*Execution completion ≠ finality.*

*Atomic completion ≠ finality.*

== 4. Consequential Financial Closure

Consequential financial closure concerns whether a governed financial consequence is validly closed under the applicable authority, state, evidence, and finality conditions.

*Finality ≠ consequential closure.*

A state may be final within one domain while remaining open, defective, or unresolved under another applicable closure requirement.

== 5. Custody-State Integrity

Custody-state integrity preserves the distinction among possession, control capability, legal or governance authority, delegated authority, and the custody state actually represented by the system.

*Custody possession ≠ custody authority.*

Possession of an asset, credential, key, account, or technical control surface does not, by itself, establish authority to exercise consequential custody actions.

== 6. Reconciliation and Finality

Reconciliation may establish that records or represented states align under a defined comparison process.

It does not independently establish finality.

*Reconciliation ≠ finality.*

A reconciled obligation may still fail applicable authority, custody, closure, temporal, or other finality requirements.

== 7. Finality and Irreversibility

Finality is distinct from irreversibility.

*Finality ≠ irreversibility.*

A financial state may be final under a governed regime while remaining reopenable, reversible, revocable, supersedable, or otherwise mutable through separately authorized processes.

== 8. Evidence and Apparent Closure

A system report of completion or closure is evidence of system state or process behavior.

That evidence is not, by itself, sufficient to establish valid consequential closure.

*Apparent closure ≠ valid consequential closure.*

Closure validity must remain traceable to the applicable canonical authority, state, custody, and finality requirements.

]

#pagebreak()

#body-columns[

== 9. Core Non-Equivalence Results

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

The F3 canonical technical surface tests obligation-finality conditions, custody-state distinctions, closure-state evaluation, authority non-implication, execution/finality separation, and adversarial attempts to infer closure from incomplete evidence.

These results constitute bounded verification evidence for the implemented canonical F3 surface. They are not universal empirical guarantees.

#colbreak()

== 11. Cross-Family Interfaces

F3 inherits the F1 distinctions among settlement, reconciliation, history, repair, and continuity, together with the F2 distinction between distributed agreement and authority.

Later financial families may depend on F3 finality and custody-state semantics without collapsing those semantics into ledger representation, cryptographic possession, programmable execution, jurisdictional reach, or autonomous economic capability.

== 12. Limits and Non-Claims

This paper does not claim production deployment, regulatory approval, institutional adoption, external certification, customer validation, legal sufficiency, or universal prevention of financial closure failure.

Its claims are limited to the canonical F3 technical architecture, formal distinctions, runtime behavior, proof surfaces, and adversarial evidence bound in FIN-PUB-12.

== 13. Conclusion

Financial closure cannot be inferred merely because execution completed, records reconciled, custody exists, or a system reports a terminal state.

F3 formalizes obligation finality, custody-state integrity, and consequential financial closure as distinct governed conditions so that each remains independently inspectable and governed.

Within the defined F3 architecture, terminal-state appearance cannot substitute for valid authority, valid custody, or valid financial closure.

]