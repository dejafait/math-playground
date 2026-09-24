# First center correction — 2026-09-12

Checkpoint: existing L146 is complete; existing changes are preserved. The current task is the first correction to L138, not a lower-bound proof.

Candidate, not yet proved at this checkpoint: with b=−π/4−iℓ(t), the local ratio is exp(bv)[1+(5v/2−iv²/4)/t]+O(exp(−πv/4)(1+|v|⁴)/t²). Gaussian integration would give the correction series with multiplier 5d−i(d²+1/2), d=b+i log n.

Resume by checking the 5/2 amplitude coefficient, controlling derivatives of the analytic Stirling remainder by Cauchy estimates (not formal differentiation of big-O), and handling all Gaussian tails. Then justify polynomial-weighted Fubini and state the lower bound needed for the corrected sum. No cancellation claim is proved by this checkpoint.

Completed: L147 proves the correction formula with a uniform additive O(t^(−2)) remainder. Cauchy estimates justify the Stirling remainder difference; Gaussian moments give the stated multiplier. The lower bound for the corrected sum remains unproved.
