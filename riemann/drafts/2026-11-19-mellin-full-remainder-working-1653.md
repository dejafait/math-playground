# Full Mellin remainder assembly: working checkpoint1653

Completed later in the same step: canonical C048j contains the full
proof and exact rational replay. The original scratch checkpoint below
is retained as unfinished-work provenance; its pending obligations have
been discharged except the separately nominated independent audit.

Approved target: the exact Next action in assessment
`literature/2026-11-19-mellin-full-remainder-reproduction-1652.md`.
This is REPRODUCTION of Kawano v1 Lemma5.1(i), not a new sign mechanism.

The component statements and necessary normalization/continuation proof
ranges have been read. C048a supplies a fixed-height identity, C048b
combines its vertical primitive and x in [0,1], and C048c gives
S=M Q with M=g(u_0)exp(h_p(u_0)), Q=sqrt(pi/A_0).
For x>=1, s=x-x_0 partitions into [1-x_0,-1], [-1,-d],
[-d,d], [d,infinity]. C048c has x_0>9/2 and 0<d<=1/36.
L799's strip identity alone identifies the full F; its saddle bounds
are excluded. The local F splits as 1 plus the lower-power mode1
plus R_modes. The normalized identity to finish is

    I/S-1 = E_o/S + (J_far+J_near+J_right
             +(J_loc-G_loc)+J_low+J_modes-(Q-G_loc))/Q.

Each J here has the K exp(h-h_0) normalization. The tails include F;
the Gaussian pair is subtracted once. No sum over modes on an infinite
contour is required; C048g supplies right-ray absolute convergence.

Scalar plan: q=e^L/L^2>28 for L>=12, using its positive derivative
and e^12>4096>28*144. The ratio of C048f's allowance to L^(9/2)/r
is 112q exp(-5q)/L^2 < (196/9)exp(-140)
<196/(9*2^20)<1/10000. Justify monotonicity of q exp(-5q)
and every strict numerical comparison in the final proof.
The lower-power ratio is <2/L^3<=1/864. The four rounded component
coefficients sum to 1.605195; adding three 1/10000 allocations and
1/864 is below 17/10. These are scratch calculations pending final
exact arithmetic and complete written proof.

Remaining obligations in this attempt: finish that proof with real,
reflected and closed-boundary cases, record exact arithmetic evidence,
canonical corollary/DAG, compact checkpoint/history, and scoped checker.
The main actual-Xi positivity, zero counts, finite regions, inversion,
C028b H_d=o(d), C028g S_F=0 and sign bridge remain unresolved.
