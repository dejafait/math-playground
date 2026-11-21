# Outer boundary attempt — step403, saved working notes

The following checkpoints preserve reasoning saved before completion.
The full result is now canonical in C999c and remains unaudited; these
notes are historical, not another current next-action record.

Approved target is exactly review401's step-modulus Hardy annihilator
test for the capped two-window sufficient objective. Reuse that EXPLORE
assessment and its separately approved BLS source contracts. No extra
literature search or cross-notebook input is proposed.

Main gap: actual-Xi positivity L030-L032/C032a, L966/L968 forcing and
unpaid L984(H). Intermediate use: an all-polynomial obstruction to the
stronger Delta_n objective would redirect the capped bridge toward
integrated cancellation; it would not bound the integrated E_n below.

Choose the ONE permitted pair lambda=1/4, eta=0, so
h_n(y)=y exp(-n H_J(y)/4), A=(7/16,9/16) in angle. This selection is
fixed before quantitative work; there will be no parameter sweep.
Essential inputs are C997c(4)-(6), C997s's original cap/grid/kernel,
and the BLS Cauchy/outer contracts recorded in review401.

Prospective argument: coefficient cap implies a circle sup bound;
Hardy Cauchy at zero annihilates p_n h_n in the bilinear dtheta pairing.
The expected boundary masses are M_A=1/(16pi) and
M_J=(1-1/(16pi))exp(-n/4). These assertions and all signs still require
proof in a canonical result before they are used.

The load-bearing issue is |P_n|: an absolute upper envelope cannot
establish a lower certificate. A successful attempt must dominate
exp(sqrt(n))*M_J and make T_U*S_n*exp(n/64) unbounded. The exact
C997c upper factor is 18 exp(27/16)(n+2)exp(9n/32), per unit input TV.
The rate threshold for S_n is 19/64, while domination of leakage for
this pair requires a target-action rate strictly below 1/4.

If this one analytic attempt cannot certify those comparisons, retain
the actual unresolved inequality or proved obstruction and park this
family. C997x/y/z and spectral-tail341 stops are preserved. Capped E_n,
C997a(8), selected/both-sign transfer, assay/reconstruction, complements,
regulators, L993, L984(H), forcing and Xi signs remain unresolved.

## Saved analytic reasoning before canonical write-up

Put a=7/16, b=9/16, c=1/2, d=1/16. In the upper rectangle use
L(z)=Log sin((z-a)/2)-Log sin((b-z)/2), with principal logarithms.
The proposed exact identity is H_J(exp(iz))=-i L(z)/pi. Thus the
pairing integrand is exp(iz) exp(n Phi(z)), where
Phi(z)=-(1+7i)z/2+i L(z)/(4pi). The single selected pair is unchanged.

Let u=cos d+7 sin d/(100pi), beta=sin d/(100pi). The upper saddle is
z_0=c-r+iv with cos r cosh v=u, sin r sinh v=beta. Elementary bounds
give 0<v<1/100 and 0<r<d. Along the line Im z=v, the real derivative
to the left of c is -1/2+Q(c-Re z), with
Q(t)=(sin d/(4pi))*sinh v*sin t/
[(cos t*cosh v-cos d)^2+sin(t)^2*sinh(v)^2].
Its derivative has positive numerator: with w=cos t, C=cos d,
H=cosh v, it is -w^3+(H^2+1+C^2)w-2HC, concave on [C,1], with
positive endpoint values C(H-1)^2 and (H-C)^2. Hence z_0 is the
unique horizontal real-part maximum and Re Phi''(z_0)<0.

At the midpoint of that horizontal contour,
Re Phi(c+iv)>-1/4+(7/2-8/pi)v>-1/4+5v/6.
Both vertical endpoint pieces are bounded by exp(-247n/800).
If these signs and branches survive the canonical check, DLMF2.4.15-16
(already within review401's assessed section scope) supplies a nonzero
fixed simple-saddle leading coefficient. This would yield
|P_n| asymptotic to a positive constant times n^(-1/2)exp(n Re Phi(z_0)),
beating exp(sqrt(n)-n/4) leakage. The weighted Delta lower bound would
then grow at rate at least 1/32+5v/6. No result is audited here.

The direct DLMF check in this research step read (iii)'s full analytic,
endpoint and phase hypotheses and (iv)'s equations2.4.14-16 and branch
convention. This checks the precise import inside existing coverage;
it is not a new literature assessment or self-approval of a new target.
