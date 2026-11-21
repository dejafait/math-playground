# Vertical endpoint working record — step536

Completed record: the full resulting proof is now canonical in
[L804](../lemmas/L804-continued-vertical-theta-mellin-endpoint-bound.md),
awaiting independent conceptual audit. The initial reasoning below is
preserved as written; its then-pending checks are discharged there.

Approved target: the standalone continued vertical endpoint allowance in
`literature/2026-11-05-mellin-vertical-endpoint-test.md`. This is an
unfinished known-method specialization, not yet a verified result.

Using L797/L798/L799/L802, write s=sigma+it, x=u+ih, y=y_L.
For fixed nonzero y, Taylor subtraction with w=2s+1 gives
V(s,y)=sum_{n>=0} p_n exp((2s+n+1)Log(iy))/(2s+n+1).
The only possible poles are s=-(n+1)/2, with residue p_n/2;
D excludes them. Do not assume odd coefficients vanish.

Candidate circle: R=pi/4-13/(224u), strictly above |y| and inside
the theta strip. Direct full-series control appears to give
sup_{|z|<=R}|P(z)|<4*10^9 u^(5/2): use
Re(pi exp(2z))>1/(50u), then compare the Gaussian sum with
integral_0^infinity (v+1)^4 exp(-v^2/(50u)) dv.
All constants and normalizations still require full written checks.

Candidate split: for 0<h<=1/2, y<3/5 and sigma>uQ/4, so the
ordinary ray integral has a strongly negative normalized phase.
For h>1/2, t>uQ/2 pays all Taylor-series denominators, while
sigma>=-Q/14 and log(|x|/y)<log(3u)<=u pay the negative-real-part
loss. The phase factor exp(-pi t) must be retained exactly.
Conjugation supplies h<0. At h=0 the prescribed value is zero;
compatibility as h tends to zero still needs a uniform height check.

No global contour identity, combined budget or sufficient-Xi sign
claim is being attempted. Next within this same attempt: complete the
constant and continuity checks and retain either the full proof or its
precise unresolved failure. No mathematical script has been run.
