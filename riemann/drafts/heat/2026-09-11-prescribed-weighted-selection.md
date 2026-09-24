# Prescribed weighted selection — 2026-09-11

Draft checkpoint: UNPROVED pending audit. Fix N in P and partition [N,2N]
into intervals starting at s in P∩[N,2N), with length d_s equal to the
successor gap clipped at 2N. Their lengths sum to N. Aim to prove for
s<j≤4N the strengthened separation
x_j-x_s ≥ (d_s+j-s)/(16 N^(1/4)).
For j before the actual successor t, use x_j≥sqrt(s)t^(1/4) and
s+d_s≤2N; for j≥t use Lemma 100's global separation. Combine this
new d_s bound with the existing j-s bound. Expanding height increments
then gives coefficients bounded by Σ_{s≤r}d_s/(d_s+r-s).
The intervals ending before r are controlled by the integral of
1/(r-u+1); at most one interval crosses r. Expected bound:
1+log(3N+1), hence weighted average O(H log(N)/sqrt(N)).
Resume by auditing these inequalities, integer endpoints and constants,
then control j>4N and reflected zeros using Lemma 100's tails.
No claim from this draft is a proved DAG input.

Completed: Lemma 101 proves the clipped-gap separation and weighted
coefficient estimate, with full tails, and hence selection inside P.
The draft's claims are now established in that canonical proof.
