# Transition weight removal — 2026-09-14

Checkpoint: existing L225 is completed; preserve all prior changes. For selected
candidates m=k_b in J coprime to a, replace W_b by H_m=(B_m-A_m)/R.
A deficient overlap implies |abcd-m²|<=R+1 or |ab(cd+1)-m²|<=R+1.
There are O(hR) pairs (m,integer product); factorization multiplicities
are O_epsilon(N^epsilon), so the aggregate loss is O_epsilon(N^(3+epsilon)),
which is o(T) for epsilon<1/2. Need write the elementary uniform divisor
bound, cover zero overlap and strict cell endpoints, and validate identities.
Unselected candidates remain zero; no fractional-part equidistribution claimed.

Completed: the endpoint argument and divisor count are proved in L226.
No distributional claim was promoted. Current next action is in PROGRESS.md.
