# Fixed-quadratic range working record2030

Approved target: the unchanged assessment2029 SPECIALIZE range screen,
N=6, q=t^2+1/4, alpha>=0, real quintic h, full U_6=T_6/S.
Main gap: actual-family eventual index<=1 in C029m, toward L030-L032.
No claim about hyperbolicity, uniformity or RH is made here.

Before calculation: write U_6=sum b_j t^j and h=sum c_j t^j.
The even coefficient equations necessary for the identity are

    b_0=c_1/4,
    b_2=(1+2alpha)c_1+3c_3/4,
    b_4=(3+2alpha)c_3+5c_5/4,
    b_6=(5+2alpha)c_5.

Thus the following necessary condition covers the full parameter domain:

    F(alpha)=(b_2-4(1+2alpha)b_0)(3+2alpha)(5+2alpha)
             -(3/4)b_4(5+2alpha)+(15/16)b_6=0.

All denominator factors used in backward elimination are positive,
including alpha=0. These equations test a necessary part of the full
identity, not an even replacement of U_6. Odd coefficient equations
may be left unused only if these necessary equations contradict it.

Continuation/abandonment test: reconstruct every full coefficient from
C029n, retain the unchanged proved pi/sqrt(2) 60-decimal intervals,
expand F symbolically before interval evaluation, and test its signs.
A contradiction for all alpha>=0 parks this fixed baseline. A zero-
containing interval or a partial parameter screen remains inconclusive.
No shifted quadratic, higher degree, precision campaign or subsequent
hyperbolicity calculation is authorized by this step.

Completion: every coefficient of the necessary cubic is strictly
negative, excluding all alpha>=0. Full proof and certificate references
are canonical in C029s. All 30 script checks pass. Independent
analytic/weighted-limit and eventual-family assumptions remain unresolved;
the finite proof awaits a separate audit. No further mechanism was tested.
