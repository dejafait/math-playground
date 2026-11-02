# Sine Peano dual: source-approved independent audit

TARGET: Audit L575's two sine-dual budgets and complete stationary endpoint sum.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed exact-weight, weighted-moment and endpoint-saddle searches and L319/L482/C574a failure comparisons in drafts/literature/2026-10-31-bounded-sine-prime-peano-dual.md; read all of L575 and the relevant local input statements and proof interfaces. No renewed broad search or novelty inference.
SOURCE_EVIDENCE: Reused Curran 2303.10123v2 Lemma 2.3, Villarino math/0504289v3 Theorem 6 and C481a's de Boor input; retrieved Gonek Invent. Math. 75 (1984), Lemmas 1--2 pp. 129--130 and their central/outer/endpoint cases, and Banks 2405.11084v1 Lemma 2.8 for the readable exact formula and Gonek attribution. L316 (7), L477, L574 and C574a supply the local interfaces; no source-proof audit or L575 mathematical audit was performed.
COMPARISON: Arbitrary finite coefficients, real prime endpoints and the endpoint-uniform logarithmic saddle cover the analytic tools actually used in L575; they do not prove its weighted cubic budgets or summed stationary estimate. SPECIALIZE approves independent verification of the existing finite argument with named theorems imported, not a new mechanism or reproof of those theorems.
GAP: Verify grouped lengths and multiplicities, the variable-jet expansion, shifted cubic cost, exact-theta reduction, both saddle branches, the complete endpoint-error sum and lattice bound, fixed constants and signed Peano/defect transfer. All of L575 remains unaudited.
REASON: Separate source approval for the previously nominated critical audit is complete; the remaining uncertainty is local mathematics rather than missing essential coverage. This approval supplies no new mathematical result and does not certify the route stop.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED required comparing the new L575 argument with reusable coverage; its complete stationary sum specifically required checking the readable primary endpoint formula and relevant Gonek proof cases.
SCOPE: Only L575 as written, arbitrary sufficiently large real T, fixed M=floor(sqrt(T/(2pi))), h=1/log T, full J=[T+h,2T-h], the entire block T^(1/16)<p<=T^(1/8), both weighted cubic remainders and the complete ordered chirp. No effective onset, source-proof audit, Xi sign, negative-mass saving or alternative approximation is covered.

## Original nomination, preserved; source status superseded above

L575 is an unaudited local mathematical result from the approved first-order
calculation. It is not a possible complete RH solution. Its proposed consequence
is to rule out precisely L477's fixed-square little-o defect route; the actual
Xi sign and negative-mass questions are separate. Preserve all older stops.

Essential inputs are L316 (7), L477, C481a, L574 and C574a. No cross-notebook
input is proposed. The previous source comparison is
`2026-10-31-bounded-sine-prime-peano-dual.md`; its initial hypotheses and primary
statements should be reused rather than generically searched again. Review
whether source extraction of the original Gonek lemma is essential to the
independent audit. If so, retrieve only that exact statement and endpoint cases.
No assertion about Mathlib coverage or source-proof correctness is made.

The audit's discriminating tests are whether the entire endpoint error really
is o(T L^3) uniformly at arbitrary real T, whether both shifted weighted cubic
costs are O(T L) and O(T L^3) with fixed constants, and whether the linear chirp
budget 1/2048 is compatible with the density lower budget 1/512. A normalization,
length, boundary or fixed-constant error would require repair or withdrawal of
the affected claim. Numerical sampling cannot validate these all-height bounds.
The current turn merely nominates this next source-coverage assessment.

## Separate source approval, 31 October 2026

The completed gate was: Assess source coverage for an independent audit of
L575's two sine-dual budgets and complete stationary endpoint sum. The exact
mathematical continuation is now the TARGET above. This is a literature-only
approval, not an independent verification of any step in L575.

The main gap is actual-Xi all-degree positivity and unbounded-height initial
signs. The intermediate target is validation or repair of L575's full-residual
lower bound. Its plausible use is to exclude precisely L477's fixed-square
little-o defect route. Lower bounds for absolute defect do not settle negative
mass, other squares, Xi signs or RH. Essential local inputs remain L316 (7),
L477, C481a, L574 and C574a; no cross-notebook input is proposed.

### Imported statements and applicability boundary

**Finite moments and prime endpoints: unchanged coverage.** Reuse Michael J.
Curran, *Correlations of the Riemann zeta function*, arXiv:2303.10123v2
(15 May 2024), [Section 2, Lemma 2.3](https://arxiv.org/html/2303.10123v2#S2),
and the prior bounded-sine assessment. This unconditional finite mean-square
theorem allows arbitrary complex coefficients and the error
O(N sum |c_n|^2). Its applicability is to each fixed grouped vector, not
height-dependent jet coefficients. The common interval translation is already
written in L574 (7). Adjacent disjoint-prime and prime-only moment lemmas do
not replace overlapping-support grouping. No source refresh is needed.

Reuse Mark B. Villarino, *Mertens' Proof of Mertens' Theorem*,
math/0504289v3 (17 May 2005), [Theorem 6, printed p. 7,
(2.3.4)--(2.3.5)](https://arxiv.org/pdf/math/0504289v3#page=7).
It covers sum_(p<=z)1/p=log log z+b+O(1/log z), real z>2.
L575's logarithm-weighted sums require checking its own finite partial
summation and retained endpoint convention. The source theorem is imported;
reproving Mertens is unnecessary. The sharper density constant is a local
audit obligation, not an imported constant.

**Logarithmic saddle: primary text retrieved.** S. M. Gonek, *Mean values of
the Riemann zeta-function and its derivatives*, Invent. Math. 75 (1984),
123--141, [Lemmas 1--2, printed pp. 129--130](https://sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf#page=7).
Read the quadratic central change, near-endpoint second-derivative bound,
interior saddle plus outer integrals, and exterior integration-by-parts cases.
The calculus lemmas impose no RH. The imported statement uses fixed sigma,
large A, A<B<=2A and positive saddle parameter r. It retains the oscillatory
main term for A<r<=B and an endpoint-distance error for every r, including
outside the interval. No source proof is independently audited.

The extracted original formula has imperfect OCR; screenshot retrieval did
not yield a usable image and a local-shell download failed DNS. No visual
formula verification is claimed. Reuse the prior primary inspection and
the following separately retrieved readable statement; these access limits
do not leave the required theorem scope inaccessible.

William Banks, *Shifting the ordinates of zeros of the Riemann zeta function*,
[arXiv:2405.11084v1, Lemma 2.8](https://arxiv.org/html/2405.11084v1#S2.SS4),
explicitly attributes the formula to Gonek Lemmas 2--3. The page labels v1
17 May 2024 and has internal date 24 August 2026. Its unconditional lemma
is uniform for 10a>=b>a>=10, sigma in [1/10,10], m in {0,1}.
For the negative phase it states the main coefficient
(2pi)^(1-sigma)u^sigma exp(i(u-pi/4)), with indicator a<u<=b,
and error O(E (log a)^m), where

    E=a^(sigma-1/2)+a^(sigma+1/2)/(|a-u|+sqrt(a))
                      +b^(sigma+1/2)/(|b-u|+sqrt(b)).

The choices a=T, b=2T, sigma=1/2, m=0 lie in these ranges.
Complex conjugation matches the positive phase in L575 (15), including
its sqrt(2pi r) normalization. Equality and exterior cases are explicitly
covered; the indicator convention alone does not make endpoint error small.
Banks's RH-dependent main theorems are not imported.

**Other interfaces: reuse, do not expand the target.** L316 (7) supplies
the analytic logarithm and actual phase; L477 fixes R=U+V and the defect
error. C574a supplies its complete coefficient bound, not a sine leakage
estimate. C481a's audited Peano input is Carl de Boor, *Divided Differences*,
Surveys in Approximation Theory 1 (2005), Section 9, p. 62, (46)--(48),
[primary text](https://surveys-in-approximation-theory.com/papers/2/2.pdf#page=17).
Finite real Taylor remainder, compact Fubini and Cauchy--Schwarz suffice as
standard named tools. Their actual applications still need review. Full
matching and supporting Mathlib coverage remain unchecked; this says nothing
about absence. No reproof of general analytic theorems is requested.

### What the next mathematical audit must decide

The published results supply tools rather than a matching full-residual
theorem. The previous assessment's inspected Fazzari and
Bettin--Chandee--Radziwill results concern different weights, cutoffs or
smoothing and do not eliminate this verification. Its exact-statement
searches and duplicate comparisons are reused without an originality claim.
L319's stationary involution, L482's uniform approximation obstruction,
L481's interpolation stop, L572's certificate failure and C574a's derivative
budget remain evidence about their specific mechanisms. None may be removed
or reported as a generic prohibition on this different sine test.

Check all of L575's existing proof, with particular attention to:

- Actual lengths and ordered multiplicities of A_sigma B^3 and E_r B^3;
  repeated primes, primes dividing n, and fixed-vector mean-square use.
- Both weighted cubic costs, including variable lambda, all |u|<=h shifts,
  and the convolution normalization and both boundary strips.
- Both chirp signs, phase and 2pi factors, the full positive stationary sum,
  every exterior and endpoint mode, and the summed errors uniformly for real
  T. A theorem for each mode is not a theorem for their aggregate.
- The lattice upper estimate, real-endpoint partial summation and compatible
  constants: density 1/512 and linear leakage 1/2048; fixed finite cubic
  constants must permit one positive epsilon independent of T.
- Signed Peano pairing, |psi|<=1 and transfer through L477's defect error.

Accept the obstruction only if the complete stationary error is uniformly
o(T(log T)^3), the cubic costs are O(T log T) and O(T(log T)^3), and both
fixed budgets hold at every sufficiently large real T. Otherwise repair the
affected claim within scope or leave it unverified and withdraw reliance on
its route stop. Finite samples are insufficient. No effective onset is claimed.
The next step is RESEARCH / REPRODUCTION, proof_audit/conceptual_audit; it
audits an existing argument and is not creative discovery. Essential review
of this new route-changing claim presently blocks preparation of a justified
creative central-gap target. No further literature turn is needed for this
unchanged scope unless an actual essential source mismatch is found.
