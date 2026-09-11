# Critical buffer sharpness checkpoint — 2026-09-11

Construction under audit: fix c>0, A_n=4^n, d_n=c sqrt(A_n log A_n), u_n=A_n+2d_n, and M_n=floor(A_n log A_n). Place multiplicity M_n at each of ±u_n±i and simple target zeros at ±A_n±i/2, starting sufficiently late that 2d_n<A_n/2. At w_n=A_n+i/2 and R_n=A_n+d_n the positive upper cluster contributes M_n/(4d_n²+1/4)→1/(4c²).

Unproved checkpoint: verify counting, reciprocal squares, and that all other exterior upward terms vanish if claiming the exact limit. Earlier clusters should be inside R_n; future clusters are geometrically separated and give O(log A_n/A_n). No theta realization or net signed upward motion is claimed.

Completed: the counting, cutoff, and geometric-tail audits establish the exact limit in L132. The earlier unproved checkpoint is resolved.
