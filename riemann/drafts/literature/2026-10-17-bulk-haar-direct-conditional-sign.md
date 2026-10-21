# Source assessment: direct conditional angular sign

TARGET: Assess whether L426's conditional mean A(g) has one strict sign throughout the saved rational g interval, using angular integration and a response-scale derivative bound.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 193 searched Schur-Horn Gaussian angular signing, validated parameter-dependent quadrature and piecewise-analytic integration; inspected NIST DLMF 1.4.11--1.4.12 and 3.5.1--3.5.3 and rechecked Johansson arXiv:1802.07942v1 Section 2; compared L426 (17)--(18), L419/L425's literal branches and the preserved step-175, 188--190 and 192 failures. No inspected theorem signs this prescribed mean; failed searches establish no novelty.
SOURCE_EVIDENCE: NIST DLMF Section 1.4(iii), equations 1.4.11--1.4.12, and Section 3.5(i), equations 3.5.1--3.5.3, online versions accessed 2026-10-17; Johansson, Numerical integration in arbitrary-precision ball arithmetic, arXiv:1802.07942v1 (22 February 2018), Section 2 pp. 2--3, full four-step algorithm and tolerance qualifications; reuse step-187's inspected Rump Sections 5.5--7.1 for inclusion and exact inputs.
COMPARISON: Known mean-value and quadrature bounds cover a finite uniform-sign test after certified response derivatives and branchwise angular errors. L426 already proves differentiability in g despite angular selector jumps. Neither the sources nor the old certificates supply a strict conditional sign or an adequate numerical budget; all step-192 node intervals contain zero.
GAP: Certify angular integrals more tightly than the failed range boxes, bound A' on complete response slabs, and cover the entire saved rational interval with one strict sign or certify two opposite-sign values. Numerical feasibility and the sign remain unproved.
REASON: The changed target now has sufficient standard-method coverage for one bounded mathematical test; this approves the test, not uniform signing or efficient convergence.
LITERATURE_REASON: The changed sufficient condition requires response-scale sign transport and tighter branchwise angular quadrature; polynomial expectation coverage alone did not assess these obligations. Reuse the existing inclusion and selector coverage rather than repeat its source discovery.
SCOPE: Only L426's unchanged A(g) and (17), the complete saved g interval, L419/L425's exact ordered two-stage selector and L423's fixed mixture. Covered methods are branchwise real trapezoidal quadrature with certified second angular derivatives, or Johansson's analyticity-tested Gaussian quadrature, full range bounds on unresolved angular neighborhoods, and a certified first g-derivative bound with the mean-value theorem. No joint prime-angle subdivision, independent polynomial/Euler-moment boxes, altered basis, fitted mixture or narrowed response support.
COVERED_TARGET: Assess whether L426's conditional mean A(g) has one strict sign throughout the saved rational g interval, using angular integration and a response-scale derivative bound.

## Relevance and exact scope

The main gap is global mixed positivity or another exclusion of every
off-line zero. This branch's immediate gap is the undecided sign of I.
The intermediate target is the stronger sufficient condition that A has
one strict sign on the entire saved g interval. Its prospective use is
L424--L426's occupation comparison: nonzero I would obstruct realization
of this complete L423 law by the specified ordinary-jet trajectories.
This does not invalidate the selected-moment obstruction or evaluate
actual clipping, capped nondegeneracy or L413's full-error regulator margin.

Reuse L426's exact definition

    A(g)=(1/3) sum_i integral_0^(2pi)
          Q(sqrt(3g) P u_i(exp(i theta))) dtheta/(2pi),

and its already proved entire state identity (17) and bounds (18).
No new identity or derivative estimate is proved in this review.
The selector depends on angle, not g. Thus L426 already supplies the
domination for g differentiation; it supplies no angular smoothness
across a selector tie. L419's first-pair/equality convention and L425's
complementary low/high order must remain literal in every evaluation.

The complete selected value `/g_full_range` in
`scripts/discriminant/bulk-haar-integral-enclosure-188.json` was inspected
with the shared JSON inspector, using `--full` only for that field:

    [164144438496585479013809/1000000000000000000000000,
     2496151417412820236290361/62500000000000000000000].

It includes coefficient and full-response uncertainty. Its endpoints,
approximately .1641444 and 39.9384227, are not permission to replace the
rational interval by a fitted or likely support. L423's fixed mixture
and L422's full-response scope remain inputs to that range. New Euler
moments are unnecessary for a uniform conditional-sign test. Retain
L037's arithmetic contracts. No cross-notebook input is used.

## Primary results and applicability

1. [NIST DLMF 1.4(iii), (1.4.11)--(1.4.12)](https://dlmf.nist.gov/1.4.iii).
   The mean-value theorem requires continuity on a closed real interval
   and differentiability in its interior. Leibniz's finite derivative
   formula applies to sufficiently differentiable products. These cover
   sign transport from certified point values using a derivative bound,
   and differentiation of L426 (17). L426 already checks the relevant
   g regularity. The numerical derivative bound remains to be established;
   finite differences or bounds at sampled g values would not suffice.

2. [NIST DLMF 3.5(i), (3.5.1)--(3.5.3)](https://dlmf.nist.gov/3.5.i).
   The elementary trapezoidal error is minus h^3 f''(xi)/12 and requires
   f in C^2 on the closed cell. The composite version uses equal spacing
   and the corresponding whole-interval second-derivative remainder.
   This permits signed integration on strict branch cells after enclosing
   their derivatives. It does not permit a single smooth periodic error
   formula across L419's jumps. Use the elementary formula separately on
   certified cells, and integrate complete range bounds on unresolved
   neighborhoods. No computed angular derivative is imported here.

3. Fredrik Johansson, *Numerical integration in arbitrary-precision ball
   arithmetic*, [arXiv:1802.07942v1](https://arxiv.org/pdf/1802.07942),
   22 February 2018, Section 2 pp. 2--3. Rechecked the full algorithm:
   callbacks enclose their entire argument boxes; the analytic flag also
   certifies the domain. Gaussian error control requires an enclosing
   complex ellipse, analyticity and a modulus bound there. Failure falls
   back to whole-segment ranges/bisection; evaluation limits may return
   wide valid balls. Requested tolerance is not achieved accuracy.

   For this selector, a strict real branch is insufficient to certify a
   complex ellipse. Freeze the actual branch and verify all square-root
   cuts and denominators on that ellipse before Gaussian acceleration.
   Real trapezoidal quadrature above is an alternative requiring only
   certified real second derivatives. Neither method assumes continuity
   through a tie or simplicity of every tie. All outer g parameters in
   a derivative enclosure must remain enclosed, not fixed at a midpoint.

Reuse [step 187's assessment](2026-10-17-bulk-haar-integral-enclosure.md)
for Rump's inclusion principle and exact-input conversion; no changed
arithmetic hypothesis requires rereading that source. Reuse step 191's
assessment only as historical comparison: its interpolation and Euler
moment machinery is not the proposed integration method.

The bounded searches used `"validated integration" "parameter" "Cauchy"
Johansson`, `"Schur Horn" "Gaussian" "angular integral" sign`,
`"Schur-Horn" "Gaussian" "sign" integral`, `"validated quadrature"
"parameter" positivity derivative`, and `"Petras" integration piecewise
analytic discontinuities parameter`. No matching signing theorem was
located or inspected. The Petras (2002) and Moczurad--Zgliczynski
(2016/2017) piecewise-analytic/complexity papers were search leads only;
their full theorems were not inspected and are not inputs or efficiency
guarantees. The DLMF Cauchy-derivative formula's separate encoded resource
failed to load; it is not needed or used because (17) and the real
Leibniz formula suffice. There is no essential source blocker.

## Duplicates, failures and the changed test

Step 175's floating screen has both signs across phase and covariance
scales; it neither signs A nor certifies two opposite conditional means.
Steps 188--190 integrate joint prime/angle range boxes. Step 190 retains
only [-.194,.114], missing its .75 width-ratio threshold. Their stopped
joint-subdivision implementation is not reopened.

Step 192 removes Euler sampling but its independent coefficient/moment
boxes fail: every node/coefficient interval contains zero and 27 raw
nonconstant moment boxes cover [-1,1]. Its final width is 5.24030 against
.229997 required. The proved entire continuation in that attempt is a
reusable input, not evidence that A has a sign. Reusing its node ranges
and applying a derivative estimate alone cannot manufacture a sign.

The new mechanism integrates the signed angular function directly at
fixed response scales with a higher-order, validated cell integral;
it performs no high-degree moment expansion and no prime-angle search.
An observed sign at a few scales is only a guide until certified.
Even a certified sign change within the full enclosing interval would
reject only this stronger uniform-sign condition: a tested scale might
lie outside the actual response support, and I could still be nonzero.

## One bounded mathematical attempt approved

The following are future proof obligations and work limits, not results
of this LITERATURE turn. Preserve the exact target text above.

- Start with the two rational endpoints and their rational midpoint.
  Seek certified A values using branchwise quadrature, retaining all
  three states, source constants, normalized cell masses and complete
  unresolved-neighborhood ranges. An absolute radius of 1/10000 is a
  requested initial goal, not a proved attainable error or a required
  mathematical sign magnitude. Do not count ordinary samples as evidence.
- Within a total cap of 262144 integrand/selector/derivative callback
  evaluations, allow at most 65 response centers and 4096 angular leaves
  per integral, with at most 160 decimal places. Count preliminary tests,
  failed branch checks and derivative evaluations. Allocate at most the
  first 65536 callbacks to the initial three-center feasibility test.
  If it certifies no strict point sign, stop this attempt as inconclusive;
  the old all-zero-containing ranges alone do not justify another mesh run.
- If a point sign is obtained, certify a first g-derivative enclosure on
  every response slab used for transport, by differentiating (17) with
  its proved domination and validated real arithmetic. Show the derivation
  in the mathematical attempt. A crude whole-range bound is allowed, but
  its actual transport error must fit the margins; no adequate constant
  is assumed by this review. Angular second derivatives are required only
  for the trapezoidal option and only on its certified strict cells.
- Cover the whole rational interval by at most 256 closed slabs. On each,
  record its center value interval, a valid sup |A'|, the slab radius and
  the resulting mean-value error. Success requires all transported
  intervals to have the same strict sign, with an explicit positive
  common rational margin. Account separately for arithmetic/constant,
  strict-cell quadrature, unresolved-angle and g-transport errors.
- Stop immediately if two certified A values have opposite strict signs;
  retain their complete certificates as a refutation of this uniform-sign
  target, without claiming a sign of I. Otherwise stop on uniform signing
  or the stated cap. Unresolved intervals are inconclusive, not zeros or
  a proof of sign change. Do not restart the stopped Euler-box or joint
  prime-angle implementations when the budget fails.

This is SPECIALIZE: import the standard error and mean-value theorems;
justify only the literal selector, derivative and arithmetic differences.
No general quadrature theorem needs a reproof. A future implementation
must write its complete certificate to disk and inspect all load-bearing
coverage and error checks, not just a summary. This review produces no
new lemma, calculation or sign, and makes no originality claim. Full
matching Mathlib coverage for this selector-specific certificate is not
checked; the existing L426 coverage qualifications remain unchanged.
