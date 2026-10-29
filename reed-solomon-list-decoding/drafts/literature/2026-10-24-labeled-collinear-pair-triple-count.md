# Labeled determinant-zero pair triples — completed bounded source review

TARGET: Assess exact counting of ordered triples of pairwise disjoint unordered pairs in the order-1024 subgroup of F_65537 whose three (sum,product) points are collinear, retaining antipodal degeneracies.
CHECKED: 2026-10-24
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched exact sum/product collinear pair triples, finite-field subgroup involutions and incidence moments; searched local literature/ATTEMPTS/history for collinearity and nonface counts, then read the identified triple-rank/transfer failures. No completed matching count was found in the inspected material; no novelty conclusion follows.
SOURCE_EVIDENCE: Reused L020 and its Shangguan–Tamo criterion coverage; inspected Macourt–Shkredov–Shparlinski 1701.06192v2 Definition 1.1, Theorem 1.2 and Lemma 2.4 with proof; Murphy–Petridis 1601.03981v3 Lemma 1 with full Section 2 proof; Macourt–Petridis–Shkredov–Shparlinski 2003.03493v1 Section 3 and Theorem 5.2 with proof.
COMPARISON: The subgroup results concern Cartesian-product points with ratio/nonzero restrictions and unspecified constants, not the labeled sum/product image with six distinct endpoints. General finite-plane second moments apply to point sets but do not determine the desired disjoint-pair third count. L020 supplies the exact individual predicate only.
GAP: No inspected theorem supplies the aggregate exact count or justified endpoint-collision corrections. A complete finite enumeration reduction, including vertical lines, antipodal pairs, shared endpoints and ordering, remains to be proved in a later research turn.
REASON: Park direct import of the inspected incidence estimates. A bounded exact enumeration reduction is independently testable and does not repeat the failed global/core supersaturation transfer; its separate continuation assessment proposes proof obligations without deriving them.
SCOPE: Completed literature comparison for exactly TARGET, with three ordered pair objects, unordered endpoints and all six endpoints distinct. No count, correction formula, symmetry reduction or new lemma was derived; future reduction work is separately scoped below.
LITERATURE_REASON: This proposed labeled-incidence target has essential missing counting coverage; existing Boolean/cardinality assessments and the determinant dictionary do not approve a subgroup incidence calculation.

## Intended use and discriminating test

The main gap remains arbitrary-center 67/68 agreement safety. The
proposed intermediate input is a rigorously specified exact labeled
count, or a usable certified bound for that count, on the fixed subgroup.
Its plausible downstream use is to calibrate the density of the forbidden
nonsingular triples in L020 before attempting any quantitative transfer.
A total count on the full subgroup is not a bound on every support
family or core link. Avoid claiming otherwise.

Essential continuation inputs are L020, C001a and foundations/02 for
the fixed field/domain and tuple/selected-support convention. Reuse
`drafts/literature/2026-10-05-triple-support-rank-diagnostic.md` and
`drafts/literature/2026-10-06-core-conditioned-determinant-transfer.md`.
Before further proof reads, locate the exact recorded nonface-count
and link-transfer failures in the active notebook. L031's four-support
criterion is an identified nearby duplicate for realizability, not a
new result to reproduce and not a mathematical input to this count.
No cross-notebook input is proposed.

One separate literature step should determine whether primary finite-field
incidence or character-sum results provide an applicable exact count or
a concrete finite enumeration reduction. Read the exact field, subgroup,
distinctness and degeneracy hypotheses and the essential proof cases.
Continue only with a nonduplicated, bounded and checkable counting target;
if an existing local result already supplies the count, import it rather
than repeat it. If the available method only counts generic configurations,
counts overlapping pairs without justified corrections, or repeats a
recorded failed transfer, preserve that evidence and select a materially
different target. No mathematical formula or source approval is asserted
by this proposal.

Unresolved independently: uniformity after removing a 61-point core,
supersaturation for selected support families, a quantitative saving
large enough for the epsilon-field-size threshold, full relaxation
feasibility, RS realization, 67-agreement safety and the qualified ABF
source comparison. Antipodal examples remain allowed. The existing
955–957 bracket is unchanged. Full matching Mathlib coverage and
supporting incidence coverage are not checked.

## Completed review, 2026-10-24

The proposal above is retained as the question reviewed, not an assertion of
source approval at proposal time. This turn completed only source comparison.

### Primary statements and essential cases actually read

1. Simon Macourt, Ilya D. Shkredov and Igor E. Shparlinski,
   [Multiplicative Energy of Shifted Subgroups and Bounds On Exponential
   Sums with Trinomials in Finite Fields](https://arxiv.org/pdf/1701.06192v2),
   v2, 17 October 2017, printed pp. 3–4, Definition 1.1/Theorem 1.2;
   pp. 7–8, Lemma 2.4 and complete proof. Definition 1.1 counts ratio
   equalities for two coordinate sets in F_p^*, with nonzero denominators.
   For a subgroup G and nonzero lambda, Theorem 1.2 bounds
   T_lambda(G)-|G|^6/p by an absolute-constant multiple of
   p^(1/2)|G|^(7/2), |G|^5 p^(-1/2), or |G|^4 log|G| in the respective
   ranges |G|>=p^(2/3), p^(2/3)>|G|>=p^(1/2)log p, and smaller G.
   The printed final logarithm says H although only G is specified;
   no finite certificate relies on resolving that notation here.
   Lemma 2.4 converts to line-incidence products with an
   O(|A|^2|B|^2) correction for changed distinctness conditions.
   Its proof groups equal slopes and intercepts after exchanging
   denominators. This correction is not an exact degeneracy count.

   Comparison: the target points are L020's (sum,product) image of pairs,
   not the Cartesian product G x G. No collinearity-preserving dictionary
   between those two problems is established. Neither that coordinate
   change nor six-endpoint distinctness may be silently assumed. No
   estimate from this source is applied to the target.

2. Brendan Murphy and Giorgis Petridis,
   [A Point-Line Incidence Identity in Finite Fields, and Applications](https://arxiv.org/pdf/1601.03981v3),
   v3, 20 February 2016, printed p. 2, Lemma 1; p. 5, full Section 2 proof.
   For any E subset F_q^2, with i(l)=|E intersect l| and sums over all
   affine lines, sum_l i(l)^2=|E|^2+q|E| and
   sum_l(i(l)-|E|/q)^2<=q|E|. No subgroup, density or genericity
   hypothesis is required. The proof separates equal from distinct point
   pairs, using q+1 lines through a point and the unique line through two
   distinct points. It includes vertical lines and the full variance
   calculation. This known identity can be imported as a later enumeration
   consistency check once the pair-image set and multiplicities are
   justified; it does not encode disjoint endpoints or a third moment.
   Reproof of this identity is unnecessary.

3. Simon Macourt, Giorgis Petridis, Ilya D. Shkredov and Igor E. Shparlinski,
   [Bounds of Trilinear and Trinomial Exponential Sums](https://arxiv.org/pdf/2003.03493v1),
   v1, 7 March 2020, printed p. 4, Section 3 definition of tilde-T;
   pp. 8–10, Theorem 5.2 and full proof. For prime p and subgroups of
   orders G>=H, it bounds tilde-T(G,H)-G^3 H^3/p by absolute-constant
   multiples of p^(1/2)G^(3/2)H^2 for GH>=p^(4/3),
   G^(5/2)H^(5/2)p^(-1/2)+G^2 H^2 log G for p<GH<p^(4/3),
   and G^3 H log G for GH<=p. Tilde-T counts Cartesian-product triples
   satisfying a specified cross-product equality with its value nonzero.
   The proof handles small/large regimes by cited earlier bounds and the
   middle regime by rich-line coset counting, separately bounding zero
   line coefficients. Thus this stronger comparison still does not count
   the target point image, and its nonzero convention cannot be substituted
   for retention of all antipodal/vertical target cases. No bound imported.

### Duplicates, failures and scope decision

Narrow local search found collinearity material in the current proposal,
2026-10-05 triple-restriction extremal transfer, 2026-10-06 core-conditioned
transfer, 2026-10-07 fixed-block neighborhood and 2026-10-20 translated-pole
second-moment assessments. The latter already inspected the 2017 paper's
shifted-energy application, which is reused as background rather than a
new source discovery. The new reads concern the precise collinear-triple
predicate and the general incidence identity. No inspected local artifact
contains the requested aggregate count. L031's nearby criterion is not a
count and is not imported. ATTEMPTS/010 and L020 retain the genuine
antipodal realization. History/040 and the two transfer assessments retain
failure of whole-pattern exclusion and the missing labeled
supersaturation/cardinality transfer. None is reopened by this review.

Queries actually used: `finite field collinear triples multiplicative
subgroups sum product unordered pairs involutions`; `Macourt Shkredov
Shparlinski 1701.06192 collinear triples theorem`; `"collinear triples"
"sum" "product" finite field unordered pairs`; `"multiplicative subgroup"
"involutions" count`; `finite field incidence line occupancy third moment
collinear triples exact identity`. Shkredov 1508.03814 and other search hits
remain unread leads, not necessary inputs for the proposed elementary finite
enumeration reduction. No search failure certifies novelty or exhaustiveness.

Decision EXPLORE licenses only a later bounded attempt, not a known exact
answer. The [separate continuation assessment](2026-10-24-labeled-count-enumeration-reduction.md)
sets that attempt's proof obligations. It requires separate approval next
turn. A calculation must not discard overlaps or antipodal cases through a
ratio denominator. A reliable whole-H count could calibrate a density;
uniform core/link estimates and a threshold-saving transfer stay independent.
Mathlib coverage for a matching count, the imported incidence identity and
supporting finite-plane results has not been checked.
