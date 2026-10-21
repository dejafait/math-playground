# 2026-10-08 — Uniform multiword length assembly working record

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-08-multi-postspell-represented-length-bound.md`.
The main gap is universal eventual descent. The approved intermediate
target is explicit A(r),B(r) with N<A(r)log N+B(r) for the stated actual
closed r-word language. A fixed-r ceiling could support a later restricted
cycle exclusion; entry, other cycles and divergence remain independent.
Continue only with controlled cyclic transfer and a useful r=3 ceiling
below 225640000. Attempt 019 and history 069 remain valid obstructions
to guard-only and designated-count-as-full-minima arguments.

Saved before canonical write-up: L035's single-word estimate can be summed
over r disjoint half-open input intervals. Thus Lambda<(23/11)sum 1/n_i,
and with b=min n_i, the published lower bound gives
b<(23r/11)exp(6.125581)K^(133/10). Since b>=47, this should imply
h_0=log(b+23/11)<(133/10)log N+8+log r.

Use the finite-word portions of L031 and L038 at each own starting
occurrence. With h_j=log(n_j+23/11), P_j=4J_j+H_j, they give
P_j<(15/4)h_j+3 and h_(j+1)<h_j+P_j/2.
Consequently h_(j+1)+4/5<(23/8)(h_j+4/5).
For Q_r=sum_(j=0)^(r-1)(23/8)^j, summing should give
K<sum P_j<(15/4)Q_r((133/10)log N+44/5+log r).
The same Lambda is <23r/517, so
N<(8/5)K+69r/1034.
Candidate functions: A(r)=(399/5)Q_r and
B(r)=(264/5+6log r)Q_r+69r/1034.

For r=3, Q_3=777/64, A(3)=310023/320<969, and using
log3<4/3 should give B(3)<739. The candidate inequality is therefore
N<969log N+739. Exact check proposed: log11000<10 follows from
e>8/3 and 8^10=1073741824>649539000=11000*3^10.
The function t-969log t-739 increases for t>=11000 and is then
positive, since 11000-9690-739=571>0.

These are unfinished assembly notes, not an independent audit. The
canonical proof must check all occurrences, primitive scaling, both
shifts, positivity, constants and independent tails. No mathematical
script or numerical screen is needed for the exact rational comparisons.

Completed in L041: all proposed functions and the r=3 ceiling were
written with complete occurrence, scaling, valuation and transfer
justifications. The exact rational and exponential comparisons establish
N<11000, passing the usefulness test. This is a local REPRODUCTION
advance, awaiting separate critical audit; the notes above preserve
the pre-write-up calculation and are not a substitute for the canonical
proof or an audit record.
