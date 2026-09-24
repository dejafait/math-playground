# Density first-moment checkpoint

The L192 checkpoint is complete and preserved. Split its affine integral
into Z_G and Z_C, retaining phi(u)/u, gcd(m,u)=1 and P,Q.
Proposed proof, not yet established at this checkpoint: outside O(1)
stationary-endpoint m values and floor-boundary pairs with
|m²-uj|<=R+2, the integer displacement interval has b+t=O(1).
Its first moment is O(R), rather than O(R²). For each m, boundary
pairs u can be counted by divisors of m²+r, |r|<=ceil(R)+2,
giving O_epsilon(R N^epsilon) weighted pairs. Their C contribution
should be O_epsilon(h N^(1/2+epsilon)), hence o(Nh).
Resume by checking all support boundaries and integer endpoint gaps,
proving the divisor accumulation, and testing the interval classification.
The G interval-mass term remains unproved.

Completed: L193 proves the C first-moment contribution is o(Nh).
The exceptional floor/support pairs admit a weighted divisor count;
the ordinary intervals have b+t=O(1). Exact rational interval checks
and the structural checker passed. The G interval-mass contribution
remains unproved and is the explicit remainder of the requested step.
