# Weighted bulk collision estimate — completed bounded source review

TARGET: Bound L104's weighted disjoint-collision excess over r=4,...,67 by (T-C/D)^2-delta.
CHECKED: 2026-10-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the prior centered-moment and fixed-pole assessments; searched prescribed-coefficient split-polynomial variance, subgroup-root collisions, subset products and finite-abelian-group subset counts, then inspected the two additional primary comparisons below; no matching effective estimate was located in this bounded search.
SOURCE_EVIDENCE: Newly read Li–Wan, Counting subset sums of finite abelian groups, author manuscript Theorem 1.1 and Section 4 full-group cycle-count cases; Gorodetsky 1810.00483v2 definitions (1.5),(1.16), Theorems 1.3/2.1, Lemma 3.2 and its proof, and Section 4 variance proof; prior Tao/Gao/shifted-energy/additive-moment and Li–Wan sieve coverage is reused at its recorded passages.
COMPARISON: Li–Wan's exact formula requires the subset domain to be the whole group; Gorodetsky's quantitative bounds require a factorization function, which does not retain specified H-root labels; his arbitrary-function variance identity adds no estimate to L104; none supplies the roughly 5.89-ppm finite weighted excess bound.
GAP: An effective estimate for the full three-coordinate, ordered, disjoint collision sum with its signed uniform subtraction remains unproved; no inspected theorem establishes either the desired bound or its failure.
REASON: The bounded source comparison is complete enough for one finite mathematical test of the unchanged target after separate approval; EXPLORE is permission to investigate, not a bound, novelty claim or renewal of the exploration budget.
SCOPE: Exactly the parameters and pending sum below; one bounded aggregate second-moment/collision estimate retaining signed centering and all three residue coordinates, with an exact finite threshold comparison; no changed pole/domain/group, pointwise-envelope retuning, product-only replacement or projective transport.
LITERATURE_REASON: Changed target from the centered collision reduction to an effective bound on its explicit weighted bulk excess; no estimate with these hypotheses was approved previously.

## Exact scope, unchanged from the pending assessment

Keep Q=65537, E=F_Q, H=<19139> of size 1024, pole 3,
s=67, F=F_(Q^28), degree<64 and every m>=1. Use L104's
K_r counting ordered disjoint r-subset pairs with equal residues
modulo (X-3)^3, P_r=binomial(1024,r)binomial(1024-r,r),
w_r=binomial(1024-2r,67-r), C=binomial(1024,67),
D=(Q-1)Q^2, T=Q^28/2^128 and

delta=C-D^(-1)sum_(r=0)^3 w_r P_r.

The pending quantity is exactly

    sum_(r=4)^67 w_r (K_r-P_r/D).

It must be bounded above by (T-C/D)^2-delta. All three unit
coordinates, the ordered convention, common-set weights, empty
labels and signed centering remain essential. A product-only moment,
an additive power-sum count or a pointwise character envelope cannot
be substituted without a justified transfer at this scale.

Essential local inputs are L104, L102, C012a and foundations/02;
L104's separate critical audit remains pending. The prior assessment
is drafts/literature/2026-10-20-translated-pole-centered-second-moment.md.
ATTEMPTS/007–008,085–086 remain failure comparisons, not estimates
of the actual centered energy. No cross-notebook result is proposed.

## Completed review — step 389

LITERATURE / NOVELTY_UNCHECKED / literature_comparison; EXPLORATION.
This completes previously missing source comparison, without a new
mathematical result, lemma, script or energy certificate. The assessment
has changed this turn and needs separate supervisor approval before a
research invocation. No mathematical exploration turn is spent or reset:
the count stays 2/3. The main gap remains arbitrary-center 67/68 safety.
The intermediate target is this finite bulk bound; its downstream use is
only exclusion of L102's center family through L104, conditional on that
reduction's correctness. L104's separate critical audit is still pending.

### Search and local comparison

Queries included `finite fields prescribed coefficients split polynomials
variance subset products Hayes equivalence class second moment`,
`multiplicative subgroup prescribed coefficients polynomials number
subsets variance collisions`, `"subset sums" "finite abelian groups"
"Li" "Wan" theorem`, `"variance" "factorization" "short intervals"
"finite fields" Gorodetsky`, `"subset products" "second moment" finite
group`, `"prescribed coefficients" "variance" "split" polynomials`,
and `"subset" "collision" "abelian group" Fourier counting`.
Follow-up title searches located the primary texts below. Unrelated
search results supply no coverage. Two mistaken arXiv identifiers
(1112.5699 and 1112.0275) were discarded on title inspection; neither is
a mathematical source for this assessment. The requested nonexistent
1810.00483v3 was corrected using the abstract page's v2 link.

Read L104's full canonical proof, L102's hypotheses/dictionary/import
passages, C012a's field/pole certificate and foundations/02's pinned
model. Reused the prior centered-moment assessment and the fixed-pole
and correlated-cubic assessments at their source-comparison passages.
History 388 and ATTEMPTS/007–008,085–086 were checked. The stopped
unsigned cycle norms, residual-pair root allowance, absolute sieve and
literal projective transport do not estimate the actual bulk excess.
No sibling notebook or cross-notebook theorem was read.

### Newly inspected primary sources

1. Li and Wan, *Counting subset sums of finite abelian groups*,
   J. Combin. Theory Ser. A 119 (2012), 170–182,
   DOI [10.1016/j.jcta.2011.07.003](https://doi.org/10.1016/j.jcta.2011.07.003).
   Read the undated 14-page [author manuscript](https://webapps.math.uci.edu/~dwan/liwan4.pdf)
   linked from Wan's bibliography: introduction and Theorem 1.1,
   printed pp. 1–2; Section 4, printed pp. 11–12, especially the
   coprime and general cycle-gcd cases. The theorem explicitly counts
   k-subsets of **all** A, with A a finite abelian group. It gives
   N(k,b)=|A|^(-1) sum_(r|gcd(|A|,k))
   (-1)^(k+k/r) binomial(|A|/r,k/r) Phi(r,b), with Phi defined
   there from the cyclic invariant factors and integer Moebius function.
   Its proof counts linear equations with variables free in A, then
   imposes distinctness. A 1024-point image of H in the much larger
   residue-unit group is not the whole-group domain stipulated there.
   No group identification meeting that hypothesis is supplied locally.
   Thus the exact formula cannot certify our restricted collision sum.
   The general distinct-coordinate sieve is already covered separately;
   no reproof is needed. Initial www.math.uci.edu and CiteSeer retrievals
   failed; following the author's webapps bibliography link resolved
   access, so this is not an essential source blocker.

2. Gorodetsky, *Mean values of arithmetic functions in short intervals
   and in arithmetic progressions in the large-degree limit*,
   Mathematika 66 (2020), 373–394,
   [arXiv:1810.00483v2](https://arxiv.org/html/1810.00483v2), 2022-04-22.
   Read Section 1.1's extended factorization type, arithmetic-progression
   variance (1.16), Theorem 1.3 (1.18), Theorem 2.1 (2.1)–(2.2),
   Section 3.1's Hayes hypotheses, Lemma 3.2 (3.17)–(3.22) including
   its complete orthogonality proof, and Section 4's variance deduction.
   For a factorization function alpha and nonzero modulus M of degree
   at most n, (1.18) bounds the averaged progression variance by
   max|alpha|^2 q^n/phi(M) times exp(O_q(n loglog(n+2)/log(n+2))).
   There is also the explicit finite character bound (2.1), with factor
   7 q^(n/2) binomial(20(ell+deg M+1)+n-1,n); constants are therefore
   not the sole issue. Both bounds require alpha to depend only on
   irreducible degrees and multiplicities, whereas our H-root restriction
   depends on root labels. Lemma 3.2 allows arbitrary arithmetic
   functions, but supplies only a character/variance identity, consistent
   with L104. Theorem 1.3's proof inserts the restricted Theorem 2.1;
   that hypothesis is not removed. No H-restricted quantitative theorem
   is imported. An Oxford repository request failed; arXiv v2 resolved
   the essential passages.

The comparison, rather than a new theorem specialization, explains why
neither citation suffices. In particular the indicator of full-field
squarefree splitting loses the H restriction. A larger raw collision
count cannot simply be re-centered using our smaller C. No transfer of
its variance or effective constants is approved here. Full matching
Mathlib coverage for this effective collision estimate was not checked;
unknown coverage is not evidence of absence.

### Reused coverage and limits

The 2026-10-20 centered-moment assessment already inspected Tao's finite
Parseval theorem, Gao v5's arbitrary-domain factorial-moment formulas,
Macourt–Shkredov–Shparlinski v2's shifted-subgroup product energy, and
Lai–Marino–Robinson–Wan v2's additive moment subset sums. Their exact
passages and hypothesis mismatches remain as recorded there. The
fixed-pole assessment already covers Li–Wan 1507.06329v1 Theorem 2.1,
Corollary 2.2 and Lemma 2.6's generating identity, and 1806.00152v3
Lemma 4.1's complete character bound. These are usable tools, not a
theorem about the pending aggregate centered error. The broader
correlated-cubic review likewise did not supply such an estimate.
No essential unread source is asserted as a dependency of the bounded
test. Search-only leads on general subset-product covering, algorithms
and newer subset-sum designs remain uninspected and supply no theorem
input. This bounded search does not establish novelty or nonexistence
of a matching result.

### Bounded mathematical continuation and stopping test

After separate approval, the unchanged TARGET permits one attempt to
bound the **aggregate** centered collision quantity, using L104 and
the already cited finite-group/signed-sieve tools. A plausible mechanism
is to retain correlations in the character-averaged squared subset sum,
or equivalently the full disjoint collision sum, before any norm bound.
No inequality for that mechanism is derived in this literature turn.
It must produce an explicit finite inequality or an independently
checkable obstruction; a new name for a pointwise cycle envelope does
not reopen ATTEMPTS/007 or 085. Re-deriving L104 alone is a duplicate.

Continue this sufficient energy route if a justified upper certificate
meets exactly (T-C/D)^2-delta, or a quantitative intermediate estimate
demonstrably reduces the unresolved bulk requirement. A rigorous lower
bound above that budget stops this sufficient energy test only. An
insufficient upper allowance stops that allowance, without implying
actual large energy or a large fiber. Preserve all r=4,...,67 weights,
ordered disjointness, empty classes, full D and signed subtraction;
individual excess terms need not be nonnegative. Dropping the product
coordinate or replacing H by the full field requires a proved transfer.

If the next attempt produces only another formal reduction or no
informative estimate, it is the third mathematical exploration turn
and requires mechanism reassessment. Do not renew that budget by this
literature review. Arbitrary-center safety, actual fibers, L104's audit
and the ABF comparison remain independent unresolved obligations.
No complete candidate or progress beyond the checked sources is claimed.
