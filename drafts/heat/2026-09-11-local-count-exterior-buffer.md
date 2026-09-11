# Local-count exterior buffer checkpoint — 2026-09-11

Proposed calculation: for a strip multiset with count in [x,x+1) at most C log(2+|x|), cover each of the two distance shells 2^k d≤|u−a|<2^(k+1)d by at most 2^k d+1 unit intervals. For d≥1 their total mass is at most 4C 2^k d log(3+A+2^(k+1)d). Division by (2^k d)^2 and summation should give

S≤(8C/d)[log(3+A+2d)+log 2].

Unproved checkpoint: audit interval endpoints, constants, arbitrary buffer limits, and the conditional substitution into L129's local rate formula. Resume by proving the shell bound and comparing log(3+A+2d)/d with log A/d. No claim about local counts for theta slices, optimal actual buffers, or RH is made.

Completed: the endpoint cover and limit audit are resolved in L133. The logarithmic sufficient scale is proved under the additional local count; actual-scale sharpness remains unproved.
