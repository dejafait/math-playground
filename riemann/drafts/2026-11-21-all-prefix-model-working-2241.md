# Fixed all-prefix model working checkpoint2241

21 November 2026. Authorized mathematical specialization under unchanged
assessment2239. This records unfinished assembly, not an audited result.

Main gap: L030-L032/C032a actual-Xi mixed positivity. Test only the fixed
F(z)=exp(-z^2)(2+cos(z))sin(z)/(3z) and its first-n real-pair quotients.
Continue only if every approved obligation holds for all n>=0; preserve
any genuine failed obligation without changing the model.

Candidate construction: g(u)=exp(-u^2/4)/(2 sqrt(pi));
mu=(2/3)delta_0+(1/6)(delta_-1+delta_1);
h_n(u)=4^n(n!)^2 cos(pi u/2)^(2n)/(2(2n)!) on (-1,1), zero outside.
The cited DLMF5.12.5 substitution should give the transform
(n!)^2/[Gamma(n+1+z/pi)Gamma(n+1-z/pi)] of h_n.
Use gamma recurrence/reflection to identify this with sin(z)/(z P_n).
Set f_n=g*mu*h_n. All-n normalization, exact transform, removability,
derivative domination and inversion still need complete written checks.

Planned uniform moment check: g has variance2, mu variance1/3, h_n is
even and supported in [-1,1]. A bound10/3 suffices; finite Taylor
coefficients may give the sharper8/3. No numerical test is needed.
For derivative tails use g^(m)=polynomial_m*g and total compact shift
in [-2,2], not merely Schwartz decay.

Zero/growth obligations: real zeros should be exactly +/-k*pi,
k>=1, simple; z_*=pi+i log(2+sqrt(3)) should survive every removal.
Use the imaginary axis for exact order, with log F_n(ir) expected
r^2+2r-(2n+1)log r+O_n(1). This is order2, whereas actual Xi is order1.
The model cannot settle an order-one bridge or actual-Xi iteration.

Source review2239 and named local stops have been reused. C919m/C919o,
L018/L019/L058 and L262 are scope comparisons, not model premises.
No backend contracts or cross-notebook inputs are imported. No original
claim is made for the already recorded Gaussian-cosine base factor.

Completion2241: the full argument is now canonical in
[C919p](../lemmas/C919p-all-prefix-positive-inverses-order-two-countermodel.md).
All proposed obligations were met, with the sharper second-moment
bound8/3 and explicit removed-root values. This partial checkpoint is
retained as the attempt record; it is not an additional proof. A
separate conceptual audit remains pending, and the Xi/order-one gaps
are unchanged.
