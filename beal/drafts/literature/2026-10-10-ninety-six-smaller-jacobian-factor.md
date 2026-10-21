# Smaller Jacobian factor — completed bounded source review

TARGET: Assess whether FNS Remark 7.13's smaller Jacobian factor can supply an unconditional exclusion of L032's retained 96a1 disk.
CHECKED: 2026-10-10
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Read FNS Remark 7.13 and its Section 7.2/7.7 interfaces; searched exact remark, 96a1/factor/unconditional and X(11)/Jacobian/twist terms; followed Lig77 to its publisher and an indexed academic copy. No usable twisted five-factor map or unconditional disk theorem was inspected.
SOURCE_EVIDENCE: FNS final author manuscript June 10, 2019, Remark 7.13 (PDF page 33, zero-based page 32), Section 7.2 and Lemma 7.7 statement/full proof; Lig77 publisher chapter DOI 10.1007/BFb0063948 gives bibliographic metadata only, while the indexed MPIM full-volume PDF returned HTTP 403.
COMPARISON: The five-dimensional isotypical factor is described abstractly by FNS, which explicitly leaves a smaller-field working description unavailable; its actual 96a1 disk exclusion still uses the degree-36 two-descent input. The CM Cartan quotient cases do not establish a map for the non-CM 96a1 twist.
GAP: No explicit twisted factor, rational-point map, arithmetic upper image or full-disk local comparison is supplied by the inspected sources; the underlying Lig77 proof was not accessible or audited. No unconditional exclusion follows.
REASON: Park this dependent lead after identifying the primary source's explicit missing-interface qualification; switch to an independent maximal-field-discriminant lower-bound test under separate coverage, preserving both historical stops.

Essential inputs: L032's disk -512+2048 Z2 with its full fourth-power
and positivity conditions; L050's identification of K96. L051 is route
evidence only. No L033/L045 arithmetic or cross-notebook input is proposed.
The primary source is FNS, Compositio Mathematica 156 (2020), 77–113,
[final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf).

Original pre-review test (preserved): retrieve the exact remark and essential theorem statements/proof cases
before comparison. Continue only if a concrete map or theorem offers a
bounded unconditional target; park if it requires the same uncertified
degree-36 class/unit input or does not address the retained disk. Do not
infer emptiness from smaller dimension, conditional rank or local
solvability. Other branches and residual signatures remain independent
gaps. This proposal claims no completed literature assessment or new
mathematics for the lead.

## What was actually inspected

The mathematical gap and intermediate test are those of the saved target:
a usable unconditional global obstruction on L032's retained 96a1 disk,
with independent signatures still unresolved. The potential downstream use
was an arithmetic computation on a smaller twisted factor that would avoid
the uncertified degree-36 class/unit input. The required threshold was a
concrete map and bounded unconditional test, not smaller dimension alone.

Primary source: N. Freitas, B. Naskręcki and M. Stoll, *The generalized
Fermat equation with exponents 2, 3, n*, Compositio Mathematica **156**
(2020), 77–113, [DOI](https://doi.org/10.1112/S0010437X19007693),
[final manuscript, Remark 7.13](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf#page=33),
dated June 10, 2019. The complete remark was read through the final
sentence, not just its search snippet. Locators are physical PDF pages
and the browser's zero-based page indices, avoiding manuscript pagination
ambiguity. Section 7.2's opening is physical page 25; Lemma 7.7 begins
on physical page 29 and its proof continues onto page 30.

Remark 7.13 reports an isogeny decomposition over Q(sqrt(-11)) with
multiplicities eleven, ten and five. The five-copy elliptic constituent
is X_ns^+(11), labelled 121b1. FNS says that the three isotypical factors
persist over Q after twisting. This does **not** identify the resulting
five-dimensional factor of the 96a1 twist with a product of five
Q-rational copies of 121b1, or give a curve-level rational quotient.
The remark supplies neither explicit twisted descent data nor a local
disk elimination. Its last sentence records the absence of a description
allowing work over a smaller field. These are qualifications in the
primary source, not a new impossibility theorem.

The Section 7.2 opening and Lemma 7.7's complete relevant proof retain
the existing degree-twelve field and its cubic two-torsion extension.
Their necessary global Selmer inclusion is compared with every local
class above a disk center, using Lemma 7.6 for constancy. Reuse the
completed certificate-scope assessment for those arithmetic obligations.
There is no replacement by the five-factor arithmetic in this argument.
The 96a1 conclusion removes exactly the disk retained by L032 only with
the source's conditional global input; it is not imported unconditionally.

For a possible duplicate shortcut, Section 7.1's non-split Cartan
quotient passage and its relevant proof cases were inspected (physical
pages 23–24): these concern the three CM labels and twists d=-1,-3.
Their elliptic covering collections over a cubic field and rational
x-coordinate condition are not a theorem for X_96a1(11). The presence
of the same untwisted constituent 121b1 does not supply the missing
twisted map. No new inference about 96a1 points is made here.

## Reference access and search limits

Gérard Ligozat, *Courbes modulaires de niveau 11*, in *Modular Functions
of One Variable V*, Lecture Notes in Mathematics **601** (1977),
149–237, [publisher chapter](https://doi.org/10.1007/BFb0063948).
The publisher page exposes metadata and a subscription preview, not
the load-bearing decomposition proof. An indexed academic full-volume
PDF at people.mpim-bonn.mpg.de/zagier/files-restricted/doi/10.1007/BFb0063941/fulltext.pdf
returned HTTP 403. A search lead points to Proposition 3.6.1, p.223;
this locator and its exact hypotheses remain **unverified**, not an
inspected theorem. No purchase, credentials or access circumvention
was attempted. The shell also lacked network DNS access to the FNS
host; the browser supplied the complete relevant FNS text instead.

Queries included `Freitas Naskrecki Stoll "Remark 7.13" Jacobian`,
`Ligozat "Courbes modulaires de niveau 11" pdf`,
`"X_E(11)" "5-dimensional" factor`,
`"X(11)" Jacobian "Ligozat" quotient five`,
`"96a1" "Jacobian" "factor"`, and `"96a1" "unconditional" "factor"`.
No adequate explicit map or unconditional exclusion was inspected.
Search silence is not a novelty claim. The original decomposition is
not reproved or installed as a mathematical premise in this turn.

## Decision and continuation

Outcome NEGATIVE: the primary remark's explicit missing-description
qualification and the absence of a usable interface change the route
decision from pursuing this lead to parking it. SOURCE_BLOCKED records
that dependent mathematics is not approved, including the unread
underlying proof; it does not assert the factor cannot ever be used.
Reopening needs accessible exact twisted map/descent data and a
discriminating full-disk test, not another search for the same remark.

Local duplicate/failure comparison used L032's complete retained row
and scalar conditions, L050's whole-fiber interface, the previous
certificate-scope assessment and ATTEMPTS/017–018. The local witness
stop and naive order-bound stop remain intact. No new lemma, map,
arithmetic script, rank estimate or GRH-free certificate is produced.
PROOF.md and DAG.md are unchanged because the mathematical argument
has not changed. Mathlib matching and supporting coverage: not checked.

Propose an independent test of whether local ramification can certify
a lower bound for the **maximal-field** discriminant of L051's degree-36
field sufficient to put its actual Minkowski cutoff above 10^6. This
is distinct from repeating L051's sufficient nonmaximal-order bound
and requires separate source coverage. It would guide certification
method selection only: even such a lower bound would not prove that
all class computations require enumerating up to that cutoff.
