# Coprime population checkpoint — 2026-09-14

Candidate combination, not yet promoted at this checkpoint: fix z=65536
and D equal to the product of primes at most z. The product over odd
integers gives phi(D)/D >= (1/2) product_(j=1)^32767 2j/(2j+1)
>= 1/(2 sqrt(65535)) > 1/512. The second inequality follows by
squaring each factor and telescoping (2j-1)/(2j+1).
Thus c_D/2 > 3/65536, whereas 2 sum_(p>z) p^(-2) <= 2/65536.

Resume by checking the direction of the product comparison and combining
L207 with Y=z and L209 with Q=N^(1/4). Their errors vanish with fixed
D, so the strict constant margin should prove T_z <= (c_D/2)#F_N
eventually. No uniformity in D or effective threshold in N is claimed.
The remaining totient selection is outside this step.

Completed: the product direction and all error limits check out. The
proof is stored in `lemmas/L210-positive-proportion-coprime-factor-population.md`.
The strict margin permits a total asymptotic error of 1/65536.
