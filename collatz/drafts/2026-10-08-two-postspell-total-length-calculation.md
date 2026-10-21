# 2026-10-08 — Total represented length working record

The approved target is an explicit absolute ceiling for represented N
in L031's actual closed two-postspell language. The main gap remains
universal eventual descent. A ceiling could support later integer-closure
analysis; it does not supply entry, exclude other cycles or divergence,
or prove the closed-root divisibility impossible.

Pre-invocation coverage is SPECIALIZE in
`drafts/literature/2026-10-08-two-postspell-total-length-bound.md`.
L035 and audited L038 have been read in full. History 085 confirms the
audit; history 069 and Attempt 019 retain their scope/guard failures.
No source refresh, parameter screen, or new general theorem is needed.

Saved intermediate calculation before canonical write-up:
let P_i=4J_i+H_i. Then K=P_1+P_2-J_1-J_2<P_1+P_2,
and L038 gives K<288 log N+190. L035 gives
0<Lambda=N log 2-K log 3<46/517, since n,x>=47.
The exact comparison 3^5=243<256=2^8 gives
log 3/log 2<8/5; the previously proved log 2>2/3 gives
Lambda/log 2<69/517<1. Thus
N<(2304/5)log N+305.

Candidate ceiling: N<4500. For t>=4500,
F(t)=t-(2304/5)log t-305 has positive derivative.
The positive exponential series gives e>8/3 and
8^9=134217728>4500*3^9=88573500, hence log 4500<9.
Therefore F(4500)>4500-20736/5-305=239/5>0,
contradicting F(N)<0 whenever N>=4500.

This eliminates an uncontrolled tail term by using N log 2 rather
than trying to bound each tail first. It keeps both tails independent,
represented rather than primitive counts, exact parities and x=n.
The closure language remains conditional, with no existence claim.
The next write-up must retain all of these guards and exact arithmetic.
