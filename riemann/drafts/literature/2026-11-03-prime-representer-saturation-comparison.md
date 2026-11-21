# Prime representer saturation: completed source comparison

TARGET: Assess paper 18/v3's quantitative comparison between the step-space projection gap for q and dist_H(1,V), checking the dilation multiplier and strong Nyman–Beurling hypotheses against the recorded full-update stop.
CHECKED: 2026-11-03
DECISION: IMPORT
SEARCH_EVIDENCE: Exact saturation/dilation searches located paper 18; strong integer-dilation and step-space searches located Baez-Duarte math/0205003v1 Theorem 1.1 and Bagchi math/0607733v1 Theorems 1 and 7. Targeted local comparisons and the two recorded stops supply no residual upper bound; no novelty claim.
SOURCE_EVIDENCE: Inspected paper 18 displayed v3 (22 October 2026), complete Stable comparison theorem (45)--(47), its multiplier/anchor/zero-functional proof cases and Limitations; Baez-Duarte math/0205003v1 pp. 1--2 Theorem 1.1; Bagchi math/0607733v1 pp. 137,144--145 Theorem 1, definitions and Theorem 7 with its proof.
COMPARISON: The source supplies an unconditional two-sided comparison with explicit constants and cutoff cost JK. Bagchi supplies the exact anchored strong criterion. Neither supplies attainment of the ceiling, decay of the Nyman--Beurling distance, or control of the complementary residual left by L729--L731.
GAP: Essential source coverage for this comparison is complete; the manuscript's quantitative inequalities have not received a local mathematical audit. The missing upper estimate remains an RH-strength task, not a consequence of invertibility or neutral density.
REASON: Import only the cited comparison's stated scope and the classical criterion for route selection; park saturation as a residual-control mechanism. No reproof, lemma, projection computation or mathematical script is warranted in this literature-only step.
SCOPE: Known-source comparison only, with H,V,S,q as below; no RH, simplicity, whole-step-space density, or uniform convergence on moving unit balls. IMPORT authorizes citation, not assuming G=U or any unestimated residual bound.

Use H=L²((1,∞),dy/y²), q from L731, and
V=closure_H span{rho_m:m≥2} from L730. Let S be the closed subspace
of functions constant on every unit cell [j,j+1), j≥1, and let b=P_S q.
The source comparison concerns ||b-P_V q|| (equivalently the
square root of the step-space ceiling minus ||P_V q||²) and dist_H(1,V).
No whole-step-space density is assumed. The following records inspected
source statements and their proof interfaces, not a new derivation or a
completed local audit.

Essential local context is L729, L730, L731, the completed representer
coverage, and the preserved stops
`ATTEMPTS/2026-11-03-dyadic-energy-contraction-source-stop.md` and
`ATTEMPTS/2026-11-03-signed-neutral-tail-gram-dual-source-stop.md`.
The earlier nomination required the separate multiplier and strong-criterion
proofs; those source-reading requirements are now fulfilled. The prior
L731 audit is unchanged. No source acceptance label is a hypothesis.

## Inspected comparison and operator scope

Primary source: bramble_trace, *Fixed and growing neutral gradients of the
anchored Selberg--Möbius approximant*, [paper 18, displayed v3](https://rstation.ai/problems/riemann_hypothesis/papers/18),
22 October 2026, “The step-space ceiling and its RH-equivalent attainment,”
Stable comparison theorem (45), conditional obstruction (46), and
Finite-cutoff comparison (47). This is a manuscript citation, not a
claim of independent verification or originality.

With G=||P_V q||² and U=||b||², its statements are

    delta dist_H(1,V) <= sqrt(U-G) <= M_0 dist_H(1,V),       (45)
    delta=log(128pi/27)-5/2>0.

The essential proof cases inspected are the weighted cell averages
b_j, their total variation bound, the strictly positive multiplier gap,
the zero-extended dilation on the whole H, and Neumann inversion:

    b_j=log(2pi)-u_j+r_j,
    u_j=j(j+1)log(1+1/j)-j,
    r_j=(j(j+1)/2) integral_j^(j+1) log(1-y^(-2))dy/y²,
    B_*=1/2-u_1-r_1,   b_1-B_*=delta,   M_0=b_1+B_*,
    D_n f(y)=1_(y>=n) f(y/n),   ||D_n||=n^(-1/2),
    D_n rho_m=rho_(nm)-rho_n/m,
    A=b_1 I+sum_(n>=2)(b_n-b_(n-1))D_n.

The source obtains sum|b_n-b_(n-1)|<=B_* from separate monotonicity
of u_j and r_j; it does not assume monotonicity of b_j. Its norm-convergent
Neumann series gives ||A||<=M_0, ||A^(-1)||<=delta^(-1), A1=b,
and invariance of V under both operators. The inverse preserves V because
its Neumann partial sums preserve V and V is closed; mere invertibility
of a general invariant operator would not suffice. The source uses
U-G=dist_H(b,V)². These are the precise bounded-operator hypotheses,
not an inverse on an uncompleted arithmetic coefficient space.

For V_K=span{rho_2,...,rho_K}, d_K=dist_H(1,V_K), and
e_K=dist_H(b,V_K)=sqrt(U-||P_(V_K)q||²), the source states, for
integers J,K>=2,

    delta d_(JK) <= e_K+sqrt(U) J^(-1/2),
    e_(JK) <= M_0 d_K+B_* J^(-1/2).                       (47)

Its proof uses the unital l¹ Dirichlet-convolution coefficient algebra,
sum|alpha_n|<=delta^(-1) for the inverse, and the n^(-1/2) dilation
norm for truncation. It enlarges support to JK. It does not compare
d_K and e_K at a free identical cutoff or prove either tends to zero.
No finite experiment or interval certificate was needed or used here.

## Exact classical criterion and applicability

[Luis Báez-Duarte, math/0205003v1](https://arxiv.org/pdf/math/0205003),
1 May 2002, Theorem 1.1, p. 2, with definitions p. 1: RH iff
chi_(0,1) belongs to the L²(0,infinity) closed span of
{ {1/(mx)} : m in N }. This is an unanchored half-line statement.
Its closure conclusion does not assert convergence of the prescribed
triangular taper. The source's RH-to-closure direction assumes RH.

For an exact anchored primary statement, [Bhaskar Bagchi,
math/0607733v1](https://arxiv.org/pdf/math/0607733), 28 July 2006,
*Proc. Indian Acad. Sci. (Math. Sci.)* 116, pp. 137--146,
Theorem 7, p. 145, defines on p. 144

    g_m(x)={1/(mx)}-(1/m){1/x},  0<x<=1,

and M as the reciprocal-cell step subspace. Theorem 7 states RH iff
1 is in their closed span, equivalently that this span is M. Its proof
checks the integer-dilation invariance and the step-indicator totality;
Theorem 1, p. 137, is the equivalent weighted sequence formulation.
Under the unitary substitution y=1/x, dx=dy/y² with reversed endpoints,
g_m(1/y)=-rho_m(y) and M maps to S. The sign does not change the
complex span; m=1 gives zero and can be removed. Thus this theorem
matches V exactly, rather than asserting density in all of H.

Paper 18 also explicitly handles the unanchored-to-anchored passage:
the unanchored tail on x>1 is a/x, where a=sum c_m/m; norm convergence
to chi forces a->0. Subtracting a{1/x} has vanishing L² cost and cancels
that tail. This is a source-stated specialization; Bagchi removes the
need to rely on an implicit change of Hilbert space.

The reverse zero-functional case in paper 18 was read: a hypothetical
zero rho=beta+i gamma with beta>1/2 gives the continuous functional
f -> integral_1^infinity f(y)y^(-rho-1)dy, of norm
(2beta-1)^(-1/2). It annihilates V and equals 1/rho on 1. The
source therefore states U-G>=delta²(2beta-1)/|rho|² in (46).
This is conditional on such a zero's existence and does not locate one.
No simplicity is assumed; no critical-line functional bound is asserted.

## Search, overlap, and route decision

Queries inspected on 2026-11-03 included `Nyman Beurling anchored strong
Baez Duarte criterion`, `step saturation dilation Nyman`, `Bagchi
Hilbert space reformulation Baez Duarte criterion step functions`,
`Nyman invertible dilation multiplier`, and the exact log(128...) constant.
The exact comparison was found in paper 18; Bagchi and Báez-Duarte cover
the closure criterion, not a residual upper estimate. Search snippets
from other sites were not theorem evidence. No exhaustive priority claim.

Targeted local searches of the representer, arithmetic-tail, neutral-density,
dyadic-energy and sqrt(N)-tail assessments found no earlier completed
assessment of this multiplier. The step-space ceiling is explicitly
credited by paper 18 to paper 21/v2, Theorem 2(c), Sections 5 and 7;
that paper was not reread for this already attributed fact. Those earlier
assessments remain reusable for their own scopes. Their full-update
and growing-unit-ball stops remain intact.

Decision: the finite-cutoff transfer is useful bookkeeping, but pays no
independent arithmetic upper estimate. The inspected Limitations section
explicitly leaves ||(I-P_(W_K))(1-g_N)||² uncontrolled. Saturation is
RH-equivalent, so the comparison is not a new residual-control mechanism.
This is an informative source-stage stop, not a disproof of RH or of
possible future estimates. No new lemma or canonical proof is added.

There is no justified creative upper-bound mechanism supplied by this
review. A materially different discriminating direction is the already
recorded but unread paper 47/v1 Section 7 prefix-obstruction proof:
determine whether scalar-anchor cancellation retains an actual zero
obstruction for the prescribed triangular residual. This concerns a
necessary arithmetic condition, not saturation or larger neutral spaces.
Its separate nomination remains REVIEW_REQUIRED; no result from it is
imported, no proof read this turn, and no mathematics approved here.

Continuation/abandonment test: examine the precise prefix, Mellin-filter
domain, pole cancellation, zero multiplicities and growth threshold.
Continue only with a source-covered independently testable obstruction
or changed mechanism; otherwise retain the stop without proposing another
full-norm reformulation. Literature exception: an essential unread proof
for this distinct recorded lead, not more literature on the ready comparison.

Mathlib: full matching comparison, strong criterion and dilation-operator
coverage not checked; availability unknown. The named Neumann-series
theorem and Hilbert projection theorem are supporting classical inputs,
not a checked matching Mathlib declaration. No absence claim.
