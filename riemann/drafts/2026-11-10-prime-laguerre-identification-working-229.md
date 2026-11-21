# Fixed-n identification working record — step229

Approved target: identify the fixed-n real-cutoff limit of L981's
P_n with the nonalternating S_f in L977/L980. Reuse SPECIALIZE
assessment review227 as supplied and completed in step228.

Finite assembly to check: write the degree n-1 polynomial with
coefficient binom(n,j+1)*(-1)^j/j!. Its compensator from1 is
(log X)^(j+1)/(j+1). The cited fixed-j compensated moment has limit
(-1)^j*j!*eta_j, so the finite coefficient product is binom(n,j+1)*eta_j.
No limit in n is being taken.

Endpoint check: N=floor X gives exactly the same complete finite
prime-power sum. For N>=3 the remaining compensator has modulus
at most 2^n*(log(N+1))^(n-1)/N, tending to zero at fixed n.
Thus no half-weight prescription or prime jump estimate is needed.

Keep this reasoning if all signs, factorials and lower endpoints
match; abandon downstream normalization use on any mismatch.
The n-uniform signed bound, actual-Xi positivity and L975/L976/
step224 obstructions remain unresolved. No new central sign
mechanism is claimed. The completed canonical proof is L982; this
working record is not a substitute for it or an independent audit.
