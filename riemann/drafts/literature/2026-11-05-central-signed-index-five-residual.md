# Central signed index-five residual — source comparison

TARGET: Test the signed index-five residual against the root-preserving coefficient interval of L791's fixed central degree-five model.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step479 checked scalar coefficient/constant pencils, primary antiderivative criteria and stronger actual-Xi Jensen results; exact queries, inspected ranges and bounded local duplicate comparison are below. No residual calculation or novelty claim.
SOURCE_EVIDENCE: Pereira arXiv:1901.08156v2 pp.1–2 introduction and Lemma1.1, including the Rolle/IVT argument; Griffin–Ono–Rolen–Thorner–Tripp–Wagner arXiv:1910.01227v3 (17December2020), (1.1)–(1.2), Theorem1.2/Corollary1.3 and Section5; reuse Holland v1 (66)–(71)/Lemma6.2 and L791/L778's audited finite inputs.
COMPARISON: Reciprocal reversal makes the single leading-coefficient variation a constant variation, covered by Pereira. Published Jensen results already cover degree5 at every shift; the unreported quantity here is the signed residual's quantitative distance to this fixed model's collision boundary, not root reality alone.
GAP: Actual gamma(5), the four critical-value enclosures and the signed residual/collision margins remain uncomputed. No uniform-in-degree signed estimate, central multiplier bound or all-degree positivity follows from these sources or from a finite successful test.
REASON: Complete the missing source interface for the unchanged saved diagnostic; specialize the known interval criterion and audited evaluator only to quantify a useful finite residual margin. A citation settles qualitative low-degree hyperbolicity but does not supply that margin.
SCOPE: Ready for one fixed n=0,d=5,D=B_J/2 signed residual/interval calculation at L791's exact solution, retaining its entire parameter box and inherited software contracts. No parameter rescue, degree sweep, new family or growing-degree theorem is covered.

## Completed source review — step479, 5 November 2026

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
the exact saved one-coefficient diagnostic, with a quantitative collision
margin as its useful output. Such a margin could guide a later signed
residual mechanism; it supplies no estimates for other degrees. This is
source approval of a known-method specialization, with no new lemma,
coefficient enclosure or mathematical script produced in this turn.

### Applicable criterion and its cases

Rajesh Pereira, [*Which quartic polynomials have a hyperbolic
antiderivative?*, arXiv:1901.08156v2](https://arxiv.org/pdf/1901.08156v2),
17 April 2019, pp.1–2, introduction and Lemma1.1, restates the
Souroujon–Stoyanov criterion. For monic real-rooted q with descending
root multiset w_k and P'=q, P-c is real-rooted exactly for
max_(k odd)P(w_k)<=c<=min_(k even)P(w_k).
Read its Rolle/IVT argument, including exterior rays. Weak endpoints
allow multiple roots; with simple critical points strict interior signs
give simple roots. Original reference[7] (2016) was not independently
read. Use this explicit criterion, not merely existence of some constant.

For specialization, use Q(x)=x^5 p(1/x) for L791's model, p_0=1.
The fifth coefficient becomes the constant. Apply Lemma1.1 to Q'/5
and its zero-constant antiderivative. L791 supplies five simple nonzero
model roots; Rolle supplies four simple real critical points.
Actual-Jensen hyperbolicity is not a premise. No new inverse-Rolle
lemma is needed.

### Exact normalization to retain in the calculation

Reuse Jonathan Holland,
[*A new hyperbolicity wedge and a joint semicircle limit for Jensen
polynomials of Riemann's xi-function*, v1](https://arxiv.org/html/2608.08682v1),
9 August 2026, (66)–(71) and Lemma6.2, as already assessed in step473.
These give S=B R_1 and P_F(y)=J^{5,0}(-y/S)/gamma(0), with coefficient
multipliers equal to1 for indices0..4. No eventual-shift estimate is
imported at n=0. L791 independently supplies this fixed model's existence
and roots, not source Lemma6.1 or Lemma7.3's asymptotic hypotheses.

The next calculation must use gamma(j)=8*4^j*j!*a_j,
R_j=gamma(j)/gamma(0), and the *same* uncertain S as L791.
The actual fifth coefficient is -R_5/S^5, the model fifth coefficient
is p_5, and their signed difference is actual minus model. In the
reciprocal polynomial this is the same constant displacement, with no
binomial factor because binom(5,5)=1. Account for the factor5 when
using the monic derivative Q'/5; do not compare an unscaled constant
against scaled critical values. Positivity of gamma(5) is available
from L021, but its quantitative enclosure has not been computed here.

Read L778's evaluator definition and (3)–(5): it encloses a degree96
polynomial on the complex radius1600 disk, with an additional uniform
analytic error. Thus index5 is within the already audited evaluator's
scope. Reuse L791's Cauchy coefficient-error procedure and the full
quadrature widths; do not treat the sixth P_0 coefficient as an exact
coefficient of G. This is existing evaluator coverage, not a newly
proved gamma(5) estimate. The source certificate remains
`scripts/actual-fredholm/fixed-pair-certificate-431.json`; L791's exact
parameter box is recorded in `scripts/central-jacobi/fixed-model-certificate-476.json`.

### Stronger known overlap

M.J. Griffin, K. Ono, L. Rolen, J. Thorner, Z. Tripp and I. Wagner,
[*Jensen polynomials for the Riemann xi-function*, arXiv:1910.01227v3](https://arxiv.org/html/1910.01227v3),
17 December 2020; Adv. Math.397(2022),108186,
Theorem1.2 assumes RH_m(T) and d<=floor(T)^2 and concludes
hyperbolicity for all n>=m. Corollary1.3 states the unconditional range
d<=9.36*10^20,n>=0, using Platt's cited finite zero verification.
Read (1.1)–(1.2), those statements and Section5's sector/derivative
argument. Their gamma is8 times the local gamma; ratios and root
reality are unchanged. This already covers the nominated degree.
It gives no collision-distance value in L791's coefficient pencil.
No independent audit of Platt's computation, Chasse's multiplier theorem
or this manuscript's full proof is claimed or needed as an input to
the proposed numerical diagnostic. The author's older submitted PDF
was also inspected; use the versioned v3 citation for theorem numbering.

### Bounded search, prior failures and decision

Queries: `real rooted polynomial varying constant coefficient critical
values interval polynomial antiderivative hyperbolic`; `Riemann xi Jensen
polynomials degree 5 all shifts hyperbolicity degree 8 Chasse`;
`polynomial hyperbolic antiderivative constant interval critical values
real rooted Pereira`; `"real-rooted" "constant term" "interval"
polynomial critical`; `"Jensen" "degree five" "coefficient" "residual"
xi`; `"polynomial" "leading coefficient" "critical values"
"hyperbolic" interval`.
Search hits were leads until the primary passages above were inspected.
No exact published quantitative residual/collision margin for L791 was
identified in this bounded search; that does not establish novelty.
Unneeded general-pencil, thesis and Planat hits were not adopted.

Narrowly checked the step379 primitive assessment, step473 wedge
assessment, fixed-model audit assessment and the step478 closure
record for index5/coefficient-pencil/residual overlap. The primitive
stop lacks an actual prescribed-constant estimate for general theta
polynomials. Here the model roots are independently established and
the proposed task is one quantitative finite test; no descent is
reopened. The general central multiplier still lacks Holland's eventual
hypotheses. No additional audit of L791 is nominated.

Continue only to obtain signed residual and both distances to the
*exact* admissible interval, with strict certified inequalities at the
exact parameter solution. Isolate all four critical points, keep the
positive fifth-coefficient magnitude, distinguish finite root collisions
from a coefficient-zero/degree-drop boundary, and retain parameter/data
uncertainty. A strict violation of a necessary interval bound stops
this fixed transfer, and would also require checking normalization against
the known qualitative overlap. Failure of enclosure precision or of
merely sufficient brackets is inconclusive. Equality permits a collision
and is not a simple-root margin. Save complete enclosures and actual/
required bounds, not a floating-point root plot. No degree or D change
may rescue a failed test in that step.

The source gate for this unchanged target is now SPECIALIZE; the next
work is a calculation reproducing known methods. Canonical proof and
any certificate belong to the research step, not this literature turn.
Mathlib coverage of the complete specialization is unchecked; no absence
claim is made. No cross-notebook input was read. A justified creative
central attempt remains blocked by missing signed growing-degree control;
this finite test is not relabeled creative to meet a scheduling aim.

## Original step478 nomination — preserved provenance

At nomination this was a new assessment requiring a separate source review, not ready
coverage and not an extension of the step478 audit. No lemma or
mathematical calculation for this target was derived or approved.
The source review should retrieve the exact applicable scalar polynomial
pencil/root-stability theorem and its relevant proof cases, compare
stronger known low-degree Jensen results, and retain their hypotheses.
If those results make this diagnostic redundant, record the overlap
and select a different target instead of reproducing known roots.

## Comparison of three possible continuations

1. Prescribed-primitive descent would need independent theta critical-value
   inequalities. The existing step379 stop records that the inspected
   antiderivative source supplies an admissible constant interval but
   does not place the actual constant inside it. No new estimate is
   available here, so this mechanism is not reopened.
2. A general diagonal residual-multiplier theorem would seek growing-degree
   control. The step473 assessment records that Holland's usable signed
   and multiplier bounds require eventual shift and exclude the central
   range. L791 does not supply those missing hypotheses. There is no
   justified central creative theorem attempt from that input alone.
3. A signed coefficient-pencil test can measure the first actual mismatch
   in the existing finite representation. This is the selected bounded
   diagnostic: establish the permitted coefficient interval from an
   applicable known theorem, and compare one rigorous actual coefficient
   enclosure to it. It neither assumes an all-degree multiplier nor
   retries the primitive's unpaid constant. No comparison value has been
   computed this turn.

Essential inputs are L791's audited exact solution and model, L778's
analytic evaluator, and L018/L021/L776 for normalization. The review must
verify the conversion from gamma(5) to the coefficient in the same
positive y-scaling S=B R_1 as L791. The actual index5 coefficient is
not part of the existing gamma(0..4) certificate. The exact Banach
solution remains enclosed, so any subsequent stability comparison must
hold for that solution, retaining all parameter uncertainty.

Continue only if the literature supplies a usable finite stability test
and the proposed calculation has information beyond reproducing known
degree-five hyperbolicity: a signed residual size and distance to the
collision boundary in this specific model. Its plausible downstream use
is to choose or reject signed residual control before any growing-degree
development. A certified residual outside the applicable interval would
stop this fixed transfer; insufficient precision or a merely sufficient
test's failure would be inconclusive. No finite outcome implies RH.
Do not enlarge degree or change D to rescue a failed test in the same turn.

The main gap is still actual-Xi all-degree mixed positivity. A justified
creative central mechanism needs an actual signed growing-degree estimate
or new structural input; neither is supplied by this finite audit.
Mathlib matching coverage is unchecked. No cross-notebook result is used.
