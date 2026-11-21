# Fixed direct joint-removal attempt2236 (work saved before computation)

Approved target: assessment2234, separately approved2235. Reused sources;
no new literature search and no changed root brackets or exterior split.
Main gap L030-L032/C032a remains open. A positive two-removal inverse
would be an intermediate input, without iteration or an all-degree bridge.

For a>0 write T_a f(u)=a integral_0^infinity f(u+t)sin(at)dt.
The proposed H=T_y T_x K has the candidate convolution formula
H(u)=integral_0^infinity K(u+t) W_xy(t)dt,
W_xy(t)=xy*(y*sin(xt)-x*sin(yt))/(y^2-x^2).
Absolute Fubini, all derivative tails, both root-origin conditions and
Fourier inversion must be paid before calling H the even quotient kernel.
The numerical trial itself is defined for the full closed nonroot box.

The fixed exterior is u>=1. Attempt termwise additive convexity of K
there, then Tuck's restricted translated cosine/sine tests. No global
G_x decrease is assumed. C919n is context, not a joint-sign premise.

For the compact test use exact rational closed parameter cells and signed
quadrature; prerecord all finite settings in this file before the numerical
pass. A negative nonroot value only rejects the stronger box certificate.
A failed enclosure is inconclusive and must be retained, with no automatic
refinement, split movement or bracket change. Full certificates go under
scripts/real-zero-origin/; retain the CPython/Fraction/libmpdec contracts.

Unfinished reasoning: convolution and the second actual-root boundary are
being developed. Expected identity is H''+y^2 H=y^2 G_x and
H'(0)=-y^2 Q_x(y)=0 because x and y are distinct actual roots. Smooth even
extension should then follow from the forcing's even origin jets. These
are proposed steps, not completed proof or acceptance.

## Frozen finite settings (before first numerical pass)

U=4; retain indices1..4; Simpson panels65536; precision80 directed
Decimal; spatial derivative cells1024 of width1/256 on[0,4].
Two frequency centers57/4,43/2, Taylor degree8, radii1/4,1/2;
16 equal x cells and32 equal y cells. Spatial parameter cells256 of
width1/256 on[0,1]. Use signed suffix Simpson moments at every spatial
cell's left endpoint, obtained from the full cumulative quadrature.
Shift the moments by the exact binomial identity to t-u and rotate
phases with the rigorously propagated sine/cosine values at u.
Frequency Taylor error uses the complete ninth moment on[t>=u],
bounded by t^9. Use cubic Taylor in u across each closed spatial cell,
with all four coefficients derived from G_x,G_y and their first
derivatives. Bound the fourth derivative by
x^2*y^2*(K(a)+(x^3+y^3)/(y^2-x^2)*integral_a^infinity K)
on the cell starting at a, using the already imported decrease of K.
Use the uniform extrema14.5,22 and denominator>=923/4 in that bound.
Target one rational compact lower bound delta=1e-10. Stop at the first
failed enclosure (retain every completed record), without refinement.

Both complete C919f tails are applicable to t^j K(t),0<=j<=9,
on the original t coordinate. Shifted moment errors include all finite
binomial weights; no new tail is silently identified with an old one.
The trial H and its derivatives are defined without root hypotheses;
the exact even quotient interpretation remains conditional on both roots.

For the exterior, direct differentiation gives
K_n''(u)=exp(u/2-v)*[32v^4-224v^3+330v^2-75v], v=pi*n^2*exp(2u).
For u>=1, v>21, and the bracket is positive by
32v-224>0 and330v-75>0 after grouping v^3 and v.
Convergence of the differentiated series and the strict Tuck application
remain to be fully written in the canonical proof after this test.

## Completion

The frozen test passed all131072 closed cells; the lower endpoint is
>6.9e-9 against required1e-10. Full internal reconstruction passed464918
exact-rational checks, zero failures. Canonical C919o contains the complete
proof, qualifications and artifact paths. No settings were changed after
the numerical pass; no second target or refinement was attempted.
Separate critical audit remains pending. The initial unfinished reasoning
above is preserved as a prerecord, not an independent statement of proof.
