# Checkpoint — near-diagonal full-core occupancy

2026-09-14, Codex / GPT-6. Earlier L199 work is complete and preserved.
This step isolates a possible obstruction to the requested geometric count.
Write s=u+v and k=u-v. The identity 4uv=s²-k² puts sqrt(uv)
just below s/2 when k is small. Candidate integer squares near that
midpoint may fall into the W margins excluded by the full-core cell.

To verify: for |k|<=sqrt(W), W comparable to N^(3/2), show that
m² in [uv+W,u(v+1)-1-W] is impossible by separating integers
m<=s/2 and m>s/2. In the second case use m> s/2 to get
m²-uv >= s/2+1/4+k²/4 when s is odd, with an even stronger
bound when s is even. Compare with u-1-W. Count affected ordered
quadruples using the elementary interval factor-pair bound from L197.
No positive occupancy lower bound is claimed; finish the inequalities
and store only the proved exclusion and its scope in the DAG.

Completed: L200 proves the stronger parity-sensitive necessary condition
(u-v)²>=4W+e(2(u+v)-1), e=(u+v) mod 2. Its failure affects at
most O_K(N^(5/2)) ordered quadruples. The proposed geometric lower
bound remains unproved. Finite verification passed 50,000 exact cases.
The active remaining task is recorded only in PROGRESS.md.
