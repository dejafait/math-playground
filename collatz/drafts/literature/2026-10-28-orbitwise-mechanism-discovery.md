# Orbitwise descent mechanisms — completed source comparison

TARGET: Source-assess up to three non-sorting mechanisms for actual descent at the first coefficient drop, and nominate one bounded pointwise test or record why none qualifies.
CHECKED: 2026-10-28
DECISION: EXPLORE
SEARCH_EVIDENCE: Step538 compared harmonic-mean control, nonleast-representative separation, and two-peak integer elimination; exact queries, primary passages, local duplicates and qualifications appear below. One symbolic two-peak subcase is nominated, without executing it or claiming novelty.
SOURCE_EVIDENCE: Rozier–Terracol arXiv:2502.00948v5 (2026-05-17), Definition1.2/C1–C3, Theorem4.2/full product proof, Corollaries4.3–4.4/proofs, Remark5.5 and AppendixA/full acyclic proof plus its separate circuit premise; Lagarias1985 printed pp.7–9 definitions/TheoremC and both proof cases, p.11 TheoremE/full proof sketch; Simons–deWeger2005 section1.2, Theorem3(b) and section3.3 cyclic chaining comparison. Reuse the saved finite Rozier2019 assessment.
COMPARISON: Harmonic-mean bounds need an additional orbitwise inequality; TheoremE leaves the least representative unresolved; one-peak exclusion and closed-cycle bounds do not cover an open two-peak first-drop excursion. Remark5.5 explicitly motivates fixed-maximum shapes. Nominate a symbolic b=1 two-peak test with unbounded other run lengths, rather than another census or swap comparison.
GAP: The proposed two-junction elimination is unproved. Success would settle only its restricted coefficient-to-actual transfer, leaving other peak shapes and finite coefficient-drop existence independent and open.
REASON: A source-suggested structural family supplies a materially different, independently testable continuation after L109; this literature step proves no new result. The separate new assessment requires next-turn approval before mathematics.
SCOPE: Completed literature-only comparison of exactly three mechanisms; no lemma, mathematical script, calculation or canonical argument change.
LITERATURE_REASON: The first-drop pointwise mechanism lay outside the completed finite swap audit; primary comparison for a non-sorting continuation was essential and previously missing.

## Gap, target and decision

The main gap is eventual strict descent for every positive integer n>1.
The intermediate target here assumes a finite first coefficient drop and
asks whether actual descent occurs then. This is the finite-time part of
the CST conjecture, not an established bridge. Its downstream use would
be to discharge one of the two obligations separated in PROGRESS.md.
Existence of a finite coefficient drop is not assumed universally.

The [MathPrize statement](https://mathprize.net/posts/collatz-conjecture/)
was rechecked on 2026-10-28: the page dated July7,2021 specifies n/2
for even n and 3n+1 for odd n, universally reaching1. The shortcut
conventions in foundations/01-target-and-scope.md still apply. Prize
adjudication is separate.

## Three mechanisms

1. **Harmonic-mean control.** Rozier–Terracol v5, Theorem4.2 and
   Corollaries4.3–4.4 constrain paradoxical segments through the harmonic
   mean of their odd states. The proof multiplies the exact one-step
   ratios and applies arithmetic/geometric means; its upper estimate
   applies without paradoxicality. This supplies a necessary condition,
   not an orbitwise exclusion. No new lower bound on that harmonic mean
   relative to the coefficient gap was located. Reusing only the minimum
   or extending finite height tables would not be a new bridge. Park.

2. **Nonleast-representative separation.** Lagarias, *The 3x+1 Problem
   and Its Generalizations*, American Mathematical Monthly92(1985),3–23,
   TheoremE, printed p.11, leaves at most the smallest representative
   exceptional in each admissible class once its length is sufficiently
   large. Read p.8's strict proper-prefix definition, p.9's threshold and
   both nonadmissible cases, and the entire p.11 proof sketch: logarithmic
   separation, remainder bound, then comparison with the next class member.
   The constant is effectively computable, not numerically specified
   there. This is useful known localization but does not settle the least
   representative which already occurs in L109. No new effective constant,
   census, or claim that it covers every positive integer is proposed. Park
   as a direct solution route; retain it as a precise scope comparison.

3. **Two-peak integer elimination.** Rozier–Terracol v5, Remark5.5
   proposes fixed numbers of local maxima; AppendixA LemmaA.1 treats one
   peak, with its acyclic proof using an integer endpoint difference and
   the initial odd-run congruence. The equality case cites circuit
   exclusion separately. Two peaks are not established by that proof.
   Simons–deWeger, *Theoretical and computational bounds for m-cycles of
   the 3n+1-problem*, Acta Arithmetica117(2005),51–70, section1.2 and
   Theorem3(b), impose periodic closure. Section3.3 explicitly chains
   estimates cyclically. An open endpoint at or above its start cannot be
   substituted for closure. Nominate only the b=1 open two-peak subcase
   specified in the separate assessment; retain equality as well as strict
   endpoint growth in that future test.

Precise primary locations:
[Rozier–Terracol v5](https://arxiv.org/html/2502.00948v5#S4),
[Remark5.5](https://arxiv.org/html/2502.00948v5#S5),
[AppendixA](https://arxiv.org/html/2502.00948v5#A1),
[Lagarias1985 scan, printed pp.7–11](https://web.williams.edu/Mathematics/sjmiller/public_html/372Fa15/addcomments/Lagarias_3x%2B1AndItsGeneralizations.pdf),
[Simons–deWeger2005, printed pp.52,55,58](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
The Lagarias scan begins at printed p.3: PDF pages5–7 and9 were rendered
and read because its text layer and the web screenshots were empty.
The source is a published primary article, not the search snippet or
bibliography summary. No Baker/Feldman constant is extracted or reproved.
The cycle paper's numerical exclusion proof was not audited or imported;
its closure hypothesis and cyclic chaining were inspected for comparison.

## Exact nomination and bounded decision test

The nominated target is to attempt first-drop descent for actual parity
words 1^a 0 1^c 0^d, integers a,c,d>=1, with no bound on their sizes.
It uses two chronological odd-run junctions and their exact integrality,
not an order on words or a count of survivors. The first intervening even
run has length1. The final even run may be incomplete; the endpoint need
not be odd. Every proper-prefix coefficient guard is retained.

Make one symbolic elimination attempt on this family. Continue only on a
proof of uniform strict descent, a useful proved parameter subcase with
its remaining boundary explicit, or new evidence identifying an exact
failure of the proposed elimination. An unresolved sign is EXPLORATION,
not a negative theorem; preserve it and do not expand a finite search or
silently enlarge the family. Full details and the same target text are in
`2026-10-28-two-peak-unit-gap-test.md`. This is a nomination for separate
approval next turn, not execution or proof in this turn.

## Duplicates and stopped routes

Read L109 and Attempt036 in full; reuse steps534/536's completed source
comparisons. Read L002, L005 and Attempts002/003: their growing complete
blocks do not guarantee coefficient contraction. The new test explicitly
conditions on first contraction, rather than asserting descent within a
fixed number of blocks. It does not reopen fixed-window/block descent,
periodic growing-word escape, CRT zero-run forcing, finite sieving,
rationality or lattice-count upgrades. The nominated family does not
reuse the false adjacent-swap margin inequality.

Scoped searches in ATTEMPTS, foundations, the local assessments and the
October28 histories found no completed two-peak first-drop theorem. This
is not evidence of originality. The cyclic d35 results and L005's growing
alphabet have different hypotheses; they are not premises of the new
claim. No cross-notebook input is proposed. Full matching Mathlib coverage
for the nominated family is not checked; unknown is not absent.

## Search and access record

Queries included:
- `Collatz "coefficient stopping time" "paradoxical" descent`
- `Collatz paradoxical sequences Diophantine approximation first stopping time remainder`
- `Collatz "coefficient stopping time" "two"`
- `Collatz "paradoxical" "maxima"`
- `Collatz "two local maxima" stopping`
- `"coefficient stopping time" "Garner" theorem`
- `Collatz two cycles Simons 2005 2 cycles proof pdf`
- `"Collatz" "acyclic" "two"`
- `"coefficient stopping time" "runs"`
- `"coefficient stopping time" "two local maxima"`
- `"Collatz" "two" "acyclic paradoxical"`
- `Collatz "1^a" "1^c" stopping`

Only the named primary passages support this comparison. Publisher/index
abstracts and unrelated proof claims were leads, not theorem evidence.
The AMS Garner1981 PDF and Simons2007 publisher fetch returned403; neither
is essential to the selected test or imported. Their access failures do
not justify further unchanged retrieval. The existing finite coding
assessment remains adequate. The exact version used for the new structural
lead is v5, 2026-05-17, rather than silently changing the v2 audit inputs.
