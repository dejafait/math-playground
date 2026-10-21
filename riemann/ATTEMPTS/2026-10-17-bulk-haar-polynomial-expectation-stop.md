# Stop: angular polynomial interpolation with independent Euler boxes

The complete proof, hypotheses, source specialization and arithmetic
evidence are canonical in [L426's step-192 section](../lemmas/L426-covariance-free-bulk-actual-height-phase-average.md). Full certificates:
`scripts/discriminant/bulk-haar-polynomial-preflight-192.json`,
`scripts/discriminant/bulk-haar-polynomial-nodes-192.json`, and
`scripts/discriminant/bulk-haar-polynomial-expectation-192.json`.

WHY IT FAILS: Refining only unresolved angle cells makes the degree-32
analytic interpolation remainder useful (symmetric width about .07234),
but every angular node interval and every resulting Chebyshev coefficient
interval contains zero. The signed full Euler calculation through order
448 also loses cancellation: 27 of 32 raw nonconstant Chebyshev-moment
intervals cover [-1,1]. Even after imposing that exact bound, the final
envelope expectation is approximately [-2.62435,2.61595], of width
5.24030 against the required .229997. Both sign and material-narrowing
tests fail. Stop this independent coefficient/moment-box implementation.
The failure is not a lower bound on optimal approximation error, a
measured irreducible source floor, or a proof of I=0. The stronger
step-190 enclosure and all prior stops remain intact. A direct conditional
angular-sign test would have to avoid the large moment cancellation and
receive separate coverage; it is only a proposed continuation.
