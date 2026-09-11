# Fixed-box single-candidate checkpoint — 2026-09-14

The previous L217 step is complete; preserve all existing changes.
Current scoped task: reduce its fixed-box arithmetic mass to one exact
integer candidate per ordered quadruple, not assert the requested bound.

Write u=ab, v=cd, x=sqrt(uv), and x_R=sqrt(uv-R).
The necessary cell interval for m is
[x_R,sqrt(u(v+1)+R-1)]. On c,d in [1.6N,1.7N],
u<=4N² and v>=2.56N² make its length at most
u/(2sqrt(uv-R))+o(1)<=5/8+o(1)<1.
Thus the sole possible m is ceil(x_R); retain the exact endpoints
of L191 and gcd(m,u)=1. Need prove uniform bounds and weighted
normalization carefully. With actual a± near 2N², a fixed margin
inside their interval makes non-floor cutoffs inactive except R and
rho. This latter simplification is optional and is not yet proved.

Resume by establishing the exact single-candidate formula, then the
square-product exclusion (the candidate is the integer root, hence
not coprime to u>1), and a weighted counting criterion. Do not claim
an occupancy distribution or lower bound. Validate the finite formula
against brute-force exact cells on rational/integer test parameters.

Completed outcome: L218 proves the single-candidate formula, square
exclusion, and equivalence to Q_N=O(N³). The optional interior cutoff
simplification was not needed or asserted. All original endpoint cutoffs
remain in e. The elementary support count yields only O(N^(7/2));
the stronger estimate remains unproved. The completed proof and exact
finite checker supersede the provisional reasoning above.
