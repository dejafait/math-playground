# Finite balanced-phase localization — bounded continuation

TARGET: Test whether L939's scalar phase admits a uniform supporting-parabola bound h_r(s)>=c s^2 with explicit c>0 for sqrt(2/3)<=r<=2 and -r<=s<=11r, as a finite-energy localization input for L938.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse completed step97 comparison in 2026-11-09-signed-balanced-simplex-outer-budget-96.md: exact-object, exp-square-root supporting-inequality, finite Laplace and scoped duplicate/failure searches found no inspected theorem settling this scalar bound. Search misses do not establish novelty.
SOURCE_EVIDENCE: Direct primary sources: https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf Sections3.1.3-3.1.4, pp69-71; https://dlmf.nist.gov/1.4#E11 and https://dlmf.nist.gov/1.4#E35 through E37; reused contextual sources https://arxiv.org/pdf/2406.12706v3 and https://arxiv.org/pdf/1511.00302v2. L939(10)-(14) supplies the exact phase and its existing r>=2 constrained estimate; Katsevich arXiv:2406.12706v3 Assumption2.1 and Remark2.5 identify minimum/complement obligations; Majerski arXiv:1511.00302v2 Theorem2.1(A1)-(A2), local/outer proof cases and Theorem2.4 identify explicit-gap obligations; Boyd-Vandenberghe Sections3.1.3-3.1.4 and DLMF1.4.11,1.4.35-37 supply supporting calculus under checked hypotheses. Exact citations and source limitations are in assessment96, completed step97.
COMPARISON: Known Laplace bounds need quantitative localization; neither they nor L939's r>=2 proof supplies this finite-range scalar constant. L940 stops global Schur-concavity of the signed amplitude, a different object; L950 stops the fixed negative-row cost. This is a new finite specialization test within the established saddle route, not a new general Laplace theorem or central creative mechanism.
GAP: Prove the displayed scalar inequality with one explicit uniform positive c, or refute it by a rigorously certified violating pair or obstruction to any positive c. Its constrained-simplex use must be justified separately within this attempt; signed amplitude, local remainder constants, full-theta/boundary budget and infinite-energy join remain unproved.
REASON: This isolates an independently testable missing finite-energy input before a much larger effective signed-budget calculation. Step98 completes the separate source-approval/recovery turn: direct primary URLs and hypotheses are verified below; EXPLORE remains ready for exactly TARGET. No mathematical attempt or inequality is supplied by this approval.
SCOPE: Exactly TARGET and its finite-sum transfer to L939's constrained phase. Analytic proof/obstruction only; no signed-density estimate, global variation claim, moment/exponent optimization, compact extension, grid campaign or BKR-dependent shortcut. Full/supporting Mathlib coverage is unchecked.

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
The reviewed outer objective remains the actual tilted negative mass
on E>=8 below exact L949 m-B. This subtarget could supply a coercivity
input for a later signed-localization/complement estimate; success
would not pay that objective. Other signs, head/global variation,
contacts, all other degrees, initialization and realization remain open.

Use precisely L939's definitions, reproduced here only to fix the target:

    f_r(s)=exp(2r(sqrt(1+s/r)-1)),
    h_r(s)=f_r(s)-1-s,
    z_r(y)=sum_(i=1)^12 h_r(y_i),
    sum_i y_i=0, y_i>=-r.

The proposed finite range corresponds to E in[8,48] under the already
fixed r=sqrt(E/12). Check the scalar coordinate range against the
constrained simplex rather than silently changing it. The desired
constant is uniform in both variables, not an existential
energy-dependent c(r), a sampled minimum or an asymptotic o(1).
This assessment asserts neither its existence nor its value.

Essential local inputs are L939's exact phase/derivative/Hessian and
existing r>=2 estimate, with L938 for the full signed integral context.
L019/L058 enter through these canonical inputs. L947/L949 give only
budget context, and L950 only the stopped alternative. No numerical
arithmetic contract is required for an analytic phase proof; any
certificate used instead must state and justify its exact arithmetic
and transcendental inclusions. No cross-notebook input is needed.

Import the cited elementary supporting-line/curvature/Taylor results,
checking their hypotheses on each proposed interval. Do not assume
f_r convex on the whole scalar range. The boundary s=-r can lack
square-root derivatives; any substitution, endpoint limit or separate
case must be justified. At s=0 the requested inequality must be proved
with a valid local remainder rather than division by zero. The change
from r>=2 is exactly why L939's old proof is not itself sufficient.
No reproof of a general Laplace theorem or dependence on its unspecified
constants is needed to perform this isolated test.

Continue only with a complete uniform inequality and an explicit c>0,
plus justified finite-sum applicability, or with an informative rigorous
obstruction. A finite witness can refute a proposed c; to rule out every
positive c requires a nonpositive value at s!=0 or a certified limiting
obstruction. Failure of this stronger scalar condition does not refute
constrained localization, B_4<m, or RH. Stop after the one attempt at
an unpaid uniform obligation; preserve partial reasoning and require
materially new input before another try. Do not silently weaken to
h_r>=0 and call the quantitative target complete.

This is established-route development. An explicit phase constant,
if obtained, still leaves the signed polynomial's cancellations,
local amplitude/error estimates, actual singular-boundary mass and
effective infinite-energy join unpaid. A successful constant alone
must not be advertised as a numerical budget or an effective tail sign.

## Step98 source approval and URL repair (2026-11-09)

LITERATURE_REASON: The supervisor identified missing direct source URLs in
this ready assessment. This bounded source check repairs that defect;
it does not reopen the completed Laplace comparison or change TARGET.

Directly reopened Boyd and Vandenberghe, *Convex Optimization* (2004,
seventh printing with corrections 2009), [author-hosted PDF](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf).
Read Sections3.1.3-3.1.4, printed pp69-71 (PDF pages83-85), including
the full one-variable supporting-line proof and its converse, the
line-restriction argument, and the second-order criterion. Equation(3.2)
requires differentiability on an open convex domain; equation(3.4) is
the scalar version. The second-order criterion additionally requires
twice differentiability and a nonnegative Hessian throughout that
domain. These are tools to import, not evidence that L939's f_r meets
their hypotheses on the whole proposed interval. No reproof of these
general facts is needed. A future proof must verify each interval and
handle the square-root endpoint separately.

Directly reopened NIST DLMF, live Section1.4 on 2026-11-09:
[mean-value theorem, equation1.4.11](https://dlmf.nist.gov/1.4#E11),
and [Taylor formulas, equations1.4.35-37](https://dlmf.nist.gov/1.4#E35).
Read the complete hypothesis and remainder displays: the former needs
closed-interval continuity and interior differentiability; the latter
assumes C^(n+1) on the closed interval and provides both Lagrange and
integral remainders. Applicability at s=-r is not supplied by these
formulas. At s=0, a future proof must justify the quadratic estimate
without dividing by zero. Nothing here establishes a uniform c.

Reuse assessment96's inspected Katsevich v3 Assumptions2.1-2.3,
Remark2.5, Theorem2.12 and LemmaE.1, and Majerski v2 Theorems2.1/2.4
and local/outer cases, with their direct PDFs above. Those contextual
results were not downloaded again in step98: their target and
hypotheses have not changed. Their unspecified local constants or
unpaid explicit phase-gap/onset conditions still prevent a finite
outer-budget import. The scalar target needs the elementary sources,
not another general Laplace theorem or access to the parked leads.

Local comparison reread L939(10)-(14), L938's exact density hypotheses,
and L940/L950 conclusions. The existing coercivity argument starts at
r>=2; the saved finite-range target is not proved there. The recorded
amplitude and fixed-row failures address different quantities, and
are preserved. A narrowly scoped search of November9 assessments and
attempt records found only the saved scalar proposal and its source
comparison; this does not establish novelty. Full/supporting Mathlib
coverage remains unchecked. Decision EXPLORE is approved for one
analytic proof/obstruction attempt with the unchanged scope and stop
test above. No new lemma, calculation, or central creative mechanism
has been introduced in this source-approval turn.
