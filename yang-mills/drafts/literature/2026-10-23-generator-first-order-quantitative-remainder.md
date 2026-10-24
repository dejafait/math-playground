# Generator-displacement first-order remainder — source comparison

TARGET: Determine whether L119's exact first-derivative insertion satisfies |Delta_V-V_N| <= C_i N^(5/2)log(eN)^2 for both actual probes.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the parent transverse-H assessment's primary-source comparisons; searched local assessments, the original generator-linearization draft, ATTEMPTS/032 and recent compression history for this exact remainder and duplicates; six bounded external queries below supplied no inspected matching response theorem.
SOURCE_EVIDENCE: Reused the parent and L267 audit's inspected Lawler--Limic (2010), section 1.1 and Theorem 4.3.1 pp. 81--83 at https://www.math.uchicago.edu/~lawler/srwbook.pdf; inspected NIST DLMF v1.2.8 section 1.4(vi), (1.4.35)--(1.4.37), hypotheses and both remainder forms at https://dlmf.nist.gov/1.4#vi; read L119 in full, L028 proof section 1 through (4) and its ensuing displacement paragraph, L110 definitions/conclusion, L111 exact placement and proof sections 3--4, and L267's scalar normalization and (8)--(14).
COMPARISON: Standard Taylor calculus and the already audited L267 full-matrix decay cover the scalar and kernel inputs; L119(9)--(15) supplies the exact qualitative reduction and full trace/heat envelope. No inspected source or local result states the requested quantitative response remainder. A joint clipped-moment specialization is needed, with no reproof of the scalar Green theorem or Taylor's theorem.
GAP: Quantify L119(12)'s exact all-offset eta(a), with its finite shifts and clipped Taylor modulus, then use L119(13)--(15) unchanged to test the displayed response threshold. This review proves neither that modulus nor the rate, and excludes V_N's coefficient comparison and the other transverse-H errors.
REASON: Essential source coverage is accessible and sufficient for one bounded quantitative remainder attempt; the unproved difference is its joint lattice-sum estimate and exact finite-trace specialization, rather than a missing source or a new continuum hypothesis.
SCOPE: Only the difference Delta_V-V_N defined in L119(3),(7), for relative SU(2) cube, sufficiently fine even N, a=8/N, tau=1/16, lower-rooted forest, stored coordinates and bare-first order; both probes i=3,6, both coefficient levels, all stencil shifts and generator orientations, both residual Q forms, finite middle P, upper jump, all source/end rows, constant modes and full heat sums remain.

LITERATURE_REASON: The saved narrower quantitative target was REVIEW_REQUIRED at invocation start; the ready compression audit and qualitative parent coverage do not assess its clipped Taylor modulus. This turn completes that separate comparison without deriving the specialization.

## Source scope and applicability

NIST, [DLMF section 1.4(vi)](https://dlmf.nist.gov/1.4#vi),
version 1.2.8, released 2026-09-15, accessed 2026-10-23,
(1.4.35)--(1.4.37), assumes a scalar function in C^(n+1) on the
closed expansion interval and supplies Lagrange and integral remainders.
Use the integral form on line segments of the displacement. L028 proof
section 1, (3)--(4), supplies global smooth u_a, common compact support,
uniform fixed-order derivative bounds and O(a^2) C^r convergence.
Thus this scalar input concerns a smooth prescribed coefficient.
It supplies no regularity of a forest field or projection kernel.
The C^2 and C^1 constants and each finite shift must remain explicit
in a quantitative application. No reproof of Taylor's theorem is needed.

Reuse Lawler--Limic, *Random Walk: A Modern Introduction* (Cambridge,
2010), [author-hosted 289-page text](https://www.math.uchicago.edu/~lawler/srwbook.pdf),
section 1.1 pp. 9--11 and Theorem 4.3.1 pp. 81--83, with the
transient and bipartite proof cases already inspected in the parent
assessment. Its symmetric finite-range irreducible d>=3 walk includes
four-dimensional nearest-neighbor simple walk. The scalar result is
imported through L267: the unnormalized Laplacian has H=G_walk/8.
L267(8)--(10) already handles all nine signed matrix entries, including
mixed shifts, by bounding the scalar asymptotic remainder at four
points. Its independently audited conclusion (1) is the full
Frobenius bound, uniform in every integer axial offset and spatial
argument, including zero. Reuse that local result, rather than
reproving mixed differences or differentiating the scalar remainder.
The existing source comparison remains applicable without changed
walk, covariance, normalization or boundary hypotheses.

Neither source contains a pinned variable-coefficient SU(2) response
theorem. The parent assessment's Adams--Lee 0709.0781v3 section II
and Appendix A, Del Debbio--Patella--Rago 1306.1173v1 section 6,
and Luescher--Weisz 1101.0963v2 sections 7.2--7.4/8.2 exclusions
are reused unchanged: translation-invariant one-loop integrals and
renormalized flowed Ward finiteness do not assign this isolated bare
forest block its remainder. No fresh reading or stronger conclusion
from those papers is claimed. No essential unread source was identified.

## Exact local coverage and difference still to prove

L119 was read completely. Its (7)--(8) fixes the original Delta_V,
with A_r(h) C_r(q) e_j(d+h+q) and the exact difference
b_(r,t)(x+h)-b_(r,t)(y). Its (2)--(3) fixes V_N with the continuum
derivative at the output x. These conventions remain the target;
the scalar expansion point must not be silently moved to x+h.

The existing quantitative inputs, not new conclusions of this review,
are L119(9)'s clipped modulus

    omega_a(d,h)=min(C, delta(a)+C a(|d|+|h|)),
    delta(a)=O(a^2),

and L267(1)'s full-matrix pointwise decay. L119(12) defines eta(a)
by summing the shifted weighted ell^2 norms over every j and every
finite r,h,q. Its proof currently invokes two dominated-convergence
arguments and gives no rate. L119(13)--(15) retains both full
Hilbert--Schmidt factors and bounds the complete response by
C_i N^3 eta(a), with fixed constants absorbed. The next attempt must
compare this exact eta with the requested response budget, rather
than infer a rate from dominated convergence or from a fixed-j tail.

A permissible test is to keep the clipped modulus while splitting
the joint spatial/axial sums into near and far regimes, using L267's
pointwise bound and L119(10)--(11)'s shifted Q_j,W_j bounds where
appropriate. The resulting uniform modulus, if proved, must then be
inserted into the unchanged finite trace count. This is a proposed
calculation, not a derived moment estimate or an asserted improvement.
No global second moment, separately summable absolute first moment,
small projection commutator or finite-covariance substitution is
approved as a premise.

L111(13), checked in its proof section 4, supplies the original
Z=F_l(s)^T P F_k(t) Hilbert--Schmidt envelope and complete polynomially
weighted heat sum for both probes. P stays finite and in this order;
all actual end rows and both coefficient levels stay present.
L267's compression conclusion alone is not a Taylor-remainder theorem.
The narrower task uses its kernel conclusion, not its different
compression selectors or support-clearance trace estimate.

## Search, duplicates and recorded failures

The original `drafts/2026-10-11-other-other-generator-commutator-linearization.md`
and history/145 establish only the qualitative first-order reduction;
history/431 hands off precisely this quantitative gap. Scoped local
searches for Delta_V, V_N, eta(a), first-derivative and L119 quantitative
coverage found no existing proof of the requested rate. L120 is the
subsequent qualitative coefficient comparison, not a duplicate rate.
L267 controls a different complete error. Preserve every unfinished
draft and all imported audit qualifications.

External queries on 2026-10-23 were:

- `"lattice Green function" "commutator" "Taylor" remainder Hilbert Schmidt`
- `"first order" "commutator" "lattice" "Green" remainder`
- `"lattice Green" "weighted" "second moment" decay four dimensions`
- `"lattice Green function" "Taylor remainder"`
- `"lattice" "commutator expansion" "Hilbert-Schmidt"`
- `"generator-displacement" "first-order"`

These searches produced unrelated spin/quantum-simulation and
operator-theory leads, with no inspected matching response statement.
They are unused and unread beyond search excerpts; their presence is
not source evidence. No novelty or global absence claim follows.
The actual positive coverage is the precise Taylor input and the
reused primary scalar theorem with its canonical local specialization.

L109 and ATTEMPTS/032 stop separate first absolute moments of a
projected alternating factor. They do not stop a weighted squared
moment of the already circulated covariance. The original L119 draft
also rejects assuming an unavailable global second moment. This review
preserves that stop: the proposed test retains the clipped remainder
and must prove its sums rather than assume stronger moments. No
varying mass is inserted into a qualitative fixed-mass theorem.

Full matching Mathlib coverage, and supporting Taylor, counting-sum
and Hilbert--Schmidt coverage: **not checked**. Unknown is not absent.

## Bounded continuation and relevance

Essential local inputs are L028 (smooth displacement), L110 (energy
kernel), L111 (exact placement and heat envelope), L119 (exact V_N and
qualitative remainder), and L267 (audited full matrix decay). L120 is the
prospective downstream use: its separate comparison of V_N with the cubic
coefficient remains outside this target. L109 and ATTEMPTS/032 retain the
failure of separate first absolute moments. All unresolved upstream audit
qualifications remain; the present source review did not settle them.

The main gap remains interacting continuum construction, a nonzero physical
sector, the axioms and finite positive infinite-volume mass. A bound for this
one first-order error could supply a quantitative input to the generator
coefficient comparison, without settling that comparison or the three other
transverse-H coefficient remainders. Full quantitative L011 assembly and the
construction gaps remain independent.

The discriminating test remains a uniform finite-mesh bound for the exact
Delta_V-V_N at the displayed threshold after restoring both Hilbert--Schmidt
factors, the outside normalization, every axial level and the full heat sum.
Fixed-offset Taylor convergence alone does not suffice. An uncontrolled
all-offset remainder or an above-budget estimate requires narrowing or
changing the mechanism; it is not evidence of signed growth. No estimate
for V_N-a^(-3)K_(i,V), projection transfer, or full transverse-H rate may be
silently included. Coverage is now ready for the same exact target:
one RESEARCH / REPRODUCTION attempt may specialize these known inputs,
but this LITERATURE / NOVELTY_UNCHECKED turn establishes no new estimate.
No cross-notebook input is proposed. It spends no mathematical
exploration turn. The main argument and DAG are unchanged.
