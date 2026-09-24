# Power-gap nonexplosion checkpoint — 2026-09-11

Existing Lemma 107 is complete and all earlier changes are preserved.
The universal coordinate question is too broad for the present step;
we test the forward process on a precisely scoped class.

Draft claim (unproved at this checkpoint): if for some a>1/2 and c>0,
x_j-x_i >= c(j^a-i^a) for every j>i, then the process in Lemma 107
has infinite lifetime almost surely from every starting index.
Choose 0<p<2a-1 and f(i)=i^p. Its generator should be bounded by
C i^(p+1-2a)(1+log i), hence uniformly bounded. Split the sum into
i<j<=2i and j>2i; derivative bounds handle the first part and a
convergent power tail handles the second.

Resume at the proof audit: use the capped function min(i^p,R^p) and
stop at the first index >=R. This gives a finite-state chain with an
absorbing exit state, avoiding any assumed nonexplosion in a Dynkin
formula. Bound the exit probability by (n^p+Ct)/R^p and let R grow.
The general summable-coordinate assertion remains unproved. No claim
that reciprocal-square summability implies the power-gap hypothesis.

Completed: the derivative estimates, power tail, uniform generator bound,
and finite-state exit argument are proved in Lemma 108. The draft claim
above is now established under its stated power-gap hypothesis. The
universal question remains open; no failed counterexample was produced.
