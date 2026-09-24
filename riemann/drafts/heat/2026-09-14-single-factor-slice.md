# Single-factor slice checkpoint — 2026-09-14

Inspecting L218's completed result, not repeating its proof. Fix a,c,d,
v=cd. The necessary cell inequalities inverted in b give
[(m²-R+1)/(a(v+1)), (m²+R)/(av)]. Intersect with [N,2N].
Keep exact e and gcd(m,ab) for integer b; this is only a support interval.
Distinct m intervals are disjoint eventually by L218's width argument.
For interior m of size N² the interval width is comparable to 1/N.
There are O(h) such m, while the full b support has length O(h/N).
Thus summing interval lengths gives O(h/N), already sqrt(N), not O(1).
Need to state and prove a conditional interior-slice lower bound for the relaxed
real measure, distinguishing it from the integer weighted population.
No population lower bound or desired O(N³) estimate is proved.

Completed: L219 establishes the exact slice and disjoint inverse intervals,
the existing O(sqrt(N)) bound per slice, and the conditional real-measure
obstruction. The real-volume shortcut is archived under ATTEMPTS. Integer
occupancy discrepancy, including coprimality, remains unproved.
