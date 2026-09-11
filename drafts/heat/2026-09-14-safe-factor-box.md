# Checkpoint — safe factor box before phase selection

2026-09-14, Codex / GPT-6. L201 is complete; existing changes preserved.
Scoped calculation: put V=2N², L=N^(3/2), H=h/(2πL), and
choose a fixed t>0 with 2t<K and 4t<inf H for large N.
Restrict both products to [V-2tL,V-tL], and their first factors
to [11N/10,6N/5]. The second factors approach [5N/3,20N/11],
so they are in the original support and on the opposite side of sqrt(2).
Each pair population should be bounded above and below by constants
 times L, giving order N³ quadruples. For m0=floor(sqrt(uv))+1,
all safe-m cutoffs should hold uniformly when 0<W<=min(R,L).

Resume by proving the integer pair lower bound and all three safe-m
inequalities, with the actual a±=V-1/4 and V-h/(2π)-1/4.
The phase interval selection is UNPROVED: a Cartesian product count
cannot be promoted to the requested full-core occupancy lower bound.

Completed as L202: the integer pair counts give order N³ tuples;
the exact candidate satisfies every safe-m cutoff, with uniform margins.
The phase-selected population remains unproved. Finite verification:
8,000 exact candidate checks and 520 selected floor-cell checks passed.
The current continuation is recorded only in PROGRESS.md.
