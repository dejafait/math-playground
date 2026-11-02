# Three scaled pole moments — completed source comparison

TARGET: Test whether the first three n-scaled inverse-Blaschke pole moments have a uniform positive lower bound on C645d's admissible clusters.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed the bounded exact-weight, Prony, confluent-Vandermonde and collision searches listed below; checked C645d/L645 and the named local scalar and growing-Pick comparisons. No inspected theorem settles this correlated three-moment family; failed searches do not establish novelty.
SOURCE_EVIDENCE: Batenkov, arXiv:1212.0172v2, Definition 1/Theorem 1, Lemma 1 and full Sections 2–3 https://arxiv.org/pdf/1212.0172v2 ; Batenkov–Yomdin, arXiv:1106.1137v3, Lemma 4.2/Corollaries 4.3–4.4/Theorem 4.5 and proof pp.10–12 https://arxiv.org/pdf/1106.1137v3 ; Batenkov–Yomdin, Journal of Singularities 10 (2014), Sections 6.2–6.4, Theorems 6.10/6.14/6.17 and collision proof cases pp.14–20 https://dimabatenkov.info/pdf/batenkov_geometry_2014.pdf . Reuse the saved residue/contour coverage without repeating it.
COMPARISON: Quantitative inverse-Vandermonde bounds require separation; Prony local inverse constants depend on the node configuration. Divided-difference coordinates handle collisions locally, but do not provide a global lower bound for the three specified moments with inverse-Blaschke-correlated amplitudes, an anchored unit term and potentially unbounded scaled displacements.
GAP: Prove the exact separation-free, all-large-n lower bound below or construct an admissible degenerating family refuting it; fixed-cluster invertibility, local continuity and bounds containing an unassumed separation factor do not suffice. Actual-Xi and contour-transfer gaps remain independent.
REASON: Essential source comparison is now complete for this bounded finite-family question. EXPLORE licenses a separate mathematical test of the identified difference, with no lower bound, obstruction or originality claim established by this literature turn.
LITERATURE_REASON: The changed vector weights required previously unread quantitative moment and collision cases; the ready scalar audit and residue calculus did not cover them. Those missing comparisons were inspected here, so unchanged follow-up browsing is unnecessary.
SCOPE: The exact TARGET and all hypotheses below are retained. This assessment covers a proof or counterfamily attempt for that test, including coalescence and escaping scaled displacements, without adding separation, positive moment weights or Xi realization. It does not cover a larger cluster or a contour-transfer theorem.

## Exact target retained after source review

Fix delta in (0,1/2), a=3/2, d=a-delta, R=a-delta/2 and x=-d.
Use L645/C645d's unchanged complex product

    B_n(z) = product_(0<=j<n) R(z-i j/n)/(R^2+i(j/n)z), n>=5.

The synthetic cluster Z contains x and at most two additional distinct
points z, each with residue one, satisfying

    |z+d| < delta/8,   -3/2 < Re z < -1,   |z| < R.

Every cluster point avoids the grid. There is no lower separation
assumption, Xi realization, symmetry, PSD or interpolant hypothesis.
Retain all these hypotheses rather than silently adding separation.
For k=0,1,2 the proposed observables are

    M_(n,k)(Z) = B_n(x) sum_(z in Z) [n(z-x)]^k / B_n(z).

For k=0 the polynomial weight is identically one, including at x.
The question is whether constants c_delta>0 and an integer N_delta
exist such that

    max_(k=0,1,2) |M_(n,k)(Z)| >= c_delta

for every integer n>=N_delta and every permitted Z, or whether a
rigorously specified admissible family makes that maximum tend to zero
along unbounded n. Exact simultaneous cancellation would also refute
the bound. A numerical sample, mere nonvanishing at each fixed cluster,
or a bound with an unassumed separation factor does not settle it.
No outcome of this mathematical test is asserted in this review.

## Relevance, comparison and stopping boundary

Main gap: actual-Xi signs/all-degree mixed positivity and the detector's
derivative normalization. Plausible downstream use: a vector of contour
observables could detect a cluster missed by the single scalar sum.
The completed comparison below addresses finite power moments,
confluent Vandermonde interpolation, exponential sums and clustered
meromorphic residues. These sources supply comparison tools; none is
imported as the asserted lower bound.

Continue only with a source-covered proof target that retains uniformity
as permitted points coalesce. A proved degenerating family would stop
this particular three-moment mechanism. The present review completes
the essential source scope for this finite-family test. Its proposed
mathematics has not been attempted or approved as true in this turn.

Essential local inputs are C645d's canonical definitions and audited
scalar obstruction and L645's unchanged factors/grid. Neither supplies
the vector lower bound. The parent contour assessment records that a
later Xi application still needs actual pole realization, arbitrary
other-pole/multiplicity control, grid interpolation, contour clearance
and uniform boundary control for an n-dependent positive-real P.
Additional polynomial-weight boundary costs also need checking there;
they are not part of this finite-family test. No cross-notebook input
is requested. Full matching Mathlib coverage remains unchecked.

## Completed review — 1 November 2026

### Quantitative inverse matrices: explicit separation

D. Batenkov, *On the norm of inverses of confluent Vandermonde matrices*,
[arXiv:1212.0172v2](https://arxiv.org/pdf/1212.0172v2), 4 December 2012
(the PDF's internal date separately says November 2018), Definition 1
and Theorem 1, p.1; Lemma 1 and complete proof, pp.2–3.
For distinct complex nodes with |x_j|<=1, multiplicities ell_j>=1 and
N=sum ell_j, the theorem assumes |x_i-x_j|>=eta>0. The inverse row for
the k-th derivative at node j, 0<=k<ell_j, has l1 norm at most

    (2/eta)^N (2/k!) (1/2+N/eta)^(ell_j-1-k).

The proof uses Hermite cardinal polynomials and derivatives of products
of inverse node differences. Confluence means derivative columns at
prescribed repeated nodes; distinct nodes still require separation.
Our scaled nodes need neither stay in the unit disk nor have fixed
positive separation. Any rescaling must account for its parameters.
The theorem supplies no uniform constant for the proposed family.

### Local Prony accuracy: configuration-dependent constants

D. Batenkov and Y. Yomdin, *On the accuracy of solving confluent Prony
systems*, [arXiv:1106.1137v3](https://arxiv.org/pdf/1106.1137v3),
26 June 2012, Lemma 4.2, Corollaries 4.3–4.4, Theorem 4.5 and complete
proof, printed pp.10–12. The square parameter-to-moment map is locally
inverted at a regular point, with errors small enough to stay in that
inverse neighborhood. Regularity requires distinct nodes and nonzero
highest amplitudes. Its constants depend on nodes and multiplicities.
The proof factors the Jacobian and uses an inverse confluent Vandermonde
norm; it gives no configuration-uniform constant at collisions. This
concerns parameter recovery rather than lower-bounding three prescribed
correlated measurements. No specialization or reproof is performed here.

### Collision coordinates: local continuity

Batenkov and Yomdin, *Geometry and Singularities of the Prony Mapping*,
Journal of Singularities **10** (2014), 1–25,
[author-hosted published text](https://dimabatenkov.info/pdf/batenkov_geometry_2014.pdf),
DOI 10.5427/jsing.2014.10a, Sections 6.2–6.4, pp.14–20.
Read the repeated-node definitions, Lemma 6.9, Theorems 6.10/6.14,
their basis proof including the collision case, and Theorem 6.17's full
proof. Divided-difference functionals form a basis even at repeated
complex nodes. A partition works locally precisely when coincident
indices belong to the same block. Near an existing solution of the
rank-restricted problem with its full 2r-moment data, these coordinates
vary continuously as multivalued algebraic functions. The proof retains
a locally nondegenerate moment system. This is not a uniform bound
near zero data or over unbounded scaled configurations. It prescribes
neither inverse-Blaschke amplitudes nor only three measurements.
Generic collision instability therefore does not settle our target.
These are comparison results, not an imported lower bound.

### Exact hypothesis match and the mathematical continuation

For comparison with Prony terminology, the proposed nodes are
u_z=n(z-x) and amplitudes are B_n(x)/B_n(z), exactly as in the definition
of M_(n,k). Those amplitudes are complex and constrained by the same
product as the nodes; residue one before division is not a positive
moment weight. No independent-amplitude countermodel may be substituted.
The family includes arbitrarily close distinct points and displacements
u_z that need not remain bounded as n grows. A source applicable only
to separated nodes, positive real weights, a fixed scaled compact set
or a fixed n would not resolve the target. These are hypothesis
comparisons, not new estimates or assertions that a particular
degenerating regime succeeds.

The standard residue and finite-Blaschke inputs remain those precisely
cited in C645d and the
[parent contour review](2026-11-01-derivative-free-pick-contour-detector.md).
Reuse its inspected Austin–Kravanja–Trefethen (2014), Sections 4.1/4.3,
comparison: root-of-unity boundary data and finite polefinding do not
supply this interior-grid, correlated-weight uniform bound. No contour
formula is asserted here. The new primary sources were inspected only
in the stated results and essential proof cases, not audited as complete
manuscripts. Mathlib matching coverage was not checked; absence is not
asserted.

The sole mathematical continuation remains the exact TARGET. Continue
the mechanism only with a proof retaining all admissible clusters and
constants depending solely on fixed delta. A rigorous permitted family
with all three moments tending to zero stops this three-moment proposal.
An inconclusive attempt must preserve its partial reasoning and identify
a materially new input or refined test before repetition. No numerical
test or mathematical script was run in this source review.

### Searches, duplicates and preserved failures

Queries included `Prony method clustered nodes confluent Vandermonde
moment lower bound complex amplitudes separation Batenkov Yomdin`,
`inverse Blaschke product power moments pole cluster cancellation
Vandermonde`, `"inverse Blaschke" "moments"`,
`"Batenkov" "Norm of the inverses" "Vandermonde"`,
`"moment" "analytic weights" "coalescing" Vandermonde lower bound`,
`Batenkov "Norm of the inverses of confluent Vandermonde matrices"
arxiv`, and `"complex" "moments" "analytic weights" "Vandermonde"`.
The exact-weight searches yielded no inspected matching theorem. Search
results on clustered Fourier matrices, later Prony algorithms and
prescribed critical points of Blaschke products were leads only, not
inputs; the quantitative comparison used the primary sources above.
No claim of exhaustive search or novelty follows.

Local searches covered Pick/pole/Blaschke assessments, C645d/L645 and
related histories/stops; an adjacent Hermite-rescaled heat-cluster
assessment was checked and is unrelated to these moments. The
[C645d scalar stop](../../ATTEMPTS/2026-11-01-inverse-blaschke-unit-residue-noncancellation-stop.md)
and its audit remain unchanged; no vector test was found in the scoped
Pick record. The Vandermonde passage in
[the growing vertical-Pick review](2026-11-01-growing-vertical-pick-block-norm.md)
concerns a different squared-pole Hankel family on a high real axis.
Its external proof was not reopened. No cross-notebook input is used.
No zero-free-region or reciprocal-continuation estimate is proposed,
so those separate baseline sources are not inputs to this step.

This is a completed literature EXPLORATION, not a mathematical advance
or an informative mathematical counterexample. It changes source
coverage from REVIEW_REQUIRED to EXPLORE for the unchanged target.
The main RH gap, derivative normalization, actual symmetries/realization,
unrestricted poles/multiplicities, interpolation, contour clearance and
weighted boundary control remain open. DAG.md, PROOF.md, lemmas/ and
mathematical scripts are unchanged by this turn.
