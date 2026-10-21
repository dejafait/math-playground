# E static trace — quantitative continuum source comparison

TARGET: Determine whether the finite static trace in L101(3) differs from a^(-3) K_(i,E) in L101(5) by O(N^(5/2) log(eN)^2) for both actual probes, retaining the cumulative insertion, moving-cut endpoint and complete heat spectrum.
CHECKED: 2026-10-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Read L101 sections 3–6 and its finite identities, L097's path/spectral/finite-range arguments, L028's coefficient and prefix qualifications, L008's actual forms and heat bounds, L223's exact scope and ATTEMPTS/024–025/030; reused the prior quantitative assessments and performed the four new bounded queries below. No matching full-trace theorem was established.
SOURCE_EVIDENCE: Reused Lawler–Limic Theorem 4.3.1 and newly inspected Corollary 4.3.3, Proposition 4.6.2(a) with its transient proof, and Theorem 6.3.8(a)–(b) with its harmonic-measure proof; inspected Gurevich 1504.02673v2 Conditions 2.1–2.3, Theorem 3.1 and proof opening. Precise versions and applicability follow; Chung–Yau/Dowker and Adams–Lee restrictions are reused.
COMPARISON: Scalar Green differences and harmonic interior estimates are available for an explicit finite-N localization test. Neither they nor the inspected whole-space heat theorem give the ordered variable-coefficient cumulative trace rate. L101's uniform mass-removal estimate supplies only part of that comparison; L223 and L222 control different errors.
GAP: Quantify the ordered transverse inverse/projection products, cumulative stencil convergence, exterior modal coefficients and physical quadrature before the full heat sum; truncation or regularization requires explicit joint dependence on N and auxiliary parameters.
REASON: Essential standard scalar and finite-dimensional inputs are accessible, and a concrete kernel-localization test remains independently assessable. Approve a later bounded attempt on the unchanged target without asserting the rate, a matching theorem or novelty.
LITERATURE_REASON: The static-trace continuum comparison was explicitly outside both ready replacement and diagnostic assessments; its quantitative source coverage was essential and missing at invocation start.
SCOPE: SU(2), relative fixed cube, straight lower-rooted forest, admitted even N, a=8/N, tau=1/16, actual probes i=3,6; exactly L101(3)'s displayed finite static sum minus a^(-3) times L101(5), retaining L101(13) and every heat label. No other component or complete-response rate is approved.

This is one completed literature-only review. No rate is proved and no
lemma or mathematical script is written or changed. The assessment makes
one bounded attempt source-ready, subject to the supervisor's separate
continuation approval; it does not certify mathematical correctness.

## Exact comparison and existing quantitative information

Use T_(i,N), already defined in L223's conclusion, for exactly the
finite static sum displayed in L101(3), excluding its displayed error.
The target is |T_(i,N)-a^(-3)K_(i,E)|=O_i(N^(5/2)log(eN)^2).
The normalized threshold is O_i(N^(-1/2)log(eN)^2), up to the fixed
factor from a=8/N. This restates the request, not a result.

Essential inputs are L008 L028 L065 L097 L101 L223. L101's finite
identities and qualitative limit are imported, not newly audited.
Its (13) retains the quarter-weight layer, full cumulative scalar
transport/shear and triplet terms, and moving-cut u_(a,1)(s) endpoint.
Its (14) is an energy form bound; section 4 identifies the limiting
stencil by divided commutators and axial Riemann sums. The coefficients
have fixed transverse range and compact transverse support. Their
cumulative axial weights need not vanish above the displacement support;
compact axial support of the full cumulative insertion is unavailable.

L101(16) preserves the order
T G (a A_<s) G T^T zeta_k(s)^T S_T zeta_l(s).
Section 5 bounds normalized mass removal by C_i sqrt(epsilon), uniformly
in N, but next uses fixed-epsilon inverse polynomials and fixed-range
walks. It supplies no joint degree/freezing/inverse error at a varying
schedule. Section 6 has a heat-summable polynomial envelope for values,
followed by fixed-mode convergence. A rate needs an error envelope too.
L028(4) supplies coefficient C^r consistency before retraction; L097's
path convergence is stated qualitatively. Its actual product modes and
prefix sums must justify a quantitative comparison. All upper rows,
constant modes, both insertion subtractions and heat labels remain.
No smooth upper extension or outside factor 3 is assumed.

The scoped searches found no duplicate rate in the relevant assessments,
E rate draft, L097/L101/L223 or histories 286–290. This is not an
exhaustive novelty search. L223's accepted static replacement and L222's
diagnostic rate concern separate errors; neither is re-audited here.

## Primary inputs and precise limitations

Lawler–Limic, [*Random Walk: A Modern Introduction*](https://www.math.uchicago.edu/~lawler/srwbook.pdf)
(2010; inspected 289-page author-hosted text on 2026-10-17).
Reuse Theorem 4.3.1, printed pp. 81–84. Newly read Corollary 4.3.3,
p. 84: for d>=3 and symmetric finite-range irreducible walks p in P_d, first
Green differences are O(|x|^(1-d)) and repeated coordinate differences
are O(|x|^(-d)). Proposition 4.6.2(a), p. 97, gives killed Green as
full Green minus its exit expectation for any subset, d>=3; its proof
splits visits at exit. Theorem 6.3.8, p. 131, gives first/second bounded-
step differences at the center of a harmonic ball of radius n, bounded
by C||g||_infinity/n and C||g||_infinity/n^2; its nonnegative case uses
f(0). Its proof retains harmonic measure and an interior buffer.
These cover the three-dimensional nearest-neighbor scalar vertex
inverse with Delta=6(I-P_walk), hence G_Delta=G_walk/6. They do not
identify the relative curvature inverse with scalar killed Green,
or supply mixed-source estimates and the complete ordered trace.
Those reductions and boundary uniformity must be checked locally.

Pavel Gurevich, [*Asymptotics of parabolic Green's functions on lattices*](https://arxiv.org/pdf/1504.02673v2),
v2, 29 June 2016, 37 pages. Inspected pp. 6–12, Conditions 2.1–2.3,
Theorem 3.1, (3.1)–(3.3), and Fourier proof opening. Assumptions:
constant coefficients, even-order strongly elliptic continuous symbol,
an Mth-order finite-difference approximation on the full lattice,
and positive real part of the discrete symbol away from zero. The
remainder is uniform in position and t>=t0 epsilon^ell, with explicit
epsilon/time powers. This is a parabolic whole-space theorem. No
application to the pinned trace, time-integrated differentiated inverse
products or cumulative coefficients has been justified. It is not
imported into the continuation; its remaining proof is unread.

Reuse the prior Adams–Lee 0709.0781v3 Appendix A assessment: its
translation-invariant integral hypotheses and parameter-dependent
constants have not been matched to this trace. Reuse Chung–Yau/Dowker
interval statements only as scalar building blocks. Reproving those
results would not address this difference. These comparisons are in
[the replacement assessment](2026-10-17-e-static-replacement-quantitative-rate.md)
and [the broad rate assessment](2026-10-17-complete-coefficient-quantitative-remainder.md).
The official Jaffe–Witten version/scope are reused from the former's
2026-10-17 source check and foundations/01-target-and-scope.md; this
step changes no construction route or interpretation of the target.
Full and supporting Mathlib coverage have not been checked; unknown
availability is not absence.

## Bounded search and approved test

New queries on 2026-10-17:

- `discrete Laplacian Green projection variable coefficients trace asymptotics quantitative lattice Dirichlet box`
- `Lawler Limic Random Walk Modern Introduction theorem 4.3.1 4.6.2 Green function difference estimates pdf`
- `"trace" "discrete" "Laplacian" "Szego" variable coefficients inverse`
- `"discrete Green" "mixed derivatives" "Dirichlet" estimates cube`

These found the inspected scalar and parabolic sources. Chanzy's
two-dimensional rectangle inverse-trace work, general Szego/Toeplitz
leads and finite-difference numerical papers were not read at theorem
level and supply no coverage. No novelty or global absence follows.

Keep the cumulative stencil in the original ordered trace and test
quantitative finite-radius localization of the energy-sandwiched
transverse Green products. Import the named scalar results if used,
verifying relative component reduction, with radius and boundary errors
explicit before coefficient freezing. Also account for actual finite-
mode coefficient errors and physical quadrature within this same trace
comparison. Select a radius or mass schedule only after finite-N bounds
with stated dependence; never insert a varying parameter into a merely
fixed-parameter limit. This proposes a test, not a new estimate.

ATTEMPTS/024 excludes deleting the surviving upper Dirichlet correction;
025 excludes an absolute-profile shortcut for a different first pair;
030 records nonuniform fixed-mass cubic transfer. These do not disprove
the present signed error after subtracting its own continuum term.
Do not infer arbitrary mixed Green differences just from repeated-
coordinate bounds without justification. No infinite inverse is assumed
bounded on all l2, no multiplier is commuted through G or S_T, and no
rough prefix is assigned smoothness across the pin.

Continue on a complete bound meeting the stated threshold, a stronger
bound, or new evidence isolating a failed shortcut with an independently
testable alternative. Abandon the particular mechanism if it leaves an
uncontrolled boundary/source sector, nonsummable modal constants or
unstated parameter dependence; such failure is not signed growth.
After two unproductive mathematical attempts reassess the mechanism.
There is no essential inaccessible source for this bounded test.
Mathematical exploration usage remains zero on this new target.

## Relevance and remaining gaps

The main gap is interacting cutoff removal with the required continuum
axioms and finite positive mass; reflected error <=c_box/2 is unproved.
This intermediate rate could combine with L223's O(N^(5/2)) replacement
bound to control the E component below cubic scale. Other component
rates, the full-response remainder, L220's separate audit and coupling-
uniform interacting control remain independent and unproved. All
continuation inputs retain their original hypotheses; no uniform
localization rate is imported from a qualitative limit. No cross-
notebook mathematical input is used. PROOF.md and DAG.md stay unchanged.
