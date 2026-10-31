# Common-pole test-shape threshold: completed source comparison

TARGET: Assess source coverage for the threshold sup c(h)>=pi/4 over real even h in C_c^infinity(-1,1) with ||h||_2=1, using L527's fixed K and Fourier measure; do not assume its trace asymptotic extends to this class.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact K/phase and common-pole searches plus truncated Wiener-Hopf, spectral variational and time-frequency concentration searches found general operator tools and different-symbol results, not a matching pi/4 theorem. Scoped L526/L527 proofs, ready assessments and both fixed-packet stops were checked; queries and source scopes are recorded below. No novelty inference.
SOURCE_EVIDENCE: Teschl, Mathematical Methods in Quantum Mechanics, posted GSM 99 edition dated 12 February 2009, Theorem 2.19 (2.90)--(2.91), p.77, and Theorems 4.10/4.13 with proofs, pp.118--120, https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf ; Carlsson, On truncated Wiener Hopf operators and BMO(Z), Purdue GMIG report (2010), (1.1)--(1.4), Theorem 2.5 and proof, printed pp.9,15, https://gmig.science.purdue.edu/pdfs/2010/10-02.pdf . A different-symbol comparison with Zhu v2, (2)--(3) and Theorem 1.1, is detailed below.
COMPARISON: Known results cover the bounded compressed-multiplier framework and variational principles, not an evaluated spectral edge for this fixed K, interval and even smooth class. L527's trace asymptotic remains restricted to its prescribed bump. Neither norm-extension comparability nor a finite trial space below threshold bounds the full supremum from above.
GAP: One bounded fixed-symbol variational test remains justified: obtain a certified strict smooth witness or a uniform strict upper bound, with explicit control of any discarded sector. No such bound, compactness, extremizer, trace extension or RH consequence is established by this review.
REASON: Essential general-tool coverage is now sufficient for a direct test of this independently falsifiable shape variation. Exact-symbol estimates and certificate errors are mathematical obligations, not inaccessible source inputs. The separately nominated calculation requires next-invocation approval.
LITERATURE_REASON: The test class changed from L527's one positive bump to all normalized real even compact smooth tests; the essential operator/variational comparison was previously missing. Ready common-pole source assessments are reused without reopening their source proofs.
SCOPE: Completed literature-only review of TARGET. A bounded mathematical continuation is nominated in 2026-10-30-common-pole-test-shape-variational-test.md; no calculation, generalized trace proof, lemma or mathematical script was made this turn.

Use only the same interval, Fourier convention H(t)=integral
h(x)exp(-itx)dx, and measure dm=dt/(2pi). The proposed functional is

    K(t)=(e exp(2it)-1)/(1+2it),
    c(h)=integral |H(t)|^2 Re(K(t)/|K(t)|) dm(t).

The target is the supremum over real even C_c^infinity(-1,1) with
L2 norm one. No positivity requirement is placed on h. Preserve the
fixed K, support interval and normalization while assessing it.
Distinguish supremum >=pi/4 from a smooth witness >=pi/4; an endpoint
limit alone need not supply a witness or a useful strict margin.

Main gap: actual-Xi all-degree positivity. Plausible downstream use:
a certified strict witness would motivate separately justifying the
trace-asymptotic extension for that one chosen h; a strict upper bound
below pi/4 would obstruct this test-shape variation. Neither supplies
collective signs, missing-prime control or actual-Xi transfer.
If the literature leaves only a reformulation or no discriminating
bound, record that honestly and prepare at most one bounded operator
or constructive test. Do not repeat the fixed-bump quadrature.

Essential local input IDs: L527 for the fixed functional/threshold and
L526 for the support/phase context only. The enlargement of h and all
spectral/variational estimates are unresolved. Do not assume new
Sonin localization, a moving-family trace identity or full-Weil
identification. Source proofs and full Mathlib coverage remain
unaudited/unchecked. No cross-notebook input is proposed.

## Completed comparison, 30 October 2026

The original nomination above is retained as the turn-start scope.
This review establishes source coverage only. The pi/4 comparison
and every generalized trace assertion remain unproved.

### Local overlap and recorded failures

Read L527's hypotheses, conclusion and positive-compression setup;
L526's hypotheses/conclusion and the scope of its Toeplitz-kernel
commutator import. Reused the ready generic-increment and L527
critical-audit assessments. The generic and Sonin stop records and
the omitted-signed-increment comparison were inspected narrowly.
They provide no variational bound over the enlarged class. The fixed
bump obstruction is retained, as is the source-level residual overlap
stop. No previous failed calculation of this enlarged supremum was
found in these relevant records; this is not an exhaustive notebook
or originality claim.

### Searches and primary-source comparison

Queries included the following, with mathematical notation rendered
as typed search strings:

- `"truncated Wiener-Hopf" self-adjoint symbol maximum eigenvalue variational`
- `"Fourier" "compact support" "unimodular" "Rayleigh" Toeplitz`
- `"truncated Wiener" "Rayleigh" symbol eigenvalue bound`
- `"e^{2it}" "1+2it" phase`
- `"K(t)" "pi/4" "Wiener"`
- `"e exp(2it)-1"`
- `"exp(2it)" "K(t)" "Sonin"`
- `"common-pole" "test" "variational"`
- `"weighted" "spectral concentration" "Rayleigh" Slepian operator`
- `"Sharp Schatten asymptotics and Sonin trace localization" variational`

Exact strings returned no inspected matching theorem. Broader searches
located the following tools and comparisons. Search failure does not
certify novelty.

**Teschl: variational tools.** [Author's GSM 99 PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
version 12 February 2009, Theorem 2.19, printed p.77,
(2.90)--(2.91): for self-adjoint A, the lower/upper spectral edges
equal the infimum/supremum of its unit-vector quadratic form on D(A).
Theorem 4.10, pp.118--119, uses eigenvalues below essential spectrum,
then its infimum when eigenvalues run out; its proof includes that
case. Theorem 4.13, pp.119--120, requires a normalized domain vector,
Rayleigh value in (lambda_1,lambda_2), and exactly one spectral value
E in that interval. It bounds E using the squared residual divided
by the two distances to the endpoints. Its proof and final
lowest-eigenvalue qualification were read. These are standard inputs,
not the target estimate. A proposed application must establish
self-adjointness on the relevant sector; Temple's inequality needs
spectral isolation established independently. A finite matrix alone
does not furnish that isolation or a bound for the discarded sector.
No theorem here evaluates the present symbol's spectral edge.

**Carlsson: finite-interval multiplier framework.** [Primary Purdue report](https://gmig.science.purdue.edu/pdfs/2010/10-02.pdf),
*On truncated Wiener Hopf operators and BMO(Z)*, GMIG proceedings
(2010), printed pp.9--24. Read (1.1)--(1.4), Theorems 1.1/1.2 and
Theorem 2.5 with proof, printed p.15. For a>0 and a distribution
Phi on (-a,a), Theorem 2.5 characterizes bounded convolution
compression on L2(0,a) by an extension Psi whose Fourier transform
is bounded. If C_Phi is the infimum of ||hat Psi||_infinity over
these extensions, it is attained and
C_Phi/3<=||W_Phi||<=C_Phi. The proof reduces to a=1, regularizes
interior restrictions, uses Proposition 2.4 and takes a distributional
limit. The Fourier sign in (1.2) is positive. This covers a general
framework after checking translation, reflection and normalization;
it supplies neither a numerical extension norm nor the upper spectral
edge in the real-even sector. A symbol-specific estimate is still
necessary. No reproof of this theorem is proposed.

**Different Weil-window problem.** The search also found
[Xuefeng Zhu, arXiv:2608.24827v2](https://arxiv.org/html/2608.24827v2),
2 September 2026, manuscript dated 3 September. Read (2)--(3),
Theorem 1.1 and its stated qualifications. Its form is a rank-one
pole term plus a multiplier containing a digamma function and a finite
prime-power cosine sum. The theorem requires L>0 and a frequency
cutoff with beta*=log(Tsharp/(2pi))-1/Tsharp-A_L>0. Its infinite-space
lower estimate includes both a discarded-block deviation and a
leading-to-tail coupling norm, in addition to the finite block's
least eigenvalue. This is not the fixed phase-ratio symbol c(h).
No source proof, numerical certificate or specialization is imported;
only the exact stated form/hypotheses were compared to reject direct
coverage. No transfer inequality between the two functionals is known
here. Other results in that manuscript were not audited.

**Screened but not imported.** Slepian--Pollak (1961),
*Prolate Spheroidal Wave Functions, Fourier Analysis and Uncertainty I*,
Bell System Technical Journal 40, 43--63,
[DOI](https://doi.org/10.1002/j.1538-7305.1961.tb03976.x),
was located as a concentration lead. Its indexed introduction was
available, but the scan supplied no readable theorem text through
the browser; direct shell retrieval failed DNS. No precise theorem
from it is claimed inspected or used. Likewise Böttcher--Grudsky--Iserles
(2011), DOI 10.1017/S0305004111000259, was screened at abstract level:
its increasing-interval, rational-symbol setting does not supply an
import for the saved fixed-symbol target. Neither lead is essential
to the direct bounded-multiplier test proposed below. They must be
read before invoking a prolate theorem or rational-symbol asymptotic.

### Decision and bounded continuation

EXPLORE is justified for a direct fixed-symbol test using the inspected
general tools; it is not an assertion that the threshold is new or
true. No essential source blocker prevents that test. General
time-band asymptotics, compactness, discrete extremizers or a norm
limit for finite sections must not be assumed.

The proposed discriminator is either a certified real even smooth
unit test with c(h)>pi/4, or a bound uniform over the whole stated
class with supremum strictly below pi/4. A finite-space value below
pi/4 or stabilization of numerical eigenvalues is inconclusive.
An endpoint equality does not imply a strict smooth witness.
Any enlargement to L2, return to compact smooth tests, real-even
sector restriction, Fourier normalization and infinite remainder
must be justified in the mathematical attempt, not assumed from
this source review. A proposed compressed multiplier is a tool to
verify, not a spectral conclusion already established here.

A strict witness would motivate a separate trace-specialization
assessment for that one h; a strict upper bound would stop this
particular shape variation. Neither supplies a collective signed
comparison or RH. L526/L527 are the essential local input IDs for
motivation and conventions only. Source-proof, omitted-term,
missing-prime, full-Weil, nullvector/trace/nonresonance, family-rate
and actual-Xi transfer obligations remain unchanged. Full matching
Mathlib coverage is not checked. No lemma or mathematical script
was written; the new continuation is separately nominated for the
supervisor's next-turn approval.
