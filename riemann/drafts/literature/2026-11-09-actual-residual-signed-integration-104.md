# Actual common-residual integration — completed source comparison

TARGET: Test whether signed evaluation of L948's actual common-residual response J_p(k-p;8), with a complete integration error and unchanged second-order remainder, can certify v(8)>0.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step105 checked assessment102, response assessments87/92, direct-density notes68, stop69, L952 and its stop/history; searched certified singular-weight quadrature, Gauss-Jacobi/Gauss-Chebyshev analytic error and exact signed-theta response terms. Primary method statements and proof cases inspected are identified below; no matching actual endpoint-sign theorem was inspected and no novelty is inferred.
SOURCE_EVIDENCE: NIST DLMF3.5.18-20_1,22-23,26; Trefethen ATAP Chapter8 author source, Theorems8.1-8.2 and proofs; Johansson arXiv:1802.07942v1 Sections2,2.1,3.2. Reuse assessment102's complete Taylor/beta coverage and L938's analytic ellipse/theta inclusion; details and qualifications below.
COMPARISON: Known positive weighted Gaussian quadrature and analytic polynomial approximation cover a finite signed-integral test; ordinary Arb integration alone does not cover the unbounded endpoint. L952's stopped uniform-norm allowance remains evidence. No source guarantees a favorable sign, accuracy at the fixed precision or feasible execution cost.
GAP: Derive and execute the specified fixed weighted-rule specialization, enclose actual residual values and all signed cancellation, pay analytic quadrature error, every omitted response degree and unchanged L948 remainder, then compare in actual-density units. None of these new numerical bounds or the actual endpoint sign is established here.
REASON: Essential primary method coverage is complete for one later REPRODUCTION calculation with the finite error prescription below, subject to separate approval of this newly completed assessment. This is source-scope preparation, not new mathematics or a sign theorem.
LITERATURE_REASON: Changed mechanism from a uniform absolute residual norm to signed evaluation of the actual common residual; the missing weighted-quadrature and cancellation cases required this literature-only step.
SCOPE: One fixed E=8 calculation; original p,257 interpolation nodes,theta8,precision200,grid10^-120 and full epsilon unchanged; one 4096-node first-kind Gauss-Chebyshev integration rule, ellipse parameter3/2, signed response prefix J=1411 and L952's complete pointwise complement; no parameter campaign or interval/tail claim.
COVERED_TARGET: Test whether signed evaluation of L948's actual common-residual response J_p(k-p;8), with a complete integration error and unchanged second-order remainder, can certify v(8)>0.

## Original nomination — preserved, superseded by the completed comparison

Main gap remains L030-L032/C032a actual-Xi all-degree mixed positivity.
This independently testable local input would only decide the endpoint
obstacle of the density route. It supplies no interval, infinite join,
outer negative-mass budget or independent all-degree signs. It is not
nominated as a new central creative mechanism.

Essential inputs are L938's actual full-theta kernel, unchanged p and
epsilon, all34 rows/twelve factors/factorials/M_0^12; L948(1),(4)-(5);
C948a's exact response prefixes and full-degree complement obligations;
L952's exact full polynomial endpoint and remainder. Preserve inherited
theta, polynomial, prefix and arithmetic contracts. No cross-notebook
input is proposed. Mathlib unchecked.

Review exact primary hypotheses for a certified signed integral with
the integrable beta singularity, actual theta values and subtraction
of the fixed polynomial. First search these specific local mechanisms
and failures, including stop69, L952 and assessment102, before external
source extraction. A generic quadrature theorem or unqualified floating
subtraction does not establish feasible accuracy. No actual residual
sign, independence, integrated-to-pointwise transfer or analytic absolute
value may be assumed. Preserve the fixed kernel/node/cutoff/precision/grid;
any changed mathematical scope needs a new gate, not automatic refinement.

Approve a concrete later calculation only if complete source coverage
and a finite error prescription permit comparison of v_p(8)+J_p(k-p;8)
against the full L948 remainder in actual-density units. Record overlap
with ready known methods as import/specialization rather than originality.
If a primary hypothesis or complete error case is missing, park this
dependent target; do not repeat a norm-bound or access-retry campaign.

## Completed comparison — step105, 9 November 2026

LITERATURE / NOVELTY_UNCHECKED / EXPLORATION; actual task type
literature_comparison. No lemma, mathematical script, quadrature value,
new integration identity or specialized error bound is produced.

### Relevance, local evidence and source search

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. The intermediate target is only the actual v(8) sign.
A positive enclosure would remove one endpoint obstacle to a proposed
positive tail starting at8. It would not prove positivity on an interval,
an effective infinite join, an integrated negative-mass budget or any
independent mixed sign. A negative enclosure would reject that proposed
pointwise tail, without refuting RH or the integrated route.

Read L938's full row table and(5)-(18), L019's kernel, L948's complete
response/remainder and beta-face argument, C948a's prefix/complement
construction and L952's complete pointwise test. Reuse assessment102
and assessments87/92 for unchanged calculus and coefficient methods.
Read direct-density notes68's integration comparison and search record,
stop69 and L952's stop/history. Notes68 already inspected Johansson:
it is reused for its established scope, with the singular and tolerance
cases reopened for this changed application. No certificate is rerun
or claimed independently verified in this turn.

Stop69 concerns the coarse E=4 rowwise allowance. C948a succeeds for
an integrated replacement budget. L952 fails at E=8 with its fixed
absolute prefix norm. These have different quantifiers and none settles
the actual signed residual response. The new test must keep that
response signed through quadrature; returning to epsilon times the
same prefix norm would merely repeat L952. Its complement and complete
second-order remainder remain valid payments, with their contracts.

Queries included `certified quadrature algebraic endpoint singularities
ball arithmetic Petras Johansson integration`, `Gauss Jacobi quadrature
rigorous error bound derivative algebraic endpoint singularities`,
`Gauss quadrature analytic function Bernstein ellipse positive measure
error bound`, `Gauss Chebyshev quadrature analytic Bernstein ellipse
error bound rho 2n author pdf`, and the exact combinations `Riemann
theta signed convolution quadrature` and `kernel first variation signed
Gauss-Chebyshev residual`. The latter returned no inspected theorem
for this density. Public notebook extracts and unrelated search hits
are not independent mathematical evidence. No novelty is inferred.

### Primary theorem scope actually inspected

NIST DLMF, live edition inspected9November2026, release identifier not
independently checked: [3.5.18-20_1](https://dlmf.nist.gov/3.5#E18)
give positive Gaussian weights and exactness through degree2n-1;
[3.5.22-23](https://dlmf.nist.gov/3.5#E22) give the first-kind
Chebyshev weight and explicit cosine nodes/equal weights;
[3.5.26](https://dlmf.nist.gov/3.5#E26) requires both Jacobi
exponents greater than-1. The actual beta parameters satisfy this
condition. The derivative remainder is not selected: it would require
a full high-order derivative bound, not a finite-rule difference.
For the proposed Chebyshev specialization, the integer extra power
in the beta weight belongs in the amplitude. Its exact affine factors
and normalization must be justified in the later application.

L. N. Trefethen, *Approximation Theory and Approximation Practice*,
Chapter8, [author's executable chapter](https://raw.githubusercontent.com/chebfun/ATAP/master/chap8.m),
master version inspected9November2026 (commit not independently pinned),
Theorems8.1-8.2, equations8.1-8.3 and proofs, source lines104-159:
analyticity in the open Bernstein ellipse and a bound M there give
Chebyshev coefficient decay and projection error at most
2 M rho^(-m)/(rho-1) at degree m. Read the annulus proof, including
its open-boundary limiting case. The source's sup norm is on[-1,1].
This supplies a quantitative polynomial approximation input; it does
not itself certify floating evaluation or this weighted endpoint sign.
The accessible 2010 sample lacks this theorem and is not substituted
for the inspected author chapter. General reproof is unnecessary.

Fredrik Johansson, *Numerical integration in arbitrary-precision ball
arithmetic*, [arXiv:1802.07942v1](https://arxiv.org/pdf/1802.07942v1),
22February2018, Sections2,2.1,3.2, printed pp2-4,6: reopened the
complete bisection/Gaussian algorithm, analyticity callback, evaluation
limit and singular-endpoint cases. It requires bounded integrands on
finite paths; unbounded endpoints need external treatment. Requested
tolerances do not guarantee achieved radii, especially under cancellation.
This excludes a bare call on L948's singular weighted integrand as a
complete certificate. No performance benchmark is a feasibility proof.
Its original Petras reference remains an optional unread lead.

The FLINT3.7.0-dev [integration API](https://flintlib.org/doc/acb_calc/index.html)
was read for comparison, including its bounded-path requirement and
caller-owned improper-integral handling. It discloses partial LLM
generation. No theorem or implementation guarantee rests on that page;
the versioned Johansson paper supplies the relevant obstruction.
The new method uses inherited directed Decimal contracts rather than
assuming an uninspected Arb evaluator. The newer Gauss-Jacobi analytic
error paper DOI10.1090/mcom/3977 was an optional lead: full text returned
403 and is not imported. No essential source remains blocked.

### One finite later test and complete error prescription

The exact TARGET is preserved. After separate approval, permit one
REPRODUCTION calculation, standard/high. Keep the original257
interpolation nodes; the4096 integration nodes are a distinct fixed
rule, not a replacement kernel or interpolation grid. No refinement
following an inconclusive result is approved.

1. Start from L948(5) at E=8. Use the standard first-kind weighted
   Gaussian rule after moving the extra integer power of the beta
   weight into the amplitude. The candidate amplitude is
   y^11 r(8(1-y)) Q_<=1411(8,y). Establish its exact weight/affine
   normalization and all external pi/8^17 factors in the research
   proof. This review does not assert a newly derived identity.
   Keep both endpoint neighborhoods in the weighted integral.

2. Reuse L938's analyticity and |k|<10^9 on its energy ellipse3/2,
   including the removable square-root issue at zero. For the affine
   image of the candidate amplitude, construct a finite rational upper
   bound M on the entire corresponding ellipse3/2. Use the complete
   exact coefficients of p and the retained signed response prefix,
   with finite absolute coefficient sums and explicit ellipse geometry.
   Do not extend the real residual bound epsilon to complex arguments.
   No complex theta-truncation assertion is needed: the full k bound
   is already an analytic input. A sampled ellipse maximum is inadequate.

3. Apply the imported projection theorem at degree8191. Use Gaussian
   exactness through8191 and positivity of all4096 weights to pay
   the approximation error on both the exact integral and the finite
   rule. The multiplier must include both complete weight masses and
   L948's external scale. The projection need not be computed. This
   is a finite prescription using named inputs; its specialized proof,
   exact constant and achieved size remain research obligations.

4. At every integration node, enclose L019's actual k with theta
   terms1..8 plus L938(14)'s complete omitted tail. Enclose node
   cosines, square roots, pi, exponentials, the unchanged rational p,
   every prefix coefficient, products, subtraction and the final signed
   sum by the inherited precision200 directed arithmetic. Node argument
   uncertainty must propagate through the entire evaluation. Do not
   replace k-p by a floating midpoint or assume relative accuracy after
   subtraction. Saved Bernstein intervals may be used only with their
   complete rounding inclusions; exact coefficients are also available.
   The actual finite-sum interval, not a requested tolerance, pays
   cancellation. Any nonfinite operation or insufficient enclosure is
   reported as a failed fixed test; precision is not increased.

5. Pay every response degree1412..2816 using L952's existing pointwise
   complement, full epsilon and correct pi factor. Retain its(l+17)!
   normalization and ratio256/1430; the integrated C948a allowance is
   not a substitute. Add L948(1)'s full second-order remainder at8,
   exactly as already bounded in L952(8)-(9). Reuse the complete
   L952(10) polynomial endpoint, with its enclosing pi factors and
   execution qualifications. No high-degree response term or higher
   replacement term is dropped or estimated from an observed prefix.

6. Assemble v_p(8) plus the signed quadrature interval and all three
   separate payments: analytic quadrature error, pointwise response
   complement and complete higher-replacement remainder. Retain all
   finite evaluation errors from step4. Compare its full lower endpoint
   with zero in actual-density units. Independently replay normalization
   and all final bound comparisons; save complete evidence and failures.
   L952's positive polynomial endpoint is about1.2309e-61 and its
   unchanged second-order allowance about1.5124e-67; neither establishes
   the size or sign of the new signed correction.

The continuation test is a strictly positive complete enclosure.
A strictly negative enclosure rejects only the proposed positive tail
from8. A zero-containing enclosure, oversized complete analytic bound,
unpaid evaluation case or infeasible finite execution ends this fixed
test; there is no automatic node/precision/prefix/kernel campaign.
The recipe is finite and permits a comparison, but neither its practical
cost nor any successful margin is established by source review.

All34 signed rows, twelve labelled factors, factorials and M_0^12
normalization remain. Inherited theta inclusion, prefix/full-polynomial
execution and arithmetic contracts remain unresolved qualifications.
No residual independence, analytic absolute value, integrated-to-pointwise
transfer or favorable sign is assumed. Full/supporting Mathlib coverage
is unchecked. No cross-notebook input is used. No creative central-gap
mechanism follows from these sources: all-degree sign transfer and the
global join are still missing. This bounded known-method specialization
must not be routed as creative merely to satisfy a scheduling target.
