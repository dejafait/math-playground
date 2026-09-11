# Displacement interval and Möbius checkpoint

Prior L190 is complete. For fixed u,v,m in M with gcd(m,u)=1, intersect
[-R,R], [a−²−m²,a+²−m²], [−2m rho+rho²,2m rho+rho²],
[uN²−m²,4uN²−m²], and [uv−m²,u(v+1)−m²).
Take ceilings of closed lower endpoints and floors of closed upper endpoints;
the strict integer upper endpoint is u(v+1)−m²−1. Remove r=0.
Finite Möbius inversion gives sum_(d|u) mu(d) sum_(ceil(b/d)≤k≤floor(e/d), k≠0) H_m(dk).
H is affine in r, so use exact count and arithmetic-progression first moment.
Resume: prove equivalence, implement exact rational endpoint and weighted checks,
then save L191, graph and history; no cancellation estimate is yet proved.

Completed: L191 gives the exact interval and affine Möbius evaluation.
Exact rational endpoint and weighted regression checks passed. Cancellation
and endpoint-error estimates remain unproved.
