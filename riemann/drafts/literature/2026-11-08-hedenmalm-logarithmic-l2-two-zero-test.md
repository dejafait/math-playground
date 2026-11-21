# Explicit logarithmic L2 metric: completed source coverage

TARGET: Test whether the logarithmic L2 form makes Hedenmalm's pair symmetric on the span of the first two positive real-zero functions, by rigorously bounding the off-diagonal L-image Gram entry.
CHECKED: 2026-11-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step149 searched the exact identifier/title with logarithmic L2, orthogonality, Gram and normalization, plus certified zeta-zero and rigorous-integration terminology; inspected the primary sources below and reused the ready pair/domain reviews and two local stops. No matching evaluation of this Gram entry was found among inspected sources; no novelty inference.
SOURCE_EVIDENCE: Hedenmalm arXiv:2606.17494v1 PDF pp2-8, (1.2.3), (2.2.1)-(2.2.2), (3.3.2), Theorem3.3.3, Definition4.2.1 and Theorem4.2.2/both proof cases; L018-L020 and audited L906/L907; Arb2.23.0 acb_dirichlet Riemann zeta function zeros and acb_calc Integration/Local integration algorithms; Johansson arXiv:1802.07942v1 Sections2,2.1,3.2,3.3; Arias de Reyna (2012) Section2, Theorem2.1 and both index-range cases, pp104-107. Exact links and limitations below.
COMPARISON: Known results supply the conditional orthogonality requirement, endpoint starting estimates, indexed zero isolation/counting and certified finite-interval integration. They do not evaluate this logarithmic L2 Gram entry. The necessary specialization is normalization reconciliation, explicit L-image/tail bounds and an interval implementation propagating root uncertainty; no new spectral theorem or reproof of the standard algorithms is warranted.
GAP: The source coverage gate is complete for this bounded specialization, but its mathematics remains unperformed: reconcile the printed Mellin prefactor with L018-L020; certify the first two roots; prove L-image L2 convergence; enclose the complete off-diagonal integral including every tail and numerical error.
REASON: Approve the unchanged step148 nomination for one mathematical attempt next turn. This turn only checks sources and applicability; it neither derives the specialization nor certifies any Gram value. The prior positive-pair and enlarged-domain stops remain scoped and intact.
LITERATURE_REASON: The REVIEW_REQUIRED nomination introduces an explicit metric, indexed certified roots and improper Gram integration outside the ready finite-span audit scope; these essential sources are inspected once here.
SCOPE: The exact TARGET, using only the source w,D,L,u_alpha, the first two distinct positive real zeros, and measure dt/t. Covers deriving the identified normalization/convergence difference and one certified Gram test from the cited inputs next turn. Does not cover any changed weight, nonlocal metric, generalized eigenfunction, completed space or all-zero symmetry.

## Original step148 nomination and its limits (historical)

Use the exact w,D,L,u_alpha and complex zero set of L907. Let alpha_1
and alpha_2 denote the first two distinct positive real zeros of that
source's Xi, to be rigorously identified rather than inserted as
rounded decimal ordinates. The proposed form on L-images is

\[
\langle f,g\rangle_2=\int_0^\infty f(t)\overline{g(t)}\,\frac{dt}{t},
\qquad
\Gamma_{12}=\int_{\mathbb R}(Lu_{\alpha_1})(e^x)
                  \overline{(Lu_{\alpha_2})(e^x)}\,dx.
\]

These are definitions of a candidate, with convergence still to be
checked. Hedenmalm Theorem4.2.2(b) makes exact orthogonality a necessary
test for the proposed symmetry at two distinct real zeros. A rigorous
complex enclosure excluding zero would reject this specific metric
on the actual spectral domain. An enclosure containing zero is
inconclusive; numerical smallness is not orthogonality. Retain the
candidate for further development only with an exact identity or
other decisive evidence after the source review. No conclusion is
derived in this nomination, including about the sign of Gamma_12.

This target could distinguish a usable baseline metric from a need
for a different weight or nonlocal form. It tests actual L-images,
not an enlarged domain whose relation to H_finite is unknown. A
negative answer leaves other metrics open. Even exact success on
this block would leave all complex-zero functions, full symmetry,
completion and actual-Xi mixed positivity unresolved. Restricting
the diagnostic to two known real zeros does not restrict the eventual
RH criterion to real zeros.

Essential local inputs are L906 and L907; L019/L020 are only prospective
normalization-comparison inputs if the next review establishes their
necessity, and have not been read for this nomination. No cross-notebook
input is planned. The source's printed small-t estimate and an unverified
Mellin constant may not replace the required endpoint reasoning. Use
primary zero-certification results and distinguish approximate labels
from certified roots. Full and supporting Mathlib coverage is unchecked.

This is a routine metric specialization/obstruction test, not yet a
justified creative construction. No independent mechanism cancelling
the symmetry defect has been supplied. The next turn is source
comparison for this exact target; it must not carry out an uncovered
calculation or approve and prove the target in the same turn.

## Separate source approval, 8 November 2026 (step149)

The historical nomination above is preserved; its pending-review language
is superseded by this approval. The TARGET has not changed. No new lemma,
mathematical script, root certificate, convergence result or Gram bound
was produced in this literature-only turn.

### Primary inputs inspected

1. Hedenmalm, *Spectral interpretation of Riemann zeta zeros*,
   [arXiv:2606.17494v1 PDF](https://arxiv.org/pdf/2606.17494v1),
   submitted 16 June 2026; corresponding
   [HTML](https://arxiv.org/html/2606.17494v1).
   Read the defining coefficients (1.2.3), Mellin/xi conventions
   (2.2.1)-(2.2.2), integral/ODE (3.3.2), complex boundary statement,
   finite span, Definition4.2.1 and both Theorem4.2.2 proof cases.
   Part(b) assumes the pair symmetry and distinct real roots, then
   substitutes the eigen-equations to require orthogonality. It does
   not select a measure or supply an unconditional Gram identity.
   The complex boundary proof is omitted; it is not needed as an
   unaudited integral estimate for this real two-root diagnostic.
   Retain w exactly as defined by (1.2.3). Its coefficients and those
   of local L019, with L020's half-line cosine convention, require
   reconciliation before (2.2.1) can be used numerically. A corrected
   transform constant is not asserted here. The defining series and
   exact inversion, rather than the printed small-t bound, govern
   future endpoint reasoning. The full positive-metric import stop
   remains effective.

2. Frozen **Arb2.23.0 manual**, [acb_dirichlet, Riemann zeta function
   zeros](https://arblib.org/acb_dirichlet.html#riemann-zeta-function-zeros).
   Read the isolation, refinement, indexed-zero and total-count
   specifications, including the low-index range 1<=n<=126 of the
   Gram isolation routine. The public indexed routines require n>=1;
   n=1,len=2 is within scope. The total-count routine counts positive
   imaginary parts through t, with multiplicity, rather than only
   detected line sign changes. Use returned balls and integer counts,
   not rounded decimal labels. No global RH or simplicity assumption
   is supplied by this review. A future certificate must retain the
   actual isolating intervals, finite disjoint balls, indexing/count
   evidence and precision/library versions. APIs are assessed here,
   not executed. For extra direct verification, sign brackets and
   exact total counts at surrounding rational heights can be checked.
   No such values have been computed in step149.

3. Arias de Reyna, *Programs for Riemann's zeta function*, in
   *Leven met getallen*, CWI (2012), pp102-112,
   [primary full text](https://ir.cwi.nl/pub/19724/19724D.pdf),
   Section2 pp104-107. This reference was followed from the Arb manual.
   Read Theorem2.1 and the algorithm's small-index/table and
   large-index/counting cases, including the Rosser-exception fallback.
   The theorem requires consecutive Rosser blocks satisfying Rosser's
   rule and K>=0.0061(log g_p)^2+0.08 log g_p, and concludes
   N(g_n)<=n+1 and N(g_p)>=p+1; it also records Trudgian's alternative
   bound. The surrounding-block argument obtains exact counts before
   labeling an isolated zero. Gram's law alone is not a universal
   counting theorem. The paper explains an mpmath algorithm; its
   floating-point examples are not interval certificates. We import
   the Arb implementation contract, not those decimal outputs or an
   unverified reimplementation of Turing's method. Brent/Trudgian full
   papers are further leads, not independently inspected inputs here.

4. Johansson, *Numerical integration in arbitrary-precision ball
   arithmetic*, [arXiv:1802.07942v1](https://arxiv.org/html/1802.07942v1),
   22 February 2018; ICMS2018, LNCS10931, pp255-263.
   Read Section2's complete direct-enclosure/analytic-quadrature/
   bisection algorithm, Section2.1 tolerances and stopping limits,
   Section3.2 improper tails and Section3.3 complex-extension caveat.
   The callback must enclose every value on the input ball, and in
   analytic mode verify holomorphy there. A finite-segment integral
   is certified by the returned ball, not by its requested tolerance.
   Infinite endpoints require manually proved tails. Direct complex
   conjugation is not holomorphic; a valid analytic continuation of
   the real-axis integrand, or direct real interval integration, is
   required. These conditions apply also to any inner primitive
   evaluation. No complexity promise or automatic tail theorem for
   this Gram integrand is imported.

5. Frozen **Arb2.23.0 manual**, [acb_calc Integration and Local
   integration algorithms](https://arblib.org/acb_calc.html#integration).
   Read callback order0/order1 contracts, bounded finite-path
   hypotheses, return codes, tolerance qualification and ellipse bound:

       error <= 64 M / (15 (rho-1) rho^(2n-1)),  rho>1,

   for an n-point Gaussian rule on [-1,1], when f is holomorphic
   and bounded by M in the ellipse with foci +/-1 and semiaxes
   X,Y=sqrt(X^2-1), rho=X+Y. Read the affine scaling prescription
   as well. These are sufficient standard quadrature inputs; do
   not reprove them. Every bound for the particular integrand and
   every rounding, parameter and infinite-tail error remains local
   work. Near-zero values require an actual final enclosure test;
   a success code alone does not prove a requested global radius.
   The underlying Trefethen2008 reference was identified but its
   full paper was not read; the imported contract is the manual's
   displayed bound, supported by Johansson's algorithm description.

Current FLINT3.7.0-dev documentation was also compared, specifically
[zero isolation](https://flintlib.org/doc/acb_dirichlet/zeta-zeros.html)
and [integration](https://flintlib.org/doc/acb_calc/index.html).
These pages carry an October2026 generated-text warning. They are
supporting comparisons; the original paper and frozen Arb manual
above govern coverage. The GitHub source link inspected resolved to
an interface header, not the implementation; no code audit is claimed.
The attempted obsolete /acb_calc/integration.html URL was inaccessible;
the complete frozen manual resolved that access issue. There is no
persistent essential source blocker.

### Duplicate and failure comparison

Exact-path reads covered L906/L907, L018-L020, the ready operator-pair
assessment, the ready critical-audit assessment, and
ATTEMPTS/2026-11-08-hedenmalm-positive-pair-import-stop.md and
ATTEMPTS/2026-11-08-hedenmalm-enlarged-domain-inverse-stop.md.
L907 removes finite-span ambiguity only. L906 refutes a different,
enlarged V prescription. Neither evaluates this two-root Gram entry.
The earlier positive-realization import failed because symmetry and
definiteness were assumed. Here the measure is explicitly specified
and can be rejected on an actual two-root block; that is a different,
independently testable obligation, not a reopened automatic import.

Queries included `Hedenmalm "2606.17494" logarithmic L2 orthogonality`,
`"2606.17494" "orthogonality"`, the exact title with `L2` and
`inner product`, `"2606.17494" "Gram"`, the exact title with
`normalization`, and certified zeta-zero / Johansson integration
terminology. Returned secondary summaries and unrelated spectral
proposals are leads only. No inspected theorem supplies this exact
Gram entry or its nonvanishing. Failed search does not establish
novelty. The initial oversized notebook-local search was replaced by
Hedenmalm-specific paths and exact canonical reads; no conclusion
uses its truncated output. No sibling notebook was read.

### Approved specialization and discriminating test

The exact TARGET is approved as **SPECIALIZE**, with prospective
classification **REPRODUCTION**. Standard zero isolation and rigorous
quadrature are imported by citation; only the identified application
work is justified. Perform these obligations within one coherent
mathematical attempt, preserving partial work if the test is not
completed:

- Establish the exact source-kernel/local-Xi normalization from
  L018-L020 and (1.2.3), checking the full-line versus half-line
  convention and a nonzero transform factor. Do not silently replace
  the source w or assume the printed (2.2.1) constant. Then justify
  that the certified zeta roots are the intended alpha labels and
  that the full Mellin integral vanishes at those exact roots.
- Certify the first two positive real roots with an indexed rigorous
  routine, disjoint enclosures and count/index evidence. Propagate
  the entire root balls through every subsequent bound. A midpoint
  is not an exact zero. Do not extend a root identity to all nearby
  parameters when using an upper-tail representation of u_alpha.
- Starting with L906's complete series/inversion estimates and
  L907's integral identity, prove L-image square integrability and
  absolute cross-integrability. Control the logarithmic derivative
  w'/w with a positive denominator bound; rapid decay of w alone
  does not control its reciprocal. Keep both endpoint contributions.
- Enclose the finite central integral by a verified interval method,
  carrying the full theta-series remainder, primitive truncation,
  quadrature, root-parameter and arithmetic errors. Prove any
  holomorphic reflected-factor construction before analytic
  quadrature; raw conjugation of the integration variable is invalid.
  Add explicit full integral tails. Record all constants and returned
  bounds in a certificate, with a complete analytical justification.

Bound numerical refinement to an initial 128-bit pass and, only if
needed, one 256-bit pass with justified cutoffs and truncation degrees.
An exact analytic identity may instead settle the test. These are
work bounds, not an assertion that either pass will succeed. If a
prerequisite fails, record that precise obstruction and stop; do not
substitute a new metric in this attempt. If the complete final complex
enclosure excludes zero, reject this logarithmic L2 metric on the
specified real two-root span. If it includes zero, record inconclusive;
do not promote smallness to exact orthogonality or indefinitely tune
precision. Exact orthogonality would pass this block only.

Essential local inputs are L018-L020 and audited L906/L907. No
cross-notebook result is required. Full matching Mathlib coverage for
this metric/Gram test and supporting interval-integration coverage
remain unchecked; no absence is claimed. All-zero symmetry, a positive
completed realization and actual-Xi mixed positivity remain unresolved.
No concrete new mechanism paying that central symmetry obligation was
found, so this baseline test is not labeled creative. After this
separate source approval, unchanged coverage should be reused for
mathematics rather than another literature turn.
