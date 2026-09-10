# Lemma 57: any fixed number of Hankel tests can coexist with nonreal zeros

**Hypotheses.** N≥0 is a fixed integer. F_a is the family of Lemma 55, extended at a=0 by F_0=G. Define each H_d(F_a) from the paired reciprocal-zero power sums, equivalently from its local logarithmic coefficients.

**Conclusion.** There exists a_N∈(0,1/100] such that H_d(F_{a_N}) is positive definite for all 0≤d≤N, while F_{a_N} has nonreal zeros and every generic property in Lemma 55. The choice of a_N is allowed to depend on N; no single nonzero a is asserted to pass all degrees.

**Proof.** The entire-order, evenness, and positive-at-zero hypotheses needed for the paired product and local logarithmic identities hold for every F_a and for G by Lemmas 51, 55, and 56. Also F_a(0)=G(0)>0 exactly. The explicit factor

F_a(z)/G(z)=[cosh(a/10)+cos(az)]/[cosh(a/10)+1]

tends to 1 locally uniformly as a tends to zero. In particular each fixed Taylor coefficient of F_a tends to that of G. This also follows directly without differentiating a limit: integrate the finite binomial expansion for each shifted moment of g, whose coefficients are continuous functions of a and cosh(a/10).

For each fixed k, the normalized coefficients e_j and the finite Newton recurrence in Lemma 40 show that the reciprocal power sum T_k(F_a) tends to T_k(G). Hence every fixed finite determinant det H_d(F_a) is continuous at a=0. Lemma 56 makes det H_d(G)>0 for each d. For the finitely many d=0,…,N, choose a common sufficiently small positive a_N≤1/100 so that all those determinants stay positive. Sylvester's criterion, or successive completion of squares, then makes each H_d(F_{a_N}) positive definite. Yet Lemma 55 supplies its nonreal zeros (2k+1)π/a_N±i/10 and all the other stated properties. ∎
