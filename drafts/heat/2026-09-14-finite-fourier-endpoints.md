# Finite Fourier endpoint checkpoint — 2026-09-14

Working on the retained divisor sum with D=N^(1/4). Proposed construction:
use the centered sawtooth with value zero at integers and its ordinary
Fourier truncation H=ceil(N^6). Keep the exact half-atoms at both endpoints.
For distance at least rho=N^-3 the tail is O(1/(H rho)).
For closer phases, multiplying out the square gives distance less than
1/4 between the integer product abcd (or ab(cd+1)) and t²+R
(or t²-R+1), for a nearby multiple t of e. For each a,t there is at
most one integer product value; elementary divisor bounds then give
O(N^epsilon) triples. Counting a,t and divisor multiplicity should cost
O_epsilon(N^(1+epsilon)h), negligible against B_0.

Checkpoint claims are unproved until the two product counts, Fourier
endpoint conventions and aggregate errors have been checked. Resume there.

Completed in L230. Both product counts work: the upper endpoint uses
b|q/a followed by cd=q/(ab)-1. Near endpoints, including atoms, cost
O_epsilon(N^(1+epsilon)h). The ordinary Fourier tail outside rho=N^-3
costs O(N^-1 h log N) at H=ceil(N^6). The exact sawtooth convention
introduces minus one half of each endpoint atom. No cancellation in
the resulting finite sum has been proved.
