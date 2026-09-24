# Totient threshold checkpoint — 2026-09-14

Proposed proof, not yet promoted: write P_N for the first-pair count
in L202, so #F_N=P_N² and P_N>=(t/48)N^(3/2).
For each prime p<=2N, count either factor divisible by p using at
most N/p+1 multiples in [N,2N] and at most t sqrt(N)+1 partners.
Eventually this gives proportion <=192(1/p+1/N). The finite
identity log(ab/phi(ab))=sum_(p|ab) log(p/(p-1)) and
log(p/(p-1))<=2/p should bound its pair average by 768.
Markov with B=2^25 would delete at most 3/131072 of all tuples,
leaving more than 3/131072 after L210. Set eta=exp(-B).

Resume by checking both factor orientations, real-N endpoint rounding,
the average constant, and the subtraction without any independence
assumption. The negative-strip mass assembly is outside this step.

Completed: both orientations and the average bound check out. The proof
is stored in `lemmas/L211-totient-threshold-on-the-coprime-population.md`.
No independence is needed; deletion occurs in the whole Cartesian box.
