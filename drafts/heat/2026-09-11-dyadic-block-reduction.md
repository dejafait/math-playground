# Draft: dyadic block test versus unrestricted counts — 2026-09-11

Let S be the union of [2^j,2^(j+1)-2], j>=1. Map each positive
integer k to T(k)=min{s in S:s>=k}. Then k<=T(k)<=k+1,
T is nondecreasing, and each fiber has at most two elements.
For arbitrary summable positive integer counts m_k, put
N_r=sum_{T(k)=r} m_k on S. These masses have summable N_r/r^2.
If the requested block theorem supplies H for baseline 1+N, pull back
P(k)=H(T(k)). For distinct images, T(l)-T(k)<=2(l-k), so
QP(k)<=4 QH(T(k)); equal images contribute zero. Weighted integrability
pulls back with factor four. Add B(k)=1-1/(k+1) for strict increase.
Its generator is bounded by sum m_l/l^2, since
(k+1)(l-k)>=l for integers l>k. Thus the block existence statement
implies the unrestricted statement; the converse is immediate.

Checkpoint: this is an unproved draft pending audit of missing sites,
finite fibers, grouping all destinations, weighted bound, and the exact
quantifiers in the equivalence. It does not establish existence for either
class. Resume by making that distinction explicit in a canonical lemma.

Audit completed: the equivalence is stored in Lemma 117. The proof
removes equal-image terms before division and uses only nonnegative
series grouping. The bounded correction has generator at most the
original weighted mass sum. Neither universal existence assertion is
promoted to a proved premise. This completes the reduction substep.
