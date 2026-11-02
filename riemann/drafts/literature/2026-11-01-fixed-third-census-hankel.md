# Fixed one-third census — completed source comparison

TARGET: Assess whether C645g's exact Hankel symbol at delta=1/4 and eta=1/100 satisfies ||H_q||>=c exp(-n/32) for some c>0 and all sufficiently large n whenever M<=n/3, with arbitrary distinct grid-avoiding poles, positive integer residues and the prescribed anchor.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the full-pole, sparse-positive-residue, one-sided-census and C645i-audit assessments; read C645g's exact bound and C645i's complete construction/costs. Three bounded changed-coefficient searches below found no matching inspected theorem. Newly checked Komarov's weighted-alternance hypotheses and relevant positivity proof case; no exhaustive absence or novelty claim.
SOURCE_EVIDENCE: Reuse primary inputs recorded in 2026-11-01-full-pole-hankel-boundary-mechanism.md and 2026-11-01-c645i-one-sided-counterfamily-audit.md; directly retrieved BCQ arXiv:1501.01161v2, Sections 4--5.2/(17)--(27), pp.7--10, and Komarov, Izv. Math. 81:3 (2017), 568--591, Theorem 1 p.569, Section 1.6 p.572, Lemma 1/proof pp.579--580. Exact versions, links and applicability are below.
COMPARISON: C645g retains its small coefficient; C645i's audited full-boundary cancellation uses delta=2/5 and M=10n. Neither decides the fixed delta=1/4, M<=n/3 target. The inspected rational Hankel formulas leave its rate unevaluated; real weighted SPF alternance does not allow these complex residue weights or this circle norm.
GAP: A uniform lower bound at exp(-n/32), or an admissible asymptotic counterfamily at exactly this census, remains unproved. The sources provide tools for one bounded test, not the required quantitative conclusion; actual-Xi clearance, realization, independent upper bounds and signs remain separate.
REASON: Essential changed-coefficient comparison is complete. This fixed census is an independently testable restriction of the stopped arbitrary-C claim; try one global degree-budgeted Hardy dual rather than repeating the old absolute contour cost or importing the C=10 counterfamily outside its scope. No mathematics is attempted in this source turn.
LITERATURE_REASON: The invocation-start gate was REVIEW_REQUIRED for the fixed delta=1/4, M<=n/3 claim; ready general operator coverage was reused, and only the changed quantitative scope and a specific weighted-SPF lead required comparison.
SCOPE: One later proof attempt on the exact synthetic target below, retaining all complex weights, integer residues and arbitrary close distinct poles; standard operator/residue inputs may be cited. No full displacement theorem, actual-Xi transfer, enlarged census or new positivity premise is covered.
COVERED_TARGET: Assess whether C645g's exact Hankel symbol at delta=1/4 and eta=1/100 satisfies ||H_q||>=c exp(-n/32) for some c>0 and all sufficiently large n whenever M<=n/3, with arbitrary distinct grid-avoiding poles, positive integer residues and the prescribed anchor.

## Exact scope retained

Use n an integer, n>=5, delta=1/4, eta=1/100, d=5/4,
R=11/8, x=-5/4, t_j=j/n (0<=j<n), and C645g's exact product
B_n(z)=product_j R(z-i t_j)/(R^2+i t_j z).
The finite set Z consists of distinct points |a|<=R-eta, contains x,
and avoids all i t_j. Each residue r_a is a positive integer;
M=sum_a r_a<=n/3. No simplicity, pole-separation or one-sided
support assumption may be added. The symbol is exactly

    q(zeta)=sum_a [r_a B_n(x)/(R B_n(a))]/(zeta-a/R),
    H_q f=P_-(q f): H^2 -> H^2_-,

with normalized unit-circle measure. The target bound is uniform over
all such Z and residues, with c>0 and an onset depending only on the
fixed parameters. A counterfamily with this census and
exp(n/32)||H_q||->0 would stop it. Failure of one numerical search
would not prove a lower bound. No mathematical test is performed here.

## Relevance and stopping test

For delta=1/4, C645j's computed coefficient is
sqrt(57)/(16*pi)+0.10076, below 1/3. Thus a bound at this census
could connect a known total-count envelope to a noncancelling Hankel
estimate at one fixed displacement, beyond C645g's present tiny
coefficient. This is a proposed downstream use, not an established
extension of C645g or a proof for every displacement. Clearance,
interpolation, a useful independent boundary upper bound and actual
matrix signs remain unresolved. No off-line zero is asserted.

The completed comparison below checks the precise circle construction
and its quadrature costs, rather than treating a historical stop as a
global ban. Full matching Mathlib coverage is not checked. No lemma,
counterfamily, new estimate or mathematical script was written here.

## Completed comparison — 1 November 2026

### Reused coverage and scoped local screening

Read the ready [full-pole assessment](2026-11-01-full-pole-hankel-boundary-mechanism.md),
[sparse-census assessment](2026-11-01-positive-residue-hankel-exponent-test.md),
[one-sided comparison](2026-11-01-one-sided-pole-hankel-census.md) and
[C645i source approval](2026-11-01-c645i-one-sided-counterfamily-audit.md).
Their primary Nehari/AAK, rational-symbol, Gorin, one-sided quadrature
and segment-measure comparisons remain usable in their stated scope.
No reproof or new general-operator survey is needed.

The local search was limited to these Hankel assessments, related
Hankel/counterfamily histories and the recorded one-sided stop. The
fixed-third nomination was the only matching target found there.
This is a scoped duplicate check, not a search of all notebook proofs.
Read C645g's hypotheses, (3)--(6) and census-cost conclusion, all of
C645i including its independent audit and table, C645h's transfer
hypotheses/conclusion, and C645j's count-envelope statement. No
mathematical certificate was rerun: this is comparison, not a fresh
audit of the accepted counterfamily or its arithmetic.

C645g (5) has cost exp(-delta*n/16-A*m), with
A=1+log(256R/delta) and m the number of distinct poles. Its sufficient
condition is M<=delta*n/(16A). It does not state the target at M<=n/3.
The source review does not optimize or rederive this bound.

C645i (1)--(3) instead fixes delta=2/5, R=13/10, x=-11/10,
c=-239/200, r=19/200, and m=M=10n unit-residue polygon points.
Its auxiliary radius is s=1/10. The complete error (15) contains
200*exp(n/5)*(19/20)^m/[1-(19/20)^m]; its subsequent error estimate
uses m=10n. The product estimate (22) and final exponent 513/10000
also use those fixed geometric parameters. Thus its certified full
operator-norm upper bound is a comparison, not a counterexample with
the new parameters and budget. Neither deleting polygon nodes nor
changing n while holding that certificate fixed preserves its stated
symbol and quadrature proof. Whether a different construction can
work at n/3 is left for research; no exclusion of such constructions
has been inferred. The canonical C645i stop is preserved.

### Bounded searches and newly checked primary scope

Queries actually issued:

- `Hankel operator rational symbol positive integer residues Blaschke logarithmic derivative lower norm`
- `"simple partial fractions" "weighted" "lower" Blaschke`
- `"Hankel" "rational" "lower bounds" "pole" Baratchart Chevillard Qian`

L. Baratchart, S. Chevillard and T. Qian, *Minimax principle and lower
bounds in H2-rational approximation*, J. Approx. Theory **206** (2016),
17--47, [DOI](https://doi.org/10.1016/j.jat.2015.03.004).
Directly retrieved [author preprint v2](https://arxiv.org/pdf/1501.01161v2),
24 March 2015: (17)--(19), Theorem 4/Corollary 1, and the complete
Section 5.2/(24)--(27), printed pp.7--10. For coprime proper rational
p/q with all denominator roots in the disk, the finite model uses a
Malmquist--Walsh basis and Bezout division to compute the Hermitian
matrix of H*H. Its eigenvalues are the squared singular values. This
is applicable operator machinery, with denominator degree counting
distinct simple poles rather than total integer residue. It supplies
no evaluated uniform exponent for our weights. Theorem 4 retains
singular values and singular-vector norm factors. Reuse the previous
inner-symbol/geodesic scope comparison; no stronger matching bound
has been found in these inspected statements.

M. A. Komarov, *A criterion for the best uniform approximation by simple
partial fractions in terms of alternance. II*, Izv. Math. **81:3**
(2017), 568--591, [DOI](https://doi.org/10.1070/IM8548),
[English publisher PDF](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=rus&paperid=8548&what=fullteng).
Read the SPF/class definitions, Theorem 1 p.569, Section 1.6 p.572,
and Lemma 1 with its proof pp.579--580. Theorem 1 characterizes the
best approximation of a continuous real function on [-1,1] by real
SPFs of order <=n, when the candidate's poles lie outside the closed
unit disk, through n+1 alternation points. The weighted extension
requires a continuous nonnegative real weight, not identically zero,
whose zero set has no interior and at each zero x0 satisfies
(x-x0)/omega(x)->0. Lemma 1's convex-combination proof uses generating
polynomials positive on the real interval. These hypotheses do not
hold for the arbitrary planar, inverse-grid-weighted circle symbol.
The weight is on the approximation norm, not complex pole residues.
No circle/Hankel specialization or quantitative import is justified.

The MathNet endpoint initially redirected to metadata; its English-PDF
link yielded the primary text. Some screenshot requests redirected
again or returned no readable image; only the retrieved text passages
above are claimed read. These display failures leave no essential
source dependency missing. Other search hits, including general
inverse-spectral and displacement-matrix work, were unread leads;
no theorem from them is asserted or required for the bounded attempt.

### Decision and bounded continuation

DECISION is EXPLORE, not IMPORT or a claim of novelty. No inspected
theorem decides the exact uniform inequality, and no essential unread
input is identified for attempting it using the covered elementary
residue/Hardy tools. This source review is EXPLORATION: it completes
the changed-scope comparison without a new mathematical result.

For one later attempt, test a global Hardy dual that couples the entire
degree budget M<=n/3 to the exact grid product, instead of isolating a
small circle and paying the old absolute cost pole by pole. This is
a proposed mechanism, not an established dual formula or estimate.
Essential inputs are C645g's symbol and normalization and the cited
Hardy/residue tools. C645i is the mandatory full-norm cancellation
comparison; C645j motivates the coefficient and C645h gives the
possible downstream interpretation, not extra premises of the claim.

Decisive positive evidence is a proof with c>0 and an onset independent
of all pole positions/residues at these exact fixed parameters.
Decisive negative evidence is an admissible sequence n->infinity,
M<=n/3 and exp(n/32)||H_q||->0 controlling the largest operator norm.
A scalar cancellation, small least singular value, finite experiment
or failed candidate dual does not settle it. Save partial work as
EXPLORATION if neither test is met, and require a refined mechanism
or materially new input before repetition. No such test was executed
here. The newly completed scope receives the supervisor's separate
approval before research; this turn does not self-invoke it.

Actual-Xi census and clearance, exact interpolation/realization, a
smaller independent boundary upper bound and all-degree signs remain
unresolved; this one displacement would not cover every displacement.
No cross-notebook input, full Mathlib match or RH candidate is claimed.
