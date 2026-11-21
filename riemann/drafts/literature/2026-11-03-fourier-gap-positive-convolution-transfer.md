# Source review: a positive-convolution transfer of an anchored Fourier gap

TARGET: Assess exponential decay of L666's c_0(1) from a fixed summable anchored Fourier gap centered at omega_*, using a positive-convolution kernel with finite endpoints retained.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 116 searched rational characteristic-function mixtures, convolution concentration, spectral-gap rational sampling and finite summable lattice truncation; retrieved primary probability and distribution sources and checked the specific local comparisons below. No inspected theorem states the exact scalar estimate; this bounded search establishes neither novelty nor impossibility.
SOURCE_EVIDENCE: Durrett, Probability: Theory and Examples, version 5 (11 January 2019), Thms 3.3.1--3.3.2 p.126, Example 3.3.8 and Lemma 3.3.9 p.128; Vershynin, High-Dimensional Probability, first-edition author version (20 May 2024), Prop.2.7.1 pp.31--33, Definition 2.7.5 p.33, Example 2.7.8 p.34, Thm 2.8.1 and proof pp.36--37; Miller, Some notes on distributions (15 January 2006), Thms 4.1--4.2 and Section 6 pp.7--9; Lev arXiv:2007.09930v3 Section 4.10 and Lemma 3.3 with full proofs. Reuse the prior Lev/l1 assessments for L694; direct links and reading limits below.
COMPARISON: Mixture/product rules and Bernstein concentration are known inputs, but do not themselves pair the exact rational kernel with an infinite counting measure or pay truncation. Lev permits prescriptions in any fixed admissible annulus; L694 states only an existential gap at its selected center. Its center replacement and scalar transfer remain proof differences. L690 and L695 do not settle this signed scalar question.
GAP: Verify the prescribed center with L694's l1 construction and cap, the exact positive-convolution identity and frequency scale, a justified rational pairing or regularization with quantitative error, and exponentially paid finite endpoints. No matching finite theorem is imported; none of these new conclusions is proved in this literature turn.
REASON: Essential comparison is complete for one bounded finite scalar proof attempt under the exact saved target, using named standard inputs rather than reproving their general theorems. EXPLORE approves investigation of the identified difference, not its truth. No persistent essential source blocker remains.
LITERATURE_REASON: The proposed rational characteristic-kernel and concentration mechanism, prescribed gap center and non-Schwartz Fourier pairing are outside the completed head-tail assessment's inspected sources.
SCOPE: The exact TARGET and scalar formula below, with fixed real l1 shifts, cap 1/8, anchor, unit masses, n=12q+3, all j including 0, u=1 and finite endpoints retained. Center specialization may be tested from L694's existing proof; conditional transfer must label centered-gap existence separately until established. No angular interval, spatial-moment or logarithmic bound is preapproved.

The completed comparison below supersedes the pending-review language
in the original proposal retained next. That proposal states targets
and obligations, not established mathematical assertions.

## Exact proposed target and hypotheses to assess

Keep L666's x=-d=-5/4, U=121/64, R=11/8, n=12q+3,
h=27/(10n), all j=0,...,n-1 factors and denominator angle 1/u.
The fixed sequence is real, in l1(Z), and has sup norm <=1/8.
The real counting measure is

    mu=delta_0+sum_(m in Z) delta_(m+1/2+e_m),
    F_ang(mu)(omega)=integral exp(-i*omega*s) dmu(s)

in the tempered-distribution sense. Define the proposed center

    omega_*=(27/10)*integral_0^1
                         [(d+t)^(-1)-t/(U+d*t)] dt.

The source comparison must determine whether the already inspected
prescription method provides the same cap and summability with a gap
on some fixed open neighborhood of this particular omega_*. L694's
existential gap is not silently assumed to have the required center.
A conditional transfer under an explicitly assumed centered gap can
be a useful intermediate target, provided that existence remains open
and the statement does not hide the desired finite estimate as a premise.

For the actual finite family the scalar target is

    c_(0,n)(1)=R^(-1)*[1+sum_(-2q<=m<2q)
                       W_(x+i*h*(m+1/2+e_m))(1)],
    |c_(0,n)(1)|<=C*exp(-c*n)

for some C,c>0 and one onset, allowed to depend on the fixed profile
and gap, not on n. This is a proposed upper bound at one angle, not
a complete logarithmic or signed-energy conclusion.

One candidate factorization to verify in the source review/approved
attempt is the product of ratios

    (1-i*alpha_j*y)/(1-i*beta_j*y),
    alpha_j=t_j/(U+d*t_j), beta_j=1/(d+t_j).

The proposed interpretation is a convolution of positive probability
kernels, whose frequency concentrates near omega_* after the h scaling.
No such representation or concentration estimate is imported or proved
by this pending note. If it is a standard known result, cite it and
check the actual hypotheses rather than reprove it as a discovery.

Distributional cancellation requires a valid test function. The
unmodified rational weight and its frequency kernel cannot be assumed
Schwartz, and the finite endpoints at m=-2q and 2q-1 must be paid.
An infinite formal sum, an unproved Poisson interchange or a generic
large-deviation statement with no endpoint bound does not establish
the target. The j=0 factor and fixed anchor must survive every step.

## Relevance and bounded decision

Main gap: actual-Xi all-degree mixed positivity. The nearer unresolved
issue is whether an infinite anchored Fourier gap has a useful finite
rational consequence. This scalar target is independently testable and
introduces positive convolution in place of the stopped absolute tail
estimate. It could justify a later investigation of all moments and an
angular interval; it does not supply either of them. Even a successful
scalar estimate would not refute A_n(e)>=A_n(0)-o(n), prove a full-cube
bound, settle H/support or realize Xi data.

Compare primary results on rational characteristic functions and
convolution concentration, as well as the exact Lev prescription and
finite summation/pairing cases. Reuse the existing Lev source material;
do not reopen unchanged general Mahler continuity. Continue only with
an applicable import or an explicitly source-assessed finite estimate.
Park this target if the center cannot be supplied or essential pairing
or endpoint control stays blocked; do not replace an exponential rate
by unquantified distributional convergence.

Essential local references for that review are L666's exact product,
L694's audited prescription, L690's baseline qualification, and L695's
fixed-profile stop. L657 remains the complete-charge standard for any
later logarithmic conclusion. Full matching Mathlib coverage is unchecked.

## Completed comparison — 3 November 2026, step 116

### Primary inputs and exact reading limits

Rick Durrett, *Probability: Theory and Examples*, version 5,
11 January 2019, [author PDF](https://math.duke.edu/~rtd/PTE/PTE5_011119.pdf),
printed pp.126,128 (PDF pp.134,136). Read Theorems 3.3.1--3.3.2
and their proofs, Example 3.3.8 and its integral, and Lemma 3.3.9.
Independent real random variables have product characteristic functions;
finite convex mixtures have the corresponding convex combination.
The rate-one exponential has characteristic function (1-i*t)^(-1)
in the source's positive-exponent convention. Scaling is Theorem
3.3.1(e). These imports support testing the proposed ratios; they do
not identify them with L666's W. Check coefficient signs, mixture
weights, the j=0 factor and Fourier reflection before using them.
No general characteristic-function theorem needs reproving.

Roman Vershynin, *High-Dimensional Probability*, first-edition author
version dated 20 May 2024,
[author PDF](https://webapps.math.uci.edu/~rvershyn/papers/HDP-book/HDP-1.pdf),
Theorem 2.8.1, printed pp.36--37 (PDF pp.44--45): for independent,
mean-zero, sub-exponential real X_j and t>=0,

    P(|sum_j X_j|>=t)
      <=2 exp[-c min(t^2/sum_j ||X_j||_(psi1)^2,
                         t/max_j ||X_j||_(psi1))],

where c>0 is absolute. Identical laws are not required. Read the full
proof: exponential Markov bound, independent product, admissible MGF
range, constrained optimization and reflected tail. Also read
Proposition 2.7.1's statement and displayed proof cases, Definition
2.7.5 and Example 2.7.8 (pp.31--34); centering is Exercise 2.7.10
(p.35), not a proved matching application in the source. This is a
tail-probability bound, not a density-derivative or distribution-pairing
estimate. The actual family still requires verified uniform centered
norms, mean, scaling and a fixed margin inside the gap. No rate for
our scalar is inferred here. The first edition is cited deliberately;
the second edition was not used.

Stephen D. Miller, *Some notes on distributions*, 15 January 2006,
[author notes](https://sites.math.rutgers.edu/~sdmiller/musagei/distributions.pdf),
Section 4, Theorems 4.1--4.2 and proofs, and Section 6,
PDF pp.6--9. Poisson summation is proved for Schwartz functions by
absolute periodization and Fourier expansion. The Fourier-duality
definition (6.1) tests a tempered distribution on Schwartz functions;
(6.2) is the Dirac-comb identity. These inputs justify smooth compactly
supported frequency tests, not direct substitution of an arbitrary
rational weight. No broader Poisson theorem is claimed from these
notes. A non-Schwartz extension needs its own convergence proof.

Nir Lev, *An example concerning Fourier analytic criteria for
translational tiling*, RMI **38** (2022), DOI
[10.4171/RMI/1318](https://doi.org/10.4171/RMI/1318),
[arXiv:2007.09930v3](https://arxiv.org/html/2007.09930v3#S4.SS10),
27 September 2021. Reused the earlier prescription and l1 comparisons;
reinspected Theorem 4.8 and its full Section 4.10 proof for the changed
center. It permits fixed 0<a<b<1/2 and small Hermitian prescriptions
in the two annuli. It does not state an anchored l1 theorem at omega_*.
Read Lemma 3.3's full proof (Section 3.3): it requires h in L1,
compact spectral support in (-b,b), and its local pseudomeasure
identity. Smoothing, Wiener convergence and bounded-density summation
are checked. It cannot simply be invoked for our rational W.
Section 3.1's spectral-synthesis warning was inspected as context;
Malliavin's original theorem was not independently read or imported.

### Source-assessed finite test, still unproved

Keep the exact original scalar target. First check whether replacing
L694's c=1/4 by c=omega_*/(2*pi), with an appropriately chosen fixed
annulus and narrow cutoff, meets every smallness, Hermitian, l1 and
unit-mass hypothesis of that existing construction. This is a proposed
specialization, not a conclusion of this review. A conditional scalar
theorem may assume a centered open gap explicitly; it must not claim
that L694's stated existential interval is centered there.

For the scalar transfer, verify the exact factorization proposed above
before importing the mixture/product rules. Identify the resulting
scaled frequency law and its mean. Import Bernstein only after
checking its actual hypotheses. Probability mass outside the gap
is not by itself a bound for an arbitrary tempered-distribution
pairing: the test and the necessary norm must be identified.

One available local input is L694's signed-interval primitive F in L1,
with F'=delta_Z-delta_Lambda and ||F||1<=sum |e_m|, followed by its
explicit half-translation and anchor. A later proof may test whether
this primitive permits integration by parts and Fubini with the exact
rational kernel, or use a smooth cutoff with all errors quantified.
This is a proposed way to discharge the pairing obligation, not a
new extension theorem. Neither smoothness nor an unrestricted pairing
is assumed. Track all 2*pi factors and Fourier signs.

Finally, separately bound the discrepancy between the justified infinite
pairing and the exact finite indices -2q<=m<2q. Both endpoints, anchor,
and j=0 must survive. A formal infinite cancellation, a qualitative
distributional limit, or only a fixed-index tail estimate fails the
test. Required evidence is C*exp(-c*n), with c>0 and C and onset
independent of n for the fixed profile/gap, after every endpoint and
regularization error. No particular value of c is asserted or needed.

Continue only if these checks yield that rate or a precise informative
obstruction. If the centered construction fails, keep any conditional
transfer qualified; if pairing or endpoints fail, preserve that exact
failure and park the dependent branch. Do not weaken the target to
unquantified cancellation. A successful u=1 bound still leaves angular
intervals, all M moments, signed logarithms, L657's complete charges,
H/support, actual-Xi realization and all-degree positivity open.

This is an EXPLORE decision because the inspected standard tools do
not state the finite transfer. A later successful application is not
to be reported as a new general concentration or Fourier theorem.
Full matching Mathlib coverage was not checked; that is not evidence
of absence and is not an essential source blocker for this test.

### Search, overlap and access record

Executed queries included `characteristic function ratio (1 i a t)
(1 i b t) mixture exponential atom convolution concentration Chernoff`;
`Chernoff 1952 measure asymptotic efficiency tests hypothesis pdf
theorem`; `Fourier transform tempered distribution spectral gap test
functions non Schwartz finite measure Poisson summation rational
function`; `Vershynin high dimensional probability pdf Theorem 2.8.1
Bernstein inequality sub exponential`; `"Fourier gap" "rational"
"perturbations" lattice`; `"spectral gap" "convolution" "counting
measure" exponential`; `"spectral gap" "rational functions" "measure"
exponential`; `"Fourier gap" "finite" "summable" lattice convolution`;
and `"positive convolution" "spectral gap" "truncation"`. Author-site
queries then located the exact probability PDFs. Many hits concerned
operator spectral gaps, not frequency gaps; none supplies the target.
Chernoff's 1952 paper was located but not read at theorem level and
is not an input. The accessible non-iid Bernstein theorem suffices.
Initial UCI host fetches failed; its author webapps mirror resolved
access. Duke's author PDF and Miller's notes were accessible. No
repeated access turn is required.

Local duplicate/failure checks used only L666's relevant product,
L694's stated/audited scope and anchored prescription, L690/L695's
qualifications, the existing anchored/summable/nonuniform-kernel
assessments, and the signed-canonical/absolute-tail attempt records.
L695's full angular/spatial absolute-tail lower bound does not supply
a signed scalar obstruction at u=1. L690's common-displacement
baseline does not prescribe an anchored gap. Step 105's uncertified
finite optimization remains parked. No cross-notebook input, new
lemma, mathematical script or mathematical calculation was used.
