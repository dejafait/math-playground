# Source comparison: growing finite-prime covariance weights

TARGET: Assess source coverage for replacing L423's bounded covariance weight by a slowly growing finite-prime Poisson product while preserving its selected moments and matching every fixed single-prime second correlation.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 209 searched weighted prime phases, finite Euler/Poisson products, Riesz products and GCD Poisson integrals; inspected the published Aistleitner--Berkes--Seip Lemma 1 and its complete preceding integral identity, Silvestre section 2.4 and BCR Theorem 1; reused step 204's Young/conditional-result comparison and step 183's compact-group coverage. Scoped October-15--18 local searches found the proposal and narrower stops, not a completed growing-product law; no novelty claim follows.
SOURCE_EVIDENCE: Aistleitner--Berkes--Seip, JEMS 17 (2015), 1517--1546, DOI 10.4171/JEMS/537, section 3, pp. 1523, 1527, Lemma 1/(23) and preceding identity, https://ems.press/content/serial-article-files/32047?nt=1 ; Young, Arch. Math. 95 (2010), Lemmas 4--5, pp. 542--543 through audited L381 (7); Kowalski B.6.3/B.6.5 and 3.2.5/3.2.6, and Tao Lemma 2.3 through the inspected step-183 assessment. Exact versions and limits are recorded below.
COMPARISON: The proposed finite product is a standard polydisc Poisson kernel; its coefficient identity is already in the literature. Known fixed-test zeta moments and compact-group convergence cover the fixed-cutoff inputs. They do not supply an H-dependent full counterlaw; cutoff selection, complete response tails, normalization and simultaneous law margins remain specialization obligations.
GAP: Test simultaneous feasibility of a sufficiently slow cutoff with the full covariance subtraction, translated negative support, original selected tolerances, fixed physical envelopes and all fixed single-prime tests. No construction, cutoff rate, new coefficient theorem or compatibility conclusion is established here.
REASON: Essential source coverage is adequate for the bounded feasibility test documented in the separate continuation assessment; import the standard identities and prove only the changed law and limit bookkeeping after separate approval. This completed literature-only comparison modifies no lemma or mathematical script.
SCOPE: Fixed finite-prime products first, sharp real-height averages, complete response on Re s=5/2, and a prospective qualitative diagonal cutoff only; no uniform growing-twist theorem, conditional critical-jet law or infinite critical-line Euler product is covered.
LITERATURE_REASON: The saved target changes L423's fixed bounded weight and falls outside step 204's bounded-density test; finite-product coefficient and full-law limit coverage was essential and REVIEW_REQUIRED at invocation start.

## Original proposal retained from step 208

The main gap is global mixed positivity. The intermediate target is
source coverage for one concrete replacement weight: the finite product

    P_y(t)=product_(p<=y) (1-1/p)/|1-p^(-1/2-it)|^2,

with a cutoff y=y(H) tending to infinity sufficiently slowly, and the
same fiber normalization g_H=P_y/E_H[w P_y] as in L423. This is a
proposed ansatz only. No coefficient evaluation, cutoff rate, limit,
feasibility claim or new mathematical result is asserted.

A feasible replacement could determine whether the all-fixed-prime
constraints still permit joint-sign avoidance and a vanishing capped
cubic once the uniform bulk-density bound is relaxed. Conversely, an
obstruction would need to distinguish this changed mechanism from
L428's already exhausted uniformly bounded case. Neither outcome
would itself decide actual clipping, actual critical-function
realization, L413's full-error regulator margin or RH.

The review must check the finite-product statement against known
weighted zeta and harmonic-analysis results, reuse the inspected Young
and Poisson inputs when adequate, and identify essential missing cases.
A fixed-cutoff-first diagonal choice must not be mistaken for a uniform
growing-twist theorem. A conditional weighted-distribution theorem
would not supply an unconditional input. The high and intermediate
components and full raw covariance subtraction must stay visible;
no independence of actual critical jets and prime phases is assumed.

Continuation test: approve a bounded mathematical target only if the
sources cover the fixed-product coefficients and limiting framework,
and allow an explicit test of the growth/lower-bound requirements
needed by L423's full covariance and selected tolerances. If these
requirements conflict, record the conflict as a target for proof;
if essential sources remain unavailable, delimit the blocker without
attempting dependent mathematics. Do not approve merely from the
formal product or from the failure of the old uniform bound.

Essential local inputs: audited L428, L381 (7), L389 (3), L419's
negative trace and response bounds, L421's two rare components, and
L423's full normalization and matrix correction. L422's imported
response-weighted coefficient and L427's narrower stop may need their
specific relevant ranges during the comparison. No cross-notebook
input is proposed. Global realization, actual clipping, capped
nondegeneracy and the regulator margin remain unresolved. Mathlib
coverage for this changed construction has not been checked.

## Completed comparison — step 209

This review supplies source coverage, not the proposed mathematical
construction. The original proposal above is retained; its statements
about missing review describe its startup state. The main RH gap and
the proposed downstream use remain exactly as stated there.

### Direct finite-product source

C. Aistleitner, I. Berkes and K. Seip, *GCD sums from Poisson integrals
and systems of dilated functions*, J. Eur. Math. Soc. 17 (2015),
1517--1546, [published primary PDF](https://ems.press/content/serial-article-files/32047?nt=1),
DOI 10.4171/JEMS/537: read section 3's multi-index/prime notation on
p. 1523 and the complete kernel identity and Lemma 1, equation (23),
p. 1527. For positive coordinates r_j<1, normalized Haar measure on
T^K, and finitely supported nonnegative multi-indices beta,mu with
support in {1,...,K}, the displayed identity is

    integral z^beta conjugate(z^mu) P_K(r,z) d sigma_K
        = r^(|beta-mu|).

Lemma 1 states the resulting identity for arbitrary finite complex
coefficients and their whole squared polynomial. The preceding proof
is iterated one-circle integration; it requires no square summability
of the infinite sequence. Taking the source's coordinates r_j=p_j^-1/2
meets its hypotheses, including the endpoint alpha=1/2. Its kernel
definition is exactly the proposed finite product. This known identity
should be cited rather than rediscovered. It identifies no actual
conditional critical-jet law or admissible growing cutoff.

Silvestre, [PDE notes](https://www.math.uchicago.edu/~luis/pdenotes.pdf),
section 2.4, printed p. 24 (PDF page 24), was directly rechecked: the
disk kernel has Fourier series (2pi)^-1 sum r^|k| exp(ik theta),
0<=r<1, and total integral one in d theta. The proposed convention
uses normalized Haar measure, hence omits the (2pi)^-1. This supports
the finite-product import but adds no growing-parameter theorem.

### Reused moment and averaging coverage

Reuse the exact Young hypotheses and both off-diagonal cases already
inspected in
`drafts/literature/2026-10-17-finite-prime-covariance-domination.md`.
The primary source is M. P. Young, *A short proof of Levinson's theorem*,
Arch. Math. 95 (2010), 539--548, Lemmas 4--5, pp. 542--543,
[published PDF](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf).
L381 (7) is the audited fixed rational-twist specialization with both
functional-equation diagonals. L428 (3)--(6) supplies the sharp fixed
single-prime target by four nonnegative squares. No new zeta moment
or extension of twist length is needed merely to define those targets.

Reuse step 183's inspected primary statements, exact versions and proof
cases in
`drafts/literature/2026-10-17-covariance-free-bulk-phase-averaging.md`:
E. Kowalski, *Arithmetic Randonnee*, January 19, 2021, Theorem B.6.3,
B.6.5(2), Example B.6.6(2), pp. 146--147, and Proposition 3.2.5/Lemma
3.2.6, pp. 42--43,
[course manuscript](https://metaphor.ethz.ch/x/2021/fs/401-3109-65L/probabilistic-number-theory-fs-2021.pdf);
and T. Tao, *247B Lecture Notes 8*, Winter 2007, Lemma 2.3/(4),
pp. 4--5, [author notes](https://www.math.ucla.edu/~tao/247b.1.07w/notes8.pdf).
Their compact-group character criterion and sharp nonstationary bound
are adequate fixed-product tools. L419 (5) and L423's fixed gamma
harmonic provide local examples. An H-dependent increasing character
family is not itself covered by weak convergence. A prospective slow
diagonal selection must be written separately for all real H beyond
chosen thresholds, keeping its finite stage fixed when taking limits.
No effective growth rate is asserted or needed for the proposed test.

Directly revisited S. Bettin, V. Chandee and M. Radziwill,
*The mean square of the product of the Riemann zeta-function with
Dirichlet polynomials*, [arXiv:1411.7764v1](https://arxiv.org/pdf/1411.7764v1),
November 28, 2014, (1.1)/Theorem 1, pp. 1--2. It assumes smooth phi
supported in [1,2], a_n=O_epsilon(n^epsilon), and N=T^theta with
theta<17/33; the error is
O(T^(3/20+epsilon)N^(33/20)+T^(1/3+epsilon)). An untruncated finite
Euler product still has infinitely many prime-power terms, so this
is not a direct growing-product law theorem. Its stronger length range
is unnecessary for a fixed-stage qualitative construction. Do not
reprove it or claim that it solves the covariance problem.

### What must still be proved in the mathematical attempt

The separate continuation assessment specifies a single feasibility
test. Its load-bearing obligations are these; none is proved here.

- Connect the cited finite-product coefficients to the sharp actual
  single-prime targets. For complete W and W^2, identify the limiting
  response-weighted coefficients with L419's S and L422's T using
  their absolute series and all rational collisions. Retain the gamma
  harmonic for the first-D calibration. These are mathematical
  specializations, not assumed phase independence.
- Control full response tails uniformly in the eventual cutoff using
  normalized positive weighted mass, or another proved bound. A tail
  estimate multiplied by an uncontrolled sup P_y is insufficient.
  A fixed-y limit alone does not prove the moving-y statement.
- Retain L421's unchanged high and intermediate components, their
  unnormalized second matrix Q=O(sqrt(ell)) and E(1-w)=O(ell^-5/2).
  L423's N_H and A_H must be used in full. Its old uniform bounds on
  g_H cannot be quoted for the new weight. Both the minimum and maximum
  of each finite product, normalization losses and all error constants
  must enter the prospective threshold selection.
- Check positive definiteness of Sigma=ell g_H K+A_H, negative trace
  and negativity of each *translated* six-state atom. The translation
  error depends on the largest covariance, whereas the negative margin
  can depend on its smallest value. Checking either extreme alone is
  inadequate. Reuse L419's Borel Schur--Horn construction, not a new
  unproved measurable-selection assertion.
- Preserve the original required tolerances: all six raw second
  entries and first-B mean can be enforced by their exact formulas;
  first-D, signed cubic, all 23 quartics, absolute envelopes and fixed
  physical jet constants still need estimates. L423's improved bulk
  O(sqrt(ell)) support and O(ell) cubic errors are not hypotheses to
  impose unchanged; the original moment tolerances are the target.
  Include vanishing capped absolute cubic for every fixed cap with
  one family independent of that cap, if claiming the counterlaw.

The diagonal is therefore a prospective finite-stage proof obligation,
not an imported uniform theorem. The cited inputs suffice to *test*
these obligations without missing essential source coverage; they do
not certify that they are compatible. If they conflict for this exact
ansatz, preserve the conflict rather than modify the ansatz mid-attempt.

### Search, overlap, failures and decision

Queries included `zeta weighted prime phases Poisson kernel twisted
second moment finite Euler product`, `Riesz product Poisson kernel
primes zeta second moment limiting measure`, `"zeta" "Poisson kernels"
primes`, and `Aistleitner Berkes Seip GCD sums Poisson integrals
Proposition 1 polydisc`. Searches for a slow-parameter diagonal theorem
produced no useful primary statement; no such hit is used. The elementary
threshold bookkeeping remains to be supplied, not a named theorem
claimed from memory. Other snippets, random-zeta models and informal
RH claims were not theorem inputs.

Scoped searches in the active notebook's October-15--18 assessments,
histories and ATTEMPTS, followed by an exact author/DOI search in local
source records, found no completed law for this new weight. The GCD
representation is explicitly known; the search establishes no novelty
for any remaining construction. Step 204's Fazzari comparison remains
adequate: the inspected weighted central limit statements have RH and/or
moment-conjecture assumptions and do not cover this unconditional law.
No additional conditional source is imported.

L422's single-power mismatch, L427's unchanged-mixture mismatch and
L428's uniform-density contradiction remain valid at their exact scopes.
They do not already decide this changed ansatz. The C426b/C426c
core/tail implementation stays parked at 261020/262144; I is not used.

Decision: SPECIALIZE for the one feasibility test in
`drafts/literature/2026-10-18-growing-prime-poisson-law-feasibility.md`.
Continue only with a complete simultaneous cutoff/margin/tolerance
argument or an informative obstruction specific to this ansatz. Stop
an argument that assumes a uniform growing-twist theorem, independence,
an infinite critical Euler product or a dropped rare/correction term.
A new ready continuation receives separate approval next turn. No
mathematical exploration turn is spent by this review. Full matching
Mathlib coverage was not checked; no absence claim is made. No new
lemma, construction, actual clipped value, regulator margin or RH
advance is reported.
