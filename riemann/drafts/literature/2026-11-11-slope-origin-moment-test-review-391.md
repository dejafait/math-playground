# Slope-origin moment extraction — source scope approved in step392

TARGET: Test slope-origin moment extraction from C997s's complete capped residual, using analytic propagation to c=0 and growing centered frequency moments, against the exp(-n/64) threshold.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed step391/review390 compares three mechanisms and records exact/stronger-result searches on capped analytic approximation, superoscillatory interpolation, smallness propagation and moving-window moments; scoped duplicate searches found no matching prior origin-extraction assessment. No inspected theorem pays the proposed rate and no novelty is inferred.
SOURCE_EVIDENCE: Step392 directly rechecked Trefethen BIT60(2020) Lemma2.1/Theorems5.1-5.2 and proofs pp904,908, https://people.maths.ox.ac.uk/trefethen/trefethen_ac.pdf ; NIST DLMF https://dlmf.nist.gov/1.9.E31 , https://dlmf.nist.gov/1.10.viii , https://dlmf.nist.gov/18.5.E12 ; exact contracts below. Review390 supplies the already inspected Ferreira–Kempf comparison. These sources cover standard tools, not the extractor or its rate.
COMPARISON: Proposed inverse propagation is in the slope variable, for arbitrary coefficients obeying the original cap; it does not prescribe C997w's jets or reuse a stopped Gaussian or determinant density.
GAP: Construct and bound the specified moment extractor on the complete integrated kernel, pay complex-slope growth and contour-uniform propagation/extraction costs, then compare the lower rate with 1/64. The cap gap, inverse conditioning and final estimate have not been derived here.
REASON: Separate literature-only step392 verifies the direct primary-source trail and approves the unchanged bounded exploration scope. The missing direct-URL process issue is repaired; neither step391 nor step392 derives or approves the prospective mathematical result.
SCOPE: Integer n>=2, C997s's complete kernel and original complex cap, its fixed gamma grid, and exactly the origin-moment/complex-slope certificate below. No change of grid or cap, direct pointwise spectral approximation assumption, general-band obstruction or actual-Xi conclusion is covered.

## Proposed bounded test, not an established identity or estimate

Use exactly C997s's k_n(c,z), I=[7/4,9/4], z_star=1+i/8,
gamma_j=15/8+j/(4n), and arbitrary complex A_j with
sum|A_j|<=exp(sqrt(n)). Write

    R_(n,A)(c)=k_n(c,z_star)-sum_(j=0)^n A_j k_n(c,gamma_j),
    h_(n,A)(t)=exp(i*z_star*t)-sum_(j=0)^n A_j exp(i*gamma_j*t),
    m_n=ceil(sqrt(n)),
    Q_n(z)=((z-2)/(z_star-2))^m_n,
    M_(n,A)=Q_n(z_star)-sum_(j=0)^n A_j Q_n(gamma_j).

These define proposed objects. This review does not prove a moment
gap, recover M from R, or bound its recovery. The research test is:

1. Try to recover M_(n,A) from the c=0 germ of the COMPLETE R_(n,A).
   The proposed procedure is to remove its exp(-cn/4) factor, use
   positive-order Taylor coefficients to separate the c-independent
   lower-window integral, undo the moving-window integration on
   Taylor coefficients, and deconvolve the exact Taylor coefficients
   of g_n. Then form the centered h moment represented by Q_n.
   Every diagonal/nonzero factor, factorial, scaling and inversion
   norm must be proved; no global division by g_n is permitted.
2. Seek a quantitative bound on that extractor using propagation
   from I in the FIXED disk Omega={c:|c-1|<3/2}, followed by Cauchy
   estimates on |c|=1/n. Start with this one geometry; no repeated
   domain tuning or another norm-only regularization is authorized.
   Pay the complex-domain residual bound in the original cap,
   including target growth, both windows and all polynomial factors.
   A pointwise existential propagation exponent is insufficient:
   the contour-uniform exponent and every n-dependent constant must
   be explicit enough to decide the exponential rate. Any gauge
   change must be charged in both the data and extraction norms.
3. Compare the cap-supported lower estimate for |M_(n,A)| with the
   fully paid extractor upper estimate. The desired discriminator is
   a fixed eta>0 and an unbounded integer subsequence on which

       E_n >= exp(-(1/64-eta)*n).

   This would obstruct E_n=O(exp(-n/64)) for this grid and cap.
   An unspecified constant or finitely many degrees is insufficient.
   If a weaker rigorous lower bound is available, record its actual
   exponent and compare it honestly with 1/64. If the fixed-domain
   propagation envelope cannot support the desired comparison,
   preserve its precise cost and park this certificate after the
   single attempt; that is not an upper bound on E_n or proof that
   every inverse mechanism fails. Likewise, inability to bound an
   inverse norm is not a lower bound proving instability.

No derivative of arbitrary C(I) data is proposed. The extractor is
only on the specified finite-dimensional analytic residual range;
its norm must be justified by the global analytic prior furnished
by the cap. First verify analytic extension by a fixed-parameter
integral or an entire antiderivative, before using complex c. The
original lower-window term must be eliminated by an exact identity,
not dropped from the objective.

## Applicability, relevance and prior stops

The complete kernel is the essential input from C997c; C997s supplies
the actual continuum objective and complex l1 budget. Use DLMF18.5.12
for finite Laguerre coefficients, DLMF1.10.18 only after fixing the
integration parameter, and DLMF1.9.31 only on a valid analytic contour.
The primary contracts, theorem proof cases and comparison searches
are in [completed review390](2026-11-11-direct-capped-kernel-discovery-review-390.md).
Do not reprove the standard continuation or Cauchy theorems. Their
kernel-specific inverse and the growing-order quantitative estimate
are exactly the unpaid work, not a source theorem specialization
already performed by this literature turn.

C997w/C997x concern an uncapped successful interpolant with inadmissible
prescribed high jets. Here no candidate coefficients have prescribed
jets; the aim is a necessary consequence of a small integrated residual
for every admissible vector. C997r's sufficient defect upper bound
cannot be reversed without proof. C997s's finite atomic searches
neither provide nor exclude this detector. C997t's constant-ODE and
C997u's prescribed determinant-density scopes do not cover this germ
inverse. C997v's absolute contour envelope and C997d's forward Hardy
envelope are preserved without reuse as a universal impossibility.
No prior stop is erased or treated as a global ban.

The main gap remains L030-L032/C032a actual-Xi positivity,
L966/L968 signed forcing and unpaid L984(H). A successful lower rate
would stop one fixed-grid capped bridge and guide a different assay;
it would not stop arbitrary band measures or imply RH or its negation.
Independent gaps include C997a(8), selected/both-sign transfer,
assay/reconstruction, complements/regulators and L993. Full matching
Mathlib coverage is unchecked. No cross-notebook input or RH candidate.

## Separate approval and direct source trail — step392, 11 November2026

The recovery issue was missing direct source URLs in this ready assessment.
This separate literature-only approval checks the same target and assumptions;
it authorizes one attempt, not its conclusion. No lemma, calculation or
mathematical script is added. Review390's search and scoped-family comparisons
are reused; no new novelty claim or repeated discovery search is needed.

* L. N. Trefethen, *Quantifying the ill-conditioning of analytic continuation*,
  BIT Numerical Mathematics 60 (2020), 901–915,
  [published author PDF](https://people.maths.ox.ac.uk/trefethen/trefethen_ac.pdf),
  DOI [10.1007/s10543-020-00802-7](https://doi.org/10.1007/s10543-020-00802-7).
  Rechecked Lemma2.1 and proof p904: an analytic function bounded by one
  in 0<Re(w)<1, with boundary limsup at Re(w)=0 at most epsilon in (0,1),
  obeys the three-lines power bound. The proof uses bounded-strip
  Phragmen–Lindelof; it does not license an unbounded auxiliary function.
  Rechecked Theorems5.1-5.2 and proof p908: connected open Omega, bounded
  nonempty continuum E whose closure encloses no points of Omega\E,
  analyticity on Omega union E, piecewise smooth boundary of E, data
  bound epsilon, and global bound one yield a point-dependent exponent
  in (0,1). The proof connects E to the point by an arc and maps a
  suitable neighborhood to the half-strip. It provides neither the
  required uniform exponent on our contour nor the original-cap growth
  bound. These remain explicit research obligations.
* NIST DLMF [1.9.30–31](https://dlmf.nist.gov/1.9.E31), Cauchy integral
  formulas: continuity within and on a simple closed contour, analyticity
  inside, interior evaluation point, and positive contour orientation.
  The derivative formula retains its order factorial and denominator
  power. It supplies no inverse norm on the residual range.
* NIST DLMF [1.10(viii), equations18–19](https://dlmf.nist.gov/1.10.viii):
  joint continuity and parameter analyticity on a fixed finite real
  integration segment give analyticity and differentiation under the
  integral. Improper endpoints additionally require compact-uniform
  convergence. The proposed moving-window conversion must still be
  written and justified before use; this review does not perform it.
* NIST DLMF [18.5.12](https://dlmf.nist.gov/18.5.E12): the finite Laguerre
  expansion applies at integer degree n+1 and alpha=2. Its finite-sum
  form supplies exact coefficients, retaining the kernel's separate
  constant subtraction. It gives no deconvolution conditioning bound.

DLMF live text was rechecked on 11 November2026; the release identifier
was not independently verified. These are primary theorem/formula sources.
The Ferreira–Kempf comparison remains the inspected review390 contract
([author PDF](https://sweet.ua.pt/pjf/PDF/Ferreira2006a.pdf), Theorem2,
pp3736–3738): finite-energy interpolation is a different norm and data
problem. It is not an imported obstruction for C997s. Full matching
Mathlib coverage remains unchecked. No unresolved source-access blocker
is claimed; the remaining analytic and inverse estimates are the target.

## Routing after the completed separate approval gate

Recommend proof_attempt/creative, deep_research/max, for this precise
test, now source-approved: the new mechanism would turn complete-integral
smallness into a necessary moment constraint on all capped coefficients.
The critical obstruction is quantitative loss in inversion and analytic
propagation to the origin. The bounded evidence is the explicit final
lower exponent versus 1/64, or a precise failure of this fixed-domain
certificate. Do not label another mere application of a generic
continuation bound an advance. No extraction, rate calculation, new
lemma or mathematical script was produced in either literature review.
