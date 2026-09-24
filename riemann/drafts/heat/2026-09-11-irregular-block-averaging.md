# Irregular block averaging — 2026-09-11

Checkpoint: candidate UNPROVED pending audit. For B=S∩[N,2N), M=|B|>0,
A=min_{n∈B} x_n/sqrt(n), the increment crossing count at separation k
is at most min(k,M). Its reciprocal-square weighted sum is at most
2+log M. Hence average Q ≤16H N(2+log M)/(M A²).
Selected blocks with this ratio tending to zero suffice.

Resume by checking the crossing bound and constructing an explicit case
outside both previous hypotheses. Proposed coordinates: x_n=n on
[16^k,4·16^k]; on (m,T)=(4·16^k,16^(k+1)), set
x_n=sqrt(T n)(1+(T-n)/(4T)). These gap interiors have decreasing a_n,
while x_n increases; suffix set should be exactly the dense intervals.
Check boundaries, summability, divergent suffix weights and empty dyadic
blocks before promoting anything. General unrestricted assertion remains
unproved.

Completed audit: the criterion and example are proved in
`lemmas/L090-upward-averaging-on-selected-irregular-blocks.md`.
This draft is superseded for those claims. The unrestricted assertion
is still unproved; the remaining block-ratio regime is explicit there.
