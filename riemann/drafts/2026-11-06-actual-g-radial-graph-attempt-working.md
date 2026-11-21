# Actual-G periodic radial graph — bounded attempt in progress

The saved EXPLORE assessment is
`literature/2026-11-06-actual-g-radial-graph-full-phase.md`; its exact
target and all zero/degeneracy qualifications are retained. Startup
PROOF/DAG and the supplied assessment were read directly. Targeted
reads of L018, L775, L845(4), L846(3), the reusable joint-contour
assessment and the two named contour failure records found no matching
completed graph calculation. Existing notebook changes are preserved.

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
Intermediate target: decide existence, or a rigorously delimited
obstruction, for the fixed r=2,k=1 bounded C^2 periodic radial graph
with nonnegative full oriented pullback. A graph would supply only
fixed-case contour participation; all other shifts, growing order,
uniform errors and RH would remain open.

Continuation test: retain both factors 1/i, every density zero and
every possible complex-Jacobian zero; verify the torus homotopy and
test a global compatibility condition. A phase equation alone is not
an advance. Stop this bounded attempt after a graph, a scoped
obstruction, or an exact unresolved condition is obtained.

Initial algebra to check: with A=Du (rows indexed by u_j),
the logarithmic volume factor is det(I-iA)=1-det A-i tr A. Thus the
candidate full density is F_2(z(theta)) times this factor. This does
not assume that either factor is nonzero. The explicit deformation
z_j(t,theta)=R_1 exp(t u_j(theta)+i theta_j) stays in X for 0<=t<=1.
No conclusion about existence, signs or novelty was recorded at this
initial checkpoint.

Next within this attempt: test global periodic constraints in this
full equation, rather than delete its zero sets or infer existence
from local phase optimization. No new source theorem is needed for
the elementary differential calculation under the ready assessment.

## Provisional obstruction saved before the full write-up

The bounded attempt now tests the product subclass
u_1(theta)=v_1(theta_1), u_2(theta)=v_2(theta_2). This is a scoped
test inside the approved graph question, not an assumption on all
allowed graphs. For its simple closed radial curves gamma_j,
omega pulls back as C A_1(t) A_2(s) (gamma_1(t)-gamma_2(s))^2,
where C=R_1^2/G(R_1)^2>0 and A_j=G(gamma_j)gamma_j'/gamma_j^3.
If this is nonnegative, compare its values at two fixed points a,b
on the first curve with nonzero A_1. Except at finitely many zeros,
the ratio forces (a-w)/(lambda(b-w)) real on the second curve,
where lambda^2=A_1(b)/A_1(a). Thus that curve lies on a generalized
circle through a,b. Continuity retains the excluded points. Radial
winding makes it a whole circle enclosing zero. Varying a shows that
the first curve is the same circle.

For that circle z=c+rho exp(it), rho>|c|, nonnegativity forces
H(z)=G(z)(z-c)^2/z^3 real on its boundary. If c=0, the positive
Fourier coefficient a_3 rho^2 has no negative partner. If c!=0,
H has a genuine third-order pole at zero. Subtract its principal
part P=h_3/z^3+h_2/z^2+h_1/z, h_3=c^2 a_0!=0, leaving an entire
function. In w=(z-c)/rho the positive Fourier coefficients have
root limit zero, whereas the negative coefficients have root limit
|c|/rho>0. Boundary reality is impossible. Full details, orientations
and the finite-zero argument are to be checked in the canonical
write-up; this checkpoint is not an independent verification.

The general coupled equation remains open. Nothing here excludes
complex-Jacobian zeros for coupled graphs. A successful proof of
this scoped obstruction would justify abandoning independent
one-variable contour choices, not all periodic radial graphs.

## Completion

The complete argument is now canonical in L847. The provisional
reasoning above is preserved as the pre-write-up checkpoint, not a
second proof or an independent audit. The result excludes only the
product subclass; the general coupled compatibility system (4) in
L847 remains unclosed. The bounded attempt ends with that negative
result and a separate REVIEW_REQUIRED conceptual-audit nomination.
