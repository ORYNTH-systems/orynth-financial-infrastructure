# ORYNTH Financial Systems Series — House Design Specification v0.1

## Status

```text
DOCUMENT TYPE             : SERIES COMPOSITION SPECIFICATION
DERIVATION BASIS          : F1 + F2 visual consensus, informed by F3 R6
CONTENT AUTHORITY         : NONE
SEMANTIC AUTHORITY        : NONE
PURPOSE                   : PUBLICATION-COMPOSITION CONTROL
F1 MUTATION               : NONE
F2 MUTATION               : NONE
F3 MUTATION               : NONE
```

This specification governs the visual and typographic identity of the ORYNTH
Financial Systems Series. It does not alter the content, claims, mathematics,
formal status, publication status, or canonical standing of any paper.

## 1. Bound reference artifacts

| Paper | Reference artifact | Pages | SHA-256 |
|---|---|---:|---|
| F1 | `Partial_Settlement_Compensating_Execution_and_Economic_State_Continuity_F1_01U (1).pdf` | 11 | `27e6be94e785d6155fc30803ef7affc790a92e64a239c892f5407c3c1985c59a` |
| F2 | `Distributed_Settlement_Multiparty_Authority_and_Economic_State_Continuity_F2_R2 (1).pdf` | 6 | `ea5009e0023249774304414bcd9cf8dcecb32465e58dae393169e3bef6d39fb6` |
| F3 | `Obligation_Finality_Custody_State_Integrity_and_Consequential_Financial_Closure_F3_R6.pdf` | 2 | `0ad7147327a3a083c9d8d7f7d379409a785ee6e38b8bf1ee2d07aa1d4a23d1c0` |

## 2. Derivation rule

The house specification is not an average of all three papers.

F1 and F2 share the same page geometry, font system, title architecture,
heading hierarchy, body measure, page furniture, and full-width-to-two-column
transition. Those shared controls are normative.

F3 R6 uses an older short-paper composition lineage: US Letter, Nimbus Roman
body text, a smaller sans-serif title, a wider gutter, unruled sans-serif
section headings, and a columnized abstract. Those properties are variances,
not new house rules. F3 contributes one valid series rule: a short terminal
page may be balanced by moving whole sections across columns at a semantic
boundary.

## 3. Comparative determination

| Surface | F1 | F2 | F3 R6 | House determination |
|---|---|---|---|---|
| Page size | A4 | A4 | US Letter | **A4 required** |
| Page margins | 16 mm left/right/top; 17 mm bottom | Same | Approximately 17 mm left/right and 15–16 mm top/bottom | **F1/F2 values required** |
| Body face | Libertinus Serif, 9 pt | Same | Nimbus Roman, 9.7 pt | **Libertinus Serif, 9 pt** |
| Institutional face | Nimbus Sans | Same | Nimbus Sans | **Nimbus Sans** |
| Math face | New Computer Modern Math, 9.1 pt | Same | No dedicated math face | **New Computer Modern Math, 9.1 pt** |
| Title | Libertinus Serif semibold, 21 pt | Same | Nimbus Sans bold, 17 pt | **F1/F2 treatment required** |
| Subtitle | None | Descriptive, 9.4 pt roman | Proposition, 10 pt italic | **Optional 9.4 pt slot; style follows subtitle class** |
| Author | Libertinus Serif semibold, 10 pt | Same | Nimbus Sans bold, 9 pt | **F1/F2 treatment required** |
| Affiliation | Nimbus Sans italic, 8.2 pt | Same | Nimbus Sans roman, 8 pt | **F1/F2 treatment required** |
| Paper code in author block | Absent | Absent | `F3` present | **Omit; use metadata and running head** |
| Abstract | Full-width | Full-width | Two-column | **Full-width required** |
| Main body | Two columns | Two columns | Two columns | **Two columns required by default** |
| Column gutter | 5.5 mm | 5.5 mm | 0.31 in / 7.87 mm | **5.5 mm required** |
| Section headings | Serif semibold, ruled | Same | Sans bold, unruled | **F1/F2 hierarchy required** |
| Running header | Sans, gray, two-part, no rule | Same | Sans, black, ruled | **F1/F2 treatment required** |
| Page number | Explicit centered sans, 7.3 pt gray | Same | Default numbering treatment | **F1/F2 treatment required** |
| Terminal-page logic | Full-width evidence register | Full-width appendix register | Balanced short-paper columns | **Select by content class** |

## 4. Normative page geometry

| Control | Required value |
|---|---:|
| Paper | A4 — 210 × 297 mm |
| Left margin | 16 mm |
| Right margin | 16 mm |
| Top margin | 16 mm |
| Bottom margin | 17 mm |
| Usable text width | 178 mm |
| Standard column count | 2 |
| Column gutter | 5.5 mm |
| Nominal column width | 86.25 mm |
| Full-width surface | 178 mm maximum within page frame |

US Letter is not a series-conformant default. It may be used only when an
external venue requires it and the derivative is explicitly identified as a
venue-specific composition.

## 5. Typography hierarchy

### 5.1 Primary type system

| Role | Typeface | Size | Weight/style | Color |
|---|---|---:|---|---|
| Scholarly body | Libertinus Serif | 9 pt | Regular | Black |
| Main title | Libertinus Serif | 21 pt | Semibold | Black |
| Author | Libertinus Serif | 10 pt | Semibold | Black |
| Level-1 heading | Libertinus Serif | 13 pt | Semibold | Black |
| Level-2 heading | Libertinus Serif | 10.2 pt | Semibold | Black |
| Level-3 heading | Libertinus Serif | 9.1 pt | Semibold italic | Black |
| Mathematics | New Computer Modern Math | 9.1 pt | Book | Black |
| Series furniture | Nimbus Sans | 7.1–8.2 pt | Regular/semibold as specified | Controlled gray |

### 5.2 Body composition

```text
JUSTIFICATION             : FULL
LINEBREAKING              : OPTIMIZED
HYPHENATION               : DISABLED
BODY LEADING              : 0.56 em
PARAGRAPH SPACING         : 0.62 em
FIRST-LINE INDENT         : 0
```

Disabling automatic hyphenation is part of the archival extraction control.
Lexical compounds that still land at a line boundary may be kept intact with
a local nonbreaking composition wrapper; the lexical characters themselves
must remain ordinary, machine-readable characters.

## 6. Title architecture

The first-page title surface uses the following order:

1. Series banner.
2. Main title.
3. Optional subtitle.
4. Short horizontal rule.
5. Author.
6. Affiliation.
7. Abstract.

### 6.1 Series banner

```text
TEXT                      : ORYNTH FINANCIAL SYSTEMS SERIES
FONT                      : Nimbus Sans
SIZE                      : 7.4 pt
WEIGHT                    : Semibold
TRACKING                  : 1.15 pt
COLOR                     : #565B60
ALIGNMENT                 : Center
TOP OFFSET                : 4 mm
SPACE AFTER               : 5 mm
```

### 6.2 Main title

```text
FONT                      : Libertinus Serif
SIZE                      : 21 pt
WEIGHT                    : Semibold
MAXIMUM BLOCK WIDTH       : 165 mm
ALIGNMENT                 : Center
INTERNAL LEADING          : 0.18 em
LINE COUNT                : Prefer 1–2; permit 3 only when unavoidable
```

Do not reduce a normal series title to a smaller sans-serif display merely to
force a preferred line count. Title wrapping is controlled by the 165 mm title
measure and semantic break placement.

### 6.3 Optional subtitle

The subtitle occupies a maximum 150 mm centered block at 9.4 pt.

| Subtitle class | Treatment |
|---|---|
| Descriptive research subtitle | Libertinus Serif, roman, controlled gray `#3F4449` |
| Controlling proposition or equation-like statement | Libertinus Serif, italic; mathematical glyphs preserved exactly |
| No subtitle | Omit the surface and close the title-to-rule space accordingly |

Spacing with a subtitle:

```text
TITLE → SUBTITLE          : 2.5 mm
SUBTITLE → RULE           : 4 mm
```

Spacing without a subtitle:

```text
TITLE → RULE              : 4 mm
```

### 6.4 Title rule and author block

```text
RULE LENGTH               : 34 mm
RULE WEIGHT               : 0.65 pt
RULE COLOR                : #5E6368
RULE → AUTHOR             : 4 mm
AUTHOR                    : Libertinus Serif, 10 pt, semibold
AUTHOR → AFFILIATION      : 1.5 pt
AFFILIATION               : Nimbus Sans, 8.2 pt, italic, #50555A
AUTHOR BLOCK → ABSTRACT   : 5 mm
```

The paper identifier (`F1`, `F2`, `F3`, and successors) does not appear as a
separate line in the author block. It belongs in document metadata and the
running header.

## 7. Abstract architecture

The Abstract is a full-width surface on page 1. It is not placed inside the
two-column body.

After the final abstract paragraph:

```text
SPACE ABOVE SEPARATOR     : 2 mm
SEPARATOR                 : 0.45 pt, #777B80, full text width
SPACE BELOW SEPARATOR     : 2 mm
THEN                      : Begin two-column main body
```

Formal equations may appear in the abstract when central to the paper, but
they remain centered, unbroken display units. Lists in the abstract use the
same compact list controls as the body.

## 8. Main-body column architecture

The default main body uses two equal columns with a 5.5 mm gutter.

Full-width composition is admitted when the object materially requires it:

- wide equations or aligned formal constructions;
- formal-result registers whose internal relationships would be damaged by a
  column break;
- figures and tables that require the page width for legibility;
- evidence, appendix, or claim-control registers whose comparison structure is
  more important than column continuity.

Full width is not granted merely because an object is important.

## 9. Heading hierarchy

### 9.1 Level 1 — major stage or appendix family

```text
FONT                      : Libertinus Serif
SIZE                      : 13 pt
WEIGHT                    : Semibold
SPACE ABOVE               : 16 pt
SPACE BELOW               : 8 pt
STICKY                    : Yes
```

### 9.2 Level 2 — numbered section or named primary section

```text
FONT                      : Libertinus Serif
SIZE                      : 10.2 pt
WEIGHT                    : Semibold
TRACKING                  : 0.18 pt
SPACE ABOVE               : 12 pt
SPACE BELOW               : 5.5 pt
RULE OFFSET               : 2.5 pt below heading text
RULE WEIGHT               : 0.45 pt
RULE COLOR                : #73777C
STICKY                    : Yes
```

### 9.3 Level 3 — subsection or local formal division

```text
FONT                      : Libertinus Serif
SIZE                      : 9.1 pt
WEIGHT                    : Semibold
STYLE                     : Italic
SPACE ABOVE               : 8 pt
SPACE BELOW               : 3.5 pt
STICKY                    : Yes
```

No heading may be stranded at the foot of a column or page. A heading must
travel with enough following material to make its presence meaningful.

## 10. Lists, equations, figures, and tables

### 10.1 Lists

```text
LIST INDENT               : 1.05 em
BODY INDENT               : 0.48 em
ITEM SPACING              : 0.22 em
```

### 10.2 Display mathematics

```text
FONT                      : New Computer Modern Math
SIZE                      : 9.1 pt
SPACE ABOVE               : 6 pt
SPACE BELOW               : 6 pt
BREAKABLE                 : No
ALIGNMENT                 : Center unless formal structure requires otherwise
```

Definition → equation → explanation and result → proof → limitation units are
kept intact where practical. Visible mathematical correctness takes precedence
over cosmetic plain-text linearization.

### 10.3 Figures and tables

- Caption size: 8 pt.
- Figure/table titles align to the object width.
- Rules are restrained; tables do not use decorative boxes.
- Header rows use 8.2 pt semibold text.
- Full-width evidence pages may combine figures, tables, and explanatory text
  in a controlled vertical register.
- No figure, caption, or table row may be clipped, collided, or stranded.

## 11. Running furniture

### 11.1 Running header

The running header begins on page 2.

```text
LEFT                      : ORYNTH FINANCIAL SYSTEMS SERIES
RIGHT                     : [SHORT PAPER TITLE] · F[number]
FONT                      : Nimbus Sans
SIZE                      : 7.1 pt
TRACKING                  : 0.45 pt
COLOR                     : #4B4F54
ALIGNMENT                 : Left / right grid
UNDERLINE                 : None
```

Use a centered middle dot (`·`) before the family identifier. Do not alternate
between an em dash and a middle dot across papers.

### 11.2 Page number

```text
POSITION                  : Centered footer
FONT                      : Nimbus Sans
SIZE                      : 7.3 pt
COLOR                     : #55595E
FORMAT                    : Arabic numeral
FIRST PAGE                : Included
```

## 12. Whitespace and page rhythm

Whitespace is structural, not decorative.

- Preserve the stable page frame and column measure before changing type size.
- Keep formal units intact rather than compressing their internal relationships.
- Do not create empty space to emphasize importance.
- Do not pad a short paper merely to imitate the page count of a longer paper.
- A terminal page may retain lower-page whitespace when the content is
  genuinely exhausted, but the occupied region must read as deliberately
  composed rather than accidentally abandoned.
- Simultaneous large lower-page voids in both columns are a composition failure
  when whole-unit redistribution can correct them without mutation.

## 13. Second-page and terminal-page balancing

The correct balancing strategy depends on the content class.

### 13.1 Short narrative paper

For a two-page or similarly short paper:

1. Continue the two-column body on page 2.
2. Keep enumerated results and other formal registers intact.
3. Move only whole sections or whole formal units across columns.
4. Place a controlled column break at a semantic boundary.
5. Prefer approximately comparable occupied depth in the two columns.
6. Do not stretch leading, enlarge type, or add content to fill the page.

F3 R6 demonstrates this valid rule by moving the §12–§13 terminal unit to the
right column. Its balancing logic is retained even though its current page and
type system are nonconformant.

### 13.2 Evidence or formal-register terminal page

When the terminal page contains figures, tables, evidence matrices, or
appendix registers, use a full-width structured surface or a deliberate grid.

- F1 page 11 is the reference for a full-width evidence/figure/table close.
- F2 page 6 is the reference for an appendix-register close with a full-width
  primary appendix and a controlled two-part lower register.

Do not force evidence objects into narrative columns merely to imitate the
short-paper balancing pattern.

## 14. Allowed variants

| Variant | Allowed treatment |
|---|---|
| No subtitle | Close title directly to the short rule |
| Descriptive subtitle | 9.4 pt roman centered block |
| Proposition subtitle | 9.4 pt italic centered statement |
| Formal-heavy paper | Two-column formal stage with selective full-width objects |
| Evidence-heavy terminal stage | Full-width figures/tables/registers |
| Short two-page paper | Balanced terminal columns using whole-unit breaks |
| Venue-mandated paper size | Separate venue-specific derivative; do not redefine house master |

## 15. Prohibited variation

- US Letter as the unmarked series master.
- Sans-serif main title when the house serif title is available.
- Body typography larger or looser merely to increase page count.
- Abstract placed in columns without an explicit controlled exception.
- Unruled sans-serif primary section headings as an undocumented variant.
- Paper identifier duplicated in the author block.
- Running-header separator drift (`—`, `-`, and `·` used inconsistently).
- Automatic discretionary hyphenation that damages extraction.
- Artificial vertical padding used to conceal weak page balance.
- Splitting formal results, equations, proof units, captions, or table rows when
  whole-unit movement is available.

## 16. F3 R6 conformance disposition

F3 R6 is a valid editorial-content candidate and a useful short-paper balance
reference. It is not yet a full house-format visual master.

| F3 R6 surface | Required house correction in a future derivative |
|---|---|
| US Letter page | Convert to A4 |
| 17 pt Nimbus Sans title | Convert to 21 pt Libertinus Serif semibold |
| Nimbus Roman 9.7 pt body | Convert to Libertinus Serif 9 pt |
| 7.87 mm gutter | Convert to 5.5 mm |
| Columnized abstract | Convert to full-width abstract |
| Sans 9 pt unruled headings | Apply serif ruled hierarchy |
| `F3` in author block | Remove from author block; retain in metadata/header |
| Ruled running header | Use unruled F1/F2 header |
| Default page numbering | Apply explicit 7.3 pt Nimbus Sans gray footer |
| Balanced page-2 unit break | Preserve |

Any such operation must create a new controlled F3 derivative. It must not
overwrite R6 or silently imply that R6 itself already satisfies the house
specification.

## 17. Conformance checklist

```text
PAGE SIZE                 : A4
MARGINS                   : 16 / 16 / 16 / 17 mm
SERIES BANNER             : PRESENT AND EXACT
TITLE                     : 21 pt LIBERTINUS SERIF SEMIBOLD
OPTIONAL SUBTITLE         : CONTROLLED 9.4 pt SLOT
TITLE RULE                : 34 mm / 0.65 pt
AUTHOR                    : 10 pt SERIF SEMIBOLD
AFFILIATION               : 8.2 pt NIMBUS SANS ITALIC
PAPER CODE IN AUTHOR BLOCK: ABSENT
ABSTRACT                  : FULL WIDTH
BODY                      : 9 pt LIBERTINUS SERIF
COLUMNS                   : 2 × 86.25 mm
GUTTER                    : 5.5 mm
LEVEL-2 HEADINGS          : 10.2 pt SERIF + RULE
MATH                      : NEW COMPUTER MODERN MATH 9.1 pt
RUNNING HEADER            : PAGE 2+, UNRULED, TWO-PART
PAGE NUMBER               : CENTERED 7.3 pt SANS
TERMINAL BALANCE          : CONTENT-CLASS APPROPRIATE
HYPHENATION               : DISABLED / EXTRACTION SAFE
CLIPPING OR COLLISION     : NONE
REPLACEMENT GLYPHS        : NONE
```

## 18. Governing summary

The shared series identity is:

```text
A4 disciplined page frame
        +
restrained sans-serif institutional furniture
        +
serif scholarly title and body
        +
full-width title/abstract opening
        +
ruled two-column analytical body
        +
content-class-aware full-width exceptions
        +
balanced, non-padded terminal composition
```

F1 supplies the complete long-form argument/formal/evidence rhythm. F2 proves
that the same system scales to a dense six-page formal paper. F3 supplies the
short-paper balancing rule. Together they define a coherent series only when
those roles remain distinct.
