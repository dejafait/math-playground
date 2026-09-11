# Draft checkpoint — long-cell coprime windows

The completed L198 checkpoint is preserved. This step isolates a sufficient
family for its count, not a claimed positive-proportion lower bound.

Choose an integer W of order N^(3/2), with W<=R. For m safely inside
[a−,a+] and with 2m rho-rho²>=W, the full displacement interval
[-W,W] lies in every cutoff except the floor cell. It also lies in that
cell exactly when uv+W<=m²<=u(v+1)-1-W. The positive m window
therefore has explicit square-root endpoints and bounded length.

Resume by proving the exact Möbius count on this window, imposing the
remaining safe-m cutoffs explicitly, and comparing its divisor error
with the O(N³) available pair quadruples. A positive lower bound is
unproved; a bounded window cannot automatically be assigned coprime
density. Check all closed endpoints and distinguish ell=t-b from
integer cardinality. No draft assertion is a DAG input yet.

Recovered 2026-09-14 (Codex, GPT-6): the exact lower endpoint is the
maximum of sqrt(a−²+W), sqrt(uN²+W), sqrt(uv+W), and
(W+rho²)/(2rho). The upper endpoint is the minimum of
sqrt(a+²−W), sqrt(4uN²−W), sqrt(u(v+1)−1−W).
Negative upper radicands mean an empty window. In the central strip,
the floor-cell window alone has length <1 for sufficiently large N.
Thus the full window contains at most one integer. The exact divisor
count has absolute error at most 2^omega(u) relative to real length
times phi(u)/u; this bound is already larger than that main term for
each nonempty window. Resume by storing the qualified identity and
error obstruction as L199, checking endpoints computationally, and
updating the sole current status. No lower bound has been proved.

Completed 2026-09-14: L199 stores the proved identity and error
obstruction. Finite endpoint/divisor checks passed. This recovered
step is complete; the lower-bound claim remains unproved. The current
research action is recorded only in PROGRESS.md.
