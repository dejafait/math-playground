# Source assessment: conditional core and full-response tail

TARGET: Test whether L426's I is negative by combining a uniformly negative conditional core with a certified full-response tail bound.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 195 inspected Sheffield's Markov statement and indicator proof, DLMF 27.4.1--27.4.3 and 27.4.10, and Lamzouri Theorem 1.1's strip/threshold hypotheses; compared L426 (13), (17)--(18), its positive Haar moments, C426a, L422 (9)--(10), L423 (3)--(7), and the step-190/192 stops. No inspected theorem signs this prescribed conditional mean or its expectation; searches do not establish novelty.
SOURCE_EVIDENCE: S. Sheffield, MIT 18.175 Lecture 8, undated current PDF pp. 40--41 (one-based), Markov inequality and complete indicator proof, accessed 2026-10-17; NIST DLMF 27.4.1--27.4.3 and 27.4.10, accessed 2026-10-17; Y. Lamzouri, arXiv:1005.4640v2 (9 January 2011), PDF p. 3, Theorem 1.1 and Remark 1, hypothesis comparison only; reuse the inspected step-193 real quadrature/mean-value and step-187 inclusion/Fubini coverage.
COMPARISON: Markov applies to positive powers of the complete bounded response weight; L426 already identifies their finite positive Euler-moment expansions. This avoids step-192's signed Chebyshev cancellations. Known results approve a finite core/tail comparison, not a sufficient negative margin, a numerical feasibility claim, or narrower response support. Lamzouri's inspected tail theorem requires 1/2<sigma<1 and does not cover sigma=5/2.
GAP: Certify a uniformly negative core, a full-response upper-tail probability, and a bound on every positive conditional contribution outside the core, with a strict negative final comparison. None of these numerical margins is supplied by this review.
REASON: Essential standard-method coverage is now sufficient for one bounded specialization using positive moments and branchwise quadrature; approve only the finite test below, without reproving the probability/Euler theorems.
LITERATURE_REASON: The changed target introduces a signed conditional core and the distribution of the complete multiplicative response; this essential coverage lies outside the saved uniform-sign assessment.
SCOPE: Only L426's unchanged I and A, full product-prime Haar response at exponent 5/2, L423's fixed mixture, and L419/L425's literal selector. One lower core [a,c], positive integer moments of G=gfrak(|Zcal|^2) through order 8, Markov upper tails, and the previously assessed branchwise real quadrature plus g-derivative transport. No independent signed polynomial/moment boxes, joint prime-angle refinement, inverse moments, fitted coefficients or altered response law.
COVERED_TARGET: Test whether L426's I is negative by combining a uniformly negative conditional core with a certified full-response tail bound.

## Relevance, inputs and unresolved assumptions

The main gap remains all-degree mixed positivity or another exclusion
of every off-line zero. This branch's immediate gap is the sign of I.
The intermediate target is a negative conditional core with enough
complete response probability to dominate the complement. Nonzero I
would provide an occupation-test obstruction for the specified L423 law;
it would not repair actual clipping, capped nondegeneracy, actual-function
realization, L413's full-error regulator margin or global mixed positivity.

Essential local inputs are L037, L419, L422, L423, L424, L425, L426
and C426a. Keep the exact rational a,b in C426a, identical to
`/g_full_range` in `scripts/discriminant/bulk-haar-integral-enclosure-188.json`.
These bounds include full-response and coefficient uncertainty. C426a
certifies A(a)<-1/3000 and A(b)>1/1200000, subject to its separate
critical-audit qualification. Neither endpoint attainability nor a core
of useful probability follows. No such assumption is used in this review.
The retained enclosure of I remains step 190's [-.194,.114].

## Inspected primary results and reuse

1. S. Sheffield, *18.175: Lecture 8, Weak laws and moment-generating/
   characteristic functions*, [PDF pp. 40--41](https://math.mit.edu/~sheffield/175/Lecture8.pdf#page=40),
   Markov statement and full indicator proof. A nonnegative random
   variable with finite expectation satisfies P(X>=t)<=E(X)/t for t>0.
   No independence or density hypothesis is required. Apply only to
   positive integer powers of G, which is positive and bounded by L426.
   The resulting numerical tail and its adequacy remain future work.

2. [DLMF 27.4.1--27.4.3 and 27.4.10](https://dlmf.nist.gov/27.4),
   with absolute convergence and, for the divisor generating series,
   integer order and Re(s)>1. These cover the Euler expansion, not
   independence at composite coordinates. Reuse L426's step-192 proof
   of E_mu |Zcal|^(2j)=C_j by absolute multiplication and prime-character
   orthogonality. L422 (9)--(10) already proves the local ratio and full
   omitted-prime bounds for each fixed positive integer j. No new
   probabilistic or Euler-product theorem needs a reproof.

3. Reuse [step 193](2026-10-17-bulk-haar-direct-conditional-sign.md):
   DLMF 3.5.1--3.5.3 requires C^2 on each closed angular cell, and
   DLMF 1.4.11 supplies response-scale mean-value transport. Strict
   selector branches may use certified angular second derivatives;
   unresolved neighborhoods retain their full mass and L426 (13).
   L426 (17)--(18) already provides entire g dependence and domination.
   This is not angular regularity through a tie. Reuse step 187's Rump
   interval inclusion and finite-measure monotonicity/Fubini coverage.
   L426 already makes I the integral of A(G), so no new limit theorem
   or actual-height rate is needed for the limiting sign test.

4. Y. Lamzouri, *On the distribution of extreme values of zeta and
   L-functions in the strip 1/2<sigma<1*,
   [arXiv:1005.4640v2 (9 January 2011), PDF p. 3, Theorem 1.1 and Remark 1](https://arxiv.org/pdf/1005.4640v2#page=3).
   The inspected theorem assumes 1/2<sigma<1 and a large-deviation
   threshold in its stated T-dependent range. Its left-tail remark
   retains that range. Neither statement covers our fixed sigma=5/2
   bounded-response probability. It is a comparison, not an input;
   no passage across sigma=1 or asymptotic tail estimate is imported.

An auxiliary source, P. Stark, *Statistics 240 Lecture Notes*, Chapter 1,
[Sections 1.17.1--1.17.5, PDF pp. 13--15](https://www.stat.berkeley.edu/~stark/Teach/S240/Notes/ch1.pdf#page=13),
was inspected. Do not import its displayed (17) without the increasing,
nonnegative-transform and positive-threshold qualifications, or its
uncentered displayed (22) as written. Sheffield's complete Markov proof
suffices. Hoeffding's 1963 original PDF was retrieved but its theorem
images were not successfully inspected; it is an unread optional lead,
not an input or an essential blocker. A Vershynin PDF request failed
with 502; that source is also unnecessary. No concentration theorem
beyond Markov is approved by this assessment.

## Search comparison and preserved failures

Queries included `Hoeffding 1963 Probability inequalities sums bounded
random variables theorem 2 pdf`, `random Euler product modulus
distribution absolute convergence Bohr Jessen log zeta tail moments`,
`site.math.mit.edu Markov inequality nonnegative random variable lecture
notes pdf`, `"random Euler product" "sigma > 1" distribution modulus
moments tail`, and `"Euler product" "Markov" "moments" random zeta sigma`.
Search leads about critical-line multiplicative chaos, other random
multiplicative models, or the 2026 ICM survey were not inspected as
theorem inputs. No source was found that evaluates this literal A or I;
this bounded search makes no novelty claim.

Step 190's joint prime/angle refinement failed its .75 width-ratio
test. Step 192's signed polynomial/Euler-box expectation had width
5.24030 against .229997 required, with 27 raw nonconstant moment
intervals covering [-1,1]. Those stops remain intact. The present
method uses only nonnegative monomial moments for one tail probability,
not signed Chebyshev reconstruction of E A(G). Step 194's opposite
conditional signs rule out uniform signing on [a,b], not a signed
probability comparison. No sampling or joint refinement is reopened.

## One bounded mathematical test approved

Everything below is a future proof obligation or work limit. This
literature turn derives no new bound, core, sign or lemma.

- Write G=gfrak(W) with W=|Zcal|^2, retaining the exact fixed constants.
  Establish the finite nonnegative-coefficient expansion of E G^r
  for 1<=r<=8 using L426's C_j; required orders are at most 112.
  The changed computation is this positive-moment specialization, not
  a reproof of Markov, orthogonality or the Euler theorem. No unknown
  critical-line moment is required. Saved step-192 positive C_j records
  may be reused only after their relevant full records and tail checks
  are verified; their previews alone are not evidence.
- Use the audited L422/L423 coefficient enclosures. If extra Euler
  evaluation is necessary, cap primes at 200 and local exponents at
  1024. Check every next-term ratio, positive denominator, and r_C(j)<1
  before applying the complete tail formula. No omitted-prime mass
  may be set to zero. Report a failure within these caps honestly.
- Seek a rational c with a<c<b and a certified delta>0 such that
  A(g)<=-delta for every g in [a,c]. Separately enclose A(g)<=M on
  the whole [c,b], with M>=0. The old global bound (13) is a valid
  initial option for M; a smaller value needs a complete certificate.
  Reuse strict-cell real trapezoids, full unresolved-angle ranges and
  a certified sup |A'| for every response transport slab. Point samples,
  zero-measure tie statements and endpoint signs alone cannot certify
  either interval. The core begins at a so no lower-tail assumption
  or inverse moment is needed.
- Obtain an upper bound pbar<=1 for P(G>c) by the minimum of 1 and
  the certified Markov bounds E G^r/c^r, r=1,...,8. For the test to
  succeed, prove the core/complement monotonicity comparison and
  certify the explicit strict inequality

      -delta*(1-pbar)+M*pbar < 0.

  Report delta, M, pbar, the actual left side and its rational margin.
  This is the required threshold, not an inequality established here.
  A useful conditional negative value without this probability budget
  is only partial evidence; it does not sign I.
- Allow at most 33 response centers, 256 response transport slabs,
  4096 angular leaves per integral, 160 decimal places and 262144
  total selector/state/angular-jet/response-derivative callbacks,
  counting preliminary and failed calls. The first 65536 new callbacks
  form a feasibility stage: stop if no nondegenerate negative core is
  certified. Saved certificates can be reused under their contracts;
  new replays count. Use at most 32 candidate cutoffs, within the same
  total budget; do not begin joint prime-angle subdivision or signed
  polynomial expectation work if the comparison fails.
- Stop on a complete strict negative comparison or the stated caps.
  A zero-containing comparison is inconclusive. If no cutoff succeeds,
  record which angular/core or probability error prevents the target
  and park this implementation; repeating it needs a materially changed
  mechanism and separate coverage. No failure disproves negativity of I.

All full certificates and failures must be saved and their load-bearing
fields inspected in the mathematical turn. The success mechanism is
explicit and independently testable; its feasibility is unproved.
This is SPECIALIZE / REPRODUCTION coverage, with no progress beyond
the checked standard tools or originality claim. Full matching Mathlib
coverage for this selector-specific probability certificate is not
checked; supporting integration or Markov results would not verify its
numerical margins. No lemma, mathematical script, DAG or PROOF change
is made by this literature review.
