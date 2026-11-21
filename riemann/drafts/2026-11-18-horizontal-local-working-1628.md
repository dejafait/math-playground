# Horizontal local audit1628 — preserved working reasoning

Completed 19 November2026: the full reproduction proof is now canonical
in C048c, with its exact fixed-constant certificate under
`scripts/mellin-horizontal-local/`. Independent conceptual audit is pending.
The chronological scratch below is preserved, not an additional theorem.

Approved target: the exact T_loc target in literature assessment1627.
This is a reproduction attempt, not a full Mellin remainder or sign proof.

The proof candidate uses only C048a's branch and C048b's geometry (4)-(5).
Since |w|>9, log|w|>2; the Lambert modulus identity implies U+2<L,
so |w|<L. For V>=0, split V<=4/3 (cos V>=1/9>1/L) and V>4/3.
In the latter case delta=pi/2-V >=atan(V/U)-asin(1/(4L))
> [4/3-4/729-13/50]/L >16/(15L).
Then sin(delta)>1/L by sin(x)>=x-x^3/6 at x=16/(15L)<=4/45.
All inequalities still need full written justification and exact comparisons.

The candidate curvature is A=4p(1+w)/w^2
=2pi exp(w)(1+1/w), so Re A>4r/L^2 and |A|<(160/27)r/L<6r/L.
The branch identity w sqrt(A)/2=sqrt(p(1+w)) follows by the positive
real part of the left side and squaring, and should pay the S phase.

For |s|<=1/(3L), m=|u0+s|>161/36>40/9 and m>L/3.
K=e^(9s/2)/(1+s/u0), |K|<(8/7)(162/161)<29/25.
The resulting quadratic amplitude coefficient is
(29/50)(81/4+81/40+81/800)=12.978225<13.
The cubic coefficient is <=(2656/729)r/L<(73/20)r/L;
the quartic phase remainder is <(3/128+32/17)(r/L)|s|^4<2(r/L)|s|^4.
Thus |Z|<(371/100)(r/L)|s|^3. Four-term residual and odd cancellation
give quadratic13, quartic<22r/L and sextic<8(r/L)^2; its exponential
is absorbed with b_*=(799/300)r/L^2. Gaussian moment normalization
then yields precisely the assessed A_loc. These calculations are
unfinished until the canonical proof and exact constant certificate are saved.

Unresolved independently: lower-power mode1, higher modes, Gaussian
extension, horizontal tails, full remainder, zero count, inversion,
and a sufficient actual-Xi sign bridge. No grid is proof of a uniform bound.
