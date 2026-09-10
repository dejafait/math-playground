# Multiple-zero checkpoint — 2026-09-10

Draft reasoning, not a proved DAG input. Existing work through Lemma 59 is complete and preserved.

For exact multiplicity m, iterating the heat equation makes the coefficient of t^j w^k equal to (-1)^j F_z^(2j+k)/(j!k!). Rescaling t=s²,w=sv and dividing by s^m should give A P_m(v)/m!, where P_m=Σ_j m!(-1)^j v^(m-2j)/(j!(m-2j)!). Prove its real simple roots by the recurrence P_(n+1)=vP_n-2nP_(n-1) and interlacing, then use implicit branches and Rouché. Negative t rotates nonzero leading roots to imaginary directions; for odd m the central branch needs an exact reality argument (w_0(-s)=w_0(s)), not just its vanishing leading coefficient. Resume with these proofs and uniform remainders. Global collision exclusion is unproved.

Completed in lemmas/L060-local-splitting-at-a-real-multiple-zero.md on 2026-09-10. The polynomial, analytic counting, and odd central-branch claims are proved there. This draft remains only a checkpoint record. Global collision exclusion remains unproved.
