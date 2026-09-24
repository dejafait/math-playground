# Draft checkpoint — unrestricted opposite slice

2026-09-14, Codex / GPT-6. Earlier L207 work is complete and preserved.
For common divisors of m0 and either a or b, fix (a,b,c) and vary d
through its full interval. The divisor condition on the first pair no
longer restricts the oscillatory variable to a progression.
For f(j)=sqrt(abc(d0+j))/p the normalized third-derivative bound is
O_t(k^(1/6)p^(-1/6)N^(-1/6)+k^(-1/6)p^(1/6)N^(-1/12)).
For p<=N^(1/2-eta), H=floor(N^(eta/2)), 0<eta<1/4 fixed,
this is O_t(N^(-eta/6)) for 1<=k<=H.
Use L207's uniform interval majorants with smoothing N^(-eta/4).
Expected discrepancy: O_(t,eta)(N^(-eta/6) log N).
The first-pair divisor frequency remains 1/p+O_t(N^(-1/2)); summing
rounding errors over at most N^(1/2-eta) primes costs N^(-eta).
Resume by checking these exponents and writing the bounded band result.
The tail above N^(1/2-eta) is explicitly unproved. At p comparable to
sqrt(N), the second term of this derivative estimate no longer decays.

Completed: the exponent and uniformity checks are written in L208.
The newly controlled band has relative count o(1); the remaining
large-prime assertion is unproved. The draft is no longer a pending checkpoint.
