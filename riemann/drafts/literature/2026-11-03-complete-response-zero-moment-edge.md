# Source comparison: the constant spatial coefficient

TARGET: Assess source coverage for proving limsup log|G_n(u_*,0)|/n>=r(b)/2 for the unchanged fixed L666/L703 profile.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 207 searched signed complex-phase Laplace support, sampled analytic-symbol moments, rational principal-value Poisson and BV jump versions; compared the exact local inverses and scalar/origin/highest-moment stops. No matching complete zero-moment rate theorem was found in this bounded search; queries and inspected sources are recorded below, with no novelty inference.
SOURCE_EVIDENCE: Liflyand--Stadtmueller (2014), Lemma 1.1 and Theorem 2.1, complete d=1 proof pp.491--495; NIST DLMF v1.2.8, (1.8.14)--(1.8.15), (1.14.3); reused the precise primary analytic-symbol, support/germ and polynomial-Jensen readings identified below. New sources cover conditional summation and midpoint values, not TARGET's exponential estimate.
COMPARISON: L714 already supplies the exact inverse g_n of W_n and its relation to p_n; L719--L721 supply a concrete analytic-symbol/support-edge mechanism for p_n, while L723's complete correction proof is for z=-1. Removing the resolvent changes the kernel's decay and origin continuity, so neither that correction proof nor the signed rate transfers by citation. The BV results provide the missing summation tools but no uniform-in-n payment.
GAP: Verify an elliptic factorial expansion or equivalent exact support-edge realization for the zero-moment kernel, then identify and bound its complete comb/origin/remote-frequency/paired-tail contribution on a common allowed subsequence. No zero-moment lower rate, eventual nonvanishing or noncancellation is established.
REASON: Essential tool coverage is adequate for one bounded test of the unchanged coefficient; remaining issues are mathematical applicability and estimates rather than an inaccessible source. EXPLORE supplies a test, not an imported rate. The newly written continuation is subject to separate supervisor approval; this literature turn derives no result and changes no lemma or script.
LITERATURE_REASON: The zero spatial moment removes [1-(-a/R)^M]/(R+a) from L723; the ready assessment is restricted to z=-1 and does not cover signed support-edge noncancellation for the resulting sum of W_a.
SCOPE: Original fixed actual L703/L708 profile and full L666 response, n=12q+3, M=n/3, u_*=(3+4i)/10, fixed chi, 0<delta<1/3000, b=sup supp chi and r(b)>1/200. No profile replacement, angular-circle conclusion, positive-residue premise for complex W_a, or generic boundary-to-center transfer is authorized.
COVERED_TARGET: Test whether limsup log|G_n(u_*,0)|/n>=r(b)/2 for the unchanged fixed L666/L703 profile, retaining the origin term and both finite tails.

The sections preceding the completed comparison preserve step 206's
nomination and its then-pending review status. Step 207 resolves the
source gate only within the scope stated above; the proposed bound
remains unproved.

## Exact question and potential use

The main gap is actual-Xi all-degree mixed positivity. The proposed
intermediate question, for a later source-gated attempt, is

    limsup_(q->infinity) log|G_(12q+3)(u_*,0)|/(12q+3)
                                                   >= r(b)/2.

Here G_n(u,0)=R^(-1)*sum_(a in Z_n) W_a(u) is the existing
constant coefficient, with exactly L666's original weights, masses,
anchor, inverse angle, j=0 factor and endpoints. It is not a new
response or a truncation of the downstream spatial polynomial. The
profile remains the one in L723. No nonzero value or positive rate
at this particular angular point is assumed.

A successful rate could feed the existing polynomial Jensen comparison
to give a spatial logarithmic lower bound at u_*. The review must
check that interface for nonzero evaluations on the selected subsequence.
Full angular accounting, required charge, H/support, Xi realization
and actual-Xi signs remain open. This would not turn L724's tiny arc
into full-circle payment.

## Distinction from existing work and preserved stops

The accepted L724 proof needs no further audit merely because the next
question is uncovered. Its angular disk and zero-factor argument do not
compare spatial arguments. Generic polynomials can have large boundary
values and small or zero constant coefficients. The question must use
the exact signed weights and profile, not L723's peak alone.

The prospective mechanism is to inspect the signed zero-moment transform
and its sampled generating germ directly. The spatial resolvent factor
is absent, so L723's nonremovable singularity cannot be assumed to
survive. The review should distinguish a matching standard theorem,
routine specialization of the kernel analysis, and a genuinely different
noncancellation problem. No new transform formula or asymptotic is
derived here.

Reuse the readings in `2026-11-03-complete-response-support-germ-scope.md`,
`2026-11-03-complete-response-angular-log-propagation.md` and
`2026-11-03-centered-gap-scalar-complete-log-lower.md` only within their
actual hypotheses. The last assessment's full-circle scalar target
uses L696's centered-gap profile, not this fixed L703 profile. The
exterior-anchor coefficient relaxation, absolute-contour and two-arc
completion stops retain their stated scopes. L712 stops B_sp=o(n),
not this scalar question. No absolute envelope, growing-degree Jensen
cost, sampled array or assumed eventual nonvanishing replaces the
signed coefficient estimate. The scoped local comparison is not a
completed literature assessment or evidence of novelty. No
cross-notebook input is proposed.

## Discriminating review and routing

Identify a matching theorem with checked hypotheses, precise coverage
for one bounded test of the displayed rate, or a specific obstruction.
The later mathematical test must give a subsequential rate at least
r(b)/2 or quantify an informative deficit. Scalar nonidentity, the
z=-1 peak, a norm upper bound or unpaid O(n) loss does not suffice.
Essential unresolved assumptions are zero-moment support-edge survival,
cancellation with the complete finite correction, and control of the
relevant generating germ.

Immediate routing is literature_comparison, standard/high. A creative
attempt is not yet justified by source coverage. After review, route a
genuinely new mechanism as creative with a bounded test; route routine
specialization according to its actual difficulty. Do not label it
creative to satisfy scheduling. Full matching Mathlib coverage is
unchecked. This nomination neither spends a mathematical exploration
attempt nor resets any prior stop.

## Completed source comparison — 3 November 2026, step 207

### Exact local interfaces, duplicates and recorded failures

Read L666's definitions, conclusions and Section 4; L703's hypotheses,
conclusion and cited construction interface; L708's hypotheses and
real-frequency prescription; L714's hypotheses, (1)--(5) and Section 2;
L719--L720's exact-kernel and analytic-symbol statements; L721's
hypotheses and Sections 1--4; and L723's exact finite identity,
real-physical product bounds, density bounds and complete correction
proof. The accepted audits are reused, not performed again. L724's
accepted audit and unchanged scope are supplied startup evidence.

L714 (5) already defines g_n, the inverse density of W_n itself,
supported on the positive half-line. Its Section 2 records finite
exponential formulas, finite variation measures, finite first absolute
moment, the transform convention, and the derivative relation between
p_n and g_n on v>0. These are established local inputs, not new formulas
derived in this review. L714 explicitly distinguishes nonvanishing of
g_n from noncancellation after bump integration. Its density has a nonzero
right-hand limit at v=0, whereas its extension to v<0 is zero; the
point value at zero does not determine the transform. L723's p_n instead
has a continuous gluing at zero. No value may be silently transferred
between these conventions.

L723 Section 2, (8), gives W_n only a 1/|y| tail factor, while its
resolvent-weighted physical kernel has a 1/y^2 factor. Its absolutely
convergent comb and separately absolute physical-tail argument therefore
do not cover W_n by deletion of the resolvent. The full zero-moment
coefficient is a finite sum and is well-defined; any introduced infinite
sum must state its summation prescription and recover precisely the
original endpoints. One-sided divergent sums may not be subtracted.
This is a hypothesis mismatch in an existing proof, not a new theorem
that the requested estimate fails.

L719--L720 prove the factorial expansion for the exact p_n on fixed
complex neighborhoods, at all orders up to epsilon*n. Their existing
contour, phase and uniform product estimates are relevant reusable
inputs. They do not state that expansion for g_n. L721 Sections 2--4
use the full factorial remainder and a nonvanishing leading amplitude
to build a fixed triangular operator and the sampled Cauchy germ;
scalar nonvanishing or a fixed-order O(1/n) estimate cannot replace
those hypotheses. The unchanged phase geometry is already available,
but its use with a changed amplitude and exact remainder must be checked.

The scoped comparisons preserve these stops:

- The centered-gap scalar assessment and step-129 failure concern a
  whole angular-circle mean for an L696 profile; the real-residue
  interlacing payment is unresolved. They do not decide this fixed
  angular value for the actual L703 profile.
- `ATTEMPTS/2026-11-03-low-moment-origin-closure-overlap.md` concerns
  angular evaluation at u=0 and the C645p pole-clearing cost. Our
  spatial argument is zero but angular argument is u_*; that stop is
  not a theorem about this observable.
- `ATTEMPTS/2026-11-03-highest-spatial-moment-stop.md` concerns the
  highest moment and its zero-displacement countersequence, not the
  unchanged fixed prescribed profile's constant coefficient.
- The complete-response support/germ assessment retains the absolute
  contour, common-phase, gamma/Rice and remainder-subordination stops.
  None supplies cancellation information for the present coefficient.
  Do not restart those mechanisms under a new name.

L666's polynomial Jensen comparison is the prospective downstream use:
at any specified angular parameter where the polynomial is defined
and its constant coefficient is nonzero, the spatial logarithmic mean
has that coefficient as a lower comparison. The cited root formula
allows boundary roots, multiplicities and actual degree drops. This
does not move u_* to an angular circle or pay a complementary mean.
The desired positive-rate subsequence would have to be proved first.

### New primary statements and essential proof cases

E. Liflyand and U. Stadtmueller, *Poisson summation for functions of
bounded variation on R^d*, Acta Sci. Math. (Szeged) **80** (2014),
491--498, DOI 10.14232/actasm-013-518-5,
[publisher PDF](https://acta.hu/download.phtml?id=3276).
Read Lemma 1.1, pp.491--492, Theorem 2.1 and its complete d=1 proof,
pp.493--495. For BV f tending to zero at both infinities, integer
values are midpoint limits and nonzero modulation x modulo 2*pi is
required. The identity compares the modulated samples with transform
samples at 2*pi*k-x. The proof uses symmetric partial sums, Dirichlet
convergence away from zero, a BV series/integral bound, Stieltjes
integration, a summable remainder and dominated sine-series convergence;
Fourier inversion finishes it. No multidimensional extension is used.
It supplies a conditional-sum tool, not a bound uniform in n. Applying
it here requires a correct scaling/modulation and verification of BV,
midpoint conventions and the exact finite endpoint recovery. No
specialized lattice identity is established by this review.

NIST DLMF **v1.2.8** (release 15 September 2026),
[1.8(iv), (1.8.14)--(1.8.15)](https://dlmf.nist.gov/1.8.iv):
read both statements and their immediate hypotheses. The two-sided
formula assumes C^2 regularity and integrability of f and |f''|.
The half-line formula assumes continuity, BV, integrability and decay
to zero, and retains half the origin value. Neither grants the
shifted-comb specialization or an n-uniform remainder. General proofs
are not reconstructed; the complete BV proof above supplies the
summation case needed for comparison.

NIST DLMF **v1.2.8**,
[1.14(i), (1.14.3)](https://dlmf.nist.gov/1.14.E3):
read the inversion statement, convention and principal-value
qualification. Absolute integrability of f and local BV at u give
the average of its two one-sided values through principal-value
inversion. A continuous-density value cannot replace this average
at a jump. The future application must track Fourier sign, scale h
and normalization. This theorem does not supply a signed lower bound.

### Reused coverage and its limits

Reuse `2026-11-03-signed-bump-analytic-symbol.md`, completed comparison:
Hitrik--Sjostrand, *Two Minicourses on Analytic Microlocal Analysis*,
[arXiv:1508.00649v1](https://arxiv.org/pdf/1508.00649v1), Section 2.2,
(2.2.1), pp.32--33; Section 2.3, Theorems 2.3.1/2.3.3, Lemma 2.3.2
and deformation/Morse proof pp.37--40. The analytic Gaussian theorem's
factorial estimates, common domains and full complementary contour
control matter here. It is not a theorem for the changed array without
checking those hypotheses. Reuse L720's precise applicability work
where unchanged; do not reprove the general stationary-phase theorem.

Reuse `2026-11-03-signed-bump-support-edge-transfer.md`, its primary
analytic ellipticity, support and real-coordinate sampled-Laplace
comparisons, and `2026-11-03-complete-response-support-germ-scope.md`
for Poisson and germ identification. In particular the fixed
real-coordinate Laplace support theorem is not an automatic import
for a complex phase with size-dependent amplitude. An analytic FIO's
forward wavefront inclusion cannot be reversed without its inverse
and actual operator hypotheses. L721 supplies a concrete alternative
construction for p_n; extending it is a mathematical task.

Reuse `2026-11-03-centered-gap-scalar-complete-log-lower.md` for
Brunault--Zudilin, *Many Variations of Mahler Measures*, Propositions
1.4--1.5, pp.6--7, including all root cases and rational qualifications.
This supplies only the Jensen interface, not the scalar coefficient
estimate. The generating-series radius and analytic-error tools are
already covered by the complete-response assessment and L721/L723;
no new singularity-transfer asymptotic is needed merely for a limsup.
Mathlib coverage of the full target remains unchecked; no absence
claim follows. No cross-notebook theorem is used.

### Bounded search record

Queries included `"Poisson summation" "jump" "symmetric" bounded
variation`, `"Poisson summation" "rational" "1/x" principal value`,
`"Laplace" "support" "complex phase" "moments" cancellation`,
`"sampled" "support" "analytic symbol" generating function`,
`"signed" "support" "Laplace" "complex curve" moments theorem`,
`"G_n" "zero moment" "support edge"`, and exact author/title searches
for BV Poisson. No matching coefficient theorem was located. The
publisher BV paper and DLMF statements above were inspected; search
snippets, Wikipedia, aggregators and unrelated examples are not inputs.
Rahman--Schmeisser's 1994 Poisson/Plana paper was a discovered primary
lead, but its full proof was not inspected and it is not imported.
The sufficient BV source was accessible, so no persistent source
blocker remains. The bounded search does not establish novelty.

### One permitted mathematical test and decision rule

The COVERED_TARGET is the unchanged displayed rate at n=12q+3; no
calculation or proof of it occurs here. Start from the original finite
coefficient and L714's established g_n. Test its analytic-symbol
hypotheses using the exact finite formula and/or L714's recorded
derivative relation on a smaller fixed complex neighborhood of I.
Any differentiation of an asymptotic remainder needs a common
holomorphic domain and uniform Cauchy control. Determine the actual
leading amplitude and its nonvanishing; do not assume that deleting
a resolvent preserves it. Retain the entire kernel and exponential
remainder before applying the L721-type fixed-density/germ test.

At the same time the complete coefficient must be identified with
the exact signed bump plus its actual origin, comb, remote-frequency
and finite-tail terms. The new BV sources permit checking symmetric
summation or an equivalent justified regularization, not erasing the
zero-frequency contribution. Retain the original paired endpoints
-2q<=m<2q and the original shifts, with their fixed summability and
cap. The z=-1 finite geometric correction is not a formula for this
coefficient: do not substitute into L723's identity or discard a term
without an exact zero-moment identity. All M moments remain in the
downstream full spatial polynomial.

Continue if a checked complete representation yields an unbounded
subsequence with rate at least r(b)/2. A stronger edge rate is useful
only if its complete correction cannot cancel it on that same
subsequence. A proved cancellation or an upper rate strictly below
r(b)/2 is an informative negative. If the effort produces only the
old boundary peak, scalar nonidentity, a norm bound, a fixed-order
expansion or an unpaid O(n) charge, record the precise unmet obligation
and stop the unchanged attempt. No eventual nonvanishing, positivity
of complex densities, endpoint law for chi or profile substitution is
allowed. Full angular payment, spatial/global charge, H/support,
Xi realization and actual-Xi mixed signs remain independent gaps.

This is difficult development of the existing exact-kernel mechanism,
not a justified creative mechanism at the central RH gap. The absence
of a covered new realization/positivity mechanism blocks a protected
creative attempt in this step; the scheduling preference does not
justify relabeling this specialization. Recommend proof_attempt with
development purpose, deep_research/xhigh, after separate approval of
this newly written continuation. No mathematical exploration budget
is reset by this literature-only review.
