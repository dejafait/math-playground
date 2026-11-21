# Jensen-disk model calculation — step116

Gate: reuse unchanged EXPLORE assessment
`literature/2026-11-09-kim-disk-free-endpoint-test-115.md`.
Only its rescaled trigonometric-polynomial endpoint test is attempted.

Candidate: f(z)=(cosh(2pi)+cos(8pi z))/(cosh(2pi)+1).
The exponential quadratic from L052 gives potential zeros
(2k+1)/8 +/- i/4, k integer. Their disks have radius1/4 and
centers spaced1/4; nearest-center distance is at most1/8.
Proof obligations: no omitted zeros; simplicity; nonconstant real-even
entire and f(0)=1; order/genus<=1 from a growth bound and named Hadamard
factorization; exact union covers every real point, not a finite plot.

Completed: all obligations above are proved in canonical
`lemmas/L956-generic-strip-hypotheses-do-not-give-jensen-disk-free-endpoints.md`.
The exact nearest-center bound is1/8 against required radius1/4,
so both real tails and the entire intervening line are covered strictly.

This is an elementary specialization/model obstruction, not a new Xi
estimate or claimed novelty. Independent critical-zero, actual-theta
and all-degree sign gaps remain. No numerical script was needed.
