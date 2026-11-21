# Order-five coefficient countermodel — step408 working note

Gate: reuse the pre-invocation SPECIALIZE assessment
`literature/2026-11-04-strong-log-concavity-exceptional-minor-test.md`.
Main gap: actual-Xi exceptional signs and all-degree positivity.
One target: the exact positive-entire order-five countermodel named
there. A negative minor together with every ratio and every-iterate
certificate stops only the generic coefficient implication. It cannot
decide signs under the missing actual-theta moment constraints.

Construction to check: symmetric prefix
`(10^-12,10^-6,10^-2,3/5,1,3/5,10^-2,10^-6,10^-12)`.
For k>=0 extend b_(8+k)=10^-12 (10^-6)^k 4^(-k(k+1)/2).
This follows the cited small-diagonal perturbation of a tridiagonal
Toeplitz model. Exact determinant and prefix ratios remain to check.
The tail should have every adjacent ratio 4, including index 8,
and successive quotient tending to zero, proving entire convergence.
McNamara–Sagan Lemma2.1 should then preserve r_0-factor
log-concavity; strict positivity requires explicit treatment of index0.
No finite iterate preview will replace that theorem.

Continuation test: prove all those properties and a strictly negative
D_(5,4), or retain the failed parameter choice without asserting a
universal obstruction. Do not broaden to other orders or actual-Xi.
L021/L771 motivate only; neither L766 nor the Liu–Mao lead is an input.

Completed: the canonical proof is
`lemmas/L772-positive-entire-infinite-log-concavity-negative-minor.md`.
The exact finite certificate passes every check; reversal-block
factorization also proves its negative sign independently of the
120-term expansion. The canonical proof supplies all tail, convergence,
strictness and preservation-theorem obligations. The interim unverified
construction above is preserved as working history. The new next audit
assessment awaits separate approval; this turn is not its audit.
