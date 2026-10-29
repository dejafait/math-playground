# Two-overlap disjoint-pair extraction — source comparison

TARGET: Assess source coverage for forcing a disjoint pair in a linear family of 12–14 two-overlap supports on the fixed seven-set with maximum label degree four.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reviewed ATTEMPTS/016,017,027 and relevant L023/L025/L072 proofs, L086/L109, the October 20 uniform-pair assessment and October 4 matching assessment; searched intersecting linear four-uniform, bounded-degree and two-plus-two partition terminology; primary statements and relevant proof cases inspected below.
SOURCE_EVIDENCE: Füredi (1981), Corollary 3 p. 158, definitions pp. 155–156, section 2 p. 157 and intersecting proof cases in section 5 pp. 159–161; Francetic et al. arXiv:1508.00951v3 pp. 1–3; Alfaro et al. arXiv:1903.08984v2 section 4 pp. 9–10 and definition p. 2.
COMPARISON: The general degree theorem leaves a non-plane family of at most twelve edges and the exceptional order-three plane; neither it nor the other inspected statements directly settles the exact two-plus-two partition at twelve edges. Recorded local failures do not refute this implication.
GAP: Establish or refute the partition-sensitive implication, retaining all 12–14 edge counts, isolated labels and maximum degree four; do not assume regularity, four-partiteness, a projective-plane embedding or a specific extracted numeric pair.
REASON: Known bounds cover part of the target, while the exact balanced-partition difference remains; a bounded specialization attempt is justified without claiming novelty or deriving it in this literature-only turn.
SCOPE: Pure finite incidence on the fixed sixteen labels; no moment feasibility, chart transport, uniform pair exclusion or universal representation is approved by this assessment.
COVERED_TARGET: Prove or refute the disjoint-pair implication for 12–14 distinct linear two-plus-two supports on the fixed seven-set with maximum label degree four.
LITERATURE_REASON: The newly proposed extraction implication was outside the ready labeled-pair filter assessment and explicitly REVIEW_REQUIRED at invocation start.

## Exact target, relevance and test

Let H be the sixteen-label domain and S={1,8,12,18,22,27,33}.
Consider 12–14 distinct four-subsets E of H, each having exactly two
labels in S and two in H minus S. Every pair meets in at most one
label and each label has degree at most four. Does E contain two
disjoint members? This review proves neither answer.

The main unresolved equality exclusion needs at most fifteen actual
original events rather than sixteen. L086/L109 provide necessary
incidence conditions in the represented t=0 class; L151 is an audited
conditional fixed-pair exclusion, not an extraction theorem. A positive
answer here would supply an arbitrary disjoint pair for a future uniform
exclusion. It would not supply L151's numeric pair, uniform coverage,
universal representation or identification with the challenge.

Continue with one bounded proof/counterexample attempt using the
partition and the imported general bound. Require all admissible sizes,
not only fourteen. A complete proof or an explicit fully verified
incidence counterexample is informative; a counterexample parks only
this implication. Failure to close the exceptional or boundary case
must remain an unresolved case, not a theorem. The proposed ready
continuation requires the supervisor's separate next-turn approval.

## Primary source comparison

**Z. Füredi**, *Maximum degree and fractional matchings in uniform
hypergraphs*, Combinatorica 1(2) (1981), 155–162,
[author-hosted published scan](https://www.renyi.hu/~furedi/PUBS3/furedi_007_cca1981_fractional_matchings.pdf),
[DOI](https://doi.org/10.1007/BF02579271).
Corollary 3, p. 158: an intersecting r-uniform hypergraph is either a
projective plane of order r−1 or has maximum degree at least |E|/(r−1).
The former has r²−r+1 edges and degree r (p. 157).
Read definitions, equation (1), the section 2 theorem and Corollary 1,
and section 5's low-degree and regular cases, including the ν=1
projective-plane exception; checked the printed corollary on PDF page 4.
At r=4, degree at most four allows at most twelve edges outside the
thirteen-edge plane. This leaves the twelve-edge boundary and the plane's
compatibility with the specified partition unresolved here. No regularity
or absence of a plane may be added silently. Cite this corollary rather
than reprove its general bound; only the partition difference needs work.

**N. Francetic, S. Herke, B. D. McKay, I. M. Wanless**,
*On Ryser’s Conjecture for Linear Intersecting Multipartite Hypergraphs*,
[arXiv:1508.00951v3](https://arxiv.org/pdf/1508.00951v3), 29 September 2015;
European J. Combin. 61 (2017), 91–105.
Read pp. 1–3: their r-partite convention is exactly one vertex per side;
section 2 studies the additional hypothesis tau=r. The two-plus-two
partition here is not that hypothesis. Lemma 2.2's line-count paragraph
supports a general degree bound, but the stronger cover conclusions
cannot be imported without the missing assumptions. No such refinement
of the partition is supplied or assumed.

**C. A. Alfaro, G. Araujo-Pardo, C. Rubio-Montiel, A. Vazquez-Avila**,
*On transversal and 2-packing numbers in uniform linear systems*,
[arXiv:1903.08984v2](https://arxiv.org/pdf/1903.08984v2), 28 March 2019,
section 4 pp. 9–10, Theorem 4.1 and Corollary 4.2.
Their classification requires tau=nu_2=4 (L_4). Read the family definition,
classification statements and their construction discussion. Definition
p. 2 makes nu_2 a maximum family with no three concurrent lines, not an
ordinary matching number; the abstract has misleading wording on this
point. Those additional equalities are unproved here, so the
classification is not a matching theorem for this target. No reliance
on its quoted Lemmas 4.2/4.3 is needed. Publisher PDF returned 403;
the versioned primary arXiv PDF was accessible, so there is no essential
source blocker. Referenced classification proofs were not traced further
because this route requires additional unproved hypotheses.

## Local duplicate and failure comparison

ATTEMPTS/016 and L023 refute disjoint-triple forcing in balanced families.
Its displayed translates {0,1,2,4} and {1,2,3,5} meet in two labels,
so that example does not meet the present linearity premise. This is
inspection of its displayed evidence, not a new construction.
ATTEMPTS/017 and L025 refute a six-edge/eight-vertex extraction; the
first two displayed translates meet in two labels as well. Matching
number two in either example already supplies a disjoint pair; neither
is a counterexample to this target.

ATTEMPTS/027 and L072 give a linear affine-plane witness preventing
additional pairs with union five or six. Its proof explicitly contains
disjoint parallel lines. It does not assert a two-plus-two restriction
to this S or absence of a disjoint pair in such a restriction. Thus it
stops the stronger/different useful-pair route, not the present claim.
Do not infer that the whole sixteen-edge witness is an admissible
12–14-edge restricted family.

The October 20 uniform-disjoint-pair assessment expressly leaves
extraction unresolved and permits no transport of labeled moment
exclusions. Reuse its coding-theory and exterior-algebra coverage only
if later applying incidence to actual pencils; it is not needed for
this pure finite-incidence implication. The October 4 assessment's
1991 Füredi coverage has a large-degree caveat and concerned matching
number two; today's direct 1981 corollary read addresses matching one.
No duplicate of the exact implication was found in these checked paths.

## Search scope and qualifications

Queries included `intersecting linear 4 uniform hypergraph 12 edges 16
vertices maximum degree 4`, `linear intersecting hypergraph 4 uniform at
least 12 edges projective plane 13`, `linear intersecting (2,2)
hypergraph`, `intersecting partitioned linear hypergraph`, `linear
intersecting two parts hypergraphs`, and `linear intersecting bipartite
4-uniform`. Followed the author's publication list to Füredi's original.
No exact partition theorem was located; unsuccessful searches establish
no novelty. General projective-plane constructions do not automatically
meet the prescribed partition. The search-result lead *Degrees, sizes
and chromatic indices of uniform hypergraphs* was not read (fetch
timeout); its displayed large-degree hypothesis does not certify degree
four and it is not an essential input. No persistent dependent blocker
is retained.

Mathlib coverage of the exact implication and the cited general
corollary was not checked. No absence claim is made. No lemma, new
incidence bound, counterexample or mathematical script was produced.
