# Weighted point-plane incidence — completed source comparison

TARGET: Compare primary finite-field point-plane incidence bounds with the 959-point, 18769-indexed-plane full-sheet configuration, retaining repeated planes and extra incidences.
CHECKED: 2026-10-29
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the saved narrow duplicate search; searched Rudnev weighted point-plane incidence, Vinh hyperplane incidence, Kollár dimension-three incidence and arbitrary-field VC-dimension improvements. Exact queries, primary versions, inspected theorem/proof ranges and unread leads are recorded below; no novelty conclusion.
SOURCE_EVIDENCE: Rudnev arXiv:1407.0426v5 Theorem 3/duality, Theorem 14 and its complete weight-rearrangement proof, pp.4,20; Rudnev arXiv:1806.03534v1 Theorems 1/1A/1C and the weighting argument, pp.2,4–5; Vinh arXiv:0711.4427v1 Theorem 5 and its proof qualification, Section 2/Lemma 1, pp.3–4; Kollár arXiv:1405.2243v3 Theorems 2/4, pp.1–2, and finite-characteristic proof cases in Section 4, pp.12–14.
COMPARISON: The inspected results do not certify an upper bound below seven incidences per plane index. Rudnev's unweighted scale already exceeds this threshold in the optimistic distinct-plane case; its cited weighted statement also requires equal total weights, absent here. Vinh's field-size error is too large; Kollár bounds distinct lines, not these repeated section planes. Details and qualifications follow.
GAP: No inspected direct import excludes a nonconstant span-three sheet. Plane multiplicities remain uncontrolled, but merely removing repetitions would not repair the incidence scale. The newer VC-dimension lead lacks inspected essential proof cases and is not coverage. Universal collapse, retention, compatible laws and RS transfer remain open.
REASON: New primary comparisons supply an informative negative decision: park direct use of these general incidence bounds rather than undertake a dependent calculation or assume injectivity. Consider a separately gated large-message-fiber propagation test; this review establishes no such result.
SCOPE: Completed source comparison only for the pinned full sheet over E or F, arbitrary C,sigma, repeated quadratics and extra incidences. EXPLORE records lack of an adequate match, not approval of an incidence reproof, multiplicity bound or any new mathematical target.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED identified missing essential incidence theorem coverage for a new mechanism; the L138 module assessment does not cover these theorems.

## Proposed comparison and bounded decision

The main gap remains arbitrary-center 67/68 safety. The intermediate
target is source coverage for a weighted incidence obstruction to a
nonconstant span-three full-sheet assignment. The existing cone
assessment describes the candidate points
[1:x_(t,y):x_(t,y)^2:d_(t,y)] in projective three-space and the indexed
planes with equation a_0(P)Z_0+a_1(P)Z_1+a_2(P)Z_2-Z_3=0.
Each indexed plane has seven prescribed incidences. This is the saved
object to compare with sources, not a newly proved incidence theorem
or an assumption that distinct indices give distinct planes.

Essential inputs are L030's arbitrary labeling, L138's full-sheet
equations and the cone assessment's Exact object to compare section.
ATTEMPTS/109–113 preserve the rank/fiber/translation stops; these stops
do not themselves preclude a different incidence mechanism. No
cross-notebook theorem is used. Full-sheet exclusion, even if obtained,
would still leave partial retention, compatible laws and RS transfer
unresolved, so this comparison cannot improve the 955–957 bracket.

The source comparison must distinguish indexed from distinct planes
and keep all multiplicities, repeated messages and extra incidences.
Read primary theorem hypotheses and essential proof cases first;
do not import an unweighted theorem by assuming injectivity or
unproved multiplicity control. Track the theorem's incidence threshold
against the prescribed seven incidences per index, allowing all extra
incidences. Also retain field-size and characteristic restrictions,
exceptional point/line/plane concentrations, and the difference between
affine and projective formulations. The ambient field changes from E
to its degree-28 extension; neither contains the auxiliary F_137.

Continue only if an inspected theorem supplies an applicable obstruction
or a concrete independently testable missing hypothesis with plausible
downstream use. Otherwise record its exact mismatch and park this
incidence-import route. No mathematical calculation or new lemma is
approved by this file. New targets need a separate assessment and
approval. Literature novelty and Mathlib coverage remain unchecked.

## Primary statements and essential cases actually inspected

**Rudnev, original paper.** [arXiv:1407.0426v5](https://arxiv.org/pdf/1407.0426v5),
4 December 2015, Theorem 3, printed p.4: for m points and n planes,
m>=n, characteristic p!=2 and n=O(p^2), the bound is
O(m sqrt(n)+km), where k counts planes in a pencil; the following
duality paragraph reverses the roles. Theorem 14, p.20, concerns positive
weighted point/plane sets with **equal** total weight W, maximum weight
w0>1, unweighted collinearity k and W/w0=O(p^2):
Iw=O(W sqrt(w0 W)+k w0 W). Its entire proof was read: replace by
richest subsets and maximum weights, then apply Theorem 3. The
discounted-line variant counts a reduced incidence quantity. No balanced
weight construction for this notebook is imported.

**Rudnev, later formulation.** [arXiv:1806.03534v1](https://arxiv.org/pdf/1806.03534v1),
9 June 2018, Theorem 1, p.2: |Q|<=|Pi|, |Q|<p^2 in positive
characteristic, k maximum collinear points, gives
I<<|Pi|(sqrt(|Q|)+k). Theorem 1A, p.4, discounts incidences supported
on specified lines. Theorem 1C, pp.4–5, has equal total weights W,
w0>=1, W/w0<p^2 and Iw<<W(sqrt(w0 W)+kw0). The preceding
rearrangement argument and the following dyadic-weight qualification
were inspected. These are asymptotic constants, not a certified sharp
seven-incidence threshold.

**Vinh.** [arXiv:0711.4427v1](https://arxiv.org/pdf/0711.4427v1),
28 November 2007 identifier/version (the PDF also prints an October 2018
date), *Szemerédi–Trotter type theorem and sum-product estimate in finite
fields*, Theorem 5, p.4: for affine points/hyperplanes in F_Q^d, d>2,
I<=|P||H|/Q+(1+o(1))Q^((d-1)/2)sqrt(|P||H|).
The displayed product has a P/L typographical inconsistency, retained
here as the intended point/hyperplane cardinalities. Section 2's
projective embedding, adjacency identity and Lemma 1 mixing argument,
pp.3–4, were read. The higher-dimensional proof is explicitly left to
the reader; no weighted or explicit finite-Q strengthening is imported.

**Kollár.** [arXiv:1405.2243v3](https://arxiv.org/pdf/1405.2243v3),
3 December 2014, *Szemerédi–Trotter-type theorems in dimension 3*,
Theorem 4, p.2, assumes m distinct lines and n distinct points in K^3,
no plane containing more than c sqrt(m) lines. Its bound is
2.45mn^(2/5)+2.45n^(6/5)+0.91c^2 mn^(1/3)+6.74n.
Theorem 2 is stated over C. Section 4, pp.12–14, was inspected through
the finite-characteristic nonruled cases (36),(37) and final estimate
(38), rather than substituting the complex exponent. Neither theorem
is a point-plane theorem. No conversion of our object to its distinct
lines with a verified concentration bound is available.

## Applicability and required threshold

These comparisons specialize source statements only; they prove no new
lemma about the saved working reduction. Write M=18769 for the number
of plane **indices**, n=959 for the distinct design points, and m<=M for
the number of distinct planes. The saved seven incidences per index
give the comparison threshold 7M=131383; extra incidences can only
increase the actual incidence count. The task would require an upper
bound strictly below that threshold for a nonconstant sheet.

Both K=E and K=F have characteristic p=65537; Q=|K| is respectively
65537 or 65537^28. The auxiliary 137 is neither p nor Q. The points
already lie in the affine Z0=1 chart, and the section equations there
define affine planes over K, so this chart change needs no embedding
of F_137. The characteristic and small-set conditions of Rudnev are
not the missing premise at these cardinalities.

In the optimistic unweighted situation m=M, Theorem 1's displayed
scale per plane is sqrt(959)+k, with sqrt(959)>30, against seven
prescribed incidences. Even setting aside concentration, no explicit
constant giving the required strict bound is supplied. Repetitions
cannot be silently erased: the actual weights are 1 on points and
the numbers of indices on distinct planes, with total weights 959
and 18769. They do not meet Theorem 1C's equal-mass hypothesis. No
padding, rescaling, asymmetric weighted theorem or reproof is made.
An independently proved multiplicity bound alone would still leave
the unfavorable unweighted threshold comparison.

For Vinh's d=3 statement, even the optimistic distinct-plane error
scale is Q sqrt(959M), already larger than 7M for Q>=65537; the
extension makes it worse. Its o(1) is not converted into an effective
finite-field estimate. The cited theorem also supplies no weighted
statement for repeated indices. Kollár's theorem fails the object
type before numerical substitution; duality alone changes points to
planes, not to a collection of distinct lines. No unproved line,
plane or quadric concentration hypothesis has been inserted. Span
three by itself supplies none of the missing source hypotheses.

Thus the inspected direct imports are parked, including attempts to
rescue them just by declaring all planes distinct. This is not a
counterexample to collapse, nor a statement excluding every specialized
incidence theorem. L030, L138 and the saved exact-object qualification
remain unchanged; PROOF.md and DAG.md need no mathematical update.

## Search record, duplicates and unread leads

Queries included `Rudnev point plane incidences weighted theorem weighted
points planes maximum weight finite fields`, `Vinh point hyperplane
incidences finite fields theorem weighted`, `Kollar incidences points
planes three dimensions arbitrary fields theorem`, and the exact title
`Improved incidence bounds over arbitrary finite fields via the
VC-dimension theory`. The supplied duplicate search is reused; narrow
additional reads checked ATTEMPTS/109,110,113 and the span-three working
record. The latter concerns auxiliary-line image rank, not a repeated
message's set of indices. Stops 109–113 remain in force for their
mechanisms. No sibling notebook was searched or used.

Iosevich–Pham–Senger–Tait, [European J. Combin. 118 (2024), 103928](https://doi.org/10.1016/j.ejc.2024.103928),
Theorems 1.2/1.5/1.7, surfaced in publisher-indexed text. Direct primary
page/accepted-manuscript requests returned 403. Essential proofs were
not inspected, so these are **unread leads**, not imported theorems or
coverage for a calculation. The retrieved arXiv:2303.00330v1 is titled
*An improved point-line incidence bound...*, and cannot silently stand
in for this later point-plane paper. No claim of exhaustive literature
coverage or novelty follows. Mathlib coverage was not checked; there
is no formalization claim.

## Decision and separate continuation

The continuation/abandonment test for this review is met negatively:
the inspected bounds yield no certified obstruction at seven incidences
per index, even with optimistic distinctness, and weighting adds an
unmet premise. Do not spend a mathematical turn computing these bounds
again. Reopen only for a genuinely sharper applicable theorem or an
additional incidence supply, not a renamed concentration audit.

A separately gated possibility is to control a **large repeated-message
fiber directly**, using polynomial-root agreement and the auxiliary
lines, rather than an incidence upper bound or a translation action.
Its proposed numerical cutoff and exact source comparison are recorded
in `2026-10-29-large-message-fiber-propagation.md` as REVIEW_REQUIRED.
No cutoff, propagation result, or ready mathematical continuation is
asserted here. Even success would leave small fibers and the independent
retention/global-transfer gaps unresolved.
