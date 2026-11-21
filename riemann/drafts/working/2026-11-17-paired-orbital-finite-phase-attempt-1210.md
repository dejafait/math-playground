# Two-level finite-phase response — bounded attempt1210

The invocation-start EXPLORE assessment1208, separately approved1209,
authorizes exactly the finite-phase bound for the common-background
family in C030m. The full supplied overview and DAG were read first;
the complete C030m and C030l proofs and the narrow audit1208 record
were then read. Existing notebook changes are preserved. The initial
notebook-scoped status output was oversized and is not treated as an
exhaustive change inspection; subsequent inspections are target-scoped.

Main gap: actual-Xi all-degree positivity in L030-L032/C032a, with
theta signing and graph realization independent. Intermediate target:
an absolute C with |E_(k,b)(x)|<=C*x*b^2 throughout |x*b|<=1/4.
Plausible use: a paid signed perturbation of C030l's finite real
reference. Continue with an explicit uniform C or stop the proposed
bound on a rigorous unbounded normalized-defect family. Unequal
backgrounds, pair summation and Xi transfer are outside this attempt.

Reuse assessment1208/approval1209's exact finite-phase source comparison,
broader1204 search, scoped duplicate check and recorded stops. C030l
imports Sra author v3 C.7/C.8 pp25-27 and Olshanski2013 Corollary3.2
p1017 (strict rows), with its own weak-row extension. No new source,
complex stochastic order, common normalizer or cross-notebook input
is being assumed. C030m's existing Taylor result alone is insufficient.

## Saved partial reasoning

Put d=h-ell for the leading two-by-two corner of Q=V P_j V*.
C030m's U(2) orientation calculation extends directly from the square
to the bounded observable cos(v*T): its orientation average is
sinc(v*d)=integral_0^1 cos(v*d*s)ds. Thus the separately normalized
partition quotient is the real tilted expectation of that sinc.

For a!=r, set epsilon=sign(a-r), t=x*|a-r| and c=b/|a-r|.
Scale the orbit to t*Q and use the fixed field c_2=-epsilon in
C030l. The observable becomes phi(h_t-ell_t)=sinc(c*(h_t-ell_t)).
For 0<=d<=U with |c|*U<pi, phi'<=0 and |phi'|<=c^2*U/3.
The compensated tests phi(h-ell)+L*h and -phi(h-ell)+L*ell,
L=c^2*U/3, should be increasing. Together with C030l's translated
upper sandwich and separate normalization, they give a finite
difference bound L*eta, hence |F_j'(t)|<=c^2*t/3.

The denominator should satisfy F_j>=1-(x*b)^2/6>=95/96.
This would give each rank's response at most (32/95)*x*b^2,
and the adjacent defect at most (64/95)*x*b^2. Before concluding,
check the global increasing-test extensions, fixed-rate chain rule,
smoothness of normalized expectations, boundary |x*b|=1/4,
a=r, b=0, n=2 and j=0,n. This checkpoint is unfinished reasoning,
not an independently reviewed theorem or an RH candidate.

## Completion

The bounded test succeeds with C=64/95. Full hypotheses, argument,
source qualifications and unchecked Mathlib coverage are canonical in
[C030n](../../lemmas/C030n-two-level-finite-phase-orbital-bound.md).
No numerical experiment or mathematical script was needed.

The final proof simplifies the saved contrast rescaling: scale the
projection orbit directly by t=x and hold the real field c_2=-(a-r)
fixed. This includes zero contrast with no singular division. U(2)
averaging gives a sinc of the scaled corner gap. Globally increasing
extensions of the two compensated tests, together with C030l's
separately normalized translation sandwich, prove the finite-difference
estimate in C030n (9). Fixed-Haar smoothness then gives (10); the
positive lower bound (5) yields (1)-(2). Both contrast signs, b=0,
the closed phase boundary, scalar endpoint ranks and n=2 are included.
This is a finite-window proof, not a pointwise Taylor inference.

Outcome ADVANCE means a new relevant local finite-family input has
been written, pending independent conceptual audit. POTENTIALLY_NEW
means only that the reused checked sources supplied no matching bound;
originality is unverified. Actual-Xi positivity remains unresolved.
One mathematical attempt, no extra probes or literature turn, and no
claim to have independently audited C030n or its imported orbital law.

C030n uses C030l's full real comparison and C030m's definitions and
orientation identity; the DAG adds precisely those two direct inputs.
The PROOF summary records the new restricted bound and preserves its
displaced audit-status shorthand in history1210. Existing proofs and
unfinished work remain unchanged. The sole continuation is a conceptual
audit of C030n, nominated REVIEW_REQUIRED for separate scope approval;
no new assessment is approved in this research step.
