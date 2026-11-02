# Spatial signed-sum enclosure — source comparison

TARGET: Assess source coverage for a carrier-centered signed finite-sum enclosure of the L495 moving-cutoff increment on [X,4*pi*(691260^2-t/16)] at t=.16836, using joint logarithmic weights and explicit spatial derivative bounds to test the full two-charge r0 budget on whole cells.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared primary Taylor-model containment and interval Taylor/automatic-differentiation results; exact queries, inspected ranges, narrow duplicate search and retained failures are recorded below. No search establishes originality.
SOURCE_EVIDENCE: Makino–Berz (2003), publisher PDF, Definitions 1–3, 4–7, Theorem 3 and Algorithm 1; Lin–Stadtherr REC 2006 Section 2 equations (1)–(7); Johansson arXiv:1611.02831v1 Sections V/V-A and VI; official FLINT power-series contract and Mathlib Taylor statements inspected as specified below.
COMPARISON: Known finite-code-list containment and explicit Taylor remainders cover a bounded signed spatial enclosure procedure, but supply neither a favorable numerical bound nor a complexity guarantee for this block. C499d's exhausted curvature/absolute-tail envelope is a different estimator.
GAP: Carrier reconstruction, every required whole-cell derivative enclosure, joint finite sums, canonical cutoff equalities and the strict full r0 comparison remain uncomputed; source coverage is not a uniform exclusion theorem.
REASON: Permit only the capped known-method specialization below after separate supervisor approval of this changed assessment; no new cancellation theorem or mathematical calculation was performed in this review.
LITERATURE_REASON: The proposed next technique requires essential unread effective spatial-enclosure inputs outside the approved derivative-in-index curvature/absolute-tail scope.
SCOPE: Only the exact covered capped procedure; t=.16836, X=6000284561421.5, n=691004, N=691260, exact nu, q(x), P={primes<=307}, ell0, r0 and full L494 epsilon_1; preserve L494/L495/L496/L499 and C499c/C499d qualifications.
COVERED_TARGET: Test the carrier-centered signed L495 increment on [X,4*pi*(691260^2-t/16)] at t=.16836 with degree-16 interval Taylor enclosures, at most 65536 enclosure evaluations and 2^28 scalar interval operations, retaining both uniform charges and requiring total cost<r0 on every cutoff cell.

The following original nomination records the pre-review state. The
completed comparison below supersedes its missing-coverage statements;
it does not assert a successful enclosure.

The main gap remains actual-Xi all-degree signs and uniform collision
exclusion. This candidate would only provide a qualified finite spatial
interval at one positive time. It is not a proposed central all-height
creative mechanism. Later intervals, other times, H1, zero time and source
audits remain independent. No cross-notebook input is proposed.

The source review should compare rigorous finite exponential-polynomial
enclosures, frequency centering and derivative-controlled interpolation
against the existing finite Abel/curvature input. Locate exact effective
primary hypotheses and check whether joint control of the primitive and
log-weighted sum is available with every finite prefix/cutoff convention.
Do not infer a uniform result from endpoint samples. Whole-cell derivative
control, both charges and full resultant reconstruction remain necessary.

Continuation test: approve only a concrete finite procedure with explicit
error bounds and a fixed resource/partition budget that can test
B_unif+U_s,unif+U_r,unif<r0 on the entire prescribed interval. If no
controlled effective procedure is identified, park this nomination; do
not renew the exhausted curvature envelope or start adjacent endpoint
certificates. This file supplies no ready mathematical coverage.

## Completed source review — 2026-11-01

This is literature-only. No carrier identity, derivative specialization,
new bound, lemma or mathematical script was derived. The exact TARGET
was retained. SPECIALIZE covers only the exact COVERED_TARGET and its
finite procedure below, subject to separate approval next turn.

### Primary inputs and scope

1. K. Makino and M. Berz, *Taylor Models and Other Validated Functional
   Inclusion Methods*, International Journal of Pure and Applied
   Mathematics **6**(3) (2003), 239–312 as printed on the
   [publisher PDF](https://www.ijpam.eu/contents/2003-6-3/1/1.pdf).
   Inspected Definitions 1–2 and required cases of Definition 3
   (pp.243–249), intrinsic remainder cases
   exp/log/inverse/square root/sine/cosine/arctangent, Theorem 1 and
   proof (pp.249–250), Definitions 4–7 and addition/product error accounting
   (pp.253–257), and Theorem 3 with complete proof and Algorithm 1
   (p.258). Theorem 3 assumes an enclosure Pf+If on D and a finite
   elementary/intrinsic code list g defined on its enclosure range.
   Executing g in admissible floating-point Taylor-model arithmetic
   encloses g composed with f on D. The proof is induction through
   the code list. Algorithm 1 evaluates the identity model, then the
   code list, then bounds the polynomial and adds its remainder.
   Positivity/nonzero restrictions on intrinsic domains, discarded
   high-degree terms and rounding errors must be charged. The scaling
   theorem is asymptotic, not an effective cost or accuracy guarantee
   here. No COSY implementation is assumed installed or audited.

2. Y. Lin and M. A. Stadtherr, *Validated Solution of Initial Value
   Problems for ODEs with Interval Parameters*, REC 2006,
   [author manuscript](https://academicweb.nd.edu/~markst/lin-stadtherr-rec06-v2.pdf),
   Section 2.1–2.2, pp.2–4, equations (1)–(7), inspected completely.
   Equation (3) is the finite Taylor formula with a derivative remainder
   at an intermediate point; equation (4) specifies the multivariate
   differential operator. Use the one-real-variable case, separately
   for real and imaginary components. Assume C^17 on an open
   neighbourhood of each closed cell, stronger than the displayed
   differentiability assumptions. Equations (5)–(7) retain addition
   and multiplication dependence in the polynomial and bound the
   discarded product terms. This provides an explicit alternative:
   degree-16 coefficients at a centre, and the order-17 coefficient
   enclosed throughout the cell. A shared intermediate point for
   complex components is neither asserted nor needed. ODE existence
   and all later numerical examples are outside the inspected scope.

3. F. Johansson, *Arb: Efficient Arbitrary-Precision Midpoint-Radius
   Interval Arithmetic*, [arXiv:1611.02831v1, 9 November 2016](https://arxiv.org/html/1611.02831v1),
   Section V/V-A and Section VI's power-series discussion inspected.
   Set containment includes propagated and arithmetic errors; V-A's
   derivative error bound uses a supremum on the whole input interval,
   not only the centre. Finite approximation and truncation error are
   separate charges. The source supplies a ball-arithmetic contract,
   not a proof of a favorable range or automatic high-precision remedy
   for dependency loss. Timings and examples are not used as evidence.

4. Official FLINT documentation, *Power series and Taylor expansions*,
   [primary repository text](https://raw.githubusercontent.com/flintlib/flint/main/doc/src/arb_poly/power-series.md),
   inspected 2026-11-01, lines 5–21 and 85–103. Series functions compute
   coefficients modulo the requested length, with rigorous coefficient
   error bounds. A ball constant term encloses coefficients at every
   centre in that ball. The documented nonzero/positive constant-term
   conditions must hold. This supports interval automatic differentiation
   for the remainder coefficient; a truncated polynomial alone still
   does not certify a function range. This is a mutable main-branch
   contract, not evidence about the locally installed version: pin and
   record the actual backend if used. The initially attempted legacy
   documentation URLs returned access errors; this inspected primary
   replacement removes the source-access blocker. No library installation
   is authorized or needed by this review.

5. [DLMF 4.21.2–3](https://dlmf.nist.gov/4.21#E2), sine/cosine addition
   formulas, inspected. They cover exact real phase centering; they
   supply no cancellation estimate. Carrier reconstruction is an
   application obligation for the later calculation, not a new identity
   proved or approved here.

### Local comparison, failure reuse and searches

Read L495's definitions and proof Sections 1–4, C499c Sections 1–3,
and C499d Sections 1–4. C499c supplies the complete factored finite
increment, actual phase convention and Euler/logarithmic interface.
Its favorable endpoint enclosure cannot be interpolated. C499d supplies
the closed-domain and independently uniform charge interfaces, with
its existing audit qualifications. Its failed envelope exceeds r0;
that is not a lower bound on the actual increment.

The narrow search covered these C499 files, the November 1 phase-sensitive
and uniform-resonant literature assessments and heat working notes, and
the named failure records. No duplicate whole-cell signed enclosure was
identified within that scope. The earlier assessment's comparison with
explicit derivative/Abel and endpoint-transform bounds is reused rather
than re-browsed. C499d's curvature/absolute-tail failure and the complete
September 13 smooth-cutoff-absolute-variation, total-frequency-cutoff-
derivative and block-mean-square-cutoff-inference stop records were read.
Their uncontrolled cutoff derivatives and moment-only inferences remain
excluded. No sibling notebook or cross-notebook input was read.

Queries included `Taylor models Makino Berz remainder bounds interval
arithmetic Taylor model elementary functions`; `Arb Taylor polynomial
interval rigorous enclosure exponential series`; `"carrier" "exponential
sums" "interval arithmetic"`; `"finite exponential sums" "Taylor models"`;
and `rigorous exponential sums logarithmic weights interval Taylor
enclosure`, plus primary FLINT and Mathlib Taylor searches. Exact carrier
queries did not locate an inspected ready numerical theorem for this
block. Search leads about matrix exponentials, exponential-sum size and
unrelated multiplicative sums were not inspected or used. No novelty
claim follows. The strongest inspected relevant conclusion is general
effective finite-expression containment, not the requested strict budget.

### Concrete capped procedure and remaining application obligations

The following is a proposed implementation specification, not a
mathematical derivation or a claim that the cap suffices.

* Retain exactly t,X,n,N,P, nu, the Euler product, actual ell, ell0,
  full epsilon_1 and rational r0 from C499c/C499d. Inputs are C499c,
  C499d, L494–L496 and L499, with L497/L498 only through accepted
  old mass. Reuse that mass; do not replay the coefficient ledger.
* Partition at every exact cutoff entry, treating q as fixed on each
  piece. Enclose whole closed supersets of the half-open cells, with
  the right endpoint of each comparison still using that piece's fixed
  index. Explicitly test every entry with its canonical NEW index and
  the singleton Y with N. Symbolic pi-dependent endpoints require
  outward enclosures; rounded endpoints may not leave a gap. No
  derivative of q is taken. Empty sums must be exact zero.
* Use one real local coordinate and shared degree-16 polynomial data
  for the primitive and log-weighted increments. Centre the primitive
  phase at a fixed log-frequency in the block, and account for restoring
  that carrier, its phase and all logarithmic factors in C499c's exact
  finite expression. Verify the finite algebra before using it. Enclose
  order-17 derivatives on the entire piece, via interval automatic
  differentiation or the cited admissible remainder arithmetic. Bound
  the resulting polynomial range plus its remainder. Do not replace
  the shared signed polynomials by independent termwise modulus sums
  before the designated finite combinations. Any conservative Euler
  or phase overenclosure must be an explicit valid inequality.
* Check smoothness and all denominators/real intrinsic domains on each
  enclosing piece; L496's nonvanishing and ell floor are supporting
  inputs, not permission to divide by a zero-containing interval.
  Use exact rational or certified outward ball arithmetic. Keep large
  phase-reduction errors and derivative remainders, even if they make
  the bound useless. Formal-series coefficients alone are insufficient.
* Use deterministic bisection within fixed-cutoff cells, degree 16,
  initial 256-bit outward arithmetic and at most one 512-bit replay
  when arithmetic width is the identified bottleneck. Limit total
  enclosure evaluations, including boundary cases and any replay, to
  65536, depth to 16 per original cell, and scalar interval operations
  to 2^28 (count or conservatively bound coefficient operations).
  Save partial reasoning/certificates before the expensive run. These
  are hard resource ceilings, not a complexity promise from a source.
* Import or explicitly replay C499d's separately uniform U_s and U_r
  inequalities with their original qualifications; do not use the
  small signed increment to reduce the absolute log-support charge.
  Preserve both saddle corrections, rho, product derivative, full
  entering-pair epsilon_1 and old-model lower bound. Test the strict
  total against the exact r0 on every piece; report actual/required
  bounds, any failure and the certificate path. No sampled endpoint
  or partial covering establishes the result.

Success would provide only a qualified finite positive-time interval.
On exhaustion or an overlarge sufficient envelope, save the failed
pieces and distinguish INCONCLUSIVE/ENCLOSURE_FAIL from any certified
lower bound for the actual cost. Neither constitutes a heat collision
or RH counterexample. Park this precise capped estimator rather than
renew it with more precision, cells or adjacent endpoint tests without
materially new evidence and fresh scope. No asymptotic all-height or
zero-time transfer has been supplied. This is routine specialization,
not a justified protected creative attempt at the central gap.

### Mathlib

The primary [Mathlib.Analysis.Calculus.Taylor documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Taylor.html#taylor_mean_remainder_lagrange)
was inspected, including the full statement of
`taylor_mean_remainder_lagrange`: distinct real centre/point, ContDiffOn
through order n on the unordered closed interval and differentiability
of the n-th iterated derivative on its interior imply the Lagrange
formula. This is supporting real-component Taylor coverage. Full
matching coverage for the heat resultant, shared signed enclosure,
cutoff implementation and certificate is unchecked; no formalization
or independent implementation audit is claimed.
