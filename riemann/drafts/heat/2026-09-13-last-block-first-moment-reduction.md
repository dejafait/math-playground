# Last-block first-moment reduction — 2026-09-13

Checkpoint before proof audit. Earlier finite probe is complete and preserved.
At H=T^(3/4), the last midpoint has u=2−h/(2T). Replace the
normalized coefficients by their u=2 profile. Their differences and
x derivatives are O(h/T), so the elementary off-diagonal frequency
bound gives an L2 replacement error O(h/T), hence O(T^(−1/4)).
This is a proposed estimate pending the full proof below/in the lemma;
it does not establish vanishing first moments.

Resume by checking normalization constants, finite endpoint convention,
and Abel summation of the limiting decreasing weight against partial
Dirichlet sums. The desired cancellation estimate remains unproved.

## Completed audit

The estimate is proved in L173, with error O(T^(−1/4)). The exact
normalization is N^(−1/2)b_u(n/N), and the limiting squared profile
integrates to one. Finite Abel summation gives a sufficient unweighted
partial-sum first-moment condition. Ordinary second-moment estimates
supply only O(1) for the normalized first moment, so vanishing is still
unproved. No additional computation or phase-distribution theorem was
used. The next unresolved calculation is the first moment of P_y on
the actual moving last block, at the o(sqrt(N)) scale.
