# Global-envelope saturation feasibility: working record

Invocation-start assessment:
`literature/2026-10-29-saturation-global-polynomial-feasibility.md`,
SPECIALIZE; exact target and hypotheses unchanged. This is a calculation
using a classical theorem, not new central sign mathematics.

Saved reasoning before final assembly: write a=(log T)^A. Once B_T>=a,
uniform error 1/8 implies p(a)-p(0)>=1/4 and ||p||<=9/8.
The mean-value theorem and affinely scaled classical Markov inequality
then give d^2>=B_T/(9a). Since sum_(n<=N)n^(-1/2)>=sqrt N,
this forces d to grow for every fixed A. Independently, if d>=4,
J>=M N^12 and M N^12/T tends to 1/sqrt(2pi), contradicting
J log(2J)=o(T). Check floors, degree zero, arbitrary real T and
subsequences in the canonical proof before accepting the conclusion.

Length interpretation to retain: for D_j=sum_(n<=M)(log n)^j n^(-1/2-it),
the nonchirped term multiplied by |F|^(6k) groups into bilinear products
of D_j F^(3k), each supported through M N^(3k). This extends only
L481's stated mean-square interface; chirped terms, coefficient norms
and signed approximation errors remain separate. No universal lower
bound on all possible product representations is claimed.

Possible next implementation, not attempted or approved here: replace
uniform control on [0,B_T] by approximation in the actual |R_T| measure,
with A=0 and degree at most three. Source coverage for that changed
norm is missing; nominate a REVIEW_REQUIRED assessment rather than
derive or approve it in this step.
