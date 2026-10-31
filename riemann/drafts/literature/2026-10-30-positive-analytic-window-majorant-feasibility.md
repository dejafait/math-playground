# Analytic-majorant feasibility: completed source comparison

TARGET: Review whether a nonnegative band-limited analytic majorant of the off-line mesoscopic rectangle can have a Bettin--Fazzari k=1 main term of O(delta log T exp(-c delta log T)) at delta=log log T/log T.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded exact-class, positive-harmonic-strip and Beurling--Selberg searches; inspected Axler--Bourdon--Ramey Theorem 3.4/(3.5) and proof, and Carneiro--Chandee--Littmann--Milinovich Corollary 14 and admissibility definition. Reused the existing arithmetic assessment and local failure records; queries and source scope below.
SOURCE_EVIDENCE: Axler--Bourdon--Ramey, Harmonic Function Theory, second edition, author PDF dated 17 July 2020, Theorem 3.4 and (3.5), printed pp. 47--48, https://axler.net/HFT.pdf#page=54; Carneiro--Chandee--Littmann--Milinovich arXiv:1406.5462v1, Section 1.1 and Corollary 14, pp. 2 and 24, https://arxiv.org/pdf/1406.5462v1; Bettin--Fazzari arithmetic coverage is reused, with a targeted coordinate/growth check described below.
COMPARISON: Harnack supplies uniform interior value comparisons for the real part of an analytic test, independently of its Fourier support. The same-kernel extremal result uses real-axis positivity and support [-1,1], not this off-axis rectangle or arbitrary fixed R. Neither source is cited as the proposed detector's quantitative impossibility theorem.
GAP: Specialize the disk inequality to the moving strip and integrate against K to test a uniform lower bound c_* log T. The geometry, constants and comparison with the requested upper scale remain unwritten mathematics. Moving-test arithmetic errors and height-weight transfer are still independent gaps.
REASON: Essential coverage for one necessary-bound test is now available. A construction is not the next justified task: first test the cost imposed by nonnegative harmonicity. This is a standard-source specialization, not a novelty claim or an obstruction already proved.
SCOPE: Source review of precisely the entire-test class below. The separately saved quantitative continuation uses only the cited Harnack inequality and elementary kernel estimates; no RH, simplicity, spacing, external half-plane premise or weighted zero moment is assumed.
LITERATURE_REASON: The new requirement is positivity of Re f on the full complex zero strip, which was outside the existing exact-amplitude and Green assessments; only that essential geometric coverage and its primary comparisons were refreshed.

## Exact proposed feasibility question

Put L=log T, delta=log L/L and

    B_T=L/(4pi), a_T=delta L/pi, b_T=delta L/(4pi),
    K(x)=1-(sin(pi x)/(pi x))^2, with K(0)=0.

Determine source coverage for the existence, for every sufficiently
large real T, of an even entire f_T, real on the real axis, whose
Fourier transform is C-infinity and supported in [-R,R] for some
fixed R>0, with

    Re f_T(x+iy)>=0          for all real x and |y|<B_T,
    Re f_T(x+iy)>=1          for |x|<=a_T and b_T<|y|<B_T,
    integral_R f_T(x)K(x)dx <= C delta L exp(-c delta L),

where C,c>0 are fixed independently of T. The Fourier convention is
f_T(z)=integral hat(f_T)(u) exp(2pi i u z)du. These are proposed
requirements, not an asserted construction, implication or lower bound.
The main term K is the real-axis k=1 kernel recorded in the existing
source assessment. The primary complex-zero convention agrees with this
geometry; the reflection and fixed-test qualifications are recorded below.

The dimensions correspond to the intended closed ordinate window
|gamma-t|<=2delta and strict displacement beta>1/2+delta/2, using
the source coordinate ((gamma-t)+i(1/2-beta))L/(2pi). Requiring
nonnegativity on the whole zero strip prevents compensating negative
contributions from unselected zeros. This is a prospective sufficient
detector class; its failure would not rule out signed analytic detectors
or the weighted-count target itself.

The source comparison below replaces the nomination's unread geometric
leads. No theorem for the exact optimized detector class was identified
in this bounded search; no novelty claim follows.

## Relevance and bounded decision

A feasible majorant with a sufficiently small main term could make
the known exact-amplitude analytic statistic relevant to the positive
off-line count. Uniform errors for a T-dependent test, smooth-to-sharp
height transfer, kernel transfer, other scales and individual Xi signs
would still be independent gaps. Neither source fixed-test asymptotics
nor a positive real-axis kernel settles those issues.

Continue only with primary coverage that permits one discriminating
construction or necessary-bound test for the stated detector class.
If an applicable known theorem already rules out its main-term scale,
import that obstruction and park this class. If essential coverage is
missing, keep REVIEW_REQUIRED or SOURCE_BLOCKED; do not derive and
approve an uncovered theorem in the same turn.

L018 supplies actual-zero coordinates and multiplicities for a later
application. L501 is an unaudited diagnostic reason for changing the
test, not a load-bearing theorem in this geometric question. L485 and
ordinary zeta moments are not assumed to bound selected amplitudes.
No cross-notebook input is needed. Full Mathlib coverage is unchecked.

## Search and local overlap checked

Queries on 2026-10-30 included:

- `Axler Bourdon Ramey Harmonic Function Theory Harnack inequality 3.1 pdf`;
- `nonnegative real part entire function strip bandlimited majorant Harnack inequality`;
- `"positive harmonic" "strip" "integral" Harnack`;
- `"Beurling" "Selberg" "majorant" "complex" strip positivity`;
- `Littmann "Entire majorants via Euler" pdf`.

The last query surfaced the exact pair-correlation kernel extremal paper
below, which was then inspected directly. Search snippets were discovery
aids only. Littmann's Euler--Maclaurin paper, Mugler's completely-convex
strip representation, and Rippon--Stallard's annular application remain
unimported leads; their theorems are unnecessary for the selected disk test.

A scoped search for Harnack/positive-harmonic/strip-positivity coverage in
local literature assessments, foundations, attempts and today's history
found only this nomination. The exact-weight assessment's source
discussion (file lines 95--110), and both detector and Green stop
records, were inspected. L500's selected two-height correlations and
L501's nonharmonic covariance are different obstructions. They supply no
proof of failure for this class and are not inputs to the proposed test.

## Primary geometric input inspected

S. Axler, P. Bourdon and W. Ramey, *Harmonic Function Theory*, second
edition (Springer, 2001), [author PDF dated 17 July 2020](https://axler.net/HFT.pdf#page=54),
Theorem 3.4, printed p. 47, and (3.5), p. 48:
for positive harmonic u on the open disk D(a,r), dimension two, and
|z-a|<=s<r,

    (r-s)/(r+s) u(a) <= u(z) <= (r+s)/(r-s) u(a).

Read the complete proof on p. 47: Poisson-kernel bounds first treat a
neighborhood of the closed disk; dilation and a limit treat an open disk.
Equation (3.5) explicitly allows translation and dilation. Thus no strip
boundary values, uniform global bound or boundary integrability are
needed. For weak positivity the specialization must address u+epsilon
and its limit. The analytic real part is the applicable harmonic function;
the source theorem itself is imported, not reproved. No detector integral
bound is derived here.

The exact remaining specialization is to choose disks inside |Im z|<B_T,
compare one point in the required rectangle with a real interval whose
length is proportional to B_T, and bound the K-weighted integral. Whether
this yields a common positive c_* is the next mathematical test. Its
support-independent formulation avoids an unproved Fourier optimization.

## Primary band-limited comparison inspected

E. Carneiro, V. Chandee, F. Littmann and M. B. Milinovich,
*Hilbert spaces and the pair correlation of zeros of the Riemann
zeta-function*, [arXiv:1406.5462v1](https://arxiv.org/pdf/1406.5462v1),
Section 1.1 p. 2, (1.6), and Corollary 14/Section 3.5 p. 24:
an admissible R is integrable on the real axis with Fourier support
[-1,1]. If R>=0 there and R(0)>=1, then

    integral_R R(x)K(x)dx >= 2^(-1/2)cot(2^(-1/2))-1/2.

This analytic inequality does not assume RH; the zero-pair application
of Montgomery's formula (1.5) does. Read the corollary's factorization
and reproducing-kernel proof. Also inspected the real-axis extremal
constraints (1.29)--(1.31), pp. 9--10, and Theorem 5's statement. They
do not assert positivity of the real part throughout a complex strip.
Our class permits any fixed R and imposes off-axis values, so Corollary
14 is a comparison, not a direct import of the desired conclusion.
No rescaling or complex-point extremal inequality is inferred here.

## Reused arithmetic input and coordinate applicability

The completed assessment
`drafts/literature/2026-10-30-zeta-squared-weighted-local-density.md`
remains the arithmetic review. A targeted reinspection of
[Bettin--Fazzari v1](https://arxiv.org/pdf/2208.08421v1), p. 1 footnote,
Theorem 1.2 p. 3, and Section 2.1 p. 6, confirms: the source writes
rho=1/2+i gamma with gamma possibly complex; k=1 has no fixed support
restriction beyond smooth compact Fourier support. Its integration by
parts bound depends on derivatives of the chosen Fourier transform.
It does not provide a uniform asymptotic for our moving family.

For rho=beta+i tau this convention gives
gamma=tau+i(1/2-beta). L018's stated zero symmetry pairs beta+i tau
with 1-beta+i tau, with equal multiplicity. Real-entire f gives conjugate
test values at their translated coordinates; a critical-line zero has
a real coordinate and is counted once with its multiplicity. The selected
right-half zero has negative coordinate imaginary part; the proposed
two-sided rectangle covers it. These are normalization checks, not a
weighted-count estimate or a replacement of algebraic values by modulus
squares. No arithmetic source proof was independently audited here.

## Decision and separate continuation

Source coverage is ready for the quantitative Harnack test saved in
`drafts/literature/2026-10-30-positive-strip-harnack-bound-test.md`.
The prospective lower bound of order log T is a target, not a result of
this literature turn. Proving it would park only this everywhere-positive
analytic detector class at this scale. Failure to obtain it must identify
the exact hypothesis or geometric failure before any construction is
continued. Signed analytic statistics, weaker positivity assumptions,
weighted counts and the main RH gap would remain open.

No lemma, mathematical script, DAG edge or proof assembly changed.
Full Mathlib coverage of Harnack or the detector specialization was not
checked; unknown coverage is not absence.
