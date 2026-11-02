# Full grid remainder and finite positive measures — source comparison

TARGET: Assess multipoint Pade and Markov-function remainder theorems for a lower bound mean_u ||kappa_u||^2>=c exp(-n/16)D_single,n in L649's unchanged integer-mass angular family.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact/stronger-result searches for multipoint Pade Markov remainder lower bounds, complex/conjugate interpolation, finite support, prescribed denominators, and logarithmic-derivative rational interpolation; inspected five primary texts below and reused the saved angular Fourier/residue and positive-mass assessments. No matching theorem was identified in this scope; no novelty claim.
SOURCE_EVIDENCE: Gonchar--Lopez Lagomasino (1978), pp.449--453, especially p.450 and remainder (8), p.451; Beckermann--Bisch--Luce 2106.05098v2, (1.1), Theorems 2.1/2.6, (2.3)--(2.5)/(2.15)--(2.16), pp.1,3--4,8; Baratchart--Yattselev 0804.2206v1, Section 2/Theorem 2.3 and (3.51)--(3.53), pp.4--7,22--23; Buslaev (2021), H0 definition/Theorems 1,4 and lower-bound proof case, pp.353,355--357,361--362; Beckermann--Reichel (2009), author PDF (1.4), Theorem 6.1 and proof of (c), pp.3,22--25.
COMPARISON: Ordinary Pade error can vanish for finite support and is not L649's omitted component. The quantitative Markov bounds are upper bounds; the inspected lower bounds require infinite regular support, nonzero arc jumps, or a real-even prescribed-pole geometry absent here. C645y instead supplies a fixed-denominator full-grid interpolant and a degree-M polynomial identity, without the required relative estimate.
GAP: Bound the complete finite-grid omitted energy relative to D_single,n at squared rate 1/16, uniformly in the n-dependent integer atomic measures and arbitrarily close poles. None of the inspected sources supplies that bound or an admissible countersequence.
REASON: The primary-source mismatch rules out the proposed direct Pade/Markov import, not the finite-support detector. A distinct bounded test may use C645y's entire identity (10) and a P-dependent polynomial dual, retaining every grid term; its exact continuation is recorded in the companion assessment for separate supervisor approval.
LITERATURE_REASON: At invocation the target changed from pure-power deweighting to a lower bound on its omitted component; essential primary multipoint Pade/Markov remainder hypotheses and proof cases were unread. This step completes that coverage rather than repeating a ready comparison.
SCOPE: Completed source comparison only; no theorem is imported into the RH argument and no new remainder formula, estimate, lemma or mathematical script is established. The companion full-grid-polynomial-dual assessment specifies the proposed mathematical continuation.

## Exact family, purpose, and scope of the review

Keep n>=5, x=-5/4, R=11/8, eta=1/100, t_j=j/n, distinct
common poles Re(a)=x, |a|<=R-eta, x in Z, positive integer
simple-pole residues r_a, and M=sum r_a<=n/3. Keep all n factors
of B_u and their conjugated denominator angle, all spatial modes,
and both normalized circle means. L649 defines c(u), T_u and
kappa_u=(I-T_u^*T_u)c(u). D_single,n is the exact diagonal energy.
L649 is independently unaudited and must not be treated as an RH input.

The proposed subject is a lower bound on the omitted component, using
the finite positive measure on the pole ordinates and the rational
function's complete pole support. It is not another ambient norm
estimate for recovering h. No claim that a Markov/Pade theorem applies
to the complex rotated grid has been made. In particular, positivity
on a real interval cannot be silently extended to those grid nodes.

Read primary statements and essential proof cases before large source
extracts. Check direction (upper versus lower remainder estimates),
degree versus original integer mass, number and placement of sample
points, all constants and exponential rates, and required separation
or endpoint restrictions. Compare stronger known results and the
C645y full-grid identity before proposing any derivation. A formula
for the remainder without a lower bound does not decide the target.

Continue only if a theorem supplies a relevant bound or leaves a
specific independently testable difference under the exact hypotheses.
Otherwise record the precise mismatch and select another mechanism;
do not reproduce the early-prefix or full-inner-input stops. Actual-Xi
layer isolation, other poles, census/clearance, simultaneous realization,
upper bounds and signs remain separate even if this synthetic bound holds.
Mathlib coverage for the prospective result has not been checked.

## What was searched and read

Queries included “multipoint Pade approximation Markov functions error
formula conjugate interpolation nodes positive measure”, “multipoint Pade
approximants Markov functions lower bound error rational interpolation”,
“multipoint Pade finite support remainder lower bounds”, “logarithmic
derivative rational interpolation lower bound”, and “Markov function
prescribed poles lower bounds finite measure”. Search hits were used as
leads; the conclusions below use primary theorem text and the indicated
proof cases. No source's publication date was inferred from a crawler date.

1. A. A. Gonchar and G. Lopez Lagomasino, *On Markov's theorem for
   multipoint Pade approximants*, Math. USSR-Sbornik 34(4) (1978),
   449--459, [DOI](https://doi.org/10.1070/SM1978v034n04ABEH001218),
   [English primary PDF](https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&option_lang=eng&paperid=2537&what=fullteng).
   Read pp.449--453, including Section 2's orthogonality, remainder (8),
   quadrature (10) and positivity discussion. The paper assumes infinite
   support on p.450, explicitly explaining that otherwise the classical
   approximant eventually equals the rational Cauchy transform. Section 2
   uses 2m interpolation nodes, plus infinity, invariant under conjugation
   and outside the support interval. Its positive weight dmu/omega and
   orthogonal denominator give the squared-denominator remainder.
   Theorem 1 gives convergence and upper-rate information for such tables,
   not the desired finite-family lower energy. This is a substantive
   finite-support qualification, not a source-access failure.

2. B. Beckermann, J. Bisch and R. Luce, *On the rational approximation
   of Markov functions, with applications to the computation of Markov
   functions of Toeplitz matrices*, [arXiv:2106.05098v2](https://arxiv.org/pdf/2106.05098v2),
   18 January 2022. Read (1.1), Theorem 2.1 and its positivity/remainder
   argument (2.2)--(2.5), and the disk case, Theorem 2.6 and
   (2.15)--(2.16). Equation (1.1) assumes infinite positive support.
   Theorem 2.1 bounds relative L-infinity error on a real set outside
   the support interval; nodes are conjugate-paired, and real even
   multiplicity defines its positive case. The proof's omega>0 is
   what allows positive orthogonality and the real extremal formula.
   Theorem 2.6 permits complex evaluation on the disk, but still requires
   conjugate-paired nodes and support to the left of -1. Its estimates
   are upper bounds. The proof explicitly says (2.4)--(2.5) do not
   survive complex evaluation; its replacement uses Cauchy--Schwarz.
   Neither theorem may be reversed to bound kappa below.

3. L. Baratchart and M. Yattselev, *Multipoint Pade approximants to complex
   Cauchy transforms with polar singularities*, J. Approx. Theory 156
   (2009), 187--211, [DOI](https://doi.org/10.1016/j.jat.2008.04.013),
   [arXiv:0804.2206v1](https://arxiv.org/pdf/0804.2206v1).
   The retrieved PDF bears 11 November 2021 on its title page while
   retaining the v1/14 April 2008 arXiv footer; citations here use its
   internal numbering. Read Section 2's BVT and admissibility definitions,
   Theorems 2.1/2.3, and the lower-bound case (3.51)--(3.53).
   Support is infinite, compact and regular; the measure has bounded
   argument variation and a lower power bound on relative balls.
   Admissibility requires node limits away from the singular support,
   finite-energy limiting distribution, and uniformly bounded argument
   derivatives of interpolation polynomials. Thus exact conjugate
   symmetry is not indispensable in this broader theorem. Theorem 2.3
   gives a 1/(2m)-root error limit in capacity for a fixed function.
   Its lower proof uses a positive-capacity subset and local mass.
   Finite atomic support fails this framework; no uniform estimate for
   our n-dependent measures follows. No claim that all complex-node
   Markov theory requires exact conjugate symmetry is intended.

4. V. I. Buslaev, *On a lower bound for the rate of convergence of
   multipoint Pade approximants of piecewise analytic functions*,
   Izv. Math. 85(3) (2021), 351--366,
   [DOI](https://doi.org/10.1070/IM9047),
   [English primary PDF](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=9047&what=fullteng).
   Read the definitions of symmetric arc sets and H0 (pp.352--353),
   Theorem 1 (p.355), Theorem 4/(6)--(10) (pp.356--357), and the
   lower-bound construction (17)--(23) (pp.361--362). Theorem 1 gives
   |f-R_m|^(1/m) -> exp(-2 G_F^alpha) in capacity, with a limiting
   node measure and an external-field-symmetric arc set whose every
   complementary component has an interior arc. The H0 hypothesis
   requires continuous nonzero boundary jump outside a capacity-zero
   exceptional set. Theorem 4's lower argument chooses an interior arc
   on which that jump is nonzero. Our rational transform has no such
   jump across an ordinary support interval away from its finite poles.
   This genuine lower-rate theorem therefore does not cover it, and
   capacity asymptotics are not uniform circle L2 constants.

5. B. Beckermann and L. Reichel, *Error estimates and evaluation of matrix
   functions via the Faber transform*, SIAM J. Numer. Anal. 47(5) (2009),
   3849--3883, [DOI](https://doi.org/10.1137/080741744),
   [author PDF](https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/bernhard_beckermann/abs/paper15.pdf)
   (PDF title: “Error estimation and evaluation ...”, retrieved
   2 November 2026). Read (1.4), Theorem 6.1/(6.1)--(6.5), and proof
   of part (c), author-PDF pp.3,22--25. This source does give a
   prescribed-denominator lower bound, so an “upper bounds only”
   characterization of the literature would be wrong. Its set E is
   compact, convex and real-axis symmetric, to the right of the real
   measure support. Prescribed exterior poles are real or conjugate-paired;
   part (c) additionally requires even multiplicity for poles lying in
   the transformed support interval. The proof uses a constant-sign
   Blaschke product and an extremal interpolation grid. It bounds a
   best uniform approximation error, not a model-space interpolant norm.
   Our complex grid has no established reduction to that geometry or
   error functional. No application or reproof is asserted.

## Exact comparison and route decision

The positive atomic measure is on the ordinates of a=x+iy. Passing to
that real coordinate does not make the interpolation table real or
conjugate-paired: every b_j=t_j u has Re(b_j)>x, so all its images
-i(b_j-x) lie strictly on one side of the real axis. This elementary
hypothesis check concerns the prescribed table; circle reflection in
B_u's denominator cannot silently be substituted for reflection in
the pole line. Adding reflected nodes would change the problem.

Also distinguish original mass M from the number of distinct atoms.
P has degree M, but P'/P has simple poles at the distinct atoms even
when residues exceed one. An asymptotic free-pole Pade remainder is
therefore the wrong object to identify with kappa. C645y instead has
a fixed-denominator rational function F^n interpolating B_u(x)L at
every grid point; (8)--(10) retain the full grid principal parts and
the common P. Its analytic interpolant norm is not automatically
either of the best-approximation errors above. These are comparisons
with existing canonical formulas, not a new remainder theorem.

Read L649 in full; C645y's hypotheses, (1)--(5), the complete rational
decomposition and identity (10), inverse Gram argument, and prefix
failure; C645n's rate statement; C645o's signed-energy statement;
L646/L648's exact-recovery/reflection stop statements; and C645x's
fractional universal-dual obstruction. Preserve those distinctions:
raw sample norms, initial prefixes, ambient inverse recovery, a
universal unit-pole dual, and a single reflected input are stopped
mechanisms. None refutes a P-dependent full-grid estimate at integer
mass <=n/3. L649 and C645y remain separately unaudited.

The new evidence stops importing an ordinary Pade/Markov lower error
as the omitted energy. It does not stop the full-grid polynomial
mechanism. The independently testable remaining difference is whether
the *entire* identity (10), with degree-M P and its permitted roots,
admits a P-dependent dual with a sufficient complete norm cost.
Merely restating that identity is not an advance. The companion
[continuation assessment](2026-11-02-full-grid-polynomial-dual.md)
records one bounded attempt for separate approval next turn. No
source-dependent generalization of the inspected theorems is approved.

## Access, unread leads, and Mathlib

The initial iupui PDF endpoint returned 502; arXiv supplied the
Baratchart--Yattselev primary text. Direct hashed MathNet PDF URLs
failed; the article pages' getFT links supplied both English papers.
Shell download lacked DNS access; web retrieval succeeded. These
access failures do not block the completed comparisons. Other search
hits on Szego/analytic-arc asymptotics and general rational Remez
estimates remain uninspected and are not inputs. Full matching Mathlib
coverage is not checked; supporting Fourier coverage is reused from
the ready angular assessment. No claim of absence is made.
