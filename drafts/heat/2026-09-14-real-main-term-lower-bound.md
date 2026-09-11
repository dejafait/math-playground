# Real main-term lower-bound checkpoint

Restrict a to [11N/10,6N/5], retain every c,d in the fixed box,
and restrict m to the middle half of [a−,a+]. Then m/N² tends
uniformly to 2 and m²/(acd) stays strictly inside [N,2N].
A plateau in the exact f_m has height bounded below and width
comparable to 1/N: use displacements ±w with
w=min(R/4,m rho/4), and x between (m²+w)/(a(v+1))
and (m²-w)/(av). Check the upper endpoint's minus one explicitly.
Count coprime a,m by a union bound over primes <=6N/5; the main
excluded fraction is at most sum_{n>=2}n^-2<=3/4, with lower-order
interval errors. Universal phi(n)/n>=1/(1+log_2 n) suffices for
M_tot >= c N^(7/2)/(log N)^2, which exceeds N³.
Resume by verifying all rounded cutoffs and the coprime count, then
record a lemma and conditional signed-discrepancy consequence.
No integer population lower bound or cancellation is proved here.

Completed: L221 proves the lower bound. The plateau lower endpoint
includes +1 in its numerator to preserve the strict floor endpoint.
The coprime count uses a finite prime union bound; a universal
logarithmic totient bound suffices. No unfinished claim in this draft
is promoted beyond L221's stated result.
