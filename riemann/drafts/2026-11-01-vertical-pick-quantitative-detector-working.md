# Quantitative vertical Pick detector — working checkpoint

2026-11-01. One RESEARCH / REPRODUCTION attempt on the exact target in
`literature/2026-11-01-vertical-pick-quantitative-pole-detection.md`;
its invocation-start SPECIALIZE coverage is reused unchanged.

Main gap: actual-Xi signs at unbounded heights, then all-degree mixed
positivity. Intermediate target: the nominated every-n detector with
sample count bounded by a delta-only constant times 1+log^+ H_rho.
Its downstream use is conditional exclusion from finite matrix positivity;
positivity itself, multiple zeros and height-only growth remain open.

Read L018 and L258 completely, the specific Laguerre and fixed-reserve
stop records, and relevant source-comparison passages. L018 is the
mathematical input; L258 is overlap and C644a only a contrast. Existing
changes and unfinished work are preserved. No cross-notebook input.

Partial reasoning, not yet a completed result: under temporary K_n>=0,
finite Schur interpolation should yield a holomorphic positive-real P
on Re(s)>1/2 with P(s_j)=F(s_j). Set a=3/2, d=a-delta,
R=a-delta/2. Borel–Caratheodory on radius a for -P with real-part
upper bound 1 suggests |P|<=(6/delta-1)(1+|F(s_*)|) on radius R.
The analytic residual E=xi'-P xi vanishes at each sample, while
E(rho)=xi'(rho). Its proposed bound is
(6/delta-1)(1+|F(s_*)|)M_rho. Finite Blaschke division should then
give 1<=(6/delta-1)H_rho q_delta^n if K_n>=0, where
q_delta^2=R^2(d^2+1)/(R^4+d^2)<1. Check the exact Cayley congruence,
singular/boundary interpolation cases, disk margins, factor algebra,
strict integer threshold and nonnested-array quantifier before claiming it.

Continue only with the stated explicit bound or a precise obstruction;
compare with floor(log gamma) without supplying an unproved bound for H_rho.
No mathematical computation script is needed for these exact identities.

Completed: the canonical statement, full proof, constants, strict threshold
and limitations are in `lemmas/L645-quantitative-vertical-pick-pole-detector.md`.
The Cayley congruence includes singular PSD and purely imaginary data.
The attained comparison at N=floor(log gamma) still requires
lambda_delta N>log A_delta+log^+ H_rho; no such growth estimate or sign
is supplied. Local outcome ADVANCE / REPRODUCTION, pending independent
audit; no result beyond the checked standard machinery is claimed.
