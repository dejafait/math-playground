# Fourth-moment checkpoint — 2026-09-12

Existing work through L149 is complete and preserved. Current calculation:
remove the unit phase as in L149 and square the Dirichlet series. Group by
k=mn, with coefficient a_k(t)=sum_{mn=k}b_m(t)b_n(t). For N=sqrt(T/(2π))
and M=N², the L149 envelope gives A_k=C N^(-4)d(k)f(k/M),
f(x)=min(x²,x^(-4)), since f(x)f(y)≤f(xy).
Each individual four-weight product is unimodal in log t, permitting the
same integrated off-diagonal bound 4 A_k A_l/|log(k/l)| even though the
grouped coefficient itself need not be unimodal. Use d(k)²≤d_4(k) and
sum_{k≤X}d_4(k)≤X(1+log X)³. Near pairs can be bounded by 2ab≤a²+b²,
then a harmonic sum; expected fourth moment O(T^(-2)log(2T)^4).
Together with L149 this gives a set of measure at least cT/log(2T)^4
where |S|≥c' T^(-3/4), not a positive-proportion conclusion.
Resume by verifying weighted divisor sums, all infinite tails, and the
Cauchy–Schwarz measure deduction. Claims here are draft until recorded
and reviewed in the lemma.

Completed in L150: the grouped envelope has total mass O(N^(-2)log M),
not the smaller original-envelope product bound. This still controls far
pairs within the stated fourth-moment bound. All estimates and the measure
deduction are proved in the lemma; positive proportion remains unproved.
