# Multiset height selection — 2026-09-11

Draft checkpoint (unproved pending audit): enumerate copies of upper-half-plane
points z_i with bounded positive heights and sum (1+|z_i|^2)^(-1)<infinity.
Use auxiliary distinct t_i near 1+|z_i|, perturbing by less than
min(1, one quarter of the distance from z_i to any distinct location).
For distinct locations, |t_i-t_j| <= (3/2)|z_i-z_j|, so exact
height-directed rates 1/|z_i-z_j|^2 are bounded by (9/4)/(t_i-t_j)^2.
Copies at the same location never interact upward. Order t_i and apply
L122's payoff, then repeat L124's finite cutoff and bounded-height
argument. This covers both signs of the real part without a reflection
term. Resume by auditing discreteness, choice and summability of t_i,
rate finiteness, and the no-repeated-state cutoff argument.

Completed: the audited argument is stored in Lemma 125. The auxiliary
coordinates dominate exact rates only between distinct locations, which
is sufficient because transitions require strictly increasing heights.
All multiplicities are retained in coordinate summability and rate sums.
No unfinished claim from this draft has been promoted without proof;
heat-parameter uniformity remains outside the result.
