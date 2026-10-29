# Scale-adapted complementary mass: completed source comparison

TARGET: Review scale-adapted finite-factor bounds and shifted second moments for the L471 sector 1<d_j log T<=log T/16.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact scale-adapted/zero-quotient/finite-Blaschke moment searches and narrow local comparisons found no matching complementary pair-mass bound. Inspected Bettin v1, Titchmarsh's uniform mean square and the Conrey--Keating wider-shift lead; reuse L474's finite-factor assessment and preserve the parked selected-energy/Dirichlet routes. Queries and limits below; no novelty claim.
SOURCE_EVIDENCE: Bettin arXiv:1111.0925v1 Theorem 1 p. 2, Lemma 1 p. 3, standing assumptions p. 5 and small-imaginary-difference case pp. 9--10; Titchmarsh--Heath-Brown (1986), Theorem 7.2(A) p. 141 and its proof, (2.1.9)--(2.1.10) p. 16, (4.12.3) p. 78 and Section 5.1 p. 95; DLMF 5.11.1--2/5.11.9 and bounded-real-part uniformity; Conrey--Keating arXiv:1506.06842v1 Section 2 p. 2 and reference B p. 12. Local L471 definitions, L474 Sections 1--4, L465 Section 2 and L018.
COMPARISON: Bettin v1 does not cover shifts growing beyond O(1/log T); its broader-shift remark is not a theorem. Titchmarsh 7.2(A) instead supplies the uniform continuous upper bound on the right of 1/2, with reflection and explicit chi cost on the left. Sector Stirling supplies completion costs. These cover a bounded scale-adapted test, not its factor compensation or a mass saving.
GAP: Derive the band majorant with its full radius, completion, reflection, area-overlap and residual-factor costs; test summable decay in u without assuming occupancy or sparsity. No complementary mass estimate, cancellation of growth costs or optimized comparison is established.
REASON: Essential source coverage for a concrete classical-tool specialization is accessible. Nominate one bounded compensation-versus-growth calculation, with the single-pair case mandatory; a genuinely new cancellation mechanism is not yet justified. The proposed continuation requires separate approval next turn.
LITERATURE_REASON: Real shifts now have size O(d_j) rather than O(1/log T); the completion ratio is no longer uniformly bounded by the existing microscopic argument. Essential coverage of this change is missing.
SCOPE: Actual Xi; L471's multiplicities, one-pair quotient and clipped windows; 1<d_j log T<=log T/16, with no RH, simplicity, separation, density, selected-energy saving or external fixed-half-plane premise. The sector d_j>1/16 and the fixed microscopic annulus remain independent gaps.

## Original review plan (preserved; comparison completed below)

Set L=log T. For each u>=1 with u<L/16, consider the part of L471's
B(T) with u<d_j L<=min(2u,L/16). This is a proposed dyadic band,
with its full m_j and actual J_j(T) retained. No bound is asserted.
The ultimate useful threshold for this sector is o(T L^3). The first
test is narrower: obtain from the inspected source statements an
explicit list of costs and admissible radii for one such band, so a
subsequent mathematical attempt can decide whether a summable saving
in u is possible or an unavoidable cost prevents it.

The proposed mechanism changes spatial scale with displacement instead
of trying to improve a fixed-radius selected norm. A disk radius R=C d
for fixed C>1 could retain the pair geometrically. Its real-shift range,
gamma variation, norm cost, and occupancy compensation must ALL be
compared; no claim of a useful tradeoff has been derived. Treat the
parameter C and exact allowable upper displacement as review questions,
not assumed admissible choices.

Read Bettin's exact real-part bounds, joint shift uniformity, main-term
pole prescription and the relevant proof case before claiming its
applicability. Reuse its already assessed microscopic case. Check
stronger shifted-moment estimates and prior local failures specifically
for this growing microscopic radius. L471's replacement F_j=-AZ/q_j
and ordinary fourth-moment loss, L473's finite-law obstruction, and the
parked positive-energy route remain intact. No generic zero-count or
sparse-occupancy hypothesis may fill the gap.

Continue toward a bounded creative attempt only if the completed
comparison supplies an explicit admissible normalization and a test
that distinguishes factor compensation from the real-shift growth cost.
Otherwise record the source-level obstruction and select a different
mechanism. No source-access-only chain is intended. A successful band
bound would still leave the other displacement sectors, conversion
from mass to individual signs, higher signs and RH unresolved.

This nomination approves source comparison only. It derives no new
lemma and contains no mathematical certificate. No cross-notebook input.
Full matching Mathlib coverage is not checked.

## Inspected source statements and limits

**Bettin: the real-shift limitation is genuine.** Sandro Bettin,
*The second moment of the Riemann zeta function with unbounded shifts*,
Int. J. Number Theory 6 (2010), 1933--1944,
[arXiv:1111.0925v1](https://arxiv.org/pdf/1111.0925v1#page=2),
Theorem 1, assumes absolute real parts of both shifts bounded by a
fixed multiple of 1/log U. Its integrand is
zeta(1/2+a+it) zeta(1/2-b-it); the main integrand is
zeta(1+c)+zeta(1-c)chi(1/2+a+it)chi(1/2-b-it), c=a-b,
with the pointwise c->0 prescription and error
O((sqrt(U)+sqrt(|Im a|)+sqrt(|Im b|))log^2 U).
The sentence preceding the theorem only anticipates bounded real
shifts. Lemma 1 and the standing assumptions retain microscopic real
parts; the pp. 9--10 small-imaginary-difference case does not remove
that restriction. Therefore a constant in O(1/log U) cannot silently
grow with the band parameter u. The microscopic L474 application
remains covered; the proposed uniform larger-scale application is not.

**An independent uniform mean-square input is sufficient for a test.**
E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, second
edition revised by D. R. Heath-Brown, Oxford (1986),
[Theorem 7.2(A), printed p. 141](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=75),
states, with an absolute constant K,

    integral_1^U |zeta(sigma+it)|^2 dt
      <= K U min(log U, 1/(sigma-1/2)),   1/2<=sigma<=2.

At sigma=1/2 the minimum means log U. Read the proof on that page,
including its uniform Dirichlet-sum estimate and both bounds on the
off-diagonal term near 1/2. This is uniform, unlike Theorem 7.2's
fixed-sigma asymptotic. For the left side use the functional equation
(2.1.9)--(2.1.10), p. 16, retaining |chi(s)|^2. Equation (4.12.3),
p. 78, and Section 5.1, p. 95, give
|chi(sigma+it)|=(t/(2pi))^(1/2-sigma)(1+O(1/t)) uniformly on
fixed real strips. No off-line-zero sample or short-interval estimate
is asserted. High dyadic intervals are contained in [1,3T]; the
nonnegative integrand permits this upper-bound use.

**Completion costs must be calculated, not declared bounded.**
[NIST DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9) states

    |Gamma(alpha+i beta)| ~ sqrt(2pi) |beta|^(alpha-1/2)
                                      exp(-pi |beta|/2),

uniformly for bounded real alpha as beta->+/-infinity. Also inspected
[5.11.1--2](https://dlmf.nist.gov/5.11#i), with the closed-sector
condition |arg z|<=pi-delta. These are the classical inputs to L465's
normalization estimates. Reuse its sector control, but not L474's
microscopic bounded-ratio conclusion on a larger disk. The polynomial
s(s-1)/2, pi^(-s/2), Gamma(s/2), both signs of vertical displacement,
and the horizontal variation relative to A(c) must all remain in the
future calculation. Gamma has no pole on the high-height rectangles.
No specialized completion estimate is proved in this review.

**A stronger-shift lead is not used to extend Bettin v1.**
Conrey--Keating, *Moments of zeta and correlations of divisor-sums: I*,
[arXiv:1506.06842v1, Section 2, p. 2](https://arxiv.org/pdf/1506.06842v1#page=2),
reports a wider real-shift range for Bettin; reference B, p. 12,
identifies the published paper. That report is not a replacement for
the narrower inspected primary theorem. A wider primary theorem and
its error uniformity were not established here. This version/scope
question is nonessential because 7.2(A) supplies the upper-bound
input needed for the nominated calculation. No general two-shift
asymptotic outside v1's hypotheses is imported.

## Finite-factor scope and an admissible proposed geometry

Reuse L474's inspected Broughan II (2017), Theorem 3.3, proof (1),(4),
pp. 26--27: the finite disk supremum statement permits arbitrary
finite zero lists and repeated factors. It has no microscopic
physical-radius restriction. L474's Section 3 is the local precedent,
not a new theorem to reproduce here. A disk rescaling still requires
its own denominator, evaluation-point and multiplicity checks.

One concrete choice to test is h=u/L, cells of width h, radius 6h,
and an area collar h. Here 1<=u<L/16 and the selected band is
u<d_j L<=min(2u,L/16). The outer radius is at most 7/16; the
zeta real parts on it therefore lie in [1/16,15/16], and reflection
puts the left side within 7.2(A)'s [1/2,2]. This domain check is an
applicability comparison, not a new norm or mass estimate. It also
keeps the completion formula within L018's Re s>0 domain and at high
imaginary height, away from the zeta pole. No enlargement beyond
these fixed domains is approved by this comparison.

The cost inventory is now explicit at the level of source inputs:
7.2(A)'s minimum; the functional equation's chi factor; bounded-strip
Stirling's power and exponential factors; finite-factor division
and its unremoved copies; submean area scaling and disk overlap.
Their combined dependence on u is UNCALCULATED. The full m_j,
one-pair removal and clipped J_j(T) must be retained. In particular
the single-pair cell is an obligatory test, since no occupancy
lower bound is available. A large-cluster bound alone cannot settle
the band sum.

## Searches, duplicates and decision

Queries included `Bettin second moment zeta unbounded shifts real
parts Theorem 1 1111.0925`, `zeta mean square uniform 1/2 sigma 3/4
Titchmarsh theorem 7.2 formula error`, `Riemann zeta mean square
uniform sigma 1/2 1 Ingham second moment theorem pdf`, `zeta Xi
Blaschke mean square zeros`, and `zeta finite Blaschke second moment`.
Search leads were followed to the primary statements above. General
xi pages, conditional shifted higher moments, and work on different
tempered functions were not used as theorem evidence. No inspected
source gives the exact complementary mass saving; this bounded
comparison establishes neither novelty nor its impossibility.

Narrow comparisons used L471's ordinary-fourth-moment loss, L474,
the small-displacement cluster assessment/attempt, and the completed
zero-selected-disk and nonreal-factor-Dirichlet assessments. Their
fixed microscopic selection/positive-defect stops remain recorded.
None supplies the changed real-shift costs. Merely allowing a growing
constant in the old microscopic bound would not be a valid extension.

Continue to ONE calculation of the specified band scheme: obtain
its full u-dependent upper envelope and compare it with a dyadically
summable tail. Continue this implementation only if that comparison
produces decay or identifies a precise additional constraint with an
independent plausible test. If the available majorant fails even in
the admissible single-pair case and offers no such constraint, park
this implementation. Failure of an upper-bound method does not
disprove a band estimate or RH. Fixed u, the microscopic annulus,
d_j>1/16, full B(T), and individual/higher signs remain separate.

This is a completed literature comparison, with no new lemma, script,
band bound or mathematical certificate. The next bounded calculation
is nominated in `2026-10-28-scale-adapted-band-cost-test.md` for separate
approval. It is an established-tool specialization; no justified
creative cancellation mechanism has yet been identified. Full matching
Mathlib coverage is not checked; it is not inferred absent.
