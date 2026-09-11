# Checkpoint — full-core phase reduction

2026-09-14, Codex / GPT-6. Prior L200 work is complete and preserved.
This step treats the geometric occupancy question without coprimality.
For x=sqrt(uv), W>0 forces the first possible integer to be
m0=floor(x)+1, including when x is integral. The central-strip
floor-cell width is less than one, so this is the only candidate.
Its exact square displacement is 2x g+g², g=1-frac(x).
Retain the other L199 inequalities explicitly at m0.

For |u-v|=O(N^(3/2)), s=u+v comparable to N², expand
x=s/2-k²/(4s)-k⁴/(16s³)+O(N^(-1)). The quartic term is
order one and cannot be omitted in an o(1) phase approximation.
To finish: prove the uniform remainder, give an exact-arithmetic
verification of the candidate criterion, and state a sufficient interior
phase interval. No N³ phase-population lower bound is yet proved.

Completed in L201: the exact criterion retains all safe-m cutoffs;
the quartic approximation has a proved one-sided O(N^(-1)) error.
A fixed interior phase interval suffices for the floor-cell part.
10,000 exact candidate checks and rational Taylor bounds passed.
The N³ simultaneous phase-and-cutoff count remains unproved;
its active next action is recorded only in PROGRESS.md.
