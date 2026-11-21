# Fixed prime-gap probe calculation1118 — working checkpoint

16 November 2026. Authorized target and pre-existing SPECIALIZE coverage:
`drafts/literature/2026-11-16-prime-gap-defect-test-1117.md`.
This is one quantitative specialization, not an RH sign mechanism.

Main gap: L030/L032/C032a actual-Xi algebraic-square positivity in all
degrees; C030b is only finite. Current target quantifies an arithmetic
defect already known qualitatively in Polson v24 Theorem12.2(vi).
Continue only with an explicit positive signal and cubic fixed-strip
norm bound for the prescribed bump, uniformly in g and 0<=B-A<=2.

Partial reasoning to preserve before finishing the proof:
put d=(B-A)/2 in [0,1], m=cosh((4/5)/4)-1>0 and
W_d=chi[cosh(x/4)-cos(dx)]. Then K=2[cosh(x/4)-cos(dx)]cos(gx),
and the requested signal is integral W_d(1+cos(2gx)). Its mean is
at least m. One integration by parts bounds the oscillatory integral
by M/(2g), where M=(cosh(9/40)+1)||chi'||_1+sinh(9/40)/4+1.
Thus proposed explicit c=m/2 and G=max(1000,ceil(M/m)) suffice.
All bump derivatives vanish at endpoints; check all estimates in the
canonical write-up before treating these working notes as established.

For the strip, E(x)=chi(|x|) is smooth, even, supported on two compact
intervals. For r=t+iy, |y|<=3/4, differentiate
exp(-yx)E(x)cos(gx) three times before integrating by parts in t.
The L1 derivative norm is bounded by
2 exp(27/40)(1+g)^3 sum_(j=0)^3 binom(3,j)||chi^(j)||_1.
Use the direct integral bound for |t|<=1 and the third derivative
bound for |t|>1. The proposed strip constant is this coefficient
multiplied by (11/4)^(9/4). Need finish entire phi, inversion and
normalization checks, especially full zero difference=4*signal,
half-pair difference=2*signal, arithmetic measure defect=-2K dx.
No script, numerical quadrature or actual zero selection is needed.

Completion: the full argument and all qualifications are now in canonical
C030c. Both prescribed thresholds hold with the constants above. The
normalizations and entire test-class construction are included there.
This working checkpoint preserves partial reasoning; it is not a second
canonical proof. Separate audit is pending, and PROGRESS.md alone holds
the current next action.
